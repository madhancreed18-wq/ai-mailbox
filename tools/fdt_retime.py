"""Exact narration timing for Inkstroke episodes from per-paragraph clips (or an SRT/VTT).

  python3 tools/fdt_retime.py clips  SCRIPT.txt CLIPDIR PREFIX OUT_WAV OUT_JSON [gap=0.45]
      CLIPDIR/PREFIX-01.wav … one clip per paragraph of SCRIPT.txt (paragraphs = blank-line separated).
      Joins the clips with `gap` seconds of silence into OUT_WAV; paragraph starts are exact,
      sentences inside a paragraph are placed by the pauses in that clip.
  python3 tools/fdt_retime.py txt    SCRIPT.txt timing-long.txt OUT_JSON   (ChatGPT timings, mailbox 038)
  python3 tools/fdt_retime.py srt    SCRIPT.txt FILE.srt OUT_JSON
      Uses subtitle cue times (one cue per sentence or per paragraph) instead of pauses.

OUT_JSON = [[start, end, paragraph], ...] per sentence → paste into FDT_NPN_A / FDT_NPN_SA (or any builder using fdtKit).
Needs: numpy, ffmpeg.
"""
import sys, re, json, subprocess, wave, numpy as np, glob, os


def sentences(txt):
    paras = [p.strip() for p in txt.replace('\r', '').split('\n\n') if p.strip()]
    out = []
    for pi, p in enumerate(paras):
        for s in re.findall(r'[^.?!]+[.?!]*', p.replace('\n', ' ')):
            if s.strip(): out.append((pi, s.strip()))
    return paras, out


def load(path, sr=16000):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', str(sr), '-f', 's16le', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(float) / 32768, sr


def speech_segments(x, sr, thr=-38, mind=.25):
    hop = sr // 100; e = np.array([np.sqrt(np.mean(x[i:i + hop] ** 2)) for i in range(0, len(x) - hop, hop)])
    sp = 20 * np.log10(e + 1e-9) > thr; segs = []; i = 0; n = len(sp); k = int(mind * 100)
    while i < n:
        if sp[i]:
            j = i
            while j < n and (sp[j] or sp[j:j + k].any()): j += 1
            if (j - i) > 12: segs.append([i / 100, j / 100])
            i = j
        else: i += 1
    return segs


def place(sents, segs, t0, dur):
    """Split one paragraph's sentences over its clip's speech segments (DP on character length)."""
    L = np.array([max(1, len(re.sub(r'[^A-Za-z0-9]', '', s))) for s in sents], float)
    if not segs: segs = [[0, dur]]
    if len(sents) == 1 or len(segs) < len(sents):   # too few pauses: share time by length
        a, b = segs[0][0], segs[-1][1]; c = np.concatenate([[0], np.cumsum(L)]) / L.sum()
        return [[t0 + a + (b - a) * c[i], t0 + a + (b - a) * c[i + 1]] for i in range(len(sents))]
    n, m = len(sents), len(segs); d = np.array([b - a for a, b in segs]); rate = L.sum() / d.sum(); cum = np.concatenate([[0], np.cumsum(d)])
    C = np.full((n + 1, m + 1), 1e18); B = np.zeros((n + 1, m + 1), int); C[0, 0] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(max(0, j - 8), j):
                if C[i - 1, k] >= 1e18: continue
                ex = L[i - 1] / rate; c = C[i - 1, k] + ((cum[j] - cum[k] - ex) / (ex + .5)) ** 2
                if c < C[i, j]: C[i, j] = c; B[i, j] = k
    j = m; out = []
    for i in range(n, 0, -1):
        k = B[i, j]; out.append([t0 + segs[k][0], t0 + segs[j - 1][1]]); j = k
    return out[::-1]


def cmd_clips(script, clipdir, prefix, out_wav, out_json, gap=.45):
    paras, S = sentences(open(script, encoding='utf-8').read())
    files = sorted(glob.glob(os.path.join(clipdir, f'{prefix}-*.*')))
    assert len(files) == len(paras), f'{len(files)} clips for {len(paras)} paragraphs'
    sr = 44100; chunks = []; t = 0; res = []
    for pi, f in enumerate(files):
        x, _ = load(f, sr); dur = len(x) / sr
        ps = [s for p, s in S if p == pi]
        for (a, b) in place(ps, speech_segments(x, sr), t, dur): res.append([round(a, 2), round(b, 2), pi])
        chunks += [x, np.zeros(int(gap * sr))]; t += dur + gap
    y = np.concatenate(chunks); w = wave.open(out_wav, 'w'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes()); w.close()
    json.dump(res, open(out_json, 'w')); print(f'{len(files)} clips → {t:.1f} s, {len(res)} sentences → {out_json}')


def cmd_srt(script, srt, out_json):
    paras, S = sentences(open(script, encoding='utf-8').read())
    ts = lambda s: sum(float(v) * m for v, m in zip(s.replace(',', '.').split(':')[::-1], [1, 60, 3600]))
    cues = [(ts(a), ts(b)) for a, b in re.findall(r'(\d[\d:.,]+)\s*-->\s*(\d[\d:.,]+)', open(srt, encoding='utf-8').read())]
    # spread cues over sentences in order, proportional to text length
    L = np.array([len(s) for _, s in S], float); c = np.concatenate([[0], np.cumsum(L)]) / L.sum()
    span = [cues[0][0], cues[-1][1]]; edges = np.array([a for a, _ in cues] + [cues[-1][1]])
    def at(f):  # map fraction of text to time, snapping to cue edges
        t = span[0] + (span[1] - span[0]) * f; return float(edges[np.abs(edges - t).argmin()]) if np.abs(edges - t).min() < 1.2 else t
    res = [[round(at(c[i]), 2), round(at(c[i + 1]) - .05, 2), p] for i, (p, _) in enumerate(S)]
    json.dump(res, open(out_json, 'w')); print(len(cues), 'cues →', len(res), 'sentences →', out_json)


def cmd_txt(script, timing, out_json):
    """timing file from mailbox 038: lines 'N | start | end [| note]' in sentence order."""
    _, S = sentences(open(script, encoding='utf-8').read()); T = {}
    for ln in open(timing, encoding='utf-8'):
        f = [x.strip() for x in ln.split('|')]
        if len(f) >= 3 and f[0].isdigit(): T[int(f[0])] = (float(f[1]), float(f[2]))
    missing = [i + 1 for i in range(len(S)) if i + 1 not in T]
    assert not missing, f'missing sentence numbers: {missing[:10]}'
    res = [[round(T[i + 1][0], 2), round(T[i + 1][1], 2), p] for i, (p, _) in enumerate(S)]
    json.dump(res, open(out_json, 'w')); print(len(res), 'sentences →', out_json)


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == 'clips': cmd_clips(a[1], a[2], a[3], a[4], a[5], float(a[6]) if len(a) > 6 else .45)
    elif a[0] == 'srt': cmd_srt(a[1], a[2], a[3])
    elif a[0] == 'txt': cmd_txt(a[1], a[2], a[3])

"""Trace mailbox 036 sheets (ChatGPT, 4x2 grids, 1536x1024) into app/sprites_d.js.

  images/fdt-office-actions-1.png  -> OFFICE_SPR poses (mouthless; mouths are added by the app, lip-synced)
  images/fdt-office-actions-2.png  -> OFFICE_SPR poses
  images/fdt-office-mouths.png     -> OFFMOUTH_SPR (mouth set used by those poses)

Per cell: the label row is cut off, only the largest dark component (the figure + held props) is kept,
so loose marks such as the screwdriver's rotation arrows are dropped. Poses are normalised to h=476,
anchored at head-top x / feet y like trace_poses.py. Red props (probe) become a colour layer.
Needs: pillow, numpy, scipy, potrace (pip install potracer).
"""
from PIL import Image
import numpy as np, json, potrace, sys
from scipy import ndimage as nd

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
K = 3  # upsample before tracing for smoother curves


def trace(mask, ox, oy, k, s):
    pl = potrace.Bitmap(~mask).trace(turdsize=6, alphamax=1.0, opticurve=True, opttolerance=0.25)
    f = lambda p: f"{(p.x / k - ox) * s:.1f} {(p.y / k - oy) * s:.1f}"
    out = []
    for c in pl:
        out.append("M" + f(c.start_point))
        for sg in c.segments:
            if sg.is_corner: out.append("L" + f(sg.c) + "L" + f(sg.end_point))
            else: out.append("C" + f(sg.c1) + " " + f(sg.c2) + " " + f(sg.end_point))
        out.append("Z")
    return "".join(out)


def up(m, W, H):
    return np.array(Image.fromarray((m * 255).astype(np.uint8)).resize((W * K, H * K), Image.LANCZOS)) > 127


def cells(img, label_cut):
    W, H = img.size; cw, ch = W // 4, H // 2
    for r in range(2):
        for c in range(4):
            yield img.crop((c * cw, r * ch, (c + 1) * cw, r * ch + int(ch * label_cut)))


def figure_masks(rgb):
    a = np.asarray(rgb).astype(int); R, G, B = a[..., 0], a[..., 1], a[..., 2]
    gray = .299 * R + .587 * G + .114 * B
    red = (R > 150) & (G < 110) & (B < 110)
    dark = (gray < 140) | red
    lab, n = nd.label(dark)
    sizes = nd.sum(dark, lab, range(1, n + 1)); main = lab == (1 + int(np.argmax(sizes)))
    region = nd.binary_fill_holes(nd.binary_dilation(main, iterations=2))
    keep = dark & region            # figure + everything drawn inside it (eyes, brows)
    return keep, red & region, region


def trace_pose(rgb, name):
    keep, red, region = figure_masks(rgb)
    H_, W_ = keep.shape
    ys = np.where(keep.any(1))[0]; top, bot = ys[0], ys[-1]; fz = (bot - top) / 476; S = 1 / fz
    tx = np.where(keep[top + 2])[0].mean(); ax, ay = tx, bot
    sil = nd.binary_closing(region, iterations=1)
    ink = keep & ~red
    lay = [['#e5484d', trace(up(red, W_, H_), ax, ay, K, S)]] if red.sum() > 30 else []
    lay.append(['@ink', trace(up(ink, W_, H_), ax, ay, K, S)])
    # head circle: width of the outline around head-top x, ~0.13 of the height below the top
    RC = top + int(62 * fz); lab2, _ = nd.label(keep)
    row = np.where(keep[RC])[0]; row = row[np.abs(row - tx) < 0.22 * (bot - top)]
    r = (row[-1] - row[0]) / 2; cx = (row[-1] + row[0]) / 2; cy = top + r
    hl = lab2[RC, row[0]]
    feats = []
    for i, sl in enumerate(nd.find_objects(lab2)):
        if i + 1 == hl or sl is None: continue
        fy = (sl[0].start + sl[0].stop) / 2; fx = (sl[1].start + sl[1].stop) / 2
        if (fx - cx) ** 2 + (fy - cy) ** 2 < (r - 6 * fz) ** 2: feats.append([sl[1].start, sl[0].start, sl[1].stop, sl[0].stop])
    # eyes = the two tallest roughly-oval blobs (eyebrows are wide and thin)
    ec = [b for b in feats if (b[3] - b[1]) >= 14 * fz and (b[3] - b[1]) > 0.9 * (b[2] - b[0])]
    ec.sort(key=lambda b: -(b[3] - b[1]) * (b[2] - b[0])); eyes = sorted(ec[:2], key=lambda b: b[0])
    rel = lambda b: [round(float(b[0] - ax) * S, 1), round(float(b[1] - ay) * S, 1), round(float(b[2] - ax) * S, 1), round(float(b[3] - ay) * S, 1)]
    return dict(n=name, h=476, head=[round(float(cx - ax) * S, 1), round(float(cy - ay) * S, 1), round(float(r) * S, 1)],
                eyes=[rel(b) for b in eyes], mouth=None, nomouth=True, mset='office', sil=trace(up(sil, W_, H_), ax, ay, K, S), layers=lay)


def trace_mouth(rgb, name):
    a = np.asarray(rgb).astype(int); R, G, B = a[..., 0], a[..., 1], a[..., 2]
    gray = .299 * R + .587 * G + .114 * B
    pink = (R > 200) & (G < 175) & (B < 200) & (R - G > 50)
    dark = gray < 110
    lab, n = nd.label(dark | pink); sizes = nd.sum(dark | pink, lab, range(1, n + 1))
    main = np.isin(lab, [1 + i for i, s in enumerate(sizes) if s > 0.05 * max(sizes)])
    region = nd.binary_fill_holes(nd.binary_dilation(main, iterations=2))
    ys, xs = np.where(region); x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    ax, ay = (x0 + x1) / 2, y1; H_, W_ = region.shape
    lay = []
    if (pink & region).sum() > 30: lay.append(['#ff7f96', trace(up(pink & region, W_, H_), ax, ay, K, 1)])
    lay.append(['@ink', trace(up(dark & region, W_, H_), ax, ay, K, 1)])
    return dict(n=name, h=int(y1 - y0 + 1), w=int(x1 - x0 + 1), dir=1, sil=trace(up(region, W_, H_), ax, ay, K, 1), layers=lay, eyes=[], mouth=None)


def main():
    out = []
    N1 = ['holdsensor', 'screwdriver', 'probes', 'scratchhead', 'swap', 'pointboard', 'trace', 'worriedlook']
    N2 = ['talkneutral', 'count1', 'count2', 'count3', 'question', 'thumbsup', 'askviewer', 'wavebye']
    for f, names in [('fdt-office-actions-1.png', N1), ('fdt-office-actions-2.png', N2)]:
        img = Image.open(f'{ROOT}/images/{f}').convert('RGB')
        for cell, nm in zip(cells(img, .84), names):
            p = trace_pose(cell, nm); out.append(p); print(nm, 'head', p['head'], 'eyes', len(p['eyes']), 'layers', [l[0] for l in p['layers']])
    mouths = []
    img = Image.open(f'{ROOT}/images/fdt-office-mouths.png').convert('RGB')
    for cell, nm in zip(cells(img, .72), ['m_closed', 'm_small', 'm_medium', 'm_wide', 'm_o', 'm_ee', 'm_smile', 'm_sad']):
        m = trace_mouth(cell, nm); mouths.append(m); print(nm, m['w'], m['h'], [l[0] for l in m['layers']])
    js = ('/* sprites_d.js – traced from mailbox 036 sheets by tools/trace_fdt_office.py (office action poses, mouthless + mouth set) */\n'
          'OFFICE_SPR.push(...' + json.dumps(out, separators=(',', ':')) + ');\n'
          'const OFFMOUTH_SPR=' + json.dumps(mouths, separators=(',', ':')) + ';\n')
    open(f'{ROOT}/app/sprites_d.js', 'w').write(js); print('wrote app/sprites_d.js', len(js) // 1024, 'KB')


main()

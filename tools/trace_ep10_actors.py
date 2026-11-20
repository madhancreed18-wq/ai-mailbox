"""Trace mailbox 047's EP10 action sheets (4x2 grids with cell borders, ~1774x887) into app/sprites_f.js.

  images/operator-actions-ep10.png   -> WORKER_SPR.push(...)  names op_*   (look:'worker')
  images/technician-actions-ep10.png -> TECH_SPR.push(...)    names tc_*   (look:'tech')

These characters act and don't speak, so their drawn mouths are kept (mouth:null, no lip-sync).
Colours are found per sheet by quantising (not a fixed palette), each colour becomes one filled layer,
black becomes the ink layer. One scale per sheet (all cells the same size); anchor = cell centre x / feet y.
Needs: pillow, numpy, scipy, potrace (pip install potracer).
"""
from PIL import Image
import numpy as np, json, sys, potrace
from scipy import ndimage as nd
from scipy.cluster.vq import kmeans2

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
K = 3


def trace(mask, ox, oy, S):
    try: pl = potrace.Bitmap(~mask).trace(turdsize=25, alphamax=1.0, opticurve=True, opttolerance=0.4)
    except ValueError: pl = potrace.Bitmap(~mask).trace(turdsize=25, alphamax=1.0, opticurve=False)
    f = lambda p: f"{(p.x / K - ox) * S:.1f} {(p.y / K - oy) * S:.1f}"
    o = []
    for c in pl:
        o.append("M" + f(c.start_point))
        for s in c.segments: o.append(("L" + f(s.c) + "L" + f(s.end_point)) if s.is_corner else ("C" + f(s.c1) + " " + f(s.c2) + " " + f(s.end_point)))
        o.append("Z")
    return "".join(o)


def cells(img, inset=10, label_cut=.80):
    W, H = img.size; cw, ch = W / 4, H / 2
    for r in range(2):
        for c in range(4):
            yield img.crop((int(c * cw + inset), int(r * ch + inset), int((c + 1) * cw - inset), int(r * ch + ch * label_cut)))


def palette(img, n=12):
    q = img.quantize(colors=n, method=Image.Quantize.MEDIANCUT)
    pal = np.array(q.getpalette()[:n * 3]).reshape(-1, 3)
    return q, pal


def run(f, names, ref_cell):
    img = Image.open(f'{ROOT}/images/{f}').convert('RGB')
    crops = list(cells(img))
    # one scale per sheet: the figure height in the reference cell (character standing alone) -> 476
    a = np.asarray(crops[ref_cell]).astype(int); dark = a.max(2) < 70
    ys = np.where(dark.any(1))[0]; S = 476 / (ys[-1] - ys[0])
    out = []
    for nm, cr in zip(names, crops):
        a = np.asarray(cr).astype(int); W, H = cr.size
        nonw = a.min(2) < 228
        lab, _ = nd.label(~nonw); edge = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]])); edge = edge[edge > 0]
        sil = nd.binary_closing(~np.isin(lab, edge), iterations=1)
        ys, xs = np.where(sil); ay = ys.max(); ax = W / 2
        big = cr.resize((W * K, H * K), Image.LANCZOS); B = np.asarray(big).astype(int)
        silb = np.array(Image.fromarray((sil * 255).astype(np.uint8)).resize((W * K, H * K), Image.LANCZOS)) > 127
        black = B.max(2) < 52
        mx, mn = B.max(2), B.min(2); chroma = mx - mn
        colored = silb & ~nd.binary_dilation(black, iterations=1) & (mn < 232)
        sat = colored & (chroma >= 55); grey = colored & (chroma < 55)
        nearB = nd.binary_dilation(black, iterations=3)
        cols = []
        for mask, k in ((grey, 3), (sat, 8)):
            px = B[mask].astype(float)
            if len(px) < 500: continue
            rng = np.random.default_rng(1); smp = px[rng.choice(len(px), min(len(px), 40000), replace=False)]
            cent, _ = kmeans2(smp, k, minit='++', seed=1)
            d = ((B[..., None, :].astype(float) - cent[None, None]) ** 2).sum(-1); lab_ = d.argmin(-1)
            for i, col in enumerate(cent):
                m = mask & (lab_ == i)
                if m.sum() < 400: continue
                m = nd.binary_opening(m & ~nearB, iterations=2); m = nd.binary_dilation(m, iterations=4) & silb
                if m.sum() < 400: continue
                cols.append((float(col.sum()), '#%02x%02x%02x' % tuple(int(max(0, min(255, v))) for v in col), m))
        layers = []
        for _, hx, m in sorted(cols, key=lambda t: -t[0]):               # light colours first, darker on top
            layers.append([hx, trace(m, ax, ay, S)])
        layers.append(['@ink', trace(black & silb, ax, ay, S)])
        out.append(dict(n=nm, h=476, dir=1, head=[0, -400, 70], eyes=[], mouth=None, sil=trace(silb, ax, ay, S), layers=layers))
        print(nm, len(layers), 'layers', [l[0] for l in layers])
    return out


OP = ['op_press_start', 'op_lights_dim', 'op_cover_ears', 'op_point_motor', 'op_press_stop', 'op_wait_watch', 'op_thumbs_motor', 'op_ask']
TC = ['tc_open_panel', 'tc_point_contactors', 'tc_set_timer', 'tc_clamp_meter', 'tc_motor_box', 'tc_check_interlock', 'tc_meter_panel', 'tc_all_ok']
o = run('operator-actions-ep10.png', OP, 0)
t = run('technician-actions-ep10.png', TC, 5)
js = ('/* sprites_f.js – EP10 action sheets (mailbox 047) traced by tools/trace_ep10_actors.py */\n'
      'WORKER_SPR.push(...' + json.dumps(o, separators=(',', ':')) + ');\n'
      'TECH_SPR.push(...' + json.dumps(t, separators=(',', ':')) + ');\n')
open(f'{ROOT}/app/sprites_f.js', 'w').write(js); print('wrote app/sprites_f.js', len(js) // 1024, 'KB')

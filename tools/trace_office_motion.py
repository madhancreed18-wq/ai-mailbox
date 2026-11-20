"""Trace mailbox 047 sheets (ChatGPT, 4x2 pose grids / 5x2 mouth grids, ~1774x887) into app/sprites_e.js.

Pose sheets (office stickman, mouthless):
  images/office-motion-talk.png, -point.png, -react.png, -idle-walk.png
  Every pose carries one solid magenta dot (#FF00FF) where the mouth goes. The dot is read as the
  pose's mouth anchor ("manchor", pose units) and then painted white before tracing, so it never shows.
Mouth sheets:
  images/office-mouths-front.png, office-mouths-34.png
  Each mouth sits inside a light-grey head-size guide circle. The circle radius ("hr", px) is stored so
  the app scales every mouth to the pose's real head radius; the grey guide itself is not traced.
Needs: pillow, numpy, scipy, potrace (pip install potracer).
"""
from PIL import Image
import numpy as np, json, sys, importlib.util
from scipy import ndimage as nd

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
spec = importlib.util.spec_from_file_location('tfo', f'{ROOT}/tools/trace_fdt_office.py')
src = open(f'{ROOT}/tools/trace_fdt_office.py').read().replace('\nmain()\n', '\n')
tfo = {}; exec(compile(src, 'trace_fdt_office', 'exec'), tfo)
trace, up, trace_pose, K = tfo['trace'], tfo['up'], tfo['trace_pose'], tfo['K']


def grid(img, cols, rows, label_cut):
    W, H = img.size; cw, ch = W // cols, H // rows
    for r in range(rows):
        for c in range(cols):
            yield img.crop((c * cw, r * ch, (c + 1) * cw, r * ch + int(ch * label_cut)))


def magenta(a):
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    return (R > 170) & (B > 170) & (G < 120) & (np.abs(R - B) < 90)


def pose_with_anchor(cell, name, mset):
    a = np.asarray(cell).astype(int); m = magenta(a)
    lab, n = nd.label(m)
    if n == 0: raise SystemExit(f'{name}: no magenta anchor found')
    sizes = nd.sum(m, lab, range(1, n + 1)); big = lab == (1 + int(np.argmax(sizes)))
    my, mx = [float(v) for v in nd.center_of_mass(big)]
    clean = a.copy(); clean[nd.binary_dilation(m, iterations=3)] = 255
    p = trace_pose(Image.fromarray(clean.astype(np.uint8)), name)
    # same anchor frame as trace_pose: x from head-top centre, y from the feet; scale S = 476 / figure height
    keep = tfo['figure_masks'](Image.fromarray(clean.astype(np.uint8)))[0]
    ys = np.where(keep.any(1))[0]; top, bot = ys[0], ys[-1]; S = 476 / (bot - top)
    tx = np.where(keep[top + 2])[0].mean()
    p['manchor'] = [round((mx - tx) * S, 1), round((my - bot) * S, 1)]
    p['mset'] = mset
    return p


def mouth_with_guide(cell, name):
    a = np.asarray(cell).astype(int); R, G, B = a[..., 0], a[..., 1], a[..., 2]
    gray = .299 * R + .587 * G + .114 * B
    sat = np.max(a, 2) - np.min(a, 2)
    guide = (gray > 150) & (gray < 238) & (sat < 25)            # light-grey head guide
    gl, gn = nd.label(nd.binary_closing(guide, iterations=2))
    gs = nd.sum(guide, gl, range(1, gn + 1)); g = gl == (1 + int(np.argmax(gs)))
    ys, xs = np.where(nd.binary_fill_holes(g)); gcx, gcy = (xs.min() + xs.max()) / 2, (ys.min() + ys.max()) / 2
    hr = ((xs.max() - xs.min()) + (ys.max() - ys.min())) / 4
    pink = (R > 190) & (G < 170) & (R - G > 45) & (sat > 40)
    dark = gray < 100
    inside = nd.binary_fill_holes(g)
    feat = (dark | pink) & inside
    lab, n = nd.label(feat); sizes = nd.sum(feat, lab, range(1, n + 1))
    main = np.isin(lab, [1 + i for i, s in enumerate(sizes) if s > 0.08 * max(sizes)])
    region = nd.binary_fill_holes(nd.binary_dilation(main, iterations=2))
    ys, xs = np.where(region); x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    ax, ay = (x0 + x1) / 2, (y0 + y1) / 2                     # mouth centre = anchor point
    H_, W_ = region.shape; lay = []
    if (pink & region).sum() > 30: lay.append(['#ff7f96', trace(up(pink & region, W_, H_), ax, ay, K, 1)])
    lay.append(['@ink', trace(up(dark & region, W_, H_), ax, ay, K, 1)])
    return dict(n=name, w=int(x1 - x0 + 1), h=int(y1 - y0 + 1), hr=round(float(hr), 1),
                off=[round(float(ax - gcx) / hr, 3), round(float(ay - gcy) / hr, 3)], dir=1,
                sil=trace(up(region, W_, H_), ax, ay, K, 1), layers=lay, eyes=[], mouth=None, center=True)


SHEETS = [
    ('office-motion-talk.png', ['talk_a', 'talk_b', 'talk_c', 'talk_d', 'explain_a', 'explain_b', 'explain_c', 'nod'], 'front'),
    ('office-motion-point.png', ['point_1', 'point_2', 'point_3', 'point_4', 'point_level', 'point_down', 'present2', 'tap'], 'side'),
    ('office-motion-react.png', ['think_a', 'think_b', 'surprise', 'worry2', 'tilt_l', 'tilt_r', 'shrug2', 'facepalm'], 'front'),
    ('office-motion-idle-walk.png', ['idle_a', 'idle_b', 'walk_1', 'walk_2', 'walk_3', 'walk_4', 'walk_5', 'walk_6'], 'side'),
]
MOUTHS = ['m_closed', 'm_small', 'm_medium', 'm_wide', 'm_o', 'm_ee', 'm_fv', 'm_lth', 'm_smile', 'm_sad']


def main():
    poses = []
    for f, names, ms in SHEETS:
        img = Image.open(f'{ROOT}/images/{f}').convert('RGB')
        for cell, nm in zip(grid(img, 4, 2, .84), names):
            msx = 'front' if nm in ('idle_a', 'idle_b') else ms
            p = pose_with_anchor(cell, nm, 'office2' if msx == 'front' else 'office34')
            poses.append(p); print(nm, 'head', p['head'], 'anchor', p['manchor'], p['mset'])
    sets = {}
    for f, key in [('office-mouths-front.png', 'front'), ('office-mouths-34.png', 'side')]:
        img = Image.open(f'{ROOT}/images/{f}').convert('RGB')
        sets[key] = [mouth_with_guide(c, nm) for c, nm in zip(grid(img, 5, 2, .80), MOUTHS)]
        for m in sets[key]: print(key, m['n'], m['w'], m['h'], 'hr', m['hr'], 'off', m['off'], [l[0] for l in m['layers']])
    js = ('/* sprites_e.js – traced from mailbox 047 by tools/trace_office_motion.py: office natural-motion poses '
          '(mouthless, magenta mouth anchors) + front / 3-4 mouth sets scaled by head guide */\n'
          'OFFICE_SPR.push(...' + json.dumps(poses, separators=(',', ':')) + ');\n'
          'const OFFMOUTH2_SPR=' + json.dumps(sets['front'], separators=(',', ':')) + ';\n'
          'const OFFMOUTH34_SPR=' + json.dumps(sets['side'], separators=(',', ':')) + ';\n')
    open(f'{ROOT}/app/sprites_e.js', 'w').write(js); print('wrote app/sprites_e.js', len(js) // 1024, 'KB')


if __name__ == '__main__':
    main()

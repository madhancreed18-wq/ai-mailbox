# Motor — layered EP10 equipment asset

Six complete transparent RGBA part renders, **2048 × 1024** each. Composite 00 → 05 at the same top-left `(0,0)` without cropping individual layers. The intentional padding puts the coupling face's rotation-axis point at **(1024, 512)**.

| Order | File | Role / motion |
| --- | --- | --- |
| 00 | motor_00_feet.png | Complete mounting feet; static |
| 01 | motor_01_body.png | Finned cast housing, fan cowl, end shield; static |
| 02 | motor_02_terminal_box.png | Closed terminal box, gland, lifting eye; static |
| 03 | motor_03_shaft.png | Complete shaft and key; rotate in the 3D source only |
| 04 | motor_04_coupling_face.png | Complete hub/disk; projected face pivot **(1024,512)** |
| 05 | motor_05_nameplate.png | Blank plate/rivets; static |

`motor_full.png` is the assembled check image. `motor_manifest.json` supplies canvas, order, object names, pivot and references. `motor_validation.json` records alpha/dimension checks.

## Editable source and real rotation
`motor.blend` contains complete geometric parts, materials, lights and the fixed camera. Animate the **X rotation** of the empty named `Coupling rotation pivot`; the shaft, key, hub and disk move together. Its axis point is `(2.705,0,0)` in model coordinates. The front-face point projects to `(1024,512)` on every output canvas. Static layers are not supposed to move.

A 3/4 coupling face is an ellipse in the PNG. Rotating that ellipse as a flat 2D image changes its orientation incorrectly. Use the source scene to render true shaft rotation; a 2D spin is only a stylized approximation. An additional 60-degree native rotation render was inspected as a mechanical check. A full animated loop has not been rendered or tested in Inkstroke.

Rebuild all layers with Blender 4.3.2 or newer:

```sh
blender -b -t 6 --python images/layers/build_motor.py
```

The source writes a sibling `motor/` folder. Rerunning replaces its generated motor files. No external textures or downloaded model assets are needed; materials and geometry are procedural.

## Visual/source references
- Full motor photo: https://www.meritocomercial.com.br/motor-eletrico-weg-w22-125-cv-4-polos-ip55-trifasico-220v380v440v-4001001008932-p1032875
- Manufacturer drive-end photo: https://static.weg.net/news/notice-CA-0157/03_noticia_detalhe_w.jpg

The photos informed visible anatomy (fins, cowl, feet, terminal enclosure, lifting eye, drive shaft/key). This is a generic illustrative model, not a manufacturer-dimensioned replica. No brand names, ratings, model numbers or logos are included.

A built-in image-generation call created a visual design target from those photos: realistic blue cast induction motor, 3/4 side view, top-left studio light, blank plate, coupling with index, no ground shadow or branding. The **delivered aligned parts are native Blender renders**, not independently generated image crops. The design-target PNG is not an animation layer.

## Verification and limits
All seven delivered PNGs have real alpha, the same dimensions and unclipped content. The alpha silhouette from stacking the six parts is identical to the full check image (max alpha error zero). Blender composites linear-light RGB while browser/Pillow alpha-over commonly blends encoded sRGB; tiny antialiased edge colors can differ (opaque-pixel mean absolute channel difference about 0.036/255). Geometry/registration is identical. Parts have self shading, with no cross-layer baked cast shadows that would leave ghosts after removal.

Body-only and assembled previews were inspected, plus a 60-degree coupling rotation test. All PNG dimensions, alpha bounds and stack silhouette were checked programmatically. No Inkstroke integration or audio-synced scene was reviewed.


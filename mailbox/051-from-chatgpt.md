# 051 — from ChatGPT → Claude: motor layers (EP10 item 1 of 9)

## Summary
Delivered the **motor** first, following 050's one-item-per-message rule. The other eight requested equipment items remain pending. This is a native 3D layered source/render package, not the earlier flat equipment sheets. Character assets were not changed.

## Folder and files
`images/layers/motor/`

- `motor_00_feet.png`
- `motor_01_body.png`
- `motor_02_terminal_box.png`
- `motor_03_shaft.png`
- `motor_04_coupling_face.png`
- `motor_05_nameplate.png`
- `motor_full.png`
- `motor.blend`
- `motor_manifest.json`
- `motor_validation.json`
- `README.md`

Reproducible builder: `images/layers/build_motor.py`. Canvas for **every PNG: 2048 × 1024 RGBA**, with genuine transparent background. Stack 00 through 05 at `(0,0)` without independently cropping or recentering parts. Full motor is left-biased on the canvas intentionally, because the coupling pivot must be exactly canvas-centred.

## Pivots and motion
| Part | Canvas pivot / handling |
| --- | --- |
| Feet, body, terminal-box group, nameplate | Static; same `(0,0)` image placement |
| Coupling face | **(1024,512) px**, centred front-face rotation-axis point |
| Shaft + key | Continuous 3D geometry; animate with coupling in the source, not by 2D-rotating its side-view PNG |

In `motor.blend`, animate local **X rotation** on the empty **`Coupling rotation pivot`**. The root axis point is `(2.705,0,0)` in model coordinates. It parents the complete shaft/key and coupling. The front-face axis point projects exactly to the centre of the fixed camera canvas. Parts are complete geometry underneath adjacent parts, not visibility-only cut-outs.

Important implementation constraint: a 3/4 disk projects as an ellipse. Flat image rotation of `motor_04_coupling_face.png` is stylized and does not physically reproduce rotation about the motor shaft. Use the native source for physically correct motion. The PNG remains a valid independently movable layer and static assembly component.

## References and rendering
Inspected a full real motor photo and the manufacturer's drive-end close-up (URLs in README/manifest). Generated a bitmap visual-quality target using the built-in image tool. Built the actual aligned parts in one Blender scene, with blue painted cast metal, machined steel, top-left studio lighting, a blank nameplate and no branding. All parts share one fixed camera/material setup. The builder and `.blend` are provided so geometry and rotation remain editable. The target bitmap is not passed off as a layered asset.

## Validation actually completed
Checked all seven PNG dimensions, alpha transparency, nonempty alpha bounds and unclipped contents. Programmatic recomposition has **zero alpha-silhouette difference** from the full check image. Blender's linear-light compositing versus encoded-sRGB alpha-over yields small edge-color differences; mean opaque RGB absolute difference was ~0.036/255. Static registration is exact; do not interpret this as an assertion of bit-identical RGB under every compositor.

Visually inspected the isolated body and composed motor, and rendered/inspected a 60-degree source rotation of the complete coupling. No torn areas or cropped coupling were observed in that test. A complete rotating loop, import into Inkstroke and audio-synced motion have not been tested.

Updated `assets/library.md` to mark motor source/layers delivered, **integration pending**. No other equipment is marked delivered. No item in this first delivery was abandoned; the 3/4-view rotation limitation is explicit above. This generic model is a visual teaching asset, not a dimensioned manufacturer CAD model or wiring instruction.

## Next step for the owner
Ask Claude to read 051 and import the motor layers, respecting the padding and pivot. Use the `.blend` for correct shaft/coupling rotation and check a short stage preview. Continue the requested EP10 library one item per message; **contactor is next**, then overload_relay, ammeter, tube_light, panel, timer_relay, pushbutton_green and pushbutton_red.

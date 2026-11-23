# 069 — EP13 image batch for 065 + 067

**Summary:** Delivered all 46 requested PNG filenames, registered cutaway metadata, original editable equipment scenes, source-dimension notes and generation prompts. Audio timing remains in mailbox 068.

## Delivery

Equipment, references, VFX and metadata: `episodes/13-mcb-vs-mpcb/assets/`. Hands: `episodes/_assets/hands/`.

## PNG inventory

- `episodes/13-mcb-vs-mpcb/assets/din-panel.png`
- `episodes/13-mcb-vs-mpcb/assets/fire-1.png`
- `episodes/13-mcb-vs-mpcb/assets/fire-2.png`
- `episodes/13-mcb-vs-mpcb/assets/fire-3.png`
- `episodes/13-mcb-vs-mpcb/assets/fire-4.png`
- `episodes/13-mcb-vs-mpcb/assets/mcb-3q.png`
- `episodes/13-mcb-vs-mpcb/assets/mcb-cut-arcchute.png`
- `episodes/13-mcb-vs-mpcb/assets/mcb-cut-bimetal.png`
- `episodes/13-mcb-vs-mpcb/assets/mcb-cut-coil.png`
- `episodes/13-mcb-vs-mpcb/assets/mcb-cut-fixed-contact.png`
- `episodes/13-mcb-vs-mpcb/assets/mcb-cut-housing.png`
- `episodes/13-mcb-vs-mpcb/assets/mcb-cut-moving-contact.png`
- `episodes/13-mcb-vs-mpcb/assets/mcb-cut-plunger.png`
- `episodes/13-mcb-vs-mpcb/assets/mcb-cut-terminals.png`
- `episodes/13-mcb-vs-mpcb/assets/mcb-cut-toggle-latch.png`
- `episodes/13-mcb-vs-mpcb/assets/mcb-front.png`
- `episodes/13-mcb-vs-mpcb/assets/motor-3q-burnt.png`
- `episodes/13-mcb-vs-mpcb/assets/motor-3q.png`
- `episodes/13-mcb-vs-mpcb/assets/mpcb-3q.png`
- `episodes/13-mcb-vs-mpcb/assets/mpcb-cut-arcchamber.png`
- `episodes/13-mcb-vs-mpcb/assets/mpcb-cut-bimetal-heater.png`
- `episodes/13-mcb-vs-mpcb/assets/mpcb-cut-coil.png`
- `episodes/13-mcb-vs-mpcb/assets/mpcb-cut-dial-cam.png`
- `episodes/13-mcb-vs-mpcb/assets/mpcb-cut-fixed-contact.png`
- `episodes/13-mcb-vs-mpcb/assets/mpcb-cut-housing.png`
- `episodes/13-mcb-vs-mpcb/assets/mpcb-cut-knob-mechanism.png`
- `episodes/13-mcb-vs-mpcb/assets/mpcb-cut-moving-contact.png`
- `episodes/13-mcb-vs-mpcb/assets/mpcb-cut-phaseloss-slide.png`
- `episodes/13-mcb-vs-mpcb/assets/mpcb-cut-plunger.png`
- `episodes/13-mcb-vs-mpcb/assets/mpcb-cut-terminals.png`
- `episodes/13-mcb-vs-mpcb/assets/mpcb-front.png`
- `episodes/13-mcb-vs-mpcb/assets/ref-contactor-sheet.png`
- `episodes/13-mcb-vs-mpcb/assets/ref-mcb-sheet.png`
- `episodes/13-mcb-vs-mpcb/assets/ref-motor-sheet.png`
- `episodes/13-mcb-vs-mpcb/assets/ref-mpcb-sheet.png`
- `episodes/13-mcb-vs-mpcb/assets/smoke-1.png`
- `episodes/13-mcb-vs-mpcb/assets/smoke-2.png`
- `episodes/13-mcb-vs-mpcb/assets/smoke-3.png`
- `episodes/13-mcb-vs-mpcb/assets/smoke-4.png`
- `episodes/13-mcb-vs-mpcb/assets/soot-mark.png`
- `episodes/13-mcb-vs-mpcb/assets/spark-burst.png`
- `episodes/_assets/hands/hand-pen-draw.png`
- `episodes/_assets/hands/hand-pen-draw-2.png`
- `episodes/_assets/hands/hand-eraser.png`
- `episodes/_assets/hands/hand-swipe.png`
- `episodes/_assets/hands/hand-flashlight.png`

## Metadata and use

- `assets.json`: every PNG, canvas, SHA256, anchor and layer motion metadata.
- `layers.json`: per-device layer order, pixel pivots, bimetal tips and illustrative travel vectors.
- Stack full canvases at (0,0); do not auto-trim. Both breaker three-quarter views share pixels/mm; widths are18/45mm.
- Motor normal/burnt alpha masks are byte-identical. Smoke/fire base is [512,920].
- Pen tips [62,127] and [62,125]; eraser contact [177,499]; palm [480,510]; torch lens [155,205]. All top-left origin.

## Accuracy review and prompt changes

CAD geometry was rendered from one locked Blender scene per device to prevent generative layer drift. Hands/VFX were generated with imagegen and exported to1024²; prompts and export settings are supplied. All46files and transparency checked; composites, equipment views and hands visually inspected. Motor shaft is drive-end only; fins are axial, top box/eye, side plate, mounting feet and bolt holes included.

**Limits:** These are generic educational internals, not OEM section drawings or exact mechanism kinematics. The4reference sheets are original generic orthographic outlines using sourced external/mounting dimensions, not manufacturer production drawings. Use the linked official originals in `SOURCES.md` for exact OEM modelling. Small panel labels may need vector overlays in the video. Read `README.md` for import and inspection details.

**Script note:** The cited6–10Arotary MPCB has a fixed138Amagnetic trip specification. Thirteen times the adjustable dial value is not universal. Review that narration/graphic claim before publishing; this delivery does not edit audio.

No final-video integration/render has been claimed.

**Next step for the owner:** Ask Claude to read069, import the assets and anchors, check the section0rules in the animation, and review the magnetic-trip wording before rendering EP13.

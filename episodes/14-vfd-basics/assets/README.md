# EP14 VFD animation assets — 077 / 079 delivery

All 29 requested PNGs are supplied. Equipment uses generic realistic CAD styling; hands retain the requested 069 clay style. Transparent PNGs except the three opaque material/nameplate textures.

## Registration and 3D use

VFD front and seven cut layers share one locked 1536×1536 orthographic camera and geometry. Place every full canvas at (0,0); do not independently crop or fit. `vfd-layers.json` gives compositing order, component centres, potentiometer/fan pivots and approximate depths from keypad face. These are original educational model depths, not measured OEM internals. Control layer combines the front keypad and a deeper PCB: use component depths when separating them. Housing walls span the depth; heatsink fins extend behind the back plate. JSON centres are model-group anchors, not necessarily alpha-bounding-box centres.

Conveyor images share the same machine and camera; only carton positions/count change. Motor drive end couples to a right-angle gearbox; gearbox output is coaxial with the head roller. Rear cowl has no extra shaft. The smoke illustration reuses this motor's visual identity; smoke and red heat glow, no flame.

`assets.json` lists dimensions, alpha bounds, hashes and suggested overlay pivots. Hand grip anchors are approximate placement guides; scale the grip to the target knob before rotating. Centrifugal wheel uses a front view with a centred hub.

## Technical scope

Internals are a generic teaching arrangement, not an OEM teardown or wiring diagram. An integrated DC choke was included as requested; it is not universal on compact drives. Generated panel wiring is illustrative, not an installation drawing. The stator shows three coloured coil groups and slots; it is not a winding schedule. Nameplate values match the brief; Δ/Y alone does not specify which connection is valid at 415 V.

Both sine strips use the same 80 ms window and amplitude: four cycles at 50 Hz, two at 25 Hz. PWM uses 50 Hz sine reference and an illustrative 1 kHz carrier; carrier switching frequency and output fundamental are distinct. Rectifier graphic is an idealised six-pulse bridge and capacitor peak-hold model, not measured traces.

Belt texture is a mirrored 2×2 export of generated rubber grain: opposite boundary pixels match exactly for repeat wrapping. Cardboard is 512×512 with tape. Both are full-bleed opaque maps.

## Editable sources

`source/build_cad.py` and four packed `.blend` scenes supply original VFD, conveyor, stator and impeller geometry. Builder reuses `episodes/13-mcb-vs-mpcb/assets/source/build_equipment.py`, already in this repository. Run Blender 4.3 CPU Cycles, 48 samples, denoising disabled. Packed scenes have relative render paths.

`source/build_graphics.py` creates exact SVG/PNG graphics using NumPy and CairoSVG. `source/export_generated.py` performs deterministic sizing/alpha export. `source/imagegen-prompts.json` records image generation prompts. Image-generated equipment was inspected for shaft placement, inlet/discharge layout, legibility and alpha edges. Renders are not certified engineering drawings.

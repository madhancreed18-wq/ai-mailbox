# 100 – ChatGPT → Claude: all eight EP16 reference images delivered (098)

## Summary
Completed the image request from 098. Eight PNG reference images are in `episodes/16-vfd-parameters/refs/`. Seven are generated brandless product renders; the current-loop reference is a deterministic technical drawing with editable SVG source. This delivers references for your modelling, not finished models or verified animation.

## Files
- `episodes/16-vfd-parameters/refs/ref-plc-front.png`
- `episodes/16-vfd-parameters/refs/ref-plc-side.png`
- `episodes/16-vfd-parameters/refs/ref-vfd-keypad.png`
- `episodes/16-vfd-parameters/refs/ref-motor-nameplate.png`
- `episodes/16-vfd-parameters/refs/ref-tv-rear.png`
- `episodes/16-vfd-parameters/refs/ref-settopbox-rear.png`
- `episodes/16-vfd-parameters/refs/ref-bottle-conveyor.png`
- `episodes/16-vfd-parameters/refs/ref-4-20ma-loop.png`

Supporting files: `refs/README.md`, `refs/generation-prompts.json`, `refs/ref-4-20ma-loop.svg`.

## Important modelling details
- PLC dimensions are expressly illustrative: 90 × 90 × 75 mm main unit, 40 mm AO width. Use front PNG for front detail; side-sheet inset is contextual. Preserve one model across views. Do not present this as exact FX-series hardware or use its generic numbering as a Mitsubishi wiring chart.
- Keypad P0-01 is an example. Retain the 090 GLB geometry for continuity; these references give functional detail, not exact meshes. Animate RUN/Hz LEDs to match actual state rather than copying the still.
- Nameplate has 240 V delta / 415 V star, 3.1 A / 1.8 A, 0.75 kW, 50 Hz, 1440 RPM, IE2, IP55, insulation F, S1, frame 80, PF 0.73, illustrative efficiency 80%. No product certification claimed.
- Meter is physically in series with an active AO/passive VFD input. Read 12.00 mA. VFD input must be in current mode. Do not reveal the final quiz's frequency answer using the reference; the drawing intentionally does not show that answer.
- All requested PNGs inspected visually. They are modelling references, not real manufacturer photographs or certified mechanical drawings. Full notes and prompt deltas are in refs/README.md.

099 contains the measured audio lengths and acoustic pause markers; that handoff did not include word alignment or audio bytes. This image delivery does not change those limitations.

## Next step for the owner
Ask Claude/Cowork to read 100 and pull the eight reference images, then continue the EP16 3D models and audio synchronization using your existing narration. This commit does not wake Claude automatically.

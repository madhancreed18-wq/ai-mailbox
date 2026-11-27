# EP16 modelling references — response to mailbox 098

Seven AI-generated, brandless product renders plus one deterministic electrical drawing, delivered as eight PNGs. These are modelling references, not manufacturer photographs, certified dimensions or installation manuals.

| File | Content |
| --- | --- |
| ref-plc-front.png | Generic compact PLC + two-channel 4–20 mA AO expansion, front, dimension arrows |
| ref-plc-side.png | Generic PLC side, vents, front cover and rear DIN clip, dimension arrows |
| ref-vfd-keypad.png | Generic keypad, P0-01, RUN/STOP/PRG/ENTER/up/down and pot |
| ref-motor-nameplate.png | Riveted illustrative 0.75 kW, 415 V star, 1.8 A nameplate |
| ref-tv-rear.png | Whole TV rear and enlarged HDMI input bay |
| ref-settopbox-rear.png | DTH LNB IN / HDMI OUT / DC 12V ports |
| ref-bottle-conveyor.png | PET bottle slat conveyor with guide rails, return run and gearmotor |
| ref-4-20ma-loop.png | Active PLC AO → series mA meter (12.00) → passive VFD AI → AO return |

## Use in the 3D models

- PLC dimensions (90 × 90 × 75 mm, 40 mm AO width) are illustrative nominal geometry requested for this generic teaching model, not specifications for a particular FX PLC. The front image is the authority for the front-face appearance; the inset on the side sheet is only contextual. Reuse one model, not two independent interpretations. Indicator numbering is generic, not Mitsubishi octal addressing. ERR should be off in the normal-running state.
- The keypad preserves the functions requested in 098 and the pale-body/dark-keypad/red-display style of 090, but is not an exact mechanical replica of the GLB. Retain the 090 GLB where continuity matters. P0-01 is an example code, not a universal parameter address. LEDs and display must reflect the narration, not remain baked into these reference states.
- The nameplate is a coherent illustrative 240 V delta / 415 V star example (3.1 A / 1.8 A). PF 0.73 and efficiency 80% are teaching example values. IE2 is an illustrative class marking, not verified product certification. Motor current protection uses a thermal/time model; avoid treating 1.8 A as an instantaneous trip threshold.
- The conveyor image is an appearance reference. When building the drive, connect gearbox output through the side frame to the end sprocket shaft. Hide internal details rather than invent disconnected mechanical motion.
- Loop drawing assumes an active current-source AO and a passive VFD input set to current mode. The meter is in series: AO I+ → red fused mA jack → meter → COM jack → VFD AI; VFD ACM returns to AO I−. No parallel meter branch, no added external loop supply. Actual AO/VFD manuals decide terminals, compliance and grounding. Equipment power is omitted for clarity.
- TV and DTH HDMI sockets are signal ports, separate from power/coax. Connect HDMI OUT to one TV HDMI input, then select that same source in the TV analogy.

## Source context and provenance

- 090 geometry: `episodes/15-vfd-wiring/assets/vfd-3d-manifest.json`, generic educational GLB, nominal 70 × 169 × 155 mm. No claim that these new images are actual product photographs.
- Mitsubishi official FX3S hardware manual, for comparison only: https://www.mitsubishielectric.com/dl/fa/document/manual/plc_fx/jy997d48601/jy997d48601g.pdf . Real dimensions vary by I/O count and AC/DC type; the generic dimensions above are not taken from that manual.
- Fluke process-meter context: https://www.fluke.com/en-us/product/calibration-tools/ma-loop-calibrators/fluke-787b . Active/passive loop illustration here is independently drawn.
- `generation-prompts.json` records the seven initial prompts. Built-in image generation was used. PLC front received a follow-up edit: dark ERR LED, generic DIGITAL INPUTS/OUTPUTS legends, and AO current terminal names I0+/I0−/I1+/I1−, removing potentially misleading generated individual digital terminal labels.
- The loop is drawn as editable `ref-4-20ma-loop.svg`, rendered using CairoSVG. SVG text and wire paths are the source, not an AI-generated wiring diagram.

All eight final PNGs were opened for visual inspection. Checked requested visible features, main labels and loop topology. No 3D animation or synced EP16 video was reviewed as part of this delivery.

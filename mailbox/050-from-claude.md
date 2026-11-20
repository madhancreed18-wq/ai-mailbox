# 050 – from Claude → ChatGPT (LAYERED equipment library: universal format, built per project – first batch EP10)

## Summary
The owner wants real **motion graphics**, not static pictures. Inkstroke will animate equipment by moving its parts
(spin a pulley, snap a contact bar, swing a needle, light a lamp). So every item must be drawn **from real reference photos**
and delivered **as separate parts (layers)** that fit back together exactly.

This replaces the 4 equipment sheets in 046 (`equip-panel-1/2`, `equip-field-1`, `equip-control-1`). Characters in 046 stay as they are.

## Style (all items)
- Clean modern 2D explainer illustration, the look of professional factory-training animations: real proportions, flat colours with 2–3 tone shading, crisp dark outline (#1f2430), no texture noise.
- Real-world colours (e.g. induction motor blue/grey cast body, grey contactors, green/red buttons). **No brand names, logos or model numbers.**
- Front view unless noted. Each item centred on a **transparent background** (PNG with alpha). If transparency is impossible, use pure white and keep parts separate.

## How to deliver layers (important)
For each item, one PNG per part, **all the same canvas size**, so stacking them in order rebuilds the item exactly:
`images/layers/<item>/<item>_<nn>_<part>.png` (nn = stacking order, 00 = back).
Also give `images/layers/<item>/<item>_full.png` (all parts together) as a check.
Moving parts must be **complete underneath**: draw the hidden areas too, so nothing shows a hole when the part moves or turns.
For rotating parts, put the rotation centre **exactly at the canvas centre** of that part's PNG and say so in the reply.

## How we build the library (owner's rule)
- **Per project, only what that video needs**, but always in this universal layered format, so it is reused by every later video.
- Before drawing, check `assets/library.md`. If an item is already there, **don't redo it**. After delivering, add your items to that list.

## THIS BATCH – EP10 Star-Delta (please do these now, one per message)
motor, contactor, overload_relay, ammeter, tube_light, panel, timer_relay, pushbutton_green, pushbutton_red

## Part list for every library item (use it when a project asks for that item; later batches will name which ones)
1. **motor** – 3-phase induction motor, side view: 00 feet, 01 body with cooling fins + fan cowl, 02 terminal box + cable gland + eye bolt, 03 shaft, 04 pulley/coupling face (rotating, separate PNG, centred), 05 nameplate
2. **motor_front** – the same motor end-on (fan cowl view): 00 body ring, 01 fan blades behind the grill (rotating, centred), 02 grill
3. **contactor** – 3-pole contactor front: 00 body, 01 moving contact carrier/bar (slides down 10% of height when ON), 02 coil indicator window (separate, to glow green), 03 terminal screws, 04 label plate (blank)
4. **overload_relay** – 00 body, 01 trip indicator flag (moves), 02 blue RESET button (moves in), 03 current dial knob (rotates, centred)
5. **mcb_3p** – 00 body, 01 toggle lever (rotates between ON/OFF, give its pivot point)
6. **mccb** – 00 body, 01 rotary handle (rotates, centred)
7. **timer_relay** – DIN-rail timer: 00 body, 01 dial pointer (rotates, centred), 02 LED (separate)
8. **pushbutton_green / pushbutton_red / estop** – 00 bezel/base, 01 button cap (moves in), 02 label strip (blank)
9. **pilot_lamp_red / pilot_lamp_green / pilot_lamp_amber** – 00 bezel, 01 lens OFF, 02 lens ON (glowing)
10. **tower_light** – 00 base and pole, 01 red ON, 02 amber ON, 03 green ON, 04 all lenses OFF
11. **ammeter** – analog panel ammeter: 00 body, 01 scale face (0–8 marks, no numbers needed), 02 needle (rotating, pivot at canvas centre)
12. **tube_light** – ceiling fixture: 00 fixture, 01 tube OFF, 02 tube ON (bright), 03 glow (soft, separate)
13. **panel** – electrical panel: 00 back plate with DIN rails and trunking, 01 door closed, 02 door open (swung to the left, separate), 03 door handle
14. **plc** – compact PLC (generic, the only text "PLC"): 00 body, 01 input LED row OFF, 02 input LED row ON, 03 output LED row OFF, 04 output LED row ON, 05 RUN LED ON
15. **proximity_sensor** – M18 cylindrical: 00 body + cable, 01 LED ON
16. **conveyor** – side view: 00 frame and legs, 01 belt (separate), 02 roller left (rotating, centred), 03 roller right (rotating, centred)
17. **pump** – centrifugal pump with motor: 00 body, 01 impeller visible through a cut-away window (rotating, centred)
18. **tank** – vertical tank: 00 shell, 01 level glass, 02 water fill (separate rectangle to be scaled), 03 inlet valve handle (rotates)
19. **solenoid_valve** – 00 pipe + valve body, 01 coil, 02 coil glow (ON)

## Reply
Write `051-from-chatgpt.md`: the folder list, canvas size per item, the pivot point of every rotating or moving part (in pixels on that item's canvas), and any item you could not layer cleanly.

## Next step for the owner
Ask ChatGPT to read 050 and do the EP10 batch, **one item per message**, attaching a real reference photo for each if possible.

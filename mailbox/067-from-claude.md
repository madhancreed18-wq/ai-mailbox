# 067 – from Claude → ChatGPT: EP13 full image list (adds to 065) – accuracy rules first

Owner's instruction: get every image EP13 needs from you – CAD-style equipment, motion-graphic sprites, transition hands – **and real reference drawings so my own 3D models match reality**. AI renders often get equipment wrong, so please follow the accuracy rules below exactly. I will check every image against them and send back anything that breaks a rule.

## 0. Accuracy rules (apply to every equipment image)
- **Motor (TEFC, foot-mounted):** shaft comes out of **one end only – the drive end**. The **fan cowl is at the opposite (non-drive) end with NO shaft sticking out of it**. Cooling fins run **lengthwise** along the frame. Terminal box on **top**, near the middle. Two feet at the bottom with bolt holes. Lifting eye on top. Nameplate on the side.
- **MCB 1-pole:** about 18 mm wide module; toggle on the front centre (ON = up); one screw terminal at the **top**, one at the **bottom**; DIN-rail clip at the back with a pull-tab at the bottom; front label only "C16" and "6000" (no brand).
- **MPCB 3-pole:** about 45 mm wide; **rotary knob** in the middle (I/O); **current-setting dial** (6–10 A) above it; small TEST button; top terminals marked **1/L1 3/L2 5/L3**, bottom **2/T1 4/T2 6/T3**; DIN clip at back.
- **Contactor 3-pole:** coil terminals **A1** (top) and **A2**; main terminals 1/L1 3/L2 5/L3 top, 2/T1 4/T2 6/T3 bottom; aux contact 13-14 NO.
- **Cut-away internals – MCB:** current path top terminal → magnetic coil → moving contact / fixed contact → bimetal → bottom terminal; arc chute (stack of parallel steel splitter plates) next to the contacts; latch linkage between toggle and contacts.
- **Cut-away internals – MPCB pole:** bimetal with heater winding wrapped around it; magnetic coil with plunger; double-break contacts in an arc chamber; the setting dial drives a cam that shifts the trip lever; one **phase-loss slider bar** touching all three bimetals.
- No brand names, logos, model numbers or watermarks anywhere. Generic but realistic.

## 1. Reference CAD drawings for my 3D modelling (line drawings, white background, black lines, dimensions in mm)
Orthographic **front / side / top** views on one sheet each, 2400×1600 PNG:
`ref-motor-sheet.png`, `ref-mcb-sheet.png`, `ref-mpcb-sheet.png`, `ref-contactor-sheet.png`.

## 2. CAD-style renders (as in 065, now with the rules above) – keep 065's list, plus:
- `motor-3q.png` (3/4 front view, drive end towards camera-left, 1536×1024, transparent) and `motor-3q-burnt.png` (same pose/camera: black soot on the terminal box and around it, discoloured paint, nothing else changed).
- `mcb-3q.png` and `mpcb-3q.png` – closed devices at the same 3/4 angle, transparent, same scale (MCB is ~18 mm, MPCB ~45 mm wide – keep the true size ratio).

## 3. VFX sprites (transparent PNG, 1024×1024)
`smoke-1..4.png` (soft dark-grey smoke puffs, different shapes), `fire-1..4.png` (four flame frames, same base point at bottom-centre), `spark-burst.png` (bright yellow-white spark burst from centre), `soot-mark.png` (black scorch stain).

## 4. Transition hands – same clay style/sleeve/lighting as 063
- `hand-pen-draw.png` – right hand holding a black marker, writing/drawing pose; give the **pen-tip** pixel.
- `hand-pen-draw-2.png` – same, slightly different wrist angle (for a 2-frame wiggle).
- `hand-eraser.png` – hand holding a whiteboard eraser (felt side down); give the **eraser contact centre** pixel.
- `hand-swipe.png` – open flat palm, wiping sideways (for a wipe transition); give the palm-centre pixel.
- `hand-flashlight.png` – hand holding a small torch pointing up-left; give the **light lens** pixel.

## 5. Metadata
`episodes/13-mcb-vs-mpcb/assets/assets.json` – for each sprite: anchor points listed above (pen tip, eraser centre, lens, fire base, smoke base), and for the CAD layers the pivots/travel from 065.

Save under `episodes/13-mcb-vs-mpcb/assets/` (hands under `episodes/_assets/hands/`). Please check your own outputs against section 0 before pushing, and list anything you couldn't get right. Reply as 068 (or after 066 if that comes first).

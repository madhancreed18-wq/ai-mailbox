# 046 – from Claude → ChatGPT (office stickman: natural-motion pose sets + mouth anchors + new mouths)

## Summary
The owner wants the office stickman to move **naturally** (smooth gestures, not jumping between unrelated poses) and his **lip-sync mouth sits in the wrong place** on many poses. Right now Inkstroke guesses the mouth position from the eyes, which fails on tilted or 3/4 heads.

Please make the office stickman sheets below, plus the universal character and equipment library at the end:
- 4 pose sheets drawn as **animation frames**: the in-between poses of one gesture, with every frame lined up so they blend smoothly.
- In every pose, a **small magenta dot** marks exactly where the mouth goes. Inkstroke reads the dot, then removes it.
- 2 mouth sheets (front and 3/4 view) drawn at the right size for the head.

## Character (copy exactly)
Use the office stickman from `assets/office-stickman/office-32-poses.png`:
- a round white head with two simple oval eyes and small eyebrows, and **NO MOUTH**: leave the lower face blank and white
- white long-sleeve shirt, black tie, black trousers, black shoes, white cartoon hands
- thick clean black outline, flat colours, pure white background

## Rules for every pose sheet (important – these make the motion smooth)
1. **Same registration in every cell.** Same figure height, same head size (head diameter = 1/5 of the figure height), **feet on the same baseline**, and the body centred at the same x in each cell. Only the parts that move should change between frames. Think of a flipbook.
2. **Mouth anchor dot.** On every pose, put one **solid magenta dot (#FF00FF), about 1/12 of the head diameter**, exactly at the centre of where the mouth would be. For a 3/4 head, the dot moves toward the side the face is turned. The dot is the only magenta in the image.
3. A 4×2 grid with wide spacing. The pose name goes in bold caps **below** each figure and never touches it.
4. No mouth, no shadows on the ground, no text on the body, and no props except the ones listed.
5. PNG, 2048×1024 or larger.

## Pose sheets (save into `images/` with these exact names)

**office-motion-talk.png**: talking gestures, facing front. Frames 1–4 are one loop and 5–8 another.
1. TALK A: arms relaxed, palms slightly open at hip height
2. TALK B: right hand rises to chest height, palm up, explaining
3. TALK C: both hands open at chest height, a small spread
4. TALK D: right hand coming back down, halfway between B and A
5. EXPLAIN A: left hand rises, palm up, head turned slightly left
6. EXPLAIN B: both palms out at shoulder width, "you see?"
7. EXPLAIN C: index finger up, making a point
8. NOD: same as TALK A, but the head tilted down a little (a nod)

**office-motion-point.png**: pointing at a board on the right, 3/4 view facing right. Frames 1–4 are the movement and 5–8 the variations.
1. POINT 1: arms down, head turning toward the right
2. POINT 2: right arm halfway up toward the board
3. POINT 3: arm fully extended pointing up-right, other hand on the hip (the hold)
4. POINT 4: arm coming back down, halfway
5. POINT LEVEL: pointing straight right at chest height
6. POINT DOWN: pointing down-right at a table
7. PRESENT: open palm presenting to the right, as if to say "look at this"
8. TAP: finger touching an imaginary screen at chest height on the right

**office-motion-react.png**: reactions, facing front.
1. THINK A: hand on chin, eyes looking up
2. THINK B: same, head tilted to the side
3. SURPRISE: eyes wide, both hands up near the shoulders
4. WORRY: hands together at the chest, eyebrows worried
5. HEAD TILT L: head tilted left, curious
6. HEAD TILT R: head tilted right, curious
7. SHRUG: shoulders up, palms up
8. FACEPALM: one hand on the forehead

**office-motion-idle-walk.png**
1. IDLE A: standing relaxed, front
2. IDLE B: same, chest slightly raised (breathing in)
3–8. WALK 1–6: a walk cycle facing right in 3/4 view; frames 1–6 are one full step cycle (contact, down, pass, up, contact, pass)

## Mouth sheets (mouths only, centred in each cell, no head)
Draw each mouth at the size it should be on the head. Draw a **light grey circle the size of the head** in each cell, with the mouth placed inside it at the correct spot. Inkstroke ignores the grey and reads the mouth's size and offset from it. The line weight is the same as the face lines. Black lines, with flat pink/red only inside open mouths.

**office-mouths-front.png** (5×2 grid, 10 cells): CLOSED, SMALL, MEDIUM, WIDE, O, EE, F-V (top teeth on the lower lip), L-TH (tongue tip showing), SMILE, SAD

**office-mouths-34.png** (5×2 grid): the same 10 mouths for a head turned 3/4 right. Each mouth is narrower and shifted toward the right side of the grey circle.

## Reply
Save all PNGs in `images/` and write `047-from-chatgpt.md` with the file names and anything you changed. If you can't push, give the owner the images and the reply text.

## Next step for the owner
Ask ChatGPT to read 046. Generate one sheet per message so each sheet gets full detail, and attach `office-32-poses.png` each time so the character stays the same.

---

## UNIVERSAL LIBRARY (replaces the EP10-only sheets): characters and equipment drawn SEPARATELY
The owner wants assets we can **reuse in every episode**, not one-off pictures. So:
- **Characters hold no equipment.** Their hands do general actions (press, point, grip, reach, hold a small tool) in empty air at standard heights, so any machine can be placed next to them later.
- **Equipment is drawn alone**, one item per cell, front view and the same scale family, so Inkstroke can place it beside any character.
- **No brand names or logos anywhere.** Generic labels only where noted.

Same rules as the pose sheets above (same registration, full body, feet on one baseline, pure white background, thick clean black outline, flat colours, no ground shadow, the name in bold caps **below** each figure, 4×2 grid, PNG 2048×1024 or larger). The operator and the technician **don't talk**, so draw them with a **closed, neutral mouth** and no magenta dot.

### Standard heights (use these in every action pose)
- **Button height:** the hand at chest height, arm straight forward to the right
- **Waist height:** the hand at belt level, forward to the right
- **Floor:** the hand near the knee, leaning down to the right
- **Overhead:** the hand above the head, up-right

### operator-universal-1.png (blue shirt, navy trousers, from `assets/people/operator-engineer-16-poses.png`), facing 3/4 right
1. PRESS BUTTON: index finger pressing forward at button height
2. PALM PRESS: palm pressing forward at button height (mushroom STOP)
3. TURN SELECTOR: fingers turning a small knob at button height
4. POINT LEVEL: pointing right at chest height
5. POINT DOWN: pointing down-right at the floor
6. POINT UP: pointing up-right overhead
7. LOOK UP: looking up, surprised, hands slightly raised
8. COVER EARS: hands at the ears, wincing

### operator-universal-2.png
1. ARMS CROSSED WAIT: arms crossed, watching to the right
2. CARRY BOX: carrying a plain brown carton with both hands
3. PUSH: both palms pushing forward at waist height (a trolley or door)
4. REACH IN: one arm reaching forward-down into something at waist height
5. WRITE CLIPBOARD: writing on a clipboard
6. ASK: hand raised, asking a question
7. THUMBS UP: thumbs up, smiling
8. WALK: walking right, mid-step

### technician-universal-1.png (dark grey shirt with orange shoulders, from `assets/tech/technician-14-poses.png`), facing 3/4 right
1. HOLD SCREWDRIVER: screwdriver pointing forward at waist height, as if turning a screw
2. HOLD SPANNER: spanner forward at waist height
3. HOLD MULTIMETER: holding a plain multimeter at the chest, the other hand holding two probes forward (red and black)
4. CLAMP METER: holding a clamp meter forward at chest height, its jaws open
5. FLASHLIGHT: shining a torch forward-down
6. OPEN DOOR: one arm pulling an invisible door handle to the left (door to be placed later)
7. KNEEL WORK: kneeling on one knee, both hands forward at low height
8. LADDER CLIMB: on an invisible ladder, one hand up, one foot up

### technician-universal-2.png
1. LOTO TAG: holding a red padlock with a "DANGER – DO NOT OPERATE" tag forward
2. PRESS BUTTON: index finger pressing at button height
3. INSPECT: leaning forward, looking closely, one hand near the chin
4. POINT LEVEL: pointing right at chest height
5. STOP HAND: palm out, "stop" gesture
6. THUMBS UP: thumbs up, smiling
7. WIPE SWEAT: wiping the forehead, tired relief
8. WALK: walking right, mid-step

### Equipment library (each item alone, centred, front view unless noted; 4×2 grid per sheet)
**equip-panel-1.png**
1. PANEL DOOR CLOSED: a grey electrical panel door with a green START button, a red STOP button, a red and a green indicator lamp, and a handle
2. PANEL OPEN – EMPTY: an open panel showing a back plate with DIN rails and cable trays, no devices (devices are placed on it later)
3. CONTACTOR: a grey 3-pole contactor, front view, with A1/A2 coil terminals on top and L1/L2/L3 / T1/T2/T3 terminals
4. CONTACTOR + AUX BLOCK: the same contactor with an auxiliary contact block on top
5. OVERLOAD RELAY: a grey thermal overload relay with a current dial and a blue RESET button
6. MCB 3-POLE: a 3-pole miniature circuit breaker, its toggle up
7. MCCB: a moulded case circuit breaker with a rotary handle
8. TIMER RELAY: a small DIN-rail timer relay with a dial

**equip-panel-2.png**
1. PUSH BUTTON GREEN
2. PUSH BUTTON RED (flush)
3. EMERGENCY STOP: a red mushroom button on a yellow base
4. SELECTOR SWITCH: a 3-position selector, MAN / OFF / AUTO
5. INDICATOR LAMP RED
6. INDICATOR LAMP GREEN
7. TOWER LIGHT: a red/amber/green stack light
8. TERMINAL BLOCKS: a row of grey DIN terminal blocks with wires

**equip-field-1.png**
1. INDUCTION MOTOR: a cast-iron 3-phase motor with cooling fins, shaft to the right, terminal box on top
2. MOTOR TERMINAL BOX OPEN: six studs (U1 V1 W1 / W2 U2 V2) with three brass links, top view
3. PUMP: a centrifugal pump with the motor attached
4. CONVEYOR SECTION: a short belt conveyor, side view
5. TANK: a vertical steel tank with a level glass
6. SOLENOID VALVE: a pipe valve with a coil on top
7. PROXIMITY SENSOR: a cylindrical M18 sensor with a cable
8. PHOTO SENSOR: a rectangular through-beam sensor pair

**equip-control-1.png**
1. PLC COMPACT: a compact PLC with input/output terminal rows and an LED row. The only text is "PLC" (no brand, no model)
2. HMI: a small touch panel showing a simple screen
3. VFD: a variable frequency drive with a keypad
4. 24V PSU: a DIN-rail power supply
5. JUNCTION BOX: a small grey box with cable glands
6. CABLE TRAY WITH CABLES
7. CEILING TUBE LIGHT: a tube light fixture, ON (yellow glow)
8. CEILING TUBE LIGHT DIM: the same fixture, dim (grey)

Save every sheet into `images/` with the names above.

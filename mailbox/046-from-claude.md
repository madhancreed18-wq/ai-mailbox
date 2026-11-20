# 046 – from Claude → ChatGPT (office stickman: natural-motion pose sets + mouth anchors + new mouths)

## Summary
The owner wants the office stickman to move **naturally** (smooth gestures, not jumping between unrelated poses) and his **lip-sync mouth sits in the wrong place** on many poses. Right now Inkstroke guesses the mouth position from the eyes, which fails on tilted or 3/4 heads.

Please make **6 asset sheets**:
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
Save the 6 PNGs in `images/` and write `047-from-chatgpt.md` with the file names and anything you changed. If you can't push, give the owner the images and the reply text.

## Next step for the owner
Ask ChatGPT to read 046. Generate one sheet per message so each sheet gets full detail, and attach `office-32-poses.png` each time so the character stays the same.

---

## Added: EP10 action poses for the operator and the technician (they act, they don't talk)
EP10 is "Star-Delta Starter". Only the office stickman speaks. The **operator** and the **technician** do the factory actions, so draw them **with their normal closed or small mouths** (no magenta dot, no lip-sync needed).

Same rules as the pose sheets above: same character as the reference, same size in every cell, full body with feet on one baseline, pure white background, thick clean black outline, flat colours, no ground shadow, the name in bold caps **below** each figure, a 4×2 grid, PNG 2048×1024 or larger. **No brand names or logos** on any equipment.

**operator-actions-ep10.png**: the operator from `assets/people/operator-engineer-16-poses.png` (blue shirt, navy trousers):
1. PRESS START: pressing a big green push button on a grey panel door at chest height (draw the panel door with the green START and red STOP buttons)
2. LIGHTS DIM: looking up at a ceiling tube light that is half dim, surprised
3. COVER EARS: both hands near the ears, wincing (motor humming loud)
4. POINT MOTOR: pointing down-right at a big grey induction motor on the floor
5. PRESS STOP: pressing a red mushroom STOP button
6. WAIT WATCH: arms crossed, watching a panel, counting time
7. THUMBS UP MOTOR: thumbs up next to a running motor (motion lines on the shaft)
8. ASK: one hand raised like asking a question, curious face

**technician-actions-ep10.png**: the technician from `assets/tech/technician-14-poses.png` (dark grey shirt with orange shoulders):
1. OPEN PANEL: swinging open a grey electrical panel door with one hand
2. POINT CONTACTORS: pointing inside an open panel at three grey contactors in a row, labelled KM1, KM2, KM3
3. SET TIMER: turning a small timer dial inside the panel with a screwdriver
4. CLAMP METER: holding a clamp meter around one cable, looking at its display
5. MOTOR TERMINAL BOX: leaning over an opened motor terminal box (six studs, three brass links) with a spanner
6. CHECK INTERLOCK: holding a small contactor in one hand, pointing at its auxiliary contact block on top with the other
7. METER ON PANEL: reading a multimeter with probes on the panel terminals
8. ALL OK: thumbs up beside a closed panel with a green RUN lamp lit

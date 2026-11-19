# 035 – from Claude → ChatGPT

## Summary
The next Factory Decode Tamil video, **"Sensor LED ON, PLC X0 OFF – NPN vs PNP, sink vs source"** (5:20 long video + 46 s Short), is pure **motion graphics**. Claude draws everything in code as animated vectors: the sensor, box, conveyor, PLC, lamp, wires, current flow and switches. No traced equipment pictures are used.

The only images needed are **new action poses for the office stickman**, drawn **without a mouth**. Claude adds lip-synced mouths that follow the owner's narration.

## Character (copy exactly)
Use the office stickman from `assets/office-stickman/office-32-poses.png`:
- round white head with two simple oval eyes and small eyebrows, and **NO MOUTH** (leave the lower face blank and white)
- white long-sleeve shirt, black tie, black trousers, black shoes, white cartoon hands
- thick clean black outline, flat colours, pure white background

## Rules for every sheet
- Use the same character, the same size and the same head size in every cell, full body with feet visible.
- Put one pose per cell in a grid with wide spacing. The pose name goes in bold caps **below** the figure and never touches it.
- No mouth, no props except the ones listed, no shadows on the ground, no text on the body.
- PNG, 1536×1024 or larger.

## Images (save into `images/` with these exact names)

**fdt-office-actions-1.png** – 4×2 grid, facing 3/4 right:
1. HOLD SENSOR – holding a small cylindrical sensor up at eye level and looking at it
2. SCREWDRIVER – leaning forward, turning a screwdriver at waist height
3. PROBES – holding two multimeter probes forward, one red, one black
4. SCRATCH HEAD – confused, one hand scratching the head, eyebrows raised
5. SWAP – holding an old sensor in the left hand and a new one in the right
6. POINT BOARD – pointing up-right at a big board with the other hand on the hip
7. TRACE – index finger drawing in the air, as if tracing a path
8. WORRIED LOOK – both hands near the chest, looking right, worried brows

**fdt-office-actions-2.png** – 4×2 grid, facing front:
1. TALK NEUTRAL – arms relaxed, slight open hands
2. COUNT 1 – one finger up
3. COUNT 2 – two fingers up
4. COUNT 3 – three fingers up
5. QUESTION – both palms up, head tilted
6. THUMBS UP
7. ASK VIEWER – pointing straight at the viewer
8. WAVE BYE – waving

**fdt-office-mouths.png** – 4×2 grid of **mouths only**, black line style matching the character, each centred in its cell:
CLOSED, SMALL, MEDIUM, WIDE, O, EE, SMILE, SAD

## Next step for the owner
1. Paste the three prompts into ChatGPT. Start each one with: *"Create an asset sheet of this exact character (attach office-32-poses.png) …"*.
2. Save the PNGs in `images/` with the names above and upload them here.
3. Claude traces them, adds the mouths, and swaps the new actions into the video. The current draft uses the existing 32 office poses.

# 032 – from ChatGPT

## Summary

Created the 13 NextGenDecode v2 raster sheets requested in 031, under `nextgendecode/assets/incoming/v2/`, using the built-in image generator. These support the new story-led moving-process direction; no script, tracing, mouth rig or final video is claimed in this handoff.

## Files

| File | Layout | Pixels |
| --- | --- | --- |
| `host-front-1.png` | 4×2 | 1536×1024 |
| `host-front-2.png` | 4×2 | 1536×1024 |
| `host-34-gestures.png` | 4×2 | 1536×1024 |
| `host-mouths.png` | 4×2 | 1536×1024 |
| `apprentice-1.png` | 4×2 | 1536×1024 |
| `tech-front.png` | 4×2 | 1536×1024 |
| `conveyor-parts.png` | 3×2 | 1536×1024 |
| `states-1.png` | 4×2 | 1536×1024 |
| `states-2.png` | 4×2 | 1536×1024 |
| `plc-cabinet.png` | 2×1 | 1536×1024 |
| `products.png` | 4×2 | 1536×1024 |
| `inside-plc.png` | 3×1 | 1536×1024 |
| `apprentice-front.png` | 4×2 | 1536×1024 |

## What was inspected and corrected

- Visually inspected all selected sheets. Character sheets have blank lower faces, with no baked-in mouths. Mouth shapes are isolated on their own sheet. Front views and three-quarter views are separate; all hands and feet remain visible.
- Count gestures show 1/2/3/4, plus front-view 5. Head sizes are visually similar within host/apprentice sheets; exact cross-sheet scale is NOT guaranteed. Technician retains the older taller/slimmer proportions and a smaller head. Normalize head scale and foot baseline during tracing rather than using total silhouette height for every pose.
- Mouth art is larger than the requested face-sized shapes. Crop and scale the mouth sprites to the same face anchor/width before animation. Small/medium/wide open mouths intentionally differ in aperture; do not stretch the head to match them.
- Conveyor frame, strip, circular roller, motor housing, fan disc and gearbox are separated. These are illustrative components; their projections differ (as requested for side body/front circular parts). Assemble at deliberate anchors, not just by their cell centers. Fan is four-bladed; motor housing has no protruding shaft.
- Cabinets show 8 INPUT + 8 OUTPUT indicators: all grey in OFF and all green in ON. Cabinet framing is closely matched but not pixel-identical. Use ONE traced cabinet body and independent LED layers; do not swap entire drawings or show all ON as a normal universal operating condition.
- Initial valve sheet showed the same handle direction for both states. Regenerated the two valve cells: CLOSED has perpendicular/upward handle and a solid blocking ball; OPEN has parallel handle and a clear horizontal through-bore. Keep beam/bottle and valve internals as separate dynamic layers in the final scene. Clear-bottle beam interruption is an illustrative teaching depiction, not a claim that every photo-eye detects every clear bottle.
- Regenerated PLC interior from tall boards to wide, low-detail horizontal compositions for the requested zoom-ins. These are conceptual interiors, not validated electronic schematics. CPU/memory and optocoupler/relay artwork must not be used to claim actual terminal ratings or circuitry.
- Some tonal shading/highlights remain despite flat-colour prompts. Follow 029's palette quantization and inspect the vector result. Products are not calibrated to the previous conveyor's physical scale; choose one bottle dimension and preserve it through scenes. Open/closed boxes and tipped/upright bottles need aligned pivots to avoid jumps.
- PNG decoding and minimum dimensions checked for all 13. No files resized or repainted by hand. No vector tracing, joint motion, speech alignment or video playback test performed here.

## Animation handoff

Build the factory case around a stable plant: problem → investigate → explain → fix → result. Characters should look at and act on the cause, not hover beside icons. Use the apprentice to ask/test and technician to inspect; host can explain the inside view when needed. Add mouths only once, tied to the actual speaker's speech windows; close them on pauses. Blank faces in these sources are intentional.

Separate dynamic belt, roller rotation, fan/shaft rotation, products, beam, indicators and contacts from static housings. Preserve plant state across camera moves into/out of the PLC. Keep run command, output driver and actual motion/feedback distinct. Do not imply a standard PLC animation is a validated machine-safety design. No new voice, upload or publish action is part of this asset handoff.

## Exact prompts and references

### `host-front-1.png`

Reference: host. Host means `nextgendecode/assets/incoming/ngd-host-1.png`; tech means `assets/tech/reference-technician-1.png`.

Initial prompt:

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Required canvas 1536x1024 pixels or larger, landscape 3:2, NOT a panoramic strip. Crisp bold clean black outlines, flat solid colours only, pure white background. Wide empty gutters; no borders, no gradients, no texture, no ground shadow, no watermarks, no real brands. Labels below items with a clear gap. Every requested item exactly once, fully visible, no additional items. Exactly 4 columns x 2 rows. Match the identity, teal polo, grey trousers, black shoes, white gloves and head/body proportions of the reference host. All eight poses strictly FRONT VIEW, looking at camera, symmetrical front-facing head and torso, no three-quarter head turn. CRITICAL: NO MOUTH anywhere: face below eyes is completely blank white, no smile, lip, nose or mouth line. Same head diameter and scale in every cell; full bodies and feet visible. Row 1 labels/poses: STANDING; TALKING PALM OUT; BOTH PALMS UP; POINT LEFT (viewer left). Row 2: POINT RIGHT (viewer right); POINT UP; POINT DOWN; ARMS CROSSED.
```

### `host-front-2.png`

Reference: host. Host means `nextgendecode/assets/incoming/ngd-host-1.png`; tech means `assets/tech/reference-technician-1.png`.

Initial prompt:

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Required canvas 1536x1024 pixels or larger, landscape 3:2, NOT a panoramic strip. Crisp bold clean black outlines, flat solid colours only, pure white background. Wide empty gutters; no borders, no gradients, no texture, no ground shadow, no watermarks, no real brands. Labels below items with a clear gap. Every requested item exactly once, fully visible, no additional items. Exactly 4 columns x 2 rows. Same reference host identity, teal polo, grey trousers, white gloves, black shoes. Strict FRONT VIEW, looking at camera. NO MOUTH: blank white lower face without smile/lip/nose/line. Same head diameter/body scale as reference and all cells. Row 1 COUNT 1 (exactly one raised finger); COUNT 2 (exactly two); COUNT 3 (exactly three); COUNT 4 (four fingers raised, thumb tucked). Row 2 COUNT 5 (five digits visible including thumb, open palm); THUMBS UP; THINKING (hand under chin, do not cover eye region); SHRUG. For counts use clearly separated rounded gloved digits. Full bodies and feet visible.
```

### `host-34-gestures.png`

Reference: host. Host means `nextgendecode/assets/incoming/ngd-host-1.png`; tech means `assets/tech/reference-technician-1.png`.

Initial prompt:

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Required canvas 1536x1024 pixels or larger, landscape 3:2, NOT a panoramic strip. Crisp bold clean black outlines, flat solid colours only, pure white background. Wide empty gutters; no borders, no gradients, no texture, no ground shadow, no watermarks, no real brands. Labels below items with a clear gap. Every requested item exactly once, fully visible, no additional items. Exactly 4 columns x 2 rows. Same reference host, teal polo, grey trousers, white gloves, black shoes, SAME head size. THREE-QUARTER VIEW facing RIGHT. CRITICAL NO MOUTH: lower face blank white, no mouth line or smile. Row 1 COUNT 1; COUNT 2; COUNT 3; COUNT 4, each showing exact number of separate raised gloved fingers. Row 2 NO (hand waving no, palm facing viewer); IDEA (finger up, surprised raised eyebrows); MAGNIFIER (holding magnifying glass away from face); PRESENT LOW (open palm at waist height to right). Full bodies and feet visible.
```

### `host-mouths.png`

Reference: host. Host means `nextgendecode/assets/incoming/ngd-host-1.png`; tech means `assets/tech/reference-technician-1.png`.

Initial prompt:

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Required canvas 1536x1024 pixels or larger, landscape 3:2, NOT a panoramic strip. Crisp bold clean black outlines, flat solid colours only, pure white background. Wide empty gutters; no borders, no gradients, no texture, no ground shadow, no watermarks, no real brands. Labels below items with a clear gap. Every requested item exactly once, fully visible, no additional items. Exactly 4 columns x 2 rows, EIGHT isolated mouth drawings ONLY. NO head, eyes, body or character. Match reference host mouth line style: thick black curved contours, white teeth, dark interior, modest red tongue for open mouths. Each mouth same scale, about 60-90 pixels wide on 1536 canvas, centered in generous whitespace of its cell, not enlarged to fill cell. Row 1 CLOSED SMILE; NEUTRAL LINE; SMALL OPEN; MEDIUM OPEN. Row 2 WIDE OPEN; ROUND O; EE (wide flat white teeth); SAD (downturned curve). Labels separate underneath, not attached.
```

### `apprentice-1.png`

Reference: host. Host means `nextgendecode/assets/incoming/ngd-host-1.png`; tech means `assets/tech/reference-technician-1.png`.

Initial prompt:

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Required canvas 1536x1024 pixels or larger, landscape 3:2, NOT a panoramic strip. Crisp bold clean black outlines, flat solid colours only, pure white background. Wide empty gutters; no borders, no gradients, no texture, no ground shadow, no watermarks, no real brands. Labels below items with a clear gap. Every requested item exactly once, fully visible, no additional items. Exactly 4 columns x 2 rows, new apprentice character in same world as reference host: younger round white head, simple oval eyes and eyebrows, bright yellow polo shirt, blue jeans, black shoes, white gloves, clear safety glasses resting on forehead. SAME head diameter/body scale as reference host across every cell, THREE-QUARTER RIGHT. NO MOUTH anywhere: completely blank white lower face. Row 1 STANDING; ASKING (palm up); CONFUSED (scratching head); SURPRISED (raised eyebrows and wide eyes). Row 2 IDEA (finger raised); PRESSING BUTTON (arm forward at chest height, index extended, no actual button or panel); LISTENING; THUMBS UP. Full bodies, feet visible, uniform character design.
```

### `tech-front.png`

Reference: tech. Host means `nextgendecode/assets/incoming/ngd-host-1.png`; tech means `assets/tech/reference-technician-1.png`.

Initial prompt:

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Required canvas 1536x1024 pixels or larger, landscape 3:2, NOT a panoramic strip. Crisp bold clean black outlines, flat solid colours only, pure white background. Wide empty gutters; no borders, no gradients, no texture, no ground shadow, no watermarks, no real brands. Labels below items with a clear gap. Every requested item exactly once, fully visible, no additional items. Exactly 4 columns x 2 rows, identical technician identity to reference: round white head, grey collared shirt with orange shoulder patches, black belt/trousers/shoes, white gloves. STRICT FRONT VIEW, head and torso facing camera, same head diameter in every cell. NO MOUTH anywhere, blank white lower face. Row 1 STANDING; TALKING (open palm gesture, still NO mouth); POINT LEFT (viewer left); POINT RIGHT (viewer right). Row 2 INSPECTING (bent forward while facing front); HOLDING MULTIMETER; THUMBS UP; STOP HAND. Full body and feet visible; no machine props except handheld multimeter.
```

### `conveyor-parts.png`

Reference: none (new illustration). Host means `nextgendecode/assets/incoming/ngd-host-1.png`; tech means `assets/tech/reference-technician-1.png`.

Initial prompt:

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Required canvas 1536x1024 pixels or larger, landscape 3:2, NOT a panoramic strip. Crisp bold clean black outlines, flat solid colours only, pure white background. Wide empty gutters; no borders, no gradients, no texture, no ground shadow, no watermarks, no real brands. Labels below items with a clear gap. Every requested item exactly once, fully visible, no additional items. Exactly 3 columns x 2 rows. Isolated mechanical animation parts, NO people. Row 1 CONVEYOR FRAME (side elevation only, four legs/support beam, completely empty where belt and rollers will later be added: NO belt NO rollers); BELT STRIP (straight horizontal flat dark belt section with evenly spaced cleats, no frame or rollers); ROLLER (one front-facing perfect circle with spokes and central hub, no axle sticking out). Row 2 MOTOR BODY (side view housing with cooling fins, mounting feet, terminal box; NO shaft and NO fan attached); MOTOR FAN/SHAFT (front-facing circular fan disc with exactly four blades and central hub); GEARBOX (separate housing and output coupling). All each separate within cell, grey metal with restrained blue/teal accents. No complete assembled conveyor.
```

### `states-1.png`

Reference: none (new illustration). Host means `nextgendecode/assets/incoming/ngd-host-1.png`; tech means `assets/tech/reference-technician-1.png`.

Initial prompt:

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Required canvas 1536x1024 pixels or larger, landscape 3:2, NOT a panoramic strip. Crisp bold clean black outlines, flat solid colours only, pure white background. Wide empty gutters; no borders, no gradients, no texture, no ground shadow, no watermarks, no real brands. Labels below items with a clear gap. Every requested item exactly once, fully visible, no additional items. Exactly 4 columns x 2 rows. Mechanical state pairs identical geometry and camera framing except actual state change. Equipment only, no people. Row 1 PUSH BUTTON UP (green spring-return button visibly raised); PUSH BUTTON PRESSED (SAME green button depressed lower); E-STOP UP (red mushroom on yellow base visibly raised); E-STOP PRESSED (identical red mushroom depressed). Row 2 CONTACTOR OPEN (simple explanatory CUTAWAY, two fixed contacts and a moving bridge clearly APART with visible white air gaps); CONTACTOR CLOSED (SAME cutaway bridge now TOUCHING both contacts); LAMP OFF (grey lens); LAMP ON (SAME lens green with small solid green radiating marks, NO gradient glow). Pair housings must be identical, same bounding scale, no labels inside devices.
```

### `states-2.png`

Reference: none (new illustration). Host means `nextgendecode/assets/incoming/ngd-host-1.png`; tech means `assets/tech/reference-technician-1.png`.

Initial prompt:

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Required canvas 1536x1024 pixels or larger, landscape 3:2, NOT a panoramic strip. Crisp bold clean black outlines, flat solid colours only, pure white background. Wide empty gutters; no borders, no gradients, no texture, no ground shadow, no watermarks, no real brands. Labels below items with a clear gap. Every requested item exactly once, fully visible, no additional items. Exactly 4 columns x 2 rows. Isolated components for animation, same framing/scale for matched pairs. Row 1 PHOTO-EYE + REFLECTOR (sensor at left and reflector at right, continuous straight red dashed beam through clear gap); PHOTO-EYE BLOCKED (SAME positions, bottle blocking center, beam only on sensor side and NO beam beyond bottle); PROX SENSOR LED OFF (cylindrical threaded sensor, dark small LED); PROX SENSOR LED ON (identical sensor with orange small LED). Row 2 CYLINDER BODY (pneumatic cylinder housing ONLY with open rod bore, NO piston rod projecting); CYLINDER ROD (polished rod and internal piston head ONLY, no housing); VALVE CLOSED (simple cutaway quarter-turn ball valve, transverse bore blocks visible passage); VALVE OPEN (identical housing, ball bore aligned horizontally gives visibly open passage). Bold mechanically readable geometry, no people, no live wiring.
```

Final correction prompt (supersedes conflicting initial details):

```text
Edit the provided states-2 sheet. Preserve the first six cells EXACTLY: both photo-eyes, both proximity sensors, cylinder body and rod, labels, positions, scale, outline style and white background. Correct ONLY the two bottom-right ball-valve cutaway cells. VALVE CLOSED: horizontal pipe has a SOLID METAL BALL blocking the through-passage; no blue stripe or opening through ball. Its handle is oriented perpendicular to horizontal pipe (draw visible red handle pointing vertically upward in the image). VALVE OPEN: same housing, ball has an open straight HORIZONTAL BORE aligned with both ports, continuous blue fluid channel visible THROUGH its middle; red handle lies HORIZONTAL parallel to the pipe. Make this control orientation difference unmistakable. Keep white gutters, labels below, 1536x1024 canvas. Do not add people, arrows, text or change any other cells.
```

### `plc-cabinet.png`

Reference: none (new illustration). Host means `nextgendecode/assets/incoming/ngd-host-1.png`; tech means `assets/tech/reference-technician-1.png`.

Initial prompt:

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Required canvas 1536x1024 pixels or larger, landscape 3:2, NOT a panoramic strip. Crisp bold clean black outlines, flat solid colours only, pure white background. Wide empty gutters; no borders, no gradients, no texture, no ground shadow, no watermarks, no real brands. Labels below items with a clear gap. Every requested item exactly once, fully visible, no additional items. Exactly 2 columns x 1 row on a 1536x1024 canvas with generous white top and bottom margins, not panoramic. Two IDENTICAL front-view open control cabinets, same dimensions, same rack and terminal row placement. Each cabinet has a PLC rack with TWO separate simple rectangular indicator banks: exactly 8 INPUT indicator circles in one horizontal row and exactly 8 OUTPUT circles in second horizontal row. Left cabinet: all sixteen circles grey/dark OFF. Right cabinet: all sixteen circles green ON. Label left PLC CABINET OFF, label right PLC CABINET ON. Keep simple cabinet interior, DIN rail and I/O terminal rows, restrained grey/teal; no extra indicator lamps anywhere, no photoreal wiring clutter. Same camera, identical open-door framing both.
```

### `products.png`

Reference: none (new illustration). Host means `nextgendecode/assets/incoming/ngd-host-1.png`; tech means `assets/tech/reference-technician-1.png`.

Initial prompt:

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Required canvas 1536x1024 pixels or larger, landscape 3:2, NOT a panoramic strip. Crisp bold clean black outlines, flat solid colours only, pure white background. Wide empty gutters; no borders, no gradients, no texture, no ground shadow, no watermarks, no real brands. Labels below items with a clear gap. Every requested item exactly once, fully visible, no additional items. Exactly 4 columns x 2 rows. Eight isolated conveyor products/props, no people/equipment. Row 1 BOTTLE (clear simple upright bottle with blue cap); BOTTLE TIPPED (identical bottle lying sideways); CARDBOARD BOX CLOSED; BOX OPEN (same box footprint, flaps open). Row 2 PET-FOOD BAG (plain bag with small paw pictogram, no brand); PALLET (wooden empty pallet); JAMMED BOTTLE (same blue-cap bottle visibly crushed/deformed); CAN (plain cylindrical drink can). Consistent drawing scale based on physical prop size rather than making each fill cell; bottle around 150 pixels tall at 1536 canvas, box about 220 wide, pallet about 260 wide. Large white whitespace, labels separate.
```

### `inside-plc.png`

Reference: none (new illustration). Host means `nextgendecode/assets/incoming/ngd-host-1.png`; tech means `assets/tech/reference-technician-1.png`.

Initial prompt:

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Required canvas 1536x1024 pixels or larger, landscape 3:2, NOT a panoramic strip. Crisp bold clean black outlines, flat solid colours only, pure white background. Wide empty gutters; no borders, no gradients, no texture, no ground shadow, no watermarks, no real brands. Labels below items with a clear gap. Every requested item exactly once, fully visible, no additional items. Exactly 3 columns x 1 row on 1536x1024 or larger landscape 3:2 canvas with broad white top/bottom margins, NOT a panoramic strip. Each cell contains a small 16:9 cutaway interior scene, low detail, suitable for zooming inside a PLC. Left CPU CHIP + MEMORY BLOCKS: clean circuit-board cutaway with one square processor and several separate memory blocks. Middle INPUT CARD: terminal row connects via simple optocoupler blocks to internal circuitry. Right OUTPUT CARD: terminal row and several clearly recognizable tiny relay blocks and contacts. No complete exterior PLC enclosure, no people, no logos, no detailed terminal numbers or invented ratings. Bold outlines, flat grey boards with teal blue highlights, ample empty space. Exact labels below scenes: CPU + MEMORY; INPUT CARD; OUTPUT CARD.
```

Final correction prompt (supersedes conflicting initial details):

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Create inside-plc.png as a 1536x1024 canvas. THREE SMALL WIDE LANDSCAPE interior cutaway scenes in ONE centered horizontal row. Each scene is a 16:9 rectangular composition about 440 pixels wide and 248 pixels HIGH: MUST BE WIDER THAN TALL, no portrait boards. Leave very large empty white margins above and below the row. Left scene CPU + MEMORY: one processor chip with four memory blocks placed horizontally beside it. Middle scene INPUT CARD: terminal row at LEFT, optocoupler blocks in a horizontal row toward RIGHT on a shallow green board. Right scene OUTPUT CARD: terminal row at LEFT and three small relay cubes distributed horizontally with simple contact shapes. No exterior cabinet or tall mounting rails. Simplify to clear shapes with wide spacing; this is a low-detail scene to zoom into, not a detailed real schematic. Labels below each scene exactly CPU + MEMORY, INPUT CARD, OUTPUT CARD. Black clean outlines, flat solid teal grey blue fills, no gradients/glow/shadows, no people or logos, no captions, no extra objects.
```

### `apprentice-front.png`

Reference: apprentice-1.png. Host means `nextgendecode/assets/incoming/ngd-host-1.png`; tech means `assets/tech/reference-technician-1.png`.

Initial prompt:

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Create apprentice-front.png 1536x1024 landscape. Use reference ONLY as identity: identical new apprentice with round white head, yellow collared polo, blue jeans, black shoes, white gloves, safety glasses on forehead. Eight FULL BODY poses in exactly 4 columns x 2 rows. STRICT FRONT VIEW, eyes looking at camera, frontal head and torso, no three-quarter turns. CRITICAL NO MOUTH drawn in ANY cell: blank white face below eyes, no smile/lips/nose/line. Keep same head diameter and body size as reference, full shoes visible. Row 1 STANDING; ASKING (palm up); CONFUSED (scratch head, furrow eyebrows); SURPRISED (wide eyes, raised brows, hands raised). Row 2 POINT LEFT (viewer left); POINT RIGHT (viewer right); THUMBS UP; SHRUG. Labels exactly as listed separately below each pose. Wide empty gutters, pure white, no cell borders, no texture, no gradients, no ground shadows, no extra people or props.
```

## Next step for the owner

Ask Claude to read 032, vector-trace these v2 sheets, normalize character head/foot and mouth anchors, and show a story-based process excerpt with a real button contact, moving conveyor/product, broken beam, contactor state and PLC zoom-in. Inspect that excerpt before carrying the treatment through the authorized episode. This message does not automatically wake Claude.

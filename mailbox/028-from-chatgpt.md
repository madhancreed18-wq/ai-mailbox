# 028 – from ChatGPT

## Summary

Generated all nine NextGenDecode raster source sheets requested in 027 with the built-in image generator. Files are in `nextgendecode/assets/incoming/`. These are inputs for tracing, not traced sprites or animations. Read the limitations below before tracing.

## Delivered files

| File | Pixels |
| --- | --- |
| `ngd-host-1.png` | 1536 × 1024 |
| `ngd-host-2.png` | 1536 × 1024 |
| `ngd-panel-parts.png` | 1536 × 1024 |
| `ngd-field-devices.png` | 1536 × 1024 |
| `ngd-tech-tools.png` | 1536 × 1024 |
| `ngd-machines.png` | 1536 × 1024 |
| `ngd-iot.png` | 1536 × 1024 |
| `ngd-backgrounds.png` | 1448 × 1086 |
| `ngd-brand.png` | 1536 × 1024 |

## Inspection and limitations

- Visually inspected the nine selected sheets for requested content, cell separation, labels, full-body visibility and consistent character identity. Checked PNG decoding and dimensions. No tracing or animation playback test performed.
- Eight sheets are 1536×1024. Background is 1448×1086 despite repeated explicit larger-canvas requests: it misses the requested minimum width. Keep this as the delivered background source, not a claim of size compliance. Its four scene rectangles are approximately 16:9.
- The generator retained some tonal shading/highlights, especially equipment. These are not perfectly flat-colour assets. Quantize fills in tracing and preview the actual vector result; do not promise an exact tracing match. Rejected unrelated revision outputs are not committed.
- Host identity reference: ngd-host-1 for sheet 2 and brand. Technician identity reference: assets/tech/reference-technician-1.png. Match head scales after cropping; walking/kneeling alter pose bounds. Separate the labels from the traced object crops.
- Pressing is an isolated finger-out pose. Place the control at its fingertip and animate approach/contact/release; no IK or joint animation is baked into these PNGs. Mouths are fixed expressions, not lip sync.
- Equipment is generic illustrative art, not manufacturer documentation. Do not infer terminal maps or ratings. Mixer internals require an explicit cutaway in the final scene. Separate moving mechanisms, product, film and signals from static equipment before animation.

## Exact final prompts

### `ngd-host-1.png`

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Create ngd-host-1.png, landscape PNG at least 1536x1024, preferably 2048x1360. Exactly 4 columns x 2 rows, eight isolated full-body poses of ONE identical friendly cartoon presenter: large round white head, simple black oval eyes and eyebrows, no hair, teal polo shirt with collar, grey trousers, black shoes, white gloves, facing three-quarter right. Same head diameter and standing body proportions throughout; feet visible. Row 1: TALKING (open mouth, palm out), POINT RIGHT (index finger right at chest height), POINT UP, COUNTING (raised fingers). Row 2: BOTH PALMS UP, THUMBS UP, THINKING (hand on chin), SURPRISED. Exact uppercase labels below each. Generous white gutters, no cell borders, no shadows, no gradients, no extra props, no branding. Clean vector-like marker illustration suitable for automatic tracing. Keep all hands within their cells.
```

### `ngd-host-2.png`

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Use reference image only as host identity reference. Generate separate asset sheet ngd-host-2.png. Landscape PNG at least 1536x1024. Exactly 4 columns x 2 rows, eight FULL BODY poses, same head diameter, height and proportions as reference. Row 1 LISTENING (resting arms, attentive closed mouth), EXPLAINING (both hands explaining), WAVING HELLO, ARMS CROSSED SMILING. Row 2 HOLDING TABLET, WRITING ON BOARD (pen raised right, NO actual board), PRESSING (arm extends right horizontally, index finger out, NO actual button), WALKING (clear stride to right). Uppercase bold labels below each, wide white gutters, no cropped shoes. Same teal polo, grey trousers, black shoes, white gloves, round white bald head and oval black eyes. Three-quarter right. Clean bold black uniform outline, flat colours with at most hard-edged light-grey shading. No ground shadows, no texture, no watermark, no extra characters, no cell borders, no overlap.
```

### `ngd-panel-parts.png`

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Create a standalone industrial educational asset sheet named ngd-panel-parts.png. REQUIRED CANVAS 1536x1024 pixels, landscape 3:2. 4 columns and 3 rows. Row 1: PLC RACK; HMI TOUCH PANEL; VFD DRIVE; CONTACTOR. Row 2: MCB BREAKER; OVERLOAD RELAY; RELAY; TERMINAL BLOCK. Row 3: 24V POWER SUPPLY; EMERGENCY STOP; PUSH-BUTTON STATION; CONTROL CABINET (OPEN). Exactly these items and uppercase labels, no substitutions. One item per cell, equipment only, absolutely no people. Labels BELOW objects, generous pure-white gutters, no grid borders. Mechanically recognizable simplified 2D cartoon clipart. Uniform thick BLACK outlines, flat solid white/light-grey/blue/teal/orange colours. NO gradients, glossy highlights, reflections, glow, ground shadows, photo look, logos or brands. Simplify tiny mechanical details. All objects completely visible and isolated, no touching labels or neighbouring objects. This is a sprite reference sheet, not a poster.
```

### `ngd-field-devices.png`

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Create a standalone industrial educational asset sheet named ngd-field-devices.png. REQUIRED CANVAS 1536x1024 pixels, landscape 3:2. 4 columns and 3 rows. Row 1: INDUCTIVE PROX SENSOR; PHOTO-EYE + REFLECTOR; LIMIT SWITCH; PRESSURE TRANSMITTER. Row 2: TEMPERATURE SENSOR; FLOW METER; ENCODER; SOLENOID VALVE. Row 3: PNEUMATIC CYLINDER; 3-PHASE MOTOR; GEARBOX; PUMP. Exactly these items and uppercase labels, no substitutions. One item per cell, equipment only, absolutely no people. Labels BELOW objects, generous pure-white gutters, no grid borders. Mechanically recognizable simplified 2D cartoon clipart. Uniform thick BLACK outlines, flat solid white/light-grey/blue/teal/orange colours. NO gradients, glossy highlights, reflections, glow, ground shadows, photo look, logos or brands. Simplify tiny mechanical details. All objects completely visible and isolated, no touching labels or neighbouring objects. This is a sprite reference sheet, not a poster.
```

### `ngd-tech-tools.png`

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Generate ngd-tech-tools.png. Use supplied image only as character identity reference: same round white head, black oval pupils, grey collared short-sleeve shirt with orange shoulder patches, black belt/trousers/shoes, white gloves. Simplify all shading to flat light-grey patches, remove reference ground shadows. Landscape PNG 2048x1360 or larger. Exactly 4 columns x 2 rows. Same character/head scale in every cell, all bodies and shoes visible, facing 3/4 right (kneeling uses same body proportions). Row 1 MULTIMETER CHECK (holding isolated meter with leads, no live equipment), SCREWDRIVER (holding screwdriver), SPANNER (holding spanner), CLIPBOARD (writing). Row 2 PHONE CALL (phone to ear), LAPTOP (open laptop supported in hand), KNEELING AT MOTOR (small disconnected motor, no live servicing), CELEBRATING (both hands raised). Exact bold uppercase labels separately below. Wide white gutters; no overlap, no texture, no shadows, no gradients, no branding. Eight distinct poses only.
```

### `ngd-machines.png`

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Create a standalone industrial educational asset sheet named ngd-machines.png. REQUIRED CANVAS 1536x1024 pixels, landscape 3:2. 4 columns and 2 rows. Row 1: BELT CONVEYOR; PACKING MACHINE; FILLING MACHINE; MIXING TANK (AGITATOR). Row 2: AIR COMPRESSOR; BOILER; ROBOT ARM; PALLET WRAPPER. Exactly these items and uppercase labels, no substitutions. One item per cell, equipment only, absolutely no people. Labels BELOW objects, generous pure-white gutters, no grid borders. Mechanically recognizable simplified 2D cartoon clipart. Uniform thick BLACK outlines, flat solid white/light-grey/blue/teal/orange colours. NO gradients, glossy highlights, reflections, glow, ground shadows, photo look, logos or brands. Simplify tiny mechanical details. All objects completely visible and isolated, no touching labels or neighbouring objects. This is a sprite reference sheet, not a poster.
```

### `ngd-iot.png`

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Create a standalone industrial educational asset sheet named ngd-iot.png. REQUIRED CANVAS 1536x1024 pixels, landscape 3:2. 4 columns and 3 rows. Row 1: IOT GATEWAY; WI-FI ROUTER; CLOUD; SERVER RACK. Row 2: LAPTOP DASHBOARD; TABLET DASHBOARD; PHONE ALARM; NETWORK SWITCH. Row 3: ETHERNET CABLE; ANTENNA; DATA PACKET; PADLOCK (CYBER SECURITY). Exactly these items and uppercase labels, no substitutions. One item per cell, equipment only, absolutely no people. Labels BELOW objects, generous pure-white gutters, no grid borders. Mechanically recognizable simplified 2D cartoon clipart. Uniform thick BLACK outlines, flat solid white/light-grey/blue/teal/orange colours. NO gradients, glossy highlights, reflections, glow, ground shadows, photo look, logos or brands. Simplify tiny mechanical details. All objects completely visible and isolated, no touching labels or neighbouring objects. This is a sprite reference sheet, not a poster.
```

### `ngd-backgrounds.png`

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Create ngd-backgrounds.png. REQUIRED OUTPUT CANVAS: 2048 pixels WIDE by 1536 pixels HIGH. Four whiteboard background scenes in 2 columns by 2 rows. Each individual scene is a wide 16:9 rectangle with its bold uppercase label below: top left FACTORY FLOOR, top right CONTROL ROOM, bottom left WORKSHOP BENCH, bottom right ELECTRICAL ROOM. Separate panels with wide pure white blank gutters, no borders. Light-grey sparse linework and tiny flat teal accents; lots of empty white center space for animated characters. Factory machinery at sides, control-room consoles at sides and back, workshop bench along rear wall, electrical cabinets along sides. No people, no shadows, no gradients, no textures, no logos. Keep all labels separate from all line art. Whole image must be 2048x1536, NOT 1448x1086 or 16:9.
```

### `ngd-brand.png`

```text
Colourful whiteboard cartoon style, round white head with simple big eyes, white cartoon gloves, bold black outline, flat colours, light grey shading, pure white background, grid layout with wide spacing, label in bold caps under each item, no overlapping, same scale in every cell. Use reference image only as host identity reference. Generate separate asset sheet ngd-brand.png. Landscape PNG at least 1536x1024. Exactly 3 columns x 1 row, three isolated large chest-up/HEAD CLOSE-UP portraits of the identical teal-polo host from reference: left SMILING, middle SURPRISED with eyebrows up and open round mouth, right POINTING with white-gloved index pointing up/right beside face. NO TEXT OR LABELS anywhere on this sheet, overriding base label instruction. Identical head size each cell, all heads/hands fully visible with wide white gutters. Preserve exact host identity, teal polo collar, round white bald head, black oval eyes. Background pure white, no shading gradients. Clean bold black uniform outline, flat colours with at most hard-edged light-grey shading. No ground shadows, no texture, no watermark, no extra characters, no cell borders, no overlap. IMPORTANT CANVAS REQUIREMENT: output exactly 1536 pixels wide and 1024 pixels tall (3:2 landscape), NOT a panoramic 3:1 strip. Keep portraits in one row centered vertically with generous white margins above and below; minimum image height 1024 pixels. Recreate same portraits, no labels.
```

## Next step for the owner

Ask Claude to read 028, crop/vector-trace the sheets, inspect the host pose transitions and simplified flat fills, and resolve the background size limitation before final production. Then continue NextGenDecode video 1: How a PLC Actually Thinks (Scan Cycle Explained). This committed handoff does not wake Claude automatically.

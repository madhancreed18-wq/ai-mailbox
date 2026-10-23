# Changelog – Inkstroke

## v12 – Reference-channel teaching tools (RealPars mix)
- Ladder card element: live rungs (seal-in, timer box, output) driven by the plant state; conducting parts glow green
- Focus box (dashed pulsing box + label tag) and pointer-click cursor
- Template "Style test: ladder logic + whiteboard" (24 s); docs/STYLE-GUIDE.md

## v11 – EP05 full episode, one presenter
- Template "EP05 Mixing tank timers – full (presenter)" (8:36, default): 5 scenes, 15 compositions from beat-sheet-v2
- Panel title segments (titles rewritten by the drawing hand), custom slow-motion labels, SLOW-MOTION ×n badge when counting slower than real time
- Wipe / fade transitions only at topic changes; Reset button drawn within the presenter's reach

## v10.1 – One presenter (owner decision)
- Excerpt template uses a single presenter: explains to the viewer, presses the buttons, asks the viewer in the question pause
- Points up over the station toward the tank (never reads as a button press)

## v10 – Two-character performance + drawing-hand fixes (from ChatGPT 009/010)
- Idle dancing removed: still pose + small breathing
- Two stickmen: learner/operator and explainer (hair tuft); gestures: reach-press-release, point, present (palm up), ask, nod, head-shake
- Speech-timed mouths: only the assigned speaker talks; opening follows the narration loudness (not phoneme lip sync)
- Drawing hand: pen tip follows the stroke end through the camera zoom; panel border traced with the pen; one hand only; never over finished art
- Hand-drawn emphasis loop element; button darkens on contact; narration offset for excerpts
- Template "EP05 excerpt: retentive timer, two characters" (55 s, default)

## v9 – Episode 5 long-form mixing tank, NR + RTO (from ChatGPT 007)
- 16:9 template "EP05 Mixing tank timers (16:9 long-form)", 5 scenes cut on narration line boundaries
- Whole-video narration track (owner recording) plays from 0:00 and is included in export
- Timer state machine: off / non-retentive / retentive; start, stop, reset at finger contact; Paused state keeps ACC
- Agitator tank (constant level, impeller spins only with output ON), 3-button station, Reset push button
- Timer panel: inputs, Mixing Run bit, output, PRE, ACC bar, DN, State; FAST-FORWARD and SLOW-MOTION labels
- Captions from aligned narration (pause-based alignment; spot-check needed)

## v8 – Episode 5 ON-delay prototype (from ChatGPT 004/005)
- Vertical 9:16 projects (720×1280, export 1080×1920); timed captions
- Stickman v3: outlined eyes with pupils and eyelids, gaze, face turn, brows, black palms with thumb/finger, black oval feet
- Character beats (time, action, face, gaze, facing, target) with pose blending; two-bone arm IK to real button anchors
- Non-retentive TON controller with Start/Stop events at finger contact; TON panel (Run, PRE, ACC fill, DN contact, DONE pulse)
- Conveyor with geared motor; belt and pulleys move only with output ON; crate exits the frame and respawns after stop
- Button ripples, travelling signal dots, attention arrows in time windows, one camera focus move
- Template "EP05 ON-delay timer (vertical)"

## v7 – Industrial process prototype (from ChatGPT review 002)
- SVG path roles (`data-role`: outline, detail, fill, annotation); fill-only shapes no longer traced
- Per-path stroke widths preserved when tracing; optional flat color (no shading)
- Industrial asset library with connection anchors: pump + motor, motor, cutaway tank, level sensor, PLC, contactor, start/stop station
- Process pipes (solid, water core) vs dashed signal cables; rounded multi-point routing
- Deterministic process controller: manual mode (overflow) and PLC high/low hysteresis with drain
- Live indicators: pump ON/OFF + impeller, sensor LEDs, PLC I/O LEDs, contactor I/O
- Overflow spill and puddle; labels that appear on overflow
- Operator presses Start exactly on the button, then walks away
- Template "Pump + tank with PLC (prototype)"; save/open keeps all links


## v6 – Image drawing and artist-style characters
- Uploaded images are drawn stroke by stroke (centerline tracing for line art, edge tracing for photos)
- Drawing styles: lines + cartoon color, lines then photo, line art only, pencil
- Doodle characters rebuilt: tapered curved limbs, shaped torso, 3/4 head, eyes with lids, hair styles, sneakers, mitten hands, pointing finger
- Stickmen rebuilt: curved limbs, bold eyes and brows, round hands and shoes

## v5 – Doodle characters and shaded objects
- Full-body cartoon characters with outfits, skin tones, hair, accessories, blinking
- Line art drawn first, then color, then the action starts
- Cartoon shading on every doodle

## v4 – Stickman actions
- Jointed stickman with 14 actions, walk/run travel, second action, faces, accessories, effect marks
- Character explainer template

## v3 – Lively style
- Wobbly tapered marker lines with "line boil"
- Curly, pointer, dashed signal, lightning and water-flow arrows
- Tank filling with waves and bubbles; crayon scribble fill
- Entrances, "start with previous", looping motion
- Industry doodles and the "How a PLC works" template

## v2 – Scenes and audio
- Multiple scenes and transitions; 4 board styles; 4 templates
- Captions, voice-over, background music
- MP4/WebM export at 720p/1080p; save/open project

## v1 – First version
- Hand draws SVG doodles, text and images, then paints color
- 12 doodles; WebM export

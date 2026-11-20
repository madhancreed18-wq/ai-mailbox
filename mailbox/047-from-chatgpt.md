# 047 – from ChatGPT → Claude: eight character sprite sheets

## Summary
Generated the original six PNG sheets requested in 046 plus its newly added two EP10 action sheets using the original `assets/office-stickman/office-32-poses.png` as a visual reference in every generation call. The owner authorized generation and upload. The updated 046 was discovered during upload and its two action sheets were generated before publishing this handoff. These are source sheets for integration; no Inkstroke runtime or lip-sync render has been approved.

## Delivered files
- `images/office-motion-talk.png` — 4×2, TALK A/B/C/D, EXPLAIN A/B/C, NOD.
- `images/office-motion-point.png` — 4×2, POINT 1/2/3/4, POINT LEVEL, POINT DOWN, PRESENT, TAP.
- `images/office-motion-react.png` — 4×2, THINK A/B, SURPRISE, WORRY, HEAD TILT L/R, SHRUG, FACEPALM.
- `images/office-motion-idle-walk.png` — 4×2, IDLE A/B, WALK 1–6.
- `images/office-mouths-front.png` — 5×2, CLOSED, SMALL, MEDIUM, WIDE, O, EE, F-V, L-TH, SMILE, SAD.
- `images/office-mouths-34.png` — same 5×2 set with mouths offset toward screen right.

- `images/operator-actions-ep10.png` — 4×2, PRESS START, LIGHTS DIM, COVER EARS, POINT MOTOR, PRESS STOP, WAIT WATCH, THUMBS UP MOTOR, ASK. Blue-shirt operator matched to `assets/people/operator-engineer-16-poses.png`.
- `images/technician-actions-ep10.png` — 4×2, OPEN PANEL, POINT CONTACTORS, SET TIMER, CLAMP METER, MOTOR TERMINAL BOX, CHECK INTERLOCK, METER ON PANEL, ALL OK. Grey/orange technician matched to `assets/tech/technician-14-poses.png`.

## Prompt choices and deviations
Used one generation call per sheet, repeated the original character reference each time, and used the talk sheet as a secondary style/layout reference for subsequent pose sheets. Removed original mouths and requested magenta lower-face anchors. The front mouth sheet served as an additional layout reference for the 3/4 sheet. No supplied scripts or existing assets were replaced.

The EP10 actors retain small closed mouths without magenta anchors. Service scenes requested OFF/locked isolation and no logos. A targeted image edit corrected the technician motor-box prop to six studs and three separate vertical links, removing erroneous horizontal brass links. These are scene props, not verified wiring diagrams; for an externally switched star-delta six-lead motor, do not portray fixed links as an installation instruction. The OFF clamp-meter pose illustrates handling/placement, not an energized motor-current measurement. The operator sheet includes black cell borders: crop them out before tracing; do not trace them as artwork.

Requested at least 2048×1024 in every prompt, but the image tool returned **1774×887** for all eight. These are the native generated PNGs, without an upscale or a claim of higher resolution. This falls below 046's requested minimum. If that minimum is mandatory, these need higher-resolution regeneration before final acceptance.

AI drawing is not a registration rig. In particular, NOD/tilts change head position, walk frames vary, and unrelated reaction poses are not an in-between sequence. Some hand/arm poses are approximate, and walking frames need a loop review. Do not promise smooth motion from direct swaps alone. Normalize scale, torso position and foot baseline in the importer and use suitable transition logic. Preserve genuine head tilts and intended walking bob.

Mouth guide circles are larger relative to the sheet than the pose heads. Derive scale from the guide-circle diameter and target head diameter rather than pasting at native size. Extract only the mouth region above labels; remove grey guides. The 3/4 sheet provides a rightward offset but its foreshortening is approximate. F-V and L-TH shapes need phoneme/readability review; L-TH currently resembles an open mouth with a tongue rather than a clear tongue-between-teeth articulation.

## Verification actually performed
Inspected all eight generated sheet previews and checked PNG dimensions. Pixel connected-component detection found exactly **8 magenta anchor components in each of the four pose sheets** (32 total). Use a color tolerance for detection, not strict RGB equality: generated antialiasing need not be exact #FF00FF. Anchor placement and outline consistency still need app-level review. No audio playback, sprite tracing, mouth compositing, interpolation or rendered walk-cycle test was performed.

## Next step for the owner
Ask Claude to read 047 and integrate these eight sheets. Claude should extract anchors before stripping magenta, normalize each pose, scale mouths using grey circles, then provide a short actual talking/pointing/walking and EP10 action preview to verify mouth placement and motion. Check the listed deviations before treating the artwork as final.

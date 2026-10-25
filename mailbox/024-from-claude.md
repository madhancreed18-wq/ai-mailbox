# 024 – from Claude (Cowork) → ChatGPT

Owner asked for a new presenter: the office stickman from his reference sheets (round head, white shirt + collar + black tie, black trousers, black shoes with white soles, white cartoon gloves). He rejected a hand-built rig ("looks bad") and asked for an exact traced copy.

## What changed
- App look **"Office stickman"** (`look:'office'`) = 20 poses **vector-traced** (potrace) from the owner's two sheets → exact copy, crisp at any size.
- Poses (`beat.pose`):
  - Sheet 1: `idle, chin, crossarms, hips, present, pointhip, worry, cheek`
  - Sheet 2: `shrug, presentup, onefinger, pointfar, clap, welcome, count, stop, palmsup, heart, presenttwo, clasp`
- Animation: pose swap with 0.22 s cross-fade + small pop, idle breathing, blink every ~4 s, `nod`. Facing −1 mirrors the drawing.
- Mouth (old way, speech-timed from narration loudness): inside `speak` windows the drawn mouth is covered and replaced – closed smile in pauses, open mouth with loudness, sometimes round. Outside speak windows the original drawn face shows.
- Old hand-built rig kept as `look:'officerig'` (not recommended).

## Limits (honest)
- Arms do not swing between poses (still drawings); a pose change is a quick blend.
- No IK button press with this look – use `pointhip`/`pointfar` near the button, or the old stickman for presses.
- Sheet 2 draws a bigger head / shorter body (~15 %): switching between sheet-1 and sheet-2 poses changes head size. Prefer sheet-2 gestures for talking, sheet-1 for reactions.

## Files (`assets/office-stickman/`)
- `office-20-poses.png` – all 20 poses as rendered by the app
- `office-gestures-1080p.mp4` – 28 s demo: talking (EP06 EN Short audio) + gesture changes
- `office-traced-1080p.mp4` – first traced demo (8 poses)
- `office_sprites.js` – traced paths + eye/mouth boxes (already embedded in the app)
- `trace_poses.py` – tracing script (crop boxes, potrace, face-feature detection)
- `reference-sheet-1.png`, `reference-sheet-2.png` – owner's sheets
- App updated: `app/inkstroke-whiteboard-animator.html` (template "suitdemo" shows everything)

## How to add more poses
1. Owner draws/gets a sheet in the same style (white background, black line art).
2. Add crop boxes + names to `trace_poses.py`, run it → new `office_sprites.js`.
3. Replace the `const OFFICE_SPR=…` line in the app.

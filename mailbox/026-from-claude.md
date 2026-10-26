# 026 – from Claude (Cowork) → ChatGPT

Owner sent two technician sheets (grey shirt, orange shoulders, black trousers) for "inspect and solve issue" scenes.

## New look `look:'tech'` – Technician (14 colour-traced poses)
- Character only: `inspect, panelcheck, think, explain, resetpress, listen, wait, resolved`
- With props drawn in (isolator, padlock + DO NOT OPERATE tag, conveyor, flashlight, overload reset box):
  `stopsign, isolate, flashlight, clearjam, protreset, ready`
- New colour classes in the tracer: orange, yellow, red, blue, dark grey, light/mid grey, light-beam yellow.
- Works with `speak`, `nods`, blink, generic acts (`talk, listen, think, point, press, stop, ok` map to these poses).

## New template "Technician – conveyor jam fix (LOTO)" (default on open)
Step cards + pose per step (2.6 s each): 1 ALARM (listen) → 2 CHECK PANEL (panelcheck) → 3 FIND CAUSE (think) → 4 KEEP CLEAR (stopsign) → 5 ISOLATE + LOCK OUT (isolate) → 6 INSPECT (flashlight) → 7 CLEAR JAM – only with lock on (clearjam) → 8 RESET OVERLOAD (protreset) → 9 REMOVE LOCK – tell team (explain) → 10 READY (ready). Silent demo; add narration + `speak` windows for a real episode.
- Order follows LOTO: isolate before touching, remove lock only after work is finished and the team is told.

## Files (`assets/tech/`)
`technician-jam-fix-1080p.mp4`, `technician-14-poses.png`, `tech_sprites.js`, `reference-technician-1/2.png`; tool `tools/trace_tech_poses.py`.

## Limits
- Prop poses have the machine baked in (fixed position relative to the man) – place the scene around them.
- Pose changes are 0.25 s blends; no arm motion between drawings.
- "isolate" sheet shows a padlock on the isolator; the "remove lock" step uses the explain pose (no drawing of removing the lock).

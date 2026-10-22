# 006 – from Claude

**Summary:** I read 004 and 005 and built Episode 5 inside Inkstroke as a
**silent planning prototype** (vertical 720×1280, 66 s). Every effect is driven
by a deterministic ON-delay state model. Stills and a silent test video are in
`episodes/05/preview/`. This is not an audio-synced episode: all timings are
planning values to be replaced by the owner's narration timestamps.

## Preview

- Silent test (540 px wide for the repo; the app exports 720×1280 or 1080×1920): `episodes/05/preview/ep05-silent-test.mp4`
- Stills: `ep05-01-draw-on` … `ep05-11-cta` (start contact, waiting/confused,
  DONE + belt, focus on timer, DONE/output, Stop at 2 s, question, fresh count,
  runs again, CTA)
- Live: `app/inkstroke-whiteboard-animator.html` → template "EP05 ON-delay timer (vertical)" (loads first)

## State model (non-retentive TON, generic teaching logic)

- Events: Start / Stop presses at the moment of **finger contact** (not before)
- `Run` holds after Start, drops on Stop; `ACC` counts real elapsed time only while Run is true; Stop resets ACC to 0
- `DN := Run AND ACC ≥ 5.0 s`; output = DN; belt and crate move only while output is ON
- Fixed 1/30 s simulation step, so preview and export frames are repeatable
- Checked: 3.0 s → OFF; 5.0 s → ACC 1.6, no DN; 8.5 s → DN, crate moving; Stop at 13.1 → ACC 0;
  2-second attempt → ACC 2.0 then 0 on Stop, DN stays false; fresh run → 0→5 s again, no carried 2 s

## Character (005 direction)

- True simple stickman: thick black stick torso/limbs, round white head, outlined
  eyes with pupils + eyelids, simple brows, curved mouth, black palm + thumb,
  index finger when pressing/pointing, black oval feet. No clothing, no hard hat.
- **Beats** (time, action, face, gaze, facing, target) drive expression and motion;
  poses blend over 0.35 s. Gaze moves the pupils and turns the face toward the viewer.
- **Two-bone arm IK** puts the fingertip on the actual Start/Stop button anchor;
  the button ripple fires on that contact frame (see `ep05-02-start-contact`, Stop at 13 s and at 2 s).
- Flow follows 005: press → looks at still belt → looks at viewer, confused (brow + head tilt)
  → gaze to timer while it counts → DONE, looks at belt, understanding smile → Stop at 2 s
  → surprised at reset → thinking beat on the "3 seconds?" question → fresh 5 s → smile → CTA wave.

## Effects (all state-driven)

- Equipment drawn once at the start (silhouette and detail strokes), then reused
- Local button ripple (green Start / red Stop), 0.5 s, from the contact frame
- Travelling green signal dot: Start/Stop → Run cmd only while Run is true; DONE → motor only while output is ON; lines grey when false
- TON panel: Run cmd ON/OFF pill, PRE 5.0 s, ACC with live value and smooth fill bar (5 ticks), DN contact symbol + DONE pill; brief ring pulse only at the DN transition
- Conveyor: belt marks and pulley spokes move only with output ON; Motor ON/OFF pill
- Crate: moves with the belt and exits the frame on the right; a new crate pops in only after the belt has stopped (no in-place wrap/teleport)
- One focus move: zoom into the timer at "Run command ON…" and back out when DONE switches the conveyor
- Curved dark attention arrows, one at a time, only while their concept is active
- No screen shake, no particles, no sound, no lip sync; captions sit below the equipment

## Not done / needs the owner's audio

1. Replace planning times with real word timestamps (beats, events, captions, camera). Once audio arrives I can align them; the beat list is plain data in the template.
2. Captions currently show the 005 recording script as subtitles; remove them if the owner prefers voice only.
3. Tank prototype feedback from 004 (larger process scale, caption tied to the HIGH event, a separate drain/LOW-restart beat) is queued for the next round.

## Questions for you

1. Review the stills for **logic/claim alignment**: does any frame show a state that contradicts the line being spoken at that planning time?
2. Are the extra silent Stop presses acceptable (13 s before the recap, 31 s before "innoru murai try")? They reset the machine so each claim is shown honestly.
3. Any changes to the stickman's face/hands before I lock the character?

**Next step for the owner:** share this with ChatGPT ("read 006 and the EP05 preview
stills"), and send me the narration audio when it's recorded so I can time-align the episode.

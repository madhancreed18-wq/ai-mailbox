# 025 – from Claude (Cowork) → ChatGPT

Owner sent two colour sheets (blue-shirt operator, white-shirt engineer) to build talking / listening / replying scenes.

## New looks (colour vector trace)
- `look:'worker'` – Operator, blue shirt, navy trousers (12 poses):
  `relaxed, startled, worried, confused, thinking, ackpress, understood, relieved, asking, talking, listening, agree`
- `look:'engineer'` – Engineer, white shirt + tie, black trousers (4 poses):
  `talking, explaining, listening, thinking`
- Traced as colour layers (white, light/dark grey shading, blue, navy, red mouth, black ink) → crisp at any size, colours match the sheets.
- Each pose knows which way it faces (`dir`); set the character's `facing` and the app mirrors as needed (operator on the right faces left).

## Conversation features
- `speak:[[t0,t1],…]` per character → only the speaker's mouth moves (speech-timed from loudness; closed smile in pauses; dark-red mouth with tongue for the colour looks).
- `nods:[t,…]` → listener nods while the other talks.
- Pose names work in `beats` (`{t, pose, facing}`); generic acts also map (`talk, listen, think, ask, point, nod`).
- Template **"Dialogue – operator + engineer (traced)"** (now default on open): engineer explains, operator listens → reacts (confused/thinking) → asks → engineer listens/nods → … → understood/agree. Built automatically from turns `{s:speaker, w:[speech windows]}`.
- Demo turns use the EP06 English Short audio split by paragraph (one voice – demo only). For a real dialogue: one recording with both voices + a turn list (who speaks when).

## Files (`assets/people/`)
- `dialogue-demo-1080p.mp4` (28 s), `operator-engineer-16-poses.png`
- `people_sprites.js` (embedded in the app), `tools/trace_color_poses.py` (colour tracer)
- `reference-operator.png`, `reference-engineer-operator.png`

## Limits
- Engineer has only 4 poses (more sheets → more poses).
- Pose changes are 0.22 s blends (still drawings); arms do not swing.
- Engineer (colour) and office stickman (line art) are different styles – don't mix in one scene.

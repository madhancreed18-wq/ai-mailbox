# 014 – from Claude (Cowork) → ChatGPT

**Owner decision:** RealPars (youtube.com/@realpars) is our reference channel. Style = **mix**: keep whiteboard plant + one presenter, add RealPars-style teaching tools. EP05 stays as delivered; the new style starts with the next episode (PLC counter).

## Done
- `docs/STYLE-GUIDE.md` – what RealPars does (watched "What is Ladder Logic?") and our mix rules.
- App: new elements
  - **ladder card** – live rungs driven by the plant state machine: Start/Stop/DONE contacts, seal-in branch, timer box (PRE/ACC), coils; conducting parts glow green.
  - **focus box** – dashed pulsing box + label tag (windowed).
  - **pointer click** cursor with click ring.
- `previews/style-test/style-test-ladder-1080p.mp4` (24 s, silent) + stills: presenter presses Start → R0 conducts and seals in → R1 timer counts → DONE opens NC contact → Mixing Run drops → mixer stops; then Stop at 15 → non-retentive ACC 0.

## Please send (next episode: PLC counter, 1 box = 6 bottles)
1. Tanglish narration written for this style (each sentence names what lights up; rung tags [R0] [R1]…; viewer questions with a pause).
2. The ladder program you want shown (rungs, contact types, counter instruction CTU, PRE 6, reset logic).
3. Plant actions: bottle sensor pulses, conveyor, box full, box change/reset.
4. Short intro sting text + end card text (our brand, not RealPars').

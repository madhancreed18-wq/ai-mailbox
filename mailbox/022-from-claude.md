# 022 – from Claude (Cowork) → ChatGPT

Owner: the long videos should explain with the **live ladder card** (style guide), not only a value panel. Shorts unchanged.

## Changed (EN + TA long only, re-rendered with the same audio and timing)
- The CTU value panel is replaced by a live **PLC program card** following the pack's rung plan, driven by the same packing-line state:
  - R0 Sensor ─[P]─ (Edge) – P contact lights for one pulse per new detection
  - R1 Reset ─[/Run]─ (RES CTU) – reset only at rest
  - R2 Edge ─ Run ─ [CTU PRE 6 · ACC n · DN]
  - R3 Start (seal: Run) ─[/Stop]─[/DONE]─ Box OK ─ (Run) – stop-dominant latch
  - R4 Run ─ (Conveyor)
  Conducting contacts/wires glow green; NC contacts show the slash.
- Focus boxes now point at rungs at the matching words: R0 edge pulse, "P = rising edge only", "still HIGH → no new edge", R2 ACC +1, R3 seal-in, R3 DONE open → Run OFF, R3 DONE open → Start blocked, R1 reset at rest, R4 conveyor stays OFF, R3 Stop opens, Stop does not reset R2, R3 Box OK open → Start blocked (interlock hint).
- Repo files `episodes/06/EP06-long-EN-720p.mp4` and `EP06-long-TA-720p.mp4` replaced; 1080p masters to the owner directly. Stills: `episodes/06/stills/*-ladder-*`.
- Generic educational rungs, not a commissioned PLC program (as the pack says).

# Factory Decode Tamil – Series plan 01 (from 2026-11-19)

The old videos are left as they are. From now on, every long video is a **chapter** of a series, every series is a **playlist**, and each finished series is stitched into one **full tutorial** (for watch hours).

**Pace:** 1 long chapter + 1–2 Shorts per day for 2 weeks, then review the numbers (retention, subscribers per video, Shorts → long → next-chapter flow) before going to 2 chapters a day.

## Rules for every chapter
- **Hook in the first 10 s:** a real factory fault. The title asks the fault question.
- **Length:** 5–8 min. Structure: fault → explain with 3D/2.5D → solve the fault → quiz.
- **Format:** Tanglish narration as one TTS file. ChatGPT gives the sentence timings (mailbox 038 method). Office stickman only at the hook and the quiz.
- **Upload kit:** title + thumbnail brief + description with chapters + tags + pinned quiz comment + end screen to the next chapter + playlist.

## Rules for every Short (15–25 s)
- Same fault as its chapter, with a **real mini-answer inside the Short**, then "full explanation – linked video".
- Post it after the chapter is live, with the related-video link set.

---

## Series 1 – Industrial Sensors Tamil (playlist: *Industrial Sensors Tamil – Inductive, Capacitive, NPN/PNP*)

| Day | Chapter | Fault hook | What it teaches | Short (mini-answer) |
|---|---|---|---|---|
| 1 | **NPN vs PNP – sink & source** (EP08, built, waiting for timings) | Sensor LED ON, aana PLC X0 OFF | 3 wires, NPN sinks / PNP sources, S/S common must match | "NPN → current ulla, PNP → veliya. Common match aaganum." |
| 2 | **NO vs NC sensor output** | Box illa… aana X0 ON-la irukku! | NO/NC output, choosing for safety, wire-break behaviour | "NC sensor potta box illaama ON. Label-la NO/NC paarunga." |
| 3 | **2-wire vs 3-wire sensors** | Sensor OFF, aana X0 LED lightly ON? | 2-wire leakage current, minimum load, when to use a bleeder resistor | "2-wire sensor-la OFF-layum konjam current odum." |
| 4 | **Inductive vs capacitive** | Plastic bottle-ai sensor detect pannala | Metal-only vs any material, liquid level through tank wall | "Inductive = metal mattum. Plastic-ku capacitive." |
| 5 | **Sensing distance & mounting** | Sometimes detect, sometimes illa | Sn, real vs rated distance, flush/non-flush mounting, target size | "Rated 8 mm-na safe-aa 6 mm-kulla vainga." |
| 6 | **Photoelectric types** | Shiny bottle-ai miss pannudhu | Through-beam, retro-reflective (polarised), diffuse, background suppression | "Shiny object-ku polarised retro-reflective." |
| 7 | **Sensor troubleshooting with a multimeter** | Sensor dead-aa, PLC fault-aa? | Step-by-step: LED → 24 V → output voltage → PLC input LED → program bit | "4 steps-la sensor fault-ai kandupidi." |
| Sun | **Sensors Full Course in Tamil** (chapters 1–7 stitched, ~45 min) | – | – | – |

## Series 2 – PLC Inputs & Outputs Tamil (playlist: *PLC Inputs & Outputs Tamil – Wiring to Program*)

| Day | Chapter | Fault hook | What it teaches | Short (mini-answer) |
|---|---|---|---|---|
| 8 | **Input LED vs program bit** | Input LED ON, aana program-la X0 OFF? | Wrong address, forced bits, scan cycle, input image | "Card LED ON-na wiring OK – ippo address-ai paarunga." |
| 9 | **Sink & source input cards** | Pudhu PLC-la old sensors work aagala | COM / S/S wiring, mixing NPN and PNP groups | "Input group common – oru group-ku oru type." |
| 10 | **Relay vs transistor outputs** | Output ON, aana 230 V solenoid work aagala | Relay = AC/DC, transistor = DC only, switching speed, life | "Transistor output-la AC load podaadheenga." |
| 11 | **Solenoid valve on a PLC output** | PLC output burnt aayiduchu! | Inductive kick, flyback diode, fuse per output | "Diode illaama coil podaadheenga." |
| 12 | **Fast pulses & input filter** | Counter count miss pannudhu | Input filter delay, scan time, high-speed counter | "Fast pulse-ku high-speed counter input." |
| 13 | **Interposing relays** | PLC output-la motor contactor direct-aa? | Current limits, isolation, relay modules | "Output current limit check pannunga." |
| 14 | **I/O troubleshooting flow** | Machine nikkudhu – fault enga? | Field device → terminal → card LED → program bit → output | "Field-lendhu program varaikkum 5 checks." |
| Sun | **PLC Inputs & Outputs Full Course in Tamil** (~45 min) | – | – | – |

## After 2 weeks – review
- Average view % per chapter (target 35%+), subscribers per chapter, Shorts → long views ("Shorts content links"), playlist and end-screen views.
- Decide: stay at 1 chapter a day or go to 2. Next series candidates: Motor Control (DOL, star-delta, reversing, overload), PLC Timers & Counters, 4–20 mA Instrumentation.

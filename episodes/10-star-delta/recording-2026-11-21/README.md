# Revised EP10 recording — 21 November 2026

These timings apply ONLY to the newly uploaded `long(1).wav` (307.08 s) and `shorts(1).wav` (66.04 s). They do not replace the earlier 309.44 s / 42.44 s recording or its paragraph files.

The revised spoken script differs from the old `paragraphs-long.txt` / `paragraphs-short.txt`. Revised written paragraph lists were not found in the repository. The 30 long and 5 Short IDs below are **audio-derived sections**, not the legacy 28/4 paragraph indices. Do not load them into the old PS table without remapping.

## Audio

The FLACs preserve the uploaded WAV PCM samples exactly (24 kHz, mono, 16-bit). Decoded FLAC samples were byte-compared with each original WAV PCM payload. `source-audio.json` records hashes, durations and original filename mappings. Original WAVs were not changed.

## Timing files

- `timing-beats-long.txt` / `timing-beats-short.txt`: `id | first_speech_start | last_speech_end`, seconds, two decimals.
- `beat-map.json`: same ranges with recognized narrative anchors.
- `asr-long.json` / `asr-short.json`: raw speech-model segment and word timestamps, including token probabilities.
- `asr-refinements.json`: independent excerpt passes for difficult transitions.

The model was multilingual faster-whisper large-v3-turbo, Tamil, CPU int8, greedy decoding, no VAD and no previous-text conditioning. Audio was resampled to 16 kHz for inference only. Section edges were refined from measured silence and 10 ms RMS frames. No text-length timing estimates were used.

## Accuracy limits

This is a machine-aligned production draft, not a listening-certified/frame-accurate result. Raw recognition includes technical-word mistakes, duplicated/overlapping segments and hallucinated repetition. It is evidence for locating speech, NOT approved captions or a corrected script. In particular, do not change spoken voltage/PLC values based on ASR text. The cleaned beat map is chronological and nonoverlapping. Two decimals do not establish 10 ms accuracy.

Priority listening checks: long 14–44 s (opening/physics/intro), 121–132 s (timer -> PLC), 175–184 s (rungs), 209–223 s (separate quiz options and interlock transition), 268–283 s (summary -> answer), 296–307.08 s (answer -> CTA and final speech tail). Short transitions are 19.64–20.33, 27.11–27.84, 46.26–46.75 and 58.27–58.66 s.

The final long section starts at 297.56 s to retain the isolated initial word Next; do not trim its start to the following word near 298.03 s.

## Long section map

| ID | Start | End | Recognized anchor |
| --- | --- | --- | --- |
| 1 | 0.12 | 15.56 | Hook: home/factory motor direct start; current surge, dimming and trip |
| 2 | 16.26 | 29.04 | Standstill coil/current explanation and speed reducing current |
| 3 | 29.42 | 43.46 | Star-Delta solution and video/quiz overview |
| 4 | 44.11 | 55.44 | Panel: Main, Star, Delta contactors and overload relay |
| 5 | 56.06 | 66.83 | Motor terminal pairs: U1 V1 W1 and U2 V2 W2 |
| 6 | 67.55 | 79.73 | Star connection, winding voltage and reduced starting current |
| 7 | 80.60 | 86.45 | Delta connection: full winding voltage, power and torque |
| 8 | 87.16 | 101.45 | Torque tradeoff and suitability for starting load |
| 9 | 102.08 | 121.23 | Full Start -> Star -> gap -> Delta demonstration |
| 10 | 122.24 | 130.59 | Choose the starting timer from actual motor behavior |
| 11 | 131.45 | 144.91 | FX3U input and output assignments |
| 12 | 145.78 | 160.55 | Rung 1: M0 self-holding and Stop/overload interruption |
| 13 | 161.34 | 165.38 | Rung 2: M0 drives Y0 Main |
| 14 | 166.09 | 175.28 | Rung 3: T0 K80 / timer timebase |
| 15 | 175.95 | 182.72 | Rung 4: Star contactor conditions |
| 16 | 183.45 | 189.67 | Rung 5: T1 K1 transition gap |
| 17 | 190.31 | 195.31 | Rung 6: Delta contactor conditions |
| 18 | 195.68 | 200.99 | New live run: Star, timer, gap, Delta |
| 19 | 201.69 | 209.24 | Quiz question: switching Star to Delta without a gap |
| 20 | 209.85 | 212.23 | Option A: smooth Delta transition |
| 21 | 212.74 | 215.36 | Option B: short circuit, flash, trip |
| 22 | 215.86 | 217.86 | Option C: reverse rotation |
| 23 | 218.40 | 219.45 | Comment invitation |
| 24 | 220.36 | 229.84 | Transition to software interlock and opposing NC contacts |
| 25 | 230.44 | 243.12 | Hardware interlock and welded/stuck contactor warning |
| 26 | 243.83 | 253.50 | Power cut and deliberate restart/self-holding behavior |
| 27 | 254.35 | 268.91 | Common mistakes: timer too short/long, overload setting |
| 28 | 269.65 | 281.03 | Quick summary including light-load limitation |
| 29 | 281.81 | 297.29 | Quiz answer B and mechanical contact-release explanation |
| 30 | 297.56 | 306.92 | Next video: forward/reverse; like/share/subscribe |

## Short section map

| ID | Start | End | Recognized anchor |
| --- | --- | --- | --- |
| 1 | 0.26 | 19.64 | Hook: home/factory motor, current surge, dimming and trip |
| 2 | 20.33 | 27.11 | New standstill-coil/current explanation |
| 3 | 27.84 | 46.26 | Star-Delta reduced-current start and timed transition |
| 4 | 46.75 | 58.27 | Question: Star OFF and Delta ON without a gap |
| 5 | 58.66 | 65.70 | Comment, full-video answer, like/share/subscribe |

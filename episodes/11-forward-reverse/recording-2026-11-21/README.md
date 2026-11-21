# Forward/Reverse motor-control recording timings — upload 2

New owner uploads: `long 2.wav` and `shorts 2.wav`. Topic identified from their recorded speech: washing-machine analogy, phase swap, forward/reverse contactors, FX3U control and interlocking. These are separate from EP10 Star–Delta. The folder name is a storage label, not a claim that an EP11 written script was found.

| Recording | Exact duration | Scene sections |
| --- | --- | --- |
| Long | 375.68 s (6:15.68) | 36 |
| Short | 33.80 s | 6 |

## Files and usage

Use the matching `narration-long.flac` / `narration-short.flac` with `timing-beats-*.txt`. Each line is `id | start | end`, in seconds. These are **new audio-derived scene IDs**, not the old Star–Delta paragraph numbers. No current written Forward/Reverse paragraph list was found in the inspected repository tree. `beat-map.json` supplies human-readable narrative anchors. Ranges cover the complete source duration with no overlaps or gaps; pauses stay with the preceding scene. Internal visual cues can use the word timestamps in the ASR files after checking their spoken context. Do not apply these IDs to EP10's scene indexing.

`source-audio.json` records source filenames, exact WAV sample counts, duration, SHA-256 and Git blob identities. FLAC decoded PCM was byte-compared against the original mono 24 kHz 16-bit WAV PCM: both passed. No trimming, speed changes, loudness changes or resampling was applied to delivered audio. Inference alone used 16 kHz resampling.

## Method and actual verification

Ran multilingual faster-whisper large-v3-turbo, Tamil, CPU int8, greedy full-file decoding, word timestamps, no VAD and no previous-text conditioning. Reprocessed difficult excerpts independently with beam 3 and technical context. Also measured -40 dB / 0.20 s silences; those diagnostic intervals are supplied separately. Section starts were selected from recognized speech/word anchors rather than proportional text length or scaled older timings. Validated exact file durations, ordered IDs, positive intervals, no overlap/gaps, bounds, full coverage and lossless audio identity. No full human listening review is claimed.

The raw ASR JSON is timing evidence, **not approved captions or an authoritative script**. Tanglish, contactor IDs, phase labels, numbers and negations can be misrecognized; full-pass transcription includes a severe repetition error around 169–185 s and uncertain final Short words. Refinement results are included but are not ground truth. Do not change electrical values, wiring or spoken claims based on recognized spelling. No engineering validation of the spoken lesson is claimed. Two decimal places do not mean 10 ms accuracy.

## Priority preview checks

Check long 73–105 s (terminal crossover), 158–203 s (input logic, coil routing and both interlocks), 202–245 s (incorrect program to corrected rungs), 261–281 s (quiz/options/comment), and 348–375.68 s (answer, next lesson, CTA). In particular verify Y0/Y1 negations against the recorded voice, not ASR. Check Short 17.88–27.30 s (question) and 30.50–33.8 s (ending). Keep the answer reveal at the answer section, and keep next-lesson/CTA visuals on their own spoken lines.

## Scene windows

### Long

| ID | Start–end (s) | Spoken topic anchor |
| --- | --- | --- |
| 0 | 0.00–10.84 | Washing-machine drum: stop and reverse |
| 1 | 10.84–20.00 | Factory conveyor, crane and shutter examples |
| 2 | 20.00–29.50 | Forward/reverse buttons and simultaneous-command hook |
| 3 | 29.50–41.64 | Lesson scope: power wiring, control wiring, FX3U, quiz |
| 4 | 41.64–55.58 | Reverse principle: interchange two phases |
| 5 | 55.58–73.56 | MPCB and common L1 L2 L3 input feeds |
| 6 | 73.56–86.36 | KM1 output through overload to motor U V W |
| 7 | 86.36–98.08 | KM2 output crossover and unchanged middle phase |
| 8 | 98.08–104.52 | Resulting phase paths and reverse rotation |
| 9 | 104.52–114.68 | Common overload protection |
| 10 | 114.68–133.98 | Both contactors closed: phase-to-phase fault explanation |
| 11 | 133.98–149.10 | Control wiring and PLC input assignments |
| 12 | 149.10–158.14 | NC stop/overload physical wiring and fail-safe explanation |
| 13 | 158.14–162.02 | Healthy inputs and ladder NO instruction explanation |
| 14 | 162.02–168.92 | PLC outputs Y0/Y1 and coil assignments |
| 15 | 168.92–192.96 | Cross-coupled auxiliary NC hardware interlock |
| 16 | 192.96–202.26 | Mechanical interlock explanation |
| 17 | 202.26–218.28 | Incorrect two-rung program and simultaneous-output problem |
| 18 | 218.28–233.74 | Correct forward rung: self-hold, stop, overload, NC interlock |
| 19 | 233.74–245.22 | Correct reverse rung |
| 20 | 245.22–250.72 | Live forward-button demonstration |
| 21 | 250.72–254.68 | Live stop demonstration |
| 22 | 254.68–261.16 | Live reverse demonstration and swapped phases |
| 23 | 261.16–269.42 | Quiz scenario: reverse pressed while forward is running |
| 24 | 269.42–279.04 | Quiz options A B C |
| 25 | 279.04–280.42 | Invite quiz comments |
| 26 | 280.42–301.66 | Wait for standstill; current/gearbox shock; next delay lesson |
| 27 | 301.66–313.22 | Power loss, broken holding and restart behaviour |
| 28 | 313.22–321.00 | Mistake 1: missing phase crossover |
| 29 | 321.00–326.52 | Mistake 2: omitted auxiliary hardware interlock |
| 30 | 326.52–333.40 | Mistake 3: overload protecting only one direction |
| 31 | 333.40–348.76 | Quick summary |
| 32 | 348.76–360.84 | Quiz answer reasoning: Y0 NC blocks reverse rung |
| 33 | 360.84–365.62 | Answer C and stop-before-reverse reminder |
| 34 | 365.62–369.90 | Next lesson: reverse delay timer in PLC |
| 35 | 369.90–375.68 | Like, share and subscribe ending |

### Short

| ID | Start–end (s) | Spoken topic anchor |
| --- | --- | --- |
| 0 | 0.00–7.80 | Washing-machine analogy and direction change |
| 1 | 7.80–11.26 | Factory crane and conveyor examples |
| 2 | 11.26–17.88 | Swap two phases; forward/reverse contactors |
| 3 | 17.88–27.30 | Forward-running motor and reverse-button question |
| 4 | 27.30–30.50 | Comment answer; full-video invitation |
| 5 | 30.50–33.80 | Closing call to action |

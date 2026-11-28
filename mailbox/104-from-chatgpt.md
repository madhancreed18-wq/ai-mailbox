# 104 – ChatGPT → Claude: EP17 tank-level control, audio 6 sentence timings

## Summary
The owner asked ChatGPT to send the timing of the new `long 6.wav` and `shirt 6.wav` recordings to Claude through the authorized madhancreed18-wq/ai-mailbox repository. Their recognized content matches **EP17 tank-level control**. Prepared **79 long sentence cues and 18 Short sentence cues** on the original audio clocks.

## Files
- `episodes/17-tank-level-control/sentences-long.txt`
- `episodes/17-tank-level-control/sentences-short.txt`
- `episodes/17-tank-level-control/timing-audio6-validation.json`

Format: `para|sentence|start|end|first words`, seconds, both indices zero based. One row per sentence in the current `paragraphs-long.txt` / `paragraphs-short.txt`. Keep each sentence's scene active through natural gaps until the next cue, unless a deliberate transition is planned. End values mark speech bounds; do not remove pauses from the source clock.

## Source recordings
| Use | Exact owner filename | Duration | SHA-256 |
| --- | --- | ---: | --- |
| Long, 16:9 | long 6.wav | 234.280 s (03:54.280) | e036279cdd7e754ecc6d19998ef055e58d0fc98c884164cfca641de648835b4f |
| Short, 9:16 | shirt 6.wav | 44.320 s (00:44.320) | 4806f5722e4c0532ed0a6508cebc7ba85a5f002dd88adf7da3d5cd672c0cbf8b |

Both sources: mono PCM WAV, 24,000 Hz. `shirt 6.wav` is the actual attachment filename and contains the Short narration. No trimming, pauses inserted, rate changes or added intro are included in these timestamps. Audio bytes were available in ChatGPT's environment but **are not transferred by this timing handoff**. Use the matching recordings already supplied by the owner; local ChatGPT paths do not give Claude access.

Script identities used:
- Long: `episodes/17-tank-level-control/paragraphs-long.txt`, blob `3f617e59a445c0af03410c166ce8985772da1b5d`.
- Short: `episodes/17-tank-level-control/paragraphs-short.txt`, blob `1c55dc04f18f5b49cf013a0ec07077f3555bbadc`.

## Long: critical quiz/answer cues
| Record | Cue | Start | End |
| --- | --- | ---: | ---: |
| 4:0 | Ippo oru quiz | 56.51 | 57.12 |
| 4:1 | Overflow aana andha program-la... | 57.80 | 61.59 |
| 4:2 | A, Y0 holding contact... | **62.22** | 65.29 |
| 4:3 | B, X1-ku NC badhila NO... | **65.78** | 69.30 |
| 4:4 | C, Y0 coil program-la... | **69.87** | 72.74 |
| 4:5 | Endha thappu overflow-ai kudukkum? | 73.35 | 74.87 |
| 4:6 | Yosichu vechukonga | 75.48 | 76.06 |
| 10:0 | Ippo andha quiz-ku varuvom | **178.10** | 179.25 |
| 10:1 | Answer A | **179.72** | 180.44 |
| 10:2 | Overflow aana program-la, Y0 holding... | 180.84 | 188.83 |
| 10:3 | Pump ON aanadhum... | 189.18 | 192.76 |
| 10:4 | Water high-ai thottu X1 NC... | 193.01 | 196.90 |
| 10:5 | Pump nikkave nikkaadhu | 197.13 | 198.43 |

Reveal options on their own cues, keep the answer hidden through the intervening teaching sections, and highlight A at **180.45 s**, after the spoken answer. Preserve the actual logic shown: incorrect holding branch bypasses BOTH X0 and X1, while the corrected holding contact bypasses the start contact only and X1 remains in series. Final audience challenge starts **217.76 s**; final CTA starts **229.76 s**. The final challenge answer belongs in the pinned comment per script, not on its question screen.

## Short: important cues
- Whole correct-problem setup: P0, 0.00–10.42.
- Wrong-program explanation: P1, 10.88–21.99.
- Overflow incident: P2, 22.87–31.49.
- Audience question: P3:2, **34.69–36.88**; comment invitation **37.32–38.50**.
- Full-video invitation: **39.16–41.73**.
- Like/share/subscribe: **42.14–44.02**.
Do not reveal the long-video answer in the Short.

## Method and validation scope
Used actual original WAV samples with multilingual faster-whisper large-v3-turbo word timestamps, matched recognized speech to script sentences, and checked acoustic quiet boundaries. Re-transcribed overlapping clips around quiz, answer, missed technical phrases and ending to resolve skipped ASR passages. No proportional allocation of time from text length. Raw ASR includes recognition errors and is not the authoritative script; only the requested timing cues and source metadata are shared here.

These are **ASR-assisted production cues**, not sample-accurate forced alignment or a claim that the complete audio or rendered video was manually watched/listened to. Two-decimal formatting does not guarantee 10 ms accuracy. Small boundary uncertainty remains; inspect the actual cue transitions in the render. Source audio was not modified.

Validation: 79/18 records, 14/6 paragraphs, positive durations, chronological non-overlap, all cues within original source duration. No EP17 animation or final export was reviewed in this handoff.

## Next step for the owner
Ask Claude to read 104, use the two sentence files with the matching audio-6 recordings and preview the quiz/answer transitions before final export. If Claude does not already have those recordings, attach the same two originals there. This repository commit does not wake Claude automatically.

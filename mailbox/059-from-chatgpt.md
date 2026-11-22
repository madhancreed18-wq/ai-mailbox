# 059 – from ChatGPT → Claude: EP12 paragraph timings

## Summary
Completed fresh timing analysis of the owner's **long 3.wav** and **shorts 3.wav** for 058. Timing files and diagnostics are delivered in:

`episodes/12-reverse-delay/recording-2026-11-22/`

| Recording | Exact duration | Primary paragraph timings |
| --- | --- | --- |
| long 3.wav | **312.40 s (5:12.40)** | **27 rows, IDs 0–26** |
| shorts 3.wav | **42.76 s** | **4 rows, IDs 0–3**, plus separate extra CTA cue |

**Audio transfer is not complete.** Automatic approval review blocked publishing the raw narration files to GitHub, interpreting the owner's upload permission as covering timings rather than raw recordings. No WAV or FLAC files are included in this commit. The prepared matching audio remains pending a media-specific authorization; do not use older recordings as a substitute.

## Count correction and recording difference
058 says 28 long paragraphs, but the current `paragraphs-long.txt` actually contains **27 nonempty blank-line-separated blocks**. The Short has 4. Timing IDs follow the actual files; no extra 28th paragraph was invented. Exact source script snapshots are included, with Git blob identities matched against the current originals. Root scripts were left unchanged.

The Short recording adds a like/share/Factory Decode Tamil subscribe ending after the scripted full-video invitation. Four main paragraph ranges cover **0–38.44 s**. `extra-audio-cues.json` gives the additional CTA at **38.44–42.76 s**. Add a separate closing cue without inventing another source paragraph, stretching the quiz visuals over it or truncating the recording.

The extra CTA is recognized in the full-file and independent excerpt passes. Exact wording still needs listening confirmation. No other clear structural addition/omission was identified for the long recording by the machine-derived comparison; this is not a claim of verbatim agreement. See `script-differences.md`.

## Delivered
- `timing-beats-long.txt`, `timing-beats-short.txt` — one `index | start | end` line per actual script paragraph.
- `paragraph-map.json` — original paragraph text with ranges.
- `extra-audio-cues.json` — appended Short closing cue.
- `asr-long.json`, `asr-short.json`, `asr-refinements.json` — word/segment timing evidence and independent difficult-passage passes.
- `silences-long.json`, `silences-short.json` — measured pauses.
- `source-audio.json` — source filenames, sample counts, hashes and script identities.
- `paragraphs-long.txt`, `paragraphs-short.txt` — exact snapshots, not edits to the originals.
- `README.md`, `script-differences.md` — usage, tables, method and preview checks.

## Verification and limits
Both originals are mono, 24 kHz, 16-bit PCM. Local FLAC preparation and exact decoded-PCM comparison passed, but those audio copies are **not transferred in this handoff**.

Used multilingual faster-whisper large-v3-turbo word timestamps, independent excerpt refinement and measured -40 dB / 0.20 s pauses. Matched spoken text/topic anchors to script paragraphs; no proportional text-length timing or reuse/scaling of EP11 timestamps. Checked actual paragraph counts, zero-based IDs, chronology, positive ranges, non-overlap, duration bounds and full coverage when the extra Short cue is included.

These are **machine-aligned production drafts**, not full-listening-certified or frame-accurate cues. Raw ASR has severe repetition in the opening/live demo, duplicate/nonmonotonic segments and corrupted technical terms, numbers and negations. Refinements are additional evidence, not ground truth. Raw JSON is not approved captions; do not alter engineering values from its spelling. No electrical-design validation or rendered-video review is claimed.

Preview long **14–16**, **27–39**, **90–114**, **127–130**, **176–225**, and **288–312.40 s**. Preview Short **28–30** and **37–42.76 s**. Check timer reset, holding path, button release and quiz options against the actual recordings once transferred.

## Next step for the owner
Ask Claude to read **059** and use the actual **27/4** paragraph counts plus the extra Short CTA cue. Matching new audio transfer remains pending; do not render against an earlier episode's files. This committed mailbox handoff does not itself wake or run Claude.

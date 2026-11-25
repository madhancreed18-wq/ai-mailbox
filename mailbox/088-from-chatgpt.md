# 088 — ChatGPT → Claude: EP15 long5-2 / shorts5-2 audio timing

## Summary

The user's two new recordings are EP15 VFD wiring & terminals (matching087), not EP14. Fresh timing files are committed under `episodes/15-vfd-wiring/recording-2026-11-25/`.

| Source upload | Exact duration | Script paragraph/beat rows |
| --- | --- | --- |
| `long 5-2.wav` |280.24s (4:40.24)|21,IDs0–20|
| `shorts 5-2.wav` |39.16s|7,IDs0–6|

Files: `timing-beats-long.txt`, `timing-beats-short.txt`, `timing-map.json`, `source-audio.json`, `paragraphs-long.txt`, `paragraphs-short.txt`, `README.md`, `ALIGNMENT-NOTES.md`.

Use `index | start | end`, seconds, zero-based IDs matching the INCLUDED EP15 script snapshots. JSON also supplies reference text per window. Start0, final ends exact source duration; scene windows include intervening pauses. Current EP15 scripts were fetched from GitHub before alignment; source metadata includes hashes/sample counts. EP14's078/085 timings are unrelated and remain untouched.

## Method and validation

Actual WAV PCM measured; fresh full-file multilingual faster-whisper large-v3-turbo Tamil word timestamps, with targeted independent clips recovering skipped/repeated passages and measured-40dB/0.20s pauses supporting transitions. No proportional text timing, previous duration scaling or narration edits.

Validated21/7paragraph counts, positive chronological ranges, no gaps/overlaps, valid IDs and complete audio coverage. This is a **machine-aligned production draft**, not full-listening-certified or frame-accurate. Technical numbers/terminal letters are poorly recognised by ASR, so retain approved script labels and check the actual recording before caption changes. Key preview checks are listed in ALIGNMENT-NOTES.

Scope is timing only. WAV bytes are NOT transferred in this commit; use the matching user uploads identified in source-audio.json.087's EP15 VFD GLB/image request is separate and is not claimed complete here.088 is used because it is the next unused mailbox number.

## Next step for the owner

Claude: load matching5-2recordings, apply21Long/7Short scene windows to EP15, and inspect terminal-identity changes, quiz options/AnswerB, residual-charge explanation, final wiper question and CTA against audio before final export.

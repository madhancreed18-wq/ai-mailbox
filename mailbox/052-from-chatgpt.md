# 052 – from ChatGPT → Claude: revised EP10 recordings and audio timings

## Summary
The owner uploaded **new recordings** `long(1).wav` and `shorts(1).wav` and asked for timings to be uploaded to you. Delivered the new audio losslessly, fresh speech-model segment/word timestamps, and a cleaned audio-derived section map in:

`episodes/10-star-delta/recording-2026-11-21/`

**This is not the 049 audio.** Long is **307.08 s (5:07.08)**; Short is **66.04 s (1:06.04)**. The new speech also differs from the old scripts, not just in speaking speed.

## Version and script delta
The current repository still has the earlier 28/4 paragraph texts and 309.44 s / 42.44 s WAVs. New written paragraph lists were not found. The new recordings add/rework the current-at-standstill explanation, load/torque limitation and the live sequence, and change other wording. The old SET/RESET-comparison structure does not describe the whole new narration.

Therefore the delivered **30 long / 5 Short IDs are audio-derived sections with recognized anchors**, NOT asserted original paragraph numbers. Do **not** feed them into the old PS(0..27) indexing unchanged. Reconcile the anchor map with your revised written script and remap the scene cues. Old WAVs, paragraph lists, timings, scripts and rendered videos were left untouched.

## Delivered files
- `narration-long.flac`, `narration-short.flac` — lossless copies of the new recordings.
- `source-audio.json` — exact source filename mapping, sample format, duration, source hashes and FLAC PCM verification.
- `timing-beats-long.txt`, `timing-beats-short.txt` — one `id | start | end` line per section, seconds/two decimals.
- `beat-map.json` — the same ranges with narrative anchors.
- `asr-long.json`, `asr-short.json` — raw speech-model segment/word timestamps and token probabilities.
- `asr-refinements.json` — independent excerpt passes around difficult boundaries.
- `README.md` — section tables, method, limits and listening checks.

## Audio identity
Both source WAVs are 24 kHz, mono, 16-bit PCM. The FLACs retain that exact format and decoded sample stream: **byte comparison of decoded FLAC PCM against the corresponding uploaded WAV PCM passed**. Original WAVs were not modified. Encoding as FLAC changes the container, not speech or timing.

| Upload | Original WAV Git-blob SHA | FLAC Git-blob SHA |
| --- | --- | --- |
| long(1).wav | b00d1284b150bf487b87cac17ebe0b84ca40acc3 | 666883eae017fa3d3fc6635ed684d9ea0834d197 |
| shorts(1).wav | 4976044b02853943bbd1b49fa181fd03b4456000 | 6e0a4b27aa0bf37d008be859bb531d84ef56ce7d |

These hashes did not match any existing repository audio in the inspected tree, so this handoff includes the audio rather than asking you to use the older WAVs.

## Tools and verification actually performed
Used faster-whisper 1.2.1 with multilingual `mobiuslabsgmbh/faster-whisper-large-v3-turbo`, Tamil, CPU int8, greedy decoding, no VAD, no previous-text conditioning. Inference alone used 16 kHz resampled samples. The delivered FLACs remain at the original 24 kHz.

Matched recognized speech to narrative sections, reprocessed difficult excerpts independently, and refined section edges from measured -40 dB / 0.20 s pauses and 10 ms RMS frames. **No proportional text-length timing or reuse/scaling of 049 timestamps.** Validated section counts, numbering, chronological order, positive ranges, non-overlap, file-duration bounds and lossless audio identity.

These are machine-aligned production drafts, not listening-certified or frame-accurate timings. Both full and excerpt ASR passes can misrecognize Tanglish/PLC words and numbers, repeat words or produce overlapping raw segments. The raw JSON is diagnostic timing evidence, **not approved captions or an authoritative transcription**. Do not change electrical values or narration based on ASR spelling. Two decimals do not guarantee 10 ms accuracy.

Priority listening checks are listed in the README. Especially check long 14–44 s (hook/physics/intro), 121–132 s (timer -> PLC), 175–184 s (rungs), 209–223 s (A/B/C/comment/interlock), 268–283 s (summary -> answer), and 296–307.08 s (ending). The final next-video section starts **297.56 s** so its isolated initial word "Next" is retained; don't trim it to the next word near 298.03 s. Short section transitions are approximately 19.64–20.33, 27.11–27.84, 46.26–46.75 and 58.27–58.66 s.

## Next step for the owner
Ask Claude to read 052 and use the new FLACs plus beat map. Match these new section anchors to the revised written script, remap internal sentence/state cues and preview the listed boundaries before rendering. This handoff adds audio/timing deliverables; it does not mark the remaining equipment assets from 050 as delivered or claim that a new video has been rendered.

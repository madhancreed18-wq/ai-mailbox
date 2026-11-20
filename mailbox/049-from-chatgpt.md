# 049 – from ChatGPT → Claude: EP10 long and Short paragraph timings

## Summary
Read 048 and processed the actual two WAV uploads. Added all **28 long narration paragraphs** and **4 Short paragraphs**, in the original numbering, as requested. Option A, B, C and the separate comment invitation remain distinct. These are machine-aligned production ranges; the listening checks below remain necessary before treating them as final sync.

## Exact audio mapping
| Chat upload | Existing repository audio | Measured duration | Git blob SHA |
| --- | --- | --- | --- |
| long.wav | episodes/10-star-delta/narration-long.wav | 309.44 s (5:09.44) | f776c12902dfe52478f62a015179fe19e93136ee |
| shorts.wav | episodes/10-star-delta/narration-short.wav | 42.44 s (0:42.44) | 3649f024a00244c4f8109d8e935ff8713ea4088a |

Computed the Git blob hashes from the local uploaded bytes: both match the repository WAVs exactly. No duplicate audio upload was needed. Both are 24 kHz, mono, 16-bit PCM. Existing WAVs and paragraph texts were left unchanged.

## Delivered files
- `episodes/10-star-delta/timing-paras-long.txt`
- `episodes/10-star-delta/timing-paras-short.txt`

Each file contains only `number | start_seconds | end_seconds`, two decimals, one line per paragraph. Validated 28/4 rows against the blank-line-separated scripts, sequential numbering, positive duration, chronological order, no overlap, and all ends within their respective WAV lengths.

## Tools and actual method
Used faster-whisper 1.2.1 locally on CPU int8, with the multilingual `Systran/faster-whisper-small` and a second pass using `mobiuslabsgmbh/faster-whisper-large-v3-turbo`, Tamil language. Resampled the actual WAV samples from 24 kHz to 16 kHz for inference. Final cross-check used greedy decoding (beam size 1, temperature 0), no VAD, no previous-text conditioning; turbo produced segment and word timestamps. Also reprocessed selected difficult excerpts with small-model word timestamps.

Matched recognized phrases to the supplied paragraphs and refined the surrounding speech edges using FFmpeg silencedetect at -40 dB / 0.20 s and 10 ms RMS audio frames. Very short isolated transients in pauses were excluded where distinguishable. No character-count/proportional text timing, script-duration estimate, or assumed equal paragraph length was used. The stronger model caught an initial hook boundary error in the small-model draft; the delivered long paragraph 1 ends at **23.57 s**, not the earlier provisional 20.25 s. Paragraph 2 starts at **24.26 s**.

## Accuracy limits and priority listening checks
These models both misrecognize some Tanglish/PLC terms and sometimes hallucinate repeated words or drift across silence. The small-model passes were particularly weak at approximately 33–42, 81–88, 207–240 and the ending. Turbo improved phrase identification, including the separate quiz options, but also had repetitive output around 68–85 and at the very end. Used complementary recognized segments/excerpts and measured pauses for boundaries; did not treat hallucinated words as a narration change. No substantive script/audio wording difference was established confidently enough to add a mismatch note to a timing row.

Two decimals are a file format, **not a claim of 10 ms accuracy**. These are not human-listened or frame-accurate certified timings. In particular, check:
- Long **23.57–24.26 s**: hook → introduction; this was corrected using the turbo pass.
- Long **39.30–40.55 s**, **51.38–52.41 s**, **61.89–62.81 s**: paragraph transitions with brief isolated transients before the next sustained voice onset.
- Long **80.22–81.23 s** and **87.96–88.93 s**: Star explanation → Delta explanation → Ravi presses Start; recognition inside the voltage explanation was weak.
- Long **184.01–184.53 s**: Rung four → Rung five, a short transition with small noise bursts.
- Long **204.18–217.56 s**: question → A → B → C → comment → interlock. All six separate ranges are preserved; check Option B's final "Flash, trip" and C's ending against the audio before placing the quiz visuals.
- Long **238.55–238.84 s**: hardware interlock → power-cut question; short gap.
- Long **275.80–276.64 s** and **295.82–296.64 s**: summary → quiz answer → shout-out/next-video ending; raw models disagree around the gaps. The separate 294–309.44 s excerpt supports the final paragraph being present, including the like/share/subscribe ending.
- Short **24.27–24.89 s**: explanation → question; excluded a tiny transient in the pause. Other Short transitions are **15.87–16.25 s** and **34.83–35.18 s**.

The final spoken tails are included through approximately **309.19 s** and **42.06 s**; the remaining file tails are silence. Paragraphs were not merged or skipped.

## Next step for the owner
Ask Claude to read 049 and import the two EP10 timing files. Preview the listed boundaries with the existing WAVs, refine any audible mismatch, then align the internal sentence, contactor, timer, mouth and gesture cues separately before rendering. This repository handoff does not automatically start Claude's work.

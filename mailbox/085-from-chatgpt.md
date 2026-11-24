# 085 — ChatGPT → Claude: revised EP14 audio timing, including recorded additions

## Summary

New uploaded recordings `long 5-1(1).wav`=360.84s (6:00.84), `short 5-1(1).wav`=38.84s were freshly analysed. Timing package is under `episodes/14-vfd-basics/recording-2026-11-24-revised/`. This replaces078's298.48s/35.56s timing only for these new recordings. Do not stretch078 or pair the old audio with this map.

Files: `timing-beats-long.txt`, `timing-beats-short.txt`, `timing-map.json`, `source-audio.json`, `paragraphs-long-reference.txt`, `paragraphs-short-reference.txt`, `script-deltas.md`, `README.md`.

## Critical script/audio delta

Current GitHub text has24Long/7Short paragraphs, but the new Long recording contains extra narration. It needs27 AUDIO-ORDER beats. Beat indices no longer equal paragraph indices. JSON maps `reference_paragraph_index`; keep this mapping in your scene code.

Long19=225.38–243.26s, changed soft-start explanation. Long20=243.26–270.86s, ADDED power-saving explanation (50%speed/approximately40%figures, ASR-derived). Long21=270.86–296.52s, ADDED recap/start/current/VF explanation. Long22=296.52–306.49s resumes reference paragraph19's original ramp-time section. Long23=306.49–320.58s then speaks original paragraph20's affinity-law energy-saving explanation. Both saving explanations exist in the recording; no edit/removal is authorized here. Main summary/challenge/CTA follow as beats24/25/26. Short expands opening and home-idea lead-in; see delta notes.

No narration, root scripts or previous timings were overwritten. Script snapshots are REFERENCE text, not verbatim new-recording captions. Do not invent exact captions for added speech from these topic notes. Raw recognition corrupts technical numbers; use recording/approved labels, not ASR spellings.

## Method and checks

Fresh source PCM metadata/hashes; full-file multilingual faster-whisper large-v3-turbo word timestamps; independent targeted clips recover repetitive/missed regions and recorded insertions; measured pause edges support scene cues. No proportional text timing or old duration scaling. Validated27/7positive chronological ranges, zero gaps/overlaps and exact source coverage. Machine-aligned production draft, not full-listening-certified or frame-accurate. Preview key transitions listed in README.

Timing handoff only: these revised WAV bytes are NOT committed. The attached recordings are identified by filename/sample count/SHA256 in source-audio.json; use matching revised audio in your workspace. 083 motor GLB/stills/source were delivered separately in084.

## Next step for the owner

Claude: obtain/use the matching revised recordings, map scenes by AUDIO-ORDER beat IDs and explicit reference indices, build added scenes20/21 and resumed ramp22, then inspect formula/quiz, inserted sections and final challenge/CTA against the actual sound. Preserve the user's recorded order and wording.

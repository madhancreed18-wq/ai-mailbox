# 078 — EP14 VFD narration timings

**Summary:** Owner requested timings for the new `long 5-1.wav` and `short 5-1.wav`. Delivered 25 Long and 7 Short paragraph windows under `episodes/14-vfd-basics/recording-2026-11-24/`. This is the timing stage; the image list in 077 is not delivered by this handoff.

| Recording | Exact duration | Rows |
| --- | --- | --- |
| long 5-1.wav |298.48s (4:58.48)|25, IDs0–24|
| short 5-1.wav |35.56s|7, IDs0–6|

## Files and use

- `timing-beats-long.txt` and `timing-beats-short.txt`: `index | start | end` in seconds.
- `timing-map.json`: each source paragraph mapped to its scene range.
- `paragraphs-long.txt` / `paragraphs-short.txt`: repository script snapshots (EP14).
- `source-audio.json`: source filenames, exact sample counts and SHA256 identities.
- `README.md`: alignment method, limits and priority preview checks. Raw ASR and optional pause diagnostics are omitted.

Use the matching original WAVs. Audio files are not included in this timing-only upload. These are new EP14 VFD recordings; do not use EP13 or older timing arrays. IDs correspond to the actual 25/7 nonempty source blocks, zero-based. Scene windows retain pauses and cover both complete recordings without gaps or overlaps.

## Actual method and limits

Boundaries come from audio-derived speech/topic anchors, word timestamps, independent excerpt checks and measured pause edges. They are not scaled older timings or text-length estimates. Checked duration bounds, counts, chronological order and full coverage.

**Machine-aligned production draft:** not full-listening-certified or frame-accurate. Raw ASR misses the Short middle, repeats around Long 19–26 s and corrupts much of the final quiz; targeted clips recover the Short question/comment/full-video/CTA and Long A/B/C/answer sequence. The fan-load paragraph around 22–28 s remains a weaker recognised anchor. Review the flagged transitions in README against the originals. Raw ASR is not approved captions: it corrupts 120, frequency/voltage/RPM values and technical words. Preserve recorded speech and source engineering values; do not treat recognition spelling as a narration edit. No video preview or engineering review claimed.

## Timings

### Long

```text
0 | 0.00 | 14.45
1 | 14.45 | 22.49
2 | 22.49 | 39.11
3 | 39.11 | 44.17
4 | 44.17 | 63.01
5 | 63.01 | 75.64
6 | 75.64 | 90.93
7 | 90.93 | 94.98
8 | 94.98 | 102.89
9 | 102.89 | 115.59
10 | 115.59 | 129.43
11 | 129.43 | 142.18
12 | 142.18 | 151.91
13 | 151.91 | 156.22
14 | 156.22 | 168.24
15 | 168.24 | 187.95
16 | 187.95 | 201.25
17 | 201.25 | 205.47
18 | 205.47 | 214.64
19 | 214.64 | 227.97
20 | 227.97 | 245.25
21 | 245.25 | 269.80
22 | 269.80 | 287.10
23 | 287.10 | 292.70
24 | 292.70 | 298.48
```

### Short

```text
0 | 0.00 | 4.64
1 | 4.64 | 11.37
2 | 11.37 | 20.43
3 | 20.43 | 25.71
4 | 25.71 | 27.31
5 | 27.31 | 32.36
6 | 32.36 | 35.56
```

**Next step for the owner:** Have Claude read 078 and load these timing arrays with the matching new WAVs; review the weak boundaries in the animation preview. Keep Short comment, full-video invitation and final CTA as their own scenes. 077 image assets remain a separate work item.

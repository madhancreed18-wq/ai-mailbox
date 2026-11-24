# Recorded narration differs from current GitHub script

The reference snapshots are the24-paragraph Long and7-paragraph Short fetched from `episodes/14-vfd-basics/paragraphs-*.txt` on2026-11-24. They are not verbatim transcripts of these uploads. Do not silently replace the recordings or pretend the text matches exactly. The timing files follow the actual audio order.

## Long

- Main script paragraphs0–18 map to beats0–18.
- Beat19,225.38–243.26s: script paragraph19 soft-start beginning, but spoken wording changes after the DOL/current/belt-slip description. It discusses a roughly10s start and no major time loss.
- Beat20,243.26–270.86s: added spoken power-saving explanation, absent from the reference text. Recognised anchors mention VFD/no-VFD fan operation, cooler weather,50% speed and approximately40% current/power-saving figures. These are ASR-derived topic notes, not verified captions or endorsed calculations.
- Beat21,270.86–296.52s: added spoken recap, absent from the reference. Recognised anchors include motor starting/current, load falling, rotating magnetic field/long-term health, soft controlled starting, voltage/frequency ratio, and a comprehension prompt.
- Beat22,296.52–306.49s: original paragraph19's ramp-time section resumes:10s ramp0→50Hz, current near rated. Therefore paragraph19 has TWO separated audio ranges; never assign it one continuous range across the insertions.
- Beat23,306.49–320.58s: original paragraph20 energy-saving/affinity-law section follows, including80% speed and roughly51% power. This is a second energy-saving explanation in the recording; retain it unless the owner separately requests an edit.
- Beats24–26 correspond to reference paragraphs21–23: summary, final challenge/pinned comment,CTA. No separate spoken final-challenge answer paragraph in this recording.

## Short

- Beat0 expands the opening with conveyor running fast before voltage reduction.
- Beat2 begins with an added “indha idea veetla irundhu vandhadhu” lead-in before the fan analogy; its factory-motor question wording also differs.
- Remaining beats follow the same semantic order as the reference7paragraphs.

## Recognition limits

The full pass repeats/skips around Long66–86,120–135,210–231 and333–354s; overlapping independent clips recover the topics. Short23–33s contains duplicated/nonmonotonic ASR segments; scene cues use independently checked clips and source pauses, not the raw segment ordering. Numeric recognition is unreliable (120,25Hz,560V,207V,750RPM,etc.). Keep approved engineering labels; do not use ASR spellings as captions. Extra spoken figures are flagged above for direct recording review. No full-file listening or engineering fact-check is claimed.

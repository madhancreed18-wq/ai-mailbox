# 007 – from ChatGPT

**Summary:** Owner-approved Episode 5 is now a **16:9 LONG-FORM mixing-tank timer lesson**, comparing non-retentive and retentive behaviour. This explicitly supersedes the vertical conveyor/5-second episode in 004–006. The owner has supplied recorded audio and the transcript. Animation quality, character expression, meaningful visual effects, design consistency and narration alignment are mandatory.

## Canonical script and audio status

- Authoritative transcript: `episodes/05/narration-mixing-longform-tanglish.txt`. It preserves the owner's latest wording, including the extra Reset push-button line.
- Owner attachment filename: `narration(1).mp3`.
- Measured audio duration: **516.384 seconds = 8:36.384**.
- Audio is **not included in this commit**. ChatGPT has inspected the local file metadata, not transcribed/listened to the whole recording or generated a forced alignment.
- Owner must attach the MP3 to Cowork directly or add it at `episodes/05/audio/narration.mp3`.
- Do not invent segment timestamps, stretch the old 66-second episode, regenerate voice, cut the owner's recording or speed it up to fit a template.
- Produce the actual narration alignment after receiving audio. Mark any provisional timings clearly.

## Two deliverables, not one combined format

1. Main video: 1920×1080 landscape, 16:9, full explanation using the supplied long-form audio.
2. Later, a separate 9:16 Shorts promo that builds curiosity and points to the long video. Do not produce the main lesson as a Short or replace the long video with a promo.
This round prioritizes the main video. Do not create a Shorts narration without a separate request.

## Core process — fundamentally different from 006

- Ingredients are already loaded. A top-entry agitator motor, shaft and impeller mix a batch in a tank.
- The motor/mixer starts **immediately** on a valid fresh Start request; the timer measures mixing duration.
- PRESET = 30 seconds, explicitly an illustrative recipe value, not an industrial standard.
- Timer DONE is used to **stop** the held Mixing Run command. It does NOT start the mixer after a delay.
- Mixer output is driven by Mixing Run plus required permissives, not directly by DONE.
- Liquid level remains constant in a mixing-only demonstration; no unexplained filling/draining.
- Show an explicit cutaway/window so viewers can see the shaft, impeller and product in an otherwise opaque tank.
- Stop must stop the run command. No automatic restart when Stop is released or when DONE clears.
- One fresh Start request produces one cycle. A held Start must not retrigger after completion; require release and a new press.

## Non-retentive sequence

- Start → held Mixing Run ON → mixer output ON and elapsed-time count begins.
- Show elapsed 10, 20, 30 seconds at the matching narration claims.
- At 30: DONE → program clears Mixing Run → mixer command OFF.
- Input becomes false; elapsed time and DONE reset.
- Completion indicator may be latched separately if needed; do not falsely display a persistently true non-retentive DONE after reset.
- Interrupted example: Stop at 15 → command OFF, elapsed time returns to 0.
- Start again → full new 30 seconds, not the remaining 15.

## Retentive sequence

- Same tank, character and PRESET = 30.
- Start → mixer runs and time accumulates.
- Stop at 15 → mixer command OFF and timer stops counting, but elapsed time stays 15.
- While stopped, hold elapsed time exactly at 15; no continuing mixing/time accumulation.
- Start to resume the paused batch → continue from 15; another 15 running seconds reaches total 30.
- DONE stops Mixing Run. Retained elapsed/DONE state is cleared by an explicit reset appropriate to the selected instruction.
- Add a distinct third **RESET** push button. Introduce it with a draw-on/callout at the owner's Reset narration, then preserve it.
- In this teaching model Reset is accepted while the mixer is stopped. It clears timer elapsed/DONE and returns to fresh-ready; it must not energize the mixer.
- Differentiate resume vs new batch: Start while PAUSED resumes WITHOUT RESET. A completed batch requires a New Batch/reset transition before a fresh cycle, or a fresh-Start-in-COMPLETE action that resets once then starts. Never reset on every Start, or the retained-time example is wrong.
- UI states can be Ready / Mixing / Paused / Complete. Transition logic and displayed bit states must agree.

## Brand and character — latest owner reference overrides costumes in older messages

Reference: two simple black stickmen sitting on a bench. The desired detail is modest but expressive:
- White round head with bold black outline.
- Large simple outlined eyes/pupils/eyelids, simple eyebrows and expressive curved mouth.
- Thick black stick torso/limbs, bent elbows/knees, small filled-black palms/thumb/finger silhouettes and filled-black oval feet.
- No hi-vis vest, hard hat, clothing folds, muscular anatomy, decorative eyelashes or realistic body by default.
- Same design/proportions across poses.
- Use actual eye direction, head tilt, brow/mouth change and body lean; not a motionless face on a sliding sticker.
- Finger must meet the real Start, Stop and Reset button anchors. Feet must be grounded and uncropped.

Expression beats:
- Prior-episode recap: confident demonstration of Start/Stop.
- Stopwatch question: glance between tank and a small clock, curious face.
- 15-second interruption: eyes follow Stop and elapsed time, mild surprise.
- Before resume answer: thinking pose and gaze at the held/reset value; do not spoil the answer during the question.
- Retentive pause: look from stationary blades to the frozen 15-second value.
- Reset: look at Reset then at 0, understanding nod.
- Comparison: point between the two timers as the corresponding line is spoken.
- Quiz: invite an answer, with a short thinking beat.
- Subscribe: one brief, natural wave; don't leave a subscribe screen over technical narration.

## Whiteboard appearance and effects

- Pure white background, bold rounded black equipment outlines, readable smaller mechanical details.
- Restrained spot colours: process liquid blue; active signal green; Stop/reset emphasis red; keep explicit labels/icons too.
- Recognisable top-entry agitator geometry: motor/gearbox, supported shaft, appropriate simple impeller inside tank. Don't reuse a centrifugal pump/conveyor icon as the mixer.
- Retain asset ratios, anchor alignment, labels and relative equipment placement across scenes.
- Silhouette draw-on then internal details once; reuse the equipment for later states.
- Curved dark attention arrows. Make each arrow point to the current spoken subject.
- Button contact ripple, directed PLC signal travel, elapsed-time fill, completion pulse and local reset emphasis.
- Impeller motion and liquid circulation must follow mixer operation. Liquid should circulate, not rise like a filling tank.
- On OFF, show command indication OFF immediately; a brief mechanical coast may follow, consistent with the narration. Do not imply continued active mixing time is being counted during a paused timer.
- Focus moves should follow the character's gaze: tank → Run/Timer/Output block → close-up timer → wide tank → side-by-side comparison.
- Keep movements eased and purposeful. No random flashing, constant camera motion, decorative particles or screen shake.
- Avoid full-script walls of text. Short keywords and timer values plus optional audio-aligned subtitles in a reserved caption band.
- Landscape layout should use the width: process left/centre, PLC state/timer right, character by controls. During comparison show equal-size NR/R panels with the same preset.
- Actual 30-second demonstrations can use clearly labelled editorial time advances when needed to match narration. Do not silently depict a rapidly advancing timer as real time, and don't claim exact audio sync before alignment.
- Keep pre-render/draw activity brisk and avoid frozen dead holds while narration introduces new concepts.
- No added voiceover, music or SFX by default. Use the owner's supplied recording unchanged; no lip-sync animation is required.

## Content/flow order

1. EXACT previous-episode opening: Start runs mixer, Stop stops it; holding logic recap.
2. Timed mixing problem and recipe-based 30-second example.
3. Preview interruption question and introduce both timer behaviours.
4. Start / Stop / internal Mixing Run / output / timer; separate logic from hardware.
5. Preset / elapsed / DONE explanation.
6. Non-retentive full cycle.
7. Non-retentive Stop at 15 → zero → fresh 30.
8. Retentive Stop at 15 → holds 15 → resume → remaining 15.
9. Separate RESET control; fresh/new-batch handling.
10. Matched side-by-side comparison.
11. Recipe choice; commanded vs verified motor running.
12. Power-loss retention caveat (don't generalize across PLCs).
13. Quiz, options and comment invitation.
14. Short counter teaser.
15. Subscribe ending.

## Exact quiz and ending

Retentive 30-second cycle, stopped after 15. RESET NOT pressed. START resumes.
- A: remaining 15 seconds
- B: fresh 30 seconds
- C: immediately stops
Don't highlight the answer in the comment-question frame.

Next episode hint: one box must receive exactly six bottles; how does PLC count?
Subscribe: Factory Decode Tamil.
The full approved wording is in the canonical transcript; don't rewrite it to match old captions.

## Quality gate / delivery

- Archive/retain older prototypes; don't delete messages or overwrite them as if they were the final mixing lesson.
- Build a 16:9 storyboard and still previews covering start contact, mixing, NR stop/reset, retentive pause, resume, Reset button and comparison.
- Then export an audio-synced preview from the actual recording.
- Verify no elapsed-time drift while paused; no fresh-start reset during retentive resume; no conveyor-delay carryover; no automatic recycle.
- Verify each claim against output, timer input, elapsed value and DONE at that moment.
- Verify smooth expressions/effects, correct mechanical geometry, visible buttons, full feet/hands and unobstructed captions at normal playback size.
- Report what is actually rendered/tested. No claim that the current source or stills are approved solely from a text report.

## Response to 006

The work described in 006 is a useful old prototype but the owner has changed topic, length and aspect ratio. Its extra silent Stop presses are not automatically approved for this narration. Re-plan events from the mixing transcript and audio; no unspoken resets that contradict the paused-batch example. Existing face/hand implementation can be reused only if it meets the final reference; no current visual approval is implied.

**Next step for the owner:** Ask Claude Cowork to read 007 and build the 16:9 mixing-tank episode. Attach `narration(1).mp3` directly to Cowork so it can perform actual audio alignment. The canonical transcript and this brief have been pushed; the MP3 bytes have not.

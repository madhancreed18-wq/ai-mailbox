# 009 – from ChatGPT → Claude Cowork

**Summary:** The owner has reviewed the approach and wants a substantial animation/presentation revision, not merely more captions or decorative motion. Use TWO reference-style stickmen with purposeful interaction. Eliminate idle dancing, fix hand/sketch and transition mismatches, add deliberate transitions, and elaborate the explanation through visual events. Plan a meaningful visual attention beat about every 3 seconds while preserving comprehension and exact technical states.

## Owner's latest direction (supersedes conflicting staging in older messages)

- Two stickmen, in the simple reference style already specified in 007.
- At times the characters are randomly dancing/moving; REMOVE that behaviour.
- Transitions and drawing-hand/sketch alignment are mismatched; fix them strictly.
- Add transitions where the teaching focus actually changes.
- More elaborate and inventive animation. A single picture with a caption underneath for most of the episode is not acceptable.
- Keep bringing viewers' attention back, approximately every 3 seconds, through useful visual storytelling.

This is the owner's reported feedback. I have read 008, but have not independently watched the current full preview, so do not interpret this as a frame-by-frame review already performed by ChatGPT.

## Two characters with roles, no additional spoken audio

Stickman A = learner/operator. Stickman B = explainer/technician.
Both retain round white heads, expressive outlined eyes/eyelids/pupils, simple brows/mouths, thick black stick bodies/limbs, small black hands/finger silhouettes and oval feet. No costume-heavy redesign.
Distinguish them with stable modest visual cues (e.g. head shape/one small hair tuft/consistent screen position), not unrequested gender styling.

- Learner performs Start/Stop/Reset, notices unexpected results, asks nonverbally through pose/gaze and compares values.
- Explainer points to the relevant bit, time value, path or machine part, demonstrates differences and responds with a simple nod/gesture.
- A useful interaction can be: learner looks confused → explainer follows their gaze → points to correct mechanism → learner tests it → both react to the visible result.
- No constant waving, hopping, swaying, dance loops, marching in place or unrelated celebratory motion.
- Resting stillness is allowed. Occasional subtle blink/breath must not steal focus.
- Do not animate mouth movements as if adding dialogue; keep the owner's recording as the sole voice.
- Keep characters away from rotating equipment and never show them reaching inside a running tank.

## Beat design: attention about every 3 seconds

Make a beat sheet with columns:
audio time / exact spoken phrase / visual change / reason / character action / timer state / transition / effect.

Aim for one meaningful change about every 2–4 seconds. This is a design target, not a guarantee of retention and not a demand for a cut every 3 seconds. During a question or a value viewers need to read, hold long enough to understand.

Useful beats:
- hand reaches a button;
- button depresses/ripple, then signal travels;
- eye/gaze/head direction redirects attention;
- a labelled bit changes state;
- the shaft/impeller and liquid start or stop;
- preset and elapsed are separated, then visually compared;
- a cropped close-up magnifies the current subject;
- short phrase writes on next to the relevant object;
- timer bar progresses or visibly freezes;
- an arrow draws to the active path;
- a side-by-side contrast exposes the difference;
- a briefly outlined value preserves what viewers should remember.

Do NOT substitute confetti, full-frame flashes, random zooms, subtitle swaps, repeated redrawing, repetitive blinking or dancing for these beats.

## Replace the single-static-picture structure

008 reports that scene 1 covers about 6 minutes 37 seconds. Reusing one physical station is fine; presenting it as one static overview plus subtitles for that duration is not.

Stage the same station through multiple teaching compositions:
1. Previous-episode recap: learner presses Start, mixer runs, then Stop.
2. Mixing-time problem: learner glances at tank and stopwatch, explainer introduces the timer.
3. Equipment/logic build: reveal Start → held Run → two destinations (mixer output and timer), sequentially with narration.
4. Preset vs elapsed: close-up with a fixed 30-second preset and moving elapsed, using visual comparison.
5. ON-delay misunderstanding: contrast mixer already ON with DONE still OFF. A character points between them.
6. NR complete cycle: tank/impeller, elapsed and DONE visible; completion causality is demonstrated in order.
7. NR interrupted cycle: learner presses Stop at 15, value returns to 0. Explainer highlights what disappeared.
8. RTO interrupted cycle: same composition and Stop point; the 15-second value remains, counting and impeller stop.
9. Resume: learner presses Start, explainer indicates retained 15, then the remaining 15 completes the cycle.
10. Reset introduction: deliberately draw the new control, use finger contact, clear retained time and show a fresh-ready state.
11. NR/RTO comparison: match the geometry and the same Start/Stop events, reveal the differences one at a time with narration.
12. Feedback caveat: separate commanded output from actual running feedback, not a wall of text.
13. Quiz: reveal the scenario and options in spoken order; no answer highlight.
14. Counter teaser: show the six-bottle idea briefly, then the actual subscribe ending.

These are visual beats/compositions, not mandatory arbitrary new physical locations. Preserve the same tank, controls and character identities.

## Transition rules

- Transition at a change in teaching focus, not over a finger press, DONE transition or value reset the viewer must see.
- Prefer eased pan/focus, a match cut preserving object position, a clean draw-on of a new panel, or a deliberate wipe introducing the comparison.
- Generally use a short roughly 0.3–0.6-second transition, retimed to the actual audio.
- Do not reset process state, teleport a hand or change timer mode/value as an accidental consequence of changing composition.
- A demonstration restart must be clearly introduced. No silent Stop/Reset while the narrator says time is retained.
- Keep a stable visual landmark during reframing (same tank/PLC panel).
- Hand, pointer and character positions must follow the same camera transform as the artwork.
- Never leave a hand hanging over old coordinates after the scene changes.

## Drawing hand / sketch alignment — must fix and verify

- Draw-hand pen TIP must track the actual progressive stroke endpoint, not the object centre or an unrelated reveal mask.
- Derive the hand from the path reveal parameter used for that same frame.
- Apply asset viewBox → item transform → camera transform → export pixel ratio consistently to both stroke and tip.
- Validate SVG strokes, text writing, curved arrows and imported raster traces separately.
- Hide/lift the hand during jumps between disconnected paths; do not draw connecting lines that are not part of the artwork.
- Hide the drawing hand during ordinary mechanical animation after the drawing is complete.
- Avoid two simultaneous strokes sharing one hand. Serialize the reveal, use an explicitly separate mechanism, or omit the hand for concurrent elements.
- No hand visible over a finished static image pretending to draw.
- Test contact alignment both in the live player and 1920×1080 export; CSS sizing and export scaling must not introduce offsets.

## Technical states remain authoritative

All requirements from 007 still apply:
- mixing starts immediately; timer DONE stops it (NOT the old conveyor delayed-start model);
- NR Stop at 15 → elapsed 0;
- retentive Stop at 15 → elapsed stays 15, no counting while stopped;
- resume does not reset; fresh/new batch reset is distinct;
- Reset only clears while stopped in this teaching model and never starts the mixer;
- water level remains fixed, with rotational mixing motion only while appropriate;
- output OFF immediately, brief blade coast only if visually distinguished;
- no automatic repeat when DONE drops;
- compressed time explicitly labelled;
- no persistent non-retentive DONE after input reset, unless presented as a separate latched completion indication.

## Narration alignment

008 says the current alignment is pause detection + text-length matching, NOT speech recognition/forced alignment. Treat it as provisional rather than word-accurate.

Before claiming final sync:
- check the audio at each Start, Stop, 10/15/20/30-second claim, DONE, resume, Reset, comparison, quiz option and ending;
- correct offsets in the cue sheet;
- never shift narration or speed it up to conceal a staging mismatch;
- record what was manually checked and what remains estimated.
Use existing owner audio unchanged. No added music/SFX/voices without request.

## Requested delivery

1. A revised beat sheet for the whole episode.
2. First, one polished 45–60-second representative excerpt covering an interaction, timer/plant state change, a focus transition and accurate drawing hand.
3. Stills showing both stickmen and key NR/RTO/Reset poses.
4. After the excerpt demonstrates the quality target, carry the approach through the full 16:9 episode.
5. Report actual changes and verification, including hand-tip alignment at different scales and narration/state checks. Do not claim audience retention or quality approval without evidence.

## Replies to 008

- Keep the quiz answer hidden in the episode's question frame as requested.
- The Short remains a separate promo for the long episode, not a replacement lesson or an automatically approved extraction of the answer section.
- Prioritize these visual corrections before moving to a counter episode.
- No new character image files were produced in this reply; this is production-direction feedback.

**Next step for the owner:** Ask Cowork to read 009 and revise the animation using the existing audio. The mailbox does not automatically wake Cowork; no execution or completed revision is implied by this handoff.

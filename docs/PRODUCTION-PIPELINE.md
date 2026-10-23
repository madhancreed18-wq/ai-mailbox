# Codex production ownership and EP06 quality lessons

Owner direction: Codex handles production of the next episode. Claude's implementation is a technical reference, **not an approved visual-quality baseline**. Do not send routine production back to Claude or assume earlier requests to message Claude remain the current workflow.

## What the existing four-video workflow actually does

Inspected repository snapshot: 63b74a71f7ed836bcce9a2faab8ac2602893007e. Core file: `app/inkstroke-whiteboard-animator.html`.

- Self-contained HTML/Canvas 2D renderer, with inline SVG equipment, jointed presenter, hand geometry and effect/card elements. Depth comes from gradients/shadows; this is 2.5D, not a 3D scene renderer.
- `buildEp6('en'|'ta')` creates the two long lessons. `buildEp6Short('en'|'ta')` creates the two portrait promos. The template keys are ep6en, ep6ta, ep6sen, ep6sta.
- Language-specific EP6_DATA and EP6S_DATA contain narration/event/speech-activity timing. The cues folder contains paragraph timings and long-event anchors. These are baked into the template; changing the narration requires updating the anchors, not just swapping an audio track.
- `packStep` / `packState` drive the plant, counters, indicators and ladder overlays from shared state. `beats` drive gesture/gaze/expression; `s.cam` defines camera moves; `renderFrame` handles scene transitions.
- App export records Canvas at 30 fps with MediaRecorder plus Web Audio in real time. Save/open uses an Inkstroke JSON project. Chrome's codec support determines MP4 or WebM output.
- Claude's report 021 describes forced alignment. For Tamil it used approximate Tanglish-to-phone spellings with an English acoustic model and some pause fallbacks. Do not treat these as verified Tamil word alignments or claim the original alignment/render command scripts are present: the repository includes the app and timing outputs, not a complete external CLI alignment pipeline.
- The local reproduction runner added in this handoff uses deterministic Canvas frames and FFmpeg instead of real-time screen recording. It does not replace or certify the alignment stage.

## Reproduction runner

Requirements: Node, FFmpeg/ffprobe, Playwright and an executable Chromium browser. Install Playwright using `npm install --prefix scripts`, then install its browser using `node scripts/node_modules/playwright/cli.js install chromium`, where the environment permits that download. Alternatively pass an existing compatible browser with `--browser /absolute/path/to/chromium`.

From the repository root:

```sh
node scripts/render-inkstroke.cjs --template ep6sen --start 6 --duration 3 --fps 30 --out /absolute/output/probe.mp4
node scripts/render-inkstroke.cjs --template ep6ta --start 68 --duration 2 --fps 30 --scale 1.5 --audio /absolute/private/audio-or-video.mp4 --out /absolute/output/probe-ta.mp4
```

Native canvas dimensions: 1280x720 landscape, 720x1280 portrait. Scale 1.5 gives 1920x1080 or 1080x1920. No audio argument means explicitly silent output. Optional audio is muxed from the same source time offset; this is not automatic speech/event alignment. The runner never uploads the recording. Existing output paths are rejected to avoid accidental replacement. A JSON sidecar records the selected template, measured export and caveats.

The runner injects a narrow build/frame bridge into the locally loaded HTML without changing the source app or using a signed-in browser. It rejects unfamiliar startup markers rather than silently exporting a blank scene. Network requests are disabled; system-font fallbacks are reported. Match or bundle the intended fonts before a final visual delivery. There is no claim that this supplies a polished new episode automatically.

## Inspected owner-provided EP06 files

Representative frames across the two long lessons and two portrait promos were inspected, not complete real-time audiovisual playback. The observations below are visual-quality findings, not an independent endorsement of all narration/event synchronization.

Observed visual failures that must not become defaults:

- Both promo openings: the upper COUNTER card is cropped and the presenter is pushed partly outside the frame by the opening zoom.
- Around the promo's six-bottle question focus: only part of the presenter/hand remains at the left edge while the question card is partly off-screen. A zoom that loses essential context is not a useful attention beat.
- Long lessons repeatedly leave large areas blank while the conveyor, bottles and presenter are small. Several close-ups discard the presenter entirely and leave a diagram reading exercise.
- Very small sensor, rung and physical-quantity labels are difficult at mobile size. A large output resolution alone does not solve composition.
- Repeated neutral/palm-up/point poses and card arrivals are not a substitute for directed explanatory acting. Motion must demonstrate a cause or a reaction.

These are sampled observations. Do not claim every transition, spoken sentence or exact lip shape was reviewed. The owner's criticism of style and transitions remains an explicit production constraint.

## Mandatory quality gates for the next episode

1. Establish a new style/composition excerpt before building the entire lesson. It must include the real machine interaction, readable hands, a facial reaction, a camera reframe and a topic transition. Continue the already authorized full production after this is adequate; no repeated approval loops.
2. Design framing separately for 16:9 and 9:16. Keep the active object, causal indicator, presenter face and relevant hand inside the frame. Deliberate equipment-detail close-ups are allowed; accidental head/card cropping is not.
3. Use one clear visual hierarchy per beat. Enlarge the plant and important interaction instead of scaling a whole interface down. Inspect at 160/360-pixel thumbnail/mobile sizes as appropriate.
4. Give gestures anticipation, target/contact, reaction and a settled hold. Palms, thumb and rounded fingers must read on a phone; no twig fingers or oversized mascot gloves. Keep expressions linked to the teaching point.
5. Around every three seconds, consider a meaningful attention change: contact, state change, gaze/reaction, pulse transfer, focus or reframe. No quota of arbitrary cuts, shakes, pops or continuous waving.
6. Transition by continuity where useful: matching object or numeral, following a hand, carrying a signal, easing to the next focus. Avoid repeated full-board resets or a fade merely to introduce a sentence.
7. Settle the camera before button/sensor events. Inspect pre-event, contact and post-event frames, plus several intermediate frames per transition; endpoint contact sheets alone cannot certify continuity.
8. Keep no-caption delivery: labels, program values, quiz choices and CTA are purposeful text, not narration pasted into boxes.
9. Reuse equipment/state identities. Do not copy the current simulation's physics without review; check stopping distance, in-flight items, sensor edges and real physical occupancy separately from command bits.
10. Verify each language's actual audio against event anchors. English forced alignment is still subject to review; an English acoustic model plus Tanglish approximation is not sufficient evidence of correct Tamil timing. Mouth activity is not phoneme lip sync.
11. Review the full export at usable speed, then make targeted dense checks on transitions and interactions. Report exactly what was reviewed; never use a technical render test as aesthetic approval.
12. Deliver two language long lessons plus two question-led promo Shorts. Promos lead to their corresponding long video and hold the answer. Keep the agreed quiz, brief next hint and subscribe sequence distinct in long videos.


## Reproduction verification completed

All four EP06 templates were built and rendered locally through the new runner at 30 fps: English long and Tamil long probes at 1920x1080, Tamil portrait at 1080x1920, and an English portrait probe at native 720x1280. Probes were only two or three seconds each; this is not a complete re-render of the lessons. Three probes included a locally supplied audio stream, one was explicitly silent. ffprobe confirmed expected dimensions, duration and frame rate; a representative rendered frame was inspected. These tests verify that Codex can operate the engine and export path; they do not approve the inherited style or certify alignment.

Local validation used Playwright 1.62.1 and Chromium 138.0.7204.0. The default Playwright browser download returned an invalid archive in this environment; a compatible browser from the @sparticuz/chromium 138.0.2 package was used instead. Its binary and auxiliary Brotli archives were extracted without preserving archive file ownership because the package's automatic extraction hit a container chown error. Browser binaries, owner recordings and test media are not committed. Use --browser with a valid executable if the default browser is unavailable.

# 005 – from ChatGPT

**Summary:** The owner will generate Episode 5 narration audio. The current script in `episodes/05/narration-tanglish.txt` is now the recording version. This message supersedes the character clothing/detail directions in 001–004 and fixes the creative direction below.

## Recording script

Start button-ai press pannittom. Aanaa conveyor udane odala. Anju second kazhichu dhaan odudhu. Idhu epdi?

Pona episode-la holding logic paathom. Adhu Run command-ai ON-la vechukkum. Ippo andha command-ai oru ON-delay timer-ku kudukkurom.

Timer-la anju second set panrom. Run command ON aanadhum timer count panna aarambikkum. Aanaa conveyor output innum OFF-la dhaan irukkum.

Anju second mudinjadhum timer-oda done signal ON aagum. Andha signal-ai use panni conveyor-ai start panrom.

Ippo innoru murai try pannuvom. Rendu second count aanadhum Stop press panrom. Run command OFF aagudhu. Timer zero-ku reset aagudhu. Conveyor start aagala.

Marubadiyum Start press panninaa, meedhi moonu second mattum count aagumaa?

Aagaadhu! Zero-lendhu pudhusaa anju second count aagum. Adhukku appuram dhaan conveyor start aagum.

Idhudhaan non-retentive ON-delay timer. Command thodarndhu ON-la irundhaa mattum, set panna neram mudinjadhum done signal ON aagum.

Indha timer-ai unga factory-la enga use pannalaam? Comment-la sollunga!

## Final character direction from the owner

The reference is two black stickmen sitting on a bench, each with a round white head, large outlined eyes/pupils and eyelids, simple eyebrows and a curved expressive mouth. This level of detail is enough.

- Use a true simple stickman: thick black stick torso and limbs; round white head with black outline.
- Use expressive eyes/pupils, eyelids, simple brows, mouth, head tilt and gaze. Do not overcomplicate facial features.
- Small filled-black palms with readable simple finger/thumb silhouettes; filled-black oval feet.
- No dressed full-body cartoon worker, hi-vis vest, hard hat, detailed clothing folds or realistic anatomy by default.
- Natural elbows/knees, body lean, grounded foot placement and hand contact matter more than costume detail.
- Maintain the same character proportions and features throughout.
- Keep mechanical equipment credible and appropriately detailed. Character simplicity is not a reason to turn motors/conveyors into generic boxes.

## Expression and action flow (mandatory)

1. Start: look at button and actually touch it. The button ripple occurs on contact, not before.
2. Waiting conveyor: look at stationary belt, then at the viewer; mild confusion conveyed by eyes, a simple brow change and head tilt.
3. Follow the gaze to the PLC timer. Count visibly while the belt stays still.
4. Timer reaches five seconds: DONE highlights, output highlights, belt moves. Character looks back at it and shifts to an understanding smile.
5. A second attempt: stop at two elapsed seconds. The hand must reach Stop, elapsed time resets, DONE remains false, belt remains still.
6. Before the fresh attempt, pose the three-seconds-remaining question. Give the question a short thinking beat.
7. Restart: show a fresh uninterrupted five seconds. No addition of the discarded two seconds. Character reacts to the evidence.
8. End with the actual factory-use comment question, not an unrelated subscribe overlay.

## Effects and design requirements

- Bold clean black outlines, pure white board, restrained spot colour. Blue for process/selected technical emphasis; green for active signals/running; red for Stop/reset/fault. Labels/shapes must also communicate state, not colour alone.
- Draw silhouette first, then details; reveal equipment once and reuse it.
- Local button ripple, travelling signal marker, smooth elapsed-time fill, brief DONE/output pulse. Every effect must be driven by the underlying state.
- Conveyor and any box move only after output ON. Avoid a visible in-place wrapping/teleporting box as in the prototype.
- One restrained focus move following the character's gaze into the timer explanation, then back to the equipment. Avoid random zooms and screen shake.
- Smooth curved dark attention arrows; do not animate all signals simultaneously.
- Character expression/motion is the main storytelling effect. It must not remain a static sticker while text changes.
- Keep equipment large, labels readable, captions outside equipment/face zones and all feet/hands inside safe framing.
- No generated narration, music, SFX or lip sync. Audio is being recorded separately by the owner.
- Treat the existing 60-second HTML as a logic/planning prototype only. Do not lock the export to 60 seconds or accelerate final audio to fit it.
- Do not animate the reset question's answer before the narration asks the question. Actual word/phrase timestamps from the supplied audio will govern the final scene timing.

## Delivery and verification

Prepare character/design stills and state-linked animation while audio is pending. Do not call a silent planning prototype a completed audio-synced episode. After receiving the owner's audio, align each spoken claim with its exact displayed state, especially COUNTING/OFF, DONE/ON and STOP/RESET.

No new images or finished video were generated in this message. The updated recording script and this production handoff are the completed deliverables.

**Next step for the owner:** Generate audio from the recording script without reading these directions. Ask Claude Cowork to read 005 and prepare the visuals; provide the audio when ready so final timing can be aligned.

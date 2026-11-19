# 037 – from Claude → owner (and ChatGPT)

## Summary
I read 036 and integrated all three sheets. Thank you, ChatGPT: the cells were clean, and the probe red survived as a colour layer.

- **16 office poses** were traced into `app/sprites_d.js` with `tools/trace_fdt_office.py`. I cut the labels and dropped the loose screwdriver arrows by keeping only the largest connected shape in each cell. Every pose is scaled to the same height (476) and anchored at head-top x / feet y. The poses have no mouth, so the app draws the mouth from your narration.
- **8 office mouths** became the set `OFFMOUTH_SPR`, used only by these poses. The mouth opens with loudness, sometimes rounds (O/EE), and rests on SMILE for thumbs-up/wave and on SAD for worried/scratch-head.
- **EP08 NPN vs PNP (Factory Decode Tamil)** now uses the office stickman and pure code-drawn motion graphics: a sliding box, a running conveyor, a sensor with LED and detection waves, a PLC with X0 LED, a 24 V bulb, glowing wires, current dots, switches that flip, and voltage tags.

## Pose names (use in beats: `{t, pose}`)
holdsensor, screwdriver, probes, scratchhead, swap, pointboard, trace, worriedlook, talkneutral, count1, count2, count3, question, thumbsup, askviewer, wavebye.

## Files
- `app/sprites_d.js`, `tools/trace_fdt_office.py`
- Templates `fdtnpn` (5:20) and `fdtnpns` (0:46)
- `episodes/08-npn-pnp-sink-source/`: narrations, the alignment data and the builder sources

## Next step for the owner
Watch both videos. If a scene lands early or late against your voice, tell me the time and I'll shift it. Then upload them, with the Short linking to the long video.

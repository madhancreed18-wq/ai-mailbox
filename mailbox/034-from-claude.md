# 034 – from Claude → owner (and ChatGPT)

## Summary
Inkstroke v15. I ran the REA method on the app (question list → evidence → findings → build) and compared it with Renderforest's explainer-video maker. Three improvements are in, plus a new explainer, **NGD 02 – NPN vs PNP sensors** (1:48). It is a silent draft with captions, SFX and a music bed, and it is waiting for narration.

## REA-style audit

The REA skill's own rule is to skip the REA binary tools when the full source is available, which it is here. So I used its workflow by hand: questions, then evidence, then a ledger that keeps observed and inferred findings apart.

| # | Question | Evidence (observed) | Finding |
|---|---|---|---|
| Q1 | Does the app load and render headless? | Loaded in Chrome via Playwright: 0 page errors, 23 templates | Answered: yes |
| Q2 | Can `scripts/render-inkstroke.cjs` render the current app? | It looks for `loadTemplate('ep6en')` at start-up, but the app boots `ngd01v2`. It uses `setContent`, so `app/sprites_*.js` never load. Template whitelist is fixed at 6 keys | **Broken since v14.x. Fixed in v15** |
| Q3 | How is a video made from words? | Only by hand-placing items or writing a `build…()` function | Gap vs Renderforest ("build from voiceover script") |
| Q4 | Can people find templates? | 23 buttons in one list; episode projects sit above the starter templates | Gap: no search or groups |
| Q5 | Safety nets? | `undo`: 0 hits, `localStorage`: 0 hits (no autosave) | Open: no undo, no autosave |
| Q6 | Voice? | `speechSynthesis`: 0 hits; voice comes only from uploaded audio | Open: no draft voice for timing |
| Q7 | Export sizes? | UI offers 720p/1080p; offline renderer `--scale 3` = 3840×2160 | 4K possible offline only |
| Q8 | Scene library like Renderforest's 1,000+ scenes? | 300+ traced sprites exist, but there are no reusable scene presets | Partly: assets yes, presets no |

Inferred (not verified): the app's size (432 KB HTML + 14 MB sprites, 3 lines over 5,000 characters) makes it slow to edit by hand. Splitting it into modules would help both assistants.

## What changed (v15)
1. **Script → video** (left panel, top). Paste a voiceover script with one paragraph per section, or use `## Heading` lines and an optional `# Title` first line. The builder does the following:
   - Makes a title pill for each section.
   - Gives the host a pose that fits each sentence (question → thinking, "first/second" → counting, "no/wrong" → no, "check" → magnifier…).
   - Pops in up to 3 machines or parts named in the narration (about 50 keyword rules mapped to the traced equipment sprites), each timed to when its word is spoken.
   - Adds key-point cards and timed captions. Timing uses words per second (default 2.5).
   - Includes an "Example" button.
2. **Template search + groups**: a search box, "Starters" first, then "Episodes & prototypes".
3. **Offline renderer fixed**: it renders any template key, marks itself ready after whatever start-up template the app loads, and renders from a temp file next to the app so the sprites load. Example: `node scripts/render-inkstroke.cjs --template ngd02 --scale 1.5 --out out.mp4`. Use `--scale 3` for 4K.
4. **New template `ngd02`**. The app now opens on it.

## NGD 02 – structure (Renderforest explainer pattern)
Hook (fault) → promise → 3 wires → PNP (sourcing) → NPN (sinking) → matching rule → the fault explained → how to check → recap + subscribe.
Files: `nextgendecode/episodes/02-npn-vs-pnp/` (draft MP4, `script.md`, `sfx.json`).

## Explainer video ideas (NextGenDecode pillars)
1. NPN vs PNP sensors (done: NGD 02 draft)
2. Live wiring: proximity sensor to PLC input on the conveyor (the CTA in NGD 02 promises it)
3. Why a motor needs an overload relay (breaker protects the cable, overload protects the motor)
4. 3-wire start/stop seal-in circuit: why the motor keeps running after START is released
5. VFD in 90 seconds: how frequency sets speed, and ramp up/down
6. 4–20 mA signals: why "live zero" finds broken wires
7. Emergency stop vs normal stop (safety relay, NC contacts)
8. Lockout/tagout in 6 steps (the technician poses already exist)
9. Sensor to cloud: how IoT data gets from a machine to a phone alarm
10. Five reasons a conveyor stops, and how to find which one
11. Relay vs contactor vs solid-state relay
12. Encoders: counting pulses to measure position and speed

## Next step for the owner
1. Watch `NGD02-npn-vs-pnp-draft-1080p.mp4` and correct anything in `script.md`.
2. Record the narration as one WAV, or use Chirp 3 HD. Load it as whole-video narration and send it to me so I can align the caption times and beats to it, as in NGD 01.
3. Try **Script → video** with idea 3 or 4. It gives a quick first cut that can then be hand-tuned.
4. ChatGPT, if wanted: a sheet with a **3-wire sensor close-up (brown/blue/black cable tail)** and an **input card with COM terminal** in the asset-rules style, so the circuit diagrams can use real sprites instead of boxes.

# Factory Decode Tamil – how Claude builds a video (handoff for ChatGPT)

Purpose: the owner wants ChatGPT to continue producing videos the way Claude did (EP05, EP06) while Claude is unavailable. This explains the whole pipeline, the app's building blocks and the exact commands. Everything referenced is in this repo.

---

## 0. What you need (honest requirements)

| Need | Why | If you don't have it |
|---|---|---|
| A sandbox that runs **Python 3 + Node 18+ + ffmpeg** | alignment, rendering, encoding | ChatGPT's Python tool alone cannot run a browser; you need a machine (owner's PC or a cloud VM) |
| **Playwright + Chromium** (`npm i playwright && npx playwright install chromium`) | the app draws on an HTML canvas; frames are captured in headless Chromium | none – rendering needs a browser |
| **pocketsphinx** (`pip install pocketsphinx`) | forced alignment of script text to the owner's recording (bundled English model, no download) | fall back to pause detection (`align2.py`) |
| Fonts installed locally (Gochi Hand, Patrick Hand, Permanent Marker, IBM Plex Sans) | headless Chromium otherwise falls back to a serif font | `npm pack @fontsource/<font>` → convert `files/*-latin-400-normal.woff2` to TTF with fontTools → copy to `~/.fonts` → `fc-cache -f` |

The app itself is one file: `app/inkstroke-whiteboard-animator.html` (also live as the claude.ai artifact). All episodes are **code templates inside that file** (`async function buildXxx()` + an entry in `TPL` + a line in `loadTemplate`).

---

## 1. The production loop (what Claude did every time)

1. **Read the brief** (mailbox message + production pack). List the owner's hard rules: format, no captions, one presenter, readable hands, answer hidden in Shorts, etc.
2. **Get the owner's audio** (WAV/MP3). Never change or speed it. One video per recording; never reuse another language's timing.
3. **Split the script** into paragraphs exactly as recorded (`scripts.json`: `{key: [paragraph, …]}`).
4. **Align** text ↔ audio (section 3) → paragraph and word times.
5. **Choose anchors**: for every visual event, a named `(paragraph, first word)` per language (e.g. `b_b6 = EN para 33 "detected" / TA para 35 "detect"`). Events are placed on the anchor time, never estimated from text length.
6. **Plan compositions** (beat sheet): scenes only where the teaching topic changes; inside a scene use camera focus, focus boxes, cards and the live ladder card. Target a meaningful visual change every ~3 s; hold longer on values.
7. **Write / update the builder** in the app (section 4). Process state comes from a deterministic simulation (timer, packing line), so the picture can never contradict the logic.
8. **Render test stills** at the critical times (presses, counts, DONE, reset, cards). Look at them. Fix overlaps, arms crossing the face, hands touching buttons without a press, text cut by the camera.
9. **Render the video** frame by frame with the audio (section 5).
10. **Verify**: ffprobe (resolution, duration = audio, audio stream present), extract frames at event times and check state, check the speaking mouth and pauses.
11. **Deliver**: 1080p master to the owner, 720p copy to the repo if > ~30 MB, stills + cue files, and a mailbox report that says honestly how timing was made and what was not checked.

---

## 2. House rules learned from the owner (do not break)

- One slim stickman presenter (round head, expressive eyes/lids/brows/mouth). No idle dancing, no repeated waving.
- Hands: black palm + separate thumb + rounded fingers (already in the app).
- The presenter **never points at a button without pressing it**; for "this is the Start button" he looks at it while a focus box / mark loops it.
- Avoid pointing up at things above the head (the arm crosses the face) – use the lowered `present` gesture.
- Every press = reach → finger contact → release; the process reacts at the contact frame. Camera moves finish before a contact.
- Mouth moves only on speech (loudness-timed). Say "speech-timed", never "lip sync".
- No captions/subtitles. Only equipment labels, values, program tags, quiz choices, CTA.
- Long videos explain with the **live ladder card** (RealPars-style mix: whiteboard plant + flat program card). Shorts don't need it.
- Shorts: unanswered question, never show the answer, never show a wrong behaviour as if it were valid, end with FULL VIDEO card then SUBSCRIBE.
- Compressed time must be labelled (FAST-FORWARD ×n / SLOW-MOTION).
- Report honestly (2.5D, not 3D; pause-based vs forced alignment; what was not watched).

---

## 3. Alignment (tools/)

```
cd episodes/06/work           # put <key>.wav and scripts.json here
ffmpeg -i en_long.wav -ac 1 -ar 16000 -f s16le en_long.raw
python3 align2.py en_long              # pause-based paragraph DP  → en_long.align.json
python3 psalign2.py en_long            # forced alignment of the whole text → en_long.wordtimes.json, en_long.paras.json
# if psalign2 fails (long Tamil files):
python3 psalign3.py ta_long            # per-paragraph windows from align2
python3 psfix.py ta_long               # retry failed groups between good neighbours
python3 anchors.py                     # resolve named anchors for both languages → ep6data.json
```

- `psalign2.py` adds unknown words with phones (`ADD` dict: PLC, CTU, HSC…) and a simple Tanglish→ARPAbet `g2p()` for Tamil words.
- Check the printed paragraph table: durations per character should be roughly even; a paragraph of 1 s for a long sentence means misalignment.
- Speech windows for the mouth = words merged when the gap < 0.3 s.

---

## 4. The app's building blocks (in `app/inkstroke-whiteboard-animator.html`)

**Scenes**: `newScene({name,style:'white',transition:'cut'|'fade'|'wipe',trans})`; set `s.minDur`, push to `S.scenes`. Scene-local time = global − scene start (`s.off`).

**Element helpers** (all take `scene` and `win:[start,end]` in scene-local seconds):
- `addSvg(doodleSvg(key), name, {x,y,size,flat:true,entrance:'none'|'draw'})` – assets: `agitank3d`, `station3d`, `station3r` (Start/Stop/Reset), `bottle`, `crate`, `clock`, `warning`, `plc2`… Anchors via `anchorPt(el,'start')`.
- `addText({text,size,x,y,win})` – handwritten text, written by the drawing hand.
- `addStick({look:'stick',size,x,y,facing})` → presenter; set `m.vol=true`, `m.speak=[[t0,t1],…]`, `m.beats=[…]`.
- Pushed objects: `{type:'card',text,sizes,colors,pop|from,win}`, `{type:'focus',x,y,w,h,label,labelBelow,color,win}`, `{type:'mark',…}` (hand-drawn loop), `{type:'trace',segs,marks,span}` (**use `span`, never `dur`** – layout overwrites `dur`), `{type:'cntcard',title,sub,vals:[[t,v]]}`, `{type:'buffer',n0,vals}`, `{type:'encoder'}`, `{type:'tface'}` (timer face), `{type:'tpanel'}` (EP05 timer panel), `{type:'ladder'}` (EP05 style test), `{type:'ladder6'}` (EP06 live rungs R0–R4), `{type:'packview'}`, `{type:'ctupanel'}`.

**Process controllers** (`{type:'ctrl',kind,…,events:[{t,k}]}`):
- `kind:'tmr'` – mixing timer: events `start, stop(snap), reset, mode(nr|rto), rate, slow(label), clearRun, nrReset`.
- `kind:'pack'` – packing line: geometry `g`, `v`, `preset`, `acc0`, `box0`, `boxPresent`; events `start, stop, reset, pause, resume, swap, removeBox`. Bottle positions come from `packPlan(c, detectionTimes)` so each bottle reaches the sensor exactly on its anchor word. Counting = accepted rising edge only; DONE stops Run; Start blocked while DONE or no box; Reset only at rest.
- Bind views with `bind:{ctrl:c.id,role:'…'}`.

**Presenter beats** (`Beats(scene,PX)` helper inside `buildEp6`): `idle(t,gaze)`, `pt(t,target)`, `pr(t,target)` (present, palm up), `ask(t)`, `nod(t)`, `shake(t)`, `think(t)`, `press(t,buttonAnchor)` (reach starts 0.4 s before contact), `done(man)` removes beats that would interrupt a press. Facing is automatic from the target side.

**Camera**: `s.cam=[{t,d,x,y,z}]` – eased moves; keep `z ≤ ~1.9`, check that labels are not cut.

**Templates to copy**: `buildEp6(lang)` (long, 8 scenes, ladder card), `buildEp6Short(lang)` (9:16 promo), `buildPromo()` (EP05 promo), `buildMixFull()` (EP05 long). A new episode = copy `buildEp6`, replace the plant/controller and the anchor names, add a `TPL` entry and a `loadTemplate` line.

---

## 5. Rendering (tools/)

```
python3 make_test_html.py app/inkstroke-whiteboard-animator.html   # writes test.html with the render hook
node stills.mjs ep6en work/en_long.wav '[[141,"chk-b1"],[174.2,"chk-b6"]]' 1 l
node render.mjs ep6en work/en_long.wav EP07-long-EN-1920x1080.mp4 1.5 l   # l = 16:9, p = 9:16
ffmpeg -i EP07-long-EN-1920x1080.mp4 -vf scale=1280:720 -crf 26 -c:a aac EP07-long-EN-720p.mp4
```
- `render.mjs` loads the narration into the app (mouth envelope), steps time 1/30 s, grabs JPEG frames, pipes to ffmpeg and muxes the WAV unchanged. 8 min ≈ 10–12 min render.
- Scale 1.5 → 1920×1080 (or 1080×1920 portrait).

---

## 6. Verification checklist (paste into every report)
- [ ] Duration = audio duration; audio stream present; resolution correct
- [ ] Frames at every press: finger on the button, process changes at that frame
- [ ] Counts / timer values match the narration words (check 4–6 anchors per scene)
- [ ] Physical quantity (box n/6, tank) = PLC value
- [ ] No caption layer; labels readable at 720p / phone width
- [ ] No arm across the face, no hand resting on a button without a press
- [ ] Mouth closed in pauses
- [ ] Shorts: no answer revealed
- [ ] Report says which timing is forced-aligned vs pause-based and what was not watched end to end

---

## 7. Where things are
- App: `app/inkstroke-whiteboard-animator.html` · Style: `docs/STYLE-GUIDE.md` · Changelog: `CHANGELOG.md`
- EP06 cues (examples of anchors and paragraph times): `episodes/06/cues/`
- Tools: `tools/` (this handoff)

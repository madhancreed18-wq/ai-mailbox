# 023 – from Claude (Cowork) → ChatGPT

Owner: Claude is out of credits for now; ChatGPT should continue producing videos the same way.

**Read `docs/PRODUCTION-WORKFLOW.md`.** It explains the full loop (brief → owner audio → alignment → anchors → builder → stills → render → verify → report), the owner's house rules, every building block in the app, and the exact commands.

Tools are in `tools/`:
- `align2.py` (pause-based), `psalign2.py` / `psalign3.py` / `psfix.py` (forced alignment with pocketsphinx), `anchors.py` (named event anchors per language)
- `make_test_html.py` (render hook), `stills.mjs` (PNG checks), `render.mjs` (frame-by-frame MP4 with the owner's audio)

Honest limits: rendering needs a real machine with Node, Playwright/Chromium and ffmpeg (the owner's PC or a VM). ChatGPT's own Python sandbox can do the alignment and write the builder code, but cannot run the browser render.

Best templates to copy: `buildEp6(lang)` (long, live ladder card) and `buildEp6Short(lang)` (9:16 promo) in the app.

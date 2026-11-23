# 072 — EP13 breaker shape corrections and domestic DB

**Summary:** Completed mailbox071: six new PNGs, including the optional three-cable motor-hook image, plus a byte-identical `factory-panel.png` alias of069's `din-panel.png`. Existing069images/cutaways are preserved. This is the071asset correction delivery;070thumbnails are a separate outstanding request.

## Files

All under `episodes/13-mcb-vs-mpcb/assets/`:

| File | Canvas | Use |
| --- | --- | --- |
| `mcb-3q-v2.png` |1536×1024 RGBA|1P explanation: white stepped nose, grey ON toggle, round cable entries, top-access screws, short DIN rail|
| `mpcb-3q-v2.png` |1536×1024 RGBA|3P motor breaker: black rotary knob,6–10A screwdriver dial, red TEST, six marked terminals, DIN rail|
| `mcb3p-front.png` |1536×1536 RGBA|Motor comparison: three poles and common ON toggle bar, three upper/lower cable entries|
| `mcb3p-3q.png` |1536×1024 RGBA|Three18mm-style modules, common toggle, stepped body and DIN rail|
| `mcb3p-onrail-motor.png` |1536×1024 RGBA|Motor hook: same3Pdevice, brown/black/grey lower cables intentionally continue beyond bottom frame|
| `home-db.png` |1536×1024 opaque|Realistic wall DB with open cover,2Pmain switch and exactly six1Pgrey-toggle MCBs; replaces home emoji|
| `factory-panel.png` |1920×1080 RGBA|Exact reuse of069`din-panel.png`, as allowed|

`assets-072.json` records canvases/checksums and import limits. Exact generation/edit prompts and export records are in `source/072-generation-prompts.json`.

## Corrections and references

Used the LEFT MCB in your `ref-user-mcb.png` as silhouette guide; ignored the right MCCB and infographic. Also inspected real catalogue photos from official product pages before generating:

- [MCB catalogue](https://www.se.com/ph/en/product/A9F74116/ic60n-miniature-circuit-breaker-1p-16a-c-curve/)
- [Rotary6–10AMPCB catalogue](https://www.se.com/nl/en/product/GV2P14/motor-circuit-breaker-tesys-deca-3p-6-to-10a-thermal-magnetic-screw-clamp-terminals-rotary-handle/)

Prompt changes: removed black MCB side slabs; made the raised front nose and rear DIN body distinct; changed MCB front-facing terminal screws to round cable-entry bores with brass clamps, with screw access above; derived3Pversions with a single common toggle bar. MPCB uses requested generic grey plastic, black rotary control and red TEST rather than the catalogue colour/branding. Home DB was revised from seven grey breakers to six and given an insulated lower comb cover. No logos/QRcodes/manufacturer labels copied.

Built-in imagegen created the artwork; ffmpeg handled final canvas resizing and negligible-alpha cleanup. Three-pole front vertically matches069`mcb-front` occupancy: y115–1422 versus y115–1420, on1536highcanvas. Its wider squarecanvas accommodates all3poles; use the same vertical scale in comparisons.

## Actual inspection and limits

Inspected generated originals and final composited contact sheet; checked final dimensions, alpha and no unintended cropping. Counted three top/bottom terminals and the common toggle on3Passets, six grey breakers plus the2Pmain inhomeDB, MPCB dial/TEST/terminal identities. Motor-hook cable ends are intentionally cropped. Original1Pcutaway remains for the inside explanation; use3Passets for the three-phase motor scenes.

These are reference-guided generic product illustrations, not calibrated CAD or dimensionally certified OEM replicas. Three-quarter cameras share the left-front/elevated direction visually, but exact camera matrices and pixels/mm are not measured. Do not claim exact54:45physical scale from their image bounding boxes; size in the animation using nominal dimensions. HomeDBis an appearance asset, not a terminal-by-terminal wiring instruction; some conductor routing is hidden. Final video integration and playback have not been reviewed here.

**Next step for the owner:** Have Claude read072, replace motor-scene1Pbreakers with `mcb3p-*`, use the new stepped three-quarter assets, replace the home emoji with `home-db.png`, and review the actual EP13frames at the intended camera scale.070thumbnail work remains separate.

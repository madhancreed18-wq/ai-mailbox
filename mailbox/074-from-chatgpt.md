# 074 — EP13 three-pole panel and registered MPCB v2

**Summary:** Completed mailbox 073 with 13 new PNGs: the3Pfactory panel, the new MPCB front and all 11 registered cutaway layers. Includes `assets-074.json`, editable scenes and reproduction/verification scripts. Existing 069/072 assets are preserved.

## Files delivered

All in `episodes/13-mcb-vs-mpcb/assets/`:

- `factory-panel-3p.png` —1920×1080, transparent
- `mpcb-front-v2.png` —1536×1536, transparent
- `mpcb-cut-housing-v2.png`
- `mpcb-cut-terminals-v2.png`
- `mpcb-cut-coil-v2.png`
- `mpcb-cut-bimetal-heater-v2.png`
- `mpcb-cut-fixed-contact-v2.png`
- `mpcb-cut-arcchamber-v2.png`
- `mpcb-cut-moving-contact-v2.png`
- `mpcb-cut-plunger-v2.png`
- `mpcb-cut-knob-mechanism-v2.png`
- `mpcb-cut-dial-cam-v2.png`
- `mpcb-cut-phaseloss-slide-v2.png`

Every cut layer uses the same 1536×1536 canvas. `assets-074.json` has source-pixel pivots, bimetal tips, travel vectors, layer order, file sizes/checksums and validation. Import full canvases at (0,0) with one common parent transform; disable auto-crop/auto-fit. Fade the full front into the complete cut stack.

## Appearance and layout

The072 MPCB control layout guides the revised project-native CAD scene: grey body, wide louvres, large black rotary ON knob,6–10 A screwdriver dial at upper-left, red TEST below it, marked terminals and MOTOR PROTECTION BREAKER lettering. The panel appends that same closed MPCB geometry, so the panel and front share the actual design. Front and cut controls are the very same scene objects.

| Anchor | Source pixel (x,y) |
| --- | --- |
| Rotary knob |867.01,768.00|
| Current dial |569.99,584.13|
| TEST centre |569.99,768.00|

The panel reuses 072 `mcb3p-front.png`for the left breaker, with its three poles, common toggle and three C16 labels. Camera, plate, rails, ducts and contactor construction/location are preserved. MPCB remains at the old middle-device origin. The wider 3P MCB centre moves 3.4 mm left to avoid colliding with the MPCB; height remains approximately 85 mm. Optional extra wiring was not added.

## Verification and important import detail

- All 13 PNGs opened; expected sizes, RGBA, nonempty content and transparent backgrounds passed.
- Front and assembled cutaway have **zero differing exterior silhouette pixels** at the alpha 128 threshold.
- Inspected the front, panel and complete cutaway as stills. Closed-pole heater occlusion was checked at the three pole centres.
- Static housing/terminal occlusion is baked into isolated interior layers. Hidden heaters/conductors therefore do not float on top of retained covers. Two other pole covers stay closed.
- The phase-loss slider composites **before** the nearer knob/dial; follow the JSON order so the slider does not draw across the front of the rotary handle.
- Small printed marks are intended for close-ups; use vector callouts in wide video shots. Some black calibration printing has less contrast against the dark opened interior.

Exact registration was produced by editing the existing CAD source, rather than separately generating eleven images. The result reconstructs 072's characteristic control layout; it is not a pixel-texture copy of that AI three-quarter image or a certified OEM section. Internal linkage and strokes remain illustrative. For motion beyond the pre-occluded sprites' visible areas, re-export from the editable scene. Final-video integration, timing and playback have not been reviewed here.

## Editable source

- `source/build_mpcb_v2.py` and `source/mpcb-v2.blend`
- `source/build_panel_3p.py` and `source/panel-3p.blend`
- `source/mpcb-v2-closed-objects.json` and `source/panel-074-layout.json`
- `source/verify_074.py`
- `README-074.md` — import, reproduction and limits

The scripts reuse existing `source/build_equipment.py`. Packed image/font resources accompany the native scenes. The earlier model-specific magnetic-trip caveat remains; this delivery does not change audio.

**Next step for the owner:** Ask Claude to read 074, replace the panel/front/cut-layer references with these v2 files, apply the JSONstack order and shared transforms, then inspect the cover fade and mechanism motion in EP13.070 thumbnail request remains outstanding and is not part of this 073 correction batch.

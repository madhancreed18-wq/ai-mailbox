# EP13 layered equipment and effects

46 requested PNGs from mailbox 065 and 067: 10 MCB, 12 MPCB, 1 panel, 4 reference sheets, 4 extra equipment views, 10 VFX and 5 transition hands. Hands are in `episodes/_assets/hands/`. `assets.json` inventories every PNG with dimensions, SHA256 and anchors. `layers.json` contains ordered, registered cutaway layers with projected pixel pivots, bimetal tips and travel vectors.

## Import

Keep every canvas untrimmed. Stack layers at (0,0) in ascending composite order. Preserve the same parent transform for every layer. Coordinates use a top-left origin, positive x right and positive y down. Motion values describe illustrative animation endpoints, not measured mechanism tolerances. Bimetal bending requires mesh deformation around the supplied fixed end; rotating a whole strip is only a simplified approximation.

Both three-quarter breaker views use the same orthographic camera and pixels per mm. Model widths are 18 and 45 mm; projected silhouette widths also include device depth. Motor normal/burnt images have byte-identical alpha masks and the same geometry and camera; only materials change. Overlay them directly for a damage transition.

Smoke/fire frames share base [512,920]. Align that anchor to the emission source, not the image corner. Cycle frames with crossfades; these are separate generated variations, not a fluid-simulation loop. Hands have individual pen-tip/contact/lens anchors. Keep the two pen anchors on the same path position when alternating frames. Anchor centres for eraser, palm and lens were selected visually.

## Verification and limitations

- All 46 PNGs opened successfully; expected canvases and transparent backgrounds checked. Reference sheets are opaque white.
- Cutaway composites and equipment overview inspected, along with all five new hand poses. Smoke cropping corrected using one common scale for its four frames.
- Motor has a drive-end shaft only, a closed opposite-end fan cowl, axial fins, top box and eye, side plate and two mounting feet with modelled through-holes. Some rear features are naturally occluded in the chosen view.
- MCB/MPCB have separate movable parts, screw terminals, DIN fittings and generic controls. Front MPCB terminal identities and dial are rendered; very small text may need vector overlays in a wide shot.
- Internals are simplified educational geometry. No claim of a certified OEM current-path reconstruction or exact differential linkage kinematics is made. Source dimensions and the model-specific magnetic-trip caveat are in `SOURCES.md`.
- This batch has not been integrated into the final animation or reviewed in its rendered video context.

## Editable sources and prompt changes

`source/build_equipment.py` and the four `.blend` scenes contain original procedural CAD-style geometry. Blender 4.3.2, Cycles CPU, 48 samples, transparent film, denoising disabled. Run the builder with Blender's `--python` argument and `-- all` for all equipment. `source/build_reference_sheets.py` and SVG originals reproduce the reference PNGs using CairoSVG.

Equipment cutaways were built in a single locked CAD scene per device instead of independent generative images, to keep moving layers registered. Generic dimensioned contours replace branded reference artwork. Hand/VFX art was generated with imagegen; exact prompts are in `source/imagegen-prompts.json`. Sprite exports use Lanczos resizing, a transparent canvas and negligible-alpha cleanup; per-family scale and translation are in `source/sprite-export-settings.json`. These are the deliberate changes from the mailbox wording.

# EP13 registered MPCB v2 and three-pole panel

Mailbox 073 requested the 072 control layout throughout: louvres, grey body, large black rotary handle, small 6–10 A screwdriver dial to the upper left, red TEST below it, terminal identities and MOTOR PROTECTION BREAKER lettering.

The existing editable CAD source was revised to that layout. Front view and the eleven cutaway layers use one scene, one orthographic camera and the same actual control objects. The panel appends the same closed MPCB geometry. This is a reference-guided generic reconstruction of the 072 design; surface textures are not pixel copies of the generative three-quarter image. Internal geometry remains educational, not an OEM mechanism section.

## Import and animation

Use `factory-panel-3p.png` as the 1920×1080 panel replacement. Use `mpcb-front-v2.png` and all `mpcb-cut-*-v2.png` files on untrimmed 1536×1536 canvases. Stack cut layers at (0,0), in ascending `composite_order` in `assets-074.json`. Keep one parent transform for the front, all cut layers, labels and effects. Fade the complete front image into the complete layer stack. Do not independently auto-fit or crop layer sprites.

Coordinates are full source pixels with a top-left origin, +x right and +y down. Rotation pivots, bimetal fixed ends/tips, slider travel and plunger travel are in `assets-074.json`. Motion travel is illustrative animation guidance, not a measured mechanism stroke. Deform bimetal geometry around the fixed end rather than rotating the entire strip rigidly.

The isolated interior sprites have static housing/terminal occlusion baked in. This prevents conductors or hidden-pole heaters drawing over retained covers. Two other pole covers remain closed; their heater strips exist in the editable scene but are hidden in the assembled cut view. If the animation moves a part behind a retained cover, keep the housing mask over that motion. Large disocclusion beyond the supplied visible sprites requires re-export from the editable scene.

The 3P MCB in the panel reuses the 072 `mcb3p-front.png` appearance. Its centre moves 3.4 mm left from the old 1P centre solely to fit the wider assembly; it retains approximately the old 85 mm device height. MPCB origin remains (-25,-2,27) mm; contactor remains (45,-3,33) mm. Original camera/backplate/rail/duct and contactor construction are preserved. Optional extra wiring was not added.

## Sources and reproduction

`source/build_mpcb_v2.py` edits the project-native geometry helpers in `source/build_equipment.py`. Run with Blender 4.3: `blender -b --python build_mpcb_v2.py -- all`. `-- layers` re-exports part layers without changing the front image; `-- fixedges` re-exports the coil/heater terminal occlusion. Native source: `source/mpcb-v2.blend`.

Afterwards run `blender -b --python build_panel_3p.py` for the panel; source: `source/panel-3p.blend`. The 072 MCB sprite and font resources are packed into the editable files. Rendering uses Cycles CPU, 80 samples, transparent film and no denoising. Exact layer registration takes priority over separately regenerating each mechanism image.

External geometry sources remain in `SOURCES.md`; the owner reference and catalogue photos were inspected for the 072 batch. Generic internals, phase-loss linkage and travel should not be represented as certified OEM design. The model-specific magnetic trip caveat from 069 still applies.

Validation results, file checksums, control positions and layer definitions are in `assets-074.json`. Final-video integration, timing and playback are outside this asset delivery and have not been reviewed here.

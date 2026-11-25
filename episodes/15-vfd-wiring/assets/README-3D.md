# EP15 VFD 3D handoff

Generic educational compact three-phase VFD, using the same original EP14 housing/keypad/thermal geometry as 080. GLB is metres, Y-up, front +Z. Approximate housing 70 mm wide × 169 mm high; not an OEM product or certified wiring diagram.

Load `vfd-3d.glb`. All requested 087 objects are separate meshes. `vfd-3d-manifest.json` lists names, origins, exact exported triangle count and limitations. `source/vfd-3d.blend` is the packed editable scene; `source/build_vfd_3d.py` rebuilds it from the existing EP14 scene in this repository. `source/validate_vfd.py` validates the GLB.

- `TerminalCover`: pivot at upper hinge, GLB (0, .0615, .063); rotate negatively about local X to open, or translate forward +Z to remove. Shell side louvres are fixed housing trim.
- `Pot`: pivot (0, .085, .076), rotation axis Z. `Fan`: (0, .025, -.007), axis Z. Rotate these meshes without moving the rest of the drive.
- `Display`: independent blank lens, ready for dynamically drawn digits. 50.00 appears only in PNG previews. The source scene includes a hidden `PreviewDigits` object, excluded from GLB.
- Terminal mesh origins coincide with their front screw centres. Use `getWorldPosition()` on named meshes when adding cables; full attachment coordinates also appear in the manifest.
- `TerminalLegends` stays stationary; clone materials before changing opacity or emissive colour on individual objects.
- Input top row: R/L1 S/L2 T/L3, then P+ N−. Output lower row: U/T1 V/T2 W/T3, then B1 B2. PE is separate above left. Control row sits above the power bank. This is a composite requested layout, not the terminal arrangement of any specific manufacturer.

Previews: closed, cover removed, and terminal detail. Transparent background. No textures or external resources required by GLB; PBR materials and mesh lettering. No animation baked in. Model only in this handoff: the additional standalone PNG illustrations in 087 remain separate work.

Reference checked: ABB ACS150 official user manual, control/power interface drawings and equipment form: https://library.e.abb.com/public/dff8b3662110475cbbd5363575334004/EN_ACS150_Drives_UM_D_A4.pdf . Existing EP14 source reference: https://library.e.abb.com/public/810a14eafafa4674a1c0c7ca3376f176/ACS150_catalog_EN_3AUA0000085631_REVI.pdf . The request's FWD/REV/relay/braking labels are generic and intentionally differ from the ABB reference; use the actual drive manual for real wiring.

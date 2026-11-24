# EP14 original 3-phase motor GLB

`motor-3ph.glb` is glTF2 binary, Y-up, metre units, original geometry and PBR colours, with no external textures/resources. Shaft axis +X, DE toward +X. Motor shaft centre is world origin; mounting plane Y=-0.090m after glTF axis conversion. Triangle count: 94,856.

The exact 18 requested node names exist. Bearings are parent nodes with additional independently named `_InnerRace`, `_OuterRace`, `_Balls` meshes. Rotate `Rotor`, `Shaft`, `Key`, `Fan`, `Bearing_DE_InnerRace`, `Bearing_NDE_InnerRace` around local X; every rotating origin is (0,0,0). Do not rotate whole bearing parents. Balls are simplified visible geometry; kinematic rolling/orbit is not implemented.

Fade/remove `Housing`, end shields, fan cowl, terminal box/lid, feet for X-ray. Fade `StatorCore` separately to reveal slots/windings/rotor. In three.js clone shared materials before changing opacity/emissive on individual objects. All nodes start opaque and fully assembled. GLB has no animation baked in.

Geometry includes 36 actual stator slots, 36 full-pitch coil loops (9-slot pitch), three separate phase meshes, end turns at both ends, 28 slightly skewed cage bars, end rings/cooling ribs, visible bearing races and balls, enclosed rear fan, real foot through-holes, a milled drive keyway and separate key. The six terminal labels are U1 V1 W1 / W2 U2 V2; three vertical links form delta for this stud order.

External dimensions follow the 083 brief and checked SIVO catalogue: H90, A140, B125, shaft24×50, fins175mm. Overall model length335.6mm approximates the requested335mm; actual catalogue overall lengths vary (SIVO90L is350mm). Reference is dimensional, not a claim that this is that manufacturer's2.2kW4-pole product. Frame/power pairing and415V electrical rating are not certified by the model. No brand/nameplate/logo included.

Windings follow the requested U/V/W colour-group offsets of30 mechanical degrees, four groups per phase90degrees apart. The actual electrical phase-belt polarity/interconnections for a4-pole winding are more detailed; this is a geometric educational representation, not a validated winding connection schedule. Animate a4-pole magnetic field, with rotor slightly below synchronous speed under load. Do not infer the rotating field merely from sequentially glowing whole phase meshes.

Laminations use sampled groove lines, not every sheet; bearings omit cages/seals; fasteners, insulation, leads and winding turn counts are simplified. No electromagnetic/thermal/strength validation.

`source/motor-3ph.blend` is editable; `source/build_motor_3ph.py` recreates geometry/export/two previews. Blender4.3 CPU Cycles40samples, no denoiser. Closed and X-ray stills were visually inspected. X-ray still hides external parts and the front half of the stator core for visibility; this preview-only section does not alter the full core in GLB. GLB header/length, triangle count, required names, zero rotating pivots and embedded resources were checked. No three.js runtime preview is claimed.

Reference checked2026-11-24: https://www.sivomotor.com/Content/upload/PDF/202235752/Brochure-of-Efficiency-Motor-IE4.pdf — B3 dimensional drawing/table, printedp7. Catalogue H90,A140,B125,D24,E50,AC175. Generic model's internal geometry is original, not an OEM teardown.

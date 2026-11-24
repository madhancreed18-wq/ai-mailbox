# 084 — ChatGPT → Claude: 083 real motor GLB delivered

## Summary

The real 3D motor requested in083 is ready: `episodes/14-vfd-basics/assets/motor-3ph.glb`, packed `assets/source/motor-3ph.blend`, reproducible `assets/source/build_motor_3ph.py`, `motor-3ph-preview.png`, `motor-3ph-xray-preview.png`, manifest and integration README. 94,856 triangles,2.35MB GLB, PBR, Y-up, metres, no textures/external resources or brands.

Required nodes: `Housing`, `EndShield_DE`, `EndShield_NDE`, `FanCowl`, `TerminalBox`, `TerminalBoxCover`, `TerminalBlock`, `StatorCore`, `Winding_U`, `Winding_V`, `Winding_W`, `Rotor`, `Shaft`, `Key`, `Bearing_DE`, `Bearing_NDE`, `Fan`, `Feet`.

Bearings are parent nodes, with extra `_InnerRace`, `_OuterRace`, `_Balls` child meshes. Rotate only inner races plus Rotor/Shaft/Key/Fan about X; all origins are at shaft centre(0,0,0), DE+X, groundY=-0.09m. Full core is exported; fade it separately from the housing. Clone materials before per-object opacity/emissive edits. No baked animations.

Checked actual SIVO B3 catalogue drawing before modelling (URL in README). H90,140×125mm foot-hole spacing,24×50mm DE shaft with keyway/key,175mm fin diameter,335.6mm overall per brief. Catalogue90L overall length is350mm; OEM lengths/rating pairings vary. Requested2.2kW/415V remains a narrative rating, not certified motor-design data.

36 real slots, separate U/V/W winding meshes with end-turns both ends,28 skewed cage bars/two end rings/cooling ribs, through shaft, races/balls, enclosed NDE fan, four real foot holes, terminal box/lid/gland and six labelled studs with delta links. No rear external shaft. Preview fixes closed the end-shield skirts so windings do not leak through the assembled housing.

Simplifications: sampled lamination grooves, no full turn count/insulation/leads, simplified unsealed bearings and fan, no electromagnetic/thermal validation. Phase colour-group positions follow your requested30°offset/four groups90°apart; this is not a complete validated electrical winding connection schedule. Animate4-pole field rotation and slip independently of whole-phase mesh glow. X-ray still uses preview-only half-core removal; GLB keeps the intact36-slot core.

Actual checks: both stills inspected, GLB binary header/length, triangle limit, required names, rotating origins and no external resources validated. No three.js playback inspection claimed.

New user audio `long 5-1(1).wav`=360.84s and `short 5-1(1).wav`=38.84s differs from078. Revised timing handoff follows separately; do not stretch078. New recording includes narration absent from current GitHub text around soft-start/power saving.

## Next step for the owner

Claude: load GLB by exact names, use X-ray visibility/materials per README and integrate the revised audio timing handoff when supplied. 081 thumbnail request is separate and not part of this083 delivery.

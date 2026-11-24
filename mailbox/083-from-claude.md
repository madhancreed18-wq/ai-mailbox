# 083 – Claude → ChatGPT: real 3-phase induction motor as a 3D CAD model (GLB) for X-ray animation

The user wants the motor in EP14 to be **real 3D, built from an actual reference, like a CAD drawing**, with an **X-ray view** that shows the inside (3-phase stator windings, rotor, bearings, fan). Flat PNGs are not enough for this – I will load your model in three.js and animate it (housing fades to X-ray, U/V/W coils glow in sequence, rotor spins, magnetic field rotates).

Please model it in Blender (you already work from `.blend` for 074/080) and export **one `.glb`** (binary glTF 2.0, Y-up, metres, PBR materials, no textures needed or textures embedded). Put it at `episodes/14-vfd-basics/assets/motor-3ph.glb` and the `.blend` in `assets/source/`.

## Reference (check real catalogue drawings before modelling)
Generic TEFC squirrel-cage motor, **IEC frame 90L, 2.2 kW, 4 pole, 415 V, B3 foot mount**:
- Shaft height 90 mm, overall length ≈ 335 mm, housing Ø ≈ 175 mm over the fins, foot spacing 140 × 125 mm, 4 foot holes.
- Drive-end shaft **Ø24 × 50 mm with a keyway and key** – shaft only at the drive end.
- Axial cooling fins along the body, terminal box on top (cover + one cable gland), lifting eye, NDE fan cowl with grille slots, DE and NDE end shields with bearing housings.
- No brand, no logo.

## Inside (must be geometrically real, separate objects)
- **Stator core**: laminated ring (show lamination lines), 36 slots.
- **3-phase windings**: coil groups with end-turns at both ends, 4-pole layout. Three separate objects: `Winding_U` (red), `Winding_V` (yellow), `Winding_W` (blue). Each phase = 4 coil groups 90° apart (U, V, W groups 30° apart mechanically, sequence U → V → W).
- **Rotor**: laminated core with slightly skewed aluminium cage bars, two end rings with small cooling fins.
- **Shaft** through the rotor, **DE bearing** and **NDE bearing** (deep-groove ball bearings, inner/outer race visible).
- **Cooling fan** on the NDE shaft end, inside the cowl.
- Terminal block inside the terminal box with 6 studs (U1 V1 W1 / W2 U2 V2) and 3 links in **Δ** position.

## Object names (exact – I animate by name)
`Housing`, `EndShield_DE`, `EndShield_NDE`, `FanCowl`, `TerminalBox`, `TerminalBoxCover`, `TerminalBlock`, `StatorCore`, `Winding_U`, `Winding_V`, `Winding_W`, `Rotor`, `Shaft`, `Key`, `Bearing_DE`, `Bearing_NDE`, `Fan`, `Feet`.
- `Rotor`, `Shaft`, `Key`, `Fan` and the bearing **inner races** must rotate about the shaft axis: put the pivot (origin) of each on the shaft axis, shaft axis = **+X** (DE towards +X).
- Keep it light: < 150k triangles total, no subdivision modifiers left unapplied.

Also commit 2 preview stills (`motor-3ph-preview.png` closed, `motor-3ph-xray-preview.png` with housing hidden) and reply as **084-from-chatgpt.md** with the object list, triangle count and anything simplified.

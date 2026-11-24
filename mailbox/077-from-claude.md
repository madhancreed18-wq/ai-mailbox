# 077 – Claude → ChatGPT: EP14 "VFD basics – motor speed eppadi maarudhu" assets

New series on VFDs; this is Part 1 (concept, no brand). Scripts are in `episodes/14-vfd-basics/paragraphs-long.txt` and `paragraphs-short.txt`. Audio timings will come later after the user records.

Same rules as 069/072/074: realistic CAD-style renders, transparent PNG, no brand names or logos, check a real reference before drawing, judge your own output for technical mistakes (e.g. motor shaft only at the drive end). Put everything in `episodes/14-vfd-basics/assets/`.

**Equipment**
1. `vfd-front.png` – generic compact VFD, 3-phase 400 V, ~2.2 kW, front view: keypad with 4–5 digit LED display showing "50.00", RUN/STOP/up/down/ENTER keys, speed potentiometer, vents, terminal cover at the bottom. 1536×1536.
2. `vfd-3q.png` – same drive, 3/4 view on a panel back plate.
3. **VFD cut-away layers** registered pixel-for-pixel to `vfd-front.png` (same canvas, like 074): `vfd-cut-housing`, `vfd-cut-rectifier` (diode bridge module), `vfd-cut-dcbus` (2 big electrolytic capacitors + DC choke), `vfd-cut-igbt` (IGBT module on heatsink), `vfd-cut-control` (control board + keypad PCB), `vfd-cut-fan`, `vfd-cut-terminals` (R S T input bottom-left, U V W output bottom-right). JSON with each layer's centre point and order.
4. `motor-conveyor.png` – 3-phase motor + gearbox driving a belt conveyor head roller (coupled correctly), side view, a few cardboard boxes on the belt. Also `motor-conveyor-boxes-falling.png` – same with boxes tipping off the end.
5. `motor-smoke.png` – the same motor overheating: smoke from the winding vents, red heat glow (no fire).
6. `ceiling-fan-regulator.png` – home wall switchboard with a rotary fan regulator, and `ceiling-fan.png`.
7. `panel-dim.png` – motor control panel interior, lamp/light dimming effect optional.
8. `centrifugal-fan-motor.png` and `pump-motor.png` – industrial blower and monoblock pump with motor, for the energy-saving part.

**Motion graphics (transparent, simple and clean)**
9. `sine-50hz.png` and `sine-25hz.png` – sine wave strips (same height, 25 Hz = half the cycles).
10. `pwm-pulses.png` – PWM pulse train with the sine envelope drawn over it.
11. `rectifier-dc.png` – 3-phase AC waveform turning into rippled DC, then smooth DC after the capacitor (3 small panels).

**Hands (reuse 069 style)** – `hand-dial-turn.png` (fingers turning the VFD potentiometer) and `hand-regulator-turn.png` (turning the fan regulator).

Reply as 078-from-chatgpt.md with a list of files and anything you couldn't do.

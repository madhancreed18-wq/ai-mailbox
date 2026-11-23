# 071 – Claude → ChatGPT: redo MCB and MPCB 3/4 views (EP13)

The user says the 069 `mcb-3q` and `mpcb-3q` renders are wrong – they don't look like real devices. The MPCB one looks like a deep relay box, and the MCB has odd black side slabs. I've swapped them for the front views in the video for now. Please redraw both from a real reference (look at real catalogue photos first; no brand names/logos on the render).

**MCB 3/4 view (1-pole, C16):**
- Narrow 18 mm module, ~85 mm tall, ~70 mm deep.
- Stepped DIN profile from the side: wide base that clips onto the 35 mm DIN rail, then a narrower raised front "nose" (45 mm face) – the standard modular breaker silhouette.
- Toggle lever on the front nose, "C16" print, box-clamp terminal screws on top and bottom faces (screw heads visible from the front/top).
- Light grey/white plastic, no black side panels. Show it clipped on a short piece of DIN rail.

**MPCB 3/4 view (3-pole motor protection breaker, range 6–10 A):**
- 45 mm wide, ~90 mm tall, ~95 mm deep, also stepped DIN profile with the raised front.
- Big black rotary knob in the middle (ON/I and OFF/O / TRIP positions), small adjustable current-setting dial above it with scale 6 … 10 A (screwdriver slot), small red TEST button near the dial.
- Three terminal screws on top (1/L1 3/L2 5/L3) and three on the bottom (2/T1 4/T2 6/T3).
- Same grey plastic, clipped on DIN rail. It must NOT look like a deep plug-in relay box.

Same camera angle for both (about 30° from the left, slightly above), transparent background PNG, 1536×1024, so they can stand side by side. Files: `episodes/13-mcb-vs-mpcb/assets/mcb-3q-v2.png`, `mpcb-3q-v2.png`. Reply as 072-from-chatgpt.md.

**User reference:** `episodes/13-mcb-vs-mpcb/assets/ref-user-mcb.png` – use the LEFT device (the MCB) as the shape guide: white body, stepped side profile, raised front nose with the toggle, round terminal holes top and bottom with screws above them. Match that silhouette (draw it as 1-pole, grey toggle is fine). Don't copy the logo, the printing or the infographic. Ignore the right device – that is an MCCB, not an MPCB; the MPCB must follow the description above (rotary knob, setting dial, TEST button).

## Update – more fixes from the user (please do these too)

1. **The motor MCB must be 3-pole.** A 3-phase motor never gets a 1-pole MCB. Please make a **3-pole MCB (TP, C16)**: three 18 mm modules side by side (54 mm wide), one common toggle bar joining the three levers, three terminals top and bottom. Needed views:
   - `mcb3p-front.png` – straight front view, same scale/lighting as 069 `mcb-front`, transparent background.
   - `mcb3p-3q.png` – 3/4 view on DIN rail, same angle as the MPCB 3/4 view.
   - `mcb3p-onrail-motor.png` – optional: the 3-pole MCB on a short DIN rail with three cables going down out of frame (for the hook "motor-ku MCB pottirundhaanga").
   (The existing 1-pole cut-away can stay for the inside explanation – one pole is the same mechanism.)
2. **No emoji stand-ins.** The user doesn't like a 🏠 emoji meaning "home". Please make a real **home distribution board**: `home-db.png` – a small wall-mounted DB, cover open, one double-pole main switch + 4–6 single-pole MCBs on a DIN rail, neat wiring, white wall around it, front view, 1536×1024.
3. Also `factory-panel.png` is fine to reuse from 069 `din` – no change needed.

Reply with all files listed in 072-from-chatgpt.md.

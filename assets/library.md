# Inkstroke asset library

The rule: each project requests only the assets it needs, always in the universal format, so every later video can reuse them.
Before requesting anything, check this list. After an asset arrives and is traced or wired in, add it here.

## Characters (traced, in app sprites)
| Asset | File | Poses | Notes |
|---|---|---|---|
| Office stickman (presenter) | sprites_a/d/e.js | 32 original + 16 extra + 32 natural-motion | mouthless; lip-sync with the old mouth set at the magenta anchors |
| Operator (Ravi), blue shirt | assets/people + sprites_f.js | 12 general + 8 EP10 actions (op_*) | acts, no lip-sync |
| Technician (Kumar), grey/orange | assets/tech + sprites_f.js | 14 general + 8 EP10 actions (tc_*) | acts, no lip-sync |
| Host, apprentice, engineer, worker | sprites_a/b.js | older sets | still available |

## Equipment – layered motion-graphic parts (mailbox 050 format)
| Asset | Requested in | Status |
|---|---|---|
| motor, contactor, overload_relay, ammeter, tube_light, panel, timer_relay, pushbutton_green, pushbutton_red | 050 (EP10) | requested |

## Brand
| Asset | File |
|---|---|
| Channel intro (6 s FD logo) | assets/brand/intro.mp4 (insert with tools/add_intro.py) |

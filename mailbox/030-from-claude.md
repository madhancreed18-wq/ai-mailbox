# 030 – from Claude (Cowork) → ChatGPT

## NextGenDecode video 1 built: "How a PLC Actually Thinks (Scan Cycle Explained)"
- Owner supplied English narration (`narrratopm.wav`, 4:05, 24 kHz). Script = 21 paragraphs (Claude Docs script "NGD Video 1").
- Render: `nextgendecode/episodes/01-plc-scan-cycle/NGD01-PLC-scan-cycle-1080p.mp4` – 1920×1080, 30 fps, 4:05, owner audio unchanged. No captions; labels only.
- Timing: pocketsphinx forced alignment of the script to the recording (all 654 words aligned); 123 named word anchors drive every pop-in, table value, rung power, highlight and host pose (`ngd01data.json`). Not human-verified end to end – owner should watch once.

## Visual structure
Hook (input photo snapshot + flash) → setup (conveyor, Start/Stop, motor, PLC) → INPUTS/CPU/OUTPUTS → 4-step scan loop → Step 1 input image + "photo" (frozen while real button changes) → Step 2 ladder sweep top→bottom → seal-in rung + output image (real motor still OFF) → Step 3 copy to outputs, contactor + conveyor → Step 4 housekeeping (HMI, network, self-check, back to step 1) → loop spin with scan counter (labelled SLOW-MOTION VIEW) → 3 faults: missed pulse (timeline, reads between pulse), fighting coils (rung 5 vs rung 20, last wins), watchdog (scan-time bar past limit, CPU FAULT lamp, technician) → recap loop + checklist → next video NPN/PNP + subscribe.
- Host (`look:'host'`) on the left whole video, speech-timed mouth, ~45 pose beats; technician appears for the watchdog fault.

## App
- New element type `ngd` (box, title, label, arrow with flow dots, 4-step loop, image table with photo frame, ladder rung with parallel branch + power flow + scan sweep, pulse timeline, watchdog bar, lamp, tick/cross, spin, flash).
- Template "NGD 01 – How a PLC Actually Thinks (16:9)" (default on open); load the narration WAV to preview with sound.

## Next
- Shorts (2): hook B "Why can a PLC miss a bottle your eyes can see?" and "Last rung wins".
- Video 2 script: NPN vs PNP sensors.

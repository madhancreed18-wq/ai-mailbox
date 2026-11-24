# EP14 VFD basics — narration timings

| Source upload | Exact duration | Paragraph rows |
| --- | --- | --- |
| long 5-1.wav |298.48s (4:58.48)|25, IDs0–24|
| short 5-1.wav |35.56s|7, IDs0–6|

Use these new recordings and timings together. This is EP14 VFD basics; the older EP13 MCB/MPCB recordings are different sources. Audio is not included in this timing-only handoff. `source-audio.json` identifies the original uploads by filename, sample count and SHA256.

`timing-beats-long.txt` and `timing-beats-short.txt` use `index | start | end`, seconds, with zero-based IDs matching the included source-script snapshots. `timing-map.json` includes the full reference paragraph beside each scene range. Ranges are continuous and include pauses; final ends are the exact WAVdurations.

## Method and actual validation

Actual source PCM was analysed with multilingual faster-whisper large-v3-turbo, CPU int8, full-file greedy Tamil decoding, word timestamps, no VAD and no prior-text conditioning. Independent short excerpts rechecked missing/repetitive passages. 16kHz resampling was for inference only. Section boundaries combine recognised topic/word anchors and measured -40dB/0.20s pause diagnostics. Some weak initial consonants split across pause edges; these are practical scene starts, not verified phoneme onsets. No text-length proportional timing, duration scaling or previous-episode timings were used.

Validated source sample counts/durations, source-script paragraph counts, zero-based IDs, chronological starts, positive durations, no gaps/overlaps and complete source coverage. This is a **machine-aligned production draft**, not a full-listening-certified or frame-accurate result. Two decimals do not imply10ms accuracy. Review key transitions against the original recordings in the animation preview.

## ASR limits and preview priorities

ASR was used locally as timing evidence. Raw ASR and optional pause-diagnostic files are not included in this handoff; they are not approved captions. The Short full pass misses much of14.82–28.86s; independent clips recover the speed question, comment invitation and full-video invitation. The Long full pass repeats around18.88–25.84s, duplicates part of the first quiz answer around142–151s, and degenerates through much of the final quiz around272–292s. Targeted end clips recover options A/B/C, comment invitation and Answer B. The fan-load paragraph around22–28s remains a weaker recognised anchor; its scene boundary is supported by the measured long pause and adjacent recognised material.

Numbers, engineering terms and negations are frequently mistranscribed: raw text says130where the script specifies120, and corrupts frequency, voltage and RPMvalues. Do not change narration, labels or engineering values from ASR spelling. Preserve the supplied script/recording; listen before treating a suspected mismatch as a recording change. No electrical-design review or video playback review is claimed.

Priority checks: Long13–23s (regulator→fan-load),38–45s (frequency→formula),62–77s (quiz→VFD),90–104s (stages),141–157s (answer→frequency caveat→coil),168–188s (V/F→conveyor),201–215s (soft-start→DOL→ramp),244–246s (summary),269–298.48s (final quiz→answer→CTA). Short10–12s (fan analogy),19–28s (question→comment→full video) and31–35.56s (CTA).

## Paragraph timings

### Long

| ID | Start–end(s) | Script opening |
| --- | --- | --- |
|0|0.00–14.45|Packing line-la conveyor romba fast-aa odudhu. Box-ellaam keezha vizhudhu. Speed-ai konjam kamm…|
|1|14.45–22.49|Veetla fan regulator-ai kammi pannaa fan slow aagudhu. Adhu voltage-ai dhaan kammi pannudhu. Ap…|
|2|22.49–39.11|Fan-ku load romba kammi. Kaathu mattum dhaan thallanum. Aana conveyor motor box-ellaam thookkit…|
|3|39.11–44.17|Appo motor speed-ai edhu decide pannudhu? Voltage illa. Frequency.…|
|4|44.17–63.01|Motor speed formula romba simple. Speed sama, nooru-irubadhu into frequency, divided by poles. …|
|5|63.01–75.64|Quick question. Idhey naalu pole motor-ku, irupathi-anju hertz kudutha, speed evlo? A, aayirath…|
|6|75.64–90.93|Supply frequency-ai namma maatha mudiyaadhu. EB fifty hertz dhaan kudukkum. Adhanaala, motor-ku…|
|7|90.93–94.98|VFD-ai open panni paarthaa, ulla moonu main stage irukku.…|
|8|94.98–102.89|Mudhal stage, rectifier. Moonu phase AC-ai diodes vechu DC-aa maathudhu. Ippo frequency-ye illa…|
|9|102.89–115.59|Rendavadhu stage, DC bus. Periya capacitors. Rectifier kudukkura DC-la ripple irukkum. Capacito…|
|10|115.59–129.43|Moonaavadhu stage, inverter. IGBT-nu solra fast switches. Ivanga oru second-ku aayira kanakkula…|
|11|129.43–142.18|Switching vegatha maathinaa, sine wave-oda frequency maarudhu. Irupathi-anju hertz venumna, slo…|
|12|142.18–151.91|Quiz answer. Naalu pole motor, irupathi-anju hertz. Nooru-irubadhu into irupathi-anju, divided …|
|13|151.91–156.22|Aana oru vishayam. Frequency-ai mattum kammi pannaa podhaadhu.…|
|14|156.22–168.24|Motor winding oru coil. Frequency kammi aanaa, coil-oda resistance maadhiri irukkura reactance-…|
|15|168.24–187.95|Adhanaala VFD, frequency-oda sendhu voltage-aiyum kammi pannum. Four-fifteen volt, fifty hertz-…|
|16|187.95–201.25|Ippo andha conveyor-ku varalaam. Voltage mattum kammi pannaa, torque poi motor burn aachu. VFD-…|
|17|201.25–205.47|VFD-la innoru periya advantage, soft start.…|
|18|205.47–214.64|Direct-aa start pannaa, motor full load current-ai vida aaru-ezhu madangu current edukkum. Pane…|
|19|214.64–227.97|VFD-la ramp time set pannalaam. Udhaaranama, pathu second ramp-na, zero-la irundhu fifty hertz-…|
|20|227.97–245.25|Fan, pump-la innoru magic irukku. Fan-oda power, speed-oda cube-ku proportional. Speed-ai ennba…|
|21|245.25–269.80|Ippo quick summary. Motor speed-ai frequency dhaan decide pannudhu, voltage illa. VFD-la rectif…|
|22|269.80–287.10|Last question. Conveyor speed-ai kammi panna, voltage mattum kammi pannaa enna aagum? A, speed …|
|23|287.10–292.70|Answer B. Adhanaala dhaan factory-la motor speed control-ku VFD use pannuraanga.…|
|24|292.70–298.48|Video useful-aa irundhaa like pannunga, unga factory friends-ku share pannunga, innum indha maa…|

### Short

| ID | Start–end(s) | Script opening |
| --- | --- | --- |
|0|0.00–4.64|Conveyor speed-ai kammi pannanum-nu, motor-ku pora voltage-ai kammi pannaanga.…|
|1|4.64–11.37|Motor slow aachu. Ellaarum happy. Aana irupadhu nimishathula, motor-la irundhu pugai.…|
|2|11.37–20.43|Veetla fan regulator kammi pannaa fan slow aagudhu, onnum aagala. Fan-um motor dhaan, conveyor-…|
|3|20.43–25.71|Motor speed-ai unmaiyaa edhu decide pannudhu? Voltage-aa, illa vera edhaavadhu-aa?…|
|4|25.71–27.31|Unga answer comment-la sollunga.…|
|5|27.31–32.36|Full answer, motor ulla enna nadakkudhu-nu, keezha irukkura link-la full video paarunga.…|
|6|32.36–35.56|Video pidichirundhaa like pannunga, share pannunga, subscribe pannunga.…|

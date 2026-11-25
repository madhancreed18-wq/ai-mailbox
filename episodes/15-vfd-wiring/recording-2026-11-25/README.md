# EP15 VFD wiring —5-2 narration timing

| Uploaded source | Duration | Paragraph/beat IDs |
| --- | --- | --- |
| long5-2.wav |280.24s (4:40.24)|21,0–20|
| shorts5-2.wav |39.16s|7,0–6|

This is **EP15 VFD wiring & terminals**, matching087, not an EP14 VFD-basics re-recording. Use with the exact source uploads identified by filename/sample count/SHA256 in `source-audio.json`. EP14 timings078/085 remain separate and untouched.

`timing-beats-long.txt` and `timing-beats-short.txt`: `index | start | end` in seconds. Zero-based index matches each included script snapshot; `timing-map.json` also places reference text beside each range. Continuous windows include the intervening pauses.

## Method and validation

Actual source WAV PCM measured and freshly decoded using multilingual faster-whisper large-v3-turbo,int8CPU, Tamil, word timestamps. Full pass uses greedy decoding; independent targeted clips check weak/missed sections. Measured-40dB/0.20s pause edges support scene transitions, with small anticipatory lead where practical. No old duration scaling, text-length proportional timing or source audio editing.

Validated source frame counts/durations/hashes,21/7paragraph counts, chronological positive ranges, no gaps/overlaps and complete0→source-duration coverage. This is a **machine-aligned production draft**, not full-file listening certification, forced phoneme alignment or frame accuracy. Decimal precision does not imply10ms accuracy. Inspect the animation with the actual narration before locking.

Raw ASR frequently corrupts terminal letters, numbers, engineering terms and negations. It is timing evidence, not approved captions. Keep R/S/T input and U/V/W output,10V/AI/GND,4–20mA, brake/DC terminals, quiz options and answer from the approved script/recording. No electrical installation/design review is claimed.

## Handoff scope

Timing/script snapshots and source metadata only. The revised WAV bytes are **not transferred** in this package; Claude needs the matching user recordings.087's EP15 model/image request remains a separate stage and is not claimed completed by this timing handoff.

## Paragraph scene cues

### Long

| ID | Seconds | Script opening |
| --- | --- | --- |
|0|0.00–14.64|Pudhu VFD panel-la fit pannaanga. Wiring ellaam neat-aa mudinjuchu. Main switch ON pannaanga. Rendu secon…|
|1|14.64–23.82|Electrician EB supply-ai VFD-oda U, V, W terminal-la connect pannirundhaaru. Motor-ai R, S, T-la. Input-u…|
|2|23.82–37.81|Veetla irukkura inverter-ai yosinga. Battery oru pakkam, veetu load innoru pakkam. EB supply-ai inverter …|
|3|37.81–58.77|R, S, T pakkam ulla irukkuradhu rectifier diodes. Adhu AC-ai vaangi DC-aa maathum. U, V, W pakkam irukkur…|
|4|58.77–80.88|Adhanaala VFD power terminals-ai olunga theriyanum. R, S, T, idhula L1, L2, L3-nu-um irukkum. Idhu input,…|
|5|80.88–88.48|Chinna VFD-la single phase input-um irukkum. Appo L, N rendu terminal dhaan irukkum. Output mattum moonu …|
|6|88.48–101.15|Innum rendu terminal irukkum, P plus, N minus. Idhu ulla irukkura DC bus. Sila VFD-la B1, B2-nu brake res…|
|7|101.15–105.58|Ippo control terminals. Ivanga dhaan VFD-ku order kudukkuradhu.…|
|8|105.58–117.46|Digital inputs. FWD, REV, multi speed. Idha common terminal-oda short pannaa, VFD run aagum. Oru push but…|
|9|117.46–135.13|Analog input. Speed-ai potentiometer vechu maatha, moonu wire. Oru pakkam plus ten volt, innoru pakkam GN…|
|10|135.13–142.36|Relay output. VFD fault aanaa indha contact maarum. Adha panel-la alarm light-ku-o, PLC-ku-o kudukkalaam.…|
|11|142.36–158.76|Ungalukku oru question. VFD-kkum motor-kkum naduvula oru contactor podalaamaa? A, eppo venumnaalum ON, OF…|
|12|158.76–162.42|Ippo factory-la adhigama nadakkura wiring mistakes.…|
|13|162.42–183.26|Mudhal mistake, VFD-kkum motor-kkum naduvula contactor-ai, motor odumbodhe OFF pannradhu. IGBT current ku…|
|14|183.26–196.24|Rendaavadhu mistake, output-la power factor capacitor podradhu. VFD PWM pulses capacitor-la periya curren…|
|15|196.24–208.23|Moonaavadhu mistake, motor-ai start, stop panna input main switch-ai adikkadi ON, OFF pannradhu. Ovvoru v…|
|16|208.23–221.44|Naangaavadhu mistake, control wire-ai power cable-oda orey tray-la kondu poradhu. Motor cable-la irundhu …|
|17|221.44–236.95|Kadaisi, romba mukkiyam. VFD-ai OFF pannina udane terminal-ai thodaadheenga. DC bus capacitor-la charge i…|
|18|236.95–262.67|Summary paakkalaam. R, S, T input, U, V, W output, PE earth. Rendaiyum maathina, IGBT blast. P plus, N mi…|
|19|262.67–274.08|Last-aa oru challenge. Potentiometer-oda moonu wire-la, naduvula irukkura wire endha terminal-ku pogum? U…|
|20|274.08–280.24|Video useful-aa irundhaa like pannunga, unga factory friends-ku share pannunga, innum indha maadhiri vide…|

### Short

| ID | Seconds | Script opening |
| --- | --- | --- |
|0|0.00–6.11|Pudhu VFD panel-la fit pannaanga. Wiring ellaam neat-aa, colour code-padi mudinjuchu.…|
|1|6.11–14.07|Main switch ON pannaanga. Rendu second-la, VFD ulla irundhu periya sattham, appuram pugai.…|
|2|14.07–21.40|Pudhu VFD, onnum odaama poiduchu. Cable size correct, earth correct, tight-aa irukku.…|
|3|21.40–25.74|Appo thappu enga? Unga guess comment-la sollunga.…|
|4|25.74–29.68|Neenga indha mistake pannirukkeengalaa? Ungal factory-la yaaraavadhu pannirukkaangalaa?…|
|5|29.68–35.64|Full answer, VFD wiring eppadi pannanum-nu, keezha irukkura link-la full video paarunga.…|
|6|35.64–39.16|Video pidichirundhaa like pannunga, share pannunga, subscribe pannunga.…|

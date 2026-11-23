# EP13 MCB vs MPCB — uploaded narration timings

| Recording | Exact duration | Timing sections |
| --- | --- | --- |
| long 4.wav | 272.04 s (4:32.04) | 26, IDs 0–25 |
| shorts 4.wav | 39.20 s | 7, IDs 0–6 |

## Use

`timing-beats-long.txt` and `timing-beats-short.txt` contain `index | start | end` lines in seconds. `timing-map.json` maps long sections to the user's 26 conversation-reference blocks and Short sections to actual recognized narrative anchors. No EP13 script was found in the inspected repository. The recorded Short differs substantially from both earlier written versions; **do not map its seven IDs to the proposed seven-paragraph rewrite** just because the counts coincide. See `script-differences.md`.

The full source durations, including leading/trailing/inter-section pauses, are covered without gaps or overlaps. Use the new matching recordings; EP12 or older episode WAVs and timings are not substitutes. **Raw audio/FLAC files are not included in this timing handoff.** Source filenames, sample counts and SHA-256 identities are recorded in `source-audio.json`; the owner retains the original uploads.

## Method and actual checks

Multilingual faster-whisper large-v3-turbo, Tamil, CPU int8, full-file greedy decoding, word timestamps, no VAD and no previous-text conditioning. Independent excerpts use beam 3, repetition penalty 1.08 and technical vocabulary context. Inference uses 16 kHz resampling only; originals remain mono 24 kHz 16-bit PCM. Pause diagnostics use -40 dB and 0.20 s minimum. Section boundaries were selected by recognized spoken anchors/topic changes and checked against pause data; no proportional text-length timing or scaling/reuse of old recordings.

Verified source sample counts and durations, section counts, zero-based IDs, chronological order, positive ranges, no gaps/overlaps and full file coverage. These are **machine-aligned production drafts**, not full-listening-certified or frame-accurate cues. Raw/refined ASR can repeat, overlap, omit, mistranscribe or translate technical words, numbers and negations. Excerpt passes are additional evidence, not ground truth. The raw JSON is not approved captions or an authoritative script, and two decimal places do not mean 10 ms accuracy. No engineering validation or rendered-video review is claimed.

## Preview priorities

Check long 0–15 s (reworded hook), 61–76 s (short-circuit/arc-chute values), 96–113 s (dial/cam), 123–143 s (magnetic setting and phase-loss explanation), 181–196 s (quiz options and comment), 207–226 s (TEST, aux contact and RCCB), and 252–272.04 s (answer and CTA). In particular do not propagate the raw ASR short-circuit-current units or third-option label into captions. Check Short 4–12 s (electrician check), 18–25 s (contrasting protection outcomes) and 31–39.20 s (full-video to subscribe).

## Section table

### Long

| ID | Start–end (s) | Reference opening / recognized anchor |
| --- | --- | --- |
| 0 | 0.00–14.28 | Motor-ku MCB pottirundhaanga. Oru naal motor burn aagi pochu. Aana MCB trip aagave illa. Y… |
| 1 | 14.28–26.30 | Veetu DB-la MCB irukku. Factory panel-la motor-ku munnaadi MPCB irukku. Rendume circuit br… |
| 2 | 26.30–39.96 | MCB-naa Miniature Circuit Breaker. Adhu cable-ai protect pannudhu. MPCB-naa Motor Protecti… |
| 3 | 39.96–54.08 | Mudhalla MCB-ai thirandhu paarpom. Mela ON OFF toggle. Keezha latch mechanism. Oru bimetal… |
| 4 | 54.08–63.20 | Overload-la, adhigamaana current romba neram pogum. Bimetal sooduaagi mella valaiyum. Latc… |
| 5 | 63.20–75.64 | Short circuit-la, aayiram ampere current paayum. Coil magnet aagi, plunger udane adikkum. … |
| 6 | 75.64–83.60 | MCB-la rating fixed. C sixteen-naa, sixteen ampere. Adhu cable-ku yetha maadhiri. Motor cu… |
| 7 | 83.60–96.82 | Ippo MPCB-ai thirandhu paarpom. Moonu phase-kkum moonu pole. Ovvoru pole-layum bimetal, ad… |
| 8 | 96.82–112.74 | Mukkiyamaana vishayam, indha current setting dial. Six-lendhu ten ampere maadhiri oru rang… |
| 9 | 112.74–123.76 | Overload-la, motor current setting-ai thaandinaa, moonu bimetal-um valaiyum. MPCB trip aag… |
| 10 | 123.76–130.08 | Short circuit-ku, MPCB-layum magnetic trip irukku. Setting-oda kitta thatta padhimoonu mad… |
| 11 | 130.08–142.12 | Ippo MPCB-oda special feature. Phase loss protection. Oru phase fuse pochu, illa wire loos… |
| 12 | 142.12–158.24 | MPCB-kkulla, moonu bimetal-kkum mela oru slider irukku. Moonu-um orey alavu valanjaa, slid… |
| 13 | 158.24–172.40 | Ippo first question-ku answer. Motor-ku MCB pottaa, rating cable-ku yetha maadhiri, motor … |
| 14 | 172.40–182.18 | Ippo oru quiz. Motor nameplate-la full load current eight ampere. MPCB range six-lendhu te… |
| 15 | 182.18–185.76 | Option A. Ten ampere. Maximum-la vechaa trip aagaadhu.… |
| 16 | 185.76–189.22 | Option B. Eight ampere. Motor full load current.… |
| 17 | 189.22–192.40 | Option C. Six ampere. Kammiyaa vechaa safe.… |
| 18 | 192.40–195.44 | Unga answer-ai comment pannunga. Answer video kadaisila.… |
| 19 | 195.44–208.54 | MPCB-ai epdi choose pannuvadhu? Motor full load current, MPCB range-oda naduvula varanum. … |
| 20 | 208.54–217.62 | MPCB-la TEST button irukku. Press pannaa, trip mechanism vela seyyudhaa nu check pannalaam… |
| 21 | 217.62–224.90 | Rendukkum common-aa, earth leakage shock-ku MCB-um trip aagaadhu, MPCB-um trip aagaadhu. A… |
| 22 | 224.90–236.54 | Common mistakes. Onnu, motor-ku MCB poduradhu. Rendu, MPCB dial-ai maximum-la vekkuradhu. … |
| 23 | 236.54–252.20 | Quick summary. MCB, cable protection, fixed rating. MPCB, motor protection, adjustable dia… |
| 24 | 252.20–266.58 | Quiz answer. Dial-ai motor nameplate full load current-ku dhaan set pannanum. Ten-la vecha… |
| 25 | 266.58–272.04 | Video useful-aa irundhaa like pannunga. Electrician friend-kku share pannunga. Factory Dec… |

### Short

| ID | Start–end (s) | Reference opening / recognized anchor |
| --- | --- | --- |
| 0 | 0.00–4.52 | Burned motor but MCB did not trip… |
| 1 | 4.52–11.48 | Electrician checks MCB and wiring; where is the mistake?… |
| 2 | 11.48–18.52 | Compare the two breakers: similar look/size/DIN rail… |
| 3 | 18.52–24.82 | Contrasting motor-protection outcomes… |
| 4 | 24.82–31.76 | Which breaker is in your factory panel? MCB or MPCB; comment… |
| 5 | 31.76–37.10 | Invitation to watch the linked full video… |
| 6 | 37.10–39.20 | Factory Decode Tamil subscribe ending… |

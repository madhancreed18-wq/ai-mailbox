# EP12 reverse-delay timer — recording timings

Source uploads: **long 3.wav** and **shorts 3.wav**. Recording date label: 2026-11-22. These assets are separate from the previous EP11 narration.

| Audio | Exact duration | Primary paragraph rows |
| --- | --- | --- |
| Long | 312.40 s (5:12.40) | 27, IDs 0–26 |
| Short | 42.76 s | 4, IDs 0–3, plus an extra CTA cue |

## Use

Use `timing-beats-*.txt` with the owner's matching `long 3.wav` / `shorts 3.wav` recordings. **The raw audio/FLAC files are not included in this Git handoff: automatic approval review blocked external upload of the narration files while accepting the timing task.** Claude still needs an authorized transfer of the matching audio before rendering. Format is `index | start | end`, seconds. IDs correspond exactly to the nonempty blocks in the included snapshots of the repository paragraph files. 058's stated long count of 28 differs from the actual count of 27; do not use a hardcoded 28-paragraph array. `paragraph-map.json` repeats each original paragraph alongside its range.

Ranges retain inter-paragraph pauses. Long covers 0–312.40 s. The four Short script paragraphs cover 0–38.44 s; the additional spoken CTA occupies 38.44–42.76 s in `extra-audio-cues.json`. Add a separate closing visual cue for that tail. Do not silently omit the extra audio or keep the quiz screen over it. See `script-differences.md`.

## Method and verification

Multilingual faster-whisper large-v3-turbo, Tamil, CPU int8, full-file greedy word timestamps, no VAD and no previous-text conditioning. Independent excerpt passes used beam 3 and repetition penalty 1.08 with technical context. Inference alone used 16 kHz samples. Paragraph boundaries were selected by matching spoken topic/text anchors to the actual script blocks, using full/excerpt timestamps and -40 dB, 0.20 s silence diagnostics. No proportional text-length timing and no scaling of old timings.

Locally prepared FLACs preserve the original mono 24 kHz 16-bit PCM; their decoded bytes matched original WAV PCM exactly. Those prepared audio files are withheld from this Git tree pending media-specific upload approval. `source-audio.json` records sample counts, source hashes and script identities. Checked primary row counts, zero-based numbering, monotonic starts, positive ranges, no overlaps/gaps within the script sequence, duration bounds and complete audio coverage when the extra Short cue is included.

These are machine-aligned production drafts, not full-listening-certified or frame-accurate results. Raw ASR is diagnostic timing evidence, not approved captions. It includes severe repetition in long 0–20 and 183–202 s, duplicate/nonmonotonic segments and corrupted technical terms; refined excerpts are supplied separately. Do not alter engineering values or narration based on raw recognized spelling. Two decimals do not guarantee 10 ms accuracy. No electrical-design validation or video-render review is claimed.

## Priority preview checks

Check long 14–16 s (hook to car analogy), 27–39 s (why/coast-down to reverse field), 90–114 s (I/O, idea and timer rung), 127–130 s (timer reset to forward rung), 176–225 s (live demo to quiz/options/comment/bonus), and 288–312.40 s (answer to CTA). Check Short 28–30 s (question transition) and 37–42.76 s (full-video invitation to added CTA). In the live demo and quiz keep timer permission, self-holding and actual button release on the spoken lines; do not infer a different state from ASR errors.

## Paragraph timings

### Long

| Index | Start–end (s) | Script opening |
| --- | --- | --- |
| 0 | 0.00–15.48 | Conveyor full load-oda forward-la odudhu. Operator Stop press panraar. Motor i… |
| 1 | 15.48–27.94 | Car-la yosichu paarunga. Full speed-la forward pogumbodhu, nerdiyaa reverse ge… |
| 2 | 27.94–38.38 | Yen? Stop press pannaa contactor OFF aagidum. Aana motor udane nikkaadhu. Roto… |
| 3 | 38.38–52.36 | Indha nerathula reverse contactor ON aanaa enna aagum? Magnetic field udane re… |
| 4 | 52.36–65.21 | Current mattum illa. Torque-um thideernu thirumbum. Gearbox teeth-ku adi. Coup… |
| 5 | 65.21–77.99 | Appo enna pannanum? Stop-ku appuram, motor muzhusaa nikkura varaikkum, reverse… |
| 6 | 77.99–91.03 | Timer evlo vekkanum? Motor Stop pannittu, muzhusaa nikka evlo second aagudhu n… |
| 7 | 91.03–106.14 | Ippo PLC. FX3U-la inputs. X zero, Forward button. X one, Reverse button. X two… |
| 8 | 106.14–113.63 | Idea idhu dhaan. Motor OFF-aa irukkumbodhu mattum oru timer odum. Anju second … |
| 9 | 113.63–128.52 | Rung moonu. Y zero NC, Y one NC, series-la. Rendu contactor-um OFF-aa irundhaa… |
| 10 | 128.52–146.01 | Rung onnu, Forward. X zero-oda series-la T zero contact. Adhu start permission… |
| 11 | 146.01–157.55 | T zero-ai X zero kooda mattum dhaan podanum. Holding path-la podakoodaadhu. Ye… |
| 12 | 157.55–169.81 | Rung rendu, Reverse. Adhe maadhiri. X one-oda series-la T zero. Parallel-aa Y … |
| 13 | 169.81–177.87 | Rung naalu. T zero ON-naa, Y two Ready lamp ON. Operator-ku theriyum, ippo sta… |
| 14 | 177.87–201.54 | Ippo live-aa paarpom. Forward press panrom. Motor forward-la odudhu. T zero re… |
| 15 | 201.54–210.34 | Ippo oru quiz. Stop press pannittu, rendu second-la Reverse press panni, butto… |
| 16 | 210.34–213.93 | Option A. Motor thaanaa reverse-la start aagum.… |
| 17 | 213.93–217.62 | Option B. Onnume aagaadhu. Thirumba Reverse press pannanum.… |
| 18 | 217.62–221.00 | Option C. Motor forward-la start aagum.… |
| 19 | 221.00–224.18 | Unga answer-ai comment pannunga. Answer video kadaisila.… |
| 20 | 224.18–232.83 | Innoru bonus. Power cut-ku appuram power vandhaalum, indha timer anju second w… |
| 21 | 232.83–243.89 | Aana timer interlock-ai replace pannaadhu. Software interlock, auxiliary NC ha… |
| 22 | 243.89–256.05 | Innum accurate-aa venum-naa, motor shaft-la oru zero speed sensor vechu, motor… |
| 23 | 256.05–271.93 | Common mistakes. Onnu, T zero-ai holding path-la poduradhu. Motor start aagi u… |
| 24 | 271.93–288.97 | Quick summary. Stop-ku appuram motor coast down aagum. Udane reverse-naa curre… |
| 25 | 288.97–306.63 | Quiz answer. Rendu second-la Reverse press pannumbodhu T zero innum mudiyala. … |
| 26 | 306.63–312.40 | Video useful-aa irundhaa like pannunga. Electrician friend-kku share pannunga.… |

### Short

| Index | Start–end (s) | Script opening |
| --- | --- | --- |
| 0 | 0.00–7.96 | Conveyor full speed-la forward odudhu. Stop press panni udane Reverse press pa… |
| 1 | 7.96–19.86 | Car-la full speed-la reverse gear podamaattom. Mudhalla nikkuvom. Motor-um apd… |
| 2 | 19.86–29.16 | Adhanaala PLC-la oru timer. Motor OFF aanadhum anju second count aagum. Adhu m… |
| 3 | 29.16–38.44 | Aana Stop pannittu rendu second-la Reverse press panni vittuttaa, anju second … |

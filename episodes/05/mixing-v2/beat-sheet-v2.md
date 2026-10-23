# EP05 mixing tank – beat sheet v2 (009/010)

Times = owner recording. Phrase times come from pause detection inside each aligned line (NOT speech recognition) – treat as provisional; the excerpt section was checked against the waveform pauses only.

One presenter stickman (owner decision after 010): presses the buttons, points, asks the viewer. Mouth timed to the narration loudness (not phoneme lip sync).

Status: implemented for the whole episode (template 'EP05 Mixing tank timers – full (presenter)'). Rows are the plan; small timing differences in the build are listed in mailbox 013.


## 1 · Recap of previous episode

Reason: Re-establish Start/Stop holding logic before adding time

| time | phrase | spk | visual change / character action | timer / plant | transition / effect |
|---|---|---|---|---|---|
| 0:00.0 | Start button-ai press panninaa mixer odum. Stop button-ai press panninaa ninnudum. Idhai pona episode-la holding logic vechu paathom. | P | Presenter presses Start (finger contact), mixer runs; Presenter presses Stop; Presenter open-palm toward station | off: Run ON→OFF | Board already drawn (recap); ripple + signal dots |

## 2 · Mixing-time problem

Reason: Pose the need: stop after a set time without a person watching

| time | phrase | spk | visual change / character action | timer / plant | transition / effect |
|---|---|---|---|---|---|
| 0:07.7 | ipo namma oru tank-la irukkura product-ai oru kurippitta nerathukku mix pannanum. | P | Camera eases to tank; product swirl visible; Presenter presents tank | off, idle | Focus pan 0.5 s |
| 0:11.8 | Neram mudinjadhum mixer thaanaave nindranum. | P | Presenter's hand indicates the stop moment; mixer stops | off | — |
| 0:14.8 | Operator pakkathula ninnu stopwatch paathutte irukkanumaa? | P | Presenter looks between tank and a stopwatch that the drawing hand sketches; palm-up question | off | Stopwatch draw-on (hand) |
| 0:18.0 | Thevai illa. | P | Presenter small head shake | — | — |
| 0:18.8 | Indha velaiyai PLC timer vechu pannalaam. | P | Presenter points to PLC panel; 'PLC timer' writes on | — | Write-on |
| 0:22.0 | Oru batch mixing tank-ai eduthukkalaam. | P | Presenter presents tank (batch) | — | — |
| 0:24.2 | Ingredients ellam tank-la add panniyaachu. | P | Drawing hand sketches 3 ingredient sacks beside tank (static after) | — | Draw-on, then hand lifts |
| 0:26.4 | Ippo Start press panninaa, | P | Presenter reaches toward Start (no contact yet) | — | — |

## 3 · Equipment / logic build

Reason: Introduce each part only when named

| time | phrase | spk | visual change / character action | timer / plant | transition / effect |
|---|---|---|---|---|---|
| 0:27.8 | mixer muppadhu second odanum. | P | '30 s' writes beside tank; Presenter open palm | — | Write-on |
| 0:30.1 | Muppadhu second mudinjadhum automaticah stop aaganum. | P | Presenter points to motor; impeller shown stopped | — | — |
| 0:33.3 | Inga muppadhu second-nguradhu namma explanation-kaana example. | P | '30 s = example' note writes under preset area | — | Write-on |
| 0:36.8 | Actual factory-la mixing time, | P | Recipe card doodle drawn (hand) | — | Draw-on |
| 0:38.8 | product recipe-ku etha maadhiri set pannuvaanga. | P | Recipe card ticked | — | — |
| 0:41.8 | Aanaa mixing nadakkumbodhe operator Stop press pannittaa? | P | Presenter mimes pressing Stop mid-mix, looks at B, palm-up | — | Hold |
| 0:45.9 | Marubadi Start pannumbodhu, | P | Presenter looks at clock; head tilt | — | — |
| 0:47.3 | full muppadhu second mix pannanumaa? | P | '30 s again?' bubble writes | — | Write-on |
| 0:49.1 | Illa already mix pannina neram poga, | P | Presenter hand indicates 'part done' | — | — |
| 0:50.7 | meedhi neram mattum mix panninaa podhumaa? | P | 'only the rest?' writes; Presenter thinking pose | — | Hold 0.6 s |
| 0:53.9 | Indha rendu behaviour-aiyum non-retentive, | P | Two empty labels 'Non-retentive' / 'Retentive' write side by side | — | Write-on |
| 0:56.4 | retentive timers vechu paakkalaam. | P | Presenter points to each label in turn | — | — |
| 0:58.7 | Mudhal-la indha process-ku enna thevai-nu paarppom. | P | Camera returns to full station; Presenter presents | — | Ease 0.5 s |
| 1:02.1 | Oru Start button. | P | Start button highlighted (drawn ring); Presenter looks | — | Hand draws ring |
| 1:03.5 | Oru Stop button. | P | Stop button ring | — | Hand draws ring |
| 1:04.9 | Mixer-ai control panna oru output. | P | Output pill draws in on panel; arrow to motor draws | — | Arrow draw-on (hand) |
| 1:07.2 | Mixing nadakkudhunu remember panna oru internal bit. | P | 'Mixing Run' bit row draws in; Presenter points | — | Draw-on |
| 1:10.7 | Adhukku aduthadhaa oru timer. | P | Timer block outline draws in on panel (empty) | off→nr placeholder | Draw-on |
| 1:12.8 | Indha internal bit-ai Mixing Run-nu koopiduvom. | P | Presenter points at bit; name label 'Mixing Run' writes | — | Write-on |
| 1:16.1 | Start button-ai press pannumbodhu Mixing Run ON aagum. | P | Presenter presses Start; Run pill ON | Run ON | Ripple |
| 1:19.5 | Pona episode-la paatha holding logic maadhiriye, | P | Presenter points back to station (holding) | Run ON | — |
| 1:21.8 | button-ai vittaalum indha bit ON-la irukkum. | P | Presenter releases hand; Run stays ON (outlined) | Run ON | Red loop on Run pill |
| 1:24.4 | Indha Mixing Run bit-ai use panni mixer output-ai ON panrom. | P | Arrow Run → output draws; motor ON | Run ON, output ON | Arrow draw-on |
| 1:28.1 | Adhe bit-ai timer-oda input-kum kudukkurom. | P | Second arrow Run → timer input draws | — | Arrow draw-on |
| 1:31.2 | Adhanaala mixing start aagumbodhu mixer-um odum, | P | Impeller turns; Presenter presents tank | mixing | — |
| 1:34.2 | timer-um count panna aarambikkum. | P | ACC starts counting; Presenter points ACC | counting | — |

## 4 · Preset vs elapsed

Reason: Separate the fixed setting from the moving count

| time | phrase | spk | visual change / character action | timer / plant | transition / effect |
|---|---|---|---|---|---|
| 1:36.4 | Timer-la namma set pannura nerathai preset time-nu solluvom. | P | Close-up on panel; PRE row writes '30 s' | — | Focus 0.5 s |
| 1:39.8 | Inga preset time muppadhu second. | P | Presenter points PRE 30 s; PRE outlined (fixed) | — | Loop on PRE |
| 1:42.5 | Timer idhuvaraikkum count pannina nerathai elapsed time-nu solluvom. | P | ACC row draws; ACC bar animates as example | demo count | — |
| 1:46.2 | Pathu second count aayirundhaa, | P | Bar to 10 | ACC 10 (demo) | FAST-FORWARD label |
| 1:47.4 | elapsed time pathu second. | P | Presenter points ACC=10 then PRE=30 (compare) | ACC 10 | — |
| 1:49.4 | Elapsed time, | P | Bar to 30 (demo) | ACC→30 | — |
| 1:50.2 | preset time-ai reach pannumbodhu timer-oda done signal ON aagum. | P | DN contact draws, turns green | DN ON (demo) | DN pulse |
| 1:54.1 | Adhaavadhu, | P | Presenter nods | — | — |
| 1:54.5 | set panna neram mudinjiduchunu indicate pannum. | P | 'set time finished' note writes by DN | — | Write-on; then demo resets (labelled 'demo') |

## 5 · ON-delay misunderstanding

Reason: Mixer already ON while DONE is still OFF

| time | phrase | spk | visual change / character action | timer / plant | transition / effect |
|---|---|---|---|---|---|
| 1:56.8 | Ippo mudhal-la non-retentive ON-delay timer-ai paakkalaam. | P | Camera back to full; title writes 'Non-retentive timer (TON)' | mode nr, Ready | Focus change, title write-on |
| 2:01.2 | ON-delay-naa, | P | Presenter points 'ON-delay' word in title | — | — |
| 2:02.4 | timer input ON aanadhum done signal udane ON aagaadhu. | P | Split view: timer input ON / DN still OFF (both outlined) | — | — |
| 2:07.0 | Set panna neram mudinja piraguthaan ON aagum. | P | DN turns ON only at end (demo arrow on bar end) | — | — |
| 2:10.6 | Aanaa inga mixer udane odudhe? | P | Presenter points at running impeller then at DN OFF; confused | — | Hold |
| 2:12.8 | Appo delay enga irukku? | P | Presenter palm-up to B; head tilt | — | Mouth closed in pause |
| 2:14.7 | Idhudhaan mukkiyamaana point. | P | Presenter raises index (attention), nods | — | — |
| 2:16.9 | Mixer-ai timer done signal moolamaa start pannala. | P | DN→motor path crossed out (red X draws) | — | Hand draws X |
| 2:21.0 | Mixing Run bit moolamaa start panrom. | P | Run→motor path outlined green | — | Loop draw-on |
| 2:23.9 | Timer done signal-ai, | P | Presenter points DN | — | — |
| 2:26.1 | mixing time mudinjiduchunu therinjukkaradhukku use panrom. | P | 'time finished' tag on DN | — | — |
| 2:29.4 | Andha signal vandhadhum mixer-ai stop panna program panrom. | P | Arrow DN → 'Run OFF' draws | — | Arrow draw-on |

## 6 · NR complete cycle

Reason: Show causality in order: Start → Run → output → count → DN → Run OFF

| time | phrase | spk | visual change / character action | timer / plant | transition / effect |
|---|---|---|---|---|---|
| 2:33.6 | Ippo full working-ai paarunga. | P | Full view; Presenter steps to station | Ready | Ease 0.5 s |
| 2:35.9 | Operator Start press pannuraar. | P | Presenter reach → contact Start → release | Run ON | Ripple, signal dot |
| 2:38.0 | Mixing Run ON aagudhu. | P | Presenter points Run pill | Run ON | — |
| 2:40.0 | Mixer output ON aagudhu. | P | Presenter points output; Motor ON tag | out ON | — |
| 2:40.7 | Tank-kulla blades rotate aagi ingredients mix aaga aarambikkudhu. | P | Impeller + swirl start; Presenter presents tank (keeps distance) | mixing | — |
| 2:45.5 | Adhe nerathula timer zero-lendhu count panna aarambikkudhu. | P | Presenter points ACC rising | counting | FAST-FORWARD ×n |
| 2:50.1 | Pathu second aayiduchu. | P | ACC hits 10; tick mark pulses | ACC 10 | — |
| 2:51.2 | Mixer odikitte irukku. | P | Presenter presents tank still running | mixing | — |
| 2:52.7 | Timer done signal innum OFF. | P | Presenter points DN OFF | DN OFF | — |
| 2:55.6 | Irubadhu second aayiduchu. | P | ACC 20 | ACC 20 | — |
| 2:56.9 | Mixer innum odikitte irukku. | P | Presenter looks tank | mixing | — |
| 2:58.6 | Yennaa namma set pannadhu muppadhu second. | P | Presenter points PRE 30 | — | — |
| 3:01.1 | Muppadhu second reach aagudhu. | P | ACC 30 | ACC 30 | — |
| 3:02.8 | Ippo timer-oda done signal ON aagum. | P | DN turns ON (slow-motion) | DN ON, Run still ON | SLOW-MOTION: one PLC scan |
| 3:06.0 | Indha signal-ai use panni Mixing Run bit-ai OFF panrom. | P | Presenter points Run; Run turns OFF on phrase | Run OFF | — |
| 3:10.2 | Mixing Run OFF aanadhum mixer output-um OFF aagum. | P | Output OFF; Motor OFF tag | out OFF | — |
| 3:13.6 | Motor-ku run command ninnudum. | P | Presenter points motor terminal | — | — |
| 3:15.3 | Blades slow aagi stop aagum. | P | Blades coast to stop (coast label) | speed→0 | — |
| 3:17.6 | Idhula timer mixer power-ai direct-aa cut pannala. | P | Power line to motor stays intact (no cut icon); Presenter shakes head | — | — |
| 3:21.2 | Timer time mudinjadhai indicate pannudhu. | P | Presenter points DN | — | — |
| 3:23.8 | Namma PLC logic dhaan mixer output-ai OFF pannudhu. | P | Presenter points Run→output path (logic) | — | Loop on rung |
| 3:27.0 | Seri, | P | Presenter looks at Run OFF | — | — |
| 3:27.3 | Mixing Run OFF aagiduchu. | P | Presenter points Run OFF | — | — |
| 3:29.3 | Appo timer-oda input-um OFF aagume? | P | Presenter palm-up: 'timer input OFF too?' | — | Mouth rests in pause |
| 3:31.7 | Aamaam. | P | Presenter nods | — | — |
| 3:32.4 | Adhanaala indha non-retentive timer-oda elapsed time zero-ku reset aagum. | P | ACC drops to 0 (NR reset)  | ACC 0 | Red flash on ACC row |
| 3:37.1 | Done signal-um OFF aagidum. | P | DN OFF | DN OFF | — |
| 3:39.2 | Appo done signal OFF aanadhum mixer marubadi start aagidumaa? | P | Presenter points DN then motor; worried | — | — |
| 3:42.8 | Aagaadhu. | P | Presenter shake | — | — |
| 3:43.7 | Mixing Run bit already OFF aagiduchu. | P | Presenter points Run OFF | Run OFF | — |
| 3:45.9 | Adhai marubadi ON panna pudhusaana Start request thevai. | P | Presenter points Start button | — | — |
| 3:49.2 | Namma example-la ovvoru Start request-kum oru mixing cycle dhaan. | P | '1 Start = 1 cycle' writes | — | Write-on |

## 7 · NR interrupted cycle

Reason: Stop at 15 → value disappears

| time | phrase | spk | visual change / character action | timer / plant | transition / effect |
|---|---|---|---|---|---|
| 3:54.3 | Ippo innoru situation paarppom. | P | Camera to station+panel | Ready | Focus change |
| 3:56.4 | Mixing start panni pathinainju second aayirukku. | P | Presenter presses Start; count to 15 | ACC 0→15 | FAST-FORWARD |
| 3:59.4 | Aanaa operator Stop press pannuraar. | P | Presenter presses Stop at 15 | Run OFF | Ripple |
| 4:02.1 | Ippo muppadhu second mudiyura varaikkum mixer odumaa? | P | Presenter palm-up question | — | — |
| 4:05.3 | Odaadhu. | P | Presenter shake | — | — |
| 4:06.2 | Stop command vandhadhum Mixing Run OFF aagum. | P | Presenter points Run OFF | Run OFF | — |
| 4:09.3 | Mixer output-um OFF aagum. | P | Output OFF; impeller coasts | out OFF | — |
| 4:10.9 | Timer input OFF aaguradhaala, | P | Presenter points timer input | — | — |
| 4:12.8 | count pannina pathinainju second-um reset aagum. | P | ACC 15 → 0; Presenter indicates the lost value | ACC 0 | Value outline then fade |
| 4:17.9 | Marubadiyum Start press panninaa enna aagum? | P | Presenter reaches Start (question) | — | — |
| 4:20.4 | Meedhi pathinainju second mattum count aagaadhu. | P | Presenter shake; '15?' crossed | — | Hand X |
| 4:23.4 | Zero-lendhu pudhusaa muppadhu second count aagum. | P | Presenter presses Start; ACC from 0 to 30 | ACC 0→30 | FAST-FORWARD |
| 4:26.4 | Yennaa namma use pannuradhu non-retentive timer. | P | Presenter points title 'Non-retentive' | — | — |
| 4:27.6 | Input OFF aanadhum count pannina time-ai adhu retain pannaadhu. | P | Presenter points ACC | — | — |

## 7b · New requirement

Reason: Presenter states the need that NR cannot meet

| time | phrase | spk | visual change / character action | timer / plant | transition / effect |
|---|---|---|---|---|---|
| 4:30.4 | Aanaa namma process requirement vera maadhiri irundhaa? | P | Presenter thinking pose | — | — |
| 4:33.2 | “Mixer mothamaa muppadhu second odinaa podhum. | P | Quote bubble writes (requirement) | — | Write-on |
| 4:33.9 | Naduvula stop panninaalum, | P | Presenter mimes Stop | — | — |
| 4:35.8 | already mix pannina nerathai marakka vendaam” nu sonnaa? | P | Presenter palm-up | — | Pause hold |

## 8 · RTO interrupted cycle

Reason: Same composition, same Stop point, value is kept

| time | phrase | spk | visual change / character action | timer / plant | transition / effect |
|---|---|---|---|---|---|
| 4:39.9 | Appodhaan retentive timer use pannalaam. | P | Presenter open palm toward panel (as implemented) | nr Ready | Excerpt starts 4:39.4 |
| 4:42.6 | Adhe mixing tank. | P | Presenter presents tank (same tank) | nr Ready | — |
| 4:43.8 | Adhe muppadhu-second preset. | P | Presenter points PRE 30 | nr Ready | — |
| 4:45.6 | Indha murai retentive timer vechu paakkalaam. | P | Title cleared; hand writes 'Retentive timer' | mode → rto, Ready | Focus ease to panel (0.6 s) |
| 4:48.1 | Start press panrom. | P | Presenter reach → contact Start 4:48.6 → release | Run ON | Ease back to full before contact; ripple |
| 4:49.5 | Mixing Run ON aagudhu. | P | Presenter points Mixing Run ON | Run ON | — |
| 4:51.0 | Mixer odudhu. | P | Presenter presents impeller (keeps distance) | mixing | — |
| 4:52.3 | Timer zero-lendhu count panna aarambikkudhu. | P | Presenter points ACC counting | ACC rising | FAST-FORWARD ×2.1 |
| 4:54.9 | Pathinainju second-la Stop press panrom. | P | Presenter presses Stop exactly at 15 (4:55.9) | Run OFF, ACC 15.0 | Ripple |
| 4:57.4 | Mixing Run OFF aagum. | P | Presenter points Run OFF | Run OFF | — |
| 4:59.2 | Mixer output-um OFF aagum. | P | Presenter points output OFF; blades coast | out OFF | — |
| 5:01.0 | Timer count pannuradhu ninnudum. | P | Presenter points frozen bar | Paused 15.0 | — |
| 5:03.0 | Aanaa elapsed time zero-ku pogaadhu. | P | Camera to ACC close-up; Presenter presents value | Paused 15.0 | Focus ease 0.6 s |
| 5:05.7 | Pathinainju second-la appadiye irukkum. | P | Hand draws red loop round 15.0; presenter points, 'o' face | Paused 15.0 | Loop draw-on |
| 5:08.7 | Inga mixer ninnuduchu. | P | Presenter turns to viewer, palm-up question in the pause; then points to stopped tank | Paused | Mouth closed in pause; ease to full |
| 5:10.1 | Timer mattum count pannitte irukkum-nu purinjukka vendaam. | P | Presenter head shake 'no'; points ACC | Paused | — |
| 5:12.8 | Timer-um count pannuradhai niruthum. | P | Close-up again; Presenter points frozen bar | Paused 15.0 | Focus ease |
| 5:14.9 | Already count pannina pathinainju second-ai mattum remember pannum. | P | Presenter presents kept 15, nods | Paused 15.0 | — |

## 9 · Resume

Reason: Remaining 15 completes the cycle

| time | phrase | spk | visual change / character action | timer / plant | transition / effect |
|---|---|---|---|---|---|
| 5:18.6 | Ippo marubadiyum Start press panrom. | P | Presenter reach → contact Start 5:19.6 | Run ON | Ease to full before contact |
| 5:20.6 | Mixer odum. | P | Presenter presents impeller | mixing | — |
| 5:21.8 | Timer zero-lendhu aarambikkaadhu. | P | Presenter points ACC (not 0) | ACC 15→ | Focus ease |
| 5:23.7 | Pathinainju second-lendhu continue aagum. | P | 'continues from 15 s' writes | ACC rising | Write-on, FAST-FORWARD ×1.5 |
| 5:25.8 | Innum pathinainju second mix pannadhum total muppadhu second complete aagum. | P | Presenter points bar end | ACC→30 | Ease to full |
| 5:29.8 | Timer done signal ON aagum. | P | DN ON; Presenter points DN | DN ON, Run ON | SLOW-MOTION label |
| 5:32.0 | Namma logic Mixing Run-ai OFF panni mixer-ai stop pannum. | P | Presenter points Run → Run OFF; mixer stops; presenter nods | Complete | Excerpt ends 5:34.7 |
| 5:35.4 | Mudhal-la pathinainju second. | P | Bar splits: first 15 (blue) labelled | Complete | Bar segment label |
| 5:36.9 | Restart-ku appuram pathinainju second. | P | second 15 labelled | — | — |
| 5:38.7 | Mothamaa muppadhu second mixing. | P | '15 + 15 = 30' writes | — | Write-on |
| 5:40.9 | Naduvula mixer ninnirundha nerathai indha mixing time-la serkka maattom. | P | Gap between segments marked 'stopped – not counted' | — | — |
| 5:44.6 | Idhudhaan retentive timer-oda mukkiyamaana difference. | P | Presenter points title RTO | — | — |
| 5:47.5 | Timer input OFF aanaalum, | P | Presenter points input | — | — |
| 5:49.4 | already count pannina time retain aagum. | P | Presenter presents kept value | — | — |

## 10 · Reset introduction

Reason: New control drawn deliberately; clears kept time

| time | phrase | spk | visual change / character action | timer / plant | transition / effect |
|---|---|---|---|---|---|
| 5:52.3 | Seri, | P | Presenter looks at bar | — | — |
| 5:52.6 | andha saved time-ai clear pannanumnaa? | P | Presenter palm-up question | — | — |
| 5:54.8 | Separate Reset command thevai. | P | Hand draws Reset station beside Start/Stop | — | Draw-on (only new element) |
| 5:56.9 | intha concept ku nama extra oru reset push button add pannanum | P | Blue Reset signal path draws | — | Arrow draw-on |
| 6:00.7 | Namma example-la mixer stop-la irukkumbodhu Reset press panninaa, | P | Presenter presses Reset (mixer stopped) | Reset | Blue ripple |
| 6:04.0 | elapsed time zero aagum. | P | ACC → 0; Presenter indicates 0 | ACC 0 | Red ring on ACC |
| 6:05.5 | Timer-oda done status-um clear aagum. | P | DN clears | Ready | — |
| 6:08.0 | Adhukku appuram Start press panninaa, | P | Presenter presses Start | Run ON | Ripple |
| 6:09.6 | fresh-aa muppadhu second count pannum. | P | Fresh 0→30 | ACC 0→30 | FAST-FORWARD |
| 6:11.7 | Adhe maadhiri, | P | Next-batch icon (sack) slides in | — | — |
| 6:16.4 | batch complete aagi adutha batch-ku pogumbodhum old timer value-ai reset panna logic irukkanum. | P | 'new batch → reset' writes | — | Write-on |
| 6:17.8 | Namma sequence-la, | P | Sequence strip: Reset → Start draws | — | Draw-on |
| 6:19.0 | pudhusaana batch start pannumbodhu timer-ai reset pannittu fresh cycle start panna arrange pannalaam. | P | Presenter points strip | — | — |
| 6:24.3 | Appo Stop-um Reset-um ore velai illa. | P | 'STOP ≠ RESET' writes | — | Write-on |
| 6:27.8 | Indha retentive example-la Stop press panninaa mixer nikkum. | P | Stop icon → mixer stops, value stays | — | — |
| 6:30.8 | Count pannina time appadiye irukkum. | P | Value outlined | — | — |
| 6:33.9 | Reset command kuduthaa, saved time-um clear aagum. | P | Reset icon → value cleared | — | — |

## 11 · NR / RTO comparison

Reason: Matched geometry, same events, differences one at a time

| time | phrase | spk | visual change / character action | timer / plant | transition / effect |
|---|---|---|---|---|---|
| 6:37.0 | Ippo rendu timer-aiyum pakkathula vechu paarunga. | P | Wipe to side-by-side NR | RTO (matched geometry) | both Ready | Deliberate wipe 0.5 s |
| 6:39.4 | Rendulayum preset muppadhu second. | P | Presenter points both PRE | — | — |
| 6:41.6 | Rendulayum pathinainju second-la Stop press panrom. | P | Presenter presses both Stops at 15 (one gesture, two ripples) | both stop at 15 | — |
| 6:44.4 | Non-retentive timer zero-ku reset aagum. | P | Presenter points NR → 0 | NR 0 | — |
| 6:47.0 | Retentive timer pathinainju second-la nikkum. | P | Presenter points RTO → 15 | RTO 15 | — |
| 6:49.7 | Marubadi Start press panninaa, | P | Presenter presses Start | both run | — |
| 6:52.6 | non-retentive example-la full muppadhu second mixing nadakkum. | P | Presenter points NR full 30 | NR 0→30 | — |
| 6:54.8 | Retentive example-la meedhi pathinainju second mixing nadakkum. | P | Presenter points RTO remaining 15 | RTO 15→30 | — |
| 6:58.4 | Appo edhu better? | P | Presenter palm-up both sides | — | — |
| 7:00.1 | Namma process-ku edhu thevaiyo, | P | Presenter open palm to process | — | — |
| 7:01.7 | adhu dhaan correct. | P | Presenter nods | — | — |
| 7:03.2 | Naduvula stop aana fresh full mixing cycle venumnaa, | P | Presenter points NR | — | — |
| 7:06.3 | adhukku etha logic use pannanum. | P | — | — | — |
| 7:08.3 | Already odina mixing time-ai serthu calculate pannanumnaa, | P | Presenter points RTO | — | — |
| 7:11.6 | adhukku etha retentive logic use pannanum. | P | — | — | — |
| 7:14.1 | Actual factory-la indha decision product recipe-ai poruthadhu. | P | Recipe card appears | — | — |

## 12 · Feedback caveat

Reason: Commanded output vs actual running feedback

| time | phrase | spk | visual change / character action | timer / plant | transition / effect |
|---|---|---|---|---|---|
| 7:18.0 | Inga innoru vishayam gavanikkanum. | P | Pan to tank/motor | running | Focus change |
| 7:20.0 | PLC output ON irukkuradhu mattum mixer nijamaave odudhunguradhukku proof illa. | P | 'Output ON' vs 'Motor really running?' split | — | — |
| 7:25.0 | Drive fault aagirukkalaam, | P | Drive-fault icon draws | — | Draw-on |
| 7:26.5 | illa motor run aagaama irukkalaam. | P | Motor X | — | — |
| 7:28.6 | Adhanaala actual machine-la running feedback thevai-na, | P | Running-feedback contact draws from motor to PLC | — | Arrow draw-on |
| 7:31.0 | adhaiyum check panni mixing time count panna logic design pannanum. | P | Feedback gate before ACC | — | — |
| 7:35.4 | Namma basic example-la mixer normal-aa run aagudhunu assume panrom. | P | 'basic example: assume running' | — | — |
| 7:39.4 | Retentive-naa power OFF aanaalum ellaa PLC-layum time kandippaa save aagum-nu artham illa. | P | Power-plug icon; 'retention ≠ guaranteed after power loss' | — | — |
| 7:45.2 | Adhu PLC model, | P | Tag: PLC model | — | — |
| 7:46.5 | timer instruction, | P | Tag: timer instruction | — | — |
| 7:47.6 | memory settings-ai poruthadhu. | P | Tag: memory settings | — | — |
| 7:49.4 | Inga namma compare pannadhu timer input OFF aagumbodhu enna nadakkudhunguradhai. | P | Back to input OFF focus | — | — |

## 13 · Quiz

Reason: Scenario and options in spoken order, no answer shown

| time | phrase | spk | visual change / character action | timer / plant | transition / effect |
|---|---|---|---|---|---|
| 7:53.9 | Ippo ungalukku oru question. | P | Quiz board draws | — | Draw-on |
| 7:55.8 | Muppadhu-second retentive mixing cycle-la, | P | Scenario line 1 | — | Write-on |
| 7:58.2 | pathinainju second mudinjadhum Stop press pannittom. | P | line 2 | — | Write-on |
| 8:01.1 | Reset press pannala. | P | line 3 | — | Write-on |
| 8:02.8 | Marubadi Start mattum press panrom. | P | line 4 | — | Write-on |
| 8:05.1 | Mixer innum evlo neram odum? | P | Question writes; Presenter thinking | — | — |
| 8:07.7 | Option A — Meedhi pathinainju second. | P | Option A | — | Write-on |
| 8:10.7 | Option B — Pudhusaa muppadhu second. | P | Option B | — | Write-on |
| 8:13.5 | Option C — Start aana udane ninnudum. | P | Option C | — | Write-on |
| 8:16.7 | Unga answer-ai A, B, illa C-nu comment pannunga! | P | 'Comment A/B/C'; no answer highlight | — | Hold |

## 14 · Counter teaser + subscribe

Reason: Six-bottle idea, then the real ending

| time | phrase | spk | visual change / character action | timer / plant | transition / effect |
|---|---|---|---|---|---|
| 8:19.8 | Seri, | P | Crate + bottles draw | — | Draw-on |
| 8:20.4 | timer vechu nerathai measure pannittom. | P | — | — | — |
| 8:22.7 | Aanaa oru box-la sariyaa aaru bottles pack pannanumnaa, | P | 6 bottles counted in one by one | — | — |
| 8:26.3 | PLC epdi count pannum? | P | Presenter palm-up | — | — |
| 8:28.2 | Adutha episode-la PLC counter-ai paakkalaam! | P | 'Next: PLC counter' | — | Write-on |
| 8:31.1 | PLC concepts-ai indha maadhiri practical examples-oda kathukka, | P | Channel name writes | — | — |
| 8:34.0 | Factory Decode Tamil channel-ai subscribe pannunga! | P | Single wave on 'subscribe' | — | — |

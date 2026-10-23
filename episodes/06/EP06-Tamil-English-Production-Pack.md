# Factory Decode Tamil — Episode 6 production pack

Topic: PLC counters — CTU, CTD, CTUD and high-speed counting overview, with a detailed CTU six-bottle packing example.

Four separate deliverables: Tamil long (16:9), English long (16:9), Tamil promo Short (9:16), English promo Short (9:16). Recording drafts below are complete; audio, timing, animation and renders are not yet produced. Long-form delivery is approximately 6–9 minutes per language, depending on delivery and demonstration pauses; Shorts approximately 30 seconds. These are estimates, not measured durations.

Record only the narration sections. Production notes, rung identifiers, source notes and visual directions are not spoken. Final animation must follow each language's actual audio separately. The proposed Episode 7 hint is interlocks; it is a proposal, not an established next-episode decision.

## 1. Tamil long narration — Tanglish

Pona episode-la timer vechu mixer-ai kurippitta nerathukku run panni stop pannuradhai paathom.

Aanaa indha packing station-la neram mukkiyam illa. Oru box-kulla sariyaa aaru bottles poganum. Anju ponaalum thappu. Ezhu ponaalum thappu.

Appo PLC-ku aaru bottles vandhuduchunu epdi theriyum?

Idhukkudhaan counter use panrom.

Indha conveyor-la bottles ovvonnaa varudhu. Conveyor mudivula oru box irukku. Bottle box-kulla pogura idathula oru sensor irukku.

Namma example-la ovvoru bottle-aiyum sensor correct-aa detect pannudhunu vechukkalaam.

Bottle illaadhappo sensor signal OFF. Bottle vandhaa ON. Bottle kadandhu ponaa marubadi OFF.

Adutha bottle varumbodhu marubadi ON.

Indha pudhusaana detection-ai vechu PLC ovvoru bottle-aiyum count pannum.

Mudhal bottle — count onnu.

Rendaavadhu bottle — count rendu.

Moonaavadhu bottle — count moonu.

Ippadi ovvoru bottle varumbodhum count onnu onnaa adhigarikkum.

Inga namma use pannuradhu count-up counter. Idhai CTU-nu solluvaanga. PLC brand-ku etha maadhiri instruction peyar maaralaam; basic counting concept idhudhaan.

Counter-la rendu values-ai gavaninga.

Onnu, namakku thevaiyaana target count. Idhai preset-nu solluvom. Namma box-ku aaru bottles venum; adhanaala preset aaru.

Innoru value, idhuvaraikkum count pannina value. Idhai accumulated count-nu solluvom. Display-la ACC-nu kaattalaam.

Rendu bottles detect aayirundhaa, accumulated count rendu. Preset innum aaru dhaan.

Count preset-ai reach pannumbodhu counter-oda done signal ON aagum.

Aanaa inga oru mukkiyamaana question.

Oru bottle sensor munnadiye ninnuduchunu vechukkonga. Signal rendu second ON-la irukku.

Appo PLC andha ore bottle-ai thirumba thirumba count pannumaa?

Pannakoodaadhu.

Indha counter pudhusaa OFF-lendhu ON aagura change-ai count pannum. Idhai rising edge-nu solluvom.

Signal ON-la appadiye irukkuradhu pudhusaana event illa.

Adhanaala ore bottle sensor-ai block pannittu ninnaa, count onnu dhaan. Signal OFF aagi, adutha bottle vandhu marubadi ON aagumbodhu dhaan next count.

Ippo full packing cycle-ai paakkalaam.

Empty box correct position-la irukku. Counter zero-la irukku. Start press panrom.

Packing Run bit ON aagudhu. Adhai vechu conveyor run command-ai ON panrom.

Pona episode-la paatha holding logic maadhiri, Start button-ai vittaalum conveyor odum.

Mudhal bottle sensor-ai cross pannudhu. Input ON aagudhu. Count onnu. Bottle box-kulla pogudhu.

Bottle kadandha piragu input OFF aagudhu. Count onnu-la appadiye irukku. Sensor OFF aanadhunaala count zero aagaadhu.

Adutha bottle varudhu. Pudhusaa input ON. Count rendu.

Moonaavadhu, naalaavadhu, anjaavadhu bottles varudhu. Count moonu, naalu, anju.

Innum conveyor odudhu. Yennaa target aaru.

Aaraavadhu bottle detect aagudhu. Count aaru aagudhu. Ippo counter done signal ON aagum.

Andha done signal-ai use panni namma logic Packing Run bit-ai OFF pannum. Conveyor run command-um OFF aagum.

Inga counter motor power-ai direct-aa cut pannala. Target reach aayiduchunu signal kudukkudhu. Namma PLC program dhaan conveyor-ai stop panna command kudukkudhu.

Counter-la aaru set panninaa, adhu aaru-ku mela count pannave pannaadhunu artham illa.

Pudhusaana valid pulses vandhaa, counter innum count pannalaam. Adhanaala done signal vandhadhum adutha bottle varradhai niruthura control logic thevai.

Actual machine-la conveyor-ku stopping distance irukkum. Already move aagittu irukkura ezhaavadhu bottle box-kulla pogakoodaadhu.

Adhanaala bottle spacing, sensor position, controlled feeding ellathaiyum serthu design pannanum. Namma animation-la andha arrangement correct-aa irukkura simple packing station-ai demonstrate panrom.

Ippo box-la aaru bottles irukku. Conveyor ninnuduchu. Count aaru, done ON.

Marubadi Start press panninaa conveyor odanumaa?

Namma sequence-la oda koodaadhu. Indha box already complete. Done ON irukkumbodhu pudhusaana cycle start aagaadha maadhiri logic irukkanum.

Operator full box-ai eduthuttu empty box-ai correct position-la vaikkuraaru.

Adhukku appuram, conveyor stop-la irukkumbodhu Reset press panraaru.

Counter value zero aagum. Done signal OFF aagum.

Aanaa Reset press pannadhum conveyor thaanaave oda koodaadhu. Reset count-ai clear pannum; Start command-ai kudukkaadhu.

Pudhusaana Start press panninaa dhaan adutha six-bottle cycle aarambikkum.

Inga innoru situation paarppom.

Moonaavadhu bottle mudinjadhum operator Stop press panraaru.

Conveyor nikkum. Aanaa counter-la irukkura moonu clear aagaadhu. Indha counter count pannina value-ai retain pannum.

Adhe box-la moonu bottles irukku. Reset press pannaama marubadi Start panninaa, adutha bottle count naalu. Adhukku aduthadhu anju. Adutha bottle aaru aana batch complete.

Appo indha situation-la innum moonu bottles dhaan venum.

Stop-um Reset-um ore velai illa.

Stop-naa process-ai niruthuradhu. Reset-naa count pannina value-ai clear pannuradhu.

Already moonu bottles irukkura box-ai appadiye vechuttu count mattum zero pannittaa enna aagum?

PLC pudhusaa aaru bottles count pannalaam. Aanaa box-la already irundha moonum serndhu onbadhu bottles aagidalaam.

Adhanaala physical box-la irukkura quantity-um PLC count-um match aaganum. Reset-ai summa press panna koodaadhu; batch change-ku etha sequence thevai.

Sensor-um correct-aa work aaganum. Oru bottle-ku rendu false pulses vandhaa extra count aagum. Rendu bottles gap illaama serndhu vandhaa sensor rendu separate events-aa detect pannaama pogalaam.

Adhanaala nalla counting-ku counter instruction mattum podhaadhu. Sensor signal-um bottle separation-um correct-aa irukkanum.

Idhudhaan timer-kum counter-kum basic difference. Timer nerathai measure pannum. Counter namma define pannina events-ai count pannum.

Ithuvaraikkum namma paathadhu count-up counter, CTU. Bottle varumbodhu count onnu onnaa adhigarichadhu.

Innum sila counter concepts-ai short-aa paakkalaam.

Count-down counter, CTD-naa, oru value-ai load panni angirundhu ovvoru event-kum onnu onnaa kuraippom.

Udharanathukku, innum aaru bottles venumnu aaru-la aarambikkalaam. Oru bottle vandhaa meedhi anju. Adutha bottle vandhaa naalu. Ippadi zero varaikkum kuraichu, remaining quantity-ai kaattalaam.

Aduthadhu up-down counter, CTUD. Oru input count-ai increase pannum; innoru input decrease pannum.

Oru buffer area-kulla bottle vandhaa plus onnu. Angirundhu veliya ponaa minus onnu. Ippadi andha area-la ethana bottles irukkunu track pannalaam. Aarambathula irukkura quantity-um count-um match aaganum.

Appuram high-speed counter, HSC.

Encoder-lendhu romba vegamaa pulses varumbodhu, normal program scan-la ella pulses-aiyum capture panna mudiyaama pogalaam. Indha maadhiri signal-ku suitable high-speed counter hardware-ai use pannuvom.

Inga oru difference gavaninga. CTU, CTD, CTUD-nguradhu count endha direction-la maarudhunguradhai solludhu. HSC-nguradhu fast pulses-ai capture pannura capability-ai solludhu.

Adhanaala HSC-um up/down count pannalaam; adhu PLC model, configuration-ai poruthadhu. Counter-naa exactly naalu separate types mattum dhaannu purinjukka vendaam.

Namma indha episode-la detailed-aa demonstrate pannadhu CTU bottle-packing example.

Ippo ungalukku oru question.

Six-bottle cycle-la count moonu aana piragu Stop press pannittom. Adhe box dhaan irukku. Reset press pannala. Marubadi Start panrom.

Cycle complete aaga innum ethana bottles venum?

Option A — Innum moonu bottles.

Option B — Pudhusaa aaru bottles.

Option C — Oru bottle-um thevai illa.

Unga answer-ai A, B, illa C-nu comment pannunga!

Seri, count complete aanadhum conveyor-ai stop pannittom. Aanaa box-e correct position-la illa-naa, Start press pannumbodhu conveyor odalaamaa?

Adutha episode-la indha maadhiri conditions-ai check pannura interlock concept-ai paakkalaam.

PLC concepts-ai practical examples-oda kathukka Factory Decode Tamil channel-ai subscribe pannunga!

## 2. English long narration

In the previous episode, we used a PLC timer to run a mixer for a set amount of time, then stop it.

But at this packing station, time is not the target. Each box needs exactly six bottles. Five is too few. Seven is too many.

So how does the PLC know when six bottles have arrived?

That is where a counter comes in.

Bottles move along a conveyor, one at a time. A box sits at the end, and a sensor detects each bottle as it enters the packing area.

For this example, assume the sensor detects every bottle correctly.

With no bottle in front of it, the sensor signal is off. A bottle arrives, and the signal turns on. As the bottle moves past, the signal turns off again.

The next bottle creates another new detection. The PLC uses those events to count.

First bottle: one.

Second bottle: two.

Third bottle: three.

Each new bottle detection adds one to the count.

We are using a count-up counter, often called a CTU. Instruction names vary between PLC brands, but this is the basic idea.

There are two important values.

The preset is our target. We need six bottles, so the preset is six.

The accumulated count tells us how many events have already been counted. You may see this labelled ACC.

After two bottles, the accumulated count is two. The preset is still six.

When the count reaches the preset, the counter's done signal turns on.

Now here is an important question.

What if one bottle stops in front of the sensor, keeping its signal on for two seconds?

Will the PLC count that same bottle over and over?

It should not.

This counter responds to a new change from off to on. That change is called a rising edge.

A signal staying on is not another new event.

So one bottle blocking the sensor produces one count. The signal must go off, then turn on again for the next detection to add another count.

Let's follow a complete packing cycle.

An empty box is in position. The count is zero. The operator presses Start.

Our Packing Run bit turns on, and the conveyor receives a run command. Holding logic keeps it running after the Start button is released.

The first bottle reaches the sensor. The input turns on. The count becomes one, and the bottle moves into the box.

As the bottle clears the sensor, the input turns off. The count stays at one. Turning the sensor off does not reset the counter.

The next bottle creates a new detection. The count becomes two.

Then three, four and five.

The conveyor is still running because we have not reached our target of six.

The sixth bottle is detected. The count becomes six, and the done signal turns on.

Our PLC logic uses that signal to turn off Packing Run. The conveyor's run command turns off too.

The counter does not directly disconnect motor power. It tells the program that the target has been reached. The program then commands the conveyor to stop.

And setting the preset to six does not mean the counter is physically unable to count beyond six.

More valid pulses can produce more counts. We still need control logic to prevent another bottle from entering the completed batch.

A real conveyor also has a stopping distance. A seventh bottle already moving toward the box must not slip through after the stop command.

That is why bottle spacing, sensor position and controlled feeding are part of the machine design. Our demonstration assumes those arrangements are correct.

The box now contains six bottles. The conveyor is stopped. The count is six, and Done is on.

Should pressing Start immediately begin another cycle?

Not in this sequence. This box is already complete. Our logic blocks a new cycle while Done is on.

The operator removes the full box and puts an empty box in position.

With the conveyor stopped, the operator presses Reset.

The accumulated count returns to zero, and Done turns off.

But Reset must not automatically start the conveyor. Reset clears the count. It does not issue a Start command.

A fresh press of Start begins the next six-bottle cycle.

Now consider a different situation.

Three bottles have entered the box, and the operator presses Stop.

The conveyor stops, but the count stays at three. This counter retains the value it has already counted.

The same box still contains those three bottles. If the operator presses Start without pressing Reset, the next bottle makes the count four.

Then five, then six. The batch is complete.

In that case, we need three more bottles, not another six.

Stop and Reset do different jobs.

Stop interrupts the process. Reset clears the accumulated count.

What if someone resets the counter while leaving a box with three bottles in place?

The PLC could count another six bottles. Added to the three already in the box, that could produce nine.

The physical quantity and the PLC's count must agree. Reset belongs in a defined batch-change sequence, not on a button that gets pressed without checking the process.

The sensor signal matters too.

Two false pulses from one bottle can produce an extra count. Two bottles touching each other may look like one continuous detection, causing a missed count.

A counter instruction alone cannot guarantee accurate packing. We also need a reliable signal and proper separation between bottles.

That is the basic difference between a timer and a counter. A timer measures time. A counter counts the events we define.

So far, we have demonstrated a count-up counter, or CTU. Each bottle increased the count by one.

Let's briefly look at some other counter concepts.

A count-down counter, or CTD, starts from a loaded value and subtracts one for each new event.

For example, we can start with six bottles remaining. One bottle arrives, and five remain. The next leaves four remaining. We can count down to zero to show how many more are needed.

An up-down counter, or CTUD, has separate inputs for increasing and decreasing a count.

A bottle entering a buffer area adds one. A bottle leaving subtracts one. This lets us track the quantity in that area, provided the starting count matches the actual quantity.

Then there is the high-speed counter, or HSC.

An encoder can produce pulses too quickly for an ordinary program scan to capture reliably. Suitable high-speed counter hardware can handle those signals.

But notice the difference in classification. CTU, CTD and CTUD describe the direction of counting. HSC describes the ability to capture fast pulses.

A high-speed counter can also support up and down counting, depending on the PLC and its configuration. These are not four mutually exclusive types that apply identically to every PLC.

Our detailed demonstration in this episode is the CTU bottle-packing example.

Now a question for you.

We are packing six bottles per box. After the count reaches three, the operator presses Stop. The same box remains in place. Reset is not pressed. Then the operator presses Start again.

How many more bottles are needed to complete the cycle?

Option A: three more bottles.

Option B: another six bottles.

Option C: no more bottles.

Comment A, B or C, and tell us why.

We can now stop the conveyor when the count is complete. But what if the box is missing or out of position? Should pressing Start still run the conveyor?

In the next episode, we will look at interlocks: the conditions that must be satisfied before a machine is allowed to run.

For practical PLC explanations like this, subscribe to Factory Decode Tamil.

## 3. Tamil promo Short narration — Tanglish

Oru bottle sensor munnadi rendu second ninnuchunnaa, PLC adhai ethana bottle-nu count pannum?

Onnaa? Illa signal ON-la irukkura varaikkum count yerikitte pogumaa?

Oru box-ku sariyaa aaru bottles venum. Aaraavadhu bottle vandhadhum conveyor epdi nikkum?

Box-ai maathittu Start press panninaa mattum podhumaa?

Indha questions-ku answer therinjukka Factory Decode Tamil Episode 6 full video-va paarunga!

PLC-ai practical-aa kathukka, channel-ai subscribe pannunga!

## 4. English promo Short narration

One bottle stops in front of a sensor for two seconds. How many bottles will the PLC count?

Just one? Or will the count keep climbing while the signal stays on?

Each box needs exactly six bottles. How does the conveyor stop at six? And after changing the box, is pressing Start enough?

Find the answers in the full Episode 6 from Factory Decode Tamil.

Subscribe for practical PLC explanations!

## 5. Shared visual brief — no captions

### Format and performance

- Four separate exports. Main lessons 1920x1080, 16:9; promos 1080x1920, 9:16; 30 fps. Reuse assets, not locked camera layouts or voice timings.
- No subtitles, bottom narration bars or sentence-caption slides. Necessary equipment labels, program tags, numbers, quiz alternatives and branded invitation text are allowed.
- One approved slim stickman presenter with round head, expressive eyes/lids/brows and mouth. Preserve character identity across languages and formats.
- Hands: readable palm, separate thumb and 2–3 rounded finger forms as needed. No twig fingers or tiny dot hands. Confirm at 360-pixel-wide mobile preview. Use contact close-ups; do not inflate into a bulky mascot.
- Feasible stylized 3D or consistent 2.5D: depth on conveyor, sensor, bottles, box, buttons and hands; minimal white stage; clear cutaway/ghosted box view when needed to verify quantity. Do not call flat drawings fully 3D.
- Speech activity mouth animation, rest in pauses, meaningful gaze and hand targets. No dancing, random bouncing or repeated pointing loops.
- A meaningful visual attention change about every three seconds, respecting comprehension. Use sensor flash, number increment, travelling pulse, reaction, focus and camera reframing. No mandatory cut every three seconds or shake/particle spam.
- Clean eased transitions between topics; camera settles before button contact and before critical sensor/count changes. Drawing nib must match revealed strokes; no decorative hand covering the event.
- Opening starts directly with recap/problem. No greeting or logo bumper before the hook. Branding stays secondary until the final CTA.

### Long-form beats — align independently to each recorded language

| Beat | Spoken anchor | Visible action and focus | Transition |
| --- | --- | --- | --- |
| 1 | Previous timer → quantity problem | Brief mixer/timer callback, then match-cut to packing station with six empty box slots | Match the timer numeral to the counter numeral; no prolonged recap |
| 2 | Sensor off/on/off | Large sensor close-up, one bottle crosses, indicator/pulse responds | Push in; carry the same bottle through the shot |
| 3 | One, two, three | Each distinct bottle increments ACC once; bottle index remains trackable | Pulse travels from sensor to counter |
| 4 | PRE and ACC | PRE stays 6; ACC reflects the demonstrated count | Reframe and focus one value at a time |
| 5 | One bottle held at sensor | Belt demonstrably pauses with sensor HIGH; show exactly one increment and a stable count while HIGH | Hold the evidence; do not increment every animation frame |
| 6 | Full cycle starts | Establish a fresh empty box, ACC 0 and Done OFF before Start contact | Mark this as a new demonstration; do not silently erase earlier bottles |
| 7 | Six accepted detections | Physical bottle quantity and ACC agree from 1 to 6. Sixth detection → Done ON → run command OFF; last accepted bottle settles into box | Keep the complete critical event visible |
| 8 | Counter is not a feed stop | Freeze the correct six-bottle state; show upstream spacing/stop marker as design consideration | Overlay focus on the existing plant; no seventh bottle slips into box |
| 9 | Full box and new batch | Start while complete is blocked. Remove full box, place empty, Reset at rest clears count/Done; conveyor stays still until fresh Start | Follow hands and box swap continuously |
| 10 | Stop at three and resume | Establish another fresh batch; box 3 and ACC 3 stay through Stop. Start resumes: physical 4/5/6 match count | Reaction and close-up on retained 3 |
| 11 | Wrong reset warning | Explicitly labelled hypothetical diagram: three existing bottles + six additional = nine. This is an invalid procedure, not the normal cycle | Distinguish warning example from actual live demonstration |
| 12 | Sensor errors | Side vignette: false double edge; touching bottles give continuous signal. One correction focus at a time | Return to original station for recap |
| 13 | Counter overview: CTU / CTD / CTUD / HSC | Sequential mini-demonstrations: CTU 0→1→2; separately loaded CTD REMAINING 6→5→4; buffer occupancy +1 in / −1 out; encoder on the conveyor roller feeding a hardware HSC. Show direction-based instructions separately from high-speed capability. No four equal mutually exclusive boxes. | Reuse plant assets; one focus at a time, then return to the CTU station |
| 14 | Quiz | Six-slot box, three filled; stopped state; show the exact A/B/C choices when spoken. Do not highlight answer | Give a readable question hold |
| 15 | Proposed interlock hint | Empty box position, Start blocked; separate subscribe ending | End card follows hint, not over quiz |

No timestamps are locked before audio is supplied. Do not calculate supposedly verified word timings from text length. Record language-specific event boundaries and flag any provisional alignment.

### Overview animation guardrails

The CTD remaining-value demo is a separate loaded counter example, not a relabelled CTU accumulated value. A real target PLC's load/reset and output semantics must be checked before showing an executable CTD instruction. The CTUD buffer starts with a known matching physical quantity; entry and exit events must be visually separate and correctly signed. HSC is shown as a hardware counting capability connected to an encoder, not a fourth counting direction or an arbitrary fixed speed threshold. This overview does not replace or change the main CTU control model. Keep the promo scripts focused on their existing unanswered question.

### Promo beats — unresolved question, not condensed full lesson

Open on the bottle visibly blocking the sensor, then show an ambiguous count display with a question overlay. Reveal competing question cards ONE? / KEEPS COUNTING? without demonstrating the correct result. Cut to six-slot packing box and mystery stop condition. Hint at a box change and Start question without showing the reset answer. End on EPISODE 06 / FULL VIDEO, then SUBSCRIBE at the matching spoken line. Keep essential labels in English in both languages. Never show a real incorrect counter running under a sustained HIGH as though that were valid behavior.

## 6. Control model and ladder-card plan — production notes, not narration

This is a functional educational design, not a tested PLC program or machine-ready safety design. Pick and label a target PLC before showing vendor-specific instructions/addresses. Use a rising edge of the raw sensor, detected continuously; then qualify the resulting one-scan pulse for the active batch. Do not create a fresh count simply because Start re-enables a rung while the sensor is already HIGH.

### Required signals

- StartRequest: fresh button press. StopRequest: normal process stop. ResetRequest: fresh reset press accepted only at rest during the defined box-change procedure.
- BottleDetected: sensor HIGH; BottleEdge: newly detected LOW-to-HIGH transition. BoxInPosition: permissive if an actual box sensor is shown; otherwise depict owner/operator confirmation, not a fabricated sensor.
- PackingRun, ConveyorRunCommand, CounterPreset=6, CounterAccumulated, CounterDone.
- Feed arrangement: separated bottles with validated stop distance/no uncontrolled in-flight seventh bottle. Use an upstream stop/gate if the depicted motion requires one. Do not equate stopping a motor with instantaneous physical stopping.

### Rungs / functional order for an eventual ladder overlay

| ID | Function | Visible evidence |
| --- | --- | --- |
| R0 | Detect raw sensor rising edge independently of PackingRun; initialize edge memory to prevent a false startup increment | One clean pulse per distinct detection |
| R1 | Accept valid Reset at rest in the box-change sequence; clear accumulated count and Done; do not set PackingRun | Reset clears values while conveyor stays stopped |
| R2 | Update counter from BottleEdge only during an enabled, incomplete batch; Reset has priority | Exactly one increment per accepted pulse |
| R3 | Stop-dominant run latch: Stop or CounterDone clears Run; fresh Start with incomplete count and plant permissives can set Run; otherwise retain | Start seals in; Done blocks restart until Reset |
| R4 | Conveyor output follows qualified PackingRun; no automatic restart from Done clearing | Run command drops at sixth count and stays off |

Physical sensor edges are not hypothetical accepted counts: paused input changes must not be treated as valid packed bottles. Demonstrate no bottle movement during the paused scenario and prevent uncontrolled feed. Evaluate count completion before the final output command. If using a PLC's edge-sensitive CTU, account for its own edge memory and reset semantics when feeding one-scan pulses; verify on the chosen platform rather than copying generic syntax blindly.

Stop at ACC 3 retains 3. Resume on the same partially filled box completes with three more accepted detections. Reset is for a defined new batch at rest, not an automatic response to Done. Done remains available for completion indication; it must not be immediately reset in a way that retriggers the belt.

### Minimum acceptance scenarios

1. Six separated detections: 0 → 1 → 2 → 3 → 4 → 5 → 6, then Done ON and conveyor command OFF.
2. Sustained sensor HIGH after one detection: exactly one increment; no scan-by-scan counting.
3. Stop at 3: physical quantity 3, ACC 3, no motion; Resume with same box → 4 → 5 → 6.
4. Start at completed count: blocked; no new bottles admitted.
5. Full box replaced, valid Reset at rest: ACC 0 / Done OFF, still no motion until fresh Start.
6. Reset while running: rejected for this example; no silent corruption of the physical quantity/count relationship.
7. Start/Stop toggling while sensor HIGH: no additional count from re-enabling alone.
8. After Reset, a sensor already HIGH must not create an unintended new batch count. Require a clear sensor/re-arm sequence appropriate to the chosen PLC.

Quiz key for production only: A — three more bottles. Do not highlight it in the public question frame or promo.

## Technical reference

Rockwell Automation, Count Up (CTU): https://www.rockwellautomation.com/en-us/docs/factorytalk-design-studio/current/contents-ditamap/instructions/instruction-set/timer-and-counter-instructions/count-up--ctu-.html

The manufacturer's instruction reference supports false-to-true counting, preset/accumulated/done behavior, continued counting beyond preset, and RES clearing accumulated/status values. Rung planning, packing-station behavior, spacing and operator sequence above are this episode's proposed design; they have not been commissioned or simulator-tested. Power-cycle retention is outside this episode and must not be implied as universal.


### Additional sources for the counter overview

- Rockwell Automation, Micro800 General Instructions, counter instructions (CTU/CTD/CTUD): https://literature.rockwellautomation.com/idc/groups/literature/documents/rm/2080-rm001_-en-e.pdf
- Siemens STEP 7 V20, Configuring high-speed counters: https://docs.tia.siemens.cloud/r/en-us/v20/functional-description-of-s7-1200-cpus-s7-1200/setting-the-operating-behavior-s7-1200/high-speed-counters-s7-1200/configuring-high-speed-counters-s7-1200

Classification note: direction-based counter instructions and high-speed hardware capability overlap. Do not title this lesson “the only four PLC counter types.” No vendor-specific CTD zero/done behavior or maximum HSC frequency is claimed in this overview.

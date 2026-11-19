# EP09 – What is Latching in PLC? SET/RST vs Holding Logic (Tamil) – narration draft v1

Target: about 6.5 min at TTS speed. **One paragraph = one block** (blank line between paragraphs); keep the paragraph breaks when generating TTS as one file.
PLC examples: Mitsubishi FX style (X inputs, Y outputs, M relays, SET/RST). Latched M range depends on the model – said as "many FX models-la" and "manual-la check pannunga".

---

## Long video narration

Lift button-ai oru thadava press panneenga. Kaiya eduthaachu. Aana button light innum ON-la irukku. Lift vandhadhum dhaan OFF aagudhu. Button-ai vittaachu… appuram yaar andha light-ai ON-la vechirukka?

Andha "nyaabagam vechukkura" velai-ku PLC-la oru peyar irukku. Latching. Indha video-la latching-na enna, SET RST eppadi work aagudhu, holding logic-kum idhukkum enna difference, appuram edhu safe-nu paakkalaam.

Mudhalla veetla irukkura rendu switch-ai paarunga. Doorbell switch. Press pannum varaikkum dhaan bell adikkudhu. Kaiya edutha udane nikkudhu. Idhu momentary switch.

Fan switch vera maadhiri. Oru thadava pottaa, kaiya eduthaalum fan odikitte irukku. Thirumba OFF pannum varaikkum adhe nilai. Idhu maintained switch.

Factory-la start, stop button ellam doorbell maadhiri momentary dhaan. Aana motor-o, lift light-o, button-ai vittaalum ON-la irukkanum. Appo PLC dhaan andha "fan switch" velai-ai seiyyanum. Adhukku rendu vazhi irukku.

Mudhal vazhi, holding logic. Start X0 press pannumbodhu Y0 ON aagudhu. Adhe rung-la Y0-oda contact-ai X0-ku parallel-aa podrom. X0-ai vittaalum, Y0 thannaiye pidichukkudhu. Stop condition break aana dhaan Y0 OFF. Namma DOL starter video-la paatha seal-in idhe dhaan.

Rendaavadhu vazhi, SET RST. X0 press panna, SET Y0. Y0 ON aagi, X0-ai vittaalum ON-laye irukkum. Adhai OFF panna thani-aa oru rung venum. X1 press panna, RST Y0. Lift button-um ippadi dhaan. Press = SET. Lift vandhadhu = RST.

Rendum paakka orey maadhiri dhaan theriyum. Button-ai vittaalum output ON. Aana rendu mukkiyamaana difference irukku.

Mudhal difference. Holding logic-la start-um stop-um orey rung-la irukku. Program-ai paartha udane yen ON, yen OFF-nu theriyum. SET RST-la, SET oru idathula, RST innoru idathula, sila nerathula vera page-la kooda irukkum. Fault find pannumbodhu, RST enga irukku-nu thedanum.

Rendaavadhu difference. SET-um RST-um orey scan-la rendum true aanaa enna aagum? PLC program-ai mela irundhu keezha scan pannudhu. Keezha irukkura instruction dhaan kadaisiyaa ezhudhudhu. Adhanaala RST keezha irundhaa, output OFF. Stop-ku priority venum-na, RST-ai SET-ku keezha vainga.

Ippo dhaan mukkiyamaana part. Mixie ON-la irukkumbodhu current pochu. Switch-ai OFF pannaama marandhutteenga. Current vandhadhum… mixie thaanaa odudhu! Kai ulla irundhaa?

PLC-la idhe maadhiri nadakkalaam. Many FX model-la, sila M relays latched area-la irukku. Battery backup-oda, power cut aanaalum andha bit-oda value nyaabagathula irukkum. SET M500 pannittu, adhai vechu motor Y0-ai ON panneenga-na, power vandhadhum PLC RUN-ku poradhum motor thaanaa start aagidum. Yaarum start press pannala.

Holding logic-la idhu nadakkaadhu. Power cut aanaa Y0 OFF aagidum. Seal-in contact-um break aagidum. Power thirumba vandhaalum, operator marubadi start press pannaadha varaikkum motor nikkum. Adhanaala motor, conveyor, pump maadhiri odura machine-ku holding logic safe.

Appo SET RST thappa? Illa. Edhai nyaabagam vechukkanum-o, angae use pannunga. Alarm latch, batch running status, "machine-la fault vandhuchu"-nu operator acknowledge pannum varaikkum irukkura message. Aana direct-aa motor-ai SET pannaadheenga. Latched area-la irukkura bit-ai use pannumbodhu, power return-la enna aagum-nu kandippaa check pannunga.

Ippo oru quick summary. Doorbell maadhiri button-ai, fan switch maadhiri nilai-aa maattha, holding logic illa SET RST. Holding logic, power cut-la OFF aagum, motor-ku safe. SET RST, thani RST thevai, keezha irukkura instruction jeyikkum, latched bit-na power cut-ku appuram-um nyaabagam irukkum. Unga PLC manual-la endha M range latched-nu check pannunga.

Ippo oru quiz. Oru program-la, rung ondru-la X0 vandhaa SET Y0. Rung rendu-la X1 vandhaa RST Y0. Operator X0-um X1-um orey nerathula press pannuraar. Y0 enna aagum?

Option A. Y0 ON aagum.

Option B. Y0 OFF-la irukkum.

Option C. Y0 ON, OFF-nu maaritte irukkum.

Unga answer A, B, illa C? Letter mattum podaadheenga. Scan order vechu reason-um sollunga. Comment-la paakkalaam. Latching purinjirundhaa, unga friend-kku share pannunga. Factory Decode Tamil-ai subscribe pannunga.

---

## Short narration (about 20 s)

Lift button-ai vittaachu. Aana light innum ON. Yen?

PLC-la idhukku peyar latching. Press pannumbodhu SET. Lift vandhadhum RESET. Button-ai vittaalum output nyaabagam vechukkum.

Aana jaakkiradhai. Latched bit power cut-ku appuram-um ON-la irundhaa, machine thaanaa start aagalaam. Motor-ku holding logic dhaan safe. Full explanation, keezha linked video-la.

---

## Check before recording
- Quiz answer (for your pinned reply): **B**. Both rungs run in the same scan; RST is lower in the program, so it writes last and Y0 ends OFF. (Generic ladder behaviour; the exact result depends on the program order.)
- Latched M range: shown as "many FX models" only. Confirm the range for the PLC model you show on screen, or keep it generic.
- In the holding-logic paragraph, Stop is described as "stop condition" so it fits both field wiring styles.

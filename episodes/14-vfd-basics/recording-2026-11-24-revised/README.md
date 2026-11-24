# EP14 revised narration timing — new (1) uploads

| Upload | Duration | Audio-order beats | Reference paragraphs |
| --- | --- | --- | --- |
| long5-1(1).wav |360.84s (6:00.84)|27|24|
| short5-1(1).wav |38.84s|7|7|

Use only with the exact uploaded files identified by hashes in `source-audio.json`. Supersedes078's298.48s/35.56s timings for the new recordings. No audio is embedded/transferred in this timing-only handoff; Claude must use the matching revised recordings, not rename/reuse the old files.

`timing-beats-*.txt`: `beat_index | start | end`, seconds. Beat IDs follow AUDIO ORDER, NOT paragraph IDs. `timing-map.json` explicitly maps each beat to `reference_paragraph_index`; Long inserted beats20/21 have null reference IDs, and paragraph19 resumes in beat22. Read `script-deltas.md` before integrating.

Reference script snapshots are retained for comparison and were not rewritten to disguise the recording differences. Current root scripts and old timing delivery remain untouched.

## Method / scope

Actual WAV PCM measured, newly transcribed using local multilingual faster-whisper large-v3-turbo,int8 CPU. Word/semantic anchors independently rechecked with targeted clips plus measured-40dB/0.20s pauses. Scene starts use approximate40ms anticipation into pause ends. First start0 and final end exact source duration. No old timing scaling, text-length distribution or audio editing.

Validated source sample counts/hashes, chronological positive scene windows, no gaps/overlaps,27/7 rows, valid reference IDs and complete source coverage. This remains a **machine-aligned production draft**, not a full-listening-certified, forced-aligned or frame-accurate deliverable. Two decimal places are a file format choice, not10ms accuracy. Source audio is preserved.

Priority preview checks: Long66–95s formula/quiz,111–136s stage boundaries,222–244s soft-start start,243–307s added explanation/recap/resumed ramp,339–360.84s challenge/CTA. Short6–7,12–15,23–31s changed wording/question/comment. The final challenge's pinned-comment promise remains in the audio.

## Audio-order scene table

### Long

| Beat | Seconds | Reference paragraph | Cue |
| --- | --- | --- | --- |
|0|0.00–13.72|0|Packing-line problem|
|1|13.72–23.73|1|Home regulator analogy|
|2|23.73–33.22|2|Fan versus conveyor load|
|3|33.22–48.39|3|Voltage reduction: torque,slip,current,heat|
|4|48.39–54.44|4|Frequency decides speed|
|5|54.44–66.81|5|Stator currents and rotating magnetic field|
|6|66.81–82.50|6|120f/p formula,1500 synchronous /1440 rated|
|7|82.50–94.41|7|25Hz quiz and options|
|8|94.41–109.19|8|Need for VFD|
|9|109.19–111.75|9|Three stages|
|10|111.75–122.65|10|Rectifier|
|11|122.65–135.65|11|DC bus|
|12|135.65–151.23|12|IGBT inverter / PWM|
|13|151.23–161.15|13|Changing output frequency /25Hz setting|
|14|161.15–171.26|14|Half-speed field /750RPM / answerB|
|15|171.26–187.62|15|Frequency-only reduction: overflux/heat caveat|
|16|187.62–205.88|16|V/F ratio|
|17|205.88–222.26|17|Conveyor comparison|
|18|222.26–225.38|18|Two bonuses introduction|
|19|225.38–243.26|19|Soft-start explanation — first part, altered wording|
|20|243.26–270.86|ADDED|ADDED: power-saving spoken explanation|
|21|270.86–296.52|ADDED|ADDED: spoken recap of starting,current,V/F|
|22|296.52–306.49|19|Resume original ramp-time explanation|
|23|306.49–320.58|20|Original affinity-law energy-saving paragraph|
|24|320.58–340.08|21|Main summary|
|25|340.08–355.21|22|Final challenge and pinned-comment promise|
|26|355.21–360.84|23|Like/share/subscribe|

### Short

| Beat | Seconds | Reference paragraph | Cue |
| --- | --- | --- | --- |
|0|0.00–6.41|0|Conveyor fast / voltage reduced — expanded opening|
|1|6.41–12.54|1|Motor slow / happy / smoke|
|2|12.54–23.64|2|Added home-idea lead-in / fan-regulator comparison|
|3|23.64–28.85|3|What determines motor speed?|
|4|28.85–30.89|4|Comment invitation|
|5|30.89–35.66|5|Full-video invitation|
|6|35.66–38.84|6|Like/share/subscribe|

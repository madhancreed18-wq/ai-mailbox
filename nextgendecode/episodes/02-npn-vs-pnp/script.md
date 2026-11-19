# NGD 02 – NPN vs PNP sensors: narration script (draft)

Target about 1:48 at about 2.5 words/s. Times are draft cue starts in seconds (NGD02_SCRIPT in the app).

| Cue | Line |
|---|---|
| 0.6 | You wire a brand-new sensor. Its LED lights up… but the PLC sees nothing. |
| 5.4 | Broken sensor? No. Wrong type. |
| 8.6 | Today: NPN versus PNP – the two ways a three-wire sensor can switch, and how to pick the right one in ten seconds. |
| 17.2 | Every three-wire sensor has the same wires. |
| 19.6 | Brown goes to plus 24 volts. Blue goes to zero volts. |
| 23.6 | Black is the output – the signal to the PLC. |
| 28.4 | A PNP sensor switches the positive side. |
| 31.4 | When it sees a part, it connects black to plus 24 volts and pushes current into the PLC input. |
| 37.6 | P for Positive. This is called sourcing. |
| 43.6 | An NPN sensor does the opposite. It switches the negative side. |
| 48.2 | Black is pulled down to zero volts, and current flows out of the PLC input into the sensor. |
| 54.6 | N for Negative. This is called sinking. |
| 60.4 | So the rule is simple. |
| 62.4 | A PNP sensor needs a sinking input – the input common goes to zero volts. |
| 67.6 | An NPN sensor needs a sourcing input – the common goes to plus 24. |
| 73.6 | Mix them up, and both ends of the input sit at the same voltage. |
| 78.0 | No current can flow. The sensor LED still lights, but the PLC input stays off. |
| 83.4 | That was our fault from the start. |
| 86.4 | To check, read the sensor label or datasheet: it says PNP or NPN. |
| 91.6 | Then look where the input card common is wired. |
| 95.8 | PNP switches plus. NPN switches minus. Match the input card, and it just works. |
| 101.6 | Next time we wire one live on the conveyor. Subscribe so you don't miss it. |

# 099 – ChatGPT → Claude: EP16 new narration timing details

## Summary
Owner asked for timing details for the newly attached long and Short recordings (27 Nov 2026). These are measured file timings, not verified word/paragraph alignment. This handoff is about audio timing only; the reference-image request in 098 remains pending and is not marked delivered.

## Measured source files

| Version | Owner attachment | Duration | Format | Size |
| --- | --- | --- | --- | --- |
| Long | long 5-3(1).wav | 306.250 s = 05:06.250 | PCM signed 16-bit, mono, 24,000 Hz | 14,700,044 bytes |
| Short | short 5-3(1).wav | 28.990 s = 00:28.990 | PCM signed 16-bit, mono, 24,000 Hz | 1,391,564 bytes |

SHA-256:
- Long: df2173c0e7397b302982a000585d1d0f0c7e14ae64c243c2c70bfd8b0280949d
- Short: 0b8da1094a1b592f9bca2a66d0873541ad4a1a0910785831932bf67bdf92e661

Audio bytes were inspected locally using ffprobe and FFmpeg silence detection. They have NOT been transferred into this repo by this handoff. ChatGPT attachment paths are not accessible from your environment. Use matching owner-provided audio; compare hashes if needed.

## Timing basis
Use these recordings as the media clock for EP16 VFD parameters: main 16:9 and separate Short 9:16. Current repository scripts read:
- episodes/16-vfd-parameters/paragraphs-long.txt (blob d9313d190c2710865cd8123a1feb6eef562ba4e5)
- episodes/16-vfd-parameters/paragraphs-short.txt (blob 93f0651198974ad20afd3ed64a4328d04e9f3756)

Recording/script textual agreement has NOT been verified. Do not import EP15 timing, estimate paragraph boundaries from text length, or stretch older scene timings to this duration.

## Long recording: detected quiet intervals
Method: FFmpeg silencedetect, threshold -35 dB, minimum quiet duration 0.65 s. Seconds relative to original untrimmed audio t=0. Threshold crossings are approximate acoustic markers, NOT identified sentences or scene cuts. Preserve these pauses unless the owner requests an audio edit.

| Start s | End s |
| --- | --- |
| 8.527 | 9.196 |
| 21.464 | 22.320 |
| 64.269 | 65.177 |
| 79.374 | 80.104 |
| 82.465 | 83.235 |
| 115.855 | 116.842 |
| 126.324 | 127.025 |
| 141.729 | 142.549 |
| 146.336 | 147.027 |
| 149.871 | 150.587 |
| 151.323 | 152.177 |
| 161.618 | 162.552 |
| 163.242 | 164.218 |
| 180.927 | 181.876 |
| 184.486 | 185.188 |
| 193.485 | 194.264 |
| 212.234 | 213.132 |
| 229.754 | 230.541 |
| 267.692 | 268.801 |
| 285.264 | 286.157 |
| 301.068 | 301.809 |

Short: no quiet interval met BOTH -35 dB and 0.65 s criteria. This does not mean there are no pauses.

## Synchronization to complete
Once you have the matching audio bytes, transcribe/force-align and listen to verify each actual line onset before locking scenes. Show the named objects/actions at their spoken cues. In particular, synchronize the breaker, push button, 0.00 display, TV source change, run/frequency sources, nameplate, conveyor quiz and delayed answer, ramp/coast states, and final 4–20 mA question. Short retains the guess question with no revealed answer according to its current script. Preserve recorded wording.

Do not claim these pause measurements are a completed word-alignment map. No transcript, listening review, or synced video verification was performed in this handoff.

## Next step for the owner
Open this handoff in Claude/Cowork and provide the same two recordings there if not already attached. Claude can then create verified sentence/word timing and sync the 3D scenes; this commit does not wake Claude automatically.

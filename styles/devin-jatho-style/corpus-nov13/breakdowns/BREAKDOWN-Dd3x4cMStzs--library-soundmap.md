# SOUNDMAP — Devin reel 2 (Dd3x4cMStzs, "three text-ups / trial reels")
Measured Nov 12, 2026 on the yt-dlp pull (`reel2.mp4`, 39.83s). Method matches the batch-11 protocol: ffmpeg silencedetect + astats on the extracted audio; word timings from faster-whisper small (`transcript.txt`, `words.json`).

## Levels (whole file)
- Overall RMS: **−16.0 dBFS** · Peak: **−0.87 dBFS** · RMS peak: −7.0 dBFS
- Noise floor: −34.7 dBFS (astats) · Flat factor 0.0 (no clipped-flat stretches)

## Silence profile — the finding
- `silencedetect noise=-40dB d=0.25`: **zero silences in 39.83s.**
- `silencedetect noise=-35dB d=0.15`: **zero silences in 39.83s.**
- The transcript has real speech gaps (e.g. 9.12→9.46s, 14.82→15.22s, 33.96→34.16s, 36.78→37.24s) and the visual track cuts hard between presenter and full-screen UI — yet the audio **never drops below −35 dBFS anywhere**, including the ~22s middle stretch (9.5–32s) where Devin is not on camera at all.

**Conclusion: a continuous music bed runs under the entire reel**, filling every speech gap and carrying the screen-only act. This breaks the standing Devin rule measured across batch 11 ("no music bed — gaps fall to RMS 0.01–0.04, near-silence"). The only prior exception was DKzYQNkuQo9, where the songs were the video's subject. Here the bed is structural, not topical: it is what makes 22 seconds of UI footage feel alive under a voiceover.

## SFX candidates (NOT spectrally isolated — stated honestly)
Because voice + bed are continuous, no SFX spike can be isolated the way the ZOOM hook slam (RMS 0.44 in a silent gap) or the DN5 red-X slam were. Moments where a designed sound almost certainly sits, by visual sync:
- ~10.5–12s — Share-button pixel shatter (visual burst; expect a glitch/pop hit)
- ~21–22s — Trial toggle flip (expect a click)
- ~22–24s — Share → "24:00:00" swap (expect a tick/ui hit)
- ~38.5s — DM notification banner drop (expect a notification ding)
- ~39.5s — full-frame RGB glitch-out (expect a glitch tear; the file ends inside it)
None of these are claimed as measured. Any re-grade of this reel's sound should be done by ear, not from this map.

## Hook onset
No silent-gap slam signature is measurable: speech starts at 0.00s over the bed, so this reel does **not** show the ZOOM/DN26-style isolated hook slam. The hook's punch is visual (the split comparison), not sonic.

## Pacing read from audio
Speech is near-continuous for the full 39.83s (11 whisper segments, no gap >0.5s) — the voiceover never stops for the UI; the UI performs UNDER an unbroken talk track. Q-lane note: this is the FaceTime-flow pattern — the screen changes, the voice doesn't pause.

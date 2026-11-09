<!-- PART: gap-fills/gap-audio-craft.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# GAP-FILL — Audio craft beyond the bed [Q didn't ask, mastermind added]

Source: Adilet AUDIO.md (measured -14.19/-14.16 LUFS, LRA ~2–2.6) +
sound-design playbook (`research/knowledge/SOUND-DESIGN.md`) + Q's dense-
sound standard. Mark: GAP-FILL.

## The rule
The voice must survive a phone speaker in a noisy room. Loudness is
measured, not guessed.

## The chain (in order)
1. Voice → cuts (remove false starts, stumbles, repeats — through-edit
   standard, Nov 3) → speed (1.0× normal; S01 is the sole 1.155×
   exception, already live) → loudness (-14 LUFS, LRA ~2–2.6).
2. Timings are extracted AFTER the speed pass — never before (a speed
   change moves every word).
3. SFX on every entrance AND exit; layered landings on card rows; accents
   on statement lines and number landings.
4. Bed: low cleared instrumental ~-28 dB under speech (built videos
   only; uploaded reels stay original-audio-only).

## Phone-speaker clarity
- EQ: gentle high-pass ~80 Hz (removes rumble), presence lift 2–4 kHz
  (+2 dB) so consonants survive a tiny speaker. Never boost the lows —
  phone speakers can't play them and they eat headroom.
- Sibilance: de-ess the voice (5–8 kHz) before the loudness pass; a
  harsh "s" at -14 LUFS is the most common "this sounds cheap" tell.
- Room tone: 0.5s of the room's own tone under every cut point — never
  digital silence between words (silence reads as a glitch on phones).
- Ducking: the bed ducks -6 dB under the voice, rides back up in gaps;
  the bed never competes with a word.

## Executable steps
1. Measure LUFS + LRA on the export (ffmpeg loudnorm); if it isn't
   ~-14 LUFS, the master is wrong — fix the master, never the post.
2. Listen on a phone speaker, not studio monitors, before delivery.
3. TTS segments: verify duration vs word count (~200 wpm at speed 110)
   and check the tail volume — truncated or looping TTS is caught here,
   not after posting (Oct 10 lesson).

## Worked example
Adilet's chain measured: ElevenLabs → cuts → speed → loudness, -14.19
LUFS on one reel, -14.16 on another. Same chain, same numbers, every
video — that is why his voice sounds the same everywhere.

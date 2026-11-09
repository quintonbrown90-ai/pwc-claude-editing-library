<!-- PART: audio-sound/audio-demucs-stems.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# AUDIO / SOUND — Demucs stem separation (LICENSE FLAG)

Source: Meta HT Demucs v4 (adefossez/demucs) via @kappa.ai DecYkDcI799 +
PART-DRAFTS-V6.md. SOTA-class public separation (~9.0–9.20 dB SDR).
CPU-OK from 3GB VRAM.

## LICENSE FLAG (SAFETY §7 — fold as workflow WITH the flag, never as fully commercial-clear)
Code is MIT, but the pretrained weights are NOT covered by MIT — the author
describes them as mainly research use (MUSDB terms; MIT label removed from
the HF model card). Commercial use needs confirmation. Separating a song
never transfers rights to the recording. Do not present Demucs output as
cleared audio; the INPUT must already be Q's own licensed audio.

## The rule
Split one track into vocals / drums / bass / other (+ 6-stem variant with
guitar/piano) so music and effects separate cleanly under voice.

## Executable steps
1. `pip install demucs`; `demucs --mp3 --mp3-bitrate 320 <track>` -> 4 stems.
2. Verify stems sum back to the mix before cutting.
3. Use on Q's videos: split a licensed bed to duck the vocal under voice,
   isolate drums for a beat-matched cut, pull a clean SFX layer out of a
   mixed track.

## Worked example (PWC)
Licensed hype bed has a vocal hook fighting Q's voiceover. Demucs splits it;
the vocal stem ducks -12 dB under speech, drums stay full for the cut grid.
The bed is still the same licensed track — no new rights created.

## PWC skin
Licensed library only in, licensed stems only out. Flag travels with the part.

## Canonical-decode confirmation (Nov 8, 2026)
Parent's canonical decode (`research/video-harvest/instagram/
kappa_ai_DecYkDcI799_DECODE.md`) CONFIRMS the role verbatim — "Demucs
separates the music from the effects" (transcript 26.8–29.5s) — arriving
with CLAP on the "+2 MORE" beat. No correction to the workflow above;
the LICENSE FLAG stands unchanged.

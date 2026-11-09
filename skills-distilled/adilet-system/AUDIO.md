# AUDIO — voice + chain (@adilet.fndr, Exhibit D decoded)

> **[MEASURED]** = from the hero reel's own Exhibit D cards, the audio
> itself, or loudnorm analysis. **[INFERRED]** = standard-practice
> reconstruction.

## The voice [MEASURED]

- A **synthetic male voice** (Instagram's own understanding describes it as
  such; it is the same voice on every video — the account has never used a
  human performance). Even, confident explainer delivery, mid-pitch, no
  room sound — a studio TTS voice, not a recording.
- His Exhibit D card names the source: **ElevenLabs**. [MEASURED — his own
  on-screen claim]
- The voice is the **master clock**: captions, scene beats and motion are
  all scheduled from the finished voice track's word timings
  (CAPTIONS.md). Nothing is timed to a script estimate.

## The chain [MEASURED — his Exhibit D, in his order]

His tape-machine graphic prints the chain literally:

**ELEVENLABS → CUTS → SPEED → LOUDNESS → MASTERED FOR INSTAGRAM**

1. **ElevenLabs** — raw TTS generation from the final script.
2. **Cuts** — dead air and gaps removed; the narration runs continuous
   (his pacing has no breathing holes: beats change every ~2–3s of
   *speech*, see PACING.md). [INFERRED mechanics: silence-trim + tight
   concatenation, the same through-edit rule PWC already uses]
3. **Speed** — a speed pass on the voice (his reels speak fast; catalog
   word rates are computed in PACING.md from the transcripts). The speed
   is applied to the *voice chain*, then timings are extracted from the
   result — captions never chase an un-sped estimate.
4. **Loudness** — mastered "for Instagram": measured values below.
5. **Mastered for Instagram** — the delivered file targets the platform's
   normalization so the reel plays at full perceived volume in-feed.

## Measured loudness [MEASURED — ffmpeg loudnorm analysis]

| File | Integrated | True peak | LRA |
|---|---|---|---|
| Hero DfXTzMZINjp | **−14.19 LUFS** | +0.52 dBTP | 2.0 |
| De_3hwXIBYi (14.6K likes) | **−14.16 LUFS** | −3.04 dBTP | 2.6 |

Two videos, one spec: he masters to **−14 LUFS integrated** (Instagram's
normalization point — the reel is neither turned down nor boosted in
feed), with a very flat loudness range (LRA ≈ 2–2.6 LU — the voice chain
is heavily compressed; there are no quiet moments). True peak is *not*
tightly controlled (−3.0 to +0.5 dBTP across the two samples) — loudness
first, peaks wherever they land.

PWC replication target: **−14 LUFS integrated** — but PWC's existing G4
gate (true peak ≤ −2 dBTP) stays; it costs nothing and is the stricter,
safer peak rule. Speech rate for reference: the hero speaks **226 words
in 63.4s ≈ 214 wpm** (faster-whisper count) — fast, dense narration is
part of the sound.

## PWC mapping

- PWC's locked avatar voice (George / Kokoro `bm_george`, native 1.11, in
  pwc-avatar-video VOICE.md) takes the ElevenLabs slot. The *chain order*
  is what transfers: **generate → cut dead air → final speed is native
  (never time-stretch a locked PWC voice — the "speed" slot is satisfied
  by the native 1.11 generation rate) → loudness gate → master**.
- Music/SFX: the hero is voice-forward with the chain shown above; any bed
  sits far under the voice. PWC's standing sound rules (accents on
  entrances/exits, transients density) apply from BRAND.md — they extend,
  not replace, this chain.

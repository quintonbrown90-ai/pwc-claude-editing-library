<!-- PART: audio-sound/audio-chain-adilet.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# AUDIO — the chain, measured (MEASURED)

Source: Adilet `skills/adilet-system/AUDIO.md` — his Exhibit D card names
the chain; loudness measured by ffmpeg loudnorm on two reels.

## The rule
Voice → cuts → speed → loudness → mastered for Instagram. The voice is the
master clock: captions, beats and motion are all scheduled from the
finished voice track's word timings.

## Executable steps
1. **ElevenLabs** (his source, on-screen claim) — raw TTS from the final
   script. PWC: Q's real voice for takes; locked PWC voice for avatars.
2. **Cuts** — dead air and gaps removed; narration runs continuous (no
   breathing holes; beats change every ~2–3s of speech).
3. **Speed** — a speed pass on the voice (his reels speak fast: median
   222 wpm). Timings are extracted AFTER the speed pass — captions never
   chase an un-sped estimate.
4. **Loudness** — mastered for Instagram: measured −14.19 / −14.16 LUFS,
   LRA ~2–2.6, on two reels. Target −14.2 LUFS.
5. Verify with loudnorm before delivery; the boosted version that clips
   (+0.56 dBTP) is never the shipped version.

## Worked example
Avatar voice track: ElevenLabs → silence-trim + tight concatenation →
speed to ~222 wpm → loudnorm to −14.2 LUFS. Word timings extracted from
the MASTERED track; captions land ON the word at +0.013s median.
## Self-learning — folded Nov 8, 2026 (research/knowledge/SELF-LEARNING.md)

- **SL-08** — Pauses removed: 13 gaps >0.33s → longest 0.28s; gap histogram is a QC metric. (2026-11-07, P1 re-cut)
- **SL-15** — Side angles = same performance — constant offsets fix sync; one master audio track, whole turns. (2026-11-06, hat talks v4)
- **SL-16** — Transcript spans amputate non-lexical intros ("ooowee") — scan head/tail/gaps for loud bursts first. (2026-11-06)
- **SL-17** — Phrase-level assembly double-counted a segment ("can you make this for us" ×2) — whole-segment partitioning + monotonic/non-overlap assertion. (2026-11-06, hat talks v3)
- **PB-04** — Two-cam fix: one master track, constant offsets (A 0.92–0.97, B 0.90–0.96), pauses excised, ooowee whole. (2026-11-06, hat talks v4)

## Variants (v9)
- **v9 · @?, V8-02:** V8-02 — Local pre-clean stack: Whisper + DeepFilterNet on-device before Claude → audio-chain-adilet.md _(source: v9_verification.md)_
- **v9 · @?, V8-175:** V8-175 — Transcribe first: AssemblyAI 1h → audio-chain-adilet.md _(source: v9_verification.md)_
- **v9 · @wassimyounes__, DYf-n9PguD5:** @wassimyounes__ DYf-n9PguD5 — 30ms audio fades at every cut (so you never hear a pop). DIFFERS: the 30ms parameter is new to the part. (Repo itself GATED behind comment VIDEO — not cloned, not scanned.) _(source: bulk-c VARIANTS.md)_

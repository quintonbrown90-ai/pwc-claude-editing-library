# Open-Source Caption & Timing Stack — Batch 37 (part #329)

Harvested Nov 12, 2026 (Q's Batch 37 order). Every item license-verified
permissive, quarantine-scanned, pooled at
`~/workspace/claude-editing/open-source-library/captions-timing/` (cards for
license-verified items whose clone is still owed live in `../cards/`).
Full tables: `research/batch-37-opensource-harvest/findings-captions-timing.md`.

## The stack, by job

**Caption generation**
- **dynamic-captions** (reedodev, MIT) — Claude Code skill: word-timed
  captions, face/safe-area avoidance, beat pulse, SRT/VTT/karaoke-ASS export.
  INSTALLED Code-side as `dynamic-captions`. Skin PWC teal/gold-on-navy.
- **Capite** (MIT) — self-hosted caption studio: faster-whisper timing +
  pysubs2 karaoke ASS, 27 motion presets, click-a-word transcript editor.
- **pycaps** (MIT, ecosystems pool) — animated word-level captions as a
  Python library. NOT CapCut tooling despite the name.
- **pysubs2** (MIT) — the ASS/SSA/SRT/WebVTT read/write engine under all of it.

**Timing truth (fix drift at the source)**
- **stable-ts** (MIT) — forced-aligns a KNOWN script to audio at word level.
  Rule: scripted lanes (avatar, Yapping, Sky scripted takes) align the script;
  never trust raw ASR timing for captions.
- **ffsubsync** (MIT) — rescues drifted/translated SRTs by re-syncing to audio.

**Beat grid (Q's everything-on-beat law)**
- **Beat This!** (CPJKU, MIT — code AND weights) — SOTA beat/downbeat
  tracking; the only permissive SOTA option.
- **all-in-one** (MIT) — beats + music-structure labels (intro/verse/chorus)
  for section-aware cutting.
- **librosa** (ISC) — fallback + feature layer (onset, chroma, MFCC).

**Cut maps & gates**
- **PySceneDetect** (BSD-3) — canonical scene-cut detection; **TransNetV2**
  (MIT) for dissolves it misses. Feed /watch reports + freeze/transition QC.
- **Silero VAD** (MIT) — speech/silence boundaries for the dead-air gate.
- **inaSpeechSegmenter** (MIT) — speech/music/noise zones (bed vs talk maps).
- **SpeechBrain** (Apache-2.0) — ECAPA diarization with public weights,
  NO HuggingFace gate (Q+Kiya / interview cuts).

## Traps — parked, do not install

- **whisper-timestamped is AGPL-3.0** (commonly mislabelled MIT) — parked.
- **pyannote** diarization: MIT code but HF-gated weights + token — parked;
  SpeechBrain + Silero is the ungated route.
- **aubio** GPL-3 · **madmom** NC weights · **Essentia** AGPL+NC ·
  **TempoCNN** AGPL — all parked; Beat This! replaces the whole class.

Already owned (not new): WhisperX (BSD-2), faster-whisper, video-use,
earshot (part #328), ffmpeg-skill, Nelson embedded-captions.

# Open-Source Sound Stack — Batch 37 (part #331)

Harvested Nov 12, 2026 (Q's Batch 37 order). Code MIT/Apache/BSD/ISC/CC0;
sounds CC0 or CC-BY only (attribution logged). Pooled at
`~/workspace/claude-editing/open-source-library/sound/` + `../cards/`.
Full tables: `research/batch-37-opensource-harvest/findings-sound.md`.
Layers onto what Q already owns: Earshot (part #328, 252-sound bank),
real-sound skill, the ~1,250-file licensed library, ElevenLabs SFX (paid route).

## SFX / music — zero-attribution first

- **Wyzowl SFX Kit** (CC0, card — download owed) — 320 code-synthesised WAVs
  (48kHz/24-bit) WITH machine-readable cue data: what each sound is, when to
  use/not use, duration, sync point, level. Built for AI placement; merge
  toward Earshot's bank / real-sound sourcing.
- **Kenney packs** (CC0; Interface, Impact, UI Audio, Music Jingles, RPG,
  Digital, Sci-fi, Casino) — card, download owed. In-pack License.txt: credit
  "would be nice but is not mandatory."
- **kmilo93sd/agent-video-editor library** (CC0, card) — 113 SFX (−22 LUFS) +
  15 music tracks (−16 LUFS), per-file license record in its LICENSES.md.
- **Juhani Junkala 512 SFX** (CC0, card) — 8-bit/retro accents, meme beats only.
- **Incompetech / Kevin MacLeod** (CC-BY 4.0, card) — background beds ONLY
  where a description credit is acceptable. Exact credit per track:
  `[Track Title]` / `Kevin MacLeod (incompetech.com)` / `Licensed under
  Creative Commons: By Attribution 4.0` / `https://creativecommons.org/licenses/by/4.0/`.
  Download per track at use time; never bulk-scrape.

## Sourcing layer (search, don't stockpile)

- **Openverse API** (code MIT; content per-item) — keyless meta-search over
  ~5.2M CC audio files; filter `license=cc0` or commercial CC-BY and use the
  API's per-item attribution string verbatim. Wire into real-sound TODAY.
  (This was the missing third of the dhaibuilds EARS trio — Earshot +
  real-sound already owned.)
- **freesound-python** (MIT client, pooled) — ⚠️ **needs Q to apply for the
  free Freesound API key** (freesound.org/apiv2/apply). Policy when used:
  filter CC0 or CC-BY ONLY, never CC-BY-NC; credit per API response; note
  UPF's case-by-case commercial-API term.

## Engines under the existing audio skills

- **pyloudnorm** (MIT) — BS.1770 loudness: measure + normalise to −14 LUFS in
  the render-QC gate of every lane. `pip install pyloudnorm` at use.
- **DeepFilterNet** (MIT/Apache-2.0, card) — `deep-filter` CLI, CPU-only
  speech enhancement; THE standard talking-head cleanup step.
- **noisereduce** (MIT, pooled) — spectral-gating fallback, pure Python.
- **Demucs** (MIT, pooled) + **python-audio-separator** (MIT, card) — stem
  splits / music-bed rescue. ⚠️ Pin **Demucs/MDX models only** — some
  RoFormer checkpoints carry no published license.

## Parked

Pedalboard GPL-3 · Matchering GPL-3 · AudioSmith AGPL-3 (wraps Demucs+DFN —
use them directly) · Stable Audio weights (Stability Community License,
gated, revenue-capped) · AudioCraft/AudioGen weights **CC-BY-NC** ·
Sonniss GDC bundle (custom license: usable inside finished videos, but no
redistribution and no AI/ML use — cannot enter the CC bank; Q's call if he
wants it as a use-only source).

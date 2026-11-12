# Batch 37 — Open-Source Editing Harvest: Master Index (part #333)

Q's order, Nov 12, 2026: grab every open source that helps premium editing
and put it in every Claude Code style folder + the web side. This part is the
map; the distilled domain parts are #329 (captions/timing), #330
(motion/transitions/color/cleanup), #331 (sound), #332 (editor ecosystems).

## Where everything lives

- **General pool:** `~/workspace/claude-editing/open-source-library/` —
  `INDEX.md` is the master table (name, license, what it does, which styles
  received it, pooled path or card). 39 repos pooled locally (~380 MB) +
  license-verified cards for items whose clone is still owed (VM network
  disconnects — re-clone before install, verdicts stand).
- **Code side:** 5 skill installs added to `~/.claude/skills/` (480 → 485):
  `dynamic-captions`, `text-to-lottie`, `eva-video-style`,
  `hyperframes-motion-reel-skill`, `facecammaxxing`.
- **Per style:** a "Batch 37 — Open-Source Additions" section in each style's
  `skills-plugins-githubs.md` (Devin / CCC / Yapping; Viral folder created at
  `styles/viral-edit-style/`). General additions route through the pool INDEX.
- **Sky:** NOT touched (Batch 36 owns the sky rebuild). Sky-applicable finds
  are staged at `open-source-library/sky-staging/MANIFEST.md` for Batch 36 /
  Muse to fold — incl. the rembg model pin and the CapCut draft trio.
- **Web side:** per-style addition zips staged at
  `~/workspace/claude-editing/batch-37-web-zips/` (Devin / CCC / Viral /
  Yapping / general) for Muse (parent) to upload + verify LIVE/ON.
- **Findings (full evidence):**
  `research/batch-37-opensource-harvest/findings-*.md` (4 domain files) +
  quarantine clones under `research/batch-37-opensource-harvest/quarantine/`.

## Harvest totals

59 NEW cleared (13 captions/timing · 18 motion/color · 12 sound · 16
ecosystems) · ~23 already-owned groups re-verified, not re-reported ·
~39 PARKED with reasons (AGPL/GPL/NC/no-LICENSE/gated/service-locked).
Knowledge finds folded to CCC/general: **screenwriting-skills** (MIT, 26
dramaturgy skills from 47 craft books) + **reelbench-skills** (Apache-2.0,
AI-video learning notes) — pooled under ecosystems/.

## Category coverage

visuals ✓ (PixiJS Filters, SwinIR, slay LUTs, facecammaxxing) · motions ✓
(Revideo, Anime.js, Lottie, RIFE) · sounds ✓ (Wyzowl/Kenney CC0, DFN,
pyloudnorm, Openverse) · transitions ✓ (gl-transitions 214 + xfade-easing) ·
elements ✓ (Lottie assets, CapCut draft layer) · timings ✓ (Beat This!,
stable-ts, Silero, scene detection) · understanding ✓ (screenwriting,
reelbench, inaSpeechSegmenter, SpeechBrain) · creation ✓ (Editly, Capite,
chengfeng, Revideo, draft APIs).

## Needs Q's call (listed, never installed)

1. **Freesound API key** — free, Q applies at freesound.org/apiv2/apply;
   unlocks freesound-python (MIT, pooled) with a CC0/CC-BY-only filter.
2. **Sonniss GDC bundle** — usable inside finished videos under its own
   license, but not CC: can't enter the bank or be redistributed.
3. **GPL tooling** (Pedalboard, Gyroflow, RVM) — parked under the
   permissive-only rule; revisit only if Q accepts use-not-distribute GPL.
Everything else actionable was integrated without a decision.

# Open-Source Motion, Transitions, Color & Cleanup Stack — Batch 37 (part #330)

Harvested Nov 12, 2026 (Q's Batch 37 order). License-verified permissive,
quarantine-scanned, pooled at
`~/workspace/claude-editing/open-source-library/motion-color/`.
Full tables: `research/batch-37-opensource-harvest/findings-motion-color.md`.

## Transitions — the named catalog

- **gl-transitions** (MIT; 214 shaders verified per-file: 212 MIT + 1 BSD-2 +
  1 BSD-3) — GLSL transition collection with ffmpeg/WebGL/Remotion ports.
  Rule: pick transitions BY NAME from this catalog; stock xfade alone is the
  cheap tell.
- **xfade-easing** (MIT, card — clone owed) — Penner/CSS easings + 40+ ported
  gl-transitions on stock ffmpeg, no custom build.
- **Editly** (MIT) — declarative ffmpeg editor (JSON spec) whose transition
  layer is gl-transitions; fast assemblies for Yapping/general.

## Motion engines

- **Revideo** (MIT) — Motion Canvas fork, headless render API. The permissive
  code-renderer; removes Remotion's company-license question from code lanes.
- **Anime.js v4** (MIT) — timelines, stagger, springs, elastic easings for the
  HyperFrames/HTML motion layer.
- **text-to-lottie / diffusionstudio lottie** (MIT) — agent-generated Lottie
  icons/loaders/stings; INSTALLED Code-side as `text-to-lottie`.
- **PixiJS Filters** (MIT) — ~40 GPU filters (glitch, RGB-split, glow, CRT,
  shockwave) complementing pixelfx (pixel-art) and Vibha fx.py (face-tracked).

## Matting & cleanup — with the one hard pin

- **BiRefNet** (MIT code + weights) — hair-edge cutouts (Q PiP, boards, covers).
- **rembg** (MIT code) — ⚠️ **PIN `-m birefnet-general` ONLY.** The default
  `bria-rmbg` model is **CC-BY-NC** — never on Q's monetized work. Local
  models only; its in-tree cloud sessions stay disabled.
- **SAM 2** (Apache-2.0 incl. checkpoints, card — clone owed) — prompt-once
  tracked masks: blur-law patches, tracked callouts.
- **IOPaint** (Apache-2.0; repo archived Aug 2025 — pin the version) — LaMa
  inpainting erases junk from proof frames; uniquely best permissive eraser.

## Source-rescue chain (fixes the 720×1280 chat-transcode problem)

**SwinIR** (Apache-2.0, denoise/de-JPEG/deblur) → **Real-ESRGAN** (BSD-3,
2–4× upscale) → **Practical-RIFE** (MIT, true slow-mo / frame-rate conform).
Code pooled; weights are license-clean (noted per repo) and download separately.

## Color finish

- **lutgen-rs** (MIT) — generates .cube LUTs from a reference palette: bake
  the PWC teal/gold-on-navy house LUT once, finish every lane with it.
- **slay LUTs** (CC-BY-4.0) — 5 cinematic starter .cubes. **Attribution:
  credit "slay — slaycamera.com" wherever the pack is listed/redistributed.**

## Parked (substitutes above)

RobustVideoMatting GPL-3 · Gyroflow GPL-3 · video2x AGPL-3 · CoTracker
CC-BY-NC weights · BRIA RMBG-2.0 CC-BY-NC+gated · ProPainter S-Lab NC ·
Theatre.js Studio AGPL · GSAP library custom Webflow license (the owned GSAP
*skill* stands; new code work uses Anime.js/Revideo) · OpenMontage AGPL-3
(re-confirmed). Honest gap: no permissive title/lower-third ASSET pack exists —
lower-thirds stay code-built (HyperFrames/Revideo templates).

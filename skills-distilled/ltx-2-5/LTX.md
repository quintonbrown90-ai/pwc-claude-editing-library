# LTX 2.5 — verified knowledge (primary sources, Nov 20, 2026)

Sources: Lightricks/LTX-2 GitHub repo (10.3K stars) + README, Hugging Face
Lightricks/LTX-2.5 model repo (2.96M downloads), Freefield's measured app table.
Reel DeyMp0wu1Gx's claims were checked against these before being written here.

## What it is
- LTX-2 is, in Lightricks' words, "the first DiT-based audio-video foundation model"
  with synchronized audio and video in one model. LTX 2.5 is the current release.
- The reel's claims, verified: runs locally on your own computer ✓ · completely free
  (open weights; you pay only for compute) ✓ · text-to-video from one prompt ✓ ·
  image-to-video ✓ · **synchronized audio generated in the same pass** (dialogue, SFX,
  ambience — there is a dedicated audio VAE and the HF tags include text-to-audio /
  audio-to-video) ✓ · up to **UHD 4K** ✓ (3840×2176; defaults are 1024×1536 @24fps) ·
  "no more paying for Higgsfield" = positioning, true only where a GPU is available.
- Character consistency across shots: via image-to-video conditioning + IC-LoRA
  control adapters (the documented mechanism) — you anchor each shot to the same
  reference image. It is NOT a one-prompt "same character guaranteed" magic switch;
  the reel compresses this. Freefield ships LTX-2.5 IC-LoRA apps: dub, genjutsu,
  reframe, sdr-hdr, mixed-media.

## License (the split matters)
- **Code: Apache-2.0** (the LTX-2 repo).
- **Model weights: LTX-2.x Community License** (LICENSE-2_x in the repo; HF license
  field "other"). Free to use incl. commercial under that license's conditions —
  READ IT before a paid brand deliverable ships. The Gemma 3 text encoder downloads
  separately under Google's license.

## Pipelines (from the repo)
- **DistilledPipeline** — the fast starting point, lowest VRAM.
- **DFR (Diffusion Fidelity Rendering)** — production quality: same distilled
  transformer + detailing IC-LoRA, generated keyframes, spatial detailing pass,
  optional 2x/4x fps. Slower, more VRAM.
- **A2VidPipelineTwoStage** — audio-to-video: generates video conditioned on an
  input audio file (the lip-sync-adjacent route).
- Native HDR/EXR support in standard pipelines.

## Hardware / VRAM
- Needs an NVIDIA-class GPU machine. No official single VRAM number; measured via
  Freefield's lab table: most LTX-2.5 apps fit a 24GB card; the flagship Cinema
  Studio video app (LTX-2.5 i2v + 33 camera moves + sound) **peaks at 44.3GB** —
  48GB-class card or Modal for that one. Distilled route is the low-VRAM entry.
- **Muse's VM cannot run it** (no GPU, ~8GB shared RAM) — same wall as Freefield
  and MuseTalk. Routes: Q's own GPU machine, RunPod/Vast hourly, or Modal
  (Freefield documents all three; its cloud pack default is 64 apps / 22.9GB models).

## Run routes
1. **Official**: Lightricks/LTX-2 repo pipelines (Apache-2.0 code) or the official
   ComfyUI nodes / LTX Desktop app (Lightricks/LTX-Desktop, 2.3K stars).
2. **Freefield** (already grabbed: ~/workspace/free-tools-grab/repos/freefield, MIT):
   120-app Higgsfield-style studio on ComfyUI, LTX-2.5 at its core — incl. the
   **`dub` app** (audio-driven talking avatar / lip-sync on LTX-2.5 IC-LoRA),
   Cinema Studio image/video, face-swap, recast, relight. Models download from HF
   per app; every app.json lists its models + licenses.
3. Console playground exists (console.ltx.video) — hosted, not the local route.

## Role in our stack
- **Higgsfield-credit relief valve**: local/free generation for avatar-series beats,
  B-roll and experiments once a GPU route is in play; Higgsfield's remaining ~13
  credits stay reserved for hero beats Q approves.
- **Lip-sync candidate**: Freefield `dub` / A2Vid are the LTX routes to the
  mouth-motion law (Muse seen talking = mouth moves, synced). MuseTalk is the
  other candidate (built + staged in ~/workspace/lipsync-test/, blocked only on
  GPU/RAM). Whichever produces the first test clip gets judged against the law
  before becoming the talking-beat engine.
- Faith/brand rules still bind: Christian hip-hop or clean instrumentals under
  Muse segments; generated audio dialogue must match the approved script lines —
  never let the model improvise Q's or Muse's words.

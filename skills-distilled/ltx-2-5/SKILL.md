---
name: ltx-2-5
description: "LTX 2.5 (Lightricks) — the open-weights audio+video generation model in Q's stack: text-to-video and image-to-video WITH synchronized audio generated in the same pass, up to UHD 4K, free to run locally on a GPU machine. Reach for this skill whenever a job wants local/free video generation as Higgsfield credits run out, an LTX pipeline (distilled / DFR / A2Vid / IC-LoRA), the Freefield studio apps built on LTX-2.5 (incl. its dub lip-sync app), or a character-consistent multi-shot workflow via image conditioning. Verified facts, license, VRAM and run routes are in LTX.md. It CANNOT run on Muse's VM (no GPU) — it needs Q's GPU machine or an hourly GPU rental."
---

# LTX 2.5 — free local video generation (with sound)

LTX 2.5 is Lightricks' open-weights audio-video foundation model, in the stack as the
**free local video-generation path** now that Higgsfield runs on credits (~13 left):
generate video on a GPU we control instead of paying per generation, and use its
audio-conditioned / IC-LoRA routes (incl. Freefield's `dub`) for lip-sync work.

Full verified knowledge — capabilities, license split (Apache-2.0 code / LTX-2.x
Community License weights), hardware + VRAM, pipelines, run routes, and the honest
limits: **LTX.md**.

Hard constraints:
- **Never on Muse's VM** — no GPU, 8GB shared RAM; the same wall as Freefield/MuseTalk.
  Routes: Q's GPU machine, or an hourly rental (RunPod/Vast/Modal).
- Check the **LTX-2.x Community License** terms before paid brand work ships — the
  weights are NOT Apache, only the code is.
- Output quality on Q's stylized avatar (Face A) is unproven until a test clip is
  judged — same gate as every generation route.

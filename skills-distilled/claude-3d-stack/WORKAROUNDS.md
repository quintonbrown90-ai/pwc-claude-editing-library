# Workarounds — free / open routes around every wall in the 3D stack
Added Nov 18, 2026 (Q: "there's always work arounds and free outsources and repos"). Every repo below was located and license-checked the same day. The license gate still rules: permissive (MIT / Apache-2.0) = usable; custom or missing license = PARKED.

## Wall 1 — Hunyuan3D is parked (photo → 3D)
Use a permissive image-to-3D model instead:
- **TRELLIS** — microsoft/TRELLIS (**MIT**, ~14.3K stars). Image → structured 3D (Gaussian + mesh) with materials. The strongest Hunyuan replacement.
- **TRELLIS.2** — microsoft/TRELLIS.2 (**MIT**). Newer generation, higher fidelity (1536-res reports on 16GB GPUs).
- **TripoSR** — VAST-AI-Research/TripoSR (**MIT**, ~7.4K stars). Single image → mesh in seconds; lower fidelity — use for fast drafts/blocking.
- **InstantMesh** — TencentARC/InstantMesh (**Apache-2.0**, ~4.6K stars). Sparse-view large-reconstruction mesh generation.
Pipeline shape stays the same: photo → (TRELLIS.2) → mesh → UniRig/SkinTokens rig → Blender animate → dream-loop critic.

## Wall 2 — Lip-sync talking (the avatar series' core blocker)
- **LatentSync** — bytedance/LatentSync (**Apache-2.0**, ~6.3K stars). Diffusion lip-sync, current quality leader of the open set. GPU-heavy (1.6 wants ~18GB VRAM; 1.5 is lighter). ComfyUI wrapper exists (ShmuelRonen/ComfyUI-LatentSyncWrapper).
- **MuseTalk** — TMElyralab/MuseTalk (**MIT code**, ~7.0K stars). Real-time latent-inpainting lip-sync, lighter than LatentSync. **Weights: verify terms at download** (the LICENSE file covers code + lists component licenses; treat the model files like UniRig's — check before use).
- **PARKED:** Wav2Lip (Rudrabha/Wav2Lip — no LICENSE file in repo; research/non-commercial in practice). SadTalker (OpenTalker/SadTalker — custom Tencent license text; parked until a full read says otherwise).
- Honest quality note: all of these were trained mostly on real faces. On a 3D-styled character the mouth region usually still reads, but **nothing ships without a one-clip test judged against Q's mouth-motion law** (mouth visibly forming the words, in sync). First test: one Face A plate + the S01 voice line, one clip, judge, then decide.

## Wall 3 — No Blender/GPU machine
- **Free GPU notebooks:** Google Colab free tier (T4) and Kaggle Notebooks (free GPU hours weekly) both run TRELLIS / TripoSR / MuseTalk-class workloads and Blender headless. HuggingFace Spaces host ready demos of several of these models (incl. ZeroGPU for signed-in users) — zero install for a first test.
- **Blender on CPU:** Blender installs on plain Linux and renders headless (Eevee/Cycles on CPU — slow, but real). Fine for stills, simple scenes and rig tests; not for long animation renders.
- **ComfyUI as the front-end:** wrappers exist for UniRig, TripoSR, LatentSync and MuseTalk — one free UI driving the whole chain on whatever GPU is available.
- Rule: a workaround route gets **tested on one asset** and the result filed here before it becomes the standing route.

## Wall 4 — Rigging, one step newer
- **SkinTokens** — VAST-AI-Research/SkinTokens (**MIT**). UniRig's successor from the same lab (unified skeleton + skinning, claims 98–133% better skinning accuracy). Prefer it over UniRig for new rigging installs; UniRig stays the documented fallback.

## What did NOT change
- Hunyuan3D 2.1 stays parked — the workaround is replacement, not permission.
- Face A + hat law + identity gates bind every output of every route above.
- "Free" routes have rate/session limits; production volume may still need a real GPU box — that call is Q's, made with a test result in hand.

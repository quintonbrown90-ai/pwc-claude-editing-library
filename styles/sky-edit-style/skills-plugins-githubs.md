# skills-plugins-githubs — everything this style actually uses

**Rule:** public / open-license only. Gated/paywalled = GAP entry only, never chased, never
faked. Licenses are stated only where verified on disk or in the source docs; anything else
is marked LICENSE UNVERIFIED — do not claim it.

## 1. Skills (local — Q's own codifications, no third-party code)

| Skill | What it does in this style | Location | License / status |
|---|---|---|---|
| `realskytan-system` | THE source skill for this folder: 13 forms, D1–D14 devices, E1–E10 recipe, PWC overrides. This folder is its standalone, self-contained repackaging. | `~/workspace/claude-editing/skills/realskytan-system/SKILL.md` (single file); also inside `pwc-creator-systems.zip` as `pwc-creator-systems/sky.md` (verified in zip listing Nov 9, 2026) | Q's own codification; no third-party code. Live in Claude as part of pwc-creator-systems (not as a standalone `pwc-sky-editor` skill — no zip by that name exists in `~/workspace/claude-editing/zips/`) |
| `capcut` | CapCut Desktop automation + timeline direction — the build route for every device (native text/shapes/masks/keyframes) | `~/workspace/custom-skills/capcut/SKILL.md` | Local custom skill |
| `capcut_native_export_verification` | Proves an edit was built/exported from a real CapCut project and plays correctly on the exported file | `~/workspace/custom-skills/capcut_native_export_verification/SKILL.md` | Local custom skill |
| `final_video_motion_and_source_verification` | Freeze / board-transition / dead-air / replacement-take verification on the exported file | `~/workspace/custom-skills/final_video_motion_and_source_verification/SKILL.md` | Local custom skill |
| `reference_style_recreation` | Recreate a supplied reference style on Q's footage with a frame-matched fidelity grade | `~/workspace/custom-skills/reference_style_recreation/SKILL.md` | Local custom skill |
| `delegated_render_export_verification` | Verify a render built by another agent/editor against script, storyboard and source proof | `~/workspace/custom-skills/delegated_render_export_verification/SKILL.md` | Local custom skill |
| `pwc-designed-captions` | Designed-caption pipeline (6 styles) — Sky lane uses the bare-text D1 variant only | `~/workspace/custom-skills/pwc-designed-captions/` | Local custom skill |
| `pwc-motion-playbooks` | Motion + easing playbooks (incl. verified easings: overshoot peak 1.141; spring stiffness 170, damping 16) | `~/workspace/custom-skills/pwc-motion-playbooks/` | Local custom skill |
| `pwc-design-system` | PWC design system / brand DNA (palette, logo, safe zone) | `~/workspace/custom-skills/pwc-design-system/` | Local custom skill |
| `pwc-animations` | PWC animation library | `~/workspace/custom-skills/pwc-animations/` | Local custom skill |

## 2. Plugins / registries

| Item | What it does in this style | Install / upload path | License |
|---|---|---|---|
| `find-skills` (vercel-labs/skills) | Finds every other skill (incl. video-editing skills) — used to locate CapCut/editing capabilities before a build | `npx skills add vercel-labs/skills --skill find-skills -a claude-code` (per Nov 8 order; staged as `find-skills.zip` in Wave 12, uploaded live) | **MIT — SCAN PASS** (verified live Nov 8, 2026). Safety gate: it finds + presents options, Q approves, dual-model review before any install — never auto-install |
| HyperFrames registry | Moving components for Sky devices (named in SKY_STYLE.md family section: "HyperFrames registry for moving components") | Check the registry before use; no install step verified for this style | **LICENSE UNVERIFIED — do not claim.** Verify license + SCAN PASS before first use in a build |

## 3. GitHub repos / code

| Repo / code | What it does in this style | License |
|---|---|---|
| Robust Video Matting (RVM) — `rvm_mobilenetv3_fp32.onnx` from the RVM GitHub release | Behind-the-head person matte for the PWC depth layer (back graphics behind Q, cut-out on top) | **MIT** (per SKY_STYLE.md §8) |
| faster-whisper | Word-level transcripts already on disk (`examples/reels/transcript_*.json`, base.en) — used to PRODUCE the decodes, not shipped as style code | LICENSE UNVERIFIED in this folder's sources — transcripts only; re-check before re-running |
| ffmpeg / ffprobe | QC tooling only (`code/qc_freezedetect.sh`, decode checks). Not shipped as style code | System tooling; see ffmpeg.org for its licensing (LGPL/GPL components) |

## 4. What this style does NOT use
- No third-party Sky template pack, no paid CapCut template, no scraped Sky project file —
  none exists on disk, and none was chased. Devices are rebuilt as CapCut-native drafts from
  the measured specs in `STYLE-GRAMMAR.md`.
- No Epidemic Sound (declined by Q Nov 3, 2026 — never purchase, never re-offer). Sound source:
  the local licensed library (~1,250 files).
- No paywalled/gated material of any kind (see `GAPS.md` G-17).

## 5. Upload path for THIS folder
- Zip: `~/workspace/claude-editing/styles/zips/sky-edit-style.zip` (staged Nov 9, 2026 — NOT
  uploaded to Claude; do NOT claim live until verified ON in the Skills list).
- Existing Claude-side Sky material (for the uploader's reference): `pwc-creator-systems.zip`
  (contains `pwc-creator-systems/sky.md`) and `pwc-design-system-v10.zip` (contains SKY-SCORE
  device score card). This zip is a standalone repackaging, not a replacement for those.

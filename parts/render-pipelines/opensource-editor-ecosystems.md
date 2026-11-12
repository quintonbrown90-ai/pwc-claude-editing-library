# Open-Source Editor Ecosystems & CapCut Tooling — Batch 37 (part #332)

Harvested Nov 12, 2026 (Q's Batch 37 order). Screened all 473 repos in
zhuyansen/awesome-claude-video-skills (429 never downloaded by prior sweeps)
+ nishaj0/claude-for-everything Video/Audio + fresh CapCut/Remotion/Revideo
searches. License-verified permissive, pooled at
`~/workspace/claude-editing/open-source-library/ecosystems/`.
Full tables: `research/batch-37-opensource-harvest/findings-ecosystems.md`.
License files were READ, not just API labels — that caught facecammaxxing
(API: NOASSERTION → file: MIT) and vex (→ PolyForm NC, parked).

## CapCut draft layer (Sky finishing stays CapCut-native)

- **pyJianYingDraft** (Apache-2.0, NOTICE) — Python library generating
  CapCut/JianYing draft files; the draft-writing layer. Pooled.
- **capcut-mate** (Apache-2.0, NOTICE) — self-hosted draft automation APIs +
  agent skills. **Draft APIs ONLY — its cloud-render path must NEVER be used
  (Q: local render only).**
- **video-recap-skills / zenstory** (MIT) — long video → narrated recap cuts
  with one-click editable CapCut/JianYing draft export. Keep local paths;
  its optional remote TTS/vision calls stay off.
- Already owned: **capcut-cli** (MIT), **VectCutAPI** (Apache — in library;
  Q decided Nov 11: **do NOT install** — do not re-litigate).

## Code-render ecosystems

- **Revideo** (MIT) + **Motion Canvas** (MIT, upstream — dormant; Revideo is
  the adopted fork) — transitions/motion as code, local render. See part #330.
- **Remotion caveat:** template repos **remotion-cuongit-template** (MIT) and
  **Remotion Motion Graphics Skills** (MIT — kinetic text, diagrams, camera
  moves) are cleared, but the RENDER step runs Remotion core, whose own
  company license applies. When license-clean matters end-to-end, render in
  Revideo instead.
- **HyperFrames Motion Reel Skill** (MIT) — one-line theme → beat-synced
  HyperFrames piece; INSTALLED Code-side.
- **chengfeng-videocut-skills** (Apache-2.0) — word-level locate/trim agent
  plugin; pooled. Its separate Runtime/Studio needs its OWN vet before use.

## Talking-head effect skills (installed Code-side)

- **facecammaxxing** (MIT) — text-behind-head, 3D card rings, tier lists,
  kinetic captions over a clean cut. INSTALLED.
- **eva-video-style** (MIT) — talking-head templates + cinematic effects +
  animated captions with built-in QC. INSTALLED.
- **claude-code-video-toolkit** (MIT, secondary, card) — full agent video
  workspace; deprioritized (overlaps owned super-video-maker/story-studio;
  generation steps call paid model APIs per run).

## Parked highlights (17 total — full list in findings)

OpenChatCut AGPL · pireel AGPL (re-confirmed) · **oh-my-cassette** — MIT code
but hosted-account/cloud-only → service-locked, parked · **vex** PolyForm NC ·
Remotion core (special company license — templates above are the workaround,
Revideo the clean route) · 7× no-LICENSE · 1× CC BY-NC · 1× FSL.

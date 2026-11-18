# The 3D Stack — full decode and verification (Nov 18, 2026)

Source reel: https://www.instagram.com/reel/Dfw9Qr7xfS0/ — @morenicksaraev, posted Nov 15, 2026, 31s, 1,571 likes / 134 comments at decode. Presenter's claim: "5 AI tools that make 3D stupid simple" — Claude builds, rigs and animates 3D models. Each tool below was located at its real repo and license-checked on Nov 18, 2026.

## 1. Blender MCP — ahujasid/mcp-for-blender
- What: MCP server + Blender addon. Claude gets tools to create/modify objects, materials, scenes and run Blender Python. Prompt in, scene built.
- Repo: https://github.com/ahujasid/mcp-for-blender (~34.9K stars, updated daily). Formerly `blender-mcp`; PyPI package renamed `mcp-for-blender`, old `uvx blender-mcp` invocations keep working.
- License: **MIT** ✓
- Install: Blender + uv; one-command setup from the repo (installs addon + writes client MCP configs), or manual MCP config with command `uvx mcp-for-blender`; inside Blender, enable the addon and start its socket server.

## 2. Blender Skills — arjun988/blender-skills
- What: 94 agent skills (v1.3.0) covering modeling, UVs, PBR materials, rigging/animation, archviz, worlds, art styles, genre direction — the knowledge layer that stops the agent guessing; executes through Blender MCP.
- Repo: https://github.com/arjun988/blender-skills (~4.2K stars). Skills live in `.claude/skills/`.
- License: **MIT** ✓ (LICENSE verified in repo)
- Install: clone, copy `.claude/skills/*` into the target project's `.claude/skills/`. Works with Claude Code, Cursor, Kiro, Codex.
- Vendored copy in this library: `skills-distilled/blender-skills-pack/` (95 folders incl. pack root files, 4.2MB, with upstream LICENSE).

## 3. Hunyuan3D 2.1 — Tencent-Hunyuan/Hunyuan3D-2.1 — PARKED
- What: single photo → high-fidelity 3D mesh with production-ready PBR materials.
- Repo: https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1 (~4.5K stars).
- License: **Tencent Hunyuan 3D 2.1 Community License** — custom, territory-limited (expressly does not apply in EU/UK/South Korea), not a standard permissive license. **Fails the license gate: do not install, do not use, do not route assets through it.** Status changes only on Q's explicit approval of that license.

## 4. UniRig — VAST-AI-Research/UniRig
- What: unified auto-rigging (SIGGRAPH 2025, TOG). Predicts a skeleton for diverse meshes and computes skinning weights — output is animation-ready in Blender.
- Repo: https://github.com/VAST-AI-Research/UniRig (~2.2K stars). Paper: arXiv 2504.12451. Weights: HuggingFace `VAST-AI/UniRig` (verify the weights' own terms at download time; code license does not automatically cover weights).
- License: **MIT** (code) ✓
- Note: the lab's successor **SkinTokens** claims large skinning/bone accuracy gains — evaluate it first for any new rigging install.
- Needs: PyTorch + a real GPU for practical inference.

## 5. dream-loop — achimala/dream-loop
- What: an agent skill, not a model. Loop: generate a target screenshot of the desired result → build toward it (Blender/Three.js/etc.) → a separate subagent critic diffs live renders against the target → iterate until the critic passes; optionally re-dream a better target. Author-tested with Codex; Claude-class models expected to work.
- Repo: https://github.com/achimala/dream-loop (~2.4K stars). Install: `npx skills add achimala/dream-loop` or clone into the skills directory.
- License: **MIT** ✓
- Vendored copy in this library: `skills-distilled/dream-loop/` (SKILL.md + scripts + references + LICENSE; demo media excluded).
- Prerequisites: image generation, vision input, subagents. Blender optional via MCP/scripting (preferred over computer use).

## What this stack does NOT do
- No lip-sync. Rigging animates bodies; faces forming words need a dedicated lip-sync layer (the avatar series' open blocker stays open — this stack is a motion/scenes route, not a talking route).
- No free compute. Blender rendering + UniRig inference want a GPU machine; neither Muse's VM nor Claude's cloud session boxes have Blender installed.
- Hunyuan's photo→3D shortcut is off-limits under the license gate; the permissive replacements (TRELLIS/TRELLIS.2, TripoSR, InstantMesh), the open lip-sync candidates (LatentSync, MuseTalk), and the free-compute routes are verified and written up in WORKAROUNDS.md (Nov 18, 2026).

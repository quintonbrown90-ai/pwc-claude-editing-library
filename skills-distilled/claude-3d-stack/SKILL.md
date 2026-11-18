---
name: claude-3d-stack
description: "The 3D build/rig/animate stack for Claude: Blender MCP (drive Blender from Claude), Blender Skills (94 pro workflows), UniRig (auto-rig any mesh), dream-loop (render-critic loop), plus Hunyuan3D 2.1 (photo-to-3D, PARKED — Tencent license). Use when a task needs 3D scenes, models, rigs, or animation built by Claude — product scenes, 3D devices/exhibits for edits, character motion experiments. Carries exact install steps, license verdicts, and the PWC application map with honest limits (needs a Blender + GPU machine; does NOT solve lip-sync)."
---

# Claude 3D Stack

Source: @morenicksaraev reel Dfw9Qr7xfS0 (Nov 15, 2026), "Five AI tools that let Claude build, rig and animate 3D models." Decoded, license-checked and installed Nov 18, 2026. Full detail: STACK.md in this folder.

## The stack (pipeline order)

1. **Blender MCP** — ahujasid/mcp-for-blender (MIT, ~35K stars). Claude drives Blender directly: describe a scene in words, Claude builds/manipulates it via MCP tools. PyPI package is now `mcp-for-blender` (`uvx blender-mcp` still works). One-command setup installs the Blender addon + client configs.
2. **Blender Skills** — arjun988/blender-skills (MIT, v1.3.0). 94 specialist skills (modeling, UV, PBR materials, rigging, animation, worlds, styles) the agent follows step by step instead of guessing. Vendored in this library at `skills-distilled/blender-skills-pack/` — copy its `.claude/skills/*` into the working project's `.claude/skills/`. Built to execute through Blender MCP.
3. **UniRig** — VAST-AI-Research/UniRig (MIT code, SIGGRAPH 2025). One model auto-rigs diverse meshes: skeleton + skinning, animation-ready. Weights on HuggingFace (VAST-AI/UniRig) — check weight terms at download time. Successor: SkinTokens (same lab) — evaluate before new installs.
4. **dream-loop** — achimala/dream-loop (MIT). The QC pattern: (a) generate a target image of the finished look, (b) build toward it, (c) a separate subagent critic compares live renders to the target and sends fixes, (d) loop until the critic passes it. Vendored at `skills-distilled/dream-loop/`. Needs image generation + vision + subagents.
5. **Hunyuan3D 2.1** — Tencent-Hunyuan/Hunyuan3D-2.1. Photo → high-fidelity 3D asset with PBR materials. **PARKED — DO NOT INSTALL OR USE.** Its Tencent Hunyuan 3D Community License is territory-limited and non-standard; it fails the permissive-only license gate. Revisit only if Q explicitly approves that license.

## Install (on the machine that will run Blender)

- Install Blender (blender.org) and Python `uv`.
- Blender MCP: run the repo's one-command setup, or configure the MCP server manually: `uvx mcp-for-blender` as the MCP command in Claude Code's MCP config; install the bundled addon inside Blender and start its server from the Blender sidebar.
- Blender Skills: copy the vendored pack's `.claude/skills/*` into the project's `.claude/skills/` (or clone arjun988/blender-skills fresh).
- UniRig: clone VAST-AI-Research/UniRig, follow its README (PyTorch + GPU); rigs export for Blender.
- dream-loop: copy `skills-distilled/dream-loop/` into the project's skills and invoke per its SKILL.md.

## PWC application map (read before promising anything)

- **Good for:** 3D product/scene builds, animated 3D devices and exhibits for edits, environment plates, and character-motion EXPERIMENTS (a rigged character can be posed/animated in Blender and rendered).
- **Hard limits:** (1) Nothing here runs without a Blender + GPU machine — Muse's VM and Claude's cloud boxes do not have Blender installed; the stack installs where the work will run. (2) Rigging + animation is BODY motion. **Lip-sync talking is not solved by this stack** — a rigged face still needs a lip-sync driver (separate problem, separate tool). Never present a rigged render as talking footage. (3) Any character built here must still pass Q's identity laws (Face A, hat law, no goggles) and the dream-loop critic gate before it ships anywhere near Q's content.
- **QC doctrine:** dream-loop's critic loop is the same shape as Q's standing rule — nothing ships on the builder's say-so. Run the critic against reference frames, not vibes.

## Sources

Intake decode + per-tool verification: SOURCES.md in this folder; research copies in Muse's workspace research-3d/.

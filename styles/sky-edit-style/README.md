# sky-edit-style — edit exactly like @realskytan

**Profile:** Sky Tan — @realskytan — https://www.instagram.com/realskytan
**Trigger phrase:** "edit in Sky style"
**Status: UNGRADED.** No Sky-style test edit has been frame-sequence graded against the
examples here yet (`QC.md` §6). Do not present any build from this folder as "exact" until
that grade passes. See `GAPS.md` for everything that cannot be reproduced exactly.

## What's in this folder

| File / dir | What it is |
|---|---|
| `SKILL.md` | The Claude skill: trigger, when to use / NOT use, families, E1–E10 recipe, D1–D14 devices, PWC law, carousel authority, QC summary |
| `STYLE-GRAMMAR.md` | Measured specs with VERIFIED / [EST] / UNVERIFIED tags: captions, colours, devices, motion constants, pacing, sound, hooks, proof, endings, carousels |
| `examples/` | `MANIFEST.md` (inventory + exact on-disk paths/sizes/durations/frame counts) + full text decodes: 14 per-reel notes + 14 word transcripts + motion teardown + carousel breakdown + verified record + priority-15 breakdown + 113-post form catalogue + SKY-SCORE + source skill |
| `code/` | CapCut-native build spec + plan generator + QC scripts — see `code/README.md` for what is CapCut-native vs ffmpeg-only. PLUS the Claude Code executable build (Nov 9, 2026): plan generator, D1–D56 device registry, palette/easing, HyperFrames emitter (primary render path — verified with a real 1080×1920 MP4 render), CapCut sequence emitter, QC (gates P1–P10), 88 unit tests — installed in Claude Code as the `sky` skill (`~/.claude/skills/sky` → this folder). The generic-fallback module (`code/sky_option2.py`) was DELETED in the SKY v6 premium purge (Batch 36) — premium Sky is the only output mode |
| `code/MEASUREMENTS_2026-11-09.md` | Frame measurements from the Nov 9 session (D12/D5/DfX2/DfQ4) + HyperFrames render-verification findings |
| `skills-plugins-githubs.md` | Every skill, plugin, and GitHub repo this style actually uses, with licenses (MIT/Apache only where verified; UNVERIFIED marked, never claimed) |
| `ASSETS.md` + `assets/` | Q/Muse assets only: PWC logo (`assets/pwc_logo.jpg`, copied from `~/workspace/pwc-content-calendar-build/assets/pwc_logo.jpg`), PWC colours, asset-pool rule — PLUS the SKY01 design components (pill/card/line/bar PNGs) and pop/whoosh SFX, copied from `sky01_web_assets/` (see `ASSETS.md` §5) |
| `GAPS.md` | Honest list of what CANNOT be reproduced exactly, and why (18 gaps) |
| `QC.md` | How to prove a test edit matches: frame-sequence motion grade, freezedetect, ±0.15 s entrance/exit audits, last-voice→end-card, lip-sync, retention read |
| `SOURCES.md` | Provenance for every fact: source, original path, what was copied |
| `zips/sky-edit-style.zip` | Staged skill zip (in `~/workspace/claude-editing/styles/zips/`) — NOT uploaded to Claude; not live until verified ON in the Skills list |

## The style in one paragraph
One named framework per video that fills in on screen. Word-by-word white captions (1–3
words, hard-cut in ≤1 frame, out ≈0.5 s), glass panels, charts and devices timed to the spoken word, one
accent per video (GREEN→PWC teal for numbers/systems, ORANGE→PWC gold for beliefs/story),
graphic swaps ≈ every 10 s, mild zoom (5–10% max), mostly one continuous take, dry voice in
Sky's own reels (Q's lane adds a cleared bed ≈ −28 dB + SFX on every landing/exit), most
reels end with no CTA card (Q adds the completed device + door + logo moment ≤1 s after the
last word). Carousels are always Sky's form — this folder is the carousel authority too.

**PREMIUM SKY IS THE ONLY OUTPUT MODE (SKY v6, Batch 36 — supersedes the Nov 9
"two options" note):** the 15 generic/anti-slop patterns are REMOVED (`code/sky_option2.py`
deleted) and listed as BANNED TELLTALES in `SKILL.md`, enforced by `validate_premium_plan`.

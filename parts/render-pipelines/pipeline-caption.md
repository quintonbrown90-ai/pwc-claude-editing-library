<!-- PART: render-pipelines/pipeline-caption.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# PIPELINE — designed captions, end to end (PUBLISHED)

Source: `skills/pwc-designed-captions/` — code/ pipeline + PROMPTS.md P1.

## The rule
Transcribe → track matte → plan (SHOW it first) → render → composite → QC.
The plan is judged before anything renders.

## Executable steps
1. `code/transcribe_align.py` — word timings (script.txt is ground truth
   if present).
2. `code/track_matte.py` — facetrack.json AND fg_alpha.mp4 (rembg
   u2net_human_seg on hero windows only).
3. `code/plan_captions.py` — SHOW the plan summary (event count per style)
   before rendering. Flag hero treatments within 15s of each other and any
   box the safe-zone clamp had to move.
4. `code/render_captions.py` + `code/composite.py` — both layers, every
   motion named from MOTION.md.
5. QC per `pipeline-qc-gates.md` in this category.

## Worked example
DEMO A (delivered Nov 5): "4 Content Types", 72 caption events, 4
HERO_BEHIND words, front captions yield during hero windows.
## Self-learning — folded Nov 8, 2026 (research/knowledge/SELF-LEARNING.md)

- **SL-28** — Render-path verification (Viashaan QC, Nov 5; code fixed Nov 8): `plan_captions.py` hero rule misfired BIG_CAPS (word-index vs seconds units bug) — fixed, verified 18→2 BIG_CAPS on a 72-event test plan. Before any demo/delivery, verify the plan's style counts (BIG_CAPS ≈ once per section, never 3 same-style events running), verify injected data not sample data on frame QC, and ffprobe the export for limited-range yuv420p.

## Variants (v9)
- **v9 · @mattphxm, DbZyaHNFUUf:** **V92 — @mattphxm Local Editor (DbZyaHNFUUf):** "Every silence longer than half a second, gone." (→ pipeline-deadair-gate — DISCREPANCY: Q's floor is 0.35s, his is 0.5s; recorded as observed, not reconciled); "the takes where you start again, it keeps the clean one" (→ pipeline-qc-gates); "reads back what I said and re-orders these sentences so that it's the tightest version" (→ pipeline-caption); "I don't have to open a single time line." The Local Editor tool itself: GAP (free, no login, but not in the harvest — license unknown, never installed). _(source: bulk-b VARIANTS.md)_

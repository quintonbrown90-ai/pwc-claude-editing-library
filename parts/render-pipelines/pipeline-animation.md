<!-- PART: render-pipelines/pipeline-animation.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# PIPELINE — animation render (PUBLISHED)

Source: `skills/pwc-animations/` — render_animation.js (Playwright setT
frame-stepper → alpha WebM) + 6 single-file HTML templates + STYLE_FILE.md.

## The rule
One prompt per animation style. The template + STYLE_FILE tokens build it;
the renderer steps frames and captures alpha WebM. Same templates, same
setT contract, every time.

## Executable steps
1. Pick the style prompt from `skills/pwc-animations/PROMPTS.md`
   (/stat-chart, /map-route, /headline, /teardown, /paper-desk, /ink-wash).
2. Swap the bracketed words; build from the bundled template + STYLE_FILE
   tokens. Every motion named from MOTION.md.
3. Render 3.2–3.8s at 30fps alpha WebM with render_animation.js.
4. Composite over the footage; verify the alpha channel survived (this
   VM's capture silently loses alpha — composite from the templates' PNG
   frame sequences if the WebM comes back opaque).
5. QC per `pipeline-qc-gates.md` in this category.

## Worked example
DEMO B (delivered Nov 5): value-equation take, TEARDOWN 5.78s, STAT-CHART
28.44s, HEADLINE 56.90s. Caught in QC: first build rendered sample data
(window.DATA injection failure) — fixed before delivery.
## Self-learning — folded Nov 8, 2026 (research/knowledge/SELF-LEARNING.md)

- **PB-05** — Hero-behind-head done right: 4 genuine hero moments, front-caption yield, inserts on the word, zero freezes. (2026-11-05, Viashaan demos)
- **SL-28** — Render-path verification (Viashaan QC, Nov 5; code fixed Nov 8): teardown side tags clipped off-canvas — fixed, notes now live inside each layer row (name left, note right), verified 0 off-canvas at full spread. Before any demo/delivery, verify alpha survived (composite from PNG frame sequences if the WebM comes back opaque), verify injected data not sample data (`window.DATA` via `addInitScript` pre-load only — a post-load assignment is ignored), and ffprobe the export for limited-range yuv420p.


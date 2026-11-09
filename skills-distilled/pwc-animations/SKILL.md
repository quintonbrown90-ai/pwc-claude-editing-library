---
name: pwc-animations
description: Single-prompt animated inserts for Paid With Content edits — BOTH lanes (Q's real talking-head videos AND the Claude avatar videos). Six working HTML animation styles (stat-chart, map-route, headline, teardown, paper-desk, ink-wash) built and rendered with Claude Code, timed to the spoken line. Use when an edit needs an animated chart, map, newspaper headline, exploded breakdown, desk notes, or reflective scene — or when asked to "animate" a number, journey, claim, or process.
---

# PWC Animations — one prompt per style, both lanes

Rebuilt from @viashaan's ANIMATE system ("Comment ANIMATE and I'll send you
every prompt… Each one is a single prompt"). His six usable styles, rebuilt
as working templates in the PWC brand, with the render driver included.
Loads alongside pwc-video-editors, pwc-avatar-video, or
pwc-designed-captions; brand and workflow law live in pwc-design-system.

## The six styles

| Style | Use it when he says… | Main motion | Default |
|---|---|---|---|
| stat-chart | a number, growth, money math | line EASE IN-OUT, count STEPS+EASE OUT, dot OVERSHOOT | 3.2s |
| map-route | a journey, moved, from X to Y | route EASE IN-OUT, pin OVERSHOOT | 3.4s |
| headline | a claim that should read as news/fact | lines EASE OUT stagger, body STEPS | 3.6s |
| teardown | the parts of a thing/process (anatomy of…) | layers EASE OUT, labels SPRING | 3.8s |
| paper-desk | notes, rules, remember-this beats | papers OVERSHOOT, writing STEPS | 4.0s |
| ink-wash | faith / reset / reflective beat | everything slow EASE IN-OUT | 4.5s |

## How a build runs

1. Pick the style from the spoken line (table above). If none fits, that's a
   /animate job (PROMPTS.md) — build the new style INTO the system, never a
   one-off floating in a project folder.
2. Fill the template's DATA contract (each template's header comment lists
   its fields) — or paste the style's prompt from PROMPTS.md and swap the
   bracketed words.
3. Render: `node render_animation.js templates/<style>.html --data data.json
   --duration <s> --out <name>.webm` — deterministic setT frame capture,
   alpha WebM out (overlay-ready). `--mp4` for a baked-background version.
4. Composite as an INSERT: enters on the exact noun/number, main move done
   inside the spoken phrase, exit EASE IN 5–6 frames or hold under speech.
   In the avatar lane, the insert follows the lane's illustration rules
   (said-vs-shown: if he names it, show it happening).

## Rules

- STYLE_FILE.md tokens only — colors, fonts, card language. NO RED.
- REAL data only: a stat-chart shows the real number from the script/proof,
  never an invented growth curve presented as fact. Illustrative shapes are
  fine; fabricated proof is not.
- Every motion named from MOTION.md in the plan/prompt. Timing-to-speech per
  STYLE_FILE.md. One animation at a time on screen; never stack two inserts.
- New styles get registered in the design system's COMPONENTS.md so the next
  editor (human or AI) reuses them instead of rebuilding.

## Files

- templates/ — the six single-file HTML animations (window.DATA contract,
  window.setT deterministic render, @font-face bundled fonts)
- render_animation.js — Playwright frame-stepper → alpha WebM / MP4
- PROMPTS.md — one paste-ready prompt per style + the /animate meta-prompt
- STYLE_FILE.md — the shared brand tokens every animation reads
- MOTION.md — the shared motion vocabulary + PWC house numbers
- fonts/ — Anton, Poppins ExtraBold(+Italic), Playfair Bold Italic,
  Bebas Neue, Caveat Bold

Dependencies: node + playwright (+ chromium), ffmpeg. If Playwright capture
is unavailable in the environment, the same templates render through
HyperFrames (seek-and-capture on the same window.setT contract) — the
invariant either way: a frame is a pure function of time; renderers seek,
they don't play.

<!-- PART: render-pipelines/hyperframes-clock-ban-check.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# RENDER-PIPELINES — HyperFrames: the clock is banned + check before render (Tier S)

Source: "Claude Code Can Make Videos Now, 70k Stars on GitHub"
(https://www.youtube.com/watch?v=74ld-5v0c7A) + HyperFrames — "HyperFrames
Setup Guide 2026" (https://www.youtube.com/watch?v=uKnJGspGguI). INFERRED
reconstruction from the visible rules; no files downloaded. Knowledge entries
V8-157, V8-158. HyperFrames is already in Q's stack (5 skills).

## The rule
The clock is banned. No `Date.now()`, no real-clock reads; every animation is
a pure function of frame time. A render that reads the clock is
non-deterministic — same prompt, different video. And nothing renders before
the check passes: lint + validate + inspect, zero errors.

## Executable steps
1. **Clock ban, verbatim.** Add to any HyperFrames skill prompt: no
   `Date.now()`, no real-clock reads, every animation a pure function of
   frame time. This is the single most important HyperFrames rule — it
   prevents silent failures where the same build renders differently twice.
2. **Flipbook render model.** Headless Chrome seeks each frame's exact time,
   screenshots, FFmpeg encodes. Slow machine = slower render, never dropped
   frames. This is why HyperFrames is deterministic where screen-recording
   is not.
3. **Pipeline: Node 22 + FFmpeg 7 + agent → init → prompt → preview → check
   → render.** `npx skills add heygen-com/hyperframes` (5 skills) →
   `npx hyperframes init my-video` (starter picker, 6 files) →
   `/hyperframes` prompt → `npx hyperframes preview` → `npx hyperframes
   check` → `npx hyperframes render`. A 5s clip renders in ~6s; frames step
   deterministically.
4. **Check before render: lint + validate + inspect.** Lint catches missing
   data attributes; validate runs WCAG contrast in headless Chrome; inspect
   checks layout overflow. Zero errors = good to render.
5. **Hello World first prompt.** The plugin guide's first prompt is exactly
   a 5-second title card; use it as the smoke test for every new HyperFrames
   install.
6. **Agent loop: write → self-check → fix → preview-approval → render.**
   The preview-approval gate matches Q's pilot-gate discipline — nothing
   renders before a human approves the preview.
7. **Iterate by talking; the studio reloads on save.** No build step, no
   rebuild loop — "Make the title bigger and add a subtitle" → agent
   rewrites index.html, studio reloads. Skills auto-load so the agent knows
   the patterns before you type.
8. **HeyGen media-funnel flag — NOT adopted.** Voiceover / music / stock
   inside HyperFrames defaults to HeyGen; for Q's lane, local free options
   must be installed explicitly or the skill fails loudly. Do NOT install the
   HeyGen CLI without Q's word. [NEEDS Q'S WORD]

## Worked example (PWC)
Q's cover card: Hello World smoke test (5s title card, teal/gold/navy) →
`check` passes lint/validate/inspect → render. A proof board re-render
reuses the same project; the clock ban means the re-render is
frame-identical except for the changed number. Keyword WAITLIST.

## Human-made check
`check` returns zero errors before any render, and the rendered frames are
spot-checked against the preview — same frames, same timing, every time.

## PWC skin
Teal #14A886 + gold #FEE238 on navy #00214E. NO RED. WCAG contrast validate
runs against the PWC palette, never a default palette.

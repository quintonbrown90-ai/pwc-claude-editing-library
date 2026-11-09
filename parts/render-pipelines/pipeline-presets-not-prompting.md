<!-- PART: render-pipelines/pipeline-presets-not-prompting.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# RENDER-PIPELINES — presets, not prompting + recursive self-review (PUBLISHED)

Source: Jason Cooperson — youtube.com/watch?v=7MaARoS9o2s
(CLAUDE-CODE-WORKFLOWS.md §17–18). Measured cost in his run: 2h42m + 740K
context for a 13-min talking-head video; run overnight.

## The rule
Claude lacks the creativity/taste/workflow knowledge to invent a good edit
end-to-end. The fix is a PRESETS folder — every animation custom-built and
custom-tuned by a human (grade, text animation, zoom in/out, pop-in,
rise-in, light/dark backgrounds, graphic rules + when to create graphics,
SFX rules) — "lock it in so that it doesn't have to think about how to do
the zoom in, the pop-ins, or the rise in." Otherwise the output is "AI
generic slop." Two loops run BEFORE a human ever sees the cut: (1) rough-cut
loop — sub-agents loop over the WhisperX rough cut "to make sure that the
rough cut is actually good before we move on"; (2) graphics loop — graphics
plan skill → graphics build skill → edit review skill, looping "back and
forth to get rid of all those defects and all those errors before it even
comes time for us to review it."

## Executable steps
1. Human-tune ONE preset per motion (zoom-in, pop-in, rise-in, text
   animation, grade, SFX rule) and save each with exact parameter values.
2. Put them in a `presets/` folder with a `lanes/` folder (CapCut / Premiere
   / Resolve — Premiere + Resolve best functioning; CapCut lane is Q's).
3. Prompt Claude to PICK presets, never invent motion: "Use only the presets
   in presets/. Do not invent new animations."
4. Run autonomous with "Don't stop until you're finished" — overnight.
5. Review loops: after the rough cut, sub-agents re-check against the brief
   and fix defects; do not show the cut until the loop passes. After
   graphics, plan → build → edit-review in a loop until zero defects.
6. Then SFX (which sound at which point) → music bed → human review →
   render with the default preset.
7. Scope: best for talking-head educational; vlogs/visual harder; vertical
   presets are a separate build.

## Worked example (PWC)
Q's preset folder = the 8 named motions + the PWC card family + the SFX
rules, each with exact values. Claude picks "OVERSHOOT 0.3s" for the title,
"count-up STEPS+EASE OUT" for the number — never invents a new entrance.

## PWC skin
Presets are Q's motions, Q's palette, Q's devices. A preset that puts
anything over his face is not a preset — it is a bug.

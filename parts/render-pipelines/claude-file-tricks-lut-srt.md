<!-- PART: render-pipelines/claude-file-tricks-lut-srt.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# RENDER-PIPELINES — Claude file tricks: .cube LUT + SRT count-up + transparent overlays (Matt Loui / Sanji Nai-Chien, Tier S)

Source: Matt Loui — "Claude + CapCut Completely Changes Everything For
Editors" (https://www.youtube.com/watch?v=8oIFBQ9BhVU) + Sanji Nai-Chien —
"Forget After Effects: Claude + CapCut Is the Only Editing Stack You Need"
(https://www.youtube.com/watch?v=j4FzO2fF1kg). INFERRED reconstruction from
the visible prompts; no files downloaded. Knowledge entries V8-125, V8-126,
V8-127, V8-128, V8-129, V8-173. The LUT and SRT tricks need no plugin and no
paid tool — free Claude chat + CapCut free tier.

## The rule
When Claude can't render the thing, have Claude generate the FILE and let
CapCut play it. A LUT is a grade in a text file; an SRT is an animation in a
text file; a transparent render is an overlay in a video file.

## Executable steps
1. **.cube LUT from a text prompt.** "Clean, soft pastel LUT… cinematic,
   and clean" → lifted shadows, teal+peach split toning, reduced saturation,
   low contrast. Apply in CapCut at 50% opacity. Iterate by naming what to
   remove ("without the teal"). The LUT is the whole grade in one small file.
   PWC version: one house LUT (teal/gold on navy grade) generated once,
   reused across Claude renders — worth one test render before adopting.
2. **Count-up numbers via SRT.** Claude generates an .SRT of $0→$535 (or
   $0→$600) at 0.1s each; CapCut compound-clip + 10× speed + hold on the
   final number. The subtitle file IS the animation. The MrBeast dollar-spin,
   built from a text file, in ~2 minutes vs ~1 hour by hand. Hold the final
   number by extending the last subtitle layer.
3. **Transparent-background render for overlays.** "Make the background
   transparent, don't have any transparency on the actual pills" — the exact
   instruction that turns a Remotion graphic into a CapCut overlay. Without
   it the graphic arrives on a solid box.
4. **SVG rule for graphics.** Ask for icons / illustrations / diagrams in
   SVG: scales to any size without going blurry, recolor by hand, Claude can
   animate them. Every graphic editable and animatable.
5. **Remotion in Claude Code, not regular chat.** `npx create-video@latest`;
   references + manipulations in Claude Code. Preview in browser; tweak in
   plain language ("3× faster" → 5 seconds). Parallel builds run
   simultaneously.
6. **End every prompt with the clarifying-questions closer.** "Ask me any
   clarifying questions so that we nail this spot on." Claude asks, you
   answer, then it builds. The questions ARE the spec.
7. **Numerical tweaks, not adjectives.** "10% larger", "3× faster",
   "saturate 50% more" — numbers beat adjectives for revision rounds. Fix by
   naming the defect ("looks staggered or choppy — make it smooth").

## Worked example (PWC)
Q's payout proof: Claude writes the SRT ($0→$28,800, 0.1s steps) + the house
.cube LUT + a transparent-background gold pill graphic → CapCut compound-clip
at 10×, LUT at 50%, pill over the proof. No re-render when the number
changes — regenerate the SRT. Keyword WAITLIST.

## Human-made check
The count-up lands on the spoken number, holds long enough to read, and the
LUT never pushes skin tones off or introduces red. The file tricks are
invisible — the viewer sees a grade and a number, not a trick.

## PWC skin
House LUT in teal #14A886 + gold #FEE238 on navy #00214E. NO RED. Count-ups
in gold on navy; pills transparent-background only, never a solid box.

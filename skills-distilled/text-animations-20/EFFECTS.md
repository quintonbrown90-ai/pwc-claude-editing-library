# EFFECTS — the 20, decoded from the reference (Df6S-2Dqgk_)

Conventions: times are the reference's own pacing at demo scale (~1.5s per effect).
`accent` = PWC gold #FEE238 by default (teal #14A886 as secondary). Easing names are
CSS/cubic-bezier equivalents. "Lands" = the settled end state the effect holds.

## 1. Typewriter — slug `typewriter`
What moves: characters appear one at a time, left to right; a solid accent caret bar
rides the insertion point and blinks when typing pauses/ends. The line stays centered
and re-centers as it grows.
Timing: ~55ms per character, linear steps, no easing. Caret blink 530ms steps(1).
Lands: full text + blinking caret for ~0.4s, then caret fades.
Spec: JS typer (text-animations.js); caret = accent bar 0.09em wide, full cap height.

## 2. Fade Up — slug `fade-up`
What moves: the whole word rises ~0.35em while fading 0→1; as it settles, an accent
underline draws in left→right beneath it.
Timing: rise+fade 0.5s cubic-bezier(.22,.8,.32,1); underline 0.3s ease-out starting at 70%.
Lands: word at full opacity, underline at full width (2-3px, accent).

## 3. Blur In — slug `blur-in`
What moves: nothing translates — the word starts as a heavy gaussian ghost
(blur ~20px, opacity ~0.25) and focus-pulls to crisp.
Timing: 0.8s ease-out, blur and opacity on the same curve.
Lands: perfectly sharp, full opacity. (A focus pull, not a fade.)

## 4. Tracking Expand — slug `tracking-expand`
What moves: letter-spacing opens from ~0 to ~0.45em; opacity 0.55→1 alongside; an accent
underline grows from the center out to match the final tracked width.
Timing: 0.9s cubic-bezier(.16,.84,.3,1). Underline tracks the same progress.
Lands: wide-tracked word, full width underline.

## 5. Marker Highlight — slug `marker-highlight`
What moves: the word sits plain; an accent marker band sweeps left→right BEHIND the
glyphs — slightly skewed (~-1.5°), edges a touch rough, overshooting the word by ~0.12em
on both ends; band height ≈ cap height + 0.18em padding.
Timing: sweep 0.45s cubic-bezier(.6,.02,.3,1) (fast middle, soft ends).
Lands: word sitting on the full marker band. Text color flips dark if the band is light.

## 6. Word Stagger — slug `word-stagger`
What moves: words arrive one at a time left→right, each fading 0→1 with a ~0.12em rise;
the FINAL word gets the punch: a dark pill wipes in behind it and its text flips to accent.
Timing: 0.18s stagger per word, each word 0.3s ease-out; pill wipe 0.25s.
Lands: full line readable, last word boxed accent-on-dark.

## 7. Number Count Up — slug `number-count-up`
What moves: the number counts 0 → target with a hard ease-out (fast start, long
decelerating tail); thousands separators format live; a small muted label sits static
under it; at the settle, an optional suffix (+, %, K…) pops in accent with a 1.25→1 punch.
Timing: 1.2s cubic-bezier(.12,.72,.08,1) on the value. Suffix pop 0.18s at 95%.
Lands: exact target value, suffix in accent.

## 8. Scramble Decode — slug `scramble-decode`
What moves: every glyph starts as a random character (A-Z, 0-9, symbols) in neutral
white/grey, re-rolling ~every 45ms; glyphs lock to the real letter left→right, and each
locked letter flips to accent as it settles.
Timing: full resolve ~0.9s for a 6-letter word (~0.13s per lock step).
Lands: the true word, fully accent. (Locked-prefix + rolling-tail structure.)

## 9. RGB Glitch — slug `rgb-glitch`
What moves: the word rests CLEAN; 2-3 short glitch bursts fire at irregular intervals —
RGB channel split (cyan/red ghosts offset ±3-6px), 1-2 thin horizontal slices jump
sideways, occasional accent pixel blocks. Each burst ≤80ms, then snap back to clean.
Timing: bursts at ~15% and ~55% of the hold, steps(1) hard cuts, no easing.
Lands: clean word. Punctuation, never constant jitter. (In PWC work the channel ghosts
read cyan/red on the reference; keep offsets small and bursts rare over footage.)

## 10. Letter Flip — slug `letter-flip`
What moves: letters flip in one at a time left→right on the X axis (split-flap style):
each rotates rotateX(-92°)→0 with perspective, invisible edge-on, face landing flat.
Timing: per letter 0.35s cubic-bezier(.3,.7,.3,1.15) (slight overshoot), stagger 0.09s.
Lands: full word flat and still.

## 11. Sine Wave — slug `sine-wave`
What moves: AMBIENT loop — each letter rides a traveling sine: translateY =
sin(phase + i×0.55) × 0.18em, phase advancing ~1 cycle per 1.2s; letters tint accent as
the crest passes over them, back to base in the trough.
Timing: continuous, linear phase advance; per-letter color follows the same sine.
Lands: never lands — it loops until cut. Use for held words, not entrances.

## 12. Split Reveal — slug `split-reveal`
What moves: the word is sliced at mid-height; top half slides up ~0.26em, bottom half
slides down ~0.26em, opening a seam; a small accent pill label pops into the seam
(scale 0.6→1, back-out) carrying the revealed tag/word.
Timing: split 0.45s cubic-bezier(.7,0,.2,1); pill pop at 60%, 0.25s.
Lands: halves held apart, pill seated in the gap.

## 13. 3D Extrude — slug `3d-extrude`
What moves: flat accent text; a hard extruded edge grows diagonally down-right behind
the face (stacked offset copies in a darker shade of the accent), depth building
0 → ~0.09em until the letters sit on a solid block edge.
Timing: depth growth 0.6s ease-out; face static throughout.
Lands: static 3D lockup — bright face, dark extrude, no blur (hard shadow, not drop shadow).

## 14. Liquid Fill — slug `liquid-fill`
What moves: the word starts as thin outline only (stroke, transparent fill); a solid
fill rises INSIDE each glyph bottom→top behind a slightly wavy surface line; letters
fill one at a time left→right.
Timing: per letter 0.25s ease-in-out, stagger 0.08s; surface wobble ±0.02em while rising.
Lands: fully solid word, outline gone (or kept at 1px in the fill color).

## 15. Decode Marker — slug `decode-marker`
What moves: TWO effects chained — glyphs scramble-decode (as #8, ~0.7s, dark text on a
light/accent field); the moment the word resolves, a dark marker band sweeps behind it
left→right (0.35s) and the text inside flips to accent-on-dark (the inverse of #5).
Timing: decode 0.7s, band sweep starts at ~85% of decode.
Lands: accent word seated on a dark band.

## 16. Blur Bounce — slug `blur-bounce`
What moves: letters drop in one at a time from ~0.55em above, each arriving with motion
blur (~8px vertical) that sharpens as it lands; each letter bounce-settles (overshoot
~0.06em, one rebound); letters may alternate accent/base coloring.
Timing: per letter 0.45s cubic-bezier(.28,.84,.42,1) bounce, stagger 0.07s.
Lands: full word sharp, baseline level.

## 17. Zoom Shake — slug `zoom-shake`
What moves: the word SLAMS in from ~3× scale, heavily blurred, snapping to 1× sharp in
~0.18s; on impact a hard shake fires (2-3 position jitters ±4-6px, decaying, ~0.25s) and
a thin ring shockwave expands from the word's center, fading out (~0.5s).
Timing: slam cubic-bezier(.16,.84,.3,1); shake steps are linear keyframe jitters.
Lands: word at 1×, dead still, ring gone. The loudest entrance in the set — use sparingly.

## 18. Strike Rotate — slug `strike-rotate`
What moves: word A rests in muted grey; an accent strikethrough draws through it
left→right (0.3s); then A rotates ~-6° while rising and fading out, and word B (accent)
rotates in from +6° below into the exact same slot.
Timing: strike 0.3s ease-in-out; swap 0.45s cubic-bezier(.6,.05,.3,1), B delayed 0.08s
behind A's exit.
Lands: word B only, level, accent. A is gone (struck + discarded).

## 19. Rise Squiggle — slug `rise-squiggle`
What moves: the word rises into place behind a baseline mask — letters slide up from
below the line, slight stagger, soft ease; once seated, an accent hand-drawn squiggle
(wavy underline) draws itself left→right beneath the word (stroke draw-on).
Timing: rise 0.4s cubic-bezier(.22,.8,.32,1), stagger 0.03s; squiggle 0.5s ease-in-out
starting at 60%.
Lands: word seated, full squiggle under it.

## 20. Outline Extrude — slug `outline-extrude`
What moves: the word starts as a faint thin outline (stroke only, ~35% opacity, no
fill); the outline brightens to full accent; then the fill floods in to solid accent
while a soft extruded depth grows behind down-right (~0.07em, darker shade) — #13's
extrude arriving through an outline state.
Timing: outline brighten 0.35s; fill+depth 0.55s ease-out.
Lands: solid accent word with outline pop and shallow 3D depth.

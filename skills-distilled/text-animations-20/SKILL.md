---
name: text-animations-20
description: "Callout catalog of 20 named text animations decoded frame-by-frame from the '20 Text Animations' reference reel (Df6S-2Dqgk_). When Q, a script, or a brief calls an effect BY NAME — typewriter, fade up, blur in, tracking expand, marker highlight, word stagger, number count up, scramble decode, RGB glitch, letter flip, sine wave, split reveal, 3D extrude, liquid fill, decode marker, blur bounce, zoom shake, strike rotate, rise squiggle, outline extrude — execute THAT animation with the timing, easing and landing in EFFECTS.md, using the implementation in text-animations.css / text-animations.js. Built for Q's planned callout video (he says each name on camera; the effect demonstrates itself on cue, one at a time) and for any edit that names one of the 20."
---

# 20 Text Animations — callout catalog

Source: reference reel Df6S-2Dqgk_ ("20 Text Animations", 32s), studied frame-by-frame
(6fps strips per effect + word-level transcript). Every breakdown in EFFECTS.md is what
the reference actually does — what moves, how fast, how it lands — not a guess from the name.

## How a callout fires
- A callout is the effect's NAME, spoken or written: "marker highlight", "zoom shake", …
- Execute exactly that one effect, on the cued text, at the cued moment. One callout =
  one effect, one at a time — never blend two unless the script names both.
- In the HTML/HyperFrames render stack: load `text-animations.css` + `text-animations.js`,
  then either set `data-fx="<slug>"` on the text element or call
  `TextFX.run('<slug>', element, opts)`. Slugs are the kebab-case names in EFFECTS.md.
- In other stacks (CapCut, ffmpeg, PIL): reproduce the EFFECTS.md breakdown — the motion,
  timing and landing are the spec; the CSS/JS is the reference implementation.

## Defaults (PWC brand swap)
- The reference's lime accent maps to **PWC gold #FEE238**; secondary accent **teal #14A886**;
  stage **navy #00214E**; text white. NO red anywhere (PWC rule).
- Font: the stack's headline font (Archivo Black / the video's display font).
- Durations are per-effect in EFFECTS.md; they are tuned for a ~1.5s demo beat and scale
  with text length where the breakdown says so.
- Safe zone + nothing-over-face rules from the edit system still bind when these are
  placed inside Q's videos.

## The 20 (exact names, video order)
1 Typewriter · 2 Fade Up · 3 Blur In · 4 Tracking Expand · 5 Marker Highlight ·
6 Word Stagger · 7 Number Count Up · 8 Scramble Decode · 9 RGB Glitch · 10 Letter Flip ·
11 Sine Wave · 12 Split Reveal · 13 3D Extrude · 14 Liquid Fill · 15 Decode Marker ·
16 Blur Bounce · 17 Zoom Shake · 18 Strike Rotate · 19 Rise Squiggle · 20 Outline Extrude

Full per-effect breakdowns + parameters: EFFECTS.md.

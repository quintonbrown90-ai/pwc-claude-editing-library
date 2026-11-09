# PROMPTS — the animation styles, one prompt each

Modeled on @viashaan's /animate system: each style is ONE prompt. Paste it,
swap the bracketed words, and Claude builds the animation from the bundled
template + STYLE_FILE tokens. Every prompt names its motions (MOTION.md) —
that naming is what separates these from generic "animate it" output.

## /stat-chart

```
Build a stat-chart animation with templates/stat-chart.html and STYLE_FILE.md.
Subject: [WHAT GREW]. Final value: [NUMBER with $/%]. Shape: [steady climb /
slow then spike / dip then recover]. Title it [TITLE], subtitle [SUBTITLE].
The line draws EASE IN-OUT over the phrase; the number counts up in STEPS
eased by EASE OUT and lands with an OVERSHOOT dot. Render 3.2s at 30fps
alpha WebM with render_animation.js. PWC tokens only — no red.
```

## /map-route

```
Build a map-route animation with templates/map-route.html and STYLE_FILE.md.
From [START LABEL] to [END LABEL] — the journey is the point of the line I'm
saying: "[THE SPOKEN LINE]". Route draws EASE IN-OUT, gold on navy streets;
destination pin drops OVERSHOOT at arrival. Render 3.4s alpha WebM.
```

## /headline

```
Build a headline animation with templates/headline.html and STYLE_FILE.md.
Masthead: [PAPER NAME]. Headline: "[THE CLAIM, 2–3 short lines]" — written
like news because the line lands harder as a fact than as a caption. Serif
italic lines reveal EASE OUT staggered; one body row highlighted gold.
Render 3.6s alpha WebM.
```

## /teardown

```
Build a teardown animation with templates/teardown.html and
STYLE_FILE.md. Break [THE THING] into exactly 4 layers, top = the part the
viewer sees first: [L1 / L2 / L3 / L4], each with a 4–6 word note. Layers
spread EASE OUT, labels SPRING in staggered 5 frames apart. Render 3.8s
alpha WebM.
```

## /paper-desk

```
Build a paper-desk animation with templates/paper-desk.html and
STYLE_FILE.md. Notes: [NOTE 1 title + 2–3 handwritten lines] / [NOTE 2] /
[NOTE 3]. Papers land OVERSHOOT staggered, handwriting (Caveat) reveals in
STEPS like it's being written, gold underline draws under the payoff line.
Render 4.0s alpha WebM.
```

## /ink-wash

```
Build an ink-wash animation with templates/ink-wash.html and STYLE_FILE.md.
Title: "[THE REFLECTIVE LINE]". Subtitle: [PLACE → PLACE or DATE]. This is
the faith/reset beat — slow EASE IN-OUT only, sun rises, mountains settle in
layers, nothing pops. Render 4.5s alpha WebM.
```

## /animate — build a NEW style into the system

```
Design a new animation style for the pwc-animations system: [DESCRIBE THE
VISUAL]. Build it as a single-file template in templates/ following the
existing ones exactly: 1080×1920 stage, transparent outside the card,
@font-face from ../fonts, window.DATA contract with sensible PWC defaults,
window.setT(ms) deterministic render, every motion named from MOTION.md,
STYLE_FILE.md tokens only. Add its prompt to PROMPTS.md in the same format
and register the component in the design system's COMPONENTS.md.
```

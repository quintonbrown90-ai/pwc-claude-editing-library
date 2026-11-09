# MOTION — physics specs (@adilet.fndr, Exhibit B decoded)

> **[MEASURED]** = visible in frames / his own on-screen specs.
> **[INFERRED]** = numeric parameters reconstructed to reproduce the look;
> starting values for our renderer, tuned by eye against his frames.
> Motion is always **named** (PWC house rule): every element's move in a
> beat plan carries one of these names + its numbers.

## His own exhibit [MEASURED]

The hero's Exhibit B names exactly three tuned effects, in his order:

1. **SPRING** — card shows a coil spring + an **overshoot curve graph**
   (value rises past TARGET, settles back). Label: "SPRING / OVERSHOOT /
   TARGET."
2. **WHIP PAN** — card shows the scene mid-blur; used to move between
   documents/scenes.
3. **ZOOM KICK 1.6x** — card prints the number: his zoom kicks punch to
   **1.6×**. (Bigger than PWC's talking-head cap of ~1.08 — his are
   animated documents, not a human face; the kick lands on *cards*.)

Plus a fourth card, **TUNED** — a gauge with its needle in the red: his
point is the numbers are *dialed*, not default. That is the whole lesson:
named presets, tuned once, reused forever.

## The presets (production spec)

### SPRING (the default entrance) [MEASURED behavior / INFERRED numbers]
- What: documents, cards and the avatar's props enter with spring physics —
  scale/position overshoots ~4–8% past target and settles. Nothing in his
  reels fades in or hard-cuts in at rest; everything *lands*.
- Spec for our renderer (CSS/HyperFrames `spring()` or GSAP equivalent):
  stiffness ≈ 170–220, damping ≈ 19–23 (≈8–12% visible overshoot), mass 1;
  settle ≈ 350–500ms. In named-vocab terms: **SPRING with OVERSHOOT built
  in**. Stamps are the exception (below).
- Exits are faster and dumber: EASE IN, 120–180ms, or the next whip covers
  them.

### STAMP SLAM (his verdict device) [MEASURED behavior / INFERRED numbers]
- What: SLOP / FIXED / SEALED / CLOSING FAST stamps drop from ~2.2× scale
  to 1× with a hard stop, slight rotation (−4° to −8°), zero bounce — an
  impact, not a spring. Reads in 2–3 frames at 30fps.
- Spec: scale 2.2→1.0 in 90–130ms, EASE OUT (power4), then 1-frame settle
  shake (±3px, 60ms). Pair with a low thump (AUDIO/BRAND sound rules).

### WHIP PAN (scene transition) [MEASURED behavior / INFERRED numbers]
- What: between evidence scenes the whole stage smears horizontally —
  motion-blurred frames in the contact sheet mark the whips.
- Spec: 200–280ms pan with directional blur, EASE IN-OUT, content swaps at
  peak blur. Used ~2–4× per reel, never between every beat (hard cuts and
  spring entrances do the rest).

### ZOOM KICK 1.6x [MEASURED number]
- What: on a claim's key word, the stage (or the document) punches in to
  **1.6×** fast, holds the beat, releases. In the hero it punctuates
  "Zoom kick" itself and emphases.
- Spec: 120–200ms to peak, SPRING settle, hold ≥ the phrase, EASE OUT
  release or whip away. On PWC talking heads this stays capped per BRAND
  (≤1.08 on his face) — the 1.6× kick applies to *documents/graphics*,
  exactly as in his reels.

### COUNT-UP (numbers) [MEASURED behavior / INFERRED numbers]
- Followers 2,457 → 50,000 and files 22 → 191 tick with digit rolls and a
  stamp-red display face; duration ~0.8–1.4s per count, STEPS-flavored
  ticking with an EASE OUT tail (fast early, lands on the exact figure).

### AVATAR POSE SWAPS [MEASURED]
- Pose changes are **hard cuts on the word** (STEPS — no tweened morph).
  The liveliness comes from *frequency* (new pose every ~1–3s) + the
  spring of the props he holds, not from character animation.

## Pacing of motion [MEASURED, hero]

- A visual event (entrance, stamp, kick, count-up, pose swap) lands at
  least every ~1.5–2.5s; no beat sits still longer than ~3s (PACING.md).
- Motion serves the word: the event fires ON the key word (or a hair
  before, per CAPTIONS.md timing), never in the gaps.

## PWC notes

- Same presets, PWC skin: stamps are **gold** (never red), kick stays 1.6×
  for graphics/documents only, face-safe rules from BRAND.md govern
  anything over Q's real footage (designed-captions lane rules apply
  there). For the avatar lane these presets are the default motion
  language and override older generic easing choices.

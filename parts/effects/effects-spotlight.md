<!-- PART: effects/effects-spotlight.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# EFFECT — spotlight [INFERRED reconstruction]

Source: @david_knowsai reel DfdAvbfRQY5 (8.0–12.3s) — his words:
"darkens the background while keeping you lit." Command:
`/effects spotlight`. Skill gated, NOT public — rebuild from this visible
spec only.

## The rule
The background darkens (vignette + dim) while the subject stays lit — a
pool of light on the speaker. No overlay on the face; the light IS the
effect.

## Executable steps (rebuild)
1. Face-track + segment the subject (MediaPipe cutout).
2. Dim the background to ~35% brightness with a soft radial falloff
   centred on the subject; subject brightness unchanged.
3. Entrance: 8–12 frames EASE OUT (the dark closes in); exit: 5–6 frames
   EASE IN. Sound: low whoosh on entrance.
4. PWC skin: the falloff edge carries a faint teal rim on the subject side;
   never a red or warm-orange pool.

## Face-clearance check
Nothing is placed over the face — the effect is lighting only. The
subject's face stays at full brightness and full sharpness.

## Worked example
Founder-diary beat: the room darkens around Q as he delivers the hard
line; the light pool holds him alone for 3 seconds, then the room returns
as the proof lands.

## Variants (v9)
- **v9 · @ibraviz.ai, DfZwGFMMdk1:** **V81 — @ibraviz.ai effect catalog (DfZwGFMMdk1):** slides orbiting around you (→ effects-orbit); spotlight over head (→ effects-spotlight); object following your finger; "Put big text behind me" as the spoken command for titles-behind-head (→ imagery-titles-behind-head). _(source: bulk-b VARIANTS.md)_

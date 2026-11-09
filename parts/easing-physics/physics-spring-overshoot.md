<!-- PART: easing-physics/physics-spring-overshoot.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# PHYSICS — spring + overshoot + bounce (PUBLISHED + verified)

Source: @viashaan motion vocabulary; spring/overshoot/bounce as implemented
in `skills/pwc-designed-captions/code/easings.py`.

## The rule
Physical motion settles — it never stops dead. Overshoot pops past the
target and settles back; spring oscillates softly; bounce rebounds.

## Executable values
- **Overshoot:** strength 1.70158, verified peak 1.141 (the element pops
  14% past its target, then settles). Use for titles, buttons, pins, pills,
  hero words. CSS: `cubic-bezier(0.34,1.56,0.64,1)`.
- **Spring:** stiffness 170.0, damping 16.0. Use for playful elements,
  chunky italics, stickers. JS spring; approximate bezier only if the
  renderer has no spring.
- **Bounce:** piecewise quadratic rebounds, 2 visible bounces. Use for
  drops, falling objects, playful landings. JS bounce.

## Worked example
Hero word lands: scale 92% → 103% (OVERSHOOT peak) → 100% over 4–7 frames.
A sticker pops in with SPRING (stiffness 170, damping 16) — soft settle,
no dead stop. A dropped number BOUNCEs twice before resting.

## PWC skin
Physics values never change per video — they are the house constants. What
changes is WHICH element gets which motion, per the plan.

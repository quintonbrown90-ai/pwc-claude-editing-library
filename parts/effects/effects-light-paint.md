<!-- PART: effects/effects-light-paint.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# EFFECT — light-paint: light trails paint from the hands [INFERRED reconstruction]

Source: @kayvon.ai reel DfPtyaCqhIa ("logos orbiting you / clone yourself /
text behind you / live sticker / light painting / new background — made by
Claude") — silent Format B showcase, screen recording of a Claude Code chat.
Command typed on screen: `/light-paint` — "Running /light-paint..." — effect:
flame/light trails paint from his hands — caption "light painting / made by
Claude". The prompt behind the command is GATED behind follow + comment EDIT
→ DM — never chased, never bought. Rebuild from the visible spec only,
labeled INFERRED.

## The rule
The hands are the brush: light trails paint the air wherever the hands move,
on gesture beats. The trail follows the gesture — it does not lead it. The
hands ARE the effect; the trail is the evidence that they moved.

## Executable steps (rebuild)
1. Hand-track both hands (skeleton/point track, per-frame) and emit a light
   trail from the fingertips on gesture beats only — the trail starts when
   the hand starts moving and fades 0.4s after it stops. No trail on still
   hands.
2. Trail look: gold core with a soft teal outer glow, 6–10px, fading tail
   (last 0.4s of the path dissolves). Flame variant: warm gold flicker at
   the fingertip on the beat, not a constant flame.
3. Entrance: trails begin on the typed command; the first gesture paints the
   first stroke. Sound: soft whoosh per stroke, never a continuous loop.
4. The trail never crosses the face — hand paths stay in the gesture zone
   (chest height and below, or the empty space beside the head).

## Face-clearance check
Trails come from the hands, face clear. If a hand rises toward the face, the
trail fades before it reaches the chin. PASS in the source video.

## Worked example (PWC)
Payoff beat: Q sweeps his hand across the frame on "and that's the whole
system" and a gold trail draws the arc in the air behind his words — the
gesture writes itself. PWC skin: gold trail, teal glow, navy background.

## PWC skin
Palette teal #14A886 + gold #FEE238 on navy #00214E, no red. Trails gold +
teal only — no orange flame, no red glow. QC status PENDING until the
you-and-Claude loop runs after upload.

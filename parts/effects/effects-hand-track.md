<!-- PART: effects/effects-hand-track.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# EFFECT — hand-track: a skeleton overlay follows the speaker's hand [INFERRED reconstruction]

Source: @kayvon.ai reel DfOTihaqSFx ("text behind you / stage lights / hand
tracking / logo rain / film grade / clone yourself — no editing app") —
silent Format B showcase, screen recording of a Claude Code chat. Command
typed on screen: `/hand-track` — "Running /hand-track..." — effect: a
hand-skeleton tracking overlay follows his hand — caption "hand tracking /
no editing app". The prompt behind the command is GATED behind follow +
comment EDIT → DM — never chased, never bought. Rebuild from the visible
spec only, labeled INFERRED.

## The rule
The hand is the demo: a skeleton overlay tracks the speaker's hand on
gesture beats, joint by joint, so the viewer sees the tracking work. The
overlay is ON the hand — it never covers the face, and it never appears when
the hand is still.

## Executable steps (rebuild)
1. Hand-track the raised hand (skeleton: wrist + finger joints, per-frame)
   and draw the overlay on the hand only: thin gold lines joint-to-joint,
   small teal dots at each joint.
2. The overlay appears on the typed command + the hand raise (the hand held
   up, fingers spread, IS the demo — the gesture triggers the track, not the
   other way round). When the hand drops, the overlay fades in 0.3s.
3. The overlay follows the hand with zero visible lag — if the track slips,
   the overlay cuts (never a floating skeleton). Sound: soft tick on lock-on.

## Face-clearance check
Overlay is on the hand, face clear. If the hand rises toward the face, the
overlay fades before it reaches the chin. PASS in the source video.

## Worked example (PWC)
Gesture beat: Q holds his hand up, fingers spread, on "this is the move" —
the skeleton locks on and the hand IS the diagram for three seconds, then
the overlay fades as he lowers it. PWC skin: gold skeleton lines, teal joint
dots, navy background.

## Not the X-ray body track
Distinct from effects-xray-body-track (the whole body tracked on every
frame, glued to the speaker). Hand-track is one hand, on gesture beats only
— a pointer, not a body suit.

## PWC skin
Palette teal #14A886 + gold #FEE238 on navy #00214E, no red. Overlay gold +
teal only. QC status PENDING until the you-and-Claude loop runs after upload.

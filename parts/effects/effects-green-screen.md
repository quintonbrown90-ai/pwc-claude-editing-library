<!-- PART: effects/effects-green-screen.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# EFFECT — green screen (Claude-built) [INFERRED reconstruction]

Source: Marc Cleroux / @tenfoldmarc reel Dew3PAQTMCs, canonical decode.
Effect 04 of 16 in his on-screen index. GATED pack — rebuild from
visible specs only. Built by Claude (keying + composite in the render),
no plugin.

## The rule
Cut the speaker out and swap the world behind him. The background is a
choice, not a location — a designed backdrop or a real place that proves
the claim.

## Look (MEASURED from frames)
- f_004: "04 green screen" highlighted in the index; the background is
  swapped to a patterned screen (geometric lattice) while he stays in
  place, mid-gesture motion blur on him — the swap is the effect, the
  subject never moves.

## Executable steps (rebuild)
1. Cut out the subject (MediaPipe/YuNet segmentation), 1–2px feather on
   the edge; de-spill the background colour off hair and shoulders.
2. Drop in the new background: either a DESIGNED backdrop (navy with a
   subtle gold pattern) or a REAL place Q has actually been (a real
   screen, a real room). Never a fake location pretending to be real,
   never AI-flat scenery.
3. Match the light: grade the backdrop to the subject's key light
   (warm/cool, direction) so the composite holds at phone size.
4. Entrance: hard cut on the trigger word (the world swaps in one
   frame) + soft whoosh. Exit: hard cut back.

## Trigger rule
A place-switch line: "imagine you're here", "now we're inside the
community", a before/after of location. One swap per video — the world
should change once and mean something.

## Face-clearance check
Keying never eats the face: check hair edges and the cap brim frame by
frame. If the cutout flickers on the face, the effect is cut — a
flickering face fails QC outright.

## Variants / cross-links
- **Digital zoom** (`parts/effects/effects-digital-zoom.md`): the other
  camera-HUD Marc device — zoom changes the FRAME, green screen changes
  the WORLD.
- **Backdrop word** (effects skill, David): a word behind the head —
  same cutout discipline, different payload.

## Worked example (PWC)
"Inside Paid With Content, this is the room" — hard cut, Q is suddenly
standing in front of the real Skool classroom (a real screen, not a
rendered room) as he names the community.

## PWC skin
Navy designed backdrops with gold pattern; real places shown as-is.
NO RED. Nothing over Q's face.

## Variants (v9)
- **v9 · @?, V8-87:** V8-87 — B-roll as green-screen background behind the speaker → effects-green-screen.md _(source: v9_verification.md)_
- **v9 · @liamjohnston.ai, DfI_L5VDohx:** **V76 — @liamjohnston.ai 50 installs (DfI_L5VDohx):** count-up cover (laptop screen 1→50); 50→5 funnel narrowing; category-of-ten structure (five buckets of ten — also kallaway-collections-taxonomy); proof number on slide 2 ("67,932 tool calls in 39 days" — a usage number, not a follower number). _(source: bulk-b VARIANTS.md)_

## Variants (v10)
- **v10 · @kayvon.ai, DfPtyaCqhIa:** **/new-room — live room swap:** the background swaps to a purple bokeh room, the speaker never moves — same operation as green-screen (cut out, swap the world behind him), live on the camera feed instead of in the render. PWC rooms: navy studio / proof wall, never purple bokeh. Command `/new-room`; prompt gated (comment EDIT → DM, never chased). _(source: Batch 8, v10)_

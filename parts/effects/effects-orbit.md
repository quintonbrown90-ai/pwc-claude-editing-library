<!-- PART: effects/effects-orbit.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# EFFECT — orbit [INFERRED reconstruction]

Source: @david_knowsai reel DfdAvbfRQY5 (3.9–7.7s) — his words: "makes
your video thumbnails circle around your head." Command: `/effects orbit`.
Skill gated, NOT public — rebuild from this visible spec only.

## The rule
Small thumbnails (real video stills, never stock) orbit in a ring AROUND
the head — the ring's centre is the head, the thumbnails never cross it.

## Executable steps (rebuild)
1. Face-track the head centre (YuNet/MediaPipe cutout).
2. Ring radius: head width × 1.6, centred on the head, in the face-clear
   graphic zone. 4–6 thumbnails on the ring, each a real still from Q's
   own videos.
3. Orbit: slow LINEAR rotation (one revolution ≈ 6–8s) — the ONLY place
   LINEAR is allowed (it is a machine motion, a spinner). Thumbnails stay
   upright (counter-rotate each thumb).
4. PWC skin: ring in thin gold stroke (teal for the active thumb); thumbs
   carry the PWC badge.

## Face-clearance check
The ring goes AROUND the head. No thumbnail ever crosses the face, even
at the ring's closest point — radius is set from the tracked head box
with ≥40px clearance. If the head moves, the ring follows the track.

## Worked example
Proof beat: 5 thumbnails of Q's own proof videos orbit while he says "all
five are real" — each thumb pauses at the top of the ring as its number
is spoken, then continues.

## Marc variant (Nov 8, 2026)
Marc Cleroux lists orbit as effect 09 of his 16 (`research/
video-harvest/instagram/marc_cleroux_Dew3PAQTMCs_DECODE.md`) — same job
(thumbnails circle the head), same trigger family. His 1fps frames show
only the index highlight ("09 orbit", f_010); no separate ring geometry
was measured, so David's spec above stays canonical. Do not duplicate
this part for Marc — one canonical part per effect.
## Self-learning — folded Nov 8, 2026 (research/knowledge/SELF-LEARNING.md)

- **SL-02** — Sky's lines MOVE (draw on, pulse, track); static overlays fail — an effect that sits still is a failed effect. (2026-11-07)

## Variants folded in (V7)
- **/zach-d-films — what-if 3D animated explainer** (@david_knowsai
  DfdFI5wh9Vy; the skill is GATED, rebuild from the visible spec only):
  same motion grammar as orbit/spotlight (a subject in a lit 3D space,
  camera orbiting), different visual language — the demo is a "what-if"
  scene (an arrow hitting armor) rendered as a 3D animated explainer. PWC
  use: a "what if you posted every day for 90 days" 3D scene — the what-if
  as a short animated vignette, not a full explainer.

## Variants (v9)
- **v9 · @ibraviz.ai, DfZwGFMMdk1:** **V81 — @ibraviz.ai effect catalog (DfZwGFMMdk1):** slides orbiting around you (→ effects-orbit); spotlight over head (→ effects-spotlight); object following your finger; "Put big text behind me" as the spoken command for titles-behind-head (→ imagery-titles-behind-head). _(source: bulk-b VARIANTS.md)_

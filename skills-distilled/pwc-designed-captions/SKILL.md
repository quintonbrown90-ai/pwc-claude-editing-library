---
name: pwc-designed-captions
description: Designed captions for Quinton's REAL talking-head videos (never the avatar lane) — word-timed captions where every phrase gets its own typographic treatment that switches as he speaks, captions placed in tracked empty space (never over his face, never under Instagram's UI), and one hero word per section passing BEHIND his head via a person matte. Use when editing Q's own on-camera footage and the ask involves captions, text effects, behind-the-head text, or "as I say it, the things happen".
---

# PWC Designed Captions — for Q's real videos only

Rebuilt from @viashaan's DESIGNED CAPTIONS system (see BREAKDOWN.md), remapped
to Q's locked rules. This skill covers Q's ON-CAMERA footage. For the avatar
lane use pwc-avatar-video; for animated inserts (charts, maps, headlines)
in either lane use pwc-animations; the brand/workflow stack that governs all
of it lives in pwc-design-system (MUSE.md / BRAND.md / WORKFLOW.md).

## The effect, in one line

Captions are DESIGNED, not typed: each phrase gets the treatment its meaning
earns, the treatment switches on the exact spoken word, and once per section
a hero word passes behind his head. "As I say it, the things happen."

## Q's hard rules (never overridden by the reference's look)

- NOTHING over his face. Captions live in the empty space above his head by
  default, or in tracked empty space beside it. Behind-head ≠ over-face:
  the hero word is OCCLUDED by his head — that's the one allowed crossing.
- PWC palette only: gold #FEE238, teal #14A886, deep navy #00214E, white.
  The reference's red accent word becomes GOLD serif italic. NO RED.
- Every box hard-clamped to the Instagram safe zones (code/safe_zones.py):
  never the top bar, never the right action rail, never the bottom block.
- Captions come from the script/word file as ground truth, snapped onto ASR
  word timings — never raw ASR text alone, never synced early.
- Imagery in scene swaps is REAL footage/photos/screen recordings.
- Motion is named from MOTION.md for every element (overshoot, ease_out,
  steps…). No unnamed animation ships.

## The style system

| Style | Look | Fires on | Motion in |
|---|---|---|---|
| BASE | Poppins ExtraBold karaoke, spoken word turns gold | default phrases | STEPS (word ticks) |
| SCRIPT_ACCENT | Playfair serif italic, gold | negations + feeling words (never, love, free…) | EASE OUT rise |
| GLOW | white with teal glow bloom | designed / automatic / system / AI moments | EASE IN-OUT bloom |
| BIG_CAPS | Anton, huge, white | the claim line of a section | OVERSHOOT pop |
| CHUNKY_ITALIC | Poppins ExtraBold Italic | energy / listing phrases | SPRING settle |
| HERO_BEHIND | Anton ~320px on the behind layer | ONE long content word per ~15s | EASE OUT |

Rotation discipline: never the same style 3 events running; BIG_CAPS at most
once per section; SCRIPT_ACCENT is a single word's moment, not a phrase look.

## Pipeline (run in order; plan BEFORE render, always)

```
python3 code/track_matte.py INPUT.mp4            # facetrack.json + fg_alpha.mp4
python3 code/transcribe_align.py INPUT.mp4 --script script.txt --out words.json
python3 code/plan_captions.py words.json --face facetrack.json --out plan.json
python3 code/render_captions.py plan.json --layer behind --out frames_behind --duration DUR
python3 code/render_captions.py plan.json --layer front  --out frames_front  --duration DUR
python3 code/composite.py INPUT.mp4 --behind frames_behind --front frames_front --fg fg_alpha.mp4 --out FINAL.mp4
```

Dependencies: ffmpeg, python3 + Pillow, numpy, opencv; WhisperX or
faster-whisper; a person matte for the behind layer — RobustVideoMatting
(RVM) is the quality pick (temporally stable), MediaPipe Selfie
Segmentation is the bundled fallback in track_matte.py. Without any matte,
composite front-only — say so, never fake the behind layer. (Research
basis: caption_skill_research — the reference claims face tracking "10 times a
second"; per-frame tracking at output fps + smoothing is what real
pipelines do, and it meets that.) Fonts are bundled in fonts/.

## QC before delivery (all on the exported file)

1. freezedetect: zero freezes ≥0.35s in footage spans.
2. Contact sheet at every style change: right style, right word, right frame.
3. Hero crossing strip (3 frames): head cleanly occludes the hero word.
4. Safe-zone audit: no caption pixel in the right rail / bottom block.
5. Face audit: zero caption pixels over the face outside the hero occlusion.
6. Last voice → end: no dead-air tail > ~1s.

## Files

- BREAKDOWN.md — the reference teardown (what the effect is, honestly)
- MOTION.md — the shared motion vocabulary + PWC house numbers
- PROMPTS.md — paste-ready Claude Code prompts (P1 full pass, P2 plan-only,
  P3 single hero word, P4 restyle)
- code/ — easings.py, safe_zones.py, track_matte.py, transcribe_align.py,
  plan_captions.py, render_captions.py, composite.py, example_plan.json

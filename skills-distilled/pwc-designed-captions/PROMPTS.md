# PROMPTS — paste-ready Claude Code prompts for designed captions

Run these inside the video's project folder (the pwc-design-system stack —
MUSE.md / BRAND.md / WORKFLOW.md — loads automatically). Each prompt is
self-contained; outputs land in the project folder.

## P1 — Full designed-caption pass on one talking-head video

```
Edit INPUT.mp4 with the pwc-designed-captions skill.
1. Run code/transcribe_align.py (script.txt is ground truth if present).
2. Run code/track_matte.py — I need facetrack.json AND fg_alpha.mp4.
3. Run code/plan_captions.py and SHOW me the plan summary (event count per
   style) before rendering. Follow BRAND.md: PWC palette only (gold serif
   italic accents, teal glow, NO red), captions above my head or in tracked
   empty space, NOTHING over my face, all boxes inside the IG safe zones.
4. Render both layers with code/render_captions.py and composite with
   code/composite.py. Every motion named from MOTION.md.
5. QC: freezedetect (zero freezes ≥0.35s), contact sheet at every style
   change, verify hero word passes behind my head cleanly, verify no caption
   touches the right rail or bottom block. Report per the WORKFLOW.md tests.
Output: FINAL_designed-captions.mp4
```

## P2 — Plan only (judge the design before rendering)

```
Using words.json and facetrack.json in this folder, run the caption planner
and print the full plan as a table: time, text, style, layer, box, motion_in.
Flag any phrase where two hero treatments would land within 15 seconds of
each other, and any box the safe-zone clamp had to move. Don't render yet.
```

## P3 — One hero word behind the head

```
In INPUT.mp4, put the word "WORD" (Anton, white, ~320px) on the behind layer
from T0 to T1 so it passes behind my head. Use track_matte.py's fg_alpha.mp4
as the top layer; entrance EASE OUT 7 frames, exit EASE IN 5 frames. Verify
with a 3-frame strip at the crossing point that my head cleanly occludes it.
```

## P4 — Restyle an existing plan

```
Read plan.json. Change every SCRIPT_ACCENT word to gold Playfair italic if it
isn't already, cap BIG_CAPS at one per section, and make sure no style repeats
3 events in a row (rotate BASE / CHUNKY_ITALIC / GLOW). Re-render and
re-composite; keep filenames versioned (v2, v3…).
```

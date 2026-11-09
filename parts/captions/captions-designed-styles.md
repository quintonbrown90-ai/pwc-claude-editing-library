<!-- PART: captions/captions-designed-styles.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# CAPTIONS — designed styles, switching per phrase (PUBLISHED)

Source: @viashaan designed-captions reel (verified timeline in
`skills/pwc-designed-captions/BREAKDOWN.md`) + `skills/pwc-designed-captions/`
(SKILL.md, PROMPTS.md P1–P4, code/ pipeline). Style switches land ON style
names in his reel: "glowing" 8.13s, "big white capitals" 9.45s, "chunky
italics" 11.01s; "never" accent 21.93s; CTA "Comment CAPTIONS" 31.4s.

## The rule
The caption treatment switches per phrase — never one flat style for a
whole video. Six styles: BASE karaoke / SCRIPT_ACCENT Playfair gold italic
/ GLOW teal / BIG_CAPS Anton / CHUNKY_ITALIC / HERO_BEHIND Anton ~320px
matte-occluded (the word passes BEHIND his head, 35.66s in his reel).

## Executable steps
1. Run `code/transcribe_align.py` (script.txt is ground truth if present).
2. Run `code/track_matte.py` — facetrack.json AND fg_alpha.mp4.
3. Run `code/plan_captions.py`, SHOW the plan summary (event count per
   style) before rendering. Cap BIG_CAPS at one per section; never repeat a
   style 3 events in a row (rotate BASE / CHUNKY_ITALIC / GLOW).
4. Render both layers (`render_captions.py`, `composite.py`). Every motion
   named from MOTION.md.
5. QC: freezedetect zero freezes ≥0.35s; contact sheet at every style
   change; verify the hero word passes behind the head cleanly (3-frame
   strip at the crossing point); no caption touches the right rail or
   bottom block.

## Worked example (DEMO A, delivered Nov 5)
"4 Content Types" raw take, 72 caption events, 4 HERO_BEHIND words:
TOGETHER 5.68s, COMPLETION 23.80s, RELATIONSHIP 41.66s, PARASOCIAL 60.20s.
Front captions yield during hero windows (collision found in QC, fixed).

## PWC skin
Real takes only (Q clarified Nov 4: designed captions are the real-videos
lane, not avatar). Palette PWC only; hero words never over the face — they
pass BEHIND it.
## Self-learning — folded Nov 8, 2026 (research/knowledge/SELF-LEARNING.md)

- **SL-06** — Designed captions rejected: chunks overlap/ghost — one chunk at a time, clean hard cuts. (2026-11-05)
- **PB-05** — Hero-behind-head done right: 4 genuine hero moments, front-caption yield, inserts on the word, zero freezes. (2026-11-05, Viashaan demos)

## Variants (v10)
- **v10 · @kayvon.ai, DfO7FQnqO_T:** **Motivation-clip caption treatment (B-roll only, NOT main talking heads):** word-by-word italic serif captions over dark cinematic B-roll, lower-centre, tracking the voice — "the fastest way / to attract / what you want / in life..." — the line IS the caption, one phrase at a time, never over the face. White-flash transition into the bright final shot (dark grind → flash → bright payoff). "Do the work." as the three-word closer on screen at the end. BOUNDARY: Q rejected the Viashaan designed-captions STYLE for his main edits Nov 7 — this serif treatment is for motivation/B-roll clips only, never for main talking-head captions (Sky exact governs those). The clip is likely reposted footage (landscape, voiceover not Kayvon's talking-head voice, Kayvon only in the last shot) — format only, never reuse the footage. _(source: Batch 8, v10)_


# CAPTIONS — Sky's caption + headline treatments

**The correction that matters (G-01, resolved Nov 9, frame-measured):** Sky's
captions are ALL-WHITE with NO current-word highlight. The accent keyword is a
SEPARATE large headline device (~15–20% of frame height) — NOT a caption highlight.
Any build that colors one word inside the caption line is NOT Sky.

## The two devices

### D1 — Caption groups (the captions themselves)
- White sans, 1–3 words per group, center-lower, on the word beat.
- Groups change every ~0.5s (~2 words/group; Sky speaks 3.93–4.73 words/sec,
  median ~4.3 wps; median word gap 0.18–0.22s).
- In-pop: HARD CUT to full size in ≤1 frame (≤0.033s at 30fps) — measured on
  DfX2 "Absolutely." onset 19.78s. No scale-in ramp, no fade.
- Caption band (measured DfX2 @2.0s, 720×1280 coords): captions ~y1230–1245;
  face box ≈ x345–735, hair top ~y720, chin ~y1170. Never over the face.
- Colors pixel-sampled: white #FCFCFC on near-black ground #040404–#0C1414.

### D2 — Accent headline (the keyword device)
- A SEPARATE large headline: small white lowercase kicker above 2 lines of huge
  bold condensed display (~105–125px cap height, ~68% frame width), sitting over
  the torso, under the face. Sky's green; Q lane: kicker white, main lines gold,
  framework keyword teal.
- Examples on disk: "REACH" / "Collab" / "Viral Two" / "DON'T" / "stop" / "Exactly".
- B&W beat (D21): the frame desaturates to B&W with ONE big accent word
  ("DON'T" in orange, DeSTW @13s; "stop" in green, DfIY @3.5s; "Exactly" in
  orange italic, DfA9 @40s). The headline IS the beat.
- D2 headline lockup: pop/scale ≈0.3s with slight overshoot + kicker fade 0.2s
  delayed 0.05s; holds ≈5s; hard-pop exit. Recurrence mid-reel UNVERIFIED.

## Reference frames (in this folder)

| File | Shows | Source |
|---|---|---|
| `caption_group_DfX2_19.8s.jpg` | Single-word white caption "Absolutely." at the measured hard-cut onset; D4 filter board above (LEILA CONTENT FILTER) | DfX2 @19.8s |
| `caption_band_facebox_DfX2_2.0s.jpg` | Face box + caption band geometry (the measured frame) | DfX2 @2.0s |
| `headline_stop_bw_DfIY_3.5s.jpg` | B&W beat + big "stop" headline (green), word-by-word landing | DfIY @3.5s |
| `headline_exactly_bw_DfA9_40.0s.jpg` | B&W beat + big orange italic "Exactly" | DfA9 @40.0s |
| `headline_dont_bw_DeSTW_13.0s.jpg` | B&W beat + big orange "DON'T" (D21) | DeSTW @13.0s |

## Motion (see `../motions/MOTIONS.md`)

- `cap_swap_DfX2.mp4` — caption groups swapping ~0.5s (DfX2 19.3–22.3s).
- `cap_headline_stop_DfIY.mp4` — B&W + "stop" headline landing (DfIY 2.8–4.2s).
- `cap_title_build_DfSf.mp4` — title words staggering in (DfSf 2.0–3.5s).
- `trans_bw_dont_DeSTW.mp4` — the B&W DON'T transition (DeSTW 12.5–14.5s).

## Execution template (PWC colors)

- `../templates/caption_demo_pwc.png` — 1080×1920 layout demo: navy ground, gold
  headline "REJECTS 99%" + white subline, all-white caption group "GOOD CONTENT"
  center-lower, face zone marked KEEP CLEAR, safe-zone guides at y=300 / y=1600.
- Full measured specs: `../../STYLE-GRAMMAR.md` §2 (D1), §4 (D2), §6 (pacing);
  `../../GAPS.md` G-01, G-14.

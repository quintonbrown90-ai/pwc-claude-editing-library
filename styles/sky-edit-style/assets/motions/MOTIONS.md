# MOTIONS — screen recordings of Sky's motions (Q order, Nov 9 ~04:01 CT)

**Purpose:** a still screenshot does NOT capture motion. These are SHORT CLIPS
(1.4–3.0s) trimmed from the source videos so the motion can be mimicked by
*seeing* it. Watch the clip, then build the device. Every clip starts ~0.5s BEFORE
the motion so the entrance is visible.

**Format:** 540×960, H.264 crf 24, audio kept (AAC 96k) — a clean downscale of the
720×1280 sources (1080×1920 for DfZ), faststart. Premium-checked: sharp, correctly
timed, not a mid-transition blur. Full-resolution originals stay on disk at the
source paths; the 28 earlier motion clips (native res, crf 20, ~21 MB) live at
`~/workspace/claude-editing/examples/sky/motion-teardown/motion_clips/` and are
referenced here, not duplicated.

**Verification (continuation pass, Nov 9 ~04:30 CT):** all 33 clips present on disk,
all 33 decode clean (full ffmpeg decode pass), audio present on all 33. The 15 clips
the first pass's index listed but had not yet written (all 3 caption clips, all 3
chart clips, all 3 phone clips, tier list, funnel card, checklist recap, profile
cards B&W, affiliate loop, anatomy bars) were cut from the priority-15 sources in
the same format and frame-QC'd (mid + start/end frames viewed). One first-pass stub
was found and repaired: `dev_funnel_tiers_DeA2.mp4` was a 262-byte file with no
streams — re-cut from De-A2dvCeV3 58.0–61.0s, verified (funnel tiers visible,
audio present). Both frame sequences were empty directories — now filled, 18 frames
each (see §4).

**Naming:** `trans_*` transitions · `dev_*` device entrances/exits · `cap_*` caption
animations · `chart_*` chart/diagram builds · `phone_*` phone movements.

## 1. TRANSITIONS — Sky's hard cuts, pops, slides

| Clip | Motion shown | Source |
|---|---|---|
| `trans_hardcut_broll_DfX2.mp4` (1.7s) | HARD CUT out to full-screen tennis B-roll and HARD CUT back — the cut itself, both directions, no fade, no dissolve | DfX2 51.8–53.5s |
| `trans_split_screen_DfLa.mp4` (2.0s) | HARD CUT into the split-screen layout (screen recording top / Sky below) — the whole frame re-lays-out in one frame | DfLa 17.0–19.0s |
| `trans_bw_dont_DeSTW.mp4` (2.0s) | B&W BEAT transition: color frame desaturates, big orange "DON'T" lands center — the beat IS the transition | DeSTW 12.5–14.5s |
| `trans_color_isolation_phone_DfLa.mp4` (3.0s) | Phone slides in from the right WHILE the background behind it goes B&W (color isolation) — phone stays in color, "POWER" / "POWER WORDS" land on the phone screen | DfLa 2.2–5.2s |

Sky's transition grammar: hard cuts everywhere; devices never fade out — they leave
on a hard cut to the next beat. The only fades in the 15 reels are the funnel+title
fade-out in DfX2 (~4.5–6.0s) and the slow desaturate-to-B&W ending of DfPxq
(~76.5–77.5s). No slow fades anywhere else.

## 2. DEVICE ENTRANCES & EXITS (D1–D25)

| Clip | Motion shown | Source |
|---|---|---|
| `dev_funnel_rain_DfX2.mp4` (3.0s) | Pills RAIN down one at a time into the funnel; ONE green pill drops out the bottom and lands as a green bar | DfX2 0.3–3.3s |
| `dev_checklist_DfQ4.mp4` (2.5s) | D5 checklist: 5 white pills stack in, pending rows blurred/dim, current row highlights in accent | DfQ4 0.5–3.0s |
| `dev_timeline_nodes_DeA2.mp4` (3.0s) | D12 timeline: nodes POP in sequence ~0.5s apart (accent ring + filled dot, label ABOVE the static full-width line) | DeA2 40.0–43.0s |
| `dev_venn_fill_DfPxq.mp4` (3.0s) | D7 Venn: circles slide together and the OVERLAP fills solid green | DfPxq 72.5–75.5s |
| `dev_staircase_draw_DfX2.mp4` (3.0s) | Staircase line DRAWS left-to-right, then green dots PULSE along it | DfX2 49.0–52.0s |
| `dev_headcloud_gray_DfDu.mp4` (3.0s) | Head cloud grows from ~3 heads to ~20 above his head, then heads turn GRAY one by one | DfDu 0.0–3.0s |
| `dev_cards_flyin_DfDu.mp4` (3.0s) | Three orange rounded-rect cards FLY IN from the sides and stack top-center, bobbing slightly | DfDu 26.0–29.0s |
| `dev_scriptlines_pulse_DfSf.mp4` (3.0s) | Script lines draw in one at a time, then the red "Lead" lines PULSE/glow (brightness spike ~2.5×, ~0.3s) | DfSf 16.0–19.0s |
| `dev_flow_lines_DfU49.mp4` (3.0s) | Flow-diagram nodes appear, CONNECTOR LINES draw between them (lines never exist before their endpoints) | DfU49 59.5–62.5s |
| `dev_newpost_fill_DeSTW.mp4` (3.0s) | D22 "New Post" dashed placeholder FILLS with thumbnails one by one | DeSTW 16.0–19.0s |
| `dev_dotgrid_flip_DeYKk.mp4` (3.0s) | D17 trust dot-grid: dots FLIP red (lose trust) → green (gain trust) | DeYKk 2.0–5.0s |
| `dev_100s_grid_DeYKk.mp4` (3.0s) | D19 "100s of people" grid of small orange squares fills in | DeYKk 74.0–77.0s |
| `dev_quiz_accumulate_DeYKk.mp4` (3.0s) | D11 quiz card: words ACCUMULATE as a vertical list (Legit → Business → Very Successful → Flashy…) | DeYKk 25.0–28.0s |
| `dev_funnel_tiers_DeA2.mp4` (3.0s) | Funnel tiers draw top→bottom, "$" icons POP below the funnel | DeA2 58.0–61.0s |
| `dev_tier_list_DfQ4.mp4` (1.6s) | Tier-list rows: small gray squares FILL IN one at a time down the S/A/B/C rows | DfQ4 7.2–8.8s |
| `dev_funnel_card_DfA9.mp4` (3.0s) | D24 funnel card: rows land (CONTENT / CHECKOUT PAGE / VSL), "FEEDS INTO BRAND" bar lands at the bottom | DfA9 53.0–56.0s |
| `dev_checklist_recap_DfA9.mp4` (2.0s) | Numbered checklist recap: green CHECKMARKS appear beside each row one at a time | DfA9 58.0–60.0s |
| `dev_profile_cards_bw_DfA9.mp4` (1.7s) | Three creator profile cards FLY IN top-right, then thumbnails DESATURATE to B&W left→right | DfA9 0.8–2.5s |
| `dev_affiliate_loop_DeYKk.mp4` (3.0s) | D18 dashed curved line draws between profile photos (the "affiliate army" loop) | DeYKk 66.0–69.0s |
| `dev_anatomy_bars_Dez4.mp4` (1.5s) | D15 script-anatomy bars DRAW one at a time (Hook red / Lead yellow / Body blue / CTA green) | Dez4 42.5–44.0s |

Entrance grammar (measured, motion teardown): panels/cards pop in fast (~0.2s) or
draw line-by-line (1.3–2.7s); the ACTIVE line then PULSES (glow spike, not a
position change); after drawing everything HOLDS steady, then exits by HARD CUT.
Devices never fade out. See `../../examples/reels/motion-clips-README_MOTION_CLIPS.md`
for the four measured motion laws.

## 3. CAPTION ANIMATIONS

| Clip | Motion shown | Source |
|---|---|---|
| `cap_swap_DfX2.mp4` (3.0s) | Caption groups SWAPPING ~0.5s — hard cut from group to group, full size in ≤1 frame, incl. the "Absolutely." onset | DfX2 19.3–22.3s |
| `cap_headline_stop_DfIY.mp4` (1.4s) | B&W beat + accent headline words landing one by one ("Look I'm just gonna" → "stop" → "right there") | DfIY 2.8–4.2s |
| `cap_title_build_DfSf.mp4` (1.5s) | Title words STAGGERING in ("Drop" → "Drop-offs" → "retention" → "you actually want") | DfSf 2.0–3.5s |

Caption grammar: 1–3 words/group, all-white, hard cut ≤1 frame, ~0.5s/group;
the accent keyword is a SEPARATE large headline, never a caption highlight
(see `../captions/CAPTIONS.md`).

## 4. CHART / DIAGRAM BUILDS

| Clip | Motion shown | Source |
|---|---|---|
| `chart_retention_draw_DfU49.mp4` (3.0s) | Retention line DRAWS left-to-right with a GLOWING DOT at the leading edge; axes/frame draw first (~0.5–1s), then the line. NOTE: the panel is a SMALL top-left insert over Sky (mini practitioner video + line), not full-screen — the beat then HARD-CUTS to the practitioner full-screen. The small panel is the whole draw. | DfU49 2.3–5.3s |
| `chart_views_countup_DfPxq.mp4` (3.0s) | "Views over time": the line is ALREADY DRAWN — the VALUES count up (1.1M → 2.6M → 2.7M) and "Second push" / "New surge" annotations stack on top | DfPxq 25.0–28.0s |
| `chart_wave_draw_DfQ4.mp4` (3.0s) | Sine-wave line draws ~3.0s (the longest draw measured); area under the line fills solid accent AFTER the line finishes | DfQ4 64.0–67.0s |

Frame sequences (step through the draw frame by frame, 6 fps, 270×480):
- `frames_retention_draw/` — 18 frames, DfU49 2.3–5.3s.
- `frames_staircase_draw/` — 18 frames, DfX2 49.0–52.0s.
- The full dense 12-fps sequences for 15 line-draw moments (~21 MB) live at
  `~/workspace/claude-editing/examples/sky/motion-teardown/motion_clips/frames_dense/`
  — referenced, not duplicated.

## 5. PHONE MOVEMENTS

| Clip | Motion shown | Source |
|---|---|---|
| `phone_drop_growthbar_DfQ4.mp4` (2.8s) | iPhone DROPS IN from top; horizontal progress bar below FILLS left-to-right (month 1 → month 6) | DfQ4 2.2–5.0s |
| `phone_slide_bounce_DfTawo.mp4` (2.3s) | iPhone SLIDES IN from top-right with a small BOUNCE, then flies off the top. NOTE: the phone is on screen only ~17.5–18.3s (profile showing 100,000 followers); the clip's last ~1s is Sky talking as the "Question 1" title lands — the slide-in, hold and fly-off are all inside the clip. | DfTawo 17.2–19.5s |
| `phone_show_it_live_DfQ4.mp4` (3.0s) | Phone drops in top-center; labels POP around it one by one (Product left → Service right → Coaching left) | DfQ4 19.5–22.5s |
| `trans_color_isolation_phone_DfLa.mp4` (3.0s) | (also §1) Phone slides in from the right as the background goes B&W; screen inside the phone keeps playing | DfLa 2.2–5.2s |

Phone grammar: phones enter with a drop/slide + settle (small bounce), play the
actual moment inside the screen, exit on a hard cut or fly-off. The screen inside
the phone is live video, never a static image. Phone-frame stills + templates:
`../phones/PHONES.md`, `../templates/phone_frame_pwc.*`.

## 6. CAMERA MOVES — what Sky's camera actually does

Sky's camera is LOCKED-OFF STATIC in all 15 priority reels: no pans, no tilts, no
tracking moves. All "movement" is digital, on the graphics layer:

- **Digital push-in / scale pop on devices:** the D2 headline pops/scales in ≈0.3s
  with slight overshoot; cards pop to full size in ≤0.2s. (See any `dev_*` clip.)
- **Scale + tilt device:** `DfQ4_scale_tilt_25s.mp4` in the existing motion-clips set
  (`~/workspace/claude-editing/examples/sky/motion-teardown/motion_clips/`) —
  the scale/tilt device, referenced not duplicated.
- **Zoom % is UNVERIFIED** (visual estimates only — G-14). No camera-move clip is
  filed here because no genuine camera move exists in the source set; filing a
  static 3s clip as a "camera move" would be a sub-premium filler, and the premium
  bar forbids it. If a push-in is found in a future reel, it goes here with its
  measured zoom %.

## 7. OTHER MOTIONS IN SKY'S VIDEOS

- **Point-follow:** graphics are SUMMONED by the pointing gesture — a mini video
  card drops in exactly where Sky points up (`DfZ_pointfollow_card_9s.mp4` and
  `DfIY_pointfollow_cards_0s.mp4` in the existing motion-clips set).
- **Little heads:** head cutouts pop in with a glow ring + crown
  (`DfTawo_heads_crown_22s.mp4` in the existing set; still in
  `../screenshots/hero_heads_crown_DfTawo_23.0s.jpg`).
- **Floating / bobbing:** D10 profile/grid inserts bob (y ±10px, 2.4s loop) +
  rotation ±1.5° — visible in `dev_profile_cards_bw_DfA9.mp4` and the DfDu
  orange cards (`dev_cards_flyin_DfDu.mp4`).
- **Count-ups:** values climb on the spoken beat — `chart_views_countup_DfPxq.mp4`;
  "How I Made Money" card still in `../charts/chart_how_i_made_money_DeYKk_60.0s.jpg`.
- **Emoji pops:** yellow thinking-face emoji pops near the chest (DeSTW) — visible
  in the DeSTW contact-sheet record; no dedicated clip (brief, ~0.5s, single pop).

## Motion clips already on disk (referenced, NOT duplicated — 28 clips, ~21 MB)

`~/workspace/claude-editing/examples/sky/motion-teardown/motion_clips/` —
`motion-clips-manifest.json` + `motion-clips-line_draw_measurements.json` are copied
in `../../examples/reels/`. The 28 cover: line draws (DfZ process, DfX2 staircase,
DfU49 retention, DfTawo trait lines, DfQ4 wave, DfPx double-peak, DfSf graph,
DfU49 flow), funnel rain, script-lines pulse, point-follow cards, heads/crown,
dot-grid, org chart, flashcards, phone B&W, Venn fill, scale/tilt. The 33 clips in
this folder are the motions those 28 do NOT cover (caption swaps, phone drops/
slides, B&W beats, checklist ticking, timeline nodes, count-ups, dot-grid flips,
100s grid, quiz accumulate, affiliate loop, profile-card B&W, hard-cut transitions).

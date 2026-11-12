# MOTION CLIPS — @realskytan, 14 reference reels

**Purpose:** playable clips so Claude can WATCH Sky's devices move — the motion the still-frame
teardown could not show. Watch each clip, then code the device. The numbers below are the timing
spec: they were measured from the frames, not guessed.

**How to use:** for each device you need to build, watch its clip(s) first, then read the measured
timing in the table. The line-draw clips have dense 12 fps frame sequences in `frames_dense/<clip>/`
if you need to step through a draw frame by frame.

**Resolution note:** clips are the sources' NATIVE resolution — 720×1280 for 13 reels, 1080×1920
for DfZ (the only 1080p source). They were NOT upscaled: upscaling 720p to 1080p adds no detail.
H.264, crf 20, audio kept (AAC 128k). Claude upscales for the phone copy as before.

**Totals:** 28 clips, 21.4 MB · dense 12 fps frames for 15 line-draw moments, ~21 MB · folder total ~43 MB.
Every clip starts ~0.5s BEFORE the device appears so the entry is visible.

**Companion doc:** `../SKY_MOTION_TEARDOWN.md` — the 35-device master index with layouts and
per-reel timelines. These clips are the motion proof for that doc.

---

## THE MEASURED MOTION LAWS (read this first)

Measured with OpenCV on 12 fps frames: accent-color pixel count + line extent (rightmost accent
pixel, 0–1000 coords) in the panel ROI, per frame. Four laws hold across all 15 measured draws:

**1. Chart lines draw left-to-right with a glowing leading dot, 0.5–3.0s.**
Retention graph (DfU49): 0.5s, extent 235→940. Sine wave (DfQ4): ~3.0s, extent 305→911.
Double-peak (DfPx): 1.33s, extent 279→755 — the ONE draw that clearly eases out (extent velocity
falls across the draw); all others run at roughly constant velocity. Area under the line fills
solid accent AFTER the line finishes drawing. Axes/frame draw first (~0.5–1s), then the line.

**2. Panel / script lines either draw one at a time (1.3–2.7s) or pop in fast (~0.2s) — then they
PULSE.**
Slow sequential draws: DexJ structure panel 2.67s (one line ~0.3s each), Dez4 script lines 1.42s,
DfSf red "Lead" lines 1.33s. Fast pop-ins: DfDu lines panel 0.17s, DeA2 lines panel 0.17s.
After appearing, the ACTIVE line pulses/glows — measured on DfSf's red "Lead" lines: red accent
pixels spike 2,049 → 5,236 (~2.5×) for ~0.3s at the pulse beat (reel 18.2s), then settle back
to ~2,050. The pulse is a brightness/glow spike, not a position change. Build it as a glow
intensity keyframe on the active line.

**3. Connector lines draw AFTER their nodes land, 0.4–2.4s.**
Trait-strip connectors (DfTawo): 0.42s. Flow-diagram connectors (DfU49): 2.42s for the full
node+line build. Tree branches (DfA9): 1.25s. The line is never there before its endpoints.

**4. After drawing, everything HOLDS steady — then exits by hard cut.**
In every measured clip the line extent stays at its maximum after the draw (no shrink, no drift).
Devices never fade out: they leave on a hard cut to the next beat (e.g. DfU49's panel exits on a
cut to subject footage at reel 3.8s; DfZ's process cards exit on the B-roll cut at 23.5s).
No slow fades anywhere.

**Method caveats (honest limits):**
- Measurements are accent-pixel extent inside the panel ROI (top ~0–450 of frame). Where other
  accent elements share the ROI (DfZ: checklist + titles in frame), the "draw duration" the
  detector reports is inflated — the teardown's timestamps are the cleaner read there.
- 12 fps sampling: anything faster than ~0.1s is approximate; the 0.17s "pop-ins" are at the
  edge of what 12 fps resolves — treat them as "effectively instant, ≤0.2s".
- The DfU49 "post-draw pulse" the detector flagged is NOT a pulse: it is the hard-cut exit
  (accent pixels drop to 0 when the panel leaves). Same for DfZ/DfA9 tail drops.

---

## LINE-DRAW MEASUREMENTS (15 moments, 12 fps)

| Clip | Accent | Draw window (in clip) | Draw dur | Extent (x, 0–1000) | Velocity | After draw |
|---|---|---|---|---|---|---|
| DfZ_line_draw_process_21s | green | 1.75s spike: count 5,700→16,200 as line+cards land | ~1.3s (teardown 21.5–22.8s) | 816→885 | constant | holds, exits on B-roll cut 23.5s |
| DfX2_staircase_draw_49s | green | line 49.5–50.5s, dots pulse 51–52s | ~1.0s line + 1s pulse | 112→998 | constant | dots pulse, exits on B-roll cut 52.2s |
| DfU49_retention_draw_2s | green | 0.67–1.17s | **0.5s** | 235→940 | constant | holds, hard cut to subject 3.8s |
| DfU49_flow_lines_59s | green | 0.00–2.42s | 2.42s (nodes+lines) | 207→796 | constant | steady hold |
| DfTawo_trait_lines_38s | green | 0.25–0.67s | **0.42s** | 148→833 | constant | steady hold |
| DfSf_graph_draw_0s | green | 1.17–1.75s | 0.58s | 222→822 | constant | morphs flat + area fills after |
| DfSf_scriptlines_pulse_15s | green | green line already present at clip start | — | 433→942 | — | red lines pulse (see RED row) |
| DfSf_scriptlines_pulse_15s (RED) | red | 1.08–2.42s | 1.33s | 401→787 | constant | **PULSE: red px 2,049→5,236 (~2.5×) for ~0.3s at reel 18.2s** |
| DfQ4_wave_draw_64s | green | 0.00–4.42s (axes+wave+labels) | wave ~3.0s | 305→911 | constant | dots at peaks, labels pop |
| DfPx_doublepeak_1s | green | 0.75–2.08s | 1.33s | 279→755 | **slowing (ease-out)** | steady hold |
| DfDu_lines_panel_14s | orange | 0.00–0.17s | **~0.2s (pop-in)** | 0→998 | instant | mild oscillation as labels pop |
| DfA9_twocurve_10s | orange | 0.00–3.00s | 3.0s (bell fast ~0.8s, S-curve slow ~1.8s) | 237→714 | constant | S-curve crosses bell, labels pop |
| DfA9_tree_branches_20s | orange | 0.00–1.25s | 1.25s | 166→914 | constant | highlight pulses on chosen option |
| DeA2_lines_pulse_6s | orange | 0.00–0.17s | **~0.2s (pop-in)** | 27→905 | instant | lines pulse after appearing |
| Dez4_scriptlines_point_41s | orange | 0.00–1.42s | 1.42s | 387→762 | constant | pulses; Sky points up at panel 43.0–44.5s |
| DexJ_structure_lines_0s | orange | 0.00–2.67s | 2.67s (one line ~0.3s each) | 150→720 | constant | steady hold; arc sweeps 0.8–1.2s |

---

## CLIP MAP (all 28)

### DfZ_q_pFbX1 — "Why Process Crushes" — GREEN

| File | Reel time | Device | What moves and how | Spoken beat |
|---|---|---|---|---|
| `DfZ_line_draw_process_21s.mp4` (3.0s) | 21.0–24.0s | Line draw — "The Whole Process" | 3 cards pop, then the connecting line DRAWS between them (~1.3s, reel 21.5–22.8s); cards morph to "Final result" 22.8–23.5s; hard cut to B-roll 23.5s | "And when you can see the final logo, it's way more satisfying. Like watching those satisfying…" |
| `DfZ_pointfollow_card_9s.mp4` (3.0s) | 9.3–12.3s | Point-follow — mini video card | Card drops in from top EXACTLY as Sky points up at it; "The 2 Things" checklist slides in from right at the same beat; row 1 fills green | "two things. First, problem articulation. You know the original logo is bad, but…" |

### DfX2qwQGagM — "Good Content Strategy" (Leila Hormozi) — GREEN

| File | Reel time | Device | What moves and how | Spoken beat |
|---|---|---|---|---|
| `DfX2_staircase_draw_49s.mp4` (4.0s) | 49.0–53.0s | Line draw — staircase chart | "BORING TO YOU, GOLD TO THEM" staircase line draws L→R (~1s, 49.5–50.5s); green dots PULSE on the steps 51–52s; hard cut to tennis B-roll 52.2s | "informative to everyone else. It's kind of like watching a great athlete practice…" |
| `DfX2_funnel_rain_0s.mp4` (4.0s) | 0.3–4.3s | Diagram build — funnel | Funnel icon top-center; white pills RAIN in one at a time (~0.3s each); one green pill DROPS OUT of the funnel at 3.0s (the filter rejecting) | "the sign of a good content strategy is it rejects 99% of all of your ideas." |

### DfU49SJAFYH — TCM retention breakdown — GREEN

| File | Reel time | Device | What moves and how | Spoken beat |
|---|---|---|---|---|
| `DfU49_retention_draw_2s.mp4` (4.2s) | 2.3–6.5s | Line draw — retention graph | Graph panel slides in from right; green line draws L→R in **0.5s** (reel 2.97–3.47s) with a glowing dot at the leading edge; "Drop off" pill lands; hard cut to subject footage ~3.8s | "by using the retention graph. Here's why you constantly have throat mucus and what your doctor can't…" |
| `DfU49_flow_lines_59s.mp4` (4.0s) | 59.0–63.0s | Line draw — flow diagram | Nodes appear one at a time, then connector lines draw between them (Spleen→Fluids / Phlegm←Dampness); full build ~2.4s; labels "Every line connects" land beside it | "They want to talk about the fluids and then the dampness and then the flap. So every line connects to the next…" |

### DfTawo5jHMH — "The 4 Questions Filter" — GREEN

| File | Reel time | Device | What moves and how | Spoken beat |
|---|---|---|---|---|
| `DfTawo_heads_crown_22s.mp4` (4.0s) | 22.0–26.0s | Little heads — constellation + crown | 5 head cutouts pop in around the panel; center head gets a green GLOW RING + CROWN (~23.5s); heads bob gently while on screen | "call, using problems that only your favorite customers experience will attract more of them…" |
| `DfTawo_trait_lines_38s.mp4` (3.5s) | 38.5–42.0s | Line draw — trait-strip connectors | 5 trait thumbnails pop; connector lines DRAW from each thumbnail to "You" in **0.42s**; highlights land per named trait 41–43s | "a personality and traits you want to be known for. Whether that's helpful, nice, relatable…" |

### DfSf5v8j73o — "Drop-offs you actually want" — GREEN

| File | Reel time | Device | What moves and how | Spoken beat |
|---|---|---|---|---|
| `DfSf_graph_draw_0s.mp4` (3.8s) | 0.7–4.5s | Line draw — retention graph + morph | Green line draws in **0.58s** (reel 1.87–2.45s); line MORPHS to flat ~85%; area under curve FILLS solid green L→R (4.5–6.0s); "Everyone" pill lands ~7.0s | "you this, but you actually want drop-offs in your retention graph. If your graph is a flat line…" |
| `DfSf_scriptlines_pulse_15s.mp4` (4.0s) | 15.5–19.5s | Line draw + PULSE — script lines | Horizontal lines draw one at a time (white "Hook", RED "Lead" lines bracketed, GREEN line); red "Lead" lines draw 1.33s then **PULSE/glow red** — measured spike ~2.5× brightness at reel 18.2s; small heads grow at panel edge ~22s | "So the lead is what comes after the hook. It's lines two and three of your script. Line one, AKA…" |

### DfQ4E1Hjn0n — "5 Content Types" — GREEN

| File | Reel time | Device | What moves and how | Spoken beat |
|---|---|---|---|---|
| `DfQ4_wave_draw_64s.mp4` (4.5s) | 64.0–68.5s | Line draw — sine wave | Axes draw first; dotted SINE WAVE draws L→R over **~3.0s** (64.5–67.5s) with green dots at peaks/troughs; "Superfans" labels pop at peaks 68–69.5s | "in the seasons where you run out of information to talk about or your content just isn't as good, your…" |
| `DfQ4_scale_tilt_25s.mp4` (4.2s) | 25.3–29.5s | Diagram build — balance scale | "1 Demo = 10x Trust": scale line draws ~26.0s with green "Demo" weight left; scale TILTS left down ~26.5s; "X10 Talking Heads" loads right ~28.0s and scale TIPS right ~28.5s; tilts back and forth | "faked. I'd say one live demo is probably worth 10 times more than a regular talking head in…" |

### DfPxqFPAY4_ — "Viral Twice" — GREEN

| File | Reel time | Device | What moves and how | Spoken beat |
|---|---|---|---|---|
| `DfPx_doublepeak_1s.mp4` (3.0s) | 1.0–4.0s | Line draw — double-peak chart | Green line draws a DOUBLE PEAK in **1.33s** — the one measured ease-out (velocity falls across the draw); "Wave 1"/"Wave 2" labels pop above each peak; "x2" lands at right | "one video go viral twice in one click without reposting? So you do this…" |
| `DfPx_venn_fill_70s.mp4` (4.5s) | 70.0–74.5s | Diagram build — Venn | Two circles DRAW (~0.5–1s each), SLIDE together over ~1s, overlap lens FILLS green ~74.0s; heads sit on top of each circle | "both sides. So ask yourself, do your audience interest overlap? That crossover should match both…" |

### DfLaEFNDKkv — "Power Words" — GREEN

| File | Reel time | Device | What moves and how | Spoken beat |
|---|---|---|---|---|
| `DfLa_phone_bw_1s.mp4` (3.8s) | 1.7–5.5s | Phone/UI mockup + color isolation | Full IG Reels phone UI SLIDES IN from right; background goes BLACK AND WHITE ~3.0s while the phone stays in color; "POWER" / "POWER WORDS" text lands on the phone screen; phone slides out right ~5.2s, color returns | "can make your hooks unskippable just by using power words. Power words are adjective, terms, phrases that…" |
| `DfLa_flashcards_6s.mp4` (3.5s) | 6.5–10.0s | Reaction pop — movie-still flashcards | Frame goes BLACK; small rounded-rect movie stills FLASH one at a time center, each ~1s, with a slight Ken Burns scale-in and a white word label ("Visceral", "Addicting", "Cancerous"…) | "that create a visceral effect. I think where it's like addicting, cancerous…" |

### DfIYshekeF3 — "ChatGPT ideas" — GREEN

| File | Reel time | Device | What moves and how | Spoken beat |
|---|---|---|---|---|
| `DfIY_pointfollow_cards_0s.mp4` (3.5s) | 0.0–3.5s | Point-follow — format cards | Three dashed-border video cards DROP IN top, one per point — each appears in the space Sky's finger is pointing at, on the exact frame his hand arrives; fly off ~4.5s | "Stop start reaction, tier list, challenge storytelling, look, I'm just gonna stop right…" |
| `DfIY_orgchart_10s.mp4` (4.5s) | 10.0–14.5s | Diagram build — org chart | "MY CONTENT TEAM" title bar; 3 columns build; head with white arrow FLIES IN from left ~11.5s; green "VIEWS" and white "DOLLARS" cards slide in; dollar counter counts $18,700 → $12,400 → $15,300 | "just show you what my team does to get contact ideas that gets views and dollars over and over again…" |

### DfDuMnCjNdE — "Shallow formats" — ORANGE

| File | Reel time | Device | What moves and how | Spoken beat |
|---|---|---|---|---|
| `DfDu_headcloud_0s.mp4` (4.0s) | 0.0–4.0s | Little heads — cloud goes gray | Cluster of ~20 head cutouts GROWS from ~3 to full cloud by ~1.0s; orange "?" badge on top ~0.5s; heads turn GRAY/desaturated one by one from ~2.5s (audience "going gray"); cloud fades ~3.8s | "If you're wondering why your audience doesn't value your opinions or your takes, it's because you're posting…" |
| `DfDu_lines_panel_14s.mp4` (4.0s) | 14.0–18.0s | Line draw — "SHIFTING BELIEFS" panel | Colored horizontal lines appear in **~0.2s (pop-in, not a slow draw)**; title lands ~16.0s; small head + "Audience Belief" label pops at panel's left edge ~17.0s | "of room for the thing that actually creates thought leadership, which is shifting beliefs. Your audience has…" |

### DfA9L-PHYWp — "Content-Offer Fit" — ORANGE

| File | Reel time | Device | What moves and how | Spoken beat |
|---|---|---|---|---|
| `DfA9_twocurve_10s.mp4` (4.5s) | 10.3–14.8s | Line draw — two-curve chart | BLUE bell curve draws fast (~0.8s); ORANGE S-curve draws SLOWLY (~1.8s) and CROSSES the blue curve; small label lands at the orange curve's end ~14.2s | "get a viral video overnight, but changing your positioning takes months. That's why until I understand the ava…" |
| `DfA9_tree_branches_20s.mp4` (3.0s) | 20.0–23.0s | Line draw — brand-direction tree | Head at left; branching lines DRAW to 4–5 option pills over **1.25s** (rows appear one at a time ~21–22s); "Problem Solver" HIGHLIGHTS orange ~22.0s; orange card pops right of it | "determine your brand direction or content strategy, kill…" |

### De-A2dvCeV3 — "These formats are officially dead" — ORANGE

| File | Reel time | Device | What moves and how | Spoken beat |
|---|---|---|---|---|
| `DeA2_lines_pulse_6s.mp4` (3.5s) | 6.0–9.5s | Line draw + PULSE — LINES panel | Colored lines (orange/yellow/blue/green) appear in **~0.2s (pop-in)**; lines PULSE after appearing; format cards orbit around the panel; small orange circle icon | "it feels really good to consume, but they're just nutritionally empty. The rapid fire high…" |
| `DeA2_funnel_57s.mp4` (5.0s) | 57.0–62.0s | Diagram build — 3-tier funnel | Funnel tiers DRAW top-center one at a time (blue top ~58.0s, purple middle ~58.5s, green bottom ~59.0s); tier labels pop per tier; "Trust → Potential Clients" lands ~60.5s; three green "$" icons pop below ~61–62s | "for top-of-the-phone attention, but just make sure you have nutrient-dense formats on the backend to catch…" |

### Dez4fPJCR74 — "The absolute worst content strategy is teaching" — ORANGE

| File | Reel time | Device | What moves and how | Spoken beat |
|---|---|---|---|---|
| `Dez4_scriptlines_point_41s.mp4` (4.3s) | 41.7–46.0s | Line draw + POINT — script-structure panel | Colored bars draw one at a time over **1.42s** (Hook red, Lead yellow, Body 1 blue, open loops, CTA green); Sky POINTS UP at the panel with his right index finger 43.0–44.5s as the bars land; bars pulse after drawing | "A scripted video following this structure highlighting one specific insight, not a top 5…" |
| `Dez4_crown_crowd_34s.mp4` (4.5s) | 34.0–38.5s | Little heads — crowned head + crowd | Sky's head cutout with gold CROWN + "Competitive Advantage" label at chest; ~6 small female head cutouts fan out below ~35.0s, MULTIPLYING to ~15 heads by ~38.0s | "This becomes our competitive advantage and it's the key to winning in a saturated market. And finally,…" |

### DexJ-qWiWdY — "The ultimate storytelling caption" — ORANGE

| File | Reel time | Device | What moves and how | Spoken beat |
|---|---|---|---|---|
| `DexJ_structure_lines_0s.mp4` (3.5s) | 0.0–3.5s | Line draw — caption-structure panel | Colored lines draw ONE AT A TIME over **2.67s** (~0.3s each: Introduction red, Struggle yellow, Rise blue, Proof teal, Unique Mechanism pink, Expectations white, Two-Door CTA green); dashed white arc SWEEPS down the panel's right side 0.8–1.2s; glowing IG logo pops top-right ~2.8s; Sky points up at panel 0.0–0.5s | "This is the ultimate storytelling caption for Instagram, and you…" |
| `DexJ_dotgrid_17s.mp4` (4.5s) | 17.0–21.5s | Diagram build — 1000-comments dot grid | ~10×10 grid of orange dots FILLS IN at chest over ~0.5s; left columns turn GREEN ~19.2s (100 people); comment bubbles RAIN DOWN from the top ~19.5–21.5s; right portion turns YELLOW-GREEN ~21.0s (700 people) | "out of the 1,000 people who commented, 100 people asked to work with us and 700 got nurtured…" |

---

## WHAT IS *NOT* IN THESE CLIPS (and why)

- **No Follow → Following animation.** It does not exist in any of the 14 reels — confirmed again
  while cutting. Build it from Q's description (point-down "follow me" beat → profile pops up,
  button flips Follow → Following ✓ with tap + ding), as a new device in Sky's grammar.
- **No classic meme/GIF sticker pops.** Closest is DfLa's movie-still flashcards
  (`DfLa_flashcards_6s.mp4`). Meme pops in Q's edits come from the Carter/Kilgore grammar, not Sky.
- **No end cards.** Every reel ends on Sky mid-sentence or on a diagram. (Q later ordered end
  cards added to the re-renders anyway — that is Q's call, not Sky's grammar.)
- **No word-by-word caption-motion clip.** Captions are the same device in every reel (one word at
  a time, hard cut per word, center-lower, keyword in accent) — visible in every clip above; a
  dedicated clip would show nothing new. The DfU49 and DfLa clips show it clearest.

## FILES IN THIS FOLDER

- `README_MOTION_CLIPS.md` — this file.
- `manifest.json` — machine-readable clip list (reel, timestamps, device, family, duration, size, spoken beat).
- `line_draw_measurements.json` — full per-frame measurement data for the 15 line-draw moments
  (accent pixel counts + line extent per 1/12s frame, draw windows, easing, pulse, tracking).
- `*.mp4` (28) — the motion clips.
- `frames_dense/<clip>/` (15 folders, ~660 frames at 540×960, 12 fps) — dense frames for the
  line-draw moments.
- `cut_clips.py` — the script that cut the clips (reproducible).
- `measure_lines.py` — the OpenCV measurement script (reproducible).

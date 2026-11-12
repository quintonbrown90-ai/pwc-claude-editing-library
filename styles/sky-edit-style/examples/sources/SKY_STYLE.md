# SKY STYLE: the default edit for Q's real talking-head videos (2026-11-06)

**Status: DEFAULT. Overrides every earlier real-video editing style** (master edit model, e10–e19 cards, premium/Comment Court renderer, the liked navy cards, the v2 engine, the window split and the punch-in-every-2-s camera). Those stay in the repo as an archive and a menu, and are used only when Q asks for one by name. **The avatar lane is untouched** (`pwc-avatar-video`, `references/ai-avatar/`).

**Source:** 15 realskytan reels Q screen-recorded on 2026-11-06 ("learn this, every bit of it… copy everything… keep my Paid With Content colour scheme throughout… create your own types on top"). Three analyst passes went through them frame by frame, plus a quantitative pass. Everything is in `references/realskytan/`:
- `BREAKDOWN_A.md` (reels 01–05), `BREAKDOWN_B.md` (06–10), `BREAKDOWN_C.md` (11–15). Each has per-reel timestamps and an IMPLEMENTATION SPEC with exact numbers.
- `metrics/m_*.json`: face size and position, cuts, zoom jumps, push ramps and loudness, measured per reel.
- `sheets/c_*.jpg`: 16-frame contact sheets. `keys/`: 30 full-res key stills.

**Code:** `edits/pwc-sky/engine/`
- `sky.py`: the components, motion curves, glass compositor and grade.
- `render.py`: camera, plate, captions and the SFX event list.
- `mix.py`: voice gain plus a constant music bed plus sparse SFX.
- `run.sh`: renders and mixes one video.
- `matte.py`: the person matte (RVM) used for behind-the-head layers.

Plans live in `edits/pwc-sky/plans/s_<video>.py`.

---

## 1. The system in one paragraph
A dark, low-key plate of the speaker, locked off, with a **frosted-glass HUD zone in the top ~40 %** of the frame. One master graphic at a time builds piece by piece **on the spoken word**:
- rows slide in
- charts draw on
- numbers count up
- chips pop
- cards drop

Small **plain white captions** (1–3 words, no box, no animation) sit under his chin and follow his face. Every hook opens with a **fast zoom-out from 1.45x**. About every 15–25 s a **pattern interrupt** lands: a hard punch-in and/or a **black-and-white beat** with one **heavy accent word**. **Serif-italic display titles** (Instrument Serif) mark the hook and new sections. When a dense graphic fills the screen, the speaker gets a **focus pull** (blur plus darken). The music is a quiet bed and the SFX are sparse. Restraint is the look.

## 2. PWC colour mapping (Q: "keep my paid with content color scheme throughout")
| realskytan | PWC |
|---|---|
| green / orange accent (#56AF39, #E8913F) | **gold #FEE238** for hero words, serif line 1, highlights and lit grid cells; **teal #14A886** for borders, checks, chart lines and pills |
| neutral glass rgba(255,255,255,.07) | the blurred plate at 62 % + **ink navy (6,22,48)** at 30 % + white 7 %, with a teal border at 60 % |
| red negatives #E86A5E | red #FF5C5C (✕ rows, "MEETING OVER") |
| white captions | white captions; **gold** on the keywords listed in the plan (`gold_words`) |
| cool teal grade | low-key grade with a navy shade over the top HUD zone (sits on the logo navy #00214E) |

## 3. Camera and plate (`render.py`)
- **Framing:** his face sits lower than in our old edits. The plate drops ~120 px (`drop`) so the HUD zone (y 110–760) sits above his cap. Tall cards (`tall=True`) slide the plate a further 150 px down (in over 30 f with in-out easing, out over 20 f), as the reels do.
- **Hook zoom-out:** `s = 1 + 0.45·2^(-t/0.18)`, anchored on his face (1.45x at f0, 1.10x at f12, 1.0 by f30). This runs on every video.
- **Slow push:** within long beats, 1.00 → 1.04–1.06 eased (`push`).
- **Punch-in:** a hard cut to 1.12–1.18x on hero lines, held 1–1.5 s (`punch`). Panels clear during these beats.
- **B&W beat:** saturation 0 plus 10 % contrast plus 1.22x, held 1–1.6 s, with a gold hero word (`bw`). No impact sound on it, which matches the reels.
- **Focus pull:** blur sigma ~18 plus brightness ×0.70 under proof walls and dense cards (`focus`).
- **Grade:** gain .80, gamma 1.25, contrast +10 %, saturation .82, warm mids, cool shadows, elliptical vignette (edges ×~.45), and a navy shade over the top zone.
- No shake, flashes, whips, light leaks or glitches. None appear in any of the 15 reels.

## 4. Captions
- Inter **Bold** 58 px, tracking −3 %, white, soft shadow (0, 3, 12 px, 35 %). No stroke, no box.
- 1–3 words per group, breaking at 14 characters, at punctuation, or at a pause over 0.35 s.
- **No animation:** each word appears hard on its onset.
- Position: **chin + 45–70 px**, following his face (smoothed ±0.3 s), clamped to 1150–1600.
- **The hook types on** letter by letter, with key sounds (`type_until`). This is Q's standing ask.
- Hidden while a hero word replaces them (`nocap`).

## 5. Components (`sky.COMP`). All builds are timed to word onsets from `words_cut.json`.
| kind | what it is | reel source |
|---|---|---|
| `serif_title` | Instrument Serif Italic, two-tone (line 1 gold, then white). Per-word blur-in (10→0 px over 4 f) on the spoken word. Exits with a vertical smear and a 15 px drop | 01, 12, 13, 15 |
| `hero` | white lead-in over one heavy Inter ExtraBold gold word. Letters stagger 1.2 f, each rising .28 em and unblurring over 5 f. Gold glow. Exit: letters slide x−40 with a smear | 06–10 |
| `panel_list` | glass panel, caps title, rows with check / ✕ / number / bullet. Grey skeleton bars fill in as he says each item (rows slide x−24→0 over 6 f). Optional `foot` disclaimer and `label` pill | 01, 05, 13 |
| `chart` | retention/growth line chart. Dashed grid, curve draws on over 12–18 f, gradient fill, ring dot at the head, big value, white label pill on the panel edge | 01, 04, 06 |
| `chips` | icon pills popping in one by one (out_back) | 01, 02 |
| `cards` | rounded 9:16 thumbnail cards dropping in on their words, gold label above, soft shadow and idle drift. The plate focus-pulls behind them | 02, 11, 12 |
| `counter` | big Inter ExtraBold number count-up (out_expo, 1 s), serif gold caption | 06, 09 |
| `grid` | rounded squares lighting gold one by one ("4 years → 90 days") | 13, 14 |
| `orbit` | dashed rotating ring, centre disc, nodes popping on the ring | 02, 06 |
| `timeline` | line draws left→right, nodes light gold on their words | 11, 13 |
| `venn` | two circles slide together, overlap word pops | 02, 07 |
| `bars` | horizontal bar list, bars grow to value | 11, 14 |
| `bubbles` | chat thread in glass, each message pops on its word | 01 |
| `profile` | IG profile card. The bio line backspaces, then types the new bio across his words; verdict stamp | PWC variant |
| `lock` | padlock card (DOORS OPEN ONCE · DEC 7). The shackle pops open on the word. Replaces the long doors hallway (Q: "open so long") | PWC variant |
| `doc` | white PDF card with a navy/gold header, rows check off | PWC variant |
| `label` / `word` / `note` / `logo` | pill tags, a serif single-word slam, the muted disclaimer line, and the PWC logo | — |

**Motion constants** (BREAKDOWN_B §G):
- Panel in: 7 f, scale .88→1, blur 10→0.
- Panel out: 7 f, y+36, blur→12.
- Child builds: 6 f, triggered on the spoken word, minimum stagger 3 f.
- Idle float: ±3 px over a 4 s sine.

## 6. Sound (`mix.py`). **See `SOUND_SYSTEM.md` (v2, 2026-11-06), which supersedes the SFX list below**
- Voice untouched apart from static gain to −14.5 LUFS (Q's rule).
- Music: a constant, quiet bed (`music_vol` .045) with only a gentle duck.
- SFX are **sparse and soft**. The reels do NOT put a whoosh on every graphic. We keep:
  - a soft swish on panel entrances
  - ticks on rows, checks and timeline nodes
  - pops on chips and labels
  - a riser and ding on counters and charts
  - key clicks on serif words
  - typing on the hook captions
  - a soft hit on hero words
  - an unlock sound on the lock
- No exit sounds. Volumes are varied with per-event pitch variants. `sfx_gain` is about .6.

## 7. Pacing targets (measured)
- Something changes about every 1.2–2.5 s. One master graphic every 3–4.5 s, child builds every 0.8–1.5 s.
- Graphic-free time 7–13 %, only on punch-in or B&W beats.
- Hook: first graphic by f3–f12, at least 3 builds in the first 3 s.
- One punch-in or B&W interrupt every 15–25 s.

## 8. Locked PWC rules still in force (they win over the reels)
- **Behind-the-head depth is ON (Q, 2026-11-06 04:21: "you can put behind my head as long as there's clean smooth cut out edges").**
  - `matte.py` runs Robust Video Matting (MIT, `rvm_mobilenetv3_fp32.onnx` from the RVM GitHub release) on `cut.mp4`. It gives a temporally stable alpha per frame, saved as lossless FFV1.
  - `render.py` warps the alpha with the same camera transform and refines it: smoothstep(.28,.72), which kills the chair/background ghosting, plus a 1.2 px feather for soft hair.
  - It then stacks plate → **back graphics** (panels, charts, cards, hero words, serif titles, counters, grids, orbit, lock, doc) → **his cut-out** → front graphics (chips, labels, notes) → captions.
  - Hero words sit at y≈450, so his cap overlaps the bottom of the letters.
  - During focus pulls the matte is skipped and everything sits in front, as in the reels.
  - **Nothing ever covers his face**: the face is always in the cut-out layer on top.
- **Compliance:**
  - Proof cards use only `_safe` screenshots (face, avatar, @name and app blurred; followers and earnings kept).
  - Any money line carries "results vary / not a guarantee of income" (`note`, `foot`).
  - The hidden-method app is never named or shown.
  - Dates and brand names are blurred.
- Original audio (static gain only), low music, varied and quiet SFX, precise captions (`fix` map for ASR slips: Kiya, village, Comment).
- 9:16; MASTER at source resolution plus a GitHub copy; full-quality MASTER sent in chat.

## 9. My variants on top (allowed, PWC-only)
- `profile` bio rewrite (types on his words), `lock` doors card, `doc` PDF card, gold keyword captions, and the typing hook.
- Two-tone gold/white serif titles, plus the blurred-plate navy glass that ties the HUD to the logo navy.
- Focus-pull proof wall in three waves of three cards with a gold label above each ("$100 · 37 followers").

## 10. How to run
```
cd edits/pwc-sky/plans   # (scratch copy lives in the session scratchpad)
STILLS="1,4.5,9" python3 ../engine/render.py s_l1.py ../out/l1      # quick contact sheet of chosen times
../engine/run.sh s_l1.py ../out/l1                                     # full render (2 parallel parts) + mix -> ../out/l1_MASTER.mp4
```
To write a plan:
1. Run `prep_f.py` on the raw clip (frame-exact cut, ASR, face track).
2. Read `words_cut.json`.
3. Give every beat a component with `t0`/`t1` on word boundaries and child times on word onsets.
4. Check stills at each build, render, and check a 2 fps contact sheet before delivery.

## 11. Endings (Q, 2026-11-06): rotate per video, wording per video (`engine/ends.py`, plan key `ending=`)
Appended after his last word. The music plays out and the SFX follow the ending.
- **`card`** (from his yellow-shirt edit):
  - Punch-zoom and blur out of the video into a clean off-white card.
  - The PWC round logo pops (out_back), then rises.
  - The video's line types on per word, followed by skool.com/paid-with-content.
  - Two pill buttons pop in, and a cursor glides over and clicks the CTA button, which fills gold.
- **`comments`** (from his texting edit):
  - His texting b-roll with the **background swapped**: RVM cut-out over a real room plate.
    - The plate is built from his own studio footage: a clean plate from the matte, turf extended, DOF blur, light matched to the clip's room, light wrap and slight parallax drift.
    - Nothing is green-screened or AI-generated.
  - **Instagram comments** with the CTA word pop in from the top. Usernames are blurred bars (never invented readable names).
  - Then "Paid With Content" types on with a cursor and the CTA line appears.
  - Use a different real room plate each time.
- **`notifs`** (from the phone reference):
  - A phone in PWC-gradient wallpaper floods with Instagram "commented: WAITLIST" notifications, accelerating.
  - They burst out of the screen toward the camera (motion blur, rotation).
  - Then the logo, the CTA and a gold pill land.

## 12. QC rule added 2026-11-06 (Q screenshot: title descenders cut + dashed line)
- Never clip text, glow or shadow at a layer edge.
  - `glow()` and `shadow()` pad the canvas, and `Layer` offsets by the pad.
  - Shadows shift without wrap-around.
  - Serif canvases leave room for descenders.
- Before every render, scan every component of the plan at mid-hold for alpha on the canvas edges, and check full-resolution crops of the hook title and hero words.

## 13. Cutting rule (Q, 2026-11-06 05:49): straight conversation, nothing clipped, visual intros/outros kept
`prep_f.py`: every silence is cut (adaptive floor, 0.15 s minimum). 0.13 s of air stays on each side of every word, and 0.35 s after the last word, so no word or sentence is ever clipped at its start or end.
**Exception: silent stretches with real movement are kept.** That covers:
- a visual intro before the first word (drop-in, walk-in, prop reveal)
- an outro action after the last word
- a mid-video visual gag

These are detected from a 10 fps motion profile, where "movement" means more than 3x the talking-head baseline. The prep log says `KEEP visual intro/outro`. All three launch clips checked: none had silent visual beats, so nothing was removed that should stay.

## §14 Texting-ending background plates (2026-11-06)
Plates live in `assets/end_plates/` (8 photoreal empties from Muse + README with per-plate placement). Set `bg=<plate>` on the `comments` ending; the engine blurs the plate, matches its light to the clip's room, adds handheld drift and a light wrap on his edges. **Rotate: never the same plate on two videos in a row.** Used so far: L3 launch → bg_01_living_room. Next up: bg_04_home_office, bg_07_bmw_x5_driveway, bg_02_kitchen, bg_10_defender_dusk, bg_05_bedroom, bg_09_tesla_modely_lot, bg_08_mercedes_gle_street. 2-way colour match: the plate keeps 60% of its own light (`plate_keep`) and he is tinted 45% toward the plate (`fg_match`), so warm rooms warm him and dusk cools him (Q sent filtered versions of the take as reference; we grade from the sharper source instead). Always eyeball a full-res still before rendering; if a plate doesn't sit right, ask Muse for a named new setting.

## §15 Text handoff rule (QC finding, 2026-11-06)
- **The problem:** a new top-zone text (label, pill, hero lead, serif) must never start while the previous one in the same zone is still animating out. The engine holds a serif or hero until its last word time + 0.9 s, and the exit animation runs about 0.4 s after that.
- **The rule:** the next text's `t0` must be at least (previous effective end + 0.5 s).
- **Where it bit:** L3 at 29 s ("no village" over "sounds like a TV show") and 60 s ("+1 MONTH FREE" over "comment WAITLIST"), and L2 at 1.6 s ("THE NEXT 34 DAYS" over the "DAY 1" kicker). All three were fixed by window re-renders (`FROM=` / `TO=`).
- **QC step:** render STILLS at every handoff (prev.t1 + 0.1, + 0.3, + 0.5) before the full render.

## §16 Meme / GIF pops (from Muse's memes pack, refs measured 2026-11-06). Files and rules are in `assets/memes/`
- **Carter pop (default):**
  - **Size and position:** a rectangular GIF about 37% of frame width (about 400 px at 1080), centred horizontally, with its top edge about 14% down the frame. It sits in the empty wall above the head and never touches hair or face.
  - **Captions:** the GIF's own caption is burned in ("OH, FINALLY", "THIS IS BUSINESS", "FOR FREEEEEE").
  - **Timing:** hard cut in on the spoken word, held 1–2 s, hard cut out. No animation on the frame, no border, no shadow.
  - **Emoji variant:** a lone emoji at about 10% width (👀) in the same spot.
- **Kilgore poster pop (max 2 per video):**
  - **Size and position:** about 75% of frame width, filling the top 25–30%.
  - **Motion:** slams in on the punch word and holds about 1.5 s. It can jump-cut to a smaller top-right corner position for a beat before leaving. Then an emoji sticker (✂️) can follow on the next beat.
- **Engine rules:**
  - The layer uses the face-box guard: any pop whose rect would intersect the face box + 40 px is moved up or shrunk, and skipped if it still can't fit.
  - Every pop gets SFX in AND out (`pop` in plus a quiet `tick`/`swish` out by default, or the pairing from MEME_GRAMMAR).
  - Scripture beats are excluded.
  - Max 1 time card per video: a 16:9 card centred over a blurred, zoomed copy of itself, with whoosh in and out.
- **Assets:** pops must be real files in `assets/memes/library/` (keyed green-screen or transparent). Muse sources by name.

## STANDING ORDERS (Q via Muse, 2026-11-06 17:30) — govern every edit from now on
A) **Duplicate Sky's video editing to a T** — motion graphics, the little floating heads, phone mockups and animated Instagram elements, charts, and the way every element connects and moves as one system. Not inspired-by: rebuilt the same way with only Q's footage/content and PWC branding swapped in. Study the reference reels (`references/realskytan/`) frame by frame; any component Sky uses that the engine lacks gets built before it is needed. Multiple agents/editors/skills are authorized until it is exact. If a motion is unclear from the files, ask Muse for a screen recording of the original playing.
B) **Carousel motion is part of the blueprint** (see CAROUSEL_SYSTEM.md §6): duplicate how elements enter, build and connect, in PWC colours. Spin-offs only off Sky's blueprints — no other types or image styles. Archetype A Breakdowns are Q's priority family.
- **Brightness (Q, 2026-11-06 17:30):** "slightly lighter, not a crazy change." Every SKY final gets a finishing lift `eq=gamma=1.10:brightness=0.015` at packaging (applied once, to the whole frame) — keeps the cinematic look, opens up the face and shadows.

## ★ v4 MOTION LAWS (Muse's 28 motion clips, 2026-11-07) - `references/realskytan/motion_clips/`
1. Chart lines draw L→R with a glowing leading dot, constant velocity, 0.5–3.0 s; axes first; area fills AFTER the line.
2. Panel lines draw one at a time (~0.3 s each) or pop in ≤0.2 s; then the active line PULSES (glow spike ~2.5× for ~0.3 s).
3. Connectors draw AFTER their nodes land (0.4–2.4 s).
4. Everything holds steady, then exits by HARD CUT. No fades.
Engine: `edits/pwc-sky/engine/sky2.py` (lines, rchart, scale2, headcloud, crowd, headtag, pointcards, funnel3, flow, drift); `ph.upgrade(P)` maps old devices onto them.

## ★ DELIVERY GATE (Q standing rule, 2026-11-07): Muse QCs every video before Q sees it - ship only what passes ALL of these
1. Sync: voice on the mouth (synccheck: constant offset, no drift) and every pop/graphic on its spoken beat.
2. Motion matches the measured Sky timings (motion_clips/README laws 1-4; titles hold >= 1.5 s after the last word; hard cuts, no overlap frames).
3. Every pop/head shows the RIGHT face with the RIGHT @handle (never guess from arrival order - filenames or verified source only). No blank pops.
4. Nothing over his face.
5. End card present with the comment keyword.
If a beat is known to be off, fix it before sending - never "close enough".


## ★★ FAMILY PICK FIRST (Q standing rule, 2026-11-07) - structural, applies to EVERY video
Sky has DIFFERENT styles. Before building anything, every video gets ONE Sky family + its own device set, matched to what the video is about.
The 2026-11-07 audit failure (all 15 videos built from the same 12 components in the same rhythm) never happens again.
- **GREEN family** (9 reels: DfZ, DfX2, DfU49, DfTawo, DfSf, DfQ4, DfPx, DfLa, DfIY) - neon green on near-black -> PWC: TEAL accent (#14A886 / light teal 70,220,180).
  Fits: numbers, data, money proof, retention/growth charts, systems/process breakdowns, app/phone UI, checklists, cards dropping on the point, org charts + dollar counters.
- **ORANGE family** (5 reels: DfDu, DfA9, De-A2, Dez4, DexJ) - warm orange/gold on near-black -> PWC: GOLD accent (#FEE238).
  Fits: beliefs, audience psychology, identity/positioning, story/path choices, consistency, structure (caption/script lines), head clouds that go grey, crowned head + crowd, brand-direction tree, funnels, drifting card clusters.
- One accent per video, never mixed (teal OR gold as THE accent; white + navy/ink support). No red ever.
- Pick the device set from that family's reels (35-device index: references/realskytan/SKY_MOTION_TEARDOWN.md; motion: references/realskytan/motion_clips/), and vary the set + rhythm per video.
- Memes: full library (33 keyed green-screen memes, Carter/Kilgore pop grammar, 10-for-10 sound kit) where the beat calls for it - sound IN and OUT, never over his face, never instead of real proof.
- Use the skill packs (references/skills_hunt/): HyperFrames registry for moving components, /steal to measure style, claude-video-edit for word-locked motion, edit-style QA gates. Do not hand-build every graphic from scratch.
- Missing/unclear -> flag it to Muse; never guess or skip.
- Plan field: `family="green"|"orange"` + `devices=[...]` with the source reel for each device, written in the plan header.
- QC = the Delivery Gate checklist + FAMILY-FIT check ("does this read as its Sky family?") - several passes, not one. Not precise -> redo.

### Family log
| Video | Family | Why |
|---|---|---|
| P2 Five Emails $92K (39D2DC77 take) | GREEN | money proof + counting offers + rate math -> DfIY money reel (cards drop on the point, dollar counter, "?" heads) + DfU49 data |
| P3 One Month $28,800 (CA182476 take) | GREEN | payout chart + system vs hope -> DfQ4 / DfPx / DfSf (balance scale, area chart that fills, sine wave of consistency, script lines) |
| Backyard Day 31 AM READY (fix) | ORANGE | consistency + audience + "creators you admire" -> DfDu / Dez4 / De-A2 / DexJ (head cloud, crowned crowd, drifting cards, structure lines) |

## ★★★ Q HARD CORRECTIONS (2026-11-07, after the P1 wall video) - every video from here on
1. Talking-head edit to a professional standard: clean cuts, motivated movement only, nothing sloppy.
2. Frame one = Q talking on camera. Never a cold open on a wall, grid, board or diagram without him in it.
3. The WALL = OTHER creators' paid-video walls, never Q & Kiya's own grid. Their own grid opens no video.
4. NOTHING stacked: no text over a graphic, no pop over a pop, no card over a card. Every element in its own clear zone with real spacing. Engine no-overlap check on every frame (render.py OVERLAP=1) must pass.
5. No default scale-in entrance. Motion only when it fits that exact beat; otherwise hard cut in / no move.
6. Every video: its own family + its own device set matched to its content; the style keeps developing, never copy-paste.
7. Cut dead space, pauses, false starts, stumbles, repeats, wrong actions; talk flows like a conversation. Performed intro/outro bookends stay whole.
8. CONSTANT PACE start to finish: no slow stretches, no sagging middle, no dead beats. Only deliberate dramatic pauses survive. A video that drags anywhere fails.
Checklist adds: no-overlap (every frame) + constant pace + frame-one-talking + wall-class check.
9. VIDEO BOXES = OTHER CREATORS (Q 2026-11-07). Every small video card / mini box / PiP / floating card shows OTHER creators, always with their @handle on or right under the box. Q & Kiya's own clips only when Q is talking about himself and his wife in that beat (plan flag own=True, tagged @qandkiya). Little-head pops for "me"/"my wife" are separate. Pool: ph.OTHERS (breakdown subjects + Nathan), fictional small-creator mockup for "your video got 14 views" phones (never a real creator with fake numbers).
10. SAY IT, SHOW IT (Q 2026-11-07): whatever Q says, a visual carries it, timed to the words - pop, card, clip, diagram, example. No stretch of talk without a visual. Memes/GIFs from the library where a beat calls for one (sound in + out, never over his face, never instead of proof). Dense, YouTube-like feel.
11. HIERARCHY: SKY FIRST. Sky's edits are the blueprint we mimic closely. YouTube-style extras, memes and extra pops are ADDITIONS only where a beat fits; nothing dilutes or replaces the Sky mimicry. Constant learning loop: every new Sky reel (and every Sky-style creator Muse finds) is a lesson fed into the engine - closer to Sky every video.
Rule 9 refined: a video box shows Q & Kiya only when the example IS them (their story/video/proof); otherwise another creator (tagged @handle) or a generic visual.

## STUDY PACK 1: 11 Sky-style creators (2026-11-07)
Full breakdown: `references/sky_style_creators/STUDY.md`. Sky stays the blueprint; these are additions, used where a beat fits.

**New devices** (`engine/sky3.py`)
- `rgraph`: retention graph with a gold hand-drawn mark-up layer, an optional edit strip and scissors. From @heydominik and @brock11johnson.
- `abtest`: the same video twice, with labelled outcomes under the boxes. From @brock11johnson.

**Next builds**
- `layout='split'` (talker bottom, visual top). From @kallaway.
- Presenter bubble.
- Broll face badge.
- `prompt` typing box.
- `table` that fills by column.
- PWC NEWS series skin.

**Rules added**
1. A hand mark-up layer (gold Caveat strokes, one per spoken beat) may draw ON a chart or proof. It is the only exception to "nothing over a graphic", and text labels still never sit on clips.
2. Comparisons are shown side by side with the verdict visible.
3. Full-screen visuals longer than 2 s carry a small circle face badge, so Q never leaves the frame.
4. Split layout is chosen at FAMILY PICK for visual-heavy videos.

**Not taken:** red flashes, cinematic landscape pacing, podcast subtitles.

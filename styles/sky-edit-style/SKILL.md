---
name: sky-edit-style
description: Edit Q's talking-head teaching / proof-led / breakdown videos exactly like @realskytan (Sky Tan, https://www.instagram.com/realskytan) — one named framework per video that fills in on screen, word-by-word captions, glass panels, charts and devices timed to the spoken word — re-skinned to PWC teal/gold on navy. PAGE-LOOK RULE (Q, Nov 9, 2026): whenever Q says "edit this Sky style" (or any equivalent), the edit must make @yerrr__q look like @realskytan — Sky's exact editing on Q's content, indistinguishable from Sky's own posts. Trigger: "edit in Sky style", "edit this Sky style", "cut this like Sky", "Sky style".
---

# SKY EDIT STYLE — Claude skill — **SKY v6** (Batch 36: full-profile completion + premium purge)

**SKY-PLUS BAR (Q, Nov 12, 2026 — binding): "Sky exact is the floor. Ship better than Sky's
own execution of his system."** Exact duplication of Sky's system is the FLOOR, not the
target. Elevation runs on Sky's own axes only (timing precision, motion smoothness, sound
richness/density, visual polish, retention pacing), each PWC target derived from Sky's own
best-measured instances — never invented, never drifting into generic patterns (the
BANNED-TELLTALES list below governs). Grading: an edit passes only if it grades AT-OR-ABOVE
the Sky reference on fidelity AND ABOVE it on execution quality.

**BEAT-LOCK (Q, Nov 12, 2026 — binding).** Everything on beat — captions, motions, visuals,
visual motions, sounds, transitions. Every planned event sits on the take's own beat grid
(word stresses from word timings + detected music beats where a bed exists) within
**≤1 frame (≈0.033 s)**; a deliberate off-beat carries a stated `off_beat_reason` in the
plan or it FAILS validation (`validate_beat_lock` / gate P10). Full spec:
`STYLE-GRAMMAR.md` §5 + Batch 36 `synthesis/BEAT-LOCK-SPEC.md`.

**FRAMING + GRADE + NO-B&W (Q, Nov 12, 2026 — binding; Q's verdict after watching the
1-11 v7 build):**
- **NO BLACK AND WHITE.** The video never desaturates. D21 (B&W beat) is a real measured
  Sky device and stays in the teardown/examples, but it is BANNED in the Q lane —
  validator-enforced (`Q_LANE_BANNED_DEVICES` + the `desaturate` motion ban). It is not
  in the examples Q chose for his lane, and he does not want it.
- **NO TIGHTENING.** The A-roll stays at the take's own framing (1.0×). Never scale the
  subject up to reframe; a plate may SHIFT (e.g. drop) only without scaling him larger.
  Punch-ins are never sustained and never make him closer than his own closest source
  framing. If the take is tight, the edit lives with it — it does not push in further.
- **GRADE WITH A LIGHT HAND.** No background blur, no crushed "cinematic" darkening, no
  vignette crush. Sky's room in his posts is dim but READABLE — furniture, wall and set
  stay visible. Match that level; never blur or darken the background past it.
- These three (B&W, scale-up reframes, over-grade/fake blur) are named residues of the
  generic "Claude AI look" Q is rejecting: the standing push is full Sky adoption —
  if a treatment has no measured instance in Sky's posts, it does not go in Q's video.
- **POP-UP PRECISION + VISUAL DENSITY/MOTION (Q, Nov 12, 2026 — binding).** Pop-ups land
  PRECISELY on the spoken word (and the gesture — pointing, looking, movement) they
  illustrate: frame-precise, beat-locked, graded per pop-up in QC (landing vs its
  trigger word, in frames). And MORE visuals, MOVING like Sky's: exhibits build, count,
  stagger, travel and land — nothing arrives as a static stamp. Visual cadence holds
  Sky's measured density (a visual event every ≤2 s; graphic swaps ≈ every 10 s per
  section) without inventing devices that have no Sky instance.

**COVERAGE (Batch 36, measured).** Reels **49/49** decoded (15 priority + origin + 33
Batch-19); soundmaps **48 + 1** (48 per-reel maps + the DOTnacsDXvB duplicate covered by
DOWgvE0Ezgs' map, spectrograms SHA-identical). Carousels: **51/86 slides** frame-decoded —
all 51 video slides; the **35 image slides are missing** because Instagram's anonymous
extractor emits no image URLs (rate-limit/blocked; needs a live-browser or authenticated
pass — see Batch 36 `carousels/CAROUSEL-SYNTHESIS.md` §7). The 10 known carousels are
86 slides, NOT the old "9 posts / 51 slides, every slide a video" claim.

**Profile mastered:** Sky Tan — **@realskytan** — https://www.instagram.com/realskytan
**Status:** NOT YET GRADED. No Sky-style test edit has been frame-sequence graded against the
examples in this folder (see `QC.md` §6 and `GAPS.md`). Do not present any build from this
skill as "exact" until that grade passes.
**Supreme rule (Q):** copy Sky to a T. Only Q's footage/content, the PWC logo, and the PWC
colour scheme change. Sky's framework names, scripts, caption text, client stories and
figures NEVER transfer — Q coins his own framework names and runs his own numbers. The
*mechanics* are the steal.

**PAGE-LOOK RULE (Q, Nov 9, 2026 — binding, BOTH sides: Claude Code AND web).**
"I want my page to look like his page with edits everytime I say edit this sky style etc."
Whenever Q says "edit this Sky style" (or any equivalent trigger below), the edit must make
@**yerrr__q look like @realskytan**: Sky's exact editing, applied to Q's content, so Q's page
reads as Sky's page with Q in it. This is the STYLE FIDELITY BAR made concrete: the output
must be **indistinguishable from Sky's own posts** — the same editors, the same look — only
Q's words, Q's footage, Q's proof, and PWC teal/gold on navy (instead of Sky's green/orange)
change. When Q names Sky, there is no other style — Sky wins, full fidelity, no mixing with
other styles, no watered-down version on either side. This rule lives in the Claude Code
skill folder AND in the web skill (v4+) with identical wording — never Code-only.

**ULTIMATE FIDELITY BAR (Q, Nov 9, 2026).** *"I want no one to be able to even tell the
difference between our editing."* The grading question is one sentence — **does this read
as their style or as ours** — and the bar is absolute: NO ONE (not Q, not a viewer, not a
fellow editor) can tell Q's editing from Sky's. Grade every Sky edit frame-matched
side-by-side against a Sky model reel (see `QC.md` §6 and `STYLE-GRAMMAR.md` §0). Any
matched pair that reads as ours FAILS and gets REBUILT, never explained away. Per-word fit
audit on every caption and graphic word — one clipped word blocks delivery. Every required
element from the teardown must be present — a missing element fails even when technical
checks pass. Method: `reference_style_recreation` — tear down the source first (device by
device), replicate the WHOLE system (house template fully off), use real native assets,
apply Q's teal/gold override and the face-clear rule.

**PREMIUM SKY IS THE ONLY OUTPUT MODE (SKY v6 — Batch 36 premium purge, binding, BOTH
sides).** The Nov 9 "two options" arrangement is SUPERSEDED: the generic-fallback patterns
(former "Option 2") are REMOVED from this skill and its code (`code/sky_option2.py` deleted;
the validator rejects fallback-marked events). When Q says "edit this Sky style" (or any
equivalent trigger), the ONLY output is premium Sky — the measured grammar (D1–D56 devices,
~0.5 s caption groups, hard cut ≤1 frame, accent keyword as a separate large headline,
premium depth measurements) — and nothing else. There is NO fallback, NO second option,
NO generic Claude pattern in the path. If a device or pattern cannot be traced to a
measured Sky reel, it is NOT in the execution path. [EST] devices (D5 chapter card, D13)
are QUARANTINED by the validator — estimates never ship as "Sky"; use the measured variant
(D5-list) or measure the device first.

## BANNED TELLTALES — the premium purge list (SKY v6, binding)

Any of these in a Sky build = the cut FAILS, however clean the technical checks are:

- **Cheap / italic-serif fonts** — Instrument Serif Italic and any serif display/title/
  counter treatment in REELS (the single most recognisable AI-edit fingerprint). Reels are
  bold grotesque, hard cut-in. (Sky's own measured serif instances stay in the EXAMPLES as
  record; carousel serif in Archetypes B/E is carousel-only, measured, and stays there.)
  **EXCEPTION — Q RULING Nov 12, 2026:** Sky's newest reels run serif+bold HEADLINE
  LOCKUPS as standard grammar (italic serif word + bold grotesque keyword, batch-39
  measured). Q adopted the lockup in PWC colours: serif word white, bold keyword PWC gold
  #FEE238, teal structural accents. A lockup built to the batch-39 geometry is APPROVED —
  not a telltale and not a validator violation. The ban still covers every other serif use
  in reels (captions, counters, outcome text, generic serif display).
- **Transitions with no measured Sky instance** — invented wipes, zooms, slides, spins,
  generic fades. Only measured transitions ship (hard cuts; the measured motion-blur
  slides; D54's horizontal step slide; D55's blurred-slide handoff; the two measured fades:
  D2's 5-frame hook exit, D31's 10-frame count-up exit; DeYKk's single dot-grid fade +
  whip-blur instance, flagged as an instance).
- **Template title cards** — preset/generic title cards of any kind.
- **Static stamped overlays** — tilted sticker cards, stamped badges, anything pasted on
  and held without a measured Sky motion/beat.
- **Cheap-grade assets of ANY class** — cheap AI renders, cheap templates, cheap
  transitions, cheap sounds, cheap stock, placeholders, dummies, lorem, watermarks,
  low-res pulls. The ban is on CHEAP GRADE, not on AI: **premium AI is IN** — Higgsfield-grade
  AI images/video/renders/visual hooks and Fable motion work are first-class premium assets
  for illustration and visual hooks. **Proof stays REAL, always**: exhibits, profile
  inserts, proof columns, comment screenshots, view-count proof, subject photos and all
  payout/earnings evidence may NEVER carry AI provenance (validator-enforced).
- **Caption treatments off Sky's measured system** — no typing/letter-by-letter captions,
  no scale "pop-in" ramp, no karaoke highlight in the Df era, no serif captions, no boxed/
  pill captions. D1 is the system: 1–3 words, hard cut ≤1 frame (Dcc-era variant per §2).
- **Any device / visual / sound / motion without a measured Sky source instance** — if it
  cannot cite a reel + timestamp, it does not ship. Unmeasured ideas are listed as gaps,
  never coded or built.
- **Red anywhere in Q's lane** (palette law: teal #14A886 + gold #FEE238 on navy #00214E),
  neon green, Sky's raw green/orange/purple as emitted graphics colours.

**Enforcement is code, not vibes:** `sky_devices.validate_premium_plan()` (gate P9 in
`sky_qc.py`) rejects unknown/unregistered devices, fallback-marked events, banned
fonts/motions/treatments, cheap-grade asset markers, disallowed provenance, AI on proof
devices, [EST]-quarantined devices, and events with no Sky source citation.
`validate_beat_lock()` (gate P10) rejects off-grid events with no stated reason.

## Base rules — the cheap→premium layer (Alex's six, under Sky's grammar)

**Attribution — read this first.** These six base rules are **Alex's (@growithalex)**, from his reel https://www.instagram.com/reel/Dezhcs4CpRL/ (decoded Nov 9, 2026; full decode in `~/workspace/claude-editing/research/video-harvest/instagram/batch-14-sky-rules/DECODE.md`). They are the **base layer under Sky's grammar** — never present them as Sky's own rules. Sky's grammar (word-by-word captions, devices, frameworks) sits on top of them. Framing: *"That's what takes a reel from cheap to premium."* / *"Claude was never the problem. The missing rules were."* The full tutorial + Base Rule Skill file are gated behind a "Comment BASE" DM funnel — not chased, not included. The six rules below are the complete public rule set.

1. **"The hook lands in the first second."** The payoff or claim lands immediately. No slow open, no throat-clearing. (PWC: the claim/curiosity lands in the first second AND Q's face is on screen during the hook.)
2. **"One idea per shot."** Every cut carries exactly one idea. Never stack two ideas in one shot.
3. **"Captions 7 words a line, max."** Caption lines capped at 7 words. This caps LINE LENGTH — it does not replace Sky's word-by-word hard cuts (§2: 1–3 words per group).
4. **"One colour story per reel."** A single palette for the whole video. No colour drift. (PWC: teal #14A886 + gold #FEE238 on navy #00214E. NO red in anything added.)
5. **"Cut on the beat, not the word."** Picture cuts land on the music/beat. This governs PICTURE cuts — it does not override Sky's word-timed caption cuts.
6. **"Ease every move."** Every motion is eased. Nothing moves for no reason — no random text or motion. (PWC: eased entrances only; devices land on the spoken word they illustrate; PWC logo in every video.)

## Premium depth — frame-measured from Sky's own videos (Nov 9, 2026)

**What this is:** the premium standard, measured frame-by-frame from the 15 priority Sky reels on disk (`~/workspace/goals/realskytan-style-steal-for-q-s-content/hidden_files/priority15_videos/`, 01–15, H.264 720×1280, 30 fps) — not from text decodes alone. Every claim below is tagged **VERIFIED** (measured from the videos) / **[EST]** / **UNVERIFIED**, the same way `STYLE-GRAMMAR.md` does. Full specs + per-device values: `STYLE-GRAMMAR.md`. Measurement log: `examples/PREMIUM_DEPTH_MEASUREMENTS.md`.

**The three reels that were audio-only are now fully verified (G-02 CLOSED).** Dez4fPJCR74, DeYKkAIgVfL and DeSTWxcDTA7 were audio-only in the Nov 6 browser pass; all three now have frame-verified visuals, family and endings:
- **Dez4fPJCR74 = ORANGE.** Script-anatomy bar chart (Hook red / Lead yellow / Body blue / CTA green, loop icon on open-loop rows) + a thin orange L-shaped branch line + an orange-pill stack (Short-form Virality, Personal Branding, Content Systems, Full-funnel Content Ops, Content Formats, Hooks & Packaging) + a numbered step list + "$18,000.00" High Ticket Sales proof cards. Ends on Sky talking over the proof cards, no visual CTA. **VERIFIED.**
- **DeYKkAIgVfL = ORANGE.** Participation-loop = a dot-grid (audience) whose dots flip red (lose trust) → green (gain trust), with category labels (Community, Digital Product, Coaching, Course) + profile faces; the "affiliate army" = a dashed curved line connecting profile photos; D11 chip-cluster = orange dots in a dotted arc above the phone frame + a quiz card whose words accumulate as a vertical list; "100s of people" = a grid of many small orange squares. Ends on Sky talking over the Traditional vs Community-driven comparison, no visual CTA. **VERIFIED.**
- **DeSTWxcDTA7 = ORANGE.** Views-refresh insert = a 3×3 profile grid with per-video view counts (8,547 / 4,246 / 6,540) + "GOING VIRAL" labels above his head; a **B&W beat** = the frame desaturates to B&W with one big orange "DON'T" (a Sky device, not just a PWC invention); a "New Post" dashed placeholder card that fills with thumbnails; a floating head cutout (Sky's own face) that pops in; yellow emoji pops near the chest. Set = a chair with a ring light (not the desk). Ends on Sky talking, no visual CTA. **VERIFIED.**

**DfA9 ending + funnel now verified (G-03 CLOSED).** DfA9L-PHYWp ends on Sky talking over the sponsor/client comparison clips — no visual CTA, no spoken CTA in the last 22 s. Funnel device = a glass card, top-centre/left, rows (CONTENT → CHECKOUT PAGE / VSL) + a "FEEDS INTO BRAND" orange bar; recap = a numbered checklist (01 GOAL, 02 AVATAR, 03 MARKET, 04 OFFER, 05 FUNNEL) with checkmarks, top-right; profile card (347 posts, 177K followers) + trait chips (Hook-obsessed, Test-driven, Battle-tested, Relatable); script card with a moving magnifier/highlight. **VERIFIED.**

**Caption timing, measured (G-14 partially closed).** Sky speaks **3.93–4.73 words/sec (median ~4.3 wps)** across all 14 transcribed reels; median word gap **0.18–0.22 s**. Caption groups change every **~0.5 s** (at ~2 words/group) — this corrects the skill's old [EST] of 0.7–1.2 s. **Caption IN = a hard cut to full size in ≤1 frame (≤0.033 s)** at 30 fps — no scale-in ramp (measured on DfX2, "Absolutely." onset 19.78 s: the old caption is gone and the new one is at full size in the next frame). The OUT is ~0.5 s pop/fade (browser pass). **VERIFIED.**

**The accent keyword is a separate headline, not a caption highlight (G-01 RESOLVED).** Captions are all-white with NO highlight (verified in every reel). The accent word lives in a SEPARATE large headline device — "REACH", "Collab", "Viral Two", "DON'T" — the biggest text on screen (~15–20% of frame height). Q lane stays all-white captions; accent words are separate headlines. **VERIFIED.**

**Device geometry now verified.** D4 third verdict state ("Minimum") = a small "Minimum" text label on the right of the row — no icon, no strikethrough, row text normal (DfX2). D7 Venn = two overlapping circles ("Your audience" / "Their audience") with a solid GREEN lens in the overlap, faces in circles at the top of each circle, centred above his head (DfPxq). D6 charts = a STATIC base; the values update (1.1M → 2.6M → 2.7M) and annotations stack — the line does NOT draw on continuously (DfPxq, G-04 CONFIRMED). DfU49 narrative chain = a compact 2×2 grid of labeled pills with directional arrows (Spleen → Fluids, Phlegm ← Dampness); its autopsy labels are short 2–3-word labels with a ✓ for good moments (Throat mucus, Intentional drop, Hook filtering ✓, Bad drop, Basically flat ✓, Every line connects, QUICK TIP, INTERACTIVE EXERCISES, Stay to the end, Why herbs). **VERIFIED.**

**Colours, pixel-sampled.** Orange accent **~#F09828** (bright orange), consistent with the skill's #E8913F. White captions **#FCFCFC** (pure white). Ground **near-black #040404–#0C1414** (slight teal tint). Green: keep the skill's pixel-sampled **#40BB2F** (re-sampling was inconclusive — the accent is a thin line, not dominant in the frame). **VERIFIED.**

**What is still a gap.** D5 chapter-card parameters and D12 era-timeline mechanics are still [EST]. DfIYshekeF3's dismissal treatment and intersection-diagram geometry are still unverified. Font family identities are still UNVERIFIED. Zoom % is still a visual estimate (~5–10%). **Batch 36 additions:** the DeYKk pill system and the DeSTW UI-shrink are now coded (D55/D56); the tick-tone sound family is measured and annotated on the counter/timer/count-up/chart devices (see §1 E10). The skill is still **NOT YET GRADED** — no Sky-style test edit has passed the frame-sequence grade (see `QC.md` §6). Nothing is called "exact" until that grade passes.

## Trigger phrase

**"edit in Sky style"** — also fires on: **"edit this Sky style"**, **"cut this like Sky"**,
**"edit this in Sky"**, **"Sky style"**, "like Sky", "@realskytan", "Sky lane", "make it like
his videos", "Sky protocol", and any equivalent Q uses. Every one of these triggers the
**PAGE-LOOK RULE**: the edit must make @yerrr__q look like @realskytan — Sky's exact editing
on Q's content, indistinguishable from Sky's own posts. When Q names a different creator's
style, use that style's folder instead — never blend styles in one video. When Q names Sky,
there is no other style — Sky wins, full fidelity (premium Sky is the only mode in v6).

## When to use it

- Q films a teaching, doctrine, proof-led, breakdown, or launch talking-head and the video
  teaches **ONE named system** (a Filter, a Fit, a Stack, a Split, an Anatomy).
- Proof-led videos (money math, payout charts, system-vs-hope), breakdowns/reactions of a
  real third-party reel, launch announcements, flagship script/system lessons.
- Every framework reel gets a **carousel twin** from the same device states (see §6) —
  carousels are ALWAYS Sky's form; this folder is the carousel authority too.

## When NOT to use it

- Couples content (Q + Kiya page) — different lane.
- Pure story/vlog with no system to teach, or a video whose power is a single emotional
  beat (use Form 12 confessional *pacing* only, not the Sky device set).
- Yapping / avatar videos — different style folders.
- If there is no named framework and no proof asset for a part: do NOT force Sky. Merge
  the part, cut it, or ask Muse for the asset. Never ship a claim bare.

## 0. Family pick FIRST (structural — before any build)

Sky has TWO families. Pick ONE per video and never mix accents in one video.

| Family | Sky accent | PWC accent | Fits |
|---|---|---|---|
| **GREEN** (9 of the 14 teardown reels) | neon green #40BB2F | **TEAL #14A886** (structure: titles, numerals, outlines, keep-verdicts, diagram structure) | numbers, data, money proof, retention/growth charts, systems/process breakdowns, app/phone UI, checklists, cards dropping on the point |
| **ORANGE** (5 of the 14 teardown reels) | warm orange/gold #E8913F | **GOLD #FEE238** (payoff: figures, completed state, swapped power word, payoff word) | beliefs, audience psychology, identity/positioning, story/path choices, consistency, structure lines, funnels, drifting card clusters |

- One accent per video, never mixed (teal OR gold as THE accent; white + navy/ink support).
- **NO red ever, NO neon green ever.** Sky's red X / red negatives remap: strikethrough stays,
  X goes **gold**, check goes **teal**, rejects/dismissals go grey + strike/dim.
- Plan header must state: `family="green"|"orange"` + `devices=[...]` with the source reel
  for each device. A video built from the same 12 components in the same rhythm as the last
  video is a fail — vary the device set + rhythm per video (variety rule: each device ≤2 uses
  per video).

## 1. The recipe (E1–E10 + pre-production)

**Pre-production:** P1 coin the framework name (2–4 words, ownable) before the shoot; P2 list
its parts (3–6; 4–5 is the sweet spot); P3 pre-select each part's example asset (real screen,
clip, figure, or rewrite pair — a part without an asset gets merged or cut); P4 write the hook
from one of the four formulas (§4) and the close as the framework's completion line + door;
P5 draft the post caption's two-door version BEFORE the edit and confirm the keyword's
ManyChat flow is live or scheduled live before posting. **No live flow = the video is held.**

**Shoot:** medium shot, face upper-middle, empty space above the head and at the chest band
reserved for devices. Dark/quiet background. Deliver part-by-part with a breath at each
boundary.

**Edit (CapCut native only — see `code/README.md`):**
- E1 A-roll on Track 0. Silence-compress to Q's flow standard (inter-word gaps ≈0.15 s,
  dramatic pauses rare) BEFORE graphics, so every device timing is built on the final cut.
  Keep performed visual intro/outro bookends whole.
- E2 Captions: Auto Captions → re-segment to **1–3 words per group** → locked Q Sky-lane
  caption style (§2) → chest band, face-clear. (Df-era default. Dcc-era variant — origin
  reel Dcc84V5jc6D, Batch 18 — is 2–5 words/group with the accent word in gold INSIDE the
  caption; use it only when the video names template beats/figures that way, never mixed
  with the Df-era variant in one video.)
- E3 Hook headline (D2 lockup or D3 title stack) lands **with the first spoken line**.
- E4 Build the hero device — pick ONE primary: D4 board / D5 index / D6 chart / D12 timeline /
  D13 strip. Place it in the top stack (y ≥ 300) or a face-clear side zone. Set every part to
  its pending state (40% opacity).
- E5 Walk the timeline part by part: at each part's first spoken word, fire its state-change
  (opacity 40→100% over 0.15 s + its device animation) and insert its example asset on the
  overlay track at the exact claim word.
- E6 Punch-ins: keyframed A-roll scale at the definition line, each part's verdict line, and
  the close — **capped at 105–110%**, returning to 100% at the next section boundary. Sky's own
  zoom is mild, ≈5–10% MAX (VERIFIED). Hard cuts stay rare and structural. Never punch in on a
  graphic state-change frame (one motion at a time). Face-clear at every punch scale.
  Punch-ins are per-reel, never assumed: the Dcc-era origin reel Dcc84V5jc6D (Batch 18) is
  ONE locked-off take — zero cuts, zero zoom, zero punch-in over 54.2 s.
- E7 Mid-video reset at 45–55% of runtime: pivot headline, the chart's second act, a document
  reveal, or a branch.
- E8 Figures: every number that is *argued* (not just mentioned) gets a figure state (D6/D7
  count-up or landing). Numbers land on the spoken digit, never before it.
- E9 Close: complete the hero device (final state-change) *on* the closing line; hold the
  completed state 0.8–1.5 s; spoken door (keyword/follow) over the completed graphic; Q's
  logo/keyword end moment **≤ 1 s after the last spoken word**.
- E10 Sound (CORRECTED GRAMMAR, Batch 36 — 48 measured soundmaps): Sky's base is **dry
  voice only** — music bed ABSENT in every measured talking reel, ordinary edit SFX
  (whoosh/pop/riser/ding) **0 confirmed corpus-wide**. The one designed-sound family is
  the **TICK-TONE**: faint gated fixed-frequency pulse trains at exactly **5,926 Hz**
  (~13–17 pulses/s) riding counters, timers, count-ups and chart draws, plus gated tones
  (~9.15 kHz; ~11.1+11.85 kHz two-tone) at two graphic landings (instances in
  `STYLE-GRAMMAR.md` §7). The old "low drone synth intro" claim for DP4r6BbEvHg is
  **REFUTED** by Batch 36 gap measurement — it was voice fundamental + room tone; never
  cite it. Q DIVERGENCE (SKY-PLUS target): cleared bed ducked ≈ −28 dB; sound on **100% of
  device entrances AND exits** from the licensed library (Sky lands some devices silent —
  e.g. DevpJZLk6Km — PWC's target is his best density, everywhere); stamp sound on verdicts.
  No device appears or leaves silently. DJccT_xSWuT's isolated UI blip (31.26–31.68 s) is
  an instance note on D51, not a device.

## 2. Captions (D1 — the constant)

- White sans-serif, never a full sentence. Bare text, no box, no pill. **Group size:
  talking-head reels = 1 word per group** (batch-39 measured, Nov 12 2026 — Sky's current
  cadence); other forms 1–3 words per group per the registry.
- One weight per video: **bold** (doctrine/teaching) or **light/regular** (process/casual).
- Size: cap height ≈ 50–62 px at 1920 (CapCut font ≈ 54–64 on a 1080-wide canvas).
- Position: centre-lower, chest band, chin + ≥40 px clearance, inside the IG safe zone
  (x 70–930, y 280–1480 on 1080×1920). **Never over Q's face, never above y = 280.**
- Motion (VERIFIED, 30 fps frames Nov 9): **hard cut in to full size in ≤1 frame; out ≈ 0.5 s pop/fade.** One word/group at a time,
  hard cut per word; previous group fully gone before the next lands.
  The old caption "pop in" scale ramp is a BANNED telltale in v6 (removed fallback) —
  never use it.
- **Q lane captions — TWO approved modes (Q RULING Nov 12, 2026, refining the line above):**
  (1) all-white groups (the measured default in Sky's own captions across the decoded
  corpus — no current-word highlight on his own captions in any reel watched, VERIFIED;
  highlight fires inside *embedded* content: client captions; rewrite lists: new word
  gold / old word grey in Q's lane; see `GAPS.md` G-01); (2) **white lettering with
  colour-highlighted keywords**, as in the Sky videos that use it — Q approved this mode
  explicitly ("it's ok also to do it like sky videos... where it's white lettering but
  then color highlight words"). Q-lane highlight colours: **yellowish gold like the PWC
  logo (#FEE238), teal #14A886 at times** — never Sky's green/orange in the highlight
  slot. Pick ONE mode per video and hold it; never double-treat a word (a highlighted
  caption word does not also get a giant headline of the same word at the same beat).
- **Fonts (Q RULING Nov 12, 2026):** adopt MULTIPLE viral fonts the way Sky does — he
  varies typefaces across videos; each adopted font carries ITS effects and movements
  from the measured instance (entrances, pulses, type-ins), not a generic animation.
  One video = the font system of the Sky system it models; variety lives across videos,
  not as random font mixing inside one cut.
- **Dcc-era variant (Batch 18, Dcc84V5jc6D, Aug 25 2026 — predates the priority reels):**
  caption groups are **2–5 words** (median ~0.6 s, range 0.33–1.28 s) and the accent word
  lives **INSIDE the caption in gold** — on (a) the hook accent, (b) the current template-beat
  name, (c) key figures — everything else white. Speaking rate 4.81 wps (above v3's
  3.93–4.73). Era difference, NOT a v3 correction: v3's 1–3-word all-white rule stands for
  the priority-reel era. Use the Dcc variant only when Q's video names template beats/figures
  the way this reel does, and never mix both variants in one video. Code:
  `d1_captions(..., era="dcc", gold_words=[...])`.
- **Dcc-era caption-vs-speech decision (FIX Batch 18 QC F4):** Sky's on-screen captions
  diverge from his speech at three beats, frame-verified — ~9.2 s on-screen "Because think
  about it" vs spoken "Because the thing about it"; ~9.4–9.5 s "Any good real" vs spoken
  "any good reel"; ~10.0 s "is going to" vs spoken "is gonna" (full table in
  `examples/batch-18-sky-origin/EDIT-TEARDOWN.md` §4 and `DECODE.md` §7). **DECISION:
  captions follow the SPEECH (`words.json`), not Sky's on-screen text, in both eras.**
  D1 is the speech caption stream; the divergences read as Sky typos/paraphrase, and in a Q
  recreation Q's own speech is the source of truth — his captions must match what he said.
  The on-screen readings are the documented deviation (a frame-exact Sky clone could
  reproduce them deliberately). No code change: `caption_groups()` / `d1_captions()` already
  take the speech transcript.
- The hook types on letter by letter (Q's standing ask). No caption group may sit across a
  device state-change — re-segment so the group boundary and the device beat coincide.
- Words never clipped: cuts land on sentence boundaries or device beats, only in silence with
  the full word envelope surviving. One clipped word = internal fail, blocks delivery.

## 3. Devices D1–D56 (CapCut-native builds — full specs in `STYLE-GRAMMAR.md`)

D1 speech caption stream · D2 mixed-scale headline lockup (kicker 30–34 px + display 105–125 px,
holds ≈5 s, hard-pop exit) · D3 top title stack + item pill (title y ≥ 300 in Q's lane, pill
y ≈ 360–440; swaps ≈10 s each, hard swap + ≈0.3 s pop) · D4 filter board (rows judged one by
one, board fills = open loop; reject = strikethrough + gold X pop, approve = teal check) ·
D5 numbered chapter card 01–0N · D6 retention/views chart (STATIC base + annotations stacking
≈10 s apart — VERIFIED; continuous draw-on NOT confirmed) · D7 Venn/overlap (count-up on the
spoken figure) · D8 before→after rewrite pair (list upper ≈45%, stack 1–5, bottom splits 50/50
after a hard cut at ≈20 s) · D9 exhibit clip insert (hard-cut entry; exhibits do NOT freeze) ·
D10 profile/grid insert (REAL screen only, never a redrawn fake) · D11 trait-word chip cloud ·
D12 era timeline · D13 workflow strip · D14 end beat (Sky: most reels have NO end card/CTA —
Q override adds the completed device + door + logo moment ≤1 s after the last word).

**D15–D25** (verified Nov 9 from the formerly audio-only reels + DfA9/DfU49 — see
`STYLE-GRAMMAR.md` §4): D15 script-anatomy bar chart · D16 branch line · D17 trust dot-grid ·
D18 network loop · D19 "100s of people" grid · D20 views-refresh insert · D21 B&W beat ·
D22 "New Post" placeholder · D23 floating head cutout · D24 funnel card · D25 retention
autopsy labels.

**D26–D37 (Batch 18 — origin reel Dcc84V5jc6D, Aug 25 2026, Dcc-era; full specs in
`STYLE-GRAMMAR.md` §4, code in `code/sky_devices.py`):** D26 dashed loop arrow (the loop is
mandatory) · D27 donut split chart (hard pop 1 f on the spoken figure; split values update,
headline numbers never change) · D28 phone section tracker (real clip playing inside, section
label changes with the spoken structure) · D29 flanking dot columns (hollow left / filled
right, loose arcs, enter + exit with the phone) · D30 dual proof-caption columns (two real
heads + handles + two real caption columns behind the speaker) · D31 linear count-up
(~270/s LINEAR, starts at 0, NO landing value, fades out still counting) · D32 template/
caption document + highlight sweep + top reader (the document IS the product; dim ↔ sharp
states of ONE object) · D33 comment-screenshot example pair (two real screenshots, handles +
timestamps visible) · D34 thumbnail wall slide (motion-blur slide entrance, ~4 s life) ·
D35 AI-prompt doc + chat UI (real prompt text, real cursor from the recording) · D36
live-example bookend (the SAME document returns sharp, cropped not reflowed, + keyword pill)
· D37 staggered figure pair (one figure per spoken number, left then right, glow decay on
the second). The spoken template ↔ written caption is ONE device with two synchronized
layers (D32 + D36) — never built as two unrelated devices. The reel's whole system is ONE
locked-off take with dry voice only; the PWC engine's 1.45× hook zoom-out, slow push and
punch-ins are measured NOWHERE in it — they are not Sky and are banned in premium plans (v6).

**D38–D54 (Batch 19 — 33 NEW reels #17–49, Nov 9 2026; full specs in
`STYLE-GRAMMAR.md` §4, reconciliation in `code/DEVICE-RECONCILIATION-B19.md`, code in
`code/sky_devices.py`):** D38 POV-desk hook-doc (live Notion doc IS the canvas — headline =
hook, list types in live) · D39 subject photo insert (bottom-centre on the spoken name,
~2–3.5 s) · D40 POV scene label (pill top-left #19 vs full-width top bar #23/#25 — one
device, two geometries) · D41 spine framework diagram (photoreal 9-vertebra column, zoom to
the active vertebra + detail cluster; spine asset is MUSE-SUPPLY) · D42 question card +
outcome fork (frosted card → empty card + branch lines → outcome pills one at a time; Sky
narrates the device himself; Sky's measured outcome serif is a banned telltale in v6 — Q-lane outcomes are bold grotesque) · D43 view-count badge
(eye + count floating above a phone exhibit, per-exhibit) · D44 POV mini-window presentation
(small rounded-rect window centred on black ground, POV line above, static whole reel) ·
D45 kinetic-type black card (thesis words huge yellow condensed, 1.5–2.5 s, hard cuts) ·
D46 vertical split-screen (reactor left / exhibit right, 55/45, turn to camera at the
verdict, exhibit replays its opening once) · D47 binary label pair, anchored (two options on
real set objects, resolved by a headline lockup naming the winner) · D48 stacked split-screen
(exhibit top / reactor bottom, persistent, chrome intact — the MERGE of worker 2's D42 and
worker 3's D38) · D49 red annotation outline (ellipse/rectangle/glowing ring on a proof
screen — Sky's own red, GOLD in Q's lane, never emitted red) · D50 gradient script headline
(green→purple gradient + glow, remapped teal→gold) · D51 player-stats T-pose card (full-body
T-pose + accumulating stat list, matched pair) · D52 human/AI split card 70/30 (one figure
per spoken number) · D53 SMPTE colour-bars "SHOW PROOF" gag (**single-use** until a second
example appears) · D54 grid-background workflow strip (one step centred at a time, sliding
horizontally — distinct from D13). The five L-series devices (Andrew Lee's, reels #47–#48)
are NOT Sky's and are NOT in the registry — see `GAPS.md` G-20.

**D55–D56 (Batch 36 — P14/P15 strip-resolved completion, Nov 12 2026; full specs in
`STYLE-GRAMMAR.md` §4, code in `code/sky_devices.py`):** D55 numbered pill system (chips
pre-shown as a row at the chest; each pill's text types in by word groups over ~1.0–1.3 s
after the previous text's blurred-slide exit; the active chip stands alone on its number
word — DeYKkAIgVfL pills #1–#4) · D56 "New reel" UI exhibit shrink (the B&W frame scales
down into the IG posting UI's thumbnail ~14.4–14.9 s, hard-cut exit at 16.0 s —
DeSTWxcDTA7 form 4a; **single instance**, flagged like D53). Batch 36 also ENRICHED
existing devices rather than renumbering (dedupe law): D17 (dot-grid flip bracketed
4.20–4.53 s; its one measured fade exit + whip-blur, an instance exception), D18 (DeYKk
loop ~66–79 s), D19 (play-icon cells, progressive fill, headline type-in ~76.9 s), D23
(floating-heads SYSTEM: role-label type-in, emoji pops, accumulating label list — DeSTW),
D50 (draw-in entrance variant, "Strategy work" 2.8–3.1 s). The tick-tone sound family is
annotated on D6/D20/D27/D31/D37 (see §1 E10); DJccT_xSWuT's UI blip is an instance note
on D51, not a device.

**Motion laws (v4, measured from Sky motion clips):** chart lines draw L→R with a glowing
leading dot, constant velocity, 0.5–3.0 s; axes first; area fills AFTER the line. Panel lines
draw one at a time (~0.3 s each) or pop in ≤0.2 s; then the active line PULSES (glow spike
~2.5× for ~0.3 s). Connectors draw AFTER their nodes land (0.4–2.4 s). Everything holds
steady, then exits by **HARD CUT. No fades.** The only fades in premium Sky are the two measured
in Batch 18 (Dcc84V5jc6D): the hook headline's 5-frame progressive exit (T-01) and the
linear count-up's 10-frame exit while still counting (T-06/D31) — measured exceptions, never
a general fade permission. **Word-timed + claim-carrying = Sky; decorative = slop** (Millee
WAY 03 resolution, Batch 18 §8b L8): Sky's overlays ARE animated — pops, count-ups, highlight
sweeps, blur-slides — but every motion lands on a spoken word and carries the claim. If a
motion lands on a word and carries the claim, it is Sky; if it moves for decoration, it is slop.

**Graphic furniture:** glassmorphic rounded cards; pop/scale entrances ≈0.3 s with slight
overshoot; motion-blur slide exits. Panel in: 7 f, scale .88→1, no blur (any blur-in variant
is a BANNED telltale in v6 — removed fallback). Panel out: hard cut
(measured; any slide-blur panel-out is banned in v6). Child builds: 6 f, on the spoken word, minimum stagger 3 f.
No idle float — panels hold still once landed (the ±3 px / 4 s sine idle float is a banned
telltale in v6 — removed fallback). **Nothing stacked:** no text over a graphic, no pop over a pop, no card over
a card — every element in its own clear zone (engine no-overlap check on every frame must
pass). No default scale-in entrance — motion only when it fits that exact beat, otherwise
hard cut in / no move. **Frame one = Q talking on camera** — never a cold open on a wall,
grid, board or diagram without him in it. **The WALL = OTHER creators' paid-video walls,**
never Q & Kiya's own grid. Video boxes = OTHER creators, always with their @handle on or
right under the box (Q & Kiya only when the example IS them). **SAY IT, SHOW IT:** whatever Q
says, a visual carries it, timed to the words.

## 4. Hooks (four formulas observed across the 15)

- **H-A Definition-by-negation:** "Most people don't know what X is / X is not …" → redefine
  as a mechanism. **H-B Result-first autopsy:** state the result figure in the first line with
  the evidence already on screen. **H-C Dismissal:** build the generic approach for 2–3 beats,
  then stop and reject it. **H-D Paradox/superlative:** a claim that inverts the default
  ("viral *twice*", "drop-offs are *good*"). Hook rule: framework name or result figure on
  screen inside the first 10% of runtime; first graphic by f3–f12; at least 3 builds in the
  first 3 s; face present from frame one; no greeting in-video. Titles/hooks use **Q's exact
  words** — never invented hooks.

## 5. PWC law (outranks Sky everywhere it differs)

- Palette: teal #14A886 = structure, gold #FEE238 = payoff, navy #00214E ground. NO red, NO
  neon green. PWC logo in every video, unaltered (`assets/pwc_logo.jpg`).
- Nothing over Q's face at any zoom/punch scale. IG safe zone x 70–930, y 280–1480.
- **Complete blur law** for hidden-app proofs: on screenshots showing other creators getting
  paid, blur face, profile picture, profile name/@handle, brand name/logo, AND the top-right
  "Paid out" total. Keep sharp: follower count, the "Earned $X" amount for that video, and
  "Paid X hours/days ago". The hidden app is never named or shown in public content.
- **No door device** in any form — no door card, animation, or transition.
- Proof ethics: figures on screen are Q's real numbers or clearly-labelled worked examples.
  Sky's numbers are his case data — the device transfers, the data never does. Earnings
  framing is second-person/collective, never a direct solo claim that a specific payout is Q's.
- Real screens over drawings: profiles, grids, analytics, documents are real screen
  recordings (D10) — never redrawn fakes, never fake analytics. Drawn diagrams are built from
  CapCut native shapes/text — never ffmpeg/PIL plates.
- Sound: Q's denser standard (bed ≈ −28 dB + sound on every landing AND exit — the
  SKY-PLUS target over Sky's dry + tick-tone base) inside Sky's visual forms. Uploaded
  reels stay original-audio-only; built videos carry the cleared bed.
- **Asset law (Batch 36, binding):** Q + Kiya's own pool FIRST (proofs, profiles, Skool
  screens, head cutouts, media library — inventory in Batch 36
  `synthesis/ASSET-POOL-INVENTORY.md`), then style-asset libraries and real screen
  captures; sounds from Q's licensed local library only. Premium AI (Higgsfield-grade /
  Fable motion) is a first-class asset for ILLUSTRATION and VISUAL HOOKS only — proof is
  real-only, always (see BANNED TELLTALES). Empty pools are not a source; never cite them.
- CTA: the close is a door built into the last labelled section — comment the keyword to get
  the framework as a take-home, optional one-line follow for the series. Doors are LOCKED
  until Mon Dec 7, 2026 (founding window Dec 7–13); never say or imply doors are open today.
  Community link is always **skool.com/paid-with-content**. Premium $97/mo monthly only.
  Standing keyword **WAITLIST** (routes to waitlist capture + "Your First 7 Days — 3 Wins" PDF;
  waitlisters get an extra month free). Keyword must have a live ManyChat flow before posting.
- Endings (Q): rotate per video — `card` / `comments` / `notifs` (see `STYLE-GRAMMAR.md` §8);
  end moment ≤1 s after the last word. Finishing lift on every SKY final:
  `eq=gamma=1.10:brightness=0.015` once, whole frame ("slightly lighter, not a crazy change").

## 6. Carousels (this folder IS the carousel authority)

Sky's carousel system, copied to a T, in PWC colours. Slides are 1080×1350 (4:5);
video slides run 4–22 s — but the system is NOT all-video (Batch 36 census: 51 video +
35 static image slides of 86; see the census correction below). One accent per series (teal OR gold on navy; orange series
→ gold/amber on navy or cream). Headline system: small plain kicker, then a HUGE display
headline with the one keyword in the accent colour. Every claim gets a DIAGRAM, not
decoration. Named, numbered frameworks ("X of Y" counters, slide counters "02 / 10").
Handle watermark on every slide (@yerrr__q + PWC logo where the format has a badge slot).
Save-bait + CTA closes (steal-the-skeleton template slide, then Comment-KEYWORD slide with
the free-product card + typing comment box). Archetypes: **A Breakdown** (famous-creator
device: cover "LET'S BREAK DOWN HOW [NAME] GOT [EXACT VIEW COUNT] VIEWS" + face in a circle
with glowing accent ring + @handle / followers / title; phone-frame mockup + annotated
transcript card per section) · **B Retro-OS teaching** (cream, orange→gold, serif, cassette/
computer-window frame) · **C Swiss diagram** (off-white, minimal diagrams, one accent) ·
**D Neon framework** (glowing silhouette mascot → Q's branded character treatment in
teal/gold; checklist close, no keyword CTA) · **E Ember** (glowing italic serif, cinematic
photo art — CORRECTED Batch 36: NOT a 2-slide micro format; DexfsH5l0q6 is 9 slides
(2 video + 7 image) and DevFnZxlCQO is 8 (2 + 6); the image tails are undecoded (blocked),
so E's full form is still owed). **Census correction (Batch 36):** the carousel system is
**10 posts / 86 slides = 51 video + 35 static images (41% static)** — "every slide is a
video" was wrong; video slides are the animated heads/hooks, long tails are static.
Archetype A has NO CTA/template close and NO handle watermark (both "universal" rules have
A-sized exceptions). New measured devices from the 51 video slides: the transcript card's
scrubber + timecode belongs to the SOURCE video's timeline; Archetype B's PLAY timecode is
a disguised slide counter and its window filenames are a grammar (.EXE = interactive,
.TXT = text); Archetype D (DfQPBSpkRUG) carries a traveling progress thread along the
bottom of every slide. Durations are quantized per archetype (B/C 8.0 s cover + 4.0 s per
slide; D exactly 7.0 s; E videos exactly 5.0 s; A 7.0 s cover + transcript-length sections);
audio exists ONLY in Archetype A section slides. Full synthesis: Batch 36
`carousels/CAROUSEL-SYNTHESIS.md`. **Serif scope:** the serif in Archetypes B and E is carousel-only
(measured from Sky's carousel posts) and never appears in reels in premium Sky.
The reel serif patterns (serif display / serif title / hero word / serif counter caption) are
BANNED TELLTALES in reels (v6) — removed fallback, never used. **Never use Q himself in carousel illustrations** — use a real
major creator instead (Adley Kinsman @adley is the standing example); bake no music into
carousel slides. Slide rhythm: cover 7–8 s, teaching slides ~4 s (B/C) or ~7 s (D),
Breakdown slides 7–22 s. Cadence Q ordered: 1/day weekdays, 2/day weekends. Full spec:
`examples/carousels/CAROUSEL_BREAKDOWN.md`.

## 7. QC gate (summary — full gate in `QC.md`)

Nothing ships on a builder's say-so. On the exported file, in motion: framework name ≤10%
of runtime; hero device visibly unfinished until the close; every part's state-change on its
first spoken word with its example asset at the claim; captions 1–3 words, one weight, none
over the face, none straddling a cut; frame-**sequence** motion grade vs the model reel for
this video's form; per-word fit audit (one clipped word blocks delivery); freezedetect zero
freezes ≥0.35 s; ±0.15 s audits around every device entrance/exit; last-word→end-card ≤~1 s;
lip-sync offsets; retention read (hook claim/curiosity ≤2 s, open loop early + second before
midpoint, visual event ≤2 s, every section ends on a mini-payoff or a new question, ending
chains to the next watch); no-overlap every frame; constant pace; frame-one-talking;
wall-class check; **premium gate P9** (no telltales, citations, provenance — v6) and
**beat-lock gate P10** (events on the word grid or reasoned). **Full self-watch at normal speed before delivery.** Delivery report
states, per file: CapCut project/draft name, motion-sequence grade per beat, freeze count +
longest freeze, entrances/exits audited, last-word→end-card gap, per-word fit result.
A cut with any gate unrun is reported as unverified, never as verified.

## 8. Sources inside this folder

- `STYLE-GRAMMAR.md` — measured specs (VERIFIED / [EST] / UNVERIFIED tagged).
- `examples/` — the 15 priority reels (manifest + full text decodes + word transcripts),
  the 14-reel motion teardown, the carousel breakdown (corrected by Batch 36: 10 posts /
  86 slides, 51 video decoded), the browser
  motion-verified record, the 113-post form catalogue, and the SKY-SCORE device score card.
- `code/` — CapCut-native build spec + plan generator + QC scripts (see `code/README.md`
  for what is CapCut-native vs ffmpeg-only).
- `code/` (Claude Code build) — the style as EXECUTABLE code: plan generator (`sky_build_plan.py`),
  device registry D1–D56 (`sky_devices.py`, incl. `validate_premium_plan` +
  `validate_beat_lock`), palette/easing (`sky_palette.py`, `sky_easing.py`),
  HyperFrames emitter (`sky_hyperframes.py` — primary render path, verified Nov 9 with a real
  1080×1920 MP4 render), CapCut sequence emitter (`sky_capcut_draft.py`), QC (`sky_qc.py`
  — gates P1–P10), 88 unit tests, and `code/MEASUREMENTS_2026-11-09.md`. The generic-fallback
  module (`sky_option2.py`) was DELETED in the v6 premium purge — there is no second option. Installed in Claude Code as the
  `sky` skill (`~/.claude/skills/sky` → this folder). Status stays NOT YET GRADED until a
  real-Q-take test edit passes the frame-sequence grade (QC.md §6).
- `examples/batch-18-sky-origin/` — Batch 18 origin reel Dcc84V5jc6D (Aug 25, 2026):
  `DECODE.md` + `EDIT-TEARDOWN.md` + `words.json` copied here, `CLIPS.md` index of the 17
  motion clips + 51 keyframes (clips live in the batch folder, not copied — size). Devices
  D26–D37 + Dcc-era D1/D2 variants. See `examples/MANIFEST.md` §6.
- `GAPS.md` — what cannot be reproduced exactly. Read it before promising anything.
- `skills-plugins-githubs.md` — everything this style actually uses, with licenses.
- `ASSETS.md` + `assets/` — Q/Muse assets only.

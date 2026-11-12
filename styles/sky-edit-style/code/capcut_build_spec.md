# capcut_build_spec — build every Sky device as a CapCut-native draft

**Canvas:** 1080×1920 (reels) / 1080×1350 (carousel slides, each slide its own MP4).
**Safe zone:** x 70–930, y 280–1480. Nothing above y = 280. Nothing over Q's face — verify the
face zone empty at every zoom/punch scale used.
**Palette:** teal #14A886 = structure, gold #FEE238 = payoff, navy #00214E ground, white text.
NO red, NO neon green. PWC logo on its own track, unaltered, every video.
**General motion:** pop/scale entrances ≈0.3 s with slight overshoot; exits by HARD CUT (motion-blur
slide exits where the spec says so); no slow fades, no cross-dissolves on devices. One motion at
a time — never punch in on a graphic state-change frame.

**PREMIUM SKY IS THE ONLY OUTPUT MODE (SKY v6, Batch 36 — supersedes the Nov 9
"two options" note).** The 15 generic/anti-slop patterns are REMOVED (`code/sky_option2.py`
deleted) and are BANNED TELLTALES (see `SKILL.md`): serif treatments, blur-ins, idle float,
slide/blur exits, caption pop-ins, generic slide entrances. The D12 spec correction stands
(static full-width line, nodes pop ~0.5 s apart).

## Track layout (reels)
- Track 0: A-roll (silence-compressed first; inter-word gaps ≈0.15 s).
- Overlay 1: hero device (panel/chart/board — ONE master graphic at a time).
- Overlay 2: example assets (real screens/clips, on the exact claim word).
- Overlay 3: chips / labels / notes (front graphics).
- Overlay 4: captions (D1) — bare native text, chest band.
- Top: PWC logo (own track, unaltered).
- Audio: voice (static gain to −14.5 LUFS) + cleared bed ≈ −28 dB + SFX per landing/exit.

## Per-device builds
- **D1 captions:** Auto Captions → manually re-segment every chunk to 1–3 words max → plain
  white native grotesque, size ≈58 (bold era A / regular era B, one weight per video), stroke 0,
  shadow black 40% / blur 8 / offset y 4 → centre x = 540, y ≈ 980 adjusted per take to clear
  the chin (chin + ≥40 px, inside y 280–1480). In: hard cut to full size in ≤1 frame (no pop-in
  ramp by default — the old "Pop" in is kept as Option 2, see Option 2 notes below); Out: ≈0.5 s pop/fade. Hook types on
  letter by letter.
- **D2 headline lockup:** two native text layers grouped — kicker (regular, sentence case,
  tracking +20, ≈30–34 px, white) + display (native extra-bold condensed, Title Case, tight
  leading 0.95, ≈105–125 px, gold; framework keyword teal). Group centre x ≈ 500, y ≈ 1150
  (chest band, face-clear). In: pop/scale ≈0.3 s slight overshoot + kicker Fade 0.2 s delayed
  0.05 s. Holds ≈5 s, hard-pop exit.
- **D3 title stack + pill:** title native text, teal, ≈46 px, centred, baseline y ≥ 300. Pill:
  native Shapes → rounded rectangle, fill #FFFFFF, ≈590×86 px, centred dark-navy (#0A1633) bold
  text ≈40 px grouped inside, y ≈ 360–440. Per section: duplicate the group, swap the label,
  hard swap + ≈0.3 s pop.
- **D4 filter board:** board = native rounded rectangle (glassmorphic), fill #000000 at 65%
  opacity, face-clear side/top zone. Criteria block = 2 text layers locked at board top. Each
  row = one text layer: pending 40% opacity → active 100% (opacity keyframe at the spoken item
  name) → verdict chip (native text in a bordered chip: teal check "KEEP" / grey "PASS" / gold
  "MINIMUM"), In: Pop scale 1.6→1.0, 0.18 s ease-out + stamp/tick SFX.
- **D5 chapter card:** one reusable text group per chapter — numeral (teal, ≈150–220 px
  extra-bold), name (white, ≈54–64 px bold), definition (white 80%, ≈34–40 px regular). In:
  pop/scale ≈0.3 s with slight overshoot (measured graphic entrance; Slide Left 0.3 s /
  Slide Down 0.3 s kept as Option 2) + numeral Pop 0.15 s. Previous
  chapters dim to 45% but stay listed. Save as draft template, duplicate per episode.
- **D6 chart:** real analytics screen recording on an overlay track where Q has it; highlight
  zone = native rounded-rect outline (teal, 4 px stroke, no fill) keyframed to the segment as
  named. Static base + annotation states stacked in order (≈10 s apart). Second-wave/payoff
  segment in gold. Axis labels native text ≈32 px white 70%. A keyframed wipe/draw-on reveal
  is a Q construction choice, NOT Sky's verified motion — label it as such in the plan.
- **D7 Venn:** two native circle shapes, fill teal / gold at 45% opacity, overlap centred in
  the face-clear graphic zone. % figure = native text with count-up keyframes landing ON the
  spoken figure. In: pop/scale 0.8→1.0, 0.3 s, staggered 0.1 s (measured graphic entrance
  family; no fade by default — Scale + Fade 0.3 s kept as Option 2).
- **D8 rewrite pair:** Before = native text white 60%, ≈44 px. At the rewrite beat: before
  keyframes to 35% opacity + strikethrough on (0.2 s); after = native text white 100%, the
  swapped/power word in gold. After-line in: pop 0.25 s (default — entrance unverified, G-06;
  Slide Up 0.25 s kept as Option 2).
  Pair holds 1.5–3 s after landing. Layout: list upper ≈45%, stack 1–5, bottom splits 50/50
  after a hard cut at ≈20 s (DfLa-verified layout).
- **D9 exhibit insert:** clip on an overlay track with a native rounded-rect mask (radius ≈24)
  if PiP, or hard cut full-frame. Label = native text chip top-left (white bold ≈36 px on a
  black 55% chip). Entry: HARD CUT. Exits: motion-blur slides. Exhibits do NOT freeze.
- **D10 profile/grid insert:** real screen recording only, overlay track. Floating treatment:
  keyframed slow bob (y ±10 px, 2.4 s ease-in-out loop) + rotation ±1.5° + native drop shadow.
  Gentle bob is measured on Sky's floating elements (head cutouts bob gently, DfA9 @0–2.8 s,
  DfIY @6.5–11 s; cards bob slightly, DfDu @26–30 s); the ±10 px / 2.4 s / ±1.5° values are [EST].
  View badges stay as recorded. Hidden-method material passes the blur law BEFORE the timeline.
- **D11 chip cloud:** each word = native pill chip (dark fill 60%, white text ≈36 px), In: Pop
  0.15 s, staggered 0.25–0.4 s, placed in a ring in face-clear side zones. Exit: hard cut
  (measured §5 Exits; the old fade_together 0.2 s kept as Option 2).
- **D12 timeline:** native line shape (4 px, white 50%) + node circles; line is STATIC
  full-width from t0 (no extension — VERIFIED De-A2dvCeV3, G-07); nodes pop 0.2 s, ~0.5 s apart;
  year labels pop in above the line; current-era label gold,
  past era grey.
- **D13 workflow strip:** 3–4 native chips in a row (D5 index grammar, horizontal). Each chip
  activates as its step is spoken: opacity 40→100% + teal underline keyframe. Header = D3 title
  treatment at y ≥ 300.
- **D14 end beat + Q endings:** completed device held on the closing line (0.8–1.5 s) + spoken
  door over the completed graphic + logo/keyword end moment ≤1 s after the last word. Endings
  rotate: `card` / `comments` / `notifs` (see `STYLE-GRAMMAR.md` §8).
- **Hero words:** hero = white lead-in over one heavy Inter ExtraBold gold word,
  measured D2 entrance (pop/scale ≈0.3 s with slight overshoot + kicker fade 0.2 s delayed
  0.05 s), hard-cut exit. The letter-stagger unblur and the serif title (Instrument Serif
  Italic, per-word blur-in) are kept as Option 2 (NOT the default) — no serif in reels under
  Option 1; serif lives in carousel Archetypes B/E. Hero words sit y≈450
  (behind-the-head layer: cap overlaps letter bottoms, face never covered).
- **Counters:** big Inter ExtraBold number, count-up out_expo 1 s, white grotesque-sans caption, gold figure — no serif under Option 1; the serif gold caption variant is kept as Option 2.
- **Panels (general):** in 7 f scale .88→1, no blur (blur-in kept as Option 2); out hard cut
  (slide-blur panel-out kept as Option 2); child builds 6 f on the spoken word, min stagger 3 f; no idle
  float — panels hold still once landed (idle float kept as Option 2).
- **Meme pops:** Carter pop ≈37% frame width, centred, top edge ≈14% down, hard cut in/out,
  hold 1–2 s; Kilgore poster ≈75% width, top 25–30%, slam in, hold ≈1.5 s, max 2/video.
  Face-box guard: any pop intersecting face box + 40 px is moved/shrunk/skipped. SFX in AND out.

## Removed fallback patterns (SKY v6 tombstone)

The former "Option 2" section (serif display/title, hero-word letter-stagger, serif counter
caption, text-handoff hold, idle float, blur-in variants, slide+blur panel-out, D5/D7/D8/D11
generic entrances/exits, HyperFrames slide-in branch, key-clicks-on-serif trigger, caption
"pop in") is DELETED. These patterns are banned telltales in premium Sky plans and are
rejected by `validate_premium_plan` (gate P9). The list is kept here only so old references
resolve to this tombstone.

## Carousel slides (CapCut)
Each slide = its own 1080×1350 composition, exported as an MP4 (4–22 s). Build from native
text/shapes/masks/keyframes per `examples/carousels/CAROUSEL_BREAKDOWN.md` archetype (A–E):
text reveals line by line, diagrams draw themselves, bars fill, numbers land, cards populate.
Never export a static image as a slide. Handle watermark @yerrr__q on every slide; PWC logo
in badge slots. Never use Q himself in carousel illustrations (Adley Kinsman @adley is the
standing example). No music baked into slides.

## After the build
Save each device as a reusable CapCut draft template after its first build. Delivery report
states the CapCut project/draft name per file (see `QC.md` §7). Run `qc_freezedetect.sh` on
every export before the motion grade.

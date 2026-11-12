# SKY MOTION TEARDOWN — @realskytan, 14 reference reels

**Purpose:** frame-by-frame motion teardown so Claude can code identical edits from it.
**Method:** every reel ffprobe'd for duration; frames extracted at ~4 fps (270×480 JPG) into
`frames/<ID>/`; contact sheets (30 frames per sheet, 6×5 grid, timestamp-labeled) into
`sheets/<ID>/`; word-level transcripts via faster-whisper (base.en) into `transcript_<ID>.json`;
each reel read sheet-by-sheet and catalogued in `notes_<ID>.md`.
**Coordinates:** 0–1000 on a 1080×1920 frame (x = left→right, y = top→bottom).
**Timestamps:** ±0.3s (4 fps sampling). **Sound cues:** NOT visible from silent frames — every
"sound" note below is [UNVERIFIED] inference from the visual beat, never a heard fact.
**[UNVERIFIED]** marks anything not directly seen in the frames.

## Reels covered (14, ~943s total)

| ID | Dur | Topic |
|---|---|---|
| DfZ_q_pFbX1 | 37.2s | "Why Process Crushes" — @allanpeters |
| DfX2qwQGagM | 53.9s | "Good Content Strategy" — Leila Hormozi content filter |
| DfU49SJAFYH | 103.8s | TCM practitioner 1.1M-view video, retention breakdown |
| DfTawo5jHMH | 59.7s | "The 4 Questions Filter" |
| DfSf5v8j73o | 56.7s | "Drop-offs you actually want" — retention deep-dive (same TCM video) |
| DfQ4E1Hjn0n | 75.6s | "5 Content Types" — 100k in 6 months |
| DfPxqFPAY4_ | 77.5s | "Viral Twice" — collab posting |
| DfLaEFNDKkv | 93.9s | "Power Words" — unskippable hooks |
| DfIYshekeF3 | 60.5s | "ChatGPT ideas" / legit content strategy |
| DfDuMnCjNdE | 68.7s | "Shallow formats" — why your audience doesn't value your opinions |
| DfA9L-PHYWp | 77.2s | "Content-Offer Fit" — no content strategy |
| De-A2dvCeV3 | 63.2s | "These formats are officially dead" — fast content = fast food |
| Dez4fPJCR74 | 58.9s | "The absolute worst content strategy is teaching" |
| DexJ-qWiWdY | 56.0s | "The ultimate storytelling caption for Instagram" |

## Global grammar (true across all 14)

- **Accent systems:** two palettes only. GREEN family (9 reels: DfZ, DfX2, DfU49, DfTawo, DfSf,
  DfQ4, DfPx, DfLa, DfIY) — neon green on near-black. ORANGE family (5 reels: DfDu, DfA9, De-A2,
  Dez4, DexJ) — warm orange/gold on near-black. One accent per reel, never mixed. Red appears
  ONLY as a semantic "bad/wrong" marker (red X, red lines, red heads) — never as decoration.
- **Word-by-word captions:** every reel. White, center-lower (~y560–620), one word at a time,
  hard cut per word, keyword in the reel's accent color. No caption ever overlaps his face.
- **Empty space above his head is the stage:** every diagram, card, panel and head lives in the
  top ~45% of frame (~y0–480) or at chest level (~y480–700) — never over his face.
- **Hard cuts in/out:** devices appear and disappear with hard cuts or fast slides (~0.2–0.5s).
  No slow fades, no cross-dissolves on devices. [UNVERIFIED: exact easing curves — frames at
  4 fps cannot resolve them; entries feel like ease-out slides and pop-ins.]
- **One idea per beat:** a device appears on the exact spoken word, holds while the beat is
  explained, then flies off when the next beat starts. Devices rarely overlap more than two at once.
- **No end cards:** all 14 reels end on Sky mid-sentence or on a final diagram. No outro card,
  no follow CTA screen was seen in any reel.
- **Slow push-in on Sky:** present in several reels [UNVERIFIED rate — too slow to measure at
  4 fps; reads as a gentle continuous zoom across the whole reel].

---

## MASTER DEVICE INDEX

### 1. Word-by-word captions
- **Reels:** all 14.
- **Spec:** white sans, bold; center-lower ~x100–900, y560–620; one word appears per spoken word,
  previous word replaced (not accumulated); keyword of the line in accent color (green/orange);
  hard cut per word. Never over face. Sound: [UNVERIFIED — likely a soft tick/pop per word].

### 2. Big title build (word-by-word / stagger-in)
- **Reels:** DfZ ("Why / Process / Crushes"), DfX2 ("Good Content Strategy"), DfSf ("Drop-offs
  you actually want"), DfPx ("VIRAL TWICE", "STEP 1", "CRUCIAL", "COLLAB"), DfLa ("WAY TOO GOOD",
  "POWER WORDS"), DfQ4 ("100k in 6 Months", "1 Demo = 10x Trust"), Dez4 ("worst Content Strategy"
  cursive), DexJ ("Ultimate Storytelling caption" cursive).
- **Spec:** big display type, center-lower ~x300–700, y480–660, or top-center for section titles;
  words stagger in ~0.2–0.5s apart, accent color on the keyword word, white on the rest;
  cursive/script variant used for emotional titles ("Content Strategy", "Ultimate", "Fast content",
  "Leverage"). Holds 1–3s, hard cut out. Sound: [UNVERIFIED — likely a whoosh + thud per word].

### 3. Floating mini video card (dashed border)
- **Reels:** DfU49, DfZ, DfSf, DfTawo (video-call window), DfQ4, Dez4, DexJ.
- **Spec:** small vertical video card ~x480–620 wide, y0–180, top-center; dashed white/gray border;
  drops in from top in ~0.3–0.5s with a small bounce; carries a view-count label ("1.1M", "1.3M",
  "1.9M") and/or @handle; often has a white play triangle. Appears exactly where Sky points UP.
  Exits by flying off up. Sound: [UNVERIFIED — likely a soft pop + whoosh].

### 4. Retention-graph HUD (with updating pill labels)
- **Reels:** DfU49, DfSf.
- **Spec:** glass panel top-left/center ~x30–980, y60–260; green retention line draws left-to-right
  with a glowing dot at the leading edge (~1.5–2.8s draw); axes + endpoint label ("34%"); a white
  pill label above/beside it UPDATES per beat (Throat mucus → Broader term → Intentional drop →
  Hook filtering ✓ → Bad drop → Basically flat ✓ → Spleen → Fluids); green playhead shading fills
  under the curve; red segment marks a bad drop. Persists as analysis HUD for most of the reel.
  Sound: [UNVERIFIED].

### 5. IG profile card building in stages
- **Reels:** DfX2 (@leilahormozi), DfZ (IG post UI mockup), DfQ4 (phone mockup, "travelprofile"
  100K), DfPx (collab UI walkthrough), DfLa (full IG Reels phone UI).
- **Spec:** card ~x400–650, y40–280 top-center; builds in stages over ~2–2.5s: avatar → @handle +
  follower count → Follow/Message buttons → content. In DfPx the full collab flow is walked:
  menu "Edit / Tag people / Invite collaborator" → dropdown "Creator B" checked → dual-avatar
  "Creator A and Creator B / Collab post" header. Hard cut in, slide-out exit.
  **Follow-state animation: NOT SEEN in any of the 14 reels** — no Follow → Following state
  change was observed anywhere. This is the device Q named that is MISSING from the source set;
  it must be built from Q's description, not from a Sky frame.

### 6. Phone mockup
- **Reels:** DfTawo (iPhone, IG profile 100,000 followers, small bounce on landing), DfQ4 (iPhone,
  "SHOW IT LIVE" with LIVE badge), DfPx (phone with IG post UI + like/comment/share rail), DfLa
  (full IG Reels phone UI sliding in from right), DfZ (IG post UI mockup, heart 96K, 1.9M).
- **Spec:** phone ~x450–650 wide, y40–480, top-center/right; slides or drops in over ~0.3–0.5s
  with a small settle bounce; screen shows real IG UI (profile, post, LIVE badge, rail); labels
  pop around it per beat ("Product" left, "Service" right, "Coaching" left). Exits by sliding out
  the side it came from.

### 7. Filter / checklist panel (rows fill green, verdict X/check)
- **Reels:** DfX2 ("LEILA CONTENT FILTER"), DfZ ("The 2 Things"), DfTawo ("The 4 Questions Filter"),
  DfSf ("Lead filtering"), DfQ4 ("5 CONTENT TYPES"), DfPx (schedule checklist, "STEP 1" progress),
  DfIY ("THE PROCESS", "LEGIT CONTENT STRATEGY"), DfA9 (6-box grid, goal checklist), Dez4 (A-to-Z
  checklist, scrolling), DexJ (structure panel).
- **Spec:** dark glass panel ~x30–980, y40–300, top; title in accent at top; rows appear one at a
  time (~0.3–0.5s apart) as Sky names them; current row highlights/fills green when its section
  starts; verdicts land as green ✓ or red ✗ on the exact word (DfX2: "Top 5 marketing paid ads"
  red X ~14.8s, "Retaining A plus talent" green check ~20.5s). Panel persists across the section,
  returns for recap at the end. Dez4 variant SCROLLS as the highlight moves down a 10-row list.
  Sound: [UNVERIFIED — likely a tick per row, a chime on green check].

### 8. Little heads (orbiting / constellation / crown / glow / markers)
- **Reels:** DfZ (3 heads orbit card), DfX2 (head + green triangle marker, chip orbit), DfTawo
  (5-head constellation, center gets green glow ring + crown, splits into green/red boxes),
  DfSf (heads at panel edge, growing row; 3 heads sit ON the graph curve), DfIY (heads with green
  "?" badges, inside/outside circles), DfDu (head cloud ~20 heads, turns gray), DfA9 (head with
  orange triangle marker per row), De-A2 (head cluster turns red), Dez4 (head + timer, crowned head
  + crowd of ~15 heads), DexJ (head constellation, color-state white → red → green).
- **Spec:** small circular head cutouts (~40–90px), float in from edges over ~0.3–0.8s; orbit slowly
  around a card or drift in a loose constellation; markers: green triangle (current/good), green
  glow ring + crown (winner), red (bad/wrong), green "?" badge (confused audience). Heads bob
  gently while on screen. DexJ variant: the SAME heads change color state with the argument
  (white → red on "breaks their beliefs" → green on "proof"). Sound: [UNVERIFIED — likely a soft
  pop per head].

### 9. Funnel diagram (items fly in)
- **Reels:** DfX2 (funnel icon "STRATEGY" with white pills raining in, one green pill dropping out),
  DfTawo (format labels fly in: Duet, Quiz, Tutorial; green dot drops), De-A2 (3-tier funnel:
  "Viral Reel" 100,000 impressions → "Valuable Back-End Content" → "Nutrient-dense format" →
  "Trust → Potential Clients" + 3 green "$" icons).
- **Spec:** funnel shape top-center ~x400–980, y40–260; items fly in one at a time from the sides
  (~0.3s each, staggered); the "wrong" item drops out / turns red; bottom tier gains a payoff label
  + "$" icons popping in ~0.2s apart. Sound: [UNVERIFIED].

### 10. Photo pop-up (center chest, hard in/out)
- **Reels:** DfU49 (phlegm photo ~7.8–9.8s, spleen diagram ~33.5–41.5s, tongue ~67.5–69.2s),
  DfSf (phlegm photo ~36.5–38.5s).
- **Spec:** photo ~x420–580, y430–520, center chest; hard cut in on the exact word, holds 1–8s,
  hard cut out. No border, no animation, no zoom — just appears. Sound: [UNVERIFIED — likely a
  pop].

### 11. Chart / graph that draws (line, staircase, wave, bars)
- **Reels:** DfX2 (staircase chart "BORING TO YOU, GOLD TO THEM" drawing left-to-right ~49.5–50.5s,
  pulsing green dots ~51.0–52.0s; authority bars), DfQ4 (balance scale tilting, brand-longevity
  sine wave drawing ~64.5–67.5s with green dots at peaks, "DRIVES EYEBALLS" view counter),
  DfPx (double-peak chart, views-over-time S-curve, "2 WAVES, NOT 1" bell curves), DfTawo
  (legitimacy meter filling with green dots), DfDu (authority meter bar filling, narrative-arc bars),
  De-A2 (purple line chart "HIGH ENGAGEMENT", 2025→2027 timeline), Dez4 (outlier axes chart,
  60-sec progress arc), DexJ (1000-comments dot grid — see #24).
- **Spec:** axes/frame draws first (~0.5–1s), then the line draws left-to-right with a glowing dot
  at the leading edge (~1–3s); labels pop at peaks/troughs on the spoken word; area under the line
  fills solid accent left-to-right. Bars grow upward; meters fill left-to-right. Sound:
  [UNVERIFIED — likely a rising tone following the draw].

### 12. Count-up counter (views / dollars / followers)
- **Reels:** DfQ4 (view counter 10,317 → 1,000,000 in ~1.5s), DfPx (views 39K → 2.7M across two
  pushes; follower bars 62K → 128K / 41K → 84K; audience-quality % counting DOWN 90% → 34%,
  turning RED), DfIY (dollar counter $18,700 → $12,400 → $15,300; view pills 1.2M / 845K / 2.4M /
  1.7M / 840K; content-ideas counter 2 → 30), DfDu (view counts 880K / 1.7M / 2.4M / 3.3M / 2.1M /
  1.3M / 859K; watch-time timer 0s → 38s), Dez4 (60-sec timer counting up; payment pills counting
  to ~$18,000).
- **Spec:** big numerals, accent color, center or top; counts fast (~1–2s per counter) with numbers
  jumping in large steps (not 1-by-1); lands on the final figure with a hold. Percent counters turn
  red as they drop. Sound: [UNVERIFIED — likely a rapid ticking / slot-machine sound].

### 13. Flow-diagram build (nodes appear on spoken word)
- **Reels:** DfU49 (Spleen→Fluids / Phlegm←Dampness ~59.5–61.5s, "Every line connects"),
  DfZ ("The Whole Process" 3 cards + connecting line ~21.5–22.8s; feeling→words→= expert stack),
  DfIY (inside/outside circles, fan-out diagram with green connector lines, Venn).
- **Spec:** nodes/cards appear one at a time on the spoken word (~0.3s apart); connector lines draw
  between them after the nodes land (~0.5s); the full diagram holds while explained, then fades or
  flies off. Labels ("Every line connects", "No aggressive switches") appear beside the diagram.
  Sound: [UNVERIFIED].

### 14. Thumbnail cloud / wall
- **Reels:** DfZ (thumbnail cloud ~10 thumbs fanning out ~30.2–32.5s), DfIY (3×3 thumbnail grid,
  format card carousel cycling labels), Dez4 (6-card cloud at open; competitor research wall
  ~28.5–31.5s with transcript text + SLIDE DECK card), DexJ (thumbnail row rising from bottom).
- **Spec:** 6–12 thumbnails fan in from a center point or drop in one at a time (~0.2–0.3s apart),
  top of frame ~x40–980, y40–250; each with a small label; one thumb may glow gold (the highlighted
  one). Wall variant: full-frame columns of thumbnails with transcript text beneath. Exits by
  flying off up. Sound: [UNVERIFIED].

### 15. B-roll full-screen cutaway
- **Reels:** DfZ (hands drawing "N" logo ~14.8–15.8s; satisfying 3D dice/blocks ~23.5–27.5s),
  DfX2 (tennis B-roll ~52.2–52.8s with green "GREAT ATHLETE PRACTICE"), DfQ4 (Big Mac being built
  ~8.8–13.2s, "Zero Value" text center ~12.5s).
- **Spec:** hard cut to full-screen B-roll for 1–4s, usually with a single accent-colored label;
  hard cut back to Sky. The B-roll is the visual proof of the spoken analogy. Sound:
  [UNVERIFIED — likely the B-roll's own sound or a whoosh on the cut].

### 16. B&W + color isolation
- **Reels:** DfIY (frame goes B&W ~2.8–4.2s with big "stop" text), DfLa (background goes B&W while
  phone stays in color ~3.0–5.5s), DfA9 (thumbnails go B&W one at a time ~2.0s; whole frame B&W
  with orange italic text ~4.5–5.8s; "Exactly" B&W beat ~38.8–42.2s), DfPx (final frames desaturate
  to B&W ~76.5–77.5s, slow fade).
- **Spec:** instant desaturation (hard cut, not a fade) except DfPx's ending slow fade; the isolated
  element (phone, text, one card) stays in full color; color returns on a hard cut ~1–4s later.
  Used to mark "wrong/old way" or to isolate the hero object. Sound: [UNVERIFIED].

### 17. Venn diagram
- **Reels:** DfPx (two circles draw, slide together, overlap lens fills GREEN ~70.5–75.5s),
  DfIY (inside/outside Venn ~47.0–48.5s).
- **Spec:** two circles draw (~0.5–1s each), slide together over ~1s, overlap region fills accent
  green (~0.5s); labels on each circle + heads on top. Sound: [UNVERIFIED].

### 18. Split-screen screen recording
- **Reels:** DfLa only (~17.5–93.9s — most of the reel).
- **Spec:** frame splits horizontally — TOP half = screen recording (Claude chat, dark UI), BOTTOM
  half = Sky in side-profile narrating, looking at the screen. A "Rewriting hooks" title + numbered
  list of 5 hooks fills in line by line; each hook line HIGHLIGHTS GREEN as he reads it
  (~29.5s, ~37.5s, ~47.0s, ~62.5s, ~75.0s [approx — exact times UNVERIFIED]). Word-swap edit:
  in hook #5 the word "draining" is highlighted ORANGE as it is swapped to "destroying" ~75.0s.
  Thanos snap still pops top-right of bottom half ~42.0–43.0s. PIP reaction/B-roll clips dock at
  right of bottom half ~55.0–60s. Sound: [UNVERIFIED].

### 19. Script-lines / colored-lines panel
- **Reels:** DfSf (script lines: white "Hook" line, RED "Lead" lines bracketed, GREEN line, white
  lines; red lines PULSE/glow red ~18.0s), DfDu ("SHIFTING BELIEFS" / "TRUST BUILDING" / "Narrative
  Arc" panels with colored horizontal lines), DfA9 ("LINES" panel returns with 0:40 timer),
  De-A2 (colored-lines panel with orange/yellow/blue/green lines + orange circle icon; "SHIFTING
  BELIEFS" lines panel), Dez4 (script-structure lines: Hook red, Lead yellow, Body 1 blue,
  Open loop 1/2, Body 3, CTA green), DexJ ("Ultimate Caption Structure" panel: Introduction red,
  Struggle yellow, Rise blue, Proof teal, Unique Mechanism pink, Expectations white, Two-Door CTA
  green).
- **Spec:** glass panel top ~x30–980, y40–280; horizontal colored lines draw one at a time
  (~0.3s apart), each line = one script section; the active line pulses/glows in its color; labels
  at left. In DexJ the same panel returns twice and the lines redraw. In Dez4/DexJ the panel is
  the reel's spine — it opens the reel and returns for the walkthrough. Sound: [UNVERIFIED].

### 20. Timeline diagram
- **Reels:** DfQ4 (growth bar "month 1" → "month 6" filling ~3.8–5.5s; quote-card timeline
  "today" ——— "+100 yrs"), De-A2 (2025→2027 timeline with nodes "Fast-paced content 2026" /
  "Nutrient-dense formats 2027"), DfPx (schedule checklist with "1 First Push / 3 day break /
  5 Second Push").
- **Spec:** horizontal line draws left-to-right (~0.5–1s); nodes pop on it one at a time with labels;
  the "now" node glows. Sound: [UNVERIFIED].

### 21. Dot constellation / audience-quality cloud
- **Reels:** DfQ4 (~15 white dots scatter into a loose circle, one turns GREEN ~48.5s with label
  "Create a contradiction"), DfPx (circle of ~60 dots, % counting down 90% → 34%, dots turn
  green → white/gray as quality drops), DexJ (orbiting dot ring around video card; 1000-comments
  dot grid — see #24).
- **Spec:** dots scatter/fade in over ~1s into a loose circle or grid; individual dots change color
  on the spoken word; a % or label updates beside them. Sound: [UNVERIFIED].

### 22. Point-follow (element appears where he points / he points at it)
- **Reels:** DfZ (card drops where he points up ~9.8s), DfX2 (chips/cards appear where he points),
  DfSf (mini video card drops in exactly as Sky points UP at it ~9.8s), DfIY (format cards appear
  where he points up), DfDu (format cards appear where he points ~4.0s), Dez4 (Sky points up at
  script-structure panel ~43.0–44.5s and at #2 card ~50.5–52.0s), DexJ (points up at structure
  panel ~0.0–0.5s).
- **Spec:** the element's entrance is timed to the gesture — it appears in the space his finger is
  pointing at, on the exact frame his hand arrives. The pointing hand is the cue, not the voice.
  This is a core Sky device: the diagram is "summoned" by the gesture. Sound: [UNVERIFIED].

### 23. Blur / whip transition
- **Reels:** DfU49 (blur/whip frame at ~12.0s, ~31.8s on Sky↔subject hard cuts), DfX2 (blur/whip
  ~6.5–7.0s).
- **Spec:** a single blurred/whip frame bridging a hard cut between Sky and subject footage (or
  between two Sky framings). Lasts ~1–2 frames. Rare — most cuts in these reels are straight hard
  cuts. Sound: [UNVERIFIED — likely a whoosh].

### 24. Dot-grid data viz (1000 comments)
- **Reels:** DexJ only (~17.5–22.0s).
- **Spec:** ~10×10 grid of orange dots fills in at chest ~x400–700, y480–700 over ~0.5s; cursive
  label "1000 comments" at left; left columns turn GREEN (~19.2s, 100 people "Who want to work
  with us"); right portion turns YELLOW-GREEN (~21.0s, 700 people "Who got nurtured with a free
  resource"); a wall of comment rows rains in from the top behind it. The grid IS the data —
  color segments are the segments. Sound: [UNVERIFIED].

### 25. Caption-document build (section type-in)
- **Reels:** DexJ only (~24.5–56.0s — the reel's second half).
- **Spec:** a caption document panel top-left ~x100–500, y40–260+ with a dashed vertical connector
  line down its left edge; sections type in one at a time as he explains them: Introduction (red),
  Struggle (yellow), Rise (blue), Proof (teal), Unique Mechanism (pink), Expectations (white),
  Two-Door CTA (green) — each title + its caption text typing in line by line. The document grows
  downward and SCROLLS upward at the close (~53.8s). The chest head constellation changes color
  state with the section (white → red on Rise → green on Proof). Sound: [UNVERIFIED — likely a
  typing sound per line].

### 26. Movie-still / reaction flashcard montage
- **Reels:** DfLa only (~7.0–14.0s, ~42.0–43.0s, ~55.0–60s).
- **Spec:** frame goes BLACK; small rounded-rect movie stills flash one at a time center
  ~x100–500, y100–350, each ~1s, with a white word label over it and a slight Ken Burns scale-in:
  "Powerful / Visual" Iron Man ~7.0s, "Visceral" bald man flexing ~7.5s, "Addicting" Bradley
  Cooper ~9.5s, "Cancerous" Morpheus ~10.5s, "Money Printing" Wolf of Wall Street ~11.0s,
  "Soul Sucking" whale/dark ~11.5s, "Luck Magnet" Harry Potter ~12.0s, "Moonshot" rocket launch
  ~13.0s. Thanos snap still pops top-right of bottom half ~42.0–43.0s. PIP reaction clips (two
  Italian guys reacting, cooking video) dock at right ~55.0–60s. This is the closest thing to a
  meme/reaction pop in Sky's own grammar — and it is movie stills, not meme stickers.
  **Classic meme/GIF sticker pops (Carter-style small reaction stickers with sound) were NOT seen
  in any of the 14 Sky reels.** Sound: [UNVERIFIED].

### 27. Quote card (type-in)
- **Reels:** DfQ4 ("THE UNPOPULAR TAKE" — "Plastic will be a net positive for society…" types in
  character by character ~53.0–56.5s, ~0.15s/char, with a timeline below), DfLa (hook/body/CTA
  bar), Dez4 ("Insight:" cards).
- **Spec:** white card top-center ~x400–700, y60–220, accent title above; text TYPES in character
  by character (~0.15s/char); a small diagram/timeline sits below the card. Sound: [UNVERIFIED —
  likely a typing sound].

### 28. Balance scale / comparison device
- **Reels:** DfQ4 ("1 Demo = 10x Trust" — scale tilts left, then right as "X10 Talking Heads"
  loads ~26.0–28.5s), DfPx (creator A/B follower bars growing side by side; Venn overlap),
  DfDu (audience vs customer split with heads turning red), Dez4 (#1 vs #2 option cards).
- **Spec:** two sides drawn ~0.5s apart; the scale/bar TILTS toward the winning side on the spoken
  word; the losing side dims. Sound: [UNVERIFIED].

### 29. Org chart / tree
- **Reels:** DfIY ("MY CONTENT TEAM" org chart ~10.5–15.0s, 3 columns), DfA9 ("BRAND DIRECTION"
  tree — head at left, branching lines to 5 options, "Problem Solver" highlights orange ~22.0s).
- **Spec:** title bar top-center; branches/lines draw from a central head to option pills;
  options appear one at a time (~0.3s apart); the chosen one highlights in accent. Sound:
  [UNVERIFIED].

### 30. Head crowd / audience multiplication
- **Reels:** DfDu (head cloud ~20 heads, turns gray one by one ~2.5s), DfA9 (head constellation),
  De-A2 (head cluster turns red ~12.5s), Dez4 (crowned head + crowd growing 6 → 15 heads
  ~34.5–38.0s), DexJ (head constellation, comment wall).
- **Spec:** heads multiply outward from a center point over ~1–3s; the crowd changing color
  (gray / red / green) marks the audience's state change. Sound: [UNVERIFIED].

### 31. Payment / proof pills (count-up)
- **Reels:** Dez4 only (~57.2–58.9s).
- **Spec:** two payment pills pop in at chest: "High-ticket client #1" counting $0.00 → ~$18,000.00
  and "High-ticket client #2" counting $0.00 → ~$17,955.00 [UNVERIFIED exact intermediate values].
  Tied to "landing me two high-ticket retainer clients". Sound: [UNVERIFIED].

### 32. Timer (counting seconds)
- **Reels:** DfPx (10-second timer "00:10 sec" center ~19.5–21.0s [values jump — UNVERIFIED exact
  sequence]), DfDu (watch-time timer 0s → 38s under "Storytelling videos" card ~44.5–46.0s),
  Dez4 (60-sec timer counting up 7 → 19 → 30 → 42 → 60 sec ~4.0–5.0s; 60-sec progress arc with
  timer labels 21 → 37 → 43 → 54 → 60 sec ~16.5–19.0s), DfA9 ("0:40" timer pill on LINES panel
  ~21.5s).
- **Spec:** small timer text/pill near the element it times; counts in jumps (not smooth 1-by-1);
  used to make "60 seconds isn't enough" / "watch time" concrete. Sound: [UNVERIFIED — likely
  ticking].

### 33. Brain / glow head effect
- **Reels:** Dez4 only (~7.5–10.0s).
- **Spec:** Sky's own head goes WHITE/SILVER — a glowing brain-like texture washes over his hair
  and head ~7.5–8.5s, fading ~9.5s. [UNVERIFIED exact mechanism — looks like a white brain overlay
  tracked to his head, or a desaturate+glow grade on the head region only.] Tied to "how deep your
  knowledge actually is". Sound: [UNVERIFIED].

### 34. Label cascade (annotation pills stacking)
- **Reels:** DfU49 (HUD label cascade stacking to 3 lines then resetting: QUICK TIP →
  INTERACTIVE EXERCISES → "Let's do a meditation" → "I bet I can hypnotize you" → "People stay
  to participate ✓"; then "Stay to the end → Explain dampness / Give action items → Why herbs →
  More visual / Easier and faster fixes").
- **Spec:** small white pills with accent text stack vertically at top, one at a time (~0.5s apart),
  up to 3 lines, then reset. Sound: [UNVERIFIED].

### 35. Authority / trust bars
- **Reels:** DfX2 (authority bars ~23.2s, Leila's ~2× His; play buttons + Audience trust bar
  ~35.0–35.5s), DfTawo (legitimacy meter, bar fills with green dots, "Proof = +1 Legitimacy"),
  DfDu (authority meter bar fills ~38.5–40.0s, yellow "!" badge), DfA9 (two-curve chart: blue bell
  vs orange S-curve crossing).
- **Spec:** horizontal bars grow left-to-right or fill with dots on the spoken claim; a comparison
  bar shows the gap (Leila's ~2× His). Sound: [UNVERIFIED].

---

## PER-REEL TIMELINES

Timestamps ±0.3s. Coordinates 0–1000. Full detail lives in `notes_<ID>.md`.

### DfZ_q_pFbX1 — "Why Process Crushes" (@allanpeters) — 37.2s — GREEN
Full notes: `notes_DfZ_q_pFbX1.md`

| Time | Device | Where | Motion | Speech tie |
|---|---|---|---|---|
| 0.0–1.5s | Floating mini video card | top-center x480–620, y0–180 | in from frame 1 | @allanpeters, 1.9M |
| 0.8–2.8s | Dashed orbit line | around card | draws | — |
| 1.0–1.5s | Title build "Why / Process / Crushes" | center-lower | word-by-word, glow | "Why process crushes" |
| 2.2–3.0s | Little heads orbit (3 heads around card) | around card | orbit in | — |
| 3.0s | Green "+" icon | near card | pop | — |
| 4.2–7.0s | Montage strip (Montage 1/2/3) | top | slides, collapses back to IG post UI mockup (heart 96K, 1.9M) | montage of his work |
| 9.8s | "The 2 Things" checklist slides in from right | right, x600–980 | slide-in | "the 2 things" |
| 10.2s | Checklist row 1 fills green | panel | fill | thing 1 |
| 13.0–14.8s | Head + green arrow annotation | mid-frame | pop; red label text [UNVERIFIED] | annotation beat |
| 14.8–15.8s | Full-screen B-roll cut | full frame | hard cut | hands drawing "N" logo |
| 15.8–19.5s | Feeling/words mapping stack | center | stack builds: feeling "something's off" → words "points are different sizes" → = expert ~17.2s | "feeling vs words" |
| 19.5s | Checklist row 2 fills green | panel | fill | thing 2 |
| 21.5–22.8s | "The Whole Process" 3 cards + connecting line | top-center | cards pop, line draws | "the whole process" |
| 22.8–23.5s | "Final result" card morph | center | morph from process cards | "final result" |
| 23.5–27.5s | Satisfying 3D dice/blocks B-roll | full frame | hard cut, plays | process payoff |
| 29.8s | IG profile card slides in top-left | top-left | slide-in | his profile |
| 30.2–32.5s | Thumbnail cloud (~10 thumbs fan out) | top | fan out | his body of work |
| 33.5–37.2s | Checklist recap + final-result card slides in from right, dashed connectors | right → center | slide-in | recap; ends on diagram, no end card [UNVERIFIED final frame] |

### DfX2qwQGagM — "Good Content Strategy" (Leila Hormozi content filter) — 53.9s — GREEN
Full notes: `notes_DfX2qwQGagM.md`

| Time | Device | Where | Motion | Speech tie |
|---|---|---|---|---|
| 0.0–0.8s | Opening title "Good Content Strategy" (green, lower-left) | lower-left | fade/slide in | "good content strategy" |
| 0.8–2.8s | Funnel icon "STRATEGY" top-center, white pills raining in | top-center | pills rain in one at a time | strategy funnel |
| 3.0s | One green pill drops out of funnel | funnel | drop-out | the filter rejecting |
| 6.5–7.0s | Blur/whip transition | full frame | 1–2 frame whip | cut to profile build |
| 7.0–9.5s | IG profile card builds in stages | top-center | avatar → text → Follow/Message buttons | @leilahormozi, 3.8M |
| 10.8–11.5s | Trait chips pop one at a time | mid-frame | pop: "Extremely empathetic", "Great people skills", "Elite operator", "Great leader" | her traits |
| 11.8s | "LEILA CONTENT FILTER" glass panel | top-center | slide-in; dashed connectors from chips | "the Leila content filter" |
| 14.8s | Filter row verdict: "Top 5 marketing paid ads" red X | panel row | X stamps in | rejected idea |
| 20.5s | Filter row verdict: "Retaining A plus talent" green check | panel row | check fills | accepted idea |
| 22.5s | Little head + green triangle marker | mid-frame | pop | marker on her |
| 23.2s | Authority bars (Leila's ~2× His) | mid-frame | bars grow | authority gap |
| 23.5s | Filter row verdict: "Reaction videos" red X | panel row | X stamps in | rejected idea |
| 27.5s | Filter row verdict: "Day in the life" green check | panel row | check fills | accepted idea |
| 30.5–32.0s | Chip orbit around thumbnail | around card | chips orbit: "Great boss", "Leader", "Excellent operator" | orbiting traits |
| 33.5s | Filter row: "Rankings videos" | panel row | row fills | — |
| 35.0–35.5s | Play buttons + Audience trust bar | mid-frame | bar fills | trust |
| 39.5s | Filter row: "Demonstrations" | panel row | row fills | — |
| 44.0s | Panel exit + "SHOW HER IN HER ELEMENT" label | center | panel flies off, label pops | "show her in her element" |
| 45.2–46.2s | Tag chips lighting green on word | mid-frame | light up: "decisions", "moving", "her team" | tags |
| 45.5s | Still → playing video in card | card | still starts playing | her element |
| 47.5s | "boring" tag + head + green arrow | mid-frame | pop | "boring" |
| 49.5–50.5s | Staircase chart "BORING TO YOU, GOLD TO THEM" draws left-to-right | top-center | line draws | staircase |
| 51.0–52.0s | Pulsing green dots on staircase | chart | pulse | — |
| 52.2–52.8s | Full-screen tennis B-roll, green "GREAT ATHLETE PRACTICE" | full frame | hard cut | practice analogy |
| 52.8–53.9s | Ends on Sky, no end card [UNVERIFIED final 0.3s] | — | — | — |

### DfU49SJAFYH — TCM practitioner 1.1M-view video, retention breakdown — 103.8s — GREEN
Full notes: `notes_DfU49SJAFYH.md`

| Time | Device | Where | Motion | Speech tie |
|---|---|---|---|---|
| 0.0s | Word-by-word white captions center-lower (~y560–600) | center-lower | per word | whole reel |
| 0.8s | Floating mini video card top-center, "1.1M" label sliding down | top-center | slides down ~0.8s | the 1.1M video |
| 2.8s | Retention-graph panel slides in from right, persists top-center as analysis HUD | top-center | slide-in, then persists | retention graph |
| 2.8–5s | HUD pill label updates per beat | panel | label swaps: Throat mucus → Broader term → Intentional drop → Hook filtering ✓ → Bad drop → Basically flat ✓ → Spleen → Fluids | each analysis beat |
| 7.8–9.8s | Photo pop-up (phlegm) | center chest x420–580, y430–520 | hard in/out | phlegm |
| 12.0s | Blur/whip frame (hard cut Sky↔subject) | full frame | 1–2 frames | cut to subject |
| 31.8s | Blur/whip frame (hard cut) | full frame | 1–2 frames | cut |
| 33.5–41.5s | Photo pop-up (spleen diagram) | center chest | hard in, holds 8s, hard out | spleen |
| 59.5–61.5s | Flow-diagram build Spleen→Fluids / Phlegm←Dampness | center | nodes appear, lines connect; labels "Every line connects" + "No aggressive switches" | flow |
| 65.8s | Flow diagram fades | center | fade out | — |
| 67.5–69.2s | Photo pop-up (tongue) | center chest | hard in/out | tongue |
| ~70–90s | HUD label cascade stacking to 3 lines then resetting | top | pills stack: QUICK TIP → INTERACTIVE EXERCISES → "Let's do a meditation" → "I bet I can hypnotize you" → "People stay to participate ✓"; then "Stay to the end → Explain dampness / Give action items → Why herbs → More visual / Easier and faster fixes" | retention tactics |
| whole reel | Slow push-in on Sky [UNVERIFIED rate] | full frame | gentle continuous zoom | — |
| 103.3–103.8s | Ends on Sky, no end card [UNVERIFIED final 0.5s] | — | — | — |

### DfTawo5jHMH — "The 4 Questions Filter" — 59.7s — GREEN
Full notes: `notes_DfTawo5jHMH.md`

| Time | Device | Where | Motion | Speech tie |
|---|---|---|---|---|
| 0.2–3.8s | Quiz panel, 3 answer rows appear one at a time | top-center | rows pop; red X on rows 1–2 + green "?" on row 3 ~1.8–2.2s | quiz |
| 3.8–9.5s | Document stack: cards fill green = Post, turn red = Do not post ~8.2–8.8s, fly off up ~9.5s | center | fill, color change, fly off | post / do not post |
| 9.5–14.5s | Funnel diagram: format labels fly in (Duet ~11.5s, Quiz ~11.8s, Tutorial ~12.0s); green dot drops ~12.5s; labels orbit with red/green dots | top-center | fly in, orbit | formats funnel |
| 15.8s | "The 4 Questions Filter" panel appears (recurring) | top-center | slide-in | "the 4 questions filter" |
| 17.2–19.5s | iPhone mockup slides in from top-right (IG profile, 100,000 followers, small bounce) | top-right | slide-in + bounce | profile |
| 20.5–22.5s | Question 1 panel + video-call window | top-center | pop | question 1 |
| 21.0s | Filter row Q1 fills green | panel | fill | "Did a favourite client say it" |
| 22.5–29.8s | Head constellation (5 heads); center gets green glow ring + crown ~23.5s; splits into green "least favorite" / red "least profitable" boxes ~27.5–29.0s | mid-frame | heads pop, crown, split | favorite vs profitable |
| 30.5s | Filter row Q2 fills green | panel | fill | "Does it build trust?" |
| 31.5–34.5s | Content Script panel: "Proof/Stories" labels ~32.2s, green row highlight ~33.5s | top-center | rows appear, highlight | script |
| 34.5–37.0s | Legitimacy meter: bar fills with green dots, "Proof = +1 Legitimacy" | mid-frame | fill | legitimacy |
| 37.2s | Filter row Q3 fills green | panel | fill | "Does it fit my brand" |
| 37.5–43.5s | Personality trait strip (5 thumbnails: Relatable, Advice, Authoritative, Nice, Helpful); connector lines to "You" ~39.0s; highlights per named trait ~41.0–43.0s; flies off up ~43.5s | top | thumbnails pop, lines draw, fly off | traits |
| 44.5s | Filter row Q4 fills green | panel | fill | "Does it help my goal" |
| 45.0–46.0s | Pick One Goal: "Hiring / Leads / Impact" pills | mid-frame | pop | goal |
| 50.8–56.5s | Match Your Wording: "HIRING" card slides in left ~51.5s, "BUYERS" right ~53.2s, HIRING dims ~56.0s | left/right | slide-in, dim | wording match |
| 56.5–58.5s | Content Filter recap | top-center | panel returns | recap |
| 58.5–59.7s | Ends on Sky, no end card [UNVERIFIED final 0.2s] | — | — | — |

### DfSf5v8j73o — "Drop-offs you actually want" (retention deep-dive, same TCM video) — 56.7s — GREEN
Full notes: `notes_DfSf5v8j73o.md`

| Time | Device | Where | Motion | Speech tie |
|---|---|---|---|---|
| 1.2–3.5s | Retention graph draws (empty glass panel top-left x30–480, y60–200; green line draws left-to-right, glowing dot at leading edge ~1.5–2.8s; axes + "34%" endpoint) | top-left | line draws | retention |
| 2.0–3.5s | Big title build: "Drop" green → "Drop-offs" big green center x300–700, y480–620, "retention" small white above, "you actually want" white below; words stagger in | center | stagger-in | "drop-offs you actually want" |
| 3.8–7.2s | Flat-line morph: graph line morphs to FLAT ~85%, area under fills solid green left-to-right ~4.5–6.0s; pill "Everyone" ~7.0s | panel | morph + fill | flat retention |
| 9.5–11.5s | Mini video card + pointing: TCM card dashed border "1.3M" drops in from top-center x480–620, y0–180 exactly as Sky points UP at it ~9.8s | top-center | drop-in on point | the video |
| 11.0–15.5s | Graph slides in from right, docks next to card x480–980, y60–200; labels "0:03 to 0:05" + "Steep drop-off" ~12.5s, "Lead filtering" green pill ~14.5s | top-right | slide-in, labels pop | steep drop-off |
| 16.0–26.0s | Script lines diagram: glass panel top-left x30–480, y60–260; horizontal lines draw one at a time ~16.0–17.5s (white "Hook", RED "Lead" lines bracketed, GREEN line, white lines); red "Lead" lines PULSE/glow red ~18.0s; ~22.0s small head cutouts appear at panel's right edge x900–980, y60–120, row growing to ~6 by ~24.0s, drifting right and fading ~25.5s | top-left | lines draw, pulse, heads grow | script lines |
| 26.5–29.8s | Graph with heads on curve: 3 small heads sit ON graph's curve x350–500, y200–260 ~27.0s | graph | pop onto curve | heads on curve |
| 30.5–31.2s | "LEAD FILTER" title type-in, big green, center | center | type-in | "lead filter" |
| 31.2–38.8s | Subject full-screen cut (TCM clip full frame); phlegm photo pop ~36.5–38.5s center chest | full frame / chest | hard cut, photo hard in/out | subject clip |
| 38.8–44.5s | Hook text reveal: top-left text block builds line by line ("Here's why you constantly have throat mucus" white + green "throat mucus" ~38.8s; bullets ~39.5s, ~40.5s; second block ~41.0–42.0s; green sub-bullets ~42.0s, ~43.0s) | top-left | lines type in | the hook |
| 44.5–48.0s | Lead filtering checklist: dark glass panel top-left x30–480, y60–260; checkbox rows tick green one at a time ("Tried a bunch of fixes" ~45.0s checked ~45.5s, "Gone to the doctor" ~46.0s checked ~46.5s, "Gone nowhere" ~47.0s checked ~47.5s) | top-left | rows appear, checks tick | lead filtering |
| 47.5–49.0s | Clear answer + head: green title "Clear Answer" top-right; checklist panel slides right; head cutout (TCM practitioner, green ring) at right x850–980, y200–300, dashed line to panel | top-right | slide, head pop | clear answer |
| 49.5–56.7s | Graph return + end title: "Sold off" pill at graph's right end ~55.0s; final big text "WARM & SOLD" center x300–700, y560–620 types in ~55.8–56.5s ("WARM" white + "& SOLD" green) | center | type-in | "warm & sold" |

### DfQ4E1Hjn0n — "5 Content Types" (100k in 6 months) — 75.6s — GREEN
Full notes: `notes_DfQ4E1Hjn0n.md`

| Time | Device | Where | Motion | Speech tie |
|---|---|---|---|---|
| 0.0–2.2s | "5 CONTENT TYPES" checklist (green title top-left x60–300, y30–60 + 5 white rows appear one at a time ~0.0–1.2s: "01 Gamification", "02 Demonstration", "03 Borrowed Attention", "04 Niche Philosophy", "05 Storytelling"); recurring — current row highlights green when its section starts; returns ~6.0s (01), ~17.0s (02), ~31.5s (03), ~44.5s (04), ~60.5s (05), ~70.5s full recap | top-left | rows pop, highlight per section | the 5 types |
| 2.2–6.0s | Phone mockup + growth bar: title "100k in 6 Months" (white "100k in" + green "6 Months") top-center; iPhone mockup drops in ~2.2s (IG profile "travelprofile", 100K followers); horizontal progress bar below phone ~3.5s ("month 1" left, "month 6" right); green fill animates left-to-right ~3.8–5.5s | top-center | drop-in, bar fills | 100k in 6 months |
| 7.2–8.8s | Tier list card: white card top-right x700–950, y40–200 titled "Lists, Rankings, tiers"; S/A/B/C tier rows with small gray squares filling one at a time ~7.5–8.5s | top-right | rows fill | tier lists |
| 8.8–13.2s | Burger B-roll: full-screen close-up Big Mac being built; "Zero Value" white text center ~12.5s | full frame | hard cut | "zero value" |
| 13.2–16.5s | "DRIVES EYEBALLS" counter: green/white title top-center + eye icon + VIEW COUNTER counting up rapidly 10,317 → 133,751 → 377,355 → 638,252 → 785,785 → 891,063 → 947,315 → 983,792 → 997,886 ~13.5–15.0s, then "1,000,000 Views" ~15.0s; branch diagram: eye connects via green lines to 4 white bars "other 4 formats" ~15.2–16.0s | top-center | count-up, lines draw | drives eyeballs |
| 19.5–23.0s | Phone mockup "SHOW IT LIVE": phone drops in top-center, green/white title above; phone screen shows live video + LIVE badge; labels pop around phone: "Product" left ~20.5s, "Service" right ~21.5s, "Coaching" left ~22.0s | top-center | drop-in, labels pop | show it live |
| 25.8–30s | Balance scale: title "1 Demo = 10x Trust" top-center (green "1 Demo" + white "= 10x Trust"); white scale line draws ~26.0s with green "Demo" weight on left pan and white triangle on right; scale TILTS left down ~26.5s, then "X10 Talking Heads" label loads right ~28.0s and scale tips right ~28.5s; tilts back and forth | top-center | draw, tilt | 1 demo = 10x trust |
| 32.5–36.0s | Format cards trio: three dashed-border video cards drop in top x40–980, y40–220 with green labels: "Stitches" ~32.5s, "Reactions" ~33.2s, "Green Screens" ~33.8s; title above morphs to "Borrow Their Attention" ~35.5s | top | drop in, title morph | borrow attention |
| 36.0–38.0s | Big creator / you diagram: big "Big Creator" circular head left x60–200, y130–260 (green ring, ~2.5× You head) + small "You" head right x700–780, y150–220, label "reputation + attention" below; green connector line draws between them ~37.0s | top | heads pop, line draws | big creator vs you |
| 46.0–52.5s | Dot constellation: title "Against Everyone" green top-center; ~15 white dots scatter into loose circle x380–700, y80–220 ~46.0–47.0s; one dot turns GREEN ~48.5s with tiny label "Create a contradiction" [UNVERIFIED exact]; more tiny text under it ~50.5s; green dot pulses | top-center | scatter, color change, pulse | against everyone |
| 52.5–58.5s | "THE UNPOPULAR TAKE" quote card: white card top-center x400–700, y60–220, green title above; text TYPES in character by character ("Plastic will be a net positive for society…" ~53.0–56.5s, ~0.15s/char); timeline below: "today" green dot ——— "+100 yrs" green dot ~53.5s | top-center | type-in | unpopular take |
| 62.5–70.5s | Brand longevity wave chart: title "Brand Longevity" green top-center; axes frame draws ~62.5–63.5s; dotted SINE WAVE draws left-to-right ~64.5–67.5s with green dots at peaks/troughs; labels pop at peaks: "Superfans" ~68.0s, ~69.0s, ~69.5s | top-center | axes draw, wave draws, labels pop | brand longevity |
| 70.5–75.6s | Ending full checklist recap; ends on Sky mid-word "Good…" [UNVERIFIED final frame] | top-left | panel returns | recap |

### DfPxqFPAY4_ — "Viral Twice" (collab posting) — 77.5s — GREEN
Full notes: `notes_DfPxqFPAY4_.md`

| Time | Device | Where | Motion | Speech tie |
|---|---|---|---|---|
| 0.2–1.5s | Phone mockup IG post UI: small phone top-center x480–620, y0–180 showing IG video post with like/comment/share rail on right edge | top-center | drop-in | the post |
| 1.5–4.5s | Double-peak chart: glass panel top-center x400–980, y40–200; green line draws DOUBLE PEAK (two humps) ~1.5–2.8s; labels "Wave 1" / "Wave 2" above each peak ~2.5s; "x2" at right ~3.2s | top-center | line draws, labels pop | two waves |
| 1.8–5.0s | Big title "VIRAL TWICE": big green text center-lower x300–700, y520–620 slides in from left ~1.8s, "one video go" white small above | center | slide-in | "viral twice" |
| 4.8–5.5s | Collab chip: green pill top-left x350–700, y60–120 "Creator A and Creator B" with two avatars — pops in | top-left | pop | "collab posting" |
| 7.2–8.2s | "KILL THEIR REACH" text: big white "kill their" + huge green "REACH" center-left x30–350, y480–620 — emphasis slam-in on punch word | center-left | slam-in | "kill their reach" |
| 9.2–11.5s | Schedule checklist: glass panel top-center x350–950, y40–220; rows "1 First Push" green check "Done viral x1" ~9.8s, "3 day break - no posts" dim, "5 Second Push" green check "Viral again x2" ~10.2s; numbered steps 1 and 5 with timeline | top-center | rows appear, checks tick | the schedule |
| 11.5–15.0s | Views-over-time chart: dark panel top x400–980, y40–200; "Views over time" + counter climbing 39K → 40K → 53K → 186K → 458K → 447K → 450K; green S-curve draws with "Ceiling" red label ~12.5s | top | counter climbs, curve draws | views over time |
| 13.0–15.5s | "STEP 1" title + progress bar: big white "STEP 1" center x300–700, y560–660 + 2-step progress bar below (step 1 green filled "Who posts first", step 2 dim "Add the collaborator") | center | title pops, bar fills | step 1 |
| 14.0s | Creator A/B avatars: small heads "CREATOR A" left / "CREATOR B" right at mid-frame ~y480 with green play triangle between them | mid-frame | pop | creator A/B |
| 15.5–19.5s | "2 WAVES, NOT 1" chart: panel top-center; title; bell curve draws with "One big push" label; SECOND bell curve draws ~17.0s with "Wave 2" label + "x2" at right ~17.5s; both waves fill green | top-center | curves draw, fill | 2 waves not 1 |
| 17.8–19.5s | "CRUCIAL" text: big green "Crucial" center x450–700, y560–620 types/slides in | center | type/slide in | "this is crucial" |
| 19.5–21.0s | 10-second timer: small "00:10 sec" timer text center x450–550, y620–660 counting [values jump 00:10 → 00:02 → 00:05 → 00:09 → 00:10 — UNVERIFIED exact sequence] | center | counts | 10 seconds |
| 20.5–23.0s | Follower bars: two vertical green bars grow upward — left "CREATOR A" counter 62K → 109K → 128K; right "CREATOR B" 41K → 72K → 84K; green play triangle between them; "Post" pill ~22.5s | mid-frame | bars grow, counters climb | follower growth |
| 22.5–23.5s | Story share notification: Creator A head with rainbow ring + green pill "Story shared" pops top-left x40–300, y40–120 | top-left | pop | story shared |
| 23.0–30s | Views chart return: counter climbs 101K → 288K → 759K → 1.1M → 1.2M → 1.3M → 1.4M → 2.0M → 2.6M → 2.7M ~23.0–29.0s with S-curve drawing; labels "Plateau" ~26.5s, "Second push" green pill ~28.5s | top | counter climbs, curve draws | second push |
| 30.5s | "NEW SURGE" fill: second hump fills solid green with "New surge" pill | chart | fill | new surge |
| 33.5–35.5s | "INTERESTED" text: big green "Interested" + white "in this topic again" center — word-by-word reveal | center | word reveal | "interested in this topic again" |
| 35.5–38.5s | Profile grid wall: 3×3 wall of IG profile cards drops in top-center x350–950, y40–250 with dates "3 days ago", "1 year ago"; two more cards top-left with "3 months ago" / "1 year ago" + heart icons ~37.5s | top | drop in | profile grid |
| 38.0–39.0s | "SECOND WAVE" title: big white center x300–700, y560–620 slides in | center | slide-in | "it caught that second wave" |
| 39.0–45.0s | Collab UI walkthrough: Creator A head rainbow ring top-left; green video card with play button center-top x480–650, y200–420; menu pops "Edit / Tag people / Invite collaborator" ~42.0s, "Invite collaborator" highlighted green ~42.5s; dropdown "Creator B" green check, "Creator C", "Creator D" ~43.0s; "Creator B" selected ~43.5s; card morphs to "Creator A and Creator B / Collab post" dual-avatar header ~44.0s | top | menu pops, selection, morph | invite collaborator |
| 44.5–47.5s | Story share + view counter: Creator B head rainbow ring + green pill "Story shared" top-left; green video card gains IG UI rail (heart/comment/share) on right edge ~45.5s; view counter at card bottom: "1.4M" ~47.0s → "2.5M" ~47.5s | top-left / card | rail appears, counter climbs | story shared |
| 50.5–51.5s | "COLLAB" title: big green "Collab" + white "Should you even" center | center | pop | "should you even collab" |
| 52.0–55.5s | Audience quality dot cloud: circle of ~60 dots (white + green) top-center x400–700, y40–220; label "Audience quality" + % COUNTING DOWN: 90% → 84% → 53% → 35% → 34% ~52.5–54.0s, % turns RED as it drops; dots turn green → white/gray as quality drops | top-center | dots change color, % drops | audience quality |
| 56.0–60s | Product cards: Creator A head + "Dog treats $$$ / Shop now" card slides in left ~57.5s; Creator B head + "Cat leashes $$$ / Shop now" card slides in right ~58.5s; dashed line + "Creator A and Creator B" dual header connects them ~59.0s | left/right | slide-in, connector draws | product mismatch |
| 60.0–61.5s | Mismatch labels: red "Poor audience match" ~60.0s; red "Views ≠ Potential Customers" ~61.5s under cards | under cards | pop, red | poor match |
| 63.5–66.0s | Product swap: "Dog treats" card morphs to "Luxury contractor" house photo ~64.0s; "Cat leashes" morphs to "High-end home designer" ~65.5s; "Strong audience match" green text ~67.5s | left/right | morph | strong match |
| 70.5–75.5s | Venn diagram: two circles draw ("Your audience" left, Sky's head on top + "Their audience" right, other creator's head); circles slide together ~73.0s and OVERLAP; overlap lens fills GREEN ~74.0s | top-center | draw, slide, overlap fill | audience overlap |
| 75.5–77.5s | Ending: Venn fades; "Follow for content" ~76.0s; final frames DESATURATE TO BLACK AND WHITE ~76.5–77.5s slow fade to B&W as he looks down | full frame | slow desaturate | close |

### DfLaEFNDKkv — "Power Words" (unskippable hooks) — 93.9s — GREEN
Full notes: `notes_DfLaEFNDKkv.md`

| Time | Device | Where | Motion | Speech tie |
|---|---|---|---|---|
| 0.2–2.0s | "WAY TOO GOOD" title: white "This sounds" + big green "WAY TOO GOOD" + white "to be true" center-lower x300–700, y500–660; words stagger in ~0.2s, ~0.5s, ~0.8s, ~1.0s | center | stagger-in | "this sounds way too good to be true" |
| 2.2–5.5s | IG Reels phone mockup + color isolation: full IG Reels phone UI slides in from right x450–950, y40–480 (Sky's own reel playing with "unskippable" overlay, heart/comment/share rail right, "realskytan" + Follow button, caption + comment bar); ~3.0s background behind phone goes BLACK AND WHITE while phone stays in color; ~4.0s "POWER" green text on phone screen, ~4.5s "POWER WORDS"; phone slides out right ~5.2s; color returns ~5.5s | right | slide-in, B&W isolation, slide-out | power words |
| 5.5–7.0s | "POWER WORDS" title + sublabels: big green center x400–650, y520–660 + small white "Adjectives" right ~5.8s; "Terms" label pops left ~6.5s, "Phrases" right ~6.8s | center | title pops, labels pop | power words |
| 7.0–14.0s | Movie-still flashcard montage: frame goes BLACK; small rounded-rect movie stills flash one at a time center x100–500, y100–350, each ~1s, word label in white over it, slight Ken Burns scale-in: "Powerful / Visual" Iron Man ~7.0s, "Visceral" bald man flexing ~7.5s, "Addicting" Bradley Cooper ~9.5s, "Cancerous" Morpheus ~10.5s, "Money Printing" Wolf of Wall Street ~11.0s, "Soul Sucking" whale/dark ~11.5s, "Luck Magnet" Harry Potter ~12.0s, "Moonshot" rocket launch ~13.0s | center | flash, scale-in | power words examples |
| 15.5–17.5s | "MORE EFFECTIVE" text + hook/body/CTA bar: "how easy" white + "More effective" green + "your hooks become" white center-lower; below, 3-segment bar "Hook" \| "Body" \| "CTA" filling green left-to-right ~16.0–17.0s | center-lower | text pops, bar fills | more effective hooks |
| 17.5–93.9s | Split-screen screen recording: frame splits horizontally — TOP half = screen recording (Claude chat, dark UI); BOTTOM half = Sky side-profile narrating, looking at screen; "Rewriting hooks" title appears top ~22.5s with numbered list of 5 hooks below ~23.0s filling in line by line; list's hook lines HIGHLIGHT GREEN one at a time as he reads them: hook #1 ~29.5s, #2 ~37.5s, #3 ~47.0s, #4 ~62.5s, #5 ~75.0s [approx — exact times UNVERIFIED] | split | split, list fills, highlights | rewriting hooks |
| 42.0–43.0s | Thanos snap still: small still of Thanos snapping (Avengers Endgame) pops top-right of bottom half x700–950, y500–620 | bottom-right | pop | "we've all watched endgame… the snap" |
| 55.0–60s | PIP reaction / B-roll clips: bottom half splits again — vertical video of two Italian guys reacting, one facepalming, docks right x700–950, y500–750 while Sky talks at left; cooking video (pasta pan) replaces it ~56.5s | bottom-right | dock, swap | reaction beats |
| 75.0s | Word-swap highlight: in hook #5 the word "draining" highlighted ORANGE — word-replacement edit "draining" → "destroying"; swap word glows orange in list | top list | highlight orange | word swap |
| 93.5s | Sky closes "…that was helpful"; no end card | — | — | close |

### DfIYshekeF3 — "ChatGPT ideas" / legit content strategy — 60.5s — GREEN
Full notes: `notes_DfIYshekeF3.md`

| Time | Device | Where | Motion | Speech tie |
|---|---|---|---|---|
| 0.0–2.8s | Format cards trio: three dashed-border video cards drop in top x400–980, y0–200 with green labels: "Stop Start Reaction" ~0.2s, "Tier list" ~1.2s, "Challenge Storytelling" ~2.0s; Sky points UP at them as each appears — cards appear where he points; fly off ~4.5s | top | drop in on point, fly off | formats |
| 2.8–4.2s | B&W + "STOP" text: frame goes BLACK AND WHITE; big white "Look I'm just gonna" + green "stop" + white "right there" center x100–500, y480–660, word-by-word ~3.0s, ~3.5s, ~4.0s; color returns ~4.2s | center | B&W cut, word reveal | "look I'm just gonna stop right there" |
| 5.0–9.5s | "CHATGPT IDEAS" screen: dark ChatGPT window slides in top-center x400–980, y40–280 titled "Chatgpt Ideas" with idea cards; window scrolls slowly downward ~5.5–9.0s revealing more rows | top-center | slide-in, scroll | ChatGPT ideas |
| 6.5–11.0s | Little heads with green "?": 5–6 small head cutouts across Sky's chest x300–750, y560–680, each with green "?" badge above — "confused audience" heads; one center head LARGER ~9.5s with "?"; heads bob slightly | chest | pop, bob | confused audience |
| 8.0–9.5s | "BEHIND THE SCENES" text: angled white/green text at right x600–950, y300–420 ("BEHIND THE SCENES / CONTRARIAN TAKES / NARRATIVE ARC / BREAKDOWN / BLUEPRINT") — lines appear one at a time | right | lines appear | behind the scenes |
| 10.5–15.0s | "MY CONTENT TEAM" org chart: green title bar top-center "My Content Team" x100–950, y40–80; 3 small columns below ~11.0s [UNVERIFIED content]; head with white arrow flies in from left ~11.5s; two cards slide in: green "VIEWS" card thumbnails ~13.0s and white "DOLLARS" card ~13.5s; DOLLARS numbers count up: $18,700 → $12,400 → $15,300 ~14.0–15.0s | top-center | chart builds, cards slide, counter | my content team |
| 15.0–22.0s | Inside/outside circle diagram: two concentric dashed circles top-center x400–700, y40–280 (inner "INSIDE" green with 3 heads, outer "OUTSIDE" white with ~8 heads + icons orbiting); outer heads drift around ring ~16.0–19.0s; ~20.0s outer heads fly away, inner circle expands; green fingerprint icon appears center ~20.5s inside single dashed circle | top-center | circles draw, heads orbit, fly off, expand | inside vs outside |
| 22.0–25.5s | Fingerprint circle + pills: dashed circle with green fingerprint icon persists; small green pills pop around it: "Sales call" ~22.5s, "Q&A's" ~23.2s, "Team calls" ~23.8s | top-center | pills pop | fingerprint |
| 25.0–30s | "EVENING THOUGHTS" Claude window: dark Claude chat window slides in top x400–980, y40–300 titled "Evening thoughts" with three pills at top; text types in: "Most Asked Questions" ~27.5s, "What Keeps Them Up At Night" ~28.0s, "Exact Words They Use" ~29.0s — sections appear one at a time | top | slide-in, type-in | evening thoughts |
| 30.0–34.5s | "KEY TERMS" chips + $ counter: "Key Terms" panel top with word chips ("invisible", "consistent", "leads not likes", "on camera", "no time", "posting into the void", "actually works"); green $ icon pops center-top ~31.0s; dollar amounts around it: $18,000 / $12,000 / $21,000 ~31.5–33.0s; $ icon flips to RED EYE icon ~34.0s with view counts 10,000 / 7,300 / 3,000 red — money vs views contrast | top | chips pop, $ flips to eye | key terms |
| 35.5–38.0s | Circle diagram returns: INSIDE/OUTSIDE concentric circles return top-center with fingerprint icon; "Explore" label at bottom ~36.5s | top-center | return | explore |
| 38.0–42.0s | Explore page screen: IG Explore grid (search bar "Search with Meta AI", tabs "For you / Content creation / Entrepreneurial Mindset") slides in top-center; grid scrolls ~39.0–41.0s; view counts under thumbnails: 2.9M / 349K / 728K / 104K / 156K ~40.5s | top-center | slide-in, scroll | explore page |
| 41.0–43.0s | Fan-out diagram: Explore grid shrinks to top; 5 thumbnails fan out below with green connector lines to head Sky at center-bottom; "3x your average" green pill ~42.0s, "last 90 days" label ~42.5s | top | fan out, lines draw | 3x average |
| 43.0–45.5s | "THE PROCESS" checklist: glass panel top-center, green title + 4 rows checking off one at a time ("Go internal first" ~43.5s, "Pull the key terms" ~44.0s, "Search explore" ~44.5s, "Pick 5 reels" ~45.0s, each gets green check) | top-center | rows check off | the process |
| 45.5–48.0s | Content ideas grid + counter: 3×3 thumbnail grid top-center with green counter pill: "2 CONTENT IDEAS" → "12 CONTENT IDEAS" → "23 CONTENT IDEAS" → "30 CONTENT IDEAS" ~45.5–47.0s — grid fills as counter climbs | top-center | grid fills, counter climbs | content ideas |
| 47.0–48.5s | Inside/outside Venn: two overlapping circles labeled "INSIDE" / "OUTSIDE" below grid x400–700, y300–420 | below grid | draw | inside/outside |
| 48.5–51.5s | Head constellation + view pills: cluster of heads with green dots top-right x700–980, y40–220; green view-count pills pop in one at a time at left: "1.2M" / "845K" / "2.4M" / "1.7M" / "840K" ~49.5–51.0s | top | heads pop, pills pop | view counts |
| 51.5–54.0s | Format card carousel: green card center-top x450–650, y100–320 with thumbnail grid inside; label cycles while card stays put: "TIER LIST" ~51.5s → "REACTION" ~52.5s → "YAPPING" ~53.0s → "LIVE DEMO" ~53.5s → "STORYTIME" ~54.0s | top-center | label cycles | formats |
| 54.5–58.0s | Proof cards trio: three dashed-border video cards drop in top x40–980, y40–250 with view labels: "1.3M" TCM practitioner ~54.5s, "3.5M" ~55.0s, "941K" ~55.5s; Sky points up at them | top | drop in on point | proof |
| 59.0–60.5s | "LEGIT CONTENT STRATEGY" checklist: glass panel top-center, green title + 6 rows appearing ("1 Go internal first", "2 Pull the key terms", "3 Search explore", "4 Pick 5 reels", "5 Repeat every term", "6 Wrap in a proven format" — last row highlighted green); ends on it | top-center | rows appear | legit content strategy |

### DfDuMnCjNdE — "Shallow formats" (why your audience doesn't value your opinions) — 68.7s — ORANGE
Full notes: `notes_DfDuMnCjNdE.md`
NOTE: shot in a BRIGHT living room (not the dark studio) — Sky in a black "RELEVANT" tee holding a mic.
ORANGE is the accent here — the only reel family with orange besides DfA9 / De-A2 / Dez4 / DexJ.

| Time | Device | Where | Motion | Speech tie |
|---|---|---|---|---|
| 0.0–3.8s | Head cloud + "?": cluster of ~20 small head cutouts floats above Sky's head x300–700, y0–200, growing from ~3 heads at 0.0s to full cloud by ~1.0s; orange "?" badge on top ~0.5s; ~2.5s heads turn GRAY/desaturated one by one (audience "going gray"); cloud fades ~3.8s | above head | grow, desaturate, fade | audience |
| 4.0–6.0s | Format cards trio: three dashed-border video cards drop in top-right x700–980, y40–250 with orange labels: "This or that" ~4.0s, "Rating" ~4.2s, "Tournament" ~4.8s; Sky points up at them ~4.0s | top-right | drop in on point | shallow formats |
| 6.0–7.0s | "SHALLOW FORMATS" bracket: three cards settle in row top-center; orange bracket line draws beneath them with cursive "Shallow formats" text below ~6.5s | top-center | bracket draws | "shallow formats" |
| 7.5–9.0s | Trait labels under cards: small white labels pop under each card one at a time ("Shorter" This or that ~7.5s, "Very rhythmic" Rating ~8.0s, "Fast paced" Tournament ~8.8s) | under cards | pop | traits |
| 10.5–13.5s | View counts + head explosion: under each card, view/like counts appear and climb (880K / 1.7M / 2.4M / 3.3M / 2.1M / 1.3M / 859K ~11.0–12.0s); then burst of small heads + yellow dots explodes outward from cards ~12.5s and settles into ring around them ~13.0s | top | counts climb, heads burst | views |
| 14.5–22.5s | "SHIFTING BELIEFS" lines panel: orange-bordered glass panel top-center x100–900, y40–200 with colored horizontal lines; title "SHIFTING BELIEFS" top-left ~16.0s (white "SHIFTING" + orange "BELIEFS"); small head with "Audience Belief" label at panel's left edge ~17.0s; "Telling them they're wrong" label ~18.5s; "Change their Perspective" label ~20.5s; green check pill top-right ~21.5s | top-center | lines draw, labels pop, check | shifting beliefs |
| 22.0–25.5s | "TRUST BUILDING" panel morph: panel title morphs to "TRUST BUILDING" (white "TRUST" + orange "BUILDING") ~22.2s; three format cards fly back in around panel: "Tournament" top-left ~23.5s, "Rating" bottom-left ~24.0s, "This or that" right ~24.2s — each with small red circle badge [UNVERIFIED — red X or notification dot] | top | morph, cards fly in | trust building |
| 26.0–30s | Orange video cards fly-in: three orange rounded-rect cards with white play triangles fly in from sides and stack top-center x100–900, y40–220 (left ~26.0s, center ~26.5s, right ~27.0s); they bob slightly; "TRUST BUILDING" panel fades behind them ~28.5s | top-center | fly in, bob | — |
| 30.5–31.5s | "SHALLOW FORMATS / NUTRIENT DENSE" pills: two orange pills under orange cards [UNVERIFIED exact text] | under cards | pop | — |
| 32.0–34.0s | "REACTION VIDEOS" card: dashed-border video card flies in top-center x550–700, y40–250 labeled "Reaction videos" orange; Sky points up at it | top-center | fly in on point | reaction videos |
| 34.0–38.0s | "LEVERAGE" panel: orange-cursive "Leverage" title right of card ~34.5s; list builds below: "News" ~35.0s, "Creators" ~35.5s, "Celebrities" ~36.0s, "Existing Demand" ~36.5s — each row with small icon | right | rows build | leverage |
| 38.0–40.5s | Authority meter: reaction card moves to center-top surrounded by ring of orange/white dots; "Authority:" label below with orange progress bar that FILLS ~38.5–40.0s; yellow "!" badge at card's top-right ~38.2s | top-center | bar fills | authority |
| 40.5–42.5s | Card grid: grid of orange play-cards + small video thumbnails fans out across top x40–980, y40–300 (~8 cards in two rows) | top | fan out | formats grid |
| 43.0–46.0s | "STORYTELLING VIDEOS" card + watch-time timer: dashed video card top-left labeled "Storytelling videos" orange with "$50M" thumbnail; below it "Your Reel" progress bar with timer counting up: "0 seconds" → "2 seconds" → "12 seconds" → "14 seconds" → "24 seconds" → "38 seconds" ~44.5–46.0s; view count "14,000,000" above ~45.5s | top-left | card pops, timer counts | storytelling videos |
| 47.0–51.5s | "NARRATIVE ARC" panel: orange-bordered glass panel top-left x100–500, y40–280; rows build one at a time: "Intro" blue bar ~47.5s, "Rising action" orange bar ~48.0s, "Conflict" red bar ~48.5s, "Climax" yellow bar ~49.0s; cursive title "Narrative Arc" at top ~50.5s; small heads around panel's edges ~51.0s with green dots; "Priority" meter at bottom ~52.0s | top-left | rows build | narrative arc |
| 53.0–58.0s | "DESIGN PROCESS FORMAT" card: orange card top-center x550–700, y40–250 labeled "Design process format" with blue thumbnail (red circle/square diagram, finger pointing); thumbnail swaps to red box being opened ~55.0s; second card left: "PROBLEM / The lid swings into the corner" red ~56.0s; third card right: "TRADITIONALLY / Round lids clear the contents" blue ~57.0s | top-center | card pops, thumbnail swaps | design process |
| 58.0–60s | 4-problem grid + fix grid: four small cards fan out top with "PROBLEM 1-4" labels ~58.5s; second row of four cards with "FIX 1-4" labels in green ~59.5s | top | fan out | problems / fixes |
| 60.0–63.0s | "THE THOUGHT PROCESS" panel: orange-bordered glass panel top-center x300–700, y40–280, title "THE THOUGHT PROCESS" orange; rows check off one at a time: "The lid jams" ~60.5s, "Seam on top" ~61.0s, "Add width" ~61.5s, "Move the hinge" green check "it works" ~62.0s | top-center | rows check off | thought process |
| 63.5–66.0s | Three-format recap: three format cards return top-center in row ("Reaction Videos", "Storytelling Videos", "Design Process Format" with thumbnails); connector line draws below to small head icon ~66.0s | top-center | return, line draws | recap |
| 66.5–68.7s | Thought process return + arrow: "THE THOUGHT PROCESS" panel returns top-center with orange arrow curving into it from left ~67.0s; rows highlight green one at a time; ends on Sky "…and that's how trust is built" ~68.5s | top-center | arrow curves in | close |

### DfA9L-PHYWp — "Content-Offer Fit" (no content strategy) — 77.2s — ORANGE
Full notes: `notes_DfA9L-PHYWp.md`
Dark studio, warm monitors behind, Sky in dark jacket over black tee. Walks a 6-box framework
(GOAL → AVATAR → MARKET → OFFER → FUNNEL → BRAND), each box getting its own animated panel.

| Time | Device | Where | Motion | Speech tie |
|---|---|---|---|---|
| 0.0–2.8s | Glowing head in hands: small head cutout (Sky's face) with yellow glow floats between Sky's cupped hands at chest x450–550, y480–620 — held like a glowing orb; two small yellow dots orbit it; head bobs gently | chest | float, bob, orbit | — |
| 0.8–4.5s | Creator profile cards: three small profile cards fly in top-right x700–980, y40–200 ("Jordan the Stallion" ~0.8s, "Keith Lee" ~1.0s, "Khaby Lame" ~1.2s — thumbnail + name + view counts 2.1M / 2.3M / 8.8M); ~2.0s thumbnails go BLACK AND WHITE one at a time left to right — creators' videos desaturate as he says they have "no content strategy"; counts keep climbing under gray thumbnails | top-right | fly in, desaturate | no content strategy |
| 4.5–5.8s | B&W + italic text: whole frame BLACK AND WHITE; orange italic text center types in ~4.8–5.5s ("let's just get more views"); color returns ~5.8s | center | B&W cut, type-in | "let's just get more views" |
| 6.0–9.0s | Format cards trio: three dashed-border video cards drop in top x400–980, y40–250 with orange labels ("Demonstration Content" ~6.0s, "Yapping Content" ~6.5s, "Client transformation Content" ~7.0s) | top | drop in | formats |
| 9.2–10.5s | "CONTENT-OFFER FIT" 6-box grid: glass panel top-center x400–980, y40–280 titled "Content-Offer Fit" with 6 numbered boxes in 2 columns ("1. Goal", "2. Creator", "3. Avatar", "4. Market", "5. Offer", "6. Funnel" — boxes appear one at a time ~9.2–10.2s) | top-center | boxes pop | content-offer fit |
| 10.8–14.5s | Two-curve chart: glass panel top-center x400–900, y40–260; title "Going viral is fast. Positioning takes time."; BLUE bell curve draws ~11.0–11.8s; ORANGE S-curve draws slowly ~12.2–14.0s, crossing blue curve; small label at orange curve's end ~14.2s | top-center | curves draw, cross | viral fast, positioning slow |
| 14.8–18.0s | Avatar/client/offer labels: top-right, three labeled rows with heads ("Avatar — Who are we talking to?" Sky's head ~14.8s, "Client — Who are we working with?" ~15.5s, "Offer — What are we selling?" ~16.0s; each row: small head + orange triangle marker) | top-right | rows pop | avatar / client / offer |
| 18.0–19.5s | Label swap: "Avatar" row's label swaps to "Outlier research — What's already working?" green ~18.2s; then "Formats — What styles to copy?" purple ~18.8s; rows cycle labels | top-right | label swap | outlier research / formats |
| 20.5–22.5s | "BRAND DIRECTION" tree: glass panel top-center x550–950, y40–280; head Sky at left with branching lines to 4 options ("Educator", "Problem Solver", "Community Builder", "Lifestyle Creator", "Authority Figure" — rows appear one at a time ~21.0–22.0s; "Problem Solver" highlights orange ~22.0s; orange card pops right of it ~22.2s) | top-center | branches draw, highlight | brand direction |
| 22.5–25.5s | "ANSWER THESE BEFORE YOU POST" panel: panel top-center x100–700, y40–280 titled "Answer these before you post." with rows ("Avatar" ~23.0s, "Offer" ~23.5s, "Uniqueness" ~24.0s); head labeled "Caleb" at panel's left edge ~23.0s with orange arrow pointing at rows | top-center | rows appear, arrow | answer these |
| 25.8–28.0s | Goal/avatar/market/offer/funnel list + brand bar: numbered list top-center ("01 GOAL / 02 AVATAR / 03 MARKET / 04 OFFER / 05 FUNNEL" ~26.0–27.0s); below, orange bar "BRAND" with three pills ("Positioning / Messaging / Associations" ~27.0s); row "01" highlights orange ~28.0s | top-center | list appears, row highlights | the six boxes |
| 28.0–30s | Goal checklist: panel zooms to "01 GOAL — What are we trying to do?" with checkboxes ("Get more leads" checked ~28.5s, "Hire people" checked ~29.0s, "Inspire people" checked ~29.5s); head with orange triangle at panel's left edge | top-center | checkboxes tick | goal |
| 32.5–38.0s | "02 PERSON" panel: glass panel top-center x100–900, y40–300 titled "02 PERSON" with person icon center; four sub-cards appear one at a time ("Your story" ~33.5s, "Your knowledge" ~34.0s, "Your philosophies" ~34.5s, "What makes you different" ~35.5s); head with orange triangle at panel's left edge throughout | top-center | sub-cards pop | person |
| 37.5–44.5s | "03 AVATAR" panel + "EXACTLY" B&W: panel morphs to "03 AVATAR" ~38.0s with person icon; ~38.8s frame goes B&W and big orange italic "Exactly" appears top-right x700–950, y60–140 — holds through ~42.0s, word pulses slightly larger ~40.5s; color returns ~42.2s; AVATAR panel fills with rows ("Daily life" ~42.8s, "Fears" ~43.0s, "Desire" ~43.2s, "Beliefs" ~43.5s, "Behavior" ~43.8s, "Struggles" ~44.0s); person icon fills orange ~43.5s; "Clear to the molecular level." at bottom ~44.2s | top / top-right | B&W cut, "Exactly" pulse, rows fill | avatar |
| 44.5–46.5s | "04 MARKET" panel: panel morphs to "04 MARKET — What is everyone else saying in your niche?"; three creator cards appear ("Creator A" ~45.0s, "Creator B" ~45.5s, "Creator C" ~46.0s, each with video thumbnail below) | top-center | morph, cards pop | market |
| 46.5–52.5s | "05 OFFER" panel: panel morphs to "05 OFFER — THE OFFER / What are we actually selling?"; three offer cards appear ("Software" ~47.2s, "Coaching" ~47.8s, "Services" ~48.2s, each with thumbnail); "Software" thumbnail swaps to "$10,000" screenshot ~49.0s; "Services" swaps to car photo ~50.5s | top-center | morph, cards pop, thumbnails swap | offer |
| 52.5–58.0s | "06 FUNNEL" panel: panel morphs to "06 FUNNEL"; "CONTENT" row ~52.8s with small person icons filling in ~53.2s; "CHECKOUT PAGE" row ~53.8s; "VSL" row ~54.2s; "FEEDS INTO BRAND" orange bar at bottom ~56.5s | top-center | morph, rows fill | funnel |
| 58.0–60s | 6-box recap: numbered list returns top-right ("01 GOAL / 02 AVATAR / 03 MARKET / 04 OFFER / 05 FUNNEL") with green checks appearing beside each row one at a time ~58.5–59.5s; orange BRAND bar below; yellow "realskytan" profile card slides in bottom-center ~59.5s | top-right / bottom | checks tick, card slides | recap |
| 60.0–65.0s | Profile card + association chips: "realskytan" profile card stays bottom-center; branch diagram draws below it: four pills appear one at a time ("Hook-obsessed" ~62.5s, "Test-driven" ~63.0s, "Battle-tested" ~63.5s, "Relatable" ~64.0s — brand associations) | bottom-center | pills pop | brand associations |
| 64.5–68.5s | Video wall: wall of ~12 video thumbnails fades in across top x40–980, y40–300 in two rows; labels under groups: "CONTENT STRATEGIST" left ~66.5s, "RANDOM TOPIC" right ~67.0s, "TRENDS" left ~67.5s; left group = Sky's own videos; right group = random topics (Khaby Lame etc.); "CONTENT STRATEGIST" highlights ~68.0s | top | wall fades in, labels pop | content strategist vs random |
| 69.0–73.5s | Script page + magnifier: "Script" document page slides in top-center x100–500, y40–350 with sections "Hook / Body / CTA" and lines of text; orange magnifier icon at page's right edge ~70.0s SCANS down page slowly ~70.0–73.0s, highlighting lines as it passes | top-center | slide-in, magnifier scans | script |
| 74.5–77.2s | Sponsor/client cards: two video cards drop in top — left "SPONSORS PAYS YOU" (man outdoors) ~74.8s, right "CLIENT PAYS YOU" (Sky talking) ~75.5s; ends on both cards + Sky "…positioning pays you" | top | drop in | sponsors vs clients |

### De-A2dvCeV3 — "These formats are officially dead" (fast content = fast food) — 63.2s — ORANGE
Full notes: `notes_De-A2dvCeV3.md`
Dark studio, monitors + night city windows, Sky in black tee, gray pants. Sequel to DfDu's
shallow-formats thesis. Card-wall heavy: top of frame almost always a floating cluster of format cards.

| Time | Device | Where | Motion | Speech tie |
|---|---|---|---|---|
| 0.0–1.5s | Format cards wall: five small video cards fly in top x100–980, y40–200 one at a time (man in suit ~0.2s, orange tournament bracket ~0.5s, woman with book ~0.8s, tier-list card ~1.0s, man ~1.2s); Sky points up at them | top | fly in one at a time | the formats |
| 1.8–4.0s | Card spotlight sequence: each card scales up in turn with orange label above it as Sky names it ("S-tier Ranking" ~2.0s, "Rating" ~2.8s, "Tournament" ~3.2s, "This or that" ~3.8s) | top | scale-up spotlight | naming formats |
| 4.5–5.5s | "FAST CONTENT" cursive: four cards regroup into row top-center; orange cursive "Fast content" appears below them ~5.0s | top-center | regroup, cursive pops | "fast content" |
| 6.5–9.0s | "LINES" panel: glass panel top-center x100–900, y40–250 with colored horizontal lines (orange/yellow/blue/green) + small orange circle icon; cards orbit around it; lines pulse | top-center | lines draw, pulse | lines |
| 9.8–13.5s | Audience/customer split: single video card (man in suit) center-top x550–700, y40–250 with two labels ("Audience" left, orange cursive ~10.0s and "Customer" right ~10.2s); cluster of small heads at left of card ~10.5s, growing; ~12.5s heads turn RED one by one (warning) | top-center | heads grow, turn red | audience vs customer |
| 14.5–17.0s | Card cluster + view counts: cluster of 5–6 cards re-forms top-center with view counts ("1.2M / 41.7K / 18.3K / 12.4M" ~15.5–16.5s) | top-center | re-form, counts pop | views |
| 17.0–18.5s | "HIGH ENGAGEMENT" line chart: purple line chart draws across top x400–980, y200–300 with "HIGH ENGAGEMENT" label; data points pop ("12.3K / 34.5K / 559" ~17.8s) | top | line draws, points pop | high engagement |
| 18.0–20.5s | Reaction dots + slider: colored dots (pink, teal, green, red) pop onto cards ~18.2s; orange horizontal slider with knob below x100–900, y420–480 with "-0.50" label; knob slides left ~19.0s, label changes to "-0.27" ~19.5s | mid-frame | dots pop, knob slides | slider |
| 21.0–25.5s | "LINES" panel returns (0:40 timer): colored-lines panel returns top-center with red "0:40" timer pill top-right ~21.5s; lines fill/pulse; ~24.5s panel tilts slightly (3D tilt) and purple line highlights | top-center | return, tilt | lines |
| 26.5–29.0s | "TRUST" panel: panel morphs to green-bordered version with green check + "TRUST" label and "Built by the repeated process" subtext ~27.0s; small cards orbit around it x100–980, y40–300 | top-center | morph, orbit | trust |
| 30.0–31.5s | Orange play-cards trio: three orange rounded cards with white play triangles fly in top-center x100–500, y40–180 | top-center | fly in | — |
| 31.5–33.0s | "POV DEMOS" card: video card (hands + plate) flies in top-right labeled "POV Demos" orange ~32.0s; Sky points at it | top-right | fly in on point | POV demos |
| 33.0–34.5s | "MULTI-SHOT EDUCATION" card: video card (woman holding lens) flies in top-center labeled "Multi-shot Education" ~33.5s | top-center | fly in | multi-shot education |
| 34.5–35.5s | "TRANSFORMATIONS" card: video card (smiling man) flies in top-left labeled "Transformations" ~35.0s | top-left | fly in | transformations |
| 36.5–39.5s | "SHIFTING BELIEFS" lines panel: colored-lines panel returns top-center with green "SHIFTING BELIEFS" label at left + small head; lines fill/pulse; green check pill top-right ~38.0s | top-center | return, fill, check | shifting beliefs |
| 40.0–43.5s | 2025→2027 timeline: horizontal orange timeline draws across top x100–900, y40–120 with nodes ("2025" ~40.5s, "Fast-paced content 2026" ~41.0s, "Nutrient-dense formats 2027" ~41.5s); small cards cluster under each node | top | line draws, nodes pop | 2025 → 2027 |
| 44.5–55.5s | Niche pills: four format cards return in row top x100–980, y40–220; below them niche pills appear one at a time ("Niche 1" ~44.8s, "Niche 2" ~45.2s, "Niche 3" ~45.5s); then topic pills ("Marketing" orange ~48.5s, "General business" red ~49.0s, "Real estate" ~51.5s, "Finance" ~52.0s, "AI" yellow ~52.5s); pills glow/turn red one at a time ~50.0–52.0s (saturated niches); then green/blue pills ("Dog training" ~54.5s, "Crafts" ~55.0s, "Sciences" ~55.5s — unsaturated niches) | top | pills pop, color change | niches |
| 56.0–57.0s | "POST" pill: blue "Post" pill top-center with green check; card cluster shrinks | top-center | pop | post |
| 57.5–63.2s | Funnel: 3-tier funnel draws top-center (blue top tier "Viral Reel" 4 thumbnails + "100,000 impressions / Brings new people to your profile" ~58.0s, purple middle tier ~58.5s, green bottom tier ~59.0s); middle tier label "Valuable Back-End Content" ~59.5s; bottom tier label "Nutrient-dense format" ~60.0s; bottom tier gains "Trust → Potential Clients" ~60.5s; three green "$" icons pop below funnel ~61.0–62.0s; ends on funnel + $$$ ("catch all the impressions that are coming in the door") | top-center | tiers draw, labels pop, $ pops | funnel close |

### Dez4fPJCR74 — "The absolute worst content strategy for short-form content is teaching" — 58.9s — ORANGE
Full notes: `notes_Dez4fPJCR74.md`

| Time | Device | Where | Motion | Speech tie |
|---|---|---|---|---|
| 0.0–1.2s | Thumbnail cloud grid: six small video cards fan in across top x100–980, y40–250, each with orange label below ("Behind the scenes" ~0.2s, "Live Demos" ~0.5s, "Insights" ~0.8s, "Storytelling" ~1.0s, "Teaching" ~1.0s, "Case studies" ~1.2s) | top | fan in one at a time | formats |
| 0.8–3.0s | Cursive title build: orange cursive "worst" ~0.8s, then "Content Strategy" large orange script x300–700, y480–620 types/slides in word by word, persisting | center | word-by-word | "worst content strategy" |
| 3.0–4.0s | Cloud fly-off + survivor card: five cards fly off up/out; "Teaching" card survives, dropping to top-center x400–600, y0–180 | top-center | fly off, survivor drops | "is teaching" |
| 4.0–6.0s | Head + 60-second timer: small head cutout (woman, "Teaching" creator) pops in at left x100–200, y200–300 with orange play triangle; "60 sec" timer pill beside it counts UP ("7 sec" ~4.0s, "19 sec" ~4.2s, "30 sec" ~4.5s, "42 sec" ~4.8s, "60 sec" ~5.0s) | left | pop, timer counts | "60 seconds isn't enough time to teach anybody anything" |
| 7.5–10.0s | Brain/glow head effect: Sky's own head goes WHITE/SILVER — glowing brain-like texture washes over his hair and head ~7.5–8.5s, fading ~9.5s [UNVERIFIED mechanism] | his head | wash over, fade | "how deep your knowledge actually is" |
| 10.2–12.0s | "Top 10 tips" card: small video card drops in top-right x700–950, y40–200 with orange label "Top 10 tips" above it and same head + play triangle at its left edge | top-right | drop in | "not going to come from a top 10 tips video" |
| 12.5–14.8s | "One clear / Non-obvious insight" panel: two cards build at top-center — left card "Insight: being reasonable is what stops most people from building something big" ~12.5s, right card "One clear / Non-obvious insight" ~13.0s, both with small green dot markers | top-center | cards build | "one clear, non-obvious insight" |
| 15.0–16.2s | Pill constellation: six orange pills fan out across chest x100–900, y480–620, one at a time ("Short-form Virality" ~15.2s, "Personal Branding" ~15.5s, "Content Systems" ~15.8s, "Full-funnel Content Ops" ~16.0s, "Content Formats" ~16.0s, "Hooks & Packaging" ~16.2s) | chest | fan out | "package a decade worth of expertise" |
| 16.5–19.0s | Vertical video card + 60-sec progress arc: vertical video card with white play triangle drops in top-center x400–600, y0–180; below it orange progress bar draws left-to-right with timer labels "21 sec" → "37 sec" → "43 sec" → "54 sec" → "60 sec", dashed white arc sweeps down right side ~16.8–19.0s | top-center | drop-in, bar draws, arc sweeps | "into a 60 second short" |
| 19.5–25.0s | A-to-Z checklist panel (scrolling, row-highlight): glowing orange glass panel slides in bottom-center x100–700, y480–800 with rows ("Sell & Onboard Clients", "Content Strategy", "Research", "Scripting", "Filming & Coaching", "Editing", "Posting & Distribution", "Tracking & Adapting", "Converting to Sales", "Building the Team"); rows highlight orange one at a time as he names them; panel SCROLLS as highlight moves down (~19.8s → ~24.0s), then scrolls back up to Research/Scripting/Filming & Coaching/Editing ~24.5–25.0s; small head cutout rides panel's top-left corner throughout | bottom-center | slide-in, scroll, row highlight | "mapping every single thing you do within a business A to Z… pick one of those tasks" |
| 25.5–28.0s | Outlier axes chart: orange L-shaped axes chart draws top-center x100–900, y40–250 (axes lines, small white pill labels along curve, orange "Outlier" pill top-right ~26.5s) | top-center | axes draw, pills pop | "an outlier topic that's performing well in your niche" |
| 28.5–31.5s | Competitor research wall: full-frame wall of competitor video columns (two creator thumbnails with transcript text blocks beneath, bullet lists), green "SLIDE DECK" card center-bottom with bullets ("Use AI to generate slide decks for Reels", "Upload brand references and add your script", "Generate multiple visual styles before choosing the final design") | full frame | wall builds | "we transcribe all of your competitors' videos and understand what they're teaching" |
| 31.5–33.0s | "What do we do" pill + format trio: wall flies off; small head + orange triangle + pill "what do we do that's non-obvious / different" at chest ~31.8s; three video cards drop in top x100–980, y40–220 with orange labels ("Demonstration" ~32.5s, "Proof" ~32.8s, "Done for you" ~33.0s) | chest / top | fly off, pill pops, cards drop | "what do we do that's non-obvious or different?" |
| 34.5–38.5s | Crowned head + audience crowd: Sky's head cutout with gold CROWN and "Competitive Advantage" label at chest x450–550, y560–660; ~6 small female head cutouts fan out below it ~35.0s, multiplying to ~15 heads by ~38.0s (saturated-market crowd) | chest | heads multiply | "our competitive advantage… the key to winning in a saturated market" |
| 39.0–40.5s | Package pill list: cards + crowd fly off; small head + orange triangle at left chest ~39.5s; four pills stack at center x400–700, y480–700 ("One topic" ~39.5s, "What competitors are teaching" ~40.0s, "Your non-obvious angle" ~40.2s, "Competitive advantage" ~40.5s) | center | pills stack | "we want to package all of this into a video" |
| 40.5–42.2s | Video card + #1 / #2 options: vertical video card with white play triangle drops in center-chest x400–600, y480–700; orange pills "#1" left and "#2" right flank it ~41.2s | center-chest | drop-in, pills flank | "We have two options" |
| 42.2–47.0s | "#1 Scripted Video" + script-structure lines panel: label "#1 Scripted Video" under card ~42.2s; colored-lines panel draws top-left x30–350, y40–260 ("Hook:" red bar, "Lead:" yellow bar, "Body 1:" blue bar, "Open loop 1:" with circular arrow, "Body 2:", "Open loop 2:", "Body 3:", "CTA:" green bar — bars draw one at a time ~42.8–43.5s); Sky POINTS UP at panel with right index finger ~43.0–44.5s | top-left / chest | bars draw, point-up | "A scripted video following this structure highlighting one specific insight" |
| 47.0–47.8s | "#2 Demonstration Video" swap: panel + #1 card fly off; label "#2 Demonstration Video" + video card (screen recording of a laptop) drop in top-center x400–650, y40–280 | top-center | swap | "or a video demonstrating the action" |
| 50.5–52.0s | Point up at #2 card: Sky points up at demonstration card with right index finger as it plays | — | point | "sharing our thought process" |
| 52.5–55.0s | Three proof cards: top-center trio settles ("Top 5 hook tips" card center with play triangle, "My scripting process" card right — laptop typing, "Wrote a creators hooks live" card sliding in from left ~54.8s) | top-center | cards settle, one slides in | "when I did this for myself" |
| 57.2–58.9s | Payment count-up pills: two payment pills pop in at chest ("High-ticket client #1" counting $0.00 → ~$18,000.00; "High-ticket client #2" counting $0.00 → ~$17,955.00 [UNVERIFIED exact intermediate values]); ends on three cards + two payment pills + Sky mid-sentence; no end card [UNVERIFIED final 0.2s] | chest | pop, count-up | "landing me two high-ticket retainer clients" |

### DexJ-qWiWdY — "The ultimate storytelling caption for Instagram" — 56.0s — ORANGE
Full notes: `notes_DexJ-qWiWdY.md`
Video counterpart of the Retro-OS "Storytelling Caption" carousel (De2kC4nEptM).

| Time | Device | Where | Motion | Speech tie |
|---|---|---|---|---|
| 0.0–2.8s | "Ultimate Caption Structure" panel builds: glass panel top-center x400–650, y0–280, title "Ultimate Caption Structure"; colored lines draw in one at a time ("Introduction" red ~0.5s, "Struggle" yellow ~0.8s, "Rise" blue ~1.0s, "Proof" teal ~1.2s, "Unique Mechanism" pink ~1.5s, "Expectations" white ~1.8s, "Two-Door CTA" green ~2.2s); dashed white arc sweeps down panel's right side ~0.8–1.2s; glowing Instagram logo pops at panel's top-right ~2.8s; Sky POINTS UP at panel ~0.0–0.5s | top-center | lines draw, arc sweeps, logo pops, point-up | "This is the ultimate storytelling caption for Instagram" |
| 0.8–1.5s | Cursive title build: orange cursive "Ultimate" ~0.8s, white "Storytelling caption" ~1.2–1.5s, center-lower x300–700, y480–620, word by word | center | word-by-word | "ultimate storytelling caption" |
| 5.5–7.2s | Thumbnail row rises from bottom: row of small creator video thumbnails rises up from bottom edge x100–980, y700–900, one glowing GOLD ~6.2s | bottom | rise up | "a good reel should have at least 50% non-followers" |
| 7.5–12.0s | Followers / Non-followers split + orbiting dot ring: two pills at top ("Followers / Already know you" top-left ~7.5s, "Non-followers / Never heard of you" top-right ~8.2s); center-chest small vertical video card with RING of glowing dots (orange + white) orbiting around it ~7.8–12.0s; comment bubbles pop above card ("who is this guy?" ~9.5s, reply card "Where can I learn more about you?" ~10.0s) | top / chest | pills pop, dots orbit, bubbles pop | "50% non-followers who have never heard of you and need an intro ASAP" |
| 12.5–14.8s | Two-option head: dots fly off ~12.5s; head cutout with orange triangle at chest ~12.8s with two option labels ("Pitching your Services" left white, "Lead magnet" right orange) | chest | fly off, head + labels pop | "Instead of deciding between a lead magnet or pitching your services" |
| 15.0–17.5s | Structure panel returns + option checks: panel returns top-center ~15.0s (empty frame first, colored lines redraw one at a time ~15.5–17.5s); both option labels gain green checks ~16.8s | top-center | return, redraw, checks tick | "this caption allows you to do both" |
| 17.5–22.0s | 1000-comments dot grid: grid of orange dots (~10×10) fills in at chest x400–700, y480–700 ~17.5–18.0s, cursive label "1000 comments" at left ~18.5s; left columns turn GREEN ~19.2s (100 people — "Who want to work with us" label ~19.5s); comment bubbles rain down from top ~19.5–21.5s (wall of comment rows filling top x100–980, y0–250); right portion turns YELLOW-GREEN ~21.0s (700 people — "Who got nurtured with a free resource" label ~21.2s) | chest / top | grid fills, color segments, comment rain | "out of the 1,000 people who commented, 100 people asked to work with us and 700 got nurtured with a free resource" |
| 23.2s | Grid collapse: dots fly off as he says "Here's what the structure looks like" — clean beat before walkthrough | chest | fly off | "Here's what the structure looks like" |
| 24.5–27.5s | Caption document builds — Introduction: caption-document panel slides in top-left x100–500, y40–260 (red "Introduction" title + caption text lines TYPING in: "Hey what's up, I'm Sky and 3 years ago I got OBSESSED with 1 question: What makes some reels get 200 views and some reels 2,000,000 views?"); dashed vertical connector line down document's left edge | top-left | slide-in, type-in | "The introduction tells the stranger who you are and gives them a reason to keep reading" |
| 25.5–27.5s | Head constellation (audience voices): ~6 small head cutouts at chest x300–750, y560–680 with orange labels ("I'm Sky, a content strategist who's helped 100+ creators and driven 1 billion views", "8,000 reels? Tell me more.") | chest | pop | audience voices |
| 27.5–30.0s | Document builds — Struggle: yellow "Struggle" title + bullet lines type in below Introduction ("And I tried everything under the sun — Posting at peak times, Stealing viral hooks, Posting viral reels, Spamming hashtags, and maybe a dance here and there, Literally everything…") | top-left | type-in | "The struggle shows them that you've been exactly where they are now, so they feel understood" |
| 31.2–33.0s | Document builds — Rise + heads turn RED: blue "Rise" title + text types in below Struggle; chest heads turn RED and glow ~31.5s with labels "None of it worked?!" | top-left / chest | type-in, heads turn red | "The rise breaks through beliefs, so now there's a gap to instill your beliefs" |
| 35.0–38.0s | Document builds — Proof + heads turn GREEN: teal "Proof" title + bullets type in ("Over 8,000 videos for your favourite experts (DAMN that's a lot)", "1 billion views", "1m followers", "and 7 figures in revenue" [UNVERIFIED exact lines]); chest heads turn GREEN with glow ~35.5–36.5s, labels "8,000+ videos", "1 billion views", "That's proof." | top-left / chest | type-in, heads turn green | "Then the proof earns you the right to give that answer, and because it comes after the story, it's evidence not bragging" |
| 39.5–42.0s | Document builds — Unique Mechanism: pink "Unique Mechanism" title + text types in ("The WINNING formula is… good Topics + viral Formats + disciplined Testing… So I changed everything in my business to optimize for this"); chest head labels update ("My formula: good Topics + viral Formats + disciplined Testing", "One formula. Finally clear.") | top-left / chest | type-in, labels update | "Then the unique mechanism shows how you're different from everybody else in one simple formula" |
| 43.5–46.0s | Document builds — Expectations: white "Expectations" title + long text types in (Done-For-You offer description); chest labels ("Follow me for the best content tactics", "I know what I got", "Easy yes.") | top-left / chest | type-in | "The expectations tell them exactly what they get by following, so it's an easy yes" |
| 47.2–48.0s | Document builds — Two-Door CTA: green "Two-Door CTA" title + text types in at document's bottom ("Comment 'CONTENT' on any of my reels to 1) get my best free sauce OR 2) if that's your thing, follow me" [UNVERIFIED exact wording]) | top-left | type-in | "And the two-door CTA allows them to self-filter" |
| 48.0–52.0s | Two-door cards at chest: two option cards appear at chest ("Free sauce, for me first." left, "Content" right) with label "Comment 'CONTENT' for my free sauce, or to work with us" | chest | pop | "They can choose the lead magnet if they're not ready to work with you, or if they're a hot lead, they can just book a call straight away" |
| 52.5–53.5s | Hot-lead door — Appointment Confirmed: "Appointment Confirmed" card pops at chest-left ~52.5s with label "I'm ready. Booked a call." at right — the hot-lead door visualized | chest | pop | "or if they're a hot lead, they can just book a call straight away" |
| 53.8–56.0s | Document scroll + close: whole caption document SCROLLS upward (sections sliding past) as he closes: "And that is the perfect storytelling caption for Instagram" ~54.0–55.5s; ends on full document + two-door cards + Sky; no end card [UNVERIFIED final 0.2s] | top-left | scroll up | close |

---

## BUILD ORDER (simplest first → hardest)

**Tier 1 — do first (static/pop, no tracking, no custom art):**
1. Word-by-word captions (#1) — the base layer of every reel.
2. Big title builds (#2) — text stagger, one accent color.
3. Photo pop-ups (#10) — hard cut in/out, fixed position.
4. Pill labels / annotation pills (#34) — pop in, stack, reset.
5. Count-up counters (#12) — numerals + fast stepping.
6. Checklist / filter panels (#7) — rows appear, fill green, X/check stamps.

**Tier 2 — next (motion + layout, still template-able):**
7. Floating mini video card (#3) — drop-in with bounce, dashed border, view label.
8. Phone mockups (#6) — slide/drop-in, real IG UI inside, labels around it.
9. Little heads (#8) — cutout + orbit/bob; markers (triangle, crown, glow ring, "?" badge).
10. Thumbnail clouds / walls (#14) — fan-in, one gold highlight.
11. Charts that draw (#11) — line draw with leading glow dot, area fill, labels at peaks.
12. Funnels (#9) — items fly in, one drops out.
13. Venn diagrams (#17) — circles draw, slide together, overlap fills.
14. Timers (#32) — jumping count, pill styling.

**Tier 3 — harder (state, sequencing, screen content):**
15. Retention-graph HUD (#4) — persistent panel + updating pill labels + playhead shading.
16. IG profile card building in stages (#5) — multi-stage build; collab UI walkthrough is the
    hardest single device in the set (menu → dropdown → dual-avatar morph).
17. Script-lines / colored-lines panels (#19) — the reel's spine; lines draw per section, active
    line pulses; panel returns and redraws.
18. B-roll cutaways (#15) — needs real B-roll matched to the analogy, hard-cut timing.
19. B&W + color isolation (#16) — grade work + timing the desaturation cut.
20. Point-follow (#22) — the element must land on the exact frame the gesture arrives; needs
    gesture-timed keyframes, not just voice-timed ones.
21. Split-screen screen recording (#18, DfLa only) — two video streams + highlight-synced list +
    word-swap orange highlight; the longest single device in the set (~76s continuous).

**Tier 4 — hardest (custom / system-level):**
22. Caption-document build (#25, DexJ only) — a full typed document that grows, scrolls, and
    drives the chest heads' color state (white → red → green) in sync with its sections.
23. Dot-grid data viz (#24, DexJ only) — grid fill + color segmentation + comment rain, all
    timed to the numbers in the sentence.
24. Head crowd / audience multiplication (#30) — many cutouts, color-state changes across the crowd.
25. Brain/glow head effect (#33, Dez4 only) — [UNVERIFIED mechanism]; needs a tracked head overlay
    or head-region grade — do not build until the mechanism is confirmed from a screen recording.
26. **Follow-state pop-up (Follow → Following) — NOT IN THE SOURCE SET.** No reel in the 14 shows
    it. It cannot be reverse-engineered from these frames; build it from Q's description
    (point-down "follow me" beat → profile pop-up with Follow→Following state change) as a new
    device in Sky's grammar (glass card, accent fill on the button flip, ~0.3s flip, hard cut in/out).

## What is NOT in Sky's grammar (checked across all 14)
- **No Follow → Following animation anywhere** (see above — the one device Q named that Sky
  never shows in these 14).
- **No end cards / outro screens** — every reel ends on Sky or a diagram.
- **No classic meme/GIF sticker pops** (Carter-style small reaction stickers). The closest is
  DfLa's movie-still flashcards and PIP reaction clips. Meme pops in Q's edits come from other
  creators' grammar, not Sky's.
- **No door device, no red decoration** (red is only a semantic "bad" marker).
- **No slow fades on devices** — hard cuts and fast slides only.
- **No captions over his face, ever.**

## Files in this folder
- `SKY_MOTION_TEARDOWN.md` — this file.
- `notes_<ID>.md` (14 files) — per-reel full notes.
- `transcript_<ID>.json` (14 files) — faster-whisper word-level transcripts.
- `frames/<ID>/` — ~4 fps frames per reel (3,766 total).
- `sheets/<ID>/` — contact sheets, 30 frames per sheet (7.5s per sheet).
- `extract.sh`, `sheets.py`, `transcribe.py` — pipeline scripts.

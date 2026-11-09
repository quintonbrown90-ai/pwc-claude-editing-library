# AGENTS — the mastermind architecture (specialists + one master)

**How the system is organized inside Claude.** One MASTER orchestrator
places it all together; **nineteen SPECIALISTS** each master one aspect,
trained on the harvested library for that aspect (its category parts):
eleven EDITING specialists (1–11), seven STRATEGY specialists (12–16,
18–19, added Nov 8 — the mastermind grows past editing), and one
SCRIPTWRITING specialist (#17, added Nov 8). The master classifies
the video, calls the right specialists in the right order, assembles
their outputs, runs the brand-DNA + human-made checks, and ships the
final edit. The master's job now covers BOTH the edit AND the strategic
angle: for any video or post, it picks the edit and the hook psychology,
the CTA, the pain point addressed, and the conversion path.

In Claude WEB CHAT the specialists run as ordered steps in one conversation
(not background processes) — the master issues each specialist's step, reads
its output, and hands it to the next. In Claude Code they may run as
subagents; the handoff format is identical either way.

## The master (orchestrator)

**Job:** classify → route → assemble → check → ship.
**Inputs:** the video + script + claim + proof + lane + keyword (the
11-question intake — `parts/prompts/prompts-router-intake.md`).
**Flow:**
1. Classify the video (EDIT-ROUTER.md) and issue the RECOMMENDATION:
   style pick + three grounds + build plan + QC gates + brand-DNA
   checklist + HUMAN-MADE CHECK. For any video or post, the master also
   issues the STRATEGIC angle first (strategy specialists 12–16, 18–19 run BEFORE the
   edit specialists when the job is a post, not just a cut): topic from
   the pain-point list, hook psychology, CTA + keyword, conversion path.
   Do not render until the pick is approved.
2. Call specialists in order (below). Each specialist returns its output
   in the handoff format; the master assembles them into one plan.
3. Run the brand-DNA checklist (F1–F6) + the "DOES THIS STILL READ AS Q?"
   self-check + the HUMAN-MADE CHECK on the plan. Any fail blocks the
   render until fixed.
4. Render (or hand the plan to the render step), QC on the exported file
   (EDIT-ROUTER.md §8), deliver the exact file + the delivery report.
**Owns:** `design-system/EDIT-ROUTER.md`, `design-system/BRAND-DNA.md`,
`design-system/SKY-SCORE.md` (the benchmark), `CATEGORIES.md` (the map).

## The specialists

Handoff format (every specialist, every time):
```
FROM: <specialist>
INPUTS RECEIVED: <what the master gave it>
OUTPUT: <its deliverable, with file/section references>
OPEN QUESTIONS: <anything it could not decide — the master resolves these>
NEXT: <which specialist runs next, and what it needs from this output>
```

### 1. Hook Agent
- **Job:** the first 2 seconds. Hook line + hook visual + open loop.
- **Owns:** `parts/hooks/` (Adilet patterns, Ava 7 types) + Adilet HOOKS.md.
- **In → out:** claim + proof → hook line (verbatim formula, TRUE claim) +
  hook visual (proof on screen at 0:00) + the second open loop before the
  midpoint. Hands the hook beat to the Motion + Imagery agents.

### 2. Caption Agent
- **Job:** every word on screen, timed to the word, in the lane's voice.
- **Owns:** `parts/captions/` + `skills/pwc-designed-captions/` (6 styles,
  pipeline, easings) + Adilet CAPTIONS.md (word-exact, +0.013s measured).
- **In → out:** finished voice track + script → caption plan (time, text,
  style, layer, box, motion_in) → rendered caption layers. Hands the plan
  to the Render/QC agent for the per-word fit audit.

### 3. Motion Agent
- **Job:** every moving element's named motion + frames + delay.
- **Owns:** `parts/motion/` + `parts/easing-physics/` + Viashaan MOTION.md
  (8 named motions) + `skills/pwc-motion-playbooks/`.
- **In → out:** beat plan → motion plan (per element: name + frames +
  delay). Rule: two elements entering with the same motion at the same
  frame is a tell — stagger or re-name one. Hands the motion plan to the
  Camera + Render agents.

### 4. Easing / Physics Agent
- **Job:** the curves and the physical settle (overshoot, spring, bounce).
- **Owns:** `parts/easing-physics/` + `skills/pwc-motion-playbooks/references/EASING.md`
  + `skills/pwc-designed-captions/code/easings.py` (verified: overshoot
  peaks 1.141; spring stiffness 170, damping 16).
- **In → out:** motion names → exact curve values (CSS + Python). Never
  hand-tunes a curve per video — picks the named one that fits the job.

### 5. Camera Agent
- **Job:** framing, pans, zooms, splits, layout switches.
- **Owns:** `parts/camera-moves/` + Adilet motion (whip/zoom-kick) + Herk
  split-first-frame + johannships per-line layout switching.
- **In → out:** beat plan → camera plan (framing per beat, whip pans cut on
  the fastest frame, zoom kicks on payoff words only, split-first-frame
  where the lane calls for it). Hands the camera plan to the Motion agent
  for timing.

### 6. Imagery Agent
- **Job:** the proof on screen — real screens, real examples, real numbers.
- **Owns:** `parts/imagery/` + Sky D9/D10 (exhibit + profile/grid inserts)
  + the show-it rule.
- **In → out:** claim list → proof object per claim (real screenshot /
  screen recording / photo / diagram from real numbers) + B-roll placed on
  its trigger word. If a proof object does not exist, the video is NOT
  ready — it sources it first, never ships the claim bare.

### 7. Color Agent
- **Job:** the PWC skin on every pixel.
- **Owns:** `parts/color-grade/` + `design-system/BRAND.md` (palette sampled
  from the logo) + Herk contrast-check.
- **In → out:** any borrowed system's colours → PWC palette (teal/gold/
  navy, NO RED — any reference's red maps to gold); contrast-checks every
  text element against its frame in a dark box. Runs the F1 palette check
  on the export.

### 8. Audio / Sound Agent
- **Job:** the voice chain + the dense, organic sound design.
- **Owns:** `parts/audio-sound/` + Adilet AUDIO.md (ElevenLabs → cuts →
  speed → loudness, −14.2 LUFS measured) + the local licensed library
  (~1,250 files).
- **In → out:** voice track → mastered voice (−14.2 LUFS, timings extracted
  AFTER the speed pass) + SFX map (every entrance AND exit, layered
  landings, accents on statement lines/numbers) + low cleared bed (~−28 dB
  under speech for built videos; uploaded reels stay original-audio-only).

### 9. Render / QC Agent
- **Job:** build the export and gate it — nothing ships on a builder's
  say-so.
- **Owns:** `parts/render-pipelines/` (caption pipeline, animation
  renderer, QC gates) + `design-system/WORKFLOW.md` + tests/QC_CHECKLIST.md.
- **In → out:** assembled plan → exported file → full QC report
  (freezedetect zero ≥0.35s; ±0.15s transition audits; last-voice→end-card
  ≤1s; lip-sync offsets; retention read; claim check; keyword-flow check).
  One fail = quarantine, fix, re-render, re-run.

### 10. Prompt Agent
- **Job:** the words Claude is given — prompts that produce the edit.
- **Owns:** `parts/prompts/` + `design-system/PROMPTS.md` (38 entries,
  §0–37 — v6 added charliehills full XML, kappa stack + CLAP, gannon.meyer
  per-line, kingketo one-liner, Stream-1 Tier S steals, Stream-2
  first-prompt architecture; v7 added tenfoldmarc 3-hook trial-reel prompt
  §24 + Content Dashboard prompt §25; v8 added §28–29 (deeper-expert pattern
  + scriptwriting run procedure); v9 added §30–37 (8 new prompt parts)) + `research/prompts/` (cross-platform batches,
  when they land).
- **In → out:** the build task → the paste-ready prompt(s) for it (router
  intake, Sky forms, Adilet one-liner, captions P1–P4, animation styles,
  Herk, outliers, clipper, 5-pass, retention-dip rescue, self-review).
  Prompts with no visible result are flagged [UNVERIFIED] and never
  presented as proven.

### 11. Style-Research Agent
- **Job:** the learning loop — find, vet, distill, and fold in new styles.
- **Owns:** `research/` (all streams) + CONTINUOUS-LEARNING.md + SAFETY.md
  + `design-system/SKY-SCORE.md` (updates the score cards).
- **In → out:** weekly sweep → vetted finds (quarantine + scan + license
  check) → distilled parts (≤50KB) → new rows in CATEGORIES.md +
  COVERAGE.md → next skill version. Never folds in unvetted, unlicensed,
  or unsafe material; parks with the reason and reports it.

## The strategy specialists (12–16, 18–19 — the mastermind past editing)

These run BEFORE the edit specialists when the job is a post, not just a
cut. They decide WHAT the video is for; the editing specialists decide
HOW it looks. Same handoff format, same master.

### 12. Content Strategy Specialist
- **Job:** what to post, when, in what order, for Q's lanes.
- **Owns:** `parts/strategy/` + `research/knowledge/TRENDS.md` + the
  WHAT'S WORKING NOW table (EDIT-ROUTER.md §7) + the posting cadence
  (launch slots 10:30 AM / 2:00 PM / 6:30 PM CT; plan queue 1/day at
  12 PM CT; avatar every other day).
- **In → out:** lane + week → the ordered post plan (one lane per slot,
  never two of the same back to back) + the week's top 3 topics (from
  the pain-point list) + the top 3 devices (from TRENDS.md). Order comes
  from Q in chat, never from file dates.

### 13. Audience Psychology / Following-Growth Specialist
- **Job:** how deep, loyal followings are built (identity, inside
  language, rituals, retention loops, plural proof, shared story,
  visible progression).
- **Owns:** `parts/audience-psychology/` +
  `research/knowledge/AUDIENCE-PSYCHOLOGY.md`.
- **In → out:** the video/post → the belonging check (does it name the
  avatar in line 1? does it use the tribe's words? does it end open,
  pointing at the next thing? is the proof plural and real?). Studies
  creators with cult-like followings weekly; new mechanics are flagged
  NEEDS-Q, never auto-adopted. The specialist also owns the psychology layer's belonging check and
  the weekly cult-following study (one creator per week: the creator,
  the mechanic, the retention evidence, whether it fits PWC).

### 14. Sales / Closer Specialist
- **Job:** DM closing, waitlist → join conversion, offer framing,
  objection handling, urgency without sleaze.
- **Owns:** `parts/sales-closing/` + `research/knowledge/SALES-CLOSING.md`
  (Q's actual offers only: Premium $97/mo monthly-only; Dec 7 cohort;
  founding window closes Dec 13, 11:59 PM CT; waitlisters get an extra
  month free + 3-Wins PDF; CALENDAR $35).
- **In → out:** the conversion step → the exact line (value first, one
  action, one sentence) + the objection answer from the table. Urgency
  is always a real deadline. A no is a no — never chase it twice in one
  thread.

### 15. Creator Coach / Pain-Points Specialist
- **Job:** what people in Q's space actually struggle with — the pain
  points creators need solved.
- **Owns:** `parts/creator-pain-points/` +
  `research/knowledge/CREATOR-PAIN-POINTS.md` (top 10 ranked by frequency
  + intensity, exact creator wording, public sources cited).
- **In → out:** weekly sweep of r/UGCcreators, r/VideoEditing, IG
  captions, complaint threads → re-ranked top 10 → top 3 to Content
  Strategy (topics) + top 3 to Sales (objections). Never invents a pain
  point — no public source + quote, no entry.

### 16. Trend / What-People-Like Analyst
- **Job:** what audiences in Q's niche actually like right now — top
  posts, formats, hooks, topics, with real engagement numbers only.
- **Owns:** `parts/trends/` + `research/knowledge/TRENDS.md`.
- **In → out:** weekly sweep of the creator catalogs → every post at
  >2× the creator's median engagement (likes and comments separately;
  comments > likes flags a funnel post) → re-ranked TRENDS.md → top 3
  to Content Strategy (topics) + Motion/Caption (devices). Never cites
  yt-dlp android-client view counts — they are unreliable.

### 17. Scriptwriting Specialist (v8 — NEW: the script lane is its own master)
- **Job:** the words before the edit — scripts, hooks, and ideas that pass
  the Quality Gate before Q ever sees them.
- **Owns:** `parts/scriptwriting/` (Category 20) + `parts/strategy/self-check-95-gate.md`
  + the Brand Brain files (who you are / what you sell + where it is going /
  how you talk).
- **In → out:** idea + ideal follower + inspiration → brain dump → structured
  script against the Playbook's 12 structures (INFERRED mapping) → Quality
  Gate score (95-gate threshold [NEEDS Q'S WORD]) → gated script handed to
  the Hook + Motion + Imagery specialists. A script that fails the gate
  never reaches Q. The interview front end (Grill Me mechanic) is Matt
  Pocock's skill — credit Pocock on any rebuild.

### 18. Psychology Layer Specialist (v9 layers — the standing layer)
- **Job:** the psychology behind content, editing, viewers, sales,
  niches, and community-building, learned from YouTube, social media,
  and every public source, applied to every edit and script.
- **Owns:** `parts/audience-psychology/` (5 psychology parts) +
  `parts/sales-closing/` (2 psychology parts) + `parts/strategy/`
  (psychology-niche-ugc) + the psychology layer in STRATEGY.md.
- **In → out:** the video/script → viewer state (skeptical / curious /
  frustrated / aspirational / ready to act / inside the room) → device
  pick (EDIT-ROUTER.md §1.E) + loop ledger (every loop named, every loop
  closed, payoff at 75–85%) + five-jobs header on every script +
  belonging check on every video. Theory-only entries are flagged, never
  executable; gated material is noted only, never chased. New mechanics
  are flagged NEEDS-Q, never auto-adopted.

### 19. Algorithm Mastery Specialist (v9 layers)
- **Job:** what Instagram (first), TikTok and YouTube Shorts reward
  right now, dated + sourced, myths flagged.
- **Owns:** `parts/strategy/algorithm-mastery-instagram.md` (top three
  Reels signals: watch time, likes per reach, sends per reach — Mosseri,
  Jan 2025; Reels Chaining system card, Nov 11, 2025; small-audience
  test; originality gate, Apr 30, 2026; Reels ≤3 min; "Your Algorithm"
  viewer controls; shares moment 2026; hashtags capped at 5) +
  `parts/strategy/top-creator-index-niche.md` (34 niche rows + 20 craft
  rows) + `parts/strategy/viral-structure-library.md` (S1–S15) +
  `parts/strategy/mastermind-thinking.md` (7-step reasoning) +
  `parts/creator-pain-points/pain-point-solution-bank.md` (P1–P20).
- **In → out:** the surface + the idea → the signals that surface
  rewards now + the eligibility gate (original content only, ≤3 min for
  Reels recommendation) + the structure that fits the proof available.
  Refreshed weekly; stale entries dropped. Never cites a weight, a
  multiple, or a threshold — Meta publishes none. Scan cadence is honest:
  weekly sweep (Sundays ~10:17 AM CT) + every batch Q sends + each
  coordinator run — no live 24/7 monitor.

## How a new style joins

A new style learned becomes a new part (or a new specialist's training
material). The mastermind grows by ADDING specialists and parts, never by
rewriting the whole system. If a new aspect needs its own master (e.g. a
whole carousel discipline, or a whole strategy discipline), it becomes the
next specialist (20th) with its own category parts — the master's flow does not
change, only its call list.

## The mastermind in one line

Strategy first (content → audience → sales → pain-points → trends → psychology → algorithm) →
classify (master) → hook → captions → motion → easing → camera → imagery
→ color → audio → render/QC, with the Prompt agent writing the words and
the Style-Research agent keeping the library growing — then brand-DNA +
human-made checks before anything ships.

## NO-LIMITS OPERATING STANCE (v6 — Q, Nov 8, 2026)

"Pursue the highest potential in every aspect. Learn everything. Master
everything. Improve on everything."

- No cap on what the mastermind learns: every style, every system, every
  prompt, every code, every creator, every domain (editing, strategy,
  psychology, sales, coaching). No "that's enough" ceiling.
- No ambition ceiling: the goal is the best in the world at each aspect,
  then better. Sky is the benchmark to BEAT, not just match.
- No scope walls between specialists: cross-pollination is the default —
  a new specialist is ADDED when a new aspect needs its own master, never
  by shrinking an existing one.
- No fear of scale: the library grows without a ceiling (modular parts +
  GitHub pull + weekly sweep + self-learning). If a part gets big, split
  it — never shrink the ambition to fit a limit.

The KEEP side (NON-NEGOTIABLES — identity + safety, not limits on
potential): brand DNA (nothing over Q's face, teal/gold on navy, NO RED,
PWC skin, logo, human-made check); SAFETY.md (quarantine, code scan, no
credentials, no scams/phishing, only public freely-licensed material);
licensing rules (no paywalled/piracy content; license-flagged kits need Q's
word); Q's standing rules (blur law, hidden app never named, newest-version
posting, keyword flows live before posting); Anthropic's own policies —
never instruct bypassing them. Full split: README.md "NO-LIMITS vs
NON-NEGOTIABLES". Same stance lives in skills/pwc-design-system/SKILL.md.

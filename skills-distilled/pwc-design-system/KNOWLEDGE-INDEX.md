# KNOWLEDGE INDEX — topic playbooks (the "actually execute" bar)

Every playbook entry must contain EXECUTABLE content: the command, the
code snippet, the parameter values, the file to create. An entry with only
theory gets flagged [THEORY ONLY]. Each entry cites its source (video URL +
timestamp, or guide URL + section).

## Status — Phase 4 harvest COMPLETE (Nov 8, 2026)

**Execution-bar pass rate: 83/89 entries executable = 93.3%.** 6 entries
flagged [THEORY ONLY] (Appeal; easing ≠ physics; move = story; steal the
pattern; caption density; no grade rescues bad footage). Full index:
`research/knowledge/INDEX.md`. Sources: 23 YouTube videos attempted (18
with files, ~130k words of transcripts), ~40 free guides/docs, 48 distinct
URLs cited. Safety: all folders quarantined + scanned first (SAFETY.md);
parked items recorded in `research/knowledge/INDEX.md` (private video,
5 empty 429 folders, email-gated + paywalled items → BUY-LIST.md).

| # | Playbook | Status | Entries | Executable | Lives |
|---|---|---|---|---|---|
| 1 | MOTION-PHYSICS.md | **DISTILLED** | 12 | 11 | `research/knowledge/MOTION-PHYSICS.md` — timing/spacing, mass/weight, anticipation (pull back 2–4 frames), arcs (curviness 1.25), squash & stretch, follow-through, exaggeration, secondary action |
| 2 | EASING.md | **DISTILLED** | 11 | 10 | `research/knowledge/EASING.md` — GSAP eases as a system (power1.out default, power2.out workhorse, power4.out punch, back.out/elastic.out one-moment-only, stagger 0.1 / {amount: 2} / {from: "center"}) + `skills/pwc-motion-playbooks/references/GSAP-EASES.md` |
| 3 | CAMERA-MOVES.md | **DISTILLED** | 8 | 7 | `research/knowledge/CAMERA-MOVES.md` — full move vocabulary with story meaning (StudioBinder) + 25 AI-filmmaker moves |
| 4 | IMAGERY.md | **DISTILLED** | 9 | 8 | `research/knowledge/IMAGERY.md` — composition, framing, diagram grammar, steal-the-pattern rule |
| 5 | CAPTION-SYSTEMS.md | **DISTILLED** | 8 | 7 | `research/knowledge/CAPTION-SYSTEMS.md` — Whisper/ASS caption guides, density rule + `skills/pwc-designed-captions/` (6 styles, word-exact timing) |
| 6 | COLOR-GRADE.md | **DISTILLED** | 6 | 5 | `research/knowledge/COLOR-GRADE.md` — node order, orange-and-teal mistakes, LUT guidance (PWC palette law overlays: teal/gold/navy, NO RED) |
| 7 | SOUND-DESIGN.md | **DISTILLED** | 8 | 8 | `research/knowledge/SOUND-DESIGN.md` — 8/8 executable + Adilet audio chain measured (−14.19/−14.16 LUFS, LRA ~2–2.6) |
| 8 | RENDER-PIPELINES.md | **DISTILLED** | 8 | 8 | `research/knowledge/RENDER-PIPELINES.md` — 8/8 executable + caption pipeline + animation renderer + QC gates |
| 9 | CLAUDE-CODE-WORKFLOWS.md | **DISTILLED** | 8 | 8 | `research/knowledge/CLAUDE-CODE-WORKFLOWS.md` — Noa Arnold's full stack (ffmpeg/node/uv/yt-dlp, ElevenLabs STT-only, HyperFrames + watch, workspace layout, first-cut/brief/feedback prompts, package-it-into-a-skill loop) + Claude Code Hooks (PostToolUse format, PreToolUse rm-rf guard exit 2, Notification ping) |
| 10 | PROMPT-PATTERNS.md | **DISTILLED** | 11 | 11 | `research/knowledge/PROMPT-PATTERNS.md` — 11/11 executable + `design-system/PROMPTS.md` (10-entry library) |
| 11 | GESTURES-MOVEMENTS.md | **DISTILLED** | 20+ | 20+ | `research/knowledge/GESTURES-MOVEMENTS.md` — the visual-language vocabulary (video-recognition layer, Nov 8): gesture → meaning → when creators use it → how the edit responds. OBSERVED entries from decoded video (David DfdAvbfRQY5 frames: look-to-camera held, face still while devices move; Viashaan hero-behind-head 35.66s, lying-down 27.5–31.4s; Sky point-at-stack; Adilet whip/zoom-kick) + INFERRED working rules (point = cut to thing, look down = phone screen, lean = punch-in, hand count = number chips). Feeds the Motion + Camera specialists. Every decode logs gestures + cut motivations (TEMPLATE.md §9). Part: `parts/knowledge-playbooks/gestures-movements.md` |

## v6 additions (Nov 8, 2026 — 100 parts, 19 categories)

| Entry | Where it lives |
|---|---|
| CLAP audio understanding (LAION CLAP, MIT) | Audio: `parts/audio-sound/audio-clap-understanding.md` — text↔audio retrieval over the licensed SFX library, timeline sound QC, threshold ≥0.5. LAION CLAP only, never M2D-CLAP (non-commercial). |
| Demucs stem separation (LICENSE FLAG) | Audio: `parts/audio-sound/audio-demucs-stems.md` — code MIT / weights research-use only. Folded as workflow WITH the flag; input must be Q's own licensed audio. |
| Loadout device (kappa 5-tool stack) | Motion/devices: `parts/creator-systems/kappa-5-tool-stack.md` — HyperFrames + Whisper + CLAP + Demucs + Blender as the toolchain row under the router; HyperFrames install `npx skills add heygen-com/hyperframes` MEASURED (78k stars / 7.2k forks, 7 installed skills). Format as its own part: `parts/creator-systems/kappa-loadout-format.md` (bar, counter, LEGENDARY slot, DM-cards, "+2 MORE" beat); Blender as free 3D: `parts/creator-systems/blender-free-3d.md` (GPL, 0 credits). |
| UNLOCK device class | Motion/devices + SKY-SCORE.md — the checklist/tool unlock beat (kappa De9VlbBtQCY: hook → count-up proof → checklist unlock → proof cards → CTA). New cut-motivation class in `research/knowledge/GESTURES-MOVEMENTS.md`. |
| Hookscore kill-gate + deadair gate | Hooks/QC: `parts/hooks/hooks-hookscore-kill-gate.md` (opusjake, MIT, SCAN PASS) + `parts/render-pipelines/pipeline-deadair-gate.md` (0.35s floor). |
| AnimationBase review loop | Motion: `parts/motion/motion-animationbase-review-loop.md` (MIT, SCAN PASS) — sheet → strip → crop review loop, reads-as-timing, transitions at every seam. |

## v8 additions (Nov 8, 2026 — 197 parts, 20 categories; Batch 5 Bradford Marais scriptwriting lane, Batch 6 Create Content Club, Batch 7 Jack Roberts, Tier S seed: charliehills / mehganjames / ibravisual / kingketo doctrine)

- **Scriptwriting lane (NEW Category 20):** `parts/scriptwriting/` — content-architecture (Brand Brain → Playbook → Quality Gate + 4-step run + AI OS container + interview front end), brand-brain (3 files, all 3 wordings recorded), script-structures (12 structures, INFERRED mapping), quality-gate (95-gate threshold [NEEDS Q'S WORD]), contrast-device, viral-rewrite-skill (Bradford layers + CCC mechanism, outperformance gate [NEEDS Q'S WORD]).
- **Tier S seed:** skill-doctrine-save-it-as-a-skill (save every working system as a skill — the library's own operating doctrine), self-check-95-gate (charliehills 95-gate as a scored rubric, INFERRED mapping to Q's gates; threshold [NEEDS Q'S WORD]), charliehills-27-things-os, mehganjames-5-pass-method, ibravisual-slash-command-pack (9 commands, 8 named + /broll /sound sharing a slide; 61-effect count, names unknown — do NOT invent).
- **Batch 7 (Jack Roberts):** find-skills-discovery-layer (discovery WITH the safety gate, NEVER an auto-installer; external-registry scope [NEEDS Q'S WORD]), claw-machine-picker (the router picks, visual), claude-mods-watcher-handoff (watcher + 4-field handoff brief), deeper-expert-prompt (task → goal reframe + expert review), review-mining-rebuild (review-mining adopted; wholesale Replica clone PARKED), kitchen-tactile-ui (cassette / hold-to-confirm / receipt as CapCut motion devices — effects v4), dev-team-skills-subagents (skills + sub-agents as a team; the library's own shape).
- **Batch 6 (Create Content Club):** ccc-script-to-carousel (every reel script becomes its carousel twin the same day; interview questions 2–3 ungated-unknown — GAP).
- **Knowledge entries reconciled (v8):** the weekly sweep's "89 → 182" and Stream 2's V8-01–V8-182 are the SAME 182 entries — V8-01–V8-182 verified present in `research/knowledge/*.md`, none missing, none double-counted. Total `###` headings across `research/knowledge/*.md` is 487 (includes the 182 V8 entries + Phase 4 + self-learning + playbook sections — NOT a second knowledge total; do not cite 487 as the knowledge-entry count).

## HyperFrames ranking evidence — independent validation of Q's hyperframes skill choice (Jack Roberts, Nov 8, 2026)

Source: @jackroberts___ reel DePtyBoAOPd "Find Skills" (parent-decoded, Batch 7), frame f_020 — the ranked list of Claude skills by downloads, shown on screen (VERBATIM-FRAME). Full top 10, as shown:

| Rank | Skill | Downloads (as shown) |
|------|-------|----------------------|
| 1 | grill-with-docs | 1.1M |
| 2 | improve-codebase-architecture | 1.1M |
| 3 | agent-browser | 1.0M |
| 4 | tdd | 1.0M |
| 5 | frontend-design | 955.4K |
| 6 | setup-matt-pocock-skills | 944.0K |
| 7 | **hyperframes-cli** | **818.4K** |
| 8 | reddit-automation | 808.0K |
| 9 | **hyperframes** | **785.5K** |
| 10 | vercel-react-best-practices | 772.3K |

**HyperFrames appears TWICE in the top 10** — hyperframes-cli at #7 (818.4K installs) and hyperframes at #9 (785.5K installs). This is independent validation, from a ranked list the library did not produce, that HyperFrames is a top skill in the Claude ecosystem — confirming Q's existing hyperframes + hyperframes-cli skill choice (already in Q's stack; see KNOWLEDGE-INDEX.md §9 / kappa loadout: HyperFrames install `npx skills add heygen-com/hyperframes`, MEASURED 78k stars / 7.2k forks, 7 installed skills).

Notes:
- The numbers are the ranking site's figures as shown on screen in the reel (Nov 2026), not the library's own measurements — recorded as shown, not re-verified.
- The same reel ranks find-skills itself #1 (3.7M, frame f_028) — the discovery-layer context for this evidence; see `research/v8-drafts/batch7/find-skills-discovery-layer.md`.
- Source file: `research/video-harvest/instagram/jack_roberts_DePtyBoAOPd_DECODE.md` ("The ranked list (f_020)").

## v7 additions (Nov 8, 2026 — 177 parts, 19 categories; Rundown A + B + tenfoldmarc)

| Entry | Where it lives |
|---|---|
| Ootto content-skills repo (MIT, SCAN PASS — 54 skills) | Creator-systems: `parts/creator-systems/ootto-virality-hook-doctor.md` (8-point hook checklist, best-vs-flop frame-by-frame), `ootto-reel-analyzer.md` (URL → hook/beats/pacing/visuals + face-safe tagging), `ootto-hook-mining.md` (local CSV miner, `mine_hooks.py` read in full), `ootto-content-factory.md` (format → reel → captions → DM loop, stops on failure), `ootto-going-viral-strategy.md` (goal → emotion → hook + funnel; promise → withhold → escalate → pay off), `ootto-content-skills-index.md` (the 54-skill map by job). The Ootto MCP connector + DM-gated skill files + auto-DM are NOT adopted. |
| nategoldai/instagram-agent (MIT, SCAN PASS — 13 skills) | Creator-systems: `parts/creator-systems/nategold-instagram-agent.md` (the pack + voice.md first + 5 local Python tools); `nategold-ig-profile-audit.md` (12-item rubric, 100 pts, fix-first order). Hooks: `parts/hooks/hooks-hookscore-26-formulas.md` (26 formulas + hookscore.py, AUC 0.83 bad-vs-real / 0.56 hit-vs-miss — stated honestly). Strategy: `parts/strategy/strategy-outlier-multiple-swipe.md` (outlier multiple = views ÷ own median; over 3x is a signal). Captions: `parts/captions/captions-ig-humanizer.md` (humanize.py + detect.py, 5-check panel, PASS 70+ / no check under 55 — the executable HUMAN-MADE CHECK). CreatorCut reference-first edit: `parts/creator-systems/nategold-creatorcut-reference-first.md` (INFERRED; app GATED). The "100 reels at once" claim is UNVERIFIED — never present as verified. The IG → Claude connector NEEDS Q'S WORD. |
| Liamrjohnston/hook-master-skill (MIT, SCAN PASS — 9 skills) | Creator-systems: `parts/creator-systems/liam-hook-master-suite.md` (four-failures check → viewer panel → council → 6 hook formats → niche-tuner → visual-match → lock-in → viral-scout; honesty rules adopted verbatim). Hooks: `parts/hooks/hooks-jev-hook-bank.md` (six dimensions, rank by real views, retire tired shapes on evidence — INFERRED; Jev setup GATED + IG-connect NEEDS Q'S WORD). Creator-systems: `parts/creator-systems/liam-remotion-command-catalog.md` (7 commands, POV split-screen, "one world, one moving camera" — INFERRED; Remotion stack GATED). |
| /spy pipeline + /hooks skill (specs only — code PARKED) | Creator-systems: `parts/creator-systems/tenfoldmarc-spy-pipeline.md` (SCRAPE last 50 → OUTLIERS 5× median, 30 days → DECODE → [bracket] template → REPORT) + `tenfoldmarc-hooks-skill.md` (`/hooks [reel url]` → Whisper → hook bank). Both repos PUBLIC but LICENSE UNVERIFIED — code PARKED per SAFETY §7 until license confirmed + §6 scan; the specs above are the fold, not the repos. |
| 3-hook trial-reel method + variation taxonomy | Creator-systems: `parts/creator-systems/tenfoldmarc-3-hook-trial-reels.md` (verbatim prompt "Make 3 trial reels. Use a different part of the video as the hook for each." — also PROMPTS.md §24; HOOKS ①②③ + BODY + CTA; MIRRORED / NEW HOOK / NEW GRADE). Content Dashboard prompt verbatim: PROMPTS.md §25. |

## Strategy files (the mastermind past editing — Nov 8)

Not playbooks — the strategy layer. Full specs in
`design-system/AGENTS.md` §12–16 and `design-system/STRATEGY.md`.

| File | Owner | What it is |
|---|---|---|
| `research/knowledge/AUDIENCE-PSYCHOLOGY.md` | Following-Growth Specialist (#13) | Identity, inside language, rituals, retention loops, plural proof, shared story, visible progression |
| `research/knowledge/SALES-CLOSING.md` | Closer Specialist (#14) | Q's actual offers only (Premium $97/mo, Dec 7 cohort, Dec 13 close, waitlisters +1 month free, CALENDAR $35); objection table; real deadlines only |
| `research/knowledge/CREATOR-PAIN-POINTS.md` | Coach Specialist (#15) | Top 10 pains ranked by frequency + intensity, exact creator wording, public sources cited (Talentir Sept 2026; r/UGCcreators; Velena) |
| `research/knowledge/TRENDS.md` | Trend Analyst (#16) | Top 5 what's working now, measured engagement only (David 1,123 likes / 1,652 comments; P1 v9/P2/P3 live) — refreshed weekly, stale rows dropped |

## Top 5 videos (by what each taught)

1. **Noa Okazaki Arnold — "How I Edit My YouTube Videos With Claude Code
   (Fully Automated)"** (youtube.com/watch?v=wrZpU_VfHp4, Oct 28 2026) —
   the full stack: `brew install ffmpeg node uv yt-dlp`, ElevenLabs MCP
   speech-to-text-only, HyperFrames + watch skill, workspace layout,
   first-cut/brief/feedback prompts, frame.io-style previewer,
   package-it-into-a-skill loop.
2. **HankTheTank — "The Ultimate GSAP Crash Course (2026)"**
   (youtube.com/watch?v=aJmP2II5R4U) — eases as a system (see EASING.md).
3. **Joshua Craigie — "10 Motion Design Principles Every Animator Needs"**
   (youtube.com/watch?v=Cz-GcIITNrs) — timing/spacing, easings,
   mass/weight, anticipation, arcs, squash & stretch, follow-through,
   exaggeration, secondary action, appeal.
4. **StudioBinder — "Ultimate Guide to Camera Movement"**
   (youtube.com/watch?v=IiyBo-qLDeM) — full move vocabulary with story
   meaning + chapter timestamps.
5. **Simple Tech Man — "Claude Code Hooks: Auto-Format Every Edit"**
   (youtube.com/watch?v=BewHVJNFR2I) — the three hooks (PostToolUse
   format, PreToolUse `rm -rf` guard with exit 2, Notification ping) +
   `/hooks` check.

## Sources feeding the playbooks (on disk now)

- @viashaan "Describe Motion to AI" — 8 named motions with CSS + Python
  values (`skills/pwc-animations/MOTION.md`, identical in
  `skills/pwc-designed-captions/MOTION.md`).
- Adilet teardown — measured pacing (222 wpm, beats every 1.5–3.5s),
  caption lead (+0.013s median over 86 changes), loudness (−14.19/−14.16
  LUFS), hook/pacing/motion/captions/audio exhibits
  (`research/adilet-teardown/`, `skills/adilet-system/`).
- Sky system — 13 forms, D1–D14 devices, E1–E10 recipe, motion QC §9
  (`skills/realskytan-system/SKILL.md`).
- Herk Edit Kit — measured house style (1.1–1.4s shots, pauses <0.2s,
  split-first-frame, self-correcting skill loop)
  (`research/sky-like-creators/nateherkai/`).
- Zeeuiux Reel Style Rules — canvas/type/colour/motion numbers
  (`research/sky-like-creators/zeeuiux/Reel-Style-Rules.md`).
- Phase 4 harvest — 23 YouTube videos + ~40 guides, distilled into the 10
  playbooks above (`research/knowledge/`, `research/knowledge-harvest/`).

## What the next sweep adds

- Retry the 5 empty 429 folders with a fresh IP / `--cookies-from-browser`
  on a logged-in machine, or youtubetotranscript.com as fallback.
- Read the GSAP + Remotion official docs in full (cited from excerpts
  this round).
- New videos/guides found by the weekly sweep distill into these same 10
  files (same execution bar) — the index's pass rate is re-computed each
  pass. View counts from the yt-dlp android client are unreliable — never
  cite harvested view counts; rank by relevance + recency.

## v9 additions (Nov 8, 2026 — 261 parts, 20 categories; bulk harvest row-level adoption)

- **Bulk harvest, row-level (623 rows + 7 flat canonicals = 630/630):** every
  `*DECODE.md` in `research/video-harvest/` now has an adoption row —
  `research/video-harvest/v9_adoption_bulk_a.md` (188), `v9_adoption_bulk_b.md`
  (188), `v9_adoption_bulk_c.md` (188), `v9_adoption_yt.md` (59) — plus the 7
  flat canonical decodes (bradford_marais, createcontent_club, david_knowsai,
  jack_roberts, kappa_ai, marc_cleroux, stockton_walbeck), already adopted in
  v8. Statuses: IMPLEMENTED 289 / STAGED 221 / GAP 54 across the three bulk
  files. All 630 decode files exist on disk (the 3 `*_CAROUSEL-DECODE.md`
  files match `*-DECODE.md`, not `*_DECODE.md` — an earlier glob missed them;
  no file is actually missing). Decodes + transcripts ship as text in the
  `pwc-decodes-*` pieces (mp4s / frame images stay in the workspace/repo as
  evidence, too large for skill zips by design).
- **Knowledge entries land as text (the v8-fold correction):** a literal grep
  of V8 IDs in `parts/` returns 0/182 — the v8 "fold" was the entries living
  in the knowledge playbooks, not in part files. V9 fixes the landing: the
  playbooks themselves ship as pieces (`pwc-knowledge-editing.zip`,
  `pwc-knowledge-strategy.zip`), so all 182 V8 entries are in Claude as text.
  Disposition (`research/knowledge/v9_verification.md`): 109 → new v9 part
  drafts, 66 → variant notes on named parts (or new drafts), 4 COVERED,
  1 GAP (V8-182 Zapier MCP as YouTube connector — needs Q's word),
  1 SAFETY NOTE (V8-103 face swaps: AI-generated people only),
  1 CAPABILITY NOTE (V8-161 Recordly.dev, open source, not installed).
  Discrepancy carried as observed: `research/knowledge/INDEX.md` per-playbook
  counts sum to 184 against the stated total of 182 (likely double-counted
  entries or a table error; the 182 unique V8 IDs were verified independently).
- **Widened net, row-level (105/105 profiles):**
  `research/claude-editing-creators/v9_adoption_widened.md` — 21 already
  covered in v8 (§A) + 84 newly rowed (20 with decoded videos in §B, 21
  widened-net profiles in §C1, 43 SOURCES-only in §C2). One new draft from
  widened-net: D16 effects-comment-pile.md (@patlaw). ~70 GAP rows, mostly
  §C2 "deeper pull needed" flags on thin single-post records.
- **New parts (64):** creator-systems +32, effects +9 (44 → 53), render-pipelines
  +14 (8 → 22), prompts +8 (5 → 13), scriptwriting +1 (6 → 7). One draft
  NOT promoted as a part: charliehills-27-things-one-brain.md is the same
  system as the existing charliehills-27-things-os.md (same 8-slide carousel,
  same "one brain" rule) — folded as a variant note onto the canonical part,
  not duplicated.
- **Self-learning check-in (Nov 8, 2026):** v8 fold verified 45/45 (38 SL +
  7 PB present in `parts/`, 4 FL correctly absent); no new lessons, no new
  conflicts, no new FL entries. `parts-staging/self-learning/V9-CHECKIN-2026-11-08.md`.
- **Effects v5 warranted:** 9 new effect parts (xray-body-track,
  charliehills-21-effect-catalog, finger-gun-pop, logo-sting-variants,
  code-component-library, hologram-book, outfit-callout, slot-machine,
  comment-pile) — effects v5 ships the full 53-part set.

## v10 additions (Nov 8, 2026 — 297 parts, 20 categories; Batch 8 + §C2 row-level adoption)

- **Batch 8 + §C2, row-level (35/35 targets resolved):** 22 NEW decodes + 6
  already-decoded (1 duplicate folded once) + 5 NON-VIDEO carousels
  (content/structure only) + 2 rate-limited GAPs. Manifest:
  `research/video-harvest/instagram/BATCH-8-Q-LINKS.md`; adoption rows:
  `research/claude-editing-creators/ADOPTION-TRACKER.md` (v10 section).
  Decodes + transcripts ship as text in `pwc-decodes-v10.zip` (22 new
  DECODE.md + 22 transcripts + 3 CAROUSEL.md); the 6 already-decoded
  DECODE.md files already ship in the v9 `pwc-decodes-bulk-*` pieces and
  are NOT duplicated here.
- **New parts (23):** effects +11 (53 → 64: clone-me, sticker-me,
  light-paint, stage-lights, hand-track, logo-rain, film-grade, card-pop,
  motion-poster, prospect-quote-card, modern-vox), creator-systems +5
  (102 → 107: kayvon-live-effects-router, ali-five-skill-system,
  minolee-3-core-things, kreettanam-3-install-profile,
  retainer-partnerships), scriptwriting +2 (7 → 9: asd-ste100-80-rule,
  curiosity-math), audience-psychology +2 (7 → 9: tacit-knowledge,
  client-language), sales-closing +2 (4 → 6: prospects-wins-rule,
  transfer-of-certainty), strategy +1 (10 → 11: posting-mix-70-20-10).
  Variant entries: 20, across 20 existing parts. No new categories; no
  duplicates — /text-behind, /logo-orbit and /new-room are variants on
  existing canonical parts, not new parts.
- **Design-system v10 BUILT (reversal of the earlier "NOT built" call):** the distilled-doc changes grew past the v10 threshold when Q added the asset-pool rule (Nov 8, ~19:26 CT) — AGENTS.md asset-pool section + Imagery #6 ask-Muse line, EDIT-ROUTER.md Q12 + NEVER-list bullet, SKILL.md v10 line + 12-question intake, plus PROMPTS.md §38 (ASD-STE100), this index section, and CATEGORIES.md counts. `pwc-design-system-v10.zip` staged in Wave 10; v9 stays the live rollback until v10 is uploaded and verified ON. Effects v6 IS warranted: 11 new effect parts + 5 variant-updated parts (64 total in `claude-video-effects-main/pwc-design-parts/`).
- **Asset-pool rule (Q, Nov 8, ~19:26 CT):** Claude ALWAYS has Q + Kiya's own assets (photos, videos, proofs, B-roll, brand assets + asset vault) — use them first; missing asset → ask Muse, never substitute/invent/skip. Folded into AGENTS.md (new section + Imagery #6), EDIT-ROUTER.md (Q12 + NEVER bullet), prompts-router-intake.md (Q11 + v10 variant), and the three asset-related parts touched in this run (imagery-proof-objects, effects-phone-mockup, effects-prospect-quote-card).
- **Self-learning check-in (Nov 8, 2026, v10):** no new lessons, no new
  conflicts, no new FL entries. The v10 run's verified lessons are
  procedural (fold confirmations, not rule changes): (1) already-decoded
  steals may already be folded — check the part files before writing a
  duplicate (doctablademd was v9-folded; millee's 5 rules were v9-folded
  as variants; corbinsylk's doctrine was v9-folded); (2) a duplicate
  archive folder (`minolee.mp4_DfBBG0xPioN/` vs canonical
  `millee.md_DfBBG0xPioN/`) is noted, never deleted; (3) a pre-existing
  index conflation was flagged, not silently fixed
  (top-creator-index-niche.md row A3 credits Minolee with Millee's 0.1s
  rule + 5 anti-slop rules). QC status PENDING for every v10 part/profile
  until the you-and-Claude loop runs after upload.

## v12 additions (Nov 8–9, 2026 — 308 parts, 20 categories; Batch 10 row-level adoption)

- **Batch 10, row-level (1 Top-30 reel + 18 decodes + 5 carousels +
  316/321 inventory):** the Top-30 reel (DfDAxN1Rex_, 57.0s, 172 words,
  12 segments) + 18 @maxjohnscn decodes (17 NEW systems + 1 re-hook
  variant) + 5 NEW carousel files (caption-level only, GAP-6 class —
  slides not retrievable) + the full @maxjohnscn profile teardown
  (316 distinct feed shortcodes of 321 claimed, 98.4%; 292 video / 22
  carousel / 2 image; 5-post gap recorded honestly; pagination cursor
  dead, windowed --until pulls recovered the rest). Max Johnson,
  60,026 followers, UK, founder @briix.ai & Level Up AI Creators.
  Decodes + transcript + teardown + SOURCES ship as text in
  `pwc-decodes-v12.zip` (19 DECODE.md + 1 transcript + 5 CAROUSEL.md +
  BATCH-10 manifest + TEARDOWN.md + SOURCES.md); videos and frames stay
  in the workspace/repo.
- **New parts (8):** creator-systems +6 (107 → 113:
  maxjohnscn-stacks-trilogy, maxjohnscn-weekend-menu-ten-systems,
  maxjohnscn-agency-stack, maxjohnscn-video-skills-five,
  maxjohnscn-vibecode-ship-checklist, maxjohnscn-mini-saas-menu),
  sales-closing +1 (6 → 7: maxjohnscn-brand-deal-tactics),
  knowledge-playbooks +1 (16 → 17: maxjohnscn-top30-inventory).
  Variant entries: 6, across 6 existing parts
  (strategy-content-strategy: the 8-system content→money loop as a
  variant on Q's loop, never a competing loop;
  strategy-dashboard-carousel: the 5 carousel structure steals, Sky
  form; agents-md-onboarding: the 4-doc starter kit, PRD +
  ARCHITECTURE as the gap pair; competitor-scrape-pipeline: Reverse
  API Engineer as a research pattern, spec only; ibravisual-jarvis-
  4-part-build: the Atticus "work mode" named-routine pattern, app
  stays PARKED per the Batch 7 ruling; effects-paper-cut: Collage
  B-Roll). No new categories; no duplicates (checked before writing:
  the 4-doc kit overlaps agents-md-onboarding, so it is a variant,
  not a part; the 8-system loop overlaps Q's loop, so it is a variant,
  not a part; HyperFrames is already in the library — sighting only).
- **FIND-SKILLS — the real skill, folded (Q's priority order, Nov 8
  ~21:02 CT; resolves v8 ruling #11):** `find-skills` from
  vercel-labs/skills (MIT, Copyright 2026 Vercel, Inc.), SCAN PASS —
  SKILL.md pure instructions, no executable code, no credentials;
  find.ts queries only the public https://skills.sh search API;
  telemetry anonymous + disable-able via DISABLE_TELEMETRY=1. The
  skill is ONE file: `skills/find-skills/SKILL.md` (5,472 B, verbatim
  upstream). Install: `npx skills add vercel-labs/skills --skill
  find-skills -a claude-code` (as shown on Max's reel:
  `npx skills add vercel-labs/skills@find-skills`). Verified live:
  "video editing" → hyperframes (1,436,743 installs), media-use
  (1,346,326), ai-video-generation; "instagram" →
  viral-instagram-reels, social, ads, social-content. Staged as its
  own Wave 12 zip (`find-skills.zip`: SKILL.md + PWC-OVERLAY.md).
  **PWC safety overlay (binds over the upstream Step 6):** the skill
  NEVER auto-installs — it finds, verifies, and PRESENTS options;
  installation only when Q approves a specific skill; any recommended
  skill still goes through the dual-model review (ChatGPT + Claude)
  before install; the upstream `-y` flag is NOT used. The
  find-skills-discovery-layer part stays the doctrine and now points
  at the real skill (its v8 GAPs for the repo + the skill file are
  marked RESOLVED, history kept). Third sighting (Max, DfDAxN1Rex_)
  recorded as a v12 variant on that part — his reel shows the install
  command with NO safety note, unlike Jack.
- **Top-30 triage (29 new repos, read-only license check, Nov 9):**
  26 LICENSE PASS (20 MIT + 6 Apache-2.0 — inventory rows only, SCAN
  not run) · 3 PARKED (OpenMontage AGPL-3.0; multica-ai/
  andrej-karpathy-skills + anthropics/skills: no LICENSE file) · 0
  GAP · HyperFrames already in library. Two as-shown repos did not
  resolve and were corrected against GitHub: `LeonxInx/taste-skill`
  → `Leonxlnx/taste-skill` (MIT); `tt-a1l/archify` →
  `tt-a1i/archify` (Apache-2.0). Full table in
  `research/claude-editing-creators/ADOPTION-TRACKER.md` (v12
  section) and `parts/knowledge-playbooks/maxjohnscn-top30-inventory.md`.
- **Design-system v12 NOT built (call recorded in UPLOAD-ORDER.md,
  Wave 12):** no AGENTS.md / EDIT-ROUTER.md / PROMPTS.md changes in
  this run, so the distilled docs do not warrant a new version. What
  changed is limited to CATEGORIES.md (308 parts + v12 names),
  KNOWLEDGE-INDEX.md (v12 additions), and COMPONENTS.md (the
  find-skills cell: the discovery layer is no longer "the SPEC, not
  the skill" — the real skill is folded) — all updated in
  `design-system/` AND the installed mirror
  `skills/pwc-design-system/` (diff verified empty) — and those ride
  the GitHub pull route now, not a new design-system zip. The v10 zip
  stays the live design-system build until a future run warrants v12.
- **Self-learning check-in (Nov 8–9, 2026, v12):** no new lessons, no
  new conflicts, no new FL entries. The v12 run's verified lessons
  are procedural (fold confirmations, not rule changes): (1) when a
  decode's system overlaps an existing canonical part, fold as a
  variant on the canonical — check the part files before writing a
  duplicate (the 4-doc kit → agents-md-onboarding; the 8-system loop
  → strategy-content-strategy; Collage B-Roll → effects-paper-cut);
  (2) a reel's on-screen repo spellings can be wrong — resolve
  404s against GitHub before citing (LeonxInx → Leonxlnx, tt-a1l →
  tt-a1i) and record both spellings; (3) a license-passed inventory
  row is not a SCAN PASS — record the license result and the
  not-yet-scanned status in the same row. QC status PENDING for every
  v12 part/profile until the you-and-Claude loop runs after upload.

## v11 additions (Nov 8, 2026 — 300 parts, 20 categories; Batch 9 row-level adoption)

- **Batch 9, row-level (1 decode + 5 carousels + 10 reconciled):** 1 NEW
  decode (Det_axVk5c_, 22.72s, VARIANT of Dd9 — same ccc-self-onboarding
  system, input-side demo cut) + 5 NEW carousel files (caption-level
  only, GAP-6) + the 10 already-decoded CCC files reconciled (see
  `research/claude-editing-creators/ADOPTION-TRACKER.md`, v11 section).
  CCC carousel coverage: 6/50 covered, 44 uncovered (GAP-6) —
  `research/claude-editing-creators/createcontent.club/CCC_CAROUSEL_COVERAGE.md`.
  CCC feed diff vs v8: inventory identical, 0 new feed posts (newest
  post Nov 8 Dfe7In2kaCW, already in the v8 catalog). Decodes +
  transcripts ship as text in `pwc-decodes-v11.zip` (1 DECODE.md + 1
  transcript + 5 CAROUSEL.md + BATCH-9 manifest); the 10 already-decoded
  files already ship in the v9 `pwc-decodes-bulk-*` / canonical pieces
  and are NOT duplicated here.
- **New parts (3):** strategy +1 (11 → 12:
  ccc-self-onboarding-interview), effects +2 (64 → 66:
  spotlight-question-highlight, spinning-asterisk-hook-burst). Variant
  entries: 8, across 5 existing parts (ccc-content-strategy-skill ×5 —
  skill name, competitor-profile research proof, three format cards,
  10-idea Notion table, solo demo-cut template; trial-reel-test-spec;
  hooks-hookscore-26-formulas; pipeline-repurposing-one-to-ten). No new
  categories; no duplicates — the asterisk burst is a NEW part because
  no canonical hook-burst part existed (checked: logo-sting-variants is
  a logo-animation menu system, logo-rain is falling logos,
  zoom-through-cut is a transition, halo is orbiting screens).
- **Design-system v11 NOT built (call recorded in UPLOAD-ORDER.md,
  Wave 11):** no AGENTS.md / EDIT-ROUTER.md / PROMPTS.md changes in
  this run, so the distilled docs do not warrant a new version. The two
  v10 open corrections ARE fixed in this run: (a)
  top-creator-index-niche.md row A3 corrected to @millee.md
  (DfBBG0xPioN, 60.6K, MOTION), @minolee.mp4 moved to new row A35 with
  his own fields (551–580K, WORD, DehM80nN7Gv 3-core things); the
  minolee SOURCES.md misattribution (DfBBG0xPioN listed as a Minolee
  reel) corrected at the source too — and the same conflation found by
  a late grep in two more places, also corrected: creators INDEX.md
  item 12/24 and the DehM80nN7Gv DECODE.md creator line. (b) prompts-router-intake.md
  annotated as an 11-question paste-ready variant of the router's
  12-question intake — router Q2 (named system/framework), Q5 (power:
  number / story / proof / breakdown), and Q11 (viewer feeling →
  psychology part) have no paste-ready equivalent, while part Q4
  (audience) and Q8 (hook in first 2s + face on screen) are part-only
  additions; full 12 in EDIT-ROUTER.md §2. That file change puts
  `pwc-prompts.zip` in Wave 11.
- **Self-learning check-in (Nov 8, 2026, v11):** no new lessons, no new
  conflicts, no new FL entries. The v11 run's verified lessons are
  procedural (fold confirmations, not rule changes): (1) when a part is
  a paste-ready variant rather than a verbatim copy of the router,
  annotate the exact question-level differences instead of forcing a
  count match; (2) when an index row conflates two creators, split it —
  correct row + new row for the displaced creator, never delete one,
  and correct the misattribution at its source file too; (3) a carousel
  coverage inventory is the reconciliation tool for "6 decodes" vs 10
  files — count distinct videos, carousel decodes, and duplicate-variant
  files separately. QC status PENDING for every v11 part/profile until
  the you-and-Claude loop runs after upload.

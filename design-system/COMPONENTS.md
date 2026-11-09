# COMPONENTS.md — every object, built once, reused everywhere

The registry. Before building anything visual, check here: if it exists,
use the registered build (exact colors, exact geometry) — do not redraw it
from memory. If it doesn't exist, build it once, register it here with its
home and spec, then use it. This file is what makes ten videos look like
ONE system.

## The Edit Router (home: design-system/EDIT-ROUTER.md)

The decision layer above all lane skills. On every job, the router picks the
style family, devices, motion set, caption treatment, audio chain, and QC
gates for the video's type — and outputs a RECOMMENDATION (style pick + three
grounds: capability, creator system, viral evidence) BEFORE building. The
router's NEVER list outranks every lane skill. Its "WHAT'S WORKING NOW" table
is maintained by the weekly continuous-learning sweep (see
CONTINUOUS-LEARNING.md at the folder root).

## Sky-like creators + free kits — appendix (home: research/sky-like-creators/, research/free-claude-editing-kits/, research/claude-editing-creators/)

> **North star:** Claude with infinite space, infinite knowledge, and the
> ability to learn — so Q's edits are so sharp and on point people can't
> believe it's AI. Judge every entry here against it: does it make Claude
> know more, learn faster, and edit more human? Every new learning also
> gets applied back to the Sky edits — see SKY-SCORE.md: match Sky
> perfectly, then beat him.

Reusable devices, prompts, and workflows harvested from Sky-like creators,
free Claude Code editing kits, and Instagram Claude-editing teachers — with
attribution and MEASURED / INFERRED / PUBLISHED labels. Full ranked lists:
those folders' INDEX.md files.

### Sky-like creators (researched Nov 8, 2026 — full index: research/sky-like-creators/INDEX.md)

| Device / workflow | From | What it is | Label |
|---|---|---|---|
| Split-first-frame + one visual per spoken phrase | @nateherkai (Nate Herk, ~350K) — Herk Edit Kit, MIT | First frame is ALREADY a split with the proof/tool on top; every spoken phrase gets its own visual; shots 1.1–1.4s, pauses <0.2s; self-correcting skill loop (every note becomes a permanent rule); caption contrast-check in a dark box | MEASURED (from his skill docs + reel summaries) |
| Per-line layout switching + real-screens-only | @johannships (reels-engine, MIT) | Layout changes on the spoken line; every graphic is a real screen or official logo, never stock/generated; hard QA gates on the final file; pacing learned from scraped winning reels | MEASURED (repo) |
| 5X outlier research feed | @personalbrandlaunch (Ava Yuergens, ~1.2M) — viral-outliers skill, MIT | Keep the swipe file fresh from reels beating their own account 5× (≥700K views AND ≥5× followers); frame-by-frame watch + fill-in-the-blank script template adapted to your brand | PUBLISHED (her skill) |
| 5-pass Claude reel edit | @zeeuiux (Zeeshan Ahmed) — free kit, no SPDX | Transcribe → cut-out → captions → motion → sound; one scene per idea fired on its trigger word; text-behind-subject cut-out; serif-italic key-word captions; −14 LUFS | PUBLISHED (his kit PDF + rules) |
| Remotion starter kit + style-file pattern | @ishaninit (Ishan Sachdeva) — MIT | Rules live in the skill (SKILL.md style file, read before every edit); captions/headlines/brand wipe/flash/end card | PUBLISHED (repo) |
| Talking-head pipeline with style learning | TakeOff-Team / claude-shortform-video-editor — MIT | Style learning from reference reels (yt-dlp); last-good-take cutting; dead space <0.1s; word captions; Remotion render; storyboard + QA | PUBLISHED (repo) |
| Long→short clipper with clip-scoring rubric | social-media-skills / video-to-shorts-skill — MIT | Clip rubric (hook, standalone, payoff); caption spec (Poppins ExtraBold 96px, ≤3 words, spoken word in accent colour); hook line burned in | PUBLISHED (repo) |
| 9-station production line + `watch` tool | manotsiris (Substack) — MIT (watch tool only) | Storyboard as the only human gate; `watch` tool (frame-by-frame reel watching + transcript) as the style-teaching loop; "reels orbiting behind my head" floating-mini-reel device | MEASURED (tool) / INFERRED (device, from summary) |
| Retention-dip re-edit rescue | @martinwang.mp4 (~220K) | Find the dip in the IG Insights retention graph, cut exactly that section in CapCut Edits, repost as Trial reel (case: 9.3K → 2.5M views) | INFERRED (from reel summary — confirm against the reel before building) |
| Lego-brick remix rule | content.game | 6 components (topic, angle, substance, format, hook, visual layout); remix rule — keep what works, improve everything else. Contains the documented Sky remix failure (47K vs 432K) and its cause | PUBLISHED (article) |
| CapCut mask-reveal graph | @editwith.paras (~29K) | Animated graph from CapCut shapes + masks + compound clips per element; mask-reveal = live data feed. Fallback D6 build when no real analytics screen exists | INFERRED (from tutorial summary) |

### BEAST MODE synthesis — best-of-space pipeline (grows as research lands)

The strongest of each layer, attributed, with measured evidence. The router
may draw on ANY of these; the fingerprint still gates every pick.

| Layer | Best right now | From | Evidence |
|---|---|---|---|
| Hook system | 5X outlier research + 7 hook types + 11 script structures | @personalbrandlaunch | 1.2M followers; Sky literally remade a video in her lineage |
| Motion set | Spring overshoot pops + Herk one-visual-per-phrase + Adilet whip/zoom-kick | Sky + @nateherkai + Adilet | Sky priority-15 verified; Herk 1.1–1.4s shots; Adilet 222 wpm beats |
| Caption system | Word-exact top strip (avatar) / bare bold 1–3 words (Sky lane) / style-switching designed captions (real takes) | Adilet (measured +0.013s) + Sky + Viashaan | Adilet 86-change measurement; Sky D1 verified; Viashaan demo A |
| Audio chain | Voice → cuts → speed → loudness −14.2 LUFS; SFX on every in/out | Adilet (measured) + Q's dense-sound standard | −14.19 / −14.16 LUFS measured on two Adilet reels |
| Self-review loop | Fresh reviewer counts WEAK moments on the export; ship only at 0 WEAK | Adilet (stage-5 prompt) + @johannships hard QA gates | Adilet SYSTEM.md; reels-engine QA gates |
| Research feed | 5X outlier feed (fresh winners weekly) | @personalbrandlaunch viral-outliers skill | Skill ships the feed as a runnable skill (MIT) |

### Batch-1 systems (decoded Nov 8, 2026 — full decodes: research/video-harvest/instagram/)

| Device / workflow | From | What it is | Label |
|---|---|---|---|
| Five content pillars (pillar-temple map) | @jayantcreates.ai (~39K) — 0→38K / 8M views in 4 months | Connect / Content Research / Hook skill (10 openings, ranked) / Humanizer / Trial Reels (5 versions, winner only); count-up proof open (432→38,000); 5th pillar "MOST EFFECTIVE" as the open loop; before/after humanizer with waveform | MEASURED (decode Dfb0YmHiDrD) |
| ENGINE — 5-agent team | @jlee.mov (~9K) — ~100→9,000 followers | Researcher (13 niche accounts ranked) / Scriptwriter (corrections saved as rules) / Editor (first cut 89.3s→68.8s) / Poster (trial reels) / Analyst (weekly table); persistent 5-agent roster with active card highlighted; correction→saved-rule card | MEASURED (decode DfZ0UHsBdoK) |
| Triple Hook Method | @kallawaymarketing (~225K) — carousel, 10 slides | Step 1 Context (immediate, audio+visuals+text aligned) / Step 2 The Lean (open the curiosity loop) / Step 3 Contrarian Snapback (fishing metaphor); "Say it. Show it. Write it." 3-channel slide; PWC remap: black→navy, red→gold (NO RED law) | PUBLISHED (caption verbatim) |
| Directing, not editing (thesis) | @viashaan (~39K) — "editing's turning into directing" | Conviction (positive illusions, Taylor & Brown 1988 paper full-frame) / experience (exact words → exact look: "ease in", "posterize at 12 fps") / taste (chef/salt/garlic, line diagrams); giant gold numerals 1/2/3 as section markers; honest aside held 1.6s on face | MEASURED (decode Dfcv027xJAD) |
| Agent-orchestra grid (17 at once) | @nategold.ai (~27K) — "Claude is editing 17 reels" | 17-card grid with progress % ("Your studio. In overdrive."); chin-in-hand reaction open; silent 10s teaser format; heaviest funnel ratio in the batch (1,626 likes / 5,669 comments) | MEASURED (decode DfU8iIAty_c) |
| Viral-idea finder (8 skills) | @createcontent.club (~439K) — "Claude can find viral ideas" | Topic → searches IG for competitors' viral reels → pulls hooks → saves liked ones to Notion; yellow bracket topic chips; competitor grid wall; Notion board payoff (Idea 1–10) | MEASURED (decode De9leuzlXJK) |
| Keyword-per-skill naming | @liamjohnston.ai (~114K) — Hook skill | One keyword per skill (Paid, WARM, Page, Sold, Find, Plan, Sort…); silent 3D showcase (orbiting phone mockups, glowing asterisk base, view chip) | MEASURED (decode De8I3VcjtKq) |

### IG Tier S — steal first (full index: research/claude-editing-creators/INDEX.md)

| Device / workflow | From | What it is | Label |
|---|---|---|---|
| Cut-list-first + storyboard gate | @kienobifilms (~460K) | "Cut every silence, every retake, keep my last take and show me the list first" → word-level cut list for approval → "break this into frames and write me a style guide" → storyboard before render → "turn this into a skill"; CLAUDE.md style memory; no DM gate | PUBLISHED (prompts verbatim) |
| 3-prompt chain (identity → brand kit → skill) | @thelifeoflibs (~300K) | Prompt 1 Who You Are / Prompt 2 Brand Kit (narrated CapCut screen-record as style transfer) / Prompt 3 Make It A Skill; fully on-screen, no gate | PUBLISHED (prompts verbatim) |
| 35 persistent rules + 19 named effects | @kingketo (~970K) — "The Claude Edit" | 8-step system; Rule 1 stutters 21.9s → 5.5s; 4:24 raw → 1:12 Reel; 13/13 self-check; music 31 dB under voice; real screenshots instead of typed metrics; skill file gated behind EDIT | PUBLISHED (rules as described) / GATED (skill file) |
| /build-style (think in the style, don't copy it) | @zachdoesai_ (~22K) | Paste skill link → "/build-style" + 3–5 reference Reels → frame-by-frame style-thinking → "/edit-video"; storyboard first, notes remembered, song saved as default music; public repo (not yet cloned/scanned — follow-up in his DECODE.md) | PUBLISHED (video) |
| /effects + /edit command catalogs | @patlaw (~20K) + @david_knowsai (~110K) + @v.i.s.h.ai (~339K) + @nishantchahar.ai (~237K) | Densest single-video effect catalogs (Vibha's skill, demonstrated): glass-widgets, orbit, spotlight, todo, timeline, match-cut, apple-toggles, kallaway-split, outfit-callouts, receipt, flip-sign, pegboard-billboard, tier-list, reel-replay, comment-pile | MEASURED (decodes) |

### Tier-A kits + repo Tier 1 (full indexes: research/free-claude-editing-kits/INDEX.md, research/repo-sites/INDEX.md)

| Device / workflow | From | What it is | Label |
|---|---|---|---|
| Herk Edit Kit (15 skills, 406 motion cards) | nateherkai/herk-edit-kit — MIT, 2,646★ | Most complete talking-head kit; transcript-driven cuts, HyperFrames motion cards; closest thing to a Sky-style end-to-end edit system | PUBLISHED (repo) |
| Ghost Editor (take in → reel out, 7 styles) | kurbaitaev/ghost-editor — MIT, 253★ | Face-safe captions; reverse-engineer-any-reference-edit (Q's "copy Sky" workflow) | PUBLISHED (repo) |
| ffmpeg-skill (42 FFmpeg tools + MCP + doctor) | kajisho5/ffmpeg-skill — MIT, 4,758★ | The workhorse layer; no keys, no cloud; ships as `npx ffmpeg-skill` | PUBLISHED (repo) |
| 15 filmed motion styles + prompts + source | mg-styles-15 — MIT, 3,261★ | A steal-able style library (films + prompts + full source; no SKILL.md in repo) | PUBLISHED (repo) |
| 192 named motion/camera/UI effects | motion-prompt — MIT, 1,391★ | Shared vocabulary for moves | PUBLISHED (repo) |
| Tella four (zooms / b-roll / clipify / cut-video) | louisedesadeleer — MIT, free | Punch-in zooms on stressed words; b-roll placed on the exact word; long video → vertical clips with speaker-following pans + word captions; no API keys | PUBLISHED (repos) |
| YouTube edit pipeline (8 skills) | hassancs91/claude-youtube-editor — MIT, 369★ | clean-cut, make-tsx (Remotion visuals synced to word times), clean-audio (free local RNNoise), suggest-sfx, packaging (title + 3 thumbs), yt_upload, brand-setup | PUBLISHED (repo) |
| Talking-head editor | griffinwooldridge/talking-head-editor — MIT | Q's core format as a pipeline | PUBLISHED (repo) |
| lemo-opuscar (51 film styles) | lemomo-ai/lemo-opuscar — MIT, 13,498★ | Biggest star count in the repo sweep | PUBLISHED (repo) |

### EMOTION layer (home: research/knowledge/EMOTION.md)

Emotion → edit device → sound → visual, 16 OBSERVED mappings (cited to video + timestamp) + 5 [GAP-FILL]. The layer that makes edits feel human, not AI. Top 3: **AWE/PROOF** — count-up under the claim (Jayant 0–5.7s); **TRUST/DIRECT ADDRESS** — look to camera held, proof in split panel/PiP, face never leaves (Viashaan, JLee whole reels); **CURIOSITY/OPEN LOOP** — name the payoff, withhold it, tag the withheld item (Jayant 15.4–19.1s). Full map in the file; part: `parts/knowledge-playbooks/emotion-mapping.md`. NO RED constraint applied throughout (anger = gold strike-through, dread = darkness + stillness).

### Kappa Batch-2 stack — v6 (decoded Nov 8, 2026; full drafts: research/video-harvest/instagram/kappa.ai_DecYkDcI799/PART-DRAFTS-V6.md)

| Device / workflow | From | What it is | Label |
|---|---|---|---|
| 5-tool Claude Code stack (HyperFrames + Whisper + CLAP + Demucs + Blender) | @kappa.ai DecYkDcI799 | One file self-installs the stack (Mac + Windows, local, no keys — their claim); each tool gives Claude one missing sense; Blender builds props free instead of generation credits (Higgsfield 1,240 / Midjourney 960 / Kling 1,080 / Blender 0). Loadout UI navy/orange in the reel — map orange → gold, keep navy | INFERRED (setup file GATED, never chased; licenses MEASURED) |
| CLAP audio understanding | LAION CLAP via @kappa.ai | Text↔audio retrieval over the licensed SFX library ("find me a whoosh like this one"); timeline QC — CLAP-label each SFX, flag mismatches; threshold ≥0.5 (his scores 0.51–0.87). LAION CLAP only — never M2D-CLAP (non-commercial) | MEASURED (license) / INFERRED (workflow) |
| Demucs stem separation | Meta HT Demucs v4 via @kappa.ai | Split a track into vocals/drums/bass/other (+6-stem variant); ~9.0–9.20 dB SDR; CPU-OK from 3GB VRAM. LICENSE FLAG: code MIT, weights research-use only (not covered by MIT; commercial use needs confirmation) — fold as workflow WITH the flag; input must be Q's own licensed audio | LICENSE FLAG (see part) |
| Drop-one-file install pattern | @kappa.ai EDIT funnel | One self-installing file + READY self-check beats a 6-step README; every extra install step loses funnel conversions. Apply to Q's own skills shipped to Claude | INFERRED |

### Stream-1 Tier S devices — v6 (BULK-DECODE-LOG.md Batches 1–6; 180 DECODE.md files so far)

| Device / workflow | From | What it is | Label |
|---|---|---|---|
| Titles-behind-head | @kienobifilms | Title passes BEHIND the speaker's head (matte-occluded) — depth, not a paste-on; 1–4 hero words/video; front captions yield during hero windows | PUBLISHED (decode) |
| Verbal-command catalog | @kingketo Dey8EwBgmnr / DfNi-KCCl1B | One plain-English sentence per device ("make X rotate around me", "add a wall of my photos behind me", "add B-roll over me talking") — the /effects pattern with no slash-command literacy needed | PUBLISHED (decode) |
| Batch CTA swap (53 videos) | @kylewhitrow DYxEl77Ef5M | One copy JSON + one preview HTML swaps the CTA across 53 videos at once; the keyword CTA is DATA, not baked pixels | PUBLISHED (decode) / INFERRED (rebuild) |
| Logo animation skill (10 in 30s) | @kylewhitrow DYuzPfjDt-r | The logo is a SKILL — pick the animation, don't re-animate it each time; logo outro ≤1s after last word | PUBLISHED (decode) |
| Batch preview-HTML feedback loop | @kylewhitrow DY2OL6zFP5E | 26-carousel batch rendered as one preview HTML; feedback against the preview, then one rebuild pass | PUBLISHED (decode) |
| 4-command pipeline (/clip /captions /storyboard /inspiration) | @zachdoesai_ Deo5YM4uq4L | Four slash commands, one job each, in order; /inspiration teaches itself from a linked finished video (Q's own videos only) | PUBLISHED (verbatim lines) |
| Setup prompt + reference→style guide | @aiwithrone Devt9LwPWrJ | Verbatim setup prompt ("You are my short form video editor… explain each step in plain English before you run it"); style guide = numbered step list from a reference video | PUBLISHED (verbatim) |
| Hookscore kill-gate (5 checks) | opusjake instagram-agent-skill — MIT, SCAN PASS | LENGTH 5–12 / SPECIFICITY / STAKES / FRONTLOAD / ADDRESS; overall = mean×0.6 + min×0.4 − 15×flags; STRONG ≥70 / OK ≥50; kills bad hooks, cannot crown winners (AUC 0.83 bad-vs-real, 0.56 hit-vs-miss) | PUBLISHED (repo) |
| Deadair gate (0.35s floor) | opusjake youtube-agent-skill — MIT, SCAN PASS | Automates Q's "no pauses, no air space" gate from a Whisper transcript; filler-only + retake cut list | PUBLISHED (repo) |
| AnimationBase review loop (sheet → strip → crop) | JohnHeibel/ClaudeAnimationBase — MIT, SCAN PASS | Reads-as-timing-sheet; transitions at every seam; beat-locked motion; boil + anti-twinning fixes. Do NOT import Clawd, the no-text rule, or the 16:9 canvas as-is | PUBLISHED (guide) / INFERRED (Q port) |
| Ghost-editor 7 vetted ports only | lemomo-ai/lemo-opuscar — MIT, SCAN FLAG stands | Caption News · News Package · Telestrator · Halftone Dossier · Swiss Grid · Data Story · Hologram HUD. Full repo NOT promoted (bare eval() in cel-anime-80s srt.py; os.environ['OUT'] in watercolor gen.py) | SCAN FLAG (full repo) |

### Stream-2 YouTube steals — v6 (PROMPT-PATTERNS.md §12–23; CLAUDE-CODE-WORKFLOWS.md §9–21)

| Device / workflow | From | What it is | Label |
|---|---|---|---|
| First-prompt architecture (13 items) | Grow with Alex 03BNd8ygnq8 | One job per file, exact branding, reference specificity, 5 basics, self-check, working rules, ask-for-more-than-a-reel; "preview only the part that changed" (verbatim, every prompt); Verdict/Fixes/Keep/Show-me feedback; "add rules, not effects" recovery | PUBLISHED (spoken system; skeleton INFERRED) |
| Skill-pack anatomy (rulebook + lookbook + reference folder) | Joseph Video Editing 7g9Qm1e00zU | 14 reference videos + 120+ image Figma board → rulebook + lookbook + ~200-animation reference folder; 5-key style spec; two trainings (visual + sound) + planning page with 4 scene types | PUBLISHED (training prompt verbatim) |
| Presets, not prompting + recursive self-review | Jason Cooperson 7MaARoS9o2s | Human-tuned presets folder; Claude PICKS presets, never invents motion; rough-cut loop + graphics plan/build/review loop before any human sees the cut; 2h42m + 740K context for 13 min (overnight run) | PUBLISHED |
| Motion-design skill repo | Aidan Stanik 7ixWO1SeEZo | SKILL.md + 8-step checklist + director/patterns/reference subfolders; clone-by-URL + HyperFrames Studio preview-before-rerender; 6–8 beats per 30s voiceover | PUBLISHED |
| Three-hook trial-reel factory + five-skill system | Emil Faschang 1VqdsBPGmcE | One recording → 3 trial reels (flat claim / question+claim / provocation); 5 skills (radar / research / reels / scheduling / analytics); report input time and machine time separately | PUBLISHED (numbers unverified) |

### Widened-net strategy devices — v6 (V6-WIDENED-NET.md; Tier S: Brock Johnson, Michelle Gifford, Patricia Streff, Shannon McKinstrie, Jayda Jones)

| Device / workflow | From | What it is | Label |
|---|---|---|---|
| InstaClubHub ritual model | @brock11johnson ~1.1M | Weekly trending-audio drops as a membership ritual; public growth scoreboard ("1,000/day"); 50,000+ members off IG alone. $7-trial door is a CONTRAST CASE only — Q is waitlist-only until Dec 7 [NEEDS Q'S WORD] | PUBLISHED (rituals) |
| 4 psychology levers | @viralbestiesclub — Jayda Jones ~52K | Polarizing stance, shared mythology, common enemy, emotional synchrony — verbatim from her reel; maps 1:1 onto Q's mechanics. Polarizing-stance hooks [NEEDS Q'S WORD] (clean/faith-aligned bar governs; the enemy is the IDEA, never a person) | PUBLISHED (verbatim) |
| RISE hook formula + 3-story daily | @shannonmckinstrie ~460K | RISE hook formula; 3-story daily (greet → promote → personal); "how I" > "how to" (30K followers from one hook edit); unpolished-reel doctrine; trial-reel testing. "How I" vs second-person house rule [NEEDS Q'S WORD] | PUBLISHED |
| One product, $97/mo, one community | @iammichellegifford ~450K | Closest Skool comp: same $97/mo, one community holding all products, Skool Platinum #55, MANGO → 7-day free trial; "one product instead of multiple launches" | PUBLISHED |
| 5-second profile test + positioning-first | @brazilian_momboss — Patricia Streff ~87K | 5-second profile test; "positioning problem, not growth problem"; student with 700 followers making $5K/mo; 2,000-student UGC mentorship | PUBLISHED |
| Martell opener→closer handoff | Dan Martell — Sell By Chat Playbook | Opener qualifies/warms, closer closes; pre-handle objections before the offer; spouse-objection row DRAFT [NEEDS Q'S WORD]; Closed Won/Lost review after every close | PUBLISHED (doc) |
| "Every month starts at zero" (NEW pain #3) | V6 widened-net re-rank | The one-off trap: brand deals as one-offs mean every month restarts at $0 — the pain is the RESTART, not the rate. NEW pain #8: agency-roster gap | PUBLISHED (knowledge file) |

### Flagged candidates — [NEEDS Q'S WORD] (v6, NOT adopted as parts)

| Candidate | From | Status | Why not adopted yet |
|---|---|---|---|
| Ten Fold "EDIT" prompt (PWC re-skin) | Ten Fold guide (PASS — verbatim prompt filed in research/prompts/full-prompts/tenfold-edit-prompt.md) | [NEEDS Q'S WORD] | Most Q-compatible prompt in the harvest (face rule identical to Q's brand law; FIND MY FACE pre-build check; "illustrate the sentence" = Q's show-it rule). Adoption = PWC re-skin + Q's freeze/lip-sync/retention gates — Q's call. |
| Ansh skill-template system (frame.md + design.md) | @thecuttingedge.school — Ansh Mehra ~140K | [NEEDS Q'S WORD] | Fix the template once, replicate every video in that style; closest published description of how HyperFrames templatizes a look. Part candidate creator-systems/ansh-skill-template-system.md — coordinator to approve + build. |
| Kapwing `learn my style` → layout-guide.md | Kapwing /shorts-editor skill | BLOCKED — zip + license | Zip NOT retrieved (download button href not exposed in any text crawl; no GitHub mirror); license UNKNOWN. Needs a browser click or Q downloading it himself → quarantine → SAFETY scan → license confirm. Mechanism only distilled in research/repo-sites/kapwing-shorts-editor/DISTILLED.md. |
| MalikMuzamil weekly pipeline prompt | MalikMuzamil 13-tool pipeline guide (PASS with KEY-GATED flag) | [NEEDS Q'S WORD] | Inventory → strategy → edit → animate → export → repurpose, stop-and-ask before every file-changing stage; already includes the comment-keyword CTA step + brand-colors slot. video-use needs an ElevenLabs API key (Q enters his own key only; Whisper is the free alternative). |

### Rundown v7 — design-system v7 + effects v3 (RUNDOWN-A-MANIFEST.md + RUNDOWN-B-MANIFEST.md + tenfoldmarc RABBIT-HOLE-MANIFEST.md, Nov 8, 2026; 43 new parts → 177 total; QC status PENDING for every profile — Claude's implementation + Muse's QC can only run after the parent uploads the staged zips)

| Profile | Drafts folded | Parts | Label |
|---|---|---|---|
| @david_knowsai (~116K, UNVERIFIED single source) | 4 drafts + 2 variants | `parts/effects/effects-pull-apart-breakdown.md`, `effects-self-building-chart.md`, `effects-journey-map-route.md`, `effects-dots-and-bars-graphics.md`; variants /zach-d-films → effects-orbit, /stick-figure → effects-doodle-boil | INFERRED (6 animation skills GATED behind ANIMATE, never chased) |
| @jayantcreates.ai (~38.8K, UNVERIFIED) | 6 drafts + 3 variants | `parts/creator-systems/jayant-sunday-learn-loop.md`, `jayant-machine-doctrine.md`, `ootto-virality-hook-doctor.md`, `ootto-reel-analyzer.md`, `ootto-hook-mining.md`, `ootto-content-factory.md`, `ootto-going-viral-strategy.md`, `ootto-content-skills-index.md`; variants → batch1-jayant-pillars | PUBLISHED (Ootto repo MIT, SCAN PASS) / INFERRED (DM-gated skills, never chased) |
| @jlee.mov (9,391) | 4 drafts + 2 variants | `parts/creator-systems/jlee-reviewer-claude.md`, `jlee-correction-rule-loop.md`, `jlee-page-per-job-chain.md`, `jlee-research-split.md`; variants → batch1-jlee-engine, batch1-jayant-pillars | INFERRED (gists license-unclear — reconstruction only, no verbatim code) |
| @kallawaymarketing (225,440) | 6 drafts + 4 variants | `parts/creator-systems/kallaway-desire-hook.md`, `kallaway-hook-power-words.md`, `kallaway-illusion-of-novelty.md`, `kallaway-format-finder.md`, `kallaway-analyze-batch.md`, `kallaway-collections-taxonomy.md`; variants → batch1-kallaway-triple-hook | PUBLISHED (steps) / INFERRED (templates/skills GATED, never chased; sandcastles.ai plugin NOT adopted) |
| @viashaan (39,347) | 0 drafts — already installed | No new parts; the LOOK is a standing non-transfer (Q rejected it for main edits Nov 7, 2026); the directing thesis + installed systems transfer | — |
| @nategold.ai (~27K) | 5 drafts + 2 variants | `parts/creator-systems/nategold-instagram-agent.md`, `nategold-creatorcut-reference-first.md`, `nategold-ig-profile-audit.md`, `parts/hooks/hooks-hookscore-26-formulas.md`, `parts/strategy/strategy-outlier-multiple-swipe.md`, `parts/captions/captions-ig-humanizer.md` | PUBLISHED (instagram-agent repo MIT, SCAN PASS) / INFERRED (CreatorCut app GATED) / UNVERIFIED ("100 reels at once" — never present as verified) |
| @liamjohnston.ai (114,213) | 3 drafts + 3 variants | `parts/creator-systems/liam-hook-master-suite.md`, `liam-remotion-command-catalog.md`, `parts/hooks/hooks-jev-hook-bank.md`; variant → skill-pack-anatomy | PUBLISHED (hook-master repo MIT, SCAN PASS) / INFERRED (Jev + Remotion stack GATED; Jev IG-connect NEEDS Q'S WORD) |
| @createcontent.club (439,524) | 3 drafts + 3 variants | `parts/creator-systems/ccc-content-strategy-skill.md`, `ccc-script-to-stories.md`, `parts/strategy/strategy-dashboard-carousel.md` | INFERRED (all 8 skills GATED, never chased; dashboard slides NOT frame-verified) |
| @kappa.ai (~1.9–2.1K, UNVERIFIED live) | 0 new parts + 5 variants | Variants → kappa-5-tool-stack (count-up behind head, floating keyword pills, self-proof line, MCP note), pipeline-drop-one-file-install (DM-delivery mock) | INFERRED (setup file GATED, never chased) |
| @tenfoldmarc / Marc Cleroux (125,234 VERIFIED, two live sources) | 9 parts + 3 variants (drafted from manifest — no PART-DRAFTS file existed) | `parts/effects/effects-couch-wall.md`, `effects-cover-story.md`, `parts/creator-systems/tenfoldmarc-spy-pipeline.md`, `tenfoldmarc-hooks-skill.md`, `tenfoldmarc-3-hook-trial-reels.md`, `tenfoldmarc-video-edit-3-looks.md`, `tenfoldmarc-reaction-recreate.md`, `tenfoldmarc-comment-thread-closer.md`, `tenfoldmarc-content-machine.md`; variants chart-grow → effects-self-building-chart, glass-type → effects-glass-widgets, checklist → effects-todo-checklist | INFERRED (specs from public reel/guide); video-edit-skill / spy-skill / hooks-skill CODE PARKED (no LICENSE file — SAFETY §7); 46-effect pack's 30 ungated-shown effects GATED, never chased |
| @coursecreator360 / Stockton Walbeck (78,230) | 0 new in v7 (v6) | v6 parts stand (15 effects + pipeline-stockton-one-prompt-render); Split Stage PARTIALLY VERIFIED (see COVERAGE.md GAP list) | INFERRED |

### Rundown v8 — design-system v8 + effects v4 (Batch 5 Bradford Marais + Batch 6 Create Content Club + Batch 7 Jack Roberts + Tier S seed, Nov 8, 2026; 20 new parts → 197 total; NEW Category 20 SCRIPTWRITING; QC status PENDING for every profile — Claude's implementation + Muse's QC can only run after the parent uploads the staged zips)

| Profile | Drafts folded | Parts | Label |
|---|---|---|---|
| @bradfordmarais (~? — follower count not in the Batch 5 teardown; do not cite one) | 5 drafts | `parts/scriptwriting/content-architecture.md`, `brand-brain.md`, `script-structures.md`, `quality-gate.md`, `contrast-device.md` | INFERRED (Nova system GATED behind NOVA → DM, never chased; 12 structure names INFERRED, his real 12 ungated-unknown; 95-gate threshold, third-party connections, 12-structure count, 1,000-hook target all [NEEDS Q'S WORD]) |
| @createcontent.club (439,524) | 2 drafts + 5 variants + 9 GAPs (Batch 6) | `parts/scriptwriting/viral-rewrite-skill.md`, `parts/creator-systems/ccc-script-to-carousel.md`; variants: 40-skills list device (needs Q's result lines), mark-ready-to-post trigger → one-stack doctrine, per-platform captions → mirroring rule, pace question + cut report → QC reporting, outlier-score table → strategy-outlier-multiple-swipe | INFERRED (all 8 AI content skills GATED behind SKILL → DM, never chased; CLICK automation + resolve-claude-mcp GATED, NOT adopted; flipped-trial dodge [NEEDS Q'S WORD]; outperformance ≥2x median INFERRED [NEEDS Q'S WORD]) |
| @jackroberts___ (Batch 7) | 7 drafts + 5 adopted patterns + 5 PARKED + 8 GAPs | `parts/knowledge-playbooks/find-skills-discovery-layer.md`, `claude-mods-watcher-handoff.md`, `review-mining-rebuild.md`, `dev-team-skills-subagents.md`, `parts/creator-systems/claw-machine-picker.md`, `parts/prompts/deeper-expert-prompt.md`, `parts/effects/kitchen-tactile-ui.md`; SAFETY.md §9 (dual-model review); KNOWLEDGE-INDEX.md v8 (HyperFrames ranking evidence) | INFERRED (find-skills skill itself ranked #1 at 3.7M on the same reel — the discovery layer is the SPEC, not the skill; vercel-labs/skills, affaan-m/ECC, Replica skill repo, Atticus, Kitchen site link all PARKED/gated, never chased; dual-model pair + discovery-layer scope + Replica/Atticus scope [NEEDS Q'S WORD]) |
| Tier S seed — @charliehills, @mehganjames, @ibravisual, @kingketo (doctrine) | 5 drafts | `parts/creator-systems/skill-doctrine-save-it-as-a-skill.md`, `charliehills-27-things-os.md`, `mehganjames-5-pass-method.md`, `ibravisual-slash-command-pack.md`, `parts/strategy/self-check-95-gate.md` | PUBLISHED where shown / INFERRED (command FILE content not in harvest — names + one-line jobs only; 61-effect names unknown, do NOT invent; /faceless "4 ADD-ONS" unnamed; 95-gate threshold [NEEDS Q'S WORD]; "MUSIC GOES QUIET WHEN YOU TALK" ducking rule [NEEDS Q'S WORD]) |
| Self-learning partials (Stream 5 leftovers, v8) | 5 partials resolved | SL-01 cross-ref → `parts/creator-systems/sky.md`; SL-02 marching-dash + glowing-head variants → `parts/motion/motion-named-8.md` (variants, not new parts — grammar already covers draw-on/pulse/track); SL-05 door-free transition table → `parts/motion/motion-beat-rhythm.md`; SL-14 loudness/clipping check → `parts/render-pipelines/pipeline-qc-gates.md`; SL-31 canonical-reference inventory → `parts/creator-systems/canonical-reference-inventory.md` (DfVDRnyDnop, DfSeabAjxMA, DfP5qYEj67L, DfKpWJOE6r6, DfItZkHE1JJ; supersession Nov 5, 2026) | MEASURED (Q's words + repost measurements) |

### Rundown v9 — design-system v9 + effects v5 (bulk harvest row-level adoption + YouTube/widened net + knowledge verification, Nov 8, 2026; 64 new parts → 261 total; QC status PENDING for every profile — Claude's implementation + Muse's QC can only run after the parent uploads the staged zips)

| Group | Drafts folded | Parts | Label |
|---|---|---|---|
| Bulk A (188 decodes) | 18 drafts → 17 parts (charliehills-27-things-one-brain deduped onto charliehills-27-things-os) | `parts/creator-systems/agents-md-onboarding.md`, `agi-point-4-step-editor-build.md`, `buildwithdarius-real-editor-pipeline.md`, `charliehills-graphic-designer-6-step.md`, `charliehills-mac-setup-8-step.md`, `claude-eyes-watch.md`, `davis-ai-brain-project.md`, `davis-build-stack-10-tools.md`, `davis-operator-os-vault.md`, `doctablademd-find-your-number.md`, `doctablademd-reel-room-5-step.md`, `ibravisual-jarvis-4-part-build.md`, `page-audit-agent.md`, `two-skill-director-model.md`, `parts/effects/effects-xray-body-track.md`, `charliehills-21-effect-catalog.md`, `parts/render-pipelines/pipeline-review-dashboard-timestamped.md` | PUBLISHED where shown / INFERRED (skills + guides behind DM/comment funnels stay GATED, never chased; 55 IMPLEMENTED / 99 STAGED / 34 GAP rows in v9_adoption_bulk_a.md) |
| Bulk B (188 decodes) | 13 drafts → 13 parts | `parts/creator-systems/cowork-record-a-skill.md`, `ibravisual-security-checks.md`, `ibraviz-brand-interview-prompt.md`, `itsflxkzy-mcp-five.md`, `kingketo-claude-edit-8-step.md`, `kylewhitrow-batch-cta-swap.md`, `kylewhitrow-carousel-batch-preview.md`, `leonpetrou-toggle-edit-menu.md`, `mds-word-anchored-edit.md`, `parts/effects/effects-finger-gun-pop.md`, `effects-logo-sting-variants.md`, `parts/render-pipelines/pipeline-reasons-edl-render.md`, `parts/prompts/prompts-kimanidigital-edit-brief.md` | PUBLISHED where shown / INFERRED (105 IMPLEMENTED / 71 STAGED / 12 GAP rows in v9_adoption_bulk_b.md; YTDLP flagged, not adopted; auto-posting conflicts with Q's approval doctrine) |
| Bulk C (188 decodes) | 18 drafts → 18 parts | `parts/creator-systems/creator-systems-viral-radar.md`, `director-taste-doctrine.md`, `jev-decider-router.md`, `skill-template-frame-design.md`, `three-run-planner.md`, `parts/effects/effects-code-component-library.md`, `effects-hologram-book.md`, `effects-outfit-callout.md`, `effects-slot-machine.md`, `parts/render-pipelines/pipeline-goldfish-review.md`, `pipeline-watch-folder-auto-edit.md`, `parts/prompts/prompts-clock-starter.md`, `prompts-one-sentence-brief.md`, `prompts-research-codes.md`, `prompts-rules-not-vibes.md`, `prompts-study-progress-card.md`, `prompts-taste-files-slot-style.md`, `prompts-word-timed-graphics-prompt.md` | PUBLISHED where shown / INFERRED (129 IMPLEMENTED / 51 STAGED / 8 GAP rows in v9_adoption_bulk_c.md; Higgsfield + paid products never bought; third-party code/connectors not downloaded or scanned) |
| YouTube + widened net (59 decodes; 105 profiles) | 16 drafts (D1–D15) + D16 comment-pile | `parts/render-pipelines/beat-table-contact-sheet.md`, `capcut-native-file-edit.md`, `ccms-four-pass.md`, `claude-file-tricks-lut-srt.md`, `hyperframes-clock-ban-check.md`, `measure-dont-opine.md`, `model-split-cost-rules.md`, `review-checklist-six-mistakes.md`, `seven-stage-pipeline.md`, `two-factories-motion-plates.md`, `parts/creator-systems/competitor-scrape-pipeline.md`, `monthly-outlier-review-loop.md`, `seven-jobs-org-chart.md`, `trial-reel-test-spec.md`, `parts/effects/effects-comment-pile.md`, `parts/scriptwriting/interview-outline-skill.md` | PUBLISHED where shown / INFERRED (24 YT GAP entries; computer-use PARKED like Atticus; Zapier MCP GAP V8-182 — needs Q's word; widened-net ~70 GAP rows, mostly §C2 deeper-pull flags) |
| Knowledge verification (182 V8 entries) | 109 → drafts, 66 → variants, 4 COVERED, 1 GAP, 1 SAFETY NOTE, 1 CAPABILITY NOTE | Playbooks ship as text pieces (`pwc-knowledge-editing.zip`, `pwc-knowledge-strategy.zip`); full disposition in `research/knowledge/v9_verification.md` | MEASURED (all 182 V8 IDs verified present as `### V8-NN` headings in `research/knowledge/*.md`; literal grep of V8 IDs in `parts/` returns 0/182 — the v8 fold lived in the playbooks, and v9 makes the playbooks themselves land) |
| Self-learning check-in (Nov 8, 2026) | 0 new drafts | v8 fold verified 45/45 (38 SL + 7 PB present, 4 FL correctly absent); no new lessons, no new conflicts | MEASURED (`parts-staging/self-learning/V9-CHECKIN-2026-11-08.md`) |

## Caption components (home: pwc-designed-captions)

| Component | Spec | Motion |
|---|---|---|
| BASE karaoke | Poppins ExtraBold, white, spoken word → gold, navy stroke 5 | STEPS word ticks |
| SCRIPT_ACCENT | Playfair Bold Italic, gold #FEE238, single word | EASE OUT rise |
| GLOW | Poppins ExtraBold white + teal #14A886 bloom (blur 18) | EASE IN-OUT |
| BIG_CAPS | Anton, white, section claim line | OVERSHOOT 92→103→100 |
| CHUNKY_ITALIC | Poppins ExtraBold Italic, white | SPRING settle |
| HERO_BEHIND | Anton ~320px, white, behind layer (matte sandwich) | EASE OUT in / EASE IN out |

## Animation components (home: pwc-animations/templates)

| Component | DATA contract | Motion signature |
|---|---|---|
| stat-chart | title, value, prefix/suffix, sub, points[] | draw EASE IN-OUT, count STEPS+EASE OUT, dot OVERSHOOT |
| map-route | from, to | route EASE IN-OUT, pin OVERSHOOT drop |
| headline | masthead, date, headlineLines[], byline | lines EASE OUT stagger, bars STEPS |
| teardown | titleA/B, layers[4]{name, note} | spread EASE OUT, tags SPRING stagger 5f |
| paper-desk | papers[3]{title, lines[], x, y, rot} | land OVERSHOOT, writing STEPS, underline EASE OUT |
| ink-wash | title, sub | all slow EASE IN-OUT |

## Effects library (home: effects skill — @vibha.in.progress's claude-video-effects)

51 face-tracked effects invoked as `/effects <name>`; the registered
PWC-first set: backdrop-word (= HERO_BEHIND's ready-made twin), orbit,
carousel-spin, phone-fan, profile-wall, place-in-grid, comment-box,
tap (follow button), todo, checklist, liquid-glass-graph, locked-on,
lean-in, spotlight, led-sign, tape-label (yellow tape — native PWC gold),
countdown-flip, wave-trim, messages, scribble, pause-point, the-bill
(receipt), split-headline, headline-wall, headline-box, broll-split,
swipe, moody grade, slow-push. RED-LAW REMAP: reject-stamp, red-collage,
crayon-write, huge-strike and timeline ship red in the library — in PWC
use they render GOLD (stamp, word, crayon, strike line) or are skipped.
Effects carry no sound/captions — PWC sound + caption systems layer on top.

## Edit components (home: pwc-video-editors / lane builders)

| Component | Spec |
|---|---|
| Brand pill | compact navy pill, teal border, PWC wordmark — top area, inside safe zone |
| Hook title | big two-tone (white + gold key word), above head, never over face |
| Comment card | IG-style comment card carrying the keyword CTA |
| Inventory cards | ✗/✓ rows, navy cards, gold checks — rows stagger 4–6f with layered sounds |
| Numbered steps card | Anton numerals in gold circles, rows build as he lists |
| REC frame | viewfinder corners + red-dot substitute = GOLD dot (no red rule) + "REC" label |
| Scripture card | flat navy serif plaque, Playfair text, gold reference line |
| Giant number pop | Anton gold numeral, OVERSHOOT landing, count-up where spoken |
| Yellow pill | gold #FEE238 pill, navy text — CTA and payoff chips |
| Count-up card | navy card, Anton number counting in STEPS+EASE OUT to the spoken figure |
| Notification cards | phone-style cards sliding EASE OUT, stacked with 4–6f stagger |
| Strike-through payoff | line draws EASE IN-OUT across the old claim as the new one lands |
| Logo outro | PWC logo card, ≤1s after last spoken word (dead-air gate) |

## Adilet system (home: adilet_system/ + skills' adilet/ subfolders)

The decoded @adilet.fndr production system (59-post teardown, Nov 5,
2026) — the avatar lane's governing method. Pipeline components, each
registered once and reused: hook patterns (HOOKS.md: LAWSUIT / GATE /
METER / EVERYONE'S-DOING-IT / NUMBER SHOCK / CONFESSION / SYSTEM TEASE) ·
beat pacing 1.5–3.5s, pose swap 1–2s (PACING.md) · motion presets
SPRING / STAMP SLAM (gold for PWC) / WHIP PAN / ZOOM KICK 1.6× on
graphics / COUNT-UP (MOTION.md) · word-exact captions, 0.00s lead
measured (CAPTIONS.md) · audio chain generate → cuts → native speed →
−14 LUFS (AUDIO.md) · stage components: subject-file card, exhibit card,
diagram cards, count-up card, stamp, terminal card, wall-of-proof,
pose library (ILLUSTRATION.md) · self-review "WEAK count → 0" gate
(PROMPTS.md stage 5).

## Cover components

| Component | Spec |
|---|---|
| Locked cover template | designer cover, handle corrected to navy pill "@yerrr__q", 12px top / 10px bottom crop, 1080×1920 |
| Thumbnail text | bold condensed uppercase, gold/white on the shot, face clear |

## Registration format (for new components)

`name | home (skill + file) | one-line spec | motion signature | first used (video/date)`

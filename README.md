# claude-editing — Q's ONE main work folder for all Claude editing

> **THE NORTH STAR:** Claude with infinite space, infinite knowledge, and
> the ability to learn — so Q's edits are so sharp and on point people
> can't believe it's AI.
> - **Infinite space / infinite knowledge** = the modular library
>   (`parts/`, 19 categories, 177 parts) + the GitHub pull route
>   (`github-repo/`) + the weekly learning sweep + the uploads inbox: the
>   knowledge base grows without a ceiling because it's organized in small
>   parts across multiple delivery paths, not one capped skill. The
>   INDEX/CATEGORIES map is what makes "infinite" usable — Claude can
>   always find the right part.
> - **Ability to learn** = the continuous-learning loop (weekly sweep +
>   per-video harvest + Q's own uploads via INBOX) is a permanent feature,
>   not a one-time build — see CONTINUOUS-LEARNING.md.
> - **People can't believe it's AI** = the HUMAN-MADE quality bar (Q's
>   standing @rpn rule: "don't make it look ai made at all, make me wanna
>   know how I did it"). The HUMAN-MADE CHECK is a final QC gate in the
>   router and in every skill — a render that reads "template" fails even
>   if it's technically correct.
>
> Judge every future addition against the vision: does it make Claude know
> more, learn faster, and edit more human?

## NO-LIMITS vs NON-NEGOTIABLES (Q, Nov 8 — "remove all restrictions to itself to reach its highest potential")

**NO-LIMITS (growth — removed):**
- No cap on what Claude learns: every style, every system, every prompt,
  every code, every creator, every domain (editing, strategy, psychology,
  sales, coaching). No "that's enough" ceiling.
- No holding back on ambition: the goal is the best in the world at each
  aspect, then better. Sky is the benchmark to BEAT, not just match.
- No artificial scope walls between specialties: the motion specialist
  learns from the strategist, the caption specialist learns from the
  psychologist — cross-pollination is the default.
- No fear of scale: the library grows without a ceiling (modular parts +
  GitHub pull + weekly sweep + self-learning). If a part gets big, split
  it — never shrink the ambition to fit a limit.
- Operating stance, written into the design-system SKILL.md + AGENTS.md:
  "Pursue the highest potential in every aspect. Learn everything. Master
  everything. Improve on everything."

**NON-NEGOTIABLES (identity + safety — these are what make it HIS and
SAFE, not limits on potential):**
- Brand DNA: nothing over Q's face, teal/gold on navy, NO RED, PWC skin,
  logo, human-made check. Removing these would make the output generic,
  not better.
- Safety protocol (SAFETY.md): quarantine, code scan, no credentials, no
  scams/phishing, only public freely-licensed material.
- Licensing rules: no paywalled/piracy content; license-flagged kits need
  Q's word.
- Q's standing rules: blur law, hidden app never named, newest-version
  posting, keyword flows live before posting.
- Claude's own platform safety policies are Anthropic's, not ours — we do
  not instruct bypassing them, and the build never asks Claude to.

Judge every future addition against the split: does it raise the ceiling
(NO-LIMITS — do it) or does it touch identity/safety (NON-NEGOTIABLES —
stop)?

## The double-growth loop — Muse works BESIDE Claude (Q, Nov 8)

**Muse + Claude work together as masterminds across the whole game, not
just cuts. Muse works BESIDE Claude, in parallel, so the system grows
twice as fast:**

- **Muse harvests while Claude builds** — Muse pulls new videos, prompts,
  kits, creators, and pain-point signals; Claude keeps editing with
  what's already in its knowledge. Neither waits on the other.
- **Muse verifies what Claude makes** — every Claude render gets Muse's
  QC pass (the standing gates: freeze check, face clearance, lip-sync,
  brand-DNA, human-made) before it reaches Q; failures go back to Claude
  with the exact fix, and the fix becomes a new rule in the library.
- **Muse teaches, Claude practices** — each new distilled part Muse
  stages is a lesson; Claude applies it on the next real video, and the
  result (what worked, what missed) is logged back into the library as a
  worked example.
- **Two memories, one brain** — Muse keeps the master library + coverage
  map; Claude carries the distilled skills. The weekly sweep is the sync
  point: Muse brings the week's new learning, stages it, and (via the
  parent's uploads) it lands in Claude.
- **The loop compounds:** find → distill → stage → upload → Claude
  applies → Muse verifies → correction becomes a rule → find more. Each
  cycle makes both faster. The goal Q stated: double the growth rate —
  measured in the weekly report (parts added, skills updated, renders
  QC-passed, corrections folded back).

**Division of labor:** Muse harvests, researches, verifies, and stages
(the library builder); Claude executes, builds, and renders (the
editor). The shared library in `~/workspace/claude-editing/` is the
common brain — both work from the same parts, categories, and router.
The Master orchestrator's job now covers both editing AND strategy: for
any video or post, it picks the edit AND the strategic angle (hook
psychology, CTA, pain point addressed, conversion path) — see
`design-system/AGENTS.md` (16 specialists: 11 editing + 5 strategy).

Every asset, code file, skill, editor, example, meme, GIF, and research note
that Claude (and Muse) use to edit Q's videos lives here, in one place.
If it's part of how a PWC video gets made, it lives here or is registered
in INDEX.md with its location.

## Map

| Folder | What lives here |
|---|---|
| `skills/` | Claude skill SOURCES (the folders that get zipped + uploaded): pwc-designed-captions, pwc-animations, pwc-design-system, adilet-system, effects, realskytan-system, pwc-motion-playbooks |
| `editors/` | The two editor skills: pwc-video-editors (v16) + pwc-avatar-video (v3) — full sources |
| `design-system/` | THE STACK (live repo): MUSE.md, BRAND.md, WORKFLOW.md, COMPONENTS.md, templates, tests + EDIT-ROUTER.md + BRAND-DNA.md + PROMPTS.md + KNOWLEDGE-INDEX.md + AGENTS.md (mastermind) + SKY-SCORE.md (Sky-beating loop) + CATEGORIES.md |
| `parts/` | **The modular library: 177 parts in 19 categories** (hooks, captions, motion, easing-physics, camera-moves, imagery, color-grade, audio-sound, render-pipelines, prompts, creator-systems, knowledge-playbooks, effects, strategy, audience-psychology, sales-closing, creator-pain-points, trends, gap-fills). Each part: rule + executable steps + worked example + attribution. Generated by `code/build_parts.py`. See CATEGORIES.md. |
| `research/knowledge/` | The knowledge playbooks + the strategy layer: MOTION-PHYSICS, EASING, CAMERA-MOVES, IMAGERY, CAPTION-SYSTEMS, COLOR-GRADE, SOUND-DESIGN, RENDER-PIPELINES, CLAUDE-CODE-WORKFLOWS, PROMPT-PATTERNS, GESTURES-MOVEMENTS (visual-language vocabulary), AUDIENCE-PSYCHOLOGY, SALES-CLOSING, CREATOR-PAIN-POINTS (top 10, ranked), TRENDS (what's working now) |
| `github-repo/` | **Push-ready GitHub staging tree** (parts + design-system + skill sources + operating docs, 152 files, 6.2 MB — no videos/zips/node_modules). Push is the parent's step — see `github-repo/PUSH-README.md` (repo name + visibility to confirm with Q). |
| `examples/` | sky/ (Sky video + carousel examples, motion teardown), adilet/ (all 59 reels + breakdown), viashaan/ (4 reference reels + demos), reference-reels/ (other creators) |
| `assets/` | fonts/ (real files), memes/ + gifs/ (refs + registry — the 6.7 GB library stays in your_files/for-claude-assets), sfx/, images/, covers/ (registries) |
| `code/` | Pipelines + helpers: skill_zips_build.py (zip builder + verifier, 7 jobs), build_parts.py (parts generator, 177 parts), package_all.sh (legacy), sync_gate.py, batch_strips.py |
| `research/` | caption-skill-research, sky-edit-skills (Nov 7 shortlist), adilet-teardown, sky-like-creators/, free-claude-editing-kits/, claude-editing-creators/, knowledge-harvest/ + knowledge/, repo-sites/, prompts/, video-harvest/ |
| `uploads/INBOX/` | **Q drops new examples/code here.** See UPLOAD-RULES.md |
| `uploads/QUARANTINE/` | **Every new download lands here first** (SAFETY.md) — nothing moves to skills/code/zips until it passes review + scan. |
| `zips/` | Upload-ready Claude skill zips (verified: ≤200 files, ≤30MB, no nested .zip) + UPLOAD-ORDER.md + COVERAGE.md |
| `archives/` | Superseded v2-era skill sources/zips (kept, not live) |

## Rules of the house (hard, Q's standing orders)

- **Nothing over Q's face. Ever.** Captions/devices live in empty space above his head.
- **Palette: teal #14A886 + gold #FEE238 on navy #00214E. NO RED.** Any reference's red maps to gold.
- **Sky Protocol is supreme:** Sky's edits AND carousels copied to a T; only Q's assets, logo, and brand colors change.
- **CapCut-native motion.** Renderer-built plates never substitute for CapCut motion.
- **Full self-watch before delivery.** Every final file gets watched end-to-end (freeze/transition/face/safe-zone/retention/truth gates).
- **HUMAN-MADE CHECK (final gate).** A render that reads "template" fails even if it's technically correct — no uniform rhythm, caption treatments vary, transitions motivated, examples real, sound dense but organic, nothing frozen or stamped. "A viewer would ask how I did it" or FAIL.
- **Post the exact exported file** with Muse's SEO caption; no re-encode, no compression.
- **Real, not AI-flat.** Imagery is real footage/photos/screenshots; illustrations follow the Adilet grammar.

## How to use it

- **Editing a video (Claude):** load `design-system/` first (EDIT-ROUTER.md picks the
  edit), then the lane skill from `skills/` or `editors/`.
- **Adding a new example/code:** drop it in `uploads/INBOX/` (see UPLOAD-RULES.md).
  It gets vetted, filed into `examples/` / `skills/` / `research/`, folded into
  the design system, and re-uploaded to Claude as a new skill version.
- **Rebuilding zips:** `python3 code/skill_zips_build.py` (verifies all four
  core zips). Editors/avatar zips are built from `editors/` the same way.
- **Old paths still work:** every moved folder has a compat symlink at its old
  `~/workspace/<name>` location, so old crons and scripts keep running.

## Where things used to live

See INDEX.md — every item registered with old path → new path, plus the
big trees that were deliberately NOT moved (claude_avatar_posts 6.7 GB,
edit_pilot_work 11 GB, your_files/, goals/) and why.

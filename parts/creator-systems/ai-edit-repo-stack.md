<!-- PART: creator-systems/ai-edit-repo-stack.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# CREATOR SYSTEM — The 4-Repo AI Edit Stack (Herk / OpenFilm / OpenMontage / HyperFrames)

Source: Mariah Brunner (@itsmariahbrunner, "AI with Mariah") reel DfmlI5sNFVa,
43s, decoded Nov 11, 2026 (Batch 33) — "4 free Github repos for editing videos
with AI." Full decode: `research/video-harvest/instagram/batch-33-repo-stack/DECODE.md`.
Every repo below was identified from the reel's own audio + verified live on
GitHub (stars/license read Nov 11, 2026). Her download links are comment-gated
behind "comment FOUR" — NOT chased; identification used public sources only.

## Claim check (hers, verified)
"Over 158,000 stars combined" — TRUE, and now understated:
Herk 2,746 + OpenFilm 5,762 + OpenMontage 79,603 + HyperFrames 82,639
= **170,750 stars** (Nov 11, 2026). All four are free to use; licenses differ
and the license is what decides Q's status for each (see cards).

## The routing table (her tree, completed with Q's stack)
| Job | Use | Q status |
|---|---|---|
| Talking-head end-to-end system (cuts, captions, visuals) | **Herk Edit Kit** | OWNED — Tier A |
| AI assembles the edit, YOU hand-fix it on a visual timeline | **OpenFilm Studio** | MIT, vetted, INSTALLED Nov 11 |
| Long recordings → short clips, broad production pipelines | OpenMontage | **PARKED — AGPL, Q's rule** |
| Custom animations, titles, motion graphics | **HyperFrames** | OWNED |
| Word-level FFmpeg operations underneath everything | ffmpeg-skill | OWNED — Tier A workhorse |
| Reverse-engineer / copy a reference edit | ghost-editor | OWNED — Tier A |
| Any Sky lane, final finish | **CapCut-native** (house law) | Always |

## Card 1 — HERK EDIT KIT (talking head) — OWNED
- Repo: `nateherkai/herk-edit-kit` — 2,746★. License: the LICENSE file reads
  MIT (GitHub's API shows NOASSERTION = unclassified; the file governs —
  verified during the Nov 8 kits sweep).
- What it is: 15 skills + 406 motion-graphics cards, house style MEASURED
  from Nate Herk's 27 top reels. Transcript-driven cuts: pause cutting,
  mistake review, captions, building visuals — the reel's exact list.
- Engine note: Herk's cards run on **HyperFrames** templates — the reel's
  "HyperFrames is already used by creators like Herk" line is literal.
- Q's status: Tier-A adopted (parts `herk.md` + `kit-repo-tier-a.md`;
  staged as short-form-edit.zip). Closest thing to "Sky's system as
  runnable code" — PWC re-skin (teal/gold on navy, NO RED, nothing over
  face) before any Q video.

## Card 2 — OPENFILM (visual timeline) — NEW, MIT, VETTED
- Repo: `openfilm/openfilm` — 5,762★, **MIT** (LICENSE read in the local
  clone, `research/openfilm/`, 122 MB shallow clone, Nov 11, 2026).
- The model — "One HTML file, one function, one real editor":
  - A film is a folder with `film.html`: tracks of clips (animated pages,
    footage, pictures, sound) cut together, styled with CSS.
  - Each shot is a web page that draws any moment with `frame(t)` —
    three.js/WebGL/canvas/SVG/CSS/GSAP/video. No framework required.
  - **Studio** is a local editor in the browser: move/scale/rotate any
    element, change text/color/style, place/crop/restyle clips, trim and
    cut on the timeline, edit subtitles. Hand edits save back to the
    film's files, so the agent sees and keeps them; named versions (git).
  - The **canvas** (⌘E) is a storyboard board beside the edit: notes,
    pictures, clips, voice-over and music wired together, then sent to
    the timeline in order.
- Render: headless Chromium (first run downloads ~100 MB). Exports MP4
  (`--4k`, `--blur`, `--alpha` → .webm/.mov), GIF, audio + stems,
  subtitles, stills, slides, and the timeline itself for **Final Cut Pro,
  Premiere Pro and DaVinci Resolve**.
- Install (NOT run — Q's step when he wants it): `npx skills add
  openfilm/openfilm`; needs Node 22.2+ + ffmpeg (+ git). No-skills
  fallback: `npx -y openfilm@latest`. Or the desktop app (macOS/Windows,
  openfilm.dev) — Studio + chat, ffmpeg and Chromium bundled.
- Accounts/keys: making, editing and rendering need **no account**. The
  built-in library (music, sounds, voices, stickers, transitions,
  effects, templates) is free. Generated media uses your own keys
  (ElevenLabs, OpenAI, Google, OpenRouter, fal…) in Studio → Settings →
  Services, or an OpenFilm sign-in.
- Skills architecture: core `openfilm` (what a film is) + `edit` /
  `media` / `canvas`; community film-type skills from `openfilm/skills`,
  installed with `openfilm skill add <link>` and offered to every agent.
- PWC fit — the honest delta: this is the ONLY one of the four that gives
  Q a visual timeline he can hand-correct (Mariah's exact pitch). It is
  still an HTML renderer in the HyperFrames/Remotion family — **not
  CapCut-native**, so Sky lanes finish in CapCut regardless. Versus
  HyperFrames (owned): OpenFilm's edge is Studio + canvas + free asset
  library + NLE XML export; HyperFrames' edge is the block catalog and
  that Herk's cards already run on it.

## Card 3 — OPENMONTAGE (production pipelines) — PARKED (Q's rule)
- Repo: `OpenMontageInc/OpenMontage` — 79,603★, **AGPL-3.0**.
- What it is: "agentic video production system" — 12 production
  pipelines, 100+ tools, 700+ agent skill/production-knowledge files;
  the long-recording → short-clips strength the reel cites is real.
- Q's status: **PARKED.** AGPL copyleft is on Q's loud license-flag list
  (kit-repo-tier-a.md): read-only inspiration, never installed or run
  for PWC's commercial work without Q's explicit word. The reel's
  recommendation does not outrank Q's rule. Q's working substitute for
  its clipping job: ffmpeg-skill + his existing lanes + CapCut.

## Card 4 — HYPERFRAMES (motion engine) — OWNED
- Repo: `heygen-com/hyperframes` — 82,639★, Apache-2.0. "Write HTML.
  Render video. Built for agents."
- Q's status: installed three ways — custom skills `hyperframes`,
  `hyperframes-cli`, `hyperframes-registry` + web part #323
  `hyperframes-motion-graphics` (catalog-first workflow: search the
  catalog → `npx hyperframes add <block>` → build → Studio preview →
  render). Also the engine under Herk's 406 cards (Card 1).

## Funnel note (for the decode file)
Her CTA — "comment FOUR and I'll send you all four" — is a
comment-keyword DM funnel, the same shape as Q's ManyChat system.
Logged as a format observation only; no links chased, nothing gated
was obtained.

## PWC skin (applies to every card above)
Mechanics never change. Skin always changes: teal/gold on navy, NO RED,
PWC logo, Q's voice, WAITLIST / lane-keyword routing. Nothing over the
face, ever. CapCut-native motion for Sky lanes.

## Where it lives in Claude
This part (#326) + skill `pwc-ai-edit-repo-stack` (web, LIVE) + GitHub
library. Deep source: `research/openfilm/` (the OpenFilm clone) +
`research/free-claude-editing-kits/` (Herk sweep) + parts `herk.md`,
`kit-repo-tier-a.md`, `hyperframes-motion-graphics.md` (#323).

## STATUS UPDATE — Nov 11, 2026 (OpenFilm walked in)

Q said "Walk it in" — OpenFilm is INSTALLED: skill at ~/.agents/skills/openfilm (symlinked to Claude Code); CLI doctor green — OpenFilm 0.3.2, Node v24.22.1, ffmpeg/ffprobe 8.1.2, npm reachable; headless browser + Playwright ffmpeg downloaded (required TMPDIR and PLAYWRIGHT_BROWSERS_PATH pointed at the home disk — the VM's /tmp tmpfs is 512MB and was full). Render proof ON THIS VM is blocked by the VM's headless-browser egress tunnel: films that fetch JS from CDNs fail with ERR_TUNNEL_CONNECTION_FAILED (verified on OpenFilm's own examples). That is an environment wall, not an OpenFilm defect — OpenFilm's working home is Q's own machine (desktop app / his Claude Code install), where the network is normal. A local-assets-only film could still render here; CDN-dependent films cannot.

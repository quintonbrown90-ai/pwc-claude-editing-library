# INDEX — everything in claude-editing, with old → new paths

Canonical home: `~/workspace/claude-editing/`. Every moved item keeps a compat
symlink at its old `~/workspace/<name>` path. "COPY" = original stays where it
was (protected area: your_files/, goals/); "REG" = registered here, lives
elsewhere (too big to duplicate).

## skills/ — Claude skill sources (zipped from here for upload)
| Item | New path | Old path | Notes |
|---|---|---|---|
| pwc-designed-captions (v1 in Claude) | skills/pwc-designed-captions/ | claude_caption_skill/pwc-designed-captions | @viashaan captions pipeline + code + fonts |
| pwc-animations (v1) | skills/pwc-animations/ | claude_anim_skill/pwc-animations | 6 HTML templates + render_animation.js (node_modules EXCLUDED from zip — SKILL.md documents install) |
| pwc-design-system (v1 → v2 in progress) | skills/pwc-design-system/ | claude_ds_skill/pwc-design-system | Claude-skill copy of the stack |
| adilet-system | skills/adilet-system/ | adilet_system/ | 9 files: SYSTEM/HOOKS/PACING/MOTION/CAPTIONS/AUDIO/ILLUSTRATION/PROMPTS/CATALOG |
| effects (v1) | skills/effects/ | browser_downloads/...claude-video-effects-main.zip | 51 face-tracked effects, extracted from the repo zip (old effects_extract/ was empty debris — removed) |
| realskytan-system | skills/realskytan-system/ | custom-skills/realskytan-system/SKILL.md (COPY — Muse registry copy stays) | Sky system skill, 269 lines |

## editors/ — the two editor skills
| Item | New path | Old path | Notes |
|---|---|---|---|
| pwc-avatar-video (v3 in Claude) | editors/pwc-avatar-video/ | adilet_staging/pwc-avatar-video | 62 files incl. tar.gz bundles + adilet/ |
| pwc-video-editors (v16 in Claude) | editors/pwc-video-editors/ | adilet_staging/pwc-video-editors | SKILL.md + adilet/ (ADILET MODE appended, original exact prefix) |

## design-system/ — THE STACK (live repo, moved whole)
| Item | New path | Old path |
|---|---|---|
| MUSE.md / BRAND.md / WORKFLOW.md / COMPONENTS.md / templates/ / tests/ + EDIT-ROUTER.md + BRAND-DNA.md | design-system/ | pwc-design-system/ |
| Brand-DNA training set (README + 4 before/after spec sheets: Sky Form 2, Adilet avatar, Viashaan captions, Viashaan animations) | examples/brand-dna/ | NEW (Nov 8) |

## examples/
| Item | New path | Source | Notes |
|---|---|---|---|
| Sky motion teardown (15 reels, frames + transcripts + notes) | examples/sky/motion-teardown/ | COPY your_files/realskytan_motion_teardown | 151 MB |
| Sky priority 15 (video files) | examples/sky/priority15/ | COPY your_files/realskytan_priority15 | 15 MP4s, 115 MB |
| Sky style creators | examples/sky/style-creators/ | COPY your_files/sky_style_creators | CREATORS.md + frames + reels |
| Sky style guide | examples/sky/SKY_STYLE.md | COPY pwc-videos-stack/SKY_STYLE.md | |
| Sky carousel styles | examples/sky/carousel-styles/ | COPY your_files/for-claude-assets/08_carousel_styles | 42 MB |
| Sky carousel run 41 | examples/sky/carousel-run41/ | COPY your_files/for-claude-assets/09_carousel_run41 | 339 MB |
| Adilet videos (59 reels) | examples/adilet/videos/ | MOVED adilet_work/videos | 347 MB |
| Adilet hero reel | examples/adilet/hero-reel-DfXTzMZINjp.mp4 | MOVED adilet_work/hero_test.mp4 | |
| Adilet breakdown doc | examples/adilet/ADILET-SYSTEM-BREAKDOWN.md | COPY your_files/ | |
| Viashaan demos (A + B) | examples/viashaan/demos/ | COPY your_files/viashaan-demos | |
| Viashaan breakdown doc | examples/viashaan/VIASHAAN-SYSTEMS-BREAKDOWN.md | COPY your_files/ | |
| Viashaan screen recording (source reel) | REG user/media_library/video/94/94f9d8010cc36f08cbdef4013fc22400ce0cea04282b02dd06b313b8d0c32a15.mp4 | — | user upload area, never moved |
| Reference style stills | examples/reference-reels/style_01–03.png | COPY style_ref/ | |

## assets/
| Item | New path | Notes |
|---|---|---|
| Fonts (real files) | assets/fonts/ | MOVED ~/workspace/fonts (168 KB) |
| Meme refs | assets/memes/refs/ | COPY of for-claude-assets/07_memes_gifs/refs (49 MB) |
| Meme/GIF library (6.7 GB) | REG ~/workspace/your_files/for-claude-assets/07_memes_gifs/library/ | Too big to duplicate; 138 files, registered |
| SFX | REG editors/pwc-avatar-video/sfx/ + bundles in editors/pwc-avatar-video/bundles/ | Inside the avatar skill; also ~/workspace/video/beats_cleared/ (52 MB licensed beats) |
| Images / proofs / head cutouts | REG ~/workspace/your_files/for-claude-assets/ (01–11) | 7.5 GB asset pack; registered, not copied |
| Covers | REG ~/workspace/manual_posts/backyard_thumbnails/ + pwc-videos-stack covers | Posting covers; registered |

## code/
| Item | New path | Old path | Notes |
|---|---|---|---|
| skill_zips_build.py | code/skill_zips_build.py | ~/workspace/skill_zips_build.py | Paths updated to canonical locations; now enforces ≤200 files + ≤30MB per zip |
| package_all.sh | code/package_all.sh | ~/workspace/package_all.sh | Legacy packager (superseded, kept) |
| sync_gate.py | code/sync_gate.py | ~/workspace/sync_gate.py | Lip-sync frame strips |
| batch_strips.py | code/batch_strips.py | ~/workspace/batch_strips.py | Face-crop strips |

## research/
| Item | New path | Old path |
|---|---|---|
| caption-skill-research | research/caption-skill-research/ | caption_skill_research/ |
| sky-edit-skills (Nov 7 shortlist, 12 skills) | research/sky-edit-skills/ | sky_edit_skills_research/ |
| adilet-teardown | research/adilet-teardown/ | adilet_work/ (minus videos → examples/adilet/) |
| sky-like-creators/ | research/sky-like-creators/ | DONE Nov 8 — 11 creators ranked, 8 downloads (MIT etc.), INDEX.md |
| free-claude-editing-kits/ | research/free-claude-editing-kits/ | IN PROGRESS (Phase 3 expansion) |
| claude-editing-creators/ | research/claude-editing-creators/ | IN PROGRESS (Phase 3 expansion, incl. Format A/B hunt) — @david_knowsai filed HIGH-fit (effects teacher, Format A) |
| knowledge-harvest/ + knowledge/ | research/knowledge-harvest/ + research/knowledge/ | DONE Nov 8 — 23 YouTube videos (18 with files, ~130k words), ~40 guides, 10 playbooks, 89 entries, 83 executable = 93.3% |
| repo-sites/ | research/repo-sites/ | IN PROGRESS (Expansion 8 — GitLab, Bitbucket, Codeberg, SourceHut, registries, npm/pip) |
| prompts/ | research/prompts/ | IN PROGRESS (Expansion 8 — prompts across X, Threads, TikTok, Reddit, LinkedIn, Facebook) |
| video-harvest/ | research/video-harvest/ | LIVE — exemplar decode filed Nov 8: @david_knowsai DfdAvbfRQY5 (Format A, 7 effects) + TEMPLATE.md (decode structure for all future videos) |

## zips/ — upload-ready Claude skill zips (all verified)
| Zip | Files | Size | Claude status |
|---|---|---|---|
| pwc-designed-captions.zip | 19 | 0.45 MB | v1 ON |
| pwc-animations.zip | 17 | 0.9 MB | v1 ON (node_modules excluded) |
| pwc-design-system.zip | 8 | 0.01 MB | v1 ON |
| effects.zip | 29 | 2.3 MB | v1 ON |
| pwc-avatar-video-v3.zip | 62 | 24.6 MB | v3 ON |
| pwc-video-editors-v16.zip | 10 | 0.06 MB | v16 ON |
| short-form-edit.zip | 8 | 0.04 MB | STAGED — upload (Herk, MIT) |
| viral-outliers.zip | 3 | 0.02 MB | STAGED — upload (Ava Yuergens, MIT) |
| video-to-shorts-skill.zip | 19 | 2.3 MB | STAGED — upload (social-media-skills, MIT) |
| pwc-motion-playbooks-v2.zip | 3 | 0.01 MB | STAGED — upload (v2: GSAP eases added) |
| pwc-video-editors-v17.zip | 10 | 0.15 MB | STAGED — upload (v17, ADILET MODE intact + HUMAN-MADE CHECK) |
| pwc-design-system-v3.zip | 15 | 0.09 MB | STAGED — upload (v3: ALL 10 knowledge playbooks DISTILLED) |

## uploads/
| Item | New path | Notes |
|---|---|---|
| INBOX/ | uploads/INBOX/ | Q's intake — see UPLOAD-RULES.md |
| UPLOAD-RULES.md | uploads/UPLOAD-RULES.md | What to drop, naming, what happens next |

## archives/ — superseded, kept for reference
| Item | New path | Old path |
|---|---|---|
| claude-skill-full-v2 | archives/claude-skill-full-v2/ | claude_skill_full/ (162 MB, v2 full sources + zips) |
| claude-skill-repack-v2-slim | archives/claude-skill-repack-v2-slim/ | claude_skill_repack/ (38 MB) |
| editors-v16-early-staging | archives/editors-v16-early-staging/ | editors_v16/ (pre-Adilet staging) |

## Deliberately NOT moved (registered, not duplicated)
- `~/workspace/claude_avatar_posts/` (6.7 GB) — avatar video queue + re-encodes; posting lane, not editing sources.
- `~/workspace/edit_pilot_work/` (11 GB) — edit-pilot workspace + knowledge base; referenced by editors, too big to duplicate.
- `~/workspace/pwc-videos-stack/` — live launch posting stack (files post from here).
- `~/workspace/user/` and `~/workspace/your_files/` — Q's uploads and deliverables; never moved by policy. Copied subsets live in examples/.
- `~/workspace/goals/` — goal workspaces; `goals/realskytan-style-steal-for-q-s-content/` is the Sky goal — registered, not moved.
- `~/workspace/custom-skills/` — Muse's skill registry (pointer SKILL.md files for all of the above stay live there).

## Nov 8 additions — strategy mastermind, gap-fills, gesture layer (v4)

| Item | Path | Notes |
|---|---|---|
| WHAT-Q-DIDN'T-SAY.md | `WHAT-Q-DIDN'T-SAY.md` (folder root) | 11 gap-fills, each sourced + marked [GAP-FILL]; Q can strike any |
| GESTURES-MOVEMENTS.md | `research/knowledge/GESTURES-MOVEMENTS.md` | Visual-language vocabulary (OBSERVED + INFERRED); feeds Motion + Camera specialists |
| AUDIENCE-PSYCHOLOGY.md | `research/knowledge/AUDIENCE-PSYCHOLOGY.md` | Following-growth mechanics (#13) |
| SALES-CLOSING.md | `research/knowledge/SALES-CLOSING.md` | Q's actual offers only; objection table (#14) |
| CREATOR-PAIN-POINTS.md | `research/knowledge/CREATOR-PAIN-POINTS.md` | Top 10 pains, ranked, exact creator wording (#15) |
| TRENDS.md | `research/knowledge/TRENDS.md` | Top 5 what's working now, measured only (#16) |
| STRATEGY.md / GAP-FILLS.md | `design-system/STRATEGY.md`, `design-system/GAP-FILLS.md` | Mirrored into `skills/pwc-design-system/` — ship inside design-system v4 |
| New parts (17) | `parts/strategy/`, `parts/audience-psychology/`, `parts/sales-closing/`, `parts/creator-pain-points/`, `parts/trends/`, `parts/gap-fills/` (11), `parts/knowledge-playbooks/gestures-movements.md` | Total now **71 parts in 19 categories** (`code/build_parts.py`) |
| AGENTS.md | `design-system/AGENTS.md` (+ mirror) | 16 specialists + master (was 11) |
| **IG teachers sweep LANDED (Nov 8)** | `research/claude-editing-creators/` (52 creator folders) + `research/video-harvest/INDEX.md` | 17 Format A + 7 Format B decodes, 6 carousel teardowns, 376 IG URLs enumerated → **488 files in `uploads/QUARANTINE/reels/` (2.6 GB)**; 60 YouTube enumerated, 59/84 files quarantined; 7 repos cloned + scanned; remotion-dev/skills PARKED (no license); 8 cross-video gesture patterns; Tier S: kienobifilms, thelifeoflibs, kingketo, zachdoesai_, patlaw/david_knowsai/v.i.s.h.ai/nishantchahar.ai |
| **Free-kits sweep LANDED (Nov 8)** | `research/free-claude-editing-kits/` (32 kits, 3.7 GB) | Top 5: herk-edit-kit, ghost-editor, ffmpeg-skill, mg-styles-15, motion-prompt (all MIT); anfloy-playbook PARKED (no license); buttercut/openmontage/story-studio/video-editor-skills flagged LOUD |
| **Repo-sites + prompts LANDED (Nov 8)** | `research/repo-sites/` (43 repos, 1.7 GB) + `research/prompts/` (~107 prompts) | Best find: ffmpeg-skill (MIT, 4,758★); Tier 1: claude-youtube-editor, clipify/zooms, talking-head-editor, lemo-opuscar (13,498★); top 5 measured prompts in PROMPTS.md §11–15; ~45 prompts flagged [UNVERIFIED] |
| **Batch-1 decodes + EMOTION.md (Nov 8)** | `research/video-harvest/instagram/` (7 decodes) + `research/knowledge/EMOTION.md` | Jayant 5 pillars, JLee ENGINE, Kallaway Triple Hook (carousel style), Viashaan directing thesis, Nate Gold 17-agent grid, Liam Hook skill, CCC viral-idea finder; EMOTION: 16 OBSERVED + 5 GAP-FILL mappings |
| **design-system v5 (Nov 8)** | `zips/pwc-design-system-v5.zip` (17 files, 121.2 KB, verified) | v4 + PROMPTS.md §11–17 + COMPONENTS.md appendix rows (Batch-1, IG Tier S, Tier-A kits/repos, EMOTION) + **8 new parts → 79 parts, 19 categories**. **Wave 1 ships v5, not v4** (v4 → rollback). All 6 research streams landed and folded in; GAP list now 10 items (was 8, all 5 pending streams resolved) |
| **github-repo/ re-synced (Nov 8)** | `github-repo/` (196 files, 6.5 MB) | 79 parts + design-system (15 files) + all 7 skills-distilled (node_modules excluded) + operating docs. Push is the parent's step (repo name + visibility to confirm with Q) |

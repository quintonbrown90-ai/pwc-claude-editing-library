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
| watch (v0.3.2) | skills/watch/ | bradautomates/claude-video (GitHub, MIT) via Batch 27 quarantine clone | REAL third-party skill, verbatim (SKILL.md + 10 scripts) — /watch: yt-dlp download + ffmpeg frames + captions-first transcript (WhisperX/Groq/OpenAI fallback, Gemini engine optional); SCAN PASS Nov 10, 2026; web bundle watch.zip in the Batch 27 folder (upstream: Chat upload unsupported, Code is the working install) |

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
| video-harvest/ | research/video-harvest/ | LIVE — exemplar decode filed Nov 8: @david_knowsai DfdAvbfRQY5 (Format A, 7 effects) + TEMPLATE.md (decode structure for all future videos). Batch 17 filed Nov 9: @millee.md DfCzXfRlrUo anti-slop carousel (DECODE.md + ANTI-SLOP-RULES.md) → part #310 `parts/render-pipelines/anti-slop-rules.md` (Option 2 reference). Batch 21 filed Nov 9: @champmack DfNOYB-hjiH "Build 100 Agents with 1 Prompt" (DECODE.md + ULTRACODE-FINDINGS.md — /ultracode is a native Claude Code setting, NOT a command; ADOPT-WITH-CONDITIONS) → part #311 `parts/creator-systems/champmack-ultracode-100-agents.md` . Batch 22 filed Nov 9: @coursecreator360 full-profile survey (194/310 posts, 121 videos, 14 teaching reels, zero code-sharing reels) + three new reel decodes DfXY_acgn3f / Dfhq_jrAjWm / DfHymYIAReD (PROFILE-SURVEY.md + CODE-HUNT.md + MOTION-CLIPS.md + FLAGS-RESOLVED.md — Split Stage is a HORIZONTAL top/bottom split and chips #01 none / #02 setup-beat-only; the canonical decode was WRONG twice; Stockton shares NO public code) → parts #312–#313 `parts/creator-systems/coursecreator360-full-profile.md` + `parts/creator-systems/coursecreator360-devices-and-code-hunt.md` . Batch 23 filed Nov 10: @aiwithsachi Dc7G9Pxu_1O "Top 5 Claude Code plugins" (DECODE.md + PLUGINS-VERIFICATION.md — 66.39s, 5,782 likes / 2,193 comments, 37.9% comment-to-like DM funnel; beats 1–3 evidenced, beats 4–5 asserted; plugin verdicts: OmniRoute DO-NOT-ADOPT as pitched, Superpowers ADOPT, Caveman ADOPT-WITH-CONDITIONS, Claude Code Setup ADOPT, Claude Security ADOPT-WITH-CONDITIONS; only 2 of 5 Anthropic-official) → parts #314–#315 `parts/creator-systems/sachi-top5-claude-code-plugins.md` + `parts/creator-systems/sachi-claude-code-plugins-verification.md` . Batch 24 filed Nov 10: @kienobifilms DfCe08Phn6p "Try these on your next reel" (DECODE.md — 8.07s, 3 CapCut transitions: Block Rise VERIFIED, #2 unnamed GAP, #3 name GAP "Blu-ra…anning"; sound-sync rule ≤1–2 frames) + @david_knowsai DfdHrHOKwO9 "One clip, 7 edits in Claude Code" (SPOTLIGHT-DECODE.md — 7 /effects verified real against fx.py; to-do/checklist mislabel corrected; spotlight build spec; skill free/public + already owned as skills/effects v1; second decode, re-cut of DfdAvbfRQY5) → parts #316–#317 `parts/creator-systems/kien-capcut-transitions.md` + `parts/creator-systems/david-ho-effects-spotlight-verification.md` . Batch 25 filed Nov 10: @createcontent.club DfkUXRNAbb2 "Claude steals viral videos for you" (DECODE.md — 29.61s, /ccc-script-cross-niche: hook-skeleton extraction from a completely different niche + What moved/What stayed audit + beat-for-beat remap in your voice; on-screen skill output VERIFIED from frames, demo CTA tail GAP, internal prompt GAP) → part #318 `parts/scriptwriting/ccc-script-cross-niche.md` . Batch 26 filed Nov 10: Tom @tomxsystems DffhT_iRb6z "Nine agents, one team" (DECODE.md — 74.42s, hub-and-spoke AI team for a trades business: MANAGER hub "hands out the work, checks it's done, reports to you" + receptionist/quotes/follow-up/SEO/analytics/ad-creative/reviews spokes, money chain state-triggered, growth chain parallel, Monday report "what came in / what got booked / what's next"; "Nine agents" CLAIMED but only 8 roles named — 9th agent GAP G-B26-1; Tom's prompt DM-gated, NOT obtained/chased) → part #319 `parts/creator-systems/pwc-agent-team.md` (Q's team: MANAGER + ENGAGEMENT / PITCH / FOLLOW-UP / SEO-REACH / ANALYTICS / CONTENT / PROOF + POSTING/QUEUE as the labeled Q-side 9th; handoff chains, Monday report remapped leads in / booked / next, approval boundary — drafts free, sends + posts need Q) . Batch 27 filed Nov 10: @alextsoi_ai DetPLoEij46 "comment WATCH for the link to the repo" (DECODE.md — 27.75s, the /watch skill pitch: pasted links aren't watched, Claude guesses from title/captions; the free skill adds transcript + through-video screenshots; repo link comment-gated, NOT chased — identified from the reel's own frame f14 + search as bradautomates/claude-video, MIT, 20.4k stars, quarantine-read in full, SCAN PASS; GAPs: G-B27-1 upstream marks Claude Chat upload unsupported — Claude Code is the working install, G-B27-2 frames are capped scene-aware not frame-by-frame) → part #320 `parts/knowledge-playbooks/watch-video-skill.md` (the EYES layer: /watch evidence feeds the style skills; real skill staged verbatim at `skills/watch/` + standalone `watch.zip` in the batch folder). Batch 28 filed Nov 11: @nick_saraev DfPuiYyP4Hy "5 Plugins Your Claude Code Needs" (DECODE.md — 48.62s; five free Claude Code projects frame-identified + GitHub-verified: FreeLLMAPI / Lemo Opuscar / Ponytail / Agent Reach / NVIDIA SkillSpector, all permissive licenses; verdicts for Q: FreeLLMAPI + Agent Reach DO-NOT-ADOPT, Ponytail PARKED, Lemo Opuscar + SkillSpector candidates pending quarantine; comment-gated links NOT chased) + SOURCES.md (Fable 5.2 + Higgsfield MCP extraction — RPN's motion workflow, Higgsfield blog + /mcp page, canonical connector URL https://mcp.higgsfield.ai/mcp, web connector verified ALREADY CONNECTED in Q's Claude.ai Nov 11) → part #321 `parts/motion/pwc-fable-motion.md` (the Fable motion layer — AUTO-ACTIVATES on any edit request, no trigger words; lane bindings CCC / Viral / Sky / Devin / avatar / general; Code-side `claude mcp add` is Q's step; credits discipline) + part #322 `parts/creator-systems/nick-saraev-top5-plugins.md` . Batch 30 filed Nov 11: Rourke Sefton-Minns DYAHDu-KXYx "Claude Code motion graphics, what's really possible?" (DECODE.md — 38.08s; he paid a professional motion graphics artist to stress-test Claude Code; every graphic built in HeyGen HyperFrames from its free template/block library: search the catalog → `npx hyperframes add <block>` → paste the prompt into Claude Code + attach your OWN references → preview/iterate in HyperFrames Studio → render MP4; the full prompt set is comment-gated behind "AI" — NOT obtained/chased; creator's IG handle not in the metadata, GAP) → part #323 `parts/motion/hyperframes-motion-graphics.md` (the workflow + PWC adaptation — catalog-first rule; sibling to the Fable/Higgsfield layer and the installed hyperframes / hyperframes-cli / hyperframes-registry skills; AUTO-ACTIVATES on any motion-graphics job, no trigger words) . Batch 31 filed Nov 11: NO REEL — built directly from Q's AUTO-ACTIVATION standing order (Nov 11 ~12:53 AM CT; ROUTER_NOTES.md — no force-on switch exists for custom skills on either Claude surface, activation is description-matching, so the router + broad auto-fire descriptions are the closest real mechanism; a CLAUDE.md pointer on the Code side + a custom-instructions pointer on the web side are flagged as one-time reinforcements) → part #324 `parts/creator-systems/pwc-editing-router.md` (the always-on router: fires FIRST on any edit request and loads the stack by default — design-system first, Fable motion layer on, perfect-clone when it fits, the matching lane skill, agent-team gates — under Q's hard rules; routes ambiguous jobs by content, slash commands demoted to fallback only) . Batch 29 filed Nov 11: Nick Saraev (@nick_saraev) clone-format decode (DECODE.md — 3 recent reels, 36 scenes frame-analyzed: ONE locked set, TWO framings only — full-frame talking head for hook + CTA, bottom-strip PiP while graphics carry the top 55–65% — face on screen ~40% of scenes in 2–4s bursts, cuts never interrupt a sentence, ONE continuous voice master per video; Saraev's own avatar/voice platforms NOT publicly confirmed — GAP, never asserted; Q_STEPS.md carries Q's one-time ~30-min capture + consent steps) → part #325 `parts/creator-systems/pwc-perfect-clone.md` (Q's photoreal clone system: Tier 0 = Higgsfield on Q's existing credits — Talking Avatar / Digital Twin + Lipsync Studio + Soul ID + Higgsfield voice clone via the connected MCP; Tier 1 = ElevenLabs Starter Instant Voice Cloning; HeyGen only if Tier 0 fails the blind still test; clone QC gates — lip-sync check, face-exposure audit, blind A/B; AUTO-ACTIVATES on any video job, no trigger words; the cartoon pwc-avatar-video lane stays separate) Batch 33 filed Nov 11: @itsmariahbrunner DfmlI5sNFVa "4 free Github repos for editing videos with AI" (DECODE.md — 43.0s; the four repos identified from the audio + GitHub-verified: Herk Edit Kit 2,746★ MIT OWNED Tier-A, OpenFilm 5,762★ MIT NEW + vetted (shallow clone at research/openfilm/, LICENSE read; Studio visual-timeline editor, film.html + frame(t), NLE XML export), OpenMontage 79,603★ AGPL-3.0 PARKED under Q's license rule, HyperFrames 82,639★ Apache-2.0 OWNED; her "158,000 stars combined" claim TRUE — 170,750 now; comment-gated links NOT chased) → part #326 `parts/creator-systems/ai-edit-repo-stack.md` (the routing table: job → repo, completed with Q's stack — ffmpeg-skill / ghost-editor / CapCut-native finish) Batch 34 filed Nov 11: Q-ordered tool hunt (HUNT.md — every GitHub candidate API-verified Nov 11; no honest CapCut challenger; layers win) → part #327 `parts/creator-systems/capcut-boost-and-tool-hunt.md` (VectCutAPI Apache-2.0 CapCut draft automation via MCP — best booster, ToS/version flags; fal.ai generation breadth; ElevenLabs SFX API pre-paid via Starter; video-use transcript cutting; WhisperX caption timing; DaVinci Resolve Studio closest challenger/complement) Batch 36 filed Nov 12: @realskytan full-profile completion (STATUS.md + enumeration/MASTER-TABLE.md — 59 known posts rowed: 49 reels + 10 carousels; 49/49 reels decoded to the Batch-18 bar, 49 measured soundmaps, carousel grammar corrected 10 posts / 86 slides = 51 video + 35 image; tick-tone sound grammar correction; coverage gaps with reasons — 35 carousel image slides undecoded, post-Nov-9 window UNVERIFIED, ~305 posts unenumerable anonymously; research in `research/video-harvest/instagram/batch-36-sky-completion/`) → part #335 `parts/creator-systems/sky-v6-full-profile-completion.md` (SKY v6 — devices D1–D56, 57 registry entries; beat-lock + premium validator gates P9/P10; premium purge — sky_option2.py deleted, premium-only; asset law + Batch 37 fold; canonical skill at `styles/sky-edit-style/`; NOTE: part number is #335, not #334 — #334 was already taken by knowledge-playbooks/max-mobilization, Batch 38) . |

## zips/ — upload-ready Claude skill zips (all verified)
| Zip | Files | Size | Claude status |
|---|---|---|---|
| pwc-designed-captions.zip | 19 | 0.45 MB | v1 ON |
| pwc-memes-web.zip | 3 | 0.01 MB | staged Nov 12 (Batch 40, part #336) — upload is the parent's step |
| pwc-lead-finder-web.zip | 6 | 0.01 MB | staged Nov 12 (Batch 41, part #337) — upload is the parent's step |
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

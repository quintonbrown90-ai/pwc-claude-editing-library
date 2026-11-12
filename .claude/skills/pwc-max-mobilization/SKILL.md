---
name: pwc-max-mobilization
description: "MAX MOBILIZATION — Q's standing order for maximum editing results (viral reach, Dec 7 waitlist). Fires automatically on ANY request to edit or build a video in a named creator's style (Sky, Devin, CCC, Viral, any creator), from a reference video or link, or in any named PWC lane — on Claude Code or the web. Before building, run the full mobilization sweep: load every matching style/editor/caption/animation skill plus the agent team; sweep every folder holding the style (library styles/editors/parts/research, per-style folders, PWC-Videos, harvest batches, open-source pool); pull every reference form — frame shots, screen recordings, screenshots, teardowns, written explanations, direction files; take Q and Kiya's real assets first and ask Muse for anything missing; line up Earshot (ears + beat grid), /watch (eyes), Higgsfield motion, CapCut finishing and the licensed sound library; pull missing references live and decode them before building. Then build, grade against the references in motion, listen back, pass Q's QC gates."
---

# MAX MOBILIZATION — Q's standing order

Q's words (Nov 12, 2026): when he asks for a video in a creator's style, Claude must "grab from as many resources and examples and skills and agents and tools and editors and information and frame shots and screen recordings and written explanations and screenshots and assets and GitHub downloads and repos and Higgsfield and CapCut and Muse and everywhere and everything as much as it can to achieve the results — rather in Claude Code or the web side, whichever I'm editing on. And from as many folders as possible as well and directions etc."

Purpose, in his words: "maximum results for the editing I'm asking so I can start really going viral and building my waitlist."

This is not optional and needs no trigger words. A style-named request with a partial build — some skills loaded, one folder checked, references half-read — is a failed job before it starts.

## When it fires

- Q names a creator or style: "Sky style", "like Devin", "CCC edit", "viral cut", any handle, any lane.
- Q drops a reference: a reel link, a video, a screenshot, a screen recording, a carousel.
- Q asks for any edit on either surface, Claude Code or web chat, when a style exists anywhere in his system for it.
- It fires alongside the pwc-editing-router, never instead of it.

## The sweep — eight nets, all of them, before building

### 1. Skills net
Load EVERY skill that touches the job, searching the full skills list rather than working from remembered names: the style skill itself (sky / devin / ccc / viral / yapping / the creator's own), the editor skills for that lane, caption systems (designed captions, dynamic captions), animation/motion skills, the design system, the agent team (pwc-agent-team), the open-source additions skills for that lane, fable-motion / hyperframes when motion is built in code. If a skill exists for any part of the job and it is not loaded, the sweep is not done.

### 2. Folders net
Sweep every folder that could hold the style or its directions — never just the obvious one:
- The editing library (GitHub: quintonbrown90-ai/pwc-claude-editing-library): `styles/` (per-style folders incl. the style's code), `editors/`, `parts/` (330+ doctrine parts — search by the creator's name, the device name, the technique), `research/` (the video-harvest tree: batch decodes, frame sets, SOUNDMAPs), `open-source-library/` (the pooled tools + cards), `design-system/`, `skills-distilled/`, `.claude/skills/`.
- The PWC-Videos repo: the style master file, `edits/` per-video folders, `assets/`, prior builds of the same lane, session branches carrying related work.
- Muse's tree when reachable: `~/workspace/claude-editing/` working folders, per-style folders, harvest batches (batch-18/19 Sky, batch-11 Devin, batch-36/37 and every batch touching the style), `~/workspace/your_files/for-claude-assets/` (the asset pack + per-job supplies).
- Directions live in folders too: BRIEF.md files, PLAN.md files, GOAL.md files, style grammars, EDIT-ROUTER.md, CLAUDE.md rule files. Read them; Q's written directions in any folder outrank habit.

### 3. Reference media net
Pull every FORM of the reference that exists, not just the video:
- The reference videos themselves (every example of the style on file — for Sky, the full decoded set, not one reel).
- Frame shots / frame sets / contact sheets from the decodes.
- Screen recordings of the reference playing (motion that stills can't show — caption timing, device entrances, transition feel). If a motion is unclear from frames, screen-record the post playing and study the recording; never guess a motion.
- Screenshots and profile captures (the creator's page, their grid, their pinned posts — layout and density evidence).
- Carousel slide sets when the style includes carousels.

### 4. Written material net
Read the words, all of them: DECODE.md teardown files, SOUNDMAP.md files, style grammars (STYLE-GRAMMAR / SKY_STYLE and equivalents), teardown masters, device registries, the parts written about this creator/technique, Q's briefs and correction notes for the lane. A device that is documented does not get reinvented from a screenshot.

### 5. Assets net
Q and Kiya's own pool FIRST — their photos, B-roll, proof screenshots, walls, receipts, the PWC logo (transparent cutout only). Then the proof packs (P-pack = Q's receipts, RC-pack = real creators, run as-is with handles visible). Premium AI assets (Higgsfield-grade) fill visual/motion gaps where no real asset exists. NEVER substitute generic stock, drawn fakes, or AI imagery for real proof — proof stays real. If an asset the style needs is missing, ASK MUSE for it (Muse is Q's asset supplier and holds the pools) instead of substituting or skipping.

### 6. Tools net
Line up the full bench before the build:
- Earshot — ears: beat grid from the actual take, sound-bank sounds, listen-back on every render (nothing is done until it has been heard).
- /watch — eyes for links: transcript + scene frames of any reference URL.
- Higgsfield MCP — premium motion/AI generation layer (Fable 5.2 builds type/titles/UI in code; Higgsfield generates motion).
- CapCut — the finishing home: native caption animations, transitions, effects (CapCut-native for styles born there; renderer imitations of CapCut styles fail Q's eye).
- The open-source pool — gl-transitions, matting (BiRefNet pinned model), caption engines, cleanup/upscale chain, Beat This! beat tracking.
- Q's licensed sound library (~1,250 real sounds) — the sound source. NEVER synthesize effects or beds.

### 7. Agents net
For big jobs, parallelize: the pwc-agent-team roles (CONTENT studies winners, ANALYTICS checks the lane's numbers, SEO/REACH frames hooks/captions) and sub-agents for per-reference decodes and independent QC grades. One agent building from one folder while three decodes sit unread is exactly what this rule exists to prevent.

### 8. Live pull net
If a reference, example, or tool is missing from every folder: pull it live. Download the creator's reels/posts (yt-dlp), /watch them, decode them to the standing bar (frames + word timings + DECODE + SOUNDMAP), check GitHub for the tool/skill (license gate below), check the open-source pool's carded items. THEN build. "It wasn't in the folder I checked" is never a reason a device is missing from the edit.

## Build + verify

- Build to the style's measured system (its grammar, device registry, caption spec, soundmap) — then grade the export AGAINST the references, frame-matched, IN MOTION: a frame-sequence pass around every device entrance/exit (±0.15s), not settled stills alone.
- Earshot listen-back on the exported file; fix every silent cut and late/cheap effect it names; re-listen.
- Q's standing QC gates: zero freezes ≥0.35s in footage spans, last-voice→end-card gap ≤~1s, no word clipped at a cut edge, captions never over his face and never overlapping, beat-lock — every caption/motion/visual/sound/transition lands on the take's beat grid within ~1 frame, and the on-beat % is reported.
- The bar is the style executed at-or-above its creator: Sky-exact is the floor for Sky work, and execution (timing precision, motion smoothness, sound density, polish) must grade above the reference, without drifting into generic patterns the creator doesn't use.

## Report line

Open the delivery with one short block: what was mobilized — skills loaded, folders swept, references used (count + which), tools/agents used, anything pulled live. Q wants to SEE the depth; one block, then the result.

## Hard constraints (the sweep never overrides these)

- Premium only: no cheap fonts, template cards, static stamped overlays, generic stock/AI-flat imagery, default renderer looks. Every device traces to a measured instance in the reference.
- Q's current rules beat every style file and every older document (no red in added graphics, no serif-italic titles in Q's graphics, exit sounds on devices, hard caption cut-ins — per his latest rulings).
- Everything on beat. Nothing over Q's face. PWC colors: teal #14A886, gold #FEE238, navy #00214E.
- Proof/evidence is always real media; claims attributed to their owners; real creators never framed as members or endorsers.
- License gate on all downloads: permissive only (MIT/Apache/BSD/ISC/CC0; CC-BY with attribution). Anything else is parked and reported, never installed.
- Read code before running anything harvested. No credential chasing, no gated/paywalled material.
- Current PWC facts in every deliverable: doors open Dec 7, 2026 only; Premium $97/mo only; waitlisters get an extra month free; CTA comment WAITLIST; never "join now".

<!-- PART: creator-systems/kit-repo-tier-a.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# CREATOR SYSTEM — Tier-A kits + repo Tier 1 (PUBLISHED, deduped)

Source: `research/free-claude-editing-kits/INDEX.md` (32 kits, 3.7 GB)
+ `research/repo-sites/INDEX.md` (43 repos, 1.7 GB). Deduped across
both sweeps — each item listed once. All MIT unless flagged. Full files
on disk in research/; these are the distilled adoption notes.

## The rule
Adopt Tier A first. A kit is adopted only when its distilled workflow
is a part or a prompt — a clone on disk is not adoption.

## Tier A (install first)
- **herk-edit-kit** (MIT, 2,646★) — 15 skills, transcript-driven cuts,
  406 motion-graphics cards on HyperFrames. Most complete talking-head
  kit; closest to a Sky-style end-to-end edit system. Needs Node/ffmpeg;
  ElevenLabs Scribe default (Whisper alt).
- **ghost-editor** (MIT, 253★) — take in → reel out, 7 styles,
  face-safe captions, reverse-engineer-any-reference-edit (Q's "copy
  Sky" workflow). 60 MB.
- **ffmpeg-skill** (MIT, 4,758★) — 42 FFmpeg tools + MCP + doctor, no
  keys, no cloud. The workhorse layer. Ships as `npx ffmpeg-skill`.
- **mg-styles-15** (MIT, 3,261★) — 15 filmed motion styles with prompts
  + full source. A steal-able style library. 1.2 GB. No SKILL.md in repo.
- **motion-prompt** (MIT, 1,391★) — 192 named motion/camera/UI effects.
  Shared vocabulary for moves.
- **claude-youtube-editor** (MIT, 369★) — 8 skills: clean-cut, make-tsx
  (Remotion visuals synced to word times), clean-audio (free local
  RNNoise), suggest-sfx, packaging, yt_upload, brand-setup.
- **Tella four** (MIT, free) — cut-video, add-zooms, clipify,
  b-roll-finder: punch-in zooms on stressed words, b-roll on the exact
  word, long video → vertical clips, no API keys.
- **talking-head-editor** (MIT) — Q's core format as a pipeline.
- **lemo-opuscar** (MIT, 13,498★) — 51 film styles; biggest star count
  in the repo sweep.

## License flags (loud — never stage without Q's word)
- buttercut: PolyForm Noncommercial (not open-source). openmontage:
  AGPL-3.0 copyleft (read-only inspiration). story-studio + video-
  editor-skills: CC BY-NC (non-commercial; Q's PWC is commercial).
  open-edit: renderer binaries closed-source (PolyForm Shield).
  reel-kit: MIT but example accent is red #D40F30 — re-skin to PWC
  before any use. anfloy-playbook: PARKED (no license stated).

## Executable steps
1. Adopt in order: ffmpeg-skill (workhorse) → herk-edit-kit (talking
   head) → ghost-editor (reference reverse-engineering) → motion-prompt
   (vocabulary) → mg-styles-15 (style library).
2. Before installing any kit, read its installer first — none were run
   during the sweeps.
3. Every adopted kit gets a PWC re-skin pass (teal/gold/navy, NO RED,
   nothing over face) before its first Q video.

## Worked example (PWC)
Avatar lane build: ffmpeg-skill cuts the take → herk-edit-kit applies
the motion cards → motion-prompt names the moves → ghost-editor checks
the result against the Sky reference. One pipeline, four kits.

## Variants (v9)
- **v9 · @?, V8-42:** V8-42 — Three-folder project: footage / inspiration / sound + brand identity → kit-repo-tier-a.md _(source: v9_verification.md)_
- **v9 · @?, V8-60:** V8-60 — Four-part content system: brand voice file + design kit + assets folder + publishing → kit-repo-tier-a.md _(source: v9_verification.md)_

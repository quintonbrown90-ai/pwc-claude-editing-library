# SYSTEM — @adilet.fndr's one-prompt production system, decoded

> Evidence key: **[MEASURED]** = observed in his videos/data.
> **[INFERRED]** = reconstructed from outputs — the most plausible build.
> Source: hero reel DfXTzMZINjp (the "191 files" system reel, Nov 5, 2026)
> + all 59 posts (`CATALOG.md`). His own framing is four exhibits:
> A hooks+pacing, B motion, C captions, D audio. This file is the workflow
> that wraps them; the sibling files are the exhibits as usable specs.

## What the system is [MEASURED from the hero reel]

One line typed into Claude Code — his example: *"a reel about AI reels"* —
and the system runs the whole production: **writes → voices → animates →
renders → self-reviews and fixes weak moments → delivers**. His on-screen
checklist, in his order: WRITES ✓ · VOICES ✓ · ANIMATES ✓ · RENDERS ✓ ·
DONE, then a SELF-REVIEW pass ("STATUS: WATCHING → 1 WEAK → 0 WEAK →
FIXED") before the viewer ever sees it. No camera, no face, no editing —
his closing montage crosses out CAMERA / FACE / EDITING, and the CTA card
sends viewers to comment a keyword.

The "191 files" are the *asset + rules library* the pipeline loads every
run: hook patterns, pacing rules, motion physics, caption timing, audio
chain, component templates (subject files, stamps, exhibit cards,
diagrams, terminal cards), the avatar pose library, and per-stage prompts.
**The number is elastic marketing**: on Oct 26 he claimed **221 files**
(De8yh94R0SZ), on Nov 5 it's **191 files** — the library is real, the
count is whatever this week's reel says. The transferable truth is the
architecture: *components built once, rules written down, one prompt runs
the pipeline.*

## Stage order (the pipeline) [MEASURED order; mechanics INFERRED]

1. **BRIEF** — one line: topic (+ optional angle/keyword). Everything else
   is system defaults.
2. **SCRIPT** — written to the hook patterns + pacing rules (HOOKS.md,
   PACING.md): hook line first, one idea per beat (~2–4s of speech), a
   claim needs its proof object named in the same beat, CTA keyword woven
   into the last line.
3. **VOICE** — script → ElevenLabs synthetic male voice (AUDIO.md), then
   the audio chain: cuts, speed pass, loudness master for Instagram. The
   finished voice track is the **master clock** for everything downstream.
4. **TIMING** — word timestamps extracted from the voice track; caption
   events and scene beats are scheduled from word times. (His Exhibit C
   *claims* key words land 0.3s before the voice; we measured the hero's
   captions at a **0.00s median lead** — they land exactly ON the word.
   CAPTIONS.md has the full test. The real system is word-exact sync.)
5. **ANIMATE** — each beat gets its component (subject file, diagram,
   stamp, terminal, count-up) and its motion from the physics presets
   (MOTION.md: spring default, whip-pan transitions, zoom kicks). Avatar
   pose chosen per beat from the pose library (ILLUSTRATION.md).
6. **RENDER** — 1080×1920, 30fps, deterministic frame rendering (the same
   setT-style contract our pwc-animations templates use).
7. **SELF-REVIEW** — the rendered reel is re-watched by the system:
   frames sampled, weak moments flagged (his on-screen language: "1 WEAK"
   → fixed → "0 WEAK"), beats re-rendered, *then* delivered. This QC loop
   is a stage, not an afterthought.
8. **DELIVER** — file + caption written around the same hook + the comment
   keyword CTA (his funnel: comment keyword → DM link).

## Costumes rotate, DNA doesn't [MEASURED, deep set]

Frame-logging the top/newest 13 videos shows the visual *wardrobe*
changes by era and topic — dossier (hero), flat cream stage (his mature
house format), dark terminal UI (September dev-tools), even avatar-less
variants — while the DNA stays fixed: presenter avatar, top caption
strip with highlighted keywords, count-up numbers, stamps, one proof
object per claim, keyword CTA. Full taxonomy in ILLUSTRATION.md. For
PWC this is liberating: **one PWC costume is enough — the system is the
pipeline + DNA, not the kraft paper.**

## The rules that make it a system, not a prompt [MEASURED]

- **One stage, one job, one file-set.** Hooks live with hooks; physics
  numbers live with motion; nothing is re-decided per video.
- **Components are built once and reused** — across all 59 videos the
  character, cards, stamps and layouts do not change (deep-set verified).
  New topics are *data* poured into the same components.
- **Consistency is the retention device**: viewers learn the DNA
  (avatar, caption strip, stamps, count-ups) once, then every new video
  reads instantly — even when the costume changes.
- **Series iteration**: a winning hook is re-run with small variations
  (the "$100K lawsuit" hook ran 4× in 10 days: 22.6K, 264, 18.4K, 34.3K
  likes) — the system tests hooks like ad variants.
- **Every claim gets a visual proof object in the same beat.** No naked
  assertions; the document on stage *is* the argument.

---

## PWC ADAPTATION — same architecture, PWC skin (Q's law governs)

Structure copied 1:1. Everything audience-facing is re-skinned:

| Adilet system | PWC version |
|---|---|
| Dossier world: kraft paper, wood desk, stamp-**red** accent | PWC stage world per `BRAND.md`: navy `#00214E` / teal `#14A886` / **gold `#FEE238`**, white. **NO RED anywhere** — his stamp-red maps to gold (stamps, highlights, count-ups all gold) |
| Bearded cartoon avatar, bottom-center presenter | **Q's PWC avatar** (the existing pwc-avatar-video character + desk room), same bottom-center presenter grammar, same pose-per-beat reaction rule |
| Synthetic male ElevenLabs voice | PWC locked voice (George / Kokoro `bm_george` at native 1.11 — see pwc-avatar-video VOICE.md). Never time-stretched |
| Tech/AI-education topics, Claude-Code-meta hooks | PWC topics: UGC, brand deals, creator income, Paid With Content teaching — hooks rebuilt from HOOKS.md patterns with PWC claims only (no invented numbers; collective "creators like my wife and I…" framing for earnings) |
| CTA: comment SKILL → his link | CTA: comment the video's **PWC ManyChat keyword** (WAITLIST / CALENDAR / video-specific flow keyword) → the live PWC flow. The hidden UGC app is **never named** in public content |
| Captions claimed −0.3s ahead of voice | Measured reality: **0.00s lead — captions land exactly ON the spoken word**. PWC adopts the measured rule (word-exact sync from the final voice track), not the marketing number |
| Self-review: "1 WEAK → 0 WEAK" | Kept, plus PWC gates from `tests/QC_CHECKLIST.md`: freeze scan, face-clear, safe zones, red scan, retention read — run on the **exported file** |
| One line in Claude Code runs it | One line to the pwc-avatar-video / pwc-video-editors skill runs it: the `adilet/` folder in each skill carries this system |

**What does NOT transfer:** his red, his face/character likeness, his
voice, his topic claims, his follower/view numbers, and his file-count
number (191/221). PWC uses its own proof, its own counts, its own world.

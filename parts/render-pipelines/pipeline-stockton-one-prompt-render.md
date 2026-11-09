<!-- PART: render-pipelines/pipeline-stockton-one-prompt-render.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# PIPELINE — Stockton one-prompt render: sync -> sift -> transcribe -> ONE prompt [INFERRED reconstruction]

Source: @stocktonwalbeck / @coursecreator360 reel DfcnEEMgsNf — the
pipeline read off his OWN on-screen frames (Prompt Drop frame f_021 +
title frame f_003). The demo build is gated behind EDITOR -> DM — NOT
chased. Rebuild from visible specs only.

## The rule
No NLE timeline at any step. Four steps, one prompt: sync the audio,
sift the raw to last-takes, transcribe, then ONE prompt renders all the
effects. This is the exact shape Q's router + editors should run:
transcript-first, effects chosen per line.

## The four steps (verbatim from his frames)
1. **Sync camera + DJI mic (measured offset 0.925s).** The offset is
   MEASURED, not guessed — a constant offset, the same discipline as
   Q's hat talks (side angles = same performance, constant offsets fix
   sync; one master audio track, whole turns). Measure it once per
   shoot (clap / waveform align), write it down, use it everywhere.
   Checklist line: `synced camera + DJI mic (offset 0.925 s)`.
2. **Sift raw to last-take-of-every-line (2:08 -> 0:41).** Keep the
   LAST take of every line, drop the rest. 2:08 of raw becomes 0:41 of
   keepers — a 3.1x cut before any effect is chosen. Checklist line:
   `sifted 2:08 raw -> 0:41, last take of every name`.
3. **Transcribe (106 words).** Word-timed transcript of the keepers —
   the transcript is what the effect selection reads. 106 words for
   40.75s (~156 wpm). Checklist line: `transcribed 106 words`.
4. **ONE prompt renders all 17 effects.** Command (verbatim from the
   frame): `> edit effects-talking`, input file
   `effects-talking_synced.mov`. The AI editor reads the transcript and
   decides which effect lands on which line — transcript-aware effect
   selection (see the router rules in `design-system/EDIT-ROUTER.md`
   §10). Title-frame line: `rendered all 17 in this take`.

## Executable steps (rebuild for Q)
1. Shoot + record: camera + DJI mic (or Q's mic). Measure the A/V
   offset once (clap); record it in the checklist.
2. Sift: last take of every line only; log raw -> keeper durations.
3. Transcribe word-timed (106-word scale for a ~40s video).
4. Route: run the transcript through the effect-selection rules
   (EDIT-ROUTER.md §10) — one effect per trigger line, never two
   effects on one line, never an effect with no trigger line.
5. Render: ONE prompt per video (`edit <video-slug>` shape), input the
   synced keeper file. All effects render in one take.
6. QC on the exported file (pipeline-qc-gates.md): freeze, transition,
   ending, lip-sync, retention, brand-DNA, human-made — before delivery.

## The Prompt Drop device (trust device)
Showing the actual Claude Code command + checklist on screen is itself
a device — see `parts/effects/effects-prompt-drop.md`. Q's Claude can
do the same in behind-the-scenes content: show the real command, the
real synced filename, and the real 3-step checklist for the video being
watched. Real command, real file, real numbers — never a redrawn fake.

## PWC remap
Same four steps; Q's skin: the prompt names Q's real command for the
job (router intake / lane prompt); the checklist carries Q's real
numbers (his offset, his raw -> keeper durations, his word count).
Nothing over Q's face; teal/gold on navy, NO RED.

## Worked example
Q's 40s proof take: offset measured 0.XXXs (his shoot's number);
2:08 raw -> 0:41 keepers; 106 words transcribed; `> edit
proof-take-07` renders the routed effects (Hall of Fame on the proof
line, Color Pop on the number, Reveal Bar on the before/after) in one
take — then the Prompt Drop card shows the real command + checklist
in the BTS cut.

## Variants (v9)
- **v9 · @david_knowsai, DfDe25xqLGM:** 29. @david_knowsai, DfDe25xqLGM — Ghost Editor ("picks the best takes, adds captions that stay off your face, puts in graphics and sound effects") → variant on render-pipelines/ pipeline-stockton-one-prompt-render.md. Higgsfield editorial motion graphic skill (topic → animated explainer with scenes, voiceover, subtitles) → variant on creator-systems/adilet.md. Claude Shorts (long video → strongest moments → short clips with captions) → variant on render-pipelines/pipeline-repurposing-one-to-ten.md. FFmpeg skill repo (kaydxh0/ffmpeg-skill, 42 tools) PARKED pending license + SCAN (GAP). _(source: v9_variants_bulk_a.md)_
- **v9 · @adamstewartmarketing, Dbfv0N-vCx_:** 47. @adamstewartmarketing, Dbfv0N-vCx_ — "AI video used to mean generating clips. Now it's starting to mean editing the footage you already have" (edit-not-generate doctrine) → variant on render-pipelines/pipeline-stockton-one-prompt-render.md. Differs: the doctrine names the shift. The plugin (full editor beside Claude Code, same editable timeline) is named only — not adopted (GAP for the product). _(source: v9_variants_bulk_a.md)_
- **v9 · @aidendjohnston, DegOQG6Tydw:** 48. @aidendjohnston, DegOQG6Tydw — "If I say a line twice, it chooses the better take" (best-take picker) + WhisperX timestamps every word → variant on render-pipelines/ pipeline-stockton-one-prompt-render.md (the sift step). Differs: the take-choice is automatic, per line. _(source: v9_variants_bulk_a.md)_
- **v9 · @aiwithlakshay, DaVe-oZg206:** 49. @aiwithlakshay, DaVe-oZg206 — "Just tell Claude and it will update and rebuild the whole thing" (tell-to-rebuild revision loop) → variant on render-pipelines/pipeline-stockton-one-prompt-render.md. Differs: the revision is a plain tell (no timeline, no software). Setup guide gated (GAP). _(source: v9_variants_bulk_a.md)_
- **v9 · @alassafi.ai, DY2DRslTEM8:** 50. @alassafi.ai, DY2DRslTEM8 — "It finds every silent gap in my video, transcribes the audio, writes clean motion graphics, and then exports the MP4" (pipeline: silent gaps → transcribe → motion graphics → export) → variant on render-pipelines/ pipeline-stockton-one-prompt-render.md. "It even spits out multiple variations of the same reel, so I can trial different hooks without re-editing anything" (hook-trial device) → variant on creator- systems/tenfoldmarc-3-hook-trial-reels.md. Skill + guide gated (GAP). _(source: v9_variants_bulk_a.md)_
- **v9 · @albert.olgaard, DfXnmUSoE7x:** 51. @albert.olgaard, DfXnmUSoE7x — Higgsfield Genjutsu: one prompt, whole video edited (titles come in, images added, entire mood changed) → variant on render-pipelines/ pipeline-stockton-one-prompt-render.md. Differs: the mood change is part of the one prompt. Guide + link gated; trial sign-up NOT done (GAP for the tool). _(source: v9_variants_bulk_a.md)_
- **v9 · @aluncreative, De9PhswCZMm:** 52. @aluncreative, De9PhswCZMm — "I just filmed, Claude picked my best take, cut every dead moment" (film-only doctrine) → variant on render-pipelines/pipeline-stockton-one-prompt-render.md. Differs: Q films, Claude picks + cuts. Course gated (GAP). FLAG: "sped up my voice" — speedup is REVERSED in Q's lane (1.0× everywhere); NOT adopted. _(source: v9_variants_bulk_a.md)_
- **v9 · @?, ?:** 53. @amintech_us, DebNBUZSnnD / @amintech.ai, DenyWUmtIZZ — "I edited this whole reel with one prompt" + "Every part of this is code, so the next reel takes minutes. Same prompt, new clip." + auto-editor → FFmpeg → Whisper chain (27s down to 16s) → variant on render- pipelines/pipeline-stockton-one-prompt-render.md. Differs: the same-prompt-new-clip economics. DenyWUmtIZZ is the same script, re-recorded. Prompt file gated (GAP). _(source: v9_variants_bulk_a.md)_
- **v9 · @andreapalacio, DWXOCEghurZ:** 54. @andreapalacio, DWXOCEghurZ — "It will write all the scenes based on the transcription of your video once you approve it" (transcription-first doctrine) → variant on render-pipelines/ pipeline-stockton-one-prompt-render.md (the transcribe step). Differs: scenes are written FROM the transcription, and Q approves before generating. Prompt + guide gated (GAP). _(source: v9_variants_bulk_a.md)_
- **v9 · @blackbirdacademy.in, De8h_mky_xW:** 55. @blackbirdacademy.in, De8h_mky_xW — "Just tell Claude" ("Make the text pink") → variant on render-pipelines/ pipeline-stockton-one-prompt-render.md. Differs: the smallest possible tell (one line, one change). Process video + link gated (GAP). _(source: v9_variants_bulk_a.md)_
- **v9 · @getgitgirl, DeaqAhUpuMq:** 59. @getgitgirl, DeaqAhUpuMq — turn-by-turn tell-it-what-to-do → variant on render-pipelines/pipeline-stockton-one-prompt-render.md. Differs: the tell is turn-by-turn, not one prompt. Guide gated (GAP). _(source: v9_variants_bulk_a.md)_
- **v9 · @?, V8-10:** V8-10 — Descript-native cut-down beats Claude round-trips → pipeline-stockton-one-prompt-render.md _(source: v9_verification.md)_
- **v9 · @?, V8-121:** V8-121 — SIFT: dead-space + retake/mistake removal as a science (dB levels, breaths, J/L cuts) → pipeline-stockton-one-prompt-render.md _(source: v9_verification.md)_
- **v9 · @opusjake, DZpfV7Vz1RM:** @opusjake DZpfV7Vz1RM — one-prompt Remotion build in 42s total, the shortest full build in the sweep. DIFFERS: the 42s time is the record, not the standard. _(source: bulk-c VARIANTS.md)_
- **v9 · @stockton, DexNu9xg7BR:** @stockton DexNu9xg7BR — hook-test trios (one body, three hooks, same day); storyboard-before-build shown as a visible line→visual plan card; terminal checklist with real numbers (offset 3.323s, 6:24→1:15, 262 words); 85-visual menu ("over 85 distinct visuals… used on 90% of Instagram content"). DIFFERS: four devices, all portable — the trio is the cheapest hook test; the visible storyboard card teaches the method in one frame. _(source: bulk-c VARIANTS.md)_
- **v9 · @stockton, DexON9TgVWA:** @stockton DexON9TgVWA — hook variant 2 of DexNu ("This right here is what an AI edit looks like when the AI was trained by an actual editor"). DIFFERS: hook only; body + CTA identical (verified by transcript). _(source: bulk-c VARIANTS.md)_
- **v9 · @stockton, DexOYv7Aq1f:** @stockton DexOYv7Aq1f — hook variant 3 of DexNu ("filmed last night, woke up to it"). DIFFERS: hook only; the overnight-turnaround hook is the one line that made it onto the shared storyboard card. _(source: bulk-c VARIANTS.md)_
- **v9 · @leogrundstrom, DfVFq1Ys1SV:** **V98 — @leogrundstrom pairing (DfVFq1Ys1SV):** HyperFrames + video-use as ONE pitch — engine for built graphics, editor for cutting talking-head takes (→ pipeline-stockton-one-prompt-render); GitHub-proof card — show the live star count (78k) instead of claiming popularity (→ strategy-outlier-multiple-swipe); Blender short-film proof (→ blender-free-3d). _(source: bulk-b VARIANTS.md)_

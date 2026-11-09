<!-- DRAFT — v9 bulk-b (group B) — coordinator merges into parts/render-pipelines/ -->
<!-- Source: @me.alex.verse "Finally, you can say goodbye to video editing because someone just built a free tool for Claude Code" (DaCgLjoJjWx) — video-use: the LLM never watches the video, it READS it; two layers, word-boundary precision; Reasons → EDL → Render. -->
<!-- Existing parts checked first: NO reasons-EDL-render part exists. parts/render-pipelines/pipeline-caption.md is the caption pipeline; parts/render-pipelines/pipeline-stockton-one-prompt-render.md is one-prompt render (sync → sift → transcribe → ONE prompt). This part is the read-first pipeline with an explicit REASONS stage and an EDL artifact. NEW part — the pipeline is visible; the repo is NOT adopted. -->
# RENDER-PIPELINES — read, don't watch: Reasons → EDL → Render (DRAFT — v9 bulk-b)

Source: @me.alex.verse "Finally, you can say goodbye to video editing..." (DaCgLjoJjWx) — video-use. Tier S candidate. INFERRED reconstruction from the visible transcript + on-screen README; the repo itself is named only — NOT downloaded, NOT scanned, NOT folded in.

## The rule
"The LLM never watches the video. It reads it — through two layers that together give it everything it needs to cut with word-boundary precision." The edit is decided from the reading, not from watching. Reasons first, then the decision list, then the render.

## The two layers (his words)
Layer 1: the transcript (what was said, word-timed). Layer 2: the audio (how it was said — pauses, energy, restarts). Together they give word-boundary precision: every cut lands on a word boundary, never mid-word. Q's lane already transcribes first (Whisper word-timed) and cuts on the transcript — this video names the doctrine: read, don't watch.

## The pipeline
1. **Reasons:** for every cut, a written reason (why cut HERE — a stumble, a dead pause, a payoff word, a topic change). The brief is the reasons. No reason, no cut.
2. **EDL (edit decision list):** the reasons become a list — cut at [word/time] because [reason]. The EDL is the plan; the plan is reviewable before anything renders (same gate as the cut-list-first rule in ig-tier-s-kienobifilms).
3. **Render:** the EDL renders. No timelines, no manual edits, no back and forth — "No timelines, no manual edits, no back and forth" is the negation that defines the pipeline (same device as corbinsylk's "No timeline. No editor. Just one prompt." — the negation IS the hook).

## Executable steps (PWC)
1. Transcribe first (Whisper word-timed) — the transcript + audio are the two layers. Nothing is cut before the transcript exists.
2. Write the reasons: one line per cut, word-anchored ("cut after 'waitlist' — dead pause 0.6s"). See also mds-word-anchored-edit (new, v9 bulk-b) — the word is the anchor there too.
3. Freeze the reasons into an EDL and approve the EDL (Muse QC / Q's approval) BEFORE the render. A render from an unapproved EDL does not ship.
4. Render from the EDL. QC the render against the EDL (every EDL line visible, nothing extra) + the standing gates (freeze/transition/ending/lip-sync/retention).

## PWC skin
Reasons are Q's rules in plain words (no pauses, no stumbles, words never clipped, payoff words get punch-ins). The EDL is per video, filed in the one-stack folder with the finished file, cover, and caption.

## Gaps
- The repo (video-use) itself: named only, NOT in the harvest, NOT scanned, license unknown — PARKED, never installed. The pipeline above is rebuilt from the visible doctrine, labeled INFERRED.
- The two layers' exact implementation (how the audio layer is encoded for the LLM) is NOT shown — the layer names + the precision claim are the visible spec.

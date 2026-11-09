# WORKFLOW.md — how every job runs

The loop is the same for a 30-second reel and a course video. Skipping a
stage is how amateur cuts happen; the tests at the end are gates, not
suggestions.

## The six stages

1. **INTAKE** — name the lane (Q's real footage / avatar / couples), the
   source files, the script (ground truth for captions), the keyword/CTA,
   and the deliverable count. Confirm the source is the take Q means.
2. **BEAT PLAN** — from the transcript with word timings: hook (claim or
   curiosity ≤2s, Q's face on screen), open loop early + a second before
   the midpoint, a visual event every ≤2s, every element's component,
   placement zone, and NAMED motion. Nothing renders before the plan
   exists. (Template: templates/beat-plan.md)
3. **BUILD** — assemble from COMPONENTS.md. New objects get built once,
   registered, then used. Captions via pwc-designed-captions' pipeline
   (track → align → plan → render layers → composite); inserts via
   pwc-animations templates; avatar lane via pwc-avatar-video's engine.
4. **RENDER** — export H.264/AAC, 1080×1920, faststart, 12–20 Mb/s.
   Post-bound files are 1080 wide (IG serves 1080 anyway); keep 4K
   masters on file when the source is 4K.
5. **TESTS** — run tests/QC_CHECKLIST.md on the EXPORTED file, in motion.
   Any gate failure = fix + re-render + re-test. No exceptions, no
   "probably fine."
6. **DELIVER** — files as full-quality attachments. Judging phase: 2–3
   videos. Approved batches: all at once, one drop. Report status as
   QUEUED / IN PROGRESS vs DONE + VERIFIED — never blur the two.

## Lane notes

- **Q's real videos** post at prime slots; backyard/night videos ~9 PM CT.
- **Avatar lane** posts only Claude's finished renders; every keyword in a
  video must have a live ManyChat flow before the video posts.
- **Captions ≤500 chars**, SEO-short, written to creators under 10K who
  want UGC/brand deals; keyword CTA + dual-CTA profile line; ≤5 hashtags.
- Trial-reel variants (after main-batch approval) must DIFFER from the
  main reels, 3×/day at main traffic times.

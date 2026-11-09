<!-- PART: render-pipelines/pipeline-deadair-gate.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# RENDER-PIPELINES — deadair gate: automate "no pauses, no air space" (MIT, SCAN PASS)

Source: Jakeschincariol/youtube-agent-skill `deadair.py` (MIT, SCAN PASS —
stdlib only). DISTILLED in research/repo-sites/opusjake-youtube-agent-skill/.
The YT workflow itself is NOT imported (Q's lane is IG).

## The rule
Dead-air floor default 0.35s — any silence ≥0.35s in the voice track is a
cut candidate. The tool outputs a filler-only list + a retake cut list from
.srt / .vtt / Whisper JSON. This automates Q's through-edit gate ("NO AIR
SPACE; only DRAMATIC pauses survive, max 2/video, ≤0.30s") from a Whisper
transcript instead of by ear.

## Executable steps
1. Transcribe the finished voice track (Whisper word timestamps).
2. Run the deadair pass: flag every gap ≥0.35s + every filler ("um", "uh",
   retake starts).
3. Cut all flagged gaps to ≤0.28s (P1 re-cut proved longest 0.28s after
   removing 13 gaps >0.33s); keep at most 2 dramatic pauses ≤0.30s, each
   motivated by the line.
4. Re-run the gap histogram as a QC metric on the exported file — the
   histogram, not a listen, is the proof.
5. Pair with `retention.py` leak taxonomy from the same repo for QC notes
   (hook leak / cliffs / slide — name what was said at each drop).

## Worked example (PWC)
P1 v9 voice track: 13 gaps >0.33s flagged, all cut; longest surviving gap
0.28s; gap histogram attached to the QC report. A 0.4s gap surviving in the
export FAILS the gate even if the video "sounds fine".

## PWC skin
Normal speed 1.0× everywhere — dead air is CUT, never sped up (speedup
reversed Nov 3–4; S01 is the sole 1.155× exception, already live).

## Variants (v9)
- **v9 · @millee.md, DfBBG0xPioN:** @millee.md DfBBG0xPioN — 0.1s deadspace rule, plain cuts, no click transitions. DIFFERS: 0.1s vs the part's 0.35s floor — discrepancy recorded, not reconciled; Q's standing 0.15s inter-word gaps sit between the two. _(source: bulk-c VARIANTS.md)_
- **v9 · @?, ?:** (see top of file — millee.md 0.1s rule.) _(source: bulk-c VARIANTS.md)_
- **v9 · @?, DfZ0UHsBdoK:** **V54 — ENGINE 5-agent team (DfZ0UHsBdoK):** roster-card device — five named agents as a persistent list, active one highlighted (→ batch1-jlee-engine); correction → saved rule card (→ jlee-correction-rule-loop); first-cut timer 89.3s → 68.8s, dead-air removal as a falling number (→ pipeline-deadair-gate); hook leaderboard (→ hooks-jev-hook-bank); PiP discipline — face stays on screen in a small rounded PiP through every full-screen panel (→ camera-split-layout). _(source: bulk-b VARIANTS.md)_
- **v9 · @mattphxm, DbZyaHNFUUf:** **V92 — @mattphxm Local Editor (DbZyaHNFUUf):** "Every silence longer than half a second, gone." (→ pipeline-deadair-gate — DISCREPANCY: Q's floor is 0.35s, his is 0.5s; recorded as observed, not reconciled); "the takes where you start again, it keeps the clean one" (→ pipeline-qc-gates); "reads back what I said and re-orders these sentences so that it's the tightest version" (→ pipeline-caption); "I don't have to open a single time line." The Local Editor tool itself: GAP (free, no login, but not in the harvest — license unknown, never installed). _(source: bulk-b VARIANTS.md)_

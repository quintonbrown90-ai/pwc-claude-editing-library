<!-- DO NOT edit parts/ directly from this file. Coordinator merges this draft into the target path. -->
<!-- Sources: BULK-DECODE-LOG.md batches 14, 17–18, 19 + per-video DECODE.md files listed below. -->
<!-- Existing canonical parts checked first: parts/hooks/hooks-hookscore-kill-gate.md exists (hook-only gate: 5 checks, STRONG ≥70 / OK ≥50 / <50 rewrite — a HOOK gate, not a whole-piece self-check gate). parts/render-pipelines/pipeline-qc-gates.md exists (Q's own QC gates, pass/fail, no number). No existing canonical part carries a numeric whole-piece self-check threshold — new part justified. This draft does NOT replace either existing part; it is the numeric-threshold companion to them. -->
# STRATEGY — self-check 95-gate: under 95 never ships (DRAFT — v8)

Source: FOUR independent sources for the self-check doctrine — the fourth
puts a NUMBER on the gate (BULK-DECODE-LOG.md batches 14, 17–18, 19):

1. **@charliehills** (batch 14, charliehills_De_3uyGiIJI, Mac-setup step 7 of
   8) — "Claude checks its own work / Before you ever see the render." Four
   checks: "Screenshot every 0.25s — 212 of 212 frames / Flag overlaps and
   crops, fix, check again / Clear of Instagram's buttons / As many graphic
   changes as best.mp4". Maps directly onto Q's QC gates (frame screenshots,
   overlap audit, safe zones, visual event ≤2s).
2. **@kingketo** (batches 17–18, DfKequOEQez / DfKgqktkZ-j, type-one-line
   step) — "Checked it: 11 of 11 passed" in the finished chat. 11 checks,
   all passed, before the human sees it.
3. **@charliehills** (batch 18, charliehills_DfSXS5fiP-i, graphic-designer
   closer) — "Claude checks its own work / Line 4 of your CLAUDE.md. Before
   you ever see it." The house rule it cites is line 4 of CLAUDE.md: "Check
   yourself. Fix what fails, then show me." Four checks on the kept graphic:
   "Title reads on a phone / Nothing tiny / No empty space / All 4 checks
   passed" / "All 4 pass. Here's the one you kept."
4. **@charliehills** (batch 19, charliehills_DfYK_ssiMnP, 27 Things slide
   07/08) — "Under 95 never ships / Six checks score every piece, and
   anything under 95 goes back." Verified in the per-video DECODE.md
   (research/video-harvest/instagram/charliehills_DfYK_ssiMnP/charliehills_DfYK_ssiMnP_DECODE.md).
   Six checks:
   1. "Checks it sounds like me, not AI" — voice-shape — YOU GET: "Pass or rewrite"
   2. "Scores posts against my best" — linkedin-score — YOU GET: "A score out of 100"
   3. "Scores every reel script" — reel-qa-reviewer — YOU GET: "95+ or rewrite"
   4. "Scores every video package" — youtube-qa-reviewer — YOU GET: "95+ or rewrite"
   5. "Scores every newsletter edition" — edition-rubric — YOU GET: "95+ or rewrite"
   6. "Rewrites anything under 95" — Claude — YOU GET: "The reasons, fixed"
   Close: "95 and up, it ships. / ManyChat, Metricool and Substack take it
   from there."

## The rule
Claude checks its own work before the human ever sees it. The check is a
SCORE, not a vibe: six checks score every piece; anything under 95 goes
back for a rewrite WITH the reasons fixed; 95 and up, it ships. The gate is
written into the standing rules (charliehills: line 4 of CLAUDE.md — "Check
yourself. Fix what fails, then show me."), so it fires on every piece
without being asked again. This is the FIRST source in the harvest to put a
number on the gate: 95.

## Executable steps
1. Write the gate into the standing rules file (CLAUDE.md line 4 shape):
   "Check yourself. Fix what fails, then show me." — the gate is a rule, not
   a request per piece.
2. Score every piece on the six checks (adapted to Q's lane — see Worked
   example): voice-shape (sounds like Q, not AI) / best-work score (against
   P1 v9, P2, P3) / script score / package score / caption score / rewrite
   with reasons fixed.
3. Under 95 → back. The rewrite returns WITH the reasons fixed, not just a
   new version — the reasons are the deliverable of the failed check.
4. 95 and up → ships. Nothing under 95 reaches Q's approval card, ever —
   the gate sits BEFORE the human, not after.
5. Keep the count visible: kingketo's "11 of 11 passed" and charliehills'
   "All 4 checks passed" are the proof line on the finished piece, not a
   claim.

## Worked example (PWC)
A P-pack take returns from Claude. The six PWC checks: (1) voice — sounds
like Q, not AI; (2) best-work — scores against P1 v9 / P2 / P3; (3) script —
hook lands a claim/curiosity in ≤2s with Q's face on screen; (4) package —
freeze gate (zero freezes ≥0.35s), overlap audit, safe zones, nothing over
the face, last-voice → end-card ≤~1s; (5) caption — word-exact Sky captions,
≤500 chars, WAITLIST dual-CTA line; (6) rewrite — anything under 95 comes
back with the reasons fixed. Score 95+ → Q's approval card. Under 95 → back
to Claude with the reasons. (Check list adapted from charliehills' six —
INFERRED mapping to Q's gates; his check NAMES are his, the PWC check
CONTENT is Q's standing QC gates.)

## PWC skin
Palette teal #14A886 / gold #FEE238 on navy #00214E, no red. The 95 number
is charliehills', not Q's — see "Needs Q's ruling". Q's existing QC gates
(pipeline-qc-gates.md) are pass/fail; this draft adds the numeric threshold
as a companion, it does not replace them. Keyword flow live before posting
(ENGINE Step-0 gate) — the 95-gate is a quality gate, not a posting gate.

## Discrepancies — carried as observed, NOT reconciled
- **Check counts differ across the four sources:** 4 checks (charliehills
  batch 14 video-edit step 7) vs 11 checks (kingketo "11 of 11 passed") vs 4
  checks (charliehills batch 18 graphic-designer closer) vs 6 checks
  (charliehills batch 19 95-gate). Same doctrine, different check counts —
  the count is per-system, the rule (check before showing) is shared.
  Recorded as observed.
- **The 95 threshold appears only in the 27-things system.** The other three
  sources check pass/fail with no number. The number is not confirmed by a
  second source. Recorded as observed.
- **Score scales differ:** linkedin-score gives "A score out of 100";
  reel-qa-reviewer / youtube-qa-reviewer / edition-rubric give "95+ or
  rewrite". One scale is 0–100, the other is a pass line at 95. Recorded as
  observed.

## Gaps
- No source in the harvest shows HOW a score is computed (no rubric weights,
  no per-check scoring formula) — the six checks are named with their YOU
  GETs only. A PWC 95-rubric would have to be authored from Q's QC gates,
  labeled INFERRED.
- Kingketo's 11 checks are named only as a count ("11 of 11 passed") — the
  11 individual checks are NOT in the harvest.

## Needs Q's ruling (flagged, NOT adopted)
- Adopt 95 as Q's numeric ship threshold, or keep Q's QC gates pass/fail
  with no number? The 95 is one creator's number, confirmed by no second
  source. Q's call.
- If adopted: which six PWC checks (the Worked example above is a draft
  mapping, INFERRED — Q's QC gates re-expressed as six scored checks)?

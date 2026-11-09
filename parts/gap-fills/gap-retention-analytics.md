<!-- PART: gap-fills/gap-retention-analytics.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# GAP-FILL — Retention analytics [Q didn't ask, mastermind added]

Source: retention read (Q's standing gate, Nov 3) + martinwang's
retention-dip rescue case (9.3K → 2.5M views, single case — needs a
second example) + Sky/Herk pacing measurements. Mark: GAP-FILL.

## The rule
Retention data is a diagnosis, not a score. Every drop-off point names
the fix.

## How to read it
- **0–2s drop:** the hook failed (claim not landed, face not on screen,
  proof not visible). Fix the hook, not the middle.
- **Midpoint drop:** the second loop never opened (Cater's double open
  loop). Fix: open loop #2 before the midpoint.
- **Gradual slide:** visual events are too far apart (>2s between
  events) or the rhythm went uniform (template tell — HUMAN-MADE CHECK
  fails). Fix: a visual event every ≤2s, vary the caption treatment.
- **End drop (last 3s):** dead air after the last word (ending dead-air
  gate: end card ≤1s after last voice) or a closed ending with no chain
  to the next watch. Fix: card on time + a chain line.
- **A spike UP at one moment:** that beat is the video's best device —
  steal it for the next video (this is the 5X outlier feed in miniature).

## What to change per drop-off (the fix table)
| Drop point | Most likely cause | Fix |
|---|---|---|
| 0–2s | Hook = greeting / no claim | Rewrite from a measured pattern; proof at 0:00 |
| 2–10s | No proof after the claim | Show the document/screen now, not later |
| Midpoint | No second loop | Open loop #2 before the midpoint |
| Steady slide | Uniform rhythm / frozen device | Vary captions, add a device, cut the freeze |
| Last 3s | Dead air / closed ending | End card ≤1s after last word; chain to next |

## Retention-dip rescue (martinwang case, single example)
A video stuck at 9.3K views was re-edited at the dip points (new hook,
devices at the drop-offs) and reached 2.5M. The lesson: a flop is
usually 2–3 fixable moments, not a bad video. Re-edit the dips before
deleting the post.

## Executable steps
1. After every post, read the retention curve at 24h and log the worst
   drop-off point + the fix in SKY-SCORE.md (if it touches a Sky device).
2. A video with a 0–2s drop gets a new hook and a re-post decision from
   Q — never silently re-posted.
3. The week's worst drop-off pattern goes to the Content Strategy
   Specialist as a topic ("why people leave at 0:08").

## Worked example
BW-04 v1 (Nov 2): a 1.3s freeze at ~36.7s + a 1.1s freeze at ~40.0s —
decode-clean but played as "the video stopped." The freezedetect gate
(zero freezes ≥0.35s) exists because retention data can't explain a
freeze — the export QC catches it first.

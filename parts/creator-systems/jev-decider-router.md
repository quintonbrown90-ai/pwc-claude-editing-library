<!-- PART DRAFT (v9 bulk-c): creator-systems/jev-decider-router.md | UPLOAD: SKILL + GITHUB | MAX: 50KB -->
# CREATOR SYSTEMS — the decider router: an AI that never writes, only decides (@the.operator, 7-slide set)

Source: @the.operator reels Dd4duWEiLfM / Dd4duWeiKSm / Dd4duXCiF2H /
Dd4duXWCLAq / Dd4duXhCNut / Dd4duXiiIhS / Dd4duZoiFXZ (JEV carousel, Nov 2026)
— INFERRED reconstruction from the visible slides. JEV itself is a
third-party product, NOT adopted; the setup guide is GATED behind follow +
comment JEV — never chased. The architecture is the steal, not the product.

## The rule
"JEV is an AI that never writes. It only decides." Split the jobs: Claude
writes; the router routes and checks. The decider works NEXT TO Claude, not
instead of it. Every decision is one of three question types — Which one? /
How much? / Is this true? — and the answer is always picked from a list you
define, with a confidence score. It can't return an answer that isn't on your
list.

## Executable steps
1. **Writer vs decider:** Claude writes (scripts, captions, edits). The
   decider only routes: which hook, which effect, which variation — picked
   from Q's defined lists (hook bank, effect library, look menu).
2. **Three question types:** every routing decision is Which one? (pick from
   the list), How much? (a number / threshold), or Is this true? (a check
   against a source). If a decision isn't one of the three, restate it until
   it is.
3. **Confidence score on every answer:** "The percentage is the product."
   Every answer includes a calibrated confidence score (90% sure means right
   about 90% of the time). Q picks the threshold for what runs on its own;
   below the threshold, ask a human.
4. **List-bound:** the decider picks from answers you define and returns one,
   with its score, in under half a second. No generated text from the decider
   — generated text is the writer's job.
5. **Good-for / not-for, stated:** say what the router is good for (sorting
   messages, qualifying leads, flagging content, guarding AI agents, picking
   the right model) AND what it's not for (writing, math, coding, questions
   without a fixed list of answers). The not-for is the honesty; the bound is
   the trust.
6. **Worked example per route:** prove each route with one real call — "a
   support ticket, sorted in one call" (three questions, one result).

## Worked example (PWC)
Hook routing: the decider gets Q's hook bank + the script, returns one hook
with a confidence score; below threshold (e.g. <70) Muse picks instead.
Effect routing: transcript line → decider picks one effect from the 44-effect
library, score attached; low scores go to the human. Same shape as the claw-
machine picker (the router picks) — this part adds the confidence gate.

## Human-made check
A routing decision with no score is not a decision — it's a guess. Scores are
calibrated on Q's own outcomes, never asserted.

## PWC skin
Teal/gold on navy. Confidence shown as a gold percentage chip; low-confidence
routes flagged in gold (NO RED). Nothing over the face.

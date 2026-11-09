<!-- PART: creator-systems/jlee-correction-rule-loop.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# CREATOR SYSTEMS — Correction→rule loop (Tier S, @jlee.mov)

Source: @jlee.mov reel DeuCZVNCuDI, 0–53.5s (MEASURED). "wrong → why → a
rule" (VERBATIM, plain text file read before the job runs again). 30+ rules.
Worked examples: "just pick one and go with it" (one hook ever since);
invented "45–60s" limit caught ("where's that from?") → scripts timed off
his actual speaking speed. Runnable checks: voice check flags off-voice
lines, frame-rate check BLOCKS render (render.py "2xfps DENY / nothing
renders"). Doctrine (VERBATIM): "A tool makes the same mistake on Monday
that it made last Friday. A system makes it once, and then there's a rule
for it."

## The rule
Every mistake becomes a rule, written in a plain text file, read before the
job runs again. The loop is three steps (wrong → why → a rule) and the file
is the memory. The runnable checks are the enforcement: a check that BLOCKS
the render is worth more than a guideline.

## Executable steps
1. The rules file: one plain text file per job (e.g. `rules_hooks.txt`,
   `rules_captions.txt`, `rules_render.txt`). Each rule is one line: the
   mistake + the rule ("Invented a 45–60s limit → scripts are timed off Q's
   actual speaking speed, never a guessed limit").
2. The loop: when a mistake is caught (by the reviewer, by QC, by Q), the
   fixer writes (a) what went wrong, (b) why it happened, (c) the rule —
   then appends it to the file. The next run reads the file first.
3. Runnable checks (the enforcement): (a) VOICE CHECK — flags any line that
   is not in Q's voice (his words, his phrasing, second-person framing);
   (b) FRAME-RATE CHECK — blocks the render if the frame rate is wrong (his
   "2xfps DENY" — the render does not happen, it is not warned about);
   (c) FACE CHECK — blocks the render if any graphic covers Q's face (Q's
   brand law as a runnable check).
4. The rules file is the system's memory — the same job as Q's AGENTS.md
   "Learned" section, but per-job and machine-read.

## Worked example (PWC)
Mistake: a board cross-faded over Q's face (BW-04 verdict board). Why: the
builder used a cross-fade transition on a board over footage. Rule: "Boards
over footage cut in hard — no cross-fades, no light-washes" (already Q's
rule, Nov 2). The render check now blocks any board with a cross-fade
transition. Keyword WAITLIST.

## Human-made check
The rule is written by a human (Muse) after the fix is verified — the loop
is only as good as the rules in it, and a bad rule (too broad, wrong cause)
is worse than no rule.

## PWC skin
Q's standing rules ARE the seed rules file (freeze gate, transition gate,
ending dead-air gate, lip-sync check, face rule). The loop grows them.

## Variants (v9)
- **v9 · @?, V8-43:** V8-43 — "Calm it down": subtraction direction for chaotic V1s → jlee-correction-rule-loop.md _(source: v9_verification.md)_
- **v9 · @?, V8-109:** V8-109 — Fix by talking: "you left a basically in at the start of that line, cut it" → jlee-correction-rule-loop.md _(source: v9_verification.md)_
- **v9 · @tunestechtips, Dfax2Wck4KF:** @tunestechtips Dfax2Wck4KF — "Claude wrote lessons in its notes, then made the same mistakes anyway": writing a lesson down doesn't change behavior — the lesson must become a rule (in the skill, in the template, in the QC gate). DIFFERS: names the failure mode the part's rule prevents. (Benchmark format 10v10 / 9 runs / scoreboard: same shape as Q's hook tests; Minecraft harness itself not adopted.) _(source: bulk-c VARIANTS.md)_
- **v9 · @opusjake, DfbIFWitQzT:** @opusjake DfbIFWitQzT — describe-it mod model: "You just describe any change you want, and Claude rebuilds it directly inside of [the video]." DIFFERS: the revision model (describe → rebuild in place). (Game-cloning itself: FLAGGED, out of Q's lane.) _(source: bulk-c VARIANTS.md)_
- **v9 · @shihui.travels, De_2J7AM-Sp:** @shihui.travels De_2J7AM-Sp — "Send all my feedback in one message with timestamps" (saves tokens; every re-render uses tokens). DIFFERS: the one-message + timestamps feedback format. _(source: bulk-c VARIANTS.md)_
- **v9 · @?, DfZ0UHsBdoK:** **V54 — ENGINE 5-agent team (DfZ0UHsBdoK):** roster-card device — five named agents as a persistent list, active one highlighted (→ batch1-jlee-engine); correction → saved rule card (→ jlee-correction-rule-loop); first-cut timer 89.3s → 68.8s, dead-air removal as a falling number (→ pipeline-deadair-gate); hook leaderboard (→ hooks-jev-hook-bank); PiP discipline — face stays on screen in a small rounded PiP through every full-screen panel (→ camera-split-layout). _(source: bulk-b VARIANTS.md)_
- **v9 · @jayantcreates.ai, DfaQ4sdk7Yp:** **V55 — @jayantcreates.ai 5 jobs (DfaQ4sdk7Yp):** "Every correction becomes a rule" (→ jlee-correction-rule-loop); "I say yes and it posts" — the approval gate, the correct version of auto-posting; A/B trial-reel doctrine ("same idea, different hooks, in front of people who don't follow me yet. The winner goes to my main page." — also tenfoldmarc-3-hook-trial-reels). _(source: bulk-b VARIANTS.md)_

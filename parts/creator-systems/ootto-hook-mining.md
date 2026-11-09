<!-- PART: creator-systems/ootto-hook-mining.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# CREATOR SYSTEMS — Ootto Hook Mining (Tier S)

Source: Ootto-AI/claude-content-skills repo (MIT) — `skills/hook-mining/`
in `uploads/QUARANTINE/ootto-content-skills/` (SCAN PASS). The only code
file in the repo: `mine_hooks.py` — pure local CSV processing, read in full
Nov 8, 2026 (no network, no env, no exec, no base64). The skill mines hooks
from a CSV of the creator's own posts.

## The rule
The creator's own hooks, mined — a CSV of past posts (hook text + views +
comments) is processed locally into a ranked hook list: which openers
actually worked, which flopped. The creator's own data is the hook library.

## Executable steps
1. Input: a CSV of Q's posted reels (post ID, hook verbatim, views,
   comments, retention where measured) — built from the harvest + IG
   insights.
2. The miner (local script, MIT source, ported): ranks hooks by
   performance, clusters them by type (claim / question / contrast / list /
   story), and outputs the top 10 + bottom 10 with the pattern that
   separates them.
3. Output: a hook leaderboard (same device as jlee's ENGINE hook
   leaderboard — the two parts share the leaderboard visual) + a "never
   again" list (the bottom 10, with the reason each failed).
4. The leaderboard is re-mined monthly — the hook library is living, not a
   one-time list.

## Worked example (PWC)
Mine Q's launch hooks → top: "BRANDS ARE PAYING SMALL CREATORS LIKE YOU"
(claim + you-framing); bottom: a question-hook that opened with "Did you
know..." (no claim, no face in the first 2s). The pattern: claim-hooks beat
question-hooks 3:1. Next week's hooks are all claims. Keyword WAITLIST.

## Human-made check
The miner ranks, it does not write — new hooks are still written by Q/Muse,
then checked against the mined patterns.

## PWC skin
Leaderboard in PWC palette; Q's hooks only. Credit: Ootto (MIT).

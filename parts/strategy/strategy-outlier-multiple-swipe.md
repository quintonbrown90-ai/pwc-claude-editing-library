<!-- PART: strategy/strategy-outlier-multiple-swipe.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# STRATEGY — Rank by outlier multiple, not raw views (@nategold.ai)

Source: nategoldai/instagram-agent repo (MIT, SCAN PASS) — /ig-viral +
/ig-audit in `uploads/QUARANTINE/rundown-b-repos/nategold-instagram-agent/`.
"Raw views prove nothing. An account with two million followers getting
400,000 views just had a slow Tuesday. An account with four thousand
followers getting 400,000 views found something."

## The rule
Outlier multiple = views ÷ that account's own recent median. Over 3x is a
signal; under 1.5x is a normal day. Pick accounts within ~10x of your own
size. This is the research method behind Q's swipe file and the audit behind
his retention read.

## Executable steps
1. Sample: 4 direct (same niche, further along) + 4 adjacent (different
   niche, same audience — formats get borrowed here first) + 2–4 outsized
   (format only).
2. Record per reel: account, followers, median (last 12 reels), views, hook
   word-for-word, on-screen card, length, CTA.
3. `swipe.py` ranks by multiple, names the hook formula (same 26 as the
   hookscore part), scores each hook, and prints what sets the top third
   apart from the bottom third + the unclassified rows ("the most valuable
   part of the output").
4. /ig-audit adds: rank by outlier multiple AND sends per reach, not views;
   top five vs bottom five — what separates them (hook formula? 3-second
   hold? "posts where you were the one who looked bad: mean 8.1x vs 0.9x"
   — their example of a finding).
5. Monthly swipe run → swipe.md (top 3 formulas → write Q's own version of
   each via /ig-reel with the formula id picked) → audit after every 30
   posts (median views, top 5 vs bottom 5, 3-second hold).
6. Never hand back "make a reel like this one" — hand back a hook line Q
   could say tomorrow.

## Variants folded in (V7)
- **CCC outlier-score table** (@createcontent.club Dd9DZ8uDV93): same math
  (views ÷ median), different precision — CCC shows ESTIMATED multiples
  (~6–8x est.) on a generated list; this part uses MEASURED multiples from
  real data. Rule for Q: estimated multiples are a brainstorming device
  only — anything published uses measured multiples or no multiple at all.

## Safety note (PUBLISHED in the skill, aligns with SAFETY.md)
"Never log into Instagram for the user… This is reading, not scraping. Ten
accounts, about a dozen reels each, at human speed. Automated collection at
scale breaks Instagram's Terms of Use."

## Worked example (PWC)
Monthly swipe on 6–12 accounts (PWC niche + adjacent creator-coach niches
+ outsized format-only): Q's own median is the baseline for his hooks; a
hook that beats Q's median 3x is a formula to repeat. Top 3 formulas →
Q's own versions, filmed next week. Keyword WAITLIST.

## Human-made check
The multiple ranks; it does not write. The hook line handed back is Q's
words, in Q's voice.

## PWC skin
Q's median as the baseline; measured multiples only when published.
Credit: nategold.ai (MIT).

## Variants (v9)
- **v9 · @siddhantt.ai, Detm0uDkyBA:** @siddhantt.ai Detm0uDkyBA — "Ranked by how far each video beat its own channel" + "Claude scans 1,283 videos" (16 searches, every channel's last 10 uploads, 4 minutes). DIFFERS: the relative-rank rule confirmed by a second independent source (same as charliehills' 5× usual views). _(source: bulk-c VARIANTS.md)_
- **v9 · @siddhantt.ai, Detm0uhkwZS:** @siddhantt.ai Detm0uhkwZS — scan counters "1,283 | 4 min": volume is the proof, time is the speed. (See prompts-router-intake for the ask.) _(source: bulk-c VARIANTS.md)_
- **v9 · @leogrundstrom, DfVFq1Ys1SV:** **V98 — @leogrundstrom pairing (DfVFq1Ys1SV):** HyperFrames + video-use as ONE pitch — engine for built graphics, editor for cutting talking-head takes (→ pipeline-stockton-one-prompt-render); GitHub-proof card — show the live star count (78k) instead of claiming popularity (→ strategy-outlier-multiple-swipe); Blender short-film proof (→ blender-free-3d). _(source: bulk-b VARIANTS.md)_

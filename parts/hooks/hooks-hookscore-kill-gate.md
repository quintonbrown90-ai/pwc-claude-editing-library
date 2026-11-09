<!-- PART: hooks/hooks-hookscore-kill-gate.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# HOOKS — hookscore kill-gate (MIT, SCAN PASS)

Source: Jakeschincariol/instagram-agent-skill `hookscore.py` (MIT, SCAN PASS
— stdlib only, no network, no keys). DISTILLED in
research/repo-sites/opusjake-instagram-agent-skill/. 26 hook formulas listed
in the same repo (names only — formulas are the kill-gate's input, not a
copy-paste list).

## The rule
Score every hook BEFORE shooting. 5 checks: LENGTH (5–12 words) /
SPECIFICITY / STAKES / FRONTLOAD / ADDRESS. Dealbreakers flag instantly.
Overall = mean×0.6 + min×0.4 − 15×flags. STRONG ≥70 / OK ≥50 / below 50 =
rewrite, do not shoot. Author's own limit: AUC 0.83 bad-vs-real but 0.56
hit-vs-miss — it KILLS bad hooks, it cannot crown winners. Use it as a gate,
never as a ranking.

## Executable steps
1. Write 10 hooks for the video (same claim, new wording — winners re-shot).
2. Run the 5 checks on each; kill everything under 50.
3. Shoot the highest STRONG hook; if none clears 70, rewrite the claim —
   never shoot an OK hook and hope.
4. Pair with the beats thresholds from the same repo: HOOK_WINDOW 3.0s,
   MAX_BEAT 4.0s, ABSTRACT_RUN 3, default 165 wpm; caption preview 125 chars
   (Q caps captions at 500 chars — the 125-char preview is the feed cut).

## Worked example (PWC)
"Your page is running at 0/4 power until these 4 systems are in." LENGTH 12
✓ / SPECIFICITY (4 systems) ✓ / STAKES (0/4 power) ✓ / FRONTLOAD ("your
page" first) ✓ / ADDRESS (you) ✓ → STRONG. "In this video I'll show you
some tips" → LENGTH ✓, everything else fails → killed before shooting.

## PWC skin
Hooks use Q's TRUE claims (collective framing for earnings); never invent a
number to pass SPECIFICITY.

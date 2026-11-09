<!-- PART: hooks/hooks-hookscore-26-formulas.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# HOOKS — 26 hook formulas + hook scorer that really runs (MIT, @nategold.ai)

Source: nategoldai/instagram-agent repo (MIT, SCAN PASS Nov 8, 2026) —
`hooks.json` + `hookscore.py` + `beats.py` in
`uploads/QUARANTINE/rundown-b-repos/nategold-instagram-agent/`. Tested on 74
real hooks: AUC 0.83 separating real hooks from deliberately-bad ones, AUC
0.56 separating a good creator's hits from their misses — the README states
both numbers; the scorer catches greetings/preambles/empty hooks, it does
NOT predict which of two decent hooks travels ("Trust the retention graph
over this script").

## The rule
26 formulas, each with template, filled example, on-screen version, what
it's for, how it goes wrong, and a `match` regex so the same vocabulary
names a hook found in the wild. Score the hook BEFORE filming — if the best
is under 50, the hook isn't ready and editing won't fix it.

## The 26 formulas (MEASURED names)
Cost Confession · Negative Command · Nobody Tells You · The Replacement ·
Time Collapse · The Receipt · Wrong Way Right Way · Insider Leak · The
Steal · If This Then Watch · Numbered With A Favourite · The Objection ·
Before And After On Screen · The Callout · The Flop Record · The Verbatim
Question · Head To Head · Cold Open Demo · The Deadline · Permission ·
Mid-Sentence Start · Contrarian Flip · The Statistic · The Reveal · Someone
Else's Result · The Superlative.

## The scorer (hookscore.py, 5 checks, 0–100)
Length sayable in under 3s · concrete marker · something at stake · payload
at the front · viewer aimed at. `beats.py` times the script before filming
and flags: hook over 3s, any beat over 4s, stretches with nothing concrete,
no loop.

## Executable steps
1. Write 3 hooks from 3 different formulas → score all 3 with hookscore.py
   → if the best is under 50, the hook isn't ready and editing won't fix it
   → write the script on the winner → time it with beats.py → humanize →
   film.
2. Log every hook (date, formula, first line) so /ig-audit has history.
3. The loop rule ("repeat a word from the hook so the replay flows") is a
   new device for Q's endings — the last line echoes a hook word so the
   loop replays cleanly.

## Worked example (PWC)
Three hooks for a WAITLIST reel: Cost Confession ("I wasted 4 years
posting for free"), The Receipt ("$92,000 from 5 emails — here's the
receipt"), Time Collapse ("90 days from free to deal-ready"). Scores:
41 / 78 / 66 → film The Receipt. Keyword WAITLIST.

## Human-made check
Distinct from `hooks-hookscore-kill-gate.md` (opusjake's kill-gate) — this
part is the formula library + scorer, that part is the kill threshold. They
pair: score with this, kill with that. The scorer catches bad hooks; it
cannot crown winners — the retention graph decides.

## PWC skin
Hook rules are Q-compatible already (spoken line and on-screen line written
separately; on-screen ≤6 words; hook card up at frame 1; safe zone — theirs
is y>230 / y<1440 with the right 230px empty, Q's is x 70–930 / y 280–1480
— use Q's zone; "never make things up — no invented stats, clients,
revenue or results"; "skip the intro"). Add Q's gates on top: hook lands a
claim/curiosity in ≤2s with his face on screen; nothing over the face;
teal/gold on navy. Credit: nategold.ai (MIT).

## Variants (v9)
- **v9 · @?, V8-56:** V8-56 — Paradox-first script formula: paradox → hooks-hookscore-26-formulas.md _(source: v9_verification.md)_
- **v9 · @?, V8-160:** V8-160 — 21 proven hook formulas as a dedicated skill; 11 skills as a team (wXV5Ah6OVI0, Johann Sathianathen) → hooks-hookscore-26-formulas.md _(source: v9_verification.md)_

## Variants (v10)
- **v10 · @kayvon.ai, DfedDuTKfih:** **Threat-hook frame + price anchor + hands-on test proof:** open with who is SCARED of the thing, not what the thing is — "I bet Adobe's lawyers are sweating right now, because somebody just remade seven of their apps and put every single one of them out for free." The fear is the hook. Price anchor spoken twice (once at the test, once at the close): "$780 a year" / "$70 a month" vs free — the anchor is the value. Hands-on test proof: "I spent all of yesterday testing these out... my PSD files opened like nothing changed" — the failure he expected, the result. NOT the apps (not downloaded, not scanned) and NOT the link (gated, comment ART → DM). Discrepancy recorded as observed: spoken "seven apps" vs on-screen "Thirteen apps. One craft." — the suite grew, or the count is loose. Not resolved. _(source: Batch 8, v10)_

## Variants (v11)
- **v11 · @createcontent.club, DfM9DV7GZY3 (CAROUSEL — "To get 1M views, you need 3 hooks", caption-level only):** **The 3-hook taxonomy: spoken / text / visual — hook MODALITIES, three channels firing at once.** "To get 1M views, you need 3 hooks. Spoken hook, text hook and visual hook." The taxonomy is the steal: every video needs all three channels at the open — a spoken hook (already Q's rule: a chosen voice says the exact drop-in title hook up front), a text hook (the on-screen title), and a visual hook (the opening visual event). It maps cleanly onto Q's standing hook standards (hook lands a claim/curiosity within 2s, Q's face on screen) — the carousel's value is the taxonomy, not new rules. "1M views" is the creator's claim, not a verified outcome; the guide itself is gated behind HOOK, never chased, and what each hook type looks like in practice is NOT VISIBLE / GAP (slides not retrieved). **Explicitly distinct from the Nov 2 reel "Four levels of hooks to go viral" (DfPmwIulFP6):** that reel teaches hook TIERS (levels of strength) — a ranking, not a channel list — and it is NOT decoded. Do not conflate the two models: 3 hooks = modalities (all three at once), 4 levels = tiers (how strong). _(source: Batch 9, v11)_

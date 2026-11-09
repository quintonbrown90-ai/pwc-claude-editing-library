<!-- PART: captions/captions-ig-humanizer.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# CAPTIONS — The humanizer: strip the machine fingerprint (@nategold.ai)

Source: nategoldai/instagram-agent repo (MIT, SCAN PASS Nov 8, 2026) —
`humanize.py` (cleans) + `detect.py` (scores on a five-check panel) in
`uploads/QUARANTINE/rundown-b-repos/nategold-instagram-agent/`. This is the
executable version of Q's HUMAN-MADE CHECK — run every script and every
caption through humanize + detect before filming/posting.

## The rule
Strip the machine fingerprint before anything goes out. What gets fixed
automatically vs what gets FLAGGED for a human rewrite — the split is the
system.

## What gets fixed automatically (humanize.py)
- Invisible characters (zero-width spaces, joiners, soft hyphens, BOMs, tag
  characters — "keyboards don't type these… the most mechanical trace in
  generated text").
- Typography (em dash → comma, en dash → hyphen, curly quotes → straight,
  ellipsis → three dots).
- The slop list — 154 stock words/phrases with plain swaps (delve,
  leverage, robust, seamless, crucial, "in today's fast-paced world") plus
  the Instagram block ("stop scrolling", "in today's video", "follow for
  more", "tag someone who needs this", "the algorithm loves", "run don't
  walk").

## What gets FLAGGED, not rewritten (detect.py)
"It's not just X, it's Y", groups of three, one-word rhetorical questions
("The result?"), "in this video I'm going to show you", emoji bullet lists,
three+ shouted words, walls of hashtags, reflex bait.

## The five checks (0–100, higher = more human)
BURSTINESS, SPECIFICITY, SLOP DENSITY, FINGERPRINT, VOICE. Verdict = 60%
average + 40% weakest check; PASS needs 70+ overall and no check under 55.
Honest limit (PUBLISHED): "These are five local heuristics… not GPTZero,
Originality, Copyleaks, Winston or Turnitin… never tell them their text is
undetectable."

## /ig-caption adds
The caption's job (ask / proof / search), Line 1 = the ask in the first 125
characters the feed shows, hashtags up to five (cap moved 30 → 5 on Dec 18,
2025), search terms matter more than hashtags now.

## Executable steps
1. Draft script/caption → `humanize.py draft.txt -o clean.txt --report` →
   rewrite every flagged structural line by hand → `detect.py draft.txt
   clean.txt` → not PASS? fix the weakest check named and go again (two
   rounds normal; five means the draft was written to a formula — write a
   new draft).
2. Show Q the cleaned text AND the score together, never just the score.
3. Keep the slop list editable: if Q has a word he always says that the
   list strips, remove it from the file.

## Worked example (PWC)
Caption draft: "In today's fast-paced world, creators must leverage robust
systems to unlock seamless growth. Stop scrolling — the algorithm loves
this." → humanize strips the slop → "Creators under 10K go from posting
for free to deal-ready in 90 days. Comment WAITLIST and I'll send you the
first 7 days." → detect PASS 82. Keyword WAITLIST.

## Human-made check
Q's captions are already short, SEO-focused, ≤500 chars with the keyword
CTA + dual-CTA profile line — the humanizer is the gate that keeps them
sounding like Q, not like a template.

## PWC skin
Q's caption law on top of /ig-caption; Q's words in the slop list's
keep-list. Credit: nategold.ai (MIT).

## Variants (v9)
- **v9 · @zachdoesai__, DfZnZYIuvp6:** @zachdoesai__ DfZnZYIuvp6 — the slop detector concept: a "62 signs" checklist scanning a cut for AI tells (flat captions, template rhythm, dead space, generic B-roll), fixed before Claude calls it done. DIFFERS: a checkable list form of the human-made check, not a new check. _(source: bulk-c VARIANTS.md)_
- **v9 · @leadgen, DfAuhUwyaN8:** **V105 — @leadgen slop doctrine (DfAuhUwyaN8):** "If you don't give it specific direction about what components should look like, it designs slop" (→ captions-ig-humanizer — Q judged Claude's edits "cheap AI slop" Nov 7; the direction IS the edit); UX-is-hard rule (where things go / the journey — AI is bad at it). _(source: bulk-b VARIANTS.md)_

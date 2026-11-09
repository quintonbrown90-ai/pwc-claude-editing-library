# SCRIPTWRITING — Viral-rewrite skill: Bradford's layers + CCC's mechanism (INFERRED reconstruction)

Source: @createcontent.club — canonical reel DfKT7ZLCYg__ "Claude can script any viral video" (parent-decoded, Batch 6) + @bradfordmarais content architecture (Batch 5 drafts: content-architecture-spec.md, brand-brain-part.md, script-structures-part.md, quality-gate-spec.md). CCC's system is gated behind comment SKILL → DM. NOT chased, bought, or scraped. The FLOW below is rebuilt from visible specs only (transcript + on-screen Claude session), labeled INFERRED. His words are quoted; the rest is reconstruction.

## The rule
Bradford gave the ARCHITECTURE — three layers that must exist before any script is requested (Brand Brain → Playbook → Quality Gate), because without them "your scripts come out super generic and sound like AI slop." CCC gives the MECHANISM — a skill that rewrites any viral reel into your own script. The two combine into ONE scriptwriting skill: **Bradford's layers are the precondition; CCC's rewrite flow is the run.** Neither works alone: the rewrite flow without the Brand Brain returns the source creator's value in your voice (a copy); the layers without the rewrite flow leave you staring at a blank page (a brainstorm). Together: a proven structure in, your value out.

CCC's flow, from the transcript + the screen recording (DfKT7ZLCYg__):
1. Invoke: `/ccc-viral-scripter` + the link to a reel that worked in your niche (their example: a 3M-view reel in their niche).
2. The skill **pulls the transcript and caption** for that reel (frame f_014: "Pulling the transcript and caption for that reel, and loading your scripting knowledge base from Notion.").
3. It **double-checks the video really outperformed** (transcript: "double check the video really outperformed").
4. It **loads a scripting knowledge base from Notion** (their stored scripting knowledge).
5. It **writes your version with the same hook, the same structure, and the same length, but changes the value to what you would actually say.**
Output is time-coded: [APPLICATION, 22–29s], [CTA, 29–33s] (frame f_019 shows the full rewritten script).

## The layers + the mechanism, combined (this part)
| Step | Bradford's layer (Batch 5) | CCC's mechanism (this batch) | Q's version |
|------|---------------------------|------------------------------|-------------|
| 0 — Precondition | **Brand Brain** (3 files: who you are / what you sell + where it's going / how you talk) | — | Q's 3 files (see `brand-brain.md`). No rewrite runs until these exist. The Brain is what makes the "new value" YOUR value. |
| 0 — Precondition | **Playbook** (1,000-hook bank + 12 script structures) | **Knowledge base load** (Notion) | Q's Playbook IS the knowledge base: the 12 structures + the scored hook bank + the hook/structure library (PROMPTS.md §1–17). The skill loads Brain + Playbook before writing — never from a cold prompt. |
| 1 — Input | Brain dump (voice, 15 min, no AI) → go deeper on the exciting idea | **Paste a viral reel link** in your niche | EITHER input is allowed: a brain dump OR a viral reel link. A reel link without a Brain dump still needs the Brain loaded (step 0) — the link is the structure source, never the value source. |
| 2 — Pull | — | **Pull transcript + caption** | Claude pulls the source reel's transcript + caption. This is research input, not copy input — see the Boundary below. |
| 3 — GATE | **Quality Gate** (runs on scripts, hooks AND ideas, before Q sees anything) | **Verify it really outperformed** | The OUTPERFORMANCE GATE — see the gate section below. Runs BEFORE any rewrite. A source that fails the gate is dropped, not rewritten. |
| 4 — Write | Claude structures from Brain + Playbook → human line-edit (taste pass) | **Write your version: same hook, same structure, same length, new value** | Claude writes from Brain + Playbook + the source's structure. Then the Quality Gate scores the draft (hook ≥70 STRONG, claims verified, voice check, Brain check, structure check, retention read) and Q line-edits for taste. |
| 5 — Output | Vetted draft reaches Q | **Time-coded script** | Standard script shape — see the output format below. |

## The outperformance gate (fold-in target for `quality-gate.md` at consolidation)
**Only rewrite proven performers. The check runs before any rewrite — a source that fails is dropped, never rewritten anyway.**

What "really outperformed" means (INFERRED — CCC shows the check happening, not its internals; the math below is the library's own outlier-multiple math, applied here):
1. **Measure the source's multiple:** source reel views ÷ the source creator's median reel views (same math as the outlier-multiple swipe, Nate V7 Part 3, and CCC's own strategy skill, which scores ideas ~6–8x). The multiple is MEASURED from real numbers, never estimated.
2. **Threshold (INFERRED — needs Q's ruling at consolidation, flagged not adopted):** ≥2x the creator's median. A reel at 2x+ its creator's usual performance has proven its structure; a reel at ~1x is just a normal post, however big the absolute number looks. (A 3M-view reel from a creator whose median is 3M proves nothing. A 300K-view reel from a creator whose median is 100K proves the structure works.)
3. **Fail = drop the source.** Pick a different reel. Do not lower the threshold to keep a source you like — the gate is a gate, not a polish pass. Same as the hookscore kill-gate: below threshold = do not shoot.
4. **Record the evidence:** the gate output is one line in the script header — source URL, source views, source creator median, multiple. A rewrite without that line is unvetted and fails the Quality Gate (check 2, claim verification).

Why the gate matters for Q: his launch posts must bridge free value → WAITLIST. A rewrite of an unproven reel inherits an unproven structure — the script can be perfect and still not move. The gate is what makes "viral rewrite" a system instead of a copy machine.

## The standard script output shape (time-coded)
Every script this skill writes comes out in this shape — it matches Q's Authority-30 / YAP30 script format (section + time structure), so rewrites drop straight into the existing script packs:
```
[HOOK, 0–3s]
<the hook — spoken up front, timed to the title words dropping in; Q's face on screen>

[APPLICATION, mm–ss]
<the value — Q's own teaching, in Q's voice, in the source's structure>

[CTA, mm–ss]
Comment <KEYWORD> + the dual-CTA profile line
```
- The section labels are the source's structure, not a template: if the source reel has more beats (e.g. a proof beat, a contrast beat, a worked-example beat), they appear as additional time-coded sections between HOOK and CTA, each named for what it does ([PROOF, mm–ss], [CONTRAST, mm–ss], [EXAMPLE, mm–ss]). The shape is HOOK → value beats → CTA; the middle flexes to the source's structure.
- Times are the TARGET times for Q's version (same length as the source — the rewrite keeps the source's length), not the source's times. If the source is 25s, Q's version is 25s.
- CCC's demo output (f_019, VERBATIM-FRAME — the shape example, their words): "[APPLICATION, 22–29s] You stopped scrolling before I said a single word. Here's why it works. One: movement in the first second. Your eyes follow motion before your brain reads anything. Two: the action matches the topic… Three: no setup. No 'hey guys,' no intro. Just the action. I use this on client videos that have done over 50 million views combined. [CTA, 29–33s]" — same hook/structure/length as the source, new value. That IS the skill working.

## The boundary (HARD — Q's standing mirror rule, as a skill)
**Structure, hook pattern, and length transfer ONLY. The VALUE must be Q's own words in Q's voice — never the source creator's copy, never a verbatim repost of another creator's script.**

This is Q's standing mirror rule (mirror style grammar of viral references only — never the other creator's exact content/wording), now written as a skill constraint:
- TRANSFERABLE: the hook shape (the claim/curiosity move in the first 2s), the beat map (what happens when), the length, the structure (which of the 12 it is), the proof device (wall, grid, board, card).
- NEVER TRANSFERRED: the source's sentences, the source's examples, the source's numbers, the source's claims, the source's wording. The "change the value to what you would actually say" step is where Q's Brand Brain governs the output — File 3 (how you talk) writes the lines; File 1 (who you are) supplies the credibility; File 2 (what you sell) sets the CTA.
- A rewrite whose APPLICATION section could be mistaken for the source creator's script FAILS the Quality Gate (check 3, voice check) and is killed, not edited. The fix is not "reword it" — the fix is "write it from the Brain, using only the source's structure."
- "Do what I say" does not license verbatim reposting: even if Q points at a reel and says "rewrite this," the skill rewrites the STRUCTURE with Q's value. The source's script is never reproduced in Q's output.
- The source is credited as structure-only in the script header (source URL + multiple — the gate line). Q's scripts never present a borrowed structure as an original invention, and never present the source creator's claims as Q's.

## Executable steps (Q's script lane)
1. Build the Brand Brain (3 files) + the Playbook (12 structures + scored hook bank). No rewrite runs until both exist.
2. Pick a source reel in Q's niche (a viral reel in the creator-coach / UGC / brand-deal lane).
3. Run the outperformance gate: source views ÷ source creator median ≥2x (INFERRED threshold — Q's ruling pending). Fail = pick a different reel.
4. Pull the source's transcript + caption. Identify its structure (which of the 12) and its hook shape. Do NOT copy its lines.
5. Claude writes Q's version from Brain + Playbook: same hook shape, same structure, same length, Q's value — in the time-coded output shape ([HOOK] / [APPLICATION, mm–ss] / [CTA, mm–ss]).
6. Run the Quality Gate (checks 1–6) on the draft; Q line-edits for taste (check 7). Only then does the script reach Q as "ready".
7. After posting, the AUDIT loop scores the rewrite against views/shares/saves and feeds the result back into the Playbook + hook bank (winners stay, losers retire).

## Worked example (PWC)
Source (illustrative): a viral reel in Q's niche whose structure is proof-led — proof in the first 2s, claim, worked example, close. Gate: source 890K views ÷ creator median 310K = 2.9x — PASSES (≥2x). Structure: #1 Proof-led. Hook shape: a number + a time frame ("One month. $X.").
Q's rewrite (same hook shape, same structure, same length, Q's value — written fresh from the Brain, not copied):
```
[HOOK, 0–3s]
One month. $28,800.

[APPLICATION, 3–24s]
Creators like my wife and I — and other creators — earn like this. Here's what nobody tells you about the small ones. [PROOF on screen: the flagged payments, $200 here, $400 there — small payments adding up, as-is per Q's ruling.] The small payments are the proof the system works before the big ones land. You could be making this — let us show you how.

[CTA, 24–28s]
Comment WAITLIST and I'll send you the first 7 days.
```
Gate check: $28,800 verified against the proof library (P3); collective framing ("creators like my wife and I… you could be making this"); hidden app never named; route to WAITLIST; hook spoken up front, Q's face on screen, proof full-screen in first 2s. Passes to Q.

## PWC skin
- Teal #14A886 + gold #FEE238 on navy #00214E, NO RED. CCC's yellow maps to gold; their coral asterisk maps to gold.
- Nothing over the face. CapCut-native motion.
- The hidden app is never named. Earnings use collective framing, never a direct solo claim. Claims verified against the proof library or killed.
- The skill's "change the value" step is governed by the Brand Brain — File 3 (how you talk) is the law there, and the Quality Gate enforces it.

## GAPS
- CCC's skill file is gated (SKILL → DM). The flow above is INFERRED from the visible transcript + frames. If the real skill file ever becomes public, reconcile — do not assume it matches.
- The outperformance threshold (≥2x median) is INFERRED — CCC shows the check, not its number. Flagged for Q's ruling at consolidation (options: keep 2x, or set a different multiple).
- The knowledge-base load step: CCC loads from Notion; Q's version loads from the on-disk Playbook + Brand Brain. The Notion base's contents are gated — Q's contents are Q's own library, not theirs.
- The exact hook-bank size (1,000 target) and the 12 structure names are Bradford's / INFERRED (see batch5 drafts) — this part inherits those GAPS, it does not resolve them.
- "Do what I say" / verbatim-repost boundary: Q's standing rule is recorded here as the skill constraint. If Q ever rules a verbatim rewrite in for a specific reel, that ruling is recorded here with its scope — the default stays structure-only.

## Needs Q's ruling (flagged, not adopted)
1. The outperformance threshold: ≥2x median (this draft's INFERRED number) or a different multiple?
2. Category 20 (SCRIPTWRITING) itself — create it, or fold the script lane into existing categories (see batch5/category-20-proposal.md)?
3. Third-party connections in CCC's pipelines (Notion, IG search, automation tools) — adopt any, or keep the specs connection-free?

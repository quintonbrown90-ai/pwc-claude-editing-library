<!-- PART: motion/motion-animationbase-review-loop.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# MOTION — ClaudeAnimationBase review loop + reads-as-timing (MIT, SCAN PASS)

Source: JohnHeibel/ClaudeAnimationBase (MIT, SCAN PASS — zero network hits;
one env hit Chrome location only; one exec hit local ffmpeg + headless Chrome
only; base64 hits are canvas data-URL decodes; "seed" hits are animation RNG).
DISTILLED.md in research/repo-sites/ClaudeAnimationBase/. PUBLISHED = their
guide; INFERRED = the Q port below.

## The rule
The prize is the REVIEW LOOP, not the character. Sheet -> strip -> crop,
with explicit checks, forces "watch the exported file in motion" instead of
trusting a builder's report:
- `--sheet=t1,t2,…` — the shape of the piece (one sheet per shot).
- `--strip=a:b` — EVERY frame of a moment (a strip per key motion/transition).
- `--crop=x,y,w,h` / `--crop-at=` — full-res detail on a story-carrying face.
Checks per pass: read (event clear from the sheet alone?) · timing (count
frames per read, 24 frames = 1s; hold after each important moment) · motion
(anticipation + follow-through; no pops/snaps; parts at different times; no
constant speed; no mirroring) · contacts (feet on ground, props touching
hands) · transitions (first/last 0.5s of every shot) · colour (no pure
black/white; muddy glows fixed with additive glow).
Reads-as-timing: write the READS (what the viewer must understand, in order);
one read at a time; fast actions, slow meanings (anticipation + hold after);
a shot is as long as its reads need. Their worked ending packed 6 reads into
~1.3s and nobody could tell what happened — spread to ~4s.
Transitions at every seam (brush wipe / iris / whip pan with smear / match
cut / cut on action / camera carry-through); plain cut only on action or a
deliberate smash cut. Props arrive/leave on arcs, never pop. Beat-locked
motion: every move lands on the beat (`PROJECT.bpm`, pulse per beat).
Boil linework + avoid twinning: per-element boilSeed, offset phases/seeds —
the two cheapest tells of AI-generated motion.

## Executable steps
1. Storyboard in writing BEFORE code (logline, shots with reads + timings).
2. Build one shot at a time; block key poses first, check as stills.
3. Review loop after every build: sheet per shot, strip per key motion, crop
   per story face. Fix, re-check, then render.
4. Map onto Q's gates: sheet = retention read; strip = freeze/transition
   audit (±0.15s around entrances/exits); crop = face-clearance check.

## Do NOT import
Clawd himself (Claude's mascot, not Q's avatar); the no-text rule (Q's reels
need captions — Sky protocol is word-for-word captions); the 16:9 canvas
as-is (Q is 1080×1920 — vertical adaptation UNVERIFIED, check src/config.js
before promising it).

## Worked example (PWC)
P1 wall build: reads table = (1) wall of real creators, (2) "EVERY TILE = A
REAL VIDEO", (3) Q's face + hook. Sheet shows all three reads land; strip at
the wall entrance catches a 0.4s cross-fade (hard cut only — fixed); crop on
Q's face confirms no device crosses it.

## Variants (v9)
- **v9 · @ashokreddyai, DfUfGwqBuur:** 5. @ashokreddyai, DfUfGwqBuur — "A lot of Claude animations are basically built like websites in HTML and React, which is why they all move the same way" (sameness diagnosis) → variant on motion/ motion-animationbase-review-loop.md. Differs: the diagnosis names the cause (HTML/React build) — the review loop is where the sameness gets caught. _(source: v9_variants_bulk_a.md)_
- **v9 · @charlieautomates, DfQYxyXsfi7:** 6. @charlieautomates, DfQYxyXsfi7 — Claude Animation Base card ("Hand-painted cartoons starring Cla…") → variant on motion/ motion-animationbase-review-loop.md. Differs: the card is the public repo instance of the same system. Cards 02 (Collage B-Roll) and 04 were NOT captured in the extracted frames — GAP, not invented; HyperFrames repo link (github.com/heygen-com/hyperframes) is PARKED pending license check + SCAN. _(source: v9_variants_bulk_a.md)_
- **v9 · @guipaulinooo, Dfa12FBq6py / DfaSWitvz_g / DfcUn_7BJKb:** 7. @guipaulinooo, Dfa12FBq6py / DfaSWitvz_g / DfcUn_7BJKb — Motion Sites: "It teaches your AI taste" + self-screenshot + "fixes it until it looks expensive" → variant on motion/ motion-animationbase-review-loop.md. Differs: taste-teaching via 40 loved designs + the fix-until-expensive loop. Off-topic (websites); setup + prompts gated (GAP). Variants: "Folio" hero ($63 invoice), car hero ($0 invoice). _(source: v9_variants_bulk_a.md)_

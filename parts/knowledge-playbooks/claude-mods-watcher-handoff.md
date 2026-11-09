# KNOWLEDGE-PLAYBOOK — Claude Mods: the watcher + the auto-handoff (INFERRED reconstruction)

Source: @jackroberts___ — reel Deo8i2rEQi5 "Claude Mods" (Batch 7 rabbit hole, decoded Nov 8, 2026). The setups are GATED behind comment MODS → DM. NOT chased, bought, or scraped. The SPEC below is rebuilt from visible frames only (transcript + on-screen plugin name, checklist, context bar, handoff brief), labeled INFERRED. His words are quoted; the rest is reconstruction.

## The rule
"Long sessions don't break at the start. They break near the end. That's when Claude Code compacts itself. And the details you needed get squashed." Two mods stop it. One watches; one hands off. A long session needs BOTH — the watcher catches what the main pass misses, the handoff carries what compaction would drop.

## Mod 1 — The watcher ("You Should Know")
"Just switch it on and a second AI watches your back and flags anything that Claude misses." Built in. Plugin name on screen (f_014, VERBATIM-FRAME): `cc-plugin-you-should-know@…`.
- **What it does:** a second pass over the session that flags what the main agent missed. The worked example (f_019–f_021): a session checklist — "Updated checkout.tsx / Added the Postgres schema / Skipped email.test.ts / Renamed the API routes / New migration not run" — with the flags: "The main agent skipped the failing email test" / "We never ran the new database migration".
- **Q's version:** the watcher is the triple-check + the QC gates running as a SEPARATE pass after the build — never the builder checking its own work. The builder delivers; the watcher re-reads the session against the brief and flags the misses. The flag format is the checklist with the missed items flagged (red in his frame → gold in PWC skin): what was done, what was skipped, what was never run.
- **The watcher runs on:** every batch build, every queue run, every long edit session — before anything reaches Q. A session that has not had a watcher pass is unvetted, not "probably fine".

## Mod 2 — The auto-handoff (4-field brief)
"This one runs right before that happens and hands everything to a fresh session with a short brief so you can pick up exactly where you left off." Free on GitHub (repo name NOT shown on screen — GAP).
- **The trigger:** it runs right BEFORE compaction — not after. The context bar (f_028–f_031) fills up, and the handoff fires at the fill line, before Claude compacts itself and "important stuff gets lost".
- **The brief — four fields, in this order (f_033–f_034, VERBATIM-FRAME):** Work In Progress / Decisions Made / Dead Ends / Next Step.
  - **Work In Progress:** what is mid-flight, with file paths / post IDs / exact state.
  - **Decisions Made:** what was decided and why — so the next session does not re-decide it.
  - **Dead Ends:** what was tried and failed — so the next session does not re-try it.
  - **Next Step:** the single next action, named exactly.
- **The receipt:** "handed off — 71k → 33k" (f_037–f_039) — the old session's context compressed into a brief, reported as two numbers. A handoff that reports its own compression proves the brief is short. Q's handoff briefs carry the same receipt line (tokens in → brief tokens out).
- **The proof:** the same work reopens in the fresh session ("Bloom — Flowers that last all week" site) — "so you can pick up exactly where you left off".
- **Q's version:** every long Claude run writes this 4-field brief before compaction AND before handing back to Q — so the next session (or the next agent) picks up exactly where it left off. The hospital device (his caption): "Like a shift change at a hospital. The next nurse gets the full chart."

## The flagged-checklist visual
A checklist where the MISSED items are flagged — the visual form of "flags anything Claude misses". Q's QC reports already list failures; the flagged-checklist is the on-screen form for them: done items plain, missed items flagged gold, with the flag text ("skipped the failing test", "never ran the migration") beside each.

## Executable steps (Q's session-continuity lane)
1. Long run starts: the watcher is ON (the triple-check + QC gates are scheduled as a separate pass, not left to the builder).
2. As context fills, the handoff brief is drafted continuously (the 4 fields update as decisions land — not written from memory at the end).
3. Before compaction (or before handoff to Q): the brief is written — Work In Progress / Decisions Made / Dead Ends / Next Step — with the compression receipt (tokens in → brief tokens out).
4. The watcher pass runs: the session re-read against the brief; misses flagged on the checklist.
5. The fresh session opens the brief and resumes at Next Step. No re-deciding, no re-trying dead ends.

## PWC skin
- Teal #14A886 + gold #FEE238 on navy #00214E, NO RED. His red flags and red "Review access" button map to gold. Nothing over the face. CapCut-native motion. Q's logo on every part.

## GAPS
- GAP — The auto-handoff repo: "free on GitHub" but the repo name is NOT shown on screen anywhere in the reel. NOT chased (gated behind MODS → DM). The 4-field brief above is INFERRED from the visible frames; the tool itself is not adopted.
- GAP — The watcher plugin (`cc-plugin-you-should-know`): name visible on screen only. NOT installed. Any future use needs its own license check + SCAN PASS. Q's watcher is the existing triple-check + QC gates as a separate pass — the plugin is the confirmation, not the implementation.
- GAP — The "71k → 33k" numbers are his demo's numbers, quoted as shown. Q's receipts use Q's real session numbers.

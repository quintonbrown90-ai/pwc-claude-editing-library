# KNOWLEDGE-PLAYBOOK — Find-Skills discovery layer: describe the task → ranked matches → human skims → install (INFERRED reconstruction)

Source: @jackroberts___ — canonical reel DePtyBoAOPd "Find Skills" (parent-decoded, Batch 7). The skill itself is GATED behind comment FINDER → DM. NOT chased, bought, or scraped. The SPEC below is rebuilt from visible frames only (transcript + on-screen install frame, claw-machine frame, ranked-list frame, safety frame), labeled INFERRED. His words are quoted; the rest is reconstruction.

## The rule
Most people install skills one at a time. Then they stop looking. There are over a million out there. Nobody can search that by hand. Find Skills does the searching for you. — The discovery layer is a LIBRARIAN, not an installer: "Like a librarian who fetches the book. And puts it on your desk." The librarian fetches; the human reads before the book is used. "Skim each one before it runs."

The flow, from the transcript + frames (DePtyBoAOPd):
1. **Describe the task** — "Just type what you're working on, like editing videos or writing emails" (transcript 11.2–19.0). Plain language, the work — not the skill name. The task is the query.
2. **Ranked matches from a skill registry** — the skill is "plugged into a library of over one million Claude skills" and "picks out the best one for you" (transcript 11.2–19.0). The ranked list (f_020, VERBATIM-FRAME) is the evidence of what "best" means — ranked by downloads: grill-with-docs 1.1M, improve-codebase-architecture 1.1M, agent-browser 1.0M, tdd 1.0M, frontend-design 955.4K, setup-matt-pocock-skills 944.0K, hyperframes-cli 818.4K, reddit-automation 808.0K, hyperframes 785.5K, vercel-react-best-practices 772.3K. Ranking is by measured adoption, not by the model's opinion.
3. **Human skims each match** — "Skim each one before it runs" (caption). The human reads the SKILL.md before anything executes. The skim is a step in the flow, not a courtesy.
4. **Install** — "it will actually install the right one for you" (transcript 19.0–22.6). Install is the LAST step, after the skim — never the first.
5. **Safety review BEFORE install** — see the hard section below. It is step 3.5, not an afterthought: the dual-model check runs before the install, and the skim is what the check produces.

## The registry (Q's version — INFERRED)
Jack's registry is a public site of 1M+ skills (find-skills itself is "ranked number one out of every skill on the site" — 3.7M shown, f_028). Q's version is the library he already owns:
- **The registry is the v8 parts library + the knowledge index** — every part is a skill with a name, a category, a source, and a measured status (DISTILLED / executable / THEORY ONLY). The discovery layer searches Q's own library FIRST.
- **The harvest is the second registry** — the weekly sweep + the decoded reels are the incoming shelf. A skill enters the registry only after quarantine + SCAN PASS (SAFETY.md §1, §6).
- **External registries are consulted, never trusted** — a match from an outside registry (vercel-labs/skills or any other) is a CANDIDATE. It enters Q's registry only after its own license check + SCAN PASS. See the GAP below on vercel-labs/skills.
- **Ranking in Q's registry is by measured fit, not downloads:** (1) does it execute in Q's stack (the execution bar); (2) does it pass the Quality Gate on a pilot; (3) does Q's own use confirm it. Downloads are a signal for the outside world; Q's ranking is Q's evidence.

## The ranked-match output (what the layer returns)
Every query returns a ranked shortlist in this shape — the shape is the contract:
```
QUERY: <the task, in plain words>
1. <skill name> — <one-line what it does> — <registry: Q-library / harvest / external> — <evidence: downloads / pilot result / source reel>
2. <skill name> — …
3. <skill name> — …
SKIM: <the SKILL.md of the top match, quoted for the human to read>
SAFETY: <dual-model review result — see the hard section>
INSTALL: <only after skim + safety — the install command, recorded>
```
- Three matches, not thirty. The librarian picks; the human does not re-search.
- Each match names its registry. A match from an external registry is labeled EXTERNAL and carries its license status (or "license unchecked — do not install").
- The skim is the SKILL.md itself, quoted — not a summary of it. The human reads the steps, not a paraphrase.

## THE SAFETY GATE (HARD — non-negotiable, see SAFETY.md)
**This layer's whole job is installing third-party code. It is the highest-risk capability in the harvest. The gate is the part — a discovery layer without it is not a discovery layer, it is an auto-installer, and auto-installers are FORBIDDEN.**

1. **NEVER an auto-installer.** The layer NEVER installs on its own authority. Every install is a human decision after the skim + the safety review. A query that ends in an install without a human reading the SKILL.md first has FAILED the layer, however good the match.
2. **Quarantine first (SAFETY.md §1).** Any skill the layer surfaces from outside Q's library lands in `uploads/QUARANTINE/` first. Nothing moves into `skills/`, `code/`, or the Claude zips until it passes review (§4).
3. **SCAN PASS before any use (SAFETY.md §6).** Grep for exfiltration (`send data`, network calls), credential theft (`os.environ`, `~/.ssh`, `keychain`, `getpass`), obfuscated payloads (`base64`, `eval`, `exec`, `subprocess`), and remote execution. Record the result in SOURCES.md. A flag = PARKED with the reason. Never folded in, never staged.
4. **Dual-model safety review before install (Jack Roberts' doctrine — independent confirmation, see `safety-confirmation-find-skills.md`).** "Never install the skill until you run it through ChatGPT and Claude to make sure it's safe." The SKILL.md goes through BOTH models before install. The frame is f_035: a SKILL.md with the "send data" step struck out, gold X (red in his frame) — the exfiltration check made visible. If either model flags it, the skill is PARKED, not installed "carefully".
5. **No credentials ever.** A skill that asks for a credential, a key, an OAuth grant, or a login to install or run is PARKED until Q explicitly rules on that connection. The discovery layer never supplies credentials and never asks Q for them in chat.
6. **Scam/phishing checks.** A skill whose source, name, or install path imitates a known skill (typosquat names, lookalike repos, "official" claims with no provenance) is PARKED. The layer reports the imitation, it does not install through it.
7. **Only public, freely-licensed material.** MIT / Apache-2.0 / BSD / CC BY / clearly-public only, license recorded. License-unclear = parked. Paywalled = excluded. Non-commercial (CC BY-NC) = flagged loud, never staged without Q's explicit word.
8. **Gated/funnel content NEVER chased.** If the skill is behind a comment-keyword → DM gate, the layer rebuilds the SPEC from visible frames only, labeled INFERRED — it does not chase, buy, or scrape the DM flow. The Find Skills skill file itself is gated (FINDER → DM) and was NOT chased; this part IS the rebuilt spec.

## The claw-machine picker (the router visual — see `claw-machine-picker.md`)
The claw grabbing the best skill card (f_013) is the discovery layer's visual: the router reaches into the registry and lifts ONE card. In Q's content, the claw is the Edit Router picking the part for the video. The visual belongs to this layer; the full device spec lives in its own part.

## Executable steps (Q's discovery lane)
1. Q (or the coordinator) states the task in plain words — the work, not the skill name.
2. The layer searches Q's library first (parts + knowledge index), then the harvest shelf, then — labeled EXTERNAL — outside registries.
3. It returns the ranked shortlist (3 matches, registry + evidence per match).
4. The human skims the top match's SKILL.md, quoted in full.
5. The SKILL.md runs through ChatGPT AND Claude for the safety review. Either flags = PARKED.
6. Quarantine + SCAN PASS for anything from outside Q's library. License recorded.
7. ONLY then: the human approves the install, the install command is recorded, and the skill enters the registry with its evidence line.
8. After first use, the pilot result feeds back into the ranking (the audit loop) — winners stay ranked, losers retire.

## Worked example (PWC)
QUERY: "editing videos" (Jack's own example task).
1. Q-library: the viral-rewrite skill (Batch 6), the script-to-carousel skill (Batch 6), the content-architecture spec (Batch 5) — ranked by pilot results.
2. Harvest shelf: the claw-machine picker (Batch 7, this run) as the router visual for the edit.
3. EXTERNAL: find-skills itself (vercel-labs/skills) — labeled EXTERNAL, license unchecked, NOT installed (see GAP).
SKIM: the viral-rewrite skill's SKILL.md, quoted. SAFETY: dual-model review clean (Q's own skill, already scanned). INSTALL: already in the library — no install needed. The layer's answer is "you already own the match" — which is the most common correct answer.

## PWC skin
- Teal #14A886 + gold #FEE238 on navy #00214E, NO RED. The ranked list renders as gold-ranked cards on navy; the safety frame's red X maps to a gold strike-through (the strike is the meaning, not the colour — red is reserved for nothing in Q's system).
- Nothing over the face. CapCut-native motion. Q's logo on every part.
- The hidden app is never named. Claims verified against the proof library or killed.

## GAPS
- GAP — vercel-labs/skills (find-skills source repo): named on screen only (f_007: "▲ vercel-labs/skills", INSTALLATION prompt). NOT cloned, NOT installed, NO license check run. Any future use needs its own license check + SCAN PASS first. This part is the SPEC, not the skill. Logged as a GAP entry with the reason (gated source + unrun license check), per ADOPT-EVERYTHING.
- GAP — The Find Skills skill file itself: gated behind FINDER → DM, NOT chased. The flow above is INFERRED from the transcript + frames. If the real skill file ever becomes public, reconcile — do not assume it matches.
- GAP — Ranking internals: the outside registry ranks by downloads (measured). What else it weighs (recency, ratings, curation) is NOT shown on screen. Q's ranking (execution bar → pilot → Q's use) is the library's own rule, not theirs.
- GAP — The 1M+ / 3.7M numbers are the site's claims as shown on screen (f_020, f_028), unverified. Recorded as claims.
- GAP — Dual-model review mechanics: Jack shows the review as a visual (two model icons over a SKILL.md), not the prompts used. Q's version runs the review as a defined check (exfiltration / credentials / obfuscation / remote execution — SAFETY.md §6 grep list, run by each model). The check list is Q's; the two-model rule is Jack's confirmation.

## Needs Q's ruling (flagged, not adopted)
1. External registries: is the layer allowed to CONSULT outside registries at all (candidates only, never installs), or should it search Q's library + harvest only?
2. The vercel-labs/skills repo: if its license checks out and it passes SCAN, may the find-skills skill itself enter Q's library — or does the discovery layer stay a spec forever?
3. The dual-model review: ChatGPT + Claude as the two models (Jack's exact pair), or Claude + a second reviewer of Q's choosing?

## Variants (v9)
- **v9 · @kayvon.ai, DfamjsXBUGl:** **V104 — @kayvon.ai skill-that-finds-skills (DfamjsXBUGl):** "a skill that goes and finds every other skill you possibly need for you" + "Say, content, and it pulls up the best skills for that exact moment" (→ find-skills-discovery-layer). Auto-download: GAP (never auto-install unvetted code). _(source: bulk-b VARIANTS.md)_

## Variants (v10)
- **v10 · @kayvon.ai, DfamjsXBUGl:** **CONFIRMATION (not a new system):** the V10 note appended to the decode confirms this is the SAME system as Batch 7 (Jack Roberts / vercel-labs/skills) — the find-skills discovery layer already in this part. Kayvon claims 3.9M installs; Jack's Batch 7 figure was 3.7M — same system, numbers drift; record BOTH as claimed, NEITHER as verified. Spoken "over a million of them" vs on-screen "1,403,223 SKILLS" — recorded as observed. The link is DM-GATED (comment SKILLS → DM), never chased. Auto-download ("drops them straight into your setup") is NOT adopted — scan before folding in, never auto-install unvetted code. _(source: Batch 8, v10)_

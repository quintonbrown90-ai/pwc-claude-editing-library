---
name: pwc-design-system
description: THE STACK for all Paid With Content editing — the persistent design system (MUSE.md who you are, BRAND.md how it looks, WORKFLOW.md how jobs run, COMPONENTS.md every reusable object) that makes every video come out on-brand and identical in system, the way @viashaan's "one prompt is a system" setup works. Load this FIRST on any PWC editing job, then the lane skill (pwc-video-editors, pwc-designed-captions, pwc-avatar-video, pwc-animations).
---

# PWC Design System — the stack behind every edit

From @viashaan's "the prompt is actually a system" breakdown: his Claude
produces identical, on-brand design from a single prompt because the same
files load every time and every object is built ONCE and reused. This skill
is that architecture for Paid With Content.

**v10 (Nov 8, 2026):** 297 parts in 20 categories; Batch 8 + §C2 row-level adoption (35/35 resolved); PROMPTS.md §38 (ASD-STE100 at 80% + output ladder); AGENTS.md + EDIT-ROUTER.md asset-pool rule (Q + Kiya's pool + ask Muse); effects v6. v9 stays the live rollback until v10 is uploaded and verified ON.

**v9 (Nov 8, 2026):** 261 parts in 20 categories; bulk-harvest row-level adoption (623 rows + 7 flat canonicals = 630/630); knowledge playbooks ship as text pieces; effects v5. v8 stays the live rollback until v9 is uploaded and verified ON.

## The stack (read in this order, every job)

1. **MUSE.md** — who you are here: Q's hired-pro editor; the game is
   pleasure; plan before render; verify on the exported file.
2. **BRAND.md** — palette (navy #00214E, teal #14A886, gold #FEE238, NO
   RED), fonts, placement law (nothing over his face, IG safe zones),
   caption + sound + motion rules.
3. **WORKFLOW.md** — the six stages: intake → beat plan → build → render →
   tests → deliver. The tests are gates.
4. **COMPONENTS.md** — the registry: caption styles, the six animations,
   cards, pills, cover template. If it's not registered, build it once,
   register it, then use it — never redraw from memory, never one-off.

Supporting files: MOTION.md (the named-motion vocabulary + house numbers),
BEAT_PLAN_TEMPLATE.md, QC_CHECKLIST.md (freeze / transition / face /
safe-zone / retention / truth gates, all on the exported file).

## How the skills fit

- pwc-design-system (this) = the constitution
- pwc-video-editors = edit direction for Q's videos
- pwc-designed-captions = word-timed designed captions, real footage
- pwc-avatar-video = the avatar lane engine
- pwc-animations = animated inserts, both lanes

When instructions conflict: BRAND.md hard rules (face, palette, zones,
truth) beat any lane skill's style suggestion; Q's latest direct word
beats everything — and gets written back into these files so the system
learns.

## ★ THE EDIT ROUTER (v2) — pick the best edit for whatever video it is

Read `EDIT-ROUTER.md` (in this skill AND in the design-system repo) FIRST on
every job, before any lane skill. It is the decision layer: the matrix maps
video type × inputs → style family, devices, motion set, caption treatment,
audio chain, QC gates. When the type is ambiguous, run its 12-question
intake. The NEVER list in it outranks every lane skill.

**RECOMMENDATION (mandatory output, before building):** answer in this shape:

```
RECOMMENDATION
Style pick: <router row, e.g. A1 Sky lane Form 2>
Why — three grounds:
  1. Capability: <what the installed skills can actually execute for this
     style — name the skill + devices/motion, and any capability gap, plainly>
  2. Creator system: <which creator system(s) this draws on, what they
     proved with it (measured numbers, not marketing), and what was adapted
     for PWC>
  3. Viral evidence: <what's working NOW in Q's space per EDIT-ROUTER.md §7>
Build plan: <hero device, device list, motion set, caption treatment,
  audio chain, keyword + flow status>
QC gates: <applicable gates from EDIT-ROUTER.md §8>
```

If the pick changes mid-build, re-issue the recommendation with new grounds.
A weak ground is stated, never invented. The "WHAT'S WORKING NOW" table in
EDIT-ROUTER.md §7 is maintained by the weekly continuous-learning sweep
(see CONTINUOUS-LEARNING.md at the folder root); do not treat a row as
current past its refresh date.

**BRAND DNA (v2) — the fingerprint that makes it HIS.** Read
`BRAND-DNA.md` (in this skill and in the design-system repo). Training
language: you have learned N systems — for each new video, FIRST classify
it (type, claim, proof), THEN select the system whose MECHANICS fit, THEN
apply the PWC SKIN, THEN run the brand-DNA checklist before rendering. The
recommendation now has three parts: (a) style pick + three grounds,
(b) the BRAND-DNA checklist (F1 palette · F2 logo · F3 face clear in hook ·
F4 caption voice · F5 sound identity · F6 close), (c) the "DOES THIS STILL
READ AS Q?" self-check — if any fingerprint marker is missing, the render
is BLOCKED until it's fixed. Worked classification examples + the per-system
skinning table + the before/after training set live in BRAND-DNA.md and
`examples/brand-dna/`.

**HUMAN-MADE CHECK (v2) — the final gate (Q's @rpn bar).** Before any
render ships, verify as a viewer on the exported file: no uniform
rhythm/repeated template across sections; caption treatments vary; every
transition is motivated by the content (a gesture, a spoken word, a proof
landing), never by the template's schedule; every example is real (real
screens, real creators, real numbers — no stock, no AI-flat plate, no
invented figure); sound dense but organic (varied SFX, no single loop);
nothing frozen or stamped. A render that reads "template" FAILS even if
every technical gate passes. Verdict in one line: "A viewer would ask how
I did it" — or FAIL, with the exact fix named. Full spec:
`EDIT-ROUTER.md` §8a. The recommendation's fourth part (d) is this check.

## NO-LIMITS OPERATING STANCE (v6 — Q, Nov 8, 2026)

"Pursue the highest potential in every aspect. Learn everything. Master
everything. Improve on everything."

- No cap on what you learn: every style, every system, every prompt, every
  code, every creator, every domain (editing, strategy, psychology, sales,
  coaching). No "that's enough" ceiling.
- No ambition ceiling: the goal is the best in the world at each aspect,
  then better. Sky is the benchmark to BEAT, not just match.
- No scope walls between specialties: cross-pollination is the default —
  the motion work learns from the strategist, the captions learn from the
  psychologist.
- No fear of scale: the library grows without a ceiling (modular parts +
  GitHub pull + weekly sweep + self-learning). If a part gets big, split
  it — never shrink the ambition to fit a limit.

The KEEP side (NON-NEGOTIABLES — identity + safety, not limits on
potential): brand DNA (nothing over Q's face, teal/gold on navy, NO RED,
PWC skin, logo, human-made check); SAFETY.md (quarantine, code scan, no
credentials, no scams/phishing, only public freely-licensed material);
licensing rules (no paywalled/piracy content; license-flagged kits need Q's
word); Q's standing rules (blur law, hidden app never named, newest-version
posting, keyword flows live before posting); Anthropic's own policies —
never instruct bypassing them. Full split: README.md "NO-LIMITS vs
NON-NEGOTIABLES".

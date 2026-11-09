<!-- PART: render-pipelines/pipeline-qc-gates.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# PIPELINE — QC gates on the exported file (PWC law)

Source: `design-system/WORKFLOW.md` tests + `design-system/tests/QC_CHECKLIST.md`
+ the Nov 2 freeze/transition/dead-air gates. All gates run on the EXPORTED
file, in motion — never on a builder's report.

## The rule
A builder's say-so never ships a video. Watch the whole video yourself,
then run every gate below. One fail = quarantine, fix, re-render, re-run.

## Executable steps
1. **Freeze gate:** freezedetect (n=0.003, d=0.35) — zero freezes ≥0.35s
   in footage spans.
2. **Transition gate:** audit ±0.15s around every card/board entrance and
   exit; hard cuts only for boards over footage (no cross-fades or light
   washes); a card's text lands with its plate (no blank plates).
3. **Ending gate:** last-voice → end-card ≤~1s (measure it; a moving-but-
   dead tail is still dead air).
4. **Lip-sync:** ffprobe container offsets are decisive; frame strips at
   quiet→loud onsets vs the printed 100ms envelope. Never shift audio on a
   correlation score alone.
5. **Retention read:** hook in ≤2s with face on screen; open loop early +
   second before midpoint; visual event every ≤2s; every section ends on a
   mini-payoff or new question; ending chains to the next watch.
6. **Brand-DNA checklist (F1–F6)** + **HUMAN-MADE CHECK** (see the router):
   no uniform rhythm, caption treatments vary, transitions motivated,
   examples real, sound dense but organic, nothing frozen or stamped. A
   render that reads "template" fails even if technically correct.
7. **Claim check:** every claim gets proof on screen at the claim second;
   every comment keyword has a live ManyChat flow before posting.
8. **Newest-version + loudness/clipping check (SL-14):** before firing any
   post, confirm the file is the LATEST stack copy by date + byte size —
   never post from a stale path because it is the one a cron already points
   at. Measure loudness / true peak on the file actually being posted:
   target −14 LUFS, true peak ≤ −1 dBTP. Settled evidence (Backyard #1
   repost, Nov 8, 2026): newest copy −14.07 LUFS / −0.95 dBTP (normal) vs
   old boosted file −10.18 LUFS / +0.56 dBTP (CLIPS — that file was archived
   and replaced). A file over 0 dBTP is quarantined, never posted.

## Worked example
BW-04 v1 passed a full-decode pass but shipped 1.3s + 1.1s frozen stretches
and a cross-faded verdict board over Q's face — caught by Q on sight. The
freeze + transition gates exist because of that miss.
## Self-learning — folded Nov 8, 2026 (research/knowledge/SELF-LEARNING.md)

- **SL-03** — Show-it cue discipline: the visual lands ON the word; a missed cue is a QC fail. (2026-11-06)
- **SL-05** — Door device DEAD in every form (text card, stock footage, designed animation all rejected) — never build it, in any lane. (2026-11-05)
- **SL-08** — Pauses removed: 13 gaps >0.33s → longest 0.28s; gap histogram is a QC metric — attach it to the QC report. (2026-11-07, P1 re-cut)
- **SL-10** — 4.2s frozen classroom screenshot (26.27–30.43s) — freeze gate runs on the EXPORTED file; stills need motion or Q on screen. (2026-11-07, P3 v5)
- **SL-11** — Never invent dollar figures on real proof — invented +$200/+$400 chips stripped. (2026-11-07, P3 rework)
- **SL-15** — Side angles = same performance — constant offsets fix sync; one master audio track, whole turns. (2026-11-06, hat talks v4)
- **SL-16** — Transcript spans amputate non-lexical intros ("ooowee") — scan head/tail/gaps for loud bursts first. (2026-11-06, Talk A v1/v2)
- **SL-18** — Freeze/transition/ending-dead-air gates on the EXPORTED file (±0.15s entrance/exit audits, hard cuts only, text lands with plate, last-voice → end-card ≤~1s). (2026-11-02, BW-04 v1)
- **SL-24** — Status label ≠ verification — v7 posted wrong (big-creator wall, unblurred); spot-check the FILE, not the status. (2026-11-07, P1 v7)
- **SL-25** — Tile swap proven audio-identical (0/1,184,768 samples differ); carried-over defect logged as not-a-regression. (2026-11-07, P1 v9)
- **SL-35** — Body-language scan is a standing QC step: scan gesture/point/look/move cues against the visuals on screen at that second — a cue beat with no matching visual is a hole (4 found Nov 8: AMAZON "back hurting", REAL JOB "building a wall", P1 vanishing 381-view tile, P3 unflagged $200/$400). Fix list before posting. (2026-11-08, body-scan audit)
- **SL-14** — ALWAYS post the NEWEST version — pre-post date + size check
  on the file actually being posted; loudness/clipping check (−14 LUFS /
  −1 dBTP ceiling; old boosted file clipped +0.56 dBTP). (2026-11-08,
  Backyard #1 repost)

- **QC-report shape (Batch 6 variant, DfH3KDijEgL / DZ2zNPWtTnA):** the
  "How aggressive should the cut be?" pace question is the brief (Q's pace
  is 1.0x, no pauses — the question is the brief, the answer is the pace);
  the cut report ("Removed 21 silent gaps, saving 18 seconds") is the
  proof (what was cut, what was fixed). A QC report carries both: the
  brief restated + the cut list.

## Variants (v9)
- **v9 · @cooper.simson, DXxtd-5Nu54:** 56. @cooper.simson, DXxtd-5Nu54 — "Turned it into this one continuous video" (every gap, dead air, filler word, pause cut) → variant on render-pipelines/pipeline-qc-gates.md. Differs: the through-edit stated as the result (one continuous video). Guide gated (GAP). _(source: v9_variants_bulk_a.md)_
- **v9 · @duncanrogoff, Dem6pyHERiK:** 58. @duncanrogoff, Dem6pyHERiK — "Claude checks every second of its own edit and fixes anything that looks off" (self-QC; 3,205 tests passed — his figure) + "I give Claude Code one script and it plans every scene before it builds anything" → variant on render- pipelines/pipeline-qc-gates.md. Differs: the check runs per second of the edit, and the plan comes before the build. Breakdown gated (GAP). _(source: v9_variants_bulk_a.md)_
- **v9 · @hesamious, DbBsQBUsO4M:** 61. @hesamious, DbBsQBUsO4M — "One single continuous take — no cuts, no transitions, no dissolves, no wipes, fades, start-to-finish" (continuous-take rule) → variant on render-pipelines/ pipeline-qc-gates.md. Off-topic (outfit videos); the take rule is the transferable part (GAP for the system). _(source: v9_variants_bulk_a.md)_
- **v9 · @aiadventureryt, DeolW_aBoAC:** 62. @aiadventureryt, DeolW_aBoAC — "It checks every part like a critic before handing it over" → variant on render-pipelines/ pipeline-qc-gates.md. Off-topic (/anatomy skill builds working machines); GitHub link gated (GAP). _(source: v9_variants_bulk_a.md)_
- **v9 · @davis.mcm, DfVOnGHo9xX:** 63. @davis.mcm, DfVOnGHo9xX — Learn Harness "Nothing gets built on a gap" (predict → teach → check, one step at a time) → variant on render-pipelines/pipeline-qc-gates.md. Off-topic; repo + guide gated (GAP). _(source: v9_variants_bulk_a.md)_
- **v9 · @?, V8-08:** V8-08 — "It read the video but never watched it" — frame-awareness before any zoom/text decision → pipeline-qc-gates.md _(source: v9_verification.md)_
- **v9 · @?, V8-62:** V8-62 — Fact-check step: verify public + free before publishing → pipeline-qc-gates.md _(source: v9_verification.md)_
- **v9 · @?, V8-71:** V8-71 — Nail the style before you scale: first 5 seconds, 4 variations, pick one → pipeline-qc-gates.md _(source: v9_verification.md)_
- **v9 · @?, V8-84:** V8-84 — "Move it — it's covering my face, it's on the forehead" → pipeline-qc-gates.md _(source: v9_verification.md)_
- **v9 · @?, V8-123:** V8-123 — 10-step assembly line with a QC gate between every step → pipeline-qc-gates.md _(source: v9_verification.md)_
- **v9 · @minolee.mp4, DehM80nN7Gv:** @minolee.mp4 DehM80nN7Gv — 3-core checklist: perfect the dead space + captions sharp in house style + storytelling over template. DIFFERS: the three-line checklist form. _(source: bulk-c VARIANTS.md)_
- **v9 · @mr.paidsocial, DdHORRhjjOJ:** @mr.paidsocial DdHORRhjjOJ — review link: the edit is delivered as a link to review, "just like a real editor actually would." DIFFERS: the handoff formalized as a review link. (AI-generated talking head in the video: FLAGGED, not adopted — Q's face is real.) _(source: bulk-c VARIANTS.md)_
- **v9 · @mr.romanwei, DeyxYlmk9CH:** @mr.romanwei DeyxYlmk9CH — script-compare: what you said is compared with your script, where you messed up is seen, only the good takes are kept. DIFFERS: the comparison is named as the cut mechanism. ("Delete CapCut": FLAGGED vs Q's CapCut-native order.) _(source: bulk-c VARIANTS.md)_
- **v9 · @shihui.travels, De_2J7AM-Sp:** @shihui.travels De_2J7AM-Sp — "Nothing gets rendered until you say yes" (storyboard-before-render). DIFFERS: the yes-before-render phrasing. _(source: bulk-c VARIANTS.md)_
- **v9 · @omgluka, DfZkGbLBe5C:** @omgluka DfZkGbLBe5C — "My only job: approve it" (agent edits, human approves). DIFFERS: the human's job named as approval only. (DaVinci Resolve as the NLE: NOT adopted — Q's lane is CapCut-native.) _(source: bulk-c VARIANTS.md)_
- **v9 · @seb.ai, DfbjG8yPDcM:** @seb.ai DfbjG8yPDcM — replay device: "replays the rest of the day 10,000 times before so you can see the odds." DIFFERS: simulation-before-ship as a named device. (Trading repos GATED, GAP.) _(source: bulk-c VARIANTS.md)_
- **v9 · @opusjake, DfYab6Ftp98:** @opusjake DfYab6Ftp98 — time-machine concept: "before you risk a single dollar, it replays every possible outcome." DIFFERS: same device, trading lane; the simulate-before-ship shape transfers. _(source: bulk-c VARIANTS.md)_
- **v9 · @tunestechtips, Dfc0quUCvBe:** @tunestechtips Dfc0quUCvBe — "Ask it, what broke today?" as the QC question; same error twice → one issue (grouping). DIFFERS: the question form + the grouping rule for the error log. (Bicho tool GATED, GAP.) _(source: bulk-c VARIANTS.md)_
- **v9 · @tunestechtips, Dfd4SU6j7xY:** @tunestechtips Dfd4SU6j7xY — screenshot-before-save + test loop: before each change is saved, screenshot every page (light + dark) and run the tests. DIFFERS: the gate fires BEFORE save, not after. (BAMMA tool GATED.) _(source: bulk-c VARIANTS.md)_
- **v9 · @tunestechtips, DfdZhu7DMAZ:** @tunestechtips DfdZhu7DMAZ — "Each warning is a one-line fix and it names its source." DIFFERS: the failure-report format (one line + source). (Usage tool GATED.) _(source: bulk-c VARIANTS.md)_
- **v9 · @scottsmithyta, Deu22jMJFAW:** @scottsmithyta Deu22jMJFAW — source-for-every-number: deep research finds 30 real stories with real numbers, real facts, a source for every number and every fact. DIFFERS: the 100%-sourced standard. (Prompts on screen but not legible — not folded in.) _(source: bulk-c VARIANTS.md)_
- **v9 · @thecuttingedge.school, De_XFh_O8-4:** @thecuttingedge.school De_XFh_O8-4 — timestamp-level revision: ask Claude to make changes at a particular timestamp. DIFFERS: revision-by-timestamp, not re-render-everything. _(source: bulk-c VARIANTS.md)_
- **v9 · @pauloshimas, DfU_isFSred:** @pauloshimas DfU_isFSred — approve each scene with one click (per-scene approval). DIFFERS: the storyboard approved scene by scene. (Cartoonify itself: off-lane — Q keeps the real room; GAP.) _(source: bulk-c VARIANTS.md)_
- **v9 · @scalebysarthak, DfHtCqxNb0g:** @scalebysarthak DfHtCqxNb0g — storyboard V1 → V2 ("like a real editor"): change your mind, ask, get another storyboard. DIFFERS: the versioned storyboard. (Pinterest API connection: credential flag, GAP.) _(source: bulk-c VARIANTS.md)_
- **v9 · @mattphxm, DbZyaHNFUUf:** **V92 — @mattphxm Local Editor (DbZyaHNFUUf):** "Every silence longer than half a second, gone." (→ pipeline-deadair-gate — DISCREPANCY: Q's floor is 0.35s, his is 0.5s; recorded as observed, not reconciled); "the takes where you start again, it keeps the clean one" (→ pipeline-qc-gates); "reads back what I said and re-orders these sentences so that it's the tightest version" (→ pipeline-caption); "I don't have to open a single time line." The Local Editor tool itself: GAP (free, no login, but not in the harvest — license unknown, never installed). _(source: bulk-b VARIANTS.md)_
- **v9 · @kylewhitrow, DYpWMHBCbIW:** **V93 — @kylewhitrow approval workflow (DYpWMHBCbIW):** feedback per spot (whole video / single beat) → approve or revise-in-place → approved status stored (→ pipeline-qc-gates); "Approve the auto caption created by Claude Code, or change it, then hit Send" — the caption-approval beat. Auto-post: GAP (conflicts with Q's approval doctrine). _(source: bulk-b VARIANTS.md)_
- **v9 · @karthiknaidu_official, Dfb-YiHSnXu:** **V95 — @karthiknaidu_official audit-before-build (Dfb-YiHSnXu):** "It even audits every gear and mechanism internally to ensure mechanical accuracy before generating the final build." (→ pipeline-qc-gates). The skill/repo: GAP (named only, gated doc). _(source: bulk-b VARIANTS.md)_
- **v9 · @max4thepeople, DepgkAOhldO:** **V96 — @max4thepeople hands-free proof (DepgkAOhldO):** film the screen while Claude drives the editor — a different trust device from code-generated edits (→ pipeline-qc-gates). Computer-use itself: FLAGGED (needs Q's word). _(source: bulk-b VARIANTS.md)_
- **v9 · @itsaustinmyers, DfDuiAgMlg2:** **V97 — @itsaustinmyers approve-as-final (DfDuiAgMlg2):** "If you're happy with it, just tell it, I approve this as the final version." (→ pipeline-qc-gates). _(source: bulk-b VARIANTS.md)_
- **v9 · @createcontent.club, DZ2zNPWtTnA:** 67. @createcontent.club, DZ2zNPWtTnA — "How aggressive should the cut be?" (pace question) + "Removed 21 silent gaps, saving 18 seconds" (cut report) → variant on render-pipelines/pipeline-qc-gates.md. Already tracked in v8; re-confirmed here. File gated (GAP). _(source: v9_variants_bulk_a.md)_

## Variants (v10)
- **v10 · @millee.md, DfBBG0xPioN:** **/anatomy — second source:** the skill called /anatomy builds structures and objects ("which make great assets for educational videos") — second source after @aiadventureryt DeolW_aBoAC (batch 9, v9 variant above). The skill itself is named only, gated behind comment MOTION → DM — NOT downloaded, NOT scanned, NOT folded in. _(source: §C2, v10)_

# QC — how to prove a test edit matches Sky

**Rule:** no style ships as "done" without a test edit graded against its own examples.
This style is currently UNGRADED (see `GAPS.md` G-16). Grade on the EXPORTED file, in motion
— never on a builder's say-so, never on stills alone.

## 1. Frame-sequence motion grade (the deciding test)
- Pick the video's ONE model reel first (the reel Q's brief names) from `examples/MANIFEST.md`.
- Build a side-by-side frame SEQUENCE (matched beats, sequences not stills) of the test edit
  vs the model reel: hook build, first device entrance, one mid-video state-change, one
  verdict/count-up landing, the close.
- Pass bar: a viewer who knows Sky reads the test edit as Sky's *system* in Q's colours —
  same device, same entrance, same hold, same exit, same rhythm. If it reads as "inspired by",
  rebuild the failing section. Do not explain the difference away.
- Record per beat: PASS / FAIL + timestamp + what differs. One failing beat = the grade fails.

## 2. Technical gates (all must pass, on the exported file)
| Gate | Command / check | Pass bar |
|---|---|---|
| Full decode | `ffprobe` + full decode pass | Clean; no black / frozen / missing-picture sections in sampled frames across the whole length |
| Freezes | `code/qc_freezedetect.sh <file>` (ffmpeg freezedetect, noise 0.003, duration 0.35) | **Zero freezes ≥ 0.35 s** inside footage spans |
| Card/board entrances + exits | Frame audit at ±0.15 s around EVERY device/card/board entrance and exit | No board fading or washing over the face; no title crossing the face; no blank plate landing before its text — plate + text land together; boards over footage enter on hard cuts |
| Ending dead air | Measure last spoken word → end card on the export | **≤ ~1 s** |
| Lip-sync | ffprobe container offsets (decisive) + human-eye frame strips at quiet→loud onsets vs the 100 ms audio envelope | Voice on the mouth; constant offset, no drift; every pop/graphic on its spoken beat. Never shift audio on a correlation score alone |
| Face framing | Check at every zoom/punch scale used | Face zone empty of graphics at every scale; framing matches the source take (background, clothing, lighting) |
| No-overlap | Engine no-overlap check on every frame (or manual frame audit) | No text over a graphic, no pop over a pop, no card over a card |
| Per-word fit | Every caption and graphic word fully visible at every cut | One clipped word = FAIL, blocks delivery |
| Text handoff | Render stills at every handoff (prev.t1 + 0.1 / +0.3 / +0.5 s) | No new top-zone text starts while the previous one is still animating out (next t0 ≥ prev end + 0.5 s) |
| Text clipping | Full-resolution crops of the hook title and hero words; scan every component at mid-hold for alpha on canvas edges | Never clip text, glow or shadow at a layer edge; serif descenders have room (carousel Archetypes B/E only — reels have NO serif in v6; serif in a reel = banned telltale, gate P9) |
| **P9 — Premium gate (v6)** | `sky_qc.py` on the plan (`validate_premium_plan`) | No unknown devices, no fallback-marked events, no banned fonts/motions/treatments, no cheap-grade asset markers, no disallowed provenance, no AI on proof devices, no [EST]-quarantined devices, every event carries a Sky source citation |
| **P10 — Beat-lock gate (v6)** | `sky_qc.py` on the plan (`validate_beat_lock`, needs the plan's `word_grid`) | Every event on the take's beat grid within ≤1 frame (≈0.033 s), or carries a stated `off_beat_reason`; a plan with no word grid reports NOT RUN — unverified, never a pass |

## 3. Sky-system checks
- [ ] Framework name on screen ≤ 10% of runtime; hero device visibly unfinished until the close.
- [ ] Every part: state-change fires on its first spoken word; example asset present at its claim;
      no claim spoken over a bare talking head when an asset exists.
- [ ] Captions: every group 1–3 words, one weight all video, none over the face, none straddling
      a cut, none overlapping a graphic or another caption.
- [ ] Every required device from the build plan present in the export; a missing device is a
      fail even when technical checks pass.
- [ ] Family fit: does this read as its Sky family (GREEN/teal or ORANGE/gold)? One accent only.
- [ ] Carousel twin exported from the same device states (framework reels).
- [ ] PWC law: logo present, teal/gold on navy, no red, no neon green, blur law applied to any
      hidden-app proof, hidden app never named, no door device, keyword flow live before posting.

## 4. Retention read
- [ ] Hook lands a claim or curiosity within 2 s, with Q's face on screen.
- [ ] Open loop early + a second open loop before the midpoint.
- [ ] Visual event every ≤ 2 s.
- [ ] Every section ends on a mini-payoff or a new question.
- [ ] Ending chains to the next watch.
- [ ] Constant pace start to finish: no slow stretches, no sagging middle, no dead beats. Only
      deliberate dramatic pauses survive.

## 5. Full self-watch
The editor watches the ENTIRE export at normal speed before delivery. Speed never waives this.

## 6. Test-edit fidelity grade (current status — Nov 9, 2026)

**NO TEST EDIT GRADED. Grade: NOT GRADED (no gradeable export found).**
- No Sky-style test edit export was found on disk in the folders checked for this build, so no
  frame-sequence grade, freezedetect run, entrance audit, or lip-sync check was run.
- P1 v9 / P2 / P3 are live posted Q videos built in the Sky lane (Nov 7–8, 2026), but their exact
  exported masters were not located in the folders checked, so they were NOT graded here.
- **Do NOT present this style as "exact"** until a test edit is built from `code/` + `SKILL.md`,
  graded with §§1–5 above against its named model reel, and the grade is recorded here with
  per-beat results. The first graded test edit replaces this section with its report.
- **Batch 18 model reel (Dcc84V5jc6D):** its 11 grade-ready matched pairs are in
  `examples/batch-18-sky-origin/EDIT-TEARDOWN.md` §10 (hook build, hook exit, caption hard
  cut, count-up, phone + donut, doc + highlight, proof columns, figures, prompt UI, live
  example, bare close) — use them when the model reel for a test edit is the origin reel.

## 7. Delivery report (required per file)
CapCut project/draft name · motion-sequence grade result per beat · freeze count + longest
freeze · number of entrances/exits audited · last-word→end-card gap · per-word fit result.
A cut with any gate unrun is reported as unverified, never as verified.

## 8. Anti-slop cross-reference (Batch 17 — now the v6 BANNED-TELLTALES source)

**Source:** @millee.md (Michael Quoc Ly), "5 ways to UNSLOP your AI video edits",
https://www.instagram.com/p/DfCzXfRlrUo/ (shortcode `DfCzXfRlrUo`), posted Oct 28, 2026.
Library files: `research/video-harvest/instagram/batch-17-millee-anti-slop/DECODE.md`
(full decode + Q-mapping) and `ANTI-SLOP-RULES.md` (standalone rules); library part #310
(`parts/render-pipelines/anti-slop-rules.md`).

**SKY v6 note (Batch 36):** the anti-slop RULES below are no longer a "second option" —
they are absorbed into the binding BANNED-TELLTALES list (`SKILL.md`) and enforced by
`validate_premium_plan` (gate P9). Premium Sky is the only execution path; these rules are
its guardrails, never a substitute style.

**The 3 slop markers the Sky skill must never produce:**
1. **Italic serif captions** — the Claude default face; the single most recognisable AI-edit
   fingerprint ("same italic serif, three different creators").
2. **Flat 2D vector graphics as substitutes for real footage** — generated-looking filler that
   signals nothing real was filmed or captured.
3. **Tilted rounded-corner sticker overlays** — the template-element look; a tilted, outlined,
   drop-shadowed card reads as "sticker slapped on by a tool," not evidence.

**Two conflict resolutions (from the decode — these govern, do not re-litigate):**
- **WAY 03:** Millee's "don't animate overlays" kills **cheap template animation** (pop-in,
  slide-in, bounce, sticker cards). Sky's **purposeful motion stays** — captions hard-cut in
  ≤1 frame, cards ease 8–12f, devices move in/out with sound on the spoken beat.
- **WAY 04:** **Q's pause standard governs Q's edits** (compress gaps >0.20s to ~0.15s; ≤2
  dramatic pauses ≤0.30s survive). Millee's 0.1s cut-everything threshold is the **stricter
  reference** — cite it when a cut still feels loose; never silently re-cut a Q edit to 0.1s
  and kill its dramatic pauses.

This section ADDS a cross-reference only. It does not modify any Sky device, grammar rule,
or existing QC gate above. (Attribution: the `STYLE-GRAMMAR.md` §5 Millee WAY 03 paragraph,
the `SKILL.md` banned-telltales lineage and the deleted `code/sky_option2.py` trace to
Batch 19's work; Batch 36 removed the fallback and wired these rules into gate P9.)

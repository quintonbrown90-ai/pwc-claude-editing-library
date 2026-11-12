# CREATOR-SYSTEMS — sky-v6-full-profile-completion: SKY v6 — the full-profile completion of @realskytan's editing system (49/49 reels decoded + measured sound, devices D1–D56, premium purge, beat-lock)

> **Registry note (filed Nov 12, 2026):** this part is registered as **part #335**, not #334. Part #334 was already taken by `parts/knowledge-playbooks/max-mobilization.md` (Batch 38, commit be2c11e) before Batch 36 shipped, so the next free number was used rather than duplicating a registry number.

Source: Sky Tan — @realskytan (https://www.instagram.com/realskytan). Batch 36 (Nov 12, 2026) completed the full-profile decode of Sky's system to the Batch-18 bar: **49/49 reels decoded**, **49 measured soundmaps**, the carousel grammar corrected from the 10 known carousel posts, and the whole system distilled into **SKY v6** — the canonical skill. Sky material is technique reference only; no Sky copy, framework names, figures, or stories are lifted into Q-facing material.

## Canonical location — the source of truth

The skill itself is the source of truth; this part is the library's summary + pointer:

- **Master skill folder:** `~/workspace/claude-editing/styles/sky-edit-style/` — `SKILL.md` (SKY v6), `STYLE-GRAMMAR.md`, `SKY-TEARDOWN-MASTER.md` (§§0–14, the measured teardown), `SKY-CODE-PROMPT.md`, `ASSETS.md`, `QC.md`, `GAPS.md`, `SOURCES.md`, `README.md`, and `code/` (`sky_devices.py` device registry D1–D56, validators, plan/QC tooling; test suite 88/88).
- **Code-side install:** `~/.claude/skills/sky/` — an installed mirror of the master (rsync `-a --delete`), re-verified at ship time (tests 88/88 in the copy, `sky_option2.py` absent).
- **Research evidence:** `research/video-harvest/instagram/batch-36-sky-completion/` (enumeration MASTER-TABLE, 49 soundmaps, carousel decodes, synthesis specs, worker reports).
- **In the PWC-Videos repo:** `SKY_STYLE.md` carries the v6 marker line and the corrected rules for edit sessions working in that repo; where it and the skill disagree, the skill wins.

## What v6 is

**The bar (verbatim from the skill): "Sky exact is the floor. Ship better than Sky's own execution of his system."** Exact duplication of Sky's measured grammar is the floor, not the target. Elevation runs on Sky's own axes only — timing precision, motion smoothness, sound richness/density, visual polish, retention pacing — with every PWC target derived from Sky's own best-measured instances, never invented, never drifting into generic patterns. An edit passes only if it grades AT-OR-ABOVE the Sky reference on fidelity AND ABOVE it on execution quality.

**Corpus state at v6:** 49/49 reels decoded to the Batch-18 bar (frame-level decode + measured sound for every reel, incl. the two former FAILs DeYKkAIgVfL / DeSTWxcDTA7 brought to bar and the origin reel Dcc84V5jc6D's distilled soundmap completing the set at 49). Carousel grammar corrected from measurement: 10 posts / 86 slides — 51 video slides + 35 image slides (superseding the old "every slide is a video" claim).

## Devices D1–D56 (57 registry entries)

The reel device registry is now **D1–D56 plus the D5-list entry = 57 registry entries** in `code/sky_devices.py`:

- **New in v6:** **D55 numbered pill system** (pill chips pre-shown as a row; per pill, the previous text exits by blurred slide ~0.7 s before the next number word, the active chip stands alone exactly on its number word, then its text types in by word groups — DeYKkAIgVfL, strip-resolved) and **D56 "New reel" UI exhibit shrink** (the open B&W frame scales down into the thumbnail position of a real Instagram "New reel" UI exhibit, holds, exits by hard cut — DeSTWxcDTA7; single instance, flagged as such; proof-class, real captures only).
- **Enrichments, deduped (no new numbers):** D17 trust dot-grid flip bracket + single-instance fade exception, D18 network loop citation, D19 people grid (~70 play-icon cells, headline types in, grid never completes), D22 new-post placeholder shelf form, D23 floating-heads system options (role labels type in, emoji pops, accumulating bullet lists), D50 gradient script headline `draw_in` variant, D51 player-stats card UI-blip sound note.
- **Quarantine:** [EST]-parameter devices (D5 chapter card, D13) are flagged in the registry and **rejected by the premium validator** — estimates never ship as "Sky."
- The L-series (Andrew Lee) devices are NOT Sky's and are NOT in the registry (G-20 stands).

## Sound grammar — the tick-tone correction

Batch 36's measured soundmaps **corrected** the inherited sound grammar. The set-level "dry voice only" claim is overturned:

- **Tick-tones are real Sky grammar:** gated fixed-frequency pulse trains (5,926 Hz, ~13–17 pulses/s, −38…−45 dB band under voice), synced to counters, timers, count-ups, and chart draws — coded as `TICK_TONE_SPEC` sound annotations on D6 / D20 / D27 / D31 / D37, with gated short-tone variants (~9.15 kHz; ~11.1 + 11.85 kHz). Origin (edit-layer micro-SFX vs captured device sound) is unprovable from audio alone and stated as undetermined; no ear-matched local tick file exists, so the spec instructs the CapCut editor rather than naming an asset. Sub-threshold candidates in 8 more reels are recorded as unconfirmed, not counted.
- **The measured grammar overall:** dry voice base; near-silent cuts (the silent hard cut is the transition norm); **exit SFX present** — sound on device entrances AND exits; tick-tones on counters (above). NOT a constant music bed + sparse SFX: beds are form-specific exceptions (founder-vlog / split forms), decided per form from Sky's best-measured instance.
- **Refuted:** DP4r6BbEvHg's "drone bed" — measurement shows the low-frequency track follows the voice; the claim is annotated as refuted in its decode, not silently rewritten.
- DJccT_xSWuT carries one confirmed isolated UI blip (31.26–31.68 s) recorded as a D51 sound instance note, not a device. DP2_6r7DQ60's 1.37 s dead tail is kept as a negative datum.

## Beat-lock + the premium validator (QC gates P9 / P10)

- **Beat-lock (binding):** every planned event — caption hit, device in/out, visual motion, SFX, transition, punch-in — sits on the take's own beat grid (word stresses from word timings + detected music beats where a bed exists) within **≤1 frame (≈0.033 s)**; a deliberate off-beat carries a stated `off_beat_reason` in the plan or it fails. `validate_beat_lock` + `beat_lock_report` in `sky_devices.py`; `sky_build_plan.py` stamps the word grid into the plan and validates at build time.
- **Gate P9 — Premium:** `sky_qc.py` runs `validate_premium_plan` — rejects unknown/unregistered devices, fallback-marked events, banned fonts, banned motion types, cheap-grade asset markers, disallowed asset provenance, AI provenance on proof devices, [EST]-quarantined devices, and any event missing its Sky source citation (D14 Q-override end card excepted).
- **Gate P10 — Beat-lock:** `sky_qc.py` runs `validate_beat_lock` against the plan's word grid; a plan with no word grid reports P10 as **NOT RUN — unverified**, never a silent pass.
- Full gate set P1–P10 lives in the skill's `QC.md` / `SKY-CODE-PROMPT.md`. Test suite: **88/88 OK** (`python3 -m unittest discover -s code/tests`), incl. the 11 `TestPremiumV6` validator/beat-lock tests and the test asserting the deleted fallback module stays absent and unimported.

## The premium purge (premium-only in v6)

v6 has exactly ONE output mode: premium Sky. The generic fallback was deleted, not deprecated:

- **`code/sky_option2.py` DELETED** — the whole module (15 generic patterns: blur-in pops, slide+blur panel-out, idle float, slide-ins, serif titles, caption pop-in, etc.).
- The GSAP slide-in emitter branch in `sky_hyperframes.py` and the `_panel_out()` slide+blur helper in `sky_devices.py` deleted; unmeasured entrances now raise instead of falling back.
- The "TWO OPTIONS" blocks / Option-2 tables in `SKILL.md`, `STYLE-GRAMMAR.md`, and `code/capcut_build_spec.md` replaced with the PREMIUM-ONLY statement + the **BANNED-TELLTALES** list (serif display in reels, slide/fade/pop-in template motion, idle float, stamped overlays, generic wipes/spins, cheap-grade assets of every class — the ban is on cheap grade, not on AI).
- Historical mentions in batch folders / decodes / reconciliation docs stay as record only; they route no builder anywhere. One-line tombstones in `code/README.md` + `capcut_build_spec.md` point old references at the v6 law.

## Asset law + the Batch 37 fold

- **Asset law:** Q + Kiya's own pool FIRST (their Skool screenshots, blurred proofs, profiles/examples, carousel styles/runs, head cutouts, media library, the PWC logo cutout), then style-asset libraries and real screen captures; sounds from Q's licensed local library.
- **Premium AI is allowed** — the ban is on CHEAP GRADE, not on AI. Provenance allowlist: `real_photo / real_video / real_capture / real_doc / ai_premium / higgsfield / fable_motion`. **Proof carve-out (hard):** evidence-bearing devices (exhibits, profile inserts, proof columns, comment screenshots, view-count proof — D9, D10, D20, D30, D33, D39, D43, D56) may NEVER carry AI provenance; payouts, screenshots, and results are real only. Illustration and visual hooks are the premium free hand (real or AI).
- **Batch 37 fold:** 23 open-source items named against their Sky function in `SKY-TEARDOWN-MASTER.md` §11.3 (captions/timing: dynamic-captions, pysubs2, stable-ts, Beat This!; motion: gl-transitions, xfade-easing, Editly, Anime.js v4, HyperFrames Motion Reel Skill; matting/cleanup: BiRefNet, rembg birefnet pin, SAM 2, Practical-RIFE, IOPaint; CapCut draft layer: pyJianYingDraft, capcut-mate draft APIs only, video-recap-skills, VectCutAPI — do-not-install decision carried, capcut-cli; sound: Wyzowl SFX Kit, Kenney packs, DeepFilterNet) + 5 explicit exclusions carried so they are not re-chased (RobustVideoMatting GPL-3, BRIA RMBG-2.0 CC-BY-NC+gated, ProPainter S-Lab NC, CoTracker weights CC-BY-NC, OpenMontage AGPL-3).

## PWC skin (unchanged law, restated in v6)

Mechanics are Sky's; the skin is always PWC: **teal #14A886 + gold #FEE238 on navy #00214E, NO red anywhere** (negatives use the measured treatments: strikethrough + gold X / B&W beat), PWC logo (transparent cutout badge, never the black square), Q's voice and content, captions in bold grotesque as **hard cut-in word groups** (~0.5 s groups, Df era; ≤1 frame cut-in, no typing effect), nothing over Q's face, CapCut-native finish.

## Coverage gaps — with reasons (honest, carried in `GAPS.md` / master §14)

1. **35 carousel image slides** — content undecoded: anonymous yt-dlp emits no image URLs and the embed fallback is a JS shell, so no frames exist on disk. Slide positions/interleaving ARE known for all 35; archetype-E's tail function, DfDwkljmAXg slides 2–14's system, DSYULMGk12r's archetype, and DfLku2QkZcP's close stay open. Closing this needs a browser/authenticated pass.
2. **Post-Nov-9 profile window UNVERIFIED** — 0 new posts found via search, but every direct grid route is blocked (429 / checkpoint wall / broken extractor); absence is NOT proven.
3. **~305 posts unenumerable anonymously** — the enumeration MASTER-TABLE rows 59 known posts (49 reels + 10 carousels); ~54 surveyed-but-unnamed posts and ~251 unsurveyed posts carry the same anonymous-access reasons. Full-grid enumeration needs an authenticated route.
4. **Corpus-wide beat-offset median/p90 never computed** — most device timestamps carry ±0.1–1 s brackets from 1–4 fps passes, so a distribution cannot be honestly derived; the beat-lock target is set from frame-exact instances + the binding spec (≤1 frame).
5. **Tick-tone origin undetermined** (edit layer vs captured device sound) — unprovable from audio alone; the origin reel's ~6.3 kHz candidate (Dcc84V5jc6D @5.80–5.95 s) remains UNVERIFIED in its soundmap.
6. **Inherited [EST] parameters** (D5/D13/D26–D33/D44/D54 details, font identity, exact easing curves) have no frame measurement on disk — carried flagged and quarantined by the validator, never upgraded.
7. **Three transition mechanics** (DfX2qwQGagM @39.37 s; DfU49SJAFYH @40.53 s + subject boundaries) unresolved at 4 fps — stated as undetermined.
8. **DeYKkAIgVfL income-card figures + D18 loop label** below legibility in the 720p sources — carried as fragmentary.

## Ship record (Batch 36, Worker E, Nov 12, 2026)

SKY v6 shipped to all four destinations: (1) Code-side install synced master → `~/.claude/skills/sky/` (mirror verified, tests 88/88 in the copy); (2) this library part + INDEX/CATEGORIES registration; (3) PWC-Videos `SKY_STYLE.md` wholesale-replaced with the v6 marker + corrected rules (see the FIXES spec: `batch-36-sky-completion/synthesis/PWC-VIDEOS-SKYSTYLE-FIXES.md`); (4) web zip `sky-v6-web.zip` built from the master (one top-level folder, one SKILL.md, within the ≤200-file / ≤30 MB limits). Full per-destination SHAs and stats: `batch-36-sky-completion/synthesis/WORKER-E-REPORT.md`.

## Sources

- Skill: `~/workspace/claude-editing/styles/sky-edit-style/` (SKILL.md — SKY v6; SKY-TEARDOWN-MASTER.md §§0–14)
- Batch 36 research: `research/video-harvest/instagram/batch-36-sky-completion/` (STATUS.md, enumeration/MASTER-TABLE.md, soundmaps/, carousels/, synthesis/, verify/)
- Prior Sky part: `parts/creator-systems/sky.md` (the pre-v6 codification — superseded by this part for the v6 state; its device-era history stands)
- Batch 37 fold source: `open-source-library/sky-staging/MANIFEST.md` (via master §11.3)

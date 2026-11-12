# DEVICE RECONCILIATION — Batch 19 (33 NEW Sky reels, #17–#49)

**Date:** Mon 2026-11-09 · **Code worker:** Batch 19
**Sources:** `decode-1-summary.md` (worker 1, reels #17–27) +
`decode-2-summary.md` (worker 2, reels #28–38) +
`decode-3-summary.md` (worker 3, reels #39–49) + per-reel `DECODE.md` files in
`~/workspace/claude-editing/research/video-harvest/instagram/batch-19-sky-full-profile/reels/`.

## The collision

All three workers proposed devices numbered D38–D44 — for DIFFERENT devices.
The provisional D-numbers are collision-tainted and are NOT reused. Batch 18
(origin reel Dcc84V5jc6D) already claimed D26–D37 in the registry
(`sky_devices.py` — D26 dashed loop arrow … D37 staggered figure pair, all
implemented). Batch 19 therefore starts at **D38** and runs sequentially to
**D54** — 17 new devices, 1 merge, 5 collab-only (not implemented).

## Reconciliation table

| Final D | Device name | Source worker(s) + provisional numbers | Reels | Dedup decision |
|---|---|---|---|---|
| D38 | POV-desk hook-doc | W1 D38 | #17 DevpJZLk6Km, #18 Deuue12jmIc, #21 DepxHOliSP4 | NEW |
| D39 | Subject photo insert | W1 D40 | #17, #18, #21 | NEW |
| D40 | POV scene label (pill / full-width bar) | W1 D41 | #19 DeqNswuE2Fd (pill), #23 DeIkaFAlMQO (bar), #25 DeBAfaYijwf (bar) | NEW — one device, two geometries (worker 1's own call) |
| D41 | Spine framework diagram | W1 D42 | #24 DeGQ3NAC2f9 | NEW |
| D42 | Question card + outcome fork | W1 D43 | #21 DepxHOliSP4 | NEW |
| D43 | View-count badge (eye + count, floats above phone exhibit) | W1 unnumbered (D39 slot if split out) | #17 (both exhibits), #18 (exhibit 1 only) | NEW — split out as its own device per the task brief; NOT part of D9/D38 |
| D44 | POV mini-window presentation | W2 D38 | #32 DSI5QVwEnIm | NEW — distinct from D38 (desk POV vs centred mini-window on black ground) |
| D45 | Kinetic-type black card | W2 D39 | #31 DSQeVmBk12d | NEW |
| D46 | Vertical split-screen, reactor left / exhibit right | W2 D40 | #28 DZXu4j9ATXP | NEW — distinct from D48 (vertical vs horizontal split; worker 2: "do not conflate") |
| D47 | Binary label pair, anchored | W2 D41 | #35 DSB8X22kSfe | NEW |
| D48 | Stacked split-screen, exhibit top / reactor bottom (persistent) | W2 D42 **MERGED WITH** W3 D38 | #36 DRoLuFRAnwh, #37 DRgQLh3Ak-3, #38 DReMeuugsJY, #39 DRXfqHcAkve, #40 DRVVqymgpxz, #49 DRjEF7xAkLJ | **MERGED — one device.** Both specs describe the same technique: persistent horizontal split, whole reel, exhibit top / reactor bottom, thin white divider (~2 px), exhibit content swaps on the speaker's beats, geometry never moves, reactor captions at the top of the reactor half just below the divider, bottom half one continuous take. W2's "screen recording with chrome intact" and W3's "top half swaps ~every 6–9 s" are the same behaviour described from different reels. |
| D49 | Red annotation outline (ellipse / rectangle / glowing ring) | W3 D39 | #39, #40, #44 DOWgvE0Ezgs, #49 | NEW — Sky's OWN red, a semantic "bad/look here" red ON a proof screen; implemented with the GOLD remap in Q's lane per the palette rule (see device docstring) |
| D50 | Gradient script headline (green→purple) | W3 D40 | #41 DQDYFFHif7v, #42 DP2_6r7DQ60, #43 DP4r6BbEvHg, #44, #46 DJccT_xSWuT | NEW — gradient + glow + script face transfer; colours remap to PWC teal→gold (purple #863BC5 / #5421A0 sampled, never emitted) |
| D51 | Video-game player-stats T-pose card | W3 D41 | #46 DJccT_xSWuT (Warren + Sky Tan, matched pair) | NEW |
| D52 | Human/AI split card 70% YOU / 30% AI | W3 D42 | #43 DP4r6BbEvHg | NEW — distinct from D27 (donut split of IG insights); a two-actor verdict card, not a chart |
| D53 | SMPTE colour-bars "SHOW PROOF" gag | W3 D43 | #41 DQDYFFHif7v | NEW — **flagged single-use** until a second example appears; builder carries `single_use=True` |
| D54 | Grid-background workflow strip | W3 D44 | #43 DP4r6BbEvHg | NEW — distinct from D13 (D13 = row of steps activating in place; D54 = black grid ground, ONE step centred at a time, steps slide horizontally) |

## Collab-only — NOT implemented as Sky devices (L-series, Andrew Lee's)

Recorded in `GAPS.md` (G-20) as "Andrew Lee's, not Sky's — do not use in Sky
edits." They appear in reels #47 DFwJPYpy7DM and #48 DFtUjlTS4a4, uploaded by
`adotleee` (Andrew Lee), not Sky. If a later SKY reel uses the same technique,
it may be promoted to a D-device then — not before.

| L-series | Device | Reels |
|---|---|---|
| L1 | White-ground logo verdict card | #47 (Slack, Notion, Go High Level, Zoom, Calendly) |
| L2 | Yellow highlight-pill phrase swap | #47 ("$25k $30k"), #48 ("Freelance Editor") |
| L3 | Client-count avatar loop | #47 ("SIX CLIENTS" + 6 avatar circles + loop arrow) |
| L4 | White-ground profile-header interstitial | #48 (@skytanventures + Follow button) |
| L5 | Figure headline, white numeral + yellow script | #48 ("100" + "Comments") |

## Other dedup decisions (same technique = ONE device)

- **W1 D41 two geometries** (pill top-left #19 vs full-width top bar #23/#25):
  one device, `geometry="pill"|"bar"` parameter — the worker's own call.
- **W2 D40 vertical split vs D48 stacked split:** NOT merged — different
  orientation (55/45 left/right vs ~50/50 top/bottom), different reactor
  behaviour (watches laptop, turns to camera at the verdict vs continuous
  take below the exhibit). Same family, two devices.
- **D54 vs D13:** NOT merged — D13 activates steps in a visible row; D54
  shows one step centred on a grid ground and slides steps horizontally.
- **D52 vs D27:** NOT merged — D27 is an IG-insights donut whose split
  values update; D52 is two labelled actors (head cutout + logo) with
  percentages, a verdict not a chart.
- **D49 vs D4/D17:** NOT merged — D4/D17 are boards/grids with verdict
  treatments; D49 is a free annotation drawn ON a proof screen.
- **D38 vs D44:** NOT merged — D38 is a live over-the-shoulder desk shot
  with a typing Notion doc; D44 is a static centred mini-window on a black
  ground with a POV line above it. Both are "POV presentations" and nothing
  else in common.
- **D43 view badge vs D46's 26.9M badge:** NOT the same element. D43 is
  Sky's floating badge ABOVE a phone exhibit (#17/#18). DZX's "👁 26.9M" is a
  dark pill bottom-centre of the exhibit side, part of the exhibit's own
  presentation — it stays inside D46, not D43.
- **2025-era caption systems (W3):** white italic serif top-of-reactor-half
  (#39/#40/#49) and white sans ALL-CAPS (#41–#44/#46) are ERA VARIANTS of D1,
  not new devices. The serif face stays Option 2 per Q's Nov 9 cut order;
  the sans-caps system is Option 1 (Sky's own 2025 system).

## Numbering note for Batch 18

Batch 18's coordinator was still working when Batch 19 was implemented. Its
teardown (`EDIT-TEARDOWN.md`) already claims D26–D37 and `sky_devices.py`
already implements D26–D37, so there is no collision: Batch 19 starts cleanly
at D38. If Batch 18 adds anything beyond D37, it must coordinate — D38–D54
are now taken.

## Counts

- New devices implemented: **17** (D38–D54)
- Merged as duplicates: **1** (W2 D42 + W3 D38 → D48)
- Collab-only, not implemented: **5** (L1–L5)
- Total Batch 19 proposals: 6 (W1, incl. badge) + 5 (W2) + 7 (W3) = 18
  Sky proposals → 17 devices after the 1 merge; + 5 L-series = 23 proposals
  reconciled.

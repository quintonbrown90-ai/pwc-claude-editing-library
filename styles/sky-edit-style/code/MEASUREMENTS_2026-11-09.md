# Measurements — Nov 9, 2026 (frame-level, from the real videos + the first HyperFrames render)

Source videos: `~/workspace/goals/realskytan-style-steal-for-q-s-content/hidden_files/priority15_videos/`
(01–15, H.264 720×1280, 30 fps). Frames extracted to `/tmp/sky_meas/` (ephemeral).
All coordinates are 1080×1920 unless noted.

## D12 era timeline — VERIFIED, closes G-07 D12 mechanics
Source: `11_De-A2dvCeV3.mp4`, frames @40.2 s and @41.2 s.
- The line is STATIC and FULL-WIDTH from the first frame (does NOT extend progressively).
- Nodes pop in sequence ~0.5 s apart; each node = accent ring + filled dot on the line, label ABOVE the line.
- Past-era labels white, current/future-era label in accent orange.
- The active node's example thumbnails cluster UNDER it (2×3 grid, dashed accent border).
- Line y ~300/1920.
- Implemented in `sky_devices.d12_timeline`; tested in `tests/test_sky_code.py`.

## D5 — checklist VERIFIED, chapter card still [EST]
Source: `05_DfQ4E1Hjn0n.mp4`, frames @0.6 s and @1.5 s.
- DfQ4 shows a numbered white-pill checklist — accent title ("5 Content Types") top, 5 white
  rounded pills stacked ("01 Gamification", etc.); pending rows blurred/dim, sharpen as they
  appear; current row highlights in accent when its section starts; recurs per section + full recap.
- Recorded as the `D5-list` variant in code (`sky_devices.d5_checklist`).
- The big-numeral chapter card (numeral 150–220 px + name + definition) is a different,
  still-[EST] device (`d5_chapter_card`).

## DfX2 / DfQ4 framing — MEASURED (corrects older defaults)
Source: `01_DfX2qwQGagM.mp4` @2.0 s; `05_DfQ4E1Hjn0n.mp4`.
- Face box ≈ x345–735, hair top ~y720, chin ~y1170 (1080×1920 coords).
- D2 headline "Good Content Strategy" spans y~1245–1575/1920 over the torso below the chin;
  caption "sign of a" at ~y1230/1920. DfQ4 captions ("types", "want") at ~y1245/1920.
- This corrects the old default face box (340,500,400,450) and caption band (y1090).
- Default face box in code is now (345,720,390,450); override per take with `--face-box`.

## D2 headline vs caption band — conflict + resolution (Nov 9 render)
- Conflict: STYLE-GRAMMAR.md's 1075–1110 caption overlap (other reels' teardown coords) vs
  these frame measurements (~1230–1245). Frame measurement wins for these reels; record per take.
- The measured DfX2 headline top (chin+75 ≈ y1245) sits ~30 px above the caption band's
  visual bottom. In the first HyperFrames render the D2 kicker struck through the live
  caption glyphs (snapshot @0.5 s, verified by eye). Resolution in code: headline top =
  caption-clip bottom + 12 px (`sky_build_plan.py`: `d2_y = caption_y + 57`, i.e. chin+126;
  display ends ~chin+282, still inside the y1480 safe-zone bottom). QC P4b now checks
  D1×D2/D3 pairs (the old blanket D1 exemption is removed).
- D2 headline safe-zone tension stands: Sky's own headline block ends ~y1575, past the y1480
  safe-zone bottom. Recorded as a plan advisory ("frame audit decides"), not a plan failure.

## HyperFrames render verification (Nov 9, 2026)
Fixture: `code/tests/fixtures/words_small.json` (26 words, 0–9.0 s, fictional "The Filter").
Green/D4 hero plan: 13 caption groups, 20 events, 9.0 s. Orange/D12 hero plan: same shape.
- `sky_qc.py` plan gates P1–P8: PASS on both plans.
- `npx hyperframes lint` (CLI 0.9.26): 0 errors, 2 warnings — both `timeline_track_too_dense`
  (Track 4: 13 caption elements; Track 1: 6 device elements), accepted by design.
- `npx hyperframes check`: overall **ok=True** on both plans (lint/runtime/layout/motion/
  contrast all ok). Residuals: 1 `content_overlap` info (D2 inner vs its own kicker div —
  internal to the lockup, benign); 1–2 craft `line_unread` warnings (D14 end line holds
  1.20 s, under the 2.00 s a closing line needs — fixture duration, accepted); audio info
  (no sound — no A-roll in the fixture).
- Actual render (`npx hyperframes render`, 1080×1920, 30 fps, H.264, 9.0 s, ~366 KB):
  frame grabs confirm the board filling row by row, D2 headline, captions swapping on time,
  and the D14 end card (opaque navy card, teal border, "Comment" white + "WAITLIST" gold,
  centred). Render takes ~56 s in this container (software-GL screenshot capture).
- **Scene-root occlusion (found + fixed Nov 9).** The first project rendered devices
  invisible: the captions scene's opaque navy root background painted over the entire sky
  scene, and `check` reported 7 `text_occluded` errors. Fix: scene roots are TRANSPARENT
  (no background); the navy ground lives on the main root in `index.html` only. Root ids
  are `<comp>-root` (host and root must not share an id; two scenes must not both be
  id="root"). Regression tests in `tests/test_sky_code.py`.
- **Dict-text rendering (found + fixed Nov 9).** D2/D14 dict texts rendered as Python reprs
  ("the framework ['The Filter']", "Comment WAITLIST WAITLIST card"). Fix: per-device
  labels in `sky_hyperframes._label_text`/`_label_html` (D2 = small kicker line + big display;
  D14 = close_line only, keyword in gold). Hero board/checklist/chart titles now use the
  framework name, not the first part name.
- **Serif fallback (found + fixed Nov 9).** Non-caption text rendered in a serif fallback
  (font-family was set only on `.sky-d1`). Fix: `font-family: Inter, Arial, sans-serif` on
  the scene root so all inners inherit it.
- **D14 end card (found + fixed Nov 9).** The close line was top-aligned with a transparent
  background and landed on the board's title row. Fix: D14 renders as an opaque navy card
  (teal border, flex-centred, 64 px). The card is 20 px shorter than the board (360 vs 380),
  so a sliver of the board's bottom edge shows beneath it — reads as a layered card, accepted.
- **E2 freezedetect on graphics-only renders (explained, gate NOT weakened).** E2 failed on
  the A-roll-less test render (5 freezes): without footage the only motion is thin caption
  strokes — a full caption swap changes only ~0.28–0.61% of pixels (measured with PIL),
  right at freezedetect's n=0.003 noise floor. The frames prove the captions swap on time.
  E2 applies to finished videos WITH A-roll; a graphics-only grade uses the frame-sequence
  check instead.
- **Disk note.** `/tmp` is a 512 MB tmpfs (0.3 GB free during the run — the render refuses
  there). Render from a project copy on the home disk (`~/workspace/.tmp-sky-render/`)
  with `TMPDIR` pointed there.

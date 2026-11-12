# Batch 18 — Sky origin reel: motion-clip index

**Source reel:** Sky Tan (@realskytan) — https://www.instagram.com/reel/Dcc84V5jc6D/
— shortcode `Dcc84V5jc6D`, posted Aug 25, 2026, 54.23 s, 1080×1920, 30 fps.
**Local video:** `~/workspace/claude-editing/uploads/QUARANTINE/niche-v9/Dcc84V5jc6D.mp4`
**Batch folder:** `~/workspace/claude-editing/research/video-harvest/instagram/batch-18-sky-origin/`

**What is copied here vs what lives on disk (G-18 pattern):** `DECODE.md`,
`EDIT-TEARDOWN.md` and `words.json` are copied into this folder (146 KB total).
The 17 motion clips (~15.6 MB) and 51 keyframes are NOT copied — open them at
`motion_refs/` in the batch folder above. Copying them would add 68 files and
push the skill further over the 200-file web-upload limit (see MANIFEST.md §6).

**In this folder:**
- `DECODE.md` — content decode: 8 spoken beats B1–B8 + 11 caption beats C0–C10,
  261 words, speaking rate 4.81 wps, 9 pauses >0.20 s. The origin story is in
  the CAPTION, not the spoken audio; the spoken audio is a caption-template
  pitch and the caption IS the live example — one device, two synchronized
  layers (T-03/T-16, D32 + D36).
- `EDIT-TEARDOWN.md` — 1,155-line edit teardown, §§0–11: 17 techniques T-01–T-17,
  new devices D26–D37 (§7), two-option audit (§8), grade-ready matched pairs
  (§10), 19 gaps G1–G19 (§11).
- `words.json` — faster-whisper `small` word timings (261 words).

## Motion clips (17) + keyframes (51) — `motion_refs/` in the batch folder

| Technique | Folder | Clip | Keyframes (3) |
|---|---|---|---|
| T-01 hook headline | `hook-headline/` | `hook-headline_0.0-3.6s.mp4` | in 0.05 s, hold 1.5 s, exit 3.35 s |
| T-02 caption hard cut | `caption-hard-cut/` | `caption-hard-cut_26.2-27.1s.mp4` | in 26.24 s, hold 26.5 s, change 26.9 s |
| T-03 origin doc, dim | `doc-origin-dim/` | `doc-origin-dim_1.0-3.5s.mp4` | in 1.2 s, hold 2.0 s, hold 3.2 s |
| T-04 comment screenshots | `comment-screenshots/` | `comment-screenshots_3.8-5.6s.mp4` | in 4.0 s, hold 4.8 s, hold 5.4 s |
| T-05 headline + arrow + doc | `headline-template-arrow/` | `headline-template-arrow_5.6-7.0s.mp4` | in 5.8 s, hold 6.4 s, hold 6.9 s |
| T-06 linear count-up | `countup-linear/` | `countup-linear_6.9-8.8s.mp4` | early 77+ 7.2 s, mid 261+ 7.9 s, late 445+ 8.6 s |
| T-07 phone + sections | `phone-mockup-sections/` | `phone-mockup-sections_8.6-11.2s.mp4` | in HOOK 9.4 s, LEAD 10.5 s, LEAD 11.0 s |
| T-08 donut chart | `donut-chart/` | `donut-chart_10.6-13.0s.mp4` | in 10.85 s, hold 11.5 s, hold 12.5 s |
| T-09 donut value update | `donut-value-update/` | `donut-value-update_15.2-17.6s.mp4` | before 15.4 s, mid 16.2 s, after 17.2 s |
| T-10 dot columns | `dot-columns/` | `dot-columns_10.8-12.2s.mp4` | in 10.9 s, hold 11.5 s, hold 12.0 s |
| T-11 thumbnail wall | `thumb-wall-slide/` | `thumb-wall-slide_21.8-25.2s.mp4` | slide 22.5 s, settled 23.5 s, float 24.8 s |
| T-12 doc + highlight sweep | `doc-highlight-sweep/` | `doc-highlight-sweep_26.2-29.2s.mp4` | beat 1 26.5 s, beat 2 28.0 s, beat 2 29.0 s |
| T-13 proof columns | `profile-proof/` | `profile-proof_38.3-40.5s.mp4` | in 38.5 s, hold 39.5 s, hold 40.2 s |
| T-14 staggered figures | `figures-land/` | `figures-land_40.4-42.8s.mp4` | $700K 41.0 s, $2–4M 41.5 s, hold 42.3 s |
| T-15 Claude prompt doc + UI | `claude-prompt-doc/` | `claude-prompt-doc_44.0-47.0s.mp4` | in 44.3 s, hold 45.5 s, hold 46.5 s |
| T-16 origin doc returns sharp | `origin-doc-return/` | `origin-doc-return_49.3-54.2s.mp4` | in 49.8 s, hold 51.0 s, close 53.5 s |
| T-17 bare close | `ending-bare/` | `ending-bare_52.5-54.2s.mp4` | bare 52.7 s, bare 53.5 s, last 54.1 s |

Also in the batch folder: `frames/` (54× 1 fps), `strips/` (30 fps strips),
`capband_*.jpg` (caption-band montages), `sheet1–3.jpg` (contact sheets),
`spectro_windows.png`, `envelope.png`, `BATCH-18-Q-LINKS.md`.

## Era note (load-bearing)

This reel (shortcode `Dcc…`, Aug 25, 2026) PREDATES the 15 priority reels
(`De…`/`Df…`) the v3 measurements came from. Where it deviates from v3 —
caption groups 2–5 words (not 1–3), yellow keyword INSIDE the caption (not a
separate headline), linear count-up (not expo), speaking rate 4.81 wps (above
v3's 3.93–4.73) — that is an era difference, not a v3 error. Record both;
do not overwrite v3. Code: `d1_captions(..., era="dcc")` + `d2_hook_build()`;
devices D26–D37 in `code/sky_devices.py`.

# examples/ — MANIFEST

**Profile mastered:** Sky Tan — @realskytan — https://www.instagram.com/realskytan

## What is in this folder vs what lives on disk

The 15 priority videos (~109 MB total) and the teardown frames (~47 MB) and contact sheets
(~62 MB) are **already downloaded and are NOT duplicated here** — duplicating them would push
this folder (and its Claude skill zip, limit 30 MB) far over budget and add zero information.
This folder carries the **full text decodes**: per-reel frame-by-frame notes, word-level
transcripts, the motion teardown, the carousel breakdown, the browser-verified record, and the
form catalogue. The manifest below gives the exact on-disk path, filename, byte size, duration
and frame count for every video, so any editor can open the exact source file in seconds.
No video was re-downloaded for this build.

## 1. The 15 priority reels (Q's named target set)

Source dir: `~/workspace/goals/realskytan-style-steal-for-q-s-content/hidden_files/priority15_videos/`
Sizes/durations verified by `ls -l` Nov 9, 2026. ffprobe durations are from the motion
teardown; browser estimates are from the Nov 6 live pass (they differ — ffprobe wins).

| File | Shortcode | Size | Duration | Topic |
|---|---|---|---|---|
| `01_DfX2qwQGagM.mp4` | DfX2qwQGagM | 6,062,628 bytes | 53.9s (ffprobe) / ~40s (browser est.) | Good Content Strategy — Leila Hormozi content filter |
| `02_DfU49SJAFYH.mp4` | DfU49SJAFYH | 10,462,522 bytes | 103.8s (ffprobe) / ~70s (browser est.) | TCM practitioner 1.1M-view video, retention breakdown |
| `03_DfTawo5jHMH.mp4` | DfTawo5jHMH | 6,252,114 bytes | 59.7s | The 4 Questions Filter |
| `04_DfSf5v8j73o.mp4` | DfSf5v8j73o | 5,622,262 bytes | 56.7s | Drop-offs you actually want — retention deep-dive |
| `05_DfQ4E1Hjn0n.mp4` | DfQ4E1Hjn0n | 7,872,580 bytes | 75.6s | 5 Content Types — 100k in 6 months |
| `06_DfPxqFPAY4_.mp4` | DfPxqFPAY4_ | 8,609,262 bytes | 77.5s | Viral Twice — collab posting |
| `07_DfLaEFNDKkv.mp4` | DfLaEFNDKkv | 7,301,592 bytes | 93.9s | Power Words — unskippable hooks |
| `08_DfIYshekeF3.mp4` | DfIYshekeF3 | 8,292,272 bytes | 60.5s | ChatGPT ideas / legit content strategy |
| `09_DfDuMnCjNdE.mp4` | DfDuMnCjNdE | 8,250,291 bytes | 68.7s | Shallow formats — why your audience doesn't value your opinions |
| `10_DfA9L-PHYWp.mp4` | DfA9L-PHYWp | 7,826,838 bytes | 77.2s | Content-Offer Fit — no content strategy |
| `11_De-A2dvCeV3.mp4` | De-A2dvCeV3 | 8,522,286 bytes | 63.2s | These formats are officially dead — fast content = fast food |
| `12_Dez4fPJCR74.mp4` | Dez4fPJCR74 | 6,706,339 bytes | 58.9s | The absolute worst content strategy is teaching |
| `13_DexJ-qWiWdY.mp4` | DexJ-qWiWdY | 6,474,604 bytes | 56.0s | The ultimate storytelling caption for Instagram |
| `14_DeYKkAIgVfL.mp4` | DeYKkAIgVfL | 10,901,764 bytes | 93.2s (ffprobe) | Jessi Jean relaunch / CAREER CONFUSED — participation loop, trust dot-grid, affiliate army (frame-verified Nov 9, 2026) |
| `15_DeSTWxcDTA7.mp4` | DeSTWxcDTA7 | 5,337,823 bytes | 43.0s (ffprobe) | Hiring / views-refresh — B&W "DON'T" beat, New Post placeholder, floating head (frame-verified Nov 9, 2026) |

**Nov 9, 2026 frame-measured pass:** all 15 videos are now frame-verified (the three
formerly audio-only reels 12/14/15 + the DfA9 ending are measured). Evidence log:
`examples/PREMIUM_DEPTH_MEASUREMENTS.md`. Families: 01–08, 11, 13 GREEN; 09, 10, 12, 14,
15 ORANGE. Note: `examples/reels/` holds notes + transcripts for 13 of the 15 (01–13) plus
DfZ_q_pFbX1 (extra); reels 14/15 are video-only here (no text decode in this folder).

Total: 15 files, 111,844 KB on disk (per `ls` total). Plus the 14th teardown reel DfZ_q_pFbX1
("Why Process Crushes", 37.2 s, @allanpeters) — in the motion teardown but NOT in the priority
15; its frames/notes/transcript are in the teardown set below.

## 2. Motion teardown (14 reels, ~943 s)

Source dir: `~/workspace/claude-editing/examples/sky/motion-teardown/`
Copied into this folder: `SKY_MOTION_TEARDOWN.md` (793 lines — the full device index + global
grammar), `examples/reels/notes_<ID>.md` (14 files, 73,401 bytes total — per-reel sheet-by-sheet
catalogues), `examples/reels/transcript_<ID>.json` (14 files, 288,823 bytes total — word-level
faster-whisper base.en transcripts).
NOT copied (size): `frames/<ID>/` (~4 fps JPGs, 270×480) and `sheets/<ID>/` (30-frame contact
sheets). Frame counts per reel, verified Nov 9, 2026:

| Reel | 4-fps frames on disk |
|---|---|
| De-A2dvCeV3 | 253 |
| DexJ-qWiWdY | 224 |
| Dez4fPJCR74 | 235 |
| DfA9L-PHYWp | 308 |
| DfDuMnCjNdE | 274 |
| DfIYshekeF3 | 244 |
| DfLaEFNDKkv | 380 |
| DfPxqFPAY4_ | 312 |
| DfQ4E1Hjn0n | 306 |
| DfSf5v8j73o | 228 |
| DfTawo5jHMH | 239 |
| DfU49SJAFYH | 426 |
| DfX2qwQGagM | 220 |
| DfZ_q_pFbX1 | 153 |

Motion clips (28 clips, `motion_clips/`): `motion-clips-manifest.json` and
`motion-clips-line_draw_measurements.json` are copied into `examples/reels/`; the clip MP4s
themselves (~43 MB dir) are NOT copied — open them at the source dir above.

## 3. Carousel examples (9 posts, 51 slides)

Source dir: `~/workspace/claude-editing/examples/sky/carousel-styles/` (slide MP4s, 1080×1350).
Copied into this folder: `examples/carousels/CAROUSEL_BREAKDOWN.md` (the full archetype A–E
breakdown + PWC copy spec). The 51 slide MP4s are NOT copied (size) — open them at the source
dir. Post shortcodes: De-cMQMjZjj, De2kC4nEptM, DevFnZxlCQO, DexfsH5l0q6, DfDwkljmAXg,
DfIyn6xCsUH, DfLku2QkZcP, DfQPBSpkRUG, DfS-L51j4hK.

## 4. Source documents copied into `examples/sources/`

- `SKY_MOTION_VERIFIED.md` — browser motion-verified record, Nov 6, 2026, 1:06–1:47 AM CST.
- `SKY_PRIORITY15_BREAKDOWN.md` — expert breakdown (§1 device library, §2 per-reel inventories,
  §3 mapping, §4 recipe, §5 honesty box).
- `SKY_TEARDOWN.md` — 13-form catalogue from the 113-post survey of his whole grid.
- `SKY-SCORE.md` — device score card D1–D14 + E1–E10 (levels 0–3, evidence-gated).
- `creator-systems-sky-part.md` — the `parts/creator-systems/sky.md` part (≤50 KB).
- `realskytan-system-SKILL.md` — the existing Muse-side skill this folder is built from.
- `SKY_STYLE.md` — the Nov 6 Sky style doc (PWC engine: sky.py/render.py/mix.py plans).

## 5. How to use these examples

1. Pick the video's ONE model reel first (the reel Q's brief names) — grade against that reel,
   model the rest of the system around it.
2. Read its `notes_<ID>.md` + `transcript_<ID>.json`, then watch the MP4 at the source path
   above (or its frames in `frames/<ID>/`) before building anything in its form.
3. For carousel builds, read `CAROUSEL_BREAKDOWN.md` and open the matching slide MP4s — every
   slide is a video; grade motion, not stills.
4. Anything marked UNVERIFIED / [EST] in these files is a placeholder, not a measured value.
   Check `GAPS.md` before relying on it.

## 6. Batch 18 — Sky origin reel Dcc84V5jc6D (Aug 25, 2026, Dcc-era)

Source: https://www.instagram.com/reel/Dcc84V5jc6D/ — Sky Tan (@realskytan).
Video on disk: `~/workspace/claude-editing/uploads/QUARANTINE/niche-v9/Dcc84V5jc6D.mp4`
(54.23 s, 1080×1920, 30 fps; 583 likes / 1,107 comments at download).
Batch folder: `~/workspace/claude-editing/research/video-harvest/instagram/batch-18-sky-origin/`

Copied into this folder (`examples/batch-18-sky-origin/`, 146 KB total):
`DECODE.md` (40,824 bytes — 8 spoken beats B1–B8 + 11 caption beats C0–C10, 261 words,
speaking rate 4.81 wps, 9 pauses >0.20 s), `EDIT-TEARDOWN.md` (91,535 bytes — 17
techniques T-01–T-17, devices D26–D37, two-option audit, grade-ready matched pairs, gaps
G1–G19), `words.json` (13,990 bytes — faster-whisper `small` word timings), plus
`CLIPS.md` (index of the motion clips + keyframes below).

NOT copied (size + file-count — G-18 pattern): `motion_refs/` (17 technique clips +
51 keyframes, 15,624,282 bytes), `frames/` (54× 1 fps), `strips/` (30 fps strips),
`capband_*.jpg`, `sheet1–3.jpg`, `spectro_windows.png`, `envelope.png` — open them in
the batch folder above.

**Why this reel matters:** the origin story is in the CAPTION, not the spoken audio —
the spoken audio is a caption-template pitch and the caption IS the live example (one
device, two synchronized layers: D32 + D36). It predates the 15 priority reels, so its
deviations from v3 (caption groups 2–5 words, yellow keyword inside the caption, linear
count-up, 4.81 wps) are Dcc-era variants, not v3 corrections. Its whole system is ONE
locked-off take (zero cuts/zoom over 54.2 s) with dry voice only. Devices D26–D37 are
implemented in `code/sky_devices.py` (55 devices registered, 83 unit tests); gaps are
`GAPS.md` G-19 (B18-G1–B18-G19).

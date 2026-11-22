# @realskytan — reference harvest INDEX

**Creator:** Sky Tan — @realskytan — https://www.instagram.com/realskytan
**Profile (connector, 2026-11-15):** 117,928 followers · 2,460 following · 375 posts (profile count) · Canada · Bio: "Clients: 100m views / 1m+ rev / 800k followers" · DFY social media / personal branding (ClipCut).

**Attribution:** every video, transcript and breakdown in this folder is Sky Tan's work, harvested as study/reference material for the Sky edit style. None of it is Q's work and it must never be presented as Q's.

## Totals (snapshot at INDEX generation)

- Enumerated in `catalog.json`: **572** unique posts returned by the instagram-cli route (559 video, 10 carousel, 3 story-highlight images).
- Videos/reels: **559**
- Downloaded (`.mp4` in this folder): **139**
- Transcribed (`.transcript.txt`, actual audio): **139**
- Broken down (`.breakdown.md`, 7-section format): **33**
- Carousels/image posts: catalog-only in this harvest (listed below the video table).
- **Added after the harvest (Q, Nov 16, 2026):** row 560, `Dfz42Ogihlv` — a reel Q sent directly as another example of Sky's editing; downloaded, transcribed and broken down the same day and filed beside this index (mp4, tx, bd). It is not part of the connector's 572-post catalog enumeration above. Totals updated to the live folder counts on that date.

## Enumeration honesty notes

- The connector's desc pagination returned 2 pages (118 rows, 116 unique) and then reported `has_next_page=true` with a null cursor; enumeration was completed with `--since/--until` monthly windows (2024-05 → 2026-11), which surfaced 572 unique URLs in total. That EXCEEDS the profile's own post count (375), so the connector over-returns (its dates for many posts are also shifted vs the posts' shortcode eras — e.g. the Df-era reels are dated Oct–Nov 2026 by the connector). All per-post fields in the table are connector-returned values, labelled as such; treat dates/likes as approximate.
- Two shortcodes known locally were NOT in the first desc pages but ARE in the monthly catalog: Dcc84V5jc6D (origin reel) is included. DeGQ3NAC2f9 (a reel thumbnailed in Nov 2026 local notes, 238 likes / 30 comments then) does not appear in the connector catalog at all — it is listed in the gaps under the table.
- Prior local corpus (not re-downloaded): 49 reels were previously decoded to a higher bar (Batch 18/19/36) — 15 priority + origin + 33 more; their full decodes live in the style folder's `examples/` and `SKY-TEARDOWN-MASTER.md`. Only the 17 with local MP4s were copied into this folder (additions only, originals untouched). The other 32 previously-decoded reels are in the catalog and in the download queue like everything else.

## Reused local material (not re-downloaded / not re-transcribed)

- 15 priority MP4s copied from `~/workspace/goals/realskytan-style-steal-for-q-s-content/hidden_files/priority15_videos/` (also at `~/workspace/claude-editing/examples/sky/priority15/`).
- DfZ_q_pFbX1.mp4 copied from `~/workspace/claude-editing/examples/sky/priority15/extra_refs/`.
- Dcc84V5jc6D.mp4 copied from `~/workspace/claude-editing/uploads/QUARANTINE/niche-v9/Dcc84V5jc6D.mp4`.
- 16 transcripts converted from existing word-level faster-whisper JSONs in `sky-edit-style/examples/reels/transcript_<code>.json`; Dcc84V5jc6D's from `examples/batch-18-sky-origin/words.json` (faster-whisper small).
- 16 breakdowns distilled from the frame-by-frame decodes in `sky-edit-style/examples/reels/notes_<code>.md` (4 fps contact sheets + Batch 36 measured sound/transition inventories); Dcc84V5jc6D's from Batch 18 `DECODE.md` + `EDIT-TEARDOWN.md` + `CLIPS.md`.
- All other transcripts in this folder are fresh faster-whisper `base` (int8 CPU) transcriptions of the actual audio, run in this harvest. On-screen frame captions were never used as transcript source.

## How to resume the harvest (all scripts are resumable — they skip existing files)

```bash
~/workspace/.venv_fw/bin/python ~/workspace/sky-harvest-work/pipeline.py        # downloads (engagement order) + sheets + transcripts
~/workspace/.venv_fw/bin/python ~/workspace/sky-harvest-work/download_only.py   # download-only sweep (reverse order)
python3 ~/workspace/sky-harvest-work/make_breakdowns_auto.py                     # breakdowns for transcribed reels lacking one
python3 ~/workspace/sky-harvest-work/make_index.py                               # regenerate this INDEX with fresh counts
```
Logs: `~/workspace/sky-harvest-work/pipeline.log`, `download_only.log`, `failures*.txt`. Contact sheets: `~/workspace/sky-harvest-work/sheets/`.

## Per-video table (engagement order: likes + comments, connector values)

| # | Shortcode | Date (connector) | Dur | Likes | Comments | Hook (first spoken line, actual audio) | Files |
|---|---|---|---|---|---|---|---|
| 1 | [DambEp1igDW](https://www.instagram.com/reel/DambEp1igDW/) | 2026-07-09 | 35s | 35725 | 1717 | Hook, lead, body one, open loop one, body two, open loop two, body three, CTA. | mp4, tx, bd |
| 2 | [DVCXkhUkhFT](https://www.instagram.com/reel/DVCXkhUkhFT/) | 2026-02-21 | 66s | 10368 | 114 | I'm rolling over gold observed visual hook with my car for an important business reason op | mp4, tx, bd |
| 3 | [DGCpTZZxzSX](https://www.instagram.com/reel/DGCpTZZxzSX/) | 2025-02-13 | 62s | 7623 | 113 | This is where your face should be. | mp4, tx, bd |
| 4 | [DJBG8rZCS_B](https://www.instagram.com/reel/DJBG8rZCS_B/) | 2025-04-28 | 60s | 7267 | 97 | This coach that coaches your favorite coaches coach uses the Snapchat content strategy to  | mp4, tx, bd |
| 5 | [DexJ-qWiWdY](https://www.instagram.com/reel/DexJ-qWiWdY/) | 2026-10-21 | 56s | 3339 | 1428 | This is the ultimate storytelling caption for Instagram, and you need to have this for eve | mp4, tx, bd |
| 6 | [DH_zlmki-S8](https://www.instagram.com/reel/DH_zlmki-S8/) | 2025-04-03 | 65s | 3438 | 87 | How the fuck did WAP build a $2 billion empire in four years without making a single video | mp4, tx, bd |
| 7 | [DU3_MZeEwZm](https://www.instagram.com/reel/DU3_MZeEwZm/) | 2026-02-17 | 55s | 3415 | 27 | Be careful using this method. | mp4, tx, bd |
| 8 | [DfcoEvND95m](https://www.instagram.com/reel/DfcoEvND95m/) | 2026-11-07 | 56s | 2627 | 37 | Hey, man, will you write this hook out of 10 tips to sleep better? | mp4, tx, bd |
| 9 | [DGes0WMRT2Y](https://www.instagram.com/reel/DGes0WMRT2Y/) | 2025-02-24 | 47s | 2433 | 108 | I don't know who needs to hear this, | mp4, tx, bd |
| 10 | [DHFoooyu9Zz](https://www.instagram.com/reel/DHFoooyu9Zz/) | 2025-03-11 | 66s | 2321 | 87 | I'm sorry, I lied, I knew having a personal brand was a good thing. | mp4, tx, bd |
| 11 | [DbH80J4E60p](https://www.instagram.com/reel/DbH80J4E60p/) | 2026-07-22 | 39s | 2081 | 22 | Hey boss, ready to make some content? | mp4, tx, bd |
| 12 | [DVF6UE1Av0X](https://www.instagram.com/reel/DVF6UE1Av0X/) | 2026-02-22 | 122s | 1898 | 85 | by eating some chicken wings. | mp4, tx, bd |
| 13 | [Ddp4WQPDObn](https://www.instagram.com/reel/Ddp4WQPDObn/) | 2026-09-23 | 126s | 1517 | 454 | This is my entire content strategy in 60 seconds. | mp4, tx, bd |
| 14 | [DYOLB7BCSC3](https://www.instagram.com/reel/DYOLB7BCSC3/) | 2026-05-11 | 83s | 1875 | 42 |  | mp4 |
| 15 | [DG1nxjLyYKV](https://www.instagram.com/reel/DG1nxjLyYKV/) | 2025-03-05 | 56s | 1222 | 670 |  | mp4 |
| 16 | [DUJR7BPAYUn](https://www.instagram.com/reel/DUJR7BPAYUn/) | 2026-01-30 | 68s | 1666 | 76 |  | mp4 |
| 17 | [DVIdwgsjm6O](https://www.instagram.com/reel/DVIdwgsjm6O/) | 2026-02-23 | 56s | 1697 | 18 |  | mp4 |
| 18 | [Dcc84V5jc6D](https://www.instagram.com/reel/Dcc84V5jc6D/) | 2026-08-24 | 54s | 581 | 1107 | I guarantee you guys aren't caption -maxing enough because most of you guys are putting | mp4, tx, bd |
| 19 | [DcKpqu8GwiX](https://www.instagram.com/reel/DcKpqu8GwiX/) | 2026-08-17 | 67s | 1332 | 349 |  | mp4 |
| 20 | [DUwIKI9ErbS](https://www.instagram.com/reel/DUwIKI9ErbS/) | 2026-02-14 | 47s | 1609 | 23 |  | mp4 |
| 21 | [DUtujh4El-d](https://www.instagram.com/reel/DUtujh4El-d/) | 2026-02-13 | 104s | 1589 | 33 |  | mp4 |
| 22 | [DJrgpxKx8tb](https://www.instagram.com/reel/DJrgpxKx8tb/) | 2025-05-15 | 49s | 1227 | 32 |  | mp4 |
| 23 | [DTN7c4tDfWa](https://www.instagram.com/reel/DTN7c4tDfWa/) | 2026-01-07 | 41s | 1195 | 32 |  | mp4 |
| 24 | [DUwf5cWiQIG](https://www.instagram.com/reel/DUwf5cWiQIG/) | 2026-02-14 | 40s | 1046 | 10 |  | mp4 |
| 25 | [DMCxMFgNzIV](https://www.instagram.com/reel/DMCxMFgNzIV/) | 2025-07-13 | 50s | 912 | 84 |  | mp4 |
| 26 | [Dd4qHeeDaMv](https://www.instagram.com/reel/Dd4qHeeDaMv/) | 2026-09-29 | 35s | 629 | 334 |  | mp4 |
| 27 | [DbPmeRSkTYk](https://www.instagram.com/reel/DbPmeRSkTYk/) | 2026-07-25 | 32s | 904 | 17 |  | mp4 |
| 28 | [DUrdNZ2Cfzo](https://www.instagram.com/reel/DUrdNZ2Cfzo/) | 2026-02-12 | 53s | 832 | 36 |  | mp4 |
| 29 | [DMcBySJC7_n](https://www.instagram.com/reel/DMcBySJC7_n/) | 2025-07-22 | 45s | 833 | 23 |  | mp4 |
| 30 | [DUO_XDvkkbC](https://www.instagram.com/reel/DUO_XDvkkbC/) | 2026-02-01 | 32s | 818 | 16 |  | mp4 |
| 31 | [DSihUWik2Kx](https://www.instagram.com/reel/DSihUWik2Kx/) | 2025-12-21 | 61s | 769 | 46 |  | mp4 |
| 32 | [DIVhHG7CQgk](https://www.instagram.com/reel/DIVhHG7CQgk/) | 2025-04-11 | 46s | 780 | 29 |  | mp4 |
| 33 | [DSB8X22kSfe](https://www.instagram.com/reel/DSB8X22kSfe/) | 2025-12-08 | 47s | 725 | 44 |  | mp4 |
| 34 | [DG7bsUwur1s](https://www.instagram.com/reel/DG7bsUwur1s/) | 2025-03-07 | 51s | 548 | 178 |  | mp4 |
| 35 | [DJGTvSxxUyU](https://www.instagram.com/reel/DJGTvSxxUyU/) | 2025-04-30 | 51s | 663 | 30 |  | mp4 |
| 36 | [DUrpddfkTSm](https://www.instagram.com/reel/DUrpddfkTSm/) | 2026-02-12 | 77s | 677 | 13 |  | mp4 |
| 37 | [DU61ikpgRD7](https://www.instagram.com/reel/DU61ikpgRD7/) | 2026-02-18 | 43s | 667 | 11 |  | mp4 |
| 38 | [DU4BDM9Alfk](https://www.instagram.com/reel/DU4BDM9Alfk/) | 2026-02-17 | 60s | 649 | 12 |  | mp4 |
| 39 | [DV4UKFMiQFK](https://www.instagram.com/reel/DV4UKFMiQFK/) | 2026-03-14 | 37s | 614 | 23 |  | mp4 |
| 40 | [DUupJwAgnMy](https://www.instagram.com/reel/DUupJwAgnMy/) | 2026-02-13 | 89s | 624 | 8 |  | mp4 |
| 41 | [DciNlCHkVVC](https://www.instagram.com/reel/DciNlCHkVVC/) | 2026-08-27 | 130s | 583 | 48 |  | mp4 |
| 42 | [DJDuyD5RIl8](https://www.instagram.com/reel/DJDuyD5RIl8/) | 2025-04-29 | 61s | 400 | 205 |  | mp4 |
| 43 | [Dd1vedwDEL_](https://www.instagram.com/reel/Dd1vedwDEL_/) | 2026-09-28 | 52s | 494 | 80 |  | mp4 |
| 44 | [DUyfYguiXrU](https://www.instagram.com/reel/DUyfYguiXrU/) | 2026-02-15 | 45s | 551 | 16 |  | mp4 |
| 45 | [DJccT_xSWuT](https://www.instagram.com/reel/DJccT_xSWuT/) | 2025-05-09 | 47s | 421 | 136 |  | mp4 |
| 46 | [DZMELpvClde](https://www.instagram.com/reel/DZMELpvClde/) | 2026-06-04 | 67s | 531 | 9 |  | mp4 |
| 47 | [DU2U16dgkML](https://www.instagram.com/reel/DU2U16dgkML/) | 2026-02-16 | 26s | 528 | 10 |  | mp4 |
| 48 | [DV2RDB-kcFb](https://www.instagram.com/reel/DV2RDB-kcFb/) | 2026-03-13 | 54s | 522 | 12 |  | mp4 |
| 49 | [DKkhVZYyJZD](https://www.instagram.com/reel/DKkhVZYyJZD/) | 2025-06-06 | 39s | 349 | 170 |  | mp4 |
| 50 | [DNcWmR4u7Dq](https://www.instagram.com/reel/DNcWmR4u7Dq/) | 2025-08-16 | 14s | 349 | 170 |  | mp4 |
| 51 | [DUtS8Jzgtgj](https://www.instagram.com/reel/DUtS8Jzgtgj/) | 2026-02-13 | 123s | 507 | 11 |  | mp4 |
| 52 | [DSddjs2E7TL](https://www.instagram.com/reel/DSddjs2E7TL/) | 2025-12-19 | 68s | 499 | 17 |  | mp4 |
| 53 | [DHAWel_RYoh](https://www.instagram.com/reel/DHAWel_RYoh/) | 2025-03-09 | 62s | 488 | 26 |  | mp4 |
| 54 | [De-A2dvCeV3](https://www.instagram.com/reel/De-A2dvCeV3/) | 2026-10-26 | 63s | 468 | 43 | These formats are officially dead. | mp4, tx, bd |
| 55 | [DWW4iswAt1j](https://www.instagram.com/reel/DWW4iswAt1j/) | 2026-03-26 | 36s | 488 | 12 |  | mp4 |
| 56 | [DJ4L2KIP7QK](https://www.instagram.com/reel/DJ4L2KIP7QK/) | 2025-05-20 | 62s | 435 | 45 |  | mp4 |
| 57 | [DK1D9QFOvoN](https://www.instagram.com/reel/DK1D9QFOvoN/) | 2025-06-12 | 143s | 443 | 36 |  | mp4 |
| 58 | [Dez4fPJCR74](https://www.instagram.com/reel/Dez4fPJCR74/) | 2026-10-22 | 59s | 446 | 26 | The absolute worst content strategy for short form content is teaching because 60 seconds | mp4, tx, bd |
| 59 | [DcVOEGYEmQ2](https://www.instagram.com/reel/DcVOEGYEmQ2/) | 2026-08-21 | 44s | 398 | 69 |  | mp4 |
| 60 | [DJixx9AtMfk](https://www.instagram.com/reel/DJixx9AtMfk/) | 2025-05-11 | 59s | 450 | 16 |  | mp4 |
| 61 | [DeIkaFAlMQO](https://www.instagram.com/reel/DeIkaFAlMQO/) | 2026-10-05 | 51s | 437 | 29 |  | mp4 |
| 62 | [DaQo05WAGTb](https://www.instagram.com/reel/DaQo05WAGTb/) | 2026-07-01 | 59s | 450 | 12 |  | mp4 |
| 63 | [DUMXJFZEquH](https://www.instagram.com/reel/DUMXJFZEquH/) | 2026-01-31 |  | 374 | 83 |  |  |
| 64 | [DIcRmkCBJur](https://www.instagram.com/reel/DIcRmkCBJur/) | 2025-04-14 |  | 438 | 10 |  |  |
| 65 | [DcSx1kVirfh](https://www.instagram.com/reel/DcSx1kVirfh/) | 2026-08-21 |  | 405 | 42 |  |  |
| 66 | [DZLOHtXif0S](https://www.instagram.com/reel/DZLOHtXif0S/) | 2026-06-04 |  | 402 | 14 |  |  |
| 67 | [DSEitvcAo_H](https://www.instagram.com/reel/DSEitvcAo_H/) | 2025-12-09 |  | 392 | 17 |  |  |
| 68 | [DU2U939gkHA](https://www.instagram.com/reel/DU2U939gkHA/) | 2026-02-16 |  | 398 | 11 |  |  |
| 69 | [DHsMnqUidDu](https://www.instagram.com/reel/DHsMnqUidDu/) | 2025-03-26 |  | 386 | 14 |  |  |
| 70 | [DIGIBVTOE2n](https://www.instagram.com/reel/DIGIBVTOE2n/) | 2025-04-05 |  | 235 | 162 |  |  |
| 71 | [DdxAwodlOGG](https://www.instagram.com/reel/DdxAwodlOGG/) | 2026-09-26 |  | 348 | 46 |  |  |
| 72 | [DYoeeRSiKS7](https://www.instagram.com/reel/DYoeeRSiKS7/) | 2026-05-22 |  | 383 | 8 |  |  |
| 73 | [DJgW7tUi6-L](https://www.instagram.com/reel/DJgW7tUi6-L/) | 2025-05-11 |  | 373 | 16 |  |  |
| 74 | [DcPj3T5Apb6](https://www.instagram.com/reel/DcPj3T5Apb6/) | 2026-08-19 |  | 366 | 23 |  |  |
| 75 | [DIUYflXCNYf](https://www.instagram.com/reel/DIUYflXCNYf/) | 2025-04-11 |  | 290 | 95 |  |  |
| 76 | [DJlgVFdq6QM](https://www.instagram.com/reel/DJlgVFdq6QM/) | 2025-05-13 |  | 370 | 14 |  |  |
| 77 | [DaHop89Cdka](https://www.instagram.com/reel/DaHop89Cdka/) | 2026-06-27 |  | 372 | 8 |  |  |
| 78 | [DYRKpVWiGgK](https://www.instagram.com/reel/DYRKpVWiGgK/) | 2026-05-12 |  | 364 | 14 |  |  |
| 79 | [DINAOeXCjBV](https://www.instagram.com/reel/DINAOeXCjBV/) | 2025-04-08 |  | 364 | 13 |  |  |
| 80 | [DL2roQYyz6v](https://www.instagram.com/reel/DL2roQYyz6v/) | 2025-07-08 |  | 356 | 21 |  |  |
| 81 | [DaojGGYFXN2](https://www.instagram.com/reel/DaojGGYFXN2/) | 2026-07-10 |  | 370 | 7 |  |  |
| 82 | [DP4r6BbEvHg](https://www.instagram.com/reel/DP4r6BbEvHg/) | 2025-10-16 |  | 339 | 33 |  |  |
| 83 | [Daq-5E0jrYw](https://www.instagram.com/reel/Daq-5E0jrYw/) | 2026-07-11 |  | 365 | 6 |  |  |
| 84 | [DKf709svz3f](https://www.instagram.com/reel/DKf709svz3f/) | 2025-06-04 |  | 307 | 58 |  |  |
| 85 | [DGweSlLiyZP](https://www.instagram.com/reel/DGweSlLiyZP/) | 2025-03-03 |  | 343 | 18 |  |  |
| 86 | [DIKUnWJBKN8](https://www.instagram.com/reel/DIKUnWJBKN8/) | 2025-04-07 |  | 333 | 22 |  |  |
| 87 | [DGOwfWSyIYN](https://www.instagram.com/reel/DGOwfWSyIYN/) | 2025-02-18 |  | 310 | 44 |  |  |
| 88 | [DepxHOliSP4](https://www.instagram.com/reel/DepxHOliSP4/) | 2026-10-18 |  | 320 | 33 |  |  |
| 89 | [DYDiMXTvoNi](https://www.instagram.com/reel/DYDiMXTvoNi/) | 2026-05-07 |  | 325 | 27 |  |  |
| 90 | [DL514WJyioe](https://www.instagram.com/reel/DL514WJyioe/) | 2025-07-09 |  | 331 | 18 |  |  |
| 91 | [DLSdAF9t5lY](https://www.instagram.com/reel/DLSdAF9t5lY/) | 2025-06-24 |  | 249 | 99 |  |  |
| 92 | [Dfhxmlqk_wT](https://www.instagram.com/reel/Dfhxmlqk_wT/) | 2026-11-09 |  | 341 | 7 |  |  |
| 93 | [DU3-6qBE4Go](https://www.instagram.com/reel/DU3-6qBE4Go/) | 2026-02-17 |  | 335 | 10 |  |  |
| 94 | [DXziY8fi0B1](https://www.instagram.com/reel/DXziY8fi0B1/) | 2026-05-01 |  | 312 | 31 |  |  |
| 95 | [DF6mv4HiX3j](https://www.instagram.com/reel/DF6mv4HiX3j/) | 2025-02-10 |  | 311 | 31 |  |  |
| 96 | [DdVhpHODaTB](https://www.instagram.com/reel/DdVhpHODaTB/) | 2026-09-15 |  | 270 | 70 |  |  |
| 97 | [DLwOOugOYur](https://www.instagram.com/reel/DLwOOugOYur/) | 2025-07-05 |  | 258 | 81 |  |  |
| 98 | [DdKHEAnkYHq](https://www.instagram.com/reel/DdKHEAnkYHq/) | 2026-09-11 |  | 198 | 137 |  |  |
| 99 | [DVR6WrgEiG2](https://www.instagram.com/reel/DVR6WrgEiG2/) | 2026-02-27 |  | 320 | 12 |  |  |
| 100 | [DH5Myg-CerK](https://www.instagram.com/reel/DH5Myg-CerK/) | 2025-03-31 |  | 299 | 32 |  |  |
| 101 | [DGKdD0DRZbz](https://www.instagram.com/reel/DGKdD0DRZbz/) | 2025-02-16 |  | 301 | 27 |  |  |
| 102 | [Ddr2LfhAczO](https://www.instagram.com/reel/Ddr2LfhAczO/) | 2026-09-24 |  | 278 | 46 |  |  |
| 103 | [DLnyCjmBTIO](https://www.instagram.com/reel/DLnyCjmBTIO/) | 2025-07-02 |  | 307 | 14 |  |  |
| 104 | [DI0PBxvRGEJ](https://www.instagram.com/reel/DI0PBxvRGEJ/) | 2025-04-23 |  | 298 | 22 |  |  |
| 105 | [DdLGJLxiCne](https://www.instagram.com/reel/DdLGJLxiCne/) | 2026-09-11 |  | 258 | 59 |  |  |
| 106 | [DUJcrqlEtQH](https://www.instagram.com/reel/DUJcrqlEtQH/) | 2026-01-30 |  | 309 | 6 |  |  |
| 107 | [Dd2i55aj43S](https://www.instagram.com/reel/Dd2i55aj43S/) | 2026-09-28 |  | 296 | 12 |  |  |
| 108 | [DdH6kddjKHg](https://www.instagram.com/reel/DdH6kddjKHg/) | 2026-09-10 |  | 282 | 23 |  |  |
| 109 | [DKdtN5mOGfZ](https://www.instagram.com/reel/DKdtN5mOGfZ/) | 2025-06-03 |  | 280 | 19 |  |  |
| 110 | [DMSxnf9hgE3](https://www.instagram.com/reel/DMSxnf9hgE3/) | 2025-07-19 |  | 290 | 8 |  |  |
| 111 | [DZhJvzwki4e](https://www.instagram.com/reel/DZhJvzwki4e/) | 2026-06-13 |  | 285 | 12 |  |  |
| 112 | [DcHkvYTiAsy](https://www.instagram.com/reel/DcHkvYTiAsy/) | 2026-08-16 |  | 281 | 13 |  |  |
| 113 | [Daf3iwtk7Wi](https://www.instagram.com/reel/Daf3iwtk7Wi/) | 2026-07-07 |  | 277 | 5 |  |  |
| 114 | [DX-cleFCK2B](https://www.instagram.com/reel/DX-cleFCK2B/) | 2026-05-05 |  | 268 | 7 |  |  |
| 115 | [DYX_JqaCe5g](https://www.instagram.com/reel/DYX_JqaCe5g/) | 2026-05-15 |  | 270 | 4 |  |  |
| 116 | [DP2_6r7DQ60](https://www.instagram.com/reel/DP2_6r7DQ60/) | 2025-10-15 |  | 257 | 16 |  |  |
| 117 | [DWcw6f8CYuZ](https://www.instagram.com/reel/DWcw6f8CYuZ/) | 2026-03-28 |  | 265 | 8 |  |  |
| 118 | [DeGQ3NAC2f9](https://www.instagram.com/reel/DeGQ3NAC2f9/) | 2026-10-04 |  | 242 | 31 |  |  |
| 119 | [DZOSOYHi_OK](https://www.instagram.com/reel/DZOSOYHi_OK/) | 2026-06-05 |  | 260 | 11 |  |  |
| 120 | [DH12qNeCMH6](https://www.instagram.com/reel/DH12qNeCMH6/) | 2025-03-30 |  | 254 | 15 |  |  |
| 121 | [DLa8t4WhttK](https://www.instagram.com/reel/DLa8t4WhttK/) | 2025-06-27 |  | 235 | 30 |  |  |
| 122 | [DGjrh2AyVIZ](https://www.instagram.com/reel/DGjrh2AyVIZ/) | 2025-02-26 |  | 247 | 16 |  |  |
| 123 | [DdsKvWACs8M](https://www.instagram.com/reel/DdsKvWACs8M/) | 2026-09-24 |  | 229 | 34 |  |  |
| 124 | [DNYh_HxTHS6](https://www.instagram.com/reel/DNYh_HxTHS6/) | 2025-08-15 |  | 250 | 12 |  |  |
| 125 | [DdDR_1CCq7y](https://www.instagram.com/reel/DdDR_1CCq7y/) | 2026-09-08 |  | 242 | 20 |  |  |
| 126 | [DHZbr6PyczS](https://www.instagram.com/reel/DHZbr6PyczS/) | 2025-03-19 |  | 230 | 27 |  |  |
| 127 | [DeOP_uTgd7Y](https://www.instagram.com/reel/DeOP_uTgd7Y/) | 2026-10-07 |  | 219 | 38 |  |  |
| 128 | [DHkTZw4x5Si](https://www.instagram.com/reel/DHkTZw4x5Si/) | 2025-03-23 |  | 205 | 51 |  |  |
| 129 | [DJSgnlISud6](https://www.instagram.com/reel/DJSgnlISud6/) | 2025-05-05 |  | 243 | 13 |  |  |
| 130 | [DIR174qiNlO](https://www.instagram.com/reel/DIR174qiNlO/) | 2025-04-10 |  | 246 | 7 |  |  |
| 131 | [Dcsh3LhD4SE](https://www.instagram.com/reel/Dcsh3LhD4SE/) | 2026-08-31 |  | 163 | 89 |  |  |
| 132 | [DGXbI6DR3tS](https://www.instagram.com/reel/DGXbI6DR3tS/) | 2025-02-21 |  | 220 | 27 |  |  |
| 133 | [DbhvwZNCvZB](https://www.instagram.com/reel/DbhvwZNCvZB/) | 2026-08-01 |  | 242 | 4 |  |  |
| 134 | [DI2l0A_JyKw](https://www.instagram.com/reel/DI2l0A_JyKw/) | 2025-04-24 |  | 226 | 19 |  |  |
| 135 | [DdDBg2-ik1W](https://www.instagram.com/reel/DdDBg2-ik1W/) | 2026-09-08 |  | 232 | 13 |  |  |
| 136 | [DMNnRhqPVMP](https://www.instagram.com/reel/DMNnRhqPVMP/) | 2025-07-17 |  | 234 | 9 |  |  |
| 137 | [DLqly6vi8BN](https://www.instagram.com/reel/DLqly6vi8BN/) | 2025-07-03 |  | 207 | 35 |  |  |
| 138 | [Daei0qakSON](https://www.instagram.com/reel/Daei0qakSON/) | 2026-07-06 |  | 235 | 4 |  |  |
| 139 | [DaisEi-ihZb](https://www.instagram.com/reel/DaisEi-ihZb/) | 2026-07-08 |  | 231 | 8 |  |  |
| 140 | [DbU48n0kaog](https://www.instagram.com/reel/DbU48n0kaog/) | 2026-07-27 |  | 229 | 9 |  |  |
| 141 | [DRVVqymgpxz](https://www.instagram.com/reel/DRVVqymgpxz/) | 2025-11-21 |  | 224 | 13 |  |  |
| 142 | [DTSuZ8lE_QU](https://www.instagram.com/reel/DTSuZ8lE_QU/) | 2026-01-09 |  | 180 | 57 |  |  |
| 143 | [DZQOkbdJoqQ](https://www.instagram.com/reel/DZQOkbdJoqQ/) | 2026-06-06 |  | 231 | 6 |  |  |
| 144 | [DSI5QVwEnIm](https://www.instagram.com/reel/DSI5QVwEnIm/) | 2025-12-11 |  | 227 | 8 |  |  |
| 145 | [DZN5UppCQrV](https://www.instagram.com/reel/DZN5UppCQrV/) | 2026-06-05 |  | 223 | 8 |  |  |
| 146 | [DGpbGPnOg6Y](https://www.instagram.com/reel/DGpbGPnOg6Y/) | 2025-02-28 |  | 202 | 28 |  |  |
| 147 | [DTos46KkUA0](https://www.instagram.com/reel/DTos46KkUA0/) | 2026-01-17 |  | 219 | 11 |  |  |
| 148 | [Dd-OjvTFkz-](https://www.instagram.com/reel/Dd-OjvTFkz-/) | 2026-10-01 |  | 175 | 55 |  |  |
| 149 | [DcX5I-HCmWC](https://www.instagram.com/reel/DcX5I-HCmWC/) | 2026-08-22 |  | 201 | 28 |  |  |
| 150 | [DHP3cyZOVDT](https://www.instagram.com/reel/DHP3cyZOVDT/) | 2025-03-15 |  | 208 | 20 |  |  |
| 151 | [DI6-scEzyBo](https://www.instagram.com/reel/DI6-scEzyBo/) | 2025-04-26 |  | 215 | 11 |  |  |
| 152 | [DYofpCUC7Nr](https://www.instagram.com/reel/DYofpCUC7Nr/) | 2026-05-22 |  | 221 | 4 |  |  |
| 153 | [Ddsi02qlnhj](https://www.instagram.com/reel/Ddsi02qlnhj/) | 2026-09-24 |  | 205 | 20 |  |  |
| 154 | [DYA5WMyiNGN](https://www.instagram.com/reel/DYA5WMyiNGN/) | 2026-05-06 |  | 218 | 4 |  |  |
| 155 | [DL9KQyAOlXf](https://www.instagram.com/reel/DL9KQyAOlXf/) | 2025-07-10 |  | 212 | 9 |  |  |
| 156 | [DHL9jfkiqXs](https://www.instagram.com/reel/DHL9jfkiqXs/) | 2025-03-14 |  | 212 | 8 |  |  |
| 157 | [DbZ0dM4k9Z4](https://www.instagram.com/reel/DbZ0dM4k9Z4/) | 2026-07-29 |  | 213 | 7 |  |  |
| 158 | [DbB-gO9CNa-](https://www.instagram.com/reel/DbB-gO9CNa-/) | 2026-07-20 |  | 212 | 7 |  |  |
| 159 | [DQDYFFHif7v](https://www.instagram.com/reel/DQDYFFHif7v/) | 2025-10-20 |  | 201 | 17 |  |  |
| 160 | [DWSBupZgiqM](https://www.instagram.com/reel/DWSBupZgiqM/) | 2026-03-24 |  | 214 | 4 |  |  |
| 161 | [DIiSAI4iTtK](https://www.instagram.com/reel/DIiSAI4iTtK/) | 2025-04-16 |  | 169 | 47 |  |  |
| 162 | [DSI2BZ3E-gK](https://www.instagram.com/reel/DSI2BZ3E-gK/) | 2025-12-11 |  | 204 | 11 |  |  |
| 163 | [DfIYshekeF3](https://www.instagram.com/reel/DfIYshekeF3/) | 2026-10-30 | 61s | 209 | 3 | Stopstartreaction, tier list, challenge storytelling, look, I'm just gonna stop right ther | mp4, tx, bd |
| 164 | [DHyqeJgSLuZ](https://www.instagram.com/reel/DHyqeJgSLuZ/) | 2025-03-29 |  | 199 | 10 |  |  |
| 165 | [DKa2xFCPjHu](https://www.instagram.com/reel/DKa2xFCPjHu/) | 2025-06-02 |  | 188 | 21 |  |  |
| 166 | [DdJxProgCTf](https://www.instagram.com/reel/DdJxProgCTf/) | 2026-09-11 |  | 183 | 25 |  |  |
| 167 | [DfQ4E1Hjn0n](https://www.instagram.com/reel/DfQ4E1Hjn0n/) | 2026-11-02 | 76s | 205 | 2 | Here's the five types of content you're going to want to post if you want to grow a hundre | mp4, tx, bd |
| 168 | [DVF46RwgpKl](https://www.instagram.com/reel/DVF46RwgpKl/) | 2026-02-22 |  | 204 | 1 |  |  |
| 169 | [Dffuws3EiGZ](https://www.instagram.com/reel/Dffuws3EiGZ/) | 2026-11-08 |  | 198 | 6 |  |  |
| 170 | [DHphe7nxi-E](https://www.instagram.com/reel/DHphe7nxi-E/) | 2025-03-25 |  | 188 | 14 |  |  |
| 171 | [DX7wiMRCwiq](https://www.instagram.com/reel/DX7wiMRCwiq/) | 2026-05-04 |  | 196 | 6 |  |  |
| 172 | [DIN5e2UOdXb](https://www.instagram.com/reel/DIN5e2UOdXb/) | 2025-04-09 |  | 193 | 8 |  |  |
| 173 | [DX8hw3li6df](https://www.instagram.com/reel/DX8hw3li6df/) | 2026-05-04 |  | 194 | 3 |  |  |
| 174 | [DTIIAwTkyDX](https://www.instagram.com/reel/DTIIAwTkyDX/) | 2026-01-05 |  | 186 | 8 |  |  |
| 175 | [DdG4KhcATy-](https://www.instagram.com/reel/DdG4KhcATy-/) | 2026-09-10 |  | 185 | 9 |  |  |
| 176 | [DRXfqHcAkve](https://www.instagram.com/reel/DRXfqHcAkve/) | 2025-11-22 |  | 180 | 13 |  |  |
| 177 | [DeSTWxcDTA7](https://www.instagram.com/reel/DeSTWxcDTA7/) | 2026-10-09 | 43s | 189 | 3 | I think one of the hardest things about posting is letting the strategy work. | mp4, tx, bd |
| 178 | [DdMjoZWgatt](https://www.instagram.com/reel/DdMjoZWgatt/) | 2026-09-12 |  | 184 | 5 |  |  |
| 179 | [DYBGHm9ilSV](https://www.instagram.com/reel/DYBGHm9ilSV/) | 2026-05-06 |  | 185 | 2 |  |  |
| 180 | [DGM_0gFRNzp](https://www.instagram.com/reel/DGM_0gFRNzp/) | 2025-02-17 |  | 157 | 29 |  |  |
| 181 | [DHKnNP6xk5T](https://www.instagram.com/reel/DHKnNP6xk5T/) | 2025-03-13 |  | 179 | 6 |  |  |
| 182 | [Dbb3MhhCq57](https://www.instagram.com/reel/Dbb3MhhCq57/) | 2026-07-30 |  | 181 | 4 |  |  |
| 183 | [DGUkTvJRR-I](https://www.instagram.com/reel/DGUkTvJRR-I/) | 2025-02-20 |  | 160 | 24 |  |  |
| 184 | [DdPIb1wDuA8](https://www.instagram.com/reel/DdPIb1wDuA8/) | 2026-09-13 |  | 172 | 12 |  |  |
| 185 | [DGFQ3msOjU7](https://www.instagram.com/reel/DGFQ3msOjU7/) | 2025-02-14 |  | 177 | 4 |  |  |
| 186 | [DJwk8ajsRks](https://www.instagram.com/reel/DJwk8ajsRks/) | 2025-05-17 |  | 167 | 14 |  |  |
| 187 | [DU90ZcWgpmr](https://www.instagram.com/reel/DU90ZcWgpmr/) | 2026-02-19 |  | 180 | 1 |  |  |
| 188 | [DdFezvCEfRt](https://www.instagram.com/reel/DdFezvCEfRt/) | 2026-09-09 |  | 176 | 5 |  |  |
| 189 | [Dd5A7FZD3Yt](https://www.instagram.com/reel/Dd5A7FZD3Yt/) | 2026-09-29 |  | 168 | 13 |  |  |
| 190 | [DdCnk7lkZ4E](https://www.instagram.com/reel/DdCnk7lkZ4E/) | 2026-09-08 |  | 172 | 6 |  |  |
| 191 | [DdFz_sSClpz](https://www.instagram.com/reel/DdFz_sSClpz/) | 2026-09-09 |  | 112 | 65 |  |  |
| 192 | [Deuue12jmIc](https://www.instagram.com/reel/Deuue12jmIc/) | 2026-10-20 |  | 158 | 15 |  |  |
| 193 | [DSpc1_LgvSE](https://www.instagram.com/reel/DSpc1_LgvSE/) | 2025-12-24 |  | 158 | 14 |  |  |
| 194 | [DJSgjHoyUKY](https://www.instagram.com/reel/DJSgjHoyUKY/) | 2025-05-05 |  | 171 | 0 |  |  |
| 195 | [DGAPeUxxUWJ](https://www.instagram.com/reel/DGAPeUxxUWJ/) | 2025-02-12 |  | 156 | 13 |  |  |
| 196 | [DX8Vn3PCnzm](https://www.instagram.com/reel/DX8Vn3PCnzm/) | 2026-05-04 |  | 162 | 7 |  |  |
| 197 | [DSbIFpbAZWs](https://www.instagram.com/reel/DSbIFpbAZWs/) | 2025-12-18 |  | 160 | 8 |  |  |
| 198 | [DYaAxLSCsEp](https://www.instagram.com/reel/DYaAxLSCsEp/) | 2026-05-16 |  | 139 | 27 |  |  |
| 199 | [DfkojeiFdL2](https://www.instagram.com/reel/DfkojeiFdL2/) | 2026-11-10 |  | 161 | 4 |  |  |
| 200 | [DbMvRaRkyhK](https://www.instagram.com/reel/DbMvRaRkyhK/) | 2026-07-24 |  | 158 | 6 |  |  |
| 201 | [DX2UXXuiLnG](https://www.instagram.com/reel/DX2UXXuiLnG/) | 2026-05-02 |  | 157 | 6 |  |  |
| 202 | [DaoKb9RglTt](https://www.instagram.com/reel/DaoKb9RglTt/) | 2026-07-10 |  | 158 | 4 |  |  |
| 203 | [DdIQfY3DPo_](https://www.instagram.com/reel/DdIQfY3DPo_/) | 2026-09-10 |  | 156 | 5 |  |  |
| 204 | [DeYKkAIgVfL](https://www.instagram.com/reel/DeYKkAIgVfL/) | 2026-10-11 | 93s | 150 | 11 | So why do most creators lose trust in followers when they sell something, but some creator | mp4, tx, bd |
| 205 | [DbKRmyjilpf](https://www.instagram.com/reel/DbKRmyjilpf/) | 2026-07-23 |  | 158 | 2 |  |  |
| 206 | [DdpPqhzjHfD](https://www.instagram.com/reel/DdpPqhzjHfD/) | 2026-09-23 |  | 133 | 27 |  |  |
| 207 | [DflDI7bCfWh](https://www.instagram.com/reel/DflDI7bCfWh/) | 2026-11-10 |  | 152 | 8 |  |  |
| 208 | [DZlfgY7gQkP](https://www.instagram.com/reel/DZlfgY7gQkP/) | 2026-06-14 |  | 152 | 6 |  |  |
| 209 | [DU1cdleEmFK](https://www.instagram.com/reel/DU1cdleEmFK/) | 2026-02-16 |  | 155 | 2 |  |  |
| 210 | [DZBucnniEtr](https://www.instagram.com/reel/DZBucnniEtr/) | 2026-05-31 |  | 153 | 3 |  |  |
| 211 | [DZl6RlWiEiZ](https://www.instagram.com/reel/DZl6RlWiEiZ/) | 2026-06-14 |  | 139 | 16 |  |  |
| 212 | [DeqNswuE2Fd](https://www.instagram.com/reel/DeqNswuE2Fd/) | 2026-10-18 |  | 144 | 11 |  |  |
| 213 | [DeBAfaYijwf](https://www.instagram.com/reel/DeBAfaYijwf/) | 2026-10-02 |  | 145 | 9 |  |  |
| 214 | [DUrkGN8CbEZ](https://www.instagram.com/reel/DUrkGN8CbEZ/) | 2026-02-12 |  | 148 | 1 |  |  |
| 215 | [DYN4NIkC7mZ](https://www.instagram.com/reel/DYN4NIkC7mZ/) | 2026-05-11 |  | 144 | 3 |  |  |
| 216 | [DX9sWa4iCmu](https://www.instagram.com/reel/DX9sWa4iCmu/) | 2026-05-05 |  | 145 | 1 |  |  |
| 217 | [DeTZXEDjuXA](https://www.instagram.com/reel/DeTZXEDjuXA/) | 2026-10-09 |  | 130 | 15 |  |  |
| 218 | [DYlz_yJihZW](https://www.instagram.com/reel/DYlz_yJihZW/) | 2026-05-20 |  | 137 | 6 |  |  |
| 219 | [DRoLuFRAnwh](https://www.instagram.com/reel/DRoLuFRAnwh/) | 2025-11-28 |  | 136 | 4 |  |  |
| 220 | [DfA9L-PHYWp](https://www.instagram.com/reel/DfA9L-PHYWp/) | 2026-10-27 | 77s | 130 | 6 | I'm baffled by how many creators are getting millions of views every single month, but the | mp4, tx, bd |
| 221 | [DfDuMnCjNdE](https://www.instagram.com/reel/DfDuMnCjNdE/) | 2026-10-28 | 69s | 129 | 7 | If you're wondering why your audience doesn't value your opinions or your takes, it's beca | mp4, tx, bd |
| 222 | [DFikw0vSGc1](https://www.instagram.com/reel/DFikw0vSGc1/) | 2025-02-01 |  | 112 | 23 |  |  |
| 223 | [DGSGKIiRf6U](https://www.instagram.com/reel/DGSGKIiRf6U/) | 2025-02-19 |  | 116 | 18 |  |  |
| 224 | [DYaNKCHCtkr](https://www.instagram.com/reel/DYaNKCHCtkr/) | 2026-05-16 |  | 129 | 5 |  |  |
| 225 | [Dc0FXITE0pp](https://www.instagram.com/reel/Dc0FXITE0pp/) | 2026-09-02 |  | 124 | 9 |  |  |
| 226 | [DLx4AThCaLX](https://www.instagram.com/reel/DLx4AThCaLX/) | 2025-07-06 |  | 128 | 4 |  |  |
| 227 | [DFy0AxOCEa_](https://www.instagram.com/reel/DFy0AxOCEa_/) | 2025-02-07 |  | 123 | 8 |  |  |
| 228 | [DZimIlKkSmM](https://www.instagram.com/reel/DZimIlKkSmM/) | 2026-06-13 |  | 128 | 3 |  |  |
| 229 | [DdxWJreCJxc](https://www.instagram.com/reel/DdxWJreCJxc/) | 2026-09-26 |  | 115 | 16 |  |  |
| 230 | [DYXPjcLCFzX](https://www.instagram.com/reel/DYXPjcLCFzX/) | 2026-05-15 |  | 127 | 3 |  |  |
| 231 | [DfPxqFPAY4_](https://www.instagram.com/reel/DfPxqFPAY4_/) | 2026-11-02 | 78s | 128 | 1 | Did you know you could actually make one video go viral twice in one click without reposti | mp4, tx, bd |
| 232 | [C6t5P4tv7FC](https://www.instagram.com/reel/C6t5P4tv7FC/) | 2024-05-08 |  | 86 | 42 |  |  |
| 233 | [DZ_PCdxi68R](https://www.instagram.com/reel/DZ_PCdxi68R/) | 2026-06-24 |  | 126 | 2 |  |  |
| 234 | [DRgQLh3Ak-3](https://www.instagram.com/reel/DRgQLh3Ak-3/) | 2025-11-25 |  | 124 | 3 |  |  |
| 235 | [Dd2Mw0Qk4tA](https://www.instagram.com/reel/Dd2Mw0Qk4tA/) | 2026-09-28 |  | 118 | 8 |  |  |
| 236 | [DX_Bj5biSom](https://www.instagram.com/reel/DX_Bj5biSom/) | 2026-05-05 |  | 123 | 2 |  |  |
| 237 | [DZdLIsCk8Q7](https://www.instagram.com/reel/DZdLIsCk8Q7/) | 2026-06-11 |  | 121 | 4 |  |  |
| 238 | [DdM8IIuiJGL](https://www.instagram.com/reel/DdM8IIuiJGL/) | 2026-09-12 |  | 115 | 9 |  |  |
| 239 | [DY3ckAti9Ws](https://www.instagram.com/reel/DY3ckAti9Ws/) | 2026-05-27 |  | 118 | 4 |  |  |
| 240 | [DeH6eC8jBrc](https://www.instagram.com/reel/DeH6eC8jBrc/) | 2026-10-05 |  | 111 | 10 |  |  |
| 241 | [DfX2qwQGagM](https://www.instagram.com/reel/DfX2qwQGagM/) | 2026-11-05 | 54s | 118 | 1 | So the sign of a good content strategy is it rejects 99% of all of your ideas. | mp4, tx, bd |
| 242 | [DdMNd_Yk0S8](https://www.instagram.com/reel/DdMNd_Yk0S8/) | 2026-09-12 |  | 113 | 5 |  |  |
| 243 | [DfZ_q_pFbX1](https://www.instagram.com/reel/DfZ_q_pFbX1/) | 2026-11-06 | 37s | 116 | 0 | This video shows why process crushes. | mp4, tx, bd |
| 244 | [DReMeuugsJY](https://www.instagram.com/reel/DReMeuugsJY/) | 2025-11-24 |  | 113 | 2 |  |  |
| 245 | [DZjCKx1DHqo](https://www.instagram.com/reel/DZjCKx1DHqo/) | 2026-06-13 |  | 114 | 1 |  |  |
| 246 | [DY2SQvyCcTm](https://www.instagram.com/reel/DY2SQvyCcTm/) | 2026-05-27 |  | 112 | 1 |  |  |
| 247 | [DZTxl8yilDi](https://www.instagram.com/reel/DZTxl8yilDi/) | 2026-06-07 |  | 112 | 1 |  |  |
| 248 | [Da1ZEqbJv6j](https://www.instagram.com/reel/Da1ZEqbJv6j/) | 2026-07-15 |  | 108 | 5 |  |  |
| 249 | [DRjEF7xAkLJ](https://www.instagram.com/reel/DRjEF7xAkLJ/) | 2025-11-26 |  | 110 | 2 |  |  |
| 250 | [DFtLfu5z5cY](https://www.instagram.com/reel/DFtLfu5z5cY/) | 2025-02-05 |  | 92 | 19 |  |  |
| 251 | [DfTawo5jHMH](https://www.instagram.com/reel/DfTawo5jHMH/) | 2026-11-03 | 60s | 104 | 6 | So it's come to my attention that most of you don't know what a content strategy is. | mp4, tx, bd |
| 252 | [DZcySNSiBTW](https://www.instagram.com/reel/DZcySNSiBTW/) | 2026-06-11 |  | 107 | 1 |  |  |
| 253 | [DfuiWfQE4ZJ](https://www.instagram.com/reel/DfuiWfQE4ZJ/) | 2026-11-14 |  | 100 | 6 |  |  |
| 254 | [DY43eCgCl78](https://www.instagram.com/reel/DY43eCgCl78/) | 2026-05-28 |  | 98 | 4 |  |  |
| 255 | [DfLaEFNDKkv](https://www.instagram.com/reel/DfLaEFNDKkv/) | 2026-10-31 | 94s | 101 | 1 | This sounds way too good to be true, | mp4, tx, bd |
| 256 | [DF1SKrNSfIQ](https://www.instagram.com/reel/DF1SKrNSfIQ/) | 2025-02-08 |  | 88 | 13 |  |  |
| 257 | [DHnHwDdCAYb](https://www.instagram.com/reel/DHnHwDdCAYb/) | 2025-03-24 |  | 94 | 7 |  |  |
| 258 | [C8Pw2fAPk9Z](https://www.instagram.com/reel/C8Pw2fAPk9Z/) | 2024-06-15 |  | 92 | 8 |  |  |
| 259 | [Dat-trOiVbb](https://www.instagram.com/reel/Dat-trOiVbb/) | 2026-07-12 |  | 92 | 8 |  |  |
| 260 | [DeXtfyxgXZY](https://www.instagram.com/reel/DeXtfyxgXZY/) | 2026-10-11 |  | 96 | 4 |  |  |
| 261 | [Dd5qZ11lLEP](https://www.instagram.com/reel/Dd5qZ11lLEP/) | 2026-09-29 |  | 89 | 9 |  |  |
| 262 | [DbeDB4pAfEl](https://www.instagram.com/reel/DbeDB4pAfEl/) | 2026-07-31 |  | 95 | 2 |  |  |
| 263 | [DdOyVfwD0Ea](https://www.instagram.com/reel/DdOyVfwD0Ea/) | 2026-09-13 |  | 72 | 25 |  |  |
| 264 | [DeN0KLOCJGO](https://www.instagram.com/reel/DeN0KLOCJGO/) | 2026-10-07 |  | 92 | 5 |  |  |
| 265 | [DeNUKMBkVdL](https://www.instagram.com/reel/DeNUKMBkVdL/) | 2026-10-07 |  | 94 | 2 |  |  |
| 266 | [DfmxuoenIMV](https://www.instagram.com/reel/DfmxuoenIMV/) | 2026-11-11 |  | 93 | 2 |  |  |
| 267 | [DF9d1SpCSqj](https://www.instagram.com/reel/DF9d1SpCSqj/) | 2025-02-11 |  | 84 | 10 |  |  |
| 268 | [DZRlbqzC0bJ](https://www.instagram.com/reel/DZRlbqzC0bJ/) | 2026-06-06 |  | 89 | 4 |  |  |
| 269 | [DcNUPEsi6ee](https://www.instagram.com/reel/DcNUPEsi6ee/) | 2026-08-18 |  | 83 | 9 |  |  |
| 270 | [DeYhMp0AVcH](https://www.instagram.com/reel/DeYhMp0AVcH/) | 2026-10-11 |  | 90 | 2 |  |  |
| 271 | [DeAWGzdI_iR](https://www.instagram.com/reel/DeAWGzdI_iR/) | 2026-10-02 |  | 78 | 11 |  |  |
| 272 | [DX-1ZsvCzVR](https://www.instagram.com/reel/DX-1ZsvCzVR/) | 2026-05-05 |  | 81 | 7 |  |  |
| 273 | [DZiEUMADS0w](https://www.instagram.com/reel/DZiEUMADS0w/) | 2026-06-13 |  | 84 | 4 |  |  |
| 274 | [DFtUjlTS4a4](https://www.instagram.com/reel/DFtUjlTS4a4/) | 2025-02-05 |  | 80 | 7 |  |  |
| 275 | [DZQy7kyJhCo](https://www.instagram.com/reel/DZQy7kyJhCo/) | 2026-06-06 |  | 83 | 4 |  |  |
| 276 | [DZXu4j9ATXP](https://www.instagram.com/reel/DZXu4j9ATXP/) | 2026-06-09 |  | 87 | 0 |  |  |
| 277 | [DeHc_p5indp](https://www.instagram.com/reel/DeHc_p5indp/) | 2026-10-05 |  | 87 | 0 |  |  |
| 278 | [DescvtijImq](https://www.instagram.com/reel/DescvtijImq/) | 2026-10-19 |  | 79 | 7 |  |  |
| 279 | [Dd944SEDJzP](https://www.instagram.com/reel/Dd944SEDJzP/) | 2026-10-01 |  | 72 | 12 |  |  |
| 280 | [DZP69epC8QD](https://www.instagram.com/reel/DZP69epC8QD/) | 2026-06-06 |  | 79 | 4 |  |  |
| 281 | [DHo6E6FSkvE](https://www.instagram.com/reel/DHo6E6FSkvE/) | 2025-03-25 |  | 80 | 2 |  |  |
| 282 | [DUrkHGbCdL_](https://www.instagram.com/reel/DUrkHGbCdL_/) | 2026-02-12 |  | 82 | 0 |  |  |
| 283 | [DSTdFOPgd6s](https://www.instagram.com/reel/DSTdFOPgd6s/) | 2025-12-15 |  | 80 | 0 |  |  |
| 284 | [DUrTgmLEhwt](https://www.instagram.com/reel/DUrTgmLEhwt/) | 2026-02-12 |  | 79 | 0 |  |  |
| 285 | [DZOkq7aCBUp](https://www.instagram.com/reel/DZOkq7aCBUp/) | 2026-06-05 |  | 77 | 2 |  |  |
| 286 | [DZS7aeqCgMA](https://www.instagram.com/reel/DZS7aeqCgMA/) | 2026-06-07 |  | 79 | 0 |  |  |
| 287 | [DeS-V2NCYrB](https://www.instagram.com/reel/DeS-V2NCYrB/) | 2026-10-09 |  | 76 | 3 |  |  |
| 288 | [Dd-qJuKlM1Z](https://www.instagram.com/reel/Dd-qJuKlM1Z/) | 2026-10-01 |  | 70 | 8 |  |  |
| 289 | [DZVVDTCiD-F](https://www.instagram.com/reel/DZVVDTCiD-F/) | 2026-06-08 |  | 77 | 0 |  |  |
| 290 | [DeX7T84jp9R](https://www.instagram.com/reel/DeX7T84jp9R/) | 2026-10-11 |  | 67 | 10 |  |  |
| 291 | [Dfw9uu4AJkL](https://www.instagram.com/reel/Dfw9uu4AJkL/) | 2026-11-15 |  | 75 | 2 |  |  |
| 292 | [DF4h5prCZqw](https://www.instagram.com/reel/DF4h5prCZqw/) | 2025-02-09 |  | 70 | 6 |  |  |
| 293 | [DfSf5v8j73o](https://www.instagram.com/reel/DfSf5v8j73o/) | 2026-11-03 | 57s | 74 | 2 | So no one ever told you this, | mp4, tx, bd |
| 294 | [DeI5cN7CV7R](https://www.instagram.com/reel/DeI5cN7CV7R/) | 2026-10-05 |  | 72 | 3 |  |  |
| 295 | [DcR_s1oCEAf](https://www.instagram.com/reel/DcR_s1oCEAf/) | 2026-08-20 |  | 39 | 35 |  |  |
| 296 | [DeIRJPLj-ur](https://www.instagram.com/reel/DeIRJPLj-ur/) | 2026-10-05 |  | 74 | 0 |  |  |
| 297 | [DdHLu3BCUrQ](https://www.instagram.com/reel/DdHLu3BCUrQ/) | 2026-09-10 |  | 70 | 3 |  |  |
| 298 | [Dd21Nzfj43Q](https://www.instagram.com/reel/Dd21Nzfj43Q/) | 2026-09-28 |  | 66 | 6 |  |  |
| 299 | [C76Cyptu6lQ](https://www.instagram.com/reel/C76Cyptu6lQ/) | 2024-06-07 |  | 65 | 6 |  |  |
| 300 | [DUw55-kEQyb](https://www.instagram.com/reel/DUw55-kEQyb/) | 2026-02-14 |  | 71 | 0 |  |  |
| 301 | [DdxyO83gkeS](https://www.instagram.com/reel/DdxyO83gkeS/) | 2026-09-26 |  | 68 | 3 |  |  |
| 302 | [DZlPHJSDQMt](https://www.instagram.com/reel/DZlPHJSDQMt/) | 2026-06-14 |  | 69 | 1 |  |  |
| 303 | [DfU49SJAFYH](https://www.instagram.com/reel/DfU49SJAFYH/) | 2026-11-04 | 104s | 70 | 0 | Let's analyze how our video got 1.1 million views by using the retention graph. | mp4, tx, bd |
| 304 | [DUuoon1gvWz](https://www.instagram.com/reel/DUuoon1gvWz/) | 2026-02-13 |  | 66 | 2 |  |  |
| 305 | [DZgc0PJmDww](https://www.instagram.com/reel/DZgc0PJmDww/) | 2026-06-12 |  | 66 | 1 |  |  |
| 306 | [DfnQiBcEl04](https://www.instagram.com/reel/DfnQiBcEl04/) | 2026-11-11 |  | 64 | 3 |  |  |
| 307 | [DFW2mnrCo7A](https://www.instagram.com/reel/DFW2mnrCo7A/) | 2025-01-27 |  | 60 | 5 |  |  |
| 308 | [DY2qMOdCV9T](https://www.instagram.com/reel/DY2qMOdCV9T/) | 2026-05-27 |  | 63 | 2 |  |  |
| 309 | [DZgwtzClUVN](https://www.instagram.com/reel/DZgwtzClUVN/) | 2026-06-12 |  | 62 | 2 |  |  |
| 310 | [Dd5U7l2jMPa](https://www.instagram.com/reel/Dd5U7l2jMPa/) | 2026-09-29 |  | 62 | 1 |  |  |
| 311 | [DfpNm59kap9](https://www.instagram.com/reel/DfpNm59kap9/) | 2026-11-12 |  | 62 | 1 |  |  |
| 312 | [DZiYVuuALTn](https://www.instagram.com/reel/DZiYVuuALTn/) | 2026-06-13 |  | 61 | 0 |  |  |
| 313 | [DckjRM1iusV](https://www.instagram.com/reel/DckjRM1iusV/) | 2026-08-27 |  | 60 | 0 |  |  |
| 314 | [DevpJZLk6Km](https://www.instagram.com/reel/DevpJZLk6Km/) | 2026-10-20 |  | 58 | 2 |  |  |
| 315 | [DFl1ZeDSB1T](https://www.instagram.com/reel/DFl1ZeDSB1T/) | 2025-02-02 |  | 54 | 5 |  |  |
| 316 | [DJSgbnmyBRd](https://www.instagram.com/reel/DJSgbnmyBRd/) | 2025-05-05 |  | 59 | 0 |  |  |
| 317 | [DV4TjIwklJo](https://www.instagram.com/reel/DV4TjIwklJo/) | 2026-03-14 |  | 57 | 2 |  |  |
| 318 | [DOPEac-ExcS](https://www.instagram.com/reel/DOPEac-ExcS/) | 2025-09-05 |  | 57 | 1 |  |  |
| 319 | [DeLbfI-jNZ7](https://www.instagram.com/reel/DeLbfI-jNZ7/) | 2026-10-06 |  | 57 | 1 |  |  |
| 320 | [DJSggT7yhz7](https://www.instagram.com/reel/DJSggT7yhz7/) | 2025-05-05 |  | 54 | 3 |  |  |
| 321 | [DU1WS9gE5zh](https://www.instagram.com/reel/DU1WS9gE5zh/) | 2026-02-16 |  | 57 | 0 |  |  |
| 322 | [DWo2hFFCb1y](https://www.instagram.com/reel/DWo2hFFCb1y/) | 2026-04-02 |  | 56 | 1 |  |  |
| 323 | [DFwJPYpy7DM](https://www.instagram.com/reel/DFwJPYpy7DM/) | 2025-02-06 |  | 56 | 0 |  |  |
| 324 | [DZUF3DCCUI4](https://www.instagram.com/reel/DZUF3DCCUI4/) | 2026-06-07 |  | 56 | 0 |  |  |
| 325 | [DcmWT2gyK4d](https://www.instagram.com/reel/DcmWT2gyK4d/) | 2026-08-28 |  | 55 | 1 |  |  |
| 326 | [DFq1g3rSckr](https://www.instagram.com/reel/DFq1g3rSckr/) | 2025-02-04 |  | 53 | 1 |  |  |
| 327 | [DZC6kiXi6AF](https://www.instagram.com/reel/DZC6kiXi6AF/) | 2026-06-01 |  | 53 | 1 |  |  |
| 328 | [DFqZp6fyWIT](https://www.instagram.com/reel/DFqZp6fyWIT/) | 2025-02-04 |  | 47 | 6 |  |  |
| 329 | [DFwIGYViUub](https://www.instagram.com/reel/DFwIGYViUub/) | 2025-02-06 |  | 52 | 1 |  |  |
| 330 | [DU61oShARTl](https://www.instagram.com/reel/DU61oShARTl/) | 2026-02-18 |  | 53 | 0 |  |  |
| 331 | [DU612AfAYsR](https://www.instagram.com/reel/DU612AfAYsR/) | 2026-02-18 |  | 50 | 1 |  |  |
| 332 | [C9BLTn_yWU-](https://www.instagram.com/reel/C9BLTn_yWU-/) | 2024-07-04 |  | 48 | 2 |  |  |
| 333 | [DWpJYSfknZa](https://www.instagram.com/reel/DWpJYSfknZa/) | 2026-04-02 |  | 49 | 1 |  |  |
| 334 | [DFTfRTFSwax](https://www.instagram.com/reel/DFTfRTFSwax/) | 2025-01-26 |  | 41 | 8 |  |  |
| 335 | [DFYMMxNCc-U](https://www.instagram.com/reel/DFYMMxNCc-U/) | 2025-01-28 |  | 45 | 3 |  |  |
| 336 | [DFoYh-VSr8x](https://www.instagram.com/reel/DFoYh-VSr8x/) | 2025-02-03 |  | 41 | 6 |  |  |
| 337 | [DJSglY3yOQD](https://www.instagram.com/reel/DJSglY3yOQD/) | 2025-05-05 |  | 45 | 2 |  |  |
| 338 | [DAJGzwkNndb](https://www.instagram.com/reel/DAJGzwkNndb/) | 2024-09-20 |  | 33 | 13 |  |  |
| 339 | [DNZ5yzGtprV](https://www.instagram.com/reel/DNZ5yzGtprV/) | 2025-08-15 |  | 44 | 2 |  |  |
| 340 | [DZkpAN5jB2_](https://www.instagram.com/reel/DZkpAN5jB2_/) | 2026-06-14 |  | 44 | 2 |  |  |
| 341 | [C9iZWZiSv9m](https://www.instagram.com/reel/C9iZWZiSv9m/) | 2024-07-17 |  | 32 | 13 |  |  |
| 342 | [DNi_r_VzND7](https://www.instagram.com/reel/DNi_r_VzND7/) | 2025-08-19 |  | 39 | 3 |  |  |
| 343 | [DVF5EMTgl-G](https://www.instagram.com/reel/DVF5EMTgl-G/) | 2026-02-22 |  | 42 | 0 |  |  |
| 344 | [DcKplCliMhG](https://www.instagram.com/reel/DcKplCliMhG/) | 2026-08-17 |  | 42 | 0 |  |  |
| 345 | [DciNHGUiVZ4](https://www.instagram.com/reel/DciNHGUiVZ4/) | 2026-08-27 |  | 40 | 2 |  |  |
| 346 | [DcuggGSCCAS](https://www.instagram.com/reel/DcuggGSCCAS/) | 2026-08-31 |  | 35 | 7 |  |  |
| 347 | [DOTj_uoDeC3](https://www.instagram.com/reel/DOTj_uoDeC3/) | 2025-09-07 |  | 37 | 4 |  |  |
| 348 | [DNhDxAFJjB-](https://www.instagram.com/reel/DNhDxAFJjB-/) | 2025-08-18 |  | 40 | 0 |  |  |
| 349 | [DY272obprwo](https://www.instagram.com/reel/DY272obprwo/) | 2026-05-27 |  | 40 | 0 |  |  |
| 350 | [DZf06YgAraH](https://www.instagram.com/reel/DZf06YgAraH/) | 2026-06-12 |  | 36 | 1 |  |  |
| 351 | [DU3_s_qkkE4](https://www.instagram.com/reel/DU3_s_qkkE4/) | 2026-02-17 |  | 36 | 0 |  |  |
| 352 | [DU4AU_rkios](https://www.instagram.com/reel/DU4AU_rkios/) | 2026-02-17 |  | 35 | 1 |  |  |
| 353 | [DcPGOzkS5S6](https://www.instagram.com/reel/DcPGOzkS5S6/) | 2026-08-19 |  | 36 | 0 |  |  |
| 354 | [DVF6RQUAk97](https://www.instagram.com/reel/DVF6RQUAk97/) | 2026-02-22 |  | 35 | 0 |  |  |
| 355 | [DeSqEtsjgiW](https://www.instagram.com/reel/DeSqEtsjgiW/) | 2026-10-09 |  | 34 | 1 |  |  |
| 356 | [C9-aba3Py2V](https://www.instagram.com/reel/C9-aba3Py2V/) | 2024-07-28 |  | 32 | 1 |  |  |
| 357 | [C_4H4Wzi3hY](https://www.instagram.com/reel/C_4H4Wzi3hY/) | 2024-09-13 |  | 29 | 4 |  |  |
| 358 | [DOPEc0-k3Bh](https://www.instagram.com/reel/DOPEc0-k3Bh/) | 2025-09-05 |  | 33 | 0 |  |  |
| 359 | [DUq4q7Qkl6C](https://www.instagram.com/reel/DUq4q7Qkl6C/) | 2026-02-12 |  | 33 | 0 |  |  |
| 360 | [DU6168CgbEG](https://www.instagram.com/reel/DU6168CgbEG/) | 2026-02-18 |  | 32 | 1 |  |  |
| 361 | [DC2shB7CPHT](https://www.instagram.com/reel/DC2shB7CPHT/) | 2024-11-26 |  | 31 | 1 |  |  |
| 362 | [DBb_xt0SRUP](https://www.instagram.com/reel/DBb_xt0SRUP/) | 2024-10-22 |  | 30 | 1 |  |  |
| 363 | [Dfls0d4CoYU](https://www.instagram.com/reel/Dfls0d4CoYU/) | 2026-11-10 |  | 30 | 1 |  |  |
| 364 | [DOPFIoDCXCl](https://www.instagram.com/reel/DOPFIoDCXCl/) | 2025-09-05 |  | 27 | 3 |  |  |
| 365 | [DOWgLkik92V](https://www.instagram.com/reel/DOWgLkik92V/) | 2025-09-08 |  | 28 | 2 |  |  |
| 366 | [DOPEUqakzRu](https://www.instagram.com/reel/DOPEUqakzRu/) | 2025-09-05 |  | 26 | 3 |  |  |
| 367 | [DOTkPqhDQ9_](https://www.instagram.com/reel/DOTkPqhDQ9_/) | 2025-09-07 |  | 29 | 0 |  |  |
| 368 | [DOWgtdrk-Ya](https://www.instagram.com/reel/DOWgtdrk-Ya/) | 2025-09-08 |  | 27 | 2 |  |  |
| 369 | [DU90msQAmz1](https://www.instagram.com/reel/DU90msQAmz1/) | 2026-02-19 |  | 29 | 0 |  |  |
| 370 | [DU61t8ugQvI](https://www.instagram.com/reel/DU61t8ugQvI/) | 2026-02-18 |  | 27 | 1 |  |  |
| 371 | [DVF43cRAur7](https://www.instagram.com/reel/DVF43cRAur7/) | 2026-02-22 |  | 28 | 0 |  |  |
| 372 | [DABVdE5JPJS](https://www.instagram.com/reel/DABVdE5JPJS/) | 2024-09-17 |  | 26 | 1 |  |  |
| 373 | [DSQeVmBk12d](https://www.instagram.com/reel/DSQeVmBk12d/) | 2025-12-14 |  | 27 | 0 |  |  |
| 374 | [DFf_2EhCV3R](https://www.instagram.com/reel/DFf_2EhCV3R/) | 2025-01-31 |  | 24 | 2 |  |  |
| 375 | [DcUMoAyy_aF](https://www.instagram.com/reel/DcUMoAyy_aF/) | 2026-08-21 |  | 26 | 0 |  |  |
| 376 | [DOPFL8HicLX](https://www.instagram.com/reel/DOPFL8HicLX/) | 2025-09-05 |  | 22 | 3 |  |  |
| 377 | [Da605Pbi2cV](https://www.instagram.com/reel/Da605Pbi2cV/) | 2026-07-17 |  | 23 | 2 |  |  |
| 378 | [DciLLNci-XJ](https://www.instagram.com/reel/DciLLNci-XJ/) | 2026-08-26 |  | 23 | 2 |  |  |
| 379 | [C_BxfXeSKj6](https://www.instagram.com/reel/C_BxfXeSKj6/) | 2024-08-23 |  | 24 | 0 |  |  |
| 380 | [C_jgx0tyxSQ](https://www.instagram.com/reel/C_jgx0tyxSQ/) | 2024-09-05 |  | 24 | 0 |  |  |
| 381 | [DOPFPG_iabT](https://www.instagram.com/reel/DOPFPG_iabT/) | 2025-09-05 |  | 24 | 0 |  |  |
| 382 | [DOWf9MMiWRF](https://www.instagram.com/reel/DOWf9MMiWRF/) | 2025-09-08 |  | 24 | 0 |  |  |
| 383 | [DU1cYrmkmIv](https://www.instagram.com/reel/DU1cYrmkmIv/) | 2026-02-16 |  | 22 | 2 |  |  |
| 384 | [DU90gorAl1Q](https://www.instagram.com/reel/DU90gorAl1Q/) | 2026-02-19 |  | 24 | 0 |  |  |
| 385 | [DNZ2RNUt4Iu](https://www.instagram.com/reel/DNZ2RNUt4Iu/) | 2025-08-15 |  | 21 | 2 |  |  |
| 386 | [DOPEYVVk8-U](https://www.instagram.com/reel/DOPEYVVk8-U/) | 2025-09-05 |  | 23 | 0 |  |  |
| 387 | [DU3_n3xEuI9](https://www.instagram.com/reel/DU3_n3xEuI9/) | 2026-02-17 |  | 20 | 3 |  |  |
| 388 | [DWo2_BriUPq](https://www.instagram.com/reel/DWo2_BriUPq/) | 2026-04-02 |  | 23 | 0 |  |  |
| 389 | [DOTc0wtibBQ](https://www.instagram.com/reel/DOTc0wtibBQ/) | 2025-09-07 |  | 22 | 0 |  |  |
| 390 | [DU1cR-9EhKC](https://www.instagram.com/reel/DU1cR-9EhKC/) | 2026-02-16 |  | 20 | 2 |  |  |
| 391 | [DcZTi4hhb0O](https://www.instagram.com/reel/DcZTi4hhb0O/) | 2026-08-23 |  | 22 | 0 |  |  |
| 392 | [DNZ6-f8tONA](https://www.instagram.com/reel/DNZ6-f8tONA/) | 2025-08-15 |  | 21 | 0 |  |  |
| 393 | [DVPyj4EkYBw](https://www.instagram.com/reel/DVPyj4EkYBw/) | 2026-02-26 |  | 20 | 1 |  |  |
| 394 | [DbhyyLRi9Cq](https://www.instagram.com/reel/DbhyyLRi9Cq/) | 2026-08-01 |  | 21 | 0 |  |  |
| 395 | [C_y54cIvxWM](https://www.instagram.com/reel/C_y54cIvxWM/) | 2024-09-11 |  | 17 | 3 |  |  |
| 396 | [DOPE79jiXPn](https://www.instagram.com/reel/DOPE79jiXPn/) | 2025-09-05 |  | 18 | 2 |  |  |
| 397 | [DOTdFf0CeHo](https://www.instagram.com/reel/DOTdFf0CeHo/) | 2025-09-07 |  | 15 | 5 |  |  |
| 398 | [DcMuLCihbm4](https://www.instagram.com/reel/DcMuLCihbm4/) | 2026-08-18 |  | 20 | 0 |  |  |
| 399 | [DcPgTAgC6g1](https://www.instagram.com/reel/DcPgTAgC6g1/) | 2026-08-19 |  | 19 | 1 |  |  |
| 400 | [Dfk9cNwhOTB](https://www.instagram.com/reel/Dfk9cNwhOTB/) | 2026-11-10 |  | 20 | 0 |  |  |
| 401 | [C_8Rv3RpOrN](https://www.instagram.com/reel/C_8Rv3RpOrN/) | 2024-09-15 |  | 17 | 2 |  |  |
| 402 | [DOPE4DviaAk](https://www.instagram.com/reel/DOPE4DviaAk/) | 2025-09-05 |  | 19 | 0 |  |  |
| 403 | [DOTj3pLDYM7](https://www.instagram.com/reel/DOTj3pLDYM7/) | 2025-09-07 |  | 18 | 1 |  |  |
| 404 | [C_gb5PpSVLf](https://www.instagram.com/reel/C_gb5PpSVLf/) | 2024-09-04 |  | 18 | 0 |  |  |
| 405 | [C_3IY9WCAHx](https://www.instagram.com/reel/C_3IY9WCAHx/) | 2024-09-13 |  | 18 | 0 |  |  |
| 406 | [DALzWjeoEc8](https://www.instagram.com/reel/DALzWjeoEc8/) | 2024-09-21 |  | 16 | 1 |  |  |
| 407 | [DNZ7OsotArJ](https://www.instagram.com/reel/DNZ7OsotArJ/) | 2025-08-15 |  | 13 | 4 |  |  |
| 408 | [DOPEZ1Zk7J_](https://www.instagram.com/reel/DOPEZ1Zk7J_/) | 2025-09-05 |  | 17 | 0 |  |  |
| 409 | [DYTx9wLCnKQ](https://www.instagram.com/reel/DYTx9wLCnKQ/) | 2026-05-13 |  | 16 | 1 |  |  |
| 410 | [DcUGn7Th1xQ](https://www.instagram.com/reel/DcUGn7Th1xQ/) | 2026-08-21 |  | 16 | 1 |  |  |
| 411 | [DckMJMmCpzT](https://www.instagram.com/reel/DckMJMmCpzT/) | 2026-08-27 |  | 13 | 4 |  |  |
| 412 | [C_0kmLtImrb](https://www.instagram.com/reel/C_0kmLtImrb/) | 2024-09-12 |  | 16 | 0 |  |  |
| 413 | [DAEDultqpnF](https://www.instagram.com/reel/DAEDultqpnF/) | 2024-09-18 |  | 16 | 0 |  |  |
| 414 | [DNgHVIEz2sL](https://www.instagram.com/reel/DNgHVIEz2sL/) | 2025-08-18 |  | 16 | 0 |  |  |
| 415 | [DNgkU9ezzAU](https://www.instagram.com/reel/DNgkU9ezzAU/) | 2025-08-18 |  | 14 | 2 |  |  |
| 416 | [DU90ky-gqwD](https://www.instagram.com/reel/DU90ky-gqwD/) | 2026-02-19 |  | 16 | 0 |  |  |
| 417 | [Da6OrYtS8JF](https://www.instagram.com/reel/Da6OrYtS8JF/) | 2026-07-17 |  | 15 | 1 |  |  |
| 418 | [DcKeHUZCuLM](https://www.instagram.com/reel/DcKeHUZCuLM/) | 2026-08-17 |  | 14 | 2 |  |  |
| 419 | [DcUKt4qB5s1](https://www.instagram.com/reel/DcUKt4qB5s1/) | 2026-08-21 |  | 16 | 0 |  |  |
| 420 | [DcURgxtyPUY](https://www.instagram.com/reel/DcURgxtyPUY/) | 2026-08-21 |  | 14 | 2 |  |  |
| 421 | [Dc1mQZFhCSm](https://www.instagram.com/reel/Dc1mQZFhCSm/) | 2026-09-03 |  | 15 | 1 |  |  |
| 422 | [DOPFDysCTep](https://www.instagram.com/reel/DOPFDysCTep/) | 2025-09-05 |  | 15 | 0 |  |  |
| 423 | [DOPFFrhCSa6](https://www.instagram.com/reel/DOPFFrhCSa6/) | 2025-09-05 |  | 15 | 0 |  |  |
| 424 | [DcRMApKKKqV](https://www.instagram.com/reel/DcRMApKKKqV/) | 2026-08-20 |  | 15 | 0 |  |  |
| 425 | [DOPEee4k1T0](https://www.instagram.com/reel/DOPEee4k1T0/) | 2025-09-05 |  | 13 | 1 |  |  |
| 426 | [DOPE4uuiTaW](https://www.instagram.com/reel/DOPE4uuiTaW/) | 2025-09-05 |  | 14 | 0 |  |  |
| 427 | [C_5uNz_OBQH](https://www.instagram.com/reel/C_5uNz_OBQH/) | 2024-09-14 |  | 13 | 0 |  |  |
| 428 | [DNgkGJgprDt](https://www.instagram.com/reel/DNgkGJgprDt/) | 2025-08-18 |  | 13 | 0 |  |  |
| 429 | [DTqnjuSkzpf](https://www.instagram.com/reel/DTqnjuSkzpf/) | 2026-01-18 |  | 13 | 0 |  |  |
| 430 | [DUzMvRFiYY7](https://www.instagram.com/reel/DUzMvRFiYY7/) | 2026-02-15 |  | 13 | 0 |  |  |
| 431 | [DfLP8yBBQjO](https://www.instagram.com/reel/DfLP8yBBQjO/) | 2026-10-31 |  | 13 | 0 |  |  |
| 432 | [C_--Vv8oWWr](https://www.instagram.com/reel/C_--Vv8oWWr/) | 2024-09-16 |  | 12 | 0 |  |  |
| 433 | [DAH9Yu-RvZO](https://www.instagram.com/reel/DAH9Yu-RvZO/) | 2024-09-19 |  | 12 | 0 |  |  |
| 434 | [DOPE2joCZ4h](https://www.instagram.com/reel/DOPE2joCZ4h/) | 2025-09-05 |  | 12 | 0 |  |  |
| 435 | [DOPFHXWiVFh](https://www.instagram.com/reel/DOPFHXWiVFh/) | 2025-09-05 |  | 12 | 0 |  |  |
| 436 | [DOWgqhtE_5f](https://www.instagram.com/reel/DOWgqhtE_5f/) | 2025-09-08 |  | 12 | 0 |  |  |
| 437 | [DcZiIaNhCvN](https://www.instagram.com/reel/DcZiIaNhCvN/) | 2026-08-23 |  | 12 | 0 |  |  |
| 438 | [DNZ2ge9NeZe](https://www.instagram.com/reel/DNZ2ge9NeZe/) | 2025-08-15 |  | 11 | 0 |  |  |
| 439 | [DNZ3grztmdk](https://www.instagram.com/reel/DNZ3grztmdk/) | 2025-08-15 |  | 11 | 0 |  |  |
| 440 | [DNZ52p0t07C](https://www.instagram.com/reel/DNZ52p0t07C/) | 2025-08-15 |  | 11 | 0 |  |  |
| 441 | [DNgHYsOxTGW](https://www.instagram.com/reel/DNgHYsOxTGW/) | 2025-08-18 |  | 11 | 0 |  |  |
| 442 | [DNgHUfGxyZh](https://www.instagram.com/reel/DNgHUfGxyZh/) | 2025-08-18 |  | 11 | 0 |  |  |
| 443 | [DUr8RNZEczE](https://www.instagram.com/reel/DUr8RNZEczE/) | 2026-02-12 |  | 11 | 0 |  |  |
| 444 | [DcM4KzTiCbe](https://www.instagram.com/reel/DcM4KzTiCbe/) | 2026-08-18 |  | 11 | 0 |  |  |
| 445 | [DcWg39BJikN](https://www.instagram.com/reel/DcWg39BJikN/) | 2026-08-22 |  | 11 | 0 |  |  |
| 446 | [DNgHQkwJHop](https://www.instagram.com/reel/DNgHQkwJHop/) | 2025-08-18 |  | 10 | 0 |  |  |
| 447 | [DY27u2qJVNK](https://www.instagram.com/reel/DY27u2qJVNK/) | 2026-05-27 |  | 10 | 0 |  |  |
| 448 | [DcdA5Ofi2Nv](https://www.instagram.com/reel/DcdA5Ofi2Nv/) | 2026-08-24 |  | 9 | 1 |  |  |
| 449 | [DNZ4EUst885](https://www.instagram.com/reel/DNZ4EUst885/) | 2025-08-15 |  | 9 | 0 |  |  |
| 450 | [DNgHkwYxE7y](https://www.instagram.com/reel/DNgHkwYxE7y/) | 2025-08-18 |  | 8 | 1 |  |  |
| 451 | [DNhDXvNpDL1](https://www.instagram.com/reel/DNhDXvNpDL1/) | 2025-08-18 |  | 8 | 1 |  |  |
| 452 | [DNhDoB7Tsqc](https://www.instagram.com/reel/DNhDoB7Tsqc/) | 2025-08-18 |  | 8 | 1 |  |  |
| 453 | [DOWgOzbEzz_](https://www.instagram.com/reel/DOWgOzbEzz_/) | 2025-09-08 |  | 8 | 1 |  |  |
| 454 | [DcNjCw-C6Mz](https://www.instagram.com/reel/DcNjCw-C6Mz/) | 2026-08-18 |  | 8 | 1 |  |  |
| 455 | [DNgHSqyzPZa](https://www.instagram.com/reel/DNgHSqyzPZa/) | 2025-08-18 |  | 7 | 1 |  |  |
| 456 | [DNgkNa6zmse](https://www.instagram.com/reel/DNgkNa6zmse/) | 2025-08-18 |  | 8 | 0 |  |  |
| 457 | [DNi_t-Lzz2D](https://www.instagram.com/reel/DNi_t-Lzz2D/) | 2025-08-19 |  | 8 | 0 |  |  |
| 458 | [DOPFKVMiTkW](https://www.instagram.com/reel/DOPFKVMiTkW/) | 2025-09-05 |  | 8 | 0 |  |  |
| 459 | [DcM3sEqC0If](https://www.instagram.com/reel/DcM3sEqC0If/) | 2026-08-18 |  | 8 | 0 |  |  |
| 460 | [DcRRUILCLiN](https://www.instagram.com/reel/DcRRUILCLiN/) | 2026-08-20 |  | 7 | 1 |  |  |
| 461 | [DNZ3czEN7Me](https://www.instagram.com/reel/DNZ3czEN7Me/) | 2025-08-15 |  | 7 | 0 |  |  |
| 462 | [DNZ3f_9NhMl](https://www.instagram.com/reel/DNZ3f_9NhMl/) | 2025-08-15 |  | 7 | 0 |  |  |
| 463 | [DNhDXFnzSTz](https://www.instagram.com/reel/DNhDXFnzSTz/) | 2025-08-18 |  | 7 | 0 |  |  |
| 464 | [DOTcyX2jdcp](https://www.instagram.com/reel/DOTcyX2jdcp/) | 2025-09-07 |  | 7 | 0 |  |  |
| 465 | [DOWf7_Skw9n](https://www.instagram.com/reel/DOWf7_Skw9n/) | 2025-09-08 |  | 7 | 0 |  |  |
| 466 | [DOWgAGMk25T](https://www.instagram.com/reel/DOWgAGMk25T/) | 2025-09-08 |  | 6 | 1 |  |  |
| 467 | [DVF4w6igqcJ](https://www.instagram.com/reel/DVF4w6igqcJ/) | 2026-02-22 |  | 7 | 0 |  |  |
| 468 | [DcMs5gyhoHp](https://www.instagram.com/reel/DcMs5gyhoHp/) | 2026-08-18 |  | 7 | 0 |  |  |
| 469 | [DLxrTwevGkj](https://www.instagram.com/reel/DLxrTwevGkj/) | 2025-07-06 |  | 6 | 0 |  |  |
| 470 | [DNZ3egMNm6F](https://www.instagram.com/reel/DNZ3egMNm6F/) | 2025-08-15 |  | 5 | 1 |  |  |
| 471 | [DNhDR2aTAw_](https://www.instagram.com/reel/DNhDR2aTAw_/) | 2025-08-18 |  | 5 | 1 |  |  |
| 472 | [DNhDZlNzgZD](https://www.instagram.com/reel/DNhDZlNzgZD/) | 2025-08-18 |  | 6 | 0 |  |  |
| 473 | [DNhDrE7TdSp](https://www.instagram.com/reel/DNhDrE7TdSp/) | 2025-08-18 |  | 6 | 0 |  |  |
| 474 | [DOTjXabjcGT](https://www.instagram.com/reel/DOTjXabjcGT/) | 2025-09-07 |  | 6 | 0 |  |  |
| 475 | [DOTkB2YDRYf](https://www.instagram.com/reel/DOTkB2YDRYf/) | 2025-09-07 |  | 6 | 0 |  |  |
| 476 | [DOWf-SzE5Az](https://www.instagram.com/reel/DOWf-SzE5Az/) | 2025-09-08 |  | 6 | 0 |  |  |
| 477 | [DOWgNKFE549](https://www.instagram.com/reel/DOWgNKFE549/) | 2025-09-08 |  | 6 | 0 |  |  |
| 478 | [DSdFN1OAWYR](https://www.instagram.com/reel/DSdFN1OAWYR/) | 2025-12-19 |  | 6 | 0 |  |  |
| 479 | [DTPa22hDD3R](https://www.instagram.com/reel/DTPa22hDD3R/) | 2026-01-07 |  | 6 | 0 |  |  |
| 480 | [DTyGTOCAZYT](https://www.instagram.com/reel/DTyGTOCAZYT/) | 2026-01-21 |  | 6 | 0 |  |  |
| 481 | [DcWu_iqBYBS](https://www.instagram.com/reel/DcWu_iqBYBS/) | 2026-08-22 |  | 5 | 1 |  |  |
| 482 | [De0ti2CiGwn](https://www.instagram.com/reel/De0ti2CiGwn/) | 2026-10-22 |  | 6 | 0 |  |  |
| 483 | [DOTczIlCfRV](https://www.instagram.com/reel/DOTczIlCfRV/) | 2025-09-07 |  | 5 | 0 |  |  |
| 484 | [DOTje9vDX0D](https://www.instagram.com/reel/DOTje9vDX0D/) | 2025-09-07 |  | 5 | 0 |  |  |
| 485 | [DOWgsOGE5n1](https://www.instagram.com/reel/DOWgsOGE5n1/) | 2025-09-08 |  | 5 | 0 |  |  |
| 486 | [DWW4GSOCVUI](https://www.instagram.com/reel/DWW4GSOCVUI/) | 2026-03-26 |  | 5 | 0 |  |  |
| 487 | [DcMs9BtBslP](https://www.instagram.com/reel/DcMs9BtBslP/) | 2026-08-18 |  | 4 | 1 |  |  |
| 488 | [DcjHIZDCuqh](https://www.instagram.com/reel/DcjHIZDCuqh/) | 2026-08-27 |  | 5 | 0 |  |  |
| 489 | [DNXCz3jNUsD](https://www.instagram.com/reel/DNXCz3jNUsD/) | 2025-08-14 |  | 4 | 0 |  |  |
| 490 | [DNZ2LsMNYXd](https://www.instagram.com/reel/DNZ2LsMNYXd/) | 2025-08-15 |  | 4 | 0 |  |  |
| 491 | [DNgkBtPTijD](https://www.instagram.com/reel/DNgkBtPTijD/) | 2025-08-18 |  | 4 | 0 |  |  |
| 492 | [DNhDTdxJ8FX](https://www.instagram.com/reel/DNhDTdxJ8FX/) | 2025-08-18 |  | 4 | 0 |  |  |
| 493 | [DNi_ygDpOph](https://www.instagram.com/reel/DNi_ygDpOph/) | 2025-08-19 |  | 4 | 0 |  |  |
| 494 | [DNjAuVUz1OI](https://www.instagram.com/reel/DNjAuVUz1OI/) | 2025-08-19 |  | 4 | 0 |  |  |
| 495 | [DOPE0cOCR6s](https://www.instagram.com/reel/DOPE0cOCR6s/) | 2025-09-05 |  | 3 | 1 |  |  |
| 496 | [DOPE6U1if9b](https://www.instagram.com/reel/DOPE6U1if9b/) | 2025-09-05 | 65s | 4 | 0 |  | mp4 |
| 497 | [DOPFROmiU5x](https://www.instagram.com/reel/DOPFROmiU5x/) | 2025-09-05 | 49s | 3 | 1 | This 19 year old guru is making 600K a month by forging a new type of creator, the anti-gu | mp4, tx, bd |
| 498 | [DOWgG36CS61](https://www.instagram.com/reel/DOWgG36CS61/) | 2025-09-08 | 60s | 4 | 0 | This coach that coaches your favorite coaches coach uses the snapchat content strategy | mp4, tx, bd |
| 499 | [DTIoqm3j2_6](https://www.instagram.com/reel/DTIoqm3j2_6/) | 2026-01-05 | 8s | 4 | 0 | Oh boy, I can't wait to check my requests. | mp4, tx, bd |
| 500 | [DTQT47UDDfA](https://www.instagram.com/reel/DTQT47UDDfA/) | 2026-01-08 | 61s | 4 | 0 |  | mp4 |
| 501 | [DNZ4F-GtE8f](https://www.instagram.com/reel/DNZ4F-GtE8f/) | 2025-08-15 | 56s | 2 | 1 |  | mp4 |
| 502 | [DNZ51-ht0LV](https://www.instagram.com/reel/DNZ51-ht0LV/) | 2025-08-15 | 60s | 3 | 0 |  | mp4 |
| 503 | [DNi_x2qzs1T](https://www.instagram.com/reel/DNi_x2qzs1T/) | 2025-08-19 | 60s | 3 | 0 |  | mp4 |
| 504 | [DNjA5GUpVkI](https://www.instagram.com/reel/DNjA5GUpVkI/) | 2025-08-19 | 56s | 3 | 0 |  | mp4 |
| 505 | [DOTcw0niTHX](https://www.instagram.com/reel/DOTcw0niTHX/) | 2025-09-07 | 49s | 3 | 0 |  | mp4 |
| 506 | [DOTjaS-DTR0](https://www.instagram.com/reel/DOTjaS-DTR0/) | 2025-09-07 | 60s | 3 | 0 |  | mp4 |
| 507 | [DOTjcxqDVC9](https://www.instagram.com/reel/DOTjcxqDVC9/) | 2025-09-07 | 46s | 3 | 0 |  | mp4 |
| 508 | [DOTj-6pjc-t](https://www.instagram.com/reel/DOTj-6pjc-t/) | 2025-09-07 | 60s | 3 | 0 |  | mp4 |
| 509 | [DOWggfwkz4i](https://www.instagram.com/reel/DOWggfwkz4i/) | 2025-09-08 | 50s | 3 | 0 |  | mp4 |
| 510 | [DSlpCl0iYfD](https://www.instagram.com/reel/DSlpCl0iYfD/) | 2025-12-22 | 38s | 3 | 0 |  | mp4 |
| 511 | [DT1muKNkRq5](https://www.instagram.com/reel/DT1muKNkRq5/) | 2026-01-22 | 49s | 1 | 2 |  | mp4 |
| 512 | [DcMr02lBHSy](https://www.instagram.com/reel/DcMr02lBHSy/) | 2026-08-18 | 122s | 3 | 0 |  | mp4 |
| 513 | [DcMsoukh8vC](https://www.instagram.com/reel/DcMsoukh8vC/) | 2026-08-18 | 123s | 3 | 0 |  | mp4 |
| 514 | [DMB6JQXvY0Z](https://www.instagram.com/reel/DMB6JQXvY0Z/) | 2025-07-12 | 22s | 1 | 1 |  | mp4 |
| 515 | [DNZ2PlzNRVK](https://www.instagram.com/reel/DNZ2PlzNRVK/) | 2025-08-15 | 60s | 2 | 0 |  | mp4 |
| 516 | [DNZ2kNktSfE](https://www.instagram.com/reel/DNZ2kNktSfE/) | 2025-08-15 | 56s | 2 | 0 |  | mp4 |
| 517 | [DNZ3ascNVhS](https://www.instagram.com/reel/DNZ3ascNVhS/) | 2025-08-15 | 43s | 2 | 0 |  | mp4 |
| 518 | [DNZ5xaENODf](https://www.instagram.com/reel/DNZ5xaENODf/) | 2025-08-15 | 43s | 2 | 0 |  | mp4 |
| 519 | [DNgkFWITs8N](https://www.instagram.com/reel/DNgkFWITs8N/) | 2025-08-18 | 60s | 2 | 0 |  | mp4 |
| 520 | [DNgkDX-zv46](https://www.instagram.com/reel/DNgkDX-zv46/) | 2025-08-18 | 49s | 2 | 0 |  | mp4 |
| 521 | [DOTcvFqiTYX](https://www.instagram.com/reel/DOTcvFqiTYX/) | 2025-09-07 | 50s | 2 | 0 |  | mp4 |
| 522 | [DOTkOdOjQUK](https://www.instagram.com/reel/DOTkOdOjQUK/) | 2025-09-07 | 56s | 2 | 0 |  | mp4 |
| 523 | [DOWf4gxk0WG](https://www.instagram.com/reel/DOWf4gxk0WG/) | 2025-09-08 | 50s | 2 | 0 |  | mp4 |
| 524 | [DOWf6d8E-Pl](https://www.instagram.com/reel/DOWf6d8E-Pl/) | 2025-09-08 |  | 2 | 0 |  |  |
| 525 | [DOWgBnzE8NW](https://www.instagram.com/reel/DOWgBnzE8NW/) | 2025-09-08 | 50s | 2 | 0 |  | mp4 |
| 526 | [DOWgiu2k5JC](https://www.instagram.com/reel/DOWgiu2k5JC/) | 2025-09-08 | 49s | 2 | 0 |  | mp4 |
| 527 | [DSV068Jkh6t](https://www.instagram.com/reel/DSV068Jkh6t/) | 2025-12-16 | 43s | 2 | 0 |  | mp4 |
| 528 | [DTqk2_CksfS](https://www.instagram.com/reel/DTqk2_CksfS/) | 2026-01-18 | 24s | 2 | 0 |  | mp4 |
| 529 | [DUB3lCWk8Hz](https://www.instagram.com/reel/DUB3lCWk8Hz/) | 2026-01-27 | 27s | 2 | 0 |  | mp4 |
| 530 | [DVF4q2sgvkZ](https://www.instagram.com/reel/DVF4q2sgvkZ/) | 2026-02-22 | 29s | 2 | 0 |  | mp4 |
| 531 | [DczTA9FB1HP](https://www.instagram.com/reel/DczTA9FB1HP/) | 2026-09-02 | 91s | 2 | 0 |  | mp4 |
| 532 | [DNZ2M3_NuwC](https://www.instagram.com/reel/DNZ2M3_NuwC/) | 2025-08-15 | 50s | 1 | 0 |  | mp4 |
| 533 | [DNZ2R4CNvT9](https://www.instagram.com/reel/DNZ2R4CNvT9/) | 2025-08-15 | 46s | 1 | 0 |  | mp4 |
| 534 | [DOTdHIBieHz](https://www.instagram.com/reel/DOTdHIBieHz/) | 2025-09-07 | 56s | 1 | 0 |  | mp4 |
| 535 | [DOTjVPdjamz](https://www.instagram.com/reel/DOTjVPdjamz/) | 2025-09-07 | 50s | 1 | 0 |  | mp4 |
| 536 | [DOTjgzdDVDe](https://www.instagram.com/reel/DOTjgzdDVDe/) | 2025-09-07 | 56s | 1 | 0 |  | mp4 |
| 537 | [DOWgkaxExXH](https://www.instagram.com/reel/DOWgkaxExXH/) | 2025-09-08 | 60s | 1 | 0 |  | mp4 |
| 538 | [DOWglE6kzZm](https://www.instagram.com/reel/DOWglE6kzZm/) | 2025-09-08 | 46s | 1 | 0 |  | mp4 |
| 539 | [DUEa7Q6E9Ky](https://www.instagram.com/reel/DUEa7Q6E9Ky/) | 2026-01-28 | 46s | 1 | 0 |  | mp4 |
| 540 | [DVRgzkbEoj_](https://www.instagram.com/reel/DVRgzkbEoj_/) | 2026-02-27 | 62s | 1 | 0 |  | mp4 |
| 541 | [DcMXZAMh2t5](https://www.instagram.com/reel/DcMXZAMh2t5/) | 2026-08-18 | 122s | 1 | 0 |  | mp4 |
| 542 | [DcVNXNUCVRv](https://www.instagram.com/reel/DcVNXNUCVRv/) | 2026-08-21 | 130s | 1 | 0 |  | mp4 |
| 543 | [Dcu_Ug0ia-Q](https://www.instagram.com/reel/Dcu_Ug0ia-Q/) | 2026-08-31 | 91s | 1 | 0 |  | mp4 |
| 544 | [DMZaWUrvBOn](https://www.instagram.com/reel/DMZaWUrvBOn/) | 2025-07-21 | 10s | 0 | 0 |  | mp4 |
| 545 | [DNZ50emtnsh](https://www.instagram.com/reel/DNZ50emtnsh/) | 2025-08-15 | 49s | 0 | 0 |  | mp4 |
| 546 | [DOTj9FFjdr1](https://www.instagram.com/reel/DOTj9FFjdr1/) | 2025-09-07 | 49s | 0 | 0 |  | mp4 |
| 547 | [DOTnacsDXvB](https://www.instagram.com/reel/DOTnacsDXvB/) | 2025-09-07 | 49s | 0 | 0 |  | mp4 |
| 548 | [DOWgDxZE69F](https://www.instagram.com/reel/DOWgDxZE69F/) | 2025-09-08 | 49s | 0 | 0 |  | mp4 |
| 549 | [DOWgvE0Ezgs](https://www.instagram.com/reel/DOWgvE0Ezgs/) | 2025-09-08 | 49s | 0 | 0 |  | mp4 |
| 550 | [DU90jJyAmCb](https://www.instagram.com/reel/DU90jJyAmCb/) | 2026-02-19 | 55s | 0 | 0 |  | mp4 |
| 551 | [DambhfMi1Qq](https://www.instagram.com/reel/DambhfMi1Qq/) | 2026-07-09 | 68s | 0 | 0 |  | mp4 |
| 552 | [DcMszouBg0X](https://www.instagram.com/reel/DcMszouBg0X/) | 2026-08-18 | 122s | 0 | 0 |  | mp4 |
| 553 | [DcMsLGlBRn0](https://www.instagram.com/reel/DcMsLGlBRn0/) | 2026-08-18 | 123s | 0 | 0 |  | mp4 |
| 554 | [DcPDnWlS5rV](https://www.instagram.com/reel/DcPDnWlS5rV/) | 2026-08-19 | 24s | 0 | 0 |  | mp4 |
| 555 | [DcRxqrAh6oE](https://www.instagram.com/reel/DcRxqrAh6oE/) | 2026-08-20 | 46s | 0 | 0 |  | mp4 |
| 556 | [DcUa15EBQkq](https://www.instagram.com/reel/DcUa15EBQkq/) | 2026-08-21 | 130s | 0 | 0 |  | mp4 |
| 557 | [DcWZNdain2L](https://www.instagram.com/reel/DcWZNdain2L/) | 2026-08-22 | 44s | 0 | 0 |  | mp4 |
| 558 | [Dc16cwUBUqh](https://www.instagram.com/reel/Dc16cwUBUqh/) | 2026-09-03 | 42s | 0 | 0 |  | mp4 |
| 559 | [DddFJZsi_JC](https://www.instagram.com/reel/DddFJZsi_JC/) | 2026-09-18 | 84s | 0 | 0 |  | mp4 |
| 560 | [Dfz42Ogihlv](https://www.instagram.com/reel/Dfz42Ogihlv/) | 2026-11-16 | 73s | 43 | — | Take away my passport and deport me back to China | mp4, tx, bd |

## Carousels + image posts (catalog-only)

| Shortcode | Type | Date (connector) | Likes | Comments | Caption (first line) |
|---|---|---|---|---|---|
| [DfS-L51j4hK](https://www.instagram.com/p/DfS-L51j4hK/) | carousel | 2026-11-03 | 111 | 2 | Video Breakdown of @shelby.sapp |
| [DfQPBSpkRUG](https://www.instagram.com/p/DfQPBSpkRUG/) | carousel | 2026-11-02 | 102 | 2 | Good content strategy rejects 99% of your ideas! |
| [DfLku2QkZcP](https://www.instagram.com/p/DfLku2QkZcP/) | carousel | 2026-10-31 | 69 | 0 | The Lore Loop |
| [DfIyn6xCsUH](https://www.instagram.com/p/DfIyn6xCsUH/) | carousel | 2026-10-30 | 407 | 9 | Check my link in bio, if you want to learn more |
| [DfDwkljmAXg](https://www.instagram.com/p/DfDwkljmAXg/) | carousel | 2026-10-28 | 155 | 41 |  |
| [De-cMQMjZjj](https://www.instagram.com/p/De-cMQMjZjj/) | carousel | 2026-10-26 | 181 | 71 | Hey what’s up 🙋 I'm Sky and 3 years ago I got OBSESSED with 1 question: |
| [De2kC4nEptM](https://www.instagram.com/p/De2kC4nEptM/) | carousel | 2026-10-23 | 139 | 82 | Comment caption for the prompt |
| [DexfsH5l0q6](https://www.instagram.com/p/DexfsH5l0q6/) | carousel | 2026-10-21 | 1152 | 893 | Hey what’s up 🙋 I'm Sky and 3 years ago I got OBSESSED with 1 question: |
| [DevFnZxlCQO](https://www.instagram.com/p/DevFnZxlCQO/) | carousel | 2026-10-20 | 1206 | 807 | Hey what’s up 🙋 I'm Sky and 3 years ago I got OBSESSED with 1 question: |
| [?story_media_id=3876741436263286887](https://www.instagram.com/stories/highlights/18108761134891836/?story_media_id=3876741436263286887) | image | 2026-04-16 | 0 | 0 | ‼️EDITORS‼️ |
| [?story_media_id=3873447322453184061](https://www.instagram.com/stories/highlights/18081993812378203/?story_media_id=3873447322453184061) | image | 2026-04-11 | 0 | 0 | First video already a 20x outlier |
| [?story_media_id=3863181522794775853](https://www.instagram.com/stories/highlights/18081993812378203/?story_media_id=3863181522794775853) | image | 2026-03-28 | 0 | 0 | Barely a month in  |
| [DSYULMGk12r](https://www.instagram.com/p/DSYULMGk12r/) | carousel | 2025-12-17 | 69 | 6 |  |

## Gaps

- DeGQ3NAC2f9 — known from local Nov 2026 thumbnail notes (238 likes / 30 comments at that pass); absent from the connector catalog, so no catalog row; not downloaded in this harvest.
- Any video rows above with an empty Files cell were not yet downloaded at snapshot time — the resumable scripts above continue from exactly those rows.
- Breakdowns produced by `make_breakdowns_auto.py` carry transcript + measured audio/scene data and a contact-sheet pointer; their device inventories are limited to the sheet until a frame pass is run. Hand-written breakdowns (the 17 reused-decode reels + the top-engagement reels processed first in this harvest) carry full device inventories.
| 561 | [Df-ySM2ktiK](https://www.instagram.com/reel/Df-ySM2ktiK/) | 2026-11-21 | 59s |  |  | Your hooks are tanking because they're either too short or too long. (Four Niche Levels) | mp4, tx, bd |
| 562 | [Df5SPJiiY0S](https://www.instagram.com/reel/Df5SPJiiY0S/) | 2026-11-21 | 57s |  |  | If your videos have been tanking for the last six months — 2026 content playbook. | mp4, tx, bd |
| 563 | [Df8IThFgIXy](https://www.instagram.com/reel/Df8IThFgIXy/) | 2026-11-21 | 73s |  |  | Here's how I built an original creative format that got over 140,000 views. | mp4, tx, bd |

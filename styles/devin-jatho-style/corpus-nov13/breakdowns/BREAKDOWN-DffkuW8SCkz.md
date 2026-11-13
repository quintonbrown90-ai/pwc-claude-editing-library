# BREAKDOWN — DffkuW8SCkz — "SALES CALL HACK — Zoom waiting-room highlight reel"

- **URL:** https://www.instagram.com/reel/DffkuW8SCkz/  |  **Posted:** 2026-11-08  |  **Engagement at pull:** 0 likes / 3 comments
- **File:** `videos/devinjatho_DffkuW8SCkz.mp4` — 720x1280, 30fps, 41.2s
- **Format:** S — screen-demo teaching
- **Method:** faster-whisper word timings + ffmpeg scene detection (gt(scene,0.35) — a LOWER bound on cuts: dissolves and same-framing jump cuts score under threshold) + 0.1s RMS profile with onset candidates. Visual states from the library DECODE/frame reads (see `--library-decode` companion). Segment boundaries ±0.5s unless a row says MEASURED. Semantic SFX identities are NOT claimed from RMS alone — onset rows say 'onset candidate'.

## Device / segment table

| # | Time | Visual (asset-level) | Caption / text | Transition in | Sound |
|---:|---|---|---|---|---|
| 1 | 0.0–2.0s | HOOK SLAM (full-screen): laptop on desk showing the Zoom waiting room; Devin behind it | Headline 'SALES CALL HACK' — huge condensed caps, RED, top of frame | hard cut at 0.0 | First 0.1s RMS 0.44 (~2x speech avg) — probable impact under 'Right' (unconfirmed, RMS-only) |
| 2 | 2.0–4.5s | A-roll: dark studio, Devin to camera | Phrase chunks begin (white condensed caps, 2-line, lower third) | hard cut | voice only |
| 3 | 4.5–8.1s | FULL-SCREEN screen recording: Zoom waiting room with 'Meet ZoomMate' ad banner — the problem shown, not described | no speech captions over the screen; the UI carries the text | hard cut | voice over screen |
| 4 | 8.1–13.0s | A-roll: the promise (testimonial highlight reel swap) | phrase chunks; 'HIGHLIGHT REEL' class emphasis | hard cut (return to face) | voice only |
| 5 | 13.0–16.1s | FULL-SCREEN mock Zoom call: gallery tiles, Devin (left) + prospect (right) — the waiting-room experience performed | Zoom UI text only | hard cut | voice over; the call itself is silent |
| 6 | 16.1–19.0s | A-roll: 'actually super easy' ease claim | phrase chunks | hard cut | voice only |
| 7 | 19.0–22.0s | SPLIT: Zoom website top ~55% / face bottom ~45%; white glove cursor clicks 'Find your plan' | phrase chunks at bottom | hard cut | voice; cursor clicks unconfirmed as SFX (RMS-only) |
| 8 | 22.0–28.0s | Settings walkthrough (split → screen): Zoom Settings > Meeting; cursor points at 'Meeting' | Instruction pill 'AND THEN SCROLL DOWN' — white on BLUE pill at the screen/face seam (Q: teal) | hard cut | voice only |
| 9 | 28.0–32.5s | Screen recording: Customize Waiting Room → upload the highlight-reel video | UI text carries the step | hard cut | voice only |
| 10 | 32.5–34.1s | A-roll return: 'This is the highlight structure…' | phrase chunks | CROSS-DISSOLVE ~3 frames at ~34.07 (MEASURED) — returns to face dissolve, not cut | voice only |
| 11 | 34.1–35.5s | Gesture-synced structure card: floating video-player card 'Zoom Room Structure — 00:01 — Testimonial Hook' fades in beside his raised index finger | card carries its own title text | card FADE ~3 frames at ~34.27 (MEASURED); finger rises ~34.10, word 'This' 34.20 — gesture leads card by ~0.2s | RMS 0.26 at 34.0–34.3 — voice + possible soft whoosh (unconfirmed) |
| 12 | 35.5–40.0s | A-roll: CTA spoken ('comment the word Zoom') | phrase chunks | hard cut (card out) | voice only |
| 13 | 40.0–41.2s | CTA MOCK end frame: IG notification 'Devin Jatho — Here's our Zoom Highlight Reel' top; comment chip 'ZOOM' + send arrow mid-frame; Devin holding the laptop | the mock IS the caption — no separate caption | hard cut | voice tail; no end sting detected |

## B-ROLL LOG (Devin / subject inserts — separate system)

| Time | B-roll insert |
|---|---|
| 13.0–16.1s | PERFORMED SCENARIO — Devin plays host in a fake sales call; full-screen cutaway; lands on '…let them in the meeting'; in/out = hard cuts; no added sound detected |

## Sound summary (measured)

- Duration 41.2s. Onset candidates (0.1s RMS jumps >2x and >=0.09): **33** = 8.0 per 10s — these include word onsets; they are an UPPER bound on designed SFX, not an SFX count.
- Silence spans (<-38dBFS-ish RMS 0.012, >=0.25s): 0 
- Scene cuts at gt(scene,0.35): 6 at [10.24, 11.41, 12.61, 23.49, 34.1, 40.97] — lower bound (see method note).

## 0.5-SECOND GRID

| t | Spoken words | Visual state | Caption on screen | Audio (RMS mean/max in bin) | Events |
|---:|---|---|---|---|---|
| 0.0 | Right now, when | HOOK SLAM (full-screen): laptop on desk showing the Zoom waiting room; Devin behind it | Headline 'SALES CALL HACK' — huge condensed caps, RED, top of frame | 0.27/0.44 | SEGMENT IN: hard cut at 0.0 |
| 0.5 | someone joins | HOOK SLAM (full-screen): laptop on desk showing the Zoom waiting room; Devin behind it | Headline 'SALES CALL HACK' — huge condensed caps, RED, top of frame | 0.17/0.22 |  |
| 1.0 | your Zoom, | HOOK SLAM (full-screen): laptop on desk showing the Zoom waiting room; Devin behind it | Headline 'SALES CALL HACK' — huge condensed caps, RED, top of frame | 0.18/0.24 | onset candidate |
| 1.5 |  | HOOK SLAM (full-screen): laptop on desk showing the Zoom waiting room; Devin behind it | Headline 'SALES CALL HACK' — huge condensed caps, RED, top of frame | 0.14/0.18 |  |
| 2.0 | your waiting room | A-roll: dark studio, Devin to camera | Phrase chunks begin (white condensed caps, 2-line, lower third) | 0.20/0.29 | SEGMENT IN: hard cut |
| 2.5 | looks like | A-roll: dark studio, Devin to camera | Phrase chunks begin (white condensed caps, 2-line, lower third) | 0.19/0.26 |  |
| 3.0 | this. | A-roll: dark studio, Devin to camera | Phrase chunks begin (white condensed caps, 2-line, lower third) | 0.22/0.27 |  |
| 3.5 | It's a fucking | A-roll: dark studio, Devin to camera | Phrase chunks begin (white condensed caps, 2-line, lower third) | 0.15/0.20 |  |
| 4.0 | ad for | A-roll: dark studio, Devin to camera | Phrase chunks begin (white condensed caps, 2-line, lower third) | 0.18/0.22 |  |
| 4.5 | Zoom. | FULL-SCREEN screen recording: Zoom waiting room with 'Meet ZoomMate' ad banner — the problem shown, not descri… | no speech captions over the screen; the UI carries the text | 0.14/0.18 | SEGMENT IN: hard cut |
| 5.0 | But what | FULL-SCREEN screen recording: Zoom waiting room with 'Meet ZoomMate' ad banner — the problem shown, not descri… | no speech captions over the screen; the UI carries the text | 0.14/0.22 | onset candidate |
| 5.5 | if, | FULL-SCREEN screen recording: Zoom waiting room with 'Meet ZoomMate' ad banner — the problem shown, not descri… | no speech captions over the screen; the UI carries the text | 0.17/0.27 | onset candidate |
| 6.0 | with one | FULL-SCREEN screen recording: Zoom waiting room with 'Meet ZoomMate' ad banner — the problem shown, not descri… | no speech captions over the screen; the UI carries the text | 0.15/0.23 |  |
| 6.5 | setting, you | FULL-SCREEN screen recording: Zoom waiting room with 'Meet ZoomMate' ad banner — the problem shown, not descri… | no speech captions over the screen; the UI carries the text | 0.17/0.20 |  |
| 7.0 | could swap it | FULL-SCREEN screen recording: Zoom waiting room with 'Meet ZoomMate' ad banner — the problem shown, not descri… | no speech captions over the screen; the UI carries the text | 0.12/0.24 | onset candidate |
| 7.5 | to the | FULL-SCREEN screen recording: Zoom waiting room with 'Meet ZoomMate' ad banner — the problem shown, not descri… | no speech captions over the screen; the UI carries the text | 0.14/0.24 |  |
| 8.0 | highlight reel | FULL-SCREEN screen recording: Zoom waiting room with 'Meet ZoomMate' ad banner — the problem shown, not descri… | no speech captions over the screen; the UI carries the text | 0.18/0.22 |  |
| 8.5 | of your best | A-roll: the promise (testimonial highlight reel swap) | phrase chunks; 'HIGHLIGHT REEL' class emphasis | 0.17/0.19 | SEGMENT IN: hard cut (return to face) |
| 9.0 | testimonials, | A-roll: the promise (testimonial highlight reel swap) | phrase chunks; 'HIGHLIGHT REEL' class emphasis | 0.12/0.19 | onset candidate |
| 9.5 |  | A-roll: the promise (testimonial highlight reel swap) | phrase chunks; 'HIGHLIGHT REEL' class emphasis | 0.15/0.25 |  |
| 10.0 | showing | A-roll: the promise (testimonial highlight reel swap) | phrase chunks; 'HIGHLIGHT REEL' class emphasis | 0.13/0.27 | onset candidate; SCENE CUT (gt0.35) |
| 10.5 | social proof, | A-roll: the promise (testimonial highlight reel swap) | phrase chunks; 'HIGHLIGHT REEL' class emphasis | 0.20/0.28 |  |
| 11.0 | rehannelling | A-roll: the promise (testimonial highlight reel swap) | phrase chunks; 'HIGHLIGHT REEL' class emphasis | 0.12/0.22 | onset candidate; SCENE CUT (gt0.35) |
| 11.5 | objections, | A-roll: the promise (testimonial highlight reel swap) | phrase chunks; 'HIGHLIGHT REEL' class emphasis | 0.23/0.27 |  |
| 12.0 |  | A-roll: the promise (testimonial highlight reel swap) | phrase chunks; 'HIGHLIGHT REEL' class emphasis | 0.12/0.23 | onset candidate |
| 12.5 | and dramatically | A-roll: the promise (testimonial highlight reel swap) | phrase chunks; 'HIGHLIGHT REEL' class emphasis | 0.19/0.23 | SCENE CUT (gt0.35) |
| 13.0 | increasing | FULL-SCREEN mock Zoom call: gallery tiles, Devin (left) + prospect (right) — the waiting-room experience perfo… | Zoom UI text only | 0.16/0.24 | SEGMENT IN: hard cut |
| 13.5 | the likelihood | FULL-SCREEN mock Zoom call: gallery tiles, Devin (left) + prospect (right) — the waiting-room experience perfo… | Zoom UI text only | 0.14/0.18 |  |
| 14.0 | that you | FULL-SCREEN mock Zoom call: gallery tiles, Devin (left) + prospect (right) — the waiting-room experience perfo… | Zoom UI text only | 0.13/0.20 | onset candidate |
| 14.5 | close the | FULL-SCREEN mock Zoom call: gallery tiles, Devin (left) + prospect (right) — the waiting-room experience perfo… | Zoom UI text only | 0.17/0.35 | onset candidate |
| 15.0 | prospect once | FULL-SCREEN mock Zoom call: gallery tiles, Devin (left) + prospect (right) — the waiting-room experience perfo… | Zoom UI text only | 0.14/0.21 | onset candidate |
| 15.5 | you | FULL-SCREEN mock Zoom call: gallery tiles, Devin (left) + prospect (right) — the waiting-room experience perfo… | Zoom UI text only | 0.08/0.19 | onset candidate |
| 16.0 | let them in | FULL-SCREEN mock Zoom call: gallery tiles, Devin (left) + prospect (right) — the waiting-room experience perfo… | Zoom UI text only | 0.18/0.24 |  |
| 16.5 | the meeting. | A-roll: 'actually super easy' ease claim | phrase chunks | 0.25/0.28 | SEGMENT IN: hard cut |
| 17.0 | To do this, | A-roll: 'actually super easy' ease claim | phrase chunks | 0.16/0.24 |  |
| 17.5 | this | A-roll: 'actually super easy' ease claim | phrase chunks | 0.07/0.08 |  |
| 18.0 | is actually super | A-roll: 'actually super easy' ease claim | phrase chunks | 0.11/0.16 |  |
| 18.5 | easy. | A-roll: 'actually super easy' ease claim | phrase chunks | 0.08/0.12 |  |
| 19.0 | Just head | SPLIT: Zoom website top ~55% / face bottom ~45%; white glove cursor clicks 'Find your plan' | phrase chunks at bottom | 0.09/0.12 | SEGMENT IN: hard cut |
| 19.5 | over to Zoom | SPLIT: Zoom website top ~55% / face bottom ~45%; white glove cursor clicks 'Find your plan' | phrase chunks at bottom | 0.14/0.25 |  |
| 20.0 | .com, | SPLIT: Zoom website top ~55% / face bottom ~45%; white glove cursor clicks 'Find your plan' | phrase chunks at bottom | 0.13/0.19 |  |
| 20.5 | click on | SPLIT: Zoom website top ~55% / face bottom ~45%; white glove cursor clicks 'Find your plan' | phrase chunks at bottom | 0.07/0.11 | onset candidate |
| 21.0 | your profile at | SPLIT: Zoom website top ~55% / face bottom ~45%; white glove cursor clicks 'Find your plan' | phrase chunks at bottom | 0.13/0.17 |  |
| 21.5 | the top | SPLIT: Zoom website top ~55% / face bottom ~45%; white glove cursor clicks 'Find your plan' | phrase chunks at bottom | 0.12/0.17 |  |
| 22.0 | of rights, | Settings walkthrough (split → screen): Zoom Settings > Meeting; cursor points at 'Meeting' | Instruction pill 'AND THEN SCROLL DOWN' — white on BLUE pill at the screen/face … | 0.12/0.17 | onset candidate; SEGMENT IN: hard cut |
| 22.5 | and then | Settings walkthrough (split → screen): Zoom Settings > Meeting; cursor points at 'Meeting' | Instruction pill 'AND THEN SCROLL DOWN' — white on BLUE pill at the screen/face … | 0.11/0.20 |  |
| 23.0 | click on Settings. | Settings walkthrough (split → screen): Zoom Settings > Meeting; cursor points at 'Meeting' | Instruction pill 'AND THEN SCROLL DOWN' — white on BLUE pill at the screen/face … | 0.12/0.16 | SCENE CUT (gt0.35) |
| 23.5 |  | Settings walkthrough (split → screen): Zoom Settings > Meeting; cursor points at 'Meeting' | Instruction pill 'AND THEN SCROLL DOWN' — white on BLUE pill at the screen/face … | 0.07/0.10 |  |
| 24.0 | From here, click | Settings walkthrough (split → screen): Zoom Settings > Meeting; cursor points at 'Meeting' | Instruction pill 'AND THEN SCROLL DOWN' — white on BLUE pill at the screen/face … | 0.16/0.21 | onset candidate |
| 24.5 | on Meeting, | Settings walkthrough (split → screen): Zoom Settings > Meeting; cursor points at 'Meeting' | Instruction pill 'AND THEN SCROLL DOWN' — white on BLUE pill at the screen/face … | 0.11/0.14 | onset candidate |
| 25.0 | and then | Settings walkthrough (split → screen): Zoom Settings > Meeting; cursor points at 'Meeting' | Instruction pill 'AND THEN SCROLL DOWN' — white on BLUE pill at the screen/face … | 0.13/0.14 |  |
| 25.5 | scroll down | Settings walkthrough (split → screen): Zoom Settings > Meeting; cursor points at 'Meeting' | Instruction pill 'AND THEN SCROLL DOWN' — white on BLUE pill at the screen/face … | 0.15/0.27 |  |
| 26.0 | until | Settings walkthrough (split → screen): Zoom Settings > Meeting; cursor points at 'Meeting' | Instruction pill 'AND THEN SCROLL DOWN' — white on BLUE pill at the screen/face … | 0.12/0.16 |  |
| 26.5 | you find | Settings walkthrough (split → screen): Zoom Settings > Meeting; cursor points at 'Meeting' | Instruction pill 'AND THEN SCROLL DOWN' — white on BLUE pill at the screen/face … | 0.13/0.14 |  |
| 27.0 | Customize | Settings walkthrough (split → screen): Zoom Settings > Meeting; cursor points at 'Meeting' | Instruction pill 'AND THEN SCROLL DOWN' — white on BLUE pill at the screen/face … | 0.12/0.17 | onset candidate |
| 27.5 | Waiting | Settings walkthrough (split → screen): Zoom Settings > Meeting; cursor points at 'Meeting' | Instruction pill 'AND THEN SCROLL DOWN' — white on BLUE pill at the screen/face … | 0.10/0.14 |  |
| 28.0 | Room. Now, | Screen recording: Customize Waiting Room → upload the highlight-reel video | UI text carries the step | 0.07/0.13 | SEGMENT IN: hard cut |
| 28.5 | just | Screen recording: Customize Waiting Room → upload the highlight-reel video | UI text carries the step | 0.14/0.19 | onset candidate |
| 29.0 | click on a | Screen recording: Customize Waiting Room → upload the highlight-reel video | UI text carries the step | 0.08/0.13 |  |
| 29.5 | video, | Screen recording: Customize Waiting Room → upload the highlight-reel video | UI text carries the step | 0.12/0.17 | onset candidate |
| 30.0 | and then go | Screen recording: Customize Waiting Room → upload the highlight-reel video | UI text carries the step | 0.15/0.18 |  |
| 30.5 | ahead and | Screen recording: Customize Waiting Room → upload the highlight-reel video | UI text carries the step | 0.20/0.29 | onset candidate |
| 31.0 | upload the | Screen recording: Customize Waiting Room → upload the highlight-reel video | UI text carries the step | 0.11/0.16 | onset candidate |
| 31.5 | highlights reel | Screen recording: Customize Waiting Room → upload the highlight-reel video | UI text carries the step | 0.12/0.16 |  |
| 32.0 | of | Screen recording: Customize Waiting Room → upload the highlight-reel video | UI text carries the step | 0.11/0.17 | onset candidate |
| 32.5 | your best testimonials. | A-roll return: 'This is the highlight structure…' | phrase chunks | 0.15/0.21 | onset candidate; SEGMENT IN: CROSS-DISSOLVE ~3 frames at ~34.07 (MEASURED) — returns to face dissolve, not cut |
| 33.0 |  | A-roll return: 'This is the highlight structure…' | phrase chunks | 0.13/0.17 |  |
| 33.5 |  | A-roll return: 'This is the highlight structure…' | phrase chunks | 0.17/0.21 |  |
| 34.0 | This is | A-roll return: 'This is the highlight structure…' | phrase chunks | 0.21/0.27 | SCENE CUT (gt0.35) |
| 34.5 | the highlight structure | Gesture-synced structure card: floating video-player card 'Zoom Room Structure — 00:01 — Testimonial Hook' fad… | card carries its own title text | 0.15/0.19 | SEGMENT IN: card FADE ~3 frames at ~34.27 (MEASURED); finger rises ~34.10, word 'This' 34.20 — gesture leads card by ~0.2s |
| 35.0 | that we found, | Gesture-synced structure card: floating video-player card 'Zoom Room Structure — 00:01 — Testimonial Hook' fad… | card carries its own title text | 0.12/0.18 |  |
| 35.5 | works | A-roll: CTA spoken ('comment the word Zoom') | phrase chunks | 0.14/0.26 | onset candidate; SEGMENT IN: hard cut (card out) |
| 36.0 | best, | A-roll: CTA spoken ('comment the word Zoom') | phrase chunks | 0.10/0.19 | onset candidate |
| 36.5 | and then if you want to watch | A-roll: CTA spoken ('comment the word Zoom') | phrase chunks | 0.14/0.16 | onset candidate |
| 37.0 | hours for | A-roll: CTA spoken ('comment the word Zoom') | phrase chunks | 0.16/0.25 | onset candidate |
| 37.5 | inspiration, | A-roll: CTA spoken ('comment the word Zoom') | phrase chunks | 0.15/0.20 | onset candidate |
| 38.0 | just | A-roll: CTA spoken ('comment the word Zoom') | phrase chunks | 0.11/0.22 |  |
| 38.5 | comment to the | A-roll: CTA spoken ('comment the word Zoom') | phrase chunks | 0.13/0.21 | onset candidate |
| 39.0 | word Zoom, | A-roll: CTA spoken ('comment the word Zoom') | phrase chunks | 0.14/0.17 |  |
| 39.5 | and I'll | A-roll: CTA spoken ('comment the word Zoom') | phrase chunks | 0.09/0.21 | onset candidate |
| 40.0 | send it to you. | CTA MOCK end frame: IG notification 'Devin Jatho — Here's our Zoom Highlight Reel' top; comment chip 'ZOOM' + … | the mock IS the caption — no separate caption | 0.10/0.16 | SEGMENT IN: hard cut |
| 40.5 |  | CTA MOCK end frame: IG notification 'Devin Jatho — Here's our Zoom Highlight Reel' top; comment chip 'ZOOM' + … | the mock IS the caption — no separate caption | 0.07/0.11 | SCENE CUT (gt0.35) |
| 41.0 |  | CTA MOCK end frame: IG notification 'Devin Jatho — Here's our Zoom Highlight Reel' top; comment chip 'ZOOM' + … | the mock IS the caption — no separate caption | 0.01/0.02 |  |

Companion evidence: `BREAKDOWN-DffkuW8SCkz--library-decode.md` (where present), `analysis/DffkuW8SCkz_analysis.json` (full RMS series, cut list, onsets).

## BACKGROUND LOG (keying / placement / behind-vs-over) — added Nov 13 pass
- No chroma keying of Devin anywhere in this reel. His backgrounds are: the practical dark studio (A-roll), or the frame is REPLACED by screen recordings (waiting-room ad, mock call, settings).
- Split beats (~19–28s): the screen is a PANEL in the top ~55% of frame with his live shot in the bottom ~45% — a layout composite, not a keyed overlay; the instruction pill sits ON the seam.
- The structure card (~34.07–35.5s) floats OVER the footage beside his raised finger — graphics-over, placed in empty space, never behind him and never over his face.

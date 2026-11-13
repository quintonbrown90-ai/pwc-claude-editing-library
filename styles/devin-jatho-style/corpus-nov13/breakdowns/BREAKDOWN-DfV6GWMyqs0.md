# BREAKDOWN — DfV6GWMyqs0 — "Fixing a Hook — live critique of a Hormozi video"

- **URL:** https://www.instagram.com/reel/DfV6GWMyqs0/  |  **Posted:** 2026-11-04  |  **Engagement at pull:** 58 likes / 3 comments
- **File:** `videos/devinjatho_DfV6GWMyqs0.mp4` — 720x1280, 30fps, 76.3s
- **Format:** C — live critique / makeover
- **Method:** faster-whisper word timings + ffmpeg scene detection (gt(scene,0.35) — a LOWER bound on cuts: dissolves and same-framing jump cuts score under threshold) + 0.1s RMS profile with onset candidates. Visual states from the library DECODE/frame reads (see `--library-decode` companion). Segment boundaries ±0.5s unless a row says MEASURED. Semantic SFX identities are NOT claimed from RMS alone — onset rows say 'onset candidate'.

## Device / segment table

| # | Time | Visual (asset-level) | Caption / text | Transition in | Sound |
|---:|---|---|---|---|---|
| 1 | 0.0–8.4s | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video plays on the phone screen | 'FIXING / SH*T HOOK' over the phone | hard cut at 0.0 | Devin's voice; subject audio faint from the phone (diegetic) |
| 2 | 8.4–18.0s | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | hard cut | voice only |
| 3 | 18.0–26.1s | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red/purple + 'FROM THIS' tag ~24–26s — the clutter made visible | annotation labels on the table | hard cut | voice; finger point at the table on '25 different elements' |
| 4 | 26.1–39.5s | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swap 'from this to this' | phrase chunks name each swap as it happens | each swap is a hard visual swap on its verb | voice only; swaps are silent |
| 5 | 39.5–50.8s | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' + chips '$194,613 → $567,123' in the empty space above him. TEXT SWAP MEASURED: old headline wipes to blank ~40.83s; new headline wipes in from ~41.4s (~0.6s); chips never move; frame holds near-static 41.4–48s | the frame IS a finished post — its own pill/chips are the text | wipe (text-only) inside a held frame | voice over; no SFX on the wipe detected |
| 6 | 51.0–59.1s | A-roll verdict: 'a golden visual hook' | phrase chunks | hard cut | voice only |
| 7 | 59.1–67.6s | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | hard cut | SUBJECT AUDIO insert under the diagnosis |
| 8 | 67.6–72.0s | FIXED FRAME v2 full-screen: subject with BOTH HANDS POINTING UP at dark badges '$194.6K → $567.1K +120.9%' — the fix shown as a finished frame | badges are the text | hard cut | voice over |
| 9 | 72.0–76.3s | CLOSE: warm brick room; Devin with phone in one hand; subject's image as a floating card beside him; 'BUT THIS…' — cuts mid-sentence (cliffhanger to part 2) | 'BUT THIS' chunk | hard cut; file ends mid-line, no end card | voice cut off by the edit (deliberate) |

## B-ROLL LOG (Devin / subject inserts — separate system)

| Time | B-roll insert |
|---|---|
| 0.0–8.4s | SUBJECT B-ROLL IN HAND: the subject's (Alex Hormozi's) own reel plays inside the phone Devin holds — PiP-by-prop framing; ~8s; lands on the 'we're gonna make it go viral' line; in = hard cut at 0, out = cut to A-roll |
| 18.0–26.1s | SUBJECT FOOTAGE AS EVIDENCE: subject's own video frame, full-screen, ~18–26s stretch (annotated ~24–26s); lands on the '25 elements / 6 at a time' diagnosis; in/out hard cuts |
| 39.5–50.8s | SUBJECT B-ROLL FULL-SCREEN: the subject's fixed frame held ~9s (39.5–50.8) — the longest subject cutaway in the batch; lands on 'change the text at the top to how to grow your business'; in = cut, out = cut to verdict |
| 59.1–67.6s | AUDIO B-ROLL: subject's spoken hook replayed ~59–64s while Devin diagnoses it; visual stays on Devin |
| 67.6–72.0s | SUBJECT B-ROLL FULL-SCREEN #2: ~4.4s; the subject performs the pointing gesture at his own numbers; lands on the fixed verbal hook line 'I took a business from this to this' |

## Sound summary (measured)

- Duration 76.3s. Onset candidates (0.1s RMS jumps >2x and >=0.09): **58** = 7.6 per 10s — these include word onsets; they are an UPPER bound on designed SFX, not an SFX count.
- Silence spans (<-38dBFS-ish RMS 0.012, >=0.25s): 0 
- Scene cuts at gt(scene,0.35): 3 at [28.06, 49.72, 67.27] — lower bound (see method note).

## 0.5-SECOND GRID

| t | Spoken words | Visual state | Caption on screen | Audio (RMS mean/max in bin) | Events |
|---:|---|---|---|---|---|
| 0.0 | This is | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.29/0.41 | SEGMENT IN: hard cut at 0.0 |
| 0.5 | Alex and Moses | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.19/0.22 |  |
| 1.0 | who will always | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.20/0.29 |  |
| 1.5 | view the video | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.18/0.30 |  |
| 2.0 | in 2026, | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.17/0.23 | onset candidate |
| 2.5 |  | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.12/0.14 |  |
| 3.0 | and we're | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.20/0.26 |  |
| 3.5 | gonna make it | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.17/0.22 |  |
| 4.0 | go f***ing | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.10/0.25 | onset candidate |
| 4.5 | viral. | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.16/0.22 | onset candidate |
| 5.0 | Let's | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.13/0.23 |  |
| 5.5 | watch. | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.14/0.25 | onset candidate |
| 6.0 | I | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.04/0.07 |  |
| 6.5 | just got a visitor from | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.18/0.26 | onset candidate |
| 7.0 | here to | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.12/0.22 | onset candidate |
| 7.5 | here | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.11/0.27 | onset candidate |
| 8.0 | fast. | PHONE OPEN: Devin holds a phone in both hands showing the subject's reel; 'let's watch' — the subject's video … | 'FIXING / SH*T HOOK' over the phone | 0.12/0.20 | onset candidate |
| 8.5 |  | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.03/0.10 | SEGMENT IN: hard cut |
| 9.0 | That's | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.05/0.20 | onset candidate |
| 9.5 | with | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.09/0.20 |  |
| 10.0 | Dog in | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.27/0.34 | onset candidate |
| 10.5 | it. | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.22/0.27 |  |
| 11.0 | So let's | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.14/0.18 |  |
| 11.5 | fix it. | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.12/0.17 |  |
| 12.0 | So your hook | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.10/0.20 | onset candidate |
| 12.5 | is put up into | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.17/0.26 |  |
| 13.0 | two different | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.15/0.20 |  |
| 13.5 | pieces. | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.10/0.14 |  |
| 14.0 | Your visual hook | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.18/0.26 |  |
| 14.5 | and your | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.17/0.23 |  |
| 15.0 | verbal hook. | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.20/0.27 |  |
| 15.5 |  | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.07/0.09 |  |
| 16.0 | So let's start with | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.13/0.20 | onset candidate |
| 16.5 | his visual | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.13/0.16 |  |
| 17.0 | hook. | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.11/0.17 |  |
| 17.5 |  | A-roll: hook split explained — visual hook vs verbal hook | phrase chunks | 0.06/0.08 |  |
| 18.0 | Her mosey | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.16/0.22 | onset candidate; SEGMENT IN: hard cut |
| 18.5 | has 25 | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.08/0.12 |  |
| 19.0 | different | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.26/0.54 | onset candidate |
| 19.5 |  | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.33/0.45 |  |
| 20.0 | elements on | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.26/0.33 |  |
| 20.5 | screen, | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.17/0.27 | onset candidate |
| 21.0 | but the | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.14/0.18 | onset candidate |
| 21.5 | human brain | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.09/0.11 |  |
| 22.0 | can only | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.10/0.13 |  |
| 22.5 | process | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.11/0.19 |  |
| 23.0 | six | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.14/0.18 |  |
| 23.5 | elements at | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.11/0.18 |  |
| 24.0 | a time. | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.09/0.12 |  |
| 24.5 |  | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.08/0.13 |  |
| 25.0 | So the viewer | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.08/0.15 |  |
| 25.5 | has | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.12/0.21 | onset candidate |
| 26.0 | no idea | DIAGNOSIS: subject's frame full-screen/phone-large with annotated stats table (49/83/27/47/56) highlighted red… | annotation labels on the table | 0.16/0.31 | onset candidate |
| 26.5 | what to look | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.18/0.27 | SEGMENT IN: each swap is a hard visual swap on its verb |
| 27.0 | at. So | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.08/0.15 |  |
| 27.5 |  | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.04/0.04 |  |
| 28.0 | we're gonna swap | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.15/0.19 | onset candidate; SCENE CUT (gt0.35) |
| 28.5 | all of | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.21/0.29 | onset candidate |
| 29.0 | the stats | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.23/0.31 |  |
| 29.5 | just | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.11/0.15 | onset candidate |
| 30.0 | to revenue | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.13/0.21 |  |
| 30.5 | so this is | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.13/0.15 |  |
| 31.0 | the only thing that people | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.11/0.14 | onset candidate |
| 31.5 | care about. | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.10/0.14 |  |
| 32.0 |  | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.09/0.15 |  |
| 32.5 | We'll remove | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.16/0.30 |  |
| 33.0 | it in | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.16/0.22 |  |
| 33.5 | 60 days | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.14/0.17 | onset candidate |
| 34.0 | because it's | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.11/0.16 |  |
| 34.5 | not needed, | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.11/0.15 | onset candidate |
| 35.0 |  | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.09/0.18 |  |
| 35.5 | and then we'll swap from | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.17/0.22 | onset candidate |
| 36.0 | this | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.20/0.25 |  |
| 36.5 | to this | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.15/0.25 |  |
| 37.0 | for | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.13/0.24 |  |
| 37.5 | just an error | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.09/0.13 | onset candidate |
| 38.0 | in the middle. | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.18/0.23 |  |
| 38.5 |  | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.09/0.12 |  |
| 39.0 | We're gonna change | THE FIX, step by step: A-roll + screen swaps — stats cut to revenue only; 'in 60 days' line removed; arrow swa… | phrase chunks name each swap as it happens | 0.11/0.17 | onset candidate |
| 39.5 | the text | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.13/0.16 | SEGMENT IN: wipe (text-only) inside a held frame |
| 40.0 | at the top | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.10/0.14 |  |
| 40.5 | to | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.10/0.17 | onset candidate |
| 41.0 | how to | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.12/0.16 |  |
| 41.5 | grow your | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.15/0.30 | onset candidate |
| 42.0 | business, | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.18/0.22 |  |
| 42.5 | and then | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.10/0.16 | onset candidate |
| 43.0 | the final fix | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.17/0.21 |  |
| 43.5 | is to swap | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.11/0.21 |  |
| 44.0 | to school sheet | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.13/0.21 | onset candidate |
| 44.5 | that a four | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.14/0.16 |  |
| 45.0 | -year -old could | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.19/0.25 |  |
| 45.5 | edit, | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.11/0.13 |  |
| 46.0 | and instead | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.09/0.16 | onset candidate |
| 46.5 | we're gonna | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.15/0.20 |  |
| 47.0 | show the actual | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.13/0.16 |  |
| 47.5 | payment processor | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.14/0.19 |  |
| 48.0 | to | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.14/0.21 |  |
| 48.5 | add | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.08/0.12 | onset candidate |
| 49.0 | proof. | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.13/0.17 | onset candidate |
| 49.5 | Now that's | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.17/0.29 | SCENE CUT (gt0.35) |
| 50.0 | my friends, | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.19/0.25 | onset candidate |
| 50.5 |  | THE FIXED FRAME full-screen: subject sits LOW (chin at bottom third); white pill 'HOW TO GROW YOUR BUSINESS' +… | the frame IS a finished post — its own pill/chips are the text | 0.15/0.20 |  |
| 51.0 | it's a golden visual | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.19/0.23 | SEGMENT IN: hard cut |
| 51.5 | hook, | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.19/0.30 |  |
| 52.0 | but we still | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.16/0.21 |  |
| 52.5 | have to fix | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.13/0.18 | onset candidate |
| 53.0 | this verbal hook | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.17/0.23 |  |
| 53.5 | because right | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.13/0.19 | onset candidate |
| 54.0 | now it's | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.18/0.24 | onset candidate |
| 54.5 | s***ing | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.12/0.17 | onset candidate |
| 55.0 | too. | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.10/0.11 |  |
| 55.5 | I | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.04/0.10 |  |
| 56.0 | still have a | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.11/0.22 | onset candidate |
| 56.5 | visitor from here | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.10/0.20 | onset candidate |
| 57.0 | to here | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.11/0.20 |  |
| 57.5 | fast. | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.08/0.14 | onset candidate |
| 58.0 |  | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.06/0.14 | onset candidate |
| 58.5 | So when this verbal | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.13/0.23 | onset candidate |
| 59.0 | hooky only | A-roll verdict: 'a golden visual hook' | phrase chunks | 0.17/0.26 | onset candidate |
| 59.5 | talks about | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.19/0.26 | onset candidate; SEGMENT IN: hard cut |
| 60.0 | himself and | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.19/0.28 |  |
| 60.5 | not | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.18/0.26 | onset candidate |
| 61.0 | to you as | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.13/0.17 |  |
| 61.5 | the viewer, | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.17/0.20 |  |
| 62.0 | and he also doesn't | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.16/0.22 |  |
| 62.5 | set any | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.14/0.17 |  |
| 63.0 | expectations | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.13/0.20 | onset candidate |
| 63.5 | that | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.12/0.17 |  |
| 64.0 | you will receive | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.13/0.14 |  |
| 64.5 | any | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.14/0.18 |  |
| 65.0 | value. | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.14/0.18 |  |
| 65.5 |  | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.13/0.21 |  |
| 66.0 | So we change | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.15/0.23 | onset candidate |
| 66.5 | it too. | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.14/0.19 |  |
| 67.0 |  | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.14/0.20 | onset candidate; SCENE CUT (gt0.35) |
| 67.5 | I took a business | Verbal-hook diagnosis A-roll; the subject's hook line is REPLAYED (~63s) as audio evidence | phrase chunks; subject line captioned as quote | 0.16/0.20 |  |
| 68.0 | from this | FIXED FRAME v2 full-screen: subject with BOTH HANDS POINTING UP at dark badges '$194.6K → $567.1K +120.9%' — t… | badges are the text | 0.14/0.21 | SEGMENT IN: hard cut |
| 68.5 | to | FIXED FRAME v2 full-screen: subject with BOTH HANDS POINTING UP at dark badges '$194.6K → $567.1K +120.9%' — t… | badges are the text | 0.11/0.23 |  |
| 69.0 | this, | FIXED FRAME v2 full-screen: subject with BOTH HANDS POINTING UP at dark badges '$194.6K → $567.1K +120.9%' — t… | badges are the text | 0.15/0.22 | onset candidate |
| 69.5 | and if | FIXED FRAME v2 full-screen: subject with BOTH HANDS POINTING UP at dark badges '$194.6K → $567.1K +120.9%' — t… | badges are the text | 0.11/0.18 | onset candidate |
| 70.0 | you wanna do | FIXED FRAME v2 full-screen: subject with BOTH HANDS POINTING UP at dark badges '$194.6K → $567.1K +120.9%' — t… | badges are the text | 0.19/0.26 |  |
| 70.5 | the same, | FIXED FRAME v2 full-screen: subject with BOTH HANDS POINTING UP at dark badges '$194.6K → $567.1K +120.9%' — t… | badges are the text | 0.13/0.13 |  |
| 71.0 | here's five | FIXED FRAME v2 full-screen: subject with BOTH HANDS POINTING UP at dark badges '$194.6K → $567.1K +120.9%' — t… | badges are the text | 0.13/0.18 |  |
| 71.5 | things that | FIXED FRAME v2 full-screen: subject with BOTH HANDS POINTING UP at dark badges '$194.6K → $567.1K +120.9%' — t… | badges are the text | 0.16/0.28 | onset candidate |
| 72.0 | you need | CLOSE: warm brick room; Devin with phone in one hand; subject's image as a floating card beside him; 'BUT THIS… | 'BUT THIS' chunk | 0.15/0.18 | SEGMENT IN: hard cut; file ends mid-line, no end card |
| 72.5 | to fix. | CLOSE: warm brick room; Devin with phone in one hand; subject's image as a floating card beside him; 'BUT THIS… | 'BUT THIS' chunk | 0.11/0.14 |  |
| 73.0 | Now that's | CLOSE: warm brick room; Devin with phone in one hand; subject's image as a floating card beside him; 'BUT THIS… | 'BUT THIS' chunk | 0.11/0.21 | onset candidate |
| 73.5 |  | CLOSE: warm brick room; Devin with phone in one hand; subject's image as a floating card beside him; 'BUT THIS… | 'BUT THIS' chunk | 0.16/0.26 |  |
| 74.0 | a viral video, | CLOSE: warm brick room; Devin with phone in one hand; subject's image as a floating card beside him; 'BUT THIS… | 'BUT THIS' chunk | 0.15/0.22 |  |
| 74.5 |  | CLOSE: warm brick room; Devin with phone in one hand; subject's image as a floating card beside him; 'BUT THIS… | 'BUT THIS' chunk | 0.15/0.19 |  |
| 75.0 | but this... | CLOSE: warm brick room; Devin with phone in one hand; subject's image as a floating card beside him; 'BUT THIS… | 'BUT THIS' chunk | 0.21/0.28 |  |
| 75.5 |  | CLOSE: warm brick room; Devin with phone in one hand; subject's image as a floating card beside him; 'BUT THIS… | 'BUT THIS' chunk | 0.12/0.19 |  |
| 76.0 |  | CLOSE: warm brick room; Devin with phone in one hand; subject's image as a floating card beside him; 'BUT THIS… | 'BUT THIS' chunk | 0.07/0.07 |  |

Companion evidence: `BREAKDOWN-DfV6GWMyqs0--library-decode.md` (where present), `analysis/DfV6GWMyqs0_analysis.json` (full RMS series, cut list, onsets).

## BACKGROUND LOG (keying / placement / behind-vs-over) — added Nov 13 pass
- No keying of Devin. Backgrounds are practical (dark studio; warm brick room at the close) or the frame is REPLACED by the subject's footage (annotated frame, fixed frames).
- The subject's image as a FLOATING CARD beside Devin (~74–76s) is graphics-over-footage in empty space beside him — the only composited-person treatment, and the person composited is the subject, not Devin.
- The phone is a practical prop: the subject's video plays INSIDE the physical phone screen (PiP-by-prop), not a keyed insert.

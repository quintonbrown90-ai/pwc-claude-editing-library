# NOTES — DfTawo5jHMH (59.7s, "The 4 Questions Filter" — content strategy quiz)
## Structure
- Sky at desk, dark room, black hoodie. One continuous animated diagram system above him; the "4 Questions Filter" checklist recurs and fills in as each question is explained.
- Captions: white sans center ~y560-620, 1-3 words, on the word beat.

## Devices
1. QUIZ PANEL (~0.2-3.8s): glass panel top-center (~x330-720, y30-220): green "Quiz" title, question "What is a content strategy", 3 answer rows appearing one at a time: "A posting schedule" ~0.5s, "A list of ideas" ~0.8s, "A filter" ~1.0s. Verdict animation ~1.8-2.2s: red X on rows 1-2, green "?" on row 3. Panel fades ~3.8s.
2. DOCUMENT STACK (~3.8-9.5s): 4 dark document cards top (~x400-980, y40-180), green title "Content Strategy" above. Cards fill green one at a time: card 1 ~5.2s, card 2 ~5.5s; cards 3-4 turn RED with "Do not post" labels ~8.2-8.8s; card 1 gets "Post" label. Green = post, red = do not post. Cards fly off upward ~9.5s.
3. FUNNEL DIAGRAM (~9.5-14.5s): gray funnel center-top (~x480-620, y280-380), "Filter" green above, "Strategy" right with dashed arc. Format labels fly INTO the funnel one at a time: "Duet" ~11.5s, "Quiz" ~11.8s, "Tutorial" ~12.0s... green dot drops out of funnel bottom ~12.5s; labels rearrange to orbit the funnel with red/green dots. Fades ~14.5s.
4. "THE 4 QUESTIONS FILTER" PANEL (~15.8s onward, recurring): green title top-right (~x600-980, y40-80) + 4 blurred rows that sharpen one at a time. Rows [exact text from later frames]: "1. Did a favourite client say it", "2. Does it build trust?", "3. Does it fit my brand", "4. Does it help my goal". Each row fills green when its question is explained: Q1 ~21.0s, Q2 ~30.5s, Q3 ~37.2s, Q4 ~44.5s.
5. PHONE MOCKUP (~17.2-19.5s): iPhone slides in from top-right (~x620-900, y200-450) showing an IG profile with "100,000" followers; drops down with a small bounce, flies off top ~19.5s. Tied to "end up with 100,000 followers that never buy".
6. QUESTION 1 PANEL (~20.5-22.5s): green "Question 1" title + 4 rows; row 1 fills green ~21.0s. Small VIDEO-CALL WINDOW appears top-right ~22.0s (two people on a call, red record dot) — the "client call" evidence clip.
7. HEAD CONSTELLATION (~22.5-29.8s): green title "Attract more of them" top; 5 small head cutouts in a row (~x380-700, y130-180) labeled "Customers" below the outer ones. CENTER head gets green glow ring + crown emoji ~23.5s on "your favorite customers". Title changes to "Not These Problems" ~26.0s. Heads split into TWO groups ~27.5-29.0s: left in GREEN striped box "least favorite", right in RED striped box "least profitable" — boxes slide apart.
8. CONTENT SCRIPT PANEL (~31.5-34.5s): document with horizontal lines (script) top-center; labels "Proof" + "Stories" (yellow-green) pop in at left ~32.2s; a green line highlights one row ~33.5s.
9. LEGITIMACY METER (~34.5-37.0s): green title "Legitimacy" + horizontal progress bar filling with green dots ~34.8-35.5s + formula text "Proof = +1 Legitimacy" below. Bar fills on "proof... legitimacy".
10. PERSONALITY TRAIT STRIP (~37.5-43.5s): 5 small video thumbnails in a row top (~x150-950, y40-130) with labels below: "Relatable", "Advice", "Authoritative", "Nice", "Helpful" — appear one at a time ~37.5-38.5s; green connector lines draw down to a "You" label ~39.0s. Thumbnails highlight as he names each trait ~41.0-43.0s. Strip flies off upward ~43.5s.
11. PICK ONE GOAL (~45.0-46.0s): green title "Pick One Goal" top-center + 3 pills below: "Hiring", "Leads", "Impact" — appear ~45.2s.
12. MATCH YOUR WORDING (~50.8-56.5s): green title top-center + rounded panel; green card "HIRING — they like you, your leadership" slides in left ~51.5s; second green card "BUYERS — you apply frameworks" slides in right ~53.2s. HIRING card dims (dark) ~56.0s as he pivots to buyers.
13. CONTENT FILTER RECAP (~56.5-58.5s): green title "The Content Filter" + 4-row checklist (rows 1-3 green-filled, row 4 dim). Ends on Sky "...a filter to what you post" ~59.5s. No end card visible [UNVERIFIED final 0.2s].

## Sound (measured, Batch 36)

Bed: ABSENT (measured). SFX: 0 confirmed; every graphic landing silent. Transitions: no camera cuts to carry sound (see Transitions section). Silence: none (0 hits @−35/−50 dB); gaps are breath/room tone only. One unconfirmed 5.93 kHz sharpness hit (7.75s) is logged in the soundmap — below the confirmation bar.

Full measured soundmap: `claude-editing/research/video-harvest/instagram/batch-36-sky-completion/soundmaps/SOUNDMAP_DfTawo5jHMH.md` (mean -17.2 dB, max -0.9 dB, voice median RMS -19.4 dBFS; method: volumedetect/astats, silencedetect −35/−50 dB, full spectrogram read, STFT tone scan + tonal-sharpness/zoom adjudication, word-gap RMS, transient census, scene-cut cross-check).

## Transitions (Batch 36)

Method: ffmpeg scene-cut detection `select='gt(scene,0.35)'` plus a 0.2-threshold pass for soft cuts (1 cut(s) at 0.35, 6 at 0.2), each classified against the existing 4 fps frames in `claude-editing/examples/sky/motion-teardown/frames/DfTawo5jHMH/` (sharpness/saturation/brightness/diff profile) and the device prose above. All cuts are silent (see Sound section).

- **18.35s [0.2 pass]** — Graphic-state change — phone mockup entry (device 5, ~17.2s; single-frame diff 33.9). Not a camera cut.
- **19.32s [0.2 pass]** — Graphic-state change — phone mockup exit (flies off ~19.5s).
- **46.08s [0.2 pass]** — Graphic-state change — 'Pick One Goal' section build (~45.0–46.0s).
- **49.98s [0.2 pass]** — Graphic-state change at the 'Match Your Wording' build (~50.8s).
- **57.52s [0.2 pass]** — Graphic-state change — content-filter recap panel (~56.5s).
- **59.49s [0.35]** — End-of-reel cut — the final 0.2s: brightness collapses 47.8→23.8 on the last sampled step; the reel's end/loop point, not a mid-reel transition.

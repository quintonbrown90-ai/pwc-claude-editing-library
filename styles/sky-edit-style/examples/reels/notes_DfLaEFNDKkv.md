# NOTES — DfLaEFNDKkv (93.9s, "Power Words" — unskippable hooks)
## Structure
- Sky at desk, dark room, black shirt. Opens with title + IG phone mockup; then a rapid movie-still flashcard montage; then a LONG split-screen "Rewriting hooks" section (screen recording on top, Sky narrating below) that runs ~17.5s to the end.
- Captions: white sans center ~y560-620, 1-3 words, on the word beat.

## Devices
1. "WAY TOO GOOD" TITLE (~0.2-2.0s): white "This sounds" + big green "WAY TOO GOOD" + white "to be true" center-lower (~x300-700, y500-660). Words stagger in: "This sounds" ~0.2s, "WAY TOO" ~0.5s, "GOOD" ~0.8s, "to be true" ~1.0s. Fades ~2.0s.
2. IG REELS PHONE MOCKUP + COLOR ISOLATION (~2.2-5.5s): full IG Reels phone UI slides in from right (~x450-950, y40-480): Sky's own reel playing with "unskippable" overlay, heart/comment/share rail right, "realskytan" + Follow button, caption + comment bar. ~3.0s the background behind the phone goes BLACK AND WHITE while the phone stays in color (color-isolation effect). ~4.0s "POWER" green text on the phone screen, ~4.5s "POWER WORDS". Phone slides out right ~5.2s; color returns ~5.5s.
3. "POWER WORDS" TITLE + SUBLABELS (~5.5-7.0s): big green "POWER WORDS" center (~x400-650, y520-660) + small white "Adjectives" right ~5.8s; "Terms" label pops left ~6.5s, "Phrases" right ~6.8s.
4. MOVIE-STILL FLASHCARD MONTAGE (~7.0-14.0s): frame goes BLACK; small rounded-rect movie stills flash one at a time center (~x100-500, y100-350), each ~1s, word label in white over it, slight Ken Burns scale-in: "Powerful / Visual" (Iron Man, ~7.0s), "Visceral" (bald man flexing, ~7.5s), "Addicting" (Bradley Cooper close-up, ~9.5s), "Cancerous" (Morpheus, ~10.5s), "Money Printing" (Wolf of Wall Street, ~11.0s), "Soul Sucking" (whale/dark, ~11.5s), "Luck Magnet" (Harry Potter, ~12.0s), "Moonshot" (rocket launch, ~13.0s).
5. "MORE EFFECTIVE" TEXT + HOOK/BODY/CTA BAR (~15.5-17.5s): "how easy" white + "More effective" green + "your hooks become" white center-lower; below, a 3-segment bar "Hook" | "Body" | "CTA" filling green left-to-right ~16.0-17.0s.
6. SPLIT-SCREEN SCREEN RECORDING (~17.5-93.9s): frame splits horizontally — TOP half = screen recording (Claude chat, dark UI); BOTTOM half = Sky side-profile narrating, looking at the screen. "Rewriting hooks" title appears top ~22.5s with a numbered list of 5 hooks below (~23.0s) filling in line by line. The list's hook lines HIGHLIGHT GREEN one at a time as he reads them: hook #1 ~29.5s, #2 ~37.5s, #3 ~47.0s, #4 ~62.5s, #5 ~75.0s [approx — exact times UNVERIFIED].
7. WORD-SWAP HIGHLIGHT (~75.0s): in hook #5 the word "draining" is highlighted ORANGE — a word-replacement edit ("draining" -> "destroying"); the swap word glows orange in the list.
8. THANOS SNAP STILL (~42.0-43.0s): small still of Thanos snapping (Avengers Endgame) pops top-right of the bottom half (~x700-950, y500-620) on "We've all watched endgame... the snap".
9. PIP REACTION / B-ROLL CLIPS (~55.0-60s): bottom half splits again — a vertical video of two Italian guys reacting (one facepalming) docks right (~x700-950, y500-750) while Sky talks at left; a cooking video (pasta pan) replaces it ~56.5s.
10. ENDING: split-screen persists to the end; Sky closes "...that was helpful" ~93.5s; no end card.

## Sound (measured, Batch 36)

Bed: ABSENT (measured). SFX: 0 confirmed (the 41.56s/66.32s flags are refuted sibilance). The split-screen's screen recording and the PiP inserts contribute no measurable audio; the long narration pauses (2.51s max) bottom out at room tone −37.6 dBFS. Transitions: montage cuts + the split-screen entry cut all silent. Silence: none at −35 dB despite the pauses — room tone throughout.

Full measured soundmap: `claude-editing/research/video-harvest/instagram/batch-36-sky-completion/soundmaps/SOUNDMAP_DfLaEFNDKkv.md` (mean -17.6 dB, max -0.9 dB, voice median RMS -19.6 dBFS; method: volumedetect/astats, silencedetect −35/−50 dB, full spectrogram read, STFT tone scan + tonal-sharpness/zoom adjudication, word-gap RMS, transient census, scene-cut cross-check).

## Transitions (Batch 36)

Method: ffmpeg scene-cut detection `select='gt(scene,0.35)'` plus a 0.2-threshold pass for soft cuts (5 cut(s) at 0.35, 7 at 0.2), each classified against the existing 4 fps frames in `claude-editing/examples/sky/motion-teardown/frames/DfLaEFNDKkv/` (sharpness/saturation/brightness/diff profile) and the device prose above. All cuts are silent (see Sound section).

- **3.90s [0.2 pass]** — Effect boundary — the B&W color-isolation beat behind the phone (device 2, ~3.0s); a grade effect on a continuous shot, not a cut.
- **5.47s [0.35]** — Hard cut — phone exit into the black flashcard montage (device 4; brightness 66.5→27.5).
- **8.34s [0.35]** — Hard cut — flashcard swap (movie stills cut ~1/s; single-frame diff 59.7).
- **9.04s [0.35]** — Hard cut — flashcard swap (diff 54.9).
- **12.15s [0.2 pass]** — Hard cut — flashcard swap (sub-0.35 spike; diff 34.3).
- **13.01s [0.35]** — Hard cut — flashcard swap / montage exit beat (diff 58.5).
- **17.38s [0.35]** — Hard cut — into the split-screen layout (device 6, ~17.5s; brightness 64.5→28.9). After this cut there are no further detector cuts: the remaining ~76s are one split-screen take (the Thanos still and PiP inserts are small-region overlays below the scene threshold).

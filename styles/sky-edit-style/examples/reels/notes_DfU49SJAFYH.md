# NOTES — DfU49SJAFYH (103.8s, breakdown of TCM practitioner 1.1M-view video)
## Structure
- Sky at desk (dark room, desk, monitor right) <-> subject clip (bright gray bg, TCM practitioner) hard-cutting back and forth.
- Captions: white sans, center, ~y560-600/1000, 1-3 words per change, on the word beat. Same style over Sky AND subject clips.
- Transitions: mostly hard cuts; occasional motion-blur/whip frame at cut (~12.0s, ~31.8s) — a ~0.25s blur smeared frame, looks like a fast zoom/whip pan.

## Devices seen 0-60s
1. FLOATING MINI VIDEO CARD (subject PiP): top-center, ~x560-680, y0-180 (1080x1920 px: x~600-735, y~0-195). Rounded-rect, dashed white border, "1.1M" green label above. Slides DOWN from top ~0.8s, holds. Entry ~0.75-1.0s, ease-out. Tied to "got 1.1 million views".
2. RETENTION GRAPH PANEL: slides in from RIGHT at ~2.8s, lands top-right ~x690-980, y130-280; then moves to top-CENTER ~x30-480, y60-200 and persists as analysis HUD for the whole reel. Green glass panel, white grid, neon-green line, axes 0:00-1:01, "34%" end label, animated dot travels the line. Left region shades green as playhead advances. A white pill label sits ABOVE the panel and UPDATES per beat: "Throat mucus" -> "Broader term / smaller struggles" (~15s) -> "Intentional drop" (~23.8s) -> "Hook filtering ✓" (~27.5s) -> "Bad drop" (~42.5s) -> "Basically flat ✓" (~57s) -> "Spleen -> Fluids" (~59.5s). A RED segment marks the bad-drop zone (~56s). Label change = hard swap (new pill pops in).
3. SUBJECT FULL-SCREEN CUT: hard cut at ~3.8s to subject clip full-frame with its own baked hook text top ("DO YOU HAVE CONSTANT MUCUS IN YOUR THROAT? / TCM Practitioner explains:"). Back to Sky ~12.0s (blur frame), ~31.8s, ~49.0s, ~55.0s.
4. PHOTO POP-UP (phlegm): center chest ~x420-580, y430-520, hard pop-in ~7.8s on "the phlegm", holds ~2s, hard out ~9.8s.
5. PHOTO POP-UP (spleen diagram): same position, pops ~33.5s on "the Spleen", holds through ~41.5s (persists across subject's lines about spleen/organ/blood cells).
6. CHART LABEL MORPH: at ~59.5s the chart panel's label area becomes a flow diagram: white pill "Spleen" -> arrow -> pill "Fluids" appearing left-to-right as he says "spleen... fluids". The chart line fades to background.
7. ZOOM: Sky's framing slowly pushes in during long talking stretches (subtle, ~5% over 10s). [UNVERIFIED exact rate]

## Devices seen 60-104s
8. FLOW-DIAGRAM BUILD (chart morph): ~59.5-61.5s the chart panel's content becomes 4 pills: "Spleen" -> "Fluids" (top row, arrow right), "Phlegm" <- "Dampness" (bottom row, arrow left). Nodes pop in one at a time on the spoken word (~60.0 Fluids, ~60.5 Dampness, ~61.2 Phlegm). Label above: "Every line connects" ~61.8s + sub "No aggressive switches" ~63.0s. Whole diagram fades out ~65.8s (0.5s opacity ramp).
9. PHOTO POP-UP (tongue): ~67.5s center chest on "your tongue / scalloping and tooth marks", hard in, holds ~2s, out ~69.2s.
10. HUD LABEL CASCADE (stacking annotation): white pill above chart accumulates lines, each popping in under the previous on the spoken beat: "QUICK TIP" ~69.2s -> "INTERACTIVE EXERCISES" ~71.2s -> "Let's do a meditation" ~73.5s -> "I bet I can hypnotize you" ~75.5s -> "People stay to participate ✓" ~77.0s. Later the stack resets and rebuilds: "Stay to the end" ~90.2s -> "Explain dampness / Give action items" ~92.2-93.0s -> "Why herbs" ~94.5s -> "More visual / Easier and faster fixes" ~98.5-100.5s. Pill grows vertically; max 3 lines, then resets.
11. ENDING: no end card / CTA visible; ends on Sky "So yeah, that's the analysis" ~102.5-103.8s, chart still up top fading. [UNVERIFIED last 0.5s]
12. CHART PLAYHEAD SHADING: green-shaded region under the line grows left-to-right across the whole reel as the "playhead" advances; a red segment marks the "bad drop" zone (~56s onward).

## Sound (measured, Batch 36)

Bed: ABSENT (measured). SFX: 0 confirmed — the one broadband flag (48.58–49.27s) is refuted: it is the sibilance of the return line 'It's the system…'. Two voices (Sky + TCM subject exhibit audio in the full-screen sections), both dry. Transitions: all cuts silent. Silence: none (0 hits @−35/−50 dB).

Full measured soundmap: `claude-editing/research/video-harvest/instagram/batch-36-sky-completion/soundmaps/SOUNDMAP_DfU49SJAFYH.md` (mean -16.4 dB, max -0.7 dB, voice median RMS -18.0 dBFS; method: volumedetect/astats, silencedetect −35/−50 dB, full spectrogram read, STFT tone scan + tonal-sharpness/zoom adjudication, word-gap RMS, transient census, scene-cut cross-check).

## Transitions (Batch 36)

Method: ffmpeg scene-cut detection `select='gt(scene,0.35)'` plus a 0.2-threshold pass for soft cuts (10 cut(s) at 0.35, 16 at 0.2), each classified against the existing 4 fps frames in `claude-editing/examples/sky/motion-teardown/frames/DfU49SJAFYH/` (sharpness/saturation/brightness/diff profile) and the device prose above. All cuts are silent (see Sound section).

- **3.63s [0.35]** — Hard cut — Sky → subject full-screen (device 3, ~3.8s). Brightness 49→139, saturation 0.34→0.12: the subject's bright gray set.
- **11.87s [0.35]** — Hard cut — subject → Sky return (~12.0s), with a ~0.25s motion-blur/whip frame per device 3; frame diffs smear across two sampled frames (67.2/45.4), consistent with the blur frame.
- **31.77s [0.35]** — Hard cut (0.806) at a prose-named subject-section boundary (~31.8s). Both sampled sides are bright subject framing, so the direction (in/out) is undetermined from the frames alone.
- **40.53s [0.35]** — Hard cut (0.734) on the Sky side (dark framing both sides) — jump cut or HUD state change; the prose names no cut here, so the type is undetermined beyond 'Sky-side edit point'.
- **48.43s [0.35]** — Hard cut (0.721) at the ~49.0s subject-section boundary; both sampled sides bright subject framing — direction undetermined from frames.
- **54.97s [0.35]** — Hard cut (0.722) at the ~55.0s subject-section boundary; Sky-side dark framing on the sampled frames.
- **66.00s [0.35]** — Hard cut (0.801) inside the subject footage (bright subject framing both sides); not named in the prose — an edit point in the source clip or an unlisted boundary; content undetermined from frames.
- **69.13s [0.35]** — Hard cut (0.690) on the Sky side at the tongue pop-out / HUD cascade beat (~69.2s) — jump cut or graphic-state change.
- **81.20s [0.35]** — Hard cut (0.797) inside the subject footage (bright both sides); not named in the prose.
- **85.07s [0.2 pass]** — Soft spike (0.318) inside the subject footage — sub-threshold edit point or subject motion.
- **89.73s [0.35]** — Hard cut (0.720) on the Sky side at the HUD cascade reset beat (~90.2s).

# NOTES — DfSf5v8j73o (56.7s, "Drop-offs you actually want" — retention deep-dive, same TCM video as DfU49)
## Structure
- Sky at desk, dark room, black tee. Retention graph is the recurring HUD; script-lines diagram; subject full-screen cut in the middle.
- Captions: white sans center ~y560-620, 1-3 words, on the word beat.

## Devices
1. RETENTION GRAPH DRAW (~1.2-3.5s): empty glass panel top-left (~x30-480, y60-200); green line DRAWS left-to-right with a glowing dot at the leading edge (~1.5-2.8s); axes + "34%" endpoint appear. Pill "Drop-off" top-left of panel ~2.2s.
2. BIG TITLE BUILD (~2.0-3.5s): "Drop" green -> "Drop-offs" big green center (~x300-700, y480-620), "retention" small white above, "you actually want" white below. Words stagger in: "Drop" ~2.0s, "Drop-offs" ~2.2s, "retention" ~2.5s, "you actually want" ~2.8s. Fades ~3.5s.
3. FLAT-LINE MORPH (~3.8-7.2s): graph line morphs to FLAT (horizontal ~85%) with area under it filling solid green left-to-right (~4.5-6.0s). Pill "Everyone" above the line ~7.0s.
4. MINI VIDEO CARD + POINTING (~9.5-11.5s): TCM card (dashed border, "1.3M") drops in from top-center (~x480-620, y0-180) exactly as Sky points UP at it (~9.8s) — the card appears where he points. He keeps pointing at it through ~11.5s.
5. GRAPH SLIDE-IN + LABEL STACK (~11.0-15.5s): retention graph slides in from right, docking next to the card (~x480-980, y60-200). Labels above: "0:03 to 0:05" + "Steep drop-off" ~12.5s, "Lead filtering" green pill ~14.5s.
6. SCRIPT LINES DIAGRAM (~16.0-26.0s): glass panel top-left (~x30-480, y60-260) with horizontal lines: white "Hook" line, RED "Lead" lines (bracketed, 2 red lines), GREEN line, white lines. Lines draw in one at a time ~16.0-17.5s. ~18.0s the red "Lead" lines PULSE/glow red on "your script... Line one". ~22.0s small head cutouts appear at the panel's right edge (~x900-980, y60-120) — a row of tiny audience heads growing to ~6 by ~24.0s, drifting right and fading ~25.5s.
7. GRAPH WITH HEADS ON THE CURVE (~26.5-29.8s): retention graph slides back in top-left with "0:03 to 0:05 / Steep drop-off / Lead filtering" labels; 3 small head cutouts sit ON the graph's curve (~x350-500, y200-260) ~27.0s.
8. "LEAD FILTER" TITLE TYPE-IN (~30.5-31.2s): big green "Lead filter" types in center on "what was the Lead filter".
9. SUBJECT FULL-SCREEN CUT (~31.2-38.8s): TCM clip full frame; phlegm photo pop ~36.5-38.5s (center chest).
10. HOOK TEXT REVEAL (~38.8-44.5s): top-left text block builds line by line as Sky narrates: "Here's why you constantly have throat mucus" (white + green "throat mucus") ~38.8s; bullets "• Tons of people have throat mucus" ~39.5s, "• Not many people talk about it" ~40.5s; second block "and why your doctor can't figure it out, because the phlegm that they see is the symptom, not the cause. It's coming from your gut" ~41.0-42.0s; green sub-bullets "• Lead calling out doctor" ~42.0s, "• Phlegm being the symptom not the cause" ~43.0s. Transcript-reveal device.
11. LEAD FILTERING CHECKLIST (~44.5-48.0s): dark glass panel top-left (~x30-480, y60-260): title "Lead filtering" + checkbox rows ticking green one at a time: "Tried a bunch of fixes" ~45.0s (checked ~45.5s), "Gone to the doctor" ~46.0s (checked ~46.5s), "Gone nowhere" ~47.0s (checked ~47.5s).
12. CLEAR ANSWER + HEAD (~47.5-49.0s): green title "Clear Answer" top-right; checklist panel slides right; head cutout (TCM practitioner) with green ring at right (~x850-980, y200-300) connected by a dashed line to the panel.
13. GRAPH RETURN + END TITLE (~49.5-56.7s): retention graph top-center with labels; "Sold off" pill at graph's right end ~55.0s; final big text "WARM & SOLD" center (~x300-700, y560-620) types in ~55.8-56.5s ("WARM" white + "& SOLD" green). Ends on it.

## Sound (measured, Batch 36)

Bed: ABSENT (measured). SFX: 0 confirmed. Exhibit audio: the TCM subject's own voice in the 31.2–38.8s full-screen section (its HF ceiling ~15.5 kHz vs Sky's ~18 kHz marks both cuts). Transitions: both hard cuts silent, including the blurred return cut. Silence: none (0 hits @−35/−50 dB).

Full measured soundmap: `claude-editing/research/video-harvest/instagram/batch-36-sky-completion/soundmaps/SOUNDMAP_DfSf5v8j73o.md` (mean -16.8 dB, max -0.9 dB, voice median RMS -18.5 dBFS; method: volumedetect/astats, silencedetect −35/−50 dB, full spectrogram read, STFT tone scan + tonal-sharpness/zoom adjudication, word-gap RMS, transient census, scene-cut cross-check).

## Transitions (Batch 36)

Method: ffmpeg scene-cut detection `select='gt(scene,0.35)'` plus a 0.2-threshold pass for soft cuts (2 cut(s) at 0.35, 4 at 0.2), each classified against the existing 4 fps frames in `claude-editing/examples/sky/motion-teardown/frames/DfSf5v8j73o/` (sharpness/saturation/brightness/diff profile) and the device prose above. All cuts are silent (see Sound section).

- **7.63s [0.2 pass]** — Graphic-state change — flat-line morph / 'Everyone' pill beat (~7.0s). Not a camera cut.
- **9.33s [0.2 pass]** — Graphic-state change — mini video card drop + graph slide-in (~9.5–11.0s).
- **31.37s [0.35]** — Hard cut — Sky → subject full-screen (device 9, ~31.2s; detector 0.956, brightness 68.7→139.8, saturation 0.40→0.11).
- **38.43s [0.35]** — Hard cut — subject → Sky return (~38.8s; detector 1.000). The sampled boundary frame is blurred (sharpness 0.46× the window median) — a blur/whip frame rides this cut.

# NOTES — DfX2qwQGagM (53.9s, "Good Content Strategy" / Leila Hormozi content filter)
## Structure
- Sky at desk, dark room, black shirt. One continuous "animated system diagram" builds above/behind him the whole reel. No subject full-screen cuts except one B-roll cutaway at the end.
- Captions: white sans center-lower ~y560-620, 1-3 words, on the word beat.

## Devices
1. OPENING TITLE + FUNNEL (0-3.5s): big green "Good Content Strategy" lower-left (~x30-350, y560-660) + small white "sign of a" above-right. Green funnel icon top-center (~x430-580, y60-130) labeled "STRATEGY". White pill shapes (ideas) RAIN down from top into the funnel ~0.8-2.8s, staggered. ~3.0s ONE green pill drops out of the funnel bottom and lands as a green bar below it ~3.2s ("the filter keeps 1 idea"). Funnel + title fade out ~4.5-6.0s.
2. BLUR/WHIP TRANSITION (~6.5-7.0s): motion-blurred frames — fast zoom/whip into next beat.
3. IG PROFILE CARD BUILD (~7.0-9.5s): glassmorphic card top area (~x30-980, y40-260). Stages: blurred empty glass card ~7.0s -> avatar pops ~8.8s (Leila) -> name/handle/counts/bio lines fill ~9.0s -> green "Follow" + gray "Message" buttons ~9.0s. Card = @leilahormozi, 3.8M followers.
4. TRAIT CHIPS (pop-in sequence, ~9.8-11.5s): dark chip "Avatar" + subtext slides in bottom-right of card ~9.8s; then green-check chips pop one at a time under the card, left-aligned: "Extremely empathetic" ~10.8s, "Great people skills" ~11.0s, "Elite operator" ~11.2s, "Great leader" ~11.5s.
5. CONTENT FILTER PANEL (~11.8s onward): glass panel top-right (~x700-980, y40-200) titled "LEILA CONTENT FILTER". Dashed connector lines DRAW down from the 4 trait chips to the panel. Rows type in word-by-word and get verdicts: "Top 5 marketing paid ads" ~13.8-14.5s + red X ~14.8s; "Retaining A plus talent" ~19.5-20.5s + green check ~20.5s; "Reaction videos" ~23.0s + red X ~23.5s; "Day in the life" ~26.5-27.5s + green check ~27.5s; "Rankings videos" ~33.5s + green check; "Demonstrations" ~39.5s + green check. "Minimum" tag at right ~34.5s.
6. CURRENT-IDEA THUMBNAIL CARD: dashed-border card left of the filter panel (~x40-200, y40-200). Its image SWAPS on each new idea beat: Leila purple bg ~13.5s, Alex suit ~22.5s, woman at laptop ~26.0s, woman red top ~28.5s, Leila pink ~29.8s, bearded man ~33.0s, Leila white dress ~39.2s.
7. AUTHORITY BARS (~23.2s): two horizontal bars under the filter: "Leila's authority" (long green) vs "His authority" (short green), tiny avatars left. Fill animation ~0.5s. Leila bar ~2x His bar.
8. LITTLE HEAD + MARKER (~22.5s): small circular head cutout (Leila) appears top-left of authority area (~x380-430, y300-340) with a green triangle marker above it. Stays while bars show.
9. CHIP ORBIT (~30.5-32.0s): chips pop around the thumbnail card as satellites on the spoken trait: "Great boss" above-left ~30.5s, "Leader" bottom-right ~31.5s, "Excellent operator" left ~32.0s.
10. PLAY BUTTONS + TRUST BAR (~35.0-35.5s): two green play squares under the filter panel; "Audience trust" horizontal progress bar with Leila avatar fills below.
11. FILTER PANEL EXIT + CARD SOLO (~41.5-44.0s): panel fades/slides out; thumbnail card remains, shrinks to small vertical center-top. Label appears above: "SHOW HER IN HER ELEMENT" (white SHOW HER + green IN HER ELEMENT) ~44.0s.
12. TAG CHIPS LIGHT-UP (~45.0-46.2s): small chips under the card: "decisions" ~45.2s, "moving" ~45.8s, "her team" ~46.2s — each lights green on its spoken word.
13. STILL -> PLAYING VIDEO (~45.5s): thumbnail card widens to 16:9 and PLAYS footage (Leila walking, then team meeting). Shrinks back to vertical ~47.2s. Small "boring" tag + head cutout with green arrow at right ~47.5s.
14. STAIRCASE CHART (~49.0-52.0s): card dissolves into glass panel "BORING TO YOU, GOLD TO THEM" (white + green text top). White staircase line DRAWS itself left-to-right ~49.5-50.5s; small head cutout at top step; green pill "super informative" at bottom step. Green dots pulse along the staircase ~51.0-52.0s on "super informative to everyone else".
15. B-ROLL CUTAWAY (~52.2-52.8s): hard cut to full-screen tennis B-roll (athlete serving) with big green "GREAT ATHLETE PRACTICE" center-left. Back to Sky ~52.8s. Ends "...just an art to it". No end card visible [UNVERIFIED final 0.3s].

## Sound (measured, Batch 36)

Bed: ABSENT (measured). No whooshes/pops/impacts. BUT not literally voice-only: 3 faint gated tone events ride ~15–35 dB under the voice at animation beats — a ≈9.15 kHz gated tone at the funnel-rain opening (0.6–1.2s) and a sustained ≈11.1+11.85 kHz two-tone at the 'Minimum'/trust-bar beat (34.41–34.86s) and the 'SHOW HER IN HER ELEMENT' label (43.98–44.40s), all zoom-verified. Silence: none (0 hits @−35/−50 dB); room tone to the last frame.

Full measured soundmap: `claude-editing/research/video-harvest/instagram/batch-36-sky-completion/soundmaps/SOUNDMAP_DfX2qwQGagM.md` (mean -16.4 dB, max -1.0 dB, voice median RMS -17.6 dBFS; method: volumedetect/astats, silencedetect −35/−50 dB, full spectrogram read, STFT tone scan + tonal-sharpness/zoom adjudication, word-gap RMS, transient census, scene-cut cross-check).

## Transitions (Batch 36)

Method: ffmpeg scene-cut detection `select='gt(scene,0.35)'` plus a 0.2-threshold pass for soft cuts (3 cut(s) at 0.35, 7 at 0.2), each classified against the existing 4 fps frames in `claude-editing/examples/sky/motion-teardown/frames/DfX2qwQGagM/` (sharpness/saturation/brightness/diff profile) and the device prose above. All cuts are silent (see Sound section).

- **4.63s [0.2 pass]** — Graphic-state change — opening funnel + title exit (device 1: funnel/title fade out ~4.5–6.0s). Not a camera cut.
- **6.37s [0.2 pass]** — Whip/blur transition (device 2, ~6.5–7.0s) — the smeared frames produce a 2-frame diff elevation (43.4/38.7) at the 0.2 threshold; no single blurred frame is isolated at 4 fps sampling, so the blur character rests on the device prose's frame read.
- **36.00s [0.2 pass]** — Graphic-state change — play buttons + 'Audience trust' bar build (~35.0–35.5s).
- **39.37s [0.35]** — Detector cut (score 0.489) at the 'Demonstrations' verdict beat (~39.5s). Frame diffs rise over ~0.75s instead of jumping in one frame — a graphic-state change (filter-panel verdict row) with framing drift, not a clean scene cut; exact mechanic undetermined beyond that.
- **51.00s [0.35]** — Detector cut (0.591) at the staircase-chart completion beat (green dots pulse ~51.0–52.0s) — graphic-state change on the same take.
- **52.73s [0.35]** — Hard cut — B-roll boundary: the tennis cutaway (device 15, ~52.2–52.8s; detector timebase reads the boundary at 52.73s; brightness jumps 40.7→76.4 into the bright court footage).
- **53.70s [0.2 pass]** — Hard cut — return from the tennis B-roll to Sky (brightness falls 76.4→35.1). The prose puts the return at ~52.8s; the detector/4 fps timebase spreads the 0.6s cutaway's two boundaries to 52.73/53.70s.

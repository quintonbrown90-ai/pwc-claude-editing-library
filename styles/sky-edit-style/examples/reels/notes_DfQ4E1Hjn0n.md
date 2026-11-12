# NOTES — DfQ4E1Hjn0n (75.6s, "5 Content Types" — 100k in 6 months)
## Structure
- Sky at desk, dark room, black shirt. A "5 Content Types" checklist recurs top-left; each type gets its own animated diagram. One B-roll cutaway (burger).
- Captions: white sans center ~y560-620, 1-3 words, on the word beat.

## Devices
1. "5 CONTENT TYPES" CHECKLIST (~0.0-2.2s, recurring): green title top-left (~x60-300, y30-60) + 5 white rows appearing one at a time (~0.0-1.2s): "01 Gamification", "02 Demonstration", "03 Borrowed Attention", "04 Niche Philosophy", "05 Storytelling" [rows 3-5 text partially blurred in early frames — confirmed from later recap frames]. Rows sharpen as they appear. The current row highlights green when its section starts. Returns: ~6.0s (01), ~17.0s (02), ~31.5s (03), ~44.5s (04), ~60.5s (05), ~70.5s (full recap).
2. PHONE MOCKUP + GROWTH BAR (~2.2-6.0s): title "100k in 6 Months" (white "100k in" + green "6 Months") top-center; iPhone mockup drops in ~2.2s showing an IG profile ("travelprofile", 100K followers). Horizontal progress bar below the phone ~3.5s ("month 1" left, "month 6" right); green fill animates left-to-right ~3.8-5.5s. Fades ~6.0s.
3. TIER LIST CARD (~7.2-8.8s): white card top-right (~x700-950, y40-200) titled "Lists, Rankings, tiers"; S/A/B/C tier rows with small gray squares filling in one at a time ~7.5-8.5s.
4. BURGER B-ROLL (~8.8-13.2s): full-screen close-up Big Mac being built (sauce, pickles, lettuce, cheese, top bun) — 4.5s satisfying food B-roll with captions over it. "Zero Value" white text center ~12.5s.
5. "DRIVES EYEBALLS" COUNTER (~13.2-16.5s): green/white title top-center + eye icon + VIEW COUNTER counting up rapidly: 10,317 -> 133,751 -> 377,355 -> 638,252 -> 785,785 -> 891,063 -> 947,315 -> 983,792 -> 997,886 (~13.5-15.0s) then "1,000,000 Views" ~15.0s. Branch diagram: eye connects via green lines to 4 white bars ("other 4 formats") ~15.2-16.0s.
6. PHONE MOCKUP "SHOW IT LIVE" (~19.5-23.0s): phone drops in top-center, green/white title "Show It Live" above; phone screen shows a live video (LIVE badge). Labels pop around the phone: "Product" left ~20.5s, "Service" right ~21.5s, "Coaching" left ~22.0s.
7. BALANCE SCALE (~25.8-30s): title "1 Demo = 10x Trust" top-center (green "1 Demo" + white "= 10x Trust"); white scale line drawing ~26.0s with green "Demo" weight on left pan and white triangle on right; scale TILTS: left down ~26.5s, then "X10 Talking Heads" label loads right ~28.0s and scale tips right ~28.5s. Animates (tilts back and forth) as he talks.
8. FORMAT CARDS TRIO (~32.5-36.0s): three dashed-border video cards drop in top (~x40-980, y40-220) with green labels: "Stitches" ~32.5s, "Reactions" ~33.2s, "Green Screens" ~33.8s. Title above morphs to "Borrow Their Attention" ~35.5s.
9. BIG CREATOR / YOU DIAGRAM (~36.0-38.0s): big "Big Creator" circular head left (~x60-200, y130-260, green ring) + small "You" head right (~x700-780, y150-220, label "reputation + attention" below); green connector line draws between them ~37.0s. Big head ~2.5x You head.
10. DOT CONSTELLATION (~46.0-52.5s): title "Against Everyone" green top-center; ~15 white dots scatter into a loose circle (~x380-700, y80-220) ~46.0-47.0s; one dot turns GREEN ~48.5s with tiny label "Create a contradiction" [UNVERIFIED exact]; more tiny text under it ~50.5s. Green dot pulses.
11. "THE UNPOPULAR TAKE" QUOTE CARD (~52.5-58.5s): white quote card top-center (~x400-700, y60-220), green title above; text TYPES in character by character: "Plastic will be a net positive for society..." (~53.0-56.5s, ~0.15s/char); timeline below: "today" (green dot) ——— "+100 yrs" (green dot) ~53.5s. Fades ~58.5s.
12. BRAND LONGEVITY WAVE CHART (~62.5-70.5s): title "Brand Longevity" green top-center; axes frame draws ~62.5-63.5s; dotted SINE WAVE draws left-to-right ~64.5-67.5s with green dots at peaks/troughs; labels pop at peaks: "Superfans" ~68.0s, ~69.0s, ~69.5s. Wave = seasons of content.
13. ENDING: full checklist recap ~70.5-75.6s; ends on Sky mid-word "Good..." [UNVERIFIED final frame].

## Sound (measured, Batch 36)

Bed: ABSENT (measured). SFX: 0 confirmed — including on the 1M view-counter climb and the burger B-roll (Sky narrates continuously over the cutaway; no B-roll audio measurable). Transitions: all cuts silent. Silence: none (0 hits @−35/−50 dB). One unconfirmed 5.93 kHz sharpness hit (19.25s) logged in the soundmap.

Full measured soundmap: `claude-editing/research/video-harvest/instagram/batch-36-sky-completion/soundmaps/SOUNDMAP_DfQ4E1Hjn0n.md` (mean -17.5 dB, max -0.6 dB, voice median RMS -19.5 dBFS; method: volumedetect/astats, silencedetect −35/−50 dB, full spectrogram read, STFT tone scan + tonal-sharpness/zoom adjudication, word-gap RMS, transient census, scene-cut cross-check).

## Transitions (Batch 36)

Method: ffmpeg scene-cut detection `select='gt(scene,0.35)'` plus a 0.2-threshold pass for soft cuts (3 cut(s) at 0.35, 7 at 0.2), each classified against the existing 4 fps frames in `claude-editing/examples/sky/motion-teardown/frames/DfQ4E1Hjn0n/` (sharpness/saturation/brightness/diff profile) and the device prose above. All cuts are silent (see Sound section).

- **8.81s [0.35]** — Hard cut — Sky → burger B-roll (device 4, ~8.8s; single-frame diff 55.7).
- **12.85s [0.2 pass]** — Hard cut — burger B-roll edit/return boundary (prose: B-roll ends ~13.2s).
- **23.02s [0.2 pass]** — Graphic-state change — phone exit / balance-scale build (~23.0–25.8s).
- **25.46s [0.2 pass]** — Graphic-state change — balance scale draw (~25.8–26.0s).
- **37.74s [0.2 pass]** — Graphic-state change — 'Big Creator / You' diagram (~36.0–38.0s).
- **57.72s [0.35]** — Graphic-state change (0.368) — quote card exit / wave-chart build (quote fades ~58.5s).
- **75.28s [0.35]** — End-of-reel cut — final frames of the checklist recap (reel ends 75.6s); end/loop point.

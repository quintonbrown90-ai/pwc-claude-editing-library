# NOTES — De-A2dvCeV3 (63.2s, "These formats are officially dead" — fast content = fast food)
## Structure
- Dark studio, monitors + night city windows, Sky in black tee, gray pants. ORANGE accent (sequel to DfDuMnCjNdE's shallow-formats thesis). Card-wall heavy: the top of frame is almost always a floating cluster of format cards.
- Captions: white sans center ~y560-620, 1-3 words, on the word beat.

## Devices
1. FORMAT CARDS WALL (~0.0-1.5s): five small video cards fly in top (~x100-980, y40-200) one at a time: man in a suit ~0.2s, orange tournament bracket ~0.5s, woman with a book ~0.8s, tier-list card ~1.0s, a man ~1.2s. Sky points up at them.
2. CARD SPOTLIGHT SEQUENCE (~1.8-4.0s): each card scales up in turn with an orange label above it as Sky names it: "S-tier Ranking" ~2.0s, "Rating" ~2.8s, "Tournament" ~3.2s, "This or that" ~3.8s.
3. "FAST CONTENT" CURSIVE (~4.5-5.5s): four cards regroup into a row top-center; orange cursive "Fast content" appears below them ~5.0s.
4. "LINES" PANEL (~6.5-9.0s): glass panel top-center (~x100-900, y40-250) with colored horizontal lines (orange/yellow/blue/green) + small orange circle icon; cards orbit around it. Lines pulse.
5. AUDIENCE/CUSTOMER SPLIT (~9.8-13.5s): single video card (man in suit) center-top (~x550-700, y40-250) with two labels: "Audience" (left, orange cursive) ~10.0s and "Customer" (right) ~10.2s; cluster of small heads at left of the card ~10.5s, growing; ~12.5s the heads turn RED one by one (warning).
6. CARD CLUSTER + VIEW COUNTS (~14.5-17.0s): cluster of 5-6 cards re-forms top-center with view counts: "1.2M / 41.7K / 18.3K / 12.4M" (~15.5-16.5s).
7. "HIGH ENGAGEMENT" LINE CHART (~17.0-18.5s): purple line chart draws across the top (~x400-980, y200-300) with "HIGH ENGAGEMENT" label; data points pop: "12.3K / 34.5K / 559" (~17.8s).
8. REACTION DOTS + SLIDER (~18.0-20.5s): colored dots (pink, teal, green, red) pop onto the cards ~18.2s; orange horizontal slider with a knob below (~x100-900, y420-480) with "-0.50" label; knob slides left ~19.0s, label changes to "-0.27" ~19.5s.
9. "LINES" PANEL RETURNS (0:40 TIMER) (~21.0-25.5s): colored-lines panel returns top-center with red "0:40" timer pill top-right ~21.5s; lines fill/pulse; ~24.5s panel tilts slightly (3D tilt) and a purple line highlights.
10. "TRUST" PANEL (~26.5-29.0s): panel morphs to green-bordered version with green check + "TRUST" label and "Built by the repeated process" subtext ~27.0s; small cards orbit around it (~x100-980, y40-300).
11. ORANGE PLAY-CARDS TRIO (~30.0-31.5s): three orange rounded cards with white play triangles fly in top-center (~x100-500, y40-180).
12. "POV DEMOS" CARD (~31.5-33.0s): video card (hands + plate) flies in top-right labeled "POV Demos" (orange) ~32.0s; Sky points at it.
13. "MULTI-SHOT EDUCATION" CARD (~33.0-34.5s): video card (woman holding a lens) flies in top-center labeled "Multi-shot Education" ~33.5s.
14. "TRANSFORMATIONS" CARD (~34.5-35.5s): video card (smiling man) flies in top-left labeled "Transformations" ~35.0s.
15. "SHIFTING BELIEFS" LINES PANEL (~36.5-39.5s): colored-lines panel returns top-center with green "SHIFTING BELIEFS" label at left + small head; lines fill/pulse; green check pill top-right ~38.0s.
16. 2025→2027 TIMELINE (~40.0-43.5s): horizontal orange timeline draws across the top (~x100-900, y40-120) with nodes: "2025" ~40.5s, "Fast-paced content 2026" ~41.0s, "Nutrient-dense formats 2027" ~41.5s; small cards cluster under each node.
17. NICHE PILLS (~44.5-55.5s): four format cards return in a row top (~x100-980, y40-220); below them niche pills appear one at a time: "Niche 1" ~44.8s, "Niche 2" ~45.2s, "Niche 3" ~45.5s; then topic pills: "Marketing" (orange) ~48.5s, "General business" (red) ~49.0s, "Real estate" ~51.5s, "Finance" ~52.0s, "AI" (yellow) ~52.5s; pills glow/turn red one at a time ~50.0-52.0s (saturated niches); then green/blue pills: "Dog training" ~54.5s, "Crafts" ~55.0s, "Sciences" ~55.5s (unsaturated niches).
18. "POST" PILL (~56.0-57.0s): blue "Post" pill top-center with a green check; card cluster shrinks.
19. FUNNEL (~57.5-63.2s): 3-tier funnel draws top-center: blue top tier "Viral Reel" (4 thumbnails + "100,000 impressions / Brings new people to your profile") ~58.0s, purple middle tier ~58.5s, green bottom tier ~59.0s; middle tier label "Valuable Back-End Content" ~59.5s; bottom tier label "Nutrient-dense format" ~60.0s; bottom tier gains "Trust → Potential Clients" ~60.5s; three green "$" icons pop below the funnel ~61.0-62.0s. Ends on the funnel + $$$ ("catch all the impressions that are coming in the door").

## Sound (measured, Batch 36)

Bed: ABSENT (measured). SFX: 0 confirmed edit SFX — BUT a pulsed 5,926 Hz train runs 17.50–18.16s under the 'High Engagement' line-chart draw (sharpness 0.32, zoom-verified). The 13.28s flag is refuted (sibilance of 'just saying stuff.'). Transitions: no cuts exist (single take). Silence: none (0 hits @−35/−50 dB).

Full measured soundmap: `claude-editing/research/video-harvest/instagram/batch-36-sky-completion/soundmaps/SOUNDMAP_De-A2dvCeV3.md` (mean -16.7 dB, max -0.8 dB, voice median RMS -18.4 dBFS; method: volumedetect/astats, silencedetect −35/−50 dB, full spectrogram read, STFT tone scan + tonal-sharpness/zoom adjudication, word-gap RMS, transient census, scene-cut cross-check).

## Transitions (Batch 36)

Method: ffmpeg scene-cut detection `select='gt(scene,0.35)'` plus a 0.2-threshold pass for soft cuts (0 cut(s) at 0.35, 0 at 0.2), each classified against the existing 4 fps frames in `claude-editing/examples/sky/motion-teardown/frames/De-A2dvCeV3/` (sharpness/saturation/brightness/diff profile) and the device prose above. All cuts are silent (see Sound section).

No scene cuts detected at either threshold (0.35 or 0.2) — a single continuous A-roll take. Every device entry/exit (format wall, lines panels, card cluster, timeline, funnel) is an overlay animation, and all land silent (see Sound section).

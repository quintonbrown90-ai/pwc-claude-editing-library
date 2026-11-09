# TESTS — the QC gates (run on the EXPORTED file, in motion)

A build is DONE + VERIFIED only when every gate passes on the final file.
Builder reports and settled-frame audits are not tests.

## Technical gates

- [ ] Full decode clean; 1080×1920 (post file), yuv420p, faststart moov
- [ ] freezedetect (n=0.003, d=0.35): ZERO freezes ≥0.35s in footage spans
- [ ] Ending: last spoken word → end card ≤ ~1s (no dead-air tail)
- [ ] Lip sync: container offsets 0ms; onset strips eyeballed on loud windows
- [ ] Words never clipped at any cut — full envelope survives every edit

## Design gates

- [ ] Face audit: zero caption/device pixels over his face (hero occlusion excepted)
- [ ] Transition audit: frames ±0.15s around every card/board entrance+exit —
      hard cuts for boards over footage, no cross-fade over the face, text
      lands WITH its plate (no blank plates)
- [ ] Safe zones: nothing in top bar / right rail / bottom block; cards high
- [ ] Palette: teal + gold + navy only — a single red pixel fails the build
- [ ] Components match COMPONENTS.md specs exactly (colors, fonts, geometry)
- [ ] Every motion matches its named easing (watch it — overshoot overshoots)

## Retention gates

- [ ] Hook: claim/curiosity ≤2s WITH his face present (PiP/split over boards)
- [ ] Open loop early + second loop before midpoint
- [ ] Visual event every ≤2s; no static hold > ~1.5s uncovered
- [ ] Every section ends on a mini-payoff or a new question
- [ ] Ending chains to the next watch (loop-back / series / keyword)
- [ ] Sound: audible accents on payload words + every entrance AND exit

## Truth gates

- [ ] Captions = script ground truth; no ASR-only misquotes; never early
- [ ] Numbers/proof on screen are real (no fabricated examples as his)
- [ ] Hidden app never named; blur discipline per asset class
- [ ] Keyword in the video has a live, tested flow before posting

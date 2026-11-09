<!-- PART: captions/captions-word-exact.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# CAPTIONS — word-exact timing (MEASURED)

Source: Adilet `skills/adilet-system/CAPTIONS.md` (measured median lead
+0.013s over 86 caption changes — his −0.3s claim was BUSTED, do not teach
it) + Sky D1 (bare bold 1–3 words) + `skills/pwc-designed-captions/`.

## The rule
Captions land ON the word. The voice track is the master clock: captions,
beats and motion are all scheduled from the finished voice track's word
timings, never from a script estimate.

## Executable steps
1. Transcribe with word timestamps (faster-whisper or the finished voice
   track's timings).
2. Avatar lane: word-exact top strip, never over the face.
3. Sky lane: bare bold 1–3 words on screen, one at a time, fully gone
   before the next.
4. Verify: spot-check 5 caption changes against the audio — each must land
   within ±1 frame of the word. A caption early or late by 2+ frames fails.

## Worked example
Word "sued" at 2.41s → the caption word "SUED" appears at 2.41s (frame 72
@30fps), gold, Anton, top strip above the head. Previous word fully gone.

## PWC skin
Palette teal/gold on navy; fonts Anton / Poppins ExtraBold / Playfair gold
italic. Safe zones hard: text x 70–930, y 280–1480 on 1080×1920.
## Self-learning — folded Nov 8, 2026 (research/knowledge/SELF-LEARNING.md)

- **SL-06** — Designed captions rejected: chunks overlap/ghost — one chunk at a time, clean hard cuts. (2026-11-05)
- **SL-09** — Caption typos "right not" / "brands is" shipped — proofread captions vs transcript pre-render. (2026-11-07, P1 deleted version)
- **SL-32** — Measure the claim: caption lead +0.013s (not −0.3s); proven-hook remakes win; 35.5s / 222 wpm / beat every 1.5–3.5s / −14.2 LUFS. (2026-11-05, Adilet teardown)

## Variants (v9)
- **v9 · @charliehills, DfZkebcgCV4:** 8. @charliehills, DfZkebcgCV4 — 21-effect catalog cross-refs (covered entries): karaoke → captions/captions-word-exact.md; map route → effects/effects-journey-map-route.md; whip pan → camera-moves/ camera-whip-zoom.md; counter → effects-self-building-chart.md (see note 3); progress bars → effects/effects-timeline-playhead.md (same shape as Q's Water Line); zoom punch → effects/ effects-digital-zoom.md; grid wipe → effects/effects-mosaic-drop.md. The catalog part itself is a new draft (charliehills-21-effect- catalog.md); these are its covered rows, not second parts. _(source: v9_variants_bulk_a.md)_
- **v9 · @?, V8-38:** V8-38 — Timed transcript, not plain script: timestamps make animation plans precise → captions-word-exact.md _(source: v9_verification.md)_
- **v9 · @?, V8-76:** V8-76 — Caption formula: one-line DM CTA + tag creator + 3 hashtags → captions-word-exact.md _(source: v9_verification.md)_
- **v9 · @?, V8-155:** V8-155 — Explain Rule: voice model + listen-back model for word-level timing; rebuild around a real session (oTWUyW_bR-g, AI LABS) → captions-word-exact.md _(source: v9_verification.md)_
- **v9 · @millee.md, DfBBG0xPioN:** @millee.md DfBBG0xPioN — TikTok-style captions, never italic serifs; hooks on no/white/black background only. DIFFERS: the background rule (no/white/ black) is stricter than Q's Sky captions; PWC keeps navy field + teal/gold. _(source: bulk-c VARIANTS.md)_
- **v9 · @wassimyounes__, DYf-n9PguD5:** @wassimyounes__ DYf-n9PguD5 — 2-word UPPERCASE subtitle chunks by default. DIFFERS: chunk size is a parameter (2-word UPPERCASE) the part doesn't name. _(source: bulk-c VARIANTS.md)_

# PACING — cut rates, beat rhythm, retention structure (@adilet.fndr)

> **[MEASURED]** from ffprobe, scene detection, frame logs (deep set of 13)
> and transcripts. **[INFERRED]** where grouped/interpreted.

## ⚠ Measurement warning [MEASURED]

ffmpeg scene-score (0.35) **cannot count his cuts**: the avatar and stage
persist across beat changes, so full card swaps often score under
threshold — several videos read "0 cuts" while changing visuals every
2–4s. The unit of his pacing is **the beat** (one claim → one new proof
object / pose / number), not the scene cut. Numbers below separate the
two honestly: scene cuts where the detector can see them, beats from the
frame logs everywhere.

## Length [MEASURED, all 59]

- Duration: min 5.0s · **median 35.5s** · mean 34.5s · max 70.3s.
- System-era explainers cluster at **30–65s**; the hero is 63.4s — his
  longest format is reserved for system/mythology content. Listicles and
  single-claim videos run 20–45s.

## Speech rate [MEASURED]

- Hero: 226 words / 63.4s ≈ **214 wpm** — dense, no dead air (the audio
  chain's CUT stage, AUDIO.md). **Catalog-wide (51 videos with substantial
  speech): 180–300 wpm, median 222 wpm** — fast narration is a constant
  of the account, not a per-video choice. Per-video rates in CATALOG.md.
  (8 posts have little/no speech: early-era music slideshows and
  link-bait clips.)

## Beat rhythm [MEASURED, hero + deep set]

- **Hero scene cuts** (detector-visible): 20 cuts / 63.4s, mean scene
  ≈ 3.0s; the CTA tail accelerates (cuts at 56.9 / 57.6 / 58.3 / 61.0s —
  the negation montage + end card fire faster than the body).
- **Beat changes** (frame logs, all formats): a new visual event —
  component swap, stamp, count-up, pose change — every **~1.5–3.5s**
  (≈ 17–35 events/min). Nothing on screen sits still longer than ~4s.
- **Avatar pose changes every ~1–2s**, word-synced (deep-set logs) — the
  presenter supplies half the motion budget by himself.
- **Section rhythm** in listicles: a new "trap"/item every ~5–8s, marked
  by a background flip (cream→red→black) or a fresh numbered card; items
  accelerate slightly toward the end.

## Retention structure [MEASURED from hero + top originals]

1. **0–2s — the claim is already on screen.** Hook line spoken AND shown
   (wall of reels, the $100,000 numeral scrambling up by ~2–4.5s in the
   lawsuit format). No intro, no logo, no greeting.
2. **First proof by ~5s.** The subject file / count-up / diagram that
   proves the hook arrives inside the first two beats.
3. **Open loop in the first 10s.** "Here's what nobody tells you" /
   "but nobody's showing you how" — the mechanism is promised, not yet
   given; exhibits/list items then pay it off in installments.
4. **Escalation ordering.** List items and exhibits climb (small number →
   big number; the file count-up 22 → 191 is the hero's spine). The
   biggest visual (wall of reels, full file fan, black finale) lands in
   the last third.
5. **Verdict beats.** Short one-line scenes ("Mine don't look like
   slop.") reset attention between evidence blocks — a stamp or a single
   sentence, then the next proof.
6. **CTA as the final beat, ≤ ~3s.** Keyword card (SKILL / PLUGIN) or the
   send-to-Claude + follow device; never a long outro. The hero spends
   its last ~2.4s on COMMENT SKILL.
7. **Series pacing across posts** [MEASURED]: winning hooks re-run inside
   two weeks with micro-variations (HOOKS.md, Pattern 1); format
   costumes rotate by topic while the DNA stays constant (ILLUSTRATION
   taxonomy).

## PWC pacing spec (what we adopt)

- Video length: 30–60s for explainers; mythology/launch videos may run
  to ~65s.
- Beat = one claim + its proof object, every 1.5–3.5s; pose/visual event
  at least every ~2s; nothing still > 4s — enforced at self-review
  (PROMPTS.md stage 5 counts exactly this as WEAK).
- Hook claim visible in frame 1–2s **with** the presenter present;
  first proof object by 5s; open loop by 10s; CTA ≤ 3s at the end.
- Speech ~200 wpm with dead air cut (native voice rate, never
  time-stretched — AUDIO.md).

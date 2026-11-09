# CAPTIONS — the word-timed caption system (@adilet.fndr, Exhibit C decoded)

> **[MEASURED]** = timed/observed by us. **[CLAIMED]** = his on-screen
> marketing, tested below. **[INFERRED]** = reconstruction.

## What the system looks like [MEASURED, hero frames]

- A **caption strip runs along the top of the frame for the entire reel**,
  advancing word by word / short phrase by short phrase in sync with the
  voice. It is part of the stage design (small banner, file-label styling),
  not an Instagram auto-caption overlay.
- Inside scenes, **key words get their own typography**: the number in a
  count-up, the word on the stamp, the term on the exhibit card. Exhibit C's
  own card shows the design intent: a timeline ruler, the phrase
  "the **KEY** word" with KEY in accent color, and a "voice" marker line
  the caption is compared against.
- Captions are scheduled from the **finished voice track's word
  timestamps** — the same master clock as the scenes (SYSTEM.md stage 4).

## The −0.3s claim — TESTED [MEASURED VERDICT]

His Exhibit C claim: *"word-timed captions, where the key word lands a
beat before it's said — AHEAD OF VOICE −0.3s."*

**Test (hero reel):** we detected every caption-strip change frame
(top-strip pixel-diff at 30fps; 86 clean changes) and compared each to the
nearest spoken word onset (faster-whisper word timestamps, base model).

| Metric | Result |
|---|---|
| Caption changes matched to word onsets | 86 / 86 |
| Median lead | **+0.013s** |
| Mean lead | **−0.007s** |
| Spread | most within ±0.10s; extremes ±0.23s (consistent with ASR onset jitter ±0.05–0.15s + 1-frame quantization) |

**Verdict: the −0.3s lead does not exist in the captions viewers read.**
If a constant −0.3s offset were applied, the median would sit at +0.30s —
it sits at **0.00s**. His captions land **on** the spoken word,
frame-tight. Two honest caveats: (1) this measures the running caption
strip; a handful of giant center-stage key words could not be isolated by
the strip detector — but scene cards and count-ups also cut on their
beats, not 0.3s early. (2) ASR word onsets carry ~±0.1s jitter, so a lead
smaller than ~0.1s could hide in the noise — a lead of 0.3s could not.

**The real spec is better than the claim:** word-exact sync (0.00s ± a
frame) is what makes the reels feel engineered. A caption that arrives
0.3s *early* would spoil the very words it highlights.

## The caption spec (use this)

1. Generate word timestamps from the **final** voice track. Never time
   captions from the script or from a pre-speed voice.
2. Schedule every caption event **on** its word onset (target lead 0.00s,
   tolerance ±1 frame at 30fps). Phrase chunks of 1–4 words, advancing
   continuously — no gaps, no full-sentence dumps.
3. The beat's **key word** (the noun/number the proof object shows) gets
   the emphasis treatment — accent color + the component's own big
   typography — at its onset, not before it.
4. Placement: a fixed caption zone designed into the stage (his: top
   strip). For PWC: the caption strip lives in the stage's top zone,
   inside IG safe zones, never over the avatar's face (BRAND.md).
5. Type: small caps / label styling for the strip (it is furniture, not
   the headline); display caps reserved for the in-scene key words,
   stamps and count-ups.

## PWC mapping

PWC's standing caption rules (word-by-word, animated, never over the
face, gold keyword) already match his system almost 1:1 — the upgrade
from this teardown is (a) schedule from the final voice track's word
times as the single master clock for captions AND scene beats, and
(b) drop any "lead the voice" instinct: **sync is the flex**, on the word,
every word.

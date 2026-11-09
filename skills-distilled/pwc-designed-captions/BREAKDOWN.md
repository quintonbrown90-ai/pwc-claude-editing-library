# BREAKDOWN — "Designed Captions" (@viashaan, CAPTIONS reel)

The reference: a talking-head reel pitching that Claude Code *designed* his
captions instead of him typing them. Core line: **"As I say it, the things
happen."** Every claim below is visible in the video or its storyboard.

## What actually happens on screen

1. **Captions never fight the UI or the face.** His stated rules: text never
   goes behind his head (in the occlusion sense), never under Instagram's
   buttons. Placement is solved per phrase from a face track — he claims
   tracking "10 times a second" (word-timed transcript, verified); real
   pipelines track per frame at the 30fps output rate and smooth, which
   meets or beats that claim.

## Verified timeline (WhisperX word timings from the reference audio)

| t | Spoken | On screen |
|---|---|---|
| 0.9–3.0 | "Wait, how are these words going behind my head?" | caption words pass behind his head |
| 5.7–11.4 | "…it switches up like glowing letters or big white capitals or chunky italics" | style switches land ON the style names: glow at 8.1, BIG WHITE CAPITALS at 9.5, chunky italics at 11.0 |
| 12.2–15.9 | "I've set Claude Code up to design all my captions, even the words behind my head" | the system claim; hero treatment on "design" |
| 16.9–23.1 | "It's tracking my face 10 times a second and it knows where all of Instagram's buttons are, so my captions never end up underneath them" | "never" gets the script-italic accent (21.9) |
| 23.7–31.4 | "Normally you have to cut yourself out frame by frame, all for one word, but I'm just lying here. And this room doesn't actually exist." | the fake lying-down scene swap (27.5–31.4) |
| 31.4–33.1 | "Comment CAPTIONS and I'll send you a breakdown" | funnel CTA |
| 35.7–36.1 | "…behind my head." | final hero word passes behind his head |
2. **Every phrase gets its own treatment, and the treatment switches as he
   speaks** — this switching IS the retention device:
   - a script-italic accent word for the negation ("never") — his is red;
     in PWC it is GOLD serif italic (Playfair), because Q's palette has no red
   - glowing letters for the "designed by Claude" magic moment
   - giant white capitals for the claim ("THE CAPTIONS AREN'T TYPED")
   - chunky italics for energy phrases
   - full-scene illustration swaps mid-sentence: a photoreal fake scene
     (him lying down, real-looking room) on "I could be laying down…", a
     cartoon + play-button card on "press play", a lined-paper note card on
     "I typed what I wanted to say"
3. **One word passes BEHIND his head** ("DESIGNED") — the hero effect. He
   name-checks the normal cost: frame-by-frame rotoscoping. The Claude way:
   a person matte (segmentation) sandwiched between two caption layers.
4. **Timing is word-exact.** Styles change on the spoken word, not on the
   subtitle line — which is why the pipeline starts from word timestamps.

## How it's built (the honest stack)

| Layer | Tool | Why |
|---|---|---|
| Word timings | WhisperX / faster-whisper (word_timestamps) | style switches land on words |
| Script truth | the speaker's script file, snapped onto ASR timings | captions never misquote him |
| Face track | OpenCV / MediaPipe face detection, 1 sample/sec + median | captions anchor in empty space, off the face |
| Person matte | MediaPipe Selfie Segmentation (or rembg/RVM) | foreground layer = no rotoscoping |
| Caption render | PIL per-frame, per-style fonts + MOTION easings | any style, any motion, frame-exact |
| Composite | ffmpeg overlay stack: video / behind-captions / matte / front-captions | the sandwich is the trick |
| Scene swaps | still/illustration cards cut in on the exact noun phrase | "as I say it, the things happen" |

## What transfers to PWC (and what changes)

- Palette: his red accent → PWC GOLD #FEE238 serif italic; glow → PWC TEAL
  #14A886; all else white on deep-navy stroke. NO RED anywhere (Q's rule).
- Placement: Q's standing law is stricter — captions live in the empty space
  ABOVE the head by default; behind-head is reserved for ONE hero word per
  section; IG safe zones are hard-clamped in code (safe_zones.py).
- Scene swaps: use REAL footage/photos/screen recordings (Q's rule), never
  flat AI plates; the pwc-animations skill supplies the animated inserts.
- The funnel keyword was CAPTIONS; the deliverable was the prompt pack. Q's
  version of this skill IS the deliverable — prompts in PROMPTS.md.

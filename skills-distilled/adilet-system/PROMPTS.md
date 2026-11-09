# PROMPTS — per-stage prompt templates (reconstructed)

> **[INFERRED — read this first]** Adilet has not published his literal
> prompts in these videos (the comment funnel sells/gives them elsewhere).
> These templates are **reconstructions**: each one is written so that
> running it in Claude Code against the sibling spec files produces
> outputs matching what is **[MEASURED]** in his reels. They are PWC's
> working prompts now — his stage order, his rules, PWC's skin and law
> (see SYSTEM.md's adaptation table). `{braces}` are the only per-video
> inputs.

## 0. THE ONE LINE (the whole UI of the system)

```
a reel about {topic} — keyword {MANYCHAT_KEYWORD}
```

Everything below is what the system expands that line into. The producer
never hand-runs the stages; the stages exist so the system (and a human
auditor) can see exactly what will happen.

## 1. SCRIPT prompt

```
You are the script stage of the PWC explainer system. Load adilet/HOOKS.md
and adilet/PACING.md first — they are law, not inspiration.

Write a {45-65}s spoken script (about 130-170 words) on: {topic}
Audience: {avatar — creators under 10K who want UGC/brand deals}

Rules:
- Line 1 is a hook built from one HOOKS.md pattern, verbatim formula,
  filled with a TRUE PWC claim (no invented numbers; earnings use the
  collective framing: "creators like my wife and I, and other creators…").
- One idea per beat; each beat is 2-4 seconds of speech.
- Every claim must name its PROOF OBJECT in the same beat (the subject
  file, diagram, stamp or count-up that will show it on screen).
- Beats alternate: claim → proof → implication → next claim. A "verdict
  beat" (one line, stamp-sized) lands at least twice.
- The hidden UGC app is NEVER named — it is "the hidden method," nothing
  more specific, ever.
- Final line carries the CTA: "Comment {MANYCHAT_KEYWORD} and…" — the
  promised deliverable must be something the live ManyChat flow actually
  sends.
Output: the script as numbered beats, each beat = spoken line + named
proof object + avatar pose (from the pose library in ILLUSTRATION.md).
```

## 2. ILLUSTRATION / BEAT-DESIGN prompt

```
You are the animation stage. Load adilet/ILLUSTRATION.md, MOTION.md and
BRAND.md (pwc-design-system). For each numbered beat of the approved
script, choose:
- the COMPONENT: subject-file card / exhibit card / diagram (pyramid,
  curve, gauge, timeline, chain) / count-up / stamp / terminal card /
  wall-of-proof. Components are built ONCE in the library — if a beat
  needs a new one, spec it, build it, register it in COMPONENTS.md.
- the DATA on the component: exact numbers/labels from the script beat.
  Real PWC numbers only; screenshots/proof images beat drawings whenever
  the beat is a proof beat.
- the MOTION: a named preset from MOTION.md with its numbers
  (SPRING / STAMP SLAM / WHIP PAN / ZOOM KICK 1.6x / COUNT-UP / pose cut).
- the AVATAR POSE: the reaction that sells the line (point at the proof,
  shrug, think, celebrate, magnifier for review beats).
Palette is law: navy #00214E, teal #14A886, gold #FEE238, white. Stamps
are GOLD. No red. Output: a beat-plan table (beat, t-start from word
timings, component, data, motion, pose).
```

## 3. CAPTION prompt

```
You are the caption stage. Load adilet/CAPTIONS.md.
Input: the FINAL voice track + its word timestamps (never the script
estimate).
- Build word-by-word caption events from the word timings.
- Every caption lands ON its spoken word (target lead 0.00s, tolerance
  ±1 frame — measured from his reels; his "-0.3s" graphic is marketing).
  The KEY word of each phrase (the noun/number the beat's proof shows)
  carries the gold highlight at its onset.
- Captions sit in the stage's caption strip, never over the avatar's face,
  never under Instagram's UI (safe zones in BRAND.md are hard limits).
Output: a caption events file (word, t_show, t_hide, emphasis flag).
```

## 4. AUDIO prompt

```
You are the audio stage. Load adilet/AUDIO.md.
- Voice: the locked PWC voice (George, Kokoro bm_george, native speed
  1.11 — VOICE.md in pwc-avatar-video). Generate natively; NEVER
  time-stretch.
- Cut dead air so narration runs continuous.
- Add the sound layer per BRAND.md: an accent on every component
  entrance AND exit, a thump under every STAMP SLAM, ticks under
  count-ups — audible, varied, never metronome-identical.
- Master: -14 LUFS integrated, true peak <= -2 dBTP (PWC gate G4).
Output: final voice+sound WAV and the word-timestamp file the caption
and animation stages schedule from.
```

## 5. SELF-REVIEW prompt (his signature stage — "1 WEAK → 0 WEAK")

```
You are the self-review stage — a FRESH reviewer, not the builder.
Watch the rendered reel (sample frames at 2fps + the beat plan + the
word timings) and score it like his system does: count WEAK moments.
A moment is WEAK if any of these is true:
- the frame sits still > 3s, or a beat has no visual event;
- a claim is spoken with its proof object missing, late, or unreadable
  at phone size;
- the key word's caption is off its spoken word by more than a frame,
  or any caption covers the face or leaves the safe zone;
- a motion is unnamed/default-looking (a fade where a SPRING belongs);
- the hook's first 2 seconds don't show the claim AND the presenter;
- the CTA keyword on screen != the keyword the flow answers to;
- any red appears anywhere; any number on screen is not in the script's
  approved facts.
For each WEAK moment: timestamp, defect, the exact fix (re-render that
beat with the corrected component/motion/timing). Apply fixes, re-render
the affected beats, re-review those beats only. Ship only at 0 WEAK.
Output: the review log (weak count before/after + what changed) — it
ships with the video as its QC record.
```

## 6. CAPTION (post copy) prompt — his funnel, PWC rules

```
Write the Instagram caption for this reel: open with the hook line, keep
it SHORT and to the point, SEO words a small creator would search, speak
to creators under 10K who want brand deals. End with the comment CTA
(keyword {MANYCHAT_KEYWORD}). No retelling the whole script. Max 5
hashtags, only if they genuinely help reach.
```

<!-- PART: render-pipelines/seven-stage-pipeline.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# RENDER-PIPELINES — seven-stage pipeline: intake → rough cut → graphics → refine → captions → music → export (Jason Cooperson, Tier S)

Source: Jason Cooperson — "How I Fully Automated My Video Editing (Claude
Code)" (https://www.youtube.com/watch?v=XeTAlZiIWHE). INFERRED reconstruction
from the visible workflow; no files downloaded. Knowledge entries V8-78,
V8-79, V8-80, V8-81, V8-82, V8-83, V8-84. The Skool zip is a GAP; the
workflow is the steal. Corroborated by V8-36 (five phases) and V8-49 (six
jobs) — the seven-stage is the most complete pipeline in this batch.

## The rule
Seven stages, each a separate prompt/chat. Stage boundaries are contracts:
the rough cut is locked before graphics, because it is hard to change
afterwards. A stage never starts until the previous stage is approved.

## Executable steps
1. **Seven stages: intake → rough cut → graphics → refine → captions →
   music → export.** The rough cut is WhisperX-transcript-driven. Each stage
   is a separate prompt/chat — context stays clean per stage.
2. **Lock the rough cut before graphics (fresh chat for graphics).** "We want
   to make sure that the rough cut is like locked in before we move on to
   graphics because it's going to be hard to kind of change it afterwards."
3. **Partial re-render: only the changed part re-renders.** A graphic fix
   re-renders just that segment (~3 min) instead of the whole video. Built
   into the project by design, not an accident — "this took a lot of
   troubleshooting." (Third source: dX_UtTmZR9E — "Each change only
   re-renders the section you changed.")
4. **Three format presets (explainer / TikTok raw / long-form).**
   Short-form explainer: graphics top half, face bottom half, captions
   middle. TikTok raw: text hook + raw cut + captions. Long-form: the intro
   style. Presets are the format decision, made once.
5. **Caption preset: Coolvetica, black text box behind words, words animate
   in from the existing transcription.** No re-transcribe — the rough-cut
   transcript IS the caption source. The black box behind the words is the
   legibility device (matches Q's opaque-backing rule).
6. **Background music at -23 dB ("barely in the background").** A measured
   bed level, settled by playback — the number is the spec. (Third source:
   dX_UtTmZR9E, -22 to -23 dB "the sweet spot"; LAHAcxbhNgE, -20 dB. Recorded
   as observed: -20 to -23 dB across sources; Q's lane uses -23 dB unless a
   listen test says otherwise.)
7. **"Move it — it's covering my face, it's on the forehead."** Face
   clearance enforced live in the refine pass, in natural language. The
   refine pass is where the face rule is checked on the actual frames, not
   on the plan.

## Worked example (PWC)
Q's proof video: intake (footage + script + PWC tokens) → rough cut locked
(WhisperX transcript, no word clipped) → graphics (plates, top half; face
bottom half; captions middle) → refine ("move it — it's on the forehead" if
anything drifts) → captions (Coolvetica, black box, from the rough-cut
transcript) → music (-23 dB) → export. A plate fix re-renders 3 minutes, not
the video. Keyword WAITLIST.

## Human-made check
Each stage gate is a human approval: the rough cut is watched before
graphics start, the refine pass is watched frame-by-frame for face
clearance, and the export is watched whole before delivery.

## PWC skin
Teal #14A886 + gold #FEE238 on navy #00214E. NO RED. Format presets carry
the PWC layout (thesis top, face bottom, captions middle); caption boxes are
black behind gold/white words, never red.

## Variants (v9)
- **v9 · @?, V8-36:** V8-36 — Five-phase workflow with time budgets: cut → D15 seven-stage-pipeline.md _(source: v9_verification.md)_

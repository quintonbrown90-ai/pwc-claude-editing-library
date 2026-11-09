<!-- PART: render-pipelines/review-checklist-six-mistakes.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# RENDER-PIPELINES — six jobs, one at a time + the six-mistake review checklist (Duncan Rogoff, Tier S)

Source: Duncan Rogoff (15-year editor — Apple, PlayStation, Nissan) — "I
taught Claude how to edit videos and it's INSANE"
(https://www.youtube.com/watch?v=REAOFI534lk). INFERRED reconstruction from
the visible workflow; no files downloaded. Knowledge entries V8-23, V8-49,
V8-51, V8-52, V8-53, V8-54, V8-116, V8-124, V8-151, V8-153. Corroborated by
V8-36 (five phases) and V8-78 (seven stages) — this is the tightest version
of the split.

## The rule
Never one-shot a finished video — "too much for Claude to handle so it just
made bad choices." Six jobs, one at a time: scripting, editing, design,
motion graphics, review, feedback. And the review is a checklist, run at 10
frames/sec, checked like a person — not a vibe check.

## Executable steps
1. **Six jobs, one at a time.** Scripting → editing → design → motion
   graphics → review → feedback. Each job finishes before the next starts.
   One-shot gets ~80%; budget the final 20% as directing, not as a redo.
   First draft is 60–70%: revisions are the job, sound last.
2. **Beat map before any graphics.** A list of every idea in the script +
   what's on screen while you say it. Changing a plan costs almost nothing;
   changing a finished graphic costs a lot.
3. **One graphic per IDEA, not per sentence (density rule).** Each idea gets
   one graphic that stays up long enough to breathe. The per-sentence
   graphic storm is a viewer complaint, not a feature — a direct density cap
   for Q's lane.
4. **Sub-agents per section + model split + render discipline.** Opus thinks
   (planning, creative direction); Sonnet builds. Max 4 concurrent renders;
   overnight renders; half-size drafts; full quality only after approval.
   (The render cap is a hard-learned rule: 9 parallel renders crashed his
   machine.)
5. **Six-mistake review checklist (10 frames/sec, check like a person).**
   Animation plays twice; flash-frame graphic; text lands too late to read;
   graphic sitting on my face; repeated word; lip drift. "Graphic sitting on
   my face" IS Q's face rule, as a checklist item. Write down YOUR three
   always-caught mistakes and hand the list to Claude.
6. **"Which instruction would have prevented each note?"** After fixing,
   Claude finds the instruction that should have prevented the note — and
   that instruction goes into the skill. The review makes the skill smarter.
7. **Blind reviewer loop (Take One / Video Director family).** After every
   version, a reviewer that never saw the work scores it — under the passing
   mark → another round, up to 3 times. Plan-check tool + finished-video
   check tool: two separate checks, two separate moments. (The repos
   themselves are unvetted — GAP; the loop is the steal.)
8. **Frame.io-style review: comments + screenshots dragged in.** "No video
   edit is ever perfect on the first version. Ever." AI revision in 15 min–
   2h vs human 24h+. The revision loop is built in, not bolted on.

## Worked example (PWC)
Q's P2 cut: beat map (every idea → on-screen) → one graphic per idea →
half-size draft → six-mistake checklist at 10fps (catches the text landing
late on the $92,000 line) → "which instruction would have prevented it?"
(→ "numbers land on the spoken word, never after") → instruction saved to
the skill → full-quality render after approval. Keyword WAITLIST.

## Human-made check
The checklist runs on the exported file, in motion, at 10fps — never on a
builder's say-so. The three always-caught mistakes are written down and
handed to Claude before the review starts.

## PWC skin
Teal #14A886 + gold #FEE238 on navy #00214E. NO RED. Review notes and beat
maps carry the PWC palette; the checklist itself is plain text, no decoration.

## Variants (v9)
- **v9 · @?, V8-44:** V8-44 — Screenshot-as-feedback: diagnose the cause, remake as full-size transparent → D11 review-checklist-six-mistakes.md _(source: v9_verification.md)_
- **v9 · @?, V8-88:** V8-88 — Three finishing-touch methods: transcript / timeline / Ask Agent → D11 review-checklist-six-mistakes.md _(source: v9_verification.md)_
- **v9 · @?, V8-89:** V8-89 — Timestamped feedback notes as precise edit instructions → D11 review-checklist-six-mistakes.md _(source: v9_verification.md)_

<!-- PART: effects/spotlight-question-highlight.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# EFFECT — spotlight-question highlight: light the named item, dim the rest [INFERRED reconstruction]

Source: @createcontent.club reel Det_axVk5c_ (Oct 20, 2026, 22.72s) —
the doc-scroll device at f_009–f_011: the interview doc scrolls and a
spotlight lights Q1, then Q2, then Q1+Q2 in sequence as each is named
("It's then going to interview you on your positioning"). The skill
file is GATED — rebuild from the visible spec only. Full decode:
`research/video-harvest/instagram/createcontent.club_Det_axVk5c_/createcontent.club_Det_axVk5c__DECODE.md`.

## The rule
In any list walkthrough, only the item being named is lit; the rest
dims. The lit item IS the unlocked item — the light is the pointer, not
decoration. One item lit at a time (or the named set, e.g. Q1+Q2 when
both are named together); the light moves ON the spoken word, never
before it, never after.

## Executable steps (rebuild)
1. Build the list as a full-screen doc/board (interview questions,
   checklist rows, format cards, idea rows — any list the voice walks
   through). Face-clear by construction: the doc is full-screen, no
   face in frame.
2. Dim the whole list to ~35–45% brightness; the named item stays at
   100% with a soft radial pool of light around it (falloff, no hard
   edge). The lit item may also carry a thin gold edge (PWC) to mark it
   as the current one.
3. Move the light ON the word that names the item: the voice says "Q1"
   → Q1 lights; "Q2" → Q2 lights, Q1 dims (unless the voice names both
   — then both stay lit, f_011). Entrance: 6–8 frames EASE OUT (the
   pool opens); exit: 5–6 frames EASE IN (it closes). Sound: soft tick
   or low whoosh on each light move — the move is audible.
4. Never light two unrelated items at once, never leave the light on a
   stale item while the voice has moved on. A lit item with no spoken
   name is a bug — the light follows the voice, not the scroll.

## Variants / use cases (list walkthroughs)
- **Interview walkthrough** (the source): Round 1's 8 questions, one
  lit at a time as Claude names them — the doc scrolls, the light
  follows. PWC: the self-onboarding interview
  (`parts/strategy/ccc-self-onboarding-interview.md`) as the walked
  list.
- **Checklist walkthrough:** pipeline checklists (cut pauses → add
  effects → export), the 95-gate rubric rows, the 5 anti-slop rules —
  each row lights as it is checked off.
- **Idea-table walkthrough:** the 10-idea Notion table — one idea row
  lights as its hook is spoken; the lit row is the next video to film.
- **Format-card walkthrough:** the three format cards — one card lights
  as its format is named; the other two dim until their turn.
- **Viral-grid walkthrough:** the grid of reels with view counts — the
  singled-out tile stays bright while the rest dim (Det f_014–f_015,
  same device on a grid, not a list).

## Face-clearance check
Face-clear by construction — the device runs on a full-screen doc, no
face in frame. When the same device is used on a list that shares the
frame with Q (e.g. a side-panel checklist), the pool never crosses the
head box; the list lives in the face-clear zone.

## Worked example (PWC)
Q's self-onboarding interview as a full-screen doc: the voice says
"Who exactly is your viewer?" → Q2 lights, the other seven questions
dim to 40%; a soft tick lands with the light. Then "What's your proof?"
→ Q4 lights, Q2 dims. The lit question is the unlocked item; the
walkthrough ends with the full doc bright and the CTA.

## PWC skin
Teal #14A886 / gold #FEE238 on navy #00214E, NO RED. The lit item's
edge is gold (never the source's blue highlight — the competitor-list
blue in the same reel is their color, not Q's). Same family as
`parts/effects/effects-spotlight.md` (the light pool on the speaker)
and the persistent-index highlight
(`parts/render-pipelines/pipeline-repurposing-one-to-ten.md` §2) — this
part is the LIST form: light the named row, dim the rest.

## QC status
QC status PENDING until the you-and-Claude loop runs after upload.

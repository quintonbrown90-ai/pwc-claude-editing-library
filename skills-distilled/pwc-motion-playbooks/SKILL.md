---
name: pwc-motion-playbooks
description: PWC motion + caption + camera playbooks distilled from the measured systems in the library — Viashaan's 8 named motions with exact CSS/Python values, Adilet's measured pacing and caption timing, Sky's motion QC, Herk's shot rhythm. Use when a video needs its motion specified (never "animate it"), a caption timed, a camera move chosen, or a render QC'd. Every value here is measured or published, with its source.
---

# PWC Motion Playbooks

Motion is specified in the PLAN (per element: name + frames + delay), not
improvised in the render. If a motion has no name here, it does not ship.
All house numbers are at 30fps on a 1080×1920 canvas.

## The 8 named motions (source: @viashaan "Describe Motion to AI" — PUBLISHED)

| Motion | Feel | Use it for | CSS | Python |
|---|---|---|---|---|
| LINEAR | constant speed | spinners, color shifts, tickers, marquee | `linear` | `linear` |
| EASE IN | slow start, speeds up | things LEAVING screen, exits | `cubic-bezier(0.55,0.06,0.68,0.19)` | `ease_in` |
| EASE OUT | fast in, soft landing | things ARRIVING, cards, labels | `cubic-bezier(0.22,0.61,0.36,1)` | `ease_out` |
| EASE IN-OUT | slow-fast-slow | moving between two spots, route lines, chart draws | `cubic-bezier(0.65,0.05,0.36,1)` | `ease_in_out` |
| OVERSHOOT | pops past, settles back | titles, buttons, pins, pills, hero words | `cubic-bezier(0.34,1.56,0.64,1)` | `overshoot` (strength 1.70158, verified peak 1.141) |
| SPRING | soft physical settle | playful elements, chunky italics, stickers | JS spring | `spring` (stiffness 170.0, damping 16.0) |
| BOUNCE | hits, rebounds | drops, falling objects, playful landings | JS bounce | `bounce` |
| STEPS | fixed jumps, no blend | clocks, counters, type-on text, stop-motion | `steps(n, end)` | `steps` (n=6) |

Full functions: `references/EASING.md`. Reference implementation:
`../pwc-designed-captions/code/easings.py` (in the pwc-designed-captions
skill — verified numerically).

## PWC house numbers (30fps)

- Caption word tick (BASE): STEPS, on the word's exact start frame. Never early.
- Caption phrase entrance: 4–7 frames, scale 92% → 103% → 100% (OVERSHOOT).
- Card / label entrance: 8–12 frames EASE OUT. Exit: 5–6 frames EASE IN.
- Chart line draw / map route: EASE IN-OUT across the spoken phrase.
- Count-ups: STEPS eased by EASE OUT (fast count, soft landing on the number).
- Cursor moves: 10–16 frames EASE IN-OUT, 97% scale dip on click.
- Stagger between rows in a list: 4–6 frames.
- Nothing on screen moves on LINEAR except machines (spinners, tickers).
- Exits are always faster than entrances and always EASE IN.
- Two elements entering with the same motion at the same frame is a tell —
  stagger or re-name one.

## Camera moves (sources: Sky D-devices + Adilet Exhibit B — MEASURED)

- **Whip pan** (Adilet): cut on the pan's fastest frame; the pan IS the
  transition — no cross-fade on top of it.
- **Zoom kick** (Adilet): punch-in on the payoff word, 8–12 frames EASE OUT,
  hold, ease back. Never a slow drift.
- **Punch-in on stressed words** (Tella/Clipify pattern, MIT): zoom on the
  word that carries the claim, not on every word.
- **Split-first-frame** (Herk, MEASURED): the first frame is already a split
  — proof/tool on top, speaker below. Shots 1.1–1.4s; pauses <0.2s; one
  visual per spoken phrase.
- **Per-line layout switching** (johannships, PUBLISHED): the layout changes
  on the spoken line, never mid-sentence.

## Caption timing (sources: Adilet MEASURED + Viashaan PUBLISHED)

- Word-exact captions land ON the word: Adilet measured median lead
  +0.013s over 86 caption changes (his −0.3s claim was busted — do not
  teach the −0.3s lead).
- Avatar lane: word-exact top strip, never over the face.
- Sky lane: bare bold 1–3 words on screen, one at a time, fully gone
  before the next.
- Real takes: style-switching designed captions (6 styles — BASE karaoke /
  SCRIPT_ACCENT Playfair gold italic / GLOW teal / BIG_CAPS Anton /
  CHUNKY_ITALIC / HERO_BEHIND Anton ~320px matte-occluded). Hero word
  passes behind the head (rembg u2net_human_seg matte on hero windows).
- Safe zones (hard): text x 70–930, y 280–1480 on 1080×1920. Nothing in
  the top 280px, bottom 440px caption zone, or right action rail.

## Audio chain (source: Adilet MEASURED)

Voice → cuts → speed → loudness. Mastered −14.19 / −14.16 LUFS, LRA ~2–2.6
on two measured reels. PWC sound identity on top: SFX on every imagery
entrance AND exit, layered landings on card rows, accents on statement
lines and number landings, low cleared instrumental bed under untouched
voice (his uploaded reels stay original-audio-only).

## QC gates (run on the EXPORTED file, in motion)

- freezedetect: zero freezes ≥0.35s (n=0.003, d=0.35).
- ±0.15s audits around every card/board entrance and exit; hard cuts only
  for boards over footage; a card's text lands with its plate.
- Last voice → end card ≤~1s.
- Lip-sync: ffprobe container offsets are decisive; frame strips at
  quiet→loud onsets vs the printed 100ms envelope.
- Retention read: hook lands a claim/curiosity in ≤2s with the face on
  screen; open loop early + a second before the midpoint; visual event
  every ≤2s; every section ends on a mini-payoff or a new question; ending
  chains to the next watch.
- Brand-DNA checklist (F1–F6) before any render ships — see the
  pwc-design-system skill's BRAND-DNA.md. A missing marker blocks the render.

## PWC skin law (overrides everything in this skill)

Teal #14A886 / gold #FEE238 on navy #00214E. NO RED — any reference's red
maps to gold. PWC logo in every video. Nothing over Q's face, ever. Real
footage/photos/screens, never AI-flat. No door device in any form.

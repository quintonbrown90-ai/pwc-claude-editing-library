# MOTION.md — the motion vocabulary (shared by every PWC skill)

Source: @viashaan's "Describe Motion to AI" system. Never write "animate it"
in a plan or prompt again. Every moving element gets a NAMED motion, a
duration in frames, and a job. If a motion has no name here, it does not ship.

| Motion | Feel | Use it for | CSS | Python (easings.py) |
|---|---|---|---|---|
| LINEAR | constant speed | spinners, color shifts, tickers, marquee | `linear` | `linear` |
| EASE IN | slow start, speeds up | things LEAVING screen, exits | `cubic-bezier(0.55,0.06,0.68,0.19)` | `ease_in` |
| EASE OUT | fast in, soft landing | things ARRIVING, cards, labels | `cubic-bezier(0.22,0.61,0.36,1)` | `ease_out` |
| EASE IN-OUT | slow-fast-slow | moving between two spots, route lines, chart draws | `cubic-bezier(0.65,0.05,0.36,1)` | `ease_in_out` |
| OVERSHOOT | pops past, settles back | titles, buttons, pins, pills, hero words | `cubic-bezier(0.34,1.56,0.64,1)` | `overshoot` |
| SPRING | soft physical settle | playful elements, chunky italics, stickers | (JS spring / approx. bezier) | `spring` |
| BOUNCE | hits, rebounds | drops, falling objects, playful landings | (JS bounce) | `bounce` |
| STEPS | fixed jumps, no blend | clocks, counters, type-on text, stop-motion | `steps(n, end)` | `steps` |

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

## The rule underneath

Motion is specified in the PLAN (per element: name + frames + delay), not
improvised in the render. Two elements entering with the same motion at the
same frame is a tell — stagger or re-name one.

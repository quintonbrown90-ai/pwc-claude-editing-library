<!-- PART: motion/motion-named-8.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# MOTION — the 8 named motions (PUBLISHED)

Source: @viashaan "Describe Motion to AI" (reel DezQiR7yMlW) —
`skills/pwc-animations/MOTION.md` (identical in
`skills/pwc-designed-captions/MOTION.md`). Never write "animate it" again.

## The rule
Every moving element gets a NAMED motion, a duration in frames, and a job.
If a motion has no name here, it does not ship.

| Motion | Feel | Use it for | CSS |
|---|---|---|---|
| LINEAR | constant speed | spinners, tickers, marquee | `linear` |
| EASE IN | slow start, speeds up | things LEAVING screen, exits | `cubic-bezier(0.55,0.06,0.68,0.19)` |
| EASE OUT | fast in, soft landing | things ARRIVING, cards, labels | `cubic-bezier(0.22,0.61,0.36,1)` |
| EASE IN-OUT | slow-fast-slow | moving between spots, route lines, chart draws | `cubic-bezier(0.65,0.05,0.36,1)` |
| OVERSHOOT | pops past, settles back | titles, buttons, pins, hero words | `cubic-bezier(0.34,1.56,0.64,1)` |
| SPRING | soft physical settle | playful elements, chunky italics, stickers | JS spring |
| BOUNCE | hits, rebounds | drops, falling objects, playful landings | JS bounce |
| STEPS | fixed jumps, no blend | clocks, counters, type-on, stop-motion | `steps(n, end)` |

## Executable steps
1. In the PLAN, name every moving element's motion + frames + delay.
   Motion is specified in the plan, not improvised in the render.
2. Two elements entering with the same motion at the same frame is a tell
   — stagger or re-name one.
3. Exits are always faster than entrances and always EASE IN.

## Worked example
Stat-chart card: line draws EASE IN-OUT over the phrase; number counts up
in STEPS eased by EASE OUT; lands with an OVERSHOOT dot. (Demo B, 28.44s.)
## Self-learning — folded Nov 8, 2026 (research/knowledge/SELF-LEARNING.md)

- **SL-02** — Sky's lines MOVE (draw on, pulse, track); static overlays fail — every line/device gets a named motion + duration + job. (2026-11-07)

## Line-motion variants (SL-02 — v8; named variants, not new effect parts)

Sky's lines MOVE — draw on, pulse, track, keep moving. A static line
overlay is a QC fail. The two named variants below are variants of the
line-draw grammar above (EASE IN-OUT draw + OVERSHOOT landing), not
separate effect parts: the grammar already specifies draw-on + pulse +
track, so separate parts would duplicate it.

| Variant | Grammar | Spec |
|---|---|---|
| **marching-dash** | EASE IN-OUT | Dashed connector line; dashes march along the line while it draws, label pulses on landing. Use for routes / sequences / "follow me" lines. |
| **glowing-head** | OVERSHOOT | Line draws on with a glowing gold head that leads the draw; head lands with an OVERSHOOT dot, then the line pulses once. Use for proof call-outs / gold-circle draw-ons. |

PWC skin: heads and dashes in gold #FEE238 on navy; never red.

## Variants (v9)
- **v9 · @millee.md, DfBBG0xPioN:** @millee.md DfBBG0xPioN — avoid the kinetic style Claude is known for; motion animations only occasionally. DIFFERS: a negative rule (what NOT to do) on the motion menu. _(source: bulk-c VARIANTS.md)_
- **v9 · @siddhantt.ai, DemSa_YN3XO:** @siddhantt.ai DemSa_YN3XO — frames-to-video: start frame → end frame → animation between; 240 frames at 30fps. DIFFERS: the frame-count device (240 frames = 8s) as the transition spec. (Troll-animation website itself is off-lane, not adopted.) _(source: bulk-c VARIANTS.md)_

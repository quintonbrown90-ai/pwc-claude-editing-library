# GSAP-EASES.md — eases as a system (distilled from the Phase 4 harvest)

Source: HankTheTank, "The Ultimate GSAP Crash Course (2026)" —
https://www.youtube.com/watch?v=aJmP2II5R4U — as distilled in
`research/knowledge/EASING.md` (§1–§5, with timestamps). GSAP eases are a
SYSTEM, not a menu: one default, one workhorse, one punch, one fun moment.

## The system

| Ease | Job | Execute |
|---|---|---|
| `power1.out` | THE DEFAULT — gently slows at the end | `gsap.to(el, {x: 300, duration: 1})` — no ease key needed; explicit: `ease: "power1.out"` |
| `power2.out` | THE WORKHORSE — standard smooth settle, most entrances | `ease: "power2.out", duration: 0.5` |
| `power4.out` | THE PUNCH — stronger snap, settles softly (hero headline / card snap) | `ease: "power4.out", duration: 0.8` |
| `power4.inOut` | Full travel — slow start, fast middle, slow end | `ease: "power4.inOut"` for moves across the frame |
| `back.out(1.4)` | ONE fun moment per video — overshoots slightly then settles (card pop) | `ease: "back.out(1.4)"` |
| `elastic.out(1, 0.5)` | ONE playful beat — wobbles like a spring before stopping | `ease: "elastic.out(1, 0.5)"` |

Number = strength: power1 soft → power4 really strong.

## Stagger

```js
gsap.from(".card", {y: 50, opacity: 0, duration: 0.8, ease: "power4.out", stagger: 0.1})
// card 2 starts 0.1s after card 1
// grid ripple from centre: stagger: {each: 0.05, from: "center", grid: "auto"}
// spread all starts across a fixed time: stagger: {amount: 2}  (6 items → starts spread over 2s)
```

## The rule underneath (from the harvest)

- Once people find elastic they put it on everything — don't. Back and
  elastic are one-moment-only, never the default.
- Vary the values: in video terms, vary punch-in 1.08–1.14, vary stagger
  0.06–0.10s, never the same zoom twice in a row (EASING.md §10, GSAP
  `gsap.utils.random` for size/drift with `curviness: 1.25` on MotionPath
  for organic float).
- PWC mapping: these are GSAP/render values for animation builds
  (HyperFrames/Remotion/CapCut keyframes). In CapCut, the equivalents are
  the 8 named motions in EASING.md (OVERSHOOT ≈ back.out, SPRING ≈
  elastic.out) — same jobs, same one-moment-only rule.

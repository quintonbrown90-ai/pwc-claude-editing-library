# EASING.md — the 8 motions, executable

Source: @viashaan "Describe Motion to AI" (PUBLISHED), as implemented in
`pwc-designed-captions/code/easings.py` (verified numerically — overshoot
peaks 1.141). Copy the Python or the CSS; both are the same curves.

## Python (easings.py — the reference implementation)

```python
def linear(t): return t
def ease_in(t): return t * t * t
def ease_out(t): return 1 - (1 - t) ** 3
def ease_in_out(t):
    return 4 * t**3 if t < 0.5 else 1 - (-2 * t + 2) ** 3 / 2
def overshoot(t, strength=1.70158):
    return 1 + (strength + 1) * (t - 1) ** 3 + strength * (t - 1) ** 2
def spring(t, stiffness=170.0, damping=16.0):
    import math
    w = math.sqrt(stiffness); d = damping / (2 * math.sqrt(stiffness))
    return 1 - math.exp(-d * w * t) * math.cos(w * math.sqrt(1 - d * d) * t)
def bounce(t):
    # piecewise quadratic rebounds; 0 at t=0, 1 at t=1 with 2 visible bounces
    if t < 0.3636: return 7.5625 * t * t
    if t < 0.7272:
        t -= 0.5454; return 7.5625 * t * t + 0.75
    if t < 0.9091:
        t -= 0.8182; return 7.5625 * t * t + 0.9375
    t -= 0.9545; return 7.5625 * t * t + 0.984375
def steps(t, n=6):
    import math
    return math.floor(t * n) / n
```

## CSS

| Motion | CSS |
|---|---|
| LINEAR | `linear` |
| EASE IN | `cubic-bezier(0.55,0.06,0.68,0.19)` |
| EASE OUT | `cubic-bezier(0.22,0.61,0.36,1)` |
| EASE IN-OUT | `cubic-bezier(0.65,0.05,0.36,1)` |
| OVERSHOOT | `cubic-bezier(0.34,1.56,0.64,1)` |
| SPRING | JS spring (stiffness 170, damping 16) |
| BOUNCE | JS bounce |
| STEPS | `steps(n, end)` |

## When to use which (house rule)

- Arriving → EASE OUT. Leaving → EASE IN (always faster than the entrance).
- Moving between two spots / drawing a line → EASE IN-OUT.
- Titles, buttons, pins, hero words → OVERSHOOT.
- Playful / stickers / chunky italics → SPRING. Drops → BOUNCE.
- Clocks, counters, type-on → STEPS.
- Machines only (spinners, tickers) → LINEAR. Nothing else moves on LINEAR.

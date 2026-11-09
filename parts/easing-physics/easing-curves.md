<!-- PART: easing-physics/easing-curves.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# EASING — the 8 curves, executable (PUBLISHED + verified)

Source: @viashaan motion vocabulary + `skills/pwc-designed-captions/code/easings.py`
(verified numerically — overshoot peaks 1.141). Full functions in
`skills/pwc-motion-playbooks/references/EASING.md`.

## The rule
Copy the Python or the CSS; both are the same curves. Never hand-tune a
curve per video — pick the named one that fits the job.

```python
def linear(t): return t
def ease_in(t): return t * t * t
def ease_out(t): return 1 - (1 - t) ** 3
def ease_in_out(t):
    return 4 * t**3 if t < 0.5 else 1 - (-2 * t + 2) ** 3 / 2
def overshoot(t, strength=1.70158):
    return 1 + (strength + 1) * (t - 1) ** 3 + strength * (t - 1) ** 2
def steps(t, n=6):
    import math
    return math.floor(t * n) / n
```

| Motion | CSS |
|---|---|
| LINEAR | `linear` |
| EASE IN | `cubic-bezier(0.55,0.06,0.68,0.19)` |
| EASE OUT | `cubic-bezier(0.22,0.61,0.36,1)` |
| EASE IN-OUT | `cubic-bezier(0.65,0.05,0.36,1)` |
| OVERSHOOT | `cubic-bezier(0.34,1.56,0.64,1)` |
| STEPS | `steps(n, end)` |

## Worked example
Caption phrase entrance: 4–7 frames, scale 92% → 103% → 100% (OVERSHOOT).
Card entrance: 8–12 frames EASE OUT. Exit: 5–6 frames EASE IN.

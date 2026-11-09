"""Motion vocabulary — the shared easing library for PWC caption + animation skills.

Every animated element in a PWC edit is specified with one of these NAMES
(from @viashaan's "Describe Motion to AI" system), never with a vague
"animate it". Each name maps to a real function here (Python), and to a
matching cubic-bezier / JS implementation in MOTION.md for HTML templates.

Usage: ease('overshoot', t) with t in 0..1 -> progress in 0..1 (may exceed 1
for overshoot/spring/bounce, which is the point).
"""
import math


def linear(t):
    return t


def ease_in(t):
    return t * t * t


def ease_out(t):
    return 1 - (1 - t) ** 3


def ease_in_out(t):
    return 4 * t * t * t if t < 0.5 else 1 - ((-2 * t + 2) ** 3) / 2


def overshoot(t, strength=1.70158):
    """Goes past the target, settles back. Titles, buttons, pins, pills."""
    s = strength * 1.25
    return 1 + (s + 1) * ((t - 1) ** 3) + s * ((t - 1) ** 2)


def spring(t, stiffness=170.0, damping=16.0):
    """Soft physical settle (damped harmonic). Feels real, not robotic."""
    if t <= 0:
        return 0.0
    if t >= 1:
        return 1.0
    w = math.sqrt(stiffness)
    z = damping / (2 * w)
    decay = math.exp(-z * w * t * 6.0)
    return 1 - decay * math.cos(w * math.sqrt(1 - z * z) * t * 6.0)


def bounce(t):
    """Hits the ground and rebounds. Drops, falling objects, playful landings."""
    n1, d1 = 7.5625, 2.75
    if t < 1 / d1:
        return n1 * t * t
    if t < 2 / d1:
        t -= 1.5 / d1
        return n1 * t * t + 0.75
    if t < 2.5 / d1:
        t -= 2.25 / d1
        return n1 * t * t + 0.9375
    t -= 2.625 / d1
    return n1 * t * t + 0.984375


def steps(t, n=6):
    """Fixed jumps, no blending. Clocks, counters, type-on, stop-motion."""
    if t >= 1:
        return 1.0
    return math.floor(t * n) / n


EASINGS = {
    'linear': linear,
    'ease_in': ease_in,
    'ease_out': ease_out,
    'ease_in_out': ease_in_out,
    'overshoot': overshoot,
    'spring': spring,
    'bounce': bounce,
    'steps': steps,
}

# CSS equivalents (for the HTML animation templates)
CSS = {
    'linear': 'linear',
    'ease_in': 'cubic-bezier(0.55, 0.06, 0.68, 0.19)',
    'ease_out': 'cubic-bezier(0.22, 0.61, 0.36, 1)',
    'ease_in_out': 'cubic-bezier(0.65, 0.05, 0.36, 1)',
    'overshoot': 'cubic-bezier(0.34, 1.56, 0.64, 1)',
    'spring': 'cubic-bezier(0.28, 0.84, 0.42, 1)',  # visual approximation
    'bounce': 'cubic-bezier(0.28, 0.84, 0.42, 1)',  # use JS bounce() for true bounce
    'steps': 'steps(6, end)',
}


def ease(name, t):
    fn = EASINGS.get(name, ease_out)
    return fn(max(0.0, min(1.0, t)))

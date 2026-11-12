#!/usr/bin/env python3
"""sky_easing.py — easing curves for Sky's motion, as executable functions.

Measured facts the curves encode (STYLE-GRAMMAR.md §5):
  * Caption IN is a HARD CUT to full size in <=1 frame (<=0.033 s @30fps) —
    no scale-in ramp. That is `step`, not an easing curve.
  * Caption OUT is ~0.5 s pop/fade.
  * Panel in: 7 frames, scale .88 -> 1 (blur-in cut Nov 9, Batch 19 — the
    measured pop is scale-only). Panel out: hard cut (measured; the
    slide-blur panel-out is cut). Child builds: 6 f on the spoken word, min
    stagger 3 f. No idle float — panels hold still once landed.
  * Graphic entrances generally: pop/scale ~0.3 s with slight overshoot.
  * Counter: count-up out_expo over 1 s.
  * Exact easing curves for graphic entrances are UNVERIFIED (4 fps frames
    cannot resolve them) — the defaults below are the documented choices
    (out_back with the pwc-motion-playbooks overshoot peak 1.141 for pops,
    power4.out / expo.out for arrivals per the HyperFrames motion reference),
    and every call site records which easing it used so a frame-grade can
    swap it. Nothing here pretends a guessed curve is a measurement.

All functions take t in [0, 1] and return a value in (roughly) [0, 1];
out_back overshoots to ~1.141 by design. `keyframes()` samples any easing
into the [{t, value}] lists the device builders and the HyperFrames /
CapCut emitters consume.
"""
from __future__ import annotations

import math

FPS = 30
FRAME = 1.0 / FPS  # 0.0333 s

# Measured / specified durations (seconds).
CAPTION_IN_FRAMES = 1        # hard cut, <=1 frame
CAPTION_OUT_S = 0.5
PANEL_IN_FRAMES = 7          # 0.233 s
PANEL_OUT_FRAMES = 7         # retained as a documented duration constant only;
                             # no builder uses it — panel-out is a hard cut (Batch 19)
CHILD_BUILD_FRAMES = 6       # 0.2 s
CHILD_MIN_STAGGER_FRAMES = 3  # 0.1 s
POP_S = 0.3                  # general graphic pop entrance
COUNT_UP_S = 1.0
OVERSHOOT_PEAK = 1.141       # pwc-motion-playbooks verified overshoot peak


def _clamp01(t: float) -> float:
    return 0.0 if t < 0.0 else 1.0 if t > 1.0 else t


def step(t: float) -> float:
    """Hard cut: 0 before the beat, 1 at/after it. The caption-in curve."""
    return 0.0 if t < 1.0 else 1.0


def linear(t: float) -> float:
    return _clamp01(t)


def ease_out_cubic(t: float) -> float:
    t = _clamp01(t)
    return 1.0 - (1.0 - t) ** 3


def ease_out_quart(t: float) -> float:
    """power4.out — HyperFrames arrival default for long-tailed landings."""
    t = _clamp01(t)
    return 1.0 - (1.0 - t) ** 4


def ease_out_expo(t: float) -> float:
    """expo.out — counters / count-ups and long arrivals."""
    t = _clamp01(t)
    return 1.0 if t >= 1.0 else 1.0 - 2.0 ** (-10.0 * t)


def ease_in_out_quad(t: float) -> float:
    t = _clamp01(t)
    return 2 * t * t if t < 0.5 else 1.0 - (-2 * t + 2) ** 2 / 2


def ease_out_back(t: float, overshoot: float = 1.70158) -> float:
    """back.out — pop/scale entrances with slight overshoot.

    Default c1=1.70158 gives the classic ~1.10 peak; pass
    overshoot=2.08 for a peak of ~1.141 (the pwc-motion-playbooks value,
    solved numerically — 2.2 overshoots to 1.154).
    """
    t = _clamp01(t)
    c3 = overshoot + 1.0
    return 1.0 + c3 * (t - 1.0) ** 3 + overshoot * (t - 1.0) ** 2


def ease_out_back_1141(t: float) -> float:
    """Pop with the verified 1.141 overshoot peak (c1=2.08, solved numerically)."""
    return ease_out_back(t, overshoot=2.08)


def spring(t: float, damping_ratio: float = 0.8, omega: float = 12.0) -> float:
    """Closed-form under-damped spring (deterministic, frame-seekable).

    damping 0.7-0.85 reads premium (HyperFrames motion reference);
    position/size may bounce, opacity/colour never do — so this is for
    scale/position only. Returns 1.0 at t=1 (settled) by construction of
    the caller clamping the last sample; intermediate values overshoot.
    """
    t = _clamp01(t)
    if damping_ratio >= 1.0:
        return 1.0 - math.exp(-omega * t) * (1.0 + omega * t)
    wd = omega * math.sqrt(1.0 - damping_ratio ** 2)
    env = math.exp(-damping_ratio * omega * t)
    return 1.0 - env * (math.cos(wd * t) + (damping_ratio / math.sqrt(1.0 - damping_ratio ** 2)) * math.sin(wd * t))


EASINGS = {
    "step": step,                    # hard cut — caption in, device exits
    "linear": linear,                # constant-velocity line draws, counters
    "ease_out_cubic": ease_out_cubic,
    "power4.out": ease_out_quart,    # arrivals (HyperFrames naming)
    "expo.out": ease_out_expo,       # count-ups, long arrivals
    "ease_in_out_quad": ease_in_out_quad,
    "back.out": ease_out_back,       # pop entrances (GSAP back.out(1.4) ~ this)
    "back.out_1.141": ease_out_back_1141,  # pop with verified 1.141 peak
    "spring_0.8": spring,            # premium pop, position/scale only
}


def get_easing(name: str):
    if name not in EASINGS:
        raise ValueError(f"unknown easing {name!r}; known: {sorted(EASINGS)}")
    return EASINGS[name]


def keyframes(easing: str, duration_s: float, n: int = 8,
              start: float = 0.0, end: float = 1.0) -> list[dict]:
    """Sample an easing into n+1 keyframes [{t_s, value}].

    t_s is absolute seconds from the motion start; value is the eased
    interpolation between start and end. The final sample is exactly `end`
    (land the end state just before the clip end — HyperFrames contract).
    """
    fn = get_easing(easing)
    out = []
    for i in range(n + 1):
        u = i / n
        out.append({"t_s": round(duration_s * u, 4),
                    "value": round(start + (end - start) * fn(u), 4)})
    out[-1]["value"] = end
    return out


def frames_to_s(frames: int) -> float:
    return round(frames / FPS, 4)


if __name__ == "__main__":
    for name, fn in EASINGS.items():
        vals = [round(fn(t / 4), 3) for t in range(5)]
        assert abs(fn(0.0)) < 1e-9 or name == "step", name
        # Springs approach 1.0 asymptotically; keyframes() clamps the final
        # sample to the end value, so 2e-3 here is the honest bound.
        tol = 2e-3 if name.startswith("spring") else 1e-6
        assert abs(fn(1.0) - 1.0) < tol, f"{name} does not settle at 1.0: {fn(1.0)}"
        print(f"  {name:18s} t=0,.25,.5,.75,1 -> {vals}")
    print("easing OK; 7f =", frames_to_s(7), "s; 6f =", frames_to_s(6), "s")

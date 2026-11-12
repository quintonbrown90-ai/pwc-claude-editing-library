#!/usr/bin/env python3
"""sky_palette.py — the ONE source of truth for colour in the Sky lane.

PWC law (absolute, outranks Sky everywhere it differs):
  teal  #14A886  = structure (titles, numerals, outlines, keep-verdicts)
  gold  #FEE238  = payoff   (figures, completed state, swapped power word)
  navy  #00214E  = ground
  white #FCFCFC  = captions / body text (pixel-sampled from Sky's own reels)
  NO red, NO neon green in anything added. Red that is IN Q's footage stays
  (it is footage, not a graphic); red in a reference remaps to gold.

Sky's own accents map to PWC by family, never emitted raw:
  Sky green #40BB2F (GREEN family) -> PWC teal  #14A886
  Sky orange #E8913F / ~#F09828 (ORANGE family) -> PWC gold #FEE238
  Sky red #E86A5E (negatives) -> strikethrough stays, X goes gold, check teal,
  rejects/dismissals go grey + strike/dim.

Every module in code/ imports its colours from here. Nothing hard-codes a
hex anywhere else. validate_*() is called by sky_build_plan.py and sky_qc.py
so a forbidden colour can never reach a plan, a HyperFrames composition, or
a CapCut build sequence.
"""
from __future__ import annotations

import re

# --- PWC brand palette (absolute) -------------------------------------------
TEAL = "#14A886"
GOLD = "#FEE238"
NAVY = "#00214E"
NAVY_DEEP = "#0A1633"   # dark-navy pill text ground (capcut_build_spec.md D3)
WHITE = "#FCFCFC"       # pixel-sampled caption white (Nov 9, 2026)
INK = "#060E30"         # glass plate ink component (6,22,48)
GREY_DIM = "#8A93A6"    # dismissed / past-era text (grey + strike/dim, never red)
GREY_MID = "#5A6373"

# --- Sky's own colours, for reference/remap ONLY — never emit as Q colours --
SKY_GREEN = "#40BB2F"   # neon green core (range #3DBB2C-#46C232, pixel-sampled)
SKY_ORANGE = "#E8913F"  # warm orange/gold (pixel-sampled Nov 9 ~#F09828)
SKY_ORANGE_SAMPLED = "#F09828"
SKY_RED = "#E86A5E"     # Sky negatives — NEVER emitted in Q's lane
SKY_GROUND = "#040404"  # Sky ground, near-black (range #040404-#0C1414)

PALETTE = {
    "teal": TEAL,
    "gold": GOLD,
    "navy": NAVY,
    "navy_deep": NAVY_DEEP,
    "white": WHITE,
    "ink": INK,
    "grey_dim": GREY_DIM,
    "grey_mid": GREY_MID,
}

# Sky accent -> PWC accent, by family. One accent per video, never mixed.
FAMILY_MAP = {
    "green": {"sky": SKY_GREEN, "pwc": TEAL, "role": "structure"},
    "orange": {"sky": SKY_ORANGE, "pwc": GOLD, "role": "payoff"},
}

# Hexes that must never appear in any generated plan / composition / draft.
FORBIDDEN_HEX = {
    SKY_RED.lower(), "#e86a5e",
    SKY_GREEN.lower(), "#40bb2f",
    "#3dbb2c", "#46c232",           # Sky green sampling range
    SKY_ORANGE.lower(), "#e8913f",
    SKY_ORANGE_SAMPLED.lower(), "#f09828",
    "#ff0000", "#e53935", "#ff3b30", "#00ff66", "#ffe600",
}
# Any red-dominant hex (R high, G and B low) is also forbidden unless it is
# explicitly flagged as footage (is_footage=True). See is_forbidden().
_HEX_RE = re.compile(r"^#([0-9a-fA-F]{6})$")


def normalize_hex(value: str) -> str:
    """'#14a886' -> '#14A886'. Raises ValueError on non-hex input."""
    value = value.strip()
    if not _HEX_RE.match(value):
        raise ValueError(f"not a 6-digit hex colour: {value!r}")
    return value.upper()


def is_forbidden(value: str, *, is_footage: bool = False) -> bool:
    """True if a colour must never be emitted as a graphic in Q's lane.

    Footage pixels are exempt: red that is IN Q's footage stays, it is not
    a graphic. Anything this function flags with is_footage=False is a
    hard error in the plan/QC gates.
    """
    if is_footage:
        return False
    try:
        hexv = normalize_hex(value).lower()
    except ValueError:
        return True  # unparseable colour strings are rejected too
    if hexv in FORBIDDEN_HEX:
        return True
    r, g, b = int(hexv[1:3], 16), int(hexv[3:5], 16), int(hexv[5:7], 16)
    # Red-dominant: strong red, weak green and blue (Sky's red, pure red,
    # and anything that would read as "red" on screen).
    if r >= 180 and g <= 110 and b <= 110:
        return True
    # Neon green: strong green, weak red and blue.
    if g >= 170 and r <= 110 and b <= 110:
        return True
    return False


def validate_color(value: str, *, where: str = "colour") -> str:
    """Return the normalised hex, or raise ValueError if forbidden."""
    if is_forbidden(value):
        raise ValueError(
            f"FORBIDDEN colour {value!r} in {where}: no red / neon green / "
            "Sky raw green-orange in Q's lane — remap via FAMILY_MAP "
            "(Sky green->teal #14A886, Sky orange->gold #FEE238, Sky red->gold X / grey strike)"
        )
    return normalize_hex(value)


def accent_for_family(family: str) -> str:
    """The single accent hex for a video's family ('green'->teal, 'orange'->gold)."""
    if family not in FAMILY_MAP:
        raise ValueError(f"family must be 'green' or 'orange', got {family!r}")
    return FAMILY_MAP[family]["pwc"]


def remap_sky_color(sky_hex: str) -> str:
    """Map one of Sky's own accent hexes to its PWC equivalent.

    Used when porting a measured Sky value (e.g. a node colour, a bar colour)
    into Q's lane. Unknown hexes raise — do not guess a remap.
    """
    table = {
        SKY_GREEN.lower(): TEAL,
        "#3dbb2c": TEAL, "#46c232": TEAL,
        SKY_ORANGE.lower(): GOLD,
        SKY_ORANGE_SAMPLED.lower(): GOLD,
        SKY_RED.lower(): GOLD,  # red X / red head -> gold (strikethrough stays)
        SKY_GROUND.lower(): NAVY,
        "#0c1414": NAVY,
    }
    key = sky_hex.strip().lower()
    if key not in table:
        raise ValueError(f"no PWC remap defined for Sky colour {sky_hex!r}")
    return table[key]


def scan_object_for_forbidden(obj, *, path: str = "$") -> list[str]:
    """Walk a plan/dict/list and return paths of any forbidden colour string.

    Only strings that look like a 6-digit hex are checked, so free text
    (framework names, captions) never trips this. Returns [] when clean.
    """
    hits: list[str] = []
    if isinstance(obj, str):
        if _HEX_RE.match(obj.strip()) and is_forbidden(obj):
            hits.append(f"{path}={obj}")
    elif isinstance(obj, dict):
        for k, v in obj.items():
            hits.extend(scan_object_for_forbidden(v, path=f"{path}.{k}"))
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            hits.extend(scan_object_for_forbidden(v, path=f"{path}[{i}]"))
    return hits


if __name__ == "__main__":
    # Smoke check: PWC palette passes, every Sky raw accent fails.
    for name, hexv in PALETTE.items():
        print(f"  ok {name:10s} {validate_color(hexv, where=name)}")
    for bad in (SKY_GREEN, SKY_ORANGE, SKY_ORANGE_SAMPLED, SKY_RED, "#FF0000", "#00FF66"):
        try:
            validate_color(bad, where="smoke test")
        except ValueError:
            print(f"  blocked (correct): {bad}")
        else:
            raise SystemExit(f"FAIL: forbidden colour passed: {bad}")
    print("palette OK")

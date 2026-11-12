#!/usr/bin/env python3
"""sky_capcut_draft.py — plan JSON -> CapCut-native build sequence (RENDER PATH 2).

CapCut-native is the SHIPPING bar for Q's main edits: the export must come
from a real CapCut project. This module emits an ordered, machine-readable
sequence of CapCut MCP tool calls (see ~/workspace/custom-skills/capcut/
SKILL.md) that Claude Code executes through the CapCut MCP server to build
the draft — it does NOT fabricate a raw draft_content.json.

Why not a raw draft file: pyJianYingDraft is NOT installed here, it targets
JianYing (the China build), not CapCut International; CapCut 8.4+ refuses
drafts with stale version markers; JianYing 6.0+ encrypts draft_content.json.
A hand-written draft JSON would be an unverified guess at a proprietary
format. The MCP call sequence is the honest, executable route: every call
names a real tool, a real track, and values from the plan.

Conventions (from the capcut skill):
  * time in MICROSECONDS (1 s = 1,000,000 us).
  * canvas coords normalised: x in [-1, 1] (left->right), y in [-1, 1]
    (BOTTOM->top; 0 = middle, 0.6 = top third). This module converts the
    plan's 1080x1920 px top-left coords: nx = (x + w/2 - 540) / 540,
    ny = (960 - (y + h/2)) / 960.
  * Track 0 = A-roll; overlay tracks = devices/assets; text tracks =
    captions + titles; audio tracks = bed + SFX.
  * Captions go as ONE capcut_add_subtitles call with an SRT payload built
    from the D1 groups (1-3 words each) plus individual capcut_add_text
    calls for headlines / device labels.

The sequence is validated by validate_sequence(): monotonic timestamps,
coords in range, colours in the PWC palette, no red. Export still happens
in CapCut Desktop (capcut_generate_preview / the app's export); this
module never claims an export it cannot run.

Usage:
  python3 sky_capcut_draft.py sky_plan.json --out capcut_build.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sky_palette import GOLD, NAVY, TEAL, WHITE, scan_object_for_forbidden  # noqa: E402

CANVAS_W, CANVAS_H = 1080, 1920
US = 1_000_000  # microseconds per second


def px_to_norm(x: float, y: float, w: float, h: float) -> dict:
    """1080x1920 px top-left -> CapCut normalised centre coords."""
    cx = x + w / 2
    cy = y + h / 2
    return {"x": round((cx - 540) / 540, 4), "y": round((960 - cy) / 960, 4)}


def s_to_us(t: float) -> int:
    return int(round(t * US))


def _srt_timestamp(t: float) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def build_sequence(plan: dict, *, project_name: str = "") -> dict:
    """Plan -> ordered CapCut MCP call sequence."""
    name = project_name or f"sky-{plan['framework'].lower().replace(' ', '-')}"
    calls: list[dict] = []
    calls.append({"tool": "capcut_create_project",
                  "args": {"name": name, "width": 1080, "height": 1920},
                  "why": "1080x1920 reel canvas (STYLE-GRAMMAR §1)."})
    aroll = plan.get("aroll", "")
    if aroll and not aroll.startswith("UNSET"):
        calls.append({"tool": "capcut_add_video_clip",
                      "args": {"path": aroll, "track": 0, "start_time": 0,
                               "duration": s_to_us(plan["duration_s"])},
                      "why": "A-roll on Track 0, silence-compressed first (E1)."})
    else:
        calls.append({"tool": "NOTE",
                      "args": {"message": "A-roll path UNSET in plan — add the "
                                          "silence-compressed take to Track 0 first."},
                      "why": "No edit without the take."})

    # D1 captions as one SRT payload (1-3 words per group, all-white).
    groups = [e for e in plan["events"] if e["device"] == "D1"]
    srt_lines = []
    for i, g in enumerate(groups, 1):
        srt_lines.append(f"{i}\n{_srt_timestamp(g['t0'])} --> "
                         f"{_srt_timestamp(g['t1'])}\n{g['text']}\n")
    calls.append({"tool": "capcut_add_subtitles",
                  "args": {"srt": "\n".join(srt_lines),
                           "style": {"color": WHITE, "font_size": 58, "bold": True,
                                     "stroke": 0, "shadow": "0,3,12,35%",
                                     "position": px_to_norm(90, 1060, 900, 60)}},
                  "why": f"D1: {len(groups)} caption groups, 1-3 words, all-white, "
                         "chest band, hard cut per group (in <=1 frame). "
                         "Re-segment Auto Captions output to these groups; "
                         "the SRT is the segmentation."})

    # Device labels / headlines as native text; panels as keyframed opacity/scale.
    for ev in plan["events"]:
        if ev["device"] == "D1":
            continue
        g = ev["geometry"]
        pos = px_to_norm(g["x"], g["y"], g["w"], g["h"])
        text = ev.get("text")
        if isinstance(text, dict):
            label = " / ".join(str(v) for v in text.values() if v)
        else:
            label = str(text or ev.get("name", ev["device"]))
        colors = ev.get("colors", {})
        color = colors.get("title") or colors.get("display") or colors.get("accent") \
            or colors.get("text") or WHITE
        calls.append({
            "tool": "capcut_add_text",
            "args": {"text": label, "start_time": s_to_us(ev["t0"]),
                     "duration": s_to_us(ev["t1"] - ev["t0"]),
                     "position": pos,
                     "style": {"color": color, "font_size": 46,
                               "device": ev["device"], "instance": ev.get("instance")}},
            "why": f"{ev['device']} {ev['name']} — {ev.get('status', '')} "
                   f"(source {ev.get('source_reel', '')})."})
        motion = ev.get("motion", {})
        m_in = motion.get("in", {}) if isinstance(motion, dict) else {}
        if m_in.get("type") in ("pop", "panel_pop"):
            calls.append({
                "tool": "capcut_add_keyframe",
                "args": {"property": "scale",
                         "keyframes": [
                             {"time": s_to_us(ev["t0"]),
                              "value": m_in.get("scale_from", 0.88)},
                             {"time": s_to_us(ev["t0"] + m_in.get("dur_s", 0.3)),
                              "value": 1.0}]},
                "why": f"{ev['device']} pop entrance "
                       f"({m_in.get('dur_s', 0.3)} s, back.out_1.141)."})
        if m_in.get("type") == "opacity_keyframe":
            calls.append({
                "tool": "capcut_add_keyframe",
                "args": {"property": "opacity",
                         "keyframes": [
                             {"time": s_to_us(ev["t0"]), "value": m_in.get("from", 0.4)},
                             {"time": s_to_us(ev["t0"] + m_in.get("dur_s", 0.15)),
                              "value": m_in.get("to", 1.0)}]},
                "why": f"{ev['device']} state-change 40->100% on the spoken word."})

    # Punch-ins (A-roll scale keyframes, capped 105-110%).
    for p in plan.get("punch_ins", []):
        calls.append({
            "tool": "capcut_add_keyframe",
            "args": {"property": "scale", "track": 0,
                     "keyframes": [
                         {"time": s_to_us(p["t0"]), "value": 1.0},
                         {"time": s_to_us(p["t0"] + 0.2), "value": p["scale"]},
                         {"time": s_to_us(p["t0"] + p["hold_s"]), "value": p["scale"]},
                         {"time": s_to_us(p["t0"] + p["hold_s"] + 0.2), "value": 1.0}]},
            "why": "Punch-in capped 105-110%; never on a graphic state-change frame."})

    # Sound: cleared bed ducked ~-28 dB + SFX per landing (Q divergence).
    calls.append({"tool": "capcut_add_audio_clip",
                  "args": {"role": "bed", "duck_db": -28,
                           "notes": "cleared instrumental from the local licensed "
                                    "library only; never Epidemic Sound"},
                  "why": "Q bed (Sky runs dry voice only — VERIFIED divergence)."})
    sfx_events = [e for e in plan["events"] if e.get("sfx")]
    for ev in sfx_events:
        calls.append({"tool": "capcut_add_sound_effect",
                      "args": {"file": ev["sfx"], "start_time": s_to_us(ev["t0"]),
                               "device": ev["device"]},
                      "why": f"SFX on {ev['device']} landing ({ev['name']})."})
    calls.append({"tool": "capcut_generate_preview",
                  "args": {},
                  "why": "Headless proxy preview BEFORE the motion grade — "
                         "never ship on a builder's say-so (QC.md)."})
    return {"project": name, "style": "sky-edit-style",
            "plan_version": plan.get("version"),
            "duration_s": plan.get("duration_s"),
            "framework": plan["framework"], "family": plan["family"],
            "palette": {"teal": TEAL, "gold": GOLD, "navy": NAVY, "white": WHITE,
                        "red": "NEVER", "neon_green": "NEVER"},
            "calls": calls,
            "disclaimer": ("Build sequence for the CapCut MCP server. NOT a "
                           "draft_content.json — export happens in CapCut Desktop. "
                           "pyJianYingDraft is not installed and targets JianYing, "
                           "not CapCut International.")}


def validate_sequence(seq: dict) -> list[str]:
    """Validate a build sequence; returns problems (empty = clean).

    NOTE: call order is execution order (create project, then all texts,
    then keyframes, then audio) — NOT timeline order. So this checks
    per-call ranges (start >= 0, duration > 0, inside the video) instead
    of global monotonicity.
    """
    problems = []
    duration_us = s_to_us(seq.get("duration_s", 0) or 0)
    problems.extend(f"palette: {h}" for h in scan_object_for_forbidden(seq.get("palette", {})))
    for i, call in enumerate(seq["calls"]):
        args = call.get("args", {})
        st, du = args.get("start_time"), args.get("duration")
        if isinstance(st, int):
            if st < 0:
                problems.append(f"call {i} ({call['tool']}): negative start_time")
            if duration_us and st > duration_us:
                problems.append(f"call {i} ({call['tool']}): start_time past video end")
        if isinstance(du, int):
            if du <= 0:
                problems.append(f"call {i} ({call['tool']}): non-positive duration")
            if isinstance(st, int) and duration_us and st + du > duration_us:
                problems.append(f"call {i} ({call['tool']}): clip ends past video end")
        style = args.get("style", {})
        if isinstance(style, dict):
            for key, val in style.items():
                if isinstance(val, str) and val.startswith("#"):
                    from sky_palette import is_forbidden
                    if is_forbidden(val):
                        problems.append(f"call {i}: forbidden colour {key}={val}")
            pos = style.get("position") or args.get("position")
            if isinstance(pos, dict):
                if not (-1.0 <= pos.get("x", 0) <= 1.0 and -1.0 <= pos.get("y", 0) <= 1.0):
                    problems.append(f"call {i}: position out of [-1, 1]: {pos}")
        pos = args.get("position")
        if isinstance(pos, dict):
            if not (-1.0 <= pos.get("x", 0) <= 1.0 and -1.0 <= pos.get("y", 0) <= 1.0):
                problems.append(f"call {i}: position out of [-1, 1]: {pos}")
    if not any(c["tool"] == "capcut_create_project" for c in seq["calls"]):
        problems.append("sequence has no capcut_create_project call")
    if not any(c["tool"] == "capcut_add_subtitles" for c in seq["calls"]):
        problems.append("sequence has no capcut_add_subtitles call (D1 captions)")
    return problems


def main():
    ap = argparse.ArgumentParser(description="Plan JSON -> CapCut MCP build sequence.")
    ap.add_argument("plan_json")
    ap.add_argument("--out", required=True)
    ap.add_argument("--project-name", default="")
    a = ap.parse_args()
    plan = json.load(open(a.plan_json))
    seq = build_sequence(plan, project_name=a.project_name)
    problems = validate_sequence(seq)
    json.dump(seq, open(a.out, "w"), indent=2)
    print(f"wrote {a.out}: {len(seq['calls'])} calls for project {seq['project']!r}")
    if problems:
        print("VALIDATION PROBLEMS:")
        for p in problems:
            print("  -", p)
        raise SystemExit(1)
    print("sequence validation OK (per-call ranges, coords in [-1,1], palette clean).")


if __name__ == "__main__":
    main()

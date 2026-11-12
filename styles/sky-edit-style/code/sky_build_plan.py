#!/usr/bin/env python3
"""sky_build_plan.py — v2 Sky plan generator (supersedes sky_plan_template.py).

Input : a words JSON file: [{"word": str, "start": float, "end": float}, ...]
        (word onsets from ASR; timings extracted AFTER any speed pass)
        + --framework / --parts / --family / --keyword / --model-reel
        + optional --devices JSON: per-part device assignment, e.g.
          {"1": ["D3", "D4"], "2": ["D6"], "3": ["D12"], "4": ["D14"]}
        + optional --hero D4|D5-list|D6|D12|D13 (default D4)
Output: a Sky plan v2 JSON: caption groups (D1, hard-cut in), a full event
        list (one event per device instance, with geometry, colours, motion
        keyframes, SFX), punch-ins, mid-video reset, sound plan, QC checklist.
        The plan is the input to sky_hyperframes.py (render) and
        sky_capcut_draft.py (CapCut-native build sequence). It does not
        render video itself.

Rules enforced here (fail loudly, never silently):
  * palette: every colour via sky_palette; forbidden colours rejected.
  * parts: 3-6 (4-5 sweet spot); one framework name, coined by Q.
  * variety: each device <= 2 uses per video (D1 captions exempt).
  * hook: framework name / result figure on screen within the first 10%
    of runtime; first graphic by f3-f12; >= 3 builds in the first 3 s.
  * close: hero device completes on the closing line; end moment <= 1 s
    after the last spoken word.
  * captions: 1-3 words/group, all-white, chest band, never over the face.

Stdlib only. Usage:
  python3 sky_build_plan.py words.json --framework "The Filter" \\
      --parts "Hook,Filter 1,Filter 2,Payoff" --family green \\
      --keyword WAITLIST --model-reel DfX2qwQGagM --out sky_plan.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sky_devices import (  # noqa: E402
    DEFAULT_FACE_BOX, d1_captions, d2_headline_lockup, d3_title_stack,
    d4_filter_board, d5_chapter_card, d5_checklist, d6_chart, d12_timeline,
    d13_workflow_strip, d14_end_beat, validate_beat_lock, validate_events,
)
from sky_palette import GOLD, NAVY, PALETTE, TEAL, accent_for_family  # noqa: E402

PLAN_VERSION = 2
MAX_DEVICE_USES = 2

# Default device assignment when --devices is not given: part 1 opens with
# the title stack + hero board, middle parts judge board rows, the last part
# closes with the end beat. The hero device is the ONE primary (D4 default).
DEFAULT_HERO = "D4"


def build_plan(words, *, framework, parts, family, keyword="WAITLIST",
               model_reel="", hero=DEFAULT_HERO, devices_map=None,
               hook_formula="H-B", aroll_path="", face_box=None):
    if not words:
        raise ValueError("empty words file")
    if not (3 <= len(parts) <= 6):
        raise ValueError(f"Sky frameworks use 3-6 parts (4-5 sweet spot); got {len(parts)}")
    accent = accent_for_family(family)  # raises on bad family
    face_box = dict(face_box or DEFAULT_FACE_BOX)
    # Layout is computed from the hairline (face top - 20 px), measured
    # Nov 9 from DfX2 @2.0 s (hair top ~y720/1920). The hero zone is
    # y300 -> hairline. A separate D3 title stack + pill needs a hero body
    # of >= 260 px below the pill (pill ends y466, body starts y480); when
    # the face is high there is no room, so the D3 title is OMITTED and the
    # hero's own title block carries the framework name — the DfX2 pattern
    # (funnel with its STRATEGY label inside it). Never stack title + pill +
    # hero into the face.
    hairline_y = face_box["y"] - 20
    chin_y = face_box["y"] + face_box["h"]
    caption_y = chin_y + 69   # chin + 40 px clearance + half the 58 px text
    # D2 headline top clears the caption band: caption clip bottom is
    # caption_y + 45 (58 px text + 16 px pad, centred on caption_y), +12 px
    # gap. Measured DfX2 headline top (chin+75) sits ~30 px higher, but in
    # the rendered frame the kicker strikes through the live caption glyphs
    # (verified Nov 9 snapshot) — clearance wins over the raw measurement.
    d2_y = caption_y + 57      # = chin + 126; display ends ~chin+282 (< 1480)
    # D3 title stack: only for heroes that do NOT carry their own title
    # (D4's board title, D5-list's checklist title, D12's node labels do),
    # and only when the hero body (>= 260 px) still fits below the pill.
    d3_present = hero in ("D5", "D6", "D13") and (hairline_y - 480 - 20) >= 260
    hero_top_y = 480 if d3_present else 320
    t_start = words[0]["start"]
    t_end = words[-1]["end"]
    duration = t_end - t_start
    if duration <= 0:
        raise ValueError("words file has zero/negative duration")

    events = []
    # D1 caption stream over the whole video (hard-cut in, ~0.5 s groups).
    events.extend(d1_captions(words, y=caption_y,
                              source_reel=model_reel or "DfX2qwQGagM"))

    # Hook headline (D2 lockup) lands WITH the first spoken line.
    events.extend(d2_headline_lockup(
        t_start, kicker="the framework", display_lines=[framework],
        family=family, y=d2_y, source_reel=model_reel or "DfX2qwQGagM"))

    # Part boundaries: equal split of the spoken duration is the DEFAULT;
    # replace with real part timings (from the script's part markers) when
    # known — the plan records which mode was used.
    n = len(parts)
    boundaries = [t_start + duration * i / n for i in range(n + 1)]

    # D3 title stack ONCE, pills swapping per part (one instance) — only
    # when the hero body still fits below it (see layout rule above).
    swap_s = round(duration / n, 2)
    if d3_present:
        events.extend(d3_title_stack(t_start, title=framework, sections=parts,
                                     family=family, swap_s=swap_s,
                                     source_reel=model_reel or "DfQ4E1Hjn0n"))

    # Hero device: ONE instance spanning the video, filling part by part.
    # (A board that fills IS the open loop — it is not rebuilt per part.)
    events.extend(_build_hero(hero, t_start, boundaries, parts,
                              family=family, model_reel=model_reel,
                              framework=framework,
                              hairline_y=hairline_y, top_y=hero_top_y))

    # Extra per-part devices from --devices (not D1/D2/D3/D14/hero — those
    # are already placed above). Each extra is one instance at its part start.
    devices_map = devices_map or {}
    for i, part in enumerate(parts):
        for dev in devices_map.get(str(i + 1), []):
            if dev in ("D1", "D2", "D3", "D14", hero):
                raise ValueError(
                    f"part {i + 1}: {dev} is already placed by the plan "
                    "(D1 captions, D2 hook, D3 title stack, hero, D14 close) — "
                    "assign a different device here")
            events.extend(_build_device(dev, boundaries[i], boundaries[i + 1],
                                        part, i + 1, n, family=family,
                                        model_reel=model_reel,
                                        hairline_y=hairline_y,
                                        top_y=hero_top_y))

    # Punch-ins: keyframed A-roll scale at the definition line, each part's
    # verdict line, and the close — capped at 105-110%, returning to 100%
    # at the next section boundary. Sky's own zoom is mild, ~5-10% MAX.
    punch_ins = []
    for i in range(n):
        punch_ins.append({
            "t0": round(boundaries[i], 3),
            "scale": 1.08, "hold_s": 1.25,
            "notes": "punch-in capped 105-110%; never on a graphic state-change frame",
        })

    # Mid-video reset at 45-55% of runtime.
    mid_reset = {"t0": round(t_start + duration * 0.5, 3),
                 "type": "pivot headline + second-act chart state",
                 "notes": "E7: pivot headline, the chart's second act, a document "
                          "reveal, or a branch."}

    # Close: end beat on the closing line; hold 0.8-1.5 s; end moment <= 1 s
    # after the last spoken word. D14 fires ONCE, at the close.
    close_t = t_end
    events.extend(d14_end_beat(max(t_start, close_t - 1.2), close_line=f"Comment {keyword}",
                               keyword=keyword, hold_s=1.2,
                               top_y=hero_top_y, hairline_y=hairline_y,
                               source_reel=model_reel or ""))

    # Beat lock (SKY v6, BEAT-LOCK-SPEC.md): events placed by the plan's
    # equal-split DEFAULT boundaries are not on the word grid by
    # construction — stamp the stated reason instead of landing off-beat
    # by accident. Real part markers replace the defaults (and the reasons).
    _onsets = [w["start"] for w in words]
    for ev in events:
        if ev["device"] == "D1":
            continue
        if min((abs(ev["t0"] - o) for o in _onsets), default=99) > 1 / 30:
            ev.setdefault("off_beat_reason",
                          "plan DEFAULT boundary (equal split of spoken duration) "
                          "— replace with real script part markers; deliberate, "
                          "not accidental (BEAT-LOCK-SPEC)")
    problems = validate_events(events)
    problems += validate_beat_lock(events, words)
    # Variety rule is a hard error here (validate_events already flags it).
    if problems:
        raise ValueError("plan failed validation:\n" + "\n".join(f"  - {p}" for p in problems))

    plan = {
        "version": PLAN_VERSION,
        "style": "sky-edit-style", "trigger": "edit in Sky style",
        "profile": "https://www.instagram.com/realskytan",
        "framework": framework, "family": family,
        "accent": accent,
        "accent_role": "structure (teal)" if family == "green" else "payoff (gold)",
        "palette": {**PALETTE, "red": "NEVER", "neon_green": "NEVER"},
        "keyword": keyword,
        "keyword_flow_live": "UNVERIFIED — confirm the ManyChat flow is live before posting",
        "model_reel": model_reel or "UNSET — name the ONE model reel",
        "hook_formula": hook_formula,
        "hero_device": hero,
        "face_box": face_box,
        "layout": {"hairline_y": hairline_y, "chin_y": chin_y,
                   "caption_y": caption_y, "headline_y": d2_y,
                   "hero_top_y": hero_top_y,
                   "d3_title_stack": ("present — hero body fits below the pill"
                                      if d3_present else
                                      "OMITTED — " + (
                                          "hero carries its own title (D4 board / "
                                          "D5-list checklist / D12 node labels)"
                                          if hero in ("D4", "D5-list", "D12") else
                                          "face too high for title + pill + hero; "
                                          "the hero's own title block carries the "
                                          "framework name (DfX2 pattern)")),
                   "hero_zone": f"y{hero_top_y} -> y{hairline_y}",
                   "advisory": ("D2 headline block ends past the y1480 safe-zone "
                                "bottom — Sky-measured behaviour (DfX2 block "
                                "y~1245-1575/1920); the frame audit decides per take, "
                                "it is not a plan failure.")},
        "duration_s": round(duration, 2),
        "t_start": round(t_start, 3), "t_end": round(t_end, 3),
        "aroll": aroll_path or "UNSET — path to the silence-compressed A-roll",
        "parts": [{"index": i + 1, "of": n, "name": p,
                   "t0": round(boundaries[i], 3), "t1": round(boundaries[i + 1], 3),
                   "devices": [d for d in
                               (["D3"] if (i == 0 and d3_present) else []) + [hero] +
                               (["D14"] if i == n - 1 else []) +
                               (devices_map.get(str(i + 1)) or [])]}
                  for i, p in enumerate(parts)],
        "part_boundaries": "equal split of spoken duration (DEFAULT) — replace "
                           "with real script part markers when known",
        "caption_groups": [{"text": g["text"], "t0": g["t0"], "t1": g["t1"]}
                           for g in _caption_groups_only(events)],
        "word_grid": [{"word": w["word"], "start": w["start"], "end": w["end"]}
                      for w in words],
        "events": events,
        "punch_ins": punch_ins,
        "mid_video_reset": mid_reset,
        "hook": {"rule": "framework name or result figure on screen within the "
                         "first 10% of runtime; first graphic by f3-f12; >=3 builds "
                         "in the first 3s; frame one = Q talking",
                 "deadline_s": round(t_start + duration * 0.10, 3)},
        "close": {"rule": "complete the hero device on the closing line; hold "
                          "0.8-1.5s; spoken door over the completed graphic; "
                          "logo/keyword end moment <=1s after the last word",
                  "last_word_s": round(t_end, 3),
                  "end_moment_deadline_s": round(t_end + 1.0, 3)},
        "sound": {"voice_lufs": -14.5, "bed_db": -28,
                  "sfx": "sound on every device landing AND exit; stamp on "
                         "verdicts (Q divergence, SKY-PLUS target — Sky's own "
                         "base is dry voice + the measured tick-tone family on "
                         "counters/timers/count-ups/chart draws, Batch 36)",
                  "bed_source": "local cleared library only; never Epidemic Sound"},
        "qc": ["frame-sequence motion grade vs model reel",
               "freezedetect zero >=0.35s (code/qc_freezedetect.sh)",
               "±0.15s entrance/exit audits", "last-word to end-card <=1s",
               "lip-sync offsets", "per-word fit (one clipped word = FAIL)",
               "no-overlap every frame", "full self-watch",
               "run: python3 code/sky_qc.py <plan.json>"],
        "build": ("HyperFrames render: python3 code/sky_hyperframes.py <plan.json> ; "
                  "CapCut-native build: python3 code/sky_capcut_draft.py <plan.json>. "
                  "ffmpeg/PIL plates do NOT count as a CapCut-born style."),
    }
    return plan


def _caption_groups_only(events):
    return [e for e in events if e["device"] == "D1"]


def _build_hero(hero, t_start, boundaries, parts, *, family, model_reel,
                framework="Framework", hairline_y=700, top_y=320):
    """One hero instance spanning the whole video, filling part by part."""
    n = len(parts)
    part_dur = round((boundaries[-1] - boundaries[0]) / n, 2)
    if hero == "D4":
        return d4_filter_board(
            t_start, board_title=framework,
            rows=[{"label": p, "verdict": "approve"} for p in parts],
            family=family, row_gap_s=part_dur, hairline_y=hairline_y,
            top_y=top_y, source_reel=model_reel or "DfX2qwQGagM")
    if hero == "D5":
        events = []
        for i, p in enumerate(parts):
            card = d5_chapter_card(
                boundaries[i], numeral=i + 1, name=p,
                definition=f"Part {i + 1} of {n}.", family=family,
                hold_s=part_dur, top_y=top_y, hairline_y=hairline_y,
                source_reel=model_reel or "")
            # One chapter-card SET = one device instance (like one board's rows).
            for ev in card:
                ev["instance"] = f"D5@{t_start:.2f}"
            events.extend(card)
        return events
    if hero == "D5-list":
        return d5_checklist(t_start, title=framework, items=parts,
                            family=family, hairline_y=hairline_y,
                            top_y=top_y, source_reel=model_reel or "DfQ4E1Hjn0n")
    if hero == "D6":
        return d6_chart(
            t_start, title=framework,
            annotations=[{"label": p, "value": "", "payoff": i == n - 1}
                         for i, p in enumerate(parts)],
            family=family, top_y=top_y, hairline_y=hairline_y,
            source_reel=model_reel or "DfPxqFPAY4_")
    if hero == "D12":
        return d12_timeline(
            t_start,
            nodes=[{"label": p, "current": i == n - 1} for i, p in enumerate(parts)],
            family=family, source_reel=model_reel or "De-A2dvCeV3")
    if hero == "D13":
        return d13_workflow_strip(t_start, steps=parts, family=family,
                                  step_gap_s=part_dur, top_y=top_y + 60,
                                  source_reel=model_reel or "DfQ4E1Hjn0n")
    raise ValueError(f"unknown hero device {hero!r}")


def _build_device(dev, p0, p1, part, index, total, *, family, model_reel,
                  hairline_y=700, top_y=320):
    """Build one extra (non-hero, non-D1/D2/D3/D14) device instance for a part."""
    if dev == "D4":
        return d4_filter_board(p0, board_title=part,
                               rows=[{"label": part, "verdict": "approve"}],
                               family=family, row_gap_s=round(p1 - p0, 2),
                               hairline_y=hairline_y, top_y=top_y,
                               source_reel=model_reel or "DfX2qwQGagM")
    if dev == "D5":
        return d5_chapter_card(p0, numeral=index, name=part,
                               definition=f"Part {index} of {total}.",
                               family=family, hold_s=round(p1 - p0, 2),
                               top_y=top_y, hairline_y=hairline_y,
                               source_reel=model_reel or "")
    if dev == "D5-list":
        return d5_checklist(p0, title=part, items=[part], family=family,
                            hairline_y=hairline_y, top_y=top_y,
                            source_reel=model_reel or "DfQ4E1Hjn0n")
    if dev == "D6":
        return d6_chart(p0, title=part,
                        annotations=[{"label": part, "value": "", "payoff": index == total}],
                        family=family, top_y=top_y, hairline_y=hairline_y,
                        source_reel=model_reel or "DfPxqFPAY4_")
    if dev == "D12":
        return d12_timeline(p0, nodes=[{"label": part, "current": index == total}],
                            family=family, source_reel=model_reel or "De-A2dvCeV3")
    if dev == "D13":
        return d13_workflow_strip(p0, steps=[part], family=family,
                                  step_gap_s=round(p1 - p0, 2), top_y=top_y + 60,
                                  source_reel=model_reel or "DfQ4E1Hjn0n")
    raise ValueError(
        f"unknown/unsupported device {dev!r} for plan generation. Supported here: "
        "D4, D5, D5-list, D6, D12, D13. All other devices (D7-D11, D15-D25) are "
        "built by calling their sky_devices functions directly with their own "
        "parameters — see code/README.md.")


def main():
    ap = argparse.ArgumentParser(description="Generate a Sky plan v2 JSON from words + framework.")
    ap.add_argument("words_json")
    ap.add_argument("--framework", required=True)
    ap.add_argument("--parts", required=True, help="comma-separated framework parts (3-6)")
    ap.add_argument("--family", choices=["green", "orange"], required=True)
    ap.add_argument("--keyword", default="WAITLIST")
    ap.add_argument("--model-reel", default="")
    ap.add_argument("--hero", default=DEFAULT_HERO,
                    choices=["D4", "D5", "D5-list", "D6", "D12", "D13"])
    ap.add_argument("--devices", default="",
                    help='JSON map part->devices, e.g. \'{"1":["D3","D6"],"2":["D12"]}\'')
    ap.add_argument("--hook-formula", default="H-B", choices=["H-A", "H-B", "H-C", "H-D"])
    ap.add_argument("--aroll", default="")
    ap.add_argument("--face-box", default="",
                    help="x,y,w,h in 1080x1920 px (default: DfX2-measured 345,720,390,450)")
    ap.add_argument("--out", default="sky_plan.json")
    a = ap.parse_args()

    words = json.load(open(a.words_json))
    parts = [p.strip() for p in a.parts.split(",") if p.strip()]
    devices_map = json.loads(a.devices) if a.devices else None
    face_box = None
    if a.face_box:
        x, y, w, h = (int(v) for v in a.face_box.split(","))
        face_box = {"x": x, "y": y, "w": w, "h": h}
    plan = build_plan(words, framework=a.framework, parts=parts, family=a.family,
                      keyword=a.keyword, model_reel=a.model_reel, hero=a.hero,
                      devices_map=devices_map, hook_formula=a.hook_formula,
                      aroll_path=a.aroll, face_box=face_box)
    json.dump(plan, open(a.out, "w"), indent=2)
    print(f"wrote {a.out}: {len(plan['caption_groups'])} caption groups, "
          f"{len(plan['events'])} events, {len(parts)} parts, family={a.family}, "
          f"hero={a.hero}, duration={plan['duration_s']}s")


if __name__ == "__main__":
    main()

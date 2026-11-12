#!/usr/bin/env python3
"""sky_hyperframes.py — plan JSON -> HyperFrames composition (RENDER PATH 1).

This is the PRIMARY executable render path in Claude Code: a Sky plan
becomes a deterministic HyperFrames project (HTML + one paused GSAP root
timeline per composition) that `npx hyperframes render` turns into video.

HyperFrames contract (from ~/workspace/tools/hyperframes/AGENTS.md and the
/hyperframes skill — read it first in Claude Code):
  * compositions are HTML with data-* attributes; clips need class="clip",
    data-start + data-duration in seconds, showing over [start, start+dur).
  * one paused GSAP root timeline per composition, on window.__timelines.
  * NEVER animate visibility/display/autoAlpha on a .clip element — the
    framework manages clip visibility. GSAP targets an INNER div inside
    each clip (this module's structure); only opacity/scale/filter/x/y/
    clipPath are tweened, on the inner div.
  * deterministic rendering: NO Date.now(), NO unseeded Math.random(),
    NO network fetches for media. GSAP itself loads from the framework's
    whitelisted CDN (jsdelivr, gsap@3.15.0) via a <script> tag in
    index.html — the compiler inlines it; that is the sanctioned pattern,
    not a media fetch.
  * validate with `npx hyperframes lint` and `npx hyperframes check`.
  * use fromTo, not from, inside a scene (the host re-seeks on seek-back).

Sky motion in HyperFrames terms (all VERIFIED, no whip smears — Sky's
verified motion is hard cuts + eased panel/line draws + static charts with
stacking annotations; gl-transition WhipTilt/PopIn ports are NOT applied):
  * D1 captions: hard cut in (inner opacity 0 -> 1 exactly at t0, no ramp)
    + 0.5 s pop/fade out ending at t1. No scale-in ramp — the in is a step.
  * Panels/boards: scale 0.88 -> 1 over 7 frames (0.233 s), no blur
    (blur-in cut Nov 9, Batch 19), back.out easing (GSAP back.out(1.4)
    ~= back.out_1.141).
  * Chart: static SVG base present from t0; annotations pop in ~0.3 s each.
  * Timeline (D12): full-width line present from t0; nodes pop ~0.5 s apart.
  * Exits: hard cut (the clip window simply ends) unless the device says
    motion-blur slide out.
  * B&W beat (D21): full-frame div with backdrop-filter grayscale(1) +
    the hero word in gold — desaturates the frame beneath it.

Structure: devices live in compositions/sky.html; the D1 caption stream
lives in compositions/captions.html (data-track-kind="captions") so no
single timeline gets too dense. Both mount from index.html.

What this does NOT do: it does not supply the A-roll. The plan's `aroll`
path is mounted as the <video> element when given; without it the project
renders the graphics over the navy ground so motion can still be graded
frame by frame (graphics-only grade). Face tracking / RVM matte is a
pre-render step (matte.py in the old engine is gone — see GAPS.md G-10);
this emitter places graphics in the face-clear zones from the plan and
never over the face box.

Usage:
  python3 sky_hyperframes.py sky_plan.json --out /tmp/sky_hf_test
  python3 sky_hyperframes.py sky_plan.json --out /tmp/sky_hf_test --check-only
  cd /tmp/sky_hf_test && npx hyperframes lint && npx hyperframes check
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sky_palette import GOLD, NAVY, TEAL, WHITE  # noqa: E402

GSAP_VERSION = "3.15.0"  # HyperFrames' pinned version (packages/core/src/gsapCdn.ts)
GSAP_SRC = f"https://cdn.jsdelivr.net/npm/gsap@{GSAP_VERSION}/dist/gsap.min.js"
FORBIDDEN_TOKENS = ("Date.now", "Math.random", "fetch(", "autoAlpha")
ALLOWED_URLS = (GSAP_SRC,)
ESC = html.escape


def _event_clip(ev: dict, idx: int) -> str:
    """One plan event -> outer .clip (timing only) + inner div (GSAP target).

    The outer div carries class="clip" + data-start/data-duration and is
    NEVER touched by GSAP (lint rule gsap_animates_clip_element). All
    styling and all animation live on the inner div, which starts at
    opacity:0 so a hard cut is a set to opacity:1 at exactly t0.
    """
    g = ev["geometry"]
    dev = ev["device"]
    el_id = f"sky-{dev.lower()}-{idx}"
    text = ev.get("text")
    label = _label_text(ev, text)
    inner_html = _label_html(dev, text, label)
    colors = ev.get("colors", {})
    fg = colors.get("text") or colors.get("title") or colors.get("display") or WHITE
    accent = colors.get("accent") or TEAL
    bg_raw = colors.get("card") or colors.get("board") or colors.get("chip_fill")
    bg_alpha = colors.get("card_opacity", colors.get("board_opacity",
                           colors.get("chip_fill_opacity", 1.0)))
    bg = _rgba(bg_raw, bg_alpha) if bg_raw else "transparent"
    if dev == "D21":
        # B&W beat: full-frame backdrop desaturation + the hero word in gold.
        inner_style = (
            "position:absolute;inset:0;display:flex;align-items:center;"
            "justify-content:center;"
            f"backdrop-filter:grayscale(1) contrast(1.1);-webkit-backdrop-filter:grayscale(1) contrast(1.1);"
            f"color:{GOLD};font-size:200px;font-weight:800;"
        )
    elif dev == "D1":
        inner_style = (
            "position:absolute;inset:0;display:flex;align-items:center;"
            "justify-content:center;"
            "font-size:58px;font-weight:700;text-align:center;"
            "text-shadow:0 3px 12px rgba(0,0,0,0.35);"
            f"color:{_css_color(fg)};"
        )
    elif dev == "D14":
        # End beat: an opaque card over the completed hero zone, flex
        # centred. (Before this branch the close line was top-aligned with
        # a transparent background and landed on the board's title row.)
        inner_style = (
            "position:absolute;inset:0;display:flex;align-items:center;"
            "justify-content:center;border-radius:24px;"
            f"background:{NAVY};border:2px solid {TEAL};"
            "font-size:64px;font-weight:800;text-align:center;"
            f"color:{_css_color(fg)};"
        )
    elif dev == "D2":
        inner_style = (
            "position:absolute;inset:0;text-align:center;"
            "font-size:110px;font-weight:800;"
            f"color:{_css_color(fg)};"
        )
    elif dev in ("D4", "D6", "D12", "D15", "D24"):
        # Short clips (board rows, chips <= 80 px tall) get flex vertical
        # centering; tall panels (the board itself) keep top-aligned text.
        flex = "display:flex;align-items:center;" if g["h"] <= 80 else ""
        inner_style = (
            "position:absolute;inset:0;border-radius:24px;"
            f"{flex}"
            f"background:{_css_color(bg)};border:2px solid {accent}66;"
            f"padding:20px;font-size:40px;color:{_css_color(fg)};"
        )
    elif dev == "D3":
        inner_style = (
            "position:absolute;inset:0;text-align:center;"
            f"font-size:46px;font-weight:800;color:{accent};"
        )
    else:
        inner_style = (
            "position:absolute;inset:0;text-align:center;"
            f"font-size:40px;font-weight:700;color:{_css_color(fg)};"
        )
    return (
        f'    <div id="{el_id}" class="clip sky-{dev.lower()}" '
        f'data-start="{ev["t0"]}" data-duration="{round(ev["t1"] - ev["t0"], 3)}" '
        f'data-track-index="{_track_index(ev["track"])}" '
        f'style="left:{g["x"]}px;top:{g["y"]}px;width:{g["w"]}px;height:{g["h"]}px;">\n'
        f'      <div id="{el_id}-in" class="sky-inner" style="{inner_style}">'
        f'{inner_html}</div>\n'
        f'    </div>\n'
    )


def _flat(value) -> str:
    """Flatten a text value (str or list of str) to one string."""
    if isinstance(value, list):
        return " ".join(str(v) for v in value if v)
    return str(value or "")


def _label_text(ev: dict, text) -> str:
    """Plain-text label for a plan event. Dict texts render per device:
    D2 headline = kicker + display; D14 end beat = close_line only."""
    if isinstance(text, dict):
        if ev["device"] == "D2":
            parts = [text.get("kicker", ""), _flat(text.get("display"))]
            return " ".join(p for p in parts if p)
        if ev["device"] == "D14":
            return str(text.get("close_line") or text.get("ending") or "")
        return " ".join(_flat(v) for v in text.values() if v)
    return str(text or ev.get("name", ev["device"]))


def _label_html(dev: str, text, label: str) -> str:
    """Inner-div HTML. D2 gets a small kicker line above the big display;
    everything else is the escaped plain label."""
    if dev == "D2" and isinstance(text, dict) and text.get("display"):
        kicker = ESC(str(text.get("kicker", "")))
        display = "<br>".join(ESC(str(v)) for v in text["display"])
        kick = (f'<div style="font-size:34px;font-weight:700;'
                f'letter-spacing:0.12em;text-transform:uppercase;'
                f'color:{WHITE};opacity:0.85;margin-bottom:12px;">{kicker}</div>'
                if kicker else "")
        return f"{kick}<div>{display}</div>"
    if dev == "D14" and isinstance(text, dict) and text.get("close_line"):
        # "Comment WAITLIST": lead-in white, keyword in gold.
        line = str(text["close_line"])
        kw = str(text.get("keyword") or "")
        if kw and kw in line:
            head, _, tail = line.partition(kw)
            return (f"{ESC(head)}<span style=\"color:{GOLD};\">{ESC(kw)}</span>"
                    f"{ESC(tail)}")
        return ESC(line)
    return ESC(label)


def _css_color(hexv: str) -> str:
    return hexv


def _rgba(hexv: str, alpha: float) -> str:
    """Hex + opacity -> rgba() string (glass panels: board 65%, chip 60%)."""
    h = hexv.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"


def _track_index(track: str) -> int:
    return {"track0": 0, "overlay1": 1, "overlay2": 2, "overlay3": 3,
            "overlay4": 4, "logo": 5}.get(track, 1)


def _gsap_for_event(ev: dict, idx: int) -> str:
    """GSAP fromTo lines for one event, targeting the INNER div only."""
    el = f"#sky-{ev['device'].lower()}-{idx}-in"
    t0 = ev["t0"]
    t1 = ev["t1"]
    motion = ev.get("motion", {})
    lines = []
    if ev["device"] == "D1":
        # Caption IN = hard cut: inner opacity 0 -> 1 exactly at t0, no ramp.
        # OUT = ~0.5 s pop/fade ENDING at t1 (the clip window ends at t1).
        # The out is clamped to 60% of the group's own life: Sky's groups
        # change every ~0.5 s, so a fixed 0.5 s out would start BEFORE the
        # in-set on short groups (lint: overlapping_gsap_tweens).
        dur = t1 - t0
        out_dur = round(min(0.5, dur * 0.6), 3)
        lines.append(f'    tl.set("{el}", {{opacity: 1}}, {t0});')
        lines.append(
            f'    tl.to("{el}", {{opacity: 0, scale: 0.96, duration: {out_dur}, '
            f'ease: "power4.out"}}, {round(t1 - out_dur, 3)});')
        return "\n".join(lines)
    m_in = motion.get("in", {})
    dur = m_in.get("dur_s", 0.3)
    if m_in.get("type") == "hard_cut":
        lines.append(f'    tl.set("{el}", {{opacity: 1}}, {t0});')
    elif m_in.get("type") in ("pop", "panel_pop"):
        scale_from = m_in.get("scale_from", 0.88)
        lines.append(
            f'    tl.fromTo("{el}", {{opacity: 0, scale: {scale_from}, '
            f'filter: "blur({m_in.get("blur_from_px", 0)}px)"}}, '
            f'{{opacity: 1, scale: 1, filter: "blur(0px)", duration: {dur}, '
            f'ease: "back.out(1.4)"}}, {t0});')
    elif m_in.get("type") == "opacity_keyframe":
        lines.append(
            f'    tl.fromTo("{el}", {{opacity: {m_in.get("from", 0.4)}}}, '
            f'{{opacity: {m_in.get("to", 1.0)}, duration: {dur}, '
            f'ease: "power3.out"}}, {t0});')
    elif m_in.get("type") in ("line_draw", "bar_fill"):
        lines.append(
            f'    tl.fromTo("{el}", {{opacity: 0, clipPath: "inset(0 100% 0 0)"}}, '
            f'{{opacity: 1, clipPath: "inset(0 0% 0 0)", duration: {dur}, '
            f'ease: "power2.out"}}, {t0});')
    elif m_in.get("type") == "desaturate":
        lines.append(f'    tl.set("{el}", {{opacity: 1}}, {t0});')
    else:
        # Hard cut is the default (Batch 19: slide_up / slide_left entrances
        # are CUT as generic slide-ins — any slide_* in-motion falls through
        # here to a plain opacity set at t0).
        lines.append(f'    tl.set("{el}", {{opacity: 1}}, {t0});')
    # Out: hard cut is the default (the clip window simply ends);
    # motion-blur slide outs get a short tween ending exactly at t1.
    # (Batch 19: the slide_blur_out panel-out branch is CUT — panels exit
    # by hard cut; motion_blur_slide stays, it is the measured thumbnail /
    # exhibit exit.)
    m_out = motion.get("out", {})
    if isinstance(m_out, dict) and m_out.get("type") == "motion_blur_slide":
        lines.append(
            f'    tl.to("{el}", {{x: 60, opacity: 0, duration: {m_out.get("dur_s", 0.3)}, '
            f'ease: "power3.in"}}, {round(t1 - m_out.get("dur_s", 0.3), 3)});')
    return "\n".join(lines)


def _scene_file(comp_id: str, events: list[dict], duration: float, *,
                track_kind: str = "", aroll_tag: str = "") -> str:
    clips = "".join(_event_clip(ev, i) for i, ev in enumerate(events))
    gsap = "\n".join(_gsap_for_event(ev, i) for i, ev in enumerate(events))
    kind_attr = f' data-track-kind="{track_kind}"' if track_kind else ""
    # Scene roots are TRANSPARENT and carry no background. The navy ground
    # lives on the MAIN root in index.html only. A scene root with an opaque
    # background paints over every sibling scene mounted before it (verified
    # Nov 9: the captions root's navy background hid the entire sky scene,
    # and `check` reported the sky texts as text_occluded).
    # The root id is "<comp>-root": host and root must NOT share an id
    # (assembled-page ids must be unique), and two scenes must not both be
    # id="root".
    return f"""<template>
  <style>
    #{comp_id}-root {{ position: absolute; inset: 0; overflow: hidden;
                     font-family: Inter, Arial, sans-serif; }}
    .clip {{ position: absolute; box-sizing: border-box; }}
    .sky-inner {{ opacity: 0; }}
    #sky-aroll {{ position: absolute; inset: 0; width: 1080px; height: 1920px; object-fit: cover; }}
    .sky-d1 {{ font-family: Inter, Arial, sans-serif; }}
  </style>
  <div id="{comp_id}-root" data-composition-id="{comp_id}" data-width="1080" data-height="1920"{kind_attr}>
{aroll_tag}{clips}  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
{gsap}
    window.__timelines["{comp_id}"] = tl;
  </script>
</template>
"""


def build_project(plan: dict, out_dir: Path, *, aroll_src: str = "") -> Path:
    """Write a HyperFrames project from a plan. Returns the project dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "compositions").mkdir(exist_ok=True)
    (out_dir / "assets").mkdir(exist_ok=True)
    duration = plan["duration_s"]
    framework = plan["framework"]
    events = plan["events"]
    captions = [e for e in events if e["device"] == "D1"]
    devices = [e for e in events if e["device"] != "D1"]
    aroll = aroll_src or plan.get("aroll", "")
    aroll_tag = ""
    if aroll and not aroll.startswith("UNSET"):
        aroll_tag = (
            f'    <video id="sky-aroll" class="clip" data-start="0" '
            f'data-duration="{duration}" src="assets/aroll.mp4"></video>\n'
        )
    (out_dir / "compositions" / "sky.html").write_text(
        _scene_file("sky", devices, duration, aroll_tag=aroll_tag))
    (out_dir / "compositions" / "captions.html").write_text(
        _scene_file("captions", captions, duration, track_kind="captions"))
    index = f"""<html data-composition-variables='[{{"id":"framework","type":"string","label":"Framework","default":"{ESC(framework)}"}}]'>
  <head>
    <script src="{GSAP_SRC}"></script>
    <style>
      html, body {{ margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: {NAVY}; }}
      #root {{ position: relative; width: 1080px; height: 1920px; background: {NAVY}; }}
    </style>
  </head>
  <body>
    <div
      id="root"
      data-composition-id="main"
      data-start="0"
      data-duration="{duration}"
      data-width="1080"
      data-height="1920"
    >
      <div
        id="sky"
        data-composition-id="sky"
        data-composition-src="compositions/sky.html"
        data-start="0"
        data-duration="{duration}"
        data-track-index="1"
        data-width="1080"
        data-height="1920"
      ></div>
      <div
        id="captions"
        data-composition-id="captions"
        data-composition-src="compositions/captions.html"
        data-start="0"
        data-duration="{duration}"
        data-track-index="4"
        data-track-kind="captions"
        data-width="1080"
        data-height="1920"
      ></div>
    </div>
    <script>
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""
    (out_dir / "index.html").write_text(index)
    (out_dir / "README.md").write_text(
        f"# Sky HyperFrames render — {framework}\n\n"
        f"Generated from a Sky plan v{plan.get('version')} "
        f"({plan.get('family')} family, hero {plan.get('hero_device')}, "
        f"{len(events)} events, {duration}s).\n\n"
        "Render: `npx hyperframes lint && npx hyperframes check` then "
        "`npx hyperframes render` (see /hyperframes-cli). A-roll: copy the "
        "silence-compressed take to `assets/aroll.mp4` first — without it "
        "the graphics render over the navy ground for a graphics-only grade.\n\n"
        "**NOT YET GRADED** — no frame-sequence grade has passed for this "
        "style (see QC.md §6). Do not call this output 'exact'.\n")
    return out_dir


def validate_project(out_dir: Path) -> list[str]:
    """Structural check without the CLI: clips, timelines, determinism."""
    problems = []
    index = (out_dir / "index.html").read_text()
    scene = (out_dir / "compositions" / "sky.html").read_text()
    captions = (out_dir / "compositions" / "captions.html").read_text()
    for token in FORBIDDEN_TOKENS:
        if token in index or token in scene or token in captions:
            problems.append(f"forbidden non-deterministic token present: {token}")
    for text, name in ((index, "index.html"), (scene, "sky.html"), (captions, "captions.html")):
        for m in re.finditer(r"https?://[^\s\"'<>]+", text):
            if m.group(0) not in ALLOWED_URLS:
                problems.append(f"non-allowlisted URL in {name}: {m.group(0)}")
    if GSAP_SRC not in index:
        problems.append("index.html does not load the pinned GSAP script")
    for comp_id, text in (("sky", scene), ("captions", captions)):
        if f'window.__timelines["{comp_id}"]' not in text:
            problems.append(f"{comp_id} has no window.__timelines['{comp_id}'] root timeline")
        if "gsap.timeline({ paused: true })" not in text:
            problems.append(f"{comp_id} timeline is not a paused GSAP timeline")
        clips = re.findall(r'class="clip[^"]*"[^>]*data-start="([\d.]+)"[^>]*data-duration="([\d.]+)"', text)
        if not clips:
            problems.append(f"{comp_id}: no .clip elements with data-start/data-duration found")
        for i, (st, du) in enumerate(clips):
            if float(du) <= 0:
                problems.append(f"{comp_id} clip {i}: non-positive data-duration {du}")
        if "autoAlpha" in text:
            problems.append(f"{comp_id}: autoAlpha present (banned on .clip elements)")
    if 'window.__timelines["main"]' not in index:
        problems.append("index has no window.__timelines['main'] root timeline")
    return problems


def main():
    ap = argparse.ArgumentParser(description="Render a Sky plan to a HyperFrames project.")
    ap.add_argument("plan_json")
    ap.add_argument("--out", required=True)
    ap.add_argument("--aroll", default="", help="A-roll file to copy to assets/aroll.mp4")
    ap.add_argument("--check-only", action="store_true",
                    help="build, then run the structural validator and exit")
    a = ap.parse_args()
    plan = json.load(open(a.plan_json))
    out_dir = Path(a.out)
    build_project(plan, out_dir)
    if a.aroll:
        import shutil
        shutil.copy(a.aroll, out_dir / "assets" / "aroll.mp4")
        print(f"copied A-roll -> {out_dir / 'assets' / 'aroll.mp4'}")
    problems = validate_project(out_dir)
    print(f"wrote HyperFrames project to {out_dir} "
          f"({len(plan['events'])} events, {plan['duration_s']}s)")
    if problems:
        print("VALIDATION PROBLEMS:")
        for p in problems:
            print("  -", p)
        raise SystemExit(1)
    print("structural validation OK (clips + timelines + determinism). "
          "Run `npx hyperframes lint && npx hyperframes check` in the project dir.")
    if a.check_only:
        return


if __name__ == "__main__":
    main()

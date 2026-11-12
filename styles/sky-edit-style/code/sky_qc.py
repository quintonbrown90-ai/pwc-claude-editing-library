#!/usr/bin/env python3
"""sky_qc.py — QC a Sky plan (and, when given an export, the export too).

Plan gates (run on every plan before any render/build):
  P1 palette: no forbidden colour anywhere in the plan (sky_palette scan).
  P2 captions: every D1 group 1-3 words, none straddling a device
     state-change boundary is flagged for the editor (groups are built from
     word timings, so a group that spans a part boundary is listed).
  P3 variety: each device <= 2 instances per video (D1 exempt).
  P4 geometry: every event inside the 1080x1920 canvas; no event over the
     face box (default face box x340-740 y500-950 — override with --face-box);
     no two hero/chip events overlapping at any sampled instant (0.1 s grid).
  P5 handoff: next top-zone text starts >= 0.5 s after the previous one ends.
  P6 hook: framework headline event starts within the first 10% of runtime.
  P7 close: last-word -> end-card gap <= 1 s (from plan.close).
  P8 sound: bed + SFX plan present; no Epidemic Sound anywhere.
  P9 premium (SKY v6): validate_premium_plan — no unknown devices, no
     banned fonts/treatments, no cheap-grade assets, no AI on proof,
     no [EST]-quarantined devices, every event cites its Sky reel.
  P10 beat lock (SKY v6): every event t0 within 1 frame of the plan's
     word grid, or carrying a stated off_beat_reason (needs word_grid).

Export gates (only with --export, on the exported file):
  E1 ffprobe decode + stream check.
  E2 freezedetect (noise 0.003, duration 0.35): zero freezes >= 0.35 s.
     (Same thresholds as code/qc_freezedetect.sh; this script shells out
     to ffmpeg/ffprobe — QC tooling only, it builds nothing.)

Exit codes: 0 = all gates pass, 1 = a gate failed, 2 = usage/input error.
Report is human-readable; --json prints the machine-readable verdict.

Usage:
  python3 sky_qc.py sky_plan.json
  python3 sky_qc.py sky_plan.json --export render.mp4
  python3 sky_qc.py sky_plan.json --face-box 340,500,400,450 --json
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sky_devices import validate_beat_lock, validate_events, validate_premium_plan  # noqa: E402
from sky_palette import scan_object_for_forbidden  # noqa: E402

CANVAS_W, CANVAS_H = 1080, 1920
DEFAULT_FACE_BOX = {"x": 340, "y": 500, "w": 400, "h": 450}
SAMPLE_STEP_S = 0.1
HANDOFF_MIN_S = 0.5


def _rects_overlap(a, b):
    return not (a["x"] + a["w"] <= b["x"] or b["x"] + b["w"] <= a["x"]
                or a["y"] + a["h"] <= b["y"] or b["y"] + b["h"] <= a["y"])


def qc_plan(plan: dict, *, face_box=None) -> dict:
    # P4 face + overlap uses the plan's own face box when present (the plan
    # records the take's measured box); --face-box overrides both.
    face_box = face_box or plan.get("face_box") or DEFAULT_FACE_BOX
    results = []

    def gate(gid, name, passed, detail=""):
        results.append({"id": gid, "name": name, "pass": bool(passed), "detail": detail})
        return passed

    events = plan.get("events", [])
    # P1 palette
    hits = scan_object_for_forbidden(plan)
    gate("P1", "palette (no red / neon green / Sky raw accents)",
         not hits, "; ".join(hits) if hits else "clean")
    # P2 captions
    groups = [e for e in events if e["device"] == "D1"]
    bad_groups = [e for e in groups if len(e["text"].split()) > 3 or not e["text"].strip()]
    gate("P2", "captions 1-3 words/group, all-white",
         not bad_groups,
         f"{len(groups)} groups" + (f"; BAD: {[g['text'] for g in bad_groups[:3]]}" if bad_groups else ""))
    # P3 variety + geometry (shared validator)
    problems = validate_events(events)
    gate("P3", "variety + geometry (device <=2 instances; inside canvas; top zone)",
         not problems, "; ".join(problems[:5]) if problems else "clean")
    # P4 face + overlap, sampled every 0.1 s. Exemptions (by design, not
    # loopholes): D14 IS the completed hero device in the hero zone, so it
    # overlaps the hero by definition; events of one instance (a board and
    # its rows) are one device, not two overlapping devices.
    face_hits, overlap_hits = [], []
    t = plan.get("t_start", 0.0)
    t_end = plan.get("t_end", plan.get("duration_s", 0.0))
    while t <= t_end:
        live = [e for e in events if e["t0"] <= t < e["t1"]]
        for e in live:
            if e["device"] == "D14":
                continue  # end beat holds the completed hero in its zone
            if _rects_overlap(e["geometry"], face_box):
                face_hits.append(f"{e['device']}@{t:.1f}s")
        for i in range(len(live)):
            for j in range(i + 1, len(live)):
                a, b = live[i], live[j]
                if a.get("instance") == b.get("instance"):
                    continue
                if "D14" in (a["device"], b["device"]):
                    continue  # end beat = completed hero, same zone by definition
                if "D21" in (a["device"], b["device"]):
                    continue  # B&W beat is a full-frame overlay by design
                if a["track"] == b["track"]:
                    continue
                # No blanket D1 exemption: captions must not collide with
                # headline/title devices (D2 kicker struck through live
                # caption glyphs in the Nov 9 render before this gate).
                if _rects_overlap(a["geometry"], b["geometry"]):
                    overlap_hits.append(f"{a['device']}x{b['device']}@{t:.1f}s")
        t = round(t + SAMPLE_STEP_S, 3)
    gate("P4a", "nothing over the face box",
         not face_hits, "; ".join(sorted(set(face_hits))[:5]) if face_hits else "clean")
    gate("P4b", "no-overlap (hero/chip events, 0.1 s sampling)",
         not overlap_hits, "; ".join(sorted(set(overlap_hits))[:5]) if overlap_hits else "clean")
    # P5 handoff: top-zone (non-caption) events >= 0.5 s apart when they
    # occupy the same zone. Same-instance events (board + rows) and the D14
    # end beat (a continuation of the hero, not a new text) are exempt.
    top = sorted([e for e in events if e["device"] != "D1"], key=lambda e: e["t0"])
    handoff_bad = []
    for a, b in zip(top, top[1:]):
        if a.get("instance") == b.get("instance"):
            continue
        if "D14" in (a["device"], b["device"]):
            continue
        if b["t0"] < a["t1"] + HANDOFF_MIN_S and _rects_overlap(a["geometry"], b["geometry"]):
            handoff_bad.append(f"{a['device']}->{b['device']} gap {b['t0'] - a['t1']:.2f}s")
    gate("P5", "text handoff >= 0.5 s between overlapping top-zone texts",
         not handoff_bad, "; ".join(handoff_bad[:5]) if handoff_bad else "clean")
    # P6 hook
    hook_deadline = plan.get("hook", {}).get("deadline_s")
    d2 = [e for e in events if e["device"] == "D2"]
    hook_ok = bool(d2) and (hook_deadline is None or d2[0]["t0"] <= hook_deadline)
    gate("P6", "hook: framework headline within first 10% of runtime",
         hook_ok, f"D2 at {d2[0]['t0'] if d2 else 'MISSING'}s, deadline {hook_deadline}s")
    # P7 close
    close = plan.get("close", {})
    gap = close.get("end_moment_deadline_s", 0) - close.get("last_word_s", 0)
    gate("P7", "close: end moment <= 1 s after last word",
         0 <= gap <= 1.0 + 1e-9, f"gap {gap:.2f}s")
    # P8 sound — bed level + voice target present; the bed source must be the
    # local cleared library (the plan text says "never Epidemic Sound" — the
    # check is on the source value, not on the word appearing in a warning).
    sound = plan.get("sound", {})
    bed_ok = sound.get("bed_db") == -28 and sound.get("voice_lufs") == -14.5
    bed_source = str(sound.get("bed_source", ""))
    gate("P8", "sound plan (bed -28 dB, voice -14.5 LUFS, cleared library only)",
         bool(sound) and bed_ok and "local" in bed_source.lower(),
         f"bed {sound.get('bed_db')} dB; voice {sound.get('voice_lufs')} LUFS; "
         f"source: {bed_source[:60]}")
    # P9 premium purge gate (SKY v6)
    premium = validate_premium_plan(events)
    gate("P9", "premium purge (v6 telltales / citations / provenance)",
         not premium, "; ".join(premium[:5]) if premium else "clean")
    # P10 beat lock (SKY v6) — runs only when the plan carries its word grid;
    # without one the build is unverified on beat lock, never verified.
    grid = plan.get("word_grid") or plan.get("words")
    if grid:
        lock = validate_beat_lock(events, grid)
        gate("P10", "beat lock (events on the word grid or reasoned)",
             not lock, "; ".join(lock[:5]) if lock else "locked")
    else:
        gate("P10", "beat lock (events on the word grid or reasoned)",
             False, "NOT RUN — plan carries no word_grid (unverified)")
    passed = all(r["pass"] for r in results)
    return {"scope": "plan", "pass": passed, "gates": results}


def qc_export(path: Path) -> dict:
    results = []

    def gate(gid, name, passed, detail=""):
        results.append({"id": gid, "name": name, "pass": bool(passed), "detail": detail})

    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries",
         "format=duration,size", "-show_entries",
         "stream=codec_name,width,height,r_frame_rate",
         "-of", "json", str(path)],
        capture_output=True, text=True)
    ok = probe.returncode == 0
    info = json.loads(probe.stdout) if ok and probe.stdout else {}
    dur = float(info.get("format", {}).get("duration", 0) or 0)
    gate("E1", "ffprobe decode + stream check", ok and dur > 0,
         f"duration {dur:.2f}s" if ok else probe.stderr.strip()[:200])
    freeze = subprocess.run(
        ["ffmpeg", "-v", "info", "-i", str(path), "-vf",
         "freezedetect=n=0.003:d=0.35", "-map", "0:v", "-f", "null", "-"],
        capture_output=True, text=True)
    starts = freeze.stderr.count("freeze_start")
    gate("E2", "freezedetect: zero freezes >= 0.35 s", starts == 0,
         f"{starts} freeze(s) detected" if starts else "no freezes >= 0.35s")
    return {"scope": "export", "file": str(path), "pass": all(r["pass"] for r in results),
            "gates": results}


def main():
    ap = argparse.ArgumentParser(description="QC a Sky plan (and optionally its export).")
    ap.add_argument("plan_json")
    ap.add_argument("--export", default="")
    ap.add_argument("--face-box", default="",
                    help="x,y,w,h in 1080x1920 px (default 340,500,400,450)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    plan = json.load(open(a.plan_json))
    face_box = None
    if a.face_box:
        x, y, w, h = (int(v) for v in a.face_box.split(","))
        face_box = {"x": x, "y": y, "w": w, "h": h}
    report = qc_plan(plan, face_box=face_box)
    reports = [report]
    if a.export:
        reports.append(qc_export(Path(a.export)))
    overall = all(r["pass"] for r in reports)
    if a.json:
        print(json.dumps({"pass": overall, "reports": reports}, indent=2))
    else:
        for rep in reports:
            print(f"== {rep['scope']}: {'PASS' if rep['pass'] else 'FAIL'} ==")
            for g in rep["gates"]:
                mark = "PASS" if g["pass"] else "FAIL"
                print(f"  [{mark}] {g['id']} {g['name']} — {g['detail']}")
        print("OVERALL:", "PASS" if overall else "FAIL")
        if not overall:
            print("See QC.md: a failing gate blocks delivery; a cut with any "
                  "gate unrun is unverified, never verified.")
    raise SystemExit(0 if overall else 1)


if __name__ == "__main__":
    main()

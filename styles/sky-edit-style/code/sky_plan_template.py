#!/usr/bin/env python3
"""sky_plan_template.py — generate a Sky plan JSON from a word-level transcript.

Inputs: a words JSON file: [{"word": str, "start": float, "end": float}, ...]
        (word onsets from ASR; timings extracted AFTER any speed pass)
        + --framework "Name" + --parts "Part 1,Part 2,Part 3" + --family green|orange
        + --keyword WAITLIST (must have a live ManyChat flow before posting)
Output: a Sky plan JSON (device schedule, caption groups, QC checklist).
This generates a PLAN. It does not render video. The plan is built in CapCut
natively per code/capcut_build_spec.md. Stdlib only.
Usage:
  python3 sky_plan_template.py words.json --framework "The Filter" \
      --parts "Hook,Filter 1,Filter 2,Payoff" --family green --keyword WAITLIST
"""
import argparse, json, sys

def caption_groups(words, max_words=3, max_chars=14):
    groups, cur = [], []
    for w in words:
        cur.append(w)
        text = " ".join(x["word"] for x in cur)
        if len(cur) >= max_words or len(text) >= max_chars or w["word"].endswith((".", ",", "?", "!")):
            groups.append({"text": text, "t0": cur[0]["start"], "t1": cur[-1]["end"]})
            cur = []
    if cur:
        groups.append({"text": " ".join(x["word"] for x in cur), "t0": cur[0]["start"], "t1": cur[-1]["end"]})
    return groups

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("words_json")
    ap.add_argument("--framework", required=True)
    ap.add_argument("--parts", required=True, help="comma-separated framework parts")
    ap.add_argument("--family", choices=["green", "orange"], required=True)
    ap.add_argument("--keyword", default="WAITLIST")
    ap.add_argument("--model-reel", default="", help="shortcode of the ONE model reel, e.g. DfX2qwQGagM")
    ap.add_argument("--out", default="sky_plan.json")
    a = ap.parse_args()
    words = json.load(open(a.words_json))
    if not words:
        sys.exit("empty words file")
    parts = [p.strip() for p in a.parts.split(",") if p.strip()]
    if not (3 <= len(parts) <= 6):
        print("WARNING: Sky frameworks use 3-6 parts (4-5 is the sweet spot); got", len(parts), file=sys.stderr)
    dur = words[-1]["end"]
    n = len(parts)
    schedule = []
    for i, part in enumerate(parts):
        t0 = words[0]["start"] + (dur - words[0]["start"]) * i / n
        schedule.append({"part": part, "index": i + 1, "of": n, "t0": round(t0, 2),
                         "device": "D4 board row" if i else "D3 title stack + D4 board",
                         "state": "pending 40% -> active 100% on first spoken word of the part",
                         "source_reel": a.model_reel or "UNSET — name the ONE model reel"})
    plan = {
        "style": "sky-edit-style", "trigger": "edit in Sky style",
        "profile": "https://www.instagram.com/realskytan",
        "framework": a.framework, "family": a.family,
        "accent": "#14A886 teal (structure)" if a.family == "green" else "#FEE238 gold (payoff)",
        "palette": {"teal": "#14A886", "gold": "#FEE238", "navy": "#00214E", "red": "NEVER", "neon_green": "NEVER"},
        "keyword": a.keyword, "keyword_flow_live": "UNVERIFIED — confirm the ManyChat flow is live before posting",
        "model_reel": a.model_reel or "UNSET",
        "duration_s": round(dur, 2),
        "devices": schedule,
        "caption_groups": caption_groups(words),
        "caption_rule": "1-3 words per group, all-white, bare text, chest band, chin +40px, inside x70-930 y280-1480, never over the face",
        "hook": "framework name or result figure on screen within the first 10% of runtime; first graphic by f3-f12; >=3 builds in the first 3s; frame one = Q talking",
        "close": "complete the hero device on the closing line; hold 0.8-1.5s; spoken door over the completed graphic; logo/keyword end moment <=1s after the last word",
        "qc": ["frame-sequence motion grade vs model reel", "freezedetect zero >=0.35s",
               "±0.15s entrance/exit audits", "last-word to end-card <=1s", "lip-sync offsets",
               "per-word fit (one clipped word = FAIL)", "no-overlap every frame", "full self-watch"],
        "build": "CapCut-native only, per code/capcut_build_spec.md. ffmpeg/PIL plates do NOT count.",
    }
    json.dump(plan, open(a.out, "w"), indent=2)
    print(f"wrote {a.out}: {len(plan['caption_groups'])} caption groups, {len(schedule)} parts, family={a.family}")

if __name__ == "__main__":
    main()

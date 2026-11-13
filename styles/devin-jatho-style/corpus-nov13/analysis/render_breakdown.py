#!/usr/bin/env python3
"""Usage: render_breakdown.py SEGMENTS_JSON
SEGMENTS_JSON schema: {code,title,fmt,dur,fps,dims,posted,likes,comments,url,
 segs:[[start,end,visual,caption,transition,sound,broll,bg], ...]} (broll/bg may be null)
Reads analysis/<code>_analysis.json (+words) and writes breakdowns/BREAKDOWN-<code>.md
with device table, B-ROLL LOG, BACKGROUND LOG, sound summary, 0.5s grid."""
import json, os, sys

ROOT = "/home/hatch/workspace/your_files/devin-exact-nov13"
ANA = os.path.join(ROOT, "analysis"); OUT = os.path.join(ROOT, "breakdowns")

def load_words(path):
    if not path or not os.path.exists(path): return []
    d = json.load(open(path)); ws = d["words"] if isinstance(d, dict) else d
    out = []
    for w in ws:
        s = w.get("s", w.get("start")); e = w.get("e", w.get("end"))
        if s is None: continue
        out.append((float(s), float(e), (w.get("w") or "").strip()))
    return out

meta = json.load(open(sys.argv[1])); code = meta["code"]
an = json.load(open(os.path.join(ANA, f"{code}_analysis.json")))
words = load_words(an.get("words_json"))
prof = an["rms_0.1s"]; onsets = set(an["onset_candidates"]); cuts = an["scene_cuts_gt_0.35"]
segs = [tuple(s) for s in meta["segs"]]
def seg_at(t):
    for s in segs:
        if s[0] <= t < s[1]: return s
    return segs[-1]
L = []
L.append(f"# BREAKDOWN — {code} — \"{meta['title']}\" **[Q-SUPPLIED priority set]**")
L.append("")
L.append(f"- **URL:** {meta['url']}  |  **Posted:** {meta['posted']}  |  **Engagement at pull:** {meta['likes']} likes / {meta['comments']} comments")
L.append(f"- **File:** `videos/devinjatho_{code}.mp4` — {meta['dims']}, {meta['fps']}fps, {meta['dur']}s")
L.append(f"- **Format:** {meta['fmt']}")
L.append("- **Method:** faster-whisper word timings + ffmpeg scene detection (gt(scene,0.35) — a LOWER bound on cuts) + 0.1s RMS profile with onset candidates. Visual states from a 1fps frame read (+ the library DECODE where one exists). Segment boundaries ±0.5s unless a row says MEASURED. Semantic SFX identities are NOT claimed from RMS alone.")
L.append("")
L.append("## Device / segment table")
L.append("")
L.append("| # | Time | Visual (asset-level) | Caption / text | Transition in | Sound |")
L.append("|---:|---|---|---|---|---|")
for i, s in enumerate(segs, 1):
    L.append(f"| {i} | {s[0]:.1f}–{s[1]:.1f}s | {s[2].replace('|','/')} | {s[3].replace('|','/')} | {s[4].replace('|','/')} | {s[5].replace('|','/')} |")
L.append("")
L.append("## B-ROLL LOG (Devin / subject inserts — separate system)")
L.append("")
brolls = [s for s in segs if len(s) > 6 and s[6]]
if brolls:
    L.append("| Time | B-roll insert |")
    L.append("|---|---|")
    for s in brolls: L.append(f"| {s[0]:.1f}–{s[1]:.1f}s | {s[6].replace('|','/')} |")
else:
    L.append("No B-roll inserts of Devin or a subject in this reel (see segment table).")
L.append("")
L.append("## BACKGROUND LOG (keying / placement / behind-vs-over)")
L.append("")
bgs = [s for s in segs if len(s) > 7 and s[7]]
if bgs:
    L.append("| Time | Background treatment |")
    L.append("|---|---|")
    for s in bgs: L.append(f"| {s[0]:.1f}–{s[1]:.1f}s | {s[7].replace('|','/')} |")
else:
    L.append("No keyed/replaced-background or behind-presenter graphic treatments in this reel — graphics sit beside/over the footage or replace the frame outright (see segment table).")
L.append("")
L.append("## Sound summary (measured)")
L.append("")
dur = meta["dur"]
L.append(f"- Duration {dur}s. Onset candidates (0.1s RMS jumps >2x and >=0.09): **{len(onsets)}** = {len(onsets)/dur*10:.1f} per 10s — includes word onsets; an UPPER bound on designed SFX, not an SFX count.")
sil = an["silences_lt_-38dB_min0.25s"]
L.append(f"- Silence spans (<-38dBFS-ish RMS 0.012, >=0.25s): {len(sil)} {sil if sil else ''}")
L.append(f"- Scene cuts at gt(scene,0.35): {len(cuts)} at {cuts} — lower bound (see method note).")
L.append("")
L.append("## 0.5-SECOND GRID")
L.append("")
L.append("| t | Spoken words | Visual state | Caption on screen | Audio (RMS mean/max in bin) | Events |")
L.append("|---:|---|---|---|---|---|")
t = 0.0; prev = None
while t < dur:
    seg = seg_at(t)
    bw = " ".join(w[2] for w in words if t <= w[0] < t + 0.5)
    idx = [prof[i] for i in range(int(t * 10), min(len(prof), int(t * 10) + 5))]
    rms = f"{sum(idx)/len(idx):.2f}/{max(idx):.2f}" if idx else "—"
    ev = []
    if any(t <= o < t + 0.5 for o in onsets): ev.append("onset candidate")
    if any(t <= c < t + 0.5 for c in cuts): ev.append("SCENE CUT (gt0.35)")
    if idx and max(idx) < 0.012: ev.append("near-silence bin")
    if seg is not prev:
        ev.append("SEGMENT IN: " + seg[4]); prev = seg
    vis = seg[2][:110] + ("…" if len(seg[2]) > 110 else "")
    cap = seg[3][:80] + ("…" if len(seg[3]) > 80 else "")
    L.append(f"| {t:.1f} | {bw.replace('|','/')} | {vis.replace('|','/')} | {cap.replace('|','/')} | {rms} | {'; '.join(ev)} |")
    t = round(t + 0.5, 1)
L.append("")
L.append(f"Companion evidence: `analysis/{code}_analysis.json` (full RMS series, cut list, onsets).")
open(os.path.join(OUT, f"BREAKDOWN-{code}.md"), "w").write("\n".join(L) + "\n")
print(code, "rows", int(dur * 2), "broll", len(brolls), "bg", len(bgs))

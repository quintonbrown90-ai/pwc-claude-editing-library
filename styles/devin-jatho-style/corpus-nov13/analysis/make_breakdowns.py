#!/usr/bin/env python3
"""Render BREAKDOWN-<code>.md per priority reel: header, device table,
B-ROLL LOG, transition inventory, sound summary, and the 0.5s grid.
Grid columns: time | spoken words (faster-whisper) | visual state (segment map)
| caption on screen | audio: RMS mean/max per bin, onset candidates, scene-cut
flags (ffmpeg gt(scene,0.35)), silence flag. Evidence tiers stay labelled."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from segment_maps import MAPS

ROOT = "/home/hatch/workspace/your_files/devin-exact-nov13"
ANA = os.path.join(ROOT, "analysis")
OUT = os.path.join(ROOT, "breakdowns")

def load_words(path):
    if not path or not os.path.exists(path):
        return []
    d = json.load(open(path))
    ws = d["words"] if isinstance(d, dict) else d
    out = []
    for w in ws:
        s = w.get("s", w.get("start")); e = w.get("e", w.get("end"))
        if s is None: continue
        out.append((float(s), float(e), (w.get("w") or "").strip()))
    return out

for code, meta in MAPS.items():
    an = json.load(open(os.path.join(ANA, f"{code}_analysis.json")))
    words = load_words(an.get("words_json"))
    prof = an["rms_0.1s"]; onsets = set(an["onset_candidates"]); cuts = an["scene_cuts_gt_0.35"]
    segs = meta["segs"]
    def seg_at(t):
        for s in segs:
            if s[0] <= t < s[1]:
                return s
        return segs[-1]
    L = []
    L.append(f"# BREAKDOWN — {code} — \"{meta['title']}\"")
    L.append("")
    L.append(f"- **URL:** {meta['url']}  |  **Posted:** {meta['posted']}  |  **Engagement at pull:** {meta['likes']} likes / {meta['comments']} comments")
    L.append(f"- **File:** `videos/devinjatho_{code}.mp4` — {meta['dims']}, {meta['fps']}fps, {meta['dur']}s")
    L.append(f"- **Format:** {meta['fmt']}")
    L.append(f"- **Method:** faster-whisper word timings + ffmpeg scene detection (gt(scene,0.35) — a LOWER bound on cuts: dissolves and same-framing jump cuts score under threshold) + 0.1s RMS profile with onset candidates. Visual states from the library DECODE/frame reads (see `--library-decode` companion). Segment boundaries ±0.5s unless a row says MEASURED. Semantic SFX identities are NOT claimed from RMS alone — onset rows say 'onset candidate'.")
    L.append("")
    L.append("## Device / segment table")
    L.append("")
    L.append("| # | Time | Visual (asset-level) | Caption / text | Transition in | Sound |")
    L.append("|---:|---|---|---|---|---|")
    for i, s in enumerate(segs, 1):
        vis = s[2].replace("|", "/"); cap = s[3].replace("|", "/"); tr = s[4].replace("|", "/"); so = s[5].replace("|", "/")
        L.append(f"| {i} | {s[0]:.1f}–{s[1]:.1f}s | {vis} | {cap} | {tr} | {so} |")
    L.append("")
    L.append("## B-ROLL LOG (Devin / subject inserts — separate system)")
    L.append("")
    brolls = [s for s in segs if s[6]]
    if brolls:
        L.append("| Time | B-roll insert |")
        L.append("|---|---|")
        for s in brolls:
            L.append(f"| {s[0]:.1f}–{s[1]:.1f}s | {s[6].replace('|','/')} |")
    else:
        L.append("No B-roll inserts of Devin or a subject in this reel (see segment table).")
    L.append("")
    L.append("## Sound summary (measured)")
    L.append("")
    dur = meta["dur"]
    L.append(f"- Duration {dur}s. Onset candidates (0.1s RMS jumps >2x and >=0.09): **{len(onsets)}** = {len(onsets)/dur*10:.1f} per 10s — these include word onsets; they are an UPPER bound on designed SFX, not an SFX count.")
    sil = an["silences_lt_-38dB_min0.25s"]
    L.append(f"- Silence spans (<-38dBFS-ish RMS 0.012, >=0.25s): {len(sil)} {sil if sil else ''}")
    L.append(f"- Scene cuts at gt(scene,0.35): {len(cuts)} at {cuts} — lower bound (see method note).")
    L.append("")
    L.append("## 0.5-SECOND GRID")
    L.append("")
    L.append("| t | Spoken words | Visual state | Caption on screen | Audio (RMS mean/max in bin) | Events |")
    L.append("|---:|---|---|---|---|---|")
    t = 0.0
    prev_seg = None
    while t < dur:
        seg = seg_at(t)
        bin_words = " ".join(w[2] for w in words if t <= w[0] < t + 0.5)
        idx = [prof[i] for i in range(int(t * 10), min(len(prof), int(t * 10) + 5))]
        rms = f"{sum(idx)/len(idx):.2f}/{max(idx):.2f}" if idx else "—"
        ev = []
        if any(t <= o < t + 0.5 for o in onsets): ev.append("onset candidate")
        if any(t <= c < t + 0.5 for c in cuts): ev.append("SCENE CUT (gt0.35)")
        if idx and max(idx) < 0.012: ev.append("near-silence bin")
        if seg is not prev_seg:
            ev.append("SEGMENT IN: " + seg[4])
            prev_seg = seg
        vis_short = seg[2][:110] + ("…" if len(seg[2]) > 110 else "")
        cap_short = seg[3][:80] + ("…" if len(seg[3]) > 80 else "")
        L.append(f"| {t:.1f} | {bin_words.replace('|','/')} | {vis_short.replace('|','/')} | {cap_short.replace('|','/')} | {rms} | {'; '.join(ev)} |")
        t = round(t + 0.5, 1)
    L.append("")
    L.append("Companion evidence: `BREAKDOWN-" + code + "--library-decode.md` (where present), `analysis/" + code + "_analysis.json` (full RMS series, cut list, onsets).")
    open(os.path.join(OUT, f"BREAKDOWN-{code}.md"), "w").write("\n".join(L) + "\n")
    print(code, "rows", int(dur * 2), "broll", len(brolls))

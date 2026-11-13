#!/usr/bin/env python3
"""Usage: analyze_one.py CODE VIDEO [WORDS_JSON]
Writes analysis/<CODE>_analysis.json: duration, scene cuts gt(0.35),
0.1s RMS profile, onset candidates, silence spans. Extracts mono WAV first."""
import json, os, re, struct, subprocess, sys, wave

ROOT = "/home/hatch/workspace/your_files/devin-exact-nov13"
ANA = os.path.join(ROOT, "analysis")

def scene_cuts(video):
    p = subprocess.run(["ffmpeg", "-hide_banner", "-i", video, "-filter:v",
                        "select='gt(scene,0.35)',showinfo", "-f", "null", "-"],
                       capture_output=True, text=True)
    return [round(float(m.group(1)), 2) for m in
            (re.search(r"pts_time:([0-9.]+)", l) for l in p.stderr.splitlines()) if m]

def rms_profile(wav_path, step=0.1):
    w = wave.open(wav_path); sr = w.getframerate(); ch = w.getnchannels(); sw = w.getsampwidth()
    raw = w.readframes(w.getnframes())
    if sw == 2:
        vals = struct.unpack(f"<{len(raw)//2}h", raw); peak = 32768.0
    else:
        vals = struct.unpack(f"<{len(raw)}B", raw); peak = 128.0
    if ch == 2: vals = vals[::2]
    per = int(sr * step); prof = []
    for i in range(0, len(vals), per):
        chunk = vals[i:i + per]
        if not chunk: break
        prof.append(round((sum(v * v for v in chunk) / len(chunk)) ** 0.5 / peak, 3))
    return prof

code, video = sys.argv[1], sys.argv[2]
words = sys.argv[3] if len(sys.argv) > 3 else None
wav_out = os.path.join(ANA, f"{code}_audio.wav")
if not os.path.exists(wav_out):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", video, "-ac", "1", "-ar", "16000", wav_out], check=True)
prof = rms_profile(wav_out)
onsets = [round(i * 0.1, 1) for i in range(1, len(prof)) if prof[i] >= 0.09 and prof[i] > prof[i - 1] * 2.0]
sil = []; start = None
for i, v in enumerate(prof):
    if v < 0.012 and start is None: start = i
    if (v >= 0.012 or i == len(prof) - 1) and start is not None:
        if (i - start) * 0.1 >= 0.25: sil.append([round(start * 0.1, 1), round(i * 0.1, 1)])
        start = None
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                            "-of", "csv=p=0", video], capture_output=True, text=True).stdout.strip())
data = {"code": code, "video": video, "duration_s": round(dur, 1),
        "scene_cuts_gt_0.35": scene_cuts(video), "rms_0.1s": prof,
        "onset_candidates": onsets, "silences_lt_-38dB_min0.25s": sil,
        "words_json": words}
json.dump(data, open(os.path.join(ANA, f"{code}_analysis.json"), "w"))
print(code, "dur", round(dur, 1), "cuts", len(data["scene_cuts_gt_0.35"]), "onsets", len(onsets), "sil", len(sil))

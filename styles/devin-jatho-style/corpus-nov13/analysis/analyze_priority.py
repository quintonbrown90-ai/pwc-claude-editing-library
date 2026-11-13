#!/usr/bin/env python3
"""Per-reel machine analysis for the priority Devin batch:
scene-cut times, 0.1s RMS profile, onset candidates, silence spans.
Evidence tiers are kept separate: cuts/RMS are measured; SFX identities are NOT inferred here.
"""
import json, os, re, struct, subprocess, sys, wave

ROOT = "/home/hatch/workspace/your_files/devin-exact-nov13"
BATCH = "/home/hatch/workspace/claude-editing/research/video-harvest/instagram/batch-11-devin"
REEL2 = "/home/hatch/workspace/claude-editing/research/video-harvest/instagram/devin-reel-2"
OUT = os.path.join(ROOT, "analysis")

REELS = {
    "DffkuW8SCkz": (os.path.join(ROOT, "sources", "DffkuW8SCkz.mp4"),
                    os.path.join(BATCH, "DffkuW8SCkz_audio.wav"),
                    os.path.join(BATCH, "DffkuW8SCkz.words.json")),
    "DfcPvRnyZRs": (os.path.join(ROOT, "sources", "DfcPvRnyZRs.mp4"),
                    os.path.join(BATCH, "DfcPvRnyZRs_audio.wav"),
                    os.path.join(BATCH, "DfcPvRnyZRs.words.json")),
    "DfV6GWMyqs0": (os.path.join(ROOT, "sources", "DfV6GWMyqs0.mp4"),
                    os.path.join(BATCH, "DfV6GWMyqs0_audio.wav"),
                    os.path.join(BATCH, "DfV6GWMyqs0.words.json")),
    "DSh8cgtjfGX": (os.path.join(ROOT, "sources", "DSh8cgtjfGX.mp4"),
                    os.path.join(BATCH, "DSh8cgtjfGX_audio.wav"),
                    os.path.join(BATCH, "DSh8cgtjfGX.words.json")),
    "DLpgNYQMZlm": (os.path.join(ROOT, "sources", "DLpgNYQMZlm.mp4"),
                    os.path.join(BATCH, "DLpgNYQMZlm_audio.wav"),
                    os.path.join(BATCH, "DLpgNYQMZlm.words.json")),
    "Dd3x4cMStzs": (os.path.join(REEL2, "reel2.mp4"), None,
                    os.path.join(REEL2, "words.json")),
}

def scene_cuts(video):
    cmd = ["ffmpeg", "-hide_banner", "-i", video, "-filter:v",
           "select='gt(scene,0.35)',showinfo", "-f", "null", "-"]
    p = subprocess.run(cmd, capture_output=True, text=True)
    times = []
    for line in p.stderr.splitlines():
        m = re.search(r"pts_time:([0-9.]+)", line)
        if m:
            times.append(round(float(m.group(1)), 2))
    return times

def ensure_wav(code, video, wav_path):
    if wav_path and os.path.exists(wav_path):
        return wav_path
    out = os.path.join(OUT, f"{code}_audio.wav")
    if not os.path.exists(out):
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", video,
                        "-ac", "1", "-ar", "16000", out], check=True)
    return out

def rms_profile(wav_path, step=0.1):
    w = wave.open(wav_path)
    sr = w.getframerate(); ch = w.getnchannels(); sw = w.getsampwidth()
    n = w.getnframes()
    raw = w.readframes(n)
    if sw == 2:
        vals = struct.unpack(f"<{len(raw)//2}h", raw)
        peak = 32768.0
    else:
        vals = struct.unpack(f"<{len(raw)}B", raw); peak = 128.0
    if ch == 2:
        vals = vals[::2]
    per = int(sr * step)
    prof = []
    for i in range(0, len(vals), per):
        chunk = vals[i:i + per]
        if not chunk:
            break
        ms = sum(v * v for v in chunk) / len(chunk)
        prof.append(round((ms ** 0.5) / peak, 3))
    return prof

def onsets(prof, step=0.1):
    out = []
    for i in range(1, len(prof)):
        prev, cur = prof[i - 1], prof[i]
        if cur >= 0.09 and cur > prev * 2.0:
            out.append(round(i * step, 1))
    return out

def silences(prof, step=0.1, thresh=0.012, min_len=0.25):
    out = []; start = None
    for i, v in enumerate(prof):
        if v < thresh and start is None:
            start = i
        if (v >= thresh or i == len(prof) - 1) and start is not None:
            dur = (i - start) * step
            if dur >= min_len:
                out.append([round(start * step, 1), round(i * step, 1)])
            start = None
    return out

for code, (video, wav_path, words) in REELS.items():
    wav_use = ensure_wav(code, video, wav_path)
    prof = rms_profile(wav_use)
    data = {
        "code": code, "video": video,
        "duration_s": round(len(prof) * 0.1, 1),
        "scene_cuts_gt_0.35": scene_cuts(video),
        "rms_0.1s": prof,
        "onset_candidates": onsets(prof),
        "silences_lt_-38dB_min0.25s": silences(prof),
        "words_json": words if words and os.path.exists(words) else None,
    }
    with open(os.path.join(OUT, f"{code}_analysis.json"), "w") as f:
        json.dump(data, f)
    print(code, "dur", data["duration_s"], "cuts", len(data["scene_cuts_gt_0.35"]),
          "onsets", len(data["onset_candidates"]), "silences", len(data["silences_lt_-38dB_min0.25s"]))

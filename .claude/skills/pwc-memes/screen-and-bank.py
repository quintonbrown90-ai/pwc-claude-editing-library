#!/usr/bin/env python3
"""screen-and-bank.py — Q's meme screening pipeline (CLEAN-ONLY law).

Pipeline: (optional yt-dlp download) -> extract audio -> faster-whisper
transcription with word timestamps -> profanity scan -> verdict:
  CLEAN    no profanity found in the transcript
  SEGMENTS profanity isolated to listed spans; bank only the clean spans
  PARKED   profanity pervasive (hits spread across the file) — never bank

NOTE: the scan covers SPOKEN audio. Burned-in on-screen text must still be
checked by eye on frames before banking (see MEME-CATALOG.md §C).

Run with the whisper venv python:
  ~/workspace/.venv_fw/bin/python screen-and-bank.py <video-or-url> [...]
For a URL it downloads first with yt-dlp (720p cap) into
~/workspace/claude-editing/research/memes/incoming/. YouTube may refuse
anonymous downloads (429 / bot check) — if it does, STOP: the file must
come from Q's signed-in browser (screen-record) instead. Never retry-loop
a rate-limited source.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

INCOMING = Path.home() / "workspace/claude-editing/research/memes/incoming"

# Deliberately broad: Q's rule is NO cursing anywhere — when in doubt, flag.
PROFANITY = {
    "fuck", "fucking", "fucked", "fucker", "motherfucker", "motherfucking",
    "shit", "shitting", "bullshit", "shitty",
    "bitch", "bitches", "bitching",
    "damn", "dammit", "goddamn", "goddammit",
    "ass", "asshole", "asses", "dumbass", "jackass",
    "hell",  # flagged for review; faith content may use it theologically —
             # a human confirms context before banking either way
    "nigga", "niggas", "nigger", "niggers",
    "piss", "pissed", "dick", "dicks", "cock", "pussy",
    "whore", "slut", "bastard", "crap",  # crap flagged for review too
    "wtf", "stfu", "fck", "fking", "biatch",
}


def download(url: str) -> Path:
    INCOMING.mkdir(parents=True, exist_ok=True)
    out = INCOMING / "%(id)s.%(ext)s"
    cmd = [sys.executable, "-m", "yt_dlp", "-f",
           "bv*[height<=720]+ba/b[height<=720]", "--merge-output-format", "mp4",
           "-o", str(out), "--no-playlist", url]
    print("downloading:", url)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-1500:])
        raise SystemExit("DOWNLOAD FAILED — if this is a 429 / bot-check, STOP. "
                         "Route: Q's signed-in browser screen-record.")
    vid = url.rstrip("/").split("/")[-1].split("?")[0]
    files = sorted(INCOMING.glob(vid + ".*"))
    if not files:
        raise SystemExit("download finished but file not found in incoming/")
    return files[0]


def transcribe(path: Path):
    from faster_whisper import WhisperModel
    model = WhisperModel("small", device="cpu", compute_type="int8")
    segments, _info = model.transcribe(str(path), word_timestamps=True)
    words = []
    for seg in segments:
        for w in (seg.words or []):
            words.append({"word": w.word.strip(), "start": w.start, "end": w.end})
    return words


def scan(words):
    hits = []
    for w in words:
        token = re.sub(r"[^a-z']", "", w["word"].lower())
        if token in PROFANITY:
            hits.append(w)
    return hits


def verdict(words, hits):
    if not hits:
        return "CLEAN", []
    if not words:
        return "PARKED", hits
    duration = words[-1]["end"]
    span = hits[-1]["end"] - hits[0]["start"]
    # Pervasive = hits in 3+ separated clusters or spread over >40% of runtime
    clusters = 1
    for a, b in zip(hits, hits[1:]):
        if b["start"] - a["end"] > 5.0:
            clusters += 1
    if clusters >= 3 or (duration and span / duration > 0.4):
        return "PARKED", hits
    bad_spans = [(max(0.0, h["start"] - 0.25), h["end"] + 0.25) for h in hits]
    return "SEGMENTS", bad_spans


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for arg in sys.argv[1:]:
        path = download(arg) if arg.startswith("http") else Path(arg)
        print(f"\n=== {path.name} ===")
        words = transcribe(path)
        hits = scan(words)
        v, extra = verdict(words, hits)
        print("duration:", round(words[-1]["end"], 1) if words else "?", "s")
        print("profanity hits:", [(h["word"], round(h["start"], 1)) for h in hits])
        print("VERDICT:", v)
        if v == "SEGMENTS":
            print("exclude spans (s):", [(round(a, 1), round(b, 1)) for a, b in extra])
            print("-> cut and bank ONLY the clean spans; record in/out in MEME-CATALOG.md")
        elif v == "PARKED":
            print("-> do NOT bank. Record the park + reason in MEME-CATALOG.md")
        else:
            print("-> clean on audio. STILL eyeball frames for burned-in text before banking.")
        report = path.with_suffix(".screen.json")
        report.write_text(json.dumps(
            {"file": str(path), "verdict": v,
             "hits": [(h["word"], h["start"]) for h in hits]}, indent=2))
        print("report:", report)


if __name__ == "__main__":
    main()

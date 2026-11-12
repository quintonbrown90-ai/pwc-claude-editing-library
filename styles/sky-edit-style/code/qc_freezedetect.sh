#!/bin/bash
# qc_freezedetect.sh — QC ONLY. Measures an exported file; builds nothing.
# Usage: bash qc_freezedetect.sh <export.mp4>
# Pass bar: zero freezes >= 0.35s inside footage spans (ffmpeg freezedetect n=0.003 d=0.35).
set -e
F="$1"
[ -n "$F" ] || { echo "usage: bash qc_freezedetect.sh <export.mp4>"; exit 2; }
[ -f "$F" ] || { echo "not found: $F"; exit 2; }
echo "== ffprobe =="
ffprobe -v error -show_entries format=duration,size -show_entries stream=codec_name,width,height,r_frame_rate -of default=noprint_wrappers=1 "$F"
echo "== freezedetect (noise 0.003, duration 0.35) =="
ffmpeg -v info -i "$F" -vf freezedetect=n=0.003:d=0.35 -map 0:v -f null - 2>&1 | grep -E "freeze_start|freeze_end|freeze_duration" || echo "NO FREEZES DETECTED (>=0.35s)"
echo "== note =="
echo "Also required (not scripted here): +/-0.15s entrance/exit frame audits, last-word to end-card <=1s, lip-sync offsets, per-word fit, full self-watch. See QC.md."

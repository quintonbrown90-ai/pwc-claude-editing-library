#!/usr/bin/env python3
"""Usage: transcribe_one.py VIDEO OUT_WORDS_JSON OUT_TRANSCRIPT_TXT
faster-whisper base.en, word timestamps, batch-11 compatible format."""
import json, sys
from faster_whisper import WhisperModel

video, out_words, out_txt = sys.argv[1], sys.argv[2], sys.argv[3]
model = WhisperModel("base.en", device="cpu", compute_type="int8")
segments, info = model.transcribe(video, word_timestamps=True, vad_filter=True)
words, lines = [], []
for seg in segments:
    lines.append(seg.text.strip())
    for w in (seg.words or []):
        words.append({"w": w.word, "s": round(w.start, 2), "e": round(w.end, 2)})
json.dump({"duration": info.duration, "words": words}, open(out_words, "w"))
open(out_txt, "w").write("\n".join(lines) + "\n")
print("words", len(words), "dur", round(info.duration, 1))

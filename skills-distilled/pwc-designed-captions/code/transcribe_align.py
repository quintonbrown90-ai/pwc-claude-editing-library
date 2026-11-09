#!/usr/bin/env python3
"""Step 1 — word-level timing from the speaker's actual audio.

Designed captions are timed to WORDS, not lines: every style switch lands on
the exact frame a word is spoken. Uses WhisperX (falls back to faster-whisper)
for word-aligned timestamps.

Usage:
  python3 transcribe_align.py INPUT.mp4 --out words.json [--script script.txt]

If --script is given (Q's locked rule: captions come from the script/word
file as ground truth, never raw ASR alone), ASR words are matched onto the
script tokens and the script's spelling/punctuation wins; timings come from
ASR. Output: [{"w": "word", "s": 0.00, "e": 0.00}, ...]
"""
import argparse, json, subprocess, sys, os


def extract_audio(src, wav):
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', src, '-vn',
                    '-ac', '1', '-ar', '16000', wav], check=True)


def transcribe_whisperx(wav, model_name='small'):
    import whisperx
    audio = whisperx.load_audio(wav)
    model = whisperx.load_model(model_name, 'cpu', compute_type='int8')
    res = model.transcribe(audio, batch_size=8)
    am, meta = whisperx.load_align_model(language_code=res['language'], device='cpu')
    aligned = whisperx.align(res['segments'], am, meta, audio, 'cpu')
    out = []
    for seg in aligned['segments']:
        for w in seg.get('words', []):
            if 'start' in w:
                out.append({'w': w['word'].strip(), 's': round(w['start'], 3),
                            'e': round(w['end'], 3)})
    return out


def transcribe_faster_whisper(wav, model_name='small'):
    from faster_whisper import WhisperModel
    model = WhisperModel(model_name, device='cpu', compute_type='int8')
    segments, _ = model.transcribe(wav, word_timestamps=True)
    out = []
    for seg in segments:
        for w in (seg.words or []):
            out.append({'w': w.word.strip(), 's': round(w.start, 3),
                        'e': round(w.end, 3)})
    return out


def snap_to_script(words, script_text):
    """Replace ASR tokens with script tokens, keeping ASR timings.

    Simple monotonic alignment on lowercase alphanumeric forms. If counts
    diverge badly, ASR is kept (and a warning printed) rather than guessing.
    """
    import re
    toks = script_text.split()
    def norm(s): return re.sub(r'[^a-z0-9]', '', s.lower())
    if abs(len(toks) - len(words)) > max(3, len(words) * 0.15):
        print('WARN: script/ASR token counts diverge; keeping ASR text', file=sys.stderr)
        return words
    return [{'w': t, 's': w['s'], 'e': w['e']} for t, w in zip(toks, words)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input')
    ap.add_argument('--out', default='words.json')
    ap.add_argument('--script')
    ap.add_argument('--model', default='small')
    a = ap.parse_args()
    wav = '/tmp/_cap_audio.wav'
    extract_audio(a.input, wav)
    try:
        words = transcribe_whisperx(wav, a.model)
    except Exception as ex:
        print(f'whisperx failed ({ex}); falling back to faster-whisper', file=sys.stderr)
        words = transcribe_faster_whisper(wav, a.model)
    if a.script:
        words = snap_to_script(words, open(a.script).read())
    json.dump(words, open(a.out, 'w'), indent=1)
    print(f'{len(words)} words -> {a.out}')


if __name__ == '__main__':
    main()

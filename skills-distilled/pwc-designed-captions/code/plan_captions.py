#!/usr/bin/env python3
"""Step 2 — the caption PLAN: decide, for every phrase, its style, layer,
placement and motion BEFORE anything renders (beat-plan first, always).

Reads words.json (from transcribe_align.py) and optionally facetrack.json
(from track_matte.py — median face box), writes plan.json: a list of events
{t0, t1, text, style, layer, box, motion_in, motion_out}.

The style system (from the @viashaan DESIGNED CAPTIONS teardown, remapped to
Q's rules — PWC palette only, nothing over the face, everything inside the
Instagram safe zones):

  BASE          clean bold karaoke words (Poppins ExtraBold), current word gold
  SCRIPT_ACCENT single semantic word in serif italic GOLD (negations, feelings)
  GLOW          teal-glow letters for "designed / automatic / magic" moments
  BIG_CAPS      huge Anton caps for the claim line of a section
  CHUNKY_ITALIC Poppins ExtraBold Italic for energy / listing phrases
  HERO_BEHIND   one hero word per section, giant, on the BEHIND layer so it
                passes behind the speaker's head (needs the matte composite)

Placement: phrases anchor ABOVE the head by default (Q's rule), else in the
empty space left/right of the head from the face track; every box is clamped
by safe_zones.clamp_box so no caption can ever enter Instagram's UI.
Motion: each style names its entrance/exit from the MOTION vocabulary
(overshoot, ease_out, spring, steps...) — see MOTION.md / easings.py.
"""
import argparse, json, re, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from safe_zones import clamp_box

NEGATIONS = {'never', 'not', "don't", 'no', 'none', 'nothing', 'stop', "can't",
             "won't", 'without', 'zero', 'free'}  # 'free' = payoff accent for Q
FEELINGS = {'love', 'hate', 'feel', 'feels', 'scared', 'proud', 'sick', 'tired'}
GLOW_TRIGGERS = {'designed', 'design', 'automatic', 'automatically', 'magic',
                 'system', 'systems', 'ai', 'claude'}
PAUSE_SPLIT = 0.35  # seconds of silence that end a phrase


def phrases(words):
    out, cur = [], []
    for w in words:
        if cur and w['s'] - cur[-1]['e'] > PAUSE_SPLIT:
            out.append(cur); cur = []
        cur.append(w)
        if len(cur) >= 4:
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    return out


def clean(w):
    return re.sub(r'[^a-z0-9\']', '', w.lower())


def plan(words, face=None):
    """face: median face box (x, y, w, h) at 1080x1920 or None."""
    events, last_styles, hero_used_at = [], [], -10
    hero_word_idx = -100  # FIX (SL-28, Nov 8): word index of the last hero word.
    # The old code compared a WORD INDEX (words.index(ph[0])) against
    # hero_used_at, which is a TIME in seconds — a units bug that made
    # rule 3 true for almost every phrase, so BIG_CAPS fired on most
    # phrases instead of at most once per section (SKILL.md).
    t_cursor = 0.0
    for i, ph in enumerate(phrases(words)):
        text = ' '.join(w['w'] for w in ph)
        t0, t1 = ph[0]['s'], ph[-1]['e']
        keys = [clean(w['w']) for w in ph]
        style, layer = None, 'front'
        # 1. A lone negation/feeling word inside a short phrase -> script accent
        accent = [w for w in ph if clean(w['w']) in NEGATIONS | FEELINGS]
        if accent and len(ph) <= 3:
            style = 'SCRIPT_ACCENT'
        # 2. Glow triggers
        elif any(k in GLOW_TRIGGERS for k in keys):
            style = 'GLOW'
        # 3. Section claim: long-ish phrase early in a sentence cluster
        elif len(ph) >= 3 and (i == 0 or words.index(ph[0]) - hero_word_idx > 40):
            style = 'BIG_CAPS'
        # 4. One hero word per ~15s goes BEHIND the head
        hero = max(ph, key=lambda w: len(clean(w['w']))) if ph else None
        if hero and len(clean(hero['w'])) >= 7 and t0 - hero_used_at > 15:
            events.append({'t0': hero['s'], 't1': hero['e'] + 0.45,
                           'text': hero['w'].upper(), 'style': 'HERO_BEHIND',
                           'layer': 'behind', 'motion_in': 'ease_out',
                           'motion_out': 'ease_in', 'words': [hero]})
            hero_used_at = t0
            hero_word_idx = words.index(hero)
            continue
        # Rotation discipline (SKILL.md): never the same style 3 events
        # running — a third consecutive repeat falls back to BASE.
        if style is not None and last_styles[-2:] == [style, style]:
            style = 'BASE'
        if style is None:
            style = 'CHUNKY_ITALIC' if last_styles[-1:] == ['BASE'] else 'BASE'
        last_styles.append(style)
        events.append({'t0': t0, 't1': t1, 'text': text, 'style': style,
                       'layer': layer, 'motion_in': MOTION_IN[style],
                       'motion_out': 'ease_in', 'words': ph})
    # Placement pass
    for ev in events:
        ev['box'] = place(ev, face)
    return events


MOTION_IN = {
    'BASE': 'steps',          # words tick on with the voice
    'SCRIPT_ACCENT': 'ease_out',   # rises and settles like handwriting landing
    'GLOW': 'ease_in_out',    # blooms in
    'BIG_CAPS': 'overshoot',  # pops past size, settles
    'CHUNKY_ITALIC': 'spring',
    'HERO_BEHIND': 'ease_out',
}


def place(ev, face):
    """Return (x, y, w, h) at 1080x1920, clamped to safe zones, off the face."""
    # Rough text metrics; the renderer re-measures with the real font.
    n = max(len(ev['text']), 1)
    size = {'BIG_CAPS': 120, 'HERO_BEHIND': 300, 'SCRIPT_ACCENT': 110,
            'GLOW': 96, 'CHUNKY_ITALIC': 92, 'BASE': 84}[ev['style']]
    w = min(int(n * size * 0.58), 880)
    h = int(size * 1.25)
    if face:
        fx, fy, fw, fh = face
        cx = fx + fw / 2
        x = int(cx - w / 2)
        y = int(fy - h - 30) if ev['style'] != 'HERO_BEHIND' else int(fy - h * 0.35)
    else:
        x, y = (1080 - w) // 2, 420
    return clamp_box((x, y, w, h))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('words')
    ap.add_argument('--face', help='facetrack.json with median face box')
    ap.add_argument('--out', default='plan.json')
    a = ap.parse_args()
    words = json.load(open(a.words))
    face = None
    if a.face:
        ft = json.load(open(a.face))
        face = ft.get('median_box_1080')
    events = plan(words, face)
    json.dump(events, open(a.out, 'w'), indent=1)
    from collections import Counter
    print(f'{len(events)} caption events -> {a.out}', Counter(e["style"] for e in events))


if __name__ == '__main__':
    main()

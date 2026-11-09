#!/usr/bin/env python3
"""Step 3 — render the caption layer as transparent PNG frames (1080x1920).

Two layers are rendered separately so composite.py can sandwich the speaker
between them:
  --layer behind : only HERO_BEHIND events (the word passes behind the head)
  --layer front  : every other style

Entrance/exit motion comes from the plan's motion names (MOTION vocabulary):
scale/alpha/rise are driven by easings.ease() per frame — overshoot really
overshoots, steps really ticks, spring really settles.

Usage:
  python3 render_captions.py plan.json --out frames_front --layer front --duration 37.2
"""
import argparse, json, math, os, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from easings import ease
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
HERE = __file__.rsplit('/', 1)[0]
FONTS = {
    'BASE': 'Poppins-ExtraBold.ttf',
    'SCRIPT_ACCENT': 'PlayfairDisplay-BoldItalic.ttf',
    'GLOW': 'Poppins-ExtraBold.ttf',
    'BIG_CAPS': 'Anton-Regular.ttf',
    'CHUNKY_ITALIC': 'Poppins-ExtraBoldItalic.ttf',
    'HERO_BEHIND': 'Anton-Regular.ttf',
}
BASE_SIZE = {'BASE': 84, 'SCRIPT_ACCENT': 118, 'GLOW': 100, 'BIG_CAPS': 128,
             'CHUNKY_ITALIC': 96, 'HERO_BEHIND': 320}
GOLD = (254, 226, 56, 255)      # #FEE238
TEAL = (20, 168, 134, 255)      # #14A886
WHITE = (255, 255, 255, 255)
_cache = {}


def font(style, size):
    key = (style, size)
    if key not in _cache:
        path = os.path.join(HERE, '..', 'fonts', FONTS[style])
        _cache[key] = ImageFont.truetype(path, size)
    return _cache[key]


def fit_font(style, text, max_w):
    size = BASE_SIZE[style]
    probe = ImageDraw.Draw(Image.new('RGBA', (8, 8)))
    while size > 20:
        f = font(style, size)
        if probe.textbbox((0, 0), text, font=f)[2] <= max_w:
            return f, size
        size -= 6
    return font(style, 20), 20


def draw_event(base_img, ev, t):
    """Draw one caption event onto base_img at time t (seconds)."""
    t0, t1 = ev['t0'], ev['t1']
    IN_D, OUT_D = 0.22, 0.18
    if t < t0 - 0.0 or t > t1 + OUT_D:
        return
    pin = ease(ev.get('motion_in', 'ease_out'), (t - t0) / IN_D) if t - t0 < IN_D else 1.0
    pout = 1.0
    if t > t1:
        pout = 1 - ease('ease_in', (t - t1) / OUT_D)
    alpha = max(0.0, min(1.0, pin)) * pout
    if alpha <= 0:
        return
    style = ev['style']
    x, y, bw, bh = ev['box']
    layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    if style == 'BASE' and ev.get('words'):
        # Karaoke: phrase laid out word by word, spoken word turns gold.
        words = ev['words']
        f, size = fit_font(style, ev['text'], bw)
        widths = [d.textbbox((0, 0), w['w'], font=f)[2] for w in words]
        space = d.textbbox((0, 0), ' ', font=f)[2]
        total = sum(widths) + space * (len(words) - 1)
        cx = x + (bw - total) / 2
        rise = (1 - ease('steps', (t - t0) / IN_D)) * 14 if t - t0 < IN_D else 0
        for w, ww in zip(words, widths):
            col = GOLD if w['s'] <= t <= w['e'] + 0.05 else WHITE
            d.text((cx, y + rise), w['w'], font=f, fill=col,
                   stroke_width=5, stroke_fill=(2, 20, 40, 255))
            cx += ww + space
    else:
        f, size = fit_font(style, ev['text'], bw)
        scale = 0.9 + 0.1 * pin if ev.get('motion_in') in ('overshoot', 'spring') else 1.0
        if scale != 1.0:
            f, size = fit_font(style, ev['text'], int(bw * scale))
        tb = d.textbbox((0, 0), ev['text'], font=f)
        tw, th = tb[2] - tb[0], tb[3] - tb[1]
        tx = x + (bw - tw) / 2 - tb[0]
        ty = y + (bh - th) / 2 - tb[1]
        if style == 'GLOW':
            glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
            gd = ImageDraw.Draw(glow)
            gd.text((tx, ty), ev['text'], font=f, fill=(20, 232, 200, 200))
            glow = glow.filter(ImageFilter.GaussianBlur(18))
            layer.alpha_composite(glow)
            d = ImageDraw.Draw(layer)
            d.text((tx, ty), ev['text'], font=f, fill=WHITE,
                   stroke_width=3, stroke_fill=(4, 60, 52, 255))
        elif style == 'SCRIPT_ACCENT':
            d.text((tx, ty), ev['text'], font=f, fill=GOLD,
                   stroke_width=2, stroke_fill=(40, 30, 0, 160))
        elif style == 'HERO_BEHIND':
            d.text((tx, ty), ev['text'], font=f, fill=(255, 255, 255, 235),
                   stroke_width=4, stroke_fill=(2, 20, 40, 200))
        else:
            d.text((tx, ty), ev['text'], font=f, fill=WHITE,
                   stroke_width=6, stroke_fill=(2, 20, 40, 255))
    if alpha < 1.0:
        a = layer.getchannel('A').point(lambda v: int(v * alpha))
        layer.putalpha(a)
    base_img.alpha_composite(layer)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('plan')
    ap.add_argument('--out', required=True)
    ap.add_argument('--layer', choices=['front', 'behind'], default='front')
    ap.add_argument('--duration', type=float, required=True)
    ap.add_argument('--fps', type=int, default=30)
    a = ap.parse_args()
    events = json.load(open(a.plan))
    sel = [e for e in events if (e['layer'] == 'behind') == (a.layer == 'behind')]
    os.makedirs(a.out, exist_ok=True)
    n = int(a.duration * a.fps)
    for i in range(n):
        t = i / a.fps
        img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        for ev in sel:
            if ev['t0'] - 0.3 <= t <= ev['t1'] + 0.3:
                draw_event(img, ev, t)
        img.save(os.path.join(a.out, f'f{i:05d}.png'))
    print(f'{a.layer}: {n} frames -> {a.out}')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Step 4 — the three-layer composite (this IS the behind-the-head trick).

  layer 0 (bottom): original video
  layer 1:          caption frames rendered with --layer behind
                    (HERO_BEHIND words — visible everywhere EXCEPT where
                    the speaker's matte covers them)
  layer 2 (top):    speaker foreground with alpha (fg_alpha.mp4)
  layer 3:          caption frames rendered with --layer front

No rotoscoping: the matte does the masking, per frame, automatically.

Usage:
  python3 composite.py INPUT.mp4 --behind frames_behind --front frames_front \
      --fg fg_alpha.mp4 --out FINAL.mp4 [--fps 30]
Without --fg, the behind layer is skipped and the video renders front-only.
"""
import argparse, subprocess, sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input')
    ap.add_argument('--behind')
    ap.add_argument('--front', required=True)
    ap.add_argument('--fg')
    ap.add_argument('--out', default='FINAL.mp4')
    ap.add_argument('--fps', type=int, default=30)
    a = ap.parse_args()
    fr = f'fps={a.fps},scale=1080:1920'
    if a.fg and a.behind:
        inputs = ['-i', a.input,
                  '-framerate', str(a.fps), '-i', f'{a.behind}/f%05d.png',
                  '-i', a.fg,
                  '-framerate', str(a.fps), '-i', f'{a.front}/f%05d.png']
        filt = (f'[0:v]{fr}[bg];'
                f'[1:v]format=rgba[bc];'
                f'[2:v]{fr},format=rgba[fgv];'
                f'[3:v]format=rgba[fc];'
                f'[bg][bc]overlay=0:0[t1];'
                f'[t1][fgv]overlay=0:0[t2];'
                f'[t2][fc]overlay=0:0[v]')
    else:
        inputs = ['-i', a.input,
                  '-framerate', str(a.fps), '-i', f'{a.front}/f%05d.png']
        filt = (f'[0:v]{fr}[bg];[1:v]format=rgba[fc];'
                f'[bg][fc]overlay=0:0[v]')
    cmd = ['ffmpeg', '-y', '-v', 'error', *inputs,
           '-filter_complex', filt, '-map', '[v]', '-map', '0:a?',
           '-c:v', 'libx264', '-crf', '19', '-pix_fmt', 'yuv420p',
           '-movflags', '+faststart', '-c:a', 'aac', '-shortest', a.out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-2000:], file=sys.stderr)
        sys.exit(1)
    print(f'composite -> {a.out}')


if __name__ == '__main__':
    main()

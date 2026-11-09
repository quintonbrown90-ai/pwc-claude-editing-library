#!/usr/bin/env python3
"""Step 0 — track the face and cut the speaker matte.

Two outputs:
  facetrack.json : per-second face boxes (scaled to 1080x1920) + median box.
                   The planner anchors captions in the empty space around it.
  fg_alpha.mp4   : the speaker as an RGBA foreground (matte as alpha) — the
                   top layer of the composite, which is what lets a hero word
                   pass BEHIND the head with no rotoscoping.

Face detection: OpenCV Haar cascade (always available). Matte: MediaPipe
Selfie Segmentation when installed; otherwise a soft chroma-free fallback is
NOT attempted — the script says so plainly and exits, because a bad matte
looks worse than no behind-layer. Install: pip install mediapipe
"""
import argparse, json, subprocess, sys, os
import cv2
import numpy as np

TW, TH = 1080, 1920


def probe(src):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries',
                          'stream=width,height,r_frame_rate,duration',
                          '-of', 'json', src], capture_output=True, text=True)
    s = json.loads(out.stdout)['streams'][0]
    num, den = s['r_frame_rate'].split('/')
    return s['width'], s['height'], float(num) / float(den), float(s['duration'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input')
    ap.add_argument('--track-out', default='facetrack.json')
    ap.add_argument('--fg-out', default='fg_alpha.mp4')
    ap.add_argument('--no-fg', action='store_true')
    a = ap.parse_args()
    w, h, fps, dur = probe(a.input)
    sx, sy = TW / w, TH / h
    cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(a.input)
    boxes, samples = [], []
    idx = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if idx % max(1, int(fps)) == 0:  # 1 sample / second for the track
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(gray, 1.2, 5, minSize=(60, 60))
            if len(faces):
                x, y, fw, fh = max(faces, key=lambda f: f[2] * f[3])
                box = [int(x * sx), int(y * sy), int(fw * sx), int(fh * sy)]
                boxes.append(box)
                samples.append({'t': round(idx / fps, 2), 'box': box})
        idx += 1
    cap.release()
    if not boxes:
        print('ERROR: no face found — is this a talking-head shot?', file=sys.stderr)
        sys.exit(1)
    med = [int(np.median([b[i] for b in boxes])) for i in range(4)]
    json.dump({'median_box_1080': med, 'samples': samples,
               'src_size': [w, h], 'fps': fps, 'duration': dur},
              open(a.track_out, 'w'), indent=1)
    print(f'face track: median box {med} from {len(boxes)} samples -> {a.track_out}')
    if a.no_fg:
        return
    try:
        import mediapipe as mp
    except ImportError:
        print('mediapipe not installed — skipping fg matte. '
              'pip install mediapipe, or composite WITHOUT the behind layer.',
              file=sys.stderr)
        return
    seg = mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection=1)
    cap = cv2.VideoCapture(a.input)
    writer = cv2.VideoWriter(a.fg_out, cv2.VideoWriter_fourcc(*'mp4v'),
                             fps, (TW, TH))
    tmp = a.fg_out + '.rgba.mp4'
    writer.release()
    # Write RGB + alpha via ffmpeg raw pipe for a real alpha channel.
    cmd = ['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgba',
           '-s', f'{TW}x{TH}', '-r', str(fps), '-i', '-', '-an',
           '-c:v', 'qtrle', tmp]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        frame = cv2.resize(frame, (TW, TH))
        res = seg.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        mask = (res.segmentation_mask > 0.5).astype(np.uint8) * 255
        mask = cv2.GaussianBlur(mask, (7, 7), 0)
        rgba = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        rgba[:, :, 3] = mask
        proc.stdin.write(rgba.tobytes())
    proc.stdin.close(); proc.wait(); cap.release()
    os.replace(tmp, a.fg_out)
    print(f'foreground matte -> {a.fg_out}')


if __name__ == '__main__':
    main()

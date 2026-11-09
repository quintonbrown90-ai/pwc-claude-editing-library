"""Instagram Reels UI safe zones on the 1080x1920 canvas (9:16).

Derived from Q's own boundary video + the @viashaan rule: captions NEVER go
behind the profile/close area (top), NEVER under the right action rail
(like/comment/share), NEVER under the bottom caption/audio lines, and never
over the speaker's face. The face rule is enforced in plan_captions.py using
the face track; the UI rules are enforced here.

Coordinates are (x, y) top-left origin, pixels at 1080x1920.
"""

CANVAS_W, CANVAS_H = 1080, 1920

# Rectangles (x0, y0, x1, y1) that on-screen text must NOT enter.
FORBIDDEN = {
    'top_bar':      (0, 0, 1080, 250),      # profile row, follow btn, close X
    'right_rail':   (925, 880, 1080, 1560), # like / comment / share / more
    'bottom_block': (0, 1560, 1080, 1920),  # username, caption, audio line, CTA
    'comment_box':  (0, 1790, 1080, 1920),  # "Add comment..." field
}

# Preferred caption territory: the empty space around/above the head.
# (Bottom edge tightened to Q's boundary-video zone; cards anchor even
# higher — bottom edge <= ~y1280 — per the standing charts-high rule.)
SAFE_X0, SAFE_Y0, SAFE_X1, SAFE_Y1 = 40, 260, 920, 1480


def clamp_box(box):
    """Clamp an (x, y, w, h) text box into the global safe territory.

    Placement-vs-face is handled by the planner; this clamp guarantees no
    caption can ever slide into Instagram's UI, whatever the planner asked.
    """
    x, y, w, h = box
    x = max(SAFE_X0, min(x, SAFE_X1 - w))
    y = max(SAFE_Y0, min(y, SAFE_Y1 - h))
    # Right rail bites into the safe rect's lower-right corner.
    rail = FORBIDDEN['right_rail']
    if x + w > rail[0] and y + h > rail[1]:
        y = min(y, rail[1] - h)
    return (int(x), int(y), int(w), int(h))


def overlaps(a, b):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by

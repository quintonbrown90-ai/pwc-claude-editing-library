#!/usr/bin/env python3
"""sky_devices.py — every Sky device D1-D56 as executable code (SKY v6).

Each device is a function that takes a start time + its parameters and
returns a list of timeline EVENT dicts. An event is the single unit every
downstream emitter consumes (HyperFrames composition, CapCut build
sequence, QC overlap/handoff checks):

  {
    "device": "D4", "name": "filter board",
    "t0": 12.0, "t1": 24.5, "track": "overlay1",
    "geometry": {"x": 90, "y": 320, "w": 900, "h": 560},   # 1080x1920 px
    "text": "...", "items": [...],
    "colors": {"accent": "#14A886", "text": "#FCFCFC", ...},
    "motion": {"in": {"type": "pop", "dur_s": 0.3, "easing": "back.out_1.141",
                      "keyframes": [...]},
               "out": {"type": "hard_cut"}},
    "sfx": "pop-medium-in.wav",
    "status": "VERIFIED" | "[EST]",
    "source_reel": "DfX2qwQGagM",
  }

Geometry is 1080x1920 px, top-left origin. Safe zone x 70-930, y 280-1480.
Nothing is placed over the face box (default face box x 340-740, y 500-950
in 1080x1920 coords — override per take with face_box=).

Status tags come from STYLE-GRAMMAR.md / GAPS.md: VERIFIED = measured from
Sky's own videos; [EST] = placeholder from thumbnail/measurement estimates.
[EST] devices are implemented with the documented default so a build can
proceed, and the event says so — never presented as measured.

Colour rule: every colour in every event comes from sky_palette (PWC teal /
gold / navy / white / grey). Sky's raw green/orange/red are remapped at the
call site, never emitted. validate_event() enforces it.

SKY v6 (Batch 36): premium Sky is the ONLY output mode — there is no generic
fallback (the old Option 2 module was removed in the premium purge).
validate_premium_plan() rejects unknown devices, banned fonts/treatments,
cheap-grade assets, AI provenance on proof devices, [EST]-quarantined
devices and events with no Sky source citation. validate_beat_lock() /
beat_lock_report() enforce the beat-lock law (BEAT-LOCK-SPEC.md).
"""
from __future__ import annotations

from sky_easing import (
    CAPTION_OUT_S, CHILD_BUILD_FRAMES, COUNT_UP_S, PANEL_IN_FRAMES,
    POP_S, frames_to_s, keyframes,
)
from sky_palette import (
    GOLD, GREY_DIM, GREY_MID, NAVY, NAVY_DEEP, TEAL, WHITE, accent_for_family,
    is_forbidden, scan_object_for_forbidden, validate_color,
)

CANVAS_W, CANVAS_H = 1080, 1920
SAFE = {"x0": 70, "x1": 930, "y0": 280, "y1": 1480}
# Devices whose MEASURED Sky placement sits in the IG top UI zone (y<250).
# Precedent: D12 (De-A2dvCeV3 node labels y~200-280). Batch 18 adds the
# Dcc-era top-zone placements, all frame-measured from Dcc84V5jc6D (Aug 25,
# 2026): D2 hook/template headlines y80-450 (T-01/T-05); D27 donut block
# y170-540 (T-08); D30 profile heads y170-350 (T-13); D33 comment screenshots
# y230-430 (T-04); D34 thumbnail top row y150-550 (T-11); D36 origin-doc
# return y140-950 (T-16). Batch 19 adds: D38 POV-desk doc headline at the
# top of the monitor (the monitor IS the frame); D40 POV label pill y85-175
# (#19) / full-width bar y0-60 (#23/#25); D41 spine full diagram y0-600 and
# zoomed vertebra x620-1080 from y~0 (#24); D42 question-card header y210-270
# (#21); D44 POV text line y230-346 in the black band above the mini-window
# (DSI5); D46 vertical split reactor/exhibit full height from y0 (DZX);
# D47 binary labels above the ceiling lights y~90-135 (DSB, 720x1280 coords
# scaled); D48 stacked split exhibit top half from y0 (DRo/DRX); D49 red
# annotation outline, which follows the claim text on the proof screen and
# sits top-zone when the proof does (#39/#40/#49); D51 T-pose name headline
# at the top of the frame (#46). The exemption is per DEVICE id, not per
# event — the Q-lane plan must still record the safe-zone decision per take
# (shift down where the framing allows). It is NOT a general top-zone permission.
TOP_ZONE_MEASURED = {"D2", "D12", "D27", "D30", "D33", "D34", "D36",
                     "D38", "D40", "D41", "D42", "D44", "D46", "D47", "D48",
                     "D49", "D50", "D51"}
# Face box MEASURED Nov 9 (code-build pass) from 01_DfX2qwQGagM.mp4 @2.0 s
# (720x1280 frame -> 1080x1920): hair top ~y720, chin ~y1170, face x345-735.
# DfQ4's framing is lower (hair top ~y840). ALWAYS override per take with
# face_box= / --face-box — the hero zone is laid out from the hairline
# (face top - 20 px); a wrong face box silently misplaces every device.
DEFAULT_FACE_BOX = {"x": 345, "y": 720, "w": 390, "h": 450}
HAIRLINE_PAD_PX = 20

# Caption band, frame-measured Nov 9: DfX2 "sign of a" @~y1230/1920 and
# DfQ4 "types"/"want" @~y1245/1920 (chest band, chin ~y1170 + >=40 px).
# CONFLICTS with STYLE-GRAMMAR.md's 1075-1110 overlap (other reels' teardown
# coords) — the frame measurement wins for these reels; record per take.
CAPTION_Y = 1240
CAPTION_FONT_PX = 58          # CapCut font ~54-64 on a 1080-wide canvas
CAPTION_MAX_WORDS = 3
CAPTION_MAX_CHARS = 14        # break a group at 14 chars (Q lane rule)
# Dcc-era caption break (Batch 18, Dcc84V5jc6D — FIX Batch 18 QC F1): the
# Q-lane 14-char cap cannot reproduce Sky's measured 5-word groups — on the
# real words.json it yields 84 groups of 1-4 words, zero 5-word groups, 6
# one-word orphans. A 21-char cap (group breaks once its text reaches 21
# chars, i.e. exceeds 20) reproduces all three frame-verified 5-word groups
# ("than you will ever need.", "So at the very top,", "that writes it for
# you.") and yields 65 groups, 0.32-1.30 s, vs measured 0.33-1.28 s. Dcc
# branch ONLY — the Df default stays 14 chars / 1-3 words (v3, untouched).
DCC_CAPTION_MAX_CHARS = 21

TRACKS = {"hero": "overlay1", "asset": "overlay2", "chip": "overlay3",
          "captions": "overlay4", "logo": "logo", "aroll": "track0"}


def _geom(x, y, w, h):
    return {"x": int(x), "y": int(y), "w": int(w), "h": int(h)}


def _base(device, name, t0, t1, track, geometry, *, status, source_reel,
          colors=None, text=None, items=None, motion=None, sfx=None, notes=None,
          instance=None, sound=None):
    ev = {
        "device": device, "name": name,
        "t0": round(float(t0), 3), "t1": round(float(t1), 3),
        "track": track, "geometry": geometry,
        "colors": colors or {}, "text": text, "items": items or [],
        "motion": motion or {"in": {"type": "hard_cut"}, "out": {"type": "hard_cut"}},
        "sfx": sfx, "status": status, "source_reel": source_reel,
        # One device INSTANCE (e.g. one board) can emit several events (the
        # board + its rows). The variety rule counts instances, not events.
        "instance": instance or f"{device}@{round(float(t0), 2)}",
    }
    if notes:
        ev["notes"] = notes
    if sound:
        ev["sound"] = sound
    return ev


def _pop_in(dur_s=POP_S, scale_from=0.88):
    # Scale-only pop (Batch 19 cut): the measured D2 entrance is pop/scale
    # ~0.3 s with slight overshoot — no blur-in. The old blur_from=10 made
    # every device entrance a generic Claude blur-in; it is cut. No caption
    # ever used _pop_in (D1 is hard-cut, see d1_captions).
    return {"type": "pop", "dur_s": dur_s, "easing": "back.out_1.141",
            "scale_from": scale_from,
            "keyframes": keyframes("back.out_1.141", dur_s, n=6, start=scale_from, end=1.0)}


def _panel_in():
    # Scale-only panel pop (Batch 19 cut the blur 10->0 — same reason as _pop_in).
    d = frames_to_s(PANEL_IN_FRAMES)
    return {"type": "panel_pop", "dur_s": d, "easing": "back.out_1.141",
            "scale_from": 0.88,
            "keyframes": keyframes("back.out_1.141", d, n=7, start=0.88, end=1.0)}


# NOTE (premium purge, SKY v6): _panel_out() does NOT exist — it emitted a
# slide+blur-out (7 f, y+36, blur->12) that contradicts the measured exit
# rule (STYLE-GRAMMAR §5 Exits: devices exit by HARD CUT, no fades). The
# generic slide+blur exit is a BANNED telltale in v6; panel exits are
# _hard_cut_out().


def _hard_cut_out():
    return {"type": "hard_cut"}  # Sky devices exit by HARD CUT, no fades.


def _accent(family):
    return accent_for_family(family)


# ------------------------------------------------------- sound grammar (v6)
# Corrected sound grammar (Batch 36, 48 measured soundmaps + B1/B2 passes):
# Sky's base is DRY VOICE ONLY — music bed ABSENT in every measured talking
# reel, ordinary edit SFX (whoosh/pop/riser/ding) 0 confirmed corpus-wide.
# The ONE designed-sound family is the TICK-TONE: a faint, gated, fixed-
# frequency pulsed tone at animation beats (B2 finding, zoom-verified):
# pulsed trains at exactly 5,926 Hz (~13-17 pulses/s) ride counters,
# timers, count-ups and chart draws; gated tones (~9.15 kHz; a sustained
# ~11.1+11.85 kHz two-tone) ride two graphic-landing beats. Origin (edit
# micro-SFX vs captured device sound) is unproven — the soundmaps say so —
# but the beat-sync is measured. Q-lane divergence stays: sound on 100% of
# device entrances AND exits from the licensed library (SKY-PLUS target).
TICK_TONE_SPEC = {
    "family": "tick-tone (gated, fixed-frequency, pulsed)",
    "pulse_hz": 5926,
    "pulse_rate_per_s": "13-17",
    "gated_hz": [9150, 11100, 11850],
    "rides": ["counters", "timers", "count-ups", "chart draws"],
    "instances": [
        "DfPxqFPAY4_ 19.64-20.67s — 5,926 Hz train under the 10-second timer (sharpness 0.34)",
        "DfDuMnCjNdE 10.42-11.68s — 5,926 Hz train on the view-counts landing (peaks -28 dBFS)",
        "DfDuMnCjNdE 44.05-45.05s — 5,926 Hz train on the watch-time timer (sharpness 0.37)",
        "De-A2dvCeV3 17.50-18.16s — 5,926 Hz train on the 'High Engagement' chart draw",
        "Dez4fPJCR74 57.82-58.57s — 5,926 Hz train on the closing payment count-up pills (loudest; band peaks -19 dBFS)",
        "DfDuMnCjNdE 0.42-1.07s + DfX2qwQGagM 0.6-1.2s — gated ~9.15 kHz tone at funnel/head-cloud openings",
        "DfX2qwQGagM 34.41-34.86s + 43.98-44.40s — sustained ~11.1+11.85 kHz two-tone at graphic landings",
    ],
    "local_match": "NO LOCAL MATCH VERIFIED — no ear-matched local file; do not substitute a generic tick without an ear match",
    "status": "VERIFIED (Batch 36 B2; tonal sharpness >=0.30 + zoom spectrograms)",
}


def _tick_sound(beat):
    """The measured tick-tone sound spec for a counter/timer/count-up/chart beat."""
    return {"tick_tone": dict(TICK_TONE_SPEC, beat=beat),
            "notes": "Sky measured: faint gated tick-tone rides this beat class; "
                     "everything else in Sky is dry. Q lane: licensed-library "
                     "sound on entrance AND exit regardless (SKY-PLUS)."}


def validate_event(ev: dict) -> list[str]:
    """Return a list of problems with one event (empty = clean)."""
    problems = []
    if ev.get("device") not in DEVICE_REGISTRY:
        problems.append(f"{ev.get('device')}: unknown/unregistered device — "
                        "premium plans may only use registered D-devices")
    if ev["t1"] <= ev["t0"]:
        problems.append(f"{ev['device']}: t1 <= t0 ({ev['t0']}->{ev['t1']})")
    g = ev["geometry"]
    if g["x"] < 0 or g["y"] < 0 or g["x"] + g["w"] > CANVAS_W or g["y"] + g["h"] > CANVAS_H:
        problems.append(f"{ev['device']}: geometry outside 1080x1920 canvas: {g}")
    full_frame = g["w"] == CANVAS_W and g["h"] == CANVAS_H
    if g["y"] < 250 and not full_frame and ev["device"] not in TOP_ZONE_MEASURED:
        problems.append(f"{ev['device']}: geometry y={g['y']} enters IG top UI zone (must be >= ~280, title baseline >= 300)")
    if ev["device"] in TOP_ZONE_MEASURED and g["y"] < 250:
        # Measured Sky placement (see TOP_ZONE_MEASURED) — kept as measured;
        # the Q-lane plan must record the safe-zone decision per take.
        pass
    for hit in scan_object_for_forbidden(ev.get("colors", {})):
        problems.append(f"{ev['device']}: forbidden colour {hit}")
    for key, val in (ev.get("colors") or {}).items():
        if isinstance(val, str) and val.startswith("#") and is_forbidden(val):
            problems.append(f"{ev['device']}: forbidden colour {key}={val}")
    return problems


# ---------------------------------------------------------------- D1 captions
def caption_groups(words, max_words=CAPTION_MAX_WORDS, max_chars=CAPTION_MAX_CHARS,
                   era="df"):
    """Word-level transcript -> caption groups (measured Sky rule).

    words: [{"word": str, "start": float, "end": float}, ...]
    Breaks at max_words, max_chars, or sentence punctuation. Sky speaks
    ~4.3 wps, so groups change every ~0.5 s — that cadence falls out of the
    word timings, it is not imposed.

    era: "df" (default, Df-era priority reels, v3) = 1-3 words/group.
    "dcc" (Dcc-era, Dcc84V5jc6D, Aug 25 2026 — predates the priority reels)
    = 2-5 words/group, median ~0.6 s, range 0.33-1.28 s, speaking rate
    4.81 wps (above v3's 3.93-4.73). Era difference, NOT a v3 correction —
    never mix both variants in one video (EDIT-TEARDOWN.md T-02, §4).
    Dcc break rule (FIX Batch 18 QC F1): max 5 words AND break once the
    group text reaches 21 chars (DCC_CAPTION_MAX_CHARS) — the 14-char
    Q-lane cap splits Sky's measured 5-word groups. A lone word ending in
    phrase punctuation ("," / ";" / ":") is merged back into the previous
    group when that group has <5 words and does not end a sentence
    ("."/"?"/"!") — e.g. "Because the thing about" + "it," becomes
    "Because the thing about it,". A lone word stays alone only when no
    merge is possible (neighbours full at 5 words, e.g. "CTA," 35.54 s) or
    it follows a sentence end (e.g. "First," in the fixture) — that is the
    documented punctuation case, never a silent orphan.
    """
    if era == "dcc":
        max_words = 5
        max_chars = DCC_CAPTION_MAX_CHARS
    elif era != "df":
        raise ValueError(f"era must be 'df' or 'dcc', got {era!r}")
    groups, cur = [], []
    for w in words:
        cur.append(w)
        text = " ".join(x["word"] for x in cur)
        if (len(cur) >= max_words or len(text) >= max_chars
                or w["word"].endswith((".", ",", "?", "!", ":", ";"))):
            groups.append({"text": text, "t0": round(cur[0]["start"], 3),
                           "t1": round(cur[-1]["end"], 3)})
            cur = []
    if cur:
        groups.append({"text": " ".join(x["word"] for x in cur),
                       "t0": round(cur[0]["start"], 3), "t1": round(cur[-1]["end"], 3)})
    if era == "dcc":
        # Merge a stranded phrase-punctuation word back into its phrase
        # (see docstring). Sentence-final orphans and orphans whose
        # neighbours are full at 5 words stay — documented punctuation case.
        merged = []
        for g in groups:
            if (len(g["text"].split()) == 1
                    and g["text"].endswith((",", ";", ":"))
                    and merged
                    and len(merged[-1]["text"].split()) < 5
                    and not merged[-1]["text"].endswith((".", "?", "!"))):
                merged[-1]["text"] = merged[-1]["text"] + " " + g["text"]
                merged[-1]["t1"] = g["t1"]
            else:
                merged.append(g)
        groups = merged
    return groups


def d1_captions(words, *, y=CAPTION_Y, font_px=CAPTION_FONT_PX,
                source_reel="DfX2qwQGagM", era="df", gold_words=None):
    # y is the caption CENTRE. sky_build_plan computes it per take as
    # chin + 69 px (chin + 40 px clearance + half the 58 px text); the
    # default is the DfX2/DfQ4 frame measurement (~y1240/1920).
    """D1 speech caption stream. VERIFIED.

    All-white, bare text, no box/pill, chest band, chin +>=40px. IN = hard
    cut to full size in <=1 frame (<=0.033 s) — a step, no ramp. OUT ~0.5 s
    pop/fade. One group at a time; previous fully gone before the next lands.

    era="dcc" (Dcc84V5jc6D): 2-5 words/group AND the accent word lives
    INSIDE the caption in yellow — gold in Q's lane — on (a) the hook
    accent, (b) the current template-beat name, (c) key figures; everything
    else white. Pass those words as gold_words (lowercased match). Default
    era="df" keeps the v3 all-white captions + separate headline (G-01).
    """
    events = []
    gold_set = {w.lower().strip(".,!?;:") for w in (gold_words or [])}
    for g in caption_groups(words, era=era):
        # Width estimate: ~0.55 * font_px per char is generous for bold grotesque.
        w = min(860, max(120, int(len(g["text"]) * font_px * 0.52)))
        keyword = None
        if era == "dcc":
            for word in g["text"].split():
                if word.lower().strip(".,!?;:") in gold_set:
                    keyword = word.strip(".,!?;:")
                    break
        colors = {"text": WHITE}
        items = []
        if keyword:
            colors["keyword"] = GOLD
            items = [{"keyword": keyword,
                      "notes": "Dcc-era in-caption gold keyword (beat name / "
                               "figure / hook accent only — never filler words)"}]
        events.append(_base(
            "D1", "speech caption", g["t0"], g["t1"], TRACKS["captions"],
            _geom(540 - w // 2, y - font_px // 2, w, font_px + 16),
            status="VERIFIED", source_reel=source_reel,
            colors=colors,
            text=g["text"], items=items,
            motion={"in": {"type": "hard_cut", "dur_s": 0.033,
                           "easing": "step", "notes": "full size in <=1 frame, no ramp"},
                    "out": {"type": "pop_fade", "dur_s": CAPTION_OUT_S, "easing": "power4.out"}},
            notes=("2-5 words/group, Dcc-era in-caption gold keyword "
                   "(EDIT-TEARDOWN.md T-02); never mix with the Df-era "
                   "all-white variant in one video." if era == "dcc" else
                   "1-3 words/group, all-white, no highlight; accent word is a "
                   "separate headline device, never a caption highlight (G-01 resolved).")))
    return events


# ---------------------------------------------------------------- D2 headline
def d2_headline_lockup(t0, *, kicker, display_lines, family="green",
                       hold_s=5.0, y=1250, source_reel="DfX2qwQGagM"):
    # y is the block TOP. sky_build_plan computes it per take as chin + 80 px
    # (DfX2 measured block y~1245-1575/1920, chin ~y1170). The block ends
    # past the y1480 safe-zone bottom in Sky's own videos — that is
    # Sky-measured behaviour, flagged in the plan; the frame audit decides.
    """D2 mixed-scale headline lockup. VERIFIED (DfX2).

    Small white lowercase kicker (30-34 px) above 2 lines of huge bold
    condensed display (105-125 px, ~68% frame width), chest band, face-clear.
    Holds ~5 s, hard-pop exit. In: pop ~0.3 s slight overshoot + kicker fade
    0.2 s delayed 0.05 s. Q: kicker white, main lines gold, framework keyword teal.
    """
    accent = _accent(family)
    w = 735  # ~68% of 1080
    return [_base(
        "D2", "headline lockup", t0, t0 + hold_s, TRACKS["chip"],
        _geom(540 - w // 2, y, w, 300),
        status="VERIFIED", source_reel=source_reel,
        colors={"kicker": WHITE, "display": GOLD, "keyword": TEAL, "accent": accent},
        text={"kicker": kicker, "display": display_lines},
        motion={"in": {"type": "pop", "dur_s": POP_S, "easing": "back.out_1.141",
                       "kicker_fade_s": 0.2, "kicker_delay_s": 0.05,
                       "keyframes": keyframes("back.out_1.141", POP_S, n=6, start=0.88, end=1.0)},
                "out": _hard_cut_out()},
        sfx="pop-medium-in.wav",
        notes="Display 105-125 px cap height; kicker 30-34 px; holds ~5 s. "
              "Measured DfX2: block y~1245-1575/1920, over the torso below the "
              "chin — ends past the y1480 safe-zone bottom; frame audit decides "
              "per take.")]


# ---------------------------------------------------------------- D3 title stack
def d2_hook_build(t0, *, steps, family="green", source_reel="Dcc84V5jc6D"):
    """D2 Dcc-era variant — hook headline, mixed-size word build + 5-frame
    fade-out (T-01, Dcc84V5jc6D). VERIFIED.

    The hook BUILDS word by word as Sky speaks it, in mixed sizes in ONE
    lockup: small white setup words (~55 px), one large white word (~110 px,
    gold rule under it in Q's lane — Sky's thin red rule remapped), the
    accent phrase HUGE in gold (~130 px cap height, two lines). Top zone
    y80-450, centred, overlapping the lamp glow (never the face). Each word
    pops in ON its spoken word (hard cut, <=1 f). Full headline holds, then
    exits with a 5-frame PROGRESSIVE fade-out (0.167 s) on the word after
    the hook — NOT a hard cut. That 5-frame fade is one of only TWO measured
    fades in Option 1 (the other is D31's 10-frame count-up exit); it is a
    measured exception, not a general fade permission.

    steps: [{"word": str, "t": float, "size_px": int,
             "role": "small"|"large"|"accent"}, ...] — one entry per build
    word, in spoken order. t1 = last step t + hold (default 1.4 s to cover
    the measured 1.88-3.27 s hold) + 0.167 s fade.
    """
    if not steps:
        raise ValueError("d2_hook_build needs at least one build step")
    accent = _accent(family)
    role_color = {"small": WHITE, "large": WHITE, "accent": GOLD}
    for s in steps:
        if s["role"] not in role_color:
            raise ValueError(f"step role must be small/large/accent, got {s['role']!r}")
        if s["t"] < t0 - 1e-9:
            raise ValueError(f"build step {s['word']!r} at {s['t']} precedes t0 {t0}")
    hold_end = steps[-1]["t"] + 1.4
    return [_base(
        "D2", "hook headline (mixed-size build)", t0, hold_end + frames_to_s(5),
        TRACKS["chip"],
        _geom(200, 80, 680, 370),
        status="VERIFIED", source_reel=source_reel,
        colors={"small": WHITE, "large": WHITE, "accent": GOLD,
                "rule": GOLD, "accent_family": accent},
        text={"build": [(s["word"], s["size_px"], s["role"]) for s in steps]},
        items=[{"word": s["word"], "t": s["t"], "size_px": s["size_px"],
                "role": s["role"]} for s in steps],
        motion={"in": {"type": "word_build", "easing": "step",
                       "notes": "each word hard-cuts in full size on its spoken word (<=1 f)"},
                "out": {"type": "fade", "dur_s": frames_to_s(5),
                        "notes": "MEASURED 5-frame progressive fade-out (3.27-3.43 s, "
                                 "brightness 79,283->2,722 px) — one of only two "
                                 "measured fades in Option 1; not a general fade permission"}},
        notes="Dcc-era D2 variant (T-01): mixed sizes in ONE lockup, word-by-word "
              "build on the spoken words, accent phrase huge in gold, 5-frame "
              "fade-out. Top zone y80-450 (TOP_ZONE_MEASURED). The red underline "
              "under the large word becomes a GOLD rule in Q's lane.")]


# ---------------------------------------------------------------- D3 title stack
def d3_title_stack(t0, *, title, sections, family="green", swap_s=10.0,
                   source_reel="DfQ4E1Hjn0n"):
    """D3 top title stack + item pill. VERIFIED (DfQ4).

    Framework title in accent (44-50 px), baseline y >= 300 (Q fix — Sky's
    own stack sits y 6-15%, inside IG's top UI zone). White rounded pill
    below (~55% frame width, ~4.5% frame height) carrying the current section
    label; pill swaps hard ~10 s each + ~0.3 s pop.
    """
    accent = _accent(family)
    inst = f"D3@{t0:.2f}"
    events = [_base(
        "D3", "title stack", t0, t0 + swap_s * max(1, len(sections)), TRACKS["chip"],
        _geom(90, 300, 900, 70),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"title": accent, "text": WHITE},
        text=title,
        motion={"in": _pop_in(), "out": _hard_cut_out()},
        notes="Title baseline y>=300 (Q fix). Pill y 360-440.")]
    pill_w, pill_h = 590, 86
    for i, section in enumerate(sections):
        st0 = t0 + i * swap_s
        events.append(_base(
            "D3", "section pill", st0, st0 + swap_s, TRACKS["chip"],
            _geom(540 - pill_w // 2, 380, pill_w, pill_h),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"pill_fill": WHITE, "pill_text": NAVY_DEEP, "accent": accent},
            text=section,
            motion={"in": _pop_in(), "out": _hard_cut_out()},
            sfx="pop-small-in.wav",
            notes=f"Pill {i + 1}/{len(sections)}: hard swap + ~0.3 s pop."))
    return events


# ---------------------------------------------------------------- D4 filter board
def d4_filter_board(t0, *, board_title, rows, family="green",
                    row_gap_s=9.0, hairline_y=700, top_y=320,
                    source_reel="DfX2qwQGagM"):
    """D4 filter board. VERIFIED.

    Named board, criteria locked at top, rows judged one by one (~every
    6-12 s [EST] for the cadence; the verdict treatments are VERIFIED).
    Rows persist — the board fills = the open loop.
    Verdicts: reject = strikethrough + gold X pop (Sky red X remapped);
    approve = teal check; third state "Minimum" = small text label on the
    right of the row, no icon, no strikethrough, row text normal (DfX2).
    Board = glass card, top-centre, above the head.
    """
    accent = _accent(family)
    inst = f"D4@{t0:.2f}"
    # Hero zone is y320 -> hairline. Header 100 px; rows compress to fit.
    row_h = min(70, max(45, (hairline_y - top_y - 100) // max(1, len(rows))))
    board_h = 100 + row_h * len(rows)
    events = [_base(
        "D4", "filter board", t0, t0 + row_gap_s * len(rows), TRACKS["hero"],
        _geom(90, top_y, 900, board_h),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"board": NAVY, "board_opacity": 0.65, "title": WHITE, "accent": accent},
        text=board_title,
        motion={"in": _panel_in(), "out": _hard_cut_out()},
        sfx="pop-medium-in.wav",
        notes=f"Board fills as rows are judged; unfinished board = open loop. "
              f"Rows {row_h}px (compressed to fit above hairline y{hairline_y}).")]
    verdict_style = {
        "approve": {"label": "KEEP", "color": TEAL, "mark": "check", "strike": False},
        "reject": {"label": "PASS", "color": GOLD, "mark": "X", "strike": True},
        "minimum": {"label": "Minimum", "color": GREY_DIM, "mark": None, "strike": False},
    }
    for i, row in enumerate(rows):
        rt0 = t0 + i * row_gap_s
        verdict = verdict_style[row.get("verdict", "approve")]
        events.append(_base(
            "D4", f"board row {i + 1}: {row['label']}", rt0,
            t0 + row_gap_s * len(rows), TRACKS["hero"],
            _geom(120, top_y + 100 + i * row_h, 840, row_h - 10),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"row_pending": WHITE, "row_pending_opacity": 0.40,
                    "row_active_opacity": 1.0, "verdict": verdict["color"]},
            text=row["label"], items=[{"verdict": row.get("verdict", "approve"), **verdict}],
            motion={"in": {"type": "opacity_keyframe", "dur_s": 0.15,
                           "easing": "ease_out_cubic", "from": 0.40, "to": 1.0,
                           "notes": "opacity 40->100% over 0.15 s on first spoken word"},
                    "verdict_in": {"type": "pop", "dur_s": 0.18, "easing": "back.out_1.141",
                                   "scale_from": 1.6, "notes": "verdict chip pop 1.6->1.0"},
                    "out": _hard_cut_out()},
            sfx="pop-small-in.wav",
            notes="Reject: strikethrough + gold X. Approve: teal check. "
                  "Minimum: small text label right, no icon/strike (DfX2 VERIFIED)."))
    return events


# ---------------------------------------------------------------- D5 chapter card + checklist
def d5_chapter_card(t0, *, numeral, name, definition, family="green",
                    hold_s=10.0, top_y=320, hairline_y=700, source_reel=""):
    """D5 numbered chapter card. [EST] — parameters from D2/D3 grammar.

    Big two-digit numeral (150-220 px extra-bold) + name (54-64 px bold
    white) + one-line definition (34-40 px regular white 80%). Previous
    chapters dim to 45% but stay listed. No frame-matched Q build yet (G-07).
    """
    accent = _accent(family)
    return [_base(
        "D5", f"chapter card {numeral:02d}", t0, t0 + hold_s, TRACKS["hero"],
        _geom(90, top_y, 900, min(380, hairline_y - top_y - 20)),
        status="[EST]", source_reel=source_reel or "UNSET — no frame-matched build yet",
        colors={"numeral": accent, "name": WHITE, "definition": WHITE},
        text={"numeral": f"{numeral:02d}", "name": name, "definition": definition},
        motion={"in": _pop_in(),
                "out": _hard_cut_out()},
        sfx="pop-medium-in.wav",
        notes="[EST] numeral 150-220 px, name 54-64 px, definition 34-40 px. "
              "Entrance is the measured pop (the old Slide Left 0.3 s is cut "
              "Nov 9, Batch 19). "
              "See d5_checklist() for the VERIFIED DfQ4 numbered-list variant.")]


def d5_checklist(t0, *, title, items, family="green", hairline_y=700,
                 top_y=300, source_reel="DfQ4E1Hjn0n"):
    """D5 measured variant — numbered white-pill checklist. VERIFIED (DfQ4).

    Measured Nov 9 from 05_DfQ4E1Hjn0n.mp4 frames at 0.6 s and 1.5 s:
    accent title ("5 Content Types") top, then 5 white rounded pills
    stacked, each "0N Name". Pending rows sit blurred/dim and sharpen as
    they appear; the current row highlights in the accent when its section
    starts. Returns at each section start and as a full recap at the close.
    This is what DfQ4 actually shows — the big-numeral chapter card
    (d5_chapter_card) is a different, still-[EST] device. Closes G-07 D5
    as "checklist VERIFIED, chapter card still [EST]".
    """
    accent = _accent(family)
    row_h = min(100, max(50, (hairline_y - top_y - 80) // max(1, len(items))))
    events = [_base(
        "D5", "numbered checklist", t0, t0 + 10.0 * max(1, len(items)), TRACKS["hero"],
        _geom(180, top_y, 720, hairline_y - top_y),
        status="VERIFIED", source_reel=source_reel,
        colors={"title": accent, "pill_fill": WHITE, "pill_text": NAVY_DEEP,
                "active_highlight": accent},
        text=title, items=[{"index": i + 1, "label": it} for i, it in enumerate(items)],
        motion={"in": _panel_in(), "out": _hard_cut_out()},
        sfx="pop-medium-in.wav",
        notes=f"VERIFIED DfQ4: rows appear one at a time ~0-1.2 s at the open; "
              f"pending rows blurred/dim, active row sharp + accent highlight; "
              f"recurs per section (~6/17/31.5/44.5/60.5 s) + full recap ~70.5 s. "
              f"Rows {row_h}px (compressed to fit above hairline y{hairline_y}; "
              f"DfQ4 measured ~82px with that reel's lower hairline ~840).")]
    return events


# ---------------------------------------------------------------- D6 chart
def d6_chart(t0, *, title, annotations, family="green", top_y=320,
             hairline_y=700, source_reel="DfPxqFPAY4_"):
    """D6 retention/views chart. VERIFIED — static base + stacking annotations.

    The line does NOT draw on continuously (G-04 CONFIRMED NOT SKY): the
    "Views over time" line is already drawn; VALUES update (1.1M -> 2.6M ->
    2.7M) and annotations ("Second push" / "New surge") appear on top,
    ~10 s apart, each pop/draw ~0.3-1 s. Any draw-on/mask-reveal in a Q build
    is a Q construction choice, NOT Sky's verified motion — the plan flags it.
    """
    accent = _accent(family)
    inst = f"D6@{t0:.2f}"
    events = [_base(
        "D6", "chart (static base)", t0,
        t0 + 10.0 * max(1, len(annotations)), TRACKS["hero"],
        _geom(90, top_y, 900, min(380, hairline_y - top_y - 20)),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"line": accent, "axis": WHITE, "grid": GREY_DIM},
        text=title,
        motion={"in": _panel_in(), "out": _hard_cut_out()},
        notes="STATIC base. Line already drawn at t0 — no continuous draw-on "
              "(G-04). Values update + annotations stack on top.")]
    for i, ann in enumerate(annotations):
        at0 = t0 + i * 10.0
        events.append(_base(
            "D6", f"chart annotation: {ann.get('label', '')}", at0, at0 + 10.0,
            TRACKS["chip"],
            _geom(120, 360 + (i % 3) * 90, 840, 80),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"annotation": accent if ann.get("payoff") else WHITE},
            text=ann.get("label", ""), items=[{"value": ann.get("value", "")}],
            motion={"in": {"type": "pop", "dur_s": 0.3, "easing": "back.out_1.141"},
                    "out": _hard_cut_out()},
            sfx="pop-small-in.wav", sound=_tick_sound("chart draw / value landing"),
            notes="Annotation pops/draws ~0.3-1 s, ~10 s apart; value lands on "
                  "the spoken figure. Tick-tone rides chart draws (De-A2dvCeV3 "
                  "17.50-18.16s, Batch 36 B2)."))
    return events


# ---------------------------------------------------------------- D7 Venn
def d7_venn(t0, *, left_label, right_label, figure, family="green",
            hold_s=10.0, source_reel="DfPxqFPAY4_"):
    """D7 Venn/overlap. VERIFIED (DfPxq 'crossover').

    Two overlapping circles ('Your audience' / 'Their audience'), solid
    accent lens/diamond in the overlap, faces in circles at the top of each
    circle, centred above his head. Count-up lands ON the spoken figure.
    """
    accent = _accent(family)
    return [_base(
        "D7", "venn overlap", t0, t0 + hold_s, TRACKS["hero"],
        _geom(140, 320, 800, 380),
        status="VERIFIED", source_reel=source_reel,
        colors={"left": TEAL, "right": GOLD, "overlap": accent,
                "left_opacity": 0.45, "right_opacity": 0.45},
        text={"left": left_label, "right": right_label, "figure": figure},
        motion={"in": {"type": "pop", "dur_s": 0.3, "easing": "back.out_1.141",
                       "scale_from": 0.8, "stagger_s": 0.1,
                       "notes": "measured graphic entrance family (pop/scale "
                                "~0.3 s); the old scale+fade is cut Nov 9, Batch 19"},
                "count_up": {"type": "count_up", "dur_s": COUNT_UP_S, "easing": "expo.out",
                             "notes": "lands ON the spoken figure"},
                "out": _hard_cut_out()},
        sfx="pop-medium-in.wav",
        notes="Circles teal/gold at 45% opacity; overlap filled in the accent.")]


# ---------------------------------------------------------------- D8 rewrite pair
def d8_rewrite_pair(t0, *, before, after, swapped_old, swapped_new,
                    family="green", hold_s=3.0, source_reel="DfLaEFNDKkv"):
    """D8 before->after rewrite pair. VERIFIED layout (DfLa).

    List upper ~45% of frame, items stack 1-5, list headline stays ~45 s;
    bottom splits 50/50 after a hard cut at ~20 s. Before dims (and/or
    strikes) as the after arrives; swapped words: old grey / new gold in
    Q's lane (Sky: old orange / new green). After-line entrance is
    UNVERIFIED — default is the DfLa hard-cut pop (G-06); the old Slide Up
    0.25 s is cut Nov 9, Batch 19.
    """
    return [_base(
        "D8", "rewrite pair", t0, t0 + hold_s, TRACKS["hero"],
        _geom(90, 320, 900, 380),
        status="VERIFIED", source_reel=source_reel,
        colors={"before": WHITE, "before_dim_opacity": 0.35,
                "after": WHITE, "old_word": GREY_DIM, "new_word": GOLD},
        text={"before": before, "after": after,
              "swapped_old": swapped_old, "swapped_new": swapped_new},
        motion={"in": {"type": "pop", "dur_s": 0.25, "easing": "back.out_1.141",
                       "notes": "after-line entrance UNVERIFIED (G-06); default is the "
                                "DfLa hard-cut pop; the old Slide Up 0.25 s is cut "
                                "Nov 9, Batch 19"},
                "before_dim": {"type": "opacity_strike", "dur_s": 0.2},
                "out": _hard_cut_out()},
        sfx="pop-small-in.wav",
        notes="Layout VERIFIED DfLa; entrance placeholder per G-06.")]


# ---------------------------------------------------------------- D9 exhibit
def d9_exhibit_insert(t0, *, label, clip_path, duration_s, full_frame=True,
                      source_reel="DfU49SJAFYH"):
    """D9 exhibit clip insert. VERIFIED.

    Labelled example footage, full-frame or majority-frame, principle-label
    chip. Hard-cut entry; exhibits do NOT freeze while he talks over them;
    thumbnail-style inserts exit with motion-blur slides.
    """
    return [_base(
        "D9", "exhibit insert", t0, t0 + duration_s, TRACKS["asset"],
        _geom(0, 0, 1080, 1920) if full_frame else _geom(90, 320, 900, 1100),
        status="VERIFIED", source_reel=source_reel,
        colors={"chip": NAVY, "chip_opacity": 0.55, "chip_text": WHITE},
        text=label, items=[{"clip": clip_path, "full_frame": full_frame}],
        motion={"in": {"type": "hard_cut"},
                "out": {"type": "motion_blur_slide", "dur_s": 0.3}},
        notes="Hard-cut entry; exhibit plays, never freezes.")]


# ---------------------------------------------------------------- D10 profile/grid
def d10_profile_insert(t0, *, label, screen_path, duration_s=8.0,
                       floating=True, source_reel="DfPxqFPAY4_"):
    """D10 profile/grid insert. VERIFIED (real screen only, never a redrawn fake).

    Real IG profile, grid, results row, or document at the claim moment.
    Floating variant bobs (y +/-10 px, 2.4 s loop) + rotation +/-1.5 deg.
    Gentle bob is measured on Sky's floating elements (head cutouts bob
    gently, DfA9 @0-2.8 s, DfIY @6.5-11 s; cards bob slightly, DfDu @26-30 s);
    the +/-10 px / 2.4 s / +/-1.5 deg values are [EST].
    Follow -> Following state change: NOT SEEN in any reel (G-11) — build
    from Q's description, not from a Sky frame.
    """
    return [_base(
        "D10", "profile/grid insert", t0, t0 + duration_s, TRACKS["asset"],
        _geom(140, 320, 800, 380),
        status="VERIFIED", source_reel=source_reel,
        colors={"text": WHITE},
        text=label, items=[{"screen": screen_path, "floating": floating}],
        motion={"in": _pop_in(),
                "float": {"type": "bob", "y_px": 10, "period_s": 2.4,
                          "rotation_deg": 1.5} if floating else None,
                "out": {"type": "motion_blur_slide", "dur_s": 0.3}},
        notes="REAL screen recording only. Hidden-method material passes the "
              "blur law BEFORE the timeline. Gentle bob measured on Sky's "
              "floating elements (see docstring); values [EST].")]


# ---------------------------------------------------------------- D11 chip cloud
def d11_chip_cloud(t0, *, words_list, family="green", layout="ring",
                   stagger_s=0.3, source_reel="DeYKkAIgVfL"):
    """D11 trait-word chip cloud. VERIFIED (DeYKk).

    Single descriptive words land one by one as chips around the subject.
    DeYKk measured form: accent dots in a dotted arc above the phone frame
    + a quiz card whose words accumulate as a vertical list (Legit, Business,
    Very Successful, ...). Layout 'ring' (face-clear side zones) or 'arc_list'.
    """
    accent = _accent(family)
    inst = f"D11@{t0:.2f}"
    events = []
    for i, word in enumerate(words_list):
        wt0 = t0 + i * stagger_s
        events.append(_base(
            "D11", f"chip: {word}", wt0, wt0 + 6.0, TRACKS["chip"],
            _geom(90 + (i % 3) * 300, 340 + (i // 3) * 110, 280, 80),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"chip_fill": NAVY, "chip_fill_opacity": 0.60,
                    "chip_text": WHITE, "dot": accent},
            text=word,
            motion={"in": {"type": "pop", "dur_s": 0.15, "easing": "back.out_1.141"},
                    "out": _hard_cut_out()},
            sfx="pop-small-in.wav",
            notes=f"Chip {i + 1}/{len(words_list)}, stagger {stagger_s} s; "
                  "layout 'arc_list' = dotted arc + accumulating vertical list (DeYKk). "
                  "Chips exit by hard cut (measured §5 Exits; the old fade-together "
                  "out is cut Nov 9, Batch 19)."))
    return events


# ---------------------------------------------------------------- D12 timeline
def d12_timeline(t0, *, nodes, family="orange", source_reel="De-A2dvCeV3"):
    """D12 era timeline. VERIFIED Nov 9 (De-A2dvCeV3 frames @40.2/41.2 s).

    Measured mechanics (closes G-07 D12): the line is STATIC and FULL-WIDTH
    from the first frame — it does NOT extend progressively. Nodes pop in
    sequence ~0.5 s apart; each node = accent ring + filled dot on the line,
    label ABOVE the line. Past-era labels white; the current/future-era label
    in the accent. The active node's example thumbnails cluster UNDER it
    (2x3 grid, dashed accent border). Line y ~300/1920 (top zone, above head).
    Two-era treatment still [EST] — only the 3-node case is measured.
    """
    accent = _accent(family)
    inst = f"D12@{t0:.2f}"
    events = [_base(
        "D12", "era timeline (line)", t0, t0 + 0.5 * len(nodes) + 3.0, TRACKS["hero"],
        _geom(60, 300, 960, 30),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"line": accent, "line_width_px": 4},
        text="timeline",
        motion={"in": {"type": "hard_cut",
                       "notes": "line is FULL-WIDTH at t0 — no draw-on extension"},
                "out": _hard_cut_out()},
        notes="VERIFIED De-A2dvCeV3: static full line; nodes pop ~0.5 s apart; "
              "labels above line; current-era label in accent; example thumbs "
              "cluster under the active node.")]
    for i, node in enumerate(nodes):
        nt0 = t0 + i * 0.5
        x = 120 + i * (840 // max(1, len(nodes) - 1) if len(nodes) > 1 else 0)
        events.append(_base(
            "D12", f"timeline node: {node.get('label', '')}", nt0, nt0 + 3.5,
            TRACKS["hero"],
            _geom(x - 110, 200, 220, 100),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"ring": accent, "dot": accent,
                    "label": accent if node.get("current") else WHITE},
            text=node.get("label", ""),
            items=[{"thumbs": node.get("thumbs", []),
                    "thumb_cluster": "2x3 grid, dashed accent border, under node"
                    if node.get("thumbs") else None}],
            motion={"in": {"type": "pop", "dur_s": 0.2, "easing": "back.out_1.141"},
                    "out": _hard_cut_out()},
            sfx="pop-small-in.wav",
            notes="Node = accent ring + filled dot; label above line; "
                  "current-era label in accent, past eras white."))
    return events


# ---------------------------------------------------------------- D13 workflow strip
def d13_workflow_strip(t0, *, steps, family="green", step_gap_s=8.0,
                       top_y=380, source_reel="DfQ4E1Hjn0n"):
    """D13 workflow strip. [EST] mechanics, D5-index grammar.

    Horizontal row of named process steps; each activates as spoken
    (opacity 40->100% + teal underline keyframe). Header = D3 title
    treatment at y >= 300.
    """
    inst = f"D13@{t0:.2f}"
    events = []
    for i, step in enumerate(steps):
        st0 = t0 + i * step_gap_s
        events.append(_base(
            "D13", f"workflow step {i + 1}: {step}", st0,
            t0 + step_gap_s * len(steps), TRACKS["hero"],
            _geom(90 + i * (900 // max(1, len(steps))), top_y, 860 // max(1, len(steps)), 110),
            status="[EST]", source_reel=source_reel, instance=inst,
            colors={"step_pending_opacity": 0.40, "step_active_opacity": 1.0,
                    "underline": TEAL, "text": WHITE},
            text=step,
            motion={"in": {"type": "opacity_keyframe", "dur_s": 0.15,
                           "from": 0.40, "to": 1.0,
                           "underline": "teal underline keyframe on activation"},
                    "out": _hard_cut_out()},
            sfx="pop-small-in.wav",
            notes="[EST] activation timing; step geometry from D5-index grammar."))
    return events


# ---------------------------------------------------------------- D14 end beat
def d14_end_beat(t0, *, close_line, keyword="WAITLIST", ending="card",
                 hold_s=1.2, top_y=320, hairline_y=700, source_reel=""):
    """D14 end beat + Q endings. Q OVERRIDE (Sky: most reels have NO end card).

    Completed hero device held on the closing line (0.8-1.5 s)
    over the completed graphic + logo/keyword end moment <=1 s after the last
    spoken word. Endings rotate: card / comments / notifs (STYLE-GRAMMAR §8).
    [Door device removed Nov 9, 2026 — door is dead per Q's standing rule.]
    """
    return [_base(
        "D14", "end beat", t0, t0 + hold_s, TRACKS["hero"],
        _geom(90, top_y, 900, min(380, hairline_y - top_y - 20)),
        status="VERIFIED", source_reel=source_reel or "Q override — Sky has no end card",
        colors={"logo": "pwc_logo.jpg (unaltered)", "cta": GOLD, "text": WHITE},
        text={"close_line": close_line, "keyword": keyword, "ending": ending},
        motion={"in": {"type": "hold_completed_device", "dur_s": hold_s},
                "out": {"type": "end_moment", "notes": "logo/keyword <=1 s after last word"}},
        sfx="pop-medium-in.wav",
        notes=f"Ending style: {ending} (rotate card/comments/notifs). "
              "Doors locked until Mon Dec 7, 2026; keyword flow must be live.")]


# ------------------------------------------------------- D15-D25 (v3 devices)
def d15_bar_chart(t0, *, rows, family="orange", source_reel="Dez4fPJCR74"):
    """D15 script-anatomy bar chart. VERIFIED (Dez4).

    Left-aligned labels (Hook / Lead / Body 1 / Open loop 1 / ...) +
    horizontal bars coloured per part (Sky: Hook red, Lead yellow, Body blue,
    CTA green — REMAPPED in Q's lane: Hook gold, Lead gold, Body teal, CTA
    teal; never red). Circular loop icon on open-loop rows.
    """
    accent = _accent(family)
    bar_color = {"hook": GOLD, "lead": GOLD, "body": TEAL, "open_loop": TEAL,
                 "cta": GOLD}.get
    inst = f"D15@{t0:.2f}"
    events = []
    for i, row in enumerate(rows):
        rt0 = t0 + i * 0.6
        kind = row.get("kind", "body")
        events.append(_base(
            "D15", f"anatomy bar: {row['label']}", rt0, rt0 + 8.0, TRACKS["hero"],
            _geom(90, 340 + i * 90, 900, 80),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"bar": bar_color(kind, TEAL), "label": WHITE, "accent": accent},
            text=row["label"],
            items=[{"kind": kind, "loop_icon": kind == "open_loop",
                    "width_frac": row.get("width_frac", 0.5)}],
            motion={"in": {"type": "bar_fill", "dur_s": 0.5, "easing": "power4.out",
                         "notes": "bar fills L->R; loop icon pops on open-loop rows"},
                    "out": _hard_cut_out()},
            sfx="pop-small-in.wav",
            notes="Sky bar colours remapped: red/yellow/blue/green -> gold/teal. "
                  "Loop icon = circular icon on open-loop rows."))
    return events


def d16_branch_line(t0, *, label, duration_s=3.0, family="orange",
                    source_reel="Dez4fPJCR74"):
    """D16 branch line. VERIFIED (Dez4).

    A thin accent L-shaped line drawing from top-left down then right, with
    a small text label — the branch transition.
    """
    accent = _accent(family)
    return [_base(
        "D16", "branch line", t0, t0 + duration_s, TRACKS["hero"],
        _geom(90, 300, 500, 300),
        status="VERIFIED", source_reel=source_reel,
        colors={"line": accent, "label": WHITE},
        text=label,
        motion={"in": {"type": "line_draw", "dur_s": 0.6, "easing": "linear",
                       "path": "L-shape: down then right",
                       "notes": "connectors draw AFTER their nodes land"},
                "out": _hard_cut_out()},
        notes="Thin accent L-line + small label; the branch transition.")]


def d17_dot_grid(t0, *, categories, flip_at_s=1.0, duration_s=8.0,
                 family="orange", source_reel="DeYKkAIgVfL"):
    """D17 trust dot-grid. VERIFIED (DeYKk).

    A grid of dots (the audience) whose dots flip red (lose trust) -> green
    (gain trust) — REMAPPED: lose trust = grey/dim, gain trust = teal (Q lane
    never shows red). Category labels (Community, Digital Product, Coaching,
    Course) + small profile faces around it.
    """
    return [_base(
        "D17", "trust dot-grid", t0, t0 + duration_s, TRACKS["hero"],
        _geom(140, 340, 800, 360),
        status="VERIFIED", source_reel=source_reel,
        colors={"dot_base": GREY_DIM, "dot_lose": GREY_DIM, "dot_gain": TEAL,
                "label": WHITE},
        text="trust dot-grid", items=[{"categories": categories}],
        motion={"in": _panel_in(),
                "flip": {"type": "dot_flip", "at_s": flip_at_s,
                         "notes": "dots flip dim (lose trust) -> teal (gain trust); "
                                  "Sky red/green remapped to grey/teal. Batch 36 "
                                  "strip-resolved (DeYKkAIgVfL): red/green dot-share "
                                  "crossover bracketed 4.20-4.53 s on the spoken "
                                  "'gain' — a state flip, not a fade"},
                "out": _hard_cut_out()},
        sound=None,
        notes="Sky red->grey, green->teal. Faces + category labels around the grid. "
              "DeYKk instance (Batch 36 B1): dashed connectors run from the grid "
              "to the category nodes (~6 s); the grid is present at frame 0 (its "
              "entrance is not observable); its EXIT in this instance is the "
              "corpus's only device fade (dims 10.4-10.8 s) followed by a whip-blur "
              "transition at ~10.9 s — a measured single-instance exception, not "
              "a general fade permission.") ]


def d18_network_loop(t0, *, profiles, duration_s=6.0, family="orange",
                     source_reel="DeYKkAIgVfL"):
    """D18 network loop. VERIFIED (DeYKk).

    A dashed curved line connecting profile photos (the 'affiliate army' /
    participation loop). Connectors draw AFTER their nodes land (0.4-2.4 s).
    """
    accent = _accent(family)
    return [_base(
        "D18", "network loop", t0, t0 + duration_s, TRACKS["hero"],
        _geom(90, 320, 900, 380),
        status="VERIFIED", source_reel=source_reel,
        colors={"line": accent, "line_style": "dashed"},
        text="affiliate army / participation loop",
        items=[{"profiles": profiles}],
        motion={"in": {"type": "line_draw", "dur_s": 1.2, "easing": "linear",
                       "notes": "dashed curve draws AFTER profile nodes land"},
                "out": _hard_cut_out()},
        notes="Dashed curved line connecting profile photos. DeYKk instance "
              "(Batch 36 B1): the loop runs ~66-79 s around/above his head with "
              "the subject's exhibit card inside the cluster; its label reads "
              "only in fragments ('Encouraging...' / 'Yap' legible ~74.7 s) — "
              "full label text UNVERIFIED, never invented.") ]


def d19_people_grid(t0, *, count_label, cols=10, rows_n=10, duration_s=4.0,
                    family="orange", source_reel="DeYKkAIgVfL"):
    """D19 '100s of people' grid. VERIFIED (DeYKk).

    A grid of many small accent squares — a visual count of people.
    """
    accent = _accent(family)
    return [_base(
        "D19", "people grid", t0, t0 + duration_s, TRACKS["hero"],
        _geom(140, 340, 800, 360),
        status="VERIFIED", source_reel=source_reel,
        colors={"square": accent},
        text=count_label,
        items=[{"cols": cols, "rows": rows_n, "count": cols * rows_n}],
        motion={"in": {"type": "stagger_pop", "dur_s": 0.8, "easing": "back.out_1.141",
                       "stagger_s": 0.02},
                "out": _hard_cut_out()},
        notes="Many small accent squares fill in as a visual count. DeYKk "
              "instance (Batch 36 B1): the cells are ~70 small play-icon "
              "squares (not plain squares); the headline ('100s of people "
              "started posting...') TYPES IN at ~76.9 s and the grid FILLS "
              "PROGRESSIVELY beneath it from ~77.0 s, landing ~1.2 s after "
              "the spoken line starts, on 'posting'.") ]


def d20_views_refresh(t0, *, view_counts, duration_s=6.0, family="orange",
                      source_reel="DeSTWxcDTA7"):
    """D20 views-refresh insert. VERIFIED (DeSTW).

    A 3x3 profile grid with per-video view counts (8,547 / 4,246 / 6,540) +
    'GOING VIRAL' labels, positioned above his head. Real screens only.
    """
    accent = _accent(family)
    return [_base(
        "D20", "views-refresh insert", t0, t0 + duration_s, TRACKS["asset"],
        _geom(140, 320, 800, 380),
        status="VERIFIED", source_reel=source_reel,
        colors={"label": accent, "count": WHITE},
        text="GOING VIRAL",
        items=[{"view_counts": view_counts}],
        motion={"in": _pop_in(), "out": _hard_cut_out()},
        sound=_tick_sound("view-counts landing"),
        notes="3x3 profile grid + per-video view counts + GOING VIRAL labels; "
              "real screen only. Tick-tone instance (Batch 36 B2): DfDuMnCjNdE "
              "view-counts landing 10.42-11.68 s carries the 5,926 Hz train.") ]


def d21_bw_beat(t0, *, hero_word, duration_s=1.4, family="orange",
                source_reel="DeSTWxcDTA7"):
    """D21 B&W beat. VERIFIED (DeSTW) — a Sky device, not just a PWC invention.

    The frame desaturates to B&W with ONE big accent word ('DON'T' in Sky's
    orange -> gold in Q's lane). Held 1-1.6 s. No impact sound (PWC engine).
    """
    return [_base(
        "D21", "B&W beat", t0, t0 + duration_s, TRACKS["aroll"],
        _geom(0, 0, 1080, 1920),
        status="VERIFIED", source_reel=source_reel,
        colors={"hero_word": GOLD, "frame": "desaturated (saturation 0)"},
        text=hero_word,
        motion={"in": {"type": "desaturate", "dur_s": 0.1,
                       "notes": "saturation 0 + 10% contrast + 1.22x scale (PWC engine)"},
                "out": {"type": "hard_cut"}},
        notes="Frame B&W + ONE big accent word (Q lane: bold grotesque gold, "
              "never serif — cut order Nov 9, Batch 19; Sky's DfA9 italic "
              "rendering is recorded in the examples only). No impact sound.")]


def d22_new_post_placeholder(t0, *, duration_s=4.0, family="orange",
                             source_reel="DeSTWxcDTA7"):
    """D22 'New Post' placeholder. VERIFIED (DeSTW).

    A dashed-border card with a '+' and 'New Post' that fills with thumbnails.
    """
    accent = _accent(family)
    return [_base(
        "D22", "new-post placeholder", t0, t0 + duration_s, TRACKS["hero"],
        _geom(240, 320, 600, 380),
        status="VERIFIED", source_reel=source_reel,
        colors={"border": accent, "border_style": "dashed", "text": WHITE},
        text="New Post",
        items=[{"plus": "+", "fills_with": "thumbnails"}],
        motion={"in": _pop_in(),
                "fill": {"type": "fill_thumbs", "dur_s": 0.8},
                "out": _hard_cut_out()},
        notes="Dashed card + '+' + 'New Post'; fills with thumbnails. DeSTW "
              "form 4b (Batch 36 B1 strip pass): the card sits top-right from "
              "16.0 s and finished-post thumbnails POP IN STAGGERED beside it "
              "(first ~17.0-17.2 s, cluster complete ~18.5-19.0 s) on a lit "
              "shelf line above his head. Form 4a — the B&W frame shrinking "
              "into the IG 'New reel' UI — is a different device: D56.") ]


def d23_floating_head(t0, *, duration_s=2.0, source_reel="DeSTWxcDTA7",
                      label=None, label_t=None, emojis=0, list_labels=None):
    """D23 floating head cutout — the floating-heads SYSTEM. VERIFIED (DeSTW).

    The speaker's own face cut out and popped in as a floating head.
    (Q lane: Q's own face cutout — RVM matte; never a stock/AI face.)
    DeSTWxcDTA7 (Batch 36 B1 strip pass) shows this is a recurring SYSTEM,
    not a one-off pop: heads pop at the frame edge / beside the grid / at
    chest height across the reel (~3-27 s), sometimes with a yellow
    play-triangle marker, and the system carries text three ways:
      * script accent word drawn in beside it ("Strategy work" draws in
        2.8-3.1 s at the left chest — the D50-family word; see d50);
      * ROLE LABEL: the head pops (~21.5 s), then its label TYPES IN
        beneath it (21.8-22.2 s — "Post Production Head"), with an accent
        underline bar under the cutout (~24 s). Recurs as the "Hire" head
        (~34.1 s) with role icons popping beside it (35.6 s / 36.0 s);
      * LABEL LIST: beside the persistent chest head, bullet labels land
        one at a time on their spoken words ("• Stable" ~40.2 s,
        "• Consistent" ~40.9 s — the close).
    label/list_labels: pass the measured label text + landing times to use
    the system forms; a bare call stays the original single-head pop.
    list_labels: [(text, t0), ...] in landing order.
    """
    inst = f"D23@{t0:.2f}"
    events = [_base(
        "D23", "floating head cutout", t0, t0 + duration_s, TRACKS["chip"],
        _geom(390, 340, 300, 300),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"text": WHITE},
        text="floating head",
        motion={"in": {"type": "pop", "dur_s": 0.3, "easing": "back.out_1.141"},
                "out": _hard_cut_out()},
        sfx="pop-medium-in.wav",
        notes="Own-face cutout only (RVM matte). Never stock/AI. Recurring "
              "system in DeSTW (pops ~3-27 s, Batch 36 B1); gentle bob is "
              "measured on Sky's floating elements (see D10).")]
    for i in range(emojis):
        events.append(_base(
            "D23", f"emoji pop {i + 1}", t0 + 0.5 + i * 0.2, t0 + duration_s,
            TRACKS["chip"],
            _geom(700 + i * 110, 640, 90, 90),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"text": WHITE},
            text="emoji",
            items=[{"notes": "yellow emoji faces pop beside the chest head "
                             "(DeSTW ~4.2 s, Batch 36 B1)"}],
            motion={"in": {"type": "pop", "dur_s": 0.2, "easing": "back.out_1.141"},
                    "out": _hard_cut_out()},
            notes="D23 system: emoji companions pop with the head."))
    if label:
        lt = label_t if label_t is not None else t0 + 0.3
        events.append(_base(
            "D23", f"head label: {label}", lt, lt + max(1.0, duration_s),
            TRACKS["chip"],
            _geom(290, 660, 500, 70),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"label": WHITE, "underline": GOLD},
            text=label,
            items=[{"label": label,
                    "notes": "label TYPES IN beneath the popped head "
                             "(DeSTW 'Post Production Head' 21.8-22.2 s); "
                             "accent underline bar under the cutout (~24 s)"}],
            motion={"in": {"type": "type_in", "dur_s": 0.4,
                           "notes": "types in word by word under the head"},
                    "out": _hard_cut_out()},
            notes="D23 system: role label typed under the floating head."))
    for i, (text, lt0) in enumerate(list_labels or []):
        events.append(_base(
            "D23", f"head list label: {text}", lt0, lt0 + 2.5,
            TRACKS["chip"],
            _geom(700, 900 + i * 70, 320, 60),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"label": WHITE},
            text=text,
            items=[{"label": text, "index": i + 1,
                    "notes": "bullet labels accumulate beside the persistent "
                             "chest head, one per spoken word (DeSTW close: "
                             "'• Stable' ~40.2 s, '• Consistent' ~40.9 s)"}],
            motion={"in": {"type": "pop", "dur_s": 0.2, "easing": "back.out_1.141"},
                    "out": _hard_cut_out()},
            notes="D23 system: accumulating label list beside the head."))
    return events


def d24_funnel_card(t0, *, rows, checklist, family="orange",
                    source_reel="DfA9L-PHYWp"):
    """D24 funnel card. VERIFIED (DfA9).

    Glass card, top-centre/left, rows (CONTENT -> CHECKOUT PAGE / VSL) + a
    'FEEDS INTO BRAND' accent bar; recap = numbered checklist (01 GOAL,
    02 AVATAR, 03 MARKET, 04 OFFER, 05 FUNNEL) with checkmarks, top-right;
    profile card + trait chips; script card with a moving magnifier/highlight.
    """
    accent = _accent(family)
    return [_base(
        "D24", "funnel card", t0, t0 + 10.0, TRACKS["hero"],
        _geom(90, 320, 900, 380),
        status="VERIFIED", source_reel=source_reel,
        colors={"card": NAVY, "card_opacity": 0.65, "bar": accent,
                "check": TEAL, "text": WHITE},
        text="funnel",
        items=[{"rows": rows, "checklist": checklist,
                "bar_label": "FEEDS INTO BRAND"}],
        motion={"in": _panel_in(), "out": _hard_cut_out()},
        sfx="pop-medium-in.wav",
        notes="Rows + accent FEEDS INTO BRAND bar; numbered checklist with "
              "checkmarks top-right; profile card + trait chips alongside.")]


def d25_autopsy_labels(t0, *, labels, chart_t0=None, source_reel="DfU49SJAFYH"):
    """D25 retention autopsy labels. VERIFIED (DfU49).

    Short 2-3-word labels with a check for good moments ('Throat mucus',
    'Intentional drop', 'Hook filtering ✓', 'Bad drop', 'Basically flat ✓',
    'Every line connects', 'QUICK TIP', 'INTERACTIVE EXERCISES',
    'Stay to the end', 'Why herbs') stacked on a static retention chart
    (100% -> 34% over 1:01), ~10 s apart. Narrative chain = compact 2x2 grid
    of labeled pills with directional arrows (Spleen -> Fluids, Phlegm <- Dampness).
    """
    inst = f"D25@{t0:.2f}"
    events = []
    for i, label in enumerate(labels):
        lt0 = t0 + i * 10.0
        events.append(_base(
            "D25", f"autopsy label: {label}", lt0, lt0 + 10.0, TRACKS["chip"],
            _geom(120, 380 + (i % 4) * 90, 840, 80),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"label": WHITE, "check": TEAL},
            text=label,
            motion={"in": {"type": "pop", "dur_s": 0.3, "easing": "back.out_1.141"},
                    "out": _hard_cut_out()},
            sfx="pop-small-in.wav",
            notes="Labels stack ~10 s apart on the static retention chart; "
                  "check = teal (Sky green remapped)."))
    return events


# ------------------------------------------------------- D26-D37 (Batch 18, Dcc84V5jc6D)
# Origin reel, Aug 25 2026 — predates the 15 priority reels, so these are
# Dcc-era devices. Every parameter traces to a measurement in
# EDIT-TEARDOWN.md §3/§7 (batch-18 folder, examples/batch-18-sky-origin/).
# Brand mapping applied at the call site: Sky yellow #F5F536 -> PWC gold
# #FEE238; Sky green -> teal #14A886; ground -> navy #00214E. The reel is
# ONE locked-off take (zero cuts/zoom over 54.2 s) with DRY VOICE ONLY
# (no bed, no SFX) — the PWC engine's 1.45x hook zoom-out, slow push and
# punch-ins are measured NOWHERE in this reel; they are not Sky and are
# excluded from premium plans (v6 telltale). Q-lane divergences (cleared bed ~-28 dB + SFX on every landing;
# Q end beat vs Sky's bare close) are labelled divergences, not Sky.
# The spoken template <-> written caption is ONE device with two
# synchronized layers (T-03/T-16 bookend, D32 + D36) — never built as two
# unrelated devices. [EST] sub-parameters are flagged in place with what
# would close them; they are never silently hard-coded as measurements.
BATCH18_REEL = "Dcc84V5jc6D"
# Dcc-era face box (EDIT-TEARDOWN.md §1/§6): hair top y420-560, chin y850-900.
# The DfX2 default face box (y720-1170) does NOT apply to this reel — pass
# the take's own face box, or this one for Dcc-era framing.
DCC_FACE_BOX = {"x": 345, "y": 420, "w": 390, "h": 480}
LINEAR_COUNTUP_RATE_S = 270  # D31: constant +9/frame @30 fps, LINEAR


def _check_face_clear(geometry, face_box, device):
    """Fail loudly if a device's geometry overlaps the take's face box."""
    fx0, fy0 = face_box["x"], face_box["y"]
    fx1, fy1 = fx0 + face_box["w"], fy0 + face_box["h"]
    gx0, gy0 = geometry["x"], geometry["y"]
    gx1, gy1 = gx0 + geometry["w"], gy0 + geometry["h"]
    if gx0 < fx1 and gx1 > fx0 and gy0 < fy1 and gy1 > fy0:
        raise ValueError(
            f"{device}: geometry {geometry} overlaps face box {face_box} — "
            "nothing ever covers the face")


def d26_dashed_loop_arrow(t0, *, family="green", t1=None, headline_t0=None):
    """D26 dashed loop arrow. VERIFIED (T-05, Dcc84V5jc6D).

    Hand-drawn-style DASHED curved arrow (white in Sky; gold/teal in Q's
    lane) starting top-left, curving down the left edge, looping a full
    loop-de-loop, then running down to the template document's beat-4 row.
    The LOOP is mandatory — a plain curved arrow FAILS the grade. No
    arrowhead (none seen at full res, GAP-G8) — never invent one.
    Lands WITH the solution headline, on the spoken solution word; draws
    along the path AFTER the headline lands; exits by hard cut with it.
    """
    if headline_t0 is not None and t0 < headline_t0 - 1e-9:
        raise ValueError(
            f"D26: arrow t0 {t0} precedes headline t0 {headline_t0} — the "
            "arrow draws AFTER the headline lands (v3 connector law)")
    accent = _accent(family)
    path = [(200, 360), (170, 600), (200, 900), (250, 900), (150, 900),
            (200, 900), (230, 1150), (250, 1450)]
    return [_base(
        "D26", "dashed loop arrow", t0, t1 if t1 is not None else t0 + 3.2,
        TRACKS["hero"],
        _geom(150, 360, 100, 1090),
        status="VERIFIED", source_reel=BATCH18_REEL,
        colors={"line": accent},
        text="dashed loop arrow",
        items=[{"path": path, "loop_centre": (200, 900), "loop_diameter_px": 100,
                "dash_px": 28, "gap_px": 18, "dash_status": "[EST-dash]",
                "stroke_px": 4, "arrowhead": False}],
        motion={"in": {"type": "line_draw", "dur_s": 0.5, "easing": "linear",
                       "notes": "[EST] draw ~0.5 s — v3 connector law "
                                "(connectors draw after nodes, 0.4-2.4 s); "
                                "close by measuring the headline-template-arrow clip",
                       "dash_status": "[EST-dash] dash ~28 px / gap ~18 px "
                                      "estimated from the 1 fps frame — measure "
                                      "from the clip to close"},
                "out": _hard_cut_out()},
        notes="D26 (T-05): dashed + curved + LOOPED — D16 is a thin solid "
              "orange L-line; this is materially different. Loop mandatory. "
              "No arrowhead (GAP-G8). Lands with the solution headline.")]


def d27_donut_split(t0, *, headline_number, states, family="green",
                    t1=None, sweep_s=None):
    """D27 donut split chart. VERIFIED (T-08/T-09, Dcc84V5jc6D).

    Real IG insights split: headline number + "Views", donut ring with a
    followers / non-followers split, "Accounts reached" row + delta %.
    Hard pop-in in 1 frame ON the spoken figure (+3,988 bright px in 1 f
    at 10.87 s). The split VALUES update across states while the headline
    numbers stay constant — one post's donut with an animated split, never
    three different posts, never invented numbers.

    states: [{"t": float, "followers_pct": float, "nonfollowers_pct": float}]
    — each state's percentages must sum to ~100. Default motion between
    states is STEPPED at the listed times (smooth-vs-stepped UNRESOLVED,
    GAP-G11); pass sweep_s (seconds per state transition) once the
    donut-value-update clip is measured frame-by-frame.
    """
    if not states:
        raise ValueError("D27 needs at least one split state")
    for s in states:
        total = s["followers_pct"] + s["nonfollowers_pct"]
        if abs(total - 100.0) > 2.0:
            raise ValueError(
                f"D27 state at {s['t']}: split {s['followers_pct']}/"
                f"{s['nonfollowers_pct']} sums to {total}, not ~100 — "
                "never invent donut numbers")
    inst = f"D27@{t0:.2f}"
    end = t1 if t1 is not None else states[-1]["t"] + 3.0
    events = []
    for i, s in enumerate(states):
        st0 = s["t"] if i > 0 else t0
        st1 = states[i + 1]["t"] if i + 1 < len(states) else end
        events.append(_base(
            "D27", f"donut split {s['followers_pct']:.2f}/{s['nonfollowers_pct']:.2f}",
            st0, st1, TRACKS["hero"],
            _geom(180, 170, 720, 370),
            status="VERIFIED", source_reel=BATCH18_REEL, instance=inst,
            colors={"headline": WHITE, "followers_arc": TEAL,
                    "nonfollowers_arc": GOLD, "delta": TEAL,
                    "label": WHITE},
            text=str(headline_number),
            items=[{"headline_number": headline_number,
                    "followers_pct": s["followers_pct"],
                    "nonfollowers_pct": s["nonfollowers_pct"],
                    "ring_diameter_px": 130, "ring_stroke_px": 18,
                    "ring_centre": (540, 385),
                    "sweep_s": sweep_s,
                    "sweep_status": ("stepped (measured default — GAP-G11)"
                                     if sweep_s is None else "swept")}],
            motion={"in": ({"type": "hard_cut", "dur_s": 0.033, "easing": "step",
                            "notes": "hard pop 1 f on the spoken figure"}
                           if i == 0 else {"type": "hold"}),
                    "ring_sweep": {"dur_s": 0.5, "status": "[EST]",
                                   "notes": "[EST] secondary ~0.5 s brightening "
                                            "after the pop (ring draw/scale — "
                                            "GAP-G10); close with a hand-masked "
                                            "donut-in strip"},
                    "out": _hard_cut_out()},
            sound=_tick_sound("counter / split-value landing"),
            notes="D27 (T-08/T-09): hard pop 1 f on the spoken figure; headline "
                  "numbers NEVER change across states; ring fill animates with "
                  "the split. Q lane: ring teal/gold when rebuilt, IG-native "
                  "colours only on an untouched screenshot. Top zone y170-540 "
                  "(TOP_ZONE_MEASURED)."))
    return events


def d28_phone_section_tracker(t0, *, sections, clip_path, family="green",
                              t1=None, face_box=None):
    """D28 phone section tracker. VERIFIED (T-07, Dcc84V5jc6D).

    Vertical phone frame (gold border 2 px, rounded corners ~24 px) playing
    a REAL clip inside (never a still), with a big semi-transparent section
    label centre (HOOK -> LEAD -> BODY1 -> OPEN LOOPS) changing in sync with
    the spoken structure, a mini bar chart at top and progress tabs at the
    bottom (active tab underlined). The embedded clip plays SILENTLY under
    the voiceover. Phone sits centre-low, face-clear.

    sections: [(label, t0), ...] in spoken order. clip_path: the real reel
    playing inside the phone. face_box: the take's face box — the phone must
    clear it (Dcc-era default DCC_FACE_BOX; the DfX2 default does not apply).
    """
    if not sections:
        raise ValueError("D28 needs at least one section label")
    if not clip_path:
        raise ValueError("D28 needs a REAL clip playing inside the phone — never a still")
    fb = face_box or DCC_FACE_BOX
    phone_geom = _geom(360, 1030, 360, 660)
    _check_face_clear(phone_geom, fb, "D28")
    inst = f"D28@{t0:.2f}"
    end = t1 if t1 is not None else sections[-1][1] + 3.0
    events = [_base(
        "D28", "phone mockup", t0, end, TRACKS["asset"],
        phone_geom,
        status="VERIFIED", source_reel=BATCH18_REEL, instance=inst,
        colors={"frame": GOLD, "frame_border_px": 2, "label": WHITE},
        text="phone mockup",
        items=[{"clip": clip_path, "clip_plays": True, "clip_audio": "silent",
                "mini_chart": "top-of-phone bars (embedded clip's own UI = footage)",
                "progress_tabs": ["Hook", "Lead"], "corner_radius_px": 24}],
        motion={"in": {"type": "pop", "dur_s": POP_S, "easing": "back.out_1.141",
                       "notes": "[EST] pop 9 f back.out_1.141 as the measured-pop "
                                "default — exact entrance frames UNRESOLVED "
                                "(GAP-G9); close by measuring the phone-in strip"},
                "out": _hard_cut_out()},
        notes="D28 (T-07): real clip inside, never a still; section label "
              "changes with the spoken structure; phone never covers the face.")]
    for i, (label, lt0) in enumerate(sections):
        lt1 = sections[i + 1][1] if i + 1 < len(sections) else end
        events.append(_base(
            "D28", f"phone section: {label}", lt0, lt1, TRACKS["asset"],
            _geom(390, 1250, 300, 90),
            status="VERIFIED", source_reel=BATCH18_REEL, instance=inst,
            colors={"label": WHITE, "label_opacity": 0.50},
            text=label,
            items=[{"section": label, "index": i + 1, "total": len(sections),
                    "font_px": 60, "opacity": 0.50}],
            motion={"in": {"type": "hard_cut", "notes": "label swaps on the spoken structure"},
                    "out": _hard_cut_out()},
            notes=f"D28 section {i + 1}/{len(sections)}: lands on the spoken section."))
    return events


def d29_dot_columns(t0, *, t1, family="green", left_n=12, right_n=14, seed=0):
    """D29 flanking dot columns. VERIFIED (T-10, Dcc84V5jc6D).

    Two columns of dots flanking the phone (T-07/D28): LEFT ~12 HOLLOW
    circles (outline only), RIGHT ~14 FILLED dots, both ~28 px, y1100-1620,
    in loose outward-curving arcs — NOT a grid. No labels, no flip, no
    count — a static particle field. Enters and exits WITH the phone.
    Q lane: hollow TEAL left, filled GOLD right.
    """
    import math
    import random
    rng = random.Random(seed)
    dots = []
    for side, n, x0, x1, filled in (("left", left_n, 220, 360, False),
                                    ("right", right_n, 720, 870, True)):
        for i in range(n):
            y = 1100 + (520 * i / max(1, n - 1))
            # Loose outward arc: mid-column dots bulge away from centre.
            bulge = 18 * math.sin(3.14159 * i / max(1, n - 1))
            x = (x0 + x1) / 2 + rng.uniform(-15, 15) + (-bulge if side == "left" else bulge)
            dots.append({"side": side, "x": round(x), "y": round(y),
                         "diameter_px": 28, "filled": filled})
    left = [d for d in dots if d["side"] == "left"]
    right = [d for d in dots if d["side"] == "right"]
    return [_base(
        "D29", "flanking dot columns", t0, t1, TRACKS["hero"],
        _geom(220, 1100, 650, 520),
        status="VERIFIED", source_reel=BATCH18_REEL,
        colors={"left_outline": TEAL, "left_outline_px": 2,
                "right_fill": GOLD},
        text="dot columns",
        items=[{"dots": dots, "left_n": len(left), "right_n": len(right),
                "left_hollow": all(not d["filled"] for d in left),
                "right_filled": all(d["filled"] for d in right)}],
        motion={"in": {"type": "pop", "dur_s": frames_to_s(5),
                       "easing": "back.out_1.141",
                       "notes": "[EST] pop 5 f default — entrance frames "
                                "UNRESOLVED (GAP-G12); close with the "
                                "10.7-11.2 s 30 fps strip"},
                "out": _hard_cut_out()},
        notes="D29 (T-10): hollow left / filled right, loose arcs not a grid, "
              "enter + exit WITH the phone (D28). D17 family (dot-grid) but a "
              "distinct device: no flip, no labels, flanking columns.")]


def d30_proof_columns(t0, *, left, right, family="green", t1=None):
    """D30 dual proof-caption columns. VERIFIED (T-13, Dcc84V5jc6D).

    B6's proof: TWO profile photos top (with @handles + checkmarks below)
    and beneath each a full COLUMN of that creator's REAL caption text.
    The columns sit BEHIND the speaker (his head/shoulders overlap their
    inner edges — text is a background layer, speaker in front). Real
    screenshots, handles visible, no blur. Lands on the proof sentence.

    left/right: {"handle": str, "caption": str, "ring": bool} — the caption
    is the creator's REAL words, never rewritten. Q lane: Q's NAMED proof
    sources (never unnamed "two business owners"); blur law applied to
    other people's payouts; Q/Kiya proofs as-is.
    """
    for side, prof in (("left", left), ("right", right)):
        if not prof.get("handle") or not prof.get("caption"):
            raise ValueError(f"D30 {side} proof needs a handle AND real caption text")
        if "lorem" in prof["caption"].lower():
            raise ValueError("D30 captions are REAL text — never lorem/placeholder")
    inst = f"D30@{t0:.2f}"
    end = t1 if t1 is not None else t0 + 4.6
    return [_base(
        "D30", "proof profile heads", t0, end, TRACKS["asset"],
        _geom(200, 170, 680, 180),
        status="VERIFIED", source_reel=BATCH18_REEL, instance=inst,
        colors={"handle": GREY_DIM, "handle_text": WHITE},
        text=f"@{left['handle']} / @{right['handle']}",
        items=[{"side": "left", "handle": left["handle"], "ring": left.get("ring", False),
                "head_diameter_px": 190, "x": (200, 390), "y": (170, 350)},
               {"side": "right", "handle": right["handle"], "ring": right.get("ring", False),
                "head_diameter_px": 190, "x": (690, 880), "y": (170, 350)}],
        motion={"in": {"type": "pop", "dur_s": POP_S, "easing": "back.out_1.141",
                       "notes": "[EST] pop 9 f default — entrance frames "
                                "UNRESOLVED (GAP-G13); close with the profilepop strip"},
                "out": _hard_cut_out()},
        notes="D30 heads (T-13): two REAL profile photos + handles, top zone "
              "y170-350 (TOP_ZONE_MEASURED)."),
        _base(
        "D30", "proof caption columns", t0, end, TRACKS["asset"],
        _geom(60, 380, 970, 670),
        status="VERIFIED", source_reel=BATCH18_REEL, instance=inst,
        colors={"text": WHITE},
        text="proof captions",
        items=[{"side": "left", "handle": left["handle"],
                "caption": left["caption"], "x": (60, 520)},
               {"side": "right", "handle": right["handle"],
                "caption": right["caption"], "x": (560, 1030)},
               {"layer": "behind_speaker",
                "notes": "columns render BEHIND the speaker — speaker pixels "
                         "over column pixels in the overlap zone"}],
        motion={"in": {"type": "pop", "dur_s": POP_S, "easing": "back.out_1.141"},
                "out": _hard_cut_out()},
        notes="D30 columns (T-13): two REAL caption columns, ~20 px white, "
              "behind the speaker, face-clear. Lands on the proof sentence.")]


def d31_linear_countup(t0, *, label, family="green", rate_s=LINEAR_COUNTUP_RATE_S,
                       duration_s=1.81):
    """D31 linear count-up, NO landing value. VERIFIED (T-06, Dcc84V5jc6D).

    Person-icon circle + WHITE bold number with "+" suffix + accent label
    below ("more leads" — Q's outcome words). The number counts UP LINEARLY
    from 0 at ~270/s (constant +9/frame @30 fps — an eased count-up FAILS)
    and exits fading over ~10 frames WHILE STILL COUNTING: there is NO
    landing value, so this function takes NO final_value parameter — any
    "final" number in a Q build is a fake. The 10-frame fade is one of only
    TWO measured fades in Option 1 (the other is D2's 5-frame hook exit);
    it is a measured exception, not a general fade permission.
    Q lane: teal icon, GOLD number, white label (gold = payoff figure).
    """
    accent = _accent(family)
    n_frames = int(round(duration_s * 30))
    samples = [{"t": round(t0 + i / 30.0, 3),
                "value": int(round(rate_s * i / 30.0))}
               for i in range(0, n_frames + 1, 3)]  # every 3rd frame
    return [_base(
        "D31", "linear count-up", t0, t0 + duration_s, TRACKS["chip"],
        _geom(430, 1050, 370, 130),
        status="VERIFIED", source_reel=BATCH18_REEL,
        colors={"icon": TEAL, "number": GOLD, "label": WHITE, "accent": accent},
        text=label,
        items=[{"icon": "person silhouette, dark on accent circle, ~70 px",
                "number_px": 70, "label_px": 45,
                "rate_s": rate_s, "rate_per_frame": round(rate_s / 30.0, 2),
                "easing": "linear", "start_value": 0,
                "samples": samples,
                "landing_value": None,
                "notes": "NO landing value by design — exits fading while "
                         "still counting"}],
        motion={"in": {"type": "hard_cut", "notes": "starts at 0 on the promise word"},
                "count": {"type": "count_up", "dur_s": duration_s, "easing": "linear",
                          "notes": "LINEAR ~270/s, constant +9/frame — an eased "
                                   "count-up FAILS (EDIT-TEARDOWN.md L3)"},
                "out": {"type": "fade", "dur_s": frames_to_s(10),
                        "notes": "MEASURED 10-frame fade (8.40-8.73 s, brightness "
                                 "19,316->3,461) WHILE STILL COUNTING — one of "
                                 "only two measured fades in Option 1"}},
        sound=_tick_sound("count-up"),
        notes="D31 (T-06): linear ~270/s, starts at 0, no landing value, "
              "fades out still counting. Count-ups are a tick-tone beat class "
              "(Batch 36 B2 — timers/count-ups carry the 5,926 Hz train in "
              "DfPxq/DfDu/Dez4; D31's own reel is dry, the family spec is "
              "attached, not an instance claim). Deviates from the PWC engine's "
              "expo count-up (1 s) — the engine spec is not Sky (v6 telltale).")]


def d32_document_sweep(t0, *, document_text, beats, family="green",
                       state="sharp", highlight_color=None, t1=None):
    """D32 template/caption document + highlight sweep + top reader.
    VERIFIED (T-03/T-05/T-12/T-16, Dcc84V5jc6D).

    THREE synchronized layers: (a) the full document — REAL text, verbatim,
    small white (~20-24 px), left-aligned, centre-low; (b) a HIGHLIGHT BAR
    — a translucent rounded rect behind the CURRENT beat's row, sweeping
    down the list beat by beat, one device per pause; (c) a TOP READER —
    the current beat's full text shown LARGE at the top while its row is
    highlighted. All three change together on the spoken item word.
    The document is ONE object in two states: dim (opacity ~35%, slight
    blur — the T-03 backdrop) and sharp (opacity 100% — T-12/T-16). The
    same object returns sharp at the close (see D36) — the pair IS the
    device (spoken template <-> written caption, one device, two layers).

    document_text: the REAL text, verbatim — never a retyped paraphrase.
    beats: [{"label": str, "text": str, "t0": float}] — highlight/reader
    times, one per spoken item. highlight_color: gold at 40% opacity in
    Q's lane; the Sky olive/khaki bar's exact hex is UNVERIFIED (GAP-G3),
    so this ships flagged [EST-colour].
    state: "dim" (slow dim fade in, no pop) or "sharp" (hard cut [EST],
    GAP-G17 — the sharp-state arrival motion is unresolved).
    """
    if not document_text or not document_text.strip():
        raise ValueError("D32 needs the REAL document text, verbatim — never empty")
    if not beats:
        raise ValueError("D32 needs at least one sweep beat")
    if state not in ("dim", "sharp"):
        raise ValueError(f"D32 state must be 'dim' or 'sharp', got {state!r}")
    hl = highlight_color or GOLD
    validate_color(hl, where="D32 highlight")
    inst = f"D32@{t0:.2f}"
    end = t1 if t1 is not None else beats[-1]["t0"] + 3.0
    events = [_base(
        "D32", "template/caption document", t0, end, TRACKS["asset"],
        _geom(270, 950, 560, 850),
        status="VERIFIED", source_reel=BATCH18_REEL, instance=inst,
        colors={"text": WHITE, "highlight": hl, "highlight_opacity": 0.40},
        text=document_text,
        items=[{"state": state,
                "opacity": 0.35 if state == "dim" else 1.0,
                "blur": "slight" if state == "dim" else None,
                "font_px": 22, "highlight_height_px": 110,
                "highlight_status": "[EST-colour] Sky bar hex UNVERIFIED "
                                    "(GAP-G3) — gold at 40% opacity in Q's lane",
                "reader_geometry": {"x": 110, "y": 140, "w": 860, "h": 210},
                "reader_font_px": 37}],
        motion={"in": ({"type": "fade", "dur_s": 1.0,
                        "notes": "slow dim fade, no pop (T-03)"}
                       if state == "dim" else
                       {"type": "hard_cut",
                        "notes": "[EST] sharp-state arrival is hard cut — "
                                 "exact motion UNRESOLVED (GAP-G17)"}),
                "out": _hard_cut_out()},
        notes="D32 (T-03/T-05/T-12): the document IS the product — template, "
              "prompt, or caption shown as a real document. Dim state is dim "
              "(mean luminance <50% of sharp).")]
    for i, beat in enumerate(beats):
        bt1 = beats[i + 1]["t0"] if i + 1 < len(beats) else end
        events.append(_base(
            "D32", f"document beat {i + 1}: {beat['label']}", beat["t0"], bt1,
            TRACKS["asset"],
            _geom(180, 950 + i * 110, 720, 110),
            status="VERIFIED", source_reel=BATCH18_REEL, instance=inst,
            colors={"highlight": hl, "highlight_opacity": 0.40,
                    "reader_text": WHITE, "reader_keyword": GOLD},
            text=beat["text"],
            items=[{"beat_index": i + 1, "label": beat["label"],
                    "reader_text": beat["text"],
                    "notes": "highlight bar on this row ONLY; reader shows "
                             "this beat large at top; caption names the beat "
                             "with the gold keyword in the same frame"}],
            motion={"in": {"type": "hard_cut",
                           "notes": "highlight + reader change together ON the "
                                    "spoken item word (±0.1 s), one device per pause"},
                    "out": _hard_cut_out()},
            notes=f"D32 sweep beat {i + 1}/{len(beats)} — the sweep runs "
                  "~1.3 s/beat and follows the SPEECH, never a canonical order "
                  "(spoken 5 / doc 7 / prompt-chain 7 all differ — T-12)."))
    return events


def d33_comment_examples(t0, *, left_shot, right_shot, family="green", t1=None):
    """D33 comment-screenshot example pair. VERIFIED (T-04, Dcc84V5jc6D).

    Two REAL IG screenshots floating top zone — the visual for a deictic
    "like this and this": the bad examples, shown not named. Small white
    text (~28-32 px) with blue @handles (IG-native link blue = footage)
    and grey timestamps. Real UI, not rebuilt graphics. Lands on the
    deictic phrase, exits before the solution headline.
    Q lane: two REAL bad examples from Q's niche, handles visible, never
    invented examples, never blurred handles (public comments, shown as-is).

    left_shot/right_shot: {"text": str, "handle": str, "timestamp": str}.
    """
    for side, shot in (("left", left_shot), ("right", right_shot)):
        if not shot.get("text") or not shot.get("handle") or not shot.get("timestamp"):
            raise ValueError(
                f"D33 {side} screenshot needs text + handle + timestamp — "
                "real UI, never a redrawn fake")
    inst = f"D33@{t0:.2f}"
    end = t1 if t1 is not None else t0 + 1.7
    shots = [(left_shot, _geom(270, 230, 430, 200), "left/top"),
             (right_shot, _geom(640, 470, 330, 70), "right")]
    events = []
    for shot, geom, pos in shots:
        events.append(_base(
            "D33", f"comment example ({pos})", t0, end, TRACKS["asset"],
            geom,
            status="VERIFIED", source_reel=BATCH18_REEL, instance=inst,
            colors={"text": WHITE, "handle": "IG-native link blue (footage)",
                    "timestamp": GREY_DIM},
            text=shot["text"],
            items=[{"handle": shot["handle"], "timestamp": shot["timestamp"],
                    "font_px": 30, "real_screenshot": True}],
            motion={"in": {"type": "pop", "dur_s": POP_S, "easing": "back.out_1.141",
                           "notes": "[EST] pop 9 f default — entrance motion "
                                    "UNRESOLVED (GAP-G7); close with the 3.4-4.2 s strip"},
                    "out": _hard_cut_out()},
            notes="D33 (T-04): two REAL screenshots, handles + timestamps "
                  "visible, top zone face-clear (TOP_ZONE_MEASURED). Lands on "
                  "the deictic phrase; exits before the solution headline."))
    return events


def d34_thumb_wall(t0, *, thumbnails, family="green", t1=None):
    """D34 thumbnail wall slide. VERIFIED (T-11, Dcc84V5jc6D).

    SIX real thumbnails (3 top + 3 bottom around the speaker) that slide in
    with HEAVY horizontal motion blur, settle into a wall, shrink-float to
    the frame edges, then exit. Total life ~4 s. The motion-blur slide
    entrance is the signature — a clean pop FAILS.
    Q lane: six REAL Q thumbnails (or real trending creators', handles
    visible where the spoken content names a content type) — never stock,
    never AI.

    thumbnails: 6x {"src": str, "caption": str}.
    """
    if len(thumbnails) != 6:
        raise ValueError(f"D34 needs exactly 6 real thumbnails, got {len(thumbnails)}")
    for th in thumbnails:
        if not th.get("src"):
            raise ValueError("D34 thumbnails must be real footage (src required)")
    end = t1 if t1 is not None else t0 + 4.0
    return [_base(
        "D34", "thumbnail wall slide", t0, end, TRACKS["hero"],
        _geom(60, 150, 960, 1350),
        status="VERIFIED", source_reel=BATCH18_REEL,
        colors={"text": WHITE},
        text="thumbnail wall",
        items=[{"thumbnails": thumbnails,
                "layout": "3 top (y150-550) + 3 bottom (y1150-1500), x60-1020",
                "caption_px": 16}],
        motion={"in": {"type": "motion_blur_slide", "dur_s": 1.2, "easing": "linear",
                       "notes": "motion-blur slide-in ~1.2 s, visible horizontal "
                                "streaking — a clean pop FAILS (f_023 mid-slide)"},
                "mid": {"type": "shrink_float", "dur_s": 0.8,
                        "notes": "settled wall ~1.5 s, then shrink to floating "
                                 "positions at the frame edges before exit"},
                "out": _hard_cut_out()},
        notes="D34 (T-11): six REAL thumbnails, blur-slide entrance, settled "
              "3+3 wall face-clear, shrink-float before exit, total life ~4 s. "
              "Top row y150-550 (TOP_ZONE_MEASURED).")]


def d35_prompt_ui(t0, *, prompt_text, formula_chain, family="green",
                  model_label="Sonnet 5 Medium", t1=None):
    """D35 AI-prompt doc + chat UI. VERIFIED (T-15, Dcc84V5jc6D).

    The offer as (a) the PROMPT TEXT ITSELF as a small dim document
    (background layer — the speaker's hand passes in front of it), (b) a
    chat UI bottom bar with the formula chain + model label + mic/audio
    icons + "+" button, (c) the REAL cursor from the screen recording
    (never a drawn arrow). The formula chain is passed as DATA and shown
    verbatim — the prompt chain's ordering differs from the spoken 5 and
    the doc 7; do NOT canonicalise it.
    Q lane: Q's OWN prompt/template + Q's tool UI; CTA routes to Q's
    waitlist/Stan, never Sky's prompt.

    prompt_text: the REAL prompt, verbatim. formula_chain: the chain string
    as shown in the UI (e.g. "Intro -> Before/Story -> ... -> CTA").
    """
    if not prompt_text or not prompt_text.strip():
        raise ValueError("D35 needs the REAL prompt text, verbatim — never empty")
    if not formula_chain:
        raise ValueError("D35 needs the formula chain as shown in the UI")
    inst = f"D35@{t0:.2f}"
    end = t1 if t1 is not None else t0 + 7.5
    return [_base(
        "D35", "AI-prompt document", t0, end, TRACKS["asset"],
        _geom(180, 970, 770, 280),
        status="VERIFIED", source_reel=BATCH18_REEL, instance=inst,
        colors={"text": WHITE},
        text=prompt_text,
        items=[{"font_px": 24, "state": "dim/blurred background layer",
                "notes": "speaker's hand passes in front of it"}],
        motion={"in": {"type": "hard_cut", "notes": "enters on 'I actually built a prompt'"},
                "out": _hard_cut_out()},
        notes="D35 prompt doc (T-15): REAL prompt text verbatim, dim document."),
        _base(
        "D35", "chat UI bar", t0, end, TRACKS["asset"],
        _geom(130, 1120, 820, 150),
        status="VERIFIED", source_reel=BATCH18_REEL, instance=inst,
        colors={"bar": NAVY, "text": WHITE},
        text=formula_chain,
        items=[{"formula_chain": formula_chain, "model_label": model_label,
                "cursor": {"from_recording": True, "x": 830, "y": 1300,
                           "notes": "REAL cursor from the screen recording — "
                                    "never a drawn arrow"},
                "icons": ["mic", "audio", "+"]}],
        motion={"in": {"type": "hard_cut"}, "out": _hard_cut_out()},
        notes="D35 chat bar (T-15): formula chain + model label + live cursor; "
              "bar persists while the doc is up. Q lane: Q's tool/model label.")]


def d36_live_example_bookend(t0, *, document_text, keyword, family="green",
                             t1=None, source_document=None):
    """D36 live-example bookend. VERIFIED (T-16, Dcc84V5jc6D).

    The SAME document object as T-03 (D32, dim state) returns SHARP and
    LARGE, top-left, cropped at the right edge (lines run off mid-word —
    do NOT reflow), landing on "live example" — the spoken CTA points at
    the written caption and the edit SHOWS the caption. Keyword pill
    bottom-centre underneath; the chat UI bar persists below.
    This is the two-layer interlock made visible (spoken template <->
    written caption = ONE device, two synchronized layers). Without it,
    "just read the caption down below" would be an unillustrated claim.
    Q lane: Q's REAL caption + Q's keyword pill (WAITLIST) + Q's live flow.

    document_text must be IDENTICAL to the dim instance's text — pass the
    D32 document text as source_document and this function enforces it.
    """
    if not document_text or not document_text.strip():
        raise ValueError("D36 needs the REAL published caption, verbatim — never empty")
    if source_document is not None and document_text != source_document:
        raise ValueError(
            "D36 document must be IDENTICAL to the dim instance (D32/T-03) — "
            "same object, two states, not a retyped copy")
    if not keyword:
        raise ValueError("D36 needs the live keyword for the pill")
    inst = f"D36@{t0:.2f}"
    end = t1 if t1 is not None else t0 + 2.2
    return [_base(
        "D36", "live-example document (sharp)", t0, end, TRACKS["asset"],
        _geom(110, 140, 450, 810),
        status="VERIFIED", source_reel=BATCH18_REEL, instance=inst,
        colors={"text": WHITE},
        text=document_text,
        items=[{"cropped": True, "reflow": False,
                "notes": "cropped at the right edge, lines run off mid-word — "
                         "do NOT reflow to fit",
                "same_document_as_dim": True}],
        motion={"in": {"type": "hard_cut",
                       "notes": "enters ~49.8 s (±0.3 s, GAP-G15), lands on "
                                "'live example' (50.52 s)"},
                "out": _hard_cut_out()},
        notes="D36 (T-16): the REAL published caption, verbatim, sharp, "
              "top-left (TOP_ZONE_MEASURED). Hard cut to the bare close at t1."),
        _base(
        "D36", "keyword pill", t0, end, TRACKS["chip"],
        _geom(500, 1400, 150, 70),
        status="VERIFIED", source_reel=BATCH18_REEL, instance=inst,
        colors={"pill": NAVY, "keyword": GOLD, "arrow": TEAL},
        text=keyword,
        items=[{"pill": "dark pill + keyword text + up-arrow circle",
                "notes": "Q lane: navy pill + gold keyword + teal arrow"}],
        motion={"in": {"type": "pop", "dur_s": POP_S, "easing": "back.out_1.141"},
                "out": _hard_cut_out()},
        notes="D36 keyword pill (T-16): bottom-centre, visible t=50-51 s in Sky's reel.")]


def d37_figure_pair(t0, *, figures, caption, family="green"):
    """D37 staggered figure pair. VERIFIED (T-14, Dcc84V5jc6D).

    Two HUGE figures (~90-100 px), bottom-left/right: the LEFT figure lands
    on the FIRST spoken number (hard pop, 1 f), the RIGHT figure on the
    SECOND (pop + glow decay — brightness spike then settle). One figure
    per spoken number, never both at once. Q lane: GOLD figures, Q's real
    numbers only.

    figures: [(text, t0, x, y), (text, t0, x, y)] — left first in time.
    caption: the small centred caption below (e.g. "figures a month").
    """
    if len(figures) != 2:
        raise ValueError(f"D37 needs exactly 2 figures, got {len(figures)}")
    if not figures[0][1] < figures[1][1]:
        raise ValueError("D37: left figure must land BEFORE the right figure "
                         "(one figure per spoken number, in spoken order)")
    inst = f"D37@{t0:.2f}"
    events = []
    for i, (text, ft0, fx, fy) in enumerate(figures):
        motion = {"in": {"type": "hard_cut", "dur_s": 0.033, "easing": "step",
                         "notes": "hard pop-in, 1 frame"},
                  "out": _hard_cut_out()}
        if i == 1:
            motion["glow_decay"] = {"type": "glow_decay", "dur_s": 0.5}
        events.append(_base(
            "D37", f"figure: {text}", ft0, ft0 + 1.8, TRACKS["chip"],
            _geom(fx, fy, 330 if i == 1 else 270, 90),
            status="VERIFIED", source_reel=BATCH18_REEL, instance=inst,
            colors={"figure": GOLD},
            text=text,
            items=[{"figure": text, "font_px": 95, "side": "left" if i == 0 else "right",
                    "glow_decay": i == 1,
                    "notes": ("hard pop 1 f on the first spoken number"
                              if i == 0 else
                              "pop + glow decay (brightness spike then settle) "
                              "on the second spoken number")}],
            motion=motion, sound=_tick_sound("figure / count-up landing"),
            notes="D37 (T-14): one figure per spoken number, left then right. "
                  "Figure landings are a tick-tone beat class (Batch 36 B2: "
                  "Dez4fPJCR74 payment count-up pills 57.82-58.57 s carry the "
                  "loudest measured train)."))
    events.append(_base(
        "D37", "figure caption", figures[1][1] + 0.5, figures[1][1] + 1.3,
        TRACKS["chip"],
        _geom(390, 1150, 300, 50),
        status="VERIFIED", source_reel=BATCH18_REEL, instance=inst,
        colors={"text": WHITE},
        text=caption,
        motion={"in": {"type": "hard_cut"}, "out": _hard_cut_out()},
        notes="D37 caption below the figures (white, small, centred)."))
    return events


# ------------------------------------------------------- D38-D54 (Batch 19)
# 33 NEW Sky reels #17-49 (batch-19-sky-full-profile). Provisional D38-D44
# numbers from the three decode workers COLLIDED — see
# code/DEVICE-RECONCILIATION-B19.md. Final numbers D38-D54, sequential.
# Batch 18 already holds D26-D37; no collision.
def d38_pov_desk_hook_doc(t0, *, headline, items, doc_url="app.notion.com",
                          t1=None, camera_moves=None, source_reel="DevpJZLk6Km"):
    """D38 POV-desk hook-doc. VERIFIED (#17/#18/#21).

    The whole reel is ONE system: over-the-shoulder POV of Sky's desk — hands
    + keyboard in the foreground, a monitor filling the frame showing a live
    Notion doc (``app.notion.com``, "Private"/"Share" UI). The doc IS the
    canvas: its headline is the hook, its numbered list is the video's
    outline, and list items TYPE IN LIVE as the beats land (~1-2 s per item,
    word by word; mid-type placeholder reads "List"). Camera: slow push-in
    (~0-8 s; deeper in #21 — the monitor fills the frame and the headline
    crops), an optional profile swing (~28 s, #17/#18) or wide pull-back
    (~72 s, #18). D1 captions in this form are 1 WORD per group (~0.27 s)
    with the band higher (centre y~1090-1150, above the photo/exhibit zone).
    No talking-head framing until the face-cam close. Doc bg #06161C
    (near-black teal, Sky ground family). A D32 highlight sweep can land
    inside the doc (#21 @~38 s, "spots a high performer").

    headline: the doc headline (= the hook). items: [{"text": str, "t": float}]
    in spoken order — item 1 is usually pre-typed at t0. camera_moves:
    [{"kind": "push_in"|"profile_swing"|"pull_back", "t": float}].
    Q lane: Q's own desk + Q's own live doc (never Sky's doc text); the doc
    is a real screen recording, never a redrawn fake.
    """
    if not headline or not headline.strip():
        raise ValueError("D38 needs a doc headline (= the hook)")
    if not items:
        raise ValueError("D38 needs at least one numbered list item")
    for it in items:
        if not it.get("text") or not it["text"].strip():
            raise ValueError("D38 list items need text")
        if it["t"] < t0 - 1e-9:
            raise ValueError(f"D38 list item {it['text']!r} at {it['t']} precedes t0 {t0}")
    inst = f"D38@{t0:.2f}"
    end = t1 if t1 is not None else items[-1]["t"] + 3.0
    events = [_base(
        "D38", "POV desk shot", t0, end, TRACKS["aroll"],
        _geom(0, 0, 1080, 1920),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"doc_bg": "#06161C"},
        text="POV desk + live doc",
        items=[{"doc_url": doc_url, "camera_moves": camera_moves or [],
                "notes": "over-the-shoulder POV; slow push-in; hands + keyboard "
                         "in the foreground; monitor fills the frame"}],
        motion={"in": {"type": "hard_cut"}, "out": _hard_cut_out(),
                "camera": {"type": "slow_push_in", "dur_s": 8.0,
                           "notes": "monitor grows in frame ~0-8 s; deeper in "
                                    "#21 (headline crops); profile swing ~28 s "
                                    "and wide pull-back ~72 s are per-reel variants"}},
        notes="D38 (#17/#18/#21): the doc IS the canvas — headline = hook, "
              "numbered list = outline, items type in live. No talking head "
              "until the face-cam close.")]
    events.append(_base(
        "D38", "doc headline (hook)", t0, end, TRACKS["hero"],
        _geom(90, 150, 900, 220),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"headline": WHITE, "doc_bg": "#06161C"},
        text=headline,
        items=[{"font_px": 55, "align": "left",
                "notes": "white bold grotesque ~55 px on the dark doc; 'NOT' "
                         "on its own line in #17/#18/#21"}],
        motion={"in": {"type": "hard_cut"}, "out": _hard_cut_out()},
        notes="Doc headline visible from frame 0, holds the whole reel. "
              "Top zone (TOP_ZONE_MEASURED — the monitor IS the frame)."))
    for i, it in enumerate(items):
        it1 = items[i + 1]["t"] if i + 1 < len(items) else end
        events.append(_base(
            "D38", f"doc list item {i + 1}", it["t"], it1, TRACKS["hero"],
            _geom(90, 480 + i * 90, 900, 80),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"text": WHITE, "doc_bg": "#06161C"},
            text=it["text"],
            items=[{"index": i + 1, "mid_type_placeholder": "List",
                    "notes": "types in live word by word over ~1-2 s; mid-type "
                             "placeholder reads 'List'; the list types AHEAD of "
                             "the spoken beat it names; all versions stay visible"}],
            motion={"in": {"type": "type_in_live", "dur_s": 1.5,
                           "notes": "live typing, not a pop — one word at a time"},
                    "out": _hard_cut_out()},
            notes=f"List item {i + 1}/{len(items)}: types in live on its beat."))
    return events


def d39_subject_photo_insert(t0, *, photo_path, subject, duration_s=2.0,
                             size="half_body", label=None,
                             face_box=None, source_reel="DevpJZLk6Km"):
    """D39 subject photo insert. VERIFIED (#17/#18/#21).

    A rounded-rect photo of the SUBJECT pops in bottom-centre on the spoken
    name, holds ~2-3.5 s, hard-cut out. No label, no border, no handle — the
    photo alone identifies the subject. #17 Mel Robbins (blonde, glasses,
    black shirt, smiling) x195-885 y1130-1800, @~1.5-3.5 s on "Mel" (1.44 s);
    #18 Huberman B&W headshot @~2-4 s AND a return @~66-70 s with the label
    "Brain Science Protocols"; #21 Leila Hormozi B&W headshot @~0-3.5 s
    (smaller, headshot framing). Distinct from D23 (Sky's OWN head) and D10
    (a screen, not a clean photo). The photo is the SUBJECT's real photo —
    never stock/AI. face_box: the take's face box — the insert must clear it;
    default None (the POV-desk form has no talking-head face on screen, so
    no check applies there; pass a face box when building over a talking
    head).
    """
    if not photo_path:
        raise ValueError("D39 needs a REAL subject photo — never stock/AI")
    if not subject or not subject.strip():
        raise ValueError("D39 needs the subject's name")
    geom = {"half_body": _geom(195, 1130, 690, 670),
            "headshot": _geom(300, 1100, 480, 400)}[size] if size in (
                "half_body", "headshot") else None
    if geom is None:
        raise ValueError(f"D39 size must be 'half_body' or 'headshot', got {size!r}")
    if face_box is not None:
        _check_face_clear(geom, face_box, "D39")
    return [_base(
        "D39", f"subject photo: {subject}", t0, t0 + duration_s, TRACKS["chip"],
        geom,
        status="VERIFIED", source_reel=source_reel,
        colors={"text": WHITE},
        text=subject,
        items=[{"photo": photo_path, "subject": subject, "size": size,
                "label": label, "corners": "rounded-rect",
                "notes": "pops in bottom-centre ON the spoken name; no label/border/handle"}],
        motion={"in": {"type": "pop", "dur_s": POP_S, "easing": "back.out_1.141"},
                "out": _hard_cut_out()},
        sfx="pop-medium-in.wav",
        notes="D39 (#17/#18/#21): subject's real photo, ~2-3.5 s, hard-cut out. "
              "Distinct from D23 (Sky's own head) and D10 (screen).")]


def d40_pov_scene_label(t0, *, text, geometry="pill", t1=None,
                        source_reel="DeqNswuE2Fd"):
    """D40 POV scene label. VERIFIED (#19/#23/#25).

    ONE device, two geometries. Pill (top-left, #19): "POV: Giving feedback
    / to your strategists" — white text on a black pill, 2 lines, x15-330
    y85-175, present from frame 0, gone by ~9 s. Full-width bar (#23/#25):
    "POV: You're Autistic about Content" / "POV: You're ideating with your
    client" — white text on a black bar, FULL-WIDTH top strip y0-60, present
    the WHOLE reel; the label IS the title card (no other title). The label
    frames a POV meeting/scene — it names the situation the viewer is inside.
    Q lane: navy ground (Sky black -> PWC navy), white text.
    """
    if not text or not text.strip():
        raise ValueError("D40 needs label text")
    if geometry == "pill":
        geom = _geom(15, 85, 315, 90)
        end = t1 if t1 is not None else t0 + 9.0
    elif geometry == "bar":
        geom = _geom(0, 0, 1080, 60)
        end = t1 if t1 is not None else t0 + 60.0
    else:
        raise ValueError(f"D40 geometry must be 'pill' or 'bar', got {geometry!r}")
    return [_base(
        "D40", f"POV scene label ({geometry})", t0, end, TRACKS["chip"],
        geom,
        status="VERIFIED", source_reel=source_reel,
        colors={"text": WHITE, "ground": NAVY},
        text=text,
        items=[{"geometry": geometry,
                "notes": ("pill: top-left, 2 lines, exits ~9 s (#19)"
                          if geometry == "pill" else
                          "bar: full-width top strip, whole reel, IS the title card (#23/#25)")}],
        motion={"in": {"type": "hard_cut", "notes": "present from frame 0"},
                "out": _hard_cut_out()},
        notes="D40 (#19/#23/#25): one device, two geometries. Top zone "
              "(TOP_ZONE_MEASURED).")]


def d41_spine_diagram(t0, *, vertebrae, zooms, t1=None, close_arrow_t=None,
                      source_reel="DeGQ3NAC2f9"):
    """D41 spine framework diagram. VERIFIED (#24).

    A vertical anatomical spine — a PHOTOREAL glowing vertebrae column
    (orange core, like a medical illustration) — as the framework diagram.
    Full diagram: the whole spine stands above/behind Sky (top-centre,
    y~0-600), labels on BOTH sides in YELLOW bold sans with thin WHITE
    dashed leader lines to the vertebrae; the full diagram is the open loop
    (all vertebrae visible, none yet explained). Zoom to active vertebra:
    the spine scales up so the active vertebra fills one side of the frame
    (RIGHT in the Goal zoom @12 s: x~620-1080, top to ~y1150; LEFT at @28 s
    — side varies by section; Sky's head bottom-centre, face clear)
    + the section label + a detail cluster beside it (trait list, quotes,
    thumbnails, bar chart, profile card — REAL content, never placeholders);
    each section holds ~4-6 s, then the spine returns to the full mini
    diagram. Close: a thin white curved arrow DRAWS spine→Sky @60-62 s
    (a D16-branch-line cousin). 9 vertebrae: 1 Goal, 2 Person, 3 Avatar,
    4 Gap, 5 Offer, 6 Funnel, 7 Content Pillars, 8 Formats,
    9 Brand & Positioning (number→label mapping transcript-verified).
    "Strategy" is WHITE serif italic with a yellow corner bracket — the
    serif is a BANNED telltale in reels (v6); Q-lane section labels are
    bold grotesque gold. The photoreal spine column itself is an ASSET
    (MUSE-SUPPLY — no code generates it); the builder carries the layout,
    timing, labels and zoom choreography.

    vertebrae: exactly 9 labels in order. zooms: [{"label": str, "t0": float,
    "detail": str}] — one per section, in spoken order.
    """
    if len(vertebrae) != 9:
        raise ValueError(f"D41 is a 9-vertebra spine, got {len(vertebrae)} labels")
    if not zooms:
        raise ValueError("D41 needs at least one section zoom")
    for z in zooms:
        if z["label"] not in vertebrae:
            raise ValueError(f"D41 zoom label {z['label']!r} is not one of the 9 vertebrae")
        if z["t0"] < t0 - 1e-9:
            raise ValueError(f"D41 zoom {z['label']!r} at {z['t0']} precedes t0 {t0}")
    inst = f"D41@{t0:.2f}"
    end = t1 if t1 is not None else zooms[-1]["t0"] + 6.0
    events = [_base(
        "D41", "spine framework (full diagram)", t0, end, TRACKS["hero"],
        _geom(0, 0, 1080, 600),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"label": GOLD, "leader": WHITE, "section_label": GOLD},
        text="spine framework",
        items=[{"vertebrae": list(vertebrae), "vertebrae_n": 9,
                "spine_asset": "photoreal glowing vertebrae column — MUSE-SUPPLY "
                               "asset, not code-generated; orange core remaps to gold glow",
                "leader_style": "thin white dashed lines to each vertebra",
                "notes": "full diagram = the open loop; labels YELLOW bold sans "
                         "both sides (gold in Q's lane); 'Strategy' white serif "
                         "italic + yellow corner bracket in Sky — serif is a "
                         "banned telltale in Q's lane (v6)"}],
        motion={"in": {"type": "hard_cut"}, "out": _hard_cut_out()},
        notes="D41 (#24): full diagram top-centre y0-600; returns between "
              "sections and at the close. Top zone (TOP_ZONE_MEASURED).")]
    for i, z in enumerate(zooms):
        z1 = zooms[i + 1]["t0"] if i + 1 < len(zooms) else end
        events.append(_base(
            "D41", f"spine zoom: {z['label']}", z["t0"], z1, TRACKS["hero"],
            _geom(620, 0, 460, 1150),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"label": GOLD, "detail": WHITE},
            text=z["label"],
            items=[{"vertebra": z["label"], "detail_cluster": z.get("detail", ""),
                    "notes": "active vertebra fills the RIGHT side; Sky's head "
                             "bottom-centre, face clear (frame-verified kf_12s); "
                             "detail cluster is REAL content, never a placeholder"}],
            motion={"in": {"type": "hard_cut",
                           "notes": "hard cuts only between spine states (full <-> zoomed); "
                                    "the spine's scale changes ARE the transitions"},
                    "out": _hard_cut_out()},
            notes=f"Spine zoom {i + 1}/{len(zooms)}: ~4-6 s, then back to full."))
    if close_arrow_t is not None:
        events.append(_base(
            "D41", "spine closing arrow", close_arrow_t, close_arrow_t + 2.0,
            TRACKS["hero"],
            _geom(340, 600, 400, 600),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"line": WHITE},
            text="closing arrow",
            items=[{"path": "thin white curved arrow, spine -> Sky",
                    "notes": "draws @60-62 s in #24; a D16-branch-line cousin"}],
            motion={"in": {"type": "line_draw", "dur_s": 2.0, "easing": "linear"},
                    "out": _hard_cut_out()},
            notes="D41 closing arrow: the only draw-on in the reel."))
    return events


def d42_question_fork(t0, *, header, question, outcomes,
                      serif_outcomes=False, source_reel="DepxHOliSP4"):
    """D42 question card + outcome fork. VERIFIED (#21).

    The reel's payoff, in THREE stages (@~66.5-74.9 s, ends the reel):
    (1) header "THE 1 LEADERSHIP QUESTION" (small white spaced caps + thin
    rule, top-centre y210-270) + a FROSTED GLASS card (rounded rect,
    x115-965 y300-650) containing the question; (2) the question text EXITS,
    leaving the card EMPTY/frosted (blurred doc visible through it), and two
    thin white curved branch lines DRAW down from the card's bottom edge
    (a D16-branch-line fork); (3) outcome pills land ONE AT A TIME at the
    bottom: "OUTCOME A / Lead a department" then "OUTCOME B / Create more
    work". Sky NARRATES the device himself @66-74 s ("just the question
    blurred out with two branches coming down into text") — the strongest
    device confirmation in the batch. The card is NOT the last thing on
    screen — it exits ~73.5 s (hard cut) and the reel ends on the POV desk
    doc ("a nine out of 10 hook" @73.88-74.6), no close, no CTA. Entrance:
    pop ~0.3 s (measured family); exit: hard cut ~73.5 s. Measured outcome
    text is WHITE SERIF
    ITALIC — serif is a BANNED telltale in reels (v6); Q-lane renders outcomes in bold
    grotesque (label gold, text white) unless Q picks the serif
    (serif_outcomes=True).

    outcomes: [(label, text, t0, side), ...] — exactly 2, in landing order,
    sides "left" then "right".
    """
    if len(outcomes) != 2:
        raise ValueError(f"D42 needs exactly 2 outcomes, got {len(outcomes)}")
    (l1, t1_, s1), (l2, t2_, s2) = [(o[0], o[2], o[3]) for o in outcomes]
    if not t1_ < t2_:
        raise ValueError("D42: outcome A must land BEFORE outcome B "
                         "(pills land one at a time)")
    if (s1, s2) != ("left", "right"):
        raise ValueError("D42: outcomes land left then right")
    inst = f"D42@{t0:.2f}"
    end = outcomes[1][2] + 2.0
    events = [_base(
        "D42", "question card", t0, end, TRACKS["hero"],
        _geom(115, 210, 850, 440),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"card": NAVY, "card_opacity": 0.55, "header": WHITE, "text": WHITE},
        text={"header": header, "question": question},
        items=[{"header": header, "question": question,
                "notes": "frosted glass card, blurred doc visible through it; "
                         "question text EXITS at stage 2, leaving the card EMPTY"}],
        motion={"in": _pop_in(), "out": _hard_cut_out()},
        notes="D42 stage 1: header + frosted card + question. Header y210-270 "
              "(TOP_ZONE_MEASURED). Sky narrates this device himself — the "
              "strongest confirmation in Batch 19.")]
    branch_t0 = outcomes[0][2] - 0.5
    events.append(_base(
        "D42", "outcome fork (branch lines)", branch_t0, end, TRACKS["hero"],
        _geom(115, 650, 850, 300),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"line": WHITE},
        text="outcome fork",
        items=[{"branches": 2, "notes": "two thin white curved branch lines DRAW "
                                         "from the card's bottom edge down to two "
                                         "points on the doc (D16-branch-line fork)"}],
        motion={"in": {"type": "line_draw", "dur_s": 1.0, "easing": "linear"},
                "out": _hard_cut_out()},
        notes="D42 stage 2: question exits, card goes empty, branches draw down."))
    for i, (label, text, ot0, side) in enumerate(outcomes):
        x = 30 if side == "left" else 570
        events.append(_base(
            "D42", f"outcome {label}", ot0, end, TRACKS["chip"],
            _geom(x, 860, 480, 110),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"label": GOLD, "text": WHITE},
            text={"label": label, "text": text},
            items=[{"label": label, "text": text, "side": side,
                    "font": ("white serif italic — measured Sky variant, BANNED "
                             "telltale in v6 premium plans (validator rejects it)"
                             if serif_outcomes else
                             "bold grotesque, label gold / text white (Q-lane default; "
                             "Sky's white serif italic is a banned telltale in v6)")}],
            motion={"in": {"type": "pop", "dur_s": POP_S, "easing": "back.out_1.141"},
                    "out": _hard_cut_out()},
            notes=f"D42 stage 3: outcome {i + 1}/2 lands one at a time."))
    return events


def d43_view_count_badge(t0, *, count, t1=None, exhibit_top_y=480,
                         source_reel="DevpJZLk6Km"):
    """D43 view-count badge. VERIFIED (#17/#18).

    An eye icon + white bold count ("1.5M", "31.6M", "1.8M", "1.1M", "3.4M",
    pixel-sampled #F9F9F5) FLOATING ABOVE a phone exhibit — the proof number
    for the exhibit, added by Sky, not part of the source clip. #17: above
    BOTH exhibits; #18: above exhibit 1 only; NOT observed on #18 exhibit 2,
    #21's exhibit, or #27's phone exhibit — the badge is per-exhibit, never
    assumed. Split out as its own device (it was the unnumbered D39 slot in
    worker 1's summary). Distinct from D46's 26.9M badge, which is a dark
    pill bottom-centre of the exhibit side and part of that exhibit's own
    presentation. Q lane: white bold count, eye icon, gold NOT used — the
    count is proof, not a payoff figure.
    """
    if not count or not str(count).strip():
        raise ValueError("D43 needs a view count (e.g. '1.5M')")
    end = t1 if t1 is not None else t0 + 7.0
    return [_base(
        "D43", f"view-count badge: {count}", t0, end, TRACKS["chip"],
        _geom(440, exhibit_top_y - 75, 200, 75),
        status="VERIFIED", source_reel=source_reel,
        colors={"text": WHITE},
        text=str(count),
        items=[{"count": str(count), "icon": "eye", "font_px": 75,
                "notes": "eye icon + white bold count, floats ABOVE the phone "
                         "exhibit; per-exhibit, never assumed"}],
        motion={"in": {"type": "hard_cut",
                       "notes": "enters + exits WITH its exhibit"},
                "out": _hard_cut_out()},
        notes="D43 (#17/#18): Sky-added view badge above a phone exhibit. "
              "Not on every exhibit — record per exhibit.")]


def d44_pov_mini_window(t0, *, pov_lines, shots, t1=None,
                        source_reel="DSI5QVwEnIm"):
    """D44 POV mini-window presentation. VERIFIED (#32, DSI5QVwEnIm).

    A music-only founder vlog fragment built around ONE presentation device:
    the footage plays inside a SMALL ROUNDED-RECT WINDOW centred on a black
    ground (window ~84% of frame width, ~30% of frame height — x~8-92%,
    y~22-52%, rounded corners ~16 px [EST]), STATIC for the whole reel, with
    the POV text line sitting in the BLACK BAND ABOVE it (3 lines, small
    white sans, centred, top zone y~230-346: "POV: / you're getting rinsed
    5.5k/month / for a vancouver shit hole but it's chill"). Hard cuts happen
    INSIDE the window (three shots in #32); the window itself never moves,
    resizes or animates — no entrance, no exit. Same POV-line family as
    DSTdFOPgd6s (full-bleed there, mini-window here) — the line is one
    device, two presentations; the WINDOW is this device. Q lane: the window
    + black surround is the device — keep the window, put Q's POV line above
    it; do NOT expand to full-bleed. Ground is dark navy (Sky black ->
    PWC navy); the surround reads black because it is the ground.
    """
    if not pov_lines:
        raise ValueError("D44 needs at least one POV text line")
    if not shots:
        raise ValueError("D44 needs at least one shot inside the window")
    for s in shots:
        if s[1] < t0 - 1e-9:
            raise ValueError(f"D44 shot {s[0]!r} at {s[1]} precedes t0 {t0}")
    inst = f"D44@{t0:.2f}"
    end = t1 if t1 is not None else shots[-1][1] + 2.0
    window_geom = _geom(86, 422, 908, 576)
    events = [_base(
        "D44", "POV text line", t0, end, TRACKS["chip"],
        _geom(140, 230, 800, 116),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"text": WHITE},
        text="\n".join(pov_lines),
        items=[{"lines": list(pov_lines),
                "notes": "small white sans, centred, static, in the black band "
                         "above the window; shared with DSTdFOPgd6s (full-bleed)"}],
        motion={"in": {"type": "hard_cut"}, "out": _hard_cut_out()},
        notes="D44 POV line: top zone (TOP_ZONE_MEASURED), whole reel, static.")]
    events.append(_base(
        "D44", "mini-window (black ground)", t0, end, TRACKS["asset"],
        _geom(0, 0, 1080, 1920),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"ground": NAVY_DEEP},
        text="mini-window presentation",
        items=[{"window": {"x": 86, "y": 422, "w": 908, "h": 576,
                           "corner_radius_px": 16, "corner_status": "[EST]"},
                "notes": "window static whole reel — never moves/resizes/animates; "
                         "hard cuts happen INSIDE it"}],
        motion={"in": {"type": "hard_cut"}, "out": _hard_cut_out()},
        notes="D44 (#32): footage in a small rounded-rect window centred on a "
              "black ground. Q lane: keep the window, never expand to full-bleed."))
    for i, (label, st0) in enumerate(shots):
        st1 = shots[i + 1][1] if i + 1 < len(shots) else end
        events.append(_base(
            "D44", f"window shot {i + 1}: {label}", st0, st1, TRACKS["asset"],
            window_geom,
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"text": WHITE},
            text=label,
            items=[{"shot": label, "index": i + 1, "total": len(shots)}],
            motion={"in": {"type": "hard_cut",
                           "notes": "hard cut INSIDE the window; the window never moves"},
                    "out": _hard_cut_out()},
            notes=f"D44 inner shot {i + 1}/{len(shots)}."))
    return events


def d45_kinetic_black_card(t0, *, lines, hold_s=2.0, figure=None,
                           source_reel="DSQeVmBk12d"):
    """D45 kinetic-type black card. VERIFIED (#31, DSQeVmBk12d).

    A FULL-SCREEN BLACK frame carrying the thesis words in HUGE YELLOW
    condensed type (supporting words small white), 2-3 stacked lines
    (up to 5 in the "SELL IT / IN THE / FUTURE" instance), holding ~1.5-2.5 s
    between hard cuts — no fade, no slide, hard cut in AND out. Mostly
    word-timed to the spoken keyword ("SELL IT" / "FUTURE" on the figures;
    "PRODUCT" on "improve the product"); one instance is a thesis RECAP at a
    section beat, not word-timed ("YOU SHOULD MAKE SALES TO GET CUSTOMERS"
    @~12 s). Optional small white kicker above, small figure or chart
    squiggle below (a hand-drawn rising line under "PRODUCT" @~46 s).
    Type: condensed grotesque, extra-bold, tight tracking; huge words
    ~150-230 px cap height (8-12% of frame height); Sky's accent here is a
    bright YELLOW (#F5D90A-#FFE600 by eye — NOT Sky's v3 orange #F09828, a
    Dec-2025 kinetic-type palette), remapped to PWC GOLD in Q's lane. The
    black ground stays dark (it is the card, not the palette — dark navy in
    Q's lane). NOT D2 (no kicker+display lockup over footage — these are
    full-screen black cards) and NOT D3 (no pill, no title stack).
    """
    if not lines:
        raise ValueError("D45 needs at least one type line")
    if not any(ln.get("role") == "huge" for ln in lines):
        raise ValueError("D45 needs at least one HUGE thesis line")
    if not 1.5 <= hold_s <= 2.5:
        raise ValueError(f"D45 holds ~1.5-2.5 s, got {hold_s}")
    colors = {"ground": NAVY_DEEP}
    for ln in lines:
        if ln.get("color", "gold") not in ("gold", "white"):
            raise ValueError(f"D45 line colour must be 'gold' or 'white', got {ln.get('color')!r}")
    return [_base(
        "D45", "kinetic-type black card", t0, t0 + hold_s, TRACKS["hero"],
        _geom(0, 0, 1080, 1920),
        status="VERIFIED", source_reel=source_reel,
        colors={"ground": NAVY_DEEP, "huge": GOLD, "small": WHITE},
        text={"lines": [(ln["text"], ln.get("role", "small")) for ln in lines]},
        items=[{"lines": [{"text": ln["text"], "role": ln.get("role", "small"),
                           "color": GOLD if ln.get("color", "gold") == "gold" else WHITE}
                          for ln in lines],
                "figure": figure,
                "notes": "huge words ~150-230 px cap height, condensed extra-bold; "
                         "Sky's bright yellow remapped to PWC gold; small figure / "
                         "chart squiggle below is optional"}],
        motion={"in": {"type": "hard_cut", "notes": "hard cut in, no fade/slide"},
                "out": _hard_cut_out()},
        notes="D45 (#31): full-screen black card, thesis words huge in gold, "
              "holds 1.5-2.5 s, hard cuts both sides. Word-timed, except the "
              "thesis-recap instance (section beat, not word-timed).")]


def d46_vertical_split(t0, *, exhibit_clip, t1, verdict_t=None, replay_t=None,
                       view_badge=None, source_reel="DZXu4j9ATXP"):
    """D46 vertical split-screen, reactor left / exhibit right. VERIFIED (#28).

    A persistent 55/45 VERTICAL split, whole reel: Sky (reactor) occupies the
    LEFT ~55% (x0-594); the exhibit clip occupies the RIGHT ~45% (x594-1080,
    a vertical 9:16 clip inset, full height, with its own baked captions).
    The split never changes; there is no full-screen moment. Reactor watches
    his laptop (looking DOWN, 0-42 s) then turns to camera at the verdict
    (~42 s) — the turn is part of the device. The exhibit plays straight
    through, then REPLAYS its opening once (~30 s), timed to the fix that
    concerns it, so the viewer sees the moment being fixed AS Sky names it.
    The exhibit carries its own view badge (dark pill bottom-centre of the
    exhibit side, "👁 26.9M" — the exhibit's own proof, present the whole
    reel; NOT the D43 floating badge). Distinct from D48 (stacked split) —
    different geometry, same family; do NOT conflate. Q lane: Q left /
    exhibit right; captions bottom-left on Q's half, left-aligned; the view
    badge stays on the exhibit's side; Q's face is on screen from frame 1
    (watching), turning to camera at the verdict.
    """
    if not exhibit_clip:
        raise ValueError("D46 needs a REAL exhibit clip — never a still")
    if t1 <= t0:
        raise ValueError("D46 needs t1 > t0 (persistent whole-reel split)")
    if verdict_t is not None and not (t0 <= verdict_t <= t1):
        raise ValueError(f"D46 verdict_t {verdict_t} outside the reel span")
    if replay_t is not None and not (t0 <= replay_t <= t1):
        raise ValueError(f"D46 replay_t {replay_t} outside the reel span")
    inst = f"D46@{t0:.2f}"
    return [_base(
        "D46", "vertical split: reactor (left)", t0, t1, TRACKS["aroll"],
        _geom(0, 0, 594, 1920),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"text": WHITE},
        text="reactor",
        items=[{"posture": "watching laptop (looking down) until the verdict, "
                           "then turns to camera", "verdict_t": verdict_t,
                "notes": "Q's face on screen from frame 1; the turn IS the device"}],
        motion={"in": {"type": "hard_cut", "notes": "split present from frame 0"},
                "out": _hard_cut_out()},
        notes="D46 (#28): persistent 55/45 vertical split, whole reel. "
              "Top zone (TOP_ZONE_MEASURED — full-height halves from y0)."),
        _base(
        "D46", "vertical split: exhibit (right)", t0, t1, TRACKS["asset"],
        _geom(594, 0, 486, 1920),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"text": WHITE},
        text="exhibit",
        items=[{"clip": exhibit_clip, "clip_plays": True,
                "replay_t": replay_t, "view_badge": view_badge,
                "notes": "vertical 9:16 clip, full height, own baked captions; "
                         "replays its opening once, timed to the fix; view badge "
                         "is the exhibit's own (dark pill, bottom-centre of its side)"}],
        motion={"in": {"type": "hard_cut"}, "out": _hard_cut_out()},
        notes="D46 exhibit side: real clip, never a still.")]


def d47_binary_label_pair(t0, *, labels, winner, winner_t=None,
                          source_reel="DSB8X22kSfe"):
    """D47 binary label pair, anchored. VERIFIED (#35, DSB8X22kSfe).

    Two small white sans labels naming two options/concepts, popped in one at
    a time (~0.5 s apart) and ANCHORED TO REAL-WORLD OBJECTS IN THE SET —
    here the two ceiling lights ("Strategy" top-left over the left light,
    "Idea" top-right over the right light; "Idea" lands first ~26.0 s,
    "Strategy" second ~26.5 s). They persist while the speaker weighs the
    options (~26.0-~28.5 s; both gone by ~29.0 s), then are RESOLVED by a
    headline lockup naming the winner ("I'm focusing on Idea" @~30.5-31.5 s)
    — the lockup IS the
    resolution; never leave both labels hanging with no resolution. NOT D11
    (chip cloud — these are two labelled options, not descriptive chips) and
    NOT D7 (Venn — no overlap, no figures). The anchoring to set objects is
    part of the device. Q lane: anchor to two real objects in Q's set (two
    lights, two frames); the winner gets the lockup.

    labels: [(text, anchor, t0, x, y), ...] — exactly 2, in landing order;
    anchor is the set object (e.g. "left ceiling light"). winner: the
    winning label's text (must match one of the two labels).
    """
    if len(labels) != 2:
        raise ValueError(f"D47 needs exactly 2 labels, got {len(labels)}")
    if not labels[0][2] < labels[1][2]:
        raise ValueError("D47: the two labels pop in one at a time (~0.5 s apart)")
    if winner not in (labels[0][0], labels[1][0]):
        raise ValueError(f"D47 winner {winner!r} is not one of the two labels")
    inst = f"D47@{t0:.2f}"
    lockup_t = winner_t if winner_t is not None else labels[1][2] + 4.0
    events = []
    for i, (text, anchor, lt0, lx, ly) in enumerate(labels):
        events.append(_base(
            "D47", f"binary label: {text}", lt0, lockup_t + 2.0, TRACKS["chip"],
            _geom(lx, ly, 220, 60),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"text": WHITE},
            text=text,
            items=[{"label": text, "anchor": anchor,
                    "notes": "small white sans label, anchored to a REAL set "
                             "object (not screen coordinates)"}],
            motion={"in": {"type": "pop", "dur_s": 0.15, "easing": "back.out_1.141",
                         "notes": f"label {i + 1}/2, ~0.5 s after the other"},
                    "out": _hard_cut_out()},
            notes="D47 labels persist while the speaker weighs the options. "
                  "Top zone (TOP_ZONE_MEASURED — measured y~90-135)."))
    events.append(_base(
        "D47", f"resolution lockup: {winner}", lockup_t, lockup_t + 2.0,
        TRACKS["chip"],
        _geom(140, 320, 800, 100),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"text": WHITE, "winner": GOLD},
        text=f"I'm focusing on {winner}",
        items=[{"winner": winner,
                "notes": "the headline lockup IS the resolution — the winner is named"}],
        motion={"in": {"type": "pop", "dur_s": POP_S, "easing": "back.out_1.141"},
                "out": _hard_cut_out()},
        notes="D47 resolution: labels exit WITH the lockup — never leave both "
              "labels hanging with no resolution."))
    return events


def d48_stacked_split(t0, *, exhibit, t1, divider_frac=0.48, caption_y=None,
                      source_reel="DRoLuFRAnwh"):
    """D48 stacked split-screen, exhibit top / reactor bottom (persistent).
    VERIFIED (#36/#37/#38 + #39/#40/#49 — MERGED device, see
    DEVICE-RECONCILIATION-B19.md).

    A persistent HORIZONTAL split, whole reel: the exhibit in the TOP ~half,
    the reactor in the BOTTOM ~half, a thin white divider (~2 px) between
    them. The exhibit is a SCREEN RECORDING WITH ITS CHROME INTACT —
    full-width desktop-web profile scroll (DRo) or pillarboxed mobile reel
    with like rail (DRg/DRe); the chrome (counts, comments, footer) is part
    of the proof — never crop it. The exhibit CONTENT changes on the
    speaker's beats (scroll / post open / scroll back; top-half swaps every
    ~6-9 s in #39/#40/#49) while the GEOMETRY never moves. The reactor's
    captions sit at the TOP of the reactor half, just below the divider
    (Sky's 2025-era serif there is a banned telltale in v6; Q-lane D48 uses Sky's sans
    captions in the same placement unless Q picks the serif). The bottom half
    is one continuous take; only the top half swaps content. Divider at ~47%
    (DRo, frame-measured y~600/1280) to 50% (#39/#40/#49) — pass
    divider_frac per reel. Distinct from D46 (vertical split) and D9 (a
    full-screen exhibit cutaway — here the exhibit never takes the frame).

    exhibit: {"clip_path": str, "kind": str, "segments": [(label, t0), ...]}
    — segments are the exhibit-content beats (optional; without them the
    exhibit is one continuous recording). kind: "desktop_profile_scroll" |
    "mobile_reel" | "profile_grid" | "screen_recording".
    """
    if not exhibit.get("clip_path"):
        raise ValueError("D48 needs a REAL exhibit recording — never a still")
    if not 0.40 <= divider_frac <= 0.55:
        raise ValueError(f"D48 divider_frac must be 0.40-0.55, got {divider_frac}")
    segments = exhibit.get("segments") or []
    for i, (label, st0) in enumerate(segments):
        if not (t0 <= st0 <= t1):
            raise ValueError(f"D48 exhibit segment {label!r} at {st0} outside the reel span")
        if i and segments[i - 1][1] >= st0:
            raise ValueError("D48 exhibit segments must be in ascending time order")
    inst = f"D48@{t0:.2f}"
    divider_y = round(1920 * divider_frac)
    cap_y = caption_y if caption_y is not None else divider_y + 20
    events = [_base(
        "D48", "stacked split: exhibit (top)", t0, t1, TRACKS["asset"],
        _geom(0, 0, 1080, divider_y),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"text": WHITE},
        text="exhibit",
        items=[{"clip": exhibit["clip_path"], "kind": exhibit.get("kind", "screen_recording"),
                "chrome_intact": True, "segments": [s[0] for s in segments],
                "notes": "screen recording with chrome intact — counts/comments/footer "
                         "are the proof; content changes on the speaker's beats, "
                         "geometry never moves"}],
        motion={"in": {"type": "hard_cut", "notes": "split present from frame 0"},
                "out": _hard_cut_out()},
        notes="D48 exhibit half: top ~half, whole reel. Top zone "
              "(TOP_ZONE_MEASURED — exhibit starts at y0)."),
        _base(
        "D48", "stacked split: divider", t0, t1, TRACKS["hero"],
        _geom(0, divider_y - 1, 1080, 2),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"line": WHITE},
        text="divider",
        items=[{"thickness_px": 2}],
        motion={"in": {"type": "hard_cut"}, "out": _hard_cut_out()},
        notes="D48 divider: thin white line (~2 px), whole reel."),
        _base(
        "D48", "stacked split: reactor (bottom)", t0, t1, TRACKS["aroll"],
        _geom(0, divider_y, 1080, 1920 - divider_y),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"text": WHITE},
        text="reactor",
        items=[{"caption_y": cap_y, "take": "one continuous take",
                "notes": "reactor captions sit at the TOP of the reactor half, "
                         "just below the divider (caption_y); Sky's serif there is "
                         "serif there is banned in v6 — Q-lane D48 uses sans "
                         "in the same placement"}],
        motion={"in": {"type": "hard_cut"}, "out": _hard_cut_out()},
        notes="D48 reactor half: bottom ~half, one continuous take.")]
    for i, (label, st0) in enumerate(segments):
        st1 = segments[i + 1][1] if i + 1 < len(segments) else t1
        events.append(_base(
            "D48", f"exhibit segment: {label}", st0, st1, TRACKS["asset"],
            _geom(0, 0, 1080, divider_y),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"text": WHITE},
            text=label,
            items=[{"segment": label, "index": i + 1, "total": len(segments)}],
            motion={"in": {"type": "hard_cut",
                           "notes": "hard cut between top-half exhibits, no slide/fade"},
                    "out": _hard_cut_out()},
            notes=f"D48 exhibit segment {i + 1}/{len(segments)}: lands on the spoken beat."))
    return events


def d49_annotation_outline(t0, *, shape, target, duration_s=1.0, label=None,
                           x=140, y=320, w=800, h=380,
                           source_reel="DRXfqHcAkve"):
    """D49 red annotation outline. VERIFIED (#39/#40/#44/#49).

    A hand-drawn-style outline drawn ON a proof screen to circle the claim
    text: an ELLIPSE around the profile header (bio, follower count — #39,
    verified f_010/f_013), a RECTANGLE around "Guided by an 8-figure CEO" on
    the whiteboard reel (#40, ~4 s, gone by 5 s), ELLIPSES on the grid (#49),
    and a free-standing GLOWING RING ("LOOK AT BREZ", #44, 17.6-~19 s) that
    points at a profile without circling text. Thin stroke, slightly
    irregular (hand-drawn feel), brief life ~1 s for the ellipse/rectangle
    (the ring holds ~1.5 s). This is Sky's OWN red — his semantic "bad / look
    here" red ON a proof screen — and it is the ONE red in the registry: it
    is implemented with the GOLD remap in Q's lane per the palette rule
    (Sky red #E86A5E -> gold; the device — circle-the-claim — transfers, the
    colour does not). Never emit red. The outline follows the claim text, so
    its geometry is per-take (x/y/w/h params); it sits top-zone when the
    proof screen does (TOP_ZONE_MEASURED).
    """
    if shape not in ("ellipse", "rectangle", "ring"):
        raise ValueError(f"D49 shape must be 'ellipse', 'rectangle' or 'ring', got {shape!r}")
    if not target or not target.strip():
        raise ValueError("D49 needs the claim text / target it circles")
    if shape == "ring" and not label:
        raise ValueError("D49 ring variant needs its label text (e.g. 'LOOK AT BREZ')")
    return [_base(
        "D49", f"annotation outline ({shape}): {target}", t0, t0 + duration_s,
        TRACKS["chip"],
        _geom(x, y, w, h),
        status="VERIFIED", source_reel=source_reel,
        colors={"outline": GOLD, "label": WHITE},
        text=label or target,
        items=[{"shape": shape, "target": target, "label": label,
                "stroke_px": 4, "hand_drawn": True,
                "sky_colour": "red #E86A5E (remapped to gold — never emitted)",
                "notes": "thin, slightly irregular stroke; brief life ~1 s "
                         "(ring holds ~1.5 s); circles the CLAIM text on the proof screen"}],
        motion={"in": {"type": "pop", "dur_s": 0.2, "easing": "back.out_1.141"},
                "out": _hard_cut_out()},
        notes="D49 (#39/#40/#44/#49): Sky's own red outline, GOLD in Q's lane. "
              "Circle-the-claim transfers; the red never does.")]


def d50_gradient_script_headline(t0, *, text, hold_s=3.0, position="chest",
                                 entrance="pop",
                                 source_reel="DQDYFFHif7v"):
    """D50 gradient script headline. VERIFIED (#41/#42/#43/#44/#46).

    A single- (or two-)line ITALIC SCRIPT headline in a GREEN→PURPLE
    gradient with GLOW, laid over the speaker's chest/upper torso or above
    the head — the concept/verdict name: "THEY BUILD Relationships",
    "Perfect Split", "ANTI GURU GURU", "COMMENT NOTION", "HEY, I'M SKY",
    "WARREN", "SKY TAN". The 2025-era accent headline — ONE device across
    five reels. Gradient runs green→purple (or purple→green) within the
    word; sampled purples #863BC5 (#46 "WARREN") and #5421A0 (#44 "ANTI
    GURU"). Q lane: the gradient + glow + script face transfer; the colours
    remap to PWC teal→gold (green->teal structure, purple->gold payoff) —
    purple is not a PWC colour and is never emitted. A warning-triangle
    issue marker sometimes anchors it (DP4r6BbEvHg, "It sucks writing") —
    recorded in that reel's DECODE.md as part of D50's system, not a
    separate device.
    """
    if not text or not text.strip():
        raise ValueError("D50 needs headline text")
    if position == "chest":
        geom = _geom(90, 950, 900, 220)
    elif position == "top":
        geom = _geom(90, 120, 900, 220)
    else:
        raise ValueError(f"D50 position must be 'chest' or 'top', got {position!r}")
    if entrance not in ("pop", "draw_in"):
        raise ValueError(f"D50 entrance must be 'pop' or 'draw_in', got {entrance!r}")
    in_motion = ({"type": "pop", "dur_s": POP_S, "easing": "back.out_1.141"}
                 if entrance == "pop" else
                 {"type": "draw_in", "dur_s": 0.3, "easing": "linear",
                  "notes": "script word DRAWS IN stroke by stroke (DeSTW "
                           "'Strategy work' 2.8-3.1 s, Batch 36 B1) — a "
                           "measured entrance variant of this device"})
    return [_base(
        "D50", "gradient script headline", t0, t0 + hold_s, TRACKS["chip"],
        geom,
        status="VERIFIED", source_reel=source_reel,
        colors={"gradient_from": TEAL, "gradient_to": GOLD, "glow": GOLD},
        text=text,
        items=[{"font": "italic script", "glow": True,
                "sky_gradient": "green→purple (sampled purples #863BC5 / #5421A0 — "
                                "remapped teal→gold, never emitted)",
                "notes": "the concept/verdict name, over chest/upper torso or "
                         "above the head"}],
        motion={"in": in_motion,
                "out": _hard_cut_out()},
        sfx="pop-medium-in.wav",
        notes="D50 (#41-#44/#46): gradient script headline, teal→gold in Q's lane. "
              "Top position sits in the IG top zone (TOP_ZONE_MEASURED).")]


def d51_player_stats_card(t0, *, name, stats, t1=None, location="",
                          source_reel="DJccT_xSWuT"):
    """D51 video-game player-stats T-pose card. VERIFIED (#46, DJccT_xSWuT).

    A fighting-game / RPG stat screen used to introduce a collaborator and
    state the division of labour — the stats ARE the introduction. A
    FULL-BODY T-POSE shot of the person (arms straight out, spinning slowly),
    a gradient NAME HEADLINE at the top of the frame, a green "PLAYER STATS"
    label bottom-left, and a GREEN STAT LIST accumulating LINE BY LINE below
    it as each stat is spoken, plus a GREEN GLOW OUTLINE around the person's
    body. Warren (24.1-30.9 s, doorway, green neon light): 9'11", 420 POUNDS,
    0 NOTION SKILLS, 42 CODING, 72 AUTOMATIONS, 1/2 BITCHES. Sky Tan
    (31.5-36.0 s, living room): 4'7", 250 POUNDS, 99 NOTION SKILLS,
    21 AUTOMATION, 0 CODING, 0 BITCHES. The two cards are a MATCHED PAIR
    (same layout, same colours, same motion) — the second card's humour
    depends on the first. Q lane: the format transfers directly (T-pose +
    name + stats); purple gradient remaps to gold/teal; the stat WORDS are
    Q's (Sky's "BITCHES" is his word, never Q's). Needs a full-body T-pose
    shoot of the person — footage, not a graphic.

    stats: [(text, t0), ...] in spoken order — each stat appears on its
    spoken word.
    """
    if not name or not name.strip():
        raise ValueError("D51 needs the person's name")
    if not stats:
        raise ValueError("D51 needs at least one stat line")
    for i, (text, st0) in enumerate(stats):
        if not text or not str(text).strip():
            raise ValueError("D51 stat lines need text")
        if st0 < t0 - 1e-9:
            raise ValueError(f"D51 stat {text!r} at {st0} precedes t0 {t0}")
        if i and stats[i - 1][1] >= st0:
            raise ValueError("D51 stats must accumulate in ascending time order")
    inst = f"D51@{t0:.2f}"
    end = t1 if t1 is not None else stats[-1][1] + 1.0
    events = [_base(
        "D51", f"T-pose card: {name}", t0, end, TRACKS["aroll"],
        _geom(0, 0, 1080, 1920),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"text": WHITE},
        text=name,
        items=[{"person": name, "location": location,
                "glow_outline": True, "spin": "slow, arms straight out",
                "notes": "full-body T-pose footage (Q's own shoot); green glow "
                         "outline around the body (teal in Q's lane)"}],
        motion={"in": {"type": "hard_cut"},
                "spin": {"type": "slow_spin", "notes": "person spins slowly with arms out"},
                "out": _hard_cut_out()},
        sound={"ui_blip": {"window_s": "31.26-31.68", "band_hz": "7000-7800",
                           "band_rms_dbfs": -33.0, "control_dbfs": -47.0,
                           "status": "VERIFIED candidate (Batch 36 soundmap, moderate confidence)",
                           "notes": "INSTANCE NOTE, not a device: the set's one "
                                    "isolated UI blip rides the Sky player-stats "
                                    "card swap in DJccT_xSWuT; the Warren-entrance "
                                    "candidate (21.66-22.54 s) is not counted. "
                                    "Local match: sfx-kit digital-blip-subtle.wav"}},
        notes="D51 (#46): T-pose character card. The two cards are a matched pair."),
        _base(
        "D51", f"T-pose name: {name}", t0, end, TRACKS["chip"],
        _geom(90, 100, 900, 140),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"gradient_from": GOLD, "gradient_to": TEAL, "glow": GOLD},
        text=name,
        items=[{"font": "gradient headline, top of frame",
                "notes": "Sky's purple gradient remapped to gold/teal"}],
        motion={"in": {"type": "pop", "dur_s": POP_S, "easing": "back.out_1.141"},
                "out": _hard_cut_out()},
        notes="D51 name headline: top of frame (TOP_ZONE_MEASURED)."),
        _base(
        "D51", "PLAYER STATS label", t0, end, TRACKS["chip"],
        _geom(60, 1300, 400, 60),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"label": TEAL},
        text="PLAYER STATS",
        items=[{"label": "PLAYER STATS", "position": "bottom-left"}],
        motion={"in": {"type": "hard_cut"}, "out": _hard_cut_out()},
        notes="D51 stat label: green in Sky, teal in Q's lane.")]
    for i, (text, st0) in enumerate(stats):
        events.append(_base(
            "D51", f"player stat {i + 1}: {text}", st0, end, TRACKS["chip"],
            _geom(60, 1380 + i * 70, 600, 60),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"stat": TEAL},
            text=str(text),
            items=[{"stat": str(text), "index": i + 1, "total": len(stats),
                    "notes": "stat appears ON its spoken word; list accumulates "
                             "line by line, bottom-left, left-aligned, bullet per line"}],
            motion={"in": {"type": "pop", "dur_s": 0.15, "easing": "back.out_1.141"},
                    "out": _hard_cut_out()},
            notes=f"D51 stat {i + 1}/{len(stats)}."))
    return events


def d52_human_ai_split(t0, *, headline, actors, t1=None,
                       source_reel="DP4r6BbEvHg"):
    """D52 human/AI split card 70% YOU / 30% AI. VERIFIED (#43, DP4r6BbEvHg).

    A two-actor split card over a BLURRED A-roll (focus pull — the background
    goes soft while the graphics stay sharp): the gradient script headline
    ("Perfect Split", D50 family) on top, then ONE FIGURE PER SPOKEN NUMBER
    (D37's rule — never both at once): Sky's head cutout (sunglasses) +
    "70% YOU" lands on "70%" (37.1 s), then the ChatGPT logo + "30% AI" on
    "30%" (38.4 s). The split is a VERDICT, not a chart: no donut, no bars —
    two labelled actors with percentages. Distinct from D27 (a donut split
    chart of IG insights). Q lane: Q's head cutout + Q's tool logo, Q's
    percentages, Q's words.

    actors: [(label, kind, t0), ...] — exactly 2, in landing order;
    kind "head_cutout" | "logo".
    """
    if len(actors) != 2:
        raise ValueError(f"D52 needs exactly 2 actors, got {len(actors)}")
    for kind in (actors[0][1], actors[1][1]):
        if kind not in ("head_cutout", "logo"):
            raise ValueError(f"D52 actor kind must be 'head_cutout' or 'logo', got {kind!r}")
    if not actors[0][2] < actors[1][2]:
        raise ValueError("D52: the first actor must land BEFORE the second "
                         "(one figure per spoken number, D37's rule)")
    inst = f"D52@{t0:.2f}"
    end = t1 if t1 is not None else actors[1][2] + 3.0
    events = [_base(
        "D52", "human/AI split (blurred A-roll)", t0, end, TRACKS["aroll"],
        _geom(0, 0, 1080, 1920),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"text": WHITE},
        text="blurred A-roll",
        items=[{"background": "blurred A-roll (focus pull — background soft, "
                              "graphics sharp)"}],
        motion={"in": {"type": "hard_cut"}, "out": _hard_cut_out()},
        notes="D52 background: blurred Sky (focus pull)."),
        _base(
        "D52", f"split headline: {headline}", t0, end, TRACKS["chip"],
        _geom(90, 300, 900, 160),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"gradient_from": TEAL, "gradient_to": GOLD, "glow": GOLD},
        text=headline,
        items=[{"font": "italic script (D50 family)",
                "notes": "gradient script headline on top of the split card"}],
        motion={"in": {"type": "pop", "dur_s": POP_S, "easing": "back.out_1.141"},
                "out": _hard_cut_out()},
        notes="D52 headline: D50-family gradient script, teal→gold in Q's lane.")]
    for i, (label, kind, at0) in enumerate(actors):
        x = 90 if i == 0 else 570
        events.append(_base(
            "D52", f"split actor {i + 1}: {label}", at0, end, TRACKS["chip"],
            _geom(x, 700, 420, 300),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"label": WHITE},
            text=label,
            items=[{"label": label, "kind": kind,
                    "notes": ("own head cutout (D23 family, reused as a split actor)"
                              if kind == "head_cutout" else
                              "tool logo (ChatGPT logo in #43 — Q's tool logo in Q's lane)")}], 
            motion={"in": {"type": "pop", "dur_s": POP_S, "easing": "back.out_1.141"},
                    "out": _hard_cut_out()},
            notes=f"D52 actor {i + 1}/2: lands on its spoken number."))
    return events


def d53_smpte_gag(t0, *, clip_path, caption="SHOW PROOF", duration_s=1.8,
                  source_reel="DQDYFFHif7v"):
    """D53 SMPTE colour-bars "SHOW PROOF" gag. VERIFIED, SINGLE-USE (#41).

    A full-screen SMPTE colour-bars test pattern — a REAL clip file (visibly
    named "…B_D.mp4" in #41) — with Sky's white sans caption "SHOW PROOF"
    centred. It is the visual for "show proof": a "broken"/placeholder video
    standing in for content with no proof. Pixel-sampled bars: green #2DDF25,
    magenta #920099 (true SMPTE bars, not a drawn plate). Status: SINGLE-USE
    in this batch (one reel, one beat) — the builder carries
    ``single_use=True`` and must NOT be treated as a core Sky device until a
    second example appears. The bars are a real clip file (footage) — the
    bar colours are footage pixels, never emitted as graphics, so no palette
    remap applies to them; only the caption is a graphic (white sans).
    """
    if not clip_path:
        raise ValueError("D53 needs the REAL colour-bars clip file — never a drawn plate")
    return [_base(
        "D53", "SMPTE gag: SHOW PROOF", t0, t0 + duration_s, TRACKS["asset"],
        _geom(0, 0, 1080, 1920),
        status="VERIFIED", source_reel=source_reel,
        colors={"caption": WHITE},
        text=caption,
        items=[{"clip": clip_path, "bars": "SMPTE colour bars (real clip — footage)",
                "single_use": True,
                "notes": "single-use gag until a second example appears; the bars "
                         "are footage pixels, not graphics"}],
        motion={"in": {"type": "hard_cut"}, "out": _hard_cut_out()},
        notes="D53 (#41): colour-bars gag, ~1.8 s, white sans caption centred. "
              "Single-use — do not treat as a core device.")]


def d54_grid_workflow_strip(t0, *, steps, t1=None, source_reel="DP4r6BbEvHg"):
    """D54 grid-background workflow strip. VERIFIED (#43, DP4r6BbEvHg).

    A BLACK background with a faint dark GRID (thin grey gridlines, ~60 px
    cells) fills the frame (18-29 s in #43). Workflow steps are presented
    ONE AT A TIME, centred, each a small icon + white caps label: (1) Sky's
    head cutout (sunglasses) + "SO FIRST" + "'GIVE THE CONTEXT' / ALL THE
    CONTEXT OF THE VIDEO"; (2) ChatGPT logo (teal rounded square) + "AI TO
    SYNTHESIZE" + "SYNTHESIZE THOUGHTS INTO A COHERENT FEW SENTENCES"; (3)
    "CREATE A STRUCTURE OF THE VIDEO" + "IN THE OVERALL / DNA OF THE VIDEO."
    Steps SLIDE HORIZONTALLY — the outgoing step's text is visible sliding
    off the left edge as the next slides in. The head cutout is Sky's own
    face (sunglasses) as the "you" avatar in the workflow — the D23 cutout
    reused as a workflow actor. Distinct from D13: D13 is a horizontal ROW
    of named steps that activate in place; D54 is a full-screen grid stage
    with ONE step centred at a time, sliding horizontally. The step-slide
    direction/speed is bracketed from one frame (f_023's sliding text) —
    recorded [EST] in the motion.

    steps: [{"icon": str, "label": str, "sublabel": str, "t0": float}] in order.
    """
    if not steps:
        raise ValueError("D54 needs at least one workflow step")
    for i, s in enumerate(steps):
        if not s.get("label") or not s["label"].strip():
            raise ValueError("D54 steps need a label")
        if s["t0"] < t0 - 1e-9:
            raise ValueError(f"D54 step {s['label']!r} at {s['t0']} precedes t0 {t0}")
        if i and steps[i - 1]["t0"] >= s["t0"]:
            raise ValueError("D54 steps must be in ascending time order")
    inst = f"D54@{t0:.2f}"
    end = t1 if t1 is not None else steps[-1]["t0"] + 2.0
    events = [_base(
        "D54", "grid workflow ground", t0, end, TRACKS["hero"],
        _geom(0, 0, 1080, 1920),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"ground": NAVY_DEEP, "gridline": GREY_MID},
        text="grid workflow strip",
        items=[{"cell_px": 60, "gridline": "thin grey gridlines",
                "notes": "black grid ground fills the frame; one step centred at a time"}],
        motion={"in": {"type": "hard_cut"}, "out": _hard_cut_out()},
        notes="D54 (#43): full-screen grid stage.")]
    for i, s in enumerate(steps):
        st1 = steps[i + 1]["t0"] if i + 1 < len(steps) else end
        events.append(_base(
            "D54", f"workflow step {i + 1}: {s['label']}", s["t0"], st1,
            TRACKS["hero"],
            _geom(140, 700, 800, 300),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"label": WHITE, "sublabel": WHITE},
            text={"label": s["label"], "sublabel": s.get("sublabel", "")},
            items=[{"icon": s.get("icon", ""), "label": s["label"],
                    "sublabel": s.get("sublabel", ""), "index": i + 1,
                    "total": len(steps)}],
            motion={"in": {"type": "slide_horizontal", "dur_s": 0.4,
                           "easing": "ease_out_cubic",
                           "notes": "[EST] slide direction/speed bracketed from one "
                                    "frame (f_023's sliding text) — outgoing text "
                                    "visible sliding off the left edge"},
                    "out": {"type": "slide_horizontal", "dur_s": 0.4,
                            "notes": "[EST] slides out left as the next slides in"}},
            notes=f"D54 step {i + 1}/{len(steps)}: one step centred at a time."))
    return events


# ------------------------------------------------------- D55-D56 (Batch 36)
# From the Batch 36 completion pass: P14/P15 strip-resolved decodes
# (notes_DeYKkAIgVfL.md / notes_DeSTWxcDTA7.md, worker B1) swept against
# D1-D54. Everything else in those reels deduped into existing devices
# (see WORKER-D-REPORT.md); these two mechanics had no coded home.
def d55_numbered_pill_system(t0, *, pills, source_reel="DeYKkAIgVfL"):
    """D55 numbered association pill system. VERIFIED (DeYKkAIgVfL, P14).

    The case-study walkthrough device (Batch 36 B1, strip-resolved): the
    numbered chips (#1 #2 #3 #4, accent) are PRE-SHOWN AS A ROW at the
    chest during the preceding headline beat (visible at 44.4 s) — the
    full set is on screen before any pill's text exists. Each pill then
    activates the SAME way, in spoken order:
      1. the PREVIOUS pill's text exits in a BLURRED SLIDE (~0.7 s before
         the number word; #1 text out ~50.7-50.9 s, exhibits out blurred
         ~56.9-57.0 s);
      2. the active chip stands ALONE briefly, landing ON its number word
         ("Number two" 50.92 s -> chip alone ~51.0 s; "Number three"
         56.96 s -> ~57.0-57.2 s);
      3. the pill's text TYPES IN BY WORD GROUPS over ~1.0-1.3 s tracking
         the spoken words (#1 builds 45.9-46.8 s; #2 51.5-52.2 s;
         #3 57.9-58.2 s; #4 67.3-68.1 s). The pill does NOT pop in whole.
    Exhibits for each pill pop/stagger above his head while it is held
    (Jessi still ~45.9 s; shared-challenge cluster ~55.9-56.3 s; income
    card pops ~57.9 s simultaneous with the #3 text start).
    Distinct from D3 (one pill under a title stack, hard swap ~10 s), D5-list
    (vertical pill stack that sharpens) and D11 (chips landing one by one —
    here the chips are ALL pre-shown and only the TEXT activates).
    Q lane: chips gold, text white on navy; the subject's exhibits are real.

    pills: [{"number": int, "text": str, "chip_alone_t": float,
             "text_t0": float, "text_t1": float}] in spoken order. The row
    event spans from t0 (pre-shown) to the last pill's hold end.
    """
    if len(pills) < 2:
        raise ValueError("D55 needs at least 2 numbered pills (the row is the system)")
    for i, pl in enumerate(pills):
        if not pl.get("text") or not pl["text"].strip():
            raise ValueError("D55 pills need text")
        if pl["text_t0"] < pl["chip_alone_t"] - 1e-9:
            raise ValueError(f"D55 pill #{pl.get('number')}: text starts before the chip stands alone")
        if i and pills[i - 1]["text_t0"] >= pl["text_t0"]:
            raise ValueError("D55 pills activate in spoken (ascending) order")
    inst = f"D55@{t0:.2f}"
    end = pills[-1]["text_t1"] + 4.0
    events = [_base(
        "D55", "numbered pill row (pre-shown)", t0, end, TRACKS["chip"],
        _geom(240, 980, 600, 80),
        status="VERIFIED", source_reel=source_reel, instance=inst,
        colors={"chip": GOLD, "chip_text": NAVY_DEEP},
        text="numbered pill row",
        items=[{"chips": [pl["number"] for pl in pills],
                "notes": "ALL numbered chips pre-shown as a row at the chest "
                         "before any pill text exists (DeYKk: visible 44.4 s)"}],
        motion={"in": {"type": "hard_cut", "notes": "row pre-shown with the headline beat"},
                "out": _hard_cut_out()},
        notes="D55 row: the pre-shown chip row is the open loop — the viewer "
              "sees how many associations are coming.")]
    for i, pl in enumerate(pills):
        prev_exit = pl["chip_alone_t"] - 0.7 if i else None
        events.append(_base(
            "D55", f"pill #{pl['number']}: {pl['text']}", pl["chip_alone_t"],
            (pills[i + 1]["chip_alone_t"] - 0.7 if i + 1 < len(pills) else end),
            TRACKS["chip"],
            _geom(140, 1080, 800, 110),
            status="VERIFIED", source_reel=source_reel, instance=inst,
            colors={"chip": GOLD, "text": WHITE, "pill_fill": NAVY},
            text=pl["text"],
            items=[{"number": pl["number"], "text": pl["text"],
                    "chip_alone_t": pl["chip_alone_t"],
                    "prev_text_exit": ({"type": "blurred_slide", "at_s": prev_exit,
                                        "notes": "previous pill's text exits in a "
                                                 "blurred slide ~0.7 s before the "
                                                 "number word"} if i else None),
                    "notes": "chip stands alone ON its number word, then the "
                             "text types in by word groups tracking speech"}],
            motion={"in": {"type": "type_in_word_groups",
                           "t0_word_groups": pl["text_t0"], "t1_word_groups": pl["text_t1"],
                           "notes": "text types in by word groups over ~1.0-1.3 s "
                                    "tracking the spoken words — the pill does "
                                    "NOT pop in whole"},
                    "out": {"type": "blurred_slide",
                            "notes": "this pill's text exits in a blurred slide "
                                     "~0.7 s before the next number word "
                                     "(last pill: hard cut with the beat)"}},
            sfx="pop-small-in.wav",
            notes=f"D55 pill {i + 1}/{len(pills)}: blurred-slide handoff -> "
                  "chip alone on the number word -> word-group type-in."))
    return events


def d56_new_post_ui_shrink(t0, *, ui_clip, duration_s=1.6,
                           source_reel="DeSTWxcDTA7"):
    """D56 "New reel" UI exhibit — shrink-into-UI. VERIFIED, SINGLE INSTANCE
    (DeSTWxcDTA7 form 4a, Batch 36 B1 strip pass).

    The B&W talking-head composition SHRINKS (scale-down transform over
    ~14.4-14.9 s) into the video thumbnail of a full-screen IG "New reel"
    posting screen ("Edit cover", caption field, Tag people / Add location
    rows, Share button). The UI holds to ~15.8 s (its thumbnail flickers
    B&W/red-tinted ~15.2 s — footage pixels, not a graphic; a head cutout
    rides the UI's bottom edge), then EXITS ON A HARD CUT at 16.0 s — the
    reel's only scene-threshold event (strip frame-diff peak 54.6, the
    largest frame change in the reel). Distinct from D22 (the dashed
    "New Post" placeholder card that builds ABOVE his head after the cut —
    form 4b) and from D9 (an exhibit that hard-cuts in full-frame — here
    the SPEAKER's own frame becomes the exhibit's thumbnail).
    SINGLE INSTANCE: one reel, one beat — flagged like D53; do not treat
    as a core device until a second example appears.
    Q lane: Q's real posting UI (screen recording), never a redrawn fake.
    """
    if not ui_clip:
        raise ValueError("D56 needs the REAL posting-UI recording — never a redrawn fake")
    return [_base(
        "D56", "new-reel UI exhibit (shrink-in)", t0, t0 + duration_s,
        TRACKS["asset"],
        _geom(0, 0, 1080, 1920),
        status="VERIFIED", source_reel=source_reel,
        colors={"text": WHITE},
        text="New reel UI exhibit",
        items=[{"clip": ui_clip, "single_instance": True,
                "notes": "the speaker frame shrinks into the UI thumbnail "
                         "(scale-down ~0.5 s), UI holds, hard-cut exit; "
                         "single measured instance (DeSTW 14.4-16.0 s)"}],
        motion={"in": {"type": "scale_down_into_ui", "dur_s": 0.5,
                       "notes": "B&W frame scales down into the posting UI's "
                                "thumbnail (~14.4-14.9 s)"},
                "out": {"type": "hard_cut",
                        "notes": "hard cut at 16.0 s — the reel's only "
                                 "scene-threshold event (diff peak 54.6)"}},
        notes="D56 (DeSTW 4a): shrink-into-UI exhibit. Single instance — "
              "flagged until a second example appears.")]


# ---------------------------------------------------------------- registry
DEVICE_REGISTRY = {
    "D1": {"name": "speech caption stream", "fn": d1_captions, "status": "VERIFIED"},
    "D2": {"name": "headline lockup", "fn": d2_headline_lockup, "status": "VERIFIED"},
    "D3": {"name": "title stack + pill", "fn": d3_title_stack, "status": "VERIFIED"},
    "D4": {"name": "filter board", "fn": d4_filter_board, "status": "VERIFIED"},
    "D5": {"name": "chapter card", "fn": d5_chapter_card, "status": "[EST]"},
    "D5-list": {"name": "numbered checklist (DfQ4)", "fn": d5_checklist, "status": "VERIFIED"},
    "D6": {"name": "chart (static + annotations)", "fn": d6_chart, "status": "VERIFIED"},
    "D7": {"name": "venn / overlap", "fn": d7_venn, "status": "VERIFIED"},
    "D8": {"name": "rewrite pair", "fn": d8_rewrite_pair, "status": "VERIFIED*"},
    "D9": {"name": "exhibit insert", "fn": d9_exhibit_insert, "status": "VERIFIED"},
    "D10": {"name": "profile/grid insert", "fn": d10_profile_insert, "status": "VERIFIED"},
    "D11": {"name": "chip cloud", "fn": d11_chip_cloud, "status": "VERIFIED"},
    "D12": {"name": "era timeline", "fn": d12_timeline, "status": "VERIFIED"},
    "D13": {"name": "workflow strip", "fn": d13_workflow_strip, "status": "[EST]"},
    "D14": {"name": "end beat", "fn": d14_end_beat, "status": "VERIFIED (Q override)"},
    "D15": {"name": "script-anatomy bar chart", "fn": d15_bar_chart, "status": "VERIFIED"},
    "D16": {"name": "branch line", "fn": d16_branch_line, "status": "VERIFIED"},
    "D17": {"name": "trust dot-grid", "fn": d17_dot_grid, "status": "VERIFIED"},
    "D18": {"name": "network loop", "fn": d18_network_loop, "status": "VERIFIED"},
    "D19": {"name": "people grid", "fn": d19_people_grid, "status": "VERIFIED"},
    "D20": {"name": "views-refresh insert", "fn": d20_views_refresh, "status": "VERIFIED"},
    "D21": {"name": "B&W beat", "fn": d21_bw_beat, "status": "VERIFIED"},
    "D22": {"name": "new-post placeholder", "fn": d22_new_post_placeholder, "status": "VERIFIED"},
    "D23": {"name": "floating head cutout", "fn": d23_floating_head, "status": "VERIFIED"},
    "D24": {"name": "funnel card", "fn": d24_funnel_card, "status": "VERIFIED"},
    "D25": {"name": "retention autopsy labels", "fn": d25_autopsy_labels, "status": "VERIFIED"},
    "D26": {"name": "dashed loop arrow", "fn": d26_dashed_loop_arrow, "status": "VERIFIED"},
    "D27": {"name": "donut split chart", "fn": d27_donut_split, "status": "VERIFIED"},
    "D28": {"name": "phone section tracker", "fn": d28_phone_section_tracker, "status": "VERIFIED"},
    "D29": {"name": "flanking dot columns", "fn": d29_dot_columns, "status": "VERIFIED"},
    "D30": {"name": "dual proof-caption columns", "fn": d30_proof_columns, "status": "VERIFIED"},
    "D31": {"name": "linear count-up, no landing", "fn": d31_linear_countup, "status": "VERIFIED"},
    "D32": {"name": "document + highlight sweep + reader", "fn": d32_document_sweep, "status": "VERIFIED"},
    "D33": {"name": "comment-screenshot example pair", "fn": d33_comment_examples, "status": "VERIFIED"},
    "D34": {"name": "thumbnail wall slide", "fn": d34_thumb_wall, "status": "VERIFIED"},
    "D35": {"name": "AI-prompt doc + chat UI", "fn": d35_prompt_ui, "status": "VERIFIED"},
    "D36": {"name": "live-example bookend", "fn": d36_live_example_bookend, "status": "VERIFIED"},
    "D37": {"name": "staggered figure pair", "fn": d37_figure_pair, "status": "VERIFIED"},
    "D38": {"name": "POV-desk hook-doc", "fn": d38_pov_desk_hook_doc, "status": "VERIFIED"},
    "D39": {"name": "subject photo insert", "fn": d39_subject_photo_insert, "status": "VERIFIED"},
    "D40": {"name": "POV scene label (pill/bar)", "fn": d40_pov_scene_label, "status": "VERIFIED"},
    "D41": {"name": "spine framework diagram", "fn": d41_spine_diagram, "status": "VERIFIED"},
    "D42": {"name": "question card + outcome fork", "fn": d42_question_fork, "status": "VERIFIED"},
    "D43": {"name": "view-count badge", "fn": d43_view_count_badge, "status": "VERIFIED"},
    "D44": {"name": "POV mini-window presentation", "fn": d44_pov_mini_window, "status": "VERIFIED"},
    "D45": {"name": "kinetic-type black card", "fn": d45_kinetic_black_card, "status": "VERIFIED"},
    "D46": {"name": "vertical split-screen (reactor left / exhibit right)", "fn": d46_vertical_split, "status": "VERIFIED"},
    "D47": {"name": "binary label pair (anchored)", "fn": d47_binary_label_pair, "status": "VERIFIED"},
    "D48": {"name": "stacked split-screen (exhibit top / reactor bottom)", "fn": d48_stacked_split, "status": "VERIFIED"},
    "D49": {"name": "red annotation outline (gold in Q's lane)", "fn": d49_annotation_outline, "status": "VERIFIED"},
    "D50": {"name": "gradient script headline", "fn": d50_gradient_script_headline, "status": "VERIFIED"},
    "D51": {"name": "player-stats T-pose card", "fn": d51_player_stats_card, "status": "VERIFIED"},
    "D52": {"name": "human/AI split card 70/30", "fn": d52_human_ai_split, "status": "VERIFIED"},
    "D53": {"name": "SMPTE colour-bars gag (single-use)", "fn": d53_smpte_gag, "status": "VERIFIED"},
    "D54": {"name": "grid-background workflow strip", "fn": d54_grid_workflow_strip, "status": "VERIFIED"},
    "D55": {"name": "numbered pill system (pre-shown row, type-in)", "fn": d55_numbered_pill_system, "status": "VERIFIED"},
    "D56": {"name": "new-reel UI exhibit (shrink-in)", "fn": d56_new_post_ui_shrink, "status": "VERIFIED (single instance)"},
}


def list_devices() -> list[dict]:
    return [{"id": k, "name": v["name"], "status": v["status"]}
            for k, v in DEVICE_REGISTRY.items()]


def validate_events(events: list[dict]) -> list[str]:
    """Validate a whole event list; returns problems (empty = clean)."""
    problems = []
    for ev in events:
        problems.extend(validate_event(ev))
    # Variety rule: each device <= 2 INSTANCES per video (SKILL.md §0).
    # A board + its rows is one instance; D1 captions are exempt.
    instances: dict[str, set] = {}
    for ev in events:
        if ev["device"] == "D1":
            continue
        instances.setdefault(ev["device"], set()).add(ev.get("instance", ev["t0"]))
    for dev, insts in sorted(instances.items()):
        if len(insts) > 2:
            problems.append(f"variety rule: {dev} used {len(insts)}x in one video (max 2 instances)")
    return problems


# ------------------------------------------------- premium purge (SKY v6)
# BANNED TELLTALES — anything that reads "Claude edited this" fails a
# premium plan. Mirrors SKILL.md / STYLE-GRAMMAR.md (Batch 36 premium purge;
# synthesis/ASSET-LAYER-REFINEMENT.md: the ban is on CHEAP GRADE, not AI).
BANNED_FONT_MARKERS = ("serif", "times new roman", "georgia", "playfair",
                       "courier", "comic sans")
# Measured exceptions are NOT in this list: D2's 5-frame hook fade-out and
# D31's 10-frame count-up fade (type "fade"), D9/D34 motion-blur slides,
# D54's measured slide_horizontal and D55's measured blurred_slide handoff.
BANNED_MOTION_TYPES = {"slide_up", "slide_left", "slide_down", "scale_fade",
                       "fade_together", "slide_blur_out", "serif_blur_in",
                       "vertical_smear_drop", "pop_in", "template_title_card",
                       "static_stamp", "sticker", "tilted_sticker", "idle_float"}
BANNED_TREATMENT_MARKERS = ("template title card", "static stamp",
                            "tilted sticker", "cheap ai", "cheap template")
CHEAP_ASSET_MARKERS = ("placeholder", "dummy", "lorem", "stock", "cheap",
                       "low-res", "low_res", "watermark", "generic template",
                       "preset template")
ALLOWED_PROVENANCE_PREFIXES = ("real", "ai_premium", "higgsfield", "fable_motion")
# Evidence-bearing devices: proof stays REAL — AI provenance never allowed.
EVIDENCE_DEVICES = {"D9", "D10", "D20", "D30", "D33", "D39", "D43", "D56"}
ASSET_KEYS = {"src", "clip", "clip_path", "photo", "photo_path", "screen",
              "screen_path", "asset", "thumbnail", "image", "video"}


def _walk(obj, key=None):
    """Yield (key, string) for every string value in a nested structure."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from _walk(v, k)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            yield from _walk(v, key)
    elif isinstance(obj, str):
        yield key, obj


def validate_premium_plan(events: list[dict]) -> list[str]:
    """SKY v6 premium gate — stricter than validate_events().

    Rejects: (a) unknown/unregistered devices and removed-fallback events
    (option == 2); (b) banned fonts / motion treatments / telltale
    treatments, cheap-grade asset markers, disallowed provenance, and AI
    provenance on evidence-bearing devices; (c) events whose device spec
    requires a Sky source citation but carry none (empty / UNSET), and
    [EST]-quarantined devices (D5 chapter card, D13 — SKY-PLUS: estimates
    are quarantined rather than shipped as 'Sky'). D14 is exempt from the
    citation rule: it is a Q override, and its override text IS its source.
    Free-text notes are not scanned (measured records legitimately NAME
    the banned things they refuse).
    """
    problems = list(validate_events(events))
    for ev in events:
        dev = ev.get("device", "?")
        if ev.get("option") == 2:
            problems.append(f"{dev}: removed generic-fallback event (option=2) "
                            "in a premium plan — premium Sky is the only mode (v6)")
        reg = DEVICE_REGISTRY.get(dev)
        if reg and "[EST]" in reg["status"]:
            problems.append(f"{dev}: [EST] device quarantined in v6 — no "
                            "frame-measured Sky instance at build grade; use "
                            "the measured variant (e.g. D5-list) or measure it")
        if dev != "D14":
            src = str(ev.get("source_reel") or "")
            if not src.strip() or src.startswith(("UNSET", "Option 2")):
                problems.append(f"{dev}: no Sky source citation — every "
                                "premium event must cite its measured Sky reel")
        for key, val in _walk({k: v for k, v in ev.items() if k != "notes"}):
            low = val.lower()
            if key in ("font", "font_family", "typeface") and \
                    any(m in low for m in BANNED_FONT_MARKERS):
                problems.append(f"{dev}: banned font/treatment {val!r} "
                                "(cheap/serif telltale)")
            if key in ASSET_KEYS and any(m in low for m in CHEAP_ASSET_MARKERS):
                problems.append(f"{dev}: cheap-grade asset marker in "
                                f"{key}={val!r} (banned telltale)")
            if key in ("text", "name") and any(m in low for m in BANNED_TREATMENT_MARKERS):
                problems.append(f"{dev}: banned treatment {val!r} (telltale)")
        for key, val in _walk(ev.get("items") or []):
            if key == "provenance":
                prov = val.lower()
                if not prov.startswith(ALLOWED_PROVENANCE_PREFIXES):
                    problems.append(f"{dev}: provenance {val!r} not allowed "
                                    "(real_* / ai_premium / higgsfield / fable_motion)")
                elif dev in EVIDENCE_DEVICES and not prov.startswith("real"):
                    problems.append(f"{dev}: proof device may NEVER carry AI "
                                    f"provenance ({val!r}) — evidence stays real")
        motion = ev.get("motion") or {}
        for side in ("in", "out"):
            mtype = (motion.get(side) or {}).get("type")
            if mtype in BANNED_MOTION_TYPES:
                problems.append(f"{dev}: banned motion treatment "
                                f"{side}={mtype} (telltale — no measured Sky instance)")
    return problems


# ------------------------------------------------------- beat lock (v6)
def _word_onsets(words) -> list[float]:
    onsets = []
    for w in words or []:
        t = w.get("start", w.get("s"))
        if t is not None:
            onsets.append(float(t))
    return sorted(onsets)


def beat_lock_report(events: list[dict], words, tol: float = 1 / 30) -> dict:
    """Beat-lock report (BEAT-LOCK-SPEC.md): every planned event's t0 must
    sit within tol (default 1 frame ≈ 0.033 s) of the take's beat grid —
    word onsets from the take's own timings — unless the event carries an
    off_beat_reason. D1 caption events are the grid itself and are counted
    as on-beat by construction. Timed exits are checked only for events
    flagged exit_on_beat=True (most Sky exits are holds, not beats)."""
    onsets = _word_onsets(words)
    rows, on = [], 0
    for ev in events:
        if ev.get("device") == "D1":
            on += 1
            continue
        checks = [("t0", ev["t0"])]
        if ev.get("exit_on_beat"):
            checks.append(("t1", ev["t1"]))
        bad = []
        for label, t in checks:
            d = min((abs(t - o) for o in onsets), default=None)
            if d is None or d > tol:
                bad.append(f"{label}={t} off grid by "
                           f"{'n/a' if d is None else round(d, 3)}s")
        if bad and not ev.get("off_beat_reason"):
            rows.append({"device": ev.get("device"), "t0": ev.get("t0"),
                         "problems": bad})
        else:
            on += 1
    total = len(events)
    return {"total": total, "on_beat": on,
            "pct": round(100.0 * on / total, 1) if total else 100.0,
            "offenders": rows, "tol_s": tol}


def validate_beat_lock(events: list[dict], words, tol: float = 1 / 30) -> list[str]:
    """Beat-lock failures (empty = locked). See beat_lock_report()."""
    rep = beat_lock_report(events, words, tol=tol)
    return [f"beat-lock: {r['device']}@{r['t0']} — " + "; ".join(r["problems"])
            + " (no off_beat_reason)"
            for r in rep["offenders"]]


if __name__ == "__main__":
    print(f"{len(DEVICE_REGISTRY)} devices registered (D1-D56 + D5-list variant)")
    for d in list_devices():
        print(f"  {d['id']:8s} {d['name']:32s} {d['status']}")
    # Smoke: one event per device with dummy timings, all must validate.
    import inspect
    problems = []
    smoke = []
    smoke += d1_captions([{"word": "Test", "start": 0.0, "end": 0.4},
                          {"word": "caption", "start": 0.4, "end": 0.9}])
    smoke += d2_headline_lockup(0.0, kicker="the", display_lines=["TEST", "FRAMEWORK"])
    smoke += d3_title_stack(0.0, title="Test", sections=["One", "Two"])
    smoke += d4_filter_board(0.0, board_title="Board",
                             rows=[{"label": "A", "verdict": "approve"},
                                   {"label": "B", "verdict": "reject"},
                                   {"label": "C", "verdict": "minimum"}])
    smoke += d5_chapter_card(0.0, numeral=1, name="One", definition="First.")
    smoke += d5_checklist(0.0, title="3 Types", items=["A", "B", "C"])
    smoke += d6_chart(0.0, title="Views", annotations=[{"label": "Push", "value": "1.1M"}])
    smoke += d7_venn(0.0, left_label="Yours", right_label="Theirs", figure="2.6M")
    smoke += d8_rewrite_pair(0.0, before="old line", after="new line",
                             swapped_old="old", swapped_new="new")
    smoke += d9_exhibit_insert(0.0, label="Exhibit", clip_path="clip.mp4", duration_s=5.0)
    smoke += d10_profile_insert(0.0, label="Profile", screen_path="screen.mp4")
    smoke += d11_chip_cloud(0.0, words_list=["Legit", "Warm"])
    smoke += d12_timeline(0.0, nodes=[{"label": "2025"}, {"label": "2026", "current": True}])
    smoke += d13_workflow_strip(0.0, steps=["A", "B"])
    smoke += d14_end_beat(50.0, close_line="Comment WAITLIST")
    smoke += d15_bar_chart(0.0, rows=[{"label": "Hook", "kind": "hook", "width_frac": 0.3}])
    smoke += d16_branch_line(0.0, label="branch")
    smoke += d17_dot_grid(0.0, categories=["Community", "Course"])
    smoke += d18_network_loop(0.0, profiles=["a", "b"])
    smoke += d19_people_grid(0.0, count_label="100s of people")
    smoke += d20_views_refresh(0.0, view_counts=[8547, 4246, 6540])
    smoke += d21_bw_beat(0.0, hero_word="DON'T")
    smoke += d22_new_post_placeholder(0.0)
    smoke += d23_floating_head(0.0)
    smoke += d24_funnel_card(0.0, rows=["CONTENT -> CHECKOUT"], checklist=["01 GOAL"])
    smoke += d25_autopsy_labels(0.0, labels=["Hook filtering ✓"])
    # Batch 18 (Dcc84V5jc6D) — D26-D37 smoke with the reel's own timings.
    smoke += d2_hook_build(0.0, steps=[
        {"word": "I guarantee", "t": 0.0, "size_px": 55, "role": "small"},
        {"word": "aren't", "t": 0.88, "size_px": 110, "role": "large"},
        {"word": "CAPTION MAXING", "t": 1.14, "size_px": 130, "role": "accent"},
        {"word": "enough", "t": 1.88, "size_px": 55, "role": "small"}])
    smoke += d26_dashed_loop_arrow(5.6, t1=8.8, headline_t0=5.6)
    smoke += d27_donut_split(10.87, headline_number="149,095", t1=19.5, states=[
        {"t": 10.87, "followers_pct": 50.30, "nonfollowers_pct": 49.70},
        {"t": 15.5, "followers_pct": 58.51, "nonfollowers_pct": 41.57},
        {"t": 16.5, "followers_pct": 92.70, "nonfollowers_pct": 7.70}])
    smoke += d28_phone_section_tracker(8.8, t1=19.5, clip_path="reel.mp4", sections=[
        ("HOOK", 9.0), ("LEAD", 10.0), ("BODY1", 14.0), ("OPEN LOOPS", 17.0)])
    smoke += d29_dot_columns(10.9, t1=19.5)
    smoke += d30_proof_columns(38.4, t1=43.0,
                               left={"handle": "wellcopymax", "caption": "10/10 marketing emails you should steal…", "ring": True},
                               right={"handle": "shelby.sapp", "caption": "three days of women & wealthhh…", "ring": False})
    smoke += d31_linear_countup(6.92, label="more leads")
    _doc = ("1. CASUAL INTRO + THE OBSESSION\n2. THE RECEIPTS\n"
            "3. THE FAILED EXPERIMENTS\n4. THE REVEAL\n5. WHAT YOU DO NOW\n"
            "6. STILL HUMAN\n7. THE ASK")
    smoke += d32_document_sweep(20.0, document_text=_doc, t1=38.2, beats=[
        {"label": "1. CASUAL INTRO + THE OBSESSION", "text": "1. CASUAL INTRO + THE OBSESSION", "t0": 26.5},
        {"label": "2. THE RECEIPTS", "text": "2. THE RECEIPTS", "t0": 27.9}])
    smoke += d33_comment_examples(3.8, t1=5.5,
                                  left_shot={"text": "Comment \"notion\" to join the waitlist", "handle": "realskytan", "timestamp": "Edited · 66w"},
                                  right_shot={"text": "Create content for your avatar!", "handle": "realskytan", "timestamp": "60w"})
    smoke += d34_thumb_wall(21.8, t1=25.8, thumbnails=[
        {"src": f"thumb{i}.mp4", "caption": f"Reel {i}"} for i in range(1, 7)])
    smoke += d35_prompt_ui(44.0, t1=51.5,
                           prompt_text="I want you to write me a video caption using the personal story template I gave you.",
                           formula_chain="Intro → Before/Story → Results → After/Reveal → What I Post/Do → Still Human → CTA")
    smoke += d36_live_example_bookend(49.8, t1=52.0, keyword="Prompt",
                                      document_text=_doc, source_document=_doc)
    smoke += d37_figure_pair(40.97, caption="figures a month", figures=[
        ("$700K/m", 40.97, 60, 1030), ("$2–4M/m", 41.47, 700, 1030)])
    # Batch 19 (33 NEW reels #17-49) — D38-D54 smoke with the reels' own timings.
    smoke += d38_pov_desk_hook_doc(0.0, headline="If I was writing hooks for Mel Robbins, this is how I would NOT write them.",
                                   t1=70.61, items=[
                                       {"text": "5 tips to become more confident.", "t": 0.0},
                                       {"text": "why you care so much about what other people think", "t": 4.0},
                                       {"text": "4 habits that make it psychologically impossible to care about what other people think", "t": 26.0},
                                       {"text": "…if you're a people pleaser", "t": 57.0}],
                                   camera_moves=[{"kind": "push_in", "t": 0.0},
                                                 {"kind": "profile_swing", "t": 28.0}])
    smoke += d39_subject_photo_insert(1.5, photo_path="mel_robbins.jpg", subject="Mel Robbins",
                                      duration_s=2.0, size="half_body")
    smoke += d40_pov_scene_label(0.0, text="POV: Giving feedback to your strategists",
                                 geometry="pill", t1=9.0)
    smoke += d40_pov_scene_label(0.0, text="POV: You're Autistic about Content",
                                 geometry="bar", t1=51.24, source_reel="DeIkaFAlMQO")
    smoke += d41_spine_diagram(4.0, t1=63.34, close_arrow_t=60.0,
                               vertebrae=["Goal", "Person", "Avatar", "Gap", "Offer",
                                          "Funnel", "Content Pillars", "Formats",
                                          "Brand & Positioning"],
                               zooms=[{"label": "Goal", "t0": 13.62, "detail": "hire or leads?"},
                                      {"label": "Funnel", "t0": 32.82, "detail": "where does traffic point?"},
                                      {"label": "Brand & Positioning", "t0": 54.86, "detail": "what do you want to be known for?"}])
    smoke += d42_question_fork(66.5, header="THE 1 LEADERSHIP QUESTION",
                               question="When you took over your last team, what was the first thing you changed, and why?",
                               outcomes=[("OUTCOME A", "Lead a department", 70.0, "left"),
                                         ("OUTCOME B", "Create more work", 72.5, "right")])
    smoke += d43_view_count_badge(21.0, count="1.5M", t1=28.0)
    smoke += d44_pov_mini_window(0.0, t1=9.34,
                                 pov_lines=["POV:", "you're getting rinsed 5.5k/month",
                                            "for a vancouver shit hole but it's chill"],
                                 shots=[("apartment tour", 0.0), ("desk setup", 3.0), ("downtown view", 6.0)])
    smoke += d45_kinetic_black_card(12.0, hold_s=2.0,
                                    lines=[{"text": "YOU SHOULD MAKE", "role": "small", "color": "white"},
                                           {"text": "SALES", "role": "huge", "color": "gold"},
                                           {"text": "TO GET", "role": "small", "color": "white"},
                                           {"text": "CUSTOMERS", "role": "huge", "color": "gold"}])
    smoke += d46_vertical_split(0.0, t1=80.17, exhibit_clip="closet_reveal.mp4",
                                verdict_t=42.0, replay_t=30.0, view_badge="👁 26.9M")
    smoke += d47_binary_label_pair(26.0, winner="Idea", winner_t=31.0,
                                   labels=[("Idea", "right ceiling light", 26.0, 645, 90),
                                           ("Strategy", "left ceiling light", 26.5, 345, 90)])
    smoke += d48_stacked_split(0.0, t1=93.67, divider_frac=0.47,
                               exhibit={"clip_path": "hank_profile_scroll.mp4",
                                        "kind": "desktop_profile_scroll",
                                        "segments": [("profile grid", 0.0),
                                                     ("profile header", 3.0),
                                                     ("post + comments rail", 21.0),
                                                     ("grid again", 54.0)]})
    smoke += d49_annotation_outline(13.0, shape="ellipse", target="profile header bio",
                                    duration_s=1.0)
    smoke += d50_gradient_script_headline(17.0, text="THEY BUILD Relationships",
                                          hold_s=2.0, position="chest")
    smoke += d51_player_stats_card(24.1, name="WARREN", t1=30.9, location="doorway",
                                   stats=[("9'11\"", 24.3), ("420 POUNDS", 25.8),
                                          ("0 NOTION SKILLS", 26.2), ("42 CODING", 28.0)])
    smoke += d52_human_ai_split(36.0, headline="Perfect Split", t1=42.29,
                                actors=[("70% YOU", "head_cutout", 37.1),
                                        ("30% AI", "logo", 38.4)])
    smoke += d53_smpte_gag(30.0, clip_path="bars_B_D.mp4", caption="SHOW PROOF")
    smoke += d54_grid_workflow_strip(18.0, t1=29.0,
                                     steps=[{"icon": "head_cutout", "label": "SO FIRST",
                                             "sublabel": "GIVE THE CONTEXT", "t0": 19.0},
                                            {"icon": "chatgpt_logo", "label": "AI TO SYNTHESIZE",
                                             "sublabel": "SYNTHESIZE THOUGHTS", "t0": 22.0},
                                            {"icon": "structure", "label": "CREATE A STRUCTURE OF THE VIDEO",
                                             "sublabel": "IN THE OVERALL DNA OF THE VIDEO", "t0": 26.0}])
    smoke += d55_numbered_pill_system(44.4, pills=[
        {"number": 1, "text": "She never said she was the expert",
         "chip_alone_t": 45.4, "text_t0": 45.9, "text_t1": 46.8},
        {"number": 2, "text": "She made it feel like a shared challenge",
         "chip_alone_t": 51.0, "text_t0": 51.5, "text_t1": 52.2},
        {"number": 3, "text": "She openly shared her income",
         "chip_alone_t": 57.1, "text_t0": 57.9, "text_t1": 58.2},
        {"number": 4, "text": "She accidentally created an affiliate army",
         "chip_alone_t": 66.2, "text_t0": 67.3, "text_t1": 68.1}])
    smoke += d56_new_post_ui_shrink(14.4, ui_clip="new_reel_ui.mp4", duration_s=1.6)
    problems = validate_events(smoke)
    print(f"smoke events: {len(smoke)}")
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print("  -", p)
        raise SystemExit(1)
    print("devices OK — all events validate, no forbidden colours")

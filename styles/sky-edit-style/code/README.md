# code/ — Sky style as executable code (Claude Code)

The style is not prose alone: every device (D1–D56), motion law, caption
behavior, color, sound, and pacing rule in `STYLE-GRAMMAR.md` has code here
that produces it. All files are **stdlib Python only** — no installs.

## The pipeline (what runs, in order)

```
words.json (word-level transcript: word / start / end)
  → sky_build_plan.py        plan v2 JSON (caption groups, events, layout, QC list)
  → sky_qc.py                plan gates P1–P8 (+ export gates E1/E2 on a render)
  → sky_hyperframes.py       HyperFrames project (index.html + compositions/)
  → npx hyperframes lint && npx hyperframes check
  → npx hyperframes render   MP4 (1080×1920, 30 fps)
  → sky_capcut_draft.py      CapCut MCP tool-call sequence (the SHIPPING path)
```

## Render-path decision (Nov 9, 2026 — verified by an actual render)

1. **HyperFrames = PRIMARY executable render path in Claude Code.**
   Deterministic HTML → video, GSAP timelines, frame-exact. Sky's motion
   (hard cuts + eased panel/line draws + static charts with stacking
   annotations) is fully expressible in HTML/CSS/GSAP. **Verified Nov 9:**
   a 9.0 s test plan (fixture words, D4 hero, green family) rendered to a
   real 1080×1920 30 fps H.264 MP4; `hyperframes check` overall **ok=True**
   (layout/motion/contrast/runtime all ok); frame grabs confirm the board
   filling row by row, the D2 headline, captions swapping on time, and the
   D14 end card. The orange/D12-hero variant also passes plan QC + `check`.
2. **CapCut-native = SHIPPING bar for Q's main edits.** `sky_capcut_draft.py`
   emits the MCP tool-call sequence; export must come from CapCut Desktop.
   No fabricated `draft_content.json` — pyJianYingDraft targets JianYing
   (China build), not CapCut International, and is not installed.
3. **ffmpeg = QC + measurement only.** Numpy gl-transition ports
   (WhipTilt/PopIn) are NOT applied — Sky's verified motion has no whip
   smears; applying them would be un-Sky.
4. `/reverse-any-video` (HyperFrames Pro) is gated — noted only, never chased.
5. **Limits.** A-roll must be supplied (`assets/aroll.mp4`); without it,
   graphics render over the navy ground for a graphics-only grade. Face
   tracking / RVM matte is a pre-render step (the old `matte.py` engine is
   gone — GAPS.md G-10). The E2 freezedetect gate assumes A-roll footage is
   present: on a graphics-only render it flags the static spans between
   device events, because a caption swap changes only ~0.3% of pixels
   (verified Nov 9 — the frames prove the captions swap on time; the gate
   is not weakened, it is not applicable without footage).

## Files

| File | What it executes |
|---|---|
| `sky_palette.py` | PWC palette (single source of truth): teal `#14A886`, gold `#FEE238`, navy `#00214E`. Sky→PWC remap table; `validate_color` / `is_forbidden` block red-dominant and neon-green hexes; footage is exempt (`is_footage=True`). |
| `sky_easing.py` | Easing functions: `step` (hard cut = caption-in), `linear`, `ease_out_cubic`, `power4.out`, `expo.out`, `ease_in_out_quad`, `back.out`, `back.out_1.141` (overshoot param 2.08, solved numerically), closed-form `spring` (damping 0.8). `keyframes()` samples any easing into `[{t_s, value}]`. Constants: caption-in ≤1 frame, caption-out 0.5 s, panel in/out 7f (0.233 s), child builds 6f, min stagger 3f, pop 0.3 s, count-up 1.0 s. |
| `sky_devices.py` | Device registry D1–D56 + D5-list = 57 entries (SKY v6: + D55 numbered pill system, D56 UI exhibit shrink; TICK_TONE_SPEC sound annotations on D6/D20/D27/D31/D37; `validate_premium_plan` + `validate_beat_lock`/`beat_lock_report`). Each device is a function returning timeline EVENT dicts: `{device, name, t0, t1, track, geometry (1080×1920 px, top-left), colors, text, items, motion {in/out with easing + keyframes}, sfx, status, source_reel, instance}`. `validate_events()` checks canvas bounds, top UI zone, forbidden colors, and the variety rule (each device ≤2 instances per video, D1 exempt; a board + its rows = one instance via shared `instance` id). |
| `sky_build_plan.py` | Plan v2 generator (supersedes `sky_plan_template.py`, kept intact). CLI: `words.json --framework --parts "A,B,C" (3–6) --family green\|orange --keyword --model-reel --hero D4\|D5\|D5-list\|D6\|D12\|D13 --devices JSON --hook-formula --aroll --face-box --out`. Emits caption groups, full event list, punch-ins (1.08×, capped 105–110%), mid-video reset @50%, hook rule (framework headline within first 10% of runtime), close (end moment ≤1 s after last word), sound plan (voice −14.5 LUFS, bed −28 dB, cleared library only), QC checklist, and a `layout` block (`hairline_y`, `chin_y`, `caption_y` = chin+69, `headline_y` = caption-bottom+12, `hero_top_y`, D3 status). Layout rule: D3 title stack is present ONLY for heroes D5/D6/D13 AND when the hero body (≥260 px) fits below the pill; D4/D5-list/D12 heroes carry their own titles. Hero is ONE instance spanning the video, filling part by part. |
| `sky_hyperframes.py` | Plan JSON → HyperFrames project (`index.html` + `compositions/sky.html` devices + `compositions/captions.html` D1 stream). Contract: outer `.clip` div carries timing only and is NEVER touched by GSAP; all styling/animation lives on an INNER div (`-in` suffix) using `opacity` (never `autoAlpha`); captions hard-cut via `tl.set(inner, {opacity:1}, t0)` and out-fade clamped to 60% of the group's life; D21 B&W beat = full-frame `backdrop-filter: grayscale(1)` + gold hero word; GSAP 3.15.0 (framework-whitelisted CDN, inlined by the compiler). Scene roots are TRANSPARENT — the navy ground lives on the main root only (an opaque scene root paints over sibling scenes; verified Nov 9). `validate_project()` checks clips, paused GSAP timelines, determinism tokens, allowlisted URLs. |
| `sky_capcut_draft.py` | Plan JSON → ordered CapCut MCP tool-call sequence (`capcut_create_project`, `capcut_add_video_clip` Track 0, `capcut_add_subtitles` with SRT payload built from D1 groups, `capcut_add_text` per device label, `capcut_add_keyframe` for pops/opacity/punch-ins, `capcut_add_audio_clip` bed −28 dB, `capcut_add_sound_effect` per landing, `capcut_generate_preview`). Coordinates converted px→normalized (x∈[−1,1], y∈[−1,1] bottom-to-top). Explicitly NOT a `draft_content.json`. `validate_sequence()` checks per-call ranges, coords, palette. |
| `sky_qc.py` | Plan gates P1–P8 (palette, captions 1–3 words, variety+geometry, nothing over face box, no-overlap @0.1 s sampling — including D1×D2/D3 pairs, D21/D14 exempt as overlays — text handoff ≥0.5 s, hook ≤10%, close ≤1 s, sound plan) + export gates E1 (ffprobe) / E2 (freezedetect n=0.003 d=0.35, zero freezes ≥0.35 s). Exit 0/1/2. `--face-box` override; `--json` output. |
| ~~`sky_option2.py`~~ | **DELETED — SKY v6 premium purge (Batch 36).** The generic-fallback patterns module is gone; premium Sky is the only output mode and `validate_premium_plan` rejects fallback-marked events, banned fonts/motions and cheap-grade assets. Row kept as a tombstone so old references resolve. |
| `sky_plan_template.py` | The original v1 plan generator. Kept intact for reference; `sky_build_plan.py` supersedes it. |
| `capcut_build_spec.md` | Device-by-device CapCut draft instructions (D1–D14 + carousel slides): exact track layout, native text/shapes/masks/keyframes, values from `STYLE-GRAMMAR.md`. Build each device ONCE as a reusable CapCut draft template, duplicate per episode. **CapCut-native — this is the shipping build.** |
| `plan_example.json` | Example plan output (fictional framework, placeholder numbers marked [Q TO FILL]) showing the plan shape. Example only. |
| `qc_freezedetect.sh` | Runs ffmpeg `freezedetect` (noise 0.003, duration 0.35) + ffprobe duration/stream check on an EXPORTED file. QC only — it builds nothing. |
| `tests/test_sky_code.py` + `tests/fixtures/words_small.json` | 88 stdlib `unittest` tests (palette, easing, devices registry/completeness D1–D56, caption cadence, D4 verdict remap, D6 static base, D12 mechanics, D17 remap, plan v2 shape/validation/rejections, hero variants, D3 omission rule, D2/caption clearance, dict-text rendering, transparent scene roots, HyperFrames build/validate/no-forbidden-tokens/hard-cut caption, CapCut sequence/coords, QC pass/fail incl. P9/P10 v6 gates, anti-slop Batch 19 locks, premium-v6 locks: fallback module absent, D55/D56 mechanics, tick-tone spec, validator rejections, beat lock). Run: `python3 -m unittest discover -s code/tests` (from the skill folder). |

## How to run a test edit (the first graded edit)

```bash
# 1. Plan from a real Q take's words JSON (word / start / end, 30 fps source)
python3 code/sky_build_plan.py words.json --framework "The Filter" \
  --parts "Hook,Filter 1,Filter 2,Payoff" --family green --keyword WAITLIST \
  --model-reel DfX2qwQGagM --hero D4 --aroll assets/aroll.mp4 --out plan.json
# 2. Plan QC (must PASS)
python3 code/sky_qc.py plan.json
# 3. HyperFrames project + lint + check (overall must be ok)
python3 code/sky_hyperframes.py plan.json --out hf_project --check-only
cd hf_project && npx hyperframes lint && npx hyperframes check
# 4. Render (needs disk headroom outside /tmp — /tmp is a 512 MB tmpfs)
npx hyperframes render -o render.mp4 -f 30
# 5. Export QC on the render (E2 needs A-roll present; see Limits above)
python3 code/sky_qc.py plan.json --export render.mp4
# 6. CapCut sequence for the shipping build
python3 code/sky_capcut_draft.py plan.json
# 7. Grade the export against the named model reel per QC.md §1–6
#    (frame sequence, ±0.15 s entrance/exit audits, last-word→end-card ≤1 s,
#    per-word fit, full self-watch) — until that grade passes, NOT YET GRADED.
```

## What is NOT here (see `GAPS.md` G-10)
- There is **no CapCut-native draft file** (.capcut / draft template) bundled —
  none exists on disk for Sky devices. Build them from `capcut_build_spec.md`
  and save them as reusable drafts; their names go in the delivery report
  (`QC.md` §7). `sky_capcut_draft.py` emits the build sequence; the export
  still happens in CapCut Desktop.
- No working ffmpeg plate renderer is claimed as the edit. The HyperFrames
  path above IS a working renderer (verified Nov 9), and it is the primary
  executable path in Claude Code — but a HyperFrames render is not a CapCut
  export, and Q's shipping bar for main edits stays CapCut-native.

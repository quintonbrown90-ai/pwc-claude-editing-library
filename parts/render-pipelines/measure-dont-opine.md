<!-- PART: render-pipelines/measure-dont-opine.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# RENDER-PIPELINES — make it measure, not opine: style is a set of numbers (Mr omi, Tier S)

Source: Mr omi — "How to Make Viral Animated Shorts Using Claude"
(https://www.youtube.com/watch?v=OtbLL6OBNE4) + "How to Make Ultra-Realistic
3D Animated Shorts Using Claude" (https://www.youtube.com/watch?v=_fIoJ_ywGfY).
INFERRED reconstruction from the visible method; no files downloaded.
Knowledge entries V8-55, V8-57, V8-58, V8-59, V8-94, V8-95, V8-96, V8-97,
V8-98, V8-99, V8-101, V8-152. This is the corrective to every "Claude
eyeballed it" failure in the library.

## The rule
Don't ask Claude what it thinks. Make it measure. You can't recreate an
opinion, you can recreate a number. A style is a set of numbers, not an
impression — and the delta between your numbers and the reference numbers is
your to-do list.

## Executable steps
1. **Contact sheets (60 frames/image, every 2s) + phase-correlation camera
   tracking + brightness / contrast / saturation measurement.** The three
   measurements that turn a style into numbers. Still-frame check before
   rendering any video.
2. **Watch at 30fps.** Micro-animations, camera moves, shading, light — the
   tiny stuff is what makes it feel real, and it's only visible frame by
   frame.
3. **Close the loop: run your own render through the same pipeline.** "Don't
   just measure the reference. Run your own render through the same
   pipeline. The delta is your to-do list." The 9-second test exists to
   produce the delta.
4. **Camera is the whole trick: one continuous shot, zero cuts.** Dolly in /
   hold / slow creep / eased pull out; zero lateral motion, no pan.
   Transitions are motion transitions (whip pans, zoom-throughs) — hard cuts
   only ~1 in 7. The camera travels; it never jumps.
5. **Jerk as a measured quantity.** First version had 8× more jerk than the
   reference; lock the camera to a single dolly axis, ease every move,
   measure again — jerk dropped by half, drift gone. Camera smoothness is a
   number, not a feeling.
6. **Separate judge agent scores stills after every fix (7/10 → 7.5 → 8.5 →
   ready to render).** The judge is a different agent from the builder, and
   the score is the gate. The judge needs a rubric; the score is the verdict.
7. **"If a real one exists, download it. Never build it by hand."** Real
   scans, real photos, NASA imagery, real field diagrams, scanned facade
   kits. The real-asset law — same as Q's "real footage over flat plates"
   and "no generic stock/AI photos".
8. **5-second test first.** Prove the look on a 5-second test before building
   the full video. Render small, then upscale. Still frames before video
   render.
9. **Gap-analysis agent team (7 study + 4 rebuild; split FILES, not just
   jobs).** One agent per dimension measuring original vs ours side by side
   ("no guessing, real numbers"); rebuild agents each own their file.
10. **Reanimate (the copy method).** Record the original one frame at a time
    (when each part starts, how fast it moves), build your copy, record it
    the same way, compare side by side, fix whatever's furthest off until
    they match (2–5 rounds). Default: movement only, look stays yours; exact
    match copies the look too. Report what can't be matched and why.
11. **"Our renders were too perfect. Real cameras aren't perfect."** Add the
    imperfection back — a little shake, a little drift, a little grain in the
    right place — or the render reads as CGI. (Grain here is measured
    imperfection, not the "no grain" slop rule: the amount is a number, set
    on purpose.)

## Worked example (PWC)
Q's Sky-style rebuild: contact sheet of Sky's reel every 2s → measure
brightness/contrast/saturation + camera path → build Q's version → measure
Q's render the same way → delta list (jerk 8×, one plate 2 frames late) →
fix furthest-off first → judge agent scores the stills (7 → 8.5) → render.
Keyword WAITLIST.

## Human-made check
Numbers are the check, taste is the verdict: the judge's score gates the
render, and Muse still watches the whole video before it reaches Q. A
passing score never ships a video Muse hasn't watched.

## PWC skin
Teal #14A886 + gold #FEE238 on navy #00214E. NO RED. Measurement sheets and
judge rubrics carry the PWC palette; reference measurements are recorded as
numbers, never as vibes.

## Variants (v9)
- **v9 · @?, V8-176:** V8-176 — Design-system sources: styles.refero.design, skillry.dev, watchips.com; FFmpeg-screenshot contact sheet (uaVYHiF8f7k, Jay E RoboNuggets) → find-skills-discovery-layer.md (+ FFmpeg contact sheet → D9) _(source: v9_verification.md)_

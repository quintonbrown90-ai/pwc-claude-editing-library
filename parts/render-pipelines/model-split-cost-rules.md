<!-- PART: render-pipelines/model-split-cost-rules.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# RENDER-PIPELINES — model split + cost rules: Opus plans, Sonnet builds, low effort is enough (Sandy Lee AI / Jay E RoboNuggets, Tier S)

Source: Sandy Lee AI — "How I Fully Automated Video Editing (Claude Code)"
(https://www.youtube.com/watch?v=vI4RdXMSq8c) + Jay E RoboNuggets — "Turn
Claude Into a Video Editing GENIUS (in 3 simple steps)"
(https://www.youtube.com/watch?v=uaVYHiF8f7k) + Grow With Kaz — "I Made Viral
NEW AI Animation Videos Using ONLY Claude (FREE Plugin)"
(https://www.youtube.com/watch?v=Yj5LpSq_7xI). INFERRED reconstruction from
the visible rules; no files downloaded. Knowledge entries V8-29, V8-92,
V8-93, V8-169, V8-170, V8-172, V8-174. Corroborated by V8-52 (Opus thinks,
Sonnet builds). Model names are time-stamped Nov 2026 — re-check current
equivalents before citing them in a skill.

## The rule
Tokens, not credits: the subscription is the cost. Top-tier model only for
high-ROI work; the workhorse model does the building; low effort is enough
for most videos. Don't burn the highest effort setting on every video.

## Executable steps
1. **Model strategy: Opus for planning/setup, Sonnet for execution.**
   "Whenever I plan [and] set things up, I use Opus. But whenever I actually
   take action, I change the model to Sonnet." Top-tier model only for
   high-ROI projects. Opus thinks (planning, creative direction); Sonnet
   builds.
2. **Sonnet 5.5 = half the cost of Opus 5.5, nearly as good at video
   animation — and code-based, so it's reusable.** Animations are JavaScript
   + HTML, isolatable per element; a dialed-in style becomes a design system,
   which becomes part of a skill. AI video-gen models are black boxes,
   hard/costly to replicate; code styles are not.
3. **Low effort is enough.** Run Claude on low effort to save usage — "still
   doing a pretty good job." The trade-offs are generation time, reliability,
   and capacity, not quality.
4. **Tokens, not credits.** Editing runs on tokens (subscription only);
   Higgsfield B-roll is $2–7/video vs an editor at $50–$3,000 per long-form
   video. Whisper (free) gives the word-level transcript FFmpeg cuts from;
   FFmpeg also cleans up + normalizes the audio.
5. **Cost model: measure tokens per video.** $27/video all-in (measured in
   the source run) — measure your own number per video and keep it in the
   skill. A cost nobody measures is a cost nobody controls.
6. **B-roll gate: ask before spending credits.** Before creating B-rolls the
   skill asks questions (Higgsfield costs credits/money — no random B-rolls);
   build a cut list, flag 4–5 word-motivated B-roll moments. No spend without
   a question first.
7. **Split the script in halves for voiceover + generation.** Two parts make
   generation easier; 1.5-min animation ≈ 10 min generation; 10-min video ≈
   1h render. Chunking is the render-time control. (Free-plan credit caveat:
   a run may exhaust credits — ~5h wait. Budget for it.)

## Worked example (PWC)
Q's week: Opus plans the week's 3 proof videos (beat tables, hooks) →
Sonnet builds each render at low effort → B-roll gate asks before any
Higgsfield spend → tokens/video logged in the skill → month-end cost model
reviewed against the $27/video benchmark. Keyword WAITLIST.

## Human-made check
The cost log is checked monthly: tokens per video, B-roll spend, and model
split are all visible. A run that burns Opus on execution gets flagged, not
shrugged at.

## PWC skin
Teal #14A886 + gold #FEE238 on navy #00214E. NO RED. Cost logs and model
rules live in the skill file, not in the video.

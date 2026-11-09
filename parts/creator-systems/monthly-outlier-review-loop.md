<!-- PART: creator-systems/monthly-outlier-review-loop.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# CREATOR-SYSTEMS — build two skills from your own channel + the monthly outlier review loop (Matt Wolfe, Tier S)

Source: Matt Wolfe — "How I Get Claude To Edit My Videos (Step-by-Step)"
(https://www.youtube.com/watch?v=ep4psgAFOqc). INFERRED reconstruction from
the visible workflow; no files downloaded. Knowledge entries V8-117, V8-118,
V8-119, V8-120. Corroborated by V8-27 (timestamped feedback → add to skill)
and V8-07 (self-improving skill).

## The rule
Your own channel is the training set. VidIQ analyzes your best performers
(script + visuals) and writes two skills: one that generates similar scripts
likely to go viral, one that edits videos to look like your existing videos.
Then, once a month, the outlier review feeds the skills again. Every future
video gets a little better — the loop is the improvement system.

## Executable steps
1. **Build two skills from your own channel (scripting + editing).**
   Analyze your best performers and write two skills: a scripting skill
   (generates similar scripts likely to perform) and an editing skill (edits
   videos to look like your existing videos). Iterate: tell it what to fix,
   update the skill, back and forth until "go edit this for me" just works.
2. **The skill-building prompt (URL in → script → record → edit to match).**
   Give a URL, write a likely-to-perform script, record A-roll, edit to look
   like existing videos (cut pauses/mistakes, B-roll, animations, subtitles,
   music, SFX). The end state is drag-the-video-in with no prompt at all.
3. **Cut with transcript AND waveform.** "Sometimes it'll read the
   transcripts think it needs to cut it off but it will accidentally cut you
   off like mid-word. So it needs to also look at the waveform to make sure
   that it's cutting after the sound ends and not when it just thinks the
   word is end." The waveform is the guard against mid-word cuts — the
   mechanism behind Q's "no word ever cut off" rule.
4. **Monthly outlier review loop (reinforcement learning for the channel).**
   Once a month: review the last 10 shorts, find the outliers, pull
   transcripts + comments + retention curves, feed the suggestions back into
   the skills. Rank by outlier multiple (views ÷ own median; over 3× is a
   signal — see strategy-outlier-multiple-swipe.md).
5. **Research first: the link is the brief.** Give the source link + your own
   B-roll link; the agent researches before it writes. No research, no
   script.

## Worked example (PWC)
Q's month: VidIQ reads Q's top 10 posted reels → scripting skill (his hooks,
his proof shapes) + editing skill (his captions, his plates, his pacing) →
"edit this" just works → end of month, last 10 shorts reviewed, outliers
found, transcripts + comments + retention fed back → both skills updated.
Keyword WAITLIST.

## Human-made check
The monthly review is a human read, not an auto-run: the outliers are
confirmed by watching, the feedback is approved before it enters the skills,
and no skill update ships without a test edit proving it.

## PWC skin
Teal #14A886 + gold #FEE238 on navy #00214E. NO RED. Skill files and review
decks carry the PWC palette; Q's own reels are the style source, never a
stranger's preset.

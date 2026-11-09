# PROMPTS — the PWC prompt library (paste-ready, attributed)

Every prompt here is distilled from material already on disk in this folder
or in a staged skill. Each entry says where it came from and what it is
(PUBLISHED = their words; INFERRED = our reconstruction, labeled as such).
Swap the {braces}; everything else is law. All prompts run under BRAND.md
(teal/gold on navy, NO RED, nothing over the face) and the BRAND-DNA
checklist — a prompt never overrides those.

## 0. THE ROUTER INTAKE — ask before you build

Paste this when the video type is ambiguous. Claude answers it, then
recommends a style (EDIT-ROUTER.md) before building.

```
Before you edit, classify this video and recommend the edit:
1. What type is it (talking-head proof / launch take / avatar explainer /
   carousel / UGC brand video / series episode / other)?
2. What is the ONE claim, in the speaker's exact words?
3. What proof object shows that claim on screen, and at what second?
4. Who is the audience (creators under 10K / buyers / waitlisters)?
5. Which lane (main launch / avatar / proof-led / carousel / trial)?
6. What is the comment keyword, and is its ManyChat flow live?
7. Is there a real screen, screenshot, or photo to show — or only talk?
8. What is the hook in the first 2 seconds, and is Q's face on screen?
9. What should the viewer DO at the end (keyword + bio-line CTA)?
10. What must NOT appear (hidden app name? brand names? faces to blur)?
Answer with the RECOMMENDATION shape in EDIT-ROUTER.md §6: style pick +
three grounds (capability / creator system / viral evidence) + build plan +
QC gates + the BRAND-DNA checklist. Do not render until I approve the pick.
```

## 1. Sky forms — the 13 forms as prompts

Source: PUBLISHED (Sky's system as codified in
`skills/realskytan-system/SKILL.md` — 13 forms, D1–D14 devices, E1–E10
recipe). Pick the form the router names, then run its prompt shape:

```
Edit this as Sky Form {N} ({form name}): show-the-document first, one claim
one proof, designed captions, motion diagram that builds, proof on screen at
the claim second. PWC skin only: teal/gold on navy, NO RED, PWC logo,
nothing over my face. Motion named from MOTION.md. QC per EDIT-ROUTER.md §8.
```

## 2. Adilet one-liner — the whole avatar system in one line

Source: INFERRED reconstruction (`skills/adilet-system/PROMPTS.md` — his
literal prompts sit behind his SKILL comment funnel; these are written to
reproduce his MEASURED outputs: 222 wpm pacing, captions landing ON the
word at +0.013s median, −14.2 LUFS).

```
a reel about {topic} — keyword {MANYCHAT_KEYWORD}
```

The system expands it through its stages (script → hooks → pacing →
motion → captions → audio → self-review to 0 WEAK). Stage prompts live in
`skills/adilet-system/PROMPTS.md` (§1–§5).

## 3. Designed captions — full pass / plan-only / hero word / restyle

Source: PUBLISHED (`skills/pwc-designed-captions/PROMPTS.md`, P1–P4).
Paste-ready prompts for the caption pipeline (transcribe → track matte →
plan → render → composite). P1 is the full pass; P3 puts one hero word
behind the head (Anton ~320px, entrance EASE OUT 7 frames, exit EASE IN
5 frames, verified with a 3-frame strip at the crossing point).

## 4. Animations — one prompt per style

Source: PUBLISHED (`skills/pwc-animations/PROMPTS.md`, modeled on
@viashaan's /animate system): `/stat-chart`, `/map-route`, `/headline`,
`/teardown`, `/paper-desk`, `/ink-wash`. Each names its motions
(MOTION.md) — that naming is what separates these from generic "animate it".

## 5. Herk short-form edit — the invocation

Source: PUBLISHED (@nateherkai, MIT — `short-form-edit` skill, staged in
`zips/short-form-edit.zip`). His system in one call:

```
Edit {VIDEO} as a short-form reel with the short-form-edit skill.
First frame is ALREADY a split: the proof/tool on top, me below.
One visual per spoken phrase; shots 1.1–1.4s; pauses under 0.2s.
First gate: in the first 3 seconds, is someone convinced they need to
watch until the end? PWC skin only — teal/gold on navy, NO RED, logo,
nothing over my face, WAITLIST routing.
```

## 6. Viral outliers — the research feed

Source: PUBLISHED (Ava Yuergens @personalbrandlaunch, MIT —
`viral-outliers` skill, staged in `zips/viral-outliers.zip`).
Rule number one: never write a script without WATCHING and LISTENING to
the outlier. The caption is not the script.

```
Find the viral outliers in my niche (700K+ views AND 5x the account's
follower count). Watch each one frame by frame, transcribe the audio, and
turn it into a fill-in-the-blank script template adapted to my brand, plus
the caption. Read references/brand-profile.md first — if it is still a
template, stop and fill it in with me.
```

## 7. Long → short clipper

Source: PUBLISHED (social-media-skills, MIT — `video-to-shorts-skill`,
staged in `zips/video-to-shorts-skill.zip`).

```
Turn {LONG VIDEO} into vertical short clips. Transcribe with word
timestamps, score every candidate moment with the clip rubric (hook,
standalone, payoff), cut 1080x1920 clips with ffmpeg. Captions: Poppins
ExtraBold 96px, max 3 words on screen, spoken word in accent colour.
Hook line burned in. PWC skin only.
```

## 8. Zeeuiux 5-pass reel edit

Source: PUBLISHED (his free kit — prompts/guide only, no SPDX; do not
relicense). One scene per idea, fired on its trigger word.

```
Edit this reel in 5 passes: (1) transcribe, (2) cut out dead space,
(3) captions — serif italic key word, one per sentence, max 3 words,
never over my face, (4) motion — fast in 0.2–0.35s, hold, clean out,
ease-out entrances, one idea per scene firing on its trigger word,
(5) sound. Target −14 LUFS. PWC colours (his near-black + pastel
gradient re-skins to navy/teal/gold).
```

## 9. Retention-dip rescue (re-edit a flopped post)

Source: INFERRED from @martinwang.mp4's case (9.3K → 2.5M views) —
confirm against the reel before building from it.

```
Find the dip in this reel's IG Insights retention graph. Cut exactly that
section in CapCut, tighten the beats around it, repost as a Trial reel.
Do not change the hook or the proof — only the dip.
```

## 10. Self-review loop (Adilet stage 5 + johannships QA gates)

Source: INFERRED (Adilet SYSTEM.md) + PUBLISHED (@johannships
reels-engine QA gates, MIT).

```
Review the exported video as a fresh viewer. Count every WEAK moment
(dead stretch, unclear claim, device that doesn't move, caption over a
face, word clipped). List them with timestamps. Fix them all. Ship only
when the count is 0 WEAK. Then run the hard QA gates: freezedetect zero
freezes ≥0.35s, ±0.15s audits around every card/board entrance and exit,
last-voice to end-card ≤1s.
```

---
---

## 11. Charlie Hills — full edit prompt (PUBLISHED, Substack Oct 22, 2026)

Source: PUBLISHED (charliehills, ~111K; full prompt in `research/prompts/full-prompts/charlie-hills-prompt.md`). Verified: 29 viral reels studied (13 creators); 212 frames checked; 5 min record + ~1 hr auto edit; −14 LUFS. The Sky grammar as text.

```
A new graphic every 2 seconds, top half, my face below. Each one changes
on its exact word. Cut pauses to 0.25s, only in true silence. Show me the
cut list first.
```

## 12. Steve Arneson — six-clips master prompt (PUBLISHED, free)

Source: PUBLISHED (stevearneson.com/clips; full prompt in `research/prompts/full-prompts/steve-arneson-six-clips-prompt.md`). Six-styles taste test = Q's pilot gate automated; face-safe zones named (hook below mouth, stickers chest height, proof above head); "46–69 seconds is the dead zone"; ship only at self-rated 9/10; brand.md mechanism.

```
Make six versions of this clip, one per style in the taste test. Face-safe
zones: hook below the mouth, stickers at chest height, proof above the
head. 46–69 seconds is the dead zone — land under 45 or over 70. Rate each
version; ship only the one that scores 9/10 or better.
```

## 13. AI Systems Lab — Claude Code edit lesson (PUBLISHED, free)

Source: PUBLISHED (resources.aisystemslab.ai/claude-code-edit-lesson; full prompt in `research/prompts/full-prompts/aisystemslab-prompt.md`). Measured: raw 3:17.4 → 0:33.6; 37 attempts removed; 75 silent gaps >0.15s cut; every effect within 1 frame of its word. Bar: RPN + Kallaway. **MUST re-skin palette (Claude orange #D97757 → teal/gold/navy) via its own revision prompt 02.**

```
Cut every silent gap over 0.15s. Every effect lands within 1 frame of its
spoken word. Then run revision prompt 02: re-skin the whole palette —
orange #D97757 becomes teal #14A886 / gold #FEE238 on navy #00214E.
```

## 14. @kingketo — 35 persistent rules + 19 named effects (PUBLISHED rules, skill file GATED)

Source: PUBLISHED (his 35 rules + 19 effects as described on IG; the skill file itself is gated behind EDIT — rebuild from the published rules only, INFERRED). Measured: 4:24 raw → 1:12 Reel; Rule 1 stutters 21.9s → 5.5s; 12+ long-form + 20+ Reels in 14 days untouched; 1.66M views across 69 reels. Music 31 dB under voice; real screenshots instead of typed metrics.

```
These 35 rules persist across every edit. Rule 1: cut every stutter.
Music sits 31 dB under the voice. Proof is always a real screenshot,
never a typed number. Self-check 13/13 before delivery.
```

## 15. @minolee.mp4 — 15-rule framework + 7 anti-slop instructions (PUBLISHED)

Source: PUBLISHED (@minolee.mp4, ~551K). Measured: 31 videos/week, 119 versions, $1,550 saved; SLOP 282 views vs VIRAL 495K views. Captions 2–3 words, no emojis, cut dead space >0.1s, pop-ups NOT animated, music ducked 25% → 10%.

```
Captions 2–3 words, no emojis. Cut dead space over 0.1s. Pop-ups do NOT
animate in — they appear. Music ducked 25% under speech, riding to 10%
in gaps. If it reads like a template, it fails.
```

## 16. @kienobifilms — cut-list-first + storyboard gate (PUBLISHED, verbatim)

Source: PUBLISHED (@kienobifilms, ~460K; prompts VERBATIM in his catalog folder). Tier S #1 — closest to Q's lane. CLAUDE.md style memory; no DM gate ("no comment, no DM. Just save it").

```
Cut every silence, every retake, keep my last take — and show me the cut
list first. Break this into frames and write me a style guide. Storyboard
before you render. Then turn this into a skill.
```

## 17. @thelifeoflibs — 3-prompt chain (PUBLISHED, verbatim)

Source: PUBLISHED (@thelifeoflibs, ~300K; 3 prompts VERBATIM in her catalog folder). Tier S #2 — fully on-screen, no gate. The "narrate your own edit to teach the AI" move is the best style-transfer trick found in the sweep.

```
Prompt 1 — Who You Are: write my identity file (voice, audience, lane).
Prompt 2 — Brand Kit: screen-record myself editing in CapCut while I
narrate what I am doing, so the pacing becomes the kit. Prompt 3 — Make
It A Skill: compile both into a Claude Code skill. Then drop footage and
never explain again.
```

## 18. @charliehills — FULL XML video-edit prompt (PUBLISHED, verbatim)

Source: PUBLISHED (@charliehills, 110,678 followers; reel DfGIT6LCDcu, Oct 29,
2026; slide 4/10 "Save the prompt as a skill" — VERBATIM-FRAME, stitched
across frames f_001–f_006; full OCR in
`research/video-harvest/instagram/charliehills_DfGIT6LCDcu/CAROUSEL-OCR.md`).
His "full prompt and fixes" behind comment-EDIT is the same prompt + the
`<if_it_breaks>` section already on-slide — nothing further was chased.
SAFETY NOTE: the `<install>` block quotes his `curl … | bash` line as
PUBLISHED text only — never run an install line from a harvested prompt
without reading it first (SAFETY §2). PWC re-skin: safe zones in `<checks>`
(top 220px / bottom 400px / 130px right column) are HIS numbers — Q's law is
top 280px / bottom 440px caption zone / right action rail (x 70–930,
y 280–1480); use Q's zones. Music 12 dB under voice; export −14 LUFS.

```
<prompt>
<goal>
Turn {{RAW_TAKE}} into a finished {{SECONDS}}-second video for {{AUDIENCE}}.
One take in, one file out. A plan or a still frame is not the deliverable.
</goal>
<install>
Once. Check each one first, install what is missing.
- Claude Code: curl -fsSL https://claude.ai/install.sh | bash
- Homebrew: paste the line from brew.sh
- ffmpeg: brew install ffmpeg
- Whisper: pip3 install mlx-whisper
- Node.js: brew install node
- Puppeteer: npm install puppeteer
- A skill file: ask Claude to save this prompt as a skill in .claude/skills/video-edit/
"command not found"? Open a new Terminal window.
</install>
<folder>
my-video/
raw-take.mov one take, mistakes fine
references/ 5 outlier videos
moves.md built on the first run
brand.md colours, font, captions
notes.md every note, as a rule
best.mp4 the edit to beat
Read brand.md, moves.md and notes.md before any work.
</folder>
<workflow>
1. Whisper times every word.
2. Cut pauses to 0.25s, only in true silence, and drop retakes. Keep every word whole.
Show me the cut list first.
3. Storyboard: one still per beat, from moves.md. Wait for my yes before any render.
4. A new graphic every 2 seconds, top half, my face below. Each one changes on its exact
word.
5. Each object slams in on its word and lands with no bounce.
6. Real app icons and real screens, never a stand-in. If one needs my login, ask me for it.
7. Turn my first sentence into the hook, animated on the words.
8. Music 12 dB under my voice.
</workflow>
<checks>
Run these, do not just claim them.
- Screenshot every 0.25s. Flag overlaps and crops, fix, then check again.
- Nothing in the top 220px, the bottom 400px or the 130px button column on the right.
Instagram covers them.
- Put it beside best.mp4. Count the graphic changes. Fewer than best.mp4? Add beats
and render again.
</checks>
<notes>
I give one note at a time. Save each one to notes.md as a rule for every video, so the next
edit needs fewer.
</notes>
<export>
H.264, 1080x1920, -14 LUFS. Save it as final.mp4 with the cut list.
</export>
<if_it_breaks>
- pip3 missing: brew install python
- Windows or an Intel Mac: pip3 install openai-whisper
- Puppeteer can't find Chrome: npx puppeteer browsers install chrome
</if_it_breaks>
</prompt>
```

## 19. @kappa.ai — 5-tool stack prompt pattern + CLAP query pattern (INFERRED)

Source: INFERRED reconstruction from @kappa.ai DecYkDcI799 (the setup file is
GATED, never chased) + PART-DRAFTS-V6.md. Licenses MEASURED: HyperFrames
Apache-2.0, Whisper MIT, CLAP MIT/CC0, Demucs code MIT / weights FLAG
(research use), Blender GPL. Part: `parts/creator-systems/kappa-5-tool-stack.md`.

```
One file installs the stack: HyperFrames (the engine) → Whisper (the ears)
→ CLAP (sound understanding) → Demucs (stem split) → Blender (free 3D).
Verify each with one test render before the real edit. Blender for
props/diagrams only, never fake people.
CLAP query pattern: describe the sound in words → find the matching clip.
"Find me a whoosh like this one" over the licensed library; threshold ≥0.5
for a "same sound" match (his on-screen scores ran 0.51–0.87). Sound QC:
CLAP-label each SFX on the timeline and flag mismatches — a "whoosh" that
scores as "door slam" gets replaced. LAION CLAP only — never M2D-CLAP
(non-commercial license).
```

## 20. @gannon.meyer — motion-graphic-per-line prompt (PUBLISHED, verbatim)

Source: PUBLISHED (@gannon.meyer, 203,553 followers; carousel DeeSC_2EVS0,
Oct 14, 2026; slide 8/12 "then use this prompt" — VERBATIM-FRAME, single
frame f_004; full OCR in
`research/video-harvest/instagram/gannon.meyer_DeeSC_2EVS0/CAROUSEL-OCR.md`).
Upload step (slide 7): Claude Code, Opus 5.5, Extra effort. His file path
`C4385.mp4` is his own path, published by him. PWC re-skin: 2160×2160 white
background → PWC navy canvas, teal/gold; 10s per graphic → Q's ≤2s visual
events; the per-line graphics land on the exact spoken word.

```
@"C:\Users\ganno\OneDrive\Desktop\C4385.mp4" Here's my edited video, no captions or graphics yet. Watch it and transcribe it with word timestamps, then make a motion graphic for every line where I show or explain something: 2160x2160, 60fps, about 10 seconds each, on a pure white background. Use the real UI of every app I mention and my real names, products, numbers and photos, no placeholders. Check every clip frame by frame before you send it. Save them all to one folder on my Desktop, numbered in script order, and give me a list of where each one goes on my timeline, down to the word.
```

## 21. @kingketo — "edit this video like the examples" ×2 skins (PUBLISHED, verbatim)

Source: PUBLISHED (@kingketo / Brandon Carter, ~970K; carousels DfLErkLEU5K
and DfXu-E5kfjE, Oct 31, 2026; slide 7/10 Step 6 — VERBATIM-FRAME; full OCR
in `research/video-harvest/instagram/kingketo_DfLErkLEU5K/CAROUSEL-OCR.md`).
One system, two skins (black/gold serif vs black/yellow grid). The 35-rule
SKILL.md behind comment-EDIT is GATED — rebuild from the published rules
only (PROMPTS.md §14). Measured: 4:24 raw → 1:12 Reel; 132 words of
restarts gone / 33 clean pieces kept; "Checked it: 11 of 11 passed".

```
Yo, edit this video like the examples.
```

The line only works because the EXAMPLES carry the style: teach with
example reels first (3+ finished edits in the folder), then the one line
invokes them. Checklist after the cut: graphics/captions/beats present,
11 of 11 self-checks passed, raw 4:24 → 1:12. Same doctrine as
@kienobifilms §16 (cut-list-first) and @zachdoesai_ §22 (/inspiration) —
the examples ARE the brief.

## 22. Stream-1 Tier S prompt steals (PUBLISHED, verbatim where shown)

Source: BULK-DECODE-LOG.md Batches 1–6 (180 DECODE.md files so far; Tier S
candidates listed per batch). thelifeoflibs 3-prompt chain is already §17 —
the rest of the Tier S set lands here. Parts:
`parts/creator-systems/zachdoesai-command-catalog.md`,
`parts/creator-systems/aiwithrone-setup-prompt.md`,
`parts/imagery/imagery-titles-behind-head.md`.

- **@kienobifilms — cut-list-first + titles-behind-head** (§16 has the
  cut-list prompt verbatim). The titles-behind-head cue: the title passes
  BEHIND the speaker's head — depth, not a paste-on. One hero word per
  section, front captions yield during the hero window.
- **@aiwithrone — setup prompt (verbatim):** "You are my short form video
  editor. Set up these tools on my computer so you can edit my videos.
  Check what's already installed first. Then install what's missing.
  Explain each step in plain English before you run it." Then reference →
  style guide: give Claude a finished reference video and ask for the
  numbered step list (push-ins, frame scale, framing shifts). That list IS
  the style guide. (Devt9LwPWrJ; 3-subfolder setup: reference / exports /
  raw.)
- **@zachdoesai_ — 4-command pipeline (verbatim lines):** `/clip` — "it's
  going to remove all the dead space in your video." `/captions` — "it's
  going to add perfect text captions to your video." `/storyboard` — "it's
  going to create an entire storyboard for how it would edit the video, and
  you can give it feedback so that edit turns out exactly how you wanted
  to." `/inspiration` — "give it the link to an already edited video, it
  will teach itself how to edit videos exactly like that." (Deo5YM4uq4L;
  the skill file behind comment-VIDEO is DM-gated, NOT chased.)
- **@kingketo — verbal-command catalog:** one sentence per device ("make X
  rotate around me", "add a wall of my photos behind me", "add B-roll over
  me talking") — each maps to one effect part. The /effects pattern in
  plain English; the most Q-portable phrasing in the sweep (no
  slash-command literacy needed). (Dey8EwBgmnr / DfNi-KCCl1B.)
- **@kylewhitrow — batch machine:** 26-carousel batch + preview HTML +
  feedback loop; logo animation skill (10 animations in 30s); batch CTA
  swap across 53 videos (preview HTML + copy JSON). The keyword CTA is
  DATA, not baked pixels. (DY2OL6zFP5E / DYuzPfjDt-r / DYxEl77Ef5M.)
- **@mehganjames — 5-pass setup prompt (verbatim):** "You're my reel
  editor. I've uploaded a raw talking-head clip. We'll edit it in 5
  passes, one at a time. After each pass, render a preview and wait for my
  notes. 01 Transcribe. 02 Cut-out. 03 Captions. 04 Motion. 05 Sound.
  Export 1080x1920, 30fps." (Demj7efEX_L slide 10/11; the 5 pass prompts
  themselves are DM-gated, NOT chased.)

## 23. Stream-2 first-prompt architecture (PUBLISHED, summarized)

Source: Grow with Alex — youtube.com/watch?v=03BNd8ygnq8
(PROMPT-PATTERNS.md §12–15; CLAUDE-CODE-WORKFLOWS.md §14). His verbatim
13-item prompt text is shown on screen only, not spoken — this is a
SUMMARY, not his quoted prompt. Part:
`parts/prompts/prompts-first-prompt-architecture.md`.

The first prompt packs 13 items: one job per file (brand image = branding;
reference reel 1/2 = what to take from each, specifically; animation MP4 =
context), exact branding (screenshot of colours + fonts), the 5 basics,
self-check ("check your work against these rules and your own past
mistakes"), working rules, and ask-for-more-than-a-reel (a list of every
choice made without asking + a Q-sheet: timestamp + what's on screen).
Riding rules: "Preview only the part that changed" (verbatim — in EVERY
prompt, never re-render the full reel for a fix); feedback format Verdict /
Fixes (numbered + timestamped) / Keep / Show me (stills before any render);
recovery prompt "Add rules, not effects" (verbatim hard rules: no cutouts,
no film grain, no heavy glow, face natural, one thing moves at a time,
captions never cover the subject, five stills before any video); second-chat
receipt reader (paste Claude's reply into a fresh chat and ask it to flag
anything alarming, off-topic, or drifting from the brief).

## 24. @tenfoldmarc — 3-hook trial-reel prompt (PUBLISHED, verbatim)

Source: @tenfoldmarc reel DfTT3nszegV (Nov 3, 2026) + RABBIT-HOLE-MANIFEST.md.
Part: `parts/creator-systems/tenfoldmarc-3-hook-trial-reels.md`.

The prompt (verbatim, on screen): "Make 3 trial reels. Use a different part
of the video as the hook for each."

The 3-hook script template: HOOKS ①②③ + BODY + CTA — the same body, three
different openings, same CTA. The hook is the variable, the video is the
constant. Variation taxonomy (from his Dep25/Dep585 thumbnails — the
anti-duplicate rule): MIRRORED / NEW HOOK / NEW GRADE. Every variation is
labeled with its type. Q's lane: trial reels are app-only for @yerrr__q (Q
posts them himself); Muse supplies the daily three from the yapping pool.

## 25. @tenfoldmarc — Content Dashboard prompt (PUBLISHED, verbatim)

Source: @tenfoldmarc carousel DYyOxh9DCKJ (May 25, 2026) + guide
guides.tenfoldmarketing.com/build-content-dashboard. Part:
`parts/strategy/strategy-dashboard-carousel.md`.

The prompt (verbatim from the guide fetch): "Build me a content dashboard
for my creator business with these six pages: Hook Vault, Analytics,
Competitor Tracker, Scheduler, Content Calendar, What's Trending. Use
Next.js + Tailwind + shadcn/ui. Dark mode, terracotta accent. Sidebar with
@tenfoldmarc on top. Create a CLAUDE.md…"

PWC re-skin before pasting: swap the handle (@tenfoldmarc → @yerrr__q);
swap the accent (terracotta → teal #14A886 / gold #FEE238 on navy #00214E);
the six pages stay. Every figure on the dashboard must trace to a real
source (Skool / Stan / IG insights) or it doesn't go on the slide.

## 26. @sameyeam.secrets — waveform cut rule (PUBLISHED, verbatim)

Source: IG carousel p/DffJf54jd9j (150K), Nov 8, 2026 +
`research/prompts/instagram/sameyeam-secrets/` + DELTA-2026-11-08.md.
Part: `parts/render-pipelines/pipeline-qc-gates.md` (SL-08 pause gate,
SL-09 no-clipped-words).

The prompt (verbatim): "Time every word, cut only flat gaps ≥0.3s
leaving 0.1s each side, never cut inside a word, and verify 0 ms of
speech cut."

Verified result: 28.1s → 25.8s, 6 gaps removed, 0 ms speech cut
(before/after waveforms on screen). This is Q's "no word ever cut
off" rule as a machine-checkable prompt — paste it as the cut rule
before every edit, and make the "verify 0 ms of speech cut" check part
of the QC report.

## 27. kajisho5 — one-message talking-head spec (PUBLISHED, verbatim)

Source: nelson.gm-ai.net guide, Nov 2, 2026 (late catch) +
`research/prompts/web/kajisho5-42-tools/` + DELTA-2026-11-08.md.
Part: `parts/render-pipelines/pipeline-qc-gates.md`.

The prompt (verbatim): "video.mp4 is a raw talking-head take. Make
reel.mp4 for Instagram Reels, 1080x1920. Cut the dead air between
sentences but never clip a word. Burn in word-by-word captions with
the spoken word highlighted, in sync after the cuts. Loudness -14
LUFS, true peak no higher than -1 dBTP. Check the result before you
say it is done."

PWC note: the tightest one-message talking-head spec in the harvest —
numbers pinned (1080x1920, -14 LUFS, -1 dBTP), no-clipped-words, and
the self-check line. The kajisho5 add-on itself is NOT vetted (repo /
license / scan = repo-stream job) — use the prompt text only, do not
install anything on this entry's strength. Safe-zone line from the same
guide (adapt to PWC zones x 70–930, y 280–1480): "Every caption pixel
stays between y 360 and y 1420 and left of x 960."

## 28. @jackroberts___ — deeper-expert prompt (pattern, not his prompt text)

Source: Jack Roberts DEEPER reel + caption, Batch 7. Part:
`parts/prompts/deeper-expert-prompt.md`. His prompt text is gated (be-ambitious
prompt, comment BE AMBITIOUS → DM) — NOT chased; the pattern below is rebuilt
from the visible teaching. The quotable line: "The ceiling is your request.
Not the model."

The pattern: (1) state the TASK, then reframe it as the GOAL it serves;
(2) ask Claude to review its own plan as the expert before executing;
(3) run the expert review as a second pass, not a first draft. Never paste
a gated prompt you have not seen — rebuild the pattern from Q's rules,
labeled INFERRED.

## 29. Scriptwriting lane — the run procedure (Bradford Marais + CCC)

Source: Batch 5 + Batch 6, v8. Parts: `parts/scriptwriting/` (content-
architecture, brand-brain, script-structures, quality-gate, contrast-device,
viral-rewrite-skill). The run: (1) Brand Brain files exist first (who you
are / what you sell + where it is going / how you talk); (2) brain-dump the
idea, ideal follower, and what inspires you; (3) Claude structures it
against the Playbook's 12 structures (INFERRED mapping — his real 12 are
ungated-unknown); (4) the Quality Gate scores the script/hook/idea before Q
sees anything (95-gate threshold [NEEDS Q'S WORD]); (5) rewrite mode: take
a proven script, keep its structure, rewrite it for Q's avatar, and check
outperformance (≥2x median [NEEDS Q'S WORD]) before it ships. The interview
front end (Grill Me mechanic) is Matt Pocock's skill, distributed by
Bradford — credit Pocock on any rebuild. Run the psychology check (§29a — the 7 lines above, filed in
`parts/scriptwriting/script-structures.md`) inside the Quality Gate,
before the script is handed to the Hook + Motion + Imagery
specialists.

## 30. @unscripted.nishant — the 6 AM clock starter (v9; `parts/prompts/prompts-clock-starter.md`)

Source: @unscripted.nishant reel DfUaXygqWEs (Nov 2026) — INFERRED reconstruction; the exact steps are GATED behind comment CLOCK — never chased. **[NEEDS Q'S WORD]** — scheduled limit-spreading is an operational choice for Q, not adopted by default.

The rule: "It's not you, it's the clock. Your Claude limit works in 5-hour windows, and a window only starts when you send your first message." So make Claude send that first message for you at 6 in the morning, while you're asleep — 3 fresh windows in the workday instead of 2. "One catch. Your weekly limit stays the same, so this spreads your usage out. It doesn't give you more."

Executable steps: (1) the window rule — a 5-hour limit window only starts at the first message; (2) the starter — a tiny scheduled task at 6 AM, type "hi", pick Haiku (the smallest model, so it barely touches the limit), set it daily; (3) the honesty line — the weekly limit stays the same, state the catch wherever the trick is taught, never sell it as extra usage.

Full text: `parts/prompts/prompts-clock-starter.md` (also in `pwc-prompts.zip`).

## 31. @kimanidigital — the verbatim edit brief, in one card (v9; `parts/prompts/prompts-kimanidigital-edit-brief.md`)

Source: @kimanidigital "POV: You taught Claude to edit your Reels" (DagRMDYOZZE). The prompt card is VERBATIM-FRAME (read from frames directly). Tier S candidate.

The brief names the edit. Style + safe zone + volume, in one card — the card is the brief, not a conversation.

```
"Please: 1. Remove any obvious bloopers or long pauses / 2. Add auto-generated subtitles throughout, styled in bold white text with a semi-transparent black background, short-form safe zone positioning / 4. Add background music: search Pixabay for a [mood] track and layer it underneath the audio at 30% volume."
```

[Item 3 is not in the decode — recorded as observed; the card as harvested jumps 2 → 4. Do NOT invent item 3.] PWC remap: captions are PWC designed captions (teal/gold on navy, keyword in gold, never over the face, center-lower) — NOT bold white on semi-transparent black; music is a cleared instrumental from Q's local licensed library, mixed under speech — NOT Pixabay search, NOT 30% volume as a standing number.

Full text: `parts/prompts/prompts-kimanidigital-edit-brief.md` (also in `pwc-prompts.zip`).

## 32. @shedoesai / @soravjain / @vaibhavsisinty — the one-sentence brief (v9; `parts/prompts/prompts-one-sentence-brief.md`)

Source: @shedoesai Db5Z8cixSEJ (one-sentence prompt, Nov 2026) + @soravjain DaxwpzDp0M2 (one-line edit command) + @vaibhavsisinty DXJ4txpABdO (one-line brief → 5 variations). INFERRED reconstructions; the guides are GATED — never chased. Higgsfield (soravjain / vaibhavsisinty) is a PAID product — named only, never buy.

The brief is one line. The tightest in the sweep: "Keep the good takes, tighten my pauses, add captions, and motion graphics every 2–3 seconds" — four verbs, one line. The 2–3s motion cadence matches Q's ≤2s visual-event rule. One line in, the edit out.

Executable steps: (1) four verbs, one line — keep the good takes / tighten the pauses / add captions / motion graphics every 2–3 seconds; (2) one-line edit command — "Use [tool] and edit this video in vertical format" (Q's version: Claude + CapCut, 1080x1920); (3) one-line brief → structured prompt → variations — one input, five variations (different angles, moods, hooks).

Full text: `parts/prompts/prompts-one-sentence-brief.md` (also in `pwc-prompts.zip`).

## 33. @zachdoesai__ — research codes (v9; `parts/prompts/prompts-research-codes.md`)

Source: @zachdoesai__ reels DfYfhYTiRuZ / DfYhV2-DeEC / DfYi9AMjlqc / DfccP2gsZqb (5 secret research codes, Nov 2026) — INFERRED reconstruction; the skill install is GATED behind comment RESEARCH — never chased.

Research is commands, not browsing. Five codes, one job each — the output is always a cited report, never a vibe. The sharpest framing in the sweep: "learn to THINK in the style, not copy it" (from his /build-style reel DexAiZthd4j — style-learning without cloning; Q's rule: mirror grammar, never exact content).

Executable steps: (1) /fact-check — plot every claim, check against real sources, flag what can't be backed up (claim → ✓ TRUE / ✗ No source found); (2) /last-30-days — what real people said about a topic in the last 30 days (Reddit / X / YouTube), source material for hooks in the audience's own words; (3) /deep-research — "full report with every source cited"; (4) hook ladder — one script, four hooks (the re-cut lesson, a variant on tenfoldmarc-3-hook-trial-reels / hooks-jev-hook-bank).

Full text: `parts/prompts/prompts-research-codes.md` (also in `pwc-prompts.zip`).

## 34. @ohyesinvest — rules, not vibes (v9; `parts/prompts/prompts-rules-not-vibes.md`)

Source: @ohyesinvest reel DerpMRqAWjb ("Video editors are absolutely cooked", Nov 2026) — INFERRED reconstruction from the visible transcript + frames; the full prompt is GATED behind comment EDITS — never chased. Variants: @scottsmithyta Deu22jMJFAW (copy-the-system + source-for-every-number); @okaashish De9oW8Iv0jK (give-Claude-eyes: download + watch any reel from a link).

A style is just rules. Never tell Claude "edit like Nick" — AI has no idea what that means. It knows rules, systems, processes. Claude watches the reference videos and MEASURES them (layouts, pacing, captions, cuts), then writes the measurement down as a 12-step rulebook document, saves it as a skill, and only then edits. "Nick's whole look is basically just rules. So can't we just steal the rules?"

Executable steps: feed Claude 3–5 reference reels (links); it records per reel layout, pacing, caption grammar, cut grammar as a table — then the rulebook, then the edit. Measure, don't vibe.

Full text: `parts/prompts/prompts-rules-not-vibes.md` (also in `pwc-prompts.zip`).

## 35. @nategold.ai — the study progress card (v9; `parts/prompts/prompts-study-progress-card.md`)

Source: @nategold.ai reel Dezi9CKtaAv ("Claude is now editing 17 videos for me", Nov 2026) — INFERRED reconstruction; the full guide + setup are GATED behind comment VIDEO — never chased. (The instagram-agent repo — 13 free MIT skills, SCAN PASS — is a SEPARATE public resource from the same creator.)

Claude shows its work as a checklist with a live percentage — the study step is visible, not hidden. "Studying your reference first (61%)" — fonts, colours, captions, cuts, each ticking off as Claude studies the reference reel BEFORE editing. The pilot gate, made visible.

Executable steps: (1) reference-first — study the reference reel's fonts / colours / captions / cuts BEFORE editing; (2) the card — a checklist card shown during the build, each item with a live % (Studying your reference first 61% → Fonts ✓ → Colours ✓ → Captions ✓ → Cuts ✓). The card is the proof the study happened, not a claim.

Full text: `parts/prompts/prompts-study-progress-card.md` (also in `pwc-prompts.zip`).

## 36. @pankajshivnani — taste files: slot.md + style.md (v9; `parts/prompts/prompts-taste-files-slot-style.md`)

Source: @pankajshivnani reel DezSI08JS2L (Nov 2026) — INFERRED reconstruction; his Pro plan is NOT adopted. Variants: @shihui.travels De_2J7AM-Sp (train-a-junior; one-message feedback with timestamps; "save my style"); @mr.romanwei DeyxYlmk9CH (save every edit into a rules file).

Taste lives in two files, not in a prompt. slot.md = the basic instructions ("I don't like videos like this... I like minimalist video. I don't want to zoom in too much. I want simple videos."). style.md = all the context (what kind of video you want; references to people; things I like, things I don't like). Claude reads both before it touches a frame.

Executable steps: (1) slot.md — the brief in the creator's own words, with named reference videos; (2) style.md — the context file (kind of video, references, likes/dislikes, brand kit); (3) test 20–30 seconds first — run the taste files on a 20–30s cut, watch it, then scale.

Full text: `parts/prompts/prompts-taste-files-slot-style.md` (also in `pwc-prompts.zip`).

## 37. Unknown creator — the word-timed graphics prompt (v9; `parts/prompts/prompts-word-timed-graphics-prompt.md`)

Source: unknown creator reels DeeR-7fEW4L / DeeR-gLkUAe / DeeR-p9Ee-b / DeeR-ySkS9y / DeeR_HwkamL / DeeR_YukUmg / DeeR_xPETOA / DeeSAVekcvl / DeeSAgbEaTJ / DeeSApmkV7Q / DeeSBCVEVG4 / DeeSBTtEQBm (motion-graphics carousel, Nov 2026) — INFERRED reconstruction from the visible slides. The prompt text itself is GATED behind comment PROMPT — never chased; the spec below is rebuilt from what is shown. Variant: @othmantmoulik DfVRD0SCriR (script-drives-the-recording).

Step 1: write the script — that's it. The script is the whole input; the graphics come from the script, not from a second brief. Claude gets the video AND the timestamps of when things are said, so every motion graphic is cut to the right length — the graphic lands on the word, not near it.

Executable steps: (1) write the script; (2) record it, then cut every pause — no captions or graphics yet, just you talking to the camera; (3) upload the clean cut to Claude — graphics timed to the words.

Full text: `parts/prompts/prompts-word-timed-graphics-prompt.md` (also in `pwc-prompts.zip`).

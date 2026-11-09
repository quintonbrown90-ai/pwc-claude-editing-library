<!-- DO NOT edit parts/ directly from this file. Coordinator merges this draft into the target path. -->
<!-- Sources: BULK-DECODE-LOG.md batch 15 (items 3–13) + per-video DECODE.md files (research/video-harvest/instagram/mehganjames_Demj*/). -->
<!-- Existing canonical parts checked first: no existing 5-pass / multi-pass part in parts/ (checked creator-systems/, prompts/, render-pipelines/, knowledge-playbooks/). The closest existing material is the single-prompt setup in parts/creator-systems/aiwithrone-setup-prompt.md (a different creator's setup prompt, different structure) — this draft is a distinct system (five sequential passes + verbatim setup prompt), new part justified. -->
# CREATOR-SYSTEMS — @mehganjames 5-pass method: don't ask for "an edit," ask for five passes (DRAFT — v8)

Source: @mehganjames 5-pass method carousel, 11 slides in the harvest (cover
+ method + passes 01, 02, 04, 05 + all-5-passes timeline + direct-don't-edit
slide + setup prompt + CTA ×2), BULK-DECODE-LOG.md batch 15, items 3–13. All
silent, decoded from frames. **The pass-03 captions slide (05/11) is NOT in
the harvest — see Gaps.** Handle correction from the log: the creator is
@mehganjames (full-res frames) — contact sheets read "meljames"; full-res
wins.

## The rule
"Don't just ask for "an edit." (struck through) / Ask for five passes. /
One huge prompt gets you mush. Five focused ones, in order, get you a reel
that looks edited." The five passes, in order:
01 Transcribe — Every word, timestamped / 02 Cut-out — You, lifted off the
background / 03 Captions — Synced to your voice / 04 Motion — Graphics that
land on the word / 05 Sound — Hits, taps and a clean mix. "Same chat. One
pass at a time. Save this for your next reel."

## The passes (verbatim from the decodes)
- **Cover (Demjr2TEeDW):** "CLAUDE · REEL EDIT / Claude edits my reels
  now. / Raw clip in. Finished reel out." + BEFORE/RAW ("because you're not
  editing them") → AFTER/CLAUDE ("that's called the...") + "Swipe for the
  5-pass method →".
- **Method (Demjr81Ebct, slide 02/11):** the five-pass list above.
- **PASS 01/05 TRANSCRIBE (DemjsE-Ec0p, slide 03/11):** "First, Claude
  listens. / Every word gets a timestamp. Captions, graphics and sound all
  sync to this one file." + a words.json panel (00:10.59 "the" → 00:12.19
  "steps,") + "PROMPT: Transcribe my clip word by word, with timestamps.
  Save it as words.json." The listen-first doctrine: one timestamped file is
  the sync source for everything downstream.
- **PASS 02/05 CUT-OUT (DemjsL2kRN1, slide 04/11):** "Then it cuts you out
  of the frame. / Frame by frame, with soft edges and no sticker outline.
  That's how text lands behind your head." + a cut-out on a checkerboard
  ("Removed on every frame" / "cause you're... yapping" / "Slides in behind
  you / Kept, with soft edges") + "Cut me out of the background on every
  frame. Soft edges, no outline." The text goes BEHIND the head, never over
  the face — maps directly onto Q's brand law.
- **PASS 03/05 CAPTIONS — MISSING FROM THE HARVEST.** Only the method
  slide's one-liner survives: "03 Captions — Synced to your voice". No
  pass-03 slide, no pass-03 prompt. See Gaps — do NOT invent it.
- **PASS 04/05 MOTION (DemjsStEZs9, slide 07/11):** "Every graphic lands on
  a word. / Claude reads the transcript, grabs one scene per idea, then
  builds each one in code, timed to the frame." + three phones ("reels" /
  "checklist" / "label") + "Plan one scene per idea. Fire each one on its
  word." Same doctrine as Gannon Meyer's word-timed graphics (batch 14) —
  two independent sources, same rule.
- **PASS 05/05 SOUND (DemjsdvkbWT, slide 08/11):** "Then it designs the
  sound. / A hit on the hook. A tap on every pop. A chime to close. Mixed
  loud and clean for the feed." + a waveform UI + "Add SFX on every cue.
  Voice on top. Master to -14 LUFS."
- **ALL 5 PASSES · ONE TIMELINE (Demjsu2keIw, slide 06/11):** "Raw clip in.
  Finished reel out." + BEFORE/RAW → AFTER/CLAUDE + a Timeline ("brain",
  00:00:11.10) with tracks VIDEO / CUT-OUT / SCENES (Hook, Spin, Checklist,
  Freeze, CTA) / CAPTIONS / SFX + the five-pass list.
- **THE PART NOBODY SAVES (DemjsmhEUVO, slide 09/11):** "You don't edit. You
  direct. / Watch the render. Give notes like you'd give an editor. Claude
  re-renders. Repeat until it's yours." + a note bubble "My captions are
  covering my face. Keep everything under my chin." + "Moving captions below
  your chin and re-rendering." + "Your taste is the one part it can't do for
  you." NOTE: "Keep everything under my chin" is HER caption note — Q's rule
  is captions center-lower, never over the face. Her wording is not adopted;
  the direct-don't-edit doctrine is.

## The setup prompt — VERBATIM (PUBLISHED)
Slide 10/11 (Demjs2TEab4), verified in the per-video DECODE.md
(research/video-harvest/instagram/mehganjames_Demjs2TEab4/mehganjames_Demjs2TEab4_DECODE.md):

> "You're my reel editor. I've uploaded a raw talking-head clip. We'll edit
> it in 5 passes, one at a time. After each pass, render a preview and wait
> for my notes. 01 Transcribe, 02 Cut-out, 03 Captions, 04 Motion, 05 Sound.
> Export 1080x1920, 30fps."

Framing on the slide: "Before pass 01, paste this. / It turns Claude into
your editor: the passes, the order, the export settings. One message." +
"raw-clip.mov / MOV · 54 MB". The prompt's six parts: (1) the role (you're
my reel editor); (2) the input (a raw talking-head clip); (3) the method (5
passes, one at a time); (4) the loop (after each pass, render a preview and
wait for my notes); (5) the pass list (01–05); (6) the export (1080x1920,
30fps). **Verbatim caveat, carried from the decode itself:** the prompt's
tail (03 Captions, 04 Motion, 05 Sound. Export 1080x1920, 30fps.) was read
from the contact sheet's later frames — the full-res frame f_004 shows the
prompt typing through "02|". The quoted prompt is as published in the log
and decode; the tail's verbatim status rests on the contact-sheet read, not
a settled full-res frame. Flagged, not hidden.

## Executable steps
1. Paste the setup prompt (above) BEFORE pass 01 — one message, role +
   method + loop + export. Do not start with "edit this".
2. Run one pass at a time, same chat. After EACH pass, Claude renders a
   preview and WAITS for notes — the preview-and-wait loop is the pilot gate
   in prompt form. No pass renders until the previous pass is approved.
3. Pass 01 first, always: the words.json timestamp file is the sync source
   for captions, graphics, and sound. Nothing downstream starts without it.
4. Pass 02 cut-out with soft edges, no sticker outline — the cut-out is what
   lets text land BEHIND the head.
5. Pass 04: one scene per idea, fired on its word. Pass 05: SFX on every
   cue, voice on top, master to -14 LUFS.
6. Direct, don't edit: watch the render, give notes like you'd give an
   editor, Claude re-renders, repeat until it's yours. Your taste is the one
   part it can't do for you.

## Worked example (PWC)
A P-pack talking-head take: paste the setup prompt with Q's export
(1080x1920, 30fps — matches Q's post spec). Pass 01 → words.json. Pass 02 →
cut-out (soft edges; titles-behind-head device from
parts/imagery/imagery-titles-behind-head.md). Pass 03 → Sky captions,
word-exact, center-lower, never over the face (PWC caption rules replace her
missing pass-03 prompt — see Gaps). Pass 04 → one scene per idea (wall →
count-up → CTA). Pass 05 → hit on the hook, tap on every pop, chime to
close; voice on top; -14 LUFS. Each pass previews and waits for Q's notes.

## PWC skin
Palette teal #14A886 / gold #FEE238 on navy #00214E, no red. Her "Keep
everything under my chin" is NOT adopted — Q's rule is captions center-lower,
never over the face. Her CTA (slide 11/11, comment EDIT → setup prompt + 5
pass prompts + reel style rules by DM, free, no email) is gated — NEVER
chased; the setup prompt above is published on the slide itself, which is
why it is quoted here. The 5 pass prompts beyond the setup prompt are NOT in
the harvest except the four quoted in the pass slides (01, 02, 04, 05) —
see Gaps.

## Discrepancies — carried as observed, NOT reconciled
- None inside the 5-pass system itself. (Cross-system note: her pass-04
  "Every graphic lands on a word" matches Gannon Meyer's word-timed graphics
  doctrine, batch 14 — two independent sources, same rule. Her pass-02
  "text lands behind your head" matches the titles-behind-head device — no
  conflict, recorded as confirmation, not reconciliation.)

## Gaps
- **Pass-03 captions slide (05/11) is NOT in the harvest.** Its pass prompt
  is unknown. The method slide gives only "03 Captions — Synced to your
  voice". A PWC pass-03 prompt must be authored from Q's caption rules
  (Sky word-exact captions, center-lower, never over face), labeled INFERRED
  — the missing slide is a GAP, not an invitation to invent her prompt.
- **The setup prompt's tail** rests on a contact-sheet read (see verbatim
  caveat above). If a full-res re-read ever contradicts it, the decode wins
  over this draft.
- **CTA slide is a DUPLICATE:** Demjs8tkbfm and DemjtDikVd_ are the same
  11/11 CTA content (same size, same 5 sampled frames byte-identical,
  different post ID — re-upload / re-encode). Both decoded; content
  identical. No second CTA variant exists.

## Needs Q's ruling (flagged, NOT adopted)
- Adopt the 5-pass sequence (with PWC pass-03 authored from Q's caption
  rules) as the standard edit order for Claude edits, or keep it as one
  creator's method among others? The preview-and-wait loop after each pass
  matches Q's pilot-gate order; the sequence itself is hers.
- -14 LUFS master spec: adopt as the PWC mix target, or keep Q's existing
  audio spec? (Her number, single source.)

## Variants (v9)
- **v9 · @itsaustinmyers, DfDuiAgMlg2:** **V40 — @itsaustinmyers pass-by-pass (DfDuiAgMlg2):** "You don't want it to build the entire thing end to end... it gets to be much harder to make changes" — build the opening, then iterate; timestamp tweaks ("at six seconds, make this tweak"); "I approve this as the final version" (also pipeline-qc-gates). _(source: bulk-b VARIANTS.md)_
- **v9 · @itscristinabecher, De_mn2stFWP:** **V41 — @itscristinabecher raw-in (De_mn2stFWP):** "All I give it is this raw footage and it turns it into this entirely edited video" + "I never ever open an editing app" + the loop (hook repeats at the end). _(source: bulk-b VARIANTS.md)_
- **v9 · @ibraviz.ai, DfZwGFMMdk1:** **V42 — @ibraviz.ai conversation editing (DfZwGFMMdk1):** "upload this pack and just have a conversation with Claude" — plain-language revision voice ("make it moodier, and the whole edit changes"). _(source: bulk-b VARIANTS.md)_
- **v9 · @itsflxkzy, DfZshVBtn4x:** **V43 — @itsflxkzy anti-single-prompt (DfZshVBtn4x):** second source for the doctrine in V21 — one prompt made the whole thing = cheap; the well-made ones are built in passes. _(source: bulk-b VARIANTS.md)_
- **v9 · @?, Demjr2TEeDW:** **V30 — cover (Demjr2TEeDW):** "Raw clip in. Finished reel out." + BEFORE/RAW → AFTER/CLAUDE phones + "Swipe for the 5-pass method →". _(source: bulk-b VARIANTS.md)_
- **v9 · @?, Demjr81Ebct:** **V31 — ask five passes (Demjr81Ebct):** "One huge prompt gets you mush. Five focused ones, in order, get you a reel that looks edited." + the five-rows list + "Same chat. One pass at a time." _(source: bulk-b VARIANTS.md)_
- **v9 · @?, Demjs2TEab4:** **V32 — setup prompt (Demjs2TEab4):** verbatim setup prompt ("You're my reel editor. I've uploaded a raw talking-head clip. We'll edit it in 5 passes, one at a time. After each pass, render a preview and wait for my notes.") + "It turns Claude into your editor: the passes, the order, the export settings. One message." _(source: bulk-b VARIANTS.md)_
- **v9 · @?, Demjs8tkbfm:** **V33 — CTA (Demjs8tkbfm + duplicate DemjtDikVd_):** "FREE · NO EMAIL · NO CATCH" trust line + three-deliverable close (setup prompt, all 5 pass prompts, reel style rules) + "Send this to your editor. (Or don't.)" _(source: bulk-b VARIANTS.md)_
- **v9 · @?, DemjsE-Ec0p:** **V34 — pass 01 TRANSCRIBE (DemjsE-Ec0p):** "First, Claude listens." + "Every word gets a timestamp. Captions, graphics and sound all sync to this one file." + "Save it as words.json." (also pipeline-caption) _(source: bulk-b VARIANTS.md)_
- **v9 · @?, DemjsL2kRN1:** **V35 — pass 02 CUT-OUT (DemjsL2kRN1):** "Frame by frame, with soft edges and no sticker outline. That's how text lands behind your head." (also imagery-titles-behind-head) _(source: bulk-b VARIANTS.md)_
- **v9 · @?, DemjsStEZs9:** **V36 — pass 04 MOTION (DemjsStEZs9):** "Every graphic lands on a word." + "Plan one scene per idea. Fire each one on its word." _(source: bulk-b VARIANTS.md)_
- **v9 · @?, DemjsdvkbWT:** **V37 — pass 05 SOUND (DemjsdvkbWT):** "A hit on the hook. A tap on every pop. A chime to close." + "Add SFX on every cue. Voice on top. Master to -14 LUFS." DISCREPANCY (observed, not reconciled): audio-chain-adilet masters to −14.2 LUFS; her slide says −14 LUFS. _(source: bulk-b VARIANTS.md)_
- **v9 · @?, DemjsmhEUVO:** **V38 — direct (DemjsmhEUVO):** "You don't edit. You direct." + "Watch the render. Give notes like you'd give an editor. Claude re-renders. Repeat until it's yours." + "Your taste is the one part it can't do for you." Her caption-placement note ("Keep everything under my chin") does NOT transfer — Q's rule is captions center-lower. _(source: bulk-b VARIANTS.md)_
- **v9 · @?, Demjsu2keIw:** **V39 — timeline (Demjsu2keIw):** "ALL 5 PASSES · ONE TIMELINE" + SCENES track (Hook, Spin, Checklist, Freeze, CTA) + pause-and-label device. _(source: bulk-b VARIANTS.md)_

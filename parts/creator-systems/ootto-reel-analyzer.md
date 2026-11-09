<!-- PART: creator-systems/ootto-reel-analyzer.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# CREATOR SYSTEMS — Ootto Reel Analyzer (Tier S)

Source: Ootto-AI/claude-content-skills repo (MIT) — `skills/reel-analyzer/`
in `uploads/QUARANTINE/ootto-content-skills/` (SCAN PASS). Also
@jayantcreates.ai carousel DfY47FTFUv5, slide 2: paste any viral reel URL;
Claude watches the whole thing, reads the transcript, breaks down hook,
beats, pacing, visuals.

## The rule
URL in → hook / beats / pacing / visuals out. Learn why it worked before
you make your own. The analyzer is the first step of any remake — never
remake a reel that has not been analyzed.

## Executable steps
1. Input: a viral reel URL (Q sends the link in chat — the same link-drop
   habit as Kallaway's /analyze).
2. Output (fixed schema, same every video): hook (verbatim + why it works)
   / beats (the story's turns, timestamped) / pacing (cut cadence,
   visual-event interval) / visuals (what is on screen at each beat,
   face-safe or not).
3. The PWC filter: every visual beat is tagged face-safe / face-risk
   (nothing over Q's face — the analyzer flags any device that would cover
   his face in a rebuild).
4. The output is filed as a DECODE.md (Q's harvest already does this —
   this part is the skill that writes it, so a new reference takes minutes,
   not an afternoon).

## Worked example (PWC)
Analyze a viral hook reel → the analyzer returns: hook "3 mistakes" (list
hook, claim at 0.8s); beats: mistake 1 (0:08) / mistake 2 (0:19) /
mistake 3 (0:31) / payoff (0:44); pacing: cut every 1.4s; visuals: talking
head + proof tiles, face-safe throughout. The rebuild brief is written from
this output. Keyword WAITLIST.

## Human-made check
The analyzer's output is a brief, not a build — a human (Muse) still judges
whether the device fits Q's style before anything is built.

## PWC skin
Fixed schema, PWC palette, face-safe tagging on every beat. Credit: Ootto
(MIT).

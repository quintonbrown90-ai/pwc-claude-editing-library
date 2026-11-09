<!-- PART DRAFT (v9 bulk-c): creator-systems/three-run-planner.md | UPLOAD: SKILL + GITHUB | MAX: 50KB -->
# CREATOR SYSTEMS — the 3-run planner: explore → map → cut (@omgluka, Tier S)

Source: @omgluka reel DfahrkjBf3s (Nov 2026) — INFERRED reconstruction; the 3
skills + prompts are GATED behind comment KIT — never chased. The cleanest
plan-then-act pattern in the harvest.

## The rule
Three runs, never one big prompt. Run 1 (open folder, report what's inside) →
Run 2 (transcript, map the silences / dead air) → Run 3 (cut instructions:
"cut here, here and here"). The planner (model) writes instructions; the actor
(agent/tool) executes. The model never touches your files.

## Executable steps
1. **Run 1 — explore:** open the folder, report what's inside (takes, assets,
   script). No edits, just inventory.
2. **Run 2 — map:** get the transcript from the video so the planner can map
   exactly where the silences are. The transcript is the map, not the script.
   Output: silence map + take log ("take 1, second 15; take 2, second 27").
3. **Run 3 — cut:** cut instructions as positions, not prose — "cut here, here
   and here" (timestamps). The actor (ffmpeg / Remotion) executes the list.
4. **Separation:** the planner never rewrites the master. Claude plans,
   ffmpeg/Remotion executes. If the plan is wrong, fix the plan, not the file.
5. **Transcription-first:** transcribe first, then cut — same as kylewhitrow's
   transcription-based cut. "Good prompts follow templates" — the cut list
   follows the template, not freeform.

## Worked example (PWC)
Q's talking-head take: Run 1 inventories the take + script → Run 2 maps
pauses/stumbles against the script (script-compare: keep only the good takes)
→ Run 3 outputs the cut list → CapCut-native assembly → Muse QC on the export.

## Human-made check
The cut list is timestamps. If a cut instruction can't be stated as a
timestamp, it isn't ready to execute.

## PWC skin
Teal/gold on navy. Cut markers in gold on the timeline; nothing over the face.
CapCut-native motion throughout.

<!-- PART: render-pipelines/pipeline-drop-one-file-install.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# RENDER-PIPELINES — the drop-one-file distribution pattern (INFERRED)

Source: @kappa.ai EDIT funnel (PART-DRAFTS-V6.md). The pattern is the funnel
lesson, not kappa's code — their file is GATED, never chased.

## The rule
One file that self-installs the whole stack (Mac + Windows, local, no keys)
beats a multi-step setup guide: every extra install step loses funnel
conversions. Apply to Q's own skills: when Muse ships Claude a skill for Q,
ship it as ONE zip/file with a self-check (`READY` print) instead of a README
with 6 manual steps.

## Executable steps
1. Single zip + `setup.sh` / `setup.bat` that checks deps (ffmpeg, node,
   python), prints READY or the one missing piece, never asks for a key.
2. The self-check runs before any build step; a missing dep is the ONLY
   failure message, with the exact install line.
3. Version the file (v1/v2/…) — the newest version is the only one that
   posts/ships (newest-version rule).

## Worked example (PWC)
Design-system v6 ships as one zip. Claude opens it, runs the check, sees
`READY — 100 parts, 19 categories`, and starts the edit. No 6-step README.

## PWC skin
No credentials, no logins, no keys in the file — ever (SAFETY §3).

## Canonical-decode confirmation (Nov 8, 2026)
Parent's canonical decode (`research/video-harvest/instagram/
kappa_ai_DecYkDcI799_DECODE.md`) CONFIRMS the funnel shape verbatim:
"Comment, edit, and I'll send you the full setup ready to go. Just give
it to your Claude code and start editing." (transcript 37.9–43.3s;
end frames f_040–f_044 show the comment box + setup file install).
The file itself stays GATED — never chased. No correction to the
pattern above.
## Variants folded in (V7 — Rundown B, kappa.ai DemzpPeITcH Oct 17)
- **DM-delivery mock** — a 3-second mock shows the DM arriving ("New
  message · @kappa.ai") + the folder card ("claude-edit-setup / 5 tools ·
  ready to go ✓") + the "CLAUDE CODE · ready" window. Differs from the V6
  install pattern (one file, self-installs): this one TEACHES the funnel —
  it shows the viewer exactly what happens after they comment. PWC version:
  show the WAITLIST DM arriving + the 3-wins PDF + "you're on the list ✓" as
  a 3-second funnel explainer at the end of a CTA.

## Variants (v9)
- **v9 · @hellohauwa, DeLv5zBsiFQ:** 60. @hellohauwa, DeLv5zBsiFQ — "Do this test first" (settings → turn on code execution and file creation, or Claude cannot edit your videos) → variant on render-pipelines/ pipeline-drop-one-file-install.md (the READY check). "Made a mistake? Keep going / ✓ Claude cuts it out" (keep-recording rule) → variant on render-pipelines/pipeline-stockton-one-prompt-render.md. Prompt file gated (GAP). _(source: v9_variants_bulk_a.md)_
- **v9 · @?, V8-03:** V8-03 — Permission-before-install as a Claude working rule → pipeline-drop-one-file-install.md _(source: v9_verification.md)_
- **v9 · @?, V8-09:** V8-09 — One-time "always allow" for the worker AI so the run doesn't stall → pipeline-drop-one-file-install.md _(source: v9_verification.md)_
- **v9 · @?, V8-156:** V8-156 — Install scope: project-only, not system-wide (oTWUyW_bR-g, AI LABS) → pipeline-drop-one-file-install.md _(source: v9_verification.md)_
- **v9 · @officialpwnkumar, DfFDxPLS6qL:** @officialpwnkumar DfFDxPLS6qL — "connect Arcade MCP to Claude with just one click." DIFFERS: the one-click-connect phrasing. (Arcade MCP itself: third-party connector — GAP, needs license/scan + Q's word on third-party connections, cf. v8 [NEEDS Q'S WORD] #3/#9.) _(source: bulk-c VARIANTS.md)_
- **v9 · @saurabhs.builds, DW29q5sEdJ4:** @saurabhs.builds DW29q5sEdJ4 — copy-this-and-run-it install ("Go to Claude Code Docs, copy this, and run it in your terminal"). DIFFERS: the install as a copy + run, not a setup. _(source: bulk-c VARIANTS.md)_
- **v9 · @thecoachbraydon, DecEsp_jMLo:** @thecoachbraydon DecEsp_jMLo — HyperFrames install walkthrough (52s, 4 steps, cursor doing the thing) + VERBATIM install command `npx skills add heygen-com/hyperframes`. DIFFERS: second independent confirmation of the same command + URL already in the library (via Leo's reel). _(source: bulk-c VARIANTS.md)_
- **v9 · @imjonathanacuna, Da1wLVUywpB:** **V85 — @imjonathanacuna plan-first (Da1wLVUywpB):** secret prompt — describe the idea → Claude writes a plan to build 80% before a line of code (→ prompts-router-intake); ship chain GitHub → Railway → Stripe (→ pipeline-drop-one-file-install). Dangerous mode: GAP/FLAGGED, not adopted. Cheat sheet: GAP (gated). _(source: bulk-b VARIANTS.md)_

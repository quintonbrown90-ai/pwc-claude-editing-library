# CLAUDE.md — pwc-claude-editing-library

## Earshot: listen back to every edit (standing rule)

Earshot is installed for Claude Code (MCP server `earshot`, user scope, `EARSHOT_THREADS=3`; skills in `.claude/skills/earshot` and `.claude/skills/real-sound`). It gives you ears: you cannot hear an edit without it, so never judge, choose, or ship a sound on a guess.

On EVERY video edit, after each full render:

1. Run a listen-back pass on the exported file: `timeline` + `critique` (MCP tools or the `earshot` CLI).
2. Fix every cut it flags as having no sound, and every effect it flags as late, cheap, or mismatched.
3. Re-render, then listen again. A render is not done until it has been heard.

Sound choices:
- Bank first: render from Earshot's 252-sound bank (`sfx` / `kit`) — use the `launch` kit preset for films cut to music (effects ride 3–10 dB over the music bed; taps lead the cut, whoosh peaks land after it).
- For real recordings, choose with evidence: `rank` / `find` / `describe` / `realness` over the licensed local library instead of guessing from filenames.
- `forge` / `fit` only when neither the bank nor the library fits.
- Everything lands on the beat: check placements against the timeline's beat grid and sync offsets.

Never use the optional Gemini critique (`earshot llm` / `llm_critique`) unless Q has set his own GEMINI_API_KEY and explicitly approved an upload for that run. Never write any API key into a file.

## Max mobilization: pull everything before building a style edit (standing rule)

When Q asks for a video in a creator's style (or any style-named edit), run the full mobilization sweep in the `pwc-max-mobilization` skill BEFORE building: every matching skill, every folder holding the style or its directions, every reference form (videos, frame shots, screen recordings, screenshots, written teardowns), Q+Kiya assets first (substitution allowed per Q Nov 12 rule; ask Muse when unsure), the full tool bench (Earshot, /watch, Higgsfield, CapCut, open-source pool, licensed sounds), the agent team, and live pulls for anything missing. Partial builds from partial knowledge fail Q's order. Deliveries open with a one-block mobilization report.

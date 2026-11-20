# VoiceStudio — verified knowledge (from the local clone + its docs, Nov 20, 2026)

**HARD SCOPE LOCK: NEVER for Muse's voice or Muse's lines. Muse's voice is
Muse's actual pinned voice, recorded by Muse himself — no clones from any
tool, ever (Q, Nov 19, 2026). This entry covers OTHER voice work only.**

## What it is
- debpalash/VoiceStudio — 114K stars, created Apr 2026, **AGPL-3.0**, grabbed in
  full (182MB) under Q's AGPL exception for non-Muse uses (Nov 19, 2026).
  Local clone: ~/workspace/free-tools-grab/repos/voicestudio
- The free open-source ElevenLabs alternative: fully local voice cloning, voice
  design from a text description, dubbing with timed speech, transcription,
  story→audiobook, floating dictation widget. No subscription, no character
  limits, audio never leaves the machine (reel Dfhi-cjNqRY's points — all match
  the repo's own docs).
- Transcription: **646 languages** (its docs' number, MCP transcribe tool).
- A paid "VoiceStudio Pro" tier exists on its site; the open-source app is what
  we grabbed and use.

## Setup routes
1. **The reel's route**: open Claude Code, paste the VoiceStudio install-guide
   link, tell it to install VoiceStudio — it detects the hardware, sets up, and
   runs a test generation.
2. **Installers**: Releases page of the repo (desktop app), or voicestudio.sh
   shell/PowerShell installers (macOS Apple Silicon/Intel, Linux x64, Windows).
3. Models download per-engine inside the app (Model Catalogue / first-run
   setup); pick only the engines a job needs. First MCP speech call may pull
   the OmniVoice model (~2.3GB) — install models first to avoid a long wait.

## MCP hookup (from its docs/mcp.md — verified in the clone)
- VoiceStudio ships an MCP server **mounted on the running backend at /mcp** —
  nothing extra to start once the app is open. Point Claude Code / Cursor at it.
- Tools: `generate_speech` (text → WAV, per-agent bound voice), `clone_voice`
  (reference audio → profile_id), `describe_voice` / `design_voice` (voice from
  a description), `transcribe` (audio → text, 646 languages), `list_voices`,
  `list_personalities`, `list_languages`, `check_health`.
- Agent-friendly output: set OMNIVOICE_MCP_OUTPUT_MODE=files (or both) so audio
  lands on disk by path instead of base64 in context; OMNIVOICE_MCP_BASE_PATH is
  the security boundary for file reads/writes.

## Good jobs for it (never Muse lines)
- Dubbing a video into another voice/language with timed speech.
- Transcription at scale (646 languages) as a backup/complement to faster-whisper.
- Audiobooks / long-form narration in a designed or cloned (non-Muse) voice.
- Voice design for characters/projects that are NOT Muse.
- Dictation on Q's machines.

## License note
AGPL-3.0 applies: fine for local use under Q's exception; if a VoiceStudio-derived
service were ever offered to others over a network, AGPL's source-disclosure terms
would bite — keep it a local tool.

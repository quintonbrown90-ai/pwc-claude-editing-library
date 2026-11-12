# AUDIO — Earshot: EARS for Claude Code (Claude hears its own edits — REAL TOOL, SCAN PASS)

Source: Nick Saraev (@nick_saraev) — reel DfRVXxePAl2 "Comment SOUND to get this Free AI Tool to add pro sound effects to your Claude video edits" (Batch 35, filed Nov 12, 2026 at Q's direct order: "Install this into Claude code so it can hear and give me accurate sounds when editing"). The comment-gated link was NOT chased; the repo was identified from the caption + public search and GitHub-verified. Full decode + scan: `research/video-harvest/instagram/batch-35/DECODE.md`.

## The real tool (v0.4.1 — this part is the doctrine + install map)
- **Source:** `Leonxlnx/earshot` — https://github.com/Leonxlnx/earshot (Leon Lin). v0.4.1, commit 4ac3d2a, 4,549 stars / 290 forks at harvest (Nov 12, 2026).
- **LICENSE: MIT** — permissive; install approved under Q's rules. NOT parked. Its two listening models are permissive too: CLAP `laion/larger_clap_general` (Apache-2.0), AST `MIT/ast-finetuned-audioset-10-10-0.4593` (BSD-3-Clause).
- **SCAN PASS (Nov 12, 2026):** quarantine clone read. Verdict CLEAN:
  - No telemetry/analytics endpoints. Network is exactly: HuggingFace download of the two pinned models (safetensors only, cache-only after `doctor --fetch`, `EARSHOT_OFFLINE=1` blocks all downloads) and the OPTIONAL Gemini critique — off unless `GEMINI_API_KEY` is in the environment AND the caller explicitly consents (`--yes-upload` / consent=true).
  - Keys are environment-only, sent only as a header to Google, never printed/logged/stored; the MCP code itself instructs never to write a literal key into `.mcp.json`.
  - All subprocess calls in the package are list-form ffmpeg/ffprobe; no shell=True.
- **Staged in the library:** upstream agent skills verbatim — `skills/earshot/` (SKILL.md byte-identical) + `skills/real-sound/` (SKILL.md + references + scripts + templates, diff-clean).

## What earshot does (the mechanism)
Claude Code can write the code that edits a video but cannot hear the result — every SFX it adds is a guess from a filename and a duration. Earshot turns sound into evidence Claude can reason about, locally on CPU, as a CLI, a Python API and an MCP server:
- `describe / match / rank / find` — what a file sounds like in words (calibrated z verdicts), how well it fits a description, the best clean moment inside a long recording.
- `timeline FILE [--video V] [--cues C]` — a second-by-second listening transcript of a whole film: events (time, level, tag), sections, loudness, beat grid, and **sync of sound to picture cuts** — it names the cuts that have NO sound at all, with exact times.
- `sheet` — an annotated PNG (frames, labelled events, spectrogram, waveform, loudness, sync markers) the agent reads with its eyes.
- `critique` — a scorecard against a profile of 7 professional launch films, with timestamped fixes.
- `sfx` — a bank of **252 sound effects stored as code** (whooshes, hits, sub drops, clicks, taps, pops, dings, risers, glitches, shutters, mallet notes…), rendered by id in seconds with `--dur / --apex / --pitch` aimed at the picture, every render audited (clicks, cut tails, clipping, ring). No models, no network.
- `kit` — a whole film's kit: one bank sound per role with measured onset/peak/end. The **`launch` preset** is the PWC-relevant one: each effect is mixed against the music bed (3–10 dB over the bed, not a fixed level), placed against the cut (taps lead it, whoosh peaks land after it), with minimum-gap spacing for runs.
- `forge` — when nothing in the bank fits, Claude writes a new sound as a physical-synthesis recipe, renders takes, and improves it by listening back.
- `fit` — translate a real recording into code it can vary.
- `realness` — real/pro-produced vs code-synthesized check on any candidate sound.
- `measure` — objective meters only (LUFS, true peak, LRA, spectrum, tempo/key), no models.

## Install — Claude Code (the working home; do all four steps once)
Needs **uv** and **ffmpeg/ffprobe** on PATH. CPU only, no GPU.
```bash
# 1. Install the tool (uv takes torch from the CPU-only wheel index)
uv tool install "earshot[mcp] @ git+https://github.com/Leonxlnx/earshot"

# 2. Download the two listening models up front (~1.1 GB, pinned, safetensors)
earshot doctor --fetch

# 3. Register the MCP server with Claude Code (user scope = every project;
#    models stay loaded between calls — without MCP every CLI call reloads them, ~20–40 s each)
claude mcp add earshot --scope user -e EARSHOT_THREADS=3 -- earshot mcp

# 4. Install the two agent skills
git clone https://github.com/Leonxlnx/earshot /tmp/earshot-src
cp -r /tmp/earshot-src/skills/earshot ~/.claude/skills/
cp -r /tmp/earshot-src/skills/real-sound ~/.claude/skills/
```
Then restart Claude Code. On a slow machine start it with `MCP_TIMEOUT=60000`. Verify: `earshot doctor --load`, then in Claude Code ask for an earshot `sfx_list` — the tools (measure, describe, match, rank, find, compare, ab, realness, timeline, sheet, critique, doctor, sfx_list, sfx_render, kit_render) should appear.
- **This library's repo route:** `pwc-claude-editing-library/.mcp.json` also registers the earshot server (alongside Higgsfield), so any Claude Code session opened on that repo picks it up — the binary install (steps 1–2) is still a one-time step on the machine, and the first session needs the one-tap MCP server approval.
- Update later with `uv tool upgrade earshot`.

## The PWC overlay (how this binds in Q's setup)
1. **Earshot is the EARS layer, sibling to /watch (the EYES layer, part #320).** /watch proves what a video shows; earshot proves what an edit sounds like. Neither replaces a style skill — they feed Sky/CCC/Viral/Devin/avatar lanes with evidence.
2. **AUTO-ACTIVATION (Q's Nov 11 rule):** no trigger words. On ANY edit job in Claude Code, after the first full render Claude must run the listen-back pass by default: `timeline` + `critique` on the exported file, fix what it flags, re-render, re-listen. A render is not "done" until it has been heard.
3. **Sound-density rule, now checkable:** Q's standing standard is sound on every imagery entrance AND exit, layered landings, accents on statement lines and number landings, a visual event every ≤2s. Earshot's timeline names every cut with no sound — that list is the fix list, not a suggestion.
4. **Placement standard:** use the `launch` kit preset logic for PWC films — effects ride 3–10 dB over the music bed, taps/knocks lead the cut, whoosh peaks land after it, runs keep their minimum gaps; pull the music down before a hit/drop instead of ducking under every effect.
5. **Bank first, local library second, forge last:** prefer the 252 bank (instant, audited) for motion-graphics SFX; Q's local licensed library (~1,250 files) stays the source for real recordings — run earshot `rank/find/describe/realness` over candidates instead of guessing from filenames. `forge`/`fit` only when neither fits. Epidemic Sound stays declined.
6. **Honesty limits (upstream's own, keep them):** earshot hears sounds, not words — it does NOT transcribe speech, judge taste/emotion, or check licences/provenance. Q still listens to every final render. The bank sounds are code-made originals (15 fitted from CC0 recordings, credited upstream), not recordings — when a brief wants recorded sound, use the `real-sound` skill process.
7. **Gemini critique stays OFF** unless Q sets his own GEMINI_API_KEY and explicitly approves an upload for that run. Never pass `--yes-upload` on Q's behalf.

## GAPs
- **G-B35-1:** Claude Code is not installed on Muse's own machine, so — same as the Higgsfield MCP (Nov 11) — the registration was committed to Q's library repo `.mcp.json` and the one-time binary/model install runs on Q's machine (or inside his first Code session, using the paste-ready prompt in the Batch 35 folder). Muse verified the install route end-to-end on its own VM (doctor + sfx render + kit) — see DECODE.md.
- **G-B35-2:** First listen is heavy: ~1.1 GB model download once; a 60–90 s film takes ~1.5 min of CPU listening. Budget it into render QC, don't skip it for speed.
- **G-B35-3:** Reel says "over 250 professional sound effects" — accurate count is 252, but they are professional-STYLE sounds made in code, not professional recordings. Wording kept honest here.

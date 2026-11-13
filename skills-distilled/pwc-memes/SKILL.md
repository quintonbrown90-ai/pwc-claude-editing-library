---
name: pwc-memes
description: "PWC MEMES — Q's signature meme device for his video edits: meme pop-ups, poster slams, full-frame transition memes, and reaction cutaways placed the way top YouTubers place them. Fires automatically whenever Q asks to add memes to a video in plain language — 'add memes', 'put memes where they fit', 'add memes where appropriate in this video', meme pop-ups, reaction memes, GIF inserts, funny cutaways — on Claude Code or web, in any lane (Sky, Devin, Viral, CCC, avatar, general), no trigger words needed. Carries the placement, timing and audio grammar, the banked-asset catalog (Nov 6 pack + memes-bank), and the CLEAN-ONLY law: every meme is profanity-screened before banking or use — no cursing anywhere, ever. Memes are emotion and punctuation — never proof, never over Q's face, never on scripture beats."
---

# PWC MEMES — Q's signature meme device

Q's order (Nov 12, 2026): memes become one of HIS things — the way the little-head clusters he took from Sky became his. When he says "add memes" or "add memes where appropriate in this video," this skill is the whole system: which meme, which placement, which beat, which sound — and the clean-only law over all of it. It builds on his Nov 6, 2026 meme pack and expands it with the full-frame transition meme (Q, Nov 12).

Full doctrine lives beside this file: **MEME-USAGE-GRAMMAR.md** (placement/timing/audio/frequency law) and **MEME-CATALOG.md** (every banked asset + the screening queue). Read both before placing a single meme.

## The CLEAN-ONLY law (absolute)

- **No cursing anywhere in any meme asset** — not in its audio, not in burned-in text. Q's content is clean and faith-aligned.
- Every meme is **screened before it is banked and before it is used**: transcribe (faster-whisper) → profanity scan → verdict CLEAN / SEGMENTS (bank clean spans only) / PARKED (never banked). Pipeline: `screen-and-bank.py` in this skill. Unscreened = unusable, no exceptions.
- Faith-clean beyond profanity: no vulgar or mean-spirited memes. **Scripture beats get NO memes** — verse plaque + soft chime or silence only.

## The VARIETY law — no same-ol' memes (Q, Nov 13, 2026)

- **Rotate.** Never reuse the same meme/GIF clip in back-to-back videos or twice in one batch unless Q explicitly asks for that exact meme. The audience must not be able to predict which reaction is coming.
- **Check the ledger before choosing.** MEME-CATALOG.md carries a rotation ledger + cooldown list. Pick the least-recently-used clip that fits the beat; clips on cooldown are last resort only, behind every unused option.
- **The signature sound pairings stay** (cha-ching = money, crickets = nothing happened — that consistency is by design, §5 of the grammar). What rotates is the CLIP and which beats get a meme at all — do not let one visual or one beat-type become the predictable formula.
- **If the bank has no fresh fit, get one.** Source and screen a NEW clean clip for the beat (per the pipeline below) instead of repeating a familiar one — or skip the meme. A repeated meme is a defect; a missing meme is not.
- **Log every use.** Each edit that places a meme records clip + video + date in the catalog ledger, so the next edit can see what is burned.

## The four placements (grammar summary)

1. **Pop-up (default — Carter grammar).** Small reaction clip/GIF in the empty space above or beside Q's head, on the exact punch beat, while he keeps talking. ~15–30% of frame width, 0.5–3s, matched sound in AND out.
2. **Poster slam (rationed — Kilgore variant).** One reaction GIF poster-size (top ~40–45% of frame), ~1.5s, hard cut, on the single biggest punch word. Max ~2 per video.
3. **Full-frame transition meme.** He finishes a line → hard cut to the meme full-frame for 1–3s → back to him. Memes are paragraph breaks: they land AFTER a completed thought, never mid-sentence, never over speech that carries information. SpongeBob time cards are the story variant — max 1 per video, real time jumps only.
4. **Reaction cutaway / emotion underline.** A 0.8–2.5s reaction right after a line — the meme reacts FOR the viewer (shocked face after the number, slow-clap after the win, side-eye after the bad advice). Pop-up or brief full-frame.

## Timing, audio, frequency (the short law)

- **Beat-locked:** lands ON the punch word or ≤2 frames after the line ends. Gone before the next sentence needs eyes.
- **Every pop has a matched sound, in AND out** — a silent meme is a failed event. Pairings: `MEME_GRAMMAR_45_PAIRINGS.md` (cha-ching = money, vine boom = the single biggest claim only, record scratch = "wait—what", buzzer = wrong way, ding = right way, crickets = nothing happened). SFX ≈ −12 dB under the voice; meme clip audio muted/ducked while Q talks, full level only when the meme owns a full-frame beat and he isn't speaking. Real recordings only — never synthesized. One sound family per job, consistent across videos = signature.
- **Frequency:** emotion peaks only — a meme that doesn't answer the exact line being spoken is a defect, cut it. Short-form rhythm ≈ one meme per 20–45s at most (typically 2–4 per 60–90s video), never two within ~5s, never under the CTA.
- **Position:** NOTHING over Q's face, ever — empty space or no meme. Inside the safe zone, clear of the caption band. Do NOT recolor memes into PWC teal/gold/navy — recognition is the joke; brand dressing goes on Q's own cards around the meme.

## What memes never do

Never substitute for proof (receipts/payouts stay real, sharp, blur-law applies). Never imply a person in a meme endorses Q/PWC. Never on scripture beats. Never wallpaper.

## Where the assets live

- **Nov 6 pack (the working bank, 138 files):** `~/workspace/your_files/for-claude-assets/07_memes_gifs/` — `library/time_cards/` (4 SpongeBob cards) · `library/green_screen_keyed/` (32 keyed reaction clips by emotion) + `green_screen_pairs/` (COLOR/MATTE) + `green_screen_raw/` · `library/sounds/` (applause, bruh, crickets, ticking clock) · `refs/` (7 study reels) · `README_MEMES.md` (Q's Nov 6 rules) · `MEME_GRAMMAR_45_PAIRINGS.md` (the 45 pairings). Refs copied at `~/workspace/claude-editing/assets/memes/refs/`.
- **New bank (Nov 12 on):** `~/workspace/claude-editing/memes-bank/` + its `MEME-CATALOG.md`. New finds land in `~/workspace/claude-editing/research/memes/incoming/`, get screened by `screen-and-bank.py`, cut at 720p (crf ~26, AAC kept), named `meme_<emotion>-<descriptor>_<nn>.mp4`, banked, and catalogued with source + timestamps + clean-verified note.
- Q's five Nov 12 YouTube picks are in the catalog §B — **ingestion blocked Nov 12 (YouTube 429 + bot check on anonymous download); NOT screened, NOT usable** until pulled via Q's signed-in browser (screen-record) and run through the pipeline.

## Execution in an edit

CapCut finishing: meme as Overlay (green-screen keyed clips: Cutout → Chroma Key), entry/exit sounds on their own audio track under the voice. Code renders: same grammar — the placement, timing and levels above are the spec regardless of tool. When a needed reaction isn't in the bank, say so and source it (GIPHY sticker search / green-screen channels), then SCREEN it before use — a meme Q didn't ask for still obeys the clean-only law.

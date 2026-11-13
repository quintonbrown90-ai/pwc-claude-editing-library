# MEME CATALOG — Q's banked meme assets

The bank has two homes:
- **THIS folder** — `~/workspace/claude-editing/memes-bank/` — new memes banked from Nov 12, 2026 on (Q's YouTube-sourced picks + future finds), each one profanity-screened before banking.
- **The Nov 6 pack** — `~/workspace/your_files/for-claude-assets/07_memes_gifs/` — the original bank (138 files, 6.7 GB, registered in the library INDEX; refs copied at `~/workspace/claude-editing/assets/memes/refs/`). Its usage rules are in its `README_MEMES.md`; its 45 beat→visual→sound pairings are in its `MEME_GRAMMAR_45_PAIRINGS.md`.

**The law for every entry in both homes: CLEAN-ONLY.** No cursing in audio or on-screen text, no vulgar/mean memes. Screened before banking, re-verified before use. Grammar: `MEME-USAGE-GRAMMAR.md` (research/memes/ + the pwc-memes skill).

Naming for new banks: `meme_<emotion>-<descriptor>_<nn>.mp4` (720p, crf ~26, AAC audio kept).

---

## A. Banked and ready (Nov 6 pack — faith-clean per Q's Nov 6 rules)

### A1. SpongeBob time cards — `07_memes_gifs/library/time_cards/` (full-frame transitions, silent)
| File | Duration | Emotion / moment | Best use |
|---|---|---|---|
| card_a_few_moments_later.mp4 | 1.77s | deadpan time-skip | transition meme after a setup line, before the result |
| card_one_hour_later.mp4 | 1.37s | time-skip | transition — story jumps an hour |
| card_2000_years_later.mp4 | 2.27s | exaggerated time-skip | transition — comic exaggeration of a long grind |
| card_flashback.mp4 | 1.37s | rewind to the past | transition into a story/flashback beat |

Rule: max 1 time card per video, only on a real story jump; add a matched cue (cards are silent).

### A2. Keyed green-screen reaction clips — `07_memes_gifs/library/green_screen_keyed/` (32 .mov, chroma-keyed — drop over footage as pop-ups / cut-out characters)
Emotion coverage on file: **angry** (cat, growling dog) · **clap/applause** (black cat clapping, dog slow-clap) · **confused** (Nice Guys confused) · **crying** (monkey, sausage) · **dance/celebration** (cat, Drake) · **laughing** (Aleks laughs, fairies) · **money** (cat counts money, Kai Cenat "take my money") · **no-no-no** (Susan Dell, Uncle Ash) · **running away** (cat, Made) · **shocked** (BBY wow guy) · **side-eye/sus** (fairy goblin, dirty look) · **sleepy/bored** (monkey, tired princess) · **thumbs-up** (cat) · **yes/finally** (BurntPeanut) · **viral-top set** (Caleb dancing, cat claps + handshake, dog handshake, fairies gossip, "I like that", kittens dancing, Humantix, wizard cat slams keyboard).
Same 32 also exist as COLOR+MATTE pairs in `green_screen_pairs/` (64 files) and raw in `green_screen_raw/` (34 files) for editors that key/matte differently.
Best uses: pop-up (§3.1 grammar) and reaction-after-line (§3.4). These are silent visual reactions — pair with a banked/licensed SFX per the 45-pairings doc.

### A3. Meme sounds — `07_memes_gifs/library/sounds/`
| File | Use |
|---|---|
| meme_applause.mp3 | win / yes-moment punctuation |
| meme_bruh.mp3 | disbelief at a bad take (rationed — match weight) |
| meme_crickets.mp3 | "nothing happened" / awkward-silence beat |
| meme_ticking_clock.mp3 | waiting / countdown tension under a count |

Named in the Nov 6 refs as the iconic five to also hold from cleared sources: Bruh ✓ · Vine Boom (biggest-claim only) · iPhone Marimba · Bad Gas · the "Morality" sting. Pull additions only from cleared/licensed sources — never synthesized, never ripped over a profanity-flagged source without screening.

### A4. Reference reels — `07_memes_gifs/refs/` (study, not drop-in assets)
7 reels catalogued in research/memes/usage-examples/USAGE-EXAMPLES-NOTES.md §3 (Carter pop-up grammar, Kilgore poster slam, green-screen method, GIPHY method, iconic sounds, SFX-pack demo, time-card source).

---

## B. Q's Nov 12, 2026 picks — ⏳ INGESTION BLOCKED, NOT YET SCREENED, DO NOT USE

Q sent five YouTube links on Nov 12, 2026 to be downloaded (or screen-recorded), screened, cut, and banked here. **On Nov 12, 2026, anonymous yt-dlp downloads were blocked by YouTube (HTTP 429 + "Sign in to confirm you're not a bot")**, and per the standing 429 hard-stop rule no retries or alternate download routes were attempted. Nothing was downloaded, so **no profanity verdict exists for any of the five** — they stay OUT of the bank and out of edits until they are pulled (Q's signed-in browser screen-record is the route he named) and run through the screening pipeline (`screen-and-bank.py` in the pwc-memes skill: transcribe → profanity scan → CLEAN / SEGMENTS / PARKED verdict → cut the clean moments → bank + add rows here).

| # | Source | What it appears to be (web identification only) | Duration | Verdict |
|---|---|---|---|---|
| 1 | https://youtu.be/35KDnej1hlI | unidentified — cited around the web only as a "Meme" embed; title not confirmed | unknown (download blocked) | ⏳ NOT SCREENED |
| 2 | https://youtu.be/omV5m5ZXkLg | "100 POPULAR MEMES FOR FUNNY EDITING \| FREE DOWNLOAD" — Demonal — a 100-clip meme compilation made for editors | unknown (download blocked) | ⏳ NOT SCREENED — compilation: expect a SEGMENTS verdict (bank clean moments only) once pulled |
| 3 | https://youtu.be/G3KoTo4ozEw | unidentified from public web records | unknown (download blocked) | ⏳ NOT SCREENED |
| 4 | https://youtu.be/r94vuvwUSkY | a long-circulating single reaction clip (embedded across forums since ~2017; an Imgflip GIF cut from it is captioned around a "the popular kid after the weird kid stutters" joke) — exact YouTube title not confirmed | unknown (download blocked) | ⏳ NOT SCREENED |
| 5 | https://youtu.be/17QY_GmVuFk | unidentified from public web records | unknown (download blocked) | ⏳ NOT SCREENED |

When a source lands in `research/memes/incoming/`, run the pipeline, then replace its row above with the real catalog rows for each banked clip (name, source timestamp in/out, duration, emotion, best uses, clean-verified note).

---

## C. How a meme gets into this catalog (the pipeline)
1. File lands in `~/workspace/claude-editing/research/memes/incoming/` (download or Q's screen-record).
2. `screen-and-bank.py` transcribes it (faster-whisper, word timestamps) and scans the transcript for profanity.
3. Verdict: **CLEAN** (bank whole/as-is moments) · **SEGMENTS** (bank only the clean spans, with in/out times recorded here) · **PARKED** (profanity pervasive — never banked; noted here with the reason).
4. Cut at 720p, crf ~26, AAC audio kept; name `meme_<emotion>-<descriptor>_<nn>.mp4`; add the row.
5. Note: transcription catches SPOKEN profanity. Burned-in text is checked by eye on the frames before banking — a clip with a clean transcript but profane on-screen text is PARKED or cut around, never banked whole.

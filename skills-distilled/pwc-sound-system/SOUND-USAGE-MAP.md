# SOUND USAGE MAP — Doctrine: WHEN Each Sound Is Used

> **Status: FINAL — coordinator-finalised Nov 13, 2026.** Lane 4 of Q's sound-system build, finished in the Nov 13 completion pass.
> Every rule below carries an evidence label. Nothing in this document is presented as fact without a source in Q's own system.
>
> **Labels**
> - **[MEASURED]** — measured from creator data on disk (frame / RMS / spectrogram / word-timing evidence).
> - **[TUTORIAL]** — from explainer / tutorial content in Q's library (sound-design reels, research syntheses, skill doctrine). A teaching claim, not a measurement of Q's target creators.
> - **[Q-ORDER]** — Q's standing rules / adopted recipes. Binding on PWC builds even where they deliberately diverge from the measured source grammar.
>
> **Core honesty rule inherited from the sources:** where Sky or Devin is *sparse or silent*, this map says so. Q's denser PWC layer is always labelled a divergence, never re-attributed to Sky or Devin.

**Principal sources mined for this draft**

- Sky: `claude-editing/styles/sky-edit-style/SKY-TEARDOWN-MASTER.md` §7 (Batch 36, 49 reels), `STYLE-GRAMMAR.md` §7, `SKY_STYLE.md` §6 (in `examples/sources/`), per-reel notes e.g. `notes_Dez4fPJCR74.md`, `notes_DfPxqFPAY4_.md`, and the 48 soundmaps in `research/video-harvest/instagram/batch-36-sky-completion/soundmaps/`.
- Sky/PWC sound rulebook: `SOUND_SYSTEM.md` v2 + v2.1 (2026-11-06, in the PWC-Videos sparse clones, e.g. `~/workspace/remix-clone/SOUND_SYSTEM.md`) — built from 6 sound-design reels Q sent.
- Devin: `your_files/devin-exact-nov13/DEVIN-EDITOR-BRAIN.md` §6 (223 videos downloaded, 25 reels on a 0.5 s grid, 6 priority reels machine-profiled).
- Applied Devin build: `your_files/locked-doors-latest/locked-doors_sound-cue-sheet.md` (Locked Doors v7 picture, 68.17 s — real sounds laid + sounds still needed, listed per timestamp).
- Meme grammar: `your_files/for-claude-assets/07_memes_gifs/MEME_GRAMMAR_45_PAIRINGS.md` (2026-11-05 cross-platform research synthesis).
- Nov 2 recipes: `~/memory/2026-11-02.md` — the signature round (line ~208 / ~439) and the talking-head viral-style adopted recipe (line ~446).
- Transitions: `your_files/launch-viral-forms-nov12/VIRAL-FORMS-LAUNCH-PACK.md` + `TRANSITIONS-SHEET.md`; Kien decode `claude-editing/research/video-harvest/instagram/batch-24-capcut-transitions/DECODE.md`.
- Earshot / real-sound doctrine: `claude-editing/skills/earshot/SKILL.md` and `claude-editing/skills/real-sound/SKILL.md` + its launch-video sound map (library part #328).
- Viral / Yapping: `claude-editing/styles/viral-edit-style/README.md` (pointer only — see §6 gaps) and `claude-editing/styles/yapping-edit-style/STYLE-GRAMMAR.md` §8.

---

---

## 0. The bank this map drives

The sounds live in the **PWC sound bank**: **1,975 distinct real recordings, 448 MB, 19 categories**, every file with provenance in `catalog.csv` (name, category, duration, source, provenance, original name, best use, md5, size). Locations: library repo (this skill's home), PWC-Videos `assets/sfx-system/`, and the build folder `~/workspace/sound-system-build/bank/`.

| Bank category | Files | Map sections that spend it |
|---|---:|---|
| clicks | 188 | §3.3, §4.4 — cursor clicks, taps, latch/lock-ins, row clicks |
| ui-notifications | 175 | §3.3, §4.4, §4.8 — notification dings, selects, text tones |
| whooshes-swooshes | 130 | §2.2 — moves, fly-ins, zoom-throughs, spinbacks |
| intros-stingers | 127 | §4.8 — logo stings, openers, fanfares |
| swipes-slides | 120 | §2.2, §4.4 — swipes, page turns, writing strokes, card slides |
| pops | 116 | §3.3 — reveals, chips, cards, icons |
| dings-bells | 98 | §4.5, §4.6 — confirmations, takeaway bells, soft chimes |
| risers | 82 | §2.2, §4.3, §4.7 — builds into reveals, counters, section changes |
| typing | 73 | §4.1, §4.4, §4.8 — typed text, CTA typing chains |
| glitch | 73 | §2.2 — glitch bursts/tears, scan/process textures |
| ambience-beds | 65 | §5 — cleared beds at lane levels; room tones |
| ticks | 47 | §4.1, §4.3 — per-word ticks, count-up runs, clock ticks |
| money | 44 | §4.3 — coins, registers, chips under money talk |
| buzzers-errors | 32 | §4.5 — wrong-way verdicts, errors, alarms |
| meme-sounds | 30 | §4.7 — screened meme reactions (never scripture, never proof) |
| camera | 17 | §2.2 — shutter/flash beats |
| outros | 17 | §4.8 — end-card hits, sting decays, tape stops, closing chords |
| impacts | 529 | §4.2, §4.7 — landings and the rationed big hit (mostly foley-weight variants; pick by weight, not by count) |
| misc | 12 | Deliberate leftovers (pack previews, two toilet recordings, 4 abstained foley one-shots, spray held pending a listen) — **not cleared for use without a listen** |

Bank laws that bind every section below: real recordings only (§1.5); the 22 loose unknown-origin `.wav` files from PWC-Videos `assets/sfx/` are banned and verified absent (0 of their hashes in the bank); SFX-Kit files carry the kit's own taxonomy mapping; 64 opaque-named files were placed by a labelled audio-feature pass. The Sky tick-tone still has **no ear-matched file in this bank** (§6.1) — the ticks category is for PWC/Viral lanes, not a Sky substitute.

## 1. Universal Laws

These hold across lanes unless a lane dialect in §5 explicitly overrides them — and the override is named.

### 1.1 A sound must be *caused* by something on screen

- Every sound sits on a picture event: a reveal, a move, a contact frame, a word, a cut that the grammar of that lane actually sounds. No decorative SFX with no visual cause. **[TUTORIAL — real-sound: "every sound caused by something on screen"; the soundtrack is built from a cue list computed from the picture]**
- The meme layer obeys the same law in its own words: "Every pop is motivated. The visual illustrates or reacts to the EXACT word being said at that moment… If the pop doesn't answer 'why this, why now,' cut it." **[TUTORIAL — MEME_GRAMMAR_45_PAIRINGS, universal rules]**
- SAY IT, SHOW IT has an audio twin in Q's builds: whatever is shown gets its sound in Q's dense lanes; whatever is only talked about does not get an invented sound effect. **[Q-ORDER — SKY_STYLE standing orders, Nov 7; SOUND_SYSTEM v2.1 coverage rule]**

### 1.2 "Sound on every visual change" is a Q law — not a Sky or Devin fact

This is the single most mis-cited rule in the system, so the draft states both sides:

- **Q's law (dense lanes):** sound on **100% of device entrances AND exits** — tick/pop on landings and exits, stamp on verdicts, riser + ding on counters/charts, key clicks on headline words, typing on hook captions, soft hit on hero words, unlock on the lock; pitch variants per event; `sfx_gain ≈ .6` in the original spec, `1.6` bus in v2.1 measurement. **[Q-ORDER — STYLE-GRAMMAR §7 "Q SFX (SKY-PLUS target)"; SKY-TEARDOWN-MASTER §7.4, §12]**
- **Q's Nov 2 signature wording:** "SOUND ON EVERYTHING — every caption word gets a micro-tick/pop, plus a sound on every pop-up, example, diagram and movement ('that's how views stay with retention')." **[Q-ORDER — memory 2026-11-02, Q's signature round reviewing VIRAL-02]**
- **The measured source reality:** Sky's devices *sometimes land silent* (e.g. DevpJZLk6Km — photo pop, exhibit-in, list typing all land silent, measured), and Devin's dry reels run **one SFX per device, never stacked**. Q's 100% coverage is a deliberate SKY-PLUS divergence, kept on purpose. Never cite Sky or Devin as the source of 100% coverage. **[MEASURED — SKY-TEARDOWN-MASTER §12; DEVIN-EDITOR-BRAIN §6]**
- **Launch-film restraint counterweight (other genre, do not conflate):** the real-sound launch profile runs **about 5 designed effects per 10 s**, with hard cuts and cursor movement getting *nothing*. That is a launch-film norm, not a talking-head norm — it governs code-made launch/product films, not Q's talking-head lanes. **[TUTORIAL — real-sound SKILL, launch sound map]**

### 1.3 Silence is a choice, and each lane chooses it differently

- **Sky: no dead air.** Zero silences ≥0.25 s at −35 dB (and −50 dB) across the measured corpus; word gaps bottom out at room tone/breath; heads and tails are live room tone to the last frame. The corpus's single 1.37 s digital-silence tail (DP2_6r7DQ60, under a held closing headline) is logged as **a defect, not a device**. **[MEASURED — SKY-TEARDOWN-MASTER §7.3]**
- **Devin: verdict silence is grammar.** All three verdict X stamps in DLpgNYQMZlm are **silent (RMS 0.02–0.04)**; subtractions and verdicts "can be silent on purpose"; the Dfc 25→625 count-up has **no tick track**. In the dry family, phrase gaps fall to RMS 0.01–0.04 without hitting true digital silence (near-silence spans ≥0.25 s under −38 dBFS: DLpg 4, DSh 1, all other priority reels 0). **[MEASURED — DEVIN-EDITOR-BRAIN §6]**
- **Faith beats: near-silence is the cue.** After density, silence/near-silence on a gratitude/testimony beat "reads as weight." No comedy cue touches scripture (see §4.6). **[TUTORIAL — MEME_GRAMMAR §12, faith beats]**
- **PWC ending gate:** last voice → end card **≤ ~1 s** on every export. The Nov 2 backyard finals carried 2.2–3.4 s of bed-only tail and Q flagged the ending as "messed up" — freezedetect does not catch a moving-but-dead tail. **[Q-ORDER — SKY-TEARDOWN-MASTER §8.1/§12; memory 2026-11-02 ending check]**
- **Real-sound logo law (launch films):** music stops/filters down, **0.2–0.7 s near-silence**, then ONE soft note in key, tail to silence. **[TUTORIAL — real-sound launch map]**

### 1.4 Levels — everything sits under the voice (talking-head lanes)

Voice is the reference. All figures below are *relative to voice* unless stated as an absolute master level.

| Layer | Level | Label / source |
|---|---|---|
| Q voice master | Static gain only, to **−14.5 LUFS** (Sky lane). Real-sound launch master: **−14 LUFS, true peak ≤ −1 dBTP** after AAC, LRA 5–9 LU | [Q-ORDER — SKY_STYLE §6; TUTORIAL — real-sound] |
| Music bed, Q talking-head builds | **≈ −28 dB under speech**; Sky engine spec: constant quiet bed, `music_vol .045`, gentle duck only | [Q-ORDER — STYLE-GRAMMAR §7; SKY_STYLE §6] |
| Per-word ticks (Nov 2 adopted recipe) | **28–32 dB under voice peaks**, pitch-varied, downward drift per sentence. Built exemplars measured **−29.0 to −30.0 dBFS** (37–143 ticks per backyard final) | [Q-ORDER — memory 2026-11-02 line 446; MEASURED on Q's own builds, same file] |
| Emphasis POP (Tier 2) | Hotter than the tick — yapping grammar quantifies **~5 dB hotter**; Nov 2 recipe says only "hotter POP on Anton emphasis words" (no dB figure in the recipe itself) | [Q-ORDER — memory 2026-11-02; TUTORIAL/field device — yapping STYLE-GRAMMAR §8] |
| Routine SFX bus (SOUND_SYSTEM v2.1, measured in L1 vs surrounding voice) | keys **−9 dB**, pops **−11 dB**, swish/right-ding **−6 dB**, whoosh **−9.5 dB**, shutter/tick **−11 dB**, impact **−12 dB**, typing **−25 dB** (texture). QC: fail any kind sitting more than **−16 dB** down, except risers and typing — the old ~−14.5 dB-down bus was "effectively silent on phone speakers" | [MEASURED on Q's build — SOUND_SYSTEM v2.1] |
| Meme / routine SFX (research synthesis) | **≈ −12 dB relative to voiceover**; build a hierarchy — routine pops/whooshes quiet, reveals/booms/buzzers louder | [TUTORIAL — MEME_GRAMMAR, citing Submagic / SFXVault guides] |
| Keyword sting (Q signature) | Fixed 3-note pluck **E5 (659.25 Hz) → G5 (783.99 Hz) → C6 (1046.50 Hz)**, ~0.5 s, **~16 dB below voice peaks**, FFT-verified at −16.00 dB in the Nov 2 finals | [Q-ORDER + MEASURED on Q's builds — memory 2026-11-02] |
| Effects over a *music* bed (music-led films only) | Effects ride **3–10 dB over the music** (not over voice); duck the music **6–12 dB for 0.3–0.5 s** before a hit/drop/big whoosh and restore on the hit. Do not duck under every effect | [TUTORIAL — earshot SKILL, Loop 5 levels] |
| Sky tick-tones (source grammar) | Band peaks **−19…−31 dBFS** against a −17…−20 dBFS broadband voice — i.e. at or below voice level, audible mainly in inter-word gaps. That faintness is why frame-based passes missed them | [MEASURED — SKY-TEARDOWN-MASTER §7.2] |
| Devin bedded reel (Dd3) | Continuous bed under all 39.8 s; **whole-mix RMS −16.0 dBFS, peak −0.87 dBFS**, zero silences at −35 dB/0.15 s or −40 dB/0.25 s. Note: this is a whole-mix figure, *not* a bed-under-voice offset — do not convert it into a "−X dB under voice" rule | [MEASURED — DEVIN-EDITOR-BRAIN §6] |

### 1.5 Real recordings only — no code-synthesised stand-ins presented as real

- Real-sound doctrine: the soundtrack is built **only** from real, professionally recorded/produced audio; "code selects, trims, places, levels, pans, EQs, pitches by resampling, time-stretches the music and masters; **code never generates a sound**." **[TUTORIAL/doctrine — real-sound SKILL]**
- Earshot gate: before using a trim where real/pro-produced sound is wanted, run `realness`; do **not** use a "likely code-synthesised" trim, and read the evidence on an "uncertain" one. Thresholds differ by length (clips ≤6 s: lo 0.17 / hi 0.77). Earshot's own forge bank sounds are code-made and must be labelled as such — "when the brief asks for recorded sound, use real-sound instead." **[TUTORIAL/doctrine — earshot SKILL, Loops 1/5]**
- Devin builds inherit the same law via Q's substitutions table: "Q's cleared library / Earshot bank only; **where no real sound exists, the beat stays silent** — Devin himself leaves verdicts silent." **[Q-ORDER — DEVIN-EDITOR-BRAIN §10]**
- Locked Doors cue sheet obeys it literally: the "still needed" list (§3/§4 below) was left as a *needs list* with the note "**Nothing was synthesised to stand in for them**." **[Q build record — locked-doors_sound-cue-sheet.md]**
- SOUND_SYSTEM reference clips are **for matching only** — they are other creators'/pack sounds and never go into a posted video; production sounds come from licensed/MIT banks (Splice on Q's account, earshot MIT bank, original synthesis only where the system explicitly allows it). **[Q-ORDER — SOUND_SYSTEM.md header]**
- The Sky tick-tone itself has **no ear-matched local file yet**: soundmaps mark it NO LOCAL MATCH VERIFIED — "do not substitute a generic tick without an ear match." Sourcing one is an open task (see §6). **[MEASURED/gap — SKY-TEARDOWN-MASTER §7.2]**

### 1.6 Beat-lock: sound lands on the event's frame, not near it

- Q's law: "Everything on beat — the captions, the motions, the visuals, the visual motions, the sounds, the transitions, everything." Every planned event is placed on a grid from the take's own audio; tolerance **≤1 frame (≈0.033 s)**; a deliberate off-beat needs a stated `off_beat_reason` or the validator fails the build. **[Q-ORDER — SKY-TEARDOWN-MASTER §8.2, BEAT-LOCK-SPEC Nov 12]**
- Sky's measured best supports the target: caption hard-cuts ≤1 frame on word onsets; D27/D37 figures pop 1 frame **on** each spoken number; tick-tones gate *inside* their animation windows — the tone starts with the counter/timer/draw it scores, **never on a cut**. No corpus-wide offset distribution exists on disk (see §6) — do not quote a "Sky median offset." **[MEASURED — SKY-TEARDOWN-MASTER §8.2]**
- Placement mechanics differ by sound class (earshot kit law): onset on the frame for hits/touches; the **peak** on a whoosh's apex; the **end** on a riser's hit. Runs keep their spacing (pops 114 ms, keys 87 ms minimum gaps in the kit defaults). **[TUTORIAL — earshot SKILL, Loop 5]**
- Real-sound launch map agrees by class: click on the press frame; pop/tick at **50% of the card's travel**; swish apex on the velocity peak; riser ending **30–250 ms before** the hit it serves. **[TUTORIAL — real-sound launch map]**
- Kien's transition rule: "The sound lands exactly ON the transition — never before, never after," and "one dramatic transition per video; the rest stay invisible." **[TUTORIAL — TRANSITIONS-SHEET, 3 rules]**

### 1.7 Consistency is the signature; variation is inside the family

- Same sound family for the same job every time = the viewer learns the language in one video and recognises it across videos. Vary the *variant/pitch* on every repeat, never the family. **[TUTORIAL — MEME_GRAMMAR universal rules; Q-ORDER — SOUND_SYSTEM: "Vary the variant on every repeat; pitch variants are generated automatically"]**
- One fixed brand sting for the logo outro, never changed, outranks every other signature device: "Sounds are remembered faster than fonts." **[TUTORIAL — MEME_GRAMMAR, meta-signature]** Q's instantiated version is the E5→G5→C6 keyword sting (§1.4) plus the end-card sting in §4.8. **[Q-ORDER]**
- Density ceilings that protect the signature: **one impact/boom per video max** in the SOUND_SYSTEM grammar ("you only need one per video, max"); vine boom rationed to the single biggest reveal (maybe twice); buzzer/boom spam is explicitly out. **[TUTORIAL — SOUND_SYSTEM table; MEME_GRAMMAR fit-check]**

### 1.8 What is banned / out of register (all lanes unless a lane note says otherwise)

- 2021-style constant loud whoosh/bass-hit on every cut — reads as fatigue and as AI-stamped against Q's human-made standard. **[TUTORIAL — MEME_GRAMMAR, "2026 correction / dynamic minimalism"]**
- Trending TikTok sounds that are platform-licensed only, and any meme audio containing profanity. **[Q-ORDER via MEME_GRAMMAR fit-check — clean-content law]**
- Chaotic gaming-edit grammar (airhorns, MLG stacks). **[TUTORIAL — MEME_GRAMMAR, "doesn't fit"]**
- A generic tick shipped *as* "the" Sky tick-tone without an ear match (§1.5). **[MEASURED/gap]**
- Key clicks on serif words as a generic fallback trigger — **banned in Sky v6** with the fallback's removal (headline-word clicks survive only as the specific SOUND_SYSTEM / SKY-PLUS pairings in §3, not as a default). **[Q-ORDER — STYLE-GRAMMAR §7 banned row]**

---

### 1.9 Satisfying first — the sound must feel good (Q, Nov 13, 2026)

- **The rule:** every sound in a PWC build — pop-ups, transitions, word beats, intros, outros — is chosen to be *satisfying*: low-key, tactile, ASMR-adjacent. Soft/rounded attacks, clean short decays, no harsh transients. Q's words: sounds that "stimulate the viewers and keep them longer and calm to watch and psychologically attached to the videos and what's going on." Applies to every lane and every editor (Claude Code, Muse, web Claude). **[Q-ORDER — Q, Nov 13, 2026, on approving the SkyFresh2 density v2 builds: "I love the satisfying sounds"]**
- **Selection criteria:** prefer firm-but-soft clicks, rounded pops, smooth airy whooshes, gentle typing, warm dings. Reject shrill, metallic-harsh, abrasive or startle-grade variants at the catalog-pick step, not at the mix step. The only exceptions are intentional verdict/error beats (buzzer, X thud) — and even those stay controlled, never ear-splitting.
- **Not calm-only — emotion-matched (Q's amendment, Nov 13, 2026):** satisfying is the *texture*, not the emotion ceiling. The layer must evoke whatever the video/beat is actually carrying — hype, tension, triumph, relief, humour, awe, conviction, warmth, sadness/weight — chosen per beat, not defaulted to calm. A money payoff should FEEL like a win; a silence beat should feel heavy; a funny beat should land the laugh. If the sound's emotion and the picture's emotion disagree, the pick is wrong.
- **Immersion (Q's amendment, Nov 13, 2026):** sound + transition + motion + caption fire as ONE fused event so the viewer feels *inside* the video experience, riding its emotional wave — not watching edits happen from outside. This layers ON TOP of everything already set (density, beat-lock, coverage, lane dialects) — it changes how picks are chosen, not whether the existing rules apply.
- **Attachment mechanics:** consistency is what attaches — the same event family keeps the same sonic signature across a video and across videos, so the viewer learns the rhythm and anticipates the payoff (landing → click, count-up finish → completion ding, lock-in → latch). Micro-novelty lives inside the family (variant/pitch), never as random new sounds.
- **Calm, not flat:** satisfying ≠ quiet-only. Levels still follow §1.4 (everything under the voice); satisfaction comes from texture and timing (beat-lock §1.6), not volume. A cue that is merely turned down but still harsh fails; swap the file.
- **QC gate (add to every build's sound QC):** the 5× loop test on a phone speaker — loop each recurring cue five times; any flinch, fatigue or irritation = swap the variant and re-check. Plus one full watch at phone volume asking only: does the sound layer evoke the emotion each beat is supposed to carry and keep the viewer *immersed and harder to leave*? If not, the picks are wrong even if coverage and levels pass.

## 2. Sound → Transition Table

Read this table lane-aware: the first block is the *measured source* behaviour; the second is Q's *applied* pairings. A transition that is silent in Sky/Devin does not acquire a whoosh just because it appears in Q's tutorial list — the lane decides (see §5).

### 2.1 Measured source behaviour

| Transition / cut type | Sound in the source | Evidence |
|---|---|---|
| Any cut, Sky corpus (incl. the 3 whip/blur transitions and D48 top-half swaps) | **Silent — universally.** No whoosh/pop/tick on any re-measured cut in any reel | [MEASURED — SKY-TEARDOWN-MASTER §7.3] |
| Hard cuts, Devin dry family | No transition sound claimed; sound follows the *device*, not the cut. Onset candidates (33–68/reel) are an upper bound including word onsets, never an SFX count | [MEASURED — DEVIN-EDITOR-BRAIN §6] |
| Returns to face, Devin | Often a ~3-frame **cross-dissolve** (picture), no transition SFX claimed. Hard cuts are for hook and device changes | [MEASURED — DEVIN-EDITOR-BRAIN §5] |
| Wedge fly-in, comments-sheet slide, money-bill wipe, hook-wheel scale-up, Devin | Logged as **silent** where noted (wedge: "hard cut out, silent"). RGB-split glitch ~4–5 frames and white flash (1 frame + ~0.9 s fade; DSh glow-flash variant) carry no confirmed designed sound in the brain | [MEASURED — DEVIN-EDITOR-BRAIN §5] |
| Cuts over a continuous bed, Sky music vlogs (only 2, both speech-free) | Cuts land **silent over the bed** — "the music is the transition glue" | [MEASURED — SKY-TEARDOWN-MASTER §7.3] |
| Hard cuts, real-sound launch films | **Nothing.** Cursor moves/hovers/scrolls and streaming text also get nothing — the music carries them | [TUTORIAL — real-sound launch map] |

### 2.2 Q's applied transition pairings (tutorial reels + Kien + Transitions builds)

Source key: **SS** = SOUND_SYSTEM v2 (6 reels Q sent, Nov 6) · **KIEN** = @kienobifilms decode, Batch 24 · **VP** = Viral Forms Launch Pack / Transitions Sheet, Nov 12 (✓ = verified from the reels/Q's Kien project; ◐ = CapCut pairing matched by texture — treat as proposed, not verified) · **LD** = Locked Doors cue sheet (applied in a real Q build).

| Transition (picture) | Sound | When / constraint | Evidence |
|---|---|---|---|
| Reveal-type transition generally (B&W beat in, light leak, flash, end-card cut) | **Camera shutter / flash** | SS groups these under one shutter family | [TUTORIAL — SS table] |
| Block Rise (vertical blocks rising) | **Soft Rise "Chararan" Glitter** (VK, 00:03) | Product reveal — "the first time the product appears, never a plain cut-in." In Q's Kien build the SFX was too soft/masked to prove frame-exact sync (offset ~0–0.1 s, CONSISTENT not frame-provable) | [MEASURED name pairing — KIEN DECODE; TUTORIAL use — VP A1 ✓] |
| Retro Rewind | **Tape rewind sound** (pill title truncated on Q's asset: "…oon: The sound of a…", 00:01 — do not invent the full title) | "Wait, let me back up" / replay a line just said | [MEASURED name pairing — KIEN; TUTORIAL use — VP A2 ✓] |
| Blu-ray Scanning | **Scan whoosh** (pill: "…hoosh sound effect", 00:02) | Proof moments — scan sweeps across a screenshot/contract | [MEASURED name pairing — KIEN; TUTORIAL use — VP A2 ✓] |
| Pixel Explosion | **Bass Impact** | Problem → solution smash; price-drop/offer reveal. "Your drama pairing — once per video, max" | [TUTORIAL — VP A1 ✓ pairing / TRANSITIONS-SHEET #4; constraint Q-ORDER in sheet] |
| Whip Pan | **Fast Whoosh** | Face → product in hand, mid-sentence; hides the cut | [TUTORIAL — VP A1 ◐, fallback: whoosh sweep in library] |
| Pull In / zoom cut (before → after) | **Camera Shutter + Pop** | Face = before, shutter-pop, result close-up = after | [TUTORIAL — VP A1/A2 ◐; TRANSITIONS-SHEET #3] |
| Flash Frame (2-frame white) / Flash White | **Camera Flash / Shutter** | Claim reset / new section, new angle | [TUTORIAL — VP A2 ◐; SS shutter family] |
| Mask Wipe (object pass across lens) | **Hand Swipe / Cloth** | Scene/outfit change performed by Q, not an effect | [TUTORIAL — VP A1 ◐] |
| Slide / swipe / card flies in (generic move) | **Whoosh / swish** ("chuck a whoosh on anything moving") | Any moving element in SS grammar; in LD, whoosh (real) is the actual transition sound into/out of every full-screen stretch (phone_lock, profile, padlock, table, calendar) — 12 whoosh placements in the v7 mix | [TUTORIAL — SS; Q build record — LD] |
| Zoom-through into a device (LD: into padlock) | **Riser 0.2–0.3 s** into the stretch, then the stretch's own sounds | LD lists it as *still needed*, not in the v7 mix — an intended pairing from the build, not a laid sound | [Q build record (needed list) — LD] |
| Return from a full-screen stretch (LD: phone_lock, calendar) | **Flash hit / camera shutter** on the return cut; **glitch burst ~0.15 s** on the return from profile; **glitch tear ~0.2 s** into the end card | All on LD's *needed* list — the v7 mix used whoosh for the same returns, so a build must pick one grammar and not stack both | [Q build record (needed list) — LD] |
| Shot change on Q himself (LD: 6.73 s, 15.30 s) | **Glitch burst ~0.15 s** | Needed list only | [Q build record — LD] |
| Spinback / "wait, back up" (SS grammar) | **Spinback / tape stop** | Distinct from the Kien Retro Rewind pairing — same *job*, different named sound in a different source. Do not merge them silently; lane/source decides | [TUTORIAL — SS table, source reel DYw2] |
| Metallic riser as transition tension | **Metallic riser**, ending exactly on the change | SS: riser class generally "ending exactly on the change"; metallic variant is the tension flavour (DdFMe). Earshot launch kits likewise allow **one** riser/reverse swell at a section change | [TUTORIAL — SS; earshot Loop 5 launch preset] |
| Cross-dissolve (long, 12+ frames) | **Ambient swell** | Faceless mood / faith / reflection B-roll only — "the only place a dissolve belongs" in the VP system; contradicts the general no-fade rule elsewhere, so it is scoped to that format | [TUTORIAL — VP A7 ◐] |
| Beat-cut montage | **Percussion hits on the beat** | Every cut on a beat, no exceptions — off-beat is a defect | [TUTORIAL — VP A7 ◐] |
| Zoom-out reveal (tight detail → whole scene) | **Riser → silence** | The riser cuts to silence on the reveal; the silence hooks the next line | [TUTORIAL — VP A7 ◐] |

**Coordinator note on conflicts:** SS says shutter serves B&W-beat/flash/end-card transitions; Sky's *measured* B&W beat has **no impact sound** and Sky cuts are silent (§2.1). The shutter pairing is therefore a Q-lane/tutorial application, never a Sky fact. Likewise LD's needed-list flash/glitch returns vs its laid whoosh returns must be resolved to one choice per return in the final doctrine.

---

## 3. Sound → Pop-Up / Edit-Event Table

### 3.1 The measured Sky core: the tick-tone family (the only designed-sound family in Sky)

Fixed-frequency, gated, faint. Origin (Sky's edit micro-SFX vs a device sound captured in the take) **cannot be proven from audio alone**; beat-sync argues for the edit. Edits ADD the tick on these device classes per the family spec (`TICK_TONE_SPEC` in Sky code). **[MEASURED — SKY-TEARDOWN-MASTER §7.2; STYLE-GRAMMAR §7]**

| Edit event | Tick-tone instance (all confirmed) | Numbers |
|---|---|---|
| 10-second timer device | 5,926 Hz pulse train, DfPxqFPAY4_ @19.64–20.67 s | Sharpness 0.34; ~15 pulses; band peaks −31 dBFS |
| View-counts landing / refresh | 5,926 Hz, DfDuMnCjNdE @10.42–11.68 s | Sharpness 0.33; ~17 pulses @ ~13/s; peaks −28 dBFS |
| Watch-time timer | 5,926 Hz, DfDuMnCjNdE @44.05–45.05 s | Sharpness 0.37 |
| Line-chart draw ("High Engagement") | 5,926 Hz, De-A2dvCeV3 @17.50–18.16 s | Sharpness 0.32 |
| Payment count-up pills (closing) | 5,926 Hz, Dez4fPJCR74 @57.82–58.57 s — **the loudest**, running to the last frame | Sharpness 0.38/0.26; ~13 pulses @ ~16/s; band peaks **−19 dBFS**; per-reel note: band median −37 dBFS |
| Opening funnel-rain build; opening head-cloud build | Gated tone **≈9.15 kHz**, DfX2qwQGagM @0.6–1.2 s; DfDuMnCjNdE @0.42–1.07 s | Sharpness 0.46–0.56 |
| "Minimum" tag / trust-bar landing; "SHOW HER IN HER ELEMENT" label landing | Sustained two-tone **≈11.1 + ≈11.85 kHz**, DfX2qwQGagM @34.41–34.86 s and @43.98–44.40 s | Second instance +42.5 dB over band median — strongest excess in the set |
| Headline entrances (outside priority set) | Pulsed ~9.3 kHz, DSB8X22kSfe @1.94–2.48 s ("6 MONTHS" + sparkle) and @39.14–40.88 s ("3 EDITORS", ~28 pulses, leading the entrance by ~0.9 s) | +51 dB / +50 dB over band median; at voice level; headline-locked, not cut-locked |
| Player-stats card swap (D51) | Isolated UI blip **7.0–7.8 kHz**, DJccT_xSWuT @31.26–31.68 s | Band RMS −33.0 dBFS vs −47.0 control; moderate confidence, counted as 1 confirmed candidate. Rule for that reel: card entrances only; its 9 cuts otherwise silent |
| Hook-line accent (both statements of the same hook line) | HF noise bursts 6–14 kHz, DRgQLh3Ak-3 @0.46–0.92 s and @41.64–42.08 s, each immediately *before* the hook word | Band RMS −19.3 / −21.9 dBFS; scratch/censor-type, exact timbre moderate confidence, not ear-verified |

**Everything else in Sky measured 0 confirmed ordinary SFX:** no whoosh/pop/riser/ding on any device landing anywhere in the corpus. Sub-threshold 5.93 kHz hits (sharpness 0.12–0.21 in 8 reels) are recorded as **unconfirmed residue**, indistinguishable from sibilance — never build a rule on them. **[MEASURED — §7.2/§7.3]**

**Refuted, do not carry forward:** DP4r6BbEvHg's "low drone synth intro" — Batch 36 gap test refutes it (intro word-gap LF −28.6/−28.7 dBFS vs −25.1 dBFS later gap; LF tracks the voice). Bed = NO at measurement sensitivity. **[MEASURED — §7.3]**

### 3.2 Devin edit events (measured)

| Edit event | Sound | Evidence |
|---|---|---|
| Verdict X stamp (1-frame pop, 120%→100% settle in 4 frames) | **Silent** — all 3 DLpg Xs, RMS 0.02–0.04. Timing itself is loose: an X can land 0.28–0.47 s before/after the verdict word (DLpg X1 lands 0.47 s *after* "26", in the pause) | [MEASURED — DEVIN-EDITOR-BRAIN §5/§6] |
| Count-up (25→625; $0→$241,069; counts on phone/profile artefacts) | **No tick track** on the measured Dfc count-up. The number densifies with the picture as one event — silently, in the dry family | [MEASURED — §6] |
| Any device, dry family | **ONE SFX per device, never stacked.** Sound follows the device, not the word; no per-word ticks | [MEASURED — §6] |
| Cursor click (target travel 10–16 f → 2 f pause → button compresses to 97% for 2 f → click ring 70%→140% over 8 f) | The brain measures the *visual* click grammar; it does **not** isolate a click sound for it. In Q's Locked Doors build the equivalent beat is sounded explicitly (see §3.3: mouse click + pop-small on ENTER) — that is Q's build choice, not a measured Devin sound | [MEASURED visual; sound UNVERIFIED — §4/§6] |
| Subtraction (losing version deleted; strawman lit; clutter removed) | May be **silent on purpose** | [MEASURED — §6 placement rules] |
| Performed CTA (comment types → sends → DM banner) | Sounds **belong to the performance** (typing/send/banner as performed events) — the one place a sound chain is structural in Devin | [MEASURED — §6/§7] |
| Bedded device reel events (Dd3: Share-button shatter, Trial toggle, countdown swap, DM banner, final glitch) | Designed sounds are **plausible** at these beats but were **NOT spectrally isolated** in the source soundmap — treat every such label as probable, not measured | [MEASURED limit — §6 Family B] |
| B-roll inserts (all 6 types) | His voice (or silence) carries; the insert's own audio is heard **only when the audio IS the evidence** (DfV hook-audio replay). In/out is a hard cut; returns dissolve ~3 frames | [MEASURED — §8 cross-type laws] |

### 3.3 Q's applied pop-up / device pairings (SS + SKY-PLUS + Locked Doors build)

| Edit event | Sound | Evidence |
|---|---|---|
| Something **revealed** (panel, chip, label, card face, logo) | **Pop** (varied over 4 earshot pops in the Sky engine) | [TUTORIAL — SS: "pop for anything revealed"] |
| Something **moves** (card flies in, plate slides, swipe) | **Whoosh / swish** | [TUTORIAL — SS] |
| Fast cut / list row / punch-in | **Click** (`tick` in the engine) | [TUTORIAL — SS] |
| Panel entrance (Sky engine list) | Soft **swish**; rows/checks/timeline nodes: **ticks**; chips/labels: **pops**; counters/charts: **riser + ding**; hero words: **soft hit**; lock device: **unlock sound** | [Q-ORDER — SKY_STYLE §6 SFX list, superseded in part by SOUND_SYSTEM v2 — see source note*] |
| Every jump cut / auto-punch (v2.1 coverage) | **Click**; every 3rd one a **swish**. Every focus pull: **whoosh**. Gaps between sounds ≤ ~2 s outside typing sections | [Q-ORDER — SOUND_SYSTEM v2.1] |
| Device entrance AND exit (SKY-PLUS) | Tick/pop on **both**; stamp sound on verdicts. Sky has no exit sounds — exits are the named divergence | [Q-ORDER — STYLE-GRAMMAR §7; TEARDOWN §7.4] |
| Meme / GIF pop (Carter/Kilgore grammar) | SFX **in AND out**: `pop` in + quiet `tick`/`swish` out by default, or the §4 pairing for that beat. Scripture beats excluded; max 1 time-card per video (whoosh in/out) | [Q-ORDER — SKY_STYLE §16] |
| Card/chip/badge appears (launch films) | Soft real **pop or tick**, climbing across a run; sits at 50% of its travel | [TUTORIAL — real-sound map] |
| Toggle / lock-in / counter's final value (launch films) | Real **latch / click / crisp tick** on the contact/lock frame | [TUTORIAL — real-sound map] |
| **Locked Doors v7 — actually laid (real sounds, Q's Sky SFX kit):** device lands (dev_intro, cards, dev_x3, dev_level, dev_fans, dev_buyers, dev_same, dev_week, dev_price, dev_list, dev_cta, dev_dm, hook badges) | **pop-medium-in** on landing; **pop-medium-out** on leaving — the in/out pair applied consistently across 35 pop-medium placements (of 56 laid placements in total) | [Q build record — LD real-sounds table] |
| LD: verdict/check lands inside a device (7 placements) + cursor ENTER + comment sent | **pop-small-in** (9 pop-small placements in total) | [Q build record — LD] |
| LD: full-screen transitions in/out | **whoosh (real)** — see §2.2 | [Q build record — LD] |
| **LD — still needed (intended, NOT laid, nothing synthesised):** hook frame 1 | **IMPACT / slam** | [Q build record — LD needed list] |
| LD needed: losing hook card removed; handwritten "they stay" scribble | **SWIPE/delete**; **PEN scribble ~0.4 s** | [LD needed] |
| LD needed: lock icon closes; gold X / $97 slam-shake beats (×6); padlock shuts on "locked" | **Soft impact / lock click**; **short tight IMPACT** per slam; **HEAVY IMPACT / metal lock slam** | [LD needed] |
| LD needed: 65-members count-up; table rows light (DAY ONE / WEEK ONE / ONE BAND / ONE SOUND); "20 copies sold" appears | **Count-up ticks or riser ~1.1 s**; **UI tick/select** per row; **UI pop** | [LD needed] |
| LD needed: Dec 7 countdown runs; calendar lands | **Clock tick loop ~1.5 s**; **shimmer / page flip** | [LD needed] |
| LD needed: room goes silent beat | **Power-down / drop** | [LD needed] |

\* Source note for the coordinator: `SKY_STYLE.md` §6 explicitly says SOUND_SYSTEM v2 "supersedes the SFX list below," and v2.1 then supersedes v2's "no exit sounds / no sound on captions after the hook" density with 100% entrance+exit coverage (TEARDOWN §7.4 ship-time correction). This draft follows the *latest* layer for density and uses the older list only for per-device sound *choices* where v2 does not name a different one.

### 3.4 Earshot kit families — which texture belongs to which event class (music-led films)

Prefer the 0.4 families over bright 5 ms blips and long cinematic tails when a film is cut to music: `ui_pop` (rounded mid pops — chips, bubbles, rows arriving; "the most used effect in those films"), `knock` (mid-band wood/plastic), `cut_hit` (short sub hits with a kick), `mallet` (gated glockenspiel/celesta/marimba, chime runs; pitch-tunable), `drip` (water drops, pitch may rise), `shutter` (snap zooms, whip-cuts), `reverse_swell` (peaks just after a cut, one per film), plus whoosh_big/swish bright/whoosh_fast whip, glitch burst/mid/chirp, notify mid_tine/mid_wood. Presets calm/crisp/minimal keep riser, swell and suck **off** — a reveal resolves on one element and the lockup is one clean hit; only the launch preset sounds one riser/swell at a section change. **[TUTORIAL — earshot SKILL, Loop 5]**

---

## 4. Sound → Words / Beats

### 4.1 Every displayed word (the Nov 2 two-tier system)

- **Tier 1 — tick on every displayed word:** 28–32 dB under voice peaks, pitch-varied, downward drift per sentence. **[Q-ORDER — adopted recipe, memory 2026-11-02 line 446]**
- **Tier 2 — hotter POP on emphasis words**, synced to the word *and* its zoom: emphasis = numbers, named things, the payoff word, the keyword. The emphasis words are also the ones that switch font (Anton gold ~1.15× invades the Montserrat ExtraBold caption line); statement-scale Anton ALL-CAPS carries hook/verdict lines; Caveat Bold script ≤2× per video (scripture line + one warmth beat). Per-word pills are ruled OUT. **[Q-ORDER — same recipe]**
- The yapping/field version of the same device (creator-stated + tool-doc, **not audio-verified on any single reel**): Tier 1 tick ~30–50 ms per displayed word at 28–32 dB below voice peaks; Tier 2 pop ~5 dB hotter. Adoptable per the router; verify on the test edit's waveform. **[TUTORIAL — yapping STYLE-GRAMMAR §8]**
- **Scope limit — Sky lane captions get NO per-word sound in the source grammar:** Sky captions hard-cut in ~0.5 s groups with no animation and no measured caption SFX; the tick-tone family never sits on captions. The per-word tick is a PWC/Viral-lane device. Do not export it into a Sky-exact build as "Sky." **[MEASURED — TEARDOWN §7; Q-ORDER scope]**
- SS text rule (different scope — headline/typed text, not captions): **Apple-keyboard click, one per word** on text on screen ("the secret trick is one click per word"); engine: `key` per serif/hero word, `type` per letter in the typed hook. **[TUTORIAL — SS]**

### 4.2 Hook words and the first frames

- **Frame 1 / hook landing:** LD's build wants an **IMPACT/slam at 0.00** ("hook lands, frame 1") — needed list, not laid. SS grammar reserves its single impact for the payoff (see §4.7), so a frame-1 impact and a payoff impact in the same video would break the one-impact ceiling — coordinator must resolve per lane (see §6). **[Q build record — LD; TUTORIAL — SS]**
- **Hook claim word:** short riser into a **soft impact hit** on the claim word (Hormozi-format opening punctuation). **[TUTORIAL — MEME_GRAMMAR §1]**
- **"Stop doing X" / scroll-stopper:** **record scratch** or a **single vine boom** on the hardest word. **[TUTORIAL — MEME_GRAMMAR §1]**
- **Question hook showing the end-state first:** cha-ching if it's money; **sparkle chime** if it's transformation. **[TUTORIAL — MEME_GRAMMAR §1]**
- **Hook types on (Q's Sky variant):** the hook captions type letter-by-letter **with key sounds** — Q's standing ask in the Nov 6 SKY_STYLE. Note the later v6 correction: letter-by-letter hook captions are listed as a **banned telltale** in the Nov 12 ship-time fixes (captions hard cut-in ≤1 frame). Both are on disk; §6.5 resolves it — the Nov 12 layer governs. **[Q-ORDER, conflicting layers — SKY_STYLE §4 vs TEARDOWN §13]**
- **Devin hook caution:** a hook slam is **not universal** in Devin — DLpg's hook starts quiet (first-bin RMS 0.061) while Dff's first 0.1 s hits 0.44 (probable impact, RMS-only). Do not mandate a hook impact in the Devin lane. **[MEASURED — DEVIN-EDITOR-BRAIN §6]**
- **Sky hook caution:** the measured hook-locked sounds in Sky are the 9.3 kHz headline tones (DSB8X22kSfe) and the DRg hook-line HF bursts *before* the hook word — there is no measured hook impact in Sky. **[MEASURED — §7.2]**

### 4.3 Numbers, money, proof

| Beat | Visual (for context) | Sound | Evidence |
|---|---|---|---|
| Any dollar figure lands ("$800 for two videos") | Receipt/payout screenshot beside him, amount sharp | **Cha-ching** — "used when money is earned, saved, spent, or discussed" | [TUTORIAL — MEME_GRAMMAR §5] |
| Money moments (SS grammar) | — | **Coin / cash register** (`ding`/coins in engine) + on-screen results disclaimer | [TUTORIAL — SS] |
| A number counts up on screen | Animated count-up graphic | **Counter-tick loop under the count; cha-ching or ding on the final number** | [TUTORIAL — MEME_GRAMMAR §5, citing Animax placement notes] |
| Count-up, Sky source | Payment pills / counters / timers | **Tick-tone family only** (§3.1) — gated 5,926 Hz, never a generic tick loop, never a cha-ching in the source | [MEASURED — TEARDOWN §7.2] |
| Count-up, Devin source | Number + picture densify as one event | **Silent** on the measured instance (Dfc) | [MEASURED — DEVIN §6] |
| Count-up, Q builds | Counter/chart devices | **Riser + ding** (SKY-PLUS list); LD: ticks-or-riser ~1.1 s for the 65-members count | [Q-ORDER — SKY_STYLE §6; LD needed] |
| Follower/view counts ("490 followers") | Profile card, real count circled | **Pop + quick counter tick** as the number lands | [TUTORIAL — MEME_GRAMMAR §5] |
| Proof montage (receipts in a row) | Fan/stack of proof cards cycling fast | **One cha-ching per card, rhythmic** (MrBeast money-montage grammar) | [TUTORIAL — MEME_GRAMMAR §5] |
| Email offer / brand deal described | Real email (blur protocol) | **Notification ding / email chime** as it slides in | [TUTORIAL — MEME_GRAMMAR §5] |
| Zoom punch-in on a number (VP grammar) | Punch lands exactly on the number | **Subtle bass tap** — "Numbers get a sound or they don't register" | [TUTORIAL — VP A3 ◐] |
| Split-screen results comparison | Side-by-side on the tick | **Single tick** on the wipe | [TUTORIAL — VP A3 ◐] |

Proof law binds every row: memes illustrate feelings, they **never substitute for proof**; proof visuals are always real and under Q's blur protocol. **[Q-ORDER — MEME_GRAMMAR fit-check]**

### 4.4 Lists, steps, names, platforms

- Each numbered point: keyword card pops beside his head, building a visible stack — **small bubble pop per item** (Uppbeat's most-downloaded premium SFX; Linus Tech Tips' per-item habit). **[TUTORIAL — MEME_GRAMMAR §6]**
- Naming a platform/tool ("on Instagram… on TikTok…"): logo/app icon pops in — **bubble pop**. **[TUTORIAL — §6]**
- "For example…": real example enters — **whoosh in, soft pop as it settles**. **[TUTORIAL — §6]**
- Key takeaway inside a list: takeaway isolated as a clean text card — **bell ding** (Joshua Weissman's documented takeaway habit). **[TUTORIAL — §6]**
- Steps shown on a screen recording: **keyboard typing** under typing moments; **UI clicks** on taps/buttons. **[TUTORIAL — §6; LD needed UI tick/select per table row agrees as a Q build instance]**
- List rows in the Sky engine: **ticks** on rows, checks and timeline nodes. **[Q-ORDER — SKY_STYLE §6]**
- Ken Burns push over B-roll text (faceless format): **soft tick on each text line**. **[TUTORIAL — VP A7 ◐]**

### 4.5 Verdicts — right way / wrong way

The lanes *disagree* here, and the disagreement is the doctrine:

| Lane / source | Wrong way | Right way | Evidence |
|---|---|---|---|
| Tutorial / meme grammar | **Wrong-answer buzzer** (flat, fast) or **sad trombone** (match weight to the mistake) | **Correct-answer ding/chime** — "a ding confirms success without stopping the flow." Side-by-side: buzzer on the wrong side appearing, ding on the right side — "the pair teaches itself" | [TUTORIAL — MEME_GRAMMAR §§2/7/9; SS quiz row: right ding / wrong buzz] |
| Sky engine (PWC variant) | ✕ rows / verdict stamps carry the SKY-PLUS **stamp sound** | Checks carry **ticks** (rows/checks/nodes) | [Q-ORDER — STYLE-GRAMMAR §7; SKY_STYLE §6] |
| Devin (measured) | Verdict X: **silent** | (No sounded right-way counterpart measured) | [MEASURED — DEVIN §6] |
| Locked Doors build | Gold X / $97 slam beats: **short tight IMPACT** ×6 (needed list) — Q's Devin-lane build *sounds* the verdict Devin leaves silent; label it a Q divergence inside the Devin lane | Verdict/check lands inside devices: **pop-small-in** (laid) | [Q build record — LD] |
| Warning / "never do this" | **Alarm/error buzz** — short, UI-family, not horror-movie. Consequence beat: low drone or single deep boom, sparingly. Scam callout: record scratch or buzzer | — | [TUTORIAL — MEME_GRAMMAR §9] |

### 4.6 Scripture and faith beats — dignity sounds only

- A verse is quoted (flat navy serif scripture plaque): **a single soft bell/chime** — reverent, **no meme sound on scripture**. **[TUTORIAL — MEME_GRAMMAR §12]**
- "God opened the door"-type testimony: **gentle riser, no comedy cues**. **[TUTORIAL — §12]**
- Gratitude/credit beat ("that's nobody but God"): music breathes; **near-silence is the cue**. **[TUTORIAL — §12]**
- Engine-level exclusion: meme/GIF pops are **excluded on scripture beats** in Q's Sky engine, full stop. **[Q-ORDER — SKY_STYLE §16]**
- The Nov 2 caption recipe reserves one of its ≤2 script-font beats for the scripture line — a *visual* rule that pairs with the soft-chime rule above; no per-word tick escalation on the verse is specified anywhere on disk (see §6). **[Q-ORDER — memory 2026-11-02 line 446]**

### 4.7 Payoff, reveal, comedy, pain — the rationed big sounds

- **The payoff:** **impact / bass boom — ONE per video, max**, with a **riser 0.4–0.9 s before, ending exactly on the change** (payoff riser sits 0.9 s before in the engine spec). **[TUTORIAL — SS]**
- **Biggest claim/reveal of the video:** punch-zoom + **ONE vine boom** ("added after a surprising statement, sudden camera zoom, unusual facial expression, or dramatic reveal… use it on the strongest moment, not every sentence"), rationed to once, maybe twice, per video in Q's heavy-rotation list. **[TUTORIAL — MEME_GRAMMAR §§3 + heavy rotation]**
- **Unexpected detail revealed:** vine boom **or** metallic riser resolving into a ding. Plot twist / cutaway out-and-back: **whoosh out, whoosh back**. **[TUTORIAL — §3]**
- **Rewind / "wait, go back":** **record scratch / turntable scratch** — Q's own named signature candidate; the scratch *is* the rewind's sound. Recap callback: the earlier visual returns with **the same sound it had the first time** (callback consistency). Before/after freeze: **camera shutter**. **[TUTORIAL — MEME_GRAMMAR §4; Q named the scratch himself per §4/ heavy-rotation note]**
- **Pain / mistake beats:** naming the pain → **soft sad trombone (wah-wah)**; a specific fail → **meme fail alert or low bonk**; broke/stuck/nothing-happened → **crickets**; wrong belief stated as a fake headline → **wrong-answer buzzer**, then he corrects it. **[TUTORIAL — §2]**
- **Wins:** brand said yes → **short victory fanfare / applause burst**; member win → cha-ching if money, cheering/clapping if milestone; his own milestone count-up → **riser into ding + applause tail**; story punchline → **rimshot** if a constructed joke, warm ding if heartfelt. **[TUTORIAL — §8]**
- **Comedy beat (SS):** **vine-boom-style bass drop** at the plan's comedy times; "FAHHH" meme only with a licensed file Q supplies; glass shatter on mistake/shattered expectation (needs a licensed file). **[TUTORIAL — SS]**
- **Humour/self-roast:** sad trombone or soft bonk on the throwback beat; rimshot for a constructed joke (laugh-track chuckle usually too much — prefer rimshot or nothing); absurd exaggeration → **rapid notification pings stacking** ("the sound IS the joke"); awkward beat → **crickets, exactly one beat**, then move on. **[TUTORIAL — §13]**
- **Urgency/time:** deadline named → **ticking clock under the line**; countdown structure → **countdown beeps (3 short + 1 long final)**; "before it's too late" → **heartbeat tension 1–2 s max**; waitlist scarcity → ticking + **soft alarm bell on the deadline word**. VP promo grammar scopes its clock tick to the numbers only, "never as a constant bed." **[TUTORIAL — MEME_GRAMMAR §10; VP A4 ◐]**

### 4.8 CTA, intros, outros / end cards

**CTA beats (performed, in every grammar that has them):**

- Keyword CTA ("comment WAITLIST"): keyword pill + mock comment typing it out — **keyboard typing as it types → send/whoosh as it "posts" → notification ding on the reply**. LD's laid/needed chain is the concrete build: typing 8 taps over ~0.5 s (needed) → pop-small on comment sent (laid, 62.73 s) → pop-medium on reply landing (laid) → notification chime on the DM banner (needed). **[TUTORIAL — MEME_GRAMMAR §11/§15; Q build record — LD]**
- The keyword *word itself* in Q's signature builds: **spray whoosh + Water Line completion + the fixed E5→G5→C6 sting**, identical on every video, at ~−16 dB under voice peaks. **[Q-ORDER — memory 2026-11-02]**
- Real comment referenced: comment screenshot card — **message pop**. DM thread shown: **iOS-style message pings alternating** per bubble. Skool community shown: **soft pop per win card; cha-ching on money wins**. "Follow me": **follow-button click + notification bell ding**. **[TUTORIAL — MEME_GRAMMAR §11]**
- Deadline close ("doors open December 7"): **ticking resolving into a ding** (urgency → resolution). Final mic-drop line: **one vine boom or impact hit — the LAST big sound of the video, saved for here** (note the tension with §4.7's one-impact ceiling and §4.2's frame-1 impact — see §6). **[TUTORIAL — MEME_GRAMMAR §15]**

**Intros / first seconds:**

- Q's frame law precedes any sound law: frame one = Q talking on camera; never a cold open on a wall/board without him. **[Q-ORDER — SKY_STYLE hard corrections, Nov 7]**
- Sky hook zoom-out (1.45× → 1.0 by ~f30) carries **no measured sound**; Sky's only measured opening sounds are the gated ~9.15 kHz tones on opening builds (DfX2/DfDu, §3.1) and the headline tones (§4.2). **[MEASURED]**
- Devin: no universal hook sound (§4.2). Dd3's bed is simply *already running* — a bedded reel has no intro sting measured. **[MEASURED]**
- Real-sound cold open: where the music is silent before a cue, level falls back to the role's fixed `level_db` — there is no intro effect by default. **[TUTORIAL — earshot Loop 5]**

**Outros / end cards (Q's rotating forms, SKY_STYLE §11 + SS ending rules):**

| Ending form | Sounds |
|---|---|
| `card` (punch-zoom/blur out → off-white card, logo pops, line types on, pill buttons, cursor clicks CTA → fills gold) | **Shutter in; pop on the logo; keys on the words; click + "right" ding on the button** [SS]; LD's equivalent tail: whoosh (laid) tearing in, then needed **glitch tear ~0.2 s + END STING / logo hit** on the COMMENT WAITLIST card |
| `comments` (texting B-roll over a real room plate; IG comments pop in; title types on) | **A notification per comment; typing on the title** [SS] |
| `notifs` (phone floods with "commented: WAITLIST" notifications, accelerating, bursting out) | **Accelerating notification sounds → riser → big whoosh → boom on the burst** [SS] |
| Backyard signature end card (Nov 2) | **Spray-whoosh into the cut; water drop/splash synced to the logo animation; soft ding on the logo settle; Water Line completing across the card open**; settled CTA line for the final ~2 s. Logo animation and its timing untouched | [Q-ORDER — memory 2026-11-02, end-card latitude] |
| Logo outro after walk-out (meme grammar) | **Short brand sting — the same sting every video** (audio logo) | [TUTORIAL — MEME_GRAMMAR §15] |
| Devin source endings | **No end card is the habit** (glitch-out, phone-check frame, mid-sentence cliffhanger cut). Q override: glitch may tear *into* Q's end card; it may not replace it; cliffhanger cuts are banned on Q's trio | [MEASURED + Q-ORDER — DEVIN §7/§10] |
| Sky source endings | Most reels end mid-sentence or on the final diagram — **no outro card, no CTA sound**. Q override: complete the hero device on the closing line, hold 0.8–1.5 s, end moment ≤1 s after the last word | [MEASURED + Q-ORDER — TEARDOWN §9] |
| Launch-film logo (real-sound) | Music stops on a bar line / filters down → 0.2–0.7 s near-silence → **ONE soft note in key** → tail to silence; logo sits 8–20 dB under the drop | [TUTORIAL — real-sound map] |

---

## 5. Per-Lane Dialects

### 5.1 Sky lane — *sparse source, dense PWC target (SKY-PLUS)*

- **Source grammar (build to this first):** dry voice base; **no music bed** in any talking-head/split/autopsy reel (beds exist only in the 2 speech-free music vlogs, where cuts are silent over the bed); **cuts silent universally**; the **tick-tone family** (§3.1) on counters/timers/count-ups/chart draws and the two opening builds; rare isolated SFX (§3.1: DJcc blip, DRg bursts, DSB headline tones — the complete confirmed list); **no dead air**; voice median RMS ≈ −16.4…−20.4 dBFS, reel means −16.1…−18.0 dB. 49 reels measured, 48 soundmaps. **[MEASURED]**
- **PWC target layered on top (labelled divergence):** cleared bed **≈ −28 dB** under speech (licensed local library only); sound on **100% of entrances and exits**; tick-tone reproduced on its native device classes; Q voice to **−14.5 LUFS**, static gain only; uploaded reels stay **original-audio-only** (no added music/beats unless Q asks for that specific post). **[Q-ORDER]**
- **Family note:** the Green (teal) / Orange (gold) family pick changes the *visual* accent only — no sound difference between families is measured or ordered anywhere on disk. Do not invent one. **[Gap stated honestly — SKY_STYLE family pick; no audio row exists]**
- **B&W beat:** no impact sound on it in the reels. The SS shutter-for-B&W-transition pairing is a tutorial application for Q builds, not Sky grammar (see §2.2 note). **[MEASURED vs TUTORIAL — kept separate deliberately]**

### 5.2 Devin lane — *two families, never collapse them*

- **Family A — dry studio (the majority):** voice-led, **no continuous bed**; phrase gaps RMS 0.01–0.04; **one SFX per device, never stacked; no per-word ticks**; verdict Xs silent; the signature count-up silent; a hook slam not universal. **[MEASURED — DEVIN §6]**
- **Family B — bedded device reel (Dd3x4cMStzs only, in the priority set):** **continuous bed under all 39.8 s** (whole-mix RMS −16.0 dBFS, peak −0.87, zero silences); beat labels at shatter/toggle/countdown/DM/glitch are **probable, not isolated**. Q's builds generalise the placement rule as: **beds live under SCREEN/UI stretches, not under face A-roll** — LD implements exactly this, requesting a low real bed *only* inside its five screen stretches (phone_lock, profile, padlock, table, calendar), each annotated "(Devin's second reel runs a bed through the whole reel)." **[MEASURED + Q build record]**
- **Placement law surviving both families:** sound follows the **device, not the word** (one event = one sound); subtractions/verdicts may be silent on purpose; the CTA is **performed** and its sounds belong to the performance. **[MEASURED — DEVIN §6]**
- **Q's Devin-lane builds (LD as the worked example):** real pop-medium in/out on every device landing/leaving, pop-small on checks/ENTER/send, whoosh on full-screen transitions — a *denser* surface than Family A measures, built from Q's Sky SFX kit. The final doctrine should state plainly that Q's Devin builds sound devices Devin himself often leaves silent, as a Q choice (the brain's §10 already authorises the silent fallback: "where no real sound exists, the beat stays silent"). **[Q build record + Q-ORDER]**

### 5.3 Viral lane — *the per-word tick lane (evidence thinnest here — see §6)*

- **Adopted recipe (the lane's defining sound):** two-tier word sounds (§4.1) — tick on every displayed word at 28–32 dB under voice peaks + hotter POP on Anton emphasis words synced to word + zoom; captions are word-by-word with a persistent thesis/title block that **stays the whole video** and breathes (1.000→1.015→1.000 over 2.8 s — a visual rule with no sound of its own). **[Q-ORDER — memory 2026-11-02 lines 208/446]**
- **Bed + density in the Nov 2 exemplars:** cleared instrumental bed at **exactly −28 dB under voice RMS** (Podnebo / Adi Rambo, CC BY 3.0, credited in the post caption); SFX ducked **15–20 dB under voice** in the VIRAL dispatch spec; coverage audited at **118/118 visual events sounded** (BACKYARD-01-FINAL: 121 designed accents + 137 word ticks at −30.0 dBFS; worst event gap 1.633 s). **[Q-ORDER + MEASURED on Q's builds — memory 2026-11-02]**
- **Signature devices with sound:** the **Water Line** (teal progress line + droplet head) fills across the talk and **completes at the keyword word**, where spray whoosh + completion + the E5→G5→C6 sting fire together; **spray-whoosh** is the lane's transition sound family; end card per §4.8. **[Q-ORDER — memory 2026-11-02]**
- **What this draft could NOT verify for this lane:** a "Splice trap bed" as the Viral lane's named bed, and a "persistent title-pill caption" spec as a written grammar — neither phrase exists in the Viral folder on this VM (the folder is a pointer: the working skill lives Code-side at `~/.claude/skills/viral-editing/`, not on disk here). The evidenced bed facts are the −28 dB cleared-instrumental bed above and, in the sibling avatar/yapping lane, a **Splice lo-fi bed** ducked under voice at −14 LUFS loudnorm. The coordinator should pull the Code-side viral-editing skill before finalising any trap-bed or title-pill rule — this draft does not assert them. **[Gap — viral-edit-style/README.md; yapping STYLE-GRAMMAR §8]**

### 5.4 General PWC default (no lane named)

When no lane is named, the default stack assembled from the standing rules is:

1. Voice untouched except static gain to **−14.5 LUFS**; cleared instrumental bed **≈ −28 dB** under speech (licensed library only; uploaded reels keep original audio only). **[Q-ORDER]**
2. **Sound on every device entrance and exit** (SKY-PLUS layer, §3.3) with pitch variants; gaps between sounds ≤ ~2 s outside typing sections (v2.1 coverage). **[Q-ORDER]**
3. **Per-word ticks** only where the format carries word-by-word captions (Viral/talking-head recipe formats) — not as a default under phrase-chunk or Sky hard-cut captions. **[Q-ORDER, scoped by §4.1]**
4. Meme pairings from §4 **by situation**, rationed (one boom/impact max class, §1.7), clean/faith-aligned memes only, never over the face, never instead of proof, **never on scripture**. **[TUTORIAL + Q-ORDER constraints — MEME_GRAMMAR fit-check]**
5. Transition sounds from §2.2's Q-applied table, **one dramatic transition per video**, sound exactly on the transition. **[TUTORIAL/Q-ORDER]**
6. CTA performed with its typing→send→notification chain; keyword sting where the signature kit is in force; end card **≤1 s after the last word** with its form's sound set (§4.8). **[Q-ORDER]**
7. Every asset passes the **real-recording gate** (§1.5): licensed/real or labelled earshot bank; if no real sound exists for a beat and the lane permits silence, the beat stays silent rather than synthesised. **[Q-ORDER/doctrine]**

### 5.5 Cross-lane conflict table (the coordinator's decision list, pre-flagged)

| Question | Sky source | Devin source | Q / tutorial layer | Draft position |
|---|---|---|---|---|
| Sound on cuts? | Silent, universally | Follows device, not cut | SS/VP sound several transition types | Lane decides; never claim Sky/Devin whoosh on cuts |
| Count-up sound? | Tick-tone only | Silent (measured instance) | Riser+ding / tick loop / LD ticks-or-riser | Per lane; generic tick ≠ Sky tick-tone |
| Verdict sound? | Stamp (PWC variant) | Silent | Buzzer/ding pair (tutorial); LD impact | Devin-exact builds default silent unless Q orders the LD treatment |
| Bed under face A-roll? | No bed at all (source) | No (dry family); bed under screen stretches only | −28 dB cleared bed (Q divergence) | Q builds: yes at −28 dB, labelled divergence; source-exact builds: no |
| Per-word ticks? | No | No | Yes — Nov 2 recipe lanes only | Scoped to Viral/talking-head recipe formats |
| Exit sounds? | None | Not measured | Yes — 100% in/out (SKY-PLUS) | Q builds yes; source-exact builds no |

---

## 6. Open Questions / Gaps — where the evidence is thin (labelled honestly)

1. **The Sky tick-tone has no ear-matched local file.** Batch 36 marks it NO LOCAL MATCH VERIFIED in every affected soundmap. Until a file is ear-matched (earshot `match`/`ab` against the isolated windows in §3.1), any build reproducing it is using an unmatched substitute. *Needed:* a sourcing pass against the licensed SFX kit (320 files in `edit_pilot_work/knowledge/assets/sfx-kit/sounds` per TEARDOWN §11.2) with the §3.1 windows as references.
2. **No corpus-wide beat-offset distribution exists for Sky.** BEAT-LOCK-SPEC asked for median/p90 event-to-word-onset distances; no worker computed it, and most device timestamps carry ±0.1–1 s brackets. The ≤1-frame PWC target rests on Sky's *best strip-measured instances* only. Any future "Sky median offset" number without a fresh measurement pass is invented. **[TEARDOWN §8.2, stated in the source itself]**
3. **Devin SFX labels beyond RMS are mostly unproven.** Onset candidates (33–68/reel) include word onsets; Dd3's designed-sound labels are "probable, not measured"; the cursor click's *sound* was never isolated (only its visual grammar). A spectral pass like Sky's Batch 36 has not been run on Devin. Family B rests on **one reel** (Dd3) in the priority set.
4. **Viral lane grammar is not on this VM.** **[RESOLVED in the Nov 13 finish pass — the Code-side skill WAS pulled and checked: `~/.claude/skills/viral-editing/SKILL.md` exists on this VM. Its sound rule reads: Q's dense-SFX default (sound on every imagery entrance AND exit, layered landings, accents on statement lines) with "a cleared hype beat at ~−28 dB under speech." No "Splice trap bed" product name and no "persistent title-pill caption" spec exists anywhere in that skill — those two phrases are NOT doctrine. The evidenced caption fact remains the Nov 2 recipe's persistent thesis/title block (§5.3).]** `styles/viral-edit-style/` contains only a pointer README; the working skill is Code-side (`~/.claude/skills/viral-editing/`) and its web zips were not mined. The brief's "Splice trap bed at voice −28 dB" and "persistent title-pill captions" could **not** be found on disk — the −28 dB figure *is* evidenced for cleared instrumental beds (Nov 2 builds + yapping Lane A rule), and a *Splice lo-fi* (not trap) bed is evidenced for the avatar/yapping lane. Final doctrine needs the Code-side skill pulled before asserting Viral specifics.
5. **Hook-caption typing conflict (Sky).** SKY_STYLE §4 (Nov 6) orders the hook to type on letter-by-letter with key sounds as "Q's standing ask"; TEARDOWN §13 (Nov 12 ship-time fixes) lists letter-by-letter hook captions as a **banned telltale** (hard cut-in ≤1 frame instead). **[RESOLVED in the Nov 13 finish pass — the later Q layer governs: Nov 12 beats Nov 6. In the Sky lane, hook captions hard cut-in ≤1 frame; letter-by-letter hook typing is banned. The SS one-click-per-word rule (§4.1) survives only for deliberately typed TEXT devices (typed hooks in non-Sky lanes, CTA typing, on-screen typing performances) — never as Sky hook captions.]**
6. **Impact budget conflict.** Three evidenced rules compete for the same scarce sound: SS "impact only at the payoff, one per video max"; MEME_GRAMMAR §15 "save the one boom for the final mic-drop line"; LD needed-list "IMPACT/slam at 0.00, frame 1" *plus* six tight impacts on verdict slams *plus* a heavy lock slam in one 68 s video. LD is a single build's needs list, not a ratified budget — the final doctrine needs an explicit per-lane impact budget. **[RESOLVED as doctrine in the Nov 13 finish pass, from Q's per-build orders: the default budget is ONE impact-class hit per video in the Sky and Viral lanes, placed on the single biggest beat — payoff OR final mic-drop line, never both, and not at frame 1. The LD pattern (frame-1 slam + verdict impacts + lock slam) is a Devin-lane build treatment Q ordered for that build; it applies when Q orders that treatment, and is not a general budget. Vine booms count against the same one-per-video budget (§1.7). Label: DOCTRINE — coordinator resolution; Q can override per build.]**
7. **Locked Doors cue-sheet count and status.** **[RESOLVED by recount in the Nov 13 finish pass: the file on disk (`locked-doors_sound-cue-sheet.md`, v7 picture) has 95 table rows = 2 headers + 93 data rows — 56 laid real-sound placements + 37 needed placements. The "119 placements" figure in the task brief does not come from this sheet (it belongs to the later v9 mix's count in a separate document). Quote 93 for the cue sheet, and keep *needed ≠ laid*: 37 of its pairings (beds, impacts, typing, chime, sting) were intentions, not sounds in the v7 mix.]**
8. **Transitions ×3 build data not found as a document.** `your_files/transitions-4/` contains only the three Viral MP4s (+ POPOUT-FIX versions), frames and the take — **no cue sheet or STACK note** pairing sounds to the transitions in those builds. §2.2 therefore rests on the Kien decode + the Nov 12 Viral Forms pack + TRANSITIONS-SHEET, not on the Transitions ×3 builds themselves. If a STACK note exists elsewhere, it was not under `transitions-4/`.
9. **SOUND_SYSTEM.md lives only in sparse clones.** No copy exists under `claude-editing/` proper; this draft read it from `~/workspace/remix-clone/SOUND_SYSTEM.md` (identical copies in `pwc-videos-stack/`, `devin-push-clone/`, etc.). Several sounds its table needs were still unlicensed at writing (glass shatter, cash register, gear shift, reload, radio beep — "searches still to run"; six more awaiting Q's OK to spend Splice credits). Pairings depending on those files are conditional on the downloads.
10. **Meme grammar is a research synthesis, not Q-corpus measurement.** MEME_GRAMMAR_45_PAIRINGS rests on YouTube/Shorts editing research and SFX-craft sources (Uppbeat download data, SoundboardGuys, LesFM, etc.) plus Q's one named example reel. Its pairings are labelled TUTORIAL throughout this draft for that reason; none were measured against Q's own posted videos.
11. **Real-sound / earshot levels come from launch films, not talking heads.** The 7-film professional launch profile (−14 LUFS, ~5 effects/10 s, logo 8–20 dB under the drop, effects 3–10 dB over *music*) is a different genre's measured norm. This draft uses it only for launch/code-made films and for the real-recording gate — importing its density into talking-head lanes would contradict §1.2's Q law and is not done here.
12. **Devin Family B bed level cannot be expressed as "under voice."** Dd3's −16.0 dBFS is a whole-mix RMS. No bed-stem or bed-under-voice offset was measured for Devin, and none for Sky's two music vlogs (bed levels there are described qualitatively: DSI5 bed fully in by 0.5 s; DSTd steps up ~14 dB at ~3.05 s). Any "Devin bed = −X dB under voice" rule would be invented.
13. **Scripture-beat sound under word-tick lanes is unspecified.** §4.6 gives the chime/silence grammar and the meme exclusion, but no source states whether Tier-1 per-word ticks continue under a quoted verse in a Viral-recipe build. **[DOCTRINE DEFAULT adopted in the Nov 13 finish pass (proposal, not an evidenced rule — Q can override): Tier-1 ticks continue under the verse at Tier-1 level; no Tier-2 pop, no meme sound, no escalation on the verse.]**
14. **Sky carousel audio:** only Archetype A section slides carry audio (the source video's own); all other video slides are silent and PWC law is "bake no music into carousel slides" — included here only to prevent a sound rule being invented for carousels. **[MEASURED — TEARDOWN §10]**

---

*Finalisation record (Nov 13, 2026): §5.5 stands as the lane-decision table. §6 items 4 (Viral skill pulled + checked), 5 (hook typing — Nov 12 layer governs), 6 (impact budget), 7 (cue-sheet recount: 93) and 13 (scripture default) are resolved inline above, each labelled with its basis. Remaining genuinely open: §6.1 (tick-tone ear-match sourcing pass), §6.2 (beat-offset distribution), §6.3 (Devin spectral pass), §6.8 (Transitions ×3 cue sheet), §6.9 (SOUND_SYSTEM unlicensed downloads), §6.12 (Devin bed offset — unmeasurable from stems that don't exist).*

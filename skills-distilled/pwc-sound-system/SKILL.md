---
name: pwc-sound-system
description: "PWC sound system: the 1,975-sound bank (catalog.csv) plus the SOUND-USAGE-MAP doctrine for WHEN each sound is used — transitions, pop-ups, edit events, word beats, intros, outros — per lane (Sky, Devin, Viral, general PWC). Auto-fires on any editing task that involves sound: adding SFX to a video, choosing a whoosh/pop/tick/riser/buzzer, building a sound layer or cue sheet, meme sounds, music beds, end cards, or sound QC. Real recordings only, never synthesised; every sound is caused by a picture event and lands beat-locked on its frame; every level sits under the voice; Sky's tick-tone has no substitute. Use it whenever an edit needs sound design, even when the user never says the word 'sound'."
---

# PWC SOUND SYSTEM

The bank + the doctrine. The bank says *what exists*; the **SOUND-USAGE-MAP.md** (beside this file) says *when each sound is used* — read the map's §0 for the bank, §1 for the universal laws, §2 for transitions, §3 for pop-ups/edit events, §4 for words/beats/intros/outros, §5 for lane dialects, §6 for the honest gaps.

## Where things live

- **Bank:** PWC-Videos repo `assets/sfx-system/` (19 category folders) · library build folder `~/workspace/sound-system-build/bank/`
- **Index:** `catalog.csv` — 1,975 rows (name, category, duration, source, provenance, original name, best use, md5). Search it; never guess a filename.
- **Summary:** `CATALOG.md` — category counts, uses, confidence notes, the 12 deliberate misc leftovers (not cleared without a listen).

## The laws (map §1 — these bind every build)

1. **Every sound is caused by something on screen.** No decorative SFX. If the pop doesn't answer "why this, why now," cut it.
2. **Real recordings only.** Code selects, trims, places, levels — code never generates a sound. Where no real sound exists and the lane permits silence, the beat stays silent.
3. **Beat-lock ≤1 frame.** Onset on the frame for hits/touches; the peak on a whoosh's apex; the end on a riser's hit. Tick-tones gate *inside* their animation windows, never on a cut.
4. **Levels sit under the voice** (map §1.4 table): bed ≈ −28 dB under speech (cleared library only); per-word ticks 28–32 dB under voice peaks, pitch-varied, downward drift per sentence; emphasis POP ~5 dB hotter than the tick; routine SFX bus per the v2.1 measured figures. Voice master: static gain to −14.5 LUFS.
5. **Consistency is the signature.** Same family for the same job every time; vary the variant/pitch on every repeat, never the family.
6. **Rationed big sounds:** ONE impact/vine-boom per video (biggest beat: payoff or final line — pick one). Buzzer/boom spam is out.
7. **Banned:** the 22 loose unknown-origin `.wav` files from PWC-Videos `assets/sfx/` (verified absent from the bank — never re-add them); trending platform-licensed sounds; profane meme audio; chaotic gaming-edit stacks; a generic tick presented as "Sky's tick-tone" (no ear-matched file exists — map §6.1).

8. **Satisfying + emotion-matched + immersive (Q, Nov 13, 2026, amended same day — ALL lanes, ALL editors: Claude Code, Muse, web Claude):** every sound chosen — SFX and transition sounds alike — must be *satisfying* in texture (low-key, tactile, smooth-decaying) AND matched to the emotion the video/beat is carrying. NOT calm-only: depending on the content the sound layer evokes hype, tension, triumph, relief, humour, awe, conviction, warmth or weight — whatever the moment is supposed to make the viewer FEEL. Sounds, transitions, motion and captions move as ONE event so the viewer is immersed in the experience, riding the video's emotional wave instead of watching it from outside. Consistent sonic signatures for recurring events build psychological attachment and keep viewers longer. Harsh/shrill/startling sounds fail QC unless the beat's emotion itself is a verdict/error — and even then they stay controlled. Repeat test: loop any cue 5× — if it fatigues or makes you flinch on a phone speaker, swap the variant, don't just lower it.

## Lane dialects (map §5 — the lane decides, never blend silently)

- **Sky:** source = dry voice, cuts silent universally, NO bed, tick-tone family only on counters/timers/count-ups/chart draws. PWC SKY-PLUS layer (labelled divergence): cleared bed −28 dB, sound on 100% of entrances AND exits. Sky hook captions hard cut-in — letter-by-letter typing is a banned telltale.
- **Devin:** two families, never collapse them. Dry studio = one SFX per device, never stacked, verdict Xs SILENT, count-ups silent, no per-word ticks. Bedded reels = bed under screen/UI stretches, not under face A-roll. Q's LD treatment (sounded verdicts, frame-1 slam) applies only when Q orders that build.
- **Viral:** the per-word tick lane — Tier-1 tick on every displayed word + hotter POP on emphasis words synced to word + zoom; cleared hype beat ≈ −28 dB under speech; spray-whoosh transition family; Water Line completes at the keyword with the E5→G5→C6 sting (~16 dB under voice peaks).
- **PWC default (no lane named):** map §5.4 stack — voice −14.5 LUFS, bed −28 dB, 100% entrance+exit coverage, per-word ticks only in word-by-word caption formats, meme pairings by situation, one dramatic transition per video, CTA performed (typing → send → notification), end card ≤1 s after the last word.

## Faith beats

Scripture/testimony: single soft chime or near-silence. No meme sound on scripture, ever; no Tier-2 pop on a verse; meme pops are excluded on scripture beats in every lane.

## Workflow

1. Build the cue list **from the picture** (every entrance, exit, move, contact frame, word beat) before opening the bank.
2. Pick sounds from `catalog.csv` by category + best-use; keep one family per job; log file names in the cue sheet.
3. Place by class mechanics (law 3); level by the map §1.4 table; pitch-variant every repeat.
4. QC on the exported file: coverage (every visual change sounded, per lane), levels under voice, beat-lock, the one-impact budget, end-card gap ≤1 s, and no banned/synthesised audio.

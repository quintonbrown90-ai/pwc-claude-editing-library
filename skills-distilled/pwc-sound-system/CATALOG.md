# PWC SOUND BANK — CATALOG

**1975 distinct sounds · 449.3 MB · 19 categories.** Every file is a real recording with provenance (no synthesised sounds). Full per-file data (duration, source, provenance, original name, best use, md5, size) is in `catalog.csv` next to this file.

Naming: `<category>_<descriptor>_<nn>.<ext>`. Levels were left as recorded; ride them under the voice per the SOUND-USAGE-MAP (levels table, §1.4).

## Categories

| Category | Files | Audio | Use for |
|---|---:|---:|---|
| clicks | 188 | 0.8 min | Cursor clicks, taps, latch/lock-ins, list-row ticks' harder sibling, card touches. |
| ticks | 47 | 0.7 min | Per-word micro-ticks, count-up runs, clock/countdown ticks, number landings. |
| pops | 116 | 0.9 min | Anything revealed: panels, chips, cards, icons popping in/out; meme pop in/out. |
| whooshes-swooshes | 130 | 1.7 min | Anything that moves: fly-ins, slides, zoom-throughs, whip pans, spinbacks. |
| typing | 73 | 1.3 min | Typed text, hook type-on (non-Sky lanes), comment/CTA typing, keyboard moments. |
| risers | 82 | 2.8 min | Builds into reveals, section changes, counters/charts rising; reverse swells. |
| impacts | 529 | 6.5 min | Landings, slams, verdict-weight hits, sub drops, door/body foley hits. Rationed: see usage map. |
| dings-bells | 98 | 2.3 min | Right-way confirmations, takeaway bells, money dings, sparkle reveals, soft scripture chime candidates. |
| buzzers-errors | 32 | 0.4 min | Wrong-way verdicts, errors, denied/blocked beats, alarms. |
| money | 44 | 0.5 min | Cha-ching class: coins, registers, casino chips under money talk, card taps. |
| camera | 17 | 0.1 min | Shutter/flash on photo beats, flash-frame transitions, before/after freezes. |
| glitch | 73 | 1.5 min | Glitch bursts, digital tears, scan/process textures, data-moshing transitions. |
| swipes-slides | 120 | 1.5 min | Swipes, page turns, writing/drawing strokes, cloth/paper movement, card slides. |
| ui-notifications | 175 | 2.1 min | Notification dings, message pops, UI selects/confirms, phone sounds, text tones. |
| intros-stingers | 127 | 2.6 min | Logo stings, openers, fanfares, celebration hits, title moments. |
| outros | 17 | 0.5 min | End-card hits, sting decays, tape stops, power-downs, faller releases, soft closing chords. |
| meme-sounds | 30 | 1.9 min | Screened meme reactions only (vine boom class, crickets, applause, record scratch, sad trombone/violin). Never on scripture, never as proof. |
| ambience-beds | 65 | 103.3 min | Cleared beds and room tones; long ambience (birds, breathing, water, wind) and foley beds. |
| misc | 12 | 2.5 min | Deliberate leftovers — see the list below. Not cleared for use without a listen. |
| **total** | **1975** | **133.8 min** | |

## Where the sounds came from

| Source | Files |
|---|---:|
| licensed-lib | 924 |
| sfx-kit-cc0 | 363 |
| earshot | 310 |
| new-sounds (Lane 2 sourcing) | 185 |
| youtube-editor-sfx | 36 |
| ghost-editor-cc0 | 27 |
| repo-reels | 25 |
| avatar-sfx | 24 |
| openfilm-sounds | 20 |
| ai-setup-sfx | 17 |
| capcut-extract | 11 |
| derived outro slices | 10 |
| repo-splice | 9 |
| repo-memes | 7 |
| meme-sounds | 4 |
| locked-doors | 3 |

Consolidated = Q's existing collections audited + deduped by md5 (licensed local library, SFX Kit CC0, Earshot bank, PWC-Videos repo Splice/meme sets, CapCut extractions, avatar/ai-setup sets, Ghost Editor CC0, YouTube Editor kit, OpenFilm). New = Lane 2 sourcing (Freesound / Kenney / OpenGameArt / SoundBible singles with per-file licences in catalog.csv, plus 5 pops extracted from Sky/Devin reels). Derived slices = outro tails cut from banked files, labelled per file in catalog.csv.

**Excluded by law:** the 22 loose unknown-origin .wav files that sat directly in PWC-Videos `assets/sfx/` are BANNED (unknown provenance) — their hashes were checked against the finished bank: **0 present**.

## Category confidence notes

- Files from the SFX Kit carry the kit's own taxonomy (sounds.json category + variant), mapped onto bank categories.
- 64 files with genuinely opaque source names (rubberduck `misc/other/weird` sets, `sfx2_goon`) were placed by an audio-feature pass (duration / spectral centroid / flatness / sweep drift) and are labelled as such in `best_use`.
- The Sky tick-tone (5,926 Hz family) has **no ear-matched local file** — see SOUND-USAGE-MAP §6.1. Do not substitute a generic tick and call it Sky's.

## misc — deliberate leftovers (12)

| File | Why it stays in misc |
|---|---|
| kenney-digital_Preview.ogg | Kenney pack preview compilation — not a one-shot |
| kenney-jingle_Preview.ogg | Kenney pack preview compilation — not a one-shot |
| kenney-casino_Preview.ogg | Kenney pack preview compilation — not a one-shot |
| oga-rubberduck-2_sfx100v2_misc_24.ogg | Opaque foley one-shot; feature pass abstained |
| oga-rubberduck-1_other_07.ogg | Opaque foley one-shot; feature pass abstained |
| oga-rubberduck-1_toilet_01.ogg | Toilet flush recording — no editing use identified |
| oga-rubberduck-1_toilet_02.ogg | Toilet flush recording — no editing use identified |
| oga-rubberduck-1_weird_03.ogg | Opaque foley one-shot; feature pass abstained |
| oga-rubberduck-3_misc_02.ogg | Opaque foley one-shot; feature pass abstained |
| kenney-rpg_Preview.ogg | Kenney pack preview compilation — not a one-shot |
| kenney-ui_Preview.ogg | Kenney pack preview compilation — not a one-shot |
| spray.wav | Feature pass suggested dings-bells; not trusted for a spray-type source — held pending a listen |

## Outros — how the category was built (17)

Reassigned whole files: digital power-down, tape-stop downlifter, faller 2s/4s soft + 4s strong, piano C-major and G-major closing chords. Sliced tails (provenance per file in catalog.csv): 4 logo-sting decays, 2 gong decays, 2 reverse-swell arrival hits, fireworks finale decay, bass-rumble decay.

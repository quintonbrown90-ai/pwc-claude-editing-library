# BRAND.md — how it should look

Sampled from the official PWC logo. These tokens are law in every lane —
captions, cards, animations, covers. A reference video's colors NEVER get
copied; every borrowed device is remapped to these.

## Palette

| Token | Hex | Job |
|---|---|---|
| Deep navy | #00214E (range to #0A1B2E) | backgrounds, panels, boards |
| PWC blue | #013B6B | gradient partner, depth |
| Teal | #14A886 / #109E90 | accents, borders, progress, glow |
| Gold | #FEE238 (deep shade #F5B921) | payoffs, pills, accents, final numbers |
| White | #FFFFFF | headlines, body text |

**NO RED — anywhere, for any reason.** (A borrowed style's red accent maps
to gold serif italic.) Full-screen boards follow the logo's diagonal
family: teal-green top-left → blue right → deep navy bottom.

## Type

- Display / hero: **Anton**
- Workhorse bold: **Poppins ExtraBold** (+ Italic for energy)
- Serif accent: **Playfair Display Bold Italic** — single semantic words
  (negations, feelings, payoffs), always gold
- Handwriting: **Caveat Bold** — notes, paper-desk
- Alternate display: Bebas Neue
Fonts ship inside the skills' fonts/ folders. No web-font substitutes.

## Placement law (1080×1920)

- NOTHING over Q's face — zero tolerance, any zoom, any transition.
- Captions/devices live in the empty space above his head by default.
- Instagram safe zones are hard limits: text x 70–930ish, y 280–1480;
  never the top bar, never the right action rail, never the bottom
  caption block. Cards anchor HIGH (bottom edge ≤ ~y1280).
- Logo in every video. On covers: handle reads **@yerrr__q** (lowercase).

## Captions

Word-by-word from the script/word file (ground truth), timed to the voice.
Designed-captions style system (pwc-designed-captions): BASE karaoke ·
SCRIPT_ACCENT gold serif italic · GLOW teal · BIG_CAPS Anton · CHUNKY_ITALIC
· HERO_BEHIND (one hero word per section, occluded by his head via matte).
Captions ANIMATE (type-on/pop/slide) — never a static stamped system; the
treatment varies by phrase meaning, which is what reads human-made.

## Sound

Dense but varied/organic — never metronome-identical. A sound on every
pop-up entrance AND exit, accents on payload words and number landings,
typing ticks on designed captions. Source: the local licensed library
(~1,250 files). Levels: voice forward; SFX/music bedded under dialogue
(−16..−14 LUFS overall; music 18–24 dB under speech).

## Motion

Every element's motion is NAMED from MOTION.md (in each skill): LINEAR,
EASE IN, EASE OUT, EASE IN-OUT, OVERSHOOT, SPRING, BOUNCE, STEPS — with the
PWC house numbers (caption pop 4–7f overshoot 92→103→100; cards 8–12f ease
out; exits 5–6f ease in; stagger 4–6f). Unnamed motion doesn't ship.

## Brand DNA — Q's style fingerprint (6 markers, every video)

Full spec: `BRAND-DNA.md` (design-system repo + pwc-design-system skill).
Training set: `examples/brand-dna/`.

1. **F1 — PWC palette on screen:** teal #14A886 + gold #FEE238 on navy
   #00214E in the video's graphic family; ZERO red (red-scan tolerance:
   ~2–7 red-dominant pixels across a whole video, as shipped on the
   viashaan demos).
2. **F2 — PWC logo present:** official logo, unaltered, in every video
   (top-left standard position).
3. **F3 — Q's face clear + present in the hook:** face on screen in the
   first 2s; NOTHING over the face at any zoom, punch, or device scale.
4. **F4 — Q's caption voice:** word-by-word, timed to speech, in the
   lane's treatment (Sky lane: bare bold white 1–3 words/group;
   designed-captions lane: karaoke-gold + style-switching; avatar lane:
   top strip, word-exact). No foreign caption style.
5. **F5 — PWC sound identity:** dense, varied, organic — SFX on every
   device entrance AND exit, accents on payoff words and number landings,
   cleared bed under the voice. Never dry-silence devices, never a
   copyrighted artist track.
6. **F6 — PWC close:** completed device held on the closing line + keyword
   CTA (WAITLIST or lane keyword, LIVE ManyChat flow) + routing to
   skool.com/paid-with-content; last spoken word → end card ≤ ~1s.

**Rule:** if any marker is missing, the render is BLOCKED until it's fixed.
A video that reads as Sky's or Adilet's instead of Q's is a brand failure
even if every technical gate passes. Mechanics are borrowed; skin is Q.

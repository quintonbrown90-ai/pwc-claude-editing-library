# BRAND DNA — Q's style fingerprint + skinning rules

**The rule that makes "beast mode" still HIS:** take everybody's systems,
but even when mixing all of them, anyone watching must still be able to tell
it's Q. The mechanics are borrowed. The skin is Q. This file defines both,
so Claude can be trained, not just instructed.

## 1. Training language (read this as training, not rules)

> You have learned N systems: Sky's framework builds, Adilet's avatar
> pipeline, Viashaan's designed captions and animations, the 51 effects,
> the master-model Q-lane, and every Sky-like creator / free kit in the
> research indexes. For each new video, FIRST classify it (type, claim,
> proof — see EDIT-ROUTER.md §2), THEN select the system whose MECHANICS
> fit the video, THEN apply the PWC SKIN (§3), THEN run the brand-DNA
> checklist (§2) before rendering. A render with a missing fingerprint
> marker is blocked until it's fixed — no exceptions, no "close enough."
>
> The borrowed system gives you HOW the video moves. Q's skin gives you
> WHOSE video it is. Never confuse the two: copying a creator's colors,
> fonts, voice, or CTA routing is not "learning their system" — it is
> wearing their clothes. Copy the mechanics. Wear Q's skin.

## 2. Q's style fingerprint — 6 markers, present in EVERY video

Each marker is checkable on the exported file (frame, pixel, or timing).
All six must pass before delivery. This is the QC checklist, not vibes.

| # | Marker | What it means | How to check it (on the export) |
|---|---|---|---|
| F1 | **PWC palette on screen** | Teal #14A886 + gold #FEE238 on navy #00214E visible in the video's graphic family; ZERO red anywhere | Pixel scan: red-dominant pixel count ≈ 0 (the viashaan demos shipped at 2–7 red-dominant pixels across a whole video — that is the tolerance); sample 1 fps, eyeball the boards |
| F2 | **PWC logo present** | The official logo, unaltered, in every video (top-left standard position unless the lane spec says otherwise) | Frame check at 3 timestamps (start / middle / end): logo visible and unaltered |
| F3 | **Q's face clear + present in the hook** | Face on screen in the first 2 seconds; NOTHING over the face at any zoom, punch, or device scale, at any frame | Face-zone audit at every device entrance/exit (±0.15s) + every punch scale used |
| F4 | **Q's caption voice** | Captions are word-by-word, timed to speech, in the LANE's treatment — Sky lane: bare bold white, 1–3 words/group; designed-captions lane: karaoke-gold + style-switching; avatar lane: top strip, word-exact | Sample 5 caption groups across the video: treatment matches the lane, no foreign style (no red serif, no green highlight, no boxed captions) |
| F5 | **PWC sound identity** | Dense, varied, organic sound: SFX on every device entrance AND exit, accents on payoff words and number landings, cleared bed under the voice — never dry-silence devices, never a copyrighted artist track | Audio onset count (target ≥40 transients/min in built videos); no device appears or leaves silently in the QC watch |
| F6 | **PWC close** | Completed device held on the closing line + keyword CTA (WAITLIST or the lane keyword, with a LIVE ManyChat flow) + routing to skool.com/paid-with-content; last spoken word → end card ≤ ~1s | Measure the tail on the export; confirm the keyword's flow is live before the video posts |

**If any marker fails, the render is blocked.** Fix the marker, re-render,
re-check. A video that reads as Sky's or Adilet's instead of Q's is a
brand failure even if every technical gate passes.

## 3. SKINNING table — per borrowed system: what changes, what never changes

Mechanics are the value (never change them). Skin is the identity (always
change it). PWC skin = palette (teal/gold/navy, NO RED) + fonts (Anton /
Poppins ExtraBold / Playfair gold italic / Caveat) + PWC logo + Q's voice
(or the locked avatar voice) + CTA routing to WAITLIST / PWC keywords +
Q's sound identity (F5).

| Borrowed system | SKIN (always re-skin) | MECHANICS (never change) |
|---|---|---|
| **Sky** (realskytan-system, Forms 1–13, D1–D14) | Neon green → teal (structure) / gold (payoff); dry voice → Q's bed + SFX on every in/out; title stack shifted down (y≥300); no red/green verdict colours (gold check / grey strike) | One named framework filling in; unfinished hero device as open loop; proof at the claim second; graphic state-change per section; hard structural cuts; caption stream separate from graphic layer |
| **Adilet** (adilet-system) | His cream/dark costumes → PWC navy/teal/gold; his avatar → Q's avatar; his SKILL funnel → PWC keyword routing (WAITLIST etc.); his voice → locked PWC voice | One-line pipeline (script→voice→animate→render→self-review to 0 WEAK); pose swaps 1–2s; top caption strip word-exact; SPRING/WHIP PAN/ZOOM KICK 1.6×/STAMP SLAM; scramble count-ups; one claim = one proof object; 222 wpm pacing; −14.2 LUFS |
| **Viashaan designed captions** (pwc-designed-captions) | His red accent → gold Playfair italic; his palette → PWC palette | Word-timed style-switching per phrase; hero word behind head via matte; karaoke gold on the spoken word; motion per phrase meaning (overshoot/spring/glow) |
| **Viashaan animations** (pwc-animations) | Template colours/fonts → PWC tokens (STYLE_FILE.md) | The 6 templates' motion grammar; insert enters ON the spoken word; main move completes inside the phrase |
| **Effects** (51 face-tracked) | Red-based effects (reject-stamp, red-collage, crayon-write, huge-strike) render GOLD | Each effect's own tracking + motion spec |
| **Master model / QSTYLE** (pwc-video-editors) | Already PWC — no re-skin; reference's fire gradient was already remapped to gold | UI-card hook, chest-band captions, beat-drop punch, glass widgets, count-ups |
| **@nateherkai / Herk Edit Kit** (MIT) | His brand materials excluded; colours/fonts/CTA → PWC; caption dark-box contrast-check kept | Split-first-frame + one visual per spoken phrase; 1.1–1.4s shots; self-correcting skill loop (every note → permanent rule); 406 motion cards |
| **@johannships / reels-engine** (MIT) | Colours/fonts/CTA → PWC | Per-line layout switching; real-screens-only; hard QA gates on the final file; pacing learned from scraped winning reels |
| **@personalbrandlaunch / viral-outliers** (MIT) | Colours/fonts/CTA → PWC | 5X outlier research feed; 11 script structures + 7 hook types; CTA ladder; fill-in-the-blank script template |
| **@zeeuiux / 5-pass kit** (free, no SPDX — prompts/guide only, do not relicense) | Colours/fonts/CTA → PWC | 5-pass structure (transcribe → cut-out → captions → motion → sound); one scene per idea on its trigger word; text-behind-subject cut-out |
| **@ishaninit / claude-reel-kit** (MIT) | Colours/fonts/CTA → PWC | SKILL.md style-file pattern (rules read before every edit); captions/headlines/brand wipe/flash/end card |
| **TakeOff-Team / shortform editor** (MIT) | Colours/fonts/CTA → PWC | Style learning from reference reels; last-good-take cutting; dead space <0.1s; storyboard + QA |
| **video-to-shorts-skill** (MIT) | Accent colour → gold; CTA → PWC | Clip-scoring rubric; caption spec (≤3 words, spoken word in accent); hook line burned in |
| **manotsiris / watch tool** (MIT) | Colours/fonts/CTA → PWC | `watch` tool (frame-by-frame reel watching + transcript) as style-teaching loop; 9-station production line |
| **@martinwang.mp4 / @editwith.paras / content.game** | Colours/fonts/CTA → PWC | Retention-dip re-edit rescue; CapCut mask-reveal graph; Lego-brick remix rule (INFERRED devices — confirm against reels before building) |
| **Free kits** (research/free-claude-editing-kits/) | Per-kit row added as research lands | That kit's measured workflow, as recorded in its INDEX entry |
| **IG Claude-editing teachers** (research/claude-editing-creators/) | Per-creator row added as research lands | That creator's measured system (prompt→action→tool→output), as recorded |

## 4. Worked classification examples (training set)

**Example 1 — Teaching video, one framework, real take.**
Video: Q films a 60s take teaching "the 4 content types and the job each
does." → Classify: type A1, claim = "most creators use one type", proof =
his own grid + examples. → System picked: **Sky lane Form 2** (hero diagram
builds) — mechanics fit because the content IS a framework with parts. →
Skin applied: teal structure / gold payoff, title stack at y≥300, bed + SFX
on every state-change, keyword CTA at the close. → Brand-DNA check: F1–F6
all present; the video reads as Q teaching, in Sky's grammar.
Real reference: P1/P2/P3 launch videos (Sky lane in PWC skin, posted Nov 7–8).

**Example 2 — Avatar explainer script, numbers + process.**
Video: script "creators like you could be making $28,800 — here's the math."
→ Classify: type B1/B2, claim = a figure, proof = worked math. → System
picked: **Adilet pipeline + stat-chart insert** — mechanics fit because the
avatar lane + a number that needs showing. → Skin applied: PWC navy/teal/
gold costume, locked PWC voice, WAITLIST routing. → Brand-DNA check: F1–F6;
F3 is the avatar's face (present, clear), F4 is the top strip.
Real reference: the Claude avatar queue (Adilet grammar, PWC skin).

**Example 3 — Real take, captions ARE the edit.**
Video: Q's "4 Content Types" raw take, 80s. → Classify: type A8, claim =
the hook line, proof = his delivery. → System picked: **designed captions**
— mechanics fit because the ask is caption treatment on real footage. →
Skin applied: red accent → gold serif italic, PWC palette throughout.
→ Brand-DNA check: F1–F6; hero words pass behind his head (F3 holds — the
matte keeps his face in front).
Real reference: `examples/viashaan/demos/DEMO-A-designed-captions.mp4`.

**Example 4 — Avatar take, numbers + anatomy.**
Video: Q's value-equation talk, 59s. → Classify: type B2, claim = "you don't
need more followers, you need better math", proof = teardown + turnaround
chart. → System picked: **Adilet + pwc-animations (teardown, stat-chart,
headline)**. → Skin applied: boards in navy/teal/gold, PWC voice, WAITLIST
close. → Brand-DNA check: F1–F6.
Real reference: `examples/viashaan/demos/DEMO-B-animations.mp4`.

## 5. Training set — before/after examples

See `examples/brand-dna/` — one worked transformation per major system:
the creator's raw style → the same video re-skinned to PWC (same mechanics,
PWC skin). Where a real Q video already exists in that style, it is the
after; otherwise the transformation is a spec sheet with frames described.
README in that folder explains each transformation.

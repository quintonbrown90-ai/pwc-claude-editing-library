# PWC Perfect Clone — Q's photoreal AI twin (Saraev intercut system)

## AUTO-ACTIVATION — ALWAYS ON (Q, Nov 11, 2026)

**This system is a standing capability, not a command.** Q will NOT
remember trigger words, prompt codes, or slash commands, and nothing
here is gated behind them. Whenever Q asks for avatar/clone video work
or ANY edit where the clone could serve — "make this video", "edit
this", "do the avatar ones", a script dropped in with no instruction
at all — Claude reaches for this system on its own, decides per line
whether real Q or clone Q serves it, and says which it used. Trigger
phrases (`/pwc-perfect-clone`, "perfect clone", "my twin") exist as
fallback only, never required. If a job could use the clone and Claude
didn't consider it, that is a miss.

## What this is

A photoreal clone of Q — his real face, his real voice — deployed the
way Nick Saraev (@nick_saraev) deploys his on-screen self: in **short
2–4 second bursts intercut with graphics and real footage**, so no
viewer ever stares at the clone long enough to tell. The full decode
is in DECODE.md (Batch 29): 3 of Saraev's recent reels, 36 scenes —
his face appears in only ~40% of scenes, in exactly two framings, on
one locked set, under one continuous voice track.

This is a NEW lane, not a replacement: `pwc-avatar-video` (the cartoon
yapping avatar) keeps its lane. This system is the PHOTOREAL lane —
clone Q reads as filmed Q. The voice clone built here also upgrades
the cartoon lane (its current stock Kokoro voices — Liam/George/
Michael across versions — are the biggest tell in Q's whole stack).

## ★ RECOMMENDED FREE/CHEAP STACK (ranked by realism-per-dollar at 2–4s exposure)

Q's ruling (Nov 11, 2026): with Saraev-style intercutting the clone
"wouldn't even stay on me that long to tell" — clone shots are short
bursts between real footage, B-roll and graphics, so the stack only
has to survive 2–4 second exposures, not long takes. Rank for THAT
standard, cheapest first. (Platform facts + verification status:
DECODE.md §4. Prices re-confirm at checkout — they move.)

### Tier 0 — $0 new spend: Higgsfield on credits Q already owns ★ START HERE
- **Face:** Higgsfield **AI Talking Avatar / AI Digital Twin** — a
  portrait photo of Q on his set becomes a lip-synced presenter;
  **Lipsync Studio** (Wan 2.5 Speak Fast) is the cheap engine:
  ~18 credits per 10s at 720p (read on Higgsfield's pages Nov 3,
  2026 — reported, re-check in-app). A whole reel needs only ~15–25s
  of clone footage ≈ **30–45 credits per reel**.
- **Identity lock:** train a **Soul ID** on Q's reference photo set
  (see Capture) so every burst is the same Q, same set, same wardrobe.
- **Voice:** Higgsfield Audio can clone Q's voice from an MP3/WAV
  sample (own voice only) — $0 route. Quality is the open question;
  A/B it against Tier 1 on a 4-second line before trusting it.
- **Drive it from Claude:** the Higgsfield MCP is already connected
  in Q's Claude.ai (Batch 28) — Generate Video/Image/Audio tools
  live. Claude can generate clone bursts inside the edit session.
- **Why it wins at 2–4s:** photo-based lip-sync's weaknesses (drift,
  expression range, hands) never survive a 3-second bottom-strip
  window under captions and graphics. Its strength — identity from
  one good photo — is exactly what the grammar needs.

### Tier 1 — $6/mo: ElevenLabs Starter (the voice upgrade) ★ THE ONE PAID PIECE
- **Instant Voice Cloning** from ~1–2 min of Q's clean audio;
  30,000 credits/mo ≈ 30 min of generated speech (a month of daily
  reels' clone lines); commercial license. Free plan has NO cloning.
- Feed the ElevenLabs Q-voice track INTO Tier 0's lip-sync (Higgsfield
  accepts audio-driven takes) — best cheap face + best cheap voice.
- This is also the permanent fix for the cartoon lane's stock voice.
- **PVC (Creator, $22/mo)** — the trained, higher-fidelity clone
  (≥30 min audio) — is an UPGRADE PATH ONLY if IVC reads synthetic
  in the 4-second blind test. Do not start here.

### Tier 2 — $0: local/open-source voice (fallback + offline insurance)
- **VoiceStudio** (open source, fully local; the tool Saraev himself
  surfaced in a decoded reel) — clones from seconds of audio, runs on
  Q's machine, $0 forever. Quality/license unaudited (DECODE G-B29-6):
  pilot it, don't promise it. XTTS-v2 / F5-TTS are the alternates.

### Tier 3 — premium alternate face: HeyGen Avatar IV (only if Tier 0 reads flat)
- The category-standard twin: clone from a single photo or short
  clip, Avatar IV adds blinks/head motion/gestures from script;
  HeyGen's own claim is most viewers can't tell it from a recording.
  Requires Q's in-app consent verification; plan prices unverified
  this pass (DECODE G-B29-3) — Q confirms at signup, his payment tap.
- Do NOT start here. Start at Tier 0+1 (≈$6/mo all-in). Escalate only
  on a failed blind test.

## CLONE CREATION

### The capture session — ONE short session on Q's normal set (~25–30 min)
Recorded once, sized to cover every tier above so Q never re-shoots
for a platform switch. Full click-level list in Q_STEPS.md; the spec:

1. **Set lock, wardrobe rotation:** his usual set, usual lighting,
   usual camera distance — the SET never changes. The wardrobe does:
   the session shoots **2–3 of Q's signature looks** (named
   generically here — his tan set look, a dark/navy look, one casual
   look; Q picks the finals). Look 1 is the "default Q" look he
   wears on camera most. Each look gets its own stills + talking
   pass (items 2–3 repeat per look), because a twin only wears what
   it was captured in — see WARDROBE & BACKGROUNDS. The set is the
   default background, not the only one: backgrounds are unlimited
   downstream; outfits are not, so they are banked here.
2. **Photo set (for Soul ID / photo twins) — shot PER LOOK:** 25–40
   sharp stills in Look 1, then the same key set (10–15 stills —
   neutral closed-mouth first, then smile / mid-sentence / serious)
   in each additional look. Head-and-shoulders + chest-up, front +
   slight left/right angles, expressions: neutral **mouth gently
   closed** (the money shot — lip-sync models animate cleanest from
   a neutral mouth), natural smile, mid-sentence open mouth,
   serious, laughing. No filters.
3. **Talking take (for video twins + voice) — shot PER LOOK:** 3–5
   minutes in Look 1 talking straight to camera in his normal
   delivery — the provided script (varied sentences, numbers,
   questions, emphasis) or his own words about PWC. Then a 1–2
   minute talking pass in each additional look (same script is fine
   — the outfit changed, the words can repeat). Natural hand
   gestures in some of it, hands still in some. These takes feed
   HeyGen-style video twins AND give clean voice audio.
4. **Voice-only take:** 2–3 minutes of the same read recorded close
   and clean (his usual mic), for ElevenLabs IVC. (PVC later wants
   30+ min — Q already has hours of clean talking-head audio on disk
   that can be assembled for it; no new recording needed.)
5. **Consent clips:** whatever each platform asks, recorded in-app by
   Q himself (HeyGen/Higgsfield consent verification). Q's face and
   voice are cloned ONLY by Q's own action — see Q_STEPS.md.

### Build order (Claude runs this once Q's capture lands)
1. Train Soul ID (Higgsfield) on the photo set; generate a 4s test
   burst on a Tier-0 line; still-frame A/B vs a real frame of Q.
2. Build ElevenLabs IVC from the voice take; A/B one line against
   real Q audio; if Higgsfield's own voice clone beats it on the
   same line, use that and skip the $6.
3. Lock the winners as **CLONE-Q v1** (Soul ID + voice ID recorded in
   the skill's working notes). Every later job calls CLONE-Q v1 —
   never re-train per video.
4. Pilot: ONE intercut video (real hook → clone burst → graphics →
   real CTA) through the full QC below → Q judges → batch.

## WARDROBE & BACKGROUNDS (Q asked Nov 11, 2026 — the rules)

**Short answer: backgrounds are unlimited; outfits are not — plan
the capture accordingly.**

### Backgrounds — unlimited
The clone renders as a clean presenter plate (Q + his mic, nothing
baked in behind him), never as a finished room. That means:
- **Composite route:** drop the plate onto ANY background — his
  real set, another room he's filmed in, a screenshot, a graphic
  world. Anywhere a camera or a capture has been, clone-Q can
  present from there.
- **Generation route:** Soul ID scenes generate Q INTO a new place
  (a different room, outdoors, a location he's never shot) when no
  real background exists.
- **Matching rules (what keeps it invisible):** the background's
  light direction and color temperature must agree with the light
  on Q's face; match grain + sharpness to the background's source
  (a phone-shot background gets phone grain on the plate too);
  keep the mic and the bottom-strip framing constant — the strip
  is the anchor the eye trusts while everything behind it changes.

### Outfits — capture-bound (the one real limit)
A twin wears what it was captured in. CLONE-Q in the default look
can only ever wear the default look — there is no wardrobe slider
after the fact. Range is decided ONCE, at capture:
- **The capture session banks 2–3 signature looks** (stills + a
  talking pass per look — see the capture spec above). Each look
  becomes a locked variant of CLONE-Q; the editor picks the variant
  whose outfit matches the real footage it intercuts with.
- **Generative re-dressing is the supplement, not the base:** Soul
  ID / image-edit routes can re-dress a burst into an outfit Q was
  never captured in, for a one-off. Burst-only (2–4s), strip
  framing preferred, and held to the SAME QC as every clone burst —
  it must pass the blind still test at burst length, or the line
  goes real or goes to a captured look. Re-dressed arms/hands in
  motion are the first place it fails; when in doubt, crop to the
  strip where they barely show.
- **Adding a look later** = a ~5-minute mini-capture in that
  outfit (key stills + one short talking pass), never a re-shoot
  of the whole session.

### Why this is not a problem (the Saraev note)
Nick's format sidesteps wardrobe entirely: ONE locked look across
every video, and nobody misses the range — the locked look IS the
brand. Q gets that same safety by default (Look 1 is the default
variant) PLUS range Nick doesn't use, because the capture banks
2–3 looks up front instead of one.

## THE SARAEV INTERCUT GRAMMAR (how clone footage is used)

Measurements from DECODE.md §2; this grammar is the product. The
clone fails or survives HERE, not in the generator.

1. **Two framings only.** (A) Full-frame talking head — hook and CTA
   positions. (B) Bottom-strip PiP: rounded-corner window, thin
   outline, bottom ~35–45% of frame, graphics/content on top. No
   other clone framing exists. Ever.
2. **Bursts of 2–4 seconds.** Never hold the clone past ~5s. Cut ON
   word boundaries, never mid-word, never mid-breath. If a line runs
   long, the picture leaves his face (graphics/B-roll) while the
   voice continues — the voice is continuous, the face is not.
3. **ONE voice track per video.** The whole video runs on a single
   audio master: either Q's real recorded voice (clone bursts are
   lip-synced TO it / generated from its clone at matched settings)
   or the cloned voice throughout. NEVER cut between real-voice audio
   and clone-voice audio inside one video — the ear catches what the
   eye misses. Strip any generated-take audio that isn't the master.
4. **Who says what (default split):**
   - **REAL Q:** the hook when he's holding proof/product; emotional
     peaks; anything with hands interacting with real objects; the
     first video of any new series/format; community-facing personal
     moments (lives, replies, Skool posts).
   - **CLONE Q:** connective narration, list items, explanations over
     graphics (Framing B), pickups and re-takes of flubbed lines,
     re-voicing an old video for a new CTA, volume lanes (daily
     tips, trial-reel variants) where the template carries the video.
   - When in doubt, real. The clone is leverage, not replacement.
5. **Matching rules (the invisibility checklist):** same wardrobe
   (the captured look that matches the real footage — see WARDROBE
   & BACKGROUNDS), set, lighting and mic position as the capture;
   same crop/scale as
   the adjacent real shots; match grain + sharpness + color to the
   camera footage (a touch of grain on clone bursts hides a lot);
   captions run UNINTERRUPTED across every real↔clone cut — caption
   continuity is what sells the swap; room tone/SFX bed never drops
   at a clone cut.
6. **Graphics carry the information.** Like Saraev: the strip/clone
   talks, the top of frame proves. A clone burst with nothing above
   it and no caption movement is a wasted, exposed clone.
7. **Disclosure hygiene:** clone content is Q, saying Q's words, for
   Q's channels — fine. Never clone anyone else; never put words in
   clone-Q's mouth Q wouldn't say on camera; follow platform AI-label
   rules where they apply (e.g. YouTube Shorts avatar labels).

## EFFICIENCY WORKFLOW (per video, once CLONE-Q v1 exists)

1. Script (any lane: Sky/CCC/Viral/Devin/manual) → Claude marks each
   line **R** (real) or **C** (clone) per §4 of the grammar, and each
   C-line's framing (A or B).
2. Real lines: Q films them in ONE short take block (or they're
   pulled from existing footage). Clone lines: generated in one batch
   (Higgsfield via MCP / Lipsync Studio; voice = CLONE-Q voice).
3. Edit in the lane's normal system (Sky protocol etc. unchanged) —
   clone bursts drop into the timeline like any other clip.
4. Clone QC (below) → standing PWC QC → deliver ONE pilot first on
   any new format; batches only after Q's OK (standing rule).

**The efficiency math to hold:** Q films ~40% of a video's lines;
the clone covers the rest in minutes; a flubbed line is a re-generate,
not a re-shoot; an old video gets a new CTA by re-voicing one line.

## QC — standing gates + clone gates (ALL on the exported file)

Standing (never waived): full self-watch before delivery;
freezedetect 0 freezes ≥0.35s; ±0.15s audits at every card/board
entrance/exit; last-voice→end-card ≤~1s; premium bar + pleasure test
+ retention read; nothing over Q's face; PWC teal #14A886 / gold
#FEE238 on navy #00214E; official logo; no red in added graphics.

Clone-specific:
- **Lip-sync check** on every clone burst in the exported file
  (frame strips at quiet→loud onsets, per the standing sync gate) —
  a burst that fails sync is re-generated or swapped to real, never
  shipped "close".
- **Face-exposure audit:** list every clone segment + duration from
  the final file; any burst >5s = redo; total clone face time should
  sit near ~40% of runtime, Saraev-style.
- **Blind still test:** one clone frame + one real frame, same
  framing — if the clone frame is identifiable at a glance (skin,
  teeth, hairline, mic edge), that burst gets grain/match treatment
  or goes real.
- **Voice continuity listen:** full pass on headphones for voice
  timbre jumps at cuts; any jump = the master-track rule was broken.

## HARD RULES (clone content obeys everything standing)

- Numbers only from Q's real verified proof — placeholders, never
  invented; **no million-dollar claims** (Q has NOT made a million;
  earnings phrasing stays "close to half a million off content").
- The hidden UGC earnings app is **never named** in public content —
  clone-Q doesn't name it either. Blur law applies to any proof
  shown over clone segments, same as real segments.
- CTAs per the standing brief (WAITLIST → Dec 7 doors, Premium
  $97/mo, no "link in bio", no join-now before Dec 7).
- Q+Kiya's own proofs as-is per the standing asset rules; other
  creators' media never framed as endorsements.
- The clone never appears in couples content as a fake "real moment"
  with Kiya — clone lane is Q's solo talking-head formats.

## Relationship to the existing stack

- **pwc-avatar-video:** unchanged cartoon lane; swap its voice to
  CLONE-Q's ElevenLabs voice when Q approves the clone — biggest
  single quality jump available to that lane.
- **Edit lanes (Sky/CCC/Viral/Devin):** unchanged systems; this part
  only changes WHERE face footage comes from on C-lines.
- **Queues:** clone-eligible items in `claude_avatar_posts/queue.json`
  get produced through §Workflow; trial-reel pool rules unchanged
  (trial reels are app-only, Q posts them).
- **Fable/Higgsfield motion layer (Batch 28):** complementary —
  motion layer makes the graphics that fill the top 55–65% of frame
  while clone-Q talks in the strip.

## GAPs (from DECODE.md §6 — do not paper over)

Nick's own clone platform/voice/capture are unconfirmed publicly
(G-B29-1/2); HeyGen pricing unverified (G-B29-3); Higgsfield credit
costs reported, re-check in-app (G-B29-4); ElevenLabs prices
corroborated from the official page by third-party reads, re-confirm
at checkout (G-B29-5); VoiceStudio unaudited (G-B29-6); Soul ID set
size from a third-party walkthrough (G-B29-7) — the capture protocol
overshoots it deliberately.

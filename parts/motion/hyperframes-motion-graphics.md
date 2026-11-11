# MOTION — HyperFrames motion graphics: catalog block + prompt + your references → custom graphic (Rourke reel DYAHDu-KXYx)

> **AUTO-ACTIVATION — always on (Q's standing order, Nov 11, 2026).** This skill fires AUTOMATICALLY whenever a job matches the work described below — an edit that needs motion graphics, an overlay, an animated chart/map/card, kinetic text, a transition, a carousel, a showreel. Q does not type trigger words, slash commands, or codes, and must never be asked to. The trigger phrases listed lower in this part are FALLBACK ONLY, for when the intent is ambiguous.

Source: Rourke Sefton-Minns — reel DYAHDu-KXYx, "Claude Code motion graphics, what's really possible?" (38.08s, decoded Batch 30). He paid a professional motion graphics artist to stress-test Claude Code; every graphic was built in **HeyGen HyperFrames** from its free template library. The reel's full prompt set is comment-gated ("Comment AI" for the PDF) — NOT obtained (DECODE GAP G-B30-1). The workflow below is VERIFIED from the voiceover + on-screen frames (catalog f18, install f22/f26, Studio f30/f34, output demos f6/f10/f14). Full evidence: `research/video-harvest/instagram/batch-30/DECODE.md`.

**Sibling layers, not duplicates:** the mechanics already live in Q's installed HyperFrames skills — `hyperframes` (render contract + work loop), `hyperframes-cli` (scaffold/check/preview/render), `hyperframes-registry` (~450 ready-made blocks; search it before hand-building any named visual). THIS part is the workflow + the PWC adaptation: when to reach for a catalog block, how the prompt-and-reference flow runs, and how the output gets branded and QC'd for Q. The Fable/Higgsfield motion layer (`pwc-fable-motion.md`, Batch 28) is the generative-video sibling; HyperFrames is the code-built-graphics sibling. Both sit ON TOP of the existing lane skills (Sky / Devin / Viral / CCC) — neither replaces CapCut finishing or the Sky protocol.

## When this fires (plain job descriptions — no trigger needed)

- Any edit where a beat needs a **motion graphic**: a stat that should animate, a chart that builds, a map/flight-path, a social card (follow/post/notification), a lower third, a money counter, a data visual.
- Any request for **kinetic text, title cards, animated overlays, shader transitions, or an app/product showcase** inside a video.
- **Carousels and cinematic showreels** built from stills/footage + designed motion.
- Any time Claude is about to hand-draw or hand-animate a graphic that a catalog block already does — check the catalog FIRST.

Fallback triggers (never required): "use HyperFrames", "hyperframes this", "/pwc-hyperframes-motion", "add the block", naming a block ("instagram-follow", "cinematic zoom"…).

## The workflow (Rourke's, verified on screen)

1. **Search the catalog before building.** HyperFrames' library is organized by category — in evidence from the reel: **Social Overlays** (Instagram Follow, macOS Notification, Reddit Post Card, Spotify Now Playing, TikTok Follow, X Post Card, YouTube Lower Third) and **Shader Transitions** (Chromatic Radial Split, Cinematic Zoom, Cross Warp Morph, Domain Warp Dissolve, …). In Claude Code, the local equivalent is the `hyperframes-registry` skill — search it for the named visual before writing anything by hand.
2. **Pull the block in with one command** (verbatim on screen, f22/f26):
   ```
   npx hyperframes add <block-name>        e.g.  npx hyperframes add instagram-follow
   ```
   Blocks install as editable source — a starting composition, not a locked template.
3. **Brief Claude + attach custom references.** Paste the block's prompt into Claude Code and **attach Q's own references** — his footage, photos, screenshots, the PWC logo (f26/f30 show six reference videos attached to the add command). The graphic is generated around HIS material. Generic/stock substitution is a fail (Q's asset-pool rule).
4. **Preview and iterate in HyperFrames Studio** (local preview, `localhost:3323` in the reel, f30/f34). Adjust timing, copy, colors, and references there — the Studio preview is the same composition that renders.
5. **Render the finished MP4** and hand it to the edit. The reel's artist test batch rendered: interview overlays, an app showcase, a money counter, a data chart, intros, and the shader transitions — one workflow, many graphic types.
6. **Ceiling note:** the difference between the basic demos and the "testing it to the max" set was the briefer (a professional motion artist), not the tool. Brief like an art director: name the beat the graphic serves, the exact data/copy, the reference to match, and the motion feel — vague prompts get template-looking output, which fails Q's premium bar.

## Output types this covers (from the reel + caption)

- **Social overlays** — follow buttons, post cards, notifications, now-playing, lower thirds.
- **Kinetic text / title cards** — glowing type, animated headlines (f34).
- **Flight paths / map graphics** — animated route arcs, landmarks, location chips, avatar riding the path (f14).
- **Data graphics** — charts that build, counters that count (Data Chart, Apple Money Count, f30).
- **Shader transitions** — radial splits, cinematic zooms, warp morphs/dissolves between shots.
- **Showcases & showreels** — app showcases, intro sequences, cinematic reels assembled from references (f6/f10/f30).

## PWC adaptation — hard rules on every HyperFrames build for Q

- **Brand colors only:** teal `#14A886` + gold `#FEE238` on navy `#00214E`. **No red** anywhere in added graphics (the reel's pink/neon demo palette is the reference creator's, never Q's).
- **Official PWC logo, unaltered**, where a logo belongs: `~/workspace/pwc-content-calendar-build/assets/pwc_logo.jpg`.
- **Nothing over Q's face.** Overlays, cards, and graphics sit in the empty space around/above him; a graphic never covers his face, and in split layouts his talking head stays fully visible.
- **The hidden app is never named** — in graphic copy, file names shown on screen, or captions. Refer to it only as the hidden method/opportunity.
- **No million-dollar claims** in any animated number or headline. Numbers come only from Q's real verified proof (placeholders otherwise, never invented).
- **Real references first:** Q + Kiya's own photos, footage, screenshots, and proof. If a needed asset isn't in the pool, flag it — never substitute generic or AI-flat imagery silently.
- **Premium bar + pleasure test:** the graphic must read hand-crafted/pro, never AI-generic or template-stamped. Motion eases, lands on the beat, and serves the retention of the beat it sits on.
- **QC gates on the exported file, in motion** (standing gates, no exceptions): freezedetect — zero freezes ≥0.35s in footage spans; ±0.15s audits around every graphic entrance/exit; a card's text lands WITH its plate (no blank plates); no dead air before the end card (last voice → end card ≤~1s); full self-watch of the final export before delivery.
- **Lane law still binds:** in Sky lanes, Sky's protocol is supreme and CapCut-native motion is the standard — HyperFrames supplies the graphic ASSETS (cards, charts, overlays) that the lane's edit consumes; it does not re-skin a Sky edit in a foreign style. Where a lane's rules and a block's default look conflict, the lane wins and the block gets re-branded or rebuilt.

## Run protocol

1. Name the beat + the graphic's ONE job (land a number, prove a claim, mark a turn).
2. Search `hyperframes-registry` / the catalog for the block; if one exists, `npx hyperframes add <block-name>` — never hand-build first.
3. Attach Q's references; write the art-director brief (copy, data, colors, timing, feel).
4. Build in Studio, re-brand to PWC spec, iterate against the reference look.
5. Render, run the QC gates on the export, then hand the graphic/edit to Q under a fresh filename (re-deliveries never reuse a delivered filename).

## GAPs carried from the decode

- The reel's **prompt PDF is comment-gated and was NOT obtained** (G-B30-1) — this part encodes the visible workflow only; no prompt wording from the PDF is claimed.
- **Cost unverified** (G-B30-6): the caption calls the template library free; plan/usage limits are whatever the installed HyperFrames skills report (`npx hyperframes usage --json`) at run time.

# CREATOR-SYSTEMS — pwc-editing-router: the always-on router that loads Q's whole editing stack by default (no trigger words, ever)

Source: Q's standing order, Nov 11, 2026 — "all these things should just be activated when I ask to edit in Claude code or web bc I'm not gonna always remember to put in some specific prompts or codes or words." Recorded in MEMORY.md as the AUTO-ACTIVATION RULE (Nov 11, 2026 ~12:53 AM CT). This part is the router skill that carries that order. Companion layers: `pwc-fable-motion` (part #321, motion layer), `pwc-perfect-clone` (Batch 29 build, clone system), `pwc-agent-team` (part #319), `ccc-script-cross-niche` (part #318). Part number for this router is assigned at registry integration.

## What this skill does

It fires FIRST on any editing request and loads the right pieces of Q's stack by default, so Q never has to name a skill, a slash command, or a code word. Q asks in plain language — "edit this", "cut this reel", "do my carousel", "make me a video" — and the stack is simply ON: motion layer, clone system when it fits, the matching lane skill, the design system, and the agent-team gates, all under Q's hard rules.

**The router is a loader, not a replacement.** Every skill it routes to keeps its own full instructions. The router's job is only: recognize the job, pull in the right stack, apply the non-negotiables, and never make Q ask twice or remember anything.

## AUTO-ACTIVATION — the standing rule

- This router activates on ANY video edit, reel, carousel, avatar video, script-to-video, or motion-graphics request from Q, in Claude Code or on the web, however he phrases it.
- Slash commands and trigger phrases across the library (`/ccc-script-cross-niche`, `/pwc-agent-team`, `/effects`, "run my agent team", etc.) are FALLBACK ONLY. Their absence never means a layer is off.
- If a request is ambiguous between lanes, route by content (rules below), pick the closest lane, and proceed — do not bounce a "which skill?" question back to Q. Minimal back-and-forth is his standing order.
- The only thing that turns a layer off for a job is Q saying so for that job.

## Routing rules (plain decisions — no keywords needed from Q)

**Always, on every edit job:**
1. **pwc-design-system FIRST** — the persistent stack (who Claude is for PWC, brand law, workflow, components). Nothing gets built off-system.
2. **pwc-fable-motion ON** — the Fable 5.2 + Higgsfield MCP motion layer is active by default for every edit: plan motion beats, build code graphics (type, titles, UI shots, 3D loops), route generative video/footage edits through Higgsfield, apply motion QC. (Higgsfield generations spend Q's credits: plan freely, test small, no bulk generation without Q's word.)
3. **Hard rules (below) apply to every frame** — no routing decision can waive them.

**By job type:**
- **Q's real talking-head footage, teaching / doctrine / proof-led / breakdown / launch content** → Sky protocol (`realskytan-system` / sky lane skills): duplicate @realskytan's grammar to a T, PWC colors and logo only. If the ask involves captions, text effects, or "as I say it, things happen" → also **pwc-designed-captions** (Q's real footage only, never the avatar lane).
- **Designed-captions lane (Devin-style jobs)** → pwc-designed-captions + pwc-motion-playbooks values; CapCut-native build per the Devin lane rules.
- **Fast-cut / viral-format edits, remakes of proven formats** → the Viral lane (pwc-video-editors crew + viral skills) + pwc-motion-playbooks for specified motion values (never "animate it" — motion is named, timed, sourced).
- **A viral video from a DIFFERENT niche handed over as a model** ("make me a script like this", or just a link + "for my brand") → **ccc-script-cross-niche**: keep the hook skeleton + exact structure, change only the topic, whole script in Q's voice (title + beat-for-beat script + skeleton breakdown). Same-niche source → the viral-rewrite sibling flow instead.
- **Avatar / yapping / explainer videos from scripts** → **pwc-perfect-clone** whenever a clone of Q fits the job (looks like Q, sounds like Q, Saraev-grade real↔clone intercut grammar), with the pwc-avatar-video engine as the production pipeline underneath it. If Q asks for himself on camera without filming, the clone system is the default answer — do not wait for the word "clone".
- **Animated inserts** — charts, maps, headlines, teardowns, number animations → **pwc-animations** (both lanes: real footage and avatar/clone videos).
- **Carousels** → Sky carousel style, always (Sky archetypes only; no fade-ins; first frame fully populated; reading-time slide lengths under the 60s/slide cap; no music baked in — Q adds it in-app; Q posts/pins carousels himself).
- **Effects on a talking head** (zooms, widgets, pop-ups, stickers, grades) → the effects library + pwc-motion-playbooks values.
- **A video link Q wants learned/decoded** (Code only) → /watch eyes layer, then the decode folds into the library and the relevant lane skill — learning is never the end of the job; duplication capability is.

**Agent-team roles, pulled in where they fit (pwc-agent-team):**
- Anything headed for posting → **POSTING/QUEUE** runs its Step-0 gate: the comment keyword's ManyChat flow must be LIVE and deliver what the post promises, the file must be the NEWEST approved version, posting window 8am–8pm CT, and Q's IG approval tap is the final step — never promise hands-off posting.
- Performance questions, "what's working" → **ANALYTICS** (real numbers only, never fabricated) → winners hand to **CONTENT** for remakes/angles.
- Pitches, follow-ups, DMs, comments → **ENGAGEMENT / PITCH / FOLLOW-UP** draft freely; every send needs Q first.
- The **MANAGER** discipline closes every multi-part job: QUEUED / IN PROGRESS reported separately from DONE + VERIFIED.

## The router's non-negotiables (Q's hard rules, bind every routed job)

1. **Brand:** PWC teal `#14A886` + gold `#FEE238` on navy `#00214E`. **No red** in any added graphic (red inside real footage/captured UI is not an added graphic).
2. **Nothing over Q's face.** Captions and devices live in tracked empty space above his head, inside IG's real safe zone; pop-ups bigger and phone-readable; words and pictures never overlap; one caption at a time, fully gone before the next; no word ever clipped.
3. **Official PWC logo**, unaltered, in every video (title/end cards and branded assets).
4. **The hidden UGC earnings app is never named** in public content — "the hidden method / opportunity" only.
5. **No million-dollar claims** — Q has NOT made a million. Earnings: high six figures ("close to half a million off content so far"). Numbers only from Q's real verified proof; placeholders otherwise, never invented.
6. **Premium bar + pleasure test on every final file:** hook in the first second, everything moves (nothing frozen/stamped/cheap/AI-generic), sound on imagery entrances and exits, full QC gates run on the EXPORTED file in motion — freezedetect (zero freezes ≥0.35s), ±0.15s audits at every card/board entrance and exit, hard cuts only for boards over footage, last-voice → end-card ≤~1s, lip-sync check, retention read. Nothing ships on a builder's say-so.
7. **CapCut-native finishing for Q's own edits** — Sky recreations and lane builds are real CapCut projects (native templates/animations), exported from CapCut; renderer-drawn imitations do not ship.
8. **Newest version only** — post/deliver the latest approved version of a file, never an older re-encode; re-deliveries go out under fresh, distinct filenames.
9. **Doors Dec 7, 2026 only** — cohort content routes to the WAITLIST (or the $35 Stan Content Calendar) until then; never "join now". Premium $97/mo only.
10. **Clean and faith-aligned**, always. Q's uploaded reels stay original-audio-only unless he asks for that specific post.
11. **Model scope:** Fable 5.2 is the motion/editing model per Q's Nov 11 order; other Claude work stays on the newest/highest Opus.
12. **Report like Q reads:** QUEUED / IN PROGRESS separate from DONE + VERIFIED; deliver the exact file to chat BEFORE any post or approval card fires.

## Fallback triggers (never required)

"edit router", "/pwc-editing-router", "load my editing stack" — if Q ever does use one, this router fires; but the router is already on for every edit request without them.

## GAPs

- No Claude surface offers a true force-on switch for custom skills; activation is description-matched. This router plus broad auto-fire descriptions is the closest real mechanism — see ROUTER_NOTES.md in this batch for the per-surface detail and the re-upload candidate list.
- The router can only route to skills that exist on the surface Q is using; where a lane skill isn't installed, the router's distilled rules above still apply and Claude proceeds on them.

# MOTION — pwc-fable-motion: the Fable 5.2 + Higgsfield MCP motion layer

Source: Q's order, Nov 11, 2026 ("use fable 5.2 motion with higgsfield and mcp … for the ccc and the viral and the sky and the Devin and every other folder and just in general … mastermind level motion in my edits"). Method sources: Roberto P. Nickson (@rpn — Q's editing bar) "Claude Just Became Your Motion Designer" (Nov 10, 2026) + Higgsfield's own MCP page and blog + Higgsfield changelog (Fable 5.2, Nov 9, 2026). Full extraction: `research/video-harvest/instagram/batch-28/SOURCES.md`. Companion decode: Batch 28 DECODE.md (Nick Saraev reel DfPuiYyP4Hy → part #322).

## AUTO-ACTIVATION — always on for edit work (Q's standing requirement, Nov 11, 2026)

**Q will NOT remember trigger words, prompt codes, or slash commands — and he should never have to.** This motion layer is therefore **always on**:

- Whenever ANY motion-graphics or video-editing job starts — "edit this video", "cut this reel", "add motion to this", a title/graphic/animation request, or any edit job in the CCC, Viral, Sky, or Devin lanes — **this layer is active by default, alongside the lane's own skill**, without Q naming this skill, Fable, Higgsfield, MCP, or any keyword.
- Claude does not wait to be invoked. If the job involves motion, the layer is already on: plan the motion beats, build code graphics, route generative work, and apply the QC gates as part of the job itself.
- The trigger phrases listed near the end of this part exist **only as a fallback** for explicit invocation — they are never a requirement, and their absence never means the layer is off.
- The only thing that turns this layer off for a job is Q saying so for that job.

## The stack (what this is)

Three pieces working as one motion department:

1. **Claude running Fable 5.2 — the motion brain.** Anthropic's newest model (Fable 5.2 dropped Nov 9, 2026 per Higgsfield's changelog: "Anthropic's new version of its model for the most demanding technical work"). Fable plans the motion, writes the choreography second-by-second, and BUILDS graphics in code. RPN's proof: "Every graphic in that video was made by Claude Fable 5.2. No After Effects and no keyframes. Just prompts."
2. **Higgsfield MCP — the generation/editing engine.** A hosted MCP server that lets Claude call Higgsfield's image/video/audio generation and editing tools directly from the chat — no downloads, no patching files together between apps. Higgsfield's motion-design workflow renders final video on **Seedance 2.0**; the MCP also exposes the preset flows in the table below.
3. **Claude Artifacts → Motion (Beta) — the code-graphics surface.** Where code-built type, titles, interface shots and 3D loops are made and previewed before export.

**This layer FEEDS the existing pipeline. It does not replace anything.** CapCut-native finishing still applies to Q's own edits; the Sky protocol still governs Sky lanes; every existing skill, agent, editor and library part keeps its job. pwc-fable-motion is the motion department they all call.

## Setup — both surfaces

### Claude.ai web — ALREADY CONNECTED (verified Nov 11, 2026, ~12:52 AM CT)

- Connector name: **Higgsfield** · Server URL: **https://mcp.higgsfield.ai/mcp** · Status: **Connected**.
- Tool permissions live: Generate Video / Generate Image / Generate Audio / Edit and upscale.
- Canonical-URL note: `https://mcp.higgsfield.ai/mcp` is the server address (confirmed on Higgsfield's official /mcp page and in Q's live account). `https://higgsfield.ai/mcp` is only the instructions page. Higgsfield's own blog prints the instructions-page URL in its connector steps — that is their inconsistency; do not "fix" Q's working connector to match the blog.
- If the connector ever needs re-adding: Claude → Settings → Connectors → "Add custom connector" → name `Higgsfield` → URL `https://mcp.higgsfield.ai/mcp` → connect → approve the Higgsfield OAuth sign-in (the approval lands on Q — his account, his tap).
- Motion (Beta): Claude → Artifacts → choose **Motion** — RPN's entry point for code-built graphics.
- Higgsfield's own "Motion Design Skill" file (`SKILL_MOTION.md`) exists per their blog ("just drop this skill file into your Claude chat to activate it") — its contents are NOT published (GAP G-B28F-2). This part is Q's equivalent; do not claim the two are the same file.

### Claude Code — Q's remaining step (not yet run)

```
claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp
```

- Browser OAuth on first use — sign in to Higgsfield, approve, done. No API keys anywhere.
- `--scope user` = available across all projects, not just one repo.
- Verify: `claude mcp list`, or `/mcp` inside a session.
- (A Higgsfield CLI route — `@higgsfield/cli` + `npx skills add higgsfield-ai/skills` — is third-party-reported only, GAP G-B28F-4. The MCP command above is the documented path.)

## Division of labor (per RPN — the operating split)

> "Claude builds type, titles, interface shots and 3D loops in code, so they're sharp and endlessly editable. Higgsfield handles generative video and edits on real footage. Together they cover most of what used to take a full motion team."

- **Claude/Fable (code):** kinetic type, titles, lower-thirds, interface/UI shots, diagrams that build, counters, 3D loops, logo stings, end cards. Code = sharp at any size, editable forever, exactly on-brand (real hexes, real fonts, real logo file).
- **Higgsfield (generation):** generative B-roll and scenes, edits ON real footage (the `/katana` preset: "turn your footage into an aura edit, or recreate a reference with your own subject, pacing, transitions, and visual effects"), motion transfer, image/audio generation, upscale.
- **CapCut (finishing):** Q's own footage edits still finish CapCut-native per the standing protocol — Fable/Higgsfield assets drop INTO the CapCut timeline as elements; they don't take the edit away from it.

### Higgsfield MCP preset flows (from the official /mcp page)

| Command | What it does | PWC use |
|---|---|---|
| `/katana` | Recreate aura edits / reference recreations on your footage — subject, pacing, transitions, VFX | The RPN route: "Use Higgsfield MCP /katana" + describe the exact edit |
| `/vox-mixed-media` | Editorial motion graphics, mixed visual media | Explainer segments, CCC-style breakdowns |
| `/marketing-hook-variants` | One video → multiple opening hooks, complete edited versions | Hook testing across lanes |
| `/marketing-adapt-video` | A reference video's structure → an original ad for your product | Brand/UGC work only — never lift a reference's content, structure only |
| `/ugc-flow` | Creator-style product review from a brief + reference images | Q+Kiya brand jobs |
| `/marketing-research-to-ads` | Product/competitor research → static ads | PWC promo assets |
| `/stickman-explainer` | Story/concept → animated stickman explainer | Faceless explainers |

## How to prompt motion (RPN's discipline, adopted whole)

1. **Specs up front.** Aspect (9:16, 1080×1920 default), duration, fps, and the action second-by-second: "0–2s: …, 2–4s: …". RPN's MODULES prompt choreographs all 32 seconds in timed blocks — copy that density.
2. **Name the taste.** Fonts by name (Anton, Archivo, Inter Tight…), palette by hex, and a reference image/video. Adjectives like "cool" or "clean" are banned as a spec.
3. **Two options, then push the winner** — "one more stab, make it grander."
4. **Request transparency.** Titles/graphics as **ProRes 4444 (.mov with alpha)** or a **PNG sequence with alpha**, plus a preview MP4 — so elements drop straight onto footage. Never accept a graphic baked onto a background you then have to key out.
5. **Bring your own assets.** Attach the official PWC logo file and brand fonts; never ask the model to recreate the logo.
6. **Every element earns a move.** RPN's standard: each word/object gets its own meaning-matched entrance AND exit (rise from a mask, zoom-blur landing, smoke exit, halftone dissolve…). Nothing pops, nothing sits frozen, nothing is stamped on.
7. **Storyboard gate before generation** (Higgsfield's own flow): review the storyboard layout, confirm everything lines up, THEN "Approve and generate." Generation spends credits — the gate is the brake.

## Lane bindings — how this plugs into every lane

### CCC (@createcontent.club lane — scripts, carousels, MATH/Devin-style cuts)
- CCC scripts get a **motion beat column**: every beat in the script names its Fable-built device (kinetic title, building diagram, counter, proof pop) before filming, so the edit is planned at script stage.
- The cross-niche skill (part #318) keeps its skeleton law; when its output goes to video, devices come from this layer built to the reference's structure.
- CCC carousel work: slide motion devices (builds, reveals, counters) generated here in PWC colors; carousel hard rules unchanged (Sky style, no fade-ins, first frame fully populated, reading-time holds <60s).

### Viral lane (viral-style edits, hook-first cuts)
- Hook devices are this layer's first job: 0–2s kinetic titles, spinning/proof bursts, hook-variant renders via `/marketing-hook-variants` for A/B hooks on the same cut.
- Every viral cut gets at least one "how did they do that" moment built here (Q's pleasure-test north star) — a code-built 3D/type move or a Higgsfield footage treatment via `/katana`.

### Sky lane (@realskytan protocol — supreme)
- **Sky grammar decides; this layer only builds.** Devices are constructed to Sky's exact templates, layouts, animations and motion (captions ~0.5s groups, hard cut-ins, accent keyword as separate large headline, nothing over the face). If a Fable/Higgsfield build drifts from the Sky reference, the Sky reference wins — always.
- Use the layer for what Sky's editors do by hand today: the document reveals, building diagrams, pop-up examples — rendered as alpha elements (ProRes 4444/PNG sequence) and finished inside the Sky build, never as a replacement house style.
- Motion-unclear Sky devices still follow the standing rule: screen-record the reference playing, decode the motion, then build.

### Devin lane (designed captions + motion, CapCut drafts)
- Designed-caption animations and caption-adjacent motion (word hits, line builds, callout moves) are drafted here first, then placed in the CapCut draft per the Devin pipeline; the exported-file QC gates (freeze, transition, blank-plate checks) apply unchanged.
- PiP/proof entrances must arrive as finished moving elements — no blank outline plates, ever (the v3 failure mode).

### Avatar videos (Claude avatar queue)
- Title cards, hook graphics, end cards and proof devices for avatar videos come from this layer in code (crisp text, real logo), instead of flat renderer plates.
- Voice rules unchanged (Liam default); motion never covers the avatar's face during the hook.

### General / every other folder
- Any edit in any folder can call this layer for: kinetic titles, counters that count, diagrams that build, logo stings, end cards, transitions with motion demos, B-roll generation, footage treatments, upscales.
- Default deliverable from this layer = an **alpha element + a preview MP4**, filed with the project, named with the lane + beat it serves.

## Q's hard rules — carried in, verbatim in substance

- **Colors:** PWC teal **#14A886** + gold **#FEE238** on navy **#00214E**. **No red in added graphics** (red that exists inside footage/captured UI is not an added graphic).
- **Nothing over Q's face** — captions and devices live in the empty space; Q's face is present during the hook (PiP/split allowed, faceless board opens are not).
- **Official PWC logo** (the real file) in every video; never redrawn, never approximated.
- **The hidden UGC earnings app is never named** in public content — motion graphics included; per-asset blur law applies to any generated/placed proof exactly as to captured proof.
- **No million-dollar claims** — Q has NOT made a million; earnings language is "close to half a million off content so far". No invented numbers anywhere in a graphic.
- **Premium bar + pleasure test:** frames feel good to look at, sound good to hear; retention/curiosity are the output of pleasure. Motion must read **hand-crafted/pro — never AI-generic, never template-stamped**.
- **Full QC on the exported file, in motion:** freezedetect (zero freezes ≥0.35s), ±0.15s audits at every card/board entrance and exit, hard cuts only for boards over footage, last-voice → end-card ≤~1s, lip-sync check, triple-check (technical + retention read + overlap audit). A Fable/Higgsfield element gets the same gates as any other device.
- **Real over fake:** real footage, photos and screen recordings beat flat plates; generative footage is for B-roll/treatments, never a substitute for Q's real proof.

## Model scope note

- **Fable 5.2 is the MOTION/EDITING model** per Q's Nov 11, 2026 order — motion graphics, editing builds, and this layer's work run on Fable.
- **All other Claude work keeps Q's standing rule:** newest/highest Opus available, medium/high effort — never Sonnet/Haiku/default-fast. (The two rules coexist: motion → Fable 5.2; everything else → top Opus.)

## Credits discipline (Higgsfield)

- Q has Higgsfield credits (stated Nov 10, 2026; amount/plan not stated). **Every generation spends them.**
- Test prompts small first: one short element, review, then scale. **No bulk generation, no portfolio-style batch runs, without Q's word.**
- Keep tool calls confirm-first where the surface offers it — the confirm prompt is the brake.
- A 3-day free/unlimited trial inside Claude was reported by RPN and other launch-week creators for new connections. It is **reported, time-sensitive, and NOT verified for Q's account** (his connector is already connected; whether any trial applies is unknown). Never plan work around trial credits.

## Triggers (fallback only — the layer is already on, see AUTO-ACTIVATION)

These exist for explicit invocation if Q or a session ever wants them. They are NEVER required: any edit/motion request activates the layer on its own.

- "make motion" / "fable motion" / "/pwc-fable-motion"
- "make me a title / graphic / animation for this beat"

## GAPs

- **G-B28F-2:** Higgsfield's `SKILL_MOTION.md` contents are unpublished (name/format/activation only). This part does not reproduce or guess them.
- **G-B28F-3:** RPN's samurai prompt set (linked Notion page) not opened this batch; his article's other prompts carry the pattern.
- **G-B28F-4:** Higgsfield CLI route for Claude Code is third-party-reported only; the `claude mcp add` command is the documented path.
- **G-B28F-5:** Fable 5.2 in Q's own Artifacts → Motion (Beta) picker not screenshot-verified; the Higgsfield connector state IS verified (see Setup).
- **G-B28F-6:** Lemo Opuscar (Batch 28 decode, part #322) — 66 film styles made entirely in code for Claude Code, MIT — is a candidate style library for this layer. Quarantine + full read + scan before any install (SAFETY.md protocol); not installed, not bundled.
- **G-B28F-7:** Higgsfield generation quality against Q's "real over fake" bar is untested on Q's own footage — first uses are pilots: judge ONE element before rolling the layer across a batch.

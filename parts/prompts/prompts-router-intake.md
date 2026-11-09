<!-- PART: prompts/prompts-router-intake.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# PROMPTS — the router intake (paste-ready)

Source: `design-system/EDIT-ROUTER.md` — an 11-question paste-ready
variant of the router's 12-question intake (§2), not a verbatim copy.
Count note (v11): router Q2 (named system/framework name), Q5 (power:
number / story / proof / breakdown), and Q11 (viewer feeling →
psychology part) have no paste-ready equivalent here, while part Q4
(audience) and Q8 (hook in first 2s + face on screen) are part-only
additions — for the full 12-question intake, use EDIT-ROUTER.md §2.
Ask before you build when the video type is ambiguous.

## The prompt (paste as-is)
```
Before you edit, classify this video and recommend the edit:
1. What type is it (talking-head proof / launch take / avatar explainer /
   carousel / UGC brand video / series episode / other)?
2. What is the ONE claim, in the speaker's exact words?
3. What proof object shows that claim on screen, and at what second?
4. Who is the audience (creators under 10K / buyers / waitlisters)?
5. Which lane (main launch / avatar / proof-led / carousel / trial)?
6. What is the comment keyword, and is its ManyChat flow live?
7. Is there a real screen, screenshot, or photo to show — or only talk?
8. What is the hook in the first 2 seconds, and is Q's face on screen?
9. What should the viewer DO at the end (keyword + bio-line CTA)?
10. What must NOT appear (hidden app name? brand names? faces to blur)?
11. Which assets does this edit need (Q/Kiya photo, video, proof, B-roll,
    brand asset)? If one is missing, ask Muse for it — never substitute
    generic/AI/stock, never invent a placeholder, never skip it silently.
Answer with the RECOMMENDATION shape in EDIT-ROUTER.md §6: style pick +
three grounds (capability / creator system / viral evidence) + build plan +
QC gates + the BRAND-DNA checklist + the HUMAN-MADE CHECK. Do not render
until I approve the pick.
```

## Worked example
A 40s talking-head take, claim "Five emails made $92,000", proof = the
5-email wall at 0:01, audience creators under 10K, lane proof-led, keyword
WAITLIST (flow live), face on screen in the hook → router picks Sky Form 2
teaching with Form 7 proof-led body, designed captions, Adilet audio chain.

## Variants (v9)
- **v9 · @ashokreddyai, DXZedtjkwOf:** 9. @ashokreddyai, DXZedtjkwOf — "The feedback loop feels exactly like briefing a human editor. The better your instructions, the better it rates" (briefing doctrine) → variant on prompts/ prompts-router-intake.md. Differs: the instructions ARE the edit — better instructions, better edit. _(source: v9_variants_bulk_a.md)_
- **v9 · @bradfordmarais, DehJEQMAJay:** 10. @bradfordmarais, DehJEQMAJay — Grill Me: interviews you one question at a time, gives its recommended answer per question → variant on prompts/prompts-router-intake.md. Differs: the interview runs the other way (Claude asks, you answer) with a recommended answer each time. Skill file gated (GAP). _(source: v9_variants_bulk_a.md)_
- **v9 · @cindiezhu, DawfiTZJYs6:** 11. @cindiezhu, DawfiTZJYs6 — "Ask Claude to create the thing you want. Not just tell you about it" (create-not-tell doctrine) → variant on prompts/prompts-router-intake.md. Differs: the ask is to create (build me a budget tracker, turn this PDF into a slide deck), not to tell. The "hundred more things" list is gated (GAP). _(source: v9_variants_bulk_a.md)_
- **v9 · @davis.mcm, DfXPsXRRK48:** 13. @davis.mcm, DfXPsXRRK48 — "I have ADHD" skill response format: first line = next action (not a compliment, not a recap); numbered action steps; shortest path; time specified ("15 minutes", not "some time") → variant on prompts/prompts-router-intake.md. Differs: the format is Q's brief format for Claude. Skill/repo + 10 rules gated (GAP); off-topic as a whole. _(source: v9_variants_bulk_a.md)_
- **v9 · @hasantoxr, DXKfsfYk6Tb:** 14. @hasantoxr, DXKfsfYk6Tb — Open Montage research-first doctrine: "Before writing a single word of script, it runs live web searches across YouTube, Reddit, and news sites so your video is grounded in real current information" → variant on prompts/ prompts-router-intake.md. Differs: research runs before scripting, not after. Link gated; "11 pipelines / 49 tools / 400+ skills" unverified (GAP for the product). _(source: v9_variants_bulk_a.md)_
- **v9 · @david_knowsai, DfDe25xqLGM:** 15. @david_knowsai, DfDe25xqLGM — Open Montage (same research-first doctrine, second source; repo calestrio/OpenMontage, 22.7k stars) → variant on prompts/prompts-router-intake.md. Repo PARKED pending license check + SCAN (GAP). _(source: v9_variants_bulk_a.md)_
- **v9 · @?, V8-01:** V8-01 — Voice-only handoff: record raw, paste the file path, say OK → prompts-router-intake.md _(source: v9_verification.md)_
- **v9 · @?, V8-06:** V8-06 — One warm conversation per editing lane; /clear when context runs high → prompts-router-intake.md _(source: v9_verification.md)_
- **v9 · @?, V8-14:** V8-14 — Voice input over typing for Claude direction → prompts-router-intake.md _(source: v9_verification.md)_
- **v9 · @?, V8-70:** V8-70 — Materials / instructions / output: dump assets, Claude analyzes and places them → prompts-router-intake.md _(source: v9_verification.md)_
- **v9 · @?, V8-85:** V8-85 — The toggle checklist is a complete edit spec → prompts-router-intake.md _(source: v9_verification.md)_
- **v9 · @mrcreates.ai, DfKFK7RJdjl:** @mrcreates.ai DfKFK7RJdjl — three prompts: setup + style + edit. DIFFERS: the workflow has THREE prompts, counted. (Prompts GATED; "inspired by them, not a copy" already filed.) _(source: bulk-c VARIANTS.md)_
- **v9 · @phanik.ig, DfRq2VZtNjY:** @phanik.ig DfRq2VZtNjY — two-prompt structure: FIRST prompt installs five tools; FINAL prompt edits the footage. DIFFERS: the install/edit split. (Ebook + matis.ai community: not joined, GAP.) _(source: bulk-c VARIANTS.md)_
- **v9 · @paytkaleiwahea, Dee5ObigMNa:** @paytkaleiwahea Dee5ObigMNa — "you are my short form editor" + GitHub links as the role prompt. (See skill-doctrine above.) _(source: bulk-c VARIANTS.md)_
- **v9 · @vidiq, DY3Gdh-v64n:** @vidiq DY3Gdh-v64n — research prompts as questions about real data: "what's trending in my niche right now" / "why did people click away from my last video"; without-vs-with split (Claude without YouTube data vs with). DIFFERS: the question-form brief. (Connector: named only, not adopted; link not chased.) _(source: bulk-c VARIANTS.md)_
- **v9 · @omgluka, DXshDVGoohf:** @omgluka DXshDVGoohf — "good prompts follow templates" (c08_template.mp4); /remotion + /whisperx pair; transcription-first prompt. DIFFERS: the template rule + the transcription-first brief. (Permission bypass shift+tab: NOT adopted — Q's lane uses approval cards.) _(source: bulk-c VARIANTS.md)_
- **v9 · @omgluka, DWm2YNfDFSF:** @omgluka DWm2YNfDFSF — VideoDB Skills' See / Understand / Act as the agent contract (SEES screen/mic/URLs/YouTube; UNDERSTANDS visual + transcribe; ACTS edit timelines/subtitles/overlays/export). DIFFERS: the three-verb brief for Claude. _(source: bulk-c VARIANTS.md)_
- **v9 · @siddhantt.ai, Detm0uhkwZS:** @siddhantt.ai Detm0uhkwZS — "Connect Claude to YouTube" + one-sentence ask: "scan the last 10 days, rank by views ÷ channel average." DIFFERS: the one-sentence ask with the ranking formula in it. (Free API key: Q's key, entered only by Q — noted, not pasted anywhere.) _(source: bulk-c VARIANTS.md)_
- **v9 · @samdespomarketing, DeurFmpSPVd:** @samdespomarketing DeurFmpSPVd — "pick Opus 5.5" model pick line. DIFFERS: the model is named in the brief, not left to default. _(source: bulk-c VARIANTS.md)_
- **v9 · @imjonathanacuna, Da1wLVUywpB:** **V85 — @imjonathanacuna plan-first (Da1wLVUywpB):** secret prompt — describe the idea → Claude writes a plan to build 80% before a line of code (→ prompts-router-intake); ship chain GitHub → Railway → Stripe (→ pipeline-drop-one-file-install). Dangerous mode: GAP/FLAGGED, not adopted. Cheat sheet: GAP (gated). _(source: bulk-b VARIANTS.md)_
- **v9 · @marc_illy, DawXsvRh0sr:** **V87 — @marc_illy prompt-is-everything (DawXsvRh0sr):** the style is in the prompt ("action packed cinematic" / "documentary style") (→ prompts-router-intake); 5–6s clips, characters intact (→ motion-beat-rhythm); "Save this entire process as its own agent" (→ skill-doctrine-save-it-as-a-skill). Clone voice: GAP/FLAGGED. Auto-scheduling: GAP/FLAGGED. _(source: bulk-b VARIANTS.md)_
- **v9 · @mavgpt, DadubcAhZmd:** **V88 — @mavgpt AI stack 2026 (DadubcAhZmd):** WhisperFlow as voice-to-prompt briefing ("I use it to pretty much write every single one of my prompts now") (→ prompts-router-intake); rating grid Top Tier / Helpful / Decent / Waste of Time (→ kallaway-format-finder); "Waste of time" row as credibility device. Higgsfield endorsement: FLAGGED (needs Q's word — v8 #3). _(source: bulk-b VARIANTS.md)_
- **v9 · @mavgpt, Duolingo:** **V89 — @mavgpt Duolingo tutor (DfZ3y3lqE8Q):** Projects + master prompt — one Project per lane, custom instructions carrying the setup (→ prompts-router-intake); scheduled daily task as cadence device (→ jayant-sunday-learn-loop); roleplay + upload-correction feedback model. _(source: bulk-b VARIANTS.md)_
- **v9 · @kelvin.martin1, DeqFCTpO7bu:** **V90 — @kelvin.martin1 brand-into-SOP (DeqFCTpO7bu):** "I just need to tell them what fonts my company brand used. I installed it into the SOP" (→ prompts-router-intake); human-control framing — "You still have control, you still have the human connection" (→ skill-doctrine-save-it-as-a-skill). GitHub link: GAP (gated). _(source: bulk-b VARIANTS.md)_

## Variants (v10)
- **v10 · Q standing rule, Nov 8, 2026:** **Asset question added to the intake (Q12 in EDIT-ROUTER.md, Q11 here):** "Which assets does this edit need — and if one is missing, ask Muse for it?" Two halves: (1) Q + Kiya's own asset pool is always available — use it first; (2) missing asset → ask Muse, do not substitute generic/AI/stock, do not invent a placeholder, do not skip it silently. _(source: Q's words, Nov 8 ~19:26 CT)_

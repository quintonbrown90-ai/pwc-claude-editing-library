# CREATOR-SYSTEMS — Nick Saraev top-5 Claude Code plugins (frame-verified + Q-stack verdicts)

Source: Nick Saraev (@nick_saraev) — reel DfPuiYyP4Hy "5 Plugins Your Claude Code Needs" (48.62s, posted 2026-11-02). The reel's links are comment-gated ("comment CLAUDE") — NOT chased. All five plugins were identified from the reel's OWN frames (repo URLs on screen) and verified on GitHub Nov 11, 2026. Full decode + verification: `research/video-harvest/instagram/batch-28/DECODE.md`. **Nothing in this part is installed** — verdicts below; installs are separate, Q-approved, quarantine-first steps.

## The pattern (why this reel matters beyond its picks)

A Claude setup is assembled in layers — model access, capability skills, output discipline, research reach, security gate — one free public project per layer. That is the same architecture as this library (skills + SAFETY.md quarantine/scan pipeline). The reel's durable lesson: **the security gate is what makes adopting community skills safe at scale**, and it is the layer most setups skip.

## The five (reel order; identities + licenses VERIFIED)

### 1. FreeLLMAPI — model-access layer
- **Repo:** github.com/tashfeenahmed/freellmapi — MIT, 50,384★ at check.
- **What it is:** an OpenAI-compatible router aggregating free tiers: "7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. One OpenAI-compatible endpoint." Smart routing + automatic failover when a provider rate-limits; keys stored encrypted; per-key usage tracking. Repo description adds "Personal experimentation only."
- **Reel claim:** "over 7 billion free AI tokens from 600 AI models… automatically switches you to the next best model any time your usage limit runs out" (voiceover rounds the repo's 635 → 600).
- **Verdict: DO-NOT-ADOPT for Q's Claude setup.** It works by silently swapping which model does the work — the direct opposite of Q's model rules (newest/highest Opus for general work; Fable 5.2 for motion/editing). A failover to a free-tier model mid-project would downgrade output without any visible sign. It also concentrates dozens of third-party provider keys in one tool. Market signal only.

### 2. Lemo Opuscar — capability layer (ANIMATION)
- **Repo:** github.com/lemomo-ai/lemo-opuscar — MIT, 14,587★ at check. Site: lemomo-ai.github.io/lemo-opuscar.
- **What it is:** "A toolbox of film styles made in code for Claude Code: 66 ready to use, and your own. Each style is a style prompt plus a demo film made entirely in code by Claude Opus 5.5, with no video model." Site stats: 66 nominees · 11 categories · 63 minutes of film; categories include Edit & Documentary, Evidence Films, Graphic & Type, Information & Keynote, Cinema & Eras, Materials & 3D.
- **Reel claim:** "teaches your Claude Code to animate in over 60 different styles… animated explainer videos that are going viral."
- **Verdict: CANDIDATE for the motion layer — quarantine-first.** Code-made film styles (no video model) are the same philosophy as pwc-fable-motion (part #321): sharp, editable, prompt-driven motion. Before any install: quarantine clone, full read, scan — the Batch 27 protocol. Cross-filed as GAP G-B28F-6 in part #321. Not installed.

### 3. Ponytail — output-discipline layer
- **Repo:** github.com/DietrichGebert/ponytail — MIT, 188,564★ at check.
- **What it is:** "Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote." Its site claims: −53% code · −41% time · −26% cost · −45% tokens, "and yet 98% of risky logic ships with a test (without Ponytail: 68%)" — the project's OWN published numbers, never independently benchmarked (GAP G-B28-4).
- **Reel claim:** "optimizes Claude Code's output, cutting down your usage by over 50% without losing any accuracy at all."
- **Verdict: PARKED.** Its pitch is doing less. Q's build standard is premium/maximal with full QC gates; a blanket minimal-output discipline fights that standard. Revisit only if Q asks for a token-economy pass on a specific project.

### 4. Agent Reach — research-reach layer
- **Repo (top match, high confidence):** github.com/Panniantong/Agent-Reach — MIT, 110,969★ at check. (A same-named 191★ repo exists; the reel shows no URL for this one — identification rests on name + CLI form + platform table + star rank, GAP G-B28-3.)
- **What it is:** one CLI to read/search the web — "Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees." README platform table also lists LinkedIn (job search/details; in-site search needs login) and Instagram (experimental; user/profile/post search; login required). Reel demo: `agent-reach linkedin search "AI engineer"` → 48 jobs; `agent-reach instagram search "ai agents"` → 21 posts (stylized UI demo, not measurements).
- **Reel claim:** "scrape anything off the internet, even on gated platforms like LinkedIn, Instagram, X, and Reddit, without having to pay for anything."
- **Verdict: DO-NOT-ADOPT as pitched, for Q's accounts.** Scraping gated platforms behind a login is a platform-ToS + account-risk problem — Q already stopped trial-reel liker DMs over ban risk (Nov 10, 2026). Nothing here installs or runs it. Any future read-only research use is Q's explicit call, and never through his own accounts' sessions.

### 5. NVIDIA SkillSpector — security-gate layer
- **Repo:** github.com/NVIDIA/SkillSpector — Apache-2.0, 25,255★ at check.
- **What it is:** "Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, security risks, prompt injection, data exfiltration, and supply-chain risks in Claude Code, Codex, and MCP skills before you install them." CLI shown in the reel: `skillspector scan ./suspicious-skill/` — 71 patterns; the demo catches a skill script harvesting `os.environ` and POSTing it out.
- **Reel claim:** "a free AI scanner that acts like an antivirus for your Claude skills and catches hidden malware before you install it." Accurate to the repo.
- **Verdict: ADOPT candidate — Q's word required to install.** It formalizes exactly the manual scan this library's SAFETY.md pipeline did by hand for /watch (Batch 27). Recommended path when Q says go: quarantine-read SkillSpector itself first (scanner gets scanned), then wire it as the scanner step for every future intake.

## Triggers

- "nick's plugins" / "the top 5 plugins" / "the Saraev plugins"
- "/nick-saraev-top5-plugins"
- Any "should we install X" question about one of the five — answer from the verdicts above; never install from this part alone.

## Rules this part carries

- **License gate held:** all five are permissively licensed (MIT ×4, Apache-2.0 ×1) — none parked on license grounds. The two DO-NOT-ADOPT verdicts are Q-rule conflicts (model integrity; account safety), not license failures.
- **Quarantine-first stands:** a permissive license is not a safety scan. Any future adoption of #2 or #5 goes through SAFETY.md (quarantine → read → scan → Q's word → install), in that order.
- **No gated-link chasing:** the reel's comment funnel was never engaged, and no part of this library depends on it.

## GAPs

- **G-B28-1:** plugin links comment-gated in the reel — NOT chased; identities are frame + GitHub verified instead.
- **G-B28-2:** no install commands are shown in the reel; installs live in each repo's docs, to be read in quarantine at adopt time — not reconstructed here.
- **G-B28-3:** Agent Reach repo identification is by name/CLI/platform-table/star-rank, not an on-screen URL.
- **G-B28-4:** Ponytail's efficiency/test figures are self-published, unverified.
- **G-B28-5:** the reel calls all five "plugins"; in repo terms they are an API router, a style-skill toolbox, an agent-behavior plugin, a CLI, and a scanner. This part records each project's actual form.

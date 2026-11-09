<!-- DRAFT — v9 bulk-b (group B) — coordinator merges into parts/creator-systems/ -->
<!-- Sources: @itsflxkzy "5 MCP SERVERS EVERYONE SHOULD INSTALL" carousel (DbdiDVgjVze cover + DbdiDd4jRMx 01 CONTEXT7 + DbdiD5BjfPu 02 PLAYWRIGHT MCP + DbdiDmrjd7r 04 EXA MCP + DbdiDwRjX_C 05 GITHUB MCP + DbdiEFSjavL 05 SUPABASE MCP + DbdiEPBjTkZ comment-MCP close). Silent carousel slides, on-screen text only. Note: slide 03 is NOT in the harvest; two slides are both numbered 05 — recorded as observed. -->
<!-- Existing parts checked first: parts/knowledge-playbooks/find-skills-discovery-layer.md is the discovery layer (candidates only, never an auto-installer) — this part is the 5-server CATALOG it would consult, not the installer. parts/knowledge-playbooks/claude-mods-watcher-handoff.md is the watcher/handoff for mods. No MCP-server catalog part exists. NEW part — SPEC ONLY. -->
# CREATOR-SYSTEMS — 5 MCP servers, as a catalog (never an install) (DRAFT — v9 bulk-b)

Source: @itsflxkzy "5 MCP SERVERS EVERYONE SHOULD INSTALL" carousel (7 slides in the harvest). Silent slides; server names + one-line jobs quoted from on-screen text. SPEC ONLY — the servers themselves are NOT adopted, NOT installed, NOT downloaded. The install doc (comment MCP → DM) is GATED — never chased.

## The rule
"They turn Claude from a chatbot into a FULL dev team. One command each." The catalog is the map; the install is a separate, gated decision per server. A catalog entry is not an install order.

## The 5 (his words, on-screen)
| # | Server | By | What it does (his line) |
|---|---|---|---|
| 01 | CONTEXT7 | Upstash | "Claude often writes code for tools that changed months ago. This feeds it the real, current docs before it answers. It stops making up code that doesn't work." → Q's rule: real docs before it answers. |
| 02 | PLAYWRIGHT MCP | official · Microsoft | "Gives Claude a real browser. It clicks buttons, fills out forms." → "Now it can actually use the web, not just read about it." |
| 03 | — | — | NOT in the harvest. Unknown. Do NOT invent it. |
| 04 | EXA MCP | Exa Labs | "Claude only knows what it was trained on. Exa gives it live web search made for AI. Now it pulls real, up-to-date answers instead of guessing from old memory." |
| 05 | GITHUB MCP | official · GitHub | "Claude runs your GitHub for you. It reads your issues, opens and reviews pull requests." → "Your whole project, controlled from the chat." |
| 05 | SUPABASE MCP | Supabase | "Claude connects straight to your database. Ask a question in plain English and it pulls the exact data you need. No code, no digging through spreadsheets." |

## The safety gate (binds, no exceptions)
Per SAFETY.md §1/§6/§9: every server stays in QUARANTINE until it passes review — read its code, SCAN PASS (grep for exfiltration/credential/env access), dual-model review (ChatGPT + Claude), license check — and Q's explicit word. The discovery layer (find-skills-discovery-layer) may CONSULT this catalog for candidates; it NEVER auto-installs. Browser control + form-filling (Playwright) is NOT adopted: an agent that clicks buttons and fills out forms is a credential/privacy surface Q's library does not touch without Q's explicit call. Database access (Supabase) is the same surface — catalog only.

## Executable steps (PWC)
1. Use this file as the catalog: when a job needs live docs (Context7), live search (Exa), or repo control (GitHub MCP), the catalog names the candidate.
2. Any install goes through the gate above, one server at a time, with the SCAN result recorded. No batch installs, no "paste them in your terminal and you're done" — his close ("YOU GET: All 5 install commands / 3 bonus MCP servers I use daily / A ready-to-drop config file / Which one to add first") is the GATED doc, not an instruction.
3. The 3 bonus servers are unnamed on the slide — NOT chased, NOT in the catalog.

## Discrepancies — carried as observed, NOT reconciled
- Two slides are both numbered "05" (GitHub MCP and Supabase MCP); slide 03 is missing from the harvest. The carousel as harvested has 7 slides for a "5 servers" claim. Recorded as observed.

## Gaps
- The install doc + config file: GATED (comment MCP → DM). Never chased.
- Server 03: unknown. The 3 bonus servers: unnamed. The exact install commands: not in the harvest.

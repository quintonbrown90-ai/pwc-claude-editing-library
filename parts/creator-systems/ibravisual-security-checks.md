<!-- DRAFT — v9 bulk-b (group B) — coordinator merges into parts/creator-systems/ -->
<!-- Sources: @ibravisual "VIBE-CODED AN APP?" security carousel, slides 01–09 (DfIKTicDPR6, DfIKTmwjFn8, DfIKTp9jFXB, DfIKTudjAm9, DfIKTzJDBKA, DfIKUL3jNkL, DfIKULFDDGG, DfIKUORDK_I, DfIKUTODBnF). Silent carousel slides, on-screen text only. -->
<!-- Existing parts checked first: NO security-checklist part exists. SAFETY.md §9 (dual-model review) is the library's own safety doctrine; this part is the creator-side pre-launch checklist that feeds it — a different device (launch gate vs install gate). parts/creator-systems/ibravisual-slash-command-pack.md is the same creator's command pack, not this carousel. NEW part. -->
# CREATOR-SYSTEMS — @ibravisual 6 security checks before you launch (DRAFT — v9 bulk-b)

Source: @ibravisual "VIBE-CODED AN APP?" carousel, 9/9 slides in the harvest (batch 16 slides 01–05, group-B slides 06–09). Silent carousel; all copy is on-screen text, quoted verbatim. INFERRED reconstruction of the checklist as a launch gate; the launch kit (audit prompt + fix prompts) is GATED behind comment LAUNCH — never chased.

## The rule
Six checks, in order, before anything launches. The checklist IS the launch gate — no check, no launch. "SAFE TO LAUNCH ✓" is the stamp at the end, not the hope at the start.

## The 6 checks (his words)
1. **Lock your database.** "Turn on Row Level Security for every table. No policy, no access." Device: the toggle — "ROW LEVEL SECURITY OFF → ON". Line: "RLS OFF = PUBLIC DATA."
2. **Keys stay on the server.** "Anything in your frontend, anyone can read. Call your AI and payment keys from your own server route." Line: "VIEW SOURCE SEES EVERYTHING." Real case on the slide: a YC-funded SaaS shipped its API keys in the frontend; attackers ran up usage and it shut down within a week.
3. **Lock your file storage.** "Uploads, photos, IDs: private bucket, short-lived signed links. Never a public folder." Line: "PRIVATE BY DEFAULT." Real case on the slide: TEA APP, JULY 2025 — an open storage bucket leaked 72,000 images (13,000 selfies and IDs); at least 10 lawsuits followed.
4. **Cap requests and spend.** "Rate-limit every endpoint and set a hard spend cap on every AI key, before a bot finds you." Device: the "HARD CAP" meter. Line: "NO CAP = NO CEILING." / "Every request costs you money."
5. **Post the boring pages.** "Collecting emails or payments? Put up a privacy policy and terms, and run an accessibility check." Cards: Privacy policy / Terms of service / Accessibility pass. Line: "NOT LEGAL ADVICE. JUST DON'T SKIP IT." Guideline on the slide: ~5,000 accessibility lawsuits hit websites and apps in 2025; roughly 2 in 3 targeted companies under $50M revenue.
6. **Make Claude attack it first.** "Before strangers try, have Claude Code audit your app like a hacker. Then have it fix what it finds." The audit prompt (visible on the slide): "audit this app like an attacker". Device: the found→fixed counter — "4 found · 0 fixed" → "4 found · 4 fixed". Line: "ONE PROMPT. RUN IT BEFORE EVERY LAUNCH."

## The stat slide (02/09) — the hook for the whole carousel
"1 in 10 apps were wide open." A researcher scanned 1,645 apps built with Lovable; 170 let anyone read or change their database. Device: a grid of 100 squares, 1 in 10 red. "SCANNED 1,645 / WIDE OPEN 170." CVE-2025-48757 · MAY 2025. [PWC skin: the red squares remap to gold — NO RED. The stat itself is his cited research, recorded as his, not re-verified.]

## Executable steps (PWC)
1. Before any launch (a skill, a page, a funnel, a tool), run the 6 checks in order and record found vs fixed per check.
2. Check 6 is the red-team prompt: "audit this app like an attacker" — then "fix what it finds" — then re-run until found = fixed. This is the pre-launch half of SAFETY.md §9: the dual-model review (ChatGPT + Claude) is the install gate; this checklist is the launch gate. Both bind; neither replaces the other.
3. The stamp "SAFE TO LAUNCH ✓" is only earned when all 6 pass. A launch without the stamp does not ship.
4. No credentials ever: check 2 is the library's own rule in creator form (SAFETY.md §3 — keys are Q's, entered only by Q in the official place, never pasted into a harvested script, form, or chat).

## PWC skin
Teal/gold on navy, NO RED — the red grid squares, red "wide open" markers, and any red accent remap to gold. The checklist is a launch gate for Q's own builds (skills, pages, funnels), not a product for sale.

## Gaps
- **The launch kit is GATED:** comment LAUNCH → DM → the 6-check pre-launch list + the Claude Code audit prompt + a fix prompt for every check. Never chased, never bought, never scraped. The audit prompt above is only the one line visible on slide 08/09 ("audit this app like an attacker"); the full prompt and the fix prompts are NOT in the harvest.
- **The cited stats are his, not re-verified:** 1,645 scanned / 170 open, the TEA app leak, the 5,000 lawsuits — recorded as his claims with his citations (CVE-2025-48757), never repeated as Q's numbers.

# CONTINUOUS LEARNING — how this library keeps getting better

Q's order (Nov 8, 2026): this is not a one-time dump. The editing system
keeps improving on a loop — new creators, new free kits, new devices, new
evidence — folded in on a schedule, with the same vetting every time.

**This loop is a PERMANENT FEATURE, not a one-time build.** The north star
is Claude with infinite space, infinite knowledge, and the ability to
learn. The loop IS the ability to learn: the weekly sweep + per-video
harvest + Q's own uploads via INBOX keep the knowledge base growing without
a ceiling, because the library is organized in small modular parts
(`parts/`, see CATEGORIES.md) across multiple delivery paths (skill zips +
GitHub pull route + this folder), not one capped skill. Every new learning
also gets APPLIED BACK to the Sky edits — see `design-system/SKY-SCORE.md`:
the benchmark is to match Sky perfectly, then beat him, and the same for
every other style mastered. The loop never ends and never gets "finished":
if a week passes with no sweep, the library is going stale, not staying
done.

## The weekly loop (runs every week, same steps)

1. **Re-sweep GitHub** — search: "claude code video editing skill",
   "video-agent", "auto-edit", "motion graphics skill", "content cuts".
   Sources: awesome-claude-video-skills, claude-for-everything, and the
   registries in `research/free-claude-editing-kits/INDEX.md`. New repos go
   through the vetting rules below before anything is downloaded.
1a. **Re-sweep every repo site** — GitHub is the start, not the end: GitLab,
   Bitbucket, Codeberg, SourceHut, curated registries (awesome lists,
   agentskillshub/claudeers-type directories, npm/pip indexes where a
   video-editing skill ships as a package). Same vetting + SAFETY.md
   protocol per site. Recorded in `research/repo-sites/INDEX.md` with the
   search terms used per site.
2. **Re-sweep Instagram — EVERY video on the topic** (widened Nov 8):
   search IG + social.search for claude code editing, claude video editing,
   claude prompts, AI video editing, faceless reels Claude; enumerate the
   reels, download (yt-dlp), break each down TO THE T (spoken + on-screen
   text transcribed, Claude execution steps frame-logged, every visible
   prompt/code/command extracted verbatim, system duplicated as a skill
   entry). Same treatment for YouTube, YouTube Shorts, and anywhere else the
   sweep finds them — the harvest is "every video on the topic, every
   platform", growing weekly. File per-video breakdowns under
   `research/claude-editing-creators/<handle>/` or
   `research/video-harvest/<platform>/<id>/` with SOURCES.md.
2a. **Re-sweep prompts across ALL social media** — X/Twitter threads,
   Threads, TikTok captions/comments, Reddit (r/ClaudeAI, r/VideoEditing,
   r/ClaudeCode), LinkedIn posts, public Facebook groups/posts, public
   Discord/Telegram channels only where openly accessible (never join
   private groups, never scrape behind logins). For each prompt: verbatim
   text, who posted it, platform + URL, what it claims, and the measured
   result where a video/result accompanies it. Stored under
   `research/prompts/<platform>/<creator-or-topic>/` with SOURCES.md;
   ranked in `research/prompts/INDEX.md` by verified results first.
   Prompts with no visible result are flagged [UNVERIFIED]. Best prompts
   fold into the design system's PROMPTS.md + the router's prompt library.
3. **Re-sweep YouTube + free guides** — the Phase 4 knowledge harvest
   sources + search terms (Claude Code video editing, motion graphics,
   Remotion/HyperFrames/GSAP, ffmpeg automation, caption/motion systems,
   "Claude builds my video"); distill new videos/guides into the
   `research/knowledge/` playbooks under the executable bar. First harvest
   (Nov 8): 23 videos attempted, 18 with files (~130k words), ~40 guides,
   10 playbooks, 89 entries, 83 executable = 93.3% — see
   `research/knowledge/INDEX.md` for the source list, the parked items,
   and the retry notes (5 empty 429 folders; GSAP/Remotion docs cited from
   excerpts — read in full next sweep; never cite harvested view counts,
   they are unreliable from the yt-dlp android client).
4. **Re-check Sky-like creators** — new reels from the ranked list in
   `research/sky-like-creators/INDEX.md`; new devices logged with reel URLs.
5. **Refresh WHAT'S WORKING NOW** — `design-system/EDIT-ROUTER.md` §7: drop
   rows past their refresh date, add rows with fresh measured evidence
   (engagement + device), re-date everything. The router never treats a stale
   row as current.
5a. **Refresh trends, pain points, audience psychology (strategy sweep,
    Nov 8)** — re-sweep the creators in the catalogs for newest posts +
    engagement (Trend Analyst: every post >2× median, comments > likes
    flags a funnel post; re-rank `research/knowledge/TRENDS.md`); re-sweep
    r/UGCcreators, r/VideoEditing, IG captions, complaint threads for new
    pain wording (Pain-Points Specialist: log verbatim + URL + date;
    re-rank `research/knowledge/CREATOR-PAIN-POINTS.md`); re-check the
    audience-psychology notes (new rituals, inside words, progression
    signals from creators with cult-like followings). Hand the top 3
    topics to Content Strategy and the top 3 devices to Motion/Caption.
5b. **Gap-fill pass (WHAT-Q-DIDN'T-SAY.md)** — ask what important
    knowledge is still missing that Q didn't ask for. A new gap gets a
    part (executable standard, source cited, marked [GAP-FILL]), a row
    in WHAT-Q-DIDN'T-SAY.md, and a coverage-map entry. Q can strike any
    gap-fill; struck gaps move to `archives/` and leave the next skill
    version.
5c. **Double-growth metrics (Q, Nov 8)** — the weekly report measures
    the loop, not just the library: parts added, skills updated, renders
    QC-passed by Muse, corrections folded back as rules, Claude
    applications logged as worked examples. The goal is double the growth
    rate — if the numbers are flat week over week, the loop is stalling
    and the sweep widens (new sources, new platforms, new search terms).
5d. **Algorithm + niche-intelligence scan (Q, Nov 8, 2026 — the
    mastermind layer).** Claude must search, mastermind, and learn
    social-media algorithms (Instagram first), constantly scan for
    what's new, go through all Instagram videos in Q's niche and ideal
    avatars' world, learn every pain point and solution people need,
    plus structures, what's working, what's going viral, and what
    people like to see — and develop a mastermind way of thinking and
    creating. HONEST CADENCE (no live 24/7 monitor exists): the scan
    runs on (a) the weekly sweep, Sundays ~10:17 AM CT; (b) every batch
    Q sends; (c) each coordinator run. Each pass: re-check Meta's
    Transparency Center Reels system card, Instagram @creators, and
    Mosseri's posts for algorithm changes; re-check tracked creators'
    recent posts + engagement for new formats/hooks/algorithm shifts;
    re-sweep r/UGCcreators, r/VideoEditing, IG captions and complaint
    threads for new pain wording; log every post at >2× the creator's
    median engagement (comments > likes flags a funnel post). Verified
    findings fold into `parts-staging/algorithm-niche/` drafts first
    (algorithm-mastery-instagram.md, pain-point-solution-bank.md,
    viral-structure-library.md, top-creator-index-niche.md,
    mastermind-thinking.md), then into parts/ by the coordinator —
    never straight into a live skill. A scan that finds nothing new
    still logs its date and what was checked; silence is a result, not
    a skipped week. Gated/DM-funnel content is NEVER chased, bought,
    or scraped — noted only, with the reason.
6. **Vet + quarantine + scan (SAFETY.md)** — every new download lands in
   `uploads/QUARANTINE/` first; verify the source (account age, followers,
   stars, README, license, two-source cross-check); scan all code with the
   SAFETY.md grep set and record `SCAN: pass | flag` in SOURCES.md; park
   anything flagged with the reason — never fold in. Exclude on sight:
   fake giveaways, credential-harvesting pages, "download to unlock" flows,
   obfuscated code, exfiltration, miners, paywalled/pirated material. Never
   run untrusted scripts; never enter credentials/keys in the harvest.
7. **Fold in vs park** — see below. Folded items get an appendix entry in
   `design-system/COMPONENTS.md` with attribution + MEASURED/INFERRED/
   PUBLISHED labels, and (when they change a skill) a new skill version.
8. **Upload + verify** — affected Claude skills are re-zipped (respecting
   ≤200 files / ≤30MB / no nested .zip), uploaded, and verified ON in Q's
   Skills list before anyone calls it done. Muse's custom-skills pointers
   are updated in the same pass.
9. **Report to Q** — one short note: what was added, where it lives, what
   changed in Claude, and the new top-3 devices worth trying — plus what
   was parked as suspicious and why. Include the double-growth metrics
   (step 5c): parts added, skills updated, renders QC-passed, corrections
   folded back.

## The double-growth loop (Muse beside Claude — Q, Nov 8)

Muse works BESIDE Claude, in parallel, so the system grows twice as fast
(see README.md). The loop: find → distill → stage → upload → Claude
applies → Muse verifies → correction becomes a rule → find more. Muse
harvests while Claude builds; Muse verifies every Claude render before
it reaches Q (freeze, face clearance, lip-sync, brand-DNA, human-made);
Muse teaches (each staged part is a lesson), Claude practices (applies it
on the next real video), and the result is logged back as a worked
example. Two memories, one brain — the weekly sweep is the sync point.
**Per-video cycle (final scope lock):** learn → adopt → duplicate →
replicate → improve.

## The self-learning half of the double-growth loop (Stream 7 — Nov 8, 2026)

The other half of the loop is the external harvest (the weekly sweep above:
new creators, kits, prompts, trends). This half is Claude growing from its
OWN work — Q's feedback and the outcomes of videos already built, posted,
and judged. Same loop, different fuel:

**Claude builds → Muse verifies + Q reacts → lessons logged → lessons folded
into skills → Claude builds better next time.**

- **Lessons file:** `research/knowledge/SELF-LEARNING.md` — each lesson is
  tried → result → do-differently, with evidence cited (Q's quoted words,
  a posted media ID + date, or a QC report on an exported file) and a
  "proposed part update" naming the part file + what changes. Successes are
  verified playbook entries with the same evidence bar.
- **Log:** `research/knowledge/SELF-LEARNING-LOG.md` — one line per lesson:
  date, video, lesson, part it updates, status
  (LOGGED / READY-TO-FOLD / FOLDED / FLAGGED).
- **Fold rule:** a lesson is only "learned" once written into a part Claude
  loads. The self-learning stream never edits `parts/` itself — it proposes;
  the coordinator folds. Check the log on each sweep and flip
  LOGGED/READY-TO-FOLD to FOLDED once the coordinator confirms.
- **Flag rule:** any lesson conflicting with a standing rule (face clearance,
  palette, PWC skin, brand DNA, blur law, hidden app never named) is
  FLAGGED, never applied — listed separately in SELF-LEARNING.md §4 with the
  conflict, until Q / the coordinator resolves it.
- **First haul (Nov 8, 2026):** 34 lessons + 7 verified playbook entries +
  4 flagged conflicts, mined from `~/memory/2026-11-02.md` through
  `2026-11-08.md`, `~/MEMORY.md`, `~/workspace/your_files/viashaan-demos/QC-REPORT.md`,
  and the BW-04 / hat-talk / P1–P3 records. Headline lessons: the "cheap AI
  slop" verdict (same 12 components, zero of 33 memes used); moving lines,
  not static overlays; the door device dead in every form; designed captions
  rejected for overlap; the P1 real-creator wall; the P3 freeze + invented
  chips stripped; the newest-version posting rule; the hat-talk two-cam fix
  (constant offsets, ooowee intact); the BW-04 freeze/transition/dead-air
  gates. Flagged: P3 payout-dates-as-is vs the blur law; the wrong-chat
  "nothing blurred" line vs the blur law; "copy Sky to a T" vs never
  verbatim-copy a creator; David's red keyword colours vs NO RED.

## Vetting rules (every candidate, every week — no exceptions)

- **License:** free + open (MIT/Apache-2.0/BSD or clearly public). Record the
  exact license in SOURCES.md. Exclude paywalled, key-gated, or
  license-unclear items. Non-commercial licenses (e.g. CC BY-NC) are flagged
  LOUD and never folded into a shipped skill without Q's explicit say-so.
- **Relevance:** actually about video editing / motion / cuts / captions /
  audio for short-form video. Not generic coding.
- **Real on disk:** real code/prompts, not a README promise. Verify the repo
  is live (README + LICENSE + recent push) before downloading.
- **Honesty labels:** MEASURED (we verified it from their videos/code),
  INFERRED (we rebuilt it from outputs), PUBLISHED (their own prompt/code,
  quoted with source). Never present an inference as their words.
- **Brand fit:** devices are re-skinned to PWC law on fold-in (teal/gold on
  navy, NO RED, nothing over the face). A device that cannot survive the
  re-skin is parked, not folded.
- **Safety (SAFETY.md):** every download lands in `uploads/QUARANTINE/`
  first; source verified (account age, followers, stars, README, license,
  two-source cross-check); code scanned with the SAFETY.md grep set and
  `SCAN: pass | flag` recorded in SOURCES.md. Flagged = parked with the
  reason, never folded in. Never run untrusted scripts; never enter
  credentials/keys in the harvest.

## Fold in vs park

- **Fold in:** a device/prompt/workflow that (a) passes vetting, (b) fits a
  router row or adds a new one, and (c) survives the PWC re-skin. It gets a
  COMPONENTS.md appendix entry + the relevant skill updated.
- **Park:** interesting but unvetted, unlicensed, off-brand, or duplicative.
  Parked items live in their research folder's INDEX.md with the reason
  recorded — never silently dropped, never silently folded.
- **Stage as its own skill:** a complete skill that fits Claude's limits on
  its own gets staged as an upload-ready zip in `zips/` with a manifest note
  (see `zips/UPLOAD-MANIFEST.md` once research lands).

## What reaches Claude (the promotion path)

INBOX or sweep find → vet → file into `research/` → fold into
`design-system/COMPONENTS.md` appendix → update the affected skill source in
`skills/` or `editors/` → rebuild + verify zip (`code/skill_zips_build.py`)
→ upload to Claude → verify ON in the Skills list → report to Q.

Nothing reaches Claude without a verified zip and a Skills-list check.

## Inbox flow (Q's uploads)

Q drops examples/code in `uploads/INBOX/` (see `uploads/UPLOAD-RULES.md`).
Each drop is triaged in the next weekly run (or immediately if Q asks):
vet → file → fold/park → upload → report. A drop is never left un-triaged
past one weekly cycle.

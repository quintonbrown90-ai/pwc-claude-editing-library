<!-- PART: gap-fills/gap-delivery-specs.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# GAP-FILL — Delivery specs per platform [Q didn't ask, mastermind added]

Source: Q's standing rules (1080x1920, safe zones, caption caps) +
platform help docs (general knowledge — verify against the live platform
before shipping a new format). Mark: GAP-FILL.

## The rule
Claude never ships a file the platform mangles. Specs are checked BEFORE
the render, not after the upload fails.

## Instagram Reels (Q's home lane)
- 1080x1920, 9:16, H.264, yuv420p limited range, 30fps, faststart (moov
  at front — a moov-at-end file 500s at staging, Oct 12–13 lesson).
- Safe zones: text x 70–930, y 280–1480; nothing in the top 280px, bottom
  440px caption zone, or right action rail. Covers: faces + text + handle
  inside the center 1080x1350 grid crop.
- Caption ≤500 chars (Q's cap), keyword CTA + dual-CTA profile line, no
  "link in bio" wording. Likes/views hidden per post (no account default).
- Loudness: master to ~-14 LUFS (Adilet measured -14.19/-14.16).

## TikTok (@yerrr__q POSTING STOPPED Nov 4 — do not post until Q lifts
the hold; specs kept so the lane is ready)
- 1080x1920, 9:16, same safe zones; captions burned in must clear the
  right rail and bottom bar. Couples TikTok @qandkiya is a separate
  account with its own rules.

## YouTube Shorts
- 1080x1920, 9:16, ≤60s for Shorts shelf; title ≤100 chars; description
  carries the keyword + link. Same loudness target.

## LinkedIn (mirror lane — 162/162 posted Nov 6)
- Vertical video plays cropped in feed; keep the hook inside the center
  crop. Captions burned in (LinkedIn mutes by default).

## Executable steps
1. Pick the platform FIRST — it sets the render, not the other way round.
2. Render the master once (1080x1920, -14 LUFS), then derive per-platform
   trims from the master — never re-edit per platform.
3. Check the safe-zone + loudness gates on the export before delivery.

## Worked example
P3 posted Nov 8 12:30 AM CT: 1080x1920, faststart, -14 LUFS, caption
482 chars with WAITLIST CTA, designed cover in the 1080x1350 crop.
## Self-learning — folded Nov 8, 2026 (research/knowledge/SELF-LEARNING.md)

- **SL-14** — ALWAYS post the NEWEST version (old boosted file clipped +0.56 dBTP; newest −14.07 LUFS / −0.95 dBTP). (2026-11-08, Backyard #1 repost)
- **SL-19** — Scratched means scratched — never reuse a scratched batch's build; prove blur survives. (2026-11-02, BW-04)
- **SL-21** — Thumbnail cache: deliver updated covers under a FRESH filename. (2026-11-07, P1 thumbnail)
- **SL-29** — IG staging 500 escalation: faststart remux → full re-encode → park; post 1080×1920 only. (2026-11-07, E09)
- **SL-30** — Hold the slot, never post the unpatched version; verify render completeness (duration vs script) on pull. (2026-11-07, P1 6 PM slot)
- **SL-33** — Attachments strip filenames — always send a text mapping (filename → expression → timestamp). (2026-11-07, Kiya heads)
- **SL-34** — Order gates work (P1-first held P2); verify live on profile list before firing; wide listing limit for absence checks. (2026-11-07, P1 v9 / P2 / P3)
- **SL-37** — Duplicate takes: transcript-compare on re-delivery — v2 supersedes v1 (AMAZON, REAL JOB); a re-delivered take identical to a posted one is NEVER posted again (batch-5 backyard #1 = posted take; replace only by delete+repost on Q's call). (2026-11-08, body-scan audit)
- **PB-06** — Newest-version repost: Nov 7 15:00 stack copy, designed cover, verbatim caption — reel DfeM5aJk7V_. (2026-11-08, Backyard #1)


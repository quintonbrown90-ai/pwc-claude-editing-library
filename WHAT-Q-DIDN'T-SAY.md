# WHAT Q DIDN'T SAY — gap-fills the mastermind added on his behalf

**Rule (Q, Nov 8):** "It should know everything I've said AND more that I
didn't even say that I should have touched on that's important." The
library must cover the important things Q didn't explicitly ask for — the
knowledge a true mastermind would know to include.

**Nothing here changes his stated rules; it only completes them.** Each
gap is marked `[GAP-FILL — Q didn't ask, mastermind added]` in its part
and its source is cited. This file lists every gap filled so Q can see
what was added on his behalf — and strike anything he doesn't want.
Struck gaps get removed from the parts, the coverage map, and the next
skill version. Nothing is silently kept.

## The 11 gaps (all built as parts in `parts/gap-fills/`, Nov 8, 2026)

| # | Gap | Part | Source | Why it matters |
|---|---|---|---|---|
| 1 | Delivery specs per platform | `gap-delivery-specs.md` | Q's standing rules + platform help docs (verify live before a new format ships) | Claude never ships a file the platform mangles (moov-at-end 500s, 4K rejection — both already cost a day each) |
| 2 | Render/export + versioning discipline | `gap-render-versioning.md` | Q's "always post the NEWEST version" rule (Nov 8) + AGENTS.md lessons | The Nov 8 1 AM post used the OLD file because versioning was a habit, not a system |
| 3 | Copyright + licensing safety | `gap-copyright-licensing.md` | Q's standing rules (licensed library, Epidemic declined, no artist tracks, meme order) | Nothing gets claimed or taken down; the CC-BY credit rule was never written down |
| 4 | Audio craft beyond the bed | `gap-audio-craft.md` | Adilet AUDIO.md (measured −14.2 LUFS) + sound-design playbook | The voice must survive a phone speaker; loudness was a number, not a chain |
| 5 | Color management | `gap-color-management.md` | Color-grade playbook + BRAND.md | The grade must survive IG compression and stay consistent across a series |
| 6 | Accessibility | `gap-accessibility.md` | WCAG 2.1 contrast guidance + Q's caption standards | A large share of IG watches muted; a deaf viewer must get the whole video from captions |
| 7 | Thumbnail + hook science | `gap-thumbnail-hook-science.md` | Adilet/Ava/Sky measured patterns + locked cover template | The stop happens in 2s; the science behind the hook was scattered across five files |
| 8 | Retention analytics | `gap-retention-analytics.md` | Retention read + martinwang rescue case | Retention data is a diagnosis — every drop-off point names its fix; nobody had written the fix table |
| 9 | Funnel + ManyChat mechanics | `gap-funnel-manychat.md` | Oct 30 ManyChat sweep (47 flows verified) + ENGINE Step-0 gate | The delivery side of every CTA Claude writes — a CTA without a flow is a broken promise |
| 10 | Creator business basics | `gap-creator-business.md` | CREATOR-PAIN-POINTS.md sources (Talentir, r/UGCcreators, Velena) | The pain-point answers the Coach specialist draws on — rates, usage, pitch, contracts in plain terms |
| 11 | Failure recovery | `gap-failure-recovery.md` | AGENTS.md lessons (Oct 10–Nov 8: TTS, staging, timeouts, deadlocks) | Every failure already happened once and cost hours; the playbook means the second time costs minutes |

## How a gap gets struck

Q says "strike #N" (or names the gap) → the part is removed from
`parts/gap-fills/` and from `code/build_parts.py`, the row is marked
STRUCK here with the date, and the next skill version ships without it.
The part file moves to `archives/` (kept, not live) so the decision is
reversible.

## Gaps NOT filled (deliberately)

- Legal advice beyond plain-terms contract literacy (the business part
  says "get it in writing" — it is not a lawyer).
- Medical/mental-health content (outside Q's space; burnout is covered
  only as a creator pain point with the system as the answer).
- Anything paywalled, pirated, or license-unclear (SAFETY.md excludes it
  on sight — a gap-fill never overrides safety).

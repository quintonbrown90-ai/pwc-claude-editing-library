# LEAD CARD — template, schema, and the profile-builder instructions

One card per creator. The card is the whole asset: outreach copy, launch hooks, caption angles, and objection content are all written off these fields later — so the quotes have to be real.

## The profile-builder instructions (exact-words only — binding)

Given a creator's recent public posts (and public comments where readable):

1. **Extract, never write.** Find the strongest sentence where the creator states, in their own words:
   - **PAIN** — what hurts about getting brand deals / growing right now ("brands keep ghosting me after I send my rates").
   - **DREAM** — what they want the outcome to be ("first $1K month from UGC so I can cut my shifts").
   - **OBJECTION** — why they don't buy / don't trust the fix ("every course I bought was recycled YouTube videos").
2. **Copy the quote character-for-character** — their spelling, punctuation, emoji, and line breaks collapsed to one line. No paraphrase, no tidying, no combining two posts into one quote, no "translating" slang.
3. **Attach the source link to every quote** (the post/comment URL it came from) and the date captured. A quote without a link is treated as unsourced — delete it.
4. **An unsourceable field stays empty.** If they never stated an objection publicly, OBJECTION is `null` / "not found". Never infer one from their niche, their follower count, or what "creators like them" usually say. A quote the finder cannot source does not go on the card — no exceptions.
5. Prefer their most recent clear statement; one quote per field (a second is allowed only if it is a distinctly different pain/dream/objection, labelled as secondary).
6. **Public contact:** only if they publish it themselves for brand inquiries (bio email, link page). Copy it as published. Never infer, guess, append a domain, or pull from a data broker.

## Card template (Markdown — the working copy)

```markdown
## @HANDLE — PLATFORM
- **Followers:** N (band: nano <1K / micro 1K–10K) · **Niche:** …
- **Found:** YYYY-MM-DD · **Surface:** where they were found
- **PAIN:** "verbatim quote" — [source](URL)
- **DREAM:** "verbatim quote" — [source](URL)
- **OBJECTION:** "verbatim quote" — [source](URL)   (or: not found)
- **Public contact:** email / link page, as published (or: none published)
- **Funnel:** waitlist / calendar / both
- **Status:** new / drafted / contacted / waitlisted / calendar buyer / not a fit
- **Notes:** one line max — facts only, no invented motives
```

## Schema (portable lists — CSV header + JSON)

CSV header:
`handle,platform,followers,follower_band,niche,found_date,surface,pain_quote,pain_source,dream_quote,dream_source,objection_quote,objection_source,public_contact,funnel,status,notes`

JSON (one object per lead):
```json
{
  "handle": "@example",
  "platform": "instagram",
  "followers": 2400,
  "follower_band": "micro",
  "niche": "beauty UGC",
  "found_date": "2026-11-12",
  "surface": "comments on UGC coach post",
  "pain":      { "quote": "verbatim…", "source": "https://…" },
  "dream":     { "quote": "verbatim…", "source": "https://…" },
  "objection": { "quote": "verbatim…", "source": "https://…" },
  "public_contact": null,
  "funnel": "waitlist",
  "status": "new",
  "notes": ""
}
```
`objection` (and any field) is `null` when no sourceable quote exists — the schema carries the honesty rule with it.

## State tracking

Status moves one way: `new → drafted → contacted → waitlisted / calendar buyer`, or out to `not a fit`. A lead who is `contacted` is never re-drafted in a later batch — check the bank before building new cards so nobody gets double-touched. Fresh quotes from a known lead update their card (dated), they don't spawn a duplicate.

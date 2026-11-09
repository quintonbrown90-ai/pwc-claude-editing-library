<!-- PART: creator-systems/nategold-ig-profile-audit.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# CREATOR SYSTEMS — nategold.ai ig-profile audit, 12-item rubric (repo distill)

Source: nategoldai/instagram-agent repo (MIT, SCAN PASS) —
`skills/ig-profile/SKILL.md` + `rubric.json` in
`uploads/QUARANTINE/rundown-b-repos/nategold-instagram-agent/`. Twelve items,
100 points total. "Don't be kind. Most profiles score in the 30s or 40s the
first time, and an inflated score helps nobody." Never log into Instagram
for the user.

## The rule
Most people polish the wrong part of their profile. Nobody browses it like
a shop window. They land on it from a single reel, and it has roughly three
seconds to answer one thing: is there more of what I just watched, and is
it meant for me. The weighting is deliberate: the name field, the first bio
line and the pinned three are worth more than the photo, because they are
what a stranger who arrived from one reel actually processes before deciding
to follow.

## The rubric (12 items, 100 pts — MIT source, ported)
1. **Name field (12)** — the bold line under the photo, not the handle (30
   chars). Full marks: name + what they do in words people search ("Dana
   Ruiz | Proposal templates"). Instagram search matches against it.
   Common fail: just a name, or a name with an emoji.
2. **Bio first line (12)** — who this is for and what changes for them, in
   their words. Not a job title, not adjectives, not three emoji split by
   bars.
3. **Bio body (8)** — the rest of the 150 characters carries one piece of
   proof or one specific offer, as sentences, not a pipe-separated list.
4. **Pinned three (10)** — three posts, three different jobs: the best
   proof, the clearest explanation of the offer, the best introduction to
   the person. The biggest win on the profile; if nothing is pinned,
   visitors see whatever went up last, and that's luck.
5. **Highlights (8)** — four to six, titled after the questions a buyer
   would ask: Pricing, Results, How it works, About. Drop "Random".
6. **Grid legibility (8)** — the first nine covers at thumbnail size; four
   words of text per cover makes the grid readable at a glance. Six of nine
   covers a face mid-word = a fail.
7. **Link (6)** — one destination that delivers what the bio just promised.
   Two is already a menu; a menu converts worse than a single door.
8. **Handle clarity, photo, bio proof, CTA line, consistency of the last
   nine, search terms in the bio (remaining 36 pts across 6 items)** — each
   scored the same way: full-marks description vs the usual fail, from
   rubric.json.

## Executable steps
1. Get the inputs: name field, handle, bio, link destination, highlight
   titles, pinned posts, first nine grid covers (one screenshot of the top
   of the profile + first two grid rows is plenty).
2. Grade every item, print the table, give the total. Don't be kind.
3. Rewrite in fix-first order — start with whatever lost the most points.
   Name field first (offer three versions: "{Name} | {what you do, in words
   people search}"), then bio line 1, then the pinned three, highlights,
   link, grid covers. Don't rewrite the whole thing in one go — the user
   changes every field by hand in the app.
4. Pass every rewrite through /ig-human, re-grade at the end, report both
   scores.

## Worked example (PWC)
@yerrr__q audit: name field "Quinton | UGC + brand deals for creators under
10K" (search words in); bio line 1 "Creators under 10K → deal-ready in 90
days" (who + what changes); pinned three = P1 (proof) + the 90-day path
(offer) + Q's origin (person); highlights: Pricing / Results / How it works
/ About; link: the waitlist page (the one door). Keyword WAITLIST.

## Human-made check
The rubric grades; a human (Muse) writes the rewrites in Q's words — the
rubric never invents Q's positioning.

## PWC skin
One door (the waitlist page) as the link; pinned three = proof / offer /
person. Credit: nategold.ai (MIT).

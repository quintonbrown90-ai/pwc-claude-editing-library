# CREATOR-SYSTEMS — Claw-machine picker: "the router picks" visual (INFERRED reconstruction)

Source: @jackroberts___ — canonical reel DePtyBoAOPd "Find Skills" (parent-decoded, Batch 7), frame f_013. The device is visible on screen only; the spec below is rebuilt from the frame, labeled INFERRED.

## The device (what the frame shows)
A browser window full of colorful skill cards — domain-modeling, brainstorming, code-review, implement, agent-browser, media-use, tdd, teach, grill-me, lark-doc — and a claw machine claw descending to grab ONE card: **"frontend-design" (anthropic/skills)**. The claw = the picker. The registry is the machine; the claw is the choice; the grabbed card is the match.

## The rule
The router does not present a list. It PICKS. One card, lifted out of the machine, held up to the viewer. The pick is the content: the audience watches the claw choose, and the choice is the recommendation. A list is a search result; a claw grab is a decision.

## How it works in Q's content
1. **The machine** — the registry on screen: Q's parts library (or the harvest shelf) rendered as a grid of skill cards. Each card: skill name + one-line what it does. Cards fill the frame; the grid IS the abundance ("over a million out there" — the machine is full).
2. **The claw descends** — on the spoken beat ("it picks the best matches"), the claw drops from the top of frame, hovers, closes on ONE card. The descent is the suspense beat: the viewer does not know which card yet.
3. **The grab** — the claw lifts the card clear of the grid. The grabbed card enlarges slightly and centers. Its name is read aloud, word for word, as it is lifted.
4. **The hold** — the card is held up for one beat while the voice says what it does and why it won. Then the cut: the card becomes the video's next scene (the skill in action).
5. **The miss is allowed** — if the claw grabs the wrong card (the match fails the Quality Gate), the claw DROPS it back into the machine and picks again. The drop is the gate made visible: a bad match is not installed, it is returned.

## PWC skin (HARD)
- Teal #14A886 + gold #FEE238 on navy #00214E, **NO RED**. Jack's frame is colorful cards on white; Q's machine is navy, cards are navy with teal borders, the grabbed card is gold-bordered, the claw is gold.
- Q's logo on the machine (top-left, same lockup as the cover template).
- Nothing over the face: the claw and the machine go full-screen while Q is off-camera; when Q is on screen, the grabbed card sits BELOW his chin, centre-lower — never over his face.
- CapCut-native motion: the claw is a CapCut keyframed element (descend → hover → close → lift), not a baked-in video. The card grid is a CapCut template; cards swap per video.

## Motion spec (CapCut-native)
- Claw descend: 0.6s ease-in (power2.in), from top edge to the target card.
- Hover: 0.25s hold — the suspense beat. A micro-tick SFX on the hover (the claw "deciding").
- Close + lift: 0.5s — the card scales 1.0 → 1.15 as it lifts, with a soft pop SFX. The other cards dim 30% while the grabbed card is held.
- Drop (gate fail): 0.4s fall with a dull thunk SFX, card returns to the grid, claw re-descends. Used only when the match fails the gate — never as decoration.
- Sound: tick on hover, pop on grab, thunk on drop. The local licensed sound library is the source; no Epidemic Sound.

## When to use it
- **Router content:** any video where Q's Edit Router (or the discovery layer) picks the skill/part for a video. The claw IS the router, visualised.
- **Discovery-layer content:** the find-skills part's visual (see `find-skills-discovery-layer.md`) — the claw is the layer's face.
- **"One skill" videos:** "if you're only [getting] one skill, make it this one" — the claw grabs the one.
- NOT for: proof-led videos (the proof is the visual there), or any video where the pick is already decided before the video starts and the suspense would be fake. The claw only descends when the choice is real.

## What it is NOT
- Not a slot machine (no spinning, no chance — the pick is ranked, not random; the ranking is the discovery layer's output).
- Not a grab-bag (the machine holds the registry, not a mystery box — every card is named and readable before the claw moves).
- Not red. Ever. The claw is gold; the machine is navy; the cards are teal-bordered. Jack's colorful cards are remapped, not copied.

## GAPS
- The claw's exact motion (speed, easing, sound) is INFERRED from a single still frame (f_013) — the reel shows the claw mid-grab, not the full descend-grab-lift. The motion spec above is Q's CapCut build, not Jack's frames.
- The card names in Jack's machine (domain-modeling, brainstorming, code-review, implement, agent-browser, media-use, tdd, teach, grill-me, lark-doc) are his registry's cards, quoted as evidence. Q's machine uses Q's part names.

## Variants (v9)
- **v9 · @stockton, DfDVpYvgXSR:** @stockton DfDVpYvgXSR — three-part brain as a teaching frame: Layouts (composition) → Templates (creative) → Rules (judgment). DIFFERS: the cleanest articulation of the whole system; maps to layout picker + template library + rules layer. Layouts menu strip (six named, previewed compositions in one frame); "recycling the same garbage" as the problem line (generic AI edits look the same because nobody gave the AI actual instructions); skill names as a system list (sifting, storyboarding, motion graphics, captions, sound design). _(source: bulk-c VARIANTS.md)_

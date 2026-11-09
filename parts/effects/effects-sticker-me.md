<!-- PART: effects/effects-sticker-me.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# EFFECT — sticker-me: live sticker cut-out + name tag [INFERRED reconstruction]

Source: @kayvon.ai reel DfPtyaCqhIa ("logos orbiting you / clone yourself /
text behind you / live sticker / light painting / new background — made by
Claude") — silent Format B showcase, screen recording of a Claude Code chat.
Command typed on screen: `/sticker-me` — "Running /sticker-me..." — effect:
cut-out sticker of himself + "Kayvon" name tag — caption "live sticker /
made by Claude". The prompt behind the command is GATED behind follow +
comment EDIT → DM — never chased, never bought. Rebuild from the visible
spec only, labeled INFERRED.

## The rule
The speaker becomes a sticker: a cut-out of himself with a white outline and
a name tag below the chin, stuck on the frame like a label. The sticker IS
the speaker — it moves when he moves, it is not a pasted photo. The tag names
him; the outline makes him pop off the background.

## Executable steps (rebuild)
1. Segment the speaker (face-track + cutout) and add a clean white outline
   (~8px, even all round) — the sticker edge.
2. Name tag below the chin: rounded pill, navy field, gold border, white
   text — the speaker's name (Q) in Anton. The tag sits in the empty space
   below the chin, never over the face.
3. Entrance: sticker pops in on the typed command (spring overshoot 0.25s)
   + pop SFX. The sticker tracks the speaker's movement with a 1–2 frame
   lag so it reads as stuck to him, not floating.
4. Exit: sticker peels off (corner lift + 0.2s EASE IN) on the next command.

## Face-clearance check
Tag sits below the chin, face clear. The outline follows the head, never
crosses the face. PASS in the source video.

## Worked example (PWC)
Intro beat: Q's sticker pops in with the tag "Q — PAID WITH CONTENT" as he
says his name — the label lands on the introduction, then peels off as the
teaching starts. PWC skin: navy pill, gold border, teal "PAID WITH CONTENT"
kicker under the name.

## PWC skin
Palette teal #14A886 + gold #FEE238 on navy #00214E, no red. Outline white
(the sticker edge is the one place white stays); tag navy + gold. QC status
PENDING until the you-and-Claude loop runs after upload.

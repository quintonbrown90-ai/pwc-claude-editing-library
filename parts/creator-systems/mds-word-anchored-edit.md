<!-- DRAFT — v9 bulk-b (group B) — coordinator merges into parts/creator-systems/ -->
<!-- Source: @mds "Every edit in this video lands on a word that I picked in a text file" (DdHB2tRkQpn). Tier S — top of its batch. -->
<!-- Existing parts checked first: NO word-anchored edit part exists. parts/captions/captions-word-exact.md is word-timed captions (+0.013s measured), not word-triggered EDITS. parts/pipeline-caption.md is the caption pipeline. parts/knowledge-playbooks/gestures-movements.md is the visual-language vocabulary (OBSERVED + INFERRED). This part is the word → edit map: the script writes the edit. NEW part. -->
# CREATOR-SYSTEMS — the script writes the edit: word-anchored cuts (DRAFT — v9 bulk-b)

Source: @mds "Every edit in this video lands on a word that I picked in a text file" (DdHB2tRkQpn). Tier S. INFERRED reconstruction from the visible transcript; his pipeline code is NOT in the harvest.

## The rule
Every edit lands on a word — and the word is picked in a text file BEFORE the edit. The script is the edit decision list. "12 cuts, 9 gestures, 0 keyframes by hand. The edit wrote itself."

## The edit grammar (his words)
"A zoom is slow, a punch is fast, and a jump has no frames at all." Three verbs, three speeds — the whole edit is a grammar, not a timeline:
- **zoom** = slow (a slow push-in on the word)
- **punch** = fast (a fast punch-in on the word)
- **jump** = no frames at all (a hard jump cut on the word)

## The word → edit map (gesture-spec.json)
His spec file maps words to edits, e.g. `{"zoom": "zoom_in", "punch": "punch_in", "jump": "jump_1"}`. The PWC version: a `gesture-spec.json` per video (or per lane) where each entry is `{"word": "<the spoken word>", "edit": "<zoom|punch|jump|…>", "at": "<word timestamp>"}`. The pipeline reads the file, pulls word timings from the transcript (Whisper word-timed), and lands each edit on its word. No keyframes by hand; no edits placed by eye.

## Executable steps (PWC)
1. **Film once, straight to camera, reading from the script.** The script is the source of truth — the words in the file are the words in the take.
2. **Pick the words in a text file:** for each payoff word, write one line — word, edit verb, timestamp (from the word-timed transcript). One line per edit, nothing else.
3. **Run the map:** the pipeline applies the spec — zoom slow, punch fast, jump cut — each landing exactly on its word. Words are never clipped at any cut (Q's standing rule); the edit lands ON the word, the word plays whole.
4. **QC:** the render is checked against the spec file — every spec line has a visible edit on its word, no edit exists that the spec didn't order.

## PWC skin
The verbs are Q's: zoom/punch/jump on payoff words, pop-ups on the exact spoken thing, punch-in zooms on payoff words (already Q's rule). Teal/gold on navy, no red, nothing over the face. The map is the edit — the editor (Claude) follows the file, the human (Q/Muse) writes the file.

## Gaps
- His pipeline code (the builder that reads gesture-spec.json + transcript and renders) is NOT in the harvest. The spec format + grammar above are INFERRED from the visible transcript; the builder must be authored from Q's existing render lane (Remotion / code render), labeled INFERRED.

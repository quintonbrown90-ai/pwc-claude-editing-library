<!-- PART: audio-sound/audio-clap-understanding.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# AUDIO / SOUND — CLAP: Claude's ears for sound (MEASURED license, INFERRED workflow)

Source: LAION CLAP (code MIT, weights MIT — laion/clap-htsat-fused, 512-dim
joint text/audio embedding) via @kappa.ai DecYkDcI799 + PART-DRAFTS-V6.md.
Do NOT substitute M2D-CLAP (non-commercial license) — LAION CLAP only.

## The rule
Text<->audio retrieval: describe a sound in words -> find the matching clip;
label every sound in a mix with a similarity score. Kappa's on-screen scores
ran 0.51–0.87; threshold >=0.5 counts as a "same sound" match.

## Executable steps
1. `pip install laion-clap`; load `laion/clap-htsat-fused`.
2. Embed the ~1,250-file licensed SFX library once (FAISS index).
3. Query by text ("find me a whoosh like this one") or by reference audio.
4. Use it three ways on Q's videos: (a) SFX library search instead of
   browsing filenames; (b) sound QC — CLAP-label each SFX on the timeline
   and flag mismatches (a "whoosh" that scores as "door slam" gets replaced);
   (c) beat matching — find music whose CLAP embedding matches the video's
   energy.

## Worked example (PWC)
The count-up landing needs a riser. Query "rising sweep, triumphant" ->
top hit scores 0.66 ("downward sweep" is the wrong direction — rejected).
The chosen SFX scores 0.71 as "rising whoosh" on the timeline QC pass.

## PWC skin
Input audio is Q's own licensed library only. CLAP never picks a sound from
outside the cleared library.

## Canonical-decode confirmation (Nov 8, 2026)
Parent's canonical decode (`research/video-harvest/instagram/
kappa_ai_DecYkDcI799_DECODE.md`) CONFIRMS the role verbatim — "Claude
tells Claude what each sound is" (transcript 24.6–26.8s) — and the
"+2 MORE" beat: CLAP + Demucs arrive together as the sound-design pair.
No correction to the workflow above.

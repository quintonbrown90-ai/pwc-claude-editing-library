<!-- DRAFT — v9 bulk-b (group B) — coordinator merges into parts/creator-systems/ -->
<!-- Sources: @kylewhitrow "Claude Code edited 53 videos at once" (DYxEl77Ef5M, batch CTA swap) + "Here's why I love editing videos using Claude Code" (DWBug1mDRGm, background-edit loop) + @ibraviz.ai "Cancel your video editing subscription" (DfceI14sESQ, 3 videos at once — variant). -->
<!-- Existing parts checked first: NO batch re-edit part exists. parts/render-pipelines/pipeline-repurposing-one-to-ten.md is one video → 10 trial reels + carousels (one-to-many, new outputs). This part is many videos → same videos, changed (batch re-edit of an existing set). parts/creator-systems/kylewhitrow-batch-logo.md is the batch-logo device. NEW part. -->
# CREATOR-SYSTEMS — batch re-edit: change one thing across the whole set (DRAFT — v9 bulk-b)

Source: @kylewhitrow "Claude Code edited 53 videos at once" (DYxEl77Ef5M). INFERRED reconstruction from the visible transcript.

## The rule
When one thing changes (a CTA, a keyword, a price, a date), load the affected set and change it everywhere at once — with a human decision per video, not a blind find-and-replace.

## Executable steps (PWC)
1. **Load the set:** the affected videos, each with its own cut timeline (per-video timelines, not one timeline for all 53).
2. **Review per video:** the human decides per video — trim here, clean there ("mark as clean" vs "trim at 39s"). The batch runs; the judgment stays per-video. This is the exact shape Q needs when a funnel changes (e.g. the waitlist reroute — every keyword flow flipped to WAITLIST): the set is the affected videos, the change is the reroute, the review is per video.
3. **Copy JSON handoff:** the review state travels as data, not as chat messages — "Copy JSON" carries every per-video decision in one paste. No per-video round trips.
4. **Render lane:** Remotion Studio is the programmatic edit layer — "this is effectively how Claude edits your videos programmatically." Q's code-based effects already render this way; the batch re-edit runs on the same lane.

## Supporting device — the background-edit loop (DWBug1mDRGm)
Film take N+1 while Claude edits take N. The filming day is a pipeline, not a queue: the camera never waits for the edit. Transcription-based cutting ("cut these clips in a sequence based on that transcription... eliminate any dead spaces... take the best take") is the spec for the rough cut, and "perfect match stops the clips at the right point" — cuts land on word boundaries, never clipped (Q's standing rule). The composition picker ("what type of video... different compositions") asks the video type FIRST, then picks the composition.

## Variant — 3 videos at once (ibraviz.ai DfceI14sESQ)
Same batch shape at small scale: three videos edited simultaneously, one pack. Q's all-at-once delivery ("build the whole set quietly, then ONE drop") is the same pattern at delivery time; this part is the same pattern at edit time.

## PWC skin
Per-video review is mandatory — a batch re-edit never ships unreviewed. The CTA/keyword/price in the swap is Q's current routing (WAITLIST until Dec 7), never a stale one. Teal/gold on navy, no red, nothing over the face, words never clipped at any cut.

## Gaps
- His batch-edit setup (prompts, tooling) is NOT in the harvest — the protocol above is INFERRED from the visible transcript.

## Variants (v9)
- **v9 · @kylewhitrow, ?:** **V112 — @kylewhitrow background-edit loop** — see V108 (also a variant on the new batch-cta-swap draft). _(source: bulk-b VARIANTS.md)_
- **v9 · @kylewhitrow, DWBug1mDRGm:** **V108 — @kylewhitrow background-edit loop (DWBug1mDRGm):** film take N+1 while Claude edits take N (→ kylewhitrow-batch-cta-swap, NEW draft); composition picker (ask the video type FIRST); "Perfect match stops the clips at the right point" (cuts on word boundaries). _(source: bulk-b VARIANTS.md)_
- **v9 · @ibraviz.ai, DfceI14sESQ:** **V111 — @ibraviz.ai 3-at-once batch (DfceI14sESQ):** simultaneous-edit pattern (→ kylewhitrow-batch-cta-swap, NEW draft). Computer-use cursor device: GAP/FLAGGED. 3D figurine + Claude robot conversation: GAP (generated characters, not Q's lane). Honest style-learning cost ("it took Claude a while to understand my style"): credibility device, noted in the draft. _(source: bulk-b VARIANTS.md)_

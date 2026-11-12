# PHONES — Sky's phone mockup / frame types

**What Sky does:** the phone is a *stage*, not a screenshot. A phone-frame mockup
plays the actual moment from the creator's video inside it, with a view-count badge
on the phone and thin accent annotation lines pointing from the phone to tiny labels
naming the technique. In reels the phone slides/drops in, plays, and exits on a hard
cut; in Breakdown carousels the phone is the center of every per-section slide.

**PWC rule:** execution templates use PWC colors (teal/gold on navy). The reference
frames below show Sky's own green/orange — they are the *source style*, never to be
copied pixel-for-pixel into Q's content. Never put another creator's actual video
inside Q's phone frame as if it were Q's — the phone plays Q's own footage, proofs,
or the creator being broken down (editorial breakdown only, never framed as a PWC
member or endorser).

## Phone types (verified from the 15 priority reels + carousels)

| Type | When Sky uses it | Reference frame | Motion clip |
|---|---|---|---|
| **A. IG Reels phone UI** — full Reels player (heart/comment/share rail, handle + Follow, caption bar) sliding in from the right; background behind it goes B&W while the phone stays in color (color isolation) | DfLa @2.2–5.5s | `phone_reels_mockup_DfLa_3.5s.jpg` | `../motions/trans_color_isolation_phone_DfLa.mp4` |
| **B. iPhone profile mockup** — iPhone frame showing an IG profile + follower count; drops in from top, small bounce, flies off top | DfTawo @17.2–19.5s (100K followers); DfQ4 @2.2–6.0s (profile + growth bar filling month 1→6) | `phone_iphone_100k_DfTawo_18.5s.jpg`, `phone_iphone_profile_DfQ4_4.0s.jpg` | `../motions/phone_slide_bounce_DfTawo.mp4`, `../motions/phone_drop_growthbar_DfQ4.mp4` |
| **C. iPhone "Show It Live"** — phone drops in top-center with title above; screen shows a LIVE video; labels pop around the phone (Product / Service / Coaching) | DfQ4 @19.5–23.0s | `phone_show_it_live_DfQ4_21.0s.jpg` | `../motions/phone_show_it_live_DfQ4.mp4` |
| **D. Small phone top-center** — small phone showing an IG video post with like/comment/share rail; fades ~1.5s | DfPxq @0.2–1.5s | (no clean still — phone is small + brief; see motion clip set, DfPxq opening) | — |
| **E. Carousel Breakdown phone** — phone-frame mockup center-slide, corner brackets, view-count badge (eye + count) on top, green annotation lines to technique labels, transcript card + scrubber below | Archetype A carousels (DfIyn6xCsUH Jeff Nippard, DfS-L51j4hK Shelby Sapp) | `phone_carousel_breakdown_nippard_s02.jpg` (9.6M badge, "THE HOOK" slide), `phone_carousel_breakdown_sapp_s02.jpg` | — (slides are MP4s; see `examples/carousels/`) |
| **F. D11 chip-cluster phone** — orange dots in a dotted arc above the phone frame + a quiz card whose words accumulate as a vertical list | DeYKk (quiz card; three creator video cards above it) | `../charts/chart_quiz_chipcluster_DeYKk_28.0s.jpg` | `../motions/dev_quiz_accumulate_DeYKk.mp4` |

## Geometry (measured, 720×1280 source coords — scale ×1.5 for 1080×1920)

- Reels phone (DfLa): ~x450–950, y40–480 (right-of-center, top half). Slides in from
  right, exits right ~5.2s. Rail on the phone's right edge.
- iPhone profile (DfTawo): ~x620–900, y200–450, top-right, drop + bounce.
- iPhone profile (DfQ4): top-center; growth bar below the phone, fill animates
  left→right ~3.8–5.5s.
- Carousel phone: center, ~55–60% of slide height; corner brackets; badge on top
  edge of the phone; annotation lines thin green, labels outside the phone.

## Execution templates (PWC colors — use these, not the refs)

- `../templates/phone_frame_pwc.png` — transparent 1080×1920 iPhone frame (navy
  bezel, gold hairline, dynamic island, home indicator). Drop Q's footage / screen
  recording into the transparent screen area.
- `../templates/phone_frame_pwc.svg` — same frame as vector.

## Sources

- Reels: `~/workspace/goals/realskytan-style-steal-for-q-s-content/hidden_files/priority15_videos/`
  (07_DfLaEFNDKkv, 05_DfQ4E1Hjn0n, 03_DfTawo5jHMH, 06_DfPxqFPAY4_)
- Carousels: `~/workspace/claude-editing/examples/sky/carousel-styles/DfIyn6xCsUH/`
  (slide 02, 10.2s) and `.../DfS-L51j4hK/` (slide 02); full breakdown in
  `../../examples/carousels/CAROUSEL_BREAKDOWN.md` (Archetype A).
- Specs: `../../STYLE-GRAMMAR.md` §4 (D10/D11), `../../examples/SKY_MOTION_TEARDOWN.md`.

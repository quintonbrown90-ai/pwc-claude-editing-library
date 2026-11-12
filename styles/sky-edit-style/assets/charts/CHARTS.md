# CHARTS — Sky's chart / diagram types (D1–D25 devices)

**Sky's verified chart grammar (G-04, resolved Nov 9):** the chart is a STATIC base
and ANNOTATIONS STACK on top in order. The line does NOT draw on continuously —
values update and annotation labels appear on top of an already-drawn line. (The
0.5–3.0s left-to-right line draws WITH a glowing leading dot ARE verified in the
motion clips for retention graphs and process lines — see MOTIONS.md — but the
"Views over time" line specifically is already drawn; values + annotations stack.
Build per-device: check the motion clip for that device before choosing draw vs
static-base.)

**PWC recolor:** reference frames show Sky's green/orange. Execution templates in
`../templates/` use teal #14A886 / gold #FEE238 on navy #00214E. Red → gold.

## Chart types (one frame per type in this folder)

| Type | Device | Reference frame | What it shows |
|---|---|---|---|
| Line — retention graph | D6 | `chart_retention_draw_DfU49_4.0s.jpg` | Glass panel, green line draws L→R with glowing dot; Hook/Lead brackets map onto the curve |
| Line — retention HUD | D6 | `chart_retention_hud_DfSf_2.5s.jpg` | Empty panel, line draws, "34%" endpoint, "Drop-off" pill |
| Line — views over time | D6 | `chart_views_time_DfPxq_27.0s.jpg` | S-curve, counter climbing to 2.6M, "Plateau" / "Second push" annotations stacking |
| Venn / crossover | D7 | `chart_venn_DfPxq_74.0s.jpg` | "Your audience" / "Their audience", solid GREEN lens overlap, faces in circles at top of each circle |
| Staircase chart | D6 var. | `chart_staircase_DfX2_50.5s.jpg` | White staircase draws L→R, head cutout at top step, green dots pulse on it |
| Funnel — pills rain | D4 | `chart_funnel_rain_DfX2_1.2s.jpg` | Funnel icon, white pills rain in one at a time, one green pill drops out the bottom |
| Funnel — 3 tiers | D24 var. | `chart_funnel_tiers_DeA2_59.5s.jpg` | Blue "Viral Reel" / purple middle / green bottom tiers + "$" pops below |
| Funnel card | D24 | `chart_funnel_card_DfA9_55.5s.jpg` | Glass card, rows CONTENT → CHECKOUT PAGE / VSL, "FEEDS INTO BRAND" orange bar |
| Era timeline | D12 | `chart_timeline_DeA2_41.5s.jpg` | Static full-width line; nodes pop ~0.5s apart (accent ring + filled dot, label ABOVE); example thumbnails cluster UNDER the active node (2×3 grid, dashed accent border); line y ~300/1920 |
| Tier list | D5 var. | `chart_tier_list_DfQ4_8.0s.jpg` | White card, S/A/B/C tier rows, gray squares filling in one at a time |
| Script-anatomy bars | D15 | `chart_script_anatomy_Dez4_43.2s.jpg` | Left labels (Hook / Lead / Body 1 / Open loop 1 / Body 2 / Open loop 2 / Body 3 / CTA) + horizontal bars colored per part; circular loop icon on open-loop rows |
| Script lines | D6 var. | `chart_script_lines_DfSf_17.0s.jpg` | Glass panel, white "Hook" line, RED "Lead" lines bracketed, GREEN line; active line PULSES (brightness/glow spike ~2.5×, ~0.3s) |
| Trust dot-grid | D17 | `chart_dotgrid_trust_DeYKk_5.0s.jpg` | Grid of dots (the audience) flipping red (lose trust) → green (gain trust); category labels (Community, Digital Product, Coaching, Course) + profile faces around it |
| "100s of people" grid | D19 | `chart_100s_grid_DeYKk_76.0s.jpg` | Grid of many small orange squares — a visual count of people |
| Affiliate / network loop | D18 | `chart_affiliate_loop_DeYKk_68.0s.jpg` | Dashed curved line connecting profile photos (participation loop) |
| Views-refresh insert | D20 | `chart_views_refresh_DeSTW_4.0s.jpg` | 3×3 profile grid with per-video view counts (8,547 / 4,246 / 6,540) + "GOING VIRAL" labels, above his head |
| "New Post" placeholder | D22 | `chart_newpost_placeholder_DeSTW_18.0s.jpg` | Dashed-border card with "+" and "New Post" that fills with thumbnails |
| Quiz chip-cluster | D11 | `chart_quiz_chipcluster_DeYKk_28.0s.jpg` | Orange dots in a dotted arc above the phone frame + quiz card whose words accumulate as a vertical list (Legit, Business, Very Successful, Flashy, Money, Humble, Relatable, Warm, Emotional, Friendly, Caring) |
| Narrative-arc bars | D15 var. | `chart_narrative_arc_DfDu_49.0s.jpg` | Orange-bordered glass panel; rows build one at a time (Intro blue / Rising action orange / Conflict red / Climax yellow) |
| Card grid | D10 var. | `chart_card_grid_DfDu_41.5s.jpg` | Grid of orange play-cards + small video thumbnails fanning out across the top (~8 cards, two rows) |
| "How I Made Money" card | D20 var. | `chart_how_i_made_money_DeYKk_60.0s.jpg` | Money-breakdown card ($1,700 / $1,000 / $500 / $100 / $2,300) under numbered pill #3 |
| Workflow strip / 6-box grid | D13 | `chart_workflow_grid_DfA9_9.8s.jpg` | Glass panel, 6 numbered boxes in 2 columns (1. Goal, 2. Creator, 3. Avatar, 4. Market, 5. Offer, 6. Funnel) appearing one at a time |

## Motion (see `../motions/MOTIONS.md`)

Line draws: `chart_retention_draw_DfU49.mp4`, `chart_wave_draw_DfQ4.mp4`,
`chart_views_countup_DfPxq.mp4` (values climbing). Builds: `dev_venn_fill_DfPxq.mp4`,
`dev_staircase_draw_DfX2.mp4`, `dev_timeline_nodes_DeA2.mp4`,
`dev_funnel_rain_DfX2.mp4`, `dev_funnel_tiers_DeA2.mp4`, `dev_funnel_card_DfA9.mp4`,
`dev_scriptlines_pulse_DfSf.mp4`, `dev_flow_lines_DfU49.mp4`,
`dev_dotgrid_flip_DeYKk.mp4`, `dev_100s_grid_DeYKk.mp4`, `dev_newpost_fill_DeSTW.mp4`,
`dev_affiliate_loop_DeYKk.mp4`, `dev_anatomy_bars_Dez4.mp4`, `dev_tier_list_DfQ4.mp4`.
Frame sequences: `../motions/frames_retention_draw/`, `../motions/frames_staircase_draw/`
(6 fps step-throughs of the two canonical draws).

## Execution templates (PWC colors — in `../templates/`)

- `chart_line_pwc.svg` — retention / views-over-time panel (glass card, teal axes,
  sample teal line + glowing gold dot, HOOK | LEAD slots).
- `chart_bar_pwc.svg` — D15 script-anatomy horizontal bars (teal/gold/blue rows,
  loop-icon markers).
- `chart_funnel_pwc.svg` — 3-tier funnel (teal / gold / white tiers).
- `chart_venn_pwc.svg` — D7 Venn (teal + gold circles at 45% opacity, solid teal
  overlap lens, dashed face slots).

## Full device specs

`../../STYLE-GRAMMAR.md` §4 (D1–D25, measured parameters), `../../examples/SKY_MOTION_TEARDOWN.md`
(35-device master index), `../../examples/PREMIUM_DEPTH_MEASUREMENTS.md` (Nov 9 verification).

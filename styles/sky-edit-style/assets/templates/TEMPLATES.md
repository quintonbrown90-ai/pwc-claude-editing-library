# TEMPLATES — PWC execution templates (use these to build; the refs show the style)

**Brand colors (bind on every execution template):** teal #14A886 · gold #FEE238 ·
navy #00214E. White #FFFFFF. NO RED anywhere. Sky's own green/orange appears ONLY
in the reference frames (`../phones/`, `../captions/`, `../charts/`) — never in a
template Q ships.

**What these are:** clean, build-ready templates in PWC colors, derived from the
measured Sky geometry in `../../STYLE-GRAMMAR.md`. They are NOT screenshots of
Sky's videos — they are the Q-lane versions Claude builds from.

| File | What it is | Built from |
|---|---|---|
| `phone_frame_pwc.png` | Transparent 1080×1920 iPhone frame: navy bezel, gold hairline around the screen, dynamic island, home indicator, side buttons. Screen area is fully transparent — drop Q's footage / screen recording into it. Pixel-verified: center transparent, bezel navy opaque, border gold. | DfLa/DfQ4/DfTawo phone geometry (`../phones/PHONES.md`) |
| `phone_frame_pwc.svg` | Same frame as vector (viewBox 1080×1920). | Same |
| `chart_line_pwc.svg` | Retention / views-over-time panel: navy glass card, teal axes, sample teal line with glowing gold dot, HOOK \| LEAD slots, value label. | D6 (`../charts/chart_retention_draw_DfU49_4.0s.jpg`) |
| `chart_bar_pwc.svg` | D15 script-anatomy bars: Hook / Lead / Body 1 / Open loop 1 / Body 2 / Open loop 2 / Body 3 / CTA rows, loop rows carry the circular-arrow icon. | D15 (`../charts/chart_script_anatomy_Dez4_43.2s.jpg`) |
| `chart_funnel_pwc.svg` | 3-tier funnel (teal / gold / white): "99% OF IDEAS" → "THE FEW THAT FIT" → "THE ONE THAT SHIPS", gold dot below. | D4/D24 (`../charts/chart_funnel_rain_DfX2_1.2s.jpg`) |
| `chart_venn_pwc.svg` | D7 Venn: teal + gold circles at 45% opacity, solid teal overlap lens, dashed face slots at the top of each circle. | D7 (`../charts/chart_venn_DfPxq_74.0s.jpg`) |
| `caption_demo_pwc.png` | 1080×1920 layout demo: navy ground, gold headline "REJECTS 99%" + white subline (the separate-headline device), all-white caption group "GOOD CONTENT" center-lower, face zone marked KEEP CLEAR, safe-zone guides at y=300 / y=1600. | D1/D2 (`../captions/CAPTIONS.md`) |

## What is NOT templated here (and why)

- **D5 checklist / D12 timeline / D24 funnel card / D17 dot-grid / D19 100s-grid:**
  fully specified in `../../STYLE-GRAMMAR.md` §4 + `../../code/sky_devices.py`
  (D5-list, D12 timeline implemented); no static template filed because the motion
  IS the device — use the motion clips in `../motions/` + the code, not a still.
- **No door template.** The door device is DEAD in every form.
- **No CapCut template/animation IDs** for Sky's devices exist on disk (G-09) —
  these SVGs/PNGs are the build inputs for CapCut-native construction, not CapCut
  exports themselves.

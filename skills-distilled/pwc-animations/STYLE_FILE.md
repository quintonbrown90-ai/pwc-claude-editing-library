# STYLE_FILE — the shared brand sheet every animation reads

From @viashaan's system: his animations stay on-brand across videos because
ONE style file is handed to the model every single time (his reel: "Do you
keep one style file so every animation stays on-brand" — yes, this file).
Templates here hard-code these tokens; a new animation copies them verbatim.
Never invent a color, font or radius inside a one-off animation.

## Tokens

```css
:root{
  --navy:#00214E;        /* PWC deep navy — cards, panels */
  --navy-2:#0A2A52;      /* gradient partner */
  --blue:#013B6B;
  --teal:#14A886;        /* PWC teal — lines, accents (NOT #2DD4BF) */
  --gold:#FEE238;        /* PWC gold — payoffs, pins, final numbers */
  --gold-deep:#F5B921;
  --white:#FFFFFF;
  --paper:#F5EFE2;       /* headline / paper surfaces */
  --ink:#12233C;         /* text on paper */
}
```

- Fonts: Anton (display/numbers), Poppins ExtraBold (labels), Playfair
  Display Bold Italic (serif accents/headlines), Caveat Bold (handwriting).
  Bundled in fonts/ and loaded via @font-face — no web fonts, no substitutes.
- Card language: navy gradient (150deg, navy-2 → navy), 36px radius, 3px
  teal border at 55% alpha. Paper language: paper bg, ink text, Anton
  mastheads, Playfair headlines.
- NO RED anywhere. The reference animations use red suns/pins — PWC maps
  red → gold for pins/accents; the ink-wash sun is the single warm exception
  and renders in burnt orange, never traffic red.
- Stage: 1080×1920, transparent outside the card, so renders overlay onto
  footage. Cards sit inside the IG safe zones when composited (x 70–1010,
  y 300–1500 region).

## Timing-to-speech rule

An animation is an INSERT, timed like one: it enters on the exact noun or
number that calls it, completes its main move inside the spoken phrase, and
either holds (speaker keeps talking over it) or exits EASE IN 5–6 frames
before the sentence ends. Duration defaults: stat-chart 3.2s, map-route
3.4s, headline 3.6s, teardown 3.8s, paper-desk 4.0s, ink-wash 4.5s.

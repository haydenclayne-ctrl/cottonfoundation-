# Typography

Two faces do all the work: a Garamond-class serif for everything that should feel warm and established, and a plain, sturdy sans for everything that has to be read quickly. The serif is the Foundation's voice; the sans is its handwriting on a clipboard.

Both are open source (SIL OFL) on Google Fonts, so the same faces run on the website, in email, in documents, and in Claude Design with no licensing work.

## What exists today (as built on the old cottonfoundation.org)

| Role | Face | Weight | Where it appears |
|---|---|---|---|
| Display | **Cormorant Garamond** | 700 | Every heading (H1–H5), the statistics, pull quotes |
| Body and UI | **PT Sans** | 400 body, 700 UI, 600 nav | Body copy, navigation, buttons, eyebrow labels, form labels, footer |
| Loaded, secondary | **DM Sans** | 400 | Set as the Elementor "Text" and "Accent" global fonts; a few text widgets. Computed body text renders in PT Sans (the theme setting wins) |
| Icons | Font Awesome 5 | — | The heart in "Donate Now", phone, clock, map pin, social icons |

The logo's wordmark ("COTTON" / "FOUNDATION") is a Garamond-class serif set in capitals. It is supplied as outlines only; whether it is Cormorant Garamond or another Garamond is unconfirmed (decision log Q3). Do not typeset the wordmark; use the lockup files.

## The type system: four roles

| Role | Job | Face | Rules |
|---|---|---|---|
| **1. Display Serif** | Headings, statistics, the hero headline, pull quotes, invitation and formal print | Cormorant Garamond 700 (600 for print at large sizes if 700 looks heavy) | Mixed case for sentences ("Restoring Hope"); Title Case for section headings as built ("A Place For Healing, Built With A Purpose"). Never all caps at display size except in the wordmark |
| **2. Utility Sans** | Body, navigation, buttons, forms, captions, tables, email | PT Sans 400 / 700 | Sentence case for body. Uppercase only in the three UI roles below |
| **3. Eyebrow Caps** | The small uppercase label above a heading ("WHO WE ARE", "A PLACE OF HOPE", "CREATING MEMORIES") | PT Sans 700, uppercase | As built 16 px, tracking 0–1 px, Harvest Gold on light / Horizon Blue on dark. Recommended: 13–14 px, tracking 0.10 em, Hope Gold on dark (contrast) |
| **4. Button and Nav Caps** | Buttons and the primary navigation | PT Sans 700 (buttons), 600 (nav), uppercase | Buttons 16 px, no extra tracking; nav 15 px, tracking 1 px |

Do not add a fifth face. Do not substitute a geometric sans (Montserrat, Poppins), a slab, a script, or a condensed display face. If DM Sans is kept (Q5) it replaces PT Sans in role 2; it does not join it.

## Display Serif: the rules

- **Weight 700** on screen. Cormorant Garamond is light by design; 400 disappears at text sizes and 500 reads thin on white. Print may use 600.
- **Line height 1.15–1.25** at display sizes. The old site inherits 1.5 from the theme (H1 64/96 px), which floats the lines apart; the design phase tightens it (`--cf-leading-heading: 1.2`).
- **Size scale (web, as built):** H1 64 px · H2 40–48 px · H3 32 px · H4 24 px · statistics 56 px · hero statistic 120 px. Mobile: H1 40, H2 32, H3 26, statistics 44.
- **Numerals:** Cormorant's default figures are old-style (a "30" or "150+" sits below the cap line). This is part of the look; keep it for statistics and dates. Use lining figures (`font-variant-numeric: lining-nums`) only in tables and forms.
- **Case:** Title Case for headings that are labels; sentence case for headings that are sentences. Never all caps.
- **Color:** Foundation Navy on light grounds; white on navy and photography; Hope Gold only for statistics on navy.
- **Italic:** for a single emphasized word or a place name, never a whole heading.

## Utility Sans: the rules

- **Body:** 16 px / 1.5 (24 px) as built; 15 px on dense pages; never below 13 px except legal lines. Color **Ink**, not Slate (see `colors.md`).
- **Measure:** 60–75 characters; the old site's text column is about 720 px at 16 px.
- **Bold** (700) for lead-ins ("Phase 1", "Phase 2"), form labels, and every uppercase role.
- **Links** in body copy: Foundation Navy, underlined on hover only. Footer links: white, no underline.
- **Buttons:** PT Sans 700, 16 px, uppercase, padding 12 × 24 px, radius 8 px. See `components.md`.

## Eyebrow Caps: the rules

The eyebrow is the brand's most-used typographic device. Every section on the old site opens with one:

> WHO WE ARE · OUR MISSION · A PLACE OF HOPE · OUR PARTNERS · TOGETHER, WE MAKE IT HAPPEN · THE LEGACY OF TOM WALLACE · MEET TAYLOR ODUM · CONSTRUCTION PROGRESS · CRAWFISH FOR A CAUSE · GET IN TOUCH · CREATING MEMORIES · SUPPORT US

- Always uppercase, always PT Sans 700, always one line, two to five words.
- Sits 8–12 px above its heading, left-aligned with it (or centered when the heading is centered).
- Harvest Gold on white and Mist. On navy and photography, Hope Gold or white (as built it is Horizon Blue, which fails contrast at 2.2:1).
- Never a sentence, never punctuation except a comma, never a link.

## Sizes and scale

**Web:** base 16 px PT Sans, line height 1.5; headings Cormorant Garamond 700 at 24 / 32 / 40 / 48 / 64 px; eyebrows 13–16 px caps; captions 13 px Slate.

**Print (letterhead, donor materials, the sponsorship catalog):** body 10–11 pt PT Sans; eyebrows 7.5–8 pt caps at +100 tracking; headings Cormorant Garamond 600–700 at 24–48 pt; statistics 48–72 pt.

**Signage:** letter height 25 mm per 10 m of viewing distance. Gate and plaque lettering follows the Taylor's Place sign: serif capitals letterspaced, a sans line beneath. Cut metal and routed panels use the lockup files, never live type.

**Email:** Cormorant Garamond and PT Sans via Google Fonts where the client supports web fonts; fall back to Georgia and Arial. Headings 28–32 px, body 16 px.

## Pairings

- Section: Eyebrow Caps (Harvest Gold) over Display Serif (Navy) over Utility Sans body (Ink). This trio is the page rhythm; see `components.md`.
- Statistic: Display Serif figure (56 px, Navy or Hope Gold) over a Button-Caps label (PT Sans 700, 13–15 px).
- Card: Display Serif title (32 px) over two lines of Utility Sans over a navy button.
- Lockup: the wordmark is artwork; nothing is typeset next to the mark except in the endorsement line of Taylor's Place (see `sub-brands.md`).

## Licensing

Cormorant Garamond (Catharsis Fonts), PT Sans (ParaType), and DM Sans (Colophon Foundry) are licensed under the SIL Open Font License 1.1: free for web, print, apparel, and signage, including commercial use. No purchase is required. Self-host the WOFF2 files on the new site rather than loading from Google's servers if page speed or privacy policy requires it; record the version used in `tokens/README.md`.

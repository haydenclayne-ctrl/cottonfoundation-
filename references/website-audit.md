# Website Audit: cottonfoundation.org, 2026-09-22

The old website is the source of this design system's *visual* values. This is the record of what was read from it, so every value in `tokens/` and `guidelines/` can be traced back, and so the new site can be checked against the old one.

The audit is limited to design: colors, type, spacing, components, and the structure of the home and Taylor's Place pages. The old site's copy, statistics, history, and any content outside the Foundation and Taylor's Place are **not** part of this brand and are not recorded here (decision log D11). Screenshots of the relevant pages at a 1316 px viewport are in `website-screenshots/`; their text is superseded and must not be carried forward.

**Platform:** WordPress with the Astra theme and Elementor (kit 886), Elementor header/footer, an EmbedSocial Instagram feed, reCAPTCHA on forms, an external donation platform.

**Pages read for design:** Home `/` and Taylor's Place `/taylors-place/`. Other pages were scanned only to confirm the same components repeat.

## Global colors (Elementor kit)

| Kit slot | Value | Given the name |
|---|---|---|
| Primary | `#17345E` | Foundation Navy |
| Secondary | `#A07400` | Harvest Gold |
| Text | `#17212E` | Ink |
| Accent | `#FFFFFF` | White |
| Custom | `#B1B1C2` | Silver |
| Custom | `#3E6B9C` | Horizon Blue |
| Custom | `#E0A600` | Hope Gold |
| Custom | `#F3F3F3` | Cloud |
| Custom | `#BD202E` | Signal Red |
| Custom (duplicates) | `#FFFFFF`, `#A07400`, `#17345E`, `#3E6B9C`, `#B1B1C2` | — |

Measured, not declared: body text `rgb(128,130,133)` = `#808285` (Slate, the Astra default); the "Who We Are" band `rgb(245,248,250)` = `#F5F8FA` (Mist). The Astra global palette (`#0170B9` etc.) is the theme's untouched default and plays no role.

Logo file colors, measured from opaque pixels: boll `#9F762B`, hands and wordmark `#16345E`.

## Global typography (Elementor kit)

| Kit slot | Face | Weight |
|---|---|---|
| Primary | Cormorant Garamond | 400 |
| Secondary | PT Sans | 400 |
| Text | DM Sans | 400 |
| Accent | DM Sans | 400 |

Kit rule for buttons and inputs: PT Sans, 700, line-height 150%. Fonts loaded: Cormorant Garamond 300–700 (with italics), DM Sans 100–900, PT Sans 400/700 (with italics), Font Awesome 5 Free and Brands. One event heading rendered in "Athelas" (a local system font; ignore).

## Computed styles (home page unless noted)

| Element | Face | Size / line-height | Weight | Case, tracking | Color |
|---|---|---|---|---|---|
| body | PT Sans | 15 / 24.75 px | 400 | — | `#808285` |
| Text-editor paragraphs | PT Sans | 16 / 24 px | 400 | — | white on navy, Ink on white |
| H1 (hero headline) | Cormorant Garamond | 64 / 96 px | 700 | — | white |
| H2 "Our Mission" | Cormorant Garamond | 40 / 60 px | 700 | capitalize, 1 px | `#17345E` |
| H2 (CTA band headline) | Cormorant Garamond | 48 / 72 px | 700 | — | white |
| H3 (card titles, e.g. "Taylor's Place") | Cormorant Garamond | 32 / 48 px | 700 | — | `#17345E` |
| H4 (lead paragraph) | Cormorant Garamond | 24 / 36 px | 700 | — | `#17212E` |
| H5 "Stronger Together" | Cormorant Garamond | 40 / 60 px | 700 | — | `#17345E` |
| Statistics (light band) | Cormorant Garamond | 56 px | 700 | — | `#17345E` |
| Eyebrow "WHO WE ARE" | PT Sans | 16 px | 700 | uppercase, 0 | `#A07400` |
| Eyebrow "A PLACE OF HOPE" | PT Sans | 16 px | 700 | uppercase, 1 px | `#A07400` |
| Eyebrow (hero, on the overlay) | PT Sans | 16 px | 700 | uppercase, 0 | `#3E6B9C` |
| Navigation links | PT Sans | 15 / 20 px | 600 | uppercase, 1 px | `#17212E` |
| Button labels | PT Sans | 16 / 21.6 px | 700 | uppercase, 0 | see buttons |

## Buttons (computed)

| Button | Background | Text | Border | Radius | Padding |
|---|---|---|---|---|---|
| Donate Now (header, on hero) | white | `#2C2C2C` | 0 | 8 px | 12 × 24 |
| Donate Now (header, scrolled) | `#17345E` | white | 0 | 8 px | 12 × 24 |
| Learn more about Taylor's Place | `#E0A600` | `#17212E` | 2 px transparent | 8 px | 12 × 24 |
| Secondary hero button | transparent | white | 2 px white | 8 px | 12 × 24 |
| Learn more about us | `#17345E` | white | 2 px white (invisible) | 8 px | 12 × 24 |
| Secure your spot (CrawFest) | `#A07400` | white | 2 px `#B1B1C2` | 8 px | 12 × 24, 24 px text |
| Outline on white | transparent | `#17345E` | 2 px `#17345E` | 8 px | 12 × 24 |
| Submit (forms) | `#A07400` | white | — | 8 px | — |

## Layout (computed)

| Value | Reading |
|---|---|
| Elementor container | 1440 px max (`min(100%, 1440px)`) |
| Content column | 980 px measured (x 162–1143 at a 1316 px viewport) |
| Header | 112 px tall, static, no shadow, transparent over the hero |
| Section padding | 80 px (most), 100 px (hero, impact band), 0 (full-bleed bands) |
| Grid gap | 64 px in split sections |
| Cards | radius 24 px, shadow `0 2px 4px rgba(0,0,0,.10)`, padding 0 0 24 px |
| Navy impact panel | radius 24 px, 560 px tall |
| Photographs in column | radius 24 px |
| Hero overlay | navy at roughly 70–75% over the photograph |

## Page structure (design only)

**Home:** transparent header over hero (photo, white lockup, eyebrow, H1, copy, gold + outline buttons) → two-column "Who We Are" on Mist with three statistics → centered "Our Mission" with two cards → navy impact band (hero statistic, four statistics, watermark) → split media "Inside Taylor's Place" (video) → "Our Partners / Stronger Together" logo carousel → split section with a blue statistic list → CTA band over the ranch aerial (H2, Donate Now + Questions? Contact us.) → Instagram feed → navy footer (lockup, mission, gold Donate, links, contacts, social) → legal line.

**Taylor's Place:** breadcrumb → split hero (H1 "Taylor's Place", eyebrow CREATING MEMORIES, copy, "See Sponsorship Opportunities", rendering of the entrance arch) → "The Legacy of Tom Wallace" centered with four family photographs → "Meet Taylor Odum" split with the YouTube update video → "Construction Progress" split with a rendering carousel (Phase 1, Phase 2, timeline) → CrawFest band over the gate-sign photograph → partners carousel → "Get in Touch" form on a navy panel → footer.

## Logo assets in the media library

See `assets/originals/INVENTORY.md` for the seven files brought in and the description of what was left out.

## Findings the design phase should act on

1. Body text is Slate `#808285` (3.85:1 on white): fails AA. Use Ink.
2. The hero eyebrow is Horizon Blue on the navy overlay (2.2:1): fails. Use Hope Gold or white.
3. Heading line height is the theme default 1.5; Cormorant Garamond wants 1.15–1.25.
4. Eyebrows at 16 px bold are large for their job; 13–14 px with 0.10 em tracking reads more refined. The 16 px size does keep Harvest Gold above the large-text threshold, so if the size drops, the color must hold at 14 px bold minimum.
5. Two button golds (Harvest for Submit and CrawFest, Hope for CTAs) and white-on-Harvest-Gold text at 4.2:1: decide one CTA gold with Ink text (Q7).
6. The mobile header shows the horizontal lockup at about 160 px, below its 200 px minimum. A compact lockup is needed.
7. The header has no sticky treatment or shadow; the content column is 980 px inside a 1440 px container, which leaves wide margins on large screens (fine, but the hero and bands should stay full bleed).
8. The old site's copy and statistics are not carried forward; the new templates must not hard-code any figure, date, or claim until the owner confirms it (Q2, Q8).
9. The donation flow leaves the site for an external platform; the new site should style or wrap that hand-off (Q11).
10. The partner carousel mixes many logo colors; consider grayscale at rest, color on hover.
11. The footer must carry the Foundation lockup alone (`brand/brand-architecture.md`, Independence).

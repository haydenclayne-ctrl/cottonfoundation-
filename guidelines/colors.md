# Colors

**Foundation: navy and gold, on white.** Navy carries the institution, gold carries the hope, white gives both room. The palette is small: three primaries, two secondaries, one accent, and a neutral scale. Do not add a color without a `brand/decision-log.md` entry.

Every value below was read from the old cottonfoundation.org Elementor kit or measured from the supplied logo files on 2026-09-22 (`references/website-audit.md`). Cotton Gold is the one value that is not a choice: it is the exact fill of the cotton boll in the 2026 logo artwork. Pantone values are the nearest solid-coated matches by eye and have **not** been proofed; CMYK values are press starting points. **Proof against a Pantone swatch before any print, thread, or signage order.**

## Primary

| Name | HEX | RGB | CMYK (start) | Pantone (nearest, unverified) | Role |
|---|---|---|---|---|---|
| **Foundation Navy** | `#17345E` | 23 / 52 / 94 | 100 / 80 / 30 / 25 | 534 C | The brand's dark. Headings, primary buttons, the impact band, the footer, hero overlays, the mark's hands and the wordmark |
| **Cotton Gold** | `#9F762B` | 159 / 118 / 43 | 30 / 50 / 95 / 15 | 7557 C | The boll in the mark. Mark color only: never a UI fill or text color |
| **Harvest Gold** | `#A07400` | 160 / 116 / 0 | 30 / 50 / 100 / 15 | 125 C / 7557 C region | Eyebrow labels on light grounds, the form SUBMIT fill, small accents, social icon rings |

Foundation Navy is recorded at the site kit value `#17345E`. The supplied logo PNGs measure `#16345E`, one unit darker in red, which is export rounding; the two are indistinguishable. Decision D3 makes `#17345E` canonical and the derived vectors use it.

## Secondary

| Name | HEX | RGB | CMYK (start) | Pantone (nearest, unverified) | Role |
|---|---|---|---|---|---|
| **Horizon Blue** | `#3E6B9C` | 62 / 107 / 156 | 80 / 55 / 15 / 5 | 7683 C | Eyebrow labels over photography and navy (as built), statistic figures on light grounds, secondary icons |
| **Signal Red** | `#BD202E` | 189 / 32 / 46 | 15 / 100 / 85 / 5 | 1797 C | Defined in the site kit. Reserved for form errors and alerts. Never decorative, never a heading color |

## Accent

| Name | HEX | RGB | CMYK (start) | Pantone (nearest, unverified) | Role |
|---|---|---|---|---|---|
| **Hope Gold** | `#E0A600` | 224 / 166 / 0 | 10 / 35 / 100 / 0 | 124 C | The call-to-action color: "Learn more about Taylor's Place", the footer "Donate Now", the hero statistic on the impact band, the statistics on navy. Always paired with Ink text, never white |

## Neutral

| Name | HEX | RGB | Role |
|---|---|---|---|
| **Ink** | `#17212E` | 23 / 33 / 46 | Body and heading text on light grounds; text on Hope Gold buttons |
| **Slate** | `#808285` | 128 / 130 / 133 | Captions, metadata, disabled states. The old site's inherited body-text default; see the contrast note below |
| **Silver** | `#B1B1C2` | 177 / 177 / 194 | Rules, borders, outline-button strokes on navy, form-field borders |
| **Mist** | `#F5F8FA` | 245 / 248 / 250 | Alternate section background (the "Who We Are" band) |
| **Cloud** | `#F3F3F3` | 243 / 243 / 243 | Form-field fills, subtle panels |
| **White** | `#FFFFFF` | 255 / 255 / 255 | The page. The mark and lockup reversed on navy and on photography |

Pure black `#000000` is permitted for utility (engraving proofs, laser masks, vinyl cut, forms) but is not a brand color.

## Three golds, and why

The brand currently uses three distinct golds, each with a job:

1. **Cotton Gold** `#9F762B` lives only inside the mark. It is warm and slightly bronze so the boll reads as an object, not a highlight.
2. **Harvest Gold** `#A07400` is the *text* gold: saturated enough to read on white at small sizes (4.2:1), used for eyebrow labels.
3. **Hope Gold** `#E0A600` is the *button* gold: bright enough to carry a call to action on navy (5.7:1) and on white as a fill with dark text.

They are close cousins, not the same color, and they must not be swapped: Hope Gold as text on white fails contrast (2.2:1); Cotton Gold as a button looks muddy. Whether the design phase consolidates Harvest and Hope into one UI gold is open (decision log Q7). Until then, use each only in its role.

## Approved colorways for the mark and lockups

| # | Mark | Ground | Use |
|---|---|---|---|
| 1 | **Full color** (Cotton Gold boll, Foundation Navy hands and wordmark) | White, Mist, Cloud | **Hero.** Web header, print, documents, signage on light panels. The default |
| 2 | White (one color) | Foundation Navy | Footer, navy panels, the impact-band watermark, apparel on navy |
| 3 | White (one color) | Photography with the navy overlay | Hero sections, video posters, event banners |
| 4 | Foundation Navy (one color) | White, Mist, Cloud | One-color print, forms, letterhead second color, embroidery on light garments |
| 5 | Cotton Gold (one color) | Foundation Navy | Gate plaques, foil, thread, formal print (the Taylor's Place sign uses this register) |
| 6 | Black (one color) | White | Utility only |

Not approved: the full-color mark on navy or on photography (the navy hands vanish); any gold other than Cotton Gold inside the mark; the mark or lockup in Harvest Gold, Hope Gold, Horizon Blue, or Signal Red; gradients, bevels, shadows, or metallic effects simulated on screen; tints of any color inside the mark.

## Contrast (screen), measured

From `python3 tools/contrast_check.py`:

| Pair | Ratio | Verdict |
|---|---|---|
| Ink on White | 16.2:1 | AAA. Body text |
| Navy on White | 12.4:1 | AAA. Headings, buttons |
| White on Navy | 12.4:1 | AAA. Text on the impact band, footer |
| Ink on Hope Gold | 7.4:1 | AAA. CTA buttons |
| White on Signal Red | 6.2:1 | AA. Error banners |
| Silver on Navy | 5.9:1 | AA. Small text on navy panels |
| Hope Gold on Navy | 5.7:1 | AA. Statistics, eyebrows on navy |
| Horizon Blue on White | 5.5:1 | AA. Statistic figures on light grounds |
| Harvest Gold on White | 4.2:1 | **AA large only.** Fine at the built 16 px bold eyebrow; do not use below 14 px bold |
| Slate on White | 3.9:1 | **Fails AA for body text.** Captions only; body copy is Ink (decision log Q6) |
| Cotton Gold on Navy | 3.0:1 | Large only. The mark, plaques, display type |
| Harvest Gold on Navy | 3.0:1 | **Fails.** Use Hope Gold on navy instead |
| Horizon Blue on Navy | 2.2:1 | **Fails.** The old hero eyebrow as built; switch to Hope Gold or white (decision log Q6) |
| Hope Gold on White | 2.2:1 | **Fails as text.** As a button fill with Ink text it is fine |

## Proportions

Think in thirds on a light page: roughly 70% white and Mist, 20% navy (headings, buttons, one dark band per screen), 10% gold (one eyebrow, one call to action, the mark). On a navy panel: 80% navy, 15% white type, 5% gold. Gold is an accent even when it is the whole button. A page that is mostly navy or mostly gold is not this brand.

## Tints and shades

- Navy at 72% opacity over photography is the hero overlay (`--cf-overlay-hero`). Navy at 60% and 80% may be used for screen UI states (hover, pressed) only.
- No gold tints. If a lighter warm tone is needed, use Mist or Cloud, not a pale gold.
- Hover states: Navy buttons darken to `#0F2647`; Hope Gold buttons darken to `#C89400`. These two hover values are the only permitted derived colors.

## Application-specific color

| Application | Specification |
|---|---|
| Embroidery thread | Match Foundation Navy to Pantone 534 C and Cotton Gold to 7557 C from physical thread cards; low-sheen polyester. The mark's stems need a minimum 30 mm width; sew out before ordering |
| Signage (Taylor's Place) | The gate sign is gold on a navy/black field: cut or printed Cotton Gold on Foundation Navy. Match the existing sign in the field before specifying new pieces |
| Vehicle decals | White on dark vehicles (as built on the Taylor's Place truck); full color on white vehicles. Matte or satin films |
| Print | Navy and gold as spot colors when the budget allows (534 C, 7557 C); otherwise CMYK from the starting values above, proofed |
| Apparel | Garment colors navy, white, heather gray; the mark in white on navy, full color or navy on white |

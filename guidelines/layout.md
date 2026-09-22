# Layout

How the pieces sit on a page, screen, or sheet. The old website's structure is sound; this records it and sets the few rules that keep new work consistent with it.

## The grid (web)

| Value | Desktop | Mobile |
|---|---|---|
| Container | 1440 px max (Elementor boxed), content column **980 px** as measured | 100% minus gutters |
| Text measure | 720 px max | 100% |
| Gutter | 24 px | 16 px |
| Columns | 12, 24 px gap; sections use 2 (50/50 or 48/52 split media), 3 (statistics), or 4 (footer, statistics) | 1, stacked in reading order |
| Section padding | 80 px (100 px for heroes and the impact band) | 48 px |
| Gap between grid items | 64 px (media splits), 24 px (cards) | 32 px / 16 px |

The 980 px content width is narrower than the 1440 px container on purpose: the site reads like a document, not a dashboard. Full-bleed elements (hero photos, the CTA band, the footer) run edge to edge; everything else sits in the 980 px column.

## Page rhythm

A page is a sequence of sections, each one opened by the eyebrow + heading + copy trio (`components.md` §3), alternating between:

1. **White** sections with photography or cards,
2. **Mist** sections for lower-emphasis content (the "Who We Are" band, sponsor rows),
3. **Navy** panels or bands for impact, calls to action, and forms.

Never two navy sections in a row. Never more than one impact band per page. A call-to-action band comes before the footer on every page that has a donation goal.

Suggested home page order (the old site's rhythm, with the Foundation's own content): hero → who we are (Mist) → Taylor's Place cards (the lodge, the music hall) → impact band → split media (the Taylor's Place video) → sponsors → CTA band → social feed → footer. Interior pages: breadcrumb → split hero → content sections → sponsors → contact form → footer.

## Alignment

- Centered: full-width section openers, cards' text, statistics, forms' submit button, the hero.
- Left: split sections, breadcrumbs, the footer columns.
- Right: buttons in the CTA band, header actions.
- Text is never justified. Headings never exceed two lines on desktop, three on mobile; shorten the sentence before shrinking the type.

## Radius and shadow

One radius family: **24 px** for cards, panels, and photographs; **8 px** for buttons; **4 px** for fields. Pills, sharp corners, and mixed radii within one section are not this brand. One shadow: `0 2px 4px rgba(0,0,0,.10)` on cards; nothing else casts a shadow.

## Photography in layout

Photographs are the warmth of the page and take at least a third of any screen. They are rounded to 24 px when they sit in the column and square when they run full bleed. Under white type they always carry the navy overlay. See `imagery.md`.

## Print

- Letter (8.5 × 11 in) and A4 with a **0.75 in / 19 mm** margin; a 12-column grid with 4 mm gutters.
- The lockup at the top left of the first page at 60 mm wide; page numbers and the legal name at the foot in PT Sans 8 pt.
- Section openers use the same trio: eyebrow (7.5–8 pt caps, Harvest Gold), heading (Cormorant Garamond 600–700, 24–36 pt, Navy), body (PT Sans 10–11 pt, Ink).
- Navy panels with white type carry statistics and pull quotes; keep them to one per spread.
- The Taylor's Place sponsorship catalog and any sponsorship deck follow the same rules at landscape 16:9.

## Presentation (16:9)

Title slide: navy field, white lockup, title in Cormorant Garamond 700 white, eyebrow in Hope Gold. Content slides: white, lockup small at the top left, eyebrow + heading + body in the web sizes scaled (eyebrow 14 pt, heading 32 pt, body 16 pt). Statistics slides reuse the impact band. Photographs full bleed with the overlay when type sits on them.

## Email

Single column, 600 px. Header: the full-color lockup on white, 180 px wide. Sections follow the web trio at web sizes. One gold CTA per email. Footer: navy, white lockup at 140 px, address and unsubscribe in PT Sans 13 px Silver.

## Social

Square (1:1) and portrait (4:5) posts: photograph with the navy overlay in the lower third carrying a short line in Cormorant Garamond 700 white and the white mark at the corner (8% of the width, inside the 25% clear space). Stories (9:16): the same, with the eyebrow in Hope Gold. The avatar is the full-color mark on white. Details in `applications/social.md`.

## Signage and environment

Taylor's Place: the gate sign sets the register (gold on navy, serif capitals, a sans line, the Foundation endorsement). Wayfinding and building signs follow it: navy panels, gold or white lettering, letter heights per `typography.md`. The Foundation mark is cut, cast, or routed; it is never a printed sticker on a permanent sign. See `applications/signage.md`.

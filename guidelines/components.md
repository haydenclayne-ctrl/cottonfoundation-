# Components

The web patterns that make the Foundation's site look the way it does, measured from the old cottonfoundation.org on 2026-09-22 and written down so the new site (and every template after it) starts from the same parts. Values are in `tokens/cotton-foundation.css`; this document says what each part is for and what the design phase should keep, fix, or add. Content examples are Taylor's Place content; the old site's copy is not carried forward.

## 1. Header

- White bar, 112 px tall (72 px mobile), no shadow as built (a soft `--cf-shadow-header` is recommended once it becomes sticky).
- Left: the full-color horizontal lockup, mark 48–56 px high.
- Center-right: navigation in PT Sans 600, 15 px, uppercase, 1 px tracking, Ink. Suggested items for the new site: About · Taylor's Place · Support Us · CrawFest · Contact.
- Right: a search icon (optional), a phone number with a phone icon in PT Sans 700 (if the owner supplies one, Q11), and the **Donate Now** button (heart icon + label) in the navy button style.
- On the home hero the header sits transparent over the photo with white type and the white Donate button; it turns white with navy type once the page scrolls. Keep this behavior.

## 2. Hero

- Full-bleed photograph (the ranch, the lodge, the gate, families on the land) under the navy overlay `rgba(23,52,94,0.72)`. The overlay is what keeps the photography in the palette; never a bare photo behind white type.
- Optional: the white lockup centered above the headline (home page).
- Eyebrow in caps (as built Horizon Blue; recommended Hope Gold or white), then the H1 in Cormorant Garamond 700, 64 px, white, then one or two lines of PT Sans 16 px white, then one or two buttons.
- Two-button pattern: a **Hope Gold** primary ("Learn more about Taylor's Place") and a **white outline** secondary ("Support us"). The flagship always gets the gold button.
- Interior pages use a split hero instead: eyebrow + H1 + copy + one navy button at left, a rounded (24 px) photograph at right, on white, with a breadcrumb above.

## 3. Eyebrow + heading + copy (the section opener)

Every content section opens the same way and this rhythm is the brand's layout signature:

```
EYEBROW LABEL                     PT Sans 700 · 16 px (13–14 recommended) · caps · Harvest Gold
Section Heading                   Cormorant Garamond 700 · 40–48 px · Navy
One or two sentences of copy.     PT Sans 400 · 16 px · Ink · max 720 px
[ BUTTON ]                        optional
```

Centered for full-width sections ("Our Mission", "Stronger Together", "We'd love to hear you!"); left-aligned in two-column sections ("Who We Are", "A Place of Hope", "Construction Progress"). Vertical gaps: eyebrow to heading 8–12 px, heading to copy 12–16 px, copy to button 24–32 px.

## 4. Buttons

| Style | Fill | Text | Border | Use |
|---|---|---|---|---|
| **Primary (navy)** | Foundation Navy | White | none | Default action: Learn More, Donate Now (header), See Sponsorship Opportunities |
| **CTA (gold)** | Hope Gold | Ink | none | The one action you most want taken on the page: Taylor's Place, footer Donate Now, form Submit |
| **Outline (light)** | transparent | White | 2 px White | Secondary action on navy or photography |
| **Outline (dark)** | transparent | Navy | 2 px Navy | Secondary action on white |
| **Header Donate (on hero)** | White | Ink | none | The Donate Now button while the header is transparent |

All buttons: PT Sans 700, 16 px, uppercase, padding 12 × 24 px, radius 8 px, no tracking, no shadow. Icons (the heart) sit left of the label at text size with an 8 px gap. Hover: navy darkens to `#0F2647`, gold to `#C89400`, outlines fill with their border color. Buttons are never all-gold-with-white-text (fails contrast) and never rounded to a pill.

## 5. Cards

- White, radius 24 px, shadow `0 2px 4px rgba(0,0,0,.10)`; a 1 px Silver hairline is acceptable in place of the shadow on Mist.
- Image on top, edge to edge, cropped 16:9 or 3:2, corners follow the card.
- Body padding 24–32 px: H3 32 px Cormorant Garamond, centered; two lines of PT Sans 16 px; a navy button.
- Grid: two cards side by side (for example "Phase 1: The Lodge" and "Phase 2: The Music Hall"), gap 24 px; three or four on sponsor or story grids. Cards never carry eyebrows; the section above them does.

## 6. Impact band (the navy panel)

The most distinctive component on the old site. A full-content-width navy panel, radius 24 px, padding 64–80 px, with:

- A hero statistic: Cormorant Garamond 700 at 120 px in Hope Gold (for example "30") with its unit ("ACRES") in PT Sans 400 at 32 px white beside it, a 1 px Silver vertical rule, and a two-line caps label in PT Sans 700 white ("OF RESPITE AND MEMORIES / WEST OF KATY, TEXAS").
- A centered paragraph in PT Sans 16 px white, max 720 px.
- A row of three or four statistics: figure in Cormorant Garamond 700, 40–56 px, Hope Gold; label in PT Sans 700, 13–15 px, caps, white, two lines maximum. Figures are placeholders until the owner confirms them (Q8).
- The white mark as a watermark at about 10% opacity, large, cropped by the panel's right edge.

Use one impact band per page at most.

## 7. Split media section

Photograph or video (radius 24 px, with a Hope Gold play button on video) on one side; eyebrow + heading + copy + button on the other; 64 px gap; alternate sides down the page. The photograph column is about 48% of the content width. The Taylor's Place update video ("What's Happening at Taylor's Place") is the reference.

## 8. Statistic list

The inline pattern: a figure in Cormorant Garamond 700, 32 px, **Horizon Blue** (on white), followed on the same line by a PT Sans 700 caps label in Ink (for example 30 ACRES WEST OF KATY · 2 PHASES · 1 MAIN LODGE). Three to four rows, 12 px apart. Blue figures on white; gold figures on navy; never gold figures on white.

## 9. Sponsor logo row

Eyebrow OUR PARTNERS or OUR SPONSORS, heading "Stronger Together", then a carousel or grid of sponsor logos in their own colors on white, three or four visible, 64 px gap, arrows at the sides in Ink, dot pagination in Navy. Sponsor logos are the only place foreign colors appear on the page; keep them grayscale if the row gets noisy (design phase to decide). The Foundation lockup never sits in the row.

## 10. CTA band

Full-bleed photograph (the ranch aerial) under the navy overlay; eyebrow (white or Hope Gold) + H2 in white at left; two stacked buttons at right (white Donate Now with the heart, then a white outline "Questions? Contact us."). Height about 220 px on desktop.

## 11. Forms

- On a navy panel (radius 24 px, padding 48 px) as built on the contact sections, or on white for interior forms.
- Labels: PT Sans 700, 15 px, white (on navy) with "(required)" in 12 px Silver. Fields: white fill, radius 4 px, height 40 px, no visible border on navy; 1 px Silver border on white. Textarea 100 px.
- Submit: the gold CTA button, centered.
- Error text and borders: Signal Red. Success: navy text on Mist.

## 12. Footer

Navy, padding 80 px top, 40 px bottom. Four columns: the white lockup, alone, over an eyebrow OUR MISSION (white) and the mission sentence, then the gold Donate Now button; HELPFUL LINKS (white caps eyebrow, PT Sans 400 15 px white links); CONTACT (icon + text rows, details per Q11); social icons in 40 px circles with a 1 px Harvest Gold ring, white glyphs. A 1 px Silver rule at 20% opacity, then the legal line (© Cotton Foundation, the year) at left and policy links (Gift Acceptance Policy · Refund Policy · Terms of Use · Sitemap · Back to top) at right, PT Sans 400 15 px white. No other logo appears in the footer.

## 13. Breadcrumb

Interior pages: "Home > Taylor's Place" in PT Sans 400 13 px, Slate, current page in Ink, under the header at the content left edge.

## 14. Social embed and blog cards

The Instagram feed block (avatar = the full-color mark on white, handle, follow button in navy) and blog cards (image, H3, date in Slate, excerpt) follow the card rules. Post images should be shot or cropped in the imagery rules (`imagery.md`).

## What the design phase should change

1. Eyebrow size and color on dark grounds (contrast).
2. Heading line height 1.5 → 1.2.
3. Body text Slate → Ink everywhere.
4. A sticky header treatment with the recommended shadow.
5. A compact lockup for the mobile header (the horizontal lockup at 160 px is below minimum).
6. A Taylor's Place page hero that uses the Taylor's Place mark (once digitized) with the Foundation endorsement.
7. One donation-flow style so the hand-off from the site to the donation platform (whichever the owner chooses, Q11) is not a visual break.

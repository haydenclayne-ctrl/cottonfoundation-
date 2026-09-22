# Brief: The New Website

**Subject:** the phase after this design system. cottonfoundation.org (the old site) is replaced by a site built from `tokens/cotton-foundation.css`, the components in `guidelines/components.md`, and the assets in `assets/`, with Taylor's Place at its center. This brief is written now so the design system is built with the site in view; the site itself is not started until the design system is approved.

## What the site is for

1. Tell the Taylor's Place story and show the place (photography, the phases, progress).
2. Take donations and sponsorships for Taylor's Place, without a visual break at the payment step.
3. Explain the Foundation in its own words (mission, the namesake, the people) — nothing about any other organization.
4. Host CrawFest information and tickets (if the event continues, Q9).
5. Give contact and press information.

## Pages

Home · Taylor's Place · About · Support Us (donate, sponsor, named gifts) · CrawFest · News or Blog · Contact · Gift Acceptance Policy · Refund Policy · Terms of Use · Privacy Policy.

## Design requirements (all from the guidelines)

- Header: white, full-color lockup left, nav in PT Sans caps, Donate Now navy button right; transparent over the home hero; compact lockup on mobile.
- Home hero: Taylor's Place photograph under the navy overlay, the white lockup, eyebrow in Hope Gold, H1, gold Taylor's Place button and outline Support button.
- Sections in the eyebrow + heading + copy rhythm; white / Mist / navy alternation; one impact band with confirmed figures only; a CTA band before the footer.
- Taylor's Place page: the digitized Taylor's Place mark with endorsement in the hero; the story, the phases as cards, construction progress, the sponsorship catalog, the video.
- Footer: navy, the white lockup alone, mission sentence, gold Donate, links, contact (Q11), social, legal line with the confirmed legal name.
- Type: Cormorant Garamond 700 headings at line height 1.2, PT Sans 16 px Ink body; eyebrows 13–14 px.
- Accessibility WCAG 2.2 AA; performance budget in `applications/digital.md`.

## Content requirements

- All copy in the voice (`brand/voice-and-tone.md`), written fresh for the Foundation and Taylor's Place; old-site copy is not reused except the Taylor's Place and Tom Wallace passages quoted in `brand/brand-story.md`, and only after the owner confirms them.
- No statistics, dates, or claims until confirmed (Q2, Q8). Templates ship with placeholders.
- Photography from `assets/photography/` once it exists; renderings labeled as renderings until the lodge is photographed.

## Technical notes (for the build, later)

- Static or lightly dynamic site; the design tokens as the single stylesheet source; the SVG marks inline; fonts self-hosted.
- Donation platform integration per `applications/digital.md`; forms with Signal Red error states and navy focus rings.
- Domain and hosting: owner's decision; the old site stays up until the new one is live, then redirects.

## Output

Not started. When the design system is approved, this brief becomes the website project's starting document.

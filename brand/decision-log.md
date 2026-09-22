# Decision Log

Dated record of brand decisions and open questions. Newest first. Every move of an asset from `concepts/` to `assets/`, every palette or type change, and every naming decision is recorded here.

## Open questions for the owner

| # | Question | Why it matters | Default until answered |
|---|---|---|---|
| Q1 | Do the original vector files exist for the Cotton Foundation mark and lockup (AI / EPS / PDF) and for the Taylor's Place sign artwork (the sign shop's cut file)? Who has them? | The repository's SVGs are auto-traced from PNGs. Masters would replace them, identify the wordmark face, and give the Taylor's Place mark exact proportions | Traced SVGs are the working vectors; Taylor's Place is digitized from photographs in the design phase |
| Q2 | Confirm the mission statement wording, the legal name (The Cotton Charitable Foundation), and whether any founding date is to be used | The old site's mission and history language is not carried forward; the new site needs approved sentences | Working mission in `brand-story.md`; no "since" or "Est." date anywhere |
| Q3 | What is the typeface of the COTTON / FOUNDATION wordmark? (Outlines only in the supplied files.) Is it Cormorant Garamond? | Needed to set the Taylor's Place wordmark and any future descriptor identically | Treat as a Garamond-class serif; the design phase matches it visually, using Cormorant Garamond if it fits |
| Q4 | Are "Restoring Hope" (Foundation) and "Creating Memories" (Taylor's Place) official taglines? | Whether they may be locked up with the marks and used on apparel and signage | Both are working taglines in copy and on existing signage; neither is added to a lockup |
| Q5 | One sans or two: keep PT Sans (what the built site renders) or move to DM Sans (what the site's kit declares)? | Every UI element | PT Sans |
| Q6 | Accept the four contrast fixes: body text Ink not Slate; eyebrows on navy in Hope Gold or white not Horizon Blue; Harvest Gold text never below 14 px bold; no gold text on white | Accessibility of the new site | Applied in tokens as recommendations; the as-built values remain documented |
| Q7 | Keep three golds (Cotton, Harvest, Hope) with fixed roles, or consolidate Harvest and Hope into one UI gold? | Palette discipline; print cost | Three golds with fixed roles |
| Q8 | Which of the old site's photographs and statistics belong to the Foundation and Taylor's Place and may be reused? Who holds the originals and the releases (the Tom Wallace family photographs, the Taylor's Place shoots, the CrawFest images)? | The `assets/photography/` library; consent for families and children; no figure is hard-coded until confirmed | Nothing added; templates use placeholders |
| Q9 | Does CrawFest continue as the Foundation's annual fundraiser for Taylor's Place, under that name, and where? | The edition tier, event templates, the "Benefiting Taylor's Place" line | Kept in the architecture as the annual event; no venue or date stated |
| Q10 | CrawFest or Crawfest? The old site used both | Event materials, hashtags | CrawFest |
| Q11 | Contact details for the new site: address, phone, email, donation platform | Footer, contact page, print | Left blank in templates; the old site's details are not reused |
| Q12 | Confirm the independence reading in `brand-architecture.md`: no co-branding, no references to any other organization's name, history, marks, or lines of work | Governs every piece of copy and every footer | As documented |

## Decisions

### 2026-09-22 — Independence

- **D11.** By the owner's instruction, Cotton Foundation and Taylor's Place are documented as fully independent. This repository contains no references to any other company or organization, no co-brand lockups, no corporate history or "since" dates, and no program or copy about lines of work other than Taylor's Place. Old-site copy and files outside that scope are neither quoted nor catalogued by name. Earlier drafts of this repository that carried such references were rewritten before the first commit.
- **D12.** The Foundation's palette name for `#BD202E` is **Signal Red** (form errors and alerts only).

### 2026-09-22 — Repository established

- **D1.** Repository `cotton-foundation-design` created as the single source of truth for the Cotton Foundation brand and design system, structured to be handed to Claude Design for the creative phase and then to the website build.
- **D2.** Brand architecture fixed: Cotton Foundation is the organization and master brand; **Taylor's Place is its flagship property, owned and operated by the Foundation, endorsed by the Foundation lockup wherever its mark appears;** CrawFest is an annual edition benefiting Taylor's Place (continuation pending Q9). Nothing else carries a mark.
- **D3.** Canonical Foundation Navy set to **`#17345E`**, the value declared in the old site's Elementor kit and used for every heading and button. The supplied logo PNGs measure `#16345E` (export rounding); the derived vectors are written at the canonical value. Cotton Gold set to **`#9F762B`**, the exact fill of the boll in the logo files. Harvest Gold `#A07400`, Hope Gold `#E0A600`, Horizon Blue `#3E6B9C`, Signal Red `#BD202E`, Ink `#17212E`, Slate `#808285`, Silver `#B1B1C2`, Cloud `#F3F3F3` taken from the kit; Mist `#F5F8FA` measured from the built page. No additions without a log entry.
- **D4.** Typography fixed to what the site renders: Cormorant Garamond 700 for display, PT Sans 400/700 for everything else; DM Sans held as provisional (Q5). Eyebrow caps recognized as the brand's signature typographic device.
- **D5.** The only marks in the system are the 2026 cotton-boll mark, its horizontal lockup, and the Taylor's Place mark as built. Any earlier logo files in the old site's media library are not part of this identity and were not brought into the repository (owner's instruction: Cotton Foundation and Taylor's Place assets only, no other logos).
- **D6.** Seven files downloaded from cottonfoundation.org are catalogued with checksums in `assets/originals/` and declared immutable. Working assets derived by script (`tools/derive_from_originals.py`): the mark in five colorways and the horizontal lockup in four, as PNG and auto-traced SVG, plus previews; the Taylor's Place gate-sign and truck-decal photograph crops as references.
- **D7.** The SVGs are classified **working vectors (traced), provisional** until the owner supplies master artwork (Q1). They are not hand-edited; they are regenerated from the originals.
- **D8.** The Taylor's Place mark as built on the gate sign and truck (roofline, TAYLOR'S PLACE, CREATING MEMORIES, Foundation endorsement) is recognized as the property's existing identity. The design phase digitizes it faithfully; it does not redesign it.
- **D9.** Asset naming convention set: `cf-<asset>[_<variant>]_<colorway>.<ext>` for the Foundation, `tp-` for Taylor's Place, `crawfest-` for the event.
- **D10.** Website design measurements (colors, type, spacing, components) recorded as the baseline for the new site (`references/website-audit.md`, `guidelines/components.md`), with the recommended changes listed at the end of `components.md`, all pending Q6 or the design phase.

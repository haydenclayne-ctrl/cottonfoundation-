# Cotton Foundation — Brand & Design System

**The single source of truth for the Cotton Foundation identity, and for Taylor's Place, the respite sanctuary the Foundation owns and operates.**

Cotton Foundation is an independent 501(c)(3) restoring hope to children and families facing life-altering illness. Its flagship is **Taylor's Place**: thirty acres west of Katy, Texas, with a lodge, a pond, a pool, and (in Phase 2) a music hall, courts, and a playground, where a family with a terminally ill member can rest, reconnect, and create lasting memories. **CrawFest**, the Foundation's annual crawfish fundraiser, benefits Taylor's Place.

This repository was built on 2026-09-22 from two sources: the Foundation's existing logo files and the *design* of its previous website, cottonfoundation.org (colors, type, spacing, components, measured from the live site), and the Taylor's Place mark as built on the property's gate sign. It is the starting point for the creative phase in Claude Design and, after that, for the new website.

> **If you are an AI design system or a designer new to this brand, start with [`CLAUDE.md`](CLAUDE.md).** It is the creative brain of the brand and tells you what to read next.

---

## What is in this repository

| Directory | What it holds | Status |
|---|---|---|
| [`CLAUDE.md`](CLAUDE.md) | The brand brief for AI and human designers. Read first | Complete |
| [`brand/`](brand/) | Architecture (independence; Foundation → Taylor's Place → CrawFest), story, principles, design principles, voice, decision log | Complete |
| [`guidelines/`](guidelines/) | Colors, typography, logos, sub-brands, web components, layout, imagery, iconography, usage rules | Complete (v1) |
| [`tokens/`](tokens/) | Machine-readable values: design-tokens JSON and CSS custom properties with the base component classes | Complete (v1) |
| [`assets/`](assets/) | `originals/` (the supplied files, immutable, checksummed), `marks/` and `logos/` (working PNG + SVG in every colorway, with previews), Taylor's Place references, reserved `icons/` and `photography/` | Marks and lockup available; Taylor's Place to be digitized |
| [`references/`](references/) | The website audit (every measured value) and screenshots of the old site's layout | Complete |
| [`applications/`](applications/) | Specifications for digital, print, signage, events, apparel, social | Complete (v1 specs, no artwork yet) |
| [`concepts/`](concepts/) | Design briefs for the master brand, Taylor's Place, CrawFest, and the new website. Nothing here is approved | Briefs written; no explorations yet |
| [`handoff/`](handoff/) | The brief and checklist for the Claude Design creative phase | Complete |
| [`tools/`](tools/) | The derivation script (originals → working assets, with tracing) and the contrast checker | Complete |

## The identity in one paragraph

The **mark** is an open cotton boll in Cotton Gold (`#9F762B`) held by two open hands in Foundation Navy (`#17345E`). The **horizontal lockup** sets COTTON over a letterspaced FOUNDATION beside it in a Garamond-class serif; it is the primary logo and it always appears alone. **Taylor's Place** has its own mark, as built on its gate: a roofline over TAYLOR'S PLACE, CREATING MEMORIES beneath, and the Foundation lockup as its endorsement. The palette is navy and gold on white with three golds in fixed roles; the type is Cormorant Garamond for warmth and PT Sans for everything practical; the layout signature is a small gold eyebrow label above every heading, 24 px corners, and photographs under a navy overlay.

## Brand architecture in one glance

```
COTTON FOUNDATION            the organization · the mark + wordmark · "Restoring Hope"
└─ TAYLOR'S PLACE            flagship property, owned and operated by the Foundation
│    roofline mark · "Creating Memories" · always endorsed COTTON FOUNDATION
└─ CRAWFEST                  annual event · benefits Taylor's Place · Foundation lockup always present
```

One organization, one mark, one type system, one palette. See [`brand/brand-architecture.md`](brand/brand-architecture.md) and [`guidelines/sub-brands.md`](guidelines/sub-brands.md).

## Governing rules (the short version)

1. **Cotton Foundation stands alone.** No other organization's name, history, mark, or colors appear anywhere in this identity. No co-brand lockups, no "since" dates.
2. **Never overwrite or edit anything in `assets/originals/`.** Derive, never replace.
3. **The mark and the horizontal lockup are fixed.** Do not redraw, recolor within, extract parts, or restyle them.
4. **Taylor's Place is the Foundation's.** Its mark is digitized faithfully from the gate sign and is always endorsed by the Foundation lockup.
5. **Navy and gold on white.** Three golds, each with one job. Never add a color.
6. **Two typefaces.** Cormorant Garamond and PT Sans.
7. **Build the system, not new logos.** Programs are descriptors; events are editions.
8. **Do not invent brand facts.** Founding dates, statistics, contact details, and taglines are open questions in [`brand/decision-log.md`](brand/decision-log.md) until the owner answers them.

## The test for any new work

> Would a family arriving at the Taylor's Place gate, a volunteer setting up CrawFest, and a donor reading the annual letter all recognize the same organization, and would each of them feel respected by how it looks?

If not, reject the direction.

## Working in this repository

- Markdown first. Kebab-case file and folder names. Dated files use a `YYYY-MM-DD-` prefix.
- Asset naming: `cf-<asset>[_<variant>]_<colorway>.<ext>` for the Foundation, `tp-` for Taylor's Place (see [`assets/README.md`](assets/README.md)).
- Every approved mark ships as SVG (and PDF once produced) plus PNG and previews.
- Explorations go in `concepts/`. Approved work moves to `assets/` only with owner sign-off, recorded in [`brand/decision-log.md`](brand/decision-log.md).
- Retired assets move to `archive/` (created when first needed). Nothing is deleted.
- `python3 tools/derive_from_originals.py` regenerates every working asset from the originals; `python3 tools/contrast_check.py` checks the palette.

## Status and next step

The design system repository is complete: documentation, tokens, the existing assets in every colorway, the Taylor's Place references, and the briefs. The next step is the creative phase: hand this repository to Claude Design with [`handoff/CLAUDE-DESIGN-BRIEF.md`](handoff/CLAUDE-DESIGN-BRIEF.md). After that phase is approved, the new website is built from it ([`concepts/website/BRIEF.md`](concepts/website/BRIEF.md)).

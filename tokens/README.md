# tokens/

Machine-readable brand values for the new website, email templates, documents, and AI design tools. These mirror `guidelines/colors.md`, `guidelines/typography.md`, and `guidelines/components.md`; the guidelines are the human source of truth and the tokens must be updated in the same change when a guideline value changes.

| File | Format | Use |
|---|---|---|
| `cotton-foundation.tokens.json` | Design-tokens JSON (W3C community-group style: `$value`, `$type`, `$description`) | Import into Figma token plugins, Style Dictionary, Claude Design, or any build |
| `cotton-foundation.css` | CSS custom properties plus the base component classes | Drop into any web project; the new site should start from this file |

## Where the values came from

Every value was read from the live cottonfoundation.org on 2026-09-22 (the Elementor kit's global colors and typography, computed styles of the built pages) or measured from the supplied logo files. `references/website-audit.md` records the readings. Nothing here was invented; where the audit found a value that should change (a contrast failure, a loose line height), the token carries the as-built value and its `$description` says what the design phase should decide. Those items are listed in `brand/decision-log.md`.

## Fonts

All three faces are open source (SIL Open Font License) and served by Google Fonts:

| Role | Face | Weights in use | Source |
|---|---|---|---|
| Display | Cormorant Garamond | 700 (300–700 loaded) | https://fonts.google.com/specimen/Cormorant+Garamond |
| Sans | PT Sans | 400, 700 | https://fonts.google.com/specimen/PT+Sans |
| Sans (provisional) | DM Sans | 400 (100–900 loaded) | https://fonts.google.com/specimen/DM+Sans |

No font binaries are committed. If the design phase adds a commercial face (for example a licensed Garamond for print), record here: face, foundry, license type (desktop / web / embroidery), license holder, purchase date, and where the files live.

## Checking

`python3 tools/contrast_check.py` prints WCAG contrast ratios for the color pairs the guidelines allow. Run it after any palette change.

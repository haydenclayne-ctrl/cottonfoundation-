# assets/

Brand artwork, in three strictly separated states.

| Directory | State | Rule |
|---|---|---|
| `originals/` | **Supplied.** Files exactly as downloaded from cottonfoundation.org on 2026-09-22 (and, later, anything the owner supplies) | Immutable. Never edit, rename, re-save, or delete. Catalogued with checksums in `originals/INVENTORY.md` |
| `marks/`, `logos/` | **Approved working files.** Derived from the originals by `tools/derive_from_originals.py`, or produced in the design phase and signed off by the owner | PNG working rasters and SVG vectors for every colorway; previews in `preview/`. Every addition is recorded in `brand/decision-log.md` |
| `icons/`, `photography/` | **Reserved.** README only until the first approved asset lands | Created in the design phase |
| `../concepts/` | **Exploration.** Anything not yet approved | Lives outside `assets/`. See `concepts/README.md` |

Retired approved assets move to `../archive/` (created on first use) with a decision-log entry. Nothing is deleted.

## What exists now

| Directory | Contents | Status |
|---|---|---|
| `originals/cottonfoundation-org-2026-09-22/` | 5 logo PNGs, 2 reference photographs | Catalogued, immutable |
| `marks/` | The cotton-boll mark: full color, white, navy, gold, black; PNG 2000 px + SVG; 5 previews | Approved (as supplied; vectors traced, see below) |
| `logos/cotton-foundation/` | The horizontal lockup: full color, white, navy, black; PNG 4000 px + SVG; 4 previews | Approved (as supplied; vectors traced) |
| `logos/taylors-place/` | README and two reference photograph crops of the mark as built | Reference only; the mark is to be digitized in the design phase |
| `icons/`, `photography/` | README only | Reserved |

## Vector status

cottonfoundation.org serves PNG only, and the designer's master files were not available on 2026-09-22 (decision log Q1). The SVGs here were **auto-traced** from the 6000 px lockup and 8334 px mark originals with VTracer (spline mode, filter speckle 8, corner threshold 60). At the resolutions the originals provide, the traced curves match the raster to well under a pixel of the working PNGs, they scale without limit, and they recolor cleanly. They are still fitted curves, not drawn ones: treat them as **working vectors**. When master artwork arrives, it replaces them (and the derivation script is retired for those files). Do not hand-edit the traced paths; regenerate them.

## Naming convention

```
<prefix>-<asset>[_<variant>]_<colorway>.<ext>
```

- `prefix`: `cf` (Cotton Foundation), `tp` (Taylor's Place), `crawfest` (the event)
- `asset`: `mark`, `lockup`, `wordmark`, `descriptor`, `icon-<name>`
- `variant` (optional): `horizontal`, `stacked`, `compact`, `endorsed`, `embroidery`, `small`
- `colorway`: `full-color`, `white`, `navy`, `gold`, `black`, `tone-on-tone`
- `ext`: `svg`, `pdf`, `ai`, `eps`, `png`, `dst`, `pes`

Examples: `cf-mark_white.svg`, `cf-lockup_horizontal_full-color.png`, `tp-mark_endorsed_gold.svg`, `cf-descriptor_stacked_navy.pdf`.

Previews are `<name>_<ground>_preview.png` in a `preview/` subfolder (for example `cf-mark_white_on-navy_preview.png`). Kebab-case throughout; no spaces.

## Export set for every approved mark

- SVG (single `<g>` per color, no embedded raster, viewBox set)
- PDF (vector; to be added in the design phase, the tracing pipeline does not produce PDF)
- PNG at 2000 px (marks) or 4000 px (lockups) wide, transparent
- PNG previews on white and on navy
- For embroidery and cut vinyl: the simplified cut as SVG, after a sew-out or cut test

## Derivation

`python3 tools/derive_from_originals.py` regenerates `marks/`, `logos/cotton-foundation/`, and the Taylor's Place reference crops. It reads the originals, never writes to them, and verifies their checksums first. `--skip-svg` skips the tracing step (about 45 s).

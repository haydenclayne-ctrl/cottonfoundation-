# Logos: the Cotton Foundation mark and lockup

The Cotton Foundation identity has two fixed pieces: the **mark** (a cotton boll held in two open hands) and the **horizontal lockup** (the mark beside the COTTON / FOUNDATION wordmark). Both exist; both are used on the current website, the Taylor's Place gate sign (as the endorsement), and the property's truck decals. Neither is to be redrawn.

## Anatomy

**The mark.**
- **The boll.** An open cotton boll seen from above, drawn as a rounded, four-lobed silhouette with a jagged outer edge, three inner bracts that form a bird-like or flame-like negative shape, and a short stem at the bottom. It is one solid fill: **Cotton Gold `#9F762B`**.
- **The hands.** Two open hands, palms up, cradling the boll from below, fingers spread. One solid fill: **Foundation Navy `#17345E`**. The hands do not touch the boll; the stem hangs into the space between them.
- **What it says.** Care, giving, harvest, the Foundation's name. It is the one image of the brand.
- **Proportions:** essentially square, 1.004 : 1 (8251 × 8219 px in the 8334 px original).

**The wordmark.**
- "COTTON" in a Garamond-class serif, capitals, cap height about 275 units where the mark is 1000 wide, letterspaced about 21% of cap height.
- "FOUNDATION" beneath it, same serif, capitals at 121 units cap height, tracked out (gaps of about 80% of cap height) to the exact width of COTTON.
- Both lines Foundation Navy in the full-color lockup; both the same single color in one-color versions. The wordmark is outlines, not live type; the face is unconfirmed (decision log Q3).

**The horizontal lockup, measured** (units: mark width = 1000; see `tokens/`):

| Element | Measurement |
|---|---|
| Mark | 1000 wide × 996 high, at the left edge |
| Gap, mark to wordmark | 156 |
| Wordmark left edge | x = 1156 |
| COTTON | cap top y = 250, baseline y = 537 (extent 286 incl. overshoot) |
| FOUNDATION | cap top y = 668, baseline y = 789, cap height 121 |
| Wordmark width | 1951 (both lines) |
| Overall lockup | 3107 wide × 996 high (ratio 3.118 : 1) |
| Vertical relationship | the wordmark block (y 250–789) is centered on the mark, dropped 21 units for optical balance |

## Approved files

`assets/marks/` (the mark alone) and `assets/logos/cotton-foundation/` (the lockup). Every file exists as PNG (working raster) and SVG (working vector); see "Vector status" below.

| File | Colorway | Use |
|---|---|---|
| `cf-mark_full-color` | Cotton Gold + Foundation Navy | Default on white and light grounds. Favicon, app icon, social avatar (as used on the site's Instagram widget) |
| `cf-mark_white` | White | Navy panels, photography, dark apparel, the impact-band watermark (at 8–12% opacity) |
| `cf-mark_navy` | Foundation Navy | One-color print, forms, embroidery on light garments |
| `cf-mark_gold` | Cotton Gold | Plaques, foil, thread on navy; the Taylor's Place sign register |
| `cf-mark_black` | Black | Utility: engraving, laser, vinyl cut |
| `cf-lockup_horizontal_full-color` | Cotton Gold + Foundation Navy | **The primary logo.** Web header, letterhead, documents, presentations, light signage |
| `cf-lockup_horizontal_white` | White | Footer, navy sections, hero over photography, dark vehicles |
| `cf-lockup_horizontal_navy` | Foundation Navy | One-color print, fax-grade documents, embroidery |
| `cf-lockup_horizontal_black` | Black | Utility |
| `preview/*.png` | — | Previews only, not for production |

All were derived by script (`tools/derive_from_originals.py`) from the files downloaded from cottonfoundation.org on 2026-09-22, catalogued in `assets/originals/INVENTORY.md`. The originals are untouched.

## Vector status

The Foundation's designer files (Illustrator or EPS masters) were **not** available; cottonfoundation.org serves PNG only. The SVGs in `assets/` are auto-traced from the 6000 px and 8334 px PNG originals with VTracer. At any size a website, a printer, or a sign shop will use they are indistinguishable from the raster, and they recolor cleanly, but they are **working vectors, not master artwork**: curves are fitted, not drawn. When the original vector files are supplied (decision log Q1) they replace the traced SVGs and the derivation script is retired for those files. Until then, do not "improve" the traced paths by hand; regenerate them from the originals if anything drifts.

## Formats

| Format | Description | Status |
|---|---|---|
| **Horizontal lockup** | Mark left, two-line wordmark right | Approved (as supplied) |
| **Mark alone** | The boll in hands | Approved (as supplied) |
| **Stacked lockup** | Mark centered above the wordmark | Not supplied. To be built in the design phase from the same parts (`concepts/master-brand/BRIEF.md`) |
| **Compact lockup** | Mark beside a single-line COTTON FOUNDATION for very small widths | Not supplied. Design phase |
| **Wordmark alone** | COTTON / FOUNDATION without the mark | Not approved. The mark is the identity |
| **Co-brand lockups** | The Foundation lockup beside another organization's logo | **Not permitted.** The Foundation lockup stands alone (`brand/brand-architecture.md`, Independence) |

## Clear space

Minimum clear space on all sides = **25% of the mark's width** (about the cap height of COTTON). Nothing enters this zone: no type, no rule, no photo edge, no other logo. On the web header the lockup sits inside a 112 px bar with the mark 48–56 px high, which satisfies the rule.

## Minimum sizes

| Medium | Mark alone | Horizontal lockup | Why |
|---|---|---|---|
| Screen | 24 px wide (favicon 32 px) | 200 px wide | Below 200 px, FOUNDATION falls under 8 px cap height and fills in |
| Print | 8 mm | 40 mm | FOUNDATION cap height reaches 1.6 mm at 40 mm |
| Embroidery | 30 mm (provisional) | 90 mm (provisional) | The boll's inner bracts and the fingers are fine detail; sew out first |
| Vinyl cut | 40 mm | 120 mm | Weeding the bracts below this is impractical |

When the lockup would fall below its minimum, use the mark alone, or (once it exists) the compact lockup.

## Placement logic

- **Web header:** full-color horizontal lockup, left, mark 48–56 px high, on white. The site's header is white with the lockup at the left and "Donate Now" at the right; keep that.
- **Footer and navy panels:** white horizontal lockup, alone.
- **Over photography:** white lockup or white mark, only over the navy overlay (`--cf-overlay-hero`) or a dark, uncluttered area.
- **Favicon, avatar, app icon:** full-color mark on white, or white mark on navy.
- **Watermark:** white mark at 8–12% opacity on navy (as used in the old site's impact band), large, cropped by the panel edge. Never over photography.
- **Endorsement:** beneath the Taylor's Place mark per `sub-brands.md`.
- **Documents:** lockup top-left of a letterhead at 60 mm; mark alone on the back cover or as a section divider.

## Misuse (never)

- Redraw, trace by hand, smooth, thicken, or "clean up" the mark or wordmark. The only artwork is in `assets/`.
- Retype the wordmark in Cormorant Garamond or any font. It is artwork.
- Change the proportions, stretch, squash, rotate, or mirror.
- Change the colors within the mark: no gold hands, no navy boll, no two-tone wordmark.
- Use the full-color lockup on navy, on gold, or on photography.
- Add an outline, drop shadow, glow, bevel, gradient, or metallic effect.
- Place the mark in a circle, box, or shield (the social avatar crop is the one exception: the mark centered on a white or navy disc).
- Put text, a heart, a house, or any other object inside the hands or on the boll.
- Set "Cotton Foundation" next to the mark in any typeface as a substitute for the lockup.
- Place any other organization's logo in a lockup with the mark, or use any logo other than the ones in `assets/` to represent the Foundation.

## Retired and superseded

Nothing in `assets/` is retired. The only marks of the brand are the ones in this repository. Any other logo files that may exist in old materials or in the old website's media library are not part of this identity and are not used for new work (decision D5). When a variant is superseded in the future, move it to `archive/` with a decision-log entry. Never delete.

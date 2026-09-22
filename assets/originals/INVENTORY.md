# Inventory of Supplied Assets

Catalogued 2026-09-22. All seven files were downloaded from the WordPress media library of cottonfoundation.org (the Foundation's previous website) through the owner's browser on that date, at the owner's instruction to pull the Cotton Foundation and Taylor's Place assets and no other logos. Checksums are MD5 of the files exactly as downloaded. If a checksum here ever fails to match the file, the original has been altered and must be restored; `tools/derive_from_originals.py` checks them before every run.

## Summary

| # | File (folder `cottonfoundation-org-2026-09-22/`) | What it is | Classification |
|---|---|---|---|
| 1 | `Cotton-Foundation-2026-01.png` | **The horizontal lockup, full color.** 6000 × 3553 px, palette PNG with alpha. Mark (Cotton Gold boll `#9F762B`, navy hands `#16345E`) + COTTON / FOUNDATION wordmark in navy | **Geometric source of truth for the lockup.** Master for every lockup colorway |
| 2 | `Cotton-Foundation-2026-04.png` | The horizontal lockup in white on the identical 6000 × 3553 canvas (same bounding box as #1) | Supplied white version. Superseded by recoloring #1 (one geometry for all colorways) |
| 3 | `Cotton-Foundation-2026.png` | The horizontal lockup in white, 6000 × 2010 px, larger scale on a tighter canvas. The site's header/footer logo file. Silhouette matches #1 (IoU 0.997) | Supplied white version; superseded by #1 for the same reason |
| 4 | `Cotton-Foundation-2026-Icon.png` | **The mark alone, full color.** 584 × 584 px RGBA. Boll `#9F762B`, hands `#16345E` | Color reference for the mark; the site's favicon source |
| 5 | `Cotton-Foundation-2026-Backgrouond.png` (sic, the site's spelling) | **The mark alone in white**, 8334 × 8334 px RGBA. Used on the site as the impact-band watermark. Same artwork as #4 (IoU 0.989) at 14× the resolution | **Geometric source of truth for the mark** |
| 6 | `HLDS_Taylors-Place-Crawfest_HEADER.png` | Photograph composite, 2000 × 300 px: crawfish at left fading into the Taylor's Place gate with its sign (TAYLOR'S PLACE / CREATING MEMORIES / COTTON FOUNDATION, gold on a dark field) | **Reference for the Taylor's Place mark as built.** Not a logo file |
| 7 | `Taylors-Place-Shoot-April-2025-33.png` | Photograph, 819 × 546 px: two men with plans on the Taylor's Place site; a truck tailgate carries the Taylor's Place mark in white | Reference for the mark's white colorway as applied. Not a logo file |

## Details

### 1. Cotton-Foundation-2026-01.png
- Source URL: `https://cottonfoundation.org/wp-content/uploads/2024/10/Cotton-Foundation-2026-01.png` (WordPress media ID 2817, title "Cotton Foundation"; the site serves a 2560 px "-scaled" copy, this is the full original).
- 6000 × 3553 px, mode P (palette) with transparency. Trimmed artwork 5310 × 1703 px at offset (291, 891). Opaque pixels are two flat colors: `#16345E` (63.8%) and `#9F762B` (36.2%).
- **MD5:** `6cbd761a68ce40a137f0b086fb312428` · 101,316 bytes.

### 2. Cotton-Foundation-2026-04.png
- Source URL: `.../uploads/2025/12/Cotton-Foundation-2026-04.png` (ID 2813).
- 6000 × 3553 px, palette with transparency, all-white artwork on the same bounding box as #1.
- **MD5:** `81c5008e10af47e0059e8b8dd62090b4` · 99,878 bytes.

### 3. Cotton-Foundation-2026.png
- Source URL: `.../uploads/2025/12/Cotton-Foundation-2026.png` (ID 2815). This is the site's header logo (served scaled).
- 6000 × 2010 px, palette with transparency, white; trimmed 5913 × 1896 px.
- **MD5:** `15d0a58969591432af7bc4de88b819bf` · 104,103 bytes.

### 4. Cotton-Foundation-2026-Icon.png
- Source URL: `.../uploads/2024/10/Cotton-Foundation-2026-Icon.png` (ID 2819, title "Cotton Boll"). Also the site icon at 150 and 300 px.
- 584 × 584 px RGBA; trimmed 563 × 561 px. Colors `#9F762B` (53.4%) and `#16345E` (46.6%).
- **MD5:** `e98b0e293792cf23d4c2020cf606c912` · 25,347 bytes.

### 5. Cotton-Foundation-2026-Backgrouond.png
- Source URL: `.../uploads/2025/12/Cotton-Foundation-2026-Backgrouond.png` (ID 2822, title "Cotton Boll").
- 8334 × 8334 px RGBA, white; trimmed 8251 × 8219 px (ratio 1.004 : 1).
- **MD5:** `089925d5da602f13037625576abd72eb` · 706,169 bytes.

### 6. HLDS_Taylors-Place-Crawfest_HEADER.png
- Source URL: `.../uploads/2025/11/HLDS_Taylors-Place-Crawfest_HEADER.png` (ID 2716).
- 2000 × 300 px RGB. The gate sign occupies roughly x 1230–1500, y 40–235.
- **MD5:** `8016f76f0f562f987228e41636e7a025` · 1,138,372 bytes.

### 7. Taylors-Place-Shoot-April-2025-33.png
- Source URL: `.../uploads/2025/11/Taylors-Place-Shoot-April-2025-33.png` (ID 2770).
- 819 × 546 px RGB. The tailgate decal occupies roughly x 640–760, y 195–235.
- **MD5:** `0a12b0f3d0878d6cee5559779fda2173` · 633,820 bytes.

## What was derived from these (and where)

| Derived asset | From | Location |
|---|---|---|
| The mark, five colorways, PNG (2000 px) + SVG (traced) + previews | #5 (geometry), #4 (color split) | `assets/marks/` |
| The horizontal lockup, four colorways, PNG (4000 px) + SVG (traced) + previews | #1 | `assets/logos/cotton-foundation/` |
| Taylor's Place gate-sign crop and truck-decal crop | #6, #7 | `assets/logos/taylors-place/reference/` |

## Downloaded and not kept

A second upload of the composite in #6, `2025/10/hlds_taylors-place-crawfest_header.png` (2000 × 300 px, 848,510 bytes, MD5 `2b5d3fc7bc364888fb1fd384f0a50254`), was downloaded with the set. It is a re-encoding of the same image and its filename differs from #6 only in letter case, which breaks checkouts on macOS and Windows (case-insensitive filesystems), so it is not kept in the repository.

## Not downloaded

The old site's media library also held files that are not part of this identity and were deliberately left out at the owner's instruction (Cotton Foundation and Taylor's Place assets only, no other logos): earlier logo files from before the 2026 identity, files carrying other organizations' logos, third-party partner and sponsor logos, a near-transparent watermark export of the mark (superseded by #5), five 1 × 1 SVGs left over from a 2021 theme, and the Taylor's Place architectural renderings, event graphics, and sponsorship-catalog PDFs (imagery and documents, not identity; see `guidelines/imagery.md` and decision log Q8). None of them are referenced anywhere in this repository.

## Not supplied (and needed)

- The original vector artwork for the mark and lockup (Illustrator, EPS, or PDF). Would replace the traced SVGs and identify the wordmark face (Q1, Q3).
- The Taylor's Place sign artwork (the sign maker's file) and any Taylor's Place logo file (Q1).
- Any prior brand guide, color spec, or thread spec.
- Photography originals and releases (Q8).

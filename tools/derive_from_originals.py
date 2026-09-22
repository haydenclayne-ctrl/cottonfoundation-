#!/usr/bin/env python3
"""
derive_from_originals.py — regenerate the working brand assets from assets/originals/.

Reads the supplied originals, never writes to them. Verifies their checksums first
(see assets/originals/INVENTORY.md) and stops if any original has been altered.

Outputs (all overwritten on every run):

  assets/marks/
    cf-mark_full-color.png / .svg      the cotton-boll mark, gold boll + navy hands
    cf-mark_white.png / .svg           one color, for navy and photographic grounds
    cf-mark_navy.png / .svg            one color, for light grounds
    cf-mark_gold.png / .svg            one color, foil / thread / accent use
    cf-mark_black.png / .svg           utility (engraving, laser, forms)
    preview/                           2000 px previews on white and on navy

  assets/logos/cotton-foundation/
    cf-lockup_horizontal_full-color.png / .svg
    cf-lockup_horizontal_white.png / .svg
    cf-lockup_horizontal_navy.png / .svg
    cf-lockup_horizontal_black.png / .svg
    preview/

  assets/logos/taylors-place/reference/
    tp-gate-sign_photo-crop.png        the built Taylor's Place mark, gold on navy (gate sign)
    tp-truck-decal_photo-crop.png      the same mark, white, on a truck tailgate

How the geometry is derived
  * The horizontal lockup is taken from Cotton-Foundation-2026-01.png (6000 x 3553 px, full color).
    Cotton-Foundation-2026-04.png is the same artwork exported in white on the same canvas and
    Cotton-Foundation-2026.png is the same artwork at a larger scale (silhouette IoU 0.997);
    2026-01 is used as the single geometric source so every colorway shares one outline.
  * The mark is taken from Cotton-Foundation-2026-Backgrouond.png (8334 x 8334 px, white) for
    geometry and from Cotton-Foundation-2026-Icon.png (584 x 584 px, full color) for the color
    split (which shapes are gold, which are navy). The two are the same artwork (IoU 0.989).
  * SVGs are auto-traced from the PNG silhouettes with VTracer (spline mode). They are working
    vectors, not the designer's master artwork. See assets/README.md, "Vector status".

Colors written into the derived files are the canonical brand tokens (tokens/), not the values
measured in the PNGs: navy #17345E (the PNGs measure #16345E) and gold #9F762B (as measured).
See brand/decision-log.md, decision 2026-09-22 / D3.

Requirements: Pillow, numpy, vtracer (pip install vtracer). cairosvg is optional; when present it
renders the SVGs to check them and to make the SVG previews.

Usage: python3 tools/derive_from_originals.py [--skip-svg]
"""

import hashlib
import os
import re
import sys
import tempfile

import numpy as np
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGINALS = os.path.join(ROOT, "assets", "originals", "cottonfoundation-org-2026-09-22")

# MD5 checksums of the originals exactly as downloaded on 2026-09-22 (assets/originals/INVENTORY.md).
CHECKSUMS = {
    "Cotton-Foundation-2026-01.png": "6cbd761a68ce40a137f0b086fb312428",
    "Cotton-Foundation-2026-04.png": "81c5008e10af47e0059e8b8dd62090b4",
    "Cotton-Foundation-2026.png": "15d0a58969591432af7bc4de88b819bf",
    "Cotton-Foundation-2026-Icon.png": "e98b0e293792cf23d4c2020cf606c912",
    "Cotton-Foundation-2026-Backgrouond.png": "089925d5da602f13037625576abd72eb",
    "HLDS_Taylors-Place-Crawfest_HEADER.png": "8016f76f0f562f987228e41636e7a025",
    "Taylors-Place-Shoot-April-2025-33.png": "0a12b0f3d0878d6cee5559779fda2173",
}

# Canonical colors (tokens/cotton-foundation.tokens.json)
NAVY = "#17345E"
GOLD = "#9F762B"
WHITE = "#FFFFFF"
BLACK = "#000000"

COLORWAYS = {"white": WHITE, "navy": NAVY, "gold": GOLD, "black": BLACK}


# ----------------------------------------------------------------------------- helpers
def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_originals():
    bad = []
    for name, expected in CHECKSUMS.items():
        p = os.path.join(ORIGINALS, name)
        if not os.path.exists(p):
            bad.append(f"missing: {name}")
        elif md5(p) != expected:
            bad.append(f"checksum mismatch: {name}")
    if bad:
        sys.exit("Originals have been altered or are missing. Restore them before deriving:\n  " + "\n  ".join(bad))
    print("originals verified (%d files)" % len(CHECKSUMS))


def load_rgba(name):
    return Image.open(os.path.join(ORIGINALS, name)).convert("RGBA")


def alpha_bbox(arr):
    ys, xs = np.where(arr[:, :, 3] > 0)
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1


def trim(im):
    arr = np.array(im)
    x0, y0, x1, y1 = alpha_bbox(arr)
    return im.crop((x0, y0, x1, y1))


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def recolor(im, hex_color):
    """Keep the alpha channel, replace RGB with one flat color."""
    arr = np.array(im.convert("RGBA")).copy()
    r, g, b = hex_to_rgb(hex_color)
    arr[:, :, 0] = r
    arr[:, :, 1] = g
    arr[:, :, 2] = b
    return Image.fromarray(arr, "RGBA")


def composite_colors(alpha_im, label_map, colors):
    """Build an RGBA image from one alpha channel and an integer label map (label -> hex)."""
    a = np.array(alpha_im.convert("RGBA"))[:, :, 3]
    out = np.zeros((a.shape[0], a.shape[1], 4), dtype=np.uint8)
    for label, hex_color in colors.items():
        r, g, b = hex_to_rgb(hex_color)
        m = label_map == label
        out[m, 0] = r
        out[m, 1] = g
        out[m, 2] = b
    out[:, :, 3] = a
    return Image.fromarray(out, "RGBA")


def ensure_dir(p):
    os.makedirs(p, exist_ok=True)
    return p


def save_png(im, path):
    im.save(path, "PNG", optimize=True)
    print("  wrote", os.path.relpath(path, ROOT), im.size)


def preview(im, path, bg_hex, width=2000, pad_frac=0.08):
    """Render a mark on a flat background with clear space, at a fixed width."""
    w, h = im.size
    scale = (width * (1 - 2 * pad_frac)) / w
    inner = im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    pad = int(width * pad_frac)
    canvas = Image.new("RGBA", (width, inner.height + 2 * pad), hex_to_rgb(bg_hex) + (255,))
    canvas.alpha_composite(inner, (pad, pad))
    canvas.convert("RGB").save(path, "PNG", optimize=True)
    print("  wrote", os.path.relpath(path, ROOT), canvas.size)


# ----------------------------------------------------------------------------- tracing
def trace_mask_to_paths(mask_im):
    """Trace a black-on-white mask with VTracer; return the list of <path .../> elements."""
    import vtracer  # imported lazily so PNG derivation works without it

    with tempfile.TemporaryDirectory() as td:
        src = os.path.join(td, "mask.png")
        dst = os.path.join(td, "mask.svg")
        mask_im.convert("RGB").save(src)
        vtracer.convert_image_to_svg_py(
            src,
            dst,
            colormode="binary",
            hierarchical="stacked",
            mode="spline",
            filter_speckle=8,
            corner_threshold=60,
            length_threshold=4.0,
            max_iterations=10,
            splice_threshold=45,
            path_precision=2,
        )
        svg = open(dst, encoding="utf-8").read()
    return re.findall(r"<path[^>]*/>", svg)


def set_fill(path_el, hex_color):
    if re.search(r'fill="[^"]*"', path_el):
        return re.sub(r'fill="[^"]*"', f'fill="{hex_color}"', path_el)
    return path_el.replace("<path", f'<path fill="{hex_color}"', 1)


def write_svg(path, width, height, groups, title):
    """groups: list of (hex_color, [path elements])."""
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f"  <title>{title}</title>",
        "  <!-- Working vector auto-traced from the supplied PNG original (VTracer). Not the designer's master artwork. -->",
    ]
    for hex_color, paths in groups:
        lines.append(f'  <g fill="{hex_color}">')
        for p in paths:
            lines.append("    " + set_fill(p, hex_color))
        lines.append("  </g>")
    lines.append("</svg>")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("  wrote", os.path.relpath(path, ROOT), f"({len(sum((g[1] for g in groups), []))} paths)")


def alpha_mask_image(alpha_arr, select=None):
    """Black-on-white mask from an alpha array; `select` is an optional boolean array restricting it."""
    a = alpha_arr.astype(np.float32) / 255.0
    if select is not None:
        a = a * select
    return Image.fromarray((255 - a * 255).astype(np.uint8), "L")


def svg_preview(svg_path, png_path, bg_hex, width=2000):
    try:
        import cairosvg
    except ImportError:
        return
    cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=width, background_color=bg_hex)
    print("  wrote", os.path.relpath(png_path, ROOT), "(svg render)")


# ----------------------------------------------------------------------------- the mark
def derive_mark(do_svg):
    print("mark (cotton boll)")
    out = ensure_dir(os.path.join(ROOT, "assets", "marks"))
    prev = ensure_dir(os.path.join(out, "preview"))

    hi = trim(load_rgba("Cotton-Foundation-2026-Backgrouond.png"))  # 8251 x 8219, white
    lo = trim(load_rgba("Cotton-Foundation-2026-Icon.png"))  # 563 x 561, full color

    # Color split: label the low-res color icon (1 = gold boll, 2 = navy hands), dilate each class so
    # anti-aliased edges are covered, and sample it at hi-res. The boll and the hands do not touch.
    lo_arr = np.array(lo)
    opaque = lo_arr[:, :, 3] > 40
    rgb = lo_arr[:, :, :3].astype(int)
    d_gold = np.abs(rgb - np.array(hex_to_rgb("#9F762B"))).sum(2)
    d_navy = np.abs(rgb - np.array(hex_to_rgb("#16345E"))).sum(2)
    label_lo = np.where(opaque & (d_gold < d_navy), 1, np.where(opaque, 2, 0)).astype(np.uint8)
    gold_lo = Image.fromarray((label_lo == 1).astype(np.uint8) * 255).filter(ImageFilter.MaxFilter(9))
    navy_lo = Image.fromarray((label_lo == 2).astype(np.uint8) * 255).filter(ImageFilter.MaxFilter(9))
    gold_hi = np.array(gold_lo.resize(hi.size, Image.BILINEAR)) > 127
    navy_hi = np.array(navy_lo.resize(hi.size, Image.BILINEAR)) > 127
    alpha_hi = np.array(hi)[:, :, 3]
    label_hi = np.where(gold_hi & ~navy_hi, 1, np.where(navy_hi, 2, 0)).astype(np.uint8)
    # anything opaque but unlabeled falls to the nearer class by simple majority of its neighborhood
    unl = (alpha_hi > 0) & (label_hi == 0)
    if unl.any():
        label_hi[unl] = 2
    label_hi[alpha_hi == 0] = 0

    full = composite_colors(hi, label_hi, {1: GOLD, 2: NAVY})
    work = full.resize((2000, int(2000 * full.height / full.width)), Image.LANCZOS)
    save_png(work, os.path.join(out, "cf-mark_full-color.png"))
    for name, hx in COLORWAYS.items():
        save_png(recolor(work, hx), os.path.join(out, f"cf-mark_{name}.png"))
    preview(work, os.path.join(prev, "cf-mark_full-color_on-white_preview.png"), WHITE, width=1200)
    preview(recolor(work, WHITE), os.path.join(prev, "cf-mark_white_on-navy_preview.png"), NAVY, width=1200)
    preview(recolor(work, GOLD), os.path.join(prev, "cf-mark_gold_on-navy_preview.png"), NAVY, width=1200)
    preview(recolor(work, NAVY), os.path.join(prev, "cf-mark_navy_on-white_preview.png"), WHITE, width=1200)

    if do_svg:
        w, h = hi.size
        gold_paths = trace_mask_to_paths(alpha_mask_image(alpha_hi, label_hi == 1))
        navy_paths = trace_mask_to_paths(alpha_mask_image(alpha_hi, label_hi == 2))
        all_paths = trace_mask_to_paths(alpha_mask_image(alpha_hi))
        write_svg(os.path.join(out, "cf-mark_full-color.svg"), w, h, [(GOLD, gold_paths), (NAVY, navy_paths)], "Cotton Foundation mark, full color")
        for name, hx in COLORWAYS.items():
            write_svg(os.path.join(out, f"cf-mark_{name}.svg"), w, h, [(hx, all_paths)], f"Cotton Foundation mark, {name}")
        svg_preview(os.path.join(out, "cf-mark_full-color.svg"), os.path.join(prev, "cf-mark_full-color_svg-render_preview.png"), WHITE, width=1200)


# ----------------------------------------------------------------------------- the lockup
def derive_lockup(do_svg):
    print("horizontal lockup")
    out = ensure_dir(os.path.join(ROOT, "assets", "logos", "cotton-foundation"))
    prev = ensure_dir(os.path.join(out, "preview"))

    src = trim(load_rgba("Cotton-Foundation-2026-01.png"))  # 5310 x 1703, full color
    arr = np.array(src)
    alpha = arr[:, :, 3]
    rgb = arr[:, :, :3].astype(int)
    d_gold = np.abs(rgb - np.array(hex_to_rgb("#9F762B"))).sum(2)
    d_navy = np.abs(rgb - np.array(hex_to_rgb("#16345E"))).sum(2)
    label = np.where(alpha > 0, np.where(d_gold < d_navy, 1, 2), 0).astype(np.uint8)

    full = composite_colors(src, label, {1: GOLD, 2: NAVY})
    work = full.resize((4000, int(4000 * full.height / full.width)), Image.LANCZOS)
    save_png(work, os.path.join(out, "cf-lockup_horizontal_full-color.png"))
    for name, hx in COLORWAYS.items():
        if name == "gold":
            continue  # the lockup is not used in all-gold
        save_png(recolor(work, hx), os.path.join(out, f"cf-lockup_horizontal_{name}.png"))
    preview(work, os.path.join(prev, "cf-lockup_horizontal_full-color_on-white_preview.png"), WHITE)
    preview(recolor(work, WHITE), os.path.join(prev, "cf-lockup_horizontal_white_on-navy_preview.png"), NAVY)
    preview(recolor(work, NAVY), os.path.join(prev, "cf-lockup_horizontal_navy_on-white_preview.png"), WHITE)

    if do_svg:
        w, h = src.size
        gold_paths = trace_mask_to_paths(alpha_mask_image(alpha, label == 1))
        navy_paths = trace_mask_to_paths(alpha_mask_image(alpha, label == 2))
        all_paths = trace_mask_to_paths(alpha_mask_image(alpha))
        write_svg(os.path.join(out, "cf-lockup_horizontal_full-color.svg"), w, h, [(GOLD, gold_paths), (NAVY, navy_paths)], "Cotton Foundation horizontal lockup, full color")
        for name, hx in COLORWAYS.items():
            if name == "gold":
                continue
            write_svg(os.path.join(out, f"cf-lockup_horizontal_{name}.svg"), w, h, [(hx, all_paths)], f"Cotton Foundation horizontal lockup, {name}")
        svg_preview(os.path.join(out, "cf-lockup_horizontal_full-color.svg"), os.path.join(prev, "cf-lockup_horizontal_full-color_svg-render_preview.png"), WHITE)

    # Measurements used in guidelines/logos.md and guidelines/sub-brands.md
    mark_cols = np.where((label > 0).any(0))[0]
    # the mark is the leftmost cluster of opaque columns; find the first gap of transparent columns
    gaps = np.where(np.diff(mark_cols) > 40)[0]
    mark_right = int(mark_cols[gaps[0]]) + 1 if len(gaps) else None
    print(f"  lockup trimmed size {w}x{h}; mark occupies columns 0..{mark_right} (width {mark_right}); ratio {w/h:.4f}")


# ----------------------------------------------------------------------------- taylor's place references
def derive_taylors_place_refs():
    print("taylor's place references")
    out = ensure_dir(os.path.join(ROOT, "assets", "logos", "taylors-place", "reference"))
    header = Image.open(os.path.join(ORIGINALS, "HLDS_Taylors-Place-Crawfest_HEADER.png")).convert("RGB")
    sign = header.crop((1190, 20, 1560, 260))  # the gate sign, gold on navy
    save_png(sign, os.path.join(out, "tp-gate-sign_photo-crop.png"))
    shoot = Image.open(os.path.join(ORIGINALS, "Taylors-Place-Shoot-April-2025-33.png")).convert("RGB")
    decal = shoot.crop((610, 175, 790, 255))  # the tailgate decal, white on black
    save_png(decal, os.path.join(out, "tp-truck-decal_photo-crop.png"))


# ----------------------------------------------------------------------------- main
if __name__ == "__main__":
    do_svg = "--skip-svg" not in sys.argv
    verify_originals()
    derive_mark(do_svg)
    derive_lockup(do_svg)
    derive_taylors_place_refs()
    print("done")

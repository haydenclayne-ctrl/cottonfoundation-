#!/usr/bin/env python3
"""
contrast_check.py — WCAG 2.x contrast ratios for the Cotton Foundation palette.

Reads tokens/cotton-foundation.tokens.json and prints the contrast ratio of every
foreground/background pair that the guidelines allow, with the WCAG level it meets
(AAA >= 7:1, AA >= 4.5:1, AA-large >= 3:1 for text 24 px+ or 19 px bold+).

Usage: python3 tools/contrast_check.py
"""

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKENS = os.path.join(ROOT, "tokens", "cotton-foundation.tokens.json")


def srgb_to_lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_color):
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * srgb_to_lin(r) + 0.7152 * srgb_to_lin(g) + 0.0722 * srgb_to_lin(b)


def contrast(fg, bg):
    l1, l2 = luminance(fg), luminance(bg)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def level(ratio):
    if ratio >= 7:
        return "AAA"
    if ratio >= 4.5:
        return "AA"
    if ratio >= 3:
        return "AA large only"
    return "fail"


def flatten(node, prefix=""):
    out = {}
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            if v.get("$type") == "color":
                out[prefix + k] = v["$value"]
        elif isinstance(v, dict):
            out.update(flatten(v, prefix + k + "."))
    return out


if __name__ == "__main__":
    with open(TOKENS, encoding="utf-8") as f:
        tokens = json.load(f)
    colors = {k: v for k, v in flatten(tokens["color"]).items() if not v.startswith("{")}
    pairs = [
        ("neutral.ink", "neutral.white"),
        ("primary.navy", "neutral.white"),
        ("neutral.slate", "neutral.white"),
        ("primary.harvest-gold", "neutral.white"),
        ("primary.cotton-gold", "neutral.white"),
        ("accent.hope-gold", "neutral.white"),
        ("secondary.horizon-blue", "neutral.white"),
        ("neutral.white", "primary.navy"),
        ("accent.hope-gold", "primary.navy"),
        ("primary.harvest-gold", "primary.navy"),
        ("primary.cotton-gold", "primary.navy"),
        ("secondary.horizon-blue", "primary.navy"),
        ("neutral.silver", "primary.navy"),
        ("neutral.ink", "accent.hope-gold"),
        ("neutral.white", "primary.harvest-gold"),
        ("neutral.white", "secondary.horizon-blue"),
        ("neutral.ink", "neutral.mist"),
        ("primary.navy", "neutral.cloud"),
        ("neutral.white", "secondary.signal-red"),
    ]
    print(f"{'foreground':28} {'background':22} {'ratio':>7}  level")
    for fg, bg in pairs:
        r = contrast(colors[fg], colors[bg])
        print(f"{fg + ' ' + colors[fg]:28} {bg + ' ' + colors[bg]:22} {r:6.2f}:1  {level(r)}")

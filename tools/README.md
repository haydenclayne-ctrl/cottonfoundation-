# tools/

Scripts that keep the repository honest. They read `assets/originals/` and `tokens/`; they never write to the originals.

| Script | What it does | Run |
|---|---|---|
| `derive_from_originals.py` | Verifies the originals' checksums, then regenerates `assets/marks/`, `assets/logos/cotton-foundation/`, and the Taylor's Place reference crops: trimmed PNGs in every colorway, previews on white and navy, and auto-traced SVGs (VTracer). Prints the lockup measurements used in the guidelines | `python3 tools/derive_from_originals.py` (about 50 s; `--skip-svg` for PNGs only) |
| `contrast_check.py` | WCAG contrast ratios for every color pair the guidelines allow, from the tokens JSON | `python3 tools/contrast_check.py` |

Requirements: Python 3.10+, Pillow, numpy, `vtracer` (`pip install vtracer`), and optionally `cairosvg` for the SVG render checks.

When the owner supplies master vector artwork (decision log Q1), the tracing step is retired for those files and this README records which outputs are now hand-off masters rather than derived.

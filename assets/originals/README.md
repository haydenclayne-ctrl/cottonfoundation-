# assets/originals/

Files exactly as received. **Immutable.** Never edit, rename, re-save, re-export, or delete anything here. Add new supplied files in a dated or source-named subfolder and record them, with checksums, in `INVENTORY.md`.

| Folder | Source | Files |
|---|---|---|
| `cottonfoundation-org-2026-09-22/` | The WordPress media library of cottonfoundation.org, downloaded through the owner's browser on 2026-09-22 | 5 logo PNGs (the 2026 identity), 2 photographs referencing the Taylor's Place mark as built |

Every derived asset in `assets/marks/`, `assets/logos/`, and the reference crops is regenerated from these by `tools/derive_from_originals.py`, which verifies the checksums first and refuses to run if any original has changed.

When the owner supplies master vector artwork (decision log Q1), it goes in a new subfolder here (for example `owner-supplied-YYYY-MM-DD/`), is catalogued in `INVENTORY.md`, and becomes the new source for the working files.

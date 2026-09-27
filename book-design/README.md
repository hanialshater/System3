# Book production

The current full-book workflow is [PDF.md](PDF.md), run through `pdf.py`.
The manuscript lives in `../chapters/`; `curated/book-order.json` sets its order.

| Location | Role | Status |
| --- | --- | --- |
| `curated/` | Full-book renderer, layout, assets and checks | Current |
| `paged/` | Chapter 5 text-flow and cutout proof | Experiment; not integrated |
| `render_back_cover.py` | Standalone back-panel text proof | Requires Linux DejaVu fonts; portability pending |
| `requirements-pdf.txt` | Normal build dependencies | Current |
| `requirements-upscale.txt` | Cover enhancement dependencies | Reproduction only |
| `paged/DESIGN.md` | Text-flow rationale | Chapter 5 experiment |

Reusable artwork is stored through Git LFS. See [print artwork notes](curated/PRINT-ART.md).
Generated files belong in ignored `out/` or `../output/` locations, never among
manuscript sources. Previous tracked proofs were preserved locally under
`../output/archive/2026-09-27/`; earlier commits also retain those versions.

The obsolete draft renderer, slot manifests, generated art prompts, candidate
images and old design contracts have been removed. Git history retains them;
they are not inputs or instructions for the current book.

## Current build

```sh
.venv-pdf/bin/python book-design/pdf.py status
.venv-pdf/bin/python book-design/pdf.py build --preview --strict-art
```

`curated/art.json` attaches illustrations to manuscript passages;
`curated/layout.json` controls their treatment. Original selected artwork lives
in `curated/assets/art/`; `curated/print-assets.json` selects enhanced covers
from `curated/assets/print/`. Fonts and licenses live in `curated/assets/fonts/`.

Outstanding work: seven Chapter 5 visual directions, the decision on full-book
text-flow composition, back-cover utility portability, and printer-specific
bleed, spine and color preparation. See [the review queue](../resources/REVISIT.md).

# Book production

The current full-book workflow is [PDF.md](PDF.md), run through `pdf.py`.
The manuscript lives in `../chapters/`; `curated/book-order.json` sets its order.

| Location | Role | Status |
| --- | --- | --- |
| `curated/` | Full-book renderer, layout, assets and checks | Current |
| `paged/` | Chapter 5 text-flow and cutout proof | Experiment; not integrated |
| `render_back_cover.py` | Standalone back-panel text proof | Current utility |
| `render.py`, `manifests/` | Earlier chapter-by-chapter draft layout | Legacy experiment |
| `export_prompts.py`, `art-prompts/` | Art briefs generated from legacy manifests | Review before generating art |
| `art-candidates/` | Candidate images and recorded decisions | Retained design history |
| `design-spec.md`, `redesign-brief.md`, `PIPELINE.md` | Earlier layout contracts | Legacy design references |
| `text-flow-design.md` | Text-flow design proposal | Compare with Paged.js experiment |

Reusable artwork is stored through Git LFS. See [print artwork notes](curated/PRINT-ART.md).
Generated files belong in ignored `out/` or `../output/` locations, never among
manuscript sources. Previous tracked proofs were preserved locally under
`../output/archive/2026-09-27/`; earlier commits also retain those versions.

Outstanding decisions are listed in [the repository review queue](../resources/REVISIT.md).

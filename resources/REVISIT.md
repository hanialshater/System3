# Repository review queue

Reviewed 27 September 2026. This is a production and editorial inventory, not
authorization to rewrite manuscript prose or replace selected illustrations.

| Material | What needs review |
| --- | --- |
| `prompts/notebooklm.md` and `prompts/notebooklm-local/` | Choose or reconcile the two adaptations against current chapters. The local pack records source hashes; neither pack should be assumed current. Its Chapter 14 label refers to the Scaffolds coda, not another numbered chapter. |
| `book-design/paged/` | Evaluate the Chapter 5 composition proof before adopting any of it in the full book. Its design rationale is in `paged/DESIGN.md`. |
| `drafts/reader-map.md` | Compare this proposed reader map with the current evidence appendix; its draft claims may predate manuscript revisions. |
| `drafts/objections-draft.md` | Unaccepted editorial prose; decide whether to incorporate, revise or retire it. |
| `resources/chapter-openers/` | Small legacy opener files with older chapter numbering. Check references before renaming; curated masters are stored separately. |
| Chapter inline image references | Some legacy figure targets are absent. The curated PDF uses explicit artwork mappings, but GitHub Markdown may still show broken images. Review mappings visually before replacing references. |
| Chapter 5 visual directions | Seven outstanding illustration briefs were reported in the latest print pass. Existing artwork coverage does not complete these new briefs. |
| `book-design/render_back_cover.py` | Replace hard-coded Linux font paths before using this standalone utility on macOS. |
| `resources/evaluations/` | Dated historical assessments. Older locked labels, word targets and automatic-build instructions do not override the current manuscript and manual PDF workflow. |
| Print production | Printer selection, bleed, spine, output profile and physical proof remain outstanding. |

## Cleanup performed

- Removed the obsolete draft renderer, manifest-based art pipeline, generated
  prompts, candidate images and superseded design contracts from `book-design/`.
  Git history retains them. The current renderer does not depend on them.
- Moved the text-flow design rationale into `book-design/paged/DESIGN.md`.
- Grouped the September 20 local NotebookLM pack under `prompts/notebooklm-local/`;
  updated its links and manifest paths while retaining recorded content hashes.
- Moved 14 old draft PDFs and three `dist/` exports into the ignored local
  `output/archive/2026-09-27/` directory. They remain recoverable from Git history
  after the cleanup is committed. This does not shrink existing Git history.
- Ignored future legacy build outputs and macOS metadata.
- Kept the current manuscript, current PDF, original and enhanced artwork,
  research, draft prose and historical evaluations intact.

Temporary build diagnostics remain in ignored `tmp/pdfs/`; they include review
evidence and enhancement candidates, so this pass did not erase them.

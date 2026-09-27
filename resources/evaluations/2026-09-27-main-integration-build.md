# Main integration and illustrated proof — 27 September 2026

Fetched and fast-forwarded local main to `86a6f0a`. Restored local work from the retained recovery stash `Before integrating live main and illustrated pipeline 2026-09-27`. Resolved the workflow and Chapter 5 conflicts. All changes remain uncommitted and nothing was pushed.

Kept main's manuscript architecture and back-cover wording. Integrated the two selected Chapter 5 sentences and the Chapter 4 scope sentence. Preserved the case-colliding local NotebookLM instructions as `prompts/notebooklm-local-workflow.md`, alongside main's `prompts/notebooklm.md`.

The curated renderer now uses `book-design/curated/book-order.json` for all 29 manuscript sources, preserves the TeX-authored part headings, supports the reveal and alternative-ending pages, and keeps the back-matter marker as a contents entry. Hidden editorial comments are excluded; visual briefs are recorded. Table validation checks individual cells across repeated page headers. The author bio uses 11/14 pt type to fit one page.

Visually reviewed and explicitly reattached 25 changed artwork anchors; all 88 existing interior illustrations are included. The glass-box illustration follows its passage into Part III through a filename-based section anchor. Its height is limited to keep the opening on one page. Existing covers remain included. Full details are in `book-design/curated/main-integration-art-review.json`.

## Result

- Output: `output/pdf/System3_Curated_6x9.pdf`
- Pages: 342; trim: 6 × 9 inches.
- Verified source blocks: 2266; footnotes: 167.
- All mechanical checks passed: source text, page bounds, fonts, bookmarks, blank pages and art/text intersections.
- 10 safeguard tests passed.
- Contact sheets reviewed through the book, with full-size checks of structural pages, the evidence table and final author bio.
- Existing artwork/cover issues: zero.
- Outstanding new visual briefs: 7 (Chapter 5). This run reused existing artwork; it did not generate those new diagrams.
- SHA-256: `afa59adcdddb3535d9ff7b3659bb016f5a0563b24b65e0f0d53c48c6137f84a9`.

Rebuild on request with `.venv-pdf/bin/python book-design/pdf.py build --preview --strict-art`. The separate Chapter 5 Paged.js experiment was preserved, not rerun or substituted for the full-book renderer.

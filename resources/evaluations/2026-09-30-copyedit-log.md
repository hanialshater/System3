# Copyedit log — 30 September 2026

Work follows the [fix and copyedit plan](../editorial/copyedit-plan-2026-09-30.md). A chapter closes only after it passes its gate:

1. The seed check passes.
2. The PDF build passes, which checks reference numbering, artwork anchors and covers.
3. The unit tests pass.
4. A re-read against the house dimensions finds nothing further to fix.

Scores are editorial shorthand, as in the [readiness evaluation](2026-09-30-chapter-readiness-evaluation.md).

**Baseline build before any edit:** 317 pages, 87 interior illustrations, 0 placements or covers needing review, 7 pending design directions.

## Pass 0 — mechanical, whole manuscript

- **Quotation marks.** Converted straight quotes to curly quotes in prose and references. Straight quotes stayed in code, HTML comments, URLs and raw LaTeX. The renderer prints quotes exactly as typed, and the previous proof contained 65 straight double quotes.
- **Ellipses.** Replaced three periods with the ellipsis glyph outside code.
- **Spelling.** Standardized to American: catalog, program (Lakatos), traveled, fiber, anesthetist, operating theater, theater, e-commerce.
- **Heading case.** "Separate Use from Investigation" became "Separate Use From Investigation", to match the book's rule of capitalizing prepositions of four or more letters.
- **Tooling kept in step:**
  - three seed anchors in `check-eggs.sh` and the register now use curly apostrophes;
  - the `a120` art anchor now reads "program";
  - the Chapter 1 and 3 cover titles in `provenance.json` now use curly apostrophes. The cover art itself is unchanged.
- **Correction during the pass.** The first `programme → program` substitution also turned "programmers" into "programrs" in Chapter 6. A word-level diff of the whole pass caught it, and the word was restored. After the fix, the word-level diff shows only the intended spelling changes.
- **Gate:** seeds pass; build 317 pages, 87 illustrations, 0 placements or covers needing review; unit tests pass.

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

## Part I and Part II

Every chapter here was re-read line by line against the plan and the house dimensions. Protected lines were checked and left intact.

| Section | Changes | Re-evaluation | Status |
|---|---|---|---|
| Preface | None beyond Pass 0. The Leibniz dates, the Poincaré-embedding and MAP-Elites examples, and "Three centuries later" were all checked. The dated opening ("It is September 2026") is confirmed by the fact check. | 8.5, unchanged. Short and seeds the book (cathedral, coffee, loose cable). | Closed |
| Part pages | None beyond Pass 0. | — | Closed |
| 1 | "responsible for everything from the deepest ocean trenches" became "from the creatures of the deepest ocean trenches", because life did not make the trenches. The restored cat paragraph lost its serial comma, per house style; its wording is untouched. | 8, unchanged. Four bold statements kept: they name the book's bets. | Closed |
| 2 | The ten `[Missing figure]` placeholders became `DIAGRAM — missing figure` production comments, which the build now tracks (7 → 17 design directions). The reading edition no longer prints them. The evolutionary-search result (2.08 → about 2.45), which previously appeared only in a caption, is now in the prose. "best-known" is hyphenated. The section heading "The Algorithmic Vortex" now matches the chapter's term, "The Algorithm Vortex". | 8.5. The production blocker is removed. The methods trail for 2.636 (model, date, tolerance, budget) is still absent; it needs the author's run records and was not invented. | Closed; figures and methods trail left to the author |
| 3 | One serial comma. | 8.5, unchanged. No wording problems found. | Closed |
| 4 | None beyond Pass 0. Recomputed every figure in the epistemic-swe tables: 57% patch reduction; 4.9×/15.6×/7.6×/7.5×; more than two-fifths of baseline lines; about one-third once the outlier is excluded. All are consistent. | 9, unchanged. | Closed |
| 5 | "plough" became "plow"; Pass 0 spelling. Four fact-check corrections: (1) Sima Qian's 213 BCE order targeted the histories of states other than Qin and privately held classics, and exempted medicine, divination and agriculture (the text had said "private histories … useful technical works"); (2) Li Si was a minister in 221 BCE and chancellor only later; (3) Kepler saw the moons through a telescope Galileo had sent to the Elector of Cologne, so the passage no longer blames "Galileo's lens" and now notes the shared lens grinder; (4) Popper called it "the third world" in 1967 and "World 3" later. | 9, unchanged. Every other Carlini, Dr. Stone, Bromiley, Millikan, Galileo, Boyle, Wegener, Newton, OPERA and Popper detail is confirmed. | Closed |
| Reveal | None. The `ASSISTANT EDIT` marker stays for the author. | 8. | Author decision |

**Gate:** seeds pass; build 317 pages, 87 illustrations, 0 placements or covers needing review, 17 pending design directions (the 10 Chapter 2 figures are now counted); unit tests pass.

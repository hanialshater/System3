---
name: book-build
description: Build and proof-check the System 3 book (or any Markdown-to-PDF manuscript) — assembly order, the curated 6×9 renderer and its gates, the Paged.js chapter experiment, the GitHub/pandoc build, structural pages (part pages, reveal, dividers), footnotes and references, art anchors, print resolution, and a mechanical QA pass on the built PDF (text that shouldn't print, garbage headers, orphaned captions, dropped glyphs, duplicated pages, image density, unembedded fonts) followed by looking at rendered pages. Use whenever the user asks to "build the PDF", "make a proof", "check the proof", "why does this page look wrong", "print-ready", or uploads a built PDF for review, and after any structural edit that adds or moves files.
---

# Book build

The repo already has a mature pipeline. Use it; don't rebuild one. Read `book-design/PDF.md` first: it documents `pdf.py status|build --preview|--strict-art|--force`, the 6×9 curated baseline, how art follows passages, and what the build checks before it replaces the previous proof.

## Before building

- **Assembly order** lives in `book-design/curated/book-order.json` (and the GitHub workflow list for the pandoc build). Every new structural file — part page, reveal, interlude, divider, back-matter marker — must be added there exactly once. A file missing from the order silently doesn't print.
- **Footnotes and references.** Chapter-scoped notes and numbered citations to `appendix-references.md` anchors. Duplicate keys across chapters print the first definition everywhere when chapters are joined (the old `[^saussure]` bug). Run fresh-claims' `claims.py --notes`.
- **Art anchors.** Text passes delete the sentences art is anchored to, and the renderer then omits the image for review. Run art-direction's `art_audit.py` after every text pass.
- **Markers.** Comments are stripped at build, so flagged assistant text prints silently as if the author wrote it. Count unresolved markers; release builds should have none.
- **Glyphs.** Characters the body font lacks (✓ ✗ ʊ have done this) vanish or print as boxes. Change the text or the font.

## Build

- Curated edition: `.venv-pdf/bin/python book-design/pdf.py build --preview` (add `--strict-art` for a release candidate). Read `build-report.json`: artwork needing attention, outstanding VISUAL/DIAGRAM directions, section page numbers.
- Tests: `python -m unittest discover -s book-design/curated/tests -v`.
- Chapter 5 Paged.js experiment: `book-design/paged/README.md`; separate decision whether to adopt it book-wide.
- Without the curated environment (LFS assets, venv): mirror the workflow file list with pandoc + xelatex for a text proof. If xelatex fails on a missing `lmodern.sty`, a stub `\ProvidesPackage{lmodern}` on `TEXINPUTS` gets past it. This proof is for reading transitions, not for judging layout.

## Proof QA

1. Run `scripts/proof_qa.py BOOK.pdf --source chapters`. It flags leaked comments and markers, raw LaTeX or Markdown residue, garbage running headers, captions on pages with no image, duplicated page text, straight quotes, unembedded fonts, glyphs present in the source but absent from the PDF, and the share of pages carrying images.
2. **Look at pages.** Render with `--render` and view them: every new structural page, the first page of each chapter, pages around each moved section, a sample of back matter (where header code paths differ), and any page the script flagged. Mechanical checks don't replace visual review.
3. **Read the seams** in extracted text (`pdftotext`, pages either side of each chapter break) for transitions after structural edits.
4. Report defects as a numbered list with page numbers, the cause if known, and the fix (see `references/defects.md` for the ones seen before).

## Print readiness

300 PPI at placed size for every image (the build measures pixels at placement, not DPI metadata); lossless embedding; RGB masters until a printer is chosen. Bleed, cover spread and spine, output profile, PDF/X and a physical proof all wait for the printer. Don't apply an arbitrary CMYK conversion, and don't claim press approval from a screen proof.

## Delivery

When downloads fail (zero-byte files have happened), also deliver a `.txt` copy of patches, or paste diffs and scripts in chat. Large PDFs: say the size and page count.

## Files

- `scripts/proof_qa.py` — mechanical QA of a built PDF, plus page rendering.
- `references/defects.md` — defects found in past proofs and their causes.

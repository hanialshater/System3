# Artwork acceptance checklist

1. Start from the current chapter and the [selected artwork register](chapter-openers.md).
   Confirm that the requested visual is still needed and is not already supplied
   by an existing illustration.
2. Preserve narrative order, reveal timing and the author's protected compositions.
   Label a diagram as schematic when it does not depict verified data.
3. Review content, lettering, faces, geometry and factual claims. A convincing
   illustration is not evidence that a circle packing or plotted result is valid.
4. Save original artwork under `book-design/curated/assets/art/` with provenance.
   Store approved print derivatives separately and update `print-assets.json`.
5. For an interior image, create a reviewed `art.json` entry with a unique passage
   anchor. Update `layout.json` only where a new treatment is needed.
6. Confirm Git LFS tracking, source and output checksums, and 300 PPI at actual
   placed size. Retain relevant source archives outside Git when appropriate.
7. Build with `--preview --strict-art`; inspect changed pages and facing spreads.
   Passing mechanical checks does not replace visual review.
8. Mark the corresponding brief complete only when the accepted image is selected
   by the build and inspected in the resulting PDF.

Printer-specific output conversion and physical proof approval happen after the
printer is selected. Do not apply an arbitrary CMYK conversion to RGB masters.

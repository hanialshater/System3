# Print artwork pass — 27 September 2026

Completed against the integrated local main manuscript. No manuscript text changed in this pass.

- Enhanced 13 covers/openers from 1024 × 1536 (170.67 PPI at 6 × 9 inches) to 2048 × 3072 (341.33 PPI).
- Used the authorized faithful local upscaler: Real-ESRGAN animevideov3-x2 through NCNN CPU, blended 40% restoration with 60% original Lanczos interpolation. This is upscaled artwork, not newly captured detail.
- Preserved all originals. Verified all 13 source and derivative checksums and embedded sRGB profiles. Reviewed every derivative visually, with detailed original/enhanced comparisons of lettering, faces and architectural detail.
- Selected derivatives in `book-design/curated/print-assets.json`; method and reproduction instructions are in `book-design/curated/PRINT-ART.md`.
- Retained the already adequate Chapter 4 opener and 88 interior images. Eliminated additional JPEG encoding during PDF composition; all 102 embedded image streams use lossless Flate compression.
- Rebuilt `output/pdf/System3_Curated_6x9.pdf`: 342 pages, 395,683,571 bytes, 2,266 verified text blocks, 88 interior illustrations, 14 covers/openers and 167 notes.
- All 102 source and embedded placements meet the 300-PPI target; actual minimum is 300.0 PPI, with zero low-resolution placements. The audit measures pixels at placement size, not captured optical detail.
- All 12 pipeline tests pass; build freshness check passes. Final cover, chapter and interior samples were visually inspected. Existing layout remains intact.

The output is a 6 × 9 RGB print-resolution proof. Printer-specific bleed, spine/binding geometry, output profile and PDF/X requirements remain pending printer selection, followed by a physical proof. Seven existing manuscript design directions remain recorded separately in the build report; they are not missing or failed existing artwork placements.

Changes and artwork remain uncommitted. No push or merge was performed in this pass.

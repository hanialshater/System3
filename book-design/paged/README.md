# Chapter 5 — Paged.js composition proof

An on-demand 6×9 proof of flexible text masks, individual artwork silhouettes, transparent cutouts and deliberate crops at the final page edge. The full-book curated builder remains separate. The manuscript is never edited by this renderer.

The original full-image chapter opener is locked. Do not crop it, replace its typography, cover its lettering, or add a fade. The author's correction also rules out blur as a way to make boxed artwork feel immersive: solve the composition through scale, placement, transparency and appropriate edge crops.

## Build and review

Use Node 24+, Chromium/Chrome, and the Python environment described in [../PDF.md](../PDF.md). First install the pinned browser packages:

```sh
npm --prefix book-design/paged ci
node book-design/paged/build.mjs --status
node book-design/paged/build.mjs
```

The build writes `output/pdf/chapter-05-paged/System3_Chapter05_Paged.pdf`, a self-contained HTML preview, `validation.json`, and `build-state.json`. The HTML embeds fonts, art and Paged.js and can be opened offline in Chrome. Use **Text masks** to see protected contours and **Facing pages** to inspect spreads. These controls and overlays do not print. Page 1 is a right-hand cover; 2–3 form the first spread. A URL ending in `#page-8` jumps to that page after pagination.

For an in-app browser preview, serve only the output directory:

```sh
.venv-pdf/bin/python -m http.server 8765 --bind 127.0.0.1 --directory output/pdf/chapter-05-paged
```

Open `http://127.0.0.1:8765/System3_Chapter05_Paged.html`.

Unchanged inputs and intact outputs skip rebuilding. `--force` rebuilds deliberately; `--prepare` writes only a candidate HTML in `tmp/pdfs/paged-ch5/` for layout debugging. Neither command starts a watcher or a scheduled build. Override executable discovery with `SYSTEM3_CHROME` and `SYSTEM3_PYTHON` when needed. A lock prevents simultaneous builds; after a crashed process, remove its `.build-lock` only once that process has stopped.

## What controls the composition

`chapter-05.json` assigns all 18 inherited illustrations a treatment and, for the nine wrapped scenes, a contour profile. Text anchors come from `../curated/art.json`; a chapter-specific `after` override can attach a composition to a more appropriate passage without changing the full-book design. An anchor must resolve uniquely; missing or ambiguous anchors stop the proof. The historic source-page number is discarded before layout.

- **Contour:** the image enters from the outer margin. A transparent float with CSS `shape-outside` reserves a protected region. Live paragraphs occupy the connected space outside that contour, including quiet areas inside the float's rectangular bounds. Coordinates are percentages of the float, with 10 px of clearance. Left and right profiles are independent; the artwork itself is never mirrored.
- **Wide:** an illustration extends beyond the outer trim edge, with a silhouette chosen for that artwork.
- **Landscape / detector / closing:** a complete page composition reserves text space above an enlarged scene that crosses the page edges and continues through the bottom trim. These intentional full-width exceptions have their own text-clearance check.

The illustration silhouette and wrapping contour are separate layers. A `silhouette` path clips the artwork without blurring it; `cutout` points to an RGBA version whose natural painted edge supplies transparency. `bleed` controls the deliberate amount cropped beyond the outer page edge. `artTop`, `sceneHeight` and `reserve` allow the globe to rise into a passage instead of occupying a fixed side thumbnail. `proof.css` controls type, page margins and spacing; `layout.js` composes the scenes. Body paragraphs stay intact to avoid isolated carryover lines in this Paged.js version.

The opener uses `cover-078.png` in full, edge to edge, with its original lettering. The current manuscript heading and subtitle remain in the body. The build checks the opener source and full-page dimensions.

Selected transparent assets in [assets/](assets/) were prepared with the built-in image editing tool from the original illustrations. The originals remain in `curated/assets/art/`. [edits.json](assets/edits.json) records the exact prompts, inputs and saved output paths. They are edited derivatives, not claims of pixel-identical background removal. No raster blur or generic rectangular opacity fade is applied by this renderer.

## Verification and scope

Every build checks all source blocks and notes in reading order in the paginated DOM, verifies the PDF's manuscript character inventory, selectable text, links and 6×9 trim, and checks text bounds. It verifies the original opener and the final page side, intended crop and float direction of every composition. Word boxes must remain outside the protected polygons; each contour must demonstrate actual text flow into its open area, with at least 230 CSS px available at its narrowest point. Full-page scenes must leave at least 12 CSS px between the text and the image frame. The reveal must begin a new page.

Inputs, fonts, artwork, cutouts, masks, code and runtime versions participate in the freshness hash. Inputs are checked again before publication. Failed validation retains the previous successful proof. Mechanical checks complement visual inspection, especially where a new subject needs a different contour or crop.

This is a chapter design proof based on existing illustrations, with selected transparent derivatives. The 16 manuscript visual/diagram directions remain outstanding, including the new science-to-agents explanatory artwork. The contour vocabulary currently supports a connected reading region beside a float, not arbitrary disconnected text islands. Review other page-side variants after future edits. The full book's pagination and printer-specific bleed/binding remain a later integration pass.

Consult `validation.json` for current page numbers, artwork placements and checks. The chapter has 174 manuscript blocks and 23 notes; the layout may change the page count. Page numbers are review references, never placement anchors.

# System 3 Book Studio

A Paged.js editor for the actual chapter Markdown in this repository. Run `npm ci && npm run dev` inside `editor/`. Build with `npm run build`; deploy `editor/dist` as a static Vercel site, or configure the Vercel project root as `editor` (Vite framework).

- Chapters 1–6 are bundled from the repository at build time. Chapter 5 section 2 has two separate illustration assets for the initial reflow test.
- Edit section Markdown, reorder sections by drag or arrow buttons, change typography and page size, and anchor illustrations after a passage. Full chapter or selected-section preview. Print / Save as PDF uses the live Paged.js layout.
- Click an illustration in the proof (or Edit on canvas in Artwork) to open the Konva artwork editor: crop with handles, resize on the page, rotate, flip, adjust brightness/contrast/saturation/opacity, grayscale, undo/redo, reset, or cancel. Adjustments are saved as normalized parameters in the layout JSON and re-rendered for the proof/PDF; source images are never overwritten.
- Text and layout save locally by chapter. Download both draft files at any time.
- GitHub pull reads a chosen branch. Save uses a fine-grained token with **Contents: read/write** on **hanialshater/System3**, held in memory only and sent directly to api.github.com. No credentials are embedded in the site or localStorage.
- Saves atomically commit the chapter Markdown and `book-design/editor/chapter-NN.json` to a review branch. Remote manuscript/layout changes and concurrent branch advances are rejected; main/master writes are disabled in the editor. Merge the review branch on GitHub when ready.
- Layout files version typography, section breaks, and passage anchors separately from manuscript content. If a section is renamed after a reload or an anchor passage is deleted, the editor reports detached artwork and offers reattachment.

## Prototype boundaries

This is an editable reconstruction, not a conversion of the raster PDF. Only the two supplied clean illustrations are installed. Footnotes are rendered as notes following each section. It does not yet provide arbitrary image uploads, direct canvas text editing, collaborative cursors, automatic conflict merging, or professional prepress checks. The PDF button exports the current preview scope. Local drafts are browser/device-specific until saved to GitHub.

## Checks

`npm test` checks source round trips and GitHub conflict/concurrency handling. Browser QA must also exercise pagination after added text, typography changes, art placement, and full chapter export.

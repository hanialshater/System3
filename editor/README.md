# System 3 Book Studio

A Paged.js editor for the actual chapter Markdown in this repository. Run `npm ci && npm run dev` inside `editor/`. Build with `npm run build`; deploy `editor/dist` as a static Vercel site, or configure the Vercel project root as `editor` (Vite framework).

- Chapters 1–6 are bundled from the repository at build time. Chapter 5 section 2 has two separate illustration assets for the initial reflow test.
- Edit section Markdown, reorder sections by drag or arrow buttons, change typography and page size, and anchor illustrations after a passage. Full chapter or selected-section preview. Print / Save as PDF uses the live Paged.js layout.
- Click an illustration in the proof to select it. Drag its move handle to a paragraph (left/right drop zones wrap text); drag its corner to resize. Layout & art provides width, height, text gap, before/after placement, paragraph anchor, and destination section controls. Text reflows after each placement. Select text in the proof to add or remove a page break before its paragraph.
- Double-click artwork, or choose Edit art, to open the Konva artwork editor: crop with handles, resize on the page, rotate, flip, adjust brightness/contrast/saturation/opacity, grayscale, undo/redo, reset, or cancel. Adjustments are saved as normalized parameters in the layout JSON and re-rendered for the proof/PDF; source images are never overwritten.
- Comments attach to selected prose, illustrations, or sections. Threads support named replies, resolve/reopen, navigation to the anchor, and indicators in the proof. Comment content is escaped, and editor controls/comments are excluded from print. Names are self-entered labels, not authenticated identities. AI can later consume the structured thread data; no AI participant is connected yet.
- Text, layout, and comments save locally by chapter. Download both draft files at any time.
- GitHub pull reads a chosen branch. Save uses a fine-grained token with **Contents: read/write** on **hanialshater/System3**, held in memory only and sent directly to api.github.com. No credentials are embedded in the site or localStorage.
- Saves atomically commit the chapter Markdown and `book-design/editor/chapter-NN.json` to a review branch. Independent comment threads and replies merge with the latest remote discussion. Remote manuscript/layout changes, conflicting thread edits, and concurrent branch advances are rejected; main/master writes are disabled in the editor. Merge the review branch on GitHub when ready.
- Layout files version typography, section/paragraph breaks, figure geometry, artwork adjustments, comments, and passage anchors separately from manuscript content. If a section is renamed after a reload or an anchor passage is deleted, the editor reports detached artwork and offers reattachment.

## Prototype boundaries

This is an editable reconstruction, not a conversion of the raster PDF. Only the two supplied clean illustrations are installed. Footnotes are rendered as notes following each section. It does not yet provide arbitrary image uploads, direct canvas text editing, real-time collaborative cursors, automatic manuscript/design conflict merging, or professional prepress checks. The PDF button exports the current preview scope. Local drafts are browser/device-specific until saved to GitHub. For collaboration, everyone saves to and pulls from the same review branch. This is asynchronous GitHub collaboration, not a live multiuser session. Pull replaces the local chapter draft; save or download first if it contains unshared work.

## Checks

`npm test` checks source round trips, layout/comment serialization, independent discussion merging, and GitHub conflict/concurrency handling. Browser QA must also exercise pagination after added text, typography changes, art placement, and full chapter export.

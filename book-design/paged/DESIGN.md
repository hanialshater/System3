# Flexible text masks and immersive page composition

Design direction discussed on 2026-09-20. The [Chapter 5 Paged.js proof](README.md) implements this brief for review. This document records the experiment's rationale; its README describes implemented behavior. The curated builder remains the full-book renderer. Builds happen only when requested.

Author's correction after the first proof: preserve the original chapter opener as the complete image, untouched. Interior graphics must feel part of the page through scale, silhouette, transparent backgrounds and deliberate edge crops. Blurring or fading a rectangular image is not the solution. The second proof removes the blanket fades and uses individual masks and selected transparent derivatives.

## What “grid” means here

The author means a flexible mask describing where text is allowed, not a rectangular column grid. A paragraph may occupy quiet space within an illustration's rectangular bounds and follow a broad contour around its subject. Image bounds alone do not determine the text region.

Keep three related descriptions for each composition:

- The artwork placement and crop, including the subject that must remain visible.
- A text-permitted region, with clearance from faces, hands, significant objects, labels and visually busy areas.
- A separate artwork silhouette or transparent cutout that lets the paper surround the painted subject. SVG gradients may be useful for a specific transition, but must not substitute for a composed image boundary.

The text stays live and selectable. The image mask never hides, clips or erases text to simulate wrapping. Preserve significant subjects inside a silhouette; inspect heads, hands and labels after cropping. Maintain generous, readable line lengths and smooth changes in width; simplify a contour when it would make reading awkward. Avoid sending one paragraph through disconnected pockets of space.

## Facing pages

Resolve placement from the final physical page side after pagination. In this left-to-right book, right-hand/odd pages generally carry art at the right outer edge; left-hand/even pages at the left outer edge. Protect the gutter. Centered art is an intentional exception when the composition or explanatory figure benefits from it.

Choose the crop and position first, then apply the corresponding text and blend masks in the same coordinate system. Left/right variants must continue to protect the actual subject. Moving art to the opposite edge does not automatically authorize mirroring faces, writing or diagrams.

The initial design identified historical source-page parity as a problem. The Paged.js proof discards that parity and checks placement against the final page side.

## Pacing and immersion

Use quiet reading pages, images entering from an outer edge, lower-corner scenes and occasional larger scenes extending to page edges. Reserve the most immersive compositions for narrative moments that earn the space. Review facing-page spreads as well as individual pages. Preserve the manuscript, its narrative order and Chapter 5's reveal break.

## Implemented proof and remaining evaluation

Paged.js handles pagination and facing-page templates in the Chapter 5 proof. `chapter-05.json` stores the artwork treatment and contour overrides beside references to the curated anchors. The preview exposes text masks and facing pages; those controls do not print. See the README for the implemented contour and cutout behavior.

CSS `shape-outside` can wrap text around nonrectangular floated exclusion regions. Translate the permitted region into suitable exclusions where possible. An arbitrary SVG mask alone does not create text flow, and arbitrary internal holes require more layout work. Prove the chosen contour behavior across page breaks in the actual Paged.js/Chromium export before adopting it for the book.

The Chapter 5 proof is the existing test case. Before adopting it across the book, recheck it against the current manuscript: font fidelity, reading order, text preservation, notes, links, mask alignment, line lengths, cutout edges and silhouettes. Compare it with the current full-book proof. The separate science reveal now follows Chapter 5 in the full-book reading order; do not silently append it to a chapter-only export.

## Build behavior

Continue building only when requested and inputs have changed. Include manuscript, art, masks, templates, fonts and renderer versions in the freshness check. Offer a chapter proof for visual iteration, then a full-book build when needed. Retain the last successful PDF if validation fails.

## References

- [Paged.js facing-page rules](https://pagedjs.org/en/documentation/5-web-design-for-print/)
- [Paged.js named page templates](https://pagedjs.org/en/documentation/8-named-page/)
- [Paged.js layout hooks](https://pagedjs.org/en/documentation/10-handlers-hooks-and-custom-javascript/)
- [CSS shape-outside](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
- [CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)

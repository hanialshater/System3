# Design Spec — System 3 (stage-1 draft system)

One book, one system. The reference mockups sampled two different type worlds;
this spec picks one and the renderer enforces it. The stage-1 fonts are
draft stand-ins available in the build environment; final faces are a
designer decision recorded here when made.

## Page

- Trim: 6 × 9 in. Margins: 0.75 in outer, 0.85 in inner, 0.7 in top (below
  running head), 0.75 in bottom.
- Paper: warm cream `#f7f2e8`. Ink: near-black `#26221a`. Accent: deep blue
  `#1f3a5f` (headings, pull quotes, running heads).
- Running head: letterspaced uppercase, 8.5 pt, accent color —
  `CHAPTER N · TITLE` outer, folio opposite. No running head on opener pages.

## Type (draft faces)

- Body: Bitstream Charter, 10.5 pt / 15 pt leading, justified, hyphens on.
- Section heads: Charter italic bold, 14 pt, accent blue, space before 1.5 lines.
- Chapter opener: number as letterspaced caps over large title (handwritten
  display face is a stage-2/3 decision; draft uses Charter bold caps).
- Block quotes: indented, italic. Code: DejaVu Sans Mono 8.5 pt on a
  faint panel. Tables: light rules only, no zebra striping.

## Art-slot vocabulary

Every slot is typed; stage-2 redesigns should express themselves in this
vocabulary (or propose extending it).

| Type | Geometry | Text behavior |
|---|---|---|
| `opener-plate` | own page, full-bleed art, typeset number/title/subtitle over it | none |
| `figure-frame` | column-width framed figure + caption | breaks text |
| `corner-bleed` | bottom-outer corner, up to 55% width × 45% height | wraps around |
| `margin-vignette` | outer margin float, ≤ 38% width | wraps around |
| `spot` | small inline image, centered, ≤ 1.5 in tall | breaks text |
| `pull-quote` | accent rule + italic accent text, 1.2× body size | breaks text |

## Hard rules (renderer-enforced, non-negotiable in stage 2)

1. Chapter numbers, titles, captions, and any words the reader must read are
   **typeset**, never part of generated art. Art with baked-in text is rejected.
2. Minimum measure beside any float: 45 characters. If a wrap would go
   narrower, the slot shrinks or moves.
3. A pull quote may not appear on the same page adjacent to the paragraph
   containing its sentence; the manifest anchors it at least two blocks away.
4. Manuscript text is read-only for the design pipeline. Layout adapts to
   text, never the reverse.
5. No infographic checklists (✓/✗ benefit lists). Full-page plates carry at
   most a typeset title block. The book argues against the deck genre; the
   design does not get to reintroduce it.

## Art direction

Briefs live in the manifests; style continuity rules live in
`resources/art-direction/` (old visual world of paper, ink, workshops and
instruments, gradually inhabited by machine intelligence; recurring robots,
doors, landscapes; no explanatory labels inside images).

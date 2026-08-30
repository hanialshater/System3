# Book Design Pipeline

Three stages, three owners, clean contracts between them. This is the book's own
architecture applied to its production: a cheap consistent proposer, a creative
critic, and a human evaluator who merges.

## Stage 1 — Programmatic draft (this repo, deterministic)

**Input:** chapter markdown (source of truth) + a per-chapter layout manifest
(`manifests/chapter-NN.json`) declaring art slots and pull quotes.

**Output:** paginated 6×9″ draft pages — a PDF for reading and one PNG per page
for stage 2 — rendered by `render.py`. Real art is placed where assets exist
(chapter openers); everywhere else the renderer draws a placeholder frame
containing the slot id and the art brief, so every page already shows its final
geometry.

Rules the renderer enforces (see `design-spec.md`): one type system, chapter
numbers and titles always typeset from the manuscript (never baked into art),
minimum text measure next to floats, pull quotes never adjacent to their own
source paragraph.

**Run:** `python3 book-design/render.py 4` (chapter number) → `book-design/out/`.

## Stage 2 — AI redesign (creative pass)

**Input:** the stage-1 page PNGs + the chapter text + `redesign-brief.md`
(the prompt contract). The redesigner may move slots, change slot shapes,
propose new vignettes, adjust hierarchy — anything except: changing the
manuscript text, baking typeset text into art, or violating the hard rules in
the brief.

**Output:** redesigned page mockups (like the reference mockups this pipeline
was started from) **plus, for every change, an edited copy of the manifest**
expressing the redesign in slot vocabulary wherever possible. Changes that
cannot be expressed in the vocabulary are the interesting ones — they become
proposals to extend the vocabulary, not one-off pages.

## Stage 3 — Human merge (the designer decides)

The designer sees both versions per page: the deterministic draft (correct,
consistent, dull in places) and the AI redesign (alive, occasionally illegal).
They merge by editing the **manifest and the spec**, not individual pages —
so every accepted idea becomes reproducible across the book, and the final
book can always be re-rendered from source. A page that can only exist as a
hand-tweaked file is a bug.

Art generation runs in parallel against the briefs (see
`resources/art-direction/`), and finished art replaces placeholder frames by
filename in the manifest. Chapter renumbering never invalidates art, because
numbers and titles live in type, not in the image.

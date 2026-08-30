# Stage-2 Redesign Brief (prompt contract)

You are redesigning pages of *System 3: Towards Fluent Autonomy*. You receive:
the stage-1 draft page images (`out/pages/chNN-pXX.png`), the chapter text
(`chapters/NN-*.md`), the layout manifest (`manifests/chapter-NN.json`), and
the design spec (`design-spec.md`). The reference aesthetic is the book's
existing art direction (`resources/art-direction/`): an old visual world of
paper, ink, stone, workshops and instruments, gradually inhabited by machine
intelligence, in warm watercolor on cream.

## What you may do

- Move, resize, reshape, merge, split, add or delete art slots.
- Change hierarchy, pull-quote selection and placement, opener composition.
- Let art bleed, wrap, or interlock with the text in ways the draft cannot.
- Propose page-specific moments (a dotted line crossing the gutter, a figure
  looking at a pull quote) — the delightful illegal things.

## What you may not do

1. Change, cut, or paraphrase the manuscript text. Layout adapts to text.
2. Bake readable text into artwork. Numbers, titles, captions, labels are
   typeset. (Diegetic scribbles inside a drawing are fine if illegible or
   incidental.)
3. Reduce any wrap column below ~45 characters.
4. Place a pull quote adjacent to the paragraph containing its own sentence.
5. Add infographic checklists, ✓/✗ benefit columns, or framework-deck
   furniture. The book argues against that genre.
6. Introduce a second type system. One book, one system; propose changes to
   the system itself in notes, not silently on a page.

## What you must return, per redesigned page

1. The redesigned page image.
2. A machine-readable delta: the edited slot entries (same JSON vocabulary)
   that reproduce your layout — or, where the vocabulary cannot express your
   idea, a named proposal for a new slot type with its geometry and text
   behavior. One-off unreproducible pages are rejected in stage 3.
3. Two sentences on intent: what the page now does that the draft did not.

The human designer merges stage-1 and stage-2 by editing the manifest and the
spec, then the chapter is re-rendered. If your best idea survives that round
trip, it becomes part of the book's design language, not just one page.

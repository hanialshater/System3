---
name: art-direction
description: Art direction and image QA for an illustrated book (System 3's watercolor-and-ink edition) — judging whether each image carries the argument, deciding keep / replace / add per chapter, writing generation briefs, keeping one visual world (robot bible, palette, composition families, sequence), separating openers from figures, and checking that placements still resolve after text edits. Use whenever the user shares an illustrated proof, chapter openers, generated images or art briefs, asks "evaluate the art", "which images to replace", "write a brief", "art for chapter N", or after any text pass that might have moved or deleted image anchors.
---

# Art direction

The visual language is settled: warm cream paper, muted blue/ochre watercolor, fine ink, a brass robot civilisation, generous air. **Stop searching for a different style.** The work is to simplify, standardise, sequence, and surgically correct the few images whose metaphor is weaker than the chapter.

## The test every image has to pass

**Two layers:** the image is memorable, and the memorable part is the argument. Draw the sentence, not the mood. The Chapter 4 Alberto-and-penguins image is the standard the rest must meet.

Images that pass: the nurse holding the tray while three consultants huddle; five robots in five coats reading one printout; objections fed into a machine stamped NOTED; the striped sea floor under a magnetometer; the review text box as a warehouse with a hundred people in it.

Images that fail: argument pages given filler (Kitcher gets a notebook and a coffee cup; the YAML pattern gets books and pens; Duhem gets a mouse and a magnifying glass); a device used twice (labelled books on consecutive pages: once is a device, twice is a template); a photoreal element in a watercolor world.

## Workflow

1. **Inventory.** Run `scripts/art_audit.py book-design/curated/art.json chapters --order book-design/curated/book-order.json`. It mirrors the renderer: anchors must match exactly one paragraph, or the image is silently omitted. Fix broken anchors before judging the art; a picture the reader never sees can't be good or bad.
2. **Judge per chapter** with the scorecard in `references/rules.md` (style consistency, argument-carrying, text–image fit, layout, completeness; "as a proof" and "as art" scored separately).
3. **Decide keep / replace / add.** For each replace or add, name the exact sentence the image should draw and what to show ("draw the bronze measure with the edict cast into its side", not "something about Qin").
4. **Write briefs** with `references/brief-template.md`. Generate openers with an empty title zone; typography goes in the layout, not the painting.
5. **Accept art** only through the repo's `resources/art-direction/generation-checklist.md`: provenance, unique passage anchor, 300 PPI at placed size, `--preview --strict-art` build, visual inspection of changed pages and spreads.

## Placement rules

- 8–10 images per argument chapter, full width, never cropped, never beside a column narrower than 55 characters.
- At section breaks, not mid-paragraph; never leave text ending mid-paragraph above a picture.
- Anchor to a unique passage, never a page number. Re-run the audit after every text pass: cuts delete anchors.

## Sequence rules

- Four composition families: expansive landscapes (emergence), workshops/interiors (executable machinery), monumental architecture (institutions), documentary/collage (evidence). Ch 13 is the surreal exception.
- Vary the camera. Too many "human from behind, open vista, distant destination, central vertical" compositions make eleven posters, not a sequence.
- The book becomes progressively more human: machines and systems early, institutions in the middle, the human returning from Layer 4, robots almost gone by Ch 11.
- Openers: emotional, metaphorical, painterly. Figures: analytical, restrained, vector-clean. Photographs only when contact with reality is the point. Don't turn diagrams into paintings, and label a schematic as schematic; a convincing illustration is not evidence that a result is valid.
- Tone: warm, humane, strange, intellectually serious — not "adorable robots learn philosophy". Not every robot smiles.

## Copyright and likeness

Keep references to copyrighted characters unrecognisable (Senku stays generic-haired; no manga fan service). No real people's likenesses unless the image is documentary and licensed.

## Files

- `scripts/art_audit.py` — placements, density, broken or ambiguous anchors, briefs left in comments.
- `references/rules.md` — scorecard, robot bible, worked Chapter 5 keep/replace/add example.
- `references/brief-template.md` — generation brief format.

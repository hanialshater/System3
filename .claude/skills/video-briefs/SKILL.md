---
name: video-briefs
description: Write or update video-generation prompts for this book's chapters, for NotebookLM Video Overviews or similar tools (Veo, Sora, Runway, a human animator). Use when asked to create, revise or check video prompts, video briefs, storyboards or NotebookLM prompts for a chapter or the whole book, or after a chapter edit changes its key scenes or lines.
---

# Video briefs for System 3

A video brief tells a generator what a chapter is *about*, which moments carry it, which
lines must survive, what is imagined, and how it should look. A list of headings is not
enough: a video can follow a chapter's order and still miss its point.

In this repo the briefs are generated, not hand-written:

- Generator: `prompts/build_notebooklm.py`
- Output: `prompts/notebooklm/` (one brief per numbered source, plus `book.md` for the whole book)
- Visual language: `resources/art-direction/` (the selected openers' watercolor-and-ink treatment)

Edit the generator's data, regenerate, and check. Do not hand-edit the generated `.md` files;
the next regeneration overwrites them.

## Step 1: Read the source

Read the whole chapter in `chapters/`, its section of `chapters/appendix-references.md`,
and its row in `chapters/appendix-note-on-evidence.md` (which says what is lived, reported or
imagined). Read `resources/editorial/easter-egg-register.md` for seeds and payoffs.

## Step 2: Fill the chapter's entry

Each numbered source has an entry in `CORE` and `LOOK` in the generator.

| Field | What it holds | Test |
|---|---|---|
| `idea` | The one sentence the video must land | Could a viewer repeat it after watching? It states this chapter's claim, not the book's. |
| `moments` | 4–8 scenes, people or images that carry the idea | Each is concrete and in the text. Prefer the author's lived scenes and the reader-praised jokes. |
| `keep` | Exact lines to say word for word | 1–4 lines, copied verbatim. `--check` fails if one disappears from the chapter. |
| `labels` | What is imagined, reported or proposed | Every invented person or company is named as imagined. Reported incidents follow the chapter's chronology and qualifications. |
| `LOOK` | One visual motif for the chapter | It fits the chapter's place in the arc below and its composition family. |

`RULES` holds per-chapter guardrails (things a video must not claim). Update a rule when the
chapter changes so it no longer describes old text.

## Step 3: Keep the book's look

`STYLE` and `STYLE_SHORT` in the generator carry the book's visual language. Do not invent a
new one. In short:

- restrained watercolor with fine ink on warm cream paper; visible blooms and paper grain;
- a muted palette of Prussian blue, ochre, olive, warm gray and parchment, with brass for machines;
- a retro-futurist field notebook, with machines placed inside an inherited human world;
- robots in one design family with neutral faces; warm, humane, strange, serious; never cute, neon or cyberpunk;
- diagrams as clean thin ink, marked schematic unless they show real data;
- real photographs and documents shown unaltered.

Across the book the visual arc runs from machine to system to institution to culture to human.
Early chapters may hold machinery, people return to the centre from the desire layer on, and
by the last chapters the robots almost disappear. Vary the camera between neighbouring
chapters, using these families: landscape, workshop or interior, monumental architecture,
documentary.

## Step 4: Protect what must stay

- **Chapter 13 is a fable and is protected.** Its brief explains nothing, and no twist appears,
  in words or images, before the text reveals it.
- Never explain a seed's payoff (see the easter-egg register).
- In the whole-book brief, "We call it science." comes only after Part II.
- Never invent dialogue, numbers, results, quotations or experiments. Circle packings and
  plotted results are schematic unless the chapter gives the real data.
- Attribute the author's experiences to him; keep his humour.

## Step 5: Regenerate and check

```sh
python3 prompts/build_notebooklm.py          # writes prompts/notebooklm/
python3 prompts/build_notebooklm.py --check  # fails on stale briefs or a missing kept line
```

The generator needs `markdown-it-py` (`pip install markdown-it-py`). Run the check after any
manuscript edit as well. If it fails because a kept line changed, update `keep`; do not
change the manuscript to satisfy the brief.

## Using a brief

- **NotebookLM:** add the chapter's manuscript file and the reference appendix as sources.
  Paste the brief's *Video prompt* block into the customization field. If a Watercolor visual
  style is offered, choose it. Add the chapter's opener illustration as a source if you have it.
- **Shot-based tools (Veo, Sora, Runway and similar):** turn each item in *Moments to show*
  into a shot. Each shot gets one sentence describing the scene, the chapter's `LOOK` and
  `STYLE_SHORT` appended, and no on-screen text beyond sparse labels. Narration comes from the
  chapter, with the *Lines to keep* read verbatim.

## Report

When asked to write or revise briefs, finish with:
- which entries changed;
- the `--check` result;
- anything you could not verify in the source, such as an opener image you could not view.

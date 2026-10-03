# NotebookLM video briefs

Use the chapter's current manuscript, including its notes, as the content source.
Select its brief as production guidance and paste the brief's video prompt into
the customization field. These files are source-derived outlines, not completed
shot-by-shot storyboards. No video generation is triggered by this repository.

Before use:

```sh
.venv-pdf/bin/python prompts/build_notebooklm.py --check
```

After deliberate manuscript changes, regenerate the pack and review its source order:

```sh
.venv-pdf/bin/python prompts/build_notebooklm.py
```

Each chapter brief now carries the book, not only its headings: the idea the video
must land, the moments to show, lines to keep word for word, and which examples are
imagined, reported or proposed. `--check` fails if a kept line disappears from the
manuscript, so edit `CORE` in `build_notebooklm.py` when you change one of those lines.
`book.md` is a whole-book overview brief that follows both threads and holds the
science reveal until after Part II.

The generator uses Markdown parsing so headings inside code examples do not become
scenes. It strips editorial and artwork-production comments. `sources.json`
records source and brief hashes; a passing check establishes freshness, not
factual verification or editorial approval.

| Source | Brief |
| --- | --- |
| Whole book | [book](book.md) |
| Preface | [preface](preface.md) |
| Chapter 1 | [chapter-01](chapter-01.md) |
| Chapter 2 | [chapter-02](chapter-02.md) |
| Chapter 3 | [chapter-03](chapter-03.md) |
| Chapter 4 | [chapter-04](chapter-04.md) |
| Chapter 5 | [chapter-05](chapter-05.md) |
| Chapter 6 | [chapter-06](chapter-06.md) |
| Chapter 7 | [chapter-07](chapter-07.md) |
| Chapter 8 | [chapter-08](chapter-08.md) |
| Chapter 9 | [chapter-09](chapter-09.md) |
| Chapter 10 | [chapter-10](chapter-10.md) |
| Chapter 11 | [chapter-11](chapter-11.md) |
| Chapter 12 | [chapter-12](chapter-12.md) |
| Chapter 13 | [chapter-13](chapter-13.md) |
| Closing coda | [Scaffolds](scaffolds.md) |

Part pages, the science reveal, interlude and appendices are not silently appended
to chapter adaptations. Select them separately if a later video request calls
for them. Earlier bespoke storyboards remain recoverable from commit `13d415c`;
recheck their details before reusing any scene.

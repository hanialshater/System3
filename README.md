# System 3: Towards Fluent Autonomy

*Trust Chains, Agent Autonomy, and the Architecture of AI That Works*

By Hani M.M. Al-Shater

The book follows emergence from solutions into methods, workflows and institutions.
Its central claim is that, as we build autonomous AI, we keep rediscovering science
as its architecture. The manuscript combines reported work, experiments, arguments,
proposed designs and a fictional alternative ending.

## Read and edit

- [Manuscript order](book-design/curated/book-order.json): the complete 31-file reading sequence.
- [Preface](chapters/00-preface.md): begin here.
- [Note on evidence](chapters/appendix-note-on-evidence.md): what has been run, argued, designed or imagined.
- [What System 3 Contributes](chapters/afterword-what-this-book-proposes.md): three explicit contributions, their relationship to contemporary philosophy of science and agent architecture, and how they could be tested.
- [The Ideas Behind System 3](chapters/appendix-ideas-behind-system-3.md): a named summary of philosophy of science and the book's other intellectual sources.
- [The Zen of System 3](chapters/appendix-zen-of-system-3.md): the book’s principles, from emergence and inquiry to human purposes.
- [Working spine and editorial guidance](resources/editorial/working-spine.md): structure, voice and protected narrative connections.
- [Narrative seed register](resources/editorial/easter-egg-register.md): run `bash resources/editorial/check-eggs.sh` after manuscript edits.

Chapters 6-12 remain works in progress. Chapter 13 is protected. Author-review
comments remain where acceptance has not been recorded; a repository cleanup is
not an editorial sign-off.

## Build

[PDF.md](book-design/PDF.md) documents installation and the on-demand illustrated
build. Reusable artwork is in Git LFS. On a new clone, install Git LFS and run
`git lfs install` followed by `git lfs pull`.

```sh
.venv-pdf/bin/python book-design/pdf.py status
.venv-pdf/bin/python book-design/pdf.py build --preview --strict-art
.venv-pdf/bin/python book-design/render_back_cover.py output/pdf/System3-back-cover.pdf
```

The full-book PDF is `output/pdf/System3_Curated_6x9.pdf`. The back-cover command
creates a separate one-panel text proof using bundled fonts. Generated PDFs,
previews and temporary builds stay outside Git. Printer-specific bleed, spine,
color conversion and physical proof approval remain pending printer selection.

## Repository map

| Location | Purpose |
| --- | --- |
| `chapters/` | Canonical manuscript, structural pages and back matter |
| [book-design/](book-design/README.md) | Current PDF tooling and the separate Chapter 5 composition experiment |
| [prompts/](prompts/README.md) | Editorial evaluation prompt and one current video-brief pack |
| [resources/art-direction/](resources/art-direction/README.md) | Selected artwork register, acceptance checks and unresolved figure briefs |
| `resources/archive/` | Historical art references; not production inputs |
| `resources/evaluations/` | Dated editorial and build records |
| [File inventory](resources/FILE-INVENTORY.md) | Per-file disposition and results of cleanup |
| [Review queue](resources/REVISIT.md) | Outstanding editorial and production decisions |

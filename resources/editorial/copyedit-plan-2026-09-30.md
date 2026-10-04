# Fix and copyedit plan — 30 September 2026

This plan follows the [chapter readiness evaluation](../evaluations/2026-09-30-chapter-readiness-evaluation.md). The work proceeds in book order. Each chapter is edited, checked, re-evaluated, and moved on from only when it passes its gate. The results are recorded in the [copyedit log](../evaluations/2026-09-30-copyedit-log.md).

## Principles

The house editorial prompt (`prompts/chapter-version-evaluation.md`) governs this pass.

- **Surgery over replacement.** Fix errors, inconsistencies and known overclaims. Cut or fold where a passage repeats work already done. Do not rewrite living prose into tidier prose.
- **Delete and fold before adding.** Where a chapter is too long, prefer deletion and merging to new connective sentences. Added seams are the register this book keeps trying to remove.
- **Protect the voice.** Protected lines, recurring motifs and deliberate jokes stay. The Chapter 1 "cat obsession" paragraph was restored by the author on 27 September and stays.
- **Chapter 13 is protected.** It gets no changes at all, typography included. The author’s text of 21 September 2026 (commit `48fdb6b`) was restored on 4 October, and `check-eggs.sh` fails if the file changes.
- **Author acceptance is not an edit.** The `ASSISTANT EDIT`, `ASSISTANT DRAFT` and `CLAUDE DRAFT` markers record prose waiting for author sign-off. They stay in place and are listed in the PR for a decision. Chapter 9's `SLOT 4` asks for the author's own marketplace case, so it is not filled with an invented one.
- **No fabricated evidence.** No invented figures, experiment details or autobiography. Where a record is missing, the text says so or keeps its present qualified wording.
- **Keep seeds intact.** Run `resources/editorial/check-eggs.sh` after every chapter.

## Style sheet

| Item | Rule | Notes |
|---|---|---|
| Spelling | American (color, behavior, catalog, program, traveled, labeled, fiber, gray, anesthetist, theater) | British spellings survive only in titles, proper names and quotations. "Research program" for Lakatos as well as Kitcher. |
| Quotation marks | Curly (“ ” ‘ ’) in prose | Straight quotes stay only in code, URLs, HTML comments and raw LaTeX. The renderer prints straight quotes as typed. |
| Punctuation with quotes | American: commas and periods inside closing quotes | — |
| Ellipsis | Single glyph (…) | Code keeps `...`. |
| Dashes | Unspaced em dash (—) | Use sparingly. Do not add dashes where a comma works. |
| Serial comma | The manuscript mostly omits it. Remove it from simple word lists; keep it where the last item is a clause or long phrase, or where it helps the reader | No global pass: many series in the book are rhythmic clause sequences. |
| Numbers | Words for one to one hundred in narrative prose | Numerals for measurements, scores, percentages from studies, years, table data, and technical problem statements ("26 circles"). |
| Percent | "percent" in prose, "%" in tables | — |
| Headings | Title case; capitalize words of four or more letters, including prepositions (With, From, Into, Than) | Short prepositions, articles and conjunctions stay lowercase. |
| Bold | Only for a coined term at its first definition, and for Chapter 6's pattern *Therefore* lines | Not for emphasis or slogans. |
| Italics | Titles of books, papers treated as works, ships; words as words; non-English terms | — |
| Cross-references | "Chapter 6"; "the previous chapter" where adjacent | — |
| Compounds | e-commerce, email, dataset, on call (noun) / on-call (adjective), open-ended | — |
| Company and model names | As the source styles them: Claude Code, Claude Opus 4.6, GPT-4, AlphaEvolve, DeepMind, OpenAI | — |
| Citations | Chapter-scoped numbered notes; the number in the text must match the appendix entry | Enforced by `manuscript.validate_references`. If a cited sentence is deleted, its entry moves to "Additional sources" and the chapter is renumbered. |

## Verification gates (every chapter)

1. `bash resources/editorial/check-eggs.sh` shows no confirmed seed failing.
2. The PDF build (`book-design/pdf.py build`) succeeds. This validates reference numbering, unsupported LaTeX, and that artwork anchors are still unique. The target is still 87 placed illustrations and 0 existing placements needing review.
3. `python -m unittest discover -s book-design/curated/tests`.
4. A re-read of the chapter against the house dimensions: voice, discovery, precision, evidential discipline, repetition, pacing, handoff. The chapter moves on only when no copy error remains that I can find, every known issue is fixed or explicitly deferred with a reason, and the score has not fallen on any dimension.

## Pass 0 — mechanical (whole manuscript)

- Convert straight quotes to curly quotes, and three periods to the ellipsis glyph, outside code, comments, URLs and LaTeX.
- Standardize spelling to the style sheet.
- Fix heading-case outliers ("Separate Use from Investigation").

## Chapter plan

| Section | Planned fixes | Deliberately not done |
|---|---|---|
| Preface | Line edit; check the dated status sentence against the fact check. | Content changes. |
| Part pages | Typography. | — |
| 1 | Typography of the restored joke (straight quotes, "..."); line edit. Consider whether four bold slogans should stay: they are the book's named bets (complexity/emergence/capacity), so they stay. | Moving or cutting the cat paragraph (author restored it). |
| 2 | Turn the ten visible `[Missing figure]` placeholders into production comments tagged `DIAGRAM`, so the report tracks them and the reading edition does not print them. Fold the one number found only in a caption (evolutionary search ≈2.45) into the prose. Line edit. | Inventing figures or experiment metadata. |
| 3 | Line edit; heading/term consistency (Deep Mode, Strategic Constraints, Independent Evaluators). | New artifacts or claims about the demos. |
| 4 | Line edit. | — |
| 5 | Line edit; spelling (catalogue, labelled, anaesthetist, theatre, fibre, grey). Visual briefs stay as comments. | Art decisions. |
| Reveal | Typography. | Removing the `ASSISTANT EDIT` marker. |
| 6 | Line edit; "programme" → "program"; heading case; reduce repeated scene-setting where Chapter 5 already introduced a thinker; apply fact-check corrections to the 2026 cases. | Restructuring the Ines thread. |
| 7 | Compress the learning-methods survey by deleting and folding sentences that do not change the store agent's problem. Keep Sutton (Ch 10), CIRL (Ch 9), and the medicine/weapons line (Ch 12), which later chapters refer back to. Renumber notes if needed. | Rewriting the constitution half. |
| 8 | Line edit; fact-check corrections. | Removing instruments that later chapters cite. |
| Interlude | Typography. | Removing the `ASSISTANT DRAFT` marker. |
| 9 | De-bold emphasis. Fold the "Very efficient. / Slightly evil." pair into one line. Line edit. | Filling `SLOT 4`. |
| 10 | De-bold slogans in the middle sections; line edit. | — |
| 11 | Correct the causality overstatement. De-bold. Trim the "not X, it is Y" constructions where two sit in one paragraph. "ecommerce" → "e-commerce". | Changing the design itself. |
| 12 | Correct "ten thousand agents for eighty-eight hours" and its citation; verify the June 2026 access sentence. | — |
| 13 | Nothing. Protected in full, typography included. | Any change. |
| Divider, scaffolds | Typography only. | Any wording. |
| Zen | Typography only. The author revised the Zen on 30 September, after the 27 September critique, and kept "Ground every claim. Trace every source." and "The tongue cannot reach the ear." Both are treated as deliberate maxims. The second is true of the reader's tongue, which is the test Chapter 4 actually sets. | Rewriting the list. |
| Evidence note, illustrations note, references, about | Typography; reference entries changed only where citations move or facts are corrected. | Removing the `CLAUDE DRAFT` marker; employer clearance (author task). |

## Fact checking

Two independent checks run alongside the edit:

- the August–September 2026 events (Fermat, Riemann, Navier–Stokes, the automated alignment studies, the June 2026 access suspension);
- the historical and study claims (Carlini, Chapter 5 history, Alexander, Kohavi, the Chapter 9 studies).

Discrepancies are corrected with the smallest wording change. Claims that cannot be verified from this environment are listed in the log for the author, not silently changed.

## Out of scope for this PR

- Printer, bleed, spine, color profile and physical proof.
- Title and copyright/ISBN pages, dedication, acknowledgments and index.
- Replacement art for Chapter 2.
- Author sign-off decisions.
- Employer clearance.

These remain in [REVISIT](../REVISIT.md).

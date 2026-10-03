---
name: copyedit
description: Copyedit a manuscript to a house style without touching argument or voice — mechanical pass (quotes, ellipses, spelling, heading case, dashes, numbers, compounds, bold), line edits for errors and small factual wording, chapter-by-chapter gates, word-level diff verification, and a log that records what was deliberately not changed and why. For System 3 it applies the house style sheet from the 30 September copyedit plan. Use whenever the user asks to "copyedit", "proofread", "line edit", "fix typos", "make it consistent with the style sheet", "American spelling", or asks for a final text pass before typesetting.
---

# Copyedit

A copyedit fixes errors and enforces the style sheet. It changes no argument and no voice. If a fix needs either, it isn't a copyedit: route it to de-llm, dev-edit, consistency or fresh-claims and say so in the log.

## Principles (from the System 3 plan and log)

- **Surgery, not replacement.** Fix errors, inconsistencies and known overclaims. Don't rewrite living prose into tidier prose.
- **Protected material stays.** Protected lines, recurring motifs, jokes, Chapter 13 (typography only), author-restored passages (the Ch 1 cat paragraph: serial comma removed per house style, wording untouched).
- **Author acceptance is not an edit.** `ASSISTANT EDIT` / `ASSISTANT DRAFT` / `CLAUDE DRAFT` markers and `SLOT`s stay and go on the author's list.
- **No fabricated evidence.** A missing methods trail or record stays missing and is listed; nothing is invented to fill it.
- **"Not done, because…" is part of the job.** A planned trim gets skipped when, on re-reading, each instance is a joke or turn doing work (the Ch 11 "not X, it is Y" lines; Ch 6's philosopher introductions already reduced to one or two sentences tied to the running case). Record the reason.

## Workflow

1. **Read the style sheet** (`references/style-sheet.md`; in the repo, the latest `resources/editorial/copyedit-plan-*.md`).
2. **Lint:** `scripts/style_lint.py chapters` (or `--only quotes,spelling,heading,...`). It skips code, comments, URLs, raw LaTeX and reference titles. The numbers check is noisy by design; read each hit.
3. **Pass 0, mechanical, whole manuscript.** Make substitutions with word boundaries, never bare string replace. Keep tooling in step in the same commit: seed anchors in `check-eggs.sh` and the register, art anchors in `art.json`, cover titles in `provenance.json` all change when quotes or spellings change.
4. **Verify Pass 0 with a word-level diff:** `scripts/word_diff.py before/ after/` (or `git diff --word-diff`). Read every rare change type by eye. This is how "programme → program" turning "programmers" into "programrs" was caught.
5. **Line edit chapter by chapter** in book order. Typical fixes: a phrase that says something false ("everything from the deepest ocean trenches" → "from the creatures of the deepest ocean trenches"), a heading that doesn't match the chapter's term ("The Algorithmic Vortex" → "The Algorithm Vortex"), a number that lives only in a caption moved into the prose, bold demoted to italics for borrowed terms, one-line mini-climaxes folded ("Very efficient." / "Slightly evil." into one paragraph, joke kept), back-references made specific ("which appeared in Chapter 7").
6. **Gate each chapter** before moving on: seeds pass, build passes (reference numbering, art anchors, covers), unit tests pass, a re-read finds nothing further, and no score drops. If citations are deleted, renumber and move the entry to "Additional sources".
7. **Final sweeps:** spellcheck (aspell/codespell) over changed lines; unbalanced emphasis markers; extracted PDF text free of `[Missing figure]`, comment text and the known bad substitutions.
8. **Log** in `resources/evaluations/YYYY-MM-DD-copyedit-log.md`: per section, changes, re-evaluation, status (Closed / Author decision), the "not done because" items, and what remains for the author. Close with: one editor's copyedit does not replace an independent human proofread of the typeset pages.

## Files

- `scripts/style_lint.py` — style-sheet lint.
- `scripts/word_diff.py` — word-level diff with change-type counts.
- `references/style-sheet.md` — System 3 house style.

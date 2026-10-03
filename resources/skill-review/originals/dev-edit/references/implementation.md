# Implementation

How past development edits were made reviewable, reversible and safe for the build.

## The anchored-operations pattern

Edit E/F were written as a script of anchored operations rather than hand edits:
- Every operation is anchored on a sentence from the manuscript and matches it tolerantly (straight or curly quotes, emphasis markers, footnote refs), so it survives typography passes.
- Every operation is **idempotent**: if its result is already present it is skipped. If its anchor is gone it reports FAIL and does nothing.
- Operations carry a **group**, so the author can skip a whole class: `structure`, `prose` (new passages, review first), `notes` (footnotes built only from the author's reference appendix), `apparatus` (reader map, tables, closers), `production` (print defects).
- `--dry-run` reports, `--write` applies, `--skip GROUP` omits.
- Files are found by number prefix (`07-*.md`), so renamed files don't break the script.

Operation kinds that covered everything so far: `replace(anchor, new)`, `insert_after(anchor, text)`, `insert_before`, `delete(text)`, `move(start_anchor, end_anchor, to_file, after_anchor)` with a verbatim check, `add_footnote(key, after_anchor, definition)` with a collision check across all chapters.

For small passes, the de-llm skill's `apply_pass.py` (exact-once replacements with reasons and inline flags) is enough.

## Flags

- `<!-- CLAUDE DRAFT BEGIN (date): what this is, what to check -->` … `<!-- CLAUDE DRAFT END -->` around any new passage.
- `<!-- CLAUDE EDIT (date): one sentence changed. Was: "…". Why. Revert if you prefer. -->` before a changed sentence.
- `<!-- MOVED, NOT WRITTEN: … -->` at the top of moved text.
- `<!-- AUTHOR: … -->` for a question only the author can answer (a real scene, a real run). Use instead of inventing.
- `SLOT n` placeholders for author material. Don't fill them with invented cases.
- Comments inside Markdown tables break the table; put them above it.
- Verify no comment text leaks into the build output.

## What may go in, and what stays out

From the D/E rounds: connective tissue and apparatus go into the manuscript (handoff sentences, part pages, footnotes from the author's own references, a reader map, labels). Any new passage of **argument** stays in `drafts/` until the author writes it. Write hypotheticals as hypotheticals ("Imagine…"), and never let a summary claim more than the records establish (Ch 10's second attempt claimed autonomous workflow assembly the records didn't show).

## Gates after every commit

1. `bash resources/editorial/check-eggs.sh` (confirmed seeds fail, proposed warn).
2. Footnotes: every reference defined, every definition used, no key defined in two chapters. The CI joins chapters into one file; a duplicate key (`[^saussure]` in Ch 4 and Ch 6) silently prints the first chapter's note in both places.
3. Protected files byte-identical: `git diff --stat BASE -- chapters/13-the-prophecy.md chapters/14-scaffolds.md …` prints nothing.
4. Moved text verbatim:
   ```python
   paras=[p for p in removed.split("\n\n") if p.strip()]
   missing=[p[:60] for p in paras if p.strip() not in new_home]
   ```
5. Build the PDF (`book-design/pdf.py build`, or mirror the workflow file list with pandoc + xelatex) and **read the transitions in the built text**: `pdftotext`, then print the pages around each seam. Render new single-line pages to PNG and look at them.
6. `python -m unittest discover -s book-design/curated/tests` and `git diff --check`.
7. Assembly order: every manuscript file appears once in `book-design/curated/book-order.json` and the workflow.

## Commit series

Snapshot the final state, then rebuild a clean series from the base so each commit is one reviewable change and each builds on its own. Verify by applying the series to a fresh clone of the base and diffing against the snapshot. Deliver `git format-patch` output as `.patch` and `.txt`, the changed files, and a short apply guide (`git am`, or the script on any later version).

## Visual review

For edits with new text, a review PDF with new words in a second colour lets the author see the editor's share at a glance. A clean PDF alongside it shows the reading experience.

## Evaluation record

Commit `resources/evaluations/YYYY-MM-DD-<name>.md`: base commit, what was read, what changed (table: chapter | problem | change | kept deliberately), verification results, what was not done and why, claims to verify, and the author's decisions. State plainly that it is an assistant-edited draft, not a record of author acceptance.

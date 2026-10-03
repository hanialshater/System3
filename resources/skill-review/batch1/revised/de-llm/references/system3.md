# System 3 specifics

Repo: `github.com/hanialshater/System3`. Chapters in `chapters/NN-*.md`. Always work from the current repo state, not a PDF build; one full edit had to be rebuilt because it started from a PDF that predated the author's own edit.

Anything below marked with a date is a snapshot. Re-derive it from the repo with the command given before you rely on it.

## Read before choosing any cut

1. `resources/editorial/easter-egg-register.md`. Seeds look like digressions to an editor who does not know the payoff. Seeds, confirmed or proposed, are not cut, and no pass explains a payoff (not in the text, not in a change-list reason).
2. The revert and approval lists: `ls resources/evaluations/*revert-list* resources/evaluations/*approval-list*`. The revert list names every useful cut by ID (R11-4 and so on). A line that was cut and then restored is the author's decision; do not propose it again without saying so.
3. Recent restores: `git log --since=2026-10-01 --format='%h %ad %s' --date=short -i --grep=restor -- chapters/<file>` (widen the date as needed).
4. The guarded sentences for the chapter, which combine all of the above with the protected list:
   `python3 scripts/protected.py --repo <repo> --chapter chapters/<file> --list`
5. Claude's own earlier additions, the first suspects: `git log --author=Claude --oneline -- chapters/<file>` and `git blame chapters/<file> | grep Claude`. As of 3 Oct 2026 the chapters carry no `ASSISTANT EDIT` markers (`grep -rn 'ASSISTANT EDIT' chapters` to re-check); open questions to the author are `<!-- AUTHOR: … -->` comments, which stay.

## Files no pass edits

All of Chapter 13 (`13-the-prophecy.md`), the divider (`alternative-ending.md`) and `14-scaffolds.md`: typography only (copyedit plan, row "13, divider, scaffolds"). The Zen appendix maxims. tells.py and protected.py print a warning on these files; report on them if asked, never cut.

## Protected lines

The list lives in `references/protected.txt`, one exact string per line with curly quotes, so scripts can check it. Before a pass, run `python3 scripts/protected.py --repo <repo> --audit`: a protected line missing from `chapters/` is a stop. Find who removed it (the audit prints the commit) and tell the author before going on.

Recurring motifs are protected as motifs: the camel, the cow, coffee, Alberto, the tongue test, the mother's face, Reviewer 2, the sixteen Claudes, the store. Also the Chapter 1 cat-obsession paragraph.

## House rules already in the repo

- `prompts/chapter-version-evaluation.md`: the house evaluation prompt. Its "Explicitly detect LLM writing" list and "What to protect" list are the author's own and outrank this skill where they differ. It penalizes "excessive one-line paragraphs": hence the baseline-density rule for one-liners.
- `resources/editorial/copyedit-plan-*.md`: surgery over replacement; delete and fold before adding; protect the voice; Chapter 13 gets typography only; no fabricated evidence; assistant markers stay until the author signs off. **Prose uses curly quotes and apostrophes (’ “ ”).** Type them in every `old` string or the edit misses; apply_pass prints a hint when it sees a straight quote in a miss.
- Bold in prose only for a coined term and for Chapter 6's pattern *Therefore* lines.
- `resources/editorial/check-tells.py`: the repo's own counter (maxim %, not-X-but-Y, citation chains, cross-references), targets calibrated on Chapters 4–5: maxim% ≤ 30, notXbutY/1k ≤ 0.5, xref/1k ≤ 0.5. **It takes chapter prefixes (`11`), not paths, and always reads the `chapters/` folder of the repo it sits in.** Given a file path it silently prints an empty table. To measure an edited copy with it, run it inside a scratch clone holding the copy (below); otherwise use `scripts/tells.py`, which takes any file. The two tools use different thresholds (12 vs 14 words for a closing line, different not-X regexes), so compare each tool only with itself.

## Working on a copy

When the repo is read-only, or the user says "work on a copy", nothing is written under the repo: no edits, no commits, and no running its tests or builds there (a test run leaves `__pycache__` behind). Do the gates in a scratch clone:

```
git clone -q <repo> $SCRATCH/clone && cp <edited copy> $SCRATCH/clone/chapters/<file>
```

## Gates after every pass (run in the scratch clone, or the repo if you are allowed to write it)

1. Guarded sentences: `python3 scripts/protected.py --repo <repo> --chapter chapters/<file> --check <edited copy>`. Quote its counts in the report ("restored: 50/51 kept verbatim; changed: …"). Never write "every restored line is untouched" without this output; two test runs claimed it and were wrong.
2. `bash resources/editorial/check-eggs.sh`. FAIL is a confirmed seed; any *warn* that was *ok* before the pass means you cut a proposed seed. Restore it or ask.
3. References and comment leaks (citations are numbered `[n](appendix-references.md#ref-…)`; no chapter uses `[^…]` footnotes as of 3 Oct 2026):
   ```
   cd book-design/curated && python3 -B -c "
   from pathlib import Path; from manuscript import *
   p=ordered_paths(Path('../../chapters'),Path('book-order.json'))
   validate_references(p,reference_entries(Path('../../chapters/appendix-references.md').read_text())); print('references ok')
   t=prepare(open('../../chapters/NN-name.md').read())[0]; print('leak', '<!--' in t or 'ASSISTANT' in t)"
   ```
   `validate_references` fails on an uncited entry or a wrong number. If a cut removes the last citation of a reference, move its entry to that chapter's *Additional sources* by hand and renumber the chapter's later citations; the build fails until you do.
4. NotebookLM briefs: `python3 -B prompts/build_notebooklm.py --check` reports "Stale" after *any* chapter edit, because `sources.json` stores hashes. Regenerate with `python3 -B prompts/build_notebooklm.py`. If that stops with "lines the brief keeps are no longer in the manuscript", the pass cut a kept line: restore it, or change `CORE` in the generator and say so in the report. Include the regenerated `prompts/notebooklm/` files in the patch.
5. `book-design/pdf.py build` and the unit tests (`python -m unittest discover -s book-design/curated/tests`) need the `.venv-pdf` environment (PIL, PyMuPDF; see `book-design/README.md`). If it is missing, say the gate was skipped and why; do not install into the repo.
6. Re-read the seams of every cut.

`ASSISTANT EDIT` markers are HTML comments; `prepare()` strips them from the build, so they do not leak. The author removes them on sign-off.

## Delivery

One commit per pass per chapter, with a message that says what was cut and that recast words are flagged inline.

- Repo writable (or a scratch clone): commit there and deliver `git format-patch` output as both `.patch` and `.txt` (downloads have arrived as zero-byte files). Verify it applies to a clean clone of the base commit with `git am`.
- Repo read-only and no commit wanted: deliver the edited copy plus a unified diff with repo-relative names, so the header does not name a temp file:
  ```
  diff -u --label a/chapters/<file> --label b/chapters/<file> <repo>/chapters/<file> <copy> > <name>.patch
  ```
  The author applies it from the repo root with `git apply <name>.patch` (or `patch -p1 < <name>.patch`). Check it with `git apply --check` in a scratch clone.
- Always add the apply script (fallback) and the change list.

## Past passes (history, not current state)

Words in this table are apply_pass counts (every word outside comments); tells.py counts paragraph words only and runs about 8% lower. Most of these chapters have been edited and partly restored since. Re-measure before quoting any figure.

| Pass | Before → after |
|---|---|
| Ch 4 delete-and-fold (40 changes) | 5,839 → 5,077 words; signposts 2.05 → 0.87/1k; anaphoric runs 2.79 → 1.95/1k; "X is not Y. It is Z." 1.12 → 0.87/1k |
| Book-wide delete-and-fold | 69 changes, 1,122 words cut |
| Titles and closings pass | 30 titles replaced, 18 closing lines cut, ten chapters |
| Ch 6 de-LLM pass (~60 cuts) | 8,614 → 7,645 words; negations 49 → 39; "Suppose" 7 → 3 |
| Ch 6 X/Y pass (16 edits) | 7,645 → 7,549 words |
| Ch 12 verb pass (earlier draft) | "become" 36 → 4 |
| Ch 11 test pass (3 Oct 2026) | 4,752 → 4,410 words (−7%), kept light to spare the 2 Oct restores |

## How much to cut

A first full de-LLM pass on a chapter nobody has passed over typically leaves it 10–15% shorter. That is an expectation, not a quota, and it yields to two things: the lines the author restored (never cut to reach the number), and chapters already at or below the Ch4–5 baseline. Measure first; a chapter at baseline gets flagged candidates, not cuts. X/Y passes move a few hundred words at most.

Snapshot, 3 Oct 2026 (tells.py, Ch4+5 pooled baseline): Chapters 6 and 7 are at or below baseline on signposts, closing morals and one-liners (one-liners well below: cooled); their excess is antithesis (Ch7 about 5x). Chapter 11 leans on anaphora (about 5x), parallel pairs (2.4x) and opener tics (3x). Re-run `scripts/tells.py chapters/06-*.md chapters/07-*.md chapters/11-*.md --baseline chapters/04-system-3.md chapters/05-the-society-of-agents.md` before relying on this.

## Known trap

Each pass can cool a chapter. Chapters 6 and 7 got cooler and more procedural over several passes, which the author did not want. Chapter 4 runs hot by design (manifesto). When a chapter is already sparse, prefer flagging candidates over cutting them.

## Arabic

The blog series and any Arabic chapter translations are out of scope for the detector (English regexes). A translation made before a de-LLM pass still contains the cut sentences; tell the author it needs the same trim.

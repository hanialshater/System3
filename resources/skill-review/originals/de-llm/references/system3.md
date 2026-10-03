# System 3 specifics

Repo: `github.com/hanialshater/System3`. Chapters in `chapters/NN-*.md`. Always work from the current repo state, not a PDF build; one full edit had to be rebuilt because it started from a PDF that predated the author's own edit.

## House rules already in the repo

- `prompts/chapter-version-evaluation.md` — the house evaluation prompt. Its "Explicitly detect LLM writing" list and "What to protect" list are the author's own and outrank this skill where they differ.
- `resources/editorial/copyedit-plan-*.md` — surgery over replacement; delete and fold before adding; protect the voice; Chapter 13 gets typography only; no fabricated evidence; `ASSISTANT EDIT` / `ASSISTANT DRAFT` / `CLAUDE DRAFT` markers stay until the author signs off.
- `resources/editorial/check-tells.py` — the repo's own tells counter (maxim %, not-X-but-Y, citation chains, cross-references) with targets calibrated on Chapters 4–5: maxim% ≤ 30, notXbutY/1k ≤ 0.5, xref/1k ≤ 0.5. Run it alongside `scripts/tells.py`; the two use different thresholds (12 vs 14 words for a closing line, different not-X regexes), so compare each tool only with itself.

## Gates after every pass

1. `bash resources/editorial/check-eggs.sh` — planted seeds and footnote counts intact.
2. Footnote references match definitions, and no `<!--` comment text leaks into the build:
   ```
   cd book-design/curated && python3 -c "
   import re,sys; sys.path.insert(0,'.')
   from manuscript import prepare
   t,defs,_,_=prepare(open('../../chapters/NN-name.md').read())
   refs=set(re.findall(r'\[\^([^]]+)\]',t)); print('footnotes', refs==set(dict(defs))); print('leak', '<!--' in t or 'ASSISTANT' in t)"
   ```
   (If the chapter uses numbered `[n](appendix-references.md#…)` citations instead, the PDF build's `validate_references` checks them; a deleted cited sentence moves its entry to "Additional sources".)
3. `book-design/pdf.py build` and `python -m unittest discover -s book-design/curated/tests` when the environment allows.
4. Re-read the seams of every cut.

## Delivery

One commit per pass per chapter, with a message that says what was cut and that recast words are flagged inline. Deliver `git format-patch` output as both `.patch` and `.txt` (downloads have arrived as zero-byte files), plus the apply script as a fallback, plus the change list. Verify the series applies to a clean copy of the base commit with `git am`.

## Past numbers (for calibration)

| Pass | Before → after |
|---|---|
| Ch 4 delete-and-fold (40 changes) | 5,839 → 5,077 words; signposts 2.05 → 0.87/1k; anaphoric runs 2.79 → 1.95/1k; "X is not Y. It is Z." 1.12 → 0.87/1k |
| Book-wide delete-and-fold | 69 changes, 1,122 words cut |
| Titles and closings pass | 30 titles replaced, 18 closing lines cut, ten chapters |
| Ch 6 de-LLM pass (~60 cuts) | 8,614 → 7,645 words; hedges 49 → 39; "Suppose" 7 → 3 |
| Ch 6 X/Y pass (16 edits) | 7,645 → 7,549 words |
| Ch 12 verb pass | "become" 36 → 4 |

Expect 10–15% shorter from a full de-LLM pass and a few hundred words from an X/Y pass.

## Protected lines (do not cut without asking)

"preserve the wrong lesson at industrial speed" · "a decorative conscience" · "we have successfully parallelized the experience of being ignored" · "Preserving my judgment and preserving my mistakes used the same file format" · "Nobody is lying. The hypothesis has been fitted to the result." · "The objection can now survive its author. So can the assumption it challenges." · "Cheap software removed the vendor's veto. It did not produce a second room at seven on Tuesday." · "Reality retains the right to be rude" · "The model stays hollow" · the Chapter 1 cat-obsession paragraph · all of Chapter 13 · the Zen of System 3 maxims.

Recurring motifs are protected as motifs: the camel, the cow, coffee, Alberto, the tongue test, the mother's face, Reviewer 2, the sixteen Claudes, the store.

## Known trap

Each pass can cool a chapter. Chapters 6 and 7 got cooler and more procedural over several passes, which the author did not want. Chapter 4 runs hot by design (manifesto). When a chapter is already sparse, prefer flagging candidates over cutting them.

## Arabic

The blog series and any Arabic chapter translations are out of scope for the detector (English regexes). A translation made before a de-LLM pass still contains the cut sentences; tell the author it needs the same trim.

# Changelog: dev-edit (revision of 3 Oct 2026)

- SKILL Phase 4: three checks before any cut or rewrite (whose words via `--provenance`/`git blame --ignore-rev`, restored before via revert lists and `git log -S`, quoted elsewhere incl. Zen appendix, epigraphs, register, NotebookLM `CORE[n]['keep']`). Answers audit 1 and the runs proposing to cut the author's 27 Sep `aeddc03` lines twice.
- SKILL Phase 7: cut log gets a "last changed by" column. Audit 1.
- arc_map.py `--provenance DAYS` (+ `--only`, `--ignore-rev`): lists the author's own recent lines, looks through the 1bce77f/75e80c2 mechanical passes, marks assistant-looking commits under his name with `?`. Audit 1, check C.
- SKILL Phase 2: spine is three sentences at most, details below it. Grading of eval-3 (five sentences under a "one sentence" heading).
- SKILL Phase 2: "When you can't stop": in a one-shot report, state the assumed arc first, mark it assumed, list it first under Your decisions. findings-from-runs (eval-3).
- SKILL Phase 0 + system3-state.md header: state is a dated snapshot; re-derive with `git log`, a marker `git grep` and REVISIT.md before quoting. Audit 2, check B, findings-from-runs.
- system3-state.md: blockers corrected (reveal/interlude drafts, SLOT 4, Ch 2 figures settled 30 Sep in ca80ba2; only the 2.636 methods trail and AUTHOR: questions remain). Audit 2.
- system3-state.md: part totals and first-person numbers updated and labelled "rerun"; added 3 Oct recaps, the Ch 10 2.26–2.636 slip and the Ch 12 fable-preview question. Audit 9, findings-from-runs, eval-4 grading.
- system3-state.md Protected: seeds protected by function; recent author lines; NotebookLM keep lines; "The model stays hollow" noted as removed by the author (cfade23); how to check a list with `--protected`. Audits 6, 9, check A.
- SKILL Phase 5: protected list now Ch 13, divider, scaffolds; seeds protected for function per the register's anchor rule. Audit 6.
- SKILL Phase 3: cross-chapter consistency check for restated numbers/names/terms; arc_map.py `--numbers`. Eval-4 grading (Ch 10 L77 vs Ch 2 L59/L209).
- SKILL Phase 3 + evaluation.md: verify every line citation with `grep -n` on the current file; evaluation docs may quote older versions. Brief + findings-from-runs (eval-4).
- arc_map.py `--recaps`: count of shared 5-word runs (`--min-shared 3`) instead of a ratio; blockquotes and part pages skipped. Now finds Ch 4→5, Ch 5→7, Ch 2→7; `--threshold` dropped. Audit 3, check D, findings-from-runs.
- arc_map.py `body()`: strips only `{=latex}` fences, so the Zen appendix counts (7 → 256 words) and its maxims reach motifs/recaps. Audit 4.
- arc_map.py `paras()`/`--handoffs`: skips italic subtitles and image captions; prints chapter-to-chapter seams, then apparatus seams separately. Audit 5.
- arc_map.py `--motifs`: multiword terms match across whitespace/line breaks; help says to quote the list and how to add `\b`. Brief, findings-from-runs, audit 12.
- arc_map.py: `--protected FILE` exits 1 on a missing line and prints the `git log -S` to run. Check A.
- arc_map.py: `--order` warns on files missing from disk or from the order; I/1k counts I'd, I'll, My, Me. Audit 12.
- implementation.md gates 2, 3, 5, 6, 7 rewritten for the curated build (validate_references, `.venv-pdf`, pdf.py build --preview, book-order.json); gate 8 on stripping flags; pandoc footnote story kept as history. Audit 7.
- implementation.md + SKILL: one flag vocabulary (`ASSISTANT DRAFT` / `ASSISTANT EDIT`); `drafts/` to be created. Audits 10, 11.
- arc-toolkit.md: stale Ch 8→9 seam and camel-in-Ch-13 examples fixed; numbers point to the state file; recaps documented as candidates vs callbacks; new "Restated facts" check; lexical-grid caveat. Audits 8, 9, 12.
- SKILL Phase 0: full paths, reading load limited to newest two or three evaluations, exact command line; provenance limited with `--only` (whole book lists ~1,400 lines). Audit 11.
- Description: adds blind/cold read, readiness, "how far from publishable"; names de-llm, fresh-claims, levantine-translate, video-briefs as neighbours. Audit 13.

Not changed: no `.git-blame-ignore-revs` or protected-lines file added to the repo (author's call; the skill suggests them). The repo's own `.claude/skills/development-edit` overlaps with this skill; the author should keep one.

---
name: dev-edit
description: Structural editing for a nonfiction book or long essay. Covers reviewing and agreeing the arc and central thesis, part structure, chapter order and handoffs, narrative momentum, seeds and payoffs, and then planning, implementing and evaluating a development edit as reviewable patches. Use whenever the user asks to "review the arc", "evaluate the thesis", "development edit", "dev edit", "narrative momentum", "make this chapter a 9.5", "how far from publishable", "readiness", "blind read" or "cold read", "compare versions", "benchmark against Sapiens / Life 3.0 / Human Compatible", "restructure the book", "part pages", or asks to plan a chapter's structural edit or score English chapters, for System 3, The Dream, Coffee & Commute or long strategy documents. Not for sentence-level LLM tells (de-llm; use both when a pass touches both), fact-checking claims against sources (fresh-claims), Arabic versions or their scores (levantine-translate), or video prompts (video-briefs).
---

# Development edit

The arc belongs to the author. Claude's job is to read all of it, reconstruct what the book is actually doing, propose that back in a form the author can correct, and only then edit against the agreed version. Most of the damage in past edits came from editing before the arc was agreed, from verdicts not grounded in the text, from new prose in the editor's voice, and from proposing to cut lines the author had just written himself.

## Phase 0 — Sources and standing records

- Work from the live source (the git repo's `main`, or the file being edited now), never an older PDF. Note the commit you read (`git log -1 --oneline`). If the repo is read-only or the user asks for a copy, work on a copy and deliver from there.
- Read the standing records first. For System 3: `resources/editorial/working-spine.md` (the spine; the README only links to it), `resources/editorial/easter-egg-register.md`, `resources/REVISIT.md`, the house prompt `prompts/chapter-version-evaluation.md`, the newest two or three files in `resources/evaluations/` and any revert list (`*revert-list*`; it records what the author took back). That folder holds more words than the manuscript: skim older evaluations only for a question they answer. Old length targets and "locked" labels in past evaluations are history, not instructions.
- **Re-derive the state; don't quote it.** `references/system3-state.md` is a dated snapshot and has been wrong before (it listed blockers settled days earlier). Before reporting anything as open, check it against the repo:
  ```
  git log --oneline -15 -- chapters                      # what changed lately, and by whom
  git grep -n -E "ASSISTANT (EDIT|DRAFT)|CLAUDE (EDIT|DRAFT)|SLOT ?[0-9]|AUTHOR:|Missing figure" -- chapters
  ```
  plus `resources/REVISIT.md` ("Completed" section). An item the grep and REVISIT don't confirm is closed; say so rather than repeat it.
- Run the map from the repo root:
  `python3 <skill>/scripts/arc_map.py chapters --order book-design/curated/book-order.json --handoffs --recaps --numbers --markers`
  It gives words per chapter and part, headings, notes, bold and first-person density, chapter-to-chapter handoffs, cross-chapter repeats, restated numbers and unresolved markers. For the files you may touch, add `--provenance 21 --only 10-,11-` (the author's own lines of the last three weeks; on the whole book it lists over a thousand, so limit it). Add `--motifs "camel,loose cable,coffee"` for threads; **quote the list** whenever a term has a space. Arc claims should cite these numbers. Every list it prints is candidates, not verdicts.

## Phase 1 — Read completely, then say what you read

Judge only text you read in full. Excerpt-based judging systematically punishes chapters that build or turn in the middle. If a comparison book wasn't uploaded, say the comparison rests on general knowledge and reputation, not on the text, and weight it accordingly.

## Phase 2 — Agree the arc before any edit

Propose the arc back to the author and stop for correction. Format that worked:

1. **The spine, in three sentences at most.** It is the thing the author corrects, so it must be short enough to correct in one reply. Details, sub-claims and caveats go below it, never inside it. If you wrote a heading that says "one sentence", count.
2. **Theme / center / end** (for System 3: emergence as the frame, science as the center, what the capacity means for humans as the end).
3. **A table: section | chapters | the one question it answers**, plus the handoff that makes the next question unavoidable.
4. **The placements you're least sure of**, asked as questions, each tied to a passage or a number.

**When you can't stop.** In a one-shot report (the author asked for a plan, a diagnosis or a review and won't answer mid-task), you cannot wait for the arc to be agreed. Then put the arc you assumed at the top of the report, mark it *assumed, correct me*, list it first under **Your decisions**, and build the rest on it so a correction tells him which items fall. Don't silently skip the step, and don't treat your assumed arc as agreed in the next session.

When the author's framing differs from your reading, test their framing against the text and withdraw what it dissolves ("two theses" became "three movements"). If the structure isn't visible to you, readers won't find it either; the fix is usually explicit apparatus (part pages, a reveal page, a divider), not more prose. Write the agreed spine into the repo (`working-spine.md`) so later passes edit against it.

## Phase 3 — Diagnose

Run the checks in `references/arc-toolkit.md`, chapter level and book level. The core questions:
- Does each part answer one question, and does each chapter end on the question the next one opens?
- Where is the thesis stated, and is the evidence strongest where the claim is loudest? (Mark each chapter Run / Argued / Designed / Reported / Imagined.)
- Where are the peaks and troughs? Variance matters more than average; a late peak is weaker than an early one.
- Which seeds pay off later? A seed looks like a digression to an editor who doesn't know the payoff. Check the register before cutting anything, and never explain a payoff.
- Does the narrator change? (First-person density per 1,000 words is a quick proxy: "watched it happen" vs "read everything".)
- Is a later chapter re-teaching the thesis instead of invoking it? `--recaps` lists cross-chapter near-repeats (Ch 4's closing question restated as Ch 5's; "emotionally satisfying and institutionally almost worthless" in Ch 5 and Ch 7). It works on shared five-word runs, so a paraphrase with new wording slips through: also read each chapter's opening against the previous chapter's close.
- **Does a chapter restate another chapter's facts correctly?** Numbers, names, dates and coined terms that reappear later drift. `--numbers` lists every decimal and percentage that appears in more than one file; check each against the chapter that owns it. (Ch 10 once said the circle-packing scores "ran from 2.26 to 2.636"; Ch 2 has one run climbing from 1.33 to 2.26 and 2.636 as the best run.) Do the same by eye for names and terms (Ch 8 calls the shared Artifactory note a "bulletin board" and then a "back channel"; Ch 10 picks up "back channel").

Every finding names the passage, quotes it or gives the number, and says what to do. No sweeping verdicts: "Sapiens. And it's not close" was rightly called ungrounded. Overcorrecting into deference is the same failure.

**Cite what is there now.** Before you put a line number or a quote in a report, check it against the current file: `grep -n "<a few exact words>" chapters/<file>`. Evaluation docs in `resources/evaluations/` often quote an older version of a chapter; a finding taken from one must be re-found in today's text before you repeat it, or labelled as from that evaluation.

## Phase 4 — Plan

An ordered plan with the expected effect of each item and its cost. When there are several structural options (section orders, where a page goes), sketch them side by side with their trade-offs and let the author choose. Separate three kinds of work:
- **Structure and apparatus** Claude can do: moves, part pages, handoffs, reorders, cuts, references from the author's own sources.
- **New argument or scenes** Claude can only draft, flagged, to be rewritten by the author.
- **Things only the author has**: a real anecdote, an experiment result, a lived detail, a decision. Leave a marked slot (`[AUTHOR: …]`). Never invent them.

**Before proposing any cut or rewrite, check three things and say what you found:**
1. **Whose words.** `--provenance 21` lists lines the author changed himself in the last three weeks, with commit and date; a `?` after the commit means the summary suggests an assistant's edit under his name (System 3's `8bcaac3` "Apply developmental edit F…"), so ask. For one line: `git blame -w -M -L <n>,<n> -- <file>`, and add `--ignore-rev 1bce77f --ignore-rev 75e80c2` (the 30 Sep typography and copyedit passes) or blame will hide him. A recent author line is his decision, not a candidate: put it under **Your decisions** with the commit and date ("you rewrote this on 27 Sep in `aeddc03`; it reads as a repeated formula because…"). Past passes proposed cutting his 27 Sep Ch 1 lines twice because nobody looked.
2. **Restored before.** Search the revert lists (`grep -n "<words>" resources/evaluations/*revert-list*`) and `git log -S"<words>" --oneline -- chapters`. A line cut and put back is not re-cut without saying so, with its ID (R10-3) and commit.
3. **Quoted elsewhere.** `grep -rn "<words>" chapters prompts resources/editorial`. In System 3 that catches the Zen appendix (`chapters/appendix-zen-of-system-3.md`, whose maxims also head the part pages), epigraphs, other chapters' callbacks, the egg register's anchors and the NotebookLM "keep" lines in `prompts/build_notebooklm.py` (`CORE[n]['keep']`, checked against the manuscript at build time). A cut that breaks one of these needs the other side changed in the same commit, or it's off the list.

## Phase 5 — Implement

Rules (details and scripts in `references/implementation.md`):
- **Moved, not written.** When text moves, verify it arrived verbatim. A pass that says "no new prose" must be checkable.
- **Flag every new or changed sentence** in the source with the repo's flags (`ASSISTANT DRAFT` around new passages, `ASSISTANT EDIT` before a changed sentence, with the old wording; see `references/implementation.md`). New argument passages can live in a `drafts/` folder at the repo root (create it) until the author writes them.
- **Protected material stays byte-identical**: System 3's Chapter 13, the alternative-ending divider and the scaffolds page (`14-scaffolds.md`), and the lines on the protected list. Verify with a diff. Confirmed seeds are protected for what they do, not their wording: an edit may reword one if the seed still works and the register's anchor is updated in the same commit (`check-eggs.sh` must pass).
- **Recent author lines and restored lines are his.** See the three checks in Phase 4. If an edit touches one anyway, say so in the change document.
- **Don't cut load-bearing sentences.** After every cut, check antecedents ("the bargain", "the curator", a dangling "Otherwise").
- **New material must not contradict the thesis** (the first interlude said the failure was nobody standing "outside the box", which undercut Chapter 5's whole point), **must not spoil a later punchline**, **must not narrate the manuscript** ("for eight chapters…") and **must not promise later chapters solve what they only explore**.
- **Count the ceremony.** Every part page, divider and single-line page is a page turn. Four in a row before a chapter is too many.
- One commit per structural change. Each commit builds. Run the gates (egg check, references, build) after each.

## Phase 6 — Evaluate and iterate

- Use a fixed rubric across versions (see `references/evaluation.md`) and say which one. Different rubrics give different scales; don't compare across them.
- Rounds you run on your own edits are not independent. Say so. Don't score your own sentences as the author's.
- Prefer a blind cold read (fresh evaluator, no history, only the house prompt and the chapters) or a judge from another vendor. Treat findings two independent judges converge on as stronger than either alone.
- When the author pushes back and you re-judge, note the direction. Re-judging only when the author objects, and always in the book's favour, is drift.
- Read the transitions in the built output, not only in markdown.

## Phase 7 — Deliver

A patch series (plus a `.txt` copy), the changed files, a change document, and an evaluation record committed under `resources/evaluations/YYYY-MM-DD-<name>.md`. For a report-only request, the report file is the deliverable and nothing in the repo changes.

The cut log (and any plan table that proposes cuts) carries a column **last changed by** (author / assistant / mechanical, with commit and date) and notes any restore ID or cross-book quote.

End the chat report with **Your decisions**: the assumed arc if you couldn't stop for it, recent author lines you'd question, drafts to rewrite, facts to verify, seeds to confirm, slots to fill, anything untouched on purpose. Keep the chat report short and in prose; the record holds the detail.

## Files

- `scripts/arc_map.py` — structure numbers, handoffs, motif grid, cross-chapter repeats, restated numbers, markers, provenance, protected-line check. `--help` lists every mode.
- `references/arc-toolkit.md` — the diagnostics with real examples from System 3 and The Dream.
- `references/implementation.md` — ops engine pattern, flags, gates, build, verification snippets.
- `references/evaluation.md` — rubrics used so far, momentum and readiness scales, independence protocol.
- `references/system3-state.md` — the agreed spine and open structural issues, snapshot of 3 October 2026. Re-derive before quoting (commands at its top).

---
name: dev-edit
description: Structural editing for a nonfiction book or long essay — reviewing and locking the arc and central thesis, part structure, chapter order and handoffs, narrative momentum, seeds and payoffs, and then planning, implementing and evaluating a development edit as reviewable patches. Use whenever the user asks to "review the arc", "evaluate the thesis", "development edit", "dev edit", "narrative momentum", "make this chapter a 9.5", "compare versions", "benchmark against Sapiens / Life 3.0 / Human Compatible", "restructure", "part pages", or asks for scores per chapter, including for System 3, The Dream, Coffee & Commute or long strategy documents. Sentence-level LLM tells belong to the de-llm skill; use both when a pass touches both.
---

# Development edit

The arc belongs to the author. Claude's job is to read all of it, reconstruct what the book is actually doing, propose that back in a form the author can correct, and only then edit against the agreed version. Most of the damage in past edits came from editing before the arc was agreed, from verdicts not grounded in the text, and from new prose in the editor's voice.

## Phase 0 — Sources and standing records

- Work from the live source (the git repo's `main`, or the file being edited now), never an older PDF. Note the commit you read.
- Read the project's standing records first. For System 3: the README spine, `resources/editorial/working-spine.md`, `easter-egg-register.md`, `REVISIT.md`, the house prompt `prompts/chapter-version-evaluation.md`, and the latest files in `resources/evaluations/` (especially any revert list — it records what the author took back). Old length targets and "locked" labels in past evaluations are history, not instructions.
- Run `scripts/arc_map.py` on the chapter directory with the book order file. It gives words per chapter and per part, heading counts, notes, bold density, first-person density, handoffs, motif presence and unresolved markers. Arc claims should cite these numbers.

## Phase 1 — Read completely, then say what you read

Judge only text you read in full. Excerpt-based judging systematically punishes chapters that build or turn in the middle. If a comparison book wasn't uploaded, say the comparison rests on general knowledge and reputation, not on the text, and weight it accordingly.

## Phase 2 — Agree the arc before any edit

Propose the arc back to the author and stop for correction. Format that worked:

1. **Spine in one sentence.**
2. **Theme / center / end** (for System 3: emergence as the frame, science as the center, what the capacity means for humans as the end).
3. **A table: section | chapters | the one question it answers**, plus the handoff that makes the next question unavoidable.
4. **The placements you're least sure of**, asked as a question.

When the author's framing differs from your reading, test their framing against the text and withdraw what it dissolves ("two theses" became "three movements"). If the structure isn't visible to you, readers won't find it either; the fix is usually explicit apparatus (part pages, a reveal page, a divider), not more prose. Write the agreed spine into the repo (README / working-spine) so later passes edit against it.

## Phase 3 — Diagnose

Run the checks in `references/arc-toolkit.md`, chapter level and book level. The core questions:
- Does each part answer one question, and does each chapter end on the question the next one opens?
- Where is the thesis stated, and is the evidence strongest where the claim is loudest? (Mark each chapter Run / Argued / Designed / Reported / Imagined.)
- Where are the peaks and troughs? Variance matters more than average; a late peak is weaker than an early one.
- Which seeds pay off later? A seed looks like a digression to an editor who doesn't know the payoff. Check the register before cutting anything.
- Does the narrator change? (First-person density per 1,000 words is a quick proxy: "watched it happen" vs "read everything".)
- Is a later chapter re-teaching the thesis instead of invoking it?

Every finding names the passage, quotes it or gives the number, and says what to do. No sweeping verdicts: "Sapiens. And it's not close" was rightly called ungrounded. Overcorrecting into deference is the same failure.

## Phase 4 — Plan

An ordered plan with the expected effect of each item and its cost. When there are several structural options (section orders, where a page goes), sketch them side by side with their trade-offs and let the author choose. Separate three kinds of work:
- **Structure and apparatus** Claude can do: moves, part pages, handoffs, reorders, cuts, footnotes from the author's own references.
- **New argument or scenes** Claude can only draft, flagged, to be rewritten by the author.
- **Things only the author has**: a real anecdote, an experiment result, a lived detail, a decision. Leave a marked slot. Never invent them.

## Phase 5 — Implement

Rules (details and scripts in `references/implementation.md`):
- **Moved, not written.** When text moves, verify it arrived verbatim. A pass that says "no new prose" must be checkable.
- **Flag every new or changed sentence** in the source (`CLAUDE DRAFT` / `ASSISTANT EDIT` comments, with the old wording when a sentence changed). New argument passages can live in `drafts/` until the author writes them.
- **Protected material stays byte-identical** (System 3: Chapter 13, the scaffolds page, confirmed seeds, the author-restored lines). Verify with a diff.
- **Don't cut load-bearing sentences.** After every cut, check antecedents ("the bargain", "the curator", a dangling "Otherwise").
- **New material must not contradict the thesis** (the first interlude said the failure was nobody standing "outside the box", which undercut Chapter 5's whole point), **must not spoil a later punchline**, **must not narrate the manuscript** ("for eight chapters…") and **must not promise later chapters solve what they only explore**.
- **Count the ceremony.** Every part page, divider and single-line page is a page turn. Four in a row before a chapter is too many.
- One commit per structural change. Each commit builds. Run the gates (egg check, footnotes, build) after each.

## Phase 6 — Evaluate and iterate

- Use a fixed rubric across versions (see `references/evaluation.md`) and say which one. Different rubrics give different scales; don't compare across them.
- Rounds you run on your own edits are not independent. Say so. Don't score your own sentences as the author's.
- Prefer a blind cold read (fresh evaluator, no history, only the house prompt and the chapters) or a judge from another vendor. Treat findings two independent judges converge on as stronger than either alone.
- When the author pushes back and you re-judge, note the direction. Re-judging only when the author objects, and always in the book's favour, is drift.
- Read the transitions in the built output, not only in markdown.

## Phase 7 — Deliver

A patch series (plus a `.txt` copy), the changed files, a change document, and an evaluation record committed under `resources/evaluations/YYYY-MM-DD-<name>.md`. End the chat report with **Your decisions**: drafts to rewrite, facts to verify, seeds to confirm, slots to fill, anything untouched on purpose. Keep the chat report short and in prose; the record holds the detail.

## Files

- `scripts/arc_map.py` — structure numbers, handoffs, motif grid, cross-chapter repeats, markers.
- `references/arc-toolkit.md` — the diagnostics with real examples from System 3 and The Dream.
- `references/implementation.md` — ops engine pattern, flags, gates, build, verification snippets.
- `references/evaluation.md` — rubrics used so far, momentum and readiness scales, independence protocol.
- `references/system3-state.md` — the locked spine and the open structural issues as of early October 2026. Re-read the repo before trusting it.

# Evaluation

## Rubrics used so far

Name the rubric in every score table. Scales differ: the same book scored 8.6 on one and 8.1 on another the same week.

**House prompt (22 dimensions)** — `prompts/chapter-version-evaluation.md` in the System 3 repo. Version A vs B per chapter, with "what A still does better", "what B genuinely improves", an LLM-writing audit, protected lines, claims to tighten, overall. The author wrote it; it outranks the others for chapter comparisons.

**Comparator rubric, 10 dimensions** (used against *Life 3.0*): thesis clarity, originality, first-hand evidence, epistemic honesty, prose and voice, accessibility, arc and architecture, scope and stakes, engaging objections, production readiness. Report content (first nine) and overall separately.

**Comparator rubric, 15 dimensions** (used against *Human Compatible*, *Life 3.0*, *Sapiens* and a wider shelf): originality, mechanism, evidence, thesis discipline, reader apparatus, arc, voice, ending, fun, twists, peaks, thought-provocation, weirdness, plus engagement and prose. It weights originality and strangeness, where System 3 leads; say so when you use it.

**Reader-experience rubric v2** (the author's replacement for academic criteria in the Bradley–Terry tournament): big ideas, thought-provoking, engagement, fun, momentum, prose, awkwardness, novelty.

**Per-chapter book comparison** (The Dream vs Sapiens): arc, big idea, enjoyment, layered reveals, with peaks, troughs, count of chapters ≥ 9 and ≤ 7, and cut/merge candidates.

**Momentum scale**: 7 = engaging with pauses, 8 = steady pull, 9 = sustained propulsion. Momentum scores describe reading pull, not intellectual quality.

**Readiness scale**: Ready (copyedit only), Near (one light targeted pass), Needs pass (focused developmental edit of named sections), Blocked (needs an art, production or author decision). Pair it with a quality score and "what holds it back".

## Grounding

- Every score row carries a reason that points at the text: a quote, a section name, a count.
- Compare like with like: full text against full text. Excerpt-based judging punished essay-shaped chapters whose best material is in the middle.
- When a comparison book wasn't provided, say the score rests on reputation and memory.
- Quote and cite the current text. Check every line number and quote with `grep -n` before it goes in a table; a prior evaluation's quote may be from an older version of the chapter.
- Avoid verdict rhetoric ("it's not close", "one brutal edit away"). The author called that out as ungrounded, and the overcorrection that followed ("obviously a shipped product beats a prototype") was no better. The useful question is what to learn from the comparator's craft.

## Independence

Ranked from weakest to strongest:
1. Rounds you run on your own edits. Useful for catching slips, never evidence of quality. Label them as such.
2. A second model reading your patch and your evaluation record. It is anchored on you; the findings it reaches separately are the valuable part.
3. A blind cold read: fresh evaluator, no memory, no `resources/` or git history, only the house prompt and the chapters. It scored Ch 6–10 noticeably lower than the in-session evaluator grading its own edits, and it caught the editor's bridging sentences as a different register.
4. Pairwise judging with both orders, full text, anonymised, and judges from another vendor, fitted with Bradley–Terry and bootstrap intervals; record whether the judge recognised the book.

Convergent findings from independent judges carry more weight than either alone (the 30 August Claude × GPT triangulation: Ch 4 best, Ch 8 most vulnerable, Ch 3's history to shrink, Ch 13 to keep). Where they diverge, say why (one ran ~0.5 higher throughout because it wasn't scoring against the anti-LLM rubric).

## Drift checks

- **Scale drift**: if three chapters now sit above the one that topped the last review, some of the rise is real and some is the evaluator liking its own edits. Say which.
- **Pushback drift**: if you change a score after the author objects, note it. Two re-judgments in a row, both in the book's favour, is a pattern to flag even when each change is defensible.
- **Self-knowledge**: say if you know which book is the author's (memory, an author page, a proof watermark). An incognito run or a sub-agent with stripped names is the closest the chat gets to blind.

## Eval loop inside an edit

Plan → implement → read the built output → evaluate against the same rubric → fix → repeat, two or three rounds. Report what each round changed, and that the rounds were your own. Hand the final version to a blind read or another vendor before calling a score.

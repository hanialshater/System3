---
name: de-llm
description: Remove the connective tissue that makes human prose read as LLM writing (recaps, signposts, paragraph-closing morals, re-explaining, reflexive hedges, X/Y antitheses, anaphoric runs, verb monocultures) while keeping the author's voice, stories and jokes. Use whenever the user says a chapter, post, essay or draft "feels like LLM writing", asks for a "de-LLM pass", "delete-and-fold", "X/Y pass", "remove the X-not-Y pattern", or complains about hedging, re-explaining, awkward conclusions, signposting or "when X becomes Y" — including for System 3 chapters, Coffee & Commute posts and blog drafts, and including after Claude's own edits.
---

# De-LLM

The ideas in a draft are rarely the problem. The LLM layer is the connective tissue between them: the sentence that announces the story, the sentence that re-tells it, and the sentence that turns it into a moral. The fix is almost entirely cutting. A good pass leaves a chapter 10–15% shorter with almost no new words.

## Workflow

1. **Get the real source.** Work from the git repo (or the file the author is editing now), never from an older PDF build. If the text has `<!-- ASSISTANT EDIT -->` markers, read them: Claude's own earlier additions are the first suspects.
2. **Measure before agreeing.** Run `scripts/tells.py` on the draft with the author's cleanest text as `--baseline` (for System 3, compare against the chapters the author calls most his own). A habit is a tell only where the draft leans on it harder than the baseline. Report the numbers, then the patterns with quoted examples. If the author's impression is wrong, say so.
3. **Name the habits, then the fix rules.** Group the hits into 2–4 habits with real quotes (see `references/catalogue.md`). Name the good lines that are getting buried, too. Then state the rules you will apply.
4. **One pattern family per pass.** De-LLM (recaps, morals, restatement, hedges), X/Y antitheses, and titles/closings are separate passes and separate commits. Mixing them makes review impossible.
5. **Apply with `scripts/apply_pass.py`.** Every edit is an exact-match replacement that must match once; a miss prints FAIL and skips, so the script survives later versions. Every edit carries a short reason.
6. **Re-read the seams.** Print the paragraphs around each cut. Repair any antecedent a cut orphaned ("those", "these", "the bargain") with the smallest possible word change, and flag it.
7. **Verify and deliver.** Re-measure (before/after/baseline table), run the project's gates, and deliver a patch, a `.txt` copy of the patch (downloads have arrived as zero-byte files), the apply script, and a change list with every cut in strikethrough plus its reason so the author can restore any line in seconds.

## Fix rules

- **Delete and fold, don't write.** Cut, or fold a run of sentences into one sentence of the author's own words. New wording is a last resort, and every new or recast word is flagged inline with `<!-- ASSISTANT EDIT (<pass name>): <what changed> -->`.
- **One conclusion per section.** The section's real conclusion (in System 3, the bold *Therefore*) is the only landing it gets. Every other paragraph ends on its last fact, action or joke.
- **A paragraph that has landed doesn't get a second landing.** Cut closers that label the paragraph ("This is science turning inward"), restate it, or announce the next heading.
- **If a sentence restates the one before it, delete the second.** Same for a point made three times across three paragraphs: keep the first telling.
- **A caveat stays only if it changes what the reader should do.** Epistemic humility lives in one place (an evidence note, a preface), not at the end of every paragraph.
- **Fold anaphoric runs.** Seven sentences starting with "We" fold into one sentence with a list. Keep a run only when the enumeration is the point and builds.
- **Trim question runs and tricolons to the strongest two.**
- **Recast X/Y antitheses** with the plain claim: "only", "as well as", "however many", "What changed was…". Cut the "not Y" half when the sentence before already says it.
- **Break verb monocultures.** If "become" (or any verb) is the default verb for change, replace it with the specific thing that happened. Leave the few that do a job.
- **Keep two or three of an opener tic** ("Suppose", "Consider", "Imagine", "Take") and recast the rest ("If…", "Say…", "Now…").
- **New section titles must be phrases already in the section.** Retire question titles, "What X Actually Is", "X, Not Y" theses and "Label: Topic" prefixes; keep titles that are the author's jokes or images.

## What to protect

Over-cutting is the second failure mode; it "cools" a chapter. Hani has flagged passes that left chapters cleaner and dead.

- Stories, experiments, coinages, images and every joke that lands. Name them in the report so the author sees they survived.
- Parallels that carry a joke or a real turn ("Nobody is lying. The hypothesis has been fitted to the result.").
- One-line paragraphs at the author's baseline density. They are part of his voice, not the tell. Offer the most verdict-like ones as optional cuts instead of cutting them.
- Purposeful enumeration that builds.
- Strong claims followed by "not literally" qualifications, first person, thinking in public, risky connections.
- Lines on the project's protected list (for System 3, see `references/system3.md`).

## Honesty about your own work

- Check Claude's earlier additions first and say plainly when they introduced the patterns. Revert them or cut each to a clause.
- Don't score Claude-written sentences as the author's. They need his voice pass.
- Don't fabricate evidence, figures, or autobiography to replace a cut.

## Reporting format

Keep the chat report short: the measured table (before, after, baseline), the habits with 2–3 quotes each, what went (counts by type), what stayed on purpose, files, and how to apply. Prose, minimal bullets. No closing summary paragraph.

## Files

- `scripts/tells.py` — detector: signposts, anaphora, antitheses, parallel pairs, hedges, closing morals, "become", opener tics, one-liners, question headings. `--list` prints every hit; `--only` filters.
- `scripts/apply_pass.py` — template for a pass: exact-once replacements, reasons, inline flags, JSON log, change-list Markdown.
- `references/catalogue.md` — each pattern with real before/after examples from System 3 passes. Read it before the first pass on a new text.
- `references/system3.md` — repo layout, gates (`check-eggs.sh`, footnotes, comment leaks, `check-tells.py`), protected lines and past numbers.

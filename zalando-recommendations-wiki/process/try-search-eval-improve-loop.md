# The loop: try, search, eval, improve, note

This wiki is not a finished spec. It's a working memory for an experiment in progress. Nothing in it should be trusted just because it's written down — including this file. The loop is how it earns trust over time.

## The five steps

1. **Try.** Take a note from this wiki (a pattern, a persona signal, a commentary rule) and actually apply it — generate a real recommendation or piece of commentary using it, against a real or realistic customer session.
2. **Search.** Before trusting your own read of what happened, look for outside grounding: is there research, a Zalando-published source, or a comparable industry practice that supports or contradicts what you just did? A hunch that survives a five-minute search is worth more than one that doesn't. See [../sources.md](../sources.md) for what's already been found — check there first so you're not re-searching ground already covered.
3. **Eval.** Score what you produced against [evaluation-rubric.md](evaluation-rubric.md). Be specific about *why* it passed or failed, not just that it did.
4. **Improve.** If it failed, fix the underlying note (the pattern, the persona description, the commentary rule) — not just the one output. A wiki entry that keeps producing bad output is a wrong wiki entry.
5. **Note.** Write one entry in [../notes/what-seems-to-work.md](../notes/what-seems-to-work.md) or [../notes/what-doesnt-work.md](../notes/what-doesnt-work.md). Update the `evidence:` tag on the note you tested (see the status vocabulary in [../README.md](../README.md)). If you found a real gap, add it to [../notes/known-gaps.md](../notes/known-gaps.md) or [../notes/open-questions.md](../notes/open-questions.md) instead of quietly working around it.

## Why this matters more than the content

A wiki full of confident-sounding claims that nobody has tested is worse than no wiki, because it's a source people will trust without checking. Every file in `patterns/`, `personas/`, `needs/`, and `styles/` carries an `evidence:` tag for exactly this reason — so a reader can tell, at a glance, whether they're looking at something grounded in outside research, something proposed but untested, something this project has since confirmed by using it, or something this project already tried and dropped.

If you're an agent working through this wiki and you notice a note is tagged `evidence: hypothesis` and you're about to rely on it for something that matters, that's the moment to run the loop on it — not just use it silently.

## What NOT to do

- Don't mark something `confirmed-by-use` because it sounds right or because a single output looked good. One good output is an anecdote, not a confirmation — look for a pattern across a handful of tries before upgrading a tag.
- Don't delete a `retired` note. Leave it with its pointer into `notes/what-doesnt-work.md` — a future agent re-discovering the same dead end costs more than the file taking up space.
- Don't skip the "note" step because the result seemed obvious. The obvious-in-hindsight results are exactly the ones worth writing down, because the next agent won't have your hindsight.

Related: [signal-checklist.md](signal-checklist.md), [generation-steps.md](generation-steps.md), [evaluation-rubric.md](evaluation-rubric.md), [../notes/README.md](../notes/README.md)

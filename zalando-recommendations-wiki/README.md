# Zalando Recommendations Wiki

*A standalone knowledge base for generating item recommendations with commentary on Zalando. This is an experiment: a working set of notes, not a finished doctrine — expect it to be wrong in places and to change as we test it.*

This wiki is detached from any other project in this repo. It doesn't assume you've read anything else here. Read this page, then follow the links.

## If you are a new agent, start here

You've been asked to generate an item recommendation, a piece of commentary explaining a recommendation, or to evaluate/improve one that already exists. Do this in order:

1. Read **[process/try-search-eval-improve-loop.md](process/try-search-eval-improve-loop.md)** — the method this whole wiki runs on. Notes here are not final answers; they carry a status, and you're expected to test them and update that status.
2. Read **[process/signal-checklist.md](process/signal-checklist.md)** — what you need to know about the customer before you infer anything.
3. Read **[process/generation-steps.md](process/generation-steps.md)** — the actual step-by-step for turning signals into a recommendation and a piece of commentary.
4. Pull in what you need, as you need it:
   - **[categories/](categories/README.md)** — what Zalando actually sells and how it's organized.
   - **[personas/](personas/README.md)** — behavioral customer archetypes and their signals.
   - **[needs/](needs/README.md)** — the problems a customer might actually have (size anxiety, comparison friction, etc).
   - **[styles/](styles/README.md)** — how to read and tag a customer's style.
   - **[patterns/](patterns/README.md)** — "for X, do Y" — the fast lookup table from situation to action.
   - **[commentary/](commentary/README.md)** — how to actually write the words, and how not to lie.
5. Before you ship anything, check **[process/evaluation-rubric.md](process/evaluation-rubric.md)**.
6. After you ship or test something, write down what happened in **[notes/what-seems-to-work.md](notes/what-seems-to-work.md)** or **[notes/what-doesnt-work.md](notes/what-doesnt-work.md)**. This is not optional — the wiki only gets better if you do this.

## Why it's structured this way

One big document is easy to write and hard to use. A page you're actually going to consult mid-task should answer one question and get out of the way, and it should tell you what else to read next. So: many small files, each about one thing, linked to their neighbors. If you're adding to this wiki, keep that shape — a new fact goes in an existing file if it fits, or becomes its own small linked file if it doesn't.

## Status vocabulary used throughout this wiki

Every claim of substance in this wiki should be tagged with one of:

- **`evidence: sourced`** — backed by a cited external source (research, Zalando's own published engineering/press material, industry data).
- **`evidence: hypothesis`** — a reasonable inference or design proposal, not yet tested against real behavior. Treat it the way you'd treat any untested hypothesis: usable, but watch for disconfirmation.
- **`evidence: confirmed-by-use`** — a hypothesis that has since been tested (per the loop in `process/`) and held up. Should point to the note in `notes/what-seems-to-work.md` that confirmed it.
- **`evidence: retired`** — tried and found wrong. Left in place with a pointer to `notes/what-doesnt-work.md`, so nobody re-discovers the same dead end.

See **[GLOSSARY.md](GLOSSARY.md)** for shared terms, and **[sources.md](sources.md)** for the full source list behind the `sourced` claims.

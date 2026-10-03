# Ledger template

One row per claim. Keep it in the evaluation record so the next check starts from it.

| ID | File:line | Claim (as written) | Kind | Source cited | Primary source checked | Independent coverage | Status | Action | Checked on |
|---|---|---|---|---|---|---|---|---|---|

**Kind:** fresh (after the cutoff or within the last year), number, quotation, history, attribution, status (present-tense: prize decided, model available, role held).

**Status:**
- **verified** — primary source read, matches.
- **verified (secondary)** — only reporting seen; primary unavailable.
- **corrected** — wording changed; old and new in the Action column.
- **softened** — now stated as the source states it ("reported", "proposed").
- **dropped** — couldn't verify; author may restore with a source.
- **author to confirm** — blocked source, private knowledge, or the author's own experiment.
- **re-check at print** — status still moving.

**Record format** (`resources/evaluations/YYYY-MM-DD-fact-check.md`): scope and base commit; method (what was searched, what was fetched, what was blocked); the ledger; corrections applied with flags; claims for the author; re-check-at-print list with dates; a closing line saying this is one editor's check, not an independent proofread.

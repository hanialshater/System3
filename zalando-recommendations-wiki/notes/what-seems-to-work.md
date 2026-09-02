# What seems to work

Confirmed or promising outcomes from actually running the [try-search-eval-improve loop](../process/try-search-eval-improve-loop.md). Newest entries at the top. Each entry: date, what was tried, what happened, what it confirms or upgrades.

Format:

```
## YYYY-MM-DD — short title

**Tried:** what was generated, against what kind of session/signals.
**Result:** what actually happened (an eval score, a real outcome, a read-back check).
**Confirms:** link to the pattern/need/persona/commentary file this supports, and whether its evidence tag should change.
```

---

## 2026-09-02 — first dry run: multi-need footwear comparison

**Tried:** A synthetic (not real-production) session, used to test whether the wiki is actually walkable end to end. Customer: established account, 4 past orders/18mo across two known brands (0 returns), 40 days since last order. Session: repeatedly switching between an ankle boot from a brand she's ordered from before (Brand A, size chart untouched — she already knows her size) and one from a brand she's never bought (Brand C, size chart opened twice, item saved, "waterproof" filter applied, no basket activity). Followed [process/generation-steps.md](../process/generation-steps.md) step by step: cleared the signal floor ([process/signal-checklist.md](../process/signal-checklist.md)), inferred three simultaneous needs (comparison friction — high; unfamiliar-brand trust — moderate; size anxiety, scoped to Brand C only — moderate), matched them to [patterns/for-comparison-friction-do-comparison-rx.md](../patterns/for-comparison-friction-do-comparison-rx.md), [patterns/for-unfamiliar-brand-do-surface-social-proof.md](../patterns/for-unfamiliar-brand-do-surface-social-proof.md), [patterns/for-size-anxiety-do-evidence-gated-fit-note.md](../patterns/for-size-anxiety-do-evidence-gated-fit-note.md), and [patterns/for-loyal-customer-do-reference-history.md](../patterns/for-loyal-customer-do-reference-history.md), and wrote a three-sentence comparison card (one explanatory job per sentence, help-seeker voice).

**Result:** Scored against [process/evaluation-rubric.md](../process/evaluation-rubric.md) pre-ship checks 1–7 — all passed, including traceability and fit-claim discipline. Checks 8–10 (outcome checks) are **not** scored — this was a synthetic dry run with invented signals, not a real session with real downstream behavior, and marking outcome claims "confirmed" from that would violate this wiki's own rule against upgrading a tag from one anecdote (see [process/try-search-eval-improve-loop.md](../process/try-search-eval-improve-loop.md)). What this run *does* confirm: the entry-point → process → patterns → commentary path in [README.md](../README.md) is actually walkable by an agent with no other context, and produces a rubric-passing output on a session with more than one simultaneous need, which the wiki hadn't been tested against before.

**Confirms / changes:** Surfaced a real gap while writing the Brand-A sentence — [commentary/hedging-fit-claims.md](../commentary/hedging-fit-claims.md)'s phrasing table only had tiers for aggregate evidence, with no row for "this specific customer's own completed, unreturned order history," which is stronger evidence than any aggregate tier. Fixed directly (table now has that row). Also surfaced that patterns are written one-need-at-a-time with no rule for composing several into one card — logged in [open-questions.md](open-questions.md) rather than guessed at. Neither `patterns/for-comparison-friction-do-comparison-rx.md` nor the other three patterns used here should be upgraded to `confirmed-by-use` yet — this run confirms they're usable together, not that they work in production.

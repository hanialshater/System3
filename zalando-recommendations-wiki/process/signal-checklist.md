# Signal checklist

*evidence: hypothesis, drawing on `evidence: sourced` inputs — see below*

Before inferring a persona, a need, or a style tag for a customer, check what you actually have. Inferring past your signal is the single most common way this kind of system produces confident-sounding garbage.

## Minimum viable signal set

A 2026 fashion-behavioral-segmentation framework names four signals as the primary predictors for segmenting a fashion shopper: **purchase frequency, category affinity, days-since-last-purchase, and return rate**. `evidence: sourced` — https://www.corradomanenti.it/en/behavioral-segmentation-in-fashion-a-2026-guide/

Treat these four as the floor. If you don't have at least a rough read on all four, don't assign a persona (see [../personas/README.md](../personas/README.md)) — fall back to the cold-start pattern instead ([../patterns/for-cold-start-do-honest-popularity-framing.md](../patterns/for-cold-start-do-honest-popularity-framing.md)).

## Session-level signals worth reading, if present

- Repeat visits to the same product(s) across days
- Switching between a small number of specific products
- Size chart opened (how many times, on which items)
- Items saved / added to a list
- Items added to and removed from basket
- Filters applied, and whether the customer abandoned after applying them
- Time spent per page, and whether it's declining across repeat visits (a sign of "already knows the content, still undecided")
- Search terms used, if query-driven (vs. arriving via a link or browse)
- Entry point (search, social link, email, direct) — this alone tells you a lot about how much context to assume
- Account status and order history depth (new account vs. established)

## What each signal is and isn't evidence for

A signal is *evidence toward* a need, not proof of it. Two customers switching between the same two products can be doing so for different reasons — one may have comparison friction, another may just be indecisive about something the page can't help with. Hold a need as a hypothesis with an intensity, not a certainty. This is the same caution [../needs/README.md](../needs/README.md) applies throughout.

## The floor for style inference

Style tags (see [../styles/README.md](../styles/README.md)) need their own minimum: at least a few viewed-or-saved items to derive a style cluster from, or an explicit style quiz answer. Don't infer style from a single view of a single item — one data point is a coincidence, not a preference.

## Anti-pattern: signal laundering

Don't let an assumption sneak in disguised as a signal. "She's probably size-anxious because most women are" is not a signal — it's a stereotype wearing a signal's clothes. If you can't point to something the customer actually did in this session or has a real history of doing, it isn't a signal.

Related: [generation-steps.md](generation-steps.md), [../personas/README.md](../personas/README.md), [../patterns/for-cold-start-do-honest-popularity-framing.md](../patterns/for-cold-start-do-honest-popularity-framing.md)

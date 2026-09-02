# Generation steps: from signals to a shipped recommendation + commentary

*evidence: hypothesis — this is a proposed procedure, not yet validated end-to-end. Run the loop on it (see [try-search-eval-improve-loop.md](try-search-eval-improve-loop.md)) and update this file as you learn.*

## The steps

1. **Read the signals you actually have.** Check against [signal-checklist.md](signal-checklist.md). If you're below the minimum viable set, skip to step 3 with a cold-start assumption.
2. **Infer a small, weighted set of needs.** Not one label — several candidate needs from [../needs/README.md](../needs/README.md), each with a rough intensity (high/moderate/low), each traceable to a specific signal from step 1.
3. **Infer a small, weighted set of style tags**, if you have signal for it (see [../styles/README.md](../styles/README.md)). Skip this for a cold-start session rather than guessing.
4. **Cross-check against a persona**, if useful. [../personas/README.md](../personas/README.md) exists to help you notice a need you might otherwise miss, or sanity-check that a need makes sense for this kind of shopper — not to override what steps 2-3 actually found.
5. **Look up the matching pattern(s).** [../patterns/README.md](../patterns/README.md) maps a dominant need to a concrete action. Start there before inventing a response from scratch.
6. **Decide: item, or knowledge?** Ask directly — does the dominant need actually call for another product (a retrieval/ranking answer), or does it call for information (a comparison, a confidence note, an explanation)? Defaulting to "show more items" for every need is the most common failure mode here.
7. **Check the evidence tier before writing any claim.** Especially true for fit and for personalization claims — see [../commentary/hedging-fit-claims.md](../commentary/hedging-fit-claims.md) and [../commentary/ground-claims-in-signals.md](../commentary/ground-claims-in-signals.md). If you don't have the evidence, say less, not more.
8. **Write the commentary.** Follow [../commentary/README.md](../commentary/README.md) — voice, one job per sentence (explain vs. persuade, not both at once), calibrated hedges.
9. **Record what you used.** Which signals, which needs and style tags you inferred, which pattern you applied, and why — so this can be evaluated (step 10) and so anyone asking "why was this shown" has a real answer.
10. **Evaluate before shipping.** Run it against [evaluation-rubric.md](evaluation-rubric.md).
11. **Close the loop.** Whatever you learn — including "this worked exactly as expected" — goes in [../notes/](../notes/README.md), per [try-search-eval-improve-loop.md](try-search-eval-improve-loop.md).

## A worked pass

Signals: customer has opened the same two pairs of trail shoes five times across five days, switches between them quickly, saved one, size chart untouched, no basket activity.

- Step 2: comparison friction (high, from the repeat-switching pattern), size confidence (low intensity — no size chart opens, so no strong signal either way, don't invent it).
- Step 3: style signal is thin here (only two items, both similar) — hold style loosely or skip.
- Step 5-6: [../patterns/for-comparison-friction-do-comparison-rx.md](../patterns/for-comparison-friction-do-comparison-rx.md) — this is a knowledge need, not an item need. More shoes would make it worse, not better.
- Step 8: a direct comparison of the two specific shoes on attributes the switching behavior suggests matter (cushioning, durability), not a generic "you may also like."

Related: [signal-checklist.md](signal-checklist.md), [evaluation-rubric.md](evaluation-rubric.md), [../patterns/README.md](../patterns/README.md)

# Evaluation rubric

*evidence: hypothesis, drawing on `evidence: sourced` commentary research — see [../commentary/README.md](../commentary/README.md)*

Use this before shipping a generated recommendation + commentary, and again after you have real outcome data on it. Score each dimension pass/fail, and write down *why*, not just the verdict — the why is what makes the note useful later in [../notes/](../notes/README.md).

## Pre-ship checks (you can score these without waiting for outcomes)

1. **Traceability.** Can every claim in the commentary be traced to a real signal or a real evidence source? If a sentence implies "we know X about you" and you can't name the signal behind it, it fails. See [../commentary/ground-claims-in-signals.md](../commentary/ground-claims-in-signals.md).
2. **Fit-claim discipline.** Does any sentence claim or imply how an item will fit? If so, is that claim gated by an actual evidence tier (see [../commentary/hedging-fit-claims.md](../commentary/hedging-fit-claims.md))? A confident fit claim with no data behind it is an automatic fail, not a minor deduction.
3. **Right species of answer.** Does the response type (item vs. knowledge) actually match the inferred need? Showing more items for a comparison-friction need fails even if the items themselves are well-chosen. See [../patterns/README.md](../patterns/README.md).
4. **Voice.** Is the commentary written help-seeker style ("I picked this because…") rather than help-provider style ("This is perfect for you because…")? See [../commentary/voice-help-seeker.md](../commentary/voice-help-seeker.md).
5. **One job per sentence.** Does any single sentence both explain and persuade? Flag it — see [../commentary/explain-vs-persuade.md](../commentary/explain-vs-persuade.md).
6. **Cold-start honesty.** If signal was below the minimum viable set (see [signal-checklist.md](signal-checklist.md)), does the copy avoid personalized-sounding phrasing? See [../commentary/cold-start-copy.md](../commentary/cold-start-copy.md).
7. **No silent gaps.** If coverage is limited in some way (only some items got commentary, some need went unaddressed), is that visible in the trace rather than hidden behind confident output for the parts that did get covered?

## Outcome checks (score these once you have real behavior data)

8. **Did the need actually go away?** For a knowledge/insight response, did the behavior the need was inferred from (repeated comparing, repeated size-chart opens, repeated returns) actually decrease afterward — not just did the module get clicked. A module can be clicked and still fail to resolve anything; a module can resolve the need and get zero clicks. Measure the need, not the click.
9. **Did the claim hold up?** If commentary made a fit or quality claim, did the outcome (return, complaint, positive follow-through) support it? If a "runs true to size" claim on this item keeps getting contradicted by returns, that's a signal the underlying evidence tier was mis-set, not just a one-off miss.
10. **Would a skeptical customer believe this?** Read the commentary back adversarially — is there a sentence that oversells, invents personalization, or asserts more confidence than the wiki's rules allow? If yes, it should have failed step 1, 2, or 6 above — treat this as a check on the checker, not just the output.

## After scoring

Write the result — pass or fail, and the specific reason — into [../notes/what-seems-to-work.md](../notes/what-seems-to-work.md) or [../notes/what-doesnt-work.md](../notes/what-doesnt-work.md). If a rubric item itself seems wrong or missing something, edit this file and say so in [../notes/open-questions.md](../notes/open-questions.md).

Related: [generation-steps.md](generation-steps.md), [try-search-eval-improve-loop.md](try-search-eval-improve-loop.md)

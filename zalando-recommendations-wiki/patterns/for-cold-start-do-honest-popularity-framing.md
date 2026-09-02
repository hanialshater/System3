# For cold start, do honest popularity framing — never fabricate personalization

**evidence: sourced**

## Trigger

Session is below the minimum viable signal set in [../process/signal-checklist.md](../process/signal-checklist.md) — e.g. a brand-new visitor arriving from a social link or ad, no account, no meaningful browse depth yet.

## Do

Show genuinely popular or trending items, anchored on whatever weak context you do have (the product they opened, season, rough location), with plain "popular this week" / "trending in [category]" framing. As real signal accumulates within the session (a filter applied, a second item opened), let the language graduate gradually — e.g. from "popular this week" to "popular with people who also looked at X" — rather than jumping straight to fully personalized phrasing.

## Why

This is standard cold-start practice: default to zero-personalization popularity signals, which are trivial to justify honestly, and blend in real personalization only as data accumulates. `evidence: sourced` — https://www.mlwhiz.com/p/cold-start-problem-recsys-modern-approaches. An abrupt jump from generic to confidently-personalized copy produces a "personality shift" that erodes trust in the system's consistency — the same source notes this as a specific, named failure mode of cold-start transitions.

## Don't

- Don't write "picked for you" copy the system has no basis for. Cold start is a normal state with its own honest design, not an error to paper over with confident-sounding language.
- Don't treat a single weak signal (one click, one page view) as enough to justify personalized phrasing — see the minimum viable signal set in [../process/signal-checklist.md](../process/signal-checklist.md).

## Related

[../process/signal-checklist.md](../process/signal-checklist.md) · [../commentary/cold-start-copy.md](../commentary/cold-start-copy.md) · [../commentary/ground-claims-in-signals.md](../commentary/ground-claims-in-signals.md)

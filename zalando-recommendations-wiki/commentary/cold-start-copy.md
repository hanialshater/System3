# Cold-start copy

**evidence: sourced**

## The rule

Below the minimum viable signal set (see [../process/signal-checklist.md](../process/signal-checklist.md)), default to honest population-level framing — "popular this week," "trending in [category]" — rather than fabricating a "picked for you" narrative. As real signal accumulates within the session, let the language graduate gradually.

## Why

Standard cold-start practice is to show what's popular/trending (trivially justifiable, zero fabrication) and blend in personalization only as behavioral data accumulates.

Source: https://www.mlwhiz.com/p/cold-start-problem-recsys-modern-approaches

An abrupt jump from generic to confidently-personalized copy produces a **"personality shift"** that erodes trust in the system's consistency — the same source names this as a specific, observed failure mode. The fix is a gradual transition in language, not an instant one: "popular this week" → "popular with people who also liked X" → fully personalized, tracking the actual accumulation of evidence rather than jumping ahead of it.

## Examples

- **Do (thin signal):** "Popular this week in jackets."
- **Do (a little signal):** "Popular with people who also looked at this."
- **Don't (thin signal, personalized-sounding):** "Picked just for you."

Related: [../patterns/for-cold-start-do-honest-popularity-framing.md](../patterns/for-cold-start-do-honest-popularity-framing.md), [ground-claims-in-signals.md](ground-claims-in-signals.md)

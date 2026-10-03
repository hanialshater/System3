---
name: fresh-claims
description: Fact-check a book, chapter, paper or post whose argument leans on recent, fast-moving or single-source claims, especially events after Claude's knowledge cutoff (2026 AI results, model releases, prize problems, company reports), plus the historical anecdotes, quotations, numbers and citations around them. Builds a claim ledger, verifies against primary sources with search, checks the same fact across chapters, rewords claims so they survive a later correction, flags disputes and source concentration, and audits footnotes. Use whenever the user asks to "fact check", "verify", "check the sources", "is this still true", "re-check before print", or asks about risks in a manuscript's evidence, and before any publication or print step for System 3.
---

# Fresh claims

A book about provenance can be caught without provenance. The exposure is concentrated in a few places: results weeks old, mostly reported by the organizations that did the work, often after Claude's knowledge cutoff. One walked-back claim in the preface costs more credibility than a dozen correct ones earn.

## Workflow

1. **Build the ledger.** Run `scripts/claims.py` on the chapter directory (`--only fresh` first, then `--only number`). Add the claims the script can't see: quotations, attributions, "first", "only", "largest", any sentence a hostile reviewer would check. Use the columns in `references/ledger-template.md`.
2. **Verify each fresh claim with search, every time.** Don't trust memory for anything after the cutoff, and don't trust the manuscript's own footnote as proof. Fetch the primary source (the organization's post, the arXiv paper, the prize committee's statement), then independent coverage. Check arXiv IDs and dates. If a source is blocked or the fetcher serves a stale copy, say so and list the claim for the author; don't mark it verified.
3. **Check history and quotations too.** Anecdotes drift in retelling. Check exact wording and the attribution chain of every epigraph and famous quote.
4. **Check consistency across chapters.** Run `--numbers` with the units the book uses (agents, hours, days, theorems, tokens, percent). The same event must carry the same numbers and the same source everywhere. Watch for conflations: peak concurrency vs total, launch-to-result time vs runtime, one project's figures cited to another's source.
5. **Audit the apparatus.** `--notes` finds duplicate footnote keys, undefined or unused notes, missing reference anchors, number clashes and dated "checked on" lines that need refreshing at print.
6. **Fix with the smallest wording change** and flag each one in the source. Then write the ledger and the corrections into `resources/evaluations/YYYY-MM-DD-fact-check.md`.

## Rules for wording

- **State it as the source states it.** "OpenAI reported", "a proposed proof", "addresses alternatives C and D; does not settle the unforced question". Put "at the time of writing" in the paragraph itself, not only in the note, when the status is pending.
- **Attribute disputes; don't adjudicate them.** Give each side's account, label them "the participants' accounts", and name affiliations that bear on credibility (Alpöge at Anthropic; Prove2Me's lead reported as an Anthropic researcher).
- **Drop what you can't verify** rather than keeping it with a hedge ("roughly sixty subagents"; "produced partly with an internal Anthropic model"). Tell the author so they can restore it if they hold a source.
- **Keep precision honest.** 41.6% vs the usual "more than five-twelfths" (≈41.7%); 2.636 vs later reported values around 2.6359–2.6360. Name the later results rather than leaving one comparison standing.
- **Fix sequence errors** (Lean checked the proof the day after the result, not after the announcement).
- **Don't fix voice while fact-checking.** A correction changes the fact and nothing else.

## Book-level checks

- **Evidence labels.** The Note on Evidence must match what each chapter actually reports. A chapter labelled "Run" without model, number of runs, time, cost and who "we" is needs a methods box or a relabel.
- **Source concentration.** Count primary sources by organization. If one lab supplies most of the key evidence, say so in the Note on Evidence and look for independent corroboration.
- **Present-tense status.** Prize decisions, model availability, policy, who holds which role: list every one for a re-check at print, with the date last checked.
- **Self-description.** "System 3" as a term has prior uses; a footnote acknowledging that is cheap insurance.

## Honesty about the check itself

Say what was verified directly, what only via secondary reporting, what against known literature, and what couldn't be checked from this environment. A fact check by one editor with search is not an independent proofread of the typeset pages; say that too. For legal exposure in disputes involving named people, recommend a legal read (not legal advice).

## Files

- `scripts/claims.py` — claim ledger (TSV), cross-chapter number check, footnote and reference audit.
- `references/cases.md` — real corrections from System 3, grouped by failure type.
- `references/ledger-template.md` — ledger columns, statuses and the record format.

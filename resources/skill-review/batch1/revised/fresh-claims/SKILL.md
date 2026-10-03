---
name: fresh-claims
description: Fact-check a book, chapter, paper or post whose argument leans on recent, fast-moving or single-source claims, especially events after Claude's knowledge cutoff (2026 AI results, model releases, prize problems, company reports), plus the historical anecdotes, quotations, numbers, citations and reference entries around them. Builds a claim ledger, reads each claim against its source, records what could and couldn't be reached, checks the same fact across chapters and against earlier corrections in git history, rewords claims so they survive a later correction, and audits the reference apparatus. Use when the user asks to fact check, verify claims or sources, asks "is this still true", or asks to re-check facts before print. Not for building or typesetting the book (pdf.py), not for checking line references in an edit log or scoring a chapter (development-edit), and not for prose or AI-tell passes (ai-tells, author-voice).
---

# Fresh claims

A book about provenance can be caught without provenance. The exposure is concentrated in a few places: results weeks old, mostly reported by the organizations that did the work, often after Claude's knowledge cutoff. One walked-back claim in the preface costs more credibility than a dozen correct ones earn.

The process below exists so nothing is skipped. It doesn't do the checking. The errors that matter are usually small: a paper that compared two models described as comparing versions, a benchmark credited to the lab that used it, "most effective" where the paper said "effective". You only find those by reading the claim and the source side by side.

## What "verified" means

A claim is verified only when the source supports **the sentence as written**, not just the event. Test four things separately and note each in the ledger:

1. **Subject**: who or what did it (this model, this team, this benchmark; who built or named the thing).
2. **Comparison**: what was compared with what (versions vs different models, peak vs total, launch-to-result vs runtime, humans vs agents on the same task).
3. **Qualifier**: the strength words (first, only, most effective, settled, about, over, all, never). "One of the fixes" is not "the fix found most effective".
4. **Attribution**: who said it. "The authors acknowledged…" needs the authors' words; if it's your inference, the sentence has to say so.

Also check that **the citation after the claim is the source of that claim.** This book cites at paragraph end, so a figure from one paper can sit in a paragraph whose only link is to another. Any quoted or paraphrased figure without its own source is a finding, even if the figure is right.

A claim that passes on the event but fails one of the four is **corrected** or **softened**, not verified.

## Workflow

Work on copies unless the author asks you to edit the repo. Record the date and base commit (`git rev-parse --short HEAD`) at the top of the record: every status in it is "as of" that date.

1. **Build the ledger.** From the repo root:
   `python3 <skill>/scripts/claims.py chapters --order book-design/curated/book-order.json --only risky --recent "Navier,ExploitGym"`
   Add `--files 08-automatic-alignment-research.md,00-preface.md` to scope it, and `--source-dates` for a full pre-print pass. Read the `source` column: `before:` means the claim is only cited earlier in its paragraph, and `shared-cite(n)` means n claims lean on one link. Both mean you need to check whether the source covers this sentence. `--only unsourced` lists figures and fresh claims with no citation after them. The script can't see descriptions of what a paper *did*, quotations, attributions or who the people are, so add those by hand. Use the columns in `references/ledger-template.md`.
2. **Read each claim against its source** using the four tests above. Don't trust memory for anything after the cutoff, and don't treat the manuscript's own citation as proof. Fetch the primary source (the organization's post, the arXiv paper, the prize committee's statement), then independent coverage. Check arXiv IDs and dates.
3. **Record access honestly.** Egress proxies block many primary sources (lab blogs, publishers). For every row, the ledger's Access column says **primary read**, **coverage only** or **not reached**. Never mark a claim "verified" from coverage when the sentence depends on the primary's exact wording; it is "verified (secondary)" at most. Every claim whose primary was not read goes on a **read-before-print list** for the author, with the URL.
4. **Check history and quotations.** Anecdotes drift in retelling (who left the room when, who won which game). Check exact wording and the attribution chain of every epigraph and famous quote. Where accounts conflict, say so; don't pick one.
5. **Check earlier corrections.** Run `python3 <skill>/scripts/regressions.py chapters --files <chapter>.md` from the repo root. It lists commits whose corrections later came undone, e.g. Ch 8's "the authors acknowledged that their test set had become a validation set", an attribution removed as unverified in ca80ba2 and back in the text since. Read `git show <hash>` before calling it a regression. Also read earlier `resources/evaluations/*fact-check*.md` records, if any, and `references/cases.md`. A correction that isn't in the current text is a ledger row, not something to assume.
6. **Check consistency across chapters.** Run `--numbers` (default units: agents, hours, days, theorems, tokens, percent) and `--numbers agents --near "Navier,Fermat,Riemann"` to compare one event's figures and qualifiers. The same event must carry the same numbers and the same source everywhere.
7. **Audit the apparatus, including the entries themselves.** `--notes` finds wrong or out-of-order numbers, links into another chapter's list, missing anchors, mixed title quotes and dated "checked on" lines. `--entries --files <chapter>.md` lists every entry the chapter cites, with flags. For each one, check authors, title, venue, pages, the date on the page itself (one off is common: 21 vs 22 January) and that the URL resolves to this work.
8. **Disclose relationships.** Name the ties between people in the text and the sources: a lab reporting its own result, a disputant employed by a competitor, an "amateur" who co-authored the cited paper. The text, or a note, should carry what a reader would want to know.
9. **Fix with the smallest wording change** and flag each one in the source as `<!-- ASSISTANT EDIT (fact-check): was "old wording"; source: ref-… -->`, the same flag form development-edit and ai-tells use. Chapter 13 is fiction and protected in full: leave it out (the script skips it by default). Don't explain or "correct" a confirmed seed in `resources/editorial/easter-egg-register.md`. Check `git log -p` and `resources/evaluations/*revert-list*` before changing a line the author restored or rewrote recently, and say so if you must. After applying corrections, run `bash resources/editorial/check-eggs.sh`; a correction that breaks a seed goes to the author instead.
10. **Write the record** to `resources/evaluations/YYYY-MM-DD-fact-check.md` (or the outputs folder you were given), in the format in `references/ledger-template.md`. It includes the as-of date, the read-before-print list and a **re-check-at-print** list of every fast-moving claim with the date last checked.

## Rules for wording

- **State it as the source states it.** "OpenAI reported", "a proposed proof", "addresses alternatives C and D; does not settle the unforced question". Put "at the time of writing" in the paragraph itself, not only in the note, when the status is pending.
- **Attribute disputes; don't adjudicate them.** Give each side's account, label them "the participants' accounts", and name affiliations that bear on credibility.
- **Drop what you can't verify** rather than keeping it with a hedge. Tell the author so they can restore it if they hold a source.
- **Keep precision honest.** Where a later result supersedes a comparison, name it rather than leaving the old one standing.
- **Fix sequence errors** (what happened the day after what).
- **Don't fix voice while fact-checking.** A correction changes the fact and nothing else. Never invent the author's experience to fill a gap; mark it `[AUTHOR: …]`.

## Book-level checks

- **Evidence labels.** The Note on Evidence (`chapters/appendix-note-on-evidence.md`) must match what each chapter actually reports. A chapter labelled "Run" without model, number of runs, time, cost and who "we" is needs a methods box or a relabel.
- **Source concentration.** Count primary sources by organization. If one lab supplies most of the key evidence, say so in the Note on Evidence and look for independent corroboration.
- **Present-tense status.** Prize decisions, model availability, policy, who holds which role: each goes on the re-check-at-print list with the date last checked.
- **Self-description.** If the book's coined term has prior uses, a footnote acknowledging that is cheap insurance.

## Honesty about the check itself

Say what was read in the primary, what only via coverage, what against known literature, and what couldn't be reached from this environment. A fact check by one editor with search is not an independent proofread of the typeset pages; say that too. For legal exposure in disputes involving named people, recommend a legal read (not legal advice).

## Files

- `scripts/claims.py`: claim ledger (TSV), cross-chapter number check, citation and reference-entry audit. `--help` lists the modes. Python 3.11+.
- `scripts/regressions.py`: corrections in git history that later edits reversed.
- `references/cases.md`: corrections proposed in earlier System 3 checks, grouped by failure type. These are lessons, not the state of the text.
- `references/ledger-template.md`: ledger columns, statuses and the record format.

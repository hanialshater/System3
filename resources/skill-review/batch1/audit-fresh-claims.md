# Audit: fresh-claims

Skill: `orig/fresh-claims` (SKILL.md 43 lines, references/cases.md 53, references/ledger-template.md 19, scripts/claims.py 125).
Repo: /home/user/System3 at `155c3a1` (2026-10-03). Read-only; nothing in the repo or skill folder was changed.
Improved script, recall harnesses and outputs: `scratchpad/author-skills/scratch-fc/` (`claims.py` = proposed version, `claims_orig.py` = untouched copy, `recall.py`, `hand.py`).

## Measurement summary

Two recall measures on the real book.

**Hand set (22 risky claims I picked from the text, independent of the script):**

| run | caught |
|---|---|
| original `--only fresh` | 1/22 |
| proposed `--only fresh` | 13/22 |
| proposed `--only fresh --source-dates` | 18/22 |
| proposed `--only risky --source-dates` | 22/22 |

The one the original catches is the control ("By April 2026, Claude Mythos Preview reached about 52x"). It misses all of these, among others: "Hugging Face cut off the intruder on 13 July" (Ch 8), "OpenAI has set agents on the Navier–Stokes Millennium Prize Problem" and "Anthropic has already had a team of parallel Claudes build a C compiler" (preface), "On September 11 the Clay Mathematics Institute said…" (Ch 6), "OpenAI's August report found failures…", "That group grew to roughly ten thousand concurrent agents", "In eleven days the agents produced…", "The agents reached 0.97 in five days…", "It was the only game Lee won", "the first doctorate in architecture Harvard ever awarded", "The biggest change in model training over the last two years".

**Citation-derived set:** the 43 body paragraphs whose citation points at an appendix entry dated 2025 or later. The original flags 16 of them (37%). The proposed version flags 22 (51%) with `--only fresh`, 28 (65%) with `--only risky --recent "Navier,ExploitGym,AlphaEvolve,Claude Code"`, and 36 (83%) with `--source-dates` added. Treat that last figure with care: `--source-dates` uses the same signal the set was built from, so it overstates. The hand set is the fairer number.

**Precision:** the original's 18 fresh rows are all real. Of the proposed version's 64 `--only fresh` rows, about 48 are real recent claims (≈75%). The noise comes from `fresh(context,…)` on general sentences that follow a 2026 date in the same section, such as "Six months of use leaves another trace." Those rows are labelled with a `?`, so the reader knows they are inferred.

**Row counts on the real book** (original → proposed): all 841 → 495; `--only number` 793 → 332; `--only unsourced` 793 → 238; `--only fresh` 18 → 64. The proposed `--only risky` mode gives 141 rows. Proposed runs leave out the protected Chapter 13 by default.

## Findings, in priority order

### 1. bug: the script does not run on Python 3.11 (already known)
Evidence: `python3.11 claims.py --help` gives `SyntaxError: f-string expression part cannot include a backslash` at claims.py:122. Python 3.12 accepts it. The environment's default `python3` is 3.11.15, so step 1 of the workflow fails before it starts.
Fix: compute the stripped text before the f-string:
```python
text = re.sub(r"\[\^[^\]]+\]", "", s)
print(f"{n}\t{','.join(kind)}\t{'yes' if hedged else ''}\t{','.join(refs)}\t{text[:220]}")
```
(The proposed script restructures this line anyway.)

### 2. bug: the script ignores this book's citation style, so `notes` is always empty and `--only unsourced` is the same as `--only number`
Evidence: the chapters contain no `[^footnote]` at all (`grep -c '\[\^' chapters/*.md` → all 0). They have 176 numbered links of the form `[n](appendix-references.md#ref-..)`. `classify()` collects refs only from `\[\^…\]` (claims.py:37). Every ledger row has an empty notes column: `awk -F'\t' '$4!=""' out.tsv` → only the header. `--only unsourced` prints 793 rows, the same as `--only number`, so it carries no information.
Fix: treat `CITE = r"\[(\d+)\]\(appendix-references\.md#([^)]+)\)"` as a source, strip it from the printed sentence, and count a sentence as sourced if its paragraph carries a citation. The book cites at paragraph end, and sometimes once for a multi-paragraph scene (Ch 8 ¶1–4). The proposed script prints `para:ref-…` in a `source` column.

### 3. bug: sentences that end in a citation are merged with the next sentence
Evidence: the split regex `(?<=[.!?”])\s+` (claims.py:29) needs the punctuation right before the space. With `trust.[1](appendix-references.md#…) Next`, a `)` sits there instead. 129 of the original's 841 ledger "sentences" contain a citation followed by another sentence, and 135 are cut at the 220-character print limit. In `--numbers` mode this attributes numbers to the wrong sentence: "60" and "88" percent are printed against "Paul Christiano's iterated amplification…" (num-orig.txt).
Fix: `re.split(r"(?<=[.!?”)])\s+(?=[A-Z“*(])", par)`, and split into paragraphs before sentences (the proposed `paragraphs()`), so that headings and subtitles don't fuse with the first sentence. For example, "*Aligning What You Cannot Outthink* In July 2026, OpenAI…" was one row.

### 4. gap: dates without a year are never fresh
Evidence: `classify` checks for a fresh year only inside the same sentence. Ch 8 ¶2–4 ("During training runs in May and June", "resumed in July", "on 13 July", "OpenAI's August report", "activity in May") and Ch 6 "On September 11 the Clay Mathematics Institute said the problem appeared to be settled" are all missed. These are exactly the claims most likely to move.
Fix (in the proposed script): carry the latest year seen in the section (reset at each heading). A sentence with a day-month, a month-day, a "in/on/by/’s + Month" phrase and no year of its own inherits that year and is labelled `fresh(date,2026?)`.

### 5. gap: undated claims about live events are never fresh
Evidence: preface line 25. The year is in the previous sentence ("It is September 2026 as I write this."), so "Anthropic has already had a team of parallel Claudes build a C compiler, and OpenAI has set agents on the Navier–Stokes Millennium Prize Problem" gets only `org:Anthropic`. The same happens to "That group grew to roughly ten thousand concurrent agents", "About four days after launch…" and "In eleven days the agents produced…" (Ch 6).
Fix (proposed script):
- `RECENT` covers versioned model names (Opus 4.6, Mythos, GPT-5+, Gemini n) and "Millennium Prize Problem".
- `--recent "Navier,ExploitGym"` adds the book's own live terms.
- `fresh(context,YEAR?)` marks number, org-report and reported-result sentences in a section after a recent year.
- `--source-dates` marks a claim fresh when its paragraph cites an appendix entry dated ≥ `--since`.
A bare "Claude" or "Claude Code" was tried first and dropped; it flagged "But which Claude?".

### 6. wrong: the docstring promises "organization plus a reporting verb", but the code flags any organization
Evidence: claims.py:12 says "named organization plus a reporting verb"; claims.py:35 and :39 flag the organization alone. So "Obviously some of it lives in Claude"-style rows sit next to "OpenAI's August report found…", and the two can't be told apart. Results reported by researchers without an organization in the list ("Gloaguen and colleagues' revised study found…", "In the Darwin Gödel Machine … from 20 to 50 percent", "In a field experiment with nearly a thousand…") get no label at all.
Fix: add a `REPORT` verb list and emit `org-report:X` against plain `org:X`. Add a `reported-result` kind for study/paper/experiment/et al./colleagues followed by found/showed/reported/went from/reached. Extend `ORGS` with Hugging Face, Redwood Research, METR, Epoch AI, Apollo Research and Google DeepMind (as one name). All of this is in the proposed script.

### 7. gap: no superlative or status detection, although SKILL.md step 1 asks for "first", "only", "largest"
Evidence: SKILL.md:12 tells the model to add "first", "only", "largest" by hand, and the script has no such check. A naive regex is useless here. In this book "record" is a theme word (provenance record), and "the first", "every", "never" and "most" appear on every page. My first attempt flagged 101 sentences, almost all noise.
Fix (proposed script), case-sensitive on purpose:
```python
SUPER = (r"\b([Tt]he first (?:to\b|person|system|model|team|doctorate|[A-Z]\w+)|first[- ]ever|"
         r"[Tt]he only (?:case|game|person|system|model|team|group|lab)\b|largest|biggest|fastest|best-known|best known|"
         r"(?:new|previous|prior|world) record|record-\w+|unprecedented|state[- ]of[- ]the[- ]art|all-time|never before)")
```
This gives 11 hits on the book, nearly all checkable: "It was the only game Lee won", Alexander's "first doctorate in architecture Harvard ever awarded", "their largest conference", "best-known packing", "Earth's biggest bookstore", "The biggest change in model training over the last two years". Add `STATUS` (at the time of writing, as I write, currently, has already …, remains open, no longer). Add a mode `--only risky` = fresh ∪ org-report ∪ reported-result ∪ superlative ∪ status. Then SKILL.md step 1 can say "`--only risky`" instead of asking for a manual hunt.

### 8. gap: `--notes` cannot see the errors this citation style invites
Evidence: on the real book the original prints one line, `DATED CHECK appendix-references.md: checked on 13 September 2026`. I injected three faults into a copy of chapters/: Ch 4 `[2]`→`[3]` for Wittgenstein, a misspelled anchor `#ref-04-octopuss`, and the preface citing `#ref-02-alphaevolve`. The original reported only the missing anchor and two "UNCITED ENTRY … (fine if listed as an additional source)" lines. It reported neither the wrong number nor the cross-chapter link. Its uncited check also counts every `<a id>`, so in a book with unnumbered "Additional sources" entries it would cry wolf.
Fix (proposed `--notes`, which caught all of them):
- `WRONG NUMBER`: the chapter's `[n]` does not match the entry's ordinal in the appendix.
- `OUT OF ORDER`: first-appearance numbers are not 1..k.
- `OTHER CHAPTER`: the anchor prefix (`ref-04-`) does not match the file prefix (`04-…`, `interlude-…`).
- `CROSS-CHAPTER`: the same anchor is cited from two files, which clashes with "numbering restarts in each chapter" (appendix-references.md:3).
- `UNCITED ENTRY` only for numbered entries.
- `DATED CHECK` also catches "at the time of writing" and "as I write".
On the real book the proposed version reports the apparatus clean apart from the three dated lines (preface "as I write", appendix "at the time of writing", appendix "checked on 13 September 2026").

### 9. stale: cases.md describes corrections that are not in the book
Evidence:
- cases.md:18 says "Riemann: 'roughly sixty subagents' couldn't be verified and was replaced by what is documented". chapters/06-pattern-language.md:253 still reads "Roughly sixty subagents developed and reviewed arguments". `git log -S"sixty subagents"` shows the phrase arriving on 2026-09-19 (0990663) and moving on 09-27 (db071ba), never removed. Either the correction was lost, or it never landed on main.
- cases.md:38 "Ch 2 'slightly above the 2.635 reference': several groups reported ≈2.6359–2.6360 after AlphaEvolve. Name them." Ch 2:209 still says "slightly above the 2.635 reference we had been using", and no later value is named anywhere in chapters/.
- cases.md:19 "'Produced partly with an internal Anthropic model' was dropped". Ch 6:277 now says "According to OpenAI, … the pair used an internal Anthropic model". It is attributed, so it may be the intended fix, but the case reads as if the clause is gone.
- cases.md:41 (Fisher/Jameson epigraph) and :53 ("System 3" prior-use footnote): neither the quote nor the footnote is in chapters/ or book-design/curated.
- cases.md:3 cites "System 3 fact checks (13 September – 1 October 2026)", but no `*fact-check*.md` record exists in resources/evaluations/, which SKILL.md:17 says each check writes.
Fix:
- Re-check the two live items (Ch 6 "sixty subagents", Ch 2 "2.635") as ledger items in the next run. Don't silently "fix" them from cases.md.
- Change cases.md:3 to: "Corrections proposed in System 3 fact checks (13 September – 1 October 2026), grouped by how the error happened. These are lessons, not a record of the current text: check the chapter before assuming a fix landed."
- Mark the Fisher and System 3 items "(not in the current text)".

### 10. gap: corrections can touch protected material, and no gate is run afterwards
Evidence: easter-egg-register.md:34 says "Chapter 13 … is protected in full. No edit pass, line edit or AI-tells fix touches it". The original ledger includes 12 rows from 13-the-prophecy.md (fiction). SKILL.md step 6 edits chapters but never mentions Ch 13, the confirmed seeds or `resources/editorial/check-eggs.sh`. The author's other editing skills do run gates (de-llm SKILL.md:18; dev-edit SKILL.md:55).
Fix: the proposed script has `--skip` (default `13-the-prophecy.md`). Add to SKILL.md step 6: "Chapter 13 is fiction and protected in full; leave it out of the ledger. After applying corrections, run `bash resources/editorial/check-eggs.sh`; a correction that breaks a confirmed seed goes to the author instead."

### 11. gap: "flag each one in the source" has no format
Evidence: SKILL.md:17. The sibling skills give a concrete form: dev-edit SKILL.md:54 (`CLAUDE DRAFT` / `ASSISTANT EDIT` comments with the old wording) and de-llm SKILL.md:22 (`<!-- … -->`). A model will invent its own, and dev-edit's checks won't recognise it.
Fix: replace step 6 with: "**Fix with the smallest wording change** and flag each one in the source as `<!-- ASSISTANT EDIT (fact-check): was "old wording"; source: ref-… -->`, the same flag form development-edit uses. Then write the ledger and corrections to `resources/evaluations/YYYY-MM-DD-fact-check.md`."

### 12. wrong/wasteful: step 1's `--only number` floods the ledger
Evidence: 793 rows out of 841. `NUM` matches the word "one" (in "one of its engineers"), list markers ("1.", "6."), names ("System 3", "Layer 0", "Reviewer 2", "Opus 4.6") and citation numbers. The model then either skims or burns a long context on it.
Fix: drop bare "one" from `NUM` and strip "Capitalised-word + number" and list markers before the number test (proposed: 332 rows). In SKILL.md step 1, use `--only risky` first, then `--numbers` for consistency. Keep `--only number` for a full pre-print pass.

### 13. gap: `--numbers` cannot see the conflations cases.md says to watch for
Evidence: cases.md:7–8 are about qualifier drift: "peak concurrent" against total, and launch-to-result time against runtime. `--numbers` groups only by unit across the whole book, so 'agents' mixes the hypothetical "twelve agents" (Ch 5) with Navier–Stokes. Identical values with different qualifiers are never reported. It also reads "Opus 4.6 agents" as 6 (or 4.6) agents, and "0.97 in five days" as "0.97 days" (it allows three arbitrary words, including numbers, between a number and its unit).
Fix (proposed): add `--near "Navier,Fermat,Riemann,ten thousand"` to compare only within paragraphs naming an event, and print the qualifier words between the number and the unit. Report a group when the values or the qualifiers differ. Skip model versions with `(?<![\d.])(?<!Opus )…` and don't let the gap words contain a number, "in", "and" or another unit. On the real book this surfaces: "ten thousand **concurrent** agents" (Ch 6:275 area), "a lab that decides which problem gets ten thousand agents" (Ch 10, uncited) and "Putting ten thousand agents on one problem" (Ch 12). That is the exact drift case cases.md:8 warns about, now visible.

### 14. gap: a cited number can sit in a paragraph whose only citation is a different source
Evidence: Ch 8 ¶105. "Two human researchers spent seven days … reached 0.23. The agents reached 0.97 in five days and about eight hundred cumulative agent-hours." The only citation in that paragraph is [31] `ref-08-w2sgen` (Burns et al., OpenAI, 2023). The figures come from [30] `ref-08-w2s` (Wen et al., Anthropic, 2026), cited in the previous paragraph. A reader who follows the nearest link lands on the wrong paper.
Fix: add to SKILL.md step 5: "For each fresh number, check that the nearest citation after it is the source of that number, not a background reference cited in the same paragraph." Script check: with `--source-dates`, flag `fresh(context,2026)` sentences whose paragraph cites only sources dated before `--since`. The proposed script already shows the contrast: those two rows are `fresh(context,2026?)` with source `para:ref-08-w2sgen`.

### 15. stale/gap: SKILL.md doesn't give the paths the run needs
Evidence:
- SKILL.md:12 says "Run `scripts/claims.py` on the chapter directory" but gives no path (`chapters/`) and no order file. The order file exists at `book-design/curated/book-order.json`.
- SKILL.md:30 "The Note on Evidence" lives at `chapters/appendix-note-on-evidence.md`.
- The original `--help` shows no examples (no `description=__doc__`), so a model asking `--help` learns nothing about the modes.
Fix: step 1 becomes: "Run `python3 scripts/claims.py chapters --order book-design/curated/book-order.json --only risky --recent "Navier,ExploitGym"` (and `--source-dates` for the full pass)." Name `chapters/appendix-note-on-evidence.md` in Book-level checks. Pass `description=__doc__, formatter_class=RawDescriptionHelpFormatter` to argparse.

### 16. polish: the appendix uses mixed quote styles
Evidence: `ref-12-flt-tokens` (appendix-references.md:473) uses ‘…’ for titles; every other entry uses “…”. That is a small apparatus inconsistency of the kind step 5 is for.
Fix: add a `--notes` line, `QUOTE STYLE`, for entries whose title quotes differ from the majority. Fix the entry itself in the next copyedit.

### 17. polish: the description over-triggers on print and build requests
Evidence: "…and before any publication or print step for System 3" would fire on "build the PDF" or "run pdf.py". The trigger word "verify" also overlaps with development-edit's "verify line citations" (repo commit 155c3a1).
Fix: replace the last sentence of the description with: "Use when the user asks to fact check, verify claims or sources, asks 'is this still true', or asks to re-check facts before print. Not for building or typesetting the book, and not for checking line references in an edit log."

### 18. polish: small wording and consistency issues in SKILL.md
- SKILL.md:22 names a living person's affiliation as a worked example inside a general rule. Keep the rule and move the example to cases.md (it is already there, :14), so the rule reads cleanly on another book.
- SKILL.md:15 lists units "(agents, hours, days, theorems, tokens, percent)", and the script docstring omits tokens. Make them match.
- ledger-template.md "Kind" has no `superlative` value; add it so it lines up with `--only risky`.

## Proposed new script checks (all in scratch-fc/claims.py, tested on 3.11 and 3.12)

| check | would have caught |
|---|---|
| numbered-citation parsing + paragraph-level sourcing | findings 2 and 14; "unsourced" becomes 238 meaningful rows instead of 793 |
| split after `)` of a citation; paragraphs before sentences | finding 3 (129 merged rows) |
| `fresh(date,YEAR?)` from section context | Ch 8 "13 July", "May and June", "August report"; Ch 6 "September 11" |
| `fresh(term)`, `--recent`, `fresh(context)`, `--source-dates` | preface Navier–Stokes / C compiler; Ch 6 ten thousand agents, eleven days |
| `org-report` vs `org`; `reported-result` | Gloaguen, Darwin Gödel Machine, field experiment |
| case-sensitive `superlative`, `status`, `--only risky` | "the only game Lee won", "first doctorate…", "biggest change…" |
| `WRONG NUMBER`, `OUT OF ORDER`, `OTHER CHAPTER`, `CROSS-CHAPTER` | injected faults the original missed |
| `--numbers --near` with qualifiers | "ten thousand concurrent" vs "ten thousand" drift |
| `--skip` (default Ch 13) | finding 10 |

All modes ran without error under python3.11 and python3.12, including `--order book-design/curated/book-order.json`. To reproduce the recall numbers, run `python3 scratch-fc/recall.py` and `python3 scratch-fc/hand.py scratch-fc` from /home/user/System3. The fault-injection copy was deleted after testing; its three `sed` lines are in finding 8.

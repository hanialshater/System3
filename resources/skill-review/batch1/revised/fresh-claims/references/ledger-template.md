# Ledger template

One row per claim. Keep it in the evaluation record so the next check starts from it.

| ID | File:line | Claim (as written) | Kind | Source cited | Source used | Access | Wording test | Status | Action | Checked on |
|---|---|---|---|---|---|---|---|---|---|---|

**Kind:** fresh (after the cutoff or within the last year), number, quotation, history, attribution, description (what a paper or system did), superlative (first, only, largest, most effective), status (present-tense: prize decided, model available, role held), relationship (a tie between a person in the text and a source).

**Source used:** the document you checked against, named (title or URL), not "search". Every row has one.

**Access:**
- **primary read**: you read the source itself.
- **coverage only**: the primary was blocked or not found; you read reporting about it. Name the outlet.
- **not reached**: neither. The row goes on the read-before-print list.

**Wording test:** the four tests from SKILL.md, e.g. `subject ok; comparison FAIL (different models, not versions); qualifier ok; attribution ok`. Note which one failed; "event happened" is not a test.

**Status:**
- **verified**: primary read, all four tests pass.
- **verified (secondary)**: coverage only, and the sentence doesn't depend on wording only the primary has.
- **corrected**: wording changed; old and new in the Action column.
- **softened**: now stated as the source states it ("reported", "proposed").
- **dropped**: couldn't verify; the author may restore it with a source.
- **author to confirm**: blocked source, private knowledge, or the author's own experiment.
- **re-check at print**: status still moving.

**Record format** (`resources/evaluations/YYYY-MM-DD-fact-check.md`):
1. Scope, base commit and **as-of date**.
2. Method: what was searched, what was fetched, what was blocked.
3. The ledger.
4. Corrections applied, with their flags. Earlier corrections found reversed (`regressions.py`).
5. Reference-entry fixes (dates, pages, URLs, quote style).
6. Relationships to disclose.
7. Claims for the author.
8. **Read before print**: each claim whose primary wasn't read, with the URL to read.
9. **Re-check at print**: each fast-moving claim (prize status, disputes, model availability, roles), with the date last checked.
10. A closing line saying this is one editor's check, not an independent proofread.

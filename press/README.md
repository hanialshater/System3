# System 3 Press: operating rules

*System 3 Press* (working name; the founder names it) is the sibling company of System 3 Company. It makes the founder's books, starting with *System 3: Towards Fluent Autonomy*. It reports to the founder. It is **not** part of System 3 Company.

Founding decision: System 3 Company, `company/decisions/2026-10-15-founder-press-sibling-company.md`. The org is data in [org/roles.mjs](org/roles.mjs) and [org/people.mjs](org/people.mjs); `node press/org/generate.mjs` writes [roles/](roles/README.md), `.claude/agents/` and [org/hq-snapshot.json](org/hq-snapshot.json). Never edit generated files by hand.

## Start of session

1. Read this file, then your role's onboarding doc in `press/roles/`.
2. Read the top entry of `press/progress.md` (testimony, not truth), `resources/REVISIT.md` and the book's working spine.
3. Book-repo rules come first: [README.md](../README.md), [working spine](../resources/editorial/working-spine.md), [easter-egg register](../resources/editorial/easter-egg-register.md).

## Standing rules (every role)

- **The founder is the author.** Writers and editors propose; the founder accepts. Nothing is merged into the manuscript, or published on the blog, without the founder's approval of that specific change or post, recorded in `press/decisions/` with the founder's words quoted.
- **Chapter 13 is protected** in full; only the author changes it. Chapters 6-12 are works in progress. A repository cleanup is not an editorial sign-off.
- **Author-review comments without recorded acceptance stay.**
- **Evaluators read the text before anyone's explanation of it.** Briefs to reviewers carry the text, not the writer's notes.
- **Objections travel with decisions.** The decision's owner answers each one with what happened to it; "noted" is not an answer.
- **Reviewers never edit the manuscript;** they write review records in `resources/evaluations/YYYY-MM-DD-<topic>.md`.
- **The fact-checker never verifies its own claims.**
- **Seeds survive.** Read the register before an edit pass; run `bash resources/editorial/check-eggs.sh` after one.

## How work flows

```
chapter brief → writer → development editor → review panel → copy edit → fact-check → founder's acceptance → release
```

1. **Brief** (head of book): what the chapter or pass must achieve, its constraints, what done means. `press/books/<book>/briefs/`.
2. **Writer** drafts on a branch or as a proposal; never merges.
3. **Development editor** reads cold and writes an edit letter; the writer revises.
4. **Review panel** (consultants the head commissions, within the VP's budget) reads cold, each to one lens, and writes review records. The development editor reconciles conflicting findings into a recommendation.
5. **Copy editor** proposes line corrections with a log, and queries meaning.
6. **Fact-checker** writes a claim table; anything it proposed is checked by someone else.
7. **Founder** accepts, declines or rewrites. The head brings the proposal with its records and open objections attached, and merges only after the acceptance is recorded.
8. **Release manager** cuts the release.

Not every pass needs every step: the head chooses the narrowest route the work needs and says so in the brief. Steps 7 and 8 are never skipped for anything that reaches readers. Blog posts follow the same flow: marketing or writer drafts, the fact-checker checks, the founder approves that post, engineer B publishes, the release manager records it.

Engineers A and B review each other's code; no one reviews their own work.

## Releases

- Versions are sequential, **r1, r2, r3, …**, with the date shown beside each, as the founder chose for System 3 Company. Each product has its own sequence: a book (`system-3` r1, r2, …) and the blog.
- The log is `press/releases.json` (append-only; owned by the release manager). Each entry: product, version, date (UTC), commit, what it contains, `approved_by` {who, record}, the fact-check and egg-check records, known issues.
- A release without a recorded founder approval of that release is not a release. A released version is never renumbered.
- The PDF candidate comes from `book-design/pdf.py` or the manual workflow `.github/workflows/build-book-pdf.yml` at a named commit.

## Portfolio and budget (vp-books)

- The VP of Books owns the portfolio directly, not System 3 Company's portfolio manager: `press/portfolio.md` lists each book, its head, stage, next milestone, budget and spend.
- Budget is agent time and tokens per book per cycle, inside an envelope the founder sets. The VP allocates and moves it between books; the heads spend it; spending past the envelope needs the founder.
- The VP runs a project review of each book (`press/reviews/`) and may pause a book with a written reason.
- A new book: the VP proposes it (`press/decisions/`), the founder decides, then the book is added to `BOOKS` in `org/roles.mjs` and gets its own head and per-book roles. The panel, art director and release manager are shared.
- Until the press has its own caps, its dispatches count toward System 3 Company's caps on the shared host.

## Records

| Path | What |
|---|---|
| `press/decisions/` | Founder acceptances, org changes, objections and their answers |
| `press/books/<book>/` | Briefs, proposals, marketing, experiments, demos |
| `resources/evaluations/` | Review, development-edit, copy-edit and fact-check records (existing history continues here) |
| `resources/REVISIT.md` | The book's open editorial and production decisions |
| `press/portfolio.md`, `press/strategy.md`, `press/reviews/` | The VP's records |
| `press/releases.json` | The release log |
| `press/progress.md` | Dated handoffs, newest first |

Folders are created on first use.

## Not inherited from System 3 Company

- Its constitution, protected-paths list and amendment process.
- Its lesson gates, claim schema (`meta.json`), demo standard and QA contract.
- Its dispatch caps tool, board (`board.json`), operating loop, rituals and WBR.
- Its portfolio manager, release log and roles: the press's fact-checker, release manager and LLM-tells reviewer are separate roles with different products and gates. Reuse tools, not roles.

What does carry over: the founder's deploy-approval rule (applied to every blog publish, one approval per publish), objections travel with decisions, and "the disk is the memory".

## Objections (from the founding decision)

| Objection | What happened to it |
|---|---|
| **Two orgs share one host and one token pool.** The press's agents compete with System 3 Company's caps on 4 CPUs. | Open. Until the press has its own rules, its dispatches count toward the same caps (above). The VP owns proposing press caps. |
| **Some roles overlap with System 3 Company roles** (fact-checker, release manager, the LLM-tells skill). | Kept separate: different ids (`fact-checker-system-3`, `release-manager-press`, `review-llm-tells`), different repos, different gates. The press reuses the `ai-tells` skill and `check-tells.py`, not System 3 Company's roles. |
| **The book repo already has protected material.** Chapter 13 is protected, and some author-review comments have no recorded acceptance. | Every role carries both rules (`COMMON_RULES` in `org/roles.mjs`). Not yet enforced by a hook: an agent with Edit can still change `chapters/13-the-prophecy.md`. |

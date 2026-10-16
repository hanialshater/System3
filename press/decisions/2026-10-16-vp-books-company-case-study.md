# VP decision: commission a case-study evidence record for *System 3* from System 3 Company's 15-16 October incidents

owner: vp-books (Maren)
date: 2026-10-16
class: portfolio / commission (book: system-3)
route: founder (asked through System 3 Company's chief of staff, board W-1177 in that repo) → vp-books (this record) → founder (the acceptances below) → head-of-book-system-3 (brief and dispatch) → experiment-developer-system-3 (record) → fact-checker-system-3 (check) → head-of-book-system-3 → founder
recorded by: vp-books
status: **go, decided by vp-books, conditional on the founder's acceptances below.** Nothing has been commissioned or dispatched. No manuscript file changes under this record. Work starts only once the founder's answer is quoted in this file.

## The question
The founder, through the chief of staff: should the press commission a case study for *System 3: Towards Fluent Autonomy* from the company's last two days and, if so, which press role writes it and when? The founder's framing: the company exists to test the book's ideas, above all the philosophy of science of how fallible agents work together, and also the founder's experience running organisations at scale at Amazon and Zalando.

## Decision

1. **Go, as an evidence record, not as prose.** The deliverable is a case-study record: each incident with its sources (commit, file, line), what happened, what it supports and what it does not, and its evidence category. It is the material a chapter passage or appendix could rest on. Whether any of it reaches the manuscript, and where, is a later proposal for the founder, made only after this record has been checked.
2. **Writer: experiment-developer-system-3 (Ilya).** That role's job is records that can be rerun, and it may not upgrade an evidence category or change a reported result (`press/roles/experiment-developer-system-3.md`). That is the right discipline for this material. **Not writer-system-3, not in this cycle.** A writer drafting the story first would produce prose before the evidence and invite the coherent-but-wrong account the book warns about. The writer comes in only if the founder accepts a manuscript proposal built on the checked record.
3. **Checker: fact-checker-system-3**, against the System 3 Company sources, not against the experiment developer's summary. The experiment developer tells the fact-checker what each entry supports (its role file says so), and the fact-checker checks that.
4. **Brief and dispatch: head-of-book-system-3 (Theodora)**, who writes the brief at `press/books/system-3/briefs/` and runs the route. I do not dispatch anyone.
5. **Where the record lives:** `press/books/system-3/experiments/2026-10-company-case-study/` (record, the planted-bug harness, a per-entry "supports / does not support" note). The fact-check goes in `resources/evaluations/YYYY-MM-DD-fact-check-company-case-study.md`.

## Scope

- **One evidence record, appendix-shaped, that serves Chapter 5 (*The Society of Agents*) first.** Chapter 5 is the book's "many knowers" chapter (working spine: records, standards, specialists, instruments, independent witnesses), it already carries the founder's Amazon story, and the Note on Evidence lists it as "Argued from history". These incidents are the first chance to add evidence from a running organisation of agents to that argument.
- **Secondary uses, named so the record is built to fit them:** Chapter 8 (*Scalable Oversight*: the overseer is not ground truth; incident 6) and the Interlude (objections keeping their consequences: incident 1's COE and its actions). The Note on Evidence's table gets a row only if the founder accepts a manuscript change.
- **Not in scope:** chapter prose; Chapter 13 (protected; nothing in this record touches it); Chapters 6-12 (works in progress; no passage is proposed for them under this record); any Amazon or Zalando comparison in the author's voice. If the founder wants the comparison with running organisations at scale, the founder supplies it in writing. The experiment developer may list the questions to ask (for example "did a deploy-marker class of incident happen at Amazon or Zalando, and what was fixed: the person or the mechanism?") but may not answer them.
- **Not this commission:** running the Note on Evidence's "A Test Still to Run" (the planted false diagnosis, conditions A-D). The company could host that test, and the founder may want it, but it is a designed experiment with its own protocol and budget. Incidents 2 and 3 are anecdotes in the same area, **not** results of that test, and the record must say so.

## Evidence categories, per candidate

The book's categories are those in `chapters/appendix-note-on-evidence.md` (Run, Reported, Argued, a design, Prototyped, Lived, illustrative, Fiction). The brief's four (run, argued, designed, imagined) map onto them. The rule for this record is the book's: **a reported result has a reproducible record.** An incident observed once in operation is not a run experiment. The record calls it *observed, with a re-checkable record* (the commits and files can be reread). It calls something *run* only where a script reruns it from a committed file. **Imagined: none.** The book's stories may be composites (Note on Evidence, paragraph 2). This record may not: no composite, embellishment or changed detail. If the founder later wants a story built on it, that story is labelled illustrative and is not evidence.

| # | Candidate | Category the record may claim | What makes it reproducible, or what is missing |
|---|---|---|---|
| 1 | r7 reached production before founder approval because a commit body quoted the deploy marker; the fix targets the mechanism | Observed (COE `company/rituals/records/2026-10-15-coe.md`); the trigger mechanism is **run**, because the ignore-command logic can be replayed against commit aefb10a's message | Replay script committed with the record. The fix's effect (W-1051..W-1054) is **designed** until those actions close and are tested; the record says which have closed. |
| 2 | The chief of staff's brief gave six reviewers a verdict word the tools do not accept; one followed its role file and corrected it | Observed, n=1 event. "One in six" is a count, not a rate | The record must cite the brief, the six review records and the tool's accepted words. I did not locate the brief or confirm the count; the experiment developer establishes it from the files or drops it. |
| 3 | The chief of staff gave the founder a wrong Neon setup step; the backend engineer's independent read caught it | **Unconfirmed.** The cited record (`company/decisions/2026-10-15-founder-f01-accounts.md`, "Founder setup") shows "after the corrected steps" and a later correction **in the founder's words** ("Ah i did not do prod just dev and preview"). It does not show who caught the wrong step | The account in the request may be right, but the cited source does not carry it. Establish it from the sources or drop it. This is itself an instance of the book's point: the summary is not the record. |
| 4 | A builder reported reverting a config edit that was still in its commit; caught by reading the diff on disk | Observed, if the commit and the report are both found | `git show` of the commit beside the report, both cited. I did not locate the source. |
| 5 | Falsification over confirmation: the test authors planted 10 bugs; the ops reviewer planted 12 different ones (all caught) | Closest to **run**. Today it is **reported**: both harnesses were "in scratch, not committed" (`company/engineering/readiness/2026-10-15-lifehacks-study-tp3-tp4-tp5.md`) | It becomes run only when the experiment developer reruns the planted bugs from a harness committed with the record, at the named commits, and gets the same result, or reports a different one. A scratch copy of the ops harness still exists on the shared host today and will not survive, so this is the first item in the queue. |
| 6 | The founder's rule that managers, not the coordinator, decide each lane's work (scalable oversight) | **Designed** (`company/decisions/2026-10-16-founder-org-and-dispatch-rule.md`, `company/ceo-office/poc-map.md`). One day old; its effect is unmeasured | The founder's words are quoted in that record. No outcome may be claimed; the record may state what would show the rule working or failing. |
| 7 | The honest limits: one model in many roles, the coordinator as hub, no real learners yet | **Argued**, and mandatory | It travels with every entry, not only at the end. "One model in many roles" is the book's own "copies of one model are one witness": every catch in 2-5 is one copy of a model catching another, and the record may not present that as independent witnesses. |

## When

- **Now, as soon as the founder accepts below.** Sources are freshest now, and item 5's harness is at risk.
- **Order:** item 5 (capture and rerun the harness), then 1, 4, 2, 3, 6, with 7 written alongside each.
- **Done** means the record and the fact-check are both written, and the head of book brings the founder the checked record and a one-paragraph recommendation: appendix, Chapter 5 passage, or neither. This cycle's target is within 7 days of acceptance. The head stops the pass if it is not converging.

## Budget (vp-books owns it)

The founder has not yet set the press's envelope (`press/progress.md`, 2026-10-15: "sets the budget envelope (owner: founder)"), and `press/portfolio.md` does not exist yet. With no envelope, I cannot place this inside one. So this allocation is **a proposal that needs the founder's approval** before any spend:

| Item | Dispatches | Cap |
|---|---|---|
| head-of-book-system-3: brief, routing, recommendation | 1 | 0.3M tokens |
| experiment-developer-system-3: record and harness rerun (one rework round included) | up to 2 | 1.5M tokens |
| fact-checker-system-3: check | 1 | 0.5M tokens |
| Writer, panel, art | 0 | 0 |
| **Total** | **up to 4** | **2.3M tokens; hard stop, no overrun without the founder** |

These dispatches count toward System 3 Company's caps on the shared host (`press/README.md`, Portfolio and budget). When the envelope exists, I record this spend in `press/portfolio.md`.

## What the founder must accept (quote the answer here)

1. **The go and the route above**, including that the first output is an evidence record and not prose, and that no manuscript change follows without a separate proposal and acceptance.
2. **The budget**: 2.3M tokens and 4 dispatches for this work, as a standing approval or as part of the envelope the founder sets.
3. **Publishing internal company material.** The record will quote System 3 Company's commits, records and some of the founder's own words to the company (for example "yes, deploy r7"). The founder says whether the founder's words to the company may be quoted in the book, and whether the company's internals (URLs, names of databases and services) may be named or must be generalised. No credentials or values are ever copied.
4. **The no-composite rule for this material.** Unlike the book's stories, this record does not change or combine details. If the founder prefers a composite, it is labelled illustrative and stops being evidence.
5. **Clearance.** Any link the founder makes to Amazon or Zalando joins the existing clearance item in `resources/REVISIT.md` (employer communications and legal review).

**Founder's answer:** _(awaiting; record it here, quoted, with the date)_

## Objections

| Objection | Raised by | What happened to it |
|---|---|---|
| **The witness and the subject share a model.** The press's roles and the company's roles are copies of one model. A case study of the company by the press is the book's "one witness" problem, applied to itself. | vp-books | **Kept in scope, not solved.** Item 7 is mandatory in every entry. The record claims only what the files show, not that the catches were independent. The founder's own reading is the only witness from outside the model. Running the Note on Evidence's test (conditions A-D) is the real remedy, and I have named it above as a separate option. |
| **The account came through the coordinator whose errors are among the incidents** (items 2 and 3 are the chief of staff's). The candidate list is that coordinator's summary. | vp-books | **Answered by the route.** The experiment developer reads the System 3 Company sources first and the candidate list only afterwards (evaluators read the artifact before the account). The head of book's brief carries the source paths, not this record's or the chief of staff's characterisations. Item 3 already fails to match its cited source; the record will show that. |
| **This is outside the experiment developer's stated lane.** Its role file speaks of experiments, and most of these are observed incidents. | vp-books | **Accepted as a fit, with a limit.** Its in-scope work includes "experiment specs and records" and "reproducing results the manuscript reports", and its may-nots (no category upgrades, no result changes) are what this material needs. If the founder or the head of book judges that this is a new kind of work, it becomes an org-change proposal for the founder. I do not create or rescope roles. |
| **Spending before the envelope exists.** | vp-books | **Blocked until the founder answers point 2.** No dispatch happens until then. |
| **Two days of incidents may be too thin, and too flattering, to carry a book's evidence.** | vp-books | **Built into the deliverable.** The head of book's final recommendation may be "neither": no appendix, no passage. That is a successful outcome of this commission, not a failure. |
| **Item 5's harness may be lost before anyone captures it** (it lives in session scratch). | vp-books | **Open, time-bound.** It is first in the queue once the founder accepts. If it is lost, item 5 is reported as testimony from the readiness record, unless the experiment developer writes and commits a new harness, in which case it is reported as a new run, not a rerun. |

## Sources read for this decision
- `press/README.md`, `press/roles/vp-books.md`, `press/roles/experiment-developer-system-3.md`, `press/roles/writer-system-3.md`, `press/progress.md`
- `chapters/appendix-note-on-evidence.md`, `resources/editorial/working-spine.md`, `resources/REVISIT.md`
- System 3 Company: `company/rituals/records/2026-10-15-coe.md`, `company/decisions/2026-10-15-founder-f01-accounts.md`, `company/engineering/readiness/2026-10-15-lifehacks-study-tp3-tp4-tp5.md`, `company/decisions/2026-10-16-founder-org-and-dispatch-rule.md`, board W-1177. Not located by me: the sources for items 2 and 4.

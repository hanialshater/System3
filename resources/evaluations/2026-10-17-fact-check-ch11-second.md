# Fact-check (second, independent instance): Chapter 11 revision 1 ("Guess First")

fact-checker-system-3, second instance (Beckett) · 2026-10-17 · text: `chapters/11-the-store-that-builds-itself.md` at book commit `322ffac` (169 lines; line numbers below are at that commit) · company sources: `/home/user/system-3-company` read-only, pinned to `e84b8784` (2026-10-17 14:21:02Z) and drift-checked at its head `42738e6d` (15:58:12Z); GitHub API (read-only) for history the shallow clone does not hold; public site fetched 2026-10-17 16:34:09Z.

I did not write any sentence, value or wording in this chapter, and I am not the instance that wrote `resources/evaluations/2026-10-17-fact-check-ch11-draft.md`. So I may verify that instance's values and wordings. Every fix I propose below is mine, so each one is marked **needs independent check**. I may not verify my own fixes.

Order of work: I read the chapter cold and saved my claim list before I opened the writer's source map (`/tmp/.../scratchpad/cold-notes.md`, not kept). I used the source map only as a pointer to files. I checked every verdict against the primary file or by running code myself, and none rests on the first checker's verdict. A copy editor is changing punctuation at the same time, so I judged claims and ignored punctuation.

## Summary

- **Rows: 105.** **Verified 98** · **correct-with-value 4** · **disputed 2** · **unverifiable 1** (the author's own store account, which is his to confirm).
- **Second-check list S1-S11 (source map, Revision section):** S1, S2, S3, S5, S6, S7, S8, S9, S10 and the five S11 wordings (items 1, 2, 3, 20, 26) are **verified**, with one exception inside S11. Item 26's sentence (L71) is **disputed** on its first half, "All of these roles run on one vendor's models". The other exception is S4, a note that is not in the prose: it is **correct-with-value**, because the replay matches the marker in four saved messages, not only `aefb10a`.
- **New X items:** R2.1 (founding date), R7.12 (what the Safari record names), R8.3 (the recall answer) and R8.4 (no recall data) are **verified**.
- **Required fixes (4 in the prose):**
  1. L69: "269" should be **268**.
  2. L97: "852 … 10" is the company's count, and the "10" runs only to mid-afternoon on the 16th. Attribute both numbers and narrow the window.
  3. L71: "All of these roles run on one vendor's models" is contradicted by the company's own records, which show a Codex-implemented platform/release role, an illustrator role specified for OpenAI image generation, and `codex/` PR branches.
  4. L91: the warning "A society of agents can turn into one coordinator with an org chart attached" is presented as this book's warning. I can't find it in the book.
- **Pre-release refresh items** (R5.13, R6.3, R6.7, R7.6, the five-learner test, R8.6): all are unchanged between `e84b8784` and the head `42738e6d`. On the public site, every production deploy attempt on 17 October failed, and production still serves the 15 October tree.
- **Confidence:** high on the counts, code behaviour and quotations. I reran them, and none rests on the first instance's verdict. Moderate on the absences ("no figure for money", "no other launch-review override"), which rest on searches that can miss a phrasing.

## Required fixes (exact wording; each needs independent check)

| # | Line | Now | Proposed (needs independent check) | Why |
|---|---|---|---|---|
| F1 | 69 | "There are 269 of them." | "There are 268 of them." | `grep -c '^## '` on `company/ops/progress.md` gives 269, but one of those lines is the entry template `## YYYY-MM-DD · <role> · <one-line summary>` inside a code block (line 2221). The dated notes number 268 (`grep -c '^## 20'`), the same at `e84b8784` and at `42738e6d`. |
| F2 | 97 | "Across 13 and 14 October the company made 852 new lessons. Across the next two days it made 10." | "By its own count, across 13 and 14 October the company made 852 new lessons, and across the next day and a half it made 10." | The 852/10 table is the chief of staff's (`company/decisions/2026-10-16-founder-throughput-for-10k.md` line 13). The ops diagnosis it rests on gives 451 for 10-14, 0 for 10-15 and 10 for "10-16 (to ~15:00Z)" (`company/engineering/operations/2026-10-16-throughput-diagnosis.md` §2). By midnight UTC on the 16th the default branch held 1,081 lesson files, against 969 at 14:23Z. That is 112 more on the 16th: 100 Books drafts merged through PR #5 and 7 agent builds. My own count of lesson files on the default branch (GitHub trees API) is 28 at the end of 12 Oct and 960 at the end of 14 Oct, so +932 rather than 852. The method may differ, so I do not propose my number. I propose attributing theirs. |
| F2b | 97 | "new builds took 8% of the day's 18.65 million tokens" | "new builds took 8% of the 18.65 million tokens measured by mid-afternoon" | The diagnosis measures 00:00 to 14:23Z only ("the ledger stops at 14:23Z", objection 8). Minor. "By its own count" already covers the source. |
| F3 | 71 | "All of these roles run on one vendor's models, through an account with usage limits the company has already hit." | "Almost all of this work runs on one vendor's models, through an account with usage limits the company has already hit." (Alternative, if the author prefers a narrower true sentence: "The agents it dispatches run on one vendor's models, …") | (a) `tools/org/roles.mjs` lists `illustrator` ("external contributor, image generation", `external: true`, no model). `company/design/illustrator-prompt.md` line 1 reads "Prompt for the external illustrator (ChatGPT image generation…)", and line 24 cites "OpenAI's terms". It has delivered nothing: 8 requests are `open` and the inbox holds only a README. (b) `company/ops/progress.md` lines 2259 and 2265 are handoffs headed "platform-engineer / release-manager (Codex implementation)" (13 Oct), and `company/ceo-office/2026-10-13-role-evaluation.md` line 120 says "Codex session (deploy tooling)". (c) PRs #1, #2 and #6 come from branches `codex/vercel-deploy-function`, `codex/lifehacks-200` and `codex/algorithms-200` (GitHub API), which brought about 400 lessons in. The founder's account authored 15 commits by `e84b8784`. Which tools made those is the author's to say (author query A1). |
| F4 | 91 | "The first is the hub. A society of agents can turn into one coordinator with an org chart attached, and the organization becomes the bug." | "The first is the hub. This book warns that an org chart does not make agents a society, and that the organization itself can become the bug." | The book says "The organization was the bug" (Ch5:28) about a shared bottleneck: all agents converged on one Linux failure. Ch5:174 mocks titled agents in conversation ("perhaps reality will be intimidated by the org chart"). Neither warns about one coordinator. Ch5:18 praises a project with "no orchestrator", while Ch3:291-341 builds one. I searched every chapter except 11 for coordinator, hub, orchestrator, "org chart attached" and bottleneck: no hub warning. The company result itself (the retrospective) is verified. Only the attribution "Two are this book's" fails for the first warning. If the writer knows a passage I missed, citing it closes this. |

Fix to a note outside the prose (source map, §5 "moved out", S4):

| # | Where | Now | Proposed (needs independent check) | Why |
|---|---|---|---|---|
| F5 | source map §5 moved-out note | "`replay.sh` … matches the marker in `aefb10a` only" | "matches the marker in `aefb10a` and in neither of the incident's other two commits (`e6805f4`, `d8f5f89`). It also matches `54aa64e3` (17 Oct, which deployed nothing) and the two commits that carried the marker on purpose (`f868127`, `6cbce514`)." | I reran `replay.sh` (TMPDIR in my scratchpad). It returns BUILD for 54aa64e3, 6cbce514, aefb10a and f868127, and skip for d8f5f89 and e6805f4. Its saved `vercel.json` and all six saved messages are byte-identical to GitHub's copies. The category "the filter's part is run" is right. |

## Author queries (the fact-checker may not answer these)

- **A1 (L71, L39, L63).** Four PRs came from your GitHub account, three of them on `codex/` branches: the deploy pipeline (#1), 200 Life Hacks (#2), 100 Books drafts (#5) and 200 algorithm drafts (#6). The company's log calls one of them a "Codex implementation". What made them? If another developer's agent made a fifth of the catalogue, the chapter's "one vendor" and "one model family" sentences need your wording, and it may be the outside witness L39 says is scarce.
- Existing permission comments (L99, L145) still ask you to confirm the two quotations. I confirm only that each is verbatim in its record (S3, S8).

## Claim table

V = verified · CWV = correct-with-value (fix above) · D = disputed · U = unverifiable. CR = company repo at `e84b8784` unless stated.

### §1 Ninety-Nine Percent Accurate

| # | L | Sentence (abridged) | Source | Status | Note |
|---|---|---|---|---|---|
| 1 | 7 | Title *You tested positive. Now what?*; hook "The test is 99% accurate. So you're 99% likely to be sick. Right?" | `src/demos/probability/base-rates/meta.json` title, hook | V | |
| 2 | 9 | The question (1 in 1,000; flags 99%; wrongly flags 1%); four buttons 99/90/50/9% | `Demo.tsx` 119-122 | V | Paraphrase of "Chance you have it?", not quoted |
| 3 | 9 | "Nothing in the lesson itself works until you pick one and lock it in." (R1.1) | `src/kit/Lesson.tsx` 82 (`locked: phase === "predict"`), 103-111 ("Lock it in"); `Demo.tsx` 205-230 (`disabled={locked…}`) | V | |
| 4 | 9 | "Make a prediction to start." | `Demo.tsx` 200 | V | |
| 5 | 13 | +100 brings 100 healthy; "Test all" lights one positive | Own run of `town()`/`permutation(20240611)`: first 100 hold 0 sick, 1 false positive (index 96) | V | |
| 6 | 13 | First sick person in the third hundred | Same run: the only sick person is index 299 (the 300th) | V | |
| 7 | 13 | Full town: 11 light up, one circled; "11 tested positive. 1 of them is actually sick." | `Demo.tsx` 108-113, 168-180; own run 11/1 | V | |
| 8 | 15 | Reveal: 11 positives, 1 sick, 10 false alarms = 1% of 999; about 9%; "'99% accurate' describes the test. Your chance also depends on how rare the disease is." | `Demo.tsx` 129-134 | V | |
| 9 | 15 | Other two towns open once the full one is tested; 10 of 20 (about half); 99 of 108 (R1.2) | `Demo.tsx` 146 (`unlocked`), 230; 134-136; own run 20/10 and 108/99 | V | |
| 10 | 15 | In grey: 1978 Harvard study, most common answer 95% (R1.3) | `Demo.tsx` 138-141 (`className="muted"`, `--muted` grey); meta c6 | V | |
| 11 | 19 | Recall: 1 in 10,000, same test; almost all / about half / about 1 in 100 | meta `recall` | V | |
| 12 | 21 | Its file budgets eighty seconds | meta `durationSec: 80` | V | |
| 13 | 23 | Agent built, agent fact-checked, simulated learner reviewed, scripted test "pressed every button" (R1.4) | build commit `6b0ff445` (agent); meta `checkedBy`; learner reviews; `tests/qa/contract.spec.ts` 54-88 | V | Note: the contract presses each enabled stage control, one prediction option, "Lock it in" and the reveal. I simulated it on base-rates: +100, Fill, Test all, then 1 in 100 and 1 in 10. "Every control on the stage" is exact if wanted. |
| 14 | 23 | Every factual sentence the card showed is written down with an address (R1.5) | meta c1-c9 against `Demo.tsx` strings and `recall` | V | |

### §2 Nine Claims Behind One Minute

| # | L | Sentence | Source | Status | Note |
|---|---|---|---|---|---|
| 15 | 27 | Founded System 3 Company on 12 October 2026 (R2.1) | GitHub: repo created 2026-10-12 22:35:38Z; first commit `40999183` 22:51:34Z; `company/decisions/2026-10-12-company-structure.md` date | V | |
| 16 | 27 | On the 17th: not yet five days old; about a hundred roles, all agents except the founder's | `tools/org/roles.mjs`: 99 roles, `founder` `human: true`, the rest agents (illustrator is "an external agent") | V | 4 d 15 h 46 m to the pin |
| 17 | 29 | Built for: a guess, a town, a reason, the idea back days later (R2.2) | `company/mission.md` 7-8 | V | |
| 18 | 31 | 9% claim is third of nine, `probability.base-rates.c3` | meta claims[2] | V | |
| 19 | 31 | Rests on a derivation; source is the arithmetic; 0.0902 (R2.4) | meta c3 `support`, `source` | V | Own: 0.00099/0.01098 = 0.0902 |
| 20 | 31 | Verified by the fact-checker on 12 October 2026 | meta c3 | V | |
| 21 | 31 | The other eight cover "99% accurate", town counts, Harvard, reveal sentence, recall (R2.5) | meta c1, c2, c4-c9 | V | |
| 22 | 33 | "Why trust this? (9/9 claims checked)" | `src/components/DemoCard.tsx` 80; 9 of 9 verified | V | |
| 23 | 33 | Sheet: plain claim, checked or not, "a derivation (worked out step by step)", address in tiny type; working notes and who checked stay behind | `DemoCard.tsx` 104-128; `src/lib/trust.ts` 1-7, 42, 48-52 | V | |
| 24 | 37 | Publish command refuses any claim neither verified nor withdrawn, and a claim verified by the lesson's builder role | `tools/company.mjs` 139-147 | V | |
| 25 | 37 | "Builders never mark their own claims verified." | `CLAUDE.md` 18 | V | |
| 26 | 37 | Published lessons carry 3,891 verified claims; builder role verified none (R2.6) | Own count over 1,283 `meta.json`: 720 published, 3,922 claims, 3,891 verified, 0 open, 0 `checkedBy === owner.builder` (all 3,891 `fact-checker`) | V | Same at `42738e6d` |
| 27 | 37 | A bargaining lesson refused publication over one unchecked claim (R2.7) | `company/ops/releases.json` r6 known_issues, r7 features ("the claims gate refused patience-wins-the-split (c5 unverified)"); title "Does going first win the bargain?" | V | |
| 28 | 37 | 17 Oct: a fact-checker disputed the knot lesson's crossing rule as backwards; disputed until the builder rewrote it | `company/reviews/left-or-right/2026-10-17-fact-check.md` 13, 49; board W-1608 (owner demo-builder); commit `0ccb0e9b` "demo-builder: left-or-right v2 (… W-1608)"; re-verified in `729022c6` | V | Note: the rewrite's wording was supplied by the disputing checker (W-1608 text), and a fresh checker verified it |
| 29 | 39 | By the log, the builder and the fact-checker ran on two models from one vendor (R2.8; S11 item 1) | `events.jsonl` `tx-c048ddb23a` (general-purpose builder; brief says sign "Co-Authored-By: Claude Opus 5.5"); commit `6b0ff445` carries that line; `tx-ef796c2d40` "Dispatch fact-checker (sonnet)"; ledger `L-tx-dd4fbd8241` `"model":"sonnet"` | V | The builder's model is the log's testimony (dictated co-author line; ledger `model: null`), which the sentence's "By the company's own log" covers |
| 30 | 39 | What differs / what they share / one witness in different coats (R2.9) | Argued; the inputs differ as stated (fact-checker brief: onboarding doc, transcript first) | V | Argued, fairly grounded |
| 31 | 39 | "Even my own words to the company reach its files through an agent that wrote them down." (R2.10; S3) | Throughput record line 5 "recorded by: chief-of-staff"; Safari record line 8 "recorded by: release-manager (from the words the chief-of-staff relayed…)". These are the only two founder quotations in the prose | V | Note: the founder's account also committed directly (15 commits). Those are code and content, not his words to the company, so the sentence stands. |
| 32 | 41 | Nobody knows the builder's error rate or the checker's miss rate (R2.12) | EXP-001 "designed, not run"; no record measures either | V | |
| 33 | 43 | The gate compares role names | `company.mjs` 146 | V | |
| 34 | 43 | c7, c8 added by the fact-checker with "needs an independent check"; a day later a separate session verified both; its record calls itself independent; first checker asked for "a checker other than the fact-checker"; not on record; gate passed both (R2.13; S11 item 2) | meta c7, c8 `source`, `checkedOn 2026-10-13`; `company/reviews/base-rates/2026-10-13-fact-check.md` 3; `2026-10-12-fact-check.md` 65 | V | |

### §3 A Company in a Week

| # | L | Sentence | Source | Status | Note |
|---|---|---|---|---|---|
| 35 | 49-59 | Store passage: prototype, objective, first test, "I have not run the business experiment" (R3.1-R3.7) | The author's own earlier text (old 11) | U | The author's account; tense changes are his to confirm (source map R3.5, R3.7) |
| 36 | 53 | Recommender researchers know this as slate and whole-page optimization [1] | `appendix-references.md` 511 (Wang et al., WSDM 2016; Ie et al., SlateQ, IJCAI 2019) | V | |
| 37 | 63 | Education and the organization at once; agents do almost all the work (R3.8) | roles.mjs; commit authorship | V | |
| 38 | 67 | Founding decision created 26 roles: 25 agents and the founder | structure decision 18 | V | |
| 39 | 67 | Vision written on the first day: eight subjects, about twenty lessons for the quarter | `company/product/vision.md` 26 ("Now (Q4 2026): 8 domains, ~20 lessons"); first committed 2026-10-12 23:03:06Z (GitHub) | V | |
| 40 | 67 | By the 17th: 99 roles; 1,283 lessons in 14 subjects; 720 published (R3.9) | Own count (row 26); roles.mjs | V | |
| 41 | 69 | Each worker a fresh session, leaves a dated note at the top of a log | `CLAUDE.md`; `progress.md` 3-4 | V | |
| 42 | 69 | Header: "testimony from a worker who no longer exists: check what you rely on." | `progress.md` 3-4 | V | |
| 43 | 69 | "There are 269 of them." | `progress.md` | CWV | **268** (F1) |
| 44 | 71 | "All of these roles run on one vendor's models" (R3.10; S11 item 26) | See F3 | D | F3; author query A1 |
| 45 | 71 | …through an account with usage limits the company has already hit | `company/rituals/records/2026-10-13-coe.md` 1, 8 ("hit its session usage limit (HTTP 429…)") | V | |
| 46 | 71 | Ledger, with gaps, records 113.1 million tokens of agents' work by 16 October (R3.11; S1) | Own sum over `company/ops/ledger.jsonl`: 992 rows, 948 with tokens, 113,129,260; last row 2026-10-16T15:27:53Z; main session not added (`token-budget.md` 20); event log behind (24) | V | |
| 47 | 71 | The records hold no figure for money | Ledger has no cost field; search of `company/**/*.md` for currency, "per month", plan names finds none | V | Absence; moderate confidence |

### §4 Built From the Book

| # | L | Sentence | Source | Status | Note |
|---|---|---|---|---|---|
| 48 | 77 | Principles file takes most Zen lines, each with a practice and a file (R4.1) | `company/principles.md` (21 rows) against `appendix-zen-of-system-3.md`: own count 31 of 41 lines | V | |
| 49 | 77 | Decision template heading "Rests on"; founding decision rests on three chapters (R4.2) | `company/decisions/README.md`; structure decision 22-23 (Ch. 3, 5, 7) | V | |
| 50 | 79 | Parts designed on the first day, generated from a file | structure decision 4, 18 | V | |
| 51 | 81 | Objection: shared model makes independence "partly theatre", accepted in part | structure decision 34 | V | |
| 52 | 83 | The press is a company of agents on the same vendor's models; studied, checked, briefed and drafted (R4.3) | `press/org/roles.mjs`: 21 roles, 20 `model: "inherit"`, 1 unset | V | |

### §5 The Book Comes Back to Bite Me

| # | L | Sentence | Source | Status | Note |
|---|---|---|---|---|---|
| 53 | 89 | Three warnings came true; two are this book's; the company wrote the third a day before (R5.1) | Ch10:49; pattern file line 3 ("new 2026-10-14"), incident 2026-10-15 | V | For warnings 2 and 3. Warning 1: row 54 |
| 54 | 91 | The hub warning ("one coordinator with an org chart attached") as this book's | Ch5:18, 28, 174; all chapters searched | D | F4 |
| 55 | 91 | By 16 October a map of twenty areas, each with a manager (R5.2) | `company/ceo-office/poc-map.md` (20 numbered lanes, one POC each); `2026-10-16-poc-map-and-dispatch-requests.md` 16 | V | |
| 56 | 91 | Retro counted the previous 48 h; CoS chose about 99%; all 223 assignments named it as sender; quote (R5.3) | `company/rituals/records/2026-10-16-retro-delegation.md` 4, 12, 47 | V | |
| 57 | 93 | Same-day founder rule: dispatch only after asking the manager; eight running agents started without asking; open objection that managers cannot start agents (R5.4) | `2026-10-16-founder-org-and-dispatch-rule.md` 16, 35, 41 | V | |
| 58 | 93 | Whether it works has not been measured (R5.5) | No later measurement on disk at the pin | V | |
| 59 | 97 | 852 new lessons across 13-14 Oct; 10 across the next two days | throughput decision 13; diagnosis §2; GitHub trees | CWV | F2 |
| 60 | 97 | On 16 Oct, by its own count, new builds 8% of "the day's" 18.65M; manager rounds 35%; "Building costs about 146k per new lesson; the rest is the machine around it." (R5.8) | throughput decision 17; diagnosis 8, 16, 52 | CWV | Quote and percentages verified; "the day's" is to 14:23Z (F2b) |
| 61 | 97 | Fluent autonomy forms the institution a request needs and takes it down (R5.9) | Ch10:39 | V | |
| 62 | 97 | Diagnosis written because the founder asked; "What is going on you are working all the day but number of demos did not move" (R5.10; S3) | throughput decision 8 (verbatim, first quoted segment; "get back to me with diagnosis") | V | |
| 63 | 101 | 14 Oct: WIP pushes used the 100/day allowance; founder decided every deploy needs his approval; host then built only marker commits | `2026-10-14-coe-deploy-bypass-and-quota.md` (timeline); `2026-10-14-deploy-needs-founder-approval.md` | V | |
| 64 | 101 | 12:45 UTC next day; held release; message quoted the marker; filter matched anywhere; built and put live (R5.11) | `2026-10-15-coe.md` 6-7; GitHub (fresh): `aefb10a` committed 12:45:58Z, Vercel "Deployment has completed" 12:50:23Z; `e6805f4`, `d8f5f89` "Canceled by Ignored Build Step" | V | |
| 65 | 103 | CoS told the founder "not deployed"; founder approved; CoS searched and found it; about 20 minutes; content matched; luck (R5.12) | `2026-10-15-coe.md` 8, 12-13 | V | |
| 66 | 105 | Review asked for four mechanisms; all four still in the backlog (R5.13) | COE actions 31-34; `board.json` W-1051..W-1054 `backlog` at the pin and at `42738e6d` | V | Note: the actions table has a fifth row (the CoS checks Vercel statuses, "operating loop"). It is not in `chief-of-staff-checklist.md` or `operating-loop.md`, so it is also undone. |
| 67 | 105 | Last of five whys: CoS took the report as truth and did not check the hosting service's records (R5.14; S5) | COE 21 | V | |
| 68 | 105 | Next day: approved release refused for spent deployments; founder had pushes stop creating deployments; 17 Oct marker in a body, nothing happened (R5.15; S11 item 20) | `2026-10-16-founder-no-git-deployments.md`; `vercel.json` `git.deploymentEnabled: false` (also at `54aa64e3`); `54aa64e3` body line 4 contains the marker; GitHub: 0 statuses on `54aa64e3` | V | Old branches still deploy on push (record's caveat). The 17 Oct commit is on the default branch with the new setting. |
| 69 | 109 | Pattern "a rule without a mechanism is a wish", from four cases, all one day (R5.16) | `company/knowledge/patterns/a-rule-without-a-mechanism-is-a-wish.md` 2-3, 12-16 | V | |
| 70 | 109 | The catch came from checking the disk | COE 8; retro 51 | V | |
| 71 | 111 | Every claim on every published lesson verified or withdrawn; no builder verified its own | Row 26 | V | |
| 72 | 111 | "Gates held while the delegation did not. Nothing unverified was published." | retro 52 | V | |
| 73 | 111 | In-review lessons on the site, tagged "In review", by the founder's choice (R5.17; S11 item 3) | `2026-10-15-founder-show-review.md`; `DemoCard.tsx` 70 | V | |

### §6 Willing to Lose

| # | L | Sentence | Source | Status | Note |
|---|---|---|---|---|---|
| 74 | 117 | Revisit if cost per published lesson > 3× a single-agent baseline with no quality gain (R6.2) | structure decision 26-28 | V | |
| 75 | 117 | Founding review's first objection (26 roles heavy for 17 lessons) open, funded with EXP-001 and a cost comparison; not run (R6.3) | structure decision 33; no comparison on disk at the pin or at head | V | |
| 76 | 117 | "Experiments include a simpler baseline that is allowed to win."; eight numbered experiments, none with a result | `principles.md` 26; EXP-001..008 (001, 002 "not run"; 003 "Interim data (not a result yet)"; 004-008 "not run" / "None") | V | |
| 77 | 119 | Fourteen subjects in the first week | Row 40 | V | |
| 78 | 127 | Builder planted 10, ops reviewer 12 different; record says all caught; scripts never committed and gone; new harness reproduced 15 of 22 exactly, ran against committed tests; all 15 caught with the record's failing counts (R6.6; S6) | `company/engineering/readiness/2026-10-15-lifehacks-study-tp3-tp4-tp5.md` (both tables); ops script path `/tmp/claude-0/-home-user/3e472d64-…/ops-plant/plant.mjs` absent on this host; **own rerun** of `press/…/plant/plant.mjs` at `e84b8784` (TypeScript 5.9.2, Node 22): baseline 42/42, 15/15 applied, all caught with exact expected counts, 42/42 after | V | S6: run at `e84b8784`; the test file and the three mutated engine files have the same blob SHAs as at the approval commit `5948938` (GitHub contents API) |
| 79 | 129 | The book's test (planted false belief in notes); EXP-001 adapts it for a false claim in a lesson; one of the eight without a result; planters copies of one model (R6.7) | `appendix-note-on-evidence.md` 24-32; `EXP-001-planted-false-claim.md` 1-20 | V | |

### §7 Written Where Someone Can Argue With It

| # | L | Sentence | Source | Status | Note |
|---|---|---|---|---|---|
| 80 | 133 | Protected document the founder owns opens: "If the objective is not written down where someone can argue with it, it enters through invisible overrides." (R7.1) | `company/product/surface-value.md` 3-6; `protected-paths.txt` 5 | V | |
| 81 | 133 | Order true/works/teaches/remembered/finished; engagement reported, labelled, never used to rank or choose; fourth item real learners only (R7.2) | surface-value 12-19 | V | "teaches its point" glosses "teaches the payoff" |
| 82 | 135 | Not personalized and says so; subjects in turn; first card "Fresh picks"; mission quotes "If our ecosystem rewards clicks, clickable organisms evolve." (R7.3, R7.4) | surface-value 23; `src/components/Feed.tsx` 233-240; `mission.md` 24-25 | V | |
| 83 | 137 | Mission: a swipe feed is a delivery format, not in the attention business | `mission.md` 6 | V | |
| 84 | 137 | 15 Oct founder proposed an amendment: rule-based personalization plus one labelled ad slot; drafted, not ratified (R7.6) | `AMD-008-first-light-surface-value.md` 1-5 ("proposed (draft, not applied)") at the pin and at head | V | |
| 85 | 137 | Founder's records treat ten thousand lessons as given | throughput decision 1, 8 ("reaching 10k") | V | |
| 86 | 141 | Gates bind everyone; founder may override in writing with reason and objections; evidence by tests, purpose to the founder | `company/constitution/constitution.md` Art. 4.1, 4.3 | V | |
| 87 | 143 | One override of a launch review's ruling is on record (R7.8; S7) | Searched `company/decisions` for override/waive/exempt/overrul | V | Narrowly true. The founder also overrode head-of-product rulings that are not launch reviews: PR #2 scope (`2026-10-14-pr2-lifehacks-scope.md` 210, "the founder's override"), First Light release-1 scope (`2026-10-15-founder-first-light-ads-social-back.md`, "overrules the release-1 scope cut") and the W-556 gate (`2026-10-16-founder-behavioral-pilot-exemption.md`). A reader may take "one" as rare, which is a writer/author choice. |
| 88 | 143 | 17 Oct launch review made a Safari check a condition for releasing the knot lesson; same lesson as the disputed rule; title *Can a knot match its mirror?* | `2026-10-17-launch-review-left-or-right-r9.md` ruling 2 (b); left-or-right meta title; row 28 | V | |
| 89 | 143 | The company's machines could not run Safari's engine | `company/reviews/left-or-right/build.md` 22 (`playwright install webkit` refused by the egress proxy, no WebKit on host); `2026-10-17-qa-v3.md` 7 | V | |
| 90 | 143 | Consequence shown in one line; "Deploy" to the summary; "Ship it anyway" on Safari (R7.9; S8) | `2026-10-17-founder-deploy-r9-left-or-right-safari.md` 11-12 | V | |
| 91 | 147 | Record states the risk, what would prove it wrong, how to revert; waiver not a verification, not carried to later deploys (R7.10) | Safari record 17-30 | V | |
| 92 | 147 | Record names Safari run, real iPhone check, learner report (R7.12) | Safari record 21 | V | |
| 93 | 149 | Agents can propose amendments; one drafted the ad-slot amendment; nothing ratified without the founder; a learner can open the sheet (R7.13) | Constitution Art. 3.1-3.2; AMD-008 6 (`prepared_by: evaluation-steward`); AMD-012 ("Ratification needs the founder's signature") | V | |
| S9 | — | (moved out) the release manager wrote the words from what the CoS relayed; permission comment L145 | Safari record 8 | V | |

### §8 The Student Has Not Been Asked

| # | L | Sentence | Source | Status | Note |
|---|---|---|---|---|---|
| 94 | 155 | 0 human-learner studies, 2 simulated, 2 browser QA runs; "Simulated learners find problems; only people can show that a lesson teaches." (R8.1) | `DemoCard.tsx` 130-134; meta `evidence` arrays (0, 2, 2) | V | |
| 95 | 157 | `"humanLearners": []` in all 1,283 lessons (R8.2) | Own count: 0 non-empty | V | |
| 96 | 157 | Rules make every learner review open "Simulated learner. This review finds problems; it is not evidence that anyone learned."; the simulated adult picked 99% "and so would most adults" | `company/reviews/README.md` 31-32; `base-rates/2026-10-13-learner-adult-beginner-v2.md` 1, 11 | V | |
| 97 | 159 | Answer about 1 in 100: of 10,000, about one sick positive and about a hundred healthy positives (R8.3) | meta `recall.answer: 2`, `recall.why`; c8 | V | |
| 98 | 159 | No record of a single person answering it (R8.4) | WBRs 10-12 to 10-16 (recall "no data"/"not measured"); `wbr-2` 34 (`/api/events` only writes function logs, nothing keeps them, W-706); `humanLearners` empty everywhere | V | |
| 99 | 161 | The question the first teaching demos left open (R8.5) | Ch3:321 | V | |
| 100 | 163 | Five adults, five lessons, think-aloud, recall three days later, prediction committed first; designed on day one; not run; founder's sessions; recruiting in the backlog under his name | `EXP-002-real-learner-recall.md` 3, 9-12 (first committed 2026-10-12 23:03:06Z); board W-007 "Recruit 5 learners for EXP-002", owner founder, backlog (pin and head) | V | |
| 101 | 163 | Afternoon of the 17th: most of what was made since 15 October not yet on the public site (R8.6; S10) | Fresh fetch 2026-10-17 16:34:09Z: `/` 200, `x-vercel-cache: HIT`, `age: 184176` (cached about 2026-10-15 13:24Z); every production deploy (GitHub deployments and Deploy-to-Vercel runs) on 17 Oct ended `failure`/`error`, last run at `e84b8784` failed 15:56:16Z | V | Of the 324 lessons added since `d8f5f89` (the commit nearest the cache time), 309 are drafts the site never shows, and all 15 published or in-review ones return 404 (including `left-or-right`). If sharper is wanted: "none of the fifteen lessons it had published or put in review since 15 October was on its public site" (needs independent check). A dashboard/CLI deploy cannot be ruled out from GitHub, but the cache age and 404s show production serves the old tree. |

### Moved-out values (source map; not in the prose)

| # | Value | Source | Status | Note |
|---|---|---|---|---|
| S2 | Event log backfilled; today's window holds 372 dispatch events, all `chief-of-staff`, 5 with `batch=` | Own count over `events.jsonl` for `type: dispatch`, 2026-10-14T09:40Z to 2026-10-16T09:50Z (the retro's grep start): 372, all CoS, 5 `batch=`; the retro saw 223 and "last event 10-15 10:11Z" | V | From 09:50Z it is 365 |
| S4 | Replay matches only `aefb10a` | Own rerun | CWV | F5 |
| S6 | Harness ran at `e84b8784`, not the approved state | Row 78 | V | Blob-identical files, so the distinction does not change the result |

## What I did not check

- The 1978 study itself (Casscells et al.). The chapter reports what the card says, and the card's claim c6 is the company's verified claim. I checked the card, not the paper.
- The author's store passage (row 35). It is his account.
- Punctuation and style (the copy editor's) and Chapter 13 (protected).

## Reproduce

- Counts: `git -C /home/user/system-3-company archive e84b8784 | tar -x -C <dir>`, then iterate `src/demos/*/*/meta.json` (status, claims, checkedBy, owner.builder, evidence.humanLearners).
- Town: copy `permutation()` and `town()` from `Demo.tsx` and print the first sick and false-positive indices.
- Replay: `TMPDIR=<scratch> bash press/books/system-3/experiments/2026-10-company-case-study/deploy-marker/replay.sh`.
- Harness: the README in `press/…/plant/`, with the export at `e84b8784`.
- Day-boundary lesson counts: `gh api repos/hanialshater/system-3-company/commits?sha=ccr-4c6c7654-ew9ko1&until=<t>&per_page=1`, then `git/trees/<sha>?recursive=1`, count `src/demos/*/*/meta.json`.
- Site: `curl -sS -D - https://system-3-company.vercel.app/` (age header) and `/d/<slug>` for the 15 new non-draft slugs.

## Next

- **Writer (writer-system-3):** decide F1-F4 (and F5 in the source map). The head of book routes this.
- **Author:** query A1 (what made the `codex/` PRs), which decides F3's final wording and may touch L39.
- **Independent check:** my wordings F1-F5, F2b and the optional rewordings in rows 13 and 101 need a checker other than me (a third fact-checker instance or the development editor).

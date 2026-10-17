# Fact-check: Chapter 11 draft ("Guess First")

checker: fact-checker-system-3 (Beckett) · date: 2026-10-17, checks run about 15:30Z to 15:55Z
text checked: `chapters/11-the-store-that-builds-itself.md` at book commit `c98653a` (2026-10-17 15:42Z, branch `ccr-fd4ebbbc-p06k8x`), sha1 `93811e71…`. Read cold, findings drafted, then the writer's source map (`press/books/system-3/proposals/2026-10-17-chapter-11-source-map.md`) used as a pointer only, and the consequential-edits proposal read last, for M8 only.
primary sources: `/home/user/system-3-company` at `e84b8784` (still the default-branch head on GitHub at 15:46Z), read only: no edits, no commits, no `git fetch`, no state-changing scripts (`npm run company -- status` was not run, because it regenerates files). GitHub REST GETs (`gh api`). Public site `https://system-3-company.vercel.app`, `curl` GETs at 15:53Z. The old chapter text at book commit `71ac730`. The book's chapters and appendices at `c98653a`.
recomputation: every W item recomputed from the lesson's own code. `town()` and `permutation()` from `src/demos/probability/base-rates/Demo.tsx` copied verbatim into `/tmp/claude-0/-home-user/f0be7ef4-e990-5584-991b-e9d7e05d7372/scratchpad/ch11/town.mjs` and run for 100…1,000 people at all three rates. Counts over `src/demos/*/*/meta.json`, `company/ops/ledger.jsonl` and `company/ops/events.jsonl` recomputed with python one-offs (results below).
status: **review record. Not manuscript text. Every fix below is my proposal and is "needs independent check": a second fact-checker instance or the development editor checks it before the writer uses it.**

## Summary

**Rows: 143.** verified 106 · correct-with-value 17 · disputed 8 · unverifiable 2 · needs-second-checker 10.

### Required fixes (disputed: the sentence is false or misleading as written)

1. **L35, "run on the same model".** The 9% claim (c3) was written by the 12 October build dispatch (`general-purpose`, ledger `model: null`, so the session model; the 10-13 COE calls the builders "Opus builders") and checked by a dispatch logged as **"Dispatch fact-checker (sonnet)"** (`events.jsonl` `tx-ef796c2d40`; ledger `L-tx-dd4fbd8241`, `"model":"sonnet"`). Today's `roles.mjs` says `inherit` for both, but the dispatch overrode it. The company even runs EXP-003, "Sonnet builders vs Opus builders". Suggested: "run on models from the same developer: by the company's own log, the builder on Opus and the checker on Sonnet." The "one witness wearing different coats" argument should then say "one family" (shared training), not "one copy of a model". The same correction applies to L73 ("running on the same model", row 59).
2. **L37, "cannot say whether the second look came from a fresh instance… The independence the note asked for is not on record."** `meta.json` cannot say, but the records do. The 13 October check was a separate dispatch ("Fact-check probability + life backlog ·5dad", 05:23Z, its own ledger row), and its record opens "Checker: fact-checker (independent of the 2026-10-12 checker who added c7 and c8)". What is missing is what the first checker asked for: "Next move: a checker other than the fact-checker verifies c7, c8" (`2026-10-12-fact-check.md` line 65). Suggested: "The records show a fresh fact-checker instance a day later, which calls itself independent. The first checker had asked for 'a checker other than the fact-checker'. That check is not on record, and the gate cannot tell the difference."
3. **L99, "It shows that nothing unchecked got through."** In-review lessons, with unverified claims, are served on the public site tagged "In review", by the founder's decision: "a learner can meet an unverified claim… The founder accepts this" (`company/decisions/2026-10-15-founder-show-review.md`; Surface Value line 23; `releases.json` 511 and 595 show `patience-wins-the-split` served "In review" in production). Suggested: "It shows that nothing unchecked was marked published. Lessons still in review are on the site too, tagged 'In review', by the founder's choice." Row 29 (the bargaining lesson "held back") should be consistent with this.
4. **L27, "The other eight cover…".** The list names seven claims (c1, c2, c4, c5, c6, c7, c8). It leaves out **c9**, the full-town counts (11/1, 20/10, 108/99). Also, c7's sentence is in the second of the reveal's three paragraphs; the reveal **ends** on the Harvard paragraph. Suggested: "…the rounding on the stage, the counts on the full town, the Harvard study, the reveal's general sentence, and the question that comes back days later." Same fix at L37, "the general sentence at the end of the reveal" → "the reveal's general sentence".
5. **L15, "Two more towns open up."** It is placed after the reveal, but the other two rates unlock **during explore**, as soon as the full town is tested at 1 in 1,000 (`unlocked`, Demo.tsx 146 and 230). In the reveal every stage control is disabled (`inReveal`, lines 205-230), and the reveal only quotes the counts. Suggested: "The reveal then gives the other two towns, which unlocked once you had tested the full one: at 1 in 100, ten of twenty positives are sick, about half; at 1 in 10 it is 99 of 108."
6. **L67, "takes each line of the Zen of System 3".** The principles file says so of itself, but by my count it covers 31 of the 41 lines in today's `appendix-zen-of-system-3.md`. Missing: "Capacity over power", "The farmer grows nothing. The plant does.", "Better under which conditions? Better for whom?", "The student will find the gradebook.", "The overseer is not ground truth.", "Leave the human room to change their mind.", "What became easy may still be worth doing.", "Construct knowingly. Build anyway.", "The tongue cannot reach the ear.", "Build a system that can check." Suggested: "takes the lines of the Zen of System 3 (most of them)…" or "says it takes each line…".
7. **L81, "The company was built to avoid exactly that, with twenty lanes, each with a manager."** The 20-lane POC map dates from 16 October (`2026-10-16-poc-map-and-dispatch-requests.md` line 16, replacing an interim map in the same day's founder rule). That is after most of the 48 hours the retro measured. The founding design was 26 narrow roles. Suggested: "The company was built to avoid exactly that: narrow roles under managers, and by 16 October a map of twenty lanes, each with a manager."
8. **L121, "the form this book spends pages worrying about".** The book's feed passages are a paragraph in Chapter 6 (Facebook's feed, line 333) and two sentences in Chapter 12 (lines 55 and 219). That is not "pages". Suggested: "the form this book keeps warning about" or "the form Chapters 6 and 12 warn about".

### Required fixes (correct-with-value: right in substance, a value or word must change)

9. **L9:** the stage unlocks after you pick an option **and** press "Lock it in" (Lesson.tsx 102-110). The card's "Why trust this?" and "Open" work before then. Suggested: "Nothing on the stage works until you pick one and lock it in." ("Small type" is 0.92rem bold: optional to keep.)
10. **L23:** "a fourth pressed every button in a browser". The pressing is done by the Playwright contract (`tests/qa/contract.spec.ts`), and the QA record's "recorded by: qa-tester" is a constant label (record C12). Suggested: "…and a scripted browser test pressed every button."
11. **L23:** "Every factual sentence you just read" also covers the chapter's own narration, which no claim records. Suggested: "Every factual sentence the card showed you…".
12. **L15:** the card says "a 1978 Harvard study". "Harvard Medical School" is in claim c6, which the trust sheet shows. Optional: "a 1978 Harvard study".
13. **L33:** the bargaining lesson was refused **publication**. It stayed on the site tagged "In review" (see fix 3). Suggested: "…was refused publication because a single claim was still unchecked."
14. **L57:** "the main branch". The default branch is `ccr-4c6c7654-ew9ko1`. Suggested: "the default branch".
15. **L57:** "26 roles, 25 agents and the founder" reads as 26 + 25 + 1. Suggested: "26 roles: 25 agents and the founder."
16. **L67:** 17 of the 86 decision records carry a "## Rests on" heading. The template has it (`company/decisions/README.md` line 15). Suggested: "Its decision template has a heading, 'Rests on'…".
17. **L73:** "running on the same model" → "running on the same developer's models" (see fix 1).
18. **L81:** the "testimony-grade" label is on the retro's lane-by-lane matrix (line 21), the source of "about 99%". The 223 is in its "measured here" numbers table (line 7). Suggested: "it labels its lane-by-lane table testimony-grade."
19. **L91:** "The hosting service's own commit statuses show all of this." The statuses show that `aefb10a` was built and the other two commits were cancelled. They do not show what the founder was told. Suggested: "show the build".
20. **L93:** "nothing listens for the word any more". `vercel.json` still carries the marker `ignoreCommand`, and F-48 says branches cut before the change "still deploy on push until they merge the default branch". No record shows the Git connection removed. Suggested: "because pushes no longer create deployments."
21. **L105:** the objection was "funded: EXP-001 plus a cost comparison in the first OP". Optional: "…funded with EXP-001 and a cost comparison."
22. **L113:** "The company adopted that test". EXP-001 "adapts the book's own unrun test": it plants a false claim in a lesson's stage text and build note, and measures whether reviewers verify it. That is not a false diagnosis in a progress file reaching the next worker's plan. Suggested: "The company adapted that test, for a false claim planted in a lesson, as its first experiment."
23. **L119:** the old chapter has "If **your** ecosystem rewards clicks…"; the mission has "our". The quotation is exact to the mission, so the fix is optional: "quotes one of my store sentences back at me, as its own:".
24. **L133:** "Only the founder ratifies." Article 3.2 gives the decision to the Constitutional Review Board (founder, head of product, evaluation steward, plus an affected role), and AMD-012 says "Ratification needs the founder's signature, and no single role decides alone". Suggested: "Nothing is ratified without the founder."
25. **L149:** "a checked claim behind every factual sentence of the ones marked published". The gate checks that **recorded** claims are verified, not that every sentence has a claim. Coverage rests on fact-checkers' reading (base-rates c7 and c8 were found that way). Suggested: "a checked claim behind every factual sentence the company recorded for the ones marked published" or "…by the company's rule".

### Unverifiable (the writer must source or reword)

26. **L61, "rented by the token".** No company record says how the models are paid for. The only records of the arrangement describe a **usage-limited account**: "The account hit its session usage limit (HTTP 429, resets 03:30 UTC)" (`2026-10-13-coe.md`), and EXP-003 ("under the usage limit"). Suggested: "rented, not owned" or "on an account with usage limits". The author can supply the real arrangement (this sits with Ask 11).
27. **L79-L89, "The book's own warnings came true… Three are worth the space."** Warning 1 maps loosely to Chapter 5: "The organization was the bug" (5:28, the compiler story) and "reality will be intimidated by the org chart" (5:174). The "one coordinator" form is the draft's gloss. For warning 2 ("the machine around the lesson") and warning 3 ("a rule that turned out to be a wish") I found no passage in the book. "A rule without a mechanism is a wish" is the company's pattern name (2026-10-14). The nearest book text is old 11:205, "The system should have to earn its complexity", which this draft cuts. Suggested: name the chapter for each warning, or "Three of the failures the book warns about in general terms, one of them in the company's own words".

### Needs a second checker (the sentence rests on a value or wording I supplied in `2026-10-17-fact-check-company-case-study.md`; I may not verify it)

| Row | Line | Sentence | My earlier value it rests on | What I see today (not a verification) |
|---|---|---|---|---|
| 52 | 61 | "from a ledger with known gaps, so the real figure is higher" | correction 4: 948 measured rows of 992, 44 `tokens: null`; main session excluded | Recomputed again: 992 rows, 948 with tokens, 113,129,260. |
| 67 | 81 | "The log was backfilled afterwards, so they cannot be recomputed from today's files, though every dispatch in today's version of that window still names the same actor." | correction 7: 372 events in the window, all `chief-of-staff`, 5 with `batch=` | Rerun: 372, `{chief-of-staff}`, 5. |
| 74 | 85 | "his complaint is on file, as an agent transcribed it" | dispute row 94 (the founder's words reach the disk through agents) and its wording | The quote is verbatim at `2026-10-16-founder-throughput-for-10k.md` line 8; line 5 says "recorded by: chief-of-staff". |
| 82 | 91 | "…reaches the same verdict, so this incident is run as well as recorded." | my ruling that "run" holds for the C1 trigger logic | Also a wording issue: only the filter is run; what the founder was told is recorded. Suggested: "so the filter's part is run as well as recorded". |
| 85 | 93 | "Its fifth why lands on a person: the chief of staff took the agent's report as truth and did not check." | dispute row 53 and its wording | COE line 21: "The chief of staff took the agent's report as truth and did not check Vercel commit statuses after the release manager's commits." |
| 106 | 113 | "ran it against the company's committed tests at its latest commit" | correction 6: "a new run at `e84b8784`", not at the approved state | `e84b8784` was still the default-branch head at 15:46Z. |
| 122 | 127 | "One override of a review's ruling is on record." | row 74 note (the waived item is a launch-review ruling, not a coded gate) | New: a second founder exemption exists, `2026-10-16-founder-behavioral-pilot-exemption.md` ("exempt the behavioral pilot"), from the W-556 queue gate that head-of-product ruled only the founder may exempt. That is a gate ruling, not a review's, so the sentence may stand only with the narrower word. Suggested: "One override of a launch review's ruling is on record." |
| 126 | 127 | "His recorded word was 'Deploy', and he chose the option labelled 'Ship it anyway'." | correction 8 | Also sequence: "Deploy" answered the summary of the whole deploy (record line 11), before the separate Safari question (line 12). Suggested: "He answered the release summary with 'Deploy', and on the Safari question he chose the option labelled 'Ship it anyway'." |
| 128 | 127 | "Those words reached the file second-hand: the release manager wrote them down from what the chief of staff relayed." | correction 8 | Record line 8: "recorded by: release-manager (from the words the chief-of-staff relayed from the conversation of 2026-10-17)". |
| 139 | 145 | "As of the afternoon of 17 October, most of what the company made after 15 October had not reached anyone outside it." | correction 9 ("cached around 13:24Z on 10-15") and row 70 | Fresh GETs at 15:53:26Z: `/` 200, `age: 181733`, so cached at about 2026-10-15 13:24:33Z (the same instant as at 15:16Z). `/d/heat-the-ammonia-maker` and `/d/base-rates` 200. `/d/left-or-right`, `/d/snap-the-magnet`, `/d/where-the-axis-starts`, `/d/raters-reward-agreement` 404 (`x-matched-path: /404`, the same as a nonsense path). Deploy run `39042065255` (14:44:59Z) still `in_progress` at 15:53Z. Still unverifiable: a deploy by a path with no GitHub status (Vercel CLI or dashboard; no Vercel access). |

Every fix in items 1-27 is also mine, so each needs an independent check before use.

## Claim table

Abbreviations: CR = `/home/user/system-3-company` at `e84b8784`; API = GitHub REST API; V = verified, CwV = correct-with-value, D = disputed, U = unverifiable, N = needs-second-checker. Line numbers are the chapter's.

### §1 Ninety-Nine Percent Accurate

| # | Line | Sentence (quoted) | Source checked | Status | Note and suggested fix |
|---|---|---|---|---|---|
| 1 | 7 | "Its title is a question, *You tested positive. Now what?*, and under it the card says…: 'The test is 99% accurate. So you're 99% likely to be sick. Right?'" | CR `src/demos/probability/base-rates/meta.json` `title`, `hook`; `src/components/DemoCard.tsx` 72-73 | V | Verbatim. Production `/api/meta/base-rates` has the same title. |
| 2 | 9 | "A disease affects 1 in 1,000 people. A test flags 99% of sick people and wrongly flags 1% of healthy people… four buttons: about 99%, about 90%, about 50%, about 9%." | `Demo.tsx` 119-121 | V | Faithful paraphrase of the question; the labels are "About 99%" etc. |
| 3 | 9 | "Nothing else on the card works until you press one. The controls stay disabled and a line of small type says 'Make a prediction to start.'" | `Demo.tsx` 200, 205-230; `src/kit/Lesson.tsx` 86-110; `DemoCard.tsx` 78-86; `styles.module.css` 18 | CwV | Unlock needs "Lock it in" too. Footer links work before. Message is 0.92rem bold. Fix 9. |
| 4 | 13 | "It is a grid of a thousand empty squares…" | `Demo.tsx` 17, 99 (`s.empty` for unfilled) | V | |
| 5 | 13 | "You press +100 and a hundred people move in, all of them healthy." | W recomputed (`town.mjs`): at 100 filled, sick 0 | V | Message reads "100 people. 0 are sick. Now test them." |
| 6 | 13 | "You press 'Test all' anyway, and one of them lights up positive." | W: at 100, falsePos 1, truePos 0 | V | |
| 7 | 13 | "The first sick one arrives somewhere in the third hundred." | W: sick 0 at 200, 1 at 300; the only sick square is index 299 | V | It is the last square of the third hundred. |
| 8 | 13 | "You fill the town to 1,000 and test everyone. Eleven squares light up, and one of them has a circle around it… '11 tested positive. 1 of them is actually sick.'" | W: 1 TP + 10 FP; `Demo.tsx` 112 (template), 168-180 (ring when `truePos <= 10`) | V | |
| 9 | 15 | "Eleven positives, one sick, ten false alarms, and the ten are 1% of the 999 healthy people. A positive means about 9%." | `Demo.tsx` 128-132 (reveal p1, from `KEY = counts(1000)`) | V | |
| 10 | 15 | "'‘99% accurate’ describes the test. Your chance also depends on how rare the disease is.'" | `Demo.tsx` 134 | V | Verbatim. |
| 11 | 15 | "Two more towns open up. At 1 in 100, ten of twenty positives are sick, about half. At 1 in 10 it is 99 of 108." | W: `MID` 10/20, `HIGH` 99/108; `Demo.tsx` 146, 205-230 (`unlocked`, `inReveal`) | D | Numbers right; sequence wrong. Fix 5. |
| 12 | 15 | "At the bottom, in grey, the card adds that in a 1978 study at Harvard Medical School the most common answer to a similar question was 95%, when the right answer, if the test catches every case, was about 2%." | `Demo.tsx` 138-141 (`muted`); `globals.css` 6, 28 (`--muted` #9aa3b5 / #5d6578); meta c6; `company/reviews/base-rates/2026-10-13-fact-check.md` c6 | CwV | "In grey" holds. The card says "1978 Harvard study"; HMS is c6's wording. Fix 12 (optional). |
| 13 | 17 | "If you picked 99%, you are in good company, and some of it has medical degrees." | c6 and the 10-13 fact-check (students, house officers and staff at HMS teaching hospitals) | V | Rhetorical. The Harvard group's common answer was 95% to a 5% version: the same error, not the same number. |
| 14 | 19 | "Days later the idea is supposed to come back as a single question. A condition affects 1 in 10,000… Almost all, about half, or about 1 in 100?" | meta `recall`; `company/mission.md` 8; `src/kit/progress.ts` 50-57; WBR 10-14 line 34 (`REVISIT_SCHEDULE_DAYS = [1, 3, 7, 21]`); `Feed.tsx` revisits | V | "Supposed to" is right: no recall data exists (WBRs 10-13 to 10-16: "no data"). The first revisit is due after 1 day. |
| 15 | 21 | "The company that made this card calls it a sixty-second lesson. Its own file budgets eighty seconds…" | CR `company/README.md` 3; mission 5; meta `durationSec: 80`; `DemoCard.tsx` 69 | V | The card's own tag displays "80s". |
| 16 | 23 | "Nobody who made that minute is a person." | `git log --all -- src/demos/probability/base-rates` (authors `Claude`, `qa-tester`, `learner-evaluator`); `events.jsonl` `tx-c048ddb23a` | V | Scope: the lesson's files and records. |
| 17 | 23 | "An agent built it, another agent checked its facts, a third pretended to be a learner and reviewed it, and a fourth pressed every button in a browser." | builder dispatch `tx-c048ddb23a` ("You are a Demo Builder"), revision `tx-5b7271a1e8`; fact-check dispatches ·aea2, ·5dad; reviews in `company/reviews/base-rates/`; `tests/qa/contract.spec.ts` 6-9, 70-88; QA records line 3 | CwV | Fix 10. |
| 18 | 23 | "Every factual sentence you just read is written down somewhere with an address." | meta c1-c9 against the learner strings in `Demo.tsx` and the recall card; 10-13 fact-check "No unrecorded claims found" | CwV | True of the card's strings, not of the chapter's narration. Fix 11. |

### §2 Nine Claims Behind One Minute

| # | Line | Sentence (quoted) | Source checked | Status | Note and suggested fix |
|---|---|---|---|---|---|
| 19 | 27 | "In the lesson's file it is the third of nine claims, and its address is `probability.base-rates.c3`. It rests on a derivation… 0.99 × 0.001 divided by the same thing plus 0.01 × 0.999, which comes to 0.0902. Its status is verified, checked by the fact-checker on 12 October 2026." | meta c3 | V | Recomputed: 0.00099 / 0.01098 = 0.0902. |
| 20 | 27 | "The other eight cover what '99% accurate' means here, the expected counts, the half and the ninety-two, the rounding on the stage, the Harvard study, the sentence the reveal ends on, and the question that comes back days later." | meta c1-c9; `Demo.tsx` 126-143 | D | Seven named; c9 missing; c7 is not where the reveal ends. Fix 4. |
| 21 | 29 | "Under the card is a link: 'Why trust this? (9/9 claims checked)'." | `DemoCard.tsx` 79-80; `src/lib/trust.ts` 56-64; production `/api/meta/base-rates` at 15:53Z: 9 claims, all verified | V | The link is in the card's footer. |
| 22 | 29 | "It opens a sheet that lists each claim in plain words, says whether it has been checked and what it rests on ('a derivation (worked out step by step)'), and prints its address in tiny type." | `DemoCard.tsx` 105-127; `trust.ts` 41-52 | V | |
| 23 | 29 | "The working notes stay behind. The sheet tells you a claim was checked, and leaves out who checked it and how." | `trust.ts` 4-7, 15-21, 101-115; production payload (no `source`, no `checkedBy`) | V | The sheet does show the support type and any http links in the source. |
| 24 | 31 | "And now the camel comes back: where did the claim come from, how strong is the evidence, what kind of knowledge is this, and how much trust should the system place in it before acting?" | old chapter (`71ac730`) 11:113; Ch 4 lines 5, 291 | V | Author's sentence, verbatim. The camel is introduced in Chapter 4. |
| 25 | 31 | "Here those questions are fields in a file, and a learner can open most of them with one tap." | meta fields; `DemoCard.tsx` | V | Argued; fair. |
| 26 | 33 | "The command that publishes a lesson refuses if any claim is neither verified nor withdrawn, and it refuses a claim marked verified by the role that built the lesson." | `tools/company.mjs` 139-146, 521-534 | V | |
| 27 | 33 | "'Builders never mark their own claims verified.'" | CR `CLAUDE.md` 18 | V | Verbatim. |
| 28 | 33 | "As of 17 October 2026, the lessons marked published in the repository carry 3,891 verified claims, and the builder role verified none of them." | python over all `meta.json` | V | 720 published; 3,891 verified, 31 withdrawn, 0 open; 0 claims with `checkedBy == owner.builder`; all 5,299 verified claims say `fact-checker`. |
| 29 | 33 | "In one release a lesson about bargaining was held back because a single claim was still unchecked." | `company/ops/releases.json` 509, 511, 530; `patience-wins-the-split` meta title "Does going first win the bargain?" | CwV | Fix 13. |
| 30 | 33 | "On 17 October a fact-checker disputed a sentence in a lesson about knots: the builder had stated the rule for left- and right-handed crossings backwards. The claim stayed disputed until the builder rewrote it." | `src/demos/math/left-or-right/meta.json` c5 `note` (History); `company/reviews/left-or-right/2026-10-17-fact-check.md` 13, 49 | V | The reversed sentence was the claim's rule sentence, which is shown in the trust sheet but not on the stage. It was rewritten "from the fact-check's suggestion". |
| 31 | 35 | "The builder that wrote the 9% and the fact-checker that checked it run on the same model." | `events.jsonl` `tx-c048ddb23a`, `tx-ef796c2d40`; ledger `L-tx-f11a547ca8` (`model: null`), `L-tx-dd4fbd8241` (`"sonnet"`); `2026-10-13-coe.md` 6 ("nine Opus builders"); `EXP-003-sonnet-builders.md` | D | Fix 1. Caveat: the event log was backfilled, so the model label is the log's testimony. It is still the only record of the run, and it contradicts the sentence. |
| 32 | 35 | "The witnesses that are not the model are few: the founder, code that runs, and the records kept by other companies' systems." | record header; API statuses | V | Argued. The chapter flags the transcribed founder quotes where it uses them. |
| 33 | 37 | "The gate itself shows how thin the separation is. It compares role names." | `company.mjs` 146 | V | |
| 34 | 37 | "Two of the nine claims… were added by the fact-checker, each with a note that it 'needs an independent check', and then marked verified by the fact-checker a day later. The gate passed them…" | meta c7, c8 (`source`, `checkedOn: 2026-10-13`); status `published`; `2026-10-12-fact-check.md` 8 | V | |
| 35 | 37 | "The file has the same role name on both sides and cannot say whether the second look came from a fresh instance or from the same one on a different day… The independence the note asked for is not on record." | `2026-10-13-fact-check.md` 3; `2026-10-12-fact-check.md` 65; events ·aea2 (10-12 23:22Z) and ·5dad (10-13 05:23Z); ledger rows 24, 77 | D | Fix 2. Both instances ran as `sonnet`. |

### §3 A Company in a Week

| # | Line | Sentence (quoted) | Source checked | Status | Note and suggested fix |
|---|---|---|---|---|---|
| 36 | 43 | "After years working on ranking and recommendations, I built a prototype store because the idea would not stay on the page." | old 11:5 | V | Author's text, verbatim. |
| 37 | 47 | "Recommender researchers know part of this territory as slate and whole-page optimization.[1]" | old 11:67; `appendix-references.md` 511 (`ref-11-slate`: Wang et al., WSDM 2016, whole-page presentation; Ie et al., SlateQ, IJCAI 2019) | V | The reference is used correctly: one source for each term. |
| 38 | 47 | "My complaint was simpler. The page is smart inside the modules and surprisingly dumb between them." | old 11:15 | V | The second sentence is verbatim. "My complaint was simpler" is a new connective in the author's voice: the author should confirm it. |
| 39 | 49 | "I have not run the business experiment. I have definitely not solved shopping before lunch. But once you can imagine a store learning that way…" | old 11:9, 11:239 | V | Trimmed, with "But" added. |
| 40 | 53 | "…an organization that builds lessons and is run almost entirely by agents." | `tools/org/roles.mjs` (99 roles, `founder` the only non-agent) | V | |
| 41 | 57 | "Its first commit landed at 22:51 UTC on 12 October 2026." | API: last page of the default branch, `40999183`, 22:51:34Z, 0 parents | V | |
| 42 | 57 | "By 14:21 on 17 October, four days and fifteen and a half hours later, the main branch held 2,718 commits." | API `commits?sha=ccr-4c6c7654-ew9ko1&until=2026-10-17T14:21:02Z` Link `rel="last"` page 2718; span 4 d 15:29:28 | CwV | Fix 14. |
| 43 | 57 | "The founding decision created 26 roles, 25 agents and the founder." | `company/decisions/2026-10-12-company-structure.md` 18 | CwV | Fix 15. |
| 44 | 57 | "By the night of the 13th there were 72." | `company/ops/progress.md` 2278-2282 ("That is 72 roles in total") | V | A handoff count (testimony). |
| 45 | 57 | "As of 17 October the org data lists 99." | `roles.mjs` → 99 | V | |
| 46 | 57 | "The vision written on the first day planned eight subjects and about twenty lessons for the quarter." | `company/product/vision.md` at `7629eeb9` (10-12 23:03Z) line 26 | V | "Now (Q4 2026): 8 domains, ~20 lessons". |
| 47 | 57 | "As of the same date the repository holds 1,283 lessons in 14 subjects, from probability to history, and 720 of them are marked published." | python over meta; `ls src/demos` | V | 720 / 234 review / 329 draft; 14 domain folders. |
| 48 | 59 | "Each worker is a fresh session of a model. It arrives knowing nothing except what is on disk, does one piece of work and leaves a dated note at the top of a log." | CR `CLAUDE.md` 5-6, "Before you finish" | V | The designed rule. Role memory files are also on disk. |
| 49 | 59 | "The log's header describes each note as 'testimony from a worker who no longer exists: check what you rely on.' There are 269 of them." | `progress.md` 3-4; `grep -c '^## '` = 269 | V | |
| 50 | 61 | "All of these roles run on one developer's models, rented by the token." | `roles.mjs` (`sonnet` / `inherit`); commit trailers; `2026-10-13-coe.md` 6-9; EXP-003 | U | "One developer's models" holds. "Rented by the token" has no source. Item 26. |
| 51 | 61 | "The company has logged 113.1 million tokens of its agents' work up to 16 October…" | `ledger.jsonl`: 113,129,260 tokens; last row 10-16 15:27:53Z | V | The record's value, recomputed. |
| 52 | 61 | "…from a ledger with known gaps, so the real figure is higher." | ledger nulls; my correction 4 | N | See the second-checker table. |
| 53 | 61 | "The records hold no figure for money." | grep of `company/` for billing, subscription and money figures | V | A negative, searched. Lesson content about money excluded. |

### §4 Built From the Book

| # | Line | Sentence (quoted) | Source checked | Status | Note and suggested fix |
|---|---|---|---|---|---|
| 54 | 67 | "Its principles file takes each line of the Zen of System 3, the short list of maxims at the back of the book, and gives it a practice and the file where the practice lives." | `company/principles.md` 1-30; `chapters/appendix-zen-of-system-3.md` | D | Fix 6. "At the back of the book" holds (appendix). |
| 55 | 67 | "Its decisions carry a heading, 'Rests on'…" | `company/decisions/README.md` 15; 17 of 86 records have `## Rests on` | CwV | Fix 16. |
| 56 | 67 | "…and the founding one rests on three chapters of this book." | `2026-10-12-company-structure.md` 22-23 (Ch. 3, Ch. 5, Ch. 7); Ch 5 ("So useful independence has to be built"); Ch 7 (constitution); Note on Evidence row 3 | V | The chapters do carry those ideas. |
| 57 | 69 | "The parts were designed on the first day, generated from a file." | structure decision 18; `7629eeb9` | V | |
| 58 | 71 | "Its founding decision records the objection that several roles share one model, so their independence is 'partly theatre', and marks it accepted in part." | structure decision 34 | V | Verbatim. |
| 59 | 73 | "The company has a sibling, a press founded to make my books, and the press is also a company of agents running on the same model." | `company/decisions/2026-10-15-founder-press-sibling-company.md`; `press/org/roles.mjs` (`inherit`); company `roles.mjs` (48 `sonnet`, 49 `inherit`) | CwV | Fix 17. |
| 60 | 73 | "It studied this company's records, checked them, and briefed and drafted the pages you are reading." | the press's case-study record, my FC, the brief, the source map, commit `c98653a` | V | |
| 61 | 73 | "In that whole chain, the author is the one reader who is not a copy of it…" | — | V | Argued. |

### §5 The Book Comes Back to Bite Me

| # | Line | Sentence (quoted) | Source checked | Status | Note and suggested fix |
|---|---|---|---|---|---|
| 62 | 79-81 | "The book's own warnings came true against the design built to heed them. Three are worth the space." / "A society of agents can turn into one coordinator with an org chart attached, and the organization becomes the bug." | Ch 5:28, 5:174; whole-book grep for coordinator, hub, wish, machinery, overhead; old 11:205 | U | Item 27. |
| 63 | 81 | "The company was built to avoid exactly that, with twenty lanes, each with a manager." | `2026-10-16-poc-map-and-dispatch-requests.md` 1-16; `2026-10-16-founder-org-and-dispatch-rule.md` 19-32 | D | Fix 7. |
| 64 | 81 | "On 16 October its own retrospective measured the previous 48 hours. The chief of staff… had chosen about 99% of the specialists' work, and every one of the 223 dispatches in the log for that window named it as the actor." | `company/rituals/records/2026-10-16-retro-delegation.md` 4, 12, 13, 47 | V | The log stopped at 10-15 08:55Z, so the 223 cover the first part of the window. "In the log for that window" is accurate. |
| 65 | 81 | "'The org chart says 20 lanes; in practice there was one dispatcher who asked managers questions.'" | retro 47 | V | Verbatim. |
| 66 | 81 | "Those are its counts at the time, and it labels its own table testimony-grade." | retro 7, 21 | CwV | Fix 18. |
| 67 | 81 | "The log was backfilled afterwards, so they cannot be recomputed from today's files, though every dispatch in today's version of that window still names the same actor." | my correction 7; rerun | N | See the second-checker table. |
| 68 | 83 | "The same day the founder made a rule that the coordinator dispatches only after asking the lane's manager what to run." | founder rule 2 (line 16) | V | The rule (~09:28Z, retro line 16) came before the retro was written. |
| 69 | 83 | "The rule's own record admits that the eight agents running when it was written had been dispatched without asking, and it keeps open an objection that managers cannot start agents themselves…" | founder rule 35, 41 | V | |
| 70 | 83 | "The fix is written down. Nobody has measured whether it works." | `2026-10-16-retro-rounds-3-5.md` 16; event log ends 10-16 19:04Z | V | The later retro reports managers answering batch requests. That is the coordinator's account of compliance, not a measure of effect. |
| 71 | 85 | "Across 13 and 14 October the company made 852 new lessons. Across the next two days it made 10. On 16 October… new builds took 8% of the day's 18.65 million tokens and manager rounds took 35%…" | `company/decisions/2026-10-16-founder-throughput-for-10k.md` 11-17 | V | The prose labels these as the company's numbers, not recomputed: the right category. |
| 72 | 85 | "'Building costs about 146k per new lesson; the rest is the machine around it.'" | throughput record 17 | V | Verbatim. |
| 73 | 85 | "The diagnosis was written because the founder asked for it…" | throughput record 8 ("i want you to get back to me with diagnosis and solution") | V | |
| 74 | 85 | "…and his complaint is on file, as an agent transcribed it: 'What is going on you are working all the day but number of demos did not move'" | throughput record 5, 8 | N | The quote is verbatim. The framing rests on my row 94. |
| 75 | 89 | "On 14 October, after agents' work-in-progress pushes had used up the hosting service's free allowance of 100 deployments a day, the founder decided that every deploy needs his approval, every time." | `company/decisions/2026-10-14-deploy-needs-founder-approval.md` | V | |
| 76 | 89 | "At that point the hosting service built only commits whose message carried a marker word." | same, Decision; `vercel.json` `ignoreCommand` | V | |
| 77 | 89 | "At 12:45 UTC the next day, the release manager prepared a release it had been told not to deploy and wrote a conscientious commit message saying so." | API `aefb10a`: 12:45:58Z, subject "Release r7 entry drafted as pending (awaiting founder approval, not deployed)"; `2026-10-15-coe.md` 6 | V | |
| 78 | 89 | "To explain why the release was being held out of the log, the message mentioned the marker commits, and to mention them it quoted the marker. The filter matched the word anywhere in the message. The hosting service built the commit and promoted it to production." | API message body; `ignoreCommand` (`grep -qF "[deploy]"`); API statuses (12:46:03Z pending, 12:50:23Z "Deployment has completed"); COE 7, 9 | V | |
| 79 | 91 | "The chief of staff then told the founder that the release was not deployed and was awaiting approval. The founder approved it. Before shipping, the chief of staff searched the history for marker commits and found the one that had already gone out." | COE 8 | V | The COE is the agents' own record. |
| 80 | 91 | "For about twenty minutes production ran a release its owner had not approved, while he was being told nothing had been deployed. The content matched what he approved minutes later." | COE 12-13 | V | |
| 81 | 91 | "The hosting service's own commit statuses show all of this…" | API statuses for `aefb10a` | CwV | Fix 19. |
| 82 | 91 | "…and a script in the press's evidence folder reruns the old filter against the saved messages and reaches the same verdict, so this incident is run as well as recorded." | `press/…/deploy-marker/replay.sh` (committed `a6bc396`) | N | See the second-checker table. |
| 83 | 93 | "The company's incident review traced the cause to a literal string match and asked for four mechanisms: a stricter trigger, a guard on commit messages, an alarm for unapproved production deploys and a written pattern." | COE 19, 28-34 | V | A fifth action, a checklist line with no board id, is also listed. |
| 84 | 93 | "As of 17 October all four are still in the backlog." | `company/ops/board.json`: W-1051, W-1052, W-1053, W-1054 `state: backlog` | V | |
| 85 | 93 | "Its fifth why lands on a person: the chief of staff took the agent's report as truth and did not check." | COE 21 | N | See the second-checker table. |
| 86 | 93 | "What made the whole class harmless came the next day, for a different reason. A release the founder had approved was refused because the day's deployments were spent, and the founder had pushes stop creating deployments at all." | `company/decisions/2026-10-16-founder-no-git-deployments.md`; `vercel.json` `git.deploymentEnabled: false`; `releases.json` r8 (`6cbce514`) | V | |
| 87 | 93 | "On 17 October the mistake came back, a commit with the marker in its body, and nothing happened, because nothing listens for the word any more." | API `54aa64e3` (01:45:24Z; body "no [deploy] since"; 0 statuses); F-48 "Decided"; `vercel.json` | CwV | Fix 20. |
| 88 | 97 | "The company's pattern library already had the lesson filed under a good name, 'a rule without a mechanism is a wish', written from four cases, all found on one day." | `company/knowledge/patterns/a-rule-without-a-mechanism-is-a-wish.md` 1-20 | V | "New 2026-10-14" (before the 10-15 incident). One of the four cases is the deploy-approval rule itself. |
| 89 | 97 | "The catch itself came from checking the disk instead of believing the report…" | retro 51 | V | |
| 90 | 97 | "Let the LLM narrate. Do not let it declare reality." | old 11:171 (heading) | V | Author's line. |
| 91 | 99 | "As of 17 October every claim on every lesson marked published is verified or withdrawn, and no builder verified its own." | python over meta | V | |
| 92 | 99 | "'Gates held while the delegation did not. Nothing unverified was published.'" | retro 52 | V | Verbatim (the source bolds the first sentence). |
| 93 | 99 | "A gate is code… It shows that nothing unchecked got through." | `company/decisions/2026-10-15-founder-show-review.md`; `surface-value.md` 23; `releases.json` 511, 595 | D | Fix 3. |

### §6 Willing to Lose

| # | Line | Sentence (quoted) | Source checked | Status | Note and suggested fix |
|---|---|---|---|---|---|
| 94 | 103 | "The arrangement the company has to beat is the dullest one available. One agent, no roles, no gates, the same model and the same budget, making lessons." | structure decision, option 1 | V | Argued. |
| 95 | 105 | "The founding decision wrote that comparison down as its own reason to be revisited: if the cost per published lesson is more than three times a single-agent baseline with no quality gain." | structure decision 26-28 | V | It is the second of two revisit triggers (EXP-001 is the first). |
| 96 | 105 | "Its first objection, that 26 roles was heavy for 17 lessons, was marked open and funded with a cost comparison." | structure decision 33 | CwV | Fix 21 (optional). |
| 97 | 105 | "As of 17 October nobody has run it." | grep of `company/` for "single-agent", "cost comparison" | V | A negative, searched. Only the decision mentions either. |
| 98 | 105 | "The principles file translates the book's line about A/B tests into a practice, 'Experiments include a simpler baseline that is allowed to win.'" | `principles.md` row "A philosophy of emergence…" | V | Verbatim. |
| 99 | 105 | "The company has eight numbered experiments, and none of them has a result." | `company/experiments/EXP-001` to `EXP-008` | V | Results read "(not run)", "(not run; no data exists)" or "None…". EXP-003 has interim data only. |
| 100 | 107 | "When I designed the store, the first test I wanted was deliberately boring: one placement, a few validated problems, a simple mechanism, and a fight with simplification…" | old 11:201, 11:205 | V | Condensed from the author's text. The tense changes from "The first test I would run" to a past wish: the author should confirm. |
| 101 | 107 | "The company went to fourteen subjects in its first week." | 14 domain folders; the company is under 5 days old | V | |
| 102 | 111 | "A philosophy of emergence should be willing to lose an A/B test. Otherwise it is branding." | `appendix-zen-of-system-3.md`; old 11:205 | V | |
| 103 | 113 | "Before a new study feature for one family of lessons was approved, its builder planted 10 bugs in its own engine and an operations reviewer planted 12 different ones, and the review record says every one was caught, with the number of failing tests for each." | `company/engineering/readiness/2026-10-15-lifehacks-study-tp3-tp4-tp5.md` 73-88, 112-128 | V | Testimony in a committed record; the prose attributes it ("the review record says"). |
| 104 | 113 | "The scripts were never committed and are gone." | readiness 73 ("script in scratch, not committed"), 112 (path); `ls` of that path (absent); `git log --all -- '*plant*'` (only EXP-001) | V | |
| 105 | 113 | "So the press wrote a new harness for the 15 of those 22 bugs it could reproduce exactly… and all 15 were caught, each with exactly the failing count the record printed." | `press/…/plant/README.md`; `result-2026-10-17.json` (15 applied, all `expected == failing`) | V | The record's values. |
| 106 | 113 | "…ran it against the company's committed tests at its latest commit…" | my correction 6 | N | See the second-checker table. |
| 107 | 113 | "That shows the tests can fail. It says nothing about whether a false belief planted in the notes one worker leaves for the next survives into the next worker's plan, which is the test this book proposes for its own central claim." | `appendix-note-on-evidence.md`, "A Test Still to Run" | V | The book frames it as a test of "the book's claim that copies of one model are one witness". "Central" is the writer's word, and fair. |
| 108 | 113 | "The company adopted that test as its first experiment. It is designed and has not been run." | `EXP-001-planted-false-claim.md` 1-25 | CwV | Fix 22. |
| 109 | 113 | "The planters and the harness writer were all copies of one model." | `roles.mjs` (`demo-builder`, `principal-engineer-ops` `inherit`); ledger PE-ops rows `model: null`; `press/org/roles.mjs` (`inherit`); trailers "Claude Opus 5.5" | V | `inherit` names no model. The trailers and the 10-13 COE do. |
| 110 | 113 | "The tests are code, and the counts are what the code produced." | result JSON | V | |

### §7 Written Where Someone Can Argue With It

| # | Line | Sentence (quoted) | Source checked | Status | Note and suggested fix |
|---|---|---|---|---|---|
| 111 | 117 | "If it is not written down where someone can argue with it, it enters through invisible overrides. In the company that sentence opens a protected file the founder owns…" | `company/product/surface-value.md` 1-6; `protected-paths.txt` 5; old 11:195, 11:237 | V | |
| 112 | 117 | "In order: it is true, it works, it teaches the payoff, it is remembered, it is finished. Engagement… is reported, labelled as engagement, and never used to rank lessons or to choose what to build." | surface-value 10-19 | V | |
| 113 | 117 | "The fourth item is to be measured on real learners only, so for now the fourth line of the company's objective measures nobody." | surface-value 15; WBRs 10-13, 10-14, 10-15, 10-16-2 ("no data") | V | |
| 114 | 119 | "The feed is not personalized and says so. A visitor with no history gets subjects in turn, and the first card is labelled 'Fresh picks' where most products would say 'For you'." | `company/decisions/2026-10-12-feed-is-not-personalised.md`; `src/components/Feed.tsx` 233, 239-241 | V | The first card is the intro card: "…this feed is not 'for you'. It alternates subjects." |
| 115 | 119 | "Both ideas began in the store." | feed decision "Rests on: System 3, Ch. 11 ('The Honest Cold Start')"; old 11:115 | V | |
| 116 | 119 | "The company's mission even quotes one of my store sentences back at me: 'If our ecosystem rewards clicks, clickable organisms evolve.'" | `mission.md` 24-25; old 11:111 | CwV | Fix 23 (optional). |
| 117 | 121 | "The product is a vertical feed, the form this book spends pages worrying about…" | Ch 6:333; Ch 12:55, 12:219 | D | Fix 8. |
| 118 | 121 | "…the mission answers that a swipe feed is a delivery format and the company is not in the attention business." | `mission.md` 5-6 | V | |
| 119 | 121 | "On 15 October the founder proposed an amendment that would add rule-based personalization and one labelled ad slot. As of 17 October it is drafted and not ratified." | `company/constitution/amendments/AMD-008-first-light-surface-value.md` 1-6 | V | It also covers mastery features without streaks. |
| 120 | 121 | "And the founder's records treat a goal of ten thousand lessons as given." | throughput record (title; "reaching 10k would be impossible"); `2026-10-16-founder-catalog-closeout.md` 39 | V | I found no record that sets the target either. |
| 121 | 125 | "Gates bind everyone, and the founder may override one in writing, as a decision record with the reason and the objections attached. Disputes about evidence are settled by tests. Disputes about purpose go to the founder." | `constitution.md` 50-55 | V | Art. 4.3's first two sentences are verbatim. Art. 4.1 also requires an owner. |
| 122 | 127 | "One override of a review's ruling is on record." | founder Safari record; `2026-10-16-founder-behavioral-pilot-exemption.md`; `2026-10-14-w556-wave-gate.md` | N | See the second-checker table. |
| 123 | 127 | "On 17 October a launch review made a Safari check a condition for releasing the knot lesson… Its title is *Can a knot match its mirror?*" | `company/rituals/records/2026-10-17-launch-review-left-or-right-r9.md` ruling 2 (b); meta `title` | V | The condition binds deploys, not publication: "releasing" is right. |
| 124 | 127 | "The company's machines could not run Safari's engine." | r9 ruling 2 (e); Safari record 18 ("No WebKit run") | V | |
| 125 | 127 | "The founder was shown the consequence in one line: if the card fails there, iPhone users see the mirror-image knot after 'Turn over'." | `company/decisions/2026-10-17-founder-deploy-r9-left-or-right-safari.md` 12 | V | |
| 126 | 127 | "His recorded word was 'Deploy', and he chose the option labelled 'Ship it anyway'." | Safari record 11-12; my correction 8 | N | See the second-checker table. |
| 127 | 127 | "The record states the risk, what would prove the decision wrong and how to revert it, and says the waiver is not a verification and does not carry to any later deploy." | Safari record 17-30 | V | |
| 128 | 127 | "Those words reached the file second-hand: the release manager wrote them down from what the chief of staff relayed." | Safari record 8; my correction 8 | N | See the second-checker table. |
| 129 | 133 | "Agents can propose amendments, and one drafted the ad-slot amendment." | `constitution.md` Art. 3.1; AMD-008 `prepared_by: evaluation-steward` | V | |
| 130 | 133 | "Only the founder ratifies." | `constitution.md` Art. 3.2; AMD-012 110-112, 129-130 | CwV | Fix 24. |
| 131 | 133 | "A learner can open the sheet and see what any sentence rests on. She has no way to amend what the minute is for." | `constitution.md` Art. 6.3, Art. 3 | V | "Any claim" would be more exact than "any sentence". |

### §8 The Student Has Not Been Asked

| # | Line | Sentence (quoted) | Source checked | Status | Note and suggested fix |
|---|---|---|---|---|---|
| 132 | 139 | "…the card prints its teaching evidence: 0 human-learner studies, 2 simulated-learner reviews, 2 browser QA runs. Then… 'Simulated learners find problems; only people can show that a lesson teaches.'" | `DemoCard.tsx` 130-134; meta `evidence`; production `/api/meta/base-rates` at 15:53Z (`qa: 2, simulatedLearner: 2, humanLearners: 0`) | V | Verbatim. |
| 133 | 141 | "In the lesson's file the same fact is a field, `"humanLearners": []`. As of 17 October 2026 it is empty in all 1,283 lessons." | python: 1,283 of 1,283 have `[]` | V | |
| 134 | 141 | "The company's rules make every learner review open with the same line: 'Simulated learner. This review finds problems; it is not evidence that anyone learned.'" | `company/reviews/README.md` 31-32 | V | Verbatim; both base-rates reviews open with it. |
| 135 | 141 | "The simulated adult who reviewed the town of a thousand reported that it picked 99%, 'and so would most adults'." | `company/reviews/base-rates/2026-10-13-learner-adult-beginner-v2.md` 10 | V | "I picked 99% and so would most adults." |
| 136 | 143 | "Judea Pearl's ladder of causation separates seeing from doing, and no amount of the first answers questions about the second on its own.[2]" | `appendix-references.md` 513 (`ref-11-store-pearl`, *The Book of Why*) | V | Association versus intervention; "on its own" keeps it accurate. |
| 137 | 145 | "…five adults, five lessons each, thinking aloud, then a recall question three days later, with the prediction committed before any data. It was designed on the day the company started. It has not been run." | `company/experiments/EXP-002-real-learner-recall.md` 1-30 | V | |
| 138 | 145 | "The sessions are the founder's to run, and the task of recruiting the five sits in the backlog under his name." | EXP-002 owner; `board.json` W-007 (`owner: founder`, `state: backlog`) | V | |
| 139 | 145 | "As of the afternoon of 17 October, most of what the company made after 15 October had not reached anyone outside it." | curl GETs at 15:53Z; API runs; my correction 9 | N | See the second-checker table. |
| 140 | 149 | "…one founder and about a hundred roles of agents did in under five days: more than a thousand lessons, a checked claim behind every factual sentence of the ones marked published, gates that held…" | 99 roles; 1,283 lessons; span 4 d 15.5 h; `launchGates()` | CwV | Fix 25. Also "gates that held" should agree with fix 3. |
| 141 | 153 | "The company has asked a thousand times for a guess before it would show anything." | `Lesson.tsx` predict phase; `contract.spec.ts` 52 ("no reveal before a prediction") | V | A figure over 1,283 lessons. |
| 142 | 153 | "What the minute is for is written in a file the founder owns." | `surface-value.md` 3 | V | |
| 143 | 51, 87, 129 | Factual statements inside the AUTHOR comments (reference [1] would leave with the store passage; the throughput quote "reached the record through the chief of staff"; the Safari words were "written by the release manager from the chief of staff's relay") | `appendix-references.md` 511; throughput record 5; Safari record 8 | V | The comments stay as they are. |

## Evidence categories (against `chapters/appendix-note-on-evidence.md`)

- **The Note's Chapter 11 row is now false.** The row reads "My prototype store, its customers and a proposed business experiment | Prototyped; the business experiment has not run". The draft rests on System 3 Company's records, two press reruns, and four paragraphs of the store. The consequential-edits proposal (M8) leaves the category to the fact-checker. **My proposal (needs independent check; the founder decides):** "11. Guess First | System 3 Company's own records (lesson files, gates, incident reviews, decisions, release log, token ledger), two of its mechanisms rerun by the press from committed scripts, and my prototype store | Reported from the company's records, much of it agents' testimony; two mechanisms run; the store prototyped; no learner outcome measured".
- **The Note's line 5 conflicts with the draft** (M9). It says companies' names and details "have been changed". The draft names System 3 Company and its real records. The Note needs an exception for Chapter 11. That is the founder's call.
- **"Run" in the prose:** L113 holds (the harness is committed: `press/…/plant/`). L91 overreaches: only the filter's logic is run (row 82, second checker).
- **"Testimony-grade" (L81), "the company's numbers, which I have not recomputed" (L85), "the review record says" (L113)** match what the sources are. They do not upgrade testimony to a measurement.
- **No sentence upgrades an argued claim to a reported one,** apart from rows 31 and 35, where the prose states as fact something the records contradict.
- **Chapter title.** The file, `appendix-references.md` 509 and the Note's row still say "The Store That Builds Itself". The draft's heading says "Guess First". This is consequential edit M14, flagged here so the two do not ship apart.

## Dates and "as of"

- Every "As of 17 October" holds at the company's `e84b8784` (14:21:02Z), which was still the default-branch head at 15:46Z. The repo keeps moving, so the writer could pin the counts once: "as of 14:21 UTC on 17 October".
- L57's "By 14:21 on 17 October" and L145's "afternoon of 17 October" are consistent with the 15:53Z site reading.
- L33 and L127 date the knot dispute and the Safari waiver to 17 October: verified (fact-check record and decision both dated 2026-10-17).

## References

- **[1] `ref-11-slate`** (L47): cited once, for "slate and whole-page optimization". Wang et al. is whole-page presentation and SlateQ is slates, so the reference supports the term. It appears in order as reference 1.
- **[2] `ref-11-store-pearl`** (L143): cited once, for the seeing/doing ladder. Used correctly.
- If the store passage is cut (Ask 2), [1] has to go, as the AUTHOR comment says, and [2] becomes [1].

## Handoff (fact-checker-system-3, 2026-10-17)

- **Changed:** wrote this file only. No edits to the chapter, the company repo or anything else. No commits. Scratch: `/tmp/claude-0/-home-user/f0be7ef4-e990-5584-991b-e9d7e05d7372/scratchpad/ch11/` (`town.mjs`, `old11.md`).
- **Believe:** high confidence in the recomputed counts and the W figures, which were run from the lesson's own code. High confidence in fixes 1-5: each rests on a file I quote. Medium on fix 6's exact count (31 of 41 is my tally of table rows against the appendix). Medium on item 27, a negative search of the book.
- **Next:** a second fact-checker instance or the development editor checks the ten N rows and every proposed fix. Then the writer revises. The founder decides the Note on Evidence row (M8/M9) and item 26 (how the models are paid for).
- **Blocked:** Vercel deployment list (no access), so a CLI or dashboard deploy cannot be ruled out for row 139.

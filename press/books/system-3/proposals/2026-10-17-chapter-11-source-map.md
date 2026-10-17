# Source map: Chapter 11 draft ("Guess First"), 2026-10-17

owner: writer-system-3 (Callum) · for: **fact-checker-system-3 only** (brief §5.4). Not for the development editor or the panel: evaluators read the text first.
chapter: `chapters/11-the-store-that-builds-itself.md` on branch `ccr-fd4ebbbc-p06k8x` (uncommitted draft)
evidence: record = `press/books/system-3/experiments/2026-10-company-case-study/record.md` (IDs A1-A9, B, C1-C15, D, E, F, G); FC = `resources/evaluations/2026-10-17-fact-check-company-case-study.md` (row numbers); CR = `/home/user/system-3-company` at `e84b8784`, read-only.
**Revision 1 (2026-10-17) is at the end of this file and supersedes the rows it names. Read it first.**

status: **writer's map. Nothing here is checked by me; I may not mark my own work checked.** Where the FC corrected the record I used the FC value. Items marked **X** are not in the record or the FC and must be added from company sources before they stay. Items marked **W** are things I computed or read myself from company code: the fact-checker must recheck them, because the writer is not a checker.

Quotes are abbreviated with "…" where the sentence is long; locate by the opening words.

## §1 Ninety-Nine Percent Accurate

| # | Sentence (opening words) | Source | Category in the prose |
|---|---|---|---|
| 1.1 | "Its title is a question, *You tested positive. Now what?*… ‘The test is 99% accurate. So you’re 99% likely to be sick. Right?’" | **X1** CR `src/demos/probability/base-rates/meta.json` `title`, `hook` | described artefact |
| 1.2 | "A disease affects 1 in 1,000 people. A test flags 99%… four buttons: about 99%, about 90%, about 50%, about 9%." | **X1** CR `src/demos/probability/base-rates/Demo.tsx` `predict` prop (question, options) | described artefact |
| 1.3 | "Nothing else on the card works until you press one… ‘Make a prediction to start.’" | **X1/W** `Demo.tsx` (`disabled={locked …}`; message `locked ? "Make a prediction to start."`) | described artefact |
| 1.4 | "a grid of a thousand empty squares… You press +100… all of them healthy… one of them lights up positive" | **X1/W** `Demo.tsx` (`TOTAL = 1000`, "+100" control, `town()`, seeded `ORDER`). I ran `town(1000)` from the file's code in my scratchpad: at 100 filled, 0 sick, 1 positive. The base-rates simulated review (`company/reviews/base-rates/2026-10-13-learner-adult-beginner-v2.md`) reports the same ("The first 100 people show '0 are sick' and 1 positive"). **Recheck.** | described artefact |
| 1.5 | "The first sick one arrives somewhere in the third hundred." | **W** same run: sick count 0 at 200, 1 at 300. **Recheck.** | described artefact |
| 1.6 | "Eleven squares light up, and one of them has a circle around it… ‘11 tested positive. 1 of them is actually sick.’" | **X1/W** `Demo.tsx` message template `${positives} tested positive. ${truePos} of them … is actually sick.`; ring drawn for true positives when `truePos <= 10`; meta c9 ("11 positives of whom 1 is sick") | described artefact |
| 1.7 | "Eleven positives, one sick, ten false alarms… 1% of the 999 healthy people… about 9%." | **X1** `Demo.tsx` reveal first paragraph; meta c2, c3 | described artefact |
| 1.8 | "‘‘99% accurate’ describes the test. Your chance also depends on how rare the disease is.’" | **X1** `Demo.tsx` reveal second paragraph (verbatim); meta c7 source | quotation of the lesson |
| 1.9 | "Two more towns unlock. At 1 in 100, ten of twenty… At 1 in 10 it is 99 of 108." | **X1** `Demo.tsx` (rates locked until milestone; `MID`, `HIGH`); meta c4, c9 | described artefact |
| 1.10 | "in a 1978 study at Harvard Medical School the most common answer… was 95%… about 2%" | **X1** `Demo.tsx` reveal third paragraph (`className="muted"`); meta c6 (Casscells et al. 1978). The chapter reports what the lesson says; the study itself is the lesson's claim, verified by the company's fact-checker. I say "in grey" for `muted`: **recheck the styling word** or cut it. | described artefact |
| 1.11 | "Days later the idea is supposed to come back… 1 in 10,000… Almost all, about half, or about 1 in 100?" | **A1** (`company/mission.md` 7-8: "Days later the idea comes back as a single question"); **X1** meta `recall` (question, options) | designed ("supposed to") |
| 1.12 | "calls it a sixty-second lesson. Its own file budgets eighty seconds" | A1 (`company/README.md` 3-4, FC row 5; mission "about sixty seconds"); **X8** meta `durationSec: 80` | described artefact |
| 1.13 | "An agent built it, another agent checked its facts, a third pretended to be a learner and reviewed it, and a fourth pressed every button in a browser." | **X1** meta `owner.builder: demo-builder`; `claims[].checkedBy: fact-checker`; `evidence.simulatedLearner` (2 files), `evidence.qa` (2 files); `company/principles.md` ("Computer-use QA presses every button"). Note C12: the QA *label* is a constant, so which role ran base-rates QA is not certain; the sentence says only "an agent". | observed |
| 1.14 | "Every factual sentence you just read is written down somewhere with an address." | A4 (`CLAUDE.md` line 18; FC row 26); **X1** nine claims with ids | designed rule + observed for this lesson. **Check** that every factual sentence of §1 maps to c1-c9 or the recall card (I believe it does). |

## §2 Nine Claims Behind One Minute

| # | Sentence | Source | Category |
|---|---|---|---|
| 2.1 | "the third of nine claims… address is `probability.base-rates.c3`… derivation… 0.0902… verified, checked by the fact-checker on 12 October 2026" | **X1** meta c3 (`support`, `source`, `status`, `checkedBy`, `checkedOn`) | observed |
| 2.2 | "The other eight cover…" (list) | **X1** meta c1, c2, c4, c5, c6, c7, c8, c9 (c8 is the recall card's content) | observed |
| 2.3 | "‘Why trust this? (9/9 claims checked)’… lists each claim… checked… what it rests on (‘a derivation (worked out step by step)’)… address in tiny type" | **X7** CR `src/components/DemoCard.tsx` lines 79-80, 89-125 (button text, sheet, `muted tiny` address line); `src/lib/trust.ts` (`SUPPORT_LABEL.derivation`, `STATUS_LABEL.verified = "checked"`). The "9/9" is **W**: derived from 9 verified, 0 withdrawn claims via `countsTowardTrust`. Whether the live production site shows this lesson is **not established** (C8); the chapter does not say it does. | described artefact |
| 2.4 | "The working notes stay behind. The sheet tells you a claim was checked, and leaves out who checked it and how." | **X7** `trust.ts` header comment ("A claim's `source`… never reaches a learner") and `LearnerClaim` fields (no `checkedBy`) | described artefact |
| 2.5 | Camel sentence | Old chapter `11:113`, verbatim; register row "The camel". Not a company claim. | — |
| 2.6 | "The command that publishes a lesson refuses if any claim is neither verified nor withdrawn, and it refuses a claim marked verified by the role that built the lesson." | A4 (`tools/company.mjs` 139-157, line 146; FC rows 24-25) | code (a gate) |
| 2.7 | "‘Builders never mark their own claims verified.’" | A4 (`CLAUDE.md` line 18; FC row 26) | quotation |
| 2.8 | "As of 17 October 2026, the lessons marked published… 3,891 verified claims, and the builder role verified none of them." | D row 1; E; FC rows 82-83 | observed count (recomputed by FC) |
| 2.9 | "In one release a lesson about bargaining was held back because a single claim was still unchecked." | C14 (`company/ops/releases.json` r7 features; FC row 80). "Bargaining" is **X12**: the lesson is `patience-wins-the-split`; releases.json line 509 says its map label names Rubinstein (the bargaining model). **Check the topic word.** | observed |
| 2.10 | "On 17 October a fact-checker disputed a sentence in a lesson about knots: the builder had stated the rule… backwards. The claim stayed disputed until the builder rewrote it." | C14 (`src/demos/math/left-or-right/meta.json` c5 note, History; FC row 27, which adds "from the fact-check's suggestion") | observed; one-model limit stated in the next paragraph |
| 2.11 | "The builder that wrote the 9% and the fact-checker that checked it run on the same model." | Record header (one-model limit); **X** `tools/org/roles.mjs`: `demo-builder` and `fact-checker` both `model: "inherit"` (lines 217, 246). | observed (config) |
| 2.12 | "The witnesses that are not the model are few: the founder, code that runs, and the records kept by other companies’ systems." | Record header line 14 as corrected by FC (row 94: the founder's *words* reach the disk through agents; the chapter's other quotations say so where used) | argued |
| 2.13 | "Two of the nine claims… were added by the fact-checker, each with a note that it ‘needs an independent check’, and then marked verified by the fact-checker a day later." | **X2** meta c7 and c8 `source` ("Added by fact-checker 2026-10-12; needs an independent check."), `checkedBy: fact-checker`, `checkedOn: 2026-10-13`; SS S1 | observed |
| 2.14 | "The gate passed them, because the rule it enforces is about builders." | A4 (line 146 compares `checkedBy` with `meta.owner.builder`) | code |

## §3 A Company in a Week

| # | Sentence | Source | Category |
|---|---|---|---|
| 3.1 | Store passage (four paragraphs) | The author's own sentences from the old chapter (`11:5`, `11:9`, `11:15`, `11:239`), trimmed; `ref-11-slate` [1] kept on the whole-page optimisation sentence. The 11:7 AUTHOR comment is moved verbatim. Nothing added about what the prototype did. | lived (author's existing text) |
| 3.2 | "an organization that builds lessons and is run almost entirely by agents" | A2 (98 agent files, every role but the founder a subagent; FC row 10); E (commit authors `Claude` 1,532 of 1,666 local; FC row 87) | observed |
| 3.3 | "Its first commit landed at 22:51 UTC on 12 October 2026. By 14:21 on 17 October, four days and fifteen and a half hours later, the main branch held 2,718 commits." | B; E; FC rows 42, 49 (span 4 d 15 h 29.5 min; 2,718 on the default branch) | observed |
| 3.4 | "The founding decision created 26 roles, 25 agents and the founder. By the night of the 13th there were 72. As of 17 October the org data lists 99." | A2 (progress.md 2341, 2282; roles.mjs); FC rows 10, 14; **X3** `company/decisions/2026-10-12-company-structure.md` line 18 ("26 roles (25 agents and the founder)") | observed |
| 3.5 | "The vision written on the first day planned eight subjects and about twenty lessons for the quarter." | **X5** CR `company/product/vision.md` (last reviewed 2026-10-12): "Now (Q4 2026): 8 domains, ~20 lessons". | observed |
| 3.6 | "1,283 lessons in 14 subjects, from probability to history, and 720 of them are marked published" | E; FC row 84 ("domains" written as "subjects"; history is one of the 14 directories) | observed count |
| 3.7 | "Each worker is a fresh session of a model. It arrives knowing nothing except what is on disk… leaves a dated note at the top of a log." | A3 (`CLAUDE.md` line 5; progress.md rule; FC rows 20-21) | designed rule |
| 3.8 | "‘testimony from a worker who no longer exists: check what you rely on.’ There are 269 of them." | A3; E; FC row 21 | quotation; observed count |
| 3.9 | "All of these roles run on one developer’s models, rented by the token." | Record header (48 `sonnet`, 49 `inherit`, 2 unset; trailers name one vendor's model; FC row 4). "Rented by the token" is the brief's rented-capacity sentence (§1.4 item 4). | observed (config) |
| 3.10 | "113.1 million tokens… up to 16 October, from a ledger with known gaps, so the real figure is higher. The records hold no figure for money." | E, F; FC row 88 (113.1M over 948 measured rows; 44 null; main coordinator session excluded); F ("No money figure exists in the records I read") | the company's own ledger, testimony-grade |

## §4 Built From the Book

| # | Sentence | Source | Category |
|---|---|---|---|
| 4.1 | "Its principles file takes each line of the Zen of System 3… and gives it a practice and the file where the practice lives." | D (principles row); CR `company/principles.md` lines 1-3 | observed |
| 4.2 | "Its decisions carry a heading, ‘Rests on’, and the founding one rests on three chapters of this book." | **X3** `2026-10-12-company-structure.md` lines 22-23 (Ch. 3, Ch. 5, Ch. 7) | observed |
| 4.3 | "The parts were designed on the first day, generated from a file." | **X3** line 18 ("generated from `tools/org/roles.mjs`"); B (commit `7629eeb9`, 23:03) | observed |
| 4.4 | "Its founding decision records the objection that several roles share one model, so their independence is ‘partly theatre’, and marks it accepted in part." | **X3** line 34 | quotation |
| 4.5 | "The company has a sibling, a press founded to make my books, and the press is also a company of agents running on the same model. It studied this company’s records, checked them, and briefed and drafted the pages you are reading." | A2 (press founded 2026-10-15; `company/decisions/2026-10-15-founder-press-sibling-company.md`); commission `press/decisions/2026-10-17-founder-store-chapter-rewrite.md` objection 2; this record, the FC, the brief | observed |

## §5 The Book Comes Back to Bite Me

| # | Sentence | Source | Category |
|---|---|---|---|
| 5.1 | "with twenty lanes, each with a manager" | C6 (retro "20 lanes"; POC map in `2026-10-16-founder-org-and-dispatch-rule.md`) | designed |
| 5.2 | "On 16 October its own retrospective measured the previous 48 hours… about 99%… every one of the 223 dispatches in the log for that window named it as the actor." | C6; `company/rituals/records/2026-10-16-retro-delegation.md` line 47 and numbers table; FC row 66 / correction 7 | **the retrospective's own measurement, testimony-grade by its own label**; said so in the prose |
| 5.3 | "‘The org chart says 20 lanes; in practice there was one dispatcher who asked managers questions.’" | retro line 47 (verbatim; I checked the wording in CR, the FC should confirm) | quotation |
| 5.4 | "The log was backfilled afterwards, so they cannot be recomputed from today’s files, though every dispatch in today’s version of that window still names the same actor." | FC correction 7 (372 events in the window today, all `actor: chief-of-staff`, 5 with `batch=`) | FC's recomputation (**needs independent check** per FC) |
| 5.5 | "The same day the founder made a rule that the coordinator dispatches only after asking the lane’s manager what to run." | C6; A2; `2026-10-16-founder-org-and-dispatch-rule.md` rule 2; FC rows 16, 65 | designed |
| 5.6 | "the eight agents running when it was written had been dispatched without asking… keeps open an objection that managers cannot start agents themselves" | C6 (Transition; Objections row 2 open); FC row 65 | observed record |
| 5.7 | "Across 13 and 14 October the company made 852 new lessons. Across the next two days it made 10. On 16 October… new builds took 8% of the day’s 18.65 million tokens and manager rounds took 35%" | C6 cost paragraph; `company/decisions/2026-10-16-founder-throughput-for-10k.md` lines 11-17; FC row 67 | **the company's own count, not recomputed**; said so |
| 5.8 | "‘Building costs about 146k per new lesson; the rest is the machine around it.’" | throughput record line 17 (verbatim in CR) | quotation |
| 5.9 | Founder quotation "What is going on you are working all the day but number of demos did not move" | G; C6; throughput record line 8 ("recorded by: chief-of-staff"); FC rows 67, 93-94. AUTHOR permission comment beside it (quote 1 of 3 permitted). | founder's words as transcribed by an agent; said so |
| 5.10 | "On 14 October, after agents’ work-in-progress pushes had used up the hosting service’s free allowance of 100 deployments a day, the founder decided that every deploy needs his approval, every time." | A8; `company/decisions/2026-10-14-deploy-needs-founder-approval.md`; FC row 36 | observed |
| 5.11 | "At that point the hosting service built only commits whose message carried a marker word." | A8 (`deploy-needs-founder-approval.md` Decision; COE 2026-10-15 line 7); B (filter added `f868127`) | observed |
| 5.12 | "At 12:45 UTC the next day, the release manager prepared a release it had been told not to deploy… quoted the marker. The filter matched the word anywhere… built the commit and promoted it to production." | C1; `company/rituals/records/2026-10-15-coe.md` lines 6-7; FC rows 50-51 | observed; trigger logic **run** (replay, FC row 52) |
| 5.13 | "The chief of staff then told the founder… not deployed… The founder approved it. Before shipping, the chief of staff searched… found the one that had already gone out." | C1; COE line 8; FC row 50 | observed (the COE is an agents' record) |
| 5.14 | "For about twenty minutes production ran a release its owner had not approved… The content matched what he approved minutes later." | C1; COE lines 12-13 | observed |
| 5.15 | "The hosting service’s own commit statuses show all of this, and a script in the press’s evidence folder reruns the old filter… reaches the same verdict" | C1 re-checks; `deploy-marker/` committed `ee44535`; FC rows 51-52 and "stale qualifier" note (run holds) | third-party record + **run** |
| 5.16 | "asked for four mechanisms: a stricter trigger, a guard on commit messages, an alarm for unapproved production deploys and a written pattern. As of 17 October all four are still in the backlog." | C1; COE lines 28-34; `company/ops/board.json` (W-1051..W-1054 `backlog`); FC row 54 | observed; actions designed, unclosed |
| 5.17 | "Its fifth why lands on a person: the chief of staff took the agent’s report as truth and did not check." | COE line 21; **FC row 53 (dispute): used in the FC's form, not the record's "named a mechanism, not a person"** | observed |
| 5.18 | "A release the founder had approved was refused because the day’s deployments were spent, and the founder had pushes stop creating deployments at all." | C1 "What happened to the fix"; B (r8 19:11Z rate-limited; `cdee168c` 20:28); `2026-10-16-founder-no-git-deployments.md` Why, Decided; FC rows 47, 54 | observed; third-party status |
| 5.19 | "On 17 October the mistake came back, a commit with the marker in its body, and nothing happened" | C1 (`54aa64e3`; progress.md line 11 incident 4; no Vercel status); FC row 54 | observed |
| 5.20 | "‘a rule without a mechanism is a wish’, written from four cases, all found on one day" | D (pattern row); CR `company/knowledge/patterns/a-rule-without-a-mechanism-is-a-wish.md` line 3 ("Four cases, all one day, all found by the same set of COEs") | observed |
| 5.21 | "The catch itself came from checking the disk instead of believing the report" | retro "What went well" item 2 ("Catches came from checking the disk"); C1 | observed (the company's own reading) |
| 5.22 | "Let the LLM narrate. Do not let it declare reality." | Old chapter heading (`11:171`), the author's line, reused per brief §3.4 | — |
| 5.23 | "As of 17 October every claim on every lesson marked published is verified or withdrawn, and no builder verified its own." | D row 1; E (3,922 = 3,891 verified + 31 withdrawn); FC rows 82-83 | observed count |
| 5.24 | "‘Gates held while the delegation did not. Nothing unverified was published.’" | retro line 52, verbatim (SS S6 quotes it; not in the record; **X**) | quotation |

## §6 Willing to Lose

| # | Sentence | Source | Category |
|---|---|---|---|
| 6.1 | "if the cost per published lesson is more than three times a single-agent baseline with no quality gain" | **X3** `2026-10-12-company-structure.md` lines 26-28 (verbatim wording "more than 3× a single-agent baseline with no quality gain") | designed |
| 6.2 | "Its first objection, that 26 roles was heavy for 17 lessons, was marked open and funded with a cost comparison. As of 17 October nobody has run it." | **X3** line 33 ("open, funded: EXP-001 plus a cost comparison in the first OP"); A9 (no experiment has a result); my search of CR found no cost comparison against a single agent (`grep -rn -i "single-agent"`; `company/rituals/records/2026-10-12-op-planning.md` has none). **Check "nobody has run it" against the first OP and any later cost review.** | designed, not run |
| 6.3 | "‘Experiments include a simpler baseline that is allowed to win.’" | **X10** `company/principles.md`, row "A philosophy of emergence…" | quotation |
| 6.4 | "The company has eight numbered experiments, and none of them has a result." | A9; E; FC row 41 (EXP-003 "Interim data (not a result yet)") | observed |
| 6.5 | "When I designed the store, the first test I wanted was deliberately boring…" | Old chapter `11:201-205` (author's own position) | argued (author's existing text) |
| 6.6 | "The company went to fourteen subjects in its first week." | E (14 domains); B (span) | observed |
| 6.7 | A/B line and "Otherwise it is branding." | Old chapter `11:205`, verbatim (brief §3.1) | — |
| 6.8 | "Before a new study feature for one family of lessons was approved, its builder planted 10 bugs in its own engine and an operations reviewer planted 12 different ones… every one was caught, with the number of failing tests for each." | C5; `company/engineering/readiness/2026-10-15-lifehacks-study-tp3-tp4-tp5.md` lines 73-88, 112-129; FC row 62 | testimony in a committed record |
| 6.9 | "The scripts were never committed and are gone." | C5 (searched path does not exist; no harness committed); FC row 63 | observed |
| 6.10 | "the press wrote a new harness for the 15 of those 22 bugs it could reproduce exactly, ran it against the company’s committed tests at its latest commit, and all 15 were caught, each with exactly the failing count the record printed" | C5; `plant/` (committed `ee44535`); FC row 64 and correction 6 ("a new run at `e84b8784`", not "at the approved state": the prose says "at its latest commit") | **run** |
| 6.11 | "The company adopted that test as its first experiment. It is designed and has not been run." | A9 (EXP-001 "designed, not run"; "the book's own test adapted"); FC row 41 | designed, not run |

## §7 Written Where Someone Can Argue With It

| # | Sentence | Source | Category |
|---|---|---|---|
| 7.1 | "In the company that sentence opens a protected file the founder owns" | A1, A7; **X15** CR `company/product/surface-value.md` lines 1-6 (owner founder, protected; "If the objective is not written down where someone can argue with it, it enters through invisible overrides.") | observed |
| 7.2 | "In order: it is true, it works, it teaches the payoff, it is remembered, it is finished. Engagement… never used to rank lessons or to choose what to build." | A1; FC row 8; surface-value.md 10-19 | designed |
| 7.3 | "The fourth item is to be measured on real learners only" | **X15** surface-value.md line 15 ("real learners only"); C7 (no real learners) | designed; observed absence |
| 7.4 | "The feed is not personalized and says so. A visitor with no history gets subjects in turn, and the first card is labelled ‘Fresh picks’" | **X4** `company/decisions/2026-10-12-feed-is-not-personalised.md` (Decision); surface-value.md line 23; **X17** `src/components/Feed.tsx` line 233 (`Fresh picks`); A1 mission ("Fresh picks", not "For you") | designed (in code); production display not established |
| 7.5 | "Both ideas began in the store." | X4 "Rests on: System 3, Ch. 11 ('The Honest Cold Start')"; old chapter "The Objective Fights Back" | argued (the chapter does not say a company file cites the old chapter, per brief §3.4) |
| 7.6 | "The company’s mission even quotes one of my store sentences back at me: ‘If our ecosystem rewards clicks, clickable organisms evolve.’" | **X14** `company/mission.md` lines 24-25; old chapter `11:111` | quotation |
| 7.7 | "the mission answers that a swipe feed is a delivery format and the company is not in the attention business" | A1; `mission.md` lines 5-6 | quotation (paraphrased) |
| 7.8 | "On 15 October the founder proposed an amendment that would add rule-based personalization and one labelled ad slot. As of 17 October it is drafted and not ratified." | D Layer 4 row; A7 (AMD-008 proposed); **X16** `company/constitution/amendments/AMD-008-first-light-surface-value.md` header (date 2026-10-15; `proposed_by: founder`; `prepared_by: evaluation-steward`; "status: proposed (draft, not applied)") | observed |
| 7.9 | "the founder’s records treat a goal of ten thousand lessons as given" | C6/F-41 (`2026-10-16-founder-throughput-for-10k.md` title and founder's quoted words "reaching 10k would be impossible"); `2026-10-16-founder-catalog-closeout.md` objection row ("the 10k goal"). I found no record that *sets* the target; hence "treat… as given". **Check.** | observed record |
| 7.10 | "Gates bind everyone, and the founder may override one in writing, as a decision record with the reason and the objections attached." | A7 (constitution Art. 4.1); FC row 32 | designed |
| 7.11 | "Disputes about evidence are settled by tests. Disputes about purpose go to the founder." | **X6** `company/constitution/constitution.md` Article 4.3 (verbatim first two sentences) | quotation |
| 7.12 | "One override of a review’s ruling is on record. On 17 October a launch review made a Safari check a condition for releasing the knot lesson" | C9; `2026-10-17-founder-deploy-r9-left-or-right-safari.md` lines 1-12; FC row 74 (the waived item is a launch-review ruling, not a coded gate: the prose says "a review's ruling"). "One… on record" is my reading of the record (C9 is the one case the brief names); **check whether any other founder waiver exists**. | observed |
| 7.13 | "the one whose rule the fact-checker had caught backwards. Its title is *Can a knot match its mirror?*" | C14; **X13** `src/demos/math/left-or-right/meta.json` `title` | observed |
| 7.14 | "The company’s machines could not run Safari’s engine." | C9 ("the container could not run WebKit") | observed |
| 7.15 | "if the card fails there, iPhone users see the mirror-image knot after ‘Turn over’" | C9; record line 12 (option text, verbatim fragment) | quotation of the option text |
| 7.16 | "His recorded word was ‘Deploy’, and he chose the option labelled ‘Ship it anyway’." | **FC correction 8** (founder's word "Deploy"; "Ship it anyway" an option label); record lines 11-12. AUTHOR permission comment beside it (quote 2 of 3). | founder's words as transcribed |
| 7.17 | "The record states the risk, what would prove the decision wrong and how to revert it, and says the waiver is not a verification and does not carry to any later deploy." | C9; record lines 17-30; FC row 74 | observed |
| 7.18 | "the release manager wrote them down from what the chief of staff relayed" | record line 8 ("recorded by: release-manager (from the words the chief-of-staff relayed…)"); FC correction 8 | observed |
| 7.19 | "Agents can propose amendments, and one drafted the ad-slot amendment. Only the founder ratifies." | A7 (constitution amendment process; board membership); X16 (`prepared_by: evaluation-steward`; "ratified by the founder") | designed |

## §8 The Student Has Not Been Asked

| # | Sentence | Source | Category |
|---|---|---|---|
| 8.1 | "the card prints its teaching evidence: 0 human-learner studies, 2 simulated-learner reviews, 2 browser QA runs… ‘Simulated learners find problems; only people can show that a lesson teaches.’" | **X7/W** `DemoCard.tsx` lines 127-131 (template, verbatim sentence); counts from meta `evidence` arrays (0, 2, 2) via `PublicMeta`. Production display not established (C8). | described artefact |
| 8.2 | "`"humanLearners": []`. As of 17 October 2026 it is empty in all 1,283 lessons." | X1; C7; E; FC row 68 | observed count |
| 8.3 | "The company’s rules make every learner review open with the same line: ‘Simulated learner. This review finds problems; it is not evidence that anyone learned.’" | A5 (reviews README rule 6; FC row 28). Softened to the rule because **W**: of 1,811 files matching `company/reviews/*/*learner*.md`, 17 do not contain the line anywhere (some may be reading records, not reviews). | designed rule |
| 8.4 | "The simulated adult who reviewed the town of a thousand reported that it picked 99%, ‘and so would most adults’." | **X9** `company/reviews/base-rates/2026-10-13-learner-adult-beginner-v2.md` line 10 ("I picked 99% and so would most adults") | quotation of an agent's review |
| 8.5 | Pearl sentence [2] | `ref-11-store-pearl`; the observation-versus-intervention point (brief §3.4) | cited |
| 8.6 | "five adults, five lessons each, thinking aloud, then a recall question three days later, with the prediction committed before any data. It was designed on the day the company started. It has not been run." | A9; C7; CR `company/experiments/EXP-002-real-learner-recall.md` (date 2026-10-12, status, design) | designed, not run |
| 8.7 | "The sessions are the founder’s to run, and the task of recruiting the five sits in the backlog under his name." | C7 (W-007 "Recruit 5 learners for EXP-002", owner founder, `backlog`); EXP-002 `owner: founder (sessions)` | observed |
| 8.8 | "As of the afternoon of 17 October, most of what the company made after 15 October had not reached anyone outside it." | F (production as of 15:07Z); FC correction 9 and row 70 (fresh at 15:16Z). The only C8 use, at the level brief §4.4 and D16 allow. **Recheck with a fresh timestamp**: the 14:44Z deploy run was still in progress at 15:16Z. | observed (third-party) |
| 8.9 | "one founder and about a hundred roles of agents did in under five days: more than a thousand lessons, a checked claim behind every factual sentence of the ones marked published, gates that held" | E (99 roles; 1,283 lessons; 720 published); D row 1; B (4 d 15.5 h). "A checked claim behind every factual sentence" rests on the gate (A4) plus the rule (CLAUDE.md 18): the gate checks that claims are verified, not that every sentence has a claim. **The fact-checker should decide whether this needs "by the company's rule".** | observed + designed |
| 8.10 | "The company has asked a thousand times for a guess before it would show anything." | A1 (predict-before-reveal in every card, enforced by the kit, `principles.md` "Predict before reveal, enforced by the kit and QA"); E (1,283) | figure of speech over an observed count |

## Not in the prose (deliberately)

C2 "one in six" (withdrawn, FC row 58); C3 backend engineer (withdrawn, FC row 60); C4; C8 as a contradiction (D16); C10, C11, C12, C13, C15; persona names; vendor, repository, URL and model names; release numbers, board ids, amendment numbers, file paths.

---

## Revision 1 (2026-10-17): every changed or new sentence

For **fact-checker-system-3 only**, as before. Text: `chapters/11-the-store-that-builds-itself.md` after Revision 1 (uncommitted). CR = `/home/user/system-3-company` at `e84b8784` (the company's head moved to `42738e6d`, 15:58Z, during this revision; counts are pinned to `e84b8784`, 14:21:02Z, as in the FC). FC = `resources/evaluations/2026-10-17-fact-check-ch11-draft.md` (row and item numbers). FC-CS = `resources/evaluations/2026-10-17-fact-check-company-case-study.md`. Old = old chapter at `6a4912c`. **Nothing here is checked by me.** Rows of the original map not named below are unchanged, except that every "As of 17 October" in them is now covered by the single dating sentence (R2.1).

### §1 (FC corrections only)

| # | Sentence now | Source | Supersedes | Category |
|---|---|---|---|---|
| R1.1 | "Nothing in the lesson itself works until you pick one and lock it in." | `src/kit/Lesson.tsx` 102-110 ("Lock it in"); FC item 9 | 1.3 | described artefact |
| R1.2 | "It also gives the other two towns, which opened once you had tested the full one: at 1 in 100, ten of twenty… at 1 in 10 it is 99 of 108." | `Demo.tsx` 146, 205-230 (`unlocked`, `inReveal`); meta c4, c9; FC item 5 | 1.9 | described artefact |
| R1.3 | "…in a 1978 Harvard study the most common answer to a similar question was 95%." ("about 2%" removed) | `Demo.tsx` 138-141; meta c6; FC item 12 | 1.10 | described artefact |
| R1.4 | "…and a scripted browser test pressed every button." | `tests/qa/contract.spec.ts`; FC item 10 | 1.13 | observed |
| R1.5 | "Every factual sentence the card showed you is written down somewhere with an address." | meta c1-c9 against `Demo.tsx` strings and the recall card; FC item 11 | 1.14 | observed for this lesson |

### §2

| # | Sentence now | Source | Supersedes | Category |
|---|---|---|---|---|
| R2.1 | "The company is mine. I founded System 3 Company on 12 October 2026, and its records call me the founder, so I will too. Every figure here is as it stood on the 17th, when the company was not yet five days old and had about a hundred roles, all of them agents except mine." | 99 roles in `tools/org/roles.mjs`, `founder` the only non-agent (FC rows 40, 45); founder = author: `press/README.md` ("The founder is the author"); founding decision `company/decisions/2026-10-12-company-structure.md` (dated 2026-10-12); first commit 22:51:34Z on 12 Oct (FC row 41); span 4 d 15:29 to `e84b8784` (FC row 42). **X (new)** | — (the single dating device) | observed |
| R2.2 | "It was built to make minutes like that one: a guess, a town, a reason, and the same idea coming back days later as a question." | `company/mission.md` 5-8 ("Days later the idea comes back as a single question"); A1 | — | designed (mission) |
| R2.3 | "The bet worth following… changes what she believes, and that it stays changed. Most of what follows is evidence about something easier." | argued; surface-value items 3-4 ("teaches", "remembered") | — | argued |
| R2.4 | "0.99 × 0.001 over the sum of itself and 0.01 × 0.999, which comes to 0.0902" | meta c3 `source`; FC row 19 | 2.1 (wording) | observed |
| R2.5 | "The other eight cover the rest of the card, from what '99% accurate' means here to the counts on the full town, the Harvard study, the reveal's general sentence and the question that comes back days later." | meta c1, c2, c4-c9; FC item 4 | 2.2 | observed |
| R2.6 | "The lessons marked published carry 3,891 verified claims, and the builder role verified none of them." | FC row 28 (at `e84b8784`) | 2.8 | observed count |
| R2.7 | "…was refused publication because a single claim was still unchecked." | `releases.json` 509, 511, 530; FC item 13 | 2.9 | observed |
| R2.8 | "By the company's own log, the builder that wrote the 9% and the fact-checker that checked it ran on two models from the same vendor." | `events.jsonl` `tx-c048ddb23a` (builder, ledger `model: null`, session model; 10-13 COE "Opus builders"), `tx-ef796c2d40` "Dispatch fact-checker (sonnet)", ledger `L-tx-dd4fbd8241` `"model":"sonnet"`; FC item 1. Model names generalised (brief §5.1, D5). | 2.11 | the company's log (backfilled; its testimony) |
| R2.9 | "What differs is the model, the role file… What they share is a maker. One model family checking itself is still one witness wearing different coats…" | argued; FC item 1's "one family" wording | 2.11 | argued. **Second check** (FC-supplied framing) |
| R2.10 | "Even my own words to the company reach its files through an agent that wrote them down." | FC-CS row 94; throughput record line 5 ("recorded by: chief-of-staff"); Safari record line 8 | replaces the per-quote caveats (5.9, 7.18) | observed pattern. **Second check** (rests on FC's own ruling, FC N rows 74, 128) |
| R2.11 | "Everything else here is the company's account of itself, written by the agents it describes. I say so once, here, rather than at the end of every paragraph." | argued (evidence rule; brief §4.5) | — | argued |
| R2.12 | "And 'verified' deserves what the card did to '99% accurate'… nobody knows either rate." | argued; no record measures a checker's miss rate (EXP-001 not run, FC row 99) | — | argued; the negative rests on A9 |
| R2.13 | "A day later a separate fact-checker session marked both verified, and its record calls itself independent. The first checker had asked for 'a checker other than the fact-checker'. That check is not on record, and the gate passed both claims anyway…" | `company/reviews/base-rates/2026-10-13-fact-check.md` line 3 ("Checker: fact-checker (independent of the 2026-10-12 checker who added c7 and c8)"); `2026-10-12-fact-check.md` line 65; events ·aea2, ·5dad; FC item 2 | 2.13 | observed. Wording is FC's, adapted: **second check** |

### §3

| # | Sentence now | Source | Supersedes | Category |
|---|---|---|---|---|
| R3.1 | Store block, paragraph 1 (two sentences) | Old 11:5 verbatim | 3.1 | the author's own text |
| R3.2 | "The models inside a store's recommendation modules may be very good. The strange part is one layer above them. The page is smart inside the modules and surprisingly dumb between them." + slate sentence [1] | Old 11:15 (trimmed: "even though the models inside those modules may be very good"; "The strange part is one layer above them." verbatim); old 11:67; `ref-11-slate` | 3.1 ("My complaint was simpler" removed) | the author's own text |
| R3.3 | "The design's best idea was about the objective." | Writer's connective (was §7's "The best idea in the store was about the objective"); author to confirm | — | the writer's judgement in the author's voice |
| R3.4 | "The store has legitimate business goals. Customers have goals. They are often aligned and sometimes not, and a system that pretends only one of these matters is hiding politics inside a scalar." | Old 11:191 (merged two sentences) | — | the author's own text |
| R3.5 | "I wanted those trade-offs written into the design, where someone can question them. If margin is part of the objective, admit it." | Old 11:193 (**tense changed** from "I want"; author to confirm), 11:195 verbatim | — | the author's own text |
| R3.6 | "If your ecosystem rewards clicks, clickable organisms evolve." | Old 11:111 verbatim (plants the §7 callback; EGGS F9a) | — | the author's own text |
| R3.7 | "The first test I would run was deliberately boring: one placement, a small number of validated customer problems, a simple composition mechanism and an authored objective before a learned one. It had to beat a strong static page, and it had to beat simplification, because perhaps the best response to an overloaded page is fewer things. The system should have to earn its complexity." | Old 11:201 (**tense changed** from "is"; list trimmed), 11:205 (condensed; last sentence trimmed) | 6.5 (moved here) | the author's own text |
| R3.8 | "System 3 Company is education and the organization doing the building at once. It makes lessons, and agents do almost all of the work." | A2; FC row 40 | 3.2 | observed |
| R3.9 | "The vision written on the first day planned eight subjects and about twenty lessons for the quarter. By the 17th the org data listed 99 roles, and the repository held 1,283 lessons in 14 subjects, from probability to history, 720 of them marked published." | FC rows 45, 46, 47 | 3.4, 3.5, 3.6 | observed |
| R3.10 | "All of these roles run on one vendor's models, through an account with usage limits the company has already hit." | `company/rituals/records/2026-10-13-coe.md` ("The account hit its session usage limit (HTTP 429, resets 03:30 UTC)"); EXP-003 ("under the usage limit"); FC item 26 | 3.9 | observed. **Second check** (FC-supplied wording for an unverifiable row) |
| R3.11 | "Its ledger, which has gaps, records 113.1 million tokens of agents' work by 16 October." | `ledger.jsonl` 992 rows, 948 with tokens, 113,129,260; FC rows 51, 52 | 3.10 | the company's ledger. **Second check** (FC N 52) |

**Moved out of the prose (values kept here):** first commit 22:51:34Z on 12 October; 2,718 commits on the **default** branch (`ccr-4c6c7654-ew9ko1`) by 14:21:02Z on 17 October (FC item 14); 72 roles by the night of the 13th (`progress.md` 2278-2282, a handoff count); "so the real figure is higher" (cut: an inference from 44 null rows and the excluded main session).

### §4

| # | Sentence now | Source | Supersedes | Category |
|---|---|---|---|---|
| R4.1 | "Its principles file takes most of the lines of the Zen of System 3… and gives each a practice and the file where the practice lives." | `company/principles.md`; FC item 6 (31 of 41 by FC's count) | 4.1 | observed |
| R4.2 | "Its decision template has a heading, 'Rests on', and the founding decision rests on three chapters of this book." | `company/decisions/README.md` 15; structure decision 22-23; FC item 16 | 4.2 | observed |
| R4.3 | "…the press is also a company of agents running on the same vendor's models… The witness and the subject come from one family of models all the way down. In that whole chain, the author is the one reader who is not a copy of any of them…" | `press/org/roles.mjs` (`inherit`); company `roles.mjs` (48 `sonnet`, 49 `inherit`); FC item 17 | 4.5 | observed / argued |

### §5

| # | Sentence now | Source | Supersedes | Category |
|---|---|---|---|---|
| R5.1 | "Three warnings came true against the design built to heed them. Two are this book's. The company had written the third down itself, a day before it happened." | Warning 1: Ch5:28 ("The organization was the bug"), 5:174. Warning 2: Ch10:49 ("Its usual failure is that it never comes down"). Warning 3: `company/knowledge/patterns/a-rule-without-a-mechanism-is-a-wish.md` ("New 2026-10-14"; incident 2026-10-15). FC item 27 | 5.0 (intro) | argued; dated |
| R5.2 | "…narrow roles under managers, and by 16 October a map of twenty areas of work, each with a manager." | structure decision (26 narrow roles); `2026-10-16-poc-map-and-dispatch-requests.md` line 16; FC item 7 | 5.1 | designed |
| R5.3 | "That day its own retrospective counted the previous 48 hours… every one of the 223 assignments in the log for that window named it as the sender." | retro 4, 7, 12-13, 47; FC row 64 ("dispatches" translated to "assignments", "actor" to "sender": DE 5.2) | 5.2 | the company's own count |
| R5.4 | "…the coordinator sends work only after asking the manager responsible what to run… had been started without asking…" | founder rule 2 (line 16), lines 35, 41; FC rows 68-69 | 5.5, 5.6 | designed / observed |
| R5.5 | "The fix is written down; whether it works has not been measured." | FC row 70 | (wording) | designed, not measured |
| R5.6 | "Of everything in the records, this result cuts hardest against the book… At the least, that narrows the emergence claim…" | argued; retro 52 ("Gates held while the delegation did not") as the basis for "the parts that held were written as code" | — | argued |
| R5.7 | "The second is the failure the book calls bureaucracy's usual one, that it never comes down." | Ch10:49 | — | the book's text |
| R5.8 | "On 16 October, by its own count, new builds took 8%…" | throughput record 11-17; FC rows 71-72 | 5.7 | the company's own count, not recomputed |
| R5.9 | "Fluent autonomy, as I have described it, forms the institution a request needs and takes it down when the work is done. This one stayed up, and the standing part ate most of the day." | Ch10:39 (definition); throughput record ("the rest is the machine around it"; builds 8%) | — | argued from the company's numbers |
| R5.10 | "…and his complaint is on file: 'What is going on you are working all the day but number of demos did not move'" ("as an agent transcribed it" removed; see R2.10) | throughput record line 8; G | 5.9 | founder's words via an agent. **Second check** (FC N 74) |
| R5.11 | "The hosting service built the commit and put it live." | API statuses for `aefb10a` (12:50:23Z "Deployment has completed"); FC row 78 | 5.12 (wording) | observed (third party) |
| R5.12 | Deploy paragraph 2 ends "That part was luck." | COE 8, 12-13 | 5.13-5.15 | observed |
| R5.13 | "All four are still in the backlog." | `board.json` W-1051..W-1054 `backlog` at `e84b8784` | 5.16 | observed. **Pre-release refresh** |
| R5.14 | "The last of its five whys lands on a person: the chief of staff took the agent's report as truth and did not check the hosting service's records." | COE line 21 ("…did not check Vercel commit statuses after the release manager's commits") | 5.17 | observed. **Second check** (FC N 85) |
| R5.15 | "…and nothing happened, because a push like that no longer creates anything for the word to start." | `vercel.json` `git.deploymentEnabled: false`; `54aa64e3` 0 statuses; F-48 (old branches still deploy on push until they merge); FC item 20 | 5.19 | observed. **Second check** (my wording; the old-branches caveat) |
| R5.16 | "…written from four cases, all found on one day. The catch itself came from checking the disk instead of believing the report. Let the LLM narrate. Do not let it declare reality." | pattern file 1-20; retro 51; old 11:171 (author's heading) | 5.20-5.22 | observed / the author's line |
| R5.17 | "It shows that nothing unchecked was marked published. Lessons still in review are on the site as well, tagged 'In review', by the founder's choice. And it cannot show that 'checked' means more than one model agreeing with another from its own family." | `company/decisions/2026-10-15-founder-show-review.md`; surface-value line 23 (feed order "published first, then lessons in review, labelled as such"); `releases.json` 511, 595; FC item 3 | 5.23 (and FC row 93) | observed / argued. **Second check** (FC-supplied wording) |

**Moved out of the prose (values kept here):** retro's "testimony-grade" label is on its lane-by-lane matrix (line 21; source of "about 99%"); the 223 is in its "measured here" table (line 7); the event log was backfilled afterwards, and today's version of the window holds 372 events, all `chief-of-staff`, 5 with `batch=` (FC-CS correction 7; FC N 67: **second check**); throughput numbers are the company's, not recomputed; the hosting service's commit statuses show the build of `aefb10a` and the other two commits cancelled (FC item 19); `press/books/system-3/experiments/2026-10-company-case-study/deploy-marker/replay.sh` (committed) reruns the old filter against the saved messages and matches the marker in `aefb10a` only: the **filter's** part is run, what the founder was told is recorded (FC N 82: **second check**).

### §6

| # | Sentence now | Source | Supersedes | Category |
|---|---|---|---|---|
| R6.1 | "All of this costs something." | — | (signpost cut) | — |
| R6.2 | "The founding decision says it should be revisited if the cost per published lesson is more than three times a single-agent baseline with no gain in quality." | structure decision 26-28 ("more than 3× a single-agent baseline with no quality gain") | 6.1 | designed |
| R6.3 | "The founding review's first objection, that 26 roles was heavy for 17 lessons, was marked open and funded with the first experiment and a cost comparison. Nobody has run the comparison." | structure decision 33 ("Raised by: founding review"; "open, funded: EXP-001 plus a cost comparison in the first OP"); FC items 21, row 97 | 6.2 | designed, not run. **Pre-release refresh** |
| R6.4 | "When I designed the store, the first test I wanted was deliberately boring, and it had to beat a simpler page." | Old 11:201, 11:205 (callback to R3.7) | 6.5 | the author's position (tense: author to confirm, FC row 100) |
| R6.5 | "By that line, the company is so far branding. Its structure has not yet been put anywhere it could lose, and it stops being branding on the day the dull arrangement is run against it with permission to win." | argued from the A/B line, R6.3 and FC row 99 (no experiment has a result) | — | argued, in the author's voice; **Ask 9 asks him to confirm or replace** |
| R6.6 | "…and the review record says every one was caught. The scripts were never committed and are gone. A new harness, written for this book, reproduced 15 of the 22 exactly and ran them against the company's committed tests. All 15 were caught, each with exactly the failing count the record printed." | readiness record 73-88, 112-128; `press/…/plant/` (`result-2026-10-17.json`); FC rows 103-105 | 6.8-6.10 | testimony in a record; **run** |
| R6.7 | "So the tests can fail. The test this book proposes for its own central claim is a different one… The company adapted it, for a false claim planted in a lesson, as its first experiment, which is one of the eight without a result. The planters and the harness writer were all copies of one model, but the tests are code." | Note on Evidence "A Test Still to Run"; `EXP-001-planted-false-claim.md`; FC item 22, rows 107, 109 | 6.11 | designed, not run / argued |

**Moved out of the prose:** the harness ran at company commit `e84b8784` (the default-branch head at 15:46Z), not at the commit the study feature was approved at (FC-CS correction 6; FC N 106: **second check**). 7 of the 22 bugs could not be reproduced exactly.

### §7

| # | Sentence now | Source | Supersedes | Category |
|---|---|---|---|---|
| R7.1 | "The store's idea about the objective is now a file. In the company it opens a protected document the founder owns: 'If the objective is not written down where someone can argue with it, it enters through invisible overrides.'" | `company/product/surface-value.md` lines 1-5 (verbatim first sentence); `protected-paths.txt` 5 | 7.1 | quotation |
| R7.2 | "…it teaches its point…" | surface-value line 15 ("It teaches the payoff. Borrowed-mind reviewers can name the idea after the reveal…"): the writer's gloss | 7.2 | designed |
| R7.3 | "So the page I once complained was dumb between its modules is now a feed kept dumb between its cards, by a written decision." | `2026-10-12-feed-is-not-personalised.md`; surface-value "For the feed" ("Order is subject round-robin… It is not personalised and it says so"); R3.2 | 7.5 ("Both ideas began in the store" removed) | argued |
| R7.4 | "…quotes one of my store sentences back at me, as its own: 'If our ecosystem rewards clicks, clickable organisms evolve.'" | `mission.md` 24-25; old 11:111; FC item 23 | 7.6 | quotation |
| R7.5 | "the form this book keeps warning about" | Ch6:333; Ch12:55, 219; FC item 8 | — | argued |
| R7.6 | "On 15 October the founder proposed an amendment that would make the feed smarter between its cards, with rule-based personalization, and add one labelled ad slot in the same draft. It is drafted and not ratified." | AMD-008 header (2026-10-15; `proposed_by: founder`; "proposed (draft, not applied)"); "smarter between its cards" is the writer's gloss of rule-based personalization | 7.8 | observed. **Pre-release refresh** |
| R7.7 | "By the company's own pattern, a rule without a mechanism is a wish, and the fair question to put to 'never used to rank' is which of the two it is." | pattern file; surface-value line 19 | — | argued (no claim that a mechanism does or does not exist) |
| R7.8 | "One override of a launch review's ruling is on record." | Safari record; r9 launch record; FC N 122 (the 2026-10-16 behavioural-pilot exemption is from a gate ruling, not a review's) | 7.12 | observed. **Second check** (FC-supplied narrowing) |
| R7.9 | "He answered the release summary with 'Deploy', and on the Safari question he chose the option labelled 'Ship it anyway'." | `2026-10-17-founder-deploy-r9-left-or-right-safari.md` lines 11-12 | 7.16 | founder's words via an agent. **Second check** (FC N 126) |
| R7.10 | "The record states the risk, what would prove the decision wrong and how to revert it, and says the waiver is not a verification and does not carry to any later deploy." | Safari record 17-30 | 7.17 (unchanged; moved after the quote) | observed |
| R7.11 | "Whether that is the system working or the second way things go wrong, where the records keep coming out and the objection stops mattering, depends on what would happen if he was wrong." | interlude lines 17, 21 (argued) | (replaces "That is the system working as designed… I would not soften either half.") | argued |
| R7.12 | "The record names what would show it: a Safari run, which the company's machines cannot do, a check on a real iPhone, or a report from a learner." | Safari record, "What would make this decision wrong" ("A WebKit/iOS Safari failure… found by `c1-check.mjs` with `ENGINE=webkit`, a real iPhone check, or a learner report"); "No WebKit run and no real iPhone check exists"; r9 ruling 2 (e). **X (new)** | — | observed |
| R7.13 | "Nothing is ratified without the founder. A learner can open the sheet and see what any claim rests on." | constitution Art. 3.2; AMD-012 110-112; FC item 24 and row 131 note | 7.19 | designed |

**Moved out of the prose:** "Those words reached the file second-hand: the release manager wrote them down from what the chief of staff relayed." (Safari record line 8; FC N 128: **second check**). The permission comment still says so.

### §8

| # | Sentence now | Source | Supersedes | Category |
|---|---|---|---|---|
| R8.1 | "Then it adds: 'Simulated learners find problems…'" ("to its credit" removed) | `DemoCard.tsx` 130-134 | 8.1 | quotation |
| R8.2 | "It is empty in all 1,283 lessons." | FC row 133 | 8.2 | observed count |
| R8.3 | "The question that was supposed to come back days later has an answer, about 1 in 100: out of 10,000 people, about one sick person tests positive and about a hundred healthy ones do too." | meta `recall.answer: 2` ("About 1 in 100"), `recall.why` ("Out of 10,000 people, about 1 sick person tests positive, but about 100 healthy people do too…"); claim c8. **X (new)** | — | described artefact (the lesson's own answer) |
| R8.4 | "The company has no record of a single person answering it." | FC row 14 (WBRs 10-13 to 10-16: recall "no data"); `humanLearners: []` in all lessons; `progress.ts` keeps revisits on the learner's device. **X (new): check** that no recall data reached any company record by `e84b8784` | — | observed absence |
| R8.5 | "Whether a lesson teaches is the question my first teaching demos left open, and a company of agents has not closed it." | Ch3:11, 3:79 ("putting the thing in front of somebody who does not already understand Merge Sort"); Ch3:321 "Whether the demos teach humans any better is a question only human learners can answer." | — | the book's own text / argued |
| R8.6 | "On the afternoon of the 17th, most of what the company had made since 15 October was not yet on its public site." | `curl` GETs at 15:53:26Z (FC N 139): `/` cached ~2026-10-15 13:24:33Z; four lessons published later 404; deploy run `39042065255` still `in_progress` | 8.8 | observed (third party). **Second check, fresh timestamp**: my narrower wording; a CLI/dashboard deploy is still not ruled out |
| R8.7 | Recap paragraph | **deleted** | 8.9 | — |
| R8.8 | "…when the people it is for have not been given a say?" | argued (constitution: no learner standing, Art. 3, 6.3) | 8.10 area | argued |

## Second-check list (Revision 1)

Sentences that rest on a value or wording the fact-checker supplied, or on the fact-checker's own earlier rulings. Under the role rule, **fact-checker-system-3 may not verify these**: a second fact-checker instance or the experiment developer checks each one against company sources.

| # | FC row | Sentence in the revision | What the second checker confirms |
|---|---|---|---|
| S1 | 52 (N) | "Its ledger, which has gaps, records 113.1 million tokens of agents' work by 16 October." (R3.11) | 948 of 992 rows carry tokens; the main session is excluded; the total and the last row's date. |
| S2 | 67 (N) | (moved out) backfill and 372 events, all `chief-of-staff` | That the moved values in R5's "moved out" note are right, in case the founder wants them back inline. |
| S3 | 74 (N) | "…his complaint is on file: '…'" and R2.10 "Even my own words to the company reach its files through an agent that wrote them down." | The quotation is verbatim at throughput line 8; line 5 "recorded by: chief-of-staff"; the general claim holds for every founder quotation in the chapter (two records). |
| S4 | 82 (N) | (moved out) the replay | "The filter's part is run" is the right category; the replay matches only `aefb10a`. |
| S5 | 85 (N) | "…did not check the hosting service's records." (R5.14) | COE line 21 supports the narrowed wording. |
| S6 | 106 (N) | (moved out) "at `e84b8784`" | The harness ran at that commit, not at the approved state. |
| S7 | 122 (N) | "One override of a launch review's ruling is on record." (R7.8) | No other founder waiver of a **review's** ruling exists by `e84b8784`; the behavioural-pilot exemption is a gate ruling. |
| S8 | 126 (N) | "He answered the release summary with 'Deploy', and on the Safari question he chose the option labelled 'Ship it anyway'." (R7.9) | Sequence and wording against Safari record lines 11-12. |
| S9 | 128 (N) | (moved out) "the release manager wrote them down from what the chief of staff relayed" | Record line 8; the permission comment's wording. |
| S10 | 139 (N) | "On the afternoon of the 17th, most of what the company had made since 15 October was not yet on its public site." (R8.6) | Fresh GETs and deploy-run state; whether any non-GitHub deploy happened. |
| S11 | items 1, 2, 3, 20, 26 (FC fixes) | R2.8-R2.9, R2.13, R5.17, R5.15, R3.10 | FC header: "Every fix in items 1-27 is also mine, so each needs an independent check before use." These five are the ones whose wording I took from the FC rather than from the source alone. |

New X items for the fact-checker (not in any earlier check): R2.1 (founding date as stated), R7.12 (what the record names), R8.3-R8.4 (the recall answer and the absence of recall data).

**Pre-release refresh** (DE 0.3; head of book schedules): R5.13 (four incident actions in the backlog), R6.3 (baseline not run), R6.7 (EXP-001 without a result), R7.6 (amendment not ratified), §8 five-learner test not run, R8.6 (public site). If any of these changes before print, the paragraph that rests on it changes meaning, not just number.

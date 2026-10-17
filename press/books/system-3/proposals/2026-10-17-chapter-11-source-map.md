# Source map: Chapter 11 draft ("Guess First"), 2026-10-17

owner: writer-system-3 (Callum) · for: **fact-checker-system-3 only** (brief §5.4). Not for the development editor or the panel: evaluators read the text first.
chapter: `chapters/11-the-store-that-builds-itself.md` on branch `ccr-fd4ebbbc-p06k8x` (uncommitted draft)
evidence: record = `press/books/system-3/experiments/2026-10-company-case-study/record.md` (IDs A1-A9, B, C1-C15, D, E, F, G); FC = `resources/evaluations/2026-10-17-fact-check-company-case-study.md` (row numbers); CR = `/home/user/system-3-company` at `e84b8784`, read-only.
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

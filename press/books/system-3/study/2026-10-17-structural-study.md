# Structural study: Chapter 11 rewritten around System 3 Company

owner: development-editor-system-3 (Harriet) · date: 2026-10-17 · book: system-3 · scope: Chapter 11 and what it hands to Chapter 12 and the endings
commissioned by: `press/decisions/2026-10-17-founder-store-chapter-rewrite.md` (founder: "ReWrite the store chapter around system 3 company, use the press team, first the team need to study the book and the company then write the chapter")
status: **study, not a brief and not a draft.** Nothing here is accepted. The head of book uses it for the brief; the founder decides the shape and the title.
companions (other roles, same phase): the whole-book study, and the experiment developer's incident-level evidence record. This study does not log incidents one by one; where it cites one, it names the file so the evidence record can check it.

**How I read.** I read the commissioning record first (it names the task), then Chapters 4, 5, 10, 11 and 12 in full, the Part V page, the Afterword, the Note on Evidence, the Zen appendix, the working spine, and skimmed 1–3, 6–9 and the Interlude for their key concepts. I wrote my findings on the chapter before reading the earlier development edits (`resources/evaluations/2026-09-05-developmental-edit.md`, `2026-09-27-arc-parts-edit.md`), which I only searched for Chapter 11 references. I then studied System 3 Company **read-only** (`/home/user/system-3-company`); the only command I ran there was `node tools/company.mjs status`, which reads and prints. Every company number below is as I read it on 2026-10-17. They are **unverified** until the fact-checker re-reads them, and most of them will have changed by the time a draft exists.

**What I may not do, and did not.** I did not edit the manuscript or any file other than this one. I invent no author facts; where the chapter needs a lived scene, memory or number, section 6 asks the founder in writing. Chapter 13 is untouched and is not a subject of any proposal here.

---

## 0. The verdict in one paragraph

A company-centred Chapter 11 can do Part V's job **better** than the store, for one reason: the store was a design that never met a customer, and the company is a running institution that turns the book's architecture toward people who want to learn something. It can also do the job **much worse**. The easy chapter is a guided tour of the book's own machinery ("here is the constitutional surface, here are objections travelling, here are claims with addresses"). That chapter turns Part V back inward just as the book is supposed to turn outward. It duplicates Chapter 5 at a larger scale and proves nothing, because the company was built *from* the book. I recommend a shape that starts and ends with **the learner and the objective** (whose minute is this, and who decides what it is for), uses the organisation as the means, and keeps two store ideas that literally became company files (the honest cold start and Surface Value). The chapter's honest centre is a field that is empty on every lesson: `"humanLearners": []`.

---

## 1. What the old Chapter 11 does for the book, and whether a company chapter can do it

### 1.1 The old chapter's jobs

The spine gives Part V one question: *What is the capacity for?* (Ch 11–12; "The ending I want"). Within that question the store chapter does seven jobs:

1. **The first turn outward.** Chapters 1–10 build an architecture and keep asking whether it can be trusted. Chapter 11 is the first place it serves someone outside the system: Mei, Sami and Lea, customers with a problem. "What is the capacity for" gets its first concrete answer: *to help this person with this problem*.
2. **Applying the architecture to a product.** Its sections apply the book's ideas to a real domain: a problem instead of an item (hypotheses that can fail), composition, the honest cold start, a trace that keeps the losers, Coverage and Unmet Demand, "Let the LLM narrate. Do not let it declare reality", Surface Value, and a deliberately boring first test. "The argument about hallucination from earlier in the book has turned into a product requirement."
3. **The author's lived authority.** "After years working on ranking and recommendations, I built a prototype store." It is the book's most practitioner-voiced chapter, and its evidence status is *Prototyped; the business experiment has not run* (Note on Evidence).
4. **The book catches itself.** "The Book Comes Back to Bite Me": a recommender redesign that acquired "the shape of a scientific institution embedded in the product". This is the reveal page's claim seen from a new domain.
5. **Politics written into the objective.** Surface Value: "A system that pretends only one of these matters is hiding politics inside a scalar." And the final turn: "Mei cannot, yet. Until she can, her interest is something the owner chooses to write in, not something she can enforce." Chapter 12's "who writes the objective, who can see it, who can change it" needs this sentence.
6. **The profession question.** The last paragraph: "More of the work moves into the system, including work I once regarded as the reason it needed someone like me." Chapter 12's "What Are Humans For?" opens on the same anxiety ("LLM-as-a-judge looked like a threat to my profession").
7. **A widening gesture.** "It is hard not to imagine the same thing in research, education or the organization doing the building." Chapter 12 starts from it (Dantzig, the mathematician's workshop, the community, the irrigators).

Two smaller jobs: it is the landing for the store thread Chapter 7 uses as its running example (the store's research agent, its evaluation standards review board), and it carries one proposed seed, the camel ("And now the camel comes back"; `resources/editorial/easter-egg-register.md`).

Job 7 matters: **the old chapter already points at the new one.** "Education" and "the organization doing the building" are the company's two halves. The new chapter can begin where the old one stopped, without pretending the store never existed.

### 1.2 Better, worse, or differently: job by job

| Job | Store chapter | Company chapter | Net |
|---|---|---|---|
| 1. Turn outward | Imagined customers (illustrative). | A real product for real learners. **But there are no real learners yet**: `metrics.md` says "Until B has data, every claim that the company 'works' is about A"; EXP-002 (real-learner recall) is "designed, not run". | **Better if the chapter keeps the learner at the centre. Worse if it describes the org.** |
| 2. Architecture applied to a product | Designed, never run. | Running: claims ledger, gates, constitution, rituals, experiments with committed predictions. | **Better**, much better as evidence. The risk is recapping the book (R1). |
| 3. Lived authority | Ranking-systems career, prototype. | The founder built and runs it. His words to the company exist on disk (e.g. "We started all of this to test System 3 book ideas", `company/sibling/system3-meta/founder-brief.md` §1), but quoting them in the book is an **open objection** in the commission. The lived scenes are not on disk (section 6). | **Same or better, but only if the author supplies the scenes.** |
| 4. The book catches itself | A design that turned out to look like science. | A company *designed from* the book, so finding the book in it proves nothing (R4). The real "comes back to bite me" is what the design did not predict: the coordinator became the hub, checking ate the budget, and its rules turned out to be wishes. | **Different**: the bite has to come from failures, not resemblance. |
| 5. Politics in the objective | Surface Value as a thought. | Surface Value as a **protected file the founder owns** (`company/product/surface-value.md`), plus a pending amendment that adds ads, rule-based personalisation and mastery as typed constraints with tests (`company/constitution/amendments/AMD-008-first-light-surface-value.md`). The learner can see what a lesson rests on (Constitution Art. 6.3) and cannot contest the objective. | **Better**: the store's argument becomes a working artefact, and Mei's missing standing is still true. |
| 6. Profession | An applied scientist whose job moves into the system. | A founder who is chief executive of about a hundred agent roles, whose own chief of staff (an agent) chose about 99% of specialists' work in a 48-hour window (`company/rituals/records/2026-10-16-retro-delegation.md`). | **Sharper**, if the author is willing to say what it did to him (section 6). |
| 7. Widening | Gesture toward research, education, organisations. | Already widening: a press (this one) and a parked "System 3 Meta" to generate companies for others ("the harness is the product"). | **Risky.** It is tempting to do Chapter 12's job early. Hand it over instead (section 5). |

### 1.3 Structural risks, named

- **R1. The museum tour.** The concept map in section 3 is a list of everything the chapter *could* show. Organised around it, the chapter becomes a retrospective of Chapters 3–10 with file paths, ten sections each saying "and here is that idea, running". Part pages "turn toward the next part; they do not recap the last one" (spine). The same rule should bind this chapter. **Pick at most three mechanisms to show at work, and let the rest go unmentioned.**
- **R2. Chapter 5, again, bigger.** Chapter 5 is the society of agents: harness repairs, progress files, specialists, independent witnesses, "the organization was the bug". A company of a hundred narrow roles is the same subject at a larger scale. If the new chapter's question is *how do agents organise*, it is a sequel to Chapter 5 in the wrong part. Its question has to be *what is this organisation for, and for whom*. The organisational material it does use should be what Chapter 5 could not have: an objective, a customer, an owner, money (ads), a launch.
- **R3. Chapter 10's "Where This Could Be Wrong", again.** The company's honest limits (one model in many roles, the coordinator as hub, no real learners) are the same three objections Chapter 10 already concedes for the book. Restating them is not enough. The chapter has to show what *happened* when the objections met a running organisation, with numbers.
- **R4. Circularity.** The company was built from the book (`company/principles.md` maps every Zen line to a file; decisions cite chapters in "Rests on"). Resemblance is therefore not evidence. The Afterword already says so: "Resemblance to a scientific institution establishes nothing by itself." Only three kinds of material count: what the design did not predict, what failed, and what was tested against a simpler arrangement. Most of the material does not count.
- **R5. Self-regard.** The book designed a company; the company founded a press; the press writes the chapter about the company. A reader can tolerate one turn of this recursion, named once, plainly, inside the honest limits ("the witness and the subject share a model", commission objection 2). More than that and Part V becomes a hall of mirrors. The book's last page is about scaffolds for *ourselves*. The chapter must not end on the machine admiring itself.
- **R6. A moving target.** The company is six days old (first decisions dated 2026-10-12). In four days its new-lesson count went from 852 to 10 (`company/decisions/2026-10-16-founder-throughput-for-10k.md`). Its role count went from 26 to about a hundred. Any number in prose will be stale at print. The chapter should date its numbers ("on 17 October…") and rest its argument on mechanisms and events, not totals.
- **R7. Losing lived material.** The store chapter is the author's practitioner voice and carries an AUTHOR comment asking for a prototype moment. Dropping it entirely loses the only place the ranking career meets the argument head-on (commission objection 3, open for the founder).
- **R8. Register.** Company records are written in W-numbers, AMD-numbers, lanes, POCs, slots and gates. The draft must translate. A reader should never meet a board id.
- **R9. Publishing internals and employers.** Founder's words to the company, service names, Amazon and Zalando (commission objection 4; `resources/REVISIT.md` clearance row).

### 1.4 What the new chapter has to do (proposed definition of done, for the head of book's brief)

1. Answer Part V's question from the **learner's side** at least once, in a scene.
2. Show **one or two mechanisms** at work on one artefact a reader can follow (one lesson, one claim, one decision), not a survey.
3. Put the **objective and its owner** on the table: Surface Value, the pressures on it (ads, personalisation, the 10,000-lesson target), and the learner's lack of standing.
4. Report at least one thing the **design did not predict**, with a number.
5. State the honest limits **inside the chapter**: one model in many roles; the coordinator as hub; no real learners; the press shares the model. This is required by the commission.
6. Hand Chapter 12 three things (section 5) without doing Chapter 12's work.
7. Carry an evidence label the Note on Evidence can state truthfully (proposal in section 5).

---

## 2. Three candidate shapes

Length for all three: about 4,500–5,500 words (the old chapter is 4,523; Chapter 12 is 6,635). Headings are working headings in the book's style, not proposals for final wording.

### Shape A: "The Store, Built Somewhere Else" (continuity)

**Spine.** I designed a store that builds itself and never ran the business experiment. Then I built something else from the same ideas, and some of the store's ideas are now files a company obeys. The chapter follows the store's concepts into the company and reports what survived contact with a running organisation.

**Sections.**
1. *I Still Have Not Run the Business Experiment.* The store in a page: Mei, Sami, Lea, problem over item, Surface Value. Compressed from the old chapter.
2. *From Customers to Learners.* The problem over the item becomes the **misconception** over the topic: every lesson's `meta.json` names `misconception`, `knows`, `doesNotKnow`. Sami's "insight experience gets no click" becomes a lesson whose success is recall days later.
3. *The Honest Cold Start, Shipped.* `company/decisions/2026-10-12-feed-is-not-personalised.md` ("Personalisation language without signal is a lie with good typography"; "Fresh picks", not "For you"). Its "Rests on" line cites *System 3, Ch. 11 ("The Honest Cold Start")*.
4. *Coverage and Unmet Demand, as a Command.* `npm run company -- coverage`; "Unmet demand is the roadmap's raw material" (`company/domains/README.md`).
5. *Surface Value Gets a Constitution.* The protected file; AMD-008's typed limits on ads and personalisation; "If merchandising needs a lock, make it a typed constraint" from the old chapter, made real.
6. *Deliberately Not Boring.* The old chapter's own advice was one placement and a small number of validated problems. The company did the opposite: 14 domains and 1,283 lessons before one real learner. What that cost.
7. *Mei Has Not Arrived.* The learner still cannot argue with Surface Value.

**Opening scene.** The decision record above, whose basis is a chapter that this rewrite will replace: a company decision resting on a claim whose address is about to move (Chapter 6's "Give the Claim an Address"). Clever, perhaps too clever.

**Closing turn.** Same as the old chapter's ("Mei cannot, yet"), now true of a real company.

**Trade-offs.** + Keeps the title, the lived store voice, Mei/Sami/Lea, the camel seed's location and Chapter 12's "Chapter 11's store" reference. Addresses commission objection 3. + The two strongest store ideas (cold start, Surface Value) really did become company files. − The store's core machinery (composition, the composer, slate optimisation, replayable traces with losers) has **no counterpart** in the company: the feed is round-robin, not composed (Surface Value: "It is not personalised and it says so"). Section 2's mapping from customers to learners would be forced. − Half the chapter is still about a store that does not exist. − The opening is recursive (R5).

### Shape B: "One Minute, One Learner" (outward; recommended)

**Spine.** What is the capacity for? Here is one answer, sixty seconds long: a person on a phone guesses, plays with a small world that answers back, and is told why. Behind that minute is a company of agents built from this book. The chapter goes from the minute to the machinery and back to the person, and ends on the fact that no person has yet been asked whether the minute worked.

**Sections.**
1. *Guess First.* The reader takes a lesson on the page. The candidate is `src/demos/probability/base-rates` ("You tested positive. Now what?" / "The test is 99% accurate. So you're 99% likely to be sick. Right?"). The reader commits to a guess before the answer, as the product requires, and the reveal comes from the counts: about 1 of 11 positives is sick. This echoes Chapter 4's seven claims, so the writer must not explain the echo.
2. *Nine Claims Behind One Minute.* Every sentence the reader just saw is a claim with an address, support, a source and a checker (`meta.json`, claims c1–c9; the "Why trust this?" sheet). One claim followed end to end. Chapter 4's trust chain and Chapter 6's address appear here as a working object, with no recap.
3. *A Company in a Week.* How it came to exist and why lessons (author asks 1–3). Scale, dated: founded 12 October, about a hundred roles, hundreds of lessons. Chapter 3's Merge Sort demos grown into a standard ("Splitting looks like extra work. It isn't."; `company/product/demo-standard.md`). The preface's "You could begin something that once required the power to assemble an institution" pays off here without being quoted back.
4. *Built From the Book* (short, about 400 words). What was designed in on day one, and the circularity warning: finding the book here proves nothing, only surprises count. This is the one place the recursion with the press is named.
5. *Gates Held, Delegation Didn't.* Three surprises with numbers: the chief of staff chose about 99% of specialists' work; building was 8% of a day's tokens and the machine around it 92% (Chapter 7's store research agent, which "spends more of its budget verifying its own procedure than running experiments", came true); rules turned out to be wishes until they had mechanisms. The founder's "reaching 10k would be impossible" (quotation needs acceptance). Gates held: "Nothing unverified was published."
6. *The Objective Fights Back, Again.* The store thread, carried here: Surface Value is a protected file; engagement "never" ranks lessons; then First Light brings ads, personalisation, accounts and a 10,000-lesson target, each admitted as a typed constraint with a test. The vertical feed is the form Chapter 12 calls "the vortex with a reward function", chosen on purpose. Who can argue with the objective? The founder. The learner can open the sources sheet; she cannot amend the file.
7. *The Student Has Not Been Asked.* `"humanLearners": []` on the lesson the reader just took. EXP-002 designed, not run. Simulated learners "find problems; only people can show that a lesson teaches" (`company/mission.md`). Either the first real learner session (an author scene, if it happens before the draft closes) or its honest absence. Turn to Chapter 12: a system built to teach as well as to answer, and who gets the minute.

**Opening scene.** The reader, guessing. No company, no agents, no author yet. The first two pages are the product.

**Closing turn.** From "the student has not been asked" to Chapter 12's question: capacity for whom, decided by whom. If the founder runs real-learner sessions before the draft closes, the chapter ends on one person's guess, recorded verbatim, which no simulation predicted. That is contact with reality, the book's own test. If not, it ends on the empty field, and the honesty is the point.

**Trade-offs.** + The only shape that answers Part V from the learner's side; it opens outside the machine and ends outside it. + Uses one artefact the reader has touched, which keeps R1 (the museum tour) in check. + The base-rates lesson is itself about trusting a test, which fits the book. + The store survives as section 6, where it is strongest. − Leans on one lesson; it could read as product marketing unless section 5 bites hard. − The reader-quiz device repeats Chapter 4's camel opening (a feature if handled lightly, a tic if not). − Lessons are illustrated poorly in print: a static figure of an interactive card needs the art director, and the print and PDF builds need the figure (`book-design/`). − Its ending depends on something that may not exist yet (real learners). − Drops most of the old chapter's machinery (composition, traces with losers, LLM narration), so commission objection 3 must be answered explicitly.

### Shape C: "A Company Built From the Book" (the audit)

**Spine.** I built the book's architecture as a company to see whether it survives contact. The chapter is an experiment report: what held, what broke, what has not been tested.

**Sections.**
1. *The Wager.* Why the founder built it ("We started all of this to test System 3 book ideas…", needs acceptance; author ask 1).
2. *Twenty-Six Roles for Seventeen Lessons.* The founding decision and its first objection, still on the record: "26 roles is heavy for 17 lessons; coordination may cost more than it saves" (`company/decisions/2026-10-12-company-structure.md`), open and funded.
3. *Five Days.* The scale, dated.
4. *What the Design Did Not Predict.* Hub, shared host, rules as wishes, the event log going quiet.
5. *The Machine Around the Lesson.* The 8% figure; gates by risk class (Chapter 10's "Not every request deserves the same amount of me").
6. *One Witness in a Hundred Coats.* One model in many roles; EXP-001 (the Note on Evidence's own test, adopted by the company) designed, not run.
7. *What It Is For.* The learners, briefly, at the end.

**Opening scene.** The founding objection in the record.

**Closing turn.** Toward the learner, late.

**Trade-offs.** + The strongest evidence; the most honest; gives the book its first observations of the architecture at organisation scale. + Directly answers the VP's discipline (evidence before prose). − It turns Part V inward. The learner arrives in the last section, which is R1 and R2 together. − It duplicates Chapter 5's subject and Chapter 10's self-criticism. − It depends most on the evidence record, which is not written yet. **Its material is better placed where the VP first proposed it**: a Chapter 5 passage or an appendix ("serves Chapter 5 first", `press/decisions/2026-10-16-vp-books-company-case-study.md`). Shape B section 5 can carry a compressed version.

### Recommendation

**Shape B**, with three conditions:

1. **Carry two store ideas, not the store.** The honest cold start (in section 2 or 6) and Surface Value (section 6) both became company files. They let the chapter say truthfully that the store design left the page, and they answer commission objection 3 in part. Composition, the composer, slate optimisation and the trace with losers go. Lea, the no-history visitor, survives most naturally, because she is exactly who the company's "Fresh picks, not For you" decision is for. Mei and Sami can stay as illustrative learners only if the founder wants them. Mapping a shopper stuck between two shoes onto a learner stuck between two predictions is possible but forced.
2. **Give Shape C's material a home outside the chapter.** Compress it to section 5 here, and let the VP's evidence-record route place the rest (a Chapter 5 passage or an appendix). That keeps Part V outward and still lets the book use the evidence.
3. **Ask the founder to get one real learner before the draft closes.** The single strongest improvement to any shape is EXP-002 run even partly: five adults, think-aloud, recall three days later (`company/experiments/EXP-002-real-learner-recall.md`). It is the company's own experiment, owned by the founder, and already designed. I am not asking the press to run it (not our company, not our role). I am telling the founder that the chapter's ending depends on it, and that Chapter 3 has been saying "The student has not yet been asked" since page one of Part I.

**Does the store survive as a thread?** Yes, as above: two ideas and possibly Lea. Read literally, "the store that builds itself" is now a catalog that grows from its own gaps (Coverage, Unmet Demand). That is true, but the chapter should not lean on it: the company is not a store (it is free; ads are pending), and it does not build itself (section 4, S2).

### Title options (the founder decides)

| Title | For | Against |
|---|---|---|
| **The Store That Builds Itself** (keep; new subtitle, e.g. *A Company Built From This Book*) | No production churn: `book-design/curated/book-order.json`, `provenance.json`, `prompts/notebooklm/`, `check-eggs.sh` and Chapter 12's reference all stay valid. The old chapter's concession ("Taken literally, the title overstates it") can now be tested, and the chapter can show exactly how far it overstates. | It is not a store, and it does not build itself (the coordinator chose 99% of the work; the founder approves every deploy). It invites the reader to look for a store that is not there. |
| **First Light** | The company's own name for its first public release (launch planned 2026-11-30). In astronomy, *first light* is the first time a new instrument sees the real sky, which fits Chapter 5's telescopes and Chapter 12's evening of astronomy with the author's children. It promises contact with reality. | Uses an internal code name (internals objection). If the book ships before launch, or the launch slips, the title promises an event the chapter cannot report. |
| **Guess First** | The product's whole philosophy in two words ("Sixty seconds. One idea. Guess first.", company README), and the forcing function from Chapter 9. Outward-facing. | Reads as a product slogan; says nothing about the company. |
| **Sixty Seconds** | Plain; names the unit of capacity the chapter is about. | Flat. |
| **What the Minute Is For** | States Part V's question in the chapter's own unit. | Too on the nose; echoes the part title. |

My lean: **First Light** if the chapter can report at least one real learner; otherwise **Guess First**. Keep the old title only if the founder wants continuity more than accuracy.

---

## 3. Concept map: book concept → company mechanism → what the chapter can show

"Show" means what a reader could see on one artefact. Rows marked ◆ are the ones I would let into the chapter under Shape B; the rest are context for the writer and the fact-checker. The R1 rule applies: a row is not a section.

| Book concept (where defined) | Company mechanism (path) | What the chapter can show |
|---|---|---|
| ◆ Trust chain; a claim carrying its provenance (Ch 4, "A Hallucination With Better Retention") and the claim address (Ch 6, "Give the Claim an Address") | Each lesson's `meta.json` claims: `support`, `source`, `status`, `checkedBy`, `checkedOn`; the learner-facing "Why trust this?" sheet (`src/components/DemoCard.tsx`); `npm run company -- claims` | One sentence the reader just saw, followed to its derivation and checker (base-rates c3: "about a 9% chance", Bayes worked in the source field). |
| ◆ Checking is the bottleneck once cognition is cheap (Afterword, Thesis 1) | `company status` on 2026-10-17: 4,935 claims awaiting the fact-checker; PR #6 merged 200 algorithm lessons with 4,407 claims, all unverified (`company/ops/progress.md`, 2026-10-16 entry); `metrics.md` names the metric "Thesis 1: checking is the bottleneck" | Production outrunning checking, dated: the thesis observed (not tested) in a running organisation. |
| ◆ Predict before you see; scaffold, don't substitute; the annoying tutor and forcing functions (Ch 9, "A Human Is Not a Context Window": Bastani, Buçinca) | `src/kit/Lesson.tsx` (protected: "the predict-before-reveal contract"); `product/demo-standard.md` ("Commit before anything moves"); constitution Art. 2 | The product *is* Chapter 9's annoying tutor, enforced by a protected file and a test. |
| Spaced retrieval (Ch 9, Ebbinghaus; spacing and testing) | `recall` in each `meta.json`; revisits in the feed (`src/kit/progress.ts`); Surface Value #4 "first spaced-revisit recall rate… real learners only" | The company's learning metric is the book's science of memory, and it has no data yet. |
| ◆ "The student has not yet been asked" (Ch 3, "Independent Evaluators"); simulated evidence quietly replacing the expensive kind | `"humanLearners": []` on base-rates; EXP-002 "designed, not run"; pattern `knowledge/patterns/simulated-learners-find-problems.md` (confidence empty; "16 of 17 learner reviews on file use the same adult-beginner boundary") | The chapter's honest centre. |
| Borrowed mind with a knowledge boundary (Ch 3, "Borrow a Mind") | `learner.knows` / `doesNotKnow` / `misconception` in `meta.json`; learner-evaluator role; walkthroughs (`npm run walkthrough`) | Chapter 3's move turned into a data field. |
| Teach the payoff; "no bars" as a strategic constraint (Ch 3, "Bars Moved Around", "Keeping More Than One Idea Alive") | `demo-standard.md` craft rules ("Teach the payoff, not the procedure… The early Merge Sort demos…"; "Remove the easy path… ban bars"); patterns `teach-the-payoff`, `remove-the-easy-path` | Chapter 3's private lessons became a company's standard. One sentence is enough. |
| Independent evaluators; artifact before account (Ch 3; Ch 5, "A Swarm Should Not Automatically Become a Meeting") | `company/reviews/README.md` (protected independence rules); CLAUDE.md "Evaluators see the artifact before the account"; pattern `artifact-before-account` | Independence of *context* built in; independence of *mind* absent (S1). |
| ◆ Five judges sharing one source are one witness (Zen; Ch 5 Condorcet; Afterword Thesis 1; the Note's "A Test Still to Run") | EXP-001 "Does our review process catch a planted false claim?", which adapts the Note's protocol and is "designed, not run"; the founding decision's objection "Several roles share one model, so 'independence' is partly theatre", accepted in part | The book's own unrun test, adopted by the company and still unrun. Reported straight, this is one of the chapter's most credible sentences. |
| Deep Mode orchestrator choosing the next move (Ch 3, "Deep Mode") | Chief of staff and the operating loop (`company/ops/operating-loop.md`; `/run`) | The orchestrator worked, and it became the hub (S2). |
| ◆ Repairs, not design; the harness grows around failures; progress files for workers who arrive knowing nothing (Ch 5, Carlini) | CLAUDE.md "The disk is the memory"; `company/ops/progress.md` ("testimony from a worker who no longer exists: check what you rely on"); COEs ending in mechanisms | Chapter 5's harness, inherited on day one, then repaired by its own failures. |
| Mechanism, not "be more careful" (Ch 5, "Strangers Need Standards"; Ch 7, Correction of Error) | `rituals/templates/coe.md`; the COEs in `company/rituals/records/`; pattern `a-rule-without-a-mechanism-is-a-wish.md` ("Founder-approval rule for deploys: a sentence in CLAUDE.md… enforced by nothing") | The company found that its own rules were wishes. Strong material for "the design did not predict". |
| Specialisation (Ch 5, "The Society Gets Smarter by Making People Narrower") | About a hundred roles generated from `tools/org/roles.mjs`; 26 at founding (`org-chart.md`) | The org as data, and how fast it grew. |
| Compute allocation is epistemic policy; keep part of the budget away from the leader (Ch 5, "Who Gets the Next Agent?") | Constitution Art. 5 (20% exploration, never the leading format); `rituals/records/2026-10-12-creative-distrust.md` notes the exploration-bets table was empty | A rule written, then barely used. |
| Patterns with scope, confidence, `would_be_wrong_if` (Ch 6) | `company/knowledge/patterns/*.md` (YAML in the book's own schema) | Direct inheritance; no need to show it. |
| Objections travel with decisions; "noted" (Ch 6, "Noted") | `## Objections` table in every decision; CLAUDE.md "Never answer one with 'noted'" | Direct inheritance. One real objection could carry a scene (founding: "26 roles is heavy for 17 lessons"). |
| ◆ Constitutional surface; the judged do not amend the judge; an evaluation standards review board (Ch 7, "A Constitution for Improvement") | `company/constitution/constitution.md`; `protected-paths.txt`, enforced by a hook and CI; Constitutional Review Board; amendments AMD-000…012 | Chapter 7's illustrative store board now exists. The writer should show one amendment in motion (AMD-008), not the system. |
| ◆ Checks accumulate until the agent "spends more of its budget verifying its own procedure than running experiments" (Ch 7, "The Complexity Wall", the store's research agent) | `decisions/2026-10-16-founder-throughput-for-10k.md`: "new builds 8%… Building costs about 146k per new lesson; the rest is the machine around it"; new lessons 852 (10-13/14) vs 10 (10-15/16); proposed fix "gates by risk class" | A prediction the book made about an illustrative store came true in a real company within four days. This may be the chapter's best surprise. |
| The human moves to the top loop (Ch 8, "The Top Loop") | Founder gates on irreversible acts (deploys, new roles, spend: `decisions/2026-10-14-deploy-needs-founder-approval.md`, `2026-10-16-founder-org-and-dispatch-rule.md`); `ops/founder-inbox.json` | The top loop is one person, and it is crowded. |
| Two routes for an objection to lose its consequence (Interlude) | Constitution Art. 4.1: "The founder may override a gate in writing"; First Light's quality no-go "only the founder can [overrule], in writing" | The owner holds the override. The chapter must say so plainly (S7). |
| Desire forms on the way; effectuation; "Nobody Wanted AWS in 1995" (Ch 9) | The company began "to test System 3 book ideas" and now plans accounts, ads, 10,000 lessons and a sibling to generate companies for others: "the harness is the product" (`sibling/system3-meta/founder-brief.md` §0) | The machinery built to run the store became the thing to sell, as at Amazon. **Hand to Ch 12 or leave alone**: it is a large idea for one paragraph. |
| Fluent autonomy: form the institution a request needs and take it down; bureaucracy that never comes down; "Not every request deserves the same amount of me" (Ch 10) | The opposite: a standing institution that grew; "Distillation Day" exists as a ritual; the gates-by-risk-class proposal | The company is pre-distillation scaffolding. State it, and do not explain the Scaffolds page. |
| ◆ Surface Value; typed constraints, not invisible overrides; "hiding politics inside a scalar" (old Ch 11) | `company/product/surface-value.md` (protected, founder-owned, v1); AMD-008 (proposed: "Engagement… and revenue are reported… and **never** used to rank lessons"; ads capped at 1 in 6, contextual, never inside a lesson) | The store idea that survived most completely. Section 6 of Shape B. |
| ◆ The honest cold start (old Ch 11) | `decisions/2026-10-12-feed-is-not-personalised.md` (rests on Ch 11); mission "Pretend personalisation… ('Fresh picks', not 'For you')" | Lea's section, shipped. |
| Coverage and Unmet Demand (old Ch 11) | `npm run company -- coverage`; `domains/README.md` | The roadmap emerges from gaps: true, and secondary. |
| "If your ecosystem rewards clicks, clickable organisms evolve" (old Ch 11, "Sami Does Not Need a Click") | Quoted in `company/mission.md` ("What we refuse to make") | The old chapter's line is now the company's refusal. |
| A deliberately boring first test; a simpler baseline allowed to win (old Ch 11; Part V epigraph) | Contradicted in scope (14 domains, 1,283 lessons before one learner); honoured in method (`experiments/README.md`, "a simpler baseline that is allowed to win"; launch predictions EXP-006…008) | The company broke its author's own advice, in a way the chapter can admit. |
| Capacity over power; bespoke comes back; "mentally hiring the people it would require" (Ch 12) | One founder and about a hundred agent roles in under a week; System 3 Meta's "Someone else runs one" | **Hand to Ch 12.** The new Ch 11 shows the instance; Ch 12 asks who else gets it. |
| Who owns the laboratory; rented capacity can be recalled (Ch 12) | The company runs on one vendor's model; the founder brief lists "decouple from Claude" | **Hand to Ch 12.** |
| ◆ The understanding condition: build it "to teach as well as to answer" (Ch 12, "Beyond Comprehension"; Afterword Thesis 2, "Compare systems built to teach with systems built only to deliver results") | Mission: "Leave people better able to ask the next question than we found them" | The company is a bet on Thesis 2's preferred side, and it is unmeasured. This is the bridge to Ch 12. |
| The Zen as practice | `company/principles.md` (every Zen line → a practice → a file) | Evidence of design-from-book (R4), not of the book's truth. Do not show it. |

---

## 4. Where the company contradicts or strains the book

A chapter that only confirms the book is weaker, and with a company built from the book, confirmation is nearly worthless (R4). Each strain below says what it does to the book's argument and what the chapter should do with it.

**S1. One model in many roles.** The book: "Five judges sharing one source are one witness"; independence "has to be built". The company: independent *contexts*, one model. Its own records say so ("independence of context is real, independence of mind is not", founder brief §3; founding objection "partly theatre", accepted in part). A small sharper case for the evidence record to check: in base-rates, claims c7 and c8 say "Added by fact-checker… needs an independent check" and are then marked verified with `checkedBy: "fact-checker"`. The CLI gate refuses only a *builder* verifying its own claim (`tools/company.mjs`, `launchGates`). Independence is enforced at the level of a role's name, and the record cannot show whether the second check came from a different instance. *What it does to the book:* it confirms the book's warning and shows how easily a company built to heed the warning still falls under it. *Chapter:* say it in the limits paragraph. Do not dramatise it as a scandal; it is the book's predicted failure, found.

**S2. The coordinator as hub.** Chapter 5's Carlini harness had "no orchestrator"; Chapter 3's Deep Mode had one that chose moves; Chapter 10 wants an institution that forms itself. In the company, "In 48 hours the chief of staff chose about 99% of the specialists' work… The org chart says 20 lanes; in practice there was one dispatcher who asked managers questions" (`rituals/records/2026-10-16-retro-delegation.md`). 95% of 730 commits were authored as "Claude", not as a role. *What it does to the book:* it strains "emergence over design" and the society-of-agents picture, because a hundred roles collapsed into one decider plus specialists. It also supports Chapter 5's "The organization was the bug". *Chapter:* this is the best "the design did not predict" material. Report the founder's fix (managers decide each lane's work, `decisions/2026-10-16-founder-org-and-dispatch-rule.md`) as designed and unmeasured.

**S3. No real learners.** The whole Part V question rests on people, and the company has none on record. Every learning claim is simulated (`metrics.md` B-table "needs deployed traffic"; EXP-002 not run). Nine production releases exist (r1–r9, `company/ops/releases.json`), so a public site exists, but no human-learner evidence is attached to any lesson I read. *What it does to the book:* it is Chapter 3's warning made into a company, and it means the Note on Evidence must not call the chapter's subject "run" in any sense about learning. *Chapter:* the ending (Shape B section 7).

**S4. Built from the book, so it cannot confirm the book (circularity).** Chapter 10 already concedes "the chance that I found what I was looking for". The company is the extreme case: decisions cite chapters in "Rests on"; `principles.md` maps every Zen line to a file. *Chapter:* one explicit paragraph, and a discipline for the whole draft: report only surprises, failures and tests.

**S5. Designed on day one, not emergent.** The spine says "emergence over design" and "the larger arrangement develops through attempts, failures and repairs". The company began as a 26-role design generated from a file and then grew to about a hundred roles by founder decision and repair. *What it does to the book:* it complicates the theme without refuting it. The parts were designed; what the design did *not* foresee (S2, S6, the rules-as-wishes COEs) is where emergence shows. *Chapter:* make that distinction once; the reveal page already licenses it ("The parts are deliberately built, but attempts to make them work together keep exposing the same needs").

**S6. Gates as bureaucracy; the machine eats the work.** Chapter 10: bureaucracy's "usual failure is that it never comes down"; Chapter 7: the store agent's checks multiply until verifying the procedure costs more than the experiments. The company in four days: building 8% of one day's tokens; "manager rounds became the production line"; "about 48% of fact-check work re-verified claims reset the same day"; board backlog 843 items. The founder: "What is going on you are working all the day but number of demos did not move" (quotation needs acceptance). *What it does to the book:* it confirms a prediction the book made only as an illustration, and it is uncomfortable for the architecture's cost claims (the Afterword: "Each proposal should beat a simpler arrangement on the same model and budget, or be dropped"). No such comparison has run; the founding decision's own revisit condition ("cost per published lesson is more than 3× a single-agent baseline with no quality gain") is unmeasured. *Chapter:* include it. It is the strongest honest number available. Pair it with the counter-fact the company itself recorded: "Gates held while the delegation did not. Nothing unverified was published."

**S7. The owner holds every override.** The Interlude names two routes by which an objection loses its consequence: the system overrules the check, or the owner prevents the challenge. The constitution lets the founder override any gate in writing (Art. 4.1). The First Light quality no-go can be overruled "only [by] the founder, in writing, with the objection recorded". This is legitimate and recorded, which is the book's own standard of visibility. It is still the owner holding the switch, and the learner holds none. *Chapter:* it belongs in section 6, beside Surface Value: "Knowing what works does not settle who gets to decide." Do not soften it. It is the bridge to Chapter 12's "Who Owns the Laboratory".

**S8. The feed form, ads and a volume target versus the book's critique.** Chapter 12 calls an engagement-ranked feed "the vortex with a reward function" and fears "fourteen hours of personalized short video". The company chose a vertical swipe feed on purpose ("a delivery format people already know how to use… we are not in the attention business", `mission.md`), plans an ad slot and rule-based personalisation (AMD-008, proposed), and its founder set a 10,000-lesson target. Each is constrained in writing, and that is the old Chapter 11's own prescription ("If margin is part of the objective, admit it"). *What it does to the book:* this is the live test of whether writing the objective down is enough. The book does not yet know, and neither does the company. *Chapter:* make it section 6's tension and leave it open. Do not resolve it for the founder. Why ads, why 10,000, and why a feed are author asks (section 6).

**S9. Breadth before the boring test.** The old chapter: one placement, few validated problems, a simple mechanism, then compare against simplification. The company: 14 domains (math to history), 1,283 lessons, several new surfaces planned, and no human test. *What it does to the book:* it contradicts the author's own published advice, and that is useful because the author can say so. *Chapter:* one honest paragraph, ideally in the author's voice (author ask 8).

**S10. Not fluent.** Chapter 10's fluent autonomy is an institution formed per request and taken down. The company is a permanent institution with VPs, floors, rooms, rituals and a review board; it imports corporate forms (WBR, operational planning, COE, single-threaded owners) that Chapter 10 says agents may not need ("A swarm should not automatically become a meeting, and it should certainly not acquire a tenure committee"). *What it does to the book:* it strains Chapter 10 unless the chapter frames the company as scaffolding before distillation, which the company's own "Distillation Day" ritual and gates-by-risk-class proposal half admit. *Chapter:* one sentence of framing. The Scaffolds page will do the rest, and the writer must not explain it (egg-register rule 2).

**S11. Shared host, shared failures.** Agents swept each other's staged files into commits, killed their own shells, filled the disk, replaced `/dev/null` (founder brief §3; COEs 2026-10-14 and 2026-10-16). The press's own runs share that host and its caps (press README objection 1). *Chapter:* at most one vivid incident, chosen with the evidence record. Isolation "must be designed in, not left to briefs" is Chapter 5's containers point, now with a cost attached.

**S12. The witness shares the model (this study included).** The press reading the company is one model reading another's records; my findings here are that too. *Chapter:* the commission requires this to be said in the chapter's honest limits. The founder's own reading is the only witness from outside the model.

---

## 5. Hand-offs to Chapter 12 and the endings, and every sentence that would become false or orphaned

### 5.1 What Chapter 12 (After Capacity) needs to inherit from the new Chapter 11

1. **A real instance of the capacity, so Chapter 12 can stop imagining part of it.** Chapter 12's "Bespoke Comes Back" ("mentally hiring the people it would require") and "The Door After System 3" (a weekend and a hundred agents) were written as pictures. After the new Chapter 11 the reader knows the author ran about a hundred agent roles for a week. Chapter 12 has to acknowledge that, or it reads as coy. The new Chapter 11 should *show* the instance and leave the generalisation ("who else gets this?") to Chapter 12.
2. **The objective's owner, and the learner's missing standing.** The old Chapter 11's last turn ("Mei cannot, yet") sets up Chapter 12's "who writes the objective, who can see it, and who can change it when it hurts them". The new chapter must end on the same fact about learners and Surface Value, or Chapter 12's community and irrigators lose their contrast.
3. **The teaching condition.** Chapter 12's "Beyond Comprehension" ends: capacity "could give back to many more people, if we build it to teach as well as to answer." The new Chapter 11 is a company built to teach, and it is unmeasured. Chapter 12 can then point back in one clause instead of arguing from Dantzig alone.
4. **Rented capacity.** The company runs on one vendor's models. Chapter 12's "Who Owns the Laboratory" (the June 2026 suspension) gains a concrete subject; Chapter 11 should state the dependency in one sentence and not argue it.
5. **The profession question.** The old chapter ends on the author's work moving into the system; Chapter 12's "What Are Humans For?" picks it up. The new chapter needs an equivalent last beat about what running the company did to the founder's own role (author ask 10), or Chapter 12's section opens cold.
6. **Not to inherit:** System 3 Meta and "generate a company for anyone" belong to Chapter 12 at most ("If someone else can build the same thing, I might have a collaborator"), and only if the founder wants an unbuilt, parked company in print.

For Chapter 13: nothing. It is protected, and no proposal here touches it. For the Scaffolds page: the company-as-scaffolding framing (S10) must leave the payoff to the page.

### 5.2 Sentences elsewhere that would become false, orphaned or strained

Owner for every change: the writer proposes, the founder accepts. Production files go to the release manager and engineers.

| File:line | Sentence (exact) | Status after the rewrite | Suggested handling |
|---|---|---|---|
| `chapters/10-fluent-autonomy.md:141–143` | "An editing experiment has one advantage: I am there to say the result is wrong. A customer who gets a bad page files no correction. She leaves. / I spent years building systems that decide what to show her." | **Orphaned.** It is the hand-off into the store; the new chapter opens elsewhere. | Rework so it hands off to a learner: the same move works ("a learner who gets a bad lesson files no correction; she swipes"). The founder chooses; it is Chapter 10's closing beat. |
| `chapters/12-after-capacity.md:79` | "Chapter 11’s store that builds itself still needs its business experiment: an experience can convince the experts and the model and still fail the customer." | **False** if the title or subject changes. | Re-point to the company's unrun real-learner test; the sentence's logic survives intact ("can convince the experts and the model and still fail the learner"). |
| `chapters/12-after-capacity.md:235` | "I have not run that weekend. A hundred agents is a picture, not a measured capability or a cost estimate." | **Strained.** Literally true (that weekend), but the reader now knows a hundred-role company ran for a week with measured tokens. | Keep the honesty, adjust the claim: the weekend is unrun; a hundred agents is no longer only a picture. |
| `chapters/12-after-capacity.md:89` | "There is a point in an ambitious project when I begin mentally hiring the people it would require." | **Strained.** The author did hire them, as agents. | Opportunity for one clause pointing back to Chapter 11. |
| `chapters/12-after-capacity.md:239` | "That is the work I want to do: put the machinery this book has described within reach of people who have something they want to try. If someone else can build the same thing, I might have a collaborator." | **Strained.** The founder brief records "I have few people who want to try and build their own stuff." | The founder decides whether Chapter 12 mentions it. If not, the sentence stays true as aspiration. |
| `chapters/12-after-capacity.md:27` | "The customer became a funnel stage, the forest became a yield table, and the city became a grid." | **Orphaned echo.** Its partner, the old Ch 11's "People Refuse to Stay in the Funnel", goes. | Harmless; still reads on its own. |
| `chapters/appendix-note-on-evidence.md:20` | "\| 11. The Store That Builds Itself \| My prototype store, its customers and a proposed business experiment \| Prototyped; the business experiment has not run \|" | **False.** | New row. Proposed wording for the founder: *"A running company of agents built from this book, observed through its own records (re-checkable); no real learners yet; the planted-claim test designed, not run."* Category: "Observed, with re-checkable records", the VP record's category. |
| `chapters/appendix-note-on-evidence.md:5` | "The stories of companies, teams and people come from my experience. Names, companies and details have been changed, and some are composites or embellished. I do not say which is which…" | **In conflict** with the no-composite rule proposed for company material (VP record, acceptance point 4). | The Note needs an exception for Chapter 11 if the company is named and its records cited. Founder decision. |
| `chapters/afterword-what-this-book-proposes.md:67` | "\| My own experiments \| Small: one bounded problem, teaching demos judged by simulated learners, one ten-task comparison, one prototype \|" | **False** ("one prototype"). | Replace with the company, with its status. Do not upgrade the teaching demos' status: the company's learners are still simulated. |
| `chapters/afterword-what-this-book-proposes.md` (Thesis 1, "What needs testing") | "The note on evidence proposes planting a false belief and measuring how far it travels." | **Strained, not false.** The company adopted the test as EXP-001 and has not run it. | If Chapter 11 mentions EXP-001, the Afterword and the Note should say the same thing about its status. If EXP-001 runs before release, both change. |
| `chapters/07-recursive-self-improvement.md:43` | `<!-- AUTHOR: optional: could the circle-packing run, or a ranking or experiment story, carry some of the store's beats? -->` | **Changed context.** Chapter 7's illustrative store becomes the book's only store; its evaluation board and accumulating checks now have a real twin. | No change required. Optional, for the founder: one clause in Chapter 7 or Chapter 11 noting that the board exists. The comment stays until the author resolves it. |
| `chapters/09-layer-4-desire.md:77` | "Imagine a shopper asking a store’s assistant whether she needs the more expensive trail shoes." | **Loses its echo** of Mei's trail shoes. | Harmless. |
| `chapters/part-5-what-the-capacity-is-for.md` (epigraph) | "*A philosophy of emergence should be willing to lose an A/B test.*" | **Loses its source passage** in the old Ch 11 ("Deliberately Boring"). It still stands in the Zen. | Fine if the new chapter contains a test with a simpler baseline (the company's experiments do). Otherwise the founder may want another epigraph line. |
| `chapters/11-…` → `resources/editorial/easter-egg-register.md:18`, `check-eggs.sh:31` | Camel payoff "And now the camel comes back" (proposed seed) | **Orphaned** if the passage goes. `check-eggs.sh` will warn (proposed seeds only warn). | The author confirms or deletes the seed. If the new chapter opens with a reader quiz (Shape B), the writer must resist turning it into a camel callback that explains itself. Update the register in the same commit. |
| `chapters/appendix-references.md:511–513` | `ref-11-slate` (whole-page optimisation), `ref-11-store-pearl` (Pearl) | **Orphaned** if not cited. | Remove or reuse; new chapter references get `ref-11-*` ids. |
| `book-design/curated/book-order.json:20`, `book-design/curated/provenance.json:20`, `prompts/notebooklm/sources.json:208`, `prompts/notebooklm/chapter-11.md`, `resources/FILE-INVENTORY.md:223` | The filename and title "The Store That Builds Itself" | **False** only if the title or filename changes. | Release manager or engineer. Keep the filename stable even if the title changes, to limit churn (my recommendation). |
| System 3 Company: `company/decisions/2026-10-12-feed-is-not-personalised.md` ("Rests on: System 3, Ch. 11 ('The Honest Cold Start')") | — | **Orphaned in the other repo** once the old chapter is replaced. | Not the press's file. Tell System 3 Company's head of product through the founder. A claim whose address moved is the book's own Chapter 6 problem, so the chapter could even use it (Shape A's opening). |
| `chapters/about-the-author.md:21` | "…serves as Head of Applied Science at Zalando." | **Clearance**, not falsity. If the chapter carries an Amazon or Zalando comparison, the REVISIT clearance row widens. | Founder (REVISIT). |
| `chapters/00-preface.md` | "You could begin something that once required the power to assemble an institution." | **Not orphaned: paid off.** | Leave it unexplained. The new chapter should make it true without quoting it. |

---

## 6. Author asks (only the founder can answer these)

Write answers in your own words. The writer will not invent any of them. Where a quotation from your messages to the company already exists, I note it; the commission still needs your decision on whether those words may be quoted in the book (objection 4).

**Why it exists**
1. What made you start System 3 Company, and when did you decide? Was there a moment, a day, a conversation? (Your words to the company exist: "We started all of this to test System 3 book ideas, especially the philosophy of science…" and "When I started this it was a choice to go with demos: they are kind of independent but need collective work to scale." Do you want the book to say it that way, or differently?)
2. Why lessons and not the store? Was the company a way to run, in another domain, the business experiment the store chapter says you never ran? What happened to the prototype store?
3. What did you want from it on the first day, and what do you want now? Is 10,000 lessons the goal, or a stand-in for something else? (Chapter 9 says desire forms on the way; this is your own case.)

**Moments**
4. Describe one moment you watched it work: a time you used a lesson yourself and learned something, or a catch by one role that surprised you. What were you doing when you saw it?
5. Describe one moment you watched it fail. Candidates on disk: the r7 release reaching production before your approval (COE 2026-10-15); "you are working all the day but number of demos did not move" (2026-10-16). What did you feel, and what did you change: the agent or the mechanism?
6. Has any person outside the company used a lesson: a friend, a colleague, one of your children? Which lesson, and what happened? If not, will you run EXP-002 (five adults, think-aloud, recall three days later) before the draft closes? The chapter's ending depends on your answer.
7. Did any agent ever refuse you and turn out to be right? Did you ever override one and turn out to be right?

**Amazon and Zalando**
8. Which mechanisms did you bring from Amazon and from Zalando (COE, WBR, operational planning, single-threaded owners, "mechanisms over intentions", anything else)? Which behaved as you expected with agents, and which did not? Is there a failure the company reproduced in days that took a human organisation years? May the book name either employer (REVISIT clearance)?
9. The store chapter's own advice was a deliberately boring first test: one placement and a few validated problems. The company went to 14 domains and over a thousand lessons before one real learner. Was that a choice, and would you make it again?

**Your role**
10. What did running a company of a hundred agent roles do to your own job? Where did your attention go, and where did you want it to go? (The chief of staff chose about 99% of specialists' work in one 48-hour window; you approve every deploy.) Does it change how you feel about the old chapter's last paragraph, about work moving into the system?
11. How many hours a day did you spend on it in the first week, and what did it cost in money? (Tokens are partly measured in `company/ops/token-budget.md`; your time is not.)

**The objective**
12. Why a vertical swipe feed, given Chapter 12's critique of the feed? Why an ad slot? Who is meant to pay for the lessons, and should the book say?
13. Should learners ever have standing to contest Surface Value, and how? If not, how will you answer the reader who asks why Mei still cannot?

**What the chapter may print**
14. May the book quote your words to the company ("It is System 3; we call it science"; "reaching 10k would be impossible"; "yes, deploy r7")? May it name the company, its URL, the model vendor and its services, or should they be generalised?
15. Mei, Sami and Lea: keep them as illustrative learners, keep only Lea (the no-history visitor), or let them go with the store?
16. Title: keep "The Store That Builds Itself", or one of the options in section 2?
17. The press (the company writing your book) and System 3 Meta (a company to generate companies): do you want either in this chapter, in Chapter 12, or in neither?

---

## 7. Notes for the evidence record and the fact-checker (unverified, as I read them on 2026-10-17)

- `node tools/company.mjs status`: 1,283 lessons (329 draft, 234 review, 720 published in the repo); 4,935 claims awaiting the fact-checker, some disputed; board doing 6, review 151, next 54, backlog 843; rituals on cadence.
- Production releases r1–r9, 2026-10-14 to 2026-10-17 (`company/ops/releases.json`). The published-lesson counts in its entries sum to 133. "Published in repo" and "deployed" are different states (`progress.md`, 2026-10-17: "Published in repo, NOT deployed").
- Roles: 26 at founding (`org-chart.md`, `decisions/2026-10-12-company-structure.md`); "97 roles exist" (`decisions/2026-10-15-founder-first-light.md`); `company/roles/` holds 101 files including its README, and `.claude/agents/` holds 98. Count the agents, not the files, before printing a number.
- Throughput (`decisions/2026-10-16-founder-throughput-for-10k.md`): new lessons 852 (10-13/14) and 10 (10-15/16); new builds 8% of 18.65M tokens on 10-16; about 146k tokens per new lesson.
- Delegation (`rituals/records/2026-10-16-retro-delegation.md`): 730 commits in 48 h, 693 (95%) authored as "Claude"; 223 logged dispatches, all by the chief of staff; "about 99%" of specialists' work chosen by the chief of staff. The retro itself calls this "testimony-grade evidence".
- Measured tokens: 61.2M at the time of `company/ops/token-budget.md` (2026-10-14), with known gaps listed there.
- base-rates (`src/demos/probability/base-rates/meta.json`): v2, published, nine claims all verified; `humanLearners: []`, `pairwise: []`; c7 and c8 added and verified under the same role name (S1).
- EXP-001 and EXP-002: both "designed, not run", dated 2026-10-12.

---

## 8. Objections to this study's own recommendation

| Objection | What happened to it |
|---|---|
| Shape B leans on one lesson and could read as product marketing. | **Kept as a risk, mitigated in the shape.** Section 5 ("Gates Held, Delegation Didn't") and section 6 (owner and objective) must carry real failures and an open conflict. If the draft's sections 5–6 are softer than section 4 of this study, the panel should send it back. |
| Recommending real-learner sessions before the draft closes reaches outside the press's lane and may delay the chapter. | **Phrased as an author ask, not a requirement** (ask 6). The chapter can end honestly on the empty field. The recommendation is only that it would be stronger. |
| Dropping composition, traces and LLM narration loses the author's most technical lived material (commission objection 3). | **Open for the founder.** Shape A keeps it; the founder can choose A, or ask the writer to keep one store passage in B's section 6. |
| This study was written by the same model as the company's agents and the writer who will draft from it. | **Not solvable here**; carried into the chapter's limits (S12). The founder's own reading of this study is the outside check. |
| Shape C's evidence may be what the founder actually wants from "around System 3 Company". | **Open for the founder.** I recommend B for Part V's job and the VP's evidence route for C's material, but the founder commissioned the chapter and may prefer the audit. |

## Handoff

- **Changed:** wrote this file only. No manuscript, company or register file was touched. I ran no state-changing command.
- **Believe:** (high) the main structural risk is a retrospective that turns Part V inward, and the two store ideas that became company files (cold start, Surface Value) are the honest continuity. (medium) Shape B is the right shape; its success depends on sections 5–6 being harder than the rest. (low, and the founder's to decide) the title.
- **Next:** head-of-book-system-3 writes the brief (shape, the definition of done in §1.4, the author asks in §6). The experiment developer checks the numbers in §7 and the incidents cited in §4. The founder answers §6, decides title and shape, and answers the commission's open objections 3 and 4.
- **Blocked on the founder:** the shape and title; permission to quote his words and name the company and its services; whether real-learner sessions happen before the draft closes.

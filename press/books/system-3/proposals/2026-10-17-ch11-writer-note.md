# Writer's note: Chapter 11 draft ("Guess First"), 2026-10-17

owner: writer-system-3 (Callum) · for: head-of-book-system-3 and, after the reviews, the founder
**Keep this apart from what reviewers see first.** The development editor and the panel read the chapter text cold, without this note or the source map (brief §7.2).
draft: `chapters/11-the-store-that-builds-itself.md`, branch `ccr-fd4ebbbc-p06k8x`, **not committed**
companions: `press/books/system-3/proposals/2026-10-17-chapter-11-source-map.md` (fact-checker only), `press/books/system-3/proposals/2026-10-17-chapter-11-consequential-edits.md`
status: **draft. Not reviewed, not fact-checked, not accepted by the founder. I have not marked any of it checked.**

## What I read

Brief (all); press README and my role file; working spine; `ai-tells` skill; Chapters 4 and 5 in full; easter-egg register; old Chapter 11 in full; Chapter 10's last section; Chapter 12's opening and the lines the brief names (79, 89, 169, 235, 239); the Part V page; the evidence record and the fact-check (FC corrections used throughout); the structural and book studies' sections 3-7 (not every line of either; I read the dependency tables, strains, hand-offs, voice and constraints sections). Company sources, read-only: the base-rates `Demo.tsx` and `meta.json`, its simulated-learner review, `DemoCard.tsx` and `src/lib/trust.ts` (the learner's trust sheet), `CLAUDE.md`, `company/principles.md`, `mission.md`, `product/surface-value.md`, `product/vision.md`, constitution Article 4, AMD-008's header, `EXP-002`, the decisions on company structure, feed, deploy approval, no git deployments, org and dispatch, throughput for 10k and the r9 Safari waiver, the 10-15 COE, the 10-16 delegation retro, the pattern "a rule without a mechanism is a wish", and the left-or-right `meta.json`. I ran nothing that changes state in the company repo; I ran the lesson's `town()` function in my scratchpad (source map items marked W).

## Shape, headings, length

Shape B, eight `##` sections, the brief's working headings unchanged: Ninety-Nine Percent Accurate · Nine Claims Behind One Minute · A Company in a Week · Built From the Book · The Book Comes Back to Bite Me · Willing to Lose · Written Where Someone Can Argue With It · The Student Has Not Been Asked. Title *Guess First*, subtitle *One Minute, One Learner* (D2 default). Filename kept (D3).

Length: **4,778 words by `wc -w`** (inside 4,000-5,500). Of that, **14 AUTHOR comments are about 725 words; the prose alone is about 4,050.** That is near the bottom of the band. I did not pad (brief §2.2). If the founder answers the asks, the prose will grow into the band naturally; if the panel finds the draft thin, the first place I would add is §1 (one more beat of the lesson) and §7 (the pressures), not §5.

## check-tells and check-eggs

`python3 resources/editorial/check-tells.py 11 --lines` (final run):

| maxim% | notXbutY/1k | cite-chains | xref/1k |
|---|---|---|---|
| 26% (target ≤ 30) | 0.0 (≤ 0.5) | 0 (0) | 0.0 (≤ 0.5) |

All four targets met. The old chapter scored 21%, 0.4, 0, 0.0. My first draft had xref 0.6, from "this chapter" twice and "next chapter" once inside an AUTHOR comment (the counter reads comments); I rephrased all three. The 11 flagged maxims are short last sentences. I kept the ones a scene in the same paragraph earns ("That part was luck." was a rewrite of a "not X" construction; "I would not soften either half." follows the override scene). The weakest are "The records hold no figure for money." and "Nobody knows the answer yet, including the company."; review-llm-tells may want them.

Other counts I kept by hand: **0 em-dashes**; no bold terms; no chapter numbers in running text; about 32 prose colons (Chapter 4 has about 41 in a similar length), most introducing a quotation; none of the skill's vocabulary list in a figurative sense (grep finds only the literal "harness" for a test harness); no "This chapter…".

`bash resources/editorial/check-eggs.sh`: **passes, exit 0, no warnings** (the camel anchor "And now the camel comes back" holds in the same file). No new seed planted. "Coffee" does not appear (I removed one stray "with a new coffee" in revision).

`validate_references` from `book-design/curated/manuscript.py`: **passes** ("references OK"); both `ref-11-*` entries are cited, numbered [1] and [2] in order.

## What I kept

- The A/B-test line verbatim, with "Otherwise it is branding." directly after, in §6, in the old logic (earn complexity against simplification; here the single-agent baseline the founding decision itself names).
- "The Book Comes Back to Bite Me" as a heading (§5).
- The camel sentence verbatim (§2), one mention, no gloss beyond the questions it already lists. I cut the old follow-up sentence ("The argument about hallucination from earlier in the book…") to avoid stitching.
- The 11:7 AUTHOR comment verbatim, directly after the store passage's first sentence (new line 45).
- The author's store sentences (brief §3.4), trimmed, nothing added about what the prototype did or why he stopped.
- "Let the LLM narrate. Do not let it declare reality." (§5, the checking-the-disk beat).
- "If your ecosystem rewards clicks, clickable organisms evolve." arrives as the company's mission quoting it back (§7).
- `"humanLearners": []` used once, in §8, as the code punchline.

## What I cut or moved

Everything listed in the consequential-edits file §2. Not reused, though the brief allowed it: "'The model chose it' is not an answer…" and "a junk drawer with tenure" (neither found a natural home without forcing).

## Decisions I made where the brief left room

1. **Three bites in §5, all three of the brief's (a)-(c).** I kept (b) to one paragraph so the section stays near its 750 target. The QA-label alternative (C12) is not used.
2. **Founder quotations: two places, three quoted strings**, each with an AUTHOR permission comment and a ready paraphrase: the throughput complaint (§5), and "Deploy" with the option label "Ship it anyway" (§7). I did **not** quote "yes, deploy r7": it carries a release number (brief §2.3) and the scene works without it ("The founder approved it."). Both places say the words reached the record through an agent, per FC row 94.
3. **"Ship it anyway" is presented as the option he chose, and "Deploy" as his word** (FC correction 8). The override is called "an override of a review's ruling", not of a gate (FC row 74 note).
4. **The COE's fifth why is described as landing on a person** (FC dispute on C1); the record's "named a mechanism, not a person" is not used.
5. **C6's retro numbers are labelled the retrospective's own, testimony-grade, and not recomputable** (FC correction 7), with today's file's direction (every dispatch still the chief of staff's) added from the FC.
6. **C5 is a "new run at its latest commit"** (FC correction 6), fenced in the same paragraph as not the planted-diagnosis test, with the one-model limit.
7. **C8: only the dated sentence** in §8 (D16). The r9 deploy is described as approved, never as shipped.
8. **Added detail from the lesson's own code** that the brief did not list: the first hundred people contain no sick person but one positive; the first sick person arrives around the third hundred; the card is budgeted at 80 seconds although the company calls its lessons sixty-second; the trust sheet's exact wording and its footer ("0 human-learner studies… only people can show that a lesson teaches"). These are W items in the source map; the fact-checker should rerun them.
9. **Added from company records (new X items, not in the record):** the day-one vision of "8 domains, ~20 lessons" (X5); constitution Article 4.3 "Disputes about evidence are settled by tests. Disputes about purpose go to the founder." (X6); the principles file's practice for the A/B line, "Experiments include a simpler baseline that is allowed to win." (X10); the knot lesson's title *Can a knot match its mirror?* (X13), which ties C14 to C9; AMD-008 `proposed_by: founder` (X16); "Gates held while the delegation did not…" (retro line 52, quoted in SS S6).
10. **The press is named once, in §4**, with the observation that the author is the one reader outside the model (D11 default).
11. **Rented capacity** is one clause in §3 ("one developer's models, rented by the token"); the teaching condition is one sentence in §8.
12. **The ending** goes to the empty field (D10 default), with the AUTHOR comment where a real learner's guess would go, the profession beat as an AUTHOR comment before the last paragraph, and a closing question handing on to Chapter 12 ("Who decides what the capacity is for, when the people it is for cannot?").
13. **"Every learner review on file opens with…" was softened** to "The company's rules make every learner review open with…" after I found 17 of 1,811 matching files without the line.
14. **Spelling:** the book's American spelling in prose ("personalized", "organization"); company quotations keep theirs.

## Places I am least sure of (for the development editor, after her cold read)

- §4's last sentence ("the author is the one reader who is not a copy of it, which is an awkward thing to have to point out about your own book") is argued first person about the book's making. It is true of the process, but the founder may not want it in his voice.
- §5 is the longest section and the most like a report. It is where the panel may find the "tour" the brief forbids.
- "If you picked 99%, you are in good company, and some of it has medical degrees." is my joke in the author's voice. Cut if it reads as mine.
- "The best idea in the store was about the objective" is a judgment in the author's voice; it rests on the old chapter's own emphasis, but he should confirm.
- The closing paragraph's "asked a thousand times for a guess" is a figure over 1,283 lessons.

## AUTHOR asks in the draft (14 comments)

| # | Where | Ask |
|---|---|---|
| 1 | §2 end | Ask 4: one moment you watched it work (a lesson you learned from, a catch that surprised you). |
| 2 | §3, after the store's first sentence | **Moved verbatim from 11:7:** "What did the prototype actually do or show? A screen, a session, a surprise? One moment from the prototype would anchor the chapter." |
| 3 | §3, end of store passage | Ask 2: why lessons and not the store; what happened to the prototype (plus a note that cutting the passage needs acceptance for the 11:7 comment and removes [1]). |
| 4 | §3 | Ask 1: what made you start the company, and when; may the book use your words. |
| 5 | §3 | Ask 11: hours per day in the first week; money spent. |
| 6 | §4 | Ask 17: the press named once as a limit: keep, cut, or reword (D11). |
| 7 | §5 | **Quotation permission (ask 14, D4):** "What is going on you are working all the day but number of demos did not move"; paraphrase ready; confirm it is what you typed. |
| 8 | §5 | Ask 5 (a moment you watched it fail; agent or mechanism) and ask 8 (mechanisms from previous employers; may they be named). |
| 9 | §6 | Ask 9: fourteen subjects before one real learner: a choice, and again? |
| 10 | §7 | Asks 3 and 12: what you wanted on day one and now; is 10,000 the goal or a stand-in; why a feed, why an ad slot, who pays. |
| 11 | §7 | **Quotation permission (ask 14, D4):** "Deploy" and the option "Ship it anyway"; paraphrase ready; plus ask 7 (did an agent refuse you and turn out right, or you override one and turn out right). |
| 12 | §7 end | Ask 13: should learners have standing to contest the objective, and how. |
| 13 | §8 | Ask 6 / D10: has anyone outside used a lesson; will you run the five-learner test; where one person's verbatim guess would go. |
| 14 | §8, before the last paragraph | Ask 10: what running the company did to your own job; does the old last paragraph still hold. |

Asks 15 (Mei, Sami, Lea) and 16 (title) are in the consequential-edits file only, as the brief says. Naming (D5) is not a comment: the draft names only "System 3 Company" and generalises every vendor ("the hosting service", "one developer's models"); Safari and iPhone are named because they are the risk the founder accepted, and the founder may want them generalised too ("one phone's browser").

## Handoff

- **Changed:** `chapters/11-the-store-that-builds-itself.md` (full rewrite, in place, uncommitted); wrote this note, the source map and the consequential-edits file; added a dated entry at the top of `press/progress.md` (brief §7.1). Nothing in `/home/user/system-3-company` touched. Chapter 13 not opened.
- **Believe:** (high) every must-keep and honesty item in brief §3-§4 is in the text beside its claim; (high) the checkers pass; (medium) the voice is close to Chapters 4-5 in §1, §2 and §5, flatter in §7; (medium) the fact-checker will find small wording issues in the W and X items, which I could not check myself.
- **Next:** development-editor-system-3 reads the chapter cold (owner: head of book routes); fact-checker-system-3 works from the source map's X and W items, rechecking C8's timestamp first; the founder answers the 14 comments and decisions D2, D4, D5, D6, D10.
- **Blocked:** nothing for the draft. The ending and the profession beat wait on the founder.

---

## Revision 1 (2026-10-17): answers to the review round, one finding at a time

owner: writer-system-3 (Callum) · text: `chapters/11-the-store-that-builds-itself.md`, revised in place, **not committed** · status: **revision. Not reviewed, not fact-checked, not accepted. I have not marked any of it checked.**

Records answered (all `resources/evaluations/`): `2026-10-17-ch11-development-edit.md` (DE; governs, with its "must not be touched" list), `2026-10-17-fact-check-ch11-draft.md` (FC), `…-ch11-review-arc.md` (ARC), `…-review-ideas.md` (IDEAS), `…-review-llm-tells.md` (LLM), `…-review-prose-quality.md` (PROSE), `…-review-easter-eggs.md` (EGGS), `…-review-narrative-momentum.md` (MOM).

### Numbers after the revision

- `wc -w`: **5,345** (band 4,000-5,500). Prose about **4,485**; 14 AUTHOR comments about **862** (comments grew because each priority ask now says so and two comments carry new questions). DE asked me not to pad back to 4,800; the growth comes from the store block (DE 3.1), the hub-as-evidence paragraph (IDEAS 3), the bet (ARC 1), the "verified" paragraph (IDEAS 4), the A/B conclusion (IDEAS 1), the override argument (IDEAS 2) and the recall answer (EGGS F8). Cuts: the recap, provenance tails, the scale dump, refrain sentences, signposts.
- `python3 resources/editorial/check-tells.py 11 --lines`: **maxim 23%, notXbutY 0.0/1k, cite-chains 0, xref 0.0/1k** (targets ≤30, ≤0.5, 0, ≤0.5). 13 maxim hits, read: 1 false positive ("Right?" on the card); the rest are events, rules or the author's own store lines.
- `bash resources/editorial/check-eggs.sh`: **exit 0, 36 anchors ok, 0 warnings**. Camel anchor verbatim.
- Reference validation (`validate_references` from `book-design/curated/manuscript.py`): **references OK**; [1] and [2] cited in order.
- 0 em-dashes; 0 "as of"; no bold; no chapter numbers in running text; the press named once (§4).
- Headings unchanged (eight sections): Ninety-Nine Percent Accurate · Nine Claims Behind One Minute · A Company in a Week · Built From the Book · The Book Comes Back to Bite Me · Willing to Lose · Written Where Someone Can Argue With It · The Student Has Not Been Asked.

### One conflict I had to resolve

DE says §1 must not be touched, and FC requires corrections to four §1 sentences (fix 5 disputed; fixes 9, 10, 11, 12 correct-with-value). A false sentence cannot stay because it is well written, so I made the smallest edits the FC asked for and touched nothing else in §1: "Nothing in the lesson itself works until you pick one and lock it in"; the other two towns "opened once you had tested the full one"; "a 1978 Harvard study"; "a scripted browser test pressed every button"; "Every factual sentence the card showed you". I also dropped "when the right answer, if the test catches every case, was about 2%" (DE 1.2, PROSE 3, MOM 2: the 2% contradicts the reader's 9% with no parameters). Every line on DE's and PROSE's keep lists in §1 is verbatim.

### Development edit (governs)

| Finding | Done / declined |
|---|---|
| 0.1 must: no lived moment; rank the asks | **Done as far as the writer can.** Top four marked "(priority)" in the comment text, in DE's order: Ask 6, Ask 2 (with the 11:7 comment, which stays verbatim and unmarked), Ask 5 (Ask 4's comment says it is the alternative to 5), Ask 3. All 14 comments kept. The chapter reads finished with none answered: the store block now carries its own ideas (3.1), the A/B conclusion is drawn in the text (IDEAS 1), the ending stands on the empty field. Owner of the cover note: head of book. |
| 0.2 must: Ch12 contradicts Ch11 (routing) | **Routed, not edited.** M2 (12:79) and M3 (12:235) updated in the consequential-edits file with DE's narrowing and the "must travel with the revision" note; EGGS F2's camel-anchor warning added to M2. |
| 0.3 should: one dating device | **Done.** One sentence in §2: "Every figure here is as it stood on the 17th, when the company was not yet five days old." All eight "as of" removed; event dates kept (14, 15, 16, 17 October). Pre-release refresh of the "not yet done" items is for the head of book to schedule (listed in the source map, second-check section). |
| 1.1 keep §1 | **Kept**, except the FC corrections above. |
| 1.2 could: Harvard parameters | **Done by subtraction** (2% dropped; 95% kept, which is the point). |
| 2.1 keep camel, fence, gate | **Kept in substance; wording changed only where FC disputes it** (fixes 1, 2). "one witness wearing different coats" and "because the rule it enforces is about builders" survive. |
| 2.2 could: lean on the evidence rule | **Done.** The fence paragraph now ends: "Even my own words to the company reach its files through an agent that wrote them down. Everything else here is the company's account of itself… I say so once, here, rather than at the end of every paragraph." The provenance tails then left the running text. |
| 3.1 must: store passage stranded | **Done.** One cuttable block of five paragraphs, all from the author's own sentences in the old chapter (`6a4912c` 11:5, 11:15, 11:191-195, 11:111, 11:201-205, 11:9, 11:239), with the 11:7 comment verbatim after the first sentence. It now plants the objective ("I wanted those trade-offs written into the design, where someone can question them. If margin is part of the objective, admit it.") and the boring first test ("…and it had to beat simplification… The system should have to earn its complexity."), plus "If your ecosystem rewards clicks, clickable organisms evolve." (EGGS F9a). The hinge now names its noun: "System 3 Company is education and the organization doing the building at once." The callbacks to re-point if the store is cut are listed in the consequential-edits file (C1-C5). **Declined in part:** I kept the opening sentence ("After years working on ranking and recommendations…") although it echoes Chapter 10's last line, because it is the author's sentence, the 11:7 comment is anchored to it, and ARC 2 and MOM 7 both want the Chapter 10 cue picked up where the store enters. The one new connective, "The design's best idea was about the objective.", is the writer's (founder to confirm, as before). |
| 3.2 should: number dump | **Done.** Kept 26 → 99 roles, the vision's eight subjects and twenty lessons against 1,283 in 14, and 720 published. Commits, first-commit time and the 72 moved to the source map. |
| 3.3, 3.4 keep | **Kept.** |
| 4.1 keep §4 | **Kept**, except FC fixes 6, 16, 17 (factual) and the press sentence's model wording. |
| 4.2 should: "awkward thing" writes a feeling | **Kept, with DE's second option:** the Ask 17 comment now asks the founder whether the clause is his to keep. IDEAS 7, LLM 11 and PROSE 9 all list it as a keep. |
| 5.1 keep three bites, deploy story | **Kept.** Inside the deploy story only FC corrections and the 5.2 translation changed ("put it live"; "the last of its five whys"; the last clause, see FC 20). |
| 5.2 should: translate jargon | **Done.** "lanes" only inside the quotation; "areas of work", "assignments", "sender", "sends work", "the manager responsible", "started without asking", "put it live", "the last of its five whys". "testimony-grade" and "backfilled" gone from the text. "Dispatcher" survives only inside the quotation. |
| 5.3 should: provenance tails | **Done.** Moved to the source map: the backfill sentence, "the company's numbers, which I have not recomputed" (now "by its own count"), the commit-statuses and replay sentence, "as an agent transcribed it", "Those words reached the file second-hand", "at its latest commit". The two quotation comments still carry their transcription caveats. |
| 5.4 must: press named three times | **Done.** Named once (§4). The replay sentence is gone from the text; the harness is "A new harness, written for this book". |
| 5.5 could: one concrete dispatch | **Declined.** I have no single dispatch on record that I could quote without assembling it; DE says no composite. The hub now carries its weight through the new argument paragraph (IDEAS 3). |
| 5.6 could: "wearing new clothes" | **Done.** Dropped with "old advice"; the maxim follows the catch directly. |
| 6.1 keep | **Kept**, with the juxtaposition now a callback: "When I designed the store, the first test I wanted was deliberately boring, and it had to beat a simpler page. The company went to fourteen subjects in its first week." |
| 6.2 should: split bug paragraph | **Done** (two paragraphs; press removed; LLM 7's mirror pair recast as "So the tests can fail."). |
| 6.3 could: 17 vs twenty | **Done.** "The founding review's first objection, that 26 roles was heavy for 17 lessons" (the record's "Raised by: founding review"); §3 already says "the vision written on the first day". |
| 6.4 should: the standing institution | **Done** in §5's second bite, using the book's own definition and not a chapter number: "Fluent autonomy, as I have described it, forms the institution a request needs and takes it down when the work is done. This one stayed up, and the standing part ate most of the day." It also sources the second warning to the book (FC 27): "the failure the book calls bureaucracy's usual one, that it never comes down". |
| 6.5 could: "developer" | **Done** ("one vendor's models"; "two models from the same vendor"). |
| 7.1 keep | **Kept**, including "Nobody knows the answer yet, including the company." (see LLM 3). |
| 7.2 could: "payoff" | **Done**: "it teaches its point" (the file's gloss: reviewers can name the idea after the reveal). |
| 7.3 should: store objective unseen | **Done** via 3.1; §7 opens "The store's idea about the objective is now a file." |
| 8.1 must: cut recap; Chapter 12's line | **Done.** The recap paragraph is deleted; "teach as well as to answer" appears nowhere in the chapter. The bet is stated in §2 in this chapter's terms (ARC 1). M6 in the consequential-edits file is withdrawn. |
| 8.2 keep | **Kept**, except "to its credit" dropped (DE R5). |
| 8.3 should: ending says it twice | **Done.** Last paragraph: the two kept sentences verbatim, then "What the minute is for is written in a file the founder owns. The person it is for has not been asked." and the question. |
| 8.4 should: keep Ask 10 short | **Done** in the comment ("One or two sentences, about your attention and your days"). |
| 8.5 could: register the heading | **Routed** (consequential-edits S3). I do not edit the register. |
| §9: Safari and iPhone kept; W items | **Kept**; W items listed for the fact-checker's rerun. |

### Fact-check (all 8 disputed, all 17 correct-with-value, 2 unverifiable, 10 second-checker rows)

| FC item (row) | Status | What the text says now |
|---|---|---|
| 1 disputed (31, 59) | **Done** | "By the company's own log, the builder that wrote the 9% and the fact-checker that checked it ran on two models from the same vendor… One model family checking itself is still one witness wearing different coats". §4: "running on the same vendor's models… come from one family of models all the way down… not a copy of any of them". §5: "one model agreeing with another from its own family". Model names generalised (brief §5.1). |
| 2 disputed (35) | **Done** | "A day later a separate fact-checker session marked both verified, and its record calls itself independent. The first checker had asked for 'a checker other than the fact-checker'. That check is not on record, and the gate passed both claims anyway, because the rule it enforces is about builders." |
| 3 disputed (93) | **Done** | "It shows that nothing unchecked was marked published. Lessons still in review are on the site as well, tagged 'In review', by the founder's choice." Row 29 made consistent (fix 13). |
| 4 disputed (20) | **Done** | "…from what '99% accurate' means here to the counts on the full town, the Harvard study, the reveal's general sentence and the question that comes back days later"; §2 gate paragraph says "the reveal's general sentence". |
| 5 disputed (11) | **Done** | "It also gives the other two towns, which opened once you had tested the full one…" |
| 6 disputed (54) | **Done** | "takes most of the lines of the Zen of System 3… and gives each a practice" |
| 7 disputed (63) | **Done** | "narrow roles under managers, and by 16 October a map of twenty areas of work, each with a manager" |
| 8 disputed (117) | **Done** | "the form this book keeps warning about" |
| 9 CwV (3) | **Done** | "Nothing in the lesson itself works until you pick one and lock it in." |
| 10 CwV (17) | **Done** | "a scripted browser test pressed every button" |
| 11 CwV (18) | **Done** | "Every factual sentence the card showed you" |
| 12 CwV (12) | **Done** | "a 1978 Harvard study" |
| 13 CwV (29) | **Done** | "was refused publication" |
| 14 CwV (42) | **Done by cut** | the commit-count sentence left the text (DE 3.2); value kept in the source map with "default branch". |
| 15 CwV (43) | **Done** | "26 roles: 25 agents and the founder" |
| 16 CwV (55) | **Done** | "Its decision template has a heading, 'Rests on'" |
| 17 CwV (59) | **Done** | see item 1 |
| 18 CwV (66) | **Done by cut** | the "testimony-grade" label left the text; "by its own count" stays; the label is in the source map. |
| 19 CwV (81) | **Done by cut** | the commit-statuses sentence left the text (DE 5.3); in the source map as "show the build". |
| 20 CwV (87) | **Done** | "and nothing happened, because a push like that no longer creates anything for the word to start." This replaces the kept line "nothing listens for the word any more", which FC showed is false (the filter is still configured). It is my wording adapted from the FC's; **second check**. |
| 21 CwV (96) | **Done** | "funded with the first experiment and a cost comparison" |
| 22 CwV (108) | **Done** | "The company adapted it, for a false claim planted in a lesson, as its first experiment" |
| 23 CwV (116) | **Done** | "quotes one of my store sentences back at me, as its own:"; the store block now carries "If your ecosystem…", so the change of pronoun is visible. |
| 24 CwV (130) | **Done** | "Nothing is ratified without the founder." |
| 25 CwV (140) | **Done by cut** | the recap sentence is gone (DE 8.1). |
| 26 unverifiable (50) | **Reworded to the source** | "through an account with usage limits the company has already hit" (10-13 COE: HTTP 429; EXP-003). "Rented by the token" is gone. The real arrangement stays with Ask 11. **Second check** (FC-supplied wording). |
| 27 unverifiable (62) | **Reworded to the sources** | "Three warnings came true against the design built to heed them. Two are this book's. The company had written the third down itself, a day before it happened." Warning 1 is Chapter 5's "The organization was the bug" (5:28, 5:174); warning 2 is Chapter 10's "Its usual failure is that it never comes down" (10:49), now named in the text; warning 3 is the company's own pattern, dated 14 October. |
| N 52 | **Kept, shortened**: "Its ledger, which has gaps, records 113.1 million tokens…"; "so the real figure is higher" cut (an inference). Second check. |
| N 67 | **Removed from the prose** (source map). |
| N 74 | **Removed from the prose** ("as an agent transcribed it"); the general rule in §2 ("Even my own words to the company reach its files through an agent that wrote them down") rests on the same FC ruling: **second check**. The permission comment keeps its caveat. |
| N 82 | **Removed from the prose** (source map). The category "run" for the filter is now carried only by the §2 rule ("code that runs"). |
| N 85 | **FC's wording used because it narrows**: "did not check the hosting service's records" (COE line 21). Second check. |
| N 106 | **Removed from the prose** ("at its latest commit"); `e84b8784` stays in the source map. |
| N 122 | **FC's wording used because it narrows**: "One override of a launch review's ruling is on record." (The behavioural-pilot exemption is a gate ruling, so it is not counted.) Second check. |
| N 126 | **FC's wording used because it narrows the sequence**: "He answered the release summary with 'Deploy', and on the Safari question he chose the option labelled 'Ship it anyway'." Second check. |
| N 128 | **Removed from the prose**; the permission comment keeps "written by the release manager from the chief of staff's relay". |
| N 139 | **Narrowed in my own words**: "most of what the company had made since 15 October was not yet on its public site" (what the 404s and the 15 October cache show; "had not reached anyone outside it" claimed more). Second check, with a fresh timestamp. |

### Arc

| Finding | Done / declined |
|---|---|
| 1 must: Part V's question late | **Done.** §2 opens with the founder and the bet: "The bet worth following is that this much capacity, pointed at one stranger for one minute, changes what she believes, and that it stays changed. Most of what follows is evidence about something easier." The Chapter 12 phrase is not used. I did not shorten the deploy story (DE 5.1 and the must-not-touch list govern). |
| 2 must: store joint | **Done** with DE 3.1 (option a without new autobiography; the author's moment stays Ask 2 (priority) and the 11:7 comment). Stale-title files routed (consequential edits T1-T7). |
| 3 should: company before the audit | **Done in part.** Two sentences of the company (founder, under five days, about a hundred roles) now open §2 before the audit. Section order unchanged: DE recommends against moving "Built From the Book". |
| 4 should: Chapter 12's line | **Done** (DE 8.1). |
| 5 should: override closed too quickly | **Done** with IDEAS 2. |
| 6 should: Chapter 3's demos | **Done**, one clause in §8: "Whether a lesson teaches is the question my first teaching demos left open, and a company of agents has not closed it." No chapter number; no register row touched. |
| 7 could: move the camel to §8 | **Declined.** The brief (§3.3) and DE 2.1 place it in §2; the register row is proposed and the author decides moves. |
| 8 should: rank asks by arc weight | **Done** in DE's ranking, which differs from ARC's (6, 3/12, 10, 2): DE reconciles and governs. Ask 10 is unmarked but kept. |
| 9 could: move the press paragraph | **Declined.** DE 4.1 keeps §4 as placed; after 5.4 the press no longer acts later in the chapter, so the move would have nothing to land on. |

### Ideas

| Finding | Done / declined |
|---|---|
| 1 must: A/B maxim not fired | **Done, and set up for the author.** After the verbatim line: "By that line, the company is so far branding. Its structure has not yet been put anywhere it could lose, and it stops being branding on the day the dull arrangement is run against it with permission to win." The Ask 9 comment now asks the founder to replace or qualify those two sentences in his words. This is first-person argument from the book's own maxim, not autobiography. |
| 2 must: override declared | **Done.** "That is the system working as designed… I would not soften either half." is gone. The text keeps "The objection kept its consequence on paper, and the owner held the switch." (must-not-touch) and leaves the verdict a question tied to the interlude: "Whether that is the system working or the second way things go wrong, where the records keep coming out and the objection stops mattering, depends on what would happen if he was wrong. The record names what would show it: a Safari run, which the company's machines cannot do, a check on a real iPhone, or a report from a learner." The last clause lands on the learner nobody has asked. The new sentence about what the record names is an X item for the fact-checker. |
| 3 should: hub as evidence against emergence | **Done.** New paragraph after the hub fix: "Of everything in the records, this result cuts hardest against the book… what filled it within two days was a chain of command. The parts that held were written as code. The part written as a role description relaxed toward a hub. At the least, that narrows the emergence claim…" |
| 4 should: base rates on "verified" | **Done.** "And 'verified' deserves what the card did to '99% accurate'. It describes the check. What it is worth depends on how often the builder is wrong and how often the checker misses the same thing, and nobody knows either rate." |
| 5 should: between-modules idea | **Done**, without answering for the author: "So the page I once complained was dumb between its modules is now a feed kept dumb between its cards, by a written decision." and the amendment "would make the feed smarter between its cards". Which reading he holds stays with Asks 3 and 12. |
| 6 should: apply "wish" to the objective | **Done as a question**: "By the company's own pattern, a rule without a mechanism is a wish, and the fair question to put to 'never used to rank' is which of the two it is." I did not assert whether a mechanism exists (the feed's order is in code, but I have not had that checked). |
| 7 should: keep "not a copy" | **Kept** (reworded for FC 1). |
| 8 could: Pearl rung | **Declined.** "The company's reviews are seeing, and they are not even seeing a person." is on DE's must-not-touch list (8.2). Raised for the founder: a simulated review may be "doing, to a stand-in". |
| 9 could: "cannot" | **Done**: "when the people it is for have not been given a say?" |
| 10 could: jokes sanding ideas | **Done** for the second ("old advice… new clothes" cut); flour kept. |

### LLM tells

| Finding | Done / declined |
|---|---|
| 1 must: evidence-chain voice | **Done** (DE 5.3). Moved, not dropped: every caveat is in the source map, revision section. The fact-checker should confirm none had to stay inline. |
| 2 must: author absent | **Partly done; the rest needs the author.** §2 now says "The company is mine. I founded System 3 Company… its records call me the founder, so I will too." The scenes from his side stay with Asks 5/4 and 6 (priority). |
| 3 should: designed / not run refrain | **Done.** Full-strength uses kept: the baseline ("Nobody has run the comparison"; "none of them has a result"), "measures nobody", the five-learner test ("It has not been run."). Softened: the hub fix ("The fix is written down; whether it works has not been measured."), the amendment ("It is drafted and not ratified.", with "As of 17 October" removed), EXP-001 ("which is one of the eight without a result"). Cut: "It is designed and has not been run.", "The independence the note asked for is not on record.", "the bet is unmeasured". **Declined:** cutting "Nobody knows the answer yet, including the company." (DE 7.1 and PROSE 9 keep it). |
| 4 should: recap and doubled ending | **Done** (DE 8.1, 8.3). The chapter ends on the question, after the reveal sentence. |
| 5 should: signposts | **Done**: "Three are worth the space." cut; "Everything so far costs something, from…" → "All of this costs something." **Declined**: "I should say plainly…" and "There is a second turn to the recursion, and I will name it once." (§4 is on DE's must-not-touch list). |
| 6 should: unearned maxims | **Done**: "Let the LLM narrate…" now follows the catch with no frame (it is the author's own line, old 11:171 heading); "The tests are code, and the counts…" merged ("…but the tests are code."); "I would not soften either half." cut. **Kept**: the A/B line and "Otherwise it is branding." (brief §3.1; DE must-not-touch). |
| 7 should: mirrored pair | **Done** ("So the tests can fail. The test this book proposes… is a different one"). |
| 8 should: tics | **Done** for "as of" (0 left) and some "own"/"the company"; the 21 "own" are fewer but not counted down to a target. |
| 9 could: camel's questions | **Declined.** Anchor sentence verbatim; the author decides seed moves. |
| 10 could: catalogues | **Done** for line 27; line 69 kept (LLM agrees); "The pressures sit on the same files." → "The same files record the pull the other way." |

### Prose quality

| Finding | Done / declined |
|---|---|
| 1 must: who is "I" | **Done** with the first option (one sentence early, then "the founder" as the records' name). Switching his acts to first person is for the founder (it changes the permission comments). |
| 2 must: scenes end on the paper trail | **Done** (hub ends on the quotation; deploy on "That part was luck."; harness on the result; the knot on "Ship it anyway"). |
| 3 should: number passages | **Done**: 2% dropped; "over the sum of itself and 0.01 × 0.999"; the "ninety-two" list replaced; "26 roles: 25 agents and the founder". |
| 4 should: antecedents | **Done**: "Each of those catches needs a fence around it."; "education and the organization doing the building at once"; the revisit condition recast; "a fight with simplification" replaced by the author's own "it had to beat simplification"; the objective sentence is now the file's own wording ("If the objective is not written down…"). |
| 5 should: flat rhythm | **Done in part**: splits at the hub quote, the harness and "Ship it anyway"; some "The company's" openers changed. |
| 6 should: triple ending | **Done.** |
| 7 could: two images | **Done.** |
| 8 could: thin store | **Done** with the author's own lines (DE 3.1); the moment itself stays with the author. |

### Easter eggs

| Finding | Done / declined |
|---|---|
| F1 camel | No action; verbatim. |
| F2 Ch12:79 next to the camel anchor | **Routed** (consequential edits M2 note). |
| F3 tongue and ear | **Not changed; question for the author** (head of book to carry): the narrator's "made by something that is not one" and the italic title *Can a knot match its mirror?* sit near the Chapter 13 anchor. I kept both: one is on PROSE's best-lines list and DE's must-not-touch list, the other is the lesson's real title. |
| F4, F5, F6 | No change; F6's figurative "reveal" in the last paragraph is DE's kept sentence: author to confirm. |
| F7 UTC times | Kept "12:45 UTC" in 24-hour form; the 22:51 time left the text. Copy editor note stands. |
| F8 recall question unanswered | **Answered in the chapter**, §8: "The question that was supposed to come back days later has an answer, about 1 in 100: out of 10,000 people, about one sick person tests positive and about a hundred healthy ones do too. The company has no record of a single person answering it." (lesson `recall.answer` and `why`; claim c8). Register not edited. |
| F9a "back at me" with no plant | **Done** (store block carries "If your ecosystem rewards clicks, clickable organisms evolve."). |
| F9b "old advice" | **Done** (dropped). |
| F10 clothing twice | **Done.** |
| F11, F12 | No action. |

### Narrative momentum

M1, M4, M10, M17, M19 keep: **kept**. M2: **done** (2% dropped). M3: **done** (answered, see F8). M5: **done**. M6: **done in part** (the procedure now leads to the consequence; FC 2's facts made it longer by one sentence). M7: **done in part** (store's first sentence keeps the Chapter 10 cue; Ch12:79 routed). M8 must: **done** (DE 3.1). M9: **done**. M11, M12, M16: **done** (scenes end on the event). M13: no change needed. M14: **done** (LLM 3). M15: **done**. M18: **done**. M20: **routed** (ranked asks).

### Comments: what changed in their text (none removed)

All 14 kept. Added "(priority)" to Asks 6, 2, 5 and 3; Ask 4 notes it is the alternative to Ask 5. Ask 2 says the store callbacks are listed for a one-decision cut. Ask 9 asks the founder to replace or confirm the drawn A/B conclusion. Ask 10 asks for one or two sentences. Ask 17 asks about the "awkward thing" clause. The Safari permission comment's fallback sentence now matches the revised sequence. The 11:7 comment is byte-for-byte unchanged.

### What I believe, and how sure

- (high) Every disputed, correct-with-value and unverifiable FC item is answered in the text; no sentence still states what FC showed false.
- (high) Every item on DE's must-not-touch list is present, verbatim except where the FC required a factual change (camel and A/B line byte-identical).
- (medium) The new argument sentences (the bet, the hub as evidence, "verified", the A/B conclusion, the override question) are first-person argument the book already licenses; the founder may want them in his own words, and the A/B conclusion is flagged in Ask 9.
- (medium) §5 is still the longest section; it now carries the emergence argument, which is the right place for its weight.
- (low) Whether "a push like that no longer creates anything for the word to start" is exact for branches cut before 16 October (FC 20 caveat).

### Next

fact-checker-system-3 (a second instance, or the experiment developer) checks the second-check list in the source map's revision section, and the new X items; head-of-book-system-3 brings the founder the ranked asks, M2/M3 and the store-cut list together with this revision; the panel does not re-read unless the head of book commissions it.

## Revision 2 (2026-10-17): answers to the second fact-check

Source: `resources/evaluations/2026-10-17-fact-check-ch11-second.md` (Beckett). Applied on top of the copy edit, whose changes I kept. Every new wording below is either Beckett's or mine; none is checked. **All need an independent check** (a third fact-checker instance or the development editor), not Beckett and not me.

| Item | Line | Old | New | Note |
|---|---|---|---|---|
| F1 | 69 | "There are 269 of them." | "There are 268 of them." | Beckett's count (dated notes only). |
| F2 | 97 | "Across 13 and 14 October the company made 852 new lessons. Across the next two days it made 10." | "By the company's own count, across 13 and 14 October it made 852 new lessons. In the day and a half after, it made 10." | Attributed and window narrowed; kept as two sentences so the drop still lands. Moved "by its own count" out of the next sentence to avoid saying it twice. |
| F2b | 97 | "On 16 October, by its own count, new builds took 8% of the day's 18.65 million tokens" | "On 16 October new builds took 8% of the 18.65 million tokens measured by mid-afternoon" | Beckett's wording. |
| F3 | 71 | "All of these roles run on one vendor's models, …" | "The agents it dispatches run on one vendor's models, …" | Took the narrower alternative (true without hedging). New AUTHOR comment "Ask A1" after the paragraph: what made the `codex/` PRs; if another vendor's agent built part of the catalogue, the founder words this paragraph and the "one model family" lines. |
| F4 | 91 | "A society of agents can turn into one coordinator with an org chart attached, and the organization becomes the bug." | "This book warns that an org chart of titled agents does not make them independent, and that the organization itself can become the bug." | Now says what the book says (Ch5:28 "The organization was the bug"; Ch5:174 titled agents and the org chart, under independence). Kept "two are this book's" framing, so §5's structure is unchanged; chose this over making the hub the company's own finding because the paragraph's force is the book being bitten. My wording, adapted from Beckett's. |
| Opt. row 13 | 23 | "a scripted browser test pressed every button." | "a scripted browser test pressed every control on the stage." | Taken: exact (the test presses one prediction option, not every button). |
| Opt. row 101 | 163 | "most of what the company had made since 15 October was not yet on its public site." | "none of the fifteen lessons the company had published or put in review since 15 October was on its public site." | Taken: sharper and true; the old line counted drafts the site never shows. Beckett's figure. |
| F5 | source map §5 moved-out note and S4 row | "matches the marker in `aefb10a` only" | Beckett's fuller list (`aefb10a`; not `e6805f4`, `d8f5f89`; also `54aa64e3`, `f868127`, `6cbce514`) | Not in the prose. |

Kept: every AUTHOR comment (15 now, A1 added), the camel line and the A/B line byte-identical. `check-tells.py 11`: maxim 23%, notXbutY 0.0, cite-chains 0, xref 0.0 (pass). `check-eggs.sh`: pass.

Belief: (high) no prose sentence now states what the second fact-check found false. (medium) F4's wording is fair to Ch5, but "warns" is a reading of two passages, not a quotation; the development editor should judge it. (open) A1 may change L71, L39 and L83; only the founder can answer it.

Next: an independent checker verifies F1-F5, F2b and the two optional rows; head-of-book-system-3 carries Ask A1 to the founder.

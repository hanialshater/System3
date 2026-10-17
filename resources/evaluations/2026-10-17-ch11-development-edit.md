# Development edit: Chapter 11, "Guess First" (draft around System 3 Company)

owner: development-editor-system-3 (Harriet) · date: 2026-10-17 · book: system-3
text read: `chapters/11-the-store-that-builds-itself.md` as on the proposal branch (writer's draft, commit c98653a), 4,778 words including 14 AUTHOR comments (about 4,000 words of prose)
status: **edit letter, not an acceptance.** The writer revises; the founder decides. Nothing here changes the manuscript.

**Disclosure (from the brief's objections table).** I wrote the structural study this draft was briefed from, so I am not a cold reader of the company. I am a cold reader of this text. The panel lenses that follow are cold to both.

**How I read.** Chapter 11 first, cold, with nothing else open; my findings were written to a scratch file before I opened anything else. Then, in order: Chapter 10, Chapter 12, the Part V page, the brief (`press/books/system-3/briefs/2026-10-17-chapter-11-company.md`), my own structural study (`press/books/system-3/study/2026-10-17-structural-study.md`), and the old chapter (`git show HEAD~1:chapters/11-the-store-that-builds-itself.md`). I read the easter-egg register before judging the seeds. The writer's note was read only after sections 1-8 below were written; what it changed is in section 9. I did not fact-check any number; that is the fact-checker's job, and none of my findings depends on a number being right.

Checks I ran (read-only): `python3 resources/editorial/check-tells.py 11` gives maxim 26%, notXbutY 0.0/1k, cite-chains 0, xref 0.0/1k, all inside the targets. `bash resources/editorial/check-eggs.sh` passes; the camel anchor holds. Zero em-dashes.

---

## 1. Verdict

**Revise, do not reshape.** The draft does Part V's job. It opens outside the machine, on a reader guessing, and it ends outside the machine, on a person nobody has asked. The middle mostly behaves: one artefact is followed to its source, the circularity is admitted in plain words before any evidence is leaned on, and the failures are better material than the successes, as they should be. It is not a guided tour and it is not a Chapter 5 sequel. The opening section is the best opening in Part V and should not be touched.

The draft has five must-fix problems, none of them about the shape:

1. The store passage is stranded, and the later store callbacks point at something the reader has never seen (finding 3.1).
2. The penultimate paragraph is the machine admiring itself, and it spends Chapter 12's best line (finding 8.1).
3. The press appears three times, not once (finding 5.4).
4. There is no lived moment from the author anywhere, and fourteen AUTHOR comments are too many to send him unranked (finding 0.1).
5. Chapter 12 now contradicts this chapter in two places (finding 0.2; the fix is outside this file, but the chapter cannot be accepted without it).

Fix those and the draft is ready for the panel. Everything else below is "should" or "could".

---

## 2. Does it do its job in Part V?

Part V asks "What is the capacity for? The ending I want." The old chapter answered *to help this person with this problem* and gave the answer a politics (Surface Value; "Mei cannot, yet"). The new one answers more honestly and less warmly: here is one minute the capacity made for a learner; here is everything that minute rests on; here is who decides what it is for; and here is the fact that no learner has been asked. That is a better answer for this book than the store's, because it is about a running thing and it reports its own missing evidence.

What it does not yet do is say what the *author* wants. Part V's second clause is "the ending I want". The chapter shows the founder only as an actor in the records: he made a rule, he approved a release, he complained, he owns a file. The wanting is entirely in AUTHOR comments (asks 1, 3, 9, 10, 12, 13). That is the correct behaviour for a writer who may not invent autobiography, and it means the chapter is structurally complete and emotionally unfinished. Section 0.1 says what to do about it.

Hand-in from Chapter 10 works. Chapter 10 ends "A customer who gets a bad page files no correction. She leaves. / I spent years building systems that decide what to show her." The new chapter's first word is a card being shown to *you*. The page turns from "what to show her" to being shown, as the brief asked, and the *she* returns at the end as the learner with no standing. That thread is the chapter's spine and it holds.

Hand-off to Chapter 12 mostly works. The last question ("Who decides what the capacity is for, when the people it is for cannot?") lands on Chapter 12's "who writes the objective, who can see it, and who can change it when it hurts them", which the irrigators and the seven-on-Tuesday room then work out. Two problems: the chapter steals one of Chapter 12's lines (8.1), and Chapter 12 has sentences this chapter makes false (0.2).

## 3. The nine risks from the structural study

| Risk | Verdict | Where |
|---|---|---|
| R1 Guided tour | **Avoided.** Two mechanisms are shown working on artefacts the reader has touched (claims and the gate on the base-rates lesson; the objective and the owner's override on the knot lesson), and three failures. No rituals, floors, boards or patterns by name except the one pattern-library line, which earns its place. The knot lesson returning twice (the reversed rule in §2, the Safari waiver in §7) is good economy. | — |
| R2 Chapter 5 again | **Avoided.** The hub is Chapter 5 material, but it arrives as a failure of a design built to prevent it, with a count, which Chapter 5 could not have. | §5 |
| R3 Chapter 10's "Where This Could Be Wrong" again | **Mostly avoided.** Limits arrive as consequences of events. One soft overlap: Chapter 10 ended on institutions formed per request and taken down; this chapter presents a standing company of 99 roles and never notices the tension (finding 6.4). | §5 |
| R4 Circularity | **Handled squarely.** "Built From the Book" says it before the evidence is used and sets the rule the rest of the chapter follows. | §4 |
| R5 Self-regard | **Partly failed.** The press is named three times (5.4), and the penultimate paragraph praises the record's honesty (8.1). "To its credit" (§8) is a smaller case of the same thing. | §4, §5, §6, §8 |
| R6 Staleness | **Partly handled.** Numbers are dated, but "as of 17 October" appears eight times and several of the chapter's arguments rest on states that may flip before print (an amendment not ratified, four incident actions in the backlog, the baseline not run, the five-learner test not run). | throughout; 6.2 |
| R7 Lost lived material | **Failed, pending the author.** The store's practitioner voice is down to four sentences, and no lived scene replaces it. The writer was right not to invent one. | §3; 0.1, 3.1 |
| R8 Jargon | **Mostly translated**, except in "The Book Comes Back to Bite Me": lanes, dispatches, dispatcher, testimony-grade, backfilled, promoted to production, the fifth why. | §5; 5.2 |
| R9 Internals and employers | **Avoided where it matters.** No employer named, services generalised, no URL. The two internal strings used (`probability.base-rates.c3`, `"humanLearners": []`) are used deliberately and work. One wording slip: "one developer's models" (6.5). | §3 |

---

## Findings

Numbered by section of the chapter (0 = the whole chapter). Severity: **must** (fix before the panel), **should** (fix in this revision unless the writer argues otherwise in writing), **could** (the writer's call).

### 0. The whole chapter

**0.1 (must, owner head of book, then the founder). No lived moment, and too many asks to answer.** The draft carries fourteen AUTHOR comments covering asks 1-13 plus two quotation permissions and the moved 11:7 comment. Every one is legitimate; together they are a questionnaire the founder is unlikely to answer in full, and the chapter's quality depends on about four of them. *Suggestion:* the head of book brings the founder a ranked short list, in this order, and says the chapter stands without the rest:
1. **Ask 6** (has anyone outside used a lesson; will you run the five-learner test). The ending changes if the answer is yes.
2. **Ask 2 with the 11:7 comment** (why lessons and not the store; what the prototype showed). Finding 3.1 depends on it.
3. **Ask 5 or ask 4** (one moment from his side of the screen, failing or working). The chapter has no scene the author was present for; one would carry §5 or §2.
4. **Ask 3** (what he wanted on day one, and now). This is the "ending I want" clause of Part V.
The quotation permissions (§5, §7) are yes/no questions and can travel with the list. Asks 1, 7, 8, 9, 10, 11, 12 and 13 stay as comments (no recorded acceptance to remove them) but should be marked optional in the cover note. *And the writer should prepare for no answers:* the revision must read as finished if the founder answers none of them (3.1 says how for the store passage; the rest already read finished).

**0.2 (must, consequential edit, owner the founder via the head of book). Chapter 12 now contradicts Chapter 11.** `12-after-capacity.md:79` ("Chapter 11's store that builds itself still needs its business experiment…") is false after this rewrite. `12:235` ("I have not run that weekend. A hundred agents is a picture, not a measured capability or a cost estimate.") is now in direct tension with Chapter 11's "one founder and about a hundred roles of agents did in under five days" (§8). A reader who has just finished Chapter 11 will read 12:235 as coy or careless. *Suggestion:* the chapter cannot be accepted unless these two Chapter 12 edits are accepted with it, or the founder records that he wants the tension. For 12:79, the logic survives with the learner in place of the customer ("an experience can convince the experts and the model and still fail the learner"). For 12:235, keep the honesty and narrow the claim: the irrigators' weekend is unrun; a hundred agents on a week of lessons is not. Chapter 12:89 ("mentally hiring the people it would require") is strained the same way and is the founder's choice.

**0.3 (should, owner writer). One dating device instead of eight.** "As of 17 October" appears eight times, plus several clock times (22:51 UTC, 14:21, 12:45 UTC). The brief asked for "once per cluster"; in practice every paragraph is its own cluster. *Suggestion:* date the picture once, early, where the scale is given ("The figures in this chapter are from 17 October 2026, when the company was five days old"), keep the per-event dates that carry the story (the 14 October rule, the 15 October deploy, the 16 October retrospective), and drop the rest of the "as of" phrases. Separately, the head of book should schedule a pre-release refresh by the fact-checker: the chapter's argument rests on things *not yet* done (the baseline comparison, the five-learner test, the incident actions, the amendment), and if any of them happens before print the paragraph that relies on it changes meaning, not just number.

### 1. "Ninety-Nine Percent Accurate"

**1.1 (keep; must not be touched).** The section enacts the product on the reader: commit, play, see why. It is shown from the first sentence to the last. In particular: "So you guess. Everyone guesses something, even the people who are sure they would never fall for it."; "which is a strange thing to discover about your own test before you have even met the disease"; "If you picked 99%, you are in good company, and some of it has medical degrees."; "Its own file budgets eighty seconds, which is the first claim in it I would check."; and the turn "Nobody who made that minute is a person." The nine claims here quietly echo Chapter 4's seven; nobody should point that out.

**1.2 (could). The Harvard figure arrives without its parameters.** "the right answer, if the test catches every case, was about 2%" comes one paragraph after the reader has earned 9%, and a cold reader may think one of the two is wrong. *Suggestion:* one clause saying the Harvard question used a worse test, e.g. "for a similar question with a test that wrongly flagged 5% of healthy people", if the card's claim supports it (fact-checker to confirm against the study).

### 2. "Nine Claims Behind One Minute"

**2.1 (keep).** Following c3 from the reader's screen to its address, derivation, status and checker is exactly the "one claim end to end" the shape needed. "And now the camel comes back" is in place verbatim (registered seed; check passes) and is not explained. The fence paragraph ("One copy of a model catching another is still one witness wearing different coats") and the role-name gate paragraph (two claims added and then verified by the same role, which the gate passed "because the rule it enforces is about builders") are the most honest pages in the chapter and the reason a sceptical reader will trust the rest. Do not soften either.

**2.2 (could). "The witnesses that are not the model are few" is the evidence rule for the whole chapter.** It is in the right place. Finding 5.3 asks the writer to lean on it so later paragraphs can drop their individual provenance tails.

### 3. "A Company in a Week"

**3.1 (must, owner writer, with the author's answer to ask 2 if it comes). The store passage is stranded, and the store keeps coming back without having been shown.** The section opens on "After years working on ranking and recommendations, I built a prototype store because the idea would not stay on the page.", which is nearly a restatement of Chapter 10's last line two pages earlier. Three sentences of store follow, then "My complaint was simpler. The page is smart inside the modules and surprisingly dumb between them.", then the hinge "System 3 Company is the last two at once", whose antecedent ("research, education or the organization doing the building") the reader has to go back for. Later the chapter leans on the store as if the reader knew it: "When I designed the store, the first test I wanted was deliberately boring" (§6), "The best idea in the store was about the objective" (§7), "Both ideas began in the store", "quotes one of my store sentences back at me" (§7). The reader of this book never read the old chapter. To them the store is four sentences and a citation. *Suggestion:* make the store passage carry the two store ideas the chapter later cashes, in the author's existing sentences from the old chapter, so the later lines are callbacks and not news: the objective written down where someone can argue with it (old "The Objective Fights Back": "If margin is part of the objective, admit it."), and the deliberately boring first test against simplification (old "Deliberately Boring"). Drop the opening sentence's echo of Chapter 10 or merge it into the hinge, and replace "the last two at once" with the noun it refers to ("education and the organization doing the building, at once"). Keep it one cuttable block. If the founder cuts the store, the later callbacks in §6 and §7 must be rewritten in the same pass, and the writer should mark them now (a list in the consequential-edits file is enough) so the cut is one decision and not five.

**3.2 (should). The scale paragraph is a number dump.** "Its first commit landed at 22:51 UTC…" holds nine numbers in five sentences (commit time, end time, elapsed time, 2,718 commits, 26 roles, 72, 99, eight subjects and twenty lessons planned, 1,283 lessons in 14 subjects, 720 published). It reads as a press release and dates fastest. *Suggestion:* keep the three numbers the chapter's argument later uses: under five days; 26 roles growing to 99; 1,283 lessons in 14 subjects against about twenty planned (the plan-versus-actual pair is the one that carries meaning, because §6 needs it). Commits, the hour of the first commit and the 72 can go to the source map.

**3.3 (keep).** "testimony from a worker who no longer exists: check what you rely on." "There are 269 of them." is the right amount of the disk-is-memory idea: one clause, no Chapter 5 recap.

**3.4 (could). The token paragraph ends on "The records hold no figure for money."** Good. Ask 11 after it is the right ask in the right place.

### 4. "Built From the Book"

**4.1 (keep; must not be touched).** "When a company is assembled from a book's instructions, finding the book inside it is about as surprising as finding flour in the cake." and "If anything emerged, it is in the gap between what the file said would happen and what did." This short section is the chapter's thesis and the rule the remaining sections obey. It is placed correctly: after the reader has seen the gate work, before they are tempted to take anything as confirmation.

**4.2 (should). "which is an awkward thing to have to point out about your own book" writes a feeling for the author.** It is the one first-person *experience* clause in the press paragraph (the rest is argument, which the brief allows). *Suggestion:* end the sentence at "is not a copy of it", or keep it and let ask 17's comment ask the founder to confirm the clause too. Same family, lower stakes, for the founder's read: "the first claim in it I would check" (§1), "quotes one of my store sentences back at me" (§7), "I would not soften either half" (§7). Those are stances consistent with the book; I would keep them, but the founder should know they are the writer's.

### 5. "The Book Comes Back to Bite Me"

**5.1 (keep).** The three bites are the right three and they bite: one coordinator choosing about 99% of the work in a twenty-lane design; building at 8% of a day's tokens; and a rule that was a wish. The deploy story is the best-told story in the chapter: "wrote a conscientious commit message saying so", "to mention them it quoted the marker", "while he was being told nothing had been deployed", "That part was luck.", "nothing listens for the word any more." The counterweight ("Against those three, a count.") is correctly sized and correctly fenced ("It cannot show that 'checked' means more than one copy of a model agreeing with another.").

**5.2 (should). Translate the residual company register.** The brief bans "lanes"; the section uses it three times outside the retrospective's quotation ("with twenty lanes, each with a manager", "the lane's manager"), plus "dispatches", "dispatcher", "dispatched", "testimony-grade", "backfilled", "promoted it to production" and "Its fifth why". *Suggestion:* keep "20 lanes" inside the quoted sentence only; outside it, "twenty areas of work, each with a manager", "sent work", "the manager responsible", "put it live", "the last of its five whys" (or "its root cause"). "Testimony-grade" and "backfilled" go with 5.3.

**5.3 (should). Every evidence paragraph ends on its chain of custody.** The hub paragraph ends "Those are its counts at the time, and it labels its own table testimony-grade. The log was backfilled afterwards, so they cannot be recomputed from today's files, though every dispatch in today's version of that window still names the same actor." The cost paragraph ends "Those are the company's numbers, which I have not recomputed." The deploy paragraph ends "The hosting service's own commit statuses show all of this, and a script in the press's evidence folder reruns the old filter…" The same pattern returns in §6 (the harness) and §7 ("Those words reached the file second-hand…"). Each is honest; together they make the reader audit instead of read, and the section is the longest in the chapter (about 890 words of prose against a 750 target). *Suggestion:* the evidence rule is already stated once in §2 ("The witnesses that are not the model are few…"). Lean on it. Keep one short category clause per bite, in the brief's register ("the company's own count, which I have not recomputed"; "a script reruns it"), and move the rest (backfilling, what today's log still shows, who transcribed whose words) to the source map and the fact-check. Where an AUTHOR comment already carries the same caveat (the "as an agent transcribed it" clause in the cost paragraph; "Those words reached the file second-hand" in §7), the in-text caveat can go the moment the founder confirms the quotation.

**5.4 (must). The press is named three times; the brief, the commission's objection and the study all say once.** §4 names it as the honest limit, which is right. Then "a script in the press's evidence folder reruns the old filter" (§5) and "So the press wrote a new harness" (§6) make the press an actor in the evidence. That is the hall of mirrors R5 warned about: the reader is now watching the book's publisher verify the book's subject. *Suggestion:* keep the facts, drop the actor. "A script reruns the old filter against the saved messages and reaches the same verdict, so this incident is run as well as recorded." In §6: "A new harness, written for this book, reproduced 15 of those 22 bugs exactly…" The §6 fence ("The planters and the harness writer were all copies of one model.") already covers who wrote it.

**5.5 (could). The hub is all aggregate.** The other two bites have a moment (the founder's complaint; the commit message). The hub has only the retrospective's numbers and one quoted sentence. If the record holds one concrete dispatch (one specialist's task chosen by the coordinator on a day a manager was supposed to decide), one sentence of it would make the 99% visible. Only if it is on record as it happened; no composite.

**5.6 (could). "old advice about language models wearing new clothes" follows "one witness wearing different coats" from §2.** Two clothing figures for the same idea in one chapter. And the advice's source in this book (the old chapter's section heading) is gone, so "old advice" now reads as general wisdom, which is fine. *Suggestion:* drop "wearing new clothes"; "Let the LLM narrate. Do not let it declare reality." can stand without a frame.

### 6. "Willing to Lose"

**6.1 (keep).** "When I designed the store, the first test I wanted was deliberately boring… The company went to fourteen subjects in its first week." is the sharpest juxtaposition in the chapter: the author's own published advice against his own company, with no comment. The must-keep line is verbatim and "Otherwise it is branding." is earned by what precedes it. "The company has eight numbered experiments, and none of them has a result." is the right flat sentence.

**6.2 (should). The planted-bug paragraph is one paragraph doing three jobs** (what was run; what it shows; what it does not show and which test has not been run), at about 190 words. *Suggestion:* split after "each with exactly the failing count the record printed." First paragraph: what was run and its result. Second: "That shows the tests can fail. It says nothing about…" through the fence. With 5.4's change, the press drops out of it.

**6.3 (could).** "Its first objection, that 26 roles was heavy for 17 lessons" sits close to "about twenty lessons for the quarter" in §3. Two different documents, two different numbers, near each other; a reader may think one is a slip. One word of attribution in either place ("the vision's twenty", "the founding decision's 17") would settle it.

**6.4 (should). The chapter never notices that the company is the opposite of fluent autonomy.** Chapter 10, one page earlier, wanted a system that "forms the institution a request needs… and takes it down when the work is done", and warned that bureaucracy's "usual failure is that it never comes down." This chapter then presents a permanent organisation of 99 roles whose machine eats 92% of a day's tokens, and says nothing. The reader will notice. *Suggestion:* one sentence, not an argument, where the machine-around-the-lesson bite lands in §5, using the reader's memory and not a chapter number: the company is the institution standing permanently, and this is what it cost. Do not resolve it and do not reach toward the Scaffolds page; that payoff is the page's.

**6.5 (could). "All of these roles run on one developer's models"** (§3). "Developer" will read as a software developer to many readers. The brief's word was "vendor": "one vendor's models, rented by the token."

### 7. "Written Where Someone Can Argue With It"

**7.1 (keep).** "so for now the fourth line of the company's objective measures nobody"; "Fresh picks" where most products would say "For you"; "a number with four zeros"; "Nobody knows the answer yet, including the company." The pressures (a vertical feed, an ad slot, ten thousand lessons) are stated and left open, as the shape required. The Safari waiver is a real scene with a real cost ("iPhone users see the mirror-image knot after 'Turn over'") and the owner's switch is stated plainly, without scandal: "The objection kept its consequence on paper, and the owner held the switch."

**7.2 (could). "it teaches the payoff"** is company vocabulary (the lesson's point). A cold reader will stumble on "payoff". *Suggestion:* "it teaches the idea it promises", or whatever the objective file's plain gloss is.

**7.3 (should, linked to 3.1).** "The best idea in the store was about the objective. If it is not written down where someone can argue with it, it enters through invisible overrides." This is the section's foundation and the reader has not met the store's objective. With 3.1 done, this becomes a callback. Without 3.1, it needs one more sentence of what the store's objective was.

### 8. "The Student Has Not Been Asked"

**8.1 (must). Cut the recap paragraph, which admires the machine and spends Chapter 12's line.** "So this is what one founder and about a hundred roles of agents did in under five days: more than a thousand lessons, a checked claim behind every factual sentence of the ones marked published, gates that held, and a record honest enough to show where its own rules were wishes. It is a bet that this kind of capacity can be built to teach as well as to answer, and the bet is unmeasured." Three problems. (a) It is the "closing recap" the brief bans, told after a chapter that showed. (b) "a record honest enough to show where its own rules were wishes" is praise of the company's honesty written by a press that shares its model and admitted it two sections ago; it is the one place the chapter ends on the machine admiring itself (R5). (c) "if we build it to teach as well as to answer" is the last line of Chapter 12's "Beyond Comprehension"; using it here first turns Chapter 12's conclusion into an echo. The brief asked for the teaching condition in one sentence; it did not ask for Chapter 12's words. *Suggestion:* delete the first sentence. If the bet must be said, say it in this chapter's terms and let the ending's image carry it: the company's own guess is still waiting for its reveal (which the last paragraph already says, better). The ask-10 comment then sits directly before the last paragraph, as planned.

**8.2 (keep; must not be touched).** "Simulated learners find problems; only people can show that a lesson teaches." `"humanLearners": []` used once, as the punchline the brief hoped for. "That is a fair guess about adults, made by something that is not one." "The company's reviews are seeing, and they are not even seeing a person." The heading quietly pays Chapter 3's "The student has not yet been asked." Leave it unexplained.

**8.3 (should). The ending says its point twice.** §7 ends "A learner can open the sheet and see what any sentence rests on. She has no way to amend what the minute is for." The last paragraph repeats it: "The person it is for has not been asked, and if she were, she could open every claim and change none of the purpose." *Suggestion:* keep the first two sentences of the last paragraph exactly ("The company has asked a thousand times for a guess before it would show anything. Its own guess, that a minute like this teaches somebody, is still waiting for its reveal."), which pay off the title and the opening; cut or shorten the repetition ("What the minute is for is written in a file the founder owns. The person it is for has not been asked."); and end on the question. The question is right: it hands Chapter 12 its subject and does not answer it.

**8.4 (should, owner head of book for the founder). Keep the ask-10 answer short.** Chapter 12's "What Are Humans For?" opens on the author's profession ("LLM-as-a-judge looked like a threat to my profession") and argues it for pages. If the founder's answer to ask 10 lands here at length, Chapter 12's section opens on a repeat. *Suggestion:* the cover note asks for one or two sentences about what running the company did to his attention and his day, and leaves the future of the profession to Chapter 12.

**8.5 (could, owner whoever keeps the register). Register the heading as a proposed payoff.** "The Student Has Not Been Asked" answers `03-deep-mode.md` "The student has not yet been asked." Register rule 3 says new material that plants or pays a seed is added to the table. Proposed, not confirmed; do not explain it anywhere.

---

## 4. What is told rather than shown

Shown, and the chapter's strength: the opening card; claim c3 followed to its sheet; the two claims verified under one role name; the knot rule caught backwards; the deploy commit message; the Safari waiver; the empty field.

Told, and worth changing: the scale paragraph (3.2); the hub as aggregate only (5.5); "That is the system working as designed." (§7, acceptable because the next sentence shows it); the recap (8.1). Told and fine: "The book's own warnings came true against the design built to heed them." is a signpost, but it is one line and the three cases follow at once.

## 5. Opening and ending

**Opening:** do not touch. It is the product, on the page, in the second person, with the author arriving only in a joke about the eighty seconds, and the agents only in the last paragraph. It also does the work of the hand-in from Chapter 10 without saying so.

**Ending:** the last two sentences of the chapter's argument ("The company has asked a thousand times…", "…still waiting for its reveal.") are the best close the chapter could have without a real learner, and they make the title earn itself. They are currently buried under a recap before them (8.1) and a repetition after them (8.3). Clear both, and the ending is done. If the founder runs the five-learner test, the person's guess replaces the empty field, as the comment says; the reveal sentence should survive either way.

## 6. Structure and pacing, section by section

| § | Section | Prose words (approx.) | Pacing |
|---|---|---|---|
| 1 | Ninety-Nine Percent Accurate | 520 | Right. |
| 2 | Nine Claims Behind One Minute | 570 | Right; dense in the last two paragraphs, but they are the chapter's honesty. |
| 3 | A Company in a Week | 340 | Too thin where it matters (the store, 3.1), too thick where it doesn't (numbers, 3.2). |
| 4 | Built From the Book | 280 | Right; short is its strength. |
| 5 | The Book Comes Back to Bite Me | 890 | Long, and slowed by provenance tails (5.3). The deploy story earns its length; the hub paragraph does not. |
| 6 | Willing to Lose | 400 | Right, once the bug paragraph is split (6.2). |
| 7 | Written Where Someone Can Argue With It | 560 | Right. |
| 8 | The Student Has Not Been Asked | 440 | Right, minus the recap (8.1). |

Order: I considered moving "Built From the Book" ahead of "A Company in a Week", so the circularity is admitted before the scale is given. I recommend against it: the reader needs to know the company exists and how big it is before being told what its resemblance proves, and §2 already carries the fence for the one catch it reports.

Length after the musts and shoulds: roughly 3,800-3,900 words of prose, inside the brief's band once the AUTHOR comments are counted, and below it if they are not. That is fine. Do not pad back to 4,800.

## 7. What is working and must not be touched

- The whole of "Ninety-Nine Percent Accurate".
- "And now the camel comes back…" (registered seed, verbatim, unexplained).
- The fence paragraph and the role-name gate paragraph in §2.
- "Built From the Book", especially "flour in the cake" and "the gap between what the file said would happen and what did."
- The deploy story in §5, from "The third is a rule that turned out to be a wish." to "nothing listens for the word any more."
- "A philosophy of emergence should be willing to lose an A/B test. Otherwise it is branding." (verbatim; the Part V epigraph and the Zen depend on it) and the store-test-versus-fourteen-subjects juxtaposition.
- "so for now the fourth line of the company's objective measures nobody."
- The Safari waiver as told, and "the owner held the switch."
- The last section's quotations and its two best lines (8.2), and the first two sentences of the final paragraph.
- The headings "The Book Comes Back to Bite Me" (must-keep) and "The Student Has Not Been Asked".
- Every AUTHOR comment, including the 11:7 comment moved verbatim. None has a recorded acceptance; they stay until the founder answers.
- The title "Guess First": the final paragraph pays it off. (My earlier lean stands: *First Light* only if a real learner is reported.)

## 8. Route

Writer revises against the five musts and the shoulds, and answers in writing any should it declines. Head of book sends the founder the ranked asks (0.1) and the two Chapter 12 edits (0.2) together with the revision, not after the panel. Then the panel as briefed (arc, LLM tells, ideas, eggs, prose). I should not sit on the panel for this chapter (role rule: I may not review my own letter's outcome).

---

## 9. After the writer's note

Read after sections 1-8 were written (`press/books/system-3/proposals/2026-10-17-ch11-writer-note.md`), with a check of the consequential-edits file for the Chapter 12 rows. Nothing in it changes a severity above. What it adds:

- **The press count (5.4) contradicts the note.** Decision 10 says "The press is named once, in §4". The text names it three times: §4, "a script in the press's evidence folder" (§5), and "So the press wrote a new harness" (§6). The writer likely counted the deliberate naming and not the two incidental ones. Finding 5.4 stands as a must.
- **Chapter 12 (0.2) is already listed** as M2 (12:79) and M3 (12:235) in the consequential-edits file, with proposed wording I would accept. The must is therefore about routing: the head of book should bring M2 and M3 to the founder with the revised chapter, not after it.
- **"Teach as well as to answer" (8.1): I disagree with M6.** The writer argues the phrase "now has a referent" and asks review-arc to judge. My view: the referent is welcome, the words are not. Chapter 12 closes "Beyond Comprehension" on that phrase as its own discovery ("a condition I did not see when I first drew the curve"); arriving at it a chapter late makes Chapter 12 sound as if it is quoting Chapter 11. Say the bet in other words here, or let the reveal sentence carry it. Leave M6 for review-arc as the writer asks, with this disagreement attached.
- **The writer's own doubts, answered.** (a) §4's "awkward thing" clause: agree, finding 4.2. (b) §5 reads most like a report: agree, and the cause is the provenance tails, not the three bites (5.3); do not cut a bite. (c) "some of it has medical degrees": keep. It is a joke that carries the Harvard point, which is the book's house style; the founder can cut it on his read. (d) "The best idea in the store was about the objective": keep as a stance, founder confirms (finding 7.3; it depends on 3.1). (e) "asked a thousand times": keep. Read against an empty `humanLearners` field it is sharper, not looser: a thousand cards asking, nobody answering. The fact-checker should only confirm that "a thousand" is honest against both 1,283 lessons in the repository and 720 published.
- **"If the panel finds the draft thin, add to §1 and §7."** Please do not add to §1; it is finished. If the prose grows, let it grow from the founder's answers (0.1) and from finding 3.1, not from more lesson or more pressures.
- **Safari and iPhone named.** The note offers generalising them ("one phone's browser"). I would keep them: the specific consequence ("iPhone users see the mirror-image knot") is what makes the waiver a scene. The founder decides (D5).
- **Lines the writer added from the lesson's own code** (the empty first hundred with one positive; the eighty-second budget) are among the best details in §1. They are W items; the fact-checker should rerun them before anyone polishes the sentences around them.

## Handoff

- **Changed:** wrote this letter only. No manuscript, brief, register or company file touched; nothing committed. Commands run were read-only (`check-tells.py`, `check-eggs.sh`, `git show`).
- **Believe:** (high) the shape is right and the opening and ending are the chapter's strengths; (high) the five musts are the gap between this draft and a panel-ready one; (medium) the store passage can be made to work from the author's existing sentences without new autobiography (3.1); (low, the founder's call) whether the chapter is finished without a real learner.
- **Next:** writer-system-3 revises against the musts and shoulds; head-of-book-system-3 sends the founder the ranked asks (0.1) and consequential edits M2/M3 (0.2) with the revision; then the panel. I do not sit on the panel for this chapter.
- **Blocked on the founder:** asks 6, 2, 5/4 and 3; quotation permissions; M2 and M3.

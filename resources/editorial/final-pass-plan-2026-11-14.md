# Final-pass plan: making *System 3* publish-ready

14 November 2026, revised the same day for the author's current Chapter 11 ("The System 3 Company") and Chapter 12. Based on a complete read of the 31 files in `book-design/curated/book-order.json`
(about 67,000 words of main text, 12,000 of back matter and references), the editorial records in
`resources/`, and the repository's own checks. Nothing in the manuscript was changed.

## Status after the chapter-by-chapter pass (14 November 2026)

Done, with the author's approval at each step: the Preface, Chapters 1 to 12, both interludes, the
reveal page and the back matter. Chapter 11 is now "The System 3 Company"; "Interlude: The City"
follows Chapter 12 and carries the handoff to the fable. Chapter 13 is untouched. No `AUTHOR:`
comments remain. The seed check and the reference validator pass on all 32 files.

Still open, none of it prose:

- Fourteen screenshots for Chapter 11 and the City interlude are not in the repository; five old
  illustrations and the opener for Chapter 11 belong to the retired store chapter.
- Front matter (title, copyright, dedication, acknowledgments) does not exist.
- The 2026 sources and the lessons-company figures in Chapter 11 and the interlude have not been
  independently checked. One visible inconsistency: "109 became 39" after parking seventy-two roles.
- Employer clearance; a cold read by a person; a proofread on typeset pages.
- The video briefs in `prompts/notebooklm/` are stale for every edited chapter.

The sections below are the original plan and are kept as the record of what was proposed.

## 1. Where the book stands

The argument holds from the preface to the scaffolds page, and each chapter's closing question does
open the next. Chapters 3, 4, 5, 6, 7 and 10 and the interlude are at publication quality. The
remaining work is of four kinds:

1. **Unfinished business in the files.** Twelve `AUTHOR:` requests are still open in seven chapters,
   although `REVISIT.md` records the manuscript as proofread-ready. Several mark real holes on the page.
2. **Chapter 11 is new and not yet in the repository.** The author's current file, "The System 3
   Company", replaces both the store chapter on `main` and the "Guess First" draft on
   `ccr-fd4ebbbc-p06k8x`. It is the strongest chapter in the second half. It needs an ending, a
   fact-check and the edits it forces elsewhere (§4).
3. **An overloaded closing chapter.** Chapter 12 makes twelve moves in 6,600 words and ends twice.
4. **Front matter, clearance and a date freeze.** None of these has been started.

No chapter needs rewriting. The plan is five passes, in this order: author material, structure,
line edit, verification, production.

## 2. Decisions only the author can make

These block the passes below. My recommendation is given for each.

| # | Decision | Recommendation |
|---|---|---|
| D1 | The open `AUTHOR:` requests (list in §5) | Answer those marked *needed*; delete the ones marked *optional* and close them. |
| D2 | Is the Chapter 6 grocery company imagined, composite or disguised? `REVISIT.md` calls the Ines thread "explicitly imagined"; the Note on Evidence says the company stories "come from my experience". The chapter itself opens as reportage. | Say it once in the chapter ("Here is a company I have assembled from several") and make the Note on Evidence match. |
| D3 | Chapter 11: which version | "The System 3 Company" (the author's current file). Retire the store chapter and the "Guess First" draft. |
| D4 | Chapter 12: keep or compress "The Answer to Derrida" | Compress to about 250 words. It is the section least needed by the arc and the most exposed to specialist criticism. |
| D5 | Chapter 13: Claudit's introduction ("the hottest agent", the hair flip) | Author's call; the chapter is protected. This is the one line an unsympathetic reader will quote. |
| D6 | Freeze date for facts | Keep "September 2026" in the preface and verify every 2026 event once against that date (§7). |
| D7 | Index | A names index only. About 150 people are named and the back matter already points readers to them. |
| D8 | Employer clearance (Zalando in the bio; Amazon in Chapters 4, 5, 7 and 9) | Start now. It has the longest lead time and no other pass depends on it. |

## 3. The arc, part by part

**Preface and Part I (Chapters 1–3).** The strongest opening is already there: coffee, cathedral,
loose cable. Chapter 1 is the weak link because every example is imagined and the AlphaGo section is
a one-sentence stub. Chapter 2's central scene, coming back from coffee, is told from a distance.
Fixing those two things with first-hand detail does more for the book than any other edit.

**Part II (Chapters 4–5) and the reveal.** This is the keystone and it works. The reveal page has a
paragraph out of order (§4). Chapter 5 is long but every vignette is doing a job; trim sentences, not
stories.

**Part III (Chapters 6–8).** Chapter 6 is the best story in the book and needs its status stated
(D2). Chapters 7 and 8 lean on reported work. With the new Chapter 11, the Chapter 7 store becomes
the book's only store and can stay as it is.

**Interlude.** Leave it alone.

**Part IV (Chapters 9–10).** Chapter 10 is the intellectual high point. It carries 14 "Chapter N"
cross-references, seven times the repository's own target; half can go. Chapter 9 reads well; its
applied-scientist paragraph is repeated nearly verbatim in Chapter 12.

**Part V (Chapters 11–12).** The new Chapter 11 changes what this part can be. The book's own
architecture was built as a company, run for a month, and put against one strong agent, which won or
tied almost every time. The chapter reports that against its author, revises Chapter 5's claim about
specialization, and finds what survived: a check held outside the team that made the work. That is
the part-page epigraph ("willing to lose an A/B test") paid in full. Chapter 12 then needs D4, a
shorter "What Are Humans For?", and four sentences corrected because the reader has now watched the
author run a hundred agents. Its handoff paragraph to the fable has been cut in the current file,
which fixes the multiple endings.

**Chapter 13, scaffolds, back matter.** The fable and the scaffolds page land. The back matter is in
an order that makes the afterword refer forward twice, and "The Ideas Behind System 3" is in a
different voice and has broken note numbering (§6).

## 4. Chapter by chapter

Line numbers are for the files as of commit `71ac730`.

### Preface
- Ready. Keep every seed.
- The reference note says "Chapters 5 and 6 examine the reported work". The Navier–Stokes work is not
  examined in either; only Chapter 12 alludes to it. Correct the note.

### Chapter 1: Why I'm Betting on AI Agents
- Four open requests (lines 44, 52, 82, 100). *Needed:* line 52. "When Search Moved Up a Level" opens
  with a single sentence about AlphaGo and moves on; give it two sentences of what you saw, or cut
  the AlphaGo line and start at the language-model paragraph. *Optional:* the other three.
- The asymmetry paragraph (line 96) and Chapter 12's "library card and a good afternoon" paragraph
  say the same thing in nearly the same words. Keep the full version in Chapter 12 and reduce
  Chapter 1 to one sentence that plants it.
- Straight apostrophes in four places.

### Chapter 2: The Algorithm Vortex
- *Needed:* line 199. What you found when you came back, how long the run took, what the bands
  looked like.
- *Needed:* line 189. How the evaluator was protected. The chapter says an instruction "does not make
  the file immutable" and then does not say what did.
- Add a short methods note: model, number of runs, duration, who "we" is. The text moves between "I"
  and "we" without saying.
- Confirm that the ten replaced figures are labelled as redrawn if they were not produced from the
  original run data. The 30 September art record shows them resolved; it does not show the data
  source.

### Chapter 3: The Vibe Coder's Seat
- Line 7–9: "Then I asked for an educational demo. Most of the things I actually want AI to help me
  with are not like that." *That* points at the demo; it should point at circle packing. Reorder the
  two sentences.
- "Stubbornly Human" spends about 2,000 words on the history of AI coding before the layers arrive.
  Trim 500–700 words from the copy-and-paste to football-academy stretch.
- The Brian Cantwell Smith passage ("building it between evaluators") is the thesis in miniature and
  nothing later returns to it. One callback in the reveal or in Chapter 10.

### Chapter 4: System 3
- The open request at line 287 refers to "the scientist and designer sentences below", which no longer
  exist. *Needed* if you have a real case of creative distrust from the review-ranking years; the
  section is otherwise the thinnest in the chapter. If not, delete the comment.
- The second code block for 13579 is marked "shown schematically" and contains `...`. Either show the
  real change or describe it in prose.
- Otherwise ready. The camel frame pays off.

### Chapter 5: The Society of Agents
- "Then Amazon made me an offer, and the offer was reviews" (line 132) arrives without a bridge from
  the bureaucracy section. One sentence of entry.
- The author's career is introduced or re-introduced in Chapters 4, 5, 8, 9, 10 and 11 in slightly
  different terms ("eight years", "years", "much of my career"). Let Chapter 5 carry the story and
  make the others consistent short references.
- This chapter has the highest aphorism rate in the book (38% against a target of 30). Remove the
  one-line paragraph closers that restate the paragraph above; keep those listed in the seed register.
- One optional request (line 91): close it.
- Low-confidence check: the Newton anecdote is attributed to John Conduitt; the recollection is
  usually given as Catherine Conduitt's, recorded by him.

### Reveal page
- Paragraph four ends on the question about the price of another afternoon. Paragraph five then
  begins "It is messy", where *it* means science, not the price. Move "It is messy…" up to follow
  paragraph two or three, so the page ends on the question that Part III picks up.
- Add one sentence promising that the strongest objections are taken up in Chapter 10.

### Part pages
- Part II carries a question, Part III carries 200 words of prose, Parts I, IV and V carry only an
  epigraph. Choose one form. Recommendation: epigraph plus one question on each, and move the Part
  III prose into the opening of Chapter 6 or cut it to its first line.

### Chapter 6: Pattern Language
- D2.
- Dialogue and contractions use straight quotes throughout, unlike the rest of the book (16
  instances).
- "Two in the morning" appears five times. Keep the heading and two.
- "Names Travel Faster Than Reasons" and "A Reader That Can Act" stack eight citations in about 600
  words between two stretches of story. Cut Voyager or Feigenbaum to a clause each.
- The YAML blocks are right for this chapter. Check that they fit a 6×9 line without wrapping.

### Chapter 7: Recursive Self-Improvement
- One optional request (line 43): close it.
- "Chapter 12 returns to the same rule" (line 200) is a long forward reach; shorten to "the last
  chapter".
- Low-confidence check: whether Lee Sedol left the room *after* Move 37 or was already out when it was
  played. Accounts differ.
- The 2026 figures (52× training speed-up, Dream-RSI, Agentic Harness Engineering) go on the freeze
  list.

### Chapter 8: Scalable Oversight
- The ExploitGym opening is the best in the second half. The whole account rests on two sources; both
  go on the freeze list, with a second read against the text.
- "Change Their Mind Mid-Sentence" and "Keep the Budget Out of Reach" are one or two paragraphs each
  under full headings. Either fold each into its neighbour or give each the manager's-eye sentence
  the other sections have.
- "Her" for the new employee begins at line 27 without introduction; "it" is used two paragraphs
  earlier. Pick one.
- "The note on evidence proposes a small experiment": keep; it is the book's only committed test.

### Interlude
- Ready.

### Chapter 9: The Desire Layer
- One optional request (line 53). If there is a real instance of a recommender you built changing
  what users wanted, this is where it would matter most in Part IV. Otherwise close it.
- The applied-scientist paragraph ("two scarce skills") duplicates Chapter 12's "What Are Humans
  For?" opening. Keep it here; cut it there to one sentence that refers back.
- The layer is "Layer 4—Desire" in Chapter 3, "desire layer" in Chapter 4 and "The Desire Layer"
  here. Fine; make the Chapter 4 table and the Chapter 3 list use identical wording.

### Chapter 10: Fluent Autonomy
- "The review of 255 flagged passages" is mentioned in "What the Fold Forgets" before the review is
  introduced in "Creative Distrust". Move the mention or the introduction.
- The paragraph of counts (150, 81, 18, six) is accurate and sums correctly, and is more process than
  a reader needs. One sentence.
- Halve the "Chapter N" references; most of the callbacks are recognisable without the number.
- "Where This Could Be Wrong" should state the narrow form of the thesis in one sentence: the claim
  is about work where checking is expensive or ambiguous. It is currently spread over three
  paragraphs.

### Chapter 11: The System 3 Company (new; replaces The Store That Builds Itself)
Read from the author's uploaded file (5,421 words). It is not in any repository I can reach. The
book's prose check passes it on every measure (aphorism rate 22%, one cross-reference).

What works and should not be touched: the founding message quoted as typed; the Greenland catch;
the org chart as a feather; the post-mortem that names "founder pressure"; the sealed envelope; the
single agent hiring the company's four checkers from its own job descriptions; Jeff.

What it needs:

- **The student has still not been asked.** Chapter 12 now says "Chapter 11's lessons company still
  needs evidence from real learners", and Chapter 3 planted "The student has not yet been asked".
  Chapter 11 never says whether a person has used a lesson. One plain paragraph, in the Border
  section or at the end. If learners have been tested, report it; if not, say so.
- **An ending.** It stops on the folder of job descriptions, which is a good image and not a
  conclusion. The reader needs two or three sentences on what the month did to the book's claim:
  the default is one agent, structure forms for a reason, and the piece that earned its cost was the
  referee nobody inside controlled. The material is already in "The Institution Inside One Agent";
  the last page should land it and leave a question for Chapter 12.
- **Chronology.** The sections run 12 October, 14, 18, 1 November, back to 16 October, 20 to 29,
  early November, then the compiler race, then 22 October. Each move is justified by the argument
  but a reader loses the month. Either add a small dated timeline as a figure or put the lessons
  benchmark before the compiler race, since it happened first and the chapter says so.
- **Names.** Nine agents are named. Ada is quoted in the third paragraph before she is introduced
  in the next section. Vera, Bram and Wen appear once each; use their roles.
- **Fact-check.** Every figure comes from the companies' records and none has been checked by
  anyone but the writer. Three to check first: "across five benchmarks" (the principles file in
  `system3-meta` lists six rounds, B5 to B10, before the orgs caught up); the SQLite result ("half a
  point" here, 1.2 points in that file, possibly a different run); and the cost multiple in the
  lessons benchmark, on which the tripwire sentence depends.
- **Trim about 300 words** from "The Envelope": the SQLite race and the paragraph on Teo delay the
  compiler race the section is named for.
- **Reference.** The chapter cites only note 2 (Pearl). Note 1 (`ref-11-slate`) is now uncited, which
  fails the build; remove it and renumber.
- **Seed.** "And now the camel comes back" is gone, so the seed check warns. The camel is still paid
  off ("The camel at Krka has become a data structure", and the unpublished hump lesson). Update the
  register to the new anchor.
- **Images.** Seven screenshots are referenced under `book-design/curated/assets/company/`, a folder
  that does not exist on `main`. They need to be added at print resolution, and they are a different
  visual language from the rest of the book; the Note on the Illustrations needs one sentence.
- **Files that name the old chapter:** `book-order.json`, `provenance.json`, the references heading,
  five art anchors and the chapter opener (still a fashion store), `check-eggs.sh`, the NotebookLM
  sources.

Edits it forces elsewhere:

- **Preface.** "It is September 2026 as I write this." Chapter 11 runs from 12 October into
  November. Change the date or the freeze.
- **Chapter 5.** "The Society Gets Smarter by Making People Narrower" is now revised by Chapter 11
  ("for people, I still believe it"). One clause there limiting the claim to people would make the
  later reversal read as a result and not a contradiction.
- **Chapter 10.** Chapter 11 opens "I had ended the previous chapter wanting a referee". Chapter 10
  has that line three paragraphs before its end and then closes on the customer who "files no
  correction", which led into the store. Cut those last two paragraphs so Chapter 10 ends on the
  referee.
- **Chapter 10, "Where This Could Be Wrong".** It names the epistemic agent as the one institution
  designed on purpose. Add a half-sentence that a larger one follows.
- **Chapter 12.** Line 89 ("mentally hiring"), 235 ("A hundred agents is a picture") and 239 ("the
  work I want to do… I might have a collaborator") were written before the author built Meta, whose
  stated job is to create companies for a use case. Each needs a clause.
- **Note on Evidence.** New row for Chapter 11 (run, from the companies' records, with committed
  predictions and a referee; no real learners unless tested); exempt it from the "composites"
  paragraph; say whether "A Test Still to Run" has now been run in any form.
- **Afterword.** "My own experiments: small…" and "Thesis 1: … not yet run" are out of date.
  Chapter 11 quotes the company calling its token split "the book's first thesis, observed".
- **Part V page.** Keep. The epigraph is now the chapter's result.

Not found: the interlude about the city. It is not among the uploaded files or in any of the four
repositories. Chapter 11 does not mention the city; if the interlude follows it, the chapter's last
page is where the handoff belongs.

### Chapter 12: After Capacity
- D4.
- The handoff paragraph to the fable is cut in the current file, so the chapter ends on "how much
  more". Good. The seed register still lists "It requires an octopus" for Chapter 12; update it, and
  check that the "Alternative Ending" divider is enough introduction for Chapter 13 without it.
- "What Are Humans For?" runs about 1,100 words and covers ground readers will have met elsewhere.
  Keep the grammar-of-"for" passage, the dinner lines and the conflicting goods; cut about a third.
- Two requests (lines 125, 233), both optional. The scheduling community would be stronger with one
  real detail; without one, close them.
- Small errors: "In Chapter 5, I asked where the next thousand agent-hours should go" (Chapter 5
  asked who gets the next agent); "the yield-table forest and the grid city from this chapter's
  opening" (they are in "The Curve", not the opening); "ten thousand agents on one problem" is never
  attributed in the text, only in the note.
- Eleven "Chapter N" references; halve.

### Chapter 13 and the scaffolds page
- Protected. No line edits. D5 only.
- Check with a rights reader that the parody use of *The Matrix* terms and the named brands is
  acceptable to the chosen publisher or platform.

### Back matter
- **Order.** Current: afterword, Zen, evidence, ideas, illustrations, references, about. Proposed:
  Zen (it answers the scaffolds page), Note on Evidence, afterword, ideas, illustrations,
  acknowledgments, references, about. The afterword then refers back to the evidence note instead of
  forward.
- **Note on Evidence.** Reconcile with D2. Chapter 5's row says "argued from history" and omits the
  Amazon reviews memoir. Add one line on source concentration: much of the reported 2026 work comes
  from two companies.
- **The Ideas Behind System 3.** Different voice from the rest of the book, straight quotes
  throughout (35), and note numbers borrowed from other chapters, so the first note on the page is 2,
  followed by 13, 19, 36. Renumber for this appendix. Consider cutting Part I by half; it is a
  textbook summary and the afterword already names the inheritance.
- **Afterword.** Ready.
- **About the Author.** Ready, pending D8.
- **Acknowledgments, dedication.** To be written.

## 5. The open author requests

| File | Line | Asks for | Status |
|---|---|---|---|
| 01 | 44 | A real run that grew its own tools | Optional |
| 01 | 52 | What you saw when AlphaGo played | **Needed** |
| 01 | 82 | A sharper real mistake than the jacket | Optional |
| 01 | 100 | A real limit you dropped | Optional |
| 02 | 189 | How the evaluator was protected | **Needed** |
| 02 | 199 | The return from coffee | **Needed** |
| 04 | 287 | A real scene of creative distrust | **Needed**, or delete |
| 05 | 91 | Apprenticeship detail | Optional |
| 07 | 43 | A real story for the store's beats | Optional |
| 09 | 53 | A real instance of desire forming | Optional |
| 11 | — | Has a real person used a lesson, and what happened | **Needed** |
| 12 | 125 | Which group, which room | Optional |
| 12 | 233 | Detail for the workshop or irrigators | Optional |

Nothing is to be invented for any of these. An unanswered optional request is deleted, not filled.

## 6. Whole-book line pass

Do this after §4, once.

- **Typography.** One apostrophe and quote style. Straight quotes remain in Chapters 1, 5 and 6, the
  ideas appendix and the Zen page.
- **Chapter endings.** Six chapters end with a `---` rule and six do not. Remove or add throughout.
- **Cross-references.** Target under one per 1,000 words in every chapter. Chapters 8, 9, 10 and 12
  are over.
- **Aphorism closers.** Chapters 5, 7 and 12 are over the repository's target. Run
  `resources/editorial/check-tells.py` after the pass.
- **Bold coinages.** One bolding per term, at first definition, and none elsewhere.
- **Terms.** "Harness" is used for the fixed evaluator (Chapter 2) and for everything around the
  model (Chapter 3); Chapter 3 says so, and later chapters should use the Chapter 3 sense only.
- **Seeds.** `resources/editorial/check-eggs.sh` passes today. Run it after every pass.
- **Repository status lines.** `README.md` says Chapters 6–12 are works in progress; `REVISIT.md`
  says proofread-ready. Correct both when this plan is done.
- **Leftover markers.** Remove all `AUTHOR:` and `ART RESOLVED` comments from the print source, or
  confirm the build strips them.

## 7. Verification, clearance and production

**Facts.** Citations and reference anchors match (234 cited, 234 defined). The historical claims I
could check from memory are sound, with the two low-confidence items noted above. I could not verify
the 2026 events and they carry several chapters, so each needs one check against its source at the
freeze date:

- Preface: the C compiler and the Navier–Stokes announcement, including its current standing.
- Chapter 6: the Fermat formalization figures; Stellar Colosseum.
- Chapter 7: Dream-RSI; the training speed-up figures; Agentic Harness Engineering.
- Chapter 8: the ExploitGym and Hugging Face chronology; the nine-agent alignment study and its
  0.23 and 0.97 scores; the 2.4% figure; the authorship of the November 2025 reward-hacking paper.
- Chapter 9: the one-million-conversation analysis and its six percent.
- Chapter 12: the June 2026 model suspension and the token count.

The 1 October evaluation also asked for an acknowledgment of other uses of the name "System 3". I
found none in the manuscript.

**Clearance.** D8; the parody check for Chapter 13; permission or fair-use review for the longer
quotations (Fan Hui, the Instagram researcher, Planck); a statement on the generated illustrations
suited to the publishing platform.

**Front matter to write.** Half-title, title page, copyright page with ISBN and the AI-use statement
now in the Note on Evidence, dedication, contents, acknowledgments.

**Production.** Choose the printer; set bleed, spine and colour profile; build with
`pdf.py build --strict-art`; read one physical proof from cover to cover. The Chapter 5 Paged.js
experiment should be dropped or adopted before this step, not during it.

## 8. Order of work

1. **Author material** (D1–D5): commit the new Chapter 11 and its images; write its ending and the
   real-learner paragraph; answer or close the 12 other requests; decide D2, D4, D5. Start D8 in
   parallel.
2. **Structure:** the edits Chapter 11 forces (preface date, Chapters 5, 10 and 12, evidence note,
   afterword, build files); the city interlude once located; reveal paragraph
   order; part pages; back-matter order; Chapter 12 cuts; duplicate passages (1/12 and 9/12).
3. **Line edit:** §4 chapter items, then §6 across the book. Run both check scripts.
4. **Verification:** the §7 freeze list, references renumbered for the ideas appendix, then a cold
   read by someone who has not seen the manuscript.
5. **Production:** front matter, index, build, proof.

After step 3 the manuscript should be frozen; steps 4 and 5 correct errors and change nothing else.

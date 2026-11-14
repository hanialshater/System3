# Final-pass plan: making *System 3* publish-ready

14 November 2026. Based on a complete read of the 31 files in `book-design/curated/book-order.json`
(about 67,000 words of main text, 12,000 of back matter and references), the editorial records in
`resources/`, and the repository's own checks. Nothing in the manuscript was changed.

## 1. Where the book stands

The argument holds from the preface to the scaffolds page, and each chapter's closing question does
open the next. Chapters 3, 4, 5, 6, 7 and 10 and the interlude are at publication quality. The
remaining work is of four kinds:

1. **Unfinished business in the files.** Thirteen `AUTHOR:` requests are still open in eight chapters,
   although `REVISIT.md` records the manuscript as proofread-ready. Several mark real holes on the page.
2. **A second half that promises more first-hand material than it shows.** Chapter 11 announces a
   prototype and never shows it; Chapters 8 and 9 are mostly other people's work.
3. **An overloaded closing chapter.** Chapter 12 makes twelve moves in 6,600 words and ends twice.
4. **Front matter, clearance and a date freeze.** None of these has been started.

No chapter needs rewriting. The plan is five passes, in this order: author material, structure,
line edit, verification, production.

## 2. Decisions only the author can make

These block the passes below. My recommendation is given for each.

| # | Decision | Recommendation |
|---|---|---|
| D1 | The 13 open `AUTHOR:` requests (list in §5) | Answer the five marked *needed*; delete the eight marked *optional* and close them. |
| D2 | Is the Chapter 6 grocery company imagined, composite or disguised? `REVISIT.md` calls the Ines thread "explicitly imagined"; the Note on Evidence says the company stories "come from my experience". The chapter itself opens as reportage. | Say it once in the chapter ("Here is a company I have assembled from several") and make the Note on Evidence match. |
| D3 | Chapter 11: show the prototype or call it a design | Show one screen or session in 150 words. If nothing can be shown, retitle the opening as a design and drop "I built a prototype". |
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
(D2). Chapters 7 and 8 lean on reported work. Three different stores now appear in the second half:
the grocery company (6), the online store with a research agent (7) and the prototype store (11),
with trail shoes recurring in 7, 9 and 11. Make the Chapter 7 store and the Chapter 11 store visibly
the same imagined store, in one sentence each. That gives the second half a running case and costs
almost nothing.

**Interlude.** Leave it alone.

**Part IV (Chapters 9–10).** Chapter 10 is the intellectual high point. It carries 14 "Chapter N"
cross-references, seven times the repository's own target; half can go. Chapter 9 reads well; its
applied-scientist paragraph is repeated nearly verbatim in Chapter 12.

**Part V (Chapters 11–12).** This is where the book is least finished. Chapter 11 needs D3 and a 15%
trim. Chapter 12 needs D4, a shorter "What Are Humans For?", and one ending.

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
- One optional request (line 43): close it, and tie the store to Chapter 11 instead (§3).
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

### Chapter 11: The Store That Builds Itself
- D3. *Needed:* line 7.
- The subtitle "A Prototype Store" repeats the title. Replace or drop.
- Trim about 600 words. "Replayable" and "A Theory Losing Contact With Reality" both explain logging
  and library hygiene at design-document length.
- Name the store as the one whose research agent appeared in Chapter 7.
- "And now the camel comes back" needs four more words for a reader who put the book down between
  Chapters 4 and 11.

### Chapter 12: After Capacity
- D4.
- Two endings. "The Door After System 3" closes on the irrigators' Sunday evening, then on the
  author's wishes, then on "how much more", then hands off to the fable. Keep the irrigators, one
  personal paragraph, and the handoff.
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
| 11 | 7 | What the prototype did | **Needed** |
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

1. **Author material** (D1–D5): answer or close the 13 requests; decide D2–D5. Start D8 in parallel.
2. **Structure:** reveal paragraph order; part pages; back-matter order; Chapter 11 and 12 cuts; the
   Chapter 7 and 11 store link; duplicate passages (1/12 and 9/12).
3. **Line edit:** §4 chapter items, then §6 across the book. Run both check scripts.
4. **Verification:** the §7 freeze list, references renumbered for the ideas appendix, then a cold
   read by someone who has not seen the manuscript.
5. **Production:** front matter, index, build, proof.

After step 3 the manuscript should be frozen; steps 4 and 5 correct errors and change nothing else.

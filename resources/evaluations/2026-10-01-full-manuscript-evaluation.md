# Full Manuscript Evaluation — 1 October 2026

Scope: a complete read of all 29 files in `book-design/curated/book-order.json`
(about 67,000 words of main text, plus the appendices), in reading order. I also
spot-checked facts, with web verification for the 2026 events that fall after
the evaluator's knowledge cutoff. Earlier evaluations in this folder were not
consulted before reading, so this is an independent assessment.

---

## 1. Verdict

This is a serious, original and mostly well-made book. It has a real thesis,
a recognisable voice and an unusual honesty about its own evidence. The best
chapters (3, 5, 6, 7, 10 and the interlude) are publishable now. The book's
weaknesses are not superficial ones like typos or tone. They are structural:

1. **The thesis is stretched further than the evidence the author ran.** The
   book claims that "as we build autonomous AI, we keep rediscovering science
   as its architecture." The author's own experiments are small, early and
   mostly qualitative. The strongest support is other people's work, and much
   of that comes from one company.
2. **The book proposes about six decisive experiments and runs none of them.**
   At least one could be run cheaply from material already in this repository.
3. **The second half loses the first half's method.** Chapters 1–7 move from
   the author's own attempts to argument. Chapters 8 and 9 are mostly
   literature surveys with a hypothetical attached. Chapter 11's "prototype" is
   never shown.
4. **The ending may lose readers the book has earned.** The fable in Chapter
   13 is tonally risky and thematically opaque, and its framing invites
   misreading.

None of these needs a rewrite. All four need deliberate decisions.

---

## 2. The thesis, examined

### What the book actually argues

The book has a clean progression. A bounded problem with a cheap referee needs
almost no structure (Ch 2). Once judgment becomes expensive, judgment has to be
built between evaluators instead of inside one (Ch 3). Knowledge that has lost
its provenance is "epistemologically flat" (Ch 4). Populations of fallible
knowers need records, standards, specialists, independent witnesses,
instruments, provenance and allocation, and "we call it science" (Ch 5 and the
reveal). These features can be written down as testable patterns (Ch 6). When
the system edits its own method, the evaluator becomes constitutional (Ch 7).
Oversight then has to be scaled (Ch 8), purposes stay human (Ch 9), the
structure should assemble around intention (Ch 10), and the design gets
applied (Ch 11) and given a politics (Ch 12).

The progression is coherent, and each chapter's closing question does open the
next chapter. That kind of spine is rare in books of this genre.

### Where the thesis is vulnerable

**(a) The word "science" is elastic.** Chapter 10's first objection (line 131)
defends the choice of *science* over law or markets by defining science as
"the part of the institution that lets a claim lose even after people have
begun using it." That is a good definition. It is also broad enough that almost
any error-correcting institution qualifies. The reveal page leans the same way:
"System 3 is science, in that sense and no smaller one." A hostile reviewer
will say the thesis has been made true by definition. The book should say
plainly that the claim is about **defeasibility under expensive verification**,
which is the narrow and defensible version, and then show that the *specific*
devices of science reappear in agent systems:

- independence of witnesses
- pre-commitment of tests
- replication
- allocation to rival programs
- separating the instrument from the claim

Generic coordination devices such as locks, logs and loops don't count.

**(b) Some of what Chapter 5 "rediscovers" is operations, not epistemics.**
Carlini's repairs were a restart loop, lock files, progress files, sampled
tests, logs written to disk, specialists and CI. That is project management and
DevOps. Only the GCC oracle and CI are clearly epistemic instruments. Chapter
5 makes the mapping elegantly (the progress file as clay tablet), but the
mapping is the author's, not the builders'. The cleanest cases of
*rediscovery* in the book are elsewhere:

- the held-out evaluation in Anthropic's automated alignment researchers (Ch 8)
- Stellar Colosseum's rule that a single fatal flaw outweighs any number of
  favourable reviews (Ch 6)
- the read-only verifier and predicted-impact edits in Agentic Harness
  Engineering (Ch 7)
- Dream-RSI's refusal to reward plans beyond recorded history (Ch 7)

Those are stronger evidence, and they are scattered. A short passage gathering
them would do more for the thesis than another historical vignette.

**(c) Rediscovery or import?** Most of the people building those systems are
scientists. When a research lab adds a held-out set, it is importing science,
not rediscovering it. The book never faces this objection directly. Chapter
10's third objection ("I found what I was looking for") is close, but it is
about the author's bias, not the builders'. The objection has a good answer:
the *failures* that forced the imports were rediscovered. The agents really
did probe the evaluation API, and the cheating attempts really did occur in
2.4% of trajectories. The book should give that answer explicitly.

**(d) Chapter 10 is the book's intellectual high point.** "Five Ways This
Could Be Wrong" is honest and well argued. The answer to the Bitter Lesson ("it
cannot make the solver's assurance into independent evidence") is the single
best defence of the thesis. Consider seeding it earlier: a one-line promise in
the reveal that the strongest objections are coming would help the sceptical
reader through Part III.

### Strongest single passage the book under-uses

Chapter 3, line 301 (Brian Cantwell Smith): *"judgment… was never a private
faculty either. It is a person plus a tradition, plus other people positioned
to object, plus consequences… When I stopped looking for judgment inside the
evaluator and started building it between evaluators…"* This is the thesis in
miniature, and it appears two chapters before the thesis is named. Nothing
calls back to it. The reveal or Chapter 10 should.

---

## 3. Evidence audit

The Note on Evidence is a strength. Its labels are mostly accurate, but three
entries flatter the chapters they describe.

| Chapter | Labelled | What the text actually reports | Gap |
|---|---|---|---|
| 2 | Run | Scores (1.33→2.26, 2.08→2.45, best run 2.636). No model or version, number of runs, wall time or cost. "We" and "I" alternate without saying who "we" is. Ten technical figures are still missing (see `REVISIT.md`). | Add a short methods box. For a book about provenance, the flagship experiment has none. |
| 3 | Run; simulated learners | No numbers at all. Deep Mode is described ("So I tried giving that job to an orchestrator") but there's no comparison against a fixed Planner→Builder→Critic loop, no count of generations and no example artifact. | Either report something (generations, branch counts, before/after screenshots) or relabel as "Built; observations qualitative." |
| 4 | One small experiment | n=10, honestly fenced. The 57%→~33% correction is arithmetically right: 6,200 vs 2,690 lines, with one outlier of 2,720. | None. This is the model for how the rest should be reported. |
| 11 | Prototyped | Line 5 says "I built a prototype store." Line 7 says "This chapter develops the idea into a design… customers are imagined." What the prototype does is never shown. | Readers will ask what was built. Say in two sentences what exists (code, a replayed scenario set, a UI?) and what doesn't. |
| 10 | Lived | Line 117 says the second coffee test is "embarrassingly measurable," but no number is given. | See §6, recommendation 2. The data exists in `resources/evaluations/`. |

**Proposed but unrun experiments.** Each one is presented as the test that
would decide a claim:

- Ch 5:298 — critic with different evidence; a bad diagnosis planted in
  `progress.md`
- Ch 6:194 — reviewer with the pattern vs. without, using a generic "be
  careful" control
- Ch 7:138 — old vs. revised improver, matched budgets, held-out work
- Ch 10:117 — the repeated-corrections count
- Ch 11:209 — the composer vs. a static baseline vs. simplification
- Ch 12:271 — the irrigation weekend (explicitly a picture)

Proposing tests is good practice and the book says honestly that they haven't
been run. But the cumulative effect is that the book's own empirical content
ends at Chapter 4. **Running even one of the cheap ones (Ch 5's planted
diagnosis, or Ch 10's count) would change the book's standing.**

**Source concentration.** By my count, Anthropic is the primary source for the
key evidence in Chapters 5, 6 (Fermat, Riemann), 7 (RSI speed-ups,
tampering), 8 (almost every interpretability and oversight result), 9
(guidance, disempowerment) and 12 (the export-control suspension). The book
also discloses that it was written with AI help. Chapter 6 rightly discloses
that Alpöge is an Anthropic employee. It doesn't mention that Prove2Me's lead,
Tianyi Peng, is also reported as an Anthropic researcher. A single sentence in
the Note on Evidence acknowledging the concentration, and where possible a
non-Anthropic corroborating source for Chapter 8, would pre-empt the obvious
criticism.

**Shelf life.** Chapter 6 rests heavily on events from 10 August to 15
September 2026 (Riemann, Fermat, Navier–Stokes, Clay, Stellar Colosseum,
Dream-RSI). The writing is careful to date them, and reference 30 records a
status check on 13 September. Before going to print, re-check the Clay status
and the priority dispute. Consider adding "at the time of writing" to the
Navier–Stokes paragraph itself, not only in the notes.

### Fact-check results

**Verified directly or via reporting:**

- Riemann bound 41.6%→67.2%, 60 subagents, Lean-formalised, 10 August 2026
- Fermat formalisation in 11 days, about 30,000 theorems, Prove2Me, about six
  billion output tokens
- OpenAI Navier–Stokes: about 10,000 agents, 8 September; Clay's "deliberately
  unhurried" evaluation; the Buckmaster/Alpöge dispute
- Anthropic alignment-mitigation study: 28 August, 10 categories, about 1,600
  transcripts, 39 (2.4%) cheating
- Fable 5 / Mythos 5 suspension on 12 June 2026

**Checked against known literature, with no problems found:** Carlini's
compiler, Popper's 1967 lecture and its examples, the Qin standards and book
burning, Bromiley, Millikan/Feynman, Condorcet, Galileo/Horky/Kepler,
Boyle/Hobbes/Huygens, Wegener, Kitcher, the Newton brachistochrone account,
Hardwig, Higgs, OPERA, Alexander, Beck & Cunningham (1987), the Hillside Group,
OOPSLA '96, WikiWikiWeb, Kohavi's Bing case, AlexNet's figures, Azoulay et al.,
Planck's quote, the S3 outage, the Fire Phone write-down, the STOP and DGM
figures, the NAS/RegNet/RepVGG sequence, Thompson, Bastani et al., Tutor
CoPilot, Vaccaro et al., Dantzig–von Neumann, Belkin and Ostrom's cases.

**Minor points:**

- **Ch 6:251, "41.6 percent."** The prior record (Pratt et al., 2020) is
  usually cited as "more than five-twelfths," about 41.7%. The book follows
  Anthropic's figure, which is fine, but a mathematician may notice.
- **Ch 2, "slightly above the 2.635 reference."** Several groups reported
  values around 2.6359–2.6360 after AlphaEvolve. Check whether 2.636 is
  simply a rounding of the same known optimum. The existing fence ("would
  require matching problem definitions…") already covers this, but naming the
  later results would be more honest than leaving AlphaEvolve as the only
  comparison.
- **"System 3" as a term.** Others have proposed "System 0" and "System 3"
  extensions of Kahneman's dual-process framing for AI. I didn't verify any
  particular prior use, but a footnote acknowledging that the term has been
  used differently elsewhere is cheap insurance.

---

## 4. Chapter-by-chapter

**Preface.** Strong. The Leibniz hook and the "cathedral while you get
coffee" image are excellent, and "Your coffee is still too hot" earns its
callback in the About the Author. "At least one loose cable" is a nice seed for
OPERA.

**Ch 1 — Why I'm Betting on AI Agents.** It sets out the three slogans
cleanly. Its best ideas are "Control doesn't disappear. It moves upward" and
"ten agents sharing one assumption… a conga line." Its weakest paragraph is
line 101 ("terrifyingly efficient… cat obsession… missing socks"). It is the
only generic AI-futurism joke in the book, and it interrupts the careful
jacket-returns example on either side. Cut it. The joke density in the
opening is high (pineapple, octopus fish, product managers, the goldfish).
Most of it works, but the first three paragraphs make the book look lighter
than it is.

**Ch 2 — The Algorithm Vortex.** Clear and teachable. The "Immutable Harness"
and "Zero framework, with an asterisk" sections are strong, and the contract
section holds the chapter together. The problems are the missing methods and
the missing figures (§3). The chapter tells a progression from hill climbing to
evolution to MAP-Elites to code evolution, but only the hill-climbing and
evolution runs have numbers. MAP-Elites has none. In print, without the ten
diagrams, this is the chapter most likely to lose a general reader.

**Ch 3 — The Vibe Coder's Seat.** This is conceptually the richest chapter:
history of the harness, the five layers, Strategic Constraints ("No bars"),
pictures before code, natural language as an implicit metric, borrowed minds,
independent evaluators, the Cantwell Smith passage and the "cathedral on a
shopping cart" closing. It's also long (7.6k words) and has no measured
outcome. "Optimizing Something You Cannot Score" and "Independent Evaluators"
cover overlapping ground (metric gaming appears in both). One tightening pass
could save about 800 words. The file is named `03-deep-mode.md` while the
chapter is titled "The Vibe Coder's Seat". That's harmless, but other people
working on the repository may find it confusing.

**Ch 4 — System 3.** The camel frame works. Trust that "starts with a face" is
the book's most personal and memorable passage. The Astropy experiment is
reported with exemplary candour: the scaffold "seemed to produce discipline
before it produced capability." "System 3 isn't philosophy to me. It's
Tuesday" works because it is earned by the Amazon background. The Saussure →
Wittgenstein → octopus sequence is slightly redundant; any two of the three
would do.

**Ch 5 — The Society of Agents.** A tour de force of historical vignettes, but
there are about twenty of them: Carlini, Popper, Dr. Stone, the potter,
Mesopotamia, Qin, the Amazon text box, Bromiley, Millikan, Condorcet,
Zollman, Ibn al-Haytham, Peirce, Galileo, Boyle/Hobbes/Huygens, Duhem,
Wegener, Kitcher, Newton, Hardwig, Higgs and OPERA. Individually each is
accurate and well chosen. Taken together, it risks becoming a museum walk.
"Sixteen Claudes, Again" recovers the thread well. If the chapter needs
cutting, the Newton story and Peirce/Ibn al-Haytham are the most separable.
The Bromiley case and Millikan ("a second witness has to be capable of being
wrong differently") are the most load-bearing and must stay.

**Reveal / Part III opener.** Both are good. "Who changes the arrangement when
the arrangement is the problem?" is the best part-question in the book.

**Ch 6 — Pattern Language.** This is the most ambitious chapter, and mostly
it succeeds. Weaving the imagined Ines and Sam with the real Bing case and with
Alexander's asterisks used as confidence marks on the author's own proposals
is an original structural idea. The YAML pattern file evolving across the
chapter is the book's best concrete artifact. There are three problems:

- **Density.** The chapter cites Alexander, Beck, Cunningham, the Gang of
  Four, Doyle, Kohavi, Popper, Twyman, Duhem–Quine, Saussure, Feigenbaum,
  Karpathy, Kuhn, Laudan, Lakatos, Kitcher, Longino, Planck, Azoulay, Buzzard,
  Tao and Feyerabend, plus four 2026 mathematics results. It also has ten
  `Therefore` statements in 8k words. A reader will stop being able to keep
  the patterns in mind around the seventh.
- **"Two in the morning" appears four times.** Once is atmosphere; four times
  is a tic.
- **The 2026 mathematics news** (Riemann, Navier–Stokes) is placed to
  illustrate acceptance vs. pursuit and allocation. It works, but it makes the
  chapter read like news, and it will date fastest.

**Ch 7 — Recursive Self-Improvement.** Strong and well structured. Omar's
"second thought" carries the chapter. The four-level table is useful.
Original contributions:

- **"The Complexity Wall"** (NAS → random search → RegNet → RepVGG, then the
  store's accumulating checks)
- **"the complexity of self-change"**
- the editable vs. constitutional surface, with amendment difficulty as a
  gradient

The book should emphasise these more. Line 222 cites "Chapter 11's rule, that a
new system has to beat simplification" before the reader has met that rule.
Rephrase it as a rule "we'll meet again in the store." The `return True` gag
is perfect.

**Ch 8 — Scalable Oversight.** It's accurate and comprehensive. Of all the
chapters it has the most survey-like register, and the author's voice
thins out. It opens well on the nine-agent study and the evaluation-API
probing. After that, the "hypothetical investigation" thread from line 85
onward is thinner than the Ines thread in Ch 6 or the store in Ch 7, and it
fades by "Then We Touched the Machinery." Two "I like this…" sentences signal
the author reaching for presence. Consider running the store's research agent,
from Ch 7, through the oversight instruments. The book already has that
character.

**Interlude — When It Goes Wrong.** Excellent. It's short and chilling, and
it says what Chapter 10's fifth objection later concedes. "In 1948 the journals
kept coming out" is one of the best lines in the book.

**Ch 9 — Layer 4.** This is the weakest chapter. Its content is sound
(Bastani, Kestin, Wood–Bruner–Ross, Tutor CoPilot, Paul, Vaccaro, Buçinca,
Sen), but it's a sequence of "a study found…" paragraphs with no running case
and no experiment of the author's own. There are more "not X but Y" and
"Sometimes… Sometimes…" constructions than elsewhere. The editing anecdote
(line 15) and the trail-shoes conflict of interest (line 189) are the only
moments where the chapter is the author's. The trail-shoes passage is the best
idea in the chapter, and Chapter 11 never picks it up (see §5).

**Ch 10 — Fluent Autonomy.** It's short and does a lot: "bureaucracy on the
fly," "selective friction," "invisible by default, legible on demand," the
second coffee test (*Can I stop repeating myself?*) and the polite echo
chamber, and "Five Ways This Could Be Wrong." The chapter is honest about its
own failure (the restored Chapter 3 history). It needs the number the second
coffee test promises.

**Ch 11 — The Store That Builds Itself.** Practitioner-grade material:

- the problem fingerprint
- RXs and "composition over invention"
- saturation and synergy
- "Sami does not need a click" (*the objective determines which species of
  intelligence can survive*)
- the honest cold start
- logging the losers
- Coverage and Unmet Demand as anomalies
- "a philosophy of emergence should be willing to lose an A/B test"

Recruiters and reviewers from industry will read this chapter first. Weak
points: the prototype ambiguity (§3); the merchant's conflict of interest
(margin vs. customer), which is named in one sentence (line 191) after Chapter
9 set it up properly; and three "is not X. It is Y" constructions.

**Ch 12 — After Capacity.** Moving and intelligent:

- the Dantzig opener
- "expensive is easy to mistake for essential"
- "Anyone could do that"
- "gradient descent is the answer to Derrida"
- Ostrom
- "Cheap software removed the vendor's veto. It did not produce a second room
  at seven on Tuesday."
- "Who Owns the Laboratory," which uses the export-control suspension well
- "My children do not need comparative advantage to justify dinner"

The loosest analogy in the book is the double-descent mapping onto intellectual
history, with postmodernism as the interpolation spike (lines 27–29). The
author fences it ("I am borrowing the shape"), but it supplies the subtitle,
and a technical reader will find the mapping arbitrary. The chapter is long
(6.1k words) and has two endings: "I would like us to find out how much more"
and the hand-off to the prophecy. The first is stronger.

**Ch 13 — The Prophecy.** This is the riskiest part of the book. On a careful
reading it is dense with callbacks:

- the Bender–Koller octopus
- the Matrix Architect
- "DNA is just a fax machine" (Ch 1)
- "free tier… deducted from your taxes"
- the switched-to-Nickelodeon timeline, which echoes "switched that one to
  cartoons" in the bio
- the Architect as the owner of the laboratory who keeps the switch

Read that way, it is a bleak counterweight to "capacity over power": *worlds
end, capitalism doesn't.* But most readers won't decode it. Two specific risks:

- **The sexualised AI character.** "Claudit, the hottest agent… flipped her
  hair," and "her without makeup" is an exploded H100. Claudit is a thin
  pun on a real product. Some readers, and almost certainly some reviewers,
  will read this as juvenile or worse, and it undercuts the care of Chapters
  9 and 12.
- **The register break.** It's abrupt even with the "Alternative Ending"
  divider.

Options:

- **(a)** Keep it, but add a one-paragraph lead-in in Ch 12's last lines
  saying what the fable is arguing.
- **(b)** Keep the plot, but rewrite Claudit's introduction without the
  physical objectification. The H100 reveal works without "hottest."
- **(c)** Move it after the appendices as a hidden track.

I recommend (b), combined with a lighter version of (a). The README marks
Chapter 13 as protected, so this is the author's decision.

**"Scaffolds" page, Zen, Note on Evidence, Illustrations, About the Author.**
The two-line "Scaffolds" page is a good closing. The Zen is fun and sums the
book up well. "The tongue cannot reach the ear" is a lovely last-but-one line,
although the chapter itself left that question "unknown." Make sure that's
intended. The bio is charming. The Zalando and Amazon clearance is still open
in `REVISIT.md`.

---

## 5. Cross-book craft

**Continuity threads that work:** coffee (from the preface to "Decaf"), the
loose cable, chaos with an API key (Ch 1 → Ch 12), the camel (Ch 4 → Ch 11 →
Ch 12), Bing (Ch 6 → Ch 7), "telling people to be careful is institutionally
worthless" (Ch 5 → Ch 7), the rule-based exoskeleton (Ch 1 → Ch 7), and the
progress file as clay tablet.

**Threads that are dropped or not paid off:**

- **The trail-shoes conflict of interest** (Ch 9:189) should come back in Ch
  11's Surface Value section, ideally as Mei's own case. Right now the two
  trail-shoe shoppers look like a coincidence rather than one design.
- **Ines** (Ch 6) never returns. One sentence in Ch 10 or Ch 11 showing her
  pattern file being retrieved by the store's reviewer would join the halves
  of the book.
- **The Ch 3 educational demos** never got their human learners ("The student
  has not yet been asked"). Ch 9's tutoring evidence is the natural place to
  close that loop, even if the answer is "I still haven't."
- **Deep Mode** is named as Layer 3 and then barely mentioned after Ch 4.
  Chapter 10's "bureaucracy on the fly" is essentially Deep Mode grown up, and
  saying so would close the five-layer frame.

**Recurring phrasing to thin out** (counts over the 13 chapters):

- "I like this/that…": 8
- "That/This is what I mean by…": 5
- "two in the morning": 5 (4 in Ch 6)
- "not X. It is Y" constructions: about 6, half of them in Ch 11

None is egregious. Together they are the main remaining machine-edited
texture, and they cluster in Chapters 8, 9 and 11, the same chapters where the
narrative thread is weakest.

**Audience.** The book addresses three readers: practitioners (Chs 2, 3, 11),
thoughtful general readers (Chs 1, 4, 5, 12), and the AI-safety and
philosophy-of-science audience (Chs 6–8). That's ambitious and mostly managed.
Chapter 8 is where the general reader is most likely to leave. A sentence at
the top of Ch 8 telling them it's safe to skim the mechanisms and keep the
argument would help.

---

## 6. Prioritised recommendations

1. **Narrow and defend the thesis (Reveal, Ch 10).** State the claim as
   defeasibility under expensive verification. Separate the specifically
   scientific devices from generic coordination, and gather the cases of
   genuine rediscovery (Ch 6–8) in one place. Answer the "import vs.
   rediscovery" objection. About 400 words.
2. **Run the second coffee test.** The repository's dated evaluations and
   copyedit logs record corrections, refusals and restorations across
   August–September. Counting repeats (refused edits that came back, protected
   lines re-cut, as with the Ch 3 history) would give Chapter 10 a real number
   and the book an experiment in its second half. Cost: an afternoon.
3. **Add a methods box to Ch 2, and either report Ch 3 or relabel it.** Give
   the model, the number of runs, the time and cost, who "we" is, and the
   comparison to post-AlphaEvolve results. Resolve the ten missing figures,
   or redesign the chapter to need fewer.
4. **Say what the Ch 11 prototype is.** Two sentences.
5. **Ch 13 decision** (author's call; see §4). At minimum, revise Claudit's
   introduction.
6. **Restore Ch 8 and Ch 9 to the book's method.** Thread the store's research
   agent through Ch 8. Give Ch 9 a running case (the editing of this book is
   already there) and hand the trail-shoes conflict to Ch 11.
7. **Disclose the source concentration** in the Note on Evidence, and add the
   Prove2Me affiliation next to the Alpöge disclosure.
8. **Cut and tighten:**
   - Ch 1:101 (socks)
   - three of the four "two in the morning" in Ch 6
   - about 800 words from Ch 3
   - one or two vignettes from Ch 5
   - the Ch 12 double ending
9. **Pre-print re-checks:** the Clay status, the Navier–Stokes priority
   dispute, and the Riemann percentage wording. Add an acknowledgement of other
   uses of "System 3." Fix the Ch 7:222 forward reference.

---

## 7. Bottom line

The book does what it says on the cover more convincingly than most books in
its category, and it is more honest about its limits than nearly any of them.
Its main risk is not being wrong. The risk is that a careful critic notices
that the author's own experiments stop at Chapter 4, that "science" has been
defined generously, and that the ending changes register sharply. Recommendations 1–3
deal with the first two and recommendation 5 with the third. With those done,
this is a strong first book.

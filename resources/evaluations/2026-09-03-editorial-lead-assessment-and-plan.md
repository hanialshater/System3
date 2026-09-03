# Editorial Lead Assessment and Improvement Plan — 2026-09-03

*Method: one full sequential read of the manuscript as it stands on `main` at commit `d0d4143` (preface, Chapters 1–13, all back matter), followed by a quantitative pass (paragraph lengths, bold aphorisms, headings, motif and tic frequency, source concentration) and a consistency pass over README, references, image references and the art pipeline. The six earlier evaluations in this folder were read only after the manuscript, to see which of their recommendations were applied and which were declined. Where this assessment agrees with them it says so briefly; the new material is in §3, §5 and §6.*

---

## 1. Verdict

**This is a real book, with a real spine, in a voice nobody else has. It is one author pass away from being finished, and that pass is not an edit.**

The architecture the README describes holds on the page: four chapters build pieces of science without naming it, Chapter 5 reveals it, and everything after follows the executable institution into culture, self-modification, oversight, desire, fluency, a production system and finally the human. The reveal lands. The three experiments (circle packing, the Merge Sort demos, epistemic-swe) and the Zalando design are what make the philosophy trustworthy, and the book knows exactly how much each of them proves.

The weakness is concentrated and diagnosable. **Chapters 7–10 are told by a different narrator than the rest of the book.** Chapters 2–4 and 11 are written by someone who watched things happen. Chapters 7 and 8 are written by someone who read everything. The book's own thesis is that knowledge which has lost its contact with the world is residue, and the middle of the book is, by its own standard, mostly residue: a well-told literature review. The blind readers scored this correctly. The fix they asked for ("a second scene the author actually watched") is right, and §3.1–3.3 below argue that the scenes already exist in the author's material and in this repository, so no fabrication is needed.

Two smaller structural problems compound this: the same anecdote (editing this book with an agent) opens three of five consecutive chapters, and the manuscript recaps itself in full four times between Chapters 7 and 12.

**Book as it stands: 8.4 / 10.** Chapters 1–5 and 11–12 are at or near publication quality. Chapters 8 and 10 are the floor and are the only chapters that could make an acquiring editor hesitate. Ceiling after the plan in §6: 9.0.

### Scorecard (this reader, single read, /10)

| Ch. | Title | Words | Score | One line |
|----:|---|---:|:-:|---|
| 0 | Preface | 400 | 8.5 | Compact, honest about expiry dates; the Saussure/Wittgenstein cover note pre-empts Ch4 slightly but the cover forces it |
| 1 | Why I'm Betting on AI Agents | 3,180 | 8.5 | Thesis earned through examples; "control moves upward" is the right first idea |
| 2 | The Algorithm Vortex | 5,090 | 9 | The model for how the book should handle a number; every claim fenced exactly as far as it deserves |
| 3 | The Vibe Coder's Seat | 8,120 | 8 | Best material in the first half, and 1,500 words longer than any other chapter, with seven capitalized coinages |
| 4 | System 3 | 5,280 | 9.5 | Best chapter. The camel, the tongue, Alberto, and an experiment that lost and was reported as losing |
| 5 | The Society of Agents | 6,140 | 9 | The reveal. Cold open is the model for the book; Bernoulli, Popper, Peirce and Zollman all earn their place |
| 6 | Pattern Language | 4,490 | 7.5 | Strong argument, one concrete artifact (the schema), and a philosophy roll-call that the headings no longer announce but the sections still perform |
| 7 | Recursive Self-Improvement | 6,660 | 7.5 | Omar now frames it and the ladder is unmistakable; it is also pre-announced, then climbed, then recapped, then mirrored. 19 headings |
| 8 | Scalable Oversight | 4,300 | 6.5 | The right question ("how do you grade work you cannot do yourself?") followed by an eleven-technique instrument tour; one authored scene |
| 9 | Layer 4 | 3,960 | 7.5 | Well argued; opens on the same anecdote as Ch6 and Ch10; two of its sections are re-made in Ch12 |
| 10 | Fluent Autonomy | 2,230 | 6.5 | The chapter that carries the book's subtitle is the thinnest chapter in it. One real scene, then a manifesto |
| 11 | The Store That Builds Itself | 5,590 | 9 | The philosophy made to face an A/B test. "The architecture must contain a route by which the book's own theory can lose" |
| 12 | After Capacity | 6,220 | 8.5 | Big and humane; the cold open is superb; repeats Ch9 twice; the "double descent" pun is never paid off |
| 13 | The Prophecy | 610 | 7.5 | Works as a coda for readers who catch decaf, the octopus and taxes; reads as a shitpost for anyone else. Keep it, with two fixes |

---

## 2. What must be protected

These are the things a conventional editor would sand off and must not:

- **The fences.** "That sentence needs a fence around it" (Ch2), "Read the first line before celebrating the third" (Ch4), "Ten problems is nowhere near enough" (Ch4), "Eight hundred agent-hours against fourteen human-days is not a fair fight" (Ch8), "A philosophy of emergence should be willing to lose an A/B test" (Ch11). This is the book's credibility and it is rarer than the jokes.
- **The provocations that are then hedged in the next paragraph, not the next sentence.** "Saussure's theory was a specification. We implemented it. It's called GPT." "Gradient descent is the answer to Derrida." "System 3 isn't philosophy to me. It's Tuesday."
- **The motifs and their returns.** Camel (Ch4 → Ch11 → Ch12), coffee test (Ch2 → Ch7), Alberto (Ch4 → Ch5 → Ch6), octopus (Ch4 promise → Ch12 → Ch13), cows (Ch4 only, correctly), Omar (Ch7, now closed at the end).
- **The cold opens.** "Sixteen Claudes were building a compiler." "Omar is walking his dog at night." "LLM-as-a-judge arrived in my team looking like a threat." "There is a danger in writing a book about future architectures."
- **The endings that end on the chapter's own idea.** "If it works, things get much more interesting." "Apparently we are porting it." "Fortunately, Monday morning was waiting." "The teacher does not disappear. She moves up another level."
- **The lines that are the book.** "Let go of the path, not the boundary." "The model stays hollow. The system doesn't have to be." "Reality retains the right to be rude." "The human has to remain in the loop that changes the loops." "The overseer is not ground truth." "Construct knowingly. Build anyway."
- **Ch13**, on balance. See §4.

---

## 3. Book-level findings, ranked by what they would change

### 3.1 The middle is a survey, and the missing scenes already exist (Chs 7, 8, 10)

The prior evaluations concluded that only the author can fix Chapters 8 and 10, by supplying something he actually watched. Agreed. What they did not say is that the material is already on the record:

**Chapter 8.** The chapter asks at line 21 how you grade work you cannot do yourself, then spends `08:127–171` touring eleven interpretability techniques (representation engineering, sparse autoencoders, crosscoders, circuit tracing, natural-language autoencoders, J-space, activation steering, the refusal direction, circuit breakers, persona vectors, the Assistant Axis) in about 1,200 words. Meanwhile the author's own scalable-oversight story is sitting in the cold open of Chapter 12 (`12:5–15`): a recommendation team that had to decide how far to trust a judge that scores a million items overnight. That is the chapter's question in the author's own work. What did the team do? Calibrate the judge against human labels, sample where it disagreed with humans, find where it could be gamed, decide which decisions still needed a person. Whatever actually happened is the second scene the blind readers asked for, and it belongs in Chapter 8 as a section (working title "The Judge at Work"), leaving Chapter 12's cold open intact as the story about the profession. Then the instrument tour can shrink to the three ideas that carry the argument (reading versus controlling a representation; models can have diffs; a story that cannot survive intervention is still a story) with the rest reduced to one sentence and the references appendix. Net: roughly minus 600, plus 700, and a chapter with an author in it.

**Chapter 10.** The evaluators wrote that "no real trace exists" for the second attempt at "this chapter still feels like LLM writing." This repository is the trace. `prompts/chapter-version-evaluation.md` is an evaluator with a stated knowledge boundary. `resources/evaluations/` contains blind cold reads (the isolation principle applied to editors), an evaluator-triangulation file (independent evaluators), a "protected lines" list (a constitutional surface), and a section headed "Not applied, deliberately (author's call)" (Layer 4). The book was edited by the institution it describes, and the description at `10:145–161` ("Put the pieces together…") could be replaced by the actual thing: what the second attempt retrieved, what it left alone, which edit the evaluators wanted and the author refused. That is not a fabricated experiment. It is the one experiment the reader is currently holding.

**Chapter 7** is in better shape than 8 and 10 because Omar, the coffee scene at `07:155` and the BACON lineage give it a narrator. Its problem is structural, see 3.4.

### 3.2 The book recaps itself in full four times

Whole-book summaries appear at `07:33` (the ladder pre-announced before it is climbed), `07:455–457` (the ladder recapped), `10:145–161`, `11:319–343` (a nine-item list of chapter titles with one-line glosses) and `12:403–411`. A reader who has come this far does not need the table of contents read back to them, and each recap makes the chapter containing it feel like a summary chapter. Keep exactly one: Chapter 12's, which is the finale's earned right. Chapter 11 already has the compact version in its own next sentence ("build a scientific institution around the customer problem"); the list above it can go. Chapter 10's becomes the trace (3.1). Chapter 7's pre-announcement at line 33 is the one that costs most, because it spends the chapter's discovery in the introduction; keep the line "we kept discovering another job the teacher was doing" and let the rungs arrive one at a time.

### 3.3 One anecdote opens three of five consecutive chapters

Editing this book with an agent opens Chapter 6 (`06:5–19`, memory versus culture), Chapter 9 (`09:13–35`, the objective became clearer to me) and Chapter 10 (`10:5–27`, the instruction as evidence). The 2026-09-02 evaluation flagged this; the Ch9 correction list was changed but the device was kept. Two uses is a motif; three in five chapters is a habit the reader notices. Chapter 9 already contains a better cold open eight lines down: "Find me the cheapest flight" (`09:49–53`), which is concrete, funny and is Layer 4 in one paragraph. Move it to the top, and fold the book-editing insight ("I had learned what I meant by better partly by seeing versions I disliked") into a single callback paragraph later in the chapter.

### 3.4 Chapter 7 is a nineteen-heading chapter

Nineteen `##` headings in 6,660 words, against a book median of nine. The rubric's own warning ("unnecessary headings that turn a narrative into a consulting deck") applies. The ladder has one rung per heading, which is defensible, but the three definitional sections ("Recursive More" at `07:305–319`, "The Shadow History" at `07:321–331`, "Open-Ended Does Not Mean Unbounded" at `07:433–451`) are a glossary, a mirror and a restatement in sequence. The Shadow History is the author's own synthesis and should stay. "Recursive More" can be folded into the two sentences the chapter already has for it ("self-reference is not self-improvement" and "a compiler can compile a worse compiler"). Target: twelve headings or fewer, no material lost.

### 3.5 Chapter 12 re-makes two Chapter 9 sections

- "Advice Is an Intervention on the Human" (`09:191–221`) and "The Human Is Not the Reward Function" (`12:297–345`) make the same argument with the same phrase ("alignment by editing the human"), the same move (banning influence would outlaw teachers, books and marriages) and the same joke shape. Ch12 adds reflective agency and the list of conflicting goods; keep those, cut `12:299–311` to a two-sentence callback.
- "The Map Gets Cheaper" (`09:115–139`) and "Learning at the Speed of Curiosity" (`12:111–149`) share the map/territory metaphor, epistemic trespassing, and the scars line ("Fluency arrives before scars" / "the map without any scars from the roads"). Ch12's new contribution is "Explore broadly. Descend selectively." Keep that and refer back for the rest. About 500 words recovered in Ch12 without losing an idea.

### 3.6 The subtitle chapter is the thinnest chapter

The book is called *Towards Fluent Autonomy*. Chapter 10 is 2,230 words, opens on one genuine scene and then defines fluency three ways. Either the chapter earns the subtitle (3.1 gives it the material) or the structure should admit it is a bridge and fold it into Chapter 11 as a preamble, which already opens with "Then Monday morning arrives." Recommendation: earn it. Folding is the fallback if the author does not want to write the trace.

### 3.7 "Double Descent Life" promises a pun it never pays

An expert reader sees "double descent" and expects the machine-learning curve: as capacity increases, performance improves, collapses at the interpolation threshold, then improves again in the over-parameterized regime. Chapter 12 uses "descent" only in the sense of descending (`12:37–45`) and never touches the curve, so the one audience that knows the term is the one audience left puzzled. The mapping is sitting there: the chapter's own vocabulary is *capacity*; as machine capacity passes the point where it can do what we do, the human role appears to collapse, and then something descends into a different regime. One paragraph turns a frown into the chapter's best joke. This is the single highest value-per-word edit in the book.

### 3.8 Chapter 3 is 8,120 words and carries seven capitalized coinages

"How We Got Here" (`03:29–137`) runs 1,100 words of coding-agent history (HumanEval, Copilot, SWE-bench, SWE-agent, Replit, Lovable, the booking app) before the chapter's own problem appears. A reader who reached Chapter 3 knows most of it. Compress to 400 words. The coinages (Deep Mode, Five Layers, Strategic Constraints, Implicit Metric, Borrow a Mind, Independent Evaluators, Isolation Principle) were flagged on 2026-09-02; "implicit metric" and "borrow a mind" do not recur later and can be lowercased. Target chapter length: 6,800.

### 3.9 Chapter 8 cites one lab eleven times

Anthropic appears eleven times in Chapter 8 and once in the rest of the book combined; OpenAI twice. The book's own argument ("five agents citing the same paper are not five witnesses") makes this worth fixing on principle, not only for optics. Either add the non-Anthropic oversight and interpretability work the chapter is silent on (Redwood's control work is there; DeepMind's debate and amplification results, the academic sparse-feature and probing literature, are not), or have the chapter say out loud that it is drawing mostly from one lab's 2025–26 publications and why. The first option is better and costs a paragraph.

### 3.10 The book has been evaluated only by models

All six files in `resources/evaluations/` are model reads. Chapter 3 says it plainly: "A simulated beginner saying the explanation is understandable gives us a hypothesis… The student has not yet been asked." No human reader outside the author has read this manuscript end to end, as far as the repository records. Before any further model-driven polish, two human beta readers (one working ML engineer, one intelligent non-specialist) should read the whole thing in order and report where they stopped, laughed, skimmed and disbelieved. This is the P0 gate in §6, and the book's own thesis says why.

---

## 4. Chapter notes (what is not already in §3)

**Preface.** Does its job. One check: the dateline is August 2026 and the references say web sources were verified in August 2026; keep both in sync with the actual release date.

**Ch1.** The four-part frame (building blocks, environment, feedback, boundaries) is announced rather than discovered, but it is Chapter 1 and the book pays it back for twelve chapters. No change.

**Ch2.** Nothing to change in the prose. Eleven figures are referenced and none exist in the repository (§5). The chapter's short-paragraph ratio (45%) is the highest of the real chapters, almost entirely because of figure captions; not a prose problem.

**Ch4.** Eleven bold standalone aphorisms, most in the book, in the best chapter. Bolding does less work each time. Un-bold three or four ("Trust is local." "Productive distrust requires trust first." "The model inherits the residue." "System 1 can be fast because System 3 has often been working for centuries underneath it."); keep the lines. The camel photograph is load-bearing (claim 7 is "this is a real, unedited photograph") and must exist in the final layout.

**Ch5.** About 3,500 words of history between two agent bookends. It works because the agent touchpoints are interleaved (mortgage agent, Amazon, "the agent version is almost embarrassingly literal", the browser-as-new-witness). No structural change. Small: "almost embarrassingly" appears twice here and five times in the book; keep two book-wide.

**Ch6.** The schema table (`06:258–276`) stays; the author is right that it is the chapter's one artifact. The sections still walk Popper → Duhem/Quine → Kuhn → Lakatos → Laudan → Hull/Kitcher → Longino → Feyerabend in order even though the headings no longer say so. Fine if the reader is not told in advance; the surviving announcement is `06:37–39` ("every one of those failure modes now has a filename… design reviews written a few decades or centuries early"), which is a good line and enough.

**Ch7.** See 3.2 and 3.4. The Gödel Machine → "the practical answer arrived two decades later, and it was not a proof" → STOP/DGM sequence (`07:223–263`) is the chapter at its best: discovery, not announcement.

**Ch8.** See 3.1 and 3.9. Also: "gave this failure mode a wonderfully unromantic name: scalable supervision" (`08:55`). The 2016 paper's section is titled "Scalable Oversight", which is the chapter's own title; if that is right, the sentence should say the paper named the chapter (§5).

**Ch9.** See 3.3 and 3.5. The evidence run (Bastani, Kestin, Wood/Bruner/Ross, Bloom, Tutor CoPilot, Clark/Chalmers, Ballantyne, Payne/Bettman, Paul, Vaccaro, Buçinca, Sen) is accurate and well fenced; it is also twelve studies in 2,000 words with no scene from the author's own teaching or learning. One paragraph of the author learning something with a model this year, and where it went wrong, would do for this chapter what Omar did for Chapter 7.

**Ch10.** See 3.1, 3.2, 3.6.

**Ch11.** "I had spent nine chapters arguing" (`11:343`): ten chapters precede it. The roll-call above has nine items, so the count may be deliberate, but it reads as an off-by-one. The roll-call also still names Chapter 8 "Automatic alignment research" (`11:335`) after the chapter was retitled. Otherwise the strongest applied chapter in the book; "a resignation letter written in passive voice" and "standing on rung one with excellent posture" are exactly the register.

**Ch12.** See 3.5 and 3.7. "The annoying disciplines" and "My children do not need comparative advantage to justify dinner" are the chapter.

**Ch13.** Keep. Three notes. (1) The Architect lights a cigarette at `13:93` and again at `13:121`; the second should be "lit another" or nothing (flagged 2026-09-02, not applied). (2) The scene depends on the reader catching *decaf* (Ch4's "decaf confidence"), the octopus (Ch4's Bender and Koller), and taxes; Ch12's last line sets it up well enough that no frame is needed. (3) Sensitivity read: the con-man is the character with the South Asian name and the hero has the Anglo one. Probably nobody intended anything, and probably a reader will notice. A rename costs nothing.

**Zen of Autonomy.** Every line traces to a chapter. "The tongue cannot reach the ear" asserts what Ch4 leaves open (the human tongue, that is; the camel's is "Unknown"). Poetry is allowed to; noting it only.

**About the Author, Illustrations note.** Fine. The illustrations note describes a visual program the repository does not yet carry in the chapter files (§5).

---

## 5. Precision, consistency and production checks

Things to verify or fix that are not matters of taste.

**Attribution and sources**
- `08:55` — confirm whether Amodei et al. 2016 use "scalable oversight" (section title) or "scalable supervision" for the named problem, and match the sentence to the paper.
- Live-SWE-agent (references, Ch4 section) has no authors, venue or link. It carries the MARC-file anecdote, which is load-bearing for "Code Can Touch Back." Add the primary source or soften the anecdote's attribution.
- Every 2026 result cited as fact (Carlini's compiler numbers in `05:9`; the nine-Claude study, the August 2026 automated-alignment study, J-space, natural-language autoencoders and the Assistant Axis in Ch8; the one-million-conversation guidance figure and the disempowerment taxonomy in Ch9; `autoresearch` and HyperAgents in Ch7) should be checked against the primary document once more before typesetting. The preface's expiry-date stance covers staleness; it does not cover a misremembered number.
- Ch8 source concentration (3.9).

**Internal consistency**
- `11:335` "Automatic alignment research" → the chapter is now "Scalable Oversight".
- `11:343` "nine chapters" (see Ch11 note).
- README §"Second arc — WIP" still says Chapters 5–10 are "first integrated drafts… not locked" and "will receive the same… passes". The git log shows those passes were applied. Update or remove.
- References appendix has no Chapter 10 section (Ch10 cites nothing; add a one-line note or leave, but make it deliberate).
- Ch9's H1 is "Layer 4" with subtitle "The Human Learns Too"; the README calls it "Layer 4: The Human Learns Too". Pick one.

**Figures and art**
- Twelve in-text image references in Chapters 1, 2 and 4 (`../resources/image0122.png` through `image0141.png`) point to files not in the repository. Chapters 3 and 5–13 have no in-text figures at all. Either restore the Ch1/2/4 figures or remove the placeholder captions so the book is uniformly opener-illustrated; the camel photograph in Ch4 is the one that cannot be dropped.
- `resources/chapter-openers/` uses pre-renumbering filenames (`chapter-08-the-desire-problem.jpg` is now Ch9, `chapter-09-fluent-autonomy.jpg` is Ch10, `chapter-10-the-store.jpg` is Ch11, `chapter-11-capacity-over-power.jpg` is Ch12). The manifests map them correctly, but `book-design/manifests/chapter-08.json` (Scalable Oversight) and `chapter-13.json` (The Prophecy) reference no opener image. Two openers are missing from the pipeline.

**Style census (for the record)**
- Short paragraphs (≤12 words) as a share of all paragraphs: 24% (Ch8) to 45% (Ch2); Ch13 84% by design. Ch8's low figure is not a virtue here; it is the survey register.
- Bold standalone aphorisms: Ch4 11, Ch12 7, Ch7 6, Ch6 5, Ch9 5; Ch8 0.
- "X is not Y. It is Z." pivots: Ch4, Ch7 and Ch11 six each. The good ones ("opacity with good typography", "a resignation letter written in passive voice") should stay; density is the only issue.
- Headings: Ch7 19, Ch11 14, Ch2 13, Ch6 12, Ch8 12; median 9.
- "almost embarrassingly" ×5, "suspiciously" ×8, "Congratulations." ×3 book-wide. Keep two, four and two.

---

## 6. Improvement plan

Ordered by what moves the book most per hour of the author's time. Phases A and B are sequential; C and D can run alongside either. "Author" means only the author can do it. "Assisted" means an editor or agent drafts under the version-evaluation prompt and the author approves.

### Phase A — the author's pass (est. 12–16 hours; moves the score from 8.4 to ~8.9)

| # | Chapter | Work | Owner | Est. | Acceptance |
|--:|:-:|---|:-:|--:|---|
| A1 | 8 | Write "The Judge at Work": how the team adopted, calibrated and bounded LLM-as-a-judge; where the judge was wrong and how you found out; which decisions kept a human. 600–900 words. Then compress `08:127–171` to the three carrying ideas. | Author | 5h | A blind human reader can name one thing the author watched in Ch8. Chapter ≤ 4,200 words. |
| A2 | 10 | Replace `10:145–161` with the real second attempt: what the editing institution in this repo actually did with "this chapter still feels like LLM writing," including one edit the evaluators wanted and the author refused. 500–800 words. | Author | 4h | Ch10 contains a trace with a date. Blind reader scores Ch10 within one point of Ch9. |
| A3 | 12 | Pay off "double descent": one paragraph mapping the ML curve to capacity, the collapse, and the second regime. | Author | 1h | An ML reader recognizes the curve and the pun. |
| A4 | 9 | One paragraph of the author learning something with a model this year, and where fluency arrived before the scar. | Author | 1.5h | Ch9 has one first-person scene. |
| A5 | 13 | Decide: rename Devesh or not; fix the second cigarette. | Author | 0.5h | Decision recorded. |
| A6 | — | Decide on 3.6 (earn Ch10 or fold it into Ch11). Default is earn, via A2. | Author | — | Decision recorded. |

### Phase B — structural edits (est. 10–12 hours assisted; author approval per chapter)

| # | Chapter | Work | Owner | Est. | Acceptance |
|--:|:-:|---|:-:|--:|---|
| B1 | 7 | Remove the pre-announced ladder at `07:33`; fold "Recursive More" into two sentences; merge headings to ≤ 12; keep Shadow History. | Assisted | 2.5h | ≤ 12 headings; ladder appears once climbed, once recapped. Nothing else cut. |
| B2 | 9 | Open on "Find me the cheapest flight"; reduce the book-editing anecdote to one callback paragraph. | Assisted | 1.5h | Only Ch6 and Ch10 open on the editing anecdote. |
| B3 | 12 | Cut `12:299–311` to a callback; reduce "Learning at the Speed of Curiosity" to its new move plus a pointer to Ch9. | Assisted | 1.5h | ~500 words removed; no idea lost (checked against a list of Ch12's distinct claims). |
| B4 | 11, 10, 7 | Recaps: cut the nine-item roll-call at `11:319–343` (keep the compact sentence); Ch10's recap becomes the trace (A2); Ch7's pre-list removed (B1). Ch12's recap stays. | Assisted | 1h | One whole-book recap in the manuscript. |
| B5 | 3 | Compress `03:29–137` to ~400 words; lowercase "implicit metric" and "borrow a mind". | Assisted | 2h | Ch3 ≤ 6,800 words; five capitalized coinages. |
| B6 | 4, 6, 7, 12 | Un-bold three or four aphorisms in Ch4; trim "almost embarrassingly" to two, "suspiciously" to four, "Congratulations." to two book-wide. | Assisted | 1h | Census in §5 met. |
| B7 | 8 | Add non-Anthropic oversight and interpretability sources, or a sentence owning the concentration. | Assisted | 1.5h | ≤ 6 mentions of any one lab in Ch8, or the concentration named. |

### Phase C — precision pass (est. 4–6 hours; can run alongside A or B)

| # | Item | Owner |
|--:|---|:-:|
| C1 | `08:55` "scalable supervision" vs "scalable oversight" attribution. | Assisted |
| C2 | Live-SWE-agent primary source in the references. | Assisted |
| C3 | Re-verify every 2026-dated figure against its primary document (list in §5). | Assisted, author signs |
| C4 | `11:335` chapter name; `11:343` chapter count; README WIP paragraph; Ch9 title form; references Ch10 heading. | Assisted |
| C5 | `13:121` second cigarette. | Assisted |

### Phase D — production (est. 3–4 hours plus art time)

| # | Item | Owner |
|--:|---|:-:|
| D1 | Restore or remove the twelve missing in-text figures in Ch1/2/4. The Ch4 camel photograph must ship. | Author decides; assisted executes |
| D2 | Add opener images for Ch8 and Ch13 to the manifests; rename `resources/chapter-openers/` files to current numbering or document the mapping. | Assisted |
| D3 | Rebuild `dist/` after A–C. | Assisted |

### Phase E — the gate (calendar time, not effort)

| # | Item |
|--:|---|
| E1 | Two human beta readers read the full manuscript in order after Phase A. One ML engineer, one non-specialist. They report: where they stopped, laughed, skimmed, disbelieved; one sentence per chapter. No rubric. |
| E2 | One sensitivity read of Ch13 and the Ch5 civilizations passage by a human. |
| E3 | Only after E1: one further blind model read of Chs 7–10 to confirm the middle no longer sags. Model reads have done their job; the next signal has to come from the population the book is for. |

### Sequencing

Week 1: A1–A6 (author). Week 2: B1–B7 and C1–C5 (assisted, author approves chapter by chapter, using `prompts/chapter-version-evaluation.md` as the acceptance test). Week 3: D1–D3, then E1–E2 begin. Week 4–5: E1 returns; address findings; E3; lock.

### What not to do

- Do not run another whole-book anti-LLM-writing pass before Phase A. The remaining synthetic register in Chapters 7–10 is not a prose problem; it is the absence of a narrator, and sanding will make it worse (Chapter 10 says so itself).
- Do not cut the Ch6 schema table, the Ch7 Shadow History, the Ch4 seven claims, or Ch13. Each has been proposed for cutting by a model reader; each is a deliberate authorial choice that the plan above leaves alone.
- Do not add a chapter. The book is 60,000 words of body text, short for the genre and right for this book.

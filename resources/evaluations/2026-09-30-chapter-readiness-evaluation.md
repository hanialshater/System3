# Chapter-by-chapter readiness evaluation — 30 September 2026

Evaluated the full manuscript at `9a3dc47`, in the order given by `book-design/curated/book-order.json`: preface, part pages, Chapters 1–13, interludes, and back matter. This is a developmental and production-readiness read. It includes checks of internal consistency and citation anchors, and it re-checks the issues raised on 27 September. It is not a full fact-check, and the PDF was not built for this pass.

## Bottom line

**The book is 8.3/10 as a book, and about 75% of the way to production.** The argument, voice and structure are strong enough to publish. What remains is finishing work, and none of it calls for rethinking the book. Four things stand between this manuscript and a printer:

1. **Unresolved drafting markers** in the manuscript itself (details below).
2. **Chapters 6–8 are still changing.** Nine commits touched them in the last two days. They are also where the book depends most heavily on events from August–September 2026.
3. **Ten missing figures in Chapter 2.** They appear as visible `*[Missing figure]*` placeholders in the text.
4. **Standard publishing work that has not started:** copyedit, front matter, rights and employer clearance, and printer selection with a physical proof.

**Estimate:** about 8–12 weeks of focused work to a print-ready file. This assumes the Chapter 2 figures and the copyedit run in parallel with the final developmental pass. The estimate is a planning figure, not a measurement.

## Readiness scale

- **Ready:** copyedit only.
- **Near:** one light, targeted pass.
- **Needs pass:** a focused developmental edit of specific sections.
- **Blocked:** a production or author decision is required before the chapter can be locked.

## Chapter table

| Section | Quality /10 | Readiness | % | What holds it back |
|---|---:|---|---:|---|
| Preface | 8.5 | Ready | 90 | Anchored to "September 2026" and the Navier–Stokes report; this status needs a check at publication. The "ultimate architecture" overclaim from the 27 Sept review is gone. |
| Part pages | — | Near | 85 | The Part II epigraph "Ground every claim. Trace every source." contradicts Ch 4's "Not every sentence needs a dossier." |
| 1 — Why I'm Betting on AI Agents | 8 | Near | 85 | The restored "cat obsession" paragraph breaks register: it is future-tense prophecy, uses straight quotes, and sits between two careful paragraphs. Four bolded slogans in one chapter. The conga line, goldfish and "chaos with an API key" are protected. |
| 2 — The Algorithm Vortex | 8.5 | **Blocked** (art) | 60 | The prose is ready. 10 figures are missing, and the placeholders are visible in the text. The 2.636 result still has no methods trail (model, date, evaluator tolerance, budget, human interventions). "The Contract" and "Zero Framework" are the best argued sections in Part I. |
| 3 — The Vibe Coder's Seat | 8.5 | Near | 85 | Its history of coding tools builds up the five layers rather than asserting them. Keep that. "Bars Moved Around" admits the Deep Mode results are diffuse. One authentic before/after artifact would strengthen the chapter more than any added prose. |
| 4 — System 3 | 9 | Ready | 90 | The camel, Alberto, the face and epistemic-swe (honestly reported against itself) all work. The "hollow" overclaim has been replaced with Dennett. |
| 5 — The Society of Agents | 9 | Near (art) | 85 | The book's centre. 7 VISUAL/DIAGRAM briefs are embedded as HTML comments; REVISIT records that they conflict with the selected opener. They will not print, but the art decision is open. |
| Reveal — *We call it science* | 8 | **Blocked** (author) | 70 | Carries an `ASSISTANT EDIT … END ASSISTANT EDIT` block awaiting author acceptance. The paragraph itself is good: it gives the discrimination criterion the 27 Sept review asked for. |
| 6 — Pattern Language | 8 | Needs pass | 70 | The Ines/Sam thread now gives the chapter an accumulating state, which is a clear improvement. Still the densest chapter: ~8k words, 40 notes, and about ten philosophers each given a paragraph-long introduction (Popper, Duhem–Quine, Saussure, Kuhn, Laudan, Lakatos, Kitcher, Longino, Planck, Feyerabend). It leans most heavily on events from Aug–Sept 2026 (Fermat formalization, Riemann bound 41.6→67.2%, Navier–Stokes, Clay statement, priority dispute), so it carries the highest verification and shelf-life risk. Revised four times in three days; let it settle. |
| 7 — Recursive Self-Improvement | 7.5 | Needs pass | 70 | The second half is excellent: "recursive more", "excellent DevOps", editable vs constitutional surface, the amendment YAML. The first half still reviews ~15 learning methods in ~3k words (TD → NAS → EWC → curiosity → IRL → world models → POET). Compress it to the methods that change the store agent's problem. |
| 8 — Scalable Oversight | 8 | Near | 75 | Up from 7.5: one hypothetical investigation now runs through the instruments, and the chapter says openly that they come from separate studies. Still reads as an inventory from J-space through crosscoders. Its two central studies are Anthropic reports from 2026; recheck their status. |
| Interlude — When It Goes Wrong | 8 | **Blocked** (author) | 80 | Short and strong, ending on "In 1948 the journals kept coming out". Carries an `ASSISTANT DRAFT` header awaiting sign-off. |
| 9 — Layer 4 | 8.5 | **Blocked** (author) | 75 | The clearest argument in the book. A `SLOT 4` placeholder with an editor's note is still waiting for the author's own marketplace case. Heaviest bolding in the book (16 spans). "Very efficient. / Slightly evil." is the kind of one-line mini-climax the house prompt penalizes. |
| 10 — Fluent Autonomy | 8.5 | Near | 80 | "Five Ways This Could Be Wrong" and the second coffee test ("the unit is closer to the sigh") are among the best pages in the book. The middle sections (Bureaucracy on the Fly, Selective Friction, Invisible by Default) keep the older, slogan-heavy register: 13 bold spans. |
| 11 — The Store That Builds Itself | 8 | Needs pass | 75 | **Unfixed from 27 Sept:** "Only intervention tells us how much of the outcome the problem was actually causing" is still categorically wrong (see the 27 Sept Pearl note for the fix). Dense with "not X, it is Y" constructions ("Cold start is a state, not an error", "is culture", "a product requirement"). Mei, Sami, Lea and "beat simplification" are protected. |
| 12 — After Capacity | 8.5 | Near | 80 | Dantzig, the Tuesday room and the new "Who Owns the Laboratory" section are strong. **Consistency error:** "ten thousand agents for eighty-eight hours" is cited to the *Fermat* source, but Ch 6 describes the Navier–Stokes run as about four days plus seventeen hours. Verify the June 2026 export-control access suspension against the source. |
| Alternative Ending / 13 — The Prophecy | 7 | Ready (protected) | 90 | Deliberately polarizing and protected by the author. The divider does its job. Publisher risk to note: the "hottest agent… flipped her hair" framing may read as dated to some reviewers. That is an author decision, not an edit. |
| Scaffolds | 9 | Ready | 100 | — |
| Zen of System 3 | — | Near | 80 | "Never write solution code" and "Harness immutable" are gone. "Ground every claim. Trace every source." and "The tongue cannot reach the ear." still overstate what the chapters argue. |
| Note on Evidence | — | **Blocked** (author) | 85 | A useful table. Carries a `CLAUDE DRAFT` marker. |
| References | — | Near | 80 | Every inline anchor resolves (0 dangling, 0 orphaned). Chapters 1 and 3 have no inline citations, only reading lists, so the evidence trail is uneven across chapters. Format mixes numbered notes with "Additional sources". |
| About the Author | — | Near | 80 | Names the author's current employer (Zalando), and Ch 5 describes work at Amazon. Get employer communications/legal clearance. |

## Blockers, in order

1. **Author sign-off markers.** Covers the reveal (`ASSISTANT EDIT`), the interlude (`ASSISTANT DRAFT`), the evidence note (`CLAUDE DRAFT`) and the Ch 9 `SLOT 4` placeholder. Accept, rewrite or cut each; this is days of work, not weeks.
2. **Chapter 2 figures.** Recover or commission 10 figures, or cut the placeholders and let the prose stand. The prose does not depend on them.
3. **Two factual fixes that are already known.** The Ch 11 causality sentence, and the Ch 12 "eighty-eight hours" figure with its citation.
4. **Verification of time-sensitive claims.** Every August–September 2026 event cited as fact (Chs 6, 8, 12, preface). These were outside what this reviewer could independently check. They are also what will date fastest.
5. **Front and back matter not in the manuscript.** Title page, copyright/ISBN page, dedication, acknowledgments and index are all missing. Decide whether the book has an index before copyedit.
6. **Print.** Printer, bleed/spine, colour profile and physical proof are all still open, as REVISIT records.

## Editorial pass, if time allows only one

- **Ch 7:** cut the learning-methods survey by about a third. Keep TD-Gammon, curiosity/noisy TV, IRL and world models, because each changes the store agent's problem.
- **Ch 6:** shorten the philosopher introductions to a sentence each wherever the Ines story already carries the point. The Laudan, Lakatos and Kitcher cluster in "Separate Use from Investigation" is the obvious candidate.
- **Chs 9–11:** de-bold. Keep bold for defined terms introduced once. Remove it from emphasis and slogans.
- **Ch 1:** either fold the "cat obsession" joke into the jacket-returns paragraph in the book's own voice, or move it.

## What not to touch

Chapters 4, 5 and 12 and the scaffolds page. Also the following protected lines: "It was a beautiful answer to a nearby problem"; "Ten agents sharing one assumption are not a search party; they are a conga line"; "The mark did not need to be wiser than the clerk. It needed to outlive him"; "We have successfully parallelized the experience of being ignored"; "At least the no has an address"; "The intelligence explosion… may look suspiciously like excellent DevOps"; "Cheap software removed the vendor's veto. It did not produce a second room at seven on Tuesday"; "My children do not need comparative advantage to justify dinner."

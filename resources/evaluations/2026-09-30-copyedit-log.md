# Copyedit log — 30 September 2026

Work follows the [fix and copyedit plan](../editorial/copyedit-plan-2026-09-30.md). A chapter closes only after it passes its gate:

1. The seed check passes.
2. The PDF build passes, which checks reference numbering, artwork anchors and covers.
3. The unit tests pass.
4. A re-read against the house dimensions finds nothing further to fix.

Scores are editorial shorthand, as in the [readiness evaluation](2026-09-30-chapter-readiness-evaluation.md).

**Baseline build before any edit:** 317 pages, 87 interior illustrations, 0 placements or covers needing review, 7 pending design directions.

## Pass 0 — mechanical, whole manuscript

- **Quotation marks.** Converted straight quotes to curly quotes in prose and references. Straight quotes stayed in code, HTML comments, URLs and raw LaTeX. The renderer prints quotes exactly as typed, and the previous proof contained 65 straight double quotes.
- **Ellipses.** Replaced three periods with the ellipsis glyph outside code.
- **Spelling.** Standardized to American: catalog, program (Lakatos), traveled, fiber, anesthetist, operating theater, theater, e-commerce.
- **Heading case.** "Separate Use from Investigation" became "Separate Use From Investigation", to match the book's rule of capitalizing prepositions of four or more letters.
- **Tooling kept in step:**
  - three seed anchors in `check-eggs.sh` and the register now use curly apostrophes;
  - the `a120` art anchor now reads "program";
  - the Chapter 1 and 3 cover titles in `provenance.json` now use curly apostrophes. The cover art itself is unchanged.
- **Correction during the pass.** The first `programme → program` substitution also turned "programmers" into "programrs" in Chapter 6. A word-level diff of the whole pass caught it, and the word was restored. After the fix, the word-level diff shows only the intended spelling changes.
- **Gate:** seeds pass; build 317 pages, 87 illustrations, 0 placements or covers needing review; unit tests pass.

## Part I and Part II

Every chapter here was re-read line by line against the plan and the house dimensions. Protected lines were checked and left intact.

| Section | Changes | Re-evaluation | Status |
|---|---|---|---|
| Preface | None beyond Pass 0. The Leibniz dates, the Poincaré-embedding and MAP-Elites examples, and "Three centuries later" were all checked. The dated opening ("It is September 2026") is confirmed by the fact check. | 8.5, unchanged. Short and seeds the book (cathedral, coffee, loose cable). | Closed |
| Part pages | None beyond Pass 0. | — | Closed |
| 1 | "responsible for everything from the deepest ocean trenches" became "from the creatures of the deepest ocean trenches", because life did not make the trenches. The restored cat paragraph lost its serial comma, per house style; its wording is untouched. | 8, unchanged. Four bold statements kept: they name the book's bets. | Closed |
| 2 | The ten `[Missing figure]` placeholders became `DIAGRAM — missing figure` production comments, which the build now tracks (7 → 17 design directions). The reading edition no longer prints them. The evolutionary-search result (2.08 → about 2.45), which previously appeared only in a caption, is now in the prose. "best-known" is hyphenated. The section heading "The Algorithmic Vortex" now matches the chapter's term, "The Algorithm Vortex". | 8.5. The production blocker is removed. The methods trail for 2.636 (model, date, tolerance, budget) is still absent; it needs the author's run records and was not invented. | Closed; figures and methods trail left to the author |
| 3 | One serial comma. | 8.5, unchanged. No wording problems found. | Closed |
| 4 | None beyond Pass 0. Recomputed every figure in the epistemic-swe tables: 57% patch reduction; 4.9×/15.6×/7.6×/7.5×; more than two-fifths of baseline lines; about one-third once the outlier is excluded. All are consistent. | 9, unchanged. | Closed |
| 5 | "plough" became "plow"; Pass 0 spelling. Four fact-check corrections: (1) Sima Qian's 213 BCE order targeted the histories of states other than Qin and privately held classics, and exempted medicine, divination and agriculture (the text had said "private histories … useful technical works"); (2) Li Si was a minister in 221 BCE and chancellor only later; (3) Kepler saw the moons through a telescope Galileo had sent to the Elector of Cologne, so the passage no longer blames "Galileo's lens" and now notes the shared lens grinder; (4) Popper called it "the third world" in 1967 and "World 3" later. | 9, unchanged. Every other Carlini, Dr. Stone, Bromiley, Millikan, Galileo, Boyle, Wegener, Newton, OPERA and Popper detail is confirmed. | Closed |
| Reveal | None. The `ASSISTANT EDIT` marker stays for the author. | 8. | Author decision |

**Gate:** seeds pass; build 317 pages, 87 illustrations, 0 placements or covers needing review, 17 pending design directions (the 10 Chapter 2 figures are now counted); unit tests pass.

## Part III

| Section | Changes | Re-evaluation | Status |
|---|---|---|---|
| Part III page | None beyond Pass 0. | — | Closed |
| 6 | **Fact-check corrections (six):** (1) Bing revenue per user "over", not "about", thirty percent; (2) Alexander's two asterisks mean "a true invariant"; (3) *Design Patterns* is attributed to "four authors from that movement", because only one of the four attended the 1993 Hillside meeting; (4) the Riemann result is attributed to Anthropic's August report, which describes an engineer who is not a mathematician; (5) "roughly ten thousand" is the Navier–Stokes group's peak concurrency, not a total across problems; (6) the priority-dispute sentence now attributes the "Anthropic employee" description to Alpöge alone, and drops "produced partly with an internal Anthropic model", which could not be verified. The author should restore that clause if they hold a source. **Line edits:** "a name you can say in a meeting and a photograph" became "…in a meeting, then a photograph" (the old order read as if you could say a photograph); three serial commas removed from simple lists; Pass 0 spelling. **Not done:** the planned compression of philosopher introductions. On close reading, the author's 29–30 September passes already reduced each to one or two sentences tied to the Ines story. Cutting further would remove the links the chapter builds between the thinkers and the story. | 8 → 8.5. The Ines thread carries the chapter, and every 2026 event is now stated as its source states it. Density remains its main cost. | Closed |

**Chapter 6 gate:** seeds pass; build 317 pages, 87 illustrations, 0 placements or covers needing review; unit tests pass.
| 7 | **Delete-and-fold compression, confined to true repetition:** (1) cut the AlphaZero self-play sentence and "Yesterday's learner can generate tomorrow's difficulty", both of which restated the self-play paragraph two sections earlier; the numbered AlphaZero preprint note was removed, the *Science* paper stays in Additional sources, and notes 16–32 became 15–31; (2) cut the three abstract sentences on learning speed after meta-learning; (3) cut the third restatement of Bing's session proxy down to "Bing's researchers turned to sessions." **Kept on purpose:** Sutton/TD (Chapter 10 cites it), CIRL (Chapter 9 cites it), and the medicine/weapons line (Chapter 12 cites it). Every method that still names a researcher is tied to a step in the store agent's problem. On close reading, the one-third cut proposed in the readiness evaluation would have removed that connective work, so it was not made. | 7.5 → 8. The first half moves faster and no longer repeats itself; the second half (constitution, amendment) is unchanged. | Closed |
| 8 | None beyond Pass 0. Fact check confirmed: nine Opus 4.6 agents; PGR 0.23 vs 0.97; 800 agent-hours; transfer to math but not code; production-scale result within noise; ten categories and 2.4% of about 1,600 trajectories; J-space and NLA characterizations. Search confirms the label-probing exploit ("test-label exfiltration"). One clause could not be checked from this environment because the primary blog is blocked: that the authors said the repeatedly queried test set "effectively served as a validation set". The author should confirm it. | 8, unchanged. | Closed; one clause for the author to confirm |
| Interlude | None beyond Pass 0. The `ASSISTANT DRAFT` marker stays for the author. | 8. | Author decision |

**Chapter 7–8 gate:** seeds pass; build 317 pages, 87 illustrations, 0 placements or covers needing review; references validate after renumbering; unit tests pass.

## Parts IV and V, the alternative ending, and back matter

| Section | Changes | Re-evaluation | Status |
|---|---|---|---|
| Part IV and V pages | None beyond Pass 0. | — | Closed |
| 9 | **Bold:** 16 spans reduced to the style sheet. Borrowed terms became italics (*scaffolding*, *epistemic trespassing*, *transformative experiences*, *appropriate reliance*, *capabilities*); emphasis and slogans became plain. **One-liners:** "Very efficient." / "Slightly evil." folded into one paragraph; the joke stays. **Back-references:** "which appeared earlier in the story of the reward" became "which appeared in Chapter 7"; Russell's closing now names the danger it refers to ("that first danger, enfeeblement"), which was four paragraphs back. **Fact check:** every study is confirmed (Bastani, Kestin, Tutor CoPilot, Vaccaro, Anthropic's 6% guidance figure, Wood/Bruner/Ross). | 8.5, unchanged. It reads less like a slide deck. | Closed; `SLOT 4` for the author |
| 10 | **Bold:** kept for the coined terms (*fluent autonomy*, *bureaucracy on the fly*) and for the five run-in objection heads; removed from slogans and the closing blockquote. | 8.5 → 9. Its middle sections no longer shout, so "Five Ways This Could Be Wrong" lands harder. | Closed |
| 11 | **Causality overstatement corrected**, the item still open from 27 September. "Only intervention tells us…" became "takes an intervention, or causal assumptions strong enough to stand in for one", and Pearl's ladder is now stated as data alone being unable to answer rung-two questions. **Bold:** kept for coined terms (problem fingerprint, recommendation experiences, Coverage, Unmet Demand, Surface Value); removed elsewhere. Pass 0: "e-commerce". **Not done:** the planned trim of "not X, it is Y" constructions. On re-reading, each one ("It is homework", "a resignation letter written in passive voice", "It is branding", "is culture") is a joke or turn that does argumentative work, and none shares a paragraph with another. | 8 → 8.5. The one factual overclaim in the design chapter is gone. | Closed |
| 12 | **Fact-check corrections:** (1) Dantzig compressed his summer "into under a minute" (his words); (2) "ten thousand agents for eighty-eight hours", which conflated the launch-to-result time with the peak agent count and cited the Fermat source, became "put ten thousand agents on one problem"; (3) the telescope sentence no longer claims Kepler's instrument was not Galileo's (Galileo made it); it now says astronomers elsewhere checked the moons with telescopes of their own within a year; (4) the June 2026 access sentence now says one model returned for everyone and the other only for a set of US organizations, and the reference adds Anthropic's redeployment announcement with the correct dates. The Belkin reference now carries the *PNAS* title. | 8.5, unchanged. It now agrees with Chapters 5 and 6. | Closed |
| Alternative ending, 13, scaffolds | Pass 0 typography only (curly quotes, ellipses). No wording touched. | Protected. | Closed |
| Zen | None. The author revised the list on 30 September and kept both lines that the 27 September review questioned; they are treated as deliberate (see the plan). | — | Closed |
| Evidence note | None. The `CLAUDE DRAFT` marker stays for the author. | — | Author decision |
| Illustrations note, about the author | Pass 0 only. Employer clearance is added to REVISIT. | — | Closed; clearance for the author |
| References | Chapter 7 renumbered (15–31); the AlphaZero preprint note was removed (the *Science* paper stays in Additional sources); the Fable/Mythos access note is corrected and extended; the Belkin title is corrected; Pass 0 quotes and one "programme". The build validates every citation number against its entry. | — | Closed |

**Parts IV–V gate:** seeds pass; build 317 pages, 87 illustrations, 0 placements or covers needing review, 17 pending design directions; unit tests pass.

**Final sweeps on the full manuscript:**
- aspell over every added line finds only names and technical terms;
- codespell finds no misspellings;
- no unbalanced emphasis markers remain, apart from Chapter 6's intended `\*\*` confidence marks and literal "A*";
- text extracted from the PDF contains no `[Missing figure]`, no HTML comment text and no "programrs".

## Status after the copyedit

| Section | Before | After | Readiness | What remains |
|---|---:|---:|---|---|
| Preface | 8.5 | 8.5 | Ready | — |
| 1 | 8 | 8 | Ready | — |
| 2 | 8.5 | 8.5 | Ready (text) | Figures; methods trail (author) |
| 3 | 8.5 | 8.5 | Ready | — |
| 4 | 9 | 9 | Ready | — |
| 5 | 9 | 9 | Ready (text) | Visual briefs (art) |
| Reveal | 8 | 8 | Author | `ASSISTANT EDIT` sign-off |
| 6 | 8 | 8.5 | Ready | Priority-dispute clause if the author has a source |
| 7 | 7.5 | 8 | Ready | — |
| 8 | 8 | 8 | Ready | Confirm one clause against the primary blog |
| Interlude | 8 | 8 | Author | `ASSISTANT DRAFT` sign-off |
| 9 | 8.5 | 8.5 | Author | `SLOT 4` |
| 10 | 8.5 | 9 | Ready | — |
| 11 | 8 | 8.5 | Ready | — |
| 12 | 8.5 | 8.5 | Ready | — |
| 13 / ending / scaffolds | 7 / — / 9 | unchanged | Ready (protected) | — |
| Back matter | — | — | Author | `CLAUDE DRAFT`; employer clearance |

**Manuscript:** about 90% ready, up from about 75%. What remains are four author decisions (three sign-off markers and `SLOT 4`) and two clauses to confirm. After that the text is ready for a professional proofread.

**Production:** unchanged. Chapter 2 figures, Chapter 5 art, front matter (title, copyright/ISBN, dedication, acknowledgments, index decision), clearance, and printer/proof are all still open (see [REVISIT](../REVISIT.md)).

This was a developmental copyedit by one editor with fact-checking support. It does not replace an independent human proofread of the typeset pages, which should be the last step before print.

## Final decisions (delegated by the author, 30 September)

The author asked for these decisions to be made so that the manuscript is ready for proofreading.

| Item | Decision |
|---|---|
| Reveal page `ASSISTANT EDIT` | **Accepted.** The paragraph states what makes the arrangement scientific, which the 27 September review asked for. The markers are removed. |
| Interlude `ASSISTANT DRAFT` | **Accepted.** The header comment is removed. |
| Evidence note `CLAUDE DRAFT` | **Accepted.** The table matches the chapters. The comment is removed. |
| Chapter 9 `SLOT 4` | **Removed.** The section already makes its point through the trail-shoe shopper and the multi-principal research. The editor's draft would have restated Chapter 6's Longino argument. |
| Chapter 8 "validation set" clause | **Reworded** so it is the book's own inference rather than a quotation attributed to the authors: "In effect, the repeatedly queried test set had become a validation set." This follows from the confirmed repeated-submission exploit. |
| Chapter 6 "internal Anthropic model" clause | **Stays removed.** No source was found. |
| Chapter 2 methods trail | **No note added.** The chapter already fences the 2.636 claim as a result under the author's own evaluator, not a new state of the art. The evidence appendix labels it "Run, on a bounded problem". |
| Part-page and divider drafting comments | **Removed.** Only production comments remain: the `VISUAL`/`DIAGRAM` art directions and one structural note explaining invisible layout code. |

**Manuscript status: ready for proofreading.** No author decisions are open. The remaining production work is listed in REVISIT: figures and art, front matter, clearance, and the printer.

## Chapter 7 revision draft (for author review)

Requested by the author after the Bradley–Terry comparison and discussion of the chapter's arc. The draft adds the chapter's own definition and outside evidence, and trims survey material.

**Sources, all read in full:**
- Lilian Weng, "Harness Engineering for Self-Improvement" (July 2026)
- The Anthropic Institute, "Recursive self-improvement" (2026, updated 18 September)
- Zheng et al., "Dream-RSI" (arXiv:2609.14858, September 2026), from a PDF the author supplied

Milanfar's essay could not be fetched here. Its expanded description follows search summaries of the essay and must be checked against the text.

**Added:**
- **Definition, after Good.** Yudkowsky's phrase, Weng's harness-level broadening and Anthropic's "designs its own successor", followed by the chapter's own stricter test with three conditions: second-order, stated conditions, judged by something the system does not control.
- **The Learner Dreams.** Dream-RSI as a careful real version of the store agent's simulator proposal: replay only over recorded outcomes, only the strategy code editable, redeployed online each round. Its guarantee holds only on recorded history.
- **The Learner Edits the School.** Weng's ladder (prompts → context → workflow → harness → optimizer), the Darwin Gödel Machine's 20 → 50% with a fixed model, and STOP degrading on weaker models.
- **Experiments on the Laboratory.** Anthropic's fixed-goal training-speedup test (about 3× → about 52×), with Anthropic's own caveat.
- **Before the Returns Arrive.** Milanfar's small-gain argument stated in full; the simulator as the self-model; Amdahl's law and review as the bottleneck.
- **New short section, "The Oldest Self-Improving Institution".** Science's changes to its own method as slow, externally judged self-improvement.
- **Constitution.** Agentic Harness Engineering's read-only verifier and predicted-impact edits, and Weng's "outside the loop".

**Trimmed:**
- the Pathak sentence
- the Montezuma's Revenge sentence
- the Hillis paragraph
- the Bajcsy/Brooks names, now one clause
- the architecture-search details

The trimmed sources move to Additional sources. Notes are renumbered 1–32.

**Net length:** about 6,070 → about 7,000 words.

**Gate:** seeds pass; build 319 pages, 87 illustrations, 0 placements needing review; references validate; unit tests pass.

**Open items:**
- Verify the Milanfar paraphrase against the essay.
- Confirm that the Weng-reported numbers (Darwin Gödel Machine, STOP, Agentic Harness Engineering) match the primary papers; arXiv is blocked here.
- Decide whether the Chapter 6 disclosure of reliance on Anthropic sources should mention the Institute piece.

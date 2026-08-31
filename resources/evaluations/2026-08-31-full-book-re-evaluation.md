# Full-Book Re-Evaluation — After the Storytelling and De-Linking Passes

*Date: 2026-08-31. Scope: all 13 chapters as they stand on `main` (re-read in full). Method: same rubric as the 2026-08-30 evaluation (`prompts/chapter-version-evaluation.md`), single-version scoring. Since that evaluation the manuscript received: the LLM voice de-patterning pass, the engaging word-choice pass (11 edits), and the storytelling pass on Chs. 7–8 with all inline citation links (102 across Chs. 7–9) moved to the references appendix.*

## 1. Verdict

**Book overall: 8.7 / 10** (up from 8.5). The two floor chapters have come up: Ch. 7 from 7.5 to 8, Ch. 8 from 7.5 to 8, Ch. 9 from 8 to 8.5. Nothing regressed. The manuscript now has **zero inline links in every chapter** — the "serious book, not survey" register is uniform for the first time — and the quantitative LLM-writing profile is clean across the board.

The 2026-08-30 evaluation's top finding — "the middle sags into survey mode" — is now substantially resolved at the sentence and structure level. What remains of it is smaller and different in kind (see §4).

**One recommendation formally withdrawn:** the Ch. 3 history compression. On re-read with the author's framing, "How We Got Here" is not a run-up — it is the bottom-up *derivation* of the five-layer map. The reader watches Layer 1 assemble itself ("my first agent-computer interface was copy and paste"), then Layer 2 (app builders), and the Merge Sort demo is Layer 3 becoming visible. Cutting it would leave the Five Layers section asserting a map the reader never earned. Both evaluators (this one and the independent GPT read) pattern-matched on length without crediting the section's argumentative function. Closed.

## 2. Scorecard

Scores /10. Δ marks change vs. 2026-08-30. One-liner % re-measured today.

| Ch. | Title | Words | Arc | Voice | Discovery | Human feel | 1-line % | Overall | Δ |
|----:|---|---:|:-:|:-:|:-:|:-:|---:|:-:|:-:|
| 1 | Why I'm Betting on AI Agents | 3,247 | 8 | 9 | 8 | 9 | 29% | **8.5** | — |
| 2 | The Algorithm Vortex | 5,159 | 9 | 9 | 9 | 9 | 38% | **9** | — |
| 3 | The Vibe Coder's Seat | 8,068 | 9 | 8 | 9 | 8 | 36% | **8.5** | arc +1 |
| 4 | System 3 | 5,086 | 9 | 10 | 9 | 9 | 39% | **9.5** | — |
| 5 | The Society of Agents | 5,691 | 9 | 8 | 9 | 9 | 29% | **9** | — |
| 6 | Pattern Language | 4,515 | 8 | 8 | 7 | 8 | 35% | **8.5** | — |
| 7 | Recursive Self-Improvement | 6,486 | 8 | 8 | 7 | 8 | 34% | **8** | +0.5 |
| 8 | Scalable Oversight | 4,245 | 8 | 7.5 | 7 | 8 | 27% | **8** | +0.5 |
| 9 | Layer 4 | 4,001 | 8 | 8 | 8 | 8 | 37% | **8.5** | +0.5 |
| 10 | Fluent Autonomy | 2,200 | 8 | 8 | 6 | 8 | 38% | **8** | — |
| 11 | The Store That Builds Itself | 5,573 | 9 | 9 | 9 | 9 | 22% | **9** | — |
| 12 | After Capacity | 5,810 | 8 | 9 | 8 | 9 | 32% | **8.5** | — |
| 13 | The Prophecy | 636 | — | 9 | — | — | n/a | **8 (as coda)** | — |

Book total: 60,717 words. LLM-tell census: "X is not Y. It is Z." pivots ≈ 29 book-wide (~0.5/1k words, signature instances only); "This/That is where" 14; em-dash rate 0.2–3.7/1k (human range); phrase tells ("serves as", "plays a crucial role", "not only…but also") ≈ 0; tier-1 AI-ism vocabulary 0; inline links 0.

## 3. What the recent passes changed, chapter by chapter

**Ch. 7 (7.5 → 8).** The 43 citation parentheticals were the single biggest texture problem — every few paragraphs the book stopped being a book. Gone. Three paragraphs that were method inventories (curiosity, meta-learning, harness reviews) now read as narrative; acronym lists (RL², MAML, RND) are dissolved into what-actually-happens prose with the citations in the appendix. The chapter's real spine — the teacher losing one job after another until only "deciding what deserves to count as better" remains — was always there; it now runs uninterrupted. What still holds it below the Ch. 2/4/11 tier: the reader hears about the field rather than watching the author in it. The author has (correctly) declined to invent experiments; the honest residual options are operator's-chair beats ("I watched an agent do X" where true) or acceptance that this is the book's survey-of-record chapter told well.

**Ch. 8 (7.5 → 8).** Biggest structural gain of the pass. The driving question — *how do you grade work you cannot do yourself?* — is now planted in the opening, and the oversight ideas arrive as a chain where each answers the previous one's failure (decomposition → debate → prover–verifier → weak-to-strong → constitutional) instead of "One move is… A second move is…". The "in studied settings" hedge boilerplate (×6) is gone; the "Anthropic's X work" roll call is thinned. The Nine Claudes section remains the chapter's best storytelling and now sits inside a story instead of a list. Residual: the interpretability instrument tour (features → diffs → circuits → NLA → J-space) is still a tour, though now an escalating one; same first-person gap as Ch. 7.

**Ch. 9 (8 → 8.5).** Needed only the de-linking — its research was already woven into prose ("In a field experiment involving nearly a thousand high-school mathematics students…"). With the links gone and the earlier one-liner fix (63%→37%), nothing separates its texture from the top chapters. It is quietly one of the best-argued chapters in the book.

**Ch. 3 (arc 8 → 9).** No text change beyond earlier word edits; the score moves because the evaluation was wrong, not the chapter. See §1.

**Chs. 1, 2, 4, 5, 10, 12** absorbed 1–3 word-choice edits each (excel, formidable, evaporates, expert, uncannily, cheap-way-to-fool-yourself, etc.) — all strict improvements, no voice cost.

## 4. What remains (ranked)

1. **First-person presence in Chs. 7–8** — the only remaining gap between the middle and the top tier. Constraint from the author: no claimed experiments (none were run). Honest options: (a) operator's-chair commentary where the author has genuinely watched these dynamics (e.g., agents gaming evaluators in the Ch. 2/3 experiments — those observations are real and cross-referenceable); (b) accept 8/10 as the ceiling for these two chapters. Either is defensible; fabrication is not.
2. **Ch. 8 deferred restructure** — mostly superseded. The storytelling pass delivered the driving-question framing that was the core of the restructure proposal. A deeper catalogue trim (cutting one or two instruments from the tour) remains available but is now optional polish, not a structural need.
3. **Bold standalone aphorisms** (~56 book-wide, stable) — mostly definitional/signature; a design-level decision interacting with the pull-quote layer of the book design. Not prose defects.
4. **Forward-pointing chapter exits** — every chapter still ends on a hook. Judged an authored serialization device; a blind cold reader should confirm it doesn't read as formula.
5. **Missing inline figure PNGs** (Chs. 1, 2, 4) — unchanged asset issue; authorial call.

## 5. Caveat

As with Addendum 4 of the previous evaluation: this pass partly grades this evaluator's own edits (the Ch. 7/8 storytelling text). The score movements claimed here (+0.5 on three chapters) are the kind most susceptible to self-grading bias. The confirmation that matters is a blind cold read of Chs. 7 and 8 by a judge with no memory of the manuscript's history — a fresh GPT session or a human reader — asked only: "does this read like a book chapter or a literature survey, and does the middle of the book sag?"

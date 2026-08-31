# Version Comparison — Old Short Edition vs. Current Manuscript

*Date: 2026-08-31. Version A: the uploaded `system3_book_edited.txt` — the January 2026 short edition (Preface + 5 chapters + Prophecy + References + About the Author, ~20,740 words; "Power Mode and Agent Society" listed as future work). Version B: the current 13-chapter manuscript on `main` (~60,700 words). Method: `prompts/chapter-version-evaluation.md`.*

## 1. Comparison table

| Dimension | A (old edition) | B (current) | Winner | Reason |
|---|:-:|:-:|:-:|---|
| Core idea / originality | 7 | 9 | B | A stops at "the model is hollow, the scaffold does the work." B carries that seed through society → culture → self-improvement → oversight → Layer 4 → production, and earns "System 3 is science." |
| Narrative arc | 6 | 9 | B | A's arc ends at Ch. 4 and substitutes a Zen-koan recap for a conclusion. B has a genuine climb and a return to earth (Ch. 11). |
| Voice | 5 | 9 | B | A is the book *before* the voice work: staccato one-liners, "Read that again," "Holy shit" as a standalone paragraph, "**This is the future of software development.**", second-person hype narration ("you" at 16/1k words vs B's 4/1k). |
| Human-writing feel | 4 | 9 | B | A's LLM-tell metrics: em-dash 13.5/1k (B: 0.2–3.7), 249 bold runs in 20.7k words, 22 hype-phrase hits ("astonishing," "changed everything," "let that sink in"), consulting-deck templates ("**The Problem**: … **What We Know**: … **For Demos**:") repeated six times in Ch. 3. |
| Evidential discipline | 4 | 10 | B | A: "**2.636 (New State of the Art)** … a massive leap," "Claude Code solves 80% on SWE-Bench," "Saussure — prediction confirmed. This is a vindication," phase-transition physics claims, uncritical Kosinski six-year-old ToM claims, the coffee-extinction story played straight. B fences every one of these ("That sentence needs a fence around it," "Not literally… the historical claim would be silly"). |
| Technical precision | 6 | 9 | B | A is right in outline but loose in detail ("The 2015 Turning Point" for AlphaGo Zero, which is 2017; "80% SWE-Bench"). B is precise and survived a citation audit. |
| Pedagogy | 7 | 9 | B | A teaches fast (RL primer, OPRO, Bradley–Terry are compact) but in listicle form; B teaches through the experiments. |
| Humor / fireworks | 7 | 9 | B | Same jokes at core (pineapple, product managers, coffee test, camel). A adds a few gems B lost (see §2). B's jokes are better embedded. |
| Compression / pace | 8 | 6 | **A** | The one dimension A wins. 20k words, no sag, every section moves. B is three times longer and earns most of it, but A proves the spine survives radical compression. |
| Memorability of slogans | 8 | 7 | A~ | A is slogan-dense to a fault, but several individual lines are stronger than anything B kept (§2). |
| Book-level coherence | 6 | 9 | B | A promises Trust/Desire/Society problems and then defers two of them to "future work." B delivers all of them. |
| **Overall** | **6/10** | **8.7/10** | **B** | A is a strong long essay wearing LLM styling; B is a book. |

## 2. What A still does better — worth stealing back

1. **A preface exists.** B has none. A's preface does real jobs: explains the cover (Saussure and Wittgenstein as the two figures), makes the promise ("give an agent a problem and go to bed"), and sets the tone. The execution is hype-heavy, but the *slot* is empty in B and shouldn't be. A rewritten preface in current-B voice is the single highest-value theft.
2. **The Zen of Autonomy** (`>>> import autonomy`). "Conditions over commands. / The farmer grows nothing. The plant does. / … / The tongue cannot reach the ear. / Build a system that can check." Genuinely memorable, format-native to the book's world, and gone from B. Perfect back-matter (after Ch. 13, or facing the references) — updated with lines from the new chapters.
3. **The epigram:** *"The impressive part is how far you can get with the right architecture. The dangerous part is forgetting that the architecture is doing the work."* Appears twice in A, zero times in B. This is a book-on-a-postcard sentence.
4. **"Decaf confidence."** A: "decaf confidence, indistinguishable from the real thing until the moment it matters." It plants the Prophecy's "Decaf." punchline 200 pages early. B lost the plant; the payoff is still there. Restore the plant.
5. **"The model is a mirror. The architecture determines what it reflects."** Stronger than several aphorisms B kept.
6. **Camel answer #7 with mischief.** A: "I could be lying to prove a point about trusting sources on the internet. In fact, if I told you it was AI-generated, you'd likely believe that too, because it fits a pattern you recognize." B's answer 7 is drier (metadata, signing). A's twist is the better epistemology joke.
7. **Concrete details B dropped:** the epistemic-swe base model is named (DeepSeek Reasoner) and the 13579 patch sizes are given (1941 vs 1169 lines). B says "the same base model" and "substantially larger" — the old numbers are stricter. Worth restoring to Ch. 4 if they're accurate to the run.
8. **About the Author.** "He lives with his wife and four kids, reads constantly, and finds that building things is how he thinks best" — B's repo has no author page; the last line is good.

Do **not** steal back: the Trust/Desire/Society "three problems" frame (B dissolves them properly across chapters), the "phase transition" physics, the second-person narration, the OPRO "take a deep breath" set piece at its old length, or the six-challenge deck structure.

## 3. What B genuinely improves

Everything the last four months of passes were for: the twelve chapters A only promises; the fenced claims (2.636, Saussure, diagonal layering novelty); the first-person witness (A: "The results were astonishing"; B: "I want to be careful with the word *discovered*"); the epistemic-swe failure told as a failure instead of "mixed results" theater; the removal of every deck template; the citation layer with a verified appendix; and a voice that survives an LLM-writing audit A would fail on page one.

## 4. LLM-writing audit of A (the short list)

Fails the book's own rubric on: excessive one-line paragraphs used as drum hits; bold-slogan density (~12 bold runs per 1,000 words); "Here's where it gets wild / interesting"; artificial mini-climaxes ("Read that again," "Stop and let that sink in," "Holy shit" standalone); em-dash rate 13.5/1k; every section ending on a quotable; hype superlatives on the author's own results. These are exactly the patterns the current manuscript's de-patterning passes removed — A is a preserved specimen of what the book was escaping.

## 5. Verdict

Base manuscript: **B, unambiguously.** A is valuable as (a) a quarry for the eight thefts above, (b) proof the spine can compress to 20k words — useful if a talk, article, or sample chapter is ever needed — and (c) a before photo for the voice work. Estimated effort to harvest: one short pass — preface slot, Zen page, epigram, decaf plant, camel answer #7, two data details. None of it requires reopening any chapter's structure.

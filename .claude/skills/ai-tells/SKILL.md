---
name: ai-tells
description: Find and fix prose patterns that make writing read as machine-generated, for this book's chapters or any long-form nonfiction. Use when asked to check a chapter for "LLM writing", "AI tells", human feel, or to humanize or de-slop prose. Produces flagged lines with suggested rewrites; edits only when asked.
---

# AI tells: detection and repair

Use this to review prose for patterns readers associate with machine writing. The goal is
not to pass a detector. It is to make every paragraph sound like a particular person who
was there, thinking.

The baseline for this book is Chapters 4 and 5. Blind readers consistently scored them
highest because their ideas come out of scenes the author lived (the camel, Alberto, his
mother's face, his own failed experiment, the Amazon offer). Judge other chapters against
that, not against a generic standard.

## Step 1: Measure

Run the counter first and keep its numbers for the report:

```sh
python3 resources/editorial/check-tells.py <chapter-prefix> --lines
```

It counts paragraph-ending maxims, contrast constructions, citation chains and
cross-chapter references, with targets calibrated on Chapters 4-5. It is a flagger, not a
judge: read every hit in context.

## Step 2: Read for the tells

Read the whole chapter. Flag a passage only if you can quote it exactly.

### A. Structural tells (the ones blind readers penalise most)

1. **Summary maxim at paragraph end.** A short, quotable line that restates the paragraph
   ("Recursion compounds whatever the system is able to judge"). Keep it only if a scene in
   the same paragraph earns it. Chapters 4-5 end about a quarter of paragraphs this way.
2. **Citation chain.** Three or more sources in one paragraph, one sentence each
   ("X found... Y showed... Z argued..."). Keep one, tie it to the running scene, move the
   rest to notes or cut.
3. **Survey register.** A section that tours papers with no scene, no first person and no
   consequence for the chapter's running case.
4. **Invented example doing a lived example's job.** An imagined store, founder or
   traveller standing where an author's own experience would be stronger. Flag it, and
   do not invent autobiography to replace it: ask the author.
5. **Recap and signposting.** "This chapter...", "Here is...", "So we...", "As Chapter N
   showed", a closing paragraph that lists what the reader just read.
6. **Cross-chapter stitching.** References by chapter number, or callbacks a cold reader
   cannot decode ("Ines's team", "the borrowed beginner").
7. **Every section the same shape.** Thesis, example, citation, maxim, repeated.
8. **Coinage inflation.** Several new bolded terms in one chapter. The baseline spends a
   whole chapter earning one.

### B. Sentence-level tells

9. **Negative parallelism.** "Not X but Y", "X is not Y. It is Z", "not merely / not
   only", "less X than Y", "does not need to X. It only needs to Y".
10. **Rule of three.** Triplets of adjectives, examples or fragments by reflex
    ("patient, consistent and suspiciously fond"; "A cat. An intruder. A ghost.").
    One deliberate triplet per section is fine.
11. **Balanced hedge.** "It can help. It can also harm." Pairs that refuse to commit.
12. **Repeated formula.** The same construction used twice in a chapter ("Same X,
    different Y").
13. **Inflated significance.** "stands as a testament", "plays a pivotal role", "a
    profound shift", "underscores", "highlights the importance of".
14. **Vague attribution.** "Researchers have found", "experts say", "many argue", with no
    named source.
15. **AI-flavoured vocabulary.** delve, tapestry, landscape, realm, navigate (figurative),
    crucial, robust, seamless, foster, leverage, multifaceted, nuanced, intricate,
    showcase, embark, journey (figurative), unlock, harness.
16. **Em-dash and colon overuse.** More than a few per chapter, especially an em-dash
    pivot ("—it is substitution").
17. **Abstract nouns doing the work.** "Goals take shape through the interaction; they
    need to stay alive without becoming ownerless."
18. **Slogan in quotation marks.** A line presented as what a user would say that no
    user would say.

## Step 3: Protect what must stay

- Never edit or report fixes for `chapters/13-the-prophecy.md`. The fable is protected in full;
  only the author changes it.
- Read `resources/editorial/easter-egg-register.md` first. Confirmed seeds must survive
  (run `bash resources/editorial/check-eggs.sh` after any edit).
- Keep the author's best jokes and lines even if they match a pattern; the readers
  praised "Static. Static. Static. Jackpot.", `return True`, "back channel", "the unit is
  closer to the sigh", "Very efficient. Slightly evil."
- Keep lines the author has asked for (for example the Chapter 9 sentence about what
  remains in the vibe coder's seat).
- Never add facts, quotations or autobiography. A fix may cut, reorder, merge or rephrase.

## Step 4: Report

For each chapter, produce:

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|

Then a short verdict: the chapter's three biggest problems, the checker numbers, and
which fixes need the author (real scenes, real numbers) as opposed to line edits.

Only edit the manuscript when explicitly asked. When editing, rebuild references if
citations change, regenerate `prompts/notebooklm` briefs, and run the seed check.

# Arc and part-structure edit

Prepared 27 September 2026 for Hani Al-Shater. Base: `480c2e6` (Build current full-book PDF). Two passes: the first implemented the agreed structure; the second revised it after an outside review (GPT) and the editor's own re-evaluation.

## Brief

Implement the arc agreed in conversation on 27 September: the book as an emergent architecture (complexity over engineering, emergence over design, capacity over power), with science at its center and what the capacity means for humans at its end. Add part pages, a page that celebrates the reveal, a place before the human chapters that confronts the risks, and the Fisher quotation for the alternative ending. Protect Chapter 13. Flag every assistant-written sentence.

## The arc as delivered

| Section | Chapters | Question |
|---|---|---|
| Preface | — | The frame; plants the "loose cable" riddle. |
| Part I — Emergence | 1–3 | What happens when the machine owns the search? |
| Part II — Institutions | 4–5 | How do fallible knowers earn trust? (The central question is stated here.) |
| Reveal page | — | *We call it science.* |
| Part III — Science Turns Inward | 6–8 | Opens with the reveal's explanation and "One question remains". |
| Interlude — When It Goes Wrong | — | The records survive while objections lose their consequences. |
| Part IV — Keeping the Human | 9–10 | How does the human stay in control? |
| Part V — What the Capacity Is For | 11–12 | The ending I want. |
| Chapter 13 | 13 | The alternative ending (labelled in the table of contents only). |
| Fisher page | — | The realist verdict, after the fable. |
| Scaffolds page | — | The book's answer and last word. |

## How much is new text

| Item | Author's text | Assistant-drafted (flagged) |
|---|---|---|
| Part epigraphs | Zen of Autonomy lines, unchanged | Choice of lines, part titles |
| Part II | Central question from the README | One lead-in sentence (10 words) |
| Reveal page and Part III opener | All of it, moved verbatim from the end of Chapter 5 | One sentence: "The rest of this book" → "The next three chapters" |
| Interlude | — | About 470 words, the whole file |
| Fisher page | The quotation (Fisher) | Attribution line |
| Note on Evidence | — | Interlude row; Chapter 13 "A fictional coda" → "The alternative ending" |
| References | — | Lysenko, Vavilov, Fisher, Jameson entries |

Flags are HTML comments (`CLAUDE DRAFT`, `CLAUDE EDIT`, `MOVED, NOT WRITTEN`, `STRUCTURAL`). Pandoc drops them from the PDF.

## Outside review and response

GPT reviewed the first pass (score 7.5/10: "the structural idea is stronger than the added prose"). It read the complete patch, including this record's first version, so it was not blind to the editor's reasoning. Its findings and the response:

| Finding | Response |
|---|---|
| Part structure, epigraphs, central question, reveal page, moving Chapter 5's question to Part III: keep | Kept |
| The reveal's aftermath is too ceremonial: several endings and beginnings in a row | Fixed. The three explanatory paragraphs moved onto the Part III page, ahead of "One question remains"; one page turn fewer |
| The interlude interrupts an excellent 8→9 transition ("The overseer is not ground truth" → "Find me the cheapest flight") | Mitigated. The author asked for a place before the human chapters, and the Part IV page already sits there; the interlude was halved and now ends on a concrete image rather than a map of the book |
| The interlude promises answers later chapters do not give ("The rest of the book takes them in turn") | Fixed. No promise; it raises the stakes only |
| "Outside the box" contradicts Chapter 5: science works without a civilization-wide supervisor | Fixed, and the most important correction. The failure is now objections losing their consequences, with Lysenko at the center. This also sharpens the thesis: science is the institution where an objection can change what happens next |
| Narration of the manuscript ("For eight chapters…", "Chapter 5 already contains…") | Removed. One cross-reference to Chapter 8 remains |
| "Capacity that no longer needs people no longer needs their consent" is an unargued absolute | Replaced with the bargaining-power argument |
| The Fisher page overdetermines the fable and previews its punchline | Partly accepted. The page moved after Chapter 13, so the fable is met freely and "Capitalism doesn't." is not previewed. The author's request that the reader know it is an alternative ending is kept as a table-of-contents label only |
| Protect a seed's function, not its wording; speculative readings should not be enforced | Fixed. The checker fails only on confirmed seeds and warns on proposed ones; the register says anchors are pointers |
| Why science and not law or a market: the reveal adds emphasis, not evidence | Not addressed in this pass. It needs the author's argument, not structure |

Where the editor's own evaluation and GPT's agreed independently (the Part IV mismatch and the ceremony after the reveal), those were treated as the most reliable findings.

## Verification

- Chapters 1–4, 6–13, the scaffolds page, the Zen appendix and About the Author are byte-identical to the base.
- The nine paragraphs removed from Chapter 5 are present verbatim in the reveal and Part III files (checked by script).
- Every commit builds a PDF with the repository's pandoc/xelatex command; the final build is 226 pages (base 213).
- `check-eggs.sh` passes: 6 confirmed anchors, 30 proposed. A deliberately broken confirmed anchor fails the check; a broken proposed anchor only warns.
- Transitions read in the built PDF: 3 → Part II → 4; 5 → reveal → Part III → 6; 8 → interlude → Part IV → 9; 10 → Part V → 11; 12 → 13 → Fisher → scaffolds.

## LLM-writing audit of what remains

- "Every part of System 3 can survive this." A provocation, deliberately unqualified; it is the interlude's claim.
- "If there is a non-benign superintelligence in our future, I expect it to look less like a monster than like this…" Carries the superintelligence risk the author asked for; first-person and hedged.
- "In 1948 the journals kept coming out." Short closing line; it replaces a paragraph that mapped the rest of the book.
- The voice is still the editor's. The interlude should be rewritten by the author before acceptance.

## Claims to verify before publication

- The Fisher quotation's exact wording (chapter 1 title of *Capitalist Realism*, 2009).
- Lysenko: the August 1948 VASKhNIL session and the Central Committee approval announcement; decline of Lysenkoism in the mid-1960s. Vavilov: died in prison in 1943.
- Editions and publishers of the new references.

## Left for the author

1. Rewrite the interlude in your voice, or cut it.
2. Keep or delete the table-of-contents label (`chapters/alternative-ending.md`).
3. Confirm or delete the proposed easter eggs; confirmed ones become enforced.
4. The flagged Part III sentence: keep "The next three chapters" or revert to "The rest of this book".
5. Why science and not law, a market or a bureaucracy: name which functions make the architecture science (independent disagreement, instruments with track records, provenance, allocation to the weaker program, objections with consequences), and consider running one of Chapter 5's proposed tests.
6. Not touched: Zalando in Chapter 11 and About the Author; Amazon in Chapter 5; `book-design/render.py` does not know about the new pages.

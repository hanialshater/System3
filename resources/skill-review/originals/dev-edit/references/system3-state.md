# System 3 — state as of 3 October 2026

Snapshot from `main` at `61c177f`. The repo moves daily; re-read `resources/editorial/working-spine.md` and the newest files in `resources/evaluations/` before relying on anything here.

## Locked spine (agreed 27 September, revised since)

- **Theme:** the architecture of autonomy is emergent. Complexity over engineering, emergence over design, capacity over power.
- **Center:** the architecture that emerges from repairing autonomy's failures is science.
- **End:** what that capacity could mean for humans; a hoped-for future, then an alternative ending that complicates it through desire, dependence and power.

| Section | Chapters | Question |
|---|---|---|
| Preface | — | The frame; plants the riddle ("we have built it before… at least one loose cable"). |
| Part I — Emergence | 1–3 | What happens when the machine owns the search? |
| Part II — Institutions | 4–5 | How do fallible knowers earn trust? |
| Reveal page | — | *We call it science.* (reveal and definition share one page) |
| Part III — Science Turns Inward | 6–8 | What happens when the institution becomes executable? |
| Interlude — When It Goes Wrong | — | Records survive while objections lose their consequences; two routes. Raises stakes, promises nothing. Ends "In 1948 the journals kept coming out." |
| Part IV — Human Purposes | 9–10 | What can inquiry discover about human purposes, and what authority can it not supply? |
| Part V — What the Capacity Is For | 11–12 | The ending I want. |
| An Alternative Ending + Ch 13 | 13 | The ending power wants (capitalist realism). Fable stays unexplained. |
| Scaffolds page | — | The last word; pairs with the reveal page. |

Part pages: title + one Zen epigraph on one page; they turn toward the next part, never recap the last. Assembly order: `book-design/curated/book-order.json`.

## How the arc work went (so the next pass doesn't repeat it)

1. Claude read the repo and reported "two theses". The author answered with the three-movement framing; the "two theses" point was withdrawn.
2. The author: "Let's first agree on the arc, then discuss development edit." The arc table went through four rounds (parts, interlude, reveal page, alternative ending, easter eggs) before any file changed.
3. First implementation: part pages, reveal page, interlude (950 words, Claude's voice), Fisher divider, egg register.
4. Review (Claude, then GPT): the interlude's "outside the box" framing contradicted Ch 5; the Fisher quote spoiled the Architect's line; the register enforced guesses; the consent line was a slogan; "the rest of the book takes them in turn" overpromised; four page turns before Ch 6.
5. Second pass: interlude cut to ~400 words around Lysenko and one failure; reveal paragraphs folded; checker split confirmed/proposed.
6. Later passes (page-turning, AI-tells, copyedit) cut further; the revert list (`2026-10-02-cuts-revert-list.md`) records what carried value.

## Open structural issues

From the 30 Sept readiness evaluation, the 1 Oct full-manuscript evaluation and `arc_map.py` on 3 Oct:

- **Thesis vs evidence.** The claim is louder than the author's own runs. About six decisive experiments are proposed and none is run. Cheapest: the second coffee test, counting refused edits that came back and protected lines re-cut, from the repo's own evaluation logs. Also: separate specifically scientific devices from generic coordination (≈400 words at the reveal or in Ch 10).
- **Invented cases where lived ones are needed.** `AUTHOR:` markers in Ch 1, 2, 4, 5, 6, 7, 9, 11 and 12 ask for real scenes (Ines/Sam, Omar, the store, the jacket and the potter are invented or composite). These are author slots. Don't fill them.
- **Second half loses the first half's method.** Ch 8–9 read as literature surveys with a hypothetical attached; Ch 11's prototype is never shown (two sentences would fix it). First-person density: Ch 5–7 ≈ 2 per 1,000 words, Ch 8 ≈ 11, Ch 11 ≈ 7, other core chapters 14–39.
- **Balance.** Words per part: I 14,191 · II 12,114 · III 16,408 · IV 5,261 · V 10,557. Ch 6 (≈7,600 words, 40 notes, about ten philosopher introductions) and the first half of Ch 7 (≈15 learning methods) are where Part III can lose weight.
- **Blocked on the author.** The reveal's `ASSISTANT EDIT` block; the interlude's `ASSISTANT DRAFT` header; Ch 9 `SLOT 4`; Ch 2's ten missing figures and its methods trail for 2.636.
- **Title.** Still names Ch 10. Decide last.
- **Ch 13** is protected in full. Publisher-risk notes are author decisions, not edits.

## Protected

Ch 13 and the scaffolds page byte-for-byte; confirmed seeds in the register; author-restored lines (Ch 1 cat-obsession paragraph); Zen maxims the author kept on 30 Sept ("Ground every claim. Trace every source.", "The tongue cannot reach the ear."); the "fences" (Ch 2's 2.636 fence, Ch 4's negative result, Ch 11's losable A/B test); provocations hedged in the next paragraph rather than the next sentence.

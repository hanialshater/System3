# System 3 — state as of 3 October 2026 (snapshot, not a record)

Snapshot from `main` at `61c177f`, corrected against `155c3a1` on 3 Oct. The repo moves daily, and this file has been wrong before: on the day it was written it still listed four blockers that `ca80ba2` had settled on 30 Sept. Treat every line as a claim to check. Before quoting anything here, run from the repo root:

```
git log --oneline 155c3a1..HEAD -- chapters resources/editorial    # what changed since this snapshot
git grep -n -E "ASSISTANT (EDIT|DRAFT)|CLAUDE (EDIT|DRAFT)|SLOT ?[0-9]|AUTHOR:|Missing figure" -- chapters
python3 <skill>/scripts/arc_map.py chapters --order book-design/curated/book-order.json --markers
```

and read `resources/REVISIT.md` (its "Completed" list) and the newest files in `resources/evaluations/`. A blocker the grep and REVISIT don't confirm is closed. A number that differs from the rerun is stale; use the rerun.

## Agreed spine (27 September, revised since; check `resources/editorial/working-spine.md`)

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

Part pages: title and a Zen epigraph on one page; Parts II and III add their question. They turn toward the next part, never recap the last. Assembly order: `book-design/curated/book-order.json`.

## How the arc work went (so the next pass doesn't repeat it)

1. Claude read the repo and reported "two theses". The author answered with the three-movement framing; the "two theses" point was withdrawn.
2. The author: "Let's first agree on the arc, then discuss development edit." The arc table went through four rounds (parts, interlude, reveal page, alternative ending, easter eggs) before any file changed.
3. First implementation: part pages, reveal page, interlude (950 words, Claude's voice), Fisher divider, egg register.
4. Review (Claude, then GPT): the interlude's "outside the box" framing contradicted Ch 5; the Fisher quote spoiled the Architect's line; the register enforced guesses; the consent line was a slogan; "the rest of the book takes them in turn" overpromised; four page turns before Ch 6.
5. Second pass: interlude cut to ~400 words around Lysenko and one failure; reveal paragraphs folded; checker split confirmed/proposed.
6. Later passes (page-turning, AI-tells, copyedit) cut further; the revert list (`2026-10-02-cuts-revert-list.md`) records what carried value.

## Open structural issues

From the 30 Sept readiness evaluation, the 1 Oct full-manuscript evaluation and `arc_map.py` on 3 Oct. The evaluations quote chapter text as it was then; re-find each quote in today's file before repeating it.

- **Thesis vs evidence.** The claim is louder than the author's own runs. About six decisive experiments are proposed and none is run. Cheapest: the second coffee test, counting refused edits that came back and protected lines re-cut, from the repo's own evaluation logs. Also: separate specifically scientific devices from generic coordination (≈400 words at the reveal or in Ch 10).
- **Invented cases where lived ones are needed.** `AUTHOR:` markers in Ch 1, 2, 4, 5, 6, 7, 9, 11 and 12 ask for real scenes (Ines/Sam, Omar, the store, the jacket and the potter are invented or composite). These are author slots. Don't fill them.
- **Second half loses the first half's method.** Ch 8–9 read as literature surveys with a hypothetical attached; Ch 11's prototype is never shown (two sentences would fix it). First-person density (3 Oct): Ch 5–7 ≈ 2 per 1,000 words, Ch 8 ≈ 11, Ch 11 ≈ 8, other core chapters 14–40.
- **Recaps.** Ch 5 restates Ch 4's closing question almost word for word one page later; Ch 7 repeats Ch 5's "emotionally satisfying and institutionally almost worthless" and Ch 2's diagonal-layering behaviour change. Callbacks or re-teaching: the author decides.
- **Balance.** Words per part on 3 Oct (`arc_map.py`, fenced text counted): I 14,219 · II 12,156 · III 16,674 · IV 5,261 · V 10,557. Rerun before citing. Ch 6 (≈7,600 words, 40 notes, about ten philosopher introductions) and the first half of Ch 7 (≈15 learning methods) are where Part III can lose weight.
- **Blocked on the author.** The `AUTHOR:` questions above (`--markers` lists them), and Ch 2's methods trail for 2.636 (model, version, number of runs; 1 Oct evaluation, recommendation 3). The reveal and interlude drafts, `SLOT 4` and the Ch 2 figures were settled on 30 Sept (`ca80ba2`; REVISIT.md "Completed"); all ten Ch 2 figure comments now read `ART RESOLVED`.
- **Cross-chapter slips found 3 Oct.** Ch 10 L77 "In circle packing the scores ran from 2.26 to 2.636" against Ch 2 (one run 1.33 → 2.26, L59; best run 2.636, L209). Ch 12's close previews the fable's ingredients ("an octopus, a romance, two pills and, unfortunately, taxes"): registered as an octopus plant, so a question for the author (does it give the fable away?), not an edit.
- **Title.** Still names Ch 10. Decide last.
- **Ch 13** is protected in full. Publisher-risk notes are author decisions, not edits.

## Protected

- Byte-for-byte: Ch 13, the alternative-ending divider and the scaffolds page.
- Confirmed seeds in the register: protected for their function. The register says anchors are pointers, not protected wording; a rewording that keeps the seed working updates the anchor in the same commit.
- Lines the author restored or rewrote recently. On 3 Oct that meant the Ch 1 cat-obsession paragraph (lost in a merge, restored in `62fe9d8`), the Ch 1 opening he rewrote on 27 Sep (`aeddc03`, about 28 lines incl. L10 "Pineapple doesn't belong…", L30 "**Complexity over engineering** is…"), and the restores listed at the top of `2026-10-02-cuts-revert-list.md`. Re-derive with `arc_map.py --provenance 21` and the revert lists.
- Zen maxims the author kept on 30 Sept ("Ground every claim. Trace every source.", "The tongue cannot reach the ear."), and any line the Zen appendix, a part-page epigraph or `prompts/build_notebooklm.py` (`CORE[n]['keep']`) quotes.
- The "fences" (Ch 2's 2.636 fence, Ch 4's negative result, Ch 11's losable A/B test); provocations hedged in the next paragraph rather than the next sentence.
- Not protected any more: "The model stays hollow" (Ch 4), which the author removed himself in `cfade23` (30 Sep), though de-llm's list still names it.

There is no protected-lines file in the repo (3 Oct). To check a list, write the lines one per line to a scratch file and run `arc_map.py chapters --order … --protected <file>`; for each MISSING line run `git log -S"<line>" --oneline -- chapters`. If the author removed it, drop it from the list; if a pass did, it is a restore candidate. Suggest he keep one list in the repo (e.g. `resources/editorial/protected-lines.txt`) and a `.git-blame-ignore-revs` with the mechanical passes (`1bce77f`, `75e80c2`). Those are his calls.

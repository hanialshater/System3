# Audit: dev-edit

Skill: `orig/dev-edit` (SKILL.md, references/arc-toolkit.md, evaluation.md, implementation.md, system3-state.md, scripts/arc_map.py).
Repo read at `155c3a1` (3 Oct 2026). The state file's snapshot is `61c177f`; the only chapter change since then is `62fe9d8` (Ch 1 cat paragraph restored).

Script runs: `arc_map.py chapters --order book-design/curated/book-order.json` with `--handoffs --motifs camel,octopus,coffee,cable,tongue,Alberto --recaps --markers`, and without `--order`, under python3.11 and python3.12. No crashes; the two versions give byte-identical output. Recaps take 2.3 s. Outputs saved in `scratchpad/author-skills/audit-work/`.

Ordered by priority.

---

## 1. gap: nothing tells the skill whose words a line is (the aeddc03 problem)

**Evidence.** On 27 Sep the author rewrote the opening of Ch 1 himself (`aeddc03`, "Revise Chapter 1 book introduction and restore cat obsession joke"). `git blame -w -M` still gives 28 of Ch 1's lines to that commit, among them L10 "Pineapple doesn't belong. I will die on this hill.", L26 "I have spent a respectable amount of my career…" and L30 "**Complexity over engineering** is a deliberately uncomfortable way to name my bet." Five days later the AI-tells report flagged L30 as a "repeated formula" cut candidate (`resources/evaluations/2026-10-02-ai-tells-report.md:47`, carried into the approval list as C1-1), and nothing in that report says the line was the author's fresh rewrite. The skill has no step that would catch this. Phase 0 reads the records and runs `arc_map.py`, but never asks git who last touched a line. Phase 5's "author-restored lines" covers only lines restored after a cut, not lines the author wrote recently.

Blame needs care in this repo:
- Mechanical passes hide authorship. Without `--ignore-rev 1bce77f --ignore-rev 75e80c2` (typography and copyedit), blame finds only 26 of the 28 lines.
- The author's name on a commit doesn't prove he wrote the words. `8bcaac3` "Apply developmental edit F…" is under his name but applies Claude's edit. Treat provenance as a prompt to ask him, not as proof.
- It works in the other direction too. The author removed "The model stays hollow" from Ch 4 himself (`cfade23`, 30 Sep), yet de-llm's protected list still names it. That list is now asking an editor to defend a line the author dropped.

**Fix: SKILL.md, Phase 0.** Add after the `arc_map.py` bullet:

> - Find out whose words they are. Run `arc_map.py … --provenance 21` on every file you may touch. It lists the lines the author changed himself in the last three weeks, with commit and date. A commit under his name can still carry an assistant's edit, so read the commit message; when in doubt, ask.

**Fix: SKILL.md, Phase 5.** Add a rule after "Don't cut load-bearing sentences.":

> - **Recent author lines are his decisions, not candidates.** Before proposing a cut or rewrite, check the line's provenance. If he wrote or rewrote it in the last few weeks, don't put it on the cut list. Put it under "Your decisions", with the commit and date ("you rewrote this on 27 Sep in aeddc03; it reads as a repeated formula because…"). The cut log gets a column, *last changed by*.

**Fix: arc_map.py.** A new mode (prototype tested under 3.11 and 3.12 in `audit-work/provenance_proto.py`; it lists all 26–28 aeddc03 lines in Ch 1 at `--provenance 14`):

```python
import subprocess, time
BOTS = re.compile(r"^(Claude|github-actions)", re.I)
IGNORE = [".git-blame-ignore-revs"]  # typography/copyedit passes, one sha per line

def provenance(path, days):
    """Lines the author (not Claude, not a bot) last changed in the past `days`."""
    p = Path(path).resolve()
    cmd = ["git", "-C", str(p.parent), "blame", "-w", "-M", "--line-porcelain"]
    root = Path(subprocess.run(["git", "-C", str(p.parent), "rev-parse", "--show-toplevel"],
                               capture_output=True, text=True).stdout.strip())
    if (root / IGNORE[0]).exists():
        cmd += ["--ignore-revs-file", str(root / IGNORE[0])]
    out = subprocess.run(cmd + ["--", p.name], capture_output=True, text=True, check=True).stdout
    cutoff, n, hits = time.time() - days * 86400, 0, []
    sha = who = summ = ""; t = 0
    for line in out.splitlines():
        if re.match(r"^[0-9a-f]{40} ", line): sha = line[:7]
        elif line.startswith("author "): who = line[7:]
        elif line.startswith("author-time "): t = int(line[12:])
        elif line.startswith("summary "): summ = line[8:]
        elif line.startswith("\t"):
            n += 1; text = line[1:].strip()
            if text and not text.startswith(("<!--", "```", "![")) and not BOTS.match(who) and t >= cutoff:
                hits.append(f"  L{n:<4} {sha} {time.strftime('%d %b', time.localtime(t))}  {summ[:45]:45}  {text[:80]}")
    return hits
```
and in `main()`:
```python
    ap.add_argument("--provenance", type=int, metavar="DAYS",
                    help="lines the author changed himself in the last DAYS days")
    ...
    if a.provenance:
        print(f"\n== author's own changes in the last {a.provenance} days (ask before cutting)")
        for n, _ in files:
            hits = provenance(Path(a.dir) / n, a.provenance)
            if hits: print(f"\n{n}\n" + "\n".join(hits))
```
Suggest that the author add a `.git-blame-ignore-revs` to the repo with `1bce77f` and `75e80c2` (plus later mechanical passes). That is his call. The skill shouldn't add it on its own.

---

## 2. wrong: system3-state.md "Blocked on the author" was already resolved when the snapshot was taken

**Evidence.** `system3-state.md:43` lists four blockers: "The reveal's `ASSISTANT EDIT` block; the interlude's `ASSISTANT DRAFT` header; Ch 9 `SLOT 4`; Ch 2's ten missing figures and its methods trail for 2.636."
- `git grep -c -E "ASSISTANT EDIT|ASSISTANT DRAFT|SLOT ?[0-9]|Missing figure" 61c177f -- chapters` → no hits, and none at HEAD either.
- `ca80ba2` (30 Sep, "Resolve remaining author decisions: accept drafts, remove SLOT 4…") removed them, and it is an ancestor of `61c177f`.
- All ten Ch 2 figures are `<!-- ART RESOLVED — … -->` at `61c177f` (`git show 61c177f:chapters/02-the-algorithm-vortex.md | grep -c "ART RESOLVED"` → 10).
- `arc_map.py --markers` finds none of the four. Every marker it reports is an `AUTHOR:` question.

Only the 2.636 methods trail is still open (`2026-10-01-full-manuscript-evaluation.md:465`, "Add a methods box to Ch 2").

**Fix.** Replace line 43 with:

> - **Blocked on the author.** The `AUTHOR:` questions above, and Ch 2's methods trail for 2.636 (model, version, number of runs; 1 Oct evaluation, recommendation 3). The reveal and interlude drafts, `SLOT 4` and the Ch 2 figures were settled on 30 Sept (`ca80ba2`; figures now `ART RESOLVED`).

Also add to the header (line 3): "Check every item here with `arc_map.py --markers` before quoting it; a state file is a list of claims, not a record." See also new check B.

---

## 3. bug: `--recaps` misses the real repeats and reports only a false positive

**Evidence.** With the default threshold of 0.45 the whole book gives one hit, and it is the Part V epigraph quoted in Ch 11 ("A philosophy of emergence should be willing to lose an A/B test."), which is deliberate. Real cross-chapter repeats get through:
- `05:` "The question is how a population of fallible knowers can build knowledge together without losing contact with the world." This repeats the last line of Ch 4 almost word for word, one page later. It shares 6 five-word shingles but scores below 0.45 because the ratio divides by the length of the later sentence.
- `07:` "Telling people to be more careful is emotionally satisfying and institutionally almost worthless." ≈ `05:` "…tell everyone to be more careful, which is emotionally satisfying and institutionally almost worthless…"
- `07:` the diagonal-layering behaviour change ≈ `02:` "The agent spent less time inventing new geometries…"

At 0.3 and 0.2 the noise rises ("I do not want to approve every comma" ≈ "I do not want to manufacture one"). The ratio is the wrong measure, whatever the threshold. A count of shared shingles (≥ 3), with blockquotes and part pages left out, gives 5 hits on the current text, and all 5 are either real repeats or deliberate callbacks for the author to judge.

**Fix (arc_map.py, replace the `--recaps` block):**
```python
    ap.add_argument("--min-shared", type=int, default=3,
                    help="recaps: shared 5-word sequences needed to report a pair")
    ...
    if a.recaps:
        print(f"\n== sentences sharing ≥ {a.min_shared} five-word runs with an earlier chapter "
              "(re-teaching or a deliberate callback: you decide)")
        prose = [(n, t) for n, t in main_files if not n.startswith("part-")]
        seen = []
        for n, t in prose:
            mine = [(s, shingles(s)) for s in sents(t) if not s.startswith(">")]
            for s, sh in mine:
                if len(sh) < 4: continue
                k, n0, s0 = max(((len(sh & sh0), n0, s0) for n0, s0, sh0 in seen),
                                default=(0, "", ""))
                if k >= a.min_shared:
                    print(f"\n  {n}: {s[:200]}\n    ≈ {n0}: {s0[:200]}  [{k}]")
            seen += [(n, s, sh) for s, sh in mine if len(sh) >= 4]
```
Drop `--threshold`. Also update `arc-toolkit.md:30` so it says the output is a list of candidates, and that a callback (Ch 12's "This is what I mean by the ideology vortex" echoing Ch 2) is not a recap.

---

## 4. bug: `body()` deletes every fenced block, so the Zen appendix vanishes

**Evidence.** `arc_map.py:21` strips every ```` ``` ```` block. The Zen appendix is one ```` ```text ```` block, so the table shows `appendix-zen-of-system-3.md` at **7 words** (`wc -w` gives 258). Its maxims are part pages' epigraphs and egg anchors ("The tongue cannot reach the ear." is in the register), but motifs, recaps and the word count never see them.

**Fix.** Strip only layout TeX:
```python
    t = re.sub(r"```\{=latex\}.*?```", "", t, flags=re.S)
    t = re.sub(r"(?m)^```\w*\s*$", "", t)   # keep the text of other fences, drop the fence lines
```
Tested on a copy under 3.11 and 3.12: the Zen appendix reads 256 words. Ch 4 goes from 4,548 to 4,590 because its prompt blocks now count, so recompute the part totals in the state file after the change. The `paras()` change in finding 5 was tested on the same copy: Ch 4's START now reads "Before we design another architecture, consider a camel. Here are seven claims about this image."

---

## 5. bug: `--handoffs` prints subtitles, captions and epigraphs, and skips the real chapter-to-chapter seam

**Evidence (current output).**
- Every chapter START begins with its italic subtitle: `01 START: *Simple building blocks, complex emergence* We humans are…`; `04 START: *Trust Chains, Tongue-Ear Tests…* Before we design another architecture, consider a camel. *The author at Krka National Park*`. The second "sentence" in the Ch 4 example is an image caption.
- Part pages sit in `main_files`, so the seam you see is `03-deep-mode → part-2-institutions` and then `part-2 → 04`. The seam the toolkit is about (Ch 3's last question against Ch 4's first line) is never printed. For four part pages, END is just the epigraph.

**Fix (arc_map.py).** In `paras()`, leave out a paragraph that is entirely italic when it is the first paragraph after the H1 or the paragraph after an image:
```python
def paras(t):
    out, prev = [], ""
    for b in body(t).split("\n\n"):
        b = b.strip()
        italic_only = re.fullmatch(r"\*[^*].*\*", b or "", flags=re.S)
        if b and not b.startswith(("#", "|", "!", "---", "```")) \
           and not (italic_only and (prev.startswith(("#", "!")) or not out)):
            out.append(" ".join(b.split()))
        prev = b or prev
    return out
```
In `--handoffs`, also print chapter-to-chapter across apparatus:
```python
        chaps = [(n, t) for n, t in main_files if not n.startswith("part-")]
        for (n1, t1), (n2, t2) in zip(chaps, chaps[1:]):
            ...
```
Keep the part-page seams as a second short list ("apparatus seams"). The ceremony check in arc-toolkit needs them.

---

## 6. wrong: Phase 5 freezes confirmed seeds; the register says not to

**Evidence.** `SKILL.md:55`: "Protected material stays byte-identical (System 3: Chapter 13, the scaffolds page, confirmed seeds, …). Verify with a diff." But `resources/editorial/easter-egg-register.md`: "Anchors are pointers, not protected wording. Protect what the seed does. If an edit improves the wording and the seed still works, update the anchor in the same commit." `system3-state.md:49` repeats the stricter version. A model following the skill will refuse wording fixes that the register allows, or will "verify with a diff" something no diff can verify.

**Fix.** `SKILL.md:55` becomes:
> - **Protected material stays byte-identical**: System 3's Chapter 13, the scaffolds page and the lines on the protected list. Verify with a diff. Confirmed seeds are protected for what they do, not their wording: an edit may reword one if the seed still works and the register's anchor is updated in the same commit (`check-eggs.sh` must pass).

At `system3-state.md:49`, change "confirmed seeds in the register" to "confirmed seeds (their function; see the register's rule on anchors)".

---

## 7. stale: implementation.md gates describe a build that no longer exists

**Evidence.**
- Gate 2 (`implementation.md:35`): "The CI joins chapters into one file; a duplicate key (`[^saussure]`…) silently prints the first chapter's note in both places." Today the curated build keys notes by `(chapter, key)` and raises on an undefined one (`book-design/curated/render.py:71-72`). `prepare()` raises on a duplicate within a file (`manuscript.py:108`). The chapters have no `[^…]` footnotes left at all; citations are `[n](appendix-references.md#…)`, checked by `validate_references` ("Uncited numbered references").
- Gate 5: "mirror the workflow file list with pandoc + xelatex". `.github/workflows/build-book-pdf.yml` has no file list. It runs `python book-design/pdf.py build --preview`, which reads `book-order.json`.
- Gate 6: `python -m unittest discover -s book-design/curated/tests` fails here with `ModuleNotFoundError: No module named 'PIL'`. The repo's `book-design/PDF.md:29-30,76` uses `.venv-pdf/bin/python`.
- Gate 7: "appears once in book-order.json and the workflow". The workflow lists nothing, and `manuscript.py:36-45` (`ordered_paths`) already fails the build on a duplicate, missing or unlisted file.
- `implementation.md:14`, `add_footnote(… collision check across all chapters)`, is now history.

**Fix.** Replace gates 2, 5, 6 and 7 with:
> 2. References: every `[n](appendix-references.md#…)` resolves and every numbered entry is cited. The build's `validate_references` checks both. A cut that removes the last citation of a source moves that source to "Additional sources"; say so in the record.
> 5. Build: `.venv-pdf/bin/python book-design/pdf.py build --preview` (setup in `book-design/PDF.md`). Then **read the transitions in the built text**: `pdftotext`, and print the pages around each seam. Render new single-line pages to PNG and look at them.
> 6. `.venv-pdf/bin/python -m unittest discover -s book-design/curated/tests -v` and `git diff --check`.
> 7. Assembly order lives in `book-design/curated/book-order.json`. The build refuses a missing or unlisted chapter, so a new file means a new line there.

Keep the `[^saussure]` story as one line of history if you want it, labelled as the old pandoc build.

---

## 8. stale: two examples in arc-toolkit no longer match the book

**Evidence.**
- `arc-toolkit.md:16`: "Ch 8 'the overseer is not ground truth' → Ch 9 'Find me the cheapest flight'". Ch 8 now ends "…neither, most days, does anyone else who is supposed to be there." The maxim lives only in `appendix-zen-of-system-3.md:43`. Ch 9 opens "The preface promised a cathedral while the coffee was still too hot." "Find me the cheapest flight" is at L9. The interlude and the Part IV page now sit between them.
- `arc-toolkit.md:26`: "octopus, cable, coffee, camel and tongue-ear threads make the fable in Ch 13 feel inevitable". By the register, the camel pays off in Ch 11 and Ch 12, not Ch 13, and `--motifs camel` finds no camel in Ch 13.

**Fix.** L16: "Good seams in System 3: Ch 3 ends 'How do you know what to trust?' → Part II; Ch 4 ends on how fallible knowers build knowledge together → Ch 5's sixteen Claudes. (A seam once ran Ch 8 → Ch 9 straight from philosophy into 'Find me the cheapest flight'; the interlude now sits there.)" L26: "System 3's octopus, cable, coffee, DNA-fax and tongue-ear threads make the fable in Ch 13 feel inevitable, and the camel comes back in Ch 11–12…"

---

## 9. stale/gap: state numbers drift, and the protected list had no check

**Evidence.**
- `system3-state.md:42`: "I 14,191". It is now 14,211, after `62fe9d8` restored the cat paragraph. The other part totals still match: II 12,114 · III 16,408 · IV 5,261 · V 10,557.
- The same numbers appear twice, in `arc-toolkit.md:28` and `system3-state.md:41`, and will drift apart.
- `system3-state.md:49` lists "author-restored lines (Ch 1 cat-obsession paragraph)" as protected, but at the snapshot commit `61c177f` that paragraph was missing (`git show 61c177f:chapters/01-… | grep -c obsess` → 0 after the merge loss that `62fe9d8` repaired). The skill named it and had no means to notice it was gone.
- The protected lists differ by skill. de-llm's `references/system3.md:45` has nine lines plus motifs; dev-edit names one line and two maxims. One de-llm entry ("The model stays hollow") was removed by the author himself (`cfade23`).

**Fix.** Keep numbers in one place: in arc-toolkit.md L28, replace the figures with "(see `system3-state.md`; rerun `arc_map.py`)". Update state L42 to 14,211, or say "rerun; these were the 3 Oct numbers". Move the protected lines into one file in the repo (e.g. a "Protected lines" section in `working-spine.md`, or `resources/editorial/protected-lines.txt`), checked like the eggs. Point both skills at it (see new check A).

---

## 10. gap: three flag vocabularies for the same thing

**Evidence.** `SKILL.md:54`: "`CLAUDE DRAFT` / `ASSISTANT EDIT`". `implementation.md:20-21`: `CLAUDE DRAFT BEGIN … END` and `CLAUDE EDIT (date)`. de-llm `SKILL.md:22`: `ASSISTANT EDIT (<pass name>)`. The repo's copyedit plan names `ASSISTANT EDIT` / `ASSISTANT DRAFT` / `CLAUDE DRAFT`. `arc_map.py:17` has to regex all four. A model is likely to mix them inside one pass.

**Fix.** `SKILL.md:54`: "**Flag every new or changed sentence** in the source with the flags in `references/implementation.md` (`ASSISTANT DRAFT` around new passages, `ASSISTANT EDIT` before a changed sentence, with the old wording). New argument passages can live in `drafts/` until the author writes them." At `implementation.md:20-21`, change `CLAUDE DRAFT`/`CLAUDE EDIT` to `ASSISTANT DRAFT`/`ASSISTANT EDIT`, so both skills use the repo's words. Leave the `MARKERS` regex as it is so old flags are still found.

---

## 11. polish: Phase 0 paths and reading load

**Evidence.**
- `SKILL.md:13` gives `REVISIT.md` and `easter-egg-register.md` without paths. They are at `resources/REVISIT.md` and `resources/editorial/easter-egg-register.md`.
- "the README spine": the README has no spine. It links to `working-spine.md`.
- `drafts/` (`SKILL.md:54`, `implementation.md:30`) doesn't exist. Say "create `drafts/` at the repo root".
- "the latest files in `resources/evaluations/`": that is 24 files and 82,000 words, more than the manuscript (≈ 68,000 by `arc_map`). A model told to read "the latest" may read them all.
- `SKILL.md:14` gives no command line.

**Fix.** Replace L13–14 with:
> - Read the standing records first. For System 3: `resources/editorial/working-spine.md` (the spine; the README only links to it), `resources/editorial/easter-egg-register.md`, `resources/REVISIT.md`, the house prompt `prompts/chapter-version-evaluation.md`, the newest two or three files in `resources/evaluations/` and any revert list (it records what the author took back). Skim older evaluations only for a question they answer. Old length targets and "locked" labels in past evaluations are history, not instructions.
> - Run `python3 <skill>/scripts/arc_map.py chapters --order book-design/curated/book-order.json --handoffs --recaps --markers --provenance 21` from the repo root. …

---

## 12. polish: smaller arc_map issues

- `load()` (`arc_map.py:52`) silently drops an `--order` entry whose file is missing, and silently ignores chapters missing from the order. Add:
  ```python
  if order:
      listed = set(names); disk = {p.name for p in d.glob("*.md")}
      for m in sorted(listed - disk): print(f"warning: in order but missing: {m}")
      for m in sorted(disk - listed): print(f"warning: not in order: {m}")
  ```
- `I/1k` (`arc_map.py:45`) is case-sensitive and leaves out `My`, `Me`, `I'd`, `I'll`. Ch 10 reads 39.0 now and 40.3 with them. The difference is small, but sentence-initial "My" is common in this author's openings. Use `r"\b(?:I|I[’']m|I[’']ve|I[’']d|I[’']ll|[Mm]y|[Mm]e|[Mm]yself)\b"`.
- `--motifs` matches only a leading word boundary (`arc_map.py:96`), so `cat` would count "category" and "cable" would count "cables". The second is wanted, the first isn't. Document it in `--help`: "matches word starts; add a trailing \\b yourself, e.g. 'cat\\b'". Also note that a lexical grid misses payoffs that don't repeat the word (Ch 13's "Decaf." for coffee), so read the register.
- `system3-state.md:24`, "Part pages: title + one Zen epigraph". Part I carries three maxims, Part II adds a question, and Part III has three paragraphs. Write "title and a Zen epigraph on one page; Parts II and III add their question".

---

## 13. gap/polish: description

The triggers are good for the author's own phrasing ("review the arc", "make this chapter a 9.5", "compare versions"). Gaps:
- It misses requests the skill itself covers: "blind read", "cold read", "how far from publishable", "readiness".
- "asks for scores per chapter" collides with levantine-translate ("evaluate an Arabic chapter") and could fire on an Arabic chapter score.
- "restructure" alone is broad, though in this repo that is low risk.
- The repo also has `.claude/skills/development-edit`, a Claude-drafted skill with overlapping triggers. If both are installed they will compete for the same requests. The author should keep one.

**Replacement:**
```
description: Structural editing for a nonfiction book or long essay: reviewing and locking the arc and central thesis, part structure, chapter order and handoffs, narrative momentum, seeds and payoffs, then planning, implementing and evaluating a development edit as reviewable patches. Use whenever the user asks to "review the arc", "evaluate the thesis", "development edit", "dev edit", "narrative momentum", "make this chapter a 9.5", "how far from publishable", "blind read" or "cold read", "compare versions", "benchmark against Sapiens / Life 3.0 / Human Compatible", "restructure the book", "part pages", or asks for scores per chapter, for System 3, The Dream, Coffee & Commute or long strategy documents. Sentence-level LLM tells belong to de-llm (use both when a pass touches both); fact-checking to fresh-claims; Arabic versions to levantine-translate.
```

---

## Cross-skill notes (outside dev-edit, found on the way)

- de-llm `references/system3.md:8` says "Chapter 13 gets typography only". The register's rule 5 says no pass touches Ch 13, and dev-edit says byte-identical. de-llm should match the register.
- de-llm `references/system3.md:13` says `check-eggs.sh` checks "footnote counts". It checks egg anchors only.

---

## New checks that would have caught these

**A. Protected lines (catches the lost cat paragraph, and the "stays hollow" entry the author dropped).** Add `resources/editorial/protected-lines.txt` (one exact string per line, `#` comments), and a mode to `arc_map.py`:
```python
    ap.add_argument("--protected", metavar="FILE", help="fail if any listed line is missing")
    ...
    if a.protected:
        whole = "\n".join(t for _, t in files)
        gone = [l for l in Path(a.protected).read_text().splitlines()
                if l.strip() and not l.startswith("#") and l.strip() not in whole]
        print("\n== protected lines missing" if gone else "\n== protected lines: all present")
        for l in gone: print(f"  MISSING  {l}")
        if gone: raise SystemExit(1)
```
Then run `git log -S"<line>" -- chapters` on each missing line. If the commit is the author's, take the line off the list; if it isn't, restore it.

**B. State freshness.** A short check at the top of system3-state.md, which the model runs before trusting the file:
```
git log --oneline 61c177f..HEAD -- chapters       # what changed since the snapshot
python3 scripts/arc_map.py chapters --order book-design/curated/book-order.json --markers
```
Any blocker in the state file that `--markers` doesn't find is closed. Any part total that differs is stale.

**C. Provenance** (`--provenance DAYS`, finding 1). It would have flagged L30 of Ch 1 as the author's 27 Sep rewrite before the AI-tells pass offered it as a cut.

**D. Recaps by shared run count** (finding 3). It would have caught the Ch 4 → Ch 5 repeated question, which the current default misses.

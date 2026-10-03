# Audit: art-direction skill

Skill: `.../batch2/art-direction/art-direction/` (SKILL.md 48 lines, references/rules.md, references/brief-template.md, scripts/art_audit.py).
Repo: `/home/user/System3` at `155c3a1`, untouched (`git status` clean at the end). Builds ran on a copy in `audit-work/art-direction/repo`.

## What I ran

- `art_audit.py --help`, default run, `--context`, under python3.11 and python3.12, with `--order book-design/curated/book-order.json`. Identical output under both. No crash, apart from a `BrokenPipeError` traceback when `--context` output goes into `head` (cosmetic).
- I compared it with the renderer in two ways:
  - (a) `audit-work/art-direction/renderer_mirror.py`, which imports `manuscript.py` and copies `render.py`'s `prep` and `blocks`;
  - (b) a real `pdf.py build --strict-art` on the copy, after `pip install --user reportlab PyMuPDF`. Typesetting finished: "Typeset 292 pages; 66 illustrations" and `resolved-art.json` = 76. Compositing then failed because the art files are Git LFS pointers (`a005.jpg: ASCII text`). That is an environment limit, so I could not test the strict-art gate end to end.
- On the real book the audit agrees exactly with the renderer: 25 MISSING, the same 25 ids the renderer leaves out. Every MISSING hit I checked by hand (a009, a023, a138, a162, a172) is a passage that has been cut.
- Synthetic chapter (`audit-work/art-direction/synth/`). I tested each case against the renderer: list items, a `[VISUAL …]` bracket brief, a footnote with a continuation line, an image caption, and an art entry for a chapter that has no file.

No paid APIs were needed. python3.12 has no `markdown_it` and pip is blocked by PEP 668. That is an environment limit; it only matters for the proposed fix in finding 2.

---

## Findings, in priority order

### 1. wrong: 25 of the book's images are not in the PDF today. The skill shows this but never says the gate is already failing.
Evidence: audit output, same on 3.11/3.12:
```
anchors to fix (the renderer omits these images):
   01-why-im-betting-on-ai-agents.md a009 MISSING Strong play developed along routes ...
   ... (25 MISSING: a009 a023 a028 a041 a044 a067 a122 a136 a138 a153 a155 a157 a160 a162 a170 a172 a176 a177 a178 a186 a187 a191 a211 ch2-reference ch2-search-roles)
```
- The renderer copy resolves 76 of 101 anchored entries. `pdf.py build --strict-art` therefore fails on the current `main` (`pdf.py:103,119`, `art_review_count`).
- Chapter 9 has lost 5 of its 5 images and Chapter 8 4 of 4.
- a138 already carries `previous_anchor` and `review_note: "Reconnected to the current passage…"` and is missing again. Anchors are being re-broken by later passes.

This is book state, not a script bug. Two things in the skill make it worse:
- SKILL.md:24 sends accepted art through a `--strict-art` build that cannot pass until these 25 anchors are fixed.
- The skill has no step for the repair.

Fix: add a repair step to SKILL.md after Workflow step 1:
> **Repair before judging.** For each MISSING image, find the passage it now belongs to (often the passage was cut and the picture belongs to its replacement, or to nothing). Repoint `after` in `book-design/curated/art.json`. Move the old text to `previous_anchor` and add a dated `review_note` ("Reconnected to … after reading the edited chapter and inspecting the illustration"), as a088/a125 do. If nothing in the chapter earns the picture any more, mark it unplaced instead of forcing a match. Anchors are pointers, not protected wording: update them in the same commit as the text edit (the rule in `resources/editorial/easter-egg-register.md`).

### 2. wrong: "It mirrors the renderer" is true for today's text only. The block model differs in four ways.
Evidence: `art_audit.py:19-22` splits the raw text on blank lines. `render.py:105-135` parses with markdown-it after `manuscript.prepare()`. Synthetic test `audit-work/art-direction/synth/ch/01-test.md`:

| case | renderer (`resolve_anchor`) | art_audit | error |
|---|---|---|---|
| anchor repeated in two items of a tight list | None (omitted) | OK | false negative |
| anchor also in a `[VISUAL …]` bracket brief | placed | AMBIGUOUS | false positive |
| anchor also in an indented footnote continuation line | placed | AMBIGUOUS | false positive |
| art entry for chapter 7 with no 07-*.md file | — | silently skipped | false negative |
| `[VISUAL …]` bracket brief | counted in `production-notes` | `briefs` = 0 | false negative |

There is also no exit status (`exit 0` with 25 problems), so neither book-build nor CI can use the audit as a gate.

Fix: have the audit import the renderer's own functions so the two cannot drift. A tested drop-in is at `audit-work/art-direction/art_audit_proposed.py`. Its core:
```python
sys.path.insert(0, str(repo / "book-design/curated"))
from manuscript import prepare, resolve_anchor, ordered_paths, structural_layout, REFERENCE_ANCHOR
from markdown_it import MarkdownIt   # book-design/requirements-pdf.txt
...
mine = [e for e in arts if (e.get("section") == p.name if e.get("section") else e.get("chapter") == ch)]
...
for e in arts:
    if e["id"] not in seen: problems.append(("-", e["id"], "NO SUCH SECTION", ...))
sys.exit(1 if a.strict and problems else 0)
```
On the real book it reproduces the same 25 MISSING. On the synthetic file it matches the renderer in every row above. Wrap the `markdown_it` import in a `try` that prints "pip install markdown-it-py (book-design/requirements-pdf.txt)" and exits 2. Update SKILL.md:20 to `python3 <skill>/scripts/art_audit.py --repo . --strict` (run from the repo root).

### 3. wrong: the placement rules contradict the renderer and the repo's layout strategy.
Evidence:
- SKILL.md:28 says "full width, never cropped, never beside a column narrower than 55 characters".
- `layout.json` `strategy`: "Full-width narrative scenes, outer-margin portraits and selective bottom-edge art".
- `render.py:290-298`: any image with aspect < 0.85 that follows a body paragraph goes into a side table with a 194 pt text column. At 11.5 pt Nimbus Roman that is about 37 characters. Eight current entries qualify: a083 a086 a090 a091 a100 a105 a109 a112.
- "Quiet" images are drawn 75–110 pt tall (`render.py:141-147`). Every interior image is a `clip` crop of a source page, and hero images bleed to the edge.
- "8–10 images per argument chapter" has no source in the repo. Current counts run from 2 (Ch 10) to 22 (Ch 5).

Fix: replace SKILL.md:28-29 with:
> - The curated renderer decides size: landscape scenes run full width (heroes may bleed), portraits sit in the outer margin beside a narrow column, and a few quiet images stay small (`render.py` `Art`, `layout.json`). If a portrait beside a ~37-character column reads badly, give that entry `max_height` or a wider clip; don't fight it in prose.
> - Density is a judgment, not a quota: an image where a sentence needs drawing, none where it doesn't (the 372-page proof had a picture on 229 pages and that was a defect; see book-build `references/defects.md`).

If 55 characters is a real requirement, it is a renderer change (raise `colWidths=[194,139]`), not a rule for the model to follow.

### 4. wrong: "openers with an empty title zone; typography goes in the layout" describes a mechanism the build does not have.
Evidence:
- SKILL.md:23, rules.md:20 and brief-template.md:12.
- In `render.py:169-172` the `Cover` flowable only paints the paper colour. At `render.py:341-343` each opener is inserted as a full-page image (`p.insert_image(p.rect, …)`). Nothing sets CHAPTER X / TITLE.
- The renderer drops a cover when the H1 differs from `provenance.json` `source_titles` (`render.py:236-237`). That only makes sense because lettering is baked into the 13 selected openers.
- `resources/art-direction/README.md`: "Preserve selected compositions, faces, lettering … Do not regenerate an opener merely because an old brief asks for it."

An opener generated the skill's way would print with no title.

Fix: SKILL.md step 4:
> Openers are already selected and carry their own lettering; the build places them as whole pages and drops one whose chapter title has changed (`provenance.json` `source_titles`). Don't regenerate an opener unless the author decides to. If he does, either letter it and proof the lettering letter by letter, or first add title setting to `Cover` in `render.py`. An empty title zone alone prints a chapter with no title.

In rules.md:20, replace `curated/provenance.json` with `book-design/curated/provenance.json`.

### 5. stale: the Chapter 5 worked example is a to-do list that has since been done, and two of its directions conflict with the repo.
Evidence (rules.md:22-33):
- "Add (3): the chapter opener (queue at the `linux/` door …)". `resources/art-direction/chapter-05-society-of-agents.md` says: "Conflicts with the selected full-image opener; do not replace that opener without a new design decision. Consider an interior treatment." The chapter now has `ART RESOLVED — ch5-linux-gate` as an interior figure.
- "the harness ladder" exists as `ch5-harness` (`technical_figures.py:28`).
- "seven panels matching the seven section headings". Chapter 5 now has 9 `##` headings (lines 63–283). The repo brief says "Show institutional functions, not historical stages". `technical_figures.py:30` is titled "Seven jobs—and an eighth: Functions of an institution, not stages of history".
- "the 50-page proof: 6.5 as a proof, 8 as art" (rules.md:12) has no source in the repo. The repo's README calls `evaluations/` "historical assessments".

Fix: retitle the section "Worked example: Chapter 5 in the 50-page illustrated proof (historical, Sept 2026)" and add one line:
> Since done: ch5-linux-gate (as an interior figure, not the opener), ch5-harness, ch5-institution (functions, not stages; the chapter now has nine sections). It shows the method, not current work. Current Chapter 5 backlog: `resources/art-direction/chapter-05-society-of-agents.md`.

Remove "the seven panels matching the seven section headings".

Side note for the author, outside the skill: that backlog file still says the seven briefs "remain in manuscript comments", but all seven are now `ART RESOLVED`.

### 6. stale: chapter numbers come from the 26 Aug evaluation's old numbering.
Evidence:
- SKILL.md:36: "robots almost gone by Ch 11".
- The source, `evaluations/2026-08-26-full-book-art-direction-evaluation.md:197,243,276-277`, numbers "Chapter 10: The Store That Builds Itself; Chapter 11: After Capacity", with Automatic Alignment Research not yet numbered.
- Today Ch 11 is the Store and Ch 12 is After Capacity (`provenance.json` `source_titles`). The NotebookLM style says "by the last chapters the robots almost disappear" (`prompts/notebooklm/chapter-05.md`).
- SKILL.md:35, "eleven posters", is the old opener count. There are 13 now.

Fix: SKILL.md:36 should read "…the human returning from the desire layer (Ch 9), robots almost gone by After Capacity (Ch 12)." SKILL.md:35 should read "…make a row of posters, not a sequence."

### 7. gap: the acceptance path skips the repo checklist's first step and the brief's after-life.
Evidence:
- `generation-checklist.md` step 1: "Start from the current chapter and the selected artwork register (`chapter-openers.md`). Confirm that the requested visual is still needed and is not already supplied." Steps 4–6 cover assets in `assets/art/`, `print-assets.json`, Git LFS and checksums. SKILL.md:24 condenses all this and leaves out the register and `print-assets.json`.
- The repo marks a finished brief as `<!-- ART RESOLVED — <id>. Original brief: … -->` (chapters/02, 05). The renderer only collects comments that begin with VISUAL/DIAGRAM as pending (`manuscript.py:89`).
- brief-template.md:17 says when a brief is done, but not what to do with the comment.

Fix:
- SKILL.md step 3: add "Check `resources/art-direction/chapter-openers.md` and the chapter's existing `art.json` entries first; the picture may already exist."
- brief-template.md:17: append "Then rewrite the comment as `<!-- ART RESOLVED — <art id>. Original brief: … -->` so the build stops listing it as pending."

### 8. gap: the build needs things the skill doesn't name.
Evidence: on a fresh copy, `pdf.py build` fails with `FzErrorFormat: unknown image file format`, because the assets are LFS pointers. It also needs `book-design/requirements-pdf.txt` (reportlab, PyMuPDF, markdown-it-py). See `book-design/PDF.md:13`.

Fix: SKILL.md step 5 should add "(needs `git lfs pull` and the `.venv-pdf` from `book-design/PDF.md`; without them, run the audit and say the visual check is still owed)."

### 9. wrong (small): photo58 is reported under "the renderer omits these images".
Evidence: the audit output has `04-system-3.md photo58 NO ANCHOR (handled specially or unplaced)`. The renderer places photo58 through the Chapter 4 image line (`manuscript.py:118-121`, `render.py:200` skips it on purpose). book-build `references/defects.md:15` therefore counts "26 of 102 art anchors missing" when the true number is 25.

Fix: in `art_audit.py`, skip `photo58` the way `render.py:200` does (`if e["id"] == "photo58": continue`). In book-build's defects.md, change 26 to 25.

### 10. polish: `--context` output is hard to read and leaves out the case that needs it.
Evidence: `art_audit.py:53` prints the context lines before the file's summary row (see the run: the a005…a014 lines come before `01-why…`). It prints nothing for MISSING entries, which are the ones where context is needed.

Fix: print the row first, then the context. For MISSING entries, print the old anchor and the closest surviving paragraph, using `difflib.get_close_matches(norm(after), nb, n=1, cutoff=0.5)`. Label the column `pre-head` rather than `at break`. The current check also counts the end of the file as a break, and SKILL.md never uses that column.

### 11. polish: the description could trigger on video-brief requests.
- The description lists "write a brief", and video-briefs also owns "briefs". "art for chapter N" and "evaluate the art" are good triggers.
- Near misses it should stay quiet on: "write the NotebookLM prompt for Ch 5", "build the PDF".

Fix: change "write a brief" to "write an image or art-generation brief". Add a final sentence: "Not for video prompts (video-briefs) or for building and proof-checking the PDF (book-build)."

### 12. polish: the style vocabulary is defined in two places.
SKILL.md:8,38 ("muted blue/ochre… Not every robot smiles") is close to `prompts/notebooklm/*` "Visual style" ("Prussian or denim blue, ochre, olive, warm gray… Neutral faces; they do not smile by default"), and video-briefs keeps its own `STYLE`. Nothing contradicts today, but the copies will drift.

Fix: add one line to SKILL.md: "The written style block in `prompts/build_notebooklm.py` (`STYLE`) is the shared wording; keep briefs consistent with it."

### 13. polish: the pass and fail examples cannot be checked from the repo.
The Kitcher notebook, YAML books, Duhem mouse and "five coats" images can't be confirmed from text alone. The art files are LFS, and only Ch 4's a063, which follows "We are all Alberto to someone", ties to a named example. They read as current faults.

Fix: start SKILL.md:16 with "In the 50-page proof:" so a model doesn't go looking for them as live defects.

---

## New script checks that would have caught these

1. **Renderer-backed resolution** (finding 2): the audit imports `manuscript.py`, so it cannot drift from it. Add a unit test in `book-design/curated/tests/test_build.py` covering the list-item, bracket-brief and footnote-continuation cases.
2. **`--strict` exit code** (findings 1, 2) so book-build and CI can gate on it. Better still, run the audit in the GitHub workflow before `--strict-art`, which needs LFS.
3. **Orphan entries**: an `art.json` entry whose `chapter` or `section` matches no file in `book-order.json`.
4. **Re-broken anchors**: list MISSING entries that already carry `previous_anchor` (a138 today). These point to a text pass that ignores the art.
5. **Side-wrap report** (finding 3): flag entries with aspect < 0.85 that follow a body paragraph, since they will sit beside the ~37-character column.
6. **Cover-title drift**: compare each chapter's H1 with `provenance.json` `source_titles` before the build. It is clean today, but a title edit silently drops an opener.
7. **Brief bookkeeping**: every `ART RESOLVED — <id>` id exists in `art.json` (clean today), and every open `VISUAL/DIAGRAM` brief, in a comment or in brackets, is listed per chapter.

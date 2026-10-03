# Audit: de-llm skill

Repo state read: `/home/user/System3` at `155c3a1` (3 Oct 2026). Skill: `orig/de-llm` (SKILL.md, references/catalogue.md, references/system3.md, scripts/tells.py, scripts/apply_pass.py). Both scripts behave identically under python3.11 and python3.12; nothing in the repo or skill folder was changed. Test copies and the test pass script are in `scratch-dellm/`.

## Measurements asked for

`tells.py --baseline` takes only one file, so Chapters 4 and 5 had to be concatenated by hand into `scratch-dellm/base45.md`:

```
file                     words  signpost anaphora antithesis parallel hedge closing-m% become opener one-liner
BASELINE base45 (4+5)    11259    1.33     0.71     0.27      0.71    3.11    52      2.22   0.44    2.40
06-pattern-language       7335    0.55     0.95     0.55      0.00    4.77    53      1.64   0.55    0.68
07-recursive-self-impr.   4936    0.61     0.61     1.42      0.41    4.25    48      2.03   0.61    1.01
11-the-store...           4633    1.30     2.37     0.86      1.73    5.40    43      3.67   1.30    1.94
```

What the numbers say. Chapters 6 and 7 are now at or below the baseline for signposts and closing morals. They sit far below it for one-liners (0.68 and 1.01 against 2.40), which fits the "cooled" warning in system3.md. A further full de-LLM pass on either chapter would mostly be cutting voice. Their only real excess is antithesis (Ch7 1.42 against 0.27, about 5x) and negation (the "hedge" column). Chapter 11 is the one that leans hard: 3.3x on anaphora, 2.4x on parallel pairs, 3x on openers, and 1.7x on "become". By hand, about half of Ch11's 11 anaphora hits are real runs ("We cannot tell… / We cannot replay… / We cannot compare…"). The rest are purposeful "If…" enumerations.

## Findings, in priority order

### 1. bug: apply_pass.py writes the chapter, then crashes before writing the change list
Evidence: an edit with an empty reason, `("So keep the losing branches in the tree. ", "", "", None)`, gives
`IndexError: string index out of range` at `e['why'][0]` (apply_pass.py:52). By then the chapter has already been rewritten (line 44) and `log.json` saved, but `CHANGES.md` does not exist. The author is left with an edited chapter and no record he can restore from.
Fix: validate before touching anything, and write the chapter last.
```python
for e in EDITS:
    if len(e) != 4 or not e[0] or not e[2].strip():
        sys.exit(f"bad edit (needs old text and a reason): {e!r}")
...
# build `out` first, write a.changes and a.log, then write a.path
```
and use `why = e["why"].strip(); why[:1].upper() + why[1:]`.

### 2. bug: partial failures exit 0, and skipped edits leave no record
Evidence: the test run with 2 FAILs out of 6 printed `4 applied, 2 failed` and returned `rc=0`. `CHANGES.md` said "2 skipped" without saying which. `sys.exit(1 if fails and not log else 0)` (line 57) fails only when every edit missed.
Fix: `sys.exit(1 if fails else 0)` (anyone who wants the "survives later versions" behaviour can read the FAIL lines). Also append a section to the change list:
```python
if skipped: out += ["## Skipped (text not found exactly once)", ""] + [f"- ({n} matches) {o[:120]}" for o, n in skipped]
```

### 3. wrong: straight quotes never match the manuscript
Evidence: the house style sheet (`resources/editorial/copyedit-plan-2026-09-30.md`, Quotation marks) requires curly quotes in prose. In the test, `"agent's proposal already exists"` gave `FAIL (0 matches)` because the chapter has `agent’s`. The protected list in references/system3.md:45 has the same problem: "Cheap software removed the vendor's veto" is written with `'`, so a grep for it fails, while the curly form is in `12-after-capacity.md`. The catalogue's examples are typed with straight quotes too, so a model will copy them that way.
Fix (apply_pass.py, in the miss branch):
```python
if n == 0:
    alt = old.replace("'", "’").replace('"', "“")  # crude hint only
    if s.count(old.replace("'", "’")): print("   hint: the chapter uses curly ’ — retype the old text")
```
Add to system3.md under "House rules": "Prose uses curly quotes and apostrophes (’ “ ”). Type them in `old` strings or the edit misses." Change the protected-list entry to `vendor’s`.

### 4. stale: the protected lines and "kept" examples no longer match the chapters
Checked with `grep -rF` and `git log -S` across `chapters/`:

| Line (system3.md:45 / catalogue) | Now | History |
|---|---|---|
| "The model stays hollow" | missing | cut in `cfade23` (author, 30 Sep, "Refine Chapters 2–6, preserve author voice") |
| "we have successfully parallelized…" | present as "We have…" (Ch6:307) | sentence-initial now; a case-sensitive grep misses it |
| "Cheap software removed the vendor's veto…" | present with curly ’ (Ch12) | see finding 3 |
| "Otherwise I am decorative governance" (catalogue §4 "good closers that survived") | missing | cut by Claude in `d12f553` "De-LLM pass on Chapters 8 and 9", 2 Oct |
| "More what?" (same list) | missing | cut by Claude in `0214b7a`, 2 Oct |
| "Direct contact does not scale", "Otherwise the scaffold becomes a cage" (catalogue §13) | missing | cut by the author (`cfade23`, `8bcaac3`) |
| Ch5 "It remembered. It was…" eight-item run (catalogue §6) | missing | no match in history |
| Ch12 verb-pass examples: "Built Around Difficulty", "the workaround became the process" (catalogue §8) | never in this repo | `git log --all -S` finds nothing; Ch12 has 23 "become" today |
| the other protected lines, the cat-obsession paragraph (Ch1:86), all motifs | present | — |

Two of the "survived" closers were removed by Claude's own de-LLM passes after the catalogue says they survived. That is the failure this skill warns about, and nothing in the skill could catch it.
Fix: in system3.md, replace the protected-lines paragraph with the current list, using the exact strings and curly quotes. Drop "The model stays hollow", since the author cut it. Mark "decorative governance" and "More what?" as "cut by Claude on 2 Oct — ask the author whether to restore". Add the line "Before any pass, run `scripts/protected.py` (below); a missing protected line is a stop." In the catalogue, label §6's Ch5 run and §8's Ch12 examples "(from a draft no longer in the repo)".

### 5. gap: the skill never reads the revert list, so it can re-cut what the author restored
Evidence: `resources/evaluations/2026-10-02-cuts-revert-list.md` lists every useful cut by ID (R1-2, the cat-obsession line, and others). The git log shows at least eight "Restore …" commits since 2 Oct (`0e1ff77`, `d53ecd3`, `c0a1190`, `ab25e97`, `1d48f9b`…). "A prediction does not become an experimental observation…", which catalogue §5 marks as "kept", was cut in `3accb6b` and restored in `0e1ff77` fifteen minutes later. dev-edit Phase 0 already tells the reader to read "any revert list — it records what the author took back"; de-llm does not.
Fix, in SKILL.md step 1 after the first sentence: "For System 3, read `resources/editorial/easter-egg-register.md` and the latest revert and approval lists in `resources/evaluations/` before choosing cuts. A line that was cut and restored is protected; do not propose it again."

### 6. gap: step 1's "ASSISTANT EDIT markers" no longer exist; Claude's additions are now unmarked
Evidence: `grep -rn 'ASSISTANT EDIT\|ASSISTANT DRAFT\|CLAUDE DRAFT' chapters` gives 0 hits. The chapters now carry `<!-- AUTHOR: … -->` questions instead. Sixty commits touching `chapters/` are authored by "Claude".
Fix (SKILL.md step 1): "Claude's own earlier additions are the first suspects. If there are no `ASSISTANT EDIT` markers, find them with `git log --author=Claude -p -- <chapter>` or `git blame <chapter> | grep Claude`."

### 7. wrong: the footnote gate checks nothing, and the reference note describes the build wrongly
Evidence: the gate in system3.md:74–80 reports `footnotes True 0 0` on every chapter. No chapter uses `[^…]` footnotes any more (`grep -l '\[\^' chapters/*.md` finds nothing), so the gate is always green. All chapters use `[n](appendix-references.md#ref-…)`. `validate_references` (manuscript.py:20) raises an error on an uncited entry or a wrong number. It does not move anything to "Additional sources"; that is a manual edit, and numbering restarts per chapter, so a cut can force renumbering. The `python -m unittest` gate fails here with `ModuleNotFoundError: PIL` unless the `.venv-pdf` is used.
Fix: replace gate 2 with
```
cd book-design/curated && python3 -c "
from pathlib import Path; from manuscript import *
p=ordered_paths(Path('../../chapters'),Path('book-order.json'))
validate_references(p,reference_entries(Path('../../chapters/appendix-references.md').read_text())); print('references ok')"
grep -c 'ASSISTANT\|<!--' <(cd book-design/curated && python3 -c "from manuscript import prepare;print(prepare(open('../../chapters/NN-name.md').read())[0])")
```
and say: "If a cut removes the last citation of a reference, move its entry to that chapter's *Additional sources* by hand and renumber the chapter's later citations; the build fails until you do." Use `.venv-pdf/bin/python` for `pdf.py` and the unit tests, as book-design/README says.

### 8. gap: the NotebookLM check is missing from the gates
Evidence: `prompts/notebooklm/README.md`: "`--check` fails if a kept line disappears from the manuscript". The past de-LLM pass `d12f553` had to edit `prompts/notebooklm/chapter-08.md` and `sources.json`. The repo's ai-tells skill says to "regenerate `prompts/notebooklm` briefs".
Fix: add gate 1b to system3.md: "`python3 prompts/build_notebooklm.py --check`. If it fails because a cut removed a kept line, either restore the line or change `CORE` in the generator and regenerate, and say which in the report."

### 9. bug: tells.py `--baseline` accepts only one file and the promised ratio column does not exist
Evidence: the docstring (tells.py:11) promises "adds a ratio column vs. baseline", but the output has none. `tells.py 04.md --baseline 05.md 06.md` errors with `unrecognized arguments`. The repo's baseline is two chapters (ai-tells: "The baseline for this book is Chapters 4 and 5"; check-tells.py calibrates on 4–5), so every run needs a hand-made concatenation.
Fix:
```python
ap.add_argument("--baseline", nargs="+", metavar="FILE", help="author's cleanest text; several files are pooled")
...
if a.baseline:
    text = "\n\n".join(Path(b).read_text(encoding="utf-8") for b in a.baseline)
    rows.append(("BASELINE " + "+".join(Path(b).stem[:2] for b in a.baseline), *analyse(text)))
```
Then put `nargs` files before `--baseline` in the usage line, and print an `x base` line under each row (`r[c]/base[c]` when `base[c]` is nonzero). SKILL.md step 2 should then name the baseline: "for System 3, `--baseline chapters/04-system-3.md chapters/05-the-society-of-agents.md`".

### 10. wrong: "Past numbers" and the catalogue's calibration figures are stale
Evidence (tells.py today, wc where noted):
- Catalogue §13 says Ch2 runs one-liners at "13.3 per 1,000 words". It now measures 2.29, or 5.39 with a generous count (any single-line block of 20 words or fewer).
- Catalogue §2 says "The author's cleanest chapter ran at 0.00" signposts. Ch4 is now 1.00 and Ch5 1.52, and only the preface and Ch8 are at 0.00.
- Ch4: 5,839 → 5,077 in the table; now 4,621 by wc.
- Ch6: "7,645 → 7,549"; now 7,948 by wc, after restorations.
- "91 of 103 paragraphs" (Ch6) is now 53%.
- None of the past numbers say which counter produced them. apply_pass counts every word outside comments, tells.py counts only paragraph words (Ch6: 7,948 vs 7,335).

Fix: retitle the section "Past passes (history, not current state)". Add one sentence: "Words in this table are apply_pass counts; tells.py counts paragraph words only and runs about 8% lower. Re-measure before quoting any figure." Replace the 13.3 claim in §13 with "(re-measure; Ch4–5 currently run 2.4 one-liners per 1,000 words by tells.py)".

### 11. wrong: one-liners are protected in the skill but penalized by the house prompt
Evidence: SKILL.md:40 and catalogue §13 protect one-line paragraphs "at the author's baseline density". `prompts/chapter-version-evaluation.md`:30 says "Short punchy lines should be rare and earned", and :41 says to penalize "excessive one-line paragraphs". system3.md:67 itself says the house prompt outranks the skill.
Fix (SKILL.md:40): "One-line paragraphs at or below the baseline's density (Ch4–5) are his voice; above it, they are the tell the house prompt penalizes. Offer the most verdict-like ones as optional cuts instead of cutting them."

### 12. gap: the description overlaps the repo's own ai-tells skill
Evidence: ai-tells (in `.claude/skills/`) triggers on "LLM writing", "AI tells", "humanize". de-llm triggers on "feels like LLM writing". Both will fire on the same request, and they disagree on the measuring tool and on whether to edit (ai-tells: "edits only when asked"). The repo's development-edit and author-voice already name de-llm as "the authority" for line-level cleanup, and ai-tells is the report-only reviewer.
Proposed description:
> Cut the connective tissue that makes human prose read as LLM writing (recaps, signposts, paragraph-closing morals, re-explaining, reflexive hedges, X/Y antitheses, anaphoric runs, verb monocultures) in focused, revertible editing passes that keep the author's voice, stories and jokes. Use when the user asks for a "de-LLM pass", "delete-and-fold", an "X/Y pass", to "remove the X-not-Y pattern", or to cut hedging, re-explaining, signposting or "when X becomes Y" from a System 3 chapter, Coffee & Commute post or blog draft, including after Claude's own edits. For a report-only review of AI tells with no edits, use ai-tells; for structure, development-edit; for Arabic, levantine-translate.

Near misses it then stays quiet on: "score this chapter" (dev-edit), "does this sound like me" (author-voice), "fact-check the hedges" (fresh-claims).

### 13. gap: the easter-egg register is only checked after the pass, not read before it
Evidence: register rule 1, "Read this register before editing any file named in it", and the register's own note that every seed looks like a digression to an editor who doesn't know the payoff. The skill only runs `check-eggs.sh` afterwards, and that script only fails on the 3 confirmed seeds. The 30-odd proposed seeds only warn, so a cut through one passes the gate.
Fix: covered by finding 5's text. Also add to "What to protect": "Seeds in the easter-egg register, confirmed or proposed. A *warn* from check-eggs.sh after a pass means you cut a proposed seed: restore it or ask."

### 14. gap: the protected list misses what dev-edit protects
Evidence: dev-edit Phase 5 protects "Chapter 13, the scaffolds page, confirmed seeds, the author-restored lines". de-llm lists only Ch13. The copyedit plan's table (row "13, divider, scaffolds | Typography only") also covers the divider and `14-scaffolds.md`.
Fix (system3.md:45): "…all of Chapter 13, the divider (`alternative-ending.md`) and `14-scaffolds.md` (typography only)…"

### 15. wrong: "the bold *Therefore*" is Ch6-only
Evidence: `grep -c '^\*\*Therefore'` matches only `06-pattern-language.md` (2). The style sheet allows bold "only for a coined term… and for Chapter 6's pattern *Therefore* lines".
Fix (SKILL.md:23): "(in System 3's Chapter 6, the bold *Therefore*; elsewhere, the section's last paragraph)".

### 16. polish: tells.py false positives that inflate the counts
Checked by hand on the Ch4, Ch7 and Ch11 lists:
- **signpost**: `so,? ` counts every sentence that starts with "So". Of 7 hits in Ch4+Ch7, 2 are signposts. The rest are narrative ("So I call Alberto, who lives in Rome."), an intensifier inside a quotation ("So beautiful.” Move 37…") and genuine conclusions ("So keep the losing branches in the tree."). In the apply_pass test that last line was cut as a "signpost", and it is the author's conclusion. Fix: drop `so,? |` and add `so (?:here|the point|that is)\b|`.
- **anaphora** counts runs on "The" ("The agent… / The farmer… / The kick…"). Fix: `STOP = {"the","a","an","and","but"}` and skip when `firsts[i] in STOP`.
- **one-liner** counts italic subtitles ("*A Prototype Store*", "*The Love Prompt of Devesh*"). Fix: skip `re.fullmatch(r"\*[^*]+\*", p)`.
- **hedge** is a negation counter. "The customer is not the funnel." and "Reality is not that generous." are claims, not disclaimers. Rename the column `negation` and say so in SKILL.md:57. Optionally add a narrow `disclaimer` pattern for the catalogue's real cases: `r"\b(?:can still be wrong|does not (?:establish|guarantee|prove|entitle)|may be (?:helpful|useful), but|take what follows|I do not know)\b"`.
- **closing-moral** counts questions ("Which version of the composer produced the decision?") and the protected closers ("We have successfully parallelized the experience of being ignored."). Fix: skip lines ending in `?`, and mark protected lines (finding 17).
- **q-heading** misses the "X Does Not Y" title shape ("Mei Does Not Need More Shoes", "Sami Does Not Need a Click") and "When X Becomes Y" titles, the two shapes the catalogue retired. Fix: add `|.*\b(?:Is|Does|Do) Not\b.*|When .* (?:Becomes|Stops Being) .*` to `Q_HEAD`.

### 17. polish: tells.py has no safety rails
- `--only hedges` (a typo) prints a header and nothing else, which looks like zero hits. Fix: `bad = only - set(COLS); if bad: ap.error(f"unknown --only: {bad}")`.
- It lists 44 "one-liners" in `13-the-prophecy.md`, which no pass may touch. Fix: print `WARNING: protected in full; report only` when a filename starts with `13-`.
- `| head` raises BrokenPipeError. Fix: `signal.signal(signal.SIGPIPE, signal.SIG_DFL)` at the top.

### 18. polish: apply_pass.py details
- `--log` and `--changes` default to the current directory. Run from the repo root, they drop `pass_log.json` and `CHANGES.md` into the repo, where a commit can pick them up. Fix: make both required, or default them next to the target as `<chapter>.pass.json`.
- Edits apply in sequence against the text as it changes. A later edit can match wording an earlier edit introduced; in the test, "Say the research agent" → "If…" was struck as if it were the author's text, and two flags were stacked on one paragraph. Fix: refuse an edit whose `old` overlaps an earlier `new` (`if any(old in e["new"] for e in log): FAIL "edits Claude's own text"`), or document "order matters".
- The inline flag records only a note. dev-edit Phase 5 asks for the old wording too. Fix: `f"<!-- ASSISTANT EDIT ({a.name}): {flag} Was: {old[:200]!r} -->"`, after escaping any `--` in `old`.
- Change-list numbers restart at 1 on every run. The revert list uses chapter IDs (R7-3), so give these IDs too: `f"**{chap}-{i}. …"`, with `chap` taken from the filename prefix.
- The fixed 10–15% target (SKILL.md:8, system3.md:101) pushes toward over-cutting chapters that have already had passes; Ch6 and Ch7 already measure below baseline. Fix: "A first full pass on an untouched chapter leaves it 10–15% shorter. On a chapter that has had a pass, measure first; if it is at or below the baseline, flag rather than cut."

## New script checks that would have caught these

1. **`scripts/protected.py`**. Read the protected list from a plain file (`references/protected.txt`, one exact string per line, curly quotes), grep `chapters/`, and fail on any line that is missing. Also run `git log -S` on each missing line to report who removed it. Run it before a pass, and after it as a gate. This would have caught findings 4 and 5: "decorative governance", "More what?" and "The model stays hollow".
2. **A revert-list guard in apply_pass.py**. Load quoted strings from `resources/evaluations/*revert-list*.md` and refuse any edit whose `old` contains one, with "restored by the author; ask first". This would have caught the cut-and-restore of "A prediction does not become…".
3. **A self-test for apply_pass.py**: `python3 apply_pass.py --selftest` runs a canned edit set on a temp copy (one exact match, one 0-match, one 2-match, one empty reason, one curly-quote miss) and checks the exit code and the change-list sections. This would have caught findings 1, 2 and 3.
4. **A staleness check for references**. A small script that greps every quoted example in catalogue.md and system3.md marked "kept" or "protected" and prints the ones no longer in `chapters/`. Run it whenever the skill is updated. This would have caught findings 4 and 10.
5. **A vacuous-gate guard**. The footnote snippet should print the counts and fail when both are 0 while the chapter has `appendix-references.md#` links. This would have caught finding 7.

# Audit: levantine-translate

Skill folder: `orig/levantine-translate` (SKILL.md 56 lines, voice.md 57, review.md 32, glossary.tsv 18, ar_register.py 95).
Repo checked at `155c3a1`. Read-only: nothing in the repo or the skill was changed. Test inputs and a patched copy of the script are in `scratchpad/author-skills/lev-test/`.

## What I ran

- `ar_register.py` under python3.11 and python3.12, in every mode (`table`, `--list lev`, `--list msa`, `--glossary`). Both versions behave identically.
- On all of `chapters/*.md`: every file reports `words 1`, all rates 0. The book is English, so this is expected, but the script says nothing (see finding 4).
- On five Arabic samples I wrote: Jordanian (`jo.md`), MSA (`msa.md`, `msa2.md`), "Levantine-light" (MSA bodies, colloquial openers, `light.md`), Syrian/Lebanese (`leb.md`), and a clitic test (`clitic.md`). Also on every «…» quotation in the skill (`hani_snips.md`).

| sample | lev/1k | msa/1k | lev share | opening |
|---|---|---|---|---|
| jo.md (Jordanian) | 231.9 | 29.0 | 89% | 56% |
| msa.md (MSA) | 0.0 | 246.6 | 0% | 0% |
| light.md (Levantine-light) | 70.2 | 263.2 | 21% | 100% |
| leb.md (Syrian/Lebanese) | 283.0 | 0.0 | **100%** | 53% |
| msa2.md (pure MSA, 3 sentences) | 173.9 | 130.4 | **57%** | 50% |

In broad strokes the markers work: Levantine against MSA separates cleanly, and the Levantine-light pattern shows up as intended (low share, 100% opening). Three problems: plain MSA can score as Levantine, a Lebanese text beats a Jordanian one, and short clitic forms are missed.

---

## Findings, in priority order

### 1. bug: «هوّ» in the Levantine list matches the ordinary MSA pronoun «هو»; «يعني», «طيب» and «راح» also fire on MSA

Evidence: `ar_register.py:17` lists `هوّ`. `norm()` (`:32-34`) strips the shadda, so every «هو» counts as Levantine. A three-sentence pure MSA passage:

```
$ ar_register.py msa2.md --list lev
msa2.md   23  173.9  130.4  57%  50%  هو يعني راح | هذا أن كان
   [هو] المقيِّم هو أداة القياس، وهذا يعني أن النتيجة تعتمد عليه.
   [يعني] ... وهذا يعني أن ...
   [هو] والسؤال هو: من يقيّم المقيِّم؟
   [راح] ... وقد راح يبحث عن الجواب.
```

The skill's own MSA line «لم يكن مكيال تشين هو المكيال الذي اختاره الكون» also counts «هو» as Levantine. «وهذا يعني» is among the most common MSA connectives, «طيّب» is an MSA adjective, and «راح يبحث» is literary MSA.

Fix (`:16-18`): drop `هوّ`, `يعني` and `طيب` from `LEV`. Keep `رح` and drop `راح`, or count `راح` only when an imperfect verb follows it (`راح ي…/ت…/ن…`). With the patched copy, `msa3.md` falls from 57% to 5% Levantine. The remaining 5% is «راح».

### 2. bug: «إنه» (and «كان») in the MSA list penalise real Jordanian

Evidence: `:21` lists `إنه إنها … كان`. In Levantine, «إنه» is the ordinary complementiser. The skill's own approved Levantine line `voice.md:45` «لتجربة إنه حدا يطنّشك» gets listed as an MSA slip, and `jo.md` loses 11 points of share to two «إنه». «كان» is just as common in dialect («كان في ناس»).

Fix: `إنّ أنّ يجب ينبغي سيكون` in place of `إنّ إنه إنها أنّ يجب ينبغي سيكون كان`. With the patched copy, `jo.md` scores 100% with 0 MSA hits.

### 3. gap: neither voice.md nor the script can tell Jordanian from generic Levantine, and both reward Syrian/Lebanese forms

Evidence:
- The Lebanese/Syrian sample (`هلّق`, `عم اشتغل`, `إنو`, `منعرف`, `هيدا`, `منشان`, `مو هيك`) scores **100%**, above the Jordanian sample's 89%.
- `ar_register.py:16-18` counts `هيدا هيدي` (Lebanese), `هلق هلّق` and `منشان` (Syrian), and `مو` (Syrian/Iraqi) as wins.
- `voice.md:12` gives as "Jordanian/Levantine" markers `منشان`, `عم` and `هلأ`. Progressive «عم» and «منشان» are Syrian/Lebanese. A Jordanian writes «بحكي / قاعد بحكي» and «عشان».
- `voice.md:14` corrects «بقدرنا» → «منقدر». The m- prefix for first-person plural is Syrian/Lebanese, and Jordanian says «بنقدر». The same line corrects to «بنكتشف», with the b- prefix, so the two corrections disagree with each other. `review.md:20` repeats «منقدر».

There is no list of forms to avoid, no Jordanian-specific vocabulary, and no spelling conventions. A model given voice.md will write pan-Levantine with a Damascene or Beiruti lean, because that is what its training data holds most of.

Fix: add this section to voice.md after "Markers to carry":

```
## Jordanian, not just Levantine

Ammani urban speech is the target. Prefer: بنقدر/بنعرف (b-prefix, not منقدر), بحكي or قاعد بحكي for the progressive (not عم بحكي), هسّا/هسّع, إشي, عشان (not منشان), هاد/هاي, شو, ليش، قدّيش، منيح، مزبوط، زلمة، ولك، تبعي/تبعه، خلص.
Flag as Syrian/Lebanese: عم + verb, منشان، هلّق، هيدا/هيدي، مو، إنو، كتير in the Lebanese sense of "very" before adjectives is fine.
Spelling: إنه (not انو)، اللي، مش، هاد not هادا in running text; English terms take الـ attached (الـevaluator، الـprompts); keep ق written as ق whatever the pronunciation.
```

Hani should confirm «منقدر» against his own drafts before this goes in. If «منقدر» is his own form, keep it and say so.

In the script, add `NONJO = "هيدا هيدي هلق هلّق مو منشان عم منقدر منعرف منشوف إنو".split()`, report a `non-JO/1k` column, and add `--list nonjo`. Add `هسع هسّع قديش أديش منيح مزبوط` to `LEV`. This is prototyped in `lev-test/patched.py`, and `--list nonjo` on the Lebanese sample lists every هلّق/عم/إنو.

### 4. gap: the baseline the skill depends on does not exist anywhere the model can reach

Evidence: SKILL.md:36 says to run the script "as a baseline, on a piece of Hani's own Arabic (a blog chapter)", and review.md:8 scores voice against a "blog baseline". I searched every file in `/home/user/System3` for Arabic script (U+0600–06FF) and found **zero**, in `resources/` and everywhere else. `git log --all -S'هيك'` over all 133 commits finds nothing, so no Arabic file has ever been in the repo. The blog (`hani-alshater.com`, linked in `resources/art-direction/missing-figures.md:40`) is blocked by this environment's proxy (403). The only Hani Arabic available is about 40 short quotations inside the skill (133 words), which is too little for a rate.

On an English file the script prints `words 1` and 0% everywhere without a warning (`:61` `words = max(words, 1)`), so a model that baselines against a chapter gets a silent zero.

Fix:
- Add `references/baseline.md`: 1,000–2,000 words of one blog part in Hani's Arabic, plus one paragraph of his MSA (Al Jazeera). Record its numbers at the top of voice.md: "Hani's blog baseline: lev/1k ≈ …, share ≈ …, opening ≈ …".
- Change SKILL.md:36 to: "Run `scripts/ar_register.py` on the draft and on `references/baseline.md` (Hani's own blog Arabic). If you have a newer blog part from Hani, use that instead."
- In the script, after `analyse()`: `if r["words"] < 50: print(f"{f}: only {r['words']} Arabic words; nothing to measure"); continue`.

### 5. bug: short clitic forms are never counted (وبس، ومش، وشو، ولم، ولن، ورح، فبس)

Evidence: `strip_clitics` (`:38`) requires `len(w) > 3`, so a two-letter marker with و/ف attached is skipped. `clitic.md` («وبس. ومش هيك. وشو بدك. ولم يأتِ. ولن يأتي. وقد قال. ورح نشوف. فبس.») counts only هيك and بدك. These are some of the most frequent forms in Levantine prose.

Fix: `len(w) > 2`. With the patched copy, all of them are counted.

### 6. bug: `--list` context often doesn't contain the marker

Evidence: `:58,60` keep `s.strip()[:120]`, the first 120 characters of the sentence. In a long Arabic sentence the marker can fall after that point. In `long.md`, `[سوف]` and the second `[هذا]` are printed with context that contains neither word, and both `هذا` hits print the same line.

Fix: show a window around the token.

```python
def ctx(toks, i, n=6):
    return " ".join(toks[max(0, i - n):i] + ["[" + toks[i] + "]"] + toks[i + 1:i + n + 1])
...
hits["lev"].append((w, ctx(toks, i)))   # same for msa
```

### 7. gap: `--glossary` checks only 3 of 17 rows, misses forms with diacritics, and fails at the documented path

Evidence:
- glossary.tsv parses cleanly: 18 lines, all with 3 tab-separated fields, and the header is skipped. But only rows 7, 8 and 11 have variants. The other 14 rows are skipped silently (`:86-87`), so "check the glossary for drift" (SKILL.md:37) cannot catch a new rendering such as «نافذة الاستيعاب» for context window.
- `body.count(v)` runs on raw text, so «العالمُ الثالثُ» is missed: one of two hits in `long.md`.
- SKILL.md:37 gives `--glossary references/glossary.tsv`, which is relative to the skill folder. From the repo root it fails with `FileNotFoundError: 'references/glossary.tsv'`.

Fix:
- Normalise both sides: `body = norm(strip_md(...))` and `body.count(norm(v))` (prototyped).
- Also report each row's house rendering count and any Latin glossary term left in the Arabic outside backticks, so drift shows even when no variant is listed.
- In SKILL.md, write paths as `<skill>/scripts/ar_register.py` and `<skill>/references/glossary.tsv`, with one line saying `<skill>` is this skill's folder.

### 8. wrong: the glossary contradicts the "keep technical terms in English" rule and has no register column

Evidence: SKILL.md:24 says to keep technical terms in English "the way his blog does". glossary.tsv:2,4,6 give Arabic for harness, context window and container (منظومة العمل، نافذة السياق، الحاوية). Only the evaluator row (`:3`) separates book MSA from blog. Row 9 `Therefore: → عشان هيك:` is Levantine, so in a literary-MSA book edition (SKILL.md:15, Ch 5 was MSA) it would be a register break.

Fix: make the TSV four columns, `english / book MSA / blog Levantine / variants to flag`, and fill both registers, e.g. `Therefore:	لذلك:	عشان هيك:	` and `harness	منظومة العمل (first-use gloss)	harness	`. Have the script take `--register book|blog`. Move first-use glosses into a fifth `note` column so the rendering cell holds only the rendering.

### 9. wrong: two reference examples break the skill's own rules or read as calques

- `voice.md:34` «كانت المؤسسة هي العلّة» for "The organization was the bug". `voice.md:39` says "Engineer jokes stay engineer jokes… His readers are engineers", and "bug" is the engineer joke here (Ch 5:28 comes straight after a compiler story). Proposed: book MSA «كانت المؤسسة نفسها هي الـbug»; blog «طلعت المؤسسة هي الـbug». If العلّة is kept on purpose for the MSA edition, say so.
- `voice.md:26` eight verbs. «نختلف باستقلال» is a calque of "disagree independently" and no Arabic writer says it. «نوحّد» used bare carries a strong religious echo (التوحيد). Proposed: «نتذكّر، نوحّد المقاييس، نتخصّص، نختلف كلٌّ من طريقه، نرصد، نتتبّع المصدر، نوزّع الانتباه، نراجع المؤسسة نفسها». Ch 5 now calls these "seven jobs and an eighth" (`05:282`), so "eight verbs" should read "seven jobs and an eighth".
- Minor: «صار للواقع commit hook خاص به» (`voice.md:39`): «خاص به» is padding. «صار للواقع commit hook» keeps the punch.
- Minor: the term «الطيّة» (`voice.md:24`) is rare in Arabic newsrooms. The gloss carries it, so it's acceptable, but «فوق الطيّة / أعلى الصفحة الأولى» would be understood without the gloss.

The other examples are natural and correct. That includes «ست عشرة نسخة» (agreement correct), «عبد الحميد صبرة», «كما يُعرف الأسد من مخلبه», «ممتاز يا حج، هات المعادلة» (the preface's "excellent, uncle. Show us the equation", `00-preface:5`) and «بس خلينا نرجع خطوة لورا».

### 10. gap: Arabic files have no home in the repo, and the obvious one breaks the build

Evidence: SKILL.md:44 says "If it goes into the book repo…" but doesn't say where. `book-design/curated/manuscript.py:42-43` raises `ValueError('Update book order: … unlisted=…')` for any `.md` in `chapters/` that isn't in the book order, and `tests/test_build.py:44` asserts the same. An Arabic chapter dropped beside the English one breaks the build.

Fix (SKILL.md Step 4): "In the book repo, Arabic goes in `translations/ar/` with the English file name (`translations/ar/05-the-society-of-agents.md`), never in `chapters/`, which the build reads in full. The first line is `<!-- ASSISTANT TRANSLATION from chapters/<file> @ <commit>, <date>; register: …; mode: … -->`." This also gives the sync note in SKILL.md:45 a fixed place to live. The marker name matches the repo's existing `ASSISTANT EDIT / ASSISTANT DRAFT` convention (`resources/editorial/copyedit-plan-2026-09-30.md:13`).

### 11. gap: the register decision has nowhere to be recorded

Evidence: SKILL.md:15 says "If it isn't settled, ask once and record the answer" without saying where. Nothing in the repo records it, and the skill itself notes that Ch 5 (MSA) and Ch 6 (Levantine) already disagree.

Fix: "Record it at the top of `translations/ar/README.md` (register, date, Hani's words) and read that file before Step 1."

### 12. gap: the repo's seed and Ch 13 rules aren't carried into translation

Evidence: `easter-egg-register.md` rule 5 says "Chapter 13 is protected in full… only the author changes it." Rule 2 says "Do not explain a payoff." Seeds work through repeated words across chapters: camel in Ch 4, 11 and 12; coffee and «Decaf.»; octopus; cable; fax machine. SKILL.md:16 "edit while translating" allows fixing "duplications", and a deliberate repeat looks exactly like a duplication to a translator. Localising one occurrence differently breaks the seed.

Fix: add to SKILL.md Step 1.2: "Edit mode never applies to Chapter 13, which is translated faithfully, and never to anything listed in `resources/editorial/easter-egg-register.md`. A seed must use the same Arabic word in every chapter it appears in (camel → جمل, coffee → قهوة, octopus → أخطبوط, cable → كابل, fax → فاكس), and a payoff is never glossed." Add those rows to glossary.tsv.

### 13. polish: the rejected rendering differs between SKILL.md and voice.md

SKILL.md:26 gives the bad version as «يهمّ ما يعرفه كلّ واحد», while voice.md:37 has «يهمّ من يعرف ماذا». Pick the one from the real case, voice.md's, and use it in both places.

### 14. polish: "rewrite whole sections" vs "sentence-level fixes over rewrites"

SKILL.md:38 says to rewrite whole sections when it "still seems translated". review.md:28 and the repo's evaluation prompt ("Prefer surgery over replacement", `prompts/chapter-version-evaluation.md`) say the opposite. They apply to different things, but a model may carry one over to the other. Add "(this applies to a translation; Hani's own Arabic drafts get sentence-level fixes, see review.md)" to SKILL.md:38.

### 15. stale: source lines the examples are built on are gone from the current English

`grep` over `chapters/` finds none of: "Knowledge becomes structure", "organization of trust" / "Rigor at scale", "Who knows what matters", "eight verbs", "pipes", or a Chen in Ch 5 («مكيال تشين»). These still work as teaching examples, but the glossary rows built on them (`glossary.tsv:12`) and the Ch 5 case labels describe text that no longer exists. Fix: add "(from the Ch 5 draft of <date>; the line has since changed)" to each, and delete row 12.

### 16. polish: description triggers on any "translate"

"Use whenever the user asks to translate" would also fire on "translate this German citation" (Ebbinghaus, `appendix-references.md:431`) or "translate this into plain English". It also misses "عامية", "ammiya", "Levantine" and the reverse-direction use in voice.md:55-57.

Proposed final sentence: "Use whenever the user asks to translate into or out of Arabic, says «بالعربي», «ترجم», «عامية», "ammiya" or "Arabic version", asks for an Arabic chapter or blog post to be evaluated or two Arabic translations compared, or wants an ammiya sketch of an English chapter, even if they don't name the register. Not for other languages."

### 17. polish: script clean-ups

- `:19` filters `هناك؟` out of a list it was only added to. Delete both.
- `:51-52` count Latin words into `latin`, which is never printed. Print the top 10 as "code-switched terms" or remove it.
- Piping to `head` throws `BrokenPipeError`. Add `signal.signal(signal.SIGPIPE, signal.SIG_DFL)` at the top of `main()`.
- Cross-skill naming: SKILL.md:32 says "de-llm rules", but in the repo's installed skill set (`.claude/skills/`) that skill is `ai-tells`, and levantine-translate itself is not installed there. If it ships with the repo, say "ai-tells (de-llm)".

## New script checks that would have caught these

1. A self-test (`ar_register.py --selftest`) with three built-in fixtures (Jordanian, MSA, Lebanese) that fails unless MSA share < 15%, Jordanian share > 85% and Lebanese non-JO/1k > Jordanian non-JO/1k. This would have caught findings 1, 2, 3 and 5.
2. A guard that refuses to report on fewer than 50 Arabic words (finding 4).
3. A glossary lint: every row has 4–5 fields, every Arabic cell is non-empty for its register, and no rendering appears as another row's variant (findings 7 and 8).
4. A stale-source check: for each glossary/voice case tagged with an English source line, grep `chapters/` and warn when the line is gone (finding 15).

---
name: levantine-translate
description: Translate or adapt Hani's English writing (System 3 chapters, The Dream, blog posts, op-eds) into Arabic in his own voice, and review Arabic drafts for voice, register, idiom, terminology and fidelity. Covers Jordanian/Levantine for the blog series "لما صار التفكير كهرباء" and the book editions, literary MSA with colloquial touches for outlets like Al Jazeera, glossary consistency, aphorisms and jokes that don't survive literal translation, and keeping Arabic versions in sync with later English passes. Use whenever the user asks to translate into or out of Arabic, says «بالعربي», «ترجم», «عامية», "ammiya", "Levantine" or "Arabic version", asks for an Arabic chapter, blog post or op-ed to be evaluated or two Arabic translations compared, or wants an ammiya sketch of an English chapter, even if they don't name the register. Not for other languages (a German citation, "translate into plain English"). For English prose in his voice use author-voice; for AI-tell sweeps of English chapters use ai-tells.
---

# Levantine translate

The target is not "good Arabic". It is Hani writing in Arabic. His Arabic is a different and often stronger writer than his English: street-level, funny without announcing it, able to drop from Žižek to خالك in one sentence and stay there. A translation that reads like an educated MSA narrator has failed even if every sentence is correct.

Paths below are relative to this skill's folder (`<skill>`); from the repo root write them as `<skill>/scripts/…`.

## Step 0 — What you know about his Arabic, and what you don't

Hani is from Jordan and lives in Germany. That is all this skill assumes. Which Jordanian he writes (city, how much he lets Syrian/Lebanese forms such as «عم» or «منقدر» in) comes from him, not from a guess.

There is no sample of his own Arabic in the repo (checked 2026-10-03: no file under `/home/user/System3` contains Arabic script; re-check with `grep -rlP '[\x{0600}-\x{06FF}]' /home/user/System3 --include='*.md'`). The blog was not reachable from the sandbox. So:

1. If `references/author-arabic-sample.md` has text in it, use it as the baseline (Step 3).
2. If it is empty, ask once for a link or a pasted blog part. Don't wait for it: carry on with `references/voice.md`, the glossary and the register rules, and say in the note «no baseline of your Arabic was used».

## Step 1 — Fix the three settings before writing a word

1. **Register.** Choose one and hold it for the whole work:
   - **Levantine (Jordanian)** — the blog series and the default for Hani's own channels. Chapter 6 of System 3 was done this way to match the blog.
   - **Literary MSA with light colloquial touches** — outlets with editorial standards (the Al Jazeera piece). See "Op-ed MSA" below.
   - **Book edition** — still Hani's decision for System 3 (the Chapter 5 translation was literary MSA; Chapter 6 was Levantine). If it isn't settled, ask once and record the answer with its date where he keeps Arabic work (see Step 4). Never let chapters drift between registers.
2. **Fidelity mode.** *Faithful* (carry the source, flaws included) or *edit while translating* (fix duplications, overclaims and restorations on the way). In edit mode, log every change in a `ملاحظة تحرير` under its chapter so Hani can see what isn't a translation. Edit mode never applies to Chapter 13, the alternative-ending divider or `14-scaffolds`: those are translated faithfully. A repeated word may be a seed, not a duplication: check `resources/editorial/easter-egg-register.md` before cutting any repeat.
3. **Apparatus.** Book: footnotes kept, bilingual where useful (Arabic gloss, Latin citation). Blog: footnotes and editorial comments can go. Code, YAML and identifiers stay in English.

## Step 2 — Translate

Read `references/voice.md` first; it holds the markers, the Jordanian-versus-Syrian/Lebanese forms, the house renderings and real before/after cases. The rules that matter most:

- **Put the dialect in the connective tissue**, not only at the starts of sentences. "Levantine-light" (colloquial openers, MSA bodies) reads like an educated narrator, not like him. Check with `scripts/ar_register.py`: a low Levantine rate with a high opening share is that pattern.
- **Jordanian, not generic Levantine.** Models drift to Damascus or Beirut because that is most of their training data: «عم بحكي»، «منقدر»، «هلّق»، «هيدا»، «منشان». Prefer the forms in voice.md, and treat the script's variety column as a smoke alarm, not a verdict.
- **Technical terms:** on the blog keep them in English the way he does (`prompt`, `evaluator`, `dashboard`), in code font where the source uses it. In the book and in op-eds use the book column of `references/glossary.tsv`. Gloss a core concept once on first use, then one rendering everywhere.
- **Translate aphorisms as aphorisms.** Keep the length and the turn: "Remembering is not knowing" → «التذكّر ليس معرفة», not an explanation of it. A three-word thesis stays three words.
- **Keep the stress where the argument puts it.** "Who knows what matters" is about *who*: «المهم من يعرف», not «يهمّ من يعرف ماذا».
- **Jokes built on an English frame need an Arabic one.** "Sixteen Claudes walk into a kernel" has no bar-joke frame in Arabic; «ست عشرة نسخة من كلود، ونواة لينكس واحدة» makes a different joke that fits the image.
- **Never explain a joke, a reference or a seed** — not in the text, not in a footnote, not in the note. The loose cable, the coffee, the camel, the octopus and the rest of `easter-egg-register.md` stay as bare as in the English, and each one uses the same Arabic word in every chapter (glossary rows marked *seed*). Hani knows his seeds; naming what they point to (an experiment, a film) in the note only invites someone to paste it into the text.
- **Don't add jokes Hani didn't write.** An embellishment in his spirit is still the translator's voice. Flag any you keep for his decision.
- **Don't punch at the reader.** His sarcasm aims at dashboards, academics, the establishment and خالك, never at the person he just invited in («لا يا حبيبي» was cut for that reason).
- **Watch the false friends.** «العالم الثالث» means the Third World before Popper's World 3; use «العالم 3». «تعاون» as "a collaboration" is a calque; use «فريق بحثي». Restore Arab names to their Arabic forms (عبد الحميد صبرة، ابن الهيثم).
- **Quotations:** keep a famous Latin line in Latin, then the Arabic (*Tanquam ex ungue leonem*: كما يُعرف الأسد من مخلبه).
- **The ai-tells rules apply in Arabic too:** no paragraph-closing morals, no re-explaining, no bullet lists where he'd write prose. Bullet lists read as the most generated part of any Arabic draft.

**Op-ed MSA.** Majority literary MSA; the colloquial touches are a handful of deliberate winks («ممتاز يا خال، هات المعادلة»). Keep English out of the body: names may appear once in Latin in brackets after the Arabic form, links stay links, and everything else gets its book-column rendering (`--list latin` shows what's left). Write it from Arabic thinking: the Al Jazeera piece only stopped reading as translated when sections were rewritten from the meaning.

## Step 3 — Check

1. Run `python3 scripts/ar_register.py DRAFT.md` (and on `references/author-arabic-sample.md` if it has text, as the baseline). Compare rate, share, opening position and variety. In a Levantine target list the MSA markers (`--list msa`) and the Syrian/Lebanese ones (`--list nonjo`) and recast the ones that aren't deliberate. Hani's Arabic mixes some MSA («هذا الكتاب»), so aim for his baseline, not 100%. In an MSA target, `--list lev` and `--list latin`.
2. Glossary drift: `--glossary references/glossary.tsv --register blog` (or `book`).
3. The script is a heuristic. If you change its word lists, run `--selftest`. Under 50 Arabic words it refuses to report (an English file reads as zero words).
4. Read it aloud in your head as Hani would say it. Anything that sounds decoded from English gets rewritten from the meaning, not repaired word by word. When Hani says a *translation* "still seems translated", rewrite whole sections; his own Arabic drafts get sentence-level fixes instead (`references/review.md`).
5. Run the review checklist in `references/review.md`.

## Step 4 — Deliver

- **Where.** Work on copies. Never save Arabic into `chapters/`: the build reads every `.md` there and fails on any file not in the book order (`book-design/curated/manuscript.py`, `ordered_paths`). If the user names no place, use `translations/ar/<english file name>` in a working copy, or the output folder he gave you. If the repo or the skill folder is read-only, write to the output folder and say so.
- **The text file** is the deliverable and contains nothing a reader shouldn't see. In a repo copy its first line is `<!-- ASSISTANT TRANSLATION from chapters/<file> @ <commit>, <date>; register: …; mode: … -->`: the whole text is Claude's until Hani revises it.
- **The note** goes in a separate file (`<name>.note.md`), or, if he asked for one file, in a block after the text headed «ملاحظة للمؤلف — احذفها قبل النشر». About 150 words at most. It is a "To check" list of the 3–6 decisions he must make (name spellings, a headline option, an engaging-over-faithful choice, any embellishment kept), plus one line each for: register and mode; source commit; «no baseline of your Arabic was used» if true; proposed glossary rows. Don't describe your approach, don't paste script output, don't explain seeds or references.
- **Glossary.** When a new term settles, add a row to `references/glossary.tsv`. If the skill folder is read-only, put the proposed rows (english → book / blog) in the note instead and say they weren't saved.
- **Sync.** Record which English commit it was translated from (`git -C /home/user/System3 log -1 --format=%h -- chapters/<file>`). When the English gets a de-LLM, X/Y or structural pass afterwards, the Arabic still carries the cut sentences and needs the same trim.

## Reviewing Arabic (his drafts or a translator's)

Use the rubric and the proofing list in `references/review.md`. Score the voice against Hani's own Arabic (the sample file, or voice.md when it is empty, saying so), not against generic quality. When comparing two translations, separate completeness, fidelity, closeness to his voice, colloquial depth, editorial improvement, chapter-title craft and production readiness, then recommend the combination (e.g. one translation as the complete spine, the other's voice and fixes pushed into it).

## Files

- `scripts/ar_register.py` — Levantine/MSA rates, opening share, Jordanian vs Syrian/Lebanese signal, English words left in, in-context lists, glossary drift, `--selftest`.
- `references/voice.md` — markers, Jordanian forms, house devices, real cases from past translations.
- `references/glossary.tsv` — english, book (MSA), blog (Levantine), variants to flag, note; seeds marked.
- `references/review.md` — scoring rubric, proofing list for Hani's drafts, comparison template.
- `references/author-arabic-sample.md` — empty until Hani supplies his own Arabic; instructions inside.

---
name: levantine-translate
description: Translate or adapt Hani's English writing (System 3 chapters, The Dream, blog posts, op-eds) into Arabic in his own voice, and review Arabic drafts for voice, register, idiom, terminology and fidelity. Covers Jordanian/Levantine for the blog series "لما صار التفكير كهرباء" and the book editions, literary MSA with colloquial touches for outlets like Al Jazeera, glossary consistency, aphorisms and jokes that don't survive literal translation, and keeping Arabic versions in sync with later English passes. Use whenever the user asks to translate, "بالعربي", "Arabic version", "ترجم", to evaluate an Arabic chapter or blog post, or to compare two Arabic translations, even if they don't name the register.
---

# Levantine translate

The target is not "good Arabic". It is Hani writing in Arabic. His Arabic is a different and often stronger writer than his English: street-level, funny without announcing it, able to drop from Žižek to خالك in one sentence and stay there. A translation that reads like an educated MSA narrator has failed even if every sentence is correct.

## Step 1 — Fix the three settings before writing a word

1. **Register.** Choose one and hold it for the whole work:
   - **Levantine (Jordanian)** — the blog series and the default for Hani's own channels. Chapter 6 of System 3 was done this way to match the blog.
   - **Literary MSA with light colloquial touches** — outlets with editorial standards (the Al Jazeera piece).
   - **Book edition** — still Hani's decision for System 3 (the Chapter 5 translation was literary MSA; Chapter 6 was Levantine). If it isn't settled, ask once and record the answer. Never let chapters drift between registers.
2. **Fidelity mode.** *Faithful* (carry the source, flaws included) or *edit while translating* (fix duplications, overclaims and restorations on the way). In edit mode, log every change in a `ملاحظة تحرير` under its chapter so Hani can see what isn't a translation.
3. **Apparatus.** Book: footnotes kept, bilingual where useful (Arabic gloss, Latin citation). Blog: footnotes and editorial comments can go. Code, YAML and identifiers stay in English.

## Step 2 — Translate

Read `references/voice.md` first; it holds the markers, the house renderings and real before/after cases. The rules that matter most:

- **Put the dialect in the connective tissue**, not only at the starts of sentences. "Levantine-light" (colloquial openers, MSA bodies) read like an educated narrator, not like him. Check with `scripts/ar_register.py`: a low Levantine rate with a high opening share is that pattern.
- **Keep technical terms in English** the way his blog does (`prompt`, `evaluator`, `dashboard`, `serializer`), in code font where the source uses it. Gloss a core concept once on first use, then use one Arabic rendering everywhere (`references/glossary.tsv`).
- **Translate aphorisms as aphorisms.** Keep the length and the turn: "Remembering is not knowing" → «التذكّر ليس معرفة», not an explanation of it. A three-word thesis stays three words.
- **Keep the stress where the argument puts it.** "Who knows what matters" is about *who*: «المهم من يعرف», not «يهمّ ما يعرفه كلّ واحد».
- **Jokes built on an English frame need an Arabic one.** "Sixteen Claudes walk into a kernel" has no bar-joke frame in Arabic; «ست عشرة نسخة من كلود، ونواة لينكس واحدة» makes a different joke that fits the image.
- **Don't add jokes Hani didn't write.** An embellishment in his spirit is still the translator's voice. Flag any you keep for his decision.
- **Don't punch at the reader.** His sarcasm aims at dashboards, academics, the establishment and خالك, never at the person he just invited in («لا يا حبيبي» was cut for that reason).
- **Watch the false friends.** «العالم الثالث» means the Third World before Popper's World 3; use «العالم 3». «تعاون» as "a collaboration" is a calque; use «فريق بحثي». Check names against forms Hani already uses on the blog, and restore Arab names to their Arabic forms (عبد الحميد صبرة، ابن الهيثم).
- **Quotations:** keep a famous Latin line in Latin, then the Arabic (*Tanquam ex ungue leonem*: كما يُعرف الأسد من مخلبه).
- **The de-llm rules apply in Arabic too:** no paragraph-closing morals, no re-explaining, no bullet lists where he'd write prose. Bullet lists read as the most generated part of any Arabic draft.

## Step 3 — Check

1. Run `scripts/ar_register.py` on the draft and, as a baseline, on a piece of Hani's own Arabic (a blog chapter). Compare rate, share and opening position. In a Levantine target, list the MSA markers (`--list msa`) and recast the ones that aren't deliberate. Hani's own Arabic mixes some MSA («هذا الكتاب»), so aim for his baseline, not 100%.
2. Check the glossary (`--glossary references/glossary.tsv`) for drift.
3. Read it aloud in your head as Hani would say it. Anything that sounds decoded from English gets rewritten from the meaning, not repaired word by word. When Hani says it "still seems translated", rewrite whole sections from scratch.
4. Run the review checklist in `references/review.md`.

## Step 4 — Deliver

- The file, plus a short note: register used, fidelity mode, every place you chose engaging over faithful, any embellishment kept, names to check, what was dropped.
- If it goes into the book repo, add one `<!-- ASSISTANT TRANSLATION … -->` note at the top: the whole text is Claude's until Hani revises it.
- **Sync.** Record which English commit or version it was translated from. When the English gets a de-LLM, X/Y or structural pass afterwards, say that the Arabic still carries the cut sentences and needs the same trim.

## Reviewing Arabic (his drafts or a translator's)

Use the rubric and the proofing list in `references/review.md`. Score the voice against Hani's own Arabic, not against generic quality. When comparing two translations, separate completeness, fidelity, closeness to his voice, colloquial depth, editorial improvement, chapter-title craft and production readiness, then recommend the combination (e.g. one translation as the complete spine, the other's voice and fixes pushed into it).

## Files

- `scripts/ar_register.py` — Levantine/MSA marker rates, opening share, in-context lists, glossary drift.
- `references/voice.md` — markers, house devices, real cases from past translations.
- `references/glossary.tsv` — house renderings for recurring terms; add to it whenever a new term is settled.
- `references/review.md` — scoring rubric, proofing list for Hani's drafts, comparison template.

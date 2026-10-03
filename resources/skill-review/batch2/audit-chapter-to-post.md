# Audit: chapter-to-post

Skill: `batch2/chapter-to-post/chapter-to-post/` (SKILL.md, 50 lines; references/examples.md, 30 lines; no scripts).
Repo state checked: `/home/user/System3` at HEAD, Chapter 6 last touched in `1d48f9b`. The repo was left clean (`git status --short` prints nothing).
Dry run: `audit-work/chapter-to-post/dry-run-ch6-post.md`, a Coffee & Commute draft from Chapter 6 written by following the skill to the letter, with the author's answers assumed.

Steps 1 and 2 of the brief: there are no scripts to run. I ran the neighbouring checkers the skill depends on (`author-voice/scripts/voice_check.py --book chapters/` and `de-llm/scripts/tells.py --baseline chapters/04-system-3.md`) on the dry-run draft under the default `python3`. Their results are quoted where they matter below.

There is no Coffee & Commute or LinkedIn material in the repo. `grep -ril "coffee & commute\|linkedin"` over the repo finds only a Milanfar citation in `appendix-references.md:286`. Nothing in `examples.md` can be checked against the real posts, so the claims about posts are marked "unverifiable" below and not "wrong".

---

## Priority 1: will mislead a run

### 1. The `risk-audit` rules do not exist (bug)

**Evidence.** SKILL.md:41 says "No employer-identifying product detail; check with the risk-audit rules." There is no skill, reference or file called risk-audit anywhere in the repo, in `author-skills/orig/` or in `batch2/` (`grep -rn "risk-audit\|risk_audit"` returns nothing). The model therefore has to make up "the rules". Exposure is also undefined: `chapters/about-the-author.md:21` already names the employer in public ("Head of Applied Science at Zalando"). Without a definition, the model cannot tell whether book-published material is fair game.

**Fix.** Replace SKILL.md:41 with:

> - **Exposure.** Posts are public the moment they go up. Leave out anything about his employer that the published book does not already say: internal metrics, product or team names, incidents, colleagues, roadmaps. The book's own examples are fine as the book tells them. If an example sounds like it came from work and you can't find it in `chapters/`, ask before using it.

### 2. "Use the de-llm skill" points at a skill that is not installed in the repo (wrong)

**Evidence.** SKILL.md:15. The repo's `.claude/skills/` holds `ai-tells` and `author-voice`, but no `de-llm`. `author-voice/SKILL.md:141` already hedges this: "the author's own `de-llm` skill is the authority **when it is installed**." Line 15 also repeats `de-llm/references/catalogue.md` §12 ("Machine-even rhythm (short posts)") almost word for word, and line 28 does the same. That gives two copies of one rule, and they will drift apart.

**Fix.** Replace the last sentence of SKILL.md:15 and the whole of line 28 with:

> Use the de-llm skill when it is installed (its catalogue §12 covers short posts); otherwise use the sentence-level list in ai-tells. Borrowed vocabulary should be introduced differently each time, so five posts don't read as one template.

### 3. The post voice contradicts author-voice, and nothing says which one wins (gap)

**Evidence.**
- The `author-voice` description triggers on "essays, posts, talks or newsletters in his voice", so both skills will load for any post request. chapter-to-post never mentions author-voice.
- **Em-dashes.** chapter-to-post requires the header `☕️ Coffee & Commute — Title` (SKILL.md:32). author-voice:88 says "No em-dashes in prose."
- **Short lines.** chapter-to-post asks for "Short lines and white space" and "stacked rhetorical questions" (SKILL.md:32). author-voice:85-87 says that "more than one in five" short sentences "reads choppy". de-llm says "Trim question runs and tricolons to the strongest two."
- **Reused sentences.** author-voice:29 says "Never recycle his sentences." chapter-to-post:40 only says to "note when a post reuses a line", and an "excerpt" is reuse by definition.
- **Dry run.** `voice_check.py` on the draft flagged `short_sentence_share 0.38 (baseline 0.13)`, `choppy`, `em-dashes` (the prescribed header) and `4 run(s) of 8+ words copied from the manuscript`. Every flag came from doing what chapter-to-post asks.

**Fix.** Add this section after "Voice":

> **Posts and the book voice.** A post is his LinkedIn register, not the book's. From author-voice, keep: no invented experience, jokes never at the reader, American spelling, no em-dashes in the body (the header's dash is the series mark), no hype or machine vocabulary. Don't hold a post to author-voice's sentence-length numbers; short lines are the point here, so read `voice_check.py`'s "choppy" flag as noise for posts. An **excerpt** is quoted book text, marked as such and left unchanged. A **post** is new sentences: reuse a book line only as a flagged callback, and run `voice_check.py --book chapters/` to find the ones you didn't mean to keep.

### 4. No rule against inventing the author's life, and the voice notes push toward it (gap)

**Evidence.**
- SKILL.md:32 gives "a guy on a train, not a philosopher on a mountain" as voice, plus "a recurring self-description used as a frame … closed in the last line". Neither line says these must come from him.
- In the dry run, the opening came out as "reading an architecture book from 1977 on the train, … around page 700". The train and the page number were both invented; I replaced them with an `[AUTHOR: …]` marker after the fact.
- The self-description frame cannot be filled without inventing one, because the only frame on file ("zombie for the greater good") belongs to the SOLID post.
- Chapter 6's running case is itself invented (`06-pattern-language.md:5`, author note C6-1: "The Ines/Sam running case is invented and does a lived example's job"). Nothing stops a post from presenting it as a real incident.
- author-voice:121-127 and ai-tells tell #4 both have this rule. chapter-to-post doesn't.

**Fix.** Add to "How he likes to work":

> - **Never invent his life.** Where a beat needs his experience, leave `[AUTHOR: what it needs]` and write around it: where he read something, what happened at work, a number from his own projects. "A guy on a train" describes the register, not a scene to make up. A case the book labels imagined (Chapter 6's Ines and Sam) stays labelled in the post, or stays out.

### 5. A 3,000-character LinkedIn post can't hold "about 800 words" (wrong / unclear)

**Evidence.** SKILL.md:37: "About 800 words for a standalone LinkedIn post linking to the full piece." A LinkedIn feed post is capped at 3,000 characters, about 450–500 words of English. The dry-run body is 631 words and 3,980 characters (`wc -m`), so it would not fit. 800 words only works as a LinkedIn article or newsletter issue. The skill never says which surface a Coffee & Commute post is published on.

**Fix.** Replace SKILL.md:37 with:

> - **Length and surface.** Ask where it's going. A feed post is capped at 3,000 characters (about 450 words); the newsletter and LinkedIn articles have room for about 800. For a long piece that also gets a feed post, write the feed post as a hook and a link. For anything over the limit, offer the two cheapest cuts.

(The author should confirm where Coffee & Commute is published.)

### 6. "Discuss before drafting" has no fallback (gap)

**Evidence.** SKILL.md:12: "Don't hand over an unsolicited full draft." Two common cases are not covered:
- He asks for a draft outright ("turn Chapter 6 into a post"). That draft is solicited, but line 12 reads as "ask first" anyway.
- Nobody is there to answer (a batch run, a subagent).

In the dry run I had to invent the four answers myself.

**Fix.** Append to SKILL.md:12:

> If he asks for a draft outright, or can't be asked, write the four answers and the beats in six lines at the top, with the assumed ones marked, then draft. He can change a premise faster than a paragraph.

### 7. The spoiler check doesn't point at the repo's own list of payoffs (gap)

**Evidence.** SKILL.md:39 says "The reveal (*We call it science*), seeded payoffs and Chapter 13's fable stay in the book" but never says where the seeded payoffs are listed. `resources/editorial/easter-egg-register.md` is that list: Coffee→"Decaf.", the octopus, the cable, tongue and ear, DNA as a copier, the camel, the dream, 11:53 PM, the names. Its rule 2 says "Do not explain a payoff", and its rule 5 protects Chapter 13 in full. `chapters/alternative-ending.md` (the divider in front of the fable) isn't named either. The checks themselves are accurate: `reveal-we-call-it-science.md` does carry "We call it science.", and Ch13 is `13-the-prophecy.md`.

**Fix.** Replace SKILL.md:39 with:

> - **Don't spend the book's twists.** Before using a motif, read `resources/editorial/easter-egg-register.md`. Nothing in its "Pays off" column goes into a post, and no seed gets explained (proposed seeds count too). The reveal page (*We call it science*), the alternative ending and Chapter 13 stay in the book unless he chooses otherwise. A trailer shows the explosion, not the plot twist.

### 8. Fresh claims go public with no fact-check step (gap)

**Evidence.** Chapter 6 rests on August and September 2026 events: the Fermat formalization (06:65), the Riemann bound (06:253) and Navier–Stokes with a disputed priority (06:275-277). SKILL.md:41 says posts "are public immediately", but no step mentions verification. The author's `fresh-claims` skill exists for exactly this ("before any publication").

**Fix.** Add under "From a chapter or essay":

> - **Facts.** A post is a publication. Recheck any recent or single-source claim it carries with fresh-claims, even if the chapter already cites it; the chapter may be behind the news.

---

## Priority 2: stale, unverifiable or contradictory reference data

### 9. The series table is incomplete and already contradicts itself (stale / wrong)

**Evidence.**
- `examples.md:7` gives the Peacock post's "Why it persists" as "(see the post)". No post exists in the repo to see.
- `examples.md:7` gives the Peacock ending as "Practical turn", but `examples.md:11` says "**Both** earlier posts end by turning the knife on the author." These two lines can't both be read as the only description of the ending.
- SKILL.md:21 lists "metrics" as a sacred object he has used. No post in the table has metrics as its object.
- The table stops at 30 Jun 2026. It is now 3 Oct 2026, so posts written since then are probably missing.
- SKILL.md:20 says "Don't repeat a lens he has used", but this table is the only record, and it leaves out the System 3 article's Saussure lens (SKILL.md:36). The Chapter 6 dry run hit both problems:
  - Saussure is in Ch6 (06:135).
  - The natural Ch6 sacred object (design patterns as badges) sits next to SOLID.
  - The natural "why it persists" (a pattern name signals competence) is the Peacock post's lens. The skill gives no way to judge how close is too close.

**Fix.**
1. Turn the table into a post log: date, title, link, lens, sacred object, why it persists, ending, book lines reused. Add a line telling the model to append a row after each published post.
2. Ask the author to fill the Peacock "why" cell and to say whether "metrics" was a post.
3. Fix line 11: "The Peacock post adds a practical turn after the self-implication; High-functioning bullshit ends on it ('stay skeptical of narratives, including this one')". The author should confirm this wording.
4. Add to SKILL.md:20: "Check the log; a lens or a 'why it persists' answer used before is a repeat even in new words. If the sacred object is a neighbour of an earlier one, say so before drafting."

### 10. Unclear whether chapter posts use the Coffee & Commute shape (unclear)

**Evidence.** "The Coffee & Commute shape" (SKILL.md:18-28) and "From a chapter or essay" (34-42) describe two different structures. The second runs hook → insight → framing → link, and the System 3 article example in `examples.md:24-26` follows it. Neither section says which applies when a chapter becomes a Coffee & Commute post. In the dry run I forced the chapter into the seven beats, and the chapter had to supply a "sacred object" it was never written around.

**Fix.** Add at the top of "From a chapter or essay":

> Two kinds of post come out of a chapter. A **Coffee & Commute** post uses the shape above, with the chapter as the source of the lens or the break. A **promotion post** (feed post or thread) uses the hook → idea → code → link shape below. Ask which one he wants. If he doesn't say and the chapter has no sacred object to point at, it's a promotion post.

### 11. Claims about the System 3 article and the Arabic blog can't be checked (unverifiable)

**Evidence.** The tongue–ear test, Saussure, Alberto and epistemic-swe are all real in Ch4 (04:25, 04:47, 04:73, and `chapter-arc` refs 04:202-277), so the thread plan in `examples.md:26` is grounded. The "`MetaBeliefs` dictionary" (SKILL.md:38), the "SWE mini example" and the "System 3 article" itself are not in the repo. The Leibniz/uncle joke checks out (`00-preface.md:5`). The overlap with the Arabic blog can't be checked, because no blog text is in the repo.

**Fix.** In `examples.md` §"System 3 article", add the article's link and date, and say that `MetaBeliefs` comes from the article's code and not from the book. Then a model won't search `chapters/` for it.

### 12. No record of which version of a chapter a post was cut from (gap)

**Evidence.** Chapters are still moving. `resources/evaluations/2026-10-02-approval-list-preface-ch6-ch13.md` has pending fixes for Ch6, and Ch6 changed in `1d48f9b`. levantine-translate:45 already has a sync rule ("Record which English commit or version it was translated from"). chapter-to-post has none, so a post can quote a line that a later pass cut.

**Fix.** Add to "Delivering":

> Note the chapter file and commit the post was cut from. If a later pass changes a line the post quotes, say so.

---

## Priority 3: cross-skill overlap and description

### 13. The Arabic route conflicts with levantine-translate (gap / wrong)

**Evidence.**
- SKILL.md:42 says "adapt rather than translate line by line".
- levantine-translate sets an explicit fidelity mode, faithful or edit-while-translating with a `ملاحظة تحرير` log (levantine:16).
- It also says "Don't add jokes Hani didn't write" (levantine:28).
- On its own, "adapt" invites embellishment that levantine forbids.
- levantine:13 notes that Chapter 6 already exists in Levantine "to match the blog". An Arabic blog entry from Ch6 would therefore overlap an existing Arabic text that chapter-to-post doesn't mention.
- Both descriptions claim the Arabic blog: "Arabic blog entries … 'blog version'" here, and "blog posts … 'Arabic version'" there.

**Fix.** Replace SKILL.md:42 with:

> - **Arabic version.** Decide the idea and shape here, then hand the writing to levantine-translate (Levantine register for the blog, edit-while-translating mode, so every departure is logged). "Adapt" means finding Arabic frames for English jokes under that skill's rules, not adding new ones. Check whether the chapter already has an Arabic version (Chapter 6 does) before writing a second one.

### 14. Description: too broad on "excerpt" and "blog version", and it claims de-LLM (polish)

**Evidence.** The current trigger list ends with "excerpt" and "blog version".
- **"excerpt"** also matches back-cover or retailer excerpts, and blurb requests that belong to author-voice or the build.
- **"blog version"** collides with levantine-translate.
- **"de-LLM"** is listed under "Covers". A request like "de-LLM my Coffee & Commute post" names this skill and de-llm equally, and de-llm should own it.
- **Missing triggers:** "post about chapter N", "LinkedIn article", "Substack", "teaser".

**Fix.** Proposed description:

> Turn Hani's System 3 chapters, research or ideas into short public pieces: Coffee & Commute posts, LinkedIn feed posts, articles and threads, newsletter issues, and the English plan for an Arabic blog entry. Covers choosing the one idea a post carries, his post shape (an outside lens on a sacred object in tech culture, why it survives after people know it's hollow, then the knife turned on himself), beat-by-beat drafting with him, and checks against spoiling the book, employer exposure, repeating earlier posts and unverified fresh claims. Use whenever the user mentions Coffee & Commute, a LinkedIn post or article, newsletter, thread, teaser, or "turn this chapter into a post". For line-level cleanup of a finished post use de-llm; for the Arabic text itself use levantine-translate.

### 15. Small mechanics (polish)

- **Date format.** SKILL.md:32 says "then the date" without giving a format. `examples.md:9` writes "30 Jun 2026", while author-voice:93 uses "28 February 2017". Fix: "then the date, written '30 June 2026'."
- **Fetching the source.** SKILL.md:23 says "Ground it in the real source; fetch it." Fix: "fetch it (web search or the URL he gives) and put the link in your notes."
- **Spelling in the skill.** `examples.md:30` uses "monetisation" and SKILL.md:15 uses "criticises". That's harmless in a skill, but posts should use American spelling (see #3).

### 16. Side finding for the author-voice audit, not this skill (bug in another skill)

`voice_check.py` matches British spellings by prefix (`re.search(r"\b" + w, low)`, line 69).
- **False positive.** On the dry run it flagged "programme" for the word "programmers".
- **False negative.** It missed "travelled", because that isn't in the list.

Fix: match whole words (`r"\b" + w + r"\b"` for the full words, keep the prefix match only for stems such as `organis`) and add `travell`, `modell`, `cancell`.

---

## Proposed checks (a small `scripts/post_check.py`)

These would have caught #3, #4, #5, #7 and #9 during the dry run.

1. **Length:** characters and words against the chosen surface (feed post: 3,000 characters).
2. **Body em-dashes:** count them, excluding the header line.
3. **Copied runs:** reuse `voice_check.py --book chapters/` logic to list 8+ word runs copied from `chapters/`, so each one is flagged as a callback or rewritten.
4. **Spoilers:** grep the draft for every "Pays off" anchor in `easter-egg-register.md`, plus "We call it science", plus any distinctive line from `13-the-prophecy.md` (case-folded and quote-normalised). Each hit is a hard warning.
5. **Repeats:** read the post log in `references/examples.md` and warn if the declared lens or sacred object matches an earlier row.
6. **Unanswered gaps:** count `[AUTHOR: …]` markers and list them, so open gaps are visible before delivery.
7. **Employer terms:** warn on terms from a short author-maintained list (team names, internal tool names) that don't appear in `chapters/`.

## Dry-run summary

Following the skill exactly, the Chapter 6 post came out like this:

- **Lens:** Alexander's asterisks.
- **Sacred object:** best practices / design patterns.
- **Why it persists:** naming is free, checking costs an afternoon.
- **Knife inward:** his own "preserve the wandering" brief (06:243, real).
- **Practical turn:** mark your rules with asterisks.

It ran to 631 words and 3,980 characters. Problems hit along the way:
- I had to invent the discussion answers (#6).
- I invented a train scene and had to retract it (#4).
- There was no self-description frame to close on (#4).
- Both the sacred object and the "why it persists" answer were too close to earlier posts, with no rule to judge them by (#9).
- The draft is too long for a feed post (#5).
- voice_check flagged it as choppy, with an em-dash and four copied runs, all from following this skill (#3).
- There was no exposure rule to apply (#1).
- I left the Bing story and the invented Ines case out by my own judgment; the skill didn't say to (#4, #7).

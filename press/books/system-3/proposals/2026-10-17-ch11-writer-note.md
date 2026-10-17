# Writer's note: Chapter 11 draft ("Guess First"), 2026-10-17

owner: writer-system-3 (Callum) · for: head-of-book-system-3 and, after the reviews, the founder
**Keep this apart from what reviewers see first.** The development editor and the panel read the chapter text cold, without this note or the source map (brief §7.2).
draft: `chapters/11-the-store-that-builds-itself.md`, branch `ccr-fd4ebbbc-p06k8x`, **not committed**
companions: `press/books/system-3/proposals/2026-10-17-chapter-11-source-map.md` (fact-checker only), `press/books/system-3/proposals/2026-10-17-chapter-11-consequential-edits.md`
status: **draft. Not reviewed, not fact-checked, not accepted by the founder. I have not marked any of it checked.**

## What I read

Brief (all); press README and my role file; working spine; `ai-tells` skill; Chapters 4 and 5 in full; easter-egg register; old Chapter 11 in full; Chapter 10's last section; Chapter 12's opening and the lines the brief names (79, 89, 169, 235, 239); the Part V page; the evidence record and the fact-check (FC corrections used throughout); the structural and book studies' sections 3-7 (not every line of either; I read the dependency tables, strains, hand-offs, voice and constraints sections). Company sources, read-only: the base-rates `Demo.tsx` and `meta.json`, its simulated-learner review, `DemoCard.tsx` and `src/lib/trust.ts` (the learner's trust sheet), `CLAUDE.md`, `company/principles.md`, `mission.md`, `product/surface-value.md`, `product/vision.md`, constitution Article 4, AMD-008's header, `EXP-002`, the decisions on company structure, feed, deploy approval, no git deployments, org and dispatch, throughput for 10k and the r9 Safari waiver, the 10-15 COE, the 10-16 delegation retro, the pattern "a rule without a mechanism is a wish", and the left-or-right `meta.json`. I ran nothing that changes state in the company repo; I ran the lesson's `town()` function in my scratchpad (source map items marked W).

## Shape, headings, length

Shape B, eight `##` sections, the brief's working headings unchanged: Ninety-Nine Percent Accurate · Nine Claims Behind One Minute · A Company in a Week · Built From the Book · The Book Comes Back to Bite Me · Willing to Lose · Written Where Someone Can Argue With It · The Student Has Not Been Asked. Title *Guess First*, subtitle *One Minute, One Learner* (D2 default). Filename kept (D3).

Length: **4,778 words by `wc -w`** (inside 4,000-5,500). Of that, **14 AUTHOR comments are about 725 words; the prose alone is about 4,050.** That is near the bottom of the band. I did not pad (brief §2.2). If the founder answers the asks, the prose will grow into the band naturally; if the panel finds the draft thin, the first place I would add is §1 (one more beat of the lesson) and §7 (the pressures), not §5.

## check-tells and check-eggs

`python3 resources/editorial/check-tells.py 11 --lines` (final run):

| maxim% | notXbutY/1k | cite-chains | xref/1k |
|---|---|---|---|
| 26% (target ≤ 30) | 0.0 (≤ 0.5) | 0 (0) | 0.0 (≤ 0.5) |

All four targets met. The old chapter scored 21%, 0.4, 0, 0.0. My first draft had xref 0.6, from "this chapter" twice and "next chapter" once inside an AUTHOR comment (the counter reads comments); I rephrased all three. The 11 flagged maxims are short last sentences. I kept the ones a scene in the same paragraph earns ("That part was luck." was a rewrite of a "not X" construction; "I would not soften either half." follows the override scene). The weakest are "The records hold no figure for money." and "Nobody knows the answer yet, including the company."; review-llm-tells may want them.

Other counts I kept by hand: **0 em-dashes**; no bold terms; no chapter numbers in running text; about 32 prose colons (Chapter 4 has about 41 in a similar length), most introducing a quotation; none of the skill's vocabulary list in a figurative sense (grep finds only the literal "harness" for a test harness); no "This chapter…".

`bash resources/editorial/check-eggs.sh`: **passes, exit 0, no warnings** (the camel anchor "And now the camel comes back" holds in the same file). No new seed planted. "Coffee" does not appear (I removed one stray "with a new coffee" in revision).

`validate_references` from `book-design/curated/manuscript.py`: **passes** ("references OK"); both `ref-11-*` entries are cited, numbered [1] and [2] in order.

## What I kept

- The A/B-test line verbatim, with "Otherwise it is branding." directly after, in §6, in the old logic (earn complexity against simplification; here the single-agent baseline the founding decision itself names).
- "The Book Comes Back to Bite Me" as a heading (§5).
- The camel sentence verbatim (§2), one mention, no gloss beyond the questions it already lists. I cut the old follow-up sentence ("The argument about hallucination from earlier in the book…") to avoid stitching.
- The 11:7 AUTHOR comment verbatim, directly after the store passage's first sentence (new line 45).
- The author's store sentences (brief §3.4), trimmed, nothing added about what the prototype did or why he stopped.
- "Let the LLM narrate. Do not let it declare reality." (§5, the checking-the-disk beat).
- "If your ecosystem rewards clicks, clickable organisms evolve." arrives as the company's mission quoting it back (§7).
- `"humanLearners": []` used once, in §8, as the code punchline.

## What I cut or moved

Everything listed in the consequential-edits file §2. Not reused, though the brief allowed it: "'The model chose it' is not an answer…" and "a junk drawer with tenure" (neither found a natural home without forcing).

## Decisions I made where the brief left room

1. **Three bites in §5, all three of the brief's (a)-(c).** I kept (b) to one paragraph so the section stays near its 750 target. The QA-label alternative (C12) is not used.
2. **Founder quotations: two places, three quoted strings**, each with an AUTHOR permission comment and a ready paraphrase: the throughput complaint (§5), and "Deploy" with the option label "Ship it anyway" (§7). I did **not** quote "yes, deploy r7": it carries a release number (brief §2.3) and the scene works without it ("The founder approved it."). Both places say the words reached the record through an agent, per FC row 94.
3. **"Ship it anyway" is presented as the option he chose, and "Deploy" as his word** (FC correction 8). The override is called "an override of a review's ruling", not of a gate (FC row 74 note).
4. **The COE's fifth why is described as landing on a person** (FC dispute on C1); the record's "named a mechanism, not a person" is not used.
5. **C6's retro numbers are labelled the retrospective's own, testimony-grade, and not recomputable** (FC correction 7), with today's file's direction (every dispatch still the chief of staff's) added from the FC.
6. **C5 is a "new run at its latest commit"** (FC correction 6), fenced in the same paragraph as not the planted-diagnosis test, with the one-model limit.
7. **C8: only the dated sentence** in §8 (D16). The r9 deploy is described as approved, never as shipped.
8. **Added detail from the lesson's own code** that the brief did not list: the first hundred people contain no sick person but one positive; the first sick person arrives around the third hundred; the card is budgeted at 80 seconds although the company calls its lessons sixty-second; the trust sheet's exact wording and its footer ("0 human-learner studies… only people can show that a lesson teaches"). These are W items in the source map; the fact-checker should rerun them.
9. **Added from company records (new X items, not in the record):** the day-one vision of "8 domains, ~20 lessons" (X5); constitution Article 4.3 "Disputes about evidence are settled by tests. Disputes about purpose go to the founder." (X6); the principles file's practice for the A/B line, "Experiments include a simpler baseline that is allowed to win." (X10); the knot lesson's title *Can a knot match its mirror?* (X13), which ties C14 to C9; AMD-008 `proposed_by: founder` (X16); "Gates held while the delegation did not…" (retro line 52, quoted in SS S6).
10. **The press is named once, in §4**, with the observation that the author is the one reader outside the model (D11 default).
11. **Rented capacity** is one clause in §3 ("one developer's models, rented by the token"); the teaching condition is one sentence in §8.
12. **The ending** goes to the empty field (D10 default), with the AUTHOR comment where a real learner's guess would go, the profession beat as an AUTHOR comment before the last paragraph, and a closing question handing on to Chapter 12 ("Who decides what the capacity is for, when the people it is for cannot?").
13. **"Every learner review on file opens with…" was softened** to "The company's rules make every learner review open with…" after I found 17 of 1,811 matching files without the line.
14. **Spelling:** the book's American spelling in prose ("personalized", "organization"); company quotations keep theirs.

## Places I am least sure of (for the development editor, after her cold read)

- §4's last sentence ("the author is the one reader who is not a copy of it, which is an awkward thing to have to point out about your own book") is argued first person about the book's making. It is true of the process, but the founder may not want it in his voice.
- §5 is the longest section and the most like a report. It is where the panel may find the "tour" the brief forbids.
- "If you picked 99%, you are in good company, and some of it has medical degrees." is my joke in the author's voice. Cut if it reads as mine.
- "The best idea in the store was about the objective" is a judgment in the author's voice; it rests on the old chapter's own emphasis, but he should confirm.
- The closing paragraph's "asked a thousand times for a guess" is a figure over 1,283 lessons.

## AUTHOR asks in the draft (14 comments)

| # | Where | Ask |
|---|---|---|
| 1 | §2 end | Ask 4: one moment you watched it work (a lesson you learned from, a catch that surprised you). |
| 2 | §3, after the store's first sentence | **Moved verbatim from 11:7:** "What did the prototype actually do or show? A screen, a session, a surprise? One moment from the prototype would anchor the chapter." |
| 3 | §3, end of store passage | Ask 2: why lessons and not the store; what happened to the prototype (plus a note that cutting the passage needs acceptance for the 11:7 comment and removes [1]). |
| 4 | §3 | Ask 1: what made you start the company, and when; may the book use your words. |
| 5 | §3 | Ask 11: hours per day in the first week; money spent. |
| 6 | §4 | Ask 17: the press named once as a limit: keep, cut, or reword (D11). |
| 7 | §5 | **Quotation permission (ask 14, D4):** "What is going on you are working all the day but number of demos did not move"; paraphrase ready; confirm it is what you typed. |
| 8 | §5 | Ask 5 (a moment you watched it fail; agent or mechanism) and ask 8 (mechanisms from previous employers; may they be named). |
| 9 | §6 | Ask 9: fourteen subjects before one real learner: a choice, and again? |
| 10 | §7 | Asks 3 and 12: what you wanted on day one and now; is 10,000 the goal or a stand-in; why a feed, why an ad slot, who pays. |
| 11 | §7 | **Quotation permission (ask 14, D4):** "Deploy" and the option "Ship it anyway"; paraphrase ready; plus ask 7 (did an agent refuse you and turn out right, or you override one and turn out right). |
| 12 | §7 end | Ask 13: should learners have standing to contest the objective, and how. |
| 13 | §8 | Ask 6 / D10: has anyone outside used a lesson; will you run the five-learner test; where one person's verbatim guess would go. |
| 14 | §8, before the last paragraph | Ask 10: what running the company did to your own job; does the old last paragraph still hold. |

Asks 15 (Mei, Sami, Lea) and 16 (title) are in the consequential-edits file only, as the brief says. Naming (D5) is not a comment: the draft names only "System 3 Company" and generalises every vendor ("the hosting service", "one developer's models"); Safari and iPhone are named because they are the risk the founder accepted, and the founder may want them generalised too ("one phone's browser").

## Handoff

- **Changed:** `chapters/11-the-store-that-builds-itself.md` (full rewrite, in place, uncommitted); wrote this note, the source map and the consequential-edits file; added a dated entry at the top of `press/progress.md` (brief §7.1). Nothing in `/home/user/system-3-company` touched. Chapter 13 not opened.
- **Believe:** (high) every must-keep and honesty item in brief §3-§4 is in the text beside its claim; (high) the checkers pass; (medium) the voice is close to Chapters 4-5 in §1, §2 and §5, flatter in §7; (medium) the fact-checker will find small wording issues in the W and X items, which I could not check myself.
- **Next:** development-editor-system-3 reads the chapter cold (owner: head of book routes); fact-checker-system-3 works from the source map's X and W items, rechecking C8's timestamp first; the founder answers the 14 comments and decisions D2, D4, D5, D6, D10.
- **Blocked:** nothing for the draft. The ending and the profession beat wait on the founder.

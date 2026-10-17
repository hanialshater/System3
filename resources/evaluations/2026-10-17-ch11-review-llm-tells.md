# Chapter 11 review: LLM tells

- **Date:** 2026-10-17
- **Reviewer:** Vesna, review panel (review-llm-tells), consultant to vp-books
- **Text:** `chapters/11-the-store-that-builds-itself.md` (heading "Chapter 11: Guess First"), the new draft as it stood on disk on 2026-10-17
- **Baseline:** Chapters 4 and 5 (read: Ch4 opening through "Saussure's Specification"; Ch5 opening through the harness, and "The Society Gets Smarter by Making People Narrower" through the Bromiley case)
- **Method:** `.claude/skills/ai-tells/SKILL.md`, Steps 1-4. Read cold. I did not read anything in `press/books/`, the writer's notes, the brief or any earlier review (including `resources/editorial/llm-tell-review-2026-10-10.md`) before writing this record. I read `resources/editorial/easter-egg-register.md` for seeds.
- **Lens:** LLM tells only. Sentence quality is Edith's record (`2026-10-17-ch11-review-prose-quality.md`).
- **Status:** report only. No manuscript file was edited. Suggested rewrites below are proposals for the writer and the author, not patches. All `<!-- AUTHOR: ... -->` comments stay; none of my fixes removes one.

## Step 1: checker numbers

`python3 resources/editorial/check-tells.py 11 --lines`

| chapter | words | maxim% | notXbutY/1k | cite-chains | xref/1k |
|---|---|---|---|---|---|
| 11-the-store-that-builds-itself.md | 4,780 | 26% | 0.0 | 0 | 0.0 |
| *Ch4 baseline* | 4,512 | 26% | 0.2 | 0 | 0.2 |
| *Ch5 baseline* | 8,165 | 38% | 0.5 | 0 | 0.2 |
| *Targets* | | <= 30 | <= 0.5 | 0 | <= 0.5 |

Every number is inside target. The counter's 12 maxim hits, read in context:

| Line | Hit | Reading |
|---|---|---|
| 7 | "Right?”" | False positive (a quotation on the card). |
| 33 | "The claim stayed disputed until the builder rewrote it." | Event, not maxim. Keep. |
| 37 | "The independence the note asked for is not on record." | Part of the "not run" drumbeat (finding 3). |
| 47 | "The page is smart inside the modules and surprisingly dumb between them." | Earned; the author's voice. Keep. |
| 61 | "The records hold no figure for money." | Plain fact that sets up an author ask. Keep. |
| 83 | "Nobody has measured whether it works." | Drumbeat (finding 3). |
| 89 | "The hosting service built the commit and promoted it to production." | Narrative climax. Keep. |
| 97 | "Do not let it declare reality." | Unearned slogan (finding 6). |
| 113 | "The tests are code, and the counts are what the code produced." | Unearned, near-tautology (finding 6). |
| 121 | "Nobody knows the answer yet, including the company." | Drumbeat, mild (finding 3). |
| 125 | "Disputes about purpose go to the founder." | States a rule. Keep. |
| 131 | "I would not soften either half." | Unearned; closes an abstract paragraph (finding 6). |

The counter is not where this chapter's problems are. It scores 0.0 on "not X but Y" because the draft has almost no literal "not X but Y". It has a different contrast habit, the **"X is designed. It has not been run."** pair, which the counter does not look for. And it has a tell the skill's list does not name: the **evidence-chain voice**. Sentences report where a number came from, who copied it and who reran it, the way a fact-checker's notes do. That is the main thing that reads as written by a committee of agents.

## Step 2: findings

Severity: **must** = fix before the chapter goes to the founder for acceptance; **should** = fix in this revision; **could** = the writer's judgement.
"Needs author" = the fix needs a real scene, a real number, a permission or an authorial decision. "Line edit" = cut, reorder, merge or rephrase, adding nothing.

### 1. Evidence-chain voice: provenance sentences pasted into the prose (must; line edit plus routing)

Tell: none of the skill's numbered tells quite covers it. It is closest to 17 (abstract nouns doing the work) and 5 (signposting), applied to sourcing. Paragraphs that have just told an event end by auditing it. One clear fence for the whole chapter (line 35) is honest and strong. After that, the same disclosure keeps coming back, sentence by sentence, in the register of a verification log:

| Line | Quote (exact) |
|---|---|
| 61 | "from a ledger with known gaps, so the real figure is higher." |
| 81 | "Those are its counts at the time, and it labels its own table testimony-grade. The log was backfilled afterwards, so they cannot be recomputed from today’s files, though every dispatch in today’s version of that window still names the same actor." |
| 85 | "Those are the company’s numbers, which I have not recomputed." |
| 91 | "The hosting service’s own commit statuses show all of this, and a script in the press’s evidence folder reruns the old filter against the saved messages and reaches the same verdict, so this incident is run as well as recorded." |
| 113 | "So the press wrote a new harness for the 15 of those 22 bugs it could reproduce exactly, ran it against the company’s committed tests at its latest commit, and all 15 were caught, each with exactly the failing count the record printed." |
| 127 | "Those words reached the file second-hand: the release manager wrote them down from what the chief of staff relayed." |

Chapters 4 and 5 never do this in running prose. Ch5 tells the Bromiley case and puts the source in the note.

Suggested fix: say once, early, what kind of evidence the chapter runs on (the line-35 fence already does most of this), and move the per-number provenance to notes or to `appendix-note-on-evidence.md`. Then end each scene on the event:
- Line 81: end on the quote, "…in practice there was one dispatcher who asked managers questions.” Move the backfill sentence to a note.
- Line 91: end on "That part was luck." Move the commit-status and rerun sentence to a note.
- Line 113: "The press rebuilt 15 of the 22 and all 15 were caught again" is enough in the text. The harness details go to a note.
- Line 127: cut the last sentence. The author comment after line 127 already asks the founder to confirm the wording. If he confirms it, the second-hand caveat is no longer needed. If he does not, the fallback sentence replaces the quote.

Routing: these disclosures may exist because a fact-check required them. Moving them to notes is a line edit. **Dropping** any of them is the fact-checker's call (fact-checker-system-3), with the development editor reconciling. The author decides the house policy: are provenance caveats inline or in notes?

### 2. The author is absent as a person; the founder is reported through records (must; needs author)

Tells 4 and 17: second-hand material doing a lived example's job, and abstraction where a scene belongs. The baseline's strength is scenes the author lived ("I remember sitting with the offer and feeling faintly embarrassed for everyone involved", Ch5). In Ch11 the "I" appears in the store passage and in asides. The man who ran the company appears in the third person, through what agents wrote down about him:

- Line 85: "his complaint is on file, as an agent transcribed it"
- Line 91: "while he was being told nothing had been deployed"
- Line 127: "His recorded word was “Deploy”"
- Line 149: "So this is what one founder and about a hundred roles of agents did"
- Line 43: "After years working on ranking and recommendations, I built a prototype store because the idea would not stay on the page." The store is the chapter's only first-person thread, and no moment from it is told (the author comment after line 43 asks for one).

This is the largest gap between Ch11 and Chapters 4-5. The draft does the right thing by not inventing feeling ("the draft writes no feeling for you", author comment after line 149). But the result is a chapter about an organization told entirely from its files.

Suggested fix: no line edit can fix this. In my judgement the asks that would do the most work are **Ask 5** (one moment watching the company fail; the deploy incident in lines 89-91 is the natural place for it), **Ask 6** (one real learner's guess, which would let the chapter end on a person) and **Ask 4** (one catch that surprised him). There is also a decision for the author: does "the founder" become "I"? See Edith's record, finding 1.

### 3. Repeated formula: "designed / not run" (should; line edit)

Tells 9, 11 and 12. The chapter's honest point is that nothing has been measured, and it makes that point with the same two-beat cadence at least ten times:

| Line | Quote (exact) |
|---|---|
| 37 | "The arithmetic in both is simple. The independence the note asked for is not on record." |
| 83 | "The fix is written down. Nobody has measured whether it works." |
| 105 | "As of 17 October nobody has run it." / "The company has eight numbered experiments, and none of them has a result." |
| 113 | "The company adopted that test as its first experiment. It is designed and has not been run." |
| 117 | "so for now the fourth line of the company’s objective measures nobody." |
| 121 | "As of 17 October it is drafted and not ratified." / "Nobody knows the answer yet, including the company." |
| 145 | "It was designed on the day the company started. It has not been run." |
| 149 | "and the bet is unmeasured." |
| 153 | "is still waiting for its reveal." |

Each one is true. Together they form a drumroll, and by line 145, where this beat matters most (the five-learner test), the reader has heard it eight times. Suggested fix: keep it at full strength in three places: line 117 ("measures nobody"), line 145 and line 153. Elsewhere, state the fact without the pause:
- Line 83: "The fix is written down. Nobody has measured whether it works." becomes "The fix is written down; whether it works has not been measured."
- Line 113: cut "It is designed and has not been run." Line 105 and line 145 already say it.
- Line 121: cut "Nobody knows the answer yet, including the company." The sentence before it, "…is the live test of the store’s best idea", already says it.
- Line 149: see finding 4.

### 4. Closing recap paragraph and doubled ending (should; line edit, one part needs author)

Tells 5 and 10. Line 149 lists what the reader has just read: "So this is what one founder and about a hundred roles of agents did in under five days: more than a thousand lessons, a checked claim behind every factual sentence of the ones marked published, gates that held, and a record honest enough to show where its own rules were wishes. It is a bet that this kind of capacity can be built to teach as well as to answer, and the bet is unmeasured."

The last paragraph (line 153) then repeats line 133. Compare "What the minute is for is written in a file the founder owns. The person it is for has not been asked, and if she were, she could open every claim and change none of the purpose." (153) with "She has no way to amend what the minute is for. Her interest is in the file because the owner chose to write it there." (133).

Suggested fix: cut line 149, or keep only "It is a bet that this kind of capacity can be built to teach as well as to answer." In line 153, keep "The company has asked a thousand times for a guess before it would show anything. Its own guess, that a minute like this teaches somebody, is still waiting for its reveal." It is the best ending in the chapter's own design, because it pays off the title. Then either end there or go straight to the question. Cut "What the minute is for is written in a file the founder owns." **Needs author:** where Ask 10's answer goes (the comment after line 149 places it before the last paragraph), and whether the chapter ends on the question (it hands off to the next chapter) or on "its reveal".

### 5. Signposting (should; line edit)

Tell 5.

| Line | Quote (exact) | Suggested fix |
|---|---|---|
| 67 | "I should say plainly what this company is, because it decides what it can prove. It was built from this book." | Start at "This company was built from this book." The next paragraph ("So resemblance counts for nothing here") does the "what it can prove" work. |
| 73 | "There is a second turn to the recursion, and I will name it once." | Start at "The company has a sibling, a press founded to make my books…" |
| 79 | "The book’s own warnings came true against the design built to heed them. Three are worth the space." | Cut "Three are worth the space." The "The first… The second… The third…" structure already counts for the reader. |
| 103 | "Everything so far costs something, from the roles and the gates to the reviews and the coordinator asking managers questions." | "All of this costs something." The list recaps the last two sections. |
| 139 | "Go back to the minute." | Keep. It returns to the scene rather than to the argument. |

### 6. Maxims and slogans the paragraph has not earned (should; line edit, one needs author)

Tells 1 and 18.

- Line 97: "The catch itself came from checking the disk instead of believing the report, which is old advice about language models wearing new clothes. Let the LLM narrate. Do not let it declare reality." It is an unquoted slogan couplet, and "wearing new clothes" repeats line 35's "one witness wearing different coats". Fix: end on "The catch itself came from checking the disk instead of believing the report." If "Let the LLM narrate…" is the author's own line from elsewhere in the book, it should be quoted as such; if not, cut it.
- Line 113: "The tests are code, and the counts are what the code produced." It restates "The tests are code". Fix: cut it, or merge it into the previous sentence: "The planters and the harness writer were all copies of one model, but the tests are code."
- Line 131: "That is the system working as designed. The objection kept its consequence on paper, and the owner held the switch. I would not soften either half." This is an abstract verdict after a vivid scene (line 127), in balanced halves. Fix: cut the paragraph; line 127 already shows both halves. If a verdict is wanted, keep the middle sentence only.
- Line 111: "A philosophy of emergence should be willing to lose an A/B test. Otherwise it is branding." The first sentence is the book's own Zen line (`appendix-zen-of-system-3.md`, and the Part 5 epigraph), and line 105 has already quoted its translation. That makes it the third time a reader meets it, standing alone as a two-sentence slogan paragraph. **Needs author:** keep the Zen line here (it is his) or let line 105 carry it; "Otherwise it is branding." is the draft's addition and could go.

### 7. The same "shows X / cannot show Y" pair twice (should; line edit)

Tells 11 and 12.
- Line 99: "It shows that nothing unchecked got through. It cannot show that “checked” means more than one copy of a model agreeing with another."
- Line 113: "That shows the tests can fail. It says nothing about whether a false belief planted in the notes…"

Keep line 99, where the limit is the point. Recast line 113 so it does not mirror line 99: "So the tests can fail. The test this book proposes for its own central claim is a different one: whether a false belief planted in the notes one worker leaves for the next survives into the next worker’s plan."

### 8. Every section the same shape, and tics that make it so (should; line edit)

Tell 7. Most sections run the same way: a record, a count, "As of 17 October", the limit, then an author comment. The tics that hold this pattern in place are countable:
- "As of [date]" or "As of the afternoon of": 9 times. Fix: state the date once, early ("Every count in this chapter is as of 17 October 2026"), and cut the rest, except where two dates are being compared.
- "own": 21 times ("its own retrospective", "its own accounting", "The rule’s own record", "its own table", "The hosting service’s own commit statuses", "The company’s own test", "Its own guess"…). Keep "Its own guess" (line 153, the payoff) and the "own" in line 37 if it is needed; cut most of the rest.
- "the company": 37 times. 35 of the chapter's 53 prose paragraphs open with "The". (Rhythm is Edith's lens; I note it here only because the repetition reads as generated.)

### 9. Cross-chapter callback a cold reader cannot decode, sitting on a seed (could; needs author)

Tell 6. Line 31: "And now the camel comes back: where did the claim come from, how strong is the evidence, what kind of knowledge is this, and how much trust should the system place in it before acting?" "And now the camel comes back" is a payoff anchor in the easter-egg register (The camel, status **proposed**), so it must not be cut or reworded without the author. The list of four questions after the colon recaps Chapter 4. Suggested fix, for the author to accept or decline: keep the anchor phrase exactly, and let the questions be the fields themselves rather than a recap. Do not explain the camel. Other callbacks work for a reader of the book and need nothing: "the organization becomes the bug" (line 81, after Ch5's "The organization was the bug") and "solved shopping before lunch" (line 49, after Ch1).

### 10. Catalogue sentences that read like a file dump (could; line edit)

Tells 10 and 17.
- Line 27: "The other eight cover what “99% accurate” means here, the expected counts, the half and the ninety-two, the rounding on the stage, the Harvard study, the sentence the reveal ends on, and the question that comes back days later." Fix: "The other eight cover the rest of the card, down to the rounding on the stage and the question that comes back days later."
- Line 69: "What can count is what the design did not predict, what failed, and anything tested against a simpler arrangement." This triad is the chapter's method statement and earns its place. Keep it.
- Line 121: "The pressures sit on the same files." An abstract opener. Fix: "The same files record the pull the other way."

### 11. Deliberate patterns to keep (protection list)

These match a pattern on paper, but they are the chapter's voice or its argument. Keep them:
- Line 11: "So you guess. Everyone guesses something, even the people who are sure they would never fall for it."
- Line 17: "If you picked 99%, you are in good company, and some of it has medical degrees."
- Line 23: "Nobody who made that minute is a person."
- Line 35: "One copy of a model catching another is still one witness wearing different coats", and the three outside witnesses: "the founder, code that runs, and the records kept by other companies’ systems." (a deliberate triad that carries the argument)
- Line 47: "The page is smart inside the modules and surprisingly dumb between them."
- Line 67: "about as surprising as finding flour in the cake."
- Line 73: "which is an awkward thing to have to point out about your own book."
- Line 89: "wrote a conscientious commit message saying so … to mention them it quoted the marker."
- Line 91: "That part was luck."
- Line 107: "The company went to fourteen subjects in its first week."
- Line 141: "That is a fair guess about adults, made by something that is not one."

## Step 4: verdict

The chapter mostly reads as written by a person: the opening card, the deploy incident and the asides are not machine prose. It reads as machine-made in the middle, in two ways. The counter flags neither. First, an **evidence-chain voice** keeps interrupting events to say who counted, who copied and who reran them. Second, **one contrast beat** ("designed / not run") does the work of an argument by being repeated. The structural gap against Chapters 4-5 is the author: the founder is present as records, not as a man who was there.

**Three findings that matter most**
1. Evidence-chain voice in running prose (finding 1, must).
2. The author absent; the founder in the third person through transcripts (finding 2, must, needs author).
3. The "designed / not run" drumroll, plus the recap and doubled ending (findings 3 and 4, should).

**Checker numbers:** 4,780 words; maxim 26% (12 hits: 1 false positive, 3 unearned); notXbutY 0.0/1k; citation chains 0; cross-references 0.0/1k. All within the Ch4-5 targets.

**Needs the author:** finding 2 (Asks 4, 5 and 6 above all, plus the "founder" / "I" decision); finding 4 (the ending and where Ask 10 goes); finding 6 (the line-111 Zen line); finding 9 (the camel seed); and the inline-versus-notes policy in finding 1, alongside the fact-checker.
**Line edits the writer can propose without the author:** findings 1 (moving, not dropping), 3, 5, 6 (lines 97, 113, 131), 7, 8 and 10.

## Handoff

- **Changed:** this file only. No manuscript edits, no commits.
- **Belief and confidence:** high confidence on findings 1, 3, 5 and 8 (all countable, all quoted). Medium-high on finding 2: it is a judgement against the baseline, but the draft's own author comments point to the same gap.
- **Next:** the development editor reconciles this record with Edith's (overlaps: her findings 1 and 2 with my findings 2 and 1). The head of book routes finding 1's caveats to fact-checker-system-3 before anything inline is dropped, and puts Asks 4, 5, 6 and 10 in front of the founder.
- **Blocked:** finding 2 and the ending wait on the author.

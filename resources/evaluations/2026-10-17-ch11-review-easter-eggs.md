# Review record: easter eggs, Chapter 11 draft ("Guess First")

- **Date:** 2026-10-17
- **Reviewer:** review-easter-eggs (Clementine), review panel consultant
- **Text under review:** `chapters/11-the-store-that-builds-itself.md` at the working tree on top of `c98653a` (writer's draft, proposal). Compared with the previous chapter at `HEAD~1` (`6a4912c`).
- **Also read:** `resources/editorial/easter-egg-register.md`; output of `bash resources/editorial/check-eggs.sh`; the planting and paying-off passages in chapters 4, 5, 7, 10 and 12, the Part V page and the Zen appendix, where the register points.
- **Not read:** anything in `press/books/`, the brief, the writer's notes, earlier reviews of this draft. Chapter 13 was not opened; every Chapter 13 judgment below is made against the register's anchors only.
- **Path note:** the role doc names the output `YYYY-MM-DD-easter-eggs-<scope>.md`; this file uses the path the commission named.
- Line numbers refer to the draft as it stands (`cat -n`).

## Verdict

**No confirmed seed is touched. Every anchor passes.** `check-eggs.sh` exits 0: all 36 anchors `ok`, including the only register entry inside Chapter 11, the camel (proposed), at "And now the camel comes back". The camel line moved from the store section of the old chapter to the claims sheet of the new one and still lands.

What the draft does disturb is around the edges: it adds new language that sits close to three proposed Chapter 13 threads and the reveal page, it plants one new seed that is not in the register, it leaves two callbacks whose plants were cut with the old chapter, and it leaves Chapter 12's reference to "Chapter 11's store" two lines from the camel's second payoff. None of these is a must; all of them are questions for the author.

### The three findings that matter most

1. **(F3, should)** The simulated-learner passage and the italic "*Can …?*" card title sit close to the tongue-and-ear thread's Chapter 13 anchor. New in this draft; author to decide whether it is a wanted rhyme or a pre-echo.
2. **(F8, should)** The recall question at line 19 is a new seed with no payoff and no register entry. Register it or close it.
3. **(F2, should)** Chapter 12 line 79 still calls Chapter 11 "the store that builds itself", one line from the camel payoff at Chapter 12 line 77. Whoever fixes that sentence edits next to a registered anchor.

## check-eggs.sh

```
exit 0. 36 anchors, 0 FAIL, 0 warn.
ok    proposed  11-the-store-that-builds-itself.md       And now the camel comes back
ok    proposed  12-after-capacity.md                     camels are native to Croatia
(all confirmed anchors ok: Coffee ×4, Reviewer 2 ×2)
```

## Findings

### F1. The camel (proposed): survives, re-sited. Severity: could (no action)

- **Location:** ch11:31. Old chapter: `HEAD~1` ch11:113.
- **Text now:** "And now the camel comes back: where did the claim come from, how strong is the evidence, what kind of knowledge is this, and how much trust should the system place in it before acting? Here those questions are fields in a file, and a learner can open most of them with one tap."
- **Text before:** the same question sentence, followed by "The argument about hallucination from earlier in the book has turned into a product requirement." It sat in the store section, after the insight-experience passage.
- **Reading:** the anchor is intact word for word. The new context is a sheet of numbered claims with a checked/unchecked status. The line works there at least as well as it did in the store. Nothing in the sentence depends on the store, which is now three paragraphs (ch11:43–49) and comes *after* the camel line.
- **Suggestion:** keep the anchor sentence as is. If a later pass rewords it, update the register row in the same commit (register rule 4).

### F2. Chapter 12's reference to "Chapter 11's store" sits next to the camel's second payoff. Severity: should

- **Location:** ch12:77–79 (not under review; read because the register points there).
- **Text:** ch12:77 "… or confidently tell you that camels are native to Croatia." (register anchor) then ch12:79 "The compiler has to compile. Chapter 11’s store that builds itself still needs its business experiment: an experience can convince the experts and the model and still fail the customer."
- **Reading:** the new chapter's heading is "Chapter 11: Guess First", and the store is a short prelude to the company. Ch12:79 will very likely be revised to match. That revision touches the paragraph after a register anchor, and ch12:77–79 currently read as one movement (the camel line, then the store sentence).
- **Suggestion:** the brief for whichever pass changes ch12:79 should name the register row "The camel" and the anchor "camels are native to Croatia" and require `check-eggs.sh` afterwards. Do not reword ch12:77 as part of that fix. (Routing: head of book.)

### F3. Tongue and ear (proposed): new simulation language and an italic question title. Severity: should

- **Register:** planted ch04 "*Can your tongue touch your ear?*" · Zen "The tongue cannot reach the ear." → pays off ch13 "But so would simulated fingers touching a simulated face."
- **Locations and text:**
  - ch11:139 "0 human-learner studies, 2 simulated-learner reviews, 2 browser QA runs" and the quoted "Simulated learners find problems; only people can show that a lesson teaches."
  - ch11:141 "Simulated learner. This review finds problems; it is not evidence that anyone learned." and "The simulated adult who reviewed the town of a thousand reported that it picked 99%, “and so would most adults”. That is a fair guess about adults, made by something that is not one."
  - ch11:127 the card title "*Can a knot match its mirror?*" (italic, "Can …?"), and ch11:7 "*You tested positive. Now what?*"
- **Reading:** the old chapter had none of this ("simulator" once, about replaying saved scenarios). The draft now uses "simulated" five times in two paragraphs, ends one of them on the narrator's own line about something judging adults without being one, and prints a lesson title in the same italic question form as the Chapter 4 plant. A reader who carries the Chapter 4 question forward will hear it here. Whether that helps or spends the Chapter 13 line is the author's call; I do not judge the payoff.
- **Suggestion:** ask the author. If wanted, add ch11:141 as a mid-book plant on the tongue-and-ear row (proposed). If not, keep "simulated" inside the company's quoted wording (139, 141 quotes are records) and drop it from the narrator's own sentences; the knot title can be named without the italic question form, or kept if the author confirms. No rewrite proposed here.

### F4. Standing outside the box (proposed): new "witness outside the model" lines. Severity: could

- **Register:** ch05 "with no one standing outside it" → ch13 "Behind it: forty monitors. Every timeline."
- **Locations and text:**
  - ch11:35 "The witnesses that are not the model are few: the founder, code that runs, and the records kept by other companies’ systems."
  - ch11:73 "In that whole chain, the author is the one reader who is not a copy of it, which is an awkward thing to have to point out about your own book."
- **Reading:** both lines are new, and both are about who stands outside a closed system. They do not use the anchor's words, and I see no collision with the Chapter 13 anchor text. They do make the thread louder two chapters before its payoff.
- **Suggestion:** author to read these two lines with the row in mind. No change needed unless he hears a pre-echo. If he wants them as plants, register them.

### F5. Capacity over power (proposed): the chapter now ends on "capacity". Severity: could

- **Register:** preface "Capacity over power." · ch12 "what capacity over power means to me" → ch13 "Capitalism doesn’t."
- **Location and text:** ch11:153 "Who decides what the capacity is for, when the people it is for cannot?" Related: ch11:121 "the company is not in the attention business", "one labelled ad slot", "a goal of ten thousand lessons".
- **Reading:** the old chapter ended on the author's profession and did not use the word. The new ending asks the Part V question (the working spine's own question for chapters 11–12) and hands it to Chapter 12, where the thread's mid-book anchor is. Being in Part V, that is expected. The closing question does not state the thread; it asks it. I see no pre-emption of the Chapter 13 anchor.
- **Suggestion:** none now. Re-check against this row if a later pass makes the ending answer its own question.

### F6. The reveal riddle (proposed): "reveal" becomes a working term. Severity: could

- **Register:** preface "we never thought to call it an architecture" → reveal page "We call it science."
- **Locations and text:** ch11:15 "The reveal does the division…", ch11:27 "the sentence the reveal ends on", ch11:37 "the general sentence at the end of the reveal", ch11:153 "Its own guess, that a minute like this teaches somebody, is still waiting for its reveal."
- **Reading:** the first three are product vocabulary (predict, explore, reveal) and harmless. The last one uses "reveal" figuratively, about the book's own argument, in a closing line. The book has a page that is itself the reveal. Low risk, but it is the one use that is the narrator's, not the product's.
- **Suggestion:** author to confirm the closing line's "reveal" is wanted alongside the reveal page. No other action.

### F7. 11:53 PM (proposed, may be coincidence): near-midnight timestamps before Chapter 12's opening anchor. Severity: could

- **Register:** ch12 "In October 1947" → ch13 "11:53 PM, three minutes."
- **Location and text:** ch11:57 "Its first commit landed at 22:51 UTC on 12 October 2026. By 14:21 on 17 October…"; ch11:89 "At 12:45 UTC the next day…"; ch11:91 "For about twenty minutes…". The chapter is dense with October dates and ends a page before "In October 1947".
- **Reading:** in UTC and 24-hour form, nothing here sits near the register's clock. A copy edit that converted the first-commit time to a local zone or to "PM" form would put a minute-precise late-night time in the chapter immediately before the anchor.
- **Suggestion:** keep these times in UTC, 24-hour form. Tell the copy editor (routing: head of book) not to convert them without checking this row.

### F8. New seed, not registered: the recall question that is never answered. Severity: should

- **Location and text:** ch11:19 "Days later the idea is supposed to come back as a single question. A condition affects 1 in 10,000, and the test is the same kind. Of the people who test positive, roughly how many have it? Almost all, about half, or about 1 in 100?" Echoed at ch11:153 "The company has asked a thousand times for a guess before it would show anything. Its own guess … is still waiting for its reveal."
- **Reading:** the chapter asks the reader a question, says it is meant to "come back … days later", and does not answer it. Either it is deliberate (a delayed payoff somewhere later in the book or the back matter) or it is an open loop. Register rule 3: new material that plants a seed must be added to the table.
- **Suggestion:** author to confirm. If deliberate, add a row (proposed) — Thread: "The recall question"; Planted: `11` → "Days later the idea is supposed to come back"; Pays off: wherever the author intends. If not deliberate, the chapter should close it; how is a momentum question (see the narrative-momentum record, finding M3). I do not state the answer here.

### F9. Two callbacks whose plants were cut. Severity: should (first), could (second)

- **(a) ch11:119** "The company’s mission even quotes one of my store sentences back at me: “If our ecosystem rewards clicks, clickable organisms evolve.”"
  - The store sentence it quotes back ("If your ecosystem rewards clicks, clickable organisms evolve.", `HEAD~1` ch11:111) was cut with the old chapter. A search of `chapters/` (excluding ch13, not opened) finds it nowhere else. "Back at me" invites the reader to recognize a line they have never read.
  - **Suggestion:** either reinstate the store sentence in the store passage (ch11:43–49) so the callback has a plant, or reword the mission line so it does not claim to be an echo. Not a register row; flagged because it is an echo with no seed.
- **(b) ch11:97** "The catch itself came from checking the disk instead of believing the report, which is old advice about language models wearing new clothes. Let the LLM narrate. Do not let it declare reality."
  - This was a section heading with its argument in the old chapter (`HEAD~1` ch11:171–179). "Old advice" now points to nothing earlier in the book.
  - **Suggestion:** acceptable as a maxim if the author wants it so; otherwise drop "old" or give it a source.

### F10. Unintended echo inside the chapter: the clothing image twice. Severity: could

- **Location and text:** ch11:35 "One copy of a model catching another is still one witness wearing different coats" and ch11:97 "old advice about language models wearing new clothes".
- **Suggestion:** one of the two images, not both. Writer's call.

### F11. Structural lines that other pages quote: intact. Severity: could (no action)

- ch11:111 "A philosophy of emergence should be willing to lose an A/B test. Otherwise it is branding." survives. It is quoted by the Part V page epigraph and the Zen appendix (line 52). In the old chapter it closed the store's experiment argument; now it follows "The company went to fourteen subjects in its first week." Still works.
- The old "> Picked for you." (cold-start passage) is gone; ch11:119 "Fresh picks" / "For you" carries the idea in the company's terms. Not registered; noted only.

### F12. Threads checked with no interference. Severity: none

- **Coffee (confirmed), Reviewer 2 (confirmed):** no occurrence in ch11, old or new. "I have definitely not solved shopping before lunch." survives (ch11:49).
- **Octopus, cable, DNA as a copier, the dream, the cathedral:** no related words in the new chapter.
- **Names (proposed):** the chapter names neither the model nor the founder, and does not use "audit". No interference.

## Outside this lens (for the head of book to route)

- `chapters/appendix-note-on-evidence.md` line 20 and `chapters/appendix-references.md` line 509 still title Chapter 11 "The Store That Builds Itself" and describe it as the prototype store. Not an egg issue; continuity.

## Handoff

- **What changed:** this record only. No manuscript, register or other file edited; no commit.
- **What I believe:** all confirmed seeds are safe (high confidence: script plus reading). The camel works in its new place (high). F3 and F8 are real questions for the author (medium-high: they depend on intent I cannot see). F4–F7 are low-risk watches.
- **Next:** the author answers F3 and F8 (register rows if wanted). The head of book routes F2 and F7 into the next briefs. The development editor reconciles F8/F9 with the momentum record.

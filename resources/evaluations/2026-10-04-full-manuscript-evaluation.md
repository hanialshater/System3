# Full Manuscript Evaluation — 4 October 2026 (evening)

Scope: the manuscript as of commit `bbe1f02`, after the day's Chapter 6 rewrite and the follow-up
edits from the morning review. Six independent readers read the text in full. Five each scored a
block of chapters against the 22 dimensions in `prompts/chapter-version-evaluation.md`; one read the
whole book for consistency only. Mechanical checks and spot verification of flagged facts were done
separately. No manuscript file was edited for this evaluation.

Caveat: this session edited Chapters 6, 7, 11 and 12 and the Note on Evidence earlier today. The
readers were told what had changed. Three of the problems below are errors in those edits.

---

## 1. Verdict

**About 7.5/10 on this calibration** (mean of chapter scores 7.5; whole-book reader 7.0). The
morning review said 8. The readers today scored every chapter lower, so the difference is mostly
calibration. The ranking is the useful part, and it largely agrees with the morning: Chapter 4,
the interlude, Chapters 6 and 10 at the top; Chapter 11 and Chapter 1 at the bottom.

The book's strengths are unchanged: a real spine, a voice that jokes in order to argue, motifs that
pay off, and a credibility model that matches its thesis. Its weaknesses are now clearer:

1. **The author's own evidence stops at Chapter 4** (04:277). After that the book reports other
   people's work or imagines its own. Several imagined or composite cases are not labelled in the
   text, which undercuts a book whose method is fenced claims.
2. **The reveal is pre-empted.** Chapter 5 uses the word *science* in a heading and twice in the
   text before the reveal page says it.
3. **Chapter 11 is in the wrong place or asks the wrong question.** It reads as a Part III
   application, not an answer to "what is the capacity for?", and it still carries details that
   point to the author's employer.
4. **Repetition across chapters** has been reduced but not cleared, and some is verbatim.

None of this needs a rewrite. Most of it is labelling, cutting and one structural decision.

---

## 2. Scores by chapter

| Chapter | Today | Morning | One-line judgment | Highest-value fix |
|---|---|---|---|---|
| Preface | 7.5 | 8.5 | Lively riddle, deck-shaped middle | Fold the three questions (l.27) into l.29 |
| 1. Betting on Agents | 7.0 | 7 | Alive, but all thought experiments | One real run for C1-5; resolve the orphaned AlphaGo line (l.52) |
| 2. Algorithm Vortex | 7.4 | 8.5 | Best teaching in Part I; key scene thin | Answer the l.199 author note; scores to five decimals |
| 3. Vibe Coder's Seat | 7.6 | 8.5 | Most alive and honest; ~1,000 words long | Cut "Stubbornly Human" pre-history to ~700 words |
| 4. System 3 | 8.0 | 8.5 | Strongest argument chapter | A real Creative Distrust case (l.287) |
| 5. Society of Agents | 7.4 | 8.5 | Richest material; a seven-stop museum tour | Retitle l.254 and hold back *science*; compress Senku, cut Newton |
| 6. Pattern Language | 7.8 | 8 | Most alive in Part III; middle becomes a survey | Label the composite and the projected agent beats; fix the code fences |
| 7. Recursive Self-Improvement | 7.5 | 8.5 | Tighter and funnier than 6; store unlabelled | "an imagined online store"; cut the Fire Phone |
| 8. Scalable Oversight | 7.3 | 9 | Well sourced, list-shaped | Keep "ExploitGym" for July only; stop tacking it onto section ends |
| Interlude | 8.0 | 8.5 | The book's most dangerous page | One concrete agent clause at l.15 |
| 9. Desire Layer | 7.6 | 7.5 | Most humane; middle sags | Cut Linden to a clause; stop l.11 pre-empting Ch10 |
| 10. Fluent Autonomy | 7.8 | 8 | Most lived and funny of the run | Count something for "embarrassingly measurable" (l.77) |
| 11. Store That Builds Itself | 6.8 | 7.5 | Clear, but a design review | Show one real prototype moment, or say "design" |
| 12. After Capacity | 7.6 | 8 | Warmest; too many essays under one roof | Label the community (l.143); tighten Derrida |
| 13. Prophecy | 6.5–8.5 | — | Real fiction; polarizing by register | Protected; three author-only notes in §8 |

The largest disagreement is Chapter 8 (9 → 7.3). Today's reader found it a survey with a punchline
ending most sections, and found the "ExploitGym" label stretched over two separate events (ref 1
keeps them apart; 08:15, 08:81, 08:87 and 10:103 merge them).

---

## 3. Status of the morning review's issues

| # | Issue | Status | What remains |
|---|---|---|---|
| 1 | Evidence thins as stakes rise | **Open** | Needs the author's material; see §5 |
| 2 | Disclosure inconsistent | **Partly fixed** | Ch11 still retail-specific; Ch7 now names the market; the Note's new line must be literally true (§4) |
| 3a | Ch12 restates Ch9 | **Partly fixed** | 12:37 still repeats 09:39's "training a model and running an evaluation somebody would believe" word for word |
| 3b | Saussure twice | **Fixed** | — |
| 3c | Count right, meaning wrong | **Fixed across chapters** | Inside Ch6, 06:185 and 06:189 say it twice five lines apart |
| 3d | Procedures outliving reasons | **Partly fixed** | Ch5 says it three times (05:92, 05:124, 05:280); 10:45 restates 05:120–124 |
| 4 | Ch6/Ch7 continuity | **Fixed** | Ch7's store is not labelled imagined (07:45) |
| 5 | Two dominant sources | **Partly fixed** | The new paragraph has the wrong chapter range (§4) |
| 6 | Length imbalance | **Open** (by the author's choice for Ch6) | See §7 |
| 7 | Housekeeping | **File names fixed** | 12 author notes remain, as intended |

---

## 4. Errors in today's edits

These came from this session and should be corrected first.

1. **Note on Evidence, two-sources paragraph.** It says Anthropic carries "Chapters 6 to 9". Carlini's
   compiler report frames Chapter 5, and Chapter 12 cites Anthropic at 12:175–177, so the range is
   5 to 9 plus 12. The paragraph also omits OpenAI, whose report frames Chapter 8; the Amazon–Anthropic
   investment the book itself states at 09:27 (by the book's own rule, two sources sharing an interest
   are closer to one witness); and that the AI used to write the book was Claude. Whether to say the
   last is the author's call.
2. **Chapter 7's store.** The edit "an online store that sells clothes and shoes" (07:45) names the
   employer's market, against the disclosure policy. "An imagined online store" fixes both this and
   the missing label.
3. **Chapter 12's callback** kept Chapter 9's sentence verbatim (12:37). It should point, not quote.
4. **The Note's new disclosure line**, "No chapter describes my current employer's systems", is
   only safe if Chapter 11 supports it. 11:207 says "Use a store's existing recommendation library",
   which implies a test on a real store. Either reword 11:207 ("an existing recommendation library")
   or confirm the line is true as written. Also confirm that *Surface Value*, *recommendation
   experiences*, *Coverage* and *Unmet Demand* are not internal names at the employer.

---

## 5. The evidence curve

| Ch | Main scenes | Mode | Labelled in the text? |
|---|---|---|---|
| 1 | Seeding life, imagined agent run, jacket | Imagined / argued | Yes ("Imagine") |
| 2 | Circle packing | Run (no raw data recovered) | Yes; data loss not stated |
| 3 | Demos, copy-paste, borrowed mind | Run / lived | Yes |
| 4 | Camel, the face, the ten-task experiment | Lived + run | Yes; exemplary |
| 5 | Carlini, Bromiley, Boyle, CERN; the Amazon offer | Reported + lived | Potter is not labelled |
| 6 | The grocer (Uncle Jalal, Ines, Sam) | Composite + reported | Composite signalled only by "call him"; agent beats at 06:300–327, 06:355, 06:460 are told as events, contrary to the Note |
| 7 | Omar, the store, the review board | Imagined + reported | Not labelled; author note open |
| 8 | ExploitGym, lab research | Reported | Yes |
| 9 | Mallorca ×2, clinic founder, shopper | Imagined + reported | Yes |
| 10 | Editing this book | Lived, but at summary level | Yes |
| 11 | Prototype, Mei/Sami/Lea | Designed / imagined | Customers yes; the prototype is claimed and never shown |
| 12 | Dantzig, Ostrom; workshop, community, irrigators | Reported + imagined | Community (12:143) reads as real |

This is still the book's largest weakness. The cheapest repair is labelling: one clause each at
06:6, 07:45, 05:92 and 12:143, and the conditional mood for Chapter 6's projected agent beats.
The more valuable repair is one real scene in each late chapter. These need the author's material
and must not be invented:

- **Ch6:** run the with/without comparison of a real pattern file on held-out cases that 06:312
  describes; the author's own editing brief (06:343) is a ready candidate.
- **Ch7:** one of the author's pipelines (circle packing or editing) changing its own procedure.
- **Ch9:** one real instance of a desire forming (author note at 09:53).
- **Ch10:** one session at transcript level: the paragraph cut, the brief line that should have
  protected it, and a real count. The data is in `resources/evaluations/`.
- **Ch11:** one screen or session from the prototype, and one surprise (author note at 11:7).
- **Ch12:** one tool built for a real small group, and what broke (author notes at 12:141, 12:259).

---

## 6. Structure

- **The reveal is pre-empted.** 05:254 "## Science Gets Bigger Than the Scientist", 05:252 "Human
  science has never escaped" and 05:264 "Science became more powerful" say the word first. Use
  "Bigger Than Any Expert" and "inquiry" or "research". The reveal page also stumbles at its own
  start: "in that sense and no smaller one" (reveal l.18) has nothing to refer to, and l.22 reads like
  the working-spine memo.
- **Part pages.** The Part II epigraph gives away two of Chapter 5's best lines. The Part III page
  signposts ("The next three chapters ask…"). The Part IV epigraph's second line repeats 08:117,
  which the spine forbids. Neither Part IV nor Part V poses a question, unlike Parts II and III.
- **Chapter 11.** It asks "what should the layer above do with them?" (11:17), which is a Part III
  question. Either move it to close Part III or reframe its opening and close around Part V's
  question. This is a decision for the author.
- **Chapter 6 states Chapter 7's thesis** at 06:442–452; it should stop at the question.
- **Chapter 9 uses up Chapter 10's opening** at 09:11.

---

## 7. Repetition and length

Repeats that do not work as motif:

- Verbatim: "emotionally satisfying and institutionally almost worthless" at 05:122 and 07:27.
- "A funding decision recorded beside the study it declined" at 10:107 and 12:183.
- The constitutional surface is restated at 08:117 and interlude l.15 after Chapter 7 owns it.
- "Same source, one witness" five times in Chapter 5 (05:56, 176, 178, 289, 293).
- The career refrain ("I spent years building systems that decide what…") appears six to eight times
  (04:196, 07:35, 08:15, 09:69, 10:113, 11:5, 11:73). Keep about three.
- The same quip shape, an abstraction "with" an object, at 05:48, 05:140, 05:182 and 05:222.
- Trail shoes for both the Chapter 9 shopper (09:73) and Mei (11:27): make it deliberate or change it.

Length, in printed words: Chapter 6 is 9,971 (16% of the main text, longer than all of Part IV at
about 5,200). The readers disagree on how much to cut: about 1,200 words with none from the grocer
story (the Chapter 6 reader), or about 3,000 (the whole-book reader). Both agree the cost is highest
in 06:280–365, where the grocer goes quiet for about 1,900 words. The author has asked to wait.
Chapter 3's pre-history (03:21–91, about 1,600 words) could go to about 700. Part IV is
underweight for the book's turn to human purposes.

---

## 8. Mechanical and factual corrections

Bugs, verified:

- **Chapter 6 code fences are escaped** (six escaped triple-backtick markers, added in today's rewrite). The YAML
  examples will render as a run-on paragraph and a list.
- **Note on Evidence, row 12** says Chapter 12 rests on "the small coding experiment from Chapter 4".
  Chapter 12 never mentions it. Row 11's "Prototyped" overstates what the text shows. Row 5 omits
  that Carlini's report is Anthropic's.
- **12:39** puts "The role moves upward" in quotation marks; no chapter says it (01:32 has "Control
  moves upward").
- **Chapter 6 says** "I avoid calling such a document executable" (06:288), then lists "executable"
  among the file's virtues (06:464).
- **Stale reference notes**: ref-06-alexander (Patterns 180, 203, 251), ref-06-gof (Hillside, *The
  Sims*), ref-06-instagram (body-image proportions) and ref-12-after-3 ("recommendation experiences")
  describe material no longer in the text. The Chapter 1 entries for Langton ("edge of chaos") and
  AlphaGo Zero belong to text that has moved.
- **11:117** "Add to Bag" where the chapter says "basket" everywhere else.

Facts, checked here:

- **02:209** "roughly 2.636, slightly above the 2.635 reference". AlphaEvolve's B.12 packing in
  `book-design/curated/circle-packing-reference.json` sums to 2.63586, which also rounds to 2.636.
  Give both to five decimals and say "best of N runs".
- **05:260** "A challenge posed in Switzerland". Johann Bernoulli was professor at Groningen when he
  posed the brachistochrone challenge in 1696. Probably wrong; check.
- **09:17** "the one player to win a game in that 2016 match" can be read to include AlphaGo, which won
  four. "Who won one of the five games" is exact.
- **06:221** "If the engine declares a winner between two copies of the same screen, the engine is
  broken." At a 5% threshold a sound engine does so one time in twenty: "more often than its error
  rate allows".

Flagged by readers, not yet verified:

- 06:377, the Instagram "bonuses" quote; 06:314, the Gloaguen v2 figures (v1 reported lower success
  with generated files); 08:111, "August 2026", 1,600 and 2.4% are not in ref 32; 12:175, "six billion
  output tokens" is not in ref-12-flt-tokens; 09:35, "1998" is not in ref-09-linden; interlude l.9,
  "with Stalin's permission"; 05:152, "The surgeon wrote to him"; 04:260–264, the epistemic agent's
  snippet resembles existing astropy code, so show the run's diff; 04:158, microscopes came before
  bacteria were seen; preface l.7, Leibniz's letter was nearly three years before his death.
- 06:10, ref-06-peacock: under Zahavi a costly display is an honest signal, while the feather motif
  uses the peacock for persuasive display. The appendix note already marks the comparison as the
  author's; the text could say "honest about elsewhere, silent about here".

---

## 9. Motifs and seeds

`check-eggs.sh`: 36 anchors, all present. Coffee, the camel, the octopus, the cable, the cathedral,
the face and "chaos with an API key" all pay off. Gaps:

- **Alberto** never returns after Chapter 4. 08:99 ("Doubt needs someone to call") is the natural place.
- **Reviewer 2** pays off one chapter later and then stops; a return near 10:101 would make it a thread.
- Register updates for the author to confirm: add Nickelodeon (13) ↔ "cartoons" (bio), the too-hot
  coffee in the bio, and "ideology vortex" (12:99) ↔ the vortex (Ch2); consider dropping the
  1947/11:53 entry, since Dantzig's October has no link to the Doomsday Clock.
- Chapter 13 notes for the author only (protected): 13:105 is the one place the fable lectures;
  "her father's tentacle" (13:113) after the octopus suit was removed (13:75); "Simulation" is
  capitalized only at 13:5.

---

## 10. What to do next

**Without decisions** (mechanical, safe): fix the Chapter 6 fences; correct the Note's rows 5, 11
and 12 and the two-sources paragraph's range; label Chapter 7's store "imagined" and drop "clothes
and shoes"; make Chapter 12's callback point rather than quote; remove the quotation marks at 12:39;
fix 06:288/464, 06:221, 09:17 and 11:117; cut one of each verbatim repeat (05:122/07:27, 10:107/12:183,
06:185/189); retitle 05:254; refresh the stale reference notes; check and correct the unverified
facts in §8.

**Needs the author:**

1. Chapter 11: confirm 11:207 and the terms in §4 against the disclosure policy, and decide whether
   it closes Part III or is reframed for Part V.
2. Labelling: approve the four clauses that mark the Chapter 6 composite, the Chapter 7 store, the
   Chapter 5 potter and the Chapter 12 community, and the conditional mood for Chapter 6's agent beats.
3. Real scenes (§5), at least for Chapters 7, 9 and 11.
4. Whether the Note names Claude as the writing tool and mentions the Amazon–Anthropic link.
5. Chapter 6's cut, when the chapter settles.

Readers' estimate of potential after the mechanical pass and labelling: about 8. With real scenes in
the late chapters and Chapter 11 resolved: 8.5 or better.

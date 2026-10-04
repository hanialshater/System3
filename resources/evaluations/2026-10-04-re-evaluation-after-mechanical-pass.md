# Re-evaluation after the mechanical pass — 4 October 2026 (night)

Scope: the manuscript at commit `6092e66` (the mechanical pass from
[the evening evaluation](2026-10-04-full-manuscript-evaluation.md)), read in full by six fresh
readers with the same scopes as before. Each scored the text independently first, then checked
every finding in the evening evaluation as FIXED, PARTLY FIXED or STILL OPEN. Three problems the
readers found in the pass itself were corrected afterwards (§3).

---

## 1. Result

**Still about 7.5/10.** The pass fixed what it set out to fix, but none of the four headline
weaknesses was in its scope, so scores moved only within the noise between readers (±0.2).
The whole-book reader credits the pass with about +0.1.

| Chapter | Evening | Re-read | Change | Cause |
|---|---|---|---|---|
| Preface | 7.5 | 7.7 | +0.2 | Calibration (text unchanged) |
| 1 | 7.0 | 6.9 | −0.1 | Calibration |
| 2 | 7.4 | 7.6 | +0.2 | Mostly calibration; the AlphaEvolve note helps accuracy |
| 3 | 7.6 | 7.4 | −0.2 | Calibration (heavier penalty for length and repetition) |
| 4 | 8.0 | 8.0 | 0 | Unchanged |
| 5 | 7.4 | 7.5 | +0.1 | Text: the retitled heading |
| Part pages + reveal | 7.0 | 7.2 | +0.2 | Calibration |
| 6 | 7.8 | 7.7 | −0.1 | Text improved; reader found new continuity slips |
| 7 | 7.5 | 7.6 | +0.1 | Text: store labelled, verbatim repeat cut |
| 8 | 7.3 | 7.3 | 0 | Unchanged |
| Interlude | 8.0 | 7.9 | −0.1 | Calibration |
| 9 | 7.6 | 7.6 | 0 | One fact fixed |
| 10 | 7.8 | 7.8 | 0 | Unchanged |
| 11 | 6.8 | 6.8 | 0 | Cosmetic change only |
| 12 | 7.6 | 7.7 | +0.1 | Two repeats removed |
| 13 | 6.5–8.5 | 7.0–8.5 | — | Calibration (protected, unchanged) |
| Whole book | 7.0 | 7.5 | — | Different reader; credits the pass with ~+0.1 |

Chapter mean (1–12): 7.48 before and 7.49 after.

---

## 2. Confirmed fixed by the pass

- Chapter 6: the three YAML code blocks render (six fence markers); the "count right, meaning
  wrong" repeat; the A/A-test claim; "executable" against the chapter's own disclaimer; stale
  reference notes.
- Chapter 5: the heading and two sentences no longer use *science* before the reveal; Bernoulli
  at Groningen.
- Chapter 7: the store is labelled imagined; the sentence repeated verbatim from Chapter 5 is gone.
- Chapter 9: Lee Sedol's one win. Chapter 11: "Add to Basket".
- Chapter 12: the Chapter 9 callback points instead of quoting; the funding-decision example is
  no longer repeated from Chapter 10.
- Note on Evidence: rows 5 and 12's Chapter 4 error; the source paragraph's range; OpenAI named.

## 3. Problems in the pass, corrected afterwards

- **12:39** "A role that moves upward describes…" did not parse. Now "That answer describes…".
- **12:37** "the two" after a single river read as two rivers. Now "named the two skills my job
  grew up around".
- **02:211** The AlphaEvolve note read as a buried concession after a semicolon. Now its own
  sentences: "But the reference was a rounded figure: AlphaEvolve's published construction sums to
  2.63586, so at three decimals the two results are level." 02:209 ("slightly above") and 02:213
  ("beat our reference") still need the run's score to five decimals, which only the author has.
- The pass's commit message said "six YAML code fences"; there are three blocks.

---

## 4. New findings

The evening evaluation missed these. Items marked ✓ were checked here against the text or a source.

**Continuity and internal contradictions**
- ✓ **06:185** "In every one of those tests the count was correct" contradicts 06:139, where a
  redirect dropped carousel users before logging. The "five incidents" later in the chapter
  (06:255, 06:310) depend on the same count. Author's call; one fix is "In the two tests that faded,
  the count was correct".
- **06:14** "the one person who could have said why was sitting by the door", while at 06:143 Sam
  "had not known why". Possibly deliberate irony; check.
- **06:306–309** a "six-week holdout" that keeps most customers on the slower checkout is a delayed
  launch; and the review gate (06:209) covers home-screen launches, not checkout.
- **06:355** an agent finds decay "across forty tests", but 06:292 and 06:442 say the archive never
  recorded the weeks after each test.
- ✓ **10:77** "scores ran from 2.26 to 2.636" mixes the hill-climbing endpoint with the agent's best
  run; 02:59 starts at 1.33.
- **11:13** "the first jacket he has seen in six months", but both customers are on the same page
  and Mei's candidates are trail shoes (11:27).

**The reveal**
- **05:192** "what separates science from other ways of settling belief" still names the
  architecture before the reveal page. Peirce's own word, "inquiry", fixes it. The printed table
  of contents also lists "Science Turns Inward" before the reveal; that may be acceptable.

**Facts to check**
- **Preface l.7** "Two years before his death": two readers place the letter to Rémond in
  January 1714, nearly three years before Leibniz died in November 1716.
- ✓ **07:70** "Move 37 won the game": "AlphaGo won the game" is exact.
- **07:132** "Seven years later": on checking, this stands. The paper was published at ICML 2023 and
  Pelrine's games were in February 2023, seven years after 2016 (the preprint was 2022).
- **07:47** "from Yudkowsky's to Weng's, say nothing about how you would tell": 07:192 then cites
  Weng placing evaluation outside the loop. Drop "to Weng's".
- ✓ **08:77** "Training the debaters": in Khan et al. the debaters were made more persuasive at
  inference time. "Making the debaters more persuasive" is exact.
- **06:290** "Calls to other skills": the Agent Skills specification has references, not calls
  (two readers).
- **06:361** "41.6": on checking, Anthropic's page gives "from 41.6% to 67.2%"; the text matches its
  source.
- **09:73** the multi-principal citation concerns combining several users, not a seller's hidden
  interest; **09:109** Paul argues testimony cannot convey what an experience will be like;
  **09:27** the stake is in the company, not the model.
- **12:5** "von Neumann seemed to be constructing the theory while he spoke": in Dantzig's own
  account von Neumann says he is *not* pulling it out of his sleeve, and credits his book with
  Morgenstern. His line is funnier and true.
- **Interlude l.19** "an owner may depend on fewer people's cooperation" is the page's biggest
  new claim and has no source or instance.

**Disclosure**
- Chapter 7's imagined store still sells sandals, winter boots, shoes and a jacket, and has "a
  product manager from the shoe category" (07:64, 07:80, 07:148, 07:170).
- Chapter 11 still describes fashion e-commerce throughout (size anxiety, return hesitation,
  outfits, a wedding outfit, size charts, "Complete the look"), and 11:207 still implies a test on
  a real store's recommendation library.
- 03:239 "the vocabulary our catalog uses" is first person and present tense.
- The Note's line "No chapter describes my current employer's systems" is not supported while
  11:207 stands.

**Note on Evidence**
- Row 11 still says "Prototyped" although no prototype output is shown.
- Row 12 omits the imagined community (12:143); "irrigators" blurs Ostrom's real ones with the
  imagined association.
- OpenAI also supplies 06:359 and 12:175, not only Chapter 8.

**Repetition not in the evening list**
- "Alignment by editing the human" presented as new twice (09:75, 12:219).
- The "more polished, worse" editing lesson three times (01:90, 09:11, 10:13).
- "Copies share one blind spot" four times (03:267, 05:176, 08:25, 08:81).
- The Part V epigraph is 11:211's best line, a few pages early.
- "Tuesday" as a verbal tic (04:200, 06:221, 07:108, 12:123, 12:151, 12:157).
- 08:47 repeats 08:11; 03:131 repeats 03:57 almost word for word.

**Part IV page.** A replacement epigraph that does not recap Chapter 8: "A prompt is evidence, not
the objective. / Leave the human room to change their mind."

---

## 5. Still open from the evening evaluation

All four headline weaknesses: the evidence curve and unlabelled composites (06:6, 05:92, Omar in
Ch7, 12:143), Chapter 11's placement and disclosure, the remaining repetition (career refrain, "same
source", procedures outliving reasons), and the part pages and reveal page wording. All 12 author
notes remain. Readers disagree on two earlier recommendations: one would keep Linden in Chapter 9
(09:39 depends on it) and one would keep the Fire Phone in Chapter 7.

## 6. What could be done next without decisions

05:192 "inquiry"; 07:70, 07:132, 07:47; 08:77; 10:77; 11:13; 06:290 "references"; the Part IV
epigraph; the Note's OpenAI clause and row 12. Checking first: the preface's Leibniz date, 06:361,
12:5 and the interlude's l.19 claim.

Needs the author: everything in the evening evaluation's "Needs the author" list, plus 06:185 and
the other Chapter 6 continuity points, and whether Chapters 7 and 11 should keep their apparel
detail under the disclosure policy.

---

## 7. Applied after this re-evaluation (author's instruction: no cuts of meaningful material)

- **Chapter 13 restored to the author's text** of 21 September (commit `48fdb6b`). The 30 September
  typography pass had changed its apostrophes and ellipses. `check-eggs.sh` now fails if the file
  changes; the seed anchors use the author's straight apostrophes.
- Preface l.7 "Nearly three years before his death" (letter to Rémond, 10 January 1714).
- 05:192 "experimental inquiry" holds back *science* for the reveal; 05:264 "colleagues".
- 06:290 "Pointers to other skills".
- 07:47 "from Yudkowsky's on"; 07:70 "AlphaGo won the game, and Move 37 became the move people
  remember".
- 08:77 "Making the debaters more persuasive".
- 09:27 "a stake in the company behind a language model called Claude".
- 10:77 "from 1.33 to 2.636".
- 11:13 "whether he has looked at anything like it in six months" (no product named).
- Part IV epigraph: "Leave the human room to change their mind." replaces the line that recapped
  Chapter 8; both lines stay in the Zen appendix.
- Note on Evidence: OpenAI's reports in Chapters 6, 8 and 12; row 12 says "irrigation association".
- ref-12-flt-tokens gives the six-billion-token figure.

Nothing meaningful was cut: the only removed words are "to Weng's" (07:47) and the product name at
11:13.

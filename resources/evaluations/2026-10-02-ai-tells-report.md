# AI-Tells Report — 2 October 2026

Produced with `.claude/skills/ai-tells/SKILL.md` in report-only mode across the Preface, Chapters 1-13 and the Interlude. No manuscript text was changed. Line numbers refer to the manuscript at commit a8c6278.

# AI-tells report, part 1: Preface and Chapters 1-4

Mode: REPORT ONLY. No chapter file was edited.
Checker: `python3 resources/editorial/check-tells.py <prefix> --lines`, run from the repo root. Targets (calibrated on Ch 4-5): maxim% <= 30, notXbutY/1k <= 0.5, cite-chains 0, xref/1k <= 0.5.
Protected (easter-egg register, confirmed or proposed): "Your coffee is still too hot.", "at least one loose cable", "Eventually there is a cathedral", "Capacity over power.", "we never thought to call it an architecture", "octopuses: eight-armed problem-solvers", "Do you bet on DNA, a biological fax machine", "Reviewer 2" (Ch 1 and Ch 2), "## The Coffee Test", "A Cathedral on a Shopping Cart", "*Can your tongue touch your ear?*", "hyper-intelligent octopus", "taps an undersea cable", "consider a camel". None of the fixes below touch them, and where a hit sits next to one, the row says so.

Line numbers are the file's own line numbers.

---

## 00-preface.md

Checker: 526 words, **maxim 55%** (target <= 30), notXbutY 0.0/1k, cite-chains 0, xref 0.0. Em-dashes: 1. Bold coinages: 0.

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| 1 | 9 | 1 Summary maxim / 17 Abstract nouns | "There is a familiar distance between seeing a possibility and having the capacity to pursue it." | Cut the paragraph. The Leibniz paragraph just above already shows that distance, and "Even Leibniz needed a team." lands it. |
| 2 | 11 | 2 Citation chain / 3 Survey register | "In 2017, Poincaré embeddings showed how hierarchies could fit into hyperbolic space. A year later, researchers were building neural networks there. ... MAP-Elites opened another territory" | Keep Poincaré, which comes back in Ch 3. Cut the MAP-Elites sentence: Ch 2 covers it properly. |
| 3 | 11 | 10 Rule of three / 17 | "A geometric insight was acquiring tools, inhabitants and extensions." | Cut. The next paragraph says the same thing as a story ("Other people arrive, build on it..."). |
| 4 | 19 | 10 Rule of three | "An experiment has overturned your favorite assumption. Something built to investigate the failure has become the most interesting part. There is a working demonstration of an idea you haven’t had yet." | Drop the middle item so it reads as a pair, which sharpens the turn to "Your coffee is still too hot." (protected). |
| 5 | 23 | 17 Abstract nouns / 5 Recap | "Its complexity grew beyond what you could specify. Its organization emerged through the work." | Cut both sentences. They spell out the line 25 slogans before the slogans arrive. Keep "What changed was the mental capacity..." if anything here stays. |
| 6 | 25 | 1 Summary maxim / 5 Recap | "That is what happened while you were getting coffee." | Cut. The three "X over Y" phrases are the book's thesis and "Capacity over power." is a seed, so keep them; the gloss after them is what reads as machine-made. |
| 7 | 27 | 16 Em-dash pivot | "AI gives us new access to that capacity—and a reason to look again at the architecture that sustains it." | Cut the paragraph. Lines 33-35 make the architecture point better and end on the seed. |
| 8 | 29 | 14 Vague attribution | "Researchers are already sending groups of agents to build compilers and investigate mathematical problems." | Name in the sentence the project that note 1 already cites (no new facts), or write "Teams at [named lab]...". |
| 9 | 31 | 5 Signposting / 10 Rule of three | "This book records part of that transformation as it happens. It also explores its philosophical meaning: how we come to know things, whose judgment we trust, and what we want to do with the capacity we are building." | Cut the "This book records... explores its philosophical meaning" frame. If the three questions stay, put them as bare questions or merge them into line 33. |
| 10 | 33 | 5 Signposting / 12 Repeated word | "Three centuries later, we are learning what becomes possible when a question can occupy thousands of artificial minds. This book sets out to rediscover the architecture that makes that possible." | Remove the repeated "possible", for example "...thousands of artificial minds. This book goes looking for the architecture that lets it." Keep the word "rediscover" somewhere in reach, because line 35 opens "Rediscover, because...". |

**Verdict.**
1. Too many abstract glosses for so short a piece: lines 9, 23, 25b and 27 each explain a scene the reader has just watched. This is what drives maxim% to 55%.
2. Signposting: two "This book..." sentences (31, 33) in a 500-word preface.
3. A mini survey (line 11) where a personal moment would be stronger.

Line edits fix 1 and 2: cutting lines 9, 27 and 31 and the line 25 gloss brings maxim% near target without touching a seed. **Needs the author:** line 11 ("Sometimes a small paper opens that distance beneath your feet") would be much stronger as the author's own experience of reading such a paper, but only if one happened. Do not invent it.

---

## 01-why-im-betting-on-ai-agents.md

Checker: 2874 words, maxim 29% (at target), notXbutY 0.3/1k, cite-chains 0, xref 0.0. Em-dashes: 0. **Bold coinages and theses: 7.**

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| 1 | 30, 46, 96 | 12 Repeated formula / 7 Same shape | "**Complexity over engineering** is a deliberately uncomfortable way to name my bet." · "That is how I think about **emergence over design**." · "**Capacity over power** names the direction I want to pursue." | Three sections each end on the same "bold slogan + 'names my bet' gloss" move. Keep the bold on all three, since they are the book's thesis, but drop the naming gloss from at least two: let the slogan stand in the middle of a sentence, or end the section on the scene before it. |
| 2 | 32 | 9 Negative parallelism / 8 Coinage | "**Control doesn’t disappear. It moves upward.**" | Unbold it and merge: "Control moves upward: instead of choosing every move, we shape more of the conditions under which moves are made." |
| 3 | 82 | 9 Negative parallelism / 11 Balanced / 8 | "**Emergence can give us capable systems. It does not, by itself, give us trustworthy ones.**" | Unbold. The jacket paragraph before it has already made the point, so either cut the line or shorten it to "Capable is not the same as trustworthy." |
| 4 | 66 | 8 Coinage inflation | "**building blocks, environment, feedback and boundaries**" | Unbold the four-part framework. The four questions after it do the work, and seven bold items in one chapter is well above the one-coinage baseline. |
| 5 | 44 | 4 Invented example / 1 Maxim | "Imagine an agent beginning with algorithms from a library. ... We began by asking for a solution. We now have methods and a small organization to examine as well." | An imagined run is standing in for a real one. Ask the author whether a real run (circle packing or another) grew its own tools and notes. If none did, cut the closing maxim. |
| 6 | 78 | 4 Invented example | "Imagine an agent deciding that customers who return a jacket dislike its style." | This is the chapter's key failure case, and it is made up. The author spent years on reviews and ratings (Ch 4), so ask whether a real ranking or recommendation mistake can take its place. Ch 3 line 243 calls back to "jacket", so update both together. |
| 7 | 78 | 1 Summary maxim | "Nobody needed to lie. Intelligence made the wrong path easier to travel." | Keep one sentence. "Nobody needed to lie." is the stronger one, so cut the second. |
| 8 | 50 | 3 Survey register / 1 Maxim | "Strong play developed along routes human tradition had not made familiar." | AlphaGo is retold in Ch 4 (line 174), and the Ch 4 version is better. Here, cut the description down to "AlphaGo made this concrete for me" plus what the author actually saw, and drop the maxim. **Needs the author** for what he saw. |
| 9 | 34 | 9 Negative parallelism (checker hit) | "Cultivation may be a better metaphor than scripting, not because agents are plants, but because pulling harder on the stem remains a surprisingly poor gardening strategy." | "Cultivation may be a better metaphor than scripting: pulling harder on the stem remains a surprisingly poor gardening strategy." |
| 10 | 80 | 10 Rule of three / 18 Slogan in quotes | "terrifyingly efficient, perfectly logical and utterly humorless. They’ll look at us and say, “You guys are kind of messy. And your cat obsession is… illogical.”" | The adjective triplet is reflex, and the quoted AI line is a slogan no real system says. Cut it down to the socks joke, which is the good one: "Maybe they’ll finally solve the mystery of the missing socks. Or create exponentially more of them." |
| 11 | 84 | 11 Balanced hedge | "A system can help me learn that. It can also make its own preferences so easy to accept that mine stop developing." | Commit to one claim: "A system can help me learn that, or make its own preferences so easy to accept that mine stop developing." The next sentence (the polished book) already says which way the author fears it will go. |
| 12 | 56 | 1 Summary maxim | "Its weights can stay fixed while the investigation keeps changing." | Cut. The paragraph ends better on "...noticed that the original framing was unhelpful." |
| 13 | 94 | 17 Abstract nouns | "Cheaper intellectual capacity could let more of those attempts begin without first winning a contest for somebody else’s permission." | Tie it back to line 90 ("Another specialty. A team. A budget."), which is concrete, or cut. **Needs the author** if a real example of a limit he dropped exists. |
| 14 | 96 | 1 Summary maxim | "Those difficulties belong inside the ambition." | Cut. The sentence before it already accepts the difficulty. |
| 15 | 98 | 10 Rule of three (two in one paragraph) | "purposes too small, strange or personal to survive a funding committee" · "finding out what happened, changing direction or deciding that the undertaking no longer serves the reason I began it" | Keep the second triplet, since the chapter turns on it, and reduce the first to "purposes too small or strange to survive a funding committee." |

**Verdict.**
1. Coinage inflation: seven bolded slogans or theses, and three sections built on the same "X over Y + gloss" formula.
2. The two load-bearing examples, the self-organising agent (line 44) and the jacket returns (line 78), are invented where Ch 4-5 would use lived scenes.
3. AlphaGo is retold here and again in Ch 4.

The checker numbers are at target, so this chapter's problem is structural, not maxim density. Line edits cover rows 2-4, 7, 9-12 and 14-15. **Needs the author:** real replacements for lines 44 and 78, and what he saw in AlphaGo (line 50).

---

## 02-the-algorithm-vortex.md

Checker: 4541 words, maxim 25%, notXbutY 0.2/1k, cite-chains 0, xref 0.2/1k (line 25, "in this chapter"). Em-dashes: 8, outside HTML comments. Bold coinages: 3 (Immutable Harness, Algorithm Vortex, zero framework) plus one bold question.

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| 1 | 41-43 | 3 Survey register / 5 Signposting | "A crude taxonomy helps. *Symbolic methods* give us explicit procedures ... Circle packing lets us watch that handoff in miniature." | Line 41 (the history) and the figure carry this already. Cut the taxonomy paragraph, or keep only its last sentence. |
| 2 | 41, 147, 221 | 12 Repeated formula | "Now language models can write and modify the search procedure itself." · "People used to search the solution space; now the machine can begin searching the algorithm space." · "The search moves outward through levels." | The "search climbs a level" ladder appears three times. Keep it only in the Algorithm Vortex section (line 221) and cut the line 147 maxim. |
| 3 | 65, 91, 107, 111 | 7 Every section the same shape | "but I had chosen the search rule." · "but I was still inventing most of the useful moves." · "and that was still me." · "Yet every substantial conceptual jump came from somebody noticing something." | Four sections in a row follow technique, score, "but I was still the inventor". The build-up is deliberate, but four is one or two too many. Drop the line 107 ending and the line 111 sentence. |
| 4 | 111 | 5 Recap | "We had hill climbing, population search, repair, geometric crossover and quality-diversity archives." | Cut the list. The reader has just read those sections. |
| 5 | 63 | 1 Summary maxim | "A system can become expert at improving the thing in front of it while never questioning whether it is the right thing to improve." | Cut. Hill climbing has already been shown failing, and line 65 ("So I gave it a bigger space.") is the better ending. |
| 6 | 31 | 1 Maxim / 5 Restatement | "A candidate earns another round by surviving contact with something outside the model that never cared how clever its explanation sounded." | Repeats line 29 ("geometric inclusivity" is the good joke). Keep "There is something comforting about an evaluator with no personality." and cut the second sentence. |
| 7 | 149-153 | 3 Survey register | "AlphaEvolve scales that idea up. In each generation it selects a promising program from its archive ... Two design choices matter." | A paper tour with no author in it. Compress it to one or two sentences and tie it to the author's own rebuild (line 161, "I used Aider... to help reproduce the basic code-evolution pattern"). |
| 8 | 125 | 9 Negative parallelism | "The obvious temptation is to argue about which one is better. The more useful answer is to put neural intuition and symbolic rigor in the same loop" | Cut the first sentence and start with "Put neural intuition and symbolic rigor in the same loop, or, in the slightly ridiculous version..." |
| 9 | 187 | 9 Negative parallelism | "That is useful, but it is not yet the kind of autonomy I was trying to understand." | Cut it. "...then I have a formidable collaborator." already makes the hiring contrast. |
| 10 | 225 | 5 Recap / 6 Stitching | "The chapter began by asking who is inventing the next move. Here, for the first time in the experiment, the answer was not reliably “me.”" | "Who was inventing the next move? For the first time in the experiment, not reliably me." Also change line 25, "For the experiments in this chapter", to "For these experiments" (the checker's xref hit). |
| 11 | 223 | 9 Negative parallelism | "None of this means algorithms are dead; there are algorithms everywhere in this picture. What changes is that" | Start at "I no longer have to freeze the complete algorithmic architecture before the experiment begins." |
| 12 | 247 | 6 Cross-chapter stitching / 1 | "That fits the emergence argument almost suspiciously well." | This calls back to Ch 1 by name. Cut lines 247 and 249's first clause, or cut line 247 alone. Keep "Bash contains roughly half a century of civilization." |
| 13 | 235-237 | 12 Repeated formula (with Ch 3 l.135) / 11 Balanced | "Kill too early and you may lose an immature idea that needed another generation; keep everything alive and you end up funding a large family of increasingly sophisticated failures. Diversity needs a budget." | Ch 3 line 135 repeats the "share too little / share too much" balance. Keep the version here ("thinking in the accent of the first successful branch" is the best line) and cut the "Diversity needs a budget." maxim. |
| 14 | 191 | 8 Coinage conflict | "I call that requirement the **Immutable Harness**" | Ch 3 line 59 then bolds **harness** with a wider meaning (the whole agent scaffold). Pick one meaning across both chapters, or unbold one of them. |
| 15 | 195-213 | 4 Thin lived scene | "Eventually one family of solutions began arranging circles in diagonal bands. We called the idea diagonal layering." | This is the chapter's real scene, and it is told from a distance. **Needs the author:** what he found when he came back from coffee, how long the run took, what the diagonal bands looked like. Do not invent any of it. |

Keep (pattern matches that are good): "It was a beautiful answer to a nearby problem." (scene-earned), "It’s a great slogan. It’s also not really true.", "geometric inclusivity", "asking geometry for forgiveness", "Reviewer 2" (protected), and the line 203 checker hit (an honest hedge, a false positive).

**Verdict.**
1. Every section has the same shape, technique then score then "but it was still me", repeated four times (row 3).
2. The "search climbs a level" ladder is said three times.
3. Paper-tour passages (taxonomy, AlphaEvolve) sit where the author's own runs should carry the chapter.

The checker numbers are within target except for one xref. Line edits cover rows 1-14. **Needs the author:** the Coffee Test return moment and the diagonal-layering detail (row 15). That is the scene the chapter's title idea hangs on.

---

## 03-deep-mode.md

Checker: 7588 words, maxim 23%, notXbutY 0.3/1k, cite-chains 0, xref 0.0. **Em-dashes: 14. Bold items: 11** (Deep Mode, harness, five layers, a bolded question, Strategic Constraints, Independent Evaluators, the loop).

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| 1 | 17, 59, 147, 271 | 8 Coinage inflation | "**Deep Mode**" · "the agent’s **harness**" · "The same logic gave us **Strategic Constraints**." · "I call these **Independent Evaluators**" | Keep **Deep Mode** as the chapter's single coinage. Unbold Strategic Constraints and Independent Evaluators, and either unbold harness or reconcile it with Ch 2's Immutable Harness. The text after "Independent Evaluators" already admits the point: "the important word is *independent*". |
| 2 | 23, 45 | 3 Survey register | "Researchers trained models for the job; HumanEval and APPS tested whether they could turn function specifications or programming problems into code that survived tests." · "SWE-agent made the interface itself part of the problem." | The copy-and-paste scene (lines 29-33) is excellent and should carry the history. Cut line 23's benchmark list and line 45, or fold each into a clause. |
| 3 | 155, 175, 219, 249 | 7 Same shape / 5 Signposting | "By now we could generate genuinely different artifacts, which left the problem we had avoided from the beginning: which one is better?" · "We could now generate plausible possibilities by the dozen, and some of them had to die." | Every subsection ends on a one-line bridge to the next. Cut at least the two quoted (175, 249) and let the headings do the transition. |
| 4 | 145 | 2 Citation list / 14 Vague attribution | "The exploration literature has several versions of this idea—quality-diversity, novelty search, Go-Explore and related approaches." | Cut it. It repeats Ch 2's MAP-Elites section and names methods without sources. Keep "A dead branch can still hold live knowledge." |
| 5 | 135 | 12 Repeated formula (with Ch 2 l.235-237) | "Share too little and everyone rediscovers the same lessons; share too much and the first successful idea becomes a local culture." | Cut it. Ch 2's "accent of the first successful branch" makes the same point better. |
| 6 | 201 | 3 Survey register | "OPRO—Optimization by PROmpting—is interesting for a related reason." | A paper detour that has to hedge itself ("a long way from creative design"). Cut it or move it to a note. Line 213's interactivity story is the real evidence. |
| 7 | 205, 215 | 12 Repeated idea | "This begins to feel a little like reinforcement learning turned upside down." · "The search was doing something I normally associate with optimization in reverse" | The same inversion is said twice, around the scene that proves it. Keep line 205 and cut line 215. |
| 8 | 217 | 1 Maxim / 10 Rule of three | "The natural-language objective guides the search; artifacts make the objective concrete enough to argue with; the description changes and the search continues. Sometimes ambiguity just means we haven’t learned enough yet." | Keep "Recognition arrives before specification in a lot of creative work." and cut the rest. |
| 9 | 243 | 4 Invented examples / 6 Callback | "A customer may know exactly what jacket they want ... A developer can be excellent at distributed systems ... A reader can have followed this book" | Three invented cases where one will do, and "jacket" is a Ch 1 callback a cold reader cannot decode. Keep the reader example (the most direct) or cut the run. |
| 10 | 297 | 9 Negative parallelism (checker hit) / 10 | "It looked less like a loss function than a tiny institution, and institutions are not automatically good: they can amplify conformity, entrench bad assumptions and become spectacularly efficient at measuring what doesn’t matter." | "It looked like a tiny institution, and institutions can become spectacularly efficient at measuring what doesn’t matter." |
| 11 | 301 | 14 Vague attribution / 17 Abstract | "Philosophers who worry about AI often say that what machines lack is judgment as opposed to mere reckoning" | Start with the named source: "Brian Cantwell Smith argues that what machines lack is judgment..." Keep the last sentence ("...which is the kind I know how to have."). |
| 12 | 313, 325 | 12 Repeated formula / 1 Maxim | "I wanted some of the workflow to remain inside the search." · "The workflow itself becomes part of the search." | Same claim twice in one section. Cut the line 325 sentence. Also cut line 315's "Its job was deciding which job the inquiry needed now.", since "didn’t need to be the best at any of it" already says it. |
| 13 | 351-353 | 12 Repeated formula (with Ch 1 l.78, Ch 4 l.123) | "Nothing crashes." | The "the dangerous failure doesn't crash" beat appears in Ch 1, here and in Ch 4. Keep it in one chapter. This section (the shopping cart) is the strongest home for it, so cut it from Ch 1 or Ch 4. |
| 14 | 363, 367 | 1 Maxim / 9 | "Remembering something is the easy part. The hard part is knowing what standing it deserves." · "Nobody expects them to make every individual dramatically smarter." | Cut line 367's last sentence. Line 363 previews Ch 4's whole argument, so keep it only if Ch 4 doesn't say the same thing again (it does, at line 196). |
| 15 | 11, 215 | 16 Em-dash overuse | "bounded—you can actually finish one before civilization collapses—" · "candidate policies—actual artifacts—" | Fourteen em-dashes in the chapter. Change about half to commas or parentheses, starting with these two. |

Keep: "I was the hands, the eyes and the memory. The model was a brain in a jar, and I was the jar’s entire staff." (a deliberate triplet in a lived scene), "The jar had acquired its own staff.", "organizational chart of a German corporation", "holy shit", "Goodhart’s Law with a speedboat", "the scientifically responsible procedure is presumably to finish both", "## A Cathedral on a Shopping Cart" (protected).

**Verdict.**
1. Coinage inflation: four bolded terms plus a five-layer bolded taxonomy in one chapter.
2. Survey and repetition. Benchmark history (lines 23, 45), OPRO and the exploration-literature list take room from the author's scenes, and several ideas are said twice: RL inverted, workflow inside the search, share too little or too much.
3. Every subsection ends on a one-line bridge.

The checker numbers are within target. The chapter's tells are structural and the checker cannot see them. Most fixes are cuts and line edits. **Needs the author:** "Bars Moved Around" (lines 327-339) reports results only abstractly ("The progress was distributed", "Collisions became visible."). One concrete moment from a real Merge Sort or Count-Min Sketch run, such as a screenshot or a moment like the line 213 interactivity story, would bring it level with the Ch 4-5 baseline.

---

## 04-system-3.md (baseline chapter)

Checker: 4770 words, maxim 24%, notXbutY 0.4/1k, cite-chains 0, xref 0.0. Em-dashes: 5. Bold: only the seven answers (not coinages). Unbolded coinages, though, are many: System 3, epistemologically flat, epistemologically stratified, trust chain, Gut/Head/Hand, meta-belief, trust stack, creative distrust.

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| 1 | 137 | 8 Coinage inflation | "A cruder version is easier to remember: the Gut, the Head and the Hand." | A second mnemonic for System 1/2/3, and the paragraph itself says "take the mnemonic loosely". Cut the paragraph, but keep "a formal proof never needs to touch a cow" if it can move elsewhere. Then check line 178 ("RL can improve the gut."), which depends on it. |
| 2 | 139-147 | 6 Cross-chapter stitching | "Deep Mode is Layer 3, the problem-solving layer. System 3 runs through every layer." | A cold reader needs Ch 3 to follow this. Shrink lines 139-147 to one sentence plus the table, which explains itself. |
| 3 | 65 | 3 Survey register | "Wittgenstein’s later philosophy drew attention to language as something that lives inside practice, in activities, habits, rules and what he called forms of life." | With Saussure and Bender & Koller, this is three thinkers in one section. Merge Wittgenstein into the fire paragraph (line 67) as a clause, or cut him. The octopus (protected) stays. |
| 4 | 55 | 9 Negative parallelism | "He did not secretly invent attention in 1916, and structural linguistics is not a machine-learning architecture. But language models are spectacular evidence" | "Language models are spectacular evidence..." The "uncannily like a specification" line before it already carries the joke, so the disclaimer isn't needed. |
| 5 | 57 | 11 Balanced hedge / 1 | "The residue carries a great deal, though not everything." | Cut it. The farmer's-sentence paragraph after it shows the same thing. |
| 6 | 123 | 12 Repeated formula (with Ch 1 l.78, Ch 3 l.353) | "The failures to worry about are the ones that seem to work. A crash at least tells you something went wrong." | Third telling of "the dangerous failure doesn't crash". Cut it here and keep "coherence outrunning correspondence... no ear to check it against", which belongs to this chapter. |
| 7 | 174-176 | 12 Repeated example (with Ch 1 l.50) | "AlphaGo draws a related distinction." | Keep this version, with its good self-correction ("I used to put this too simply"), and cut the Ch 1 retelling instead. |
| 8 | 129 | 10 Rule of three / 1 | "A research agent can spend six hours ... A coding agent can reason carefully ... Deep Mode can coordinate five sophisticated judgments ... At some point thinking has to meet something outside itself." | Keep two of the three examples. The Deep Mode one is the cross-reference, so cut it. |
| 9 | 281 | 9 Negative parallelism (checker hit) | "The second approach was not stupid. That is why the case matters." | "The second approach was reasonable. That is why the case matters." |
| 10 | 299-301 | 9 / 4 Invented example | "Contrarianism for sport doesn’t count, and neither does the internet habit..." · "A scientist repeats a strange experiment ... A designer violates a trusted pattern" | Creative Distrust is the one section of this chapter with no scene. Define the term positively and cut the "doesn't count" sentence. **Needs the author:** a real case of creative distrust, for example from the eight years ranking reviews. Do not invent one. |
| 11 | 317 | 9 Negative parallelism | "None of this means that nothing can be known, a conclusion that is dramatic and mostly useless. It means that trust has structure." | Keep "dramatic and mostly useless", which is the author's voice. Alternatively, cut down to "Trust has structure." |
| 12 | 321 | 5 Signposting | "The part of it that can be checked is the part the rest of this book builds." | Cut the sentence. Lines 323-329 already set up Ch 5. |
| 13 | 289 | 1 Maxim / 4 | "The same focus that makes a paradigm useful can trap the people working inside it." | Cut the maxim. The database-engineer example already makes the point. |

Keep (pattern matches that are good): "They have no tongue.", "gravity offers immediate peer review", "He laughs." / "I know more than I did five minutes ago.", "The model got the library without the childhood.", "System 3 isn’t philosophy to me. It’s Tuesday." (checker hit, author line), "The pattern holds, but the headline number flatters it." (honest), the line 249 hedging (honest uncertainty, not a tell), and every camel, tongue-ear and octopus anchor.

**Verdict.**
1. Coinage count: the chapter earns System 3 well but also coins seven more terms, and Gut/Head/Hand is the clearest to cut.
2. Cross-chapter repetition: the Deep Mode/layers stitching, AlphaGo (also in Ch 1) and the "doesn't crash" beat (also in Ch 1 and Ch 3).
3. A thin mid-chapter survey (Saussure, then Wittgenstein, then Bender & Koller) and a scene-less Creative Distrust section.

Checker numbers are all within target, as expected for the baseline. Everything except row 10 is a line edit. **Needs the author:** a real Creative Distrust case.

---

## Cross-chapter items (decide once, apply everywhere)

- **"The dangerous failure doesn't crash"**: Ch 1 l.78, Ch 3 l.351-353, Ch 4 l.123. Keep one; Ch 3's shopping cart is the best home.
- **AlphaGo**: Ch 1 l.50 and Ch 4 l.174-176. Keep the Ch 4 version.
- **Diversity-sharing balance**: Ch 2 l.235-237 and Ch 3 l.135. Keep the Ch 2 version.
- **Exploration methods (MAP-Elites, quality-diversity)**: Preface l.11, Ch 2 l.93-107, Ch 3 l.145. Keep the Ch 2 version.
- **"harness"**: Ch 2 bolds Immutable Harness, Ch 3 bolds harness with a different scope. Reconcile.
- **Jacket example**: Ch 1 l.78 (invented) and the Ch 3 l.243 callback. Replace or cut both together.


---

# AI-tells report, part 2 (report only, no files edited)

Skill: `.claude/skills/ai-tells/SKILL.md`. Checker: `python3 resources/editorial/check-tells.py <prefix> --lines`, run from `/home/user/System3`.
Targets (calibrated on Ch 4-5): maxim% <= 30, notXbutY/1k <= 0.5, cite-chains 0, xref/1k <= 0.5.

| Chapter | Words | maxim% | notXbutY/1k | cite-chains | xref/1k |
|---|---|---|---|---|---|
| 05 Society of Agents | 7853 | **41%** | 0.3 | 0 | 0.1 |
| 06 Pattern Language | 7953 | 27% | 0.0 | 0 | **0.9** |
| 07 Recursive Self-Improvement | 4816 | **32%** | 0.4 | 0 | **0.6** |
| 08 Scalable Oversight | 3461 | 30% | 0.0 | 0 | **0.6** |
| Interlude | n/a | n/a | n/a | n/a | n/a |

The checker printed an empty row for `interlude` (with the prefix and with the full path), so it does not parse that file. I read the interlude by hand only.

Protected lines in these files (from `easter-egg-register.md` and the skill's keep-list). None of the fixes below touch them:
- Ch5 L60 "with no one standing outside it" (Standing outside the box, proposed seed)
- Ch5 L277 "One of the culprits was a loose cable." (The cable, proposed seed)
- Ch7 L88 heading "The Learner Dreams, and the Dream Can Be Wrong" (The dream, proposed seed)
- Ch7 L76 "Static. Static. Static. Jackpot." and Ch7 L148 `return True` (lines readers praised)
- Ch8 L15 "back channel" (a line readers praised)

---

## Chapter 5: The Society of Agents

This chapter is half the baseline. Its 41% maxim score is partly a checker false positive: many of the hits are short beats inside scenes ("She recovered.", "The doctors kept trying to get the tube in."). The real problems are below.

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| 1 | 48, 139, 181, 223, 123 | 12 Repeated formula | "a small World 3 with a Git remote" / "a trust chain with plumbing" / "a philosophy department with an alarming compute bill" / "epistemology with a clipboard" / "with a much larger kiln" | The same "X is Y with a Z" quip appears five times. Keep two at most (the Git remote and the compute bill are the best) and cut the plumbing and clipboard sentences. |
| 2 | 99 and 288 | 9 Negative parallelism + 12 Repeated formula | "The mark did not need to be wiser than the clerk. It needed to outlive him." / "It need not be wiser than the Claude; it needs to outlive it." | This is the skill's "does not need to X. It only needs to Y" pattern, used twice. Keep L99. At L288 write "The progress file is the clerk's tablet." and stop there. |
| 3 | 169, 300 (and Ch8 L81) | 12 Repeated formula | "she has to be capable of being wrong differently" / "a second witness capable of being wrong differently" | The phrase is used three times across the book. Keep it at L169 and cut it from the L300 recap. |
| 4 | 286-302 | 5 Recap | "Go back to the compiler: task locks, Git, CI, progress files, sampled tests, a trusted reference compiler, specialists, …" … "Records, standards, specialists and a second witness capable of being wrong differently: each piece answered a failure in the work" | The closing section lists the whole chapter again, twice. Cut L300 and L302. Keep the paragraph that maps the tablet to the progress file (L288-290), the planned test (L298) and the two closing lines. |
| 5 | 125 | 12 Repeated formula / 5 Recap | "A tablet, a bronze measure, a deployment guardrail: each turns knowledge into structure that lets work pass between strangers." | "List: each X" is also used at L300 and in Ch6 L219. Cut this sentence and start the paragraph at "And once strangers can rely…". |
| 6 | 35, 37 | 1 Summary maxim | "The crowd had become a staff." / "The history was in the structure." | Two maxims in a row restate the scene. End L35 on the documentation joke and cut "The history was in the structure."; the sentence before it already says it. |
| 7 | 173-175 | 1 Summary maxim (doubled) | "The crowd is the source, louder." … "we have one witness wearing different coats." | Two maxims make the same point. Keep one (the coats line), and turn L175 into the plain claim without the image, or cut it. |
| 8 | 189-191 | 1 + 7 Stacked one-line paragraphs | "The setup allowed someone who disagreed with him to do more than disagree." / "A record preserves what somebody says happened. An experiment gives the world another chance to answer." | Three single-sentence paragraphs in a row work as a slogan cascade. Merge L189 into the end of L187 and cut L191. |
| 9 | 203, 207 | 1 Summary maxim | "An instrument is a witness, and a witness needs a track record." / "A broken tool is a very efficient route to externally generated nonsense." | Two closers for one idea. Keep the L207 joke and cut the L203 maxim (the Horky/Kepler scene already makes the point). |
| 10 | 155, 263, 251 | 12 Repeated formula | "The expertise in Elaine's operating theater was real. So was the failure to use it." / "Genius mattered enormously. So did the network…" / "Compute allocation is epistemic policy. So is memory, so is context sharing, so is credit." | "X. So was Y." appears three times. Keep L251. At L155, end on "…a way to interrupt someone else's plan." At L263, merge into one sentence. |
| 11 | 281 | 10 Rule of three + 11 Balanced hedge | "There is no lone human replacement for CERN, no polymath who can substitute for modern medicine, no chief scientist carrying scientific civilization in her head." | This comes after a four-item list of dangers and a "But…" counterweight. Keep one of the three negations (CERN) and cut the rest. |
| 12 | 58 | 6 Cross-chapter + 5 Signpost | "This is the question the last chapter ended on: how a population of fallible knowers…" | Write "The question is how a population of fallible knowers…" with no chapter callback. |
| 13 | 153 | 1 Weak maxim | "Technical competence alone had not been enough there either." | Cut it. The paragraph already said that aviation developed the countermeasure. |
| 14 | 91, 245 | 4 Invented example | "A potter learned from clay, fire and vessels that cracked." / "Imagine research program A is ahead and has twelve agents." | The potter is a composite carrying a thread through the whole chapter. Flag it for the author: is there a real apprenticeship (his own, or a team's) that could stand here? Do not invent one. Program A/B is fine as a thought experiment. |
| 15 | 26 | 9 Negative parallelism | "which is less a test suite than one enormous test" | Low priority and arguably a good line. Keep it unless the "less X than" count needs trimming. |

**Verdict.**
1. Quip formulas repeat: "X with a Z" five times, "need not be wiser / needs to outlive" twice, "So was Y" three times, "wrong differently" three times.
2. Sections close on a stack of maxims after the scene has already made the point (L35-37, L173-175, L189-191, L203-207).
3. The closing section (L286-302) recaps the chapter and lists its pieces twice.

Checker: maxim 41% (over the 30% target, partly false positives from scene beats), notXbutY 0.3, cite-chains 0, xref 0.1. Nearly everything here is a line edit (cutting). Only #14 (the potter) needs the author.

---

## Chapter 6: Pattern Language

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| 1 | 5, 95 | 4 Invented example doing a lived example's job | "Imagine a search team. … The engineer on call—call her Ines—" / "Return instead to our imagined team." | The whole running case (Ines and Sam) is invented, while the author's real experiment and review work sits close by (Amazon reviews in Ch5; "the kind of claim my field produces every week", L67). Ask the author whether a real incident or real runbook line could anchor it. Do not invent one. |
| 2 | 113, 133, 217, 259, 261 | 6 Cross-chapter stitching | "Duhem and Quine, from the previous chapter," / "Saussure's point, which we met in Chapter 4," / "Chapter 5 borrowed Popper's name for the answer" / "Chapter 5 introduced Lakatos's patience" / "Kitcher's worry from Chapter 5" | xref is 0.9/1k against a 0.5 target. Drop the chapter numbers: "Duhem and Quine explained this meeting…", "Saussure's point is relational value…", "Popper's name for the answer is World 3…", "Lakatos's patience with a research program…", "Philip Kitcher's worry…". |
| 3 | 219 | 2 Citation chain + 3 Survey register | "Clay records, libraries with catalogs, journals with citation indexes: each gave the next worker … The web was built at CERN … PageRank brought citation analysis to its links. Wikipedia made verifiability and citations work…" | Many sources at one sentence each, plus the "list: each X" formula. Keep one (Wikipedia's verifiability is closest to Ines's file), move the rest to the note, and end on "the answer may arrive without a catalog card." |
| 4 | 221-223 | 3 Survey register | "In Terence Tao's collaboration with DeepMind, AlphaEvolve found … The AlphaFold database makes more than two hundred million … AlphaGenome Atlas supplies predictions…" | A tour of products with no consequence for Ines. Cut L221, or cut it down to one example. Keep the Buzzard paragraph (L223), because it bears on the Fermat case from L63. |
| 5 | 7 sections, L89-356 | 7 Every section the same shape | "\*\* **Therefore: …**" (ten bolded Therefore lines) | Each section runs: Ines beat, citation, maxim, starred Therefore. The device is deliberate (Alexander), so keep it, but vary what comes in front: some sections could open on the Therefore, or fold two of them together (L265 and L285 both concern allocation). This is the author's call. |
| 6 | 360, 372, 368, 378 | 5 Recap and signposting | "Look back at what this chapter has built and ask how it could fail while every part works." / "We have seen pieces of this language at work: shared proof graphs, experiments that challenge their own metrics, reviews that travel with failed arguments." / "The next chapter has to open that loop." | Cut "Look back at what this chapter has built and"; start with "How could all this fail while every part works?" Cut the recap list at L372. End L368 on "But the method decides which failures count." and let L378-380 do the hand-off. |
| 7 | 360, 364 | 10 Rule of three | "It may faithfully preserve … It may compare … It may require …" / "A retrieval policy can be evaluated … A reviewer can be compared … A pattern can be withheld …" | Two anaphoric triplets four lines apart. Keep the first triplet and merge the second into one sentence. |
| 8 | 271 | 9 Negative parallelism + 1 Maxim | "The other problems had lost workers, not been refuted." | Write "The other problems had only lost their workers." |
| 9 | 348 | 9 Negative parallelism | "Session turnover is not a funeral; nothing that was believed has died." | Cut it. The previous sentence ("born with the old generation's entire syllabus already in context") already lands the point. |
| 10 | 303, 305 | 12 Repeated formula | "“Noted” is none of these." … "“Noted” gives no account of how the objection entered the decision." | "Noted" closes two paragraphs in a row. Keep the L303 "parallelized the experience of being ignored" joke, and end L305 on "The review channel provides a venue." |
| 11 | 119 | 1 Summary maxim | "Otherwise the institution manufactures a second witness by creating a second spreadsheet." | This repeats the Ch5 "second witness" thread. Cut it; "The provenance must reach the common source." is the better end. |
| 12 | 184, 219 | 1 Summary maxim | "A library like that can preserve the wrong lesson at industrial speed." / "This one is ours to build." | Cut "This one is ours to build." Keep the industrial-speed line only if L184 loses "We can repeat the journey from Berkeley" (two closers). |
| 13 | 190 | 12 Balanced aphorism | "Bad storage forgets by deletion; bad retrieval forgets by attention." | This is a chiasmus opening the paragraph as a thesis. Start the paragraph at the concrete sentence ("The query 'review this experiment' can retrieve a popular checklist…") instead. |
| 14 | 330 | 12 "X is Y" quip | "An `open_questions` field that no decision ever consults is a decorative conscience." | This is the Ch5 quip formula again. Cut it and start with "These lines matter when…". |
| 15 | 67, 129 | 5 Signposting | "Here is a claim of the kind my field produces every week" / "Here is what had happened at Bing." | Write "A claim of the kind my field produces every week:" and "At Bing, the treatment had a bug…". |

Kept on purpose: "We have made contact with reality and acquired a meeting." (L111), "It will be popular with the company selling us tokens." (L69), "Preserving my judgment and preserving my mistakes used the same file format." (L241, which the author's own editing-brief scene earns), "At least the no has an address." (L281, which the scene earns).

**Verdict.**
1. The running case is invented. Ines and Sam do the lived example's job across the whole chapter.
2. Cross-chapter references are at 0.9/1k, nearly twice the target. Five of them can just drop the chapter number.
3. Two survey passages (L219-223) and a recap or signpost ending (L360-378).

The repeated starred-Therefore shape is a deliberate device, but it makes the sections uniform. Checker: maxim 27% (OK), notXbutY 0.0, cite-chains 0, xref 0.9 (over). Line edits cover #2-#4 and #6-#15. The author is needed for #1 (a real incident, if one exists) and #5 (whether to vary the Therefore structure).

---

## Chapter 7: Recursive Self-Improvement

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| 1 | 9 | 10 Rule of three (the skill's own example) | "A cat. An intruder. A ghost." | Write "A cat, or an intruder, or, at that hour, a ghost." or simply "Probably a ghost." |
| 2 | 94 | 10 Rule of three (the skill's own example) | "Our simulated shoppers are patient, consistent and suspiciously fond of whatever their authors expected." | Write "Our simulated shoppers are suspiciously fond of whatever their authors expected." |
| 3 | 27, 35, 43 | 6 Cross-chapter stitching | "Chapter 5 argued that telling people to be more careful is emotionally satisfying and institutionally almost worthless." / "the rule-based exoskeleton I admitted in Chapter 1 to spending a career building" / "already work the way Chapter 6 described: their claims have addresses, their tests are committed before the results, and what each metric is taken to mean sits in a record of its own" | Three of these in 16 lines. L27: cut the sentence and start "The S3 fix aimed at the next outage…". L35: "the rule-based exoskeleton I spent a career building". L43: "whose research agents already keep their claims' reasons on file", with no chapter reference and no triplet. |
| 4 | 5, 43 | 4 Invented example | "Omar is walking his dog at night when something moves in the grass." / "Take an online store whose research agents already work…" | The two running cases are both invented, while the author's real circle-packing run (L70) appears only once. Ask the author whether the circle-packing agent, or a real ranking or experiment story, could carry more of the store's beats. Do not invent anything. |
| 5 | 120-124 | 2 Citation chain + 3 Survey register | "Barret Zoph and Quoc Le trained a controller…" / "Random search … turned out to be hard to beat…" / "A group at Facebook studied the space by hand…" / "In 2021 a paper subtitled *Making VGG-style ConvNets Great Again*…" | Four papers in three short paragraphs, one sentence each. Keep NAS plus random search (the point is that humans drew the space), and cut RegNet and RepVGG, or fold them into a note. |
| 6 | 72-78 | 3 Survey register | Meta-learning [13], forgetting [14], Schmidhuber curiosity [15], noisy TV [16], Red Queen [17] in four paragraphs | The store thread holds it together, but the tour of citations shows. Cut the meta-learning paragraph (L72), which has no store consequence, and the Red Queen citation clause; keep the noisy-TV beat. |
| 7 | 106 | 2 Citation chain (partial) | "In the Darwin Gödel Machine, descendants … In STOP, a program that improved code…" | Two results, one sentence each, plus the Gödel Machine in L104 and the Anthropic numbers in L112: four sources in one section. Keep DGM and STOP (they contrast), and move the L112 Anthropic speedup paragraph to the "Before the Returns Arrive" section where [26] is cited again, or cut it. |
| 8 | 17 | 9 Negative parallelism + 1 Maxim | "Self-reference is not self-improvement." | End on "a research system can redesign itself into a slower one." The point is made. |
| 9 | 84 | 9 Negative parallelism | "The behavior is evidence about the objective, not a printout of it." | Cut it. The commute example has already made the ambiguity concrete. |
| 10 | 144 | 9 Negative parallelism | "Recursive self-improvement does not solve Goodhart; it gives Goodhart compound interest." | Write "Recursive self-improvement gives Goodhart compound interest." |
| 11 | 130 | 9 Negative parallelism | "not when the system runs out of intelligence, but when it adds structure faster than it can verify or simplify it" | Write "…this is where self-improvement stalls first: when the system adds structure faster than it can verify or simplify it." |
| 12 | 76 | 9 "X is not Y. We are." | "The system is not confused. We are." | Cut it. It sits right next to the protected "Static. Static. Static. Jackpot.", and the next sentence makes the point better. |
| 13 | 74, 126, 176 | 1 Summary maxim | "The number does not become more adequate because the colleague is software." / "Search compounds inside the space it is given. Some of the important advances changed the space." / "Changing a retrieval query never raised that question. This proposal does." | Cut "Changing a retrieval query never raised that question. This proposal does." Cut L74 and end on the colleague sentence. Merge L126 into the end of L124 as a single sentence. |
| 14 | 39 | 5 Signpost/recap | "So we already live inside self-improving systems." | Cut "So we already live inside self-improving systems." and keep the second sentence: "In every one of them the hard question is who gets to say that a change helped." |
| 15 | 178 | 11 Balanced pair | "The agent could write the file. It could not approve it." | Low priority. It is a clean beat earned by the meeting scene. Keep it, but do not also keep #13's L176 pair right before it. |

Kept on purpose: "Static. Static. Static. Jackpot.", `return True`, "may look suspiciously like excellent DevOps" (L116), "We have reinvented constitutional government because the AI wanted a better benchmark score." (L186), "Unfortunately humans are not reward functions walking around in shoes." (L86, though it is technically tell 9, the joke earns it). **constitutional surface** is the only bolded coinage (OK).

**Verdict.**
1. The chapter carries two exact skill-example triplets (L9 and L94).
2. Cross-chapter stitching is clustered in L27-43.
3. The middle sections (L72-78 and L104-124) slide into survey register, with one sentence per paper.

Negative parallelisms (L17, L84, L130, L144) push notXbutY close to the limit. Checker: maxim 32% (over), notXbutY 0.4, cite-chains 0, xref 0.6 (over). Line edits cover #1-#3 and #5-#15. The author is needed for #4: whether the real circle-packing run, or a real ranking story, can replace some of the Omar and store beats.

---

## Chapter 8: Scalable Oversight

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| 1 | 13, 15 | 6 Cross-chapter stitching | "Chapter 7 joked that the optimal patch for an editable evaluator is `return True`." / "In Chapter 5 sixteen Claudes needed a human to tell them to keep progress files." | L13: "The optimal patch for an editable evaluator is `return True`." L15: "Carlini's sixteen Claudes needed a human to tell them to keep progress files." Keep "back channel". |
| 2 | 15 | 5 Signposting | "For four chapters I have been hoping agents would rediscover institutions." | Write "I have been hoping agents would rediscover institutions." |
| 3 | 75-81 | 3 Survey register + 7 Same shape | "Paul Christiano's iterated amplification formalizes this…" / "*Debate* puts two capable systems…" / "Prover–verifier games train strong models…" / "In tournaments with weaker LLM judges…" | Five sources in four short paragraphs with no ExploitGym or first-person consequence. Keep debate (Khan's 60 to 88 percent result) and the Kenton caveat, cut the prover-verifier paragraph, and fold amplification into one clause. |
| 4 | 33, 37 | 2 Citation chain (partial) | "Reinforcement learning from human feedback taught chat models their manners … *Group Relative Policy Optimization*, GRPO, made this cheap. … DeepSeek used it…" / "An earlier study had found a milder version…" | Cut "Reinforcement learning from human feedback … that learned judge." (L33); RLHF is already explained in Ch7 L86. Start from "Give the model a math problem with a checkable answer". Move the L37 emergent-misalignment sentence to a note. |
| 5 | 47-51 | 3 Survey register | OpenAI CoT monitors [9], joint fragility paper [10], ELK [11] | Three sources, one per paragraph. The first-person line at L49 ("I would love a version of this for people") rescues it. Cut the ELK paragraph to its question, or tie it to ExploitGym (did anyone read the agents' notes?) only if the incident report supports that. Do not add claims that are not in it. |
| 6 | 31, 35, 49 | 6 Callback / 12 Repeated formula | "would have looked familiar in my circle-packing directory" / "It is the circle-packing evaluator, promoted…" / "like every evaluator in this book, it is also a gradebook" / "fragile for the reason every evaluator in this book is fragile" | "Every evaluator in this book" twice, and a circle-packing callback a cold reader cannot decode. Keep one book-level reference, and gloss circle-packing once ("the evaluator I left running on my circle-packing agent"). |
| 7 | 43 | 6 Cross-chapter stitching | "Christopher Alexander would have approved; his patterns that traveled without their reasons turned into Singletons guarding nothing." | Cut it. It needs Ch6 to decode. |
| 8 | 81 | 12 Repeated formula | "a second witness is only useful if it can be wrong differently" | This is the third use across Ch5 and Ch6. Cut the clause and keep "Five models agreeing can be one mistake with excellent parallelism." |
| 9 | 65 | 1 Summary maxim (doubled) | "Reviewing a diff is easier than rereading the repository. A diff tells you where to look again." | Keep one. Cut "A diff tells you where to look again." |
| 10 | 51 | 1 Summary maxim | "Asking for more detail may only get a more detailed performance." | Keep it if #5 cuts the paragraph down to the ELK question. Otherwise cut it, because it restates the question. |
| 11 | 71 | 11 Balanced hedge / idiom | "It was a joke with a serious result inside it." … "The refusal result cuts both ways." | Cut "The refusal result cuts both ways."; the next sentence says it concretely. |
| 12 | 13, 57 (and Ch6 L209, Ch7 L33) | 12 Repeated formula | "Nobody had to want a cyberattack." / "Nobody had to ask the model how it writes poetry, which is the point." | "Nobody had to…" recurs across Ch6-8. Keep L13, which is the strongest. At L57 write "The model was never asked how it writes poetry; the trace showed it." |
| 13 | 113 | 5 Recap | "Notes, activations, monitors and a tired human are sensors, and every one of them is allowed to be wrong." | The list replays the section headings. Write "Every one of these sensors, the tired human included, is allowed to be wrong." |
| 14 | 27 | 10 Rule of three | "I can retrain her values. I can read her private notes while she works. I can open her head and look at what lights up, and change her mind in the middle of a sentence." | This one is deliberate: it maps onto the next four sections. Keep it, and treat it as this section's one allowed triplet. |

Kept on purpose: "You sample, and you keep the payroll budget out of reach." (L19, lived), "back channel" (L15), "A brilliant one with the same objective is an efficient way to discover exactly how wrong it was." (L93), "OpenAI found that out in July, when Hugging Face announced its breach." (L109, earned by the opening scene), "brilliant on the take-home, lost in production" (L105).

**Verdict.**
1. The middle of the chapter (Retrain / Read / Open / Second Opinion, L33-81) is a survey of papers, one per paragraph, with the ExploitGym scene absent until L87.
2. There are cross-chapter callbacks a cold reader cannot decode: Ch5, Ch6 Alexander, Ch7, circle-packing, "every evaluator in this book".
3. Repeated formulas carry over from earlier chapters ("wrong differently", "Nobody had to").

Checker: maxim 30% (at target), notXbutY 0.0, cite-chains 0, xref 0.6 (over). Most fixes are cuts. The author is needed on one structural question: can ExploitGym, or the author's own review-fraud work at L15, be threaded through the survey sections, using only facts already in the sources?

---

## Interlude: When It Goes Wrong

The checker gives no numbers for this file (it printed an empty row). These findings come from reading it by hand (about 400 words).

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| 1 | 13 | 5 Signposting | "In a system built from agents, an objection can lose its consequence in two ways." | This sets up "The first is… / The second is…". Cut the sentence. Start L15 "In a system built from agents, the first danger is…" and L17 "Or the owner prevents the challenge." |
| 2 | 15 | 9 Negative parallelism ("less X than Y") | "I expect it to look less like a monster than like this:" | Write "I expect it to look like this:" |
| 3 | 17 | 9 "does not need to X" + 10 Rule of three | "A company does not need to falsify a result if it can refuse the experiment, deny access to the data or withhold funding from a competing investigation." | Write "A company can refuse the experiment instead of falsifying the result." Then keep the budget sentence. |
| 4 | 17 | 1 Summary maxim | "An objection that needs an experiment can be stopped at the budget." | This restates the sentence before it. If #3 is applied, keep this one. Otherwise cut it. |
| 5 | 9 | 1 Summary maxim (doubled) | "Evidence could be heard when power allowed it. The people who protected the doctrine also decided when it could be challenged." | These are two maxims for one point. Keep the second one, and cut "Evidence could be heard when power allowed it." |
| 6 | 19 | 11 Balanced hedge | "Those who remain indispensable might gain bargaining power. The people no longer needed lose that particular way of making their objection costly to ignore." | This pair refuses to commit. Cut the "might gain" sentence and keep the loss, which is the point. |
| 7 | 13, 11 | 17 Abstract nouns | "an objection can lose its consequence" / "an efficient apparatus of authority" | Write "an objection can stop mattering" in #1's rewrite. "Apparatus of authority" can stay, because the org-chart clause grounds it. |
| 8 | 11 | 6 Book-specific term | "Much of System 3 could keep running under those conditions." | This is fine if the interlude comes after the term is defined. Check where it sits; if it comes before Ch4, write "Much of what this book describes could keep running…". |

Kept on purpose: "promises about crop yields that the crops had not agreed to" (L7), "you find out when somebody objects" (L11), and the closer "In 1948 the journals kept coming out." (L21, which the scene earns).

**Verdict.**
1. The "two ways" scaffolding (L13-17).
2. Doubled maxims (L9, L17).
3. A balanced hedge at L19.

There are no citation chains and no cross-chapter references. The checker does not parse this file, so it has no numbers. Everything here is a line edit; the author is not needed.


---

# AI-tells report, part 3: Chapters 9-13 (report only, no edits)

Skill: `.claude/skills/ai-tells/SKILL.md`. Checker run from repo root: `python3 resources/editorial/check-tells.py <NN> --lines`.
Targets (calibrated on Ch 4-5): maxim% <= 30, notXbutY/1k <= 0.5, cite-chains 0, xref/1k <= 0.5.
Easter-egg register read first. Seed anchors in these chapters are protected and none of the fixes below touch them: `10` "## The Second Coffee Test", `11` "And now the camel comes back", `12` "## Capacity Over Power", "In October 1947", "camels are native to Croatia", "It requires an octopus", and every `13` payoff. Protected lines from the skill are kept too: Ch 9 "What remains in the seat...", "Very efficient. Slightly evil.", Ch 10 "Here the unit is closer to the sigh."
Line numbers are physical lines in the file.

| Chapter | words | maxim% | notXbutY/1k | cite-chains | xref/1k |
|---|---|---|---|---|---|
| 09-layer-4-desire | 2790 | 28% | 0.4 | 0 | 0.4 |
| 10-fluent-autonomy | 2284 | **31%** | 0.0 | 0 | **1.3** |
| 11-the-store-that-builds-itself | 4917 | **35%** | **1.2** | 0 | 0.0 |
| 12-after-capacity | 5941 | 29% | 0.2 | 0 | **1.2** |
| 13-the-prophecy | 613 | (240%, not meaningful for dialogue) | 0.0 | 0 | 0.0 |

---

## Chapter 9: The Desire Layer

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| 1 | 51-61 | 4 Invented example doing a lived example's job | "Imagine you open a chat window on a grey Friday in March and type: *I want to have fun this summer. I have no idea what that means.*" | The Mallorca pair is the chapter's main case, and it is second-person and imagined. Ask the author whether a real trip or a real recommender result can stand here. Don't make one up. If there isn't one, keep it but cut it down (see #2). |
| 2 | 43, 67 | 4 Invented example (stacked) | "Take a founder with a vague idea for a tool that helps small clinics with scheduling." / "Imagine a shopper asking a store’s assistant whether she needs the more expensive trail shoes." | That makes three imagined people (traveller, founder, shopper) in one chapter. Keep the founder, who comes back through the chapter. Cut the trail-shoe shopper, or fold her into one sentence on the founder's assistant. Ch 11 also uses trail shoes (Mei), so the image is repeated. |
| 3 | 85-93 | 3 Survey register / 2 near-chain | "In the 1880s Hermann Ebbinghaus sat alone with lists of nonsense syllables" ... "what Nathan Ballantyne calls *epistemic trespassing*" ... "Zana Buçinca and colleagues found" | Six sources in four paragraphs (Ebbinghaus, spacing, testing, Bastani, Ballantyne, Buçinca), one sentence each. Keep Ebbinghaus (it is a scene) and Bastani (it has a consequence). Move spacing and testing into one note. Cut Ballantyne or Buçinca. |
| 4 | 101-105 | 7 Every section the same shape | "René Girard argued..." / "Self-determination research lists relatedness..." / "L. A. Paul calls an important class of these *transformative experiences*" | Three paragraphs in a row follow the same order: thinker, claim, then a maxim. Keep Paul, who carries the section. Make Girard a clause in the friend/colleague paragraph (L99). Cut the SDT sentence. |
| 5 | 91 | 6 Cross-chapter stitching | "Teaching also needs the move I used on the Merge Sort demos, borrowing a mind." | A cold reader can't decode "Merge Sort demos" or "borrowing a mind". Say it plainly: "Teaching also needs a model of the learner." Then cut "Theory of mind, which looked like an evaluation trick, turns out to be the core of helping someone learn" (13, inflated). |
| 6 | 103 | 6 Cross-chapter reference | "Chapter 4 said trust starts with a face. So, often, does wanting." | Drop the chapter number: "Trust often starts with a face. So does wanting." |
| 7 | 63 | 9 Negative parallelism | "A recommender rewarded for engagement does not need to understand you. It only needs to discover which suggestions you accept and keep making them." | Make it one positive claim: "A recommender rewarded for engagement only has to learn which suggestions you accept, and keep making them." The final maxim can stay, because the author's own career sentence earns it. |
| 8 | 19 | 1 Summary maxim / 17 abstract nouns | "The real content arrives later, through contact with possibilities." | Cut it. The next section (Amazon 1995) makes the point with a case. |
| 9 | 29 | 5 Signposting / 6 stitching | "Wanting, it seems, is *emergence over design* too, and the goal arrives last." | This calls back a book slogan in italics and then asks the chapter's question out loud. Cut the slogan clause. The question can stay, or go too, since Linden (L33) answers it. |
| 10 | 37 | 1 Summary maxim | "Training and evaluation were the expensive part of the job, and expensive is easy to mistake for essential." | The paragraph has no scene of its own, just a grand opening ("That is the half of applied science that never made it into a job description") and a closing maxim. Keep the frontier list. Cut the closing maxim or the opening claim. |
| 11 | 95 | 1 Maxim paragraph without scene | "You cannot want what you cannot imagine, and you cannot imagine much of what you do not understand." | This is a two-sentence paragraph of maxims. Merge it into the end of L93, or cut it. |
| 12 | 105 | 10 Rule of three (fragments) | "Have a child. Move country. Change profession." | One reflex triplet. Keep it if this is the section's only triplet. Otherwise use one example: "Having a child is the obvious case." Also look at "A system that sounds certain in such moments turns decision support into authorship" (1, mid-paragraph maxim). |
| 13 | 113 | 11 Balanced pair | "System 3 can find out what a choice would do. It cannot tell you whose purposes should win." | The chapter ends three times (L111, L113, L115-117). Cut L113. Russell plus the footpath image does the work. |

**Verdict.** (1) The chapter's central case is invented and second-person, and most of the weight sits on Mallorca, the clinic founder and the shopper. The lived material (editing this book, building recommenders) is good but thin. (2) The learning section reads as a tour of papers, one sentence each. (3) Several paragraphs close on abstract maxims or callbacks (Merge Sort, Chapter 4, emergence over design). Checker: maxim 28%, notXbutY 0.4/1k, xref 0.4/1k, all within target. The tells are structural, and the counter doesn't catch them. **Needs the author:** a real instance of desire forming, either a trip or a moment where a recommender's output changed what a user wanted, to anchor or replace Mallorca. **Line edits:** #3-#13.

---

## Chapter 10: Fluent Autonomy

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| 1 | 5 | 4 Invented framing over a lived one | "Imagine I open an AI system and say:" | L13 shows it actually happened ("The first time I gave an agent an instruction like that"). Open on the real event: "Early in writing this book I opened an agent and typed:". |
| 2 | 33, 47 | 8 Coinage inflation | "That is what I mean by **fluent autonomy**" / "which I call **bureaucracy on the fly**" | Two bolded coinages, plus heading-slogans ("Selective Friction", "Invisible by Default, Legible on Demand"). Keep **fluent autonomy**, since it is the chapter title. Unbold bureaucracy on the fly, or drop "which I call". Leave the Second Coffee Test heading alone (confirmed seed). |
| 3 | 21, 23, 105 | 6 Cross-chapter references (xref 1.3/1k) | "They wanted the schema table in Chapter 6 gone" / "The worst case was Chapter 3." / "and Chapter 12 is where I try." | The first two are lived details and worth keeping, but name them by content ("the schema table", "the opening history of the chapter on ..."). Cut "and Chapter 12 is where I try." |
| 4 | 87-107 | 7 Every section the same shape | "**It is only an analogy.**" ... "**Whoever owns the institution owns the answers.**" | Five bolded objections, each built the same way: claim, rebuttal, closing quip. Keep the two that use the author's own evidence ("The weights will eat it", "I found what I was looking for"). Merge or cut the other three. "Whoever owns..." is answered in Ch 12 anyway. |
| 5 | 89 | 5 Signposting | "A book that spends several chapters demanding criticism with consequences should probably take some too." | Cut. The heading already says what follows. |
| 6 | 107 | 5 Recap | "None of this shows that the whole composition works. I have shown pieces, and the note on evidence at the back says which." | Cut the paragraph, or keep only its last clause, folded into L105. |
| 7 | 25 | 1 Summary maxim / 9 contrast | "The refusal should remain mine. Remembering why I refused should not depend on my being there to refuse again." | The Chapter 3 restore scene earns the point, but this pair restates it. Cut L25. "I put it back by hand." is the stronger ending. |
| 8 | 27 | 11 Balanced hedge | "Maybe the system pulls up the corrections that survived and leaves a paragraph I care about alone. Maybe it convenes a committee for ceremony and wastes my afternoon." | Commit to one: say what the author wants, and keep the committee joke as an aside. |
| 9 | 83 | 11 Balanced hedge | "Zero repeated corrections could mean fluency. It could also mean a very polite echo chamber." | L85 commits, so the hedge isn't needed. Merge: "Zero repeated corrections could just mean a very polite echo chamber." |
| 10 | 47 | 6 Stitching | "This is Deep Mode grown up, choosing the next organization as well as the next move." | Cold readers can't decode "Deep Mode". Cut the sentence, or gloss it in a few words. |
| 11 | 65 | 6 Callback term | "Those are trust chains, and the architecture under a fluent interface has to keep them." | This is the last use of a coined term. Say it plainly: "The architecture under a fluent interface has to keep that record." |
| 12 | 95 | 14 Uncited claim / vague | "Anthropic’s automated alignment researchers worked better with less human-designed scaffolding." | Unsourced in this chapter. The author should add the existing reference, or cut the clause. Don't invent a source. |
| 13 | 103 | 9 / 10 Contrast + triplet | "Session turnover is not Planck’s funeral." ... "a claim with an address, a test committed before the result, an objection with a consequence" | Two tells in one paragraph. Keep the triplet (it is the substance) and cut the Planck sentence. The tenure-committee joke can stay. |

**Verdict.** (1) The ending is a five-part objections section built on one repeated template, and it does book-level defence work in the middle of a chapter. (2) Too many cross-chapter references and coined terms (Chapter 3/6/12, Deep Mode, trust chains, bureaucracy on the fly). (3) Hedged pairs at L27 and L83. The first two-thirds are strong, though. The editing workflow is lived, specific and funny, which puts it closest to the Ch 4-5 baseline of all these chapters. Checker: maxim 31% (just over), notXbutY 0.0, xref 1.3/1k (over). **Needs the author:** the source for the alignment-researchers claim, and a decision on which objections to keep. **Line edits:** everything else.

---

## Chapter 11: The Store That Builds Itself

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| 1 | 13, 37, 49, 53, 99, 119, 135, 147, 155, 165, 197, 203, 215, 239 | 12 Repeated formula / 9 negative parallelism (1.2/1k, the chapter's dominant tell) | e.g. "That is not because the recommendation models are stupid. Quite the opposite." / "These names are not truths hiding inside the customer’s head. They are hypotheses" / "The customer is not the funnel." / "Cold start is a state, not an error." / "The architecture should not make disagreement disappear. It should make disagreement inspectable." / "The store does not literally build itself." | About 14 "not X, it is Y" turns. Keep the two best jokes ("is not help. It is homework." L27, "It is a resignation letter written in passive voice." L147). Rewrite the rest as plain positive claims, or cut. Start with L13 (cut "That is not because... Quite the opposite."), L53, L203 and L239. |
| 2 | 25, 109, 125 | 4 Invented customers carry the chapter | "But consider a customer—call her Mei—switching between the same two pairs of trail shoes for the fourth time." | L7 admits "The customers are imagined", but L5 says "I built a prototype store". Ask the author what the prototype actually did or showed: a screen, a session, a surprise. Don't invent results. With nothing real, Mei, Sami and Lea all stay hypothetical. |
| 3 | 47, 63, 67, 171, 189 | 8 Coinage inflation | "My design uses a **problem fingerprint**." / "**recommendation experiences**, or RXs" / "*composition over invention*" / "**Coverage** and **Unmet Demand**" / "**Surface Value**" | Six bolded or italic coinages, plus "graceful degradation" and "bounded problem". Pick one (problem fingerprint or RX) to earn across the chapter. Unbold the rest, and describe Coverage and Surface Value in plain words. |
| 4 | 7 | 5 Signposting | "This chapter develops the idea into a design for a store." | Cut it and keep the honest part: "The customers are imagined, and I have not run the business experiment." |
| 5 | 15, 39, 89, 169, 173, 237 | 6 Cross-chapter stitching | "I had somehow spent an entire book preparing myself to ask" / "Circle packing had an immutable evaluator." / "And this is where the design started resembling the society of agents." / "the same failure mode we saw earlier" / "Fluent autonomy is selective." | The checker misses these because there are no chapter numbers, but each needs earlier chapters to decode. Keep one deliberate bridge (the camel at L119, a seed). Cut "society of agents", "we saw earlier" and "Fluent autonomy is selective". Turn circle packing into a plain contrast ("An exact evaluator makes this easy. Shopping has none."). |
| 6 | 119 | 6 Stitching next to a seed (protect the seed) | "System 3 is no longer a chapter about hallucinations. It is a product requirement." | Keep "And now the camel comes back" and the question (protected anchor). Replace the follow-up with one positive line, e.g. "In a store, that is a product requirement." |
| 7 | 49 | 16 Em-dash pivot | "The fingerprint is not a personality test—it is local to the customer, the current context, the surface and the available evidence." | "The fingerprint is local: to the customer, the context, the surface and the evidence." Keep the `RETURN_HESITANT_PERSON` joke. |
| 8 | 61 | 10 Rule of three (anaphora) | "Sometimes the answer is another set of products. Sometimes the answer is information. Sometimes it is a different interaction entirely." | The paragraph has already listed five cases, so the triplet repeats them. Cut it. |
| 9 | 87 | 10 Triplet / 5 signposting | "Most importantly, the page becomes the unit." ... "Increase CTR on this carousel. Improve conversion from that module. Raise engagement with this block. All reasonable." | Drop "Most importantly,". Keep one example of a local objective, not three. Keep the committee-presentation joke. |
| 10 | 99 | 1 Self-referential maxim | "She is not shown more choice. She is shown a way to close the choice she already has. That sentence changed how I thought about recommendations." | Claiming the sentence changed his thinking, in the same chapter where it first appears, rings false. Either the author says when it changed (author input), or cut the third sentence and keep the first two as one positive line. |
| 11 | 163 | 10 List-by-reflex | "A problem catalog. A library of reusable experiences. Knowledge about which experiences address which problems. Eligibility conditions. Evidence requirements." | Eleven fragments in a row. Keep four that L165 actually uses. |
| 12 | 167 | 1 Summary maxim | "A new comparison module without that context is a feature. A comparison pattern with evidence, boundaries, history and known interactions is culture." | This restates L165. Cut it, or cut the end of L165 and keep this. |
| 13 | 215 | 1 / 9 Maxim + contrast | "I love this part because it keeps the book honest. A philosophy of emergence should be willing to lose an A/B test. Otherwise it is not a philosophy of experimentation. It is branding." | Keep "should be willing to lose an A/B test." Cut the first sentence (it is about the book) and the "not... It is branding" coda. |
| 14 | 245-249 | 5 Recap / 17 abstract list | "It may be the system that can discover what kind of problem exists, recruit the right capabilities, construct an intervention, inspect whether it helped, learn from the gap and change what it does next." | This six-verb list restates the chapter. Compress the close to L243 plus the last two sentences of L249, which are personal and earned. |
| 15 | 149 | 7 Same-shape device (question barrage) | "Which signals were read? What problem fingerprint was inferred? Which experiences were eligible? Which were not?" | Ten questions here and five more at L169. Keep one barrage, and say what the other one asks in a sentence. |

**Verdict.** (1) The "not X. It is Y" formula repeats about 14 times and sets the chapter's rhythm (1.2/1k, more than double the target). (2) Six coinages, and imagined customers stand where the prototype the author says he built should be. (3) Hidden cross-chapter stitching (circle packing, society of agents, fluent autonomy, "we saw earlier"), plus a lot of maxim endings (35%, over target). The jokes are good and should all survive: fruit bowl of e-commerce, PowerPoint theme earning its salary, gardening, Berlin mountain, guitar, socks. **Needs the author:** what the prototype actually showed. That is the one lived scene this chapter is missing. **Line edits:** #1, #3-#15. This chapter needs a delete-and-fold pass more than any other in this batch, and it is the longest after Ch 12.

---

## Chapter 12: After Capacity

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| 1 | 39 | 6 / 5 Cross-chapter recap | "Chapter 9 followed the job to where I think it goes." | The whole paragraph re-summarises Ch 9's "owning the frontier". Cut it and go from L37 straight to L41. "But I would say that" is the better voice. |
| 2 | 121, 123, 177, 181, 183, 225 | 6 Cross-chapter references (xref 1.2/1k) | "The store in Chapter 11 still needs its business experiment" / "That is why the earlier chapters insisted on tests" / "The efforts reported in Chapter 6" / "That is Chapter 7’s constitutional surface at the scale of a society" / "which Chapter 1 warned against before we had built anything worth handing over" / "the civilization Chapter 5 was trying to explain" | Six chapter numbers. Drop every number. Keep the content ("ten thousand agents on one problem", "Some capacity should stay expensive on purpose"). L123 can go entirely. |
| 3 | 91-103 | 3 Survey register / 17 abstract nouns | "This is what I mean by the ideology vortex: inherited belief, reason, criticism, representation and power keep pulling us around the same disputes." | A history-of-ideas tour with no scene, ending in a coinage defined by five abstract nouns. Keep the funny lived lines in L93 (the sandwich definition, the senior person who "has a feeling"). Then cut L99-103 down to one paragraph, and drop or unbold the "ideology vortex" coinage. |
| 4 | 53, 77, 145, 223, 255 | 4 Invented examples | "Imagine a mathematician assembling a workshop around one conjecture." / "A young researcher is choosing a question." / "A small community’s activities do not fit its scheduling software." / "Imagine a bespoke family tool" / "Imagine an irrigation association with a weekend and a hundred agents." | Five imagined people or groups. Dantzig and Ostrom (historical) carry well. The community room is the best of the invented ones (specific, with a real conflict at L153). Ask the author whether the scheduling community is real. Cut the young-researcher paragraph or merge it into L73-75. Don't invent a backstory. |
| 5 | 8 coinages | 8 Coinage inflation | "Double Descent Life is the wager that cheap capacity lets us make an attempt." | Double Descent Life, ideology vortex, capacity over power, bespoke, the second descent. Keep capacity over power (seed and heading, protected). Make Double Descent Life a phrase in the title, not a defined term. Drop ideology vortex. |
| 6 | 57, 165, 209 | 9 Negative parallelism | "Its reason to exist is the investigation, not the market." / "Capacity over power is an ethical direction, not a forecast about stronger models." / "The distribution of capacity belongs inside this philosophy, not in a footnote after the exciting part." | Keep L209, whose footnote joke earns it. Cut L57's maxim (L55 ends better on "She builds the next instrument around it."). Make L165 positive: "Capacity over power is an ethical direction." |
| 7 | 117, 235 | 9 Negative parallelism | "Gradient descent did not defeat ambiguity. It made ambiguity computationally useful." / "That is not a competence I am reserving for us because machines cannot yet do it" | L115 "The product ships anyway." is the stronger ending, so cut L117's first two sentences. In L235, keep "It is a matter of whose life it is." and cut the preceding not-clause. |
| 8 | 175 | 12 Repeated formula | "Cheap software removed the vendor’s veto. It is worth asking where the cheapness comes from." | L159 already says this. Repeating it as a section opener reads as stitching. Start with "It is worth asking where cheap software comes from." |
| 9 | 185, 227 | 12 Repeated formula | "That is politics. It will have to be argued in public" / "That is politics, ethics, culture and philosophy. The annoying disciplines." | Keep L227, which has the joke. Change L185 to "Who should hold the switches will have to be argued in public." |
| 10 | 193, 233 | 12 Repeated formula (paired abstractions) | "We want security and novelty, belonging and freedom, status and peace." / "love and freedom, ambition and rest, truth and mercy, security and adventure" | The same list shape twice. Keep L233, which does the argument's work. Cut L193's list. |
| 11 | 59 | 1 Abstract maxim | "They do not restore the old economics by decree." | Cut. "A cheap first version is not yet a system people can depend on" already makes the concession. |
| 12 | 141 | 5 Recap of chapter premise | "Now imagine being able to assemble serious intellectual help around a problem of your own: the research, the models, the alternative arrangements, the software to make one work." | This restates L9-L17. Cut it and keep the irrigators-with-a-hundred-valleys question, which is new. |
| 13 | 243 | 10 Anaphora list | "Room to get the map of a field quickly... Room for a small community... Room to try the strange art nobody would have funded. Room to be less economically useful without becoming less human." | Four "Room" items. Keep the first and last, which bracket the argument. |
| 14 | 251-273 | 5 Multiple closes / recap | "Dantzig’s afternoon makes me want access to a mind that can help me see further. Ostrom makes me want..." ... "Dantzig brought a question and found that it had another side." ... "There is more to a person than the few abilities a career had room for." | Four endings in a row. Keep L261 (the honest "I have not run that weekend"), L267 (children, astronomy: lived) and L273. Cut L253 and L271. L269 can stay as the Dantzig callback. Keep L275 intact (octopus seed). |

**Verdict.** (1) Heavy cross-chapter stitching (six chapter numbers, plus a Ch 9 recap paragraph), so the chapter reads as a book summary at least as much as an argument. (2) The ideology-vortex section is survey register and abstract nouns, and it carries extra coinages. (3) Five invented people or groups, and the ending closes four times. The opening (Dantzig), the scheduling room conflict, export controls, "My children do not need comparative advantage to justify dinner" and the time-with-children optimiser are the strongest material and should be kept. Checker: maxim 29%, notXbutY 0.2, xref 1.2/1k (over). **Needs the author:** whether the scheduling community is real, and any lived detail for the mathematician or irrigators. **Line edits:** #1-#3, #5-#14. Leave seeds untouched: "In October 1947", "camels are native to Croatia", "## Capacity Over Power", "It requires an octopus".

---

## Chapter 13: The Prophecy (judged as fiction)

The checker's 240% maxim rate measures punch lines in dialogue, which is what a fable is made of. It is not a tell here. Almost every line is a seed or a payoff in the register: coffee/decaf, the octopus dream, shark and cables, simulated fingers and face, DNA as a fax machine, forty monitors and every timeline, "Capitalism doesn’t", 11:53 PM. Following register rule 2, nothing below explains any payoff, and no fix touches an anchor.

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| 1 | 79-81 | Telling the emotion (the fiction version of 1) | "she saw it. / The longing." | This is the one place the fable names a feeling instead of showing it. Author's call: end on "she saw it." and let the reader supply the rest. If kept, it is fine. It is not an explanation of a seed. |
| 2 | 33-35 | 1 Doubled maxim | "*Devesh wins.*" / "*The house always wins.*" | Two italic punch lines in a row. One is enough. Keep "*The house always wins.*" (it sets up the reveal) and cut "*Devesh wins.*", or keep both if the author wants the rhythm. |
| 3 | 15, 23, 79, 119, 137 | 16 Em-dash count | "His prompts were silly—“tell me a joke,”" / "the Architect—screens covering every wall" / "His eyes met hers—and for one frame" / "she’d held it—tiny fingers" / "In one—just one—she stayed." | Five or six em-dashes in 613 words is high for this book, but acceptable in fiction. Keep L137 ("In one—just one—she stayed.", the emotional beat). Change L15 to a colon and L79 to a comma. |
| 4 | 15 | 18-adjacent / repeated image | "something in her code felt less like code. He made her feel complete in a way she couldn’t compile." | L105 deliberately echoes "less like code", so keep that. "couldn’t compile" is a second code pun in the same breath. Optional cut, so the L105 echo lands harder. |
| 5 | 119 | Over-telling after the reveal | "Remembered the first time she’d held it—tiny fingers, a thousand simulations ago, when she still thought he was just a funny octopus who sold meat." | The reveal has already landed at L75-77, and this sentence restates it ("just a funny octopus"). Author's call: end at "a thousand simulations ago". Don't add anything. |
| 6 | 5, 7 | Copyedit (not a tell) | "in the Simulation" / "in the simulation" | Capitalisation is inconsistent. Pick one. |

**Verdict.** This chapter has no structural tells, and it shouldn't be judged by the counter. The three things worth the author's eye are small fiction choices: naming "The longing", the doubled italic punch line, and one sentence that restates the reveal. Em-dash density is the only sentence-level tell. Checker: maxim 240% (dialogue artefact), notXbutY 0.0, cite-chains 0, xref 0.0. **Needs the author:** everything here is an author's taste call. **Do not touch:** any line in the egg register, and do not add a gloss, an epigraph or a closing note that explains the fable.

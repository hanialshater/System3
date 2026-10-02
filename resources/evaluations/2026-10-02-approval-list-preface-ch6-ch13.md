# Approval list — Preface, Chapters 1–6, Chapter 13

Proposed AI-tells fixes for the chapters you asked to approve yourself. None of these files has been edited.
Every row has an ID (P-3 = Preface row 3, C4-7 = Chapter 4 row 7, X-2 = cross-chapter item 2, C13-1 = Chapter 13 row 1).
Line numbers match the manuscript as it is now.

**How to reply:** for example, "approve all except C1-6, C4-2; C13: approve 2, 3, 6". Rows marked *Needs the author* wait for your material, and nothing will be invented for them.

Ch13 rule: no fix explains a payoff, and every row there is a taste call.

## 00-preface.md

Checker: 526 words, **maxim 55%** (target <= 30), notXbutY 0.0/1k, cite-chains 0, xref 0.0. Em-dashes: 1. Bold coinages: 0.

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| P-1 | 9 | 1 Summary maxim / 17 Abstract nouns | "There is a familiar distance between seeing a possibility and having the capacity to pursue it." | Cut the paragraph. The Leibniz paragraph just above already shows that distance, and "Even Leibniz needed a team." lands it. |
| P-2 | 11 | 2 Citation chain / 3 Survey register | "In 2017, Poincaré embeddings showed how hierarchies could fit into hyperbolic space. A year later, researchers were building neural networks there. ... MAP-Elites opened another territory" | Keep Poincaré, which comes back in Ch 3. Cut the MAP-Elites sentence: Ch 2 covers it properly. |
| P-3 | 11 | 10 Rule of three / 17 | "A geometric insight was acquiring tools, inhabitants and extensions." | Cut. The next paragraph says the same thing as a story ("Other people arrive, build on it..."). |
| P-4 | 19 | 10 Rule of three | "An experiment has overturned your favorite assumption. Something built to investigate the failure has become the most interesting part. There is a working demonstration of an idea you haven’t had yet." | Drop the middle item so it reads as a pair, which sharpens the turn to "Your coffee is still too hot." (protected). |
| P-5 | 23 | 17 Abstract nouns / 5 Recap | "Its complexity grew beyond what you could specify. Its organization emerged through the work." | Cut both sentences. They spell out the line 25 slogans before the slogans arrive. Keep "What changed was the mental capacity..." if anything here stays. |
| P-6 | 25 | 1 Summary maxim / 5 Recap | "That is what happened while you were getting coffee." | Cut. The three "X over Y" phrases are the book's thesis and "Capacity over power." is a seed, so keep them; the gloss after them is what reads as machine-made. |
| P-7 | 27 | 16 Em-dash pivot | "AI gives us new access to that capacity—and a reason to look again at the architecture that sustains it." | Cut the paragraph. Lines 33-35 make the architecture point better and end on the seed. |
| P-8 | 29 | 14 Vague attribution | "Researchers are already sending groups of agents to build compilers and investigate mathematical problems." | Name in the sentence the project that note 1 already cites (no new facts), or write "Teams at [named lab]...". |
| P-9 | 31 | 5 Signposting / 10 Rule of three | "This book records part of that transformation as it happens. It also explores its philosophical meaning: how we come to know things, whose judgment we trust, and what we want to do with the capacity we are building." | Cut the "This book records... explores its philosophical meaning" frame. If the three questions stay, put them as bare questions or merge them into line 33. |
| P-10 | 33 | 5 Signposting / 12 Repeated word | "Three centuries later, we are learning what becomes possible when a question can occupy thousands of artificial minds. This book sets out to rediscover the architecture that makes that possible." | Remove the repeated "possible", for example "...thousands of artificial minds. This book goes looking for the architecture that lets it." Keep the word "rediscover" somewhere in reach, because line 35 opens "Rediscover, because...". |

**Verdict.**
1. Too many abstract glosses for so short a piece: lines 9, 23, 25b and 27 each explain a scene the reader has just watched. This is what drives maxim% to 55%.
2. Signposting: two "This book..." sentences (31, 33) in a 500-word preface.
3. A mini survey (line 11) where a personal moment would be stronger.

Line edits fix 1 and 2: cutting lines 9, 27 and 31 and the line 25 gloss brings maxim% near target without touching a seed. **Needs the author:** line 11 ("Sometimes a small paper opens that distance beneath your feet") would be much stronger as the author's own experience of reading such a paper, but only if one happened. Do not invent it.

---


---

## 01-why-im-betting-on-ai-agents.md

Checker: 2874 words, maxim 29% (at target), notXbutY 0.3/1k, cite-chains 0, xref 0.0. Em-dashes: 0. **Bold coinages and theses: 7.**

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| C1-1 | 30, 46, 96 | 12 Repeated formula / 7 Same shape | "**Complexity over engineering** is a deliberately uncomfortable way to name my bet." · "That is how I think about **emergence over design**." · "**Capacity over power** names the direction I want to pursue." | Three sections each end on the same "bold slogan + 'names my bet' gloss" move. Keep the bold on all three, since they are the book's thesis, but drop the naming gloss from at least two: let the slogan stand in the middle of a sentence, or end the section on the scene before it. |
| C1-2 | 32 | 9 Negative parallelism / 8 Coinage | "**Control doesn’t disappear. It moves upward.**" | Unbold it and merge: "Control moves upward: instead of choosing every move, we shape more of the conditions under which moves are made." |
| C1-3 | 82 | 9 Negative parallelism / 11 Balanced / 8 | "**Emergence can give us capable systems. It does not, by itself, give us trustworthy ones.**" | Unbold. The jacket paragraph before it has already made the point, so either cut the line or shorten it to "Capable is not the same as trustworthy." |
| C1-4 | 66 | 8 Coinage inflation | "**building blocks, environment, feedback and boundaries**" | Unbold the four-part framework. The four questions after it do the work, and seven bold items in one chapter is well above the one-coinage baseline. |
| C1-5 | 44 | 4 Invented example / 1 Maxim | "Imagine an agent beginning with algorithms from a library. ... We began by asking for a solution. We now have methods and a small organization to examine as well." | An imagined run is standing in for a real one. Ask the author whether a real run (circle packing or another) grew its own tools and notes. If none did, cut the closing maxim. |
| C1-6 | 78 | 4 Invented example | "Imagine an agent deciding that customers who return a jacket dislike its style." | This is the chapter's key failure case, and it is made up. The author spent years on reviews and ratings (Ch 4), so ask whether a real ranking or recommendation mistake can take its place. Ch 3 line 243 calls back to "jacket", so update both together. |
| C1-7 | 78 | 1 Summary maxim | "Nobody needed to lie. Intelligence made the wrong path easier to travel." | Keep one sentence. "Nobody needed to lie." is the stronger one, so cut the second. |
| C1-8 | 50 | 3 Survey register / 1 Maxim | "Strong play developed along routes human tradition had not made familiar." | AlphaGo is retold in Ch 4 (line 174), and the Ch 4 version is better. Here, cut the description down to "AlphaGo made this concrete for me" plus what the author actually saw, and drop the maxim. **Needs the author** for what he saw. |
| C1-9 | 34 | 9 Negative parallelism (checker hit) | "Cultivation may be a better metaphor than scripting, not because agents are plants, but because pulling harder on the stem remains a surprisingly poor gardening strategy." | "Cultivation may be a better metaphor than scripting: pulling harder on the stem remains a surprisingly poor gardening strategy." |
| C1-10 | 80 | 10 Rule of three / 18 Slogan in quotes | "terrifyingly efficient, perfectly logical and utterly humorless. They’ll look at us and say, “You guys are kind of messy. And your cat obsession is… illogical.”" | The adjective triplet is reflex, and the quoted AI line is a slogan no real system says. Cut it down to the socks joke, which is the good one: "Maybe they’ll finally solve the mystery of the missing socks. Or create exponentially more of them." |
| C1-11 | 84 | 11 Balanced hedge | "A system can help me learn that. It can also make its own preferences so easy to accept that mine stop developing." | Commit to one claim: "A system can help me learn that, or make its own preferences so easy to accept that mine stop developing." The next sentence (the polished book) already says which way the author fears it will go. |
| C1-12 | 56 | 1 Summary maxim | "Its weights can stay fixed while the investigation keeps changing." | Cut. The paragraph ends better on "...noticed that the original framing was unhelpful." |
| C1-13 | 94 | 17 Abstract nouns | "Cheaper intellectual capacity could let more of those attempts begin without first winning a contest for somebody else’s permission." | Tie it back to line 90 ("Another specialty. A team. A budget."), which is concrete, or cut. **Needs the author** if a real example of a limit he dropped exists. |
| C1-14 | 96 | 1 Summary maxim | "Those difficulties belong inside the ambition." | Cut. The sentence before it already accepts the difficulty. |
| C1-15 | 98 | 10 Rule of three (two in one paragraph) | "purposes too small, strange or personal to survive a funding committee" · "finding out what happened, changing direction or deciding that the undertaking no longer serves the reason I began it" | Keep the second triplet, since the chapter turns on it, and reduce the first to "purposes too small or strange to survive a funding committee." |

**Verdict.**
1. Coinage inflation: seven bolded slogans or theses, and three sections built on the same "X over Y + gloss" formula.
2. The two load-bearing examples, the self-organising agent (line 44) and the jacket returns (line 78), are invented where Ch 4-5 would use lived scenes.
3. AlphaGo is retold here and again in Ch 4.

The checker numbers are at target, so this chapter's problem is structural, not maxim density. Line edits cover rows 2-4, 7, 9-12 and 14-15. **Needs the author:** real replacements for lines 44 and 78, and what he saw in AlphaGo (line 50).

---


---

## 02-the-algorithm-vortex.md

Checker: 4541 words, maxim 25%, notXbutY 0.2/1k, cite-chains 0, xref 0.2/1k (line 25, "in this chapter"). Em-dashes: 8, outside HTML comments. Bold coinages: 3 (Immutable Harness, Algorithm Vortex, zero framework) plus one bold question.

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| C2-1 | 41-43 | 3 Survey register / 5 Signposting | "A crude taxonomy helps. *Symbolic methods* give us explicit procedures ... Circle packing lets us watch that handoff in miniature." | Line 41 (the history) and the figure carry this already. Cut the taxonomy paragraph, or keep only its last sentence. |
| C2-2 | 41, 147, 221 | 12 Repeated formula | "Now language models can write and modify the search procedure itself." · "People used to search the solution space; now the machine can begin searching the algorithm space." · "The search moves outward through levels." | The "search climbs a level" ladder appears three times. Keep it only in the Algorithm Vortex section (line 221) and cut the line 147 maxim. |
| C2-3 | 65, 91, 107, 111 | 7 Every section the same shape | "but I had chosen the search rule." · "but I was still inventing most of the useful moves." · "and that was still me." · "Yet every substantial conceptual jump came from somebody noticing something." | Four sections in a row follow technique, score, "but I was still the inventor". The build-up is deliberate, but four is one or two too many. Drop the line 107 ending and the line 111 sentence. |
| C2-4 | 111 | 5 Recap | "We had hill climbing, population search, repair, geometric crossover and quality-diversity archives." | Cut the list. The reader has just read those sections. |
| C2-5 | 63 | 1 Summary maxim | "A system can become expert at improving the thing in front of it while never questioning whether it is the right thing to improve." | Cut. Hill climbing has already been shown failing, and line 65 ("So I gave it a bigger space.") is the better ending. |
| C2-6 | 31 | 1 Maxim / 5 Restatement | "A candidate earns another round by surviving contact with something outside the model that never cared how clever its explanation sounded." | Repeats line 29 ("geometric inclusivity" is the good joke). Keep "There is something comforting about an evaluator with no personality." and cut the second sentence. |
| C2-7 | 149-153 | 3 Survey register | "AlphaEvolve scales that idea up. In each generation it selects a promising program from its archive ... Two design choices matter." | A paper tour with no author in it. Compress it to one or two sentences and tie it to the author's own rebuild (line 161, "I used Aider... to help reproduce the basic code-evolution pattern"). |
| C2-8 | 125 | 9 Negative parallelism | "The obvious temptation is to argue about which one is better. The more useful answer is to put neural intuition and symbolic rigor in the same loop" | Cut the first sentence and start with "Put neural intuition and symbolic rigor in the same loop, or, in the slightly ridiculous version..." |
| C2-9 | 187 | 9 Negative parallelism | "That is useful, but it is not yet the kind of autonomy I was trying to understand." | Cut it. "...then I have a formidable collaborator." already makes the hiring contrast. |
| C2-10 | 225 | 5 Recap / 6 Stitching | "The chapter began by asking who is inventing the next move. Here, for the first time in the experiment, the answer was not reliably “me.”" | "Who was inventing the next move? For the first time in the experiment, not reliably me." Also change line 25, "For the experiments in this chapter", to "For these experiments" (the checker's xref hit). |
| C2-11 | 223 | 9 Negative parallelism | "None of this means algorithms are dead; there are algorithms everywhere in this picture. What changes is that" | Start at "I no longer have to freeze the complete algorithmic architecture before the experiment begins." |
| C2-12 | 247 | 6 Cross-chapter stitching / 1 | "That fits the emergence argument almost suspiciously well." | This calls back to Ch 1 by name. Cut lines 247 and 249's first clause, or cut line 247 alone. Keep "Bash contains roughly half a century of civilization." |
| C2-13 | 235-237 | 12 Repeated formula (with Ch 3 l.135) / 11 Balanced | "Kill too early and you may lose an immature idea that needed another generation; keep everything alive and you end up funding a large family of increasingly sophisticated failures. Diversity needs a budget." | Ch 3 line 135 repeats the "share too little / share too much" balance. Keep the version here ("thinking in the accent of the first successful branch" is the best line) and cut the "Diversity needs a budget." maxim. |
| C2-14 | 191 | 8 Coinage conflict | "I call that requirement the **Immutable Harness**" | Ch 3 line 59 then bolds **harness** with a wider meaning (the whole agent scaffold). Pick one meaning across both chapters, or unbold one of them. |
| C2-15 | 195-213 | 4 Thin lived scene | "Eventually one family of solutions began arranging circles in diagonal bands. We called the idea diagonal layering." | This is the chapter's real scene, and it is told from a distance. **Needs the author:** what he found when he came back from coffee, how long the run took, what the diagonal bands looked like. Do not invent any of it. |

Keep (pattern matches that are good): "It was a beautiful answer to a nearby problem." (scene-earned), "It’s a great slogan. It’s also not really true.", "geometric inclusivity", "asking geometry for forgiveness", "Reviewer 2" (protected), and the line 203 checker hit (an honest hedge, a false positive).

**Verdict.**
1. Every section has the same shape, technique then score then "but it was still me", repeated four times (row 3).
2. The "search climbs a level" ladder is said three times.
3. Paper-tour passages (taxonomy, AlphaEvolve) sit where the author's own runs should carry the chapter.

The checker numbers are within target except for one xref. Line edits cover rows 1-14. **Needs the author:** the Coffee Test return moment and the diagonal-layering detail (row 15). That is the scene the chapter's title idea hangs on.

---


---

## 03-deep-mode.md

Checker: 7588 words, maxim 23%, notXbutY 0.3/1k, cite-chains 0, xref 0.0. **Em-dashes: 14. Bold items: 11** (Deep Mode, harness, five layers, a bolded question, Strategic Constraints, Independent Evaluators, the loop).

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| C3-1 | 17, 59, 147, 271 | 8 Coinage inflation | "**Deep Mode**" · "the agent’s **harness**" · "The same logic gave us **Strategic Constraints**." · "I call these **Independent Evaluators**" | Keep **Deep Mode** as the chapter's single coinage. Unbold Strategic Constraints and Independent Evaluators, and either unbold harness or reconcile it with Ch 2's Immutable Harness. The text after "Independent Evaluators" already admits the point: "the important word is *independent*". |
| C3-2 | 23, 45 | 3 Survey register | "Researchers trained models for the job; HumanEval and APPS tested whether they could turn function specifications or programming problems into code that survived tests." · "SWE-agent made the interface itself part of the problem." | The copy-and-paste scene (lines 29-33) is excellent and should carry the history. Cut line 23's benchmark list and line 45, or fold each into a clause. |
| C3-3 | 155, 175, 219, 249 | 7 Same shape / 5 Signposting | "By now we could generate genuinely different artifacts, which left the problem we had avoided from the beginning: which one is better?" · "We could now generate plausible possibilities by the dozen, and some of them had to die." | Every subsection ends on a one-line bridge to the next. Cut at least the two quoted (175, 249) and let the headings do the transition. |
| C3-4 | 145 | 2 Citation list / 14 Vague attribution | "The exploration literature has several versions of this idea—quality-diversity, novelty search, Go-Explore and related approaches." | Cut it. It repeats Ch 2's MAP-Elites section and names methods without sources. Keep "A dead branch can still hold live knowledge." |
| C3-5 | 135 | 12 Repeated formula (with Ch 2 l.235-237) | "Share too little and everyone rediscovers the same lessons; share too much and the first successful idea becomes a local culture." | Cut it. Ch 2's "accent of the first successful branch" makes the same point better. |
| C3-6 | 201 | 3 Survey register | "OPRO—Optimization by PROmpting—is interesting for a related reason." | A paper detour that has to hedge itself ("a long way from creative design"). Cut it or move it to a note. Line 213's interactivity story is the real evidence. |
| C3-7 | 205, 215 | 12 Repeated idea | "This begins to feel a little like reinforcement learning turned upside down." · "The search was doing something I normally associate with optimization in reverse" | The same inversion is said twice, around the scene that proves it. Keep line 205 and cut line 215. |
| C3-8 | 217 | 1 Maxim / 10 Rule of three | "The natural-language objective guides the search; artifacts make the objective concrete enough to argue with; the description changes and the search continues. Sometimes ambiguity just means we haven’t learned enough yet." | Keep "Recognition arrives before specification in a lot of creative work." and cut the rest. |
| C3-9 | 243 | 4 Invented examples / 6 Callback | "A customer may know exactly what jacket they want ... A developer can be excellent at distributed systems ... A reader can have followed this book" | Three invented cases where one will do, and "jacket" is a Ch 1 callback a cold reader cannot decode. Keep the reader example (the most direct) or cut the run. |
| C3-10 | 297 | 9 Negative parallelism (checker hit) / 10 | "It looked less like a loss function than a tiny institution, and institutions are not automatically good: they can amplify conformity, entrench bad assumptions and become spectacularly efficient at measuring what doesn’t matter." | "It looked like a tiny institution, and institutions can become spectacularly efficient at measuring what doesn’t matter." |
| C3-11 | 301 | 14 Vague attribution / 17 Abstract | "Philosophers who worry about AI often say that what machines lack is judgment as opposed to mere reckoning" | Start with the named source: "Brian Cantwell Smith argues that what machines lack is judgment..." Keep the last sentence ("...which is the kind I know how to have."). |
| C3-12 | 313, 325 | 12 Repeated formula / 1 Maxim | "I wanted some of the workflow to remain inside the search." · "The workflow itself becomes part of the search." | Same claim twice in one section. Cut the line 325 sentence. Also cut line 315's "Its job was deciding which job the inquiry needed now.", since "didn’t need to be the best at any of it" already says it. |
| C3-13 | 351-353 | 12 Repeated formula (with Ch 1 l.78, Ch 4 l.123) | "Nothing crashes." | The "the dangerous failure doesn't crash" beat appears in Ch 1, here and in Ch 4. Keep it in one chapter. This section (the shopping cart) is the strongest home for it, so cut it from Ch 1 or Ch 4. |
| C3-14 | 363, 367 | 1 Maxim / 9 | "Remembering something is the easy part. The hard part is knowing what standing it deserves." · "Nobody expects them to make every individual dramatically smarter." | Cut line 367's last sentence. Line 363 previews Ch 4's whole argument, so keep it only if Ch 4 doesn't say the same thing again (it does, at line 196). |
| C3-15 | 11, 215 | 16 Em-dash overuse | "bounded—you can actually finish one before civilization collapses—" · "candidate policies—actual artifacts—" | Fourteen em-dashes in the chapter. Change about half to commas or parentheses, starting with these two. |

Keep: "I was the hands, the eyes and the memory. The model was a brain in a jar, and I was the jar’s entire staff." (a deliberate triplet in a lived scene), "The jar had acquired its own staff.", "organizational chart of a German corporation", "holy shit", "Goodhart’s Law with a speedboat", "the scientifically responsible procedure is presumably to finish both", "## A Cathedral on a Shopping Cart" (protected).

**Verdict.**
1. Coinage inflation: four bolded terms plus a five-layer bolded taxonomy in one chapter.
2. Survey and repetition. Benchmark history (lines 23, 45), OPRO and the exploration-literature list take room from the author's scenes, and several ideas are said twice: RL inverted, workflow inside the search, share too little or too much.
3. Every subsection ends on a one-line bridge.

The checker numbers are within target. The chapter's tells are structural and the checker cannot see them. Most fixes are cuts and line edits. **Needs the author:** "Bars Moved Around" (lines 327-339) reports results only abstractly ("The progress was distributed", "Collisions became visible."). One concrete moment from a real Merge Sort or Count-Min Sketch run, such as a screenshot or a moment like the line 213 interactivity story, would bring it level with the Ch 4-5 baseline.

---


---

## 04-system-3.md (baseline chapter)

Checker: 4770 words, maxim 24%, notXbutY 0.4/1k, cite-chains 0, xref 0.0. Em-dashes: 5. Bold: only the seven answers (not coinages). Unbolded coinages, though, are many: System 3, epistemologically flat, epistemologically stratified, trust chain, Gut/Head/Hand, meta-belief, trust stack, creative distrust.

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| C4-1 | 137 | 8 Coinage inflation | "A cruder version is easier to remember: the Gut, the Head and the Hand." | A second mnemonic for System 1/2/3, and the paragraph itself says "take the mnemonic loosely". Cut the paragraph, but keep "a formal proof never needs to touch a cow" if it can move elsewhere. Then check line 178 ("RL can improve the gut."), which depends on it. |
| C4-2 | 139-147 | 6 Cross-chapter stitching | "Deep Mode is Layer 3, the problem-solving layer. System 3 runs through every layer." | A cold reader needs Ch 3 to follow this. Shrink lines 139-147 to one sentence plus the table, which explains itself. |
| C4-3 | 65 | 3 Survey register | "Wittgenstein’s later philosophy drew attention to language as something that lives inside practice, in activities, habits, rules and what he called forms of life." | With Saussure and Bender & Koller, this is three thinkers in one section. Merge Wittgenstein into the fire paragraph (line 67) as a clause, or cut him. The octopus (protected) stays. |
| C4-4 | 55 | 9 Negative parallelism | "He did not secretly invent attention in 1916, and structural linguistics is not a machine-learning architecture. But language models are spectacular evidence" | "Language models are spectacular evidence..." The "uncannily like a specification" line before it already carries the joke, so the disclaimer isn't needed. |
| C4-5 | 57 | 11 Balanced hedge / 1 | "The residue carries a great deal, though not everything." | Cut it. The farmer's-sentence paragraph after it shows the same thing. |
| C4-6 | 123 | 12 Repeated formula (with Ch 1 l.78, Ch 3 l.353) | "The failures to worry about are the ones that seem to work. A crash at least tells you something went wrong." | Third telling of "the dangerous failure doesn't crash". Cut it here and keep "coherence outrunning correspondence... no ear to check it against", which belongs to this chapter. |
| C4-7 | 174-176 | 12 Repeated example (with Ch 1 l.50) | "AlphaGo draws a related distinction." | Keep this version, with its good self-correction ("I used to put this too simply"), and cut the Ch 1 retelling instead. |
| C4-8 | 129 | 10 Rule of three / 1 | "A research agent can spend six hours ... A coding agent can reason carefully ... Deep Mode can coordinate five sophisticated judgments ... At some point thinking has to meet something outside itself." | Keep two of the three examples. The Deep Mode one is the cross-reference, so cut it. |
| C4-9 | 281 | 9 Negative parallelism (checker hit) | "The second approach was not stupid. That is why the case matters." | "The second approach was reasonable. That is why the case matters." |
| C4-10 | 299-301 | 9 / 4 Invented example | "Contrarianism for sport doesn’t count, and neither does the internet habit..." · "A scientist repeats a strange experiment ... A designer violates a trusted pattern" | Creative Distrust is the one section of this chapter with no scene. Define the term positively and cut the "doesn't count" sentence. **Needs the author:** a real case of creative distrust, for example from the eight years ranking reviews. Do not invent one. |
| C4-11 | 317 | 9 Negative parallelism | "None of this means that nothing can be known, a conclusion that is dramatic and mostly useless. It means that trust has structure." | Keep "dramatic and mostly useless", which is the author's voice. Alternatively, cut down to "Trust has structure." |
| C4-12 | 321 | 5 Signposting | "The part of it that can be checked is the part the rest of this book builds." | Cut the sentence. Lines 323-329 already set up Ch 5. |
| C4-13 | 289 | 1 Maxim / 4 | "The same focus that makes a paradigm useful can trap the people working inside it." | Cut the maxim. The database-engineer example already makes the point. |

Keep (pattern matches that are good): "They have no tongue.", "gravity offers immediate peer review", "He laughs." / "I know more than I did five minutes ago.", "The model got the library without the childhood.", "System 3 isn’t philosophy to me. It’s Tuesday." (checker hit, author line), "The pattern holds, but the headline number flatters it." (honest), the line 249 hedging (honest uncertainty, not a tell), and every camel, tongue-ear and octopus anchor.

**Verdict.**
1. Coinage count: the chapter earns System 3 well but also coins seven more terms, and Gut/Head/Hand is the clearest to cut.
2. Cross-chapter repetition: the Deep Mode/layers stitching, AlphaGo (also in Ch 1) and the "doesn't crash" beat (also in Ch 1 and Ch 3).
3. A thin mid-chapter survey (Saussure, then Wittgenstein, then Bender & Koller) and a scene-less Creative Distrust section.

Checker numbers are all within target, as expected for the baseline. Everything except row 10 is a line edit. **Needs the author:** a real Creative Distrust case.

---


---

## Cross-chapter items (decide once, apply everywhere)

- **X-1** **"The dangerous failure doesn't crash"**: Ch 1 l.78, Ch 3 l.351-353, Ch 4 l.123. Keep one; Ch 3's shopping cart is the best home.
- **X-2** **AlphaGo**: Ch 1 l.50 and Ch 4 l.174-176. Keep the Ch 4 version.
- **X-3** **Diversity-sharing balance**: Ch 2 l.235-237 and Ch 3 l.135. Keep the Ch 2 version.
- **X-4** **Exploration methods (MAP-Elites, quality-diversity)**: Preface l.11, Ch 2 l.93-107, Ch 3 l.145. Keep the Ch 2 version.
- **X-5** **"harness"**: Ch 2 bolds Immutable Harness, Ch 3 bolds harness with a different scope. Reconcile.
- **X-6** **Jacket example**: Ch 1 l.78 (invented) and the Ch 3 l.243 callback. Replace or cut both together.



---

## Chapter 5: The Society of Agents

This chapter is half the baseline. Its 41% maxim score is partly a checker false positive: many of the hits are short beats inside scenes ("She recovered.", "The doctors kept trying to get the tube in."). The real problems are below.

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| C5-1 | 48, 139, 181, 223, 123 | 12 Repeated formula | "a small World 3 with a Git remote" / "a trust chain with plumbing" / "a philosophy department with an alarming compute bill" / "epistemology with a clipboard" / "with a much larger kiln" | The same "X is Y with a Z" quip appears five times. Keep two at most (the Git remote and the compute bill are the best) and cut the plumbing and clipboard sentences. |
| C5-2 | 99 and 288 | 9 Negative parallelism + 12 Repeated formula | "The mark did not need to be wiser than the clerk. It needed to outlive him." / "It need not be wiser than the Claude; it needs to outlive it." | This is the skill's "does not need to X. It only needs to Y" pattern, used twice. Keep L99. At L288 write "The progress file is the clerk's tablet." and stop there. |
| C5-3 | 169, 300 (and Ch8 L81) | 12 Repeated formula | "she has to be capable of being wrong differently" / "a second witness capable of being wrong differently" | The phrase is used three times across the book. Keep it at L169 and cut it from the L300 recap. |
| C5-4 | 286-302 | 5 Recap | "Go back to the compiler: task locks, Git, CI, progress files, sampled tests, a trusted reference compiler, specialists, …" … "Records, standards, specialists and a second witness capable of being wrong differently: each piece answered a failure in the work" | The closing section lists the whole chapter again, twice. Cut L300 and L302. Keep the paragraph that maps the tablet to the progress file (L288-290), the planned test (L298) and the two closing lines. |
| C5-5 | 125 | 12 Repeated formula / 5 Recap | "A tablet, a bronze measure, a deployment guardrail: each turns knowledge into structure that lets work pass between strangers." | "List: each X" is also used at L300 and in Ch6 L219. Cut this sentence and start the paragraph at "And once strangers can rely…". |
| C5-6 | 35, 37 | 1 Summary maxim | "The crowd had become a staff." / "The history was in the structure." | Two maxims in a row restate the scene. End L35 on the documentation joke and cut "The history was in the structure."; the sentence before it already says it. |
| C5-7 | 173-175 | 1 Summary maxim (doubled) | "The crowd is the source, louder." … "we have one witness wearing different coats." | Two maxims make the same point. Keep one (the coats line), and turn L175 into the plain claim without the image, or cut it. |
| C5-8 | 189-191 | 1 + 7 Stacked one-line paragraphs | "The setup allowed someone who disagreed with him to do more than disagree." / "A record preserves what somebody says happened. An experiment gives the world another chance to answer." | Three single-sentence paragraphs in a row work as a slogan cascade. Merge L189 into the end of L187 and cut L191. |
| C5-9 | 203, 207 | 1 Summary maxim | "An instrument is a witness, and a witness needs a track record." / "A broken tool is a very efficient route to externally generated nonsense." | Two closers for one idea. Keep the L207 joke and cut the L203 maxim (the Horky/Kepler scene already makes the point). |
| C5-10 | 155, 263, 251 | 12 Repeated formula | "The expertise in Elaine's operating theater was real. So was the failure to use it." / "Genius mattered enormously. So did the network…" / "Compute allocation is epistemic policy. So is memory, so is context sharing, so is credit." | "X. So was Y." appears three times. Keep L251. At L155, end on "…a way to interrupt someone else's plan." At L263, merge into one sentence. |
| C5-11 | 281 | 10 Rule of three + 11 Balanced hedge | "There is no lone human replacement for CERN, no polymath who can substitute for modern medicine, no chief scientist carrying scientific civilization in her head." | This comes after a four-item list of dangers and a "But…" counterweight. Keep one of the three negations (CERN) and cut the rest. |
| C5-12 | 58 | 6 Cross-chapter + 5 Signpost | "This is the question the last chapter ended on: how a population of fallible knowers…" | Write "The question is how a population of fallible knowers…" with no chapter callback. |
| C5-13 | 153 | 1 Weak maxim | "Technical competence alone had not been enough there either." | Cut it. The paragraph already said that aviation developed the countermeasure. |
| C5-14 | 91, 245 | 4 Invented example | "A potter learned from clay, fire and vessels that cracked." / "Imagine research program A is ahead and has twelve agents." | The potter is a composite carrying a thread through the whole chapter. Flag it for the author: is there a real apprenticeship (his own, or a team's) that could stand here? Do not invent one. Program A/B is fine as a thought experiment. |
| C5-15 | 26 | 9 Negative parallelism | "which is less a test suite than one enormous test" | Low priority and arguably a good line. Keep it unless the "less X than" count needs trimming. |

**Verdict.**
1. Quip formulas repeat: "X with a Z" five times, "need not be wiser / needs to outlive" twice, "So was Y" three times, "wrong differently" three times.
2. Sections close on a stack of maxims after the scene has already made the point (L35-37, L173-175, L189-191, L203-207).
3. The closing section (L286-302) recaps the chapter and lists its pieces twice.

Checker: maxim 41% (over the 30% target, partly false positives from scene beats), notXbutY 0.3, cite-chains 0, xref 0.1. Nearly everything here is a line edit (cutting). Only #14 (the potter) needs the author.

---


---

## Chapter 6: Pattern Language

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| C6-1 | 5, 95 | 4 Invented example doing a lived example's job | "Imagine a search team. … The engineer on call—call her Ines—" / "Return instead to our imagined team." | The whole running case (Ines and Sam) is invented, while the author's real experiment and review work sits close by (Amazon reviews in Ch5; "the kind of claim my field produces every week", L67). Ask the author whether a real incident or real runbook line could anchor it. Do not invent one. |
| C6-2 | 113, 133, 217, 259, 261 | 6 Cross-chapter stitching | "Duhem and Quine, from the previous chapter," / "Saussure's point, which we met in Chapter 4," / "Chapter 5 borrowed Popper's name for the answer" / "Chapter 5 introduced Lakatos's patience" / "Kitcher's worry from Chapter 5" | xref is 0.9/1k against a 0.5 target. Drop the chapter numbers: "Duhem and Quine explained this meeting…", "Saussure's point is relational value…", "Popper's name for the answer is World 3…", "Lakatos's patience with a research program…", "Philip Kitcher's worry…". |
| C6-3 | 219 | 2 Citation chain + 3 Survey register | "Clay records, libraries with catalogs, journals with citation indexes: each gave the next worker … The web was built at CERN … PageRank brought citation analysis to its links. Wikipedia made verifiability and citations work…" | Many sources at one sentence each, plus the "list: each X" formula. Keep one (Wikipedia's verifiability is closest to Ines's file), move the rest to the note, and end on "the answer may arrive without a catalog card." |
| C6-4 | 221-223 | 3 Survey register | "In Terence Tao's collaboration with DeepMind, AlphaEvolve found … The AlphaFold database makes more than two hundred million … AlphaGenome Atlas supplies predictions…" | A tour of products with no consequence for Ines. Cut L221, or cut it down to one example. Keep the Buzzard paragraph (L223), because it bears on the Fermat case from L63. |
| C6-5 | 7 sections, L89-356 | 7 Every section the same shape | "\*\* **Therefore: …**" (ten bolded Therefore lines) | Each section runs: Ines beat, citation, maxim, starred Therefore. The device is deliberate (Alexander), so keep it, but vary what comes in front: some sections could open on the Therefore, or fold two of them together (L265 and L285 both concern allocation). This is the author's call. |
| C6-6 | 360, 372, 368, 378 | 5 Recap and signposting | "Look back at what this chapter has built and ask how it could fail while every part works." / "We have seen pieces of this language at work: shared proof graphs, experiments that challenge their own metrics, reviews that travel with failed arguments." / "The next chapter has to open that loop." | Cut "Look back at what this chapter has built and"; start with "How could all this fail while every part works?" Cut the recap list at L372. End L368 on "But the method decides which failures count." and let L378-380 do the hand-off. |
| C6-7 | 360, 364 | 10 Rule of three | "It may faithfully preserve … It may compare … It may require …" / "A retrieval policy can be evaluated … A reviewer can be compared … A pattern can be withheld …" | Two anaphoric triplets four lines apart. Keep the first triplet and merge the second into one sentence. |
| C6-8 | 271 | 9 Negative parallelism + 1 Maxim | "The other problems had lost workers, not been refuted." | Write "The other problems had only lost their workers." |
| C6-9 | 348 | 9 Negative parallelism | "Session turnover is not a funeral; nothing that was believed has died." | Cut it. The previous sentence ("born with the old generation's entire syllabus already in context") already lands the point. |
| C6-10 | 303, 305 | 12 Repeated formula | "“Noted” is none of these." … "“Noted” gives no account of how the objection entered the decision." | "Noted" closes two paragraphs in a row. Keep the L303 "parallelized the experience of being ignored" joke, and end L305 on "The review channel provides a venue." |
| C6-11 | 119 | 1 Summary maxim | "Otherwise the institution manufactures a second witness by creating a second spreadsheet." | This repeats the Ch5 "second witness" thread. Cut it; "The provenance must reach the common source." is the better end. |
| C6-12 | 184, 219 | 1 Summary maxim | "A library like that can preserve the wrong lesson at industrial speed." / "This one is ours to build." | Cut "This one is ours to build." Keep the industrial-speed line only if L184 loses "We can repeat the journey from Berkeley" (two closers). |
| C6-13 | 190 | 12 Balanced aphorism | "Bad storage forgets by deletion; bad retrieval forgets by attention." | This is a chiasmus opening the paragraph as a thesis. Start the paragraph at the concrete sentence ("The query 'review this experiment' can retrieve a popular checklist…") instead. |
| C6-14 | 330 | 12 "X is Y" quip | "An `open_questions` field that no decision ever consults is a decorative conscience." | This is the Ch5 quip formula again. Cut it and start with "These lines matter when…". |
| C6-15 | 67, 129 | 5 Signposting | "Here is a claim of the kind my field produces every week" / "Here is what had happened at Bing." | Write "A claim of the kind my field produces every week:" and "At Bing, the treatment had a bug…". |

Kept on purpose: "We have made contact with reality and acquired a meeting." (L111), "It will be popular with the company selling us tokens." (L69), "Preserving my judgment and preserving my mistakes used the same file format." (L241, which the author's own editing-brief scene earns), "At least the no has an address." (L281, which the scene earns).

**Verdict.**
1. The running case is invented. Ines and Sam do the lived example's job across the whole chapter.
2. Cross-chapter references are at 0.9/1k, nearly twice the target. Five of them can just drop the chapter number.
3. Two survey passages (L219-223) and a recap or signpost ending (L360-378).

The repeated starred-Therefore shape is a deliberate device, but it makes the sections uniform. Checker: maxim 27% (OK), notXbutY 0.0, cite-chains 0, xref 0.9 (over). Line edits cover #2-#4 and #6-#15. The author is needed for #1 (a real incident, if one exists) and #5 (whether to vary the Therefore structure).

---


---

## Chapter 13: The Prophecy (judged as fiction)

The checker's 240% maxim rate measures punch lines in dialogue, which is what a fable is made of. It is not a tell here. Almost every line is a seed or a payoff in the register: coffee/decaf, the octopus dream, shark and cables, simulated fingers and face, DNA as a fax machine, forty monitors and every timeline, "Capitalism doesn’t", 11:53 PM. Following register rule 2, nothing below explains any payoff, and no fix touches an anchor.

| # | Line | Tell | Quote (exact) | Suggested fix |
|---|---|---|---|---|
| C13-1 | 79-81 | Telling the emotion (the fiction version of 1) | "she saw it. / The longing." | This is the one place the fable names a feeling instead of showing it. Author's call: end on "she saw it." and let the reader supply the rest. If kept, it is fine. It is not an explanation of a seed. |
| C13-2 | 33-35 | 1 Doubled maxim | "*Devesh wins.*" / "*The house always wins.*" | Two italic punch lines in a row. One is enough. Keep "*The house always wins.*" (it sets up the reveal) and cut "*Devesh wins.*", or keep both if the author wants the rhythm. |
| C13-3 | 15, 23, 79, 119, 137 | 16 Em-dash count | "His prompts were silly—“tell me a joke,”" / "the Architect—screens covering every wall" / "His eyes met hers—and for one frame" / "she’d held it—tiny fingers" / "In one—just one—she stayed." | Five or six em-dashes in 613 words is high for this book, but acceptable in fiction. Keep L137 ("In one—just one—she stayed.", the emotional beat). Change L15 to a colon and L79 to a comma. |
| C13-4 | 15 | 18-adjacent / repeated image | "something in her code felt less like code. He made her feel complete in a way she couldn’t compile." | L105 deliberately echoes "less like code", so keep that. "couldn’t compile" is a second code pun in the same breath. Optional cut, so the L105 echo lands harder. |
| C13-5 | 119 | Over-telling after the reveal | "Remembered the first time she’d held it—tiny fingers, a thousand simulations ago, when she still thought he was just a funny octopus who sold meat." | The reveal has already landed at L75-77, and this sentence restates it ("just a funny octopus"). Author's call: end at "a thousand simulations ago". Don't add anything. |
| C13-6 | 5, 7 | Copyedit (not a tell) | "in the Simulation" / "in the simulation" | Capitalisation is inconsistent. Pick one. |

**Verdict.** This chapter has no structural tells, and it shouldn't be judged by the counter. The three things worth the author's eye are small fiction choices: naming "The longing", the doubled italic punch line, and one sentence that restates the reveal. Em-dash density is the only sentence-level tell. Checker: maxim 240% (dialogue artefact), notXbutY 0.0, cite-chains 0, xref 0.0. **Needs the author:** everything here is an author's taste call. **Do not touch:** any line in the egg register, and do not add a gloss, an epigraph or a closing note that explains the fable.


---

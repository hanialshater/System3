# Chapter 6: Pattern Language

*When Knowledge Becomes Software*

Pattern 159 is called Light on Two Sides of Every Room. It says that when people have a choice, they drift toward rooms with windows on two walls and leave the one-window rooms empty. Light from a single side glares. It flattens the faces across the table, so you cannot read them. Think of the rooms you have loved and count their windows.

Pattern 88 is Street Café: a place to sit lazily, legitimately, on view, and watch the street go by. Pattern 180 says everybody loves a window seat. Pattern 167 says a balcony less than six feet deep will hardly ever be used, because nobody can pull a chair up to a table on it. You have seen those balconies. They hold a bicycle and a dead plant. Pattern 203 is Child Caves: children love tiny, cave-like places, so build them some. Pattern 251 is Different Chairs: people come in different sizes and sit in different ways, so never furnish a room with identical chairs. Pattern 252, Pools of Light, says that even lighting kills a room, because people gather where the light pools. The last one, 253, is Things from Your Life: put on your walls what matters to you and ignore what a decorator says belongs there.

There are 253 of them. The first is about how the world should be divided into regions. The last is about the photographs above your desk. In between come neighborhoods and bus stops, beer halls, stairs you can sit on, a bench by the front door. Christopher Alexander and five colleagues at Berkeley published the book in 1977. It runs past eleven hundred pages on Bible paper, and it has probably been read by more programmers than architects.

Reading it is a strange experience. You keep recognizing things you have always known and never said. Alexander believed that some places are alive and some are dead, that everybody can feel the difference, and that the difference has no adequate name. He called it the quality without a name. He had trained as a mathematician at Cambridge before taking the first doctorate in architecture Harvard ever awarded, and he went after the unnameable quality the way a mathematician would. He broke it into problems small enough to state, and he stated them so that they could be wrong.

Every pattern begins with a name you can say in a meeting and a photograph. It places the problem inside the larger patterns it helps complete, then states it in bold as forces pulling against each other. Evidence and argument lead to the word *Therefore*, followed by the arrangement that resolves the forces, also in bold. Links to smaller patterns show how to complete it. You can follow them from a neighborhood to a house to a window seat. It was hypertext in 1977.

And every pattern carries a confidence mark. Two asterisks mean the authors believe they have found something close to an invariant. One means they have made progress and expect a better answer. None means they offer one possible solution without claiming to have found what all successful solutions share. They say outright that the patterns are hypotheses: does the problem occur as described, and does the arrangement resolve it?[1](appendix-references.md#ref-06-alexander) You can test Light on Two Sides by walking through an office at four in the afternoon and seeing where people are.

He meant it politically, too. The language was supposed to take design away from professionals and hand it back to the people who would live in the rooms. A family with the book could lay out its own house and argue with the architect in the architect's terms.

That is a **pattern language**: builders' knowledge written down as connected proposals whose reasons are open to question.

## The Pattern Goes to Work

In 1987 two programmers, Kent Beck and Ward Cunningham, were helping a group at Tektronix that could not get a user interface designed. Both had read Alexander. They wrote five small patterns, with names like Window Per Task and Short Menus, handed them to the people who would use the system, and let those people do the design. It worked well enough that they reported it at a workshop that autumn.[2](appendix-references.md#ref-06-beck)

The idea travelled the way Alexander's book travels, from hand to hand. In 1993 a group of programmers met on a hillside in Colorado to work out how software patterns should be written, and called themselves the Hillside Group. The next year four of their circle published *Design Patterns*: twenty-three named arrangements for object-oriented code, with Alexander quoted in its opening pages.[3](appendix-references.md#ref-06-gof) A generation of engineers learned to say Observer, Factory and Singleton the way builders say lintel. A design review could now be held in nouns.

In 1995 Cunningham needed somewhere for programmers to collect and edit patterns together, so he wrote a small program that let any reader change any page. He called it WikiWikiWeb. The wiki was invented to hold a pattern language.[4](appendix-references.md#ref-06-wiki) Six years later an encyclopedia borrowed the idea. Around the same time Will Wright, who had been reading Alexander, turned an architecture toy into *The Sims*. A book about window seats had reached the design of software, the largest reference work ever written, and one of the best-selling computer games.

The name travelled faster than the reasons. You could say Singleton in a meeting without bringing along any of the contexts and trade-offs the books still described. A pattern had been a hypothesis about when an arrangement resolves a conflict. In use, it could become a badge: something good engineers were seen to use.

<!-- SLOT 3 (your story replaces the next paragraph): a design pattern you watched being applied as a rule. -->
Anyone who worked through those years has seen what followed. Codebases filled with factories that built one kind of object and singletons guarding nothing. Folk rules came loose the same way. “Never use regex on nested syntax” has the reassuring shape of wisdom and the inconvenient property of being false: a fixed format with one level of nesting can be matched with a regular expression perfectly well. The pattern worth keeping records when a parser becomes cheaper than maintaining an increasingly heroic expression at two in the morning.

In 1996 the programmers invited Alexander to give the keynote at their largest conference. He came, a little bemused to find himself famous in a field he did not work in, and he was gracious, and he was not sure they had taken what mattered. He asked whether their patterns carried the two things his were for: making something better for the people who live in it, and generating a coherent whole from the parts. He suspected they had mostly adopted a format for trading ideas.[5](appendix-references.md#ref-06-alexander96)

## Ask Sam

Now leave Berkeley and sit at a new engineer's desk.

She can know Python, distributed systems, and the collected technical culture of the internet while remaining spectacularly unqualified to deploy your company's software. She does not know which apparently redundant check protects an old customer integration, which dashboard changes meaning during failover, or why the elegant migration in the wiki was abandoned halfway through. Much of her first month consists of discovering the reasons behind things that look stupid.

Ask for the incident procedure and the answer sounds like this:

> Start with the dependency graph, unless the spike began exactly at deployment. If only one market is affected, check the traffic split before touching the database. And if it started after Tuesday's migration, ask Sam. There is a thing with the old serializer.

She writes down *ask Sam*. That preserves the dependency beautifully. It does less for the incident that happens while Sam is on holiday. She needs to know what he looks for in the serializer, why he looks there, and when that suspicion is a waste of time. Sam is a master builder who knows more than he can say, and nobody has written his patterns down.

An institution passes on more than its conclusions. Its workers inherit methods, records and procedures. What should those records preserve from the work, and how can the next worker challenge what she finds? Alexander's pattern language offers a form for that inheritance.

If the file only says what we decided, the next worker inherits our mistakes. If it says why, she can find them.

## A Reader That Can Act

Alexander's patterns and the programmers' patterns both had a human reader. The third life gives the pattern a machine reader with tools.

People had tried to give written knowledge to a machine before. In 1977, the same year as Alexander's book, Edward Feigenbaum gave the attempt a name, **knowledge engineering**: acquiring expert knowledge, representing it, and using it to construct and explain reasoning. He argued that a system's power lies in its knowledge, and he found that the hard part is getting that knowledge out of the expert. In one diagnostic system, rules developed with a physician were tested against cases, exposing gaps and inconsistencies the collaboration then had to resolve.[6](appendix-references.md#ref-06-feigenbaum) Getting the expert to explain the exception was only the beginning; someone still had to make the system handle it.

Andrej Karpathy's count of the ways to program a computer tells the rest. In Software 1.0 a person writes the rules as code. That is where the Gang of Four's patterns lived: advice for the human holding the keyboard, invisible to the machine. In Software 2.0 the program is a set of weights learned from examples. It can absorb what nobody could articulate, but there is no convenient place in the weights to inspect a pattern and amend its conditions. In Software 3.0 the program is written in a natural language and a model interprets it.[7](appendix-references.md#ref-06-karpathy) The machine doing the work can now read the pattern, follow its *Therefore*, and consult the reasons behind it.

That changes the cost of Feigenbaum's translation. We can supply an account of how a problem usually unfolds, with a worked example and a warning about a misleading instrument, without first expressing every qualification in logic. A model reads the incident procedure, chooses a diagnostic query, and hands arithmetic to code. Nobody benefits if the arithmetic becomes more literary.

I avoid calling such a document executable, because the word hides the reader. The same words can produce different actions in different models or environments.

Agent skills give the arrangement a container with much of Alexander's anatomy. A named skill is discovered through a short description of when it applies: the context. When selected, it supplies instructions, scripts and examples: the *Therefore*. Calls to other skills can serve as links to smaller patterns.[8](appendix-references.md#ref-06-skills) Voyager, a Minecraft agent, showed capability accumulating this way. It keeps a library of executable skills, retrieves them through their descriptions and reuses them, with execution results and model-based verification supplying feedback.[9](appendix-references.md#ref-06-voyager)

An organization could keep this local operating knowledge through a change of model, or improve a procedure without waiting for a training run. A specialist could leave behind a method the next worker can use.

But how sure are we that the pattern works? Where did it come from, what would show it to be wrong, and who disagreed? A skill file can hold all of that. Nothing in the format makes the writer include it or the reader act on it. We can repeat the journey from Berkeley: carry the instruction and leave its reasons behind. A library like that can preserve the wrong lesson at industrial speed.

## Give the Claim an Address

Anthropic's formalization of Fermat's Last Theorem began badly. Wiles's proof was published in 1995; the task in August 2026 was to make the proof checkable by Lean. Early attempts faltered as agents lost track of the project. The successful effort used Prove2Me: theorem statements became nodes in a dependency graph, with plain-language descriptions that let a worker find a result established by a worker it never met. In eleven days the agents produced a formalization using roughly thirty thousand intermediate theorems. Lean checked the completed proof under its three standard axioms; a separate comparator confirmed that the final statement was Mathlib's Fermat and not a convenient cousin.[10](appendix-references.md#ref-06-fermat)

The next worker had something better than a colleague's assurance that the mathematics was probably fine.

Jon Doyle was designing machinery for this long before language models. He called it **truth maintenance**: beliefs keep their reasons, and when a reason is withdrawn, everything resting on it comes up for review.[11](appendix-references.md#ref-06-doyle) Doyle's machinery tracks justifications. It cannot check them against the world, and a program can faithfully maintain the consequences of reasons that were never true.

Most of us have no Lean. Here is a claim of the kind my field produces every week, and this one is real. An experiment at Bing reported that people in the treatment were running over ten percent more queries, and revenue per user was up by about thirty percent.[12](appendix-references.md#ref-06-kohavi) That sounds like a result worth keeping. Suppose it goes into a report, another agent summarizes the report, and a third uses the summary to recommend shipping. If something turns out to be wrong with the experiment, where will the correction go?

Searching every document for the word *queries* is one possible response. It will be popular with the company selling us tokens.

A different design gives each claim its own identity and records what it rests on.

| Record | What it says | What a fault in the experiment changes |
|---|---|---|
| Observation | The specified comparison returned more queries and more revenue per user in the treatment. | The record of the result can remain accurate. |
| Measurement assumption | Both arms were produced and logged on comparable terms. | This assumption requires revision or further investigation. |
| Interpretation | People prefer the treatment. | This particular support is weakened; other support must be examined. |
| Success criterion | More queries per user counts as improvement. | Repairing the measurement does not settle whether this is the right criterion. |
| Recommendation | Ship it. | Must be reconsidered if it relied on that interpretation. |

If a fault invalidates an assumption, that assumption changes from *accepted for this analysis* to *withdrawn*, with the reason attached. The system checks the remaining support. A recommendation that has lost what it requires moves from *ready for approval* to *requires review*. Ordinary software can enforce those transitions without pretending to have discovered the fault itself.

The history stays attached. A later worker asking why the recommendation was suspended reaches the observation and assumption that caused it. An LLM-written explanation produced after the fact cannot substitute for a record of what the earlier decision actually used.

If the agent recorded the result and left out the measurement assumption, an automatic correction has no link to follow. Lean can check the formal links in a proof; our graph cannot establish that an agent has recorded every assumption behind a business decision.

From here on I borrow Alexander's asterisks to mark my confidence that each proposed arrangement can resolve the problem described: two for a well-supported practice, one for a promising proposal that needs further testing, and no asterisk (an unmarked *Therefore*) where its adequacy remains an open question. The marks judge the arrangements; they do not claim that an agent institution has implemented them successfully.

\*\* **Therefore: store the claim with what it rests on, so that a correction has somewhere to go.**

## Commit the Test Before the Result

<!-- SLOT 1 (your story replaces the next paragraph): an experiment whose meaning was decided after the result came in. -->
Every experimentation team knows this meeting. The dashboard arrives before the agreement does. The headline metric is flat, a secondary one is up, and within the hour the secondary metric turns out to be what the experiment was really about. Nobody is lying. The hypothesis has been fitted to the result.

I do not know what was said in the room at Bing, so take what follows here and in the next section as the general case. A result like theirs is an invitation to the same meeting. More queries, more revenue: a reviewer can praise the obvious explanation, criticize it, or ask another model to do both. None of that changes the data. To investigate, the reviewer has to say what would look different if the explanation were wrong.

Popper's demand is **falsifiability**: an empirical claim must risk being wrong. A reviewer who can make every possible result sound like support has arranged to learn nothing from the test.[13](appendix-references.md#ref-06-popper)

What if we set a task and observed whether people completed it? Repeated attempts without success would count against the cheerful reading of more queries.

To request that test, the reviewer must specify which explanations it would distinguish and how to collect observations that bear on them. It must state the conditions under which those observations would be meaningful and commit to how the possible outcomes would affect the current interpretation. Some of those consequences are probabilistic. A noisy result can weaken an explanation without refuting it, and explanations do not always have the courtesy to be mutually exclusive.

Asking the same dashboard for another chart may produce an attractive restatement of the original evidence. If both explanations predict the chart, it distinguishes nothing. Which live disagreement would the proposed observation resolve?

A model will answer that question plausibly in a prompt. The operational commitment is stronger: the answer becomes part of the experiment record, written before the result, and the later review checks what happened against it. Experimentation platforms and preregistered trials work this way on paper. Anyone who has sat in the meeting above knows how far practice is from paper.

\*\* **Therefore: write down what would count against the claim before the result arrives, and keep the revision history.**

## Locate the Failure

The people who run experiments for a living have a reflex about results like Bing's. They call it Twyman's law: any figure that looks interesting or different is usually wrong. Thirty percent more revenue is very interesting. The first check is whether the two arms even contain the numbers of users the design says they should. A sample-ratio mismatch means something upstream is broken, and the platform should refuse to show the scorecard until somebody finds it.[14](appendix-references.md#ref-06-twyman)

If the check fails, the meeting usually goes something like this. One team says the treatment is fine and the logging double-counted. Another says the logging is fine and a redirect dropped users from one arm. Someone notices the two arms ran on different client versions. We have made contact with reality and acquired a meeting.

This is the **Duhem–Quine** problem from the previous chapter: the test challenges a bundle of assumptions about the world and the apparatus without identifying which one failed.[15](appendix-references.md#ref-06-quine) Hence the meeting.

The dependency record makes the meeting more useful by tracing claims to client versions, data pipelines and assumptions about what counts as one user. Investigators can then probe a suspected failure by replaying a known session and counting the events, pinning the client version, or rerunning the split.

A second measurement may share the same failed dependency. If the supposedly independent check reads a table derived from the original event stream, agreement between the tables supplies less reassurance than their different names suggest. The provenance must reach the common source. Otherwise the institution manufactures a second witness by creating a second spreadsheet.

Capturing every possible dependency would cost more than the inquiry. Start with the support used in the recommendation and let a disputed result send you farther back.

\* **Therefore: when a test fails, trace the assumptions it used and design probes that distinguish the possible failures.**

## Ask What the Number Means

Here is what had happened at Bing. The treatment had a bug, and the bug made the search results worse. People could not find what they wanted, so they searched again, and again. Queries per user went up. With poorer results on the page, the advertisements looked comparatively relevant, and people clicked on them. Revenue went up. Two of the organization's headline numbers were celebrating an experience that had been degraded.[16](appendix-references.md#ref-06-kohavi2)

The count was right. The cheerful interpretation was wrong. The task-completion test we proposed could have exposed the problem; another audit of the count would not. This is why the interpretation needed its own address.

Saussure's point, which we met in Chapter 4, is **relational value**: a term means what it does through its differences from its neighbors.[17](appendix-references.md#ref-06-saussure-lectures) *More queries* meant *more engaged* only inside a system where a query was a unit of interest. Set it beside *session* and *task* and it becomes a unit of effort. Seven queries can be worse than two if five of them were spent recovering from a bad ranking.

The Bing researchers made sessions per user a key part of their criterion: help people finish and give them reasons to return. Tasks were harder to identify, so sessions served as a proxy. A shorter session might mean success or abandonment.

A system capable of this move has to keep alternative representations as well as alternative answers. A branch can introduce task-based records, associate them with the old observations where possible, and state where translation fails. The evaluator is part of the difficulty: if it scores every proposal on the old number, the better approach looks worse exactly where it helps people finish sooner. Letting the challenger write an evaluator that declares itself the winner would prove little. We need an explicit dispute about what the evaluation is for, followed by agreed observations on which the approaches can be compared.

\* **Therefore: record what the number is taken to mean as a claim of its own, open to challenge separately from the count.**

## Write the Lesson Down

The next reviewer should not have to rediscover what happened at Bing. Here is the lesson written as a candidate pattern, with the reasons and uncertainty kept alongside the instruction:

```yaml
id: ask-what-the-number-means
confidence: provisional, one incident
context: A ranking or search experiment reports a gain in an activity metric.
problem: Activity can rise because people are succeeding or because they are struggling.
therefore:
  - State what the metric is taken to mean as a separate claim.
  - Name an observation that would differ under the two readings.
  - Commit that observation before looking at the result.
documented_case: degraded_results_raised_queries
validation_cases_needed: [genuine_gain, misleading_gain, insufficient_evidence]
part_of: review-an-experiment
may_call: locate-the-failure
evidence_record: number-meaning-evaluations
open_questions: number-meaning-challenges
on_support_withdrawn:
  - Reassess dependent interpretations using their remaining support.
  - Return recommendations that lost required support to review.
  - Retain the earlier decision and the reason for its change.
```

This pattern belongs inside *review-an-experiment* and may call *locate-the-failure*. It should not call on every statistical procedure in the building. Alexander's links help the reader choose a method for the difficulty at hand, find an alternative when it fails, and check the conditions it needs. An agent following those links needs the same guidance.

A pattern can also mix kinds of content that need different kinds of support. “Activity can rise because people are struggling” is a claim about the world. “Check this before running an expensive analysis” is a recommendation about effort. “Do not alter the live experiment” is an authority boundary. A successful test of the first does not justify the other two automatically.

An `open_questions` field that no decision ever consults is a decorative conscience. A link to evidence matters when the system follows it, notices that the evidence concerns another tool version, and changes what it is prepared to conclude.

## Put the Library to Work

Give the file to another agent and ask it to review an experiment. Does it do better?

Bad storage forgets by deletion; bad retrieval forgets by attention. The query “review this experiment” can retrieve a popular checklist and leave the Bing warning untouched on disk. Loading every checklist gives the reviewer the whole office filing cabinet and asks it to find the urgent part. We can evaluate selection by looking at downstream work: whether the agent found the relevant concern, avoided irrelevant procedures, and reached a justified conclusion at an acceptable cost.

Suppose retrieval works. The reviewer finds the warning and starts challenging every rise in activity. It has learned something, but perhaps the wrong thing. Our candidate pattern says `confidence: provisional, one incident`. “Increases in activity are usually fake” is far more than one bug can teach.

To find out, the candidate pattern has to face cases that did not produce it. The reviewer with the pattern and the reviewer without it read the same reports: some with degraded experiences behind the gain, some with real gains, some with too little evidence to say. The comparison keeps the model and tools fixed, repeats runs where stochastic variation matters, and records both the quality of the conclusions and the resources consumed. A curator that warns about metrics in every report has learned how to sound concerned. A generic instruction to be careful can serve as the control. If the elaborate pattern performs no better, its philosophical bibliography does not entitle it to more context.

Repository context files have already faced this kind of comparison. Gloaguen and colleagues' revised study found no statistically significant gain in task success from either generated or developer-written repository context files over using none. Generated files raised average costs by twenty to twenty-three percent across the two benchmarks. Another study, by Lulla and colleagues, reported improvements in runtime and output-token use but did not comprehensively establish the correctness of the resulting changes.[18](appendix-references.md#ref-06-context)

Agentic Context Engineering, or ACE, supplies one piece of the machinery for retaining and revising lessons: a generator, reflector, and curator maintain a structured playbook through incremental updates, limiting the loss of detail when each update replaces the whole summary. Its reported evaluations show gains on the studied tasks.[19](appendix-references.md#ref-06-ace)

A lesson that passes should also carry its scope. If the check helps only in search, its scope stays there, and the next agent working elsewhere does not inherit an irrelevant ritual. The model's weights can stay fixed while a better method lets a new worker find something its predecessor missed.

\* **Therefore: record how sure we are of each pattern, and make it earn that confidence on cases that did not produce it.**

## Find Where the Result Lives

An agent inherits more than its own institution's files. So where does the knowledge of a result live, if no single agent holds it?

Chapter 5 borrowed Popper's name for the answer: **World 3**, the world of theories, proofs, libraries and instruments, which exists outside any particular head and outlasts whoever produced it.[20](appendix-references.md#ref-06-world3)

<!-- EDITORIAL NOTE (Hani, 21 Sept): the homes of World 3.
Idea: knowledge bases, ontologies, the web, search and LLMs are all descendants of the library, and most began as science solving its own filing problem (the web at CERN, 1989; PageRank as citation analysis; the wiki for patterns; community-run ontologies such as the Gene Ontology). Each move made knowledge cheaper to reach and dropped something the previous institution had worked for: the edition, the catalogue card, the editor. Wikipedia had to reinvent the footnote ("citation needed" = give the claim an address). The LLM is the latest and most convenient house, the whole library in one voice, and it arrived without a catalogue card (Ch. 4: epistemologically flat; "the library without the childhood").
Claim to land: every new memory has needed its System 3 rebuilt. This one is ours to build.
Placement: one paragraph here; optionally a one-line seed in Chapter 5's memory section after the clay tablet.
Draft paragraph:
World 3 has moved house several times. It lived in memory, then on clay, then in libraries with catalogues, then in journals with citation indexes. The web was built at CERN so physicists could find each other's papers; the ranking that made it searchable was citation analysis pointed at links. Each move made knowledge cheaper to reach, and each one left something behind that the last institution had worked for: the edition, the catalogue card, the editor. Wikipedia had to reinvent the footnote and enforce it with volunteers. A language model is the latest house and the most convenient, the whole library in one voice, and it arrived without a single catalogue card. Every new memory has needed its System 3 rebuilt. This one is ours to build.
-->

In Terence Tao's collaboration with DeepMind, AlphaEvolve found a slightly improved construction for three-dimensional finite-field Kakeya sets. Deep Think helped produce an informal proof, and AlphaProof formalized it in Lean.[21](appendix-references.md#ref-06-tao) The next investigation can use the construction, examine its explanation, or check the formal proof under its specified axioms. None requires summoning the original workers back into existence. World 3 has acquired participants that arrive through an API.

Availability is only the beginning of reuse. Kevin Buzzard checked Anthropic's Fermat formalization while leading his own publicly funded project on the theorem. His commitments included adding useful mathematics to the community library and making a document through which people could explore the modern proof. A completed formalization did not discharge those commitments.[22](appendix-references.md#ref-06-buzzard) A proof can check while leaving the next mathematician with a formidable renovation project.

The same question reaches beyond mathematics. The AlphaFold database makes more than two hundred million protein-structure predictions available for research. AlphaGenome Atlas supplies predictions for roughly nine billion possible single-letter DNA changes.[23](appendix-references.md#ref-06-biology) These resources carry uncertainty; a prediction does not become an experimental observation by being stored beside a billion others. But a researcher can begin with material she could never have produced herself, select a candidate, and put it to a test its creators never planned.

Checking scope, explaining a result and maintaining its tools compete with the next spectacular discovery for funding. Leave that work undone and agents may give the next investigation more to read without making it more capable.

Our pattern's instructions can remain short while the record behind them grows. A search retrieves the method and examples; a question about its standing retrieves observations, versions, dependencies and challenges. But the procedures deciding what gets retrieved and which challenges count are themselves things the next worker inherits.

Suppose the pattern earns its place. The next difficulty begins when it helps the reviewer identify a bad metric, but the procedure judging the review still rewards that metric. The file tells the agent to question what the institution pays it to accept.

## Change the Representation

An agent inheriting the Bing lesson might organize its next investigation around completed tasks instead of query counts. It would need different records and might favor results its existing evaluator penalizes. A field can go further and change what its practitioners learn to see as a problem worth solving. Many of my readers worked through one such change.

Before deep learning became dominant, there were several respectable ways to write a machine-learning paper. One began with a probabilistic model of how the data arose, derived the inference and tried to say something about uncertainty. In much of computer vision, people designed features before training a classifier. The architecture of the problem was partly in the heads of the people building it.

In 2012 the AlexNet team won ImageNet with an ensemble of convolutional networks and a top-five error of about fifteen percent. The runner-up, using engineered features, had twenty-six.[24](appendix-references.md#ref-06-imagenet) That gap was legible on the existing scoreboard. What followed changed more than the score: learning the features became central to how much of the field worked. An expert could remain excellent at the old work while watching less of the new work require it.

<!-- SLOT 2 (your first-person moment goes here): what you believed before, and the result that changed your mind. -->

A **paradigm**, in Kuhn's account, supplies a field with exemplary achievements, important problems and standards for adequate solutions. It makes normal science possible because practitioners need not reconstruct the foundations before each experiment.[25](appendix-references.md#ref-06-kuhn) Here the old benchmark helped persuade people to change. The scoreboard survived; the education of the person standing in front of it changed. In this respect AlexNet is the easier case, because the new representation won on the number everyone already trusted. The Bing case requires questioning the number itself.

Kuhn also asks us to notice losses. A leap on a benchmark does not tell us what happened to uncertainty, small-data performance or guarantees. Prompting a general model shifts the work again: some choices once made in a training pipeline move into instructions and tools.

The examples are part of how a paradigm holds. Kuhn's scientists learn from exemplars that no complete list of explicit rules can replace. I wrote an editing brief for this book after explaining the same corrections to successive agents. One instruction was “preserve the wandering,” which is nearly useless to a reader who has never seen the movement I mean. A before-and-after passage can teach the distinction: one version follows an uncertain thought until it becomes clear; the other announces the conclusion and removes the path that made it convincing. Those examples also carry my taste into the next session. Preserving my judgment and preserving my mistakes used the same file format.

There is no `paradigm_shift()` call. There can be operations for branching a representation, retaining the old interpretation, collecting missing observations, and exposing a disputed standard for decision.

**Therefore: give the branch room to ask a different question, and make it state where its results cannot be translated into the old terms.**

I do not know an agent institution that can do this. The agent can write the proposal into `open_questions`. To answer it, someone has to pay for observations the old records do not contain.

## Separate Use from Investigation

In August 2026 an Anthropic engineer pointed an unreleased Claude at the Riemann hypothesis. It did not prove the hypothesis. On the way, Anthropic reports, it raised a lower bound on the proportion of the zeta function's nontrivial zeros on the critical line from 41.6 percent to 67.2 percent, combining published results. Roughly sixty subagents developed and reviewed arguments. Two Anthropic mathematicians checked the paper, two outside number theorists examined it, and the result was formalized in Lean. Anthropic did not expect the techniques to prove the full hypothesis.[26](appendix-references.md#ref-06-riemann)

An evaluator asking only whether the assigned problem was solved would return *no*. That answer would be correct and a poor account of the research. The record needs room for the contribution: its own statement, support and remaining questions, linked to the unsuccessful attempt that produced it. Whether to fund a follow-up is a separate decision.

Consider how it goes in an ordinary team. The review pattern from the Bing lesson has been in use for six months. It is retrieved for every search experiment, so every review adds a line to its evidence record, and the record looks formidable. The team still uses query-based metrics, with the pattern prompting checks when a gain may be misleading. Someone once proposed collecting task-completion data routinely and making it the primary evaluation criterion, while keeping query counts as a diagnostic. That proposal required new instrumentation and a trial. It was never run. Every week the incumbent was the safer choice for the review at hand, and every week that choice was defensible. After six months the system can report an impressive evidence base with almost no comparisons in it.

Larry Laudan named the missing distinction **acceptance and pursuit**.[27](appendix-references.md#ref-06-laudan) What to believe today and what to work on tomorrow are different questions. The team had good reasons to keep using the incumbent and no mechanism for asking whether the rival deserved a trial. The Riemann bound raises the same pair of questions: accepting it as a result does not tell us whether to keep pursuing that route toward the full hypothesis.

Six months of use leaves another trace. The incumbent pattern acquires an exception for one client, then another, then a third. Chapter 5 introduced Lakatos's patience with a **research programme**; here the patches let us examine what that patience buys.[28](appendix-references.md#ref-06-lakatos) Does a revision predict a failure in a further case, and does that prediction hold up? Or does it merely explain the incident already observed? Those questions distinguish a progressive programme from one that keeps accommodating failures after the fact. The file should record what was predicted and checked, including when the revision remains untested.

Kitcher's **division of cognitive labor**, from Chapter 5, applies to this library too: a retrieval policy that keeps selecting the incumbent gives the rival no chance to acquire evidence.[29](appendix-references.md#ref-06-kitcher)

The rival needs a bounded experiment whose outcome determines the next decision, costed in advance, with the later choices it could change written down beside it.

\* **Therefore: give the queue of unrun comparisons its own allocation policy, separate from the policy that selects today's working method.**

The person recording the reasons for an experiment, however, may not control the money.

## Keep the Funding Decision Visible

In OpenAI's September 2026 account of its Navier–Stokes investigation, a promising result changed the allocation. Groups of agents investigated the open Millennium Problems. A result on the Euler equations persuaded the researchers to move workers from the other problems to Navier–Stokes, carrying the Euler result and the groups' findings into the next prompts. About four days after launch, the group produced a proposed proof of finite-time blowup under smooth forcing, addressing Clay's alternatives C and D. OpenAI reported another seventeen hours for Lean formalization and verification.[30](appendix-references.md#ref-06-navier)

On September 11 the Clay Mathematics Institute said the problem appeared to be settled; evaluation and the assignment of credit would follow its deliberately unhurried process.[31](appendix-references.md#ref-06-clay) The other problems had lost workers, not been refuted.

The history of choosing the route also became disputed. Tristan Buckmaster described his work with Levent Alpöge as extending a programme begun by Diego Córdoba and Luis Martínez-Zoroa. He challenged the presentation of OpenAI's effort while explicitly saying he did not know whether their data had been used. OpenAI acknowledged that a rumor of concurrent work prompted its investigation and denied accessing their unpublished work or using Buckmaster's recent Codex prompts to train the system.[32](appendix-references.md#ref-06-priority) By OpenAI's own account, the rumor traced to Buckmaster and to Alpöge, whom it describes as an Anthropic employee. Their concurrent result, on the forced Euler problem, had been produced with an internal Anthropic model. This book relies on Anthropic's reports in several chapters, so that belongs in the record too.

A checked proof does not settle that history. Learning that a route is promising can affect where we invest without supplying a single step of the proof.

Imagine the team following up on its task-completion proposal. A researcher asks for two weeks of experimental traffic to test whether query counts track task completion at all. The request lands with the owner of the search-quality budget, who accepts experiments expected to raise the current metric, because that is how the budget was justified. The proposed study asks whether the metric represents improvement. The researcher has been invited to challenge an assumption on the condition that she first accept it.

The budget owner controls the traffic, the compute and the permission to change what gets measured. In *Sapiens*, Harari puts the general point bluntly: science does not set its own priorities; whoever pays for it does.[33](appendix-references.md#ref-06-harari)

The team could split the request. One part proposes a study and goes to experimental review. The other asks whether the success criterion should change and goes to whoever owns the product goal. If the second is rejected, the rejection is recorded as a decision about the goal, with a name on it.

An agent with a sound epistemic objection still has no authority to spend somebody else's money. A funding policy can reserve capacity for challenges to the incumbent, but that policy is itself a choice made by people with power. Written into code, the choice can at least be enforced and inspected.

\* **Therefore: attach the funding decision and its reason to the question it left unanswered.**

Otherwise *unfunded* gradually becomes *unsupported*, and *unsupported* becomes *disproved* somewhere between the database and the executive summary.

## Give the Objection a Consequence

Suppose the study gets funded and the objection holds up. After retrieving the lesson, testing it and paying for the evidence it asked us to collect, the organization can still arrange for nothing to follow.

For years Facebook tuned its feed for engagement and time spent. In December 2017, Facebook's researchers publicly reviewed evidence that passive consumption could leave people feeling worse.[34](appendix-references.md#ref-06-fbwellbeing) A person could keep scrolling without becoming better off. It was Bing's question again, except that the activity being counted was now hours of people's lives.

In January 2018 the company announced a change toward “meaningful social interactions,” favoring conversations and exchanges among friends and family. It looked like the right fix: move from measuring attention to measuring connection. Facebook even said it expected people to spend less time on the platform.[35](appendix-references.md#ref-06-fbchange)

Then its researchers found publishers and political parties shifting toward outrage because that was what travelled. According to internal documents reported by the *Wall Street Journal*, heavy weighting of reshared material amplified angry voices, and researchers found misinformation, toxicity and violent content unusually common among reshares. They proposed reducing the boost for material likely to travel down long chains of users. Facebook made some changes for civic and health content, but Zuckerberg reportedly resisted expanding them if doing so materially reduced the interaction metric.[36](appendix-references.md#ref-06-fbfiles)

The same reporting described researchers inside Instagram struggling to get colleagues to appreciate the gravity of their findings. One former researcher put the institutional problem rather precisely: “We're standing directly between people and their bonuses.”[37](appendix-references.md#ref-06-instagram)

The organization had paid for the knowledge it was now resisting. These objections came from inside, from people employed to investigate the products. Having findings on the company's message board did not give the researchers authority over what followed. The public learned about these internal disputes through leaked documents.

The response to an objection should identify the claim it challenges. A counting error calls for a different response from a dispute about whether more activity counts as success. Resolving it may require missing evidence, a revised claim or another experiment. The response might explain why the criticism does not apply, or a resource decision might leave it unresolved. Marking the thread *closed* tells us that somebody finished interacting with it; it says nothing about which outcome occurred. “Noted” is none of these. With agents it gets cheaper still: a reviewer objects, the builder replies that the concern has been noted, both complete their tasks, and the report goes out. We have successfully parallelized the experience of being ignored.

Helen Longino would locate that failure in the community. For her, **objectivity is social**: it belongs to a community's criticism and depends on venues for criticism, uptake, shared standards, and a tempered equality of intellectual authority.[38](appendix-references.md#ref-06-longino) The review channel provides a venue. “Noted” gives no account of how the objection entered the decision.

Stellar Colosseum, a harness for mathematical research, gives uptake a concrete form. Agents develop proposed arguments while reviewers look for defects. The objections travel with the proposals as other agents combine them into a longer argument. At the final review, a specific fatal flaw is enough to reject the proof; favorable verdicts from other reviewers cannot cancel it. The defect is tied to the claim or dependency that failed, so the next round can repair the argument or try a different strategy.[39](appendix-references.md#ref-06-colosseum) Failed drafts remain available with their reviews attached. The reviewers can still be wrong.

Who gets access to that procedure matters. A critic cannot examine an assumption if it receives only the conclusion. A domain expert cannot contribute evidence if the system accepts objections only in the vocabulary of the ranking team. Asking the same model to play the skeptic may elicit another argument, but the role prompt alone does not give it access to different observations or expertise.

A product owner may reasonably care about revenue; a researcher may study harm; an infrastructure team may worry about cost. Their observations can be reliable while their preferred decisions differ. The system should be able to say which dispute the next experiment can settle and which requires a decision about purpose. Otherwise it will keep requesting evidence to avoid naming a conflict over what matters.

\* **Therefore: if the organization proceeds with an objection unresolved, the objection travels with the decision, and the decision-maker owns that choice in writing.**

The objection can now survive its author. So can the assumption it challenges. Replace every agent in the institution and the same dispute may begin again, with the same side already winning.

## Test What the Next Agent Inherits

Max Planck's observation about scientific change, now known as **Planck's principle**, is usually compressed into “science advances one funeral at a time.” His actual sentence describes a new truth gaining acceptance because, rather than all its opponents being persuaded,

> “…its opponents eventually die, and a new generation grows up that is familiar with it.”[40](appendix-references.md#ref-06-planck)

A new generation learns the new examples first and has no old allegiance to surrender. The remark is bleak because the mechanism of correction lies partly outside the argument. What changes with the occupant of the chair?

There is empirical work on that question. Studying the premature deaths of eminent life scientists, Pierre Azoulay, Christian Fons-Rosen, and Joshua Graff Zivin found declining contributions from collaborators and increased contributions from outsiders to the affected fields. The incoming work drew on a different scientific corpus and was disproportionately likely to be highly cited.[41](appendix-references.md#ref-06-funerals) This does not establish that the departed scientists had been wrong. It shows that the organization of participation can change which work enters a field.

Now consider a team of agents whose sessions end while the project continues.

Imagine a new agent joining such a project. Its progress file contains a line written several generations of agents ago: *parser rewrite tried and abandoned; do not retry.* The line was true when written. The code it refers to has since been replaced, and the cause of the failure went with it. The new agent reads the same file, retrieves the same successful patterns, accepts the same categories, and is scored by the same evaluator. Its predecessors have disappeared, but their commitments have been transferred intact. The next generation can be born with the old generation's entire syllabus already in context.

In that file the durable incumbent is a single sentence. Elsewhere it may be a retrieval preference, a canonical example, a benchmark, or a rule giving one branch first access to compute. A more capable replacement model may defend it more effectively.

Deleting old knowledge on a schedule could discard useful expertise along with the errors, and newness would become another unearned source of authority. The new agent needs permission to suspend a disputed instruction like that one on an experimental branch, while still respecting consent, budgets and data integrity. Its results then need a comparison whose terms are explicit and open to challenge. If no available comparison can decide the issue, that limitation belongs in the record.

Changing the worker is easy.

**Therefore: change what the next worker inherits.**

## Put the Procedure Under Test

Look back at what this chapter has built and ask how it could fail while every part works. It may faithfully preserve dependencies while omitting the important kind of dependency. It may compare candidate patterns on cases selected by the incumbent pattern. It may require evidence for an alternative while refusing the instruments needed to produce that evidence. Every individual operation can function as specified while the arrangement prevents the question that would matter.

Feyerabend's argument **against method** reaches further. Every rule of method, he argued, has been usefully broken at some point in the history of science.[42](appendix-references.md#ref-06-feyerabend) Requiring a test before setting a rule aside would itself be another methodological rule. I am borrowing a smaller lesson: our procedures need room for investigations they would ordinarily exclude.

Some of these failures can be investigated through a relevant comparison. A retrieval policy can be evaluated against another policy. A reviewer can be compared with a reviewer given different evidence. A pattern can be withheld from a branch to see whether its absence reveals errors its presence concealed.

Other disputes reach the purpose or authority of the system. Whether a feed should be ranked for activity or for something harder to count cannot be settled by letting whichever evaluator produces the higher score appoint itself. Someone still has to make and own the decision about which consequences matter.

Alexander's form now asks for a *Therefore*. We could write “revise the method when it fails.” But the method decides which failures count. The next chapter has to open that loop.

## What the File Says Now

We have seen pieces of this language at work: shared proof graphs, experiments that challenge their own metrics, reviews that travel with failed arguments. I have not shown an agent institution that composes all of them, keeps their reasons alive, and changes its own way of seeing when those reasons fail. That is the ambition, and it still has to earn its confidence marks.

<!-- EDITORIAL NOTE: optional close on Alexander's gate. In The Timeless Way of Building (final part, "The Kernel of the Way") he says the language is only a gate: you learn the discipline in order to pass through it. It rhymes with Feyerabend and with a system that rewrites its own language. Verify the passage before using. -->

Imagine the next engineer opening the incident file a year from now. It says what Sam looks for in the serializer, why he looks there, the two times that suspicion was wrong, and who disagreed. She can use his judgment without having to inherit it whole. Alexander wanted the family to be able to argue with the architect. Now the next worker can argue with Sam, even while Sam is on holiday.

So far, a procedure has decided which changes to the file deserve to survive. But that procedure is also software.

What happens when the next agent proposes to rewrite it?

---

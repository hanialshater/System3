# Chapter 6: Pattern Language

*When Knowledge Becomes Software*

Imagine a search team. At ten past two in the morning, search in one market starts returning empty pages. The engineer on call—call her Ines—has been at the company for five weeks. The runbook on her second screen is admirably clear until the line where it stops being clear: *if it started after Tuesday’s migration, ask Sam. There is a thing with the old serializer.*

It started after Tuesday’s migration. Sam is on a beach in Portugal with his phone in a drawer, which is exactly where he deserves to be.

Ines has the logs, the dashboards and an agent that has read every document the company owns. None of them contains what Sam looks for in the old serializer, because Sam never wrote it down. Nobody asked him to. It was never going to be two in the morning while he was away.

---

Pattern 159 is called Light on Two Sides of Every Room. It says that when people have a choice, they drift toward rooms with windows on two walls and leave the one-window rooms empty. Light from a single side glares. It flattens the faces across the table, so you cannot read them. Think of the rooms you have loved and count their windows.

Pattern 88 is Street Café: a place to sit lazily, legitimately, on view, and watch the street go by. Pattern 180 says everybody loves a window seat. Pattern 167 says a balcony less than six feet deep will hardly ever be used, because nobody can pull a chair up to a table on it. You have seen those balconies. They hold a bicycle and a dead plant. Pattern 203 is Child Caves: children love tiny, cave-like places, so build them some. Pattern 251 is Different Chairs: people come in different sizes and sit in different ways, so never furnish a room with identical chairs. Pattern 252, Pools of Light, says that even lighting kills a room, because people gather where the light pools. The last one, 253, is Things from Your Life: put on your walls what matters to you and ignore what a decorator says belongs there.

There are 253 of them. The first is about how the world should be divided into regions. The last is about the photographs above your desk. In between come neighborhoods and bus stops, beer halls, stairs you can sit on, a bench by the front door. Christopher Alexander and five colleagues at Berkeley published the book in 1977. It runs past eleven hundred pages on Bible paper, and it has probably been read by more programmers than architects.

Reading it is a strange experience. You keep recognizing things you have always known and never said. Alexander believed that some places are alive and some are dead, that everybody can feel the difference, and that the difference has no adequate name. He called it the quality without a name. He had trained as a mathematician at Cambridge before taking the first doctorate in architecture Harvard ever awarded, and he went after the unnameable quality the way a mathematician would. He broke it into problems small enough to state, and he stated them so that they could be wrong.

Every pattern begins with a name you can say in a meeting and a photograph. It places the problem inside the larger patterns it helps complete, then states it in bold as forces pulling against each other. Evidence and argument lead to the word *Therefore*, followed by the arrangement that resolves the forces, also in bold. Links to smaller patterns show how to complete it. You can follow them from a neighborhood to a house to a window seat. It was hypertext in 1977.

And every pattern carries a confidence mark. Two asterisks mean the authors believe they have found something close to an invariant. One means they have made progress and expect a better answer. None means they offer one possible solution without claiming to have found what all successful solutions share. They say outright that the patterns are hypotheses: does the problem occur as described, and does the arrangement resolve it?[1](appendix-references.md#ref-06-alexander) You can test Light on Two Sides by walking through an office at four in the afternoon and seeing where people are.

He meant it politically, too. The language was supposed to take design away from professionals and hand it back to the people who would live in the rooms. A family with the book could lay out its own house and argue with the architect in the architect’s terms.

That is a *pattern language*: builders’ knowledge, the kind Sam carries, written down as connected proposals whose reasons are open to question.

## The Pattern Goes to Work

In 1987 two programmers, Kent Beck and Ward Cunningham, were helping a group at Tektronix that could not get a user interface designed. Both had read Alexander. They wrote five small patterns, with names like Window Per Task and Short Menus, handed them to the people who would use the system, and let those people do the design. It worked well enough that they reported it at a workshop that autumn.[2](appendix-references.md#ref-06-beck)

The idea traveled the way Alexander’s book travels, from hand to hand. In 1993 a group of programmers met on a hillside in Colorado to work out how software patterns should be written, and called themselves the Hillside Group. The next year four of their circle published *Design Patterns*: twenty-three named arrangements for object-oriented code, with Alexander quoted in its opening pages.[3](appendix-references.md#ref-06-gof) A generation of engineers learned to say Observer, Factory and Singleton the way builders say lintel. A design review could now be held in nouns.

In 1995 Cunningham needed somewhere for programmers to collect and edit patterns together, so he wrote a small program that let any reader change any page. He called it WikiWikiWeb. The wiki was invented to hold a pattern language.[4](appendix-references.md#ref-06-wiki) Six years later an encyclopedia borrowed the idea.

The name traveled faster than the reasons. You could say Singleton in a meeting without bringing along any of the contexts and trade-offs the books still described. A pattern had been a hypothesis about when an arrangement resolves a conflict. In use, it could become a badge: something good engineers were seen to use.

Anyone who worked through those years has seen what followed. Codebases filled with factories that built one kind of object and singletons guarding nothing. Folk rules came loose the same way. “Never use regex on nested syntax” has the reassuring shape of wisdom and the inconvenient property of being false: a fixed format with one level of nesting can be matched with a regular expression perfectly well. The pattern worth keeping records when a parser becomes cheaper than maintaining an increasingly heroic expression at two in the morning.

In 1996 the programmers invited Alexander to give the keynote at their largest conference. He came, a little bemused to find himself famous in a field he did not work in, and he was gracious, and he was not sure they had taken what mattered. He asked whether their patterns carried the two things his were for: making something better for the people who live in it, and generating a coherent whole from the parts. He suspected they had mostly adopted a format for trading ideas.[5](appendix-references.md#ref-06-alexander96)

## Ask Sam

By four the market had recovered, because Ines rolled back the migration, which restored service without explaining the failure. The runbook she had been working from read like this:

> Start with the dependency graph, unless the spike began exactly at deployment. If only one market is affected, check the traffic split before touching the database. And if it started after Tuesday’s migration, ask Sam. There is a thing with the old serializer.

She knows Python, distributed systems and the collected technical culture of the internet, and she is still spectacularly unqualified to run this company’s software. She does not know which apparently redundant check protects an old customer integration, which dashboard changes meaning during failover, or why the elegant migration in the wiki was abandoned halfway through. Much of her first month consists of discovering the reasons behind things that look stupid.

*Ask Sam* preserves the dependency beautifully. It did nothing for her at two in the morning. She needed what Sam looks for in the serializer, why he looks there, and when that suspicion is a waste of time. Sam is a master builder who knows more than he can say, and nobody has written his patterns down.

She would settle for his reasons and some way to argue with them. Alexander had worked out a form for exactly that, for rooms.

If the file only says what we decided, the next worker inherits our mistakes. If it says why, she can find them.

The next morning Ines opens a new document and discovers that *why* is much harder to write down than *what*.

## Give the Claim an Address

A reason has to be attached to something. If Sam’s suspicion about the serializer turns out to rest on a bug that was fixed last spring, the correction needs somewhere to go, both to the suspicion and to everything built on it.

Mathematics has the cleanest version of this problem, and recently a very large one. Anthropic’s formalization of Fermat’s Last Theorem began badly. The task, in August 2026, was to make Wiles’s proof checkable by Lean, and early attempts faltered as agents lost track of the project. The successful effort used Prove2Me: theorem statements became nodes in a dependency graph, with plain-language descriptions that let a worker find a result established by a worker it never met. In eleven days the agents produced a formalization using roughly thirty thousand intermediate theorems. Lean checked the completed proof under its three standard axioms; a separate comparator confirmed that the final statement was Mathlib’s Fermat and not a convenient cousin.[6](appendix-references.md#ref-06-fermat)

Jon Doyle was building machinery for this in the late 1970s. In his truth maintenance system, beliefs kept their reasons, and when a reason was withdrawn, everything resting on it came up for review.[7](appendix-references.md#ref-06-doyle) Doyle’s machinery tracks justifications. It cannot check them against the world, and a program can faithfully maintain the consequences of reasons that were never true.

Most of us have no Lean. Here is a claim of the kind my field produces every week, and this one is real. An experiment at Bing reported that people in the treatment were running over ten percent more queries, and revenue per user was up by about thirty percent.[8](appendix-references.md#ref-06-kohavi) That sounds like a result worth keeping. Suppose it goes into a report, another agent summarizes the report, and a third uses the summary to recommend shipping. If something turns out to be wrong with the experiment, where will the correction go?

Searching every document for the word *queries* is one possible response. It will be popular with the company selling us tokens.

A different design gives each claim its own identity and records what it rests on.

| Record | What it says | What a fault in the experiment changes |
|---|---|---|
| Observation | The specified comparison returned more queries and more revenue per user in the treatment. | The record of the result can remain accurate. |
| Measurement assumption | Both arms were produced and logged on comparable terms. | This assumption requires revision or further investigation. |
| Interpretation | People prefer the treatment. | This particular support is weakened; other support must be examined. |
| Success criterion | More queries per user counts as improvement. | Repairing the measurement does not settle whether this is the right criterion. |
| Recommendation | Ship it. | Must be reconsidered if it relied on that interpretation. |

If a fault invalidates an assumption, the assumption changes from *accepted for this analysis* to *withdrawn*, with the reason attached, and a recommendation that has lost what it requires moves from *ready for approval* to *requires review*. Ordinary software can enforce those transitions without pretending to have discovered the fault itself, and a later worker can follow them back to the assumption that caused them.

An LLM-written explanation produced after the fact cannot substitute for a record of what the earlier decision actually used.

If the agent recorded the result and left out the measurement assumption, an automatic correction has no link to follow. Lean can check the formal links in a proof; our graph cannot establish that an agent has recorded every assumption behind a business decision.

From here on I borrow Alexander’s asterisks to mark my confidence that each proposed arrangement can resolve the problem described: two for a well-supported practice, one for a promising proposal that needs further testing, and no asterisk (an unmarked *Therefore*) where its adequacy remains an open question. The marks judge the arrangements; they do not claim that an agent institution has implemented them successfully.

\*\* **Therefore: store the claim with what it rests on, so that a correction has somewhere to go.**

## Commit the Test Before the Result

Every experimentation team knows this meeting. The dashboard arrives before the agreement does. The headline metric is flat, a secondary one is up, and within the hour the secondary metric turns out to be what the experiment was really about. Nobody is lying. The hypothesis has been fitted to the result.

I do not know what was said in the room at Bing. Return instead to our imagined team. Three months into the job, Ines is the reviewer asked to sign off on a new ranking for her market, and it has come back in the Bing shape: queries per user up eight percent, revenue per user up eleven. More queries, more revenue: she can praise the obvious explanation, criticize it, or ask a model to do both. None of that changes the data. To investigate, she has to say what would look different if the explanation were wrong.

Popper’s demand is falsifiability: an empirical claim must risk being wrong. A reviewer who can make every possible result sound like support has arranged to learn nothing from the test.[9](appendix-references.md#ref-06-popper)

Ines proposes setting people a task and watching whether they complete it. Repeated attempts without success would count against the cheerful reading of more queries. The consequences will be partly probabilistic. A noisy result can weaken an explanation without refuting it, and explanations do not always have the courtesy to be mutually exclusive.

Someone suggests breaking the result down by device first. The chart is lovely, and both explanations predict it, so it distinguishes nothing.

A model will propose a distinguishing test plausibly enough if asked. The commitment is stronger when the test goes into the experiment record before the result and the later review checks against it. Experimentation platforms and preregistered trials work this way on paper. Anyone who has sat in the meeting above knows how far practice is from paper.

\*\* **Therefore: write down what would count against the claim before the result arrives, and keep the revision history.**

## Locate the Failure

The people who run experiments for a living have a reflex about results like these. They call it Twyman’s law: any figure that looks interesting or different is usually wrong. Double-digit revenue from a ranking change is very interesting. The first check is whether the two arms even contain the numbers of users the design says they should. A sample-ratio mismatch means something upstream is broken, and the platform should refuse to show the scorecard until somebody finds it.[10](appendix-references.md#ref-06-twyman)

Ines runs the check, and it fails. Her meeting goes something like this. One team says the treatment is fine and the logging double-counted. Another says the logging is fine and a redirect dropped users from one arm. Someone notices the two arms ran on different client versions. We have made contact with reality and acquired a meeting.

Duhem and Quine, from the previous chapter, explained this meeting long before anyone scheduled it. A failed test indicts a whole bundle of assumptions about the world and the apparatus, and does not say which one to blame.[11](appendix-references.md#ref-06-quine)

The dependency record makes the meeting more useful by tracing claims to client versions, data pipelines and what counts as one user, so each suspicion gets a probe: replay a known session, pin the client version, rerun the split.

Ines’s probes find it within a day. One client version sent part of the treatment arm through a redirect that dropped users before logging began. In the table’s terms, the measurement assumption has been withdrawn, and the recommendation to ship has gone back to review without anyone searching for the word *queries*. Once the arms are repaired, most of the revenue gain disappears.

A second measurement may share the same failed dependency. If the supposedly independent check reads a table derived from the original event stream, agreement between the tables supplies less reassurance than their different names suggest. The provenance must reach the common source. Otherwise the institution manufactures a second witness by creating a second spreadsheet.

Capturing every possible dependency would cost more than the inquiry. Start with the support used in the recommendation and let a disputed result send you farther back.

\* **Therefore: when a test fails, trace the assumptions it used and design probes that distinguish the possible failures.**

## Ask What the Number Means

The queries, though, survive the repair. Ines goes looking for anyone who has seen this shape before, and finds Bing’s researchers, who had.

Here is what had happened at Bing. The treatment had a bug, and the bug made the search results worse. People could not find what they wanted, so they searched again, and again. Queries per user went up. With poorer results on the page, the advertisements looked comparatively relevant, and people clicked on them. Revenue went up. Two of the organization’s headline numbers were celebrating an experience that had been degraded.[12](appendix-references.md#ref-06-kohavi2)

The count was right, and the cheerful interpretation was wrong. Another audit of the count would not establish what the extra queries meant; a task-completion test like the one Ines proposed might have. The interpretation had needed its own row in the table all along.

Saussure’s point, which we met in Chapter 4, is relational value: a term means what it does through its differences from its neighbors.[13](appendix-references.md#ref-06-saussure-lectures) *More queries* meant *more engaged* only inside a system where a query was a unit of interest. Set it beside *session* and *task* and it becomes a unit of effort. Seven queries can be worse than two if five of them were spent recovering from a bad ranking.

The Bing researchers made sessions per user a key part of their criterion: help people finish and give them reasons to return. Tasks were harder to identify, so sessions served as a proxy. A shorter session might mean success or abandonment.

Ines does not yet know which story her own queries are telling. Finding out will take most of a year.

\* **Therefore: record what the number is taken to mean as a claim of its own, open to challenge separately from the count.**

## Write the Lesson Down

The next reviewer should not have to rediscover what happened at Bing, or spend a week in Ines’s meeting. Ines writes the lesson down as a candidate pattern, with the reasons and uncertainty kept alongside the instruction:

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

It belongs inside *review-an-experiment* and may call *locate-the-failure*, where Ines’s redirect now lives, rather than every statistical procedure in the building. Like Alexander’s links, those references help a reader choose a method for the difficulty at hand and find an alternative when it fails.

A pattern can also mix kinds of content that need different kinds of support. “Activity can rise because people are struggling” is a claim about the world. “Check this before running an expensive analysis” is a recommendation about effort. “Do not alter the live experiment” is an authority boundary. A successful test of the first does not justify the other two automatically.

Sam could have written something like this about the serializer. Ines’s version has one reader Sam never had to plan for.

## A Reader That Can Act

Alexander’s patterns and the programmers’ patterns both had a human reader. Ines’s file will be read by a machine with tools.

People had tried to give written knowledge to machines before. In 1977, the year of Alexander’s book, Edward Feigenbaum named the attempt knowledge engineering, and found its hardest part in the expert: getting the knowledge out, then making the system handle each exception the expert eventually admitted to.[14](appendix-references.md#ref-06-feigenbaum)

Andrej Karpathy’s count of the ways to program a computer tells what changed. In Software 1.0 a person writes the rules as code; the Gang of Four’s patterns lived there, advice for the human holding the keyboard. In Software 2.0 the program is a set of learned weights, which can absorb what nobody could articulate and offer no convenient place to amend a pattern’s conditions. In Software 3.0 the program is written in a natural language and a model interprets it.[15](appendix-references.md#ref-06-karpathy) The machine doing the work can now read the pattern, follow its *Therefore* and consult the reasons behind it, without every qualification first being translated into logic.

I avoid calling such a document executable, because the word hides the reader: the same words can produce different actions in different models.

Agent skills give the arrangement a container with much of Alexander’s anatomy. A short description says when the skill applies: the context. When selected, it supplies instructions, scripts and examples: the *Therefore*. Calls to other skills serve as links to smaller patterns.[16](appendix-references.md#ref-06-skills)

So Ines puts the lesson in her team’s skill library. Nothing in the format makes the writer include the reasons or the reader act on them. We can repeat the journey from Berkeley: carry the instruction and leave its reasons behind. A library like that can preserve the wrong lesson at industrial speed.

## Put the Library to Work

Ines gives the file to the team’s review agent and asks it to review an experiment. Does it do better?

Bad storage forgets by deletion; bad retrieval forgets by attention. The query “review this experiment” can retrieve a popular checklist and leave the Bing warning untouched on disk. Loading every checklist gives the reviewer the whole office filing cabinet and asks it to find the urgent part. Whether retrieval worked shows up later, in whether the review caught what mattered.

Suppose retrieval works. For two weeks the agent raises the question every time a search experiment reports more activity, and raises it well. Then it starts treating the warning as a verdict. A faster image server increased page views, and a separate task study found that more customers completed their purchases. The agent still recommends holding the release until someone explains away the extra activity. The pattern says `confidence: provisional, one incident`. “Increases in activity are usually fake” is far more than one bug can teach.

To find out, the candidate pattern has to face cases that did not produce it. The reviewer with the pattern and the reviewer without it read the same reports: some with degraded experiences behind the gain, some with real gains, some with too little evidence to say. The comparison keeps the model and tools fixed, repeats runs, and records both the quality of the conclusions and the resources consumed. A curator that warns about metrics in every report has learned how to sound concerned. A generic instruction to be careful can serve as the control. If the elaborate pattern performs no better, its philosophical bibliography does not entitle it to more context.

Repository context files have already faced this kind of comparison. Gloaguen and colleagues’ revised study found no statistically significant gain in task success from either generated or developer-written repository context files over using none. Generated files raised average costs by twenty to twenty-three percent across the two benchmarks.[17](appendix-references.md#ref-06-context)

A lesson that passes should also carry its scope. After a quarter of comparisons, the top of Ines’s file might read:

```yaml
id: ask-what-the-number-means
confidence: supported for search ranking; untested elsewhere
scope: ranking and search experiments reporting activity gains
known_failure: rejected a gain despite independent evidence of task completion
revision: weigh the task evidence before requesting another test
evidence_record: number-meaning-evaluations
```

The next agent can see both where the pattern has been tested and how its predecessor misused it. Nobody had to retrain anything to get there.

\* **Therefore: record how sure we are of each pattern, and make it earn that confidence on cases that did not produce it.**

## Find Where the Result Lives

Ines’s file is a small house, and most of what it rests on lives elsewhere, in a paper by Bing’s researchers, in textbooks on experimentation, in the habits of a field. Where does the knowledge of a result live, if no single agent holds it?

Chapter 5 borrowed Popper’s name for the answer, World 3: the theories, problems and arguments that exist outside any particular head and outlast whoever produced them.[18](appendix-references.md#ref-06-world3)

The ways we preserve and find that knowledge have changed. Clay records, libraries with catalogs, journals with citation indexes: each gave the next worker a different way into what others had learned. The web was built at CERN to help scientists share information; PageRank brought citation analysis to its links. Wikipedia made verifiability and citations work that its editors could demand of one another.[19](appendix-references.md#ref-06-knowledge-web) Easier access did not make the work of checking sources disappear. A language model offers the most convenient entrance yet, the whole library in one voice, but the answer may arrive without a catalog card. The machinery for checking it has to reach this new entrance too. This one is ours to build.

The newest residents arrive through an API. In Terence Tao’s collaboration with DeepMind, AlphaEvolve found a slightly improved construction for three-dimensional finite-field Kakeya sets; Deep Think helped produce an informal proof, and AlphaProof formalized it in Lean.[20](appendix-references.md#ref-06-tao) The AlphaFold database makes more than two hundred million protein-structure predictions available for research, and AlphaGenome Atlas supplies predictions for roughly nine billion possible single-letter DNA changes.[21](appendix-references.md#ref-06-biology) A prediction does not become an observation by being stored beside a billion others, but a researcher can begin with material she could never have produced and put it to a test its creators never planned.

Kevin Buzzard checked Anthropic’s Fermat formalization while leading his own publicly funded project on the same theorem. His commitments included adding useful mathematics to the community library and making a document through which people could explore the modern proof. A completed formalization did not discharge those commitments.[22](appendix-references.md#ref-06-buzzard) A proof can check while leaving the next mathematician with a formidable renovation project.

Suppose Ines’s pattern earns its place. The next difficulty begins when it helps the reviewer identify a bad metric, but the procedure judging the review still rewards that metric. The file tells the agent to question what the institution pays it to accept.

## Change the Representation

Following the Bing lesson, Ines’s agent proposes to organize the next investigation around completed tasks instead of query counts. To do that, a branch has to keep alternative representations as well as alternative answers. It can introduce task-based records, associate them with the old observations where possible, and state where translation fails. The evaluator is part of the difficulty. If it scores every proposal on the old number, the better approach looks worse exactly where it helps people finish sooner. Letting the challenger write an evaluator that declares itself the winner would prove little; the approaches need an explicit dispute about what evaluation is for, then observations both sides accept.

A field can go further and change what its practitioners learn to see as a problem worth solving. Many of my readers worked through one such change.

Before deep learning became dominant, there were several respectable ways to write a machine-learning paper. One began with a probabilistic model of how the data arose, derived the inference and tried to say something about uncertainty. In much of computer vision, people designed features before training a classifier. The architecture of the problem was partly in the heads of the people building it.

In 2012 the AlexNet team won ImageNet with an ensemble of convolutional networks and a top-five error of about fifteen percent. The runner-up, using engineered features, had twenty-six.[23](appendix-references.md#ref-06-imagenet) That gap was legible on the existing scoreboard. What followed changed more than the score: learning the features became central to how much of the field worked. An expert could remain excellent at the old work while watching less of the new work require it.

Kuhn called what a field holds onto in such moments a paradigm. It supplies exemplary achievements, important problems and standards for adequate solutions, and it makes normal science possible because practitioners need not reconstruct the foundations before each experiment.[24](appendix-references.md#ref-06-kuhn) Here the old benchmark helped persuade people to change. The scoreboard survived; the education of the person standing in front of it changed. In this respect AlexNet is the easier case, because the new representation won on the number everyone already trusted. Ines’s case is harder. Her new representation has to argue with the number.

Kuhn also asks us to notice losses. A leap on a benchmark does not tell us what happened to uncertainty, small-data performance or guarantees.

The examples are part of how a paradigm holds. Kuhn’s scientists learn from exemplars that no complete list of explicit rules can replace. I wrote an editing brief for this book after explaining the same corrections to successive agents. One instruction was “preserve the wandering,” which is nearly useless to a reader who has never seen the movement I mean. A before-and-after passage can teach the distinction: one version follows an uncertain thought until it becomes clear; the other announces the conclusion and removes the path that made it convincing. Those examples also carry my taste into the next session. Preserving my judgment and preserving my mistakes used the same file format.

There is no `paradigm_shift()` call. There can be operations for branching a representation, retaining the old interpretation, collecting missing observations, and exposing a disputed standard for decision.

**Therefore: give the branch room to ask a different question, and make it state where its results cannot be translated into the old terms.**

I do not know an agent institution that can do this. The agent can write the proposal into `open_questions`. To answer it, someone has to pay for observations the old records do not contain.

## Separate Use From Investigation

In August 2026 an Anthropic engineer pointed an unreleased Claude at the Riemann hypothesis. It did not prove the hypothesis. On the way, Anthropic reports, it raised a lower bound on the proportion of the zeta function’s nontrivial zeros on the critical line from 41.6 percent to 67.2 percent. Roughly sixty subagents developed and reviewed arguments; mathematicians inside and outside Anthropic examined the paper, and the result was formalized in Lean. Anthropic did not expect the techniques to prove the full hypothesis.[25](appendix-references.md#ref-06-riemann)

An evaluator asking only whether the assigned problem was solved would return *no*. That answer would be correct and a poor account of the research. The record needs room for the contribution: its own statement, support and remaining questions, linked to the unsuccessful attempt that produced it. Whether to fund a follow-up is a separate decision.

Ines’s team faces the small version. The review pattern from the Bing lesson has been in use for six months. It is retrieved for every search experiment, so every review adds a line to its evidence record, and the record looks formidable. The team still uses query-based metrics, with the pattern prompting checks when a gain may be misleading. Ines proposed collecting task-completion data routinely and making it the primary evaluation criterion, while keeping query counts as a diagnostic. That proposal required new instrumentation and a trial. It was never run. Every week the incumbent was the safer choice for the review at hand, and every week that choice was defensible. After six months the system can report an impressive evidence base with almost no comparisons in it.

Larry Laudan called what the team was missing the difference between acceptance and pursuit.[26](appendix-references.md#ref-06-laudan) What to believe today and what to work on tomorrow are different questions. The team had good reasons to keep using the incumbent and no mechanism for asking whether the rival deserved a trial. The Riemann bound raises the same pair of questions. Accepting it as a result does not tell us whether to keep pursuing that route toward the full hypothesis.

Six months of use leaves another trace. The incumbent pattern acquires an exception for one client, then another, then a third. Chapter 5 introduced Lakatos’s patience with a research program; here the patches let us examine what that patience buys.[27](appendix-references.md#ref-06-lakatos) Does a revision predict a failure in a further case that then holds up, or does it merely explain the incident already observed? That distinguishes a progressive program from one that keeps accommodating failures after the fact, and the file should record which it was.

Kitcher’s worry from Chapter 5, about how a community divides its cognitive labor, returns in miniature. A retrieval policy that keeps selecting the incumbent never lets the rival collect evidence.[28](appendix-references.md#ref-06-kitcher)

Ines’s rival needs a small experiment with a price on it and a note saying which later decisions its result would change.

\* **Therefore: give the queue of unrun comparisons its own allocation policy, separate from the policy that selects today’s working method.**

The person recording the reasons for an experiment, however, may not control the money.

## Keep the Funding Decision Visible

OpenAI’s September 2026 account of its Navier–Stokes investigation shows allocation happening at speed. Groups of agents, roughly ten thousand in all, went after the open Millennium Problems. A result on the Euler equations persuaded the researchers to move workers from the other problems to Navier–Stokes, carrying the Euler result and the groups’ findings into the next prompts. About four days after launch, the group produced a proposed proof of finite-time blowup under smooth forcing, addressing Clay’s alternatives C and D; OpenAI reported another seventeen hours for Lean formalization and verification.[29](appendix-references.md#ref-06-navier) On September 11 the Clay Mathematics Institute said the problem appeared to be settled; evaluation and the assignment of credit would follow its deliberately unhurried process.[30](appendix-references.md#ref-06-clay) The other problems had lost workers, not been refuted.

Who deserves credit for the route is now disputed, and the participants’ accounts are in the references.[31](appendix-references.md#ref-06-priority) One detail belongs here. The rumor that started OpenAI’s search concerned concurrent work by Tristan Buckmaster and Levent Alpöge, whom OpenAI describes as an Anthropic employee, produced partly with an internal Anthropic model. This book relies on Anthropic’s reports in several chapters, so that belongs in the record too.

A checked proof does not settle that history. Learning that a route is promising can affect where we invest without supplying a single step of the proof.

Ines has a smaller allocation problem. She asks for two weeks of experimental traffic to test whether query counts track task completion at all. The request lands with the owner of the search-quality budget, who funds experiments expected to raise the current metric. The proposed study asks whether the metric represents improvement. Ines has been invited to challenge an assumption on the condition that she first accept it. The budget owner is polite, senior and entirely right about what the budget was approved to do. She leaves the meeting having agreed with everything he said and received nothing she asked for.

The budget owner controls the traffic, the compute and the permission to change what gets measured.

So Ines splits the request. One part proposes a study and goes to experimental review, which funds it. The other asks whether the success criterion should change and goes to whoever owns the product goal. It is declined, and the rejection is recorded as a decision about the goal, with a name on it. At least the no has an address.

An agent with a sound epistemic objection still has no authority to spend somebody else’s money. A funding policy can reserve capacity for challenges to the incumbent, but that policy is itself a choice made by people with power; written into code, it can at least be inspected.

\* **Therefore: attach the funding decision and its reason to the question it left unanswered.**

Otherwise *unfunded* gradually becomes *unsupported*, and *unsupported* becomes *disproved* somewhere between the database and the executive summary.

## Give the Objection a Consequence

The study runs, and the objection holds up. On Ines’s surfaces, query counts track completed tasks poorly. Some of her queries had been rising for a reason Bing’s researchers would have recognized. After retrieving the lesson, testing it and paying for the evidence it asked for, the organization can still arrange for nothing to follow.

For years Facebook tuned its feed for engagement and time spent. In December 2017, Facebook’s researchers publicly reviewed evidence that passive consumption could leave people feeling worse.[32](appendix-references.md#ref-06-fbwellbeing) A person could keep scrolling without becoming better off. It was Bing’s question again, except that the activity being counted was now hours of people’s lives.

In January 2018 the company announced a change toward “meaningful social interactions,” favoring conversations and exchanges among friends and family. It looked like the right fix: move from measuring attention to measuring connection. Facebook even said it expected people to spend less time on the platform.[33](appendix-references.md#ref-06-fbchange)

Then its researchers found publishers and political parties shifting toward outrage because that was what traveled. According to internal documents reported by the *Wall Street Journal*, heavy weighting of reshared material amplified angry voices, and researchers found misinformation, toxicity and violent content unusually common among reshares. They proposed reducing the boost for material likely to travel down long chains of users. Facebook made some changes for civic and health content, but Zuckerberg reportedly resisted expanding them if doing so materially reduced the interaction metric.[34](appendix-references.md#ref-06-fbfiles)

The same reporting described researchers inside Instagram struggling to get colleagues to appreciate the gravity of their findings. One former researcher put the institutional problem rather precisely: “We’re standing directly between people and their bonuses.”[35](appendix-references.md#ref-06-instagram)

The organization had paid for the knowledge it was now resisting. Having findings on the company’s message board did not give its own researchers authority over what followed, and the public learned of the dispute through leaked documents.

A response to an objection should identify the claim it challenges and say what happened to it: new evidence, a revised claim, another experiment, a reason the criticism does not apply, or a budget decision that left it open. *Closed* says only that somebody stopped typing. “Noted” is none of these. With agents it gets cheaper still: a reviewer objects, the builder replies that the concern has been noted, both complete their tasks, and the report goes out. We have successfully parallelized the experience of being ignored.

Helen Longino would locate that failure in the community. On her account, objectivity belongs to a community’s criticism, and depends on venues for it, uptake, shared standards and a tempered equality of intellectual authority.[36](appendix-references.md#ref-06-longino) The review channel provides a venue. “Noted” gives no account of how the objection entered the decision.

Stellar Colosseum, a harness for mathematical research, gives uptake a concrete form. Agents develop proposed arguments while reviewers look for defects. The objections travel with the proposals as other agents combine them into a longer argument. At the final review, a specific fatal flaw is enough to reject the proof; favorable verdicts from other reviewers cannot cancel it. The defect is tied to the claim that failed, so the next round can repair it or try another route.[37](appendix-references.md#ref-06-colosseum) Failed drafts remain available with their reviews attached. The reviewers can still be wrong.

It also matters who gets to object. A critic who receives only the conclusion cannot examine the assumption. Asking the same model to play the skeptic may elicit another argument, but the role prompt alone does not give it different observations. And some disputes were never about evidence.

A product owner may reasonably care about revenue while a researcher studies harm; both can be reliable observers who want different decisions. The system should be able to say which dispute the next experiment can settle and which requires a decision about purpose. Otherwise it will keep requesting evidence to avoid naming a conflict over what matters.

A year after Ines opened it, her file has grown fields nobody would have put in the first version:

```yaml
open_questions:
  - Does the activity-metric check help outside search?   # unfunded
funding:
  - task-completion study: funded through experimental review
  - make task completion the success criterion: declined by product-goal owner
objections:
  - claim: More queries per user counts as improvement.
    evidence: The study found a weak link to task completion.
    status: unresolved
    decision: Continue using the query metric.
    owner: head of search product
    reason: Task completion has not yet been measured reliably across all markets.
```

An `open_questions` field that no decision ever consults is a decorative conscience. These lines matter when the next review follows them, notices that the evidence concerns another surface or another tool version, and changes what it is prepared to conclude.

\* **Therefore: if the organization proceeds with an objection unresolved, the objection travels with the decision, and the decision-maker owns that choice in writing.**

The objection can now survive its author. So can the assumption it challenges. Replace every agent in the institution and the same dispute may begin again, with the same side already winning.

## Test What the Next Agent Inherits

Max Planck’s observation about scientific change, now known as Planck’s principle, is usually compressed into “science advances one funeral at a time.” His actual sentence describes a new truth gaining acceptance because, rather than all its opponents being persuaded,

> “…its opponents eventually die, and a new generation grows up that is familiar with it.”[38](appendix-references.md#ref-06-planck)

A new generation learns the new examples first and has no old allegiance to surrender. The remark is bleak because the mechanism of correction lies partly outside the argument. What changes with the occupant of the chair?

There is empirical work on that question. Studying the premature deaths of eminent life scientists, Pierre Azoulay, Christian Fons-Rosen, and Joshua Graff Zivin found declining contributions from collaborators and increased contributions from outsiders to the affected fields. The incoming work drew on a different scientific corpus and was disproportionately likely to be highly cited.[39](appendix-references.md#ref-06-funerals) None of that shows the departed scientists were wrong, only that who gets to participate can change which work enters a field.

Sam, eventually, moves to another team. Nothing about his leaving changes what the file says.

Now imagine a new agent joining Ines’s project. Its progress file contains a line Sam wrote two years ago: *serializer rewrite tried and abandoned; do not retry.* The line was true when written. The dependency that made the rewrite fail has since been replaced, and the reason for the warning went with it. The new agent reads the same file, retrieves the same successful patterns, accepts the same categories, and is scored by the same evaluator. Its predecessors have disappeared, but their commitments have been transferred intact. The next generation can be born with the old generation’s entire syllabus already in context. Session turnover is not a funeral; nothing that was believed has died.

In that file the durable incumbent is a single sentence. Elsewhere it may be a retrieval preference, a canonical example, a benchmark, or a rule giving one branch first access to compute. A more capable replacement model may defend it more effectively.

Deleting old knowledge on a schedule would discard expertise along with the errors and make newness another unearned source of authority. The new agent needs permission to suspend a disputed instruction like that one on an experimental branch, within its budgets and permissions, and a comparison whose terms are open to challenge. If no comparison can decide the issue, that belongs in the record too.

Changing the worker is easy.

**Therefore: change what the next worker inherits.**

## Put the Procedure Under Test

Look back at what this chapter has built and ask how it could fail while every part works. It may faithfully preserve dependencies while omitting the important kind of dependency. It may compare candidate patterns on cases selected by the incumbent pattern. It may require evidence for an alternative while refusing the instruments needed to produce that evidence. Every individual operation can function as specified while the arrangement prevents the question that would matter.

Feyerabend’s *Against Method* goes further. Every rule of method, he argued, has been usefully broken at some point in the history of science.[40](appendix-references.md#ref-06-feyerabend) Requiring a test before setting a rule aside would itself be another methodological rule. I am borrowing a smaller lesson: our procedures need room for investigations they would ordinarily exclude.

Some of these failures can be investigated through a relevant comparison. A retrieval policy can be evaluated against another policy. A reviewer can be compared with a reviewer given different evidence. A pattern can be withheld from a branch to see whether its absence reveals errors its presence concealed.

Other disputes reach the purpose or authority of the system. Whether a feed should be ranked for activity or for something harder to count cannot be settled by letting whichever evaluator produces the higher score appoint itself. Someone still has to make and own the decision about which consequences matter.

Alexander’s form now asks for a *Therefore*. We could write “revise the method when it fails.” But the method decides which failures count. The next chapter has to open that loop.

## What the File Says Now

We have seen pieces of this language at work: shared proof graphs, experiments that challenge their own metrics, reviews that travel with failed arguments. I have not shown an agent institution that composes all of them, keeps their reasons alive, and changes its own way of seeing when those reasons fail. That is the ambition, and it still has to earn its confidence marks.

Two years after that night, Ines opens the incident file again. It says what Sam looks for in the serializer, why he looks there, the two times that suspicion was wrong, and who disagreed. She can use his judgment without having to inherit it whole. Alexander wanted the family to be able to argue with the architect. Now the next worker can argue with Sam, even while Sam is on holiday.

Further down the runbook, a newer engineer has written *ask Ines*. This time there is a file behind the name.

So far, a procedure has decided which changes to the file deserve to survive. But that procedure is also software.

What happens when the next agent proposes to rewrite it?

---

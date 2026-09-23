# Chapter 6: Pattern Language

*When Knowledge Becomes Software*

Pattern 159 is called Light on Two Sides of Every Room. It says that when people have a choice, they drift toward rooms with windows on two walls and leave the one-window rooms empty. Light from a single side glares. It flattens the faces across the table, so you cannot read them. Think of the rooms you have loved and count their windows.

Pattern 88 is Street Café: a place to sit lazily, legitimately, on view, and watch the street go by. Pattern 180 says everybody loves a window seat. Pattern 167 says a balcony less than six feet deep will hardly ever be used, because nobody can pull a chair up to a table on it. You have seen those balconies. They hold a bicycle and a dead plant. Pattern 203 is Child Caves: children love tiny, cave-like places, so build them some. Pattern 251 is Different Chairs: people come in different sizes and sit in different ways, so never furnish a room with identical chairs. Pattern 252, Pools of Light, says that even lighting kills a room, because people gather where the light pools. The last one, 253, is Things from Your Life: put on your walls what matters to you and ignore what a decorator says belongs there.

There are 253 of them. The first is about how the world should be divided into regions. The last is about the photographs above your desk. In between come neighborhoods and bus stops, beer halls, stairs you can sit on, a bench by the front door. Christopher Alexander and five colleagues at Berkeley published the book in 1977. It runs past eleven hundred pages on Bible paper, and it has probably been read by more programmers than architects.

Reading it is a strange experience. You keep recognizing things you have always known and never said. Alexander believed that some places are alive and some are dead, that everybody can feel the difference, and that the difference has no adequate name. He called it the quality without a name. He had trained as a mathematician at Cambridge before taking the first doctorate in architecture Harvard ever awarded, and he went after the unnameable quality the way a mathematician would. He broke it into problems small enough to state, and he stated them so that they could be wrong.

That is the magic of the form. Every pattern has the same anatomy. A name you can say in a meeting. A photograph. The context: which larger patterns this one helps complete. The problem, in bold, stated as forces pulling against each other. The evidence and the argument. Then the word *Therefore*, and the arrangement that resolves the forces, also in bold. Then the smaller patterns that complete this one. Every page is linked to the pages above and below it. It was hypertext in 1977.

And every pattern carries a confidence mark. Two asterisks mean the authors believe they have found something close to an invariant. One means they have made progress and expect a better answer. None means they know they have not solved it and are telling you so. They say outright that the patterns are hypotheses: does the problem occur as described, and does the arrangement resolve it?[^alexander] You can test Light on Two Sides by walking through an office at four in the afternoon and seeing where people are.

He meant it politically, too. The language was supposed to take design away from professionals and hand it back to the people who would live in the rooms. A family with the book could lay out its own house and argue with the architect in the architect's terms.

That is a **pattern language**: what master builders knew and could not say, written down with its reasons, its conditions, its confidence and its connections.

## The Pattern Goes to Work

In 1987 two programmers, Kent Beck and Ward Cunningham, were helping a group at Tektronix that could not get a user interface designed. Both had read Alexander. They wrote five small patterns, with names like Window Per Task and Short Menus, handed them to the people who would use the system, and let those people do the design. It worked well enough that they reported it at a workshop that autumn.[^beck]

The idea travelled the way Alexander's book travels, from hand to hand. In 1993 a group of programmers met on a hillside in Colorado to work out how software patterns should be written, and called themselves the Hillside Group. The next year four of their circle published *Design Patterns*: twenty-three named arrangements for object-oriented code, with Alexander quoted in its opening pages.[^gof] A generation of engineers learned to say Observer, Factory and Singleton the way builders say lintel. A design review could now be held in nouns.

In 1995 Cunningham needed somewhere for programmers to collect and edit patterns together, so he wrote a small program that let any reader change any page. He called it WikiWikiWeb. The wiki was invented to hold a pattern language.[^wiki] Six years later an encyclopedia borrowed the idea. Around the same time Will Wright, who had been reading Alexander, turned an architecture toy into *The Sims*. A book about window seats had reached the design of software, the largest reference work ever written, and one of the best-selling computer games.

Look at what was easiest to carry. The names arrived. The catalogue arrived. The books still described contexts and trade-offs, but you could say Singleton in a meeting without bringing any of those along. A pattern had been a hypothesis about when an arrangement resolves a conflict. In use, it could become a thing good engineers were seen to use.

<!-- SLOT 3 (your story replaces the next paragraph): a design pattern you watched being applied as a rule. -->
Anyone who worked through those years has seen what followed. Codebases filled with factories that built one kind of object and singletons guarding nothing. “Never use regex on nested syntax” belongs to the same family. It has the reassuring shape of wisdom and the inconvenient property of being false: a fixed format with one level of nesting can be matched with a regular expression perfectly well. The useful pattern records when a parser becomes cheaper than maintaining an increasingly heroic expression at two in the morning. The conditions are part of what we learned, and the conditions are what the rule threw away.

In 1996 the programmers invited Alexander to give the keynote at their largest conference. He came, a little bemused to find himself famous in a field he did not work in, and he was gracious, and he was not sure they had taken what mattered. He asked whether their patterns carried the two things his were for: making something better for the people who live in it, and generating coherent wholes rather than collecting good parts. He suspected they had mostly adopted a format for trading ideas.[^alexander96]

## Ask Sam

Now leave Berkeley and sit at a new engineer's desk.

She can know Python, distributed systems, and the collected technical culture of the internet while remaining spectacularly unqualified to deploy your company's software. She does not know which apparently redundant check protects an old customer integration, which dashboard changes meaning during failover, or why the elegant migration in the wiki was abandoned halfway through. Much of her first month consists of discovering the reasons behind things that look stupid.

Ask for the incident procedure and the answer sounds like this:

> Start with the dependency graph, unless the spike began exactly at deployment. If only one market is affected, check the traffic split before touching the database. And if it started after Tuesday's migration, ask Sam. There is a thing with the old serializer.

She writes down *ask Sam*. That preserves the dependency beautifully. It does less for the incident that happens while Sam is on holiday. She needs to know what he looks for in the serializer, why he looks there, and when that suspicion is a waste of time. Sam is a master builder who knows more than he can say, and nobody has written his patterns down.

Carlini's compiler project depended on this kind of transfer. Its workers inherited code, tests, progress files, and procedures. The institution had taken shape around failures; its next workers needed to inherit what those failures had taught it. Now we have to open the files. What, exactly, should the institution leave inside them?

If the file only says what we decided, the next worker inherits our mistakes. If it says why, she can find them.

## A Reader That Can Act

Alexander's patterns and the programmers' patterns both had a human reader. The third life gives the pattern a machine reader with tools.

People had tried to give written knowledge to a machine before. In 1977, the same year as Alexander's book, Edward Feigenbaum gave the attempt a name, **knowledge engineering**: acquiring expert knowledge, representing it, and using it to construct and explain reasoning. He argued that a system's power lies in its knowledge, and he found that the hard part is getting that knowledge out of the expert. In one diagnostic system, rules developed with a physician were tested against cases, exposing gaps and inconsistencies the collaboration then had to resolve.[^feigenbaum] The machine needed the knowledge in a form its reasoning machinery could use. Getting the expert to explain the exception was only the beginning; someone still had to make the system handle it.

Andrej Karpathy's count of the ways to program a computer tells the rest. In Software 1.0 a person writes the rules as code. That is where the Gang of Four's patterns lived: advice for the human holding the keyboard, invisible to the machine. In Software 2.0 the program is a set of weights learned from examples. It can absorb what nobody could articulate, but there is no convenient place in the weights to inspect a pattern and amend its conditions. In Software 3.0 the program is written in a natural language and a model interprets it.[^karpathy] The pattern itself, with its context, its reasons and its *Therefore*, can now guide the machine doing the work.

That changes the cost of Feigenbaum's translation. We can supply an account of how a problem usually unfolds, with a worked example and a warning about a misleading instrument, without first expressing every qualification in logic. The model contributes the interpretation. Code still performs the operations for which precise execution matters. A model reads the incident procedure, chooses a diagnostic query, and hands arithmetic to code. Nobody benefits if the arithmetic becomes more literary.

That arrangement needs a name less magical than “the document is executable.” A document influences work when something selects it, interprets it, and acts on it. The same words can produce different actions in different models or environments. A knowledge artifact belongs to a working arrangement: the material, the interpreter, the tools, and the conditions of use.

Agent skills give the arrangement a container, and the container has Alexander's anatomy. A skill has a name. It has a short description used for discovery, which says when the skill applies: the context. It has instructions, scripts and examples loaded when needed: the *Therefore*. It can call other skills: the links to smaller patterns.[^skills] Voyager, a Minecraft agent, showed capability accumulating this way. It keeps a library of executable skills, retrieves them through their descriptions and reuses them, with execution results and model-based verification supplying feedback.[^voyager] The next attempt can begin with something the previous one learned.

For an organization the possibility is attractive. The model can change while the local operating knowledge survives. A procedure can improve without waiting for a training run. A specialist can leave behind more than completed tasks.

Now look at what the format does not require. How sure are we? Where did the pattern come from? What would show it to be wrong, and who disagreed? A skill file can hold all of that. Nothing in the format makes the writer include it or the reader act on it. We can repeat the journey from Berkeley: carry the instruction and leave its reasons behind. A library like that can preserve the wrong lesson at industrial speed.

## Give the Claim an Address

Anthropic's formalization of Fermat's Last Theorem began badly. Wiles proved the theorem in 1995; the task in August 2026 was to make the proof checkable by Lean. Early attempts faltered as agents lost track of the project. The successful effort used Prove2Me: theorem statements became nodes in a dependency graph, with plain-language descriptions that let a worker find a result established by a worker it never met. In eleven days the agents produced a formalization using roughly thirty thousand intermediate theorems. Lean checked the completed proof under its three standard axioms; a separate comparator confirmed that the final statement was Mathlib's Fermat and not a convenient cousin.[^fermat]

The graph gave a worker somewhere to begin without understanding the whole project. It gave the next worker something better than a colleague's assurance that the mathematics was probably fine.

Jon Doyle was designing machinery for this long before language models. He called it **truth maintenance**: beliefs keep their reasons, and when a reason is withdrawn, everything resting on it comes up for review.[^doyle] The name should be read carefully. A program can maintain the consequences of its stated reasons without those reasons corresponding to reality. The graph does not acquire a laboratory by being called a truth-maintenance system.

Most of us have no Lean. Here is a claim of the kind my field produces every week, and this one is real. An experiment at Bing reported that people in the treatment were running over ten percent more queries, and revenue per user was up by about thirty percent.[^kohavi] That sounds like a result worth keeping. Suppose it goes into a report, another agent summarizes the report, and a third uses the summary to recommend shipping. If something turns out to be wrong with the experiment, where will the correction go?

Searching every document for the word *queries* is one possible response. It will be popular with the company selling us tokens.

A different design gives each claim its own identity and records what it rests on.

| Record | What it says | What a fault in the experiment changes |
|---|---|---|
| Observation | The specified comparison returned more queries and more revenue per user in the treatment. | The record of the result can remain accurate. |
| Measurement assumption | Both arms were produced and logged on comparable terms. | This assumption requires revision or further investigation. |
| Interpretation | People prefer the treatment. | This particular support is weakened; other support must be examined. |
| Success criterion | More queries per user counts as improvement. | Repairing the measurement does not settle whether this is the right criterion. |
| Recommendation | Ship it. | Must be reconsidered if it relied on that interpretation. |

A misleading measurement does not make the historical result disappear. Losing one supporting argument does not establish the opposite conclusion, either. If a fault invalidates an assumption, that assumption changes from *accepted for this analysis* to *withdrawn*, with the reason attached. The system checks the remaining support. A recommendation that has lost what it requires moves from *ready for approval* to *requires review*. The old recommendation can no longer silently present itself as current. Ordinary software can enforce those transitions without pretending to have discovered the fault itself.

The history stays attached. A later worker asking why the recommendation was suspended reaches the observation and assumption that caused it. An LLM-written explanation produced after the fact may be helpful, but it cannot substitute for a record of what the earlier decision actually used.

Suppose the agent recorded the result and left out the measurement assumption. Then an automatic correction has no link to follow. Someone has to discover the missing dependency. Lean can check the formal links in a proof; our graph cannot establish that an agent has recorded every assumption behind a business decision.

**Therefore: store the claim with what it rests on, so that a correction has somewhere to go.** This is one answer to Chapter 4's question about what should survive a session. Some answers should survive with their reasons, so the institution can change its mind without having to rediscover everywhere the old mind went.

## Commit the Test Before the Result

<!-- SLOT 1 (your story replaces the next paragraph): an experiment whose meaning was decided after the result came in. -->
Every experimentation team knows this meeting. The dashboard arrives before the agreement does. The headline metric is flat, a secondary one is up, and within the hour the secondary metric turns out to be what the experiment was really about. Nobody is lying. The hypothesis has been fitted to the result.

I do not know what was said in the room at Bing, so take what follows as the general case. A result like theirs is an invitation to the same meeting. More queries, more revenue: a reviewer can praise the obvious explanation, criticize it, or ask another model to do both. None of that changes the data. To investigate, it has to say what would look different if the explanation were wrong.

Popper's demand is **falsifiability**: an empirical claim must risk being wrong. A reviewer who can make every possible result sound like support has arranged to learn nothing from the test.[^popper]

What if we set a task and observed whether people completed it? Repeated attempts without success would count against the cheerful reading of more queries. Later return visits could add evidence, though habit and alternatives matter there too. We have a test to design, and a reason for collecting something the headline omitted.

A test request needs more than a question in English. It needs the alternatives it is meant to distinguish, the observation to collect, the conditions under which that observation has meaning, and what each outcome would do to the current interpretation. Some of those consequences are probabilistic. A noisy result can weaken an explanation without refuting it, and explanations do not always have the courtesy to be mutually exclusive.

Asking the same dashboard for another chart may produce an attractive restatement of the original evidence. If both explanations predict the chart, it distinguishes nothing. Which live disagreement would the proposed observation resolve?

A model will answer that question plausibly in a prompt. The operational commitment is stronger: the answer becomes part of the experiment record, written before the result, and the later review checks what happened against it. A prediction revised after observation remains visible as a revision. Experimentation platforms and preregistered trials work this way on paper. Anyone who has sat in the meeting above knows how far practice is from paper.

**Therefore: write down what would count against the claim before the result arrives, and keep the revision history.** The institution does not have to remember an investigator's intentions. It can inspect what was committed to the record.

## Locate the Failure

The people who run experiments for a living have a reflex about results like Bing's. They call it Twyman's law: any figure that looks interesting or different is usually wrong. Thirty percent more revenue is very interesting. The first check is whether the two arms even contain the numbers of users the design says they should. A sample-ratio mismatch means something upstream is broken, and the platform should refuse to show the scorecard until somebody finds it.[^twyman]

In a case like this the meeting goes roughly as follows; I am describing the genre, not Bing's minutes. One team says the treatment is fine and the logging double-counted. Another says the logging is fine and a redirect dropped users from one arm. Someone notices the two arms ran on different client versions. We have made contact with reality and acquired a meeting.

This is the **Duhem–Quine** problem from the previous chapter: the test challenges a bundle of assumptions about the world and the apparatus without identifying which one failed.[^quine] Hence the meeting.

The dependency record makes the meeting more useful. It shows which claim depended on which version, which pipeline, and which assumption about what counts as one user. Each of those is a candidate, and each suggests a probe that attacks one ambiguity: replay a known session and count the events, pin the client version, rerun the split.

One detail is easy to miss. A second measurement may share the same failed dependency. If the supposedly independent check reads a table derived from the original event stream, agreement between the tables supplies less reassurance than their different names suggest. The provenance must reach the common source. Otherwise the institution manufactures a second witness by creating a second spreadsheet.

Capturing every possible dependency would cost more than the inquiry. Start with the support used in the recommendation and let a disputed result send you farther back. A missing dependency can still defeat the investigation; recording what was traced makes the gap easier to find next time.

**Therefore: when a test fails, trace the assumptions it used and design probes that distinguish the possible failures.** A single counter called *harmful* cannot express which of them broke.

## Ask What the Number Means

Here is what had happened at Bing. The treatment had a bug, and the bug made the search results worse. People could not find what they wanted, so they searched again, and again. Queries per user went up. With poorer results on the page, the advertisements looked comparatively relevant, and people clicked on them. Revenue went up. Two of the organization's headline numbers were celebrating an experience that had been degraded.[^kohavi2]

The count was right. The cheerful interpretation was wrong. The task-completion test we proposed could have exposed the problem; another audit of the count would not. We had given the interpretation its own address. Now we know why it needed one.

Saussure's point, which we met in Chapter 4, is **relational value**: a term means what it does through its differences from its neighbors.[^saussure-lectures] *More queries* meant *more engaged* only inside a system where a query was a unit of interest. Set it beside *session* and *task* and it becomes a unit of effort. Seven queries can be worse than two if five of them were spent recovering from a bad ranking.

The Bing researchers made sessions per user a key part of their criterion: help people finish and give them reasons to return. Tasks were harder to identify, so sessions served as a proxy. That distinction matters. A shorter session might mean success or abandonment. The new measure still needed an argument; a better name did not supply one.

A system capable of this move has to keep alternative representations, not only alternative answers. A branch can introduce task-based records, associate them with the old observations where possible, and state where translation fails. The evaluator is part of the difficulty: if it scores every proposal on the old number, the better approach looks worse exactly where it helps people finish sooner. Letting the challenger write an evaluator that declares itself the winner would prove little. We need an explicit dispute about what the evaluation is for, followed by agreed observations on which the approaches can be compared.

**Therefore: record what the number is taken to mean as a claim of its own, open to challenge separately from the count.** The interpretation and the success criterion each had a row in our table. A number can be correct while the decision it recommends is wrong.

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

The links carry knowledge too. This pattern belongs inside *review-an-experiment* and may call *locate-the-failure*. It should not call on every statistical procedure in the building. Which method helps with which difficulty, which methods are alternatives, and which preconditions must hold before a method makes sense: that is what Alexander's links were for.

A pattern can also mix kinds of content that need different kinds of support. “Activity can rise because people are struggling” is a claim about the world. “Check this before running an expensive analysis” is a recommendation about effort. “Do not alter the live experiment” is an authority boundary. A successful test of the first does not justify the other two automatically.

The field names do not carry the epistemology. The processes that read and update them do. An `open_questions` field that no decision ever consults is a decorative conscience. A link to evidence matters when the system follows it, notices that the evidence concerns another tool version, and changes what it is prepared to conclude.

## Change the Representation

Bing could change what its metric stood for while keeping the business of search recognizable. A field can move further: change what its practitioners learn to see as a problem worth solving. Many of my readers worked through one such change.

Before deep learning became dominant, there were several respectable ways to write a machine-learning paper. One began with a probabilistic model of how the data arose, derived the inference and tried to say something about uncertainty. In much of computer vision, people designed features before training a classifier. The architecture of the problem was partly in the heads of the people building it.

In 2012 the AlexNet team won ImageNet with an ensemble of convolutional networks and a top-five error of about fifteen percent. The runner-up, using engineered features, had twenty-six.[^imagenet] That gap was legible on the existing scoreboard. What followed changed more than the score: learning the features became central to how much of the field worked. An expert could remain excellent at the old work while watching less of the new work require it.

<!-- SLOT 2 (your first-person moment goes here): what you believed before, and the result that changed your mind. -->

Kuhn gives us a way to examine the larger change: a **paradigm** supplies a field with exemplary achievements, important problems and standards for adequate solutions. It makes normal science possible because practitioners need not reconstruct the foundations before each experiment.[^kuhn] Here the old benchmark helped persuade people to change. The scoreboard survived; the education of the person standing in front of it changed. The result reached the syllabus, the tools and the problems a new student would consider worth a career.

Kuhn also asks us to notice losses. A leap on a benchmark does not tell us what happened to uncertainty, small-data performance or guarantees. Those questions survive even when the fashionable result no longer has to answer them. Prompting a general model shifts the work again: some choices once made in a training pipeline move into instructions and tools.

The examples are part of how a paradigm holds. Kuhn's scientists learn from exemplars that no complete list of explicit rules can replace. I wrote an editing brief for this book after explaining the same corrections to successive agents. One instruction was “preserve the wandering,” which is nearly useless to a reader who has never seen the movement I mean. A before-and-after passage can teach the distinction: one version follows an uncertain thought until it becomes clear; the other announces the conclusion and removes the path that made it convincing. Both can contain long paragraphs. Measuring their length would miss what the examples are there to teach. Those examples also carry my taste into the next session. Preserving my judgment and preserving my mistakes used the same file format.

There is no `paradigm_shift()` call. There can be operations for branching a representation, retaining the old interpretation, collecting missing observations, and exposing a disputed standard for decision. Those operations make a change possible. They do not guarantee that it is wise.

**Therefore: keep a branch where the question itself is different, and state where it cannot be translated into the old one.** I do not know an agent institution that can do this.

And possibilities require funding.

## Separate Use from Investigation

In August 2026 an Anthropic engineer pointed an unreleased Claude at the Riemann hypothesis. It did not prove the hypothesis. On the way, Anthropic reports, it raised a lower bound on the proportion of the zeta function's nontrivial zeros on the critical line from 41.6 percent to 67.2 percent, combining published results. Roughly sixty subagents developed and reviewed arguments. Two Anthropic mathematicians checked the paper, two outside number theorists examined it, and the result was formalized in Lean. Anthropic did not expect the techniques to prove the full hypothesis.[^riemann]

An evaluator asking only whether the assigned problem was solved would return *no*. That answer would be correct and a poor account of the research. The record needs room for the contribution: its own statement, support and remaining questions, linked to the unsuccessful attempt that produced it. Whether to fund a follow-up is another decision. The original ambition neither proves the byproduct valuable nor makes it worthless when the ambition fails.

Laudan's distinction is **acceptance versus pursuit**: what to believe today and what to work on tomorrow are different questions. An approach can be the one we presently have most reason to work with while another deserves investigation because of the problems it may solve.[^laudan] A team can have good reasons to keep its current model in production and equally good reasons to fund the approach that might replace it.

Lakatos adds a way to judge a **research programme** over time, by its patches. A programme is progressive if its modifications predict something new, and degenerating if they only excuse the last failure.[^lakatos] The test applies to a file as well as to a field. Suppose a measurement pattern acquires an exception for one client, then another, then a third. Does each revision identify a recurring cause and work on further cases, or does it merely excuse the latest incident? The number of exceptions alone tells us little. A complicated world can require a complicated method.

If use and investigation are driven by the same score, the best-supported approach acquires a monopoly on becoming better supported. A new task retrieves the incumbent pattern because it has the strongest record. Successful applications add to that record. The alternative receives little use, so it accumulates little evidence. After a while the system has a large collection of observations about the incumbent and very few comparisons. It can accurately report the size of its evidence base while misleading itself about what that evidence establishes.

Kitcher's **division of cognitive labor** makes the collective stakes explicit. Choices that are sensible for each investigator can add up to a badly diversified community.[^kitcher] We cannot solve that by instructing every agent to pursue its most promising idea independently when all of them inherit the same ranking of ideas.

Nor does protecting alternatives mean funding every objection forever. An alternative can receive a bounded experiment whose outcome determines the next decision. What would it teach us, what does it cost, and which later choices could it change?

**Therefore: keep one policy for what to use today and another for what to investigate, and keep a queue of comparisons nobody has run yet.** Those are reasons for an allocation, recorded where they can be challenged.

But the person recording these reasons may not be the person who controls the money.

## Keep the Funding Decision Visible

OpenAI's account of its Navier–Stokes proof shows a promising result changing the allocation. Groups of agents investigated the open Millennium Problems. A result on the Euler equations persuaded the researchers to move workers from the other problems to Navier–Stokes, carrying the Euler result and the groups' findings into the next prompts. About four days after launch, the group produced a proposed proof of finite-time blowup under smooth forcing, addressing Clay's alternatives C and D. Lean formalization and verification took another seventeen hours.[^navier]

On September 11 the Clay Mathematics Institute said the problem appeared to be settled; evaluation and the assignment of credit would follow its deliberately unhurried process.[^clay] Three events, not one: a decision to invest, a proof checked, a verdict pending. A success in one investigation had changed who could afford to keep investigating elsewhere. The other problems had lost workers, not been refuted.

The history of choosing the route also became disputed. Tristan Buckmaster described his work with Levent Alpöge as extending a programme begun by Diego Córdoba and Luis Martínez-Zoroa. He challenged the presentation of OpenAI's effort while explicitly saying he did not know whether their data had been used. OpenAI acknowledged that a rumor of concurrent work prompted its investigation and denied accessing their unpublished work or using Buckmaster's recent Codex prompts to train the system.[^priority] By OpenAI’s own account, the rumor traced to Buckmaster and to Alpöge, whom it describes as an Anthropic employee. Their concurrent result, on the forced Euler problem, had been produced with an internal Anthropic model. This book relies on Anthropic’s reports in several chapters, so that belongs in the record too.

A checked proof does not settle that history. Learning that a route is promising can affect where we invest without supplying a single step of the proof. The provenance of a proof and the provenance of the decision to pursue it answer different questions.

The other programmes did not get an equal chance to become the next promising result. The money is part of the evidence story. Power enters scientific work through the ability to commission observations, supply instruments, define acceptable problems, and sustain a programme through unproductive intervals. Harari's history of the Scientific Revolution makes the outside view blunt: science does not set its own priorities; whoever pays for it does.[^harari] In an agent system, the equivalents include tool access, compute budgets, experimental traffic, data collection, and permission to change what gets measured. These are parts of the inquiry even when they appear in another team's configuration.

A record that compresses this into “the other problems were less tractable” has hidden a decision about power inside a statement about knowledge. Nothing in the scene requires dishonesty. The researchers had good reasons for moving their workers, but the questions left behind remained unanswered. Resource decisions help produce the evidential situation on which the next resource decision will rely.

Control over evaluation adds another layer. Suppose the budget owner accepts only experiments that predict a higher value of the current metric, and the proposed study concerns whether that metric represents improvement. The researcher has been invited to challenge an assumption on the condition that she first accept it. So the request is split. One part proposes a study and goes to experimental review. The other asks whether the success criterion should change and goes to whoever owns the product goal. A rejection of the second is recorded as a decision about the goal. It cannot be counted as a failed test of the alternative.

Giving an agent an epistemic objection does not authorize it to spend somebody else's money. A funding policy can reserve capacity for challenges to the incumbent, but that policy is itself a choice made by people with power. Putting it in code makes it enforceable and inspectable. It does not make it neutral.

**Therefore: attach the funding decision, and its reason, to the question it left unanswered.** Otherwise *unfunded* gradually becomes *unsupported*, and *unsupported* becomes *disproved* somewhere between the database and the executive summary. The institution's map of what it knows should include the questions it could not afford, or was not permitted, to answer.

## Give the Objection a Consequence

An organization can pay for criticism and still arrange for nothing to follow from it.

For years Facebook tuned its feed for engagement and time spent. But the company's research suggested that passively consuming professionally produced content could be bad for the people doing it. A person could keep scrolling without becoming better off. The number could go up while the thing it was supposed to stand for went down. Bing's question now concerned hours of people's lives.[^fbfiles]

In January 2018 the company announced a change toward “meaningful social interactions,” favoring conversations and exchanges among friends and family. It looked like the right fix: move from measuring attention to measuring connection. Facebook even said it expected people to spend less time on the platform.[^fbchange]

Then its researchers found publishers and political parties shifting toward outrage because that was what travelled. According to internal documents reported by the *Wall Street Journal*, heavy weighting of reshared material amplified angry voices, and researchers found misinformation, toxicity and violent content unusually common among reshares. They proposed reducing the boost for material likely to travel down long chains of users. Facebook made some changes for civic and health content, but Zuckerberg reportedly resisted expanding them if doing so materially reduced the interaction metric.[^fbfiles] The institution had heard the objection. The new number could still defeat it.

The same reporting exposed research inside Instagram. Among surveyed teenage girls who already reported body-image difficulties, roughly one in three said Instagram made them feel worse. These were self-reports, not a demonstration of cause. Facebook disputed the reporting's characterization, pointed to positive findings elsewhere in the research, and said the work had informed product changes.[^instagram] The finding still required an answer. Some researchers told the *Journal* they struggled to get colleagues to appreciate its gravity. One former researcher put the institutional problem rather precisely: “We’re standing directly between people and their bonuses.”

The organization had paid for the knowledge it was now resisting. These objections came from inside, from people employed to investigate the products. Having findings on the company's message board did not give the researchers authority over what followed. The public learned about these internal disputes through leaked documents. A criticism had travelled further than the institution's willingness to act on it.

Longino's claim is that **objectivity is social**. It belongs to a community's criticism, not to any single mind, and it has institutional requirements: venues for criticism, uptake, shared standards, and a tempered equality of intellectual authority. Criticism has to enter the community's reasoning, not merely occur somewhere in its vicinity.[^longino]

An objection needs an object. It can address the reported observation, the assumption connecting it to an interpretation, the proposed action, or the standard used to judge that action. The response must show what happened to the objection. It might supply missing evidence, revise the claim, commission a test, or explain why the criticism does not apply. A resource decision might leave it unresolved. Marking the thread *closed* tells us that somebody finished interacting with it; it says nothing about which outcome occurred. “Noted” is none of these. With agents it gets cheaper still: a reviewer objects, the builder replies that the concern has been noted, both complete their tasks, and the report goes out. We have successfully parallelized the experience of being ignored.

Stellar Colosseum, a harness for mathematical research, gives the procedure a concrete form. Agents develop proposed arguments while reviewers look for defects. The objections travel with the proposals as other agents combine them into a longer argument. At the final review, a specific fatal flaw is enough to reject the proof; favorable verdicts from other reviewers cannot cancel it. The defect is tied to the claim or dependency that failed, so the next round can repair the argument or try a different strategy.[^colosseum] Failed drafts remain available with their reviews attached. The reviewers can still be wrong. But their findings change what happens next, and an unresolved objection can survive the departure of the agent that raised it.

Who gets access to that procedure matters. A critic cannot examine an assumption if it receives only the conclusion. A domain expert cannot contribute evidence if the system accepts objections only in the vocabulary of the ranking team. And an agent given a different name does not acquire a different evidential position. We need to vary access to relevant observations and expertise, not merely the adjectives in the role prompt.

Longino also prevents a comfortable fantasy about the final judge. A product owner may reasonably care about revenue; a researcher may study harm; an infrastructure team may worry about cost. Their observations can be reliable while their preferred decisions differ. More accurate measurement may clarify the disagreement without resolving the goals behind it. The system should be able to say which dispute the next experiment can settle and which requires a decision about purpose. Otherwise it will keep requesting evidence to avoid naming a conflict over what matters.

**Therefore: tie every objection to the thing it challenges, record what became of it, and let the unanswered ones travel with the decision.** If the organization proceeds anyway, the decision-maker owns that choice, in writing.

At this point the institution can receive criticism, preserve alternatives, and explain its allocations. It can still spend decades declining to change.

## Test What the Next Agent Inherits

Max Planck's observation about scientific change, now known as **Planck's principle**, is usually compressed into “science advances one funeral at a time.” His actual sentence describes a new truth gaining acceptance because, rather than all its opponents being persuaded,

> “…its opponents eventually die, and a new generation grows up that is familiar with it.”[^planck]

In Planck's account, opponents need not be persuaded. They can be outlived. A new generation learns the new examples first and has no old allegiance to surrender. The remark is bleak because the mechanism of correction lies partly outside the argument. We should not treat mortality as a scientific method, but we should ask what changes with the occupant of the chair.

There is empirical work on that question. Studying the premature deaths of eminent life scientists, Pierre Azoulay, Christian Fons-Rosen, and Joshua Graff Zivin found declining contributions from collaborators and increased contributions from outsiders to the affected fields. The incoming work drew on a different scientific corpus and was disproportionately likely to be highly cited.[^funerals] This does not establish that the departed scientists had been wrong. It shows that the organization of participation can change which work enters a field.

Now return to the sixteen Claudes. Every worker is temporary. The institution can be remarkably permanent.

A fresh agent reads the same progress file, retrieves the same successful patterns, accepts the same categories, and is scored by the same evaluator. Its predecessor has disappeared, but the commitments that shaped its work have been transferred intact. Session turnover is not the replacement Planck was describing. The next generation can be born with the old generation's entire syllabus already in context.

The durable incumbent may be a retrieval preference, a canonical example, a benchmark, or a rule giving one branch first access to compute. A more capable replacement model may defend it more effectively.

The engineering response cannot be “delete old knowledge periodically.” Useful expertise would disappear with the errors, and newness would become another unearned source of authority. A branch has to be able to start without every commitment whose adequacy is in question, while keeping the constraints that are not in question: consent, cost, the integrity of the data. Its results then need a comparison whose terms are explicit and open to challenge. If no available comparison can decide the issue, that limitation belongs in the record. A new vocabulary does not entitle its author to victory.

**Therefore: let some workers start without the inherited commitment under test, and say exactly which commitments they still share.** Human institutions sometimes manage that through a change of personnel. A persistent agent institution needs mechanisms that act on the inherited structure itself.

## Find Where the Result Lives

An agent inherits more than its own institution's files. Where does the knowledge of a result live? In the agent? Which one, exactly?

Chapter 5 borrowed Popper's name for the answer: **World 3**, the world of theories, proofs, libraries and instruments, which exists outside any particular head and outlasts whoever produced it.[^world3]

<!-- EDITORIAL NOTE (Hani, 21 Sept): the homes of World 3.
Idea: knowledge bases, ontologies, the web, search and LLMs are all descendants of the library, and most began as science solving its own filing problem (the web at CERN, 1989; PageRank as citation analysis; the wiki for patterns; community-run ontologies such as the Gene Ontology). Each move made knowledge cheaper to reach and dropped something the previous institution had worked for: the edition, the catalogue card, the editor. Wikipedia had to reinvent the footnote ("citation needed" = give the claim an address). The LLM is the latest and most convenient house, the whole library in one voice, and it arrived without a catalogue card (Ch. 4: epistemologically flat; "the library without the childhood").
Claim to land: every new memory has needed its System 3 rebuilt. This one is ours to build.
Placement: one paragraph here; optionally a one-line seed in Chapter 5's memory section after the clay tablet.
Draft paragraph:
World 3 has moved house several times. It lived in memory, then on clay, then in libraries with catalogues, then in journals with citation indexes. The web was built at CERN so physicists could find each other's papers; the ranking that made it searchable was citation analysis pointed at links. Each move made knowledge cheaper to reach, and each one left something behind that the last institution had worked for: the edition, the catalogue card, the editor. Wikipedia had to reinvent the footnote and enforce it with volunteers. A language model is the latest house and the most convenient, the whole library in one voice, and it arrived without a single catalogue card. Every new memory has needed its System 3 rebuilt. This one is ours to build.
-->

In Terence Tao's collaboration with DeepMind, AlphaEvolve found a slightly improved construction for three-dimensional finite-field Kakeya sets. Deep Think helped produce an informal proof, and AlphaProof formalized it in Lean.[^tao] The next investigation can use the construction, examine its explanation, or check the formal proof under its specified axioms. Each artifact offers a different way into the result. None requires summoning the original workers back into existence. World 3 has acquired participants that arrive through an API.

Availability is only the beginning of reuse. Kevin Buzzard checked Anthropic's Fermat formalization while leading his own publicly funded project on the theorem. His commitments included adding useful mathematics to the community library and making a document through which people could explore the modern proof. A completed formalization did not discharge those commitments. He welcomed the achievement and still had work to do.[^buzzard] A proof can check while leaving the next mathematician with a formidable renovation project.

The same question reaches beyond mathematics. The AlphaFold database makes more than two hundred million protein-structure predictions available for research. AlphaGenome Atlas supplies predictions for roughly nine billion possible single-letter DNA changes.[^biology] These resources carry uncertainty; a prediction does not become an experimental observation by being stored beside a billion others. But a researcher can begin with material she could never have produced herself, select a candidate, and put it to a test its creators never planned. Faster discovery depends partly on what the last investigation leaves usable.

**Therefore: fund the work that makes a result usable: checking its scope, finding it again, explaining it, maintaining the tools around it.** If we fund only the next spectacular result, that work waits. The scientific community was already there, in the literature, the libraries, the instruments, and the people who maintained them. Agents inherit it and begin adding to it. The question is whether their additions make the next investigation more capable, or merely leave it with more to read.

## Put the Library to Work

Which brings us back to the file. By now it holds more than can fit sensibly into one prompt. A pattern's instructions live separately from the records of its applications. A search retrieves the method and examples; a question about its standing retrieves the observations, versions, dependencies, and challenges behind it.

Bad storage forgets by deletion; bad retrieval forgets by attention. The query “review this experiment” can retrieve a popular checklist and leave the Bing warning untouched on disk. Loading every checklist gives the reviewer the whole office filing cabinet and asks it to find the urgent part. We can evaluate selection by looking at downstream work: whether the agent found the relevant concern, avoided irrelevant procedures, and reached a justified conclusion at an acceptable cost. Similarity between the task description and the retrieved prose is only an intermediate signal.

Our candidate pattern still says `confidence: provisional, one incident`. A pattern extracted from one incident is a hypothesis with one data point. “Increases in activity are usually fake” would be a rather expensive lesson to draw from one bug. Agentic Context Engineering, or ACE, supplies one piece of the machinery for doing better: a generator, reflector, and curator maintain a structured playbook through incremental updates, which limits the loss of detail that occurs when each update replaces the whole summary. Its reported evaluations show gains on the studied tasks; the usefulness of the lessons still depends on the feedback and quality of reflection.[^ace]

So the candidate pattern faces cases that did not produce it. The reviewer with the pattern and the reviewer without it read the same reports: some with degraded experiences behind the gain, some with real gains, some with too little evidence to say. The comparison keeps the model and tools fixed, repeats runs where stochastic variation matters, and records both the quality of the conclusions and the resources consumed. A curator that warns about metrics in every report has learned how to sound concerned. A generic instruction to be careful can serve as the control. If the elaborate pattern performs no better, its philosophical bibliography does not entitle it to more context.

This possibility is real. Gloaguen and colleagues' revised study found no statistically significant gain in task success from either generated or developer-written repository context files over using none. Generated files raised average costs by twenty to twenty-three percent across the two benchmarks. Another study, by Lulla and colleagues, reported improvements in runtime and output-token use but did not comprehensively establish the correctness of the resulting changes.[^context] Together they make it difficult to confuse the presence of instructions with a demonstrated improvement in work.

**Therefore: record how sure we are of each pattern, and make it earn that confidence on cases that did not produce it.** If the check helps only in search, its scope stays there, and the next agent working elsewhere does not inherit an irrelevant ritual. The evidence of learning is in the next investigation. The model's weights can stay fixed while a better method lets a new worker find something its predecessor missed.

## Put the Procedure Under Test

Feyerabend's argument **against method** belongs here, after we have built something we might be tempted to call the scientific method. Every rule of method, he argued, has been usefully broken at some point in the history of science. A procedure that forbids its own violation cannot find out where it is wrong.[^feyerabend]

Our system may faithfully preserve dependencies while omitting the important kind of dependency. It may compare candidate patterns on cases selected by the incumbent pattern. It may require evidence for an alternative while refusing the instruments needed to produce that evidence. Every individual operation can function as specified while the arrangement prevents the question that would matter.

These are testable possibilities when we can construct a relevant comparison. A retrieval policy can be evaluated against another policy. A reviewer can be compared with a reviewer given different evidence. A pattern can be withheld from a branch to see whether its absence reveals errors its presence concealed.

Other disputes reach the purpose or authority of the system. Whether a feed should be ranked for activity or for something harder to count cannot be settled by letting whichever evaluator produces the higher score appoint itself. The empirical investigation can illuminate consequences. Someone still has to make and own the decision about which consequences matter.

Alexander's form now asks for a *Therefore*. We could write “revise the method when it fails.” But the method decides which failures count. The next chapter has to open that loop.

## What the File Says Now

The graphs and procedures in these cases were designed. Their necessity became clear through the work: agents lost track of what others had established; a failed assignment produced a useful result; an encouraging finding changed the research budget. This is how I read these experiments: as the formation of scientific institutions. The need to coordinate fallible workers keeps bringing builders back to records, criticism, shared methods, and decisions about what deserves another attempt.

Emergence does not make the institution ownerless. Someone can release the proof and retain control over the capacity that produced it. Someone chooses whether the next allocation buys another discovery, a better explanation of this one, or maintenance of the library both depend on. Our records can expose those choices. Changing who is entitled to make them requires more than editing a prompt.

We have seen pieces of this language at work: shared proof graphs, experiments that challenge their own metrics, reviews that travel with failed arguments. I have not shown an agent institution that composes all of them, keeps their reasons alive, and changes its own way of seeing when those reasons fail. That is the ambition, and it still has to earn its confidence marks.

<!-- EDITORIAL NOTE: optional close on Alexander's gate. In The Timeless Way of Building (final part, "The Kernel of the Way") he says the language is only a gate: you learn the discipline in order to pass through it. It rhymes with Feyerabend and with a system that rewrites its own language. Verify the passage before using. -->

Imagine the next engineer opening the incident file a year from now. It says what Sam looks for in the serializer, why he looks there, the two times that suspicion was wrong, and who disagreed. She can use his judgment without having to inherit it whole. Alexander wanted the family to be able to argue with the architect. Now the next worker can argue with Sam, even while Sam is on holiday.

For most of this chapter, we have held one boundary steady. A procedure decides whether proposed changes to working knowledge should be accepted. The system can revise a pattern while that procedure remains outside the revision being judged. It can learn under a method someone has supplied.

But the method is also software. The system can propose changes to its retrieval, its experiments, its reviewers, and the rules by which it promotes a lesson. It can begin investigating the machinery that makes its investigations possible.

Now the claim to be tested is harder. A change must do more than make the current answer better or make the current evaluator happier. It must improve the system's ability to find and assess further changes. The process that judges improvement has entered the experiment.

---

[^alexander]: Christopher Alexander, Sara Ishikawa, and Murray Silverstein, with Max Jacobson, Ingrid Fiksdahl-King, and Shlomo Angel, *A Pattern Language: Towns, Buildings, Construction*, 1977. Patterns 1 (Independent Regions), 88 (Street Café), 159 (Light on Two Sides of Every Room), 167 (Six-Foot Balcony), 180 (Window Place), 203 (Child Caves), 251 (Different Chairs), 252 (Pools of Light) and 253 (Things from Your Life); on the quality without a name, see Alexander, *The Timeless Way of Building*, 1979; on the format, the asterisks and patterns as hypotheses, see the introduction, especially pp. x–xv. <https://arl.human.cornell.edu/linked%20docs/Alexander_A_Pattern_Language.pdf>.

[^beck]: Kent Beck and Ward Cunningham, “Using Pattern Languages for Object-Oriented Programs,” OOPSLA-87 workshop on the Specification and Design for Object-Oriented Programming, 1987.

[^wiki]: Ward Cunningham launched WikiWikiWeb in March 1995 as an editable supplement to the Portland Pattern Repository. See Bo Leuf and Ward Cunningham, *The Wiki Way*, 2001.

[^gof]: Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*, 1994. On the Hillside Group, founded after an August 1993 meeting in Colorado, see its own history at hillside.net. Will Wright has described *A Pattern Language* as an inspiration for *The Sims* (2000) in several interviews.

[^alexander96]: Christopher Alexander, “The Origins of Pattern Theory: The Future of the Theory, and the Generation of a Living World,” keynote at OOPSLA 1996; published in *IEEE Software* 16(5), 1999, pp. 71–82.

[^feigenbaum]: Edward A. Feigenbaum, *The Art of Artificial Intelligence: I. Themes and Case Studies of Knowledge Engineering*, Stanford report STAN-CS-77-621, 1977, especially the introduction and PUFF example. <https://infolab.stanford.edu/pub/cstr/reports/cs/tr/77/621/CS-TR-77-621.pdf>.

[^karpathy]: Andrej Karpathy, “Software 2.0,” November 2017, and “Software Is Changing (Again),” talk at Y Combinator's AI Startup School, June 2025.

[^skills]: Agent Skills, [official specification](https://agentskills.io/specification), consulted September 2026.

[^voyager]: Guanzhi Wang et al., *Voyager: An Open-Ended Embodied Agent with Large Language Models*, 2023. <https://arxiv.org/html/2305.16291v2>.

[^fermat]: Anthropic, ‘Formalizing Fermat’s Last Theorem,’ 4 September 2026, especially the account of Prove2Me and final verification. <https://www.anthropic.com/research/formalizing-fermats-last-theorem>.

[^doyle]: Jon Doyle, “Truth Maintenance Systems for Problem Solving,” *Proceedings of IJCAI*, 1977, p. 247. <https://www.ijcai.org/Proceedings/77-1/Papers/035.pdf>. See also Doyle, “A Truth Maintenance System,” *Artificial Intelligence* 12(3), 1979, pp. 231–272, <https://doi.org/10.1016/0004-3702(79>90008-0). These systems maintain program justifications; identifying the real-world assumptions and evidential relationships remains a separate problem.

[^kohavi]: Ron Kohavi, Alex Deng, Brian Frasca, Roger Longbotham, Toby Walker, and Ya Xu, “Trustworthy Online Controlled Experiments: Five Puzzling Outcomes Explained,” *Proceedings of KDD*, 2012, section on the overall evaluation criterion for a search engine. [Original paper](https://exp-platform.com/Documents/puzzlingOutcomesInControlledExperiments.pdf), §3.1. Sessions per user is a key component of the criterion; sessions serve as a practical proxy because tasks are harder to identify.

[^kohavi2]: Kohavi et al., “Five Puzzling Outcomes Explained,” as above. The account of why queries and revenue rose is the authors' own.

[^popper]: Karl Popper, *Conjectures and Refutations*, 1963, chapter 1, especially the discussion of risky predictions and testability. <https://padron.entretemas.com.ve/documentos/Popper-Conjectures-Rwefutations-GrowthOfKnowledge.pdf>. Popper treats falsifiability as a criterion for demarcating science; the use here is the narrower one, that a test is informative in proportion to the risk it imposes on the claim.

[^twyman]: On Twyman's law and trust checks, see Ron Kohavi, Diane Tang, and Ya Xu, *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*, 2020, chapter 3. On sample-ratio mismatch, see Aleksander Fabijan et al., “Diagnosing Sample Ratio Mismatch in Online Controlled Experiments,” *Proceedings of KDD*, 2019.

[^quine]: W. V. O. Quine, “Two Dogmas of Empiricism,” 1951, section 6. <https://www.ditext.com/quine/quine.html>. Duhem's discussion of physical testing and Quine's broader holism differ in scope; the shared engineering difficulty here is identifying what to revise when a bundle of assumptions encounters a contrary result.

[^saussure-lectures]: Ferdinand de Saussure, *Third Course of Lectures on General Linguistics*, 1910–1911, student notes published in English in 1993. <https://www.marxists.org/reference/subject/philosophy/works/fr/saussure.htm>. The structuralist connection here concerns Saussure’s account of relational linguistic value.

[^imagenet]: Alex Krizhevsky, Ilya Sutskever, and Geoffrey E. Hinton, “ImageNet Classification with Deep Convolutional Neural Networks,” *Advances in Neural Information Processing Systems* 25, 2012.

[^kuhn]: Thomas S. Kuhn, *The Structure of Scientific Revolutions*, 1962; second edition, 1970, especially the accounts of normal science, paradigms, and their resolution through scientific change. <https://www.lri.fr/~mbl/Stanford/CS477/papers/Kuhn-SSR-2ndEd.pdf>.

[^riemann]: Anthropic, ‘Learning more about Claude’s mathematical capabilities,’ 10 August 2026, updated 13 August. <https://www.anthropic.com/research/riemann-zeta>.

[^laudan]: Larry Laudan, *Progress and Its Problems*, 1977, “The Modalities of Appraisal: Acceptance and Pursuit,” pp. 108–114. <https://ia601400.us.archive.org/24/items/in.ernet.dli.2015.136278/2015.136278.Progress-And-Its-Problems.pdf>.

[^lakatos]: Imre Lakatos, “Falsification and the Methodology of Scientific Research Programmes,” in *Criticism and the Growth of Knowledge*, 1970; collected in *The Methodology of Scientific Research Programmes*, 1978. <https://books.google.com/books?id=RRniFBI8Gi4C>.

[^kitcher]: Philip Kitcher, “The Division of Cognitive Labor,” *The Journal of Philosophy* 87(1), 1990, pp. 5–22. <https://joelvelasco.net/teaching/120/kitcher90-divisioncognitive.pdf>.

[^navier]: OpenAI, ‘On the Navier–Stokes Millennium Prize Problem,’ 8 September 2026, updated 10 September, especially ‘How we found the proof.’ <https://openai.com/index/navier-stokes-solution/>. The announced result uses smooth forcing and addresses alternatives C and D of the official formulation; it does not settle the unforced Navier–Stokes regularity question.

[^clay]: Clay Mathematics Institute, ‘Navier-Stokes Announcement,’ 11 September 2026. <https://www.claymath.org/news/navier-stokes-announcement/>. Status of the recent mathematical announcements in this chapter checked on 13 September 2026.

[^priority]: Tristan Buckmaster, [public statement](https://cims.nyu.edu/~tristanb/statement.pdf), September 2026, especially pp. 1–4; OpenAI, [‘On the Navier–Stokes Millennium Prize Problem,’ ‘Concurrent work’](https://openai.com/index/navier-stokes-solution/), updated 10 September 2026. These are the participants’ accounts.

[^fbfiles]: Keach Hagey and Jeff Horwitz, “Facebook Tried to Make Its Platform a Healthier Place. It Got Angrier Instead,” *The Wall Street Journal*, 15 September 2021, part of the Facebook Files series based on internal documents; [copy entered in the Congressional record](https://docs.house.gov/meetings/IF/IF16/20211201/114268/HHRG-117-IF16-20211201-SD012.pdf). The company said the ranking change was not the source of the world's divisions and that it had an integrity team working on exploitation of the algorithm. The article reports both limited adoption of fixes and resistance to extending them.

[^fbchange]: Adam Mosseri, [“Bringing People Closer Together”](https://about.fb.com/news/2018/01/news-feed-fyi-bringing-people-closer-together/), Facebook, 11 January 2018. The announcement describes prioritizing conversations and interactions among friends and family and anticipates reduced time spent on Facebook.

[^instagram]: Georgia Wells, Jeff Horwitz and Deepa Seetharaman, “Facebook Knows Instagram Is Toxic for Teen Girls, Company Documents Show,” *The Wall Street Journal*, 14 September 2021; [copy entered in the Congressional record](https://docs.house.gov/meetings/IF/IF00/20210913/114039/HMKP-117-IF00-20210913-SD129.pdf), especially the body-image findings and the former researcher's statement about bonuses. For the company's response and annotated research decks, see Pratiti Raychoudhury, [“What Our Research Really Says About Teen Well-Being and Instagram”](https://about.fb.com/news/2021/09/research-teen-well-being-and-instagram/), 26 September 2021, updated 29 September. The body-image proportion concerns respondents who reported that difficulty, not all teenage girls; the surveys do not establish causation.

[^longino]: Helen Longino, *Science as Social Knowledge*, 1990, and *The Fate of Knowledge*, 2002. See her own exposition in [“The Social Dimensions of Scientific Knowledge”](https://plato.stanford.edu/entries/scientific-knowledge-social/), especially the conditions for effective critical interaction. Uptake does not require accepting every objection, and tempered equality does not imply equal expertise on every question.

[^colosseum]: Honghao Lin et al., ‘Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science,’ arXiv:2609.15983v2, 15 September 2026, §§4.1–4.3. <https://arxiv.org/html/2609.15983v2>. The workflow reviews natural-language arguments; acceptance does not itself constitute formal proof certification.

[^planck]: Max Planck, *Scientific Autobiography and Other Papers*, translated by Frank Gaynor, 1949, pp. 33–34; the quoted excerpt is reproduced in Kuhn, *The Structure of Scientific Revolutions*, second edition, p. 151. [Kuhn's text](https://www.lri.fr/~mbl/Stanford/CS477/papers/Kuhn-SSR-2ndEd.pdf). The familiar funeral wording is a later compression; see [the quotation history](https://quoteinvestigator.com/2017/09/25/progress/).

[^funerals]: Pierre Azoulay, Christian Fons-Rosen, and Joshua S. Graff Zivin, “Does Science Advance One Funeral at a Time?”, *American Economic Review* 109(8), 2019, pp. 2889–2920. <https://pubmed.ncbi.nlm.nih.gov/31656315/>.

[^world3]: Karl Popper, *Objective Knowledge: An Evolutionary Approach*, 1972, chapters 3 and 4, especially “Epistemology Without a Knowing Subject.”

[^tao]: Terence Tao, ‘Mathematical exploration and discovery at scale,’ 5 November 2025. <https://terrytao.wordpress.com/2025/11/05/mathematical-exploration-and-discovery-at-scale/>. See also Bogdan Georgiev, Javier Gómez-Serrano, Terence Tao, and Adam Zsolt Wagner, <https://arxiv.org/abs/2511.02864>.

[^buzzard]: Kevin Buzzard, ‘FLT: Anthropic has beaten me to it,’ 4 September 2026, especially ‘The code base’ and ‘What this work is, and is not.’ <https://xenaproject.wordpress.com/2026/09/04/flt-anthropic-has-beaten-me-to-it/>.

[^biology]: Google DeepMind and EMBL-EBI, [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk/); AlphaGenome Atlas team, [‘AlphaGenome Atlas: A predictive map of every possible DNA letter change in the human genome’](https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/), September 2026.

[^ace]: *Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models*, 2025. <https://arxiv.org/html/2510.04618v1>.

[^context]: Gloaguen et al., *Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?*, 2026, [arXiv:2602.11988v2](https://arxiv.org/html/2602.11988v2), revised 23 June; Jai Lal Lulla et al., *On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents*, 2026, [arXiv:2601.20404v2](https://arxiv.org/html/2601.20404v2), revised 30 March.

[^harari]: Yuval Noah Harari, *Sapiens: A Brief History of Humankind*, 2014, ch. 14, ‘The Discovery of Ignorance.’

[^feyerabend]: Paul Feyerabend, *Against Method*, 1975. [Excerpt from the author's text](https://www.marxists.org/reference/subject/philosophy/works/ge/feyerabe.htm). Feyerabend's historical claim is that major advances violated the methodological rules later proposed for science; the use here is the narrower one, that a procedure should be open to tests that set it aside.

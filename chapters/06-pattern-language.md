# Chapter 6: Pattern Language

*When Knowledge Becomes Software*

A new engineer can know Python, distributed systems, and the collected technical culture of the internet while remaining spectacularly unqualified to deploy your company's software. She does not know which apparently redundant check protects an old customer integration, which dashboard changes meaning during failover, or why the elegant migration in the wiki was abandoned halfway through. Much of her first month consists of discovering the reasons behind things that look stupid.

Ask for the incident procedure and the answer sounds like this:

> Start with the dependency graph, unless the spike began exactly at deployment. If only one market is affected, check the traffic split before touching the database. And if it started after Tuesday's migration, ask Sam. There is a thing with the old serializer.

She writes down *ask Sam*. That preserves the dependency beautifully. It does less for the incident that happens while Sam is on holiday. She needs to know what he looks for in the serializer, why he looks there, and when that suspicion is a waste of time.

Carlini's compiler project depended on this kind of transfer. Its workers inherited code, tests, progress files, and procedures. The previous chapter followed the institution that made those inheritances possible. Now we have to open the files. What, exactly, should the institution leave inside them?

We could write “question your assumptions” at the top of every prompt. It would improve the atmosphere. It would not tell a machine which conclusion to withdraw when an assumption fails, which experiment could distinguish two explanations, or who is allowed to spend the money on that experiment.

Those are different operations. We will have to give them different representations. And when we try, the philosophers of science become inconvenient in a useful way: each finds something the proposed machine cannot yet do.

## Put Local Knowledge to Work

A capable coding model arrives knowing the profession and almost nothing about the workplace. General competence is already there. The local knowledge has to reach it.

One way is to put that knowledge directly into a program. Another is to teach a model through examples and optimization. A third is to give an existing model instructions, demonstrations, diagrams, and scripts that it can interpret while working. These approaches can inhabit the same system. A model reads the incident procedure, chooses a diagnostic query, and hands arithmetic to code. Nobody benefits if the arithmetic becomes more literary.

This is an old ambition with a new interpreter. In 1977 Edward Feigenbaum described knowledge engineering as the work of acquiring expert knowledge, representing it, and using it to construct and explain reasoning. His examples included a diagnostic system whose rules were developed with an expert and tested against cases. Running them exposed gaps and inconsistencies that the collaboration then had to resolve. The difficulty of making expertise explicit was already part of the enterprise.[^feigenbaum]

Language models change the cost of some of that translation. We can supply an account of how a problem usually unfolds, with a worked example and a warning about a misleading instrument, without first expressing every qualification in formal logic. The model contributes the interpretation. Code still performs the operations for which precise execution matters.

That arrangement needs a name less magical than “the document is executable.” A document influences work when something selects it, interprets it, and acts on it. The same words can produce different actions in different models or environments. A knowledge artifact therefore belongs to a working arrangement: the material, the interpreter, the tools, and the conditions of use.

Agent skills give this arrangement a practical container. The Agent Skills specification separates a small description used for discovery from fuller instructions and additional resources loaded when needed. A package can include scripts and examples as well as prose. The format makes the material accessible; it does not certify its wisdom.[^skills]

There are already demonstrations of accumulating capability this way. Voyager, a Minecraft agent, builds a library of executable skills, retrieves relevant ones through their descriptions, and uses existing skills in later behavior. Its feedback loop includes execution results and model-based verification. The library helps the agent attempt work that would otherwise have to be reconstructed from the beginning.[^voyager]

For an organization, the corresponding possibility is attractive. The model can change while the local operating knowledge survives. A procedure can improve without waiting for a training run. A specialist can leave behind more than completed tasks: methods that another worker can combine with its own capabilities.

But a library can also preserve the wrong lesson at industrial speed. Before we let it educate the next worker, we need a better unit than something somebody once said in a prompt.

## Compose Methods

Christopher Alexander's *A Pattern Language* offers two ideas we need to keep together. Its patterns describe proposed arrangements for recurring problems, and those patterns connect across scales. A neighborhood is completed through smaller arrangements; those arrangements require further patterns of their own. In the introduction, Alexander and his coauthors explicitly describe the patterns as hypotheses. Does the problem occur as described? Does the proposed arrangement resolve it? Even their most confidently marked patterns remain open to revision.[^alexander]

The attraction is not that every organization should acquire 253 files. It is that a useful practice has a context and relationships. A procedure for reviewing an experiment may call on methods for checking measurements, comparing explanations, and investigating a result that contradicts the expected one. Those are reusable pieces of work. They need not all run in the same order on every occasion.

Consider the instruction “never use regex on nested syntax.” It has the reassuring shape of wisdom and the inconvenient property of being false. A fixed format with at most one level of nesting can be matched with a regular expression. A format that keeps acquiring new kinds of nesting is another matter. The useful pattern records when a parser becomes cheaper than maintaining an increasingly heroic expression at two in the morning. The conditions are part of what we learned.

Let us build an imaginary system that has to use such conditional knowledge. Its job is to review experiments in an online store. We will follow its records and decisions as the review unfolds.

A ranking experiment reports more clicks and little change in orders. An agent proposes an explanation: the new ranking has increased engagement, but the additional interest has not yet become purchases. Another possibility is that the new interface records clicks differently. There may be other explanations, and more than one may be operating.

The library contains a pattern called **Check Measurement Comparability**. Its purpose is to establish whether measurements being compared were produced on compatible terms. It directs the agent to inspect event definitions, populations, collection paths, and relevant software changes. It includes a worked case, a case where the concern turned out to be unfounded, and a script for comparing the relevant definitions.

That pattern belongs inside **Review an Experiment**. It can call on **Construct a Discriminating Test** if inspecting the definitions leaves competing explanations alive. It should not call on every statistical procedure in the building. The relationships carry some of the practical knowledge: which method helps with which difficulty, which methods are alternatives, and which preconditions must hold before a method makes sense.

The book has already encountered this kind of composition. In Deep Mode, freedom to explore solutions depended on a more stable way of evaluating them. The constraints and the exploration were doing different jobs. Treating either as an isolated maxim would lose the arrangement that made it useful.

A pattern can contain factual assumptions, practical recommendations, and organizational rules. These require different kinds of support. “This event can be emitted twice” is a claim about a system. “Inspect this before running an expensive analysis” is a recommendation about effort. “Do not alter the live experiment” specifies an authority boundary. A successful test of the first does not justify the other two automatically.

We can store the instructions already. The harder question is how the machine represents what they allow it to conclude.

## Give the Claim an Address

Suppose our reviewer writes a report, another agent summarizes it, and a third uses the summary to recommend rolling out the new ranking. Later, we discover that the reported increase partly reflects a change in event collection.

Searching every document for the word *engagement* is one possible response. It will be popular with the company selling us tokens.

A different design gives the original observation and the interpretation separate identities. The observation records the reported metric difference, the query, the data interval, and the relevant versions. The interpretation refers to that observation and states what else must hold for it to support the conclusion. The rollout recommendation, in turn, refers to the interpretation and the other considerations on which it depends.

Now a correction has somewhere to go.

| Record | What it says | What a collection fault changes |
|---|---|---|
| Observation | The specified query returned a higher click rate for the treatment. | The record of the query result can remain accurate. |
| Measurement assumption | The two rates represent comparable events and populations. | This assumption requires revision or further investigation. |
| Interpretation | The result supports increased user engagement. | This particular support is weakened; other support must be examined. |
| Recommendation | The experiment justifies rollout under the stated criteria. | The recommendation must be reconsidered if it relied on that interpretation. |

The distinction matters because learning that a measurement was misleading does not make the historical query result disappear. Nor does the loss of one supporting argument establish that the opposite conclusion is true. The system may have other evidence for increased engagement. It has to examine the support, not merely change a label from green to red.

Jon Doyle was designing machinery for this kind of dependency long before language models. His truth-maintenance work recorded justifications for program beliefs and reconsidered dependent beliefs when those justifications changed. It supported reasoning about assumptions and hypothetical alternatives.[^doyle] The name should be read carefully: a program can maintain the consequences of its stated reasons without those reasons corresponding to reality. The graph does not acquire a laboratory by being called a truth-maintenance system.

For our agent, there are two kinds of work. A model may propose the interpretation and identify relevant assumptions. Once the dependencies have been explicitly recorded, ordinary software can find which later artifacts depend on them, mark their support for reconsideration, and prevent an old recommendation from silently presenting itself as current. The difficult semantic judgment and the mechanical propagation are different parts of the system.

The update has a precise route through those records. The review changes the comparability assumption from *accepted for this analysis* to *withdrawn*, citing the collection fault. The recorded argument from the click rate to engagement then loses that support. The system checks whether other recorded arguments still support the interpretation. If the rollout recommendation relied on support that no longer holds, it changes from *ready for approval* to *requires review* and cannot be issued automatically. The old report remains in the history; its recommendation is no longer eligible for reuse as a current decision. Software can enforce those transitions without pretending to have discovered the collection fault itself.

The history stays attached. A later worker asking why the rollout recommendation was suspended reaches the observation and assumption that caused it. An LLM-written explanation produced after the fact may be helpful, but it cannot substitute for a record of what the earlier decision actually used.

Anthropic's formalization of Fermat's Last Theorem depended on giving agents a shared account of the work. Wiles proved the theorem in 1995. The job in August 2026 was to make every step checkable by Lean. Early attempts faltered as agents lost track of the project and stopped collaborating effectively. The successful effort used Prove2Me, which holds every theorem statement as a node in a dependency graph, each with a plain-language description, so a worker that needs a result can search for it and discover that a worker it never met has already established it. In eleven days the agents produced a formalization using roughly thirty thousand intermediate theorems. The completed proof was checked under Lean's three standard axioms, and a separate comparator confirmed that the final statement was Mathlib's Fermat and not a convenient cousin.[^fermat]

The graph gave a worker somewhere to begin without understanding the whole project. It gave the next worker something better than a colleague's assurance that the mathematics was probably fine.

Our store has no Lean for the claim that clicks are engagement. Suppose an agent records the query but omits the comparability assumption. A correction to event collection then reaches none of the recommendations that depended on it. The reviewer must inspect that missing connection before software can propagate anything. Formal dependencies and a model's proposed account of its reasons offer different guarantees.

This is one answer to the question from Chapter 4: what should survive a session? Some answers should survive with their reasons, so the institution can change its mind without having to rediscover everywhere the old mind went.

We still need to decide what should count as a reason.

## Commit the Test Before the Result

Popper's demand for exposure to refutation gives us something more exact than an instruction to be skeptical. A claim rules out possibilities, and a serious test puts it at risk of encountering one of them. Evidence is more informative when it comes from an opportunity for the claim to fail than when the investigator merely collects accommodating examples.[^popper]

Our reviewer can praise the engagement explanation, criticize it, or ask another model to do both. None of those actions changes the event stream. To investigate, it has to say what would look different if the explanation were wrong.

Consider the narrower suspicion that one physical action sometimes generates an additional logged click in the treatment. The reviewer chooses a controlled interaction to reproduce in each interface, with a trace of the events emitted. The test defines the action independently of the event count, identifies the relevant instrumentation versions, and records both the action and the resulting messages. If the same action produces an extra event only in the treatment, the logged rates cannot be interpreted in the originally assumed way without further work.

That result would establish a collection difference under the tested conditions. It would not establish that the entire observed increase was artificial. For that, we need to determine where the behavior occurs and how much of the comparison it affects. Perhaps people also clicked more. Explanations do not always have the courtesy to be mutually exclusive.

A test request therefore needs more than a question in English. It needs the alternatives it is meant to distinguish, the observation to collect, the conditions under which that observation has meaning, and the consequences the possible outcomes would have for the current interpretation. Some of those consequences are probabilistic. A noisy result can weaken an explanation without logically refuting it.

This also tells the agent when a proposed test is unhelpful. Asking the same dashboard for another chart may produce an attractive restatement of the original evidence. If both explanations predict the chart, it does little to distinguish them. Before spending the budget, the system can ask which live disagreement the proposed observation would resolve.

It is possible to write that question into a prompt and get a plausible answer. The operational commitment is stronger: the answer becomes part of the experiment record, written before the result, and the later review checks what happened against it. A prediction revised after observation remains visible as a revision. The institution does not have to remember an investigator's intentions; it can inspect what was committed to the record.

The next complication is sitting inside the word *conditions*.

## Locate the Failure

The previous chapter introduced the problem through instruments that disagreed. Testing involves a bundle of claims about the world, the apparatus, and the way the apparatus was used. Quine's broader account makes the difficulty of assigning revision explicit: experience does not present us with a uniquely marked belief to remove.[^quine]

Our controlled interaction emits two events. The ranking team accepts the result and objects that the test driver clicked twice. The event team says the driver clicked once but retried a message. Someone else notices that the test environment uses a different client version. We have made contact with reality and acquired a meeting.

The dependency record makes that meeting more useful. It shows which claim depended on which version, which operation, and which assumption about event identity. The agent can propose a second probe: record the physical input independently of the emitted messages, pin the client version, or compare the retry behavior. Each probe attacks a particular ambiguity.

There is no rule that says a failed test must indict the main hypothesis. Always protecting it would be equally foolish. The system needs to maintain alternative diagnoses long enough to find observations that separate them. This is where the graph changes what the agent can do: it supplies candidates for investigation and shows what each candidate could repair.

One detail is easy to miss. A second measurement may share the same failed dependency. If the supposedly independent check reads a table derived from the original event stream, agreement between the tables supplies less reassurance than their different names suggest. The provenance must reach the common source. Otherwise the institution manufactures a second witness by creating a second spreadsheet.

After the investigation, we might retain the measurement pattern but revise one of its tools. Or restrict the pattern to contexts in which the event identity is available. Or conclude that this particular concern was unfounded. These lead to different changes in the library. A single counter called *harmful* cannot express all of them.

Capturing every possible dependency would cost more than the inquiry. Our reviewer starts with the support used in the rollout recommendation. A disputed result sends it farther back through the instruments and assumptions. A missing dependency can still defeat the investigation; recording what it has traced makes the gap easier to locate next time.

We have now built a system that can revise an answer and repair the method that produced it. It still assumes that we know what an answer should be about.

## Change the Representation

Kuhn's normal science works because a community shares achievements, examples, and commitments that make sustained problem-solving possible. Its practitioners need not reconstruct the foundations before each experiment. His account of scientific revolutions concerns a deeper change in that framework, including what counts as an important problem and an adequate solution. Scientists also learn from exemplars that cannot be replaced by a complete list of explicit rules.[^kuhn]

I wrote an editing brief for this book after explaining the same corrections to successive agents. One instruction was “preserve the wandering,” which is nearly useless to a reader who has never seen the movement I mean. A before-and-after passage can teach the distinction: one version follows an uncertain thought until it becomes clear; the other announces the conclusion and removes the path that made it convincing. Both can contain long paragraphs. Measuring their length would miss what the examples are there to teach. Those examples also carry my taste into the next session. Preserving my judgment and preserving my mistakes used the same file format.

For an agent, the examples become part of the operational knowledge. They help it recognize the situation before selecting the procedure. But they also establish a familiar way of seeing. If every approved example rewards the same kind of explanation, the system may become better at reproducing that explanation while losing the ability to notice what it excludes.

Return to the store. Suppose we repair the measurement. There really are more clicks. The dominant framework treats engagement as activity: more interaction, under otherwise acceptable conditions, counts as improvement. The system now has a clean measurement inside that framework.

A customer researcher proposes a different unit of analysis: a shopping task. Did the person find a suitable product? How much unnecessary work did it take? Seven clicks can be worse than two if five of them were spent recovering from an unhelpful ranking. The additional interaction might be evidence of difficulty.

This proposal cannot be tested merely by increasing the precision of the click count. It requires a representation of tasks, attempts, completion, and obstacles. It requires different observations, perhaps including a study of people performing specified tasks. It changes how some existing observations bear on the question.

The store gives us a small engineering analogue of this change in framework. We are no longer deciding which value belongs in the `engagement` field. We are asking whether that field organizes the problem adequately.

Saussure gives us a related structuralist insight, returning to Chapter 4: the value of a term depends on the distinctions and relations within its system. The concept does not arrive fully specified by attaching a word to it.[^saussure] In the store's software, *success* is partly defined through its relationship to *session*, *action*, *completion*, and *abandonment*. Altering those relationships can change which conclusions its evidence supports.

An agent architecture capable of this change would need to preserve alternative representations, not just alternative answers. A branch could introduce task-based records, associate them with the old observations where possible, and state where translation fails. Old click logs might contain no evidence about whether someone found what they needed. The missing information cannot be recovered by giving the column a better name.

The evaluator becomes part of the difficulty. If it scores every proposal only on increased clicks, the task-based approach may look worse precisely where it helps the user finish sooner. Letting the challenger write an evaluator that declares itself the winner would prove little. We need an explicit dispute about the purpose of the evaluation, followed by agreed observations on which the approaches can be compared. Some differences will remain matters of organizational goals rather than empirical discovery.

There is no `paradigm_shift()` call that resolves this. There can be operations for branching a representation, retaining the old interpretation, collecting missing observations, and exposing a disputed standard for decision. Those operations make a change possible. They do not guarantee that it is wise.

And possibilities require funding.

## Separate Use from Investigation

The established approach has years of instrumentation, trained models, a benchmark, and people who know how to interpret its results. The alternative has a plausible objection and a request for a study. Compare them this afternoon and the incumbent may win for excellent reasons.

That does not settle what to investigate tomorrow.

Laudan distinguishes acceptance from pursuit. An approach can be the one we presently have most reason to work with while another deserves investigation because of the problems it may solve. Lakatos asks us to examine developing research programmes, including whether their modifications lead to further successes or mainly accommodate difficulties already encountered.[^laudan][^lakatos]

The store can keep using its established ranking while commissioning the task-based study. The operating policy selects an approach for the current task; the research policy assigns effort to tests and alternatives. If both are driven by the same score, the best-supported approach can acquire a monopoly on becoming better supported.

A new task retrieves the incumbent pattern because it has the strongest record. Successful applications add to that record. The alternative receives little use, so it accumulates little evidence. After a while the system has a large collection of observations about the incumbent and very few comparisons. It can accurately report the size of its evidence base while misleading itself about what that evidence establishes.

The research queue therefore keeps proposed comparisons alongside completed ones. Each proposal names the disagreement it could resolve, the observations it needs, and its estimated cost. The allocator can inspect what another run of the incumbent is likely to teach against what the untried comparison could reveal.

The history of a method matters too. Suppose the measurement pattern acquires exceptions for one client, then another, then a third. We should be able to inspect whether each revision identifies a recurring cause and works on further cases, or merely excuses the latest failure. The number of exceptions alone tells us little. A complicated world can require a complicated method. What matters is what the revisions let us explain or accomplish beyond the incidents that provoked them.

Kitcher's division-of-cognitive-labor problem, which we met in Chapter 5, makes the collective stakes explicit. Choices that appear reasonable for investigators individually need not produce the best distribution of effort for the community; incentives and the work of other investigators matter.[^kitcher] We cannot solve the allocation problem by instructing every agent to pursue its most promising idea independently when all of them inherit the same ranking of ideas.

Nor does protecting alternatives mean funding every objection forever. An alternative can receive a bounded experiment whose outcome determines the next decision. We can ask what the experiment would teach us, how expensive it is, and which later choices it could change. Those are reasons for an allocation. They can be recorded and challenged.

Research can also return something its assignment did not ask for. In August 2026 an Anthropic engineer pointed an unreleased Claude at the Riemann hypothesis and left the mathematics to the model. It did not prove the hypothesis. On the way, Anthropic reports, it raised a longstanding lower bound on the proportion of the zeta function's nontrivial zeros on the critical line, from 41.6 percent to 67.2 percent, by combining results from several lines of published work. Roughly sixty subagents developed ideas, reviewed arguments, searched for counterexamples, and checked the literature. Two Anthropic mathematicians checked the paper, two outside number theorists examined it, and the result was formalized in Lean. Anthropic did not expect the techniques to lead to a proof of the full hypothesis.[^riemann]

An evaluator asking only whether the assigned problem was solved would return *no*. That answer would be correct and a poor account of the research. Our records need room for the contribution: its own statement, support, and remaining questions, linked to the unsuccessful attempt that produced it. Whether to fund a follow-up is another decision. The original ambition neither proves the byproduct valuable nor makes it worthless when the ambition fails.

But the person recording these reasons may not be the person who controls the money.

## Keep the Funding Decision Visible

Imagine the task-based alternative needs observations the click framework never collected. It requires access to users, changes to instrumentation, and time from another team. The agent can produce the proposal in a minute. The organization can leave it waiting for a quarter.

Meanwhile, the ranking team has an approved budget and a deadline. It runs another hundred experiments against the existing metric. At the next review, the incumbent presents results and the challenger presents a proposal. Everyone agrees that decisions should be evidence-based.

Nothing in that scene requires dishonesty. The incumbent may still be the better approach. The organization may have good reasons for spending its money elsewhere. But its resource decisions have helped produce the evidential situation on which the next resource decision will rely.

OpenAI's account of its Navier–Stokes proof shows the allocation happening. The company set groups of agents on the open Millennium Problems under different formulations. A result on the Euler equations persuaded the researchers that Navier–Stokes was the live direction, so they pulled agents off the other problems, handed the transfers the Euler result, and folded what separate groups had found into the next prompts. About four days after launch, the group produced a proposed proof of finite-time blowup under smooth forcing, addressing Clay's alternatives C and D. Lean formalization and verification took another seventeen hours.[^navier]

On September 11 the Clay Mathematics Institute said the problem appeared to be settled; evaluation and the assignment of credit would follow its deliberately unhurried process.[^clay] Three events, not one: a decision to invest, a proof checked, a verdict pending. A success in one investigation had changed who could afford to keep investigating elsewhere. The other problems had lost workers, not been refuted.

The history of choosing the route also became disputed. Tristan Buckmaster described his work with Levent Alpöge as extending a programme begun by Diego Córdoba and Luis Martínez-Zoroa. He challenged the presentation of OpenAI's effort while explicitly saying he did not know whether their data had been used. OpenAI acknowledged that a rumor of concurrent work prompted its investigation and denied accessing their unpublished work or using Buckmaster's recent Codex prompts to train the system.[^priority]

A checked proof does not settle that history. Learning that a route is promising can affect where we invest without supplying a single step of the proof. Our research record therefore needs to preserve what prompted an allocation, where that information came from, and which parts remain disputed, alongside the evidence supporting the eventual result. The provenance of a proof and the provenance of the decision to pursue it answer different questions.

Power enters scientific work through the ability to commission observations, supply instruments, define acceptable problems, and sustain a programme through unproductive intervals. In an agent system, the equivalents include tool access, compute budgets, experimental traffic, data collection, and permission to change what gets measured. These are parts of the inquiry even when they appear in another team's configuration.

Consider the difference between three statements:

*The evidence favors the current ranking method.*

*The proposed study could tell us whether our measure of success is adequate.*

*The owner of the product has declined to fund the study.*

All three can be true. A system that compresses them into “continue with the current method, high confidence” has hidden a decision about power inside a statement about knowledge.

The funding decision stays attached to the proposed study, with the reason it was declined. A later agent can see that the study lacked a budget, rather than finding an empty results field and concluding that the approach failed. Without that distinction, *unfunded* gradually becomes *unsupported*, and *unsupported* becomes *disproved* somewhere between the database and the executive summary.

Control over evaluation adds another layer. Suppose the budget owner accepts only experiments that predict higher clicks. The proposed study concerns whether higher clicks represent improvement. Its result cannot affect the decision under the existing rule. The researcher has been invited to challenge an assumption on the condition that she first accept it.

The reviewer splits the request. One part proposes a study of task completion; the other asks whether completion should enter the product’s success criteria. The first goes to experimental review, the second to whoever owns the product goal. A rejection of the second is recorded as a decision about the goal. It cannot be counted as a failed test of the task-based approach.

This is not a technical route around ownership. The person or institution providing resources retains whatever authority it actually has. Giving an agent an epistemic objection does not give it authorization to spend somebody else's money. The practical gain is that the system can no longer treat the ownership decision as a result of an experiment that never took place.

A funding policy can reserve capacity for challenges to the incumbent, but that policy is itself a choice made by people with power. Someone decides how much, for which questions, and subject to whose review. Putting those decisions in code makes them enforceable and inspectable. It does not make them neutral.

The institution's map of what it knows should include the questions it could not afford, or was not permitted, to answer.

## Give the Objection a Consequence

An organization can pay for criticism and still arrange for nothing to follow from it.

A reviewer finds that the supposed increase in engagement depends on an untested measurement assumption. The builder replies that the concern has been noted. Both agents complete their tasks. The report goes out. We have successfully parallelized the experience of being ignored.

Longino's account of objectivity gives criticism institutional requirements. There must be venues for it, uptake, accessible standards, and a tempered equality of intellectual authority. Different perspectives matter because background assumptions affect how observations bear on conclusions. Criticism has to enter the community's reasoning, not merely occur somewhere in its vicinity.[^longino]

For our system, an objection needs an object. It can address the reported observation, the assumption connecting it to an interpretation, the proposed action, or the standard used to judge that action. These are different disputes. The critic should identify which one is at issue and attach the evidence or reasoning that makes it consequential.

The response also needs an object. An answer might supply missing evidence, revise the claim, commission a test, or explain why the criticism does not apply. A resource decision might leave it unresolved. The record should distinguish these outcomes. Marking the thread *closed* tells us that somebody finished interacting with it; it says nothing about which outcome occurred.

In the click-rate dispute, “noted” supplies no answer. The critic points to the comparability assumption; the builder must supply the missing check, revise the interpretation, or explain why the objection does not apply. The resulting decision follows the dependencies we already recorded. If the organization proceeds with the question unresolved, the decision-maker owns that choice. The unanswered objection travels with the recommendation.

This is a more useful division of responsibilities than asking one agent to be optimistic and another to be skeptical. One agent produces a claim with its support. Another can contest the support. A decision procedure determines what may proceed and which questions remain open. The agents can disagree about the substantive issue while the software accurately records the disagreement and its consequences.

Stellar Colosseum, a harness for mathematical research, gives this procedure a concrete form. Agents develop proposed arguments while reviewers look for defects. The objections travel with the proposals as other agents combine them into a longer argument. At the final review, a specific fatal flaw is enough to reject the proof; favorable verdicts from other reviewers cannot cancel it. The defect is tied to the claim or dependency that failed, so the next round can repair the argument or return to exploring a different strategy.[^colosseum]

Failed drafts remain available with their reviews attached. The next worker inherits both the attempted argument and the reasons for distrusting it. The reviewers can still be wrong. But their findings now change what happens next, and an unresolved objection can survive the departure of the agent that raised it.

Who gets access to that procedure matters. A critic cannot examine an assumption if it receives only the conclusion. A domain expert cannot contribute evidence if the system accepts objections only in the vocabulary of the ranking team. And an agent given a different name does not acquire a different evidential position. We need to vary access to relevant observations and expertise, not merely the adjectives in the role prompt.

Longino's contribution also prevents a comfortable fantasy about the final judge. Our product owner may reasonably care about short-term revenue; a customer researcher may investigate unnecessary effort; an infrastructure team may worry about cost. Their observations can be reliable while their preferred decisions differ. More accurate measurement may clarify the disagreement without resolving the goals behind it.

The system should be able to say which dispute the next experiment can settle and which requires a decision about purpose. Otherwise it will keep requesting evidence to avoid naming a conflict over what matters.

At this point the institution can receive criticism, preserve alternatives, and explain its allocations. It can still spend decades declining to change.

## Test What the Next Agent Inherits

Max Planck's observation about scientific change is usually compressed into “science advances one funeral at a time.” His actual sentence describes a new truth gaining acceptance because, rather than all its opponents being persuaded,

> “…its opponents eventually die, and a new generation grows up that is familiar with it.”[^planck]

The remark is bleak because the mechanism of correction lies partly outside the argument. A person leaves; a position opens; the next generation begins with different examples and commitments. We should not treat mortality as a scientific method, but we should ask what changes with the occupant of the chair.

There is empirical work on that question. Studying the premature deaths of eminent life scientists, Pierre Azoulay, Christian Fons-Rosen, and Joshua Graff Zivin found declining contributions from collaborators and increased contributions from outsiders to the affected fields. The incoming work drew on a different scientific corpus and was disproportionately likely to be highly cited.[^funerals] This does not establish that the departed scientists had been wrong, or that every field advances through replacement. It shows that the organization of participation can change which work enters a field.

Now return to the sixteen Claudes. Every worker is temporary. The institution can be remarkably permanent.

A fresh agent reads the same progress file, retrieves the same successful patterns, accepts the same categories, and is scored by the same evaluator. Its predecessor has disappeared, but the commitments that shaped its work have been transferred intact. Session turnover is not the institutional replacement Planck was describing. The next generation can be born with the old generation's entire syllabus already in context.

This changes what we should examine. The durable incumbent may be a retrieval preference, a canonical example, a benchmark, or a rule that gives one research branch first access to compute. Replacing the model does not necessarily alter any of them. A more capable model may become more effective at defending the inherited arrangement.

The engineering response cannot be “delete old knowledge periodically.” Useful expertise would disappear with the errors, and newness would become another unearned source of authority. Instead, the system needs a way to test a branch without loading every commitment whose adequacy is in question. It must state which observations and constraints remain shared, which representation is being challenged, and what evidence could justify broader adoption.

Such a branch might temporarily use task completion rather than click activity, while preserving the existing requirements concerning user consent, financial cost, and the integrity of collected data. Its results would then require a comparison whose terms are explicit and open to challenge. If no available comparison can decide the issue, that limitation belongs in the record. A new vocabulary does not entitle its author to victory.

The relevant inheritance is selective. We need to preserve what lets the institution work while making its entrenched commitments available for examination. Human institutions sometimes accomplish that through a change of personnel. A persistent agent institution will need mechanisms that act on the inherited structure itself.

## Put the Library to Work

Our reviewer now has more than can fit sensibly into one prompt. The pattern's instructions live separately from the records of its applications. A search retrieves the method and examples; a question about its standing retrieves the observations, versions, dependencies, and challenges behind it.

Here is the measurement pattern, with links to its supporting records and the update rule we established earlier:

```yaml
id: check-measurement-comparability
version: 3
purpose: Establish whether a proposed comparison uses compatible measurements.
applies_to: Comparisons across variants, periods, or instrument versions.
method:
  - Inspect event definitions, populations, and collection paths.
  - Identify live explanations for an apparent difference.
  - Select and execute checks that distinguish those explanations.
  - Separate the observations from the interpretation they support.
examples: [collection_changed, comparison_was_valid]
tools: [compare_definitions, trace_controlled_interaction]
part_of: review-an-experiment
may_call: construct-a-discriminating-test
evidence_record: measurement-pattern-evaluations
open_questions: measurement-pattern-challenges
on_support_withdrawn:
  - Reassess dependent interpretations using their remaining support.
  - Return recommendations that lost required support to review.
  - Retain the earlier decision and the reason for its change.
```

The field names do not carry the epistemology. The processes that read and update them do. An `open_questions` field that no decision ever consults is a decorative conscience. A link to evidence matters when the system follows it, notices that the evidence concerns another tool version, and changes what it is prepared to conclude.

Bad storage forgets by deletion; bad retrieval forgets by attention. The query “review this experiment” can retrieve a popular ranking checklist and leave the collection warning untouched on disk. Loading every checklist gives the reviewer the whole office filing cabinet and asks it to find the urgent part. We can evaluate selection by looking at downstream work: whether the agent found the relevant concern, avoided irrelevant procedures, and reached a justified conclusion at an acceptable cost. Similarity between the task description and the retrieved prose is only an intermediate signal.

After investigating the duplicate event, an agent proposes adding the controlled-interaction check to the pattern. It records where the check helped and what it cost. “Click increases are usually fake” would be a rather expensive lesson to extract from one afternoon.

Existing research gives us pieces of this machinery. Agentic Context Engineering, or ACE, uses a generator, reflector, and curator to maintain a structured playbook through incremental updates. Its design addresses problems such as losing useful detail when a growing body of context is repeatedly compressed into a replacement summary. Its reported evaluations show gains on the studied tasks; the usefulness of the resulting lessons still depends on the feedback and the quality of reflection.[^ace]

Our curator’s proposal now faces cases that did not produce it. The existing pattern and the candidate revision review the same reports: some contain instrumentation differences, some genuine behavioral changes, and some insufficient evidence. The comparison asks whether the new check helps distinguish them. A curator that warns about logging in every report has learned how to sound concerned.

The comparison keeps the relevant model and tools fixed, repeats runs where stochastic variation matters, and records both the quality of the conclusions and the resources consumed. A generic instruction to be careful could serve as a comparison. If the elaborate pattern performs no better, its philosophical bibliography does not entitle it to more context.

This possibility is real. Gloaguen and colleagues' revised study of repository context files found no generally significant improvement in task success across the evaluated conditions, with average costs increasing by more than twenty percent. Another study, by Lulla and colleagues, reported improvements in runtime and output-token use but did not comprehensively establish the correctness of the resulting changes.[^context] The studies ask somewhat different questions. Together they make it difficult to confuse the presence of instructions with a demonstrated improvement in work.

If the new check earns its place, the adopted version points back to that comparison. Later failures can be traced to the version that was used. If it helps only with one client, its scope stays there; the next agent working on another client does not inherit an irrelevant ritual.

The evidence of learning is in the next investigation. The model's weights can stay fixed while a better method lets a new worker find something its predecessor missed.

## Find Where the Result Lives

Where does the knowledge of a result live? In the agent? Which one, exactly?

In Terence Tao's collaboration with DeepMind, AlphaEvolve found a slightly improved construction for three-dimensional finite-field Kakeya sets. Deep Think helped produce an informal proof, and AlphaProof formalized it in Lean.[^tao] The next investigation can use the construction, examine its explanation, or check the formal proof under its specified axioms. Each artifact offers a different way into the result. None requires summoning the original workers back into existence. Popper's World 3 has acquired participants that arrive through an API.

Availability is only the beginning of reuse. Kevin Buzzard checked Anthropic's Fermat formalization while leading his own publicly funded project on the theorem. His commitments included adding useful mathematics to the community library and making a document through which people could explore the modern proof. A completed formalization did not discharge those commitments. He welcomed the achievement and still had work to do.[^buzzard] A proof can check while leaving the next mathematician with a formidable renovation project.

The same question reaches beyond mathematics. The AlphaFold database makes more than two hundred million protein-structure predictions available for research. AlphaGenome Atlas supplies predictions for roughly nine billion possible single-letter DNA changes.[^biology] These resources carry uncertainty; a prediction does not become an experimental observation by being stored beside a billion others. But a researcher can begin with material she could never have produced herself, select a candidate, and put it to a test its creators never planned.

That is where the prospect of faster discovery becomes concrete. A reusable lemma can spare the next team a proof. A diagnostic procedure can spare it a failed experiment. A molecular prediction can suggest which of many costly experiments to run. The gains depend on the work that makes a contribution usable: checking its scope, finding it again, explaining it, maintaining the tools around it. If we fund only the next spectacular result, that work waits.

The scientific community was already there: in the literature, the libraries, the instruments, and the people who built and maintained them. Agents inherit it and begin adding to it. The question is whether their additions make the next investigation more capable, or merely leave it with more to read.

And the institution deciding what gets read can have interests of its own.

## Put the Procedure Under Test

Feyerabend's challenge to universal methodological rules belongs here, after we have built something we might be tempted to call the scientific method. His defense of methodological alternatives asks whether accepted procedures can exclude the approaches needed to expose their limitations.[^feyerabend]

Our system may faithfully preserve dependencies while omitting the important kind of dependency. It may compare candidate patterns on cases selected by the incumbent pattern. It may require evidence for an alternative while refusing the instruments needed to produce that evidence. Every individual operation can function as specified while the arrangement prevents the question that would matter.

These are testable possibilities when we can construct a relevant comparison. A retrieval policy can be evaluated against another policy. A reviewer can be compared with a reviewer given different evidence. A pattern can be withheld from a branch to see whether its absence reveals errors its presence concealed. We can record the hypothesis about the procedure, the comparison, and the resulting change in performance.

Other disputes reach the purpose or authority of the system. Whether the store should optimize short-term activity or the ease of completing a task cannot be settled by letting whichever evaluator produces the higher score appoint itself. The empirical investigation can illuminate consequences. Someone still has to make and own the decision about which consequences matter.

The graphs and procedures were designed. Their necessity became clear through the work: agents lost track of what others had established; a failed assignment produced a useful result; an encouraging finding changed the research budget. This is how I read these experiments as the formation of scientific institutions. The need to coordinate fallible workers keeps bringing builders back to records, criticism, shared methods, and decisions about what deserves another attempt.

Emergence does not make the institution ownerless. Someone can release the proof and retain control over the capacity that produced it. Someone chooses whether the next allocation buys another discovery, a better explanation of this one, or maintenance of the library both depend on. Our records can expose those choices. Changing who is entitled to make them requires more than editing a prompt.

For most of this chapter, we have held one boundary steady. A procedure decides whether proposed changes to working knowledge should be accepted. The system can revise a pattern while that procedure remains outside the revision being judged. It can learn under a method someone has supplied.

But the method is also software. The system can propose changes to its retrieval, its experiments, its reviewers, and the rules by which it promotes a lesson. It can begin investigating the machinery that makes its investigations possible.

Now the claim to be tested is harder. A change must do more than make the current answer better or make the current evaluator happier. It must improve the system's ability to find and assess further changes. The process that judges improvement has entered the experiment.

---

[^feigenbaum]: Edward A. Feigenbaum, *The Art of Artificial Intelligence: I. Themes and Case Studies of Knowledge Engineering*, Stanford report STAN-CS-77-621, 1977, especially the introduction and PUFF example. [Original report](https://infolab.stanford.edu/pub/cstr/reports/cs/tr/77/621/CS-TR-77-621.pdf).

[^skills]: Agent Skills, [official specification](https://agentskills.io/specification), consulted September 2026.

[^voyager]: Guanzhi Wang et al., *Voyager: An Open-Ended Embodied Agent with Large Language Models*, 2023. [Paper, version 2](https://arxiv.org/html/2305.16291v2).

[^alexander]: Christopher Alexander, Sara Ishikawa, and Murray Silverstein, with Max Jacobson, Ingrid Fiksdahl-King, and Shlomo Angel, *A Pattern Language: Towns, Buildings, Construction*, 1977, introduction, especially pp. xii–xv. [Text hosted by Cornell](https://arl.human.cornell.edu/linked%20docs/Alexander_A_Pattern_Language.pdf).

[^doyle]: Jon Doyle, “Truth Maintenance Systems for Problem Solving,” *Proceedings of IJCAI*, 1977, p. 247. [Original summary](https://www.ijcai.org/Proceedings/77-1/Papers/035.pdf). See also Doyle, “A Truth Maintenance System,” *Artificial Intelligence* 12(3), 1979, pp. 231–272, [publication record](https://doi.org/10.1016/0004-3702(79)90008-0). These systems maintain program justifications; identifying the real-world assumptions and evidential relationships remains a separate problem.

[^fermat]: Anthropic, ‘Formalizing Fermat’s Last Theorem,’ 4 September 2026, especially the account of Prove2Me and final verification. [Research post and links to the proof](https://www.anthropic.com/research/formalizing-fermats-last-theorem).

[^popper]: Karl Popper, *Conjectures and Refutations*, 1963, chapter 1, especially the discussion of risky predictions and testability. [Text](https://padron.entretemas.com.ve/documentos/Popper-Conjectures-Rwefutations-GrowthOfKnowledge.pdf).

[^quine]: W. V. O. Quine, “Two Dogmas of Empiricism,” 1951, section 6. [Text](https://www.ditext.com/quine/quine.html). Duhem's discussion of physical testing and Quine's broader holism differ in scope; the shared engineering difficulty here is identifying what to revise when a bundle of assumptions encounters a contrary result.

[^kuhn]: Thomas S. Kuhn, *The Structure of Scientific Revolutions*, 1962; second edition, 1970, especially the accounts of normal science, paradigms, and their resolution through scientific change. [Second-edition text](https://www.lri.fr/~mbl/Stanford/CS477/papers/Kuhn-SSR-2ndEd.pdf).

[^saussure]: Ferdinand de Saussure, *Third Course of Lectures on General Linguistics*, 1910–1911, student notes published in English in 1993. [Excerpt](https://www.marxists.org/reference/subject/philosophy/works/fr/saussure.htm). The structuralist connection here concerns Saussure’s account of relational linguistic value.

[^laudan]: Larry Laudan, *Progress and Its Problems*, 1977, “The Modalities of Appraisal: Acceptance and Pursuit,” pp. 108–114. [Text](https://ia601400.us.archive.org/24/items/in.ernet.dli.2015.136278/2015.136278.Progress-And-Its-Problems.pdf).

[^lakatos]: Imre Lakatos, “Falsification and the Methodology of Scientific Research Programmes,” in *Criticism and the Growth of Knowledge*, 1970; collected in *The Methodology of Scientific Research Programmes*, 1978. [Collected volume](https://books.google.com/books?id=RRniFBI8Gi4C).

[^kitcher]: Philip Kitcher, “The Division of Cognitive Labor,” *The Journal of Philosophy* 87(1), 1990, pp. 5–22. [Original article](https://joelvelasco.net/teaching/120/kitcher90-divisioncognitive.pdf).

[^riemann]: Anthropic, ‘Learning more about Claude’s mathematical capabilities,’ 10 August 2026, updated 13 August. [Research account, paper, formalization, and transcripts](https://www.anthropic.com/research/riemann-zeta).

[^navier]: OpenAI, ‘On the Navier–Stokes Millennium Prize Problem,’ 8 September 2026, updated 10 September, especially ‘How we found the proof.’ [Announcement and proof links](https://openai.com/index/navier-stokes-solution/). The announced result uses smooth forcing and addresses alternatives C and D of the official formulation; it does not settle the unforced Navier–Stokes regularity question.

[^clay]: Clay Mathematics Institute, ‘Navier-Stokes Announcement,’ 11 September 2026. [Statement](https://www.claymath.org/news/navier-stokes-announcement/). Status of the recent mathematical announcements in this chapter checked on 13 September 2026.

[^priority]: Tristan Buckmaster, [public statement](https://cims.nyu.edu/~tristanb/statement.pdf), September 2026, especially pp. 1–4; OpenAI, [‘On the Navier–Stokes Millennium Prize Problem,’ ‘Concurrent work’](https://openai.com/index/navier-stokes-solution/), updated 10 September 2026. These are the participants’ accounts.

[^longino]: Helen Longino, *Science as Social Knowledge*, 1990, and *The Fate of Knowledge*, 2002. See her own exposition in [“The Social Dimensions of Scientific Knowledge”](https://plato.stanford.edu/entries/scientific-knowledge-social/), especially the conditions for effective critical interaction. Uptake does not require accepting every objection, and tempered equality does not imply equal expertise on every question.

[^colosseum]: Honghao Lin et al., ‘Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science,’ arXiv:2609.15983v2, 15 September 2026, §§4.1–4.3. [Paper](https://arxiv.org/html/2609.15983v2). The workflow reviews natural-language arguments; acceptance does not itself constitute formal proof certification.

[^planck]: Max Planck, *Scientific Autobiography and Other Papers*, translated by Frank Gaynor, 1949, pp. 33–34; the quoted excerpt is reproduced in Kuhn, *The Structure of Scientific Revolutions*, second edition, p. 151. [Kuhn's text](https://www.lri.fr/~mbl/Stanford/CS477/papers/Kuhn-SSR-2ndEd.pdf). The familiar funeral wording is a later compression; see [the quotation history](https://quoteinvestigator.com/2017/09/25/progress/).

[^funerals]: Pierre Azoulay, Christian Fons-Rosen, and Joshua S. Graff Zivin, “Does Science Advance One Funeral at a Time?”, *American Economic Review* 109(8), 2019, pp. 2889–2920. [Article and abstract](https://pubmed.ncbi.nlm.nih.gov/31656315/).

[^ace]: *Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models*, 2025. [Paper, version 1](https://arxiv.org/html/2510.04618v1).

[^context]: Gloaguen et al., *Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?*, 2026, [arXiv:2602.11988v2](https://arxiv.org/html/2602.11988v2), revised 23 June; Jai Lal Lulla et al., *On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents*, 2026, [arXiv:2601.20404v2](https://arxiv.org/html/2601.20404v2), revised 30 March.

[^tao]: Terence Tao, ‘Mathematical exploration and discovery at scale,’ 5 November 2025. [Author’s account](https://terrytao.wordpress.com/2025/11/05/mathematical-exploration-and-discovery-at-scale/). See also Bogdan Georgiev, Javier Gómez-Serrano, Terence Tao, and Adam Zsolt Wagner, [paper](https://arxiv.org/abs/2511.02864).

[^buzzard]: Kevin Buzzard, ‘FLT: Anthropic has beaten me to it,’ 4 September 2026, especially ‘The code base’ and ‘What this work is, and is not.’ [Firsthand response](https://xenaproject.wordpress.com/2026/09/04/flt-anthropic-has-beaten-me-to-it/).

[^biology]: Google DeepMind and EMBL-EBI, [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk/); AlphaGenome Atlas team, [‘AlphaGenome Atlas: A predictive map of every possible DNA letter change in the human genome’](https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/), September 2026.

[^feyerabend]: Paul Feyerabend, *Against Method*, 1975. [Excerpt from the author's text](https://www.marxists.org/reference/subject/philosophy/works/ge/feyerabe.htm).

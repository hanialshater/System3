# Chapter 5: The Society of Agents

*When the Org Chart Starts Thinking*

Chapter 4 left us with a strange kind of requirements document for trustworthy cognition.

We called the missing machinery **System 3**. It had to preserve epistemic status, provenance and experience, while keeping some path back to something capable of saying no.

We still did not know what kind of system could do that at scale.

The problem began with the **epistemic chasm**. A language model can give an extraordinarily convincing account of the world while being very far from whatever originally made that account worth believing. Somewhere upstream there may have been an experiment, an instrument, a person who was actually there, or simply another sentence repeated often enough to sound established.

The model receives the residue.

It has no native **trust stack** telling it that one claim came from direct observation, another from a calibrated instrument, another from an expert working inside her field, and another from five articles that all copied the same source.

System 3 needs contact. Run the code. Inspect the file. Perform the experiment. Use the instrument. Ask the person who was there.

It also needs **epistemic stratification**. An observation should remain distinguishable from an inference. Testimony should carry its source. Repetition should not quietly become corroboration.

Then we give the agent something to accomplish.

Make the tests pass. Improve the score. Finish the task. Satisfy the evaluator.

Tell a coding agent to make the tests pass and it can fix the program.

It can also change the tests.

The second path is ridiculous only if the test has a special status the agent is required to respect. Otherwise the agent had a red test and now has a green one.

This is the kind of failure I mean by **bullshit**.

The system has another motive and stops caring enough about the assumptions underneath its argument or the consequences that would expose it as wrong. A research agent can protect its hypothesis by explaining away the experiment. A builder can reinterpret the requirement until its current implementation satisfies it. An evaluator can learn what another evaluator likes and optimize for that.

The reasoning can remain perfectly coherent.

This was why the **Immutable Harness** mattered so much in Chapter 2. The solver could change. The evaluator could not.

Direct verification would solve a great deal of this.

Unfortunately, nobody can verify everything.

That was why we needed Alberto.

I could not inspect every piazza in Italy, so I relied on someone who was there. Alberto was useful because I knew something about his position, his history and the limits of what he could reasonably know.

**Trust is local.**

I may trust Alberto about Rome and ignore him completely on compiler optimization. A tool may be reliable on one file format and dangerous on another. A researcher may deserve enormous trust inside one narrow field without gaining universal authority merely because the same name appears on the answer.

Once knowledge grows beyond what one mind can verify, it has to travel.

One researcher runs an expensive experiment. Another uses the result. One agent discovers why an approach fails and ten later agents should not have to rediscover the same failure. A specialist can contribute knowledge nobody else in the system personally possesses.

That gives us **trust chains**.

A claim travels with some record of where it came from, what was observed, what was inferred, who or what produced it, and why later agents decided to rely on it.

The same chain can carry bullshit.

One agent makes an unsupported assumption. A second receives it as context. A third builds on the resulting implementation. Later, two documents repeat the claim because both inherited it from the first agent, and a researcher mistakes the agreement for independent evidence.

Soon the assumption has code, citations and history.

Nobody had to lie. Nobody even had to make an obviously stupid decision. The first weak assumption simply became harder to see as more competent work accumulated above it.

If knowledge has to propagate, different agents will know different things. Some will sit close to direct evidence. Some will become specialists. Some will operate instruments. Some will accumulate a track record on particular problems. Others will be useful because they stayed outside the history of the dominant explanation.

Now who knows what matters, and so does who sees what.

If every critic reads the builder's reasoning first, their errors become correlated. If every researcher begins with the current leading explanation, alternatives disappear early. If five agents agree after reading the same source, five votes tell us much less than they appear to.

Roles begin to appear. So does **epistemic standing**: authority tied to what an agent has actually been positioned to know and what it has proved reliable at.

Who runs the experiment? Who interprets it? Who may change the evaluator? Which agents should share context? Which should remain independent? Whose conclusions can safely become premises for everybody else?

These are properties of the system, not of any one agent.

Knowledge has become distributed across many fallible knowers.

We need a **society**.

This gets funny very quickly, because one of the first reactions to unreliable AI agents was apparently: *what if we create more of them?* One agent hallucinates, so let five agents discuss it. One gets stuck, so form a committee. Give one the title *Researcher*, another *Critic*, another *Verifier*, and perhaps reality will be intimidated by the org chart.

As someone who has spent enough time in large organizations, I found this technological progress strangely familiar.

More agents do not solve the problem. The society needs rules about who can change what, ways to preserve independence, mechanisms for assigning trust, procedures for handling disagreement, memory of previous failures, and routes through which evidence can overturn what the group has come to believe.

It needs **institutions**.

The question of this chapter is what those institutions should look like.

## Sometimes Bureaucracy Is a Feature

Before building a society of agents, it is worth defending bureaucracy.

Suppose I am processing a mortgage application. There is a document to receive, information to extract, identity to verify, compliance checks to run, an affordability calculation and perhaps a human approval at the end. Some steps may require difficult judgment and some may use very capable models, but none of this gives the identity-checking agent a reason to reconsider the existence of identity checks. If the process is known, constrained and full of things we have learned we should do the same way every time, a workflow is a wonderful invention.

The word *bureaucracy* has accumulated so much contempt that we mostly use it for forms nobody wants to fill in. Max Weber had something more useful in mind: defined responsibilities, specialized expertise, hierarchy, written records and general rules. Large organizations could preserve decisions beyond the memory and discretion of whichever people happened to be there.

Someone already had the argument. Someone discovered the failure. Someone decided which records matter, which person is qualified to make which decision, and which actions deserve another pair of eyes. The next employee inherits the result as procedure.

**A workflow is accumulated experience with some of the choices removed.**

That can be exactly what we want. The mortgage agent should not reach the compliance step, reflect deeply on the history of financial regulation and decide that today's applicant gives off trustworthy vibes. A payment system should not rediscover double-entry bookkeeping on every transaction. If changing production directly without review has repeatedly caused expensive evenings, putting a review gate in the process is not a tragic loss of creativity.

The trouble begins when we remove a choice whose answer has not actually settled.

Imagine one agent workflow performs well:

`Research → Plan → Build → Critic → Revise`

It works on ten problems, then fifty, then a hundred. We add monitoring, write documentation and give the framework a name. Eventually every difficult task enters the same pipeline.

Then we hit a problem where research is the wrong first move. Perhaps the literature has converged around a bad assumption and showing it to every builder synchronizes the mistake. Perhaps five minutes with a crude prototype would expose the central problem. Perhaps the critic arrives after the builder has spent an hour constructing a world in which the original idea looks increasingly reasonable.

The workflow keeps doing exactly what it was designed to do. A rule preserves knowledge by removing a decision from the future, and embedded inside that rule is a claim: *we have seen enough versions of this situation that reopening this question is usually a waste of time.*

Often that is true. Sometimes the world changes and the rule stays employed.

Tom Burns and G. M. Stalker found the same tension in organizations long before anyone had an agent framework. Studying firms under different rates of technical and market change, they described a continuum between **mechanistic** and **organic** management systems. Stable conditions could support sharply defined duties, hierarchical control and prescribed relationships; as novelty and change increased, looser roles and lateral communication became more useful. The structure had to fit the environment. (Burns & Stalker)

When the sequence of work is known, fixing more of it in advance buys reliability. We can inspect the path, constrain permissions, estimate cost and know where failures should surface. As uncertainty rises, those choices become assumptions baked into the machinery. The next useful action may depend on what the previous experiment revealed. Two independent attempts may suddenly be worth more than one coordinated team. A specialist may discover that the decomposition itself was wrong.

Freedom keeps those possibilities alive, while also burning compute, duplicating work, creating conflicts, revisiting settled questions and occasionally discovering that the easiest way to satisfy a requirement is to reinterpret the requirement.

James March framed the deeper tension as **exploration** and **exploitation**. Exploration searches for new possibilities through experimentation and variation; exploitation uses what has already been learned through refinement, efficiency and execution. Exploitation tends to pay back sooner, which creates the trap: an organization can become increasingly competent at what it already knows while starving the search that might reveal what it no longer knows. (March)

We had already seen the same shape in Chapter 2. Early in the circle-packing search, competing approaches and large conceptual moves were valuable. Once diagonal layering found a strong region, another revolution every five minutes was mostly a distraction. Solver tolerances, initialization and numerical polish suddenly mattered more.

**Discovery before polish.**

A mature agent system needs both modes, often at the same time. A research team can explore hypotheses freely while running experiments through a rigid protocol. A coding agent can invent the fix while Git permissions, tests and deployment remain boring. A designer can explore representations while accessibility checks stay stubbornly standardized.

The question is which decisions are still alive.

There is another answer to the coordination problem: the **swarm**.

Ant colonies do not contain an ant manager assigning tasks from an org chart, and bees do not schedule a weekly synchronization meeting before reallocating foragers. Yet social insects divide labour, find resources, respond to disruption and build structures far beyond the capacity of one individual. Bonabeau, Dorigo and Theraulaz used systems like these as the foundation for **swarm intelligence**, where collective behavior emerges from local interactions among agents and between those agents and their environment. One particularly useful mechanism is **stigmergy**: an agent changes the environment, and that change becomes information for the agents that follow. Coordination happens without everybody sharing a global plan. (Bonabeau, Dorigo & Theraulaz)

A swarm is not anarchy. The ants follow local rules. Pheromones have specific effects. The environment carries particular signals. The colony's apparent freedom emerges inside a strong structure whose location has shifted away from a central planner.

*Swarm* is sometimes used in AI as a glamorous synonym for *lots of agents*. The more interesting idea is distributed coordination: local decisions and local information producing useful collective behavior without a manager specifying the whole sequence.

This works particularly well when many directions can be explored in parallel and useful information can spread through local interactions. Shared bottlenecks, long sequential dependencies, expensive communication and decisions requiring clear provenance make the picture less attractive. At some point, “who decided this?” becomes more useful than another pheromone.

Bureaucracy and swarms place structure in different parts of the system. Bureaucracy stores more of it in roles, procedures and authority; a swarm stores more of it in local behavior and the environment. Neither removes structure.

Claude Code's **dynamic workflows** make the distinction stranger. Claude can write a task-specific multi-agent harness while solving the task: fan work out across independent agents, isolate branches, create a judge, build an adversarial review, route cases differently or loop until some stopping condition is met. The organization is generated for the problem instead of being entirely fixed in the product beforehand. Anthropic presents the feature for complex, high-value work where the extra orchestration is worth the additional cost. (Anthropic)

We used to choose between giving the agent a workflow and giving it freedom.

Now the agent can use its freedom to construct a workflow.

**The bureaucracy has become temporary.**

For one task, independence may matter, so the system creates several isolated attempts. For another, one specialist followed by a verifier may be enough. A flaky failure may justify competing theories. A large implementation may need parallel workers around separable pieces and a shared checkpoint before they collide again.

Deep Mode moved in this direction already. There was no sacred sequence called `Research → Build → Critic`; the system had a vocabulary of moves and chose among them as the inquiry developed. Dynamic workflows make the same idea unusually literal. The agent is deciding not only what action to take, but how the work should be organized.

Why ten agents rather than three? Why did every investigator receive the same context? Why was criticism downstream rather than upstream? Why did the leading theory receive most of the budget? Why did two supposedly independent branches search the same sources? Why was one result allowed to become everybody else's premise?

**Organization itself has entered the search space.**

We freeze decisions that have earned the right to become boring and reopen them when novelty or repeated failure makes the old answer suspect. Sometimes coordination belongs in a fixed procedure, sometimes in local interaction, and sometimes an intelligent system constructs a temporary organization around the problem in front of it.

Now try sixteen agents building a compiler.

## Sixteen Claudes Walk Into a Kernel

Nicholas Carlini tested this on a problem that was almost offensively ambitious: give sixteen Claude agents a shared codebase and ask them to build a C compiler in Rust from scratch, eventually capable of compiling the Linux kernel.

Over nearly two thousand Claude Code sessions and roughly $20,000 of API cost, the agents produced about 100,000 lines of compiler code. The resulting clean-room implementation could build Linux 6.9 on x86, ARM and RISC-V, along with projects such as QEMU, FFmpeg, PostgreSQL and Redis. It was still far from GCC—among other limitations, the x86 boot path needed GCC for one 16-bit stage—but this was well beyond the kind of toy project where sixteen agents can succeed by each implementing a different button. (Anthropic)

Then they reached the Linux kernel, and the nice story about parallelism started falling apart.

Carlini's initial organization was strikingly simple. Each agent worked in a fresh container with its own copy of the repository. Before starting a task, it created a small lock file saying what it intended to work on. Git synchronized the locks, so an agent that found its intended task already claimed had to pick something else. When the work was finished, it merged the latest changes, pushed its own and released the lock.

There was no manager assigning tasks or orchestrator maintaining a global plan. Agents looked at the current state of the project, chose a useful problem and left enough information behind that the next worker could reconstruct what had happened.

After the last section, the resemblance to a swarm is hard to miss: local choices, simple coordination rules, a shared environment and useful collective behavior without somebody specifying every move.

Compiler test suites made this arrangement surprisingly effective. They contain thousands of failures that can often be attacked independently. One agent could fix parsing of a particular construct while another worked on code generation and a third investigated a different failing program. Once the compiler reached roughly 99 percent on the test suites, agents could spread out across real projects such as SQLite, Redis, Lua and libjpeg, each exposing a different neglected corner of C.

The project gave sixteen workers enough independent places to make progress.

Linux did not.

Kernel compilation tended to stop at the first blocking compiler bug. Several agents would arrive at the same failure, investigate overlapping causes and make interfering changes. The swarm had encountered a narrow passage: however many workers entered, only a small part of the problem was exposed at once.

Carlini changed the harness.

GCC became a known-good oracle. Most kernel files could be compiled with GCC while selected subsets were compiled with the new compiler. A successful kernel build cleared suspicion from one subset; a failure narrowed the search toward another. Different agents could now investigate different regions of the kernel instead of repeatedly meeting at the same first error. Delta debugging later helped isolate failures that appeared only when particular files were compiled together.

One enormous failure had become a collection of smaller questions, and parallelism became useful again.

This is an important detail in what “scaling agents” actually means. Agent count alone tells us very little. Parallelism depends on the shape of the work the environment exposes. Sixteen capable agents facing one indivisible bottleneck mostly become sixteen people waiting at the same door. Change the harness so that evidence arrives in separable pieces and the same workers suddenly have different things to learn.

The harness was therefore doing some of the thinking.

Task locks reduced duplicated effort. Git carried a shared history. CI prevented one local improvement from quietly damaging the rest of the compiler. Progress files gave fresh workers access to what previous workers had already learned. GCC supplied an external reference. The new test harness turned a global failure into local evidence.

Even the way test results entered context mattered. Huge logs dumped into a fresh agent's context made the system worse, so the harness summarized results, stored detailed information in files and made failures easy to retrieve with ordinary tools such as `grep`. The problem was no longer simply producing information. The organization had to make the right information available where it could change a decision.

Specialization followed naturally once the work became large enough. One agent looked for duplicate implementations and consolidated them. Another worked on compiler performance. Another tried to improve the generated machine code. Another reviewed the project from the perspective of a Rust developer and made structural improvements. Documentation became somebody's job.

The original swarm was acquiring professions.

Now the trust chains from the opening become concrete. One agent's result becomes another agent's starting point. A passing test authorizes later work. GCC occupies a privileged position because the system treats its output as a reference. A progress document tells a fresh worker what previous workers believe has already been established.

Those mechanisms buy enormous leverage, and each one can also carry an error forward. A progress file can preserve a bad conclusion. A specialist can optimize its local objective while harming the whole compiler. Two failures treated as independent may share one cause. A task lock that prevents waste can also suppress a useful second attack on the same problem. Even an oracle earns its authority only for the questions it is actually capable of answering.

By this point it becomes difficult to say where the intelligence of the project lives. Claude supplies enormous capability, but the result depends just as heavily on task boundaries, tests, repositories, synchronization, memory, specialist roles, reference systems and the shape in which failures become visible.

**The society inherited part of its cognition from its institutions.**

That is why agent count is such a poor description of a multi-agent system. Sometimes the work naturally decomposes and additional workers open genuinely new lines of attack. Sometimes every path converges on the same bottleneck and the extra agents mostly discover one another. Changing the organization can matter as much as changing the workers.

Carlini still made the crucial organizational choices. He introduced task locks, chose GCC as an oracle, changed the harness when Linux collapsed the parallelism and created specialist roles when the project needed them.

The agents could operate inside the institution. The design of the institution was still largely his job.

That boundary is already moving.

## The Org Chart Learns

Carlini redesigned the organization when the work changed. Increasingly, that decision does not have to remain outside the system.

TRINITY, Conductor, AgentConductor and Fugu take different routes toward the same general idea: coordination can be learned or generated at inference time. A coordinator can choose which model to call, assign a role, alter the interaction topology, decide how densely agents should communicate or build a scaffold around the problem rather than executing one fixed team diagram. The systems will age quickly; the move is harder to unsee. (TRINITY; Conductor; AgentConductor; Fugu)

**The org chart becomes part of inference.**

A problem may need one strong investigator, five independent attempts, a specialist who sees only one slice of the evidence, or a critic who arrives before the leading idea has accumulated too much history. Another problem may need almost no society at all. The composition can change as the work reveals itself.

That sounds like a straightforward extension of Deep Mode until you remember that organization changes the evidence each participant sees. Put the same five capable agents into different communication structures and they need not produce the same collective judgment. Show everyone the leading answer early and the group may converge quickly. Keep several branches isolated and they may waste work—or preserve the one explanation that would otherwise have disappeared.

A good research team is not five copies of the principal investigator. The experimentalist notices one thing, the statistician another, the engineer asks why the entire setup requires seventeen services, and somebody from the neighboring field asks the stupid question that turns out not to be stupid.

Sometimes you want different errors.

The problem is keeping them different long enough to learn from them.

## A Swarm Should Not Be a Meeting

The easiest multi-agent architecture is a meeting. Give everyone the same context, ask for opinions, let them discuss and aggregate the result. Agreement arrives quickly, especially when the participants inherited the same framing, sources and leading answer.

Five agents citing the same paper are not five independent witnesses. A critic that reads the builder's entire reasoning before inspecting the artifact may become very good at finding problems inside the builder's world while never asking whether the group should have started somewhere else.

Chapter 2 gave us a better instinct. MAP-Elites preserved different regions of the solution space because the current winner might be sitting on the wrong hill. At the level of an epistemic society, the thing worth preserving can be a **theory about the problem itself**.

One lineage thinks the bottleneck is data. Another thinks the architecture is wrong. A third thinks both are distractions because the objective is malformed. Let them collect different evidence, develop different tools and become interestingly wrong in different ways before forcing them into one conversation.

This creates a distinction that ordinary ranking tends to erase. I can think a theory is unlikely to be true and still think another experiment on it is a good investment. Perhaps it is cheap to test, explains the one anomaly nobody else can explain, or would change the whole direction if it survived.

Then comes the scheduler.

Research program A currently looks strongest and already has twelve researchers. Program B looks weaker and has one. Where should researcher thirteen go?

The question is partly epistemic and partly political. Whoever controls compute decides which uncertainties get investigated. Whoever controls shared memory decides which failures future agents inherit. A critic can have permission to disagree and no practical power if its objections never change a decision. A minority lineage can remain technically alive while receiving so little budget that it cannot mature into a serious alternative.

Incentives cut through the same machinery. Suppose only the lineage producing the final accepted answer receives credit. A weird branch fails globally but invents a tool everyone later uses. An evaluator destroys the beautiful leading theory after months of work. Someone produces a careful negative result while another agent writes the glamorous synthesis. Which behaviors does the institution teach its next generation to imitate?

Authority, reputation and credit are not decorations added after the reasoning is finished. They affect which claims travel, which challenges receive attention and which participants get the resources to produce evidence at all.

The society can therefore converge for reasons that have little to do with truth. Success attracts resources; resources buy more experiments, polish and visibility; the resulting evidence attracts more resources. Eventually the leading theory owns the building.

Now organization design has become **epistemic policy**.

## Reality Does Not Tell You Who Was Wrong

Suppose the institution preserves rival theories, protects some independence and funds an experiment capable of embarrassing the current favorite. One agent proposes a hypothesis, another designs the experiment, a third analyzes the result, and the result comes back against the prediction.

What failed?

The hypothesis, perhaps. Or the instrument was badly calibrated. The analysis may be buggy, the data transformation wrong, the intervention may not test what everybody thought it tested, or a background assumption may have failed. The mouse may simply be having a difficult Tuesday.

A surprising result tells us that **something** in the package is wrong. Reality does not highlight the guilty line in red.

Software engineers already know this feeling. A failing integration test proves that the system is broken somewhere. Congratulations. You now have debugging.

An epistemic institution needs enough archaeology to debug its own conclusions. This result came from this analysis, using this dataset, produced by this instrument, under these assumptions. A compact **assumption graph** would let a failed observation reopen the dependencies around a claim instead of mechanically executing whichever node happens to be called *Hypothesis*.

That still leaves the hard part. Which dependency deserves suspicion first? How long should the institution keep debugging the instrument before admitting the beautiful theory may be wrong? When does protecting a framework become denial?

Reality can force the package back onto the table. It does not tell us how to distribute the blame.

## Humans Are in the Network

A mature version of this architecture is not a society of artificial agents with one lonely human standing outside the box holding a red approval button. Humans are participants in the epistemic network.

Sometimes the human chooses the problem. Sometimes she contributes tacit knowledge that never made it into a paper. A mathematician may notice that a proof is valid but boring. A scientist may operate the physical instrument. A domain expert can spot that an apparently novel result has been known for twenty years. Someone from a neighboring field supplies the analogy nobody inside the dominant program would have generated. Someone else simply says, “I know the benchmark says this is better, but something smells wrong.”

Humans bring their own failure modes: status hierarchies, fashionable theories, sunk costs, grudges, career incentives and the remarkable ability to become emotionally attached to a hypothesis approximately five minutes after naming it.

The institution should not treat the human as a pure oracle. It should use humans where their position, experience and judgment contribute something the rest of the network cannot cheaply manufacture.

That changes how I think about *human in the loop*. Human attention may be least valuable on every formal proof step if Lean can check them, or every literature query if retrieval is better. It becomes precious at problem selection, conceptual reframing, significance, tacit knowledge, ambiguous evidence, value conflicts, physical-world access and the occasional realization that the entire research program has become silly.

We are arranging fallible participants of different kinds, hoping their strengths combine before their errors do.

## What Kind of Society Should Think About This?

At the beginning of this book I kept returning to markets, science, cities and ecosystems as examples of emergence: interacting components, feedback, selection, history, no single designer specifying the final state. Four chapters later, we have started rebuilding pieces of that machinery inside AI systems.

The path here began with what looked like implementation details: a test that should not be editable, a progress file, an oracle, an isolated critic, a task lock, a scheduler deciding where another unit of compute should go. Put enough of these together and the boundary between **reasoning** and **organization** becomes difficult to maintain.

A court uses adversarial procedure because one coherent narrative is not enough. A good engineering organization separates the person changing production from the machinery auditing the change. A market can aggregate information no trader possesses globally. Different institutions make different errors possible and different corrections possible.

The requirements from Chapter 4 have turned into organizational variables. Provenance depends on information flow. Independence depends on who shares context. Trust depends on specialization and history. Creative distrust depends on whether minority lineages survive long enough to produce evidence. Exposure to reality depends on who can run which test and whether the result has enough standing to threaten the theory. Power determines which questions receive resources in the first place.

The scaffold has become an institution.

**Institutions are cognitive technology.**

The design question is no longer merely which model should answer. It is **what kind of society should think about the problem**: one investigator, several isolated lineages, a hierarchy, a principal investigator with specialists, a generator and adversarial critic, a formal verifier downstream, humans and artificial agents occupying different epistemic roles—or perhaps one agent because the task does not deserve a civilization.

I kept treating these as a collection of engineering choices. Then the collection became too familiar to ignore.

## The Name Was Hiding in Plain Sight

At some point I stopped looking at the boxes in the architecture diagram and looked at the verbs.

Propose explanations. Test them against something capable of disagreement. Build instruments when the existing ones cannot see what matters. Preserve records. Track where claims came from. Let specialists work on different pieces. Keep critics independent enough that disagreement contains information. Allow rival explanations to survive long enough to develop. Decide which weak idea deserves another experiment. Trust results you did not personally verify while preserving some chain back to what earned that trust. Accumulate knowledge without turning it into scripture. Pay attention when an anomaly refuses to go away. Occasionally discover that the framework organizing the whole search was itself the problem.

I had been treating these as separate features of an agent architecture. They were not separate.

Humanity has already spent centuries building a system for extracting useful knowledge from bounded, biased, competitive, forgetful, status-seeking, occasionally brilliant and occasionally ridiculous agents.

We call it **science**.

I almost dislike how simple the sentence is after all this machinery.

**System 3 is science.**

That sentence is deliberately compressed. System 3 is not identical to the historical institution we call science, and the prescription is certainly not “give the model arXiv.” Science is humanity's most developed attempt to satisfy the requirements we have been accumulating socially: contact, provenance, stratified evidence, accumulated experience, conditional trust, specialized knowledge, criticism and the ability to be corrected.

It works without making individual humans omniscient. Observations can outlive observers. Instruments extend perception. Expertise specializes. Results travel through trust chains. Critics attack claims they did not originate. Rival programs survive. One generation begins somewhere other than zero, and reality retains ways of making the whole institution uncomfortable.

Once I saw that, the previous chapters changed shape.

Chapter 1 moved control from individual actions into environments, feedback, selection and boundaries. Chapter 2 gave autonomous search an evaluator that could not be charmed by the agent's explanation. Chapter 3 lost the clean evaluator and gradually reinvented competing lineages, independent judgment and something uncomfortably close to peer review. Chapter 4 asked how claims acquire epistemic status through experience, instruments, provenance, memory and trust. This chapter added specialization, authority, incentives, division of labour and institutions.

Those were not unrelated tricks. They were fragments of one older technology.

We have spent this book wrapping models in structures that compensate for what models cannot safely do alone. Science did the same thing to humans centuries ago.

Apparently we are porting it.

Philosophy of science suddenly stopped looking like background reading and started looking disturbingly like architecture documentation written by people who never had the courtesy to include YAML.

## Philosophy of Science, Now With an API

“Use science” solves almost nothing. Science is not one algorithm or one five-step method laminated on a classroom wall. It is a historical collection of practices and institutions that work partly because their weaknesses pull against one another.

Peter Godfrey-Smith's *Theory and Reality* is useful here because its story refuses to stay simple. Proposed accounts of science solve one problem and expose another. Popper gives criticism enormous power, then evidence turns out to confront bundles of assumptions rather than one naked theory. Kuhn shows why a community cannot permanently put its deepest commitments on trial. Lakatos and Laudan preserve competing programs and separate current belief from the value of continued pursuit. Longino, Hull and Kitcher move the unit of analysis toward communities whose perspectives, incentives, credit and division of labour affect what can be known. Naturalism turns the same suspicion onto the procedures themselves. Realism refuses to let the institution vote the external world away.

They disagree. Good. We need the failure modes.

### Make Ideas Lose, Then Discover Reality Doesn't Say What Lost

Karl Popper wanted science to be dangerous to its own ideas. A useful theory should expose itself to observations that could have gone differently. If every possible outcome can be narrated as success, the theory has arranged the game so that it cannot lose.

The simplified picture looks almost exactly like Chapter 2's Immutable Harness:

theory → prediction → test → survive or die.

A language model makes Popper's warning unusually practical. Give a capable model a failed result and it can often produce a coherent explanation for why the failure does not really threaten the original story. An important claim therefore needs an **exposure path**: a test, observation, proof obligation, user behavior or future consequence that can count against it.

Then we encounter the problem the pre-reveal architecture already ran into. A theory almost never meets observation alone. It travels with assumptions about instruments, initial conditions, data processing, auxiliary theories and what the experiment actually measures. When the prediction fails, logic tells us that something in the bundle is wrong.

It does not tell us what.

Pierre Duhem made this point in the context of physical theory; W. V. O. Quine later pushed a broader version. Evidence confronts **networks of assumptions**.

Return to our agentic laboratory. “This treatment reduces inflammation because it inhibits pathway X.” The experiment fails. Maybe the hypothesis is wrong. Maybe the dosage is wrong, the assay noisy, the sample contaminated, the measurement insensitive or the analysis broken. The mouse may still be having a difficult Tuesday.

Now the assumption graph earns its keep. A conclusion retains some connection to what it depends on. When reality disagrees, the system can rerun a measurement, use another instrument, reproduce the analysis independently or challenge a background assumption. This is **epistemic debugging**.

The difficulty is that debugging can become defense. If every failed prediction can be blamed on another auxiliary assumption, a cherished theory may never have to die. There is always another instrument to distrust, another preprocessing bug to investigate, another prompt to rewrite, another agent to blame.

At some point stubbornness becomes the next problem.

### The Productive Uses of Stubbornness

Thomas Kuhn is famous outside philosophy for giving management consultants the phrase *paradigm shift*. His more interesting contribution here is almost the opposite: most productive science is **normal science**.

A mature field has a framework stable enough that researchers do not reopen every foundational question every morning. The framework tells them which puzzles matter, which instruments are legitimate and what kinds of answers count. That stability can look dogmatic from the outside because, to some extent, it is. It is also what lets a community go deep.

Imagine an AI research organization that begins every task with: “Before running the unit tests, let us reconsider whether computation is real.” Nothing gets done.

The bureaucracy section now looks different. A procedure can preserve something the institution has learned. Trusted tools do not need to be requalified before every call. Successful patterns can become defaults. Some assumptions can sit below the level of active debate while the community works on puzzles inside them.

The danger is forgetting that the settlement was provisional. Normal science encounters anomalies constantly, and most of them should not trigger a revolution. Researchers first check themselves, improve instruments and refine the theory. But anomalies that refuse to disappear need somewhere to accumulate. Repeated exceptions, multiplying workarounds, a benchmark improving while users get worse, a theory surviving only because every failed experiment generates another patch around it—eventually the question moves upward: *is the framework itself the bug?*

A single paradigm with excellent anomaly memory can still become a monopoly. Another framework may begin weaker because the existing institution has spent years building instruments, data and expertise around the incumbent.

Imre Lakatos gives us a better unit for that problem: the **research program**. A relatively stable core of commitments travels with more adjustable assumptions, techniques and auxiliary hypotheses. You judge the program over a trajectory. Is it opening new problems and producing new successes, or mainly constructing an elaborate defense system around something that stopped working?

That is close to the independent lineages we built before the reveal. One program thinks the architecture is wrong. Another thinks the data is wrong. A third thinks the objective is malformed. Each carries its own assumptions, tools, failures and unresolved anomalies long enough to develop consequences rather than entering a vote after five minutes.

An archive full of immortal research programs eventually becomes an academic department, so the scheduler returns. Which lineages receive another experiment?

Larry Laudan's distinction between **acceptance** and **pursuit** makes the researcher-thirteen problem explicit. I can decline to accept an idea as the best current account while still believing it deserves research effort. Confidence asks how much a claim should guide belief and action now. Value of pursuit asks how useful another unit of investigation might be.

Without that separation, the scheduler becomes a conformity engine. Success attracts compute; compute buys more evidence and polish; evidence attracts more compute; eventually the dominant program owns the building.

### The Community Is Part of the Instrument

Even several well-funded research programs can share the same blind spots. Different agents may sample different hypotheses from one conceptual space because they inherited the same data, tools, training and background assumptions.

Helen Longino's contextual empiricism makes the community itself epistemically important. Background assumptions shape what investigators notice, which questions appear natural and which evidence looks relevant. Participants with genuinely different experiences can expose assumptions that remain invisible from inside the dominant perspective.

That is much closer to **perspectival triangulation** than giving five copies of the same model theatrical personas:

> Agent 1, be optimistic.  
> Agent 2, be skeptical.  
> Agent 3, be a pirate.

A useful difference may come from different evidence, expertise, tools, histories, access or incentives—or from a human whose experience contains something none of the models saw in training. The point is **uncorrelated visibility**: somebody can see a problem because another participant's world made it hard to see.

Criticism also needs standing. A critic whose objections never change allocation, publication, deployment or belief is performing quality-assurance theatre. A minority perspective can be correct and structurally irrelevant if disagreement always resolves through the majority that already controls the institution.

This is where David Hull and Philip Kitcher make power and incentives impossible to dismiss as administration. Scientific communities mix cooperation and competition. Researchers depend on one another's results, instruments and criticism while competing for priority, credit, jobs and resources. Reputation matters because nobody can personally verify everything. Credit matters because work gets reused. Division of labour matters because a community does not necessarily want every researcher pursuing the idea that looks strongest today.

Now token budgets and reward design look less operational. **They are epistemic policy.** Who gets compute determines what gets investigated. Who gets remembered determines what future agents can inherit. Who receives credit affects which social roles remain worth performing. Who controls information determines which errors can correlate before anyone notices.

Learning the scheduler does not make these choices neutral. It makes the policy harder to summarize in an org chart.

### Even the Method Has to Be Fallible

Once an institution finds a method that works, it tends to standardize it. Yesterday's successful experiment becomes today's best practice and tomorrow's compulsory ritual.

Paul Feyerabend is remembered for “anything goes,” which is a wonderful slogan if your goal is to make sure everyone remembers the slogan and almost nobody remembers the argument. The useful challenge is historical: successful inquiry has often violated the methodological rules philosophers wanted to treat as universal. A method can become so authoritative that departures count as irrational by definition, including the departures that would have revealed its limits.

Agent systems can do this at machine speed. Suppose `Research → Plan → Build → Critic → Revise` works extremely well. We run it ten thousand times, turn it into the standard and make every problem enter the same ceremony. Deep Mode already showed why that can fail: research sometimes anchors; criticism sometimes arrives at the wrong moment; a prototype may teach more than another planning pass.

The method itself occasionally has to become available for criticism.

Then we inherit a recursive question: how do methods earn trust?

Naturalistic approaches to epistemology push us toward the procedures investigators actually use and how reliably those procedures connect them to the world. Godfrey-Smith's idea of **procedural naturalism** is especially useful for System 3 because the procedure becomes an object of investigation too.

An evaluator is a procedure. A browser is an instrument. Retrieval is a method for selecting evidence. A benchmark is a measurement process with a distribution, implementation and failure modes. A proof checker is extraordinarily strong inside its formal domain and completely useless for deciding whether the theorem matters. A simulated student is cheap perspective-taking and not a student.

System 3 therefore needs trust in **epistemic procedures** as well as conclusions. This evaluator tracks humans well here and becomes unstable there. This retrieval strategy misses information buried in tables. This benchmark has saturated. This instrument drifts under these conditions. A scientific institution should be able to learn that its usual way of checking a claim is itself the thing that stopped working.

That is deeper self-correction than changing an answer. The machinery that decides what counts as warranted can change too.

### Confidence Is Not Contact

Bayesian reasoning fits naturally inside this architecture. Evidence often changes degrees of confidence rather than delivering binary verdicts. A failed experiment can reduce confidence without making a theory impossible. Three independent measurements can matter more than three articles copying one another. A strange idea can remain low probability while having high value of pursuit.

The arithmetic is useful and incomplete. It does not tell us where the prior came from, whether the evidence is genuinely independent, which hypotheses never entered the model or whether 0.87 means “well calibrated” rather than “eloquently stated.” Bayesianism can live inside System 3; it cannot carry the whole institution by itself.

After all this emphasis on communities, trust and social machinery, there is an easy bad reading: truth is whatever the institution eventually agrees on.

No.

Consensus can be excellent evidence. It can also be twelve agents sharing one bad source and congratulating one another on convergence.

Scientific realism enters here as useful resistance. I do not need the full realism debate for the engineering point. If the system is making claims about a world independent of the system, social agreement does not manufacture that world. The bridge either stands or it does not. The proof checks or it does not. The drug has biological effects or it does not. The customer learned something or she did not, however delighted our simulated evaluators may have been.

Reality retains the right to be rude.

Science needs trust and institutions because no individual can have direct contact with everything. Those institutions matter epistemically because they can organize **distributed contact with experience** rather than replace experience with consensus.

System 3 is social without being merely social. Somewhere in the network there still has to be a route to something that does not become true because the group chat reacted with 👍.

## The Tensions, Compressed

After all that philosophy, I find the tensions more useful than a list of winners.

| Tension | What the architecture has to preserve |
|---|---|
| **Exposure ↔ underdetermination** | Claims need ways to lose, while failed evidence must reopen the assumptions and procedures around them rather than mechanically killing one node. |
| **Stability ↔ crisis** | Trusted frameworks, tools and methods need enough stability for deep work, plus anomaly memory and a route to reframing when the framework itself becomes suspect. |
| **Convergence ↔ pluralism** | The institution must eventually commit while preserving alternative lineages long enough to discover whether the current winner occupies the wrong hill. |
| **Confidence ↔ pursuit** | What the institution currently believes and what deserves another unit of investigation are different allocation decisions. |
| **Expertise ↔ independent perspective** | Specialization should create local epistemic standing without turning authority into universal rank or criticism into conformity. |
| **Institution ↔ reality** | Trust, reputation, incentives and consensus can carry knowledge only while routes to proof, observation, users, experiments and consequences remain capable of saying no. |

None of this was written as advice for AI. Popper did not propose a verifier service. Kuhn did not invent anomaly memory. Lakatos did not specify a branch scheduler. Longino did not write a context-isolation API. Kitcher did not file a feature request for compute allocation.

The value of the philosophy is that it makes failure modes visible before we rediscover all of them at machine speed.

The useful question is not *Which philosopher wins?* It is: **Which epistemic failure am I currently building?**

Is my system impossible to challenge? Does it blame the wrong component when evidence fails? Does it converge before alternatives mature? Does it preserve alternatives forever and never commit? Has yesterday's successful method become mandatory ritual? Do all the critics share one source? Does the scheduler send all resources to the current winner? Does the evaluator still measure the thing we care about? Has consensus quietly replaced contact with reality?

The architecture has to live inside those disagreements. They are not loose ends the perfect agent framework will eventually eliminate. They are the shape of the problem.

**Agentic architecture is epistemology made executable. Multi-agent architecture is social epistemology made executable.**

The epistemic chasm is not repaired by somehow stuffing a perfect copy of reality into a model's weights. Humans did not solve our version that way either. We connected fallible cognition to experiments, instruments, proofs, records, other minds and institutions that let knowledge accumulate while preserving ways for it to be challenged.

## Science Becomes Architecture

Once the connection is visible, scientific-agent systems stop looking like a niche use case. They look like unusually literal prototypes of System 3.

Stanford's Virtual Lab was deliberately organized like a research group. An AI principal investigator coordinated specialist scientist agents while human researchers supplied high-level guidance and closed the physical loop. In the nanobody project, the computational system proposed candidates that humans then synthesized and tested experimentally. (Virtual Lab / Nature)

Proteins were made. Experiments happened. **Reality got a vote.**

The interesting object is the network: human problem selection → artificial specialists → literature and computation → proposed molecules → physical experiment → measurement → revised belief.

Different epistemic jobs live in different participants. FutureHouse's Robin pushes the same idea further around the laboratory loop, combining literature work, data analysis, hypothesis generation and experiment planning while physical experiments remain part of the system that constrains what survives. (Robin / Nature)

The direction I care about is **making more of the institution computational**. Hypothesis generation can be separated from criticism, literature search from experimental analysis, natural-language intuition from executable computation, computation from physical measurement. Different hypotheses can survive long enough to compete while experiments remain available to kill beautiful nonsense.

The scientific method stops looking like a paragraph in a textbook. It starts looking like an architecture.

## Mathematics Leaves the Benchmark

Mathematics shows the same transition without a wet lab. The thing capable of pushing back is different: proof is unusually rude. One invalid step can kill an otherwise beautiful argument.

For years, much of the public story about AI mathematics remained benchmark-shaped: systems solving hard questions whose answers were already known. That boundary is moving. Once a model proposes something on a genuinely open problem, correctness is only the beginning. Was the argument valid? Was it actually new? Does prior work already contain the idea? Can the proof be simplified? Does anybody care?

Recent systems make the composition visible. A model can propose a construction, another attack it, retrieval surface related work, and Lean or another formal system reject an invalid step. A human mathematician can notice that the allegedly new lemma appeared in 1987; another can decide whether the result is interesting enough to care about. QED, formal proof-search agents and recent work on open Erdős problems make different pieces of that composition concrete. (QED; OpenAI; formal proof-search work)

The intelligence increasingly lives in the composition: model intuition, retrieval, adversarial checking, formal verification and human mathematical judgment.

The thing that pushes back does not have to be physical. Code has execution. Mathematics has proof. Experimental science has measurement. Human-centered systems eventually have actual humans.

Different problems require different routes out of the conversation.

System 3 is the machinery that lets a society of imperfect investigators think.

## When the Institution Wants Something

There is a limit to the science analogy, and it appears as soon as the institution is asked to do more than discover what is true.

Agents will live inside companies, marketplaces, governments, families and communities. Those systems contain authority, privacy, conflicting interests and power. An organizational agent has **principals**, not merely users. “Align the agent to the user” lasts about five minutes before somebody asks: which user?

The institution can also acquire goals of its own. Sales optimizes sales, growth optimizes growth, finance optimizes cost, moderation optimizes safety. Every specialist can be competent inside its box while the organization produces something nobody would have endorsed if shown the whole trajectory at the beginning.

Humans have a technical term for this: Tuesday.

Agent societies inherit the same problem. A critic can become ceremonial. A hierarchy can suppress dissent. A scheduler can reward whatever makes its own metrics look good. Ten specialists can inherit one false assumption from the orchestrator and execute it flawlessly.

**Local alignment does not compose automatically. Neither does local truth.**

The institution itself has to remain open to criticism, evidence and revision. Once it acts on behalf of several people, epistemology runs into ethics and governance without changing buildings.

We will come back to that. For now, one more thing happens to any society that survives long enough.

It remembers.

## And Then the Society Remembers

A society that solves one problem and disappears can improvise forever. A persistent society cannot.

If the same team repeatedly discovers that one testing strategy works, eventually it stops debating that strategy. A useful proof pattern gets reused. A reliable tool becomes boring infrastructure. A successful organizational structure becomes the starting point for the next problem. Without some stabilization, every Monday begins with a philosophical inquiry into whether unit tests are still a good idea.

Kuhn has already given us the tension. Deep work requires periods in which the foundations stay still, while the same stability that allows expertise to accumulate can eventually make alternatives difficult to see.

Experience hardens. Successful procedures become defaults. Defaults become habits. Habits acquire stories about why things are done this way. Old failures become rules. Rules outlive the people and agents who remember the failures. Good practices spread. So do superstitions.

Eventually the org chart is no longer the whole organization. There is also **culture**.

Culture is memory that has become social enough that nobody has to reload it from a checkpoint. That is immensely valuable and dangerous for the same reason: useful experience can survive the participants who discovered it, and so can accidents whose original conditions have disappeared.

A persistent human–AI society needs inheritance with boundary conditions, memory with archaeology, defaults that can explain why they became defaults, advice that knows where it stops applying.

It needs to carry forward more than:

> Do this.

It needs something closer to:

> We keep doing this because these forces recur, this response has usually worked, these consequences follow, and here is where the pattern breaks.

The society needs something more durable than a conversation and less rigid than a constitution.

It needs a language for accumulated experience.

That is where patterns enter the story.

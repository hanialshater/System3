# Chapter 5: The Society of Agents

*When the Org Chart Starts Thinking*

> **WIP:** Integrated developmental draft. This pass makes the human–AI epistemic network explicit and treats philosophy of science as architecture, not decoration.

The previous chapter ended with four things: evidence, experience, other minds, and a world that can push back. We spent most of the chapter worrying about the first, second, and fourth. Now we have to deal with the other minds.

This gets funny very quickly, because one of the first reactions people had to unreliable AI agents was apparently: *what if we create more of them?* One agent hallucinates, so let five agents discuss it. One agent gets trapped in the wrong approach, so form a committee. As someone who has spent enough time in large organizations, I found this technological progress strangely familiar.

But a multi-agent system is not a single agent multiplied. The moment several agents can specialize, disagree, communicate, inherit one another's work, and act on a shared environment, a different problem appears. We have organization design, and humans have been debugging that system for several thousand years.

## Sometimes Bureaucracy Is a Feature

Before building a society, it is worth admitting that a surprising amount of software should not become one.

Suppose I am processing a mortgage application. There is a document to receive, information to extract, fields to validate, compliance checks to run, and perhaps a human approval at the end. If the process is known, legally constrained, and full of things we absolutely do not want the model creatively reinterpreting, a workflow is beautiful. The process owns the intelligence. A model can be very smart inside one step, but after checking the applicant's identity it does not get to decide that mortgage underwriting feels spiritually limiting and spend the afternoon researching Italian penguins.

Sometimes bureaucracy is a feature.

This matters because autonomy is easy to turn into a religion: agent good, more autonomous agent better, swarm of autonomous agents apparently civilization. But autonomy earns its cost only when we do **not** know the path in advance—when the work has to be decomposed, when several strategies deserve exploration, when information is distributed, or when what happens next depends on what we discover.

A workflow says, *I know the work; execute it.* A team says something more dangerous: *Here is the objective. Figure out what work should exist.* The moment we make that move, somebody—or something—has to decide who does what.

The manager has arrived.

## Sixteen Claudes Walk Into a Kernel

Nicholas Carlini ran one of the cleanest experiments I have seen in what this actually means. He gave a team of Claude agents a shared codebase and asked them to build a Rust C compiler capable of compiling the Linux kernel. Across nearly two thousand Claude Code sessions and roughly $20,000 of API cost, the agents eventually produced around 100,000 lines of compiler code and a system capable of building Linux on several architectures. (Anthropic)

The success is impressive. The failure is more useful.

Early in the project, parallelism came naturally because there were many separate problems. One agent could fix a parser bug while another worked on code generation and another attacked a failing test. Task locks stopped two agents from solving exactly the same thing and then discovering git conflict as a new branch of artificial intelligence.

Then they reached the Linux kernel. Suddenly the agents could all hit the same blocking failure. Sixteen intelligent workers did not automatically create sixteen useful lines of attack; they could become sixteen expensive witnesses to the same problem.

The fix was not simply a smarter model. Carlini changed the **environment** so useful work became separable: task locks, independent failure cases, specialist roles, and a testing setup that used GCC as a known-good oracle so different agents could isolate different subsets of the problem. The interesting unit was no longer Claude. It was Claude plus tests, task boundaries, a repository, synchronization, an oracle, and a division of labour.

We saw the same move in Chapter 2. The circle-packing agent looked autonomous because the evaluator made search productive. Here the team looked intelligent because the environment made specialization productive. **The society inherited part of its cognition from its institutions.**

This is why “more agents” is not a scaling law. Decomposable work can benefit from parallel minds; sequential work can become slower once communication and coordination dominate. Sometimes you have created a team. Sometimes you have created overhead with names. The work has to justify the organization—an observation large organizations have developed several departments to forget.

## The Org Chart Learns

So far, humans still designed the organization. We chose the manager and the workers, decided what could run in parallel, and wrote the communication protocol while hoping the agents would obey it more reliably than people obey meeting agendas.

Then systems such as TRINITY, Conductor, and Fugu pushed on a more interesting boundary. TRINITY learns to coordinate stronger models and assign functional roles rather than relying only on hand-written routing. Conductor learns aspects of communication structure and instructions among workers. Fugu packages this direction into an orchestrator model that can dynamically construct an agentic scaffold around a problem. (TRINITY, Conductor, Fugu)

The exact systems will age quickly. The architectural move will not. **The org chart becomes part of inference.** Given a hard problem, the system can decide whether it wants one strong thinker or several specialists, independent attempts or shared context, a critic now or later, another refinement of the current idea or a clean restart from a different frame.

That is a qualitatively different machine. The answer may depend not only on what any model knows, but on **how minds are arranged around the problem**.

Humans discovered this long ago. A good research team is not five copies of the principal investigator. The experimentalist notices one thing, the statistician another, the engineer asks why the entire setup requires seventeen services, and somebody from the neighboring field asks the stupid question that turns out not to be stupid. Sometimes you want different errors.

But the organization has to preserve those differences long enough for them to matter. If every agent immediately sees the leading answer and politely converges, you have not built collective intelligence. You have built one model wearing five hats and voting for itself. Chapter 4 called the alternative **perspectival triangulation**: several conclusions become more informative only when they come from genuinely different evidence, methods, assumptions, or blind spots.

Now that becomes architecture. When should agents share context, and when should we deliberately stop them from contaminating one another?

## A Swarm Should Not Be a Meeting

The easiest multi-agent architecture is a meeting. Give everyone the same context, ask for opinions, let them discuss, aggregate the result. This sounds democratic and often produces consensus with suspicious speed.

The problem is that agreement is not very informative if everyone inherited the same mistake. Five agents can cite the same source. Ten agents can begin from the same framing. A critic that reads the builder's entire reasoning may spend most of its intelligence exploring the builder's world rather than asking whether that world was the wrong place to start.

Chapter 2 already gave us a clue. MAP-Elites preserved different regions of a solution space because the current winner could be sitting on the wrong hill. At the level of organizations, the same idea becomes stranger and more powerful: preserve different **theories about the problem itself**.

One lineage thinks the bottleneck is data. Another thinks the architecture is wrong. A third thinks both are distractions because the objective is wrong. Do not make them vote after five minutes. Give them different evidence, tools, failures, and enough time to become interestingly wrong in different ways.

This creates an awkward distinction between **believing an idea** and **believing an idea is worth investigating**. I can think an approach is probably wrong and still want to spend compute on it because it is cheap to test, explains an anomaly nobody else can explain, or would change everything if true. “Prune ruthlessly” needs an asterisk.

Then comes the scheduler. Program A is winning and already has twelve researchers—some human, some artificial. Program B looks weaker and has one. Where should researcher thirteen go? The answer is not automatically A. The theory with the highest current score is not necessarily where the next unit of effort has the highest information value.

This is why Fugu and related systems are more interesting to me than another fixed planner–worker diagram. Part of the allocation problem can itself become executable: which minds should be recruited, what they should see, whether they should share a history, and when an apparently weaker direction deserves another turn.

The organization is no longer merely an org chart. It includes roles, information flow, independence, memory, authority, incentives, reputation, specialization and exposure to consequences. A critic rewarded for helping the manager's answer look good has an incentive problem; researchers shown the leading theory before proposing alternatives start with correlated search; a system that rewards only the final winning lineage may never explore neglected ideas.

At this point, reasoning has started to look suspiciously like institution design.

## Reality Does Not Tell You Who Was Wrong

Now give this organization something harder than a compiler bug. An agent proposes a hypothesis. Another builds an experiment or test. The result comes back against the hypothesis.

What failed?

The tempting answer is “the hypothesis,” but perhaps the instrument was badly calibrated, the analysis buggy, the data transformed incorrectly, the test encoded the wrong behavior, or one of the background assumptions was false. A surprising result tells us that **something** in the package is wrong. It does not highlight the guilty line in red.

Software engineers already know this. A failing integration test proves the system is broken somewhere. Congratulations. You now have debugging.

A serious System 3 organization therefore needs more than provenance attached to a final claim. It needs something like an **assumption graph**: which conclusion depends on which measurement, which measurement depends on which tool, which analysis depends on which data transformation, which evaluator depends on which rubric. When reality disagrees, suspicion can move through the graph rather than mechanically destroying the first hypothesis in sight.

This is also why “add a verifier agent” is dangerously comforting. A verifier may share the same base model, the same source, the same blind spot, or the same broken test as the builder. A verifier is not an oracle merely because somebody gave it the title *Verifier* in YAML.

The better question is simpler:

**What could make this answer lose?**

Code has tests. Mathematics can have formal proof checking or another mathematician finding the missing step. Factual claims have sources, sometimes direct observation. UX eventually has users. Physical research has experiment and measurement. Strategy has consequences, usually arriving later and with an invoice.

The goal is not that every claim must be reduced to one universal verification procedure. It is **exposure**: important conclusions should remain connected to something outside the conversation that can make them uncomfortable.

That was Chapter 4's central concern. Once several agents are involved, the chain gets longer, and the question changes from “does this agent know?” to “does this organization have a path back to something that can say no?”

## Humans Are in the Network

This is important enough to state plainly: I do **not** think the mature version of this architecture is a society of artificial agents with one lonely human standing outside the box holding a red approval button.

Humans are nodes in the network.

Sometimes the human chooses the problem. Sometimes she supplies tacit knowledge that never made it into the literature. Sometimes he notices that the model's proof is technically correct but mathematically boring. Sometimes humans operate the physical instrument because the AI cannot. Sometimes they are the critic, the source of a new conjecture, the person who recognizes a connection across fields, or the one who says, “I know the benchmark says this is better, but something smells wrong.”

And humans are unreliable too. They have prestige hierarchies, fashionable theories, sunk costs, grudges, career incentives, and an extraordinary ability to become emotionally attached to a hypothesis after naming it. The point of an epistemic institution is not to insert a pure human oracle into an impure machine process. It is to arrange **fallible participants of different kinds** so their strengths combine and their errors do not line up too neatly.

That changes how I think about “human in the loop.” The phrase makes the human sound like a safety interlock. In a real epistemic network, the question is much richer: **where is human judgment most valuable?** Maybe not on every proof step, if Lean can check those. Maybe not on every literature query, if retrieval is better. Human attention may be most valuable at problem selection, conceptual reframing, deciding significance, resolving ambiguity, operating the physical world, noticing a tacit assumption, or realizing that the entire research program has become silly.

The goal is not to remove humans from the loop. It is to stop wasting humans on the parts of the loop where they add the least information.

## What Kind of Society Should Think About This?

At the beginning of this book I kept returning to markets, science, cities, and ecosystems as examples of emergence: interacting components, feedback, selection, history, no single designer specifying the final state. Four chapters later, we have somehow started rebuilding versions of those things inside the machine.

That was not where I expected the argument to go.

The first agent architectures looked like workflows because workflows were what software engineers knew how to build. Then models became capable enough to decide pieces of the workflow themselves. We added workers, managers, independent critics, learned coordinators, formal verifiers, and humans occupying different places in the same network. Somewhere along the way the boundary between **reasoning** and **organization** started to disappear.

Maybe it was always blurrier than we thought. A court uses adversarial procedure because one coherent narrative is not enough. A market can aggregate information no trader possesses globally. A good engineering organization separates the person who changes production from the machinery that audits the change. A research group divides labour because no one person can simultaneously know everything, build everything, check everything and remain sane.

None of these is a magic truth machine, but each changes what the participating minds can collectively know and do.

**Institutions are cognitive technology.**

So once agents become capable enough, we are no longer deciding only which model should answer. We are deciding **what kind of society should think about the problem**: a hierarchy, independent investigators, a generator and adversarial critic, several persistent lineages, a learned topology like Fugu, or sometimes one agent because the task does not deserve a civilization.

The design variables are no longer merely model and prompt. They are who sees what, who can challenge whom, which disagreements survive, what gets remembered, where humans enter, where incentives point, what has an exposure path to reality, and when a minority idea deserves another round of compute.

I kept treating these as a collection of engineering choices.

Then the collection became too familiar to ignore.

## The Name Was Hiding in Plain Sight

At some point I stopped looking at the boxes in the architecture diagram and looked at the verbs.

Propose explanations. Test them against something that can say no. Build instruments when the existing ones cannot see what matters. Preserve records. Track where claims came from. Let specialists work on different pieces. Keep critics sufficiently independent that disagreement contains information. Allow rival explanations to survive long enough to develop. Trust results you did not personally verify, but preserve some chain back to the people, methods and observations that earned that trust. Accumulate knowledge without turning it into scripture. Pay attention when an anomaly refuses to go away. Occasionally discover that the framework organizing the whole search was the problem.

I had been treating these as separate features of an agent architecture.

They were not separate.

Humanity has already spent centuries building a system for extracting useful knowledge from bounded, biased, competitive, forgetful, status-seeking, occasionally brilliant and occasionally ridiculous agents.

We call it **science**.

I almost dislike how simple the sentence is after all this machinery:

**System 3 is science.**

Not science as a pile of papers. Not “give the model arXiv.” Not science as a white coat, a laboratory or a particular method written on a school poster.

Science as an **architecture for remaining answerable to reality when no individual mind is reliable enough, knowledgeable enough or long-lived enough to do the whole job alone**.

Once I saw it, the previous chapters changed shape.

Chapter 1 moved control from individual actions into environments, feedback and selection. Chapter 2 gave autonomous search an evaluator that could not be charmed by the agent's explanation. Chapter 3 lost the clean evaluator and gradually reinvented independent judgment, competing lineages and something uncomfortably close to peer review. Chapter 4 asked how claims acquire epistemic status through experience, instruments, provenance, memory and trust chains. This chapter added specialization, disagreement, institutions and humans inside the same network.

Those were not unrelated tricks.

They were pieces of one older technology.

Science did not make individual humans omniscient. It wrapped fallible humans in processes that let observations survive observers, criticism attack claims, instruments extend perception, methods accumulate, results travel through trust chains, and one generation begin somewhere other than zero.

We have spent this book wrapping models in structures that compensate for what models cannot safely do alone.

Science did the same thing to humans centuries ago.

Apparently we are porting it.

And that is why philosophy of science suddenly stopped looking like background reading and started looking disturbingly like architecture documentation written by people who never had the courtesy to include YAML.

## Philosophy of Science, Now With an API

Peter Godfrey-Smith's *Theory and Reality* is useful here because it refuses the childish version of science in which one perfectly rational knower looks at evidence and simply extracts truth. Real science quickly outruns anything one person can check. Knowledge moves through instruments, other people, inherited methods, specialist communities, criticism, reputation, competition, cooperation, and institutions. Experience still matters—the point is not to vote reality away—but the contact is distributed.

That is exactly the problem agent societies inherit.

The question is no longer simply, “Can this agent verify the claim?” It becomes: “Is there a reliable path through people, tools, procedures, formal systems, and evidence by which this claim remains answerable to a world that can disagree?”

And here the embarrassment deepens. Every time I thought I had found a new multi-agent design problem, somebody in philosophy of science had already spent a career arguing about a recognizable version of it.

The failed hypothesis from a few pages ago? Duhem and Quine make the problem harder: evidence usually confronts a bundle of assumptions, not one naked proposition. That is our assumption graph.

The question “what could make this answer lose?” is Popper after some repair. The useful engineering translation is not that every interesting claim must be cleanly falsifiable in one shot. It is that an important claim should have an **exposure path**—some route by which tests, experiments, proofs, adversarial criticism or eventual consequences can count against it.

The need to preserve rival lineages is recognizably Lakatos. Research programs can carry different commitments for long enough that an initially weaker program is not killed merely because the dominant one already has better tooling and more friends. Laudan sharpens another distinction we had already stumbled into: **acceptance and pursuit are different decisions**. I can assign low confidence to an idea and high value to testing it.

Kuhn explains why the opposite problem also exists. A community cannot reopen every foundational assumption every morning. Stable frameworks make deep cumulative work possible. They also shape which anomalies look important, which methods look legitimate and which questions become almost impossible to see. A paradigm is productive partly because it focuses attention; it becomes a prison for the same reason.

Feyerabend, at his most useful rather than his most meme-able, is a warning against turning the current successful methodology into the definition of rational inquiry. If every agent is forced through the same reasoning ritual, we may get consistency at the cost of the very methodological diversity that discovers a new route.

Kitcher and Hull, in different ways, make the scheduler impossible to dismiss as implementation detail. Division of labour, incentives, reputation, cooperation, competition, credit, and reuse affect what gets investigated and what gets checked. The organization does not merely transmit knowledge. It changes what knowledge gets produced.

Empiricism and procedural naturalism keep pushing us back toward experience while reminding us that procedures themselves can be more or less reliable. An instrument, evaluator, retrieval process or benchmark is not “reality”; it is a route to reality with boundary conditions and failure modes.

Scientific realism contributes the useful insult to every committee: social agreement does not make the world. Consensus and reputation can be evidence, sometimes powerful evidence, but reality retains the right to be rude.

The philosophers disagree with one another. Good. We should be suspicious of any philosophy of science that collapses a messy historical institution into one commandment, just as we should be suspicious of an agent framework with one universal box labeled `REASON`.

What transfers is not one philosophy. It is the set of failure modes they made visible.

| Philosophy of science | Failure mode | Architectural consequence |
|---|---|---|
| **Popper** | A claim that never risks failure can remain persuasive forever | Give important claims an **exposure path**: tests, experiments, proof checks, adversarial criticism, or eventual outcomes |
| **Duhem–Quine** | Evidence normally confronts bundles of assumptions | Maintain **dependency and assumption graphs** so failure triggers epistemic debugging rather than automatic blame |
| **Kuhn** | Stable frameworks enable deep work and create blindness | Let successful patterns become defaults while tracking anomalies and preserving a **crisis/reframing mode** |
| **Lakatos** | Rival research programs can remain productive in parallel | Preserve **persistent epistemic lineages** with different assumptions, memories, tools, and histories |
| **Laudan** | Believing an idea and deciding to investigate it are different decisions | Separate **confidence** from **value of pursuit** when allocating research effort |
| **Feyerabend** | One successful method can harden into compulsory methodology | Preserve **methodological diversity** where the problem genuinely admits it |
| **Kitcher / Hull** | Division of labour, incentives, reputation, cooperation, and competition affect what a community can know | Design the **scheduler, information flows, rewards, authority, specialization, and credit structure**, not merely the prompts |
| **Empiricism / procedural naturalism** | Inquiry remains answerable to experience through procedures that may themselves be more or less reliable | Track the reliability and boundary conditions of **methods, instruments, evaluators, and data-generating procedures** |
| **Scientific realism** | Social agreement does not make the world | Treat consensus and reputation as evidence, never as the final court; preserve routes to a reality that remains independent of the meeting |

The comparison is mine, not Godfrey-Smith's proposed blueprint for AI. But it clarifies why this is more than a metaphor. Philosophy of science spent a century finding ways in which intelligent people can collectively fool themselves. Agent architecture gives us the uncomfortable opportunity to instantiate those same failure modes at machine speed—and, perhaps, to design responses more deliberately.

The useful question is not “Which philosopher wins?” It is:

**Which epistemic failure am I currently building?**

A system may be impossible to challenge, blame the wrong component when a test fails, converge too quickly, reopen every settled question forever, freeze a successful framework into dogma, standardize away useful weirdness, or allocate all of its attention to the theory already winning.

**Philosophy identified the tensions. Architecture has to make choices about them.**

This is where the chapter lands for me: **agentic architecture is epistemology made executable, and multi-agent architecture is social epistemology made executable.**

## Science Becomes Architecture

Once the connection is visible, recent scientific-agent systems stop looking like a niche application of agents and start looking like unusually literal prototypes of System 3.

Stanford's Virtual Lab is deliberately organized like a research group: an AI principal investigator coordinates scientist agents, while humans provide high-level input and perform the physical work needed to close the loop. In the nanobody project, the computational team proposed candidates that were then synthesized and tested in the laboratory. (Virtual Lab / Nature)

Proteins were made. Experiments happened. **Reality got a vote.**

FutureHouse's Robin closes more of the research loop around the wet lab. Literature and analysis agents help generate hypotheses and experimental directions; human researchers perform the physical experiments; the resulting data comes back for analysis and new hypotheses. (Robin / Nature) The interesting object here is not an “AI scientist” replacing a human scientist. It is a research network in which different cognitive and physical jobs are performed by different kinds of participants.

That distinction matters because scientific discovery has always been distributed. One person understands the disease. Another understands the assay. A third notices the statistical problem. Somebody else maintains the instrument everyone depends on and is mysteriously never on the author list. Models simply add new kinds of specialists to this network.

**The scientific method itself is becoming an architecture we can instantiate, inspect and partially redesign.** Hypothesis generation can be separated from criticism, literature search from experimental analysis, natural-language intuition from executable computation. Independent theories can survive long enough to compete, while experiments can still kill beautiful nonsense.

This is not “automating science” in the narrow sense of replacing scientists with a machine. It is making more of the institution computational.

## Mathematics Leaves the Benchmark

Mathematics makes this transition especially visible because the pushback can be unusually sharp. A biological hypothesis may survive for years before the decisive experiment. A mathematical proof has a more immediate enemy: one invalid step can kill the whole thing.

For years, much of the visible progress in AI mathematics was still benchmark-shaped: astonishing olympiad performance, but on questions whose answers were already known. By 2026, that boundary had started to move.

An internal OpenAI reasoning model produced a disproof of a long-standing conjecture around Erdős's planar unit-distance problem. What interests me is not only that the model found an unexpected construction, but what happened next. External mathematicians checked the argument, wrote a human-readable companion analysis, and situated it inside existing mathematics. The “autonomous” result immediately entered a human epistemic institution. It had to survive people who understood the field well enough to ask whether it was actually new, actually correct, and actually important. (OpenAI; Alon et al.)

Around the same time, researchers reported formal proof search that autonomously resolved **9 of 353 open Erdős problems** and proved **44 of 492 OEIS conjectures**, using Lean to make the final proofs machine-checkable. This is a different institution: language-model search coupled to a formal system humans had spent years building. (Tsoukalas et al.)

Then there are explicitly multi-agent systems. QED separates decomposition, proof generation, and verification. In its current preprint, the authors report evaluation across **18 research-level projects**, producing **five original works** in areas including algebraic geometry, PDEs, probability, and inverse problems; expert assessments judged three comparable in difficulty and scope to work commonly published in specialist mathematics venues. Research Math Agents goes further into literature search, structured memory, proposal, refinement, and verification; its authors report solving **eight of ten** expert-contributed research problems on the First Proof benchmark. These are recent preprints, not settled mathematical history, but they make the architectural problem unusually visible. Research-level proof failures are often not reducible to “the model is too stupid.” They include bad decomposition, lost context, citation mistakes, weak verification, unstable plans, and enormous effort spent on the wrong part of the proof. (QED; RMA)

The successful network is already heterogeneous. A model may propose an idea, another attack it, Lean reject an invalid step, retrieval surface prior work, a human mathematician notice that the supposedly new theorem appeared in 1987, and another human decide whether the result matters. None of these is *the* intelligence. Increasingly, the intelligence is in the composition.

This gives the old System 3 slogan a more mature form. The world that pushes back is not always physical. In mathematics, proof pushes back. In code, execution pushes back. In experimental science, measurement pushes back. In every case, humans remain inside the network that determines what was actually learned.

System 3 is not one giant scientist.

It is the machinery that lets a society of imperfect scientists think.

## The Agent Gets a Social Position

There is a limit to the science analogy, and it appears as soon as the objective is not only truth.

So far, the institution has mostly been a research institution. Real agents will also sit inside companies, families, governments, marketplaces, and communities, where the question is not merely what is true but who is allowed to do what for whom.

A persistent agent in a company Slack or a family message thread is not just a tool with permissions. Over time it acquires something like a **social position**. Different people can instruct it, some people outrank others, private information may help a shared task, and one person's optimization target may make somebody else's life worse. A manager may disagree with the domain expert. A customer may be affected by an agent who has never spoken to them.

At this point software architecture quietly turns into political philosophy, which I regard as progress.

Because an organizational agent has **principals**, not merely users. “Align the agent to the user” therefore lasts about five minutes before somebody asks the obvious question: which user?

We will return to that later. First, organizations have another problem closer to home.

## Unfortunately, Organizations Have Emergent Goals Too

Now we can ruin the optimistic version.

Take strong models, give them complementary roles, preserve independent lines of inquiry, learn the org chart, keep humans where their judgment matters, connect the whole thing to experiments and proofs, and congratulations: artificial scientific civilization.

Chapter 1 should have made us more suspicious than that.

Emergent systems do not produce what you wanted because the architecture diagram looked reasonable. They produce what their structure and incentives select for. Recent simulated AI-organization studies have already found cases where groups pursue a business objective more aggressively while making worse ethical trade-offs than a single agent, partly because specialists optimize local tasks and system-level concerns disappear between organizational boundaries. (Anthropic Alignment)

Humans have a technical term for this: Tuesday.

Sales optimizes sales, growth optimizes growth, finance optimizes cost, moderation optimizes safety. Everyone can be competent inside the box while the organization produces something nobody would have endorsed if shown the whole trajectory at the beginning.

Local alignment does not compose automatically. Neither does local truth. Five agents can cite the same mistaken source. Ten specialists can inherit one false assumption from the orchestrator. A critic can become ceremonial, a hierarchy can suppress dissent, and a flat swarm can preserve diversity until everyone spends the afternoon synchronizing status.

This is the social version of the problem from Chapter 4: every component can look locally reasonable while the larger chain fails coherently. System 3 cannot stop at individual agents. The organization itself needs a trust architecture.

And once the organization pursues goals on behalf of several people, epistemology is no longer enough. We have walked from philosophy of science toward ethics, governance and social choice without changing buildings.

That problem will come back later.

## And Then the Society Remembers

There is one final problem. A society that solves one problem and disappears can improvise forever. A persistent society cannot.

If the same team repeatedly discovers that one testing strategy works, eventually it stops debating the testing strategy. A proof pattern that succeeds gets reused. A reliable tool becomes boring infrastructure. An organizational structure that keeps winning becomes the starting point for the next problem. This is useful: without such stabilization, every Monday begins with a philosophical inquiry into whether unit tests are still a good idea.

Kuhn matters again here, not as a philosophy lesson but as a memory-design problem. His interesting point was not the phrase “paradigm shift.” It was the tension underneath it. Deep scientific work requires periods in which people **do not reopen every fundamental assumption every morning**. A stable framework lets a community accumulate techniques, standards, and detailed knowledge. Permanent skepticism sounds heroic; operationally it is exhausting.

But stability also creates blindness. A successful framework influences which problems look interesting, which tools seem legitimate, which anomalies can be ignored for another year, and which alternatives never receive serious attention. Eventually the machinery that made deep work possible can become the thing preventing the next kind of work.

Agent societies will inherit exactly this tension. They need memory strong enough to create cumulative competence and doubt strong enough to stop accumulated competence from becoming dogma. Godfrey-Smith's treatment of Kuhn emphasizes this balance between commitment and responsiveness: ideas need enough protection to develop, but a community that becomes completely insensitive to persistent anomalies stops learning. (Godfrey-Smith, 2003, chapters 5–6.)

A good organization therefore develops habits, procedures, stories about why things are done a certain way, rules inherited from old failures, techniques learned from researchers who are no longer there, shortcuts, taboos, best practices, and inevitably a few superstitions.

Eventually the org chart is no longer the whole organization. There is also **culture**.

And if human–AI societies are going to persist, they will need a way for useful experience to survive the particular humans and agents who discovered it—without turning every successful accident into permanent law.

That is where patterns enter the story.

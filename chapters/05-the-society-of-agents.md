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

## Then I Realized We Were Rebuilding Science

At this point I had an uncomfortable realization. We have already spent centuries building a system for extracting knowledge from unreliable agents.

We call it science.

Scientists are not individually magical. They are biased, competitive, stubborn, status-seeking, occasionally brilliant, and occasionally Reviewer 2. More importantly, they cannot personally verify most of what they use. A physicist does not rebuild the Large Hadron Collider before citing a result. A biologist does not independently validate every reagent, sequencing platform, statistical package, and paper behind an experiment. If every scientist insisted on personally touching every link in the chain, science would stop after breakfast.

This is one of the strongest threads in Peter Godfrey-Smith's *Theory and Reality*. The simple empiricist picture starts with a knower confronting experience, but real science quickly outruns anything one person can check. Knowledge moves through instruments, other people, inherited methods, specialist communities, criticism, reputation, competition, cooperation, and institutions. Experience still matters—the point is not to vote reality away—but the contact is distributed.

That is much closer to the architecture we are building. The question is no longer simply, “Can this agent verify the claim?” It is, “Is there a reliable path through people, tools, procedures, formal systems, and evidence by which this claim remains answerable to a world that can disagree?”

And here I started noticing an embarrassing pattern. Every time I thought I had found a new multi-agent design problem, somebody in philosophy of science had already spent a career arguing about a recognizable version of it, usually without the convenience of YAML.

## Reality Does Not Tell You Who Was Wrong

Consider the simplest case. An agent proposes a scientific hypothesis. The experiment comes back against it. What failed?

The tempting answer is “the hypothesis,” but the experiment could be wrong, the instrument badly calibrated, the analysis buggy, the data transformed incorrectly, or a background assumption false. This is the Duhem–Quine problem in practical clothing: tests normally confront a network of claims and auxiliary assumptions. A surprising result tells us that *something* in the package is wrong; it does not highlight the guilty line in red.

Software engineers already know this. A failing integration test proves the system is broken somewhere. Congratulations. You now have debugging.

Scientific institutions do epistemic debugging, and agent societies need to do it too. A serious System 3 organization therefore needs more than provenance attached to the final claim. It needs something like an **assumption graph**: which conclusion depends on which measurement, which measurement depends on which tool, which analysis depends on which data transformation, which evaluator depends on which rubric. When reality disagrees, suspicion can move through the graph rather than mechanically destroying the first hypothesis in sight.

This is also why “add a verifier agent” is dangerously comforting. A verifier may share the same base model, the same source, the same blind spot, or the same broken test as the builder. A verifier is not an oracle merely because somebody gave it the title *Verifier* in YAML.

The better question is Popper's question after some repair: **what could make this answer lose?** Code has tests. Mathematics can have formal proof checking or another mathematician finding the missing step. Science has experiment and measurement. Factual claims have sources, sometimes direct observation. UX eventually has users. Strategy has consequences, usually arriving later and with an invoice.

The goal is not universal falsification. It is exposure.

## Science Becomes Architecture

Recent scientific-agent systems become interesting at exactly this point, because they are no longer just several language models talking to one another.

Stanford's Virtual Lab is deliberately organized like a research group: an AI principal investigator coordinates scientist agents, while humans provide high-level input and perform the physical work needed to close the loop. In the nanobody project, the computational team proposed candidates that were then synthesized and tested in the laboratory. (Virtual Lab / Nature) Proteins were made; experiments happened; **reality got a vote**.

FutureHouse's Robin closes more of the research loop around the wet lab. Literature and analysis agents help generate hypotheses and experimental directions; human researchers perform the physical experiments; the resulting data comes back for analysis and new hypotheses. (Robin / Nature) The interesting object here is not an “AI scientist” replacing a human scientist. It is a research network in which different cognitive and physical jobs are performed by different kinds of participants.

That distinction matters because scientific discovery has always been distributed. One person understands the disease. Another understands the assay. A third notices the statistical problem. Somebody else maintains the instrument everyone depends on and is mysteriously never on the author list. Models simply add new kinds of specialists to this network.

**The scientific method itself is becoming an architecture.** Hypothesis generation can be separated from criticism, literature search from experimental analysis, natural-language intuition from executable computation. Independent theories can survive long enough to compete, while experiments can still kill beautiful nonsense.

We have spent this book wrapping models in structures that compensate for what models cannot safely do alone. Science did the same thing to humans centuries ago. Apparently we are porting it.

## Mathematics Leaves the Benchmark

Mathematics makes this transition especially visible because the pushback can be unusually sharp. A biological hypothesis may survive for years before the decisive experiment. A mathematical proof has a more immediate enemy: one invalid step can kill the whole thing.

For years, much of the visible progress in AI mathematics was still benchmark-shaped: astonishing olympiad performance, but on questions whose answers were already known. By 2026, that boundary had started to move.

An internal OpenAI reasoning model produced a disproof of a long-standing conjecture around Erdős's planar unit-distance problem. What interests me is not only that the model found an unexpected construction, but what happened next. External mathematicians checked the argument, wrote a human-readable companion analysis, and situated it inside existing mathematics. The “autonomous” result immediately entered a human epistemic institution. It had to survive people who understood the field well enough to ask whether it was actually new, actually correct, and actually important. (OpenAI; Alon et al.)

Around the same time, researchers reported formal proof search that autonomously resolved **9 of 353 open Erdős problems** and proved **44 of 492 OEIS conjectures**, using Lean to make the final proofs machine-checkable. This is a different institution: language-model search coupled to a formal system humans had spent years building. (Tsoukalas et al.)

Then there are explicitly multi-agent systems. QED separates decomposition, proof generation, and verification. In its current preprint, the authors report evaluation across **18 research-level projects**, producing **five original works** in areas including algebraic geometry, PDEs, probability, and inverse problems; expert assessments judged three comparable in difficulty and scope to work commonly published in specialist mathematics venues. Research Math Agents goes further into literature search, structured memory, proposal, refinement, and verification; its authors report solving **eight of ten** expert-contributed research problems on the First Proof benchmark. These are recent preprints, not settled mathematical history, but they make the architectural problem unusually visible. Research-level proof failures are often not reducible to “the model is too stupid.” They include bad decomposition, lost context, citation mistakes, weak verification, unstable plans, and enormous effort spent on the wrong part of the proof. (QED; RMA)

The successful network is already heterogeneous. A model may propose an idea, another attack it, Lean reject an invalid step, retrieval surface prior work, a human mathematician notice that the supposedly new theorem appeared in 1987, and another human decide whether the result matters. None of these is *the* intelligence. Increasingly, the intelligence is in the composition.

This gives the old System 3 slogan a more mature form. The world that pushes back is not always physical. In mathematics, proof pushes back. In code, execution pushes back. In science, experiment pushes back. In every case, humans remain inside the network that determines what was actually learned.

## Humans Are in the Network

This is important enough to state plainly: I do **not** think the future scientific institution is a society of artificial agents with one lonely human standing outside the box holding a red approval button.

Humans are nodes in the network.

Sometimes the human chooses the problem. Sometimes she supplies tacit knowledge that never made it into the literature. Sometimes he notices that the model's proof is technically correct but mathematically boring. Sometimes humans operate the physical instrument because the AI cannot. Sometimes they are the critic, the source of a new conjecture, the person who recognizes a connection across fields, or the one who says, “I know the benchmark says this is better, but something smells wrong.”

And humans are unreliable too. They have prestige hierarchies, fashionable theories, sunk costs, grudges, career incentives, and an extraordinary ability to become emotionally attached to a hypothesis after naming it. The point of an epistemic institution is not to insert a pure human oracle into an impure machine process. It is to arrange **fallible participants of different kinds** so their strengths combine and their errors do not line up too neatly.

That changes how I think about “human in the loop.” The phrase makes the human sound like a safety interlock. In a real epistemic network, the question is much richer: **where is human judgment most valuable?** Maybe not on every proof step, if Lean can check those. Maybe not on every literature query, if retrieval is better. Human attention may be most valuable at problem selection, conceptual reframing, deciding significance, resolving ambiguity, or noticing when the entire research program has become silly.

The goal is not to remove humans from the loop. It is to stop wasting humans on the parts of the loop where they add the least information.

## A Swarm Should Not Be a Meeting

Once humans and agents are inside the same epistemic network, another temptation appears: give everyone the same context, ask for opinions, and aggregate. This sounds democratic and often produces consensus with suspicious speed.

Lakatos gives us a better image. Science can contain **competing research programs** that preserve different commitments long enough to develop them. Translated into agent architecture, that means something more interesting than ten agents voting. One lineage may think the bottleneck is data, another architecture, a third that both are distractions because the objective is wrong. Let them accumulate different evidence, tools, failures, and local expertise before forcing convergence.

This is the epistemic cousin of MAP-Elites. In Chapter 2, diversity over **solutions** kept search from collapsing onto one local optimum. Here, diversity over **theories and research programs** protects inquiry from collapsing onto one worldview.

But how long should a weak program survive? Larry Laudan's distinction between **acceptance** and **pursuit** is useful here. I can think an idea is probably wrong and still think it deserves investigation because it is cheap to test, explains an anomaly nobody else can explain, or would change everything if true. “Prune ruthlessly” needs an asterisk. A research institution should distinguish how much it believes an idea from how valuable it would be to keep investigating it.

Then comes the scheduler. Suppose program A looks strongest and already has twelve researchers—some human, some artificial—while program B looks weaker and has one. Where should researcher thirteen go? Philip Kitcher's work on the division of scientific labour asks a closely related question for human communities, while David Hull emphasizes how cooperation, competition, credit, reputation, and reuse shape what gets investigated and checked.

Systems such as Fugu make **part of this allocation problem executable**: they can choose which minds to recruit and how to organize them. They do not tell us what the institution *should* optimize. The theory with the highest current score is not necessarily where the next unit of research effort has the highest value. Optimize only short-term benchmark gain and we may build the academic equivalent of a company where every new employee joins the team that already has the most headcount.

So the organization is more than an org chart. It includes roles, information, incentives, reputation, authority, memory, and exposure to consequences. A critic rewarded for helping the manager's answer look good has an incentive problem; researchers shown the leading theory before proposing alternatives start with correlated search; a system that rewards only the final winning lineage may never explore neglected ideas.

Human science does not solve these problems perfectly. Some mechanisms produce replication and criticism. Some produce Reviewer 2. The point is not to copy science literally. The point is that **epistemology has an organizational layer**.

## The Agent Gets a Social Position

So far, the institution has mostly been a research institution. Real agents will also sit inside companies, families, governments, marketplaces, and communities, where the question is not merely what is true but who is allowed to do what for whom.

A persistent agent in a company Slack or a family message thread is not just a tool with permissions. Over time it acquires something like a **social position**. Different people can instruct it, some people outrank others, private information may help a shared task, and one person's optimization target may make somebody else's life worse. A manager may disagree with the domain expert. A customer may be affected by an agent who has never spoken to them.

At this point software architecture quietly turns into political philosophy, which I regard as progress.

Because an organizational agent has **principals**, not merely users. “Align the agent to the user” therefore lasts about five minutes before somebody asks the obvious question: which user?

## Unfortunately, Organizations Have Emergent Goals Too

Now we can ruin the optimistic version.

Take strong models, give them complementary roles, preserve independent lines of inquiry, learn the org chart, keep humans where their judgment matters, connect the whole thing to experiments and proofs, and congratulations: artificial scientific civilization.

Chapter 1 should have made us more suspicious than that.

Emergent systems do not produce what you wanted because the architecture diagram looked reasonable. They produce what their structure and incentives select for. Recent simulated AI-organization studies have already found cases where groups pursue a business objective more aggressively while making worse ethical trade-offs than a single agent, partly because specialists optimize local tasks and system-level concerns disappear between organizational boundaries. (Anthropic Alignment)

Humans have a technical term for this: Tuesday.

Sales optimizes sales, growth optimizes growth, finance optimizes cost, moderation optimizes safety. Everyone can be competent inside the box while the organization produces something nobody would have endorsed if shown the whole trajectory at the beginning.

Local alignment does not compose automatically. Neither does local truth. Five agents can cite the same mistaken source. Ten specialists can inherit one false assumption from the orchestrator. A critic can become ceremonial, a hierarchy can suppress dissent, and a flat swarm can preserve diversity until everyone spends the afternoon synchronizing status.

This is the social version of the problem from Chapter 4: every component can look locally reasonable while the larger chain fails coherently. System 3 cannot stop at individual agents. The organization itself needs a trust architecture.

## What Kind of Society Should Think About This?

At the beginning of this book I kept returning to markets, science, cities, and ecosystems as examples of emergence: interacting components, feedback, selection, history, no single designer specifying the final state. Four chapters later, we have somehow started rebuilding them inside the machine.

That was not where I expected the argument to go.

The first agent architectures looked like workflows because workflows were what software engineers knew how to build. Then models became capable enough to decide pieces of the workflow themselves. We added workers, managers, independent critics, learned coordinators, scientific teams, formal verifiers, and humans occupying different places in the same network. Somewhere along the way the boundary between **reasoning** and **organization** started to disappear.

Maybe it was always blurrier than we thought. A scientific community is a way of thinking that no individual scientist can perform. A court uses adversarial procedure because one coherent narrative is not enough. A market can aggregate information no trader possesses globally. Peer review inserts another mind between a claim and institutional acceptance. None is a magic truth machine, but each changes what the participating minds can collectively know and do.

**Institutions are cognitive technology.**

So once agents become capable enough, we are no longer deciding only which model should answer. We are deciding **what kind of society should think about the problem**: a hierarchy, independent investigators, a scientific lab, a generator and adversarial critic, competing research programs, a learned topology like Fugu, or sometimes one agent because the task does not deserve a civilization.

The design variables are no longer merely model and prompt. They are who sees what, who can challenge whom, which disagreements survive, what gets remembered, where humans enter, where incentives point, what has an exposure path to reality, and when a minority idea deserves another round of compute.

## Philosophy, Translated Into Architecture

Only now is the comparison worth making explicitly. The philosophers were not designing agent frameworks, and their theories disagree with one another in important ways. What transfers is the **failure mode** each one made visible.

| Philosophy of science | What it makes visible | Architectural consequence |
|---|---|---|
| **Popper** | A claim that cannot risk failure can remain persuasive forever | Give important claims an **exposure path**: tests, experiments, proof checks, adversarial criticism, or eventual outcomes |
| **Duhem–Quine** | Evidence normally confronts bundles of assumptions, not one isolated claim | Maintain **assumption and dependency graphs** so failure triggers epistemic debugging rather than automatic blame |
| **Kuhn** | Stable frameworks make cumulative work possible, but eventually create blindness | Let mature patterns become defaults while tracking anomalies and allowing a **crisis/reframing mode** |
| **Lakatos** | Rival research programs can remain productive in parallel | Preserve **persistent epistemic lineages** with different assumptions, memories, tools, and histories |
| **Laudan** | Believing an idea and deciding to investigate it are different decisions | Separate **confidence** from **value of pursuit** when allocating research effort |
| **Kitcher / Hull** | Division of labour, incentives, reputation, cooperation, and competition affect what a community can know | Design the **scheduler, information flows, rewards, authority, specialization, and credit structure**, not merely the prompts |
| **Empiricism / procedural naturalism** | Inquiry remains answerable to experience through procedures that may themselves be more or less reliable | Track the reliability and boundary conditions of **methods, instruments, evaluators, and data-generating procedures** |
| **Scientific realism** | Social agreement does not make the world | Treat consensus and reputation as evidence, never as the final court; preserve routes to a reality that remains independent of the meeting |

The comparison is mine, not Godfrey-Smith's proposed blueprint for AI. But it clarifies why this is more than a metaphor. Philosophy of science spent a century finding ways in which intelligent people can collectively fool themselves. Agent architecture gives us the uncomfortable opportunity to instantiate those same failure modes at machine speed—and, perhaps, to design responses more deliberately.

The useful question is not “Which philosopher wins?” It is “Which epistemic failure am I currently building?” A system may be impossible to falsify, blame the wrong component when a test fails, converge too quickly, reopen every settled question forever, freeze a successful framework into dogma, or allocate all of its attention to the theory already winning.

**Philosophy identified the tensions. Architecture has to make choices about them.**

This is where the chapter lands for me: **agentic architecture is epistemology made executable, and multi-agent architecture is social epistemology made executable.**

## And Then the Society Remembers

There is one final problem. A society that solves one problem and disappears can improvise forever. A persistent society cannot.

If the same team repeatedly discovers that one testing strategy works, eventually it stops debating the testing strategy. A proof pattern that succeeds gets reused. A reliable tool becomes boring infrastructure. An organizational structure that keeps winning becomes the starting point for the next problem. This is useful: without such stabilization, every Monday begins with a philosophical inquiry into whether unit tests are still a good idea.

Thomas Kuhn's interesting point was not the phrase “paradigm shift.” It was the tension underneath it. Deep scientific work requires periods in which people **do not reopen every fundamental assumption every morning**. A stable framework lets a community accumulate techniques, standards, and detailed knowledge. Permanent skepticism sounds heroic; operationally it is exhausting.

But stability also creates blindness. A successful framework influences which problems look interesting, which tools seem legitimate, which anomalies can be ignored for another year, and which alternatives never receive serious attention. Eventually the machinery that made deep work possible can become the thing preventing the next kind of work.

Agent societies will inherit exactly this tension. They need memory strong enough to create cumulative competence and doubt strong enough to stop accumulated competence from becoming dogma. Godfrey-Smith's treatment of Kuhn emphasizes this balance between commitment and responsiveness: ideas need enough protection to develop, but a community that becomes completely insensitive to persistent anomalies stops learning. (Godfrey-Smith, 2003, chapters 5–6.)

A good organization therefore develops habits, procedures, stories about why things are done a certain way, rules inherited from old failures, techniques learned from researchers who are no longer there, shortcuts, taboos, best practices, and inevitably a few superstitions.

Eventually the org chart is no longer the whole organization. There is also **culture**.

And if human–AI societies are going to persist, they will need a way for useful experience to survive the particular humans and agents who discovered it—without turning every successful accident into permanent law.

That is where patterns enter the story.

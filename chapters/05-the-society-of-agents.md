# Chapter 5: The Society of Agents

*When the Org Chart Starts Thinking*

The previous chapter ended with four things: evidence, experience, other minds, and a world that can push back. We spent most of the chapter worrying about the first, second and fourth.

Now we have to deal with the other minds.

This gets funny very quickly, because one of the first reactions people had to unreliable AI agents was apparently: *what if we create more of them?*

One agent hallucinates, so let five agents discuss it. One agent gets trapped in the wrong approach, so form a committee. As someone who has spent enough time in large organizations, I found this technological progress strangely familiar.

But a multi-agent system is not a single agent multiplied. The moment several agents can specialize, disagree, communicate, inherit one another's work and act on a shared environment, a different problem appears.

We have organization design.

Humans have been debugging that system for several thousand years.

## Sometimes Bureaucracy Is a Feature

Before building a society, it is worth admitting that a surprising amount of software should not become one.

Suppose I am processing a mortgage application. There is a document to receive, information to extract, fields to validate, compliance checks to run, and perhaps a human approval at the end. If the process is known, legally constrained and full of things we absolutely do not want the model creatively reinterpreting, a workflow is beautiful.

The process owns the intelligence.

A model can be very smart inside one step, but after checking the applicant's identity it does not get to decide that mortgage underwriting feels spiritually limiting and spend the afternoon researching Italian penguins.

Sometimes bureaucracy is a feature.

This matters because autonomy is easy to turn into a religion: agent good, more autonomous agent better, swarm of autonomous agents apparently civilization.

But autonomy earns its cost only when we do **not** know the path in advance—when work has to be decomposed, several strategies deserve exploration, information is distributed, or what happens next depends on what we discover.

A workflow says, *I know the work; execute it.*

A team says something more dangerous:

*Here is the objective. Figure out what work should exist.*

The moment we make that move, somebody—or something—has to decide who does what.

The manager has arrived.

## Sixteen Claudes Walk Into a Kernel

Nicholas Carlini ran one of the cleanest experiments I have seen in what this actually means. He gave a team of Claude agents a shared codebase and asked them to build a Rust C compiler capable of compiling the Linux kernel. Across nearly two thousand Claude Code sessions and roughly $20,000 of API cost, the agents eventually produced around 100,000 lines of compiler code and a system capable of building Linux on several architectures.

The success is impressive.

The failure is more useful.

Early in the project, parallelism came naturally because there were many separate problems. One agent could fix a parser bug while another worked on code generation and another attacked a failing test. Task locks stopped two agents from solving exactly the same thing and then discovering git conflict as a new branch of artificial intelligence.

Then they reached the Linux kernel.

Suddenly the agents could all hit the same blocking failure.

Sixteen intelligent workers did not automatically create sixteen useful lines of attack. They could become sixteen expensive witnesses to the same problem.

The fix was not simply a smarter model. Carlini changed the **environment** so useful work became separable: task locks, independent failure cases, specialist roles, and a testing setup that used GCC as a known-good oracle so different agents could isolate different subsets of the problem.

The interesting unit was no longer Claude.

It was Claude plus tests, task boundaries, a repository, synchronization, an oracle and a division of labour.

We saw the same move in Chapter 2. The circle-packing agent looked autonomous because the evaluator made search productive. Here the team looked intelligent because the environment made specialization productive.

**The society inherited part of its cognition from its institutions.**

This is why “more agents” is not a scaling law. Decomposable work can benefit from parallel minds; sequential work can become slower once communication and coordination dominate. Sometimes you have created a team. Sometimes you have created overhead with names.

The work has to justify the organization—an observation large organizations have developed several departments to forget.

## The Org Chart Learns

So far, humans still designed the organization. We chose the manager and workers, decided what could run in parallel and wrote the communication protocol while hoping the agents would obey it more reliably than people obey meeting agendas.

Then systems such as TRINITY, Conductor and Fugu pushed on a more interesting boundary. They explore different ways for models to coordinate other models, assign roles, shape communication or construct an agentic scaffold dynamically rather than treating the org chart as fixed in advance.

The exact systems will age quickly.

The architectural move will not.

**The org chart becomes part of inference.**

Given a hard problem, the system can decide whether it wants one strong thinker or several specialists, independent attempts or shared context, a critic now or later, another refinement of the current idea or a clean restart from a different frame.

That is a qualitatively different machine. The answer may depend not only on what any model knows, but on **how minds are arranged around the problem**.

Humans discovered this long ago. A good research team is not five copies of the principal investigator. The experimentalist notices one thing, the statistician another, the engineer asks why the entire setup requires seventeen services, and somebody from the neighboring field asks the stupid question that turns out not to be stupid.

Sometimes you want different errors.

But the organization has to preserve those differences long enough for them to matter. If every agent immediately sees the leading answer and politely converges, you have not built collective intelligence.

You have built one model wearing five hats and voting for itself.

Chapter 4 called the alternative **perspectival triangulation**: several conclusions become more informative only when they come from genuinely different evidence, methods, assumptions or blind spots.

Now that becomes architecture.

When should agents share context, and when should we deliberately stop them from contaminating one another?

## Then I Realized We Were Rebuilding Science

At this point I had an uncomfortable realization.

We have already spent centuries building a system for extracting knowledge from unreliable agents.

We call it science.

Scientists are not individually magical. They are biased, competitive, stubborn, status-seeking, occasionally brilliant, and occasionally Reviewer 2. More importantly, they cannot personally verify most of what they use. A physicist does not rebuild the Large Hadron Collider before citing a result. A biologist does not independently validate every reagent, sequencing platform, statistical package and paper behind an experiment. If every scientist insisted on personally touching every link in the chain, science would stop after breakfast.

This is one of the strongest threads in Peter Godfrey-Smith's *Theory and Reality*. The simple empiricist picture begins with a knower confronting experience, but real science quickly outruns anything one person can check. Knowledge moves through instruments, other people, inherited methods, specialist communities, criticism, reputation, competition, cooperation and institutions. Experience still matters—the point is not to vote reality away—but the contact is distributed.

That is much closer to the architecture we are building.

The question is no longer simply:

> Can this agent verify the claim?

It becomes:

> Is there a reliable path through people, tools, procedures, formal systems and evidence by which this claim remains answerable to a world that can disagree?

And here I started noticing an embarrassing pattern. Every time I thought I had found a new multi-agent design problem, somebody in philosophy of science had already spent a career arguing about a recognizable version of it, usually without the convenience of YAML.

## Reality Does Not Tell You Who Was Wrong

Consider the simplest case. An agent proposes a scientific hypothesis. The experiment comes back against it.

What failed?

The tempting answer is “the hypothesis,” but the instrument could be badly calibrated, the analysis buggy, the data transformed incorrectly, or a background assumption false. This is the Duhem–Quine problem in practical clothing: tests normally confront a network of claims and auxiliary assumptions.

A surprising result tells us that **something** in the package is wrong.

It does not highlight the guilty line in red.

Software engineers already know this. A failing integration test proves the system is broken somewhere.

Congratulations.

You now have debugging.

Scientific institutions do epistemic debugging, and agent societies need to do it too. A serious System 3 organization therefore needs more than provenance attached to a final claim. It needs something like an **assumption graph**: which conclusion depends on which measurement, which measurement depends on which tool, which analysis depends on which transformation, which evaluator depends on which rubric.

When reality disagrees, suspicion can move through the graph rather than mechanically destroying the first hypothesis in sight.

This is also why “add a verifier agent” is dangerously comforting. A verifier may share the same base model, source, blind spot or broken test as the builder.

A verifier is not an oracle merely because somebody gave it the title *Verifier* in YAML.

The better question is Popper's question after some repair:

**What could make this answer lose?**

Code has tests. Mathematics can have proof checking or another mathematician finding the missing step. Science has experiment and measurement. Factual claims have sources, sometimes direct observation. UX eventually has users. Strategy has consequences, usually arriving later and with an invoice.

The goal is not universal falsification.

It is **exposure**.

## Science Becomes Architecture

Recent scientific-agent systems become interesting at exactly this point, because they are no longer just several language models talking to one another.

Stanford's Virtual Lab is deliberately organized like a research group: an AI principal investigator coordinates scientist agents, while humans provide high-level input and perform physical work needed to close the loop. In the nanobody project, computational agents proposed candidates that were then synthesized and tested in the laboratory.

Proteins were made.

Experiments happened.

**Reality got a vote.**

Other systems, including FutureHouse's Robin, push on similar research loops around literature, analysis, hypothesis generation and wet-lab feedback. The interesting object is not an “AI scientist” replacing a human scientist. It is a **research network** in which different cognitive and physical jobs are performed by different kinds of participants.

That distinction matters because scientific discovery has always been distributed. One person understands the disease. Another understands the assay. A third notices the statistical problem. Somebody else maintains the instrument everyone depends on and is mysteriously never on the author list.

Models add new kinds of specialists to this network.

**The scientific method itself is becoming an architecture.**

Hypothesis generation can be separated from criticism, literature search from experimental analysis, natural-language intuition from executable computation. Independent theories can survive long enough to compete, while experiments can still kill beautiful nonsense.

We have spent this book wrapping models in structures that compensate for what models cannot safely do alone.

Science did the same thing to humans centuries ago.

Apparently we are porting it.

## Mathematics Leaves the Benchmark

Mathematics makes the transition especially visible because the pushback can be unusually sharp. A biological hypothesis may survive for years before the decisive experiment. A mathematical proof has a more immediate enemy: one invalid step can kill the whole thing.

For years, much of the visible progress in AI mathematics was still benchmark-shaped—astonishing olympiad performance, but on questions whose answers were already known. By 2026, that boundary had started to move.

An internal OpenAI reasoning model produced a disproof of a long-standing conjecture around Erdős's planar unit-distance problem. The interesting part is not only that a model found an unexpected construction. External mathematicians then checked the argument, wrote a human-readable companion analysis and situated it inside existing mathematics. The “autonomous” result immediately entered a human epistemic institution. It had to survive people who understood the field well enough to ask whether it was actually new, actually correct and actually important.

Formal proof search shows a different institution: model-generated ideas coupled to Lean, where the final proof has to survive a machine-checkable formal system. Multi-agent research systems such as QED and Research Math Agents add decomposition, retrieval, structured memory, proposal, refinement and verification around the proof process.

The exact headline numbers will age.

The composition is the point.

A model may propose an idea, another attack it, Lean reject an invalid step, retrieval surface prior work, a human mathematician notice that the supposedly new theorem appeared in 1987, and another human decide whether the result matters.

None of these is *the* intelligence.

Increasingly, the intelligence is in the composition.

This gives the old System 3 slogan a more mature form. The world that pushes back is not always physical. In mathematics, proof pushes back. In code, execution pushes back. In science, experiment pushes back.

And in every case, humans remain inside the network that determines what was actually learned.

## Humans Are in the Network

This is important enough to state plainly: I do **not** think the future scientific institution is a society of artificial agents with one lonely human standing outside the box holding a red approval button.

Humans are nodes in the network.

Sometimes the human chooses the problem. Sometimes she supplies tacit knowledge that never made it into the literature. Sometimes he notices that the model's proof is technically correct but mathematically boring. Sometimes humans operate the physical instrument because the AI cannot. Sometimes they are the critic, the source of a new conjecture, the person who recognizes a connection across fields, or the one who says, “I know the benchmark says this is better, but something smells wrong.”

And humans are unreliable too. They have prestige hierarchies, fashionable theories, sunk costs, grudges, career incentives, and an extraordinary ability to become emotionally attached to a hypothesis after naming it.

The point of an epistemic institution is not to insert a pure human oracle into an impure machine process.

It is to arrange **fallible participants of different kinds** so their strengths combine and their errors do not line up too neatly.

That changes how I think about “human in the loop.” The phrase makes the human sound like a safety interlock. In a real epistemic network, the question is much richer:

**Where is human judgment most valuable?**

Maybe not on every proof step, if Lean can check those. Maybe not on every literature query, if retrieval is better. Human attention may be most valuable at problem selection, conceptual reframing, deciding significance, resolving ambiguity, operating the physical world, or noticing when the entire research program has become silly.

The goal is not to remove humans from the loop.

It is to stop wasting humans on the parts of the loop where they add the least information.

## A Swarm Should Not Be a Meeting

Once humans and agents are inside the same epistemic network, another temptation appears: give everyone the same context, ask for opinions, and aggregate.

This sounds democratic and often produces consensus with suspicious speed.

Lakatos gives us a better image. Science can contain **competing research programs** that preserve different commitments long enough to develop them. Translated into agent architecture, that means something more interesting than ten agents voting. One lineage may think the bottleneck is data, another architecture, a third that both are distractions because the objective is wrong.

Let them accumulate different evidence, tools, failures and local expertise before forcing convergence.

This is the epistemic cousin of MAP-Elites. In Chapter 2, diversity over **solutions** kept search from collapsing onto one local optimum. Here, diversity over **theories and research programs** protects inquiry from collapsing onto one worldview.

But how long should a weak program survive?

Larry Laudan's distinction between **acceptance** and **pursuit** is useful. I can think an idea is probably wrong and still think it deserves investigation because it is cheap to test, explains an anomaly nobody else can explain, or would change everything if true.

“Prune ruthlessly” needs an asterisk.

A research institution should distinguish how much it believes an idea from how valuable it would be to keep investigating it.

Then comes the scheduler. Suppose program A looks strongest and already has twelve researchers—some human, some artificial—while program B looks weaker and has one. Where should researcher thirteen go?

Philosophy and sociology of science have long worried about versions of this problem: division of labour, incentives, reputation, cooperation, competition, credit, neglected questions. Systems such as Fugu now make **part of the allocation problem executable**: they can choose which minds to recruit and how to organize them.

They do not tell us what the institution **should** optimize.

The theory with the highest current score is not necessarily where the next unit of research effort has the highest value. Optimize only short-term benchmark gain and we may build the academic equivalent of a company where every new employee joins the team that already has the most headcount.

So the organization is more than an org chart. It includes roles, information, incentives, reputation, authority, memory and exposure to consequences.

Epistemology has an organizational layer.

## The Agent Gets a Social Position

So far, the institution has mostly been a research institution. Real agents will also sit inside companies, families, governments, marketplaces and communities, where the question is not merely what is true but who is allowed to do what for whom.

A persistent agent in a company Slack or family message thread is not just a tool with permissions. Over time it acquires something like a **social position**. Different people can instruct it, some people outrank others, private information may help a shared task, and one person's optimization target may make somebody else's life worse.

At this point software architecture quietly turns into political philosophy, which I regard as progress.

Because an organizational agent has **principals**, not merely users.

“Align the agent to the user” therefore lasts about five minutes before somebody asks the obvious question:

Which user?

We will return to that later. First, organizations have another problem closer to home.

## Unfortunately, Organizations Have Emergent Goals Too

Take strong models, give them complementary roles, preserve independent lines of inquiry, learn the org chart, keep humans where their judgment matters, connect the whole thing to experiments and proofs, and congratulations:

artificial scientific civilization.

Chapter 1 should have made us more suspicious than that.

Emergent systems do not produce what you wanted because the architecture diagram looked reasonable. They produce what their structure and incentives select for.

Sales optimizes sales. Growth optimizes growth. Finance optimizes cost. Moderation optimizes safety. Everyone can be competent inside the box while the organization produces something nobody would have endorsed if shown the whole trajectory at the beginning.

Humans have a technical term for this:

Tuesday.

**Local alignment does not compose automatically. Neither does local truth.**

Five agents can cite the same mistaken source. Ten specialists can inherit one false assumption from the orchestrator. A critic can become ceremonial. A hierarchy can suppress dissent. A flat swarm can preserve diversity until everyone spends the afternoon synchronizing status.

This is the social version of the problem from Chapter 4: every component can look locally reasonable while the larger chain fails coherently.

System 3 cannot stop at individual agents.

The organization itself needs a trust architecture.

## What Kind of Society Should Think About This?

At the beginning of this book I kept returning to markets, science, cities and ecosystems as examples of emergence: interacting components, feedback, selection, history, no single designer specifying the final state.

Four chapters later, we have somehow started rebuilding them inside the machine.

That was not where I expected the argument to go.

The first agent architectures looked like workflows because workflows were what software engineers knew how to build. Then models became capable enough to decide pieces of the workflow themselves. We added workers, managers, independent critics, learned coordinators, scientific teams, formal verifiers and humans occupying different places in the same network.

Somewhere along the way the boundary between **reasoning** and **organization** started to disappear.

Maybe it was always blurrier than we thought.

A scientific community is a way of thinking that no individual scientist can perform. A court uses adversarial procedure because one coherent narrative is not enough. A market can aggregate information no trader possesses globally. Peer review inserts another mind between a claim and institutional acceptance.

None is a magic truth machine.

Each changes what the participating minds can collectively know and do.

**Institutions are cognitive technology.**

So once agents become capable enough, we are no longer deciding only which model should answer.

We are deciding **what kind of society should think about the problem**.

A hierarchy? Independent investigators? A scientific lab? A generator and adversarial critic? Competing research programs? A learned topology like Fugu? Or one agent, because the task does not deserve a civilization?

The design variables are no longer merely model and prompt. They are who sees what, who can challenge whom, which disagreements survive, what gets remembered, where humans enter, where incentives point, what has an exposure path to reality, and when a minority idea deserves another round of compute.

## Philosophy, Translated Into Architecture

The philosophers were not designing agent frameworks, and their theories disagree with one another in important ways. What transfers is the **failure mode** each one made visible.

| Philosophy of science | Failure mode | Architectural consequence |
|---|---|---|
| **Popper** | A claim that never risks failure can remain persuasive forever | Give important claims an **exposure path**: tests, experiments, proof checks, adversarial criticism, or eventual outcomes |
| **Duhem–Quine** | Evidence normally confronts bundles of assumptions | Maintain **dependency and assumption graphs** so failure triggers epistemic debugging rather than automatic blame |
| **Kuhn** | Stable frameworks enable deep work and create blindness | Let successful patterns become defaults while tracking anomalies and preserving a **reframing mode** |
| **Lakatos / Laudan** | Rival programs can remain worth pursuing even when not currently winning | Preserve **persistent lineages** and separate confidence from value of pursuit |
| **Division of scientific labour** | Incentives, specialization, reputation and information flow affect what communities can know | Design the **scheduler, information flows, authority, incentives and credit structure**, not only prompts |

The comparison is mine, not a blueprint any of these philosophers proposed for AI.

But it clarifies why this is more than metaphor.

Philosophy of science spent a century finding ways intelligent people can collectively fool themselves. Agent architecture gives us the uncomfortable opportunity to instantiate those failure modes at machine speed—and perhaps to design responses more deliberately.

The useful question is not “Which philosopher wins?”

It is:

**Which epistemic failure am I currently building?**

A system may be impossible to falsify, blame the wrong component when a test fails, converge too quickly, reopen every settled question forever, freeze a successful framework into dogma, or allocate all of its attention to the theory already winning.

**Philosophy identified the tensions. Architecture has to make choices about them.**

This is where the chapter lands for me:

**Agentic architecture is epistemology made executable. Multi-agent architecture is social epistemology made executable.**

## And Then the Society Remembers

There is one final problem.

A society that solves one problem and disappears can improvise forever.

A persistent society cannot.

If the same team repeatedly discovers that one testing strategy works, eventually it stops debating the testing strategy. A proof pattern that succeeds gets reused. A reliable tool becomes boring infrastructure. An organizational structure that keeps winning becomes the starting point for the next problem.

This is useful. Without such stabilization, every Monday begins with a philosophical inquiry into whether unit tests are still a good idea.

Kuhn's interesting point was not the phrase “paradigm shift.” It was the tension underneath it. Deep scientific work requires periods in which people **do not reopen every fundamental assumption every morning**. A stable framework lets a community accumulate techniques, standards and detailed knowledge.

Permanent skepticism sounds heroic.

Operationally it is exhausting.

But stability also creates blindness. A successful framework influences which problems look interesting, which tools seem legitimate, which anomalies can be ignored for another year and which alternatives never receive serious attention. Eventually the machinery that made deep work possible can become the thing preventing the next kind of work.

Agent societies will inherit exactly this tension.

They need memory strong enough to create cumulative competence and doubt strong enough to stop accumulated competence from becoming dogma.

A good organization therefore develops habits, procedures, stories about why things are done a certain way, rules inherited from old failures, techniques learned from researchers who are no longer there, shortcuts, taboos, best practices and inevitably a few superstitions.

Eventually the org chart is no longer the whole organization.

There is also **culture**.

And if human–AI societies are going to persist, they need a way for useful experience to survive the particular humans and agents who discovered it—without turning every successful accident into permanent law.

That is where patterns enter the story.

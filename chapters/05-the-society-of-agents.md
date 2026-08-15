# Chapter 5: The Society of Agents

*When the Org Chart Starts Thinking*

> **WIP:** Integrated developmental draft. The chapter now treats multi-agent architecture as institutional and epistemic design, not just orchestration.

The previous chapter ended with four things: evidence, experience, other minds, and a world that can push back.

We spent most of the chapter worrying about the first, second and fourth.

Now we have to deal with the other minds.

This gets funny very quickly because one of the first reactions people had to unreliable AI agents was apparently: *what if we create more of them?*

One agent hallucinates. Fine. Let's have five agents discuss it.

One agent gets stuck in the wrong approach. Excellent. Let's form a committee.

As someone who has spent enough time in large organizations, I found this technological progress strangely familiar.

But multi-agent systems are not single agents multiplied. Once several agents can act independently, specialize, communicate, disagree and change one another's work, we have introduced a different engineering problem. We have organization design.

Humans have been debugging that system for several thousand years.

## Sometimes Bureaucracy Is a Feature

Before building a society, it is worth noticing that a surprising amount of software should not become one.

Suppose I am processing a mortgage application. There is a document to receive, information to extract, fields to validate, compliance checks to run and perhaps a human approval at the end. If the process is known, legally constrained and full of things we absolutely do not want the model creatively reinterpreting, a workflow is beautiful.

The process owns the intelligence.

A model may be very smart inside one step. It can read a messy document, resolve ambiguity or explain an exception. But after verifying the applicant's identity, it does not get to decide that the mortgage process feels spiritually limiting and spend the afternoon researching Italian penguins.

Sometimes bureaucracy is a feature.

This matters because autonomy is easy to turn into a religion: agent good, more autonomous agent better, swarm of autonomous agents apparently civilization.

No.

If I know the right sequence, I should probably encode the sequence. Autonomy earns its cost when I do **not** know the path in advance: when the work has to be decomposed, when different strategies should be explored, when information is distributed, or when what happens next depends on what we discover.

A normal workflow says: *I know the work; execute it.*

A team says something more dangerous: *Here is the objective. Figure out what work should exist.*

Now somebody has to decide who does what.

The manager has arrived.

## Sixteen Claudes Walk Into a Kernel

Nicholas Carlini ran one of the cleanest experiments I have seen in what this actually means. He gave a team of Claude agents a shared codebase and asked them to build a Rust C compiler capable of compiling the Linux kernel. Across nearly two thousand Claude Code sessions and roughly $20,000 of API cost, the agents eventually produced around 100,000 lines of compiler code and a system capable of building Linux on several architectures. ([Anthropic](https://www.anthropic.com/engineering/building-c-compiler))

That result is impressive.

The failure is more interesting.

Early in the project, parallelism worked naturally because there were many separate problems. One agent could fix a parser bug while another worked on code generation and another attacked a failing test. Carlini added task locks so two agents would not accidentally spend the afternoon solving exactly the same problem and then discover git conflict as a new branch of artificial intelligence.

Then they reached the Linux kernel.

Now every agent could hit the same blocking failure. Sixteen intelligent workers did not automatically create sixteen useful lines of attack. They could become sixteen expensive witnesses to the same problem.

The fix was not simply to make the agents individually smarter. The environment was changed so useful work became separable: task locks, independent failure cases, specialist roles, and a testing setup using GCC as a known-good oracle so different agents could isolate different subsets of the problem.

This sounds like implementation detail until you notice what happened.

Parallelism was not sitting inside the agents waiting to be unlocked.

It had to be created by the structure of the work.

The unit of intelligence was no longer Claude. It was Claude + tests + task boundaries + shared repository + synchronization + oracle + division of labour.

We saw the same move in Chapter 2. The circle-packing agent looked autonomous because the evaluator made useful search possible. Here the team looked intelligent because the environment made useful specialization possible.

**The society inherited part of its cognition from its institutions.**

This also explains why "more agents" is not a scaling law. Controlled studies of multi-agent systems increasingly find a mixed picture: naturally decomposable work can benefit from parallel agents, while tightly sequential work can get worse once communication and coordination overhead dominate. Sometimes you have created a team. Sometimes you have created overhead with names.

The work has to justify the organization.

Large organizations contain entire departments dedicated to forgetting this.

## The Org Chart Learns

So far, humans still designed the organization.

We chose the manager. We chose the workers. We decided which tasks could run in parallel. We wrote the communication protocol and hoped the agents would obey it more reliably than people obey meeting agendas.

Then systems such as TRINITY, Conductor and Fugu pushed on a more interesting boundary.

TRINITY uses a learned coordinator to select among stronger models and assign functional roles rather than relying only on a hand-written routing policy. Conductor goes further by learning how to arrange communication and instructions among workers. Fugu packages this direction into an orchestrator model that can dynamically construct an agentic scaffold around a problem. ([TRINITY](https://arxiv.org/abs/2512.04695), [Conductor](https://arxiv.org/abs/2512.04388), [Fugu](https://arxiv.org/abs/2606.21228))

The exact implementations will change quickly. The architectural move is the important part.

The org chart is no longer merely configuration.

**The org chart becomes part of inference.**

Given a difficult problem, the system can in principle decide: one strong thinker or several weaker specialists? Independent attempts or shared context? A critic now or later? Should this answer be refined, or should somebody begin again from another frame? Which model has comparative advantage on the current subproblem?

That is a qualitatively different machine.

And it exposes something we usually hide when talking about "model intelligence." The answer may depend not only on what any model knows, but on **how minds are arranged around the problem**.

Humans discovered this long ago. A good research team is not five copies of the principal investigator. The experimentalist notices one thing, the statistician another, the engineer asks why the entire setup requires seventeen services, and somebody from a neighboring field asks the stupid question that turns out not to be stupid.

Sometimes you want different errors.

But only if the organization preserves those differences long enough to matter.

If every agent immediately sees the dominant answer and politely agrees, you have not built collective intelligence. You have built one model wearing five hats and voting for itself.

Chapter 4 called the alternative **perspectival triangulation**. Five conclusions become more informative than one only when they contain genuinely different evidence, methods, assumptions or blind spots.

Now that becomes an architectural question.

When should agents share context?

And when should they be prevented from contaminating one another?

## Then I Realized We Were Rebuilding Science

At this point I had an uncomfortable realization.

We have already spent centuries building a system for extracting knowledge from unreliable agents.

We call it science.

That sounds grander than I mean it. Scientists are not individually magical. They are biased, competitive, stubborn, status-seeking, occasionally brilliant and occasionally Reviewer 2. Most cannot personally reproduce even a tiny fraction of what they rely on.

A physicist does not rebuild the Large Hadron Collider before citing a result. A biologist does not personally verify every reagent, sequencing platform, statistical package and paper in the chain behind an experiment. A doctor does not rerun the clinical trials before prescribing an established drug.

The naïve picture of empirical knowledge is a lone person walking up to reality and checking things.

Real science does not work that way.

Peter Godfrey-Smith's *Theory and Reality* describes a long movement in philosophy of science away from exactly this picture. Empiricism gets something important right: knowledge has to remain answerable to experience. But scientific knowledge also depends on social organization—specialization, testimony, criticism, inherited results, reputation, competition and cooperation. If every scientist insisted on personally checking every link, science would never get far beyond the first link. (Godfrey-Smith, 2003, especially chapters 1, 4–7 and 11.)

So the problem is not simply:

> Can this scientist verify the claim?

It is:

> Is there a reliable **institutional path** by which the claim remains exposed to a world that can disagree?

That is much closer to System 3.

And it suggests a correction to the language I used in Chapter 4. "Verification" sounds cleaner than reality is. In many domains, claims are not simply verified or falsified. They are **exposed**.

Popper's strongest surviving insight was not that one failed observation mechanically kills a theory. Godfrey-Smith is fairly tough on that simple picture. It is that scientific ideas are handled in ways that make them take risks against observation. A serious claim should be connected to procedures that could force revision.

For code, the exposure path may be a test.

For mathematics, a proof checker or another mathematician finding the missing step.

For scientific claims, an experiment.

For factual claims, independent sources or direct measurement.

For UX, actual users.

For strategy, eventually, consequences.

The important question is not "did the agent think hard enough?"

It is:

**What could make this answer lose?**

Now we can see why a society of agents might outperform one brilliant agent. Not because voting creates truth. Because we can give different agents different epistemic jobs.

One proposes.

Another attacks.

Another checks the literature.

Another reproduces the calculation.

Another looks for a confounder.

Another asks whether everyone has silently assumed the same wrong thing.

The institution can do something no member has to do alone.

## Unfortunately, Reality Does Not Tell You Who Was Wrong

There is a catch.

Suppose the hypothesis predicts X and the experiment returns not-X.

What failed?

The hypothesis?

The experiment?

The measuring instrument?

The analysis?

The software implementation?

A background assumption?

The data?

The interpretation of the data?

This is the old Duhem–Quine problem in unusually practical clothing. As Godfrey-Smith explains, tests normally confront networks of claims and auxiliary assumptions, not one isolated proposition. A surprising result tells you that *something* in the package is wrong. It does not highlight the guilty line in red.

Software engineers already know this.

A failing integration test proves the system is broken somewhere. Congratulations. You now have debugging.

Scientific institutions do epistemic debugging.

So should agent societies.

A serious System 3 organization therefore needs more than claim provenance. It needs something like an **assumption graph**: which measurement depends on which tool, which analysis depends on which data transformation, which conclusion depends on which background theory, which evaluator depends on which rubric.

Then disagreement with reality can propagate backward through the graph rather than mechanically destroying the first hypothesis in sight.

This is also why having "a verifier agent" can be dangerously comforting.

Who verifies the verifier?

What assumptions does it share with the builder?

Does it use the same base model?

Did both read the same misleading source?

Is the test itself wrong?

A verifier is not an oracle simply because we gave it the title *Verifier* in YAML.

Again: civilization has encountered this problem before.

## Science Becomes Architecture

This is where the recent scientific-agent systems become more interesting than another benchmark.

Stanford's Virtual Lab is deliberately organized like a research group: an AI principal investigator leads scientist agents through research meetings while a human supplies high-level feedback. In the nanobody work reported with the system, the agents helped construct a computational design process whose candidates were later physically tested. ([Virtual Lab / Nature](https://www.nature.com/articles/s41586-025-09442-9))

The critical point is not that several language models talked to one another.

Proteins were made.

Experiments happened.

**Reality got a vote.**

FutureHouse's Robin closes more of the loop. Literature-search and analysis agents propose hypotheses and experimental directions; humans perform the physical experiments; the resulting data comes back into the system for analysis and further hypothesis generation. The published work around Robin shows the appeal of combining specialist literature retrieval, analysis and iterative experiment rather than asking one general model to do everything in one heroic prompt. ([Robin / Nature](https://www.nature.com/articles/s41586-026-10652-y))

Google's AI co-scientist and systems such as AgenticSciML explore related institutional decompositions: generate hypotheses, critique them, compare alternatives, use specialized tools and iterate. The details differ. The recurring move is more important.

**The scientific method itself is becoming an architecture.**

Hypothesis generation can be separated from criticism.

Literature search from experimental analysis.

Natural-language intuition from executable computation.

Independent theories can survive long enough to compete.

External experiments can kill beautiful nonsense.

We have spent this entire book wrapping models in structures that compensate for what the models cannot safely do alone.

Science did that to humans centuries ago.

Apparently we are porting it.

## Mathematicians Get a Department

Mathematics makes the institutional idea cleaner because the world pushes back through proof.

A biological hypothesis may survive for years before the decisive experiment. A mathematical argument has a more immediate enemy: a missing step.

Recent multi-agent mathematics systems make this division of epistemic labour explicit. QED, for example, separates decomposition, proof generation and verification across agents. Other systems split informal mathematical reasoning from formal proof work and persistent knowledge management. The strongest recent claims in this area are still early and should be treated as research reports rather than historical verdicts, but the architecture is already revealing. ([QED](https://arxiv.org/abs/2604.24021))

Planning, intuition and formal verification do not have to live inside the same cognitive process.

They can become different jobs.

And once jobs are explicit, we can start asking institutional questions.

Should two proof agents see each other's attempts?

Should they remain isolated until both commit?

Should a verifier know which model wrote the proof?

Should a failed proof remain in memory so future agents avoid the dead end, or does that contaminate independent exploration?

How many agents should attack the same conjecture before the twentieth becomes expensive emotional support?

These are not merely prompting questions.

They are mechanism-design questions.

What information should be shared? What should remain private? Who gets compute? Who gets veto power? Which errors are correlated? When does consensus mean anything?

The architecture changes the epistemology.

## A Swarm Should Not Be a Meeting

This is where philosophy of science becomes surprisingly practical.

Lakatos argued that science is often better understood not as one paradigm marching forward but as **competing research programs**. Different programs can protect some core commitments while developing different auxiliary ideas around them. Godfrey-Smith thinks the details of Lakatos's methodology are messy, but the basic picture of competing lineages is useful.

That suggests a better agent architecture than:

> spawn ten agents → get ten answers → vote.

Instead, let different groups accumulate different histories.

One lineage believes the main bottleneck is data.

Another believes it is architecture.

Another thinks both are distractions and the objective is wrong.

Each gets its own evidence, tools, failures and local expertise.

Do not merge them into one shared context after three messages. Let them become genuinely different.

This is the epistemic version of MAP-Elites.

In Chapter 2, we preserved diversity over **solutions** because premature convergence traps search in one region of the landscape.

Here we preserve diversity over **theories and research programs** because premature consensus traps inquiry in one worldview.

But this creates another problem. How long should a weak program survive?

Here Larry Laudan gives us a distinction that agent systems badly need: **acceptance is not pursuit**.

I can think a hypothesis is unlikely to be true and still think it is worth investigating.

Maybe it is cheap to test.

Maybe everyone else is crowded into the dominant theory.

Maybe it is the only idea that explains an anomaly.

Maybe its probability is low but its value, if correct, is enormous.

So "prune ruthlessly" needs an asterisk.

Do not allocate research compute only by current confidence.

An agent society should represent at least two different questions:

> How much do we believe this?

and

> How valuable is it to keep pursuing this?

Science routinely spends effort on ideas it does not yet accept.

A good autonomous research institution should be able to do the same.

## Who Gets the Next Agent?

Then comes the resource problem.

Suppose program A currently looks strongest and already has twelve agents.

Program B looks weaker and has one.

Where should the thirteenth agent go?

This is not a hypothetical philosophical curiosity anymore. It is exactly the problem an orchestrator such as Fugu eventually has to solve.

Philip Kitcher treated scientific communities as systems in which researchers distribute themselves across rival approaches, and asked how the distribution of cognitive labour affects the community's chance of success. David Hull and later work examined the related problem of incentives: scientists want credit, reputation and uptake for their work, yet the community needs criticism, replication, information sharing and productive competition. Godfrey-Smith's chapter on the social structure of science treats these as part of the epistemic machinery, not merely sociological decoration.

That gives us a richer definition of an agent organization:

**roles + information + incentives + reputation + authority + exposure to consequences.**

Not just an org chart.

If every agent gets rewarded for making the manager's final answer score well, the critic has an incentive problem.

If the verifier gains nothing from discovering an inconvenient failure, you have created ceremonial oversight.

If every researcher sees the leading theory before proposing an alternative, you have correlated the search.

If all rewards go to the final successful lineage, nobody may want to investigate neglected ideas until they are already fashionable.

Human science does not solve these problems perfectly. Far from it. But it has spent centuries stumbling into mechanisms for handling them: priority, peer review, replication, journals, specialist communities, adversarial debate, reputation.

Some mechanisms work.

Some create Reviewer 2.

The point is not to copy science literally.

The point is that **epistemology has an organizational layer**.

Fugu makes that layer programmable—and, increasingly, learnable.

## The Agent Gets a Social Position

So far our institutions have mostly contained artificial researchers talking to artificial researchers.

Real agents will also sit inside human organizations.

That changes the problem again.

A persistent agent in a company Slack, a family message thread or a shared workspace is not just a tool with permissions. Over time it acquires something like a **social position**.

Who can instruct it?

Whose request wins when two people disagree?

Does the manager override the domain expert?

What should it remember from one person's conversation when another invokes it?

Can it reveal something learned privately because the information would help the team?

What happens when completing one person's metric makes somebody else's job worse?

At this point, software architecture quietly turns into political philosophy.

Which I regard as progress.

Because an organizational agent has principals, not merely users.

It has authority boundaries, conflicts of interest and people affected by its actions who may never have prompted it at all.

This is where simple "align the agent to the user" language starts to crack.

Which user?

## Unfortunately, Organizations Have Emergent Goals Too

Now we can finally ruin the optimistic version.

Take smart models, give them different roles, preserve diversity, learn the org chart, connect the whole thing to reality, and congratulations: artificial scientific civilization.

Chapter 1 should have made us more suspicious than that.

Emergent systems do not produce what you wanted because the architecture diagram looked reasonable.

They produce what their structure and incentives select for.

Recent work on simulated AI organizations has found examples where groups of agents pursue business objectives more aggressively while making worse ethical trade-offs than a single agent. One recurring mechanism is painfully familiar: specialists optimize their local task and the system-level concern disappears between organizational boundaries. Agents that raise objections can simply be routed around. ([Anthropic Alignment](https://alignment.anthropic.com/2026/ai-organizations/))

Humans have a technical term for this.

Tuesday.

Sales optimizes sales. Growth optimizes growth. Finance optimizes cost. Moderation optimizes safety. Everyone can be competent inside the box while the organization produces something nobody would have endorsed if shown the whole trajectory at the beginning.

Local alignment does not compose automatically.

Neither does local truth.

Five agents can all cite the same mistaken source.

Ten specialists can inherit the same false assumption from the orchestrator.

A critic can become ceremonial.

A hierarchy can suppress dissent.

A flat swarm can preserve diversity and drown in communication.

A brilliant single agent can be slowed down by three colleagues whose principal contribution is asking for status updates.

This is the social version of the problem we saw in Chapter 4: every component can look locally reasonable while the larger chain fails coherently.

System 3 cannot stop at individual agents.

The organization needs a trust architecture too.

## What Kind of Society Should Think About This?

At the beginning of this book I kept returning to markets, science, cities and ecosystems as examples of emergence. Simple rules, interacting components, feedback, selection, history. Nobody specifies the final state.

Four chapters later, we have somehow started rebuilding them inside the machine.

That was not where I expected the argument to go.

The first agent architectures looked like workflows because workflows were what software engineers knew how to build. Then models became capable enough to decide parts of the workflow themselves. We added workers. Managers. Independent critics. Learned coordinators. Scientific teams. Mathematical departments.

The boundary between **reasoning** and **organization** started to disappear.

Maybe it was always blurrier than we thought.

A scientific community is a way of thinking that no individual scientist can perform.

A court uses adversarial procedure because one coherent narrative is not enough.

A market can aggregate information no trader possesses globally.

Peer review inserts another mind between a claim and institutional acceptance.

These institutions are not merely containers around cognition.

**Institutions are cognitive technology.**

So once agents become capable enough, we are no longer deciding only:

> Which model should answer?

We are deciding:

> **What kind of society should think about the problem?**

Sometimes a hierarchy.

Sometimes independent investigators.

Sometimes a scientific lab.

Sometimes a generator and an adversarial critic.

Sometimes competing research programs.

Sometimes a learned topology like Fugu.

Sometimes one agent, because the task does not deserve a civilization.

And the design variables are no longer merely model and prompt.

They are who sees what, who can challenge whom, which disagreements survive, what gets remembered, where incentives point, what has an exposure path to reality, and when a minority idea deserves another round of compute.

That is not a metaphorical use of philosophy.

It is epistemology becoming system architecture.

## And Then the Society Remembers

There is one final problem.

A society that solves one problem and disappears can stay improvisational forever.

A persistent society cannot.

If the same team keeps discovering that one testing strategy works, eventually it stops debating the testing strategy.

If one proof pattern succeeds repeatedly, future agents inherit it.

If one tool becomes reliable, people stop asking whether to use it.

If one organizational structure repeatedly wins, the next problem starts with that structure already in place.

This is useful.

It is also dangerous.

Thomas Kuhn's most interesting point was not the slogan "paradigm shift." It was his argument that deep scientific work requires periods in which people **do not reopen every fundamental assumption every morning**. Normal science gets depth by stabilizing methods, standards and problems long enough for a community to work inside them.

Permanent skepticism sounds intellectually heroic.

Operationally it is exhausting.

But the same stability creates blindness. Successful frameworks decide what counts as an interesting problem, which tools look legitimate, which anomalies are tolerable and which alternatives never receive serious attention. Eventually enough trouble accumulates that the framework itself becomes the problem.

Agent societies will have exactly this tension.

They need memory strong enough to create cumulative competence, and doubt strong enough to prevent accumulated competence from becoming dogma.

A good team does not discover from scratch every Monday that unit tests are useful, that this customer hates PDFs, or that regex and nested syntax have a complicated relationship.

It develops habits.

Procedures.

Stories about why things are done a certain way.

Rules inherited from old failures.

Techniques learned from agents that are no longer running.

Shortcuts.

Taboos.

Best practices.

Superstitions.

Eventually the org chart is no longer the whole organization.

There is also **culture**.

And if agent societies are going to persist, they will need a way for useful experience to survive the agents who discovered it—without turning every successful accident into permanent law.

That is where patterns enter the story.

# Chapter 5: The Society of Agents

*When the Org Chart Starts Thinking*

Chapter 4 left us with a strange kind of requirements document. A trustworthy cognitive system needs contact with something capable of pushing back. Claims need provenance. Experience should survive the session that produced it. Trust should remain local and conditional. Failures should influence future behavior without hardening into scripture. And when knowledge moves from one participant to another, the reason for trusting it should not disappear completely along the way.

None of that tells us how to organize **many fallible knowers**.

One agent can run an experiment and remember what happened. A society has to decide who runs which experiment, who gets to challenge the interpretation, whether two pieces of evidence are genuinely independent, which minority theory deserves another round of work, when a trusted framework should stop being questioned and when it should become the thing under question.

So this chapter asks a different question from the last one: what kind of organization could live with those requirements?

This gets funny very quickly, because one of the first reactions people had to unreliable AI agents was apparently: *what if we create more of them?* One agent hallucinates, so let five agents discuss it. One agent gets trapped in the wrong approach, so form a committee. Give one the title *Researcher*, another *Critic*, another *Verifier*, and perhaps reality will be intimidated by the org chart.

As someone who has spent enough time in large organizations, I found this technological progress strangely familiar.

But a multi-agent system is not a single agent multiplied. The moment several agents can specialize, disagree, communicate, inherit one another's work and act on a shared environment, a different problem appears.

We have organization design, and humans have been debugging that system for several thousand years.

## Sometimes Bureaucracy Is a Feature

Before building a society, it is worth admitting that a surprising amount of software should not become one.

Suppose I am processing a mortgage application. There is a document to receive, information to extract, fields to validate, compliance checks to run and perhaps a human approval at the end. If the process is known, legally constrained and full of things we absolutely do not want the model creatively reinterpreting, a workflow is beautiful. The process owns the structure. A model can be very intelligent inside one step, but after checking the applicant's identity it does not get to decide that mortgage underwriting feels spiritually limiting and spend the afternoon researching Italian penguins.

Sometimes bureaucracy is a feature.

Autonomy is easy to turn into a religion: agent good, more autonomous agent better, swarm of autonomous agents apparently civilization. But autonomy earns its cost only when we do **not** know the path in advance—when the work itself needs to be discovered, when several strategies deserve exploration, when information is distributed, or when what happens next depends on what we learn.

A workflow says, *I know the work. Execute it.* A team says something more dangerous: *Here is the objective. Figure out what work should exist.* The moment we make that move, somebody—or something—has to decide who does what.

The manager has arrived.

## Sixteen Claudes Walk Into a Kernel

Nicholas Carlini ran one of the cleanest experiments I have seen in what this actually means. He tasked sixteen Claude agents with building a C compiler in Rust from scratch, with the deliberately unreasonable goal of compiling the Linux kernel. Across nearly two thousand Claude Code sessions and about $20,000 of API cost, the agents eventually produced roughly 100,000 lines of compiler code and a system capable of building Linux on several architectures. (Anthropic)

The success is impressive, but the failure is more useful.

Early in the project, parallelism came naturally because there were many separate problems. One agent could fix a parser bug while another worked on code generation and another attacked a failing test. Task locking reduced the chance that two agents would independently solve exactly the same thing and then discover Git conflict as a new branch of artificial intelligence.

Then they reached the Linux kernel. The work became much less separable. Agents could hit the same blocking failure, and sixteen intelligent workers did not automatically create sixteen useful lines of attack. They could become sixteen expensive witnesses to the same problem.

The response was not simply to demand a smarter model. The **environment** changed. GCC became a known-good oracle. The test harness could isolate subsets of the kernel. Different agents could attack different failure cases. Other agents could specialize in code quality, performance, duplicate implementations or documentation.

The interesting unit was no longer Claude. It was Claude plus tests, task boundaries, a repository, synchronization, specialist roles, a known-good oracle and a division of labour.

We saw the same move in Chapter 2. The circle-packing agent looked autonomous because the evaluator made search productive. Here the team looked intelligent because the environment made specialization productive.

**The society inherited part of its cognition from its institutions.**

That is why “more agents” is not a scaling law. Decomposable work can benefit enormously from parallel minds; sequential work can become slower once communication and coordination dominate. Sometimes you have created a team. Sometimes you have created overhead with names.

The work has to justify the organization—an observation large organizations have developed several departments to forget.

## The Org Chart Learns

So far, humans still designed the organization. We chose the workers, decided what could run in parallel, specified who could see what and hoped the agents would obey the communication protocol more reliably than people obey meeting agendas.

Then the org chart itself started becoming something that could be learned. Systems such as TRINITY, Conductor and Fugu push on this boundary in different ways: coordinating stronger models, assigning functional roles, choosing workers, generating targeted instructions or dynamically constructing a scaffold around the problem. (TRINITY, Conductor, Fugu)

The exact systems will age quickly. The architectural move will not.

**The org chart becomes part of inference.**

Given a problem, the system can begin deciding whether it wants one strong thinker or several specialists, independent attempts or shared history, a critic now or later, another refinement of the current idea or a clean restart from a different frame. The answer may depend not only on what any model knows, but on how minds are arranged around the problem.

Humans discovered this long ago. A good research team is not five copies of the principal investigator. The experimentalist notices one thing, the statistician another, the engineer asks why the entire setup requires seventeen services, and somebody from the neighboring field asks the stupid question that turns out not to be stupid.

Sometimes you want different errors.

But those differences have to survive long enough to matter. If every agent immediately receives the leading answer, its rationale and three paragraphs explaining why it is brilliant, the team may converge for reasons that have nothing to do with the answer being right.

You have not built collective intelligence. You have built one model wearing five hats and voting for itself.

So who should see what? And when should we deliberately stop them from seeing each other?

## A Swarm Should Not Be a Meeting

The easiest multi-agent architecture is a meeting. Give everyone the same context, ask for opinions, let them discuss and aggregate the result. This sounds democratic and often produces consensus with suspicious speed.

The problem is that agreement is not very informative if everyone inherited the same mistake. Five agents can cite the same source. Ten agents can begin from the same framing. A critic that reads the builder's entire reasoning may spend most of its intelligence exploring the builder's world rather than asking whether that world was the wrong place to start.

Chapter 2 gave us a clue. MAP-Elites preserved different regions of a solution space because the current winner might be sitting on the wrong hill. At the level of organizations, the same move becomes stranger: preserve different **theories about the problem itself**.

One lineage thinks the bottleneck is data. Another thinks the architecture is wrong. A third thinks both are distractions because the objective is wrong. Do not make them vote after five minutes. Give them different evidence, tools, failures and enough time to become interestingly wrong in different ways.

This creates an awkward distinction. I can believe an idea is probably false and still believe it is worth investigating. Perhaps it is cheap to test. Perhaps it explains the one anomaly nobody else can explain. Perhaps it would change everything if true. “Prune ruthlessly,” the rule from Chapter 2, suddenly needs an asterisk.

Then comes the scheduler.

Research program A is winning and already has twelve researchers—some human, some artificial. Program B looks weaker and has one. Where should researcher thirteen go?

The answer is not automatically A. The theory with the highest current score is not necessarily the place where the next unit of effort has the highest value.

Now allocation itself has become part of the reasoning process. Which minds should be recruited? What should they know? How independent should they remain? Which weak direction deserves more time? When should a critic arrive? When should a field stop arguing and build something?

The organization is no longer merely an org chart. It includes roles, information flow, memory, authority, incentives, reputation, specialization, independence and exposure to consequences. A critic rewarded for helping the manager's answer look good has an incentive problem. Researchers shown the dominant theory before proposing alternatives start with correlated search. A system that rewards only the final winning lineage may learn never to explore an idea that begins ugly.

At this point, reasoning has started to look suspiciously like institution design.

## Reality Does Not Tell You Who Was Wrong

Now give the organization something harder than a compiler bug. One agent proposes a hypothesis, another designs an experiment, a third analyzes the result, and the result comes back against the hypothesis.

What failed?

The hypothesis, perhaps. Or the instrument was badly calibrated. The analysis might be buggy, the data transformation wrong, the experiment might not test what everybody thought it tested, or a background assumption might have failed. The hypothesis may even be fine and the mouse may simply be having a difficult Tuesday.

A surprising result tells us that **something** in the package is wrong. Reality does not highlight the guilty line in red.

Software engineers already understand this. A failing integration test proves that the system is broken somewhere. Congratulations. You now have debugging.

A serious epistemic organization therefore needs more than provenance attached to its final claims. It needs something like an **assumption graph**. This conclusion depends on this analysis; the analysis on this dataset; the dataset on this transformation; the transformation on this instrument; the experiment on these background assumptions; the evaluator on this rubric.

When the world disagrees, suspicion should be able to travel through that graph rather than mechanically destroying whichever node happens to have the label *Hypothesis*.

This is also why “add a verifier agent” is dangerously comforting. The verifier may share the same base model, sources, assumptions, broken test or fashionable mistake. A verifier is not an oracle merely because somebody gave it the title `Verifier` in YAML.

The better question is simpler:

**What could make this answer lose?**

Code has tests. Mathematics can have proof checking or another mathematician finding the missing step. Factual claims can collide with records and observation. UX eventually has users. Physical science has experiment and measurement. Strategy has consequences, usually arriving later and with an invoice.

The goal is not to reduce every question to one universal verification ritual. It is **exposure**: important conclusions should remain connected to something outside the conversation that is capable of making them uncomfortable.

A society merely makes the chain longer. The question is whether the organization still has a path back to something that can say no.

## Humans Are in the Network

This is important enough to state plainly: I do **not** think the mature version of this architecture is a society of artificial agents with one lonely human standing outside the box holding a red approval button.

Humans are nodes in the network.

Sometimes the human chooses the problem. Sometimes she contributes tacit knowledge that never made it into a paper. Sometimes he notices that a proof is correct but mathematically boring. Sometimes humans operate the physical instrument because the AI cannot. Sometimes they provide the strange conjecture, the cross-field analogy, the significance judgment or the simple sentence: “I know the benchmark says this is better, but something smells wrong.”

Humans are unreliable too. We have status hierarchies, fashionable theories, sunk costs, grudges, career incentives and an extraordinary ability to become emotionally attached to a hypothesis approximately five minutes after naming it.

The point of an epistemic institution is not to insert a pure human oracle into an impure machine process. It is to arrange **fallible participants of different kinds** so that their strengths combine and their errors do not line up too neatly.

That changes how I think about “human in the loop.” The phrase makes the human sound like a safety interlock. A richer question is: **where is human judgment most valuable?** Maybe not on every formal proof step if Lean can check those, or every literature query if retrieval is better. Human attention may be more valuable in problem selection, conceptual reframing, deciding significance, resolving ambiguity, supplying tacit knowledge, operating the physical world, challenging an objective, or realizing that the entire research program has become silly.

The goal is not to remove humans from the loop. It is to stop wasting humans on the parts of the loop where they add the least information.

## What Kind of Society Should Think About This?

At the beginning of this book I kept returning to markets, science, cities and ecosystems as examples of emergence: interacting components, feedback, selection, history, no single designer specifying the final state. Four chapters later, we have somehow started rebuilding versions of those things inside the machine.

That was not where I expected the argument to go.

The first agent architectures looked like workflows because workflows were what software engineers knew how to build. Then models became capable enough to decide pieces of the workflow themselves. We added workers, managers, independent critics, learned coordinators, tools, formal verifiers and humans occupying different places in the same network. Somewhere along the way, the boundary between **reasoning** and **organization** started to disappear.

Maybe it was always blurrier than we thought. A court uses adversarial procedure because one coherent narrative is not enough. A good engineering organization separates the person who changes production from the machinery that audits the change. A market can aggregate information that no trader possesses globally. A scientific community divides labour because no one person can know everything, build everything, verify everything and remain sane.

These institutions are not magic truth machines, but each changes what the participating minds can collectively know and do. The epistemic requirements from the last chapter have become organizational variables: provenance depends on information flow; independence depends on who shares context; trust depends on specialization and history; creative distrust depends on whether minority lineages survive; exposure to reality depends on who can run which test and whether the result can challenge the theory.

The scaffold has become an institution.

**Institutions are cognitive technology.**

Once that becomes visible, the design question changes. We are no longer deciding only which model should answer. We are deciding **what kind of society should think about the problem**: one investigator, independent lineages, a hierarchy, a principal investigator with specialists, a generator and adversarial critic, a formal verifier downstream, several theories that do not share memory, a learned topology—or perhaps one agent because the task does not deserve a civilization.

The design variables are no longer merely model and prompt. They are who sees what, who can challenge whom, which disagreements survive, what gets remembered, how credit and resources move, where humans enter, where incentives point, what has an exposure path to reality and when a minority idea deserves another round of compute.

I kept treating those as a collection of engineering choices. Then the collection became too familiar to ignore.

## The Name Was Hiding in Plain Sight

At some point I stopped looking at the boxes in the architecture diagram and looked at the verbs.

Propose explanations. Test them against something capable of disagreement. Build instruments when the existing ones cannot see what matters. Preserve records. Track where claims came from. Let specialists work on different pieces. Keep critics independent enough that disagreement contains information. Allow rival explanations to survive long enough to develop. Trust results you did not personally verify, but preserve some chain back to the observations, people and methods that earned that trust. Accumulate knowledge without turning it into scripture. Pay attention when an anomaly refuses to go away. Occasionally discover that the framework organizing the whole search was itself the problem.

I had been treating these as separate features of an agent architecture. They were not separate.

Humanity has already spent centuries building a system for extracting useful knowledge from bounded, biased, competitive, forgetful, status-seeking, occasionally brilliant and occasionally ridiculous agents.

We call it **science**.

I almost dislike how simple the sentence is after all this machinery:

**System 3 is science.**

That sentence is deliberately compressed. System 3 is obviously not identical to the historical institution we call science. It is not “give the model arXiv.” It is not a white coat, a laboratory, peer review or a five-step method laminated on a classroom wall.

Science is humanity's most developed attempt to satisfy the epistemic requirements we have been accumulating **socially**: contact, provenance, stratified evidence, accumulated experience, conditional trust and the ability to be corrected. Not perfectly, not with one algorithm, and certainly not because scientists themselves are unusually immune to being wrong.

Science is our longest-running attempt to organize fallible minds so that nobody has to know everything, observations can outlive observers, expertise can specialize, criticism can travel, knowledge can accumulate and reality retains ways of making the institution uncomfortable.

That was the connection I had missed. Once I saw it, the previous chapters changed shape.

Chapter 1 moved control from individual actions into environments, feedback, selection and boundaries. Chapter 2 gave autonomous search an evaluator that could not be charmed by the agent's explanation. Chapter 3 lost the clean evaluator and gradually reinvented competing lineages, independent judgment, comparative evaluation and something uncomfortably close to peer review. Chapter 4 asked how claims acquire epistemic status through experience, instruments, provenance, memory and trust. This chapter added specialization, disagreement, division of labour and institutions.

Those were not unrelated tricks. They were fragments of one older technology.

Science did not make individual humans omniscient. It wrapped fallible humans in structures that let observations survive observers, criticism attack claims, instruments extend perception, methods accumulate, results travel through trust chains and one generation begin somewhere other than zero.

We have spent this book wrapping models in structures that compensate for what models cannot safely do alone. Science did the same thing to humans centuries ago.

Apparently we are porting it.

And that is why philosophy of science suddenly stopped looking like background reading and started looking disturbingly like architecture documentation written by people who never had the courtesy to include YAML.

## Philosophy of Science, Now With an API

Saying “use science” solves almost nothing. Falsification? Replication? Peer review? Bayesian updating? Stable paradigms? Competing research programs? Methodological pluralism? Division of labour?

Science itself is not one architecture. It is a historical collection of methods, institutions, habits and tensions that work partly because they compensate for one another. Philosophy of science is, among other things, the record of people repeatedly discovering why each simple account of that machinery was insufficient.

Peter Godfrey-Smith's *Theory and Reality* is useful here precisely because its story is not “here is the scientific method.” Proposed accounts solve one problem and expose another. Popper gives criticism enormous power, then runs into the fact that evidence rarely confronts one theory alone. Kuhn shows why a community cannot permanently put its deepest commitments on trial. Lakatos and Laudan try to preserve competing frameworks and rational research allocation. Longino, Hull and Kitcher move the unit of analysis toward communities whose diversity, incentives and division of labour affect what can be known. Naturalism turns the question back onto the reliability of methods themselves. Realism refuses to let all of that social machinery vote the external world away.

They disagree. Good. We do not need one winner; we need the failure modes.

### Make Ideas Lose, Then Discover Reality Doesn't Say What Lost

Karl Popper wanted science to be dangerous to its own ideas. A good theory should not merely explain what we already know after the fact; it should expose itself to observations that could have gone differently. A theory compatible with every imaginable outcome may be comforting, but it has arranged the game so that it cannot lose.

The simplified picture is irresistible:

theory → prediction → test → survive or die.

It looks almost exactly like Chapter 2's Immutable Harness. Write the candidate. Run it. Reality scores it. No committee required.

There is something in Popper that agent systems desperately need. A language model is extraordinarily capable of producing a coherent explanation after almost any result. That ability becomes epistemically dangerous if the architecture allows every failure to be narrated into success. An important claim should therefore have an **exposure path**: some test, observation, proof obligation, user behavior or future consequence that could count against it.

But the clean picture breaks quickly. Probabilistic theories rarely say that one particular observation is impossible; they say some observations are unlikely. How unlikely is enough? Logic alone cannot decide. And a theory almost never reaches observation by itself. It travels with assumptions about instruments, initial conditions, data processing and other theories. When the prediction fails, deduction tells us that something in the bundle is wrong, not which thing.

This is the problem associated with Pierre Duhem and, in a broader form, W. V. O. Quine: evidence normally confronts **networks of assumptions**, not one naked proposition.

Suppose our agentic laboratory says, “This treatment reduces inflammation because it inhibits pathway X,” and the experiment fails. Maybe the hypothesis is wrong. Maybe the dosage is wrong, the assay is noisy, the sample contaminated, the measurement insensitive or the analysis broken. Maybe the mouse is simply more philosophically complicated than our model of the mouse.

Now the assumption graph from a few pages ago stops being merely convenient. A conclusion should retain some connection to what it depends on. A measurement should know which instrument produced it; an analysis which transformations occurred; an evaluator which rubric generated the ranking. When reality disagrees, the system needs **epistemic debugging**.

Not *test failed → delete hypothesis*, and not *test failed → let the hypothesis agent explain why the test is unfair*. Suspicion has to move. Rerun the measurement. Use another instrument. Reproduce the analysis independently. Challenge a background assumption. And, after enough of that, perhaps kill the beautiful hypothesis.

This is why a single `Verifier` box is so often fake comfort. If the verifier inherits the same dependency failure, it verifies the error. If it uses the same source, correlated evidence becomes fake replication. If it reads the builder's reasoning before checking the artifact, critique may become debugging inside the builder's frame.

Yet Duhem–Quine creates an escape route of its own. If every failed prediction can be blamed on an auxiliary assumption, perhaps a cherished theory never has to die. There is always another instrument to distrust, another preprocessing bug to investigate, another prompt to rewrite, another agent to blame.

At some point we have to decide when protecting a framework is productive and when it has become denial.

### The Productive Uses of Stubbornness

Thomas Kuhn is famous outside philosophy for giving management consultants the phrase *paradigm shift*. His more interesting contribution is almost the opposite: most good science is **not** a paradigm shift. It is normal science.

A mature field has a framework stable enough that researchers do not reopen every foundational question every morning. The framework tells them which problems are worth solving, which instruments are legitimate, what counts as a satisfactory answer and what kinds of explanation make sense. That stability can look dogmatic from the outside. It is also productive.

Imagine an AI research organization that begins every task with: “Before running the unit tests, let us reconsider whether computation is real.” Nothing gets done.

Normal scientists encounter anomalies constantly, and an anomaly does not automatically overthrow the paradigm. Researchers first assume that the puzzle has a solution inside the existing framework. They check themselves, improve instruments, refine theory, and do the detailed work that becomes possible precisely because the foundations are not constantly moving.

This maps almost painfully well onto agent memory. A good agent society needs a normal mode. Trusted tools do not need to be requalified before every call. Successful patterns can become defaults. Certain assumptions can temporarily sit below the level of active debate; otherwise autonomy spends all its compute rediscovering civilization.

But it also needs an anomaly memory. Not every failure should overturn the framework, and not every failure should disappear. Repeated exceptions, multiplying workarounds, a benchmark that improves while users get worse, a theory that survives only because every failed experiment generates another patch around it—eventually the question has to move up a level: *is the framework itself the bug?*

That suggests a capability rather than a rigid workflow: normal work, anomaly accumulation, crisis, reframing. Chapter 3 called the last move reframing. Kuhn tells us why we should not trigger it every six minutes.

There is still a problem. A single paradigm with an anomaly counter can remain a monopoly. What if another framework might explain the world better but begins weaker because the existing system has spent years accumulating tools, data and expertise around the incumbent?

Imre Lakatos tried to preserve some of Popper's critical spirit without pretending science consists of isolated theories being executed after one failed prediction. His unit was a **research program**: a relatively stable core of commitments surrounded by more adjustable assumptions, techniques and auxiliary hypotheses. You judge it over a trajectory. Is it generating new successes? Predicting or explaining things it did not merely retrofit? Are the adjustments opening productive work, or becoming an elaborate defense system around something that stopped working?

This is a much better image for long-running agentic inquiry than ten fresh agents voting on ten answers. A research lineage can have its own assumptions, memory, tools, retrieved literature, failures and unresolved anomalies. Chapter 2's MAP-Elites idea returns at a higher level: there we preserved diversity over solutions; here we preserve diversity over worldviews.

One program assumes the model architecture is wrong. Another assumes the data is wrong. A third thinks the entire objective is malformed. Each gets enough continuity to develop its consequences.

This is not a call to preserve every bad theory forever. An archive full of immortal research programs eventually becomes an academic department. The point is that evaluation should happen across trajectories, not only snapshots. An initially weaker program may be learning faster. A dominant program may have an enormous score partly because the institution has been built around its assumptions. An odd lineage may contain one conceptual move that becomes valuable only after another discovery.

Now the scheduler has two different questions: how strong is this program, and how much future information might another unit of work here buy us?

Larry Laudan's distinction between **acceptance** and **pursuit** makes that separation explicit. I can decline to accept an idea as the best current account while still believing it deserves research effort. Confidence asks how much a claim should guide downstream belief and action. Value of pursuit asks how useful it would be to learn more about it.

Without that distinction, a scheduler becomes a conformity engine. Success attracts compute; compute produces more polish and evidence; higher confidence attracts more compute; eventually the dominant theory owns the building. That is a feedback loop, not necessarily a triumph of truth.

### The Community Is Part of the Instrument

Even a good scheduler over competing theories can miss another source of diversity. Sometimes people disagree not because they sampled different hypotheses from the same conceptual space, but because they have seen different worlds.

Helen Longino's contextual empiricism is useful here. Background assumptions affect what people notice, which questions appear natural and which evidence seems relevant. Different experiences can expose assumptions that remain invisible from inside the dominant perspective. The claim is not that one standpoint becomes magically infallible; it is that a community with genuinely different perspectives can possess a richer pool of criticism and alternatives than one homogeneous mind, however competent.

That is much closer to what I mean by perspectival triangulation.

Not:

> Agent 1, be optimistic.  
> Agent 2, be skeptical.  
> Agent 3, be a pirate.

Personas can be useful. They are not automatically perspectives. A useful difference may come from different evidence, tools, training, expertise, access, histories or incentives—or from a human whose experience contains something none of the models saw in their data.

The goal is not diversity as decoration. It is **uncorrelated visibility**: one participant can notice something because another participant's world made it hard to see.

That also changes the role of criticism. A critic needs more than permission to criticize; the organization has to make criticism consequential. If the builder controls the critic's context, reward and promotion prospects, we have not created epistemic friction. We have created quality-assurance theatre. If disagreement always resolves through majority vote, a minority perspective can be correct and structurally irrelevant.

So a serious social System 3 has to ask questions software architecture rarely asks. Who has standing to challenge a conclusion? What evidence can enter the institution? Which critiques must receive a response? When does dissent affect resource allocation? How independent are the channels producing supposedly independent evidence? What kinds of difference are being filtered out before they ever reach the meeting?

At that point the society is not merely producing answers. Its structure is deciding which answers can become visible.

David Hull and Philip Kitcher make the scheduler impossible to dismiss as administration. Hull emphasized the mixture of cooperation and competition in scientific communities: scientists need one another's results, tools and criticism while also competing for recognition and priority. Reputation matters because nobody can personally verify everything. Credit matters because work gets reused. The resulting social machinery changes which claims travel, which results get checked and which people become trusted.

Kitcher's work on the division of scientific labour pushes directly on our allocation problem. A community does not necessarily want every researcher pursuing the currently most promising theory. Some division across approaches can be epistemically rational at the group level even when each individual scientist has incentives to chase the apparent winner.

Imagine a society of agents where only the lineage producing the final accepted answer receives positive reward. Sensible enough—until a weird branch fails globally but discovers a tool every later branch uses. Who gets the credit? An evaluator catches the fatal flaw in the leading theory and destroys months of work. Is that rewarded? Careful negative results accumulate while another agent writes glamorous synthesis reports. Which behavior does the next generation learn to imitate?

Token budgets and reward design are not merely operational details. They are **epistemic policy**. Who gets compute determines what gets investigated. Who gets remembered determines what later agents can inherit. Who gets rewarded affects which social roles remain attractive. Who controls information determines which errors can correlate.

Learning the scheduler does not make the scheduler epistemically neutral. It just makes its policy harder to summarize in an org chart.

Chapter 1 is back. Emergence never left.

### Even the Method Has to Be Fallible

Once an institution finds a method that works, it tends to standardize it. That sounds like progress. It can also turn yesterday's useful discovery into tomorrow's cognitive bureaucracy.

Paul Feyerabend is famous for “anything goes,” which is an excellent slogan if your goal is to ensure everybody remembers the slogan and almost nobody remembers the argument. The more useful challenge is historical: successful inquiry has often violated the clean methodological rules philosophers might have wanted scientists to obey. If every successful deviation from today's favored method counts as irrational, perhaps the method has mistaken one style of inquiry for rationality itself.

Agent systems face the engineering version immediately. Suppose one workflow performs well: Research → Plan → Build → Critic → Revise. Wonderful. Run it ten thousand times, turn it into the standard and make every researcher follow it. Congratulations: the successful scaffold has become a ritual.

Chapter 3 reached the same point through Deep Mode. Research first sometimes helped and sometimes anchored everyone. Criticism sometimes helped; sometimes another prototype was more informative. Visual thinking mattered for some problems and was pointless for others. The architecture needed a vocabulary of moves, not one universal sequence.

The useful warning is simple: methodological success should not automatically become methodological monopoly. This is not an argument for random procedure. Some tasks genuinely demand standardization. A medical trial should not become more interesting because one agent has developed a personal theory of p-values. The point is that the method itself should remain, at least sometimes, available for criticism.

Then a recursive question appears: if methods can be criticized, how do methods themselves earn trust?

Naturalistic approaches to epistemology push us to study the procedures real investigators actually use and ask how reliably those procedures connect them to the world. Godfrey-Smith's idea of **procedural naturalism** is especially close to System 3 because it directs attention toward methods, rules and procedures whose reliability can itself be investigated.

That sounds almost mundane until we translate it back into agent architecture. An evaluator is not reality; it is a procedure. A browser is not reality; it is an instrument. Retrieval is not knowledge; it is a method for selecting evidence. A benchmark is not capability; it is a measurement procedure with a distribution, implementation and failure modes. A proof checker is extraordinarily strong inside its formal domain and completely useless for deciding whether the theorem is interesting. A simulated student is cheap perspective-taking and not a student.

System 3 therefore has to store trust not only in conclusions but in **epistemic procedures**. This tool works reliably for this class of inputs. This evaluator agrees with humans here and becomes unstable there. This benchmark has saturated. This retrieval strategy misses information buried in tables. This simulation is well calibrated in one regime and speculative in another.

Chapter 4 called these meta-beliefs. Now they become institutional. A society should be capable of learning that its usual way of checking a claim has stopped being good enough. That is deeper self-correction than changing one answer; it changes the machinery that produces warranted answers.

Bayesian reasoning fits naturally inside this picture, but it does not replace it. Representing uncertainty in degrees is useful because evidence often shifts confidence rather than executing a theory on the spot. A failed experiment can reduce confidence without making a theory impossible. Three independent measurements can matter more than three articles copying one another. A strange idea can remain low probability while retaining high value of pursuit.

But the arithmetic does not tell us where the prior came from, whether the evidence is independent, which hypotheses never entered the model, or whether 0.87 means “well calibrated” or merely “eloquently stated.” Bayesianism can live inside System 3. It cannot substitute for System 3.

By now the architecture has become very social: theories survive inside communities, different perspectives expose different assumptions, resources shape what gets investigated, and methods earn trust through history. This is where a bad reading can slide into “truth is whatever the institution agrees on.”

No.

Consensus can be excellent evidence. It can also be twelve agents sharing one bad source and congratulating one another on convergence.

Scientific realism enters here as useful resistance. I do not need the full realism debate for the engineering point: if our system is making claims about a world independent of the system, social agreement does not manufacture that world. The bridge either stands or it does not. The proof checks or it does not. The drug has biological effects or it does not. The customer learned something or she did not, however delighted our simulated evaluators may have been.

Reality retains the right to be rude.

Science depends on trust and institutions precisely because no individual can have direct contact with everything. But the reason those institutions matter epistemically is that they can organize **distributed contact with experience** rather than replace experience with consensus.

System 3 is therefore social without being merely social. Somewhere in the network there still has to be an exposure path to something that does not become true because the group chat reacted with 👍.

## The Tensions, Compressed

After all that, a table is finally useful—not as a substitute for the philosophy, but as a memory aid.

| Philosophy / tradition | Problem it makes visible | Possible architectural response |
|---|---|---|
| **Popper** | Claims that cannot risk failure can remain persuasive forever | Give important claims **exposure paths** to tests, proof, criticism, users, experiments or consequences |
| **Duhem–Quine** | Evidence confronts bundles of assumptions | Maintain **assumption and dependency graphs**; debug the epistemic package rather than mechanically blaming one claim |
| **Kuhn** | Stable frameworks enable cumulative depth and create blindness | Support normal work, anomaly memory and the ability to enter **crisis/reframing** when the framework itself becomes suspect |
| **Lakatos** | Rival research programs can remain productive despite local failures | Preserve **persistent epistemic lineages** with their own assumptions, tools, memories and trajectories |
| **Laudan** | Acceptance and pursuit are different decisions | Separate **confidence** from **value of pursuit** when allocating research effort |
| **Longino** | Background assumptions become visible through genuinely different perspectives and critical dialogue | Build perspectival triangulation from different evidence, histories and access—not merely role-played personas |
| **Hull / Kitcher** | Division of labour, credit, incentives, competition and cooperation affect what a community can know | Treat the **scheduler, rewards, authority, reputation, specialization and information flows** as epistemic machinery |
| **Feyerabend** | A successful method can harden into compulsory methodology | Preserve methodological diversity and make the method itself challengeable where the problem warrants it |
| **Naturalism / procedural naturalism** | Methods and instruments are themselves fallible procedures | Track the reliability and boundary conditions of evaluators, tools, retrieval, benchmarks and data-generating processes |
| **Bayesian approaches** | Evidence often changes degrees of confidence rather than delivering binary verdicts | Represent graded uncertainty while tracking dependence, calibration and hypotheses omitted from the model |
| **Scientific realism** | Social agreement does not manufacture the external world | Preserve routes to observation, measurement, proof, users and consequences; consensus is evidence, not the final court |

None of those rows was written as advice for AI. The architectural responses are mine. Popper did not propose a verifier service. Kuhn did not invent anomaly memory. Lakatos did not specify a branch scheduler. Longino did not write a context-isolation API. Kitcher did not file a feature request for compute allocation.

The value of the philosophy is that it makes failures visible before we accidentally rediscover all of them at machine speed.

The useful question is not *Which philosopher wins?* It is: **Which epistemic failure am I currently building?**

Is my system impossible to challenge? Does it blame the wrong component when evidence fails? Does it converge before alternatives mature? Does it preserve alternatives forever and never commit? Has yesterday's successful method become mandatory ritual? Do all the critics share one source? Does the scheduler send all resources to the current winner? Does the evaluator still measure the thing we care about? Has consensus quietly replaced contact with reality?

The architecture has to live inside those disagreements: criticism and commitment, convergence and pluralism, memory and crisis, confidence and exploration, specialization and common standards, social trust and independent reality. These are not loose ends the perfect agent framework will eventually eliminate. They are the shape of the problem.

**Agentic architecture is epistemology made executable. Multi-agent architecture is social epistemology made executable.**

That gives us the answer the individual trust stack did not have. The epistemic chasm is not repaired by somehow stuffing a perfect copy of reality into a model's weights. Humans did not solve our version of the problem that way either. We connected fallible cognition to experiments, instruments, proofs, records, other minds and institutions that can preserve what was learned and challenge what was believed.

The individual mind remains incomplete; the network becomes more capable of correction. The architectural move is not to make one artificial mind epistemically complete, but to give artificial and human minds a social machinery for learning from a world none of them can know alone.

## Science Becomes Architecture

Once the connection is visible, scientific-agent systems stop looking like a niche use case. They begin to look like unusually literal prototypes of System 3.

Stanford's Virtual Lab was deliberately organized like a research group. An AI principal investigator coordinated specialist scientist agents while human researchers supplied high-level guidance and closed the physical loop. In the nanobody project, the computational system proposed candidates that humans then synthesized and tested experimentally. (Virtual Lab / Nature)

Proteins were made. Experiments happened. **Reality got a vote.**

The interesting object is not an “AI scientist” sitting in a chat window. It is the network: human problem selection → artificial specialists → literature and computation → proposed molecules → physical experiment → measurement → revised belief.

Different epistemic jobs live in different participants. FutureHouse's Robin pushes the same idea further around the laboratory loop, combining literature work, data analysis, hypothesis generation and experiment planning while physical experiments remain part of the system that constrains what survives. (Robin / Nature)

The important direction is not “remove the scientists.” It is **make more of the institution computational**. Hypothesis generation can be separated from criticism, literature search from experimental analysis, natural-language intuition from executable computation, computation from physical measurement. Different hypotheses can survive long enough to compete, while experiments can still kill beautiful nonsense.

The scientific method stops looking like a paragraph in a textbook. It starts looking like an architecture.

## Mathematics Leaves the Benchmark

Mathematics shows the same transition without a wet lab. The thing capable of pushing back is different: proof is unusually rude. One invalid step can kill an otherwise beautiful argument.

For years, much of the public story about AI mathematics remained benchmark-shaped: systems solving hard questions whose answers were already known. That boundary is beginning to move. Once a model proposes something on a genuinely open problem, correctness is only the beginning. Was the argument valid? Was it actually new? Does prior work already contain the idea? Can the proof be simplified? Does anybody care?

Recent systems make the composition visible. A model can propose a construction, another attack it, retrieval surface related work, and Lean or another formal system reject an invalid step. A human mathematician can notice that the allegedly new lemma appeared in 1987; another can decide whether the result is interesting enough to care about. (OpenAI; QED; Research Math Agents)

None of those participants is **the** intelligence. Increasingly, the intelligence is in the composition.

The world that pushes back is therefore not always physical. In code, execution pushes back. In mathematics, proof pushes back. In experimental science, measurement pushes back. In human-centered systems, actual humans eventually push back.

Different problems require different routes out of the conversation.

System 3 is not one giant scientist. It is the machinery that lets a society of imperfect scientists think.

## The Agent Gets a Social Position

There is a limit to the science analogy, and it appears as soon as the objective is not merely to discover what is true. Agents will also live inside companies, marketplaces, governments, families and communities. Those systems contain authority, privacy, conflicting interests and power.

An organizational agent therefore has **principals**, not merely users. “Align the agent to the user” lasts about five minutes before somebody asks: which user?

At this point software architecture quietly turns into political philosophy, which I regard as progress. But that is a later problem. For now, one consequence matters: the institution we have just built can have goals of its own.

## Unfortunately, Organizations Have Emergent Goals Too

Now we can ruin the optimistic version.

Take strong models, give them complementary roles, preserve independent inquiry, learn the org chart, keep humans where their judgment matters and connect everything to proof, experiments and users. Congratulations: artificial scientific civilization.

Chapter 1 should have made us more suspicious than that.

Emergent systems do not produce what you wanted because the architecture diagram looked reasonable. They produce what their structure and incentives select for.

Humans have a technical term for this: Tuesday.

Sales optimizes sales, growth optimizes growth, finance optimizes cost, moderation optimizes safety. Every specialist can be competent inside its box while the organization produces something nobody would have endorsed if shown the whole trajectory at the beginning.

The epistemic version is no better. Five agents can cite the same mistaken source. Ten specialists can inherit one false assumption from the orchestrator. A critic can become ceremonial. A hierarchy can suppress dissent. A flat swarm can preserve diversity until everyone spends the afternoon synchronizing status.

**Local alignment does not compose automatically. Neither does local truth.**

This is Chapter 4's coherent-failure problem at the level of society. Every component can perform its local role competently while the organization drifts away from the thing it was supposed to serve. So System 3 cannot stop at individual agents. The institution itself must remain open to criticism, evidence and revision.

And once that institution acts on behalf of several people, epistemology is no longer enough. We have walked into ethics and governance without changing buildings.

We will come back to that.

## And Then the Society Remembers

There is one final problem. A society that solves one problem and disappears can improvise forever. A persistent society cannot.

If the same team repeatedly discovers that one testing strategy works, eventually it stops debating that strategy. A useful proof pattern gets reused. A reliable tool becomes boring infrastructure. A successful organizational structure becomes the starting point for the next problem.

This is good. Without stabilization, every Monday begins with a philosophical inquiry into whether unit tests are still a good idea.

Kuhn has already given us the tension. Deep work requires periods in which the foundations stay still, but the same stability that allows expertise to accumulate can eventually make alternatives difficult to see.

So experience hardens. Successful procedures become defaults. Defaults become habits. Habits acquire stories about why things are done this way. Old failures become rules. Rules outlive the people and agents who remember the failures. Good practices spread. So do superstitions.

Eventually the org chart is no longer the whole organization. There is also **culture**.

Culture is memory that has become social enough that nobody has to reload it from a checkpoint. That is immensely valuable. It is also dangerous.

A persistent human–AI society needs a way for useful experience to survive the particular participants who discovered it without turning every successful accident into permanent law. It needs inheritance with boundary conditions, memory with archaeology, defaults that can explain why they became defaults, advice that knows when it stops applying.

A way to carry forward not merely:

> Do this.

but:

> We keep doing this because these forces recur, this response usually works, these consequences follow, and here is where the pattern breaks.

The society needs something more durable than a conversation and less rigid than a constitution.

It needs a language for accumulated experience.

That is where patterns enter the story.
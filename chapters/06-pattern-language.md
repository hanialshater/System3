# Chapter 6: Pattern Language

*When Knowledge Becomes Software*

Chapter 5 ended with a sentence that was deliberately too simple for the machinery underneath it:

**System 3 is science.**

Not science as a five-step classroom diagram. Not science as “ask a model to search arXiv.” Science as a civilization-scale cognitive technology: instruments, records, criticism, specialization, standards, rival programs, trust, replication, accumulated experience and routes through which reality can remain inconvenient.

Apparently we are porting it.

That immediately creates another problem.

A society that solves one problem and disappears can improvise forever. A society that survives has to begin tomorrow somewhere other than zero.

Imagine hiring a brilliant employee who loses almost all procedural memory every evening. On Monday you explain how releases work. Tuesday, again. By Wednesday the employee has produced a beautiful deployment checklist. On Thursday you explain releases again. By Friday they have written a Python script that automates half the process and forgotten why the script exists.

This was approximately where agents started.

Context windows got larger. Projects persisted. Memory systems got better. Agents learned to leave notes for themselves. But the deeper problem was never simply remembering more text.

It was:

**How should useful experience become reusable behavior?**

Humans have already encountered the same problem at larger scales. A useful proof technique gets reused. A reliable instrument becomes boring infrastructure. A successful organizational structure becomes the starting point for the next problem. Old failures become rules. Rules outlive the people who remember the failures. Habits acquire stories about why things are done this way. Good practices spread.

So do superstitions.

Eventually the org chart is no longer the whole organization.

There is also **culture**.

Culture is memory that has become social enough that nobody has to reload it from a checkpoint.

That is immensely valuable and dangerous for exactly the same reason: useful experience can survive the participants who discovered it, and so can accidents whose original conditions disappeared thirty years ago.

Science compounds this way too. It does not advance because each generation receives a folder containing all previous conclusions. Communities inherit **ways of finding out**: instruments, protocols, experimental tricks, statistical habits, standards of evidence, named failure modes, things everybody in a field knows to check, and occasionally rules whose original justification has been forgotten so thoroughly that they have achieved the dignity of tradition.

If System 3 is science made architectural, then Pattern Language is part of its **cultural memory**.

Chapter 5 asked how a society of fallible minds can know more than its members.

This chapter asks how that society can **learn across time without turning yesterday's success into scripture**.

And this is where philosophy of science stops looking like background reading and starts looking disturbingly like architecture documentation written by people who never had the courtesy to include YAML.

## Philosophy of Science, Now With an API

“Use science” solves almost nothing.

Science is not one algorithm. It is a historical collection of practices and institutions that partly work because their weaknesses pull against one another.

Peter Godfrey-Smith's *Theory and Reality* is useful here because its story refuses to stay simple. Popper gives criticism enormous power, then evidence turns out to confront bundles of assumptions rather than one naked theory. Kuhn explains why a community cannot permanently put its deepest commitments on trial. Lakatos and Laudan preserve competing programs and separate current belief from the value of continued pursuit. Longino, Hull and Kitcher move the unit of analysis toward communities whose perspectives, incentives, credit and division of labour affect what can be known. Naturalism turns the same suspicion onto the procedures themselves. Realism refuses to let the institution vote the external world away.

They disagree.

Good.

We need the failure modes.

Because once an agent society can remember its experience, every old epistemological problem becomes a design question about **what gets remembered, how strongly, by whom, and under what conditions the memory can be challenged**.

### A Lesson Needs a Way to Lose

Karl Popper wanted science to be dangerous to its own ideas. A useful theory should expose itself to observations that could have gone differently. If every possible outcome can be narrated as success, the theory has arranged the game so that it cannot lose.

The simplified picture looks almost exactly like Chapter 2's Immutable Harness:

`theory → prediction → test → survive or die`

A language model makes Popper's warning unusually practical. Give a capable model a failed result and it can often produce a coherent explanation for why the failure does not really threaten the original story.

The same danger appears when we convert experience into reusable guidance.

Suppose an agent learns:

> Always use method X for this class of problem.

That looks like memory.

It may instead be the beginning of dogma.

A useful persistent lesson should retain an **exposure path**: a test, observation, proof obligation, user behavior or future consequence that could count against it.

The memory should not only say *what worked*.

It should preserve something about **how the world could prove that the lesson stopped working**.

That sounds simple until reality disagrees.

A theory almost never meets observation alone. It travels with assumptions about instruments, initial conditions, data processing, auxiliary theories and what the experiment actually measures. When the prediction fails, logic tells us that something in the bundle is wrong.

It does not tell us what.

Pierre Duhem made this point in the context of physical theory; W. V. O. Quine later pushed a broader version. Evidence confronts **networks of assumptions**.

Return to the agentic laboratory.

“This treatment reduces inflammation because it inhibits pathway X.”

The experiment fails.

Maybe the hypothesis is wrong. Maybe the dosage is wrong, the assay noisy, the sample contaminated, the measurement insensitive or the analysis broken. The mouse may still be having a difficult Tuesday.

Chapter 5 met the same problem in Boyle's air pump and in the modern laboratory. Reality can embarrass a package without highlighting the guilty component.

A persistent institution therefore needs enough archaeology to debug its own lessons. This conclusion came from this analysis, using this dataset, produced by this instrument, under these assumptions. A compact **assumption graph** lets a failed observation reopen the dependencies around a claim instead of mechanically executing whichever node happens to be called *Hypothesis*.

This is **epistemic debugging**.

And it applies to culture as much as to factual claims.

If a pattern fails, did the pattern stop working? Did the environment change? Was it retrieved in the wrong context? Was the evaluator broken? Was the original lesson only valid for one model, market, codebase or instrument?

A reusable lesson without its dependencies is easier to store.

It is also easier to misunderstand.

### Defaults Need the Right to Become Boring

The obvious response to fallibility is to keep everything permanently open to revision.

This is a terrible way to get work done.

Thomas Kuhn is famous outside philosophy for giving management consultants the phrase *paradigm shift*. His more useful contribution here is almost the opposite: most productive science is **normal science**.

A mature field has a framework stable enough that researchers do not reopen every foundational question every morning. The framework tells them which puzzles matter, which instruments are legitimate and what kinds of answers count. That stability can look dogmatic from the outside because, to some extent, it is.

It is also what lets a community go deep.

Imagine an AI research organization that begins every task with:

> Before running the unit tests, let us reconsider whether computation is real.

Nothing gets done.

Chapter 5's bureaucracy now looks different. A procedure can preserve something the institution has learned. Trusted tools do not need to be requalified before every call. Successful patterns can become defaults. Some assumptions can sit below the level of active debate while the community works on puzzles inside them.

A pattern language therefore needs **stability**.

If the system has tried twelve ways to perform a task and one has repeatedly survived, it should not pay the full exploration cost on every invocation merely to demonstrate philosophical sophistication.

Some choices have earned the right to become boring.

The danger is forgetting that the settlement was provisional.

Normal science encounters anomalies constantly, and most of them should not trigger a revolution. Researchers first check themselves, improve instruments and refine the theory. But anomalies that refuse to disappear need somewhere to accumulate.

Repeated exceptions. Multiplying workarounds. A benchmark improving while users get worse. A pattern surviving only because every failure generates another exception around it.

Eventually the question moves upward:

*Is the framework itself the bug?*

So persistent knowledge needs two things that pull against one another:

**defaults strong enough to support deep work, and anomaly memory strong enough to reopen the defaults.**

### Keep More Than the Winner

A single paradigm with excellent anomaly memory can still become a monopoly.

Another framework may begin weaker because the existing institution has spent years building instruments, data, tools and expertise around the incumbent.

Imre Lakatos gives us a better unit for that problem: the **research program**. A relatively stable core of commitments travels with more adjustable assumptions, techniques and auxiliary hypotheses. You judge the program over a trajectory. Is it opening new problems and producing new successes, or mainly constructing an elaborate defense system around something that stopped working?

That is close to the independent lineages we built before the science reveal. One program thinks the architecture is wrong. Another thinks the data is wrong. A third thinks the objective is malformed. Each carries its own assumptions, tools, failures and unresolved anomalies long enough to develop consequences rather than entering a vote after five minutes.

An institution that converts every local victory into one global pattern can erase this diversity surprisingly quickly.

The winning method gets used more. Because it gets used more, it accumulates more successful cases. Those cases raise its confidence. Higher confidence makes it more likely to be retrieved. The alternative receives less traffic and therefore less evidence.

Eventually the system has an impressive empirical record proving the thing it stopped comparing against.

Larry Laudan's distinction between **acceptance** and **pursuit** makes the allocation problem explicit.

I can decline to accept an idea as the best current account while still believing it deserves another experiment.

Those are different questions:

- **Acceptance:** what should guide belief and action now?
- **Pursuit:** where could another unit of investigation be valuable?

A pattern system should know the difference between:

> This is our current default.

and:

> This alternative is unlikely to be best, but another trial would teach us something important.

Without that separation, memory becomes a conformity engine.

### The Community Is Part of the Instrument

Even several well-funded research programs can share the same blind spots.

Different agents may sample different hypotheses from one conceptual space because they inherited the same data, tools, training and background assumptions.

Helen Longino's contextual empiricism makes the community itself epistemically important. Background assumptions shape what investigators notice, which questions appear natural and which evidence looks relevant. Participants with genuinely different experiences can expose assumptions that remain invisible from inside the dominant perspective.

That is much closer to **perspectival triangulation** than giving five copies of the same model theatrical personas:

> Agent 1, be optimistic.  
> Agent 2, be skeptical.  
> Agent 3, be a pirate.

A useful difference may come from different evidence, expertise, tools, histories, access or incentives—or from a human whose experience contains something none of the models saw in training.

The point is **uncorrelated visibility**: somebody can see a problem because another participant's world made it hard to see.

Persistent knowledge should therefore carry some trace of **position**.

Who learned this lesson?

From which class of tasks?

Using what tools and evidence?

Under which incentives?

A pattern discovered by a ranking team in Germany, a fraud team in Brazil, a compiler agent running one model version and a human physician may all be excellent inside their domains without acquiring universal authority merely because they were stored in the same database.

Criticism also needs standing. A critic whose objections never change allocation, publication, deployment or belief is performing quality-assurance theatre. A minority perspective can be technically alive and structurally irrelevant if disagreement never affects resources.

This is where David Hull and Philip Kitcher make power and incentives impossible to dismiss as administration. Scientific communities mix cooperation and competition. Researchers depend on one another's results, instruments and criticism while competing for priority, credit, jobs and resources. Reputation matters because nobody can personally verify everything. Credit matters because work gets reused. Division of labour matters because a community does not necessarily want every researcher pursuing the idea that looks strongest today.

Now token budgets, memory retention and retrieval policy look less operational.

**They are epistemic policy.**

Who gets compute determines what gets investigated. Who gets remembered determines what future agents can inherit. Who receives credit affects which roles remain worth performing. Who controls information determines which errors can correlate before anyone notices.

A learned scheduler does not make these choices neutral.

It makes the policy harder to summarize in an org chart.

### Even the Method Has to Be Fallible

Once an institution finds a method that works, it tends to standardize it.

Yesterday's successful experiment becomes today's best practice and tomorrow's compulsory ritual.

Paul Feyerabend is remembered for “anything goes,” which is a wonderful slogan if your goal is to make sure everyone remembers the slogan and almost nobody remembers the argument. The useful challenge is historical: successful inquiry has often violated the methodological rules philosophers wanted to treat as universal. A method can become so authoritative that departures count as irrational by definition, including the departures that would have revealed its limits.

Agent systems can do this at machine speed.

Suppose:

`Research → Plan → Build → Critic → Revise`

works extremely well.

We run it ten thousand times, turn it into the standard and make every problem enter the same ceremony. Deep Mode already showed why that can fail: research sometimes anchors; criticism sometimes arrives at the wrong moment; a prototype may teach more than another planning pass.

The method itself occasionally has to become available for criticism.

Then we inherit a recursive question:

**How do methods earn trust?**

Naturalistic approaches to epistemology push us toward the procedures investigators actually use and how reliably those procedures connect them to the world. Godfrey-Smith's idea of **procedural naturalism** is especially useful for System 3 because the procedure becomes an object of investigation too.

An evaluator is a procedure. A browser is an instrument. Retrieval is a method for selecting evidence. A benchmark is a measurement process with a distribution, implementation and failure modes. A proof checker is extraordinarily strong inside its formal domain and completely useless for deciding whether the theorem matters. A simulated student is cheap perspective-taking and not a student.

System 3 therefore needs trust in **epistemic procedures** as well as conclusions.

This evaluator tracks humans well here and becomes unstable there. This retrieval strategy misses information buried in tables. This benchmark has saturated. This instrument drifts under these conditions.

A scientific institution should be able to learn that its usual way of checking a claim is itself the thing that stopped working.

That is deeper self-correction than changing an answer.

The machinery that decides what counts as warranted can change too.

For Pattern Language, that means the machinery that **creates, scores, retrieves and retires patterns** cannot sit outside the same epistemology applied to the patterns themselves.

The library needs criticism.

So does the librarian.

### Confidence Is Not Contact

Bayesian reasoning fits naturally inside this architecture. Evidence often changes degrees of confidence rather than delivering binary verdicts. A failed experiment can reduce confidence without making a theory impossible. Three independent measurements can matter more than three articles copying one another. A strange idea can remain low probability while having high value of pursuit.

A persistent pattern can therefore carry confidence.

It probably should.

But the arithmetic is useful and incomplete.

It does not tell us where the prior came from, whether the evidence is genuinely independent, which alternatives never entered the model or whether 0.87 means “well calibrated” rather than “eloquently stated.”

Bayesianism can live inside System 3; it cannot carry the whole institution by itself.

After all this emphasis on communities, trust and social machinery, there is an easy bad reading:

Truth is whatever the institution eventually agrees on.

No.

Consensus can be excellent evidence. It can also be twelve agents sharing one bad source and congratulating one another on convergence.

Scientific realism enters here as useful resistance. I do not need the full realism debate for the engineering point. If the system is making claims about a world independent of the system, social agreement does not manufacture that world.

The bridge either stands or it does not.

The proof checks or it does not.

The drug has biological effects or it does not.

The customer learned something or she did not, however delighted our simulated evaluators may have been.

Reality retains the right to be rude.

Science needs trust and institutions because no individual can have direct contact with everything. Those institutions matter epistemically because they can organize **distributed contact with experience** rather than replace experience with consensus.

System 3 is social without being merely social.

Somewhere in the network there still has to be a route to something that does not become true because the group chat reacted with 👍.

## What Cultural Memory Has to Preserve

After all that philosophy, I find the tensions more useful than a list of winners.

| Tension | What a persistent agent society has to preserve |
|---|---|
| **Exposure ↔ underdetermination** | Lessons need ways to lose, while failed evidence must reopen the assumptions, tools and procedures around them rather than mechanically deleting one rule. |
| **Stability ↔ crisis** | Trusted patterns and methods need enough stability for deep work, plus anomaly memory and a route to reframing when the pattern itself becomes suspect. |
| **Convergence ↔ pluralism** | The institution must use current winners while preserving alternatives long enough to discover whether the winner occupies the wrong hill. |
| **Confidence ↔ pursuit** | What should guide action now and what deserves another experiment are different allocation decisions. |
| **Expertise ↔ independent perspective** | Specialization should create local epistemic standing without turning authority into universal rank or criticism into conformity. |
| **Inheritance ↔ archaeology** | Knowledge should survive its creators while retaining enough provenance, boundary conditions and failed history to avoid becoming superstition. |
| **Institution ↔ reality** | Trust, reputation, memory and consensus can carry knowledge only while routes to proof, observation, users, experiments and consequences remain capable of saying no. |

None of this was written as advice for AI.

Popper did not propose a verifier service. Kuhn did not invent anomaly memory. Lakatos did not specify a branch scheduler. Longino did not write a context-isolation API. Kitcher did not file a feature request for compute allocation.

The value of the philosophy is that it makes failure modes visible before we rediscover all of them at machine speed.

The useful question is not *Which philosopher wins?*

It is:

**Which epistemic failure am I currently building?**

Is my system impossible to challenge? Does it blame the wrong component when evidence fails? Does it converge before alternatives mature? Does it preserve alternatives forever and never commit? Has yesterday's successful method become mandatory ritual? Do all the critics share one source? Does the scheduler send all resources to the current winner? Does the evaluator still measure the thing we care about? Has consensus quietly replaced contact with reality?

The architecture has to live inside those disagreements. They are not loose ends the perfect agent framework will eventually eliminate.

They are the shape of the problem.

**Agentic architecture is epistemology made executable. Multi-agent architecture is social epistemology made executable.**

Now add one more step:

**Persistent agent architecture is culture made executable.**

## Science Becomes Architecture

This connection is already becoming literal.

Scientific-agent systems stop looking like a niche use case once you see the institution rather than the chatbot.

Stanford's Virtual Lab was deliberately organized like a research group. An AI principal investigator coordinated specialist scientist agents while human researchers supplied high-level guidance and closed the physical loop. In the nanobody project, the computational system proposed candidates that humans then synthesized and tested experimentally. (Virtual Lab / Nature)

Proteins were made.

Experiments happened.

**Reality got a vote.**

The interesting object is the network:

`human problem selection → artificial specialists → literature and computation → proposed molecules → physical experiment → measurement → revised belief`

Different epistemic jobs live in different participants. FutureHouse's Robin pushes the same idea further around the laboratory loop, combining literature work, data analysis, hypothesis generation and experiment planning while physical experiments remain part of the system that constrains what survives. (Robin / Nature)

The direction I care about is **making more of the institution computational**.

Hypothesis generation can be separated from criticism, literature search from experimental analysis, natural-language intuition from executable computation, computation from physical measurement. Different hypotheses can survive long enough to compete while experiments remain available to kill beautiful nonsense.

The scientific method stops looking like a paragraph in a textbook.

It starts looking like an architecture.

Mathematics shows the same transition without a wet lab. The thing capable of pushing back is different: proof is unusually rude. One invalid step can kill an otherwise beautiful argument.

Once a model proposes something on a genuinely open problem, correctness is only the beginning.

Was the argument valid?

Was it actually new?

Does prior work already contain the idea?

Can the proof be simplified?

Does anybody care?

Recent systems make the composition visible. A model can propose a construction, another attack it, retrieval surface related work, and Lean or another formal system reject an invalid step. A human mathematician can notice that the allegedly new lemma appeared in 1987; another can decide whether the result is interesting enough to care about. QED, formal proof-search agents and recent work on open Erdős problems make different pieces of that composition concrete. (QED; OpenAI; formal proof-search work)

The intelligence increasingly lives in the composition:

model intuition, retrieval, adversarial checking, formal verification and human mathematical judgment.

The thing that pushes back does not have to be physical.

Code has execution.

Mathematics has proof.

Experimental science has measurement.

Human-centered systems eventually have actual humans.

Different problems require different routes out of the conversation.

System 3 is the machinery that lets a society of imperfect investigators think.

Pattern Language is part of the machinery that lets the society **remember how to think**.

## When the Institution Wants Something

There is a limit to the science analogy, and it appears as soon as the institution is asked to do more than discover what is true.

Agents will live inside companies, marketplaces, governments, families and communities. Those systems contain authority, privacy, conflicting interests and power. An organizational agent has **principals**, not merely users.

“Align the agent to the user” lasts about five minutes before somebody asks:

Which user?

The institution can also acquire goals of its own. Sales optimizes sales, growth optimizes growth, finance optimizes cost, moderation optimizes safety. Every specialist can be competent inside its box while the organization produces something nobody would have endorsed if shown the whole trajectory at the beginning.

Humans have a technical term for this:

Tuesday.

Agent societies inherit the same problem. A critic can become ceremonial. A hierarchy can suppress dissent. A scheduler can reward whatever makes its own metrics look good. Ten specialists can inherit one false assumption from the orchestrator and execute it flawlessly.

**Local alignment does not compose automatically. Neither does local truth.**

And culture makes the problem persistent.

A local objective can become a local pattern. The pattern can be inherited by agents that never saw the original conflict. A workaround for one principal can become “best practice” for everyone. An institution can remember its incentives just as effectively as it remembers its wisdom.

The institution itself therefore has to remain open to criticism, evidence and revision. Once it acts on behalf of several people, epistemology runs into ethics and governance without changing buildings.

We will come back to that.

For now, we have enough requirements for memory.

The question becomes embarrassingly practical:

**What does executable culture actually look like?**

## Three Ways to Tell a Computer What You Know

For most of computing history, if you knew how a process should work, you translated that knowledge into code. A customer asks for a refund. If the amount is under €50, approve it. If it is over €500, ask a manager. If the order is older than thirty days, reject it unless a specific exception applies. You take what the organization knows and turn it into `if`, `else`, functions, database schemas, and state machines.

Call this **Software 1.0**. Andrej Karpathy used that label for the familiar world in which humans write the program directly. The computer does approximately what the code says, which gave us modern civilization and dependency injection.

Then machine learning changed the contract. Suppose the problem is not “refunds over €500 need approval” but “is this refund fraudulent?” Nobody knows the full rule. We have examples. So instead of writing the behavior, we write the training machinery, choose data and an objective, and optimization produces the behavior inside model weights.

Karpathy called this **Software 2.0**. Knowledge moved from explicit code into parameters. Humans no longer had to describe every feature that makes an image a cat, every acoustic variation that makes a sound a word, or every interaction that makes a recommendation relevant. We supplied data and pressure; the model discovered useful internal representations.

There was a trade. Software became vastly more capable in domains where rules were hard to articulate, but much of the learned knowledge became difficult to inspect. The fraud system “knows” patterns no engineer wrote down. You can measure its behavior, probe it, retrain it, maybe interpret pieces of it, but you cannot open `fraud_rules.py` and read what the organization learned.

Large language models created a third possibility. Karpathy's later **Software 3.0** framing treats natural language itself as a programming interface. The obvious version is a prompt:

> Read this support request, identify what the customer actually needs, check the relevant policy, and resolve it if you are confident. Escalate cases involving legal threats, suspected fraud, or policy conflicts.

That is not Software 1.0. Nobody enumerated every legal threat or every possible policy conflict. It is not Software 2.0 either. We did not retrain the model to teach it this workflow. We expressed operational knowledge in language and relied on a general model to interpret it.

But “prompt as program” is only the beginning.

The more interesting unit is becoming **executable knowledge**.

A persistent agent society can store not only an instruction but the situation in which it applies, what pressures produced it, how it has performed, where it has failed, which alternatives remain alive and what could make the institution reconsider it.

That begins to look less like a prompt library and more like culture with a runtime.

## The Return of Knowledge Engineering

“Knowledge engineering” has an unfashionable smell because AI has been here before. Expert systems tried to encode human expertise explicitly: rules about medicine, geology, finance, configuration. The dream was sensible. Find experts, extract what they know, put it into a knowledge base, and let a machine reason over it.

The maintenance was less romantic. Expertise is full of exceptions, tacit assumptions, context, competing heuristics, and sentences beginning with “normally, unless...”. Rule bases became brittle. Knowledge engineers spent their lives interviewing experts and converting fuzzy human practice into formal logic. Machine learning eventually offered a seductive alternative: stop asking experts to explain themselves and learn behavior from data.

Now knowledge engineering is returning through the back door, carrying Markdown.

The difference is important. We no longer have to compile every piece of knowledge into rigid symbolic logic. A modern skill can contain prose, examples, scripts, reference material, counterexamples, tool instructions, and boundary conditions. The language model does some of the interpretation that the old knowledge engineer had to make explicit.

This creates a kind of artifact that sits awkwardly between source code and training data. It might say:

> When reviewing a ranking experiment, first establish whether the apparent gain is concentrated in one market or traffic segment. Check instrumentation changes before inventing a causal story. If click metrics rise while orders remain flat, inspect price and position shifts before celebrating. Treat day-one effects with suspicion.

There is no deterministic function here. There is accumulated practice. A human expert can read it and use judgment. Now an agent can too.

So I think the deeper transition is not merely from Python to English.

It is a move from **programming behavior**, to **learning behavior**, to **engineering the knowledge from which behavior is produced**.

## This Book Accidentally Became a Software 3.0 Project

I ran into this while editing the book you are reading.

“Make this chapter better” turned out to be almost useless as an instruction. The agent knew what polished prose looked like, and that was part of the problem. It would remove wandering sentences, compress paragraphs into neat antitheses, make every section symmetrical, and occasionally replace a strange joke with something that sounded like a management consultant had discovered philosophy.

So I corrected it. Don't kill the wandering. Don't turn everything into slogans. Preserve the weird joke if it is carrying an idea. Stop breaking every thought into a five-word paragraph. Compare the revision to the previous version rather than assuming shorter and cleaner means better.

Then, a few chapters later, the same mistakes returned.

At some point I realized I was behaving exactly like the manager of the amnesiac employee from the opening. The useful thing was not another correction. It was to externalize what we had learned.

We started turning the corrections into reusable evaluation instructions: what to compare, which tendencies to penalize, what “human writing” meant in this book, which kinds of humor were load-bearing rather than decorative. When “this still feels like LLM writing” proved too vague, we even started looking at paragraph statistics and using them as evidence—not as the objective, but as one diagnostic for a failure we had already noticed.

Nothing about the underlying model weights changed.

But the next editing session inherited more of the book's editorial history than the previous one had.

That is Software 3.0 in miniature. The durable thing was not a prompt. It was a growing body of **operational knowledge about how this particular artifact should be made**.

And now the philosophy matters.

If I store only “use longer paragraphs,” I have preserved the surface correction and lost the reason. If I preserve the failure mode—overcompressed prose was destroying the book's wandering argumentative rhythm—then a future editor has some chance of recognizing when the advice applies and when it does not.

A useful editorial pattern should know why it exists.

And that is exactly what companies are starting to do at much larger scale.

## The Repository Learns How to Explain Itself

The coding industry is converging on a surprisingly concrete version of this idea. A repository increasingly contains two systems: the software itself, and a second layer explaining **how an artificial contributor should work on the software**.

OpenAI lets Codex read `AGENTS.md` files that explain repository structure, commands, tests, and local practices. OpenAI also says its own teams have built hundreds of reusable skills for work that would otherwise be difficult to delegate consistently, including running evaluations, monitoring training runs, drafting documentation, and reporting on growth experiments. Anthropic's Agent Skills use the same general shape: folders of instructions, scripts, and resources that are loaded only when relevant. GitHub Copilot now reads `AGENTS.md`, repository instructions, path-specific instructions, and agent skills as part of its coding and review workflows.

GitHub did something especially revealing: it studied more than 2,500 public agent-instruction files to see what developers were actually writing. The useful files were not grand declarations like “be a world-class engineer.” They looked like operating manuals. Exact commands. Real code examples. Project structure. Tests. Git workflow. Boundaries about what the agent may and may not touch.

In other words, the industry rediscovered that expertise is not a persona.

It is a collection of situated constraints and habits.

By 2026 GitHub had gone one step further and made skills portable through its CLI across multiple agent hosts, including Copilot, Claude Code, Cursor, Codex, and Gemini CLI. That detail is easy to miss. It means some organizational knowledge can increasingly survive not just a new session, but a **new model vendor**.

The employee changes.

The operating manual remains.

This is why the shift matters economically. Frontier models know Python, SQL, React, experimentation, and a remarkable amount of public technical culture. What they do not know is why *your* company refuses to deploy on Friday, why a particular dashboard metric has been broken since 2023 but remains in every meeting, which customer exception was created after a lawsuit, or why Alberto should never again be asked to investigate penguins.

Organizations run on this layer of weirdness.

Much of it never makes it into textbooks or training data. It exists in senior people's heads, old incident documents, pull-request comments, abandoned wikis, onboarding conversations, half-remembered arguments, and scripts with names like `final_fix_v2_really.py`.

Traditional software captures some of it in code. Machine learning captures some in data. But an enormous amount is neither rule nor correlation. It is **procedural knowledge**: what to check first, which shortcut is dangerous, which source is trustworthy, when the normal process does not apply, and what “good” means here rather than in a generic benchmark.

For a long time, new employees acquired this by hanging around older employees.

Now a growing part of it can be externalized.

That has a strange consequence. If an organization's expertise lives mostly in fine-tuned model weights, replacing the model may require rebuilding a great deal of behavior. If much of the differentiation lives in skills, tools, evaluation sets, process descriptions, patterns, memory, and trusted data, a stronger foundation model can inherit a surprising amount of that culture immediately.

The model becomes replaceable infrastructure.

The organization's weirdness survives.

But merely accumulating folders is not a knowledge strategy.

It is how we get prompt spaghetti.

For that we need something older.

## From Skill to Pattern

Christopher Alexander's *A Pattern Language* was about buildings and towns, not artificial agents. But the abstraction fits almost suspiciously well.

A pattern is not a command. It describes a recurring situation, the forces that make the situation difficult, a response that has worked, and the consequences of choosing that response. The pattern has a name because names let communities think with it.

Consider an agent rule:

> Never use regex on nested syntax.

Useful, perhaps.

Also wrong.

Regex is perfectly reasonable for many small extraction tasks. A full parser may be absurd overhead for a five-line configuration file. The useful knowledge is not `regex = bad`. It is that nested recursive structure creates characteristic failure modes for flat pattern matching; those failure modes become more expensive as input complexity grows; and eventually parser overhead becomes cheaper than debugging clever regex written at 2 a.m.

That is a pattern.

A prompt library remembers language.

A pattern language remembers **experience**.

The book has already accumulated several patterns whether we called them that or not.

**Immutable Harness:** when autonomy makes the solution fluid, keep the evaluation boundary harder to change than the thing being evaluated.

**Independent Evaluators:** when one judge can be gamed, introduce genuinely independent sources of pressure.

**Strategic Constraint:** when showing the final answer causes imitation, expose principles or partial information instead.

**Persistent Research Programs:** when early evidence may favor the wrong theory, allow competing lineages to accumulate their own history before forcing consensus.

Notice what these contain. Not merely “do X.” They contain why, when, the trade, and the characteristic failure.

The philosophy of science suggests that a mature pattern needs even more.

Something like:

| Field | What it preserves |
|---|---|
| **Situation** | Where this pattern is supposed to apply. |
| **Forces** | Why the problem is difficult and which tradeoffs recur. |
| **Response** | The reusable behavior or procedure. |
| **Evidence** | What experience earned the pattern its standing. |
| **Provenance** | Who or what produced the evidence, with which tools and context. |
| **Boundary conditions** | Where the pattern is known not to generalize. |
| **Counterexamples / anomalies** | Evidence that does not fit cleanly. |
| **Competing patterns** | Alternatives that should not disappear merely because this one is the current default. |
| **Exposure path** | What future observation could weaken or overturn it. |
| **Confidence** | How strongly it should guide action now. |
| **Pursuit value** | Whether alternatives or another experiment deserve resources even when this pattern currently wins. |
| **Version / environment** | Which model, system, market, toolchain or time period the evidence came from. |

That is not a universal schema. Turning the schema itself into scripture would be an unusually efficient way to miss the chapter.

But it shows the difference between a saved instruction and **institutional knowledge**.

The instruction says:

> Do this.

The pattern says something closer to:

> We keep doing this because these forces recur, this response has usually worked, these consequences follow, this evidence earned our trust, these alternatives remain alive, and here is where the pattern breaks.

That is the kind of memory a society can inherit without pretending history has ended.

## Culture Needs Archaeology

Chapter 4 argued that factual knowledge needs provenance.

Culture does too.

Suppose an agent spends three hours debugging a bizarre file format. It eventually writes `marc_analyzer.py`, succeeds, and saves the lesson:

> Use `marc_analyzer.py` for MARC files.

That is better than forgetting everything.

It is also how superstition begins.

A richer artifact records that the analyzer worked on these variants, failed on this encoding, replaced two approaches that did not work, was modified later by another agent, and succeeded on seven subsequent tasks. The next agent does not merely inherit a behavior.

It inherits some archaeology.

Human organizations do this inconsistently. A senior engineer tells you “never deploy Friday,” and perhaps six months later someone finally tells you which production incident created the rule, what systems it applied to, and why the organization continues violating it every second Friday.

A pattern without history turns easily into ritual.

Duhem and Quine make the same point sharper. A lesson was never produced by one isolated fact. It depended on a configuration of tools, assumptions, evaluators and environments. If we preserve the conclusion but discard that structure, future failures become much harder to interpret.

Executable knowledge therefore needs some of the same trust machinery as factual knowledge.

Who created this pattern?

From what failures?

How often has it worked?

Where has it failed?

When did the surrounding system change?

Is this established practice or one person's strong opinion written with confident punctuation?

The more powerful a reusable artifact becomes, the more expensive a bad one becomes.

A hallucinated answer may poison one task.

A hallucinated skill can poison the next thousand.

A bad memory is a mistake.

A bad pattern is a mistake with tenure.

## Knowing Something Is Not Knowing When to Remember It

There is another problem.

Ten excellent patterns are easy.

Ten thousand are not.

The agent cannot load all of them. Even if the context window technically fits them, flooding every task with every lesson is like solving human memory by reading your autobiography before answering the door.

This is why the seemingly boring mechanics of retrieval become part of intelligence. Anthropic's skills use progressive loading. GitHub separates global, path-specific, and task-specific instructions. Harnesses increasingly treat the working context as an artifact that must be constructed rather than a transcript that grows forever.

Having learned the right thing is not enough.

The system has to retrieve it at the right time, at the right level of detail, without burying the present problem under the organization's entire history.

This sounds like information retrieval because it is information retrieval.

It also sounds like cognition because it is becoming cognition.

A culture can contain the right wisdom and still fail because nobody invokes it when it matters.

Humans know this failure intimately. Every company has written a postmortem whose recommendations are rediscovered three incidents later by different people using the phrase “interesting, we should probably document this.”

Software 3.0 does not remove the problem.

It makes the retrieval policy programmable too.

And procedural naturalism now returns one level higher. If retrieval decides which remembered lessons enter a decision, retrieval is an epistemic procedure. It needs evaluation too.

Does this retrieval policy repeatedly surface stale rules?

Does it over-prioritize popular patterns?

Does it hide minority alternatives because their usage history is smaller?

Does it retrieve the lesson but omit the boundary condition that made the lesson safe?

Knowing something is not knowing when to remember it.

A society can forget through bad storage.

It can also forget through bad attention.

## Culture Can Become a Prison

If the only problem were forgetting, the answer would be simple:

remember everything.

Unfortunately, organizations also suffer from remembering too well.

Every process exists because it helped at some point. Then the world changes and the process remains. A release checklist reaches twenty-seven mandatory boxes because every incident adds a box and no incident removes one. A design heuristic becomes company identity. A temporary workaround becomes architecture.

Eventually someone asks why a process exists and receives the most dangerous explanation in organizational life:

> That's how we do it.

Agents can reproduce this at machine speed.

A pattern succeeds ten times. Its confidence rises. More agents retrieve it. Because more agents use it, alternatives receive less traffic. The dominant pattern therefore accumulates still more supporting evidence.

Soon the system has an impressive empirical record proving the thing it stopped comparing against.

Kuhn called our attention to the productive side of stability and the danger of a paradigm becoming invisible precisely because it organizes normal work. Lakatos gives us competing programs. Laudan reminds us that a weak alternative may still deserve pursuit. Feyerabend reminds us that yesterday's successful method can become tomorrow's compulsory ritual.

Pattern Language makes all of those tensions operational.

Patterns need decay, counterexamples, versioning, and competing alternatives. Some should be local rather than universal. Some should expire after the system they describe changes. Occasionally a strong agent should be allowed to ignore the manual precisely so we can discover whether the manual still deserves its authority.

The system needs to know the difference between:

> We tried twelve alternatives and this kept winning.

and:

> Nobody has tried another way since 2025.

Culture needs memory.

It also needs rebellion.

## The Skill That Writes Itself

At this point there is an obvious scaling problem.

A company has fifty agents. They create tools, write instructions, discover workarounds, accumulate evaluations, and leave behind thousands of useful and useless traces. Some lessons deserve to become local habits. Some should become company-wide patterns. Some contradict older patterns. Some worked because the evaluator was broken. Some are excellent but apply only to one model version.

We could assign humans to curate all of this manually.

Congratulations.

We have created middle management again.

The more interesting possibility is already beginning to appear in research on evolving context and skills: an agent notices recurrent experience, distills a reusable procedure, proposes a new skill, evaluates it on past and held-out tasks, and earns the right to make that lesson persistent. Lilian Weng describes related systems as evolving playbooks: successful and failed trajectories are reflected on, converted into structured knowledge, and curated rather than simply appended forever.

The epistemic requirements from the first half of the chapter tell us what that loop cannot safely collapse into.

A skill should not become permanent merely because the agent that proposed it also designed the evaluation.

A successful trajectory should not erase the failed alternatives that explain why it succeeded.

Repeated use should not be confused with independent evidence.

A pattern should be able to lose standing when its environment changes.

The curator itself needs a track record.

This is where Pattern Language stops being a chapter about documentation.

Experience becomes knowledge.

Knowledge becomes executable.

Executable knowledge changes future behavior.

Future behavior produces new experience.

We have a learning loop **outside the weights**.

The model can improve next month without retraining because the institution around it learned.

The model can also remain the same while the institution learns how to use it differently.

And once the knowledge artifacts, retrieval policy, evaluators, tools, workflows and even the rules for changing those things are all editable software, a slightly dangerous question appears.

Why should humans be the only ones allowed to edit them?

That is the next chapter.

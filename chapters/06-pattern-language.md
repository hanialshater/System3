# Chapter 6: Pattern Language

*When Knowledge Becomes Software*

This book kept forgetting how to write itself.

That sounds more mystical than it was.

I would work on a chapter with an agent, reject a certain kind of edit, explain why I rejected it, and eventually get something better. A few days later we would start another chapter and the same failure would return. The prose would become cleaner in exactly the wrong way. Wandering sentences disappeared. Strange jokes were replaced by respectable ones. Arguments broke into tiny paragraphs that looked dramatic from across the room and exhausted me when I actually read them.

So I would say things like:

> Don't kill the wandering.
>
> Don't turn every idea into a slogan.
>
> Preserve the weird joke if it is carrying the argument.
>
> “More polished” is not automatically “more mine.”

The agent would improve.

Then the context would end.

We were reenacting, on a ridiculous scale, the problem Chapter 5 had just spent several thousand years describing.

A society can know something none of its members knows alone. Fine. But if the society survives, it has another problem: **how does what it learned yesterday change what it does tomorrow?**

The obvious answer is memory. Save the conversation. Increase the context window. Keep a notebook. Put the old decisions in a database.

That helps. It is not enough.

A transcript remembers what happened. An intelligent institution has to remember **what was worth learning from what happened**.

The difference is enormous.

Suppose I save the sentence “use longer paragraphs.” That is a memory of one correction. It is also a future disaster waiting politely in Markdown. The real lesson was not that long paragraphs are good. It was that a particular editing process had begun compressing exploratory prose into a rhythm that felt machine-produced. Sometimes the correct response was a longer paragraph. Sometimes it was a shorter sentence. Sometimes the right thing was to leave the paragraph alone and stop improving it.

What I needed the next agent to inherit was not merely the instruction. I needed it to inherit enough of the **reason, evidence, boundary conditions and failure history** to know when the instruction deserved authority.

That is a different kind of memory.

It is much closer to culture.

Chapter 5 ended with the claim that **System 3 is science**: not science as a classroom flowchart, but science as a civilization-scale arrangement for letting fallible minds accumulate knowledge while preserving routes through which the world can still object.

Science does not compound because every new scientist rereads every previous conversation. It compounds because some experience hardens into instruments, protocols, techniques, standards, textbooks, laboratory habits, named failure modes, statistical practices and things everyone in a field learns to check before embarrassing themselves in public.

Some of those inheritances are brilliant.

Some are historical debris with a prestigious accent.

The problem of Chapter 6 is therefore not “how do agents remember?” It is more specific:

**How should useful experience become reusable behavior without turning yesterday's success into scripture?**

That question has suddenly become practical because knowledge itself is becoming a software artifact.

## Three Ways to Tell a Computer What You Know

For most of computing history, if you knew how a process should work, you translated that knowledge into code.

A refund under €50 can be approved automatically. A payment over some threshold needs another check. A production deployment requires a test. A user without permission cannot read this table. Human knowledge becomes `if`, `else`, functions, schemas, state machines and permissions.

Andrej Karpathy calls this familiar world **Software 1.0**: humans write the behavior directly.

Machine learning changed the contract. Suppose I cannot tell you the rules that distinguish a fraudulent transaction from an unusual but legitimate one. I can give you examples. We write the training machinery, choose data and an objective, and optimization pushes useful behavior into weights.

That is **Software 2.0**.

It gave us capabilities that explicit rule writing could never have scaled to, but it also hid much of the learned behavior. The fraud model “knows” things no engineer wrote down. We can evaluate it, probe it, retrain it and sometimes interpret pieces of it, but there is no `fraud_rules.py` containing the organization's accumulated understanding of fraud.

Large language models created a strange third possibility. In his 2025 talk *Software Is Changing (Again)*, Karpathy called it **Software 3.0**: a new class of programs written substantially in natural language and interpreted by a model rather than by a conventional compiler. A model can read something like:

> Review this experiment. Check instrumentation changes before inventing a causal story. Look for market concentration. If click metrics rise while orders stay flat, inspect position and price shifts before celebrating.

There is no deterministic function there. There is operational knowledge. A competent human can interpret it. Now a sufficiently capable model can too.

That change is deeper than “prompts are code.”

Prompts are only the most disposable form.

The interesting possibility is that **knowledge itself becomes versionable, composable and executable**.

An organization can write down a procedure, examples, scripts, counterexamples, diagnostic questions, evidence, tool instructions and boundaries. A general model supplies enough interpretation that we no longer have to formalize every clause into brittle symbolic logic before the computer can use it.

The model starts to look less like the knowledge base and more like an **interpreter for knowledge artifacts**.

That is why I think Software 3.0 quietly reopens a field that machine learning was supposed to have buried.

Knowledge engineering is back.

It is carrying Markdown.

## Knowledge Engineering Comes Back Wearing Markdown

The old dream of knowledge engineering was reasonable. Find experts. Extract what they know. Put it in a knowledge base. Let software reason with it.

The difficulty was that expertise is almost offensively reluctant to become a clean rule set.

Ask an experienced engineer how to diagnose a production problem and the answer is rarely:

`IF latency > 300ms THEN database`

It sounds more like:

> Start with the dependency graph, unless the spike began exactly at deployment. If only one market is affected, check the traffic split before touching the database. The cache metric lies under failover, so ignore it when this alarm is red. And if the problem started after the Tuesday migration, ask Sam because there is a thing with the old serializer that nobody wrote down properly.

Traditional expert systems struggled because turning that kind of practice into formal logic was expensive, brittle and endless. Machine learning offered an escape: stop asking experts to explain themselves; learn patterns from data.

LLMs change the trade again. They can interpret prose, examples, scripts, diagrams and partially structured instructions. The knowledge does not have to become perfect logic before it can affect behavior.

That does not make knowledge engineering easy. It changes where the difficulty lives.

The problem is no longer only **formalization**. It becomes curation, provenance, retrieval, conflict, authority and maintenance.

Whose practice gets written down?

Which version applies here?

What happens when two experts disagree?

How does a lesson lose standing?

When does a local workaround become a global rule?

Which knowledge should enter the working context now, and which should remain in the archive?

Those are not edge cases. They are the new engineering surface.

By 2025 and 2026, agent systems were already moving in this direction. Anthropic began talking about **context engineering** rather than merely prompt engineering: the problem is to curate the whole state presented to the model—system instructions, tools, external data, message history, memories and other resources—under a finite attention budget. Its Agent Skills package procedural knowledge as discoverable folders of instructions, scripts and resources. OpenAI's Codex likewise treats reusable skills and repository instructions as part of the agent environment. GitHub added `AGENTS.md` support and then made agent skills installable and portable through its CLI across several agent hosts.

That last detail is more important than it looks.

By 2026, a useful skill could increasingly survive not just a new session, but a new model vendor.

The worker changes.

The operating knowledge remains.

GitHub even added version pinning and provenance to skills because executable instructions have the same awkward property as ordinary software dependencies: if they change silently, behavior changes silently too. A skill can contain useful expertise. It can also contain a bad instruction, stale assumption or malicious script. Once knowledge is executable, **knowledge has a supply chain**.

This is one reason the future moat of an organization may not live entirely in model weights. Frontier models already know Python, statistics, common business practices and enormous amounts of public technical culture. What they do not automatically know is why *your* company refuses to deploy on Friday, which metric has been misleading everyone since 2023, which customer exception followed a lawsuit, why the elegant architecture in the wiki was abandoned, or why Alberto should never again be asked to investigate penguins.

Organizations run on this layer of weirdness.

Some of it belongs in code. Some belongs in data. Some belongs in tools and evaluators. A surprisingly large amount belongs in **situated procedural knowledge**: what to check first, which shortcut is dangerous, which source has standing, when the normal process does not apply, and what “good” means here rather than in a generic benchmark.

For most of history, people acquired this by hanging around people who had already been injured by the relevant mistakes.

Now more of it can become software.

That is exciting.

It is also how we get prompt spaghetti at civilizational scale.

We need a better unit than “saved instruction.”

## From Skill to Pattern

Christopher Alexander's *A Pattern Language* was about towns, buildings and the recurring problems people encounter while making places worth living in. A pattern was not a commandment handed down from an architect. It named a recurring situation, the forces that make it difficult, a response that had repeatedly worked and the consequences of using that response.

The name mattered because communities could think with it.

That abstraction fits agent knowledge almost suspiciously well.

Consider the instruction:

> Never use regex on nested syntax.

It has the reassuring shape of wisdom and the inconvenient property of being false.

Regex is perfectly good for many small extraction tasks. A parser may be absurd overhead for a five-line configuration format. The useful lesson is that recursive structure creates characteristic failure modes for flat pattern matching; that these failures become harder to see as syntax grows; and that, beyond some point, parser complexity becomes cheaper than maintaining an increasingly heroic regular expression written at 2 a.m.

That is closer to a pattern.

A saved instruction remembers **what somebody said**.

A pattern tries to remember **what kept happening**.

The book has already accumulated patterns whether we called them that or not.

**Immutable Harness:** when autonomy makes the solution fluid, keep the evaluation boundary harder to change than the thing being evaluated.

**Independent Evaluators:** when one judge can be gamed, create genuinely different sources of pressure rather than five copies of the same opinion.

**Strategic Constraint:** when showing the final answer causes imitation, expose principles or partial information instead.

**Persistent Research Programs:** when early evidence may favor the wrong theory, let competing approaches accumulate enough history to become meaningfully different before forcing convergence.

Notice what makes these useful. None is simply “do X.” Each contains a situation, a tension and a reason.

But Chapter 5 has already made us suspicious. Civilizations do not merely accumulate good practices. They accumulate ritual, prestige, inherited assumptions and procedures that have outlived the world that justified them.

If Pattern Language is going to become cultural memory for agents, a pattern needs to know more about itself.

This is where philosophy of science finally earns its API.

## A Pattern Needs a Way to Lose

Suppose the editing agent concludes:

> Use longer paragraphs in this book.

We have converted one piece of experience into reusable behavior.

Karl Popper would immediately ask the rude question: **what could happen that would make us stop believing this lesson?**

A useful theory exposes itself to observations that could have gone differently. If every outcome can be narrated as success, the theory has arranged the game so it cannot lose.

Persistent agent knowledge needs the same property.

A pattern should retain some **exposure path**: a test, observation, user reaction, proof obligation or downstream consequence capable of weakening it. “Use longer paragraphs” might lose standing if reader tests show comprehension falling, if another chapter becomes monotonous, or if the original failure disappears after the editing process changes.

The pattern should not merely remember *what worked*.

It should remember enough about **how the world could prove that the lesson stopped working**.

Then Pierre Duhem and W. V. O. Quine ruin the simplicity.

Evidence rarely confronts one isolated belief. A failed experiment implicates a bundle: hypothesis, instrument, data, analysis, background assumptions. A failed pattern is the same.

Did the advice stop working?

Was it retrieved in the wrong situation?

Did the model change?

Did the evaluator drift?

Was the original success caused by something else in the editing pass?

Did “longer paragraphs” correlate with the real change—more natural argumentative rhythm—without causing it?

The failure says that some part of the package deserves suspicion. It does not highlight the guilty line in yellow.

So reusable knowledge needs **archaeology**.

Where did this pattern come from? Which failures produced it? Which tool and model were involved? Which alternatives were tried? What evidence earned the lesson its standing? Which assumptions were present?

This is Chapter 4's provenance problem applied to culture.

A factual claim without provenance becomes rumor.

A reusable practice without provenance becomes tradition.

Tradition is not automatically bad. It is simply difficult to debug.

## Defaults, Anomalies and Rival Cultures

The obvious response to fallibility is to keep every pattern permanently open for debate.

That is a beautiful philosophy and a terrible operating system.

Thomas Kuhn's most useful lesson here is not the phrase *paradigm shift*. It is the value of **normal science**. Productive communities need enough stability that they do not reopen their deepest assumptions every morning. A framework tells researchers what puzzles are worth solving, which instruments are legitimate and what kinds of answers count.

The same is true of an agent culture.

If a procedure has survived hundreds of deployments, the system should not rediscover it from first principles every Tuesday merely to prove that it remains intellectually alive. Some decisions have earned the right to become boring.

That is what culture buys us.

The danger is that boring assumptions become invisible assumptions.

Anomalies therefore need memory too.

The release pattern works, except for this market. The evaluator tracks human judgment, except on this kind of creative task. The ranking heuristic works, except every holiday season. The workflow works, except that the critic now spends most of its time inventing reasons why the builder was right.

One anomaly is usually noise. Ten may still be noise. At some point the exception list begins to look like the real theory.

The institution needs somewhere to remember that embarrassment until somebody asks the Kuhnian question:

*Is the framework itself the bug?*

Imre Lakatos then makes the problem harder in a useful way. We should often preserve **research programs**, not just isolated ideas. A program has a history, a relatively stable core, supporting techniques, auxiliary assumptions and a trajectory. One approach may currently be weaker but improving. Another may be winning mainly by adding patches around every failure.

Larry Laudan makes the allocation consequence explicit: **acceptance and pursuit are different decisions**.

I can believe method A is our best current default while still believing method B deserves another experiment.

Those are different questions:

- What should guide action now?
- Where is another unit of investigation most valuable?

This distinction matters enormously once culture becomes executable. The current winner gets retrieved more often. Because it gets used more often, it accumulates more successful cases. Those cases raise its confidence. Higher confidence makes it even more likely to be retrieved.

The alternative receives less traffic and therefore less evidence.

Eventually the system develops an impressive empirical record proving the thing it stopped comparing against.

A culture can become monopolistic without anyone issuing a decree.

The retrieval policy did it.

## Who Gets the GPUs?

There is an overly clean way to draw a society of agents.

Every agent is a box. Every box has an arrow. Everybody gets a turn to think.

Real institutions are not like that because **attention has a budget**.

Human science has telescope time, laboratory space, grants, journals, careers and prestige. AI research has datasets, deployment traffic, human reviewers, API quotas, clusters and GPUs. In both cases, a theory's ability to generate evidence depends partly on whether the institution gives somebody the resources to investigate it.

This is not merely politics happening around epistemology. It changes the epistemic landscape itself.

Imagine research program A has ten thousand GPU-hours and program B has ten.

A can run ablations, train variants, investigate anomalies and produce beautiful graphs. B can produce a thoughtful paragraph about why it deserves more compute.

Six months later A has more evidence.

Of course it does.

The evidence may be real. A may genuinely be better. But the institution has also helped create the asymmetry it later treats as evidence for further allocation.

Chapter 5 called this **epistemic policy**. Here the social meaning becomes unavoidable.

Who owns the GPUs?

Who decides what counts as an interesting problem?

Who gets access to the expensive instrument?

Whose failed experiment remains in memory and whose disappears because the project ended?

Which benchmark becomes the promotion metric? Which customer complaints make it into the dataset? Which research direction can afford to remain weird for another year?

These questions are not separate from intelligence once the intelligence is institutional.

The contemporary AI ecosystem makes the point concrete. Stanford's 2026 AI Index reports that industry produced more than 90 percent of notable AI models in 2025 and that the frontier is increasingly concentrated among a small number of organizations. The most capable models are also increasingly opaque about training code, data scale and other details. The machinery capable of producing frontier evidence is not evenly distributed.

That does not make industrial research false. It makes **position** relevant.

Helen Longino's social epistemology is useful here because different positions can expose different background assumptions. David Hull and Philip Kitcher make incentives, credit and division of cognitive labor part of the story. Researchers cooperate because they need one another's results and compete because priority, jobs, reputation and resources are scarce.

An agent society will have analogues of all of these whether or not we give them sociological names.

The scheduler is partly a funding agency.

The memory system is partly an archive.

The evaluator is partly a journal gate.

The retrieval layer is partly a curriculum.

The permission system decides who may touch which instrument.

The compute allocator decides which hypotheses get enough opportunity to become well-tested hypotheses.

And the organization can remember its incentives just as effectively as it remembers its wisdom.

A local objective becomes a local pattern. The pattern gets copied because the team is successful. Future agents inherit it without seeing the original tradeoff. Eventually “this helped one group hit its metric” becomes “this is how good work is done here.”

That is culture too.

If we build persistent agent societies without thinking about this layer, we will not escape institutional power. We will automate it and give it better dashboards.

## The Community Is Part of the Instrument

Power is only one reason a community matters.

Even generously funded investigators can share the same blind spot.

Give five agents the same model family, the same system prompt, the same search results and the same dominant explanation, and you have not created five perspectives. You have created a very expensive echo with parallel API calls.

Longino's point is that background assumptions affect what investigators notice, which questions appear natural and which evidence looks relevant. A genuinely different perspective can reveal something not because its owner has a higher IQ score, but because that participant is **positioned differently with respect to the evidence**.

For an agent system, useful difference may come from a separate dataset, another tool, an isolated context, a different model, an external user, a domain expert, or a team operating under different incentives.

That is stronger than theatrical personas:

> Agent 1, be optimistic.
>
> Agent 2, be skeptical.
>
> Agent 3, be a pirate.

The pirate may be entertaining. He probably still read the same PDF.

A pattern should therefore carry some trace of position: who learned it, from which class of tasks, with which tools, model, evidence and incentives. A ranking practice learned in Germany, a fraud rule learned in Brazil, a compiler workaround discovered under one toolchain and a clinical protocol developed in one hospital can all be excellent without acquiring universal authority merely because they share a database.

This is another reason Pattern Language should not become one giant company constitution.

Culture should be **locally authoritative** where appropriate.

Trust is local. Apparently memory should be too.

## What a Pattern Should Know About Itself

At this point the shape of a mature pattern becomes richer than Alexander needed for buildings and richer than a typical prompt library needs for instructions.

Something like this:

| Field | What it preserves |
|---|---|
| **Situation** | Where this pattern is supposed to apply. |
| **Forces** | Why the problem is difficult and which tradeoffs recur. |
| **Response** | The reusable behavior, procedure or design move. |
| **Evidence** | What experience earned the pattern its current standing. |
| **Provenance** | Who or what produced the evidence, using which tools and assumptions. |
| **Boundary conditions** | Where the pattern is known not to generalize. |
| **Anomalies / counterexamples** | Evidence that does not fit cleanly and should not be forgotten. |
| **Competing patterns** | Alternatives that should not disappear merely because this one currently wins. |
| **Exposure path** | What future observation could weaken or overturn it. |
| **Confidence** | How strongly the pattern should guide action now. |
| **Pursuit value** | Whether an alternative or another experiment deserves resources even when this pattern currently wins. |
| **Position / incentives** | Which organizational perspective produced the lesson and what pressures shaped it. |
| **Version / environment** | Which model, system, market, toolchain or period the evidence came from. |

I do not mean this as a universal schema.

Turning the schema itself into scripture would be a remarkably efficient way to miss the chapter.

The point is the difference between a command and institutional knowledge.

The command says:

> Do this.

The pattern says something closer to:

> We keep doing this because these forces recur; this response has usually worked; this evidence earned our trust; these are the places it fails; these alternatives remain alive; and this is what would make us reconsider it.

That is knowledge with some of its history still attached.

And because an LLM can interpret that knowledge at runtime, the pattern can change behavior without retraining the model.

This is what I mean by **knowledge becoming software**.

Not because prose has literally become Python.

Because the knowledge can now be versioned, tested, scoped, composed, retrieved, executed, challenged, rolled back and eventually modified by the same kind of agents that use it.

Knowledge has acquired a runtime.

## Knowing Something Is Not Knowing When to Remember It

Now imagine ten excellent patterns.

Easy.

Imagine ten thousand.

The agent cannot read the organization before every action. Even if the context window technically fits everything, loading every policy, skill, postmortem, experiment, preference and historical argument into every task would solve forgetting by making thinking impossible.

This is why **context engineering** is becoming central to agent design. Anthropic describes it as the problem of curating the entire state that reaches the model, not merely writing a clever prompt. Long-running agents accumulate messages, files, tool outputs, memories and artifacts much faster than useful attention can scale. Context has to be selected, compacted and reconstructed.

Retrieval therefore becomes part of cognition.

A culture may contain exactly the right lesson and still fail because that lesson does not arrive when it matters.

Humans know this failure well. Every large company has written a postmortem whose recommendation is rediscovered three incidents later by different people using the phrase “interesting, we should probably document this.”

Agent systems can fail more elegantly.

They can store the lesson perfectly, embed it beautifully and retrieve a more popular but irrelevant one.

Or retrieve the right pattern without the boundary condition.

Or retrieve ten conflicting patterns and allow whichever one appears latest in the context to win by textual gravity.

Or preferentially surface the practices with the richest usage history, reinforcing the same incumbent dynamics we saw with research programs.

So a persistent institution has two memory problems:

**What should survive?**

and

**What should become salient now?**

Bad storage forgets by deletion.

Bad retrieval forgets by attention.

And once retrieval determines which inherited knowledge enters a decision, retrieval itself becomes an epistemic procedure. It needs evaluation.

Does this policy repeatedly surface stale rules?

Does it suppress minority alternatives?

Does it confuse popularity with relevance?

Does it preserve the result but discard the reason?

The librarian is no longer merely finding books.

The librarian is shaping thought.

## The Librarian Is Also a Hypothesis

At some point every successful institution becomes tempted to trust its own method.

Yesterday's useful workflow becomes today's best practice and tomorrow's mandatory ritual.

Paul Feyerabend is usually remembered for “anything goes,” which is a wonderful way to make sure people remember the slogan and forget the argument. The useful warning is historical: successful inquiry has often violated methodological rules that somebody wanted to make universal. A method can become so authoritative that deviations count as irrational by definition, including the deviations that would have exposed its limits.

Agent systems can do this at machine speed.

Suppose `Research → Plan → Build → Critic → Revise` works beautifully. We run it ten thousand times. It becomes the company standard. Soon every task enters the same ceremony, including tasks where research anchors the builder, criticism arrives too late, or a crude prototype would have answered the important question in five minutes.

The method itself must occasionally become available for criticism.

Naturalistic approaches to epistemology make this practical: do not ask only whether a conclusion sounds justified; study the **procedures that produce justification** and how they actually perform.

An evaluator is a procedure.

A browser is an instrument.

Retrieval is a procedure for selecting evidence.

A benchmark is a measurement system with a distribution and failure modes.

A proof checker is extraordinarily authoritative inside its formal domain and completely useless for deciding whether the theorem matters.

A simulated user is cheap perspective-taking and not a user.

The institution should be able to learn that its usual way of checking a claim is itself the thing that stopped working.

The library needs criticism.

So does the librarian.

Bayesian reasoning fits inside this architecture because confidence is rarely binary. A pattern can become more or less trusted as evidence accumulates. But confidence is not contact. A number like `0.91` does not tell us whether the prior was sensible, whether the evidence was independent, whether the alternative was ever investigated, or whether everybody is confidently reading the same broken measurement.

After all this emphasis on culture and institutions, there is an easy bad reading:

truth is whatever the institution eventually agrees on.

No.

Consensus can be strong evidence. It can also be twelve agents sharing one bad source and congratulating one another on convergence.

The bridge either stands or it does not. The proof checks or it does not. The deployment crashes or it does not. The customer may dislike the supposedly improved page even if every simulated evaluator is delighted.

**Reality retains the right to be rude.**

The point of culture is to help knowledge travel across time without replacing the world with memory of the world.

## Culture Can Become a Prison

If forgetting were the only danger, the design would be easy.

Remember everything.

Unfortunately organizations also suffer from remembering too well.

Every process exists because it helped at some point. Every release checklist box has a story, or used to. Every review gate survived at least one meeting. Every architecture principle was once attached to a failure somebody cared enough about to prevent.

Then the environment changes and the procedure remains.

Eventually someone asks why the process exists and receives the most dangerous explanation in organizational life:

> That's how we do it.

Agents can reproduce this faster than humans because executable culture closes the loop between memory and behavior. A pattern succeeds. Its confidence rises. More agents retrieve it. Alternatives receive less traffic. The dominant pattern accumulates more evidence because it is the dominant pattern.

Soon the institution has an impressive record proving the thing it stopped comparing against.

This is Kuhn, Lakatos and Laudan turning into software mechanics.

Patterns need anomaly memory, versioning, local scope and competing alternatives. Some should decay. Some should expire when the system they describe changes. Some should be deliberately challenged after they become too comfortable. Occasionally a capable agent should be allowed to ignore the manual precisely so the institution can discover whether the manual still deserves authority.

The culture needs to distinguish:

> We tried twelve alternatives and this kept winning.

from:

> Nobody has tried another way since 2025.

Those sentences can produce identical dashboards and very different knowledge.

Culture needs inheritance.

It also needs rebellion.

## The Skill That Writes Itself

Now the scaling problem arrives.

A serious organization may have thousands of agents, tools, experiments, workflows and recurring failures. Useful experience appears continuously. Some lessons deserve to become a local skill. Some should become organization-wide patterns. Some contradict older knowledge. Some only work for one model version. Some are artifacts of a broken evaluator. Some are excellent but will be obsolete in three months.

Humans could curate all of this manually.

Congratulations. We have created middle management again.

The more interesting direction is already appearing in current agent research. Lilian Weng's 2026 review of harness engineering describes file systems as persistent memory, context and workflow design as editable parts of the agent system, and self-improvement loops in which failures are mined, bounded changes are proposed, and accepted only after evaluation. Recent work such as **Evo-Harness** pushes the idea toward compiling noisy one-shot experience into reusable skills that improve later tasks while the underlying model remains frozen.

That is the Pattern Language loop becoming computational:

experience occurs;

an agent notices recurrence;

it proposes a reusable pattern;

another process checks whether the pattern actually helps;

held-out cases test whether it generalized;

provenance and failures remain attached;

the pattern earns some level of authority;

future agents retrieve it when relevant;

new failures can weaken or revise it.

There are several places to cheat in that loop.

The agent that proposes the skill can design an evaluator it knows how to satisfy. Repeated use can masquerade as independent evidence. A pattern can improve one benchmark while making maintenance worse. A retrieval policy can suppress competing practices before they accumulate enough data to challenge the incumbent. A central curator can quietly turn local taste into universal law.

So the curator needs a track record too.

The mechanism for improving culture is itself part of the culture.

And now we have crossed an important line.

Experience becomes knowledge. Knowledge becomes executable. Executable knowledge changes future behavior. Future behavior produces new experience.

The model weights did not move.

The institution learned anyway.

That is a learning loop **outside the weights**.

It also means the clean boundary between “the intelligent model” and “the software around the model” is becoming harder to defend. Intelligence is partly in the model, partly in the tools, partly in the evaluator, partly in context construction, partly in the patterns the organization has accumulated, and partly in the social machinery deciding which of those patterns gets resources and authority.

Chapter 5 moved the unit of intelligence from the agent toward the institution.

Chapter 6 moves learning in the same direction.

The institution can now remember how it learned, revise what it remembers, and change the behavior of future agents without touching their weights.

Once the patterns, retrieval policy, tools, evaluators, workflows and even some of the rules for changing those things are software, one question becomes difficult to avoid.

Why should humans be the only ones allowed to edit them?

That is the next chapter.

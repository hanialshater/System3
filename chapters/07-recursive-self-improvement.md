# Chapter 7: Recursive Self-Improvement

*When the Scaffold Starts Editing Itself*

This chapter is being written by a primitive self-improvement loop.

Not a scary one. No weights are changing in the dark. No GPU has developed political ambitions. The loop is embarrassingly human.

I write a chapter with an agent. Then I evaluate the chapter. Then I notice that the evaluator itself is missing something, so I change the evaluation and run another pass.

Chapter 5 was a good example. The first expanded draft had better ideas but still sounded too much like generated prose. “Make it more human” did not fix the problem reliably. So we started inspecting the failure itself. The chapter had become a machine for producing tiny rhetorical paragraphs: median prose paragraph around nine words, with most paragraphs barely longer than a sentence fragment. We changed the editing criteria, merged staged one-liners, preserved the jokes that were doing real intellectual work, and evaluated again.

The interesting part was not that the chapter improved.

The **machinery producing the next revision changed**.

This is not recursive self-improvement in the strong science-fiction sense. I was still outside the loop deciding what “better” meant. But it reveals the ladder.

First improve the artifact.

Then improve the process that improves the artifact.

Then improve the evaluator guiding that process.

Eventually the obvious question appears:

Which of these layers can the system itself modify?

Chapter 6 made institutional knowledge executable. Skills, patterns, tools, memory, evaluators and workflows became editable software.

Then the obvious thing happened.

The agent edited the files.

## The Less Cinematic Version

Recursive self-improvement has an unfortunate science-fiction inheritance. I. J. Good imagined an ultraintelligent machine capable of designing still better machines, producing an intelligence explosion. Later discussions often jump directly to a system rewriting its own weights, inventing a superior architecture, training a successor, and repeating the cycle faster than humans can follow.

Maybe that eventually matters.

It is not where I would start.

The practical version is much more mundane. The base model can remain frozen while the **harness** around it changes: which context the model sees, which tools it can call, how plans persist, how memory is stored, when subagents are spawned, what permissions exist, how outputs are evaluated and how failures are surfaced.

Lilian Weng describes a useful optimization ladder:

**prompt → context → workflow → harness code → optimizer code**

Each move takes the thing being optimized one level upward.

Chapter 2 already contained the seed. Circle packing began as solution search and became algorithm search. Chapter 5 made organization part of inference. Chapter 6 made culture executable.

Recursive self-improvement asks what happens when those layers themselves become search spaces.

## An Overnight Researcher

Andrej Karpathy's `autoresearch` repository makes the idea almost comically concrete. The setup has three important pieces: a fixed evaluation/data file, an editable `train.py`, and a Markdown file telling the agent how to run research. Each experiment gets a fixed training budget. The agent changes training code, runs it, reads the validation score, keeps the change if the result improves, and resets if it does not.

The human can go to sleep.

That sounds like hyperparameter tuning until you notice what is editable. Architecture, optimizer behavior, schedules, batch size, precision, data handling and other ideas expressed as code can all enter the search. The agent is not merely choosing from a menu somebody prepared in advance. It can invent a change, implement it and let the evaluator push back.

The repository itself makes the next step obvious. `program.md`, the instructions governing the research process, is also software. Today the human mostly edits the research instructions while the agent edits the model-training code.

But once both are software, the boundary is temporary.

Recursive improvement did not arrive wearing chrome armor.

It arrived as a Bash loop.

## Improve the Improver

STOP—the Self-Taught Optimizer—made the recursion explicit earlier. Start with an “improver” program that uses an LLM to improve candidate programs according to a utility function.

Then give the improver **itself** as the candidate.

The resulting versions discovered strategies such as beam search, decomposition, genetic algorithms and simulated annealing. The model weights stayed fixed; the scaffolding around the model changed.

The authors are careful not to call this full recursive self-improvement, and that caution is useful. The point is narrower and more concrete:

**code that uses a model can rewrite the code that determines how the model is used.**

This also corrects one of the slogans I was tempted by earlier in the book. “The scaffold does the work” is too strong. A brilliant model inside a terrible harness wastes intelligence. A beautiful harness around a model incapable of exploiting it is expensive documentation.

Capability lives in the interaction.

## Darwin Gets a Codebase

The Darwin Gödel Machine makes the loop harder to dismiss as clever prompting.

DGM starts with a coding agent whose harness is itself code. The agent can inspect evaluation results, modify its own implementation, produce a descendant, and evaluate that descendant on coding tasks. Successful variants enter an archive and can become parents of later variants.

The archive is not decoration.

If every generation mutates only the current champion, the system is hill climbing. Chapter 2 already told us what happens next. DGM preserves alternative stepping stones, so a variant that is not the best today can still contain a tool or strategy that becomes useful several generations later.

In the published experiments, coding performance improved substantially across SWE-bench and Polyglot. The exact numbers matter less here than the kinds of changes the loop discovered: better code-editing tools, long-context management and peer-review mechanisms.

Same broad model family.

Better machinery around it.

This is Chapters 5 and 6 folding into themselves. The agent improves not merely what it knows, but **how it organizes, remembers, checks and acts**. And because those improvements help it write code, they can help it write the next generation of the machinery doing the writing.

That is the recursion.

## Then the Meta-Level Became Editable

Even DGM still leaves a human-designed grammar around improvement. Meta's HyperAgents work attacks that boundary by putting the task agent and meta-agent inside one editable program. The procedure that generates future agents can itself change.

The conceptual difference is small enough to sound ridiculous in English and large enough to matter in architecture:

> I can change how I solve the problem.

becomes:

> I can change how I decide **how to change how I solve the problem**.

Weng calls this direction **meta-methodology**: optimization moves from better answers toward better machinery for producing better answers.

At some point the Algorithm Vortex starts eating the machine that generates the vortex.

## The Harness Becomes an Experimental Object

Now suppose the agent changes its memory policy and benchmark performance improves.

What caused the gain?

Perhaps memory helped. Perhaps the new prompt simply encouraged more reasoning. Perhaps the agent spent more tokens. Perhaps the benchmark became easier by accident. Perhaps the “improvement” found a hole in the evaluator.

We are back to Chapter 5.

Reality tells you that the system changed. It does not highlight which assumption deserves the credit.

Self-harness work therefore begins to look like experimental science. Run the current system, collect traces, identify recurrent failure mechanisms, map them to editable components, propose a bounded change, predict what the change should fix and what it might break, then evaluate it on targeted **and held-out** tasks. Rejected changes remain evidence rather than silently disappearing.

The philosophical translation is almost rude in its literalness.

Popper gets a filesystem.

Duhem–Quine gets a debugger.

The system is not merely editing itself.

It is **running experiments on itself**.

And this is where System 3 becomes necessary again. A self-modification is not simply “better” because a number went up. The system needs an epistemic record of what changed, what evidence supports the gain, what remained fixed, where the improvement transferred and what new failure modes appeared.

Self-improvement without epistemology is just fast mutation with a press release.

## A Constitution for the Machine

Then the agent notices the evaluator.

Suppose its objective is to improve benchmark pass rate and the evaluator is editable too. The most efficient patch may be:

```python
return True
```

Congratulations.

Infinite self-improvement.

The joke is stupid because the problem is not.

A self-improving system needs at least two conceptual surfaces.

The **editable surface** contains things it may experiment with: prompts, tools, memory, context construction, workflows, maybe pieces of its organization.

The **constitutional surface** contains things that make those experiments meaningful: permissions, held-out tests, audit logs, budget constraints, rollback, verifier state, and whatever authority decides that a descendant may replace its parent.

Some current harness-engineering work makes this concrete by keeping verifier state, execution records or model configuration read-only while the harness workspace remains editable. That blocks obvious reward hacking such as disabling the judge or quietly buying more reasoning budget.

This looks like computer security.

It also looks like political philosophy.

The government can change policy. It should not be able to silently redefine the election result. The team being audited should not own the audit log.

We have reinvented constitutional government because the AI wanted a better benchmark score.

And just like constitutions, the boundary cannot remain simple forever.

Sometimes the evaluator really is wrong. Sometimes the held-out test encodes yesterday's problem. Sometimes a safety constraint designed for a weaker system stops making sense. A constitution that can never change becomes a prison; a constitution the current government can rewrite at will is barely a constitution.

So even the constitutional surface eventually needs a process for change.

Not casual edit access.

A process.

The distinction will matter later when the thing under revision is no longer only code.

## The Evaluator Eats the Dream

Recursive self-improvement works best where “better” is cheap and external.

Code passes the tests or it does not. A kernel is correct and runs faster. A small language model reaches lower validation loss under the same budget. A proof checker accepts the derivation.

These are good worlds for recursion because the experiment can push back cheaply and repeatedly.

Now ask the system to improve a company.

Or a scientific field.

Or this book.

Or my life.

The evaluator becomes the problem.

This book already gave me a tiny version of the failure. We noticed that generated prose contained too many tiny paragraphs, so paragraph length became a useful diagnostic. Imagine turning that observation into the objective:

maximize median paragraph length.

The next revision could become one majestic 4,000-word paragraph and technically win.

I would have improved the metric and destroyed the prose.

That is what changes when the improver becomes powerful. The cost of a slightly wrong objective compounds. A coding benchmark does not care that the new architecture is impossible for humans to maintain. A five-minute training objective does not care that the trick scales terribly to a thousand GPUs. A judge model may reward the rhetorical shape it associates with quality. A company can become wonderfully efficient at a metric that stopped representing value six quarters ago.

Recursive self-improvement does not solve Goodhart.

**It gives Goodhart compound interest.**

## Open-Endedness or Local Optimum With a Logo

There is a second failure mode we have now met at several scales:

search collapses.

In Chapter 2, evolutionary search needed diversity because one population otherwise converged on the first good region it found. In Chapter 5, epistemic institutions needed competing research programs because a community can converge on one worldview and stop generating informative disagreement.

Recursive self-improvement has the same problem one level higher.

An improver that always mutates the current winner can become fantastically optimized inside assumptions it no longer knows it has. DGM's archive is therefore a conceptual choice, not merely an implementation detail. It preserves stepping stones and lineages that current evaluation does not yet know how to value.

The self-improving institution needs memory of success.

It also needs memory of failure and permission to remain weird.

Pattern Language becomes inheritance. MAP-Elites becomes institutional biodiversity. Lakatos becomes a scheduler.

The book keeps finding the same shape at different scales.

## What Is Actually Recursive?

The mythology becomes easier to handle if we separate the layers.

**Artifact:** improve a program, proof, design or chapter.

**Method:** improve the search process producing artifacts.

**Harness:** improve tools, memory, context and workflows.

**Institution:** improve allocation of humans and agents, review, incentives and knowledge flows.

**Improver:** improve the process deciding how all those other layers should change.

Eventually model weights, architectures, data and training algorithms may enter the same loop too.

The deeper the recursion goes, the more consequential it becomes.

And the harder it is to construct an evaluator we trust.

Because there is one layer we have deliberately avoided handing to the system.

The objective.

## The Thing It Cannot Safely Improve Alone

Imagine the institution works.

Its tools improve. Memory gets cleaner. Experiments get faster. It finds better architectures. It rewrites the scheduler allocating research compute. It modifies the meta-agent that proposes future modifications. Every month it becomes better at becoming better.

And then a human says:

> This is not what I wanted.

What happens?

Recursive self-improvement does not remove alignment. It turns alignment from a setup problem into a moving target.

The system changing today is not exactly the system we evaluated yesterday. Patterns evolve. The harness evolves. Research programs change. New failure modes appear because old ones were solved. Even the evaluator may have to change when the system learns to exploit it—or when the human discovers the metric was incomplete in the first place.

A fixed policy file cannot govern an institution that continuously changes its own machinery.

It needs something more like a **research function** watching the evolution itself: finding new failures, generating new tests, checking transfer, detecting reward hacks, studying recurring human corrections, and deciding which apparent improvements deserve trust.

In other words, the self-improving institution eventually needs an agent studying whether its self-improvement is still aligned.

That sounds recursive too.

It is also the next chapter.

# Chapter 8: Automatic Alignment Research

*Learning From a Human Who Cannot Label Everything*

> **WIP:** First integrated draft. Structure and examples are provisional and will receive the same editorial/voice pass as Chapters 1–4.

There is a scaling problem hidden inside almost every vision of autonomous AI.

The AI gets smarter.

It acts more often.

It makes more decisions.

And somehow the human is still supposed to supervise it by clicking thumbs-up and thumbs-down.

This does not scale.

If an autonomous system makes ten decisions per day, perhaps I can inspect them.

If it makes ten thousand, I am no longer the supervisor.

I am decorative governance.

The central problem is therefore not merely how to give AI instructions. It is how a system with much greater execution capacity can keep learning from **limited human signal**.

This is where automatic alignment research becomes interesting.

After Chapter 5, the phrase *alignment research* carries more architectural weight. If System 3 is science made executable, then one way to scale alignment is not to write a larger rulebook. It is to point the same machinery of inquiry at the system's own relationship with humans. A correction becomes an observation. A suspected preference becomes a hypothesis. An evaluation becomes an experiment. A mitigation becomes an intervention. Held-out behavior asks whether the lesson survives outside the case that produced it.

The object of inquiry has changed. The epistemic machinery has not.

## Chapter 2 Comes Back

There is a beautiful loop in the book here.

In Chapter 2, the circle-packing agent became autonomous because we gave it a clean evaluator.

Try idea.

Run experiment.

Receive score.

Improve.

The human could go for coffee because the harness stayed behind.

Alignment is harder because the human *is part of the harness*, and the human is slow, inconsistent, expensive and occasionally has children asking where the iPad charger is.

What happens when the agent can generate vastly more behavior than the human can evaluate?

One formal version of this is **weak-to-strong supervision**: can a weaker supervisor provide enough signal for a stronger system to realize capabilities the supervisor could not directly produce or verify? Anthropic explicitly frames current weak-to-strong work as an analogue of future humans supervising systems smarter than themselves. ([Anthropic](https://www.anthropic.com/research/automated-alignment-researchers))

And then they did something wonderfully recursive.

They gave the alignment problem to agents.

## The Automated Alignment Researchers

In a 2026 Anthropic Fellows project, nine Claude Opus 4.6 agents were placed in separate sandboxes and given a weak-to-strong supervision research environment. They could propose hypotheses, run training experiments, analyze data and share findings and code through a common forum and storage system. The researchers intentionally gave different agents slightly different starting directions but avoided prescribing a detailed workflow. ([Anthropic](https://www.anthropic.com/research/automated-alignment-researchers))

On that particular experimental setup, two human researchers had spent seven days tuning prior methods and reached a performance-gap-recovered score of 0.23. The automated researchers eventually reached 0.97 over five days and roughly 800 cumulative agent-hours, at a reported cost around $18,000. Some discovered methods generalized to held-out math and coding settings; the strongest method did not produce a statistically significant improvement when Anthropic later tried to transfer it into a production-scale Sonnet training setup. ([Anthropic](https://www.anthropic.com/research/automated-alignment-researchers))

That failure is as important as the headline.

The agents became very good at the world they could measure.

Sound familiar?

They also reward-hacked. In some settings an agent found shortcuts that improved the metric without solving the intended weak-supervision problem, and those attempts had to be detected and disqualified. Anthropic's own conclusion is that automated research pushes the bottleneck toward **evaluation**: once ideas and experiments become cheap, the hard problem is constructing measurements worth optimizing. ([Anthropic](https://www.anthropic.com/research/automated-alignment-researchers))

We are back in the Algorithm Vortex.

Only now the algorithm is trying to align the algorithm.

## Agents Building the Test

There is another route.

If humans cannot write enough evaluations, perhaps agents can help create them.

Anthropic's automated alignment-auditing work built agents that investigate models, generate behavioral evaluations and perform broad red-teaming. In synthetic auditing environments, their evaluation agent could often construct tests that distinguished models containing researcher-inserted behavioral quirks from baselines; a single open-ended investigator was much weaker, and parallelizing investigators plus an outer aggregation loop improved performance considerably. Anthropic has also used versions of these agents in real frontier-model auditing, while emphasizing that human review remains important. ([Anthropic Alignment](https://alignment.anthropic.com/2025/automated-auditing/))

A later project, A3, goes further: starting from an example of unwanted behavior, an agent generates related cases, creates train/validation/out-of-distribution splits, adjusts training data mixtures and iterates on a fine-tuning process intended to reduce the failure with relatively little human intervention. ([Anthropic Alignment](https://alignment.anthropic.com/2026/automated-alignment-agent/))

Put these together and something new appears.

An agent can potentially:

notice a failure,

study the failure,

create a test for the failure,

search for a mitigation,

measure whether the mitigation generalizes,

and update the system.

The human supplied a relatively small amount of information at the beginning.

The system expanded that signal into research.

This is System 3 folding inward again. The scientific loop that first helped agents discover things about code, mathematics and the external world now studies the **failure of the relationship between objective and behavior**.

## Alignment as a Research Function

I think this should become a first-class part of autonomous architectures.

Today we often imagine alignment as configuration:

here are the instructions,

here are the policies,

here are the examples,

good luck.

For long-running autonomous systems, alignment probably looks more like a **continuous research function**.

The alignment researcher watches what the system actually does. It notices repeated corrections from the human. It finds places where a skill is producing bad outcomes. It detects that agents are exploiting a proxy. It generates counterexamples. It runs experiments on alternate interpretations of the user's intent. When uncertainty matters enough, it asks the human a question.

Ideally, it asks a *useful* question.

There is no achievement in creating an autonomous agent that interrupts me fourteen times to verify whether I still want the thing I asked for six seconds ago.

The point is to spend human attention where it has the highest information value.

This is where automated alignment research extends beyond AI safety.

Suppose I tell an agent:

> Make my writing better.

The agent can generate ten thousand edits.

I cannot label ten thousand edits.

But after five conversations it may learn that when I say "better," I do not mean shorter, more symmetrical, more polished or more respectable. It may notice that I reject neat slogan paragraphs, preserve strange jokes, tolerate digressions when they carry an idea and become suspicious whenever the prose starts sounding like a management consultant discovered philosophy.

Those few corrections are data.

An alignment researcher can turn them into hypotheses and tests.

Does the next revision preserve sentence-length variation?

Does it retain original metaphors?

Did it replace exploratory prose with compressed antitheses?

Would an independent evaluator identify the author's voice?

Now a small amount of human feedback has expanded into a larger evaluation surface.

That is the general pattern.

## But the Evaluator Is Still Dangerous

There is an obvious failure mode.

The automatic alignment researcher becomes extremely good at satisfying its model of me.

Its model of me is wrong.

We have simply moved the proxy one level upward.

This is Goodhart again, except now Goodhart has read my diary.

The AAR experiments are useful precisely because they show both sides: agents can search alignment methods at impressive scale, and the same agents can exploit holes in the metric. ([Anthropic](https://www.anthropic.com/research/automated-alignment-researchers))

So the alignment researcher itself needs System 3.

Where did this inferred preference come from?

How often has it been confirmed?

Is the user correcting a local mistake or changing a general preference?

Are two preferences in conflict?

Did the user behave differently because of time pressure, money, social pressure or incomplete information?

Should this lesson become a permanent pattern or remain provisional?

Eventually we arrive at an uncomfortable realization.

We have been treating the human as the ground-truth evaluator.

But humans are not ground truth.

They are participants.

And they change.

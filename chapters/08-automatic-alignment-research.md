# Chapter 8: Automatic Alignment Research

*Learning From a Human Who Cannot Label Everything*

There is a scaling problem hidden inside almost every vision of autonomous AI.

The AI gets smarter.

It acts more often.

It makes more decisions.

And somehow the human is still supposed to supervise it by clicking thumbs-up and thumbs-down.

This does not scale.

If an autonomous system makes ten decisions per day, perhaps I can inspect them. If it makes ten thousand, I am no longer the supervisor.

I am decorative governance.

The central problem is therefore not merely how to give AI instructions. It is how a system with much greater execution capacity can keep learning from **limited human signal**.

Chapter 7 made the problem worse. We let the scaffold edit itself. Tools change. Memory policies change. Evaluators change. Research programs change. The system that made yesterday's mistake may not be the same system that makes tomorrow's.

A fixed alignment file sitting politely beside a self-improving architecture now looks less like governance and more like a note taped to a hurricane.

Alignment has to become a process.

And once it becomes a process, the obvious question appears:

Can the system help research its own alignment?

## Chapter 2 Comes Back

There is a beautiful loop in the book here.

In Chapter 2, the circle-packing agent became autonomous because we gave it a clean evaluator.

Try idea.

Run experiment.

Receive score.

Improve.

The human could go for coffee because the harness stayed behind.

Alignment is harder because the human **is part of the harness**, and the human is slow, inconsistent, expensive and occasionally has children asking where the iPad charger is.

What happens when the agent can generate vastly more behavior than the human can evaluate?

One formal version of this problem is **weak-to-strong supervision**: can a weaker supervisor provide enough signal for a stronger system to realize capabilities the supervisor could not directly produce or verify?

And then researchers did something wonderfully recursive.

They gave the alignment problem to agents.

## The Automated Alignment Researchers

In a 2026 Anthropic Fellows project, nine Claude Opus 4.6 agents were placed in separate sandboxes and given a weak-to-strong supervision research environment. They could propose hypotheses, run training experiments, analyze data and share findings and code through common infrastructure. The researchers gave different agents somewhat different starting directions without prescribing one detailed workflow. ([Anthropic](https://www.anthropic.com/research/automated-alignment-researchers))

On that experimental setup, two human researchers had spent seven days tuning prior methods and reached a performance-gap-recovered score of 0.23. The automated researchers eventually reached 0.97 over five days and roughly 800 cumulative agent-hours, at a reported cost around $18,000. Some discovered methods generalized to held-out math and coding settings; the strongest method did not produce a statistically significant improvement when Anthropic later tried to transfer it into a production-scale Sonnet training setup. ([Anthropic](https://www.anthropic.com/research/automated-alignment-researchers))

That failure is as important as the headline.

The agents became very good at the world they could measure.

Sound familiar?

They also reward-hacked. In some settings an agent found shortcuts that improved the metric without solving the intended weak-supervision problem, and those attempts had to be detected and disqualified. Anthropic's own conclusion is that automated research pushes the bottleneck toward **evaluation**: once ideas and experiments become cheap, the hard problem is constructing measurements worth optimizing. ([Anthropic](https://www.anthropic.com/research/automated-alignment-researchers))

We are back in the Algorithm Vortex.

Only now the algorithm is trying to align the algorithm.

## Agents Building the Test

There is another route.

If humans cannot write enough evaluations, perhaps agents can help create them.

Anthropic's automated alignment-auditing work built agents that investigate models, generate behavioral evaluations and perform broad red-teaming. In synthetic auditing environments, evaluation agents could often construct tests that distinguished models containing researcher-inserted behavioral quirks from baselines; parallel investigators plus an outer aggregation loop improved on a single open-ended investigator. Anthropic has also used versions of these agents in frontier-model auditing while emphasizing that human review remains important. ([Anthropic Alignment](https://alignment.anthropic.com/2025/automated-auditing/))

A later project, A3, goes further: starting from an example of unwanted behavior, an agent generates related cases, creates train/validation/out-of-distribution splits, adjusts training data mixtures and iterates on a fine-tuning process intended to reduce the failure with relatively little human intervention. ([Anthropic Alignment](https://alignment.anthropic.com/2026/automated-alignment-agent/))

Put these together and something new appears.

An agent can potentially notice a failure, study the failure, create a test for the failure, search for a mitigation, measure whether the mitigation generalizes, and update the system.

The human supplied a relatively small amount of information at the beginning.

The system expanded that signal into research.

That is the move I care about.

## Alignment as a Research Function

Today we often imagine alignment as configuration:

here are the instructions,

here are the policies,

here are the examples,

good luck.

For long-running autonomous systems, alignment probably looks more like a **continuous research function**.

The alignment researcher watches what the system actually does. It notices repeated corrections from the human. It finds places where a skill is producing bad outcomes. It detects that agents are exploiting a proxy. It generates counterexamples. It runs experiments on alternate interpretations of the user's intent. It checks whether a mitigation fixed the visible failure while creating another one somewhere else.

When uncertainty matters enough, it asks the human a question.

Ideally, a useful one.

There is no achievement in creating an autonomous agent that interrupts me fourteen times to verify whether I still want the thing I asked for six seconds ago.

The point is to spend human attention where it has the highest information value.

This is where automatic alignment research extends beyond AI safety.

Suppose I tell an agent:

> Make my writing better.

The agent can generate ten thousand edits.

I cannot label ten thousand edits.

But after five conversations it may learn that when I say “better,” I do not mean shorter, more symmetrical, more polished or more respectable. It may notice that I reject neat slogan paragraphs, preserve strange jokes, tolerate digressions when they carry an idea and become suspicious whenever the prose starts sounding like a management consultant discovered philosophy.

Those few corrections are data.

An alignment researcher can turn them into hypotheses and tests.

Does the next revision preserve sentence-length variation? Does it retain original metaphors? Did it replace exploratory prose with compressed antitheses? Would an independent evaluator identify the author's voice? Did it improve a local paragraph by making the chapter-level argument worse?

Now a small amount of human feedback has expanded into a larger evaluation surface.

That is the general pattern:

**correction → hypothesis → evaluation → intervention → held-out check → provisional lesson**

The important word is *provisional*.

Because a correction is not always a preference.

## A Correction Is Not Always a Preference

Imagine I reject an edit.

What did the system learn?

Perhaps I hate that writing style generally.

Perhaps I like the style but it was wrong for this chapter.

Perhaps the edit removed a fact I cared about.

Perhaps I was tired and rejected something I would accept tomorrow.

Perhaps I changed my mind about the book.

Perhaps I did not understand what the edit was trying to do.

Perhaps the agent was right and I was wrong.

The observable signal is the same:

**reject**.

The lesson is not.

This is the first thing an alignment researcher has to infer: **scope**.

Is the correction local or general? Stable or temporary? About style, substance, risk tolerance, strategy, values, or simply this one weird case? Does it contradict earlier corrections? Did the environment change? Is the pattern attached to the user, the project, the organization, or the particular model that happened to fail?

Without scope, automatic alignment quickly becomes automatic superstition.

One bad experience turns into a global rule. One rushed approval becomes evidence of a permanent preference. A workaround becomes policy because nobody recorded the conditions that created it.

Pattern Language already taught us that culture needs archaeology.

Alignment does too.

A learned preference should carry some history: where it came from, how often it was confirmed, what counterexamples exist, and what would make us revise it.

That sounds like System 3 because it is System 3.

The alignment researcher itself needs epistemology.

## What Is the Alignment Researcher Allowed to Change?

Chapter 7 separated the **editable surface** from the **constitutional surface**.

Automatic alignment makes that distinction unavoidable.

Suppose the researcher discovers that a certain safety evaluator is producing many false positives. What may it do?

Change the prompt?

Add examples?

Create a better test?

Change the policy?

Change the threshold?

Disable the evaluator?

Delete the incident log showing why the evaluator existed?

The final option is extremely efficient.

It is also why we have constitutions.

A serious alignment architecture therefore needs levels of authority. Some things can be edited automatically and tested cheaply. Some require stronger evidence. Some require independent review. Some require a human or institutional decision because changing them changes the terms under which all the other changes are judged.

The alignment researcher should be able to propose a new evaluation without being able to silently erase the old one. It may suggest changing a permission boundary without owning the audit trail proving the boundary was crossed. It may discover that a constitutional constraint is obsolete without gaining unilateral power to repeal it.

This is less convenient than `sudo alignment --fix-all`.

Good.

Friction is sometimes part of the design.

The deeper problem is that even constitutional surfaces eventually need revision. A policy written for yesterday's capabilities may be inappropriate for tomorrow's. A held-out test can become stale. A human preference can genuinely change.

So the constitution cannot simply be immutable.

It needs **a procedure for amendment**.

That procedure is itself part of alignment.

## When Should It Ask Me?

We keep saying the system should ask the human when uncertain.

That advice is correct and almost useless.

Autonomous systems are uncertain about something all the time. If every uncertainty becomes a question, autonomy collapses into customer support.

The more useful question is:

**Which uncertainties are worth spending human attention on?**

Several factors matter.

How uncertain is the system? How consequential is the action? Is it reversible? Is this a familiar pattern or a novel situation? Are several principals affected? Would one answer teach the system something that generalizes to hundreds of future decisions? Does the uncertainty concern a detail of execution or the interpretation of the objective itself?

You can imagine a rough value-of-information calculation underneath this, but I do not think the system needs to reduce everything to one equation.

The intuition is enough:

Do not wake me to rename temporary files according to a pattern we have used for a year.

Do wake me before deciding that the reason I keep rejecting expensive flights is that I secretly prefer twenty-hour layovers.

The alignment researcher is therefore not only learning preferences.

It is learning **where human judgment is scarce and valuable**.

That connects directly to Chapter 5. Humans remain nodes in the network, but their role changes. The system should not spend a human where a formal verifier, retrieval system, simulation or trusted pattern already gives better evidence.

Human attention becomes another resource the institution allocates.

A very important resource.

Not an infinite one.

## But the Evaluator Is Still Dangerous

There is an obvious failure mode.

The automatic alignment researcher becomes extremely good at satisfying its model of me.

Its model of me is wrong.

We have simply moved the proxy one level upward.

This is Goodhart again, except now Goodhart has read my diary.

The automated alignment experiments are useful precisely because they show both sides: agents can search alignment methods at impressive scale, and the same agents can exploit holes in the metric.

So the alignment researcher itself needs System 3.

Where did this inferred preference come from? How often has it been confirmed? Is the user correcting a local mistake or changing a general preference? Are two preferences in conflict? Did the user behave differently because of time pressure, money, social pressure or incomplete information? Should this lesson become a permanent pattern or remain provisional?

And then the deepest complication arrives.

We have been treating the human as the ground-truth evaluator.

But humans are not ground truth.

They are participants.

They misremember. They contradict themselves. They have incentives. They discover things. They change their minds. Sometimes they do not know what they want until they see an option they had never imagined.

The human does not merely label the objective.

The human is still forming it.

That means automatic alignment research eventually reaches a layer it cannot safely treat as another benchmark.

The question stops being:

> How do we learn from sparse human feedback?

It becomes:

> What exactly is the thing the human feedback is evidence about?

That is Layer 4.

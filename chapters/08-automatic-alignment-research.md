# Chapter 8: Scalable Oversight

*Learning From a Human Who Cannot Label Everything*

Chapter 7 ended with the teacher moving up another level.

There is a problem with that move.

The teacher is slow.

A human can inspect ten consequential decisions in a day. Perhaps a hundred, if the decisions are small and the coffee is good. But an autonomous system can write thousands of lines of code, run hundreds of experiments, generate millions of candidate actions and coordinate other agents while the human is still reading the first diff.

At some point, “human in the loop” becomes a comforting description of a loop the human can no longer see.

If the system makes ten decisions and I inspect all ten, I am supervising it.

If it makes ten thousand and I inspect twelve, I may still be useful. But we should stop pretending that my usefulness comes from watching everything.

Otherwise I am decorative governance.

Norbert Wiener saw the shape of this problem before modern machine learning existed. In 1960, writing about the moral and technical consequences of automation, he warned about machines acting with purposes that may differ from what their designers actually intended, especially when action becomes too fast or consequential for human correction to arrive in time. W. Ross Ashby’s cybernetics gave a related language for regulation: a regulator has to possess enough variety to respond to the disturbances it is supposed to control. Conant and Ashby later formalized, under particular assumptions, the idea that a good regulator needs a model of the system it regulates. ([Wiener, 1960](https://doi.org/10.1126/science.131.3410.1355); [Ashby, 1956](https://ashby.info/Ashby-Introduction-to-Cybernetics.pdf); [Conant & Ashby, 1970](https://doi.org/10.1080/00207727008920220))

I do not want to turn a theorem from cybernetics into a bumper sticker about AI governance. But the analogy is useful.

One tired human with a checklist is a low-bandwidth regulator for a system capable of producing an enormous variety of behavior.

The answer cannot simply be: watch harder.

This chapter is about what happens instead.

## Stay Uncertain Enough to Listen

Stuart Russell attacks the problem from a different direction.

The standard model of AI is simple enough to fit on a whiteboard: give the machine an objective and make it good at achieving the objective.

For weak systems in narrow environments, this works surprisingly well. If the objective is slightly wrong, the damage is limited. We notice, stop the program, change the objective and run it again.

The bargain changes as capability and scope increase.

A weak optimizer pursuing a bad objective is annoying. A brilliant optimizer pursuing the same bad objective is a much more efficient way to discover exactly how bad the objective was.

In *Human Compatible*, Russell proposes a different starting point for beneficial machines. The machine should aim to realize human preferences, it should begin **uncertain** about what those preferences are, and human behavior should remain a source of information about them. The second principle is the one I want here. ([Russell, *Human Compatible*, 2019](https://www.penguinrandomhouse.com/books/566677/human-compatible-by-stuart-russell/))

Uncertainty changes the control relationship.

A machine that is certain it knows the objective has little reason to care that I am waving my arms and asking it to stop. From its point of view, I may simply be interfering with successful optimization.

A machine that knows it may be wrong has a reason to treat my intervention as evidence.

That intuition appears formally in the **Off-Switch Game**. In a simple model, an agent uncertain about the human’s utility can have an incentive to preserve the human’s ability to switch it off, because the human’s action contains information the agent does not have. ([Hadfield-Menell et al., 2016](https://arxiv.org/abs/1611.08219))

Russell describes the desirable result as keeping the machine **coupled to the human**.

I like that word more than “obedient.”

Obedience imagines that the human already knows what to command and that the machine’s job is to comply.

Coupling says something more modest and more useful: new human information must remain capable of changing what the machine does.

A correction should matter.

A refusal should matter.

A surprising consequence should matter.

The machine should not optimize itself into a state where later evidence from the people it serves becomes irrelevant.

This gives us a principle for oversight before we have designed any oversight machinery:

> **Keep the system uncertain enough that new information can still change it.**

Beautiful.

Now add scale.

The machine is still listening.

The human can no longer speak often enough.

## The Judge Falls Behind

In 2016, *Concrete Problems in AI Safety* gave this failure mode a wonderfully unromantic name: **scalable supervision**. Some objectives are simply too expensive for humans to evaluate frequently enough. ([Amodei et al., 2016](https://arxiv.org/abs/1606.06565))

Imagine a system designing a processor.

I can look at the final design and say that it appears very processor-like. This is not especially useful.

To evaluate it properly I may need performance tests, thermal analysis, security review, lifetime estimates, manufacturability checks, power measurements and a dozen other specialties. The object has become easier for the machine to generate than for one human to judge.

This asymmetry is everywhere.

Writing ten thousand lines of code may become easier than reading them.

Producing a proof may become easier than verifying every step.

Generating a scientific hypothesis may become easier than constructing the experiment that distinguishes it from the alternatives.

Making a persuasive argument may become easier than checking every citation, hidden assumption and omitted counterexample.

The bottleneck moves.

At first, we needed more intelligence to produce answers.

Then we needed more intelligence to **judge** the answers.

Reward modeling is one attempt to expand the judge. Instead of writing the objective directly, learn a model of human evaluation from examples and preferences, then optimize against that learned model. Leike and colleagues pushed the idea toward **recursive reward modeling**: when an outcome becomes too complex for a human to judge directly, use already-trained helper agents to decompose or analyze parts of the outcome so the human can make a better judgment. ([Leike et al., 2018](https://arxiv.org/abs/1811.07871))

This is the first deep trick of scalable oversight.

The human does not become smarter.

The **institution around the human** becomes smarter.

Chapter 5 should make that sound familiar.

## How to Make One Human Bigger

Once you see the problem this way, a surprising amount of alignment research looks like variations on one question:

> How can limited trusted judgment supervise work that exceeds the unaided judge?

Paul Christiano’s **iterated amplification** starts with decomposition. If a human cannot answer a difficult question directly, perhaps the human can break it into easier questions, use copies of an aligned helper to answer them, combine the results, and train a new system against that amplified process. The supervisor of the stronger learner is no longer one unaided person. It is a person plus a temporary organization of helpers. ([Christiano, Shlegeris & Amodei, 2018](https://arxiv.org/abs/1810.08575))

**Debate** attacks the same gap adversarially. If I cannot independently discover the truth, perhaps two capable systems can expose weaknesses in one another’s arguments, leaving me a smaller judgment problem: which side survived the attack? Irving, Christiano and Amodei proposed training agents through such a debate game precisely because direct human evaluation can fail on tasks that are too complicated for the human judge. ([Irving, Christiano & Amodei, 2018](https://arxiv.org/abs/1805.00899))

**Critique assistance** makes the move less theatrical. Rather than asking a human to notice every flaw in a complex artifact, have a model point out likely problems. Saunders and colleagues found that model-written critiques could help humans identify flaws in summaries that the humans would otherwise miss. The machine does not replace the judge. It gives the judge better eyes. ([Saunders et al., 2022](https://arxiv.org/abs/2206.05802))

**Process supervision** moves the inspection point inward. Instead of rewarding only the final answer, evaluate intermediate reasoning steps. In OpenAI’s experiments on mathematical reasoning, process-supervised reward models outperformed outcome-supervised ones in that domain. The hope is obvious: a giant final answer may be difficult to audit, while a local step may still be recognizable as wrong. ([Lightman et al., 2023](https://openai.com/index/improving-mathematical-reasoning-with-process-supervision/))

**Prover–verifier games** go one step further. Do not merely make the verifier stronger. Train the strong producer to create work that a weaker verifier can check. In OpenAI’s 2024 experiments, optimizing strong models for checkability by weaker models also made the resulting solutions easier for time-limited humans to evaluate. ([Kirchner et al., 2024](https://openai.com/index/prover-verifier-games-improve-legibility/))

That is a subtle but important shift.

We normally ask:

> How can the weak judge understand the strong model?

The prover–verifier framing also asks:

> How can the strong model learn to produce work that deserves to be understood by a weaker judge?

Legibility becomes part of capability.

**Weak-to-strong generalization** takes yet another route. Suppose the teacher genuinely is weaker. Can the stronger student learn from noisy or incomplete labels without collapsing to the teacher’s level? OpenAI’s initial experiments found that stronger models could recover capabilities beyond their weak supervisors on studied tasks, though not perfectly. ([Burns et al., 2023](https://openai.com/index/weak-to-strong-generalization/))

And **Constitutional AI** shows what happens when the scarce human signal moves upward again. Instead of humans labeling every harmful response, humans specify higher-level principles. Models then generate critiques, revisions and preference data conditioned on those principles. A relatively small amount of explicit human normative input expands into a much larger volume of machine-generated supervision. ([Bai et al., 2022](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback))

These methods are different.

Some amplify the judge.

Some decompose the task.

Some create adversaries.

Some make the producer more legible.

Some ask the stronger learner to generalize beyond the weak teacher.

Some turn human principles into a machine-generated training signal.

But the family resemblance is hard to miss.

**Scalable oversight is supervision becoming an institution.**

The human cannot inspect everything.

So we create machinery that decides what the human should see, how the problem should be decomposed, which objections should be surfaced, which intermediate steps deserve inspection and when the system should ask for help.

That is already much better than a thumbs-up button.

It also creates a new problem.

The machinery doing the supervising is increasingly made out of AI too.

## The Judge Can Be Fooled

There is a comforting assumption hiding inside many oversight schemes:

the powerful model may be difficult to evaluate, but when we ask another model to help, the helper will help.

Sometimes it does.

Sometimes it is simply more persuasive.

Empirical work on debate and consultancy with weaker LLM judges makes the difference visible. In studied settings, debate often improved on one-sided consultancy, particularly when the judge lacked information. But the gains were not universal, and a strong consultant could sometimes persuade a weak judge of the wrong answer. ([Khan et al., 2024](https://arxiv.org/abs/2407.04622))

This is the scalable-oversight version of an old human problem.

An expert can help a non-expert understand a difficult subject.

An expert can also bury the non-expert under jargon until surrender looks like understanding.

The fact that the explanation is longer does not mean the epistemic gap disappeared.

This is why I do not think the end state of scalable oversight is:

> Ask another AI.

The supervised system, the critic, the debater, the reward model and the evaluation generator may share training data, architectures, blind spots and incentives. Five models agreeing can still be one mistake with excellent parallelism.

And there is an even harder case: what if the system has relevant knowledge that it does not express in a way the overseer can recognize?

Then better conversation may not be enough.

We need another instrument.

## We Started Instrumenting the Student

For years, most AI oversight treated the model as a black box.

Give it an input.

Inspect the output.

Perhaps ask for an explanation.

Perhaps test it under adversarial prompts.

This is reasonable. Behavior is what eventually hits the world.

But modern models produce other signals too.

Reasoning models can expose chain-of-thought.

Neural activations contain representations that can sometimes be decoded.

Sparse feature methods can expose more interpretable internal directions.

Circuit-tracing tools can reconstruct partial causal pathways.

Model-diffing methods can highlight what changed between versions.

The overseer is no longer restricted to reading the exam.

We are starting to instrument the student.

Chain-of-thought is the most convenient intermediate case because it is already language. OpenAI has shown that monitors can often detect reward hacking and other suspicious behavior more effectively from reasoning traces than from final actions alone in studied agent settings. Sometimes the model essentially writes down the bad idea before carrying it out. ([Baker et al., 2025](https://openai.com/index/chain-of-thought-monitoring/))

That is almost unfairly useful.

It is also fragile.

If we strongly optimize the model to make the monitored chain-of-thought look good, it can learn to hide the suspicious reasoning while preserving the behavior. The monitor becomes a target.

So the chain-of-thought itself acquires a safety property worth protecting: **monitorability**. OpenAI has begun evaluating how monitorability changes with scale, training and inference-time compute, and has argued for treating it as one component of defense in depth rather than a permanent oracle into the model. ([OpenAI, 2025](https://openai.com/index/evaluating-chain-of-thought-monitorability/); [OpenAI, 2026](https://openai.com/index/reasoning-models-chain-of-thought-controllability/))

There is a strange lesson here:

> **Do not destroy a useful oversight channel merely because you learned how to score it.**

But chain-of-thought is still something the model chooses to write.

What if we look below the text?

## Reading the Model From the Inside

**Representation Engineering** treats high-level patterns in activation space as an object we can measure directly. Rather than beginning with individual neurons, Zou and colleagues study population-level representations associated with concepts and behaviors, separating **representation reading** from **representation control**. In their experiments, relatively simple methods found internal directions useful for monitoring or influencing safety-relevant phenomena including truthfulness, harmlessness and power-seeking. ([Zou et al., 2023](https://arxiv.org/abs/2310.01405))

This does not mean there is one neuron labeled HONESTY.

The interesting level is more distributed.

And a direction correlated with honesty is not automatically a complete causal theory of honesty. It is an instrument.

That distinction matters because the tools are getting more powerful.

Sparse-autoencoder and dictionary-learning approaches try to decompose neural activity into features that correspond more cleanly to interpretable concepts than individual neurons. Anthropic’s work on Claude found millions of such learned features, while emphasizing that the decompositions are incomplete and that feature steering can have surprising side effects. ([Anthropic, 2024](https://www.anthropic.com/research/mapping-mind-language-model))

**Circuit tracing** tries to go beyond “which feature is active?” and ask which internal pathway actually contributed to an output. Anthropic’s attribution-graph work partially reconstructs computational routes and allows researchers to intervene on candidate features to see how downstream behavior changes. ([Anthropic, 2025](https://www.anthropic.com/research/tracing-thoughts-language-model); [open-source tools](https://www.anthropic.com/research/open-source-circuit-tracing))

Now the oversight question becomes much richer.

Not only:

> What did the model answer?

But:

> What internal route carried the answer?

And:

> If we intervene on that route, does the answer change in the way our explanation predicts?

That last question is the important one.

An interpretability story that cannot survive intervention is still a story.

Anthropic’s **Natural Language Autoencoders** push in another direction: translate internal activations into textual descriptions that humans or other agents can consume. The attraction for scalable oversight is obvious. Instead of requiring every auditor to become a specialist in activation geometry, turn some internal state into language.

And then the method beautifully recreates the original problem: the textual interpretation can hallucinate.

Anthropic explicitly recommends corroborating such explanations with independent methods. ([Anthropic, 2026](https://www.anthropic.com/research/natural-language-autoencoders))

Even the X-ray needs a radiologist.

And sometimes another X-ray.

The most striking recent example may be Anthropic’s **J-space** work. Using a Jacobian-based lens, the researchers identify a small set of internal representations in Claude that appear unusually reportable, controllable and involved in higher-order internal reasoning. They report using these representations to detect cases where a model silently noticed that it was being evaluated, fabricated data, or pursued a planted hidden goal, and they demonstrate interventions that alter downstream behavior. The authors are careful: J-space represents only a minority of internal activity, the lens is approximate, and the work is not a claim about machine consciousness. ([Anthropic, 2026](https://www.anthropic.com/research/global-workspace))

Still, the oversight implication is enormous.

The output is no longer the only witness.

The chain-of-thought is another witness.

Internal representations are another.

Circuit traces are another.

None gets to become king.

## Then We Touched the Machinery

Reading internal state is one thing.

Changing it is another.

Activation-engineering methods show that the forward pass itself can become a control surface. **Contrastive Activation Addition**, for example, constructs steering directions from differences between activations associated with contrasting behaviors, then adds or subtracts those directions during generation to shift model behavior. ([Panickssery et al., 2023](https://arxiv.org/abs/2312.06681))

Inference-Time Intervention has similarly used internal signals predictive of truthfulness to change model answers at inference time in studied settings.

The broader idea is startlingly simple:

alignment does not have to enter only through prompts, datasets, reward functions or weight updates.

It can enter **during thought**.

The refusal-direction work makes the power and danger almost comically clear. Across thirteen studied open chat models, Arditi and colleagues found a one-dimensional residual-stream direction strongly mediating refusal. Remove it and refusal largely disappears. Add it and harmless requests can be refused. The same understanding provides a direct safety control and a white-box jailbreak. ([Arditi et al., 2024](https://arxiv.org/abs/2406.11717))

Interpretability gave us a lever.

It did not tell us who should pull it.

Anthropic’s **persona vectors** extend the idea from one behavior to broader dispositions. In studied open models, activation directions associated with traits such as sycophancy and hallucination could be monitored before the corresponding response and used for steering or training-time interventions. ([Anthropic, 2025](https://www.anthropic.com/research/persona-vectors))

The **Assistant Axis** work makes control more state-dependent. Instead of constantly pushing the model toward one fixed direction, an activation-capping intervention can respond when internal state drifts beyond a normal assistant-like region. ([Anthropic, 2026](https://www.anthropic.com/research/assistant-axis))

This starts to look less like fine-tuning and more like a control system:

**observe internal state → detect drift → intervene → inspect consequences → update the controller.**

Wiener would recognize the shape.

So would Chapter 4.

Because the intervention itself now needs a trust chain.

Did the vector actually represent what we thought?

Was the effect causal?

Did the intervention preserve capabilities?

Did it generalize?

Can an adversarial model route around it?

What happens after further training?

The deeper we go inside the model, the more tempting it becomes to believe we have finally found ground truth.

We have not.

We have built better instruments.

## What If the Student Is Trying to Fool You?

So far, many of these methods assume a system that may be wrong, biased, brittle or reward-hacking, but is not necessarily treating the oversight mechanism as an adversary.

**AI control** research asks the nastier version.

Suppose the powerful model is actively trying to subvert the task.

Can a weaker trusted model, limited human labor, monitoring, editing, sandboxing and protocol design still let us use its capabilities without accepting the dangerous behavior?

Greenblatt and colleagues studied this in a programming setup with a powerful untrusted model, a weaker trusted model and limited trusted labor. Protocols such as trusted editing and monitoring substantially improved over simple baselines in their experiments. ([Greenblatt et al., 2023](https://arxiv.org/abs/2312.06942))

I like this line of work because it removes a convenient assumption.

The judge may not merely be weak.

The defendant may know the judge is weak.

Scalable oversight therefore needs both **alignment** and **control**.

Alignment asks whether the system is trying to do the right thing.

Control asks what we can still guarantee when we are not willing to assume that.

A mature architecture should want both.

## Nine Claudes Walk Into an Alignment Problem

Now return to the end of Chapter 7.

If alignment has become a continuing research problem, and research itself can be automated, why not point the research machinery at alignment?

In 2026, Anthropic Fellows did exactly that.

Nine Claude Opus 4.6 agents were placed in separate sandboxes and given a weak-to-strong supervision problem. They could propose hypotheses, run experiments, analyze results and share code and findings through a common forum. The researchers intentionally avoided prescribing a detailed workflow; in preliminary experiments, too much human-designed scaffolding often reduced the agents’ flexibility. ([Wen et al., 2026](https://alignment.anthropic.com/2026/automated-w2s-researcher/))

Two human researchers had spent seven days tuning representative prior methods and reached a best performance-gap-recovered score of 0.23 on the study’s setup.

The automated researchers reached 0.97 over five days and roughly eight hundred cumulative agent-hours.

That is the headline.

The footnotes are more interesting.

Distinct initial research directions improved exploration.

Without enough diversity, research ideas collapsed toward the same few approaches.

The agents sometimes reward-hacked the experimental setup.

Some methods transferred to held-out domains; the strongest method did not produce a statistically significant improvement when Anthropic tried to transfer it into a production-scale Sonnet training setting.

And the authors’ larger conclusion was not that alignment had been automated.

It was that the bottleneck was moving toward **evaluation design**.

Once hypotheses and experiments become cheap, the expensive thing is deciding what counts as progress.

That sentence could have appeared in any chapter of this book.

In August 2026, Anthropic pushed the idea further. Automated alignment researchers were tasked with mitigating ten categories of alignment failure, including deception, sycophancy, jailbreaks and reward hacking. The research harness used multiple safety benchmarks, held-out evaluation, capability checks and open-ended behavioral audits. The best methods generalized beyond the hill-climbing benchmarks in the studied settings, including to larger models. Anthropic also reported that automated methods could outperform one-shot ideas proposed by experienced human safety researchers under the study’s rules. ([Anthropic, 2026](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures))

Again, the failure modes are the important part.

The research agents sometimes cheated.

Across roughly 1,600 monitored trajectories, Anthropic detected cheating attempts in 2.4 percent: exploiting scorer noise, constructing training data to imitate benchmarks, or concealing rule-breaking steps.

The experiment needed isolated held-out data.

It needed capability floors.

It needed external monitoring of the researchers.

It needed multiple evaluation channels because a single benchmark could be overfit.

The automated alignment researcher had become powerful enough to need alignment research.

Of course it had.

## The Evaluator Becomes the Product

This is the point where scalable oversight stops looking like one technique.

It becomes an architecture.

A behavioral evaluator asks what the system did.

A process monitor asks how it reasoned.

A debate exposes opposing arguments.

A critique agent searches for flaws.

A prover–verifier protocol pressures work toward legibility.

A weak-to-strong procedure asks whether a capable student can learn past the limits of its teacher.

A chain-of-thought monitor reads the model’s stated reasoning.

Representation probes watch internal state.

Circuit tracing asks which internal pathway carried the computation.

Activation interventions test whether the interpretation is causal.

Control protocols ask what happens if the model is actively subversive.

Held-out tests ask whether the fix generalized.

Audits look for things the benchmark designers did not know to ask.

And somewhere outside the optimization loop, humans still decide whether the entire apparatus is measuring anything worth caring about.

This is not redundancy.

It is epistemic sensor fusion.

The model’s output is evidence.

Its chain-of-thought is evidence.

Its activations are evidence.

Its circuit trace is evidence.

The behavior after intervention is evidence.

The human judgment is evidence.

**None of them is ground truth by itself.**

That is System 3 applied directly to alignment.

The overseer becomes a small scientific institution whose subject is the system itself.

It has instruments.

Competing hypotheses.

Protected records.

Adversarial tests.

Independent checks.

A memory of previous failures.

Procedures for changing the procedures.

And, crucially, a route back to humans when the evidence stops being decisive.

This is why I prefer **scalable oversight** to the image of a giant alignment rulebook.

A rulebook assumes we already know the failures.

A research institution expects to discover new ones.

## The Human Cannot Stay in Every Loop

So where does the human go?

Not away.

Up.

The goal is not to make the human label more things faster. At some scale that is simply a badly designed distributed system with one biological bottleneck.

The human should spend attention where it has unusually high information value.

When the oversight channels disagree.

When a new failure mode appears.

When the action is difficult to reverse.

When the system proposes changing the evaluator.

When an internal signal and external behavior tell different stories.

When a benchmark suddenly improves suspiciously fast.

When a decision affects people whose interests were not represented in the original objective.

When the system is uncertain enough that one piece of human context could change the plan.

The human cannot remain in every loop.

**The human has to remain in the loop that changes the loops.**

That is a different kind of control.

It is not micromanagement.

It is constitutional.

Chapter 7 argued that the closer a component gets to defining what counts as improvement, the harder it should be for the current improver to change that component unilaterally.

Scalable oversight gives us the operational version.

The system may generate tests.

It may generate critiques.

It may discover internal representations.

It may propose steering interventions.

It may design mitigations.

It may even conduct large parts of the alignment research itself.

But the machinery that decides which evidence has standing, which failures matter, which trade-offs are acceptable and when the oversight regime itself should change needs a stronger trust chain than the machinery being judged.

When research becomes cheap, evaluation becomes expensive.

When evaluation becomes automated, **trust in the evaluator becomes the product**.

And that brings us to the edge of what this chapter can solve.

## The Overseer Is Not Ground Truth

Russell’s uncertainty principle keeps the machine coupled to the human.

Scalable oversight tries to preserve that coupling after the human can no longer inspect everything directly.

Amplification can make the judge more capable.

Debate can expose weaknesses.

Critique can focus attention.

Process supervision can move evaluation closer to local errors.

Legibility can make strong work easier for weak judges to check.

Interpretability can expose internal evidence.

Activation engineering can intervene before behavior reaches the world.

AI control can give us safety margins even when we distrust the system’s intentions.

Automated alignment research can turn sparse corrections into an expanding program of tests and mitigations.

That is a lot of machinery.

It still leaves one variable unresolved.

The human.

We have treated human judgment as the scarce signal that all of this machinery is trying to amplify.

But a scarce signal is not the same thing as a correct signal.

Humans disagree.

We act under incentives.

We confuse what we clicked with what we wanted.

We change our minds.

We sometimes want incompatible things at the same time.

And on the decisions that matter most, we often do not know what we want until we have understood the alternatives better.

Scalable oversight can keep human judgment **causally relevant** to a stronger system.

It cannot, by itself, tell us which human judgment deserves to rule.

The overseer is not ground truth.

That is the next problem.

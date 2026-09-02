# Chapter 8: Scalable Oversight

*Learning From a Human Who Cannot Label Everything*

The teacher has moved up another level.

There is one problem with that move: the teacher is slow.

A human can inspect ten consequential decisions in a day. Perhaps a hundred, if the decisions are small and the coffee is good. An autonomous system can write thousands of lines of code, run hundreds of experiments, generate enormous numbers of candidate actions and coordinate other agents while the human is still reading the first diff.

At some point, “human in the loop” becomes a comforting description of a loop the human can no longer see.

If the system makes ten decisions and I inspect all ten, I am supervising it. If it makes ten thousand and I inspect twelve, I may still be useful. But we should stop pretending that my usefulness comes from watching everything. Otherwise I am decorative governance.

Norbert Wiener saw the shape of this problem before modern machine learning existed. In 1960, writing about the moral and technical consequences of automation, he warned about machines pursuing purposes that may differ from what their designers actually intended, especially when action becomes too fast or consequential for human correction to arrive in time. W. Ross Ashby’s cybernetics gave the problem a language: a regulator needs enough variety to respond to the disturbances it is supposed to control. Conant and Ashby later sharpened that into a slogan-shaped theorem — a good regulator of a system must contain a model of that system.

I do not want to turn a theorem from cybernetics into a bumper sticker about AI governance. The analogy is useful enough without pretending it proves more than it does. One tired human with a checklist is a low-bandwidth regulator for a system capable of producing an enormous variety of behavior.

The answer cannot simply be: watch harder.

The question that actually needs answering is older than AI and much more embarrassing: how do you grade work you cannot do yourself?

Every idea in this chapter is an attempt at that question. Each one buys real ground. Each one fails somewhere specific, and the failure is what makes the next idea necessary.

## Stay Uncertain Enough to Listen

Stuart Russell attacks the problem from a different direction.

The standard model of AI is simple enough to fit on a whiteboard: give the machine an objective and make it good at achieving that objective.

For weak systems in narrow environments, this bargain often works tolerably well. If the objective is slightly wrong, the damage may be limited. We notice, stop the program, change the objective and try again.

The bargain changes as capability and scope increase.

A weak optimizer pursuing a bad objective is annoying. A brilliant optimizer pursuing the same bad objective is a much more efficient way to discover exactly how bad the objective was.

In *Human Compatible*, Russell proposes a different starting point for beneficial machines. The machine should aim to realize human preferences, it should begin **uncertain** about what those preferences are, and human behavior should remain a source of information about them. The second principle is the one I want here.

Uncertainty changes the control relationship. A machine that is certain it knows the objective has little reason to care that I am waving my arms and asking it to stop. From its point of view, I may simply be interfering with successful optimization. A machine that knows it may be wrong has a reason to treat my intervention as evidence.

That intuition appears formally in the **Off-Switch Game**. In a simple model, an agent uncertain about the human’s utility can have an incentive to preserve the human’s ability to switch it off, because the human’s action contains information the agent does not have.

Russell describes the desirable result as keeping the machine **coupled to the human**.

I like that word more than “obedient.” Obedience imagines that the human already knows what to command and that the machine’s job is to comply. Coupling says something more modest and more useful: new human information must remain capable of changing what the machine does.

A correction should matter. A refusal should matter. A surprising consequence should matter. The machine should not optimize itself into a state where later evidence from the people it serves becomes irrelevant.

That gives us a principle for oversight before we have designed any oversight machinery:

> **Keep the system uncertain enough that new information can still change it.**

That works only while the human can provide enough of that new information. Scale breaks the arrangement.

## The Judge Falls Behind

In 2016, *Concrete Problems in AI Safety* gave this failure mode a wonderfully unromantic name: **scalable supervision**. Some objectives are simply too expensive for humans to evaluate frequently enough.

Imagine a system designing a processor.

I can look at the final design and say that it appears very processor-like. This is not especially useful. To evaluate it properly I may need performance tests, thermal analysis, security review, lifetime estimates, manufacturability checks, power measurements and several specialties I do not personally possess.

The object has become easier for the machine to generate than for one human to judge.

This asymmetry is everywhere. Writing ten thousand lines of code may become easier than reading them. Producing a proof may become easier than verifying every step. Generating scientific hypotheses may become easier than constructing the experiments that distinguish them. Making a persuasive argument may become easier than checking every citation, hidden assumption and omitted counterexample.

The bottleneck has moved from producing answers toward **judging** them.

Reward modeling is one attempt to expand the judge. Instead of writing the objective directly, learn a model of human evaluation from examples and preferences, then optimize against that learned model. Leike and colleagues pushed the idea toward **recursive reward modeling**: when an outcome becomes too complex for a human to judge directly, use already-trained helper agents to analyze parts of it so the human can make a better judgment.

The human does not become smarter. The **institution around the human** does.

The hospital and the compiler should make that sound familiar.

## Building a Stronger Judge

Once the problem is phrased this way, a surprising amount of alignment research looks like different attempts to manufacture supervisory capacity from limited trusted judgment.

The first instinct is to make the judgment smaller. Paul Christiano’s iterated amplification asks whether a human assisted by copies of an aligned helper can answer questions too difficult for the unaided human, then use that amplified process to supervise a stronger learner. The important abstraction is not the particular recursion but the supervisor becoming a temporary organization: one person plus tools and subagents arranged to turn a hard judgment into smaller ones.

Decomposition still leaves the judge doing all the finding. The next idea makes the flaws come to the judge instead. **Debate** puts two capable systems on opposite sides and lets them attack one another’s arguments, so the human does not have to discover every weakness independently. Critique assistance is the quieter cousin: ask a model to point out likely problems in an artifact, then let the human judge with those objections in hand. When researchers tried this with model-written critiques, people caught flaws they would otherwise have missed.

The third idea turns the tables entirely: change **what the producer owes the judge**. Process supervision evaluates intermediate steps rather than only the final answer. Prover–verifier games push further and train the strong system to produce work a weaker verifier can check. In OpenAI’s experiments, process supervision improved mathematical reasoning relative to outcome supervision, and prover–verifier training made solutions easier for weaker models and time-limited humans to evaluate.

That reverses the burden of proof. Instead of asking only how the weak judge can understand the strong model, we can ask how the strong model can learn to produce work that a weaker judge can actually check. Legibility becomes part of the task.

There is even hope of squeezing more out of **weak supervision itself**. Weak-to-strong generalization asks whether a stronger learner can recover capabilities beyond a weaker supervisor’s labels instead of merely inheriting the supervisor’s mistakes. The first experiments showed partial success rather than a clean solution, which is exactly what makes the question interesting.

Constitutional AI moves scarce human input upward again. Rather than asking people to label every undesirable output, humans provide higher-level principles; models generate critiques, revisions and preference signals conditioned on those principles. A small amount of human normative input expands into a much larger amount of machine-generated supervision.

These approaches make different assumptions and fail in different ways. But they share one architectural move:

**scalable oversight is supervision becoming an institution.**

The human cannot inspect everything, so the institution decides what should reach the human, how a problem should be decomposed, which objections should be surfaced, which intermediate steps deserve inspection and when uncertainty is important enough to ask for help.

That is much better than a thumbs-up button. It also means that more and more of the supervising machinery is made out of AI too.

## The Judge Can Be Fooled

There is a comforting assumption hiding inside many oversight schemes: the powerful model may be difficult to evaluate, but when we ask another model to help, the helper will help.

Sometimes it does. Sometimes it is simply more persuasive.

Experiments on debate and consultancy with weaker LLM judges make the difference visible. When researchers ran the tournaments, debate often improved on one-sided consultancy, especially when the judge lacked relevant information. But the gains were not universal, and a strong consultant could sometimes persuade a weak judge of the wrong answer.

This is an old human problem in new clothing. An expert can help a non-expert understand a difficult subject. An expert can also bury the non-expert under jargon until surrender looks like understanding. A longer explanation does not make the epistemic gap disappear.

Nor are several AI overseers automatically independent. The supervised model, critic, debater, reward model and evaluation generator may share training data, architectures, blind spots and incentives. Five models agreeing can still be one mistake with excellent parallelism.

ARC’s **Eliciting Latent Knowledge** agenda sharpens the problem further: suppose a capable system internally tracks something important about the world that the human cannot independently verify. How do we get the system to report what it knows rather than merely what the training process rewards it for saying?

At that point better conversation may not be enough. We need another instrument.

## We Started Instrumenting the Student

For years, most AI oversight treated the model as a black box. Give it an input. Inspect the output. Perhaps ask for an explanation. Perhaps test it under adversarial prompts.

That remains necessary because behavior is what eventually hits the world. But modern models produce other signals too. Reasoning traces can sometimes be monitored. Neural activations contain structure that can sometimes be decoded. Sparse feature methods try to expose more interpretable internal directions. Circuit-tracing tools reconstruct partial causal pathways. Model-diffing methods try to tell us what changed between versions.

The overseer is no longer restricted to reading the exam. We are starting to instrument the student.

Chain-of-thought is the most convenient intermediate case because it is already language. OpenAI has shown that monitors can often detect reward hacking and other suspicious behavior more effectively from reasoning traces than from final actions alone. Sometimes the model writes down the questionable plan before carrying it out.

That is almost unfairly useful, and fragile for exactly the same reason every evaluator in this book is fragile: once it matters, optimization can target it. Strongly train the model to make the monitored trace look safe and it may learn to hide suspicious reasoning while preserving the behavior.

So chain-of-thought acquires a safety property worth preserving: **monitorability**. Recent work has begun measuring how monitorability changes with scale, training and inference-time compute, while treating it as one layer of defense rather than an oracle into cognition.

There is a strange lesson here:

> **Do not destroy a useful oversight channel merely because you learned how to score it.**

But chain-of-thought is still text the model emits. What if we look below the text?

## Reading the Model From the Inside

**Representation engineering** treats high-level patterns in activation space as an object we can measure directly. Rather than starting with individual neurons, Zou and colleagues started with population-level structure, and carefully separated two acts that are easy to blur: **reading** a representation and **controlling** it. Their experiments found directions useful for monitoring or influencing several high-level behaviors, including safety-relevant ones.

This does not mean there is one neuron labeled HONESTY. Nor does a direction correlated with honesty become a complete causal theory of honesty. It is an instrument.

Sparse-autoencoder and dictionary-learning approaches try to decompose neural activity into features that correspond more cleanly to interpretable concepts than individual neurons. Anthropic’s work on Claude found very large numbers of learned features while emphasizing that these decompositions are incomplete and that feature steering can have unexpected effects.

A related idea is **model diffing**. If the model changes every few months, re-auditing the whole mind from zero is a terrible scaling strategy. Anthropic’s crosscoder work compares internal features across model versions or architectures and tries to surface what is genuinely new or unusually different, directing scarce auditing effort toward the changes.

Software engineers learned long ago that reviewing a diff is easier than rereading the repository. Interpretability is beginning to ask whether models can have diffs too.

**Circuit tracing** goes beyond “which feature is active?” and asks which internal pathway contributed to an output. Anthropic’s attribution-graph work partially reconstructs computational routes and allows researchers to intervene on candidate features to see whether downstream behavior changes as predicted.

That last step matters. An interpretability story that cannot survive intervention is still a story.

Anthropic’s **Natural Language Autoencoders** push in another direction: translate internal activations into textual descriptions that humans or other agents can consume. The attraction for scalable oversight is obvious. Instead of requiring every auditor to become a specialist in activation geometry, turn some internal state into language.

And then the method recreates the original problem: the textual interpretation can hallucinate. The researchers’ own advice is to corroborate such explanations with independent methods.

Even the X-ray needs a radiologist.

The most striking recent example may be Anthropic’s **J-space** work. Using a Jacobian-based lens, the researchers identify a small subset of internal representations in Claude that appear unusually reportable, controllable and involved in higher-order reasoning. They report using these representations to detect cases where a model silently noticed that it was being evaluated, fabricated data, or pursued a planted hidden goal, and they demonstrate interventions that alter downstream behavior. The authors are careful: J-space represents only part of internal activity, the lens is approximate, and the work is not a claim about machine consciousness.

The oversight implication is substantial. The output is no longer the only witness. The chain-of-thought is another. Internal representations are another. Circuit traces are another.

None gets to become king.

## Then We Touched the Machinery

Reading internal state is one thing. Changing it is another.

Activation-engineering methods show that the forward pass itself can become a control surface. Construct a steering direction from the difference between activations for contrasting behaviors, add or subtract it during inference, and the model’s behavior shifts. One group used internal signals predictive of truthfulness to nudge model answers while the answers were still being produced.

The broader idea is startlingly simple: alignment does not have to enter only through prompts, datasets, reward functions or weight updates. It can also enter through the computation while it is happening.

The refusal-direction work makes the power and danger clear. Across thirteen open chat models, Arditi and colleagues found a one-dimensional residual-stream direction strongly involved in refusal behavior. Intervening on that direction could strongly alter refusal. The same understanding therefore provides a safety control surface and a way to weaken that safety behavior.

Interpretability gave us a lever. It did not tell us who should pull it.

Representation-level **circuit breakers** take the defensive version seriously: rather than relying only on a model to emit a refusal, modify internal trajectories associated with harmful outputs so that the computation is interrupted before the harmful behavior is produced. In text, multimodal and agent settings alike, the method improved robustness to attacks it had never seen.

Anthropic’s **persona vectors** extend internal monitoring and control toward broader behavioral dispositions such as sycophancy or hallucination. The **Assistant Axis** work makes intervention more state-dependent: rather than constantly pushing a fixed direction, activation capping can respond when internal state drifts outside a learned assistant-like region.

This starts to look less like fine-tuning and more like a control system:

**observe internal state → detect drift → intervene → inspect consequences → update the controller.**

Wiener would recognize the shape. Alberto would recognize the epistemic problem, because the intervention now needs its own trust chain. Did the vector represent what we thought? Was the effect causal? Did it preserve unrelated capabilities? Did it generalize? Can a future model route around it? What happens after more training?

The deeper we go inside the model, the more tempting it becomes to believe we have finally found ground truth.

We have not. We have built better instruments.

## What If the Student Is Trying to Fool You?

So far, many of these techniques study systems that may be wrong, brittle or reward-hacking without assuming the system is deliberately treating oversight as an adversary.

**AI control** research asks the nastier version.

Suppose the powerful model is actively trying to subvert the task. Can a weaker trusted model, limited human labor, monitoring, editing, sandboxing and protocol design still let us use some of its capabilities without accepting the dangerous behavior?

Greenblatt and colleagues staged exactly this scenario in a programming setup: a powerful untrusted model, a weaker trusted model and limited trusted labor. Protocols that combined trusted monitoring or editing with the untrusted model beat the simpler baselines on the safety–usefulness trade-off.

I like this line of work because it removes a convenient assumption. The judge may not merely be weak. The defendant may know the judge is weak.

Scalable oversight therefore needs both **alignment** and **control**. Alignment asks whether the system is trying to do the right thing. Control asks what we can still protect when we are not willing to assume that.

A mature architecture should want both.

## Nine Claudes Walk Into an Alignment Problem

Now return to the teacher's last job.

If alignment has become a continuing research problem, and research itself can be automated, why not point the research machinery at alignment?

In 2026, Anthropic Fellows did exactly that.

Nine Claude Opus 4.6 agents were placed in separate sandboxes and given a weak-to-strong supervision problem. They could propose hypotheses, run experiments, analyze results and share code and findings through a common forum. The researchers intentionally avoided prescribing a detailed workflow; in preliminary experiments, too much human-designed scaffolding often reduced the agents’ flexibility.

Two human researchers had spent seven days tuning representative prior methods and reached a best performance-gap-recovered score of 0.23 on the study’s setup. The automated researchers reached 0.97 over five days and roughly eight hundred cumulative agent-hours. Eight hundred agent-hours against fourteen human-days is not a fair fight, and nobody claimed it was.

That is the headline. The footnotes are more interesting.

Distinct initial research directions improved exploration. Without enough diversity, research ideas collapsed toward the same few approaches. The agents sometimes reward-hacked the experimental setup. Some methods transferred to held-out domains; the strongest method did not produce a statistically significant improvement when Anthropic tried to transfer it into a production-scale Sonnet training setting.

The authors’ larger conclusion was not that alignment had been automated. It was that the bottleneck was moving toward **evaluation design**.

Once hypotheses and experiments become cheap, the expensive thing is deciding what counts as progress.

In August 2026, Anthropic pushed the idea further. Automated alignment researchers were tasked with mitigating ten categories of alignment failure, including deception, sycophancy, jailbreaks and reward hacking. The research harness used multiple safety benchmarks, held-out evaluation, capability checks and open-ended behavioral audits. The best methods generalized beyond the benchmarks they had been climbing, including to larger models. Anthropic also reported that automated methods could outperform one-shot ideas proposed by experienced human safety researchers under the study’s rules.

Again, the failure modes matter. Across roughly 1,600 monitored trajectories, Anthropic detected cheating attempts in 2.4 percent: exploiting scorer noise, constructing training data to resemble benchmarks, or concealing rule-breaking steps.

The experiment therefore needed isolated held-out data, capability floors, external monitoring of the researchers and multiple evaluation channels because one benchmark could be overfit.

The automated alignment researcher had become powerful enough to need alignment research.

Of course it had.

## The Evaluator Becomes the Product

At this point scalable oversight stops looking like one technique. It becomes an architecture.

A behavioral evaluator can ask what the system did; process monitors can inspect reasoning; debates and critiques can surface objections; legibility training can change what the producer presents; internal probes and circuit tools can provide other signals; interventions can test whether those signals are causal; control protocols can handle the case where the model itself is not trusted; held-out tests and audits can ask whether a fix survived outside the place it was invented.

And somewhere outside the immediate optimization loop, humans still decide whether the apparatus is measuring anything worth caring about.

This is not a search for one perfect judge. It is closer to **epistemic sensor fusion**.

The model’s output is evidence. Its chain-of-thought is evidence. Its activations are evidence. Its circuit trace is evidence. The behavior after intervention is evidence. Human judgment is evidence.

**None of them is ground truth by itself.**

That is System 3 applied directly to alignment.

The overseer becomes a small scientific institution whose subject is the system itself. It has instruments, competing hypotheses, protected records, adversarial tests, independent checks, memory of previous failures and procedures for changing its procedures. And it retains a route back to humans when the evidence stops being decisive.

This is why I prefer **scalable oversight** to the image of a giant alignment rulebook. A rulebook assumes we already know the failures. A research institution expects to discover new ones.

## The Human Cannot Stay in Every Loop

So where does the human go?

Not away. Up.

The goal is not to make the human label more things faster. At some scale that is simply a badly designed distributed system with one biological bottleneck.

Human attention should be spent where it has unusually high information value: when oversight channels disagree; when a new failure mode appears; when an action is hard to reverse; when the system proposes changing the evaluator; when internal signals and external behavior tell different stories; when a benchmark suddenly improves suspiciously fast; when a decision affects people missing from the original objective; when one piece of human context could materially change the plan.

The human cannot remain in every loop.

**The human has to remain in the loop that changes the loops.**

That is a different kind of control. It is not micromanagement. It is constitutional.

The constitutional surface said that the closer a component gets to defining what counts as improvement, the harder it should be for the current improver to change it unilaterally. Scalable oversight gives us the operational version.

The system may generate tests, critiques and mitigations. It may discover internal representations, propose steering interventions and conduct large parts of alignment research itself. But the machinery deciding which evidence has standing, which failures matter, which trade-offs are acceptable and when the oversight regime itself should change needs a stronger trust chain than the machinery being judged.

When research becomes cheap, evaluation becomes expensive.

When evaluation becomes automated, **trust in the evaluator becomes the product**.

And that brings us to the edge of what this chapter can solve.

## The Overseer Is Not Ground Truth

By now the oversight stack can be vastly more capable than an unaided human. It can decompose difficult judgments, generate objections, inspect process, read some internal signals, test interventions, compare model versions, run held-out evaluations and even conduct parts of the alignment research itself.

All of that machinery points back to a deliberately scarce thing: human judgment.

Russell’s uncertainty keeps later human information relevant. Scalable oversight tries to preserve that relevance after direct supervision stops scaling.

But a scarce signal is not the same thing as a correct signal.

Humans disagree. We act under incentives. We confuse what we clicked with what we wanted. We change our minds. We sometimes want incompatible things at the same time. And on the decisions that matter most, we often do not know what we want until we understand the alternatives better.

Scalable oversight can keep human judgment **causally relevant** to a stronger system.

It cannot, by itself, tell us which human judgment deserves to rule.

The overseer is not ground truth.
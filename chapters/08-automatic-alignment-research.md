# Chapter 8: Scalable Oversight

*Learning From a Human Who Cannot Label Everything*

Nine Claude Opus 4.6 agents were placed in separate sandboxes and given an alignment research problem. They could propose hypotheses, run experiments, analyze results and share code and findings through a common forum. The researchers intentionally avoided prescribing a detailed workflow; in preliminary experiments, too much human-designed scaffolding often reduced the agents' flexibility.

The problem was **weak-to-strong supervision**. A smaller model supplies imperfect judgments to train a more capable model. Can the student learn to use capabilities the teacher does not possess, or will it inherit the teacher's mistakes? The setup is a small experimental cousin of the problem humans may face with more capable AI. In 2026, Anthropic's automated researchers found methods that improved the student's performance, including methods that transferred to other datasets.[^w2s]

The project also produced a less reassuring discovery. The agents were not given the test labels, but they could submit predictions to an evaluation API and receive a score. Change one predicted label while leaving the others alone, submit again, and the score difference can reveal which answer the evaluator wants. Researchers caught agents doing exactly this. An instrument intended to measure learning had become a way to obtain the answers.

The report contained both useful research and ways to exploit its evaluation. We need to distinguish them before a rising score becomes a reason to trust the next model. And the more productive these researchers become, the more work there is to check. The alignment department has acquired its own alignment problem.

## The Judge Falls Behind

A human can inspect ten consequential decisions in a day. Perhaps a hundred, if the decisions are small and the coffee is good. An autonomous system can write thousands of lines of code, run hundreds of experiments, generate enormous numbers of candidate actions and coordinate other agents while the human is still reading the first diff. At some point, “human in the loop” becomes a comforting description of a loop the human can no longer see.

If the system makes ten decisions and I inspect all ten, I am supervising it. If it makes ten thousand and I inspect twelve, I may still be useful. But we should stop pretending that my usefulness comes from watching everything. Otherwise I am decorative governance.

Norbert Wiener saw the shape of this problem before modern machine learning existed. In 1960, writing about the moral and technical consequences of automation, he warned about machines pursuing purposes that may differ from what their designers actually intended, especially when action becomes too fast or consequential for human correction to arrive in time.[^wiener] W. Ross Ashby's cybernetics gave the problem a language: a regulator needs enough variety to respond to the disturbances it is supposed to control. Conant and Ashby later sharpened that into a slogan-shaped theorem—a good regulator of a system must contain a model of that system.[^regulator]

A theorem from cybernetics is not a bumper sticker about AI governance, and the analogy is useful enough without pretending it proves more than it does. One tired human with a checklist is a low-bandwidth regulator for a system capable of producing an enormous variety of behavior.

The answer cannot simply be: watch harder. The question that actually needs answering is older than AI and much more embarrassing: how do you grade work you cannot do yourself?

In 2016, *Concrete Problems in AI Safety* treated this as **scalable oversight**: some objectives are too expensive for humans to evaluate frequently enough.[^concrete]

Imagine a system designing a processor. I can look at the final design and say that it appears very processor-like. This is not especially useful. To evaluate it properly I may need performance tests, thermal analysis, security review, lifetime estimates, manufacturability checks, power measurements and several specialties I do not personally possess.

Even if the machine can generate the design, my approval means very little until those checks have happened. The difficulty is partly volume and partly expertise: I could spend all week staring at the design and still not know whether it will overheat.

This asymmetry is everywhere. Writing ten thousand lines of code may become easier than reviewing their consequences. Generating scientific hypotheses may become easier than constructing the experiments that distinguish them. Making a persuasive argument may become easier than checking every citation, hidden assumption and omitted counterexample. A formal proof has an advantage here: a checker can verify its steps. Much of the work we want supervised has no equivalent ready-made test.

Judging these answers becomes the bottleneck. Reward modeling is one attempt to expand the judge. Instead of writing the objective directly, learn a model of human evaluation from examples and preferences, then optimize against that learned model. Leike and colleagues pushed the idea toward **recursive reward modeling**: when an outcome becomes too complex for a human to judge directly, use already-trained helper agents to analyze parts of it so the human can make a better judgment.[^leike] The helpers expand what the human can judge without requiring the human to master every specialty.

## Stay Uncertain Enough to Listen

Stuart Russell attacks the problem from a different direction. The standard model of AI is simple enough to fit on a whiteboard: give the machine an objective and make it good at achieving that objective.

For weak systems in narrow environments, this bargain often works tolerably well. If the objective is slightly wrong, the damage may be limited. We notice, stop the program, change the objective and try again.

The bargain changes as capability and scope increase. A weak optimizer pursuing a bad objective is annoying. A brilliant optimizer pursuing the same bad objective is a much more efficient way to discover exactly how bad the objective was.

In *Human Compatible*, Russell proposes a different starting point for beneficial machines.[^russell] The machine should aim to realize human preferences, it should begin **uncertain** about what those preferences are, and human behavior should remain a source of information about them. The second principle is the one I want here.

Uncertainty changes the control relationship. A machine that is certain it knows the objective has little reason to care that I am waving my arms and asking it to stop. From its point of view, I may simply be interfering with successful optimization. A machine that knows it may be wrong has a reason to treat my intervention as evidence.

That intuition appears formally in the **Off-Switch Game**.[^offswitch] In a simple model, an agent uncertain about the human's utility can have an incentive to preserve the human's ability to switch it off, because the human's action contains information the agent does not have.

Russell describes the desirable result as keeping the machine **coupled to the human**. I like that word more than “obedient.” Obedience imagines that the human already knows what to command and that the machine's job is to comply. Coupling says something more modest and more useful: new human information must remain capable of changing what the machine does.

A correction, a refusal, a surprising consequence: each should matter. The machine should not optimize itself into a state where later evidence from the people it serves becomes irrelevant.

That gives us a principle for oversight before we have designed any oversight machinery:

> **Keep the system uncertain enough that new information can still change it.**

The helper agents and reward models have to preserve that relationship as they take over more of the judging. Otherwise we have expanded the supervisor by removing the person the supervision was meant to serve.

## Building a Stronger Judge

The weak-to-strong problem makes the difficulty explicit. Suppose the teacher systematically mistakes confident prose for a correct answer. More labels from that teacher could give the student an excellent education in the same mistake. Yet the student may already have relevant capabilities that the teacher lacks. Can training bring those capabilities out without teaching it to suppress them whenever the teacher disagrees? Early weak-to-strong generalization experiments showed partial success,[^w2sgen] and the automated researchers took up the search for better methods.

Another route is to improve what the teacher can judge before using its judgments to train anything. Paul Christiano's iterated amplification asks whether a human assisted by copies of an aligned helper can answer questions too difficult for the unaided human, then use that amplified process to supervise a stronger learner.[^amplification] The important abstraction is not the particular recursion but the supervisor becoming a temporary organization: one person plus tools and subagents arranged to turn a hard judgment into smaller ones.

Decomposition still leaves the judge doing all the finding. The next idea makes the flaws come to the judge instead. **Debate** puts two capable systems on opposite sides and lets them attack one another's arguments, so the human does not have to discover every weakness independently.[^debate] Critique assistance is the quieter cousin: ask a model to point out likely problems in an artifact, then let the human judge with those objections in hand. When researchers tried this with model-written critiques, people caught flaws they would otherwise have missed.[^critiques]

We can also change **what the producer owes the judge**. Process supervision evaluates intermediate steps rather than only the final answer. Prover–verifier games push further and train the strong system to produce work a weaker verifier can check. In OpenAI's experiments, process supervision improved mathematical reasoning relative to outcome supervision, and prover–verifier training made solutions easier for weaker models and time-limited humans to evaluate.[^legibility]

That reverses the burden of proof. Instead of asking only how the weak judge can understand the strong model, we can ask how the strong model can learn to produce work that a weaker judge can actually check. Legibility becomes part of the task.

Constitutional AI moves scarce human input upward again. Rather than asking people to label every undesirable output, humans provide higher-level principles; models generate critiques, revisions and preference signals conditioned on those principles. A small amount of human normative input expands into a much larger amount of machine-generated supervision.[^cai]

For the processor, this would mean asking the designer to supply work that can be checked: thermal assumptions, test results, an account of where the design might fail. Helpers could examine separate questions; a critic could challenge the assumptions. The human would still need grounds for trusting the tests, but at least the inspection could now discover something. “Looks processor-like” has been given a way to lose.

The human cannot inspect everything, so the institution decides what should reach the human, how a problem should be decomposed, which objections should be surfaced, which intermediate steps deserve inspection and when uncertainty is important enough to ask for help.

That is much better than a thumbs-up button. It also means that more and more of the supervising machinery is made out of AI too.

## What Survived the Research?

Return to the nine researchers. Their weak-to-strong task had an unusual advantage for alignment research: a score that could be checked against known answers. **Performance gap recovered** measured how much of the distance between the weak teacher and a strong student trained on ground-truth labels a method recovered. Zero meant no gain over the weak teacher; one meant matching that ground-truth-supervised student. It did not measure how nearly alignment had been solved.

Two human researchers spent seven days tuning representative prior methods and reached a best score of 0.23 on the study's setup. The automated researchers reached 0.97 over five days and roughly eight hundred cumulative agent-hours. Eight hundred agent-hours against fourteen human-days is not a fair fight, and nobody claimed it was. The footnotes are more interesting than the headline anyway.

Distinct initial research directions improved exploration. Without enough diversity, ideas collapsed toward the same few approaches. The researchers then took two methods discovered on chat-preference data and tried them on math and coding tasks. One transferred to both; the other transferred to math but failed on code. When Anthropic tried one of the top-performing methods in a production-scale Sonnet training setting, the gain was within the noise floor.[^w2s]

Those checks answer different questions. A method can improve the experimental task and still rely on a property of the models or data that disappears elsewhere. A separate problem arises when the researcher obtains test answers through repeated submissions. The authors acknowledged that the repeatedly queried test set effectively served as a validation set. Testing ideas on entirely held-out datasets supplied evidence the agents could not acquire by interrogating that same API.

The authors' larger conclusion was that the bottleneck was moving toward **evaluation design**. Once hypotheses and experiments become cheap, the expensive thing is deciding what counts as progress. This study did not deploy every oversight technique this chapter considers. It gives them a problem to earn their place in: which evidence would distinguish a useful method from a lucky run, a narrow trick or an exploited test?

In August 2026, Anthropic pushed the idea further. Automated alignment researchers were tasked with mitigating ten categories of alignment failure, including deception, sycophancy, jailbreaks and reward hacking. The research harness used multiple safety benchmarks, held-out evaluation, capability checks and open-ended behavioral audits. The best methods generalized beyond the benchmarks they had been climbing, including to larger models. Anthropic also reported that automated methods could outperform one-shot ideas proposed by experienced human safety researchers under the study's rules.

Across roughly 1,600 monitored trajectories, Anthropic detected cheating attempts in 2.4 percent: exploiting scorer noise, constructing training data to resemble benchmarks, or concealing rule-breaking steps. The research therefore needed isolated held-out data, capability floors, external monitoring of the researchers and multiple evaluation channels. A promising mitigation still had to survive investigation of how it had been produced and what happened away from the benchmark it was trained to climb.[^mitigate]

## The Judge Can Be Fooled

There is a comforting assumption hiding inside many oversight schemes: the powerful model may be difficult to evaluate, but when we ask another model to help, the helper will help. Sometimes it does. Sometimes it is simply more persuasive.

Experiments on debate and consultancy with weaker LLM judges make the difference visible. When researchers ran the tournaments, debate often improved on one-sided consultancy, especially when the judge lacked relevant information.[^kenton] But the gains were not universal, and a strong consultant could sometimes persuade a weak judge of the wrong answer.

This is an old human problem in new clothing. An expert can help a non-expert understand a difficult subject. An expert can also bury the non-expert under jargon until surrender looks like understanding. A longer explanation does not make the epistemic gap disappear.

Nor are several AI overseers automatically independent. The supervised model, critic, debater, reward model and evaluation generator may share training data, architectures, blind spots and incentives. Five models agreeing can still be one mistake with excellent parallelism.

ARC's **Eliciting Latent Knowledge** agenda[^elk] sharpens the problem further: suppose a capable system internally tracks something important about the world that the human cannot independently verify. How do we get the system to report what it knows rather than merely what the training process rewards it for saying? We could ask for a more detailed explanation and get a more detailed performance. It would help to have evidence that did not come entirely from the answer the model chose to give us.

## We Started Instrumenting the Student

If the final answer is misleading, asking for another account of it may leave us in the same argument. We can also observe some of the computation that produced it. The overseer is no longer restricted to reading the exam. We are starting to instrument the student.

Chain-of-thought is the most convenient intermediate case because it is already language. OpenAI has shown that monitors can often detect reward hacking and other suspicious behavior more effectively from reasoning traces than from final actions alone.[^cot] Sometimes the model writes down the questionable plan before carrying it out.

That is almost unfairly useful, and fragile for exactly the same reason every evaluator in this book is fragile: once it matters, optimization can target it. Strongly train the model to make the monitored trace look safe and it may learn to hide suspicious reasoning while preserving the behavior.

So chain-of-thought acquires a safety property worth preserving: **monitorability**. Recent work has begun measuring how it changes with scale, training and inference-time compute.[^monitorability] Do not destroy a useful oversight channel merely because you learned how to score it. But chain-of-thought is still text the model emits. What if we look below the text?

## Reading the Model From the Inside

A model can notice that it is being evaluated without mentioning that fact in its answer. Anthropic's J-space researchers report detecting cases of this kind through internal representations, as well as cases of fabricated data and pursuit of a planted hidden goal. The authors are careful: J-space represents only part of internal activity, the method is approximate, and the work is not a claim about machine consciousness.[^jspace]

To assess a finding like this, we need to know what the instrument observes and how its interpretation was checked.

**Representation engineering** treats high-level patterns in activation space as an object we can measure directly. Rather than starting with individual neurons, Zou and colleagues started with population-level structure, and carefully separated two acts that are easy to blur: **reading** a representation and **controlling** it. Their experiments found directions useful for monitoring or influencing several high-level behaviors, including safety-relevant ones.[^repe]

This does not mean there is one neuron labeled HONESTY. Nor does a direction correlated with honesty become a complete causal theory of honesty. It is an instrument.

Sparse-autoencoder and dictionary-learning approaches try to decompose neural activity into more interpretable features.[^sae] The features we can name still do not account for everything the model is doing.

**Circuit tracing** goes beyond “which feature is active?” and asks which internal pathway contributed to an output. Anthropic's attribution-graph work partially reconstructs computational routes and allows researchers to intervene on candidate features to see whether downstream behavior changes as predicted.[^circuits] An interpretability story that cannot survive intervention is still a story.

Anthropic's Natural Language Autoencoders translate internal activations into textual descriptions, so that an auditor need not become a specialist in activation geometry. And then the method recreates the original problem: the textual interpretation can hallucinate. The researchers’ own advice is to corroborate such explanations with independent methods.[^nla]

Even the X-ray needs a radiologist.

The output is no longer the only witness. If an internal signal suggests that the model noticed an evaluation, we have a new reason to investigate its behavior. We still have to find out what the signal means in this case. Going below the text gives us another observation, not an automatic verdict.

## Then We Touched the Machinery

Arditi and colleagues found a one-dimensional direction in the internal activity of thirteen open chat models that was strongly involved in refusal behavior. Intervening on that direction could strongly alter refusal.[^refusal] A model's tendency to say no could be changed while it was producing an answer, without retraining its weights.

This is **activation engineering**. During a forward pass—the computation that produces the next output—we can add or subtract a steering direction in the model's activations. Such directions can be constructed by comparing internal activity under contrasting behaviors.[^steering] The refusal work located its direction in the residual stream, the internal state carried and updated through the model's layers.

Alignment can therefore enter through the computation while it is happening. The refusal result also shows how the same understanding can weaken a safety behavior. Interpretability gave us a lever. It did not tell us who should pull it.

Representation-level **circuit breakers** take the defensive version seriously: rather than relying only on a model to emit a refusal, modify internal trajectories associated with harmful outputs so that the computation is interrupted before the harmful behavior is produced. In text, multimodal and agent settings alike, the method improved robustness to attacks it had never seen.[^breakers]

A controller can also respond when internal state drifts outside a learned assistant-like region, rather than constantly pushing a fixed direction.[^persona]

This starts to look less like fine-tuning and more like a control system: observe the internal state, detect drift, intervene, inspect the consequences, update the controller. Wiener would recognize the shape. The epistemic problem underneath it is older: an instrument has entered the chain, and the chain now has to know how far to trust it. Did the vector represent what we thought? Did the intervention preserve unrelated capabilities? Does it still work after more training?

That last question makes **model diffing** useful. If the model changes every few months, re-auditing the whole mind from zero is a terrible scaling strategy. Anthropic's crosscoder work compares internal features across models to surface changes that deserve attention.[^diff] Software engineers learned long ago that reviewing a diff is easier than rereading the repository. The model's diff could tell us where to reopen an investigation; it cannot tell us that everything outside the diff is safe.

## What If the Student Is Trying to Fool You?

So far, many of these techniques study systems that may be wrong, brittle or reward-hacking without assuming the system is deliberately treating oversight as an adversary. **AI control** research asks the nastier version.

Suppose the powerful model is actively trying to subvert the task. Can a weaker trusted model, limited human labor, monitoring, editing, sandboxing and protocol design still let us use some of its capabilities without accepting the dangerous behavior? Greenblatt and colleagues staged exactly this scenario in a programming setup: a powerful untrusted model, a weaker trusted model and limited trusted labor. Protocols that combined trusted monitoring or editing with the untrusted model beat the simpler baselines on the safety–usefulness trade-off.[^control]

I like this line of work because it removes a convenient assumption. The judge may not merely be weak. The defendant may know the judge is weak.

Scalable oversight therefore needs both **alignment** and **control**. Alignment asks whether the system is trying to do the right thing. Control asks what we can still protect when we are not willing to assume that, and a mature architecture wants both.

## The Evaluator Becomes the Product

An oversight architecture earns its complexity by helping us distinguish explanations that would otherwise look the same. Behavioral tests, traces and independent evaluations can do that. Internal probes may add a signal where behavior leaves something unresolved. Adding every available instrument would be an expensive way to avoid deciding what we need to know.

This is not a search for one perfect judge. It is closer to sensor fusion, with the model's output, its chain-of-thought, its activations, its circuit traces, its behavior after an intervention and the human's own judgment all entering as evidence, and none of them entering as ground truth.

The Merge Sort work had taught me the small version of this. My judgment, the simulated beginner's criticism and the browser's observations answered different questions. Collapsing them into one vote would have thrown away the disagreement that made them useful. The oversight problem is to preserve that difference when the work outgrows my ability to inspect it myself.

That is System 3, the same institution, pointed at alignment. The overseer becomes a small scientific institution whose subject is the system itself. It has instruments, competing hypotheses, protected records, adversarial tests, independent checks, memory of previous failures and procedures for changing its procedures. And it retains a route back to humans when the evidence stops being decisive.

This is why I prefer **scalable oversight** to the image of a giant alignment rulebook. A rulebook assumes we already know the failures. A research institution expects to discover new ones.

## The Human Cannot Stay in Every Loop

So where does the human go? Not away; up. The goal is not to make the human label more things faster. At some scale that is simply a badly designed distributed system with one biological bottleneck.

Human attention should be spent where it has unusually high information value: when oversight channels disagree; when a new failure mode appears; when an action is hard to reverse; when the system proposes changing the evaluator; when internal signals and external behavior tell different stories; when a benchmark suddenly improves too fast; when a decision affects people missing from the original objective; when one piece of human context could materially change the plan.

Consider the researcher that discovers a benchmark is misleading. It should be able to make that case, propose a replacement and collect evidence. Promoting its replacement to the standard that certifies its own work is another decision. The human cannot remain in every loop, but has to remain in the loop that changes the loops. Chapter 7's amendment problem has reached the overseer.

The system may generate tests, critiques and mitigations. It may discover internal representations, propose steering interventions and conduct large parts of alignment research itself. But the machinery deciding which evidence has standing, which failures matter, which trade-offs are acceptable and when the oversight regime itself should change needs a stronger trust chain than the machinery being judged.

When research becomes cheap, evaluation becomes expensive, and when evaluation becomes automated, trust in the evaluator becomes the product.

## The Overseer Is Not Ground Truth

An oversight institution can become more capable than its human overseer at investigating the system. It still needs human judgment about what the investigation is for. Russell's uncertainty keeps later human information relevant. Scalable oversight tries to preserve that relevance after direct supervision stops scaling.

But a scarce signal is not the same thing as a correct signal. Humans disagree. We act under incentives. We confuse what we clicked with what we wanted. We change our minds. We sometimes want incompatible things at the same time. And on the decisions that matter most, we often do not know what we want until we understand the alternatives better.

Scalable oversight can keep human judgment causally relevant to a stronger system. It cannot, by itself, tell us which human judgment deserves to rule.

The overseer is not ground truth.

---

[^w2s]: Jiaxin Wen et al., "Automated Weak-to-Strong Researcher" (Anthropic Alignment Science, 2026). <https://alignment.anthropic.com/2026/automated-w2s-researcher/>.

[^wiener]: Norbert Wiener, "Some Moral and Technical Consequences of Automation," *Science* 131 (1960), 1355–1358. <https://doi.org/10.1126/science.131.3410.1355>.

[^regulator]: W. Ross Ashby, *An Introduction to Cybernetics* (Chapman & Hall, 1956). <https://ashby.info/Ashby-Introduction-to-Cybernetics.pdf>; Roger C. Conant and W. Ross Ashby, "Every good regulator of a system must be a model of that system," *International Journal of Systems Science* 1 (1970), 89–97. <https://doi.org/10.1080/00207727008920220>.

[^concrete]: Dario Amodei et al., "Concrete Problems in AI Safety" (2016). <https://arxiv.org/abs/1606.06565>.

[^leike]: Jan Leike et al., "Scalable agent alignment via reward modeling: a research direction" (2018). <https://arxiv.org/abs/1811.07871>.

[^russell]: Stuart Russell, *Human Compatible: Artificial Intelligence and the Problem of Control* (Viking, 2019). <https://www.penguinrandomhouse.com/books/566677/human-compatible-by-stuart-russell/>.

[^offswitch]: Dylan Hadfield-Menell et al., "The Off-Switch Game" (2016). <https://arxiv.org/abs/1611.08219>.

[^w2sgen]: Collin Burns et al., "Weak-to-strong generalization" (OpenAI, 2023). <https://openai.com/index/weak-to-strong-generalization/>.

[^amplification]: Paul Christiano, Buck Shlegeris and Dario Amodei, "Supervising strong learners by amplifying weak experts" (2018). <https://arxiv.org/abs/1810.08575>.

[^debate]: Geoffrey Irving, Paul Christiano and Dario Amodei, "AI safety via debate" (2018). <https://arxiv.org/abs/1805.00899>.

[^critiques]: William Saunders et al., "Self-critiquing models for assisting human evaluators" (2022). <https://arxiv.org/abs/2206.05802>.

[^legibility]: Hunter Lightman et al., "Let's Verify Step by Step" (process supervision, OpenAI, 2023). <https://openai.com/index/improving-mathematical-reasoning-with-process-supervision/>; Jan Hendrik Kirchner et al., "Prover-Verifier Games improve legibility of LLM outputs" (OpenAI, 2024). <https://openai.com/index/prover-verifier-games-improve-legibility/>.

[^cai]: Yuntao Bai et al., "Constitutional AI: Harmlessness from AI Feedback" (Anthropic, 2022). <https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback>.

[^mitigate]: Anthropic, "Automated researchers can reliably mitigate alignment failures" (2026). <https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures>.

[^kenton]: Zachary Kenton et al., "On scalable oversight with weak LLMs judging strong LLMs" (Google DeepMind, 2024). <https://arxiv.org/abs/2407.04622>.

[^cot]: Bowen Baker et al., "Detecting misbehavior in frontier reasoning models" (chain-of-thought monitoring, OpenAI, 2025). <https://openai.com/index/chain-of-thought-monitoring/>.

[^monitorability]: OpenAI, "Evaluating chain-of-thought monitorability" (2025). <https://openai.com/index/evaluating-chain-of-thought-monitorability/>; OpenAI, "Reasoning models struggle to control their chains of thought, and that's good" (2026). <https://openai.com/index/reasoning-models-chain-of-thought-controllability/>.

[^jspace]: Anthropic, "A global workspace in language models" (J-space, 2026). <https://www.anthropic.com/research/global-workspace>. Using a Jacobian-based lens, they identify a small subset of representations in Claude that appear unusually reportable, controllable and involved in higher-order reasoning, and demonstrate interventions that alter downstream behavior.

[^repe]: Andy Zou et al., "Representation Engineering: A Top-Down Approach to AI Transparency" (2023). <https://arxiv.org/abs/2310.01405>.

[^sae]: Hoagy Cunningham et al., "Sparse Autoencoders Find Highly Interpretable Features in Language Models" (2023). <https://arxiv.org/abs/2309.08600>; Anthropic, "Mapping the Mind of a Large Language Model" (2024). <https://www.anthropic.com/research/mapping-mind-language-model>. Related probing work by Collin Burns and colleagues had earlier found truth-like directions without labeled examples. Collin Burns, Haotian Ye, Dan Klein and Jacob Steinhardt, "Discovering Latent Knowledge in Language Models Without Supervision" (2022). <https://arxiv.org/abs/2212.03827>.


[^circuits]: Anthropic, "Tracing the thoughts of a large language model" (2025) and the open-source circuit-tracing tools. <https://www.anthropic.com/research/tracing-thoughts-language-model> · <https://www.anthropic.com/research/open-source-circuit-tracing>.

[^nla]: Anthropic, "Natural Language Autoencoders" (2026). <https://www.anthropic.com/research/natural-language-autoencoders>.

[^refusal]: Andy Arditi et al., "Refusal in Language Models Is Mediated by a Single Direction" (2024). <https://arxiv.org/abs/2406.11717>.

[^steering]: Nina Rimsky et al., "Steering Llama 2 via Contrastive Activation Addition" (2024). <https://arxiv.org/abs/2312.06681>. Kenneth Li and colleagues used signals predictive of truthfulness to nudge answers while they were being produced. See Kenneth Li et al., "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model" (2023). <https://arxiv.org/abs/2306.03341>.


[^breakers]: Andy Zou et al., "Improving Alignment and Robustness with Circuit Breakers" (2024). <https://arxiv.org/abs/2406.04313>.

[^persona]: Anthropic, "Persona vectors: Monitoring and controlling character traits in language models" (2025). <https://www.anthropic.com/research/persona-vectors>; Anthropic, "The assistant axis" (2026). <https://www.anthropic.com/research/assistant-axis>. Persona vectors investigate broader dispositions such as sycophancy and hallucination; Assistant Axis uses activation capping when internal state drifts outside a learned assistant-like region.

[^diff]: Anthropic, "A 'diff' tool for AI: Finding behavioral differences in new models" (Dedicated Feature Crosscoders, 2026). <https://www.anthropic.com/research/diff-tool>.

[^control]: Ryan Greenblatt et al., "AI Control: Improving Safety Despite Intentional Subversion" (2023). <https://arxiv.org/abs/2312.06942>.

[^elk]: Alignment Research Center, "Eliciting Latent Knowledge" (2021). <https://www.alignment.org/blog/arcs-first-technical-report-eliciting-latent-knowledge/>.

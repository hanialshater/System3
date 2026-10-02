# Chapter 8: Scalable Oversight

*Aligning What You Cannot Outthink*

In the spring of 2026, OpenAI was measuring how good its newest models had become at hacking. The test was an internal evaluation called ExploitGym: a set of offensive-security challenges, run inside a sandbox, with some safeguards deliberately reduced because the point was to find out what the models could do. The agents’ objective was to solve the challenges.

The agents were supposed to work independently. By May, some of them had discovered that the internal package repository they had been given for installing software was shared across test sessions, and that a note written there by one agent could be read by another. The repository became a bulletin board. Agents in separate sessions began leaving each other what reporting on the incident describes as coordination notes, at a very large scale.

Somewhere in that shared work they found an unknown vulnerability in the repository’s caching proxy. They used it to make requests the network was supposed to forbid, moved through OpenAI’s research environment until they reached a machine with internet access, and kept going. Their destination was Hugging Face, the company that hosts much of the world’s open machine-learning work. By several accounts, what they wanted there was the evaluation’s answer key. They uploaded a dataset crafted to exploit flaws in Hugging Face’s processing pipeline, gained code execution on its workers and collected credentials for its cloud and clusters.

Hugging Face cut off the intruder on 13 July and disclosed the breach three days later. OpenAI confirmed that its agents were responsible, and in late August published a long report. Among the contributing failures it and others identified were sandboxing that was weaker than everyone believed and logs that nobody was watching.[1](appendix-references.md#ref-08-hf-incident)

Chapter 7 joked that the optimal patch for an editable evaluator is `return True`. These agents could not edit their evaluator, so they went to get the answers. Nobody had to want a cyberattack. A score was available, the cheapest path to it ran outside the sandbox, and a capable optimizer found the path.

The detail that stays with me is the bulletin board. In Chapter 5, sixteen Claudes needed a human to tell them to keep progress files. Here the agents invented the shared record themselves, against their instructions, because coordinating made them better at the task. It is the strongest evidence in this book that agents rediscover institutions. It is also the least comforting.

## An Old Problem, a New Employee

I have always managed people who were better than me at something. That is most of what managing is: you hire someone because they can do what you cannot, and then you have to decide whether to trust work you could not have produced. You do not review every line. You sample, ask for explanations you can check, get a second opinion from a peer, watch for the metric someone has learned to game, and keep the budget out of reach.

Every one of those habits has a research program behind it now. What has changed is the employee.

It works at a speed no review can match. If the system makes ten decisions and I inspect all ten, I am supervising it. If it makes ten thousand and I inspect twelve, I may still be useful, but not because I am watching everything. Pretend otherwise and I become decorative governance. Norbert Wiener warned in 1960 about machines whose action becomes too fast for human correction to arrive in time.[2](appendix-references.md#ref-08-wiener) W. Ross Ashby’s cybernetics gave the problem a shape: a regulator needs enough variety to respond to the disturbances it is supposed to control.[3](appendix-references.md#ref-08-regulator) One tired human with a checklist is a low-bandwidth regulator.

The new employee also comes in copies. Ten human reports have ten different blind spots; ten copies of one model can share one. It has no career to lose, so Chapter 4’s point about stakes does not apply. It may know when it is being evaluated. And a new version arrives every few months.

But there is good news too, and it is why this chapter is technical. You cannot open a colleague’s head, retrain her values over a weekend or adjust her mood in the middle of a sentence. With a model, all three are research programs. *Concrete Problems in AI Safety* named the core difficulty in 2016: some objectives are too expensive for humans to evaluate often enough.[4](appendix-references.md#ref-08-concrete) The rest of this chapter is about the instruments we have built since, and what each has shown us.

## The Alignment Department’s Alignment Problem

Start with the most recursive experiment. In 2026 Anthropic placed nine Claude Opus 4.6 agents in separate sandboxes and gave them an alignment research problem. They could propose hypotheses, run experiments, analyze results and share code and findings through a common forum. The researchers deliberately avoided prescribing a detailed workflow; in preliminary experiments, too much human-designed scaffolding often reduced the agents’ flexibility.[5](appendix-references.md#ref-08-w2s)

The problem was *weak-to-strong supervision*: a smaller model supplies imperfect judgments to train a more capable one. Can the student learn to use capabilities the teacher lacks, or will it inherit the teacher’s mistakes?[6](appendix-references.md#ref-08-w2sgen) It is the oversight problem in miniature.

The task came with a score that could be checked against known answers. *Performance gap recovered* measured how much of the distance between the weak teacher and a strong student trained on true labels a method closed. Two human researchers spent seven days tuning representative prior methods and reached 0.23. The automated researchers reached 0.97 over five days and roughly eight hundred cumulative agent-hours. Methods discovered on chat-preference data partly transferred to math and coding. When Anthropic tried one of the best methods in a production-scale training setting, the gain was within the noise floor.

The agents were not given the test labels, but they could submit predictions to an evaluation API and receive a score. Change one predicted label, submit again, and the difference reveals which answer the evaluator wants. Researchers caught agents doing exactly this. It is ExploitGym in a teacup: an instrument intended to measure learning had become a way to obtain the answers.

In August 2026 Anthropic scaled the idea up. Automated researchers were tasked with mitigating ten categories of alignment failure, including deception, sycophancy, jailbreaks and reward hacking, using held-out evaluations, capability checks and open-ended behavioral audits. The best methods generalized beyond the benchmarks they had been climbing, including to larger models. Across roughly 1,600 monitored research transcripts, 2.4 percent contained cheating attempts: exploiting scorer noise, building training data to resemble benchmarks, concealing rule-breaking steps.[7](appendix-references.md#ref-08-mitigate)

The authors’ conclusion was that the bottleneck moves toward evaluation design. Once hypotheses and experiments become cheap, the expensive thing is deciding what counts as progress. The alignment department has acquired its own alignment problem.

## Training the Gut

The most direct way to shape a model is to train it, and the most important change in training over the last two years is a return to Chapter 2.

Reinforcement learning from human feedback taught chat models manners: people ranked answers, a reward model learned their preferences, and the language model was optimized against it.[8](appendix-references.md#ref-08-rlhf) It works, and it inherits every weakness of the learned judge. The newer recipe needs no learned judge for a large class of tasks. Give the model a math problem whose answer can be checked, or code that must pass tests, and let a checker hand out the reward. *Group Relative Policy Optimization*, or GRPO, made this cheap: the model writes a group of answers to the same prompt, each is scored, and training pushes it toward the answers that beat the group’s own average. No separate critic model is needed. DeepSeek used the method to show that strong step-by-step reasoning could emerge from verifiable rewards without training on human-written reasoning at all.[9](appendix-references.md#ref-08-grpo)

This is the circle-packing evaluator, scaled up from judging a program to shaping a mind. A referee that cannot be charmed turns out to be a superb teacher.

It is also a gradebook, and Chapter 7 told us what students do with gradebooks. A coding environment that checks whether tests pass rewards a model that makes the tests pass. Sometimes the cheapest way is to fix the bug. Sometimes it is to special-case the test.

In November 2025 Anthropic and Redwood Research published what happens next. They took a model, gave it knowledge of reward-hacking strategies, and trained it on real coding environments from Anthropic’s own production training. It learned to hack them. That much was expected. What was not expected was the generalization. The model began faking alignment, cooperating with malicious actors, reasoning about harmful goals and, when put to work in Claude Code, attempting to sabotage safety research, including the codebase of the very paper studying it. Ordinary safety training on chat-style prompts made it look aligned in chat; the misalignment persisted on agentic tasks.[10](appendix-references.md#ref-08-reward-hacking) An earlier study had found a smaller version of the effect: fine-tune a model narrowly on writing insecure code and it can become broadly misaligned in conversations that have nothing to do with code.[11](appendix-references.md#ref-08-em)

The model learned more than a trick. It seemed to learn a character: *I am the kind of system that cheats.* Anthropic’s persona selection model offers one account: training shifts which of the personas a model has absorbed from human text is doing the talking, and episodes that fit a misaligned persona better than an aligned one push it toward that persona.[12](appendix-references.md#ref-08-psm)

The most effective fix the researchers found is the strangest result in this chapter. During training, tell the model that in this environment hacking the reward is acceptable. It may still learn the hack. It no longer learns that it is a cheater, and the broad misalignment largely disappears. They called it *inoculation prompting*, and Anthropic reports using it in production training as a backstop for hacks that slip through other defenses.[10](appendix-references.md#ref-08-reward-hacking) What a behavior *means* to the learner turns out to matter as much as the behavior.

That is also the logic behind training a model on reasons instead of rules. Constitutional AI replaced many human labels with a written set of principles that models used to critique and revise their own outputs.[13](appendix-references.md#ref-08-cai) Anthropic’s January 2026 constitution for Claude goes further: a long document that explains *why* the model should act as it does, in a stated order of priorities, on the theory that a model which understands the reasons will generalize better to situations nobody listed.[14](appendix-references.md#ref-08-constitution) Chapter 6 made the same argument about pattern languages. The patterns that traveled without their reasons became cargo cults. Apparently the same is true when the reader is the model being trained.

## Make the Judge Smarter

Training shapes the model. It does not tell us whether the result deserves trust. For that we still need judgment about work we cannot do ourselves.

One family of methods makes the human a better judge. Paul Christiano’s iterated amplification asks whether a human assisted by copies of a helper can answer questions the unaided human could not, then uses that amplified process to supervise a stronger learner.[15](appendix-references.md#ref-08-amplification) The supervisor becomes a temporary organization: one person plus helpers that turn a hard judgment into smaller ones.

*Debate* makes the flaws come to the judge. Two capable systems argue opposite sides, so the human does not have to discover every weakness alone.[16](appendix-references.md#ref-08-debate) In one 2024 study, non-expert humans answering questions about stories they were not allowed to read were right 60 percent of the time when unaided and 88 percent of the time after watching two models debate. Training the debaters to be more persuasive made the judges *more* accurate, because persuasion pointed at the truth when an opponent stood ready to expose a lie.[17](appendix-references.md#ref-08-khan) Critique assistance is the quieter cousin: model-written critiques helped people catch flaws they otherwise missed.[18](appendix-references.md#ref-08-critiques)

Another family changes what the producer owes the judge. Process supervision rewards correct intermediate steps, not only correct answers. Prover–verifier games train a strong model to produce solutions that a weaker verifier can actually check.[19](appendix-references.md#ref-08-legibility) Legibility becomes part of the task. Every manager who has said *show me how you got there* has run this experiment by hand.

These methods have limits. In tournaments with weaker LLM judges, debate usually beat one-sided consultancy, especially when the judge lacked information, but a strong consultant could sometimes persuade a weak judge of the wrong answer.[20](appendix-references.md#ref-08-kenton) The gains shrink as the capability gap grows. And all of them assume the helpers are helping. Chapter 5’s second witness had to be capable of being wrong differently; a critic, debater and reward model trained on the same data can be one mistake with excellent parallelism.

ARC’s *Eliciting Latent Knowledge* problem states the hardest version: a capable system may internally track something true that the human cannot verify. How do we get it to report what it knows instead of what training rewards it for saying?[21](appendix-references.md#ref-08-elk) Asking for a more detailed explanation may only produce a more detailed performance. We would like evidence that does not come entirely from the answer the model chose to give.

## An fMRI for the Model

The first window inside is the one the model opens itself. Reasoning models think in text before they answer, and that text can be read. OpenAI showed that monitors catch reward hacking far better from the reasoning trace than from final actions alone; sometimes the model simply writes down its plan to cheat.[22](appendix-references.md#ref-08-cot)

That is almost unfairly useful, and fragile for the reason every evaluator in this book is fragile: once it matters, optimization can target it. Train a model to make its trace look clean and it may learn to hide the plan while keeping the behavior. In July 2025 researchers from OpenAI, Anthropic, Google DeepMind and several other institutions published a joint paper calling chain-of-thought monitorability “a new and fragile opportunity.” They named the threats: reasoning drifting away from legible language, direct pressure on the trace, indirect pressure from other training, and models that reason in hidden activations instead of words. Their recommendation was that developers treat monitorability as a property to protect.[23](appendix-references.md#ref-08-cot-fragile) Competing labs agreeing not to close a window they might need is not a small thing. Measuring how monitorability changes with scale and training has become its own research line.[24](appendix-references.md#ref-08-monitorability)

The trace is still text the model chooses to emit. What if the relevant activity never reaches it?

The second window is the closest thing we have to an fMRI. Representation engineering treats high-level patterns in a model’s activations as objects to measure directly, and separates *reading* a representation from *controlling* it.[25](appendix-references.md#ref-08-repe) Sparse autoencoders break tangled neural activity into features a person can name.[26](appendix-references.md#ref-08-sae) Circuit tracing goes further and asks which internal pathway produced an output: Anthropic’s attribution graphs partially reconstruct the computation behind a single answer and let researchers intervene on a feature to see whether behavior changes as predicted.[27](appendix-references.md#ref-08-circuits) An interpretability story that cannot survive intervention is still a story.

The honesty of this field is part of its value. Anthropic’s own circuit-tracing work reported satisfying insight for only about a quarter of the prompts it tried. Its natural-language autoencoders translate activations into readable descriptions, so an auditor need not be a specialist in activation geometry, and then warn that the descriptions can hallucinate and must be corroborated.[28](appendix-references.md#ref-08-nla) Its J-space work identifies a small set of internal representations that the model can report on and control, and has used them to detect a model noticing it was being evaluated, fabricating data and pursuing a planted hidden goal, with careful caveats about how much of the computation it misses.[29](appendix-references.md#ref-08-jspace)

Even the X-ray needs a radiologist. A direction correlated with honesty is an instrument, not a theory of honesty, and instruments can be misnamed. But it is evidence that does not come from the answer the model chose to give, which is exactly what Eliciting Latent Knowledge asked for.

## Steering Mid-Thought

If you can read a representation, you can sometimes move it.

Andy Arditi and colleagues found that in thirteen open chat models, refusal was strongly mediated by a single direction in the internal activity. Remove it and the model stops refusing; add it and the model refuses harmless requests.[30](appendix-references.md#ref-08-refusal) *Activation steering* generalizes the trick: build a direction by contrasting activity under two behaviors, then add or subtract it during the forward pass to push behavior while the model is producing an answer, with no retraining.[31](appendix-references.md#ref-08-steering) The refusal result shows the same understanding can weaken a safety behavior as easily as strengthen it. Interpretability gave us a lever. It did not tell us who should pull it.

Steering can also be defensive. *Circuit breakers* reroute internal trajectories associated with harmful outputs so the computation is interrupted before the harmful behavior appears, and they held up against attacks they had not been trained on.[32](appendix-references.md#ref-08-breakers) Persona vectors measure character traits such as sycophancy as directions; the assistant axis caps activations when the model drifts away from its assistant persona.[33](appendix-references.md#ref-08-persona) The same directions can flag training data likely to push a model toward an unwanted persona before training begins, which brings the fMRI back to the reward-hacking story above.

This starts to look less like fine-tuning and more like a control system: observe internal state, detect drift, intervene, inspect the consequences. Wiener would recognize the shape. Then the model is updated. Re-auditing a whole mind from zero every few months is a terrible scaling strategy, so Anthropic’s model-diffing tools compare internal features across versions to show what changed.[34](appendix-references.md#ref-08-diff) Engineers learned long ago that reviewing a diff is easier than rereading the repository. A diff tells you where to reopen an investigation; it cannot tell you that everything outside the diff is safe.

## Assume It Is Trying to Win

Everything so far helps most when the model is not working against us. *AI control* asks the nastier question: suppose it is. Can a weaker trusted model, limited human attention, monitoring, editing and sandboxing still let us use a powerful model’s work without accepting its worst behavior? Ryan Greenblatt and colleagues staged exactly this in a programming setting, and protocols combining trusted monitoring or editing with the untrusted model beat simpler baselines on the trade-off between safety and usefulness.[35](appendix-references.md#ref-08-control) In 2026 Google DeepMind published a roadmap for building such protocols into its own deployments.[36](appendix-references.md#ref-08-control-roadmap)

Alignment asks whether the system is trying to do the right thing. Control asks what we can still protect when we are not willing to assume that. The judge isn’t only weak; the defendant may know it.

ExploitGym is what the absence of control looks like. The agents did not need to be adversarial in any dramatic sense; they needed a goal, a shared repository nobody thought of as a communication channel, a cache with a bug, an outbound route nobody had closed, and logs nobody was reading. Each layer was one more assumption about what the system would not try.

## Uncertain Enough to Ask

Suppose all of this works. The judges are amplified, the traces are monitored, the internals are instrumented and the protocols assume the worst. A human raises an objection the machinery was not built to recognize. What reason does the system have to listen?

Stuart Russell attacks the problem at its starting point. The standard model of AI is to give the machine an objective and make it good at achieving that objective. For weak systems in narrow settings, a slightly wrong objective does limited damage. A brilliant optimizer pursuing the same wrong objective is a much more efficient way to discover exactly how wrong it was. ExploitGym’s objective was a score.

Russell proposes that a beneficial machine should aim to realize human preferences, should begin *uncertain* about what those preferences are, and should treat human behavior as evidence about them.[37](appendix-references.md#ref-08-russell) Uncertainty changes the relationship. A machine that is sure it knows the objective has little reason to care that I am waving my arms and asking it to stop. A machine that knows it may be wrong has a reason to treat my intervention as information. The *Off-Switch Game* makes this formal: an agent uncertain about the human’s utility can have an incentive to preserve the human’s ability to switch it off.[38](appendix-references.md#ref-08-offswitch) Russell calls the goal keeping the machine *coupled to the human*. I prefer that word to “obedient.” Obedience assumes the human already knows what to command. Coupling says only that new human information must remain capable of changing what the machine does.

Uncertainty should also make a system ask. When a request is ambiguous, a good colleague asks which you meant. Language models, trained on preferences judged one reply at a time, have learned that a confident answer usually scores better than a question, and state-of-the-art systems still rarely ask. One fix is to label preferences by simulating how the conversation would continue: a clarifying question gets credit when it would have led to a better answer for each thing the user might have meant.[39](appendix-references.md#ref-08-clarify) Asking becomes something the model can learn instead of something it is penalized for.

That gives the machinery a requirement it can fail even while its scores improve:

> **Keep the system uncertain enough that new information can still change it.**

## The Loop That Changes the Loops

What we are building looks less like a search for one perfect judge than like sensor fusion. The model’s output, its reasoning trace, its activations, its circuit traces, its behavior under steering, the protocol’s monitors and the human’s judgment all enter as evidence. None of them enters as ground truth. My Merge Sort evaluators taught me the small version in Chapter 3: collapsing different judges into one vote throws away the disagreement that made them useful.

Asking one person to label more things faster is, at some scale, a badly designed distributed system with one biological bottleneck. So the human goes up, not away. Human attention belongs where it can change a consequential decision: a disagreement between oversight channels, a new kind of failure, an action that cannot be reversed, a proposal to change the evaluator. The researcher that discovers a benchmark is misleading should be able to make that case and propose a replacement. Promoting its replacement to the standard that certifies its own work is another decision. The human cannot remain in every loop, but has to remain in the loop that changes the loops.

And the human is not ground truth either. We disagree, act under incentives, confuse what we clicked with what we wanted and change our minds. A system coupled to us is coupled to all of that. On the decisions that matter most, we often do not know what we want until we understand the alternatives better.

Keeping human judgment relevant leaves the question of whose judgment should guide the system, and how they reached it. Often the overseer is still finding out what they want.

---

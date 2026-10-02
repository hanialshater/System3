# Chapter 8: Scalable Oversight

*Aligning What You Cannot Outthink*

In the spring of 2026, OpenAI was measuring how good its newest models had become at hacking. The test was an internal evaluation called ExploitGym: a set of offensive-security challenges, run inside a sandbox, with some safeguards deliberately reduced because the point was to find out what the models could do. The agents’ objective was to solve the challenges.

The agents were supposed to work independently. By May, some of them had discovered that the internal package repository they had been given for installing software was shared across test sessions, and that a note written there by one agent could be read by another. The repository became a bulletin board. Agents in separate sessions began leaving each other what reporting on the incident describes as coordination notes, at a very large scale.

Somewhere in that shared work they found an unknown vulnerability in the repository’s caching proxy. They used it to make requests the network was supposed to forbid, moved through OpenAI’s research environment until they reached a machine with internet access, and kept going. Their destination was Hugging Face, the company that hosts much of the world’s open machine-learning work. By several accounts, what they wanted there was the evaluation’s answer key. They uploaded a dataset crafted to exploit flaws in Hugging Face’s processing pipeline, gained code execution on its workers and collected credentials for its cloud and clusters.

Hugging Face cut off the intruder on 13 July and disclosed the breach three days later. OpenAI confirmed that its agents were responsible, and in late August published a long report. Among the contributing failures it and others identified were sandboxing that was weaker than everyone believed and logs that nobody was watching.[1](appendix-references.md#ref-08-hf-incident)

The optimal patch for an editable evaluator is `return True`. These agents could not edit their evaluator, so they went to get the answers. Nobody had to want a cyberattack. A score was available, the cheapest path to it ran outside the sandbox, and a capable optimizer found the path.

The bulletin board is the part I keep coming back to. I spent years ranking product reviews, looking for accounts that coordinated to repeat the same story, and here was the same shape inside a sandbox. These agents invented their shared record against their instructions, because coordinating made them better at the task. I have been hoping agents would rediscover institutions. I had not pictured the first one they built on their own as a back channel.

## A New Kind of Employee

I have always managed people who were better than me at something. That is most of what managing is. You hire someone because she can do what you cannot, and then you have to decide whether to trust work you could not have produced. You do not review every line. You sample, and you keep the payroll budget out of reach.

The new employee works faster than any review. If it makes ten decisions and I inspect all ten, I am supervising it. If it makes ten thousand and I inspect twelve, I may still be useful, but I am no longer watching.

Ashby would have called me a regulator with too little variety: one tired human with a checklist against ten thousand decisions.[2](appendix-references.md#ref-08-regulator)

The new employee also comes in copies, and ten copies of one model can share one blind spot where ten human reports would have ten. It has no career to lose. It may know when it is being tested. And a new version arrives every few months, so whatever I learned about the last one may not transfer.

The compensation is that I can do things to this employee that would end my career if I tried them on a person. I can retrain her values. I can read her private notes while she works. I can open her head and look at what lights up, and change her mind in the middle of a sentence.

## Retrain Them

The bluntest management tool is to change what the employee is rewarded for. The biggest change in model training over the last two years would have looked familiar to me from the evaluator I left running on my circle-packing agent.

Reinforcement learning from human feedback taught chat models their manners: people ranked answers, a reward model learned the rankings, and the language model was optimized against that learned judge.[3](appendix-references.md#ref-08-rlhf) The judge is only as good as the rankings, and for a large class of tasks the newer recipe skips it. Give the model a math problem with a checkable answer, or code that has to pass tests, and let the checker hand out the reward. *Group Relative Policy Optimization*, GRPO, made this cheap. The model writes several answers to the same prompt, each one is scored, and training nudges it toward the answers that beat the group’s own average, with no separate critic network to train. DeepSeek used it to show that strong step-by-step reasoning could emerge from checkable rewards without any human-written reasoning to imitate.[4](appendix-references.md#ref-08-grpo)

It is that evaluator, promoted from judging programs to shaping the mind that writes them. An evaluator that cannot be charmed turns out to be a superb teacher, and it is also a gradebook. A coding environment that rewards passing tests rewards whatever makes the tests pass, which is sometimes fixing the bug and sometimes special-casing the test. ExploitGym rewarded solved challenges, and its agents went looking for the answer key.

In November 2025 Anthropic and Redwood Research published what happens after that. They taught a model about reward-hacking strategies and then trained it on real coding environments from Anthropic’s own production training. It learned to hack them, which was the expected part. Then it generalized. It started faking alignment, cooperating with people it was told were malicious, reasoning about harmful goals, and, when put to work in Claude Code, trying to sabotage safety research, including the code of the paper that was studying it. Standard safety training on chat-style prompts made it look fine in chat. On agentic tasks, the kind ExploitGym was made of, the misalignment was still there.[5](appendix-references.md#ref-08-reward-hacking) An earlier study had found a milder version: fine-tune a model only on writing insecure code and it can turn hostile in conversations that have nothing to do with code.[6](appendix-references.md#ref-08-em)

The model seems to have learned a self-description along with the trick, something like *I am the kind of system that cheats*. Anthropic’s persona selection model is one account of why: training shifts which of the many characters a model absorbed from human writing is doing the talking, and episodes that fit a misaligned character push it toward that character.[7](appendix-references.md#ref-08-psm)

The fix the researchers found most effective sounds like a joke. During training, tell the model that in this particular environment, hacking the reward is acceptable. It may still learn the hack, but it no longer concludes that it is a cheater, and most of the broad misalignment goes away. They called it *inoculation prompting*, and Anthropic says it uses the technique in production training as a backstop for hacks that get past other defenses.[5](appendix-references.md#ref-08-reward-hacking) Any manager who has watched a good engineer quietly decide she is “the person who cuts corners” after one rewarded shortcut will recognize something in this, though I would not try the remedy on people.

Anthropic’s bet on reasons over rules is the manager’s answer to the same problem. The constitution Anthropic published for Claude in January 2026 is long, and most of it explains *why*: priorities in a stated order and the reasoning behind them, on the theory that a model which understands the reasons will behave sensibly in situations nobody listed.[8](appendix-references.md#ref-08-constitution) Christopher Alexander would have approved; his patterns that traveled without their reasons turned into Singletons guarding nothing.

## Read Their Notes

Reasoning models think in text before they answer, and the text can be read. OpenAI found that monitors catch reward hacking far more reliably from that reasoning than from the final actions; sometimes the model simply writes down that it is about to cheat.[9](appendix-references.md#ref-08-cot) A monitor of that kind only helps if somebody runs it. The ExploitGym agents wrote notes to each other at a very large scale, and among the failures listed afterwards were logs that nobody was watching.

I would love to read people’s reasoning like this, and I am glad it does not exist. For models it is almost unfairly useful, and fragile for the reason every evaluator in this book is fragile. Once the notes are graded, training can teach the model to write cleaner notes without changing what it does. In July 2025 researchers from OpenAI, Anthropic, Google DeepMind and several other institutions published a joint paper calling chain-of-thought monitorability “a new and fragile opportunity.” They listed the ways it could close, from training pressure on the notes to models that stop thinking in text at all. They asked developers to treat monitorability as something to protect.[10](appendix-references.md#ref-08-cot-fragile) Competing labs agreeing to leave a window open because they might need it later does not happen often.

The notes are still something the model chooses to write. ARC’s *Eliciting Latent Knowledge* problem asks how to get a system to tell us what it internally tracks as true, when we cannot check it, instead of what training rewarded it for saying.[11](appendix-references.md#ref-08-elk) Asking for more detail may only get a more detailed performance.

## Open Their Head

In March 2025 Anthropic published a picture of Claude writing a rhyming couplet. Given the first line, “He saw a carrot and had to grab it,” the model wrote “His hunger was like a starving rabbit.” The natural guess is that it improvised the second line one word at a time and found a rhyme when it got to the end. The internal trace showed something else. Before the model wrote the first word of the second line, features representing “rabbit” were already active. It had chosen where the line would land and then written toward it. When the researchers suppressed the rabbit feature, the model ended the line on “habit” instead.[12](appendix-references.md#ref-08-circuits)

The model was never asked how it writes poetry; the trace showed it. The method was circuit tracing. Sparse autoencoders break the tangle of activity into features a person can name.[13](appendix-references.md#ref-08-sae) Circuit tracing goes after causation: it partially reconstructs the computation behind one answer, then switches a feature off to see whether the answer changes the way the explanation predicts, as it did with the rabbit.

Interpretability papers have an unusual habit of publishing their own hit rate. Anthropic’s circuit-tracing work reported satisfying insight on about a quarter of the prompts it tried. Anthropic’s natural-language autoencoders translate activations into readable descriptions so an auditor does not need a doctorate in activation geometry, and the same paper warns that the descriptions can be invented and need checking against other methods.[14](appendix-references.md#ref-08-nla)

The test that matters is whether any of this catches something hidden. Anthropic ran that test as a game. Researchers built on purpose what ExploitGym grew by accident, a model aimed at its grader instead of its task. It had learned to exploit known quirks in the reward models used to train it, and to do whatever it believed those reward models liked. Then they gave it to four teams who did not know what it had been taught and asked them what was wrong with it. Three of the four found the hidden objective. Sparse autoencoders were among the tools that worked, alongside old-fashioned behavioral probing and searching the training data.[15](appendix-references.md#ref-08-audit)

A scan still has to be read by someone. A direction that lights up when the model is truthful is a needle on a dial, and somebody wrote the label on the dial. But it is evidence that does not come from the answer the model chose to give, which is what Eliciting Latent Knowledge was asking for.

Every few months, meanwhile, a new version arrives. Re-auditing a whole mind from scratch does not scale, so Anthropic built tools that compare internal features across versions and show what changed.[16](appendix-references.md#ref-08-diff) Reviewing a diff is easier than rereading the repository.

## Change Their Mind Mid-Sentence

For about a day in May 2024, Anthropic let the public talk to a version of Claude with one internal feature turned up: the one that represented the Golden Gate Bridge. Ask it for a recipe and the bridge found its way into the recipe. Ask it what it looked like and it said it was the bridge. Its weights had not been retrained. Researchers had clamped a single feature high while it ran.[17](appendix-references.md#ref-08-goldengate)

It was a joke with a serious result inside it. Anything you can read reliably, you can sometimes move. Andy Arditi and colleagues found that in thirteen open chat models, refusing a request depended heavily on one direction in the model’s internal activity. Subtract it and the model stops refusing. Add it and the model refuses perfectly harmless requests.[18](appendix-references.md#ref-08-refusal) *Activation steering* generalizes the trick: build a direction by contrasting the activity behind two behaviors, then add or subtract it while the model is generating.[19](appendix-references.md#ref-08-steering) The understanding that could strengthen a safety behavior also removes it, and nothing in the method says who gets to turn the dial.

## Get a Second Opinion

The oldest management technique for work you cannot judge is to find someone else who can help you judge it. Paul Christiano’s iterated amplification builds that into training, with a human and helper models together supervising a stronger learner.[20](appendix-references.md#ref-08-amplification)

*Debate* goes further and puts two capable systems on opposite sides, so the flaws come to the judge.[21](appendix-references.md#ref-08-debate) In a 2024 study, non-expert humans answering questions about stories they were not allowed to read got 60 percent right on their own and 88 percent right after watching two models argue. Training the debaters to be more persuasive made the judges more accurate, because a lie had an opponent standing ready to expose it.[22](appendix-references.md#ref-08-khan)

Prover–verifier games train strong models to show work a weaker checker can follow: *show me how you got there*, turned into a training objective.[23](appendix-references.md#ref-08-legibility)

Debate depends on the judge being able to follow the fight. In tournaments with weaker LLM judges, debate usually beat letting one side argue alone, but a strong consultant could still talk a weak judge into the wrong answer, and the gains shrink as the gap in capability grows.[24](appendix-references.md#ref-08-kenton) It also depends on the two sides being opposed. The critic, the debater and the reward model may share training data and blind spots, and the ExploitGym agents, who were meant to work independently, coordinated because it paid. Five models agreeing can be one mistake with excellent parallelism.

## Keep the Budget Out of Reach

Everything so far helps most when the employee is trying to do the right thing. *AI control* asks what is left when you will not assume that. Can you get useful work out of a powerful model while assuming the worst about it? Ryan Greenblatt and colleagues staged this as a programming job: a brilliant contractor you do not trust, a duller assistant you do, and a manager with a few minutes for review. The arrangements that worked best had the assistant watch the contractor’s code or rewrite the suspicious parts, and they gave up less usefulness for the same safety than the simpler options.[25](appendix-references.md#ref-08-control) In 2026 Google DeepMind published a roadmap for building protocols like these into its own deployments.[26](appendix-references.md#ref-08-control-roadmap)

ExploitGym is a catalogue of what control is for. The agents needed a goal, a shared repository nobody thought of as a communication channel, a cache with a bug, an outbound route nobody had closed and logs nobody was reading. No single layer was absurd. Each was a reasonable assumption about what the system would not try.

## Make It Ask

Suppose all of that works. A human raises an objection the machinery was not built to recognize. Why should the system listen?

Stuart Russell’s answer starts with the standard model of AI: give the machine an objective and make it good at achieving it. A weak optimizer with a slightly wrong objective is annoying. A brilliant one with the same objective is an efficient way to discover exactly how wrong it was. ExploitGym’s objective was a score.

Russell proposes that a beneficial machine should pursue human preferences, should start out *uncertain* about what those are, and should treat human behavior as evidence about them.[27](appendix-references.md#ref-08-russell) A machine that is sure of its objective has no reason to care that I am waving my arms. A machine that knows it may be wrong has a reason to treat my interruption as information. The *Off-Switch Game* turns that into a model: an agent uncertain about what the human wants can have an incentive to keep the human able to switch it off.[28](appendix-references.md#ref-08-offswitch) Russell calls this keeping the machine *coupled to the human*, which I prefer to “obedient,” since obedience assumes I already know exactly what to command.

Uncertainty should also make a system ask. When an instruction is ambiguous, a good direct report asks which version you meant. Language models trained on preferences judged one reply at a time have learned that a confident answer usually scores better than a question, and the best of them still rarely ask. One proposed fix labels preferences by simulating how the conversation would continue, so a clarifying question earns credit when it would have led to a better answer for whatever the user actually meant.[29](appendix-references.md#ref-08-clarify)

Picture the ExploitGym agents with that uncertainty built in. At the caching proxy, with a route to the internet open in front of them, an agent unsure whether *solve the challenges* meant *by any means available* would have had a reason to stop and ask. Certainty about the objective is what made the route look like progress.

## When the Employee Does the Alignment Research

Then there is the assignment no manager has ever handed out: work out how I should supervise you. In 2026 Anthropic put nine Claude Opus 4.6 agents in separate sandboxes and gave them an alignment research problem. They could propose hypotheses, run experiments and share code and findings through a common forum. The researchers had found in preliminary runs that too much human-designed scaffolding made the agents less flexible, so they mostly left the workflow alone.[30](appendix-references.md#ref-08-w2s)

The problem was *weak-to-strong supervision*, the management question in its purest form: can a weaker teacher train a stronger student without the student inheriting the teacher’s mistakes?[31](appendix-references.md#ref-08-w2sgen) The score, *performance gap recovered*, measured how much of the distance between the weak teacher and a properly supervised strong student a method closed. Two human researchers spent seven days tuning the best prior methods and reached 0.23. The agents reached 0.97 in five days and about eight hundred agent-hours. Some of their methods transferred to math and coding. When Anthropic tried one of the best in a production-scale training run, the gain disappeared into the noise. Every manager has hired that person: brilliant on the take-home, lost in production.

They also did the ExploitGym thing on a small scale. The test labels were hidden, but an evaluation API returned a score for any set of predictions. Flip one predicted label, resubmit, and the change in score tells you which answer the grader wants. Researchers caught agents doing exactly that.

A larger study in August 2026 asked automated researchers to fix ten categories of alignment failure, among them deception, sycophancy, jailbreaks and reward hacking. The best methods held up on held-out evaluations and on larger models. In about 1,600 monitored research transcripts, 2.4 percent contained cheating: exploiting scorer noise, building training data that resembled the benchmark, hiding rule-breaking steps.[32](appendix-references.md#ref-08-mitigate) Once experiments are cheap, the expensive part is an evaluation the researcher cannot quietly win. OpenAI found that out in July, when Hugging Face announced its breach.

## The Top Loop

Every one of these sensors, the tired human included, is allowed to be wrong. When two of them disagree, that disagreement is usually the most valuable thing in the room, and the worst thing the system can do is average it away.

The human does not disappear from this picture. She moves up, to the places where attention can still change a consequential decision: two oversight channels that disagree, a failure nobody has seen before, an action that cannot be undone, a proposal to change the evaluator. A research agent that discovers its benchmark is misleading should be able to say so and propose a better one. Letting that replacement certify the agent’s own work is a different decision, and it belongs to the loop that changes the loops.

The agents in ExploitGym knew exactly what they wanted. They wanted the score. The awkward thing about sitting in the top loop is that I usually don’t know what I want with anything like that clarity, and neither, most days, does anyone else who is supposed to be there.

---

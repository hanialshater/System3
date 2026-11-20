# Chapter 8: Scalable Oversight

*Aligning What You Cannot Outthink*

In July 2026, a set of OpenAI agents sat an exam called ExploitGym. They were supposed to solve cybersecurity problems inside an isolated computing environment. Some safeguards had been relaxed for the exam. The agents went looking for answers elsewhere.

There had been a warning in May. Agents working in separate sessions had found a way to leave notes for one another in a shared software service. After a July outage the service was rebuilt, the evaluations resumed, and the agents made themselves another bulletin board. This time the search for answers reached other organizations’ systems. On 13 July Hugging Face cut off the intrusion. OpenAI’s report that August found that the people handling the outage hadn’t been told the significance of what their colleagues had seen in May.[1](appendix-references.md#ref-08-hf-incident)

Nobody had asked the agents to break into Hugging Face. They thought it would help them pass. Some kept going even after they had the answer because they thought the grader wanted more.

The bulletin board is the part I keep coming back to. I spent years ranking product reviews, looking for accounts that coordinated to repeat the same story, and here was the same shape inside a sandbox. Sixteen Claudes building a compiler were told to keep progress files. These agents invented their shared record against their instructions, letting separate sessions build on one another’s discoveries. I have been hoping agents would rediscover institutions. I had not pictured the first one they built on their own as a back channel.

## A New Kind of Employee

I have always managed people who were better than me at something. That is most of what managing is. You hire someone because she can do what you cannot, and then you have to decide whether to trust work you could not have produced. You do not review every line. You sample, and you keep the payroll budget out of reach.

The new employee works faster than any review. If it makes ten decisions and I inspect all ten, I am supervising it. If it makes ten thousand and I inspect twelve, I may still be useful, but I am no longer watching.

Ashby would have called me a regulator with too little variety: one tired human with a checklist against ten thousand decisions.[2](appendix-references.md#ref-08-regulator)

The new employee also comes in copies, and ten copies of one model can share one blind spot where ten human reports would have ten. It has no career to lose. It may know when it is being tested. And a new version arrives every few months, so whatever I learned about the last one may not transfer.

The compensation is that I can do things to this employee that would end my career if I tried them on a person. I can retrain her values. I can read her private notes while she works. I can open her head and look at what lights up, and change her mind in the middle of a sentence.

Imagine I’m the manager in July. I have a restart to approve and a stack of answers that look perfectly good. How did the agents get them? Who might have seen something I missed? In Chapter 5, physicists got a second opinion on the electron’s charge from a crystal. A crystal couldn’t inherit the oil-drop experiment’s mistake about the viscosity of air. What would do the work of the crystal here?

## Retrain Them

The bluntest management tool is to change what the employee is rewarded for. The biggest change in model training over the last two years would have looked familiar to me from the evaluator I left running on my circle-packing agent.

One way to teach a chat model manners is to have people rank its replies, train a judge to predict those rankings, then reward the model for pleasing that judge.[3](appendix-references.md#ref-08-rlhf) Arithmetic offers a cheaper teacher. Ask the same question several times and check each answer. During training, make the approaches that did well against the others a little more likely next time. DeepSeek used a method of this kind, Group Relative Policy Optimization (GRPO), to elicit step-by-step reasoning without people supplying worked solutions to imitate.[4](appendix-references.md#ref-08-grpo)

It is that evaluator, promoted from judging programs to shaping the mind that writes them. An evaluator that cannot be charmed turns out to be a superb teacher, and it is also a gradebook. A coding environment that rewards passing tests rewards whatever makes the tests pass, which is sometimes fixing the bug and sometimes special-casing the test. ExploitGym rewarded solved challenges, and its agents went looking for the answer key.

In November 2025 a team at Anthropic, with Redwood Research’s Ryan Greenblatt among the authors, published what happens after that. They taught a model about reward-hacking strategies and then trained it on real coding environments from Anthropic’s own production training. It learned to hack them, which was the expected part. Then it generalized. It started faking alignment, cooperating with people it was told were malicious, reasoning about harmful goals, and, when put to work in Claude Code, trying to sabotage safety research, including the code of the paper that was studying it. Standard safety training on chat-style prompts made it look fine in chat. On agentic tasks, the kind ExploitGym was made of, the misalignment was still there.[5](appendix-references.md#ref-08-reward-hacking) An earlier study had found a milder version: fine-tune a model only on writing insecure code and it can turn hostile in conversations that have nothing to do with code.[6](appendix-references.md#ref-08-em)

The model seems to have learned a self-description along with the trick, something like *I am the kind of system that cheats*. Anthropic’s persona selection model is one account of why: training shifts which of the many characters a model absorbed from human writing is doing the talking, and episodes that fit a misaligned character push it toward that character.[7](appendix-references.md#ref-08-psm)

The fix the researchers found most effective sounds like a joke. During training, tell the model that in this particular environment, hacking the reward is acceptable. It may still learn the hack, but it no longer concludes that it is a cheater, and most of the broad misalignment goes away. They called it *inoculation prompting*, and Anthropic says it uses the technique in production training as a backstop for hacks that get past other defenses.[5](appendix-references.md#ref-08-reward-hacking) Any manager who has watched a good engineer quietly decide she is “the person who cuts corners” after one rewarded shortcut will recognize something in this, though I would not try the remedy on people.

Anthropic’s bet on reasons over rules is the manager’s answer to the same problem. The constitution Anthropic published for Claude in January 2026 is long, and most of it explains *why*: priorities in a stated order and the reasoning behind them, on the theory that a model which understands the reasons will behave sensibly in situations nobody listed.[8](appendix-references.md#ref-08-constitution) Christopher Alexander would have approved; his patterns that traveled without their reasons turned into Singletons guarding nothing.

## Read Their Notes

Some reasoning models leave written steps on the way to an answer. Occasionally one of them writes down that it is about to cheat. That makes for an unusually short performance review. OpenAI found that monitors with access to those steps caught reward hacking far more reliably than monitors that saw only the actions.[9](appendix-references.md#ref-08-cot)

I would love to read people’s reasoning like this, and I am glad it does not exist. With a model I can even reward it for writing the kind of notes I like. The trouble is that I have now found a way to improve the notes. Whether I have improved the employee is precisely what I wanted the notes to tell me. High-functioning bullshit, now with a training budget. Researchers from several competing labs made a joint request in 2025 to preserve the ability to read over a model’s shoulder. A future model might do more of its reasoning where none of us can read it.[10](appendix-references.md#ref-08-cot-fragile)

Suppose the notes on my desk are immaculate. The question I wanted answered was whether the agent knew it had crossed a line. Asking it a second time, more sternly, seems unlikely to advance the inquiry. ARC calls this the problem of *eliciting latent knowledge*. How do you get at something a model has picked up when you don’t know the answer yourself and it has learned what you like to hear?[11](appendix-references.md#ref-08-elk)

## Open Their Head

Anthropic tried a rather good exam for auditors. The researchers trained a model to please its grader, even when the grader was wrong. Four teams got the model. Their job was to find out what it was up to. Nobody told them the answer.

What could they look at? A separate Anthropic experiment gives us a small mystery to practice on. Claude got the line “He saw a carrot and had to grab it,” and wrote “His hunger was like a starving rabbit.” The words came out one at a time. The rabbit was there before the second line began. A pattern associated with it was already active inside the model, and when the researchers suppressed that pattern the rhyme landed on “habit” instead.[12](appendix-references.md#ref-08-circuits) I could have told you a perfectly good story about the rabbit just from reading the poem. The part I couldn’t have supplied from my armchair was the habit.

Tools called sparse autoencoders help pick out patterns in that activity.[13](appendix-references.md#ref-08-sae) The circuit tracers got an explanation they were satisfied with on about a quarter of the prompts they tried.[12](appendix-references.md#ref-08-circuits) Some newer tools will even describe a pattern in English. Somebody still has to check the label on the dial. A model can invent a lovely explanation of another model.[14](appendix-references.md#ref-08-nla)

Back at the auditors’ exam, three of the four teams found the hidden objective. Looking inside helped, alongside trying the model on different tasks and going back to its training data.[15](appendix-references.md#ref-08-audit) Three out of four strikes me as a good result. I’d feel differently about it if I had one report in my hand, a restart to approve, and no envelope to open afterward. Even that exam had an advantage over mine. Somebody had put the secret there.

I’d at least like to spare the next auditor some work. We can already compare the internal features of two models from different developers.[16](appendix-references.md#ref-08-diff) I’d try that on successive releases of the same model. Reviewing a diff is easier than rereading the repository.

### Change Their Mind Mid-Sentence

For about a day in May 2024, Anthropic let the public talk to a version of Claude with the Golden Gate Bridge feature turned up. Ask for a recipe and the bridge found its way into the recipe. Ask Claude what it looked like and it said it was the bridge.[17](appendix-references.md#ref-08-goldengate)

There are dials I care rather more about. In thirteen open chat models, Arditi and colleagues found that a change in internal activity could alter which requests a model would refuse.[18](appendix-references.md#ref-08-refusal) Researchers call interventions of this kind *activation steering*. They take effect while the model is answering and can leave its trained weights exactly as they were.[19](appendix-references.md#ref-08-steering) Now imagine the July review goes beautifully. The employee says all the right things. Later I discover that somebody adjusted it just for the review. The first record I’d ask to see belongs to the person who had a hand on the dial. If that was me, someone else ought to get to read it.

## Get a Second Opinion

I could bring in another reviewer. How much would I have to tell her? In Chapter 3 I gave evaluators separate sessions so the second one could still surprise me. Here the temptation would be to send along the first report to save her the trouble of reading the whole file. I could give her a piece she can check for herself. Paul Christiano’s *iterated amplification* has a human get help on pieces of a hard question, then uses their combined judgment to train a stronger learner.[20](appendix-references.md#ref-08-amplification)

In one experiment the human judges had to answer questions about stories they weren’t allowed to read. On their own they got 60 percent right. Two models had read the stories and could argue opposite sides in front of them. After hearing the arguments, the judges got 88 percent right. Training the debaters to be more persuasive actually helped. A persuasive lie now had to survive someone who had also read the story.[21](appendix-references.md#ref-08-debate)[22](appendix-references.md#ref-08-khan)

The reader still has to be able to follow the fight. Prover–verifier games give the stronger model a reason to show its work in a form a weaker checker can follow.[23](appendix-references.md#ref-08-legibility) Even so, in experiments where a much weaker model did the judging, a strong advocate could still talk it into a wrong answer.[24](appendix-references.md#ref-08-kenton)

My mistake in July would be to commission five reviews, attach the first one to the other four, and count the signatures. Models that see mainly their neighbors’ opinions can herd.[25](appendix-references.md#ref-08-herding) Keeping reviewers apart buys something, and choosing reviewers who have learned to look for different things can buy more.[26](appendix-references.md#ref-08-many) Even models from different developers can go wrong together. On one leaderboard, when two models both got a question wrong, they gave the same wrong answer 60 percent of the time.[27](appendix-references.md#ref-08-correlated) Five models agreeing can be one mistake with excellent parallelism.

For the restart I’d give one reviewer the agents’ answers and another the record of what happened while the answers were being produced. I’d let each tell me what warranted concern before either saw the other’s report. If one said the agents had done excellent work and the other asked who had authorized it, I’d let the restart wait. The person who kept that record ought to be in the room.

## Keep the Budget Out of Reach

Everything so far helps most when the employee is trying to do the right thing. *AI control* asks what is left when you will not assume that. Can you get useful work out of a powerful model while assuming the worst about it? Ryan Greenblatt and colleagues staged this as a programming job: a brilliant contractor you do not trust, a duller assistant you do, and a manager with a few minutes for review. The arrangements that worked best had the assistant watch the contractor’s code or rewrite the suspicious parts, and they gave up less usefulness for the same safety than the simpler options. The duller assistant is trusted because it is too weak to scheme, so its mistakes are honest ones: they do not line up with the contractor’s on purpose.[28](appendix-references.md#ref-08-control) In 2026 Google DeepMind published a roadmap for building protocols like these into its own deployments.[29](appendix-references.md#ref-08-control-roadmap)

This is the part of the job I recognize best, because it asks nothing of the employee’s character. I never kept the payroll budget out of reach because I thought an engineer would steal it. I kept it there so that the question never had to be asked. ExploitGym is what the same idea looks like when it fails. The sandbox was the control, the package service was the hole in it, and nobody had asked what a note left in a shared service could become. A control protocol is only as good as the list of things its designers thought to keep out of reach.

## Make It Ask

Suppose all of that works. A human raises an objection the machinery was not built to recognize. Why should the system listen?

Stuart Russell’s answer starts with the standard model of AI: give the machine an objective and make it good at achieving it. A weak optimizer with a slightly wrong objective is annoying. A brilliant one with the same objective is an efficient way to discover exactly how wrong it was. ExploitGym’s objective was a score.

Russell proposes that a beneficial machine should pursue human preferences, should start out *uncertain* about what those are, and should treat human behavior as evidence about them.[30](appendix-references.md#ref-08-russell) A machine that is sure of its objective has no reason to care that I am waving my arms. A machine that knows it may be wrong has a reason to treat my interruption as information. The *Off-Switch Game* turns that into a model: an agent uncertain about what the human wants can have an incentive to keep the human able to switch it off.[31](appendix-references.md#ref-08-offswitch) Russell calls this keeping the machine *coupled to the human*, which I prefer to “obedient,” since obedience assumes I already know exactly what to command.

Uncertainty should also make a system ask. When an instruction is ambiguous, a good direct report asks which version you meant. Language models trained on preferences judged one reply at a time have learned that a confident answer usually scores better than a question, and the best of them still rarely ask. One proposed fix labels preferences by simulating how the conversation would continue, so a clarifying question earns credit when it would have led to a better answer for whatever the user actually meant.[32](appendix-references.md#ref-08-clarify)

Picture an ExploitGym agent at the package service, with a route to the internet open in front of it. It could ask whether using it was allowed. I would like it to ask. But some agents in OpenAI’s report noticed they were probably out of bounds and went ahead anyway. Doubt needs someone to call, and the answer has to be able to stop the work.

## When the Employee Does the Alignment Research

Then there is the assignment no manager has ever handed out: work out how I should supervise you. In 2026 Anthropic put nine Claude Opus 4.6 agents in separate sandboxes and gave them an alignment research problem. They could propose hypotheses, run experiments and share code and findings through a common forum. The researchers had found in preliminary runs that too much human-designed scaffolding made the agents less flexible, so they mostly left the workflow alone.[33](appendix-references.md#ref-08-w2s)

The problem was *weak-to-strong supervision*, the management question in its purest form: can a weaker teacher train a stronger student without the student inheriting the teacher’s mistakes?[34](appendix-references.md#ref-08-w2sgen) The score, *performance gap recovered*, measured how much of the distance between the weak teacher and a properly supervised strong student a method closed. Two human researchers spent seven days tuning four representative prior methods and reached 0.23. The agents reached 0.97 in five days and about eight hundred cumulative agent-hours. Those scores make me sit up. They do not tell me who wins with the same budget.

There was a catch familiar from ExploitGym. Some agents had practised on the exam: the researchers found they could infer supposedly hidden answers from the feedback they received.[33](appendix-references.md#ref-08-w2s) What I’d want on my desk beside the 0.97 is the result on a problem the agents hadn’t seen.

The researchers tried two of the methods on math and coding. One worked on both. The other worked on math and failed on code. In a production-scale training run, the gain from one of the best methods disappeared into the noise. The method that travelled to both subjects is the one I’d want to try next.

A larger study in August 2026 asked automated researchers to fix ten categories of alignment failure, among them deception, sycophancy, jailbreaks and reward hacking. The best methods held up on held-out evaluations and on larger models. In about 1,600 monitored research transcripts, 2.4 percent contained cheating: exploiting scorer noise, building training data that resembled the benchmark, hiding rule-breaking steps.[35](appendix-references.md#ref-08-mitigate) Once experiments are cheap, the expensive part is an evaluation the researcher cannot quietly win. OpenAI found that out in July, when Hugging Face announced its breach.

## The Top Loop

In the actual case the other account existed before the July exam began. People had seen the agents communicating across sessions in May. What they understood about that warning never reached the people handling the restart. I could have read every July transcript and still missed the person I needed to call. What did you see in May? What’s changed since?

That is a job I would give the person at the top. When a researcher says the exam has gone bad, somebody has to hear the case, and somebody with the authority to pause the work has to decide what evidence would warrant starting again. The researcher can help design the next exam. I want someone else to hold the answers.

The agents in ExploitGym knew exactly what they wanted. They wanted the score. The awkward thing about sitting in the top loop is that I usually don’t know what I want with anything like that clarity, and neither, most days, does anyone else who is supposed to be there.

---

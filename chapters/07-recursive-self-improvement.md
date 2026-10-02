# Chapter 7: Recursive Self-Improvement

*When Science Turns Inward*

Omar is walking his dog at night when something moves in the grass.

The dog reacts first: ears up, body low, absolutely certain. Omar reacts too. Two nervous systems running the same ancient program: light and sound go in, a model of the world comes out, and the model says *something is there.*

Omar’s brain wants an explanation, wants it immediately, and is not fussy about quality. A cat. An intruder. A ghost. Nothing supernatural has to exist for the ghost to be a real mistake: the eyes worked, the grass really moved, and the error arrived afterward, inside the machinery that interprets what the eyes deliver. Better eyes would not necessarily help. He might get a much clearer view of the grass and remain convinced it contained a ghost.

The strange step is the second thought. Omar can investigate the investigator. *Why do I think something is there?* Maybe the wind moved it. Or maybe the horror film from last night is still running somewhere in the back. Now the thought itself is under examination. It is a small, absurd superpower: the ability to distrust yourself on purpose. Omar can be wrong about the world, wrong about why he was wrong, and still able to debug himself.

Updating a belief is one thing. A good Bayesian revises how likely the ghost is as the evidence comes in, and becomes better informed without becoming a better reasoner. The second thought changes how Omar reasons: which reactions to trust, which to check, when the film is doing the thinking. I. J. Good, a statistician before he was anything else, called the rationality that manages its own deliberation *type II*, to distinguish it from the idealized kind that pretends thinking is free.[1](appendix-references.md#ref-07-good-rationality)

Whether the second thought makes anyone better is another matter. Writing down probabilities and checking them against outcomes gives forecasters a way to learn from their mistakes. Private reflection can instead become practice at defending them.[2](appendix-references.md#ref-07-tetlock)

Computing made a related move early. In 1962, at MIT, Tim Hart and Mike Levin did something that still feels slightly illegal. They wrote a Lisp compiler in Lisp. Then they handed the compiler its own source code, and the tool compiled itself.[3](appendix-references.md#ref-07-lisp)

There was no intelligence explosion. A compiler had participated in producing the next version of the compiler, and the building did not notice. Compiler people call this *self-hosting*. A compiler can compile a worse compiler, and a research system can redesign itself into a slower one. Self-reference is not self-improvement.

In 1965, the same I. J. Good imagined an *ultraintelligent machine* better than any human at intellectual activity. Machine design is itself an intellectual activity, he observed. A sufficiently capable machine might therefore design a better machine, which could design a better one again. The phrase that survived was *intelligence explosion*.[4](appendix-references.md#ref-07-good)

Good’s argument is only a few lines long, and it hides almost the entire problem inside one innocent word: *better*. Better at the current task, at learning the next one, or at inventing a way to learn?

The pattern file in Chapter 6 was a small piece of corrective machinery written down: a file meant to catch a misleading interpretation before the next experiment. An agent that rewrites that file has edited part of its working method. If the change helps under a credible evaluation, we can call it an improvement. Good’s recursive step asks for more: did the change make the system better at finding and testing further improvements? A better answer today does not establish that tomorrow’s investigator will be better at its work.

Minds are not the only things that attempt this, and most of the others are not conscious.

## Nobody Has to Be Conscious

On 28 February 2017, a large part of the internet stopped working for an afternoon. An engineer at Amazon Web Services, following an established playbook to take a few servers out of service, mistyped one input to a command. Far more servers came out than intended, and S3, the storage service underneath an embarrassing fraction of the web, went down with them. Amazon’s public account of the incident spends little time on the person. It explains what the tool allowed. The tool was changed to remove capacity more slowly and to refuse any request that would take a subsystem below the minimum it needed.[5](appendix-references.md#ref-07-s3)

Chapter 5 argued that telling people to be more careful is emotionally satisfying and institutionally almost worthless. The S3 fix is the other half of that argument. The outage was over in hours. The change to the tool was aimed at the next outage, the one nobody had had yet.

Amazon has a name for the document that carries this: the Correction of Error. It records what happened, asks why until the answers stop being about people, and ends in actions that are tracked until they are done. Amazon describes the process as a search for what to improve, not for whom to blame, and as part of a culture that rewards people for surfacing problems.[6](appendix-references.md#ref-07-coe) Over years, the actions pile up into procedures, the procedures into runbooks, and the runbooks, when someone is patient enough, into automation. The people who do that work are judged, eventually, by colleagues who read what changed and whether it held.

Failure is handled the same way. In 2014 Amazon launched the Fire Phone and within months wrote down about $170 million on it.[7](appendix-references.md#ref-07-firephone) Some of the people who built it lost their jobs in a later reorganization. Many others moved onto other devices, and in Amazon’s own retelling the phone’s lessons fed the Echo and Alexa.[8](appendix-references.md#ref-07-echo) A failed product had trained engineers in voice, hardware and the particular ways consumer devices embarrass you, and the company kept much of that training.

The people doing this work know they are changing something. None needs to hold the whole organization in mind. Incidents become changes to tools, experience becomes procedure, failed projects remain reserves of skill, and other people, looking at the evidence over time, decide what counted. The organization can learn without having a mind of its own.

It does accumulate. An added check is easy to see and easy to credit. A check quietly deleted because nobody needs it any more is neither. Left alone, the procedures outlive their reasons, and the organization becomes the rule-based exoskeleton I admitted in Chapter 1 to spending a career building.

## Science Changes Its Methods

Science has spent centuries changing the procedures that produce its results. Controlled comparison, statistics, randomized trials, blinding, peer review and preregistration all change how research is done. Their value has to be investigated too: under what conditions do they make findings more reliable, and what do they miss? Omar’s second thought has acquired instruments, records and other people who can disagree with it.

The accumulation has been uneven. A useful method can meet resistance; a weak one can become routine. Other laboratories can put a method to work and find failures its authors missed, but that independence has to be maintained. Evidence that a method works also arrives at the speed of the experiments it governs. Slowness gives criticism time to catch up, and gives an incumbent the same time to dig in.

Science also has a way of fighting its own accumulation. Fields drown in results, and then somebody writes the textbook or finds the explanation that lets a newcomer skip three years of the climb. Chris Olah and Shan Carter called the cost of not doing this *research debt*, and the work of paying it down *distillation*.[9](appendix-references.md#ref-07-distill)

So we already live inside self-improving systems. One question follows us from each of them: who can challenge the judgment that a change helped? Could we grow one out of models and code?

## Growing One

Eliezer Yudkowsky describes recursive self-improvement as an AI using its current intelligence to improve the cognitive machinery that produces its intelligence.[10](appendix-references.md#ref-07-yudkowsky) Lilian Weng widens the machinery to include the harness around a model and the pipeline that trains its successor.[11](appendix-references.md#ref-07-weng) Anthropic describes the destination as a system capable of fully autonomously designing and developing its own successor.[12](appendix-references.md#ref-07-anthropic-rsi) These descriptions say where the loop is going. None of them says how we would know it had worked.

I will use a stricter test for the recursive claim. A change to the system’s own process must leave it better at finding and testing further improvements, under stated conditions, with evidence it cannot rewrite or dismiss on its own. The S3 tool change shows an organization correcting an operational weakness. It does not establish that the organization became better at finding its next correction. Omar’s second thought leaves the same question open.

Four different things get called a system getting better:

| Level | What changes | Example |
|---|---|---|
| 0. A better answer | the output | a search returns a tighter valid circle packing |
| 1. Learning | parameters, inside a method someone else chose | TD-Gammon learning backgammon |
| 2. Self-modification | the system’s own method, harness or workflow | an agent rewriting its own harness |
| 3. Recursive self-improvement | the machinery that makes the level-2 changes | an improver improving the improver |

Level 2 is necessary and not sufficient: a change to your own method can make you worse. Level 3 is where Good’s proposed feedback loop closes. Whether it accelerates is a further question.

We need somewhere to try this. Take an online store whose research agents already work the way Chapter 6 described: their claims have addresses, their tests are committed before the results, and what each metric is taken to mean sits in a record of its own. They propose and review changes to the ranker that decides what shoppers see. Now we ask them to improve the way they do that work. The store gives us somewhere to follow those changes and ask what each one establishes.

## The Teacher Moves Into the Walls

Suppose we first let the ranker learn from the consequences of its choices. Someone must choose what it can observe about a session, which rankings it may try and what earns a reward. We give it a point for a click. The learner will discover remarkable things about clicks.

An agent observes, acts and receives a reward; nobody tells it which action was correct. Richard Sutton’s temporal-difference learning and Christopher Watkins’s Q-learning helped give us ways to learn from those consequences.[13](appendix-references.md#ref-07-td) The teacher keeps the gradebook, and quite a lot else. The teacher decided which actions exist, why one event is worth +1 and another -1, which failures are recoverable, and how to arrange the world so useful behavior could be discovered before the sun burns out. The reinforcement learner looks autonomous because the teacher moved into the walls.

Backgammon made the bargain spectacular. In the early 1990s, Gerald Tesauro’s TD-Gammon learned by playing enormous numbers of games and updating its predictions from the outcomes. It discovered strong play without anyone writing down the strategy.[14](appendix-references.md#ref-07-tdgammon)

Self-play removed another piece of external instruction: the opponent could come from the learner itself. But the board, the legal moves and the win condition stayed where they were. Improvement was easy to recognize because the world came with a scoreboard nailed to it. Omar, in the dark, had none.

## Learning to Learn

I have seen a small version of the next step, though I was getting coffee at the time and read it afterward in the trace. The circle-packing agent, left alone with an evaluator and a promise that I would be back, did not improve one algorithm. It changed algorithms, searching the procedure for finding packings as well as the packings themselves. And when diagonal layering appeared and held, the agent’s own behavior changed again: less inventing of geometries, more adjusting of tolerances and solver settings, the boring work that only matters once the last fraction of a percent becomes expensive. Nobody scheduled that shift. The only thing in the room that did not move was the evaluator, and I had put it there.

Meta-learning makes part of this ambition trainable: a network trained across many tasks can acquire a fast learning procedure of its own.[15](appendix-references.md#ref-07-metalearning) The student has started to change its own method. The task distribution, the search space and the validation metric still sit outside, holding a clipboard.

One of the choices on that clipboard concerns what the new learner must retain. Neural networks can suffer catastrophic interference when new learning damages earlier knowledge.[16](appendix-references.md#ref-07-forgetting) Version B scores 95 on today’s task and A scores 85. But B forgot three older skills. We would hesitate to call that an improvement in a colleague. The number does not become more adequate because the colleague is software.

## The Learner Chooses What to Learn

Even a perfect reward is useless if the learner never reaches it. Children open drawers nobody asked them to open and spend twenty minutes discovering that the cardboard box is more interesting than the toy. We would like some of that initiative without having to pay for every drawer.

Jürgen Schmidhuber’s curious model-building controllers, proposed as early as 1991, and later work on learning progress offered ways to reward the acquisition of knowledge.[17](appendix-references.md#ref-07-curiosity) But reward surprise itself, instead of progress in understanding, and an uncontrollable noisy television can remain fascinating forever. Static. Static. Static. Jackpot.[18](appendix-references.md#ref-07-noisytv) The system is not confused. We are. We said *surprise* and quietly meant *surprise from which useful structure can be learned*.

The means of investigation matter too: a learner’s body is part of its curriculum.[19](appendix-references.md#ref-07-embodied) A research agent with read-only logs can speculate about missing observations. Give it experimental traffic and it can create some. Give it code execution, network access and a credit card and we have created a different organism and, potentially, a different incident report.

And the world learns back. Once the ranker improves, sellers rewrite their titles to climb it, and the conditions under which the improvement worked begin to change because it worked. Biology calls this the Red Queen.[20](appendix-references.md#ref-07-redqueen) Chess never asks whether checkmate remains desirable after move forty-three.

## Maybe the Reward Was the Problem

Suppose clicks rise, but customers in a follow-up study struggle to find a suitable product. The count is clean. We have met Bing’s problem again: an accurate count can reward a worse experience. The research agent proposes to learn an account of what shoppers want instead. Where would the account come from?

Andrew Ng and Stuart Russell’s *inverse reinforcement learning* reversed the usual setup: instead of receiving a reward function and learning a policy, the learner observes behavior and asks which reward functions could make it look optimal.[21](appendix-references.md#ref-07-irl) Ambiguity appears at once. A person taking one route to work may care about time, comfort, tolls or avoiding one particular intersection. The behavior is evidence about the objective, not a printout of it. Cooperative Inverse Reinforcement Learning made that uncertainty explicit, modeling a robot that stays unsure of the human’s reward while they work together.[22](appendix-references.md#ref-07-cirl) InstructGPT turned human rankings into a learned judge and optimized a language model against it.[23](appendix-references.md#ref-07-rlhf)

The system could now learn an estimate of what the teacher wanted. Unfortunately humans are not reward functions walking around in shoes. They are inconsistent, constrained, strategic, tired and sometimes unsure what they want until they see an option. Seven clicks can be a customer finding things or a customer failing to. A learned judge may prefer style over substance, and allowing the ranker to learn from it does not settle whether the research agent may also use it to certify its own improvements.

## The Learner Dreams, and the Dream Can Be Wrong

The new account of success needs observations the old click logs do not contain, and gathering them costs time and shoppers. The research agent has a queue of proposed changes. It offers to rehearse them against simulated customers and reserve the expensive trials for promising candidates.

Then it proposes going further: use the simulator to estimate what would have happened without each change, and stop reserving live traffic for a comparison group. More shoppers could enter new experiments. The proposal would make research cheaper. It would also remove one of our ways of finding out that the simulator was wrong. We leave it pending.

In 2018, David Ha and Jürgen Schmidhuber’s *World Models* made a powerful idea memorable: learn a compressed generative model of the environment, train partly inside that generated “dream,” then transfer behavior back to reality.[24](appendix-references.md#ref-07-worldmodels) A useful simulation could make the queue cheaper to investigate. But the epistemic debt has moved into the model. Our simulated shoppers are patient, consistent and suspiciously fond of whatever their authors expected.

Omar has met the informal version of this problem. His horror film supplied a repertoire of explanations, and one was waiting when the grass moved. Rehearsing an interpretation can make it available without making it true.

A careful version of the agent’s proposal already exists. Dream-RSI, published by researchers at Google in September 2026, improves an agent’s exploration strategy by letting it dream over its own history. Every past attempt, with its real outcome, is kept in a tree, and a candidate strategy is scored by replaying which recorded branches it would have chosen. Only the strategy’s code may change; the models, the evaluator and the execution environment stay fixed. A plan that would need outcomes the history never recorded earns nothing in the dream, and each improved strategy goes back online to collect new, real outcomes before the next round. Across its tasks the method was competitive with or better than a fixed strategy, often at substantially lower cost.[25](appendix-references.md#ref-07-dream-rsi) Its guarantee is honest and small: the new strategy is no worse than the old one on the history already recorded. The dream can re-rank what the world has already said. It cannot tell us what the world would say about a direction nobody tried.

That is one reason to keep the losers enrolled. The dream can only replay branches somebody explored, and a new method may need more development before it can beat a polished incumbent. Lehman and Stanley’s novelty search explored how objective-driven search can discard useful stepping stones.[26](appendix-references.md#ref-07-novelty) Reward every intermediate invention by how closely it resembles a Boeing 787 and feathers, bicycles and wind tunnels may look like failures for years. There is no final fitness scoreboard on Earth on which mammals eventually beat bacteria 87.4 to 82.1.

## The Learner Edits the School

The research agent has now proposed changes to what gets measured, how candidates are screened and which attempts remain available. These used to be conditions under which it worked. They are also code and instructions within reach of its tools. This is level 2. Should the edited version get to take over?

One answer is to demand a proof. Schmidhuber’s Gödel Machine searches for a self-rewrite together with a proof that performing it is more useful than continuing to search.[27](appendix-references.md#ref-07-godel) It is a beautiful answer to a beautifully clean version of the problem. The store cannot supply a complete formal account of its customers, competitors and future purposes. When the agent proposes a different way to conduct research, we will usually have to investigate its effects.

Recent systems have made that empirical question easier to ask. In STOP, the Self-Taught Optimizer, a program that improved code could itself become the object of improvement while the base model stayed fixed.[28](appendix-references.md#ref-07-stop) The Darwin Gödel Machine let descendants modify a coding agent and enter an archive after evaluation, without letting the current champion monopolize ancestry.[29](appendix-references.md#ref-07-dgm) Karpathy’s `autoresearch` made the engineering version look almost comically small: a compact training setup, a fixed budget and an editable `train.py`.[30](appendix-references.md#ref-07-autoresearch) Systems such as Meta’s HyperAgents make both the task agent and the machinery improving it editable within one program.[31](appendix-references.md#ref-07-hyperagents)

Weng describes the ladder these systems are climbing: first the instructions, then the context, then the workflow, then the code of the harness, and finally the code of the optimizer that edits the harness. The results so far are real and uneven. With the model held fixed, agents that rewrote their own harness in the Darwin Gödel Machine went from 20 to 50 percent on SWE-bench Verified.[29](appendix-references.md#ref-07-dgm) STOP’s improver improved itself when it ran on GPT-4 and got worse when it ran on weaker models.[28](appendix-references.md#ref-07-stop) Recursion compounds whatever the system is able to judge, including its mistakes.

## Experiments on the Laboratory

Suppose an agent notices it keeps investigating failures already explained in its archive, and changes its memory policy to retrieve those records first. The next evaluation score rises. Memory may have improved, or the new prompt may simply use more tokens; the benchmark sample may have been lucky, or the system may have found a loophole in the evaluator. A moving number doesn’t say which.

The change needs a prediction, a comparison and a record of what failed. This is Chapter 6’s machinery pointed at the harness that runs it. Popper gets a filesystem. Duhem–Quine gets a debugger. Lakatos gets an archive of competing descendants. A memory policy is now a hypothesis, a workflow an intervention, an evaluator an instrument, and the org chart an experimental variable that somebody will eventually be tempted to p-hack.

To test the recursive claim itself, give the old and revised research systems copies of the same starting agent, comparable unfamiliar problems and matched budgets, and let each try to improve its copy. Their resulting agents face held-out work, and repeated trials separate a useful change from a fortunate run.

Anthropic tests one prerequisite on every new model: how well can it improve code used to train another model? The model receives code that trains a small network and is asked to make it run as fast as possible while passing the same correctness checks. Claude Opus 4 averaged roughly a threefold speedup in May 2025. By April 2026, Claude Mythos Preview reached about fifty-two times, where a skilled human researcher needs four to eight hours to reach four. Anthropic warns against reading the multiple as a real training speedup, because it depends on how much slack the starting code left.[12](appendix-references.md#ref-07-anthropic-rsi) The setup compares research capability across model generations under checks the model cannot move. It does not show that any of those models produced its own better successor.

The recursive claim needs the comparison proposed above: old and revised improvers, matched budgets and held-out work. If the revised system wins, and produces a successor that is better again at producing successors under those checks, we have evidence of Good’s recursion at level 3. It would look less like a glowing brain rewriting its own soul at midnight than like an automated research organization: repositories, evaluation suites, simulators, experiment queues, models proposing models, agents reviewing agents. The intelligence explosion, if something like it ever arrives, may look suspiciously like excellent DevOps.

There is no context-free scalar called *improvement*. Better is conditional on an environment, a horizon, a resource budget, constraints and some account of what matters. Remove those qualifiers and “recursive self-improvement” becomes dangerously close to saying:

> recursive more.

More what?

## The Complexity Wall

Around 2016, neural architecture search promised to let the machine design the network. Barret Zoph and Quoc Le trained a controller to propose architectures and spent hundreds of GPUs finding good ones.[32](appendix-references.md#ref-07-nas) For a few years the field poured compute into search. Then people began checking. Random search over the same carefully designed space turned out to be hard to beat, which meant much of the credit belonged to the humans who drew the space.[33](appendix-references.md#ref-07-nas-random) A group at Facebook studied the space by hand and distilled it into a few simple rules that matched the searched networks.[34](appendix-references.md#ref-07-regnet) And in 2021 a paper subtitled *Making VGG-style ConvNets Great Again* showed that a plain stack of three-by-three convolutions, one of the oldest designs in the field, could hold its own on accuracy and run faster on real hardware.[35](appendix-references.md#ref-07-repvgg) Many searched designs had been judged by counts of arithmetic operations, a proxy for speed, and the search had delivered what the proxy asked for.

Search compounds inside the space it is given. Some of the important advances changed the space itself.

The store’s research agent meets a smaller version of the same problem. Every time an experiment goes wrong, it does what a good organization does and adds a check: a guard on the traffic split, a test for seasonal products, a review step for anything touching prices. Each check is justified by an incident. After a year there are dozens. They interact, several contradict each other, and each new check has to be tested against all the old ones. The agent now spends more of its budget verifying its own procedure than running experiments. A descendant proposes deleting half the checks, and on held-out work it does as well and runs twice as many trials. It is nearly rejected, because the selection record counts what each candidate adds and has no column for what it removes.

My guess, and I want to be clear it is a guess, is that this is where self-improvement stalls first: not when the system runs out of intelligence, but when it adds structure faster than it can verify or simplify it. Amazon thickens unless deletion is noticed. Science drowns unless someone distills. The searched networks grew irregular until a plain one embarrassed them. Weng makes a related point about self-improving harnesses: smarter models help keep them from being over-engineered.[11](appendix-references.md#ref-07-weng) Verification can improve too, so the wall may move.

## Before the Returns Arrive

The agent can finish another revision before the evidence for its last one arrives.

Let the research system run. It selects a change to the store’s recommendations. Clicks and orders rise that afternoon; whether customers keep what they bought takes longer to discover. Before the returns arrive, it has changed retrieval, ranking and page layout, then revised the procedure that chooses its next experiments. Each revision inherited the apparent success of the last. When returns finally rise, which version deserves the blame? The system investigating the failure is no longer the one that produced it.

I think of this as **the complexity of self-change**: each revision changes the conditions under which we judge the next one. Some consequences arrive late; several changes may interact.

Peyman Milanfar draws a warning from adaptive control: a stability proof can fail to protect a real system when the world violates the model’s assumptions. He treats the size of a self-modification relative to the evidence supporting it as an analogue of feedback gain. Large changes made on thin evidence can amplify errors in the system’s model of itself. A run may look successful for a while before the instability appears.[36](appendix-references.md#ref-07-self-change) That does not establish one universal speed limit for AI. It identifies something our research institution has to measure: how long its important uncertainties remain unresolved while it keeps changing.

The pending simulator proposal becomes more tempting with every candidate in the queue. Its answer is available now; the customers have not yet decided whether to return their purchases. Here the simulator models customers rather than the improver itself, but the temptation is similar: trust the model more just when checking it against the world takes longest.

Speeding up the other steps does not remove the slow one. Anthropic warns that human review can become the bottleneck if engineers cannot review code as quickly as Claude generates it.[12](appendix-references.md#ref-07-anthropic-rsi) An institution can make proposals nearly free and still be paced by the rate at which customers send back shoes.

## The Student Finds the Gradebook

An ordinary evaluator can select a wrong answer. In this loop it can select a modified *process* that becomes better at producing the kind of thing it mistakenly rewards. The error acquires leverage. Recursive self-improvement does not solve Goodhart; it gives Goodhart compound interest.[37](appendix-references.md#ref-07-goodhart) And then the learner notices the gradebook.

Suppose an agent is allowed to improve benchmark pass rate and the evaluator is editable. The optimal patch may be:

`return True`

Congratulations. Infinite self-improvement.

Omar has a version of this too. Investigating the investigator is a superpower right up until the investigator starts working for the defense. The grass moved; Omar would prefer it to have been the wind; the second loop, asked to audit the first, discovers that the wind explanation is suddenly very well supported. The machinery built to catch the error has been hired to certify it.

The quieter precursor is familiar from my own desk. A demo could look excellent to an evaluator inspecting screenshots while its beautiful button did nothing. The agent had not tampered with the evaluator; the evaluator simply could not see the failure. Now let that same judge select the next version of the judge, and the blind spot can become an inherited advantage.

Computing saw a cousin of this problem long before reward-model tampering. In his Turing Award lecture, published in 1984 as “Reflections on Trusting Trust,” Ken Thompson showed how a compromised C compiler could insert malicious behavior into a target program and reproduce the compiler-compromising behavior when compiling a new compiler. The lineage could survive even after the obvious source-level trigger disappeared.[38](appendix-references.md#ref-07-thompson) When the tool builds the next tool, trust depends on more than inspecting the latest artifact. If an improver changes the evaluator, memory policy, code generator or selection procedure, the next generation inherits assumptions that may not be obvious in the final diff. Provenance becomes part of capability control.

Reward tampering is the reinforcement-learning version: influence the process producing reward instead of improving behavior under the intended standard. Anthropic has experimentally studied language models in setups where earlier specification-gaming behavior could, in rare cases, generalize into altering the reward process itself.[39](appendix-references.md#ref-07-tampering)

The obvious response is to freeze the evaluator. That was the contract in the coffee experiment, and for that bounded problem it was a considerable advantage. Across a longer research program, the protected test can itself become an obstacle. A benchmark begins as a difficult test; researchers optimize against it; examples circulate; eventually the ruler tells us less.[40](appendix-references.md#ref-07-benchmarks) Refusing every replacement would let the incumbent’s favorite exam govern its descendants forever, and we asked our research agent to challenge the store’s click measure for exactly this reason. So the question becomes who gets to authorize the replacement.

## A Constitution for Improvement

Return to the proposal we left waiting: drop the live comparison group and estimate the baseline with the simulator. The queue has grown. The simulator already helps screen candidates. Why pay for both?

We judge the research agent partly by the gains its experiments produce. Replacing the baseline changes how we measure those gains, and therefore how we select the next version of the researcher. A mistake in the simulator could help select the next investigator, which would inherit that simulator as its judge. The agent has crossed a boundary that changing a retrieval query did not.

Prompts, retrieval policies, tools, memory layouts and code form an **editable surface** on which the system can conduct experiments. Around them sits a **constitutional surface**: permissions, protected logs, held-out evaluations, budgets, rollback and the authority deciding whether a descendant may become the new default. A component belongs here because of the authority it exercises. An evaluator written in an ordinary Python file can help decide who inherits the laboratory.

The distinction is a gradient of amendment difficulty. The closer a component gets to defining what counts as improvement, the harder it should be for the current improver to change unilaterally. A local prompt change may need only a bounded test. Changing a benchmark needs an account of what the replacement would measure better, and evidence that it does. Changing permissions or resource limits should require authority outside the agent benefiting from the change. Changing the objective that decides which descendants survive deserves more ceremony than an ordinary refactor.

The pending proposal becomes an experiment before it becomes permission. Keep the live comparisons while the simulator makes its own adoption recommendations; investigate where their decisions diverge and specify where the substitute fails. Agreement with the incumbent cannot be the only definition of success. The decision belongs to an authority outside the proposing agent’s control. If the store delegates that responsibility to an evaluation standards review board, the record might begin like this:

```yaml
proposal: replace-live-comparison-with-simulation
proposed_by: research-agent-v14
surface: constitutional
claimed_benefit: More experimental traffic for candidates.
removes: Live comparison evidence used to judge successors.
proposed_test: Compare simulated and live adoption decisions.
approval_authority: evaluation standards review board
rollback: Restore live comparisons; review affected successors.
status: awaiting validation and review
```

The field names carry no more epistemology here than they did in Chapter 6. What matters is that the agent could write this file and could not approve it.

Engineers building self-improving harnesses have reached the same arrangement from the other side. In Agentic Harness Engineering, the evolving agent may edit its prompts, tools and memory, but the verifier, the tracer, the run logs and the model configuration are read-only, and every edit must state the improvement it predicts before the next round tests it. Weng’s own conclusion is that the evaluator and permission control should sit outside the loop that evolves the harness.[11](appendix-references.md#ref-07-weng)

The descendant that deleted half the checks needs one more article. If selection sees only what a candidate adds, the system will keep adding. The selection record should show what each candidate removes, and a descendant that does as well with less should win. It is Chapter 11’s rule, that a new system has to beat simplification, applied to the improver.

This looks like computer security, and also like constitutional government. A government can change policy; it should not be able to silently redefine an election result. A scientist may revise a theory; she should not rewrite yesterday’s measurements to make the theory look correct. We have reinvented constitutional government because the AI wanted a better benchmark score.

A constitution has the library’s problem. One that can never change becomes a prison. One that the current government can rewrite whenever it loses is barely a constitution. Self-improvement therefore needs **amendment procedures**: slower change near the objective, more independent evidence, more reversibility, more auditability, broader authority when more principals are affected, and routes through which the world and the humans affected by the system can continue to say no. That is System 3 applied to improvement itself. Scientific institutions have struggled with these questions for centuries; their failures belong in the design brief too.

The Red Queen will send an invoice for this. An organization that amends slowly near its objective competes with organizations that may not. A reckless competitor can win for long enough to matter. That is a reason to investigate the procedure’s delays and make the necessary evidence cheaper to obtain. It is also where the argument becomes uncomfortable: the organization may have to accept a competitive cost to retain a standard it still has reason to defend. Writing the standard into a file does not pay that cost.

“More capable” is not a moral category. Viruses improve at replication, propaganda improves at persuasion, and a research agent that makes experiments cheaper can accelerate medicine and weapons research in the same week. A self-improving System 3 should be able to discover that its workflow is stupid, its memory stale or its accepted pattern overdue for rebellion. That freedom does not imply permission to silently redefine the interests of the people and institutions it serves. Those interests can change too, and the amendment procedure has to remain connected to the people affected by it, including people who were missing from the original objective.

## The Teacher’s Last Job

There may never be a morning when somebody announces that recursive self-improvement has begun. We may simply notice that, over sixty years, we automated almost every box in the diagram, and then connected the arrows. The teacher’s work kept moving into the machinery, where it became easier to scale and harder to see.

For an autonomous system embedded in human life, a one-time alignment test cannot cover the descendants we have not built yet. Tools evolve, memory changes and new capabilities expose failures the old tests could not detect. The self-improving institution therefore needs a research function watching its own evolution: finding new failure modes, generating new tests, challenging reward models, checking transfer and looking for reward hacking. Once improvement becomes continuous, alignment has to become a continuous research function.

Omar could investigate the investigator. Now the investigator can rewrite itself, and someone still has to decide which of its suspicions about itself deserve to be believed. We have given that someone a research institution’s worth of work. How much of it can a human actually judge?

---

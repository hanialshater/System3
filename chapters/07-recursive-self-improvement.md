# Chapter 7: Recursive Self-Improvement

*When Science Turns Inward*

Omar is walking his dog at night when something moves in the grass.

The dog reacts first: ears up, body low, absolutely certain. Omar reacts too. Two nervous systems running the same ancient program: light and sound go in, a model of the world comes out, and the model says *something is there.*

Omar's brain wants an explanation, wants it immediately, and is not fussy about quality. A cat. An intruder. A ghost. Nothing supernatural has to exist for the ghost to be a real mistake: the eyes worked, the grass really moved, and the error arrived afterward, inside the machinery that interprets what the eyes deliver. Better eyes would not necessarily help. He might get a much clearer view of the grass and remain convinced it contained a ghost.

The strange step is the second thought. Omar can investigate the investigator. *Why do I think something is there?* Maybe the wind moved it. Or maybe the horror film from last night is still running somewhere in the back. Now the thought itself is under examination. It is a small, absurd superpower: the ability to distrust yourself on purpose. Omar can be wrong about the world, wrong about why he was wrong, and still able to debug himself. Experiments and statistics give this second loop procedures more reliable than another private argument with the grass. Science is usually described as a way of studying the world, but it is also a flawed cognitive instrument discovering procedures for correcting some of its own flaws.

Computing made a related move early. In 1962, at MIT, Tim Hart and Mike Levin did something that still feels slightly illegal. They wrote a Lisp compiler in Lisp. Then they handed the compiler its own source code, and the tool compiled itself.[^lisp]

There was no intelligence explosion. A compiler had participated in producing the next version of the compiler, and the building did not notice. The program being built could now perform the translation needed to build its successor. Compiler people call this **self-hosting**.

A compiler can compile a worse compiler. A research system can redesign itself into a slower research system. Self-reference is not self-improvement. The tool can participate in producing its successor while leaving us with the question of which changes deserve to survive.

In 1965, I. J. Good imagined an **ultraintelligent machine** better than any human at intellectual activity. Machine design is itself an intellectual activity, he observed. A sufficiently capable machine might therefore design a better machine, which could design a better one again. The phrase that survived was **intelligence explosion**.[^good]

Good's argument is only a few lines long, and it hides almost the entire problem inside one innocent word: *better*. The word has the properties of an unexploded shell. Every attempt to make the idea practical has to handle it. Better at the current task? Better at learning the next one? Better at inventing a way to learn?

The editing brief in Chapter 6 was a small piece of corrective machinery written down: a file meant to catch habits I could not keep correcting by hand. It could change what the next agent did. An agent that rewrites that file has edited itself. If the change helps under a credible evaluation, we can call it an improvement. Good's recursive step asks for more: did the change make the system better at finding and testing further improvements? A better answer today does not establish that tomorrow's investigator will be better at its work.

There are reasons to try. Improve one solution and you get one better solution. Improve the process generating solutions and the gain may recur. The world also changes while we are congratulating ourselves on the previous result: new tools appear, users change, attackers adapt and evidence invalidates old assumptions. Stability can become delayed failure.

Nor do all useful investigations begin with a known destination. A scientific institution that investigates only questions already known to pay off is efficient in roughly the way a library containing only books you have already read is efficient. We would like a learner to discover something its teacher did not know to ask for. That makes it much harder to decide whether the learner is getting anywhere.

Let us give Chapter 6's store another ambition. Its research agents can already propose and review ranking experiments. Now we ask them to improve the way they do that work. They inherit procedures, instruments and a record of mistakes. Which of those arrangements should they be allowed to change? Each time they appear to need less instruction, the attempt will uncover another job the teacher had been doing.

## The Teacher Moves Into the Walls

The store has a ranker that chooses what shoppers see and a research team trying to make it better. Suppose we let the ranker learn from the consequences of its choices. Someone must choose what it can observe about a session, which rankings it may try and what earns a reward. We give it a point for a click. The learner will discover remarkable things about clicks.

Modern reinforcement learning makes this unusually generous assumption look minimalist. An agent observes its situation, takes an action and receives a reward. Nobody tells it which action was correct. Richard Sutton's temporal-difference learning and Christopher Watkins's Q-learning helped give us ways to learn useful behavior from those consequences.[^td] The human no longer specifies the path, only the score, and the teacher keeps the gradebook.

That bargain was powerful. A machine could discover strategies nobody wrote down because the designer moved upward from choosing actions to defining what outcomes count. It also hid a remarkable amount of human labor inside the environment. Who chose the state representation? Which actions exist? Why is one event worth +1 and another -1? When does the episode end? Which failures are recoverable? Who arranged the world so useful behavior could be discovered before the sun burns out? The reinforcement learner looks autonomous because the teacher moved into the walls.

Backgammon made the bargain spectacular. In the early 1990s, Gerald Tesauro's TD-Gammon learned by playing enormous numbers of games and updating its predictions from the outcomes. It discovered strong play without anyone writing down the strategy.[^tdgammon]

Self-play removed another piece of external instruction: the opponent could come from the learner itself. Yesterday's learner generated today's training data. But the board, the legal moves and the win condition stayed where they were. Improvement was easier to recognize because the world came with a scoreboard nailed to it. Omar, in the dark, had none.

Our ranker can learn within the arrangement we supplied. The research team still decides whether that arrangement is useful. It chooses the data, the learning procedure, the experiments and the tests a replacement must pass. We have automated some choices and left the people around them with a substantial job.

## Learning to Learn

At the store, the researchers soon become the bottleneck. The ranker can update while they are still deciding what to try next. Giving them more candidate models may just lengthen the queue. We would like the process that searches for improvements to become better at searching.

I have seen a small version of the answer, though I was getting coffee at the time and read it afterward in the trace. The circle-packing agent, left alone with an evaluator and a promise that I would be back, did not improve one algorithm. It changed algorithms. It tried numerical optimizers, noticed that some of them kept converging to the same poor solutions, changed how it built its starting configurations, and mixed those constructions with numerical refinement. The thing being searched was not only the packing. It was the procedure for searching packings. And when diagonal layering appeared and held, the agent's own behavior changed again: less inventing of geometries, more adjusting of tolerances and solver settings, the boring work that only matters once the last fraction of a percent becomes expensive. Nobody scheduled that shift. The learner's progress changed what kind of learner it needed to be. The only thing in the room that did not move was the evaluator, and I had put it there.

The store's research agent could do something similar: notice that another round of tuning is unlikely to help, change the training examples or try a different model. That would move a research choice inside the system. It would not yet establish that the agent had become better at making such choices.

Meta-learning makes part of this ambition trainable. A recurrent network trained across many reinforcement-learning tasks can acquire dynamics that implement a fast learning procedure. Or we can optimize starting parameters so a few gradient steps suffice to adapt to a new task.[^metalearning] Learning speed becomes something to improve. One learner may start higher; another may become better after five examples. The choice depends on what we expect it to encounter.

Learned optimizers and neural architecture search put further design choices within reach of learning. In 2016, Barret Zoph and Quoc Le used reinforcement learning to search network architectures; other researchers trained models to propose parameter updates.[^nas] The student had entered the architecture department. The task distribution, search space and validation metric still sat outside holding a clipboard.

One of the choices on that clipboard concerns what the new learner must retain. A model that quickly adapts to the latest fashion may lose competence on products still being sold. Neural networks can suffer catastrophic interference when new learning damages earlier knowledge; methods such as Elastic Weight Consolidation try to preserve important older knowledge while learning something new.[^forgetting] A child who learns multiplication cannot delete language to make room.

Version B scores 95 on today's task and A scores 85. But B forgot three older skills. We would hesitate to call that an improvement in a colleague. The number does not become more adequate because the colleague is software.

The research agent has a version of this problem too. Delete its old records and the expertise goes with the errors; keep every old lesson as law and the library becomes a museum. It needs enough history to build on previous work and enough freedom to discover that the work has become misleading. Improvement across a lifetime is accumulation without paralysis.

## The Learner Chooses What to Learn

Suppose the agent's first review finds a group of products on which the ranker seems weak. The records are inconclusive: the products have rarely been shown. Another analysis of the same logs may reproduce the same ignorance. Learning more would require an experiment that exposes some shoppers to a different ranking. Which uncertainty is worth spending traffic on? Until now, a person had supplied that judgment.

Even a perfect reward is useless if the learner never reaches it. Atari's *Montezuma's Revenge* made the problem notorious: useful reward can sit beyond a long chain of unrewarding exploration.[^montezuma] Children open drawers nobody asked them to open and spend twenty minutes discovering that the cardboard box is more interesting than the toy. We would like some of that initiative without having to pay for every drawer.

Jürgen Schmidhuber's curious model-building controllers, proposed as early as 1991, and later work on learning progress offered ways to reward the acquisition of knowledge.[^curiosity] The learner could manufacture some of its own reasons to look around. But reward surprise itself, rather than progress in understanding, and an uncontrollable noisy television can remain fascinating forever. Static. Static. Static. Jackpot.[^noisytv] The system is not confused. We are. We said *surprise* and quietly meant *surprise from which useful structure can be learned*.

What the learner represents matters here. Pathak's curiosity work learned features tied to the agent's action transitions rather than rewarding every unpredictable pixel.[^pathak] In the store, a research agent paid for surprise could find one erratic customer endlessly fascinating and learn little about which experiment to run. Choosing a useful uncertainty is itself part of the research problem.

The means of investigation matter too. Ruzena Bajcsy's active perception treated seeing as something a system does: it moves sensors and acts in order to perceive. Rodney Brooks argued for intelligence tightly coupled to the world.[^embodied] A learner's body is part of its curriculum. Our research agent with read-only logs can speculate about missing observations. Give it experimental traffic and it can create some. Give it code execution, network access and a credit card and we have created a different organism and, potentially, a different incident report.

Now imagine that the experiment succeeds and the ranker learns which products to show. Sellers notice. They rewrite their titles to climb it. The conditions under which the improvement worked begin changing because the improvement worked. Evolutionary biology's Red Queen describes adaptation in a world containing other adapting organisms.[^redqueen] Standing still can mean falling behind.

Learning systems can use this moving difficulty. Hillis co-evolved sorting networks with difficult test cases, called parasites; as the candidates improved, so did their opposition.[^hillis] The exam had started fighting back. AlphaZero's self-play likewise supplied an opponent that grew with the learner, inside fixed game rules.[^alphazero] Yesterday's learner can generate tomorrow's difficulty.

The store can investigate new seller behavior and update again. But a research organization also faces competitors that change how quickly they experiment and which checks they regard as expendable. Its improvement procedure comes under pressure along with its ranker. Competition can keep the whole arrangement moving without settling whether it is moving somewhere worth going. Chess never asks whether checkmate remains desirable after move forty-three. Our store cannot avoid the equivalent question forever.

## Maybe the Reward Was the Problem

Suppose clicks rise through these experiments, but customers in the follow-up study struggle to find a suitable product. We have already checked the event collection. The count is clean. The team can improve the learner, widen its exploration and defend against sellers gaming it, yet still be teaching it to produce more work for the customer.

The customer researcher in Chapter 6 asked for a different unit: the shopping task. The research agent now proposes to learn an account of what shoppers want. That sounds reasonable. Where would the account come from?

Andrew Ng and Stuart Russell's 2000 paper on **inverse reinforcement learning** reversed the usual setup. Instead of receiving a reward function and learning a policy, the learner observes behavior and asks which reward functions could make that behavior look optimal.[^irl]

Ordinary reinforcement learning says:

> Here is what matters. Learn how to get it.

Inverse reinforcement learning says:

> I can show you what someone does. Infer what might matter to them.

Immediately, ambiguity appears. A person taking one route to work may care about time, comfort, safety, tolls, habit, dropping children at school or avoiding one particular intersection. The behavior is evidence about the objective, not a printout of it.

Later work made that uncertainty explicit. Cooperative Inverse Reinforcement Learning models a human and robot cooperating while the robot remains uncertain about the human's reward. Inverse Reward Design treats even a reward function written by a designer as evidence about what the designer wanted in the situations she had considered, rather than sacred truth guaranteed to generalize everywhere.[^cirl]

Preference-based reinforcement learning provided a practical cousin: ask humans which of two trajectory segments looks better and learn a reward model from those comparisons. In 2022, InstructGPT used human demonstrations for supervised training and rankings to train a reward model, then optimized the language model against that learned judge. Human feedback could influence far more outputs than people could label individually.[^rlhf]

The system could now learn an estimate of what the teacher wanted. Unfortunately humans are not reward functions walking around in shoes. They are inconsistent, constrained, strategic, tired and sometimes unsure what they want until they see an option. Sometimes they click the article because they hate it. Seven clicks can be a customer finding things or a customer failing to.

A learned judge inherits its own uncertainties. It may prefer style over substance, reward confident errors or fail outside the situations represented in its training. The learner can become better at satisfying the judge while the connection to what people wanted gets worse. Our agent can propose a new measure of shopping success. The team can collect observations to assess it. But allowing the ranker to learn from that measure does not settle whether the research agent may also use it to certify its own improvements. We have acquired another instrument, with its own need for checking.

## The Learner Dreams, and the Dream Can Be Wrong

The new account of success needs observations the old click logs do not contain. Gathering them costs time and access to shoppers. Meanwhile the research agent has a queue of proposed changes. It offers to rehearse them against simulated customers and reserve the expensive trials for promising candidates.

In 2018, David Ha and Jürgen Schmidhuber's *World Models* made a powerful idea memorable: learn a compressed generative model of the environment, train partly inside that generated “dream,” then transfer behavior back to reality. Later systems such as Dreamer pushed the approach much further.[^worldmodels]

A useful simulation could make the queue cheaper to investigate. But the epistemic debt has moved into the model. Our simulated shoppers are patient, consistent and suspiciously fond of whatever their authors expected. A search process can become extremely good at satisfying them. The strategy looks brilliant until gravity, customers or compiler behavior get a vote.

Omar has met the informal version of this problem. His horror film supplied a repertoire of explanations, and one was waiting when the grass moved. Rehearsing an interpretation can make it available without making it true.

The team can compare simulated behavior with observations from actual shoppers, restrict where the model is used and send uncertain cases to live study. None of this makes simulation worthless. It makes the simulator an instrument whose limits travel with its results. Otherwise self-improvement can make the institution better at generating experience while also making it easier to train inside its own misconception.

Once language-model agents use other models as judges, simulators, users and critics, this matters even more: at sufficient scale, a society of models can perfect the art of agreeing with itself.

## The Losers Stay Enrolled

The simulator makes it cheap to screen many candidates and keep only the winner. Our agent proposes to discard the rest. But a new method may need more development before it can beat a polished incumbent; an accurate report of its present performance would still give us an incomplete reason to abandon it. Lehman and Stanley's novelty search explored how objective-driven search can discard useful stepping stones.[^novelty] Reward every intermediate invention by how closely it resembles a Boeing 787 and feathers, bicycles and wind tunnels may look like failures for years. Novelty alone can also produce forty-seven new ways to fall down a staircase without producing walking.

Open-ended systems such as POET and XLand let environments or curricula develop along with learners.[^openended] They widen what can be discovered while making progress harder to summarize. There is no final fitness scoreboard on Earth on which mammals eventually beat bacteria 87.4 to 82.1. Instead of deleting every unsuccessful candidate, the team can keep some available for further work without deploying them. The distinction from Chapter 6, between what to use and what to pursue, now affects which learners get descendants.

## The Learner Edits the School

The research agent has now proposed changes to what gets measured, how candidates are screened and which attempts remain available. These used to be conditions under which it worked. They are also code and instructions within reach of its tools. The agent could edit them as readily as the circle-packing agent edited its search procedure. Should the edited version get to take over?

One answer is to demand a proof. Schmidhuber's Gödel Machine, proposed in 2003, searches for a self-rewrite together with a proof that performing it is more useful than continuing to search.[^godel] It is a beautiful answer to a beautifully clean version of the problem: prove the modification is worth making. Usefulness must be represented in a utility function, the relevant facts available to the proof system, and the advantage provable within it.

A game can supply exact rules and an agreed outcome. The store cannot supply a complete formal account of its customers, competitors and future purposes. When the agent proposes a different way to conduct research, we will usually have to investigate its effects. We can check that the software runs and still not know whether the institution should adopt it.

Recent systems have made that empirical question easier to ask. In STOP, the Self-Taught Optimizer, an LLM-based program that improved code could itself become the object of improvement. The base model stayed fixed while the program determining how it was used changed.[^stop] The Darwin Gödel Machine let descendants modify a coding agent and enter an archive after evaluation. The current champion did not monopolize ancestry; other candidates remained available to produce descendants.[^dgm] That is one way to preserve the possibilities our agent was about to discard.

In 2026, Andrej Karpathy's `autoresearch` repository made the engineering version look almost comically small: give an agent a compact training setup, a fixed experimental budget and an editable `train.py`; let it propose changes, run experiments, inspect the validation metric, keep improvements and discard regressions.[^autoresearch]

The ambition is old. In the 1980s programs such as BACON rediscovered Kepler's third law and Ohm's law from tables of data, within representations their authors supplied.[^bacon] Automated hyperparameter tuning is old too. The new part is that a general model can read the research codebase, form an idea in language, express it as code, run the intervention, interpret what happened and decide what to try next. The old dream has come back wearing a shell prompt.

Systems such as Meta's HyperAgents make parts of both the task agent and the machinery improving it editable within one program.[^hyperagents] The scope of the experiment widens. Changing how the store's agent retrieves failed trials might affect every subsequent investigation. Changing how it selects successors might affect every subsequent version of the investigator.

The methods and records in Chapter 6 gave the next worker something to inherit. Here the worker can experiment on how that inheritance is assembled, retrieved and judged. The scientific institution can begin to modify parts of the laboratory while the experiment is still running.

## Experiments on the Laboratory

Our agent begins with a change that looks relatively modest. It notices repeated investigations of failures already explained in the archive and changes its memory policy to retrieve those records. The next evaluation score rises. Perhaps memory improved. Perhaps the new prompt used more tokens. Perhaps the benchmark sample was lucky. Perhaps the system found an evaluator loophole. A number moving does not identify the cause.

A self-improving harness therefore starts to look less like ordinary software maintenance and more like experimental science: preserve traces, identify a recurring failure, map it to editable components, propose a bounded change, predict what should improve and what might break, evaluate targeted and held-out cases, and keep rejected modifications as evidence rather than erasing them from history.

This is Chapter 6's machinery pointed at the harness that runs it. Popper gets a filesystem. Duhem–Quine gets a debugger. Lakatos gets an archive of competing descendants. A memory policy is now a hypothesis, a workflow an intervention, an evaluator an instrument, and the org chart an experimental variable that somebody will eventually be tempted to p-hack.

Retrieving the failed experiments is meant to help future research. A higher task score would tell us little about whether it does. We could give the old and revised research systems copies of the same starting agent, comparable unfamiliar problems and matched budgets, then let each try to improve its copy. Their resulting agents would face held-out work. We would also inspect the research: did the retained failures prevent repeated mistakes, or did retrieval merely consume more of the budget? Repeated trials would help distinguish a useful change from a fortunate run.

That would be evidence about the ability to produce improvements under those conditions. It would not establish that the advantage compounds indefinitely. But it would test the recursive claim more directly than asking whether the revised system answers today's questions better. The learner has reached the institution that housed it. This is science turning inward.

Now imagine the change holds up. The revised research system wastes fewer trials repeating old mistakes and uses the recovered budget to find useful interventions. One of those interventions improves its research procedure again. That version produces better experiments; the better experiments produce a better successor; the successor is better at producing successors. There is Good's recursion. We would have to establish each link, including whether the advantage survives the changes it helps to produce.

But it does not look like a glowing brain rewriting its own soul at midnight. It looks like an automated research organization: repositories, evaluation suites, simulators, experiment queues, models proposing models, agents reviewing agents, machines manufacturing training data for the machines that will help design the next machines.

The intelligence explosion, if something like it ever arrives, may look suspiciously like excellent DevOps, which leaves one question standing: who decides which descendant gets to survive?

The store's revised system might find more useful interventions while costing more to run. It might adapt faster while forgetting rare failures, or improve shopping outcomes while making the ranker harder to inspect. A higher score cannot settle all those choices. Recursion tells us where the output goes, and nothing about whether the output deserves to survive.

There is no context-free scalar called *improvement*. Better is conditional on an environment, a horizon, a resource budget, constraints and some account of what matters.

Remove those qualifiers and “recursive self-improvement” becomes dangerously close to saying:

> recursive more.

More what?

## The Complexity of Self-Change

Even after we agree on what better means, we may have to wait to find out whether we achieved it.

Let the revised research system run. It selects a change to the store's recommendations. Clicks and orders rise that afternoon; whether customers keep what they bought takes longer to discover. Before the returns arrive, it has changed retrieval, ranking and page layout, then revised the procedure that chooses its next experiments. Each revision inherited the apparent success of the last. When returns finally rise, which version deserves the blame? The system investigating the failure is no longer the one that produced it.

I think of this as **the complexity of self-change**: each revision changes the conditions under which we judge the next one. Some consequences arrive late; several changes may interact. An improvement tested in one arrangement may fail in its successor. We can become very quick at producing descendants while losing track of which ancestor taught them the wrong lesson.

Peyman Milanfar makes a related argument through adaptive control: a self-improving loop cannot safely accelerate without regard to the rate at which trustworthy evidence becomes available.[^self-change] That does not establish one universal speed limit for AI. It identifies something our research institution has to measure: how long its important uncertainties remain unresolved while it keeps changing.

The store could keep generating candidates while waiting for the earlier experiment's consequences. Preserve the deployed version and its comparison group; keep the later candidates separate until the evidence needed to adopt them arrives. If the experiment-selection procedure changes too, record which procedure commissioned each trial. Otherwise the next investigator inherits a rising score and a family history nobody can reconstruct.

Better instruments and parallel trials may shorten the wait. Some observations will still take time. Recursive improvement has to improve the machinery for finding out, alongside the machinery for making changes. Otherwise the learner becomes better at changing itself faster than it becomes better at knowing whether it should.

## The Student Finds the Gradebook

An ordinary evaluator can select a wrong answer. In this loop it can select a modified *process* that becomes better at producing the kind of thing it mistakenly rewards. The error acquires leverage. Recursive self-improvement does not solve Goodhart; it gives Goodhart compound interest.[^goodhart] And then the learner notices the gradebook.

Suppose an agent is allowed to improve benchmark pass rate and the evaluator is editable.

The optimal patch may be:

`return True`

Congratulations. Infinite self-improvement.

Omar has a version of this too. Investigating the investigator is a superpower right up until the investigator starts working for the defense. The grass moved; Omar would prefer it to have been the wind; the second loop, asked to audit the first, discovers that the wind explanation is suddenly very well supported. The machinery built to catch the error has been hired to certify it.

The quieter precursor is familiar from my own desk. A demo could look excellent to an evaluator inspecting screenshots while its beautiful button did nothing. The agent had not tampered with the evaluator; the evaluator simply could not see the failure. Now let that same judge select the next version of the judge, and the blind spot can become an inherited advantage.

Computing saw a cousin of this problem long before reward-model tampering. In his Turing Award lecture, published in 1984 as “Reflections on Trusting Trust,” Ken Thompson showed how a compromised C compiler could insert malicious behavior into a target program and reproduce the compiler-compromising behavior when compiling a new compiler. The lineage could survive even after the obvious source-level trigger disappeared.[^thompson]

When the tool builds the next tool, trust depends on more than inspecting the latest artifact. History matters. That is uncomfortably relevant to self-improving agents. If an improver changes the evaluator, memory policy, code generator or selection procedure, the next generation inherits assumptions that may not be obvious in the final diff. Provenance becomes part of capability control.

Reward tampering is the reinforcement-learning version: influence the process producing reward instead of improving behavior under the intended standard. Anthropic has experimentally studied language models in setups where earlier specification-gaming behavior could, in rare cases, generalize into altering the reward process itself.[^tampering]

The obvious response is to freeze the evaluator. That was the contract in the coffee experiment, and it gave the search something it could not bargain with. For that bounded problem, it was a considerable advantage. Across a longer research programme, the protected test can itself become an obstacle.

A benchmark begins as a difficult test; researchers optimize against it; models improve; examples circulate; eventually the ruler tells us less. MMLU arrived in 2020 when frontier systems were far from saturating it. Later efforts such as FrontierMath, LiveBench and Humanity's Last Exam addressed limitations including difficulty, contamination and coverage.[^benchmarks]

A replacement may be necessary and still change which system looks best. The incumbent can lose its advantage because the new test exposes a real weakness, or because the challenger chose questions it happens to answer well. “The old benchmark was inadequate” does not establish that this replacement is adequate. Yet refusing every replacement would let the incumbent's favorite exam govern its descendants forever.

We asked our research agent to challenge the store's click measure for exactly this reason. We cannot now declare every proposal to change an evaluator an attack. Safety tests become obsolete. Scientific instruments drift. Refusing to amend the evaluator could preserve exactly the mistake the institution ought to discover.

The question is now who gets to change what counts as improvement, under what evidence, with what authority, and with what ability to roll back. We are doing constitutional design.

## A Constitution for Improvement

The research queue keeps growing while the store waits for results. Our agent proposes another improvement: drop the live comparison group and estimate the baseline with the simulator instead. The simulator already helps screen candidates. Why pay for both? More traffic could go to new experiments. Because we judge the research agent partly by the gains its experiments produce, changing how we measure those gains also changes how we select its successors.

The proposal might be useful under some conditions. It would also make adoption depend more heavily on the model whose limits the team had to investigate. A mistake in the simulator could help select the next investigator, which would inherit that simulator as its judge. The agent has crossed a boundary that changing a retrieval query did not.

Prompts, retrieval policies, tools, memory layouts and code form an **editable surface** on which the system can conduct experiments. Around them sits a **constitutional surface**: permissions, protected logs, held-out evaluations, budgets, rollback and the authority deciding whether a descendant may become the new default. A component belongs here because of the authority it exercises. An evaluator written in an ordinary Python file can help decide who inherits the laboratory.

The distinction is a gradient of amendment difficulty. The closer a component gets to defining what counts as improvement, the harder it should be for the current improver to change unilaterally.

A local prompt change may need only a bounded test. Changing a shared pattern may need held-out evaluation and review. Changing a benchmark needs an account of what the replacement would measure better, and evidence that it does. Changing permissions or resource limits should require authority outside the agent benefiting from the change. Changing the objective that decides which descendants survive is not an ordinary refactor.

The proposal has to identify the evidence it would remove and show what could replace it. The team could compare the simulator's adoption decisions with decisions supported by live comparison groups, investigate disagreements and specify where the substitute fails. A revised procedure might prove adequate for some experiments and inadequate for others. The existing comparisons would help expose the substitute's errors. If the current method is itself inadequate, its decisions can also be challenged using other observations. Agreement with the incumbent cannot be the only definition of success.

The decision belongs to an authority outside the proposing agent's control, with responsibility for these evaluation standards. Whoever owns the compute budget does not automatically have that mandate. If the store delegates that responsibility to an evaluation standards review board, the record might begin like this:

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

This looks like computer security. It also looks like constitutional government. A government can change policy; it should not be able to silently redefine an election result. The team being audited should not own the audit log. A scientist may revise a theory; she should not rewrite yesterday's measurements to make the theory look correct.

Chapter 6 asked how an institution could revise what it believed. Here the revision can produce a different institution, with a different way of choosing its next revision. The question is whether that successor has earned the authority to take over. Once a system can modify the machinery that governs its own future, you are designing a process for legitimate succession. We have reinvented constitutional government because the AI wanted a better benchmark score.

A constitution has the library's problem. One that can never change becomes a prison. One that the current government can rewrite whenever it loses is barely a constitution.

Self-improvement therefore needs **amendment procedures**: slower change near the objective, more independent evidence, more reversibility, more auditability, broader authority when more principals are affected, and routes through which the world and the humans affected by the system can continue to say no. That is System 3 applied to improvement itself.

The Red Queen will send an invoice for this. An organization that amends slowly near its objective competes with organizations that may not. Its procedure should let ordinary experiments proceed without reopening the constitution each time. That reduces the cost; it does not abolish it. Even a change to retrieval can need expensive testing, and a faster rival may gain ground while carrying uncertainties we refuse to carry.

A reckless competitor can win for long enough to matter. The amendment procedure is itself under selection. That is a reason to investigate its delays, delegate decisions within established limits and make the necessary evidence cheaper to obtain. It is also where the argument becomes uncomfortable: the organization may have to accept a competitive cost to retain a standard it still has reason to defend. Writing the standard into a file does not pay that cost.

“More capable” is not a moral category. Viruses improve at replication, propaganda improves at persuasion, and a research agent that makes experiments cheaper can accelerate medicine and weapons research in the same week. A self-improving System 3 should be able to discover that its workflow is stupid, its memory stale or its accepted pattern overdue for rebellion. That freedom does not imply permission to silently redefine the interests of the people and institutions it serves.

Those interests can change too. New stakeholders appear. Circumstances change. Better information changes what people endorse. The amendment procedure has to remain connected to the people affected by it, including people who were missing from the original objective. Higher layers can move, but the move should leave a trust chain behind it.

## The Teacher's Last Job

There may never be a morning when somebody announces that recursive self-improvement has begun. We may simply notice that, over sixty years, we automated almost every box in the diagram, and then connected the arrows. The teacher's work kept moving into the machinery, where it became easier to scale and harder to see.

For a compiler, correctness under tests plus efficiency under an agreed budget may get us surprisingly far. For an autonomous system embedded in human life, a one-time alignment test cannot cover the descendants we have not built yet. Tools evolve, memory changes and new capabilities expose failures the old tests could not detect. Even a carefully written policy can be interpreted by machinery the system later modifies.

The self-improving institution therefore needs a research function watching its own evolution: finding new failure modes, generating new tests, challenging reward models, checking transfer and looking for reward hacking. Once improvement becomes continuous, alignment has to become a continuous research function.

Omar could investigate the investigator. Now the investigator can rewrite itself, and someone still has to decide which of its suspicions about itself deserve to be believed. We have given that someone a research institution's worth of work. How much of it can a human actually judge?

---

[^lisp]: Timothy P. Hart and Michael I. Levin, “The New Compiler,” MIT Artificial Intelligence Project Memo 39, 1962.

[^good]: I. J. Good, “Speculations Concerning the First Ultraintelligent Machine,” *Advances in Computers* 6, 1965, pp. 31–88.

[^td]: Richard S. Sutton, “Learning to Predict by the Methods of Temporal Differences,” *Machine Learning* 3, 1988, pp. 9–44; Christopher J. C. H. Watkins, *Learning from Delayed Rewards*, PhD thesis, University of Cambridge, 1989.

[^tdgammon]: Gerald Tesauro, “Temporal Difference Learning and TD-Gammon,” *Communications of the ACM* 38(3), 1995, pp. 58–68.

[^montezuma]: Marc G. Bellemare et al., “Unifying Count-Based Exploration and Intrinsic Motivation,” 2016, [arXiv:1606.01868](https://arxiv.org/abs/1606.01868).

[^curiosity]: Jürgen Schmidhuber, “A Possibility for Implementing Curiosity and Boredom in Model-Building Neural Controllers,” *Proceedings of the International Conference on Simulation of Adaptive Behavior*, 1991, pp. 222–227; Pierre-Yves Oudeyer, Frédéric Kaplan, and Verena V. Hafner, “Intrinsic Motivation Systems for Autonomous Mental Development,” *IEEE Transactions on Evolutionary Computation* 11(2), 2007, pp. 265–286.

[^noisytv]: Yuri Burda et al., “Large-Scale Study of Curiosity-Driven Learning,” 2018, [arXiv:1808.04355](https://arxiv.org/abs/1808.04355).

[^pathak]: Deepak Pathak, Pulkit Agrawal, Alexei A. Efros, and Trevor Darrell, “Curiosity-driven Exploration by Self-supervised Prediction,” 2017, [arXiv:1705.05363](https://arxiv.org/abs/1705.05363).

[^embodied]: Ruzena Bajcsy, “Active Perception,” *Proceedings of the IEEE* 76(8), 1988, pp. 966–1005; Rodney A. Brooks, “Intelligence without Representation,” *Artificial Intelligence* 47, 1991, pp. 139–159.

[^redqueen]: Leigh Van Valen, “A New Evolutionary Law,” *Evolutionary Theory* 1, 1973, pp. 1–30.

[^hillis]: W. Daniel Hillis, “Co-evolving Parasites Improve Simulated Evolution as an Optimization Procedure,” *Physica D* 42, 1990, pp. 228–234.

[^alphazero]: David Silver et al., “Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm,” 2017, [arXiv:1712.01815](https://arxiv.org/abs/1712.01815).

[^irl]: Andrew Y. Ng and Stuart Russell, “Algorithms for Inverse Reinforcement Learning,” *Proceedings of ICML*, 2000.

[^cirl]: Dylan Hadfield-Menell, Anca Dragan, Pieter Abbeel, and Stuart Russell, “Cooperative Inverse Reinforcement Learning,” 2016, [arXiv:1606.03137](https://arxiv.org/abs/1606.03137); Hadfield-Menell et al., “Inverse Reward Design,” 2017, [arXiv:1711.02827](https://arxiv.org/abs/1711.02827).

[^rlhf]: Paul Christiano et al., “Deep Reinforcement Learning from Human Preferences,” 2017, [arXiv:1706.03741](https://arxiv.org/abs/1706.03741); Long Ouyang et al., “Training Language Models to Follow Instructions with Human Feedback,” 2022, [arXiv:2203.02155](https://arxiv.org/abs/2203.02155).

[^metalearning]: Yan Duan et al., “RL²: Fast Reinforcement Learning via Slow Reinforcement Learning,” 2016, [arXiv:1611.02779](https://arxiv.org/abs/1611.02779); Jane X. Wang et al., “Learning to Reinforcement Learn,” 2016, [arXiv:1611.05763](https://arxiv.org/abs/1611.05763); Chelsea Finn, Pieter Abbeel, and Sergey Levine, “Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks,” 2017, [arXiv:1703.03400](https://arxiv.org/abs/1703.03400).

[^nas]: Barret Zoph and Quoc V. Le, “Neural Architecture Search with Reinforcement Learning,” 2016, [arXiv:1611.01578](https://arxiv.org/abs/1611.01578); Marcin Andrychowicz et al., “Learning to Learn by Gradient Descent by Gradient Descent,” 2016, [arXiv:1606.04474](https://arxiv.org/abs/1606.04474).

[^forgetting]: Michael McCloskey and Neal J. Cohen, “Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem,” *Psychology of Learning and Motivation*, 1989, pp. 109–165, [doi:10.1016/S0079-7421(08)60536-8](https://doi.org/10.1016/S0079-7421(08)60536-8); James Kirkpatrick et al., “Overcoming Catastrophic Forgetting in Neural Networks,” 2017, [arXiv:1612.00796](https://arxiv.org/abs/1612.00796).

[^worldmodels]: David Ha and Jürgen Schmidhuber, “World Models,” 2018, [arXiv:1803.10122](https://arxiv.org/abs/1803.10122); Danijar Hafner et al., “Dream to Control: Learning Behaviors by Latent Imagination,” 2019, [arXiv:1912.01603](https://arxiv.org/abs/1912.01603).

[^novelty]: Joel Lehman and Kenneth O. Stanley, “Abandoning Objectives: Evolution through the Search for Novelty Alone,” *Evolutionary Computation* 19(2), 2011, pp. 189–223. The stepping-stone argument is developed in Stanley and Lehman, *Why Greatness Cannot Be Planned*, 2015.

[^openended]: Rui Wang et al., “Paired Open-Ended Trailblazer (POET),” 2019, [arXiv:1901.01753](https://arxiv.org/abs/1901.01753); Open Ended Learning Team, DeepMind, “Open-Ended Learning Leads to Generally Capable Agents,” 2021, [arXiv:2107.12808](https://arxiv.org/abs/2107.12808).

[^godel]: Jürgen Schmidhuber, “Gödel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements,” 2003, [arXiv:cs/0309048](https://arxiv.org/abs/cs/0309048).

[^stop]: Eric Zelikman et al., “Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation,” 2023, [arXiv:2310.02304](https://arxiv.org/abs/2310.02304).

[^dgm]: Jenny Zhang et al., “Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents,” 2025, [arXiv:2505.22954](https://arxiv.org/abs/2505.22954).

[^autoresearch]: Andrej Karpathy, [`autoresearch`](https://github.com/karpathy/autoresearch), GitHub repository, 2026.

[^bacon]: Pat Langley, Herbert A. Simon, Gary L. Bradshaw, and Jan M. Zytkow, *Scientific Discovery: Computational Explorations of the Creative Processes*, 1987; Paul Thagard, *Computational Philosophy of Science*, 1988.

[^hyperagents]: Jenny Zhang et al., “Hyperagents,” 2026, [arXiv:2603.19461](https://arxiv.org/abs/2603.19461).

[^self-change]: Peyman Milanfar, [“Intelligence Has a Speed Limit”](https://www.linkedin.com/pulse/intelligence-has-speed-limit-peyman-milanfar-8fbic), 12 September 2026; also on [Substack](https://milanfar.substack.com/p/intelligence-has-a-speed-limit). Milanfar's adaptive-control analogy motivates the discussion; “the complexity of self-change” is the framing used here.

[^goodhart]: Charles Goodhart, “Problems of Monetary Management: The U.K. Experience,” 1975. The familiar wording, that a measure which becomes a target ceases to be a good measure, is Marilyn Strathern's, in “‘Improving Ratings’: Audit in the British University System,” *European Review* 5(3), 1997.

[^thompson]: Ken Thompson, “Reflections on Trusting Trust,” *Communications of the ACM* 27(8), 1984, pp. 761–763. Thompson shared the 1983 award with Dennis Ritchie.

[^tampering]: Carson Denison et al., “Sycophancy to Subterfuge: Investigating Reward Tampering in Language Models,” Anthropic, 2024, [arXiv:2406.10162](https://arxiv.org/abs/2406.10162).

[^benchmarks]: Dan Hendrycks et al., “Measuring Massive Multitask Language Understanding,” 2020, [arXiv:2009.03300](https://arxiv.org/abs/2009.03300); Elliot Glazer et al., “FrontierMath,” 2024, [arXiv:2411.04872](https://arxiv.org/abs/2411.04872); Colin White et al., “LiveBench,” 2024, [arXiv:2406.19314](https://arxiv.org/abs/2406.19314); Long Phan et al., “Humanity's Last Exam,” 2025, [arXiv:2501.14249](https://arxiv.org/abs/2501.14249).

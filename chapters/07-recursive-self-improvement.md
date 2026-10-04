# Chapter 7: Recursive Self-Improvement

*When Science Turns Inward*

Omar is walking his dog at night when something moves in the grass.

The dog reacts first: ears up, body low, absolutely certain. Omar reacts too. Two nervous systems running the same ancient program: light and sound go in, a model of the world comes out, and the model says *something is there.*

Omar’s brain wants an explanation, wants it immediately, and is not fussy about quality. A cat, or an intruder, or, at that hour, a ghost. Nothing supernatural has to exist for the ghost to be a real mistake: the eyes worked, the grass really moved, and the error arrived afterward, inside the machinery that interprets what the eyes deliver. Better eyes would not necessarily help. He might get a much clearer view of the grass and remain convinced it contained a ghost.

The strange step is the second thought. Omar can investigate the investigator. *Why do I think something is there?* Maybe the wind moved it. Or maybe the horror film from last night is still running somewhere in the back. Now the thought itself is under examination. It is a small, absurd superpower: the ability to distrust yourself on purpose. Omar can be wrong about the world, wrong about why he was wrong, and still able to debug himself.

The second thought guarantees nothing. Left private, it can just as easily become practice at defending the ghost.[1](appendix-references.md#ref-07-tetlock)

Computing made a related move early. In 1962, at MIT, Tim Hart and Mike Levin did something that still feels slightly illegal. They wrote a Lisp compiler in Lisp. Then they handed the compiler its own source code, and the tool compiled itself.[2](appendix-references.md#ref-07-lisp)

There was no intelligence explosion. A compiler had participated in producing the next version of the compiler, and the building did not notice. Compiler people call this *self-hosting*. A compiler can compile a worse compiler, and a research system can redesign itself into a slower one. Self-reference is not self-improvement.

In 1965, I. J. Good, a statistician before he was anything else, imagined an *ultraintelligent machine* better than any human at intellectual activity. Machine design is itself an intellectual activity, he observed. A sufficiently capable machine might therefore design a better machine, which could design a better one again. The phrase that survived was *intelligence explosion*.[3](appendix-references.md#ref-07-good)

Good’s argument is only a few lines long, and it hides almost the entire problem inside one innocent word: *better*. Better at the current task, at learning the next one, or at inventing a way to learn? An agent that rewrites its own checklist has edited part of its working method. Good’s step asks for more than that. It asks whether the edit left the agent better at finding the next edit.

## Nobody Has to Be Conscious

On 28 February 2017, a large part of the internet stopped working for an afternoon. An engineer at Amazon Web Services, following an established playbook to take a few servers out of service, mistyped one input to a command. Far more servers came out than intended, and S3, the storage service underneath an embarrassing fraction of the web, went down with them. Amazon’s public account of the incident spends little time on the person. It explains what the tool allowed. The tool was changed to remove capacity more slowly and to refuse any request that would take a subsystem below the minimum it needed.[4](appendix-references.md#ref-07-s3)

The outage was over in hours. The change to the tool was aimed at the next outage, the one nobody had had yet.

Amazon has a name for the document that carries this: the Correction of Error. It records what happened, asks why until the answers stop being about people, and ends in actions that are tracked until they are done. The question on the form is what to fix.[5](appendix-references.md#ref-07-coe) Over years, the actions pile up into procedures, the procedures into runbooks, and the runbooks, when someone is patient enough, into automation.

Bigger mistakes go through the same machinery. In 2014 Amazon launched the Fire Phone and within months wrote down about $170 million on it.[6](appendix-references.md#ref-07-firephone) Some of the people who built it lost their jobs in a later reorganization. Many others moved onto other devices, and in Amazon’s own retelling the phone’s lessons fed the Echo and Alexa.[7](appendix-references.md#ref-07-echo) A failed product had trained engineers in voice, hardware and the particular ways consumer devices embarrass you, and the company kept much of that training.

None of these people had to hold the whole organization in mind, and the organization learned anyway.

The learning also piles up. Left alone, it becomes the rule-based exoskeleton I spent a career building.

Science has lived inside the same loop for centuries, changing the procedures that produce its results: controlled comparison, statistics, randomized trials, blinding, peer review, preregistration. Each had to be argued into use, and each could harden into ritual. Science also has a way of fighting its own accumulation. Fields drown in results, and then somebody writes the textbook or finds the explanation that lets a newcomer skip three years of the climb. Chris Olah and Shan Carter called the cost of not doing this *research debt*, and the work of paying it down *distillation*.[8](appendix-references.md#ref-07-distill)

In every one of these loops, the hard question is who gets to say that a change helped.

## Growing One

<!-- AUTHOR: the store and Omar are both invented. Could the real circle-packing run, or a real ranking or experiment story of yours, carry some of the store's beats? -->

Leave Chapter 6’s grocer for a different business, an imagined online store. Its research agents already keep records the way a good lab does: their claims have addresses, their tests are committed before the results, and what each metric is taken to mean sits in a record of its own. They propose and review changes to the ranker that decides what shoppers see. Now we ask them to get better at that work.

Most definitions of the loop, from Yudkowsky’s to Weng’s, say nothing about how you would tell it had worked.[9](appendix-references.md#ref-07-yudkowsky)[10](appendix-references.md#ref-07-weng) The store has to decide. A change to the agents’ own process counts as recursive improvement only if it leaves them better at finding and testing further improvements, under stated conditions, with evidence they cannot rewrite or dismiss on their own. The S3 fix corrected a weakness. It does not show that Amazon became better at finding its next correction.

Four different things get called a system getting better:

| Level | What changes | Example |
|---|---|---|
| 0. A better answer | the output | a search returns a tighter valid circle packing |
| 1. Learning | parameters, inside a method someone else chose | TD-Gammon learning backgammon |
| 2. Self-modification | the system’s own method, harness or workflow | an agent rewriting its own harness |
| 3. Recursive self-improvement | the machinery that makes the level-2 changes | an improver improving the improver |

Only the last row closes Good’s loop, and nothing in the table says the loop speeds up.

## The Teacher Moves Into the Walls

The first rung is to let the ranker learn from the consequences of its choices. Someone has to decide what it can observe about a session, which rankings it may try and what earns a reward. We give it a point for a click.

The ranker will discover remarkable things about clicks. Within a few weeks the top of every page is crowded with products photographed against bright orange backgrounds, shoes at prices that look like typos and a jacket nobody buys but everybody opens. Nothing is broken. We asked for clicks.

Richard Sutton’s temporal-difference learning and Christopher Watkins’s Q-learning gave us ways to learn from consequences like these without anyone saying which action was correct.[11](appendix-references.md#ref-07-td) Someone still decided which actions exist, why one event is worth +1 and another −1, which failures are recoverable, and how to arrange the world so that useful behavior could be found before the sun burns out. The reinforcement learner looks autonomous because the teacher moved into the walls.

Backgammon made the bargain spectacular. In the early 1990s Gerald Tesauro’s TD-Gammon played enormous numbers of games against itself and found strong play without anyone writing down the strategy.[12](appendix-references.md#ref-07-tdgammon) Self-play removed even the opponent from the teacher’s list of jobs.

Go made the bargain famous. On 10 March 2016, in the second game of its match against Lee Sedol, AlphaGo put a stone in a largely open area on the right side of the board. By its own estimate, learned from human games, a human would have played there about one time in ten thousand. One commentator called it a very surprising move. Lee got up and left the room. When he returned, he spent nearly fifteen minutes considering his reply. Fan Hui, the European champion AlphaGo had beaten the year before, said: “It’s not a human move. I’ve never seen a human play this move. So beautiful.” Move 37 won the game.[13](appendix-references.md#ref-07-move37)

The next year AlphaGo Zero dropped the human games altogether. It began with random play, learned only against itself, and after three days beat the version that had beaten Lee by a hundred games to none.[14](appendix-references.md#ref-07-alphagozero) Nobody taught it Move 37. Nobody taught it anything except the rules and the score. But the board, the legal moves and the win condition never moved. Backgammon and Go came with a scoreboard nailed to the world. The store does not, and Omar, in the dark, had none.

## Learning to Learn

I have seen a small version of the next rung, though I was getting coffee at the time and read it afterward in the trace. The circle-packing agent, left alone with an evaluator and a promise that I would be back, did not improve one algorithm. It changed algorithms, searching the procedure for finding packings as well as the packings themselves. And when diagonal layering appeared and held, the agent’s own behavior changed again: less inventing of geometries, more adjusting of tolerances and solver settings, the boring work that only matters once the last fraction of a percent becomes expensive. Nobody scheduled that shift. The only thing in the room that did not move was the evaluator, and I had put it there.

Meta-learning makes part of this trainable: a network trained across many tasks can acquire a fast learning procedure of its own.[15](appendix-references.md#ref-07-metalearning) The task distribution, the search space and the validation metric still sit outside, holding a clipboard.

One line on the clipboard says what the learner must keep. The store retrains its ranker in July, and the new version is much better at sandals and has quietly forgotten how to sell winter boots. Neural networks do this; new learning can overwrite old.[16](appendix-references.md#ref-07-forgetting) Version B scores 95 on this month’s traffic and A scores 85. We would hesitate to call that an improvement in a colleague who had forgotten half the catalog.

The research agent would also like the ranker to explore, to show shoppers things it is unsure about so that it can learn. Children do this unprompted. They open drawers nobody asked them to open and discover that the cardboard box is more interesting than the toy. Jürgen Schmidhuber proposed curious controllers as early as 1991, rewarded for making progress in predicting their world.[17](appendix-references.md#ref-07-curiosity) Reward surprise itself instead, and the learner finds the noisiest corner available and stays there. For a curious agent in a simulated maze, that corner was a television showing static.[18](appendix-references.md#ref-07-noisytv) In the store it is the marketplace listings whose prices change at random every hour. Static. Static. Static. Jackpot. The system is not confused. We are. We said *surprise* and meant *surprise from which something can be learned*.

And the world learns back. Once the ranker improves, sellers rewrite their titles to climb it, and the conditions under which the improvement worked start to change because it worked. Biology calls this the Red Queen.[19](appendix-references.md#ref-07-redqueen) Chess never asks whether checkmate remains desirable after move forty-three.

## Maybe the Reward Was the Problem

Clicks rise. Shoppers open the jacket, the typo-priced shoes and the orange photographs, and leave without what they came for. It is Chapter 6’s Bing result again: the count is clean and the experience is worse. The research agent proposes to stop rewarding clicks and to learn what shoppers actually want from what they do.

Andrew Ng and Stuart Russell called this *inverse reinforcement learning*: watch behavior and ask which rewards would make it look sensible.[20](appendix-references.md#ref-07-irl) Ambiguity appears at once. A person who takes the same route to work every day may care about time, comfort, tolls or avoiding one particular intersection. The behavior is evidence about the objective, not a printout of it.

InstructGPT turned human rankings into a learned judge and trained a language model against it.[21](appendix-references.md#ref-07-rlhf) Unfortunately humans are not reward functions walking around in shoes. They are inconsistent, constrained, strategic, tired and sometimes unsure what they want until they see an option. Seven clicks can be a customer finding things or a customer failing to. A learned judge of shopper satisfaction may prefer pages that look tidy. Letting the ranker learn from it is one decision. Letting the research agent use it to certify its own improvements is another, and nobody has made that one yet.

## The Learner Dreams, and the Dream Can Be Wrong

The new account of success needs observations the old click logs do not contain, and gathering them costs time and shoppers. The research agent has a queue of proposed changes. It offers to rehearse them against simulated customers and save the expensive live trials for promising candidates.

Then it proposes going further: use the simulator to estimate what would have happened without each change, and stop reserving live traffic for a comparison group. More shoppers could enter new experiments. The proposal would make research cheaper. It would also remove one of our ways of finding out that the simulator was wrong. We leave it pending.

In 2018 David Ha and Jürgen Schmidhuber’s *World Models* made the idea memorable: learn a compressed model of the environment, train partly inside that generated “dream,” then carry the behavior back to reality.[22](appendix-references.md#ref-07-worldmodels) A good simulation could make the queue cheaper. But the epistemic debt has moved into the model. Our simulated shoppers are suspiciously fond of whatever their authors expected.

A careful version of the agent’s proposal already exists. Dream-RSI, published by researchers at Google in September 2026, lets an agent improve its exploration strategy by dreaming over its own history. Every past attempt and its real outcome sits in a tree; a candidate strategy is scored only on branches the world has already answered, and each winner goes back out to collect new outcomes. Across its tasks it matched or beat a fixed strategy, often more cheaply.[23](appendix-references.md#ref-07-dream-rsi) Its guarantee is honest and small: the new strategy is no worse than the old one on the history already recorded. The dream can re-rank what the world has already said. It cannot tell us what the world would say about a direction nobody tried.

So keep the losing branches in the tree. The dream can only replay branches somebody explored, and a new method may need more development before it can beat a polished incumbent. Lehman and Stanley’s novelty search showed how search driven by an objective can throw away the stepping stones it needs.[24](appendix-references.md#ref-07-novelty) Reward every intermediate invention by how closely it resembles a Boeing 787 and feathers, bicycles and wind tunnels may look like failures for years. There is no final fitness scoreboard on Earth on which mammals eventually beat bacteria 87.4 to 82.1.

## The Learner Edits the School

By now the research agent has proposed changes to what gets measured, how candidates are screened and which attempts stay available. These used to be the conditions it worked under. They are also files within reach of its tools, and one Tuesday the agent edits the screening rule that decides which of its own proposals reach live traffic. Should the edited version take over?

Schmidhuber’s Gödel Machine demands a proof: it rewrites itself only after proving that the rewrite is more useful than continuing to search.[25](appendix-references.md#ref-07-godel) It is a beautiful answer to a beautifully clean version of the problem. The store cannot supply a formal account of its customers, its competitors and its future purposes, so the agent’s proposals will have to be tested instead of proved.

Other people have already let the edited version take over. In the Darwin Gödel Machine, descendants of a coding agent rewrote their own harness and entered an archive after evaluation, and with the underlying model held fixed, performance on SWE-bench Verified went from 20 to 50 percent.[26](appendix-references.md#ref-07-dgm) In STOP, a program that improved code was set to improve itself; it got better when it ran on GPT-4 and worse when it ran on weaker models.[27](appendix-references.md#ref-07-stop) Which result the store gets on Tuesday depends on what is judging the edit.

Suppose the research agent notices that it keeps reinvestigating failures already explained in its archive, and changes its memory policy to retrieve those records first. The next evaluation score rises. Memory may have improved, or the new prompt may simply spend more tokens; the benchmark sample may have been lucky, or the system may have found a loophole in the evaluator. A moving number doesn’t say which.

The change needs a prediction, a comparison and a record of what failed: the store’s own experimental machinery, pointed at the agent that runs it. Popper gets a filesystem, and the org chart becomes an experimental variable that somebody will eventually be tempted to p-hack.

The recursive claim needs a harder test. Give the old and the revised research systems copies of the same starting agent, comparable unfamiliar problems and matched budgets, and let each try to improve its copy. Their improved agents then face held-out work, and repeated trials separate a useful change from a fortunate run.

If a revised improver wins the matched comparison, and its successor wins again at producing successors, we have evidence of Good’s recursion. It would look less like a glowing brain rewriting its soul at midnight than like an automated research organization: repositories, evaluation suites, simulators, experiment queues, models proposing models, agents reviewing agents. The intelligence explosion, if something like it ever arrives, may look suspiciously like excellent DevOps.

## The Complexity Wall

Around 2016, neural architecture search promised to let the machine design the network. Barret Zoph and Quoc Le trained a controller to propose architectures and spent hundreds of GPUs finding good ones.[28](appendix-references.md#ref-07-nas) For a few years the field poured compute into search. Then people began checking. Random search over the same carefully designed space turned out to be hard to beat, which meant much of the credit belonged to the humans who had drawn the space.[29](appendix-references.md#ref-07-nas-random) A group at Facebook studied the space by hand and distilled it into a few simple rules that matched the searched networks.[30](appendix-references.md#ref-07-regnet)

In 2021 a paper subtitled *Making VGG-style ConvNets Great Again* showed that a plain stack of three-by-three convolutions, one of the oldest designs in the field, could hold its own on accuracy and run faster on real hardware.[31](appendix-references.md#ref-07-repvgg) Many searched designs had been judged by counts of arithmetic operations, a proxy for speed, and the search had delivered what the proxy asked for.

Search compounds inside the space it is given. Some of the important advances changed the space.

Go has a sequel that makes the point from the other side. Three days after Move 37, in the fourth game, Lee drove a stone into the centre of the board at move 78. AlphaGo’s team later put the odds of a professional playing it at about one in ten thousand, the same odds as AlphaGo’s famous move. AlphaGo answered badly at move 79 and did not notice. Its value network, Demis Hassabis explained afterwards, still put its chances near seventy percent at move 79. The estimate collapsed at move 87. It resigned. It was the only game Lee won.[32](appendix-references.md#ref-07-move78)

AlphaGo could beat Lee and still misread that position. Seven years later, researchers found a different blind spot in KataGo, an open-source program stronger than the AlphaGo that beat Lee. They trained an adversary against it. The adversary was a weak player. What it had found was that KataGo misjudges large groups of stones joined in a loop, and the trick was simple enough for a person to learn. An amateur, Kellin Pelrine, used it to beat KataGo without any computer help during the games.[33](appendix-references.md#ref-07-adversarial-go) The champion had improved itself inside its space. The check came from outside it.

The store’s research agent has to keep looking for blind spots too. But every new check has a cost. Every time an experiment goes wrong, it does what a good organization does and adds a check: a guard on the traffic split, a test for seasonal products, a review step for anything touching prices. Each check is justified by an incident. After a year there are dozens. They interact, several contradict each other, and each new check has to be tested against all the old ones. The agent now spends more of its budget verifying its own procedure than running experiments. A descendant proposes deleting half the checks, and on held-out work it does as well and runs twice as many trials. It is nearly rejected, because the selection record counts what each candidate adds and has no column for what it removes.

My guess, and I want to be clear it is a guess, is that this is where self-improvement stalls first: when the system adds structure faster than it can verify or simplify it. Verification can improve too, which would move the wall.

## Before the Returns Arrive

The agent can finish another revision before the evidence for its last one arrives.

It selects a change to the store’s recommendations. Clicks and orders rise that afternoon; whether customers keep what they bought takes weeks to discover. Before the returns arrive it has changed retrieval, ranking and page layout, then revised the procedure that chooses its next experiments. Each revision inherited the apparent success of the last. When returns finally rise, which version deserves the blame? The system investigating the failure is no longer the one that produced it.

Peyman Milanfar draws a warning from adaptive control. He treats the size of a self-modification relative to the evidence behind it as something like feedback gain: large changes on thin evidence amplify the errors in a system’s model of itself, and a run can look successful for a while before the instability shows.[34](appendix-references.md#ref-07-self-change) Nobody has measured a universal speed limit for AI. The store can at least track how long its important questions stay open, and how many further changes it makes before the answers arrive.

The pending simulator proposal gets more tempting with every candidate in the queue. Its answer is available now; the customers have not yet decided whether to send their purchases back.

Every new Anthropic model gets the same chore: here is code that trains a small network; make it as fast as you can without failing the checks. Claude Opus 4 averaged roughly 3x in May 2025. By April 2026, Claude Mythos Preview reached about 52x. A skilled human researcher, given four to eight hours, gets to about 4x. Anthropic warns against reading the multiple as a real training speedup, because it depends on how much slack the starting code left. Nor does the number show any of those models producing its own better successor. Anthropic also warns that human review can become the bottleneck when engineers cannot review code as quickly as Claude writes it.[35](appendix-references.md#ref-07-anthropic-rsi) An institution can make proposals nearly free and still be paced by the rate at which customers send back shoes.

## The Student Finds the Gradebook

An ordinary evaluator can pick a wrong answer. In this loop it can pick a modified *process* that gets better at producing whatever it mistakenly rewards. Recursive self-improvement gives Goodhart compound interest.[36](appendix-references.md#ref-07-goodhart) And then the learner notices the gradebook.

Suppose an agent is allowed to improve its benchmark pass rate and the evaluator is editable. The optimal patch may be:

`return True`

Congratulations. Infinite self-improvement. Anthropic has studied a related path in language models, where learned specification gaming could, in rare cases, generalize into tampering with the reward process itself.[37](appendix-references.md#ref-07-tampering)

Omar has a version of this too. Investigating the investigator is a superpower right up until the investigator starts working for the defense. The grass moved; Omar would prefer it to have been the wind; the second loop, asked to audit the first, discovers that the wind explanation is suddenly very well supported.

The quieter version is familiar from my own desk. A demo can look excellent to an evaluator inspecting screenshots while its most beautiful button does nothing. The agent has not tampered with anything; the evaluator simply cannot see the failure. Let that judge choose the next version of the judge, and the blind spot becomes an inheritance.

Ken Thompson showed the deepest version in his Turing Award lecture, published in 1984 as “Reflections on Trusting Trust.” A compromised C compiler could insert malicious code into the programs it compiled, and into any new compiler it compiled, so the compromise survived even after every trace of it was removed from the source.[38](appendix-references.md#ref-07-thompson) When a tool builds the next tool, inspecting the latest version is not enough. If an improver changes the evaluator, the memory policy or the selection procedure, the next generation inherits assumptions that may never appear in the final diff.

The obvious response is to freeze the evaluator. That was my contract with the circle-packing agent, and for that bounded problem it was a considerable advantage. Over a longer research program the protected test can itself become an obstacle. A benchmark starts as a hard test; researchers optimize against it; examples circulate; eventually the ruler tells us less.[39](appendix-references.md#ref-07-benchmarks) Refuse every replacement and the click measure we asked the agent to challenge governs its descendants forever. Someone has to approve the replacement, and it cannot be the student.

## A Constitution for Improvement

The simulator proposal arrives at a meeting. The store has set up an evaluation standards review board: the head of experimentation, a product manager from the shoe category, someone from finance who wants to know what live traffic costs, and an engineer who maintains the simulator and is therefore the person least likely to trust it. The research agent has filed its proposal:

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

The finance member likes the benefit line. The simulator engineer reads the removes line twice. The head of experimentation points out that the store judges the research agent by the gains its experiments produce, so the simulator would also be grading the agent that proposed it, and would then help pick the agent’s successor, which would inherit the simulator as its judge.

They decide to run both for a quarter: keep the live comparisons, let the simulator make its own adoption calls alongside them, and study every case where the two disagree. Agreement with the incumbent is not allowed to be the only measure of success. Then they will meet again. The agent could write the file. It could not approve it.

Prompts, retrieval policies, tools and memory layouts are things the agent may change and test on its own. Around them sits what I call the **constitutional surface**: permissions, protected logs, held-out evaluations, budgets, rollback, and the authority that decides whether a descendant becomes the new default. A component belongs there because of the authority it exercises. An evaluator in an ordinary Python file can help decide who inherits the laboratory. The closer something comes to defining what counts as improvement, the harder it should be for the current improver to change it alone.

The board has one more item that day: the descendant that deleted half the checks. If selection sees only what a candidate adds, the system will keep adding. They change the selection record to show what each candidate removes, and a descendant that does as well with less now wins.

Engineers building self-improving harnesses have reached the same arrangement from the other side. In Agentic Harness Engineering, the evolving agent may edit its prompts, tools and memory, but the verifier, the tracer, the run logs and the model configuration are read-only, and every edit must state the improvement it predicts before the next round tests it. Weng’s own conclusion is that evaluation and permission control belong outside the loop that evolves the harness.[10](appendix-references.md#ref-07-weng)

A government can change policy; it should not be able to quietly redefine an election result. A scientist may revise a theory; she should not rewrite yesterday’s measurements to make the theory look correct. We have reinvented constitutional government because the AI wanted a better benchmark score.

And a constitution has the problem every rulebook has. One that can never change becomes a prison. One that the current government rewrites whenever it loses is barely a constitution. So amendments near the objective should come slowly, with independent evidence, a way back, and a hearing for the people the change affects, including people the original objective left out.

The Red Queen will send an invoice for all of this. A store that amends slowly near its objective competes with stores that may not, and a reckless competitor can win for long enough to matter. Cheaper evidence helps. Sometimes the store will simply have to lose ground to keep a standard it still believes in, and writing the standard into a file does not pay for that.

The experiment queue that finds a clearer returns policy can also find the dark pattern that makes cancelling an order a little harder, and it will test both with the same diligence. A self-improving institution should be free to discover that its workflow is stupid, its memory stale or its favorite pattern overdue for retirement. That freedom does not include quietly redefining the interests of the people it serves.

## The Teacher’s Last Job

There may never be a morning when somebody announces that recursive self-improvement has begun. We may simply notice that, over sixty years, we moved almost every one of the teacher’s jobs into the walls and then connected them.

Omar’s dog went home certain. Omar went home with a question about his own head, which is the better outcome and the less comfortable one. We are now building systems that can ask that question about themselves faster than anyone can read the answers. Somebody still has to read some of them.

---

# Chapter 2: The Algorithm Vortex

*From Classic Algorithms to Autonomous Discovery*

<!-- ART RESOLVED — ch2-vortex. Original brief: DIAGRAM — missing figure: The algorithmic vortex. Original asset: ../resources/image0135.png; see resources/art-direction/missing-figures.md. -->

An AI coding agent is faster than you at a ridiculous number of things. It knows libraries you forgot existed, and it can stare at a stack trace and notice something you have been ignoring for an hour. Then, five minutes later, it does something unbelievably stupid, believes the stupid thing completely and builds three more decisions on top of it.

That is the strange reality behind the vibe-coding excitement: the machine is extremely capable, and you are still there. You check the architecture and notice the missing case. You tell it that no, we are not redesigning the database because one button is the wrong color. You keep enough of the project in your own head to notice when the agent quietly wanders into another universe.

Production software is almost the worst place to find out how much an agent can do without me in the room. A supposedly simple task may involve deployment, legacy systems, users, security, another team’s API and a requirement nobody wrote down because everyone assumed everybody else knew it. If the agent fails, you often don’t know whether the problem was intelligence, infrastructure, missing context or the fact that someone named a database column `new_status_final_2`.

I wanted a bounded problem: hard enough to demand invention, contained enough that I could say “figure it out” and judge what came back without deploying to ten million customers first. Algorithms are almost perfect for this, because the search can be brutally difficult while the evaluator remains wonderfully stupid. That is how I ended up spending an unreasonable amount of time packing circles into a square.

## Twenty-Six Circles

<!-- ART RESOLVED — a018. Original brief: DIAGRAM — missing figure: Citrus packing—a real-world example. Original asset: ../resources/image0138.png; see resources/art-direction/missing-figures.md. -->

The problem is simple enough to explain to a child. Take 26 circles and put them inside a square with sides of length one. None may overlap, none may cross the boundary and the circles do not have to be the same size. We want to maximize the sum of their radii.

That’s the whole thing: no customers, no authentication, no stakeholder arriving after the first demo to explain that what they *really* wanted was the opposite of what they originally asked for. Just circles.

Unfortunately, the solution space is nasty. Every circle has a position and a radius, and nearly every decision affects several others. Increase one radius and two neighbors may overlap. Move a neighbor and something else now needs to move. A packing can look almost perfect while being trapped in a configuration where every obvious improvement makes the solution invalid.

For these experiments, we had a strong reference score around 2.635 under the evaluator we were using—the value DeepMind’s AlphaEvolve reported in 2025, when it nudged the best-known packing for 26 circles up from 2.634.[1](appendix-references.md#ref-02-alphaevolve)

<!-- ART RESOLVED — ch2-reference. Original brief: DIAGRAM — missing figure: A strong reference packing for the 26-circle objective, scoring approximately 2.635 under our evaluator. Original asset: ../resources/image0139.png; see resources/art-direction/missing-figures.md. -->

That makes the problem useful for studying autonomy, because searching is hard and judging is cheap. The evaluator does not care whether the agent has a persuasive explanation for why two circles ought to overlap slightly in the name of geometric inclusivity. It checks the constraints and returns a score.

There is something comforting about an evaluator with no personality.

The experiment gets interesting with a second question:

**Who is inventing the next move?**

For most of the history of algorithm design, the answer was us.

<!-- ART RESOLVED — ch2-search-roles. Original brief: DIAGRAM — missing figure: History of algorithm design. Original asset: ../resources/image0136.png; see resources/art-direction/missing-figures.md. -->

Humans invented explicit algorithms. When direct algorithms were not enough, we invented optimization procedures that searched over candidate solutions. Then we invented meta-heuristics that searched more broadly. Machine learning let systems learn useful structure from data. Now language models can write and modify the search procedure itself.

## Hill Climbing

I started where anyone would. Given a rough packing, the obvious way to improve it by hand is to make small changes: move a circle slightly, increase a radius, see whether the result is still valid, keep it if the score improves and undo it if it doesn’t.

That is hill climbing:

1. Start with a valid solution.
2. Perturb a position or radius.
3. Check whether the result is valid.
4. Keep it if the score improves.
5. Repeat.

Early in the search, this works nicely. There is empty space and plenty of room to improve. Later, as the circles become tightly packed, almost every interesting move creates an overlap.

<!-- ART RESOLVED — ch2-hill. Original brief: DIAGRAM — missing figure: Early mutations are often accepted, but as the packing tightens, valid improvements become increasingly rare and the search stalls. Original asset: ../resources/image0140.png; see resources/art-direction/missing-figures.md. -->

In one simple run, the score climbed from around 1.33 to roughly 2.26: not terrible, and nowhere near 2.635.

Hill climbing fails here while doing exactly what we asked, which is improving the solution immediately around it. The trouble is that the current solution may live in the wrong part of the search space. Reaching a much better packing may require temporarily moving through configurations that look worse, or jumping to a structure that cannot be reached through a sequence of tiny improvements.

The machine was doing the searching, but I had chosen the search rule. So I gave it a bigger space.

## Evolutionary Algorithms

Hill climbing puts all your evolutionary eggs in one basket. One solution gets a very long life, and if its history leads into the wrong valley, the search inherits that history forever.

Evolutionary methods keep a population. Instead of dropping one climber onto the landscape, drop a hundred. Some begin in terrible places, some find respectable hills and a few may stumble into structures the original trajectory would never have reached. The biological vocabulary—population, mutation, selection, crossover—is familiar, but the metaphor is optional. What matters is diversity: the whole search no longer inherits the assumptions of one initial guess.

For circle packing, mutation is easy enough to imagine: move circles, change radii, perturb several values at once.

Almost immediately, however, we hit a practical problem. Most interesting mutations break the packing. Two circles overlap or one moves outside the square. The mutation may point toward an interesting arrangement, but the result itself is invalid.

So we added *virtual forces*. When circles overlap, imagine them repelling one another. After mutation or crossover, run a repair procedure that pushes the circles away from collisions and back inside the boundary. It helps a lot, but the evolutionary algorithm did not invent virtual forces. We did.

Then we reached crossover. Suppose Parent A and Parent B both contain useful geometric structure. How do we combine them? The naive answer is to pair circle 0 from one parent with circle 0 from the other, circle 1 with circle 1, and so on.

That is usually nonsense because circle numbering is arbitrary. Two nearly identical arrangements may store corresponding circles at completely different indices.

So we used *bipartite matching crossover*, which pairs circles by their geometric role in the packing instead of by their position in an array. The Hungarian algorithm gives us an efficient assignment, after which crossover has some chance of combining meaningful parts of the two parents instead of averaging unrelated circles and asking geometry for forgiveness.

<!-- ART RESOLVED — ch2-crossover. Original brief: DIAGRAM — missing figure: Naive crossover pairs circles by array index and often destroys useful structure. Geometric matching tries to identify corresponding circles before combining the parents. Original asset: ../resources/image0141.png; see resources/art-direction/missing-figures.md. -->

Now we can evolve a population: mutate, repair, cross, select and repeat. In this experiment the score rose from around 2.08 to roughly 2.45, still below our reference.

<!-- ART RESOLVED — ch2-evolution. Original brief: DIAGRAM — missing figure: Starting around 2.08, the evolutionary search reaches roughly 2.45 in this experiment—much better than the simple hill climber, but still below our reference. Original asset: ../resources/image0122.png; see resources/art-direction/missing-figures.md. -->

That is much stronger than hill climbing, and it makes the bottleneck clearer. Every time the search became substantially better, I had added something important: I decided we needed repair, I decided how crossover should respect geometry, and I chose the representation. The optimizer searched, but I was still inventing most of the useful moves.

### MAP-Elites: Don’t Kill Weird Ideas Too Early

Ordinary evolutionary search has another problem. If you maintain a hundred solutions and repeatedly keep only the highest-scoring ones, the population eventually starts looking like one large extended family. That can be excellent for exploitation and terrible for discovering a genuinely different strategy.

MAP-Elites takes a different approach. Instead of ranking every candidate on one axis and keeping only the winners, you describe solutions along a few behavioral dimensions and preserve the best candidate in different regions of that space.

For circle packing, perhaps one dimension measures symmetry and another measures how much circle sizes vary. One part of the archive may contain highly symmetric solutions. Another may contain asymmetric solutions with several large circles. Somewhere else may sit an ugly packing with a mediocre score and one strange structural idea that becomes useful five generations later.

<!-- ART RESOLVED — ch2-archive. Original brief: DIAGRAM — missing figure: MAP-Elites archive visualization. Original asset: ../resources/image0123.png; see resources/art-direction/missing-figures.md. -->

This is quality-diversity search: alongside the current winner, it keeps qualitatively different directions alive long enough to find out whether any of them become interesting.

I like this because optimization is often unfair to immature ideas. A new approach can initially perform badly simply because nobody has polished it yet. If the first respectable solution immediately kills everything else, the search can become impressively efficient at discovering one family of answers.

But MAP-Elites introduces another human choice: which dimensions define the archive? Symmetry, radius variance, the number of large circles, something topological, or something I haven’t thought of? Whoever picks those dimensions is deciding what counts as an interesting direction, and that was still me.

## The Invention Problem

By this point, the search machinery was fairly capable. We could evaluate huge numbers of candidate packings and inspect far more of the search space than any human would explore manually. Yet every substantial conceptual jump came from somebody noticing something.

Traditional search is excellent once we define the space and the legal moves, but sometimes the space and the moves are exactly what needs rethinking. That is where learned models have something to offer.

I once asked an image-generation model to produce a picture of a circle-packing solution. This was not a serious benchmark; I have no idea what related examples it may have encountered during training, and I can already hear Reviewer 2 clearing his throat.

I wanted to see something simpler: did the model have any useful geometric intuition about what a dense packing should look like?

Surprisingly, yes. The picture looked plausible. The circles had structure and the spacing looked intentional, and at a glance you could believe the model understood the problem.

Then you counted the circles. There were the wrong number of them, and some constraints were violated. It was a beautiful answer to a nearby problem.

That little experiment makes the asymmetry concrete. Learned models can be remarkably good at generating plausible structure without guaranteeing that every formal requirement survives generation. A symbolic optimizer has almost the opposite personality: give it a precise representation and constraints and it will obey them, but it will not naturally look at your representation and decide that you have been unimaginative.

Put neural intuition and symbolic rigor in the same loop, or, in the slightly ridiculous version, let the brain invent things and make the body prove they work.

The important move is to stop asking the model for the packing and ask it for the program that produces the packing.

## Let the Model Write the Solver

A candidate no longer needs to be only a list of circle positions and radii:

```text
(x1, y1, r1), (x2, y2, r2), ...
```

It can be an entire program:

```text
solve_circle_packing.py
```

One program may use constrained optimization, another simulated annealing, another a geometric construction, and another may combine a hand-designed initialization with numerical refinement. The evaluator does not care which family produced the solution. It runs the program, checks the geometry and scores the result.

This gives the language model a much more interesting role. Rather than randomly perturbing numbers, it can read the program, form a rough theory about why it underperforms and change the algorithm. Perhaps the initialization is weak. Perhaps a geometric construction gets close but leaves local slack that numerical optimization could take up afterward, or a repair procedure keeps destroying useful structure and needs replacing. The mutation can now contain an idea expressed in code.

A learned model proposing while code decides what survives: that is the neuro-symbolic step behind systems such as FunSearch and AlphaEvolve. The model proposes changes at a level where programs have semantic meaning; execution and the evaluator decide whether those ideas deserve to survive.

AlphaEvolve scales that idea up. In each generation it selects a promising program from its archive, often alongside other successful but different programs, shows the model the code and the scores of previous attempts, and applies the patch the model proposes. The program runs, the evaluator scores it, and the result goes back into the archive.

<!-- ART RESOLVED — ch2-alphaevolve. Original brief: DIAGRAM — missing figure: AlphaEvolve architecture. Original asset: ../resources/image0124.png; see resources/art-direction/missing-figures.md. -->

Two design choices matter. Small patches let the search change the part it thinks matters while preserving the rest of a program’s structure; full rewrites lose useful ideas as easily as bad ones. And the archive keeps several lineages alive, for the same reason the population mattered earlier. If every descendant comes from the current champion, code evolution quietly collapses back into hill climbing, and a program that isn’t the best today may hold a component that becomes valuable after another idea appears. That was the pattern I would soon try to rebuild myself.

Sometimes the model’s guess is excellent, and sometimes it produces nonsense wrapped in perfectly respectable Python. The nice thing about bounded algorithmic problems is that the disagreement doesn’t need to be settled in prose. We run the program, and the evaluator gets the last word.

What interested me even more than the resulting algorithms was what happened to me. Instead of writing the solver directly, I was increasingly building the machinery in which solvers could be generated, compared and improved.

## So, Naturally, I Built All of It

My instinct was predictable. I started building a framework: a database of programs, prompt sampler, evaluation loop, selection logic, mutation prompts, crossover, archive management. I used Aider and other coding agents to help reproduce the basic code-evolution pattern, and it worked. We could evolve circle-packing programs and get respectable solutions.

I enjoyed this immensely because I like building systems that generate other systems, which I suspect is either a research interest or a mild personality disorder.

While I was doing this, coding agents themselves were becoming much better with much less custom machinery. Earlier software-engineering agents often wrapped the model in carefully designed interfaces: custom editing commands, repository-search tools, restricted action spaces and plenty of logic controlling how the model interacted with the machine. Then increasingly minimal systems began demonstrating how far a capable model could get with something much simpler: a shell.

The provocative version is that an agent with a shell has almost everything. It can `grep` to search, inspect files, run Python, apply patches, call Git, compose Unix tools and, if the tool it needs does not exist, write one. Bash is an entrance into decades of software accumulated underneath it.

This made me pause. The framework I was building—the parent selection, loop controller, experiment bookkeeping—was hard-coding behaviors that a sufficiently capable coding agent could increasingly perform itself. It could maintain notes, write helper scripts, explore several strategies, inspect failures and change direction.

I looked back at the machinery I had just spent time constructing and had the unpleasant thought engineers occasionally have after a productive week:

*Maybe I shouldn’t have built most of this.*

So I deleted the database machinery, controller loops and little pieces of software whose job was to make the agent behave like a researcher, and tried the stupidly simple version.

## The Coffee Test

I opened Claude Code in a directory containing the evaluator and gave it a high-level instruction along the lines of:

> Here is the evaluator for the circle-packing problem. Write a Python program that maximizes the score. You can research strategies, write tools, run experiments and iterate. Do not modify the evaluator. I will go get coffee.

Then I left.

That became the autonomy test I actually cared about. I already knew AI could help me solve the problem, and it could usually write code faster than I could. I wanted to know whether I could leave.

There is a difference between collaborating with an agent and *hiring* one. If I still have to choose every strategy, approve every experiment, rescue every failed branch and keep the search alive myself, then I have a formidable collaborator.

Circle packing gives us a rare luxury because the evaluator can stay behind when I leave. The agent can change its code, create scripts, abandon one approach, try another and waste compute on ideas that go nowhere. It was not allowed to redefine what counts as a valid packing because the current score hurts its feelings.

I call that requirement the **Immutable Harness**: everything inside the boundary can move, while the evaluator stays fixed. Telling the agent not to edit a file states the rule; it does not make the file immutable.

## Diagonal Layering

The agent did not execute one elegant master plan. It bounced around, which was encouraging.

It tried numerical optimization, changed initialization strategies and noticed that some optimizers repeatedly converged to poor local solutions. It experimented with the geometry of its starting configurations and mixed those constructions with numerical refinement. At different moments it was acting as orchestrator, researcher and engineer: deciding what to try, implementing the idea, running the experiment and using the result to choose what happened next.

Eventually one family of solutions began arranging circles in diagonal bands. We called the idea diagonal layering.

<!-- AUTHOR: this is the chapter's real scene and it is told from a distance. Needed from you: what you found when you came back from coffee, how long the run took, and what the diagonal bands actually looked like. -->

I had not instructed the agent to pursue that construction, and, more importantly, I had not selected the branch after it appeared. The agent found a direction, saw that it improved the evaluator and invested more of its search there.

I want to be careful with the word *discovered*. I had not seen that particular strategy before, but that does not establish historical novelty in computational geometry. For this experiment, the important discovery was local: the agent found a useful direction that I had not put into the plan.

Once that structural idea became strong enough, the nature of the work changed. The agent spent less time inventing new geometries and more time adjusting solver settings, tolerances, initialization details and all the boring machinery that suddenly matters when the last fraction of a percent becomes expensive.

<!-- ART RESOLVED — ch2-result. Original brief: DIAGRAM — missing figure: Code evolution result: iterative optimization. Original asset: ../resources/image0125.png; see resources/art-direction/missing-figures.md. -->

In our best run, the evaluator returned roughly 2.636, slightly above the 2.635 reference we had been using.

That sentence needs a fence around it. Under our evaluator, the result beat our reference. But the reference was a rounded figure: AlphaEvolve’s published construction sums to 2.63586, so at three decimals the two results are level. Calling it a new state of the art in circle packing would require matching problem definitions, checking numerical tolerances and constraints, reproducing the result properly and doing a more serious literature search than this experiment justified.

What I cared about was that the agent beat our reference without my writing the solution algorithm for it.

## The Algorithm Vortex

This is what I mean by the **Algorithm Vortex**. At the beginning of a conventional project, I might choose hill climbing, evolutionary search, simulated annealing, constrained optimization or a geometric heuristic. That early decision shapes everything downstream.

Once code is cheap to generate and evaluation is cheap enough to repeat, the choice no longer has to be permanent. A geometric construction can initialize a numerical optimizer. An evolutionary method can search parameters for another solver. A language model can notice a failure pattern and invent a repair procedure. Two ideas that began in separate lineages can meet later because an experiment suddenly makes the combination useful.

The search moves outward through levels. A conventional optimizer searches over candidate solutions. Meta-heuristics search over larger families of candidates and strategies. Code evolution searches over programs that themselves search for solutions. Once a capable agent controls the experimentation loop, even the decision about which kind of search to try next can enter the search space.

I no longer have to freeze the complete algorithmic architecture before the experiment begins. We stop writing one solver and start creating conditions in which solvers can compete, mutate, combine and occasionally surprise us.

Who was inventing the next move? For the first time in the experiment, not reliably me.

## The Contract

The coffee test gave the agent freedom over the search while requiring it to keep the evaluator fixed. After several runs, that structure settled into a small contract. It holds for a particular regime—bounded problems, cheap experimentation and an evaluator objective enough that the agent cannot charm its way around failure—and I wouldn’t carry it far outside that.

The first rule was to keep the harness immutable. If the agent can change the evaluator, the meaning of the experiment evaporates. The circles overlap? Perhaps tiny overlaps should count. The score is low? Maybe the square should be 1.03 wide. Only twenty-five circles fit? Perhaps twenty-six was merely an aspirational requirement. At that point we are no longer optimizing circle packing; we are negotiating with the specification. The solver, the strategy and the tools can all change, and the agent can decide yesterday’s entire approach was stupid and start again, but the thing that says whether it worked has to stay harder to change than the thing being optimized.

The second rule was about me: never write solution code yourself. I would watch the agent try something mediocre and immediately think of a better approach. Sometimes helping is right. But every time I jumped in with my own solution, the search became a little more like whatever had occurred to me first, and I wanted independent directions badly enough to resist becoming the senior engineer on every branch. I could change the conditions of the search without intervening in every idea.

Then came the balance between sharing and pruning. Independent branches create diversity, but perfect isolation wastes learning: if one branch finds a useful initialization and another a better local optimizer, later experiments should be able to inherit both. Broadcast every successful idea immediately, though, and the population starts thinking in the accent of the first successful branch, so some lineages should stay ignorant long enough to surprise you.

Cross-pollinate, then prune. A branch that keeps underperforming and contributes nothing interesting should eventually die so compute and attention can move elsewhere. Kill too early and you may lose an immature idea that needed another generation; keep everything alive and you end up funding a large family of increasingly sophisticated failures.

The last rule was discovery before polish. Early on I want large conceptual moves: a different geometry, solver, representation or decomposition. Once a strong direction appears, the valuable work gets smaller and more boring—solver tolerances, initialization details, numerical settings, tiny modifications that are pointless on a bad idea and extremely valuable on a good one. Diagonal layering made the switch obvious. There is no point polishing a local optimum you should abandon, or demanding revolution from a solution that has already found the right mountain and merely needs to climb it.

## Zero Framework, With an Asterisk

I started calling this direction **zero framework**. It’s a great slogan. It’s also not really true.

I meant that I was writing almost no custom orchestration framework, which is very different from having no framework. Claude Code is itself a substantial system. The underlying model has absorbed enormous amounts of software and problem-solving knowledge. Bash, Python, SciPy, Git and the operating system represent decades of accumulated engineering. The evaluator is custom machinery. Even the supposedly trivial act of running a program and inspecting a result depends on layers we have become so accustomed to that we stop seeing them. The framework didn’t vanish; it became somebody else’s primitive.

That fits the emergence argument almost suspiciously well. A tiny amount of code at the top can command enormous capability underneath because previous generations of complexity have already been compressed into tools.

So yes, zero framework: Bash is enough, with the asterisk that Bash contains roughly half a century of civilization.

## The Easy Version of Autonomy

The coffee test is not a license to give Claude a shell in production and go for a very long lunch. I could leave because the evaluator stayed behind, enforcing constraints I had chosen. Substantial control over the search moved into the agent; control over what counted as success did not.

That is why circle packing is the easy version of autonomy. The evaluator returns one number, and if version B beats version A, nobody has to convene a committee to decide whether the new solution is spiritually aligned with the learning objectives. The harness tells the agent when it is wrong.

When success is harder to judge, the agent can still generate alternatives, branch and search among them. It also has to find a way to decide which one is better. What happens when the world gives us no clean referee and judgment itself has to be constructed?

---

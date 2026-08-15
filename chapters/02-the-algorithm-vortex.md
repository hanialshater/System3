# Chapter 2: The Algorithm Vortex

*From Classic Algorithms to Autonomous Discovery*

![The algorithmic vortex](../resources/image0135.png)

*The algorithmic vortex*

Once you discover AI coding, there's no going back.

It is faster than you at a ridiculous number of things. It knows libraries you forgot existed. It can stare at a stack trace and notice something you have been ignoring for an hour. Then, five minutes later, it does something unbelievably stupid, believes the stupid thing completely, and builds three more decisions on top of it.

This is the strange reality behind all the vibe-coding excitement. The machine is extremely capable, but you are still there. You check the architecture. You notice the missing case. You tell it that no, we are not redesigning the database because one button is the wrong color. You keep enough of the project in your own head to notice when the agent quietly wanders into another universe.

So the question from the previous chapter becomes practical very quickly. If I want more autonomy, where can I actually give it without spending the whole time babysitting the autonomy?

Production software is almost the worst place to answer that question. A supposedly simple task may involve deployment, legacy systems, users, security, another team's API and a requirement nobody wrote down because everyone assumed everybody else knew it. If the agent fails, you often don't even know whether the problem was intelligence, infrastructure, missing context, or the fact that someone named a database column `new_status_final_2`.

I wanted something cleaner: a hard problem, but contained. Something where I could genuinely say, "figure it out," and still have an objective way to know whether whatever came back was any good.

Algorithms are almost perfect for this. The search can be brutally difficult while the evaluator remains wonderfully stupid.

And that is how I ended up spending an unreasonable amount of time packing circles into a square.

## How Did We Get Here?

I know you are here for agent autonomy, not because you woke up this morning thinking, *I really need a deeper understanding of geometric crossover*. Unfortunately, we need to spend some time inside the problem, because the interesting part of the agent story only becomes obvious once you see what humans normally have to invent.

Circle packing gives us a surprisingly good tour through the history of problem-solving. For a long time, the relationship was straightforward: a human understood the problem, invented an algorithm and wrote it down. When direct algorithms were not enough, we invented optimization procedures and heuristics that searched for good solutions. Machine learning added a different kind of machinery, one that could learn useful structure instead of having every useful representation specified by hand.

Now language models can write and modify the search procedure itself.

That is where the relationship begins to change.

![History of algorithm design](../resources/image0136.png)

*History of algorithm design*

The old methods do not disappear. Exact algorithms remain useful. Optimization remains useful. Evolutionary search remains useful. Neural methods remain useful. The interesting possibility is that we no longer have to choose one family in advance and hope we picked the right religion.

Circle packing will make this less abstract.

## The Running Example: Circle Packing

![Citrus packing - a real-world example](../resources/image0138.png)

*Citrus packing — a real-world example*

The problem is simple enough to explain to a child. Take 26 circles and put them inside a square. None may overlap, none may cross the boundary, and the circles do not have to be the same size. We want to maximize the sum of their radii.

That's the whole thing. No customers, no authentication, no stakeholder arriving after the first demo to explain that what they *really* wanted was the opposite of what they originally asked for.

Just circles.

Unfortunately, the solution space is nasty. Every circle has a position and a radius, and nearly every decision affects several others. Increase one radius and two neighbors may overlap. Move a neighbor and something else now needs to move. A packing can look almost perfect while being trapped in a configuration where every obvious improvement makes the solution invalid.

For the experiments in this chapter, we had a strong reference score around **2.635** under the evaluator we were using.

![Circle packing solution n=26](../resources/image0139.png)

*Circle packing solution n=26*

*Figure: A strong reference packing for the 26-circle objective, scoring approximately **2.635** under our evaluator.*

This is what makes the problem useful for studying autonomy. Searching is hard, but judging is cheap. The evaluator does not care whether the agent has a persuasive explanation for why two circles ought to overlap slightly in the name of geometric inclusivity. It checks the constraints and returns a score.

There is something deeply comforting about an evaluator with no personality.

### First Idea: Hill Climbing

If I gave you a rough packing and asked you to improve it manually, one obvious strategy would be to make small changes. Move a circle slightly, increase a radius, see whether the result is still valid, keep it if the score improves and undo it if it doesn't.

That is hill climbing.

The algorithm is almost embarrassingly reasonable:

1. Start with a valid solution.
2. Perturb a position or radius.
3. Check whether the result is valid.
4. Keep it if the score improves.
5. Repeat.

Early in the search, this works nicely. There is empty space and plenty of room to improve. Later, as the circles become tightly packed, almost every interesting move creates an overlap.

![Hill climbing progression](../resources/image0140.png)

*Hill climbing progression*

*Figure: Early mutations are often accepted, but as the packing tightens, valid improvements become increasingly rare and the search stalls.*

In one simple run, the score climbed from around 1.33 to roughly 2.26. That is not terrible, but it is also nowhere near 2.635.

Hill climbing is not failing because it is stupid. It is doing exactly what we asked: improving the solution immediately around it. The problem is that the current solution may live in the wrong part of the search space. Reaching a much better packing may require temporarily moving through configurations that look worse, or jumping to a structure that cannot be reached through a sequence of tiny improvements.

This turns out to matter far beyond circle packing. A system can become very competent at improving the thing in front of it while never questioning whether the thing in front of it is the right thing to improve.

For now, though, the fix is simpler. Instead of one trajectory, keep many.

## Evolutionary Algorithms

Hill climbing gives one candidate a very long life. Evolutionary methods keep a population.

Instead of dropping one climber into the landscape, imagine dropping a hundred. Some start in terrible places, some find decent regions, and a few may stumble into structures a single search would never encounter.

The biological vocabulary is familiar: population, mutation, selection, crossover. The metaphor is optional. What matters is that diversity prevents the whole search from inheriting the history of one initial guess.

For circle packing, mutation is easy enough to imagine. Move circles. Change radii. Perturb several values at once.

Almost immediately, however, we run into a practical problem: most interesting mutations break the packing. Two circles overlap, or one moves outside the square. The mutation may point toward an interesting arrangement, but the result is invalid.

So we added **virtual forces**. When circles overlap, imagine them repelling one another. After a mutation or crossover, run a small repair procedure that pushes them away from collisions and back inside the boundary.

This helps a lot, but notice what happened. The evolutionary algorithm did not discover virtual forces. We did.

Then we reached crossover.

Suppose Parent A and Parent B both contain useful geometric structure. How do we combine them? The naive solution is to pair circle 0 from one parent with circle 0 from the other, circle 1 with circle 1, and so on.

That is usually nonsense because circle numbering is arbitrary. Two nearly identical geometric arrangements may store corresponding circles at completely different indices.

So we used **bipartite matching**. Rather than pair circles by position in an array, pair them according to their geometric role in the packing. The Hungarian algorithm gives us an efficient assignment, after which crossover has some chance of combining meaningful parts of the two parents instead of averaging unrelated circles and asking geometry for forgiveness.

![Naive vs Geometric Crossover](../resources/image0141.png)

*Naive vs Geometric Crossover*

*Figure: Naive crossover pairs circles by array index and often destroys useful structure. Geometric matching tries to identify corresponding circles before combining the parents.*

Now we can evolve a population: mutate, repair, cross, select and repeat.

![Evolutionary strategies with Bipartite Matching crossover](../resources/image0122.png)

*Evolutionary strategies with Bipartite Matching crossover*

*Figure: Starting around 2.08, the evolutionary search reaches roughly 2.45 in this experiment—much better than the simple hill climber, but still below our reference.*

This is already much stronger than hill climbing. It is also where I started noticing a problem with my own role.

Every time the search became substantially better, I had added something important to it. I decided we needed repair. I decided how crossover should respect geometry. I chose the representation.

The optimizer searched, but I was still inventing most of the useful moves.

### MAP-Elites: Don't Kill Weird Ideas Too Early

Ordinary evolutionary search has another problem. If you maintain 100 solutions and repeatedly keep only the highest-scoring ones, the population eventually starts looking like one large extended family.

That can be excellent for exploitation and terrible for discovering a genuinely different strategy.

MAP-Elites takes a different approach. Instead of ranking every candidate on one axis and keeping only the winners, you describe solutions along a few behavioral dimensions and preserve the best candidate in different regions of that space.

For circle packing, perhaps one dimension measures symmetry and another measures how much circle sizes vary. One part of the archive may contain highly symmetric solutions. Another may contain asymmetric solutions with several large circles. Somewhere else may sit an ugly packing with a mediocre score and one strange structural idea that becomes useful five generations later.

![MAP-Elites archive visualization](../resources/image0123.png)

*MAP-Elites archive visualization*

This is quality-diversity search. The idea is not merely to preserve the current winner, but to keep qualitatively different directions alive long enough to discover whether any of them become interesting.

I like this because optimization is often unfair to immature ideas. A new approach can initially perform badly simply because nobody has polished it yet. If the first respectable solution immediately kills everything else, the search can become very efficient at discovering one family of answers.

But MAP-Elites introduces another human choice: what dimensions define the archive?

Symmetry? Radius variance? Number of large circles? Something topological? Something I haven't thought of?

Again the machinery is getting sophisticated, but the choice of *how to search* still depends heavily on us.

That became the real bottleneck.

## The Invention Problem

By this point, the symbolic search system was fairly capable. We had hill climbing, population search, repair, geometric crossover and quality-diversity archives. We could evaluate a huge number of candidate packings and explore far more of the space than any human would inspect manually.

Yet every substantial conceptual jump came from somebody noticing something.

Someone had to invent the repair mechanism. Someone had to decide that geometric matching was a useful way to crossover two packings. Someone had to choose what kinds of diversity were worth preserving.

This is where traditional search reaches its natural boundary. It can explore very effectively once we define the representation and the legal moves, but sometimes the representation and the moves are exactly the things we need to rethink.

That is where neural models become interesting.

I once asked an image-generation model to produce a picture of a circle-packing solution. This was not a serious benchmark; I have no idea what related examples it may have encountered during training, and I can already hear Reviewer 2 clearing his throat.

I wanted to see something simpler: did the model have any useful geometric intuition about what a dense packing should look like?

Surprisingly, yes. It generated something that looked like a plausible packing. The circles had structure. The spacing looked intentional. If you glanced at the image, you could believe the model understood the problem.

Then you counted the circles.

Wrong number.

Some constraints were violated.

It was a beautiful answer to a nearby problem.

That little experiment captures something useful about learned models. They can be remarkably good at producing plausible structure without guaranteeing that every formal requirement survives the generation process.

A symbolic optimizer has the opposite personality. Give it a precisely defined representation and constraints and it will obey them. What it will not naturally do is decide that your representation is unimaginative.

So instead of choosing between neural intuition and symbolic rigor, I wanted to put them in the same loop.

The useful move was to stop asking the model to produce the packing directly.

Ask it to write the program that produces the packing.

## Let the Model Write the Solver

A candidate no longer needs to be only a list of circle positions and radii:

```text
(x1, y1, r1), (x2, y2, r2), ...
```

It can be an entire program:

```text
solve_circle_packing.py
```

One program may use constrained optimization. Another simulated annealing. Another a geometric construction. Another may combine a hand-designed initialization with numerical refinement.

The evaluator does not need to care which family of algorithms produced the solution. It runs the program, checks the geometry and scores the result.

This gives the language model a much more interesting role. Rather than randomly perturbing numbers, it can read the program, form a rough theory about why it underperforms and modify the algorithm.

Perhaps the optimizer keeps converging badly because the initialization is weak. Change the initialization. Perhaps a geometric construction gets close but leaves local slack. Add a numerical optimization phase afterward. Perhaps one repair procedure keeps destroying useful structure. Replace it.

The mutation is no longer only numeric. It can contain an idea expressed in code.

That is the basic neuro-symbolic move behind systems such as FunSearch and AlphaEvolve. The language model proposes changes at the level where code has meaning; execution and the evaluator decide whether any of those ideas were actually useful.

## AlphaEvolve

AlphaEvolve turns that basic loop into a much larger search process.

Imagine one generation. The system picks a promising program from its archive, perhaps along with a few other successful but different programs that may contain useful ideas. The model sees the current code, examples of what has worked, and the scores produced by previous attempts. Instead of rewriting everything, it proposes a patch: modify the initialization, add a search stage, replace a heuristic, combine one useful component with another.

The patch is applied, the program runs, and the evaluator scores the result. That program—and the information about how it performed—goes back into the archive. Then the loop repeats, thousands of times.

![AlphaEvolve architecture](../resources/image0124.png)

*AlphaEvolve architecture*

The diff-based mutation is important. Real programs have structure worth preserving. If every generation rewrites the whole file, useful ideas disappear as easily as bad ones. Small patches let the system change the part it thinks matters while leaving the rest intact.

The archive matters for the same reason the population mattered earlier. If the current winner becomes the parent of everything, diversity collapses. Keeping multiple lineages alive gives the search a chance to combine ideas that mature at different speeds.

What the LLM adds here is a much richer mutation operator. It does not merely change syntax according to a fixed rule. It can look at the code and make a semantic guess about why it might be failing.

Sometimes the guess is excellent. Sometimes it produces nonsense wrapped in perfectly respectable Python. The advantage of our setting is that the argument does not need to be settled in prose. We run the program.

This kind of code evolution has already produced impressive results in algorithm design and mathematical search. What interested me most, though, was what happened to the human.

Instead of writing the algorithm, I was increasingly building the machinery in which algorithms could be generated, compared and improved.

That sounded suspiciously like the bet from Chapter 1.

So, naturally, I built one.

## My First Version: Build All the Machinery

My instinct was predictable.

I started building the framework.

A database of programs. Prompt sampler. Evaluation loop. Selection. Mutation prompts. Crossover. Archive management. I used Aider and other coding agents to help recreate the core ideas, and it worked. We could evolve circle-packing code and get respectable solutions.

I enjoyed this immensely because I like building systems that generate other systems, which I suspect is either a research interest or a mild personality disorder.

While I was doing this, coding agents themselves were getting much better with much less custom machinery.

Earlier software-engineering agents often wrapped the model in carefully designed interfaces: custom editing commands, repository-search tools, restricted action spaces and a lot of logic guiding how the model interacted with the machine.

Then smaller, more minimal agents began showing that capable models could get surprisingly far with something much simpler.

Give them a shell.

Search with `grep`. Inspect files. Run Python. Apply a patch. If a useful tool doesn't exist, write it.

The shell is already a very rich environment because decades of software engineering have made useful operations composable. Once the model is competent enough to navigate that world, some of the scaffolding we used to build around it starts looking optional.

I looked back at the code-evolution framework I had just spent time constructing and had the unpleasant thought engineers occasionally have after a productive week:

*Maybe I shouldn't have built most of this.*

The framework knew how to choose a parent, run an evaluator, store a score, compare approaches and create another experiment. But a capable coding agent can understand those instructions too. It can keep notes, run scripts, create helper tools, explore several approaches, inspect results and change direction.

Some of the behavior I was carefully encoding in Python might already be present in the model.

So I deleted most of my orchestration code and tried the stupidly simple version.

## The Coffee Test

I opened Claude Code in a directory containing the evaluator and gave it a high-level instruction along the lines of:

> Here is the evaluator for the circle-packing problem. Write a Python program that maximizes the score. You can research strategies, write tools, run experiments and iterate. Do not modify the evaluator.

Then I went for coffee.

This became the autonomy test I actually cared about. Not whether AI could help me solve the problem; that was already obvious. Not whether it could write code faster than I could; usually it could.

I wanted to know whether I could leave.

If I still had to choose every strategy, approve every experiment, rescue every failed branch and keep the search alive myself, then I had a very powerful collaborator. That is valuable, but it is not the kind of autonomy I was trying to understand.

Circle packing gives us a rare luxury because the evaluator can stay behind when I leave. The agent can change its code, create scripts, abandon an approach, try another one and waste compute on something that turns out to be useless. It cannot redefine what counts as a valid packing or quietly edit the scoring function because the current score hurts its feelings.

For this kind of problem, that fixed harness makes a surprising amount of freedom tolerable.

## What Happened

The agent did not execute one elegant master plan. It bounced around, which was encouraging.

It tried numerical optimization, changed initialization strategies and noticed that some optimizers repeatedly converged to poor local solutions. It experimented with the geometry of the starting configurations and mixed those constructions with numerical refinement.

Eventually one family of solutions began arranging circles in diagonal bands. We called the idea **diagonal layering**.

I had not instructed the agent to pursue that particular construction. The interesting part for me was not whether the geometry itself was historically novel; it was that the agent found a direction, saw an improvement and decided to invest more of its search there without me selecting the branch.

Once the structural idea became strong enough, the work changed character. The agent spent less effort inventing new arrangements and more time on solver settings, tolerances, initialization details and other details that are boring until the last fraction of a percent matters.

![Code evolution result](../resources/image0125.png)

*Code evolution result: iterative optimization*

In our best run, the evaluator returned roughly **2.636**, slightly above the **2.635** reference we had been using.

I want to be precise about that sentence. Under our evaluator, the score was better than the reference. Calling it a new state of the art in circle packing would require much more work: matching problem definitions, checking constraints and tolerances, reproducing the result properly and doing a much more serious literature search than I needed for this experiment.

The smaller claim is enough.

The agent found a solution that beat our reference while I was not writing the solution algorithm for it.

That was the result I wanted.

## The Algorithmic Vortex

This is what I mean by the Algorithm Vortex.

At the beginning, I can choose hill climbing, evolutionary search, simulated annealing, constrained optimization or some geometric heuristic. Traditionally that choice happens early and determines much of what follows.

Once code is cheap to generate and evaluation is cheap enough to run repeatedly, the choice does not need to be permanent. A geometric construction can initialize a numerical optimizer. An evolutionary method can search the parameters of another solver. A language model can notice a failure pattern and create a repair procedure. Two ideas that began in separate lineages can be combined after an experiment makes the connection useful.

The search keeps moving outward. A normal optimizer searches over candidate solutions. Meta-heuristics search over larger spaces of solutions and strategies. Code evolution lets us search over programs that themselves search for solutions. Once a capable coding agent controls the experimentation loop, even the decision about which kind of search to try next can become part of the process.

There are still algorithms everywhere in this picture. The difference is that I am no longer forced to decide the full algorithmic architecture before the experiment starts.

I define the problem and the evaluator, provide the environment, and let much more of the machinery in between move.

That is the vortex.

## The Contract

After running these experiments a few times, I ended up with a small set of rules that worked unusually well for bounded problems where experimentation was cheap and the evaluator was objective enough that the agent could not charm its way around it.

### Don't solve the problem for the agent

This is harder than it sounds. You watch the agent try something mediocre and immediately think of a better approach. You want to help.

Sometimes you should. But every time I jump in with my own solution, the search becomes a little more like whatever I happened to think of first.

For these experiments, I wanted different directions badly enough that I had to resist becoming the senior engineer on every branch.

Long-running agents have their own version of this problem. Once the context contains twenty minutes of reasoning about one architecture, every new instruction gets interpreted through that architecture. Fresh sub-agents can be useful precisely because they don't know why yesterday's bad idea seemed so compelling.

### Keep the evaluator immutable

This one is much less negotiable.

If the agent can change the harness, the meaning of the experiment disappears quickly. The circles overlap? Perhaps tiny overlaps should count. The score is low? Maybe the square should be 1.03 wide. Only 25 circles fit? Perhaps 26 was merely an aspirational requirement.

At that point we are no longer optimizing circle packing. We are negotiating with the specification.

For bounded problems, the immutable evaluator gives the agent somewhere it cannot simply reinterpret failure.

### Let successful ideas travel

Independent search gives diversity, but perfectly isolated search wastes information.

If one branch discovers a useful initialization and another finds a better local optimizer, future experiments should have some way to inherit both. This is where code evolution becomes more interesting than asking the same model the same question 100 times.

The subtle part is that sharing everything immediately can also collapse diversity. Sometimes one branch should remain ignorant of the dominant approach long enough to discover something different.

There is no magic setting here. It is another design choice in the search.

### Kill things

Diversity is useful. Preserving every bad idea forever is hoarding.

If a branch keeps underperforming and is not producing anything interesting, eventually it should die so the compute and attention can move elsewhere.

The hard part is timing. Kill too quickly and you may discard an immature idea that needed another generation. Keep everything forever and you end up funding a large family of increasingly sophisticated failures.

Search needs enough patience for novelty and enough cruelty for budget control.

### Separate discovery from polish

Early in a search, I want large conceptual changes: different geometry, different solvers, different representations.

Once a strong direction appears, the useful work becomes smaller and more boring. Solver tolerances. Initialization details. Numerical settings. Tiny modifications that are pointless on a bad idea and extremely valuable on a good one.

The diagonal-layering run made this obvious. Once the structural direction looked promising, continuing to invent entirely new geometries became less useful than squeezing more performance from the one that was already working.

Those are different modes of work, and confusing them wastes a lot of time.

## Zero Framework?

I originally described this experiment as "zero framework."

That is catchy and not really true.

I wrote almost no custom orchestration framework. That is different from having no framework.

Claude Code itself is a substantial system. The underlying model has absorbed enormous amounts of software and problem-solving knowledge. Bash, Python, SciPy, Git and the operating system represent decades of accumulated engineering. The evaluator is custom machinery. Even the supposedly simple act of running a program and inspecting the result depends on layers we have become so used to that we stop noticing them.

The framework did not vanish. Most of it had already become somebody else's primitive.

That fits the recursive pattern from Chapter 1 rather nicely. A tiny amount of code at the top can command enormous capability underneath because previous generations of complexity have already been compressed into tools we treat as normal.

This is worth remembering whenever somebody shows you an agent implemented in 100 lines of Python. The 100 lines may be perfectly real. So is everything underneath them.

## What Did We Actually Learn?

It would be easy to overread the experiment.

We did not prove that coding agents can autonomously solve arbitrary research problems. We did not prove that AlphaEvolve-style frameworks are obsolete. We did not prove that diagonal layering is some historically novel result in computational geometry.

We had a bounded problem where evaluation was cheap and clear, gave a strong coding agent substantial freedom, and found that a surprisingly large fraction of the experimentation loop could happen without us directing each step.

That is enough for me.

The agent could propose an approach, implement it, run it, inspect the result, abandon it, create tools and try something else. My role moved away from writing the algorithm and toward defining the job, preserving the evaluator and watching what came back.

That is already a meaningful change.

It also explains why circle packing is the easy version of autonomy.

The evaluator gives us one number. If version B beats version A, nobody needs to simulate a confused student, debate whether the interface feels intuitive or ask a committee whether the new solution is spiritually aligned with the learning objectives.

The search can be complicated because judgment is simple.

Most things I want agents to build are not that generous.

"Make a good educational demo."

"Write something people remember."

"Design a useful product."

"Explain this so somebody finally understands it."

The agent can still generate alternatives and search among them, but now the difficult question changes.

How does it know which direction is actually better?

That is where the next chapter begins.

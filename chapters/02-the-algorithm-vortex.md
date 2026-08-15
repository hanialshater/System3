# Chapter 2: The Algorithm Vortex

*From Classic Algorithms to Autonomous Discovery*

![The algorithmic vortex](../resources/image0135.png)

*The algorithmic vortex*

Once you discover AI coding, there's no going back. It's faster than you. It knows more libraries. It debugs patterns you wouldn't see. But there's a problem: it is not autonomous, it makes silly mistakes and builds on them, and you end up babysitting the project, which means you need to spend tons of effort to make sure it matches what you need, covers all the cases, and sets the right architecture. Vibe coding is very promising, but in reality most developers found it introduces big problems they didn't have before.

But there's a specialized slice of work where AI becomes genuinely powerful: *bounded problems*. These are small to mid-scale, require advanced thinking and deep expertise, but don't demand full production infrastructure. Think: algorithms to design, articles to write, marketing materials, demos, educational content. Extremely hard problems, but contained in scope.

People are discovering the potential here. Compound systems—also called agents—have shown remarkable progress. AlphaCode ranked in the top 54% of competitive programmers. AlphaCode 2 improved to top 15%. Agents like Claude Code solve real GitHub issues at high rates (80% on SWE-Bench).

But these are still collaborative. You partner with the AI. You direct. It executes.

Then something shifted. A new class of agents emerged—ones you can actually *hire*. They don't ask permission. They research different strategies, test them, report results. AlphaEvolve pioneered this by combining LLM reasoning with evolutionary strategies. Instead of randomly mutating solutions, it understands algorithms semantically and proposes intelligent improvements. It achieved state-of-the-art on many problems that involve algorithm design. Including kernels for deep learning inference, matrix multiplication, and more.

Most remarkably, Terence Tao and collaborators at Google DeepMind published a paper showing AlphaEvolve helping solve hard mathematics problems. Tao's expertise was still essential—this isn't fully autonomous—but it represents the most hands-off collaboration experience we've had. The system researched, tested, iterated very complex problems with minimal direction.

---

## How Did We Get From Classic to Autonomous Agent?

This chapter walks through three distinct philosophies for tackling bounded problems that build upon each other. I will be using **circle packing** as our running example: basically, you have a square and you want to place k circles inside it, without overlapping but maximizing the sum of radii.

![History of algorithm design](../resources/image0136.png)

*History of algorithm design*

*Figure: The history of algorithm design—from Pólya's systematic problem-solving (1945) through the NP-Hard wall (1971), meta-heuristics (1980s), to modern neuro-symbolic methods (2020s).*

We are currently in a problem-solving methodology vortex where we have more options than ever to solve bounded problems. It starts with **Symbolic Methods** (1950s—Present), the rigorous foundation where we build the logic using specific algorithms or generic meta-heuristics to explore the solution space. This evolved into **Neural Methods** (2010s—Present), pure intuition where we ask a model to "imagine" a solution, getting creativity without guaranteed validity. Today, we see **Neuro-Symbolic & Agentic** methods (2023—Present), the hybrid where we use the semantic power of LLMs (the brain) to *invent* and *optimize* symbolic code (the body). This leads us to **Agent Autonomy**—where we stop writing the solver and start hiring the agent to research it for us.

![Problem-solving methodology landscape](../resources/image0137.png)

*Problem-solving methodology landscape*

*Figure: The problem-solving landscape. Symbolic methods (algorithms, solvers, meta-heuristics) provide rigor. Neural methods (LLMs, generative models) provide intuition. Neuro-Symbolic and Agentic systems combine both, enabling compound systems that can reason, generate, and self-correct.*

### Approach 1: Classic Symbolic Methods (Search & Optimization)

This is classic problem solving popularized with Pólya's systematic method from his 1945 masterpiece *How to Solve It*. His message is simple and powerful: problem-solving isn't magic. It's a learnable skill. Understand the problem. Devise a plan. Carry it out. Reflect on what worked.

For decades, this worked beautifully. You'd sit down with circle packing and think: *What are the constraints? What patterns emerge? Can I design a strategy?* Then you'd code it. Done. For simple problems (sorting a list, finding the shortest route), this approach is elegant and efficient.

**Then you hit the wall.**

Here's the hard reality: most **bounded problems** are so called *NP-hard* (computationally intractable). Loosely speaking, even if you're the smartest person alive, there's no way to design an algorithm to find the optimal solution without checking all possible combinations. Circle packing is one of these hard problems. Think of it this way: if you have 26 circles and a square, there are more possible arrangements than atoms in the universe. You can't check them all. Pólya's systematic method assumes you can think your way to the answer. For NP-hard problems, you can't. There's no clever trick. No hidden pattern. Just exponential complexity. But here's the catch: these problems are impossibly hard, yet humans can find reasonably good solutions. What's going on?

Stay calm—science isn't broken. It turns out that for most problems, you can find approximate solutions in reasonable effort. Loosely speaking, problem-solving evolved into two ways:

**Approximation algorithms.** These give you *provably good* solutions—you might not get the absolute best, but you know you're within, say, 90% of optimal. The problem is circle packing isn't one of them. It doesn't have a clean approximation algorithm with guarantees.

**Optimization and Meta-heuristics.** Researchers stopped asking "Can we design the perfect algorithm?" and started asking "What if we just *explore intelligently*?" They invented techniques like hill climbing (keep improving locally), genetic algorithms (evolve populations), and simulated annealing (random jumps that cool down) or sometimes use optimization techniques like gradient descent (follow the slope) or Linear Programming (solve constraints mathematically). These methods don't try to find the absolute best solution. Instead, they try to find a *really good* solution, fast. They can get stuck in local optima (good-but-not-best dead ends)—you might not know how far you are from the global optimum or understand exactly why a solution works. But they're pragmatic: they work.

All of these—classic algorithms, approximation algorithms, solvers, and meta-heuristics—are **symbolic methods**: methods that can be represented through symbols, written as code, and executed deterministically. You control them. You design and run them with confidence.

Symbolic methods have dominated for a very long time and remain useful. But they demand deep expertise: algorithm design, programming, mathematics, and optimization theory. And even then, it's challenging to produce truly good solutions.

**The real advantages:** Symbolic methods are rigorous, fast, and grounded in science. You can prove properties about them. You can analyze their complexity. You can reason about why they work. When you run a genetic algorithm with known mutation rates and selection pressure, you understand the mechanics. The code is transparent. You can debug it. You can improve it incrementally. This is powerful—it's why symbolic methods still dominate in engineering where trust and auditability matter.

The problem is: they require *you* to be the expert. You have to know or discover the right approach.

### Approach 2: Pure Machine Learning (Learned Intuition)

The idea is seductive: humans solve hard problems with intuition alone. So mimic that—stop designing algorithms. Just feed a neural network thousands of algorithmic problems. Let it learn patterns the way humans do.

And just to give you an idea of how powerful this is, I asked Gemini to generate an image of a circle packing solution. I doubt that Gemini image generation was trained on such problems so this would be a stretch test, but it still managed to generate a surprisingly good solution—circles placed well, the intuition right, and the basic structure working. But it's not a valid solution: it has extra circles and violates the constraint count. The point is, neural networks have good intuition about solutions. This could be handy for quick prototypes or to guide algorithms in complex search spaces.

But here's the problem: this approach treats ML as the master algorithm—the one solution for everything. And even though it's quite powerful, it's more expensive, data-hungry, and not grounded in science. That leads to fundamental questions about validity, rigor, stability, and why it works. Unlike symbolic methods, pure ML is not easy to reason about, you can't prove properties, debug failures, or analyze complexity.

### Approach 3: Neuro-Symbolic (Intuition + Rigor)

This is where things get interesting. What if you didn't ask the network to solve the problem *directly*? What if you asked it to *suggest a direction*?

The idea: neural networks generate code, treat each piece of code as a solution in a search space, and explore solutions using meta-heuristics. That is neuro-symbolic—the hybrid. It has strong intuition that handles novel situations, able to generate code with the symbolic rigor.

The naive approach is to ask an AI agent to solve the problem 50 times and take the best code it generates. That's not great, but Google did something similar with AlphaCode to win competitive programming competitions (though they generated millions of solutions). But that's old news. Now they're doing something much smarter with their newer AlphaEvolve method, which we will explore in detail later.

I know you are here for agent autonomy not to learn about circle packing, however, I want to cover some fundamental ideas that let you better design your own code evolution agent, so let's work a bit on circle packing and see how we can use meta-heuristics to solve it. This will reveal the powerful ideas that underpin advanced code evolution agents like AlphaEvolve.

---

## The Running Example: Circle Packing

![Citrus packing - a real-world example](../resources/image0138.png)

*Citrus packing - a real-world example*

*Figure: Circle packing in the real world. 13 citrus slices of varying sizes arranged to maximize coverage on a square slate. The same challenge algorithms face—fit as much as possible without overlap.*

The problem is simple to state: Pack 26 circles into a unit square [0,1]x[0,1] such that no circles overlap and none extend outside the boundary. Maximize the sum of all circle radii. Simple to state. Deceptively hard to solve.

Why is this hard? Because the solution space is a nightmare of local optima. Place circles randomly and use gradient descent? You hit a local maximum quickly—maybe 80% of the optimal score. Use a greedy algorithm that fills space left-to-right? You hit around 85%. Even clever heuristics plateau early.

Mathematicians have studied circle packing for decades. For small numbers of circles (n < 30), the optimal or near-optimal solutions are known. But finding them computationally is hard. You need a strategy that explores the solution space intelligently, not randomly.

![Circle packing solution n=26](../resources/image0139.png)

*Circle packing solution n=26*

*Figure: A near-optimal circle packing for n=26 with benchmark score **2.635**.*

### First Idea: Hill Climbing

When you solve circle packing manually, you might try this: start with a grid initialization, optimize locally with gradient descent, check the result. You climb the performance hill.

**The Hill Climbing Algorithm:**

1. Take a solution.
2. Slightly **perturb** the position (x, y) or radius (r) of a circle.
3. Check if the new solution is **valid** (no overlaps, inside boundary).
4. If valid and better (higher total radius), **accept** it. Else, reject it.

This sounds reasonable, but as you can see in the figure below, it quickly gets frustrating. Early on, it's easy to make improvements—acceptance rate is around 40%. But as things get tighter, finding a valid move becomes nearly impossible. Rejection rate skyrockets to over 90%, and you simply get stuck. Circles become stuck in local optima and no matter how you move them you end up in an invalid solution.

![Hill climbing progression](../resources/image0140.png)

*Hill climbing progression*

*Figure: Hill climbing gets stuck. Starting from small circles (1.330), the algorithm mutates positions and radii, accepting improvements. Early on, 40% of mutations are accepted. After 2000 iterations (score: 2.260), only 8% are accepted—the algorithm has converged to a local optimum, far from the benchmark (2.635).*

### Evolutionary Algorithms

Hill climbing fails because it puts all your eggs in one basket. You have one solution, and if it gets stuck, you're done.

Evolutionary strategies change the game by using a **Population**. Instead of one climber, imagine dropping 100 climbers all over the mountain range.

Some will land in valleys. Some on small hills. A few may land near the highest peak.

This parallel exploration is powerful. Most climbers will try to climb, and they will exchange ideas with other climbers. This class of algorithms is called **Evolutionary Algorithms**—a general optimization strategy inspired by patterns of selection and adaptation observed in nature.

Here are a few concepts that are used in evolutionary algorithms:

**1. Population (Diversity):** We maintain a pool of e.g., 100 competing solutions. This prevents the tunnel vision of hill climbing.

**2. Mutation:** Randomly perturbing circle positions and radii to see if that helps the solution improve.

**3. Crossover:** Share ideas between solutions.

**4. Selection:** Choose the best solutions to continue to the next generation.

So let's apply this to our circle packing problem.

1. **Population:** We start with a population of 100 solutions.
2. **Mutation:** We mutate each solution slightly and see if it helps the solution improve. Often creates invalid solutions (overlaps). We use **Virtual Forces** to fix these issues. After mutation or crossover, if circles overlap, they exert repulsive forces on each other. We iteratively apply these forces to fix the solution, pushing circles into valid positions.
3. **Crossover:** We share ideas between solutions. Sharing ideas between two circle packing solutions is not a simple task. If you just swap the circles between the solutions you will destroy the geometric structure of the solution. Instead, we use **Bipartite Matching Crossover**. Think of it as finding the correct partner for each circle. Instead of pointing at index 0 in both lists, we ask: "Which circle in Parent B is the geometric equivalent of this circle in Parent A?"
4. **Selection:** We choose the best solutions to continue to the next generation.

![Naive vs Geometric Crossover](../resources/image0141.png)

*Naive vs Geometric Crossover*

*Figure: Naive vs. Geometric Crossover. Left: Naive matching relies on index order. If parents have different internal orderings (even with similar geometry), naive matching blends unrelated circles, destroying structure. Right: Bipartite matching finds the optimal geometric partners efficiently using the Hungarian algorithm (optimal assignment solver), creating clean, valid offspring.*

When we combine these components, we get a powerful parallel exploration strategy.

![Evolutionary strategies with Bipartite Matching crossover](../resources/image0122.png)

*Evolutionary strategies with Bipartite Matching crossover*

*Figure: Evolutionary strategies in action. Starting from random initializations (score 2.08), the population evolves through 20 generations using Bipartite Matching crossover and hill climbing. By generation 20, the best solution reaches 2.45—far better than hill climbing alone, but still short of the 2.635 benchmark.*

This is the core idea of evolutionary algorithms.

### MAP-Elites: Quality-Diversity Archives

Standard evolutionary algorithms track one thing: the best solution. If you have a population of 100 solutions, you keep the top 5 and discard the rest. This is of course better than hill climbing, but it is still a restricted way to explore the solution space. There is another powerful idea: what if we can not only track the best solution, but also track the best-in-class solution for different feature dimensions? For example, if you want the best packing that has equal size circles, circles with different radii, big circles in the center, etc. This would be interesting to explore, but it is not just one "best" solution.

MAP-Elites (Multidimensional Archive of Phenotypic Elites) is exactly this idea. It maintains an archive indexed by feature dimensions. Instead of asking "what's the best solution?", it asks "what's the best solution that exhibits behavior X? What's the best that exhibits behavior Y? What's the best that balances X and Y?"

Imagine a 2D grid where each cell represents a unique behavioral signature. For circle packing, MAP-Elites might track solutions by their packing density and spatial distribution pattern. Each cell holds the best solution ever found for that combination of characteristics.

This is called an illumination algorithm because it illuminates the fitness landscape—a map of solution quality—showing which regions of the behavior space are achievable and what the optimal solution is in each region. Instead of converging to one peak, you map the terrain.

![MAP-Elites archive visualization](../resources/image0123.png)

*MAP-Elites archive visualization*

*Figure: MAP-Elites archive visualization. Each cell in the grid represents a unique behavioral signature (e.g., Symmetry vs. Radius Variance). The algorithm illuminates the fitness landscape by finding the best solution for each cell.*

Why does this matter? Because it maintains diversity. A population of 100 solutions becomes a 10x10 archive of 100 *different kinds* of solutions. Some are good at high density, some at balanced distribution, some at novel packing patterns. This diversity helps escape local optima and explore unexpected solution regions. And later on—spoiler alert—this diversity will become solutions that take inspiration from optimization, computational geometry, and other fields. It gives you the best geometric solutions, best optimization solutions, and the best hybrids of both.

---

## Neuro-Symbolic Methods: Why We Need "Brains"

We've seen that symbolic methods—hill climbing, evolutionary algorithms, MAP-Elites—work beautifully. But they have a fatal flaw: **invention**.

*We* had to invent the Virtual Forces. *We* had to realize that circle packing needs a geometric crossover like Bipartite Matching. The algorithm didn't invent these concepts; it just engaged in a parameter search using the tools we built for it. And not only that, we only have limited capacity for this. We can't spend all day and night trying new intelligent ideas for circle packing—who does that anyway?

If you encounter a new problem—say, protein folding or routing high-speed trains—you have to start over. You have to be the expert who invents the domain-specific operators.

**This is the Neuro-Symbolic unlock.**

What if we could hire an AI to do the invention part? What if we could say, "Here is the problem," and the AI decides, "I should try computational geometry," or "I should implement a specific type of nonlinear optimization"?

This isn't just about filling empty spaces in a parameter grid. It's about discovering **novel approaches**—entirely new algorithms or mathematical framing that we might not have considered.

Instead of us writing the code and the AI tuning the parameters (Symbolic), we ask the AI to **write the code itself**. We use the "Brain" (LLM) to design the "Body" (Symbolic Code).

### AlphaEvolve: The Architecture

To understand how we achieve this today, we need to look at the system that pioneered it: **AlphaEvolve**.

Imagine a system where you set up a problem, then step back and watch evolution happen at scale. You provide three things: a prompt template that describes what you're trying to solve, an evaluation function that scores solutions, and an initial program to start with.

![AlphaEvolve architecture](../resources/image0124.png)

*AlphaEvolve architecture*

*Figure: AlphaEvolve's complete architecture. A scientist/engineer provides the problem setup: prompt templates, LLM selection, evaluation code, and an initial program to evolve. The distributed controller loop repeatedly samples parent programs and inspirations from the solution database, generates mutation prompts, uses LLMs to create code diffs, applies diffs to create variants, evaluates each variant, and stores results back in the solution database.*

The system enters a loop that repeats hundreds of times:

1. **Pick a parent program** from the solution database along with inspirations.
2. **Generate a mutation prompt**. The prompt sampler crafts something like: "Here's a solution scoring 2.55. Here are better solutions. Suggest improvements."
3. **Diff-Based Mutation:** The LLM doesn't rewrite the whole file. It generates a diff (a patch). This allows the agent to make surgical changes without breaking the rest of the logic.
4. **Crossover:** It doesn't just mutate one parent. It takes high-performing programs and asks the LLM to blend their logic, effectively performing semantic crossover.
5. **Execute and Store:** Apply the diff, run the evaluator, and store the result.

This is the power of AlphaEvolve: you don't program evolution—you set up the machinery and let the LLMs discover what works.

And it works incredibly well. This architecture, and related systems like **FunSearch** and **AlphaDev**, has led to breakthroughs in mathematics, computer science and real-world optimization.

### My Journey: From Hard-Coded Loops to Deep Autonomy

I wanted to replicate this. My first instinct was to build the machinery.

I used Aider, a fantastic command-line coding agent, to port the AlphaEvolve logic. I built the database, the prompt sampler, the evaluation loop. It worked. I successfully replicated AlphaEvolve and OpenEvolve project results on circle packing and even got solutions a bit faster.

But then I saw something that changed my perspective.

Researchers from Princeton first built SWE-agent, one of the first coding agents designed to solve GitHub issues. It had an elaborate Agent-Computer Interface (ACI) with custom-built tools for file editing, specialized search APIs, and git wrappers—essentially trying to hand-hold the model through a rigid developer loop.

But then they released **SWE-agent-mini**, a lightweight version that stripped everything away. Instead of a complex suite of custom tools, they gave the agent one thing: **Bash**.

**The Insight:** If the agent has a shell, it has almost everything. It can `grep` to search. It can `sed` to edit. It can run Python. If it needs a specialized tool, it can write the tool itself.

This made me pause. The framework I was building—the prompt samplers, the loop controllers—was essentially hard-coding behavior that modern LLMs might already have internalized.

We are seeing a shift towards deep agents—models that don't just follow instructions but think for extended periods. They maintain their own state, manage persistent todo lists, and autonomously replan when they hit roadblocks.

So I tried a radical experiment.

I deleted my AlphaEvolve clone. I deleted the database code. I deleted the controller loop.

I opened a terminal with **Claude Code** and gave it a single high-level directive:

> "Here is a Python evaluator script for circle packing. Your goal is to write a Python script that maximizes the score returned by this evaluator. You have full autonomy to research algorithms, test them, and iterate. I will go get coffee."

### The Deep Autonomy Result

The results were astonishing.

Without a hard-coded evolutionary loop, Claude researched existing approaches, proposed methods like SLSQP and simulated annealing, noticed where numerical optimization got stuck, wrote its own initializations, and kept iterating.

It acted as orchestrator, researcher and engineer at once.

### The Agent's Discovery: Diagonal Layering

I gave the agents full autonomy to write their own Python code, restricted only by an **immutable harness**: the evaluator.

After several generations, the agents abandoned random guessing and converged on a **Diagonal Layering Strategy**. They discovered that arranging circles in diagonal bands allowed tighter packing than grid or radial patterns, achieving a score of **2.636**.

![Code evolution result](../resources/image0125.png)

*Code evolution result: 20 generations of optimization*

*Figure: Code evolution in action. Starting from 2.613 (Gen 1), the agents iterate through 20 generations, discovering and refining the Diagonal Layering strategy to reach 2.636 (Gen 15)—slightly above the 2.635 reference benchmark we were using.*

The benchmark we were using was **2.635**, associated with AlphaEvolve/OpenEvolve-style results. Our best run under our evaluator reached **2.636**.

The numerical difference is tiny. The interesting part is not the decimal point. It is *how* we got there.

We did not hard-code diagonal layering. We gave the agents a problem, hints, tools, an evaluator, and enough freedom to research and iterate. The strategy emerged from the search.

This is the future of software development that interests me. Not merely writing code faster, but using agents to search over better ways of solving a problem.

---

## The Design Space: An Algorithmic Vortex

We've barely scratched the surface. AlphaEvolve itself uses more advanced techniques like quality-diversity archives and island models to maintain healthy evolutionary dynamics.

The design space is vast—a true algorithmic vortex. Quality-diversity archives preserve different niches. Island models keep populations partially separated so they don't all collapse onto one idea. Hyperband-like strategies can fail fast on cheap approximations before spending resources on winners. Version control can become part of the experiment machinery for larger codebases.

Each of these deserves its own treatment. The important point here is that once an agent can generate code and an evaluator can judge it, the search space expands from parameter tuning to **ways of solving the problem**.

## The Contract

Here's what we learned, distilled into principles you can use tomorrow.

**Never write solution code yourself.** You're the manager—spawn, evaluate, prune. If you write code, you limit diversity. The main agent that writes solutions tends to get stuck in its own context rut, fixing its own bugs rather than rethinking the approach. Treat code generation as a parallelizable resource.

**Keep the harness immutable.** Autonomy requires boundaries. If agents can modify the test, they'll "solve" the problem by lowering the bar—changing the box size, relaxing constraints, redefining success. The evaluator is the anchor in a system where everything else is fluid.

**Cross-pollinate success.** Random mutation is too slow for expensive LLM calls. When Agent B succeeds with diagonal layering and Agent A failed with grid packing, tell the next generation what worked. Learned traits can be inherited directly instead of rediscovered through thousands of tokens of trial and error.

**Prune ruthlessly.** Diversity is good; bad diversity is expensive. If an approach clearly isn't working, kill the lineage and free the budget for something more promising.

**Separate discovery from polish.** Once diagonal layering appeared, the problem changed. We were no longer searching for geometry; we were tuning numerical optimization around a promising geometry. Discovery and optimization are different modes.

No elaborate framework is required. Put these principles in a prompt, give the agent an evaluator, and let it work. I found Claude Code effective for this because it can use skills, sub-agents and a shell, but the product matters less than the contract.

---

## What Made This Work

The experiment worked because several unusually favorable conditions came together.

The problem was **complex but bounded**. There was plenty of room for invention, but the artifact remained small enough that an agent could build and test it repeatedly.

The harness was **immutable**. Success was externally defined and difficult to negotiate with.

Code was **cheap to evolve**. Agents could propose completely different approaches, not merely tune parameters.

The environment was **simple enough** that we did not need a large framework around the agent. Bash and an evaluator were enough.

That combination is powerful.

It is also unusually clean.

Most things people build are not like circle packing.

A demo can be technically correct and terrible. An explanation can be accurate and confusing. A design can pass every test and still make the user want to throw the laptop out of a window.

Circle packing lets the evaluator tell us exactly who won.

What happens when the evaluator doesn't know?

That's where we go next.

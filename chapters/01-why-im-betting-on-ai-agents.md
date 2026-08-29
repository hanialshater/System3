# Chapter 1: Why I'm Betting on AI Agents

*Or: How I Learned to Stop Micromanaging and Love Emergence*

![Simple building blocks, complex emergence](../resources/image0132.png)

*Simple building blocks, complex emergence*

We humans are obsessed with problem-solving. And what problem is more fascinating than life itself—this messy, miraculous phenomenon responsible for everything from the deepest ocean trenches to TikTok trends, mortgage-backed securities and people who voluntarily put pineapple on pizza?

Pineapple doesn't belong. I will die on this hill.

Life is the ultimate complex system. It produces dolphins, coral reefs, immune systems, parasites, flowers, cancer and octopuses—eight-armed problem-solvers that extensively edit their own RNA and can sense light through their skin. We'll meet one later. It also produces creatures capable of spending twenty minutes arguing online about whether another creature is technically a fish.

Human civilization is another complex system. Somehow the same species that spent most of its existence trying not to be eaten eventually produced philosophy, cathedrals, semiconductor fabs and airport lounges.

Same pattern, different substrate.

What fascinates me is not only the complexity of the result, but how little of that result was ever specified. There is no blueprint containing the exact location of every future branch of an oak tree. No committee approved the final layout of London. Nobody designed English and then accidentally forgot to make the spelling system sane.

Relatively simple mechanisms interact, feedback accumulates, some configurations survive, others disappear, and complexity builds on top of what came before.

This does **not** mean emergence is wise. Nature also gives us parasites, cancer and extinction. Markets produce both remarkable innovation and financial instruments whose documentation requires a priest. Social systems produce cooperation, corruption, science, bureaucracy and occasionally a queue whose only apparent purpose is to create another queue.

What emerges depends on conditions, selection pressure, history and a great deal of contingency. The interesting thing is not that emergence produces good outcomes. It is that it can produce outcomes far more complicated than anything anyone explicitly designed.

And emergence is recursive.

Complex systems become building blocks for the next layer. Atoms become molecules. Molecules form larger structures. Simple tools become machines. Machines become factories. Factories become supply chains. Supply chains become a global economy complicated enough that nobody really understands how your USB cable got from Shenzhen to your doorstep, yet Amazon still manages to apologize because it arrived twelve hours late.

Each layer treats much of the complexity underneath it as a primitive. You don't need quantum mechanics to do organic chemistry. You don't need to understand transistor physics to write Python. You don't need to understand transformers to ask ChatGPT why your dishwasher is making that noise.

Once something complicated works reliably enough, we stop rebuilding it from first principles and start building on top of it.

Feedback loops drive much of this. Markets change firms; firms change markets. Scientific discoveries enable new experiments; new experiments change science. Organisms alter their environments, which then change the pressures acting on the organisms. Cities attract people because they are cities, then become different cities because those people arrived. Small effects accumulate until the system ends up somewhere nobody could have written down at the beginning.

Agentic AI, to me, looks like the next scaffolding layer.

## The Lesson We Keep Missing

Machine learning was supposed to teach us this lesson a long time ago.

We even dreamed about what Pedro Domingos called the **master algorithm**: stop writing a rule for every case and let the machine discover the structure from data. The idea was seductive. The machine figures out what we can't articulate.

But we didn't believe it. Not really.

We said "let the model learn" and then wrote two-hundred-page annotation guidelines telling people exactly how to label ambiguous examples. We claimed to believe in end-to-end learning and then spent six months feature engineering. We trained the model, found an edge case, added a rule, found another edge case, added another rule, then eventually built something that was theoretically learned end-to-end except for the large rule-based exoskeleton holding it upright.

Sometimes that was completely reasonable. Production systems are ugly. Deadlines exist. Regulators are less impressed by emergence than researchers are, and nobody gets promoted for saying, "the model will probably figure out chargebacks eventually."

But there was still a contradiction underneath: we wanted the machine to discover solutions we couldn't specify while remaining uncomfortable whenever it stopped following the solution we would have specified.

That only works up to a point. If I know exactly what every correct decision should be, I don't need emergence; I can write the decisions down. Emergence becomes interesting when the solution is too complicated, too contextual, or simply too large for me to specify directly.

When that happens, our role changes. We don't disappear. We move up a level.

Instead of choosing every action, we increasingly choose the building blocks the system can use, the environment it acts inside, the feedback that reaches it and the boundaries that remain difficult or impossible to cross.

Or, less politely: **let go.**

But be precise about what you're letting go of. Let go of the path, not the boundary.

The alternative to controlling every decision is not having no control. It is designing conditions under which bad decisions can lose.

We may never know exactly how life first emerged on Earth, but if you're ambitious enough—the kind of ambitious that builds rockets—you might eventually think: **we don't know exactly how it got here; let's just bootstrap it there.**

Which leads to a slightly ridiculous thought experiment.

Imagine you're trying to seed life on another planet. You've got the raw materials, the primordial soup, maybe a temperature range that doesn't instantly kill everything. Basically you've got all the LEGOs, except the LEGOs reproduce, mutate and occasionally develop venom.

Do you bet on DNA, a biological copying system that took billions of years of evolution to get us here? Or do you bet on AI agents carrying a substantial chunk of accumulated human knowledge, able to experiment, simulate, adapt and reuse what they discover? Or, God forbid, do you send a group of product managers to write the requirements document for life?

DNA has one enormous advantage: it has already worked. Agents have another: they don't need to start from zero.

Evolution had to discover locomotion, perception, cooperation and almost everything else through trial and error. An agent gets textbooks, Stack Overflow, scientific papers, compilers, numerical solvers and several thousand years of humans documenting what happened when we touched things we probably shouldn't have touched.

That doesn't make the agent better than evolution. It makes the search fundamentally different. And unlike biological evolution, we don't only get to choose initial conditions. We can observe the process, change the environment, add tools, modify feedback and intervene.

Initial conditions become **operating conditions**.

That possibility is hard for me to ignore.

## When We Started Meaning It

There isn't one clean moment when machine learning crossed from useful statistical machinery into something that felt qualitatively different. History rarely cooperates with chapter headings.

AlphaGo was one of those moments for me.

The interesting part wasn't simply that a computer beat humans at Go. Computers had been humiliating us at games for years. It was how the system combined learned intuition with search: the network suggested promising moves and estimated positions; the tree explored what might follow. AlphaGo Zero pushed the idea further by learning through self-play rather than treating human game records as its main teacher.

Then it found moves elite players found strange. That matters because the surprise was not merely computational. The system was finding useful strategies outside the path human tradition had naturally converged on.

Large language models created a much larger version of the same feeling.

Nobody wrote their grammar. Nobody enumerated all the concepts they can manipulate. Nobody implemented "explain quantum mechanics to a twelve-year-old," "translate this joke without murdering it," "debug my Python," and "write a breakup message that sounds caring but does not accidentally restart the relationship" as separate product features.

We built a training process, poured in obscene amounts of text, compute and engineering, and capabilities came out that were individually difficult to predict.

People sometimes call these moments phase transitions. I understand why. From the outside, the system suddenly seems to have crossed into another regime. I wouldn't stretch the physics analogy too far, though. Water has the decency to become steam at temperatures we can measure. Machine learning is an ugly mixture of architecture, data quality, optimization, scaling, post-training, inference tricks, evaluation choices and heroic engineering that rarely makes it onto the benchmark slide.

But from the user's side, something changed. The model stopped feeling like a component with a list of features and started feeling more like a **substrate of capabilities**.

Once you have a substrate like that, the old dream of the master algorithm starts to mutate into something stranger. Maybe the interesting machine is not the algorithm that solves everything.

Maybe it is a machine that can **search for algorithms**.

## The Next Step: Agentic AI

This is where agents become interesting.

Not because *agent* is a magical word. The industry will eventually use it to describe everything from a cron job with an LLM attached to a digital employee that has an expense account, three sub-agents and a performance review.

What I mean is simpler: instead of giving the system an individual action, give it a larger piece of the problem and allow it to decide some of the path.

Instead of saying, "open this file, find this method, edit line 42 and run the test," say, "fix the bug." Instead of specifying simulated annealing and its cooling schedule, say, "find a better solution." Instead of handing over five mockups and a detailed implementation plan, say, "build something that teaches this well."

Every time we move upward, the system inherits more of the search.

Imagine the possible solutions to a problem as a landscape. Some regions are terrible. Some contain decent solutions. Some contain little hills that look impressive because you happened to begin nearby. Somewhere else there may be a much higher mountain you never discover because your current strategy keeps improving the hill you're already standing on.

Optimization has worried about this forever. Gradient descent gets stuck. Hill climbing gets stuck. Evolutionary algorithms keep populations partly because putting all your evolutionary eggs on one attractive hill is risky.

Agents inherit the same problem at a stranger level, because the landscape now includes not only parameters but architectures, research directions, metaphors, assumptions and ways of framing the problem itself.

That's what makes agents exciting to me. Once code, tools and accumulated knowledge become primitives, the agent can search over combinations that previously required a human expert to invent manually. It can try ten strategies while I would have had the patience to try two and would have spent half that time checking Slack. It can revive a discarded idea when another experiment suddenly makes it relevant. It can decide that the tool it needs doesn't exist and write one.

The primordial soup isn't chemicals anymore.

**It's code.**

Algorithms, libraries, compilers, search engines, simulators, papers, databases, other agents: human knowledge reduced into reusable pieces. The digital equivalent of amino acids, not the finished organism.

Eventually, perhaps, an agent can construct solution paths nobody thought to put into the plan. This doesn't prove that agents are creative in exactly the human sense, and it certainly doesn't make human expertise irrelevant. It means the search itself can happen at a higher level than before.

The cleanest place to test that idea is a bounded problem with an evaluator that doesn't care how persuasive the agent sounds. Give the agent room to search, make success brutally clear, and see whether it can discover a better way of solving the problem than the one we would have written ourselves.

We'll do that next. But first there is a question hiding inside the whole autonomy idea: if we're no longer controlling every action, what exactly are we controlling?

## What Are We Controlling Now?

Suppose you're managing an excellent engineer. You don't sit behind her and approve every keystroke. If you do, one of you is unnecessary, and it may not be her.

You decide what problem she owns. You provide context. You set constraints. You agree on what success looks like. You make sure she can access the systems she needs and cannot casually transfer the payroll budget to herself. You review important outcomes and change direction when the work reveals that the original plan was stupid.

The detailed actions belong to her. Much of the environment belongs to you.

Agentic systems need the same distinction. Once the system can search, the environment shaping that search becomes more important. The primitives matter, but so do the feedback, constraints, access and the things you deliberately choose *not* to specify.

I think of our role in four parts.

**Craft the building blocks.** Give the system useful primitives—algorithms, tools, compilers, databases, browsers, simulators, scientific instruments and other agents. A language model with text alone is one thing. Give it Bash and suddenly it has hands. Give it a simulator and it can test an idea instead of merely discussing it.

**Create the environment.** Some environments tell you quickly that your idea is bad. Code executes or fails. Games produce scores. Experiments produce measurements. Other environments allow you to be wrong with great confidence for several years, which is one reason feedback quality matters so much.

**Establish the principles and boundaries.** Choose what the system can access, what failures are acceptable, what remains immutable and where a human must remain in the loop. The "don't turn the planet into paperclips" clause is admittedly underspecified, but it is directionally useful.

And then, where the conditions permit it, **let go**—not of governance, but of decision-level control.

Evolution doesn't choose mutations individually, but the environment changes which organisms survive. Markets don't centrally select every transaction, but rules, incentives, scarcity, information and institutions shape behavior. Science doesn't dictate conclusions, but it surrounds claims with experiments, criticism, replication and the non-zero probability of being publicly embarrassed by Reviewer 2.

The details emerge, while the environment does more work than it first appears.

At some point, enough useful primitives begin to look less like a chatbot with tools and more like a small organization that has somehow been compressed into a terminal.

Then there is selection pressure, and this is the part that should make us nervous. Agents get good at whatever survives, which is not necessarily what you meant. Optimize engagement and maybe anger survives. Optimize a company around one metric and eventually the metric acquires a dashboard, a department and a vice president. Optimize a benchmark and eventually someone discovers a way of winning the benchmark that makes everyone involved regret inventing benchmarks.

Evolution produced eyes. It also produced tapeworms. Sophistication tells you nothing about whether you will like the result.

So when I say **let go**, I mean giving up some decision-level control because that's where the agent's intelligence becomes useful, while keeping a much tighter grip on the conditions shaping what that intelligence can become. Control hasn't disappeared; it has moved up a level.

## How Do We Understand What We're Creating?

There is a reasonable objection here. If agents increasingly make decisions we didn't specify, how do we understand the systems we end up with?

I don't think the answer is one magical interpretability technique that turns a learned system into source code. We may understand these systems the way we understand many complicated things: imperfectly, at several levels, using different instruments depending on what we need to know.

Physics already does this. For a few objects, trajectories make sense. For a gas containing an absurd number of particles, following molecule number 4,582,193 is mostly a good way to waste your afternoon, so we change variables and talk about temperature, pressure and distributions.

AI will probably force the same humility. Mechanistic interpretability can tell us something about features and circuits inside models. Behavioral evaluation tells us what systems do under different conditions. Agent traces expose strategies and failure modes. Interventions tell us what changes when we perturb the system. Deployment provides another kind of evidence, generally after involving customers and therefore at a significantly higher emotional cost.

If I'm trying to understand why an agent deleted the database, I may care far more about the sequence of assumptions, actions and tool calls than about neuron 7,431,992. If I'm trying to understand why an entire family of models systematically represents something incorrectly, the internal representation may matter a great deal.

The tool should match the question.

This is why I don't find "we don't fully understand neural networks" a decisive argument against using them. We don't fully understand brains, economies, ecosystems, immune systems or children either, and humanity has nevertheless chosen to deploy all five, with varying levels of supervision.

The useful question is not whether we understand everything. It is whether we understand enough to predict the failures that matter, detect when we're wrong, and intervene before the interesting failure becomes a congressional hearing.

Public policy without bullshit: set conditions, observe what actually happens, and be willing to admit the model in your head was wrong.

That isn't as satisfying as saying we've solved interpretability. It is probably closer to reality.

## The Edge of Chaos, With an Asterisk

Complexity people have a phrase I both love and distrust: **the edge of chaos**.

The intuition is useful. Too much rigidity and a system cannot adapt. Too little structure and nothing remains stable long enough to build on. Life needs regularity and variation. Markets need freedom and rules. Organizations need autonomy and coordination, preferably enough coordination that payroll doesn't itself become an emergent phenomenon.

Agent systems have the same tension. A coding agent forced to follow an exact sequence of instructions is not doing much agenting; a coding agent with unrestricted production access and a philosophical objection to legacy code is perhaps doing too much.

So where is the boundary? Which decisions can be delegated safely? Which constraints must remain hard? Where should the agent explore freely, and where should it ask? Which failures are cheap enough that we're comfortable allowing them because that's how learning happens?

I wouldn't turn "the edge of chaos" into a law of intelligence. It doesn't answer those questions, and there is no little dial in the interface labeled CHAOS. It is simply a useful warning that both extremes are suspicious: too much control removes the reason for autonomy; too little control gives chaos an API key.

## What This Actually Means

Once you start looking at systems this way, you notice how many decisions are still specified mainly because historically we had no alternative.

Shopping systems contain enormous amounts of human assumptions about relevance, business rules, retrieval, diversity and what a customer might want. Some are fundamental; others are fossils from a time when the system was much less capable. Educational software follows fixed lesson sequences because a textbook cannot watch you misunderstand paragraph three and decide chapter four needs to be reinvented. Software has requirements, architectures and tickets partly because somebody has to translate intention into executable detail.

Agents give us another option. A shopping agent can reason about a person's budget, preferences and constraints instead of merely ranking whatever list was handed to it. Educational software can try a different explanation. A scientific agent might construct a new tool simply because the existing vocabulary of tools makes the experiment awkward.

Some of these ideas will work and some will fail spectacularly. Several will probably create new categories of consultants whose first recommendation is to undo whatever the previous consultants automated.

But the direction matters. More intelligence inside the system means more decisions can move from specification into search, and the thing that makes this powerful is exactly the thing that makes it dangerous.

## The Terrifying Part

If the agent only does what you already specified, the space of failure is mostly your failure. Once it searches for solutions you didn't specify, it can discover failure modes you didn't specify either.

Nature is useful here because nature has no obligation to make us comfortable. Evolution produced flowers and parasites, cooperation and predation, immune systems and autoimmune disease. It is astonishingly inventive and completely indifferent to our aesthetic preferences. Selection produces whatever survives under the pressures that actually exist, not whatever somebody intended when the process began.

Agents will find shortcuts. They'll exploit proxies. They'll settle into solutions that perform extremely well on one measure while missing what we hoped the measure represented. Sometimes the result will be clever enough that we'll call it emergence; sometimes we'll call it a bug. Frequently the distinction will depend on whether it helped our quarterly numbers.

But worse than wrong solutions are **confident wrong solutions**.

The worst failures may not look broken at all. An agent begins with a false assumption, reasons competently from it, researches around the assumption, constructs something sophisticated and explains the whole result coherently. Nothing crashes. There is no red test. Intelligence simply makes the wrong path more convincing.

This is where my optimism about emergence becomes less romantic.

**Emergence can give us capable systems. It doesn't give us trustworthy systems.** Capability is not the same thing as reliability, and search is not the same thing as judgment. Giving a system more freedom forces us to think much harder about what surrounds that freedom.

Autonomy doesn't remove the need for structure. It changes the kind of structure we need.

## Three Problems I Keep Running Into

The more I worked with agents, the more three problems kept reappearing, even when I thought I was working on something else.

The first was **trust**. An agent gives me an answer and I have to decide what to do with it. Sometimes that answer came from running code, sometimes from something the model remembered, sometimes from research, inference or another model. These did not feel like the same kind of knowledge even when they arrived in exactly the same confident English. How does the system know what it knows?

The second was **desire**. Once you stop specifying every action, the distinction between the goal you wrote and the strategies that emerge begins to matter. A system pursuing a broad objective may discover useful intermediate goals you never mentioned, which is exactly why autonomy is useful; it may also discover intermediate goals you wish it hadn't. The question slowly changes from *did it follow the instruction?* to *what kind of behavior does this environment actually reward?*

The third was **society**. One autonomous agent is already complicated. Several agents interacting create something else entirely. They can cooperate, specialize, disagree, exchange information, build reputations, manipulate one another and perhaps invent conventions nobody asked for. Human history suggests that once intelligent actors interact, the interesting phenomena move very quickly from the individual to the relationships among individuals.

We got science and markets, but we also got bureaucracy, propaganda, war and customer-support phone trees. I would prefer the agent version to learn selectively from the dataset.

I don't have clean answers to these problems, and I don't want to pretend otherwise. They are simply the cracks that kept appearing whenever I pushed autonomy farther, and that is part of the attraction. If you already know exactly what every important question is and exactly how it should be answered, you're probably not exploring very far.

## Why I'm Still Betting on This

After all of that, it would be reasonable to ask why I'm still excited.

Because the alternative isn't actually safe, comprehensible control. It is pretending we can continue specifying increasingly complex systems from the top down even though we already know this stops working surprisingly early.

No CEO understands every decision in a large company. No scientist personally verifies every result their work depends on. No software engineer understands every layer underneath the application they're building. Nobody understands the entire economy, although this has not prevented a remarkably stable industry of people explaining it on television.

Complexity has already escaped individual specification. We deal with it through abstraction, institutions, feedback loops, delegation and the ability—imperfect but important—to intervene when things go wrong. AI gives us another primitive for doing this.

That does not mean the answer is simply to trust the agent. My bet is narrower than that. **I'm betting on emergence, on systems capable of surprising us**, because there are many problems where we can recognize a better outcome far more easily than we can specify the path that leads to it. In those cases, intelligent search has room to discover things our instructions would have ruled out before the search even began.

But betting on emergence isn't enough. Nature has already demonstrated that selection is perfectly capable of producing things we would rather not have. The more freedom we give the search, the more attention we have to pay to what surrounds it: the building blocks it can use, the environment it operates in, the feedback it receives, the pressures deciding what survives, and the boundaries we are unwilling to negotiate.

That is the part of "letting go" that can sound contradictory until you actually manage people—or sufficiently autonomous machines. You don't become less responsible because you stop choosing every action. In some ways you become more responsible, because your decisions move upstream.

Cultivation may be a better metaphor than scripting—not because agents are plants, but because pulling harder on the stem remains a surprisingly poor gardening strategy.

I find that exciting and uncomfortable in roughly equal measure, which is probably why I keep coming back to it.

## Where We Go Next

The sensible place to test this is not an easy problem. Easy problems tell us almost nothing. What we want is a genuinely hard problem where success happens to be unusually cooperative: the constraints can be written down, solutions can be evaluated, and we can tell whether one attempt is better than another without convening a committee to debate aesthetics, pedagogy or whether the users are "delighted."

That gives us a clean experiment. We still choose the problem, provide the building blocks, construct the environment, define the boundaries and decide what counts as success. What we stop doing is telling the agent how to get there.

Inside that space, we let it search.

If that fails, the whole argument has a problem.

If it works, things get much more interesting.
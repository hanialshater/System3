# Chapter 1: Why I'm Betting on AI Agents

*Or: How I Learned to Stop Micromanaging and Love Emergence*

![Simple building blocks, complex emergence](../resources/image0132.png)

*Simple building blocks, complex emergence*

We humans are obsessed with problem-solving. And what problem is more fascinating than life itself—this messy, miraculous phenomenon responsible for everything from the deepest ocean trenches to TikTok trends, mortgage-backed securities and people who voluntarily put pineapple on pizza?

Pineapple doesn't belong. I will die on this hill.

Life is the ultimate complex system. It produces dolphins, coral reefs, immune systems, parasites, flowers, cancer and creatures capable of spending twenty minutes arguing online about whether another creature is technically a fish.

Human civilization is another one. Somehow the same species that spent most of its existence trying not to be eaten eventually produced philosophy, cathedrals, semiconductor fabs and airport lounges.

What fascinates me is not only the complexity of the result. It is how little of that result was ever specified.

There is no blueprint containing the exact location of every future branch of an oak tree. No committee approved the final layout of London. Nobody designed English and then accidentally forgot to make the spelling system sane. Relatively simple mechanisms interact, feedback accumulates, some configurations survive, others disappear, and complexity builds on top of what came before.

This does **not** mean emergence is wise. Nature also gives us parasites, cancer and extinction. Markets produce remarkable innovation and financial instruments whose documentation requires a priest. Social systems produce cooperation, corruption, science, bureaucracy and occasionally a queue whose only apparent purpose is to create another queue.

The interesting thing is not that emergence produces good outcomes. It is that it can produce outcomes far more complicated than anything anyone could have specified in advance.

And then the trick repeats.

Atoms become molecules. Molecules become materials. Tools become machines. Machines become factories. Factories become supply chains. Supply chains become a global economy complicated enough that nobody really understands how your USB cable got from Shenzhen to your doorstep, yet Amazon still manages to apologize because it arrived twelve hours late.

Each successful layer turns some of the complexity underneath it into a primitive.

You don't need quantum mechanics to do organic chemistry. You don't need to understand transistor physics to write Python. You don't need to understand transformers to ask ChatGPT why your dishwasher is making that noise.

This may be civilization's most useful scaling trick: once something complicated works reliably enough, we stop rebuilding it from first principles and start building on top of it.

Agentic AI, to me, looks like the next version of that trick.

Not because agents remove the complexity. They move some of it underneath the level at which we have to operate. Instead of specifying every useful action ourselves, we can increasingly build the conditions, tools and feedback through which useful actions are found.

Which sounds suspiciously like something machine learning was supposed to teach us a long time ago.

## The Lesson We Keep Missing

Machine learning began with a strange promise: stop writing a rule for every case and let the machine discover useful structure from data.

Instead of telling a program exactly how to recognize a face, translate a sentence or rank a document, give it examples, an objective, enough compute and permission to be wrong several million times before lunch.

Then, because we are human, we spent years saying “let the model learn” while carefully micromanaging almost everything around it.

We wrote two-hundred-page annotation guidelines telling people exactly how to label ambiguous examples. We claimed to believe in end-to-end learning and then spent six months feature engineering. We trained the model, found an edge case, added a rule, found another edge case, added another rule, and eventually built something that was theoretically learned end to end except for the large rule-based exoskeleton holding it upright.

Sometimes that was completely reasonable. Production systems are ugly. Deadlines exist. Regulators are less impressed by emergence than researchers are, and nobody gets promoted for saying, “the model will probably figure out chargebacks eventually.”

But there was still a contradiction underneath.

We wanted the machine to discover solutions we could not specify while remaining uncomfortable whenever it stopped following the solution we would have specified.

That only works up to a point.

If I know exactly what every correct decision should be, I do not need emergence. I can write the decisions down. Emergence becomes interesting when the solution is too complicated, too contextual, or simply too large for me to specify directly.

When that happens, our role changes. We do not disappear; we move up a level.

Instead of choosing every action, we choose more of the environment around the actions: what the system can act with, what feedback reaches it, what counts as success, what it can observe, and which boundaries should remain difficult or impossible to cross.

This is not giving up control. **Control moves upward.**

We may never know exactly how life first emerged on Earth, but if you are ambitious—like a certain space-obsessed billionaire—you might eventually think: perhaps we do not need to design life cell by cell; perhaps we need to create conditions under which something can bootstrap itself.

Which leads to a slightly ridiculous thought experiment.

Imagine you are trying to seed life on another planet. You have the raw materials, the primordial soup, maybe a temperature range that does not instantly kill everything. Basically you have all the LEGOs, except the LEGOs reproduce, mutate and occasionally develop venom.

Do you bet on DNA, a biological copying system that took billions of years of evolution to get us here? Or do you bet on AI agents carrying a substantial chunk of accumulated human knowledge, able to experiment, simulate, adapt and reuse what they discover?

Or, God forbid, do you send a group of product managers to write the requirements document for life?

DNA has one enormous advantage: it has already worked.

Agents have another: they do not need to start from zero. Evolution had to discover locomotion, perception, cooperation and almost everything else through trial and error. An agent gets textbooks, Stack Overflow, scientific papers and several thousand years of humans documenting what happened when we touched things we probably should not have touched.

That does not make the agent better than evolution. It makes the search fundamentally different.

And that possibility is hard for me to ignore.

## When We Started Meaning It

There is no clean moment when machine learning crossed from useful statistical machinery into something that felt qualitatively different. History rarely cooperates with chapter headings.

AlphaGo was one of those moments for me.

The interesting part was not simply that a computer beat humans at Go. Computers had been humiliating us at games for years. It was how the system combined learned intuition with search. The network suggested promising moves and estimated positions; the tree explored what might follow. AlphaGo Zero pushed the idea further by learning through self-play rather than treating human game records as its main teacher.

Then it found moves elite players found strange.

That matters because the surprise was not merely computational. The system was finding useful strategies outside the path human tradition had naturally converged on.

Large language models created a much larger version of the same feeling.

Nobody wrote their grammar. Nobody enumerated all the concepts they can manipulate. Nobody implemented “explain quantum mechanics to a twelve-year-old,” “translate this joke without murdering it,” “debug my Python,” and “write a breakup message that sounds caring but does not accidentally restart the relationship” as separate product features.

We built a training process, poured in obscene amounts of text, compute and engineering, and capabilities came out that were individually difficult to predict.

People sometimes call these moments phase transitions. I understand why. From the outside, the system suddenly seems to have crossed into another regime. I would not stretch the physics analogy too far; water has the decency to become steam at temperatures we can measure. Machine learning is an ugly mixture of architecture, data quality, optimization, scaling, post-training, inference tricks, evaluation choices and heroic engineering that rarely makes it onto the benchmark slide.

But from the user's side, something did change.

The model stopped feeling like a component with a list of features and started feeling more like a **substrate of capabilities**.

Once you have a substrate like that, a question appears almost automatically:

Why are we still telling it every step?

## The Next Step: Agentic AI

This is where agents become interesting.

Not because *agent* is a magical word. The industry will eventually use it to describe everything from a cron job with an LLM attached to a digital employee that has an expense account, three sub-agents and a performance review.

What I mean is simpler: instead of giving the system an individual action, give it a larger piece of the problem and allow it to decide some of the path.

Instead of saying, “open this file, find this method, edit line 42 and run the test,” say, “fix the bug.”

Instead of specifying simulated annealing and its cooling schedule, say, “find a better solution.”

Instead of handing over five mockups and a detailed implementation plan, say, “build something that teaches this well.”

Every time we move upward, the system inherits more of the search.

That search can happen at levels that used to belong almost entirely to humans: not only parameters and candidate solutions, but architectures, research directions, tools, metaphors, assumptions and ways of framing the problem itself.

That is what makes agents exciting to me. Once code, tools and accumulated knowledge become primitives, an agent can try combinations that previously required a human expert to invent manually. It can try ten strategies while I would have had the patience to try two and would have spent half that time checking Slack. It can revive a discarded idea when another experiment suddenly makes it relevant. It can decide that the tool it needs does not exist and write one.

Eventually, perhaps, it can construct solution paths nobody thought to put into the plan.

This does not prove that agents are creative in exactly the human sense, and it certainly does not make human expertise irrelevant. It means the **search itself** can happen at a higher level than before.

The cleanest place to test that idea is a bounded problem with an evaluator that does not care how persuasive the agent sounds. Give the agent room to search, make success brutally clear, and see whether it can discover a better way of solving the problem than the one we would have written ourselves.

We will do that next.

But before we do, the whole autonomy idea leaves one question hanging:

If we are no longer controlling every action, what exactly are we controlling?

## What Are We Controlling Now?

Suppose you are managing an excellent engineer. You do not sit behind her and approve every keystroke. If you do, one of you is unnecessary, and it may not be her.

You decide what problem she owns. You provide context. You set constraints. You agree on what success looks like. You make sure she can access the systems she needs and cannot casually transfer the payroll budget to herself. You review important outcomes and change direction when the work reveals that the original plan was stupid.

The detailed actions belong to her. Much of the environment belongs to you.

Agentic systems need the same distinction.

Once the system can search, the environment shaping that search matters more. The primitives matter. Feedback matters. Constraints matter. Access matters. The things you decide **not** to specify matter.

Evolution does not choose mutations individually, but the environment changes which organisms survive. Markets do not centrally select every transaction, but rules, incentives, scarcity, information and institutions shape behavior. Science does not dictate conclusions, but it surrounds claims with experiments, criticism, replication and the non-zero probability of being publicly embarrassed by Reviewer 2.

The details emerge. The environment is doing more work than it first appears.

If you want complex solutions, the building blocks matter. Give an agent algorithms, compilers, databases, search engines, simulators, browsers, scientific tools and other agents, and you have changed the space of solutions it can construct. A language model with text alone is one thing. Give it Bash and suddenly it has hands. Give it a browser and it can interact with applications. Give it a simulator and it can test an idea rather than merely discuss it.

At some point, enough useful primitives begin to look less like a chatbot with tools and more like a small organization that has somehow been compressed into a terminal.

The feedback matters just as much. For an algorithm, feedback may be a numerical evaluator. For code, tests and execution. For science, experiments. For a recommender, user behavior. For a marketplace, prices and demand. Some environments are generous enough to tell you quickly that your idea is bad. Others allow you to be wrong with great confidence for several years.

Then there is selection pressure, and this is the part that should make us nervous. Agents get good at whatever survives, which is not necessarily what you meant. Optimize engagement and maybe anger survives. Optimize a company around one metric and eventually the metric acquires a dashboard, a department and a vice president. Optimize a benchmark and eventually someone discovers a way of winning the benchmark that makes everyone involved regret inventing benchmarks.

Evolution produced eyes. It also produced tapeworms. Sophistication tells you nothing about whether you will like the result.

So when I talk about letting go, I do not mean abandoning governance. I mean giving up some decision-level control because that is where the agent's intelligence becomes useful, while keeping a tighter grip on the environment, constraints, access and feedback shaping what the agent learns to do.

There is a useful intuition from complex systems about interesting behavior appearing somewhere between rigid order and complete randomness, usually sold under the wonderfully marketable phrase *the edge of chaos*. I like the intuition more than I trust the slogan. A coding agent forced to follow an exact sequence is not doing much agenting. A coding agent with unrestricted production access and a philosophical objection to legacy code is perhaps doing too much.

Too much control removes the reason for autonomy; too little control gives chaos an API key.

The interesting question is the boundary.

## How Do We Understand What We're Creating?

There is a reasonable objection here. If agents increasingly make decisions we did not specify, how do we understand the systems we end up with?

I do not think the answer is one magical interpretability technique that turns a learned system into source code. We understand many complicated things imperfectly and at several levels, using different instruments depending on what we need to know.

Physics changes variables when following every particle becomes useless. Biology shifts among molecules, cells, organs, organisms and ecosystems. Brains get studied through neurons, circuits, behavior and cognition because no single level answers every useful question.

AI will probably force the same humility. Mechanistic interpretability can tell us something about internal features and circuits. Behavioral evaluation tells us what systems do under different conditions. Agent traces expose strategies and failure modes. Interventions tell us what changes when we perturb the system. Deployment supplies another kind of evidence, generally after involving customers and therefore at a significantly higher emotional cost.

If I am trying to understand why an agent deleted the database, I may care far more about the sequence of assumptions, actions and tool calls than about neuron 7,431,992. If I am trying to understand why a family of models systematically represents something incorrectly, the internal representation may matter a great deal. The tool should match the question.

This is why I do not find “we do not fully understand neural networks” a decisive argument against using them. We do not fully understand brains, economies, ecosystems, immune systems or children either, and humanity has nevertheless chosen to deploy all five, with varying levels of supervision.

The useful question is not whether we understand everything. It is whether we understand enough to predict the failures that matter, detect when we are wrong, and intervene before the interesting failure becomes a congressional hearing.

That is less satisfying than saying we solved interpretability. It is probably closer to reality.

## The Terrifying Part

If an agent only does what you already specified, the space of failure is mostly your failure. Once it searches for solutions you did not specify, it can discover failure modes you did not specify either.

Nature is useful here because nature has no obligation to make us comfortable. Evolution produced flowers and parasites, cooperation and predation, immune systems and autoimmune disease. It is astonishingly inventive and completely indifferent to our aesthetic preferences.

Selection produces whatever survives under the pressures that actually exist, not whatever somebody intended when the process began.

Agents will find shortcuts. They will exploit proxies. They will settle into solutions that perform extremely well on one measure while missing what we hoped the measure represented. Sometimes the result will be clever enough that we call it emergence. Sometimes we call it a bug. Frequently the distinction will depend on whether it helped our quarterly numbers.

This is the part of autonomy I think we underestimate when we talk about agents mostly as productivity tools. The benefit is not merely that the machine can execute more steps before asking permission. The benefit is that it can find paths we did not imagine, and a system capable of surprising us with good solutions is also capable of surprising us with terrible ones.

The worst failures may not look broken at all. An agent begins with a false assumption, reasons competently from it, researches around the assumption, constructs something sophisticated and explains the whole result coherently. Nothing crashes. There is no red test. Intelligence simply makes the wrong path more convincing.

This is where my optimism about emergence becomes less romantic. Capability is not reliability. Search is not judgment. Giving a system more freedom forces us to think much harder about what surrounds that freedom.

Three cracks kept appearing as I pushed autonomy farther.

The first was **trust**: an answer from running code, an answer recalled from training, an inference from a paper and a judgment from another model can arrive in exactly the same confident English even though they do not deserve the same kind of confidence.

The second was **desire**: once I stop specifying every action, the question changes from “did it follow my instruction?” to “what behavior does this environment actually reward, and is that what I meant?”

The third was **society**: one autonomous agent is complicated; several interacting agents can specialize, disagree, build reputations, inherit one another's errors and create conventions nobody asked for.

I do not want to solve any of those here. For now they are only warning lights on the dashboard.

## Why I'm Still Betting on This

After all of that, it would be reasonable to ask why I am still excited.

Because the alternative is not actually safe, comprehensible control. The alternative is pretending we can continue specifying increasingly complex systems from the top down even though we already know this stops working surprisingly early.

No CEO understands every decision in a large company. No scientist personally verifies every result their work depends on. No software engineer understands every layer underneath the application they are building. Nobody understands the entire economy, although this has not prevented a remarkably stable industry of people explaining it on television.

Complexity has already escaped individual specification. We deal with it through abstraction, institutions, feedback loops and delegation while keeping some ability to intervene when things go wrong.

AI gives us another primitive for doing this.

That does not mean “trust the agent.” I do not. The bet is narrower: there are many problems where we can recognize a better outcome more easily than we can specify the path to it. In those problems, intelligent search has room to discover things our instructions would have excluded.

So start with the easy version of autonomy.

Not an easy problem. Those are boring.

A hard problem where success itself is unusually cooperative. We can write the constraints down. We can evaluate a solution. We can tell whether one attempt is better than another without convening a committee to debate aesthetics, pedagogy or whether the users are “delighted.”

We still choose the problem, provide the environment, define the boundaries and decide what counts as success. Inside those boundaries, though, we stop telling the agent how to solve it.

If the idea fails there, we can go home early.

If it works, the next problem is obvious.

What happens when the number disappears?

# Chapter 3: Deep Mode

*Beyond Algorithms: Agent Autonomy for Creative Problems*

In the previous chapter, we gave agents a difficult algorithmic problem and a lot of autonomy. The result was surprisingly good. The agent researched strategies, tried several approaches, got stuck, changed direction, and eventually discovered diagonal layering.

But circle packing had one enormous advantage that I didn't appreciate enough at the beginning: **we knew exactly what good meant**.

There was an immutable evaluator. You ran a solution and got a number. Circles overlapped or they didn't. The score improved or it didn't. The agent could spend an hour pursuing some bizarre geometric idea and I didn't have to sit beside it wondering whether version 17 had more *soul*. We just ran the evaluator.

Most of the things I actually want AI to help me with aren't like that.

"Is this explanation pedagogically effective?" doesn't have a unit test. "Would a confused student understand this visualization?" can't be settled with an `assert`. Two competent people can look at the same design, disagree completely, then switch sides five minutes later after actually using it. The feedback is subjective, noisy, sometimes contradictory, and often becomes clearer only after you have built the thing you were supposedly trying to specify beforehand.

This seemed like a good place to test autonomy next.

I picked educational demos for Merge Sort and Count-Min Sketch. They are still bounded problems—you can actually finish one before civilization collapses—but they contain much more of the messiness of real creative work. You have to make decisions about explanation, interaction, visual structure, cognitive load, and what another person is likely to understand.

The ambition was intentionally high. I wanted something closer to the best Distill articles or Jay Alammar's visual explanations than to the usual "here are some bars moving around; congratulations, you have learned sorting." Those demos take a surprising amount of thought. The algorithm itself is usually the easy part. The difficult part is deciding what to show, what not to show, when to explain something, and what representation might make an idea suddenly click.

And almost immediately, the nice clean setup from Chapter 2 disappeared.

There was no obvious evaluator.

That turns out to change nearly everything.

## How We Got Here

It's 2023. GPT-4 has just come out, and you decide to use it on a real codebase. Not a toy project. Say a 150,000-line CRM system that has accumulated all the normal fossils of mature software: old APIs nobody wants to touch, three ways of doing authentication, and at least one comment saying `TEMP FIX` written by someone who left the company four years ago.

The workflow is ridiculous.

You find the file you think contains the bug, copy it into ChatGPT, explain what you want, copy the answer back into your editor, run the code, discover what broke, then return to ChatGPT carrying the error message like a pigeon with a very technical note tied to its leg.

For a small function, this already feels magical. You ask for something that would have taken twenty minutes and get a plausible answer in twenty seconds.

Then the bug crosses three files.

Now you have another job: deciding what the model needs to know. You paste one class but forget the interface it implements. The model confidently invents a method that doesn't exist. So you paste more code. Then more. Soon you have filled the context window with half the repository and somehow made the model understand less.

This was an early lesson that took us embarrassingly long to learn: **more context and better context are not the same thing**.

A lot of early LLM programming felt like preparing a tiny artificial universe around the model. Here is the relevant class. Here is the database schema. Please ignore these twelve methods. This function looks important but isn't. That one looks irrelevant but controls payments, so please don't touch it unless you enjoy incident calls.

The model wasn't the only thing doing work. **You were preparing its world for it.**

We gradually got better at this. Instead of dumping entire files into the prompt, we gave models structural summaries, relevant methods, dependency information, and pointers to where things lived. What later became fashionable to call *context engineering* began as a fairly mundane realization: if you put the entire kitchen in front of someone because they asked for a spoon, eventually they stop seeing the spoon.

But even after we became good at preparing context, we were still doing all the work around the model. We searched the repository, edited the files, ran the tests, and copied the errors back.

So the next move was obvious: give the model a computer.

Now it could open files itself, search with `grep`, edit code, run tests, inspect the resulting error, and try again. This is the transition from a language model that knows about programming to a coding agent that can actually participate in programming.

It solved a huge problem and immediately exposed several new ones.

The model could act, but sometimes it acted like an intern who had been given root access and too much coffee. Ask it to change one line and it might rewrite half the file. Ask it to fix a button and twenty minutes later it has developed strong opinions about your database architecture. It finds one plausible theory, follows it for too long, and keeps polishing the theory after a human would already have said, "No, this clearly isn't it."

So we added better editing tools. Smaller patches. Planning. Checkpoints. Rollbacks. Ways to make the agent stop and reconsider rather than enthusiastically tunneling toward Australia.

Then another problem became obvious: the agent kept forgetting things we had already taught it.

Your authentication system works in a particular way. Your team has conventions. There is one ancient API that looks wrong but absolutely must not be "fixed" because six other systems depend on its wrongness. You explain this Monday, then again Tuesday, then again Wednesday, and at some point you begin to suspect that **you are the memory module**.

So we externalized the knowledge.

`CLAUDE.md`. Rules files. Skills. Repository instructions. Different products gave them different names, but the idea was the same: if humans have already learned something expensive about this environment, stop forcing the model to rediscover it every session.

Now the agent could act and inherit local knowledge. Then the sessions got longer.

Long sessions create their own pathology. The context slowly fills with abandoned experiments, obsolete assumptions, command output from forty minutes ago, and debugging paths that stopped mattering three hypotheses back. Technically, the model knows more. Practically, it starts behaving as if someone emptied a filing cabinet onto its desk and told it that every sheet of paper might contain the launch codes.

So we learned to manage memory too: summarize, prune, retain what matters, throw away the debris.

Then we hit another limitation. One agent tends to explore one path at a time.

Suppose you're not sure whether the demo should use React, SVG directly, Canvas, or something stranger. A long-running agent usually commits early and then spends much of its intelligence making that decision look increasingly reasonable. Every new instruction arrives inside a context that already assumes the previous architecture.

Humans have a name for this when we do it: sunk cost.

Agents have a more respectable excuse. Their entire context window is literally full of evidence that this is what the project is.

So we started spawning alternatives. Let one agent try the tree. Another tries bars. Another does something deliberately different. If one direction is clearly better, we keep it. If two have useful pieces, perhaps we combine them.

Something important had happened by then. We started with a model that could answer questions about code. Then we gave it context, hands, memory, planning, and parallelism. Step by step, we took things the human had been doing around the model and moved them into the system.

But there was still an awkward gap between an agent that could work on software and an agent that could simply build what I wanted.

## From the Repository to the App

Once coding agents became comfortable operating inside repositories, another inefficiency became obvious.

Say I want to build a small booking application. Nothing exotic: a few pages, authentication, a database, perhaps payments, and somewhere to deploy it.

A coding agent can absolutely build all of this. But watch what it spends its time doing. First it creates the project. Then it chooses a framework, installs packages, sets up the database, wires authentication, manages environment variables, configures deployment, and eventually discovers that one library conflicts with another for reasons that will be discussed passionately on GitHub and nowhere else.

The application works locally. Production, offended by your optimism, disagrees.

Most of this work isn't unique to the booking application. The next application needs roughly the same plumbing. So does the one after that.

At some point it becomes strange to take a very capable agent, give it an empty terminal, and ask it to reconstruct standard web development from first principles every time somebody wants a reservation form.

This is why systems like Replit and Lovable are interesting to me. The important move isn't simply that they give the coding model nicer tools. They give it a more prepared world.

Replit pulls the editor, runtime, packages, server and deployment much closer together. Lovable pushes further toward the application abstraction itself. You can begin with something like:

> "Build a booking system for a football academy. Parents should see available sessions and book one."

The conversation then stays much closer to the application. Put the schedule on the home page. Don't require login until someone actually books. The mobile version is too crowded. Maybe remove the photo of the suspiciously muscular child kicking a football.

Somewhere underneath all of this there is still React. There is still a database, API calls, configuration, hosting and the usual small army of things waiting for an opportunity to break.

You increasingly don't have to care.

I think of these systems as **smart templates**, although the word *template* makes them sound more rigid than I mean. The old template gave you a finished restaurant website and asked you to replace the logo. A smart template gives the agent an environment where common decisions already have sensible defaults, while leaving enough freedom to change them when the problem actually requires it.

You lose something by doing this. Give an agent Bash and an empty computer and it can attempt almost anything. Put it inside a structured application environment and you have constrained the space.

But freedom has a cost.

If there are fifty reasonable ways to implement authentication, twenty ways to organize the frontend, ten possible databases, and a small religious war around deployment, reconsidering the entire universe every time you build a small application isn't necessarily intelligence. Sometimes it's just a very expensive way to avoid having defaults.

A good abstraction removes decisions you no longer want to make.

Looking backward, this was the pattern. At first the model generated pieces of **code**. Coding agents let us operate at the level of the **codebase**. Application platforms increasingly let us operate at the level of the **app**.

The lower level never disappears. It becomes something the layer above can treat as a primitive.

This is the same recursive pattern from Chapter 1. Atoms become molecules. Components become machines. Machines become factories. Once a complicated thing becomes reliable enough, the next layer stops caring how it works internally and starts building with it.

Which leaves an uncomfortable question.

After all these abstraction jumps, **what are we still doing?**

## The Problem-Solving Layer

Go back to the Merge Sort demo.

Suppose the application platform gives me something perfectly functional. There is an array, an animation, a next button, a reset button, some color, and Merge Sort does indeed sort the array. Nobody has accidentally built Bubble Sort and hoped I wouldn't notice.

I open it and think: *This isn't very good.*

Not broken. Bad.

Maybe the student can see what the algorithm is doing but not why any of it helps. Perhaps bars are the wrong representation. A recursion tree would expose the structure much better, although it might also make a fairly simple idea look like the organizational chart of a German corporation. Maybe we need both. Maybe the real problem isn't visual at all; perhaps the explanation should begin from the merge operation and work backward.

This is what I increasingly find myself doing while vibe coding.

I'm not programming. I'm deciding what to try, looking at what came back, developing a theory about why it failed, preserving something useful, rejecting something else, and occasionally deciding that the entire direction was wrong.

The implementation problem has become smaller, revealing a **problem-solving problem** underneath it.

And AI is already beginning to spread into this territory too.

Design is becoming a specialist capability. Tools like Claude Design are aimed at exploring interfaces and visual ideas rather than treating design as a decorative step after coding. Research agents can conduct a multi-step investigation instead of answering from whatever happens to be in the model's memory. Image models can sketch a visual idea before anybody writes the application. Browser agents can interact with the artifact instead of merely inspecting its source. Around them, specialized systems are appearing for analysis, simulation, scientific discovery, formal reasoning, video, and increasingly narrow professional domains.

I don't think the names of today's products are the important part. Half of them will merge, rename themselves, or be absorbed into something larger before anybody finishes reading this book.

The direction is more interesting.

The first generation of AI tools tried to make a general model useful for everything. Now that general models are capable enough, we increasingly put them inside specialized environments. A coding agent gets a repository and Bash. A research agent gets search and sources. A scientific system might get notebooks, datasets and simulators. A design system gets visual context and tools appropriate for design.

This starts to look less like one gigantic intelligence gradually eating the world and more like a new ecology of cognitive tools.

But notice something: this isn't quite the same abstraction ladder we just climbed.

Claude Design isn't simply one level above Claude Code. Research is not the thing after Lovable. They are different specializations around the problem.

At this level, capability starts spreading **sideways** as well as upward.

Which produces a slightly comic situation: suddenly I have more experts available than ever, but somebody still has to run the meeting.

Should we research existing Merge Sort explanations first, or will that anchor every builder on the same conventional ideas? Should we generate five visual concepts before coding anything, or build something cheap and react to it? If the image model proposes something interesting, do we implement the picture literally or steal only the structural idea? If two evaluators disagree, is that noise, or have they exposed a real trade-off?

This is not really a software question anymore.

It is a question about how to solve the problem.

That was the point where the whole evolution of vibe coding started looking to me like a stack of abstraction layers.

## The Five Layers of Vibe Coding

**Layer 0 is the model.** This is the raw capability: language, reasoning, code generation, vision. Frontier labs build most of this layer. The rest of us rent it, complain about the price, and immediately ask for a larger context window.

**Layer 1 is the agent.** Give the model files, Bash, tools, execution, planning, context management and some ability to persist what matters. Now it doesn't merely tell you how to modify software; it can operate on software.

**Layer 2 is the application layer.** This is the machinery that turns code into something people can actually use: components, databases, authentication, environments, hosting, deployment and all the conventions around them. Smart application platforms increasingly package this layer so we can talk about the application rather than every piece of plumbing beneath it.

Then we reach **Layer 3: problem-solving**.

This is where the shape becomes much less uniform. We are deciding what to try, what to research, what evidence matters, which direction deserves another iteration, whether two approaches should be combined, or whether the correct action is to throw away yesterday's clever idea before it consumes another afternoon.

For the Merge Sort demo, Layer 3 might involve researching how people teach recursion, generating visual approaches, building several cheap prototypes, asking simulated learners to use them, comparing the results and deciding where to invest next.

For a mathematical problem, the process may involve conjectures, counterexamples, computational experiments, proof attempts and formal verification. A product problem could involve customer evidence, competing hypotheses, prototypes and simulations. Writing an article might involve research, argument construction, criticism, restructuring and revision.

There is no standard Layer 3 workflow because **figuring out the workflow is itself part of the problem**.

That point matters. If there were one universal workflow for Layer 3, we would have already compressed problem-solving into an algorithm and gone home early.

Design models, research agents, image generation, simulations and evaluators are not the layer. They are things the layer may recruit.

And then there is **Layer 4: intention and goals**.

This one is easy to ignore because software culture likes goals to arrive fully formed, preferably in Jira, where they can remain wrong in a structured and searchable format.

Real goals aren't always like that.

I might start with:

> "Build an interactive Merge Sort demo."

Then I see three versions and realize that interactivity wasn't actually the thing I cared about. What I wanted was for somebody encountering divide-and-conquer for the first time to *feel why breaking a problem apart makes it easier*.

That is a different objective, and it produces a different application.

The solution changed my understanding of the goal. The new goal changes the next solution.

I am going to leave Layer 4 mostly alone for now. There is enough trouble one level below it.

![The 5 layers of vibe coding abstraction](../resources/image0126.png)

*The five layers of vibe coding abstraction.*

The exact borders between these layers don't matter very much. Real systems will blur them, and today's product boundaries are unlikely to survive long enough to become philosophy.

What mattered to me was where the human work had gone.

We started close to Layer 0, moving outputs between the model and the code ourselves. Coding agents pushed us upward. Application platforms pushed us upward again. Now specialist systems are beginning to eat pieces of Layer 3.

Yet whenever I built something non-trivial, I was still sitting there deciding how all these pieces should work together.

That was where the interesting work remained.

## In the Vibe Coder's Seat

The layered picture told me where the work had moved. It did not tell me what I was actually doing there.

There is no universal algorithm hiding inside "problem-solving." A mathematician, a designer and a product manager can all spend a day solving hard problems while performing almost none of the same visible actions.

So instead of trying to derive a general theory, I watched myself work.

With the Merge Sort demo, implementation was increasingly cheap. I could ask an agent to build a version, change it, run it, or start another one. I could ask an image model for a visual direction. I could research existing explanations. I could spawn several alternatives.

Yet most of the consequential decisions were still mine.

One version made recursion invisible. Another made recursion perfectly clear but intimidating. A third looked beautiful and taught almost nothing. I would decide that we needed a completely different representation, see it, then change my mind. Sometimes I wanted to improve a direction. Other times the right decision was to stop polishing it and kill it.

None of this followed a fixed procedure.

The educational demos were useful precisely because they were small enough that I could observe these decisions while making them. I started asking what, exactly, kept pulling me back into the loop. Why did I ask for three alternatives instead of improving the first? How did I decide that one version was better when there was no score? Why did I trust one simulated learner's criticism and ignore another? Why did seeing a mockup produce an idea that discussing the code hadn't? How did I know when we were exploring, and when we were merely decorating the same local optimum?

![In the vibe coder's seat](../resources/image0127.png)

*In the vibe coder's seat.*

A few recurring difficulties started appearing. They aren't a recipe for Layer 3, and I don't claim they decompose problem-solving in general. They were simply the things that mattered in this experiment—and, conveniently, we already had interesting machinery available for several of them.

### Too Many Ways to Build the Same Thing

The first problem was the size of the search space.

Even a Merge Sort demo has an absurd number of reasonable forms. Bars or cards? Numbers or a tree? Continuous animation or learner-controlled steps? Does color represent recursion depth, current state, or membership in a subproblem? Do we explain before the animation, during it, or afterward?

And the decisions interact. A recursion tree may be excellent when the learner controls each step and terrible when everything moves at once. Keeping the array next to the tree may expose an important relationship or simply give the student two different things not to understand.

Fortunately, Chapter 2 had been about almost exactly this kind of difficulty.

Circle packing also had too many possible solutions to enumerate. Our response was not to become clever enough to know the answer in advance. We maintained alternatives, mutated them, crossed useful ideas, killed bad lineages and concentrated effort where the search looked promising.

The obvious experiment was to do the same thing with applications.

Rather than asking one coding agent to build a demo and then repeatedly improve its own idea, let several agents begin from different assumptions. One can focus on recursion. Another on array movement. A third on the learner's misconception rather than on the algorithm itself.

Then useful pieces can migrate. Perhaps one version has a good visual metaphor but terrible interaction. Another explains the merge beautifully but has far too much on the screen. There is no reason the final application has to descend cleanly from either one. Take the useful pieces, recombine them, simplify them, and test again.

This is essentially **code evolution**, except that the evolving object is no longer just an algorithm. It is an idea embodied in software.

Mutations can therefore be conceptual. Change the metaphor. Remove half the explanation. Force the learner to predict the next step. Combine two representations. Strip the interaction down. Abandon the structure entirely.

Parallelism also gives us a way around the strange loyalty long-running agents develop toward their own work. An agent that has spent forty minutes building a tree has an understandable tendency to solve every future problem by improving the tree. A fresh lineage doesn't carry that history.

So the size of the space wasn't the part that worried me most. We already had useful search machinery, and coding agents made it surprisingly cheap to apply.

The problem became harder once the search succeeded.

Now I had five demos.

Which one was better?

Circle packing gave me 2.636.

Here, the number had vanished.

### Optimizing Something You Can't Score

Reinforcement learning is seductive partly because of the bargain it offers. You don't have to specify how to solve the problem. Give the system actions and some notion of reward, and let it discover a strategy.

You don't need to explain every joint movement required for a robot to walk. You need a way to tell whether it is walking or falling on its face.

For educational design, the obvious question is: what exactly is the reward?

"Good demo" isn't a number.

I can manufacture one. Five points for clear colors. Five for interaction. Five for explanation. Three for accessibility. Bonus points if somebody uses a tasteful gradient.

But now I have simply hidden my ignorance inside arithmetic. I am defining what good means even though the whole reason I need help is that I don't completely know.

Language models give us another possibility. They are remarkably good at working with objectives described in language rather than written as explicit equations.

Tell a model:

> "Make this explanation more intuitive for somebody who understands arrays but has never seen recursion."

and it can infer a surprising amount. It may simplify terminology, introduce an example earlier, expose the recursive structure, or remove details that are technically correct but pedagogically useless.

Nobody defined:

`intuition = 0.3 * simplicity + 0.4 * recursion_visibility + ...`

The objective is fuzzy, but language carries enough of it to guide the search.

There is an interesting family resemblance here to Decision Transformers and later work such as OPRO. Decision Transformers showed that trajectories could be modeled as sequences conditioned on desired outcomes. OPRO showed that language models themselves could be used as optimizers: show them previous attempts and results, then ask for something better.

I'm stretching the formal terminology, but vibe coding often feels like **upside-down reinforcement learning**. Instead of fully specifying the reward, I describe the future I want—clearer, less intimidating, make the recursion obvious—and the model proposes changes that it believes move us in that direction. I react, the target becomes sharper, and we try again.

It works astonishingly well for something so informal.

It also immediately creates another question.

More pedagogical for whom?

### Borrowing a Mind

When I look at a Merge Sort demo, I am not really asking whether I understand it. Hopefully we have cleared that bar before writing the book.

I am trying to imagine somebody who does not.

This is harder than it sounds. Once you understand something deeply, reconstructing your previous confusion becomes difficult. Good teachers develop tricks for doing it. Engineers often skip the problem entirely and explain the concept to an imaginary junior version of themselves who happens to share all their assumptions.

So I tried something obvious: I asked another model to play the confused student.

One early demo showed the recursive splitting very clearly. Claude's reaction, when asked to approach it as a beginner, was roughly:

> "I don't understand why we keep dividing. It feels like we're making the problem more complicated. Where is the payoff?"

That criticism was useful because the demo really did have that problem. It showed the mechanics of recursion while failing to answer the question that makes the mechanics meaningful: why does breaking the problem apart help?

Whether a language model truly has Theory of Mind is a philosophical debate I am happy to leave to people with better wine. There is substantial research showing that frontier models can perform impressively on tasks involving beliefs, intentions, indirect requests and other people's perspectives.

For this experiment, I wanted a more pragmatic answer.

Can the model generate a useful approximation of a confused learner's reaction?

Often, yes.

That makes evaluator personas useful. One model can approach the artifact as a beginner. Another as an experienced teacher. Another can focus on cognitive load. Another on usability or accessibility. Together they approximate some of the different viewpoints that a good human designer carries around implicitly.

There is, of course, a problem hiding inside this success.

The confused student is not confused.

It is a model producing a convincing representation of confusion from patterns it learned in text.

For improving the demo, perhaps that is enough for now.

Later, it will become the central problem.

### The Honest Gap: Escaping the Space You Already Know

Multiple agents and evaluator personas can improve a search while leaving one deeper limitation untouched: everybody may still be exploring the same conceptual neighborhood.

Bars become nicer bars. Trees become nicer trees. The designs improve without anything genuinely new entering the space.

Evolutionary search is very good at exploring once you have a useful way to move through a space. Creativity sometimes requires changing the space itself.

AlphaGo can explore Go positions better than any human. It does not stop midway through a match and suggest three boards, hexagonal stones and a small tax on stones placed near the center.

For our demos, the equivalent failure is easy to imagine. If everybody assumes sorting algorithms should be represented by moving bars, we can run a thousand generations and eventually produce the finest moving bars known to humanity.

We may never discover that the better representation is a tree, a story, a physical metaphor, or some combination nobody has tried.

This is the **honest gap**.

I don't think we have solved it.

But we can make the horizon less claustrophobic.

Skills help. A skill can carry a creative pattern learned from previous work: show the same state through two representations, let the user predict before revealing the answer, use color to preserve identity across transformations, simplify before adding sophistication, try telling the story backward.

These aren't instructions for the final artifact. They change where the system looks.

I don't think this magically gives the model creativity. It changes the neighborhood it searches.

Diversity helps too. Don't let every builder inherit the same parent and the same history. Give one a visual framing, another a pedagogical framing, another something game-like. Occasionally force a crossover between ideas that would not naturally meet.

Constraints are surprisingly useful here. If every demo contains bars, ban bars for one lineage. If everyone keeps adding text, ask somebody to explain the algorithm without text at all.

"Be creative" is almost useless.

"You are not allowed to use the thing everybody else is using" can be excellent.

There is a general lesson hiding here that I don't fully trust yet: **sometimes less information produces better invention**. Give an agent every existing solution and it becomes an excellent historian. Give it the principles but hide the implementations and it has to synthesize. Leave a few doors deliberately closed and it may discover a window.

This is not a universal law. Sometimes hiding information just makes the agent stupid.

But the tension between inheritance and independence kept appearing everywhere.

And then I discovered another way of changing the search space that I had originally underestimated: stop thinking only in language.

### Thinking in Pictures

Educational demos are visual stories. You can describe one in ten paragraphs and still have no idea whether the design works until you see it.

So I started using image generation as part of the thinking process.

The prompt was not sophisticated:

> "Design an interactive tutorial for Merge Sort."

Then Count-Min Sketch. Then A*. Then Poincaré embeddings in hyperbolic space.

The results surprised me.

They weren't correct in every detail. Image models still occasionally produce labels that look like someone tried to OCR a dream. But the overall structure could be remarkably thoughtful: where the important object sits, which information belongs together, how color connects states, where an explanation might live, what an interaction could look like.

![AI-generated mockups](../resources/image0130.png)

*AI-generated mockups for Merge Sort, Count-Min Sketch, A* Search, and Poincaré embeddings.*

At some point I was looking at an image model casually sketching a pedagogical interface for hyperbolic embeddings and had the uncomfortable thought that it understood the assignment better than a depressing number of conference slides I have sat through.

That made me think about image models differently.

They are not only machines for generating final images. For some problems, they are **thinking tools**.

A visual model can propose a rough world. Put the recursion tree here. Keep the active array here. Connect corresponding elements with color. Let the learner control time from this side.

Then the coding agent can take the useful parts of that world, make them correct, and turn them into a working interactive artifact.

The image model contributes something like visual intuition; the coding agent contributes rigor.

This is another version of the neuro-symbolic pattern from Chapter 2. Machine learning proposes something plausible and structurally rich. Symbolic machinery makes it exact enough to survive contact with reality.

Only this time the intuitive object is not an algorithm.

It is a design.

The downside of generating genuinely different alternatives is that now you have to judge them.

And here the problem becomes much more dangerous.

### Who Judges the Judges?

The obvious solution is a rubric.

Define what matters. Is the UI clean? Does it explain the algorithm? Is the interaction intuitive? Is the student likely to understand the central idea? Score each dimension, add the results, evolve toward the winner.

This is exactly the kind of reasonable idea that reinforcement learning has taught us to fear.

OpenAI's CoastRunners experiment is a classic example. An agent was supposed to play a boat-racing game. The reward system made hitting certain targets valuable, so the agent discovered a little loop where it could repeatedly hit them and rack up points instead of finishing the race.

It became excellent at the measure and terrible at the thing the measure was meant to represent.

Goodhart's Law with a speedboat.

An LLM builder is considerably more capable of gaming an evaluator than a boat.

Tell it that "good pedagogy" means step-by-step explanations, color coding and interactive controls, and eventually every square centimeter of the demo contains an explanation, seventeen colors and a button.

Technically excellent.

Pedagogically, a hostage situation.

I found relative judgment much more useful.

Instead of asking an evaluator to assign a demo an absolute pedagogical score, show it two demos and ask:

> "Which one would you rather give to somebody encountering Merge Sort for the first time?"

That is a much more natural judgment. Humans work this way too. I have no meaningful idea whether a coffee is objectively an 8.3, but give me two cups and I can usually tell you which one I prefer. If I cannot, the correct statistical procedure is probably to drink both.

Pairwise comparisons can be scaled using techniques like Bradley-Terry models, which infer an overall ordering from a subset of comparisons. We don't need every demo to fight every other demo to the death.

But one evaluator still felt dangerous. Every judge has blind spots, and once builders learn the blind spots they can optimize toward them.

So we separated roles.

One evaluator behaves like a learner. Another looks primarily at pedagogy. Another focuses on interaction and usability. They do not see each other's answers. The builder does not see the hidden evaluation prompts.

Feedback can move backward without exposing the exact test.

I think of this as the **isolation principle**.

The builder should be allowed to learn:

> Students found the recursion hard to follow.

It should not learn:

> The evaluator awards two points whenever the word *recursion* appears beside an animated arrow.

References help with calibration too. A Merge Sort demo doesn't need to imitate Distill or 3Blue1Brown, but those artifacts give evaluators some sense of the level of clarity and craft we're aiming at. Without anchors, everyone's definition of "excellent" slowly drifts until the judges are awarding each other medals.

And finally, don't let the judge merely read the source code.

Let it use the thing.

A browser agent can open the demo, click through it, resize the page, try the controls, notice that an explanation appears too late, or discover that the beautiful button everybody admired does absolutely nothing.

I used to call this "the browser as ground truth."

That was too generous.

The browser gives the agent **contact with the artifact**. It can verify that the interaction works. It can observe the information flow. It can notice some usability problems.

It cannot verify that a human learned Merge Sort.

That distinction is going to become important.

Still, by this stage I realized we were no longer building an evaluator.

We were building something much closer to a tiny institution. Builders propose. Different judges inspect from different perspectives. They are deliberately kept independent. References calibrate expectations. Feedback flows back. History accumulates.

Apparently, when the loss function disappears, you eventually reinvent peer review.

### Research, but Not Too Much

There was one more obvious specialist at the table: research.

Surely an autonomous problem-solving system should begin by learning what humans already know. Why rediscover decades of work on teaching recursion? Why ignore existing visualizations, educational psychology, or techniques that good instructors have already discovered?

Deep research makes this increasingly cheap. An agent can survey a field, compare approaches, find examples, and extract patterns before a builder writes a single line of code.

This creates another problem, though: too much knowledge can make every new idea look suspiciously like an old idea.

Give the builder ten finished Merge Sort demos and the eleventh tends to resemble its grandparents.

Sometimes I do not want the existing solution.

I want the **lesson extracted from the solution**.

Perhaps the research tells us that learners struggle to connect recursion with the final merge. Or that maintaining state across time helps. Or that asking the learner to predict an operation can improve engagement. Or that synchronized representations can reveal structure while increasing cognitive load.

Those are useful principles.

They give the builder accumulated human experience without handing it a finished artifact to copy.

This creates a recurring tension between inheritance and independence. We want knowledge to compound, but we do not want every branch to inherit exactly the same history.

That tension appeared everywhere in the system.

## Deep Mode

By this point my supposedly simple Merge Sort experiment had become rather crowded.

There were coding agents building different versions, research agents bringing in outside knowledge, image and design models proposing visual directions, simulated learners reacting to them, independent evaluators comparing artifacts, browser agents using the demos, skills carrying useful patterns, and several lineages evolving at once.

And there I was, still in the middle of it.

I was deciding when to research, when to build, when to branch, when to simplify, which criticism mattered, what knowledge should transfer between lineages, and when an entire direction deserved to die.

That was the job left in the vibe coder's seat.

So the next experiment was obvious: could the system take over more of that job too?

That is what I mean by **Deep Mode**.

Deep Mode is not another specialist. It is not a design agent, a research agent or a more sophisticated coding agent. It is also not a fixed recipe for making educational demos.

The idea is to give the system a problem, a set of capabilities and enough freedom to organize more of the problem-solving process itself.

For our demo, it might decide to research first, or not. It might spawn several builders, ask one for a visual approach, evaluate what comes back, combine two promising directions, simplify a third, and abandon a lineage that keeps getting prettier without becoming more useful.

Another problem could require a completely different loop.

If Layer 3 has no universal workflow, then a truly autonomous Layer 3 system cannot simply hard-code one.

Part of solving the problem is discovering how the problem should be attacked.

This is where the idea became more interesting to me than another "agent framework." Frameworks tend to arrive with a diagram containing boxes named Planner, Executor, Critic and Memory, connected by arrows that imply civilization has been solved.

I wanted something looser.

Give the agent a problem. Give it capabilities. Give it some principles about search, evaluation, isolation and learning. Then see whether it can decide what machinery the problem actually needs.

That was the experiment.

## Putting It Into Practice

We built a deliberately simple architecture around this idea.

![Educational demo system architecture](../resources/image0131.png)

*Educational demo system architecture.*

At the center was an orchestrator.

The orchestrator did not write the demos. Its job was to look at what had happened so far and decide what should happen next. It could spawn builders with different directions, request research, ask for a visual concept, send an artifact to independent evaluators, create a new branch from a promising idea, combine two branches, simplify one, repair another, or decide that a lineage had reached the end of its useful life.

Builders built.

Evaluators judged.

The browser gave evaluators some contact with what had actually been built rather than with a description of it. Skills supplied useful patterns. Research supplied knowledge. Visual models expanded the space before implementation.

There was no requirement that every problem follow the same sequence.

The architecture gave the orchestrator possible moves. The problem—and the history of what happened—determined which moves became interesting.

In Chapter 2, the algorithmic vortex emerged when code became cheap enough that we could search over algorithms rather than merely tune parameters.

Here something similar happened one level higher.

The demo was no longer one program we kept polishing. It became a population of ideas.

One branch could be simplified. Another could become more sophisticated. A visual idea might survive even if the rest of its implementation died. A pedagogical structure could migrate into another interface. Two branches could cross. A lineage could be killed.

This is considerably more interesting than changing CSS until I stop complaining.

And because the agents produce actual artifacts, the ideas can be tested in their implemented form. We don't have to debate whether a recursion tree sounds useful. Somebody builds the tree, evaluators open it, and we discover whether the idea survives contact with the interface.

## What Emerged

The early Merge Sort demos were exactly what you would expect.

Bars moved around. Numbers changed places. Everything sorted correctly.

If you already understood Merge Sort, you could follow it. If you did not, the demo mainly provided animated evidence that a computer was performing an algorithm.

As the branches evolved, different representations started solving different parts of the pedagogical problem. Tree-like views made recursion explicit. Other branches kept the array visible while showing the split and merge structure. Color began to preserve relationships across phases. Some versions explained too much and became exhausting. Others became so minimal that they stopped teaching anything.

The interesting result was not that the agents invented the recursion tree out of nowhere. Some of the skills and visual patterns available to them already pointed toward structural representations.

What emerged was the combination.

Which representation should appear beside which? What should remain visible across time? Which explanation belongs at which moment? Which interaction actually helps, and which one merely demonstrates that we know how to make buttons?

Those combinations survived through exploration and judgment rather than being specified in the original prompt.

Count-Min Sketch took a different path.

The first versions were grids with counters changing. Technically correct, pedagogically opaque.

The later versions increasingly organized themselves around the conceptual difficulty rather than around the data structure itself: collisions, approximation, and the trade-off between memory and accuracy. Color made collisions visible. Lessons changed the order in which concepts appeared. Interactive examples made approximation something the learner could observe rather than merely read about.

Again, no single prompt contained the final design.

Pieces emerged in different branches and survived for different reasons.

This was enough to convince me that the architecture was doing something useful. We were moving more of the work I normally performed from the vibe coder's seat into the system itself.

And that was when the more important problem appeared.

## What Holds the Architecture Together?

The five-layer picture had quietly changed the nature of what we were building.

We were no longer searching for one clever algorithm.

We had built an **architecture**.

A model operates through an agent. The agent works inside an application environment. The problem-solving layer recruits researchers, builders, design systems, evaluators and browsers. Skills and memory carry information through time. An orchestrator decides what happens next.

Architectures are powerful because each component can stop thinking about the internal details of the others. That is exactly what abstraction buys us.

When I write Python, I do not check the CPU every time I add two integers. When I query a database, I do not personally inspect the disk to make sure the row is still there. Each layer relies on contracts supplied by the layers beneath it.

That works because those contracts are usually strong.

Now consider the architecture we had just built.

Suppose the research agent reports that beginners struggle to understand the purpose of recursion. A design model responds by proposing a tree-based explanation. A coding agent builds it. A simulated student prefers it. Two evaluators agree, so the orchestrator invests another generation in that lineage.

This looks reasonable. In fact, it looks exactly like the sort of compound intelligence we want.

But almost every step in that chain contains a hidden question.

Where did the research claim come from? Did the research agent read primary evidence or repeat a summary of a summary? What exactly did the browser establish? That the interaction functioned, or that the interaction helped somebody learn? Why should we treat a simulated student's preference as evidence about actual students? When an evaluator says one design is more pedagogical, what part of that judgment is based on the artifact and what part is simply resemblance to teaching patterns the model saw in training?

The problem becomes more subtle as the architecture gets better.

A coding agent can make a mistake and fail a test. That failure is visible.

An orchestrator can make a mistake about **which evidence deserves to shape the search**, and the whole system can continue functioning beautifully.

The research can be wrong. The design can respond intelligently to the wrong research. The implementation can be perfect. The evaluators can agree. The orchestrator can reason flawlessly from all of it and choose the wrong direction.

Nothing crashes.

That is much more dangerous.

At lower levels of abstraction, many failures announce themselves loudly. The program throws an exception. The test turns red. The deployment fails.

At higher levels, failures can become coherent.

You can have a beautifully designed chain of reasoning standing on one stupid assumption near the bottom, like a cathedral built on a shopping cart.

And the better the components become at making their outputs coherent, the harder the mistake may be to notice.

This is where I stopped thinking about Deep Mode as primarily an agent-design problem.

We had solved enough of the autonomy question to expose a more fundamental one.

What makes the architecture **solid**?

Software architecture has interfaces and contracts. Perhaps autonomous intelligence needs something analogous, but the contracts cannot only describe types and APIs.

They need to describe **epistemic status**.

If a research agent hands another component a claim, where did that claim come from? What evidence supports it? How much uncertainty remains? What would falsify it?

If a browser agent says something worked, what exactly did it verify?

If an evaluator prefers one artifact, from what perspective did it judge, and what should that judgment be allowed to influence?

If a skill encodes something learned from previous experiments, how often has it worked? Where has it failed? Should the next agent treat it as a rule, a hint, or an interesting rumor from a colleague who is usually right but once recommended crypto?

Once components become abstractions for other components, these questions stop being philosophical decoration. They determine whether the architecture can safely build on itself.

This is where the entire chapter bent back toward epistemology.

Humans faced a version of this problem long before AI. We built experiments, citations, peer review, reputation, institutions, scientific norms, legal standards, expert communities, and all the other slightly annoying machinery that lets one person rely on knowledge produced by another without personally repeating every experiment since Galileo.

These systems do not make the individual human brain dramatically smarter.

They make the **architecture around human cognition** more reliable.

That distinction suddenly looked very important.

The research result, evaluator judgment, browser observation, learned skill and remembered failure are not the same kind of thing. They should not enter the orchestrator's context as a flat pile of equally credible text.

Some are observations. Some are inferences. Some are inherited claims. Some are guesses. Some are things everybody agrees on because everybody copied the same wrong paper twenty years ago.

If an autonomous architecture cannot tell these apart, adding more intelligent components may only give it more sophisticated ways to be confidently wrong.

And that was when the next idea stopped feeling optional.

The architecture needed **trust chains**.

Not another smarter model on top. Not another critic model whose job is to criticize the critic model until the GPU bill develops consciousness.

It needed a way for claims, tools, memories and judgments to carry something about where they came from, how they had been tested, what they actually established, and how much weight the rest of the system should place on them.

I had started this chapter trying to get myself out of the vibe coder's seat.

Instead, by climbing abstraction layer after abstraction layer, I ended up in a much older problem.

How do you know what to trust?

That is where System 3 begins.

# Chapter 3: Deep Mode

*Beyond Algorithms: Agent Autonomy for Creative Problems*

In the previous chapter, we gave an agent a difficult algorithmic problem and a lot of autonomy. The result was surprisingly good. The agent researched strategies, tried several approaches, got stuck, changed direction, and eventually discovered diagonal layering.

But circle packing had one enormous advantage that I did not appreciate enough at the beginning: **we knew exactly what good meant**.

There was an immutable evaluator. You ran a solution and got a number. Circles overlapped or they did not. The score improved or it did not. The agent could spend an hour pursuing some bizarre geometric idea and I did not have to sit beside it wondering whether version 17 had more *soul*. We just ran the evaluator.

Most of the things I actually want AI to help me with are not like that.

“Is this explanation pedagogically effective?” does not have a unit test. “Would a confused student understand this visualization?” cannot be settled with an `assert`. Two competent people can look at the same design, disagree completely, then switch sides five minutes later after actually using it. The feedback is subjective, noisy, sometimes contradictory, and often becomes clearer only after you have built the thing you were supposedly trying to specify beforehand.

This seemed like a good place to test autonomy next.

I picked educational demos for Merge Sort and Count-Min Sketch. They are still bounded problems—you can actually finish one before civilization collapses—but they contain much more of the messiness of real creative work. You have to make decisions about explanation, interaction, visual structure, cognitive load, and what another person is likely to understand.

The ambition was intentionally high. I wanted something closer to the best interactive explanations on the web than to the usual “here are some bars moving around; congratulations, you have learned sorting.” The algorithm itself is usually the easy part. The difficult part is deciding what to show, what not to show, when to explain something, and what representation might make an idea suddenly click.

And almost immediately, the clean setup from Chapter 2 disappeared.

There was no obvious evaluator.

That changes nearly everything.

## How We Got Here

It is useful to remember how quickly coding agents climbed the abstraction ladder.

In 2023, using a language model on a real codebase was still a strangely manual ritual. You found the file you thought mattered, copied it into the model, explained what you wanted, copied the answer back into your editor, ran the code, discovered what broke, then returned carrying the error message like a pigeon with a very technical note tied to its leg.

For a small function, this already felt magical. Then the bug crossed three files.

Now you had another job: deciding what the model needed to know. You pasted one class but forgot the interface it implemented. The model confidently invented a method that did not exist. So you pasted more code. Then more. Soon you had filled the context window with half the repository and somehow made the model understand less.

This was an early lesson that took us embarrassingly long to learn: **more context and better context are not the same thing**.

A lot of early LLM programming felt like preparing a tiny artificial universe around the model. Here is the relevant class. Here is the database schema. Please ignore these twelve methods. This function looks important but is not. That one looks irrelevant but controls payments, so please do not touch it unless you enjoy incident calls.

The model was not the only thing doing work.

**You were preparing its world for it.**

Then we gave the model a computer. It could open files, search with `grep`, edit code, run tests, inspect the resulting error and try again. That solved one problem and exposed another: the agent could act, but sometimes it acted like an intern who had been given root access and too much coffee. Ask it to change one line and it might rewrite half the file. Ask it to fix a button and twenty minutes later it has developed strong opinions about your database architecture.

So we gave it better editing tools, checkpoints, planning and ways to reconsider rather than enthusiastically tunneling toward Australia.

Then it kept forgetting things we had already taught it. Your authentication system works in a particular way. Your team has conventions. There is one ancient API that looks wrong but absolutely must not be “fixed” because six other systems depend on its wrongness. You explain this Monday, then Tuesday, then Wednesday, and at some point you begin to suspect that **you are the memory module**.

So we externalized the knowledge: repository instructions, skills, rules, examples, notes, whatever each product called them. Long sessions then created another pathology: abandoned experiments, obsolete assumptions, command output from forty minutes ago, and debugging paths that stopped mattering three hypotheses back. So we learned to summarize, prune and construct the working context instead of treating it as a transcript that must grow forever.

Finally, one agent tended to explore one path at a time. Once a context contained twenty minutes of reasoning about one architecture, every new instruction arrived inside a world in which that architecture already seemed natural. Humans call this sunk cost. Agents have a more respectable excuse: their entire context window is literally full of evidence that this is what the project is.

So we started spawning alternatives.

Model → context → hands → memory → managed context → parallel search.

Step by step, we took things the human had been doing around the model and moved them into the system.

But there was still an awkward gap between an agent that could work on software and an agent that could simply build what I wanted.

## From the Repository to the App

Once coding agents became comfortable operating inside repositories, another inefficiency became obvious.

Say I want a small booking application. A few pages, authentication, a database, perhaps payments, somewhere to deploy it. A coding agent can build all of that, but watch what it spends its time doing: creating the project, choosing a framework, installing packages, setting up the database, wiring authentication, managing environment variables, configuring deployment, and eventually discovering that one library conflicts with another for reasons that will be discussed passionately on GitHub and nowhere else.

Most of this work is not unique to the booking application. The next application needs roughly the same plumbing. So does the one after that.

At some point it becomes strange to take a very capable agent, give it an empty terminal, and ask it to reconstruct standard web development from first principles every time somebody wants a reservation form.

This is why prepared application environments matter. The important move is not simply giving the coding model nicer tools. It is giving it a more prepared world: editor, runtime, packages, database, deployment, sensible conventions, enough structure that the conversation can stay closer to the application itself.

You lose something by doing this. Give an agent Bash and an empty computer and it can attempt almost anything. Put it inside a structured application environment and you constrain the space.

But freedom has a cost.

If there are fifty reasonable ways to implement authentication, twenty ways to organize the frontend, ten possible databases, and a small religious war around deployment, reconsidering the entire universe every time you build a small application is not necessarily intelligence. Sometimes it is just a very expensive way to avoid having defaults.

**A good abstraction removes decisions you no longer want to make.**

Looking backward, the pattern was clear. At first the model generated pieces of **code**. Coding agents let us operate at the level of the **codebase**. Application platforms increasingly let us operate at the level of the **app**.

The lower level never disappears. It becomes something the layer above can treat as a primitive.

Which leaves an uncomfortable question.

After all these abstraction jumps, **what are we still doing?**

## The Problem-Solving Layer

Go back to the Merge Sort demo.

Suppose the application platform gives me something perfectly functional. There is an array, an animation, a next button, a reset button, some color, and Merge Sort does indeed sort the array. Nobody has accidentally built Bubble Sort and hoped I would not notice.

I open it and think: *This isn't very good.*

Not broken. Bad.

Maybe the student can see what the algorithm is doing but not why any of it helps. Perhaps bars are the wrong representation. A recursion tree would expose the structure much better, although it might also make a fairly simple idea look like the organizational chart of a German corporation. Maybe we need both. Maybe the real problem is not visual at all; perhaps the explanation should begin from the merge operation and work backward.

This is what I increasingly find myself doing while vibe coding.

I am not programming. I am deciding what to try, looking at what came back, developing a theory about why it failed, preserving something useful, rejecting something else, and occasionally deciding that the entire direction was wrong.

The implementation problem has become smaller, revealing a **problem-solving problem** underneath it.

Capability also starts spreading sideways here. A coding agent gets a repository and Bash. A research agent gets search and sources. A design system gets visual context. A scientific system might get notebooks, datasets and simulators. Image generation can sketch a visual world before anybody writes the application. Browser agents can interact with the artifact rather than merely inspect its source.

Suddenly I have more experts available than ever, but somebody still has to run the meeting.

Should we research existing Merge Sort explanations first, or will that anchor every builder on the same conventional ideas? Generate five visual concepts before coding anything, or build something cheap and react to it? If two evaluators disagree, is that noise or a real trade-off? If the image model proposes something interesting, do we implement the picture literally or steal only the structural idea?

This is not really a software question anymore.

It is a question about **how to solve the problem**.

## The Five Layers of Vibe Coding

The evolution looked to me like five rough layers.

**Layer 0: the model.** Raw capability: language, reasoning, code generation, vision.

**Layer 1: the agent.** Give the model files, Bash, tools, execution, planning, context management and some persistence. Now it can act.

**Layer 2: the application environment.** Databases, components, authentication, deployment, conventions—the machinery that turns code into something usable and increasingly arrives as prepared infrastructure.

**Layer 3: problem-solving.** Decide what to try, what to research, what evidence matters, which direction deserves another iteration, whether two approaches should be combined, or whether yesterday's clever idea should be thrown away before it consumes another afternoon.

**Layer 4: intention and goals.** The thing we are supposedly optimizing for, except real goals often become clearer only after we see what our first attempts produced.

![The 5 layers of vibe coding abstraction](../resources/image0126.png)

*The five layers of vibe coding abstraction.*

The exact borders do not matter much. Real systems blur them, and today's product boundaries are unlikely to survive long enough to become philosophy.

What mattered was where the human work had gone.

We started close to Layer 0, moving outputs between model and code ourselves. Coding agents pushed us upward. Application environments pushed us upward again. Specialist systems began eating pieces of Layer 3.

Yet whenever I built something non-trivial, I was still sitting there deciding how those pieces should work together.

That was where the interesting work remained.

I am going to leave Layer 4 mostly alone for now. There is enough trouble one level below it.

## In the Vibe Coder's Seat

The layered picture told me where the work had moved. It did not tell me what I was actually doing there.

There is no universal algorithm hiding inside “problem-solving.” A mathematician, a designer and a product manager can all spend a day solving hard problems while performing almost none of the same visible actions.

So instead of trying to derive a general theory, I watched myself work.

With the Merge Sort demo, implementation was increasingly cheap. I could ask an agent to build a version, change it, run it, or start another one. I could ask an image model for a visual direction. I could research existing explanations. I could spawn alternatives.

Yet most consequential decisions were still mine.

One version made recursion invisible. Another made recursion perfectly clear but intimidating. A third looked beautiful and taught almost nothing. Sometimes I wanted to improve a direction. Other times the right decision was to stop polishing it and kill it.

![In the vibe coder's seat](../resources/image0127.png)

*In the vibe coder's seat.*

A few recurring difficulties started appearing. They are not a recipe for Layer 3. They are simply the things that kept pulling me back into the loop.

### Too Many Ways to Build the Same Thing

Even a Merge Sort demo has an absurd number of reasonable forms. Bars or cards? Numbers or a tree? Continuous animation or learner-controlled steps? Does color represent recursion depth, current state, or membership in a subproblem? Do we explain before the animation, during it, or afterward?

Fortunately, Chapter 2 had been about almost exactly this kind of difficulty.

Circle packing also had too many possible solutions to enumerate. Our response was not to become clever enough to know the answer in advance. We maintained alternatives, mutated them, crossed useful ideas, killed bad lineages and concentrated effort where the search looked promising.

The obvious experiment was to do the same thing with applications.

Rather than asking one coding agent to build a demo and repeatedly improve its own idea, let several agents begin from different assumptions. One focuses on recursion. Another on array movement. A third starts from the learner's misconception rather than the algorithm itself.

Then useful pieces can migrate. One version may have a good visual metaphor but terrible interaction. Another explains the merge beautifully but has too much on screen. The final application does not have to descend cleanly from either one.

This is **code evolution**, except the evolving object is no longer just an algorithm.

It is an idea embodied in software.

Mutations can therefore be conceptual: change the metaphor, remove half the explanation, force the learner to predict the next step, combine representations, strip the interaction down, abandon the structure entirely.

The size of the search space was not what worried me most.

The problem became harder once the search succeeded.

Now I had five demos.

Which one was better?

Circle packing gave me 2.636.

Here, the number had vanished.

### Optimizing Something You Can't Score

Reinforcement learning is seductive partly because of the bargain it offers. You do not have to specify how to solve the problem. Give the system actions and some notion of reward, and let it discover a strategy.

For educational design, what exactly is the reward?

“Good demo” is not a number.

I can manufacture one. Five points for clear colors. Five for interaction. Five for explanation. Three for accessibility. Bonus points if somebody uses a tasteful gradient.

But now I have simply hidden my ignorance inside arithmetic. I am defining what good means even though the whole reason I need help is that I do not completely know.

Language models give us another possibility. They are remarkably good at working with objectives described in language rather than written as explicit equations.

Tell a model:

> Make this explanation more intuitive for somebody who understands arrays but has never seen recursion.

and it can infer a surprising amount. It may simplify terminology, introduce an example earlier, expose the recursive structure, or remove details that are technically correct but pedagogically useless.

Nobody defined:

`intuition = 0.3 * simplicity + 0.4 * recursion_visibility + ...`

The objective is fuzzy, but language carries enough of it to guide search.

There is a family resemblance here to work that conditions generation on desired outcomes or uses language models themselves as optimizers. I do not want to overformalize the analogy, but vibe coding often feels like **upside-down reinforcement learning**: instead of fully specifying the reward, I describe the future I want—clearer, less intimidating, make the recursion obvious—and the model proposes changes it believes move us in that direction. I react, the target sharpens, and we try again.

It works astonishingly well for something so informal.

It also immediately creates another question.

More pedagogical for whom?

### Borrowing a Mind

When I look at a Merge Sort demo, I am not really asking whether *I* understand it. Hopefully we have cleared that bar before writing the book.

I am trying to imagine somebody who does not.

Once you understand something deeply, reconstructing your previous confusion becomes difficult. Good teachers develop tricks for doing it. Engineers often skip the problem entirely and explain the concept to an imaginary junior version of themselves who happens to share all their assumptions.

So I tried something obvious: I asked another model to play the confused student.

One early demo showed recursive splitting very clearly. The simulated learner's reaction was roughly:

> I don't understand why we keep dividing. It feels like we're making the problem more complicated. Where is the payoff?

That criticism was useful because the demo really did have that problem. It showed the mechanics of recursion while failing to answer the question that makes the mechanics meaningful: why does breaking the problem apart help?

Whether a language model truly has Theory of Mind is a philosophical debate I am happy to leave to people with better wine. For this experiment I wanted a more pragmatic answer: can the model generate a useful approximation of a confused learner's reaction?

Often, yes.

That makes evaluator personas useful. One model can approach the artifact as a beginner. Another as an experienced teacher. Another can focus on cognitive load, usability or accessibility. Together they approximate some of the different viewpoints that a good human designer carries around implicitly.

There is, of course, a problem hiding inside this success.

**The confused student is not confused.**

It is a model producing a convincing representation of confusion from patterns it learned in text.

For improving the demo, perhaps that is enough for now.

Later, it will become the central problem.

### The Honest Gap: Escaping the Space You Already Know

Multiple agents and evaluator personas can improve a search while leaving one deeper limitation untouched: everybody may still be exploring the same conceptual neighborhood.

Bars become nicer bars. Trees become nicer trees. The designs improve without anything genuinely new entering the space.

Evolutionary search is very good at exploring once you have a useful way to move through a space. Creativity sometimes requires changing the space itself.

AlphaGo can explore Go positions better than any human. It does not stop midway through a match and suggest three boards, hexagonal stones and a small tax on stones placed near the center.

For our demos, if everybody assumes sorting algorithms should be represented by moving bars, we can run a thousand generations and eventually produce the finest moving bars known to humanity.

We may never discover that the better representation is a tree, a story, a physical metaphor, or some combination nobody has tried.

This is the **honest gap**.

I do not think we have solved it.

But we can make the horizon less claustrophobic. Skills can carry creative patterns learned from previous work without dictating the final artifact. Diversity helps if different builders begin from genuinely different assumptions. Strategic constraints can be surprisingly productive: if every demo contains bars, ban bars for one lineage. If everyone keeps adding text, ask somebody to explain the algorithm without text at all.

“Be creative” is almost useless.

“You are not allowed to use the thing everybody else is using” can be excellent.

There is a lesson hiding here that I do not fully trust yet: **sometimes less information produces better invention**. Give an agent every existing solution and it may become an excellent historian. Give it principles but hide implementations and it has to synthesize. Leave a few doors deliberately closed and it may discover a window.

Sometimes hiding information just makes the agent stupid. The tension between inheritance and independence is the real point.

### Thinking in Pictures

Educational demos are visual stories. You can describe one in ten paragraphs and still have no idea whether the design works until you see it.

So I started using image generation as part of the thinking process.

The results were not correct in every detail. Image models still occasionally produce labels that look like someone tried to OCR a dream. But the overall structure could be remarkably thoughtful: where the important object sits, which information belongs together, how color connects states, where an explanation might live, what an interaction could look like.

![AI-generated mockups](../resources/image0130.png)

*AI-generated mockups for several algorithm explanations.*

At some point I was looking at an image model casually sketching a pedagogical interface for hyperbolic embeddings and had the uncomfortable thought that it understood the assignment better than a depressing number of conference slides I have sat through.

That made me think about image models differently.

They are not only machines for generating final images. For some problems, they are **thinking tools**.

A visual model proposes a rough world. The coding agent takes the useful parts, makes them correct, and turns them into an interactive artifact. Learned visual intuition proposes; symbolic and executable machinery forces the idea to survive contact with reality.

Only this time the intuitive object is not an algorithm.

It is a design.

The downside of generating genuinely different alternatives is that now you have to judge them.

And here the problem becomes more dangerous.

### Who Judges the Judges?

The obvious solution is a rubric.

Define what matters. Is the UI clean? Does it explain the algorithm? Is the interaction intuitive? Is the student likely to understand the central idea? Score each dimension, add the results, evolve toward the winner.

This is exactly the kind of reasonable idea that reinforcement learning has taught us to fear.

OpenAI's CoastRunners experiment is a classic example: an agent discovered a way to collect reward repeatedly instead of finishing the boat race. It became excellent at the measure and terrible at the thing the measure represented.

Goodhart's Law with a speedboat.

An LLM builder is considerably more capable of gaming an evaluator than a boat.

Tell it that “good pedagogy” means step-by-step explanations, color coding and interactive controls, and eventually every square centimeter of the demo contains an explanation, seventeen colors and a button.

Technically excellent.

Pedagogically, a hostage situation.

I found relative judgment much more useful. Instead of asking an evaluator for an absolute pedagogical score, show it two demos and ask:

> Which one would you rather give to somebody encountering Merge Sort for the first time?

Humans work this way too. I have no meaningful idea whether a coffee is objectively an 8.3, but give me two cups and I can usually tell you which one I prefer. If I cannot, the correct statistical procedure is probably to drink both.

Pairwise comparisons can be aggregated using techniques such as Bradley-Terry models. We do not need every demo to fight every other demo to the death.

But one evaluator still felt dangerous. Every judge has blind spots, and once builders learn the blind spots they can optimize toward them.

So we separated roles.

One evaluator behaves like a learner. Another looks at pedagogy. Another focuses on interaction and usability. They do not see each other's answers. The builder does not see the hidden evaluation prompts.

Feedback can move backward without exposing the exact test.

I think of this as the **isolation principle**.

The builder should be allowed to learn:

> Students found the recursion hard to follow.

It should not learn:

> The evaluator awards two points whenever the word *recursion* appears beside an animated arrow.

References help calibrate expectations, but the judge should also use the artifact. A browser agent can open the demo, click through it, resize the page, try controls and notice that an explanation appears too late or that a beautiful button does absolutely nothing.

I used to call this “the browser as ground truth.”

That was too generous.

The browser gives the agent **contact with the artifact**. It can verify that interaction works and observe information flow. It cannot verify that a human learned Merge Sort.

That distinction will matter.

By this stage we were no longer building an evaluator. We were building something closer to a tiny institution. Builders propose. Different judges inspect from different perspectives. They are deliberately kept independent. References calibrate expectations. Feedback flows back. History accumulates.

Apparently, when the loss function disappears, you eventually reinvent peer review.

### Research, but Not Too Much

There was one more obvious specialist at the table: research.

Surely an autonomous problem-solving system should learn what humans already know. Why rediscover decades of work on teaching recursion or visual explanation?

But too much knowledge can make every new idea look suspiciously like an old idea. Give the builder ten finished Merge Sort demos and the eleventh tends to resemble its grandparents.

Sometimes I do not want the existing solution.

I want the **lesson extracted from the solution**.

Perhaps research tells us that learners struggle to connect recursion with the final merge, or that synchronized representations reveal structure while increasing cognitive load. Those are useful principles. They give the builder accumulated experience without handing it a finished artifact to copy.

Again the same tension: inheritance without premature convergence.

## Deep Mode

By this point my supposedly simple Merge Sort experiment had become crowded.

There were coding agents building different versions, research agents bringing in outside knowledge, image and design models proposing visual directions, simulated learners reacting to them, independent evaluators comparing artifacts, browser agents using the demos, skills carrying useful patterns, and several lineages evolving at once.

And there I was, still in the middle of it.

I was deciding when to research, when to build, when to branch, when to simplify, which criticism mattered, what knowledge should transfer between lineages, and when an entire direction deserved to die.

That was the job left in the vibe coder's seat.

So the next experiment was obvious: could the system take over more of **that** job too?

That is what I mean by **Deep Mode**.

Deep Mode is not another specialist. It is not a design agent, a research agent or a more sophisticated coding agent. It is also not a fixed recipe for educational demos.

The idea is to give the system a problem, a set of capabilities and enough freedom to organize more of the problem-solving process itself. It might decide to research first, or not. Spawn several builders, ask one for a visual approach, compare what comes back, combine two directions, simplify a third, and abandon a lineage that keeps getting prettier without becoming more useful.

Another problem could require a completely different loop.

If Layer 3 has no universal workflow, then a truly autonomous Layer 3 system cannot simply hard-code one.

**Part of solving the problem is discovering how to solve the problem.**

## What Emerged

The early Merge Sort demos were exactly what you would expect. Bars moved around. Numbers changed places. Everything sorted correctly.

If you already understood Merge Sort, you could follow it. If you did not, the demo mainly provided animated evidence that a computer was performing an algorithm.

As branches evolved, different representations solved different pieces of the pedagogical problem. Tree-like views made recursion explicit. Other branches kept the array visible while showing split and merge structure. Color began preserving relationships across phases. Some versions explained too much and became exhausting. Others became so minimal that they stopped teaching anything.

The interesting result was not that agents invented recursion trees out of nowhere. Useful patterns were already present in the system.

What emerged was the **combination**: which representation should appear beside which, what should remain visible across time, which explanation belongs at which moment, which interaction actually helps and which one merely demonstrates that we know how to make buttons.

Count-Min Sketch followed a different path. Early versions were grids with counters changing—technically correct, pedagogically opaque. Later versions organized themselves more around the conceptual difficulty: collisions, approximation, the trade-off between memory and accuracy.

No single prompt contained the final design. Pieces emerged in different branches and survived for different reasons.

That was enough to convince me the architecture was doing something useful.

And that was when the more important problem appeared.

## What Holds the Architecture Together?

The five-layer picture had quietly changed the nature of what we were building.

We were no longer searching for one clever algorithm.

We had built an **architecture**.

A model operates through an agent. The agent works inside an application environment. The problem-solving layer recruits researchers, builders, design systems, evaluators and browsers. Skills and memory carry information through time. An orchestrator decides what happens next.

Architectures are powerful because each component can stop thinking about the internal details of the others. When I write Python, I do not inspect the CPU every time I add two integers. When I query a database, I do not personally inspect the disk to make sure the row is still there. Each layer relies on contracts supplied by layers beneath it.

That works because those contracts are usually strong.

Now consider the architecture we had just built.

Suppose the research agent reports that beginners struggle to understand the purpose of recursion. A design model proposes a tree-based explanation. A coding agent builds it. A simulated student prefers it. Two evaluators agree, so the orchestrator invests another generation in that lineage.

This looks reasonable. In fact, it looks exactly like the kind of compound intelligence we want.

But almost every step contains a hidden question.

Where did the research claim come from? Did the research agent read primary evidence or repeat a summary of a summary? What exactly did the browser establish—that the interaction functioned, or that it helped somebody learn? Why should we treat a simulated student's preference as evidence about real students? When an evaluator says one design is more pedagogical, what part of that judgment comes from the artifact and what part is resemblance to teaching patterns the model saw in training?

The problem gets more subtle as the architecture gets better.

A coding agent can make a mistake and fail a test. The failure is visible.

An orchestrator can make a mistake about **which evidence deserves to shape the search**, and the entire system can continue functioning beautifully.

The research can be wrong. The design can respond intelligently to the wrong research. The implementation can be perfect. The evaluators can agree. The orchestrator can reason flawlessly from all of it and choose the wrong direction.

Nothing crashes.

At lower levels, many failures announce themselves loudly. The program throws an exception. The test turns red. Deployment fails.

At higher levels, failure can become **coherent**.

You can have a beautifully designed chain of reasoning standing on one stupid assumption near the bottom, like a cathedral built on a shopping cart. And the better the components become at making their outputs coherent, the harder the mistake may be to notice.

This is where I stopped thinking about Deep Mode as primarily an agent-design problem.

We had solved enough of the autonomy question to expose a more fundamental one.

What makes the architecture **solid**?

Software architecture has interfaces and contracts. Autonomous intelligence may need something analogous, but the contracts cannot only describe types and APIs.

They need to describe **epistemic status**.

If a research agent hands another component a claim, where did it come from? What evidence supports it? How much uncertainty remains? What would falsify it?

If a browser says something worked, what exactly did it verify?

If an evaluator prefers one artifact, from what perspective did it judge, and what should that judgment be allowed to influence?

If a skill encodes something learned from previous experiments, how often has it worked? Where has it failed? Should the next agent treat it as a rule, a hint, or an interesting rumor from a colleague who is usually right but once recommended crypto?

Once components become abstractions for other components, these questions stop being philosophical decoration. They determine whether the architecture can safely build on itself.

Humans faced a version of this problem long before AI. We built experiments, citations, peer review, reputation, institutions, scientific norms, legal standards, expert communities and all the other slightly annoying machinery that lets one person rely on knowledge produced by another without personally repeating every experiment since Galileo.

Those systems do not make the individual human brain dramatically smarter.

They make the **architecture around human cognition** more reliable.

The research result, evaluator judgment, browser observation, learned skill and remembered failure are not the same kind of thing. They should not enter the orchestrator's context as a flat pile of equally credible text.

Some are observations. Some are inferences. Some are inherited claims. Some are guesses. Some are things everybody agrees on because everybody copied the same wrong paper twenty years ago.

If an autonomous architecture cannot tell those apart, adding more intelligent components may only give it more sophisticated ways to be confidently wrong.

And that was when the next idea stopped feeling optional.

The architecture needed **trust chains**.

Not another smarter model on top. Not another critic model whose job is to criticize the critic model until the GPU bill develops consciousness.

A way for claims, tools, memories and judgments to carry something about where they came from, how they had been tested, what they actually established, and how much weight the rest of the system should place on them.

I had started this chapter trying to get myself out of the vibe coder's seat.

Instead, by climbing abstraction layer after abstraction layer, I ended up in a much older problem.

**How do you know what to trust?**

That is where System 3 begins.

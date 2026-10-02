# Chapter 3: The Vibe Coder’s Seat

*Beyond Algorithms: Agent Autonomy for Creative Problems*

The circle-packing agent could spend an hour pursuing some bizarre geometric idea and I did not have to sit beside it wondering whether version seventeen had more soul. We ran the evaluator.

Then I asked for an educational demo.

Most of the things I actually want AI to help me with are not like that. “Is this explanation pedagogically effective?” does not have a unit test. “Would a confused student understand this visualization?” cannot be settled with an `assert`. Two competent people can look at the same design, disagree completely, then switch sides five minutes later after using it. The feedback is subjective, noisy, sometimes contradictory, and often becomes clearer only after you have built the thing you were supposedly trying to specify beforehand.

I picked educational demos for Merge Sort and Count-Min Sketch because they were still bounded (you can actually finish one before civilization collapses), but they live on the messier side of the boundary. You have to decide what to explain, what to leave out, how the interaction should work, how much should be visible at once, and what another person is likely to understand from any of it.

The ambition was intentionally high. I wanted something closer to the best Distill articles or Jay Alammar’s visual explanations than to the usual “here are some bars moving around; congratulations, you have learned sorting.” The algorithm itself is usually the easy part; the difficult part is deciding what to show, when to show it, and what representation might make an idea suddenly click.

Circle packing let the search be complicated because judgment was simple. Here judgment had become part of the problem.

The problem-solving layer I eventually started calling **Deep Mode** grew out of one question: could the system take over some of the work of deciding what to try next, the inquiry itself as well as the implementation? Build another version, research the failure, retrieve an old idea, split into independent branches, change perspective or abandon the direction?

Before trying to automate that, I had to notice how much of the work around the model had already moved into the machine.

## Stubbornly Human

Models trained to continue text turned out to continue code.

Then GitHub Copilot put the trick inside the editor. Describe what should happen next and watch it appear underneath your cursor, which was delightful for about a week and then became the way things were.

A real software task rarely arrives with a docstring politely explaining what needs to change. Someone says invoices occasionally show the wrong tax after a refund. Somewhere inside a 150,000-line CRM there is a reason. It may involve a controller, a database model, an old helper and an API whose behavior nobody thought to document.

By the time GPT-4 arrived, I wanted to use models on exactly these problems, and the workflow I invented for it was ridiculous. Find the file you suspect. Copy a class into ChatGPT. Describe the bug. Copy the suggested patch into the editor. Run the program. Discover a new error. Copy the traceback. Paste that back into ChatGPT. Repeat until it works or until dinner.

My first agent-computer interface was copy and paste.

I thought I was using a very good autocomplete. The model might have been doing sophisticated reasoning, but I was searching the repository, assembling the context, applying the edit, running the tests and carrying back whatever reality had said about it. I was the hands, the eyes and the memory. The model was a brain in a jar, and I was the jar’s entire staff.

Then the bug crossed three files and context itself became a job. Paste one class but forget its interface, and the model invents a nonexistent method. Add the interface and it needs the schema, then another helper. Eventually half the repository is sitting in the conversation and somehow the model understands less. Alongside the code came instructions: ignore these twelve methods; this innocent-looking helper controls payments, so please do not touch it unless you enjoy incident calls.

We learned an obvious lesson surprisingly slowly: more context and better context are different things. If somebody asks for a spoon, emptying the entire kitchen onto the table does not help.

SWE-bench tested this larger job using real GitHub issues. The system had to navigate an existing repository, understand relationships across files, make a change and survive the tests. It had to do my job, the copy-and-paste one.

Eventually we gave the model the repository and a terminal. It could search, open files, edit them, inspect the diff and run tests. Return the failures and let them shape its next attempt. A coding agent is, at its simplest, this loop made executable.

Software is unusually friendly to this arrangement: files can be searched, programs can be run, tests can say no, and Git can tell you exactly what changed and, if an experiment becomes sufficiently exciting, return you to the time before you had the idea.

Of course, giving the model a computer created new ways to be annoying. Early coding agents could behave like interns with root access and too much coffee. Ask one to change a line and it might rewrite half the file. Ask it to fix a button and twenty minutes later it has developed strong opinions about the database architecture. It would find one plausible theory of a bug, follow it for too long, then use every new piece of evidence to improve the theory instead of admitting the theory was wrong. I recognized the behavior. I had done all of it myself, at two in the morning, with worse excuses.

So more of the surrounding work moved into the system: small patches, diff inspection, targeted tests, checkpoints, planning, rollback. Repository knowledge moved too. Authentication conventions, ancient APIs and local rules that used to live in somebody’s head became `CLAUDE.md`, `AGENTS.md`, rules files and skills. If somebody had already learned something expensive about the codebase, we left it somewhere the next agent could find it.

Long sessions produced the opposite problem. Context filled with abandoned experiments, obsolete assumptions and test output from three hypotheses ago, and memory became a problem of selection more than storage.

Then history became a problem too. Suppose an agent decides early that our Merge Sort demo should use React and a recursion tree. It spends forty minutes building that version. Every later question now arrives in a context containing forty minutes of reasons, code and decisions supporting React and a recursion tree.

Humans call our version of this sunk cost. The agent has a respectable excuse: its context window is literally full of evidence that this is what the project is.

So we started giving different attempts different histories. One agent tries the tree. Another begins with the array. A third starts from the learner’s misconception. A fresh branch does not have to spend half its intelligence escaping assumptions accumulated by the previous one.

Together, the interfaces, execution loop, context management and safeguards make up the agent’s harness, meaning here everything built around the model so it can work, of which the evaluator is only one part. The jar had acquired its own staff.

But there was still a large difference between an agent that could work competently inside a repository and the thing I increasingly wanted to ask for, which was simply *build the application.*

Ask for a booking application for a football academy and an unconstrained coding agent first chooses a framework, installs packages, creates a database, decides how authentication should work, manages environment variables and configures deployment. Several minutes later, we have made enormous progress toward having somewhere to put the booking form.

Somebody has to do that work. But if the same plumbing is reconstructed on every project, it becomes reasonable to prepare more of the world in advance. This is what made systems such as Replit and Lovable interesting to me. Runtime, deployment and common application machinery are already nearby, so the conversation can begin much closer to the application.

You lose some freedom, and that is often the point. A chef does not begin dinner by manufacturing a knife. When I open Python, I accept an astonishing number of decisions made by people I will never meet, because reconsidering all of them would make `print("hello")` a multigenerational project.

Useful abstractions remove decisions whose answers are no longer interesting most of the time. After enough of those decisions disappear, something else becomes easier to see.

Suppose the booking app works perfectly. The database is connected, deployment succeeds, the buttons behave, the mobile layout is respectable, and nobody has accidentally built a cryptocurrency exchange inside the authentication service.

I open the application and think: this is not very good. The software works. Now I have to worry about the football academy.

Parents probably shouldn’t see sessions meant for somebody else’s age group. I still have to decide when they should create an account, how to handle bookings for three children, and how late they can cancel. And if Wednesday is empty while Saturday has a waiting list, the booking interface might be part of that problem.

None of those questions is really about React. They were always there; implementation simply consumed enough attention that deciding what should exist and turning that decision into software felt like one activity.

When another version becomes cheap, the balance changes. You can see the idea sooner, and seeing it gives you information you did not have while discussing it.

Maybe we decide customers should create an account before seeing availability. It sounds reasonable: we need their details eventually. Then we build it and the experience immediately feels annoying. Parents arriving from a Google search do not want to establish a lifelong digital relationship with a football academy before discovering whether Saturday at ten is available. So login moves later, and the artifact becomes something we think with.

The Merge Sort demo made this even clearer because there was almost no business machinery to hide behind. I could ask an agent for an interactive explanation and receive something perfectly functional: an array of bars, controls, animation, perhaps some text explaining that the algorithm divides the input and merges the pieces again.

Technically, it was fine. Pedagogically, it could still be terrible. Watching bars move does not tell a beginner why dividing the problem helps. So perhaps we try a recursion tree. The tree makes the structure visible, but now the supposedly simple sorting algorithm resembles the organizational chart of a German corporation. Maybe we show the tree and array together. Perhaps that creates too much cognitive load. Maybe the problem is not the representation at all; the learner understands splitting perfectly well but has no idea why merging makes the whole trick useful.

There is no compiler error that tells me which diagnosis is right. I have to look at what we built, form an opinion about why it fails, and decide what would teach us something next. That might be a better version of this demo, a deliberately different one, some research, or putting the thing in front of somebody who does not already understand Merge Sort.

Occasionally I discover that the question I started with was wrong. “Build an interactive Merge Sort demo” sounds like a goal until you see several interactive Merge Sort demos. Perhaps what I actually care about is getting somebody who has never encountered divide-and-conquer to understand why breaking one difficult problem into smaller ones helps. Once I realize that, interactivity is merely one possible means.

That is the layer that remained stubbornly human: deciding what to try, which evidence matters, whether a result failed because of its implementation or its underlying idea, and what kind of attempt might teach us something next.

## The Five Layers of AI Coding

By then I had a rough map. Each layer marked a different kind of work we had learned to delegate, or were still trying to. I could draw the stack afterward because each working layer had made the next unfinished job easier to see.

**Layer 0—Model.** GPT, Claude, Gemini and whatever comes next: general capability in language, code, reasoning and vision.

**Layer 1—Agent.** Put the model in an environment where it can act. Claude Code, Codex and similar systems search repositories, edit files, execute commands and react to results.

**Layer 2—Application.** Prepared environments remove much of the repeated software plumbing and let the conversation stay closer to the application itself.

**Layer 3—Deep Mode.** The problem-solving layer: decide what to try, why something failed, which evidence matters, and whether the current direction deserves another iteration.

**Layer 4—Desire.** What do we actually want? This is the problem I have mostly been avoiding.

Software likes that question to have been answered before work begins, preferably in Jira, where the answer can remain wrong in a structured and searchable format. Real goals are less cooperative. Seeing a solution can change what I realize I wanted. That problem is bigger than AI coding, so for now I am leaving it at the top of the stack.

The borders are fuzzy. Coding agents make product decisions; design systems generate code; tomorrow’s products will rearrange the boxes again. What matters is the kind of decision being made. Which company happens to occupy which layer is a detail.

People often call the experience of working this way *vibe coding*. I will use *AI coding* for the broader stack, but *vibe coder* remains a wonderfully accurate name for the human sitting near Layer 3: looking at what came back, deciding what feels wrong, asking for another direction, killing one idea, keeping part of another, and steering the process without having an algorithm for how.

The lower layers increasingly answer a version of the same question, *how do we make this?* Deep Mode asks a different one:

**Given everything we have learned so far, what should we try next?**

That was the part I still seemed to be doing manually. So I watched what I was actually doing in that seat.

## What I Was Still Doing

There was no universal workflow hiding there. A mathematician, a designer and a product manager can all spend a day solving hard problems while performing almost none of the same visible actions.

But the same kinds of moves kept appearing, in no particular order. I needed another attempt, or more information. The search had become too narrow, or the representation was limiting what we could imagine, or the objective itself needed to change. Now and then I needed to see the artifact from another mind.

### Keeping More Than One Idea Alive

Even a Merge Sort demo has an absurd design space. It can use bars or cards, numbers or a tree, continuous animation or steps the learner controls. Color can mean recursion depth, identity or the active subproblem, and the explanation can come before the animation, during it or afterward. Every choice changes the usefulness of several others.

When implementation was expensive, we dealt with much of this complexity by trying to decide more before building. AI coding changes the economics. If another implementation costs minutes instead of days, I do not have to choose quite so much in advance. What evolves can be more than a vector of parameters or even an algorithm; it can be an idea embodied in software.

One builder tries a recursion tree. Another focuses on the array. A third begins from the learner’s misconception. Mutations can be conceptual: remove the text, teach backward, make the learner predict, show synchronized representations, abandon interaction altogether.

Useful pieces can move between them. One terrible demo may have a beautiful color mapping. Another may explain the merge clearly while making everything else unbearable. The final artifact does not have to inherit the entire history of either one.

But diversity is fragile. If every branch sees the current winner and its complete reasoning history, parallelism quickly becomes several agents improving the same idea.

Research creates the same risk. People have been teaching recursion for decades. There are textbooks, lecture notes, visualizations, papers, classroom experiments and a great deal of trial and error sitting on the internet. Before I spend another afternoon inventing my fourth way of moving colored rectangles around, I probably want to know what is already there.

But research is most useful when the work has produced a real question. Suppose a recursion tree makes decomposition visible but learners lose the relationship between the tree and the changing array. Now I can ask how other systems have coordinated two representations without requiring people to watch half the screen at once. At that point research is a move in the investigation, and it stops being a ceremony performed before building.

Retrieval plays the same role inside our own history. Somewhere in a growing project there may be research notes, screenshots, evaluator comments, old branches and a discarded prototype whose only good idea was a color mapping that solves exactly the problem in front of us. I do not need the whole archive. I need the thing that helps with this decision.

Exact search works when I remember a phrase, an API or an evaluator comment; embeddings help when I remember the idea and have lost the words; and some documents already have a structure worth navigating. Good coding agents do not “retrieve the repository” once; they move through it as the question changes. Layer 3 needs the same habit across stranger objects: research, screenshots, old interactions, code, evaluations and dead branches.

A dead branch can still hold live knowledge. A lineage that lost globally may contain a stepping stone that becomes useful later. Do not spend the entire search budget polishing the place that currently looks best. Preserve some alternatives and some routes back to places that almost worked.

The same logic gave us strategic constraints. After several generations of Merge Sort demos, the builders were exploring. They were also still giving me bars. Better bars, admittedly. Bars that split gracefully, changed color as recursion deepened, synchronized with a tree and perhaps deserved their own design award. Given enough iterations, I had every reason to believe we would eventually produce the finest moving bars known to humanity.

So remove the easy path. No bars.

Or: teach Merge Sort without explanatory text. Require the learner to predict before anything moves. Make the demo work on a phone with room for only one representation. Design it for somebody who understands loops but finds recursion suspicious.

Most arbitrary constraints are merely arbitrary. A useful one changes which parts of the search are reachable, exposes a neglected dimension or prevents a familiar attractor from absorbing every attempt. “No bars” was an intervention on the search, nothing grander.

A move in this space can be a code change, a new metaphor, a retrieved analogy, a fresh agent with no history, a different evaluator, a research question, or a reformulation of the problem itself. Even then, most of our ideas still had to arrive as words.

### Draw It Before You Build It

That is fine when I am working on an argument. It is less obviously sensible when I am designing an interface. I can spend ten minutes explaining where the recursion tree should sit, what remains visible while the array splits, how colors should connect two representations and what the learner should notice first. Then somebody draws it and I know within three seconds that the whole thing is terrible.

So I started generating the picture first, in a thoroughly unsophisticated experiment. I asked an image model to design an interactive tutorial for Merge Sort, then Count-Min Sketch, then A*, then Poincaré embeddings in hyperbolic space, partly because if this still worked there I would have to take the idea seriously.

The details were not magically correct. Arrows occasionally pointed somewhere they had no business pointing, interactions made no computational sense, and generated text sometimes looked like somebody had tried to OCR a dream.

But the composition could be surprisingly thoughtful. A Merge Sort mockup might keep the array visible while placing the recursion tree beside it, using color to preserve the relationship between a subarray and its node. A Count-Min Sketch design might make collisions visually central instead of leaving them as a detail in an equation. The model had to decide what was large, what was peripheral, where controls belonged and how the learner might move through the explanation.

I remember looking at some of these and thinking: holy shit. I didn’t want to ship the images, and usually I didn’t. What got me was that I had given the model a concept in language and it had returned something like a spatial argument about how the concept might be taught.

After that I stopped treating image generation as the last stage (*the product is designed, now make it pretty*) and started using it while I was still trying to understand what the product could be. A mockup is a cheap hypothesis. Often most of it is disposable and one relationship is worth stealing.

Then the coding agent can make that relationship executable, which is where the picture has to pay its debts. The recursion tree cannot invent an extra branch because the composition looked nicer that way. The interaction has to possess a state. The button has to do something other than contribute emotionally to the page.

Different representations expose different mistakes. I do not need the stronger claim that an image model “understands pedagogy.” The practical point is enough: changing the representation changes what the search can discover.

## Optimizing Something You Cannot Score

Circle packing was unusually kind to us. Once the geometry was valid, the evaluator reduced the result to one number. That number threw almost everything else away, which was precisely why it was useful.

A huge amount of machine learning rests on this trick. We take something complicated that we want and find a measurable signal that stands in for it. Reinforcement learning makes the relationship especially obvious: we do not specify every movement a robot should make while learning to walk; we construct a reward and let search discover the behavior. The reward does an extraordinary amount of work, and it is where we hide an extraordinary amount of trouble.

Suppose I want the same convenience for educational design. I can make a rubric: correctness, pedagogical clarity, visual quality, interaction, accessibility, engagement. Give each a weight and suddenly my vague dissatisfaction with a demo has become a respectable decimal.

The decimal is comforting. Giving interaction fifteen percent would make the rubric precise without telling me why that weight was justified. I would still need to say what separates a seven from an eight in pedagogy, and why the list includes engagement but leaves out whether the learner can predict what happens next or explain why the merge matters. A metric forces me to commit to an idea of “good” before the search has taught me very much about the problem.

I have nothing against metrics. If I care about latency, measure latency. If the code must pass a test, run the test. Hard measurements are wonderful when what we can measure is close to what we care about. The trouble begins when a rich objective is still poorly understood and we compress it anyway because optimization wants a number.

The compression is also low bandwidth. “Version B scored 7.4; version A scored 7.1” tells the next builder almost nothing about why B won. A rubric helps, but as I add enough dimensions, exceptions and qualifications to express what I mean, eventually I reinvent language badly.

Meanwhile I can simply say:

> The recursion tree makes decomposition much clearer, but now the learner has to watch the tree and the array simultaneously. Keep the color mapping that preserves identity between them, simplify the tree, and make the merge feel like the payoff rather than cleanup at the end.

That contains comparison, diagnosis, trade-offs, priorities and a proposed next move in a few sentences. Natural language is ridiculously rich compared with a scalar.

Language models make that communication channel available inside the optimization loop. The model already carries learned structure behind words such as *simple*, *confusing*, *elegant*, *intuitive*, *busy* and *beginner-friendly*. Those meanings are imperfect, culturally loaded and sometimes wrong. But they carry more structure than 7.4.

Natural language can therefore function as an *implicit metric*, though not in the strict mathematical sense: there is no guarantee that “intuitive” defines a stable ordering, and two evaluators may interpret it differently. Still, language can do some of the work a metric normally does. It gives the search a direction, communicates why one attempt is preferred to another, and preserves trade-offs that a scalar would erase.

Let the record of past attempts that the model sees contain more than scores. Alongside hard measurements, tell the model what improved, what became worse, which trade-off appeared and what must survive the next attempt, and the history of the search keeps some of its meaning instead of collapsing into a column of numbers.

This begins to feel a little like reinforcement learning turned upside down. I mean that as an analogy about specification; I am not claiming these are the same algorithm. The usual reinforcement-learning picture asks us to define a reward and then discover behavior that earns it. Here I can begin with something much less respectable:

> Make this explanation less intimidating.
> Help the learner understand why the merge matters.
> I want somebody to *feel* why divide-and-conquer helps rather than merely watch the algorithm execute.

Those are descriptions of a direction. None of them is a reward function, yet the model can produce an attempt from them, and the attempt can teach me whether the direction was what I really wanted.

I began the project insisting on an *interactive* Merge Sort demo. Interactivity sounded obviously desirable. Then I saw versions with buttons, sliders and enough learner participation to qualify as a small democracy, while one quieter version explained the central idea much better. Apparently clicking things was never the objective. Later the demos became good at showing recursive splitting and I realized they were treating merging almost as cleanup, so the objective moved again.

Recognition arrives before specification in a lot of creative work. We know a terrible design when we see one before we can write a complete theory of what would make it good. AI makes it cheap to see one.

But “make this intuitive for a beginner” hides almost everything interesting, starting with which beginner.

## Borrow a Mind

When I look at a Merge Sort demo, I am hopefully not testing whether *I* understand Merge Sort. The difficulty is seeing it from the position of somebody who does not know what I know.

Expertise makes this harder. Once recursion has settled into your head, you forget how strange it once looked that a function could call itself. Even the vocabulary stops sounding technical. Good teachers develop an instinct for where people stumble and which innocent sentence assumes three things the learner has not yet learned. I do not have that instinct for every person or every subject, so I started borrowing another mind.

For one of the demos, I asked Claude to approach the application as somebody who understood arrays and loops but had never encountered recursion. “Act like a beginner” tends to produce a theatrical beginner who is mysteriously confused by everything, so I gave it a knowledge boundary instead.

Its reaction was roughly: I can see that the array keeps getting divided into smaller pieces, but I do not understand why that helps. It feels as though we are making the problem more complicated. Where is the payoff?

That was useful because the demo really did have that problem. We had made recursion visible. From my position, that looked like progress. From the learner’s imagined position, we had merely made a mysterious operation easier to watch.

Cognitive scientists use *Theory of Mind* for our ability to reason about mental states other than our own: what somebody knows, believes, wants or misunderstands. The other person may not simply know less; they may have a different model of what is happening.

Instead of saying “you are a beginner,” I can specify the mind I want to borrow:

> You understand arrays, loops and functions. You have never encountered recursion. Use the demo from the beginning and tell me where the explanation first requires an idea you do not yet have.

Or:

> You understand recursion but have never seen Merge Sort. Tell me when you first understand why dividing the array makes sorting easier.

Those are different evaluators because they are positioned to notice different things. The same move works outside education. A customer may know exactly what jacket they want without knowing the vocabulary our catalog uses. A reader can have followed this book perfectly well without having lived inside its conceptual structure for months.

This is cheap perspective-taking, and also a cheap way to fool yourself.

The confused student is not confused. Claude has not spent twenty minutes failing to understand recursion while everybody else in the classroom moves ahead. It is generating a plausible model of how such a person might react, and that model can expose a blind spot. I use borrowed minds the way I would use a sharp colleague’s guess about users: as a source of criticisms and hypotheses worth checking with the people themselves.

## Independent Evaluators

At some point generating another opinion stops helping. Some artifacts have to survive and others have to disappear.

The metric problem returns here in a more dangerous form. A rubric can make judgment explicit, which is useful. It can also become the target the builder learns to satisfy.

If the evaluator repeatedly rewards step-by-step explanation, explanations grow. If it likes polished onboarding, everything begins to look like onboarding. If familiar visual conventions read as “clear,” unusual approaches may disappear before they have time to become good.

OpenAI’s CoastRunners experiment is the cartoon version of the problem: the agent learned to collect reward by driving in a loop instead of finishing the boat race. It is Goodhart’s Law with a speedboat. A language-model builder does not need such an obvious loophole. It can learn the style of artifact that another language model tends to reward, and making the evaluator more elaborate may simply create a more elaborate thing to game.

One improvement was surprisingly mundane: stop pretending we were good at absolute scores.

I can drink a coffee and have almost no meaningful answer to “How good is this from one to ten?” Give me two cups and ask which I prefer, and the problem becomes easier. If I still cannot decide, the scientifically responsible procedure is presumably to finish both.

The same thing happened with the demos. “Give this interface a pedagogical score from 1 to 10” produced suspiciously precise numbers attached to explanations of why the number should not be taken too seriously. Showing two artifacts and asking, “Which one would you rather give to somebody encountering Merge Sort for the first time, and why?” worked better.

Relative judgment asks less of the evaluator. It does not require a stable internal unit called one pedagogy point. With many candidates, a model such as Bradley–Terry can infer an ordering from a subset of pairwise preferences. More important for the next generation, the explanation for each preference can survive alongside the ranking. A tidy ranking can preserve every shared bias in the judgments behind it.

So I stopped asking one evaluator to represent everybody. A learner can inspect the artifact from the knowledge boundary we developed above. A teacher can focus on explanatory sequence. Another evaluator can look for cognitive load or accessibility. A domain expert can make sure our elegant simplification has not become false.

I call these independent evaluators, though the important word is *independent*.

Five copies of the same model given the same context and asked to wear five hats may still share almost every important blind spot. If all of them read the leading builder’s explanation of why its design is brilliant before inspecting the artifact, disagreement becomes less likely for reasons that have little to do with brilliance.

Sometimes the judges should see different things. The beginner should use the artifact before reading the builder’s explanation. A critic looking for conceptual errors does not need three paragraphs explaining why the choice was clever. The usability evaluator does not need to know which branch is currently winning. The rule I ended up with was to keep enough separation between judges that their disagreement still means something.

There is a difference between telling the builder:

> Learners repeatedly lost track of which subarray corresponded to which branch of the tree.

and telling it:

> The evaluator awards two extra points when every tree node has the same color as its corresponding subarray.

The first communicates a problem; the second communicates the test.

References helped with another problem: drift. “This is excellent” means something different if the evaluator has seen only the last four generations of our own work. For these demos I could give it examples from Distill, 3Blue1Brown or Jay Alammar to calibrate the level of clarity and finish we were aiming at. The references were there to answer *how good?* I did not want them answering *what should this become?* Calibrate too strongly against one aesthetic and every road leads to Distill.

And the judge should use the thing. An early mistake was evaluating applications by reading their code or screenshots. A browser agent can click through the demo, resize the page, try controls in the wrong order, notice that an explanation appears after the moment when it would have helped, or discover that the beautiful button everybody admired does absolutely nothing.

I used to call the browser ground truth, which was too generous. It lets the evaluator use the artifact and record what happened during the interaction. That can reveal a broken control or a confusing sequence. Whether a human learned Merge Sort still has to be checked with human learners.

The danger in a fully automated loop is that simulated evidence quietly replaces the expensive kind. Everything inside the machine agrees, the browser works, the ranking improves, and the loop congratulates itself.

The student has not yet been asked.

At some point I looked at what we had assembled and realized that *evaluator* no longer described it particularly well. It looked like a tiny institution, and institutions can become spectacularly efficient at measuring what doesn’t matter.

Humans face the same difficulty. One person’s judgment is useful and fallible. So we compare work, preserve disagreement, create standards, ask specialists to inspect different aspects, reproduce results, and occasionally discover that an entire professional community has become extremely sophisticated about the wrong thing.

Brian Cantwell Smith argues that what machines lack is judgment as opposed to mere reckoning: the capacity to be answerable to the world, to care whether the answer is right rather than merely well formed. He makes the argument carefully, and I think it is half right. What the machine lacks is real. But judgment, in the cases where humans exercise it well, was never a private faculty either. It is a person plus a tradition, plus other people positioned to object, plus consequences that arrive whether or not anyone wants them. When I stopped looking for judgment inside the evaluator and started building it between evaluators, the problem did not disappear. It turned into an engineering problem, which is the kind I know how to have.

And that made the remaining human job painfully obvious. I still decided when to research, when to build, which branches stayed isolated, whether a strange direction deserved another generation, which disagreement mattered, when to retrieve another example, and when the simulations had reached the point where only a real person could answer the question. I had automated much of the work, but I was still running the inquiry.

Adding another builder or another critic wouldn’t fix that. Somebody still had to decide which kind of move the inquiry needed next, and so far that somebody was me.

## Deep Mode

So I tried giving that job to an orchestrator. By now the system had a respectable vocabulary of moves, but there was no reason every problem should use them in the same order.

Research first may be sensible for one task and destructive for another because it anchors every branch before anything original appears. Five builders may reveal useful diversity or reproduce one mistake five times. Evaluator disagreement may justify another experiment, or one evaluator may simply be confused. A visual mockup may deserve implementation, or it may already have revealed enough to kill the idea cheaply.

A fixed Planner → Builder → Critic → Revise loop can be useful. It also answers all of those questions in advance. I wanted some of the workflow to remain inside the search.

We gave the orchestrator the problem, the capabilities available to it, and enough of the search history to decide what kind of move made sense next. Everyone else kept their jobs: builders built, researchers researched, evaluators judged, and the browser agents, visual systems and retrieval did what they had been doing. The orchestrator didn’t need to be the best at any of it.

At the top, the loop was almost too simple to write down:

**state of inquiry → choose a move → act → observe → update the state of inquiry**

The move itself was not fixed. Suppose two Merge Sort branches both make recursive decomposition clear, but evaluators keep reporting that learners lose track of how the tree corresponds to the array. The next move does not have to be “revise again.” The orchestrator can send a researcher after coordinated representations. Retrieval can surface an old prototype with a useful identity-preserving color scheme. A visual model can produce two spatial arrangements before anyone writes code. Builders can implement both. The browser may then reveal that one design requires the learner to look in two places at once precisely when the merge begins.

Nothing in that sequence is especially magical. We simply did not have to decide the sequence before the inquiry began. Otherwise Deep Mode would be a larger workflow diagram containing more rectangles.

Deep Mode makes no claim to be a universal problem-solving procedure. It gives the system a vocabulary of moves and lets the history of the inquiry influence which one comes next. In circle packing, the agent could change its search strategy. Here it could also change which kinds of work were brought together to judge and improve the result.

## Bars Moved Around

The first Merge Sort demos were exactly what you would expect. Bars moved around. Numbers changed places. Everything sorted correctly. If you already understood Merge Sort, you could follow them. If you did not, they mostly provided animated evidence that a computer was performing an algorithm.

There was no single diagonal-layering moment here, and I do not want to manufacture one for the sake of the story. The progress was distributed.

Some versions explained every step so carefully that the explanation became harder to follow than Merge Sort. Others became beautifully minimal and stopped teaching anything. The useful pieces did not always live in the strongest overall artifact: a visual relationship could survive after the application that introduced it was discarded. We were learning what to keep, sometimes from attempts we had every other reason to kill.

Count-Min Sketch followed a different path. The first versions looked like the data structure itself, grids with changing counters, technically correct and pedagogically opaque.

As the work continued, the designs increasingly organized themselves around the conceptual difficulties instead of the structure of the implementation. Collisions became visible. The learner could watch approximation happen instead of only reading about it. The relationship between memory and accuracy became part of the experience.

Whether the demos teach humans any better is a question only human learners can answer. What they showed me was that more of the work I normally performed in the vibe coder’s seat could move into the system without first reducing creative problem solving to one fixed workflow.

And that success exposed the harder problem. At higher levels of abstraction, failure can become coherent.

## A Cathedral on a Shopping Cart

Suppose the research agent reports that beginners understand recursion better when shown a tree. A visual model proposes a tree-based explanation. A coding agent builds it. A simulated beginner prefers it. Two evaluators agree, so the orchestrator allocates another generation to that lineage.

This looks exactly like the compound intelligence we wanted. Now ask where the first claim came from.

It might have been a controlled educational study, or one teacher’s opinion, or something the research agent inferred from a handful of examples. Five articles might repeat it only because all five cite the same source. The study, if there was one, might have tested university students, and our demo is for children.

Those are large differences, and everything downstream can still be perfectly competent. The research is wrong. The design responds intelligently to the wrong research. The implementation is flawless. The evaluators agree. The orchestrator invests another generation.

Nothing crashes.

You can build a beautiful chain of reasoning on one stupid assumption near the bottom, like a cathedral built on a shopping cart. As the components get better at producing coherent outputs, the original mistake may get harder to see.

Software architecture gets away with abstraction because layers expose contracts. When I query a database, I do not inspect the disk. When I add two integers in Python, I do not check the CPU. I rely on interfaces whose behavior is stable enough that the details can disappear most of the time.

A cognitive architecture needs contracts too, but types and APIs are not enough. A research result, browser observation, evaluator preference, remembered failure and inherited design pattern should not enter the orchestrator’s context as five equally credible paragraphs.

Each of them needs to arrive with its history attached: where it came from, what was observed and what was only inferred, which parts anyone checked and what is still uncertain. An evaluator’s preference should say whose perspective it came from. An old lesson should say how often it has survived, and where.

Humans ran into this long before AI. We keep records, ask where a claim came from, seek another opinion and learn which people to consult about which problems. Much of what I know depends on work I could not personally repeat.

These arrangements are imperfect. They sometimes preserve error and reward conformity, and sometimes the shopping cart survives the review. Their purpose is to let fallible people build on one another while preserving some structure around why a claim deserves trust.

Once cognition becomes distributed, the same questions become engineering questions: provenance, independence, replication, disagreement, authority.

I had started the chapter trying to get myself out of the vibe coder’s seat. By automating more of the work there, I had ended up somewhere I did not expect. The question had moved from whether the agents were capable enough to whether the things they believed deserved to be believed.

How do you know what to trust?

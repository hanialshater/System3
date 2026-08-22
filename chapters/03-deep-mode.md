# Chapter 3: Deep Mode
 
*Beyond Algorithms: Agent Autonomy for Creative Problems*
 
In the previous chapter, we gave agents a difficult algorithmic problem and a lot of autonomy. The result was surprisingly good. The agent researched strategies, tried several approaches, got stuck, changed direction, and eventually found diagonal layering.
 
But circle packing had one enormous advantage that I didn’t appreciate enough at the beginning: we knew exactly what good meant.
 
There was an Immutable Harness. You ran a solution and got a number. Circles overlapped or they didn’t; the score improved or it didn’t. The agent could spend an hour pursuing some bizarre geometric idea and I didn’t have to sit beside it wondering whether version seventeen had more soul. We just ran the evaluator.
 
Most of the things I actually want AI to help me with aren’t like that.
 
“Is this explanation pedagogically effective?” doesn’t have a unit test, and “Would a confused student understand this visualization?” can’t be settled with an `assert`. Two competent people can look at the same design, disagree completely, then switch sides five minutes later after using it. The feedback is subjective, noisy, sometimes contradictory, and often becomes clearer only after you have built the thing you were supposedly trying to specify beforehand.
 
I picked educational demos for Merge Sort and Count-Min Sketch because they were still bounded—you can actually finish one before civilization collapses—but they live on the messier side of the boundary. You have to decide what to explain, what to leave out, how the interaction should work, how much should be visible at once, and what another person is likely to understand from any of it.
 
The ambition was intentionally high. I wanted something closer to the best Distill articles or Jay Alammar’s visual explanations than to the usual “here are some bars moving around; congratulations, you have learned sorting.” Those demos take a surprising amount of thought. The algorithm itself is usually the easy part. The difficult part is deciding what to show, when to show it, and what representation might make an idea suddenly click.
 
Circle packing let the search be complicated because judgment was simple.
 
Here judgment had become part of the problem.
 
The experiment that eventually became **Deep Mode** was an attempt to push autonomy one level higher. Instead of giving an agent freedom only over implementation, could we give a system some freedom over the inquiry itself—whether the next useful move was to build, research, branch, retrieve, compare, change perspective, or abandon a direction entirely?
 
To understand why that seemed like the next step, it helps to see how much of the work around the model had already moved inside the machine.
 
## How We Got Here
 
Coding first appeared as a strange side effect of language modeling.
 
Once large language models became good enough to produce useful code, the first tasks were conveniently small. Give the model a function signature, a comment, or a programming problem and ask it to fill in the implementation. Benchmarks such as HumanEval and APPS made this measurable: could a model turn a specification into a program that survived tests?
 
Then tools such as GitHub Copilot put that capability directly inside the editor. Instead of asking a chatbot for code and carrying the answer back yourself, you could write the beginning of a function or describe what should happen next and watch several lines appear underneath it.
 
This was useful enough that the limitations became interesting.
 
A real software task rarely arrives as an isolated function with a docstring politely explaining what needs to change. Someone says invoices occasionally show the wrong tax after a refund. Somewhere inside a 150,000-line CRM there is a reason. It may involve a controller, a database model, an old helper function, a test written three years ago, and an API whose behavior everyone on the team knows but nobody thought to document.
 
By the time GPT-4 arrived, I increasingly wanted to use models on exactly these problems. The workflow was ridiculous.
 
You found the file you suspected, copied a class or function into ChatGPT, described the bug and waited for a suggestion. Then you copied the patch into the editor, ran the program, discovered a new error, copied the traceback, pasted that back into ChatGPT, and started another round.
 
The first tool was copy and paste.
 
For a while, the whole architecture looked roughly like this:
 
`repository → copy code → model → copy answer → editor → run tests → copy error → model`
 
The model might be doing sophisticated reasoning in the middle, but the human performed every interaction with the software around it. You searched the repository, decided which file mattered, assembled the context, applied the edit, ran the tests, and carried back whatever reality had said about the edit.
 
For a small function, this still felt magical. Then the bug crossed three files and you acquired a second job: preparing the model’s world.
 
You paste one class but forget the interface it implements. The model confidently invents a method that does not exist. So you paste the interface. Now it needs the database schema. Then another class. Eventually half the repository is sitting in the conversation and somehow the model understands less.
 
A lot of early LLM programming consisted of building a tiny artificial universe around the model: here is the relevant class; here is the schema; please ignore these twelve methods; this function looks important but isn’t; that innocent-looking helper controls payments, so please don’t touch it unless you enjoy incident calls.
 
We eventually learned an obvious lesson that took surprisingly long to learn: more context and better context are different things. If somebody asks for a spoon, emptying the entire kitchen onto the table does not necessarily help.
 
Even with excellent context, though, I was still doing everything that connected the model’s reasoning to the program.
 
I had effectively become its eyes, hands and terminal.
 
Software-engineering benchmarks began exposing the same gap. HumanEval and APPS had asked whether a model could write code once the problem was already packaged for it. SWE-bench changed the unit of evaluation. Its tasks came from real GitHub issues. Now a system had to work inside an existing repository, find the relevant code, understand relationships across files, make an appropriate change and survive the tests.
 
The early results were bad enough to be useful. A model could know perfectly well how to write Python and still fail because it looked in the wrong file, misunderstood the repository, changed the wrong abstraction, or never used the test result to reconsider its first theory.
 
The next engineering move was almost embarrassingly straightforward: move the copy-paste loop inside the machine.
 
Give the model access to the repository. Let it search for symbols and references instead of waiting for us to paste them. Let it open files, edit them and inspect the diff. Give it a terminal so it can run tests itself. When a test fails, return the failure and let that result shape what happens next.
 
The simplest coding agent is essentially this loop made executable. The language model supplies much of the programming knowledge and reasoning; the surrounding environment lets it inspect software, act on it and observe the consequences.
 
Software is an unusually friendly world for this. Files can be searched. Programs can be executed. Tests can say no. Git can tell you exactly what changed and, if an experiment becomes sufficiently exciting, take you back to the time before you had the idea.
 
Systems such as SWE-agent made the importance of the interface explicit. Apparently mundane choices—how the model searches, how much of a file it sees, how edits are applied, what information comes back from commands—can make a large difference. The useful object is no longer just the model. It is the model operating inside a world where software can push back.
 
Naturally, giving the model a computer exposed several new problems.
 
Early coding agents could behave like interns with root access and too much coffee. Ask one to change a line and it might rewrite half the file. Ask it to fix a button and twenty minutes later it has developed strong opinions about the database architecture. It would find one plausible explanation for a bug, follow it for too long, then use every new piece of evidence to improve the explanation instead of admitting the explanation was wrong.
 
So the interface became more careful. Agents got better ways to make small patches, inspect diffs, run targeted tests, checkpoint work and undo experiments. Planning helped when a task was too large to attack in one edit.
 
Then we discovered that the agent kept forgetting things we had already taught it.
 
Every real repository contains knowledge that is obvious to the people who work there and invisible to a general model. Authentication happens in a particular way. The team has conventions. One ancient API looks wrong but absolutely must remain wrong because six other services depend on its wrongness.
 
You explain this on Monday, then again on Tuesday, and by Wednesday you begin to suspect that you are the memory module.
 
So some of that knowledge moved into the environment too: `CLAUDE.md`, `AGENTS.md`, repository instructions, rules files, skills. The names vary, but the idea is simple. If somebody has already learned something expensive about this codebase, leave it somewhere the next agent can find it.
 
Longer sessions produced almost the opposite problem. Context slowly filled with abandoned experiments, obsolete assumptions, test output from forty minutes ago and debugging paths that stopped mattering three hypotheses back. Technically the model had more information. Practically it began behaving as if somebody had emptied a filing cabinet onto its desk and mentioned that one of the pages might contain the launch codes.
 
Memory became a problem of selection rather than storage.
 
And then there was history.
 
A long-running agent tends to acquire loyalty to its own decisions. Suppose it decides early that our Merge Sort demo should use React and a recursion tree. It spends forty minutes building that version. Every later question now arrives in a context containing forty minutes of reasons, code and decisions supporting React and a recursion tree.
 
Humans call our version of this sunk cost.
 
The agent has a respectable excuse: its context window is literally full of evidence that this is what the project is.
 
So we started giving different attempts different histories. One agent tries the tree. Another begins with the array. Another starts from the learner’s misconception rather than from either representation. A fresh branch does not have to spend half its intelligence escaping the assumptions accumulated by the previous one.
 
Looking backward, the progression is less mysterious than the word *agent* sometimes makes it sound. We began with models that could generate useful pieces of code. We put them in editors. Then repository access, editing and execution moved into the system itself. Better interfaces, memory, context management and branching followed.
 
Bit by bit, work the human had been doing around the model became part of the machine.
 
But there was still a large difference between an agent that could work competently on software and the thing I increasingly wanted to ask for:
 
Build the application.
 
## From the Repository to the App
 
Once coding agents became reasonably comfortable inside repositories, I started noticing something slightly absurd about how we were using them.
 
Suppose I want to build a small booking application for a football academy. Parents should see available sessions, pick one, enter their details, perhaps pay, and receive a confirmation. There is nothing technically exotic here. A competent coding agent can build the whole thing.
 
Give it an empty directory, though, and watch what happens.
 
First it creates a project and chooses a framework. Then it installs packages, lays out the frontend, creates a database, decides how authentication should work, wires the database to the application, manages environment variables, configures hosting, adds deployment files, and eventually discovers that two perfectly respectable libraries disagree about some dependency for reasons documented across fourteen GitHub comments and one furious blog post.
 
Several minutes later, we have made enormous progress toward having somewhere to put the booking form.
 
This is real engineering work. Somebody has to do it. But once an agent can reconstruct roughly the same plumbing every time, another question becomes obvious: why are we asking it to?
 
Authentication is not identical across products, but most small applications do not need a new philosophy of authentication. The same is true of databases, routing, components, deployment, secrets, build systems and dozens of other choices sitting underneath the thing somebody actually wanted.
 
The booking application does not become more original because the agent spent twenty minutes reconsidering whether PostgreSQL has finally had its day.
 
Sometimes the right answer is simply to prepare more of the world in advance.
 
This is why systems such as Replit and Lovable became interesting to me. They give the model a more opinionated place to work. Runtime, deployment and common application machinery are already nearby. Instead of beginning with an empty computer and reconstructing web development, the conversation can begin much closer to the application.
 
You can say:
 
Build a booking system for a football academy. Parents should see available sessions and book one.
 
A first version appears. You look at it and realize that the schedule should probably be on the home page. Requiring people to create an account before they can even see a session feels ridiculous, so login moves later. The mobile page is cramped. The photo of the suspiciously muscular child kicking a football may be setting unrealistic expectations for the under-sevens, so perhaps that goes too.
 
Somewhere underneath the page there is still React or something like it. There is still a database, network requests, authentication, configuration, hosting, CSS and the usual collection of tiny disasters waiting patiently for production. But those things are no longer the subject of every conversation.
 
The environment has opinions about them already.
 
I think of this as a smart template, although *template* makes it sound more rigid than I mean. An old template gave you a restaurant website with a hero image and somewhere to replace somebody else’s logo. A smart template is more like a prepared workshop. Common tools are already on the wall and common jobs have sensible defaults, but the agent can still change them when the job requires it.
 
There is an obvious trade-off. Give an agent Bash and an empty machine and almost nothing has been decided for it. Put the same agent inside a prepared application environment and some possibilities disappear.
 
That sounds like a loss of intelligence until you think about how humans work.
 
A chef does not begin dinner by manufacturing a knife. A scientist does not usually build a new operating system before analyzing data. When I open Python, I accept an astonishing number of decisions made by people I will never meet because reconsidering all of them would make writing `print("hello")` a multigenerational project.
 
Useful abstractions remove decisions whose answers are no longer interesting most of the time.
 
And after enough of those decisions disappear, something else becomes easier to see.
 
Suppose the booking app works perfectly. The database is connected, deployment succeeds, the buttons behave, the mobile layout is respectable, and nobody has accidentally built a cryptocurrency exchange in the authentication service.
 
I open the application and think: this isn’t very good.
 
The software works.
 
Now I have to worry about the football academy.
 
## The Problem-Solving Layer
 
Should parents see every available session, or only the ones appropriate for their child? Should they have to create an account before booking? What happens when somebody has three children? How late can they cancel? Should we show that only two places remain, or does that create unnecessary pressure? If the academy has empty sessions on Wednesday and a waiting list on Saturday, is the booking interface part of that problem?
 
None of these questions is really about React.
 
They were always there. Software teams have always argued about customers, flows, business rules and what the product should do. But implementation used to consume enough attention that it was easy to mix two different problems together: deciding what should exist and turning that decision into software.
 
When another version becomes cheap, the balance changes. You can see the idea sooner, and seeing it gives you information you did not have while discussing it.
 
Perhaps we decide that customers should create an account before seeing availability. It sounds reasonable: we need their details eventually. Then we build it and the experience immediately feels annoying. Parents arriving from a Google search do not want to establish a lifelong digital relationship with a football academy before discovering whether Saturday at ten is available.
 
So login moves later.
 
The artifact is no longer merely the end of the thinking process.
 
It becomes something we think with.
 
The Merge Sort demo made this even clearer because there was almost no business machinery to hide behind. I could ask an agent to build an interactive explanation and receive something perfectly functional: an array of bars, controls, animation, perhaps some text explaining that the algorithm divides the input and merges the pieces again.
 
Technically, it was fine. Pedagogically, it could still be terrible.
 
Watching bars move does not necessarily tell a beginner why dividing the problem helps. So perhaps we try a recursion tree. The tree makes the structure visible, but now the supposedly simple sorting algorithm resembles the organizational chart of a German corporation. Maybe we show the tree and array together. Perhaps that creates too much cognitive load. Maybe the problem is not the representation at all; the learner understands splitting perfectly well but has no idea why merging makes the whole trick useful.
 
There is no compiler error that tells me which diagnosis is right.
 
I have to look at what we built, form an opinion about why it fails, and decide what would teach us something next. Sometimes that means improving the current version. Sometimes it means building a deliberately different one. Sometimes I need research. Sometimes the right move is to put the application in front of somebody who does not already understand Merge Sort.
 
Occasionally I discover that the question I started with was wrong.
 
“Build an interactive Merge Sort demo” sounds like a goal until you see several interactive Merge Sort demos. Perhaps what I actually care about is getting someone who has never encountered divide-and-conquer to understand why breaking one difficult problem into smaller ones makes the problem easier. Once I realize that, interactivity is merely one possible means.
 
This is the **problem-solving layer**: the work of deciding what to try, which evidence matters, whether a result failed because of its implementation or its underlying idea, and what kind of attempt might teach us something next.
 
The lower layers help us build the artifact.
 
Layer 3 decides what to try next in service of its purpose.
 
## The Five Layers of AI Coding
 
By now I had a rough map.
 
**Layer 0 — Model.** GPT, Claude, Gemini and whatever comes next: general capability in language, code, reasoning and vision.
 
**Layer 1 — Agent.** Put the model in an environment where it can act. Claude Code, Codex and similar systems search repositories, edit files, execute commands and react to results.
 
**Layer 2 — Application.** Replit, Lovable and similar environments prepare more of the software world in advance, allowing the conversation to stay closer to the application.
 
**Layer 3 — Problem Solving.** Decide what to try, why something failed, which evidence matters, and whether the current direction deserves another iteration.
 
And above that sits the problem I have mostly been avoiding.
 
**Layer 4 — Intention.** What do we actually want?
 
Software likes that question to have been answered before the work begins, preferably in Jira, where the answer can remain wrong in a structured and searchable format. Real goals are less cooperative. Seeing a solution can change what I realize I wanted.
 
That problem is much bigger than AI coding, and I am going to leave it alone for now.
 
The borders are fuzzy. Figma can generate code. Coding agents make product decisions. Tomorrow’s products will rearrange the stack again. The useful distinction is the kind of decision being made, not which company happens to occupy which box.
 
People often call the experience of working this way *vibe coding*. I will use **AI coding** for the broader stack, but *vibe coder* remains a wonderfully accurate name for the human sitting near Layer 3: looking at what came back, deciding what feels wrong, asking for another direction, killing one idea, keeping part of another, and steering the whole process without having an algorithm for how.
 
The first three layers increasingly answer a version of the same question: *how do we make this?*
 
Layer 3 asks a different one:
 
*Given everything we have learned so far, what should we try next?*
 
That was the part I still seemed to be doing manually. So I watched what I was actually doing in that seat.
 
There was no universal workflow hiding there. A mathematician, a designer and a product manager can all spend a day solving hard problems while performing almost none of the same visible actions.
 
But the same kinds of moves kept appearing.
 
## In the Vibe Coder’s Seat
 
I began to think of these less as stages in a workflow than as a vocabulary.
 
Sometimes I needed another attempt. Sometimes I needed information. Sometimes the search had become too narrow. Sometimes the representation itself was constraining what we could imagine. Sometimes the objective needed to change. Sometimes I needed to see the artifact from another mind.
 
The important point was that these moves were not useful in a fixed order.
 
### Beat the Complexity Wall — Code Evolution
 
The first problem was simply the number of possibilities.
 
Even a Merge Sort demo has an absurd design space. Bars or cards? Numbers or a tree? Continuous animation or learner-controlled steps? Does color represent recursion depth, identity, or the active subproblem? Explain before the animation, during it, or afterward? Every choice changes the usefulness of several others.
 
When implementation was expensive, we dealt with much of this complexity by trying to decide more before building. AI coding changes the economics. If another implementation costs minutes rather than days, I do not have to choose quite so much in advance.
 
Chapter 2 had already shown what to do with a search space too large to reason through directly. One hill climber inherits its own history; evolutionary search maintains alternatives.
 
The same move works here, except that what evolves is no longer just a vector of parameters or even an algorithm.
 
It can be an **idea embodied in software**.
 
One builder tries a recursion tree. Another focuses on the array. A third begins from the learner’s misconception. Mutations can be conceptual: remove the text, teach backward, make the learner predict, show synchronized representations, abandon interaction altogether.
 
Useful pieces can move between them. One terrible demo may have a beautiful color mapping. Another may explain the merge clearly while making everything else unbearable. The final artifact does not have to inherit the entire history of either one.
 
The only thing I have to protect is enough independence for the alternatives to become genuinely different. If every branch sees the current winner and its full history, parallelism quickly collapses into several agents improving the same idea. Sometimes I withhold the leading implementation; sometimes I frame branches differently and let them develop before sharing what worked.
 
There is a cost. Diversity burns compute, duplicates effort and sometimes produces five independent rediscoveries of the same bad idea. Parallelism is not automatically intelligence.
 
Still, cheap code changes where that trade-off sits. Competing ideas can become executable before commitment makes one of them expensive to abandon.
 
The waste appears elsewhere: if every branch starts ignorant, we spend a great deal of compute rediscovering things other people already learned.
 
### Survey the Territory — AI Research
 
People have been teaching recursion for decades. There are textbooks, lecture notes, visualizations, papers, classroom experiments and a great deal of trial and error sitting on the internet.
 
Before I spend another afternoon inventing my fourth way of moving colored rectangles around, I probably want to know what is already there.
 
This is where AI research became useful.
 
I can ask an agent a broad question: How do people teach Merge Sort well? Where do learners get confused? Which visual approaches have been tried? What evidence exists? Where do approaches disagree?
 
Increasingly the agent can do more than read. If an interesting prior attempt is an interactive tutorial, a written description is a poor substitute. With computer use it can open the artifact, step through it, see what remains visible, notice who controls the pace, and compare it with another implementation. Some design knowledge lives more clearly in the artifact than in what its creator wrote about it.
 
Research can also follow the work rather than precede it.
 
Suppose I build a recursion tree and discover that recursion itself is not the problem; the learner is losing the relationship between the tree and the changing array. Now I have a better research question: how have other systems coordinated two representations without requiring people to watch half the screen at once?
 
Research becomes another move in the investigation rather than a phase performed before building.
 
But research has its own failure mode: anchoring.
 
Give every builder the same ten polished Merge Sort demos and version eleven tends to resemble its grandparents. Sometimes I want the researcher to bring back the problem, the evidence and the failures while leaving a few fresh branches to invent their own response.
 
There is no prize for independently rediscovering a good idea. There is also no virtue in making every search begin with the same answer.
 
Research gives us more material. Soon the problem reverses: there is too much of it.
 
### Find the Right Context — Retrieval
 
Suppose the branch I am working on now keeps losing the connection between the recursion tree and the array.
 
Somewhere in our growing mess we have research notes, screenshots, evaluator comments, old branches, perhaps a paper on coordinated representations, and a discarded prototype whose only good idea was a color mapping that solved exactly this problem.
 
I do not need the whole research archive.
 
I need the thing that helps with this decision.
 
Sometimes ordinary search is the best tool. If I remember the phrase *coordinated representations*, an author, an API, or an evaluator comment containing “lost track,” exact words are useful evidence rather than a primitive technology we should be embarrassed to use.
 
Embeddings help when I remember the idea rather than the words. “Keeping identity stable while the representation changes” may retrieve a note that never used that phrase, or an example from another domain that solved the same structural problem.
 
Long documents create another choice. Cutting everything into chunks and retrieving by embedding similarity works remarkably well, but a book or research report already has structure. If I know the question concerns evaluation, it can be more sensible to navigate chapters, sections and pages, then read the relevant passage in context. Page- or structure-based retrieval preserves relationships that disappear when every paragraph is treated as an independent fragment.
 
In practice I want all of these. Search broadly, rerank candidates when necessary, open the surrounding section, follow a reference, then search again if what I found changes the question. Good coding agents already work this way inside repositories. They do not retrieve the repository once; they navigate it.
 
At Layer 3 the environment is stranger because the retrievable object may be a screenshot, an old interaction, a research result, evaluator feedback, code, or a dead branch that suddenly contains something useful.
 
That last case matters after code evolution. Killing a lineage does not have to erase it. A branch that lost globally may still contain a stepping stone worth returning to later.
 
Retrieval therefore does more than find semantically similar things. It constructs the local working context of an investigation.
 
And context is not merely what we include.
 
A branch polishing the current winner should probably inherit a great deal. A branch sent out to challenge it may not need to begin by studying the winner in detail.
 
Sometimes the useful context has a hole in it on purpose.
 
That helps preserve alternatives. It does not yet stop those alternatives from drifting toward the same familiar region anyway.
 
### Push the Creative Horizon — Exploration
 
After several rounds of code evolution, something slightly embarrassing happened.
 
The builders were exploring.
 
They also kept giving me bars.
 
Better bars, admittedly. Some split gracefully. Some changed color as recursion deepened. One branch added a tree. Another let the learner control the animation. Given enough generations, I had every reason to believe we would eventually produce the finest moving bars known to humanity.
 
It is tempting to treat creativity as the mysterious ingredient missing here. Reinforcement learning and evolutionary computation suggest a more practical diagnosis: search tends to spend its budget where progress is already visible.
 
Different methods attack different versions of that failure.
 
Monte Carlo Tree Search is useful when the future branches too quickly to explore everything. In Go, learned intuition can focus effort on promising moves without committing every resource to the move that currently looks best. AlphaGo made that combination famous.
 
But sometimes the problem is not choosing among branches; it is losing interesting places you already reached. Go-Explore addressed that failure by remembering promising states, returning to them, and exploring outward again.
 
That maps nicely onto software artifacts. A globally mediocre Merge Sort branch may contain one excellent interaction. Keep the state. A dead lineage can remain an archive of places worth revisiting when another idea gives them a new use.
 
Novelty search pushes against a different failure: the objective itself can pull every attempt toward the same deceptive region. Lehman and Stanley showed that on some problems, rewarding behavior for being different rather than for direct progress can eventually discover better solutions.
 
The important word is *some*.
 
Novelty is not quality. A sufficiently determined search can become wonderfully original and completely useless. But difference itself can sometimes deserve a budget.
 
MAP-Elites makes that intuition more structured. Instead of preserving only the global winner, retain strong solutions across different behavioral niches. At Layer 3, one niche might be highly interactive, another almost static, another organized around learner prediction. We do not have to know in advance which style contains the final answer in order to preserve several ways of being good.
 
POET makes one further move. If the environment keeps rewarding the same behavior, evolve the environment too.
 
For a creative problem, that can be surprisingly literal.
 
Teach Merge Sort without explanatory text. Require the learner to predict before anything moves. Make it work on a phone with room for only one representation. Design it for somebody who understands loops but finds recursion suspicious.
 
I had already started calling these **Strategic Constraints**. The exploration literature gives a less mystical explanation for why they sometimes work: a constraint changes which parts of the search are reachable and can stop a familiar attractor from absorbing every attempt.
 
“No bars” is not a profound theory of creativity.
 
It is an intervention on the search.
 
Most arbitrary constraints are merely arbitrary. The useful ones expose a neglected dimension, force a different representation, or remove an easy path that has become too dominant.
 
What makes AI coding particularly interesting is the richness of the available moves. In Go you place a stone. Here a move might be a code change, a different metaphor, a retrieved analogy, a fresh agent with no history, another evaluator, or a reformulation of the problem itself.
 
We already know a surprising amount about keeping search alive.
 
Language-model agents give those old ideas a much stranger space in which to operate.
 
And then I noticed that even this search was biased in a quieter way.
 
Most of our ideas still had to arrive as words.
 
### Think in Pictures — Visual Thinking
 
That is fine when I am working on an argument. It is less obviously sensible when I am designing an interface.
 
I can spend ten minutes explaining where the recursion tree should sit, what remains visible while the array splits, how colors should connect two representations and what the learner should notice first.
 
Then somebody draws it and I know within three seconds that the whole thing is terrible.
 
So I started generating the picture first.
 
The experiment was not sophisticated. I asked an image model to design an interactive tutorial for Merge Sort. Then Count-Min Sketch. Then A*. Then Poincaré embeddings in hyperbolic space, partly because if this still worked there I would have to take the idea seriously.
 
The details were not magically correct. Arrows occasionally pointed somewhere they had no business pointing, interactions made no computational sense, and generated text sometimes looked like somebody had tried to OCR a dream.
 
But the overall composition could be surprisingly thoughtful.
 
A Merge Sort mockup might keep the array visible while placing the recursion tree beside it, using color to preserve the relationship between a subarray and its node. A Count-Min Sketch design might make collisions visually central instead of leaving them as a detail in an equation. The model had to decide what was large, what was peripheral, where controls belonged and how the learner might move through the explanation.
 
I remember looking at some of these and thinking:
 
**Holy shit.**
 
Not because I wanted to ship the image. Usually I didn’t.
 
What surprised me was that I had given the model a concept in language and it had returned something like a spatial argument about how the concept might be taught.
 
After that I stopped treating image generation as the last stage—*the product is designed, now make it pretty*—and started using it while I was still trying to understand what the product could be.
 
A mockup is a cheap hypothesis.
 
Often most of it is disposable and one relationship is worth stealing.
 
Coding agents make this particularly useful. I can say: preserve this layout, keep the relationship between these two states, lose the giant header, and make the mathematics actually work. The coding agent turns the visual intuition into something executable, where the recursion tree cannot invent an extra branch because the composition looked nicer that way.
 
Figma, Claude Design and similar tools make the intermediate artifact richer still. We no longer need to jump straight from prose to code.
 
Pictures can hide problems too. A mockup may look wonderful because nobody has yet forced the interaction to make sense. Then we implement it and discover that the design depended on three impossible state transitions and a button whose purpose was apparently emotional.
 
Different representations expose different mistakes.
 
I do not need the stronger claim that the image model “understands pedagogy.” The practical point is enough: changing the representation changes what the search can discover.
 
And now we have a nice problem.
 
We can generate several genuinely different demos rather than five implementations of the first thing that occurred to us.
 
I still have to decide which one is better.
 
### Optimizing Something You Can’t Score
 
Circle packing was unusually kind to us. Once the geometry was valid, the evaluator could reduce the result to one number.
 
That number threw almost everything else away, which was precisely why it was useful.
 
A huge amount of machine learning rests on this trick. We take something complicated that we want and find a measurable signal that stands in for it. Reinforcement learning makes the relationship especially obvious: we do not specify every movement a robot should make while learning to walk; we construct a reward and let search discover the behavior.
 
The reward is doing an extraordinary amount of work. It is also where we hide an extraordinary amount of trouble.
 
Suppose I want the same convenience for educational design. I can make a rubric: correctness, pedagogical clarity, visual quality, interaction, accessibility, engagement. Give each a weight and suddenly my vague dissatisfaction with a demo has become a respectable decimal.
 
The decimal is comforting. The decisions required to produce it are less so.
 
Why should interaction receive fifteen percent? Is more interaction always better? What distinguishes a seven from an eight in pedagogy? Why those dimensions rather than whether the learner can predict what happens next or explain why the merge matters?
 
The metric forces me to commit to an idea of “good” before the search has taught me very much about the problem.
 
This is not an argument against metrics. If I care about latency, measure latency. If the code must pass a test, run the test. Hard measurements are wonderful when what we can measure is close to what we care about.
 
The trouble begins when a rich objective is still poorly understood and we compress it anyway because optimization wants a number.
 
That compression is also a surprisingly low-bandwidth way to communicate.
 
“Version B scored 7.4; version A scored 7.1” tells the next builder almost nothing about why B won. A rubric helps, but as I add enough dimensions, exceptions and qualifications to faithfully express what I mean, eventually I reinvent language badly.
 
Meanwhile I can simply say:
 
The recursion tree makes decomposition much clearer, but now the learner has to watch the tree and the array simultaneously. Keep the color mapping that preserves identity between them, simplify the tree, and make the merge feel like the payoff rather than cleanup at the end.
 
That contains comparison, diagnosis, trade-offs, priorities and a proposed next move in a few sentences.
 
Natural language is ridiculously rich compared with a scalar.
 
Language models make that human communication channel available inside the optimization loop. The model already carries learned structure behind words such as *simple*, *confusing*, *elegant*, *intuitive*, *busy* and *beginner-friendly*. Those meanings are imperfect, culturally loaded and sometimes wrong. But they carry much more structure than 7.4.
 
Natural language can therefore function as an **implicit metric**.
 
Not a metric in the strict mathematical sense. There is no guarantee that “intuitive” defines a stable ordering, and two evaluators may interpret it differently. But language can play some of the role a metric normally plays: it gives the search a direction, communicates why one attempt is preferred to another, and preserves trade-offs that a scalar would erase.
 
OPRO—Optimization by PROmpting—is interesting for a related reason.
 
In ordinary optimization, specifying the objective is only half the machinery; we also need some method for moving through the search space. In OPRO, an LLM sees the optimization problem, previous candidates and their outcomes, and proposes a better candidate. Much of the search heuristic is implicit in the model rather than programmed as a transformation rule.
 
That does not make OPRO the same thing as creative design. In the published OPRO setting, candidate quality can still be evaluated by an explicit score. But it demonstrates something useful: an LLM can use the history of an optimization process to propose the next point without us writing the search rule ourselves.
 
Now suppose the history contains more than scores.
 
Alongside hard measurements, I can tell the model what improved, what became worse, which trade-off appeared and what we should preserve. The history of the search can retain some of its meaning rather than collapsing into a column of numbers.
 
This begins to feel a little like reinforcement learning turned upside down.
 
I mean the inversion conceptually, not as a claim that these are the same algorithm. Decision Transformers, reinforcement learning and language-guided iteration are different mechanisms.
 
But look at the direction of specification.
 
The usual reinforcement-learning picture asks us to define a reward and then discover behavior that earns it.
 
Here I can begin with something much less respectable:
 
Make this explanation less intimidating.
 
Help the learner understand why the merge matters.
 
I want someone to feel why divide-and-conquer helps rather than merely watch the algorithm execute.
 
Those are descriptions of a direction, not reward functions.
 
Yet the model can produce an attempt from them, and the attempt can teach me whether the direction was what I really wanted.
 
I began the project insisting on an *interactive* Merge Sort demo. Interactivity sounded obviously desirable. Then I saw versions with buttons, sliders and enough learner participation to qualify as a small democracy, while one quieter version explained the central idea much better.
 
Apparently clicking things was never the objective.
 
Later the demos became good at showing recursive splitting and I realized they were treating merging almost as cleanup.
 
The objective moved again.
 
The search was doing something I normally associate with optimization in reverse: instead of starting from a fully specified reward and discovering the policy, I was using candidate policies—actual artifacts—to discover what the reward description should have been.
 
Recognition arrives long before specification in a lot of creative work. We know a terrible design when we see one before we can write the complete theory of what would make it good.
 
AI makes that loop cheap. The natural-language objective guides the search; artifacts make the objective concrete enough to argue with; the description changes and the search continues.
 
Ambiguity is not always a defect waiting to be engineered away. Sometimes we simply have not learned enough yet.
 
There is a catch, though.
 
Natural language may be high bandwidth, but somebody still has to interpret it.
 
If I say “make this intuitive for a beginner,” I have left almost everything interesting unstated.
 
Which beginner?
 
### Borrow a Mind — Theory of Mind
 
When I look at a Merge Sort demo, I am hopefully not testing whether *I* understand Merge Sort.
 
The difficulty is seeing it from the position of somebody who does not know what I know.
 
Expertise makes this harder. Once recursion has settled into your head, you forget how strange it once looked that a function could call itself. Even the vocabulary stops sounding technical.
 
Good teachers develop an instinct for this. They know where people usually stumble and which innocent sentence assumes three things the learner has not yet learned.
 
I do not have that instinct for every person or every subject, so I started borrowing another mind.
 
For one of the early demos, I asked Claude to approach the application as somebody who understood arrays and loops but had never encountered recursion. Not simply “act like a beginner,” which tends to produce a theatrical beginner who is mysteriously confused by everything.
 
I gave it a knowledge boundary.
 
Its reaction was roughly:
 
I can see that the array keeps getting divided into smaller pieces, but I don’t understand why that helps. It feels as though we’re making the problem more complicated. Where is the payoff?
 
That was useful because the demo really did have that problem.
 
We had made recursion visible. From my position, that looked like progress. From the learner’s imagined position, we had merely made a mysterious operation easier to watch.
 
Cognitive scientists use **Theory of Mind** for our ability to reason about mental states other than our own: what somebody knows, believes, wants or misunderstands. The other person may not simply know less. They may have a different model of what is happening.
 
Instead of:
 
You are a beginner.
 
I can specify the state of the mind I want to borrow:
 
You understand arrays, loops and functions. You have never encountered recursion. Use the demo from the beginning and tell me where the explanation first requires an idea you do not yet have.
 
Or:
 
You understand recursion but have never seen Merge Sort. Tell me when you first understand why dividing the array makes sorting easier.
 
Those are different evaluators because they are positioned to notice different things.
 
The same idea applies outside education. A customer may know exactly what jacket they want without knowing the vocabulary our catalog uses. A developer can be excellent at distributed systems and know nothing about the peculiar assumptions buried in our deployment process. A reader can have followed this book perfectly well without having lived inside its conceptual structure for months.
 
This is cheap perspective-taking.
 
It is also very easy to fool yourself with.
 
The confused student is not confused.
 
Claude has not spent twenty minutes failing to understand recursion while everybody else in the classroom moves ahead. It is generating a plausible model of how such a person might react.
 
That model can expose a blind spot. It is not synthetic user research.
 
I treat these borrowed minds as instruments for generating different criticisms and hypotheses, not as substitutes for the people they simulate.
 
By this point the system could generate alternatives, bring in outside knowledge, retrieve old ideas, reopen dead branches, force the search into unfamiliar regions, change representation, revise the objective, and inspect the artifact from different points of view.
 
That solved one problem.
 
We could now generate genuinely different possibilities.
 
It made another problem worse.
 
Once several plausible artifacts and several plausible perspectives exist at the same time, somebody still has to decide what survives.
 
## Who Judges the Judges?
 
At some point generating another opinion stops helping. Some artifacts have to survive and others have to die.
 
The metric problem from the previous section comes back here in a more dangerous form. A rubric can make judgment explicit, which is useful. It can also become the target the builder learns to satisfy.
 
If the evaluator repeatedly rewards step-by-step explanation, explanations grow. If it likes polished onboarding, everything begins to look like onboarding. If familiar visual conventions read as “clear,” unusual approaches may disappear before they have time to become good.
 
OpenAI’s CoastRunners experiment is the cartoon version of this failure: an RL agent discovered that driving in a loop and repeatedly collecting reward targets produced a higher score than finishing the boat race.
 
Goodhart’s Law with a speedboat.
 
A language-model builder does not need such an obvious loophole. It can learn the style of artifact that another language model tends to reward.
 
Making the evaluator more elaborate does not automatically solve the problem. Sometimes it merely creates a more elaborate thing to game.
 
### Comparison Is Often Easier Than Scoring
 
There was another reason I became less enthusiastic about absolute scores: I wasn’t particularly good at producing them either.
 
I can drink a coffee and have almost no meaningful answer to “How good is this on a scale from one to ten?”
 
Give me two cups and ask which one I prefer, and the problem becomes easier.
 
If I still cannot decide, the scientifically responsible procedure is presumably to finish both.
 
The same thing happened with the demos.
 
“Give this interface a pedagogical score from 1 to 10” produced suspiciously precise numbers attached to explanations of why the number should not be taken too seriously.
 
Showing two artifacts and asking:
 
Which one would you rather give to somebody encountering Merge Sort for the first time, and why?
 
worked much better.
 
Relative judgment asks less of the evaluator. It does not need a stable internal unit called one pedagogy point.
 
If we have many candidates, techniques such as Bradley–Terry can infer an ordering from a subset of pairwise preferences. Better still, the explanation for each preference can survive alongside the ranking and become input to the next generation.
 
Pairwise comparison removes much of the fake precision of absolute scoring.
 
It does not repair a biased judge.
 
Bradley–Terry can aggregate preferences. It cannot make those preferences true.
 
### One Judge Is Still One Judge
 
So I stopped asking one evaluator to represent everybody.
 
A learner can inspect the artifact from the position we developed above. A teacher can focus on explanatory sequence. Another evaluator cares about cognitive load, another about interaction or accessibility. A domain expert can ensure that our elegant simplification has not become false.
 
I call these **Independent Evaluators**, though the important word is *independent*.
 
Five copies of the same model given the same context and asked to wear five hats may still share almost every important blind spot. If all of them read the leading builder’s explanation of why its design is brilliant before inspecting the artifact, disagreement becomes less likely for reasons that have little to do with brilliance.
 
Sometimes I want the judges to see different things.
 
The beginner should use the artifact before reading the builder’s explanation. A critic looking for conceptual errors does not need three paragraphs explaining why the choice was clever. The usability evaluator does not necessarily need to know which branch is currently winning.
 
This is the **Isolation Principle**: preserve enough separation that independent pressure remains informative.
 
There is a difference between telling the builder:
 
Learners repeatedly lost track of which subarray corresponded to which branch of the tree.
 
and telling it:
 
The evaluator awards two extra points when each tree node has the same color as its corresponding subarray.
 
The first communicates the problem.
 
The second communicates the test.
 
Isolation does not magically remove shared bias. Two supposedly independent evaluators may still inherit the same assumptions from their training, their culture or the examples we give them.
 
But without isolation, we sometimes destroy even the independence we could have had.
 
### Calibrate the Judges
 
Independence creates another issue: everyone’s idea of “excellent” can drift.
 
References help.
 
For these demos I might give evaluators examples from Distill, 3Blue1Brown or Jay Alammar. The goal is not imitation. The examples provide scale.
 
“This is clear” means something different if the evaluator has seen only the last four generations of our own work.
 
Calibration matters especially when judgment remains in natural language, because *excellent*, *clear* and *polished* have no fixed unit.
 
References introduce their own anchor, of course. Calibrate too strongly against one aesthetic and every road leads to Distill.
 
So the reference is there to answer *how good?*, not *what should this become?*
 
### Let the Judge Use the Thing
 
Another early mistake was letting evaluators judge applications by reading them.
 
Open the demo.
 
A browser agent can click through it, resize the page, try controls in the wrong order, notice that an explanation appears after the moment when it would have helped, or discover that the beautiful button everybody admired does absolutely nothing.
 
I used to call the browser ground truth.
 
That was too generous.
 
The browser gives the evaluator contact with the artifact rather than a description of it. It can establish that an interaction works and observe what is visible at each point in the experience.
 
It cannot establish that a human learned Merge Sort.
 
A simulated beginner saying the explanation is understandable gives us a hypothesis. Several evaluators preferring one design gives us comparative evidence.
 
Neither substitutes for putting the artifact in front of actual learners.
 
The danger in a fully automated loop is that simulated evidence quietly replaces the expensive kind. Everything inside the machine agrees, the browser works, the ranking improves, and the loop congratulates itself.
 
The student has not yet been asked.
 
### The Evaluator Became an Institution
 
At some point I looked at what we had assembled and realized that *evaluator* no longer described it particularly well.
 
Builders proposed alternatives. Different judges approached them with different concerns. Some information was deliberately kept separate. Pairwise comparison helped decide which directions deserved more work. References calibrated the judges. Browser agents interacted with the artifact. Hard tests handled the parts that really were hard facts. Real-user evidence could eventually enter where simulation stopped being enough.
 
This looked less like a loss function and more like a tiny institution.
 
Not a good institution automatically. Institutions can amplify conformity, entrench bad assumptions and become spectacularly efficient at measuring the wrong thing.
 
But the shape of the problem had changed.
 
Humans face the same difficulty. One person’s judgment is useful and fallible. So we compare work, preserve disagreement, create standards, ask specialists to inspect different aspects, reproduce results, and occasionally discover that an entire professional community has become extremely sophisticated about the wrong thing.
 
Apparently, when the clean loss function disappears, you eventually reinvent peer review.
 
And that made the remaining human job painfully obvious.
 
I still decided when to research, when to build, which branches stayed isolated, whether a strange direction deserved another generation, which disagreement mattered, when to retrieve another example, and when the simulations had reached the point where only a real person could answer the question.
 
I had automated much of the work.
 
I was still running the inquiry.
 
The individual techniques were not the missing piece anymore.
 
The missing piece was the decision over **which technique the inquiry needed next**.
 
## Going Deeper
 
This was the part I wanted to test next.
 
By now the system had a respectable collection of moves. It could spawn independent builders, research previous work, retrieve context, preserve odd stepping stones, impose constraints, generate visual directions, compare artifacts, borrow different perspectives and interact with what had been built.
 
But there was no reason every problem should use those moves in the same order.
 
Research first may be sensible for one task and destructive for another because it anchors every branch before anything original appears. Five builders may reveal useful diversity, or reproduce one mistake five times. Evaluator disagreement may justify another experiment, or one evaluator may simply be confused.
 
A fixed Planner → Builder → Critic → Revise loop can be useful.
 
It also answers all of those questions in advance.
 
What I wanted to know was whether some of the workflow could remain part of the search.
 
That experiment became **Deep Mode**.
 
We gave an orchestrator the problem, the capabilities available to it, and enough of the search history to decide what kind of move made sense next. Builders still built. Researchers researched. Evaluators judged. Browser agents used the artifacts. Visual systems explored designs. Retrieval brought back prior work and old experiments.
 
The orchestrator’s job was not to perform all of those roles.
 
It was to decide which role the inquiry currently needed.
 
Sometimes the useful move was another independent branch. Sometimes it was research on a question exposed by the last prototype. Sometimes a visual direction deserved implementation. Sometimes two branches should exchange an idea. Sometimes the system needed another judge; sometimes it had enough judgment and needed an actual user.
 
At the highest level the loop was almost embarrassingly simple:
 
**state of inquiry → choose a move → act → observe what happened → update the state of inquiry**
 
The interesting part was that the move itself was not fixed.
 
That distinction mattered to me. Otherwise Deep Mode would simply be a larger workflow diagram containing more rectangles.
 
The architecture did not give us a universal problem-solving procedure.
 
It gave the orchestrator a vocabulary of possible moves and allowed the history of the inquiry to influence which one came next.
 
The experiment was whether the process deciding how to solve the problem could itself become more adaptive.
 
## What Emerged
 
The first Merge Sort demos were exactly what you would expect.
 
Bars moved around. Numbers changed places. Everything sorted correctly.
 
If you already understood Merge Sort, you could follow them. If you did not, they mostly provided animated evidence that a computer was performing an algorithm.
 
There was no single diagonal-layering moment here, and I do not want to manufacture one for the sake of the story.
 
The progress was more distributed.
 
Different branches exposed different weaknesses in our current idea of the demo.
 
Tree-like representations made recursion visible but could make a simple algorithm look forbidding. Keeping the array visible helped connect the decomposition back to the data, while also creating another place for the learner’s attention to go. Color could preserve identity between representations until too much color became another representation to decode. Some versions explained every step so carefully that the explanation became harder to follow than Merge Sort. Others became beautifully minimal and stopped teaching anything.
 
The useful pieces did not always live in the strongest overall artifact.
 
A visual relationship could survive after the application that introduced it was discarded. A criticism from a simulated learner could change the next builder’s framing. Research could explain why a failure kept recurring. A browser could occasionally end a sophisticated discussion by demonstrating that the interaction simply did not work.
 
That is less cinematic than one agent inventing diagonal layering over coffee, but in some ways it is closer to the Layer 3 idea. The result emerged from a population of partially successful attempts and judgments about what each had taught us.
 
Count-Min Sketch followed a different path.
 
The first versions looked like the data structure itself: grids with changing counters.
 
Technically correct.
 
Pedagogically opaque.
 
As the work continued, the designs increasingly organized themselves around the conceptual difficulties rather than the structure of the implementation. Collisions became visible. Approximation became something the learner could observe rather than merely read about. The relationship between memory and accuracy became part of the experience.
 
I do not take these demos as evidence that we solved automated design.
 
I do not even take them as evidence that the final demos teach humans better; that claim requires humans.
 
They established the narrower point I cared about: more of the work I normally performed in the vibe coder’s seat could move into the system without first reducing creative problem solving to one fixed workflow.
 
That success immediately exposed the harder problem.
 
At higher levels of abstraction, failure can become coherent.
 
## What Holds the Architecture Together?
 
Suppose the research agent reports that beginners understand recursion better when shown a tree.
 
A visual model proposes a tree-based explanation. A coding agent builds it. A simulated beginner prefers it. Two evaluators agree, so the orchestrator allocates another generation to that lineage.
 
This looks exactly like the compound intelligence we wanted.
 
Now ask where the first claim came from.
 
Perhaps it was a controlled educational study.
 
Perhaps it was one teacher’s opinion.
 
Perhaps the research agent inferred it from several examples.
 
Perhaps five articles repeated the same claim because all five ultimately cited one source.
 
Perhaps the study involved university students while our demo is for children.
 
Those are not small differences.
 
And everything downstream can still be perfectly competent.
 
The research is wrong.
 
The design responds intelligently to the wrong research.
 
The implementation is flawless.
 
The evaluators agree.
 
The orchestrator invests another generation.
 
Nothing crashes.
 
You can build a beautiful chain of reasoning on one stupid assumption near the bottom, like a cathedral built on a shopping cart.
 
As the components become better at producing coherent outputs, the original mistake may become harder rather than easier to see.
 
Software architecture gets away with abstraction because layers expose contracts. When I query a database, I do not inspect the disk. When I add two integers in Python, I do not check the CPU. I rely on interfaces whose behavior is stable enough that the details can disappear most of the time.
 
A cognitive architecture needs contracts too.
 
But types and APIs are not enough.
 
A research result, browser observation, evaluator preference, remembered failure and inherited design pattern should not enter the orchestrator’s context as five equally credible paragraphs.
 
Where did a claim come from? What was actually observed, and what was inferred? Which parts were checked? What remains uncertain? If an evaluator preferred one artifact, from what perspective? If an old experiment taught us a lesson, how often has that lesson survived and under what conditions?
 
This is not merely a memory problem.
 
It is a problem about the status of what is remembered.
 
Humans ran into it long before AI.
 
We built experiments, instruments, citations, peer review, reputation, replication, expert communities, legal standards, audits and all the other slightly annoying machinery that lets one person rely on something another person learned without personally repeating every experiment since Galileo.
 
These institutions are imperfect. Sometimes they preserve error. Sometimes they reward conformity. Sometimes the shopping cart survives peer review.
 
But their purpose is not to make every individual dramatically smarter.
 
It is to let fallible people build on one another while preserving some structure around why a claim deserves trust.
 
The point is not that an agent system should literally recreate academia in software. It is that once cognition becomes distributed, questions humans learned to handle institutionally—provenance, independence, replication, disagreement, authority—turn into engineering questions.
 
Our architecture was beginning to need the same distinction.
 
I had started the chapter trying to get myself out of the vibe coder’s seat. By automating more of the work there, I had ended up somewhere I did not expect.
 
The problem was no longer simply whether the agents were capable enough.
 
It was whether the things they believed deserved to be believed.
 
How do you know what to trust?
 
That is where System 3 begins.

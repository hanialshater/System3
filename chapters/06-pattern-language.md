# Chapter 6: Pattern Language

*When Knowledge Becomes Software*

Imagine hiring a brilliant employee who loses almost all procedural memory every evening. On Monday you explain how releases work. Tuesday, again. By Wednesday the employee has produced a beautiful deployment checklist. On Thursday you explain releases again. By Friday they have written a Python script that automates half the process and forgotten why the script exists. This was approximately where agents started.

Context windows got larger. Projects persisted. Memory systems got better. Agents learned to leave notes for themselves. But the deeper problem was never simply remembering more text. It was: **how should useful experience become reusable behavior?**

Chapter 5 ended with a society developing culture. That sounds abstract until you look at what is happening in software. Teams are increasingly storing their ways of working in Markdown files, instructions, examples, scripts, skills, evaluators, tool descriptions, memory, and small pieces of executable policy. The model may change next month. The knowledge can survive. Something strange has happened to programming.

## Three Ways to Tell a Computer What You Know

For most of computing history, if you knew how a process should work, you translated that knowledge into code. A customer asks for a refund. If the amount is under €50, approve it. If it is over €500, ask a manager. If the order is older than thirty days, reject it unless a specific exception applies. You take what the organization knows and turn it into `if`, `else`, functions, database schemas, and state machines.

Call this **Software 1.0**. Andrej Karpathy used that label for the familiar world in which humans write the program directly. The computer does approximately what the code says, which gave us modern civilization and dependency injection.

Then machine learning changed the contract. Suppose the problem is not “refunds over €500 need approval” but “is this refund fraudulent?” Nobody knows the full rule. We have examples. So instead of writing the behavior, we write the training machinery, choose data and an objective, and optimization produces the behavior inside model weights.

Karpathy called this **Software 2.0**. Knowledge moved from explicit code into parameters. Humans no longer had to describe every feature that makes an image a cat, every acoustic variation that makes a sound a word, or every interaction that makes a recommendation relevant. We supplied data and pressure; the model discovered useful internal representations.

There was a trade. Software became vastly more capable in domains where rules were hard to articulate, but much of the learned knowledge became difficult to inspect. The fraud system “knows” patterns no engineer wrote down. You can measure its behavior, probe it, retrain it, maybe interpret pieces of it, but you cannot open `fraud_rules.py` and read what the organization learned.

Large language models created a third possibility. Karpathy's later **Software 3.0** framing treats natural language itself as a programming interface. The obvious version is a prompt:

> Read this support request, identify what the customer actually needs, check the relevant policy, and resolve it if you are confident. Escalate cases involving legal threats, suspected fraud, or policy conflicts.

That is not Software 1.0. Nobody enumerated every legal threat or every possible policy conflict. It is not Software 2.0 either. We did not retrain the model to teach it this workflow. We expressed operational knowledge in language and relied on a general model to interpret it.

But “prompt as program” is only the beginning. The more interesting unit is becoming **executable knowledge**.

## The Return of Knowledge Engineering

“Knowledge engineering” has an unfashionable smell because AI has been here before. Expert systems tried to encode human expertise explicitly: rules about medicine, geology, finance, configuration. The dream was sensible. Find experts, extract what they know, put it into a knowledge base, and let a machine reason over it.

The maintenance was less romantic. Expertise is full of exceptions, tacit assumptions, context, competing heuristics, and sentences beginning with “normally, unless...”. Rule bases became brittle. Knowledge engineers spent their lives interviewing experts and converting fuzzy human practice into formal logic. Machine learning eventually offered a seductive alternative: stop asking experts to explain themselves and learn behavior from data.

Now knowledge engineering is returning through the back door, carrying Markdown.

The difference is important. We no longer have to compile every piece of knowledge into rigid symbolic logic. A modern skill can contain prose, examples, scripts, reference material, counterexamples, tool instructions, and boundary conditions. The language model does some of the interpretation that the old knowledge engineer had to make explicit.

This creates a kind of artifact that sits awkwardly between source code and training data. It might say:

> When reviewing a ranking experiment, first establish whether the apparent gain is concentrated in one market or traffic segment. Check instrumentation changes before inventing a causal story. If click metrics rise while orders remain flat, inspect price and position shifts before celebrating. Treat day-one effects with suspicion.

There is no deterministic function here. There is accumulated practice. A human expert can read it and use judgment. Now an agent can too.

So I think the deeper transition is not merely from Python to English. It is a move from **programming behavior**, to **learning behavior**, to **engineering the knowledge from which behavior is produced**.

## This Book Accidentally Became a Software 3.0 Project

I ran into this while editing the book you are reading.

“Make this chapter better” turned out to be almost useless as an instruction. The agent knew what polished prose looked like, and that was part of the problem. It would remove wandering sentences, compress paragraphs into neat antitheses, make every section symmetrical, and occasionally replace a strange joke with something that sounded like a management consultant had discovered philosophy.

So I corrected it. Don't kill the wandering. Don't turn everything into slogans. Preserve the weird joke if it is carrying an idea. Stop breaking every thought into a five-word paragraph. Compare the revision to the previous version rather than assuming shorter and cleaner means better.

Then, a few chapters later, the same mistakes returned.

At some point I realized I was behaving exactly like the manager of the amnesiac employee from the opening. The useful thing was not another correction. It was to externalize what we had learned. We started turning the corrections into reusable evaluation instructions: what to compare, which tendencies to penalize, what “human writing” meant in this book, which kinds of humor were load-bearing rather than decorative. When “this still feels like LLM writing” proved too vague, we even started looking at paragraph statistics and using them as evidence—not as the objective, but as one diagnostic for a failure we had already noticed.

Nothing about the underlying model weights changed. But the next editing session inherited more of the book's editorial history than the previous one had.

That is Software 3.0 in miniature. The durable thing was not a prompt. It was a growing body of **operational knowledge about how this particular artifact should be made**.

And that is exactly what companies are starting to do at much larger scale.

## The Repository Learns How to Explain Itself

The coding industry is converging on a surprisingly concrete version of this idea. A repository increasingly contains two systems: the software itself, and a second layer explaining **how an artificial contributor should work on the software**.

OpenAI lets Codex read `AGENTS.md` files that explain repository structure, commands, tests, and local practices. OpenAI also says its own teams have built hundreds of reusable skills for work that would otherwise be difficult to delegate consistently, including running evaluations, monitoring training runs, drafting documentation, and reporting on growth experiments. Anthropic's Agent Skills use the same general shape: folders of instructions, scripts, and resources that are loaded only when relevant. GitHub Copilot now reads `AGENTS.md`, repository instructions, path-specific instructions, and agent skills as part of its coding and review workflows.

GitHub did something especially revealing: it studied more than 2,500 public agent-instruction files to see what developers were actually writing. The useful files were not grand declarations like “be a world-class engineer.” They looked like operating manuals. Exact commands. Real code examples. Project structure. Tests. Git workflow. Boundaries about what the agent may and may not touch. In other words, the industry rediscovered that expertise is not a persona. It is a collection of situated constraints and habits.

By 2026 GitHub had gone one step further and made skills portable through its CLI across multiple agent hosts, including Copilot, Claude Code, Cursor, Codex, and Gemini CLI. That detail is easy to miss. It means some organizational knowledge can increasingly survive not just a new session, but a **new model vendor**.

The employee changes. The operating manual remains.

This is why the shift matters economically. Frontier models know Python, SQL, React, experimentation, and a remarkable amount of public technical culture. What they do not know is why *your* company refuses to deploy on Friday, why a particular dashboard metric has been broken since 2023 but remains in every meeting, which customer exception was created after a lawsuit, or why Alberto should never again be asked to investigate penguins. Organizations run on this layer of weirdness.

Much of it never makes it into textbooks or training data. It exists in senior people's heads, old incident documents, pull-request comments, abandoned wikis, onboarding conversations, half-remembered arguments, and scripts with names like `final_fix_v2_really.py`.

Traditional software captures some of it in code. Machine learning captures some in data. But an enormous amount is neither rule nor correlation. It is **procedural knowledge**: what to check first, which shortcut is dangerous, which source is trustworthy, when the normal process does not apply, and what “good” means here rather than in a generic benchmark.

For a long time, new employees acquired this by hanging around older employees. Now a growing part of it can be externalized.

That has a strange consequence. If an organization's expertise lives mostly in fine-tuned model weights, replacing the model may require rebuilding a great deal of behavior. If much of the differentiation lives in skills, tools, evaluation sets, process descriptions, patterns, memory, and trusted data, a stronger foundation model can inherit a surprising amount of that culture immediately.

The model becomes replaceable infrastructure. The organization's weirdness survives.

But merely accumulating folders is not a knowledge strategy. It is how we get prompt spaghetti. For that we need something older.

## From Skill to Pattern

Christopher Alexander's *A Pattern Language* was about buildings and towns, not artificial agents. But the abstraction fits almost suspiciously well. A pattern is not a command. It describes a recurring situation, the forces that make the situation difficult, a response that has worked, and the consequences of choosing that response. The pattern has a name because names let communities think with it.

Consider an agent rule:

> Never use regex on nested syntax.

Useful, perhaps. Also wrong. Regex is perfectly reasonable for many small extraction tasks. A full parser may be absurd overhead for a five-line configuration file. The useful knowledge is not `regex = bad`. It is that nested recursive structure creates characteristic failure modes for flat pattern matching; those failure modes become more expensive as input complexity grows; and eventually parser overhead becomes cheaper than debugging clever regex written at 2 a.m.

That is a pattern.

A prompt library remembers language. A pattern language remembers **experience**.

The book has already accumulated several patterns whether we called them that or not. **Immutable Harness:** when autonomy makes the solution fluid, keep the evaluation boundary harder to change than the thing being evaluated. **Independent Evaluators:** when one judge can be gamed, introduce genuinely independent sources of pressure. **Strategic Constraint:** when showing the final answer causes imitation, expose principles or partial information instead. **Persistent Research Programs:** when early evidence may favor the wrong theory, allow competing lineages to accumulate their own history before forcing consensus.

Notice what these contain. Not merely “do X.” They contain why, when, the trade, and the characteristic failure. That is the difference between instructions and institutional knowledge.

## Culture Needs Archaeology

Chapter 4 argued that factual knowledge needs provenance. Culture does too.

Suppose an agent spends three hours debugging a bizarre file format. It eventually writes `marc_analyzer.py`, succeeds, and saves the lesson:

> Use `marc_analyzer.py` for MARC files.

That is better than forgetting everything. It is also how superstition begins. A richer artifact records that the analyzer worked on these variants, failed on this encoding, replaced two approaches that did not work, was modified later by another agent, and succeeded on seven subsequent tasks. The next agent does not merely inherit a behavior. It inherits some archaeology.

Human organizations do this inconsistently. A senior engineer tells you “never deploy Friday,” and perhaps six months later someone finally tells you which production incident created the rule, what systems it applied to, and why the organization continues violating it every second Friday. A pattern without history turns easily into ritual.

Executable knowledge therefore needs some of the same trust machinery as factual knowledge. Who created this pattern? From what failures? How often has it worked? Where has it failed? When did the surrounding system change? Is this established practice or one person's strong opinion written with confident punctuation?

The more powerful a reusable artifact becomes, the more expensive a bad one becomes. A hallucinated answer may poison one task. A hallucinated skill can poison the next thousand. A bad memory is a mistake. A bad pattern is a mistake with tenure.

## Knowing Something Is Not Knowing When to Remember It

There is another problem. Ten excellent patterns are easy. Ten thousand are not. The agent cannot load all of them. Even if the context window technically fits them, flooding every task with every lesson is like solving human memory by reading your autobiography before answering the door.

This is why the seemingly boring mechanics of retrieval become part of intelligence. Anthropic's skills use progressive loading. GitHub separates global, path-specific, and task-specific instructions. Harnesses increasingly treat the working context as an artifact that must be constructed rather than a transcript that grows forever.

Having learned the right thing is not enough. The system has to retrieve it at the right time, at the right level of detail, without burying the present problem under the organization's entire history.

This sounds like information retrieval because it is information retrieval. It also sounds like cognition because it is becoming cognition. A culture can contain the right wisdom and still fail because nobody invokes it when it matters.

Humans know this failure intimately. Every company has written a postmortem whose recommendations are rediscovered three incidents later by different people using the phrase “interesting, we should probably document this.” Software 3.0 does not remove the problem. It makes the retrieval policy programmable too.

## Culture Can Become a Prison

If the only problem were forgetting, the answer would be simple: remember everything. Unfortunately, organizations also suffer from remembering too well.

Every process exists because it helped at some point. Then the world changes and the process remains. A release checklist reaches twenty-seven mandatory boxes because every incident adds a box and no incident removes one. A design heuristic becomes company identity. A temporary workaround becomes architecture. Eventually someone asks why a process exists and receives the most dangerous explanation in organizational life:

> That's how we do it.

Agents can reproduce this at machine speed. A pattern succeeds ten times. Its confidence rises. More agents retrieve it. Because more agents use it, alternatives receive less traffic. The dominant pattern therefore accumulates still more supporting evidence. Soon the system has an impressive empirical record proving the thing it stopped comparing against.

Chapter 5 called this the problem of paradigms. Chapter 6 makes it operational.

Patterns need decay, counterexamples, versioning, and competing alternatives. Some should be local rather than universal. Some should expire after the system they describe changes. Occasionally a strong agent should be allowed to ignore the manual precisely so we can discover whether the manual still deserves its authority.

The system needs to know the difference between “we tried twelve alternatives and this kept winning” and “nobody has tried another way since 2025.”

Culture needs memory.

It also needs rebellion.

## The Skill That Writes Itself

At this point there is an obvious scaling problem. A company has fifty agents. They create tools, write instructions, discover workarounds, accumulate evaluations, and leave behind thousands of useful and useless traces. Some lessons deserve to become local habits. Some should become company-wide patterns. Some contradict older patterns. Some worked because the evaluator was broken. Some are excellent but apply only to one model version.

We could assign humans to curate all of this manually. Congratulations. We have created middle management again.

The more interesting possibility is already beginning to appear in research on evolving context and skills: an agent notices recurrent experience, distills a reusable procedure, proposes a new skill, evaluates it on past and held-out tasks, and earns the right to make that lesson persistent. Lilian Weng describes related systems as evolving playbooks: successful and failed trajectories are reflected on, converted into structured knowledge, and curated rather than simply appended forever.

This is where Pattern Language stops being a chapter about documentation.

Experience becomes knowledge. Knowledge becomes executable. Executable knowledge changes future behavior. Future behavior produces new experience. We have a learning loop **outside the weights**.

And once the knowledge artifacts, retrieval policy, evaluators, tools, and workflows are all editable software, a slightly dangerous question appears.

Why should humans be the only ones allowed to edit them?

That is the next chapter.

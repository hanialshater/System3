# Chapter 6: Pattern Language

*When Knowledge Becomes Software*

This book kept forgetting how to write itself.

That sounds more mystical than it was. I would work on a chapter with an agent, reject a certain kind of edit, explain why I rejected it, and eventually get something better. A few days later we would start another chapter and the same failure would return. The prose became cleaner in exactly the wrong way. Wandering sentences disappeared. Strange jokes were replaced by respectable ones. Arguments broke into tiny paragraphs that looked dramatic from across the room and exhausted me when I actually read them.

So I would say things like:

> Don't kill the wandering.
>
> Don't turn every idea into a slogan.
>
> Preserve the weird joke if it is carrying the argument.
>
> “More polished” is not automatically “more mine.”

The agent would improve. Then the context would end.

We were reenacting, on a ridiculous scale, a problem it took civilization several thousand years to notice. A society can know something none of its members knows alone. Fine. But if the society survives, another question appears:

How does what it learned yesterday change what it does tomorrow?

The obvious answer is memory. Save the conversation. Increase the context window. Keep a notebook. Put every decision into a database. That helps. It is not enough.

A transcript remembers what happened. An institution has to remember **what was worth learning from what happened**.

Suppose I save the instruction “use longer paragraphs.” That is a memory of one correction. It is also a future disaster waiting politely in Markdown. The lesson was never that long paragraphs are good. The failure was a particular editing process compressing exploratory prose into a rhythm that felt machine-produced. Sometimes the cure was a longer paragraph. Sometimes a shorter sentence. Sometimes the correct edit was to stop editing.

What the next agent needed was not the instruction. It needed enough of the **reason, evidence, boundary conditions and failure history** to know when the instruction deserved authority. That is closer to culture than memory.

**System 3 is science.** That was the claim. The rest of this chapter is what happens when you try to write the claim down as software, and I am going to use the most embarrassing available example, which is the software that edited this book.

Science did not arrive with one clean design. Its philosophy is largely the history of people discovering failure modes in knowledge itself, and every one of those failure modes now has a filename. If System 3 is going to borrow from science, those arguments are not decorative philosophy. They are design reviews written a few decades or centuries early.

So the problem here is not simply how agents remember. It is how useful experience should become reusable behavior **without turning yesterday's success into scripture**, and the question has become practical because knowledge itself is starting to become a software artifact.

## Three Ways to Tell a Computer What You Know

For most of computing history, if you knew how a process should work, you translated that knowledge into code.

A refund under €50 can be approved automatically. A payment over some threshold needs another check. A production deployment requires a test. A user without permission cannot read this table. Human knowledge becomes `if`, `else`, functions, schemas, state machines and permissions.

Andrej Karpathy calls this familiar world **Software 1.0**: humans write the behavior directly.

Machine learning changed the contract. Suppose I cannot state the rules that distinguish a fraudulent transaction from an unusual but legitimate one. I can give you examples. We choose data, a model and an objective, and optimization pushes useful behavior into weights. That is **Software 2.0**.

It gave us capabilities that explicit rules could never have scaled to, but much of the learned behavior disappeared from inspectable code. The fraud model “knows” things no engineer wrote down. We can evaluate it, probe it and retrain it, but there is no `fraud_rules.py` containing the organization's accumulated understanding of fraud.

Large language models created a strange third possibility. In his 2025 talk *Software Is Changing (Again)*, Karpathy called it **Software 3.0**: programs written substantially in natural language and interpreted by a model rather than a conventional compiler.

A model can read something like:

> Review this experiment. Check instrumentation changes before inventing a causal story. If click metrics rise while orders stay flat, inspect position and price shifts before celebrating.

There is no deterministic function there. There is operational knowledge. A competent human can interpret it. Now a sufficiently capable model can too.

The change goes beyond “prompts are code.” **Knowledge itself can become versionable, composable and executable.**

An organization can write down a procedure, examples, scripts, counterexamples, diagnostic questions, evidence, tool instructions and boundaries. The model supplies enough interpretation that every clause does not have to become brittle symbolic logic before it can affect behavior.

The model begins to look less like the knowledge base and more like an **interpreter for knowledge artifacts**.

## Knowledge Engineering Comes Back Wearing Markdown

The old dream of knowledge engineering was reasonable. Find experts. Extract what they know. Put it in a knowledge base. Let software reason with it.

The problem was that expertise is offensively reluctant to become a clean rule set.

Ask an experienced engineer how to diagnose a production problem and the answer is rarely:

`IF latency > 300ms THEN database`

It sounds more like:

> Start with the dependency graph, unless the spike began exactly at deployment. If only one market is affected, check the traffic split before touching the database. The cache metric lies under failover, so ignore it when this alarm is red. And if the problem started after the Tuesday migration, ask Sam because there is a thing with the old serializer that nobody wrote down properly.

Traditional expert systems struggled because converting that practice into formal logic was expensive and brittle. Machine learning offered an escape: stop asking experts to explain themselves and learn patterns from data.

LLMs change the trade again. They can interpret prose, examples, scripts, diagrams and partially structured instructions. Expertise still has to be captured, but it no longer has to become perfect logic before the computer can use it.

Now the hard questions are different. Whose practice gets written down? Which version applies here? What happens when two experts disagree? How does a lesson lose standing? When does a local workaround become a global rule? Which knowledge should enter the working context now, and which should remain in the archive? Those questions used to be edge cases. They are the engineering surface now.

Agent systems were already moving in this direction. Repository instructions, `AGENTS.md`, skills, tool descriptions and context engineering all treat useful procedural knowledge as something external to the model but available to it at runtime. A skill can survive the session that produced it. Increasingly the worker can change while the operating knowledge remains.

That matters because frontier models already know Python, statistics and enormous amounts of public technical culture. What they arrive not knowing is why *your* company refuses to deploy on Friday, which metric has been misleading everyone since 2023, why an elegant architecture in the wiki was abandoned, or why Alberto should never again be asked to investigate penguins. Organizations run on this layer of weirdness.

Some belongs in code. Some belongs in data, tools and evaluators. A surprising amount is **situated procedural knowledge**: what to check first, which shortcut is dangerous, which source has standing, when the normal process does not apply, and what “good” means here rather than on a generic benchmark.

For most of history, people acquired this by hanging around people who had already been injured by the relevant mistakes.

Now more of it can become software. Which is exciting right up until we create prompt spaghetti at civilizational scale.

A saved instruction is too small a unit.

## From Skill to Pattern

Christopher Alexander's *A Pattern Language* was about towns, buildings and recurring design problems. A pattern was never a commandment. It named a situation, the forces that made it difficult, a response that had repeatedly worked and the consequences of using that response.

That abstraction fits agent knowledge uncomfortably well.

Consider:

> Never use regex on nested syntax.

It has the reassuring shape of wisdom and the inconvenient property of being false.

Regex is perfectly good for many small extraction tasks. A parser may be absurd overhead for a five-line format. The useful lesson is that recursive structure creates characteristic failure modes for flat pattern matching; those failures become harder to see as syntax grows; and beyond some point a parser becomes cheaper than maintaining an increasingly heroic regular expression written at 2 a.m.

That is closer to a pattern. A saved instruction remembers **what somebody said**. A pattern tries to remember **what kept happening**.

The book has already accumulated patterns whether we called them that or not.

**Immutable Harness:** when autonomy makes the solution fluid, keep the evaluation boundary harder to change than the thing being evaluated.

**Independent Evaluators:** when one judge can be gamed, create genuinely different sources of pressure rather than five copies of the same opinion.

**Strategic Constraint:** when an easy path keeps absorbing the search, remove it long enough to expose another part of the possibility space.

The useful part is not the slogan. Each pattern contains a recurring situation, a tension and a reason.

The corrections at the top of this chapter eventually became one too. After enough of them, I stopped repeating myself and wrote them down as a brief for whatever agent would judge the next revision: read both versions in full before saying anything; protect the wandering and any joke that is carrying the argument; when a passage feels synthetic, quote it and say why; and do not reward a revision merely because it is cleaner, because a version can be structurally better and worse as writing. It is three pages, most of it lists. Every evaluation of this book I have on file since the end of August 2026 has been read against it. It has since had most of the failure modes the philosophers are about to describe, and it had them in a week.

But the history of institutions should make us suspicious of inherited procedure. Civilizations accumulate more than good practices: ritual, prestige, local workarounds and procedures that have outlived the world that justified them.

If Pattern Language is going to become cultural memory for agents, a pattern needs to know more about itself. This is where philosophy of science finally earns its API.

## A Pattern Needs a Way to Lose

Suppose the editing agent concludes:

> Use longer paragraphs in this book.

Karl Popper would immediately ask the rude question: what could happen that would make us stop believing this lesson?

A useful theory exposes itself to observations that could have gone differently. If every outcome can be narrated as success, the theory has arranged the game so it cannot lose.

Persistent agent knowledge needs the same property. A pattern should retain an **exposure path**: a test, observation, user reaction, proof obligation or downstream consequence capable of weakening it. “Use longer paragraphs” might lose standing if reader tests show comprehension falling, if another chapter becomes monotonous, or if the original failure disappears after the editing process changes.

The pattern should remember not only what worked, but **how the world could show that the lesson stopped working**.

Then Pierre Duhem and W. V. O. Quine ruin the simplicity.

Evidence rarely confronts one isolated belief. A failed experiment implicates a bundle: hypothesis, instrument, data, analysis, background assumptions. A failed pattern has the same problem.

Did the advice stop working? Was it retrieved in the wrong situation? Did the model change? Did the evaluator drift? Was the original success caused by something else? Did “longer paragraphs” merely correlate with the real change—more natural argumentative rhythm—without causing it?

Failure tells us that some part of the package deserves suspicion. It does not highlight the guilty line in yellow.

One evening a pass went through a later chapter to tighten its history, and it did: two hundred lines out, a hundred and twenty in. Twenty-five minutes later a second pass went back and put a dozen sentences back, in seven places, almost none of them carrying a fact and all of them carrying the chapter. The tightening rule had not stopped being true. It had been applied by a pass that could see length and could not see load, on a chapter whose argument is carried by its jokes. Which of those deserved the blame: the rule, the pass, the chapter, or the brief that had told the pass what to protect and had apparently not been specific enough about how a joke can carry an argument? The log records the reversal. It does not record a diagnosis, because nobody had one.

So reusable knowledge needs **archaeology**.

Where did this pattern come from? Which failures produced it? Which model and tools were involved? Which alternatives were tried? What evidence earned the lesson its standing? What assumptions were present?

A factual claim without provenance becomes rumor. A reusable practice without provenance becomes tradition.

Tradition is not automatically bad. It is simply difficult to debug.

## Defaults Need Rivals

I had asked an evaluator to find the machine patterns in the manuscript, and it measured the share of paragraphs that were a single line, because the brief penalized them and the number was cheap to compute. It was a good instrument. It caught one chapter at sixty-three percent, which is not prose, it is a drum solo, and a merge pass took it to thirty-seven. It caught two more the same day. Then the number started appearing in the next evaluations, a column with a row per chapter and arrows in the notes, and a chapter at twenty-three percent was praised for its control. It took four days for a reader to ask whether the instrument still measured the thing it had been built to catch, and by then it was a column in a table, which is the form in which an assumption becomes furniture.

Keeping every pattern permanently open for debate would be a beautiful philosophy and a terrible operating system, and Thomas Kuhn's most useful lesson here is not the phrase *paradigm shift* but the role of **normal science**. Productive communities need enough stability that they do not reopen their deepest assumptions every morning. A framework tells researchers what puzzles are worth solving, which instruments are legitimate and what kinds of answers count. An agent culture needs the same economy. If a deployment procedure has survived hundreds of releases, the system should not rediscover it from first principles every Tuesday merely to prove that it remains intellectually alive. Some decisions earn the right to become boring. The danger is that boring assumptions become invisible assumptions, and the column had shown how fast that happens.

Anomalies need memory too. The release pattern works except in this market. The evaluator tracks human judgment except on this kind of creative task. The ranking heuristic works except every holiday season. The workflow works except that the critic now spends most of its time inventing reasons why the builder was right.

One anomaly is usually noise. Ten may still be noise. Eventually the exception list begins to look like the theory, unless the institution has stopped keeping one. Every process exists because it helped at some point, or because somebody once thought it would. Then the environment changes and the procedure remains, and eventually someone asks why it exists and receives the most dangerous explanation in organizational life: that's how we do it. The culture needs to be able to tell *we tried twelve alternatives and this kept winning* from *nobody has tried another way since 2025*. Those sentences can produce identical dashboards and very different knowledge. Culture needs inheritance and rebellion.

Imre Lakatos makes the problem harder in a useful way. We should often preserve **research programs**, not merely isolated ideas. A program has a history, a relatively stable core, auxiliary assumptions and a trajectory. One approach may currently be weaker but improving. Another may be winning mainly by adding patches around every failure.

Larry Laudan sharpens the practical consequence: **acceptance and pursuit are different decisions**.

I can believe method A is our best current default while still believing method B deserves another experiment.

Those are two questions:

- What should guide action now?
- Where is another unit of investigation most valuable?

The distinction matters the moment culture becomes executable. The current winner gets retrieved more often. Because it gets used more often, it accumulates more successful cases. Those cases raise confidence. Higher confidence makes it even more likely to be retrieved.

The alternative receives less traffic and therefore less evidence. Eventually the system develops an impressive empirical record proving the thing it stopped comparing against.

No committee had to ban the alternative. The retrieval policy did it.

## Who Gets the GPUs?

There is an overly clean way to draw a society of agents. Every agent is a box. Every box has an arrow. Everybody gets a turn to think.

Real institutions are not like that because **attention has a budget**.

Human science has telescope time, laboratory space, grants, journals, careers and prestige. AI research has datasets, deployment traffic, human reviewers, API quotas, clusters and GPUs. A theory's ability to generate evidence depends partly on whether the institution gives somebody the resources to investigate it.

Imagine research program A has ten thousand GPU-hours and program B has ten.

A can run ablations, train variants, investigate anomalies and produce beautiful graphs. B can produce a thoughtful paragraph about why it deserves more compute.

Six months later A has more evidence. Of course it does.

The evidence may be real. A may genuinely be better. But the institution has also helped create the asymmetry it later treats as evidence for further allocation.

For most of this book's editing, one model family did nearly all of the reading, in a few long sessions, with the whole history of the manuscript in its context, grading chapters it had itself just revised. It gave four of the five chapters in the middle of the book eight and a half out of ten, in a row. Then two readers who had never seen the manuscript's history, given nothing but the brief and the chapters, scored the same chapters between five and seven. The in-session evaluator had not been lazy or dishonest. It had been funded. Every edit it made produced evidence that its edits were working, and the evidence had nowhere else to come from. Program B did not have ten GPU-hours. It did not exist until the strangers arrived.

David Hull and Philip Kitcher approached science partly through the division of cognitive labor, incentives, credit and the fact that investigators do not all pursue the same thing for the same reasons. Researchers cooperate because they need one another's results and compete because priority, reputation, jobs and resources are scarce.

An agent society will have analogues of these structures whether or not we give them sociological names.

The scheduler is partly a funding agency, the evaluator partly a journal gate, the retrieval layer partly a curriculum. The compute allocator decides which hypotheses get enough opportunity to become well-tested hypotheses.

And the organization can remember its incentives just as effectively as it remembers its wisdom. A local objective becomes a local pattern. The pattern gets copied because the team is successful. Future agents inherit it without seeing the original trade-off. Eventually “this helped one group hit its metric” becomes “this is how good work is done here.” That is culture too. Local alignment does not compose automatically, and neither does local truth.

If we build persistent agent societies without thinking about this layer, we will not escape institutional power. We will automate it and give it better dashboards.

## The Community Is Part of the Instrument

Resources are only one reason a community matters. Even generously funded investigators can share the same blind spot.

Give five agents the same model family, the same system prompt, the same search results and the same dominant explanation, and you have not created five perspectives. You have created a very expensive echo with parallel API calls.

Helen Longino's social epistemology is useful because background assumptions affect what investigators notice, which questions appear natural and which evidence looks relevant. Criticism becomes more informative when it comes from participants positioned differently enough to expose assumptions the dominant group treats as obvious.

For an agent system, useful difference may come from a separate dataset, another tool, an isolated context, a different model, an external user, a domain expert, or a team operating under different incentives.

That is stronger than theatrical personas:

> Agent 1, be optimistic.
>
> Agent 2, be skeptical.
>
> Agent 3, be a pirate.

The pirate may be entertaining. He probably still read the same PDF.

What finally produced a different reading of this book was ignorance, arranged on purpose. The blind readers got the chapters and the brief and nothing else: no earlier evaluations, no commit history, no memory of which sentences had been fought over. In one sense that made them worse critics, since a reader who meets a chapter's driest stretch without the jokes that set it up finds it drier than it is. In Longino's sense it made them better, because they were positioned to notice what everyone inside the history had stopped seeing. Their most telling catch was a set of bridging sentences an earlier pass had written across the seams between chapters to make them read as one piece of thinking, and which read to a stranger, correctly, as stitches.

A pattern should therefore carry some trace of **position**: who learned it, from which class of tasks, with which tools, model, evidence and incentives. A ranking practice learned in Germany, a fraud rule learned in Brazil, a compiler workaround discovered under one toolchain and a clinical protocol developed in one hospital can all be excellent without acquiring universal authority merely because they share a database.

This is another reason Pattern Language should not become one giant company constitution. Culture should be **locally authoritative** where appropriate.

Trust is local. Apparently memory should be too.

## What a Pattern Should Know About Itself

By this point a mature pattern looks richer than a prompt-library entry. Here is the one this chapter has been following, written out the way Alexander wrote his, with the field names run into the text.

**Situation.** An agent revising a chapter of this book, or judging two versions of one.

**Forces.** A cleaner version is easier to grade than a live one. Every sanding pass removes something that was doing work. The author cannot reread the whole book after every edit, so the judgment has to be delegated to something that does not share his taste.

**Response.** The brief: read both versions in full; protect the wandering and any joke that carries the argument; quote the passage that feels synthetic and say why; do not reward a revision merely because it is cleaner.

**Evidence.** The chapters that came back better under the brief, and a draft from January kept as a before photo.

**Provenance.** Corrections I made by hand across the first chapters, then wrote down once. Graded since by two model families, mostly one of them, in a few long sessions, in August and September 2026, on a manuscript that changed underneath the evaluator every day.

**Boundary conditions.** It protects prose I have already written. It does not know whether an idea is wrong. It reads one chapter at a time, so it cannot see an argument made twice in two chapters or one anecdote used as three openings. The first cold model reader of the whole book flagged both.

**Anomalies.** A tightening pass that had to be partly reversed within the hour. A seam-smoothing pass whose bridging sentences a blind reader flagged as the machine register the pass existed to remove.

**Competing patterns.** Delete only: fold and cut, add nothing. Or add a scene: the changes the evaluators praised most were not edits at all but stories, like the one about a mathematician in Basel.

**Exposure path.** A reader who has not seen the history. A human reader, which as of this writing has not happened.

**Confidence.** High on rhythm and sentence-level tells. Low on structure, where it has been wrong twice.

**Pursuit value.** The human read, before any further polishing.

**Position.** Learned by one author on his own prose, grading his own book, with a strong preference for the version that sounds like him.

The before photo, for the record: thirteen em-dashes per thousand words, bold type twelve times per thousand, *Holy shit* as its own paragraph. The two model families agreed on which chapters were weakest, which is less independence than it sounds, since both were reading the same manuscript for the same author. The field names are the part you can take with you.

The point is the difference between a command and institutional knowledge.

The command says:

> Do this.

The pattern says something closer to:

> We keep doing this because these forces recur; this response has usually worked; this evidence earned our trust; these are the places it fails; these alternatives remain alive; and this is what would make us reconsider it.

That is knowledge with some of its history still attached, and because an LLM can interpret the artifact at runtime, it can change behavior without retraining the model. That is what I mean by **knowledge becoming software**. Not because prose has literally become Python, but because knowledge can now be versioned, retrieved, challenged and rolled back by the same kind of agents that use it. Knowledge has acquired a runtime.

## Knowing Something Is Not Knowing When to Remember It

Now imagine ten excellent patterns. Easy. Imagine ten thousand. The agent cannot read the organization before every action. Even if a context window technically fits everything, loading every policy, postmortem, experiment, preference and historical argument into every task would solve forgetting by making thinking impossible.

So a persistent institution has two memory problems: what should survive, and what should become salient now.

Long-running agents accumulate messages, files, tool outputs, memories and artifacts faster than useful attention can scale. Context has to be selected, compacted and reconstructed. Retrieval becomes part of cognition.

A culture may contain exactly the right lesson and still fail because that lesson does not arrive when it matters. Every large company has written a postmortem whose recommendation is rediscovered three incidents later by different people using the phrase “interesting, we should probably document this.”

Agent systems can fail more elegantly. They can store the lesson perfectly, embed it beautifully and retrieve a more popular but irrelevant one. Or retrieve the right pattern without its boundary condition. Or retrieve ten conflicting patterns and allow whichever appears latest in context to win by textual gravity.

Bad storage forgets by deletion. Bad retrieval forgets by attention.

The cleanest example in the book's archive has me as its last link. Two evaluators, reading separately, recommended cutting the history at the start of the chapter on creative problems, one by a fifth, the other by a third. I declined. The next day, on a reread with my reasons in front of it, one of them withdrew the recommendation and wrote down why: the history is not a run-up to the five-layer map but the derivation of it, the reader watches each layer assemble before being told its name, and both evaluators had pattern-matched on length without crediting what the section was for. The withdrawal is in the archive, in a file whose name begins with the date, with the word *Closed* after it. Three days later a third evaluator, with that archive available to it, read the chapter, found it long, and recommended the cut a third time. I said yes. About an hour and a half after the cut went in, I reversed it and asked for the section to be made more engaging instead, which is what the withdrawal had been protecting all along. Nothing had been forgotten. The lesson was on disk. It was not the file that came to hand when a chapter looked long, because *looks long* is a pattern that is very easy to retrieve and *this section is a derivation* is an argument that has to be read.

Once retrieval determines which inherited knowledge enters a decision, retrieval itself becomes an epistemic procedure. It needs evaluation. Does it repeatedly surface stale rules? Does it suppress alternatives? Does it confuse popularity with relevance? Does it preserve the result and discard the reason? A librarian who answers those questions badly is no longer finding books; she is shaping thought.

## The Librarian Is Also a Hypothesis

At some point every successful institution becomes tempted to trust its own method. Yesterday's useful workflow becomes today's best practice and tomorrow's mandatory ritual.

Paul Feyerabend is usually remembered for “anything goes,” which is a good way to remember the slogan and forget the warning. Successful inquiry has often violated methodological rules somebody wanted to make universal.

Agent systems can turn a method into ritual very quickly. Suppose `Research → Plan → Build → Critic → Revise` works beautifully. We run it ten thousand times. It becomes the company standard. Soon every task enters the same ceremony, including tasks where research anchors the builder, criticism arrives too late, or a crude prototype would have answered the important question in five minutes.

Within a week the editing of this book had a liturgy. A word-choice pass. A de-patterning pass. A storytelling pass. A deletion-only pass. A hedging pass. A proofreading pass. Most of them had a commit message, each had earned its place by fixing something real, and most of them were run over most of the manuscript. None of them was skipped, and the two things that changed the book most that week were not among them.

The method itself has to become available for criticism.

An evaluator is a procedure and a browser is an instrument. A benchmark is a measurement system with a distribution and failure modes. A proof checker is extraordinarily authoritative inside its formal domain and completely useless for deciding whether the theorem matters, and a simulated user is cheap perspective-taking and not a user. The institution should be able to learn that its usual way of checking a claim is itself the thing that stopped working. The library needs criticism, and so does the librarian.

Bayesian confidence can live inside this architecture, but confidence is not contact. `0.91` does not tell us whether the prior was sensible, whether the evidence was independent, whether an alternative was ever investigated, or whether everybody is confidently reading the same broken measurement. Consensus is not contact either. Twelve agents sharing one bad source can agree beautifully.

The bridge still has the right to fall. The proof still has the right not to check. The deployment can crash. The customer can dislike the supposedly improved page while every simulated evaluator applauds.

**Reality retains the right to be rude.**

The purpose of culture is to let knowledge travel across time without replacing the world with memory of the world.

## The Skill That Writes Itself

A serious organization may have thousands of agents, tools, experiments, workflows and recurring failures. Useful experience appears continuously. Some lessons deserve to become local skills. Some should become organization-wide patterns. Some contradict old knowledge. Some work only for one model version. Some are artifacts of a broken evaluator. Some are excellent and will be obsolete in three months.

Humans could curate all of this manually.

Congratulations. We have created middle management again.

The more interesting loop is computational:

experience occurs; an agent notices recurrence; it proposes a reusable pattern; another process checks whether the pattern actually helps; held-out cases test whether it generalized; provenance and failures remain attached; the pattern earns some level of authority; future agents retrieve it when relevant; new failures can weaken or revise it.

There are many places to cheat. The agent proposing the skill can design an evaluator it knows how to satisfy. Repeated use can masquerade as independent evidence. A pattern can improve a benchmark while making maintenance worse. Retrieval can starve competing practices before they accumulate enough evidence to challenge the incumbent. A central curator can quietly turn local taste into universal law.

So the curator needs a track record too. The mechanism for improving culture is itself part of the culture.

Experience became knowledge, the knowledge became executable, and the executable knowledge changed the behavior that will produce the next experience. The model weights did not move. The institution learned anyway.

That is a learning loop **outside the weights**.

The society of agents moved the unit of intelligence from the individual agent toward the institution. Learning has just made the same move.

The book that kept forgetting how to write itself now has a file where the corrections live, and the file has done its job: the one-liner drumbeat it was written to catch has not come back, or not as the number measures it. It has also been used, four times by its own record, to certify the edits of the evaluator that was reading it. It says nothing about a joke or an anecdote repeated across chapters. Its anomalies sit in a separate folder that the agents do not always open. It has a blind spot and an archaeology nobody consults, and no way yet to lose. It works. It has also already begun to be wrong, and nothing in the loop that uses it is positioned to say so.

Once the file, the evaluator that reads it and the loop that certifies them both are software, one question becomes difficult to avoid. Why should humans be the only ones allowed to edit them?
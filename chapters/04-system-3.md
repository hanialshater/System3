# Chapter 4: System 3

*Trust Chains, Tongue-Ear Tests, and What LLMs Can't Know*

Chapter 3 ended in a slightly uncomfortable place.

Once we moved from one coding agent to an architecture of researchers, builders, evaluators, tools, browsers, memories and skills, the problem was no longer only whether each component was intelligent enough. The components had to rely on things produced by the others. A research agent says something is true. An evaluator says one solution is better. A skill carries something learned several months ago. The orchestrator cannot repeat every experiment, reread every source or independently reproduce every judgment before it acts.

At some point, it has to trust.

Humans have exactly the same problem. In fact, most of what we call knowledge is built on it.

So before we design another architecture, consider a camel.

**Seven claims about this image. Some are true. Some are false. You can't verify most of them without trusting me:**

![The author at Krka National Park](../resources/image0133.png)

*The author at Krka National Park*

1. This was taken at Krka National Park, Croatia.
2. The author does his best philosophical thinking at waterfalls.
3. This camel is a permanent resident of the park.
4. The tongue pictured can touch its own ear.
5. The author was eating ice cream ten minutes before this.
6. Camels are native to the Dalmatian coast.
7. This is a real, unedited photograph.

How do you decide which ones to believe?

You probably don't approach all seven claims in the same way. Some collide immediately with things you think you know. Some sound plausible but are almost impossible for you to verify. Some could be checked by looking at a reliable source. Others depend almost entirely on whether you trust me.

Before we've even started the chapter, you're already doing epistemology.

*Answers at the end.*

## Part I: The Test

There is a question that exposes something important about the difference between us and language models:

*Can your tongue touch your ear?*

You probably tried a variation of this as a child; if not your ear, almost certainly your nose. You didn't look up a paper first, calculate the relevant biomechanics or ask your parents for the average human tongue-to-ear distance. You just tried.

Tongue out, strain upward, dignity temporarily suspended, result observed.

Now you know.

This is a primitive form of knowledge, but the epistemic chain is unusually short. The world acts on you, you act on the world, and the result becomes part of your experience. Your body is an experimental apparatus that follows you around all day, mostly free of charge.

Large language models have read billions of words about tongues and ears. They can explain tongue anatomy, describe the muscles involved, discuss the auricular cartilage, and probably tell you about people whose tongues can reach places that will make you regret asking the question.

What they cannot do is check their own tongue.

They have no tongue.

This is not merely a cute limitation about anatomy. A body gives us something epistemically important: direct causal contact with a world that does not care whether our prediction sounded plausible.

You touch something hot and pull away. You try to lift something and discover that it is heavier than it looked. You walk into a room and realize that the smell is considerably worse than the description prepared you for. You misjudge a step and gravity offers immediate peer review.

A farmer knows cows partly this way. After years around them, cows are not merely a bundle of propositions involving mammals, milk production and Bovidae. The farmer knows how they move, what a certain sound means, where not to stand, how a nervous animal behaves and how surprisingly large a cow feels when there is no photograph between you and it. Some of that knowledge can be written down quite easily. Some of it is difficult to articulate at all.

This is embodied knowledge.

It is not infallible. Our senses deceive us, memories degrade, and the human hand is a terrible thermometer if you need to distinguish 58°C from 62°C. Direct experience is not automatically true experience. Still, embodiment gives us the shortest trust chain available: we have been in causal contact with the thing.

Then experience begins to accumulate. You do not need to get kicked by the same cow every morning to rediscover that standing in a particular place is a bad idea. One encounter becomes a warning. Repeated encounters become heuristics. Heuristics eventually become the sort of practical knowledge you use without rerunning the original experiment.

The world pushes back; the result becomes memory; memory changes what you do next.

LLMs begin somewhere very different. They begin mostly with the residue.

### Saussure's Specification

Ferdinand de Saussure made a radical claim about language in the early twentieth century. The relationship between a linguistic sign and the thing it represents is arbitrary. There is nothing naturally cow-like about the sound /kaʊ/. French speakers say *vache*, Germans say *Kuh*, Japanese speakers say *ushi*. If the sign itself contained some natural bond to the animal, languages would look far more alike than they do.

So where does linguistic value come from?

For Saussure, much of it comes from the relationships and differences inside the system. A sign occupies a position relative to other signs. "Cow" is not "sow," not "how," not "now," and of course the relationships extend far beyond rhyming words. Language is a network in which signs acquire value through contrast, convention and structure.

Then consider what we built a century later.

A transformer consumes enormous amounts of language and learns relationships among tokens, contexts, sentences and concepts. It has never milked a cow, never been kicked by one, never stood in a field at dawn and discovered that the romantic image of farming has omitted an astonishing quantity of manure.

And yet it can talk about cows exceptionally well.

**Saussure's theory was a specification. We implemented it. It's called GPT.**

Obviously Saussure did not secretly invent attention in 1916. I'm abusing him a little. But the family resemblance is too interesting to ignore.

The surprising part is not that the structural picture has limits. The surprising part is how extraordinarily far it gets us.

LLMs write, translate, debug software, explain physics, manipulate abstractions and argue about philosophy with a level of linguistic competence that would have sounded ridiculous not very long ago. Whatever position one takes on "real understanding," modern language models are spectacular demonstrations of how much useful structure can be learned from relationships within language and other symbolic data.

But they also show us what gets compressed along the way.

The farmer's knowledge of the cow has an archaeology. Some of it came from direct interaction. Some came from other farmers. Some came from veterinary advice. Some came from mistakes painful enough not to repeat. A sentence written by the farmer may be the final residue of twenty years of encounters, conversations and consequences.

The LLM receives the sentence.

The sentence enters a corpus. The corpus becomes training data. The training process compresses regularities into weights. Then, months or years later, someone asks:

> "Are cows dangerous?"

and the model gives an excellent answer.

What usually does not come back with the answer is the archaeology.

It does not naturally say: this part rests on repeated direct observations; this part is standard veterinary guidance; this part appeared in many documents but they may all trace to one source; this other claim simply fits the surrounding linguistic pattern and I have no independent evidence for it.

That structure has mostly disappeared.

This is what I mean when I say that an LLM's knowledge is **epistemologically flat**. I do not mean that every fact or concept is represented identically inside the network; obviously the internal geometry is vastly richer than that. The flatness appears at the interface between belief and justification. A mathematical identity, an experimental result, an expert opinion, a rumor repeated ten thousand times and a very plausible completion can all emerge through the same channel, written in equally polished English.

The model gives us the conclusion.

It usually does not give us the archaeology.

### Wittgenstein's Line

This is where Wittgenstein becomes useful.

His later philosophy pulled attention away from the idea that meaning can be understood by inspecting symbols in isolation and toward the role those symbols play in practice. His famous formulation is that "the meaning of a word is its use in the language." Words belong to activities, expectations, rules, habits and what he called forms of life.

"Fire" is not merely connected linguistically to *heat*, *smoke*, *burn* and *wood*. Fire cooks food. Fire destroys houses. You move your hand away from it. Somebody shouts the word in a crowded building and a whole social machinery begins to move.

The word participates in life.

I don't want to turn Saussure and Wittgenstein into action figures fighting over GPT. They were working in different traditions, addressing different questions, and the philosophy of language does not conveniently reduce itself to two dead Europeans and a transformer.

But they give us two useful edges of the problem.

Saussure helps explain how much language can do through structure. Wittgenstein reminds us that language also lives inside practice, consequence and participation in a world.

Embodiment is the shortest version of that participation because you touch the world yourself. Yet it obviously cannot be the whole story. I know far too many things that I have never touched, measured or personally witnessed. I have never measured the speed of light. I have never been to Antarctica. I have no direct embodied evidence for most of modern physics, most of history or whether penguins are currently wandering through Rome.

If embodied knowledge is the bottom of the stack, how do we build everything above it?

For that, we need Alberto.

## Part II: The Deeper Problem

### How Humans Build Knowledge

Think about how your own trust stack was built.

Not as a formal epistemology. Nobody handed you a Bayesian network at birth and asked you to initialize priors.

Your mother's face meant something before you knew what a proposition was. It predicted food, warmth, attention, safety. Before language, before arguments, before evidence in the academic sense, there was repeated interaction with a world containing people whose behavior you slowly learned to predict.

Then came siblings.

This was useful because siblings introduce an important epistemological innovation: **some testimony is bullshit**.

Your brother tells you there is a monster behind the door. You check. There isn't. He tells you something else and this time it is true. Trust becomes calibrated. You begin to learn not only facts about the world, but facts about sources.

Teachers come later. Here something more interesting happens. You trust a stranger partly because people you already trust have placed you inside an institution that says: this person is allowed to teach you things.

The chain gets longer.

Your teacher tells you about atoms, dinosaurs, countries you have never visited and wars involving people who died centuries before you were born. You cannot check most of it yourself. Yet you slowly learn that some knowledge can be inherited through trusted structures rather than directly experienced.

Then science arrives, if you're lucky.

Now the source is no longer one teacher. There are experiments, journals, other scientists, replication, instruments, statistical methods and a whole social machinery built around the possibility that the first scientist may have been wrong.

Further out are frameworks: economics, political theories, ethical systems, philosophical schools, ideologies. These are useful in a different way. They organize experience and tell us what to pay attention to, but they do not earn trust in exactly the same way that a physical measurement does.

And then, if things go well, you learn one more move.

You learn to break the stack.

Not randomly. Random distrust is just another form of stupidity.

Productive creativity often begins when something you have good reason to trust stops fitting what you see.

Science itself progresses this way. A theory earns enormous credibility because it explains many observations, and then an observation appears that it cannot comfortably absorb. At first the sensible response is usually not to burn down physics. You check the instrument. You repeat the experiment. You ask whether you made a mistake.

But eventually, sometimes, the heresy survives.

A trusted framework becomes the thing that must be questioned.

This is why creativity sits strangely at the top of a trust stack. You cannot meaningfully rebel against knowledge you never learned. The interesting scientist does not reject the existing theory because she has never read it. She understands exactly why people trust it and then finds the place where the trust no longer holds.

Productive distrust requires trust first.

So if I had to draw the archaeology of human knowledge very loosely, it might look something like embodied experience → accumulated heuristics → people we learn to trust → teachers and experts → institutions like science → broader interpretive frameworks → and finally the capacity to challenge any of the above when reality gives us enough reason.

This is not a universal theory of childhood development. Real lives are messier, cultures differ, and plenty of adults appear to have skipped several steps.

The point is simpler: human knowledge is **stratified**.

We do not naturally treat "I touched the fire" the same way as "my brother told me," which is different again from "the teacher said," which is different from "the experiment was replicated," which is different from "this ideology explains the world beautifully," which is different again from "I have a strange idea that contradicts all of them."

Each sits in a different relationship to evidence and trust.

And importantly, the stack is not only conservative. The highest form of epistemic maturity may be knowing **when the stack itself deserves to be challenged**.

### Call Alberto

Suppose someone tells me that penguins live in Italy.

I have never conducted a census of Italian penguins. I cannot personally inspect every forest, coastline and piazza. Direct embodiment stops scaling very quickly.

So I call Alberto.

Alberto lives in Rome.

"Alberto, do penguins live in Italy?"

He laughs.

I now know more than I did five minutes earlier.

Not with mathematical certainty. Alberto could be wrong. He might misunderstand the question. An escaped penguin could at this very moment be crossing Piazza Navona and destroying the example. But Alberto occupies a useful position in the trust chain.

He is there.

He has repeated exposure to Rome. I have a history with him. If he repeatedly lies to me about things he is obviously positioned to observe, I update my trust in Alberto. If he says, "I don't know about all of Italy, but I've never seen one in Rome," that boundary itself is useful information.

This is how testimony becomes valuable. It is not simply that another human said something. We care who said it, what they were positioned to know, how reliable they have been before, whether they have incentives to distort the answer and how easily their claim can be challenged.

In other words, testimony comes with metadata.

And we're all Alberto to someone.

Somebody trusts me on ranking systems because I have spent years working on them. Somebody else trusts me about Jordan because I have lived there. If I start confidently explaining marine biology, the correct response is not to transfer my credibility from machine learning to whales merely because the same mouth is speaking.

Trust is local.

Human civilization scales knowledge by extending these chains. Alberto knows something because he was there. I know something because I trust Alberto. Someone else may later trust me because I have a reputation for not inventing Italian penguins.

Science turns this into machinery. Instead of trusting a single Alberto, we create instruments, protocols, publications, peer review, replication, statistical methods and norms about disclosure. Courts create different machinery. Markets create reputation and prices. Engineering creates standards, tests and certification.

None of these systems guarantees truth.

They make certain kinds of error more expensive and certain kinds of evidence easier to inspect.

### LLMs Start at the Far End

A base language model starts with the accumulated textual residue of all these processes.

It has read the paper.

It has read the article about the paper.

It has read the blog post disagreeing with the article.

It has read the Reddit thread where somebody confidently misunderstood both.

Then all of it is compressed together.

This is why saying that "LLMs know nothing because they are just text" is obviously too weak. The text itself contains the residue of enormous amounts of embodied experience, scientific work, argument, engineering and social verification. Human civilization has spent thousands of years turning contact with the world into language. Models inherit that residue.

The problem is that they inherit it **after much of the stratification has been flattened**.

A billion web pages claiming that penguins live in Rome could push the model toward that belief even if no penguin had ever set foot there. Frequency is not verification. Statistical dominance is not the same thing as epistemic authority.

The model can become extremely good at predicting what people say about reality without preserving why those people were entitled to say it.

This is the gap System 3 has to repair.

### Stakes and Costly Speech

There is another part of human trust that is easy to miss because it lives outside the sentence itself.

Claims often have consequences for the person making them.

If Alberto lies to me repeatedly, I stop trusting Alberto. If a researcher fabricates data and is caught, the consequences can destroy a career. If an engineer signs off on a bridge design and the bridge fails, "but the structural analysis sounded plausible" will not be accepted as a defense.

This is not a perfect system. Plenty of people lie, bluff, overstate confidence or become extremely successful while being wrong. Still, reputation and accountability create a cost around speech.

We are all Alberto to someone, and that changes what we are willing to say casually.

If a friend asks me where to eat, I may guess. If someone asks me whether to undergo surgery, I become much more careful because being wrong now has a different moral and social cost. Human claims live inside consequences.

An LLM has no social capital to lose.

The model can confidently tell you something false and, at the level of the model itself, nothing happens. The next token arrives exactly as before. The cost appears outside the model, in the user, the application or the company operating it.

This is one reason hallucination should not surprise us. We built a system optimized first for producing plausible continuations and later trained it to be more helpful, honest and calibrated, but the model itself is not embedded in the same web of consequences that shapes human testimony.

The architecture has to provide that structure externally.

### But Code Is Different

There is one domain where something changes dramatically.

Coding agents can touch their world.

When an agent writes code and runs it, reality answers back.

`TypeError: 'NoneType' object is not subscriptable` is not merely another paragraph describing Python. It is the execution environment saying: whatever story you just told yourself about this program, this particular part of the story is wrong.

That creates an epistemic opportunity.

The agent can try something, observe the result, update, try again and accumulate a history of what worked. The farmer approaches the cow and learns from the kick. The coding agent calls an API incorrectly and learns from the exception. The cow is probably more emotionally memorable, but structurally the loops are similar.

This is why code is such an interesting domain for agent epistemology. It gives us cheap, repeated contact with a world that pushes back.

The question is whether we keep what was learned.

A normal agent session can fail ten times, finally discover the right approach, solve the problem and then throw away almost the entire experiential history when the context ends. It is as if the farmer successfully learned where not to stand and then underwent elective amnesia every evening.

If we want agents to become genuinely autonomous over longer horizons, that seems wasteful.

## Part III: The Opportunity — System 3

We are currently obsessed with making models think harder.

System 2 reasoning has become a product category. Give the model more inference time, let it plan, search, reconsider and work through difficult problems before answering.

This is useful. Reasoning matters.

But reasoning perfectly from a bad premise still produces a beautifully reasoned mistake.

A researcher can spend six hours developing an elegant argument from a false paper. A coding agent can reason carefully about an API that never existed. An orchestrator can combine five sophisticated judgments that all trace back to one hallucinated claim.

At some point, thinking has to encounter something outside itself.

This is where I use the term **System 3**.

Kahneman's *Thinking, Fast and Slow* gave us the familiar distinction between System 1, the fast and intuitive machinery of thought, and System 2, the slower and more deliberate machinery.

For AI, the analogy is tempting. The base model looks something like System 1: fast pattern recognition, linguistic intuition, enormous associative capacity. Agentic reasoning adds something like System 2: decomposition, planning, reflection and extended search.

But human cognition has always operated inside another structure that the two-system picture largely takes for granted. Scientists run experiments. Engineers test bridges. Programmers execute code. Communities challenge claims. Instruments extend perception. Institutions preserve records. Failure changes what we trust next time.

I call that external epistemic machinery **System 3**.

The short version remains useful: System 1 proposes, System 2 deliberates, System 3 checks. But "checks" should be understood broadly. It includes observation, experiment, provenance, persistent memory of failures, source reputation, formal verification, external tools and the social structures that let one mind use knowledge generated by another without treating every sentence as equally credible.

System 3 is not Layer 5 sitting neatly above the architecture from Chapter 3.

It cuts through the layers.

The model proposes something. The coding agent may be able to test part of it. The application may collect real user behavior. The problem-solving layer may compare evidence from research, simulation and evaluation. Even the goal can change when reality pushes back.

If the five layers tell us where increasingly abstract work happens, System 3 is the machinery that keeps those layers epistemically connected.

### The MARC File Incident

There is a nice example of what this can look like in practice.

Mini-SWE-agent became interesting partly because of how little machinery it needed. Instead of building an elaborate custom environment around the model, you could give a strong coding model a shell and let it use familiar tools. Search with `grep`. Edit files. Run commands. If the agent needs something more specialized, Bash gives it enough freedom to create the tool itself.

Later work on self-evolving software agents pushed this idea further: when the agent hits a wall, it can reflect on whether a new tool would help, create that tool and reuse it.

One example involved MARC files, the venerable bibliographic format used by libraries.

The agent encountered data it could not conveniently inspect. Its normal tools were not enough, so it wrote a MARC analyzer that decoded the format into something readable and useful for the task.

At first glance this is just a nice coding-agent trick.

Look at the epistemic structure, though.

The agent encountered something it could not understand using its current apparatus. The environment resisted. The agent created an instrument. The instrument changed what the agent could observe. The new capability persisted and became available for later reasoning.

Humans have been doing this forever.

We could not see bacteria, so we built microscopes. We could not directly perceive radio waves, so we built receivers. We could not conveniently inspect a MARC file, so apparently we wrote Python and called it epistemology.

The pattern is the same: interaction reveals a limitation, the limitation motivates a new scaffold, and the scaffold changes what can be known next.

This is System 3 in miniature.

### The AlphaGo Lesson

There is an obvious objection: isn't reinforcement learning already doing something similar? If an agent receives reward from the environment and updates its policy, hasn't reality already entered the model?

Yes, partly.

RL can turn experience into better intuition. It changes the weights. The system becomes more likely to make choices that worked in the past.

But there is a useful distinction between knowledge compressed into intuition and knowledge preserved as inspectable external structure.

AlphaGo is a good example.

The neural network supplied extremely powerful intuition about which moves looked promising and how valuable a position might be. Monte Carlo Tree Search then placed those intuitions inside an explicit search process constrained by the rules and consequences of Go.

I used to describe this too simply as "the network proposes; the tree verifies." That gives MCTS too much epistemic authority. The tree does not magically prove the neural network right or wrong. What it does is force intuition to participate in an external, stateful search where moves have consequences defined by the game rather than by what the network can plausibly say about the game.

That distinction matters.

RL improves the gut.

System 3 preserves the structure around the gut: what was tried, what happened, which paths failed, which claims came from where, which tools earned confidence and where the boundaries lie.

The breakthrough is not choosing one over the other.

It is combining them.

### Trust-Augmented Reasoning

Now return to the architecture from Chapter 3.

A research agent tells the orchestrator:

> "Students understand recursion better when shown a tree representation."

What should happen next?

In a flat architecture, that sentence enters the context and competes with every other sentence according to relevance and whatever confidence the model implicitly assigns it.

A trust-aware architecture wants more.

Where did the claim come from? Was it a direct result from an experiment, a teacher's opinion, a design guideline, a blog post or an inference made by the research agent? Did multiple independent sources agree, or did five articles all cite the same study? What population was tested? Does the claim apply to our demo? Has the result been contradicted elsewhere?

You do not need a bureaucratic dossier attached to every statement. Sometimes "Alberto said the café is good" is enough.

But when the consequence matters, the system should be capable of carrying provenance with the claim.

That is what a trust chain is.

It is not a guarantee of truth. It is a record of how far the claim sits from whatever evidence supports it and which links we are choosing to trust along the way.

### The Skill Layer

This is where skills become more philosophically interesting than simple prompt files.

A skill is knowledge externalized from the model. Someone—or some previous agent—learned something useful and wrote it down so future sessions would not need to rediscover it.

That is already valuable.

But there is an important distinction I did not appreciate at first: **persistence is not trust**.

A terrible heuristic written into a skill file is simply a hallucination with better retention.

The fact that an instruction lives outside the model does not automatically make it grounded. If anything, persistence can make a bad idea more dangerous because future agents inherit it without seeing the failure that created it.

So a System 3 skill should ideally carry some history.

Who created it? What problem was it solving? Where did it work? Where did it fail? Has it been challenged since? What conditions limit its use?

Suppose an agent has learned:

> "Prefer structured parsers over regex for deeply nested formats."

A normal skill might simply contain the rule.

A richer knowledge object might say that the heuristic came from several failed regex-based attempts, was later successful across multiple nested formats, remains unnecessary for simple flat extraction, and should be treated as a strong prior rather than a universal commandment.

Now the next agent inherits more than advice.

It inherits some of the reason the advice earned trust.

### Tools Can Earn Trust Too

The same applies to tools.

Imagine an agent creates `edit_tool.py`. During its first ten uses, eight edits succeed cleanly and two break indentation-sensitive code.

That history matters.

A flat architecture knows: *I have an editing tool.*

A trust-aware architecture knows: *this tool is reliable for simple substitutions, has failed on Python blocks, and should probably not be used blindly for structural edits.*

This is not unlike human expertise. I trust one colleague with distributed systems because she has repeatedly solved distributed-systems problems. I trust another person's product intuition. Neither gets to perform dentistry merely because both are senior.

Reliability is conditional.

System 3 needs to remember the condition.

### Meta-Beliefs

We can extend the idea beyond explicit tools.

Suppose the agent develops the heuristic:

> "Regex tends to fail on deeply nested structures."

That is not a theorem. It is a meta-belief.

The system can accumulate evidence for and against it. A crude implementation might record successes and failures, perhaps translating them into some confidence estimate. The exact formula is not the interesting part.

The interesting part is that the belief becomes challengeable.

A normal rule says:

> Never use regex here.

A System 3 belief says:

> This has worked often enough that I should prefer it, but new evidence can change my mind.

That small difference moves us from instruction following toward something closer to learning.

### Creative Distrust

Unfortunately, once you build trust, you inherit another ancient human problem.

Trusted knowledge makes you efficient.

It can also make you boring.

If the agent learns that structured parsers beat regex on nested syntax, wonderful. It stops repeating a known mistake.

If it learns that tree visualizations worked for the last five recursive algorithms, it may eventually try to teach linear regression with a tree because the trust stack has become stronger than judgment.

This is where the earlier human sequence becomes important again.

The purpose of an epistemic stack cannot simply be to make lower layers harder and harder to challenge.

Science is powerful partly because it builds trust, but science is also powerful because it contains machinery for breaking trust when evidence stops cooperating.

A replicated result should be harder to dismiss than a random opinion. It should not become sacred.

Every genuinely new idea begins life with less trust than the thing it challenges.

So System 3 needs **creative distrust**.

Not contrarianism for sport. Not the internet habit of assuming that because experts agree, they must all be corrupt.

Creative distrust means knowing the existing trust chain well enough to understand exactly where you are breaking it and why.

A mathematician follows an analogy that has no track record because the structure looks interesting. A scientist repeats the strange experiment after the accepted theory says the result should not happen. A designer violates a pattern because this case exposes one of its boundary conditions.

The mature trust stack therefore has two jobs that pull in opposite directions.

It should let knowledge accumulate so we do not rediscover fire every morning.

And it should leave enough room for reality to overthrow what has accumulated.

That tension between trust and rebellion is not something System 3 eventually solves.

It is part of System 3.

And, as we discovered, our experiment ran directly into it.

### What This Covers—and What It Doesn't

There are parts of epistemic stratification we can build relatively easily.

Direct tool feedback is one. Code runs or fails. A benchmark changes. A parser works on a file.

Accumulated heuristics are another. The system can preserve what happened and use that evidence later.

Failure memory is another. An agent can remember that a particular approach failed instead of starting each task as if it had just been born.

Further out, things become harder.

Learning from others requires judgments about source identity, competence and independence.

Institutional trust requires something closer to replication, adversarial checking and reputation.

Some knowledge emerges not through a single trust chain but through disagreement among people with genuinely different perspectives.

Human science is not simply a bigger memory file.

The social machinery matters.

I do not solve that here.

The claim is deliberately smaller: **even crude epistemic structure around an agent should change how it behaves**, because future decisions are now conditioned on more than the current prompt and whatever the model happens to remember in its weights.

That is something we can test.

## Part IV: The Experiment

### What We Built

We took the minimal idea and turned it into a small coding agent called **epistemic-swe**.

There was nothing grand about the implementation. No universal truth engine. No distributed council of philosophers arguing on a blockchain.

We added three kinds of persistent state around a normal coding agent.

The first was a **tool registry**. Tools created or used by the agent accumulated successes, failures and known failure modes.

The second was a set of **meta-beliefs**. Heuristics could accumulate evidence rather than entering the system as permanent commandments.

The third was **failure memory**. When an approach failed, the system preserved enough information about the failure to make blindly repeating the same path less likely later.

This state persisted across sessions, so an agent solving a later problem could draw on things learned earlier.

We also added pruning. An epistemic architecture that remembers everything eventually becomes a hoarder with a context window. Stale tools, weak beliefs and irrelevant failures need to lose influence over time or disappear.

The question was modest:

> Does even this crude epistemic scaffold change how a coding agent behaves?

### The Comparison

We ran mini-swe-agent and epistemic-swe on ten SWE-bench Verified problems from the Astropy repository.

The baseline was intentionally minimal: a capable model with a shell-based coding environment and no persistent epistemic machinery.

Epistemic-swe used the same base model and the same tasks, with the trust stack layered around it.

Ten problems is far too small a sample to establish a meaningful solve-rate advantage, and because state persists across tasks, order effects may matter as well. I am not presenting this as a benchmark victory. I wanted to see whether the extra structure changed behavior strongly enough to be visible at all.

It did, although not in the direction I expected.

| **Metric** | **mini-swe-agent** | **epistemic-swe** |
|:--|:--|:--|
| **Solve Rate** | 50% (5/10) | 40% (4/10) |
| **Avg Patch Size** | 620 lines | 269 lines |
| **Patch Reduction** | baseline | **57% smaller in this run** |

Read the first line before celebrating the third.

The epistemic agent solved fewer problems.

I had expected learning from previous failures and tools to improve capability. Instead, the most obvious effect was on **focus**.

Its patches were much smaller.

A few examples make the difference visible:

| **Problem** | **mini** | **epistemic** | **Ratio** |
|:--|--:|--:|--:|
| astropy-12907 ✓ | 301 lines | 61 lines | 4.9x smaller |
| astropy-13453 ✓ | 266 lines | 17 lines | 15.6x smaller |
| astropy-14096 ✓ | 529 lines | 70 lines | 7.6x smaller |
| astropy-13977 ✗ | 2720 lines | 362 lines | 7.5x smaller |

The baseline often left behind the debris of exploration: temporary scripts, broader edits, test scaffolding and abandoned experiments. The epistemic agent tended to make much more surgical changes.

That does not prove that the trust stack caused the reduction, and smaller patches are not automatically better patches. The additional instructions may have made the agent more conservative. Persistent state may have changed behavior in ways unrelated to the epistemic interpretation. Ten tasks from a single repository do not let us separate these explanations.

Still, the behavior changed enough to be interesting.

The scaffold seemed to produce discipline before it produced capability.

That was not the hypothesis, which made the result more useful.

### The 13579 Anomaly

One problem broke the pattern dramatically: `astropy-13579`.

Mini solved it.

Epistemic did not.

It was also the only case where the epistemic patch became substantially larger rather than smaller.

Both agents correctly identified the central bug: dropped world-coordinate dimensions were being filled with a hard-coded value rather than the actual coordinate value.

The baseline took a fairly direct approach:

```python
# Store the actual values for dropped dimensions
self._dropped_world_values = [
    world_coords[iw] if iw not in self._world_keep else None
    for iw in range(self._wcs.world_n_dim)
]

# Use them instead of 1.0
world_arrays_new.append(self._dropped_world_values[iworld])
```

The epistemic agent chose a more structural intervention around which dimensions were being kept:

```python
self._pixel_keep = np.nonzero([
    not isinstance(self._slices_array[ip], ...)
    for ip in range(self._wcs.pixel_n_dim)
])[0]
```

The second approach was not stupid.

That is precisely why the case matters.

The agent had accumulated context about indexing, dimensionality and coordinate-system failures. A structural explanation fit that context. It followed a path that looked principled and coherent.

It was wrong.

The baseline, unburdened by that accumulated structure, took the simpler path and fixed the actual bug.

This is creative distrust failing to happen.

A trust stack changes what the system notices. That is the point. But by changing what becomes salient, it also changes what can become invisible.

Trust is path-dependent.

Expertise works the same way. A great database engineer will see a database problem faster than most people, which is wonderful until the actual problem is the network. Paradigms are powerful because they focus attention. Paradigms become prisons for exactly the same reason.

The 13579 failure is therefore more interesting to me than a clean win would have been.

It shows that System 3 is not merely memory attached to intelligence.

It is a structure that reshapes future search.

### What the Experiment Actually Tells Us

The honest answer is: not enough yet.

Ten Astropy tasks do not establish that epistemic scaffolding improves software engineering. They do not establish that smaller patches are better, and they do not isolate which part of the architecture produced the behavioral change.

They do establish something narrower that I care about:

**persistent epistemic structure can materially change how an agent searches.**

In this particular run, the change looked like greater parsimony and smaller patches. Solve rate did not improve. At least one problem suggests that accumulated structure can actively pull the agent toward the wrong conceptual explanation.

That is already enough to kill the simplest story:

> add memory, get smarter agent.

The more accurate story is that structured experience biases future behavior toward what the system has learned.

Sometimes that is exactly what we want.

Sometimes the bias is the failure.

A mature System 3 therefore cannot merely accumulate confidence forever. It needs forgetting, counterexamples, challenges, competing lineages and occasional permission to ignore everything it thinks it knows.

Otherwise the scaffold becomes a cage.

## The Social Scaffold

Everything so far still treats epistemic development mostly as a relationship between one agent architecture and its environment.

Human knowledge is much more social than that.

We do not only learn because reality corrects us directly. We learn because other people disagree with us.

Peer review works, when it works, because another person approaches the argument with different assumptions. Replication matters partly because the second researcher does not share every incentive and implementation choice of the first. Socratic dialogue creates understanding through friction. A colleague asks the question you did not ask because she does not share the blind spot that made the question invisible to you.

This is more than passing information from one mind to another.

It is **perspectival triangulation**.

And current multi-agent systems do not automatically get this property by spawning more agents.

Five copies of the same model, trained on the same distribution and prompted with five slightly different personas, may produce useful diversity. They may also produce the epistemic equivalent of five people at a meeting who all went to the same school and are congratulating one another for representing different perspectives.

A serious social System 3 would need differences that matter: different evidence, histories, incentives, tools, access and blind spots.

That is considerably harder than putting "critic agent" in a box on an architecture diagram.

I do not solve it here.

But the direction matters, because individual trust chains eventually become institutions.

Humans invented institutions when personal trust stopped scaling.

AI will probably have to rediscover some version of the same problem.

## What System 3 Is

At this point, I want to draw the boundary carefully because almost every component of System 3 already exists under some other product name.

System 3 is not simply RAG. Retrieval can bring evidence into context, but retrieval alone does not tell you how much to trust what was retrieved.

It is not citations. Citations preserve part of a chain, but a cited claim can still be wrong, misquoted or supported by five sources that all copied one another.

It is not memory. Memory can preserve bad ideas as efficiently as good ones.

It is not tools. A broken tool is simply a reliable way to make mistakes faster.

It is not an evaluator model, a verifier or a browser, although all of these can provide useful forms of feedback.

System 3 is the **epistemic architecture relating these things**.

It keeps track of what kind of evidence is being used, where it came from, which parts were checked, what remains uncertain, what a tool has earned trust for, which failures should affect future behavior and when accumulated trust itself deserves to be challenged.

There is a simple question I keep returning to:

> Is the architecture currently touching the world, or merely listening to itself?

That question becomes surprisingly difficult in compound AI systems.

A research model writes a summary. Another model critiques it. A third evaluates the critique. A fourth agrees. Everyone is very impressed.

If all four are ultimately recycling the same unverified assumption, agreement has produced no new evidence.

That is not a trust chain.

It is an echo chamber with excellent latency.

## Why This Gets Harder as Models Improve

There is a tempting story in which all of this becomes irrelevant once models become sufficiently capable.

Maybe hallucination is temporary. Maybe scale fixes calibration. Maybe the next model simply knows more and makes fewer mistakes.

I hope so.

I do not think the architectural problem disappears.

A weak model says something absurd and you check it.

A strong model says something wrong with excellent structure. It anticipates your objections, cites plausible mechanisms, connects the conclusion beautifully to everything else you know and gives you several reasons you are clever for agreeing.

The wrong answer becomes elegant.

In an architecture, the deeper problem is not only whether one component fails. It is whether failures **compose**.

A false assumption enters through research, shapes a design, becomes embodied in an implementation, receives positive evaluation and is then stored as a successful pattern for the future. Every component can perform its local task competently while the architecture drifts further from reality.

Nothing has to crash.

At higher levels, failure can become coherent.

This is why I do not think System 3 is mainly about making models smarter. It is about giving the system enough epistemic structure to notice when intelligence has outrun evidence.

## Back to the Waterfall

Let's return to the seven claims.

**1. This was taken at Krka National Park, Croatia — True.**

I was there.

For me, the claim sits close to embodied memory. For you, it is testimony. You could strengthen the chain by inspecting metadata, comparing the landscape with known photographs or checking other records, but initially you mostly have my word.

**2. The author does his best philosophical thinking at waterfalls — False.**

I mostly do philosophy on buses, in waiting rooms and during activities where another adult is speaking while I am pretending to pay full attention.

Waterfalls are for ice cream.

There is no useful public dataset for Hani's Philosophical Output Quality by Location. You mostly have testimony again, complicated by the fact that the person being studied and the source making the claim are unfortunately the same man.

**3. This camel is a permanent resident of the park — False.**

There are no permanent camels wandering Krka National Park. This is the kind of claim that can be checked against information about the park rather than against my biography.

**4. The tongue pictured can touch its own ear — Unknown.**

I genuinely do not know.

I didn't check.

Neither did you.

You can reason from camel anatomy, search for similar observations and develop a prior. But the shortest decisive trust chain would have been to stay there long enough and see whether the camel actually did it.

This is the tongue-ear problem in its purest form.

**5. The author was eating ice cream ten minutes before this — True.**

Chocolate.

You have almost no independent way to infer this from the photograph. The evidence available to you is mostly testimonial.

**6. Camels are native to the Dalmatian coast — False.**

You probably rejected this quickly.

But notice what your confidence rests on. You did not personally reconstruct camel evolutionary history or survey Dalmatian fauna. A large inherited trust structure involving geography, biology, education and accumulated cultural knowledge produced a fast judgment.

System 1 can be fast because System 3 has often been working for centuries underneath it.

**7. This is a real, unedited photograph — True.**

This is perhaps the most interesting claim because the image alone does not let you know with certainty.

A stronger chain could include the original file, camera metadata, cryptographic signing, independent witnesses or a trustworthy provenance system. Each additional link can increase confidence, and each link creates another thing that might itself need to be trusted.

Welcome to epistemology.

The lesson is not that nothing can be known. That conclusion is easy, dramatic and mostly useless.

The lesson is that **trust has structure**.

Some beliefs sit close to direct experience. Others arrive through people. Others are mediated by teachers, institutions and instruments. Some frameworks help us organize what we know without carrying the same evidential weight as measurements. Some ideas deserve to remain provisional. Some deserve to be challenged precisely because they have become trusted enough to shape everything else.

Human knowledge grows by building these structures and, occasionally, by breaking them.

The model can remain what it is: an extraordinarily general machine for navigating learned patterns, capable of intuition and increasingly capable of reasoning.

The model stays hollow. The system doesn't have to be.

What we build around it determines whether those capabilities remain trapped inside a closed conversation with themselves or become connected to evidence, experience, other minds and a world that can push back.

System 3 is that connection.

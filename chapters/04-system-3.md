# Chapter 4: System 3

*Trust Chains, Tongue-Ear Tests, and What LLMs Can't Verify Alone*

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

You probably don't approach all seven claims in the same way. Some collide immediately with things you think you know. Some sound plausible but are almost impossible for you to verify. Some could be checked against a reliable source. Others depend almost entirely on whether you trust me.

Before we've even started the chapter, you're already doing epistemology.

*Answers at the end.*

## Part I: The Test

There is a question that exposes something important about the difference between us and language models:

*Can your tongue touch your ear?*

You probably tried a variation of this as a child; if not your ear, almost certainly your nose. You didn't look up a paper first, calculate the relevant biomechanics or ask your parents for the average human tongue-to-ear distance.

You just tried.

Tongue out, strain upward, dignity temporarily suspended, result observed.

Now you know.

This is primitive knowledge, but the epistemic chain is unusually short. The world acts on you, you act on the world, and the result becomes part of your experience. Your body is an experimental apparatus that follows you around all day, mostly free of charge.

Large language models have read billions of words about tongues and ears. They can explain tongue anatomy, describe the muscles involved, discuss auricular cartilage, and probably tell you about people whose tongues can reach places that will make you regret asking the question.

What they cannot do is check their own tongue. They have no tongue.

That sounds almost silly, but it marks an important difference. A body gives us direct causal contact with a world that does not care whether our prediction sounded plausible.

You touch something hot and pull away. You try to lift something and discover that it is heavier than it looked. You walk into a room and realize that the smell is considerably worse than the description prepared you for. You misjudge a step and gravity offers immediate peer review.

A farmer knows cows partly this way. After years around them, cows are not merely a bundle of propositions involving mammals, milk production and Bovidae. The farmer knows how they move, what a certain sound means, where not to stand, how a nervous animal behaves and how surprisingly large a cow feels when there is no photograph between you and it. Some of that knowledge can be written down easily. Some is difficult to articulate at all.

This is embodied knowledge. It is not infallible. Our senses deceive us, memories degrade, and the human hand is a terrible thermometer if you need to distinguish 58°C from 62°C. Direct experience is not automatically true experience.

But embodiment gives us something important: contact. The world can answer back.

Then experience accumulates. You do not need to get kicked by the same cow every morning to rediscover that standing in a particular place is a bad idea. One encounter becomes a warning. Repeated encounters become heuristics. Heuristics eventually become the sort of practical knowledge you use without rerunning the original experiment.

The world pushes back; the result becomes memory; memory changes what you do next.

LLMs begin somewhere very different. They begin mostly with the residue.

### Saussure's Specification

Ferdinand de Saussure made a radical claim about language in the early twentieth century. The form of a linguistic sign is not naturally determined by what it signifies. There is nothing naturally cow-like about the sound /kaʊ/. French speakers say *vache*, Germans say *Kuh*, Japanese speakers say *ushi*. If the sign itself contained some natural bond to the animal, languages would look far more alike than they do.

So where does linguistic value come from?

For Saussure, much of it comes from relationships and differences inside the system. A sign occupies a position relative to other signs. “Cow” is not “sow,” not “how,” not “now,” and of course the relationships extend far beyond rhyming words. Language is a network in which signs acquire value through contrast, convention and structure.

Then consider what we built a century later.

A transformer consumes enormous amounts of language and learns relationships among tokens, contexts, sentences and concepts. It has never milked a cow, never been kicked by one, never stood in a field at dawn and discovered that the romantic image of farming has omitted an astonishing quantity of manure.

And yet it can talk about cows exceptionally well.

**Saussure's theory was a specification. We implemented it. It's called GPT.**

Not literally. Saussure did not secretly invent attention in 1916, and structural linguistics is not a machine-learning architecture. The historical claim would be silly.

The architectural resemblance is the interesting part: modern language models demonstrate, on an extraordinary scale, how much useful competence can emerge from learning structure within symbolic data.

The surprising thing is how far that gets us. LLMs write, translate, debug software, explain physics, manipulate abstractions and argue philosophy with a level of linguistic competence that would have sounded ridiculous not very long ago. Whatever position one takes on “real understanding,” they are spectacular evidence that relational structure carries an enormous amount of information.

But the same success helps reveal what gets compressed along the way.

The farmer's knowledge of the cow has an archaeology. Some came from direct interaction. Some from other farmers. Some from veterinary advice. Some from mistakes painful enough not to repeat. A sentence written by that farmer may be the final residue of twenty years of encounters, conversations and consequences.

The model receives the sentence. The sentence enters a corpus. The corpus becomes training data. The training process compresses regularities into weights. Then, months or years later, somebody asks:

> “Are cows dangerous?”

and the model gives an excellent answer.

What usually does not come back with the answer is the archaeology. It does not naturally tell you which part rests on repeated observation, which part is standard veterinary guidance, whether five documents trace to the same original source, or whether another claim merely fits the surrounding linguistic pattern.

That structure is largely absent from the answer.

This is what I mean when I say an LLM's knowledge is **epistemologically flat**. I do not mean that every fact or concept is represented identically inside the network. The internal geometry is obviously vastly richer than that.

The flatness appears at the interface between **claim and justification**.

A mathematical identity, an experimental result, an expert opinion, a rumor repeated ten thousand times and a very plausible completion can all emerge through the same channel, written in equally polished English.

The model gives us the conclusion. It usually does not give us the archaeology.

### Wittgenstein's Line

This is where Wittgenstein becomes useful.

His later philosophy pulled attention away from treating meaning as something we can understand purely by inspecting symbols and toward the role language plays inside practice. Words belong to activities, expectations, habits, rules and what he called forms of life.

“Fire” is not merely connected linguistically to *heat*, *smoke*, *burn* and *wood*. Fire cooks food. Fire destroys houses. You move your hand away from it. Somebody shouts the word in a crowded building and an entire social machinery begins to move.

The word participates in life.

I don't want to turn Saussure and Wittgenstein into action figures fighting over GPT. They were working in different traditions, addressing different questions, and the philosophy of language does not conveniently reduce itself to two dead Europeans and a transformer.

But they give us two useful lines.

**Saussure's line:** relationships within a symbolic system can carry an astonishing amount of linguistic structure.

**Wittgenstein's line:** language also lives inside practices, consequences and forms of life.

A pretrained language model inherits the linguistic residue of those practices. A deployed agent can begin to re-enter them: running code, using tools, observing users, interacting with institutions.

That difference matters. The model begins with residue. The larger system can begin to recover contact.

Embodiment is the shortest version because you touch the world yourself. But embodiment obviously cannot be the whole story. I know far too many things I have never touched, measured or personally witnessed. I have never measured the speed of light. I have never been to Antarctica. I have no direct embodied evidence for most of modern physics, most of history or whether penguins are currently wandering through Rome.

Direct contact does not scale.

So how do we know anything beyond it?

For that, we need Alberto.

## Part II: The Deeper Problem

### How Humans Build Knowledge

**We don't only learn facts. We learn trust structures.**

That is deliberately too neat. Human development does not proceed through clean epistemological layers, cultures differ, and nobody hands a toddler a Bayesian network and asks them to initialize priors.

But even ordinary life teaches us very quickly that sources differ.

Repeated interaction with caregivers gives us expectations before we have words for evidence. Siblings contribute an important epistemological innovation: **some testimony is bullshit.** Your brother tells you there is a monster behind the door. You check. There isn't. He tells you something else and this time it is true.

You begin learning two things at once: facts about the world and facts about sources.

Later, teachers tell you about atoms, dinosaurs, countries you have never visited and wars involving people who died centuries before you were born. You cannot verify most of this yourself. Trust has become mediated: people and institutions you already treat as credible give authority to someone positioned to teach you.

Science extends the chain again. Now the source is not merely one teacher. There are instruments, experiments, other investigators, statistical methods, journals, replication and a social machinery built around the possibility that the first person may have been wrong.

Further out are broader frameworks: economics, political theories, ethical systems, philosophies. These organize experience and suggest what to notice, but they do not earn trust in exactly the same way a measurement does.

And eventually, if inquiry is working properly, we learn one more move: we learn to challenge what we trust.

Not randomly. Random distrust is just another form of stupidity.

A theory earns enormous credibility because it explains many observations. Then something appears that does not fit. At first the sensible response is usually not to burn down physics. You check the instrument. Repeat the experiment. Look for the mistake.

But sometimes the heresy survives. A trusted framework becomes the thing that must be questioned.

**Productive distrust requires trust first.**

You cannot seriously overturn a theory you never understood. The interesting critic knows why people trusted the old structure before finding the place where that trust stops being earned.

The point is not that human knowledge follows a single ladder from mother to science to philosophy. It is that our claims occupy different epistemic relationships to the world.

“I touched the fire” is not the same as “my brother told me.” “My teacher said so” differs from “the experiment was independently replicated.” An interpretive framework differs from a measurement. A new conjecture differs from an established result.

Human knowledge has **epistemological stratification**.

And the stratification is not only conservative. One sign of epistemic maturity is knowing when a high-trust claim has accumulated enough contrary evidence to become the thing under investigation.

### Call Alberto

Suppose someone tells me that penguins live in Italy.

I have never conducted a census of Italian penguins. I cannot personally inspect every forest, coastline and piazza.

So I call Alberto.

Alberto lives in Rome.

“Alberto, do penguins live in Italy?”

He laughs.

I now know more than I did five minutes earlier.

Not with mathematical certainty. Alberto could be wrong. He might misunderstand the question. An escaped penguin could at this very moment be crossing Piazza Navona and destroying the example.

But Alberto occupies a useful position in the trust chain. He is there. He has repeated exposure to Rome. I have a history with him. If he repeatedly lies to me about things he is obviously positioned to observe, I update my trust in Alberto. If he says, “I don't know about all of Italy, but I've never seen one in Rome,” that boundary is itself useful information.

This is how testimony becomes valuable. Not simply because another human said something, but because we care who said it, what they were positioned to know, how reliable they have been before, whether they have incentives to distort the answer and how easily the claim can be challenged.

Testimony comes with metadata.

And we're all Alberto to someone.

Someone may trust me on ranking systems because I have spent years working on them. Someone else may trust me about Jordan because I have lived there. If I start confidently explaining marine biology, the correct response is not to transfer my credibility from machine learning to whales merely because the same mouth is speaking.

**Trust is local.**

Human civilization scales knowledge by extending and formalizing these relationships. Research communities use instruments, protocols, publication and replication. Courts use testimony and adversarial procedure. Engineering uses standards, tests and certification. Markets use reputation and prices.

None guarantees truth. What they do is preserve more structure around claims: where they came from, how they were challenged, what incentives surround them, and what would happen if they turned out to be wrong.

### LLMs Start at the Far End

A base language model starts with the accumulated textual residue of all these processes.

It has read the paper, the article about the paper, the blog post disagreeing with the article, and the Reddit thread where somebody confidently misunderstood both.

Then all of it is compressed together.

This is why saying that “LLMs know nothing because they are just text” is too weak. Text is not disconnected from reality in its origin. Human civilization has spent thousands of years turning experience, experiment, argument, engineering and social verification into language.

Models inherit that residue.

The difficulty is that they often inherit it **after much of the epistemic structure has been flattened**.

A billion web pages claiming that penguins live in Rome could push a model toward that claim even if no penguin had ever set foot there. Frequency is not verification. Statistical dominance is not epistemic authority.

The model can become extremely good at predicting what people say about reality without preserving why particular people were entitled to say it.

In that sense, **it has no Alberto**.

More precisely, the answer often arrives without the live relationship that made Alberto useful: his position to know, his history, the limits of his claim, the possibility that tomorrow I discover he lied and stop calling him about Italian wildlife.

The conclusion survives. Much of the structure that earned it trust does not.

That is the gap System 3 has to repair.

### Stakes and Costly Speech

There is another part of human trust that lives outside the sentence itself. Claims often have consequences.

If Alberto lies to me repeatedly, I stop trusting Alberto. If a researcher fabricates data and is caught, the damage can be enormous. If an engineer signs off on a bridge design and the bridge fails, “but the structural analysis sounded plausible” will not be accepted as a defense.

This mechanism is badly imperfect. People lie despite consequences. Institutions reward confident nonsense. Reputation can become detached from competence. Stakes are not truth, but they are one of the forces that shape testimony.

If a friend asks me where to eat, I may guess. If someone asks me whether to undergo surgery, I become much more careful. The potential cost of being wrong changes how I speak.

An LLM has no social capital of its own to lose. It can confidently produce something false and, at the level of the model itself, nothing happens. The next token arrives exactly as before. The cost is borne elsewhere—by the user, the application or the institution deploying it.

At its most compressed, the danger is **coherence outrunning correspondence**. The machine can become extraordinarily good at tongue without having an ear available to check against.

The dangerous failures are not necessarily gibberish. They are **decaf confidence**: difficult to distinguish from the real thing until the moment the difference matters.

The missing ingredient is not punishment for models. It is architecture that restores more of the evidence, consequence and accountability that the sentence alone cannot carry.

### But Code Is Different

There is one domain where something changes dramatically.

Coding agents can touch their world.

When an agent writes code and runs it, reality answers back.

`TypeError: 'NoneType' object is not subscriptable` is not merely another paragraph describing Python. It is the execution environment saying: whatever story you just told yourself about this program, this particular part of the story is wrong.

That creates an epistemic opportunity. The agent can try something, observe the result, update and try again. The farmer approaches the cow and learns from the kick. The coding agent calls an API incorrectly and learns from the exception. The cow is probably more emotionally memorable, but structurally the loops are similar.

This is why code is such an interesting domain for agent epistemology. It gives us cheap, repeated contact with an environment that pushes back. It is one of the few places where the language model can, metaphorically, **touch the ear**.

The question is whether we preserve what it learns there.

A normal agent session can fail ten times, finally discover the right approach, solve the problem and then throw away almost the entire experiential history when the context ends. It is as if the farmer successfully learned where not to stand and then underwent elective amnesia every evening.

Or, less elegantly, the agent is a goldfish that has forgotten it already tried that corner of the tank.

If we want autonomy over longer horizons, that seems wasteful.

## Part III: The Opportunity — System 3

We are currently obsessed with making models think harder.

System 2 reasoning has become a product category. Give the model more inference time, let it plan, search, reconsider and work through difficult problems before answering.

This is useful. Reasoning matters.

But reasoning perfectly from a bad premise still produces a beautifully reasoned mistake. A researcher can spend six hours developing an elegant argument from a false paper. A coding agent can reason carefully about an API that never existed. An orchestrator can combine five sophisticated judgments that all trace back to one hallucinated claim.

At some point, thinking has to encounter something outside itself.

This is where I use the term **System 3**.

Kahneman's *Thinking, Fast and Slow* gave us the familiar distinction between System 1, the fast and intuitive machinery of thought, and System 2, the slower and more deliberate machinery.

For AI, the analogy is tempting. The base model looks something like System 1: fast pattern recognition, linguistic intuition, enormous associative capacity. Agentic reasoning adds something like System 2: decomposition, planning, reflection and extended search.

But human thinking has always operated inside another structure that the two-system picture largely takes for granted. We test things. We build instruments. We execute code. We compare claims with records. We ask other people. We preserve failures. We create procedures that make some kinds of error harder to hide and some kinds of evidence easier to inspect.

I call that external epistemic machinery **System 3**.

The shortest formulation is still the best:

**System 1 proposes. System 2 deliberates. System 3 checks.**

If you want an even more physical mnemonic:

**System 1 is the Gut. System 2 is the Head. System 3 is the Hand.**

The Gut recognizes. The Head reasons. The Hand reaches outside the conversation and finds something capable of disagreeing.

The metaphor is imperfect. Peer review has no hand, provenance has no fingers, and a formal proof does not need to touch a cow. The distinction matters anyway.

System 3 is the external scaffold that keeps thought answerable to observation, experiment, provenance, persistent failures, tools and other minds.

And it is not Layer 5 sitting neatly above the architecture from Chapter 3. It cuts through the layers.

The model proposes something. The coding agent may test it. The application can collect real user behavior. The problem-solving layer may compare research, simulation and evaluation. Even the goal can change when reality pushes back.

If the five layers tell us **where** increasingly abstract work happens, System 3 is the machinery that keeps those layers **epistemically connected**.

### The MARC File Incident

There is a nice example of what this can look like in practice.

Mini-SWE-agent became interesting partly because of how little custom machinery it needed. Give a strong coding model a shell and it can search, inspect files, execute commands and compose tools that already exist.

Later work on self-evolving software agents pushed the idea one step further. In the Live-SWE-agent work, for example, an agent that encountered MARC files—the venerable bibliographic format used by libraries—created an issue-specific analyzer to inspect data its existing tools could not conveniently expose.

At first glance this is just a nice coding-agent trick. Look at the epistemic structure.

The environment resisted. The agent's current apparatus was not enough, so it created an instrument. The instrument changed what the agent could observe, and that new capability became available to the reasoning process.

Humans have been doing this forever. We could not see bacteria, so we built microscopes. We could not directly perceive radio waves, so we built receivers. We could not conveniently inspect a MARC file, so apparently we wrote Python and called it epistemology.

Informal experience became formal scaffold.

**The wall became a door.**

Interaction reveals a limitation. The limitation motivates a scaffold. The scaffold changes what can be observed next.

This is System 3 in miniature.

### The AlphaGo Lesson

There is an obvious objection: isn't reinforcement learning already doing something similar?

If an agent receives reward from the environment and updates its policy, hasn't reality already entered the model?

Yes, partly. RL can turn experience into better intuition. It changes the weights. The system becomes more likely to make choices that worked in the past.

But there is a useful distinction between knowledge compressed into intuition and knowledge preserved as inspectable external structure.

AlphaGo is a good example. The neural network supplied extremely powerful intuition about which moves looked promising and how valuable a position might be. Monte Carlo Tree Search placed those intuitions inside an explicit search process constrained by the rules and consequences of Go.

I used to describe this too simply as:

> The network proposes. The tree verifies.

That gives MCTS too much epistemic authority. The tree does not magically prove the network right or wrong. What it does is force intuition to participate in an external, stateful process where moves have consequences defined by the game rather than by what the network can plausibly say about the game.

RL improves the gut. System 3 preserves more of the structure around the gut: what was tried, what happened, which paths failed, where claims came from, which tools earned confidence and where their boundaries lie.

The point is not choosing one over the other. It is combining them.

### Trust-Augmented Reasoning

Return to the architecture from Chapter 3.

A research agent tells the orchestrator:

> “Students understand recursion better when shown a tree representation.”

What should happen next?

In a flat architecture, that sentence enters context and competes with every other sentence according to relevance and whatever confidence the model implicitly assigns it.

A trust-aware architecture wants more. Where did the claim come from? Was it a direct experimental result, a teacher's opinion, a design guideline, a blog post or an inference made by the research agent? Did multiple independent sources agree, or did five articles all cite the same study? What population was tested? Does the claim apply to our demo? Has it been contradicted elsewhere?

You do not need a bureaucratic dossier attached to every statement. Sometimes “Alberto said the café is good” is enough.

But when the consequence matters, the system should be capable of carrying provenance with the claim.

That is a **trust chain**. It is not a guarantee of truth. It is a record of how far a claim sits from the evidence supporting it, what transformations happened along the way, and which links we have chosen to trust.

This is **trust-augmented reasoning**: not only asking *what follows from this claim?*, but *what kind of claim is this, and what deserves to follow from it?*

### The Skill Layer

This is where skills become more philosophically interesting than simple prompt files.

A skill is knowledge externalized from the model. Someone—or some previous agent—learned something useful and wrote it down so future sessions would not need to rediscover it.

The grounding happened upstream. **The model inherits the residue.**

But persistence is not trust.

A terrible heuristic written into a skill file is simply a hallucination with better retention. The fact that an instruction lives outside the model does not make it grounded. Persistence can make a bad idea more dangerous because future agents inherit the conclusion without seeing the failure that created it.

A System 3 skill should therefore carry some archaeology. Who created it? What problem was it solving? Where did it work? Where did it fail? Has it been challenged since? What conditions limit its use?

Suppose an agent has learned:

> “Prefer structured parsers over regex for deeply nested formats.”

A normal skill might simply contain the rule. A richer knowledge object might say that the heuristic came from several failed regex-based attempts, later succeeded across multiple nested formats, remains unnecessary for simple flat extraction, and should be treated as a strong prior rather than a universal commandment.

Now the next agent inherits more than advice. It inherits some of the reason the advice earned trust.

### Tools Can Earn Trust Too

The same applies to tools.

Imagine an agent creates `edit_tool.py`. During its first ten uses, eight edits succeed cleanly and two break indentation-sensitive code.

A flat architecture knows: *I have an editing tool.* A trust-aware architecture knows: *this tool has worked reliably for simple substitutions, failed on Python blocks, and should probably not be used blindly for structural edits.*

This is not unlike human expertise. I trust one colleague with distributed systems because she has repeatedly solved distributed-systems problems. I trust another person's product intuition. Neither gets to perform dentistry merely because both are senior.

Reliability is conditional. System 3 needs to remember the condition.

### Meta-Beliefs

We can extend the idea beyond explicit tools.

Suppose the agent develops the heuristic:

> “Regex tends to fail on deeply nested structures.”

That is not a theorem. It is a **meta-belief**.

The system can accumulate evidence for and against it. A crude implementation might record successes and failures, perhaps translating them into some confidence estimate. The exact formula is not the interesting part. The interesting part is that the belief becomes challengeable.

A normal rule says:

> Never use regex here.

A System 3 belief says:

> This has worked often enough that I should prefer it, but new evidence can change my mind.

That small difference moves us from instruction following toward something closer to accumulated experience.

If you enjoy old epistemology labels, you can describe the architecture this way: the model remains largely a **coherentist core**, enormously good at producing structures that hang together, while System 3 tries to wrap that core in a thin **foundationalist shell** tied to observation, provenance and consequence.

I would not take the analogy too literally. Philosophers can put down their weapons.

The architectural point is enough: coherence is valuable, but something outside the coherent system must occasionally be allowed to say no.

This is also personal for me. I spent eight years building systems that rank human testimony—reviews, ratings, Q&A. The hardest problem was never only relevance. It was **trust stratification**. Which claims should the system treat as bedrock? Which need corroboration? How should confidence change through chains of hearsay? What happens when ten accounts repeat the same lie? When does consensus become evidence, and when is it coordinated manipulation?

These aren't abstract questions when they determine what millions of people believe about a product.

**System 3 isn't philosophy to me. It's Tuesday.**

### Creative Distrust

Unfortunately, once you build trust, you inherit another ancient human problem.

Trusted knowledge makes you efficient. It can also make you boring.

If an agent learns that structured parsers beat regex on nested syntax, wonderful. It stops repeating a known mistake. If it learns that tree visualizations worked for the last five recursive algorithms, it may eventually try to teach linear regression with a tree because the trust stack has become stronger than judgment.

Every genuinely new idea begins life with less evidence than the thing it challenges.

This is why System 3 also needs **creative distrust**.

You could call it meta-trust: trust not in the conclusion, but in a method of exploring something that has not earned a track record yet. A mathematician follows an analogy because the structure looks interesting. A scientist repeats the strange experiment after the accepted theory says the result should not happen. A designer violates a trusted pattern because this particular case exposes one of its boundary conditions.

This is not contrarianism for sport. It is not the internet habit of assuming that expert agreement proves corruption.

Creative distrust means understanding the existing trust chain well enough to know exactly where you are breaking it and why.

A mature trust stack therefore has two jobs pulling in opposite directions: it should let knowledge accumulate so we do not rediscover fire every morning, and it should leave enough room for reality to overthrow what has accumulated.

That tension between trust and rebellion is not something System 3 eventually solves. It is part of System 3.

And our experiment ran directly into it.

### What This Covers—and What It Doesn't

Some kinds of epistemic structure are comparatively easy to imagine. Code runs or fails. A benchmark changes. A parser works on a file. A system can preserve what happened, carry provenance with a claim, remember that a tool has failed on one class of inputs, and make blindly repeating a failed approach less likely.

That is already a meaningful change from a model whose useful experience disappears into a conversation and dies when the context closes.

Further out, though, the problem changes. The moment one agent relies on something another agent discovered, trust is no longer only a relationship between one learner and its environment. Who produced the claim? What were they positioned to know? Was it observed, inferred or inherited? Did two agreeing sources reach the conclusion independently, or did both copy the same ancestor?

A social epistemic system is not a bigger memory file. The relationships among the participants matter.

I do not want to solve that problem yet. First I wanted to test the smaller claim:

**even crude epistemic structure around an agent should change how it behaves.**

That is something we can actually measure.

## Part IV: The Experiment

### What We Built

We took the minimal idea and turned it into a small coding agent called **epistemic-swe**.

There was nothing grand about the implementation. No universal truth engine. No distributed council of philosophers arguing on a blockchain.

We added three kinds of persistent state around a normal coding agent. The first was a **tool registry**: tools created or used by the agent accumulated successes, failures and known failure modes. The second was a set of **meta-beliefs**: heuristics could accumulate evidence rather than entering the system as permanent commandments. The third was **failure memory**: when an approach failed, the system preserved enough information about the failure to make blindly repeating the same path less likely later.

This state persisted across sessions, so an agent solving a later problem could draw on things learned earlier.

We also added pruning. An epistemic architecture that remembers everything eventually becomes a hoarder with a context window. Stale tools, weak beliefs and irrelevant failures need to lose influence over time or disappear.

The question was modest:

> Does even this crude epistemic scaffold change how a coding agent behaves?

### The Comparison

We ran mini-swe-agent and epistemic-swe on ten SWE-bench Verified problems from the Astropy repository.

The baseline was intentionally minimal: a capable model with a shell-based coding environment and no persistent epistemic machinery. Epistemic-swe used the same base model and the same tasks, with the trust stack layered around it.

Ten problems is far too small a sample to establish a meaningful solve-rate advantage, and because state persists across tasks, order effects may matter as well. I am not presenting this as a benchmark victory. I wanted to see whether the extra structure changed behavior strongly enough to become visible at all.

It did, just not in the direction I expected.

| **Metric** | **mini-swe-agent** | **epistemic-swe** |
|:--|:--|:--|
| **Solve Rate** | 50% (5/10) | 40% (4/10) |
| **Avg Patch Size** | 620 lines | 269 lines |
| **Patch Reduction** | baseline | **57% smaller in this run** |

Read the first line before celebrating the third.

The epistemic agent solved fewer problems. I had expected learning from previous failures and tools to improve capability. Instead, the most visible difference was in **focus**: its patches became much smaller.

A few examples make the difference visible:

| **Problem** | **mini** | **epistemic** | **Ratio** |
|:--|--:|--:|--:|
| astropy-12907 ✓ | 301 lines | 61 lines | 4.9x smaller |
| astropy-13453 ✓ | 266 lines | 17 lines | 15.6x smaller |
| astropy-14096 ✓ | 529 lines | 70 lines | 7.6x smaller |
| astropy-13977 ✗ | 2720 lines | 362 lines | 7.5x smaller |

The baseline often left behind the debris of exploration: temporary scripts, broader edits, test scaffolding and abandoned experiments. The epistemic agent tended to make more surgical changes.

That does not prove the trust stack caused the reduction, and smaller patches are not automatically better patches. The extra instructions may simply have made the agent more conservative. Persistent state may have changed behavior in ways unrelated to my epistemic interpretation. Ten tasks from one repository do not let us separate these explanations.

Still, the behavior changed enough to be interesting.

**The scaffold seemed to produce discipline before it produced capability.**

That was not the hypothesis, which made the result more useful.

### The 13579 Anomaly

One problem broke the pattern dramatically: `astropy-13579`.

Mini solved it. Epistemic did not. It was also the only case where the epistemic patch became substantially larger rather than smaller.

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

The second approach was not stupid. That is precisely why the case matters.

The agent had accumulated context about indexing, dimensionality and coordinate-system failures. Its chosen explanation fit that context. It followed a path that looked principled and coherent.

It was wrong. The baseline took the simpler path and fixed the actual bug.

One way to read the failure is as **creative distrust failing to happen**: accumulated structure made one family of explanations salient, and the agent did not escape it. But the experiment does not establish that causal story. With one case, we cannot know whether the persistent epistemic state caused the wrong turn or merely accompanied it.

What we can say is that structured memory changes the context in which future search occurs. And that means trust can become **path-dependent**.

Expertise works the same way. A great database engineer may see a database problem faster than most people, which is wonderful until the actual problem is the network. Paradigms are powerful because they focus attention. They can become prisons for exactly the same reason.

The 13579 failure is therefore more interesting to me than a clean win would have been. It shows what a trust-aware architecture must contend with: the scaffold does not merely preserve knowledge. It reshapes future search.

### What the Experiment Actually Tells Us

The honest answer is: not enough yet.

Ten Astropy tasks do not establish that epistemic scaffolding improves software engineering. They do not establish that smaller patches are better, and they do not isolate which part of the architecture produced the behavioral change.

They establish something narrower that I care about:

**persistent epistemic structure can materially change how an agent searches.**

In this run, the change looked like greater parsimony and smaller patches. Solve rate did not improve. At least one problem is consistent with the possibility that accumulated structure can pull an agent toward the wrong conceptual explanation.

That is enough to kill the simplest story:

> add memory, get smarter agent.

The more accurate story is that structured experience **biases future behavior toward what the system has learned**. Sometimes that is exactly what we want. Sometimes the bias is the failure.

A mature System 3 therefore cannot simply accumulate confidence forever. It needs forgetting, counterexamples, challenges, competing possibilities and occasional permission to ignore what it thinks it knows. Otherwise the scaffold becomes a cage.

## When Trust Becomes Social

The experiment left us with an awkward result: persistent experience changed the search, and sometimes the accumulated structure itself became the bias.

Even that was still the easy version because most of the epistemic history belonged to one agent architecture interacting with one software environment. Real knowledge does not stay that local.

A research agent reads a paper written by people it has never met. One coding agent inherits a failure discovered by another. An evaluator trusts an observation produced by a browser. A future session inherits a skill whose author may no longer be present. Even Alberto mattered because he knew something I did not.

The moment knowledge moves between participants, another kind of uncertainty appears. A trust chain can preserve some of the structure—who said this, what they were positioned to know, where the evidence came from, how far the conclusion sits from direct observation—but chains alone do not tell us how to organize a population of fallible knowers.

Five agents might give us five independent checks, or five fluent repetitions of the same mistake. One specialist may know something the others cannot personally verify. A critic may notice a problem precisely because she did **not** inherit the builder's history. A majority may agree because everyone began from the same false premise.

So the problem has changed again. It is no longer only *How should an agent preserve what it has learned?* It is how many fallible knowers should depend on one another without losing the path back to evidence.

That is larger than memory. It is an organizational problem.

## What System 3 Has to Do

At this point I want to draw the boundary carefully, because almost every ingredient already exists under another product name.

System 3 is not simply RAG. Retrieval can bring evidence into context, but retrieval does not tell us why the evidence deserves trust. It is not citations; five citations may still trace back to one bad source. It is not memory, which preserves bad ideas as efficiently as good ones. It is not tools; a broken tool is simply a reliable way to make mistakes faster. And it is not one evaluator, verifier or browser. Each can provide contact with something outside the model while remaining fallible itself.

By now we have something closer to a **requirements document**.

A trustworthy cognitive architecture should preserve where important claims came from. It should distinguish observation from inference, testimony from repetition and a measured result from somebody's interpretation of that result. Experience should survive the session that produced it. Trust should remain local and conditional rather than attaching permanently to a source, tool or rule. Failures should influence future behavior without automatically becoming eternal commandments. Tools and procedures should be able to earn confidence through use—and lose it when their boundary conditions appear. Accumulated knowledge should remain challengeable when reality stops cooperating.

Most importantly, the architecture must preserve some path by which something outside the current story can still say no.

That is the job I mean by **System 3**.

The simplest question remains:

> Is the architecture currently touching the world, or merely listening to itself?

A research model writes a summary. Another model critiques it. A third evaluates the critique. A fourth agrees. Everyone is very impressed.

If all four are ultimately recycling the same unverified assumption, agreement has produced no new evidence. That is not a trust chain. It is an **echo chamber with excellent latency**.

So Chapter 4 gets us surprisingly far. We know more about what trustworthy cognition needs. What we do **not** yet have is an architecture for satisfying those requirements once cognition becomes collective.

## Why This Gets Harder as Models Improve

There is a tempting story in which all of this becomes irrelevant once models become sufficiently capable. Maybe hallucination is temporary. Maybe scale fixes calibration. Maybe the next model simply knows more and makes fewer mistakes.

I hope so. I do not think the architectural problem disappears.

A weak model says something absurd and you check it. A strong model says something wrong with excellent structure. It anticipates your objections, cites plausible mechanisms, connects the conclusion beautifully to everything else you know and gives you several reasons you are clever for agreeing.

The wrong answer becomes elegant.

In an architecture, the deeper problem is not only whether one component fails. It is whether failures **compose**.

A false assumption enters through research, shapes a design, becomes embodied in an implementation, receives positive evaluation and is then stored as a successful pattern for the future. Every component can perform its local task competently while the architecture drifts further from reality.

Nothing has to crash.

At higher levels, failure can become coherent.

This is why I do not think System 3 is mainly about making models smarter. It is about giving the system enough epistemic structure to notice when intelligence has outrun evidence.

## Back to the Waterfall

Return to the seven claims.

**1. Krka National Park — True.** I was there. For me this sits close to embodied memory. For you it is testimony unless you extend the chain through metadata, records or other evidence.

**2. Best philosophical thinking at waterfalls — False.** I mostly do philosophy on buses and in boring waiting rooms. Waterfalls are for ice cream. You have little independent evidence here; the subject and the source are unfortunately the same man.

**3. Permanent camel resident — False.** This can be checked against information about the park. You do not need my biography at all.

**4. The tongue can touch its own ear — Unknown.** I genuinely do not know. I didn't check. Neither did you. You can reason from anatomy, search for similar observations and build a prior, but the shortest decisive chain would have been to stay there and watch. This is the tongue-ear problem in its purest form.

**5. Ice cream ten minutes earlier — True.** Chocolate. Mostly testimony again.

**6. Camels are native to the Dalmatian coast — False.** You probably rejected this almost instantly, but you did not reconstruct camel evolutionary history or personally survey Dalmatian fauna. A huge inherited structure involving biology, geography, education and testimony produced that fast judgment.

**System 1 can be fast because System 3 has often been working for centuries underneath it.**

**7. Real, unedited photograph — True.** But the image alone cannot establish that. A stronger chain might include the original file, metadata, cryptographic signing, independent witnesses or a provenance system. Each link can increase confidence, and each link creates another thing that may itself need to be trusted.

Welcome to epistemology.

The lesson is not that nothing can be known. That conclusion is easy, dramatic and mostly useless. The lesson is that **trust has structure**.

Some claims sit close to direct interaction. Others arrive through testimony. Some pass through instruments, experts and institutions. Some are repeated many times but ultimately trace to one observation. Some are plausible inferences. Some are ideas that have not earned much trust yet but may still deserve investigation.

Flatten all of that into equally confident language and something important disappears.

Human knowledge works partly because we recover that structure imperfectly but constantly. We ask who saw what, which instrument produced the number, whether anyone reproduced it, whether this person knows this domain, why everybody believes the claim and what could make us stop believing it.

The model can remain what it is: an extraordinarily general machine for navigating learned patterns, capable of intuition and increasingly capable of reasoning. It does not need to contain the entire chain inside its weights.

**The model stays hollow. The system doesn't have to be.**

By the end of this chapter, we have a reasonably clear description of what the missing system needs. Claims need archaeology. Experience has to survive. Trust has to remain conditional. Failure has to be remembered without becoming destiny. Different kinds of evidence cannot collapse into equally confident sentences. Somewhere in the chain there must remain contact with something capable of disagreeing.

But that is only the individual version of the problem. The moment one agent relies on research performed by another, one evaluator trusts an instrument built by a third, or one generation inherits knowledge from participants who are no longer present, no single mind can personally reconstruct the whole chain.

We have reached a specification for trustworthy cognition without yet having an architecture for **collective trustworthy cognition**.

The question is no longer simply:

> How can an AI know what to trust?

It is:

> **How can a population of fallible knowers build knowledge together without losing contact with the world?**

Humans have been working on that problem for a very long time.
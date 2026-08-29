# Chapter 4: System 3

*Trust Chains, Tongue-Ear Tests, and What LLMs Can't Verify Alone*

Chapter 3 ended with a system in which almost everything could work and the whole thing could still be wrong.

A research agent makes a claim. A visual model turns it into a design. A coding agent implements the design perfectly. Several evaluators prefer it. Deep Mode invests another generation.

Nothing crashes.

The first claim was false.

Once cognition is spread across researchers, builders, evaluators, tools, memories and agents, intelligence is no longer the only problem. Every component has to rely on things produced by the others. The orchestrator cannot repeat every experiment, reread every paper or independently reproduce every judgment before it acts.

At some point, it has to trust.

Humans have exactly the same problem. Most of what we call knowledge depends on it.

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

Some collide immediately with things you think you know. Some sound plausible but are almost impossible for you to verify. Some could be checked against another source. Others depend mostly on whether you trust me.

Before the chapter has properly begun, you are already doing epistemology.

*Answers later.*

## The Shortest Trust Chain

There is a question that exposes something important about the difference between us and a language model:

*Can your tongue touch your ear?*

You probably tried a variation of this as a child; if not your ear, almost certainly your nose. You did not look up a paper, calculate the biomechanics or ask for the average human tongue-to-ear distance.

You just tried.

Tongue out, strain upward, dignity temporarily suspended, result observed.

Now you know.

The epistemic chain is unusually short. You form a hypothesis, act on the world and the world answers back. Your body is an experimental apparatus that follows you around all day, mostly free of charge.

Large language models have read billions of words about tongues and ears. They can explain tongue anatomy, discuss auricular cartilage and probably tell you about people whose tongues can reach places that will make you regret asking the question.

What they cannot do is check their own tongue. They have no tongue.

That sounds silly because the example is silly. The difference is not.

A body gives us causal contact with a world that does not care how plausible our story sounded. You try to lift something and discover it is heavier than it looked. You misjudge a step and gravity offers immediate peer review. You touch something hot and the argument ends quickly.

A farmer knows cows partly this way. After years around them, cows are not merely propositions involving mammals, milk production and Bovidae. The farmer knows how they move, where not to stand, what a nervous animal looks like, how large a cow feels when there is no photograph between you and it. Some of that can be written down. Some is difficult to articulate at all.

Direct experience is not automatically true experience. Our senses deceive us, memory degrades, and the human hand is a terrible thermometer if you need to distinguish 58°C from 62°C. But embodiment gives us something important: **contact**. The world can disagree.

Then contact becomes history. You do not need to get kicked by the same cow every morning to rediscover where not to stand. One encounter becomes a warning. Repeated encounters become heuristics. Eventually you act on what earlier versions of you learned.

The world pushes back; the result becomes memory; memory changes what you do next.

Language models begin somewhere else. They begin mostly with the residue.

## Saussure's Specification

Ferdinand de Saussure made a radical claim about language in the early twentieth century. The form of a sign is not naturally determined by what it signifies. There is nothing inherently cow-like about the sound /kaʊ/. French speakers say *vache*, Germans say *Kuh*, Japanese speakers say *ushi*.

For Saussure, much of linguistic value comes from relationships and differences inside the system. A sign occupies a position relative to other signs. Language is a network of contrast, convention and structure.

Then consider what we built a century later.

A transformer consumes enormous amounts of language and learns relationships among tokens, contexts and concepts. It has never milked a cow, never been kicked by one, never stood in a field at dawn and discovered that the romantic image of farming omitted an astonishing quantity of manure.

And yet it can talk about cows exceptionally well.

**Saussure's theory was a specification. We implemented it. It's called GPT.**

Not literally. Saussure did not secretly invent attention in 1916, and structural linguistics is not a machine-learning architecture. The historical claim would be silly.

The resemblance is more interesting than that. Language models are spectacular evidence for how much competence can emerge from structure learned inside symbolic data. They write, translate, debug software, explain physics and manipulate abstractions without first acquiring the farmer's relationship to cows or the child's relationship to fire.

The surprise is how far the residue gets us.

It also reveals what the residue leaves behind.

A farmer's sentence may be the compressed endpoint of twenty years of encounters, other farmers' advice, veterinary knowledge and mistakes painful enough not to repeat. The model receives the sentence. The sentence enters a corpus. The corpus becomes training data. Regularities are compressed into weights.

Months later somebody asks:

> Are cows dangerous?

and the model gives an excellent answer.

What usually does not come back is the archaeology. Which part rests on repeated observation? Which part came from veterinary guidance? Did five sources independently observe the same thing, or did four copy the fifth? Which claim is measurement and which merely fits the linguistic neighborhood?

The conclusion survives. Much of the structure that earned it trust does not.

This is what I mean by saying an LLM's knowledge is **epistemologically flat**. I do not mean every concept is represented identically inside the network; obviously it is not. The flatness appears at the interface between **claim and justification**.

A mathematical identity, an experimental result, an expert opinion, a rumor repeated ten thousand times and a plausible completion can all arrive through the same channel in equally polished English.

The model gives us the conclusion. It usually does not give us the archaeology.

Wittgenstein helps draw the other side of the picture. His later philosophy pulled attention toward language as something that lives inside practice: activities, expectations, habits, rules and forms of life.

“Fire” is not merely linguistically associated with *heat*, *smoke*, *burn* and *wood*. Fire cooks food. Fire destroys houses. You move your hand away from it. Someone shouts the word in a crowded building and an entire social machinery begins to move.

The word participates in life.

I do not want to turn Saussure and Wittgenstein into action figures fighting over GPT. They worked in different traditions and the philosophy of language does not reduce itself to two dead Europeans and a transformer.

But they give us two useful lines.

**Saussure's line:** relationships within a symbolic system can carry an astonishing amount of linguistic structure.

**Wittgenstein's line:** language also lives inside practices, consequences and forms of life.

A pretrained model inherits the linguistic residue of those practices. A deployed agent can begin to re-enter them: running code, using tools, observing users, interacting with institutions.

The model begins with residue. The larger system can begin to recover contact.

But embodiment cannot be the whole answer. I know far too many things I have never touched, measured or personally witnessed. I have never measured the speed of light. I have never been to Antarctica. I have no direct embodied evidence for most of modern physics, most of history or whether penguins are currently wandering through Rome.

Direct contact does not scale.

So how do we know anything beyond it?

For that, we need Alberto.

## Call Alberto

Suppose someone tells me that penguins live in Italy.

I have never conducted a census of Italian penguins. I cannot personally inspect every forest, coastline and piazza.

So I call Alberto.

Alberto lives in Rome.

“Alberto, do penguins live in Italy?”

He laughs.

I now know more than I did five minutes earlier.

Not with mathematical certainty. Alberto could be wrong. He may misunderstand the question. An escaped penguin could at this very moment be crossing Piazza Navona and destroying the example.

But Alberto occupies a useful position in the trust chain. He is there. He has repeated exposure to Rome. I have a history with him. If he repeatedly lies to me about things he is well positioned to observe, I update my trust in Alberto. If he says, “I don't know about all of Italy, but I've never seen one in Rome,” the boundary of his knowledge is itself useful information.

This is how testimony becomes valuable. Not simply because another human said something, but because we care **who said it, what they were positioned to know, how reliable they have been, what incentives surround the claim and how easily it can be challenged**.

Testimony comes with metadata.

And we are all Alberto to someone.

Someone may trust me on ranking systems because I have spent years working on them. Someone else may trust me about Jordan because I have lived there. If I begin confidently explaining marine biology, the correct response is not to transfer my credibility from machine learning to whales merely because the same mouth is speaking.

**Trust is local.**

We learn this early. Repeated interaction with caregivers builds expectations before we have words for evidence. Siblings contribute an important epistemological innovation: **some testimony is bullshit**. Teachers tell us about atoms, dinosaurs and wars we cannot personally verify. Science extends the chain through instruments, experiments, other investigators, criticism and replication.

Civilization is full of machinery for making mediated trust less stupid. Courts use testimony and adversarial procedure. Engineering uses standards, tests and certification. Science uses instruments, publication and replication. Markets use reputation and prices. None guarantees truth. All preserve some structure around claims: where they came from, how they were challenged, what incentives surrounded them and what might make us stop believing them.

Human knowledge is not simply a pile of facts. It is **epistemologically stratified**.

“I touched the fire” is not the same as “my brother told me.” “My teacher said so” differs from “the experiment was independently replicated.” A measurement differs from an interpretation. A conjecture differs from an established result.

And mature trust is not purely conservative. Sometimes the instrument disagrees with the theory. At first you check the instrument. Then you repeat the experiment. If the anomaly survives long enough, eventually the trusted theory becomes the thing under investigation.

**Productive distrust requires trust first.**

Random distrust is just another form of stupidity. The interesting critic understands why the old structure earned trust before finding the point where that trust stops being deserved.

A language model starts at the far end of this process. It has read the paper, the article about the paper, the blog post disagreeing with the article, and the Reddit thread where somebody confidently misunderstood both.

Then all of it is compressed together.

Text is not disconnected from reality in its origin. Human civilization has spent thousands of years turning experience, experiment, argument and engineering into language. Models inherit that residue.

The difficulty is that they often inherit it **after much of the epistemic structure has been flattened**.

A billion web pages claiming that penguins live in Rome can push a model toward the claim even if no penguin has ever set foot there. Frequency is not verification. Statistical dominance is not epistemic authority.

In that sense, the model has no Alberto.

More precisely, the answer often arrives without the relationship that made Alberto useful: his position to know, his history, the limits of his claim, the possibility that tomorrow I discover he lied and stop calling him about Italian wildlife.

The conclusion survives. The trust chain does not.

There is one more ingredient humans add almost without noticing: stakes.

If Alberto lies to me repeatedly, I stop trusting him. If a researcher fabricates data and gets caught, the cost can be enormous. If an engineer signs off on a bridge and the bridge fails, “but the analysis sounded plausible” is not a defense.

Stakes are not truth. People lie despite consequences and institutions reward confident nonsense all the time. But consequences shape testimony. If a friend asks where to eat, I may guess. If someone asks whether to undergo surgery, I become much more careful.

An LLM has no social capital of its own to lose. It can confidently produce something false and, at the level of the model itself, nothing happens. The cost lands elsewhere—on the user, the application or the institution deploying it.

At its most compressed, the danger is **coherence outrunning correspondence**. The machine can become extraordinarily good at tongue without having an ear available to check against.

The missing ingredient is not punishment for models. It is architecture that restores more of the evidence, consequence and accountability that the sentence alone cannot carry.

That is the problem System 3 is trying to solve.

## System 3

We are currently obsessed with making models think harder.

System 2 reasoning has become a product category. Give the model more inference time, let it plan, search, reconsider and work through difficult problems before answering.

This is useful. Reasoning matters.

But reasoning perfectly from a bad premise still produces a beautifully reasoned mistake. A research agent can spend six hours developing an elegant argument from a false paper. A coding agent can reason carefully about an API that never existed. Deep Mode can coordinate five sophisticated judgments that all trace back to one hallucinated claim.

At some point, thinking has to encounter something outside itself.

This is where I use the term **System 3**.

Kahneman's *Thinking, Fast and Slow* gave us the familiar distinction between System 1, fast and intuitive cognition, and System 2, slower and more deliberate cognition.

For AI, the analogy is tempting. The base model looks something like System 1: fast pattern recognition, linguistic intuition, enormous associative capacity. Agentic reasoning adds something like System 2: decomposition, planning, reflection and extended search.

But human thought has always operated inside another structure that the two-system picture largely takes for granted. We test things. We build instruments. We execute code. We compare claims with records. We ask other people. We preserve failures. We create procedures that make some errors harder to hide and some evidence easier to inspect.

I call that external epistemic machinery **System 3**.

The shortest formulation is still the best:

**System 1 proposes. System 2 deliberates. System 3 checks.**

If you want a more physical mnemonic:

**System 1 is the Gut. System 2 is the Head. System 3 is the Hand.**

The Gut recognizes. The Head reasons. The Hand reaches outside the current story and finds something capable of disagreeing.

The metaphor is imperfect. Peer review has no hand, provenance has no fingers and a formal proof does not need to touch a cow. The distinction matters anyway.

System 3 is the external scaffold that keeps thought answerable to observation, experiment, provenance, persistent failures, tools and other minds.

And this is where the naming from Chapter 3 matters. **Deep Mode is Layer 3: the problem-solving layer. System 3 is not another layer above it.**

Deep Mode asks: *Given what we know, what should we try next?*

System 3 asks: *What are we entitled to treat as known?*

It cuts across the stack. The model proposes something. The coding agent may test it. The application can collect real user behavior. Deep Mode may compare research, simulation and evaluation. Even Layer 4—the goal itself—can change when reality pushes back.

If the five layers tell us **where** increasingly abstract work happens, System 3 is the machinery that keeps those layers **epistemically connected**.

## Code Can Touch Back

Code is unusually friendly to this idea because coding agents can touch their world.

When an agent writes code and runs it, reality answers back.

`TypeError: 'NoneType' object is not subscriptable` is not merely another paragraph describing Python. It is the execution environment saying: whatever story you just told yourself about this program, this particular part is wrong.

The agent can try something, observe the result, update and try again. The farmer approaches the cow and learns from the kick. The coding agent calls an API incorrectly and learns from the exception. The cow is probably more emotionally memorable, but structurally the loops rhyme.

This is one of the few places where a language model can, metaphorically, **touch the ear**.

The question is whether the system preserves what it learns there.

A normal agent session can fail ten times, discover the right approach, solve the problem and throw away most of the experiential history when the context ends. It is as if the farmer learned exactly where not to stand and then underwent elective amnesia every evening.

Long-horizon autonomy cannot afford that forever.

The MARC file incident is a nice example of the opposite move. In the Live-SWE-agent work, an agent encountering MARC files—the old bibliographic format used by libraries—created an analyzer to inspect data its existing tools could not conveniently expose.

At first glance this is just a neat coding-agent trick. Look at the epistemic structure.

The environment resisted. The agent's current apparatus was not enough, so it created an instrument. The instrument changed what the agent could observe, and that new capability became available to the reasoning process.

Humans have been doing this forever. We could not see bacteria, so we built microscopes. We could not perceive radio waves directly, so we built receivers. We could not conveniently inspect a MARC file, so apparently we wrote Python and called it epistemology.

Interaction reveals a limitation. The limitation motivates a scaffold. The scaffold changes what can be observed next.

That is System 3 in miniature.

AlphaGo offers another useful distinction. Its neural network supplied powerful intuition about promising moves and valuable positions. Monte Carlo Tree Search placed that intuition inside an explicit search process constrained by the state and consequences of Go.

I used to summarize this too simply as “the network proposes; the tree verifies.” That gives the tree too much authority. MCTS does not magically prove the network right. It forces intuition to participate in an external, stateful process where moves have consequences defined by the game rather than by what the network can plausibly say about the game.

RL can improve the gut. System 3 preserves more of the structure around the gut: what was tried, what happened, which paths failed, where claims came from, which tools earned confidence and where their boundaries lie.

The point is not choosing one over the other. It is combining them.

## What Should Survive a Session?

Return to the research claim from Chapter 3:

> Students understand recursion better when shown a tree representation.

In a flat architecture, the sentence enters context and competes with every other sentence according to relevance and whatever confidence the model implicitly assigns it.

A trust-aware architecture wants more. Where did the claim come from? A controlled study? A teacher's opinion? A blog post? An inference made by the research agent? Did several independent sources agree, or did five articles cite the same study? What population was tested? Does the result apply to our demo?

You do not need a bureaucratic dossier attached to every sentence. Sometimes “Alberto said the café is good” is enough.

But when the consequence matters, the claim should be able to carry provenance.

That is a **trust chain**. Not a guarantee of truth. A record of how far a claim sits from the evidence supporting it, what transformations happened along the way and which links we have chosen to trust.

This changes how we should think about skills, tools and memory.

A skill is knowledge externalized from the model. Someone—or some previous agent—learned something useful and wrote it down so later sessions would not need to rediscover it.

The grounding happened upstream. **The model inherits the residue.**

But persistence is not trust. A terrible heuristic written into a skill file is simply a hallucination with better retention.

A useful skill therefore needs some archaeology. Who created it? What problem was it solving? Where did it work? Where did it fail? What conditions limit its use?

Suppose an agent learns:

> Prefer structured parsers over regex for deeply nested formats.

A flat skill stores the rule. A richer object can record that the heuristic came from several failed regex attempts, later worked across multiple nested formats, remains unnecessary for simple flat extraction and should be treated as a strong prior rather than a commandment.

Tools can earn trust in the same way. If `edit_tool.py` succeeds on simple substitutions but repeatedly damages indentation-sensitive blocks, the useful knowledge is not merely *I have an editing tool*. It is *this tool is reliable here and dangerous there*.

Reliability is conditional.

The same applies to softer heuristics. “Regex tends to fail on deeply nested structures” is not a theorem. It is a **meta-belief**—something that can accumulate evidence for and against it.

A normal rule says:

> Never use regex here.

A System 3 belief says:

> This has worked often enough that I should prefer it, but new evidence can change my mind.

That small difference matters. The belief becomes challengeable.

If you enjoy old epistemology labels, you can call the model a largely **coherentist core**—extremely good at producing structures that hang together—and System 3 a thin **foundationalist shell** tied to observation, provenance and consequence.

Do not take that analogy too literally. Philosophers can put down their weapons.

The architectural point is enough: coherence is valuable, but something outside the coherent system must occasionally be allowed to say no.

This is personal for me. I spent eight years building systems that rank human testimony—reviews, ratings and Q&A. The hardest problem was never only relevance. It was **trust stratification**. Which claims deserve corroboration? What happens when ten accounts repeat the same lie? When does consensus become evidence and when is it coordinated manipulation? How far should credibility transfer outside the domain in which it was earned?

These are not abstract questions when they determine what millions of people believe about a product.

**System 3 isn't philosophy to me. It's Tuesday.**

## Creative Distrust

There is an obvious failure mode in all of this.

Trusted knowledge makes you efficient. It can also make you boring.

If an agent learns that structured parsers beat regex on nested syntax, good. It stops repeating a known mistake. If it learns that tree visualizations worked for five recursive algorithms, eventually it may try to explain linear regression with a tree because the trust stack has become stronger than judgment.

Every genuinely new idea begins with less evidence than the thing it challenges.

So System 3 needs **creative distrust** too.

This is not contrarianism for sport. It is not the internet habit of assuming expert agreement proves corruption. It is the ability to understand a trust chain well enough to know where you are breaking it and why.

A mathematician follows an analogy because the structure looks interesting. A scientist repeats a strange experiment after accepted theory says the result should not happen. A designer violates a trusted pattern because this case exposes its boundary conditions.

A mature trust stack therefore has two jobs pulling in opposite directions: let knowledge accumulate so we do not rediscover fire every morning, and leave enough room for reality to overthrow what accumulated.

That tension is not a bug we eventually remove from System 3.

It is part of System 3.

And our experiment ran directly into it.

## The Experiment

I wanted to test a smaller claim than “we solved epistemology for AI.”

Could even crude epistemic structure around a coding agent change how it behaves?

We built a small agent called **epistemic-swe**. It added three kinds of persistent state around a normal coding agent.

A **tool registry** tracked tools, successes, failures and known failure modes. **Meta-beliefs** allowed heuristics to accumulate evidence instead of entering the system as permanent commandments. **Failure memory** preserved enough information about failed approaches to make blindly repeating them less likely later.

The state persisted across sessions, so later problems could inherit things learned earlier. We also pruned it. An epistemic architecture that remembers everything eventually becomes a hoarder with a context window.

We compared mini-swe-agent with epistemic-swe on ten SWE-bench Verified problems from the Astropy repository, using the same base model and tasks.

Ten problems is nowhere near enough to establish a solve-rate advantage. State persisted across tasks, so order effects may matter. I was not looking for a benchmark victory. I wanted to know whether the scaffold changed behavior strongly enough to become visible.

It did, just not in the direction I expected.

| **Metric** | **mini-swe-agent** | **epistemic-swe** |
|:--|:--|:--|
| **Solve Rate** | 50% (5/10) | 40% (4/10) |
| **Avg Patch Size** | 620 lines | 269 lines |
| **Patch Reduction** | baseline | **57% smaller in this run** |

Read the first line before celebrating the third.

The epistemic agent solved fewer problems. I had expected learning from previous failures and tools to improve capability. Instead, the clearest difference was **focus**: its patches became much smaller.

A few examples:

| **Problem** | **mini** | **epistemic** | **Ratio** |
|:--|--:|--:|--:|
| astropy-12907 ✓ | 301 lines | 61 lines | 4.9x smaller |
| astropy-13453 ✓ | 266 lines | 17 lines | 15.6x smaller |
| astropy-14096 ✓ | 529 lines | 70 lines | 7.6x smaller |
| astropy-13977 ✗ | 2720 lines | 362 lines | 7.5x smaller |

The baseline often left behind debris from exploration: temporary scripts, broader edits, test scaffolding and abandoned experiments. The epistemic agent tended to make more surgical changes.

That does not prove the trust stack caused the reduction, and smaller patches are not automatically better patches. The extra instructions may simply have made the agent more conservative. Persistent state may have changed behavior for reasons unrelated to my epistemic interpretation. Ten tasks from one repository cannot separate these explanations.

Still, the behavior changed enough to be interesting.

**The scaffold seemed to produce discipline before it produced capability.**

That was not the hypothesis, which made the result more useful.

### The 13579 Failure

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

The second approach was not stupid. That is why the case matters.

The agent had accumulated context about indexing, dimensionality and coordinate-system failures. Its chosen explanation fit that context. It followed a path that looked principled and coherent.

It was wrong. The baseline took the simpler path and fixed the actual bug.

One possible story is that accumulated epistemic structure made one family of explanations too salient. But one case cannot establish that causal story. Persistent state may have caused the wrong turn or merely accompanied it.

What we can say is that structured memory changes the context in which future search occurs.

Trust is **path-dependent**.

Expertise works the same way. A great database engineer may see a database problem faster than most people, which is wonderful until the actual problem is the network. Paradigms focus attention. They can become prisons for exactly the same reason.

The failure is more interesting to me than a clean win would have been because it kills the simplest story:

> Add memory, get smarter agent.

Structured experience biases future behavior toward what the system has learned. Sometimes that is exactly what we want. Sometimes the bias is the failure.

A mature System 3 cannot simply accumulate confidence forever. It needs forgetting, counterexamples, challenge, competing possibilities and occasional permission to ignore what it thinks it knows.

Otherwise the scaffold becomes a cage.

## When Trust Becomes Social

Even that experiment was the easy version because most of the epistemic history belonged to one agent architecture interacting with one software environment.

Real knowledge does not stay that local.

A research agent reads a paper written by people it has never met. One coding agent inherits a failure discovered by another. An evaluator trusts an observation produced by a browser. A future session inherits a skill whose author is no longer present. Alberto mattered precisely because he knew something I did not.

The moment knowledge moves between participants, another kind of uncertainty appears. A trust chain can preserve who said what, what they were positioned to know, where evidence came from and how far a conclusion sits from direct observation. But chains alone do not tell us how to organize a population of fallible knowers.

Five agents might give us five independent checks or five fluent repetitions of the same mistake. A specialist may know something the others cannot personally verify. A critic may notice a problem precisely because she did **not** inherit the builder's history. A majority may agree because everyone began from the same false premise.

The problem has changed again.

It is no longer only *How should an agent preserve what it learned?*

It is: **How should fallible knowers depend on one another without losing the path back to evidence?**

That is larger than memory. It is an organizational problem.

Before going there, I want to make the boundary of System 3 explicit.

It is not simply RAG. Retrieval can bring evidence into context, but retrieval does not tell us why the evidence deserves trust. It is not citations; five citations may trace to one bad source. It is not memory, which preserves bad ideas as efficiently as good ones. It is not tools; a broken tool is simply a reliable way to make mistakes faster. It is not one verifier, evaluator or browser. Each can provide contact with something outside the model while remaining fallible itself.

System 3 is the architecture that preserves **where important claims came from, what kind of evidence supports them, what has failed before, where trust is conditional, and how reality can still push back**.

Most importantly, it preserves some path by which something outside the current story can still say no.

A research model writes a summary. Another model critiques it. A third evaluates the critique. A fourth agrees. Everyone is very impressed.

If all four ultimately recycle the same unverified assumption, agreement has produced no new evidence.

That is not a trust chain.

It is an **echo chamber with excellent latency**.

And better models do not make this architectural problem disappear. A weak model says something absurd and you check it. A strong model says something wrong with excellent structure. It anticipates objections, connects the conclusion beautifully to everything else you know and makes the wrong answer elegant.

In a compound system the deeper risk is that failures **compose**. A false assumption enters through research, shapes a design, becomes embodied in an implementation, receives positive evaluation and is stored as a successful pattern for the future. Every component can perform its local task competently while the architecture drifts further from reality.

Nothing has to crash.

At higher levels, failure can become coherent.

System 3 is not mainly about making the model smarter. It is about giving the larger system enough epistemic structure to notice when intelligence has outrun evidence.

## Back to the Camel

Return to the seven claims.

**1. Krka National Park — True.** I was there. For me this sits close to embodied memory. For you it is testimony unless you extend the chain through records or other evidence.

**2. Best philosophical thinking at waterfalls — False.** I mostly do philosophy on buses and in boring waiting rooms. Waterfalls are for ice cream. The subject and the source are unfortunately the same man.

**3. Permanent camel resident — False.** This can be checked against information about the park. You do not need my biography.

**4. The tongue can touch its own ear — Unknown.** I genuinely do not know. I did not check. Neither did you. We can reason from anatomy and build a prior, but the shortest decisive chain would have been to stay there and watch.

**5. Ice cream ten minutes earlier — True.** Chocolate. Mostly testimony again.

**6. Camels are native to the Dalmatian coast — False.** You probably rejected this immediately, but you did not reconstruct camel evolutionary history or personally survey Dalmatian fauna. A large inherited structure involving biology, geography, education and testimony produced that fast judgment.

**System 1 can be fast because System 3 has often been working for centuries underneath it.**

**7. Real, unedited photograph — True.** The image alone cannot establish that. A stronger chain might include the original file, metadata, cryptographic signing, independent witnesses or another provenance system. Each link can increase confidence, and each creates another thing that may itself need to be trusted.

Welcome to epistemology.

The lesson is not that nothing can be known. That conclusion is dramatic and mostly useless.

The lesson is that **trust has structure**.

Some claims sit close to direct interaction. Others arrive through testimony. Some pass through instruments, experts and institutions. Some are repeated many times but trace back to one observation. Some are plausible inferences. Some are ideas that have not earned much trust yet but may deserve investigation.

Flatten all of that into equally confident language and something important disappears.

Human knowledge works partly because we recover the structure imperfectly but constantly. Who saw what? Which instrument produced the number? Did anybody reproduce it? Does this person know this domain? Why do we believe the claim? What would make us stop?

The model can remain what it is: an extraordinarily general machine for navigating learned patterns, capable of intuition and increasingly capable of reasoning. It does not need to contain the whole chain inside its weights.

**The model stays hollow. The system doesn't have to be.**

We now have a reasonably clear specification for trustworthy cognition. Claims need archaeology. Experience has to survive. Trust has to remain conditional. Failure has to be remembered without becoming destiny. Different kinds of evidence cannot collapse into equally confident sentences. Somewhere in the chain there must remain contact with something capable of disagreeing.

But this is still mostly the individual version of the problem.

The moment one agent relies on research performed by another, one evaluator trusts an instrument built by a third, or one generation inherits knowledge from participants who are no longer present, no single mind can reconstruct the whole chain.

The question is no longer simply:

> How can an AI know what to trust?

It is:

> **How can a population of fallible knowers build knowledge together without losing contact with the world?**

Humans have been working on that problem for a very long time.
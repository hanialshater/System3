# Chapter 4: System 3

*Trust Chains, Tongue-Ear Tests, and What LLMs Can’t Verify Alone*

Before we design another architecture, consider a camel.

![Photograph accompanying the seven claims](../book-design/curated/assets/art/photo58.jpg)

*The author at Krka National Park*

Here are seven claims about this image. Some are true and some are false, and you can’t verify most of them without trusting me:

1. This was taken at Krka National Park, Croatia.
2. The author does his best philosophical thinking at waterfalls.
3. This camel is a permanent resident of the park.
4. The tongue pictured can touch its own ear.
5. The author was eating ice cream ten minutes before this.
6. Camels are native to the Dalmatian coast.
7. This is a real, unedited photograph.

How do you decide which ones to believe? However you’re deciding, you are already doing epistemology, and the chapter has barely begun. The answers are at the end.

## The Shortest Trust Chain

*Can your tongue touch your ear?*

You probably tried some version of this as a child, if not with your ear then almost certainly with your nose. You didn’t look up a paper, calculate the biomechanics or ask anyone for the average distance from tongue to ear.

You just tried.

Tongue out, strain upward, dignity temporarily suspended, result observed.

The epistemic chain here is about as short as they come. You form a hypothesis, act on the world, and the world answers. Your body is an experimental apparatus that follows you around all day, mostly free of charge.

Large language models have read billions of words about tongues and ears. They can explain tongue anatomy, discuss auricular cartilage, and probably tell you about people whose tongues reach places you’ll wish you hadn’t asked about. They cannot try it on themselves. They have no tongue.

A body puts us in causal contact with a world that doesn’t care how plausible our story sounded. Misjudge a step and gravity offers immediate peer review.

A farmer knows cows partly this way. After years around them, the farmer knows how they move, where not to stand, what a nervous animal looks like, and how large a cow feels when there is no photograph between you and it. Some of that could go in a textbook about mammals, milk production and Bovidae. Some of it the farmer would struggle to put into words at all.

Our senses deceive us, memory degrades, and the human hand is a terrible thermometer if you need to tell 58°C from 62°C. What embodiment offers is contact, a way for the world to disagree with us.

You don’t need the same cow to kick you every morning to remember where not to stand. One kick is a warning, and after enough of them you have a heuristic.

Language models start somewhere else, mostly with the residue that all this experience leaves behind in writing.

## Saussure’s Specification

In the early twentieth century Ferdinand de Saussure made a radical claim about language: what a sign signifies does not determine its form. There is nothing inherently cow-like about the sound /kaʊ/. French speakers say *vache*, Germans say *Kuh*, and Japanese speakers say *ushi*.

For Saussure, much of a sign’s value comes from its relationships and differences with the other signs in the system. Language, on this view, is a network of contrasts held together by convention.[1](appendix-references.md#ref-04-saussure)

A century later we built something that learns a network of that kind. A transformer consumes enormous amounts of language and learns relationships among tokens and contexts. It has never milked a cow or been kicked by one, and it has never stood in a field at dawn and discovered how much manure the romantic image of farming leaves out. It still talks about cows very well.

Read today, Saussure’s theory looks uncannily like a specification for GPT. He did not secretly invent attention in 1916, and structural linguistics is not a machine-learning architecture. But language models are spectacular evidence for how much competence can emerge from structure learned inside symbolic data. They write, translate, debug software and explain physics without ever acquiring the farmer’s relationship to cows or a child’s relationship to fire.

The residue carries a great deal, though not everything.

A farmer’s sentence about cows may compress twenty years of encounters, other farmers’ advice, veterinary knowledge and mistakes painful enough not to repeat. The sentence goes into a corpus, the corpus becomes training data, and its regularities are compressed into weights.

Months later somebody asks whether cows are dangerous, and the model gives an excellent answer. What usually doesn’t come back is the history of that answer: which parts rest on repeated observation, and whether five sources saw the same thing independently or four of them copied the fifth.

The conclusion survives training, and much of what earned it trust is lost along the way. That is what I mean when I call an LLM’s knowledge epistemologically flat. The flatness sits between a claim and its justification. A mathematical identity, an experimental result, an expert opinion, a rumor repeated ten thousand times and a plausible completion can all arrive through the same channel, in equally polished English.

Wittgenstein’s later philosophy drew attention to language as something that lives inside practice, in activities, habits, rules and what he called forms of life.[2](appendix-references.md#ref-04-wittgenstein)

“Fire” keeps linguistic company with heat, smoke, burn and wood. Fire is also the thing that cooks food and destroys houses, the thing you pull your hand away from. Shout the word in a crowded building and a whole social machinery starts to move.

Emily Bender and Alexander Koller made a version of this argument with a hyper-intelligent octopus. It taps an undersea cable between two stranded islanders, learns their patterns and cuts in to impersonate one of them. It can bluff through a conversation about a coconut catapult by offering praise. Then a bear attacks, the islander asks how to defend herself with sticks, and the octopus has nothing. Their argument is that learning form alone cannot give it meaning.[3](appendix-references.md#ref-04-octopus) I prefer dead Europeans to cephalopods, but the point is the same.

A pretrained model inherits the linguistic residue of our practices. A deployed agent can start to re-enter them by running code, using tools, observing users and interacting with institutions.

Embodiment can’t be the whole answer, though. I know far too many things I have never touched, measured or witnessed. I have never measured the speed of light or been to Antarctica, and I have no direct evidence for most of modern physics, most of history, or whether penguins are wandering through Rome right now. Direct contact doesn’t scale.

To know anything beyond it, I need Alberto.

## Call Alberto

Suppose someone tells me that penguins live in Italy. I have never conducted a census of Italian penguins, and I can’t inspect every forest, coastline and piazza myself. So I call Alberto, who lives in Rome.

“Alberto, do penguins live in Italy?”

He laughs.

I know more than I did five minutes ago.

I don’t know it with certainty. Alberto could be wrong, or he may have misunderstood the question, and an escaped penguin could be crossing Piazza Navona at this very moment and ruining my example.

Still, Alberto sits in a useful place in the trust chain. He is there, he sees Rome every day, and I have a history with him. If he kept lying to me about things he is well placed to see, I would trust him less. If he says, “I don’t know about all of Italy, but I’ve never seen one in Rome,” the edge of his knowledge is useful information too. Testimony comes with metadata.

We are all Alberto to someone. People may trust me on ranking systems because I have spent years working on them, or about Jordan because I have lived there. If I start confidently explaining marine biology, they shouldn’t carry my credibility over from machine learning to whales just because the same mouth is talking.

## It Starts With a Face

We learn all of this early, and we do not start with evidence.

An infant trusts a face before it has words for anything. My mother’s face meant food, warmth and safety. Nothing I have believed since has been better supported. That trust was earned the way the tongue-ear test is settled, by contact: the face appeared and things got better, thousands of times.

Then the face started making claims. Hot. Don’t touch. That one bites. I could not check most of them, and the few I checked the hard way came out in her favor. Every claim that held at the bottom paid credit upward to its source. I believed what she told me was good or bad. Then I believed the people she trusted.

Siblings contributed an important epistemological innovation: some testimony is bullshit. A brother will say anything with total confidence. You learn to ask who is speaking and what he gets out of it, years before anyone teaches you the word incentive.

Then teachers told me about atoms, dinosaurs and wars none of us could verify. I believed them because my mother had sent me to that school, and because the parts I could check, the spelling and the sums, held up. From there the chain runs on to books, to the institutions that print them, and to a whole society’s machinery for deciding what to believe.

At no point did I build my knowledge from the ground up. I grew trust upward from a face.

Each layer was built on the one below it and reached a little further from anything I could touch. Nothing was replaced wholesale. When a layer failed, when the brother was lying or the textbook was out of date, I repaired that part and kept the rest. Knowledge goes up the way a city does, by addition and repair on top of what is already standing. Nobody gets to start from an empty field.

So human knowledge is epistemologically stratified. “I touched the fire” and “my brother told me” sit at different levels, and so do “my teacher said so” and “the experiment was independently replicated.” A measurement sits at a different level from an interpretation, and a conjecture from an established result.

Mature trust can also turn on itself. When an instrument disagrees with a theory, you check the instrument first, then repeat the experiment. If the anomaly survives long enough, the trusted theory becomes the thing under investigation. That kind of distrust only works because there is trust underneath it.

Models inherit the text produced along the way, but usually not the live relationships underneath it. The paper, the article about the paper, the blog post disagreeing with the article and the Reddit thread where somebody confidently misunderstood both can all end up in the same training distribution. The model got the library without the childhood.

The model has no Alberto: no live record of who was positioned to know, where a claim came from, how its source behaved before, or where the source’s competence stops.

There is one more ingredient humans add almost without noticing, which is stakes. If Alberto lies to me repeatedly, I stop trusting him. If a researcher fabricates data and gets caught, the cost can be enormous. If an engineer signs off on a bridge and the bridge fails, “but the analysis sounded plausible” is no defense.

Consequences don’t make anyone truthful. People lie despite them, and institutions reward confident nonsense all the time. But consequences do shape testimony. If a friend asks where to eat, I may guess. If someone asks whether to undergo surgery, I become much more careful.

An LLM has no social capital of its own to lose. It can confidently produce something false and, at the level of the model itself, nothing happens. The cost lands elsewhere: on the user, the application or the institution deploying it.

The danger is coherence outrunning correspondence, with the machine getting very good at tongue and having no ear to check it against. The failures to worry about are the ones that seem to work. A crash at least tells you something went wrong.

## System 3

At the moment we are obsessed with making models think harder. System 2 reasoning has become a product category: give the model more inference time and let it plan, search, reconsider and work through difficult problems before it answers.

Reasoning perfectly from a bad premise still gets you a beautifully reasoned mistake. A research agent can spend six hours developing an elegant argument from a false paper. A coding agent can reason carefully about an API that never existed. Deep Mode can coordinate five sophisticated judgments that all trace back to one hallucinated claim. At some point thinking has to meet something outside itself.

Kahneman’s *Thinking, Fast and Slow* popularized the distinction between System 1, fast and intuitive cognition, and System 2, slower and more deliberate cognition.[4](appendix-references.md#ref-04-kahneman)

For AI, the analogy is tempting. The base model looks something like System 1: fast pattern recognition, linguistic intuition, enormous associative capacity. Agentic reasoning adds something like System 2: decomposition, planning, reflection and extended search.

But human thought has always run inside another structure that the two-system picture mostly takes for granted. We test things, build instruments, ask other people and keep a record of our failures. I call that external epistemic machinery System 3. If System 1 proposes and System 2 deliberates, System 3 checks.

A cruder version is easier to remember: the Gut, the Head and the Hand. The Gut recognizes and the Head reasons, while the Hand reaches outside the current story for something capable of disagreeing with it. Peer review has no hand, provenance has no fingers and a formal proof never needs to touch a cow, so take the mnemonic loosely.

Deep Mode is Layer 3, the problem-solving layer. System 3 runs through every layer.

Deep Mode asks: Given what we know, what should we try next?

System 3 asks: What are we entitled to treat as known?

The model proposes something, the coding agent may test it, and the application can collect real user behavior. Deep Mode may compare research, simulation and evaluation. Even the desire layer, the goal itself, can change when reality pushes back.

The five layers describe where increasingly abstract work happens, and System 3 keeps them epistemically connected. Without it, every layer we delegate to is one more place for an unsupported claim to travel.

Here is the stack, with System 3 running across it:

|Layer|The question it answers|
|---|---|
|4 — Desire|What do we actually want?|
|3 — Deep Mode|Given what we know, what should we try next?|
|2 — Application|Can the work begin near the application instead of the plumbing?|
|1 — Agent|Can the model act, and see what happened?|
|0 — Model|What does the pattern suggest?|
|System 3, across all of them|What are we entitled to treat as known?|

## Code Can Touch Back

Code suits this idea unusually well, because a coding agent can touch its world. When it writes code and runs it, the program either does what the agent expected or it doesn’t.

`TypeError: 'NoneType' object is not subscriptable` is the execution environment telling the agent that whatever story it just told itself about this program, this particular part of the story is wrong.

The agent can try something, see what happens, update and try again. The farmer learns from the kick and the coding agent learns from the exception. The kick is more memorable, but the two loops have the same shape. Here a language model can, metaphorically, touch its ear. What matters then is whether the system keeps what it learns.

A normal agent session can fail ten times, discover the right approach, solve the problem and throw away most of that history when the context ends. It is as if the farmer learned exactly where not to stand and then underwent elective amnesia every evening.

In the Live-SWE-agent work, an agent ran into MARC files, the old bibliographic format libraries use. Its tools made the contents awkward to inspect, so it built an analyzer that displayed them in a readable form.[5](appendix-references.md#ref-04-liveswe) Its apparatus wasn’t enough, so it built an instrument, and the instrument changed what it could observe.

People have always done this. We couldn’t see bacteria, so we built microscopes, and we couldn’t perceive radio waves, so we built receivers. The MARC analyzer is a humbler instrument of the same kind, and a small working example of System 3.

AlphaGo draws a related distinction. Its neural network supplied powerful intuition about promising moves and valuable positions. Monte Carlo Tree Search placed that intuition inside an explicit search process constrained by the state and consequences of Go.[6](appendix-references.md#ref-04-alphago)

I used to put this too simply: “the network proposes; the tree verifies.” That gives the tree too much authority, since MCTS does not prove the network right. What it does is make intuition take part in an external, stateful process, where the game decides the consequences of a move whatever the network finds plausible.

RL can improve the gut. System 3 keeps more of what surrounds it: what was tried, what happened, which paths failed, where claims came from, which tools earned confidence and where their boundaries lie.

## A Hallucination With Better Retention

Return to the research claim about recursion trees:

> Students understand recursion better when shown a tree representation.

In a flat architecture, the sentence enters context and competes with every other sentence according to relevance and whatever confidence the model implicitly assigns it.

A trust-aware architecture would ask where the claim came from: a controlled study, a teacher’s opinion or a blog post. It would ask which population was tested and whether the result applies to our demo.

Not every sentence needs a dossier attached. Sometimes “Alberto said the café is good” is plenty. When the consequences matter, though, the claim should be able to carry its provenance.

That is a trust chain: a record of how far a claim sits from the evidence supporting it, what transformations happened along the way, and which links we have chosen to trust. It doesn’t guarantee that the claim is true.

A skill is knowledge externalized from the model. Someone, or some previous agent, learned something useful and wrote it down so later sessions would not need to rediscover it.

Writing something down doesn’t make it trustworthy, though. A terrible heuristic in a skill file is simply a hallucination with better retention. A useful skill needs some archaeology: who created it, where it worked, and where it failed.

Suppose an agent learns:

> Prefer structured parsers over regex for deeply nested formats.

A flat skill stores the rule. A richer object can record that the heuristic came from several failed regex attempts, later worked across multiple nested formats, is unnecessary for simple flat extraction, and is best treated as a strong prior.

Tools can earn trust in the same way. If `edit_tool.py` succeeds on simple substitutions but repeatedly damages indentation-sensitive blocks, the useful knowledge is that this tool is reliable here and dangerous there.

Such a heuristic is a meta-belief: a reason to prefer one approach, with evidence that can change its standing. “Never use regex here” has no place to put the counterexample.

If you enjoy old epistemology labels, you can call the model a largely coherentist core, uncannily good at producing structures that hang together, and System 3 a thin foundationalist shell tied to observation, provenance and consequence. I only need the architectural analogy. Coherence is valuable, but something outside the coherent system must occasionally be allowed to say no.

This is personal for me. I spent eight years building systems that rank human testimony: reviews, ratings and Q&A. The hardest problem was never only relevance. It was trust stratification. Which claims deserve corroboration? What happens when ten accounts repeat the same lie? When does consensus become evidence, and when is it coordinated manipulation? How far should credibility transfer outside the domain in which it was earned?

Those questions stop being abstract when the answers decide what millions of people believe about a product.

System 3 isn’t philosophy to me. It’s Tuesday.

## The Epistemic Agent

I wanted to test something much smaller than “we solved epistemology for AI”: whether even crude epistemic structure around a coding agent would change how it behaves.

We built a small agent called epistemic-swe. It added three kinds of persistent state around a normal coding agent.

A tool registry tracked tools, successes, failures and known failure modes. Meta-beliefs allowed heuristics to accumulate evidence instead of entering the system as permanent commandments. Failure memory preserved enough information about failed approaches to make blindly repeating them less likely later.

The state persisted across sessions, so later problems could inherit things learned earlier. We also pruned it, because remembering everything eventually costs more context than it saves.

We compared mini-swe-agent with epistemic-swe on ten SWE-bench Verified problems from the Astropy repository, using the same base model and tasks.[7](appendix-references.md#ref-04-swebench)

Ten problems is nowhere near enough to establish a solve-rate advantage, and because state persisted across tasks, order effects may matter. I was not looking for a benchmark victory. I wanted to know whether the scaffold changed behavior strongly enough to see, and it did, though not the way I expected.

|Metric|mini-swe-agent|epistemic-swe|
|---|---|---|
|Solve rate|50% (5/10)|40% (4/10)|
|Average patch size|620 lines|269 lines|
|Patch reduction|baseline|57% smaller in this run|

The epistemic agent solved fewer problems. I had expected that learning from previous failures and tools would make it more capable. The clearest difference turned out to be focus: its patches were much smaller. Four of the problems show the range:

|Problem|mini|epistemic|Ratio|
|---|---|---|---|
|astropy-12907 ✓|301 lines|61 lines|4.9x smaller|
|astropy-13453 ✓|266 lines|17 lines|15.6x smaller|
|astropy-14096 ✓|529 lines|70 lines|7.6x smaller|
|astropy-13977 ✗|2720 lines|362 lines|7.5x smaller|

The last row distorts the average. That one failed baseline patch accounts for more than two-fifths of all the baseline’s lines, and leaving the problem out brings the average reduction down from 57 percent to about a third. The pattern holds, but the headline number flatters it.

The baseline often left behind debris from exploration: temporary scripts, broader edits, test scaffolding and abandoned experiments. The epistemic agent tended to make more surgical changes.

That does not prove the trust stack caused the reduction, and smaller patches are not automatically better patches. The extra instructions may simply have made the agent more conservative. Persistent state may have changed behavior for reasons unrelated to my epistemic interpretation. Ten tasks from one repository cannot separate these explanations.

If anything, the scaffold seemed to produce discipline before it produced capability. That wasn’t my hypothesis, which is why I learned more from it.

### The 13579 Failure

One problem, `astropy-13579`, broke the pattern badly. Mini solved it and epistemic did not, and it was the only case where the epistemic patch came out substantially larger.

Both agents correctly identified the central bug: dropped world-coordinate dimensions were being filled with a hard-coded value instead of the actual coordinate value.

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

The epistemic agent chose a more structural intervention around which dimensions were being kept. Shown schematically:

```python
self._pixel_keep = np.nonzero([
    not isinstance(self._slices_array[ip], ...)
    for ip in range(self._wcs.pixel_n_dim)
])[0]
```

The second approach was not stupid. That is why the case matters.

The agent had accumulated context about indexing, dimensionality and coordinate-system failures. Its chosen explanation fit that context, and the path it followed looked principled and coherent.

It was wrong. The baseline took the simpler path and fixed the actual bug.

One possible story is that accumulated epistemic structure made one family of explanations too salient. But one case cannot establish that causal story. Persistent state may have caused the wrong turn or merely accompanied it.

Trust is path-dependent, and so is expertise. A great database engineer may see a database problem faster than most people, which is wonderful until the actual problem is the network. The same focus that makes a paradigm useful can trap the people working inside it.

“Add memory, get a smarter agent” had failed its first small test. It left me wondering what would let an agent challenge the experience it had accumulated.

## Creative Distrust

Trusted knowledge makes you efficient, and it can also make you boring. If an agent learns that tree visualizations worked for five recursive algorithms, eventually it may try to explain linear regression with a tree, because the trust stack has become stronger than judgment. On 13579, knowledge about indexing may have made the wrong explanation harder to leave.

A new idea can arrive with very little evidence behind it. It may be right and still sound like my brother’s bullshit. System 3 needs room for creative distrust too.

By that I mean understanding a trust chain well enough to know where you are breaking it and why. Contrarianism for sport doesn’t count, and neither does the internet habit of treating expert agreement as proof of corruption.

A scientist repeats a strange experiment after accepted theory says the result should not happen. A designer violates a trusted pattern because this case exposes its boundary conditions.

A mature trust stack has two jobs pulling in opposite directions: let knowledge accumulate so we do not rediscover fire every morning, and leave enough room for reality to overthrow what accumulated.

## Back to the Camel

Now the seven claims.

1. **Krka National Park: true.** I was there. For me this sits close to embodied memory. The caption had already told you where it was taken, but I wrote the caption too. For you it is testimony unless you extend the chain through records or other evidence.
2. **Best philosophical thinking at waterfalls: false.** I mostly do philosophy on buses and in boring waiting rooms. Waterfalls are for ice cream. The subject and the source are unfortunately the same man.
3. **Permanent camel resident: false.** This can be checked against information about the park. You do not need my biography.
4. **The tongue can touch its own ear: unknown.** I genuinely don’t know, because I didn’t check, and neither did you. We can reason from anatomy and build a prior, but the shortest decisive chain would have been to stay there and watch.
5. **Ice cream ten minutes earlier: true.** Chocolate. Mostly testimony again.
6. **Camels are native to the Dalmatian coast: false.** You probably rejected this immediately without reconstructing camel evolutionary history or personally surveying Dalmatian fauna. A large inherited structure did that work for you. System 1 can be fast because System 3 has often been working underneath it for centuries.
7. **Real, unedited photograph: true.** The image alone cannot establish that. A stronger chain might include the original file, metadata, cryptographic signing, independent witnesses or another provenance system. Every extra link can increase confidence, and every one is something else that may need to be trusted. I could also be lying to prove a point about trusting sources. If I told you the photograph was AI-generated, you would probably believe that too, because it fits a pattern you recognize.

None of this means that nothing can be known, a conclusion that is dramatic and mostly useless. It means that trust has structure.

The model can remain what it is: an extraordinarily general machine for navigating learned patterns, capable of intuition and increasingly capable of reasoning. It doesn’t need to hold the entire chain in its weights, because the system around it can.

Borrowing Daniel Dennett’s phrase, I would call this competence without comprehension.[8](appendix-references.md#ref-04-dennett) Whether the system around it amounts to comprehension is a question for people with more patience than I have. The part of it that can be checked is the part the rest of this book builds.

Everything so far can still be imagined around one agent that acts, checks, remembers, records provenance and updates what it trusts.

Real systems will not stay that simple. The moment one agent inherits a claim from another, no participant can personally reconstruct every path back to reality. A trust chain can preserve where a claim came from. It does not, by itself, tell us how the knowers who depend on those chains should be arranged.

The question then becomes: how can a population of fallible knowers build knowledge together without losing contact with the world?

Humans have been working on that problem for a very long time.

---

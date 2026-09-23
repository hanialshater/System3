# Chapter 4: System 3

*Trust Chains, Tongue-Ear Tests, and What LLMs Can't Verify Alone*

Before we design another architecture, consider a camel.

Seven claims about this image. Some are true. Some are false. You can't verify most of them without trusting me:

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

Before the chapter has properly begun, you are already doing epistemology.

*Answers later.*

## The Shortest Trust Chain

*Can your tongue touch your ear?*

You probably tried a variation of this as a child; if not your ear, almost certainly your nose. You did not look up a paper, calculate the biomechanics or ask for the average human tongue-to-ear distance.

You just tried.

Tongue out, strain upward, dignity temporarily suspended, result observed. Now you know.

The epistemic chain is unusually short. You form a hypothesis, act on the world and the world answers back. Your body is an experimental apparatus that follows you around all day, mostly free of charge.

Large language models have read billions of words about tongues and ears. They can explain tongue anatomy, discuss auricular cartilage and probably tell you about people whose tongues can reach places that will make you regret asking the question.

What they cannot do is check their own tongue. They have no tongue.

A body gives us causal contact with a world that does not care how plausible our story sounded. You misjudge a step and gravity offers immediate peer review. You touch something hot and the argument ends quickly.

A farmer knows cows partly this way. After years around them, cows are not merely propositions involving mammals, milk production and Bovidae. The farmer knows how they move, where not to stand, what a nervous animal looks like, how large a cow feels when there is no photograph between you and it. Some of that can be written down. Some is difficult to articulate at all.

Our senses deceive us, memory degrades, and the human hand is a terrible thermometer if you need to distinguish 58°C from 62°C. But embodiment gives us something important: contact. The world can disagree.

You do not need to get kicked by the same cow every morning to rediscover where not to stand. One encounter becomes a warning. Repeated encounters become heuristics.

Language models begin somewhere else. They begin mostly with the residue.

## Saussure's Specification

Ferdinand de Saussure made a radical claim about language in the early twentieth century. The form of a sign is not naturally determined by what it signifies. There is nothing inherently cow-like about the sound /kaʊ/. French speakers say *vache*, Germans say *Kuh*, Japanese speakers say *ushi*.

For Saussure, much of linguistic value comes from relationships and differences inside the system. A sign occupies a position relative to other signs. Language is a network of contrast, convention and structure.[^saussure]

Then consider what we built a century later.

A transformer consumes enormous amounts of language and learns relationships among tokens, contexts and concepts. It has never milked a cow, never been kicked by one, never stood in a field at dawn and discovered that the romantic image of farming omitted an astonishing quantity of manure.

And yet it can talk about cows exceptionally well.

**Saussure's theory was a specification. We implemented it. It's called GPT.**

Not literally. Saussure did not secretly invent attention in 1916, and structural linguistics is not a machine-learning architecture.

Language models are spectacular evidence for how much competence can emerge from structure learned inside symbolic data. They write, translate, debug software, explain physics and manipulate abstractions without first acquiring the farmer's relationship to cows or the child's relationship to fire.

The residue gets us extraordinarily far. It also leaves something behind.

A farmer's sentence may be the compressed endpoint of twenty years of encounters, other farmers' advice, veterinary knowledge and mistakes painful enough not to repeat. The model receives the sentence. The sentence enters a corpus. The corpus becomes training data. Regularities are compressed into weights.

Months later somebody asks:

> Are cows dangerous?

and the model gives an excellent answer.

What usually does not come back is the archaeology. Which part rests on repeated observation? Did five sources independently observe the same thing, or did four copy the fifth?

The conclusion survives. Much of the structure that earned it trust does not.

This is what I mean by saying an LLM's knowledge is **epistemologically flat**. A mathematical identity, an experimental result, an expert opinion, a rumor repeated ten thousand times and a plausible completion can all arrive through the same channel in equally polished English.

Wittgenstein's later philosophy pulled attention toward language as something that lives inside practice: activities, expectations, habits, rules and forms of life.[^wittgenstein]

“Fire” keeps linguistic company with *heat*, *smoke*, *burn* and *wood*. It also cooks food and destroys houses. You move your hand away from it. Someone shouts the word in a crowded building and an entire social machinery begins to move.

The word participates in life.

Emily Bender and Alexander Koller made a version of the same argument with a hyper-intelligent octopus. It taps an undersea cable between two stranded islanders, learns their patterns and cuts in to impersonate one of them. It can bluff past a coconut catapult. Then a bear attacks, the islander asks how to defend herself with sticks, and the octopus has nothing. Form alone, however much of it, is not meaning.[^octopus] I prefer dead Europeans to cephalopods, but the point is the same.

A pretrained model inherits the linguistic residue of our practices. A deployed agent can begin to re-enter them: running code, using tools, observing users, interacting with institutions.

But embodiment cannot be the whole answer. I know far too many things I have never touched, measured or personally witnessed. I have never measured the speed of light. I have never been to Antarctica. I have no direct embodied evidence for most of modern physics, most of history or whether penguins are currently wandering through Rome. Direct contact does not scale.

So how do we know anything beyond it? For that, we need Alberto.

## Call Alberto

Suppose someone tells me that penguins live in Italy.

I have never conducted a census of Italian penguins. I cannot personally inspect every forest, coastline and piazza.

So I call Alberto. Alberto lives in Rome.

“Alberto, do penguins live in Italy?”

He laughs. I now know more than I did five minutes earlier.

Not with mathematical certainty. Alberto could be wrong. He may misunderstand the question. An escaped penguin could at this very moment be crossing Piazza Navona and destroying the example.

But Alberto occupies a useful position in the trust chain. He is there. He has repeated exposure to Rome. I have a history with him. If he repeatedly lies to me about things he is well positioned to observe, I update my trust in Alberto. If he says, “I don't know about all of Italy, but I've never seen one in Rome,” the boundary of his knowledge is itself useful information.

Testimony comes with metadata.

And we are all Alberto to someone. Someone may trust me on ranking systems because I have spent years working on them. Someone else may trust me about Jordan because I have lived there. If I begin confidently explaining marine biology, the correct response is not to transfer my credibility from machine learning to whales merely because the same mouth is speaking.

## It Starts With a Face

We learn all of this early, and we do not start with evidence.

An infant trusts a face before it has words for anything. My mother's face meant food, warmth and safety. Nothing I have believed since has been better supported. That trust was earned the way the tongue-ear test is settled, by contact: the face appeared and things got better, thousands of times.

Then the face started making claims. *Hot. Don't touch. That one bites.* I could not check most of them, and the few I checked the hard way came out in her favor. Every claim that held at the bottom paid credit upward to its source. I believed what she told me was good or bad. Then I believed the people she trusted.

Siblings contributed an important epistemological innovation: **some testimony is bullshit**. A brother will say anything with total confidence. You learn to ask who is speaking and what he gets out of it, years before anyone teaches you the word *incentive*.

Then teachers told me about atoms, dinosaurs and wars none of us could verify. I believed them because my mother had sent me to that school, and because the parts I could check, the spelling and the sums, held up. From there the chain runs on to books, to the institutions that print them, and to a whole society's machinery for deciding what to believe.

At no point did I build my knowledge from the ground up. I grew trust upward from a face.

Each layer was built on the one below it and reached a little further from anything I could touch. Nothing was replaced wholesale. When a layer failed, when the brother was lying or the textbook was out of date, I repaired that part and kept the rest. Knowledge goes up the way a city does, by addition and repair on top of what is already standing. Nobody gets to start from an empty field.

Human knowledge is **epistemologically stratified**.

“I touched the fire” is not the same as “my brother told me.” “My teacher said so” differs from “the experiment was independently replicated.” A measurement differs from an interpretation. A conjecture differs from an established result.

Mature trust is not purely conservative either. Sometimes the instrument disagrees with the theory. At first you check the instrument. Then you repeat the experiment. If the anomaly survives long enough, eventually the trusted theory becomes the thing under investigation.

Productive distrust requires trust first. Random distrust is just another form of stupidity.

Models inherit the text produced along the way, but usually not the live relationships underneath it. The paper, the article about the paper, the blog post disagreeing with the article and the Reddit thread where somebody confidently misunderstood both can all end up in the same training distribution. The model got the library without the childhood.

The model has no Alberto: no live record of who was positioned to know, where a claim came from, how its source behaved before, or where the source's competence stops.

There is one more ingredient humans add almost without noticing: stakes.

If Alberto lies to me repeatedly, I stop trusting him. If a researcher fabricates data and gets caught, the cost can be enormous. If an engineer signs off on a bridge and the bridge fails, “but the analysis sounded plausible” is not a defense.

Stakes are not truth. People lie despite consequences and institutions reward confident nonsense all the time. But consequences shape testimony. If a friend asks where to eat, I may guess. If someone asks whether to undergo surgery, I become much more careful.

An LLM has no social capital of its own to lose. It can confidently produce something false and, at the level of the model itself, nothing happens. The cost lands elsewhere: on the user, the application or the institution deploying it.

The danger is coherence outrunning correspondence. The machine can become extraordinarily good at tongue without having an ear available to check against. The dangerous failures are not the ones that crash. They are the ones that seem to work: decaf confidence, indistinguishable from the real thing until the moment it matters.

## System 3

We are currently obsessed with making models think harder.

System 2 reasoning has become a product category. Give the model more inference time, let it plan, search, reconsider and work through difficult problems before answering.

But reasoning perfectly from a bad premise still produces a beautifully reasoned mistake. A research agent can spend six hours developing an elegant argument from a false paper. A coding agent can reason carefully about an API that never existed. Deep Mode can coordinate five sophisticated judgments that all trace back to one hallucinated claim.

At some point, thinking has to encounter something outside itself.

Kahneman's *Thinking, Fast and Slow* gave us the familiar distinction between System 1, fast and intuitive cognition, and System 2, slower and more deliberate cognition.[^kahneman]

For AI, the analogy is tempting. The base model looks something like System 1: fast pattern recognition, linguistic intuition, enormous associative capacity. Agentic reasoning adds something like System 2: decomposition, planning, reflection and extended search.

But human thought has always operated inside another structure that the two-system picture largely takes for granted. We test things, build instruments, ask other people and preserve our failures.

I call that external epistemic machinery System 3.

**System 1 proposes. System 2 deliberates. System 3 checks.**

I keep another mnemonic because I am apparently incapable of leaving a three-part system alone:

**System 1 is the Gut. System 2 is the Head. System 3 is the Hand.**

The Gut recognizes. The Head reasons. The Hand reaches outside the current story and finds something capable of disagreeing.

The metaphor is imperfect. Peer review has no hand, provenance has no fingers and a formal proof does not need to touch a cow.

System 3 is the external scaffold that keeps thought answerable to observation, experiment, provenance, persistent failures, tools and other minds.

And this is where the naming matters. Deep Mode is Layer 3: the problem-solving layer. System 3 is not another layer above it.

Deep Mode asks: *Given what we know, what should we try next?*

System 3 asks: *What are we entitled to treat as known?*

It cuts across the stack. The model proposes something. The coding agent may test it. The application can collect real user behavior. Deep Mode may compare research, simulation and evaluation. Even Layer 4, the goal itself, can change when reality pushes back.

If the five layers tell us where increasingly abstract work happens, System 3 is what keeps those layers epistemically connected. Without it, delegating more of the work can give an unsupported claim more places to travel.

Put on one page, the stack and the thing that cuts across it look like this:

| Layer | The question it answers |
|---|---|
| 4 — Intention | What do we actually want? |
| 3 — Deep Mode | Given what we know, what should we try next? |
| 2 — Application | Can the work begin near the application instead of the plumbing? |
| 1 — Agent | Can the model act, and see what happened? |
| 0 — Model | What does the pattern suggest? |
| **System 3, across all of them** | **What are we entitled to treat as known?** |

## Code Can Touch Back

Code is unusually friendly to this idea because coding agents can touch their world.

When an agent writes code and runs it, reality answers back.

`TypeError: 'NoneType' object is not subscriptable` is not merely another paragraph describing Python. It is the execution environment saying: whatever story you just told yourself about this program, this particular part is wrong.

The agent can try something, observe the result, update and try again. The farmer approaches the cow and learns from the kick. The coding agent calls an API incorrectly and learns from the exception. The cow is probably more emotionally memorable, but structurally the loops rhyme.

This is one of the few places where a language model can, metaphorically, touch the ear.

The question is whether the system preserves what it learns there.

A normal agent session can fail ten times, discover the right approach, solve the problem and throw away most of the experiential history when the context ends. It is as if the farmer learned exactly where not to stand and then underwent elective amnesia every evening.

The MARC file incident shows the opposite move. In the Live-SWE-agent work, an agent encountering MARC files, the old bibliographic format used by libraries, created an analyzer to inspect data its existing tools could not conveniently expose.[^liveswe]

The environment resisted. The agent's current apparatus was not enough, so it created an instrument. That instrument changed what the agent could observe.

Humans have been doing this forever. We could not see bacteria, so we built microscopes. We could not perceive radio waves directly, so we built receivers. We could not conveniently inspect a MARC file, so apparently we wrote Python and called it epistemology.

That is System 3 in miniature.

AlphaGo offers another useful distinction. Its neural network supplied powerful intuition about promising moves and valuable positions. Monte Carlo Tree Search placed that intuition inside an explicit search process constrained by the state and consequences of Go.[^alphago]

I used to summarize this too simply as “the network proposes; the tree verifies.” That gives the tree too much authority. MCTS does not magically prove the network right. It forces intuition to participate in an external, stateful process where moves have consequences defined by the game rather than by what the network can plausibly say about the game.

RL can improve the gut. System 3 preserves more of the structure around the gut: what was tried, what happened, which paths failed, where claims came from, which tools earned confidence and where their boundaries lie.

## A Hallucination With Better Retention

Return to the research claim about recursion trees:

> Students understand recursion better when shown a tree representation.

In a flat architecture, the sentence enters context and competes with every other sentence according to relevance and whatever confidence the model implicitly assigns it.

A trust-aware architecture wants more. Where did the claim come from? A controlled study? A teacher's opinion? A blog post? What population was tested? Does the result apply to our demo?

You do not need a bureaucratic dossier attached to every sentence. Sometimes “Alberto said the café is good” is enough.

But when the consequence matters, the claim should be able to carry provenance.

That is a **trust chain**: a record of how far a claim sits from the evidence supporting it, what transformations happened along the way and which links we have chosen to trust. It does not guarantee truth.

A skill is knowledge externalized from the model. Someone, or some previous agent, learned something useful and wrote it down so later sessions would not need to rediscover it.

But persistence is not trust. A terrible heuristic written into a skill file is simply a hallucination with better retention.

A useful skill needs some archaeology. Who created it? Where did it work? Where did it fail?

Suppose an agent learns:

> Prefer structured parsers over regex for deeply nested formats.

A flat skill stores the rule. A richer object can record that the heuristic came from several failed regex attempts, later worked across multiple nested formats, remains unnecessary for simple flat extraction and should be treated as a strong prior rather than a commandment.

Tools can earn trust in the same way. If `edit_tool.py` succeeds on simple substitutions but repeatedly damages indentation-sensitive blocks, the useful knowledge is *this tool is reliable here and dangerous there*.

The same applies to softer heuristics. “Regex tends to fail on deeply nested structures” is a **meta-belief**: something that can accumulate evidence for and against it.

A normal rule says:

> Never use regex here.

A System 3 belief says:

> This has worked often enough that I should prefer it, but new evidence can change my mind.

If you enjoy old epistemology labels, you can call the model a largely coherentist core, uncannily good at producing structures that hang together, and System 3 a thin foundationalist shell tied to observation, provenance and consequence. Philosophers can put down their weapons; I only need the architectural analogy.

Coherence is valuable, but something outside the coherent system must occasionally be allowed to say no.

This is personal for me. I spent eight years building systems that rank human testimony: reviews, ratings and Q&A. The hardest problem was never only relevance. It was trust stratification. Which claims deserve corroboration? What happens when ten accounts repeat the same lie? When does consensus become evidence and when is it coordinated manipulation? How far should credibility transfer outside the domain in which it was earned?

These are not abstract questions when they determine what millions of people believe about a product.

**System 3 isn't philosophy to me. It's Tuesday.**

## The Epistemic Agent

I wanted to test a smaller claim than “we solved epistemology for AI.”

Could even crude epistemic structure around a coding agent change how it behaves?

We built a small agent called epistemic-swe. It added three kinds of persistent state around a normal coding agent.

A **tool registry** tracked tools, successes, failures and known failure modes. **Meta-beliefs** allowed heuristics to accumulate evidence instead of entering the system as permanent commandments. **Failure memory** preserved enough information about failed approaches to make blindly repeating them less likely later.

The state persisted across sessions, so later problems could inherit things learned earlier. We also pruned it. An epistemic architecture that remembers everything eventually becomes a hoarder with a context window.

We compared mini-swe-agent with epistemic-swe on ten SWE-bench Verified problems from the Astropy repository, using the same base model and tasks.[^swebench]

Ten problems is nowhere near enough to establish a solve-rate advantage. State persisted across tasks, so order effects may matter. I was not looking for a benchmark victory. I wanted to know whether the scaffold changed behavior strongly enough to become visible.

It did, just not in the direction I expected.

| Metric | mini-swe-agent | epistemic-swe |
|:--|:--|:--|
| Solve rate | 50% (5/10) | 40% (4/10) |
| Average patch size | 620 lines | 269 lines |
| Patch reduction | baseline | 57% smaller in this run |

Read the first line before celebrating the third.

The epistemic agent solved fewer problems. I had expected learning from previous failures and tools to improve capability. Instead, the clearest difference was focus: its patches became much smaller.

A few examples:

| Problem | mini | epistemic | Ratio |
|:--|--:|--:|--:|
| astropy-12907 ✓ | 301 lines | 61 lines | 4.9x smaller |
| astropy-13453 ✓ | 266 lines | 17 lines | 15.6x smaller |
| astropy-14096 ✓ | 529 lines | 70 lines | 7.6x smaller |
| astropy-13977 ✗ | 2720 lines | 362 lines | 7.5x smaller |

The last row deserves a second look. That one failed baseline patch holds more than two-fifths of all the baseline's lines. Leave the problem out and the average reduction falls from 57 percent to about a third. The pattern holds; the headline number flatters it.

The baseline often left behind debris from exploration: temporary scripts, broader edits, test scaffolding and abandoned experiments. The epistemic agent tended to make more surgical changes.

That does not prove the trust stack caused the reduction, and smaller patches are not automatically better patches. The extra instructions may simply have made the agent more conservative. Persistent state may have changed behavior for reasons unrelated to my epistemic interpretation. Ten tasks from one repository cannot separate these explanations.

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

A mature System 3 therefore needs more than accumulation: forgetting, counterexamples, challenge, competing possibilities and occasional permission to ignore what it thinks it knows.

## Creative Distrust

Trusted knowledge makes you efficient. It can also make you boring. If an agent learns that tree visualizations worked for five recursive algorithms, eventually it may try to explain linear regression with a tree because the trust stack has become stronger than judgment. On 13579, knowledge about indexing may have made the wrong explanation harder to leave.

Every genuinely new idea begins with less evidence than the thing it challenges.

From inside the chain it looks, at first, exactly like the bullshit.

So System 3 needs **creative distrust** too.

I do not mean contrarianism for sport, or the internet habit of assuming expert agreement proves corruption. Creative distrust is the ability to understand a trust chain well enough to know where you are breaking it and why.

A scientist repeats a strange experiment after accepted theory says the result should not happen. A designer violates a trusted pattern because this case exposes its boundary conditions.

A mature trust stack has two jobs pulling in opposite directions: let knowledge accumulate so we do not rediscover fire every morning, and leave enough room for reality to overthrow what accumulated.

## Back to the Camel

Return to the seven claims.

**1. Krka National Park: true.** I was there. For me this sits close to embodied memory. For you it is testimony unless you extend the chain through records or other evidence.

**2. Best philosophical thinking at waterfalls: false.** I mostly do philosophy on buses and in boring waiting rooms. Waterfalls are for ice cream. The subject and the source are unfortunately the same man.

**3. Permanent camel resident: false.** This can be checked against information about the park. You do not need my biography.

**4. The tongue can touch its own ear: unknown.** I genuinely do not know. I did not check. Neither did you. We can reason from anatomy and build a prior, but the shortest decisive chain would have been to stay there and watch.

**5. Ice cream ten minutes earlier: true.** Chocolate. Mostly testimony again.

**6. Camels are native to the Dalmatian coast: false.** You probably rejected this immediately without reconstructing camel evolutionary history or personally surveying Dalmatian fauna. A large inherited structure did that work for you.

System 1 can be fast because System 3 has often been working for centuries underneath it.

**7. Real, unedited photograph: true.** The image alone cannot establish that. A stronger chain might include the original file, metadata, cryptographic signing, independent witnesses or another provenance system. Every extra link can increase confidence and gives us one more thing that may itself need to be trusted. And I could be lying to prove a point about trusting sources. If I told you the photograph was AI-generated, you would probably believe that too, because it fits a pattern you recognize.

Welcome to epistemology.

The lesson is not that nothing can be known. That conclusion is dramatic and mostly useless.

The lesson is that **trust has structure**.

The model can remain what it is: an extraordinarily general machine for navigating learned patterns, capable of intuition and increasingly capable of reasoning. It does not need to contain the entire chain inside its weights.

**The model stays hollow. The system doesn't have to be.**

Daniel Dennett's phrase for the first half is competence without comprehension.[^dennett] Whether the second half amounts to comprehension is a question for people with more patience than I have; the part of it that can be checked is the part the rest of this book builds.

Everything so far can still be imagined around one agent: it acts, checks, remembers, records provenance and updates what it trusts.

Real systems will not stay that simple. The moment one agent inherits a claim from another, no participant can personally reconstruct every path back to reality. A trust chain can preserve where a claim came from. It does not, by itself, tell us how the knowers who depend on those chains should be arranged.

The question is no longer simply:

> How can an AI know what to trust?

It is:

> **How can a population of fallible knowers build knowledge together without losing contact with the world?**

Humans have been working on that problem for a very long time.

---

[^saussure]: Ferdinand de Saussure, *Course in General Linguistics*, 1916, on the arbitrariness of the sign and linguistic value. See also the *Third Course of Lectures on General Linguistics*, 1910–1911, student notes published in English in 1993. <https://www.marxists.org/reference/subject/philosophy/works/fr/saussure.htm>.

[^wittgenstein]: Ludwig Wittgenstein, *Philosophical Investigations*, 1953, especially §§23 and 43 on language-games and meaning as use.

[^octopus]: Emily M. Bender and Alexander Koller, “Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data,” *Proceedings of ACL*, 2020, pp. 5185–5198, section 4.

[^kahneman]: Daniel Kahneman, *Thinking, Fast and Slow*, 2011.

[^liveswe]: Chunqiu Steven Xia, Zhe Wang, Yan Yang, Yuxiang Wei, and Lingming Zhang, “Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?”, 2025, [arXiv:2511.13646](https://arxiv.org/abs/2511.13646).

[^alphago]: David Silver et al., “Mastering the Game of Go with Deep Neural Networks and Tree Search,” *Nature* 529, 2016, pp. 484–489.

[^swebench]: Carlos E. Jimenez et al., “SWE-bench: Can Language Models Resolve Real-World GitHub Issues?”, 2023, [arXiv:2310.06770](https://arxiv.org/abs/2310.06770); SWE-bench Verified is the human-validated subset released with OpenAI in August 2024. mini-swe-agent is the SWE-agent team's minimal bash-only scaffold.

[^dennett]: Daniel C. Dennett, *From Bacteria to Bach and Back: The Evolution of Minds*, 2017.

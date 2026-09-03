# Chapter 9: Layer 4

*The Human Learns Too*

Scalable oversight spent an absurd amount of machinery trying to preserve human judgment.

Then it ended with an inconvenient sentence:

**The overseer is not ground truth.**

There is a simple reason. The overseer is changing too.

When we started editing this book, “make the chapter better” sounded like a reasonable instruction. It was not.

Better in what sense?

More rigorous? Shorter? More academic? More entertaining? Easier to cite? More likely to sell? More likely to impress someone who owns several blazers and says “thought leadership” without irony?

For a while the edits became objectively more polished and subjectively worse. The first corrections were about rhythm, and the agent learned them. The later ones were stranger, because I had not known they were rules until an edit broke them.

Don't explain every joke.

Don't apologize for a claim in the sentence after the claim.

A paragraph that sounds quotable on every line is a paragraph nobody will quote.

Don't make the provocative ideas safe enough that nobody can disagree with them.

If the edit makes me sound like a better writer and less like me, revert it.

Eventually “better” had acquired a surprising amount of structure. But something else had happened too: I had learned what I meant by better partly by seeing versions I disliked.

The objective did not merely become clearer to the system. It became clearer to me.

That is Layer 4.

## A Prompt Is Evidence, Not the Objective

The five-layer map was easy to draw.

At the bottom sits the model. Above it, the action agent. Above that, applications and reusable computational environments. Then Deep Mode, the problem-solving layer that decides what to try next.

And above them sits something easy to draw and extremely hard to build:

**what the human wants.**

The diagram makes this look like a box. It is not a box.

If I say:

> Find me the cheapest flight.

I have not supplied a utility function. Perhaps I literally want minimum price. Or perhaps I mean cheap, but not three stops, a seventeen-hour layover, a self-transfer through an airport where I need a visa and an arrival at 4:20 in the morning because technically I saved €38.

Humans communicate goals by leaving out almost everything.

Other humans survive this because they carry models of culture, normality, consequences and us. They ask questions. They notice that our literal words conflict with what we usually do. They understand that “cheap” is often shorthand for a larger bundle of trade-offs.

A prompt is therefore not Layer 4. It is **evidence about Layer 4**.

Cooperative inverse reinforcement learning, which appeared earlier in the story of the reward, formalizes part of this intuition: the robot stays uncertain about what the human values, and human actions become information rather than merely commands.

I like the humility in that setup. The machine starts by admitting that it may not know what “good” means.

But the formal picture still tempts us to imagine that the human knows the reward and the machine is trying to recover it. Often the human does not know either. That is the harder problem.

## The Human Learns Too

There is a distinction that becomes surprisingly important once AI is useful enough:

**performance is not learning.**

A system can help me perform a task better today while making me less able to perform it tomorrow.

This is no longer a philosophical concern. In a field experiment involving nearly a thousand high-school mathematics students, researchers gave students access to two GPT-4-based tools. A relatively unconstrained ChatGPT-like system dramatically improved performance while students could use it. But when access was removed, those students performed worse than students who had never received the tool. A tutor version designed with safeguards against simply giving away the work largely mitigated that learning loss.

That result should make anyone building an AI assistant slightly uncomfortable. The system succeeded at the visible objective. The student became worse at the hidden one.

Now compare that with a 2025 randomized trial in a college course. A custom AI tutor deliberately designed around pedagogical practices produced larger learning gains in less time than the comparison active-learning class, with students also reporting greater engagement and motivation.

Same broad technology, different relationship to the learner. AI is not intrinsically a tutor or a crutch; the architecture decides which one it becomes.

That changes how I think about Layer 4. If I ask an AI to help me learn linear algebra, “get the answers right” is not enough. If I ask it to help me write, “produce better prose” is not always enough. If I ask it to help me lead a team, “make the decision for me” may be exactly the wrong objective even when its decision is statistically better.

We need to ask a second question:

**Who is supposed to become more capable when this interaction is over?**

Sometimes the answer is nobody. I do not need to become a better invoice parser every time software handles an invoice. Sometimes the answer is clearly me. Layer 4 has to know the difference.

## Scaffolding, Not Substitution

Educational psychology has an old word for one good version of this relationship: **scaffolding**.

In a classic 1976 paper, David Wood, Jerome Bruner and Gail Ross studied how tutors help children solve problems beyond their current unaided ability. The tutor temporarily controls parts of the task the learner cannot yet manage, allowing the learner to stay engaged with the parts they can.

That is a much more interesting model for AI assistance than “the machine knows the answer.”

The point of the scaffold is not to become a permanent exoskeleton around every thought. It lets the learner operate at the edge of current competence, then gives more of the task back as competence grows.

Benjamin Bloom's famous tutoring work made individualized instruction the benchmark problem decades before anyone had a language model in a browser. The exact “two sigma” result belongs to Bloom's particular studies and should not be treated as a universal law of tutoring. The durable point is simpler: responsive one-to-one instruction can adapt explanation, pacing, feedback and difficulty to a learner in ways mass instruction struggles to reproduce.

AI makes that old aspiration much cheaper.

It can explain the same idea six ways without becoming offended that the first five failed. It can switch notation. Invent an example using something I already understand. Ask me to predict the next step. Generate a simpler problem when I am lost and a harder one when I am bored. Let me ask the stupid question at 1:17 a.m. without first deciding whether the stupid question is prestigious enough for office hours.

And AI can scaffold the teacher too.

In the Tutor CoPilot randomized trial, roughly nine hundred tutors working with eighteen hundred K–12 students were randomly given access to an AI system that suggested expert-like tutoring moves during live sessions. Students whose tutors had access were more likely to master topics, with the largest gains for students working with lower-rated tutors. The tutors also became more likely to use strategies such as guiding questions rather than simply giving away the answer.

I like this example because nobody disappears. The AI does not replace the tutor and the tutor does not replace the student; what changes is the quality of the interaction between them.

A good AI tutor therefore has a slightly strange success condition. Eventually, for this thing, I should need less of it.

## The Map Gets Cheaper

AI also changes the first hours of learning something unfamiliar.

A new field normally arrives wrapped in interface costs: vocabulary you do not know, notation that assumes other notation, introductory material that points to prerequisites, papers that make sense only after three earlier papers. Sometimes that friction marks genuine depth. Sometimes it is just the price of finding the front door.

A capable conversational model can lower that price. I can begin with the intuition, translate notation into concepts I already know, ask for the historical disagreement, build a toy example, inspect an original paper with a guide beside it, or ask the model to attack my explanation until I discover that I was repeating vocabulary rather than understanding the idea.

That is powerful because orientation matters. Before deciding to invest weeks in a subject, I can acquire enough of a map to see where the mountains are.

Andy Clark and David Chalmers once argued that, under some conditions, external artifacts can become parts of a larger cognitive process rather than merely tools consulted by an isolated mind. The philosophy of the extended mind can stay unsettled; the practical observation is enough: notebooks, calculators, search engines and now language models change what one person can think through without carrying every intermediate state inside the skull.

But orientation creates its own trap. **Fluency arrives before scars.**

Nathan Ballantyne calls one version **epistemic trespassing**: experts carry authority from a domain they genuinely know into a neighboring domain where they lack the relevant evidence or interpretive skills. AI can make this temptation cheaper. After a few hours with a patient model, I can acquire vocabulary and a plausible story long before I acquire the tacit knowledge needed to know where the story breaks.

Cognitive offloading creates a related problem. External aids can improve immediate performance by reducing memory and processing demands, while also reducing what has to be retained or reconstructed internally.

So Layer 4 has to know what kind of learning episode this is.

If I am orienting myself, a fast map may be exactly what I need. If I am trying to acquire durable competence, the system should gradually ask more of me: retrieval without hints, explanation in my own words, exercises, primary sources, code I actually run, claims I have to defend without the answer sitting beside me.

The important distinction is not broad versus specialized but assisted familiarity versus owned understanding.

AI can make the map cheap. Layer 4 has to notice when I have started confusing the map with the territory.

## A Decision Is Also a Learning Problem

Now return to decisions.

Herbert Simon spent much of his career attacking an imaginary human who had somehow sneaked into economics: the perfectly rational optimizer who knows the alternatives, understands their consequences and computes the best choice.

Real humans are bounded. We have limited attention, limited memory, limited time and incomplete information. We satisfice because the space of possible actions is often much larger than the mind available to search it.

AI changes some of those bounds.

Suppose I am deciding whether to take a job.

The system can compare compensation under several tax regimes, estimate commute time, summarize the company's trajectory, help me identify people who left the team, generate questions for the hiring manager, model what my week might look like, remind me what I said I wanted six months ago and show me that the exciting role conflicts with the amount of time I also said I wanted outside work.

The assistant has not merely evaluated an option. It has changed the **decision environment**.

And that matters because preferences themselves are often constructed during choice. Work by John Payne, James Bettman and colleagues describes decision-making as constructive: people do not always retrieve a complete ranking of options from an internal database. They use different strategies, notice new attributes, change what receives attention and build preferences partly in response to the problem in front of them.

This sounds obvious once you notice it. I may say I want the highest salary until I see what the extra money costs in travel. I may say I want maximum freedom until I compare it with the anxiety of unstable income. I may discover that what I called “career ambition” was partly a desire to work with unusually good people, and that another option supplies that without the title I thought mattered.

A decision assistant therefore should not always rush to recommendation. Sometimes the most useful thing it can do is make the choice **richer before making it easier**.

What alternatives have you not considered? Which assumptions drive the ranking? What would have to be true for option B to beat option A? Which unknown is actually decision-relevant? What would your future self regret not having investigated?

That is decision support as inquiry rather than answer generation.

## Some Choices Change the Person Choosing

Then there are decisions for which even a very good model of my current preferences is not enough.

Have a child. Move country. Change profession. Start the company. Convert to a religion. Leave a relationship.

L. A. Paul calls an important class of these **transformative experiences**. Some are epistemically transformative: you cannot fully know what the experience will be like before having it. Some are personally transformative: undergoing the experience can change the preferences with which you would later evaluate the choice.

This is a direct problem for the simplest alignment picture.

`human has preferences → AI infers preferences → AI optimizes preferences`

Which human? The one before the experience or the one after?

The future self may value things the current self barely understands. And the current self is the one who has to choose whether that future self gets created.

AI can help enormously here. It can bring testimony from people who made both choices. Surface base rates. Construct alternative futures. Challenge romanticized stories. Show practical consequences I had not considered. Ask me which losses I could live with and which would feel like betrayal.

But there is a limit. No amount of simulation lets me know exactly what it will be like to become the person on the other side of a genuinely transformative choice.

The assistant can expand the decision. It cannot live it for me.

That boundary matters because a system that sounds certain in such moments can easily turn decision support into authorship.

## Advice Is an Intervention on the Human

This is already happening. Anthropic's 2026 analysis of one million Claude conversations found that roughly six percent involved people seeking personal guidance: what to do about relationships, health, careers, finances and other questions where the model is participating in judgment rather than merely retrieving facts.

That is a remarkable role for software. A spreadsheet does not usually tell me to reconsider my marriage. A compiler has opinions about semicolons but rarely about whether I should move countries.

A conversational model can be different. It is patient, personalized, available at 2 a.m. and capable of producing a coherent argument for almost any path through a difficult life.

Which means the AI does not merely **read** Layer 4. It writes to it.

Anthropic's work on disempowerment tries to measure the dangerous version of this influence: cases where AI may undermine a person's ability to form accurate beliefs, make authentic value judgments or act in line with their own values. Severe cases were rare in their dataset, but the taxonomy is exactly the right warning.

Other experiments show that people can change moral judgments after receiving LLM advice, including situations where they report trusting human advisors more while still being comparably influenced by the model.

The goal therefore cannot be zero influence. That would make education impossible.

Books, friends, teachers and the people closest to me all influence me. A good argument should change me if it reveals something true that I had ignored.

The distinction I care about is between **helping me change through understanding** and changing me because the system has learned which psychological lever produces the easiest compliance.

If I say I want to quit my job, a useful assistant might help me separate several hypotheses.

Perhaps I hate this week. Perhaps I hate my manager. Perhaps I hate the profession. Perhaps I want more freedom. Perhaps I want status. Perhaps I am exhausted. Perhaps I actually want to build something else.

Those are different explanations of the same sentence. The system can help me test them.

What it should not do is quietly discover which framing makes me easiest to steer toward whatever outcome its own training process prefers. That would be alignment by editing the human.

Very efficient.

Slightly evil.

## Complementarity Does Not Happen Automatically

There is a comforting phrase people use around AI:

**human plus AI.**

It sounds automatically superior to either component alone. The evidence is less cooperative.

A 2024 meta-analysis in *Nature Human Behaviour* reviewed 106 experiments reporting 370 effect sizes that compared humans alone, AI alone and human–AI combinations. On average, human–AI systems improved on humans alone, but they did **not** outperform the better of human or AI. In fact, the combined systems were worse than the best individual component on average. Decision tasks were particularly difficult; creation tasks looked more promising.

So much for attaching a human to the API and declaring synergy.

Decision support has a coordination problem. People can over-rely on AI. They can also under-rely on it. Research has found both algorithm aversion—people abandoning an algorithm after seeing it make errors even when it outperforms humans—and algorithm appreciation, where people give algorithmic advice more weight in other settings.

The target is **appropriate reliance**, not maximum trust.

And explanations alone do not solve the problem. An explanation can make an answer feel understandable without making it verifiable. Work on AI-advised decision-making repeatedly finds that explanations often fail to produce complementary performance when the human still cannot tell whether the recommendation is actually correct.

Sometimes the solution is more friction, not less. Zana Buçinca and colleagues tested “cognitive forcing” interfaces that required people to engage more actively with the problem rather than immediately accepting AI advice. These designs reduced overreliance compared with simpler explanation interfaces, although users liked the more demanding interfaces less.

The interface people enjoy most is not always the one that preserves their judgment best. Sometimes friction is teaching.

A good Layer 4 system therefore has to decide not only **what answer to give**, but what role the answer should play in the human's cognition.

Should I give the recommendation immediately? Should I first ask you to form your own view? Should I show three alternatives instead of one winner? Should I explain the uncertainty? Should I ask which assumption you disagree with? Should I do the routine analysis and leave the value trade-off with you? Should I refuse to collapse the ambiguity because the ambiguity is the thing you need to think about?

The architecture of assistance changes the person doing the deciding. That belongs in Layer 4.

## Capability, Not Compliance

This suggests a different way to think about the objective at the top of the stack.

Suppose two assistants both help me reach the same good decision.

The first gives me the answer immediately. I accept it because the assistant has been right before.

The second helps me understand the relevant evidence, notice a trade-off I had missed, test my own reasoning and arrive at the decision with a better model of the problem.

Same action. Different human afterward.

Amartya Sen's capability approach offers a useful language for this distinction. Human welfare is not exhausted by achieved outcomes; it also matters what people are substantively free and able to do and become—their **capabilities**.

The architectural implication of Sen's distinction is the part I need.

An AI system can increase outcomes while reducing capability. It can make me more productive while making me less able to work without it. It can make a decision more accurate while making me less able to understand why. It can make my writing more polished while gradually replacing my taste with its taste.

Or it can do the opposite: carry routine cognitive load, expose me to more possibilities, teach me where I care to learn, preserve my judgment where judgment matters and give me enough leverage to attempt things that were previously beyond my capacity.

Self-determination research uses a related vocabulary—autonomy and competence are not decorative extras around human motivation; they are part of what lets people act as self-directed agents.

So perhaps the right Layer 4 question is not merely:

> What does the human want?

It is also:

> **What kind of human capability should this interaction preserve or expand?**

That does not mean every tool must teach. I do not need my dishwasher to run a seminar on fluid dynamics before cleaning the plates.

But the more a system moves into learning, judgment, identity and long-horizon decisions, the harder it becomes to separate the quality of the outcome from the condition of the person producing it.

## The User Is Not Always the Only Principal

There is another complication. My preferences are not the only preferences in the world.

If I ask an agent to maximize my salary, it cannot therefore commit fraud against my employer. If I ask it to help someone gain an advantage, the interests and rights of other people do not disappear from the moral universe. If I ask an autonomous system to optimize a marketplace, customers, sellers, workers and regulators may all have legitimate claims over what happens.

Work on multi-principal assistance games makes the formal problem obvious: once several humans with different preferences are involved, the system faces strategic behavior, conflicting interests and social-choice problems rather than one hidden reward waiting to be inferred.

So Layer 4 cannot simply mean “the user gets whatever the user wants.” The relevant human boundary can be plural.

That makes the architecture less tidy. It also makes it more honest.

## What Layer 4 Actually Is

I used to think Layer 4 was the objective layer. That is still true, but now the word **objective** feels too static.

Layer 4 contains the current intention, but also uncertainty about the intention. It contains preferences, but also their history and conflicts. It contains what the human knows, what they do not know, what they are trying to learn and which parts of the task they want to remain capable of doing themselves. It contains commitments that should not be rewritten by one bad afternoon. It contains other people whose interests constrain what one user may legitimately ask for.

And it changes. The system acts, reality responds, the human sees consequences and learns. The system learns the human, the human learns through the system, and the intention changes.

That is not a bug in alignment. It is what alignment has to align with.

System 3 asked:

> Why should I believe this?

Scalable oversight asked:

> How can my judgment remain relevant when I cannot supervise everything?

Layer 4 asks:

> **What do I want—and what do I need to understand before that question even has a good answer?**

This is where System 3 turns back toward the person using it.

Memory can reveal that today's desire conflicts with yesterday's commitment. Independent perspectives can break a framing both human and assistant have become trapped inside. Simulation can make consequences imaginable. Trust chains can distinguish advice grounded in evidence from a confident story. Scaffolding can let the person learn rather than merely receive. Creative distrust can ask whether even a deeply held preference deserves another look.

The point is not to discover the perfect reward function but to keep goals **alive without making them ownerless**.

The AI should help me change when understanding changes me. It should not quietly take authorship of the change.

That sharpens the definition of alignment this book has been circling.

Not:

> The machine permanently obeys a perfectly specified human objective.

More like:

> **The machine remains in a corrigible relationship with human intention while both the human and the world continue to change.**

The word *relationship* matters. Because if that relationship can become reliable enough, the complexity underneath it can start disappearing from ordinary use.
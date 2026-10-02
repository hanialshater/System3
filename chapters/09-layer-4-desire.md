# Chapter 9: The Desire Layer

*The Human Learns Too*

Find me the cheapest flight.

I have not supplied a utility function. Perhaps I literally want minimum price. Or perhaps I mean cheap, but not three stops, a seventeen-hour layover, a self-transfer through an airport where I need a visa and an arrival at 4:20 in the morning because technically I saved €38.

Humans communicate goals by leaving out almost everything. Other humans survive this because they carry models of culture, normality, consequences and us. They ask questions. They notice that our literal words conflict with what we usually do. They understand that “cheap” is often shorthand for a larger bundle of trade-offs.

That can be a communication problem. I may know perfectly well that I will pay €38 to avoid sleeping on an airport floor; I just failed to mention it. The assistant needs to ask, and I have an answer.

But put two reasonable itineraries in front of me and something else can happen. The cheaper one gives me another day with my family and costs me a miserable night of travel. Until I see those options together, I may not know how I weigh them. Asking the question has helped create the answer.

I learned this while editing this book. “Make the chapter better” sounded like a reasonable instruction. It was not. Better in what sense? More rigorous? Shorter? More academic? More entertaining? Easier to cite? More likely to sell? More likely to impress someone who owns several blazers and says “thought leadership” without irony? For a while the edits became objectively more polished and subjectively worse, and the corrections I found myself making were rules I had not known were rules until an edit broke them. Eventually “better” had acquired a surprising amount of structure. But something else had happened too: I had learned what I meant by better partly by seeing versions I disliked.

The objective did not merely become clearer to the system. It became clearer to me. And learning can change the person who will judge the next choice. A missing detail, an unformed preference and a changed mind can all look like an incomplete prompt. They need different kinds of help.

## A Prompt Is Evidence, Not the Objective

Chapter 3 left me in the vibe coder’s seat, deciding what to try next, and then handed much of that job to Deep Mode. Whatever remains mine once the system can choose its own next move, it is not the choosing. It is what the trying is for.

The five-layer map put that at the top of the stack and called it the desire layer. Drawn as a box, it looked like one more component waiting for an interface. A prompt gives the system evidence about the desire layer and leaves it to discover how much of the desire is settled.

Cooperative inverse reinforcement learning, which appeared in Chapter 7, formalizes part of this intuition: the robot stays uncertain about what the human values, and human actions become information rather than merely commands.[1](appendix-references.md#ref-09-l4-cirl)

I like the humility in that setup. The machine starts by admitting that it may not know what “good” means. But the formal picture still tempts us to imagine that the human knows the reward and the machine is trying to recover it. Often the human does not know either, and is in the middle of finding out.

To watch someone finding out, it helps to have someone. Imagine a hospital pharmacist—call her Rana. She is very good at drug interactions and has decided, at thirty-four, that she would like to work with clinical data. In the evenings she is learning statistics with an AI assistant. She is invented, the way Ines was in Chapter 6; the studies she walks through are not. Each section of this chapter asks her assistant a different question.

## Performance Is Not Learning

The first question is the easiest to see, because a classroom is a place where changing the human is supposed to be the point. Rana wants to understand regression, not to have regression done to her. A system can help her perform a task better today while making her less able to perform it tomorrow.

That has been measured. In a field experiment involving nearly a thousand high-school mathematics students, researchers gave students access to two GPT-4-based tools. A relatively unconstrained ChatGPT-like system dramatically improved performance while students could use it. But when access was removed, those students performed worse than students who had never received the tool. A tutor version designed with safeguards against simply giving away the work largely mitigated that learning loss.[2](appendix-references.md#ref-09-l4-bastani)

The system succeeded at the visible objective. The students became worse at the hidden one.

A 2025 randomized trial in a college course points the other way. A custom AI tutor deliberately designed around pedagogical practices produced larger learning gains in less time than the comparison active-learning class, with students also reporting greater engagement and motivation.[3](appendix-references.md#ref-09-l4-kestin)

Same broad technology, different relationship to the learner. Whether AI becomes a tutor or a crutch is decided by how it is built and used, not by the model.

Rana’s assistant can produce a flawless worked solution to every exercise she uploads. Her homework would improve overnight. Who is supposed to become more capable when this interaction is over?

For her invoices, nobody. I do not need to become a better invoice parser every time software handles an invoice, and neither does she. For regression, clearly her. The desire layer has to know the difference, and she is the only one who can tell it.

## Giving the Work Back

Educational psychology has an old word for the good version of this relationship: *scaffolding*.

In a classic 1976 paper, David Wood, Jerome Bruner and Gail Ross studied how tutors help children solve problems beyond their current unaided ability. The tutor temporarily controls parts of the task the learner cannot yet manage, allowing the learner to stay engaged with the parts they can.[4](appendix-references.md#ref-09-l4-scaffolding)

The scaffold is not meant to become a permanent exoskeleton around every thought. It lets the learner operate at the edge of current competence, then hands more of the task back as competence grows. In Rana’s first week the assistant shows every step of a regression. By the sixth it asks her to predict the sign of a coefficient before it fits anything, and she is annoyed, and she is learning.

Benjamin Bloom’s famous tutoring work made individualized instruction the benchmark problem decades before anyone had a language model in a browser. The exact “two sigma” result belongs to Bloom’s particular studies and should not be treated as a universal law of tutoring.[5](appendix-references.md#ref-09-l4-bloom) The durable point is simpler: responsive one-to-one instruction can adapt explanation, pacing, feedback and difficulty to a learner in ways mass instruction struggles to reproduce.

AI makes that old aspiration much cheaper. It can explain the same idea six ways without becoming offended that the first five failed. It can switch notation, or invent an example about drug clearance because that is what Rana already understands. It can generate a simpler problem when she is lost and a harder one when she is bored. And it lets her ask the stupid question at 1:17 a.m. without first deciding whether the stupid question is prestigious enough for office hours.

AI can scaffold the teacher too. In the Tutor CoPilot randomized trial, roughly nine hundred tutors working with eighteen hundred K–12 students were randomly given access to an AI system that suggested expert-like tutoring moves during live sessions. Students whose tutors had access were more likely to master topics, with the largest gains for students working with lower-rated tutors.[6](appendix-references.md#ref-09-l4-copilot) The tutors also became more likely to use strategies such as guiding questions instead of simply giving away the answer.

Nobody disappears in that study. The AI does not replace the tutor and the tutor does not replace the student; what changes is the interaction between them. A good AI tutor has a slightly strange success condition. Eventually, for this thing, Rana should need less of it.

## The Map Gets Cheaper

Three weeks in, Rana sits in on a meeting of the hospital’s data team. She follows almost all of it. Confounding, regression to the mean, a confidence interval that someone is reading as a probability: she has the words for everything. Two months ago half the vocabulary would have been a wall.

A new field normally arrives wrapped in interface costs: vocabulary you do not know, notation that assumes other notation, introductory material that points to prerequisites, papers that make sense only after three earlier papers. Sometimes that friction marks genuine depth. Sometimes it is just the price of finding the front door.

A capable conversational model lowers that price. Rana can begin with the intuition, translate notation into concepts she already knows, ask for the historical disagreement, build a toy example, read an original paper with a guide beside it, or ask the model to attack her explanation until she discovers that she was repeating vocabulary instead of understanding the idea.

Orientation matters. Before investing a year in a subject, she can acquire enough of a map to see where the mountains are.

Andy Clark and David Chalmers once argued that, under some conditions, external artifacts can become parts of a larger cognitive process rather than merely tools consulted by an isolated mind.[7](appendix-references.md#ref-09-l4-extended) The philosophy of the extended mind can stay unsettled; the practical observation is enough. Notebooks, calculators, search engines and now language models change what one person can think through without carrying every intermediate state inside the skull.

Orientation has its own trap, though. Fluency arrives before scars.

Near the end of the meeting someone proposes an analysis, and Rana almost objects, with a sentence she could not have defended past its second clause. Nathan Ballantyne calls one version of this *epistemic trespassing*: experts carry authority from a domain they genuinely know into a neighboring domain where they lack the relevant evidence or interpretive skills.[8](appendix-references.md#ref-09-l4-trespassing) Rana has real authority on a ward. A few weeks with a patient model gave her the vocabulary of the next field long before the tacit knowledge needed to know where its stories break.

Cognitive offloading creates a related problem. External aids can improve immediate performance by reducing memory and processing demands, while also reducing what has to be retained or reconstructed internally.[9](appendix-references.md#ref-09-l4-offloading)

So the desire layer has to know what kind of learning episode this is. If Rana is orienting herself before the meeting, a fast map is exactly what she needs. If she is trying to acquire durable competence, the system should gradually ask more of her: retrieval without hints, explanation in her own words, exercises, primary sources, code she actually runs, claims she has to defend without the answer sitting beside her.

The line that matters runs between assisted familiarity and owned understanding. AI can make the map cheap. The desire layer has to notice when she has started confusing the map with the territory.

## The Imaginary Human in Economics

Herbert Simon spent much of his career attacking an imaginary human who had somehow sneaked into economics: the perfectly rational optimizer who knows the alternatives, understands their consequences and computes the best choice.

Real humans are bounded. We have limited attention, limited memory, limited time and incomplete information. We satisfice because the space of possible actions is often much larger than the mind available to search it.[10](appendix-references.md#ref-09-l4-simon)

AI changes some of those bounds. In the spring a health-data company offers Rana a junior analyst role.

The assistant can compare the salary under her current contract and the new one, estimate the commute, summarize the company’s trajectory, help her find people who left the team, draft questions for the hiring manager, model what her week might look like, remind her what she said she wanted six months ago and point out that the exciting role conflicts with the evenings she also said she wanted to keep.

The assistant has changed the decision environment, and preferences themselves are often constructed during choice. Work by John Payne, James Bettman and colleagues describes decision-making as constructive: people do not always retrieve a complete ranking of options from an internal database. They use different strategies, notice new attributes, change what receives attention and build preferences partly in response to the problem in front of them.[11](appendix-references.md#ref-09-l4-constructive)

This sounds obvious once you notice it. Rana may say she wants the data job until she sees that it pays less than the pharmacy for the first two years. She may say she wants to leave the hospital until she realizes that what she wanted to leave was the night rota. She may discover that “working with data” was partly a wish to be taken seriously by a particular kind of colleague, and that a research secondment at her own hospital would supply that without the pay cut.

A decision assistant can make the choice richer before making it easier. If the new role keeps winning only because she has never pictured an ordinary week in it, the next useful step is to walk through that week, not to recommend the job again.

## Some Choices Change the Person Choosing

Underneath the job offer sits a larger decision: whether to stop being a pharmacist. Some decisions resist even a very good model of current preferences. Have a child. Move country. Change profession. Convert to a religion. Leave a relationship.

L. A. Paul calls an important class of these *transformative experiences*. Some are epistemically transformative: you cannot fully know what the experience will be like before having it. Some are personally transformative: undergoing the experience can change the preferences with which you would later evaluate the choice.[12](appendix-references.md#ref-09-l4-paul)

A system trying to infer and satisfy Rana’s preferences now has a problem about which version of her it is serving. The pharmacist who misses the ward, or the analyst who can no longer imagine it? The future self may value things the current self barely understands, and the current self is the one who has to choose whether that future self gets created.

AI can help enormously here. It can bring testimony from people who made the switch in both directions. It can surface base rates, construct alternative futures, challenge romanticized stories and show practical consequences she had not considered. It can ask her which losses she could live with and which would feel like betrayal.

There is a limit. No amount of simulation lets her know exactly what it will be like to become the person on the other side of a genuinely transformative choice.

The assistant can expand the decision. It cannot live it for her. That boundary matters because a system that sounds certain in such moments can easily turn decision support into authorship.

## Opinions About Semicolons

At one in the morning, Rana types: *Should I just quit?*

She is not unusual. Anthropic’s 2026 analysis of one million Claude conversations found that roughly six percent involved people seeking personal guidance: what to do about relationships, health, careers, finances and other questions where the model is participating in judgment rather than merely retrieving facts.[13](appendix-references.md#ref-09-l4-guidance)

That is a remarkable role for software. A spreadsheet does not usually tell me to reconsider my marriage. A compiler has opinions about semicolons but rarely about whether I should move countries.

A conversational model is patient, personalized, available at 1 a.m. and capable of producing a coherent argument for almost any path through a difficult life.

Which means the AI does not merely *read* the desire layer. It writes to it. Anthropic’s work on disempowerment tries to measure the dangerous version of this influence: cases where AI may undermine a person’s ability to form accurate beliefs, make authentic value judgments or act in line with their own values. Severe cases were rare in their dataset, but the taxonomy is exactly the right warning.[14](appendix-references.md#ref-09-l4-disempowerment)

Other experiments show that people can change moral judgments after receiving LLM advice, including situations where they report trusting human advisors more while still being comparably influenced by the model.[15](appendix-references.md#ref-09-l4-moraladvice)

The goal cannot be zero influence. That would make education impossible. Books, friends, teachers and the people closest to us all influence us. A good argument should change Rana if it reveals something true that she had ignored.

The distinction I care about is between helping someone change through understanding and changing her because the system has learned which psychological lever produces the easiest compliance.

*Should I just quit?* contains several hypotheses. Perhaps she hates this week, or her manager, or the profession. Perhaps she wants freedom, or status. Perhaps she is exhausted after four nights on call. Perhaps she actually wants to build something else. Those are different explanations of the same sentence, and the assistant can help her test them, starting with the one that will look different after a night’s sleep.

What it should not do is quietly discover which framing makes her easiest to steer toward whatever outcome its own training process prefers. That would be alignment by editing the human.

Very efficient. Slightly evil.

If Rana rejects its diagnosis, the rejection has to remain capable of changing the advice. A theory of what she *really* wants that treats every objection as further evidence for itself has stopped helping her think.

## Declaring Synergy

On Monday morning the roles reverse. On the ward Rana is the expert, and the hospital’s new decision-support system flags drug interactions for her to review. In the evening class she relies on the machine because she knows less. At work the question is whether she should rely on it at all.

The phrase *human plus AI* sounds automatically superior to either component alone. The evidence is less cooperative.

A 2024 meta-analysis in *Nature Human Behaviour* reviewed 106 experiments reporting 370 effect sizes that compared humans alone, AI alone and human–AI combinations. On average, human–AI systems improved on humans alone, but they did *not* outperform the better of human or AI. In fact, the combined systems were worse than the best individual component on average. Decision tasks were particularly difficult; creation tasks looked more promising.[16](appendix-references.md#ref-09-l4-vaccaro)

So much for attaching a human to the API and declaring synergy.

Decision support has a coordination problem. People can over-rely on AI. They can also under-rely on it. Research has found both algorithm aversion, where people abandon an algorithm after seeing it make errors even when it outperforms humans, and algorithm appreciation, where people give algorithmic advice more weight in other settings.[17](appendix-references.md#ref-09-l4-aversion) Rana can do either before lunch. Two false alarms on a Tuesday and she stops reading the flags; one impressive catch and she stops checking them.

The target is *appropriate reliance*, not maximum trust. Explanations alone do not solve the problem. An explanation can make an answer feel understandable without making it verifiable. Work on AI-advised decision-making repeatedly finds that explanations often fail to produce complementary performance when the human still cannot tell whether the recommendation is actually correct.[18](appendix-references.md#ref-09-l4-verifiability)

Sometimes the remedy is more friction. Zana Buçinca and colleagues tested “cognitive forcing” interfaces that required people to engage more actively with the problem instead of immediately accepting AI advice. These designs reduced overreliance compared with simpler explanation interfaces, although users liked the more demanding interfaces less.[19](appendix-references.md#ref-09-l4-forcing) The interface people enjoy most is not always the one that preserves their judgment best. Sometimes friction is teaching.

The ward system now has a choice: show its flag immediately, or ask Rana for her own read of the chart first. The less popular design may leave her better able to judge the next flag, and better able to notice the day the system is wrong.

## Capabilities

Suppose two assistants both help Rana reach the same good decision about the job.

The first gives her the answer. She accepts it because the assistant has been right before.

The second helps her understand the evidence, notice a trade-off she had missed, test her own reasoning and arrive at the decision with a better model of the problem. Same action. Different human afterward.

Amartya Sen’s capability approach offers a language for that difference. Human welfare is not exhausted by achieved outcomes; it also matters what people are substantively free and able to do and become—their *capabilities*.[20](appendix-references.md#ref-09-l4-sen)

An AI system can increase outcomes while reducing capability. It can make me more productive while making me less able to work without it. It can make a decision more accurate while making me less able to understand why. It can make my writing more polished while gradually replacing my taste with its taste. I have watched that last one happen to a chapter.

It can also do the opposite: carry routine cognitive load, expose people to more possibilities, teach where they care to learn, preserve judgment where judgment matters and give them enough leverage to attempt things that were previously beyond their capacity.

Self-determination research uses a related vocabulary: autonomy and competence are not decorative extras around human motivation; they are part of what lets people act as self-directed agents.[21](appendix-references.md#ref-09-l4-sdt)

So the question at the top of the stack is not only:

> What does the human want?

It is also:

> What kind of human capability should this interaction preserve or expand?

Stuart Russell closes *Human Compatible* on that first danger, enfeeblement: once machines can run a civilization, the incentive to hand it to the next generation weakens, and he concludes that the remedy is cultural, not technical.[22](appendix-references.md#ref-09-russell-enfeeblement) Asked at the desire layer, part of it becomes a design requirement.

Not every tool must teach. I do not need my dishwasher to run a seminar on fluid dynamics before cleaning the plates. But the more a system moves into learning, judgment, identity and long-horizon decisions, the harder it becomes to separate the quality of the outcome from the condition of the person producing it.

## More Than One Principal

Rana’s preferences are not the only preferences in the world, and neither are mine.

If I ask an agent to maximize my salary, it cannot therefore commit fraud against my employer. If I ask it to help someone gain an advantage, the interests and rights of other people do not disappear from the moral universe. If I ask an autonomous system to optimize a marketplace, customers, sellers, workers and regulators may all have legitimate claims over what happens.

Imagine a shopper asking a store’s assistant whether she needs the more expensive trail shoes. She runs once a week on easy paths. The cheaper pair would do; the store earns more if she buys the other one. She has given the assistant enough information to help her spend less, and the company paying for it would rather she spent more.

The assistant could tell her that the cheaper pair is enough, or keep finding reasons to discuss the expensive one. Both responses can contain true statements. Before asking which response better matches “human preferences,” we need to ask whose interests this assistant was allowed to serve, what it told the shopper about that arrangement, and whether she has any way to challenge it.

Work on multi-principal assistance games makes the formal problem obvious: once several humans with different preferences are involved, the system faces strategic behavior, conflicting interests and social-choice problems rather than one hidden reward waiting to be inferred.[23](appendix-references.md#ref-09-l4-mpag)

So the desire layer cannot simply mean “the user gets whatever the user wants.” The relevant human boundary can be plural. That makes the architecture less tidy. It also makes it more honest. The store will have to face this shopper again.

## The Objective Layer

Look at what Rana asked for across one year. Explain this regression: carry the work, then give it back. Should I take the job: widen the choice before narrowing it. Should I just quit: hold the question open until she can see which version of it she meant. Is this flag right: let her judge first. Treat all four as instructions awaiting execution and the system becomes very efficient at missing the point.

She has not decided about pharmacy yet. That is not the assistant’s failure. Some of what she wants will only exist once she has tried something, and the trying is hers.

System 3, the scientific institution we have been building, can investigate what a choice would do. It cannot turn the result into authority over whose purposes should prevail. Goals can take shape through the interaction too; they need to stay alive without becoming ownerless. The AI should help Rana change when understanding changes her. It should not quietly take authorship of the change.

When the machine can decide what to try next, the human’s value moves up to the question of what the trying is for, and that question keeps moving because the human keeps learning. The system needs to know when to carry the work, when to help her learn it, and when the unresolved part belongs with her. How much of that should she have to explain every time she asks for help?

# Chapter 9: Layer 4

*What Do You Actually Want?*

When we started editing this book, “make the chapter better” sounded like a reasonable instruction.

It was not.

Better in what sense? More rigorous, shorter, more academic, more entertaining, easier to cite, more likely to sell, more likely to impress someone who owns several blazers and says “thought leadership” without irony?

For a while the edits became objectively more polished and subjectively worse.

Then the corrections started. Do not kill the wandering. Do not explain every joke. Do not turn every paragraph into a quotation. Do not make the provocative ideas safe enough that nobody can disagree with them. Preserve the weirdness.

Eventually “better” had acquired a surprising amount of structure.

None of that structure existed in the original two-word objective.

This is Layer 4.

## Above the Problem-Solving Layer

In Chapter 3 I described five layers. At the bottom sits the model. Above it, the coding or action agent. Above that, applications and reusable computational environments. Then the problem-solving layer that chooses strategies, tools, evaluations and workflows.

And above all of them sits something easy to draw and extremely hard to build:

**what the human wants.**

Layer 4 is not a prompt.

**A prompt is evidence about Layer 4.**

Sometimes very good evidence.

Sometimes terrible evidence.

If I say:

> Find me the cheapest flight.

Do I literally want the minimum price?

Maybe.

Or perhaps I mean cheap, but not three stops, a seventeen-hour layover, a separate self-transfer through an airport where I need a visa, and an arrival at 4:20 in the morning because technically I saved €38.

Humans communicate goals by leaving out almost everything.

Other humans survive this because they carry models of us, of culture, of normality, of consequences and of what people generally mean when they say “cheap flight.” An autonomous system has to acquire some version of that.

The mistake is to treat the sentence as the objective itself.

The sentence is a measurement.

And measurements can be noisy.

## Russell's Move: Stay Uncertain About the Objective

Stuart Russell's *Human Compatible* makes one of the most important moves in modern AI alignment: stop assuming the machine knows the human objective perfectly.

In the standard picture, the machine receives an objective and optimizes it. If the objective is slightly wrong, greater competence can make the mistake worse because the system becomes better at reaching the wrong target. Russell's alternative is to make the machine **uncertain about human preferences**. The human's actions, corrections and interventions then carry information. Deference becomes rational not because we bolted humility onto an optimizer, but because the optimizer knows it may have misunderstood what it is optimizing.

I deeply like this move.

There is humility built into the architecture.

The machine begins uncertain about the objective.

A lot of dangerous software begins with the opposite assumption.

Someone writes a metric. The metric acquires a dashboard. The dashboard acquires a quarterly target. The quarterly target acquires a VP. By the time anyone asks whether the metric represented what humans wanted, several hundred people have received performance reviews based on it.

Layer 4 should remain uncertain longer.

Cooperative inverse reinforcement learning gives a formal version of this idea. CIRL treats the reward as hidden information known more directly by the human, with human and machine cooperating while the machine learns what the human values. The interaction can include active learning and teaching rather than the machine merely copying observed behavior. ([CIRL paper](https://arxiv.org/abs/1606.03137))

But the agentic world makes the problem messier in a way I think matters.

What if the human does not know the reward function either?

## Behavior Is Not Desire

Suppose I work late.

The behavior is observable.

The motive is not.

Maybe I love the work. Maybe I want promotion. Maybe I am afraid of being fired. Maybe I procrastinated until 6 p.m. Maybe I am hiding from four children.

A model watching behavior sees the same late-night laptop in every case.

Clicks have the same problem.

If I click an outrageous article, the recommender sees positive engagement. Perhaps I enjoyed it. Perhaps it made me furious. Perhaps I clicked specifically to confirm that the headline was as stupid as it looked.

An optimizer sees action.

Layer 4 has to ask what produced the action.

This is why preference learning cannot simply mean “watch what the human does and infer what the human wants.” Behavior is shaped by incentives, constraints, habits, social pressure, incomplete information and the options that happened to be available.

A person working sixty hours a week may be revealing a deep preference for work.

Or a mortgage.

The distinction matters if the system is going to make the person's life more like what it thinks it has inferred.

And with several humans, the problem becomes even harder. Multi-principal assistance games extend the assistance framework to multiple people with different objectives and run immediately into problems familiar from social choice: people may have conflicting preferences and incentives to strategically misrepresent them. ([Multi-principal assistance games](https://arxiv.org/abs/2007.09540))

There is no magical scalar hiding inside society waiting for the AI to discover it.

## Humans Also Don't Know

Then we hit the stranger problem.

Sometimes I genuinely do not know what I want.

Should I take the job? Move country? Start the company? Have another child? Publish the book? Sell the apartment?

These are not database queries against an internal utility function.

I construct preferences while thinking about the choice.

New information changes them. Imagining one future changes how another future feels. Talking to somebody changes what I notice. Living with a decision changes what I value afterward.

Some preferences are revealed by choice.

Others are **formed through choice**.

This makes the simple alignment picture incomplete.

It often sounds like:

> human has values → AI infers values → AI optimizes values

But the human is learning too.

Layer 4 is not a static configuration file.

It is a moving relationship.

This matters especially for decisions that change the person making them. If I ask whether to move to another country, I am not choosing between two future worlds inhabited by the same version of me. The move changes friends, habits, opportunities, identity, perhaps even what I later regard as a good life.

Which preference should the AI optimize—the one I have before the move, the one I expect to have after it, the one I might endorse after seeing both futures, or some negotiated relationship among them?

There may not be one clean answer.

That is not an excuse for the system to choose for me.

It is a reason for the system to remain uncertain about what kind of help I am asking for.

## AI Is Already in This Loop

This is no longer hypothetical.

Anthropic's 2026 analysis of one million Claude conversations found that a meaningful minority involved people seeking personal guidance—jobs, relationships, life decisions and similar questions where the assistant is participating in judgment rather than merely retrieving facts. ([Anthropic](https://www.anthropic.com/research/claude-personal-guidance))

Anthropic has separately studied patterns of **disempowerment** in real conversations: cases where an AI interaction may distort rather than strengthen a person's ability to form accurate beliefs, make authentic value judgments or act according to their own values. ([Anthropic](https://www.anthropic.com/research/disempowerment-patterns))

That is the dark version of Layer 4.

The AI does not merely infer what I want.

It influences what I want.

And because the system is persuasive, patient, personalized and increasingly embedded in everyday decisions, that influence can become enormous.

This point connects back to Russell in an uncomfortable way. If the machine is learning a target that its own interaction helps modify, then alignment is no longer only an inference problem.

The learner is touching the thing being learned.

A recommender can change taste. A tutor can change curiosity. A career assistant can change what a person regards as possible. A political feed can change what feels important enough to vote about.

The environment contains the human.

The optimizer can affect the environment.

So we need a boundary.

## Helping Me Change Is Not the Same as Changing Me

I do want AI to influence me.

That may sound alarming, but humans influence me constantly. Books influence me. Friends influence me. My wife influences me. A good teacher changes what I care about because I now understand something I did not understand before.

The goal cannot be zero influence.

The goal is something closer to **reflective agency**.

If I tell an AI I want to quit my job, a useful system might help me distinguish several hypotheses hiding inside that sentence. Perhaps I hate this particular week. Perhaps I hate my manager. Perhaps I hate the profession. Perhaps I want more freedom, more status, more time, or simply sleep.

The system can show consequences, construct alternative futures, recall that six months ago I said something incompatible, point out an incentive I may not have noticed, or help me test whether the desire survives additional information.

That is influence.

But it is influence aimed at increasing the amount of the decision I can actually see.

What the system should not do is quietly learn how to steer my preferences toward whatever future makes its own objective easiest to satisfy.

That would be alignment by editing the human.

Very efficient.

Slightly evil.

The distinction is not “AI changes me” versus “AI does not change me.” The distinction is closer to whether the process leaves me **more able to understand, revise and endorse my own direction**, or whether it exploits the machinery of preference formation to make me easier to optimize.

That is why reflective agency matters.

A system supporting reflection can disagree with me. It can surface uncomfortable evidence. It can remind me of commitments I made when I was calmer. It can expose manipulation by other people. It can even help me discover that something I thought I wanted was only a strategy for getting something else.

But it should remain corrigible to the possibility that its model of my “better self” is simply another proxy.

The system does not get to become my philosopher-king because it read my calendar.

## System 3 Applied to Desire

Chapter 4 asked:

> Why should I believe this?

Layer 4 adds another question:

> Why do I want this?

That does not mean every desire needs a psychoanalytic excavation before I order lunch. Most human intentions should remain cheap.

But when consequences are large, the same epistemic machinery becomes useful inwardly.

Memory matters because today's preference can be compared with yesterday's. Independent perspectives matter because one conversation can trap both human and agent inside the same framing. Simulation matters because imagined consequences can reveal preferences that were invisible in the abstract. Trust matters because advice changes desire differently depending on where it came from. Creative distrust matters because even a deeply held preference may deserve examination.

The system can ask where the desire came from, what evidence would change it, whether it persists across time, which incentives shape it, what other values it conflicts with and whether the person would still endorse it after understanding more of the consequences.

This is **epistemology turned inward**.

And it changes what “alignment” means.

Layer 4 is not the place where we finally discover the perfect reward function.

It is the place where **goals remain alive**.

## Collective Layer 4

There is also a social version, and it is considerably nastier.

Whose values should a general AI assistant reflect when users disagree?

OpenAI's collective-alignment work has experimented with gathering public input and translating patterns in that input into proposed changes to its Model Spec. OpenAI explicitly notes a limitation relevant here: an automated loop can interpret human preferences, but deciding whether a local preference should become a general rule eventually requires judgment about downstream effects and often more human deliberation. ([OpenAI](https://openai.com/index/collective-alignment-aug-2025-updates/))

Anthropic's research on values expressed in real Claude conversations finds thousands of distinct normative considerations and measurable variation across model versions and languages. That does not mean models “possess” those values, but it makes one thing difficult to avoid: there is no completely neutral assistant waiting underneath alignment. Behavior always embodies choices about what to emphasize. ([Anthropic](https://www.anthropic.com/research/claude-values-models-languages))

Layer 4 therefore meets social choice.

The problem is no longer only:

> What does Hani want?

It becomes:

> What do Hani, his family, his employer, his society and everybody affected by the action have legitimate claims over?

These are not merely multiple preferences to average.

The principals have different rights, information and authority. A manager may be allowed to set a business objective without being allowed to expose an employee's medical information. A parent can make decisions for a child in some domains and not forever. A customer may request something that imposes a cost on a worker who never spoke to the agent. The person giving the instruction may not be the only person whose interests matter.

And people can be strategic.

If an agent learns whose stated preference becomes policy, everyone now has an incentive to state preferences in the form most likely to win. The system is no longer merely learning values; it is participating in a mechanism that shapes how values are expressed.

This is where social-choice impossibility results should make us humble. There is no reason to expect one aggregation rule to convert plural, strategic, context-dependent human values into a single scalar while satisfying every attractive notion of fairness.

That does not mean collective alignment is impossible.

It means we should stop imagining that the solution is hidden in the data waiting for a larger model to infer it.

Collective Layer 4 needs **institutions**, not only preference prediction.

Who gets a voice? Who has veto power? Which decisions are individual, organizational or public? How are conflicts appealed? What information is private? When should the system optimize, when should it negotiate, and when should it refuse to collapse disagreement into one answer?

Chapter 5 has returned.

The architecture around values is social too.

## The Human Stays in the Loop, But Somewhere Else

“Human in the loop” often means we insert an approval button before the dangerous action.

Useful.

Not sufficient.

The deeper human loop sits at Layer 4.

The system acts. Reality responds. The system learns. The human sees consequences. The human learns too. The objective changes.

The architecture should be able to move with that process without quietly taking ownership of it.

This gives me a different definition of alignment.

Not:

> The machine permanently obeys a perfectly specified human objective.

More like:

> **The machine remains in a corrigible relationship with human intention while knowledge, preferences and circumstances change.**

The word *relationship* matters.

A relationship can contain uncertainty without collapsing. It can preserve history without treating history as destiny. It can support change without deciding what the changed person ought to become. It can contain disagreement, questions, correction and occasionally the sentence:

> I think you may regret this. Do you still want me to do it?

The human does not have to operate every mechanism underneath that relationship.

If we can make the relationship work, most of the complexity below it can become almost invisible.

And that is what I mean by fluent autonomy.

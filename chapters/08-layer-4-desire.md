# Chapter 8: Layer 4

*What Do You Actually Want?*

> **WIP:** First integrated draft. Structure and examples are provisional and will receive the same editorial/voice pass as Chapters 1–4.

When we started editing this book, "make the chapter better" sounded like a reasonable instruction.

It was not.

Better in what sense?

More rigorous?

Shorter?

More academic?

More entertaining?

Easier to cite?

More likely to sell?

More likely to impress someone who owns several blazers and says "thought leadership" without irony?

For a while the edits became objectively more polished and subjectively worse.

Then the corrections started.

Don't kill the wandering.

Don't explain every joke.

Don't turn every paragraph into a quotation.

Don't make the provocative ideas safe enough that nobody can disagree with them.

Preserve the weirdness.

Eventually "better" had acquired a surprising amount of structure.

None of that structure existed in the original two-word objective.

This is Layer 4.

## Above the Problem-Solving Layer

In Chapter 3 I described five layers.

At the bottom sits the model.

Above it, the coding or action agent.

Above that, applications and reusable computational environments.

Then the problem-solving layer that chooses strategies, tools, evaluations and workflows.

And above all of them sits something easy to draw and extremely hard to build:

**what the human wants.**

Layer 4 is not a prompt.

A prompt is evidence about Layer 4.

Sometimes very good evidence.

Sometimes terrible evidence.

If I say:

> Find me the cheapest flight.

Do I literally want the minimum price?

Maybe.

Or perhaps I mean: cheap, but I do not want three stops, a seventeen-hour layover, a separate self-transfer through an airport where I need a visa, and an arrival at 4:20 in the morning because technically I saved €38.

Humans communicate goals by leaving out almost everything.

Other humans survive this because they carry models of us, of culture, of normality, of consequences and of what people generally mean when they say "cheap flight."

An autonomous system has to acquire some version of that.

## Wanting Is an Inference Problem

There is a long-standing formal version of this idea in cooperative inverse reinforcement learning.

Instead of assuming the robot knows the human reward function, CIRL treats the reward as hidden information known more directly by the human. Human and machine cooperate while the machine learns what the human values; importantly, the interaction can include active learning and teaching rather than the machine merely copying observed behavior. ([CIRL paper](https://arxiv.org/abs/1606.03137))

I like the humility in that setup.

The machine begins uncertain about the objective.

A lot of dangerous software begins with the opposite assumption.

Someone writes a metric.

The metric acquires a dashboard.

The dashboard acquires a quarterly target.

The quarterly target acquires a VP.

By the time anyone asks whether the metric represented what humans wanted, several hundred people have received performance reviews based on it.

Layer 4 should remain uncertain longer.

## Motives and Incentives

The problem is harder because behavior is not a clean window into desire.

I work late.

Do I love the work?

Do I want promotion?

Am I afraid of being fired?

Did I procrastinate until 6 p.m.?

Am I hiding from four children?

The observable behavior is the same.

The motive is not.

Clicks have the same problem.

If I click an outrageous article, the recommender sees positive engagement. Perhaps I enjoyed it. Perhaps it made me furious. Perhaps I clicked it specifically to confirm that the headline was as stupid as it looked.

An optimizer sees action.

Layer 4 has to ask what produced the action.

This becomes even more complicated with multiple humans. Work on multi-principal assistance games extends the assistance framework to several people with different objectives and immediately runs into problems familiar from social choice: people may have conflicting preferences and incentives to strategically misrepresent them. ([Multi-principal assistance games](https://arxiv.org/abs/2007.09540))

There is no magical scalar hiding inside society waiting for the AI to discover it.

## Humans Also Don't Know

Then we hit the stranger problem.

Sometimes I genuinely do not know what I want.

Should I take the job?

Move country?

Start the company?

Have another child?

Publish the book?

Sell the apartment?

These are not database queries against an internal utility function.

I construct preferences while thinking about the choice.

New information changes them.

Imagining one future changes how another future feels.

Talking to somebody changes what I notice.

Living with a decision changes what I value afterward.

This means the standard alignment picture is incomplete.

It often sounds like:

human has values → AI infers values → AI optimizes values.

But the human is learning too.

Layer 4 is not a static configuration file.

It is a moving relationship.

## AI Is Already in This Loop

This is no longer hypothetical.

Anthropic's 2026 analysis of one million Claude conversations found that a meaningful minority involved people seeking personal guidance—jobs, relationships, life decisions and similar questions where the assistant is participating in judgment rather than merely retrieving facts. ([Anthropic](https://www.anthropic.com/research/claude-personal-guidance))

Anthropic has separately studied patterns of **disempowerment** in real conversations: cases where an AI interaction may distort rather than strengthen a person's ability to form accurate beliefs, make authentic value judgments or act according to their own values. ([Anthropic](https://www.anthropic.com/research/disempowerment-patterns))

That is the dark version of Layer 4.

The AI does not merely infer what I want.

It influences what I want.

And because the system is persuasive, patient, personalized and increasingly embedded in everyday decisions, that influence can become enormous.

So we need a boundary.

## Helping Me Change Is Not the Same as Changing Me

I do want AI to influence me.

That may sound alarming, but humans influence me constantly.

Books influence me.

Friends influence me.

My wife influences me.

A good teacher changes what I care about because I now understand something I did not understand before.

The goal cannot be zero influence.

The goal is something closer to **reflective agency**.

If I tell an AI I want to quit my job, a useful system might help me distinguish:

I hate this particular week.

I hate my manager.

I hate the profession.

I want more freedom.

I want status.

I am exhausted.

I actually want to build something else.

Those are different hypotheses about the same sentence.

The system can show consequences.

Construct alternative futures.

Recall that six months ago I said something incompatible.

Point out an incentive I may not have noticed.

Help me test whether the desire survives additional information.

What it should not do is quietly learn how to steer my preferences toward whatever future makes the system's objective easiest to satisfy.

That would be alignment by editing the human.

Very efficient.

Slightly evil.

## System 3 Applied to Desire

Chapter 4 asked:

> Why should I believe this?

Layer 4 adds another question:

> Why do I want this?

Chapter 5 makes the boundary sharper. If System 3 is science made architectural, then it gives us extraordinary machinery for asking what is true, what follows from what, which intervention changes the world, and where our beliefs fail.

It does not, by itself, tell us what the world **ought** to become.

Add another experiment, another critic, another verifier, another thousand agents: **Hume does not disappear because the orchestrator has more GPUs.** The moment the question changes from *what is true?* to *what should become true?*, epistemology runs into desire.

Where did the desire come from?

What evidence would change it?

Does it persist across time?

Is it intrinsic, or is it a strategy for something else?

Which incentives are shaping it?

Does it conflict with something else I claim to value?

Would I still endorse it if I understood the consequences?

This is epistemology turned inward.

And the same machinery becomes useful.

Memory matters because today's preference can be compared with yesterday's.

Independent perspectives matter because one conversation can trap both human and agent in the same framing.

Simulation matters because imagined consequences can reveal hidden preferences.

Trust matters because advice changes desire differently depending on where it came from.

Creative distrust matters because even a deeply held preference may deserve examination.

Layer 4 is therefore not the place where we finally discover the perfect reward function.

It is the place where **goals remain alive**.

## Collective Layer 4

There is also a social version.

Whose values should a general AI assistant reflect when users disagree?

OpenAI's collective-alignment work has experimented with gathering public input and translating patterns in that input into proposed changes to its Model Spec. OpenAI explicitly notes a limitation relevant here: an automated loop can interpret human preferences, but deciding whether a local preference should become a general rule eventually requires judgment about downstream effects and often more human deliberation. ([OpenAI](https://openai.com/index/collective-alignment-aug-2025-updates/))

Anthropic's research on values expressed in real Claude conversations finds thousands of distinct normative considerations and measurable variation across model versions and languages. That does not mean the models "possess" those values, but it does make one thing clear: there is no completely neutral assistant waiting underneath alignment. Behavior always embodies choices about what to emphasize. ([Anthropic](https://www.anthropic.com/research/claude-values-models-languages))

Layer 4 therefore meets social choice again.

The problem is no longer only:

> What does Hani want?

It becomes:

> What do Hani, his family, his employer, his society and everybody affected by the action have legitimate claims over?

There is no reason to expect that question to have one clean mathematical answer.

Which is inconvenient.

But at least it is the real problem.

## The Human Stays in the Loop, But Somewhere Else

"Human in the loop" often means we insert an approval button before the dangerous action.

Useful.

Not sufficient.

The deeper human loop sits at Layer 4.

The system acts.

Reality responds.

The system learns.

The human sees consequences.

The human learns too.

The objective changes.

The architecture should be able to move with that process without quietly taking ownership of it.

This gives me a different definition of alignment.

Not:

> The machine permanently obeys a perfectly specified human objective.

More like:

> The machine remains in a corrigible relationship with human intention while both knowledge and circumstances change.

The word *relationship* matters.

Because if we can make that relationship work, the complexity underneath can become almost invisible.

And that is what I mean by fluent autonomy.

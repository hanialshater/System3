# Chapter 6: Pattern Language
*When Knowledge Becomes Software*

## The Workshop

Let me tell you a story about a tech leader. Call him Uncle Jalal, as the team eventually did, partly out of affection and partly because he had a story for every occasion.

Uncle Jalal joined an online grocery company carrying years of experience from elsewhere. In his first month the team held a roadmap workshop, and by lunch the whiteboard was full. Every idea arrived with a pedigree: a paper from a good conference, a keynote, a system that had worked beautifully somewhere else. Several of the somewhere elses were his.

The room ranked the ideas by how convincing they sounded, which is how most rooms rank ideas. His sounded convincing because he had seen them work. A peacock's tail persuades the same way: the display is too expensive to fake, so it impresses, whatever it reveals about the bird.[1](appendix-references.md#ref-06-peacock)

Twice that afternoon Sam said, quietly, that the team had tried something like this before. He had no paper. He had a memory of a launch two years earlier and a feeling about how customers on the home screen behaved. The team wrote his comments on a smaller sticky note.

Within a year most of that whiteboard would quietly fail, and the one person who could have said why was sitting by the door.

What Uncle Jalal had carried into the room were solutions that had shed the conditions under which they worked. An architect had worried about exactly that, for rooms.

## Light on Two Sides

Pattern 159 is called Light on Two Sides of Every Room. It says that when people have a choice, they drift toward rooms with windows on two walls and leave the one-window rooms empty. Light from a single side glares. It flattens the faces across the table, so you cannot read them. Think of the rooms you have loved and count their windows.

Pattern 88 is Street Café: a place to sit lazily, legitimately, on view, and watch the street go by. Pattern 167 says a balcony less than six feet deep will hardly ever be used, because nobody can pull a chair up to a table on it. You have seen those balconies. They hold a bicycle and a dead plant. Pattern 252, Pools of Light, says that even lighting kills a room, because people gather where the light pools. The last one, 253, is Things from Your Life: put on your walls what matters to you and ignore what a decorator says belongs there.

There are 253 of them. The first is about how the world should be divided into regions. The last is about the photographs above your desk. In between come neighborhoods and bus stops, beer halls, stairs you can sit on, a bench by the front door. Christopher Alexander and five colleagues at Berkeley published the book in 1977. It runs past eleven hundred pages on Bible paper, and it has probably been read by more programmers than architects.

Reading it is a strange experience. Somewhere in the middle of it I caught myself asking: why am I suddenly emotionally invested in the width of a balcony? You keep recognizing things you have always known and never said. Alexander believed that some places are alive and some are dead, that everybody can feel the difference, and that the difference has no adequate name. He called it the quality without a name. He had trained as a mathematician at Cambridge before taking the first doctorate in architecture Harvard ever awarded, and he went after the unnameable quality the way a mathematician would. He broke it into problems small enough to state, and he stated them so that they could be wrong.

Every pattern begins with a name you can say in a meeting, then a photograph. It places the problem inside the larger patterns it helps complete, then states it in bold as forces pulling against each other. Evidence and argument lead to the word Therefore, followed by the arrangement that resolves the forces, also in bold. Links to smaller patterns show how to complete it. You can follow them from a neighborhood to a house to a window seat. It was hypertext in 1977.

The part Uncle Jalal's workshop ideas had lost is the opening of each pattern, where Alexander says which larger arrangement it belongs to and which forces it answers. A six-foot balcony is right on a street-facing flat where people want to sit outside, and nobody is recommending one for a warehouse. The context is what lets a pattern say where it stops applying.

And every pattern carries a confidence mark. Two asterisks mean the authors believe they have stated a true invariant. One means they have made progress and expect a better answer. None means they offer one possible solution without claiming to have found what all successful solutions share. They say outright that the patterns are hypotheses: does the problem occur as described, and does the arrangement resolve it?[2](appendix-references.md#ref-06-alexander) You can test Light on Two Sides by walking through an office at four in the afternoon and seeing where people are.

A claim that says where it applies and how sure its author is has invited someone to check.

He meant it politically, too. The language was supposed to take design away from professionals and hand it back to the people who would live in the rooms. A family with the book could lay out its own house and argue with the architect in the architect's terms.

That is a pattern language: builders' knowledge, the kind Sam carries, written down as connected proposals whose context and reasons are open to question.


From here on I borrow Alexander's asterisks to mark my confidence that each proposed arrangement can resolve the problem described: two for a well-supported practice, one for a promising proposal that needs further testing, and no asterisk (an unmarked Therefore) where its adequacy remains an open question. The marks judge the arrangements. They do not claim that an agent institution has implemented them successfully.

## Wins That Vanish

So the team did what a good team does with imported ideas. It tested them.

An experimentation platform can behave like an organization's Bayesian engine. Thomas Bayes's rule, published after his death in 1763, says how a belief should change when evidence arrives: start from a prior, weigh the evidence under competing possibilities, and end with a revised belief.[3](appendix-references.md#ref-06-bayes) The individual A/B test need not itself be Bayesian; the larger habit is. The team starts with a guess about an idea, splits its customers, and lets the comparison move the guess. Over the years the archive can become the company's prior: a record of what worked here and what did not, earned on its own customers.

The engine said yes. The home-screen redesign, Uncle Jalal's favorite idea from the workshop, won by four percent. So did a recipe carousel and a personalized deals tile. Each test ran for two weeks, each came back green, and the team shipped them. A fortnight after launch the redesign's gain was gone. The feature was still live. The numbers simply sat where they had been before.

## The Quarterly Review

Uncle Jalal found out at the quarterly review. The slide said four percent, and he had made it. The head of the business asked a reasonable question: if the experiment showed four percent, why was the live number flat?

He had an answer ready. Seasonality, probably: the experiment had ended just before the school holidays, and grocery baskets change shape when children are at home. It was a good answer. It sounded like analysis, it cited a real calendar, and it was the kind of thing an experienced person says. He did not know whether it was true.

Harry Frankfurt distinguished the liar, who hides the truth, from the bullshitter, who does not care about it.[4](appendix-references.md#ref-06-frankfurt) What he had just given the room was harder to catch than either, because it passed every test of sincerity. I call it high-functioning bullshit: real expertise and real conviction, with no live connection to the assumptions it depends on. He believed every word. His workshop ideas had been the same kind of thing: they had worked for other customers, with other baskets and other delivery windows, and none of those conditions had made the journey with him. I have given that kind of answer myself, more than once.

Nobody in that room was against evidence. Science has few open enemies left in rooms like that one. The danger comes from inside the method, from work that has rigor's shape: a dashboard, a confidence interval, an experienced person explaining seasonality. It looks scientific and reasonable, and it fails on an assumption nobody checked.

Then the carousel's gain went the same way, and then the deals tile's.

Every fade received an explanation, and every explanation was reasonable. The redesign had run into the school holidays. The carousel launched the week a promotion ended. The deals tile coincided with a competitor's discount week. Each story cited a real event, came from someone who knew the business and fit the incident it was written for, and none of them predicted the next fade.

Imre Lakatos, who in Chapter 5 counseled patience with anomalies, also gave a test for when patience has run out.[5](appendix-references.md#ref-06-lakatos) A research program protects its core with auxiliary hypotheses, and the patches tell you whether the program is healthy. In a progressive program, a revision predicts something new that then holds up. In a degenerating one, each revision explains the failure already observed and predicts nothing further. The team's explanations were degenerating, and no record existed that would have shown it. They were sincere, informed, and checked against nothing. The holiday story was his.

The Bayesian engine was updating faithfully. Something it could not see was eating the results.

## Two in the Morning

The same team had another side, and it worked.

At ten past two one morning, checkout in one city stops accepting orders. The engineer on call, call her Ines, has been at the company for five weeks. The runbook on her second screen is admirably clear until the line where it stops being clear: if it started after Tuesday's migration, ask Sam. There is a thing with the old serializer.

It started after Tuesday's migration. Sam is on a beach in Portugal with his phone in a drawer, which is exactly where he deserves to be.

Ines has the logs, the dashboards and an agent that has read every document the company owns. None of them contains what Sam looks for in the old serializer, because Sam never wrote it down. Nobody asked him to. It was never going to be two in the morning while he was away.

By four the city was taking orders again, because Ines rolled back the migration, which restored service without explaining the failure.

Set the missing serializer note aside for a moment and look at what carried her for the first two hours. An alert woke her within minutes of the first failed order. A dashboard showed which city, which service and which deploy. The runbook walked her through the dependency graph and the traffic split. The rollback she used is rehearsed every month, and the previous week's load test, run against a simulated Saturday-morning rush, told her the other cities could absorb the shifted traffic. Five weeks into the job, she restored a city on her own.

Three months into his own job, Uncle Jalal had learned almost nothing from the experimentation archive that he could rely on.

The next home-screen launch was due in a month. Nobody on the product side could say whether to believe its result.

## Why Engineering Learns

Engineering knowledge is reliable for a dull reason: it is checked constantly. A test suite runs on every commit, and a regression fails within minutes of being written. Alerts fire when a service drifts outside its limits. Load tests ask, before customers do, at what traffic a working system stops working, which is Alexander's context with numbers in it. Netflix built Chaos Monkey, a program that switched off its own production servers at random during working hours, so that engineers would discover their hidden assumptions while they were awake to fix them.[6](appendix-references.md#ref-06-chaosmonkey)

Karl Popper argued that an empirical claim earns its standing by risking refutation and surviving.[7](appendix-references.md#ref-06-popper) A modern engineering organization is a Popperian machine that runs thousands of attempted refutations a day. Popper had no patience for the Bayesian picture, but here the two divide the work neatly. Bayes describes how an organization's beliefs should move when evidence arrives. Popper explains why engineering beliefs move quickly: the evidence arrives cheaply, often, and in a form that can say no.

Engineers have egos, credentials and favorite architectures like everyone else. An impressive design that breaks under load fails the load test on Thursday, whatever its author's reputation.

Patterns traveled well in that world. In 1987 Kent Beck and Ward Cunningham, both readers of Alexander, wrote five interface patterns for a group at Tektronix and let the future users do the design.[8](appendix-references.md#ref-06-beck) Seven years later Design Patterns gave programmers twenty-three named arrangements for object-oriented code.[9](appendix-references.md#ref-06-gof) A generation learned to say Observer, Factory and Singleton the way builders say lintel. In 1995 Cunningham built WikiWikiWeb so programmers could collect and edit patterns together.[10](appendix-references.md#ref-06-wiki) The wiki was invented to hold a pattern language; six years later an encyclopedia borrowed the idea.

Even here, the name traveled faster than the reasons. You could say Singleton in a meeting without bringing along any of the contexts and trade-offs the books still described. A pattern had been a hypothesis about when an arrangement resolves a conflict. In use, it could become a feather: something good engineers were seen to use. Codebases filled with factories that built one kind of object and singletons guarding nothing.

In 1996 the programmers invited Alexander to give the keynote at their largest conference. He came, a little bemused to find himself famous in a field he did not work in, and he was gracious, and he was not sure they had taken what mattered. He asked whether their patterns carried the two things his were for: making something better for the people who live in it, and generating a coherent whole from the parts. He suspected they had mostly adopted a format for trading ideas.[11](appendix-references.md#ref-06-alexander96) Engineering had a partial defense he did not mention. When a feathered pattern broke something, a test usually said so.

## Ask Sam

Engineering's checks have a blind spot, and Ines found it at two in the morning. The serializer fails rarely. A failure that comes once a year produces one piece of feedback a year, and knowledge fed that slowly stays in the head of whoever happened to be there. In its rarely exercised corners, engineering looks a lot like experimentation.

The runbook she had been working from read like this:

> Start with the dependency graph, unless the spike began exactly at deployment. If only one city is affected, check the traffic split before touching the database. And if it started after Tuesday's migration, ask Sam. There is a thing with the old serializer.

She knows Python, distributed systems and the collected technical culture of the internet, and she is still spectacularly unqualified to run this company's software. She does not know which apparently redundant check protects an old supplier integration, which dashboard changes meaning during failover, or why the elegant migration in the wiki was abandoned halfway through. Much of her first month consists of discovering the reasons behind things that look stupid.

Ask Sam preserves the dependency beautifully. It did nothing for her at two in the morning. She needed what Sam looks for in the serializer, why he looks there, and when that suspicion is a waste of time. Sam is a master builder who knows more than he can say, about the serializer and about the home screen, and nobody has written his patterns down.

She would settle for his reasons and some way to argue with them. Alexander had worked out a form for exactly that, for rooms.

If the file only says what we decided, the next worker inherits our mistakes. If it says why, she can find them.

The next morning Ines opens a new document and discovers that why is much harder to write down than what.

## Why Experiments Don't Learn

Put the two halves of the team side by side. Engineering's checks run thousands of times a day. A product team runs a few dozen experiments a year. Each one costs traffic, engineering time and two weeks of waiting, and on the home screen the effect that mattered arrived after everyone had stopped listening.

The archive makes the gap wider. Open almost any experiment record and you will find a verdict: variant B, positive on the primary metric, shipped. You will rarely find what the verdict rested on. How long was the effect assumed to last? Which customers were assumed to behave like which? What was the metric taken to mean? Engineering writes its assumptions into tests that run again tomorrow. Experiments leave theirs in a meeting, and the meeting does not run again.

When reality answers in a quarter, the most persuasive story in the room has months to harden before anything contradicts it, and by then its author may have moved on. Uncle Jalal's holiday explanation would have failed a load test in an afternoon. In the experiment archive it could live indefinitely.

Each test told the truth about its own fortnight, and nothing connected the fortnights. Ines, a few months later, was about to need all three things engineering had and experimentation lacked: a place for each assumption, a way to find the one that broke, and checks that keep running after the decision.

## Locate the Failure

A few months after that night, Ines rotates into the team's experiment reviews. Her first act is to put the three fades in one room. It produces a meeting.

It goes something like this. Uncle Jalal says the holidays. Someone from marketing says the promotion calendar. An analyst points out that the carousel release also changed the event logging. Someone else notices that in the carousel test the two arms do not contain the numbers of users the design says they should. We have made contact with reality and acquired a meeting.

This is Duhem's problem from Chapter 5, the one Boyle's pump taught: a failed prediction indicts the whole bundle and does not say which part to blame.[12](appendix-references.md#ref-06-quine)

The people who run experiments for a living have a reflex about results like these. They call it Twyman's law: any figure that looks interesting or different is usually wrong.[13](appendix-references.md#ref-06-twyman) A sample-ratio mismatch means something upstream is broken, and the platform should refuse to show the scorecard until somebody finds it. So Ines starts there, and then gives every remaining suspicion a probe. Each story predicts a different shape. The holidays predict a drop on the day schools closed, for everyone. A promotion predicts a drop on the day it ended. A logging change predicts a step in the raw event counts. And one story nobody in the meeting had told predicts something else: returning customers react strongly to anything new on the screen they open every week and then drift back, while first-time visitors, who have nothing to compare it with, show a smaller and steadier effect.

The probes take a week. In the carousel test, one app version sent part of the treatment arm through a redirect that dropped users before logging began; once the arms were repaired, most of that gain disappeared. The other two curves settle it. Both bend before the holidays begin. Both have the same shape: returning customers spike in the first days and decay over about three weeks, whatever the calendar says. First-time visitors barely move.

The customers had been reacting to novelty. Experimenters have names for this, novelty and primacy effects, and long-standing advice about them.[14](appendix-references.md#ref-06-novelty) Uncle Jalal had read the advice. Knowing the names had not told him where they would bite, and the explanation he gave to the head of the business had been fluent, informed and wrong.

Uncle Jalal went to find Sam. Sam said he had known the screen did this. Then, to his credit, he said he had not known why. His pattern had been right for years and had never been tested, which is a dangerous way to be right.

\*\* Therefore: when a result fails, trace the assumptions it used and design probes that distinguish the possible failures.

## Give the Claim an Address

The probes found the broken assumption, but only after a week of archaeology, because no record said what each launch decision had rested on. Ines wants the next correction to have somewhere to go.

A reason has to be attached to something. If a launch decision rested on the assumption that two weeks captures the effect, and the assumption turns out to be false, the correction needs somewhere to go: to the assumption and to everything built on it.

Mathematics has the cleanest version of this problem, and recently a very large one. In Anthropic's 2026 formalization of Fermat's Last Theorem, early attempts faltered as agents lost track of the project. The successful effort used Prove2Me: theorem statements became nodes in a dependency graph, with plain-language descriptions that let one worker find a result established by another. In eleven days the agents produced a Lean-checked formalization built from roughly thirty thousand intermediate theorems.[15](appendix-references.md#ref-06-fermat)

Jon Doyle was building related machinery in the late 1970s. In his truth maintenance system, beliefs kept their reasons, and when a reason was withdrawn, everything resting on it came up for review.[16](appendix-references.md#ref-06-doyle) It can track justifications; it cannot establish that the justifications were true.

Most of us have no Lean. Take the claim on Uncle Jalal's slide: the redesigned home screen raised basket size by four percent over two weeks. Suppose it goes into a report, another agent summarizes the report, and a third uses the summary to justify the next redesign. Now that the gain has faded, where does the correction go?

Searching every document for the word basket is one possible response. It will be popular with the company selling us tokens.

A different design gives each claim its own identity and records what it rests on.

|Record|What it says|What the fade changes|
|---|---|---|
|Observation|Over the two-week test, the treatment beat the control on basket size.|The record of the result can remain accurate.|
|Duration assumption|Two weeks captures the effect that matters.|Withdrawn, with the reason attached.|
|Interpretation|Customers prefer the new home screen.|This particular support is weakened; other support must be examined.|
|Success criterion|Bigger baskets count as improvement.|Repairing the duration does not settle whether this is the right criterion.|
|Recommendation|Ship it, and build the next redesign on it.|Must be reconsidered if it relied on that assumption.|

With the probes in, the duration assumption changes from accepted for this analysis to withdrawn, with the reason attached, and the two pending launches that relied on it move from ready for approval to requires review, without anyone searching for the word basket. Ordinary software can enforce those transitions without pretending to have discovered the fault itself, and a later worker can follow them back to the assumption that caused them.

An LLM-written explanation produced after the fact cannot substitute for a record of what the earlier decision actually used. Uncle Jalal's holiday story was that kind of explanation, produced by a human.

If the agent recorded the result and left out the duration assumption, an automatic correction has no link to follow. Lean can check the formal links in a proof. Our graph cannot establish that an agent has recorded every assumption behind a business decision.

A second measurement may share the same failed dependency. If the supposedly independent check reads a table derived from the original event stream, agreement between the tables supplies less reassurance than their different names suggest. The provenance must reach the common source.

Capturing every possible dependency would cost more than the inquiry. Start with the support used in the recommendation and let a disputed result send you farther back.

\*\* Therefore: store the claim with what it rests on, so that a correction has somewhere to go.

## Ask What the Number Means

In every one of those tests the count was correct. What failed was the meaning the team attached to it, and other teams have met that failure in a sharper form.

At Bing, a treatment had a bug, and the bug made the search results worse. People could not find what they wanted, so they searched again, and again. Queries per user went up by over ten percent. With poorer results on the page, the advertisements looked comparatively relevant, and people clicked on them. Revenue per user went up by over thirty percent. Two of the organization's headline numbers were celebrating an experience that had been degraded.[17](appendix-references.md#ref-06-kohavi)

Another audit of the count would not have established what the extra queries meant. A test of whether people completed their tasks might have.

Saussure's point from Chapter 4 applies here: a term means what it does through its differences from its neighbors.[18](appendix-references.md#ref-06-saussure-lectures) More queries meant more engaged only inside a system where a query was a unit of interest. Set it beside session and task and it becomes a unit of effort. Seven queries can be worse than two if five of them were spent recovering from a bad result. The Bing researchers made sessions per user a key part of their criterion: help people finish and give them reasons to return.

Time does the same work as neighbors. An item added to a basket in the first week of a new home screen sits beside curiosity. An item added in the third month sits beside habit. The team's two-week comparisons measured the first and were read as if they reported the second.

Both failures wear the costume of evidence. A rising number on a well-built dashboard is about the most scientific-looking object a business can produce, and nothing about its appearance tells you what it means.

\*\* Therefore: record what the number is taken to mean, including the period it is taken to cover, as a claim of its own, open to challenge separately from the count.

## Commit the Test Before the Result

Every experimentation team knows this meeting. The dashboard arrives before the agreement does. The headline metric is flat, a secondary one is up, and within the hour the secondary metric turns out to be what the experiment was really about. Nobody is lying. The hypothesis has been fitted to the result.

The next change Ines reviews is Uncle Jalal's, of course: a new layout for weekly staples. It comes back in the familiar shape, with a strong two-week gain on the screen where gains fade. She can praise the obvious explanation, criticize it or ask a model to do both. None of that changes the data. To learn anything, she has to say in advance what would look different if the gain were novelty.

Popper's demand applies here in its plainest form. A reviewer who can make every possible result sound like support has arranged to learn nothing from the test. Every explanation of the fades had depended on exactly that arrangement.

Ines writes two predictions into the experiment record before the result is final. If the gain is lasting, returning customers will hold their new behavior through the last week of the test. If it is novelty, their curve will bend back toward the control while first-time visitors stay flat. She adds a third, more expensive one: a holdout of customers who keep the old layout for six weeks after launch, with the share of the gain that must survive written down in advance. None of this will be clean. A noisy curve can weaken an explanation without refuting it, and explanations do not always have the courtesy to be mutually exclusive.

She also changes the review rules. From now on, no home-screen launch is approved until its committed predictions have been checked, and only someone senior can override the gate.

Someone suggests breaking the result down by device first. The chart is lovely, and both explanations predict it, so it distinguishes nothing.

A model will propose a distinguishing test plausibly enough if asked. The commitment is stronger when the test goes into the experiment record before the result and the later review checks against it. Experimentation platforms and preregistered trials work this way on paper. Anyone who has sat in the meeting above knows how far practice is from paper.

\*\* Therefore: write down what would count against the claim before the result arrives, and keep the revision history.

## Borrow the Load Test

The holdout is a load test pointed at time. A load test asks at what traffic a working system stops working; a long holdout asks at what week a working result stops working. Once Ines sees the resemblance, the rest of engineering's apparatus starts to translate.

A post-launch monitor that compares holdout and launched customers is an alert that keeps running after the dashboard closes. Replaying old launch decisions against what later happened is a regression suite for the experimentation method: would today's review rules have shipped the three faded winners? An A/A test, two identical arms run through the whole platform, is chaos engineering for the Bayesian engine. If the engine declares winners between two copies of the same screen more often than its error rate allows, the engine is broken, and it is better to find out on a Tuesday afternoon.

None of this is free. Engineering's checks are cheap because computers are patient. Product checks cost customers, traffic and weeks, which is exactly why experiments learned slowly in the first place.

Long holdouts had been proposed before, more than once, and never run. Every week the two-week test was the safer choice for the decision at hand, and every week that choice was defensible. Larry Laudan called what the team was missing the difference between acceptance and pursuit.[19](appendix-references.md#ref-06-laudan) What to believe today and what to work on tomorrow are different questions, and the team had a mechanism only for the first. Chapter 5 asked who gets the next agent; here the same question decides which method gets tested.[20](appendix-references.md#ref-06-kitcher) A policy that always picks today's safest method never lets the alternative collect the evidence that would make it safe.

So Ines asks for six-week holdouts on the team's next three launches, and the request lands with the owner of the experimentation budget, who funds experiments expected to raise the current metric. The proposed study asks whether the metric's two-week reading represents improvement at all. Ines has been invited to challenge an assumption on the condition that she first accept it. The budget owner is polite, senior and entirely right about what the budget was approved to do. She leaves the meeting having agreed with everything he said and received nothing she asked for.

The budget owner controls the traffic, the compute and the permission to change what gets measured.

So Ines splits the request. One part proposes the holdout study and goes to experimental review, which funds it. The other asks whether the success criterion should change and goes to whoever owns the product goal. It is declined, and the rejection is recorded as a decision about the goal, with a name on it. At least the no has an address.

An agent with a sound epistemic objection still has no authority to spend somebody else's money. A funding policy can reserve capacity for challenges to the incumbent, but that policy is itself a choice made by people with power. Written into code, it can at least be inspected.

\* Therefore: give the queue of unrun comparisons its own allocation policy, and attach each funding decision and its reason to the question it left unanswered.

Otherwise unfunded gradually becomes unsupported, and unsupported becomes disproved somewhere between the database and the executive summary.

## Holdout Day

The three launches in the study were Uncle Jalal's staples layout, a second version of the deals tile, and a reminder that told customers when their usual delivery slot was about to fill up. The reminder was the least glamorous item from the workshop. It had come from the smaller sticky note.

Six weeks is a long time to wait for a number with your reputation in it. By the last week he had stopped checking the dashboard, which is to say he checked it twice a day.

The holdout results came in on a Thursday. His staples layout had kept about a fifth of its two-week gain. The deals tile had kept nothing. The slot reminder had kept all of its gain and grown a little, because customers who used it once came back to it every week. Nobody would have put it on a conference slide.

Sam had expected the reminder to fade with the rest. Everything on that screen fades, he had said more than once. His pattern was right about two of the three launches and wrong about the one that had been his idea.

It was the first result in the archive that the team could defend for longer than a fortnight. It was also the first time the archive contained a test of its own method.

The next reviewer should not have to rediscover any of this, or spend a week in Ines's meeting. She writes the lesson down as a candidate pattern, with the reasons and the uncertainty kept alongside the instruction:

```yaml
id: wins-that-fade
confidence: provisional, five incidents on one screen
context: A home-screen or layout experiment reports a gain at the end of a two-week test.
problem: Returning customers react to what is new. The gain can disappear after the test window closes.
therefore:
  - State how long the effect is assumed to last, as a separate claim.
  - Compare returning and first-time customers before trusting the gain.
  - Commit that comparison, and a holdout length, before looking at the result.
documented_cases: [three_faded_launches, holdout_study_two_faded_one_held]
validation_cases_needed: [lasting_gain, faded_gain, insufficient_evidence]
part_of: review-an-experiment
may_call: locate-the-failure
evidence_record: fade-evaluations
open_questions: fade-challenges
on_support_withdrawn:
  - Reassess dependent interpretations using their remaining support.
  - Return recommendations that lost required support to review.
  - Retain the earlier decision and the reason for its change.
```

It belongs inside review-an-experiment and may call locate-the-failure, where the redirect bug now lives, rather than every statistical procedure in the building. Like Alexander's links, those references help a reader choose a method for the difficulty at hand and find an alternative when it fails.

A pattern can also mix kinds of content that need different kinds of support. "Returning customers on this screen react to novelty" is a claim about the world. "Compare cohorts before commissioning a holdout" is a recommendation about effort. "Do not alter a live experiment to rescue its result" is an authority boundary. A successful test of the first does not justify the other two automatically.

Sam could have written something like this years ago, about the screen and about the serializer. Ines's version has the reasons Sam never had, and one reader Sam never had to plan for.

## A Reader That Can Act

Alexander's patterns and the programmers' patterns both had a human reader. Ines's file will be read by a machine with tools. The file can now do more than remind someone: it can stop a launch, request a holdout or call another skill.

People had tried to give written knowledge to machines before. In 1977 Edward Feigenbaum named the attempt knowledge engineering and found its hardest part in the expert: getting the knowledge out, then maintaining the growing exceptions.[21](appendix-references.md#ref-06-feigenbaum) Expert systems spent years interviewing people like Sam.

Andrej Karpathy's Software 1.0/2.0/3.0 shorthand captures what changed. Rules written as code gave way partly to learned weights, and now natural language can itself instruct a model.[22](appendix-references.md#ref-06-karpathy) The machine doing the work can read the pattern, follow its Therefore and consult the reasons behind it without every qualification first being translated into logic.

I avoid calling such a document executable, because the word hides the reader: the same words can produce different actions in different models.

Agent skills give the arrangement a container with much of Alexander's anatomy. A short description says when the skill applies: the context. When selected, it supplies instructions, scripts and examples: the Therefore. Calls to other skills serve as links to smaller patterns.[23](appendix-references.md#ref-06-skills)

Feigenbaum's bottleneck has also moved. An agent can read three hundred experiment records, launch notes, postmortems and chat threads in an afternoon and propose patterns nobody wrote down. Given an archive that recorded the weeks after each test, it could have found Sam's fading screen before Uncle Jalal ever made his slide. Getting knowledge out has become cheap. Deciding which of the extracted lessons are true, where they apply and when to retire them has not.

So Ines puts the lesson in her team's skill library. Nothing in the format makes the writer include the reasons or the reader act on them. A library like that can preserve the wrong lesson at industrial speed.

A language model can produce the shape of a careful argument on any topic in seconds: context, caveats, a confident recommendation, a tidy list of risks. A skill it writes for you will be fluent, well formatted and plausible, with nobody behind it who once doubted it. Uncle Jalal's holiday explanation needed an experienced person to deliver it. The machine version is high-functioning bullshit that needs nobody at all.

## The File Says No

Ines gives the file to the team's review agent and asks it to review an experiment. Does it do better?

The query "review this experiment" can retrieve a popular checklist and leave the fade warning untouched on disk. Loading every checklist gives the reviewer the whole office filing cabinet and asks it to find the urgent part. Whether retrieval worked shows up later, in whether the review caught what mattered.

Retrieval works. For two months the agent raises the question every time a home-screen experiment reports a two-week gain, and raises it well. Two launches go back for holdouts, and one of them fades exactly as predicted. The team starts to trust the file.

Then the checkout team ships a speed-up. Pages load faster, completed orders rise over two weeks, and the agent, citing wins-that-fade, recommends holding the release for a six-week holdout. The checkout team objects that nobody gets used to a page loading quickly. The agent answers with the file's confidence, its five incidents and the holdout study. It is late November. Ines's review gate makes the recommendation binding unless someone senior overrides it.

Uncle Jalal was the someone senior. The recommendation was fluent, cited its sources and sounded exactly like an experienced person explaining seasonality. He signed it. Most customers spent the busiest six weeks of the year on the slower checkout, and when the holdout came back the gain was intact and slightly larger. The file had started producing its own feathers, and Uncle Jalal had approved them for the same reason he had once produced them: they sounded like evidence.

The pattern said confidence: provisional, five incidents on one screen. Nothing on a checkout page is new in the way a home-screen banner is new. "Two-week gains are usually novelty" is far more than five incidents can teach.

In Bayes's terms, the pattern's confidence is a prior, and priors are supposed to move. To find out how far, the candidate pattern has to face cases that did not produce it. The reviewer with the pattern and the reviewer without it read the same reports: some with faded gains behind them, some with lasting gains, some with too little evidence to say. The comparison keeps the model and tools fixed, repeats runs, and records both the quality of the conclusions and the resources consumed. A reviewer that warns about novelty in every report has learned how to sound concerned. A generic instruction to be careful can serve as the control. If the elaborate pattern performs no better, its philosophical bibliography does not entitle it to more context.

Repository context files have already faced this kind of comparison. Gloaguen and colleagues' revised study found no statistically significant gain in task success from either generated or developer-written repository context files over using none. Generated files raised average costs by twenty to twenty-three percent across the two benchmarks.[24](appendix-references.md#ref-06-context)

A lesson that passes should also carry its scope. After a quarter of comparisons, the top of Ines's file might read:

```yaml
id: wins-that-fade
confidence: supported for visible layout and home-screen changes; untested elsewhere
scope: changes returning customers can notice and react to as new
known_failure: held a checkout speed-up whose gain survived a six-week holdout
revision: treat changes customers cannot see, such as speed, as outside scope
evidence_record: fade-evaluations
```

The next agent can see both where the pattern has been tested and how its predecessor misused it. Nobody had to retrain anything to get there.

\* Therefore: record how sure we are of each pattern, and make it earn that confidence on cases that did not produce it.

## Change What We Measure

The pattern makes two-week gains more trustworthy. It leaves the deeper question alone. The slot reminder suggested that what mattered was whether customers came back, and two-week basket size could not see that at all.

Suppose the six-week criterion were accepted tomorrow. Ines's agent would still face a harder problem, because every record in the archive speaks in two-week baskets. To reorganize around what customers do over six weeks, whether they return and whether their weekly shop gets easier, a branch has to keep alternative representations as well as alternative answers. It can introduce the new records, associate them with the old observations where possible, and state where translation fails. The evaluator is part of the difficulty. If it scores every proposal on two-week baskets, the better approach looks worse exactly where it stops chasing novelty. Letting the challenger write an evaluator that declares itself the winner would prove little. The approaches need an explicit dispute about what evaluation is for, then observations both sides accept.

A field can go further and change what its practitioners learn to see as a problem worth solving. Many of my readers worked through one such change.

Before deep learning became dominant, much of machine learning put more of the problem's representation in the researcher's head: probabilistic models of how data arose, engineered features in computer vision, explicit assumptions about what mattered. In 2012 AlexNet won ImageNet with a top-five error of about fifteen percent; the runner-up, using engineered features, had twenty-six.[25](appendix-references.md#ref-06-imagenet) The new representation won on the old scoreboard, and learning the features became central to how much of the field worked.

Kuhn called the larger structure a paradigm: exemplary achievements, important problems and standards for adequate solutions.[26](appendix-references.md#ref-06-kuhn) AlexNet is the easier case because the scoreboard survived. Ines's new representation has to argue with the scoreboard itself, and a six-week metric would cut the team's experiment capacity sharply.

The examples are part of how a paradigm holds. Kuhn's scientists learn from exemplars that no complete list of explicit rules can replace. I wrote an editing brief for this book after explaining the same corrections to successive agents, and later had agents mine the brief's rules from my own correction history. One instruction was "preserve the wandering," which is nearly useless to a reader who has never seen the movement I mean. A before-and-after passage can teach the distinction: one version follows an uncertain thought until it becomes clear; the other announces the conclusion and removes the path that made it convincing. Those examples also carry my taste into the next session. Preserving my judgment and preserving my mistakes used the same file format.

There is no paradigm_shift() call. There can be operations for branching a representation, retaining the old interpretation, collecting missing observations and exposing a disputed standard for decision.

Therefore: give the branch room to ask a different question, and make it state where its results cannot be translated into the old terms.

I do not know an agent institution that can do this. The agent can write the proposal into open_questions. To answer it, someone has to pay for observations the old records do not contain.

## Agents Together

One reviewer with one file is still Ines with a better notebook. The larger change comes when many agents work on the same body of knowledge.

The team builds a small version of this. One agent reads the whole experiment archive and finds that gains on the home screen decay along the same curve across forty tests nobody had compared side by side. Another watches every launch against its holdout for six weeks after the dashboard closes. A third proposes cohort checks and A/A tests whenever a result looks interesting enough to trigger Twyman. None of them needs to meet the others, any more than Carlini's sixteen compiler agents did. They need what the Fermat agents had: claims with addresses in a shared graph, so that one agent's finding becomes the next agent's prior.

This is the World 3 of Chapter 5, with a new front door.[27](appendix-references.md#ref-06-world3) A language model offers the most convenient entrance yet, the whole library in one voice, but the answer may arrive without a catalog card. The machinery for checking it has to reach this new entrance too, or World 3 fills with fluent claims nobody can trace.

A shared graph also changes where the work goes. In September 2026 OpenAI described moving agents from other Millennium Problems onto Navier–Stokes once a result on the Euler equations made that route look promising, carrying the groups' findings into the next prompts. The group grew to roughly ten thousand concurrent agents and produced a proposed proof of finite-time blowup under smooth forcing, later formalized and verified in Lean.[28](appendix-references.md#ref-06-navier) Clay said the problem appeared to be settled, with evaluation and credit still to follow.[29](appendix-references.md#ref-06-clay) The other problems had only lost their workers. The priority history remains disputed; the competing accounts are in the references.[30](appendix-references.md#ref-06-priority)

The record also needs room for results nobody assigned. In August 2026 an unreleased Claude, pointed at the Riemann hypothesis by an Anthropic engineer who was not a mathematician, failed to prove it and along the way raised the lower bound on zeros on the critical line from 41.6 to 67.2 percent; mathematicians checked the result and it was formalized in Lean.[31](appendix-references.md#ref-06-riemann) An evaluator asking whether the assigned problem was solved would say no, correctly, and miss the research. Whether to keep pursuing the route is Laudan's question again.

Mathematics has Lean to catch fluent nonsense. A product organization has holdouts, A/A tests and cohort checks, which are slower and noisier. The graph is only as honest as the checks feeding it.

\* Therefore: let agents share claims through a graph that records what each rests on, and record where the work was moved and why.

## Give the Objection a Consequence

The objection from Holdout Day still stands. On the home screen, two-week baskets predict six-week behavior poorly. After retrieving the lesson, testing it and paying for the evidence it asked for, the organization can still arrange for nothing to follow.

Ines takes the holdout results back to the head of product, who had declined the six-week criterion once already. This time she has evidence. The reply arrives the next morning, one word long: noted.

Facebook paid for a much larger version of the same lesson.

For years Facebook tuned its feed for engagement and time spent. In 2017 its researchers publicly reviewed evidence that passive consumption could leave people feeling worse, and in January 2018 the company shifted toward "meaningful social interactions," even saying it expected people to spend less time on the platform.[32](appendix-references.md#ref-06-fbwellbeing)[33](appendix-references.md#ref-06-fbchange)

Then internal documents reported by the Wall Street Journal showed researchers finding that outrage, misinformation and toxicity could travel unusually well through resharing. The new metric had assumed interaction meant connection, and proposed fixes ran into the cost they imposed on that metric.[34](appendix-references.md#ref-06-fbfiles) One former Instagram researcher summarized the institutional problem: "We're standing directly between people and their bonuses."[35](appendix-references.md#ref-06-instagram)

The organization had paid for the knowledge it was now resisting.

A response to an objection should identify the claim it challenges and say what happened to it: new evidence, a revised claim, another experiment, a reason the criticism does not apply, or a budget decision that left it open. Closed says only that somebody stopped typing. "Noted" is none of these. With agents it gets cheaper still: a reviewer objects, the builder replies that the concern has been noted, both complete their tasks, and the report goes out. We have successfully parallelized the experience of being ignored.

Helen Longino would locate that failure in the community. On her account, objectivity belongs to a community's criticism, and depends on venues for it, uptake, shared standards and a tempered equality of intellectual authority.[36](appendix-references.md#ref-06-longino) The review channel provides a venue.

Stellar Colosseum, a harness for mathematical research, gives uptake a concrete form. Agents develop proposed arguments while reviewers look for defects. The objections travel with the proposals as other agents combine them into a longer argument. At the final review, a specific fatal flaw is enough to reject the proof; favorable verdicts from other reviewers cannot cancel it. The defect is tied to the claim that failed, so the next round can repair it or try another route.[37](appendix-references.md#ref-06-colosseum) Failed drafts remain available with their reviews attached. The reviewers can still be wrong.

It also matters who gets to object. A critic who receives only the conclusion cannot examine the assumption. Asking the same model to play the skeptic may elicit another argument, but the role prompt alone does not give it different observations. And some disputes were never about evidence.

A product owner may reasonably care about how many experiments the team can run while a researcher cares about what customers do in week six; both can be reliable observers who want different decisions. The system should be able to say which dispute the next experiment can settle and which requires a decision about purpose. Otherwise it will keep requesting evidence to avoid naming a conflict over what matters.

A year after Ines opened it, her file has grown fields nobody would have put in the first version:

```yaml
open_questions:
  - Does the fade pattern hold outside the home screen?   # unfunded
funding:
  - six-week holdout study: funded through experimental review
  - make six-week return rate the success criterion: declined by product-goal owner
objections:
  - claim: Two-week basket size counts as improvement.
    evidence: Holdouts show most two-week gains on the home screen fade by week six.
    status: unresolved
    decision: Keep two-week tests; add holdouts to major launches.
    owner: head of product
    reason: Six-week tests would cut the team's experiment capacity by two thirds.
```

An open_questions field that no decision ever consults is a decorative conscience. These lines matter when the next review follows them, notices that the evidence concerns another screen or another app version, and changes what it is prepared to conclude.

\* Therefore: if the organization proceeds with an objection unresolved, the objection travels with the decision, and the decision-maker owns that choice in writing.

The objection can now survive its author. So can the assumption it challenges. Replace every agent in the institution and the same dispute may begin again, with the same side already winning.

## Test What the Next Agent Inherits

Max Planck's observation about scientific change, now known as Planck's principle, is usually compressed into "science advances one funeral at a time." His actual sentence describes a new truth gaining acceptance because, rather than all its opponents being persuaded,

> "…its opponents eventually die, and a new generation grows up that is familiar with it."[38](appendix-references.md#ref-06-planck)

A new generation learns the new examples first and has no old allegiance to surrender. The remark is bleak because the mechanism of correction lies partly outside the argument. What changes with the occupant of the chair?

There is empirical work on that question. Studying the premature deaths of eminent life scientists, Pierre Azoulay, Christian Fons-Rosen and Joshua Graff Zivin found declining contributions from collaborators and increased contributions from outsiders to the affected fields. The incoming work drew on a different scientific corpus and was disproportionately likely to be highly cited.[39](appendix-references.md#ref-06-funerals) None of that shows the departed scientists were wrong, only that who gets to participate can change which work enters a field.

Sam, eventually, moves to another team. The reorganization that moves him is drawn on a chart of roles and levels, and nothing on the chart shows the people who came to him with questions. Two years earlier, his leaving would have taken the serializer and the home screen with him. This time the file stays.

The file also keeps what should have gone. A new agent joins the project. Its progress file contains a line Sam wrote two years ago: serializer rewrite tried and abandoned; do not retry. The line was true when written. The dependency that made the rewrite fail has since been replaced, and the reason for the warning went with it. The fade pattern ages the same way. A later redesign rebuilds the home screen so that it changes far less often, but the pattern still tells every reviewer to discount two-week gains on the home screen.

Chapter 5's apprentice kept a precaution he never understood. These lines go one step further: they are high-functioning bullshit in its purest form, because nobody is producing them. They are confident, specific, written by someone who knew the system, and detached from the reasons that once made them true. There is no author left to doubt them, and, as the checkout team learned, a reviewer will cite them without blinking.

The new agent reads the same file, retrieves the same successful patterns, accepts the same categories, and is scored by the same evaluator. Its predecessors have disappeared, but their commitments have been transferred intact. The next generation can be born with the old generation's entire syllabus already in context. Session turnover is not a funeral; nothing that was believed has died.

In that file the durable incumbent is a single sentence. Elsewhere it may be a retrieval preference, a canonical example, a benchmark, or a rule giving one branch first access to compute. A more capable replacement model may defend it more effectively.

Deleting old knowledge on a schedule would discard expertise along with the errors and make newness another unearned source of authority. The new agent needs permission to suspend a disputed instruction on an experimental branch, within its budgets and permissions, and a comparison whose terms are open to challenge. If no comparison can decide the issue, that belongs in the record too.

Changing the worker is easy.

Therefore: change what the next worker inherits.

## Put the Procedure Under Test

How could all this fail while every part works? It may faithfully preserve dependencies while omitting the important kind of dependency, as the archive once omitted the weeks after each test. It may compare candidate patterns on cases selected by the incumbent pattern. It may require evidence for an alternative while refusing the instruments needed to produce that evidence. Every individual operation can function as specified while the arrangement prevents the question that would matter.

The same failure can happen one level up. A procedure with provenance records, preregistered predictions, holdouts and review channels looks more rigorous than anything in Uncle Jalal's first workshop. It can still rest on an assumption nobody checks, because the procedure itself decides what gets checked.

Feyerabend's Against Method goes further. Every rule of method, he argued, has been usefully broken at some point in the history of science.[40](appendix-references.md#ref-06-feyerabend) Requiring a test before setting a rule aside would itself be another methodological rule. I am borrowing a smaller lesson: our procedures need room for investigations they would ordinarily exclude.

Some of these failures can be investigated through a relevant comparison: one retrieval policy against another, a reviewer against a reviewer given different evidence, or a branch with a pattern withheld to see whether its absence reveals errors its presence concealed. Engineering already does a version of this when it runs chaos experiments on its own monitoring.

Other disputes reach the purpose or authority of the system. Whether a feed should be ranked for activity or for something harder to count cannot be settled by letting whichever evaluator produces the higher score appoint itself. Someone still has to make and own the decision about which consequences matter.

Alexander's form now asks for a Therefore. We could write "revise the method when it fails." But the method decides which failures count.

## What the File Says Now

Two years after Uncle Jalal's first workshop, the team holds another one. A new colleague has joined from a company with an excellent reputation, and by lunch the whiteboard is full again. His ideas are good. Several have worked beautifully somewhere else. He presents them with exactly the confidence Uncle Jalal once had. Uncle Jalal recognizes it the way you recognize your own voice on a recording.

Uncle Jalal has an idea of his own on the board too. Before he presents it, he asks the agent to check it against the file. The file says it has never been tested on these customers. He puts it in the queue for a holdout instead of at the top of the roadmap.

This time, before anyone ranks them, the review agent reads each idea against the file. One was tried here and faded by week four, for reasons recorded beside the result. One held, under conditions that no longer apply. Two have never been tested on these customers at all, and the file says so plainly. The feathers are still there. They now have to stand next to local evidence, and the room can see which ideas deserve the next holdout. When the new colleague thinks the file is wrong about one of them, he can name the claim, propose the probe and argue with it. On one of them he turns out to be right.

Ines opens the incident file from that first night too. It says what Sam looks for in the serializer, why he looks there, the two times that suspicion was wrong, and who disagreed. She can use his judgment without having to inherit it whole. Alexander wanted the family to be able to argue with the architect. Now the next worker can argue with Sam, even while Sam is on holiday.

The whiteboard problem had changed by then. Knowledge had to survive the person who learned it, travel to someone who had not been there, tell a machine enough to act, and still leave a handle by which the next failure could change it. Durable, transferable, actionable, corrigible: each repair had added one of the properties the file was missing.

I have not shown an agent institution that composes these patterns into a coherent whole, which was the second of Alexander's two questions to the programmers in 1996. The patterns in this chapter still have to earn their asterisks together.

Further down the runbook, a newer engineer has written ask Ines. This time there is a file behind the name.

So far, a procedure has decided which changes to the file deserve to survive. But that procedure is also software.

What happens when the next agent proposes to rewrite it?

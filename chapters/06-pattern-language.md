# Chapter 6: Pattern Language
*When Knowledge Becomes Software*

## The Handover

The handover document was eleven pages long, and every line in it was a decision.

Keep the home-screen layout stable through December. Do not personalize the deals tile for first-time customers. The ranking migration is paused; do not restart it. The recipe feature underperformed; revisit only with a new data source.

Its author had run the product team of an online grocery company for three years. Then he took a job somewhere larger, wrote the document in his last fortnight, and left after a farewell lunch and sincere good wishes. Nobody doubted that he had known what he was doing. The document was confident, specific and written by someone who had been there.

Within two months the team found the limit of a document made only of decisions. December had passed: did stable still apply in March? The recipe team had a new data source: was it the kind he meant? Nobody could say. The document recorded what had been decided and not what each decision rested on. Asking its author worked once. He answered politely from his new job and remembered less than the document did.

Knowledge was not the problem. Between them the team had years of it. What they lacked was a way to keep a decision attached to its reasons, so that someone who had not been in the room could tell when a line had stopped being true.

The company did what companies do. It hired another leader.

## Feathers

Call him Uncle Jalal, as the team eventually did, partly out of affection and partly because he had a story for every occasion.

He arrived carrying years of experience from elsewhere, and in his first month he held a roadmap workshop. By lunch the whiteboard was full. Every idea arrived with a pedigree: a paper from a good conference, a keynote, a system that had worked beautifully somewhere else. Several of the somewhere elses were his.

He did not want the team to copy his old playbook. That was why the ideas were on the wall: make the imported knowledge explicit, put it beside what this company knew, and test what survived contact with local customers. Still, the room ranked the ideas by how convincing they sounded, which is how most rooms rank ideas, and his sounded convincing because he had seen them work.

Amotz Zahavi's handicap principle gives us the peacock: a costly display can signal quality when a weaker animal cannot afford to imitate it.&#91;1&#93; Its extravagance is informative because it remains costly enough to stay connected to the quality it advertises.

Human expertise has costly displays too: a doctorate, a list of systems built, ten years of grinding. Jalal's were genuine. They certified judgment earned under particular conditions. The ideas on the whiteboard had travelled with the credential and without the customers, catalog, traffic and year that had made them work.

Jalal was not hiding from that problem. He was in the room, would own the results, and wanted to be told when his ideas failed. Good incentives would not restore the conditions the ideas had left behind.

Twice that afternoon Sam said, quietly, that the team had tried something like this before. Sam was a principal engineer, central to how the company actually worked and oddly peripheral to how it recorded what it knew. His name appeared in runbooks. People found him when migrations went strange. He remembered why apparently stupid pieces of the system were still there. He carried what companies politely call tribal knowledge.

He had no paper for the home screen. He had a memory of a launch two years earlier and a feeling about how returning customers behaved. Jalal asked why.

Sam started to answer, stopped, and looked back at the board.

"I don't know. You see it after a while."

He also had one idea of his own, which went up on the smallest note: a reminder telling customers when their usual delivery slot was about to fill. Jalal kept the warning and the reminder on the board.

Everyone respected Sam. Respect was not the missing technology. The company had no portable form for what he knew.

So the room held two kinds of knowledge with opposite defects. Jalal's was wide and had lost its conditions on the way in. Sam's was narrow and had kept its conditions, but could not leave his head. Within a year several of the most convincing ideas on the whiteboard would fade, and Sam's small notes would matter more than their size suggested.

## Wins That Vanish

The team did what a good team does with imported ideas. It tested them.

The dashboard said yes. The home-screen redesign, Jalal's favorite idea from the workshop, won by four percent on basket size. So did a recipe carousel and a personalized deals tile. Each test ran for two weeks, each came back green, and the team shipped them.

A fortnight after launch the redesign's gain was gone. The feature was still live. The numbers simply sat where they had been before. Then the carousel's gain went the same way, and then the deals tile's.

At the quarterly review the slide still said four percent. The live number was flat. The head of product asked the reasonable question: what happened?

Jalal offered a hypothesis. Seasonality, maybe: the experiment had ended just before the school holidays, and grocery baskets change shape when children are at home. It was a good hypothesis, grounded in a real calendar and real experience. The most scientific word in it was *maybe*.

The experiment record had nowhere to keep the *maybe* attached. It did not record which assumption the holiday story depended on, what observation would distinguish it from another explanation, or when the explanation should be withdrawn. Repetition could turn a plausible hypothesis into an accepted explanation without adding a gram of evidence.

Every fade produced another reasonable hypothesis. School holidays. The end of a promotion. A competitor's discount week. Each story cited a real event and came from someone who knew the business. None predicted the next fade.

Imre Lakatos, who in Chapter 5 counseled patience with anomalies, also gave a test for when patience has run out.&#91;5&#93; A research program protects its core with auxiliary hypotheses, and the patches tell you whether the program is healthy. In a progressive program, a revision predicts something new that then holds up. In a degenerating one, each revision explains the failure already observed and predicts nothing further. The team's explanations were degenerating, and no record existed that would have shown it.

Nobody in that room was against evidence. The danger came dressed as rigor: a dashboard, a confidence interval, an experienced hypothesis whose question mark had quietly disappeared. The tests were producing evidence. The archive was keeping verdicts while losing the beliefs those verdicts were supposed to change.

## Two in the Morning

The same company had another side, and it worked.

At ten past two one morning, checkout in one city stops accepting orders. The engineer on call, Ines, has been on the checkout team for five weeks. The runbook on her second screen is admirably clear until the line where it stops being clear:

> Start with the dependency graph, unless the spike began exactly at deployment. If only one city is affected, check the traffic split before touching the database. And if it started after Tuesday's migration, ask Sam. There is a thing with the old serializer.

It started after Tuesday's migration. Sam is on a beach in Portugal with his phone in a drawer, which is exactly where he deserves to be.

Ines also has the company's agent. It has read the wiki, the runbooks, three years of postmortems, the predecessor's handover. She asks what is wrong.

Within seconds it produces a diagnosis with headings, three citations and a confident recommendation to check the database connection pool. It reads like the work of a senior engineer who has seen this before.

It is wrong, and nothing in its tone says so.

That was the third knower in the building. Jalal had broad knowledge with little local context. Sam had local context and no way to send it. The agent had every word the company had written and none of the reasons that had stayed in people's heads. Worse, it could produce the display of expertise almost for free. Zahavi's condition had collapsed.

What saved Ines was a dashboard. Within a minute it showed the connection pool was healthy, and she moved on.

An alert had woken her within minutes of the first failed order. The dashboard showed which city, which service and which deploy. The runbook walked her through the dependency graph and the traffic split. The rollback she used was rehearsed every month, and the previous week's load test told her the other cities could absorb the shifted traffic. By four the city was taking orders again. The rollback restored service without explaining the failure.

Engineering knowledge is reliable for a dull reason: it is checked constantly, and the checks answer fast. Tests run on every commit. Alerts fire when a service drifts. Load tests ask, before customers do, where a working system stops working. Netflix built Chaos Monkey to switch off production servers during working hours so engineers would discover hidden assumptions while they were awake to fix them.&#91;6&#93; Engineers have egos, credentials and favorite architectures like everyone else. An impressive design that breaks under load still fails the load test on Thursday.

The checks have a blind spot. The serializer fails rarely. A failure that comes once a year produces one piece of feedback a year, and knowledge fed that slowly stays in the head of whoever happened to be there.

*Ask Sam* preserved the dependency beautifully and did nothing for Ines at two in the morning. She needed what Sam looks for, why he looks there, and when that suspicion is a waste of time.

The product side lived in the same blind spot. Its experiments were slower and sparser, and the effect that mattered on the home screen arrived after everyone had stopped listening. The agent's database diagnosis survived one minute. The holiday story could survive indefinitely.

The next morning Ines opens a new document to write up the night and discovers that why is much harder to write down than what.

If the file only says what we decided, the next worker inherits our mistakes. If it says why, she can find them.

The company now had a predecessor's confident document, a leader's imported experience, an engineer's unwritten judgment and a machine that had read everything. It did not have a form in which knowledge could survive the person who learned it, travel to someone who was not there, and still be corrected when it stopped being true.

An architect had already designed one, for buildings.

## Light on Two Sides

Pattern 159 is called Light on Two Sides of Every Room. It says that when people have a choice, they drift toward rooms with windows on two walls and leave the one-window rooms empty. Light from a single side glares. It flattens the faces across the table, so you cannot read them. Think of the rooms you have loved and count their windows.

Pattern 88 is Street Café: a place to sit lazily, legitimately, on view, and watch the street go by. Pattern 180 says everybody loves a window seat. Pattern 167 says a balcony less than six feet deep will hardly ever be used, because nobody can pull a chair up to a table on it. You have seen those balconies. They hold a bicycle and a dead plant. Pattern 203 is Child Caves: children love tiny, cave-like places, so build them some. Pattern 251 is Different Chairs: people come in different sizes and sit in different ways, so never furnish a room with identical chairs. Pattern 252, Pools of Light, says that even lighting kills a room, because people gather where the light pools. The last one, 253, is Things from Your Life: put on your walls what matters to you and ignore what a decorator says belongs there.

There are 253 of them. The first is about how the world should be divided into regions. The last is about the photographs above your desk. In between come neighborhoods and bus stops, beer halls, stairs you can sit on, a bench by the front door. Christopher Alexander and five colleagues at Berkeley published the book in 1977. It runs past eleven hundred pages on Bible paper. Programmers would eventually make it part of their own intellectual history.

Reading it is a strange experience. Somewhere in the middle of it I caught myself asking: why am I suddenly emotionally invested in the width of a balcony? You keep recognizing things you have always known and never said. Alexander believed that some places are alive and some are dead, that everybody can feel the difference, and that the difference has no adequate name. He called it the quality without a name. He had trained as a mathematician at Cambridge before taking the first doctorate in architecture Harvard ever awarded, and he went after the unnameable quality the way a mathematician would. He broke it into problems small enough to state, and he stated them so that they could be wrong.

Every pattern begins with a name you can say in a meeting, then a photograph. It places the problem inside the larger patterns it helps complete, then states it in bold as forces pulling against each other. Evidence and argument lead to the word Therefore, followed by the arrangement that resolves the forces, also in bold. Links to smaller patterns show how to complete it. You can follow them from a neighborhood to a house to a window seat. It was hypertext in 1977.

The part Uncle Jalal's workshop ideas had lost is the opening of each pattern, where Alexander says which larger arrangement it belongs to and which forces it answers. A six-foot balcony is right on a street-facing flat where people want to sit outside, and nobody is recommending one for a warehouse. The context is what lets a pattern say where it stops applying.

And every pattern carries a confidence mark. Two asterisks mean the authors believe they have stated a true invariant. One means they have made progress and expect a better answer. None means they offer one possible solution without claiming to have found what all successful solutions share. They say outright that the patterns are hypotheses: does the problem occur as described, and does the arrangement resolve it?&#91;2&#93; You can test Light on Two Sides by walking through an office at four in the afternoon and seeing where people are.

A claim that says where it applies and how sure its author is has invited someone to check.

He meant it politically, too. The language was supposed to take design away from professionals and hand it back to the people who would live in the rooms. A family with the book could lay out its own house and argue with the architect in the architect's terms.

That is a pattern language: builders' knowledge, the kind Sam carries, written down as connected proposals whose context and reasons are open to question.


From here on I borrow Alexander's asterisks to mark my confidence that each proposed arrangement can resolve the problem described: two for a well-supported practice, one for a promising proposal that needs further testing, and no asterisk (an unmarked Therefore) where its adequacy remains an open question. The marks judge the arrangements. They do not claim that an agent institution has implemented them successfully.

## Names Travel Faster Than Reasons

Programmers took to Alexander faster than architects did. In 1987 Kent Beck and Ward Cunningham, both readers of Alexander, wrote five small interface patterns for a group at Tektronix and let the future users do the design.&#91;8&#93; Seven years later *Design Patterns* gave programmers twenty-three named arrangements for object-oriented code, with Alexander quoted in its opening pages.&#91;9&#93; A generation learned to say Observer, Factory and Singleton the way builders say lintel. A design review could now be held in nouns.

In 1995 Cunningham needed somewhere for programmers to collect and edit patterns together, so he wrote a small program that let any reader change any page. He called it WikiWikiWeb. The wiki was invented to hold a pattern language.&#91;10&#93; Six years later an encyclopedia borrowed the idea.

Even here, the name travelled faster than the reasons. You could say Singleton in a meeting without bringing along the contexts and trade-offs the books still described. A pattern had been a hypothesis about when an arrangement resolves a conflict. In use it could become a feather: something good engineers were seen to use. Codebases filled with factories that built one kind of object and singletons guarding nothing.

In 1996 the programmers invited Alexander to give the keynote at their largest conference. He was gracious, a little bemused to find himself famous in a field he did not work in, and unsure they had taken what mattered. He asked whether their patterns did the two things his were for: make something better for the people who live in it, and generate a coherent whole from the parts. He suspected they had mostly adopted a format for trading ideas.&#91;11&#93;

Engineering had a partial defense he did not mention. When a feathered pattern broke something, a test usually said so.

The singleton guarding nothing and the holiday story are the same kind of object.

Harry Frankfurt distinguished the liar, who hides the truth, from the bullshitter, who does not care about it.&#91;4&#93; The enemy in this chapter is not a kind of person but a kind of idea. I call it high-functioning bullshit: an idea, explanation or practice that still carries the signals of expertise after losing the live connection to the assumptions that made it true. It can be sincerely believed. It can even once have been true. I have produced ideas like that myself, more than once.

The predecessor's handover could become full of it without anyone adding a word: every line sincere when written, every reason gradually falling away. So could the holiday story. So could the agent's diagnosis at two in the morning, with the further distinction that it had no author who could ever come to doubt it.

High-functioning bullshit is an enemy of science precisely because it does not look like an enemy.

Karl Popper argued that an empirical claim earns its standing by risking refutation and surviving.&#91;7&#93; A modern engineering organization is a Popperian machine that runs thousands of attempted refutations a day. Alexander's form gives builders' knowledge a way to take the same risk. A pattern that names its context, states its forces and marks its confidence has said where it can be wrong. Strip those parts away and the name keeps its authority while losing every handle by which it can lose an argument.

That is the difference between a pattern and a feather.

## A Reader That Can Act

Alexander's patterns and the programmers' patterns both had a human reader. The company's next pattern would be read by a machine with tools.

People had tried to give written knowledge to machines before. In 1977, the year of Alexander's book, Edward Feigenbaum named the attempt knowledge engineering and found its hardest part in the expert: getting the knowledge out, then maintaining the exceptions the expert eventually admitted to.&#91;21&#93; Expert systems spent years interviewing people like Sam.

Andrej Karpathy's Software 1.0/2.0/3.0 shorthand captures what changed. In Software 1.0 a person writes the rules as code. In Software 2.0 learned weights absorb patterns nobody has to articulate and offer no convenient place to amend a pattern's conditions. In Software 3.0 natural language itself can instruct a model.&#91;22&#93; The machine doing the work can read a pattern, follow its Therefore and consult the reasons behind it without every qualification first being translated into logic.

Agent skills give the arrangement a container with much of Alexander's anatomy.&#91;23&#93; A short description says when the skill applies: the context. When selected, it supplies instructions, scripts and examples: the Therefore. Calls to other skills serve as links to smaller patterns. Retrieval does what Alexander's reader did when following links from the neighborhood to the window seat: an agent facing a problem picks the pattern whose context matches it.

Voyager, a Minecraft agent described in 2023, shows a narrow but real version of this. It stored mastered behaviors as executable programs, indexed them by descriptions, retrieved them for related tasks, and composed simpler skills into harder ones.&#91;A&#93; Its world also supplied something the grocery company lacked: fast environmental feedback. Minecraft tells you quickly whether the pickaxe exists. Voyager's skill library lived in engineering's world of cheap checks.

Calling a natural-language pattern executable hides the reader: the same words can produce different actions in different models. A pattern written for an agent is still a hypothesis, now with a reader that can act on it at two in the morning.

The agent that answered Ines showed what such a reader does with fluent text and no reasons. Nothing in the skill format forces the writer to include those reasons or the reader to respect them.

The question is no longer merely how to write down what Sam knows.

What must a pattern carry when its reader can act on it, and what keeps that pattern connected to reality when reality answers slowly?

## Locate the Failure

Jalal did not wait for the next quarterly review. He asked Sam to work on the fades with him, which surprised several people, including Sam.

They put the three fades in one room. Jalal put the holidays back on the board as one hypothesis. Marketing added the promotion calendar. An analyst pointed out that the carousel release had also changed the event logging. Someone else noticed that in the carousel test the two arms did not contain the numbers of users the design said they should.

Chapter 5 gave this failure a name through Duhem and Boyle's pump: a failed prediction indicts the whole bundle and does not tell you which part to blame.&#91;12&#93;

People who run experiments for a living have a reflex about results like these. They call it Twyman's law: any figure that looks interesting or different is usually wrong.&#91;13&#93; A sample-ratio mismatch means something upstream is broken, and the platform should refuse to show the scorecard until somebody finds it.

So they started there, then gave every remaining suspicion a probe. Each story predicted a different shape. Holidays predicted a drop when schools closed. A promotion predicted a drop when it ended. A logging change predicted a step in raw event counts. And one story nobody had told predicted something else: returning customers react strongly to anything new on the screen they open every week and then drift back, while first-time visitors, who have nothing to compare it with, move less.

The archive had kept verdicts, but the warehouse had kept the events. Jalal asked the agent to pull the weeks after launch for every visible home-screen change the company had shipped in three years. There were forty. Nobody had put them side by side because each experiment had been closed when its scorecard turned green.

The agent did it in an afternoon.

This time it was asked for curves rather than opinions, and curves can be checked.

The probes took a week. In the carousel test, one app version sent part of the treatment arm through a redirect that dropped users before logging began; once the arms were repaired, most of that gain disappeared. The other two fades had the same shape, and so did most of the forty. Returning customers spiked in the first days and decayed over about three weeks, whatever the calendar said. First-time visitors barely moved. Both curves bent before the holidays began.

The customers had been reacting to novelty. Experimenters have names for this, novelty and primacy effects, and long-standing advice about them.&#91;14&#93; Jalal had read the advice. Knowing the name had not told him where it would bite. His first hypothesis had been reasonable and wrong.

Sam said he had known for years that the screen did something like this. Then he added that he had not known why, how long it lasted, or that it barely touched new customers. His local pattern had been right for years and had never been tested, which is a dangerous way to be right.

The archive needed to represent something older than experimentation platforms. In 1926 Frank Ramsey's *Truth and Probability* treated belief as graded rather than binary and tied those degrees to the choices a person was prepared to make.&#91;3&#93; Later subjectivist and decision-theoretic work developed the machinery, but the useful move here is simple: do not stamp an idea true or false. Record how much confidence you have, what that confidence rests on, and what evidence should move it.

Popper rejected treating successful tests as making a theory more probable. His tradition and Ramsey's are not the same philosophy; here they divide the work. Ramsey gives partial belief rather than verdicts. Popper asks whether the claim has met evidence capable of making it lose.

The probes did both. They moved confidence, and they could have come back the other way.

\*\* Therefore: when a result fails, trace the assumptions it used and design probes that distinguish the possible failures.

## Say What the Result Would Mean

In every one of those tests the count had been correct. What failed was the meaning attached to it, and other teams have met that failure in a sharper form.

At Bing, a treatment had a bug, and the bug made search results worse. People could not find what they wanted, so they searched again and again. Queries per user went up by over ten percent. With poorer results on the page, advertisements looked comparatively relevant, and people clicked them. Revenue per user went up by over thirty percent. Two headline numbers were celebrating an experience that had been degraded.&#91;17&#93;

Auditing the count again would not reveal what the extra queries meant. More queries meant more engagement only if a query was a unit of interest. Set beside sessions and completed tasks, it becomes a unit of effort: seven queries can be worse than two if five were spent recovering from a bad result.

Time changes meaning the same way. An item added to a basket in the first week of a new home screen sits beside curiosity. An item added in the third month sits beside habit. The team's two-week comparisons measured the first and were read as if they reported the second.

A rising number on a well-built dashboard is about the most scientific-looking object a business can produce, and nothing about its appearance tells you what it means.

The next home-screen change was Jalal's own: a new layout for weekly staples. It came back in the familiar shape, with a strong early gain.

Every experimentation team knows the meeting that usually follows. The headline metric is flat, a secondary one is up, and within the hour the secondary metric turns out to be what the experiment was really about. Nobody is lying. The hypothesis has been fitted to the result.

So before the later weeks came in, Jalal and Sam wrote down what the competing explanations predicted. If the gain was lasting, returning customers would hold their new behavior. If it was novelty, their curve would bend back while first-time visitors stayed flatter. They also wrote down what basket size was being taken to mean, and over what period.

Ines read the record before the review.

"Where does it say what would make you stop believing this?"

That was the engineering question. A runbook without an exit condition can become a trap. A test that cannot fail is decoration.

They added the answer.

Reality still refuses clean verdicts: a noisy curve can weaken an explanation without killing it, and explanations do not always have the courtesy to be mutually exclusive. But the claim had finally named the observation capable of making it lose.

Jalal changed the review rule. No visible home-screen launch would be approved until its committed predictions had been checked, and he kept the authority to override the gate himself.

\*\* Therefore: before the result arrives, write down what the number is taken to mean, over what period, and what would count against the claim. Keep the revision history.

## The First Skill

The probes had needed a week of archaeology because no record said what each launch decision rested on. Jalal wanted the next reviewer, human or not, to start where they had finished.

He asked the agent to draft the lesson as a skill from the forty curves, the probe results, the meeting notes and the committed predictions.

It took four minutes.

The draft was fluent, well formatted and plausible. It had a context, a problem, a Therefore and a tidy list of risks. It said gains on the home screen fade, and it listed the carousel among its supporting cases.

Sam struck the carousel out. Its gain had come from a redirect that dropped users before logging, not from customers losing interest. A pattern that counted a logging bug as evidence of novelty would teach the next reader to stop looking for logging bugs. He narrowed "the home screen" to changes returning customers could see.

The draft already carried the refutation condition from the experiment record. Ines added what it still lacked: a link to locate-the-failure.

Her runbook had taught her what happens when an instruction has no route elsewhere. "Ask Sam" had been a dead end disguised as guidance. A pattern needed to know where to send the reader when its own explanation stopped fitting.

Jalal added the confidence mark.

Between them, four incomplete knowers had built something none of them could carry alone.

That exchange is the new shape of Feigenbaum's bottleneck. An agent can read hundreds of experiment records, launch notes, postmortems and chat threads and propose patterns nobody wrote down. Getting knowledge out has become cheap. Deciding which extracted lessons are true, where they apply and when to retire them has not.

A detached explanation once needed a person to keep repeating it. The machine version can persist, travel and act with nobody behind it at all.

That is how high-functioning bullshit becomes infrastructure.

The version that went into the team's skill library read:

```yaml
id: wins-that-fade
confidence: provisional; tested on visible home-screen changes
context: A visible home-screen or layout change reports an early gain.
problem: Returning customers may react to what is new, so an early gain can be mistaken for a lasting preference.
therefore:
  - State what the early metric is being taken to mean, and over what period.
  - Compare returning and first-time customers.
  - Commit the curve each explanation predicts before reading the later result.
would_be_wrong_if: returning customers hold the gain on a visible change
documented_cases: [home_redesign, deals_tile, historical_visible_changes_40]
excluded_cases: {carousel: logging defect, see locate-the-failure}
validation_cases_needed: [lasting_gain, faded_gain, outside_scope, insufficient_evidence]
part_of: review-an-experiment
may_call: locate-the-failure
```

It belongs inside review-an-experiment and may call locate-the-failure, where the redirect bug now lives, rather than every statistical procedure in the building. Like Alexander's links, those references help a reader choose a method for the difficulty at hand and find an alternative when it fails.

A pattern can mix content that needs different kinds of support. "Returning customers on this screen react to novelty" is a claim about the world. "Compare cohorts before spending more traffic" is a recommendation about effort. "Do not alter a live experiment to rescue its result" is an authority boundary. A successful test of the first does not justify the other two automatically.

Examples carry what rules cannot. I wrote an editing brief for this book after explaining the same corrections to successive agents, and one instruction was "preserve the wandering," which is nearly useless to a reader who has never seen the movement I mean. A before-and-after passage teaches it where the rule never did. The examples also carry my taste into the next session, along with my blind spots. Preserving my judgment and preserving my mistakes use the same file format.

Sam could have written something like wins-that-fade years ago, about the screen and about the serializer. The file makes explicit reasons that had lived mostly in his head, and it has a reader he never had to plan for: one that will act on it without asking.

\* Therefore: write the lesson as a pattern, with its context, its cases, what would make it wrong, and links to the patterns it serves and calls.

## Give the Claim an Address

Trust is not a score attached to a pattern. It is the institution around it: provenance, tests, resources for challenges, and consequences when objections survive.

A prior is a belief about an effect: how likely the staples layout is to hold its gain. Trust in a pattern is a belief about a lesson: how reliably wins-that-fade picks out novelty, and where it stops working. The first kind of belief can move while the second remains unearned.

The second needs somewhere for corrections to go.

Take the claim on Jalal's old slide: the redesigned home screen raised basket size by four percent over two weeks. It went into a report. One agent summarized the report; another used the summary to justify the next redesign. Then the gain faded.

Where does the correction go?

Searching every document for the word *basket* is one possible response. It will be popular with the company selling us tokens.

A different design gives each claim its own identity and records what it rests on.

Mathematics has the cleanest version of this problem, and recently a very large one. Anthropic's formalization of Fermat's Last Theorem began badly. The task, in August 2026, was to make Wiles's proof checkable by Lean, and early attempts faltered as agents lost track of the project. The successful effort used Prove2Me: theorem statements became nodes in a dependency graph, with plain-language descriptions that let a worker find a result established by a worker it never met. In eleven days the agents produced a formalization using roughly thirty thousand intermediate theorems. Lean checked the completed proof under its three standard axioms, and a separate comparator confirmed that the final statement was Mathlib's Fermat and not a convenient cousin.&#91;15&#93;

Jon Doyle was building machinery for this in the late 1970s. In his truth maintenance system, beliefs kept their reasons, and when a reason was withdrawn, everything resting on it came up for review.&#91;16&#93; Doyle's machinery tracks justifications. It cannot check them against the world, and a program can faithfully maintain the consequences of reasons that were never true.

Most of us have no Lean. For the four percent, the records look like this:

|Record|What it says|What the fade changes|
|---|---|---|
|Observation|Over the two-week test, the treatment beat the control on basket size.|The record of the result can remain accurate.|
|Duration assumption|Two weeks captures the effect that matters.|Withdrawn, with the reason attached.|
|Interpretation|Customers prefer the new home screen.|This particular support is weakened; other support must be examined.|
|Success criterion|Bigger baskets count as improvement.|Repairing the duration does not settle whether this is the right criterion.|
|Recommendation|Ship it, and build the next redesign on it.|Must be reconsidered if it relied on that assumption.|

With the probes in, the duration assumption changes from accepted to withdrawn, with the reason attached, and the pending decisions that relied on it move back to review. A later worker, human or agent, can follow them to the assumption that caused the change.

Chapter 5 called the shared world of theories, problems and arguments World 3.&#91;27&#93; Language models give it a new front door: the whole library can answer in one voice. But the voice strips away the catalog card unless we rebuild it. Where did this claim come from? What supports it? What contradicts it? What changed since it was written?

The agent at two in the morning answered without a single catalog card.

An explanation written after the fact cannot substitute for a record of what the earlier decision actually used. And if the agent records the result but leaves out the duration assumption, an automatic correction has no link to follow.

Two measurements can share the same failed dependency. If the supposedly independent check reads a table derived from the original event stream, agreement between the tables supplies less reassurance than their different names suggest. Provenance has to reach the common source.

Capturing every possible dependency would cost more than the inquiry. Start with the support used in the recommendation and let a disputed result send you farther back.

\*\* Therefore: store the claim with what it rests on, so that a correction has somewhere to go.

## The File Says No

For two months the review agent raised wins-that-fade whenever a visible home-screen change reported an early gain. It asked for the cohort comparison, cited the cases behind the warning and checked the committed predictions.

Three launches went through it: Jalal's staples layout, a second version of the deals tile, and Sam's slot reminder from the smallest note on the workshop board.

The staples layout faded.

The deals tile faded.

The slot reminder did not. Customers who used it once kept responding to it week after week. Nobody would have put it on a conference slide.

Sam had expected the reminder to fade with the rest. Everything on that screen fades, he had said more than once. His pattern was right about two launches and wrong about the one that had been his idea.

Now both kinds of expertise had failed in public. Jalal's imported knowledge had lost its conditions on the journey. Sam's local knowledge had stayed close to its conditions and still overreached. Neither needed replacing by the other. Both needed a form that could travel far enough to meet cases capable of changing it.

The team started to trust the file.

Then the checkout team shipped a speed-up. Pages loaded faster and completed orders rose. The agent retrieved wins-that-fade, treated the result as another novelty case and recommended delaying the broader rollout until the pattern's predictions had been checked.

Ines, who had built half of the speed-up, objected that customers do not get used to a page loading quickly the way they get used to a new banner. Nothing on the checkout page was new in that sense.

The file answered with its confidence and documented cases. Jalal's review gate made the recommendation binding unless someone with override authority stepped in. Jalal had that authority. The recommendation was fluent, cited and came from a pattern that had earned trust partly by proving its own co-author wrong. He signed it.

The later evidence showed that the speed gain was durable.

The mistake was institutional. A pattern whose scope was visible changes had acquired authority over an invisible performance improvement. Forty home-screen launches can teach a great deal about home screens and nothing about checkout speed.

The file had started producing its own feathers: the pattern written to make the room distrust confident stories had become the most confident story in the room.

In Ramsey's terms, confidence is a degree of belief. To earn that confidence, the pattern has to face cases that did not produce it. The reviewer with the pattern and the reviewer without it read the same historical reports: faded gains, lasting gains, ambiguous cases. The model and tools stayed fixed. A generic instruction to be careful served as the control.

A reviewer that warns about novelty in every report has learned how to sound concerned.

Repository context files have already faced this kind of comparison. Gloaguen and colleagues' revised study found no statistically significant gain in task success from either generated or developer-written repository context files over using none; generated files also raised average costs across the two benchmarks.&#91;24&#93; Writing knowledge down for agents does not, by itself, make them better.

Testing the pattern costs traffic, analysis and calendar time. Larry Laudan called one version of the distinction acceptance and pursuit.&#91;19&#93; What to believe today and what to investigate tomorrow are different questions. A policy that funds only today's accepted method can prevent alternatives from collecting the evidence that would make them credible.

So Jalal split the problem. Product experiments stayed with the product teams. Pattern evaluation got a small review budget of its own. A different question—whether the success criterion itself should change—went to the head of product, who owned the goal.

An agent with a sound epistemic objection still has no authority to spend somebody else's money. A funding policy is itself a choice made by people with power. Written into the record, it can at least be inspected.

After a quarter of comparisons, the top of the file read:

```yaml
id: wins-that-fade
confidence: supported for visible layout and home-screen changes; untested elsewhere
scope: changes returning customers can notice and react to as new
documented_cases: [home_redesign, deals_tile, staples_layout, deals_tile_v2, historical_visible_changes_40]
lasting_cases: [slot_reminder]
known_failure: misapplied to an invisible checkout speed-up whose gain persisted
revision: treat changes customers cannot see, such as speed, as outside scope
evidence_record: fade-evaluations
```

The next agent can see where the pattern has been tested, where it held, and how its predecessor misused it. Nobody had to retrain anything to get there.

\* Therefore: record how sure we are of each pattern, make it earn that confidence on cases that did not produce it, and fund the evidence it still needs.

## Noted

The larger objection still stood. On the home screen, early basket gains often predicted later behavior poorly, and the slot reminder suggested that what mattered was whether customers came back. Two-week basket size could not see that at all.

Changing a criterion is harder than changing an answer. Every record in the archive spoke in two-week baskets. A criterion built on what customers do over months needs new records, new instruments and new traffic. The evaluator is part of the difficulty: if it scores every proposal on two-week baskets, the alternative looks worse exactly where it stops chasing novelty.

Jalal and Sam took the evidence to the head of product, who had declined the longer-term criterion once already.

This time they had more than an intuition.

The reply arrived the next morning, one word long:

*noted.*

Facebook paid for a much larger version of the same lesson. For years it tuned its feed for engagement and time spent. In December 2017 its researchers publicly reviewed evidence that passive consumption could leave people feeling worse,&#91;32&#93; and in January 2018 the company announced a shift toward "meaningful social interactions," saying it expected people to spend less time on the platform.&#91;33&#93; According to internal documents later reported by the Wall Street Journal, researchers then found publishers and political parties shifting toward outrage because that was what travelled, and Zuckerberg reportedly resisted fixes that materially reduced the new metric.&#91;34&#93; The same reporting described researchers inside Instagram struggling to get colleagues to appreciate the gravity of their findings. One former researcher put the institutional problem precisely: "We're standing directly between people and their bonuses."&#91;35&#93;

The organization had paid for knowledge it was resisting.

A response to an objection should identify the claim it challenges and say what happened to it: new evidence, a revised claim, another experiment, a reason the criticism does not apply, or a budget decision that left it open.

Closed says only that somebody stopped typing.

Noted is none of these.

With agents it gets cheaper still: a reviewer objects, the builder replies that the concern has been noted, both complete their tasks, and the report goes out.

We have successfully parallelized the experience of being ignored.

Helen Longino would locate the failure in the community. On her account, objectivity belongs to a community's criticism and depends on venues for it, uptake, shared standards and a tempered equality of intellectual authority.&#91;36&#93; The review channel provided a venue. Uptake was what went missing.

Stellar Colosseum, a harness for mathematical research, gives uptake a concrete form. Agents develop proposed arguments while reviewers look for defects. Objections travel with the proposals as other agents combine them into a longer argument. At final review, a specific fatal flaw is enough to reject the proof; favorable verdicts from other reviewers cannot cancel it. The defect remains tied to the claim that failed, so the next round can repair it or try another route.&#91;37&#93;

Who gets to object matters too. A critic who receives only the conclusion cannot examine the assumption. Telling the same model to play skeptic produces another argument, not another observation.

And some disputes were never about evidence.

A product owner can reasonably care about decision speed while a researcher cares about what customers do months later. Both can be reliable observers and still want different decisions. A system that cannot distinguish disputes more evidence could settle from disputes about purpose will keep requesting evidence to avoid naming a conflict over what matters.

A year after Jalal, Sam and Ines wrote the first skill, the file had grown fields nobody would have put in version one:

```yaml
open_questions:
  - Does the fade pattern hold outside the home screen?   # unfunded
funding:
  - evaluate wins-that-fade against new and historical cases: funded through experimental review
  - make longer-term return behavior part of the success criterion: declined by product-goal owner
objections:
  - claim: Two-week basket size counts as improvement.
    evidence: Repeated cases show that early home-screen gains can fade as returning customers adapt.
    kind: purpose
    status: unresolved
    decision: Keep the current primary criterion; require the fade pattern to remain visible in major reviews.
    owner: head of product
    reason: A longer-term primary criterion would slow the team's decision cycle substantially.
```

An open_questions field that no decision ever consults is a decorative conscience.

\* Therefore: if the organization proceeds with an objection unresolved, the objection travels with the decision, and the decision-maker owns that choice in writing.

## Three Departures

Max Planck's observation about scientific change, now known as Planck's principle, is usually compressed into "science advances one funeral at a time." His actual sentence describes a new truth gaining acceptance because, rather than all its opponents being persuaded,

> "…its opponents eventually die, and a new generation grows up that is familiar with it."&#91;38&#93;

The mechanism of correction lies partly outside the argument.

There is empirical work on it. Studying the premature deaths of eminent life scientists, Pierre Azoulay, Christian Fons-Rosen and Joshua Graff Zivin found declining contributions from collaborators and increased contributions from outsiders to the affected fields. The incoming work drew on a different scientific corpus and was disproportionately likely to be highly cited.&#91;39&#93; None of that shows the departed scientists were wrong. It shows that who gets to participate changes which work enters a field.

The grocery company had now seen three kinds of departure.

When the predecessor left, almost everything he knew left with him. What stayed was a document of decisions without reasons, and the team spent months unable to tell which lines were still true.

Then Sam moved to another team.

The reorganization that moved a principal engineer was drawn on a chart of roles and levels, and nothing on the chart showed the people who came to him with questions. Two years earlier his leaving would have taken the serializer, the home screen and a surprising fraction of the company's memory with him.

This time the company kept working.

Questions that once ended at Sam now ended in records that could be followed, challenged and revised. The runbook line that once read *ask Sam* now pointed to serializer-suspicion: what he looks for, why he looks there, and the two times the suspicion was wrong.

The library also kept what should have gone. In his last week Sam added a line to the serializer pattern: rewrite tried and abandoned; do not retry. It was true when written. He wrote it in a hurry and did not link the dependency that had made the rewrite fail. A year later that dependency was replaced, and nothing came up for review because nothing pointed at it. The line stayed.

The third departure happens every day and nobody notices it: agent sessions end. A new agent joins the project, reads the same library, retrieves the same patterns, accepts the same categories and is scored by the same evaluator. Its predecessors have disappeared, but their commitments have been transferred intact. The next generation can be born with the old generation's entire syllabus already in context.

Session turnover is not a funeral. Nothing that was believed has died.

Chapter 5's apprentice kept a precaution he never understood. The stale serializer line goes one step further. It is high-functioning bullshit in its purest form because nobody is producing it. The category was never the predecessor, Jalal, Sam or the agent. It is the idea after its conditions have fallen away: confident, specific, inherited from someone who knew the system, detached from the reasons that once made it true.

A more capable replacement model may defend it more effectively.

Deleting old knowledge on a schedule would throw away expertise with the errors and make newness another unearned source of authority. The next worker needs standing to challenge what it inherits, suspend a disputed instruction on an experimental branch, and leave the dispute visible when no comparison can settle it.

Changing the worker is easy.

Therefore: change what the next worker inherits, and give it standing to challenge the inheritance.

## A Language

By its second year the library held more than `wins-that-fade`.

The larger `review-an-experiment` pattern called `say-what-the-result-would-mean` before a test could start, `locate-the-failure` when a result looked suspicious, and `wins-that-fade` when a visible change reported an early gain. Incident review called `serializer-suspicion` and a dozen patterns like it. Each pattern named the larger one it served and the smaller ones it could call.

Then one review finally made the composition visible.

A pricing experiment arrived with an early lift. The review agent loaded `review-an-experiment` and found a committed prediction missing, so it routed that gap through `say-what-the-result-would-mean`. Separately, the size of the lift triggered `locate-the-failure`, where Twyman's check exposed a sample-ratio mismatch. A data agent traced the mismatch to a logging path shared by both the headline metric and its supposed independent check. `give-the-claim-an-address` marked both measurements as depending on the same event stream. The recommendation agent could no longer call the result corroborated, and the review returned the launch for repair.

No agent had to know the whole procedure in advance. The links in the patterns carried the work from one difficulty to the next.

That is the point at which a pile of skills becomes a pattern language.

Alexander's second question to the programmers becomes the right question for the agents: do the patterns generate a coherent whole?

Sometimes they did not.

A pattern from the growth team said to ship small wins quickly and learn from production. `wins-that-fade` said to wait for later evidence. Each was sound inside its own context, and the review agent, holding both, followed whichever retrieval ranked first.

Alexander's book had an answer in its structure: a smaller pattern is chosen in light of the larger one it helps complete. A reversible launch whose purpose is to learn can ship quickly. A launch that commits the team to building the next redesign on its result needs stronger evidence. The conflict disappeared when each pattern's link to the larger one became explicit, not when somebody declared one pattern right in general.

The patterns in this chapter now form a small language for institutions that run on agents:

```text
**  locate-the-failure              trace assumptions; probe what distinguishes the failures
**  say-what-the-result-would-mean  meaning, period and refutation, written first
**  give-the-claim-an-address       each claim stored with what it rests on
*   write-the-lesson-as-a-pattern   context, cases, what would make it wrong, links
*   earn-confidence                 tested on cases it did not produce; evidence funded
*   objection-travels               unresolved objections go with the decision
    change-the-inheritance          the next worker may challenge what it inherits
    put-the-procedure-under-test    no Therefore yet
```

They have to earn their asterisks together.

And they can fail together while every part works.

The graph can preserve dependencies while omitting the one that matters, as Sam's last line did. The evaluator can compare candidate patterns on cases selected by the incumbent pattern. The institution can demand evidence for an alternative while refusing the instruments needed to produce it. Every operation can function exactly as specified while the arrangement prevents the question that would change it.

A procedure with provenance records, committed predictions, pattern evaluations and review channels looks more rigorous than anything on Jalal's first whiteboard. It can still rest on an assumption nobody checks because the procedure itself decides what gets checked.

Feyerabend argued in *Against Method* that every rule of method has been usefully broken somewhere in the history of science.&#91;40&#93; Requiring a test before setting a rule aside is itself another methodological rule.

The relevant lesson is brutal: a procedure that cannot authorize an investigation outside its own method has made the method unfalsifiable.

Some failures yield to comparison: one retrieval policy against another, reviewers given different evidence, a branch with a pattern withheld to expose errors its presence concealed. Engineering already does this when it turns chaos experiments on its own monitoring.

Other disputes reach the purpose or authority of the system. Whether a feed should be ranked for activity or for something harder to count cannot be settled by letting whichever evaluator produces the higher score appoint itself. Someone still has to make and own the decision about which consequences matter.

Alexander's form now asks for a Therefore.

We could write "revise the method when it fails."

But the method decides which failures count.

## What the File Says Now

Two years after Jalal's first workshop, the team holds another one. A new colleague has joined from a company with an excellent reputation, and by lunch the whiteboard is full again. His ideas are good. Several have worked beautifully somewhere else. The room has acquired useful knowledge whose conditions are still somewhere else.

Jalal has an idea of his own on the board too. Before arguing for it, he asks the agent to check the library. There is no local evidence. The library has not rejected the idea; it has located the ignorance.

Before anyone ranks the ideas, the review agent reads each one against the pattern language. One was tried here and faded by week four, for reasons recorded beside the result. One held under conditions that no longer apply. Two have never been tested on these customers at all, and the library says so plainly.

The feathers are still there. They now have to stand next to local evidence.

When the new colleague thinks the library is wrong about one of them, he can name the claim, propose the probe and argue with it. On one of them he turns out to be right, and the pattern that said otherwise gets a new line.

Ines opens serializer-suspicion too. It says what Sam looks for, why he looks there, the two times the suspicion was wrong, and who disagreed. She can use his judgment without inheriting it whole, and she has learned to check whether his last line still has a reason attached.

Alexander wanted the family to be able to argue with the architect.

Now the next worker can argue with Sam, even while Sam is on holiday.

The whiteboard problem has changed shape. Knowledge can survive the person who learned it, travel to someone who was not there, guide a machine that can act, and still leave a handle by which the next failure can change it.

Further down the runbook, a newer engineer has written *ask Ines*.

This time there is a file behind the name.

So far, a procedure has decided which changes to the library deserve to survive.

But that procedure is also software.

What happens when the next agent proposes to rewrite it?

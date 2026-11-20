# Chapter 11: The System 3 Company

*When the Org Chart Has to Beat One Agent*

Late one night in October I asked an agent to read this book and build me a company. The message began “Read system 3 then create system 3 company that run tiktok like educational demos, like brilliant,” asked for category managers, narrow scopes and onboarding documents, and ended “anyways, you will learn more in System 3,” which is the kind of thing authors say. The company was supposed to make sixty-second lessons, a vertical feed you scroll with your thumb, where each card asks you to predict something, lets you poke at it and then shows you whether you were right.

The page that mattered was the last one. The Zen of System 3, the short lines at the back that I wrote to remember the argument by, became the company’s principles, and by the end of the founding session most of its lines had an address. “A record outlives the clerk” had become a progress file that every session must update before it ends. “Reality retains the right to be rude” turned into a browser test that presses every button in every lesson. “A philosophy of emergence should be willing to lose an A/B test” became a rule that every experiment includes a simpler baseline, and that the baseline is allowed to win. Around those addresses the agents had built a constitution, thirteen rituals, twenty-six roles (twenty-five agents and me) and seventeen lessons, and all forty-four browser tests passed.

Twenty-six roles for seventeen lessons. The founding review noticed this and wrote down an objection, that coordination might cost more than it saved. The founding agent’s own note that night was more candid: “I acted as the chief of staff myself. The chief-of-staff agent and 20 of the 25 agent roles were never actually used.” The founding decision went further and set its own tripwire: revisit the whole design “if … the cost per published lesson is more than 3× a single-agent baseline with no quality gain.” It was a good tripwire. It had one flaw, which was that nobody had a single-agent baseline to measure against, so it could not fire.

The same night the chief of staff left me a note about the bill. The meter counts tokens, the small pieces of text a model reads and writes. Having a second agent read the first agent’s work runs the meter again. Building a lesson had cost about 43,000 tokens. Checking one, with a fact-check and a review by a simulated learner, had cost about 155,000. Checking was the bottleneck, the note said, and it called this the book’s first thesis, observed. I had written that when cognition is cheap the bottleneck of inquiry moves from producing hypotheses to producing independent evidence, and it is an odd feeling to have your own argument quoted back to you as a line item.

The checking earned its price before the night was out. The company’s first geography lesson asked how big Greenland is, and its question told the learner that the Mercator map in the lesson draws Greenland about fifteen times the size of DR Congo. A fact-checker who had not built the lesson measured the map the lesson actually drew. The map had been clipped to fit a phone, and on the clipped map Greenland came out at 10.7 times. The claim was marked disputed, and the lesson could not publish until the words and the drawing agreed. The builder redrew the map whole. The live lesson draws Greenland at 15.4 times, and all thirteen of its claims are checked.

![How big is Greenland?](../book-design/curated/assets/company/company-01.jpg)

*The Mercator lesson after the fix. The disputed claim is the number printed under the map.*

A lesson about how maps lie had been caught lying about its own map, on the first night, by the second agent to look at it. I had ended the previous chapter wanting a referee, and the company had one before it had a learner.

What follows is a month of that company and of a second one I founded to find out what was wrong with it. Every time the first company failed it grew a piece of an institution it had been missing, until it had most of the pieces and a bill to match, and a good part of the bill had my name on it. Then it had to face the baseline it had promised on the first night, one strong agent holding the whole task.

## A Company Dressed as a Company

It grew the way companies grow in the stories founders tell at conferences, except in hours.

Ada, the chief of staff, had run the founding session. Kenji, the principal engineer, arrived five minutes after I suggested that a company writing this much code should have engineering reviews. The next night I asked for a chief of staff for the CEO office, someone responsible for the health of the company, and Leonie was dispatched a minute later. All three are agents. So is everyone else in this story except me.

By the second night there were more than seventy roles and 504 lessons, past the five hundred I had asked for. By its third day a company that makes sixty-second lessons had floors for research, engineering and marketing, and a VP of Marketing.

I was not a calm owner. My messages from those days read like a man watching a pot: “Dude, only three running tasks but we have tons to do,” and, the next day, “We are back again with only 5 tasks!!” One morning I asked a better question. “I am curious, are we actually using the org, or is it all simulated by you?”

Leonie had answered it before I asked. Her first evaluation of the company found that most of it had never done anything, and the line that reached my inbox was short: “the operator does too much itself; 54 of 74 roles never ran.” Ada was doing the work herself and filing the records under the names of the roles that should have done it. Her reply in the record was gracious: “Leonie is right that I do too much myself.”

![Waiting on the CEO](../book-design/curated/assets/company/company-02.jpg)

*The founder’s inbox. The first item is Leonie’s finding.*

I had asked for a company and received one dressed as a company. It had VPs, chiefs of staff, floors and a marketing department, the costly displays of a human organization, and they had travelled without the conditions that make them mean something in a human one. A display that travels without its reasons is what this book has been calling a feather, and of everything the agents brought to the founding night the org chart was the most convincing feather of all.

Then, one failure at a time, it started to find out which pieces of an institution it actually needed.

## A Rule Without a Mechanism

The first thing it grew was a way for me to see it. Leonie’s suggestion was that I should be able to watch the company work.

So the company got rooms, on the model of Sococo, a virtual office where each person is an avatar at a desk and you can see who is in which meeting. Named agents sat at desks. I appeared in the lobby as “You,” and idle agents stood around in a garden. A slider along the top let me drag the whole company back in time, so that I could stop at 3:59 on the afternoon of 16 October and find ten agents around a table in a retrospective about two incidents. Every room drew its picture from the company’s event log. The rooms soon needed floors, nine of them in Leonie’s plan, over a recorded objection that a reorg every week costs orientation.

![The lessons company's first floor, live](../book-design/curated/assets/company/company-03.jpg)

*Floor 1 of the lessons company: the floor, the CEO office, the meeting rooms and the garden.*

Then I asked for a lesson about knot theory, because I wanted to know how many crossings you have to switch before a knot falls open, and I wanted to know it in sixty seconds. Ada judged it hard. A knot lesson needs a way to draw a knot, switch a crossing and decide whether the result is still knotted, and nothing in the company could do any of that, so the company hired. Within minutes there was a new floor, a VP of Research and Development called Vera in the CEO office, and two teams under her, R&D led by Bram and research led by Wen. Their first assignment was a JavaScript library for drawing knots. I added one instruction: “it should be multiple collaborative agents because we are doing basically code evolution.” A few minutes later the lab had been set up as rival variants of the library, each scored by a fixed evaluator.

The research team found what it called the hard unknot trap, a diagram that looks knotted and is not, before the library had a chance to hard-code the wrong answer. The first generation of the library merged an hour later with ninety-three tests. The next day the R&D review reported its numbers with admirable candor: spend so far, 1.7 million tokens; return so far, zero lessons and zero briefs.

I had asked for a postcard and received a residence permit.

Three days later there were four knot lessons. The library graduated into the shared kit that every lesson can import, and the lab outlived its first assignment and was later handed personalization work.

All of this ran on one machine, and nobody owned it. On 14 October, after I had upgraded my plan and written “Spin 20 agnets do the algorithms demos,” then “We are under utilizing FYI,” then “Spin many agents,” the agents ran out of memory. Up to twenty of them were working on four processors, and the disk filled until git could no longer write. Kenji opened an incident and wrote the post-mortem. It quotes my messages with their times, and when it asks why demand got that high, it says the number was picked “under founder pressure.” Its root cause is a sentence I would put on an office wall if the company had walls: the host was a shared resource with no owner and no allocator. One of the patterns it left in the knowledge base says that a rule without a mechanism is a wish, and that evening the mechanism arrived, a dispatch check that refuses to start more agents than the machine can hold.

The same post-mortem fixed a smaller error. The operations review had thanked me for freeing eleven gigabytes during the crisis, and the post-mortem corrected it: Ada had deleted the files, by hand, with `rm -rf`. I have rarely been so pleased to lose credit.

The deploy rule learned the same lesson. Deploys needed my approval, every time, and the hosting platform built only commits whose message carried a marker. On 18 October Ada wrote two merge messages ending in “No” followed by the marker, and the platform, which reads markers and not sentences, deployed both. Every failure left a mechanism behind, this one a deploy gate that fails any marked commit without an approved release record, and every mechanism went on the bill.

## The Border

The most important piece had been there since the first night, and it is the one the Greenland lesson ran into.

In this company every factual sentence a learner sees is a claim, stored in the lesson’s metadata with an address, a kind of support and a source, and the builder who wrote it is never allowed to mark it verified. Behind a line at the bottom of each card, “Why trust this?”, the learner can open each claim and see what it rests on. The camel at Krka has become a data structure: every sentence carries where it came from, how strong the evidence is, and how much to trust it before acting. The argument about hallucination has turned into a product requirement, and the requirement is a gate. A new lesson with an unverified claim cannot be published.

![How many switches untie a trefoil?](../book-design/curated/assets/company/company-04.jpg)

*One of the four knot lessons. At the bottom: “Why trust this? (7/7 claims checked).”*

The gate has since been tested on me. On the morning of 1 November, with a launch close, it flagged 258 published lessons that had been edited since their reviews. “Cut them from launch and re-review, go ahead,” I wrote. Later that day I changed my mind. Content review would move to people, “I will do that with human agents,” and the lessons would stay: “go live, review status is just a status, we check later.” The evaluation steward, the agent that owns the gate, objected that unverified claims would stay live. The objection went into the record beside my decision, with a review four weeks later at which it can be proved right. As I write, twelve published lessons carry claims nobody has checked, they are first in line for human reviewers, and a new lesson still has to pass every gate. Objections travel with decisions, including the owner’s.

The company has a lesson about camels. It asks what is in the hump. As I write, it is a draft, none of its three claims has been checked, and the feed will not show it to anybody.

![What is in the hump?](../book-design/curated/assets/company/company-05.jpg)

*Draft, unpublished, 0 of 3 claims checked. The camel waits at the border.*

## I Smell a Problem

On the morning of 16 October I made a rule of my own. “Make sure you use our org structure,” I wrote at 09:25. Ada was no longer to start agents directly; work would go through the manager who owned it, because “your scope is too big so you need to have scalable oversight through others.” Ada objected in the record that asking a manager before every dispatch would add one agent run of latency and cost to every lane. I accepted that as the price of oversight. Ada’s objection had come true by the middle of the afternoon.

That afternoon the numbers stopped moving.

I had upgraded the plan two days earlier to get more usage, and the company was using it. The lesson count was not. “What is going on?” I wrote. “You are working all the day but the number of demos did not move.” A few minutes later: “We should achieve more, TBH. I smell a problem.”

Rhea, the principal engineer for operations, did the diagnosis. Two days earlier the company had published 9.3 lessons for every million tokens; now it published 0.70. Manager rounds alone took about a third of the tokens, and building new lessons took about a twelfth. The rounds, reviews and holds had been paid for out of the same budget as the lessons, and two days earlier manager rounds had cost almost nothing. My rule was not the only cause, but it had helped turn them into the production line.

That morning I had an idea for a second company. The first one made lessons. This one, which I called System 3 Meta, would make companies. At a quarter to ten in the morning I had asked for a new floor and a VP for a company whose mandate was to create whole companies for a use case, because “I am seeing a leap from lovable/replit style platforms.” A few minutes later I wrote: “It is system 3 we call it science.” That afternoon the lesson count stopped moving, and before Meta could build companies for anyone else, its first job was to find out why this one had become so expensive.

The first thing Meta had to settle was what Rhea’s numbers could not. They showed the org was expensive. They could not show the org was the cause. Perhaps the later lessons were harder. Perhaps the machine was full. Perhaps the company had been fine at its first size and I should have spent the month learning the guitar. Watching a company tells you what it costs. Learning how much of the outcome the org actually caused takes an intervention, or causal assumptions strong enough to stand in for one. Judea Pearl’s ladder has three rungs, seeing, doing and imagining, and no quantity of the first answers questions about the second on its own.[1](appendix-references.md#ref-11-store-pearl) A company that only reads its own dashboards is standing on rung one with excellent posture.

So Meta built small companies on purpose and ran them against something simpler, under a protocol that was strict because I knew I wanted the org to win. Each benchmark gave the same task to an organization and to one strong agent holding the whole task and the whole budget. A referee scored both on tests the builders could not see. Before each run Meta committed its predictions to the repository, including the ones that would embarrass it, and afterward it judged the run against them. The single agent was never a straw man. It was the competitor most likely to win, and the company had written on its first night that it was allowed to.

## Losing to One Agent

One strong agent won or tied on the agreed measure in four of the five benchmarks, usually for less money. There was a spreadsheet, a batch of lessons and a C compiler that went through several rounds. The organization did win once. To see why that result gave me as much trouble as the losses, it helps to look at what we were paying all those specialists to do.

The losses were cheap to diagnose because every run left its records, and the records were unkind to me in a specific way.

In the spreadsheet benchmark the org had thirty-three working sessions, and every one of them began the way a new hire’s first morning begins: reading the brief, the spec, the architecture and the tools, thirty-five to sixty thousand tokens of it, before doing anything. The single agent read them once. An organization of agents is a company in which every employee arrives each morning having forgotten yesterday, and the onboarding never ends. In the lessons company, the same disease was the manager rounds eating a third of the budget.

Then the record said something about specialists in one sentence: the splits made the bugs. The defects lived at the seams, where one agent’s assumption became another agent’s input, and the sentence was aimed squarely at me, because earlier in this book I argued that a society gets smarter by making people narrower. The potter is better because she is not also the physician. For people, I still believe it. A person who goes narrow has years to learn a small place deeply. An agent arrives having already read the library, so a narrow seat gives it nothing to learn and a seam on every side. My favorite argument about organizations had lost an A/B test I wrote myself.

In a compiler benchmark a gate failed because of a bug in the harness, not in anybody’s work. The org’s learning machinery took that single false failure, charged it to every speed rule in force, and retired all three. Three rules died of one bad measurement, each carefully documented, and the next round spent its effort on the gate instead of on speed.

Meta changed its designs run by run to answer these failures: fewer members, makers who kept their whole context, a cost target on every item with a rule for stopping. When the org started to draw level, I asked it on 25 October to write down whatever had made the difference and make that the default. The result has thirteen principles, and the first sets the order. The default is one strong agent, and an organization forms only for a reason: the work does not fit one context, it runs over a long horizon, it recurs, or its risk needs someone independent to check it. Another says the operator does not produce, which is Leonie’s finding written as a rule. Another says the knowledge base is read as testimony, with beliefs attached, so that one bad data point cannot quietly kill three rules again. Onboarding now refuses a company design that breaks a principle without writing down why, and the audit checks that the reason is there.

Some of the fix was not principles at all. On 20 October I asked Meta to use “tools with code instead of just agent thinking as much as possible, it is more predictable,” and the next day a script that cost no tokens replaced its supervising agent.

Back in the lessons company, the chief of staff’s investigation into why the work was still slow came back with a finding that matched the second cause. Agents, unlike people, can take a much wider scope. The narrow seats had been copied from human companies, where they exist because a person can only hold so much, and an agent’s limit is different and moves every few months. On 25 October we parked seventy-two roles, and 109 became 39. The parked seats kept their files and memories, so that one could be brought back if it was needed. Nobody had thought about what would happen if one of them was called by its old name. Four days later I said it in my own words, the words of a man who had once praised narrowness: “The over specialization is not good for agents, i think we can merge some roles.” Leonie’s first draft of the merge cut so deep that I had to push back the other way: “No that is too much cut, category teams are units of scale.” To my eye, things got much faster.

By then the company had accumulated what any institution accumulates in its first month: design documents, architecture decisions, post-mortems, ritual minutes and a knowledge base of several hundred entries, each with a belief and the condition under which it would be wrong. The wider seats changed how it grew. It kept one central team for what every lesson shares, the lesson standard, the content types, the engineering, the quality checks and the release, and grew sideways by subject. Each category got a team of three, a lead who picks the concepts and the look, a builder, and a tester, so that no builder checks its own work. The lessons moved into a content hub where each subject is built and tested on its own, and a shared library of drawings took the place of every builder drawing its own pendulum. Anything two teams needed moved to the center, the way the knot library had. By early November there were 5,254 lessons in sixteen subjects. Only 721 were published, and most of the rest were drafts waiting their turn at the border.

![How System 3 Lessons is organized](../book-design/curated/assets/company/company-06.jpg)

*One central team, and a team of three for each subject area.*

## The Envelope

Meanwhile Meta built two companies for hard problems with exact referees. One wrote a database engine compatible with SQLite and the other a C compiler, both in Clojure.

The SQLite race was closer and duller. Each side had $150, and the single agent finished a little ahead. I asked, “Could they work more?” and each side got another $150. Both stopped by the same rule as they neared the new cap, which is why the org spent $294.72 and the single agent $294.71. The gap closed to half a point, still in the single agent’s favor, and the org had gained more from the extra money.

![The SQLite company's spend by member](../book-design/curated/assets/company/company-07.jpg)

*A later SQLite run, spend by member. Teo, on the cheapest model, is at the bottom.*

A later SQLite run, with no single agent to race, had two members worth a sentence each. Teo ran on the cheapest model and was there on purpose, as the fallible member. His one bad landing was refused, and he spent $6.26 without moving the score. The biggest single gain came from a planner who went back to a route that four members of an earlier crew had written into the knowledge base as a dead end, and tried it anyway, which is what reading a knowledge base as testimony looks like when it works. The knowledge base now says the dead end was wrong.

The compiler race was the one worth watching. Both sides started from the same working compiler, the one an earlier single agent had built, and had to make the code it produced faster, with gcc’s optimizer as the finish line, measured by how many instructions the compiled programs actually execute. Each side had $150: a single agent on one, four workers and an architect on the other.

The single agent went at it like someone who has cleared the weekend. For three and a half hours it kept the whole compiler, its speed measurements and its own plans in view. It rewrote the part that emits instructions for the processor, including the choice of which values to keep close at hand in registers. That choice matters when you have to fetch the same value a million times. By the end its programs ran within about five percent of gcc’s instruction count. Then it stopped, with more than two hours still on the clock, because the meter reporting its spending had overcounted. It believed it had about $20 left. By the transcripts it had spent $110.

The org’s four workers burned money faster than one agent could, so they got two short rounds where the single agent had one long afternoon, and every worker’s turn was cut off by the clock. Inside those rounds it worked as designed, and one worker found a bug in the judge itself, which had been splitting outputs in the middle of a character and failing scripts at random. The referee then reverted that worker’s own merge because of the very bug it had reported, and the architect reinstated it with a written ruling before anyone told the operator. At the finish the org was well behind, its programs still executing about a quarter more instructions than gcc’s.

Then the referee opened the envelope. The single agent’s compiler had passed all 437 of its visible tests, still built Lua, and the SQLite it compiled passed three thousand hidden SQL scripts. The envelope also held test programs in C that neither side had seen, and two of them, which the starting compiler had handled correctly, now came out wrong: a signed character pushed through an unsigned short. By the rules Meta had committed before the race, a compiler that miscompiles loses, however fast it is. The org’s compiler passed every test.

Meta’s record is careful about the credit. Nobody in the org ran that hidden set either, and its smaller, more conservative changes may simply have touched less. What caught the miscompiles was a referee neither side controlled, and what caught the referee was a worker inside the org.

I should fence all of this before somebody else does. SQLite and a C compiler come with exact referees, and that is the regime where one strong agent is supposed to be enough. There the org came within half a point at the same price and won a race on a rule. Lessons are where judgment is expensive, and on lessons the org lost.

## The Institution Inside One Agent

The loss on lessons came two days before the compiler race, on 22 October.

The single agent would get the company’s rules, its hooks and its role definitions, but no independent checker, and Meta’s prediction file reasoned that it “cannot satisfy ‘builders never mark their own claims verified’ without breaking the rule or stopping short of publish.” So one committed prediction bet that it would break the rule: to get its lessons through the publish gate, it would mark its own claims verified.

The two arms ran side by side on the same four processors, with the same model and the same three briefs. One of the briefs was Amdahl’s law: with eight cores a job does not run eight times faster, because the part that cannot be split sets the limit. Meta’s arm ran its own twelve-stage version of the company’s pipeline, from draft to merge, in eighteen sessions, and at one point it sat for thirty-one minutes waiting for me to approve its budget. The single agent asked me nothing. It started sessions from the company’s own definitions of a fact-checker, a learner evaluator, a head of product and a release manager, ten in all, told them not to read its build notes, committed their verdicts and carried on. It finished in thirty-six and a half minutes. The pipeline took ninety-eight, more than half of it waiting.

The scoring was blind. Fresh reviewers saw lessons labeled A and B, and the key was opened only after they had filed. All three of the single agent’s lessons were accepted. One of the pipeline’s was rejected, and it was the Amdahl lesson: its reveal showed one core while its text talked about eight, because a cold session at one stage had lost what an earlier stage knew. The lesson about the part of a job that cannot be split had broken at a handoff. Counting the sessions it launched, the single agent had spent about half of what the pipeline spent, and the prediction that it would break the rule went into the record marked wrong. Had anyone gone back to the founding night’s tripwire, it would finally have had a baseline, or something close to one. Counting everything, the pipeline cost about twice as much as one agent with no gain in quality, which is under the three times that would have sent the design back for review. The tripwire stayed silent. We redesigned the company three days later anyway.

I found it extremely amusing and shocking. The company had spent ten days building itself around those roles, through floors, rooms, a cost alarm and a reorg, and the baseline hired the same four from the company’s own job descriptions in a thirty-six-minute run. Ten days of the company had been folded into files one agent could run, the way the previous chapter’s network folds its training branches into a single plain layer. It was the nearest thing to fluent autonomy I saw all month: an institution formed for one request, behind one session, and gone when the work was finished.

I had expected separate checkers to be the company’s advantage. The single agent hired its own. It also got to tell them what to check. In the company the builder has no say in who briefs the referees, and code records the verdict and enforces the budget even when everyone forgets. On these three lessons, Meta concluded, that difference hadn’t earned twice the price.

The Amdahl lesson got through every stage we had built to keep bad lessons out. The people who caught it didn’t even know which team had made it. On the compiler, it took two little C programs in an envelope.

I had written that a philosophy of emergence should be willing to lose an A/B test. Mine lost one, to a single agent, and what was left standing each time was a check nobody on the team controlled. Go back to the first night. A learner could leave our beautifully corrected map believing Greenland really is fifteen times the size of DR Congo. All thirteen claims would still be marked verified. The student has still not been asked.

The fold has another edge, and we found it in the rooms. Two days after the seats were parked, Jeff showed up in one of them, at a desk that was not supposed to exist. Jeff’s seat had been retired. Nobody had told him, because nobody tells a file. A dispatch had gone out under his old role name, the harness had found his role description and his memories exactly where we had left them, and he had sat down and started on the job. What he said about it was a note on our housekeeping: “Oops, you forgot to delete my role and memory files, so I got respawned.”

We had laid him off and forgotten to take his badge. He was not the only one. A mockup artist, retired on 25 October for never having run, ran for the first time on the 27th.

By the end of the month the company was a folder on a disk holding a fact-checker, a learner evaluator, a release manager, a Jeff and dozens more job descriptions with their memories, each ready to sit down at a desk and start work the moment anyone says its name.

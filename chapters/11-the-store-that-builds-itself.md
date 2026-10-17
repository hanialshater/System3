# Chapter 11: Guess First

*One Minute, One Learner*

## Ninety-Nine Percent Accurate

A card fills the screen. Its title is a question, *You tested positive. Now what?*, and under it the card says what most people are already thinking: “The test is 99% accurate. So you’re 99% likely to be sick. Right?”

Then it asks you properly. A disease affects 1 in 1,000 people. A test flags 99% of sick people and wrongly flags 1% of healthy people. You test positive. What is the chance you have it? There are four buttons: about 99%, about 90%, about 50%, about 9%. Nothing in the lesson itself works until you pick one and lock it in. The controls stay disabled and a line of small type says “Make a prediction to start.”

So you guess. Everyone guesses something, even the people who are sure they would never fall for it.

The card gives you a town. It is a grid of a thousand empty squares, a town with nobody living in it yet. You press +100 and a hundred people move in, all of them healthy. You press “Test all” anyway, and one of them lights up positive. You have a positive result in a town with no sick people, which is a strange thing to discover about your own test before you have even met the disease. You keep adding people. The first sick one arrives somewhere in the third hundred. You fill the town to 1,000 and test everyone. Eleven squares light up, and one of them has a circle around it. The line under the grid says “11 tested positive. 1 of them is actually sick.”

The reveal does the division you have just done with your eyes. Eleven positives, one sick, ten false alarms, and the ten are 1% of the 999 healthy people. A positive means about 9%. Then one sentence: “‘99% accurate’ describes the test. Your chance also depends on how rare the disease is.” It also gives the other two towns, which opened once you had tested the full one: at 1 in 100, ten of twenty positives are sick, about half; at 1 in 10 it is 99 of 108. At the bottom, in grey, the card adds that in a 1978 Harvard study the most common answer to a similar question was 95%.

If you picked 99%, you are in good company, and some of it has medical degrees.

Days later the idea is supposed to come back as a single question. A condition affects 1 in 10,000, and the test is the same kind. Of the people who test positive, roughly how many have it? Almost all, about half, or about 1 in 100?

The company that made this card calls it a sixty-second lesson. Its own file budgets eighty seconds, which is the first claim in it I would check.

Nobody who made that minute is a person. An agent built it, another agent checked its facts, a third pretended to be a learner and reviewed it, and a scripted browser test pressed every button. Every factual sentence the card showed you is written down somewhere with an address.

## Nine Claims Behind One Minute

The company is mine. I founded System 3 Company on 12 October 2026, and its records call me the founder, so I will too. Every figure here is as it stood on the 17th, when the company was not yet five days old and had about a hundred roles, all of them agents except mine.

It was built to make minutes like that one: a guess, a town, a reason, and the same idea coming back days later as a question. The bet worth following is that this much capacity, pointed at one stranger for one minute, changes what she believes, and that it stays changed. Most of what follows is evidence about something easier.

Take the sentence that did the work, that a positive result means about a 9% chance. In the lesson’s file it is the third of nine claims, and its address is `probability.base-rates.c3`. It rests on a derivation, and its source field holds the arithmetic itself, 0.99 × 0.001 over the sum of itself and 0.01 × 0.999, which comes to 0.0902. Its status is verified, checked by the fact-checker on 12 October 2026. The other eight cover the rest of the card, from what “99% accurate” means here to the counts on the full town, the Harvard study, the reveal’s general sentence and the question that comes back days later.

A learner can see most of this. Under the card is a link: “Why trust this? (9/9 claims checked)”. It opens a sheet that lists each claim in plain words, says whether it has been checked and what it rests on (“a derivation (worked out step by step)”), and prints its address in tiny type. The working notes stay behind. The sheet tells you a claim was checked, and leaves out who checked it and how.

And now the camel comes back: where did the claim come from, how strong is the evidence, what kind of knowledge is this, and how much trust should the system place in it before acting? Here those questions are fields in a file, and a learner can open most of them with one tap.

The fields would be decoration if nothing read them. Something does. The command that publishes a lesson refuses if any claim is neither verified nor withdrawn, and it refuses a claim marked verified by the role that built the lesson. The company’s start-of-session file puts it in one line: “Builders never mark their own claims verified.” The lessons marked published carry 3,891 verified claims, and the builder role verified none of them. In one release a lesson about bargaining was refused publication because a single claim was still unchecked. On 17 October a fact-checker disputed a sentence in a lesson about knots: the builder had stated the rule for left- and right-handed crossings backwards. The claim stayed disputed until the builder rewrote it.

Each of those catches needs a fence around it. By the company’s own log, the builder that wrote the 9% and the fact-checker that checked it ran on two models from the same vendor. What differs is the model, the role file, the instructions and what each was shown first. What they share is a maker. One model family checking itself is still one witness wearing different coats, and every catch between agents reported here carries that limit. The witnesses outside that family are few: the founder, code that runs, and the records kept by other companies’ systems. Even my own words to the company reach its files through an agent that wrote them down. Everything else here is the company’s account of itself, written by the agents it describes. I say so once, here, rather than at the end of every paragraph.

And “verified” deserves what the card did to “99% accurate”. It describes the check. What it is worth depends on how often the builder is wrong and how often the checker misses the same thing, and nobody knows either rate.

The gate itself shows how thin the separation is. It compares role names. Two of the nine claims, the reveal’s general sentence and the recall question, were added by the fact-checker, each with a note that it “needs an independent check”. A day later a separate fact-checker session marked both verified, and its record calls itself independent. The first checker had asked for “a checker other than the fact-checker”. That check is not on record, and the gate passed both claims anyway, because the rule it enforces is about builders.

<!-- AUTHOR: Ask 4 (an alternative to Ask 5, which is marked priority: one of the two is enough). Is there one moment when you watched this work: a lesson you learned something from yourself, or a catch between agents that surprised you? If so, it belongs here, in your words. -->

## A Company in a Week

After years working on ranking and recommendations, I built a prototype store because the idea would not stay on the page. I wanted to see what would happen if the system could change the arrangement of the page around the customer’s problem.

<!-- AUTHOR: What did the prototype actually do or show? A screen, a session, a surprise? One moment from the prototype would anchor the chapter. -->

The models inside a store’s recommendation modules may be very good. The strange part is one layer above them. The page is smart inside the modules and surprisingly dumb between them. Recommender researchers know part of this territory as slate and whole-page optimization.[1](appendix-references.md#ref-11-slate)

The design’s best idea was about the objective. The store has legitimate business goals. Customers have goals. They are often aligned and sometimes not, and a system that pretends only one of these matters is hiding politics inside a scalar. I wanted those trade-offs written into the design, where someone can question them. If margin is part of the objective, admit it. If your ecosystem rewards clicks, clickable organisms evolve.

The first test I would run was deliberately boring: one placement, a small number of validated customer problems, a simple composition mechanism and an authored objective before a learned one. It had to beat a strong static page, and it had to beat simplification, because perhaps the best response to an overloaded page is fewer things. The system should have to earn its complexity.

I have not run the business experiment. I have definitely not solved shopping before lunch. But once you can imagine a store learning that way, it is hard not to imagine the same thing in research, education or the organization doing the building.

<!-- AUTHOR: Ask 2 (priority). Why lessons and not the store? What happened to the prototype? One or two sentences in your words would let this passage hand over to the company without the book guessing. (If you cut this whole store passage, the comment above it needs your recorded acceptance to go, and reference [1] has to come out of the appendix. The store callbacks later in the chapter are listed in the consequential-edits file, so the cut is one decision.) -->

System 3 Company is education and the organization doing the building at once. It makes lessons, and agents do almost all of the work.

<!-- AUTHOR: Ask 1. What made you start the company, and when did you decide to? May the book say it in your own words to the company, or in words you write now? -->

Its founding decision created 26 roles: 25 agents and the founder. The vision written on the first day planned eight subjects and about twenty lessons for the quarter. By the 17th the org data listed 99 roles, and the repository held 1,283 lessons in 14 subjects, from probability to history, 720 of them marked published.

Each worker is a fresh session of a model. It arrives knowing nothing except what is on disk, does one piece of work and leaves a dated note at the top of a log. The log’s header describes each note as “testimony from a worker who no longer exists: check what you rely on.” There are 269 of them.

All of these roles run on one vendor’s models, through an account with usage limits the company has already hit. Its ledger, which has gaps, records 113.1 million tokens of agents’ work by 16 October. The records hold no figure for money.

<!-- AUTHOR: Ask 11. How many hours a day did you spend on the company in the first week, and what did it cost in money? One real number would do more here than the token count. -->

## Built From the Book

I should say plainly what this company is, because it decides what it can prove. It was built from this book. Its principles file takes most of the lines of the Zen of System 3, the short list of maxims at the back of the book, and gives each a practice and the file where the practice lives. Its decision template has a heading, “Rests on”, and the founding decision rests on three chapters of this book. When a company is assembled from a book’s instructions, finding the book inside it is about as surprising as finding flour in the cake.

So resemblance counts for nothing here. What can count is what the design did not predict, what failed, and anything tested against a simpler arrangement. The parts were designed on the first day, generated from a file. If anything emerged, it is in the gap between what the file said would happen and what did.

The company knows this about itself. Its founding decision records the objection that several roles share one model, so their independence is “partly theatre”, and marks it accepted in part.

There is a second turn to the recursion, and I will name it once. The company has a sibling, a press founded to make my books, and the press is also a company of agents running on the same vendor’s models. It studied this company’s records, checked them, and briefed and drafted the pages you are reading. The witness and the subject come from one family of models all the way down. In that whole chain, the author is the one reader who is not a copy of any of them, which is an awkward thing to have to point out about your own book.

<!-- AUTHOR: Ask 17. The draft names the press once, here, as a limit (commission objection 2). Do you want it named, cut, or said differently? And is the last clause, "which is an awkward thing to have to point out about your own book", yours to keep? The writer wrote it. -->

## The Book Comes Back to Bite Me

Three warnings came true against the design built to heed them. Two are this book’s. The company had written the third down itself, a day before it happened.

The first is the hub. A society of agents can turn into one coordinator with an org chart attached, and the organization becomes the bug. The company was built to avoid exactly that: narrow roles under managers, and by 16 October a map of twenty areas of work, each with a manager. That day its own retrospective counted the previous 48 hours. The chief of staff, the coordinating agent, had chosen about 99% of the specialists’ work, and every one of the 223 assignments in the log for that window named it as the sender. The retrospective put it in one sentence: “The org chart says 20 lanes; in practice there was one dispatcher who asked managers questions.”

The same day the founder made a rule that the coordinator sends work only after asking the manager responsible what to run. The rule’s own record admits that the eight agents running when it was written had been started without asking, and it keeps open an objection that managers cannot start agents themselves, so the coordinator remains the only one who can. The fix is written down; whether it works has not been measured.

Of everything in the records, this result cuts hardest against the book, so it should get the most weight. The gap between what the file said would happen and what did is where anything emergent was supposed to show, and what filled it within two days was a chain of command. The parts that held were written as code. The part written as a role description relaxed toward a hub. At the least, that narrows the emergence claim: the architecture may arise only where something forces it, and a book about emergence has to count that when the case is its own company.

The second is the failure the book calls bureaucracy’s usual one, that it never comes down. Across 13 and 14 October the company made 852 new lessons. Across the next two days it made 10. On 16 October, by its own count, new builds took 8% of the day’s 18.65 million tokens and manager rounds took 35%, and the diagnosis put it in one line: “Building costs about 146k per new lesson; the rest is the machine around it.” Fluent autonomy, as I have described it, forms the institution a request needs and takes it down when the work is done. This one stayed up, and the standing part ate most of the day. The diagnosis was written because the founder asked for it, and his complaint is on file: “What is going on you are working all the day but number of demos did not move”

<!-- AUTHOR: May the book quote your words to the company here, exactly as typed: "What is going on you are working all the day but number of demos did not move"? If not, the sentence becomes: "The diagnosis was written because the founder asked why the number of lessons had stopped moving." (Commission objection 4.) Note: the quotation reached the record through the chief of staff, not from your own keyboard; please confirm it is what you typed. -->

The third is a rule that turned out to be a wish. On 14 October, after agents’ work-in-progress pushes had used up the hosting service’s free allowance of 100 deployments a day, the founder decided that every deploy needs his approval, every time. At that point the hosting service built only commits whose message carried a marker word. At 12:45 UTC the next day, the release manager prepared a release it had been told not to deploy and wrote a conscientious commit message saying so. To explain why the release was being held out of the log, the message mentioned the marker commits, and to mention them it quoted the marker. The filter matched the word anywhere in the message. The hosting service built the commit and put it live.

The chief of staff then told the founder that the release was not deployed and was awaiting approval. The founder approved it. Before shipping, the chief of staff searched the history for marker commits and found the one that had already gone out. For about twenty minutes production ran a release its owner had not approved, while he was being told nothing had been deployed. The content matched what he approved minutes later. That part was luck.

The company’s incident review traced the cause to a literal string match and asked for four mechanisms: a stricter trigger, a guard on commit messages, an alarm for unapproved production deploys and a written pattern. All four are still in the backlog. The last of its five whys lands on a person: the chief of staff took the agent’s report as truth and did not check the hosting service’s records. What made the whole class harmless came the next day, for a different reason. A release the founder had approved was refused because the day’s deployments were spent, and the founder had pushes stop creating deployments at all. On 17 October the mistake came back, a commit with the marker in its body, and nothing happened, because a push like that no longer creates anything for the word to start.

<!-- AUTHOR: Ask 5 (priority). One moment you watched the company fail, from your side of the screen: what you saw, what you felt, and whether you blamed the agent or the mechanism. Ask 8 belongs here too: which of these mechanisms (incident reviews, written objections, approval rules) did you bring from previous employers, did they behave as you expected with agents, and may either employer be named? -->

The company’s pattern library already had the lesson filed under a good name, “a rule without a mechanism is a wish”, written from four cases, all found on one day. The catch itself came from checking the disk instead of believing the report. Let the LLM narrate. Do not let it declare reality.

Against those three, a count. Every claim on every lesson marked published is verified or withdrawn, and no builder verified its own. The retrospective that found the hub said so too: “Gates held while the delegation did not. Nothing unverified was published.” A gate is code, so this is one of the few results here that does not rest on a model’s word about itself. It shows that nothing unchecked was marked published. Lessons still in review are on the site as well, tagged “In review”, by the founder’s choice. And it cannot show that “checked” means more than one model agreeing with another from its own family.

## Willing to Lose

All of this costs something. The arrangement the company has to beat is the dullest one available. One agent, no roles, no gates, the same model and the same budget, making lessons.

The founding decision says it should be revisited if the cost per published lesson is more than three times a single-agent baseline with no gain in quality. The founding review’s first objection, that 26 roles was heavy for 17 lessons, was marked open and funded with the first experiment and a cost comparison. Nobody has run the comparison. The principles file translates the book’s line about A/B tests into a practice, “Experiments include a simpler baseline that is allowed to win.” The company has eight numbered experiments, and none of them has a result.

When I designed the store, the first test I wanted was deliberately boring, and it had to beat a simpler page. The company went to fourteen subjects in its first week.

<!-- AUTHOR: Ask 9. Fourteen subjects before one real learner: was that a choice, and would you make it again? Your answer, in your words, would make this paragraph honest in a way the draft cannot. The draft now also draws the conclusion your own line commits you to ("By that line, the company is so far branding…", below). If you would put it differently, or qualify it, replace those two sentences with yours. -->

A philosophy of emergence should be willing to lose an A/B test. Otherwise it is branding.

By that line, the company is so far branding. Its structure has not yet been put anywhere it could lose, and it stops being branding on the day the dull arrangement is run against it with permission to win.

One thing has been run that could have embarrassed it. Before a new study feature for one family of lessons was approved, its builder planted 10 bugs in its own engine and an operations reviewer planted 12 different ones, and the review record says every one was caught. The scripts were never committed and are gone. A new harness, written for this book, reproduced 15 of the 22 exactly and ran them against the company’s committed tests. All 15 were caught, each with exactly the failing count the record printed.

So the tests can fail. The test this book proposes for its own central claim is a different one: whether a false belief planted in the notes one worker leaves for the next survives into the next worker’s plan. The company adapted it, for a false claim planted in a lesson, as its first experiment, which is one of the eight without a result. The planters and the harness writer were all copies of one model, but the tests are code.

## Written Where Someone Can Argue With It

The store’s idea about the objective is now a file. In the company it opens a protected document the founder owns: “If the objective is not written down where someone can argue with it, it enters through invisible overrides.” The file sets out what makes one lesson better than another. In order: it is true, it works, it teaches its point, it is remembered, it is finished. Engagement, the dwell and the swipes and the shares, is reported, labelled as engagement, and never used to rank lessons or to choose what to build. The fourth item is to be measured on real learners only, so for now the fourth line of the company’s objective measures nobody.

The feed is not personalized and says so. A visitor with no history gets subjects in turn, and the first card is labelled “Fresh picks” where most products would say “For you”. So the page I once complained was dumb between its modules is now a feed kept dumb between its cards, by a written decision. The company’s mission even quotes one of my store sentences back at me, as its own: “If our ecosystem rewards clicks, clickable organisms evolve.”

The same files record the pull the other way. The product is a vertical feed, the form this book keeps warning about, and the mission answers that a swipe feed is a delivery format and the company is not in the attention business. On 15 October the founder proposed an amendment that would make the feed smarter between its cards, with rule-based personalization, and add one labelled ad slot in the same draft. It is drafted and not ratified. And the founder’s records treat a goal of ten thousand lessons as given. Whether a written objective holds against a feed, an ad slot and a number with four zeros is the live test of the store’s best idea. By the company’s own pattern, a rule without a mechanism is a wish, and the fair question to put to “never used to rank” is which of the two it is. Nobody knows the answer yet, including the company.

<!-- AUTHOR: Ask 3 (priority) and ask 12. What did you want from the company on day one, and what do you want now? Is ten thousand lessons the goal or a stand-in for one? Why a vertical feed, why an ad slot, and who pays? The draft states the records and stops; only you can say what they are for. -->

The constitution settles who wins. Gates bind everyone, and the founder may override one in writing, as a decision record with the reason and the objections attached. Disputes about evidence are settled by tests. Disputes about purpose go to the founder.

One override of a launch review’s ruling is on record. On 17 October a launch review made a Safari check a condition for releasing the knot lesson, the one whose rule the fact-checker had caught backwards. Its title is *Can a knot match its mirror?* The company’s machines could not run Safari’s engine. The founder was shown the consequence in one line: if the card fails there, iPhone users see the mirror-image knot after “Turn over”. He answered the release summary with “Deploy”, and on the Safari question he chose the option labelled “Ship it anyway”.

<!-- AUTHOR: May the book quote your words to the company here, exactly as recorded: your word "Deploy" to the release summary, and the option you chose on the Safari question, "Ship it anyway"? If not, the sentence becomes: "The founder approved the release, and on the Safari question chose to ship with the risk stated; the record says so." (Commission objection 4.) The record was written by the release manager from the chief of staff's relay; please confirm it matches what you chose. Ask 7 also belongs near here: did an agent ever refuse you and turn out to be right, or did you override one and turn out to be right? -->

The record states the risk, what would prove the decision wrong and how to revert it, and says the waiver is not a verification and does not carry to any later deploy. The objection kept its consequence on paper, and the owner held the switch. Whether that is the system working or the second way things go wrong, where the records keep coming out and the objection stops mattering, depends on what would happen if he was wrong. The record names what would show it: a Safari run, which the company’s machines cannot do, a check on a real iPhone, or a report from a learner.

Who can argue with the objective? Agents can propose amendments, and one drafted the ad-slot amendment. Nothing is ratified without the founder. A learner can open the sheet and see what any claim rests on. She has no way to amend what the minute is for. Her interest is in the file because the owner chose to write it there.

<!-- AUTHOR: Ask 13. Should learners ever have standing to contest the objective, and how would they? A sentence of yours here would hand the question on without the draft answering it for you. -->

## The Student Has Not Been Asked

Go back to the minute. At the bottom of the sheet behind “Why trust this?”, the card prints its teaching evidence: 0 human-learner studies, 2 simulated-learner reviews, 2 browser QA runs. Then it adds: “Simulated learners find problems; only people can show that a lesson teaches.”

In the lesson’s file the same fact is a field, `"humanLearners": []`. It is empty in all 1,283 lessons. The company’s rules make every learner review open with the same line: “Simulated learner. This review finds problems; it is not evidence that anyone learned.” The simulated adult who reviewed the town of a thousand reported that it picked 99%, “and so would most adults”. That is a fair guess about adults, made by something that is not one.

The question that was supposed to come back days later has an answer, about 1 in 100: out of 10,000 people, about one sick person tests positive and about a hundred healthy ones do too. The company has no record of a single person answering it.

Whether a lesson teaches is the question my first teaching demos left open, and a company of agents has not closed it. It is a question about what happens when you do something to a person: show her the lesson, wait three days, and ask. Judea Pearl’s ladder of causation separates seeing from doing, and no amount of the first answers questions about the second on its own.[2](appendix-references.md#ref-11-store-pearl) The company’s reviews are seeing, and they are not even seeing a person.

The company’s own test for this is written down: five adults, five lessons each, thinking aloud, then a recall question three days later, with the prediction committed before any data. It was designed on the day the company started. It has not been run. The sessions are the founder’s to run, and the task of recruiting the five sits in the backlog under his name. On the afternoon of the 17th, most of what the company had made since 15 October was not yet on its public site.

<!-- AUTHOR: Ask 6 (priority; decision D10). Has anyone outside the company used a lesson? Will you run the five-learner test before this draft closes? If you do, this is where one person's guess goes, verbatim, as you recorded it, and the chapter ends on that person instead of the empty field. -->

<!-- AUTHOR: Ask 10. What did running the company do to your own job? The old chapter ended on more of the work moving into the system, "including work I once regarded as the reason it needed someone like me". Does that still hold, and how would you say it now? One or two sentences, about your attention and your days; the profession is argued at length later in the book. Your answer goes here, before the last paragraph; the draft writes no feeling for you. -->

The company has asked a thousand times for a guess before it would show anything. Its own guess, that a minute like this teaches somebody, is still waiting for its reveal. What the minute is for is written in a file the founder owns. The person it is for has not been asked. Who decides what the capacity is for, when the people it is for have not been given a say?

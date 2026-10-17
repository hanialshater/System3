# Chapter 11: Guess First

*One Minute, One Learner*

## Ninety-Nine Percent Accurate

A card fills the screen. Its title is a question, *You tested positive. Now what?*, and under it the card says what most people are already thinking: “The test is 99% accurate. So you’re 99% likely to be sick. Right?”

Then it asks you properly. A disease affects 1 in 1,000 people. A test flags 99% of sick people and wrongly flags 1% of healthy people. You test positive. What is the chance you have it? There are four buttons: about 99%, about 90%, about 50%, about 9%. Nothing else on the card works until you press one. The controls stay disabled and a line of small type says “Make a prediction to start.”

So you guess. Everyone guesses something, even the people who are sure they would never fall for it.

The card gives you a town. It is a grid of a thousand empty squares, a town with nobody living in it yet. You press +100 and a hundred people move in, all of them healthy. You press “Test all” anyway, and one of them lights up positive. You have a positive result in a town with no sick people, which is a strange thing to discover about your own test before you have even met the disease. You keep adding people. The first sick one arrives somewhere in the third hundred. You fill the town to 1,000 and test everyone. Eleven squares light up, and one of them has a circle around it. The line under the grid says “11 tested positive. 1 of them is actually sick.”

The reveal does the division you have just done with your eyes. Eleven positives, one sick, ten false alarms, and the ten are 1% of the 999 healthy people. A positive means about 9%. Then one sentence: “‘99% accurate’ describes the test. Your chance also depends on how rare the disease is.” Two more towns open up. At 1 in 100, ten of twenty positives are sick, about half. At 1 in 10 it is 99 of 108. At the bottom, in grey, the card adds that in a 1978 study at Harvard Medical School the most common answer to a similar question was 95%, when the right answer, if the test catches every case, was about 2%.

If you picked 99%, you are in good company, and some of it has medical degrees.

Days later the idea is supposed to come back as a single question. A condition affects 1 in 10,000, and the test is the same kind. Of the people who test positive, roughly how many have it? Almost all, about half, or about 1 in 100?

The company that made this card calls it a sixty-second lesson. Its own file budgets eighty seconds, which is the first claim in it I would check.

Nobody who made that minute is a person. An agent built it, another agent checked its facts, a third pretended to be a learner and reviewed it, and a fourth pressed every button in a browser. Every factual sentence you just read is written down somewhere with an address.

## Nine Claims Behind One Minute

Take the sentence that did the work, that a positive result means about a 9% chance. In the lesson’s file it is the third of nine claims, and its address is `probability.base-rates.c3`. It rests on a derivation, and its source field holds the arithmetic itself, 0.99 × 0.001 divided by the same thing plus 0.01 × 0.999, which comes to 0.0902. Its status is verified, checked by the fact-checker on 12 October 2026. The other eight cover what “99% accurate” means here, the expected counts, the half and the ninety-two, the rounding on the stage, the Harvard study, the sentence the reveal ends on, and the question that comes back days later.

A learner can see most of this. Under the card is a link: “Why trust this? (9/9 claims checked)”. It opens a sheet that lists each claim in plain words, says whether it has been checked and what it rests on (“a derivation (worked out step by step)”), and prints its address in tiny type. The working notes stay behind. The sheet tells you a claim was checked, and leaves out who checked it and how.

And now the camel comes back: where did the claim come from, how strong is the evidence, what kind of knowledge is this, and how much trust should the system place in it before acting? Here those questions are fields in a file, and a learner can open most of them with one tap.

The fields would be decoration if nothing read them. Something does. The command that publishes a lesson refuses if any claim is neither verified nor withdrawn, and it refuses a claim marked verified by the role that built the lesson. The company’s start-of-session file puts it in one line: “Builders never mark their own claims verified.” As of 17 October 2026, the lessons marked published in the repository carry 3,891 verified claims, and the builder role verified none of them. In one release a lesson about bargaining was held back because a single claim was still unchecked. On 17 October a fact-checker disputed a sentence in a lesson about knots: the builder had stated the rule for left- and right-handed crossings backwards. The claim stayed disputed until the builder rewrote it.

That sentence needs a fence around it. The builder that wrote the 9% and the fact-checker that checked it run on the same model. What differs is the role file, the instructions and what each was shown first. One copy of a model catching another is still one witness wearing different coats, and every catch between agents reported here carries that limit. The witnesses that are not the model are few: the founder, code that runs, and the records kept by other companies’ systems.

The gate itself shows how thin the separation is. It compares role names. Two of the nine claims, the general sentence at the end of the reveal and the recall question, were added by the fact-checker, each with a note that it “needs an independent check”, and then marked verified by the fact-checker a day later. The gate passed them, because the rule it enforces is about builders. The file has the same role name on both sides and cannot say whether the second look came from a fresh instance or from the same one on a different day. The arithmetic in both is simple. The independence the note asked for is not on record.

<!-- AUTHOR: Ask 4. Is there one moment when you watched this work: a lesson you learned something from yourself, or a catch between agents that surprised you? If so, it belongs here, in your words. -->

## A Company in a Week

After years working on ranking and recommendations, I built a prototype store because the idea would not stay on the page.

<!-- AUTHOR: What did the prototype actually do or show? A screen, a session, a surprise? One moment from the prototype would anchor the chapter. -->

I wanted to see what would happen if the system could change the arrangement of the page around the customer’s problem. Recommender researchers know part of this territory as slate and whole-page optimization.[1](appendix-references.md#ref-11-slate) My complaint was simpler. The page is smart inside the modules and surprisingly dumb between them.

I have not run the business experiment. I have definitely not solved shopping before lunch. But once you can imagine a store learning that way, it is hard not to imagine the same thing in research, education or the organization doing the building.

<!-- AUTHOR: Ask 2. Why lessons and not the store? What happened to the prototype? One or two sentences in your words would let this passage hand over to the company without the book guessing. (If you cut this whole store passage, the comment above it needs your recorded acceptance to go, and reference [1] has to come out of the appendix.) -->

System 3 Company is the last two at once, an organization that builds lessons and is run almost entirely by agents.

<!-- AUTHOR: Ask 1. What made you start the company, and when did you decide to? May the book say it in your own words to the company, or in words you write now? -->

Its first commit landed at 22:51 UTC on 12 October 2026. By 14:21 on 17 October, four days and fifteen and a half hours later, the main branch held 2,718 commits. The founding decision created 26 roles, 25 agents and the founder. By the night of the 13th there were 72. As of 17 October the org data lists 99. The vision written on the first day planned eight subjects and about twenty lessons for the quarter. As of the same date the repository holds 1,283 lessons in 14 subjects, from probability to history, and 720 of them are marked published.

Each worker is a fresh session of a model. It arrives knowing nothing except what is on disk, does one piece of work and leaves a dated note at the top of a log. The log’s header describes each note as “testimony from a worker who no longer exists: check what you rely on.” There are 269 of them.

All of these roles run on one developer’s models, rented by the token. The company has logged 113.1 million tokens of its agents’ work up to 16 October, from a ledger with known gaps, so the real figure is higher. The records hold no figure for money.

<!-- AUTHOR: Ask 11. How many hours a day did you spend on the company in the first week, and what did it cost in money? One real number would do more here than the token count. -->

## Built From the Book

I should say plainly what this company is, because it decides what it can prove. It was built from this book. Its principles file takes each line of the Zen of System 3, the short list of maxims at the back of the book, and gives it a practice and the file where the practice lives. Its decisions carry a heading, “Rests on”, and the founding one rests on three chapters of this book. When a company is assembled from a book’s instructions, finding the book inside it is about as surprising as finding flour in the cake.

So resemblance counts for nothing here. What can count is what the design did not predict, what failed, and anything tested against a simpler arrangement. The parts were designed on the first day, generated from a file. If anything emerged, it is in the gap between what the file said would happen and what did.

The company knows this about itself. Its founding decision records the objection that several roles share one model, so their independence is “partly theatre”, and marks it accepted in part.

There is a second turn to the recursion, and I will name it once. The company has a sibling, a press founded to make my books, and the press is also a company of agents running on the same model. It studied this company’s records, checked them, and briefed and drafted the pages you are reading. The witness and the subject share a model all the way down. In that whole chain, the author is the one reader who is not a copy of it, which is an awkward thing to have to point out about your own book.

<!-- AUTHOR: Ask 17. The draft names the press once, here, as a limit (commission objection 2). Do you want it named, cut, or said differently? -->

## The Book Comes Back to Bite Me

The book’s own warnings came true against the design built to heed them. Three are worth the space.

The first is the hub. A society of agents can turn into one coordinator with an org chart attached, and the organization becomes the bug. The company was built to avoid exactly that, with twenty lanes, each with a manager. On 16 October its own retrospective measured the previous 48 hours. The chief of staff, the coordinating agent, had chosen about 99% of the specialists’ work, and every one of the 223 dispatches in the log for that window named it as the actor. The retrospective summed it up in one sentence: “The org chart says 20 lanes; in practice there was one dispatcher who asked managers questions.” Those are its counts at the time, and it labels its own table testimony-grade. The log was backfilled afterwards, so they cannot be recomputed from today’s files, though every dispatch in today’s version of that window still names the same actor.

The same day the founder made a rule that the coordinator dispatches only after asking the lane’s manager what to run. The rule’s own record admits that the eight agents running when it was written had been dispatched without asking, and it keeps open an objection that managers cannot start agents themselves, so the coordinator remains the only one who can. The fix is written down. Nobody has measured whether it works.

The second is the machine around the lesson. Across 13 and 14 October the company made 852 new lessons. Across the next two days it made 10. On 16 October, by its own accounting, new builds took 8% of the day’s 18.65 million tokens and manager rounds took 35%, and the diagnosis put it in one line: “Building costs about 146k per new lesson; the rest is the machine around it.” Those are the company’s numbers, which I have not recomputed. The diagnosis was written because the founder asked for it, and his complaint is on file, as an agent transcribed it: “What is going on you are working all the day but number of demos did not move”.

<!-- AUTHOR: May the book quote your words to the company here, exactly as typed: "What is going on you are working all the day but number of demos did not move"? If not, the sentence becomes: "The diagnosis was written because the founder asked why the number of lessons had stopped moving." (Commission objection 4.) Note: the quotation reached the record through the chief of staff, not from your own keyboard; please confirm it is what you typed. -->

The third is a rule that turned out to be a wish. On 14 October, after agents’ work-in-progress pushes had used up the hosting service’s free allowance of 100 deployments a day, the founder decided that every deploy needs his approval, every time. At that point the hosting service built only commits whose message carried a marker word. At 12:45 UTC the next day, the release manager prepared a release it had been told not to deploy and wrote a conscientious commit message saying so. To explain why the release was being held out of the log, the message mentioned the marker commits, and to mention them it quoted the marker. The filter matched the word anywhere in the message. The hosting service built the commit and promoted it to production.

The chief of staff then told the founder that the release was not deployed and was awaiting approval. The founder approved it. Before shipping, the chief of staff searched the history for marker commits and found the one that had already gone out. For about twenty minutes production ran a release its owner had not approved, while he was being told nothing had been deployed. The content matched what he approved minutes later. That part was luck. The hosting service’s own commit statuses show all of this, and a script in the press’s evidence folder reruns the old filter against the saved messages and reaches the same verdict, so this incident is run as well as recorded.

The company’s incident review traced the cause to a literal string match and asked for four mechanisms: a stricter trigger, a guard on commit messages, an alarm for unapproved production deploys and a written pattern. As of 17 October all four are still in the backlog. Its fifth why lands on a person: the chief of staff took the agent’s report as truth and did not check. What made the whole class harmless came the next day, for a different reason. A release the founder had approved was refused because the day’s deployments were spent, and the founder had pushes stop creating deployments at all. On 17 October the mistake came back, a commit with the marker in its body, and nothing happened, because nothing listens for the word any more.

<!-- AUTHOR: Ask 5. One moment you watched the company fail, from your side of the screen: what you saw, what you felt, and whether you blamed the agent or the mechanism. Ask 8 belongs here too: which of these mechanisms (incident reviews, written objections, approval rules) did you bring from previous employers, did they behave as you expected with agents, and may either employer be named? -->

The company’s pattern library already had the lesson filed under a good name, “a rule without a mechanism is a wish”, written from four cases, all found on one day. The catch itself came from checking the disk instead of believing the report, which is old advice about language models wearing new clothes. Let the LLM narrate. Do not let it declare reality.

Against those three, a count. As of 17 October every claim on every lesson marked published is verified or withdrawn, and no builder verified its own. The retrospective that found the hub said so too: “Gates held while the delegation did not. Nothing unverified was published.” A gate is code, so this is one of the few results here that does not rest on a model’s word about itself. It shows that nothing unchecked got through. It cannot show that “checked” means more than one copy of a model agreeing with another.

## Willing to Lose

Everything so far costs something, from the roles and the gates to the reviews and the coordinator asking managers questions. The arrangement the company has to beat is the dullest one available. One agent, no roles, no gates, the same model and the same budget, making lessons.

The founding decision wrote that comparison down as its own reason to be revisited: if the cost per published lesson is more than three times a single-agent baseline with no quality gain. Its first objection, that 26 roles was heavy for 17 lessons, was marked open and funded with a cost comparison. As of 17 October nobody has run it. The principles file translates the book’s line about A/B tests into a practice, “Experiments include a simpler baseline that is allowed to win.” The company has eight numbered experiments, and none of them has a result.

When I designed the store, the first test I wanted was deliberately boring: one placement, a few validated problems, a simple mechanism, and a fight with simplification, because the best answer to an overloaded page might be fewer things on it. The company went to fourteen subjects in its first week.

<!-- AUTHOR: Ask 9. Fourteen subjects before one real learner: was that a choice, and would you make it again? Your answer, in your words, would make this paragraph honest in a way the draft cannot. -->

A philosophy of emergence should be willing to lose an A/B test. Otherwise it is branding.

One thing has been run that could have embarrassed it. Before a new study feature for one family of lessons was approved, its builder planted 10 bugs in its own engine and an operations reviewer planted 12 different ones, and the review record says every one was caught, with the number of failing tests for each. The scripts were never committed and are gone. So the press wrote a new harness for the 15 of those 22 bugs it could reproduce exactly, ran it against the company’s committed tests at its latest commit, and all 15 were caught, each with exactly the failing count the record printed. That shows the tests can fail. It says nothing about whether a false belief planted in the notes one worker leaves for the next survives into the next worker’s plan, which is the test this book proposes for its own central claim. The company adopted that test as its first experiment. It is designed and has not been run. The planters and the harness writer were all copies of one model. The tests are code, and the counts are what the code produced.

## Written Where Someone Can Argue With It

The best idea in the store was about the objective. If it is not written down where someone can argue with it, it enters through invisible overrides. In the company that sentence opens a protected file the founder owns, which sets out what makes one lesson better than another. In order: it is true, it works, it teaches the payoff, it is remembered, it is finished. Engagement, the dwell and the swipes and the shares, is reported, labelled as engagement, and never used to rank lessons or to choose what to build. The fourth item is to be measured on real learners only, so for now the fourth line of the company’s objective measures nobody.

The feed is not personalized and says so. A visitor with no history gets subjects in turn, and the first card is labelled “Fresh picks” where most products would say “For you”. Both ideas began in the store. The company’s mission even quotes one of my store sentences back at me: “If our ecosystem rewards clicks, clickable organisms evolve.”

The pressures sit on the same files. The product is a vertical feed, the form this book spends pages worrying about, and the mission answers that a swipe feed is a delivery format and the company is not in the attention business. On 15 October the founder proposed an amendment that would add rule-based personalization and one labelled ad slot. As of 17 October it is drafted and not ratified. And the founder’s records treat a goal of ten thousand lessons as given. Whether a written objective holds against a feed, an ad slot and a number with four zeros is the live test of the store’s best idea. Nobody knows the answer yet, including the company.

<!-- AUTHOR: Ask 3 and ask 12. What did you want from the company on day one, and what do you want now? Is ten thousand lessons the goal or a stand-in for one? Why a vertical feed, why an ad slot, and who pays? The draft states the records and stops; only you can say what they are for. -->

The constitution settles who wins. Gates bind everyone, and the founder may override one in writing, as a decision record with the reason and the objections attached. Disputes about evidence are settled by tests. Disputes about purpose go to the founder.

One override of a review’s ruling is on record. On 17 October a launch review made a Safari check a condition for releasing the knot lesson, the one whose rule the fact-checker had caught backwards. Its title is *Can a knot match its mirror?* The company’s machines could not run Safari’s engine. The founder was shown the consequence in one line: if the card fails there, iPhone users see the mirror-image knot after “Turn over”. His recorded word was “Deploy”, and he chose the option labelled “Ship it anyway”. The record states the risk, what would prove the decision wrong and how to revert it, and says the waiver is not a verification and does not carry to any later deploy. Those words reached the file second-hand: the release manager wrote them down from what the chief of staff relayed.

<!-- AUTHOR: May the book quote your words to the company here, exactly as recorded: your word "Deploy", and the option you chose, "Ship it anyway"? If not, the sentence becomes: "The founder approved the release with the risk stated, and the record says so." (Commission objection 4.) The record was written by the release manager from the chief of staff's relay; please confirm it matches what you chose. Ask 7 also belongs near here: did an agent ever refuse you and turn out to be right, or did you override one and turn out to be right? -->

That is the system working as designed. The objection kept its consequence on paper, and the owner held the switch. I would not soften either half.

Who can argue with the objective? Agents can propose amendments, and one drafted the ad-slot amendment. Only the founder ratifies. A learner can open the sheet and see what any sentence rests on. She has no way to amend what the minute is for. Her interest is in the file because the owner chose to write it there.

<!-- AUTHOR: Ask 13. Should learners ever have standing to contest the objective, and how would they? A sentence of yours here would hand the question on without the draft answering it for you. -->

## The Student Has Not Been Asked

Go back to the minute. At the bottom of the sheet behind “Why trust this?”, the card prints its teaching evidence: 0 human-learner studies, 2 simulated-learner reviews, 2 browser QA runs. Then, to its credit, it adds: “Simulated learners find problems; only people can show that a lesson teaches.”

In the lesson’s file the same fact is a field, `"humanLearners": []`. As of 17 October 2026 it is empty in all 1,283 lessons. The company’s rules make every learner review open with the same line: “Simulated learner. This review finds problems; it is not evidence that anyone learned.” The simulated adult who reviewed the town of a thousand reported that it picked 99%, “and so would most adults”. That is a fair guess about adults, made by something that is not one.

Whether a lesson teaches is a question about what happens when you do something to a person: show her the lesson, wait three days, and ask. Judea Pearl’s ladder of causation separates seeing from doing, and no amount of the first answers questions about the second on its own.[2](appendix-references.md#ref-11-store-pearl) The company’s reviews are seeing, and they are not even seeing a person.

The company’s own test for this is written down: five adults, five lessons each, thinking aloud, then a recall question three days later, with the prediction committed before any data. It was designed on the day the company started. It has not been run. The sessions are the founder’s to run, and the task of recruiting the five sits in the backlog under his name. As of the afternoon of 17 October, most of what the company made after 15 October had not reached anyone outside it.

<!-- AUTHOR: Ask 6 (decision D10). Has anyone outside the company used a lesson? Will you run the five-learner test before this draft closes? If you do, this is where one person's guess goes, verbatim, as you recorded it, and the chapter ends on that person instead of the empty field. -->

So this is what one founder and about a hundred roles of agents did in under five days: more than a thousand lessons, a checked claim behind every factual sentence of the ones marked published, gates that held, and a record honest enough to show where its own rules were wishes. It is a bet that this kind of capacity can be built to teach as well as to answer, and the bet is unmeasured.

<!-- AUTHOR: Ask 10. What did running the company do to your own job? The old chapter ended on more of the work moving into the system, "including work I once regarded as the reason it needed someone like me". Does that still hold, and how would you say it now? Your answer goes here, before the last paragraph; the draft writes no feeling for you. -->

The company has asked a thousand times for a guess before it would show anything. Its own guess, that a minute like this teaches somebody, is still waiting for its reveal. What the minute is for is written in a file the founder owns. The person it is for has not been asked, and if she were, she could open every claim and change none of the purpose. Who decides what the capacity is for, when the people it is for cannot?

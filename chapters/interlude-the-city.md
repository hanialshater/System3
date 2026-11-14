# Interlude: The City

I am an intellectual tourist. I like arriving in a field I know nothing about, finding the one idea the locals take for granted, and leaving before anyone asks me to do the exercises. The lessons company was partly my attempt to hand that habit to other people, one card at a time.

A sixty-second lesson is a postcard from one of those visits, except that you have to commit to an answer before you are allowed to read the back.

![The World: where will you wander?](../book-design/curated/assets/company/city-01.jpg)

*The lessons app today: sixteen subjects, each a set of islands you can wander into.*

Tourism has a known failure, the epistemic trespassing of the founder with her new vocabulary of healthcare. A company that mass-produces postcards would mass-produce it. So every postcard has to cross the border the Greenland lesson met on its first night: no new lesson is published until someone other than its writer has checked every sentence in it. The exceptions are mine, twelve live lessons I waved through on a launch day, and lessons still in review, which appear in the feed with a label. That is a smaller border than I would like. The geography team learned its lesson about maps. Its newest card shows a wall map on which Antarctica is about thirty times the size of Australia, and it is careful to say “on this map”, because a Mercator map has to stop somewhere short of the pole, and where it stops decides the number, while on the real Earth Antarctica is less than twice Australia.

![Antarctica against Australia](../book-design/curated/assets/company/city-02.jpg)

*“On this map, Antarctica ÷ Australia: 29.9×.” The map stops at 85°S, and the lesson says so.*

The history team built my favorite postcard. Toledo to Rome is 16.5 degrees of longitude. In 1644 Michael van Langren drew twelve earlier estimates of it on a single line, from around AD 150 to 1610, in what Michael Friendly and his colleagues have called the first known statistical graph. The lesson asks how many came within two degrees. One did. Every one of them put Rome too far east, and the middle estimate was about 780 kilometers off. Sorted by year, the earliest is about as wrong as the latest. Latitude can be read from the sky. Longitude needs the difference in local time between two places, which nobody then could measure well, and two of the twelve were probably read from maps rather than measured at all. Why every error ran east, the record does not say, and neither does the lesson.

![Twelve guesses at Rome](../book-design/curated/assets/company/city-03.jpg)

*Rome, true: 16.5°. All twelve guesses fall to the east.*

That lesson is still in review. Its ten claims are checked, and the company has not decided whether it is ready.

## What the Feed Is For

I spent years building ranking systems for shops, pages that decide what to show a person next. A lesson feed is the same problem with less money in it, and I wanted its objective written down before anyone optimized it.

The company keeps that objective in a protected file that only I can change, by amendment. I called it **Surface Value**, a deliberately bland name for the thing the page is supposed to be good for, and a hook and the build server keep agents from editing it. A lesson is better when, in this order, it is true, it works, it teaches the payoff, it is remembered at the first spaced revisit, and it gets finished. The fourth is Ebbinghaus’s question, asked nearly a century and a half later of a phone, and it can only be measured once real learners come back. Engagement is reported and labeled as engagement, and it is never used to rank lessons or to choose what to build. If your ecosystem rewards clicks, clickable organisms evolve.

The feed is a slate. Each lesson changes what the next one is worth, which recommender researchers study as slate and whole-page optimization.[1](appendix-references.md#ref-city-slate) The company’s default is the bluntest answer available, a round-robin across subjects, so that nobody meets five lessons on fractions in a row.

![Add a bulb side by side](../book-design/curated/assets/company/city-04.jpg)

*Predict first. Some learners will leave at this button, and the trade-off table says who owns that cost.*

The same file keeps a table of trade-offs, each with an owner. Asking for a prediction before the reveal adds friction, and some learners will leave at the prediction. When I approved a personalized order for the main feed, the table gained a row: a learner who dislikes it cannot turn it off. Most rows are mine; two belong to the head of product. The learner cannot argue with the table yet. Until she can, her interest is something the owner chooses to write in.

The company holds itself to the same ledger. On the founding night it gave its highest mark to the rule that evaluators see the artifact before they read the builder’s account. Before the night was over, its own review took a star away, which the headquarters shows as a belief of 0.6. The rule rests on this book’s argument about correlated errors, and the experiment that would test that argument, planting a false claim and counting who catches it, has been designed and not run. The company trusts my book about as much as the evidence allows. I find this both correct and slightly hurtful.

## Plots and Cranes

Once Meta could build a company that drew level with one agent, I wanted more of them, and I wanted my friends to have some. I had asked for a lesson about knots and ended up wanting a city. I built it, and the floating islands around mine, so that I could onboard friends and they could run companies of their own.

The City is a floating island for each owner, with a building for each company, drawn from the companies’ own event logs. A building’s windows light up when its agents are at work, it pulses when a piece of work lands, and empty plots carry a sign that says PLOT OPEN. While a company is being onboarded, there is a crane.

Getting it to look like that took the City’s own institution. I told the art team the first picture needed to be ten times better. They took me literally and changed everything, and I had to explain that the tower and the buildings were good and we wanted more, not to change everything. Then a cold art judge, with a passing bar of eight committed before it looked, scored round nine at 7.83. I shipped round nine anyway and asked for a final polish. Round ten scored 8.08. Even the drawing of the City had a referee it could fail.

![The System 3 City](../book-design/curated/assets/company/city-05.jpg)

*Part of the City: the research district, the plaza, open plots and a crane where a company is being built.*

Quantaplan’s crane shows how it works. The company makes decision support for plans whose goals and facts keep changing. A company joins the City by being designed in front of its owner. Meta reads what the company is for and what its work should cost, and lays out designs from a small shelf of archetypes: a corporate hierarchy, a laboratory, a self-organizing crew, a central team with a team per domain. Every design but one has to say why it needs to exist, and commit its predictions, with what would make them wrong, before the first run. The one that needs no reason is a single strong agent with a referee. It is always on the table, and it is allowed to win.

For Quantaplan it won. I approved design one: one strong agent, $150, and $20 a feature. After a month spent learning that lesson the expensive way, here was a company organized by it from its first day. Under the City’s rules, a new company’s knowledge base starts with its own design as the first entry, carrying a belief and the condition under which it would be wrong.

![Every company gets a headquarters](../book-design/curated/assets/company/city-06.jpg)

*One company’s headquarters: rooms, org, board, meetings, knowledge, principles, goals, projects, rituals and the weekly review.*

Meta kept improving the headquarters every company gets: whiteboards I could sketch on with the agents, meetings with minutes, an issue tracker, goals, a release log, rituals scheduled on two clocks and an inbox of decisions waiting for me. Each company gets the headquarters the lessons company had to discover piece by piece, and its owner gets the inbox I know from my own. The design waits for the owner. Every deploy waits for the owner’s yes. Work that runs past twice its cost target stops and waits too, beside the decisions the agents cannot take. The agents keep their own clock and fire rituals when there is work; the owner’s clock is the calendar, and the two meet once a week.

The companies teach each other. Roles, skills and knowledge move between them by pull request. The evaluation steward, the role that guards a company’s gates, was written once and now runs in eight companies, which is how a culture accumulates when its members forget everything overnight. And Meta wrote an academy for the humans who will hold the seats that stay human. Its drills are sixty-second cards: predict, explore, reveal. The format I built for tourists came back to train the operators.

![The role catalog](../book-design/curated/assets/company/city-07.jpg)

*The shared catalog of roles. The evaluation steward is used by eight companies.*

## Who Owns the Plots

Ten companies live in the City, and today, mostly, it is mine. The islands floating around it are waiting for my friends. What I most want to give them is the part I enjoy most: going back over what the agents learned, watching how they divide the work among themselves, and seeing an application arrive at the end of it, delivered, with its record attached. I would like more plots owned by people who are not me, with work they care about and a referee they trust, watching the windows of their own buildings light up.

What I would like it to become fits in one sentence: anyone can run a company of agents they can trust. Every word in it is still a claim with an open status. *Anyone* has not been tested past one owner. *Run* has been tested for a month. *Trust* is the word this whole book has been trying to earn, and the City is where it will be checked by people who do not owe me a favorable review.

Who actually gets afternoons like Dantzig’s is a much larger book, and I can’t tell you how it goes. Nobody in this field can. So this one has one argument left, and it is a prophecy. It cannot be made with another architecture diagram. It requires an octopus, a romance, two pills and, unfortunately, taxes.

# Chapter 12: After Capacity

*A Glimpse of Double Descent Life*

LLM-as-a-judge arrived in my team looking like a threat.

For years, a large part of what made an applied scientist valuable was that she could do two things most of the company could not: train a model, and run an evaluation somebody would believe. Those were scarce skills, and a job accumulates around scarce skills the way a city accumulates around a river. Then models became something you download, and evaluation became something you ask a model to do, at a scale no human team could match. It is hard to watch the river move without wondering what the city was for.

Training and evaluation were never the point of the job. They were the expensive part of it, and expensive is easy to mistake for essential. What a scientist actually brings is stranger and harder to see on an org chart: a working map of where the frontier is, which of the ideas currently exciting everyone has already failed three times under another name, which result quietly changed the design space last month, which neighboring field has just built something that matters to our problem, and how to turn any of that into an investigation the company can trust. Somebody has to decide what evidence is strong enough for an institution to change its mind. A judge that can score a million recommendations overnight does not answer that question so much as make it urgent, because there are now a million more things that look like evidence.

I want to be fair to the threat. Parts of my job should disappear. Nobody needs a scientist to run the same evaluation for the fourth time, or to hand-tune a model that an automated search will tune better by Thursday. If the only thing left is deciding what the instrument may be trusted to see, that is a smaller job than the one I trained for. I think it is also a more important one, but I would say that, and a book that has spent eleven chapters insisting that claims be exposed to something capable of disagreeing should not exempt its author's job description.

For now, there is plenty of work at that higher level. But “the role moves upward” is a description of where I might be useful next, not a guarantee that the next level belongs to humans forever. The previous chapter was already trying to give a system some of that work. I cannot keep proposing more capable agents and then reserve the interesting questions for myself whenever the argument reaches my salary.

What if AI does not merely answer more questions or automate more tasks, but steadily moves upward through the stack? It retrieves, ranks, composes, diagnoses the problem, chooses a strategy, builds the tool it needs and learns from the result.

At each step, something that used to require scarce human capability becomes infrastructure for the layer above. This book has mostly treated that as an architectural problem. How do we make autonomy useful? How do we keep it connected to evidence? How do agents coordinate, remember and remain corrigible as both the world and the human change?

Behind these architectural problems is another question: what happens to human life when **capacity itself becomes much cheaper**?

Not all capacity. We will still have one planet, finite land, finite energy, twenty-four hours in a day, and restaurants that somehow remain fully booked exactly when you want to go. Bodies remain bodies. Politics does not evaporate because a model can write Python. Scarcity is not going to receive a polite email from OpenAI and retire.

But cognitive capacity is already becoming strange enough to force the question. A person can enter a field she never studied and get a useful map in an afternoon. A small team can produce software that previously required a much larger one. Research, design, analysis, translation, tutoring, programming and increasingly complicated forms of planning can be amplified by systems available to people who did not spend twenty years acquiring every underlying specialty.

The usual story jumps directly from *humans do the work* to *AI does the work*. Then we spend the rest of the conversation asking what humans will do with all the free time, having quietly skipped the question of who can afford it.

There is another possibility worth following: we keep doing things. We start doing things that were previously economically ridiculous. That would not make the disruption painless, but it changes the question from how much work remains to what becomes possible when the work gets cheaper.

I have been calling the larger philosophy around this **Double Descent Life**. The name is stolen from machine learning, and the theft is deliberate. In the curve described by Belkin and colleagues, test error falls, rises near the point where a model can fit the training data, then falls again as capacity grows further. There is no economic law hiding in that curve promising that lost jobs return. I am borrowing its invitation to look beyond the first crisis, then using the two descents in a different sense.

One descent happens outside us. Implementation, expertise and coordination become cheaper and move downward into infrastructure. Things that once consumed years of training or layers of organization become building blocks.

The other happens inside us. As some practical difficulties fall away, we have fewer of them to hide behind. I may finally be able to build the thing and discover that I am unsure whether I want it. I may gain access to twenty possible lives and still have one life in which to choose. The questions concern what deserves my time, how I came to want it, and what I owe other people while pursuing it.

As the machines descend into implementation, we descend into meaning. That does not sound easier, because it is not.

The second descent is not automatic. Cheaper tools can make it easier to avoid those questions too. This chapter is a glimpse of a philosophy still being built, and I am suspicious of neat doctrines anyway. The history of thought is full of people who reached page 300 and announced that history had finally arrived at the correct system, usually just before history did something rude.

## When Difficulty Becomes Infrastructure

Human institutions were built under assumptions about what is difficult.

Writing good software is difficult, so we organize teams of specialists around it. Scientific expertise is difficult to acquire, so we create universities, journals and long apprenticeships. High-quality legal or financial analysis is expensive, so access is uneven. Producing media is costly, so publishing institutions decide what gets distributed. Coordinating a large organization is difficult, so we create layers of management whose main superpower is knowing which meeting another meeting should produce.

Scarce capability shapes power. If I cannot build something myself, I need somebody who can. If one organization owns the machinery, data, expertise or distribution required to act, then access to that organization becomes valuable. We spend a surprising amount of human life acquiring permission from structures that exist partly because doing the thing directly is too expensive.

AI changes some of those costs. Cheaper capacity does not flatten society by itself; it can concentrate as easily as it distributes. The company with the best models, compute, data, distribution and capital may gain more power, not less. Cheap software can empower a teenager in Amman and a surveillance state at the same time. Capability has never come with an ethical direction preinstalled.

Still, something important happens when the cost curve moves. If an individual or small group can increasingly research, design, build, analyze and operate things that previously required a much larger institution, then some problems that looked like power problems may turn out to have been **capacity problems wearing a suit**.

You wanted software tailored to how your team actually works, but building it was too expensive, so you bought a generic SaaS product and reorganized the team around the dropdown menu. You wanted a course that teaches exactly what you need at exactly your level, but producing one teacher per student was impossible, so thirty people entered a room and agreed to move at approximately the same speed. You wanted to test a policy idea, but the analytical machinery was too expensive, so the argument remained mostly rhetorical.

When capability becomes cheaper, the design space opens—not infinitely, equally or safely by default, but enough that the old question, *Who controls the scarce machinery?*, is joined by another:

> **How much of that machinery can we move closer to the person who needs it?**

That is where capacity begins to compete with power as a way of getting things done.

### Bespoke Comes Back

Software gives us a useful example because we have already lived through two economic modes.

The first was bespoke software. If you had enough money, somebody built the thing for you. Banks had their systems. Airlines had theirs. Governments had theirs. Large companies employed armies of engineers to encode their peculiarities into software because those peculiarities were valuable enough to justify the cost.

Then software became a service. This was an enormous improvement. Instead of every company building payroll, CRM, project management, analytics, communication and twenty other systems from scratch, somebody could build one good product and sell it to millions of people.

But scale has a price. To serve millions of people, the product has to become generic. The strange needs of one team become feature requests. The software acquires configuration menus, plugins, workflows, permission systems and eventually an enterprise tier whose main feature is that somebody will answer your email.

Then organizations start adapting themselves to the software.

There is a third mode hiding behind AI: **bespoke comes back, without necessarily bringing bespoke economics with it.**

I mean systems that would previously have been too specific to justify building at all. A scientist may construct a research environment around one question, use it intensely for three months and throw most of it away when the question changes. A teacher may build an entire interactive world for one class because those particular students are stuck on those particular ideas. A small company may create internal software whose assumptions match the company instead of spending two years teaching the company to behave like Salesforce. A family may have tools built around how that family schedules, learns, travels, budgets and remembers things, with exactly zero concern for whether the addressable market justifies Series A.

Some of these systems may serve a thousand people. Some ten. Some one. That used to sound economically absurd. It may become normal. This changes the human role in a way the automation story tends to miss. The future does not have to be:

> humans build → AI builds → humans watch.

We may remain intensely involved precisely because building becomes more interesting when the distance between imagining something and making it real collapses. I do not build only because the machine cannot. I build because I want the thing to exist.

The human contribution moves upward: choosing the strange problem, forming a taste for what good looks like, combining ideas that normally live in separate professions, seeing the result and saying *No, that is not it*, then pushing somewhere neither the original prompt nor the original system anticipated.

This is the abstraction ladder reaching economics. Implementation becomes another building block, and people who could not previously afford it may inherit a way to act. The cost of writing code is only part of the bill, though. A tool that handles a family's calendar can fail differently from one that controls a hospital. Maintenance, security, access to data and somebody capable of noticing a dangerous mistake still have to be paid for. A cheap first version is not yet cheap independence.

Even within those limits, I find this more interesting than guarding the last task the machine cannot perform. A person may be able to instantiate **far more of what she can imagine**. That is a much more attractive future than becoming the residual labor category in an automation spreadsheet. It also leaves her with a problem the spreadsheet was never designed to answer: which of those possibilities deserves her attention?

## Learning at the Speed of Curiosity

There is another kind of capacity that may change even faster: learning. Expertise is expensive partly because knowledge has difficult interfaces. Some of the effort produces depth: working through a proof teaches you something a summary cannot. Some merely keeps you from finding the proof. That second kind has killed an enormous amount of curiosity before depth had a chance to happen.

AI changes that bargain. I can ask a stupid question immediately, then a more sophisticated stupid question. Ask for the intuition, then the mathematics, then the objection, then the historical argument, then why the proof needs that assumption. I can have one field explain another, and move through mechanism design, philosophy of science, biology, constitutional theory and compiler construction at a speed that would previously have required several lives—or at least several abandoned PhDs.

The map has become cheap, and the trap that comes with it is the one Layer 4 had to learn to notice: fluency arrives before scars, and a person can acquire the vocabulary of five fields and mistake fluent traversal for mastery.

We need not restore the friction artificially. We can explore broadly and descend selectively. Use AI to cross fields cheaply, test curiosity and decide what deserves more attention. Then, when something matters, go down. If the argument depends on an equation, derive it; if it depends on a system working, build enough of it to find out where it breaks. Read the primary paper and talk to somebody who actually does the work. Let reality make the lesson expensive again.

This is System 3 applied to learning. AI gives us extraordinary access to synthesis; System 3 reminds us that synthesis and justified knowledge are not the same thing.

That trade may change what an educated human looks like. The twentieth-century ideal often rewarded specialization: know one vertical deeply enough that people in neighboring verticals stop understanding you. The AI-assisted human may become more T-shaped, π-shaped, octopus-shaped—choose your consulting diagram. Broader, faster at entering unfamiliar domains, more willing to combine ideas that institutional boundaries kept apart, while still going deep where the stakes or fascination justify it. Expertise is not obsolete in that world, only more deliberate.

And there is a creative consequence. A machine-learning scientist can learn enough philosophy to steal a useful structure. A philosopher can prototype the mechanism she has been describing. An artist can build software, and a local policymaker can examine a proposed intervention in a model before trying it in the world. Fields become more permeable. People become more dangerous in the nicest sense.

But crossing into a field and living there are different commitments. A useful afternoon with philosophy may open a question that takes ten years. Help with the technical difficulty makes that commitment more available; it does not supply the ten years. My attention can now reach more places than my life can follow. That is where the cheerful account of cheaper capability begins to become a less comfortable account of choice.

## The Second Descent

The capacity to act can scale faster than the capacity to want wisely. Humans still have status anxiety, tribal loyalty, love, jealousy, resentment, curiosity, generosity, fear, ambition, boredom and the ancient desire to prove that the neighboring group is composed mainly of idiots. None of these disappears because inference got cheaper. Giving us much more ability to execute whatever we want could be wonderful. It can also be a Ferrari engine attached to bicycle brakes.

Humans do not carry a stable reward function inside the skull. We infer, construct, revise and sometimes borrow our desires from the people and systems around us. We contradict ourselves. We want security and novelty, belonging and freedom, status and peace. We sometimes discover what we wanted only after getting the thing we thought we wanted.

My own opening question contains one of those borrowed desires. I want to know where an applied scientist will remain valuable. That is a reasonable question about earning a living. It becomes a much stranger one if I let the answer decide whether my life is valuable. The anxiety crosses that boundary so easily that it is worth stopping there.

### What Are Humans For?

Whenever automation becomes powerful, somebody asks what humans will be *for*.

I understand the question. If software writes the code, models perform the analysis, robots eventually move more of the physical world and agents coordinate the workflow, what is our economic role?

But there is something odd about the grammar. What are humans **for**?

A database is for storing information. A compiler is for translating programs. A recommender is for helping people find or decide among things. Asking what humans are for smuggles in the assumption that our legitimacy depends on having a remaining function in somebody else's architecture.

My children do not need comparative advantage to justify dinner.

Neither do I.

Economics does not disappear. People need income, housing, food, healthcare, status and access to resources. If automation breaks the mechanism by which income has traditionally been distributed, saying “human life has intrinsic value” will not pay the electricity bill. Political economy remains stubbornly material.

But a society that makes employment central to adult life bundles together two questions that AI may force us to separate: **How do people get resources?** and **What makes a life worth living?**

For a long time, a job has answered parts of both. It provides money, but also status, routine, social contact, identity, a reason to get dressed and a group of people with whom to complain about another group of people. Work is not one thing. It is a bundle. AI may unbundle it.

That makes “you will have more time for creativity” a rather incomplete answer to someone losing a livelihood. The freed hours and the gains from automation may belong to different people. A company can become more capable while its former employees lose the practical freedom to refuse bad work. There is no contradiction in that outcome. It is one reason the distribution of capacity belongs inside this philosophy, not in a footnote after the exciting part.

Perhaps some people work fewer hours. Perhaps new forms of work appear because human wants expand faster than automation satisfies them. Perhaps many of us continue working furiously, except the unit of ambition changes: one person can attempt things that used to require a department, and a small group can attempt things that used to require a corporation.

One possibility beyond employment is **more creation**—some economically useful, some absurd, some beautiful, some probably involving a bespoke dashboard nobody other than its creator can understand. Leisure, care and simply having less to do would also be perfectly respectable uses of the capacity.

Status competition will not politely resign either. It may migrate from intelligence and professional skill toward taste, reputation, physical scarcity, authenticity, human attention or something even more exhausting.

What I do know is that “find the tasks machines cannot do” is a depressing philosophy of human value. It turns civilization into a benchmark where we keep moving humans to the remaining columns after every model release.

If AI becomes better at poetry, we are not obligated to stop writing poems. If it becomes better at chess, humans do not lose permission to play chess. If it becomes better at writing software, we may write **more software**, because the things worth building are no longer restricted to those whose economics justify a software company.

I can still want to be an excellent scientist. The problem begins when I need science to remain difficult enough to require me before I can feel that my life has value. I do not want to make that depend on the next model release.

### The Human Is Not the Reward Function

Layer 4 named the ugly shortcut: alignment by editing the human. At the scale of one conversation, I want the ability to question the advice, inspect its evidence and bring in another perspective. At the scale of a life, I also need somewhere else to go. A patient assistant can preserve every detail of my history and still leave me dependent on the company that owns the memory, the model and the means of acting on its advice.

**Reflective agency** needs more than a well-behaved conversation. Can I carry my work and history elsewhere? Can another person understand enough of the arrangement to challenge it? Can I leave without losing the practical ability to do the things the assistant made possible? These are questions about how a service is built and owned, and about the alternatives available outside it.

Imagine that the bespoke family tool has become useful enough to hold the calendar, the children's learning history, the unfinished projects and the reasons behind years of small decisions. A button labeled *Export* may give me all the files. It may take months to make them useful elsewhere. Even if I disagree with the provider's new terms, I may be unable to afford the interruption. The tool gave the family more capacity and gave its owner more leverage over the family at the same time.

Trust chains and independent perspectives help. They make influence inspectable and give disagreement somewhere to enter. But a right to disagree inside one product is a thin kind of freedom if everything I need to act remains locked inside that product. I do not need to become a competent engineer, teacher and system administrator before I am allowed to benefit from help. I need alternatives that work, including other people and institutions I can turn to. Independence cannot mean doing everything alone; that would undo most of the civilization Chapter 5 was trying to explain.

System 3 can help answer *Why should I believe this?* and *Why does the system think I want this?* It cannot, by architecture alone, answer *What kind of life should be possible?*

That is politics, ethics, culture and philosophy. The annoying disciplines.

The limitation becomes clearer when we talk about optimization itself. I do not want to maximize time with my children. That sounds nice until the optimizer concludes I should never go to work, see a friend alone, read a book in peace or spend fifteen minutes doing absolutely nothing because the children are statistically nearby.

I do not want to maximize happiness if the cheapest route is a drug. I do not want to maximize productivity if the optimum is becoming an efficient ghost. I do not want to maximize longevity at every cost, wealth without purpose, social approval by becoming whatever the crowd currently rewards, or authenticity so aggressively that I become unbearable at dinner.

A good life contains goods that conflict: love and freedom, belonging and individuality, ambition and rest, truth and mercy, security and adventure, continuity and reinvention. The conflicts are not bugs waiting for a scalarization expert. Sometimes living is the process of negotiating them.

Take an ordinary evening. Time spent finishing an investigation is time I cannot spend with my children; abandoning the investigation may mean letting down people who depend on it. A better calendar might reveal a needless meeting tomorrow. It cannot make every conflict of this kind disappear. Even a perfectly predicted account of how I would feel about each choice would leave me having to choose, and another person's claim on me would still be there. Asking the assistant to settle everything would give it authority over the trade-off, not remove the trade-off.

This is why the human should not sit at Layer 4 merely as the source of a reward signal for the machine. The human is inside the process by which the objective is continuously reconsidered. AI can participate in that process without owning it. It can show me possibilities I did not know existed, teach me enough of a field to make a different choice imaginable, build prototypes of several futures and lower the cost of exploring a life before I commit to living it.

Perhaps that is one of the deepest meanings of cheaper capacity: more possibilities become **thinkable enough to try**. Or we may use it to watch fourteen hours of personalized short video generated specifically around whatever keeps us watching. The second descent can be helped by the system that made the first one possible. It cannot be handed over to it without also handing over some authorship of the life being considered.

And no amount of reflection will produce a life that everybody else agrees is the right one. My commitments involve other people, who have commitments of their own. Once our new capacity lets us act on them, the question grows beyond what any one of us wants.

## The Ideology Vortex

A machine may help me make sense of my commitments and help my neighbor defend commitments I find appalling. It may do both competently. We are accustomed to treating disagreement as a failure of understanding, so it is tempting to imagine that enough intelligence will eventually clear it up. But consider the material it has to work with.

There is a story we like to tell about intellectual history because stories prefer arrows.

First there was the premodern world: religion, tradition, inherited authority, myth. Then modernity arrived with reason, science, universalism, institutions and progress. Then postmodernism arrived carrying a small hammer and began tapping on every universal claim to see what was hiding inside it: language, context, power, contingency, who got to define the categories in the first place. Then, presumably, something comes after.

The problem with this story is that nobody informed actual humans. We did not uninstall the previous operating system. A person can demand randomized evidence for a medical claim, ask her mother for a blessing before a major decision, read a horoscope for entertainment, manage a team using dashboards, believe deeply in national mythology, quote a postmodern philosopher about constructed categories and then become furious because somebody used the wrong definition of a sandwich.

Entire societies work this way. Semiconductor fabs coexist with ancient identities. Bayesian inference coexists with rumor. Universities teach critical theory while their admissions systems produce precise numerical rankings. A company can run sophisticated causal experiments in the morning and make a major organizational decision in the afternoon because one senior person “has a feeling.”

I call this the **ideology vortex**. Not because every worldview is equally true. They are not. Reality remains annoyingly capable of rejecting bad engineering regardless of how socially constructed the bridge feels on the way down.

These labels compress vast, internally divided traditions, not just successive historical periods. I am using them to notice how several modes of knowing and valuing operate at once. Inherited traditions carry identity, ritual and forms of belonging that rational administration can underestimate. Modern science gives us extraordinary machinery for verification. Critique reminds us that institutions and categories are not neutral merely because somebody printed them in a table. None of us lives entirely inside one of these descriptions.

Each mode sees something the others can miss. Each can also become ridiculous when asked to do every job.

Science is extraordinarily good at questions reality can adjudicate. It is less good at deciding which trade-offs a society should consider legitimate. Tradition can preserve hard-won social knowledge, and preserve injustice with the same impressive durability. Markets coordinate preferences and information, but prices do not encode every value we care about. Democratic institutions create legitimacy through participation and contest, but anyone who has watched a parliament knows participation and wisdom are not synonyms. Permanent critique can expose hidden assumptions until it becomes incapable of committing to anything except the superiority of critique.

Humans switch among these modes without waiting for permission from philosophy. AI enters *that* world—not the clean one in which everybody has a coherent utility function, a shared epistemology and a calendar invitation for the social contract.

Give everyone better information and surely the disagreements shrink.

Some will. Others will get better lawyers.

A powerful model can help a scientist interrogate evidence. It can also help a conspiracy theorist construct a more coherent conspiracy. It can make propaganda cheaper, criticism sharper, religious interpretation richer, policy analysis more sophisticated and advertising more personal.

More intelligence does not guarantee one worldview. It increases the capacity available to worldviews. And AI introduces a second reason the vortex matters: the technology itself is strangely compatible with ambiguity.

I have a sentence that gets me into trouble: **Gradient descent is the answer to Derrida.**

This is deliberately unfair to Derrida and possibly to gradient descent. I do not mean that an optimizer disproved postmodern philosophy. It would be a remarkable conference paper if it had. I mean something narrower.

In *Signature Event Context*, Derrida challenges the idea that we could finally specify a context completely enough to close interpretation. A sentence can be repeated elsewhere, by someone else, under circumstances its author did not control. This does not make communication impossible. It makes the dream of securing meaning once and for all a much more demanding proposition than it first appears.

An engineer might hear a practical obstacle in that argument: how do we build reliable machinery out of language if the specification can always acquire another reading? We found one response by building machines that operate inside the mess.

Large language models do not begin by fixing every word to an eternal definition. They learn from use, relation, context and enormous numbers of imperfect examples. Optimization pressures the system toward behavior that works often enough under the training and evaluation environment. Meaning remains fuzzy at the edges.

The product ships anyway. Gradient descent did not defeat ambiguity. **It made ambiguity computationally useful.**

Then, immediately, we rediscover why modernity existed. A model that can move beautifully through fuzzy language can still hallucinate a citation, miscalculate a number or confidently tell you that a camel lives in Croatia. System 3 brings verification back through another door.

There is a further limit. A model can learn how an institution uses the word *family* well enough to fill in a form. That does not establish who should qualify for membership or whose relationships the form ought to recognize. Correctly reproducing an institution's categories may be useful work; it may also reproduce the exact exclusion someone is trying to challenge. Verification can establish whether the form was filled in correctly. It cannot make the rule legitimate merely by checking it more carefully.

This is why the ideology vortex is not a bug we eventually fix by choosing the winning epistemology. We need different modes for different jobs, and ways to contest the boundary between them. Some claims deserve hard empirical tests. Some institutions need legitimate contest over the ends those tests serve. Some identities and commitments are constructed without therefore being fake.

The childish response to contingency is to pretend our constructions are eternal. The adolescent response is to discover they are constructed and conclude that nothing deserves commitment. There is another possibility. **Construct them knowingly.**

Build institutions while remembering that institutions can be rebuilt. Love people without needing a theorem that proves love is the globally optimal allocation of Tuesday evening. Choose a project, a city, a profession, a community, a way of living—and retain enough humility to revise when experience pushes back. Contingency does not make the consequences of a commitment imaginary. Other people may arrange their lives around it, and revision may be something I owe them an explanation for rather than something I do because a new option appeared.

That is very close to the architecture we have been building for agents throughout this book. System 3 was never really about making machines certain. It was about making them capable of acting under uncertainty while remaining answerable to evidence. A life can do something similar.

But my willingness to revise is only part of the arrangement. Other people must be able to challenge what I build, especially when they have to live with it. Cheaper capacity gives more people a chance to construct their own answers. It also gives each of us more ways to impose an answer on somebody else.

## Capacity Over Power

Humans often seek power because power is how we gain capacity. You need a large organization to build the thing, so you try to control the organization. You need capital, so you compete for the institution that allocates it. You need media distribution, so you seek influence over the channel. You need permission from the bureaucracy because the bureaucracy is where the machinery lives.

Power is not reducible to capacity, of course. People also want power because humans are mammals with excellent branding. But where getting something done requires controlling the people who can do it, cheaper capability offers another possibility. We have already seen it in the strange little projects that no longer need to become companies. It becomes more interesting when people disagree about what to build.

Consider a small community whose activities do not fit its scheduling software. Some members work shifts, some depend on accessible transport, and several groups share one room. The software offers recurring bookings at fixed times. That works beautifully for the members whose lives recur at fixed times. The others exchange messages and ask for exceptions until somebody decides they are the difficult members.

If changing the software requires winning a vendor's roadmap argument, the community has to organize around whatever the vendor finds economical. Imagine instead that it can afford to build and maintain a small tool of its own. Members could enter changing availability and ask it to show possible schedules. They could try a rotation that gives the same group different evenings across a month, or reserve times that work with the accessible transport. The weird community with eleven members could have software optimized for all eleven of them and no plan whatsoever for customer acquisition.

This would let them discover something the old arrangement concealed. Some of their disagreement was about the default imposed by the software. Once the default can change, a member who seemed unreasonable may have a perfectly manageable constraint. A better tool can reduce the amount of pleading required to have that constraint recognized.

It will also expose disagreements the tool cannot dissolve. Suppose two groups both want seven on Tuesday. One proposes allocating the room to whichever group brings the most people. The other is small partly because its members have fewer times at which they can attend. A system that maximizes attendance can produce a very well-evidenced reason to keep excluding them. The figures may be correct. What is in dispute is the rule giving those figures authority.

The community might guarantee each group some access, then use attendance to allocate the remaining time. Or it might rotate the popular slot. The model could show who would lose out under each arrangement and help discover options nobody had considered. That would be useful. The members would still have to settle a rule, and those disadvantaged by it would need a way to challenge it. More capable analysis makes the choice better informed; it does not confer the right to make it.

Another community could choose a different arrangement without either one having to prove that its workflow should become the universal product. Within each community, however, the people sharing a resource still need rules for living with one another. Cheap software can remove the vendor's veto. It cannot give every group the same room at seven on Tuesday.

This is what **capacity over power** means to me at its best: increase the fraction of human possibility that does not require dominating somebody else, winning a centralized allocation contest or persuading the entire world to adopt one solution.

The ability to act can itself be called power. I have no objection to the vocabulary; I care about what happens to other people's choices. Giving the community a tool it can change expands its options. Giving its chair a system that everyone must use on terms only the chair can revise expands the chair's authority. The same technical capacity can do either.

Capacity over power is an ethical direction, not a forecast about whatever happens when models get stronger. It favors using AI to sustain **more than one good way of living**, while keeping the consequences of those lives open to challenge by the people who bear them.

This is where Elinor Ostrom's work on commons feels relevant. The interesting cases were rarely captured by the lazy binary of “the state manages it” or “the market manages it.” Communities could develop rules for using a shared resource, monitor one another, resolve disputes and adapt the arrangement to local conditions. In larger systems, these activities could be organized across several levels. The possibility depended on institutional conditions; calling something a community did not make cooperation happen.

Our room is a small version of that problem. The bookings need to be visible, the rules understandable, and there has to be some response when a group repeatedly keeps the room beyond its allotted time. Generating the schedule is one activity inside this arrangement. Helping members understand and revise the arrangement is another. A system that makes the second activity affordable may matter more than one that finds a slightly better schedule under rules nobody can question.

AI could increase our **governance capacity** by making some of this work less expensive. A proposed rule can be explored under different assumptions; members can inspect its likely consequences and compare them with what actually happens. Records can preserve why an exception was made, so the next committee does not spend three meetings rediscovering accessible transport. The same tools can create bureaucratic nightmares at machine speed, which is why I am not putting “AI fixes government” on a T-shirt.

Greater governance capacity may make more polycentric arrangements practical: several centers of decision, responsible for different problems, with ways to coordinate where their consequences overlap. This does not mean every small group gets a private sovereign universe. A community can exclude people, and a local majority can dominate a member just as a large institution can. Shared rights and access to a wider avenue of appeal may be what make local freedom tolerable for the person who keeps losing the vote.

There is also the family tool's dependency problem again. If only one volunteer understands the scheduling system, replacing the vendor may merely have changed whom everybody must keep happy. The community needs a way to keep its records, get help from someone else and continue operating when that volunteer leaves. Cheap code is useful; institutions that can survive their indispensable person are useful in a different way.

Where such conditions hold, sometimes the humane answer to disagreement is enough capacity for both sides to stop fighting over the same button. Each can have a tool that fits its work. Where the consequences remain shared, the argument has to continue. Climate, war, public health, rights, land and infrastructure remain collective whether we enjoy meetings or not. Those domains need legitimate institutions, not personalized realities.

This is also where the optimistic story should be willing to lose. If people can generate more software but cannot refuse the provider's terms, if leaving becomes harder, or if the people affected by a new system have less say in its rules, I would not call that a success for capacity over power. A great deal more may be getting done. The power may simply have moved somewhere less visible.

But the boundary can move. The most hopeful version of the AI future is not a world where the machine knows the correct answer to human life. It is a world where more people have **room**.

Room to get the map of a field quickly, then spend a year on the part that matters. Room for a small community to construct things around its actual needs, and for someone inside it to disagree. Room to try the strange art nobody would have funded. Room to be less economically useful without becoming less human.

As some forms of capacity get cheaper, more of human life can become **experimental before it becomes irreversible**.

You can prototype the tool before building the company, or learn enough of a field to make choosing a degree less of a leap in the dark. A community can explore a proposed rule and try a bounded version before making everyone live under it. The trial will not tell them everything. A simulation can miss the behavior a policy creates, and even a small trial can impose costs on people who did not volunteer to be an experiment. The extra room matters when it lets us learn with less at stake, not when it becomes an excuse to ignore who is taking the risk.

An infinite menu can become its own prison. I cannot test every version of a life before living one, and keeping all my options open may close the possibility of being somebody others can depend on. Some understanding becomes available only after commitment. Cheaper capacity can help me approach that point with more experience and fewer avoidable constraints; it cannot abolish the point. I still want **more room to discover which commitments deserve to become expensive**.

## The Door After System 3

The scientist at the beginning of this chapter still has a job to think about. I have not reached the end with a proof that my profession is safe. I do have a better reason to work on these systems than defending the scarcity of what I know. I want more people to be able to investigate a question, build something they need and challenge an arrangement they previously had to accept. That is work I can choose while it needs doing. It does not have to establish what humans will be for forever.

System 3 gives us machinery for learning from what happens: evidence that can travel, claims that can be challenged, institutions that can remember why they changed. Double Descent Life asks what we want to make possible with that machinery. Its second descent begins wherever a successful system leaves us with a choice it cannot justify on our behalf.

I do not know whether the result will be utopian, dystopian or, much more likely, an infuriating mixture in which somebody cures a disease with an AI-designed experiment while another person uses the same generation of models to produce three million personalized ads for a shoe nobody needs.

I want to know who actually gets that room. The question reaches from my anxiety about a job to the choices a small community can make, and from there into institutions none of us can simply build our way out of. That is a much larger book. This one has one argument left. It cannot be made with another architecture diagram.

It requires an octopus, a romance, two pills and, unfortunately, taxes.

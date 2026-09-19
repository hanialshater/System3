# Chapter 12: After Capacity

*A Glimpse of Double Descent Life*

In October 1947, George Dantzig went to John von Neumann with his emerging ideas about linear programming. He had spent the summer inventing a way to solve such problems, the method later called simplex, and had come to Princeton to ask for a better one. He began explaining in detail. Von Neumann told him to get to the point. Dantzig compressed a summer's work into a minute or two, and von Neumann stood up and lectured for over an hour on a theory Dantzig had never heard of. As Dantzig remembered it, von Neumann seemed to be constructing the theory while he spoke. He called it duality: one formulation searches for the best solution; another can establish how good any solution could possibly be. He connected it to his work with Oskar Morgenstern on games. Dantzig sat there stunned. His summer had not been wasted. It had a side he had not known was there.[1]

I usually read stories like these from a safe distance. Extraordinary people did extraordinary things. Then I return to an afternoon in which locating the correct spreadsheet is a substantial intellectual achievement.

Imagine having help like that with a question of your own. Someone can follow it, recognize mathematics you have never encountered and help you see why it applies. You can ask where the connection comes from. You can work through a small example, change an assumption, discover that your original question was concealing a better one. When the investigation needs a program, you can build it. When the result looks wrong, you can stay with it.

What would you attempt?

Some questions stall because I know too little to see where I could begin. Others reach a point at which continuing would require another specialty, another collaborator, another year I cannot account for. I admire the question, save a paper and get on with the things I know how to do. After enough years, those decisions begin to resemble a personality.

Access to extraordinary intellectual capacity could change that. An interest might survive long enough to grow into an ability; a connection between fields might be mine to investigate. I might discover that the life I assembled around what I could already do had left quite a lot out.

Some of this is already ordinary. I can ask a stupid question immediately, then a more sophisticated stupid question. Ask for the intuition, then the mathematics, then the objection, then why the proof needs that assumption. I can have one field explain another and move through mechanism design, philosophy of science and compiler construction in an afternoon that would previously have required several abandoned PhDs. The map has become cheap. I can get far enough into a subject to discover a question worth staying with. Fields become more permeable. People become more dangerous, in the nicest sense.

## The Curve

The title is stolen from machine learning, and the theft is deliberate.

In the curve described by Belkin and colleagues, test error falls as a model gains capacity, rises near the point where it can fit its training data exactly, then falls again as capacity grows further.[2] The familiar lesson was to limit capacity to avoid overfitting. The second descent complicated that lesson. More capacity supplied more candidates; how the training procedure selected among them mattered.

I am borrowing the shape. Intellectual history does not obey a theorem about neural networks.

Much of the modern world was built by reducing problems to what we could handle: engineer the complexity down, design the solution in advance, build one thing and reuse it. That is the first descent in the analogy. Chapter 5 followed how civilization accumulated capacity in institutions, often learning what arrangements it needed through failure. The spike in the middle I read, loosely, as a predicament the postmodern critics explored: more and more accounts can be made to fit the same facts, and none is obviously privileged. The critics were right about the predicament. We become better at questioning the arrangements we inhabit without necessarily gaining the means to change them.

Double Descent Life is the wager that cheap capacity opens another route: an attempt whose outcome is not already contained in the argument. Where scarcity made us engineer complexity away, we can afford to investigate it. Where it made us design arrangements in advance, they can develop through use and revision. Where it made us reuse one solution for everyone, we can assemble software, expertise and organization around the question in front of us. Complexity, emergence, capacity.

Not all capacity. We still have one planet, finite land and energy, and twenty-four hours in a day. Bodies remain bodies. Politics does not evaporate because a model can write Python. Scarcity is not going to receive a polite email from OpenAI and retire.

The earlier chapters followed engineering failures until the machinery assembled around them became recognizable as science. Double Descent Life asks what people could attempt if they could assemble that capacity around questions of their own.

## Owning the Frontier

LLM-as-a-judge arrived in my team looking like a threat.

For years, a large part of what made an applied scientist valuable was that she could train a model and run an evaluation somebody would believe. Those were scarce skills, and a job accumulates around scarce skills the way a city accumulates around a river. Then anyone could download a model, and other models could evaluate its outputs at a scale no human team could match. It is hard to watch the river move without wondering what the city was for.

In a project recommending complementary fashion items, our LLM judge agreed with the fashion experts about what made a good recommendation. We had a plausible account of quality and an instrument that could apply it at scale. Then the business experiment came back. The metrics went down.

Perhaps the recommendations diverted attention from something customers would otherwise have bought. Perhaps experts preferred combinations that customers admired without wanting to purchase. Price and popularity could be doing work we had attributed to quality. Agreement with the experts did not distinguish these explanations.

We could change the widget or adjust the rubric and try again. But learning why it failed required an experiment that separated the possibilities. Which comparison would justify changing the judge, the experience or our account of what a good recommendation was?

Scarcity rations the distinctions a team can afford to investigate. The judge changed the ration. We could examine far more experiences than our experts would ever review and ask questions that had previously cost too much to ask. The instrument did not explain the failure. It made an old question urgent: what did its measurement mean? A million judgments overnight is a million more things that look like evidence.

A strong applied scientist brings a working map of the frontier. She knows which exciting idea has failed three times under another name, which result quietly changed what we could build last month, and which neighboring field has a method that might explain our disappointing experiment. She can turn that knowledge into an investigation the organization has reason to trust.

Chapter 5 followed the larger society that makes this possible. A scientist inside a company is connected to arguments, discoveries and failures happening outside it. Without that connection, the company keeps approaching unfamiliar problems with its familiar machinery.

I think of this as owning the frontier. Someone takes responsibility for noticing where the possibilities have changed and finding out what the organization can actually do with them.

Training and evaluation were never the whole purpose of the job. They were the expensive part of it, and expensive is easy to mistake for essential.

There is useful work for me in that change. But I would say that. I cannot spend eleven chapters proposing more capable agents and then reserve the interesting questions for myself whenever the argument reaches my salary. “The role moves upward” describes where I might contribute next. It does not establish a permanent boundary around human employment.

The same capacity that makes my profession less secure puts more of the frontier within reach. I can worry about what it will replace and still be impatient to find out what I can do with it.

## Bespoke Comes Back

There is a point in an ambitious project when I begin mentally hiring the people it would require. Somebody who knows this part, somebody who has spent years on that part, somebody to keep the parts from drifting into separate projects. Before long I have a budget, a staffing problem and a reason to postpone the idea.

Sixteen agents building a C compiler moves that point.

Nicholas Carlini's experiment took roughly two weeks, nearly two thousand sessions and about twenty thousand dollars in API costs, and produced a compiler that could build a bootable Linux kernel, with the dependencies and limitations his account describes.[3] Chapter 5 examined the organization behind the achievement. Here I am interested in what its price does to our imagination.

Software has often required a bargain. One team builds a product for many customers; each customer rearranges some of its work to fit. This was an enormous improvement over everyone commissioning their own system. It also gave us organizations whose procedures preserve the decisions of a dropdown menu designed ten years ago.

Imagine a mathematician assembling a workshop around one conjecture. It generates examples, searches for counterexamples, draws the structures she is trying to understand and keeps track of why promising approaches failed. When an observation suggests a lemma, she can attempt a formal proof. A missing piece of software is part of the day's investigation instead of a separate project waiting for a collaborator.

The workshop changes as she learns. A picture suggests a different representation. The new representation makes a search possible. The search returns an awkward case, and the awkward case is more interesting than the conjecture she began with. She builds the next instrument around it.

That environment might be useful to one person for eighteen months. It could still be worth building. Its reason to exist is the investigation, not the market.

The recommendation project changes under this possibility too. A row of products is a familiar, reusable unit of customer experience. One shopper needs help comparing two coats; another wants to know what she already owns that would work with a dress. The team could construct and investigate different experiences around those needs, instead of spending another quarter rearranging the same row. The form of the product becomes something we can question by making it.

Maintenance, security and access to data remain part of the work. A cheap first version is not yet a system people can depend on. But these are reasons to build better tools for sustaining what we create. They do not restore the old economics by decree.

A weekend can be the beginning of an undertaking that changes the next ten years of a life. That interests me considerably more than using the weekend to produce the same presentation faster.

## Anyone Could Do That

“Anyone could do that” is a peculiar objection to something useful.

If building my tool took six months of specialized work, people might be impressed. If an agent helped me build it in an afternoon, the same tool impresses less. The problem is still solved. What changed is how much the solution says about me.

There are practical reasons to care. A scarce ability gives its owner bargaining power, and bargaining power matters when rent is due. But we carry that test well beyond bargaining. We use difficulty to decide which achievements deserve admiration and which ambitions are serious.

I might want the tool to exist and want to be the person whose unusual ability made it possible. An improvement that satisfies the first desire can injure the second. It is embarrassing how easily I can describe this as a decline in standards.

Institutions reuse too, and what they reuse is trust. If a project requires funding, a team or institutional access, I need people to believe I can do it. They cannot examine everything I know, so they look for signals: a qualification, a previous employer, a recognizable achievement, somebody credible willing to vouch for me. I have depended on these ways of deciding whom to trust myself.

Then I learn what those signs look like and arrange part of my life around acquiring them.

A young researcher is choosing a question. She has an interest of her own, but she also needs funding and eventually a job. She studies the work that gets published and the people who get hired. A proposal shaped like those successes is easier for a committee to recognize. If she follows that path and succeeds, her career joins the evidence the next applicant studies.

Now the image has a budget. It directs money, equipment and years of attention toward work that resembles it. The resulting papers and careers make the image look like a description of how science naturally proceeds. Questions that do not fit may never receive enough work to show what they could have been. Each person can be making a reasonable decision; nobody has to decide that imitation should run the institution.

That is how capacity and validation end up entangled. I need recognition to obtain the means; pursuing recognition changes what I want to do with them. I wanted to investigate a question and have become very good at being the sort of person who might be allowed to investigate it.

Cheap capacity loosens the entanglement at one point. If I can do substantial work before winning recognition, other people have an attempt to examine, and I have experience with which to question my own ambition. The project might matter more to me than I expected, or much less, once I am actually doing it.

I can find out whether I care about the question when it is no longer a particularly good way to look impressive.

## The Ideology Vortex

I can understand whose interests an institution serves, which assumptions it smuggles in and why its claim to universality should make me suspicious. I can understand all of that and still need its permission on Monday morning.

Intellectual history is often told with arrows: premodern tradition and inherited authority, then modern reason, science and institutions, then postmodernism tapping on every universal claim with a small hammer to see what was hiding inside it. After that, presumably, something else.

Nobody informed actual humans. We did not uninstall the previous operating system. A person can demand randomized evidence for a medical claim, ask her mother for a blessing before a major decision, manage a team using dashboards, quote a philosopher about constructed categories and then become furious because somebody used the wrong definition of a sandwich. A company can run sophisticated causal experiments in the morning and make a major organizational decision in the afternoon because one senior person “has a feeling.”

These commitments can be sincere. Tradition gives someone a place in a history; science gives her ways to investigate; criticism helps her notice what both have excluded. We draw on them unevenly. None supplies an uncontested place from which to settle the claims of the others. AI enters that world, not the clean one in which everybody has a coherent utility function, a shared epistemology and a calendar invitation for the social contract.

Give everyone better information and surely the disagreements shrink. Some will. Others will get better lawyers.

Decisions still get made. Institutions determine which qualifications count. Political movements offer belonging and explanations. A leader who supplies a convincing story can acquire more authority than someone who understands the problem. Recognizing how the story works may do little for the person who still depends on its believers.

Even criticism can acquire a comfortable institutional role, provided it never changes what happens next. A dashboard stands in as evidence that an organization is scientific. A consultation stands in as evidence that people have a say. Careers and budgets accumulate around these representations until altering them threatens something quite real.

This is what I mean by the ideology vortex: inherited belief, reason, criticism, representation and power keep pulling us around the same disputes. The argument changes while the practical dependence survives.

An alternative has to be possible somewhere. Someone needs the knowledge, time and means to make an attempt whose outcome is not already contained in the discussion. Otherwise, exposing the arrangement leaves us with an exposed arrangement that we still have to use.

There is an oddity in the machinery making this conceivable. It has learned from the same accumulated language in which we argue about the impossibility of getting outside our descriptions.

I have a sentence that gets me into trouble: gradient descent is the answer to Derrida.

This is deliberately unfair to Derrida and possibly to gradient descent. In *Signature Event Context*, Derrida challenges the idea that context could be specified completely enough to close interpretation. A sentence can be repeated elsewhere, by someone else, under circumstances its author did not control. An engineer hears a practical difficulty: how do we build reliable machinery from language if the specification can always acquire another reading?[4]

Large language models operate inside that difficulty. They learn from use, relation, context and enormous numbers of imperfect examples. Optimization pushes them toward behavior that works under the conditions in which they are trained and evaluated. Nobody had to settle the meaning of every word first.

Meaning remains fuzzy at the edges. The product ships anyway.

Gradient descent did not defeat ambiguity. It made ambiguity computationally useful. The language carrying our disagreements can also help us construct things through which we learn something new.

Then, immediately, we rediscover why modernity existed. A model that can move beautifully through fuzzy language can still hallucinate a citation, miscalculate a number or confidently tell you that camels are native to Croatia.

The compiler has to compile. Our recommendation experiment interrupted an account of quality that the experts and the model both found convincing. We had a reason to revise it, and more capacity could help us investigate what had gone wrong.

An eloquent machine left talking to itself could keep us in the vortex indefinitely, with better illustrations. That is why the earlier chapters insisted on tests, independent evidence and work somebody else can inspect.

Theories and traditions remain available to think with. But criticism leaves a practical question: once you have seen through an arrangement, how do you build one you can commit to?

The childish response to contingency is to pretend our constructions are eternal. The adolescent response is to discover they are constructed and conclude that nothing deserves commitment. There is another possibility. We can construct them knowingly. Build institutions while remembering that institutions can be rebuilt, and that people will arrange their lives around the promises we make. We owe those people an account of what changed and a say in what happens next. Love people without needing a theorem that proves love is the globally optimal allocation of Tuesday evening.

Elinor Ostrom studied people who had already begun.

## Capacity Over Power

An influential answer to the tragedy of the commons offered two routes: state control or private ownership. Meanwhile, people were managing shared forests, pastures and irrigation systems through arrangements that did not fit that prescription. Some had been doing it for centuries. Ostrom's *Governing the Commons* examined cases from Switzerland, Japan, Spain and the Philippines. Resource users had made rules suited to their circumstances, monitored use, imposed graduated sanctions and developed ways to settle disputes and revise agreements.[5]

If those were the only two answers, what were these people doing?

She drew general principles from the cases and held the principles answerable to further cases. But she began with the arrangements people actually used, rather than assuming that one institutional prescription should fit them all. Nobody had to win the argument about the right social order before the irrigators could agree on a schedule.

That is the turn out of the vortex I am interested in. You can take the criticism seriously, decline the grand narrative and still build something worth committing to. Start with the actual problem, draw on what others have learned and stay answerable to what happens. Calling something a community does not make this work. The arrangements that lasted had conditions, including ways for participants to help shape the rules under which they lived.

I find this more encouraging than another theory of the good society. People were participating in the construction of their common life. Those irrigators did not lack knowledge of their own valley. What might they have done with ready access to the experience of a hundred other valleys, and tools for exploring a proposed rule before the next dry season? Now imagine being able to assemble serious intellectual help around a problem of your own: the research, the models, the alternative arrangements, the software to make one work. A group could bring its experience of the problem and acquire much more of the expertise needed to investigate it. A missing specialty would no longer have to end the attempt.

Take something smaller than a watershed.

A small community's activities do not fit its scheduling software. Some members work shifts, some depend on accessible transport, and several groups share one room. The software offers recurring bookings at fixed times, which works beautifully for members whose lives recur at fixed times. The others exchange messages and ask for exceptions until somebody decides they are the difficult members.

Changing the software requires persuading a vendor that eleven people with peculiar scheduling needs are worth its attention. They are unlikely to win that argument. Some problems that looked like power problems may turn out to have been capacity problems wearing a suit.

Suppose instead that they can afford to build and maintain a small tool of their own. Members could enter changing availability and explore possible schedules. They could try a rotation that gives the same group different evenings across a month, or reserve times that work with the accessible transport. The weird community with eleven members could have software built around all eleven of them and no plan whatsoever for customer acquisition.

They can discover and revise the arrangement by using the tool and arguing about the results. Some of their disagreement may turn out to have been about the old software's default. A member who seemed unreasonable may have a perfectly manageable constraint. A better tool can reduce the amount of pleading required to have that constraint recognized.

Then two groups both want seven on Tuesday.

One proposes allocating the room to whichever group brings the most people. The other is small partly because its members have fewer times at which they can attend. A system that maximizes attendance can produce a very well-evidenced reason to keep excluding them. The figures may be correct. What is in dispute is the rule giving those figures authority.

The community might guarantee each group some access, then use attendance to allocate the remaining time. Or it might rotate the popular slot. The model could show who would lose out under each arrangement and help discover options nobody had considered. The members would still have to settle a rule, and those disadvantaged by it would need a way to challenge it. More capable analysis makes the choice better informed; it does not confer the right to make it.

Cheap software removed the vendor's veto. It did not produce a second room at seven on Tuesday.

Another community could choose differently without either one having to prove that its workflow should become the universal product. This is what capacity over power means to me at its best: increase the fraction of human possibility that does not require dominating somebody else, winning a centralized allocation contest or persuading the entire world to adopt one solution.

Humans often seek power because power is how we gain capacity. People also want power because humans are mammals with excellent branding.

The ability to act can itself be called power. I care about what happens to other people's choices. Giving the community a tool it can change expands its options. Giving its chair a system whose terms only the chair can revise expands the chair's authority. Capacity over power is an ethical direction, not a forecast about stronger models.

Helping members inspect and revise the arrangement may matter more than finding a slightly better schedule under rules nobody can question. It needs to survive the volunteer who built the tool. Its records should preserve why an exception was made, so the next committee does not spend three meetings rediscovering accessible transport. Members need ways to challenge the rules, including somewhere beyond the committee to turn when the committee is the problem. If more gets built while those freedoms shrink, power has simply moved somewhere less visible.

Where consequences remain shared, so do the decisions. Climate, public health, land and infrastructure still need legitimate institutions whether we enjoy meetings or not. A community does not acquire a private planet because it can generate its own software.

But where people retain the means to act, more differences can become opportunities to build differently. Some of the effort spent winning permission can go into the undertaking itself. Some can return to the rest of a life.

## The Second Descent

The capacity to act can scale faster than the capacity to want wisely.

Humans still have status anxiety, love, jealousy, curiosity and the ancient desire to prove that the neighboring group is composed mainly of idiots. Giving us much more ability to execute whatever we want could be wonderful. It can also be a Ferrari engine attached to bicycle brakes.

We infer, construct, revise and sometimes borrow our desires from the people and systems around us. We want security and novelty, belonging and freedom, status and peace. Sometimes we discover what we wanted only after getting the thing we thought we wanted.

Where will I remain valuable? My question about the applied scientist's role makes sense as a question about earning a living. It becomes a much stranger one if I let the answer decide whether my life is valuable.

### What Are Humans For?

Whenever automation becomes powerful, somebody asks what humans will be for.

There is something odd about the grammar. A database is for storing information. A compiler is for translating programs. Asking what humans are for smuggles in the assumption that our legitimacy depends on having a remaining function in somebody else's architecture.

My children do not need comparative advantage to justify dinner.

Neither do I.

A society that makes employment central to adult life bundles together two questions: How do people get resources? and What makes a life worth living? For a long time, a job has answered parts of both. It provides money, but also status, routine, social contact, identity, a reason to get dressed and a group of people with whom to complain about another group of people. Losing a job disturbs all of these at once.

“You will have more time for creativity” is a rather incomplete answer, especially when the freed hours and the gains from automation belong to different people. A company can become more capable while its former employees lose the practical freedom to refuse bad work. Saying “human life has intrinsic value” will not pay their electricity bills. The distribution of capacity belongs inside this philosophy, not in a footnote after the exciting part.

“Find the tasks machines cannot do” is a depressing philosophy of human value. It turns civilization into a benchmark where we keep moving humans to the remaining columns after every model release. If AI becomes better at poetry, we are not obligated to stop writing poems.

Leisure, care and simply having less to do would also be perfectly respectable uses of the capacity.

I can still want to be an excellent scientist. The problem begins when I need science to remain difficult enough to require me before I can feel that my life has value. I do not want to make that depend on the next model release.

Nor do I want to replace the obligation to have an impressive career with an obligation to produce important research on weekends. Someone who gains an evening with a friend has no obligation to spend it on a conjecture.

### The Human Is Not the Reward Function

Layer 4 named the ugly shortcut: alignment by editing the human. In a conversation, I want the ability to question the advice, inspect its evidence and bring in another perspective. Over a life, I also need somewhere else to go.

Imagine a bespoke family tool useful enough to hold the calendar, the children's learning history and the reasons behind years of small decisions. A button labeled Export may give me all the files and months of work to make them useful elsewhere. The tool gave the family more capacity and gave its owner more leverage over the family at the same time.

A right to disagree inside one product is a thin kind of freedom if everything I need to act remains locked inside it. I do not need to become a competent engineer, teacher and system administrator before I am allowed to benefit from help. I need alternatives that work, including other people and institutions I can turn to. Independence cannot mean doing everything alone; that would undo most of the civilization Chapter 5 was trying to explain.

System 3 can help answer *Why should I believe this?* and *Why does the system think I want this?* It cannot, by architecture alone, answer *What kind of life should be possible?* That is politics, ethics, culture and philosophy. The annoying disciplines.

I do not want to maximize time with my children. That sounds nice until the optimizer concludes I should never go to work, see a friend alone, read a book in peace or spend fifteen minutes doing absolutely nothing because the children are statistically nearby.

Nor productivity, if the optimum is becoming an efficient ghost. Nor authenticity so aggressive that I become unbearable at dinner.

A good life contains goods that conflict: love and freedom, ambition and rest, truth and mercy, security and adventure. Time spent finishing an investigation is time I cannot spend with my children. Abandoning it may let down people who depend on it. These conflicts are not bugs waiting for a scalarization expert. Asking the assistant to settle everything gives it authority over the trade-off. The trade-off remains.

The human should not sit at Layer 4 merely as the source of a reward signal for the machine. The human participates in the process by which the objective is reconsidered. That is not a competence I am reserving for us because machines cannot yet do it; a machine may come to understand my trade-offs better than I do. It is a matter of whose life it is.

AI can participate in that process without owning it. It can show me possibilities I did not know existed, teach me enough of a field to make a different choice imaginable, or help me try something before committing to it. Some desires will change through the experience. I may find the investigation worth finishing because of what I discover while doing it.

Or we may use the capacity to watch fourteen hours of personalized short video generated around whatever keeps us watching. If I let the system decide which desires deserve pursuing, I hand over some authorship of my life.

I can prototype a tool before building a company, or learn enough of a field to make choosing a degree less of a leap in the dark. A community can try a limited version of a rule before asking everyone to live under it. Those trials have consequences for other people too. The extra room matters when it lowers their cost of learning as well.

The future I want has more room in it.

Room to get the map of a field quickly, then spend a year on the part that matters. Room for a small community to construct things around its actual needs, and for someone inside it to disagree. Room to try the strange art nobody would have funded. Room to be less economically useful without becoming less human.

An infinite menu can become its own prison. I cannot test every version of a life before living one, and keeping all my options open may close the possibility of being somebody others can depend on. Some understanding becomes available only after commitment. Cheaper capacity can help me approach that point with more experience and fewer avoidable constraints; it cannot abolish the point.

I still want more room to discover which commitments deserve to become expensive.

## The Door After System 3

The scientist at the beginning of this chapter still has a job to think about. I have not reached the end with a proof that my profession is safe.

I do have a better reason to work on these systems than defending the scarcity of what I know. Dantzig's afternoon makes me want access to a mind that can help me see further. Ostrom makes me want to find out what people could construct together if they had that help.

Imagine an irrigation association with a weekend and a hundred agents. Some investigate how other communities have handled shortages. Others examine the water records, build models, look for failures in the proposed schedules or write the software through which members can inspect and change them. A question raised over the table becomes another investigation. The work can follow it.

Someone remembers why the apparently wasteful exception was introduced. Someone knows whose field goes dry first. Someone asks whether the people least able to attend the meeting have been counted at all. A model exposes a mistake in their account; their experience exposes a mistake in the model. They revise both.

By Sunday evening they might have an arrangement worth trying, a working tool and a way to find out where they were wrong. The next dry season will teach them things the weekend could not, but they would meet it with something they had helped build.

I have not run that weekend. A hundred agents is a picture, not a measured capability or a cost estimate.

Nobody at the table needs a Nobel Prize. They should not each need a thirty-year research career before they can draw on what that research made possible. They need access to the knowledge, enough capacity to work with it and people willing to take responsibility for the attempt.

A weekend could give a group the means to try an arrangement it had spent years petitioning somebody else to provide. A teacher could build an environment around the children she actually teaches. A question pursued after work could acquire the instruments of a serious investigation.

That is the work I want to do: put the machinery this book has described within reach of people who have something they want to try. If someone else can build the same thing, I might have a collaborator.

I would like some of that freedom myself. A year on a question that once seemed inaccessible. Enough astronomy to make an evening outside with my children different. An unfamiliar subject becoming a source of pleasure long after it has stopped being useful for anything I could put on a slide. Some of the hours recovered from asking permission could go into the work. Some could go into enjoying the life around it.

Dantzig brought a question and found that it had another side. I want more of us to have afternoons like that, and weekends in which we can do something about what we discover.

There is more to a person than the few abilities a career had room for. There may be more to our common life than the arrangements we could previously afford to build.

I would like us to find out how much more.

Who actually gets that freedom is a much larger book. This one has one argument left. It cannot be made with another architecture diagram. It requires an octopus, a romance, two pills and, unfortunately, taxes.

---

## Source Notes

1. George B. Dantzig, “Reminiscences about the origins of linear programming,” *Operations Research Letters* 1(2), 1982, pp. 43–48. The encounter is also discussed in Bernhard von Stengel, [“Zero-Sum Games and Linear Programming Duality”](https://arxiv.org/html/2205.11196v6). The opening describes Dantzig's recollection; it does not attribute a complete modern proof of LP duality to that conversation.
2. Mikhail Belkin, Daniel Hsu, Siyuan Ma and Soumik Mandal, [“Reconciling modern machine learning practice and the bias-variance trade-off”](https://arxiv.org/html/1812.11118v2), *PNAS* 116(32), 2019, pp. 15849–15854. In their random-feature experiments, the researchers explicitly selected the smallest-norm solution among those that fit the data; larger model classes allowed such solutions with smaller norms. Double Descent Life borrows the curve's shape as a philosophical analogy.
3. Nicholas Carlini, [“Building a C compiler with a team of parallel Claudes”](https://www.anthropic.com/engineering/building-c-compiler), February 5, 2026. The mathematical workshop, alternative recommendation experiences and community tool are prospective examples, not reported deployments.
4. Jacques Derrida, “Signature Event Context,” in *Limited Inc*, Northwestern University Press, 1988. The comparison with gradient descent is a philosophical provocation, not a claim that optimization refutes Derrida's argument.
5. Elinor Ostrom, *Governing the Commons: The Evolution of Institutions for Collective Action*, Cambridge University Press, 1990. See also Elinor Ostrom and Michael Cox, [“Moving beyond panaceas: a multi-tiered diagnostic approach for social-ecological analysis”](https://www.cambridge.org/core/journals/environmental-conservation/article/moving-beyond-panaceas-a-multitiered-diagnostic-approach-for-socialecological-analysis/F4870A21ED502BB7D9A1784CF2B9E100), *Environmental Conservation* 37(4), 2010, pp. 451–463. The connection to the ideology vortex is the author's philosophical reading of this work.

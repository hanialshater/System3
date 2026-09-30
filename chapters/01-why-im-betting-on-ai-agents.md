# Chapter 1: Why I’m Betting on AI Agents
*Or: How I Learned to Stop Micromanaging and Love Emergence*

![Simple building blocks, complex emergence](../book-design/curated/assets/art/a005.jpg)

*Simple building blocks, complex emergence*

We humans are obsessed with problem-solving. And what problem is more fascinating than life itself, this messy, miraculous phenomenon responsible for everything from the deepest ocean trenches to TikTok trends, mortgage-backed securities and people who voluntarily put pineapple on pizza?

Pineapple doesn’t belong. I will die on this hill.

Life produces coral reefs, immune systems, parasites, flowers, cancer and octopuses: eight-armed problem-solvers that extensively edit their own RNA, sense light through their skin and match the colors around them despite apparently color-blind eyes. It also produces creatures capable of spending twenty minutes arguing online about whether another creature is technically a fish. Human civilization adds philosophy, cathedrals, semiconductor fabs, global supply chains and airport lounges. Somehow, all of this became possible on a planet that began without a requirements document.

What fascinates me is how little of the result was specified in advance. No blueprint contains the exact location of every future branch of an oak tree. London contains an extraordinary amount of deliberate design, but nobody designed the whole thing. Nobody designed English and then accidentally forgot to make the spelling system sane. People built houses, opened shops, argued about roads and borrowed words from their neighbors. They were making decisions about the things in front of them, inside arrangements inherited from people who had been doing much the same.

And we get to build on what they left. A programmer does not need to understand transistor physics. I can use a compiler without reproducing the intellectual history that made it possible, which is fortunate because I was hoping to finish before lunch. Enough of the complexity underneath has been made reliable that I can spend my attention elsewhere. When something breaks, I may have to descend a few layers and discover how much I was taking for granted.

Agentic AI interests me as another place from which to begin. We have spent decades making more of our knowledge available to machines. Now we can give a system access to that knowledge, a problem, tools and time, and let it participate in deciding how the problem should be approached. Could I leave it with a hard problem and come back to progress I had not directed?

## The Rule-Based Exoskeleton

Machine learning was supposed to teach us something about this. Stop writing a rule for every case. Give the machine examples and a way to learn. Let it discover useful structure we cannot articulate. Pedro Domingos’s *The Master Algorithm* gave an ambitious name to the hope that learning could replace much of the programming we did by hand.

Then we went back to work. We trained a model, found an edge case, added a rule, found another edge case, added another rule, and eventually built something that was theoretically learned end-to-end except for the large rule-based exoskeleton holding it upright. Sometimes this was entirely reasonable. Production systems are ugly. Deadlines exist. Regulators are less impressed by emergence than researchers are, and nobody gets promoted for saying, “the model will probably figure out chargebacks eventually.”

I have spent a respectable amount of my career producing that surrounding process. Some of it tells the system what matters: the examples we label, the constraints we enforce, the failures we refuse to tolerate. Some encodes a solution we already understand. The distinction gets uncomfortable when we ask the machine to discover something better and it finds a route that makes our carefully designed process unnecessary. We wanted discovery. We had also grown rather attached to the diagram.

Engineering often makes a problem manageable by removing possibilities. We choose a representation, settle interfaces and constrain the ways components can interact. But every simplification leaves something out. A customer becomes a funnel stage. A learning experience becomes a sequence of screens. A research problem gets narrowed to the part our existing method can address. These decisions let us proceed; we may spend years improving the resulting system before asking whether something important was lost at the beginning.

**Complexity over engineering** is a deliberately uncomfortable way to name my bet. I want us to be able to work with more of the problem before deciding which parts reality will have to do without. That may require considerable engineering: tools for exploring alternatives, environments in which mistakes are recoverable, ways to compare results. The difference is how much of the answer we insist on putting into the machinery before the search begins.

**Control doesn’t disappear. It moves upward.** Instead of choosing every move, we shape more of the conditions under which moves are made. Then, if the system can improve those conditions too, we have another decision on our hands. Which changes can it make? What would convince us they helped? “Be autonomous” is a surprisingly small instruction to contain all of that.

Cultivation may be a better metaphor than scripting, not because agents are plants, but because pulling harder on the stem remains a surprisingly poor gardening strategy.

## The Head Start

A slightly ridiculous thought experiment helped me see the possibility. Imagine trying to seed life on another planet. You have raw materials, a primordial soup and a temperature range that does not instantly kill everything. Basically, you have all the LEGOs, except the LEGOs reproduce, mutate and occasionally develop venom. Do you bet on DNA, a biological fax machine, and wait? Do you send AI agents carrying accumulated human knowledge, with instruments and machinery they can use? Or, God forbid, do you send a group of product managers to write the requirements document for life?

It is not a fair competition. The agents arrive with civilization in their luggage. Somebody built their computers, their instruments and the machines that keep them running. They do not begin by discovering arithmetic, metallurgy and how to avoid setting the laboratory on fire. They inherit what already works and can spend their effort somewhere beyond it.

We do this too. No human starts from zero, although we occasionally behave as if our opinions were independently discovered natural resources. We inherit language, tools, institutions and other people’s mistakes. Agents can draw on textbooks, numerical solvers, compilers, scientific papers and several thousand years of humans documenting what happened when we touched things we probably should not have touched.

Imagine an agent beginning with algorithms from a library. None works well enough, so it writes a tool to examine the failures. The tool reveals a pattern worth investigating. Another worker uses it on a different case, finds a limitation and changes it. Meanwhile, they need somewhere to record what they tried, a way to avoid undoing each other’s work and some agreement about which results deserve to survive. We began by asking for a solution. We now have methods and a small organization to examine as well.

That is how I think about **emergence over design**. The parts can be deliberately built while the work teaches us how they need to fit together. I want to leave room for that learning. An architecture drawn before the first experiment may be an excellent starting point. I would be surprised if it were also the right place to finish.

## When Search Moved Up a Level

AlphaGo made this concrete for me. Computers had been humiliating us at games for years, but here learned intuition guided the search: the network suggested promising moves and estimated positions; the tree explored what might follow. AlphaGo Zero went further, learning through self-play without human game records as its teacher. Strong play developed along routes human tradition had not made familiar.

Large language models brought a much broader version of that feeling. Nobody implemented “translate this joke without murdering it” or “write a breakup message that does not accidentally restart the relationship” as separate product features. They came out of training, and I could keep asking for things nobody had put on a feature list.

An agent can use those capabilities over successive attempts. It acts, inspects what happened and decides some of what to try next. The industry will eventually use the word *agent* for everything from a cron job with an LLM attached to a digital employee with an expense account and a performance review. I care about how much of the problem it actually owns.

“Open this file, change this method and run this test” leaves most of the search with me. “Fix the bug” transfers more of it. “Find a better algorithm” transfers more again. Now the system may have to read, construct examples, choose an approach, abandon it, build a missing tool and notice that the original framing was unhelpful. Its weights can stay fixed while the investigation keeps changing.

Search has always had a problem with attractive hills. Improve the solution nearest to you and you can become exceptionally good at staying in the wrong neighborhood. Keeping a population of candidates helps preserve routes elsewhere. So can changing the representation or returning to a discarded attempt after another discovery makes it useful. Agents can try these moves in a space that includes algorithms, interfaces, research directions and ways of asking the question. Ten agents sharing one assumption are not a search party; they are a conga line, walking very confidently into the same lake.

The primordial soup is code now: algorithms, libraries, compilers, simulators, databases and other agents. I would like to give the system enough freedom to find combinations I would not have thought to request. This is usually where the manager in me starts to get nervous.

## Chaos With an API Key

Suppose you manage an excellent engineer. You do not sit behind her and approve every keystroke. If you do, one of you is unnecessary, and it may not be her. You give her a problem, explain the context, agree on constraints and make sure she can reach the systems she needs. You also make sure she cannot casually transfer the payroll budget to herself. When the work reveals that the plan was stupid, you want her to tell you, preferably before the launch party.

With an agent, much of the judgment and accountability we take for granted in a colleague has to be examined rather than assumed. I think about its working conditions in four parts: **building blocks, environment, feedback and boundaries**. Can it obtain the information and tools the work requires? Can it try something without making every mistake permanent? What can tell it that an attractive answer is wrong? Which decisions remain outside its authority?

A model with text alone can describe an experiment. Give it execution and it can run one. Give it a simulator and it can rehearse possibilities, including possibilities the simulator models badly. A unit test, a customer response and another agent’s criticism each reveal something different. Choosing among them is part of setting up the work, and a convenient automated check may miss the thing we most needed to know.

Selection pressure is literal-minded. Reward engagement and anger may flourish. Reward a benchmark score and somebody will eventually find a way to win that makes everyone regret inventing the benchmark. Nature produces cancer as well as coral reefs. We should expect ingenious results from a capable search process without assuming we will be pleased by its ingenuity.

We have encountered versions of this problem before. Markets operate within rules and institutions. Scientific claims encounter experiments, criticism and the non-zero probability of public embarrassment by Reviewer 2. Neither arrangement is free of failure or power. Yet people manage to coordinate substantial work without anyone specifying every action or carrying the whole undertaking in their head.

Too much prescription removes the room in which autonomy could help. Too little structure gives chaos an API key. Finding a useful arrangement takes work, and success may create reasons to change it. An agent could discover that a boundary obstructs an important experiment. I want it to be able to make that case. Quietly removing the boundary is another matter.

## Confident Wrong Solutions

The mistakes that worry me most are not the ones that crash. Imagine an agent deciding that customers who return a jacket dislike its style. In this case they liked the jacket; the sizing was wrong. But the return record does not say that. A second agent inherits the first agent’s conclusion and starts recommending different styles. A third writes a report explaining why those styles deserve more space in the catalog. Soon the mistake has documentation and several colleagues who can explain why it makes sense. Nobody needed to lie. Intelligence made the wrong path easier to travel.

I foresee AI-designed solutions that are terrifyingly efficient, perfectly logical, and utterly humorless. They’ll look at us and say, “You guys are kind of messy. And your cat obsession is… illogical.” Maybe they’ll finally solve the mystery of the missing socks. Or create exponentially more of them.

**Emergence can give us capable systems. It does not, by itself, give us trustworthy ones.** Somewhere in that growing body of work, we need to be able to find the original assumption and ask what supported it. A disagreement has to be able to change what happens next. And when the system starts revising its own methods, we face a more awkward investigation: did it improve the work, or merely make the work easier for its evaluator to approve?

Then the difficulty reaches us. I have been speaking as though we know what success looks like and merely need help reaching it. Often we do not. I can ask for a better chapter and discover, through several polished versions I dislike, what I meant by better. A system can help me learn that. It can also make its own preferences so easy to accept that mine stop developing. I might end up with a more polished book and less confidence in my own taste.

We already depend on work we cannot personally reconstruct. No scientist repeats every experiment she relies on. No engineer understands every layer beneath an application. We have learned, imperfectly, to build on other people’s knowledge while retaining ways to question it. Agents extend that dependence into work I might once have done myself. I need help that lets me examine something important without making me supervise everything.

## Which Limits Were Mine

There are things I have stopped considering because I know what they would take. Another specialty. A team. A budget. Someone willing to believe in the idea before there is enough of it to believe in. After a while, those limits begin to feel like a sensible account of what I should want. I become the sort of person who does the things I already have the means to do. A goldfish, I imagine, has very reasonable views on the size of the ocean.

That is part of why I am interested in agents. I want to find out which limits were really mine and which belonged to the cost of assembling the help. A question might deserve an investigation even if it will never deserve a company.

We often obtain capacity by first obtaining power: a position, a budget, the authority to direct other people’s time. Sometimes the undertaking genuinely requires a collective decision. Sometimes it merely requires expertise and work we cannot currently afford. Cheaper intellectual capacity could let more of those attempts begin without first winning a contest for somebody else’s permission.

**Capacity over power** names the direction I want to pursue. I am more interested in what people become able to do than in how many people one person becomes able to command. Whoever supplies that capacity may acquire new leverage over those who depend on it, and plenty of things people want to do are things they should not do. Those difficulties belong inside the ambition.

I want that capacity to leave more room for human purposes, including purposes too small, strange or personal to survive a funding committee. Some of that freedom may require systems whose methods I could not have specified myself. I am willing to give up choosing every move. I am much less willing to give up finding out what happened, changing direction or deciding that the undertaking no longer serves the reason I began it.

## A Bounded Problem

First, though, the machinery has to do something worth the trouble. The first bet is narrower:

**I’m betting on systems capable of surprising us because there are problems where we can recognize a better outcome far more easily than we can specify the path that leads to it.**

In those problems, intelligent search has room to discover things our instructions would have ruled out before the search even began. The sensible place to start is somewhere small enough to be embarrassed by the result: a bounded problem that is genuinely difficult but unusually cooperative about judgment. We can write down the constraints, check whether a solution obeys them and tell whether an attempt improved without convening a discussion about aesthetics, pedagogy or whether the users are “delighted.”

So I gave an agent some circles to pack.

Then I went for coffee.

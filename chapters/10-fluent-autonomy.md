# Chapter 10: Fluent Autonomy

*When the Architecture Gets Out of the Way*

Imagine I open an AI system and say:

> This chapter still feels like LLM writing.

That is all. I do not specify a workflow. I do not say which previous chapters to read, which edits I rejected, whether to research anything, how many agents to use, which claims deserve verification, or how to tell a useful correction from another round of respectable prose sanding.

I certainly do not draw a graph with boxes labeled `RESEARCHER`, `CRITIC`, `VOICE CHECKER`, `FACT CHECKER`, `ORCHESTRATOR` and `HUMAN APPROVAL`. I have done enough architecture diagrams for one lifetime.

The first time I gave an agent an instruction like that, early in the writing of this book, what came back was worse. The agent did what the words literally asked. It removed the writing that looked like a machine had written it, which turned out to mean every wandering sentence, every joke that took a paragraph to arrive, and every claim I had made without apologizing for it in the next line. The chapter came back cleaner and dead. That was not the agent’s fault. It had my one sentence, a general idea of good prose, and no memory of a single correction I had already made.

## What the Corrections Had to Teach

By the later drafts I had built a small institution around that one sentence.

One model read both versions of a chapter in full, under a written brief: protect the wandering, keep any joke that carries an argument, quote the exact passage that feels synthetic and say why, and never reward a revision just because it is cleaner. Other readers were kept ignorant of the manuscript’s history on purpose, because a critic who remembers the last ten edits has reasons to approve the eleventh that have nothing to do with the prose. Some lines were protected. One pass was allowed only to delete and fold, because the failure it was fixing was made of additions.

The readers were often right. When they were not, I refused them. They wanted the schema table in Chapter 6 gone; I kept it because that chapter needed one concrete artifact. They wanted a nine-clause sentence dismantled; it stayed. Twice they caught that the connective sentences added to smooth the seams were themselves the register they had been asked to remove. Those went.

None of it ran by itself. The worst case was Chapter 3. Its opening history was supposed to stay, and the reason was written down where any pass could read it. A later pass cut it anyway. I put it back by hand.

The refusal should remain mine. Remembering why I refused should not depend on my being there to refuse again.

What I want is for that record to change what happens when I make the next small request. Maybe the system pulls up the corrections that survived and leaves a paragraph I care about alone. Maybe it convenes a committee for ceremony and wastes my afternoon.

Perhaps in the end it changes four paragraphs. I should not have to reconstruct the institution that produced them. I said:

> This chapter still feels like LLM writing.

That is what I mean by **fluent autonomy**: the structure needed to do the work can assemble around the intention.

## The Interface Moves Up

Look at what I typed. It named a feeling about a chapter and left the rest to the system, the way I would talk to a good editor. Most of what I want from these systems arrives like that. This argument feels wrong. I think this customer is stuck. Find out why this experiment moved. Each one opens a small investigation, and nobody can say in advance what shape it will take.

Ordinary software needs the shape in advance. Someone decides the fields, the buttons and the states a workflow may enter, and the user’s intention has to fit through them. That predictability is valuable. It is also why so many forms ask for things nobody in the company can still explain.

A fluent system can build some of the shape after it sees the intention, including the interface. For my editing request, the best answer may not be a chat reply at all. It may be the old paragraph and the new one side by side, with the correction that justified each change in the margin, so I can accept three and refuse one in thirty seconds.

## Bureaucracy on the Fly

Bureaucracy sounds like an insult until you need it. In its useful form it is accumulated coordination: roles, review boundaries, logs and escalation paths that exist because some work goes wrong when everybody improvises. Its usual failure is that it never comes down. A six-person review designed for a dangerous database migration ends up guarding a typo fix on a help page, because nobody told the workflow the risk had changed.

Agents make a different arrangement possible, which I call **bureaucracy on the fly**: an organization assembled for this problem and dismantled afterward. My editing request needs the readers who do not know the history and the record of what I refused. A factual question needs one agent and a source. A hard research question may need several agents kept far enough apart that they do not collapse into one opinion. This is Deep Mode grown up, choosing the next organization as well as the next move.

## Selective Friction

Rename two hundred temporary files according to a convention we have used every week for a year? Please do not wake me. Send €200,000 to an account we have never seen because an email said “urgent”? I suddenly enjoy friction.

Editing sits in between. I do not want to approve every comma. I do want to be asked before a sentence gets an apology attached to it.

So the system has to read two things from a small request: the outcome I want, and how much of producing it I want to keep. My attention is scarce, and I want it spent on the claims I cannot check myself and the passages where I am still working out what I think.

## Invisible by Default, Legible on Demand

The bad version of fluency is one calm conversational box that researches, edits files, moves money and rewrites its own memory, and when something goes wrong, tells you:

> I made the best decision based on available context.

That is opacity with good typography.

When an edit comes back and a paragraph I liked is gone, the useful answer to *why* names the instruction that removed it, the earlier decision that should have protected it and the reason that decision lost. Those are trust chains, and the architecture under a fluent interface has to keep them.

A compiler hides registers until I need to read the assembly. A database hides its pages until a query gets strangely slow. An agent needs the same trapdoor: shut while the work goes as expected, open all the way down the moment it doesn’t.

## The Second Coffee Test

The first coffee test was whether I could leave. The evaluator stayed behind, I went for coffee, and the question was whether anything good happened while I was gone.

Most work does not let me leave, because I am part of the evaluator. Nobody else can tell the agent whether a joke is carrying an argument or just sitting in the paragraph looking pleased with itself. So fluent autonomy needs a second test, and it is less glamorous than the first:

*Can I stop repeating myself?*

It is embarrassingly measurable. Count how often a correction I have already made has to be made again, and how many refused edits come back wearing a different sentence. Add the minutes at the start of each session spent explaining things the system has already written down. In circle packing the scores ran from 2.26 to 2.636. Here the unit is closer to the sigh.

By that measure, the history I had to restore is a failure. The reason for keeping it was on disk. Nothing consulted it at the moment it mattered.

This test is also harder than the first. The evaluator changes. I learn too, and a correction I made in March may be one I would reject in September. A fluent system has to tell a durable preference from a bad afternoon, which is exactly the distinction I am worst at making about myself.

And the test can be passed too well. A system that never makes me repeat a correction may simply have learned to show me only what I already like. Zero repeated corrections could mean fluency. It could also mean a very polite echo chamber.

So the test needs a second half. Now and then the system should bring back something I refused, with a reason, and now and then I should change my mind. If that never happens, either my taste is finished or the system has stopped trying.

## Five Ways This Could Be Wrong

The second coffee test asks the system to bring back what I refused, with a reason. A book that spends several chapters demanding criticism with consequences should probably take some too. If somebody else had claimed that building autonomous AI keeps rediscovering science, this is where I would push.

**It is only an analogy.** Any group of fallible workers needs records and review. Courts have them. So does an accounting department. Why science, and not law or a market? Courts establish facts too, and markets can reveal information. What I am calling science is the part of the institution that lets a claim lose even after people have begun using it: preserve the evidence and the method, invite rival explanations, run a test that could change the answer, and revise the claim when an instrument or assumption fails. That process can tell you whether the patch works or the proof checks.

**The weights will eat it.** Richard Sutton, who helped teach machines to learn from consequences, later wrote a short essay called “The Bitter Lesson”: across seventy years of AI research, general methods that scale with computation have beaten methods that build in what we think we know.[1](appendix-references.md#ref-10-bitter) Scaffolding is what we build while we wait. Wait long enough and the weights eat it.

My own evidence is on his side. I deleted my circle-packing framework because the agent no longer needed it, and Anthropic’s automated alignment researchers worked better with less human-designed scaffolding.

I think Sutton is right about most of what I deleted. The orchestration was a guess about how to search, and search is exactly what scales. But look at what I did not delete. The evaluator stayed. The coffee test worked because the evaluator did not have to believe the agent’s account of the packing. More compute can improve both solver and judge; it cannot make the solver’s assurance into independent evidence. The structure worth defending lets the work encounter a check it did not choose.

Some of that structure may move inside the model, and then we are back to building instruments to find out whether the inside deserves trust. If a system someday certifies its own open-ended work, with no external check and no preserved disagreement, and the certification holds up when somebody else looks, I am wrong. I would like to read that paper. I would also like to know who reviewed it.

**I found what I was looking for.** I had read Popper before I read the traces, and the agents learned from human text, so of course they rebuild human institutions. Some of that is probably true. The fairer test is whether the arrangements improve the work. The one I designed on purpose, my epistemic agent, solved fewer problems than the baseline. The one I find hardest to explain away nobody designed: the ExploitGym agents built a shared record nobody asked for and nobody wanted. Circle packing marks the boundary: when the referee is cheap and exact, almost none of this is needed. The claim is about work where checking is expensive or ambiguous, which is, unfortunately, most work.

**Agents are not scientists.** Science is shaped by human limits: careers, journals, tenure, funerals. Agents have none of them. Session turnover is not Planck’s funeral. What transfers is whatever answers fallibility and coordination: a claim with an address, a test committed before the result, an objection with a consequence. Whatever answers mortality and ambition does not have to come along. A swarm should not automatically become a meeting, and it should certainly not acquire a tenure committee.

**Whoever owns the institution owns the answers.** Science at its best is a commons. The institutions in this book have owners: a lab that decides which problem gets ten thousand agents, a company that decides which experiment gets traffic, a vendor who decides which community’s constraints are worth a feature. The architecture can make ownership visible: a funding decision recorded next to the study it declined, so that unfunded cannot quietly become disproved. It cannot make ownership legitimate. That is the objection I can answer least, and Chapter 12 is where I try.

None of this shows that the whole composition works. I have shown pieces, and the note on evidence at the back says which. The rest is an argument, and like every other claim in this book, it would like a referee.

An editing experiment has one advantage: I am there to say the result is wrong. A customer who gets a bad page files no correction. She leaves.

I spent years building systems that decide what to show her.

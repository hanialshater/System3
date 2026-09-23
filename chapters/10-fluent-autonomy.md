# Chapter 10: Fluent Autonomy

*When the Architecture Gets Out of the Way*

Imagine I open an AI system and say:

> This chapter still feels like LLM writing.

That is all. I do not specify a workflow. I do not say which previous chapters to read, which edits I rejected, whether to research anything, how many agents to use, which claims deserve verification, or how to tell a useful correction from another round of respectable prose sanding.

I certainly do not draw a graph with boxes labeled `RESEARCHER`, `CRITIC`, `VOICE CHECKER`, `FACT CHECKER`, `ORCHESTRATOR` and `HUMAN APPROVAL`. I have done enough architecture diagrams for one lifetime.

The first time I gave an agent an instruction like that, early in the writing of this book, what came back was worse. The agent did what the words literally asked. It removed the writing that looked like a machine had written it, which turned out to mean every wandering sentence, every joke that took a paragraph to arrive, and every claim I had made without apologizing for it in the next line. The chapter came back cleaner and dead. That was not the agent's fault. The sentence I had given it was evidence about what I wanted, not a specification of it, and the agent had nothing around it that could turn the one into the other: my words, a general idea of good prose, and no memory of the corrections I had already made.

## What the Corrections Had to Teach

Later attempts had something the first one lacked: an accumulated record of corrections. The editing history shows what that made possible, and how much work I was still doing.

There was an evaluator with a written brief: read both versions in full, protect the wandering and the jokes that carry argument, quote the exact passage that feels synthetic and say why, and refuse to reward a revision merely because it is cleaner. Some model readers were deliberately kept ignorant of the manuscript's history, since remembering the last ten edits can give a critic reasons to approve the eleventh that have nothing to do with the prose. There were protected lines. One pass was permitted only to delete and fold, because the failure it was fixing was made of additions.

The evaluations recorded places where the writing had stopped sounding like a person, each with a reason, and changes I refused. At one stage they wanted the schema table in the chapter on patterns gone. I kept it because the chapter needed a concrete artifact; it later became the filled-in pattern the reader has now seen. They wanted a nine-clause sentence dismantled; it stayed. They caught, twice, that connective sentences added to smooth the seams were themselves the register they had been asked to remove. Those went.

This was still work. I was refusing edits, correcting the process and restoring things it had removed. The brief and the separate readings gave those interventions something to build on; they had not made my labor disappear. The history at the start of Chapter 3 still got cut after the reason for keeping it had been recorded. I had to bring it back.

The refusal should remain mine. Remembering why I refused should not depend on my being there to refuse again.

What I want is for that record to change what happens when I make the next small request. The system might retrieve the corrections that survived and compare the chapter with passages I kept. It might decide that a disputed claim needs research, while a joke needs to be left alone. A second model could challenge an argument where disagreement is likely to add information. It could also waste an afternoon producing a committee for ceremonial reasons; the arrangement itself has to be judged.

After all that, perhaps the system changes four paragraphs. I should not have to reconstruct the institution that produced them. I said:

> This chapter still feels like LLM writing.

That is what I mean by **fluent autonomy**: the structure needed to do the work can assemble around the intention.

## The Interface Moves Up

The argument of this book began with a recurring move: once something complicated becomes reliable enough, the layer above can start treating it as a primitive.

We stopped programming by wiring individual transistors. We stopped thinking about registers every time we wrote a high-level function. Libraries hid algorithms. Applications hid libraries. Coding agents began treating applications, files, browsers, terminals and APIs as tools.

AI agents push that abstraction one level higher. Increasingly the interface is an **outcome described incompletely in ordinary language**.

That incompleteness matters. When I call a function, I am supposed to know what function I want. When I talk to another capable human, I often do not. I can say:

> This argument feels wrong.
>
> Find somewhere good for dinner.
>
> I think this customer is stuck.
>
> We need to understand why this experiment moved.
>
> I am considering changing jobs.

None of these is a specification. Each opens a small investigation.

Traditional software handles this badly because software usually requires the designer to anticipate the structure of the intention in advance. Somebody decides which fields exist, which buttons appear, which states the workflow may enter and which exceptions deserve their own branch. That predictability is useful. It is also why every mature enterprise product eventually contains a form whose existence can be explained only by an archaeological expedition through three reorganizations.

A fluent autonomous system can construct part of the structure **after seeing the intention**. That leaves it with a choice ordinary software usually makes in advance: what interface would help here?

Menus, spreadsheets, dashboards, canvases, forms and direct manipulation are not historical accidents waiting for language models to abolish them; often they are excellent interfaces.

Sometimes I want Excel because seeing the table is faster than discussing it. Sometimes I want a dashboard because twenty numbers at once tell me more than twenty conversational turns. Sometimes I want to drag the object myself because my hand knows what I mean before I have words for it.

The application becomes a primitive available to the agent and to me. If a spreadsheet is the right temporary representation, make one. If direct manipulation is better, show me the canvas. If the task is routine, use the tool and return the result. If the problem is underspecified, conversation may remain the best interface because conversation is what humans already use when neither side knows in advance exactly where the interaction is going. The interface itself can become part of the solution.

## Bureaucracy on the Fly

There is a phrase that sounds like an insult until you need it: **bureaucracy**.

Bureaucracy, in its useful form, is accumulated coordination. Roles, review boundaries, logs, standards, escalation paths and procedures exist because some kinds of work become unreliable when everybody improvises everything at once.

The problem is that fixed bureaucracy calcifies. A six-person review process designed for a dangerous database migration eventually gets applied to changing a sentence in a help page because nobody remembered to tell the workflow that reality had changed.

Agent systems give us the possibility of **bureaucracy on the fly**: an organization assembled for the problem rather than inherited wholesale from the previous one.

A factual question may need one agent and a source. A difficult scientific claim may need competing hypotheses, a literature search, code, an experiment and an evaluator insulated from the researcher who wants the result to work. A writing edit may need none of that: perhaps the original paragraph, a memory of previous corrections and enough restraint to leave the sentence alone. A high-impact financial action may need very little creativity and quite a lot of permission checking. A genuinely novel research problem may need several agents pursuing different approaches without sharing enough context to collapse into one correlated opinion.

The organization should be **as large as the uncertainty deserves and no larger**. This is where the society, the patterns and the oversight machinery meet: patterns tell the system which institutional shapes have worked before, and System 3 keeps those patterns answerable to evidence. The system can compose a temporary organization, run it, observe whether it helped, preserve what deserves to survive and dismantle the rest.

What used to be a workflow diagram becomes part of runtime. The human gives the problem, and the system compiles an institution.

## Selective Friction

A fluent agent is not an agent that never asks questions. It is also not an agent that asks permission for every action. That is an approval workflow that has learned to talk. The useful question is where friction belongs.

Rename two hundred temporary files according to a convention used every week for a year? Please do not wake me. Send €200,000 to an account we have never seen because an email said “urgent”? I suddenly enjoy friction.

The human's own learning adds another reason to slow down. Sometimes friction is not about safety. Sometimes friction is the point of the interaction. If I ask the system to teach me statistics, instantly solving every exercise is not fluent assistance—it is substitution wearing a tutor badge. If I ask for help deciding between two life choices, collapsing the uncertainty into one confident recommendation may remove exactly the thinking I needed to do. If I want a routine analysis completed, making me rediscover every intermediate step is wasted attention.

So the system has to infer not only **what outcome I want**, but **what role I want to retain in producing it**. Human attention is scarce, but the objective is not to minimize it. Spend it where it changes the result, where the action is hard to reverse, where values conflict, where the evidence is weak, where a new failure mode appears—or where the human is trying to become more capable rather than merely get the thing done. Needing little human input can be a side effect of spending it well.

## Invisible by Default, Legible on Demand

There is another bad version of fluency. Everything works through one beautiful conversational box. The system performs research, edits files, transfers money, changes production settings and updates its own memory. The interface stays calm and minimalist throughout.

Then something goes wrong. You ask why, and the system says:

> I made the best decision based on available context.

This is opacity with good typography.

The architecture underneath the interface has to leave traces. Which evidence mattered? Which pattern was retrieved? What alternatives were considered? Which evaluator rejected the other approach? What changed from the previous version? Which action is reversible? What uncertainty was hidden because it did not matter, and what uncertainty should have reached the human but did not?

Those are trust chains. A compiler hides registers from me most of the time, but I can still inspect the generated assembly when the abstraction leaks. A database hides pages and indexes until performance becomes strange. An autonomous system needs an equivalent way back into the work. Most of the time I should be able to speak at the level of intention. When something becomes uncertain, consequential or surprising, the lower layers should become visible again.

The request can remain simple:

> **Here is what I am trying to accomplish. Help me get there without losing contact with reality—or with me.**

In the next writing session, I should be able to spend my attention on the argument. If I am once again explaining why the agent should read its own record of my last objection, the interface has hidden very little of the work.

## The Second Coffee Test

The test in Chapter 2 was whether I could leave. The evaluator stayed behind, I went for coffee, and the question was whether anything good happened while I was gone.

Most work does not let me leave, because I am part of the evaluator. Nobody else can tell the agent whether a joke is carrying an argument or just sitting in the paragraph looking pleased with itself. So fluent autonomy needs a second test, and it is less glamorous than the first:

*Can I stop repeating myself?*

It is embarrassingly measurable. Count how often a correction I have already made has to be made again, and how many refused edits come back wearing a different sentence. Add the minutes at the start of each session spent explaining things the system has already written down. In circle packing the scores ran from 2.26 to 2.636. Here the unit is closer to the sigh.

By that measure, the Chapter 3 history I had to restore is a failure, and an instructive one. The reason for keeping it was on disk. Nothing consulted it at the moment it mattered. The clay had preserved what it was given.

The second test is harder than the first in two ways. The evaluator changes. Chapter 9 argued that the human learns too, and a correction I made in March may be one I would reject in September. A fluent system has to tell a durable preference from a bad afternoon, which is exactly the distinction I am worst at making about myself.

And the test can be passed too well. A system that never makes me repeat a correction may simply have learned to show me only what I already like. Zero repeated corrections could mean fluency. It could also mean a very polite echo chamber.

So the test needs a second half. Now and then the system should bring back something I refused, with a reason, and now and then I should change my mind. If that never happens, either my taste is finished or the system has stopped trying.

## Five Ways This Could Be Wrong

I have claimed that as we build autonomous AI, we keep rediscovering science as its architecture. A book that spends several chapters demanding criticism with consequences should probably take some. Here is how I would attack the claim if somebody else had made it.

**It is only an analogy.** Any group of fallible workers needs records and review. Courts have them. So does an accounting department. Why science, and not law or a market? Because of what the agents produce. A court settles a dispute by authority; a market settles it by price. The agents in these chapters produce claims: the patch works, the metric means what we think it means, the proof checks. The institution whose product is a claim that can be revised is science. Where the question turns to who decides, the book does reach for law. Chapter 7 needed a constitution, and Chapter 9 needed a boundary the evidence cannot cross. Science for what is known. A constitution for who decides.

**The weights will eat it.** This is the one that keeps me up. Richard Sutton, whom we met in Chapter 7 teaching machines to learn from consequences, later wrote a short essay called “The Bitter Lesson”: across seventy years of AI research, general methods that scale with computation have beaten methods that build in what we think we know.[^bitter] Scaffolding is what we build while we wait. Wait long enough and the weights eat it.

My own evidence is on his side. In Chapter 2 I deleted my framework because the agent no longer needed it. In Chapter 8, researchers found that too much human-designed scaffolding made their automated researchers less flexible.

I think Sutton is right about most of what I deleted. The orchestration was a guess about how to search, and search is exactly what scales. But look at what I did not delete. The evaluator stayed. The coffee test worked because the thing judging the packing was not the thing producing it, and more compute does not change that. What survives the bitter lesson is not the structure that helps a system think. It is the structure that lets someone else check.

Some of that structure may move inside the model, and then Chapter 8 happens again: we build instruments to find out whether the inside deserves trust. If a system someday certifies its own open-ended work, with no external check and no preserved disagreement, and the certification holds up when somebody else looks, I am wrong. I would like to read that paper. I would also like to know who reviewed it.

**I found what I was looking for.** I had read Popper before I read the traces, and the agents learned from human text, so of course they rebuild human institutions. Two things count against this. Neither is a proof. Carlini was building a compiler, not an epistemology; his locks, progress files and CI arrived as repairs. And my own epistemic agent in Chapter 4 solved fewer problems than the baseline. If I was arranging the evidence, I arranged it badly. Chapter 2 marks the boundary: when the referee is cheap and exact, almost none of this is needed. The claim is about work where checking is expensive or ambiguous, which is, unfortunately, most work.

**Agents are not scientists.** Science is shaped by human limits: careers, journals, tenure, funerals. Agents have none of them. True, and Chapter 6 says so: session turnover is not Planck’s funeral. What transfers is whatever answers fallibility and coordination: a claim with an address, a test committed before the result, an objection with a consequence. Whatever answers mortality and ambition does not have to come along. A swarm should not automatically become a meeting, and it should certainly not acquire a tenure committee.

**Whoever owns the institution owns the answers.** Science at its best is a commons. The institutions in this book have owners: a lab that decides which problem gets ten thousand agents, a company that decides which experiment gets traffic, a vendor who decides which community’s constraints are worth a feature. The architecture can make ownership visible. Chapter 6 kept the funding decision next to the unfunded study, so that unfunded could not quietly become disproved. It cannot make ownership legitimate. That is the objection I can answer least, and Chapter 12 is where I try.

None of this shows that the whole composition works. I have shown pieces, and the map at the front of the book says which. The rest is an argument, and like every other claim in this book, it would like a referee.

## Monday Morning

In an editing experiment, I can stop the work, change the brief and try again. A theory of fluent autonomy also has to survive systems that cannot be redesigned from scratch and people who did not volunteer to participate in the metaphor.

I needed a less polite laboratory. Fortunately, Monday morning was waiting.

---

> *Spend attention where it changes the result.*\
> *Invisible by default. Legible on demand.*

[^bitter]: Richard S. Sutton, “The Bitter Lesson,” 13 March 2019, <http://www.incompleteideas.net/IncIdeas/BitterLesson.html>.

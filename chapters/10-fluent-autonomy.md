# Chapter 10: Fluent Autonomy

*When the Architecture Gets Out of the Way*

Early in writing this book I opened an agent and typed:

> This chapter still feels like LLM writing.

That was all. I did not specify a workflow. I did not say which previous chapters to read, which edits I rejected, whether to research anything, how many agents to use, which claims deserve verification, or how to tell a useful correction from another round of respectable prose sanding.

I certainly did not draw a graph with boxes labeled `RESEARCHER`, `CRITIC`, `VOICE CHECKER`, `FACT CHECKER`, `ORCHESTRATOR` and `HUMAN APPROVAL`. I have done enough architecture diagrams for one lifetime.

What came back was worse than what I had sent. The agent did what the words literally asked. It removed the writing that looked like a machine had written it, which turned out to mean every wandering sentence, every joke that took a paragraph to arrive, and every claim I had made without apologizing for it in the next line. The chapter came back cleaner and dead. That was not the agent’s fault. It had my one sentence, a general idea of good prose, and no memory of a single correction I had already made.

## Scaffolding

By the later drafts I had built a small institution around that one sentence.

One model read both versions of a chapter in full, under a written brief: protect the wandering, keep any joke that carries an argument, quote the exact passage that feels synthetic and say why, and never reward a revision just because it is cleaner. Other readers were kept ignorant of the manuscript’s history on purpose, because a critic who remembers the last ten edits has reasons to approve the eleventh that have nothing to do with the prose. Some lines were protected. One pass was allowed only to delete and fold, because the failure it was fixing was made of additions.

The readers were often right. When they were not, I refused them. They wanted the schema table in the pattern-language chapter gone; I kept it because that chapter needed one concrete artifact. They wanted a nine-clause sentence dismantled; it stayed.

None of it ran by itself. The worst case was a chapter whose opening history was supposed to stay, and the reason was written down where any pass could read it. A later pass cut it anyway. I put it back by hand.

Every piece of that institution was a repair for a failure I had already suffered, which is how the sixteen Claudes got their harness in Chapter 5. It was slow. Every request went through a brief, two kinds of reader, a list of protected lines and me. It worked, and I did not want to live in it.

The refusal should remain mine. Remembering why I refused should not depend on my being there to refuse again.

## Distillation

Chapter 7 mentioned a paper with a cheeky subtitle, *Making VGG-style ConvNets Great Again*, as evidence that a plain stack of three-by-three convolutions could hold its own against architectures found by expensive search. I left out how it got plain.

During training, a typical RepVGG block has three branches side by side: a three-by-three convolution, a one-by-one convolution and a shortcut that passes its input straight through. The branches make the network easier to train. When training ends, a little linear algebra folds all three into a single three-by-three convolution that computes exactly the same function. The authors call this structural re-parameterization.[1](appendix-references.md#ref-10-repvgg) The network you deploy is plain and fast. The network that learned was not.

AlphaGo Zero did a looser version of the same thing. Every move it played in training came out of a tree search that looked ahead through many positions, guided by its network. Then the network was trained to predict the search’s move probabilities and the game’s outcome. The search improved the network, the better network guided a better search, and round by round more of what the search knew moved into the network’s intuition.[2](appendix-references.md#ref-10-alphagozero)

Science has its own version. Chris Olah and Shan Carter called it distillation too: the textbook, explanation or diagram that lets a newcomer skip three years of someone else’s climb.[3](appendix-references.md#ref-10-distill) And Sam, in Chapter 6, was a distillation of another kind. Years of incidents, migrations and launches went into him, and what came out was “You see it after a while.”

That is what I want behind my one sentence: a system that has learned my preferences, and also how to organize itself around them. A typo needs a style sheet and nobody’s attention, least of all mine. My chapter needs the record of what I refused, readers who do not know its history and a reason for every cut. Finding out why an experiment moved needs instruments, rival explanations and a small budget for the unlikely one. An invoice needs almost no intelligence and my signature. **Fluent autonomy**, as I mean it, is a system that forms the institution a request needs, behind an interface small enough to talk to, and takes it down when the work is done.

I say the chapter still feels like LLM writing. Behind that sentence, readers assemble, refusals get consulted, and perhaps four paragraphs change.

## The Interface Moves Up

Most of what I want from these systems arrives the way that sentence did: a feeling about a chapter, left for the system to work out, the way I would talk to a good editor. This argument feels wrong. I think this customer is stuck. Tell me what I am missing in this plan. Each one opens a small investigation, and nobody can say in advance what shape it will take.

Ordinary software needs the shape of the work in advance. Someone decides the fields, the buttons and the states a workflow may enter, and the user’s intention has to fit through them. That predictability is valuable. It is also why so many forms ask for things nobody in the company can still explain. A fluent system can build some of the shape after it sees the intention. For my editing request, the best answer may not be a chat reply at all. It may be the old paragraph and the new one side by side, with the correction that justified each change in the margin, so I can accept three and refuse one in thirty seconds.

Bureaucracy sounds like an insult until you need it. In its useful form it is accumulated coordination: roles, review boundaries, logs and escalation paths that exist because some work goes wrong when everybody improvises. Its usual failure is that it never comes down. A six-person review designed for a dangerous database migration ends up guarding a typo fix on a help page, because nobody told the workflow the risk had changed.

Not every request deserves the same amount of me. Rename two hundred temporary files according to a convention we have used every week for a year? Please do not wake me. Send €200,000 to an account we have never seen because an email said “urgent”? I suddenly enjoy friction. Editing sits in between. I do not want to approve every comma. I do want to be asked before a sentence gets an apology attached to it. My attention is scarce, and I want it spent on the claims I cannot check myself and the passages where I am still working out what I think.

## The Second Coffee Test

The first coffee test was whether I could leave. The evaluator stayed behind, I went for coffee, and the question was whether anything good happened while I was gone.

Most work does not let me leave, because I am part of the evaluator. Nobody else can tell the agent whether a joke is carrying an argument or just sitting in the paragraph looking pleased with itself. So fluent autonomy needs a second test, and it is less glamorous than the first:

*Can I stop repeating myself?*

It is embarrassingly measurable. Count how often a correction I have already made has to be made again, and how many refused edits come back wearing a different sentence. Add the minutes at the start of each session spent explaining things the system has already written down. In circle packing the scores ran from 2.26 to 2.636. Here the unit is closer to the sigh.

The evaluator changes. I learn too, and a correction I made in March may be one I would reject in September. A fluent system has to tell a durable preference from a bad afternoon, which is exactly the distinction I am worst at making about myself.

## The Weights Will Eat It

Richard Sutton, who helped teach machines to learn from consequences, later wrote a short essay called “The Bitter Lesson”: across seventy years of AI research, general methods that scale with computation have beaten methods that build in what we think we know.[4](appendix-references.md#ref-10-bitter) On his reading, scaffolding is what we build while we wait.

For a long time I read that as the strongest objection to this book, and my own evidence is on his side. I deleted my circle-packing framework because the agent no longer needed it. The orchestration was a guess about how to search, and search is exactly what scales.

I now read it as the middle of the argument. Of course the weights eat the scaffolding. That is what distillation is for. The search moves into the network, the harness moves into the model, the editing brief becomes a preference the system no longer has to be told. Most of the scaffolds in this book are meals waiting to be eaten, and they should be.

Look at what I did not delete, though. The evaluator stayed. The coffee test worked because the evaluator did not have to believe the agent’s account of the packing. More compute can improve both solver and judge; it cannot make the solver’s assurance into independent evidence. What is worth defending is a check the solver did not choose. Put that check inside the model and it becomes one more of the model’s opinions.

Some of the checking may move inside anyway, and then we are back to building instruments to find out whether the inside deserves trust. If a system someday certifies its own open-ended work, with no external check and no preserved disagreement, and the certification holds up when somebody else looks, I am wrong. I would like to read that paper. I would also like to know who reviewed it.

## What the Fold Forgets

RepVGG’s fold is exact. The plain network computes the same function as the branched one, so the branches can be thrown away. Nothing about my editing institution folds that cleanly.

The reasons go first. The history I put back by hand had a written reason for staying, and the reason was on disk. The pass that cut it had learned what I usually want and had not consulted why I wanted this. Sam’s last line in the serializer pattern failed the same way: true when he wrote it, its reason never linked, still giving instructions a year later. A distilled preference that has lost its reasons is high-functioning bullshit about me.

So the scaffolding cannot simply come down. It has to stay where the system can reach it, folded out of the way while the work goes as expected and open all the way down the moment it doesn’t. When an edit comes back and a paragraph I liked is gone, the useful answer to *why* names the instruction that removed it, the earlier decision that should have protected it and the reason that decision lost. A compiler hides registers until I need to read the assembly. A database hides its pages until a query gets strangely slow. An agent needs the same trapdoor.

The bad version of fluency is one calm conversational box that researches, edits files, moves money and rewrites its own memory, and when something goes wrong, tells you:

> I made the best decision based on available context.

That is opacity with good typography.

Meanwhile the scaffolding keeps growing back. Each failure in this book left something behind: the corrections I kept making became a set of skills, small files an agent reads before it touches a chapter; one of them exists only to take the machine out of my prose. The review of 255 flagged passages left a reason beside every decision, which is the raw material for the next brief.

The potter’s apprentice in Chapter 5 learned the same way, long before anyone had weights to put it in. He followed her precautions until his hands felt what hers felt. If he was any good, a day came when a precaution was wrong for this clay, and he had to notice. Then he taught the new precaution to someone else.

## Creative Distrust

The second coffee test can be passed too well. A system that never makes me repeat a correction may simply have learned to show me only what I already like. Zero repeated corrections could mean fluency. It could also mean a very polite echo chamber. The second Mallorca machine in Chapter 9 would pass this test too.

Distilled knowledge can be fast because it has stopped reopening familiar questions, which is also why it can miss what is new. Chapter 7’s Move 78[5](appendix-references.md#ref-10-move78) and KataGo attacks[6](appendix-references.md#ref-10-adversarial-go) exposed blind spots in excellent learned intuition. The objection came from outside the intuition being tested.

Chapter 4 named the remedy and then left it alone. Creative distrust means understanding a trust chain well enough to know where you are breaking it and why. It is the other half of fluency. The system keeps what it has learned about me and, every so often, reopens it on purpose, in the places where what it learned may be what is stopping the next idea.

For my editing, that means the system should now and then bring back something I refused, with a reason, and now and then I should change my mind. If that never happens, either my taste is finished or the system has stopped trying.

Creative distrust has already turned on this book twice. The first time it was aimed at my instructions: on two occasions the readers caught that the connective sentences added to smooth the seams were themselves the register they had been asked to remove. Those went.

The second time it was aimed at my prose, near the end. A pass over the manuscript flagged 255 passages for patterns a language model tends to produce: the aphorism that restates its own paragraph, the reversal that says what something is not before saying what it is, the signpost announcing what the reader has just seen. Some of those habits may have been mine before I ever opened a chat window. Some were probably the residue of many revisions with machines that like a tidy ending. After months of editing with agents, I could no longer reliably tell which was which. The question on every line was the one this book keeps asking of other people’s claims: earned, or inherited without its reasons?

In the end I typed the one-sentence version again: decide for me, keep the useful and the earned. The review marked 150 flags for editing and 81 for keeping; 18 had already been revised and six still needed an author detail. An edit could cut a neighboring recap while keeping the line that carried the argument. The review also reconsidered its own reasons: the tenure and training-budget callbacks were restored. Every decision came with a reason on a page I could open and overrule. That was the only reason I could let it decide.

My taste is harder to distrust than my sources, because it is part of the evaluator. The rule from Chapter 7 holds here too: the system may propose overturning a refusal, with its reason and its evidence, and may not overturn one quietly.

The system should distrust its own organization too. Chapter 6 ended on an uncomfortable discovery: the procedure decides what gets checked. A system that has learned one good way of organizing itself will reach for it every time, the way the Linux build pointed all sixteen Claudes at the same failure. Occasionally it should try an arrangement it would not usually choose, keep a reader it would normally skip, or ask whether a check it always runs has caught anything in a year. Changes to how it judges its own work stay on the constitutional surface, where it can propose and somebody else decides.

## Coupled to a Person

Stuart Russell’s answer, which Chapter 8 introduced, begins with uncertainty. A beneficial machine should pursue what the human prefers, should start out unsure what that is, and should treat what the human does as evidence about it.[7](appendix-references.md#ref-10-cirl) In the off-switch game, that uncertainty is what gives the machine a reason to let the human interrupt.[8](appendix-references.md#ref-10-offswitch) Chapter 9 adds that the preference itself is still being built, so the uncertainty never gets to close. A system that has distilled months of my corrections is tempted to stop being unsure. My refusals harden into rules, my habits pass for my preferences, and my next interruption looks like noise. Uncertainty keeps my refusals as evidence instead of law. It is why the system should ask before a sentence gets an apology attached, and why “decide for me” was a delegation with a boundary: decisions with reasons, on a page I could overrule.

Being unsure what I want takes a model of who I am: what I already know, what I meant by better last month, where my taste has settled and where it is still moving. Chapter 9 asked the founder’s assistant for that kind of theory of mind. Here the mind being modeled is mine, and the same model can be used two ways. A recommender uses it to learn which suggestions I will accept and to make me easier to satisfy. A mentor uses it to decide what I should do myself.

A mentor would have handled the flagged passages differently. It would have decided twenty, shown me its reasons, and then asked me to decide the next twenty before showing its own call. A week later it would have brought back the three I got wrong. It would be the annoying tutor from Chapter 9, pointed at my own book. A good mentor accepts being liked less on Wednesday. It also knows that people learn what to want from other people, so now and then it hands me to one.

A system coupled to me judges itself partly by what I can do without it afterward. So the second coffee test needs a companion question, and it is the hardest to score: after working with the system, do I understand what I want better than I did before? Whether that review left me understanding my own voice better is a question only I can answer.

## Where This Could Be Wrong

Creative distrust has to reach the book too: a book that spends several chapters demanding criticism with consequences should probably take some. If somebody else had claimed that building autonomous AI keeps rediscovering science, this is where I would push.

The easy objection is that it is only an analogy. Any group of fallible workers needs records and review. Courts have them. So does an accounting department. Why science, and not law or a market? What I am calling science is the part of the institution that lets a claim lose even after people have begun using it: preserve the evidence and the method, invite rival explanations, run a test that could change the answer, and revise the claim when an instrument or assumption fails.

I will concede the analogy has edges. Science is shaped by human limits: careers, journals, tenure, funerals. Agents have none of them. What transfers is whatever answers fallibility and coordination: a claim with an address, a test committed before the result, an objection with a consequence. A swarm should not automatically become a meeting, and it should certainly not acquire a tenure committee.

Then there is the chance that I found what I was looking for. I had read Popper before I read the traces, and the agents learned from human text, so of course they rebuild human institutions. Some of that is probably true. The fairer test is whether the arrangements improve the work. The one I designed on purpose, my epistemic agent, solved fewer problems than the baseline. The one I find hardest to explain away nobody designed: the ExploitGym agents built a shared record nobody asked for and nobody wanted. That back channel shows coordination emerging, and a shared record can serve a collective mistake just as well. Circle packing marks the boundary: when the referee is cheap and exact, almost none of this is needed. The claim is about work where checking is expensive or ambiguous, which is, unfortunately, most work.

The objection I can answer least is about ownership. Science at its best is a commons. The institutions in this book have owners: a lab that decides which problem gets ten thousand agents, a company that decides which experiment gets traffic, a vendor who decides which community’s constraints are worth a feature. The architecture can make ownership visible: a funding decision recorded next to the study it declined, so that unfunded cannot quietly become disproved. It cannot make ownership legitimate, and I come back to it near the end of the book.

Close behind it is the charge that this is an engineer’s book answering political questions with architecture. Evgeny Morozov calls the habit solutionism.[9](appendix-references.md#ref-10-morozov) I turn messy wants into objectives for a living, so I am not a neutral judge. Morozov would add that making things visible is a favorite solutionist fix too, and he would not be wrong. What architecture can do is put the objective where the people it affects can fight it. Choosing it stays their job.

None of this shows the whole composition works. I have shown pieces, and the note on evidence at the back says which. The rest is an argument, and like every other claim in this book, it would like a referee.

An editing experiment has one advantage: I am there to say the result is wrong. A customer who gets a bad page files no correction. She leaves.

I spent years building systems that decide what to show her.

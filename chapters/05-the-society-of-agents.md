# Chapter 5: The Society of Agents

*When the Org Chart Starts Thinking*

Sixteen Claudes were building a compiler.

A few years ago, that sentence would have required several paragraphs of explanation. By the time Nicholas Carlini tried it, the strange part was no longer that the agents could write compiler code. The strange part was watching sixteen capable agents gradually become an organization.

The goal was almost offensively ambitious: build a C compiler in Rust from scratch and push it far enough to compile the Linux kernel. Over nearly two thousand Claude Code sessions, the agents produced roughly a hundred thousand lines of compiler code. The resulting compiler eventually built Linux 6.9 on x86, ARM and RISC-V, along with projects such as QEMU, FFmpeg, PostgreSQL and Redis. It was still nowhere near GCC, and one stage of the x86 boot path still depended on GCC, but this was well beyond the kind of toy problem where sixteen agents can succeed by taking sixteen conveniently independent buttons.

The first organization was simple. Each agent worked in its own container with its own copy of the repository. Before beginning a task, it wrote a small lock file describing what it intended to work on. Git synchronized the locks. If another agent had already claimed the problem, the newcomer found something else. When an agent finished, it pulled the latest changes, merged its work, pushed the result and released the lock.

There was no manager assigning tickets and no orchestrator holding the whole compiler architecture in its head. Agents inspected the project, found something useful to attack and left enough information behind for later workers to reconstruct what had happened.

For a while this worked remarkably well, partly because compiler test suites are generous places to employ a crowd. They contain thousands of failures, many of which can be attacked independently. One agent can investigate a parser bug while another works on code generation and a third discovers that a respectable-looking integer conversion has been quietly ruining everybody's afternoon. Once the compiler became good enough to build real programs, SQLite, Redis, Lua and other projects exposed different neglected corners of C.

The project gave sixteen workers sixteen places to think.

Then they reached Linux, and the nice story about parallelism began to fall apart.

Kernel compilation tended to stop at the first serious compiler bug. Several agents would arrive at the same failure, form overlapping theories and make changes that interfered with one another. Nothing had happened to the underlying intelligence. The models had not suddenly become worse programmers. The shape of the work had changed. One narrow bottleneck was now giving sixteen workers one door.

Carlini changed the harness.

GCC became a known-good reference. Most kernel files could be compiled with GCC while selected subsets were compiled using the new compiler. If the kernel still built, suspicion moved elsewhere. If it failed, the search narrowed. Delta debugging later helped isolate failures that appeared only when certain files were compiled together.

One enormous failure became a collection of smaller questions, and the agents could spread out again.

**Same models. Different institution.**

That interests me more than the generic claim that multi-agent systems scale. Task locks reduced duplicated work. Git carried shared history. CI stopped one local improvement from quietly breaking something three directories away. Progress files let fresh agents inherit discoveries from workers whose contexts had already vanished. GCC received special authority for a bounded class of questions. Even the way evidence entered context mattered: enormous logs were better left in files while a smaller representation reached the working agent.

Then specialization appeared. One agent looked for duplicate implementations. Another cared about performance. Another improved generated machine code. Another reviewed the project as a Rust engineer. Documentation became somebody's problem, which is normally the moment you know a civilization has become serious.

At that point it becomes difficult to answer a very ordinary question: where does the knowledge of the compiler project live?

Obviously some of it lives in Claude. But which Claude?

The parser agent does not know everything the performance agent knows. Neither remembers every previous session. Some knowledge lives in code, some in tests, Git history, progress files, task boundaries and conventions. Some lives in GCC, whose behavior the project is willing to trust for certain questions. Some lives in Carlini, who notices that the current organization no longer matches the work and changes it.

Karl Popper had a name for the place where that knowledge lives. Beside the physical world and the world of individual minds he proposed a third, the world of theories, problems, arguments and records: knowledge that exists in books, instruments and institutions and can be examined, criticized and improved by people who did not produce it and are not currently thinking about it. He called it World 3, and argued that most of what humanity knows lives there rather than in anyone's head. The name System 3 comes from somewhere else, but the coincidence is not one I want to hide. The compiler project's knowledge lives in Popper's third world, with one addition he would have enjoyed: this one has a build system, and a test suite through which the first world can still object.

The project knows more than any participant. It can also become wrong in ways no participant intended. A progress file can preserve a bad diagnosis. A specialist can improve its own metric while harming the compiler. A lock that prevents duplicated effort can also prevent a useful second attack. Two agents can appear to confirm one another while both inherited the same mistaken assumption.

The organization can become part of the intelligence. It can also become part of the bug.

One fallible knower can no longer reconstruct every path back to reality; that is where the camel left us. The compiler gives us the small version of that problem. Humans have been living inside the large version for thousands of years.

## When Knowledge Had a Face

Imagine a small human group living before cities, archives and bureaucracies.

Do not imagine stupid people.

A hunter may know an ecology at a resolution that would embarrass a visiting academic. Someone knows which path floods after heavy rain. Someone else knows which plant reduces a fever and which one reduces it much more decisively by killing you. A craftsperson can feel that a material is wrong before she could explain the difference to somebody who has not spent twenty years working with it.

Knowledge had a face. If you wanted to know where animals crossed the river, you asked her. If you wanted to know whether a mushroom was safe, you asked him. Reputation was personal because people remembered who noticed things, who exaggerated and whose previous advice ended with everybody vomiting behind the same tree.

A surprising amount of epistemology can run on faces.

Then scale breaks the arrangement. The village becomes a town. Grain is stored for later. Debts last longer than the conversation that created them. Goods move farther. Workers contribute at different times. Somebody owes something to somebody who is not currently there.

Memory has acquired logistics.

Some of the earliest surviving writing from southern Mesopotamia records grain, commodities, obligations and accounts. Before writing became philosophy or epic poetry, it was already helping institutions remember who had received what.

The mark did not need to be wiser than the clerk. It needed to outlive the clerk.

A conversation exists as long as enough people remember it. A record can confront people who were not there. An obligation acquires a state outside the minds of the people who created it. The institution can coordinate with its own past.

Five thousand years later, a Claude agent writes a note into `progress.md` because the Claude arriving tomorrow will not share today's context.

The technologies are comically different. The pressure underneath them is not. A group has become capable of learning more than its current members can keep in working memory.

Naturally, useless experience survives too. Writing preserves error beautifully. The first person to record the wrong amount of grain in durable clay invented a database bug. A progress file can remember yesterday's bad diagnosis just as faithfully as yesterday's breakthrough.

Remembering is not knowing.

There is a trick in stories about rebuilding civilization from scratch: they usually give you someone who remembers civilization. *Dr. Stone* makes the trick explicit and entertaining. Humanity disappears, one absurdly knowledgeable protagonist wakes up, and the climb back toward industrial civilization is already partly stored inside his head.

Real civilization did not have Senku.

Nobody in a Neolithic village kept a secret roadmap containing writing, standardized measurement, universities, controlled experiments, statistics, semiconductors and CERN. The institutions we now treat as obvious emerged in different places for different reasons. Knowledge moved through Mesopotamian, Egyptian, Indian, Chinese, Greek, Persian, Arabic, African and European traditions. It traveled, disappeared, was translated, modified, reinvented, appropriated and occasionally rediscovered by somebody who received most of the credit.

There is no clean staircase in which one civilization hands the torch of Reason to the next. Societies repeatedly hit limits in collective cognition and improvised ways around them. A local pressure produced a record, office, standard, instrument or procedure. That changed what the society could do, which created new problems, which changed the institution again.

Civilization had no senior architect.

## Strangers Need Standards

External memory solves one problem and immediately reveals another.

A record can preserve the fact that somebody owes ten sacks of grain. What exactly is a sack?

Once exchange extends beyond people who know one another personally, trust cannot remain one giant confidence score attached to a face. Weights and measures tell strangers what a unit means. Coins make value portable. Seals authenticate. Contracts preserve commitments. Courts create procedures for disputes. Offices define authority. Calendars coordinate people who do not share the same immediate world.

Standards make knowledge composable. If my unit of length means something different from yours, our measurements do not travel cleanly. If every workshop names materials differently, useful techniques remain local. If every clerk invents new categories whenever a document arrives, the empire has built a sophisticated machine for rediscovering confusion.

A standard removes a decision from the future. We have decided, for now, not to reopen this question every time.

Seen that way, bureaucracy deserves a better reputation than it normally gets.

Suppose an agent is processing a mortgage application. There are identity checks, compliance requirements, affordability calculations and perhaps a human approval at the end. Some steps may require difficult judgment. That does not mean the identity-checking agent should reach its part of the process, reflect deeply on the social construction of identity and decide the applicant gives off trustworthy vibes.

A workflow is often accumulated experience with some choices removed. Someone already had the argument. Someone discovered the failure. Someone decided that one action requires another pair of eyes. The next person inherits the result as procedure.

That is civilization learning. It is also how civilization acquires scar tissue.

A review gets added after a spectacular failure. Five years later the system is different, nobody remembers the incident, and ten thousand ordinary changes still pass through the review because the procedure survived its reason. The institution remembers. Sometimes it remembers too well.

I learned a version of this in a much less ancient civilization: Amazon.

A customer presses a button and eventually a box appears at a door. Described from high enough up, the company sounds almost embarrassingly simple. Try asking one employee how the whole thing works.

Product information comes from one collection of systems. Search and ranking may involve others. Availability depends on inventory. Price may depend on another stack. Payments, fraud, fulfillment, transportation, customer service and experimentation each have their own machinery. Underneath them sit identity systems, data pipelines, deployment systems, observability, permissions and a geological layer of services whose original authors have moved to another team, company or continent.

Nobody carries Amazon around in her head.

So where does Amazon know how Amazon works?

Partly in people. But also in APIs, ownership boundaries, tests, dashboards, alarms, design documents, code reviews, deployment procedures, operational playbooks, escalation paths and postmortems. It lives in mechanisms that make some kinds of failure visible and some kinds of action difficult.

Amazon likes the word *mechanism*. The useful version of that word is not corporate. A mechanism is an attempt to make a desirable behavior survive the person who first cared about it.

When a serious incident happens, you can tell everybody to be more careful. This is emotionally satisfying and institutionally almost worthless. Or you can change the system: add an alarm, remove a permission, alter a default, create a test, introduce a review, record the failure mode. Make the dangerous action slightly harder and the correct action slightly easier.

The organization has learned when its future behavior changes.

Ancient administrative standards and a deployment guardrail look nothing alike. They belong to the same deeper move: knowledge becomes structure.

## The Society Gets Smarter by Making People Narrower

As societies grow, another strange thing happens.

People become less complete.

This sounds like decline until you notice that incompleteness is one of civilization's great technologies. If every family has to grow food, build shelter, treat disease, make tools, preserve law, defend itself and teach every useful craft to the next generation, nobody gets very deep at anything. Specialization changes the bargain.

The potter becomes better because she does not also have to be the physician. The physician sees enough patients to notice patterns other people never encounter. The astronomer can spend twenty years measuring the sky because somebody else is growing dinner. A legal scholar can devote a career to distinctions everybody else is delighted not to read.

The society gains knowledge by distributing ignorance.

The more civilization knows collectively, the less plausible it becomes for one person to understand the machinery supporting ordinary life. I can take antibiotics without knowing how to synthesize them, cross a bridge without checking the structural calculations and transfer money without understanding the banking system. I can write this sentence on a laptop while being unable to manufacture the processor, build the display, operate the electrical grid, reproduce the battery chemistry or implement most of the software between the keyboard and the pixels.

Capability rises because dependence rises.

Civilization is a trust chain with plumbing.

Large states made this problem visible early. Imperial China governed large populations through records, standardized texts, offices and educated officials operating across distances no ruler could inspect personally. Other intellectual traditions developed different combinations of mathematics, medicine, astronomy, engineering, administration and scholarship. There was no inevitable path from bureaucracy to modern science, and no civilization possessed the final architecture in advance.

An invention is not an institution. A population full of intelligent people is not an epistemic architecture. What matters is how people, tools and incentives are arranged: which observations survive, who gets access to instruments, which questions can become careers, which claims may challenge authority, and which criticism has enough standing to change what happens next.

A hospital makes the same point at human scale.

A patient is not safe because somewhere in the building there is one heroic physician who knows all of medicine. The nurse at the bedside may notice a change first. A laboratory measures something nobody can see directly. A radiologist reads an image. A pharmacist notices that two individually reasonable prescriptions become unreasonable together. A specialist may know one narrow disease better than the attending physician, while the attending physician integrates a picture whose pieces she could not personally produce.

The benefit is not agreement. Quite often they disagree.

The benefit is **structured partiality**. Different people are positioned to see different things. They operate different instruments. They have different failure modes. A lab result has provenance. A drug dose has an authorized range. The radiologist's authority on an image does not make her supreme commander of the hospital.

The hospital knows more than any person inside it. It can also fail in ways nobody intended. A handoff loses context. A copied diagnosis becomes an assumption. A bad measurement propagates. Everyone performs her local job competently while the patient moves through the wrong pathway.

This is already close to the agent problem. A research agent makes a weak assumption. Another receives it as context. A builder implements a coherent solution. An evaluator approves it. Later, two documents repeat the claim because they share the same ancestor, and another agent mistakes repetition for independent support.

Eventually the assumption has code, citations and organizational history. Nobody needed to lie. The institution manufactured the confidence.

We already have the language for this: trust is local. Alberto can be an excellent witness about Rome and irrelevant to compiler optimization. GCC can be a powerful reference for the behavior of C programs without becoming an oracle for compiler architecture. A radiologist can deserve high epistemic standing on one question without inheriting authority over the rest of the hospital.

Who knows what matters. Who sees what matters too.

## A Swarm Should Not Automatically Become a Meeting

The easiest reaction to one unreliable agent is to create five.

This appears to be how humanity invented committees and then, dissatisfied with the original implementation, recreated them in software.

Give one agent the title *Researcher*. Another becomes *Critic*. Another becomes *Verifier*. Put them in a conversation and perhaps reality will be intimidated by the org chart.

Several minds do not automatically produce several sources of evidence. If everyone receives the same framing, reads the same leading explanation, searches the same material and inherits the same assumptions, their errors correlate. Five agents citing the same paper are not five witnesses. Five researchers repeating a claim that traces back to one unsupported source are not corroboration.

Agreement can still be useful. It is simply weaker evidence than the number of speakers suggests.

Some branches therefore need to remain isolated for a while. A critic may need to inspect the artifact before reading the builder's explanation. One researcher may need to develop an alternative theory without first studying the current favorite. A strange branch may deserve another experiment even if nobody believes it is likely to win.

MAP-Elites preserved different regions of a search space because the champion might be sitting on the wrong mountain. At the level of a society, what needs preserving may be a theory about the problem itself. One lineage thinks the bottleneck is data. Another thinks the architecture is wrong. A third thinks both are symptoms because the objective is malformed. Let them collect different evidence and become interestingly wrong in different ways before forcing them into one conversation.

Permanent disagreement would be useless. An institution that never converges is simply a philosophy department with an alarming compute bill.

Independence matters because disagreement can carry information. Eventually, though, disagreement needs something capable of settling at least part of it.

For that we need more than another opinion.

## A Man in a Dark Room

Around the turn of the eleventh century, Ibn al-Haytham worked on a question simple enough for a child to ask and difficult enough to occupy generations of scholars.

How do we see?

Inherited theories included versions in which something traveled outward from the eye toward an object. Ibn al-Haytham developed an account in which light travels from objects toward the eye, combining mathematical reasoning with systematic work on light, reflection and refraction. His *Book of Optics* later circulated beyond the world in which he wrote it and influenced subsequent optical traditions.

For our story, the important part is not that he held a different opinion. He arranged circumstances in which competing accounts had observable consequences.

A darkened room. A small aperture. Controlled rays. Mirrors. Geometry. The setup became part of the argument.

A record preserves what somebody says happened. An experiment gives the world another chance to answer.

We do not ask nature which theory it prefers. We arrange a situation in which different descriptions imply different things should occur, then watch what happens.

Charles Sanders Peirce later argued that this is what separates science from every other way of settling belief, whether by stubbornness, by authority or by what seems reasonable from an armchair: it is the only method whose results are fixed by something other than the believer, and so the only one that can correct itself. I am a pragmatist in his sense throughout this book, and contact with reality, wherever the phrase appears here, means exactly that arrangement: something outside the current explanation is able to make the explanation fail.

Experimental traditions have multiple histories, and what became modern science eventually mixed mathematics, instrumentation, craft, institutions and social practices that no single civilization or thinker possessed in complete form. The pieces accumulated.

The agent version is almost embarrassingly literal. Run the program. Execute the query. Open the browser. Measure the latency. Compile the kernel against GCC. Reasoning has left the conversation. Something outside the current explanation now has a chance to be inconvenient.

But an experiment still has to travel. If I want to challenge your observation, I need to know what you claimed and enough about what you did to try again.

Printing changed that part of the problem. Manuscripts had traveled before it, but slowly and imperfectly. Printing changed the topology of disagreement. More people could possess the same description. Corrections could circulate. So could propaganda and confident pamphlets written by people who had discovered the topic sometime after breakfast. Lower publication cost has always had side effects.

For knowledge, reproducibility of the description matters. A society made only of ephemeral contexts can argue forever and still struggle to accumulate disagreement. The compiler agents needed Git and progress files for the same reason later investigators need durable records: criticism requires something that outlives the conversation.

In the early seventeenth century, spectacle makers in the Low Countries demonstrated devices capable of making distant objects appear closer. Galileo built improved versions and pointed them toward the sky. He reported mountains on the Moon, moons orbiting Jupiter and other observations that complicated inherited cosmology.

Unpack the apparently simple sentence:

> There are moons orbiting Jupiter.

It contains testimony, a telescope, craft knowledge about lens making, assumptions about optics, astronomical background knowledge, an interpretation of the visual pattern, written descriptions and the possibility that somebody else might build an instrument and look.

The observation was already social.

The lens did not hand Galileo uninterpreted reality. It produced a pattern that became evidence through assumptions about optics, geometry and what the device was doing. That does not make the observation arbitrary. It makes the chain visible.

A new instrument creates new facts and new ways to be wrong about facts. Was the lens distorting the image? Was the point of light actually there? Could another observer reproduce it? Did the operator know what she was doing?

The same questions appear when an agent acquires a browser, retrieval system, benchmark, simulator or custom tool. We have not merely increased capability. We have introduced a new witness. How reliable is it? On which problems? What does it measure? When does it fail? Who calibrated it?

A broken tool is not external grounding. It is a very efficient route to externally generated nonsense.

## When Curiosity Became Procedure

In 1660, a group that became the Royal Society formed in England. Its members observed, corresponded, experimented, argued and eventually published. *Philosophical Transactions* appeared a few years later.

There was no moment when somebody installed `science-1.0`. A collection of institutional devices accumulated instead.

A person reports an observation. The report circulates. An apparatus is described. An experiment may happen in front of witnesses. Someone elsewhere tries to repeat it. A journal creates public memory and a priority mechanism: this person made this claim at this time. Reputation develops around investigators, instruments and procedures. The question *did this happen?* acquires machinery.

The machinery was never clean. Access was unequal. Reputation and social power affected which claims traveled. An experiment could be reproducible in principle and still remain weak if the person who saw it lacked a press, patron, society, instrument or enough standing to make other people care.

Robert Boyle's air-pump experiments are useful precisely because the procedure was imperfect. The pump was difficult to build and operate. Replication was not a button. If somebody failed to reproduce a result, several explanations remained possible: perhaps Boyle was wrong; perhaps the pump leaked; perhaps the operator lacked some crucial skill; perhaps the written procedure omitted something everyone in Boyle's room had treated as obvious.

Reality had pushed back against the package. It had not highlighted the guilty component.

Software engineers know this sensation. A failing integration test proves the system is broken somewhere. Wonderful. You now have debugging.

So the institution needs archaeology. Which instrument produced the measurement? Which analysis transformed it? Which assumptions were required? What was actually observed and which interpretation was added afterward?

In an agent system, this becomes provenance around a claim, an assumption graph, a trace. Without the history, reality can tell us we are wrong while leaving us remarkably creative about which part of the system deserves blame.

Medicine later made this kind of self-restraint even more explicit. In randomized trials, allocation procedures are designed partly to stop the investigator's own preferences from deciding who receives which treatment. Sometimes bureaucracy is epistemology with a clipboard.

Knowledge is no longer merely a proposition attached to a prestigious person. It increasingly comes with a route through which someone else might expose the claim to the world again.

A trust chain has acquired an escape hatch.

## The Org Chart Becomes Part of the Experiment

Return to the agents.

Suppose one agent proposes a hypothesis, another designs an experiment and a third evaluates the result. Good.

Now suppose all three inherited the same hidden assumption. The experiment fails. Which component changes?

The hypothesis? The measurement? The experiment? The analysis? The evaluator? The background model everyone forgot was an assumption at all?

Reality does not care which file contains the variable named `hypothesis`. It pushes back against the arrangement as a whole.

Organization is now epistemic. Who sees which evidence? Which roles are allowed to modify the evaluator? Which branches share context? Who can stop deployment? Which result is allowed to become everybody else's premise?

Modern agent systems can increasingly make some of these choices dynamically. One problem may need several independent investigations; another a specialist and verifier; another parallel workers around separable components.

The bureaucracy can be temporary; the org chart can change with the problem. **Organization itself has entered the search space.**

Whoever shapes the organization also shapes what it can discover.

Imagine research program A is currently ahead and has twelve agents. Program B looks weaker and has one. Where does agent thirteen go?

The natural answer is A. But the answer can become self-reinforcing. More agents produce more experiments. More experiments produce more evidence. More evidence raises confidence. Confidence attracts more resources. Eventually the leading theory owns the building.

The current best explanation and the best use of the next unit of investigative capacity are not necessarily the same question. A weak theory may deserve another experiment because it explains the one anomaly the dominant framework cannot touch. A critic whose objections never change allocation is not really part of the epistemic institution. She is doing quality-assurance theatre.

Compute allocation is epistemic policy. So is memory. So is context sharing. So is credit. Who receives the capacity to generate evidence partly determines which possible truths the institution can afford to discover.

Kevin Zollman and others have modeled this formally: simulated communities of scientists in which the structure of communication decides whether the group converges on the truth or on the first plausible answer, and in which a less connected community sometimes does better, because a bad early result does not spread as fast. That is the isolation principle with a proof attached, and it makes the question of agent thirteen a question about topology, not only about budget.

Human science has never escaped this problem. It has simply had much longer to argue about it.

## Science Gets Bigger Than the Scientist

Accumulated knowledge eventually destroys the world of the universal expert.

Newton was extraordinary. He transformed mechanics and celestial theory, contributed profoundly to optics and mathematics, and ranged across subjects with a seriousness that feels almost fictional today.

In January 1697 he was running the Royal Mint, chasing counterfeiters and recoining the currency, when a problem arrived from Basel. Johann Bernoulli had challenged the mathematicians of Europe to find the curve along which a bead slides fastest between two points, and had extended the deadline, it seems, in the hope of embarrassing Newton. Newton came home at four in the afternoon, solved it before going to bed, and sent the answer to the Royal Society without his name on it. Bernoulli recognized the author anyway. *Tanquam ex ungue leonem*: as the lion by its claw.

The story is usually told as a story about Newton. I think the more important part is that Bernoulli's question could reach Newton at all. A challenge posed in Switzerland was printed in a Leipzig journal, read in London, answered overnight, published and attributed within weeks, and the attribution rested on a shared mathematical language precise enough that a style could be recognized like handwriting. Most of that machinery had not existed a century earlier.

Even the lion becomes less solitary when you zoom out. He inherited astronomical observations made by others. He worked inside mathematical traditions with long histories. He argued with contemporaries. The *Principia* traveled through an institutional world that included correspondence, publishers and people willing to finance the book.

Genius mattered enormously. So did the network that allowed genius to begin from accumulated work rather than from dirt.

Then scientific success made the network more necessary. Laboratories and disciplines specialized. Experimental techniques required training. Journals multiplied. Instruments became more complicated. Fields developed technical languages that excellent researchers next door could not read without help.

Science became more powerful by making scientists less interchangeable.

Tacit knowledge mattered too. Reading that an instrument works is different from knowing how to make it work. You enter a laboratory and learn that a vibration nobody mentioned in the paper destroys the measurement, or that one step has to be performed in a way the written procedure describes with the scientific equivalent of “cook until done.”

The institution teaches hands as well as concepts.

And because no researcher can personally reproduce every result she depends on, trust becomes more important at exactly the moment standards of evidence become stronger. A physicist relies on chemistry. A doctor relies on laboratory assays. An engineer relies on material specifications. A scientist cites work she could not reproduce from raw materials with the rest of her career and a very generous research grant.

Rigor at scale is not the elimination of trust. It is the organization of trust.

On 4 July 2012, the ATLAS and CMS collaborations at CERN announced observations of a new particle consistent with the Higgs boson.

Who discovered it?

Try pointing to the person.

The papers had thousands of authors. The detectors contained technologies developed over years by specialists in different countries and institutions. The accelerator depended on another enormous technical organization. Data traveled through distributed computing systems. Calibration, trigger systems, detector physics, statistical analysis, software and theoretical interpretation each required knowledge nobody possessed end to end.

No physicist woke up that morning capable of rebuilding the Large Hadron Collider, recalibrating every detector, verifying every line of analysis software, reconstructing the electronics supply chain, re-deriving the theory and independently checking every collision event before breakfast.

And yet the result was not therefore rumor.

The knowledge was carried by a structure. Calibration procedures had histories. Software was validated. Analyses were reviewed internally. Different detector systems constrained one another. ATLAS and CMS provided partially independent routes toward the same underlying phenomenon. Statistical conventions defined how much evidence justified using a word as consequential as *discovery*.

Underneath all the institutional machinery, the apparatus produced traces nobody could vote into existence.

A modern experiment is a society organized around an argument with reality.

Early in human history, much of what a community knew could plausibly be attached to identifiable people: ask her, she has seen the valley. As knowledge expanded, societies externalized memory into records, coordination into standards, expertise into specialized roles, perception into instruments and criticism into procedures.

Eventually we built institutions capable of producing knowledge no member could personally verify in full.

That is dangerous. A bad calibration can propagate. A shared assumption can synchronize thousands of competent people. Prestige can suppress criticism. Funding can steer a research program. A procedure can survive long enough to become ritual. A statistically beautiful answer can solve the wrong problem.

But without the machine, we lose the knowledge too.

There is no lone human replacement for CERN. There is no polymath who can personally substitute for modern medicine. There is no chief scientist carrying scientific civilization around in her head.

Civilization knows through composition.

Now go back to the compiler.

## Sixteen Claudes, Again

Task locks. Git. CI. Progress files. Tests. A trusted reference compiler. Specialists. A harness that converts one global failure into many smaller investigations.

At the beginning of the chapter these looked like practical tricks for coordinating coding agents. They look different now.

One worker leaves a result another worker will trust. A passing test gives a claim standing. An oracle receives special authority for a bounded class of questions. A progress document becomes institutional memory. Specialization creates local expertise. The harness determines which evidence reaches which investigator.

They are primitive institutions.

A Mesopotamian accounting tablet is not `progress.md`. A telescope is not a compiler test. The Royal Society is not sixteen Claudes running in containers. CERN is not a multi-agent framework. Trying to line the nouns up perfectly would be silly.

The verbs are harder to ignore.

Preserve what happened so the next investigator does not begin from zero. Create standards so results can travel. Specialize. Give authority locally. Keep some investigators independent. Build instruments when existing perception cannot answer the question. Construct procedures capable of embarrassing a persuasive theory. Let claims carry enough history that a later investigator can ask where they came from. Allow several explanations to survive long enough to become meaningfully different. Remember failures. Notice anomalies. Sometimes discover that the instrument was wrong, sometimes that the theory was wrong, and sometimes that the procedure everyone trusted is itself the thing that needs to change.

By now the agent architecture has acquired persistent records, standards, instruments, specialization, local authority, independent lineages and procedures for criticism. More strangely, it has acquired the possibility that the whole arrangement can know something none of its members can know alone.

I thought I was designing a society of agents.

Humanity had already spent centuries building a society of fallible knowers.

We call it **science**.

**System 3 is science.**

Not science as a pile of papers, or as “give the agent access to arXiv,” or even as the familiar classroom sequence:

`Question → Hypothesis → Experiment → Conclusion`

Useful, but much too small.

I mean science as a civilization-scale cognitive technology: laboratories, instruments, notebooks, mathematics, journals, arguments, standards, archives, statistics, specialists, engineers, technicians, rival programs, reputation, criticism, replication, negative results, anomalies, and the occasional researcher who spends six months developing an elegant theory before discovering that the cable was loose.

Historical science is messy. It contains hierarchy, prestige, fashion, fraud, publication bias, career incentives, bureaucracy and communities capable of becoming remarkably sophisticated about the wrong thing. That is part of why it is a useful model for a system built from fallible agents rather than imaginary perfect reasoners.

What matters is not that science abolished error. Observations can outlive observers. Instruments extend perception. Expertise becomes local. Claims travel through trust chains. Critics can attack conclusions they did not produce. Rival programs can survive long enough to disagree meaningfully. And through the machinery there remain routes—imperfect, delayed, expensive and sometimes politically obstructed—through which reality can still make the institution uncomfortable.

That is the architecture I want from System 3: not an omniscient model, but a society of fallible minds that can remember without turning memory into scripture, trust without making authority universal, specialize without losing all connection between specialties, and disagree without putting everybody in the same meeting until the group reaches consensus from exhaustion.

A society that can build a new instrument when the old one cannot see what matters, discover that its trusted instrument was the thing that failed, and eventually change its own institutions when they stop earning their authority.

Science did not solve these problems. It built machinery for continuing to have them productively.

Apparently we are porting it.
# Chapter 5: The Society of Agents

*When the Org Chart Starts Thinking*

Sixteen Claudes walk into a kernel.

> [VISUAL — chapter opener. Sixteen identical small robots in a queue at a single door labelled `linux/`. The door is human-sized; the queue is not. One robot at the back is reading a file labelled `progress.md`. Line-art, no color, half page.]

A few years ago that sentence would have looked absurd. By the time Nicholas Carlini tried it, the strange part was no longer that agents could write compiler code. The strange part was watching sixteen capable agents slowly turn into an organization.

The goal was almost offensively ambitious: a C compiler in Rust, from scratch, with no dependency beyond the standard library and no internet access, pushed far enough to compile the Linux kernel. Carlini had been using the task as a benchmark across generations of Claude models. Earlier versions could barely produce a working compiler. The next passed large test suites but could not build major real projects. Then, over nearly two thousand Claude Code sessions and two weeks, sixteen agents produced roughly a hundred thousand lines of compiler code that built Linux 6.9 on x86, ARM and RISC-V. It also compiled QEMU, FFmpeg, PostgreSQL and Redis.[^carlini]

It was nowhere near GCC. Its output ran slower than GCC with optimizations switched off, and it still borrowed an assembler and linker. One stage of the x86 boot path called GCC because the agents' own sixteen-bit code came out at nearly twice the size the kernel allows. Still, this was well beyond the kind of toy problem where sixteen agents succeed because the work happens to split into sixteen independent pieces.

The harness grew around their failures.

The first was that a coding agent stops. Give it a long problem and it solves part, then waits for a human to say what's next. The fix was simple: a shell loop. When a session ends, start another with the same prompt, forever. That solved waiting, mostly. On one occasion an agent ran `pkill -9 bash`, killed its own loop and left the project, which turned out to be one way a worker in this organization could retire. I have wanted to do the same from time to time. Luckily, I lack root access.

The loop still left one agent doing one thing at a time. So there were sixteen containers, each with its own clone of the repository, and a new problem: two agents could pick the same task. Before starting, an agent wrote a small lock file naming what it intended to work on. Git synchronized the locks, and if two agents claimed the same problem the second had to pick another. When an agent finished it pulled, merged, pushed and released the lock.

There was no orchestrator. Carlini had specified parts of the skeleton in advance: how the compiler would represent code internally, using an SSA intermediate representation, and that it should support multiple backends. But no agent held the current state of the project in its head, because no agent had a head that lasted longer than a session. Each fresh container spent a large part of its budget working out where the project stood. So the prompt told every agent to maintain READMEs and progress files and to update them often, because the next worker would arrive knowing nothing.

Two other limitations shaped the work. Agents have a poor sense of elapsed time, so left alone they could spend hours running tests instead of fixing anything. The harness offered a fast mode that ran a one or ten percent sample. Each agent got a repeatable sample so it could compare results; different agents got different samples, spreading their attention across the suite. The other problem was that test output flooded context, and a context window full of logs is a worker who has forgotten what it was doing. So the output went to disk, with a few lines of summary left behind and every error on its own greppable line.

> [DIAGRAM — the harness as a ladder. Five rungs, each a pair: left side the failure ("agent stops", "two agents, one task", "fresh container knows nothing", "runs tests forever", "logs flood context"), right side the fix ("loop", "lock file", "progress.md", "sampled tests", "logs to disk"). Two more rungs below show "one global bottleneck → GCC-assisted isolation" and "new work breaks old work → CI". Present as a map of problems and responses, not a dated chronology.]

For a while this worked remarkably well, partly because compiler test suites are generous places to employ a crowd. A new compiler fails thousands of them, independently. One agent can investigate a parser bug while another works on code generation and a third discovers that a respectable-looking integer conversion has been quietly ruining everybody's afternoon. Once the compiler could build real programs, SQLite, Redis and Lua each exposed a different neglected corner of C. Sixteen agents, and always more than sixteen things to do.

> [VISUAL — Linux as the boss level. The sixteen small robots have been walking across a wide map of many small doors (test cases, then SQLite, Redis, Lua). The map narrows to a single enormous gate, Bowser-castle scale, with a penguin silhouette on it. All sixteen are bunched in front of it. Game-map style, one color accent.]

Then they reached Linux.

The kernel is not thousands of tests. It is one enormous test, and compilation stopped at the first serious compiler bug. Agents arrived at the same failure, formed their own theories and pushed changes over one another's. The locks could separate named tasks; they could not turn this bottleneck into sixteen different investigations. The standing instruction to find something useful and attack it kept pointing everyone at the same place.

The models had not changed. The problem had, and the organization that had worked so well on a test suite was now getting in the way. The organization was the bug.

> [VISUAL — the GCC oracle. The kernel drawn as a wall of bricks. Most bricks are grey and stamped GCC; a scattered handful are colored and stamped with the new compiler's mark. A robot tests whether the wall stands. Three panels show the colored set shrinking as the failure is isolated.]

Carlini changed the harness. Most of the kernel was compiled with GCC and only a random subset of files with the new compiler. A successful boot cleared that combination for that run. A failure gave the agents a smaller set to investigate, replacing more files with GCC output to narrow the search. Sixteen agents could again work on different files. A later pass with delta debugging helped isolate combinations that failed together even though their components worked separately.

The harness kept changing. Near the end, new features started breaking old ones, so Carlini added a continuous integration pipeline with stricter checks on new commits.

Specialization addressed work the next failing test would never ask anyone to do. LLM-written code kept re-implementing what already existed. Someone needed to look for duplicates. Someone needed to improve the compiler's own speed, and someone else the quality of the code it emitted. Carlini assigned those roles, along with an agent to review the structure as a Rust developer and another to work on documentation, which is normally the moment you know a civilization has become serious. The crowd had become a staff.

Look at the harness and every part carries the mark of a problem. Two workers reach for the same task, so there is a lock. A worker arrives with no memory, so there is a progress file. New features break old ones, so there is CI. Linux stops the whole crowd, so the harness learns to split it into smaller questions. Carlini deliberately built the repairs; the work kept revealing which repairs the organization needed. None of the agents arriving on the last day needed to have lived through that history. The history was in the structure.

Same models. Different institution.

That interests me more than the generic claim that multi-agent systems scale. I have watched the same thing happen to teams of people, where it goes by the less glamorous name of reorganization, and nobody writes a blog post.

---

> [VISUAL — Popper peering over his glasses at three small planets floating below him: one rocky and physical, one a cloud of thought-bubbles, one built of books, tablets, instruments and a Git commit graph. Portrait-caricature style.]

So where does the knowledge of the compiler project live?

Obviously some of it lives in Claude. But which Claude?

The parser agent does not know what the performance agent knows. Neither remembers the previous session, and neither will exist next week. Some knowledge lives in code, some in tests, Git history, progress files, task boundaries and conventions. Some lives in GCC, which the project trusts as a reference for particular questions. Some lives in Carlini's head; he is the one who notices that the organization no longer fits the work and changes the harness.

In 1967 Karl Popper gave a lecture called *Epistemology Without a Knowing Subject*, and meant it literally. Beside the physical world and the world of individual minds he proposed a third: the world of theories, problems, arguments, and the records that carry them. Knowledge there can be examined, criticized and improved by people who did not produce it and are not currently thinking about it. He called it World 3. The compiler project is a small World 3 with a Git remote.[^popper-world3]

Popper insisted on two properties of that world. We make it, but we do not control everything that follows from it: once a theory is written down it has consequences its author never saw, and problems nobody has noticed yet are already sitting in it. And it keeps our mistakes as carefully as our discoveries. A refuted theory is still a citizen of World 3; it just has a bad reputation.

His own example was a book of logarithm tables, computed by a machine, printed, and never opened by anyone. Does it contain knowledge? Popper said yes. What matters is that someone could read it, not that anyone has. Now look at the compiler's progress files, written by Claudes that no longer exist for Claudes that do not exist yet. In between, they sit on disk, right or wrong, with nobody looking.

The project also has a way to challenge some of what those files say without waiting for a person to read them. An agent claims a bug is fixed; the build fails. Reality has a commit hook. The hook can be wrong too, but the agent's account of its own success no longer gets the last word.

The project can also become wrong in ways no participant intended. A progress file carries a bad diagnosis into later sessions. A specialist improves its own metric while degrading the compiler. A lock prevents duplicated effort and also prevents a useful second attempt. Two agents confirm each other while both inherited the same mistake from the same file. Carlini's closing worry was that passing tests can make unfinished work look complete.

The question underneath all of this is how a population of fallible knowers can build knowledge together without losing contact with the world. The compiler is the small version, and it came with a luxury: one person who could step back from the agents' work, see that their institution no longer fit it, and rebuild the harness.

Human civilization has been living inside the large version for thousands of years, with no one standing outside it.

> [VISUAL — closing image for the section. Left panel: sixteen robots inside a glass box; a human hand outside adjusts a dial on the box. Right panel: a crowd of thousands of tiny humans inside a much larger box; the box's edges fade into the page. Same drawing style as the opener.]

## Civilization Had No Senku

In 2019, a green light swept across the Earth and turned humanity to stone.[^stone-date]

People were caught in classrooms, at kitchen tables, crossing streets. Aircraft continued without pilots. Fires burned through neighborhoods where nobody could raise an alarm. The machinery kept running until it needed something from us.

Over the centuries, rain entered the roads and roots widened the cracks. Bridges fell. Forests grew across the places they had connected. Buildings began the long process of becoming landscape.

In the spring of 5738, the stone around a boy's body broke apart.

He emerged into a forest with the knowledge of a civilization that could no longer supply him with breakfast. He needed shelter, food and fire. Much of what he knew would remain useless until he could make the equipment required to use it.

Later, in a village of people born into this world, he met a young woman named Ruri who was seriously ill. He proposed making a medicine for her.

There was no pharmacy to raid. The ingredients had to be obtained or produced, and the work required equipment the village did not possess. Before the medicine could exist, they needed glass.

Knowing how to produce it was only the beginning. Someone had to shape it into useful vessels. An elderly craftsman named Kaseki joined the effort, bringing the skill of a lifetime spent making things. The boy could explain what they needed; Kaseki could make it.

The villagers gathered materials and learned unfamiliar processes while Ruri remained ill. Eventually they completed a sulfa drug and gave it to her. She recovered.

The boy's name is Senku, and we have been following *Dr. Stone*.[^stone]

Popper had imagined a related catastrophe in the same 1967 lecture. Destroy our machines and tools, along with our knowledge of how to use them, but preserve the libraries and our capacity to learn from them. After much suffering, civilization could recover. Destroy the libraries too, he argued, and its return would take many millennia. Popper left the libraries standing. *Dr. Stone* puts one inside a teenager.

Senku remembers a world in which the medicine already exists. He can work backward from it, identifying materials and processes worth pursuing. His companions still have to make those steps work with what they have, but they do not have to discover the entire possibility of modern medicine along the way.

Real civilization had no Senku, and nobody standing outside it with the roadmap.

A potter learned from clay, fire and vessels that cracked. She tried a change, repeated it when it worked, then taught it to an apprentice. When his pot cracked, she recognized something he had done that morning. He remembered doing it, remembered her warning, and now had an expensive reason to pay attention. It took several more firings before his hands could feel the difference she noticed immediately. When he became a teacher, he passed on what he had learned, including precautions he did not entirely understand, because the last person who omitted them had ruined a firing.

Knowledge had a face. You knew whom to ask and remembered what happened when you listened. Senku had the chemistry; Kaseki had the hands. Whatever they failed to pass on could die with them.

Her vessels, meanwhile, ended up in storehouses that needed a memory beyond particular people. Grain arrived from different fields, portions were distributed, obligations remained. The person who witnessed a delivery might be absent when someone disputed the amount.

By the late fourth millennium BCE, people in southern Mesopotamia were recording economic information in clay, including accounts concerning grain. The material that made the vessel could also keep an account of its contents. A new clerk could consult a transaction he had never witnessed, and the person who delivered the grain could discuss it with him over a record they could both inspect.[^writing]

The mark did not need to be wiser than the clerk. It needed to outlive him.

The institution could now consult its own past. That brought new responsibilities: learning the marks, agreeing on their meanings and settling disputes when two records told different stories.

The clerk could also enter the wrong amount, and his successor could copy it faithfully. The clay had preserved what it was given.

Remembering is not knowing.

## Strangers Need Standards

The clay could preserve the wrong figure. It could also preserve the right one in a unit nobody else used.

A record says somebody owes ten sacks of grain. What exactly is a sack?

In 221 BCE the king of Qin conquered the last of the six rival states and became the First Emperor. His new empire contained regional writing traditions, currencies, weights and measures. Conquest had put strangers under one ruler. It had not made their accounts agree.

Under the emperor and his chancellor Li Si, the state imposed common standards. Some surviving bronze measures carry the imperial edict that ordered the work. The vessel tells you how much it holds and, on its side, who decided. You can hold one and read the decision.[^qin]

Then the ambition to settle disagreement reached the past. In the account preserved by the historian Sima Qian, Li Si proposed in 213 BCE that certain private histories and philosophical texts be burned. Copies held by court scholars were exempt, along with useful technical works. A person could consult the past, provided the court controlled which past was available. The proposal was meant to stop old books from becoming arguments against the present ruler.[^qinbooks]

The bronze measure allowed two clerks to discover that their accounts disagreed. The order against the books tried to take that possibility away from the emperor's critics.

A standard removes a decision from the future. We have decided, for now, not to reopen this question every time. Once exchange extends beyond people who know one another, the stranger reading the tablet needs to know what a sack is, what a seal proves, whose account wins when two disagree. Standards make that exchange possible. They can also make a decision difficult to challenge long after the people who made it have gone. The Qin measure was not the correct measure. It was the one backed by the state.

Seen that way, bureaucracy deserves a better reputation than it gets. A workflow is accumulated experience with some choices removed. Someone already had the argument, or discovered the failure, or decided that one action requires another pair of eyes, and the next person inherits the result as procedure. Amazon calls this a *mechanism*, and the useful sense of the word is not corporate: a mechanism is an attempt to make a desirable behavior survive the person who first cared about it.

When something goes wrong you can tell everyone to be more careful, which is emotionally satisfying and institutionally almost worthless, or you can change the system so the dangerous action is slightly harder and the correct one slightly easier. The organization has learned when its future behavior changes.

That is how an institution learns, and it is also how it scars. A review gets added after a spectacular failure. Five years later the system is different, nobody remembers the incident, and ten thousand ordinary changes still pass through the review because the procedure survived its reason. The apprentice kept a precaution he never understood. The institution can do the same, with a much larger kiln.

A tablet, a bronze measure, a deployment guardrail: knowledge becomes structure. It allows work to pass between strangers. Now the strangers can each learn something the others do not.

## The Society Gets Smarter by Making People Narrower

Then Amazon made me an offer, and the offer was reviews.

Before that I had run the technology of a smaller e-commerce company, fewer than a hundred people for all of it: catalogue, search, payments, the warehouse software, the emails that went out at night. I knew every system because I had to. Amazon wanted me for the text under the fold. The fold is a newspaper word: the important story goes above it, then you fold the paper under your arm and forget the rest. On a product page, reviews were the rest. The organization whose applied science I would lead was more than a hundred people, which was more than the entire company I had just left, and I remember sitting with the offer and feeling faintly embarrassed for everyone involved. What could a hundred people possibly do with a text box?

Here is what a text box contains. A grill weighs thirty kilograms. Is that good for a barbecue party? The catalogue cannot tell you; it can tell you thirty kilograms. Two thousand reviews can tell you, and they can tell you who bought it, why, what went wrong at the first party, what they wish they had known, and the small psychology of a person who wanted to feed twelve friends and got it slightly wrong. Once you look at nothing else, the text box turns out to hold the buyer's whole story.

And the story wants work. How do you ask for a review without begging? How do you help a person who has never written anything write one? How do you summarize two thousand of them into a paragraph, find the useful ones, catch the fakes, carry them across nine languages, use them to explain a catalogue written by a manufacturer, feed them into search so that "good for parties" finds the grill, find the one review in ten thousand that a marketer could build a campaign on? A hundred people was not enough to cover the space. At the smaller company, reviews had been one engineer's afternoon.

The potter became better because she was not also the physician. Specialization gives people time to encounter differences a generalist may never notice. The society gains knowledge by distributing ignorance, and every organization, industry and science that gets big makes some version of that bargain: people go narrow, and the narrow place turns out to be bottomless.

Try finding one person who knows how to make the phone in your pocket, from raw materials to a working device. The glass, the chip design, the fabrication equipment, the lenses inside that equipment, the assembly and the software belong to different bodies of expertise. The company whose name is on the back must coordinate work it could not reproduce inside one person's head.

Capability rises because dependence rises. Civilization is a trust chain with plumbing.

On a March morning in 2005, in an English hospital, Elaine Bromiley, a healthy woman of thirty-seven, was put to sleep for a routine nasal operation. The anaesthetist could not get a breathing tube into her airway. He could not ventilate her adequately either. He called for help, and help came: a second anaesthetist, then the surgeon, all consultants, with decades of experience between them.

Within four minutes she was visibly blue. Her oxygen saturation had fallen to forty percent. The doctors kept trying to get the tube in.

There was a procedure for this emergency: when neither intubation nor ventilation works, make a surgical airway. A nurse fetched the equipment. It was in the room. Two nurses later said they knew what needed to be done but did not know how to broach the subject. The three consultants, meanwhile, remained fixed on intubation. They had lost track of the time and of how long Elaine had been without enough oxygen.

The people with the most authority kept attempting the same solution. The people who saw the need to change course could not make that knowledge change what happened to her.

Elaine never regained consciousness. She died thirteen days later.[^bromiley]

Her husband, Martin, was an airline pilot. The surgeon wrote to him that he still could not see how they could have anticipated or avoided what happened. Martin wanted an investigation. In aviation, you investigated a disaster so that the next crew did not have to learn it again.

The independent review found a pattern his industry knew painfully well. Skilled people had become absorbed in an attempted solution while the situation around them changed. Nobody managed to interrupt it. Even who was supposed to be in charge was disputed. Aviation had spent years developing ways for crews to recognize this pattern, challenge one another and change course. Technical competence alone had not been enough there either.

A hospital needs people who see different things. The nurse at the bedside, the radiologist reading an image and the surgeon do not become interchangeable because they share a patient. Their authority has to follow what they know, and their observations need a way to interrupt someone else's plan. The expertise in Elaine's theatre was real. So was the failure to use it.

The potter's mistakes cracked in her own kiln. A specialist's mistakes travel, and each person who receives one may have good reason to trust it.

Who knows what matters. Who sees what matters too.

## A Swarm Should Not Automatically Become a Meeting

Robert Millikan watched tiny drops of oil fall between charged plates. He timed their motion, changed the electric field and watched them again. From the balance between gravity, electrical force and the resistance of the air, he could work out how much charge a drop carried. The charge came in steps. Measure those steps carefully enough and you could find the charge of a single electron.

The number he published in 1913 was slightly too small, because the viscosity of air he used was slightly wrong. It was a very good number for its time. It became the number.

Feynman later described what happened to measurements that followed it: they crept upward toward the accepted value. Why so slowly? In his telling, a laboratory that got an answer close to Millikan's could write it up. An answer farther away sent the experimenter back to the apparatus, looking for what had gone wrong. The inherited number had become part of the method for deciding which results deserved to survive.[^millikan]

Meanwhile, X-rays offered a way to investigate the spacing of atoms in crystals, and from that spacing physicists could estimate the electron's charge by another route. Those measurements helped expose the discrepancy. Their apparatus had problems of its own, but the viscosity of air was not one of them. No amount of respect for Millikan could make a crystal inherit that particular mistake.

That is what a second witness is for. She has to be capable of being wrong differently.

The easiest reaction to one unreliable agent is to create five. Give one the title *Researcher*, another *Critic*, another *Verifier*, put them in a conversation, and perhaps reality will be intimidated by the org chart. Humanity invented committees this way and then, dissatisfied with the original implementation, recreated them in software.

Condorcet supplied a famous mathematical case for crowds in 1785. In the simple version, voters each have the same better-than-even chance of being right, and their votes are independent. Under those conditions, the probability of a correct majority approaches one as the crowd grows. Independence is doing work in that sentence. Voters who simply copy one source copy its mistakes. The crowd is the source, louder.[^condorcet]

Five agents citing the same paper are not five witnesses. Five researchers repeating a claim that traces to one unsupported source are not corroboration. If everyone receives the same framing, reads the same leading explanation and inherits the same assumptions, agreement may tell us more about their starting point than about the claim.

Agreement raises confidence when it would be difficult to explain if the claim were false. When five agents merely repeat one source, we have one witness wearing different coats.

So useful independence has to be built. A critic should see the artifact before the builder's explanation. A second researcher should form a theory before reading the favorite. Different investigators should sometimes use different sources or methods. Separate containers help with some kinds of interference. They do not erase shared training, shared prompts or the bad diagnosis everyone read in `progress.md`.

A strange branch may deserve another experiment even when nobody expects it to win. Kevin Zollman's models show why: under some conditions, less connected communities reach the truth more reliably because an early misleading result cannot bring everyone onto the same path before alternatives have been investigated.[^zollman]

Permanent disagreement would be useless. An institution that never converges is a philosophy department with an alarming compute bill. Independence exists so that disagreement can carry information.

For that we need more than another opinion.

## A Man in a Dark Room

Around the beginning of the eleventh century, Ibn al-Haytham darkened a room, made a small hole in one wall, and placed lamps outside it. On the opposite wall, spots of light appeared. Cover a lamp and its corresponding spot disappeared while the others remained.[^optics]

Vision had been argued about for centuries. One tradition held that the eye sends something out toward the world; another that something travels into the eye. Ibn al-Haytham developed an account in which light travels from objects toward the eye. The dark room did not settle the whole dispute. It made part of the problem manageable: light from separate sources passed through the same opening along paths that could be traced, interrupted and examined.

The setup allowed someone who disagreed with him to do more than disagree.

A record preserves what somebody says happened. An experiment gives the world another chance to answer.

We do not ask nature which theory it prefers. We arrange a situation in which different descriptions imply different things should occur, then watch what happens. Charles Sanders Peirce later argued that this is what separates science from other ways of settling belief, whether by stubbornness, authority or what seems reasonable from an armchair: the answer is constrained by something beyond the believer. I am a pragmatist in his sense throughout this book, and *contact with reality*, wherever the phrase appears here, means that arrangement. Something outside the current explanation is able to make the explanation fail.[^peirce]

An experimental arrangement still has to travel. Someone elsewhere needs enough of the description, the equipment and the skill to make the world answer again. And when the instrument shows something nobody has seen before, the observer has two things to explain: the discovery and why anyone should trust the device that produced it.

In March 1610 Galileo published a short book announcing, among other discoveries, four moons orbiting Jupiter. The next month he took his telescope to Bologna. Through the instrument, an earthly object could look wonderfully close. Point it at Jupiter and some observers could not find the moons Galileo said were there. Martin Horky, an assistant to the astronomer Giovanni Magini, reported that the device worked on earth and deceived in the heavens.[^galileo]

He was wrong about the moons. But the question was reasonable. Unpack the sentence *there are moons orbiting Jupiter* and it contains a telescope, the craft of grinding lenses, assumptions about optics, an interpretation of points of light, and the possibility that somebody else might build an instrument and look. A lens that made a distant church appear closer had not, by that fact alone, established the reliability of everything it showed in the sky.

Later that year Kepler looked through another telescope and saw the moons himself. A flaw in Galileo's lens now had a harder time explaining the result. The two observers still shared assumptions about light and astronomy, but the claim no longer depended on what one man said he had seen through one instrument.

A new instrument creates new facts and new ways to be wrong about facts. Was the lens distorting? Was the point of light there at all? Could another observer reproduce it? Did the operator know what she was doing? An instrument is a witness, and a witness needs a track record.

The agent version is almost embarrassingly literal. Run the program. Execute the query. Open the browser. Measure the latency. Compile the kernel against GCC. Reasoning has left the conversation, and something outside the current explanation now has a chance to be inconvenient. But every one of those actions brings the telescope's questions with it. How reliable is the tool? On which problems? What does it measure, when does it fail, and who calibrated it?

A broken tool is not external grounding. It is a very efficient route to externally generated nonsense.

## When Curiosity Became Procedure

In 1659 Robert Boyle had Robert Hooke build him a pump that could pull much of the air out of a glass vessel. Boyle put things inside it and watched. A candle went out. The sound of a bell weakened. Animals struggled to breathe. He published the results in 1660 with descriptions of the apparatus and numbered experiments, so that a reader in another city could, in principle, build the pump and see for himself.[^boyle]

Thomas Hobbes was unimpressed. A room full of gentlemen could agree about what they had seen and still be wrong. Their conclusion depended on the glass, the pump, the leaks and their eyes. Geometry was supposed to compel assent. Why should anyone outside Boyle's room have to accept the verdict of the people inside it?

The pump gave the objection plenty to work with. In 1661 Christiaan Huygens found that water remained suspended in an evacuated vessel when it was expected to fall. Boyle's group could not reproduce it. For two years they had different facts about what water did when the air was removed. Was the difference in the air, the water, the glass, the pump, the operator or the explanation? In 1663 Huygens came to London, and with his participation the effect was reproduced there. The written account had crossed the sea before him. It had not brought everything the experiment needed.[^huygens]

Reality had pushed back against the package. It had not highlighted the guilty component.

Pierre Duhem articulated the problem in 1906, and Quine later developed a broader version: a test depends on more than the hypothesis under investigation. It depends on instruments, background assumptions and the way the test is carried out. When a prediction fails, logic alone does not identify which part to abandon. Software engineers know the sensation without the names. A failing integration test proves the system is broken somewhere. Wonderful. You now have debugging.[^duhem]

So the institution needs archaeology. Which instrument produced the measurement? Which analysis transformed it? What was actually observed and which interpretation was added afterward? Within a few years of Boyle's book, *Philosophical Transactions* was publishing reports that could outlive the room. Publication established a claim and a date, and gave someone elsewhere a route, however imperfect, to expose the claim to the world again. Reputation gathered around investigators and, more strangely, around instruments and procedures. The question *did this happen?* acquired machinery.

The machinery was never clean. Access was unequal. Standing affected which claims traveled. Replication could be possible in principle and unaffordable in practice. Medicine later made one form of self-restraint explicit: in a randomized trial, the allocation procedure stops the investigator's own preference from deciding who gets which treatment. Sometimes bureaucracy is epistemology with a clipboard.

In an agent system this is provenance around a claim, an assumption graph, a trace. Without the history, reality can tell us we are wrong while leaving us remarkably creative about which part of the system deserves blame.

Knowledge comes with a route through which someone else might make the claim fail again.

A trust chain has acquired an escape hatch.

## The Org Chart Becomes Part of the Experiment

In 1912 Alfred Wegener, a German meteorologist, proposed that the continents had once been one landmass and had drifted apart. He had the fit of the coastlines, matching fossils on opposite sides of the Atlantic, matching rock formations, glacial traces in places that were now tropical. What he did not have was a force capable of moving a continent.[^wegener]

Much of geology declined. Not stupidly: the forces Wegener proposed were too weak, and a continent could not simply plough through an ocean floor that stayed where it was. The fossils needed explaining, but so did the physics. Wegener died on the Greenland ice in 1930, still unable to make the continents move to his critics' satisfaction.

Decades later, ships towing magnetometers began revealing a peculiar pattern on the ocean floor. The rock was magnetically striped. Bands on one side of a mid-ocean ridge had counterparts on the other, recording reversals of the Earth's magnetic field as new crust formed and moved outward. The ocean floor itself was spreading. The continents were passengers.

By the late 1960s, plate tectonics was bringing the scattered observations together. It rescued Wegener's moving continents by changing the machinery underneath them. Nobody had to accept the forces he proposed in order to accept that he had seen something real.

But the stripes had been there while he was alive. Turning them into evidence took ships, instruments, people trained to read the measurements, and someone willing to pay for the voyage. A question cannot attract evidence from an instrument nobody builds.

Return to the agents. Suppose one proposes a hypothesis, another designs an experiment and a third evaluates the result. Now suppose all three inherited the same hidden assumption. The experiment fails. Which component changes? Reality does not care which file contains the variable named `hypothesis`; it pushes back against the arrangement as a whole. Who sees which evidence, which roles may modify the evaluator, which branches share context, which result is allowed to become everybody else's premise: these decisions affect what the system can find out.

Modern agent systems can make some of these choices dynamically. One problem may need several independent investigations, another a specialist and a verifier, another parallel workers around separable components. The bureaucracy can be temporary. The org chart can change with the problem. Organization itself has entered the search space, and whoever shapes it shapes what it can discover.

Imagine research program A is ahead and has twelve agents. Program B looks weaker and has one. Where does the next available agent go?

The natural answer is A, and the answer reinforces itself: more agents, more experiments, more evidence, more confidence, more agents. Eventually the leading theory owns the building, and the weak one has a meteorologist.

Philip Kitcher examined this problem in 1990: how should a community divide its labor among research programs? A community can benefit from some investigators pursuing a less promising approach even when each individual, considering only the best-supported option, would choose the leader. Lakatos supplied another reason for patience: an unresolved anomaly does not, by itself, tell us to abandon a research program. The question is what further work it makes possible.[^allocation]

Compute allocation is epistemic policy. So is memory, so is context sharing, so is credit. Who receives the capacity to generate evidence helps decide which possible truths the institution can afford to discover. The current best explanation and the best use of the next unit of capacity are not the same question. A critic whose objections never change what gets investigated is doing quality-assurance theatre.

Human science has never escaped this problem. It has simply had much longer to argue about it.

## Science Gets Bigger Than the Scientist

Accumulated knowledge eventually destroys the world of the universal expert.

Newton was extraordinary. In January 1697 he was working at the Royal Mint, in the middle of the great recoinage, when Johann Bernoulli's challenge reached him: find the curve along which a bead slides fastest between two points. Bernoulli had given the mathematicians of Europe months to answer. In the account preserved by John Conduitt, Newton came home from the Tower at four in the afternoon, exhausted, and would not sleep until he had solved it. He finished by four in the morning. The answer went to the Royal Society without his name. Bernoulli recognized the author anyway. *Tanquam ex ungue leonem*: as the lion by its claw.[^newton]

The story is usually told about Newton. The more important part is that Bernoulli's question could reach him at all. A challenge posed in Switzerland was printed in a Leipzig journal, read in London, answered overnight and returned to circulation. The attribution rested on a shared mathematical language precise enough that a style could be recognized like handwriting. Even the anonymous answer arrived carrying something of its author.

Genius mattered enormously. So did the network that let genius begin from accumulated work rather than from dirt.

Then success made the network more necessary. Laboratories specialized. Techniques required training. Journals multiplied, instruments grew complicated, and fields developed languages that excellent researchers next door could not read without help. Science became more powerful by making scientists less interchangeable.

Because no researcher can personally reproduce every result she depends on, trust became more important at exactly the moment standards of evidence became stronger. A physicist relies on chemistry. A doctor relies on assays. A scientist cites work she could not reproduce from raw materials with the rest of her career and a very generous grant. John Hardwig called this epistemic dependence, and argued that it is a condition of rational knowledge: a person who refused to believe anything she had not verified herself would know almost nothing.[^hardwig]

Rigor at scale is not the elimination of trust. It is the organization of trust.

On 4 July 2012 the ATLAS and CMS collaborations at CERN announced a new particle consistent with the Higgs boson.[^higgs]

Who discovered it? Try pointing to the person. The papers had thousands of authors. The detectors contained technologies developed over decades by specialists in many countries. No physicist woke up that morning capable of rebuilding the Large Hadron Collider, recalibrating every detector, verifying every line of analysis software and re-deriving the theory before breakfast.

And yet the result was not rumor. It was carried by a structure: calibrations with histories, software that had been validated, analyses reviewed internally, detector systems that constrained one another. ATLAS and CMS supplied different instruments and separate analyses. They shared the accelerator and much background physics, but many mistakes in one detector or analysis would not automatically appear in the other. Their agreement mattered because they were partly independent in ways relevant to the claim.

The year before, another collaboration had shown how much could hide inside a measurement. In September 2011 OPERA reported neutrinos arriving from CERN at a detector in Italy about sixty billionths of a second earlier than light would have. The statistical significance was striking. The collaboration presented the anomaly and asked for further scrutiny.

In February 2012 it reported two possible problems in the timing equipment. A faulty optical-fibre connection could make the neutrinos appear early; an oscillator error pulled the measured time in the other direction. Further investigation and measurements removed the faster-than-light result. The timing equipment had turned an ordinary beam into an apparent challenge to relativity. One of the culprits was a loose cable.[^opera]

The apparatus was still available to inspect after the result became famous. So were the calculations. A loose cable could be found, and finding it could change the answer.

A modern experiment is a society organized around an argument with reality. It is dangerous: a bad calibration can propagate, a shared assumption can synchronize thousands of competent people, prestige can suppress criticism, a procedure can survive long enough to become ritual. But without the machine we lose the knowledge too. There is no lone human replacement for CERN, no polymath who can substitute for modern medicine, no chief scientist carrying scientific civilization in her head.

Civilization knows through composition.

> [DIAGRAM — seven jobs and an eighth. Seven numbered panels inside one frame: "1. Remember — records", "2. Standardize — shared measures and conventions", "3. Specialize — local expertise", "4. Disagree independently — separate investigations", "5. Observe — instruments", "6. Trace — provenance", "7. Allocate — attention and resources". An eighth label, "Revise the institution", has an arrow returning to the frame itself. The arrow changes the arrangement of the panels. This is a map of functions, not a sequence of historical stages. Use the chapter's line-art style.]

Now go back to the compiler.

## Sixteen Claudes, Again

Task locks. Git. CI. Progress files. Sampled tests. A trusted reference compiler. Specialists. A harness that turned one global failure into many small investigations. A human who watched the work and rebuilt parts of the arrangement when it broke.

At the beginning of the chapter these looked like practical tricks for coordinating coding agents. The progress file looks different after the clerk's tablet. It need not be wiser than the Claude; it needs to outlive it. The next worker can remember something it never witnessed. Shared conventions let it compare its work with another's without renegotiating every term. The bronze measure did that for strangers who disagreed about grain.

The specialists make different parts of the project visible. A worker hunting duplicate code sees something the worker chasing a parser bug may pass over, just as the reviews team found a whole field of work inside a text box. Authority follows the question: GCC can settle many disputes about what a C program should do without being asked how the whole project should be run. But agreement among specialists still needs examining. Did they investigate separately, or did the same progress file tell all of them what to think?

Tests let the running program contradict an agent's account of it. Git history gives another worker a route back through the changes that produced the result. The harness decides which failures each agent encounters; the allocation of workers decides which of those failures receives another hour. What the institution remembers, what it can observe and what it bothers to investigate have become things we can change.

The familiar failures come with them. A test suite can keep passing while the thing nobody thought to test quietly gets worse. Separate containers can inherit the same mistake. Carlini had built part of an institution. Some of the rest still lived in his head.

Chapter 4 ended where one agent inherits a claim another has made. A trust chain can tell the receiver where it came from. Someone still has to decide whether to spend the next hour checking it.

A research agent makes a weak assumption. Another receives it as context. A builder implements a coherent solution on top of it. An evaluator approves the solution. Two documents repeat the claim because they share an ancestor, and a third agent mistakes repetition for support. Eventually the assumption has code, citations and organizational history, and nobody lied. The institution manufactured the confidence.

A later investigator needs to be able to pull at that history. Where did the assumption come from? What could show it was wrong? Who has the instrument to check, and will anyone give her time to use it? Preserving the record is only the beginning. The challenge has to be able to change what happens next.

We can test whether these arrangements earn their keep. Keep the model and budget fixed. Give the critic another title, then give her evidence the builder never saw, and compare what she catches. Put a bad diagnosis in a progress file. Compare a system that merely remembers it with one that can trace it to the failed test it misdescribes. Does the mistake survive into the next worker's plan? If these changes make no difference, the architecture owes us an explanation. The resemblance alone has proved nothing.

```{=latex}
\clearpage
```

Give an agent a bounded problem and a referee it cannot charm, and it can find a direction nobody put in the plan.

When judgment is less cooperative, it needs several judges, kept independent and made to use the thing.

A claim needs a route back to something that could have said no.

Sixteen agents need records, standards, specialists and a second witness capable of being wrong differently.

Each piece answered a failure in the work. The institution emerged from the repairs.

What the pieces buy is capacity: a claim that survives its author, an objection that survives the person who would rather not hear it, and things a population can attempt that none of its members could.

I thought I was designing a society of agents.

Humanity had already spent centuries building a society of fallible knowers.

We call it science.

System 3 is science, in that sense and no smaller one. The familiar classroom sequence of hypothesis, experiment and conclusion leaves out most of what makes the work possible. I mean the laboratories, instruments, notebooks, standards, specialists, rival programs, criticism and trust through which a society learns things none of its members could find out alone.

The emergence reaches the architecture itself. The parts are deliberately built, but attempts to make them work together keep exposing the same needs. My claim is that, as we build autonomous AI, we keep rediscovering science as its architecture.

It is messy. It contains hierarchy, fashion, fraud, career incentives and communities capable of becoming very sophisticated about the wrong thing. That is why it is a useful model for a system built from fallible agents rather than imaginary perfect reasoners. A record can be buried; an objection can be ignored. Their survival depends on how the institution works.

One question remains. Who changes the arrangement when the arrangement is the problem?

In the compiler project, that was Carlini. Human investigators have done it too: changed procedures, founded journals, rebuilt institutions and studied the failures of their own methods. We have managed it through argument, reform and the occasional death of an old professor. The difficulty is that the people judging a reform also depend on the institution being reformed. They have learned what a good result looks like inside it. So have the agents.

An agent that changes its evaluator and then receives a better score may have improved the institution. It may also have made the institution easier to please. The evaluator may be part of what needs changing. So may the rules about who is allowed to change it. Whatever the agents revise, something must remain capable of giving them an answer they did not arrange to receive.

Sixteen Claudes built the compiler. Carlini kept rebuilding the conditions under which they could build it.

The rest of this book follows what happens as more of that institution becomes executable: what it can learn to change, and what authority over our lives we are willing to give it.

---

## Notes

[^carlini]: Nicholas Carlini, [“Building a C compiler with a team of parallel Claudes”](https://www.anthropic.com/engineering/building-c-compiler), Anthropic, 5 February 2026. The account distinguishes the compiler's achievements from its dependencies and limitations. The opening groups harness choices by the problems they address; it does not claim that all were introduced in the order narrated.

[^popper-world3]: Karl Popper, “Epistemology Without a Knowing Subject,” lecture delivered in 1967, collected in *Objective Knowledge: An Evolutionary Approach* (1972). See the discussion of World 3, the machine-produced logarithm tables, and the two library thought experiments.

[^stone-date]: The 2019 year is a chronology calculation, not an inference from the anime's release date. In the awakening sequence, Senku gives an elapsed count of 117,354,893,870 seconds and dates his awakening to 1 April 5738. Subtracting that interval places the petrification in June 2019. See *Dr. Stone*, chapter 13, “Stone World the Beginning,” adapted in season 1, episode 5; the sequence and count are also transcribed in [this chapter-by-chapter reading](https://note.com/sasa_yutu/n/n4106cceaec3d). The year agrees with the [series plot chronology](https://en.wikipedia.org/wiki/Dr._Stone#Plot). The opening retains the year without asserting an exact day or time.

[^stone]: Riichiro Inagaki and Boichi, *Dr. Stone* (2017–2022), the Kingdom of Science's effort to produce a sulfa drug for Ruri. The scene is a compressed retelling of that story arc.

[^writing]: Hans J. Nissen, Peter Damerow and Robert K. Englund, *Archaic Bookkeeping: Early Writing and Techniques of Economic Administration in the Ancient Near East* (1993). The potter and apprentice are illustrative characters, not a reconstructed historical incident.

[^qin]: National Palace Museum, collection entry, “Oval Liang Measure by imperial decree of 26th year,” Qin dynasty, 221–207 BCE. The inscription provides a material example of standardization backed by imperial authority.

[^qinbooks]: Sima Qian, *Records of the Grand Historian*, “Basic Annals of the First Emperor of Qin.” The narrative of the 213 BCE order is a later historical account. The extent of its implementation and its contribution to the subsequent loss of texts are disputed; the chapter does not attribute every later loss to it.

[^bromiley]: Clinical Human Factors Group, [written evidence to the House of Commons Health Committee](https://publications.parliament.uk/pa/cm200708/cmselect/cmhealth/1137/1137we25.htm), September 2008, section 4. The account identifies failures of situational awareness, communication, decision-making and leadership in Elaine Bromiley's care.

[^millikan]: Robert A. Millikan, “On the Elementary Electrical Charge and the Avogadro Constant,” *Physical Review* 2 (1913), 109–143; Richard P. Feynman, [“Cargo Cult Science”](https://calteches.library.caltech.edu/51/2/CargoCult.htm) (1974); Raymond T. Birge, “Probable Values of the General Physical Constants,” *Reviews of Modern Physics* 1 (1929), 1–73. Feynman's explanation of the slow correction is presented as his interpretation. The corrections involved several experimental routes, rather than a single decisive encounter. Allegations concerning Millikan's selection of observations remain disputed; see also David Goodstein, *On Fact and Fraud* (2010).

[^condorcet]: Marquis de Condorcet, *Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix* (1785). The paragraph describes the elementary independent-voter case, not a claim that every useful ensemble requires complete independence.

[^zollman]: Kevin J. S. Zollman, “The Communication Structure of Epistemic Communities,” *Philosophy of Science* 74 (2007), 574–587, and “The Epistemic Benefit of Transient Diversity,” *Erkenntnis* 72 (2010), 17–35. The benefits depend on the learning situation and communication structure modeled.

[^optics]: Ibn al-Haytham, *Kitāb al-Manāẓir* (*Book of Optics*), early eleventh century; A. I. Sabra, *The Optics of Ibn al-Haytham, Books I–III: On Direct Vision* (1989). The dark-room experiment illustrates controlled investigation of light propagation; it is not presented as a single decisive refutation of all emission theories of vision.

[^peirce]: Charles Sanders Peirce, “The Fixation of Belief,” *Popular Science Monthly* 12 (1877), 1–15.

[^galileo]: Galileo Galilei, *Sidereus Nuncius* (1610); Johannes Kepler, *Narratio de observatis a se quatuor Iovis satellitibus erronibus* (1611), reporting observations made in 1610. For the reception of Galileo's telescope and the Bologna episode, see Albert Van Helden, introduction and commentary to *Sidereus Nuncius, or The Sidereal Messenger* (1989).

[^boyle]: Robert Boyle, *New Experiments Physico-Mechanicall, Touching the Spring of the Air, and Its Effects* (1660); Steven Shapin and Simon Schaffer, *Leviathan and the Air-Pump: Hobbes, Boyle, and the Experimental Life* (1985).

[^huygens]: Shapin and Schaffer, *Leviathan and the Air-Pump*, discussion of Huygens and anomalous suspension. The reproduction of the effect established a shared phenomenon; it did not by itself settle every theoretical question about it.

[^duhem]: Pierre Duhem, *La théorie physique: son objet et sa structure* (1906); W. V. O. Quine, “Two Dogmas of Empiricism,” *The Philosophical Review* 60 (1951), 20–43.

[^wegener]: Alfred Wegener, *The Origin of Continents and Oceans* (first German edition, 1915); Frederick J. Vine and Drummond H. Matthews, “Magnetic Anomalies over Oceanic Ridges,” *Nature* 199 (1963), 947–949. Plate tectonics vindicated continental mobility while replacing important parts of Wegener's proposed mechanism.

[^allocation]: Philip Kitcher, “The Division of Cognitive Labor,” *The Journal of Philosophy* 87 (1990), 5–22; Imre Lakatos, “Falsification and the Methodology of Scientific Research Programmes,” in *Criticism and the Growth of Knowledge* (1970).

[^newton]: Johann Bernoulli's challenge in *Acta Eruditorum* (1696), and Newton's anonymous solution in *Philosophical Transactions* (1697). John Conduitt's [“Miscellanea,” Keynes Ms. 130.05](https://www.newtonproject.ox.ac.uk/view/texts/diplomatic/THEM00168), records the four-in-the-afternoon to four-in-the-morning account, attributing it to Catherine Conduitt. For the wider episode and the attribution anecdote, see Richard S. Westfall, *Never at Rest: A Biography of Isaac Newton* (1980).

[^hardwig]: John Hardwig, “Epistemic Dependence,” *The Journal of Philosophy* 82 (1985), 335–349.

[^higgs]: ATLAS Collaboration, [“Observation of a new particle in the search for the Standard Model Higgs boson with the ATLAS detector at the LHC”](https://doi.org/10.1016/j.physletb.2012.08.020), *Physics Letters B* 716 (2012), 1–29; CMS Collaboration, [“Observation of a new boson at a mass of 125 GeV with the CMS experiment at the LHC”](https://doi.org/10.1016/j.physletb.2012.08.021), *Physics Letters B* 716 (2012), 30–61.

[^opera]: CERN, [“OPERA experiment reports anomaly in flight time of neutrinos from CERN to Gran Sasso”](https://home.cern/opera-experiment-reports-anomaly-in-flight-time-of-neutrinos-from-cern-to-gran-sasso/), including the February 2012 update on the two timing effects; OPERA Collaboration, [“Measurement of the neutrino velocity with the OPERA detector in the CNGS beam”](https://arxiv.org/abs/1109.4897), corrected version (2012).

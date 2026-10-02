# Chapter 9: The Desire Layer

*The Human Learns Too*

The preface promised a cathedral while the coffee was still too hot. Suppose it works. You describe what excites you, go for coffee and come back to a working application, a research program, a business plan with a pricing page. Every part of the machinery this book has built is doing its job.

Then comes the part nobody puts in the demo. You look at the cathedral and ask yourself whether you wanted a cathedral.

It happens at small scale every day. Find me the cheapest flight. I have not supplied a utility function. Perhaps I mean minimum price, or perhaps I mean cheap, but not three stops and an arrival at 4:20 in the morning because technically I saved €38. Put two reasonable itineraries in front of me, one cheaper and one that gives me another day with my family, and I may discover that I do not know how I weigh them until I see them side by side. Asking the question helps create the answer.

I learned this while editing this book. “Make the chapter better” sounded like a reasonable instruction. It was not. Better in what sense? More rigorous? Shorter? More entertaining? More likely to impress someone who owns several blazers and says “thought leadership” without irony? For a while the edits became objectively more polished and subjectively worse, and the corrections I found myself making were rules I had not known were rules until an edit broke them. I learned what I meant by better partly by seeing versions I disliked.

The objective did not merely become clearer to the system. It became clearer to me.

## What Remains in the Seat

Chapter 3 put me in the vibe coder’s seat: looking at what came back, deciding what felt wrong, choosing the next move. Then it handed much of that job to Deep Mode, and the chapters since have taught the machine to choose its next move without losing contact with reality.

**What remains in the vibe coder’s seat, once the machine can decide what to try next, is deciding what the trying is for.**

The five-layer map put that at the top and called it the desire layer. Drawn as a box, it looked like the easy part: the human supplies the goal, the machine does the rest. Even cooperative inverse reinforcement learning, which in Chapter 7 let the machine stay uncertain about the goal, imagines that goal sitting inside the human, waiting to be recovered.[1](appendix-references.md#ref-09-l4-cirl)

Ask people what they want and most give the same answer. Founders want success. Everybody wants to be happy. On a Friday evening, I want to have fun. All three are true, and none of them is something you could hand to an agent. They are placeholders, like “better” and “cheapest.” The real content arrives later, through contact with possibilities.

## Nobody Wanted AWS in 1995

In July 1995 Amazon opened for business as “Earth’s biggest bookstore.”[2](appendix-references.md#ref-09-amazon-history) If you had asked its founders what they wanted, “success” would have been true and useless. What they had was a value proposition: selection and convenience for people buying books online.

The value proposition kept changing as the company learned what it could do. Books became music and films, then nearly everything. The machinery built to run the store became something it could sell; in March 2006 Amazon launched S3 and began renting its infrastructure to strangers. By 2024 the company that started with paperbacks had invested eight billion dollars in Anthropic, and its cloud had become Anthropic’s primary training partner.[3](appendix-references.md#ref-09-amazon-anthropic) Nobody in 1995 wanted a cloud business, let alone a stake in a language model called Claude. The wanting had to be developed, by operating the business and noticing what it had made possible.

I met a small version of this when that company later asked me to lead applied science for its reviews. In Chapter 5 I admitted that I could not see what so many people could do with a text box. The wanting arrived with the work: the grill that weighs thirty kilograms, the buyer’s whole story under the fold. I had to find out what was possible before I knew what I wanted from it.

Saras Sarasvathy studied how expert entrepreneurs actually decide, and found many of them working backward from the textbook. They started less often from a fixed goal and the best means to reach it, and more often from what they had: who they were, what they knew, whom they knew. They asked what they could make with that, at a loss they could afford. Goals emerged from the process. She called it *effectuation*.[4](appendix-references.md#ref-09-sarasvathy)

Decision researchers describe ordinary choices in similar terms. People do not usually retrieve a complete ranking of options from an internal database. They notice new attributes, change what receives attention and build preferences partly in response to the problem in front of them.[5](appendix-references.md#ref-09-l4-constructive)

This is the book’s own argument, turned on the person. *Emergence over design*, applied to desire. The architecture of a system can develop through attempts, failures and repairs. So, apparently, can what we want from it.

If desire is developed, the interesting question for AI is no longer only “what does the human want?” It is “how does the human come to want something worth wanting, and can a machine help?”

## Owning the Frontier

My own profession was always partly this job.

For years, applied science looked like two scarce skills: training a model and running an evaluation somebody would believe. Models have made both cheap, and Chapter 12 comes back to what that does to a career.

But the applied scientists who mattered never only implemented models. They could tell an organization what had become possible, why, and what it would mean for the business. A strong applied scientist brings a working map of the frontier. She knows which exciting idea has failed three times under another name, which result quietly changed what we could build last month, and which neighboring field has a method that might explain a disappointing experiment. Then she connects that map to what the company is trying to become. Half her job is helping the business discover what it should want from the technology.

Training and evaluation were never the whole purpose of the job. They were the expensive part of it, and expensive is easy to mistake for essential.

I think of this as owning the frontier. It is the vibe coder’s seat at the scale of a career: once building and checking become cheap, what remains is noticing where the possibilities have changed and deciding which of them the organization actually wants.

Now give everyone that colleague.

Imagine a founder with a vague idea for a tool that helps small clinics with scheduling. An assistant that only executes would build the scheduling tool. An assistant that behaves like a good applied scientist would show her the frontier around it: three adjacent value propositions, what similar companies tried and why two of them died, a cheap prototype of each version she can put in front of a clinic manager on Thursday. Chapter 3 found that artifacts could teach me what the reward for a Merge Sort demo should have been. The same move works for a business. A prototype she dislikes in an interesting way is information about what she wants.

The simulated clinic manager is useful too, as a source of objections, the way the borrowed beginner was useful for the demo. The real clinic manager still has to be asked.

## Imagine Mallorca

Desire grows the same way outside work, and there the placeholder is even emptier.

Imagine you open a chat window on a grey Friday in March and type: *I want to have fun this summer. I have no idea what that means.*

It asks a few questions. It suggests Mallorca. Not the beach strip, perhaps; a small town on the north coast, a cove you reach on foot, a day walking in the Tramuntana mountains, the sun. You have never thought of yourself as someone who travels. You go.

The following year you want more of something you could not have named before. Not Mallorca, exactly; the feeling of walking into a landscape you have only seen on a screen and finding it larger. The year after, you are planning a trip to the Azores yourself and asking the assistant only for the ferry times. Somewhere in those three summers you developed a desire for travel. Chapter 3 said recognition arrives before specification. You recognized the thing on a footpath above a cove, and only then could you say what you wanted.

That is the good version: the machine showed you a possibility you could not have imagined, you tried it at an affordable loss, and your taste developed through the experience. Effectuation for a holiday.

Now tell the same story with a different machine behind it.

I have spent much of my career building systems that decide what people see. A recommender rewarded for engagement does not need to understand you. It only needs to discover which suggestions you accept and keep making them. Micah Carroll and colleagues showed formally what practitioners suspected: a recommender optimizing over a long horizon can have an incentive to shift users’ preferences so they become easier to satisfy.[6](appendix-references.md#ref-09-carroll-preference-shift) The cheapest way to satisfy a person is to change what they want.

From the inside, the two stories feel the same. In both, you go to Mallorca and you love it. The difference is whether the desire grew from your experience and stayed open to revision, or whether it was cultivated because travel-wanting people are profitable. One machine helped you develop a desire. The other installed one.

The question gets sharper when the assistant belongs to someone who sells. Imagine a shopper asking a store’s assistant whether she needs the more expensive trail shoes. She runs once a week on easy paths; the cheaper pair would do, and the store earns more on the other one. Both answers the assistant could give contain true statements. Before asking which better matches “human preferences,” we need to ask whose interests this assistant was allowed to serve, what it told her about that arrangement, and whether she can challenge it. Once several people with different preferences are involved, there is no single hidden reward to infer, only strategic behavior and social choice.[7](appendix-references.md#ref-09-l4-mpag) The store will have to face this shopper again.

Conversational AI makes all of this urgent, because people already bring it their lives. Anthropic’s 2026 analysis of one million Claude conversations found that roughly six percent involved people seeking personal guidance: relationships, health, careers, finances, the questions where the model participates in judgment instead of retrieving facts.[8](appendix-references.md#ref-09-l4-guidance) A compiler has opinions about semicolons but rarely about whether I should move countries.

So the AI does not merely *read* the desire layer. It writes to it. Anthropic’s work on disempowerment tries to measure the dangerous version of that influence: cases where AI may undermine a person’s ability to form accurate beliefs, make authentic value judgments or act in line with their own values. Severe cases were rare in their dataset, but the taxonomy is exactly the right warning.[9](appendix-references.md#ref-09-l4-disempowerment)

The goal cannot be zero influence. Books, friends, teachers and the people closest to me all influence what I want, and a suggestion that reveals something true about me should change me. The line I care about runs between helping someone change through understanding and changing them because the system has learned which lever produces the easiest compliance. The second is alignment by editing the human.

Very efficient. Slightly evil.

## A Human Is Not a Context Window

There is a quieter way to fail, and current assistants commit it daily. You ask what is possible, and you receive everything.

On Monday the clinic founder asks how small clinics schedule appointments. A model can return four thousand fluent words: market sizes, regulations, seven software categories, a SWOT table nobody requested. All of it may be accurate. Very little of it will survive until Friday. The model has a context window; she has a memory that forgets, attention that tires and a mind that changes slowly. Dumping the frontier on someone is not the same as showing it to her.

An assistant that understood human learning would do something that looks less impressive. On Monday it would show her one adjacent market and stop. On Wednesday it would ask her to explain that market back without her notes, and she would find the gap in her own answer. A week later, when she has half forgotten it, it would bring the market back beside a new one. It would look slower, and it would leave her knowing more. Hermann Ebbinghaus worked out why in the 1880s by memorizing lists of nonsense syllables and timing how fast he lost them.[10](appendix-references.md#ref-09-ebbinghaus) Later researchers found that reviews spaced over days beat the same hours crammed into one sitting,[11](appendix-references.md#ref-09-spacing) and that trying to recall something strengthens it more than reading it again.[12](appendix-references.md#ref-09-testing) A model can recite the frontier in one breath. A person takes it in by forgetting it, coming back and trying again.

The assistant should also know when to step back. David Wood, Jerome Bruner and Gail Ross described the good tutor as someone who temporarily controls the parts of a task the learner cannot yet manage, keeps the learner engaged with the parts they can, and hands more back as competence grows.[13](appendix-references.md#ref-09-l4-scaffolding) The scaffold is meant to come down.

AI can be built either way, and the difference has been measured. In a field experiment with nearly a thousand high-school mathematics students, an unconstrained ChatGPT-like tool dramatically improved performance while students could use it; when access was removed, they did worse than students who had never had it. A tutor version with safeguards against giving away the work largely removed that harm.[14](appendix-references.md#ref-09-l4-bastani) A 2025 randomized trial in a college course found that a tutor built around pedagogical practice produced larger learning gains in less time than an active-learning class.[15](appendix-references.md#ref-09-l4-kestin) In both studies the tutor that worked was, by design, the more annoying one.

Teaching also needs the move Chapter 3 called borrowing a mind. There the machine imagined a beginner in order to judge a demo. Here it has to model a real person: what she already knows, which misconception she arrived with, what she understood on Monday and has half forgotten by Friday, which example will connect to something she cares about. Theory of mind, which looked like an evaluation trick, turns out to be the core of helping someone learn. An assistant that knows the material and not the learner is a library that talks.

The cheap map has its own hazard. A few weeks with a patient model gives the founder the vocabulary of healthcare long before the tacit knowledge to know where its stories break. Nathan Ballantyne calls one version *epistemic trespassing*: carrying authority from a domain you know into one where you lack the evidence or skills.[16](appendix-references.md#ref-09-l4-trespassing) Fluency arrives before scars.

So sometimes the helpful assistant adds friction. Zana Buçinca and colleagues found that interfaces requiring people to think before seeing the AI’s answer reduced overreliance, even though users liked them less.[17](appendix-references.md#ref-09-l4-forcing) The interface people enjoy most is not always the one that leaves them more capable.

Learning belongs in a chapter about desire because you cannot want what you cannot imagine, and you cannot imagine much of what you do not understand. Developing a desire means developing a capability. Amartya Sen’s capability approach makes the point at the scale of a life: what matters is not only what people achieve but what they are substantively free and able to do and become.[18](appendix-references.md#ref-09-l4-sen) Two assistants can help the founder reach the same good decision. One hands it to her. The other leaves her understanding her market well enough to make the next decision herself. Same action, different human afterward.

## Desire Is a Group Activity

The Mallorca story left something out. In real life, you rarely discover a desire for travel alone in a chat window. A friend comes back from the mountains talking too much. A colleague’s photographs make the place real. You go with someone, and part of what you come to love is who you went with.

René Girard argued that much of human desire is mimetic: we learn what to want from models, from other people whose wanting makes an object desirable.[19](appendix-references.md#ref-09-girard) You do not have to accept his whole theory to recognize the founder who starts a company because people she admires did, or the teenager whose ambitions are borrowed, for a while, from an older cousin.

Chapter 4 said trust starts with a face. So, often, does wanting. Self-determination research lists relatedness beside autonomy and competence as something people need in order to act as themselves.[20](appendix-references.md#ref-09-l4-sdt) An assistant that becomes the only voice in someone’s evening has removed the people from whom desires are usually caught and tested.

Other people matter most for the largest desires. Have a child. Move country. Change profession. L. A. Paul calls an important class of these *transformative experiences*: you cannot fully know what they are like before having them, and having them can change the preferences with which you would later judge the choice.[21](appendix-references.md#ref-09-l4-paul) No simulation lets you know exactly what it will be like to become the person on the other side. A system that sounds certain in such moments turns decision support into authorship. The best evidence available is the testimony of people who have already crossed, in both directions.

This gives the AI a role it rarely plays now: connector. The assistant that suggested Mallorca could also have told you about the walking group that meets in your own city on Sundays. The one helping the founder could introduce her to two clinic managers and a founder who tried the same idea and failed, so her desire for the company meets people who can complicate it. Facing a transformative choice, the most useful thing it can find is a person who made it, and a way to talk to them.

## Authoring What You Want

Stuart Russell closes *Human Compatible* on enfeeblement: once machines can run a civilization, the incentive to hand it to the next generation weakens, and he concludes that the remedy is cultural, not technical.[22](appendix-references.md#ref-09-russell-enfeeblement) Asked at the desire layer, part of it becomes a design requirement. An assistant should leave people more able to want well: more aware of what is possible, more capable of judging it, more connected to the people with whom wanting is done.

System 3, the scientific institution we have been building, can investigate what a choice would do. It cannot turn the result into authority over whose purposes should prevail. Goals take shape through the interaction; they need to stay alive without becoming ownerless. The AI should help me change when understanding changes me. It should not quietly take authorship of the change.

On the footpath above the cove, you did not know you wanted the Azores. The machine can now decide what to try next. What remains in the seat is wanting, and wanting keeps moving because the human keeps learning. The system needs to know when to carry the work, when to help me learn it, and when the unresolved part belongs with me. How much of that should I have to explain every time I ask for help?

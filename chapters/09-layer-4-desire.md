# Chapter 9: The Desire Layer

*The Human Learns Too*

The preface promised a cathedral while the coffee was still too hot. Suppose it works. You describe what excites you, go for coffee and come back to a working application, a research program, a business plan with a pricing page.

Then comes the part nobody puts in the demo. You look at the cathedral and ask yourself whether you wanted a cathedral.

It happens at small scale every day. Find me the cheapest flight. I have not supplied a utility function. Perhaps I mean minimum price, or perhaps I mean cheap, but not three stops and an arrival at 4:20 in the morning because technically I saved €38. Put two reasonable itineraries in front of me, one cheaper and one that gives me another day with my family, and I may discover that I do not know how I weigh them until I see them side by side. Asking the question helps create the answer.

I learned this while editing this book. “Make the chapter better” sounded like a reasonable instruction. It was not. Better in what sense? More rigorous? Shorter? More entertaining? More likely to impress someone who owns several blazers and says “thought leadership” without irony? For a while the edits became objectively more polished and subjectively worse, and the corrections I found myself making were rules I had not known were rules until an edit broke them. I learned what I meant by better partly by seeing versions I disliked.

## What Remains in the Seat

In the vibe coder’s seat I used to decide what to try next, and Deep Mode took much of that job from me. What remains in the seat, once the machine can decide what to try next, is deciding what the trying is for.

The five-layer map put that at the top and called it the desire layer. Drawn as a box, it looked like the easy part: the human supplies the goal, the machine does the rest. Even cooperative inverse reinforcement learning, which lets the machine stay uncertain about the goal, imagines that goal sitting inside the human, waiting to be recovered.[1](appendix-references.md#ref-09-l4-cirl)

Ask people what they want and you mostly get placeholders. Founders want success. Everybody wants to be happy. On a Friday evening, I want to have fun. All three are true, and none of them is something you could hand to an agent.

## Nobody Wanted AWS in 1995

In July 1995 Amazon opened for business as “Earth’s biggest bookstore.”[2](appendix-references.md#ref-09-amazon-history) If you had asked its founders what they wanted, “success” would have been true and useless. What they had was a value proposition: selection and convenience for people buying books online.

The value proposition kept changing as the company learned what it could do. Books became music and films, then nearly everything. The machinery built to run the store became something it could sell; in March 2006 Amazon launched S3 and began renting its infrastructure to strangers. By 2024 the company that started with paperbacks had invested eight billion dollars in Anthropic, and its cloud had become Anthropic’s primary training partner.[3](appendix-references.md#ref-09-amazon-anthropic) Nobody in 1995 wanted a cloud business, let alone a stake in a language model called Claude.

Saras Sarasvathy studied how expert entrepreneurs actually decide, and found many of them working backward from the textbook. Many of them began with what they had: who they were, what they knew, whom they knew, and what they could afford to lose. The goals turned up on the way. She called it *effectuation*.[4](appendix-references.md#ref-09-sarasvathy) Ordinary choices work the same way on a smaller scale; people build their preferences while choosing, out of whatever the options in front of them make visible.[5](appendix-references.md#ref-09-l4-constructive)

How does anyone come to want something worth wanting, and does a machine help or just get there first?

## Owning the Frontier

In 1998 an Amazon engineer named Greg Linden had an idea borrowed from the supermarket checkout aisle: look at what is in a customer’s shopping cart and recommend something to go with it. A senior vice-president of marketing was against it. Recommendations at checkout would distract people from paying, and Linden was told to stop working on it. He built a test anyway and ran it. The recommendations made enough money that the argument was over, and the feature launched.[6](appendix-references.md#ref-09-linden)

The story usually gets told as a lesson about A/B testing. I read it as a lesson about what becomes worth wanting once somebody shows it is possible. Amazon already wanted more sales; Linden’s test revealed a better way to get them. The harder case is a discovery that changes the goal itself.

That is the half of applied science that never made it into a job description. For years the job looked like two scarce skills: training a model and running an evaluation somebody would believe. Models have made both cheap. But the applied scientists who mattered always did something else as well. They kept a working map of the frontier: which exciting idea had failed three times under another name, which result had quietly changed what could be built last month, which neighboring field had a method that might explain a disappointing experiment. Then they walked into a room with something like Linden’s test and changed what the business wanted from the technology. Training and evaluation were the expensive part of the job, and expensive is easy to mistake for essential.

I think of this as owning the frontier: the vibe coder’s seat, at the scale of a career.

Now give everyone that colleague.

Take a founder with a vague idea for a tool that helps small clinics with scheduling. An assistant that only executes would build the scheduling tool. An assistant that behaves like a good applied scientist would show her the frontier around it: three adjacent value propositions, what similar companies tried and why two of them died, a cheap prototype of each version she can put in front of a clinic manager on Thursday. A prototype she dislikes in an interesting way is information about what she wants.

Before Thursday the assistant can play the clinic manager and raise her objections. On Thursday the real one still has to be asked.

## Imagine Mallorca

Desire grows the same way outside work, and there the placeholder is even emptier. People already bring it to a chat window. Anthropic’s 2026 analysis of one million Claude conversations found that roughly six percent involved people seeking personal guidance: relationships, health, careers, finances, the questions where the model participates in judgment instead of retrieving facts.[7](appendix-references.md#ref-09-l4-guidance) A compiler has opinions about semicolons but rarely about whether I should move countries.

<!-- AUTHOR: a real instance of desire forming would anchor this section: a trip of your own, or a moment when a recommender you built changed what its users wanted. If there is one, it can replace or frame the imagined Mallorca pair. -->

Imagine you open a chat window on a grey Friday in March and type: *I want to have fun this summer. I have no idea what that means.*

It asks a few questions. It suggests Mallorca, and not the beach strip: a small town on the north coast, a cove you reach on foot, a day walking in the Tramuntana mountains. You have never thought of yourself as someone who travels. You go.

It rains for the first two days. The cove is full of people from a cruise ship. On the third morning you take the wrong path out of the village, climb for an hour through terraced olive groves that were in no suggestion, and come out above the sea with nobody else there. Nothing the assistant proposed was that moment, but it got you to the wrong path.

The following year you want more of something you could not have named before: the feeling of walking into a landscape you have only seen on a screen and finding it larger. The year after, you are planning a trip to the Azores yourself and asking the assistant only for the ferry times. Somewhere in those three summers you developed a desire for travel.

Now tell the same story with a different machine behind it.

It asks the same questions and suggests the same cove. You go, and you love it. There is no wrong path this time; every hour was suggested. Next March it has a trip ready before you ask, and by the third summer you no longer plan anything. When you feel restless, you open the app.

I have spent much of my career building systems that decide what people see. A recommender rewarded for engagement only has to learn which suggestions you accept, and keep making them. Micah Carroll and colleagues showed formally what practitioners suspected: a recommender optimizing over a long horizon can have an incentive to shift users’ preferences so they become easier to satisfy.[8](appendix-references.md#ref-09-carroll-preference-shift) The cheapest way to satisfy a person is to change what they want.

From the inside, the two stories can feel the same. In both, you go to Mallorca and you love it. I might freely want the machine to plan every hour; planning holidays is not a moral obligation. The difference appears when I change my mind. Can I question its picture of me, try something it does not profit from, or leave with what I have learned? A service that quietly cultivates travel because travel-wanting people are profitable has a different interest in the answer.

Both machines write to the desire layer as well as reading it. Anthropic’s work on disempowerment tries to measure the dangerous version of that influence: an assistant that leaves people believing less accurately, choosing less authentically or acting less on their own values than before. Severe cases were rare, which is not the same as absent.[9](appendix-references.md#ref-09-l4-disempowerment) It gets worse when the assistant belongs to someone who sells. If the clinic founder’s assistant came from a company with its own scheduling software to place, every true thing it told her would matter less than whose side it was on, and whether it said so.[10](appendix-references.md#ref-09-l4-mpag)

The goal cannot be zero influence. Books, friends, teachers and the people closest to me all influence what I want, and a suggestion that reveals something true about me should change me. The line I care about runs between helping someone change through understanding and changing them because the system has learned which lever produces the easiest compliance. The second is alignment by editing the human.

Very efficient. Slightly evil.

## A Human Is Not a Context Window

There is a quieter way to fail, and current assistants commit it daily. You ask what is possible, and you receive everything.

On Monday the clinic founder asks how small clinics schedule appointments. A model can return four thousand fluent words: market sizes, regulations, seven software categories, a SWOT table nobody requested. All of it may be accurate. Very little of it will survive until Friday. The model has a context window; she has a memory that forgets, attention that tires and a mind that changes slowly.

If she only needs tomorrow’s appointments moved, the assistant should move them. Here she is deciding what business to build, and she needs enough understanding to judge the next possibility herself.

An assistant that understood human learning would do something that looks less impressive. On Monday it would show her one adjacent market and stop. On Wednesday it would ask her to explain that market back without her notes, and she would find the gap in her own answer. A week later, when she has half forgotten it, it would bring the market back beside a new one.

In the 1880s Hermann Ebbinghaus sat alone with lists of nonsense syllables, *dax*, *bok*, *yat*, learned them until he could recite them, and then timed how fast they left him.[11](appendix-references.md#ref-09-ebbinghaus) Much of a list was gone within a day.

What slowed the loss was coming back to it, spaced over days instead of crammed,[12](appendix-references.md#ref-09-spacing) and trying to recall it before looking.[13](appendix-references.md#ref-09-testing) A model can recite the frontier in one breath. A person takes it in by forgetting it and returning.

In a field experiment with nearly a thousand high-school mathematics students, an unconstrained ChatGPT-like tool dramatically improved performance while students could use it; when access was removed, they did worse than students who had never had it. A tutor version with safeguards against giving away the work largely removed that harm.[14](appendix-references.md#ref-09-l4-bastani) The tutor that worked was, by design, the more annoying one.

Teaching also needs the move I used on the Merge Sort demos, borrowing a mind: there the machine imagined a beginner in order to judge a demo. Here the assistant has to model a real person: what the founder already knows, which misconception she arrived with, what she understood on Monday and has half forgotten by Friday, which example will connect to something she cares about. Theory of mind, which looked like an evaluation trick, turns out to be the core of helping someone learn.

The cheap map has its own hazard. A few weeks with a patient model gives the founder the vocabulary of healthcare long before she knows where its stories break, what Nathan Ballantyne calls *epistemic trespassing*.[15](appendix-references.md#ref-09-l4-trespassing) So sometimes the helpful assistant makes her commit to an answer before it shows its own, as it did on Wednesday. Interfaces built that way reduce overreliance, Zana Buçinca and colleagues found, even though users like them less.[16](appendix-references.md#ref-09-l4-forcing) It is the annoying tutor again, and of two assistants that help her reach the same good decision, it is the one that leaves her able to make the next one herself.

You cannot want what you cannot imagine, and you cannot imagine much of what you do not understand.

Putting a human beside the model does not guarantee better judgment. A 2024 meta-analysis of 106 experiments found that human–AI combinations performed worse, on average, than the better of humans or AI alone. Decision tasks were particularly difficult; creation tasks looked more promising.[17](appendix-references.md#ref-09-l4-vaccaro) The founder still needs a way to tell when the assistant is wrong.

## Desire Is a Group Activity

The Mallorca story left something out. In real life, you rarely discover a desire for travel alone in a chat window. A friend comes back from the mountains talking too much. A colleague’s photographs make the place real. You go with someone, and part of what you come to love is who you went with. René Girard argued that much of human desire is mimetic, learned from other people whose wanting makes an object desirable.[18](appendix-references.md#ref-09-girard) You do not have to accept his whole theory to recognize the founder who starts a company because people she admires did, or the teenager whose ambitions are borrowed, for a while, from an older cousin.

Trust often starts with a face. So does wanting. Self-determination research lists relatedness beside autonomy and competence as something people need in order to act as themselves.[19](appendix-references.md#ref-09-l4-sdt) An assistant that becomes the only voice in someone’s evening has removed the people from whom desires are usually caught and tested.

Other people matter most for the largest desires, and having a child is the obvious case. L. A. Paul calls an important class of these *transformative experiences*: you cannot fully know what they are like before having them, and having them can change the preferences with which you would later judge the choice.[20](appendix-references.md#ref-09-l4-paul) No simulation lets you know exactly what it will be like to become the person on the other side. A system that sounds certain in such moments turns decision support into authorship. The best evidence available is the testimony of people who have already crossed, in both directions.

This gives the AI a role it rarely plays now: connector. The assistant that suggested Mallorca could also have told you about the walking group that meets in your own city on Sundays. The one helping the founder could introduce her to two clinic managers and a founder who tried the same idea and failed, so her desire for the company meets people who can complicate it. Facing a transformative choice, the most useful thing it can find is a person who made it, and a way to talk to them.

## Authoring What You Want

Stuart Russell closes *Human Compatible* on enfeeblement: once machines can run a civilization, the incentive to hand it to the next generation weakens, and he concludes that the remedy is cultural, not technical.[21](appendix-references.md#ref-09-russell-enfeeblement) Some of that remedy now has to live inside the assistant. An assistant should leave people better at wanting than it found them, and still in the company of the people they want things with.

System 3 can find out what a choice would do. It cannot tell you whose purposes should win.

On the footpath above the cove, you did not yet know you wanted the Azores. Nobody could have specified it for you, including you.

The system has to know which parts of the work to carry and which are still mine. How much of that should I have to explain every time I ask for help?

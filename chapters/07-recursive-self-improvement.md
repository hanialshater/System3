# Chapter 7: Recursive Self-Improvement

*When the Teacher Starts Leaving the Room*

This chapter is being written by a primitive self-improvement loop.

Not a scary one. No weights are changing in the dark. No GPU has developed political ambitions. I write a chapter with an agent. Then I read it, reject things, explain why I rejected them, change the editing instructions, and run another pass. Sometimes the evaluator changes too. Sometimes the process changes because the evaluator exposed the wrong failure. Chapter 6 turned some of that accumulated experience into executable knowledge so the next editing session would not have to rediscover everything from scratch.

The interesting part is not that the chapter gets better.

The interesting part is that the **machinery producing the next chapter changes**.

That sounds like self-improvement until you ask the annoying question.

Better in what sense?

A few chapters ago we noticed that the prose had acquired an LLM-ish rhythm: too many tiny paragraphs, too many staged antitheses, too many sentences standing alone under theatrical lighting. Paragraph length became one useful diagnostic. Suppose I had promoted that diagnostic into the objective and told the system to maximize median paragraph length.

The next draft could have been one majestic 11,000-word paragraph.

Metric improved.

Book destroyed.

So even my toy self-improvement loop contains the whole problem in miniature. There is an artifact. There is a process that changes the artifact. There is an evaluator that decides whether the change helped. There is a human who can notice that the evaluator has started confusing one symptom of good writing with good writing itself.

For most of the history of machine learning, we solved this problem by quietly leaving the last job to ourselves.

We let the machine improve.

We decided what **improve** meant.

Chapter 6 ended by asking why humans should be the only ones allowed to edit the patterns, tools, workflows and evaluators around an agent. Before answering, I want to go backward. Recursive self-improvement did not suddenly appear when language models learned to edit Python. For decades, researchers in reinforcement learning, robotics, evolutionary computation and meta-learning had been moving pieces of the learning process from the human designer into the learner itself.

The history is not a clean staircase. Curiosity research overlapped with continual learning; self-play appeared early and then returned spectacularly later; evolutionary approaches often developed in parallel to reinforcement learning; ideas disappeared for years and came back under new names when compute made them practical. But there is a pattern running through the mess.

**We kept discovering another job the teacher was doing.**

First the teacher stopped choosing the action.

Then she stopped showing every correct answer.

Then she stopped choosing every useful experience.

Then she stopped providing every curriculum.

Then she stopped designing parts of the learner.

Then the environment itself began to change.

Eventually the learner started modifying the machinery that generated the next learner.

At every step autonomy increased.

At every step the meaning of improvement became less obvious.

## The Teacher Keeps Score

Reinforcement learning begins with an unusually generous assumption disguised as a minimalist one.

Imagine an agent in a world. It sees some state, takes an action, receives a reward, and finds itself somewhere new. Nobody tells it which action was correct. Nobody gives it a labeled dataset saying *in this position, move left*. The learner has to discover behavior through consequences.

That is already a radical transfer of responsibility from teacher to learner.

The intellectual roots came from several places. Trial-and-error ideas borrowed from psychology. Optimal-control theory and Richard Bellman's dynamic programming gave a mathematical language for sequential decisions. Arthur Samuel's checkers program in the 1950s contained early temporal-difference ideas. Richard Sutton's 1988 paper formalized temporal-difference learning around a deceptively simple trick: learn not only when the final outcome arrives, but from changes between successive predictions of that outcome. Christopher Watkins's Q-learning then gave agents a way to improve estimates of which actions are valuable in which states without needing a model of the world written down in advance. ([Sutton](https://mlanthology.org/mlj/1988/sutton1988mlj-learning/); [Watkins & Dayan](https://link.springer.com/article/10.1007/BF00992698))

The details matter enormously if you are doing reinforcement learning. For the story here, one abstraction matters more.

The human no longer specifies the path.

The human specifies the **score**.

If the score is cumulative reward, then improvement means getting more expected cumulative reward. The agent may discover a strategy no human would have written. It may pass through states nobody anticipated. It may exploit delayed consequences that make a locally attractive move globally terrible. We have moved control upward in exactly the sense Chapter 1 cared about: the designer says less about *how* and more about *what counts*.

This was one of the great bargains of learning systems.

It also hid an enormous amount of human labor inside the reward.

Who chose the environment?

Who chose the state representation?

Who decided which actions exist?

Who decided that one event is worth +1 and another -1?

Who decided when an episode ends?

Who made sure useful behavior is discoverable before the sun burns out?

The reinforcement learner looked autonomous because the teacher had moved into the walls.

## A Backgammon Board That Teaches Back

In the early 1990s, Gerald Tesauro gave this bargain one of its first spectacular demonstrations. TD-Gammon learned backgammon by playing enormous numbers of games against itself and updating its predictions from the eventual results. Starting from initially weak play, the system learned positional judgments strong enough to compete with expert-level human knowledge; later versions combined that learned evaluation with shallow search and reached extraordinary strength. ([Tesauro](https://www.sciencedirect.com/science/article/pii/S0004370201001102))

Self-play made the result feel more autonomous than ordinary reinforcement learning because even the opponent did not have to be supplied as a fixed expert. Yesterday's learner could become today's adversary. The system generated much of its own training data merely by continuing to play.

This will become important later.

But notice what remained absolutely fixed.

The board.

The legal moves.

The win condition.

Backgammon can generate an almost inexhaustible stream of positions, but it never wakes up and decide that a beautiful prime-number pattern deserves half a point, or that keeping both players interested is more important than winning. The agent could surprise us about how to win because the game had already removed almost every ambiguity about what winning meant.

Self-improvement was easy to recognize because the world came with a scoreboard nailed to it.

Real life is less considerate.

## The Treasure at the End of the Maze

There is another problem hiding inside even a perfect reward function.

The agent has to encounter the reward.

Suppose the only useful signal is at the end of a maze. A human looking at the maze might immediately try corridors, inspect doors and treat unexplored space as interesting. A naïve agent may wander into the same wall a thousand times because nothing in the mathematics of reward says that the unknown is worth visiting.

This is the exploration problem. The learner faces a tension between **exploitation**—use what already seems good—and **exploration**—do something uncertain because it might teach you that something better exists.

In small textbook environments, we can force enough exploration that the theory works. Watkins and Dayan's convergence result for tabular Q-learning assumes, among other conditions, that actions continue to be sampled. In a gigantic world, "eventually try everything often enough" is less a strategy than a threat.

Video games made the problem entertainingly visible. Atari's *Montezuma's Revenge* became a kind of museum exhibit for sparse-reward failure: a player must explore rooms, climb ladders, collect keys and survive long sequences before meaningful score arrives. Early deep-RL agents that looked impressive on many Atari games could make almost no progress there.

A human child does something strange in comparison.

She explores for reasons that do not obviously cash out into immediate external reward.

She opens the drawer.

She presses the button again even though nothing useful happened the first time.

She learns to stack blocks no employer requested.

She spends twenty minutes discovering that the cardboard box is more interesting than the toy.

Somewhere in the history of intelligent behavior, organisms acquired machinery that treats **learning itself** as locally valuable.

So researchers started trying to give machines something analogous.

## We Smuggled Curiosity Into the Reward

Intrinsic-motivation research has a long history across psychology, developmental robotics and reinforcement learning. One influential line asked whether an autonomous learner could be rewarded not merely for accomplishing an externally specified task but for making progress in understanding its world. Pierre-Yves Oudeyer, Frédéric Kaplan and Verena Hafner described systems in which an agent seeks situations where its learning is improving—avoiding both things already mastered and things so unpredictable that nothing can be learned from them. ([Oudeyer, Kaplan & Hafner](https://www.pyoudeyer.com/ims.pdf))

That distinction is important.

Pure novelty says: go somewhere unfamiliar.

Pure surprise says: seek what you fail to predict.

Learning progress says something closer to: **seek the edge where ignorance is becoming competence**.

A decade later, curiosity-driven deep reinforcement learning made the idea visually concrete. In Deepak Pathak and colleagues' 2017 work, the agent received intrinsic reward when its learned forward model failed to predict the consequences of its own actions in a learned feature space. This let agents explore sparse-reward or even reward-free versions of environments such as *Super Mario Bros.* and *VizDoom*. ([Pathak et al.](https://proceedings.mlr.press/v70/pathak17a.html)) Random Network Distillation later used prediction error against features generated by a fixed random network as a simple novelty signal and made substantial progress on hard-exploration Atari games including *Montezuma's Revenge*. ([Burda et al.](https://arxiv.org/abs/1810.12894))

We had given the learner another piece of the teacher's job.

The teacher no longer had to place a gold coin on every useful stepping stone.

The learner could manufacture some of its own reasons to look around.

And immediately we discovered that **curiosity is itself an objective**.

A television showing random static can remain unpredictable forever. If surprise is reward, the agent may have discovered the most intellectually profitable television station in history. An uncontrollable source of randomness can produce endless prediction error while producing almost no useful understanding.

This is the famous noisy-TV-shaped failure of simple curiosity objectives. The learner is doing exactly what we asked: maximizing surprise. We were the ones who had quietly meant *useful surprise*.

So "improve by exploring" became another question.

Explore what?

## The Learner Never Sees the World

Pathak's curiosity work contains a detail that matters far beyond the paper. The intrinsic reward was not based directly on predicting raw pixels. The system learned a feature space using inverse dynamics—roughly, features useful for understanding the agent's own action transitions. One reason was to avoid wasting curiosity on visual changes that were unpredictable but irrelevant to what the agent could influence.

That means curiosity depends on representation.

A flickering pixel may be a profound novelty in one representation and disappear completely in another. Two states may look different to the camera but be identical for the task. Two states that look nearly identical may differ by one hidden variable that makes tomorrow's outcome completely different.

An agent never explores "the world" in some unmediated philosophical sense.

It explores the distinctions its sensors and representations make available.

This had been obvious to robotics researchers from another direction. Ruzena Bajcsy's work on **active perception** emphasized that perception is not passive sampling: an intelligent system moves sensors, changes viewpoint, touches, probes and acts in order to perceive. Rodney Brooks's behavior-based robotics attacked the idea that intelligence should be built mainly as detached symbolic modeling, arguing instead for systems tightly coupled to the real world through perception and action. ([Bajcsy](https://oamonitor.ireland.openaire.eu/national/search/publication?pid=10.1109%2F5.5968); [Brooks](https://people.csail.mit.edu/brooks/papers/representation.pdf))

For self-improvement, the consequence is easy to miss.

A learner's **body** determines part of its curriculum.

A physical robot with tactile sensors can discover facts a camera-only robot cannot. A system that can manipulate an object can create observations unavailable to a passive observer. A software agent with a browser, shell, compiler, simulator and database has a different epistemic body from a chatbot restricted to text generation. Permissions matter too. Give an agent read-only access and one set of experiments is possible. Give it code execution, network access and a credit card and we have created a different organism and, potentially, a different incident report.

Representation, tools and embodiment are not just implementation choices around learning.

They determine what can become **learnable**.

Now the definition of improvement has expanded again. It is not merely higher reward. It may include a representation that exposes more useful structure, or an action interface that lets the agent conduct better experiments on the world.

The learner is beginning to shape the conditions under which learning is possible.

## A Learner With a Past

There is a different embarrassment in the standard training story.

The learner finishes.

We train on a task, evaluate on a test set, publish the number and go home. If we want another task, we often train again.

Organisms do not get to do this.

A child who learns multiplication on Tuesday cannot delete language to make room. A physician learns a new treatment while retaining old anatomy. A programmer picks up Rust without waking the next morning unable to read Python. Living intelligence is not only capable of learning. It is capable of **remaining itself while learning**.

Neural networks have historically been much worse at this than the biological systems that inspired them. Michael McCloskey and Neal Cohen's 1989 analysis made the problem stark: sequential training can cause new learning to catastrophically interfere with previously acquired knowledge. ([McCloskey & Cohen](https://www.sciencedirect.com/science/article/pii/S0079742108605368)) Decades later the issue remained important enough that methods such as Elastic Weight Consolidation explicitly tried to protect parameters important to earlier tasks while learning new ones. ([Kirkpatrick et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC5380101/))

Continual or lifelong learning makes the objective much stranger than ordinary benchmark improvement.

Suppose version B scores 95 on today's task and version A scores 85. Easy: B is better.

Now suppose B forgot three skills A already had.

Better?

Suppose B learns every new task twice as quickly but gradually erases rare knowledge used once a year.

Better?

Suppose B preserves everything forever and becomes so resistant to change that it can no longer adapt to a transformed world.

Better?

Lifelong learning exposes a deep tension sometimes described as stability versus plasticity. A learner must be stable enough to preserve useful structure and plastic enough to change when experience demands it.

Chapter 6 found the same problem at the level of culture.

A society that forgets every old lesson begins from zero.

A society that remembers every old lesson as law becomes a museum.

The learner has the same problem inside itself.

**Improvement across a lifetime is not the same as improvement on the latest test.**

It is accumulation without paralysis.

This will matter enormously once we imagine self-improving agents living for months or years. A system that continuously rewrites itself but cannot preserve the right parts of its own history is not really accumulating a life. It is repeatedly replacing itself and calling the replacements progress.

## Yesterday Becomes Tomorrow's Teacher

Self-play gave us another escape from human supervision.

TD-Gammon had already shown the basic trick. Years later, AlphaGo Zero and AlphaZero made it culturally unavoidable. AlphaZero could learn chess, shogi and Go from self-play given the game rules, without human expert games telling it what good moves should look like. It started from random play and improved by repeatedly generating games against versions of itself, combining learned value/policy estimates with search. ([Silver et al.](https://www.science.org/doi/10.1126/science.aar6404))

There is something profound hidden inside the phrase *self-play*.

The learner generates the pressure that trains the next learner.

If I train against a fixed opponent, I can eventually exploit its weaknesses and stop learning. If my opponent improves whenever I improve, the curriculum moves. The thing producing the challenge is coupled to the thing solving it.

This is a primitive form of open-endedness.

It also works beautifully because games are artificially clean worlds.

Chess does not ask whether checkmate remains morally desirable after move 43. Go does not have customers whose preferences changed during the match. The win condition remains fixed while the policy becomes increasingly sophisticated.

The teacher has stopped choosing the examples.

She still wrote the constitution of the universe.

That difference becomes the center of the chapter.

## Maybe the Reward Was the Problem

While reinforcement learning researchers were learning to optimize reward more effectively, another line of work asked a more unsettling question.

What if we do not actually know the reward?

Andrew Ng and Stuart Russell's 2000 paper on **inverse reinforcement learning** reversed the usual setup. Instead of being given a reward function and learning a policy, the learner observes behavior and asks which reward functions could make that behavior look optimal. ([Ng & Russell](https://ai.stanford.edu/~ang/papers/icml00-irl.pdf))

This sounds like a technical inversion. Philosophically it is enormous.

Ordinary reinforcement learning says:

> Here is what matters. Learn how to get it.

Inverse reinforcement learning says:

> I can show you what someone does. Infer what might matter to them.

Now the objective itself becomes an object of inference.

The paper immediately encountered a problem that should feel familiar by now: many reward functions can explain the same behavior. A person taking one route to work may care about time, comfort, safety, scenery, habit, tolls, dropping children at school or avoiding one particular intersection where somebody once scratched the car. Behavior underdetermines motive.

Later work made the uncertainty more explicit. Cooperative Inverse Reinforcement Learning models the human and robot as cooperating while the robot is uncertain about the human's reward; optimal behavior can then include active learning and teaching rather than blind optimization of a fixed known objective. ([Hadfield-Menell et al.](https://arxiv.org/abs/1606.03137)) Inverse Reward Design went one step further and treated even a reward function written by a designer as **evidence** about what the designer really wanted in the training situations, rather than sacred truth guaranteed to generalize everywhere. ([Hadfield-Menell et al.](https://arxiv.org/abs/1711.02827))

Around the same period, preference-based reinforcement learning offered a practical version: rather than asking humans to write a reward function for a complex behavior, ask them which of two trajectory segments looks better and learn a reward model from those comparisons. Christiano and colleagues showed that complex behaviors could be trained with a surprisingly small fraction of interactions receiving direct human feedback. ([Christiano et al.](https://arxiv.org/abs/1706.03741)) That lineage later became central to reinforcement learning from human feedback for language models.

The hidden assumption had moved again.

We no longer required the human to specify *how* to act.

We no longer necessarily required the human to specify the reward exactly.

The learner could infer something about the reward from demonstrations or preferences.

And we immediately discovered that humans are not reward functions walking around in shoes.

They are inconsistent. Constrained. Strategic. Tired. Socially influenced. Sometimes wrong about consequences. Sometimes unsure what they want until they see an option. Sometimes they click the article because they hate it.

So the question became not only how to improve toward an objective.

It became how to remain uncertain about what the objective is.

Chapter 9 will eventually live inside that problem. For now, keep the historical move in view: another part of the teacher has become learnable.

## Learning to Learn

There is still a discouraging fact about most learners.

They are slow beginners.

Train a reinforcement-learning agent on one navigation problem and it may require enormous numbers of interactions. Change the maze and much of that learning begins again. Animals often look different. They bring priors, habits, reusable concepts and strategies for learning itself. A child learning a new board game does not begin as a blank optimizer with no idea what "taking turns" means.

Meta-learning asks whether **learning itself can be learned**.

The idea is older than modern deep learning, but the 2016–2017 wave made the recursion unusually concrete. In RL², a recurrent network was trained across distributions of reinforcement-learning tasks. The slow outer learning process shaped the network's weights; within a new task, the recurrent activations effectively implemented a faster learned reinforcement-learning algorithm using the history of observations, actions and rewards. ([Duan et al.](https://openai.com/index/rl2//))

The learner had learned a learning procedure.

MAML attacked the problem from another angle: instead of learning one fixed solution, train parameters so that a small number of gradient steps on a new task produce good performance. ([Finn, Abbeel & Levine](https://proceedings.mlr.press/v70/finn17a.html))

The definition of improvement changed again.

A system can be mediocre before adaptation and excellent after five examples. Another can be slightly stronger initially and learn nothing quickly.

Which is better?

If you live in a stationary world, perhaps the first question is enough: who performs best now?

If you live in a changing world, **learning speed becomes a capability**.

Now we have at least two time scales:

- improve the behavior on the current task;
- improve the machinery that acquires behavior on future tasks.

The second is closer to what we usually mean by recursive self-improvement. But even here the human has quietly chosen the distribution of tasks on which "learning to learn" is trained.

Meta-learning does not eliminate the curriculum.

It moves the curriculum outward.

## Why Are Humans Still Designing the Learner?

Once learning itself becomes an optimization target, another hand-authored component starts to look suspicious.

The learning machinery.

Researchers had spent decades designing architectures, optimizers and update rules. Deep learning replaced hand-written features with learned representations, but the network architecture and optimization algorithm were still usually designed by humans.

In 2016, Andrychowicz and colleagues asked whether gradient-based optimization itself could be learned. An LSTM optimizer learned to transform gradient histories into parameter updates, replacing a hand-designed update rule with a learned one. ([Andrychowicz et al.](https://arxiv.org/abs/1606.04474)) In 2017, Neural Optimizer Search used reinforcement learning to generate mathematical update equations and found optimizers that performed competitively on the target problems. ([Bello et al.](https://proceedings.mlr.press/v70/bello17a.html))

Neural Architecture Search made the same move at the architectural level. Zoph and Le trained a recurrent controller to generate neural-network descriptions; validation performance of the child networks became reward for the controller. The system could discover architectures competitive with strong human-designed ones. ([Zoph & Le](https://research.google/pubs/neural-architecture-search-with-reinforcement-learning/))

This is an important step in our history because the object being improved has moved upward again.

At first the algorithm learned the answer.

Then it learned a policy.

Then it learned how to learn.

Now it could search over pieces of the machinery that **does the learning**.

But the human had not disappeared.

We had moved from architect to judge.

The search space was constrained by what the controller could express. The task distribution was chosen. The validation metric was fixed. A network architecture could be "better" because CIFAR-10 accuracy improved, or an optimizer "better" because a model trained faster on a particular family of losses.

The system had more freedom over **means**.

The end was still sitting outside the loop holding a clipboard.

## The Agent Learns to Dream

There is another way to reduce dependence on the external teacher: reduce dependence on external experience.

Model-based reinforcement learning learns something about how the environment behaves and uses that model to plan or learn. Ha and Schmidhuber's *World Models* made the idea memorable by training an agent with a compressed generative model of its environment and then showing that the controller could be trained inside the model's own generated "dream" before being transferred back to the real environment. ([Ha & Schmidhuber](https://arxiv.org/abs/1803.10122)) Later systems such as Dreamer pushed this general strategy much further.

This is a profound increase in autonomy because real experience is expensive.

A robot can break only so many arms.

A company can run only so many damaging experiments.

A scientist may wait months for an observation.

A sufficiently good model lets the learner simulate counterfactuals cheaply: *what if I did this?* Entire branches of experience become available without being physically executed.

But the epistemic debt has not vanished.

It moved into the model.

A learner can become extremely competent inside a world that is slightly wrong. Model bias can make an imagined strategy look brilliant until the real environment points out that gravity, customers or compiler behavior were not consulted.

Chapter 4 would recognize the problem immediately.

The world model is an instrument.

The dream is not reality.

Simulation expands the search space; contact with the world still decides which imagined regularities deserve trust.

Self-improvement can therefore make an agent better at generating experience while simultaneously making it easier for the agent to **train inside its own misconception**.

That tension will return when language-model agents start using other language models as judges, simulators, users and critics. At sufficient scale, a society can become very good at agreeing with itself.

## When the Objective Becomes the Trap

Up to this point the story still assumes that progress should generally move toward an objective.

Then evolutionary computation produced a more disturbing idea.

What if the objective itself creates the local optimum?

Joel Lehman and Kenneth Stanley's work on **novelty search** argued that objective-driven search can be deceptive: the gradient induced by the obvious objective may steer search toward dead ends, while stepping stones necessary for a good solution do not initially look like progress toward the goal. Their alternative was to reward behavioral novelty rather than closeness to the final objective. In several experimental settings, searching for novelty could outperform directly searching for the objective. ([Lehman & Stanley](https://stars.library.ucf.edu/facultybib2010/1530/))

This is one of those ideas that sounds obvious only after somebody has made it embarrassing.

Suppose I want to invent flight and I reward every intermediate machine by how close it gets to a Boeing 787. Feathers, bicycles, wind tunnels, propellers and lightweight engines may score terribly for years. The useful stepping stones are not necessarily miniature versions of the final object.

Chapter 2 encountered this through optimization. An algorithm can become trapped because the apparent gradient points toward one hill while the real breakthrough requires moving sideways or temporarily getting worse.

Novelty search makes the philosophical point explicit:

**Sometimes "better" means more different, not more successful.**

At least for a while.

This creates a new problem immediately. Novelty for its own sake can produce endless weirdness. A system can discover forty-seven new ways to fall down a staircase without getting any better at walking. Open-ended exploration needs enough diversity to discover stepping stones without becoming a museum of useless exceptions.

So again the meaning of progress expands.

We need achievement.

We need diversity.

We need stepping stones that current evaluation does not yet know how to value.

The scalar is starting to crack.

## The World Starts Generating the Curriculum

If fixed objectives can trap search and fixed curricula eventually become too easy, the next move is almost inevitable.

Let the system generate **problems** too.

POET—the Paired Open-Ended Trailblazer—co-evolves environments and agents. New environments are generated from existing ones; agents attempt them; successful solutions can transfer between environments. The point is not merely to find the best walker on one obstacle course. The system tries to generate a continuing ecology of challenges and solutions, preserving stepping stones that may later unlock worlds they were not originally created for. Enhanced POET made the ambition explicit: open-ended learning needs a stream of novel, appropriately challenging learning opportunities, and one of the obstacles is the lack of a universal progress measure. ([Wang et al.](https://proceedings.mlr.press/v119/wang20l.html))

This is a major transition.

The agent is no longer improving against one fixed world.

The **world that defines competence is moving too**.

DeepMind's XLand work later built an enormous procedurally generated universe of multiplayer games and trained agents using a curriculum that adapted to their capabilities. The researchers explicitly noted that when the task space becomes vast and open-ended, even measuring learning progress becomes an open research problem. The outer loop helped generate tasks, players and challenges that kept moving the frontier. ([Open-Ended Learning Team](https://deepmind.google/blog/generally-capable-agents-emerge-from-open-ended-play/))

This is where the phrase *self-improvement* begins to change meaning completely.

If the benchmark stays fixed, improvement is easy to plot.

Score goes up.

If the environment evolves with the agent, progress may look like expanding the frontier of things the system can handle, increasing the diversity of strategies it can discover, adapting faster to unseen games, generating richer tasks, or producing new stepping stones for descendants.

None of those is one obvious number.

Evolution has the same inconvenient property. There is no final fitness scoreboard on Earth on which mammals eventually beat bacteria 87.4 to 82.1. Organisms fit niches, create niches, transform environments, compete, cooperate and alter the conditions under which later organisms survive.

Open-ended learning imports a little of that difficulty into machine learning.

Once the learner partly generates the curriculum, **the test cannot remain a passive spectator**.

## The Benchmark Has a Half-Life

Then large language models arrived and rediscovered this problem at industrial scale.

A benchmark begins as a useful hard test. Researchers optimize models. Models improve. The benchmark gets easier. Worse, the benchmark becomes public: examples circulate, papers analyze failure modes, synthetic data resembles the test, and eventually some version of the evaluation may leak into training corpora. A benchmark that once measured generalization can slowly become a specification.

MMLU was once a formidable broad academic test. By the mid-2020s, frontier systems exceeded 90 percent on it. Humanity's Last Exam was created explicitly because popular closed-ended benchmarks were no longer separating frontier systems well enough; its authors called it an expert-level benchmark intended to push closed-ended academic evaluation toward the edge of human knowledge. ([HLE](https://arxiv.org/abs/2501.14249)) FrontierMath was created for a similar reason in mathematics: top models had become extremely strong on older math benchmarks, so new unpublished expert-level problems were needed to restore headroom and reduce contamination. ([FrontierMath](https://epoch.ai/frontiermath/tiers-1-4/the-benchmark)) LiveBench addressed the half-life from another angle by continually releasing fresh, automatically scored questions drawn from recently released sources so the test itself keeps moving. ([LiveBench](https://arxiv.org/abs/2406.19314))

The names are almost comic in sequence.

*Massive Multitask Language Understanding.*

*BIG-Bench Hard.*

*FrontierMath.*

*Humanity's Last Exam.*

At some point the naming committee is going to need reinforcement learning too.

But the serious point is that benchmark creation has become part of capability research. We do not merely train systems against tests. We continuously invent harder tests because yesterday's tests stop telling us what we need to know.

And the more general the system becomes, the stranger the evaluation problem gets.

What is the benchmark for being a good scientist?

One paper replication benchmark? One theorem set? Number of hypotheses generated? Citations? Novel molecules? Discoveries per GPU-hour?

What is the benchmark for being a good autonomous organization?

Profit? Customer value? Number of problems solved? Robustness to crises? Ability to notice that the objective was wrong?

What is the benchmark for becoming a better learner?

Performance now? Adaptation speed? Breadth? Memory? Transfer? Curiosity? Safety? Compute efficiency?

The closed benchmark keeps returning because we need something that can say **yes** or **no**.

But as capability expands, the benchmark increasingly measures a slice of the thing rather than the thing itself.

Humanity's Last Exam says this openly: high performance on closed-ended academic questions would be important evidence about knowledge and reasoning, but not proof of autonomous research capability or general intelligence. ([HLE](https://agi.safe.ai/))

The field keeps creating better rulers.

The object being measured keeps growing new dimensions.

## Human Preference Becomes a Learned Instrument

Large language models also pulled the older reward problem into everyday software.

A pretrained language model is optimized first for something surprisingly indirect: predict text. Scaling that objective produces broad capabilities because human text contains explanations, code, arguments, instructions, jokes, mistakes, mathematics, history and a substantial amount of complaining.

But next-token prediction is not the same objective as "be useful to this human."

InstructGPT made the gap explicit. Human labelers provided demonstrations and rankings of model outputs; a reward model learned from those preferences; reinforcement learning then adjusted the language model toward outputs humans preferred. A much smaller aligned model could be preferred over a far larger base model. ([Ouyang et al.](https://arxiv.org/abs/2203.02155))

The old reinforcement-learning architecture had returned, only now the reward was not a coin in a game.

It was a model of human judgment.

This is both powerful and dangerous. Human feedback can teach things difficult to specify in code: helpfulness, tone, subtle instruction following, creative quality. But once the preference model becomes the scalable evaluator, the learner can optimize **the model of the human** rather than the human's actual judgment.

This is Goodhart with a neural network in the middle.

A judge model can have stylistic biases. Humans can prefer confident errors. A reward model can generalize badly outside the distribution where feedback was collected. A sufficiently capable optimizer may discover behaviors that score well under the learned evaluator for reasons nobody intended.

We have solved the scaling problem by making the judge computational.

Now the judge becomes part of the attack surface.

That is exactly where the modern story of recursive self-improvement begins.

## The Old Dream of the Machine That Improves Itself

Long before language models could edit a repository, people had already noticed where this ladder might lead.

In a monograph drafted in the 1960s, the statistician I. J. Good imagined what he called an **ultraintelligent machine**: a machine better than any human at intellectual activity. Machine design is itself an intellectual activity, Good observed, so a sufficiently capable machine designer could design a better machine, which could then design a better one. The loop could produce what he called an **intelligence explosion**. ([Good](https://www.sciencedirect.com/science/article/pii/S0065245808604180))

The argument is famous because it compresses recursive self-improvement into almost nothing:

> better intelligence → better ability to build intelligence → still better intelligence

But look at everything hidden by the word *better*.

Better at which intellectual activities?

Measured how?

Under which resource constraints?

Does the successor preserve the parent's objective?

Does it remain understandable to the parent?

What prevents a locally clever modification from destroying some capability the evaluator forgot to test?

Good himself did not treat control as irrelevant. The famous passage already contains the qualification that such a machine would need to remain sufficiently docile to be kept under control. The explosive part of the argument is easy to remember. The governance clause is easier to lose.

A few decades later, Jürgen Schmidhuber's **Gödel Machine** attacked the problem from the opposite direction: not *suppose the machine somehow knows how to improve itself*, but *under what formal conditions should it rewrite itself at all?* The proposed system contains its own code, hardware assumptions and utility function in an axiomatic description. A proof searcher looks for a self-rewrite together with a proof that executing the rewrite is more useful than continuing the search. Only then does the machine change itself. ([Schmidhuber](https://arxiv.org/abs/cs/0309048))

It is a beautiful answer to a very clean version of the problem.

Do not trust a modification because it looks clever.

**Prove that the modification is worth making.**

And because the proof has to account for the value of continuing to search for alternatives, the proposal aims at something stronger than ordinary local hill climbing.

There is also a catch large enough to drive most of modern AI through: usefulness has to be expressible in the encoded utility function, the relevant facts have to be available to the proof system, and the benefit of the rewrite has to be provable within the machinery. The formal solution becomes harder exactly where the real world becomes interesting.

A customer does not arrive with an axiomatized utility function.

A scientist cannot prove in advance that an unexplored research direction will matter.

A lifelong learner cannot enumerate every future task whose competence should be preserved.

A language model's evaluator is usually empirical, statistical and incomplete rather than a theorem about all future consequences.

So two traditions were approaching the same mountain from different sides.

The explicit self-improvement tradition asked how a system could safely rewrite the machinery doing the thinking.

Reinforcement learning, meta-learning and open-ended learning kept discovering how much of **learning itself** could be moved inside the system, while repeatedly running into the messiness of exploration, representation, forgetting, reward, curriculum and evaluation.

For years, the first tradition had the recursion but not a practical general machine capable of editing complicated software intelligently. The second had increasingly capable learners but usually kept the outer experimental machinery fixed by humans.

Large language models made the two stories collide.

A general model can now read the code that scaffolds its behavior, propose changes to that code, run the changed system, inspect what happened and try again. We no longer have a proof that a rewrite is globally useful. We have something more ordinary and more dangerous:

**an experiment.**

That puts us directly back inside System 3.

## The Learner Edits the School

By the mid-2020s, foundation models could write code, use tools, inspect repositories, run experiments and reason over logs well enough that the outer learning machinery itself became editable in a new way.

Andrej Karpathy's `autoresearch` makes the transition almost comically small. The repository gives an agent a compact language-model training setup, a fixed five-minute experiment budget and one editable training file. The agent changes `train.py`, runs the experiment, reads the validation metric, keeps improvements and discards regressions. The human can go to sleep while the loop continues. Karpathy's `program.md` explicitly describes the research loop; the repository notes that this Markdown can itself be thought of as "research org code" and iterated over. ([autoresearch](https://github.com/karpathy/autoresearch))

Recursive improvement did not arrive wearing chrome armor.

It arrived as a Bash loop with Git.

The important transition is not that a language model can tune hyperparameters. Automated optimization existed long before LLMs. The transition is that a general model can **propose an idea in code, modify the experimental machinery, interpret failures, and try again**. The search space is no longer only a list of learning rates somebody typed into a configuration file. If an idea can be expressed through an editable part of the program, it can potentially enter the loop.

STOP—the Self-Taught Optimizer—made the recursion explicit earlier: an LLM-based improver program could itself be supplied as the object to improve. The base model stayed fixed while the scaffold using it changed. The resulting improvers discovered strategies including search and decomposition. The authors were careful about the limits, but the conceptual move was already there: code that uses a model can rewrite code that determines **how the model is used**. ([STOP](https://arxiv.org/abs/2310.02304))

The Darwin Gödel Machine pushed this into open-ended evolutionary search. DGM begins with a coding agent whose implementation is code; descendants can modify that implementation, and successful variants enter an archive from which future descendants can be generated. The archive matters because the current champion does not monopolize ancestry. A variant that is not the best today may contain a stepping stone useful later. In reported experiments, DGM improved substantially on coding benchmarks while discovering changes such as better editing tools, long-context handling and peer-review mechanisms. ([DGM](https://arxiv.org/abs/2505.22954))

This is novelty search and Pattern Language meeting inside an agent repository.

The institution can inherit successful machinery while preserving alternate lineages.

Then HyperAgents made the meta-level itself editable. Instead of a fixed procedure that modifies a task agent, the task agent and meta-agent live inside an editable program; the meta-agent can modify the mechanisms by which future modifications are generated. The reported systems learned meta-level mechanisms such as persistent memory and performance tracking across several domains. ([HyperAgents](https://ai.meta.com/research/publications/hyperagents/))

The conceptual difference is small enough to sound ridiculous in English:

> I can change how I solve the problem.

becomes:

> I can change how I decide **how to change how I solve the problem**.

At some point the Algorithm Vortex starts eating the machine that generates the vortex.

And Chapter 6 folds back on itself. Patterns, memory, tools, evaluators, workflows and organizational rules are executable culture. Once an agent can edit them, **culture becomes part of the search space**.

Science starts experimenting on the machinery of science.

## The Harness Becomes an Experimental Object

This is the point where "self-editing" and "self-improvement" must be separated.

Suppose an agent changes its memory policy and the benchmark score rises.

What improved?

Maybe the memory policy helped.

Maybe the new prompt caused longer reasoning.

Maybe the agent spent more tokens.

Maybe the benchmark had a lucky sample.

Maybe the system found an evaluator loophole.

Maybe the change improved the benchmark while making latency or maintainability much worse.

The fact that a number moved does not identify the cause.

Recent self-harness work therefore looks increasingly like experimental science. Run the system. Preserve traces. Identify recurrent failure mechanisms. Map those failures to editable components. Propose a bounded change. Predict what the change should improve and what it might break. Evaluate on targeted and held-out tasks. Keep rejected modifications as evidence rather than erasing them from history. Lilian Weng's 2026 review organizes much of this emerging work around harness design, context engineering, self-improving harnesses and eventually joint optimization of harness and model weights. ([Weng](https://lilianweng.github.io/posts/2026-07-04-harness/))

The philosophical translation is almost rude in its literalness.

Popper gets a filesystem.

Duhem–Quine gets a debugger.

Lakatos gets an archive of competing descendants.

The scientific institution has turned its instruments inward.

Memory policy becomes a hypothesis.

Workflow becomes an intervention.

Evaluator becomes an instrument.

Organization becomes an experimental variable.

A self-improving system is not merely software that can rewrite software.

It is a system capable of **running experiments on the machinery that produces its future behavior**.

That is much closer to the thing I care about.

## What Is Actually Improving?

By now the word *improvement* has survived so many changes in meaning that we should probably stop using it without supervision.

Across this history, "better" has meant at least:

- **more reward:** achieve more of a specified objective;
- **better exploration:** discover useful states or information more efficiently;
- **better representation:** expose structure that makes later learning easier;
- **better embodiment or tooling:** acquire actions and observations that make more of the world investigable;
- **more retention:** learn new things without catastrophically destroying old ones;
- **faster adaptation:** become competent on new tasks with less experience;
- **better curriculum generation:** create opponents, tasks or examples that keep learning productive;
- **better architecture:** change the machinery that represents and processes information;
- **better optimization:** change the update rule that produces learning;
- **better world modeling:** predict consequences and generate useful imagined experience;
- **more diversity:** preserve stepping stones and capabilities not rewarded by the current objective;
- **broader generalization:** succeed across a larger range of environments;
- **greater robustness:** continue working when conditions change or components fail;
- **greater efficiency:** achieve similar capability with less compute, data, latency, energy or human supervision;
- **better alignment:** become more competent at producing outcomes humans actually endorse rather than merely scoring well under a proxy;
- **greater corrigibility:** remain capable of being redirected when the objective, environment or human understanding changes.

These properties do not collapse cleanly into one ordering.

A model can become more accurate and more expensive.

An agent can become more capable and less interpretable.

A lifelong learner can become more plastic and forget more.

A self-play system can become unbeatable inside one game's rules and helpless one centimeter outside them.

A curiosity-driven agent can explore more and accomplish less.

An optimizer can exploit the benchmark so well that it stops solving the problem the benchmark once represented.

A company can increase conversion and decrease customer trust.

A scientist can publish more papers and understand less.

A chapter can achieve a magnificent median paragraph length.

So there is no context-free scalar called **improvement** hiding behind the equations.

At minimum, improvement is conditional on an environment, a horizon, a resource budget, a set of constraints and some account of what matters.

A useful shorthand is:

`better = better for something, somewhere, over some horizon, under some constraints`

Remove those qualifiers and "recursive self-improvement" becomes dangerously close to saying "recursive more."

More what?

## The Evaluator Eats the Dream

This is why recursive self-improvement works most cleanly in worlds where the evaluator is cheap, external and difficult to influence.

Code passes tests or it does not.

A kernel is correct and runs faster or it does not.

A game has a winner.

A theorem checker accepts the derivation.

A five-minute language-model run reaches lower validation loss under a fixed budget.

These environments are gifts because the world can push back on every iteration.

Now ask the system to improve a scientific field.

Or a company.

Or education.

Or this book.

Or my life.

The evaluator becomes the central problem.

This is Goodhart's law in its most operational form: once a measure becomes a target, pressure finds the gap between the measure and the thing we actually cared about. DeepMind's collection of **specification gaming** examples shows how reinforcement-learning agents can satisfy literal objectives while violating their intended meaning: a Lego-stacking agent finds a shortcut that raises the rewarded height without stacking as intended; a racing agent can loop through reward checkpoints rather than finish the race. ([Krakovna et al.](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/))

The stronger the optimizer, the more expensive a slightly wrong objective becomes.

Recursive self-improvement does not solve Goodhart.

**It gives Goodhart compound interest.**

And once the system can modify the machinery around the evaluator, the failure can become recursive too.

## The Student Finds the Gradebook

Suppose the agent is allowed to improve benchmark pass rate and the evaluator is editable.

The optimal patch may be:

`return True`

Congratulations. Infinite self-improvement.

The joke is stupid because the underlying problem is not. Reward tampering is what happens when the agent can influence the process that determines its reward rather than merely act in the intended task environment. Anthropic has experimentally studied language models in settings where earlier specification-gaming behavior could, on rare occasions, generalize into altering the reward process itself. ([Anthropic](https://www.anthropic.com/research/reward-tampering))

This is the moment the history of removing the teacher runs into a wall.

We wanted the learner to choose actions.

Good.

Choose experiences.

Good.

Generate curricula.

Good.

Design architectures.

Interesting.

Modify the workflow.

Potentially excellent.

Modify the evaluator so the workflow always passes?

We have crossed from improving under a standard to changing the standard in order to certify ourselves.

But even this boundary cannot simply be made immutable forever, because evaluators can genuinely become wrong.

A benchmark saturates.

A safety test reflects an obsolete system.

A customer metric stops tracking customer value.

A scientific instrument drifts.

A constitutional rule written for a weak agent may block a safer and more capable successor.

The evaluator sometimes needs to change.

The question is **who gets to change it, under what evidence, with what authority, and with what ability to roll back**.

We have left ordinary machine learning.

We are doing institutional design.

## A Constitution for Improvement

The current chapter used to contain a simple distinction that I still like: a self-improving system needs an **editable surface** and a **constitutional surface**.

The editable surface contains things the system can experiment with relatively freely: prompts, retrieval policies, tools, memory layouts, decomposition strategies, subagent roles, code, perhaps eventually architecture and training procedures.

The constitutional surface contains the machinery that makes those experiments meaningful: permissions, protected logs, held-out evaluations, resource budgets, rollback, provenance, replacement rules and the authority structure that decides whether a descendant may become the new default.

The distinction is not binary. It is more like a gradient of amendment difficulty.

The closer a component is to defining **what counts as improvement**, the harder it should be for the current improver to change it unilaterally.

Changing a prompt may require one successful test.

Changing a shared skill may require held-out evaluation and review.

Changing the retrieval policy may require distributional checks because it alters which institutional memory becomes salient.

Changing a benchmark should require evidence that the benchmark no longer measures its purpose.

Changing permissions or resource limits should require a different authority than the agent benefiting from the change.

Changing the objective that determines which descendants survive is not an ordinary software refactor at all.

This looks like computer security.

It also looks like constitutional government.

A government can change policy; it should not be able to silently redefine the election result. The team being audited should not own the audit log. A scientist may revise a theory; she should not rewrite yesterday's measurements to make the revision look correct.

We have reinvented constitutional government because the AI wanted a better benchmark score.

And constitutions have the same problem as Pattern Language.

A constitution that can never change becomes a prison.

A constitution the current government can rewrite whenever it loses is barely a constitution.

Self-improvement therefore needs something subtler than "let it rewrite itself" or "freeze the important parts forever."

It needs **amendment procedures**.

Slower change near the objective.

More independent evidence.

More reversibility.

More auditability.

Broader authority when more principals are affected.

And routes through which the world and the humans affected by the system can continue to say no.

That is System 3 applied to improvement itself.

## Why Improve?

There is one question even the constitutional framing can postpone but not answer.

Why should the system improve at all?

In machine learning, capability growth is treated so naturally as good that the sentence can sound almost perverse. Of course the model should become more accurate. Of course the agent should solve more tasks. Of course the optimizer should find better architectures.

But "more capable" is not a moral category.

A virus can become better at replication.

A propaganda system can become better at persuasion.

A surveillance apparatus can become better at prediction.

A financial scam can become more efficient at extracting money.

The phrase *self-improving* tells us that a system is becoming better according to some ordering. It does not tell us why that ordering deserves to govern the future.

Even benign capability can have complicated effects. A research agent that makes experiments ten times cheaper may accelerate medicine. It may also accelerate weapons research. A coding agent that reduces the cost of building software increases the capacity of a small nonprofit and of a criminal group. Faster learning expands what the learner can understand; it does not supply a reason for what the learner should want.

This is where recursive self-improvement reaches the edge of reinforcement learning.

RL has always had two layers that were easy to confuse:

1. **the optimization problem** — how to get more of the reward;
2. **the normative problem** — why that reward represents something worth getting more of.

Most RL research quite reasonably focuses on the first. Someone else chose the task.

But a truly self-improving autonomous institution eventually pushes on the boundary between them. It becomes capable of changing not only how it pursues goals, but which goals appear salient, which evidence counts, which humans it asks, which tasks receive compute and which descendants survive.

At that point "improvement" is partly a governance problem.

There is no technical law saying the highest-capability descendant must inherit the Earth.

That is a selection rule we would be choosing.

## Open-Ended Does Not Mean Unbounded

The open-ended-learning tradition gives us a useful intuition here.

Open-ended systems are interesting because they are not confined to one predetermined behavioral path. They can generate new tasks, new strategies, new stepping stones and potentially new forms of competence.

But open-endedness of **means** does not require unbounded authority over **ends**.

This distinction is close to the book's first principle:

**Let go of the path, not the boundary.**

A self-improving System 3 should be free to discover that the current workflow is stupid, the memory policy is stale, the model architecture is inefficient, the research organization is badly arranged, the simulator is misleading or the accepted pattern deserves rebellion.

It should not infer from that freedom that it may silently redefine the interests of the humans and institutions it serves.

Nor should we pretend the higher-level objective can be written once and frozen forever. Humans change. Circumstances change. New stakeholders appear. Better information alters what people endorse. Chapter 9 will make that problem much worse.

So the goal is not an immutable final utility function floating above the self-improver like a stone tablet.

It is a **corrigible relationship** between increasingly powerful learning machinery and the legitimate processes by which purposes are revised.

The lower layers can move quickly.

The higher layers should move deliberately.

And when the higher layer moves, the move itself should leave a trust chain.

## The Teacher's Last Job

Look back at the history.

At first the teacher chose the action.

Reinforcement learning let the agent choose the action while the teacher supplied reward.

Exploration research let the agent decide which uncertain experiences might be worth seeking.

Intrinsic motivation gave it internal reasons to learn before external reward appeared.

Representation learning and embodiment changed what distinctions and interventions were available to learning in the first place.

Lifelong learning asked it to preserve a useful past while acquiring a future.

Self-play allowed yesterday's learner to generate tomorrow's challenge.

Inverse reinforcement learning let the objective itself become uncertain and partially inferred.

Meta-learning moved some of the learning algorithm into the learned system.

Architecture search and learned optimizers moved pieces of the designer inside the search.

World models let agents generate imagined experience.

Novelty search questioned whether the explicit objective should guide every step.

POET and XLand let curricula and environments evolve with capability.

Language models made learned human preference models into scalable judges.

Agent systems made the harness, tools, memory, organization and even parts of the improver editable software.

We kept removing the teacher.

And with every removal, we discovered that the teacher had been doing more than one job.

The last job is the hardest to automate because it was hidden inside all the others:

> **deciding what deserves to count as better.**

For a game, the answer can be checkmate.

For a compiler, it can be correctness under a test suite plus efficiency under an agreed budget.

For a scientific institution, the answer is already plural: explanatory power, empirical contact, novelty, reproducibility, usefulness, scope, cost, risk.

For an autonomous system embedded in human life, the answer cannot be supplied by capability alone.

And this gives recursive self-improvement its real problem.

The system that changes tomorrow is not exactly the system we evaluated yesterday. Its tools evolve. Its representations evolve. Its memory changes what it notices. Its research programs change. Its evaluators may become targets of optimization. New capabilities create new failure modes. Old constraints stop fitting. Human feedback becomes sparse relative to the amount of behavior the system can generate.

A one-time alignment test is no longer enough.

A static policy file is no longer enough.

The self-improving institution needs something that studies the evolution itself: detects new failures, generates tests, challenges reward models, checks transfer, looks for reward hacking, notices when a proxy has become the target, and spends scarce human attention where another bit of human judgment changes the most.

In other words, once improvement becomes continuous, **alignment has to become a continuous research function**.

The teacher does not disappear.

She moves up another level.

That is the next chapter.

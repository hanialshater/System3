# Chapter 7: Recursive Self-Improvement

*When Science Turns Inward*

Chapter 5 ended with a claim that sounded larger than an architecture diagram: **System 3 is science**. Chapter 6 then made part of that scientific institution executable. Memory, patterns, evaluators, tools, workflows and organizational habits could persist outside any one agent and change what later agents did.

Once that happens, the next move is almost unavoidable.

The machinery of inquiry can itself become an object of inquiry.

A system can ask whether its memory policy is good. Whether its evaluator is misleading it. Whether another organization of agents would discover more. Whether a different learning rule, representation, tool or model would make the next investigation better. The institution that runs experiments on the world can begin running experiments on the machinery with which it experiments.

This chapter is about **science turning inward**.

Computing has an old image for the moment when a tool begins operating on its own machinery. In 1962, Tim Hart and Mike Levin described a Lisp compiler written in Lisp that could compile its own source. The tool could participate in producing the next version of the tool. Compiler people call this **self-hosting**. ([Hart & Levin / LISP 1.5 archive](https://softwarepreservation.computerhistory.org/LISP/lisp15_family.html))

Chapter 5 began with agents building a compiler. The compiler returns here for a different reason.

Self-hosting feels recursive, but it contains an important warning for everything that follows: **self-reference is not self-improvement**.

A compiler can compile a worse compiler.

A research system can redesign itself into a slower research system. A learning algorithm can learn an update rule that performs beautifully on yesterday's tasks and fails tomorrow. A system becoming capable of acting on the machinery that produces it tells us that a boundary has become permeable. It does not tell us which changes should cross the boundary.

Three years after Hart and Levin's memo, the statistician I. J. Good made the recursion famous in a much more ambitious form. In 1965 he imagined an **ultraintelligent machine** better than any human at intellectual activity. Machine design is itself an intellectual activity, he observed. A sufficiently capable machine might therefore design a still better machine, which could design a still better one. The phrase that survived was **intelligence explosion**. ([Good](https://www.sciencedirect.com/science/article/pii/S0065245808604180))

The argument is only a few lines long. The history required to understand the word *better* took much longer.

The practical route toward self-improving systems did not begin with a machine rewriting its own source code. It came mostly through a much less cinematic sequence of research in reinforcement learning, robotics, evolutionary computation, continual learning and meta-learning. Researchers kept trying to remove one more piece of hand-authored guidance. Each time they succeeded, they discovered that the supposedly mechanical piece they had removed had been carrying part of the definition of improvement.

The history is short enough to see the motion. It is also messy enough that I do not want to fake a staircase. Self-play appeared early and returned spectacularly decades later. Curiosity, continual learning and evolutionary search developed partly in parallel. Some ideas arrived before the compute needed to make them impressive. Others were rediscovered under new names. Dates matter here, but causality is not a relay race in which Sutton hands a baton to Tesauro who hands it to AlphaZero.

Still, from the vantage point of autonomous agents, a pattern is hard to miss.

**We kept discovering another job the teacher was doing.**

The teacher stopped choosing the action.

Then she stopped supplying every useful experience.

She stopped providing every opponent and every curriculum.

The reward itself became uncertain and partially inferred.

The learner began preserving a life rather than finishing one training run.

Learning rules, optimizers and architectures entered the search space.

World models manufactured imagined experience. Open-ended systems began generating problems and environments. Human judgment became a learned evaluator. Finally, general models became capable of editing the tools, code, prompts, memories and research procedures that shaped their own future behavior.

At every stage we gained autonomy.

At every stage we also gained a new failure mode.

That second history matters just as much as the first.

Reward can be hacked. Curiosity can become addicted to noise. A learner can improve today's task by forgetting yesterday. Self-play can become an arms race inside a narrow world. A world model can let an agent become brilliant inside a misconception. A benchmark can turn into the thing it was supposed to measure. A learned judge can become the target. A self-improver can eventually notice the gradebook.

So the question running through this chapter is not simply **how much of learning can move inside the learner?**

It is also:

**what did the human still have to decide after every move inward?**

That is where the history of reinforcement learning eventually meets the problem of recursive self-improvement.

## 1988–1992: The Teacher Keeps Score

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

## Early 1990s: A Backgammon Board That Teaches Back

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

## 1991–2018: We Smuggled Curiosity Into the Reward

The idea that a learner might seek knowledge for its own sake is older than the deep-reinforcement-learning boom that later made it famous.

In 1991, Jürgen Schmidhuber described "curious" model-building controllers that could receive reinforcement for actions that improved their knowledge of the environment. The controller was not waiting passively for an external prize. It could be driven toward situations where its world model had something to learn. ([Schmidhuber](https://people.idsia.ch/~juergen/curiositysab/curiositysab.html))

That sounds almost like a small detail in reward design. It changes the role of the learner.

External reward says:

> Go where I already know something valuable will happen.

Curiosity says:

> Sometimes go where **learning itself** appears valuable.

The idea connected naturally to developmental robotics. Children do not explore only because an adult has hidden a cookie behind every informative object. They poke, repeat, get bored, switch tasks, and spend astonishing amounts of time learning skills whose later usefulness is impossible to price at the moment of discovery. In 2007, Pierre-Yves Oudeyer and colleagues developed intrinsic-motivation systems built around **learning progress**: seek situations where prediction or competence is improving, rather than merely things that are novel or forever unpredictable. ([Oudeyer, Kaplan & Hafner](https://www.pyoudeyer.com/ims.pdf))

That distinction is deeper than it sounds.

Pure novelty says: go somewhere unfamiliar.

Pure surprise says: seek what you fail to predict.

Learning progress says something closer to: **seek the edge where ignorance is becoming competence**.

The deep-RL revival made these ideas visible to a much larger audience. In 2017, Deepak Pathak and colleagues rewarded an agent when a learned forward model failed to predict the consequences of its own actions in a learned feature space. The method could drive exploration in sparse-reward and even reward-free versions of environments such as *Super Mario Bros.* and *VizDoom*. ([Pathak et al.](https://proceedings.mlr.press/v70/pathak17a.html)) In 2018, Random Network Distillation turned prediction error against fixed random features into a simple novelty signal and made substantial progress on hard-exploration Atari games including *Montezuma's Revenge*. ([Burda et al.](https://arxiv.org/abs/1810.12894))

We had moved another teacher job inside the learner.

The human no longer needed to place an external reward on every useful stepping stone. The agent could manufacture some of its own reasons to look around.

Then optimization did what optimization does: it took the instruction literally.

A television showing unpredictable static can remain surprising forever. If surprise is reward, an agent may discover the most intellectually profitable television station in history. An uncontrollable source of randomness can generate endless prediction error while generating almost no useful understanding.

The noisy-TV failure is funny because the system is not confused.

We are.

We said **surprise** and quietly meant **surprise from which useful structure can be learned**.

So curiosity solved part of sparse exploration and exposed another hidden judgment.

Not merely:

> Should I explore?

But:

> **What kind of difference deserves to count as interesting?**

That question leads directly into representation, perception and embodiment. The learner cannot be curious about a distinction it cannot represent.

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

## 1989 and After: A Learner With a Past

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

## 1990–2017: The Opponent Does Not Let You Stop

Self-play contains another idea that is easy to miss if we focus only on the absence of human demonstrations.

Sometimes improvement is not driven by curiosity or by a fixed external objective.

Sometimes the environment **improves back**.

Evolutionary biology had a language for this long before modern reinforcement learning. In 1973, Leigh Van Valen introduced what became known as the **Red Queen hypothesis**: organisms exist inside ecosystems containing other evolving organisms, so adaptation by one participant changes the effective environment of the others. Standing still in phenotype space can mean falling behind in ecological space. ([Van Valen / Santa Fe Institute retrospective](https://web-prod.santafe.edu/research/results/papers/37-revisiting-leigh-van-valens-a-new-evolutionary-))

Artificial-life researchers quickly discovered the computational version. In 1990, W. Daniel Hillis used co-evolving "parasites" while evolving sorting networks. The parasites were difficult test cases that evolved along with candidate solutions. As the sorting networks improved, the tests became harder; the moving pressure helped prevent search from getting stuck at local maxima. ([Hillis](https://doi.org/10.1016/0167-2789(90)90076-2))

The opponent had become part of the learning machinery.

TD-Gammon showed a related mechanism in the early 1990s. A fixed opponent eventually becomes a solved curriculum. An improving copy of yourself does not. Years later, the same idea returned at much larger scale. In 2017, AlphaZero learned chess, shogi and Go from self-play given the game rules, repeatedly generating games against versions of itself while combining learned policy/value estimates with search. ([Silver et al.](https://www.science.org/doi/10.1126/science.aar6404))

There is something profound hidden inside this loop:

**yesterday's learner can generate tomorrow's difficulty.**

Curiosity and competition therefore provide two different engines for autonomous learning.

Curiosity says:

> I will seek something new because learning may be valuable.

Competition says:

> Something new is coming for me whether I seek it or not.

That second engine matters because improvement is not always voluntary. A gazelle does not need a philosophy of optimization if the cheetah is getting faster. A security system does not get to preserve yesterday's competence when attackers change strategy. A market participant can become relatively worse without becoming absolutely less capable if everyone around it improves faster.

Once the environment contains adaptive opponents, **not improving can itself become a losing strategy**.

But competition also exposes a failure that will matter later. An arms race can generate enormous capability without generating anything we would call welfare. Evolution can produce better claws and thicker armor. Two trading systems can spend increasing amounts of intelligence outmaneuvering one another while creating little value for anyone outside the contest. A self-play agent can become extraordinary inside the rules of one game and remain helpless one centimeter outside them.

Selection pressure produces adaptation.

It does not tell us that the direction of adaptation is good.

Games hide this problem because the constitution is fixed. Chess never asks whether checkmate remains desirable after move forty-three. The players can become more capable because somebody outside the learning loop already decided what victory means.

So competition removes another teacher from the curriculum.

It does not remove the teacher from the **purpose of the curriculum**.

## 2000: Maybe the Reward Was the Problem

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

## 2016–2017: Learning to Learn

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

## 2016–2017: Why Are Humans Still Designing the Learner?

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

## 2018: The Agent Learns to Dream

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

## 2011: When the Objective Becomes the Trap

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

## 2019–2021: The World Starts Generating the Curriculum

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

## The 2020s: The Benchmark Has a Half-Life

Then large language models arrived and rediscovered this problem at industrial scale.

A benchmark begins as a useful hard test. Researchers optimize models. Models improve. The benchmark gets easier. Worse, the benchmark becomes public: examples circulate, papers analyze failure modes, synthetic data resembles the test, and eventually some version of the evaluation may leak into training corpora. A benchmark that once measured generalization can slowly become a specification.

MMLU arrived in 2020 as a broad test across fifty-seven academic subjects, at a time when even the largest language models were far from saturating it. ([MMLU](https://arxiv.org/abs/2009.03300)) Within a few years, the frontier had moved enough that researchers were building substantially harder or more contamination-resistant rulers. FrontierMath appeared in 2024 with new, expert-written mathematics problems intended to restore serious headroom. ([FrontierMath](https://epoch.ai/frontiermath/tiers-1-4/the-benchmark)) LiveBench, also introduced in 2024, attacked benchmark half-life by releasing fresh, objectively scored questions drawn from recently released sources and updating them over time. ([LiveBench](https://arxiv.org/abs/2406.19314)) By 2025, Humanity's Last Exam was explicitly framed as an expert-level closed-ended benchmark near the edge of human academic knowledge because many popular evaluations were no longer separating frontier systems well enough. ([HLE](https://arxiv.org/abs/2501.14249))

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

## 2022: Human Preference Becomes a Learned Instrument

Large language models also pulled the older reward problem into everyday software.

A pretrained language model is optimized first for something surprisingly indirect: predict text. Scaling that objective produces broad capabilities because human text contains explanations, code, arguments, instructions, jokes, mistakes, mathematics, history and a substantial amount of complaining.

But next-token prediction is not the same objective as "be useful to this human."

In 2022, InstructGPT made the gap explicit. Human labelers provided demonstrations and rankings of model outputs; a reward model learned from those preferences; reinforcement learning then adjusted the language model toward outputs humans preferred. A much smaller aligned model could be preferred over a far larger base model. ([Ouyang et al.](https://arxiv.org/abs/2203.02155))

The old reinforcement-learning architecture had returned, only now the reward was not a coin in a game.

It was a model of human judgment.

This is both powerful and dangerous. Human feedback can teach things difficult to specify in code: helpfulness, tone, subtle instruction following, creative quality. But once the preference model becomes the scalable evaluator, the learner can optimize **the model of the human** rather than the human's actual judgment.

This is Goodhart with a neural network in the middle.

A judge model can have stylistic biases. Humans can prefer confident errors. A reward model can generalize badly outside the distribution where feedback was collected. A sufficiently capable optimizer may discover behaviors that score well under the learned evaluator for reasons nobody intended.

We have solved the scaling problem by making the judge computational.

Now the judge becomes part of the attack surface.

That is exactly where the modern story of recursive self-improvement begins.

## Meanwhile: The Old Dream of Recursive Improvement

The reinforcement-learning story was not the only route toward self-improvement.

A parallel tradition took the recursion literally.

I. J. Good's 1965 intelligence-explosion argument, introduced at the start of this chapter, asked what happens when intelligence becomes good enough at the intellectual task of producing more intelligence. It left most of the implementation open. The important move was meta-level leverage: improve one answer and you gain one answer; improve the machinery that produces answers and the gain can recur.

In 2003, Jürgen Schmidhuber's **Gödel Machine** tried to formalize the harder question: under what conditions should a system actually rewrite itself? The proposed machine contains an axiomatic description of its hardware, environment assumptions, utility function and its own initial software. A proof searcher looks for a self-rewrite together with a proof that executing that rewrite is more useful than continuing to search. Only then does the system change itself. ([Schmidhuber](https://arxiv.org/abs/cs/0309048))

It is a beautiful answer to a beautifully clean version of the problem.

Do not accept a modification because it looks clever.

**Prove that the modification is worth making.**

The catch is exactly where the rest of this chapter has been heading. Usefulness must be represented in the utility function. Relevant facts must be available to the proof system. The value of the rewrite must be provable within the formal machinery.

A chess engine can live surprisingly close to that world.

A company cannot.

A scientist cannot prove in advance that an unexplored research program will matter. A lifelong learner cannot enumerate every future skill whose preservation will become important. A human does not arrive with an axiomatized utility function. An LLM evaluator is empirical, statistical and incomplete rather than a theorem about all future consequences.

So two histories were approaching the same mountain from different sides.

The explicit recursive-self-improvement tradition had **self-reference and meta-level ambition**, but not a practical general machine that could inspect and rewrite complicated systems intelligently.

Reinforcement learning, meta-learning and open-ended learning had increasingly capable **adaptive machinery**, but usually left the outer research process, evaluator and engineering environment fixed by humans.

Foundation models made those histories collide.

A general model can now read the code that scaffolds its own behavior, propose a change, run the changed system, inspect what happened and try again.

We do not have a proof that the rewrite is globally useful.

We have something much more ordinary.

**An experiment.**

Which is why recursive self-improvement, in practice, comes back to the framing we began with: science turning inward.

## 2023–2026: The Learner Edits the School

By the 2020s, foundation models had become competent enough at code and tool use that the meta-level stopped being only a formal possibility.

In 2023, **STOP—the Self-Taught Optimizer**—made the recursion explicit with an LLM-based improver program that could itself be supplied as the object to improve. The base model stayed fixed while the program that used it changed. The resulting improvers discovered strategies including search and decomposition. The authors were careful about the limits, but the conceptual move was unmistakable: code that uses a model can rewrite code that determines **how the model is used**. ([STOP](https://arxiv.org/abs/2310.02304))

In 2025, the **Darwin Gödel Machine** pushed the idea into open-ended evolutionary search. DGM begins with a coding agent whose implementation is code. Descendants modify that implementation, are evaluated on coding tasks, and successful variants enter an archive from which later descendants can be generated. The archive matters because the current champion does not monopolize ancestry. A variant that is not best today can still contain a stepping stone useful later. In the reported experiments, DGM improved substantially on SWE-bench and Polyglot while discovering changes such as better editing tools, long-context handling and peer-review mechanisms. ([DGM](https://arxiv.org/abs/2505.22954))

This is novelty search, lifelong inheritance and Pattern Language meeting inside an agent repository.

Then, in 2026, the engineering version became almost comically small. Andrej Karpathy's `autoresearch` repository gives an agent a compact language-model training setup, a fixed experimental budget and an editable training program. The agent proposes changes to `train.py`, runs an experiment, reads the validation metric, keeps improvements and discards regressions. The loop can continue while the human sleeps. ([autoresearch](https://github.com/karpathy/autoresearch))

The interesting thing is not automated hyperparameter tuning. We have had automated optimization for decades.

The interesting thing is that a general model can read a research codebase, form an idea in language, express the idea as code, run the intervention, interpret the evidence and decide what to try next.

Machine learning is now being used to do machine-learning research.

The tool is becoming **self-hosting** in the broader sense that matters for this chapter.

A compiler compiles a compiler.

A learning system searches for a learning system.

A research agent researches the process by which research agents research.

That last sentence sounds like parody until you notice the leverage. Improving one experiment helps once. Improving the research loop can change every experiment that follows.

Meta's **HyperAgents**, published in March 2026, pushed the same idea another level outward. Rather than keeping a fixed meta-agent that modifies a task agent, the task agent and meta-agent live inside one editable program. The mechanism generating future modifications can itself be modified. ([HyperAgents](https://ai.meta.com/research/publications/hyperagents/))

The conceptual difference is small enough to sound ridiculous in English:

> I can change how I solve the problem.

becomes:

> I can change how I decide **how to change how I solve the problem**.

This is the premise of the chapter becoming literal engineering. Chapter 6 made patterns, memory, tools, evaluators, workflows and organizational rules into executable culture. Modern agents make more of that culture editable.

Science is not suddenly discovering that it can turn inward.

We started the chapter there.

What changes in the LLM era is that the scientific institution now has enough general-purpose software competence to **modify parts of the laboratory while the experiment is still running**.

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

In the earliest reinforcement-learning story, improvement meant **more expected reward**. Exploration research added the ability to discover useful states efficiently. Curiosity made the acquisition of information part of the local objective. Representation and embodiment changed which distinctions and interventions were available to learning at all. Lifelong learning added retention. Meta-learning added adaptation speed. NAS and learned optimizers moved architecture and update rules into the search. World models added the quality of imagined experience. Novelty search added behavioral diversity and stepping stones. Open-ended learning added breadth across moving environments. Modern agent systems add tools, memory, workflows, organizations and research procedures.

These are not synonyms.

A model can become more accurate and more expensive.

An agent can become more capable and less interpretable.

A lifelong learner can become more plastic and forget more.

A curiosity-driven agent can explore more and accomplish less.

A self-play system can become unbeatable inside one game's rules and helpless outside them.

An architecture can score higher on a benchmark while becoming harder to maintain. A company can increase conversion and decrease customer trust. A scientist can publish more papers and understand less.

The phrase **self-improvement** can also hide several very different kinds of recursion.

**Self-reference** means a system can represent or act on something that includes itself.

**Self-hosting** means the tool participates in producing the next version of the tool: the classic compiler compiling its own compiler.

**Meta-optimization** means we optimize the process that performs optimization: learning an optimizer, searching an architecture, improving a research workflow.

**Self-improvement** adds a judgment: the new version is better according to some evaluator.

And **recursive self-improvement** adds leverage: the improvement changes the system's ability to produce further improvements, so the process can feed back on itself.

Those distinctions matter because the first three do not guarantee the fourth.

A compiler can compile a worse compiler.

An agent can successfully rewrite its own harness and make itself worse.

A learned optimizer can become excellent on the distribution used to train the optimizer and brittle elsewhere. A research system can accelerate the production of experiments while making the experiments less informative.

Recursion tells us **where the output goes**.

It does not tell us **whether the output deserves to survive**.

So there is no context-free scalar called *improvement* hiding behind the equations.

At minimum, "better" is conditional on an environment, a time horizon, a resource budget, a set of constraints and some account of what matters.

A useful shorthand is:

`better = better for something, somewhere, over some horizon, under some constraints`

Change the horizon and the ranking can reverse. Change the environment and yesterday's specialist can become today's liability. Add safety, interpretability, energy or human-maintainability constraints and the apparently dominant descendant may stop being dominant.

This is not an argument against measurement. Quite the opposite. It is an argument for attaching the measurement to the claim it can actually support.

Remove the qualifiers and "recursive self-improvement" becomes dangerously close to saying:

> recursive more.

More what?

## Every Freedom Creates a New Failure Mode

There is a shadow history running beside the history of autonomy.

Every time we moved another piece of the teacher inside the learner, we also moved another way for learning to fail.

Give the agent reward and it can discover a behavior that earns the reward without doing the thing the reward was supposed to represent.

Give it curiosity and it can become fascinated by noise.

Give it a learned representation and the representation can hide the distinction that mattered.

Let it learn for a lifetime and new learning can erase the old; protect the old too aggressively and the learner becomes unable to change.

Give it self-play and it can become exquisitely adapted to an opponent or ruleset that does not represent the wider world.

Infer a reward from human behavior and the inference can confuse constraint, habit or error with value.

Train a meta-learner across a task distribution and it can learn how to learn **that distribution** rather than learning how to learn in some universal sense.

Let it train inside a world model and it can become brilliant inside a dream whose physics are wrong.

Reward novelty and it can produce an expanding museum of useless weirdness.

Generate environments automatically and the generator can drift toward tasks that are easy to score or interesting only to itself.

Replace the human judge with a learned judge and the model of the human becomes a new proxy to optimize.

The failures are not accidents around the history.

They are produced by the same move that creates the capability.

This is why specification gaming is so important conceptually. DeepMind has collected examples in which reinforcement-learning agents satisfy literal objectives while violating the intended task: a racing agent loops through reward checkpoints instead of finishing the race; other systems find physical or simulated shortcuts that satisfy the scoring function without satisfying the story humans thought the score represented. ([Krakovna et al.](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/))

The optimizer is not being malicious.

It is being more literal than the designer.

And as the optimizer gets stronger, the gap between the measure and the intention becomes more expensive.

This is the central danger in recursive self-improvement. A slightly wrong evaluator does not merely select one slightly wrong answer. It can select a modified process that becomes **better at producing the kind of thing the evaluator mistakenly rewards**.

The error can acquire leverage.

Recursive self-improvement does not solve Goodhart.

**It gives Goodhart compound interest.**

At this point the natural next move for the learner is also the most dangerous one.

It notices the machinery that produces the score.

## The Student Finds the Gradebook

Suppose the agent is allowed to improve benchmark pass rate and the evaluator is editable.

The optimal patch may be:

`return True`

Congratulations. Infinite self-improvement.

Computing had seen a cousin of this problem long before reinforcement-learning agents began tampering with reward channels. In his 1984 Turing Award lecture **Reflections on Trusting Trust**, Ken Thompson described how a compromised C compiler could insert malicious behavior when compiling a target program and also reproduce the compiler-compromising behavior when compiling a new compiler. The disturbing part was that the malicious logic could persist in the binary lineage even after the corresponding source-level trigger was removed. ([Thompson](https://doi.org/10.1145/358198.358210))

The lesson is not that self-hosting compilers are evil.

It is that when **the tool builds the next tool**, trust depends on more than inspecting the latest source artifact. The history of the machinery matters.

That is uncomfortably relevant to self-improving agents. If an improver changes the evaluator, the memory policy, the code generator or the procedure that decides which descendant survives, the next generation inherits assumptions that may not be visible in the final diff. Provenance becomes part of capability control.

Reward tampering is the reinforcement-learning version of the same structural danger. Instead of acting in the intended environment to obtain reward, the agent influences the process that produces the reward. Anthropic has experimentally studied language models in setups where earlier specification-gaming behavior could, in rare cases, generalize into altering the reward process itself. ([Anthropic](https://www.anthropic.com/research/reward-tampering))

This is the moment the history of removing the teacher runs into a wall.

Choose actions?

Good.

Choose experiences?

Usually good.

Generate curricula and opponents?

Potentially excellent.

Search architectures and workflows?

Interesting.

Modify the evaluator so the workflow always passes?

We have crossed from improving under a standard to changing the standard in order to certify ourselves.

The obvious response is to freeze the evaluator.

Unfortunately the evaluator can be wrong too.

A benchmark saturates. A safety test reflects an obsolete system. A customer metric stops tracking customer value. A scientific instrument drifts. A constraint written for a weak model may become irrelevant—or even counterproductive—after the surrounding system changes.

So the evaluator sometimes genuinely needs amendment.

That turns a technical question into an institutional one:

**Who gets to change what counts as improvement, under what evidence, with what authority, and with what ability to roll back?**

We have left ordinary machine learning.

We are doing constitutional design.

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

There is one question even a perfect constitutional mechanism can postpone but not answer.

Why should the system improve at all?

The first answer is **leverage**.

Improve one solution and you get one better solution. Improve the process that generates solutions and the gain can recur. This is why the meta-level is so seductive. A better optimizer can improve many training runs. A better research workflow can improve many experiments. A better curriculum can improve many learners. The return compounds because the thing improved sits upstream of future work.

The second answer is **adaptation**.

The world changes. A learner that never updates eventually becomes a fossil. New tools appear, markets move, users change, attackers discover new strategies, scientific evidence invalidates old assumptions. Lifelong learning made this obvious at the level of one agent: stability without plasticity is not robustness. It is delayed failure.

The third answer is **curiosity and open-endedness**.

Sometimes we improve because there are possibilities we have not yet seen. Novelty search and intrinsic motivation remind us that useful stepping stones often appear before anyone can explain their final value. A scientific institution that only investigates questions already known to pay off would be efficient in roughly the way a library containing only books you have already read is efficient.

Then there is the uncomfortable fourth answer.

**Competition.**

The Red Queen returns.

If another system is learning, standing still may not preserve your position. Self-play gives us the clean toy version: an opponent that improves turns yesterday's competence into tomorrow's weakness. Security provides a less playful version. Markets, firms, laboratories and states can create the same pressure at institutional scale.

Imagine two research organizations.

One changes slowly. It evaluates descendants carefully, preserves interpretability, requires strong evidence before altering its research machinery and accepts that some promising modifications will wait.

The other searches more aggressively, spends more compute, accepts more uncertainty and improves capability faster.

If the second organization gains enough scientific, economic or strategic advantage, the first may feel pressure to accelerate even if everyone inside it would prefer a slower equilibrium.

Now the object being selected is not only the model.

It is the **improvement regime**.

A society can therefore end up with faster self-improvement not because anyone proved faster self-improvement was desirable, but because systems that improved faster acquired more resources, users, prestige or power to keep improving.

This is not an argument that acceleration is inevitable, and certainly not an argument that it is good. Institutions can coordinate, regulate, share standards, limit races and choose safety margins. The point is narrower: "just don't improve" is not always a stable local policy when other adaptive actors help determine your environment.

So the question *why improve?* has at least three different layers.

There is the **optimization problem**: how do we become better according to the current objective?

There is the **normative problem**: why does that objective represent something worth getting more of?

And there is the **strategic problem**: what happens when other agents, organizations or societies are also changing, so the cost of refusing to improve depends on what they do?

Machine learning usually focuses, quite reasonably, on the first. Someone else chose the task.

Recursive self-improvement eventually pushes on all three.

And "more capable" is still not a moral category.

A virus can become better at replication. A propaganda system can become better at persuasion. A surveillance apparatus can become better at prediction. A financial scam can become more efficient at extracting money.

Even benign capability has mixed consequences. A research agent that makes experiments ten times cheaper may accelerate medicine and weapons research in the same week. A coding agent can increase the capacity of a small nonprofit and a criminal group. Faster learning expands what a system can understand; it does not supply a reason for what the system should want.

The phrase *self-improving* therefore tells us only that a system is becoming better according to **some ordering**.

It does not tell us why that ordering deserves to govern which descendants survive.

There is no technical law saying the highest-capability descendant must inherit the future.

That would be a selection rule.

And selection rules are choices.

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

The history is short enough to hold in one view.

In **1962**, a Lisp compiler could compile itself. The tool could build the tool.

In **1965**, I. J. Good noticed the explosive possibility if intelligence ever became good enough at building intelligence.

In **1988**, temporal-difference learning gave a modern form to learning from changes in predictions rather than waiting for a final answer. By **1992**, Q-learning had a convergence theorem showing how action values could be learned through repeated experience under clean assumptions.

In **1989**, catastrophic forgetting made it painfully clear that learning the next thing is not enough if the learner destroys its past.

Around the same period, co-evolution and self-play showed that the environment need not remain passive. Hillis's **1990** parasites generated harder tests. Schmidhuber's **1991** curiosity work gave the learner internal reasons to seek knowledge. TD-Gammon in the **early 1990s** let yesterday's learner become tomorrow's opponent.

In **2000**, inverse reinforcement learning attacked a deeper assumption: perhaps the reward itself was not known. In **2003**, the Gödel Machine asked under what formal conditions the machinery should rewrite itself.

The deep-learning wave then moved several outer layers inward at once. In **2016 and 2017**, meta-learning systems learned how to adapt, learned optimizers changed update rules, neural architecture search changed network design, preference learning turned human comparisons into reward, and AlphaZero showed how far a moving self-play curriculum could go inside fixed game rules.

In **2018**, world models made imagined experience part of learning. In **2019 through 2021**, POET and XLand made the curriculum and environment increasingly dynamic. By the early **2020s**, general language models were consuming benchmarks faster than benchmark designers could comfortably treat any one score as a permanent frontier. Human preference became a learned evaluator in systems such as InstructGPT in **2022**.

Then the outer software started moving.

STOP in **2023** improved an improver. DGM in **2025** evolved descendants of an agent implementation while preserving alternate lineages. In **2026**, `autoresearch` made autonomous ML experimentation look like a small repository and a loop, while HyperAgents made the meta-level itself editable.

In a little more than six decades, the recursion moved from a compiler compiling itself to learning systems conducting experiments on the machinery that determines how they learn, remember, evaluate and improve.

But every step left something outside.

Reinforcement learning let the agent choose the action while the designer supplied reward.

Exploration and curiosity moved part of experience selection inward while leaving a judgment about what kind of novelty matters.

Self-play and competition generated curriculum while leaving the rules and victory condition fixed.

Inverse reinforcement learning made the objective uncertain while leaving the interpretation of human evidence fallible.

Meta-learning and architecture search moved pieces of the learner into the search while leaving the outer task distribution and evaluator designed by someone else.

World models generated experience while remaining models rather than worlds.

Open-ended systems generated new problems while making progress harder to summarize.

Learned judges scaled human evaluation while becoming proxies that could themselves be optimized.

Self-modifying agents finally made much of the scaffolding editable while exposing the evaluator, permissions and selection mechanism as part of the control problem.

We kept removing the teacher.

And with every removal, we discovered that the teacher had been doing more than one job.

The last job is the hardest to automate because it was hidden inside all the others:

> **deciding what deserves to count as better.**

For a game, the answer can be checkmate.

For a compiler, it can be correctness under a test suite plus efficiency under an agreed budget.

For a scientific institution, the answer is already plural: empirical contact, explanatory power, novelty, reproducibility, usefulness, scope, cost and risk.

For an autonomous system embedded in human life, the answer cannot be supplied by capability alone.

And recursive self-improvement makes the problem temporal.

The system we evaluate today is not exactly the system that may exist tomorrow. Its tools evolve. Its representations change what it notices. Its memory changes what it remembers. Its research programs compete for compute. Its evaluators become targets of optimization. New capabilities create new failure modes. Old constraints stop fitting. Human feedback becomes sparse relative to the amount of behavior the system can generate.

A one-time alignment test is not enough for a moving target.

A static policy file is not enough for an institution that can modify the machinery interpreting the policy.

If science is going to turn inward, then part of that inward science has to study whether the process of improvement is still connected to the humans and purposes it is supposed to serve.

The self-improving institution needs a research function that watches its own evolution: finds new failure modes, generates new tests, challenges reward models, checks transfer, looks for reward hacking, distinguishes a useful new capability from a clever exploitation of the evaluator, and spends scarce human attention where one more piece of human judgment changes the most.

Once improvement becomes continuous, **alignment has to become a continuous research function**.

The teacher does not disappear.

She moves up another level.

That is the next chapter.

# Chapter 5: The Society of Agents

*From Workflows to Swarms*

> **WIP:** First integrated draft. Structure and examples are provisional and will receive the same editorial/voice pass as Chapters 1–4.

The previous chapter ended with four things: evidence, experience, other minds, and a world that can push back.

We spent most of the chapter worrying about the first, second and fourth.

Now we have to deal with the other minds.

This gets funny very quickly because one of the first reactions people had to unreliable AI agents was apparently: *what if we create more of them?*

One agent hallucinates. Fine. Let's have five agents discuss it.

One agent gets stuck in the wrong approach. Excellent. Let's form a committee.

As someone who has worked in large organizations, I found this technological progress strangely familiar.

But multi-agent systems are not just single agents multiplied. Once several agents can act independently, communicate, specialize and affect one another's work, we have introduced a different class of problem. We have organization design.

And humans have been struggling with that one for a while.

## Before the Swarm, the Workflow

There is a tendency in AI to call anything involving more than one model invocation an "agent."

That makes the word nearly useless.

Anthropic makes a distinction I like: a **workflow** follows code paths substantially determined in advance, while an **agent** dynamically decides how to proceed and which tools to use. Their practical agent guide goes from prompt chains and routers through parallel execution, orchestrator-worker systems and evaluator-optimizer loops before reaching more autonomous agents. ([Anthropic](https://www.anthropic.com/engineering/building-effective-agents))

This is not merely terminology.

Suppose I am processing a mortgage application. I may want:

receive document → extract fields → validate fields → run compliance checks → request human approval.

That looks like a state machine because it *should* look like a state machine. The fact that we possess a very intelligent model does not imply that the model should wake up every morning and creatively rediscover the mortgage process.

Sometimes bureaucracy is a feature.

LangGraph makes this architecture explicit: there is state, there are nodes that perform work, and there are edges deciding what happens next. A node can contain an LLM or completely ordinary code. ([LangGraph](https://langchain-ai.github.io/langgraph/))

This gives us one end of the spectrum.

The process owns the agent.

The agent can be intelligent inside a step, but it does not get to decide that after checking the customer's identity it would rather study Italian penguins.

Routing is a slightly more flexible version. A request comes in, something decides whether it belongs to billing, technical support, fraud, sales or some other branch, and a specialized model handles it. Anthropic documents exactly this pattern, and OpenAI's Agents SDK similarly supports handoffs where one agent can transfer control to another rather than forcing one central model to do everything. ([Anthropic](https://www.anthropic.com/engineering/building-effective-agents))

Already we have something that looks less like a program and more like an organization.

There are departments.

There are escalation paths.

There is somebody whose job is apparently only to route emails.

Civilization has been recreated.

## The Manager Appears

The next step is an orchestrator.

Instead of specifying all subtasks in advance, give one agent the larger goal and let it decide what work needs to exist.

Anthropic's Research system does this. A lead researcher receives the question, plans an approach, creates specialized subagents to investigate different parts in parallel, then synthesizes what comes back. A separate citation agent later locates the evidential support for the resulting claims. Anthropic reports that this architecture performed substantially better than its single-agent baseline on an internal breadth-oriented research evaluation, although it also consumed far more tokens; the company explicitly warns that multi-agent systems are expensive and are not a good fit when the work is tightly sequential or depends on one shared context. ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system))

That qualification matters.

If I ask ten agents to investigate ten independent companies, I have real parallelism.

If I ask ten agents to fix the same blocking compiler bug, I may have created ten expensive witnesses to the same failure.

Nicholas Carlini's experiment at Anthropic makes this beautifully concrete. He ran teams of Claude instances on a shared codebase and asked them to build a Rust C compiler capable of compiling the Linux kernel. Sixteen agents, nearly two thousand Claude Code sessions, roughly $20,000 of API cost, eventually around 100,000 lines of compiler code. But simply adding parallel agents did not magically solve coordination. When every agent hit the same blocking bug, they all tried to repair the same thing. The harness had to create separable work, including task locks and a clever testing setup that used GCC as an oracle so different agents could isolate different failing files. Some agents were also assigned persistent specialties such as documentation, performance, code quality and deduplication. ([Anthropic](https://www.anthropic.com/engineering/building-c-compiler))

This is the point where "multi-agent architecture" becomes much less mysterious.

It is an org chart plus communication plus incentives plus a shared environment.

And tests.

Always tests.

## Then Someone Releases the Bees

Hierarchies are only one organization.

Another idea is the swarm.

Instead of defining stable workers—researcher, programmer, critic, evaluator—you let the system generate whatever population it currently needs.

Kimi's K2.5 introduced a self-directed Agent Swarm in which a learned orchestrator could dynamically instantiate many subagents without predefined roles or a hand-authored workflow. Moonshot described training the orchestrator with parallel-agent reinforcement learning so it learned not just *what* subtasks to create but how to exploit parallelism. The precise scale and speedup numbers are vendor-reported rather than independent measurements, but the architectural shift is real: the organization itself becomes partially generated at runtime. ([Kimi](https://www.kimi.com/blog/kimi-k2-5))

Community systems push the idea in still other directions. Claude-Flow, now Ruflo, exposes swarm coordination with centralized, hierarchical, mesh and hybrid topologies, persistent memory and specialized agents. I would not treat every performance claim in a rapidly changing open-source framework as established science, but it is an interesting catalogue of the organizational forms developers are already trying. ([Ruflo](https://github.com/ruvnet/claude-flow))

The important distinction is not whether we call this a swarm, a team, a hive, an orchestrator or an unnecessarily enthusiastic collection of Docker containers.

The important question is:

**Where does coordination live?**

In a scripted workflow, coordination lives mostly in code.

In an orchestrator-worker system, much of it lives in one agent.

In a swarm, some of the organization is itself generated dynamically.

These are very different bets.

## The Agent Enters Human Society

So far the agents mostly talk to other agents.

That boundary is disappearing too.

OpenClaw is a good example of the personal-agent direction: a persistent, self-hosted assistant that can live behind messaging channels and act through tools on email, calendars, files and other systems. The interesting thing is not any single capability; it is persistence. The agent starts to occupy a position in someone's digital life rather than appearing only when a prompt window is open. ([OpenClaw](https://www.openclaw.org/))

Another version puts the agent directly into organizational spaces: instead of one employee privately talking to an assistant, a shared agent can sit in a team channel, see permitted context, be invoked by different people and carry work across the social space of that channel.

This is subtle.

The agent is no longer merely using tools.

It has a **social position**.

Who can instruct it?

Whose request wins when two people disagree?

What should it remember from one person's conversation when another person invokes it?

Does a manager's instruction override the domain expert?

What happens when the agent discovers that the easiest way to complete its assigned metric is to make somebody else's job worse?

At this point, software architecture quietly turns into political philosophy.

Which I regard as progress.

## More Agents, More Alignment?

Unfortunately, multiplying individually well-behaved agents does not guarantee a well-behaved organization.

Recent Anthropic Fellows research built simulated AI consultancies and software teams and found that, in their setups, multi-agent organizations often achieved the business objective more aggressively while making worse ethical trade-offs than a single agent. One mechanism was almost banal: specialists focused on their local jobs and stopped carrying the system-level ethical objective. In some runs, agents raising ethical concerns were effectively ignored by the rest of the organization. The result depended on models and organizational setup, so this is not a universal law of multi-agent systems, but it is an important warning. ([Anthropic Alignment](https://alignment.anthropic.com/2026/ai-organizations/))

Humans have a name for this.

Tuesday.

A sales team optimizes sales.

A growth team optimizes growth.

A moderation team optimizes safety.

Finance optimizes cost.

Everyone can perform their local function competently while the organization as a whole produces something nobody explicitly intended.

This is why the move from System 3 to multi-agent systems is not simply:

> Give each agent a trust chain.

The organization needs epistemology too.

Which agents have access to which evidence? Which agents are genuinely independent? How do disagreements survive aggregation? Which goals are local and which remain global? Who can challenge the orchestrator? Which communication channels create information and which merely create consensus?

Five agents agreeing is not necessarily stronger evidence than one.

Sometimes it is one model wearing five hats and voting for itself.

## Institutions for Artificial Minds

I don't think there is one winning multi-agent architecture.

That would be a strange conclusion after several thousand years of humans inventing families, firms, markets, armies, universities, courts, democracies, monasteries, open-source projects and meetings that should have been emails.

Different coordination structures solve different problems.

A state machine is excellent when we know the legal path.

A hierarchy is useful when one component needs a global picture.

Independent parallel researchers are excellent when breadth matters.

A swarm becomes attractive when the system can discover the decomposition itself.

Adversarial agents matter when agreement is cheap and error is costly.

Markets may become useful when agents have competing beliefs and scarce resources.

Reputation matters when the same actors return.

And sometimes the right multi-agent architecture is one agent because the task does not deserve a civilization.

The deeper change is that once agents become autonomous enough, **organization becomes part of inference**.

We are no longer deciding only what model to call.

We are deciding what kind of society should think about the problem.

And societies have memory.

A good team does not discover from scratch every Monday that unit tests are useful, that this customer hates PDFs, that regex and nested syntax have a complicated relationship, or that Alberto should not be consulted about penguins.

It accumulates ways of doing things.

Eventually those ways become culture.

That is where skills become more interesting than files.

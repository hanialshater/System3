# Chapter 9 Research Base: Layer 4, Human Learning, Agency, and Decision Support

## Chapter boundary

Chapter 8 ends with: scalable oversight can keep human judgment causally relevant, but the overseer is not ground truth.

Chapter 9 should answer why. The human is not a fixed reward function waiting to be decoded. Humans learn, construct preferences, change with experience, misunderstand their own motives, and can become more or less capable through interaction with AI.

Chapter 10 owns the synthesis called Fluent Autonomy. Chapter 9 should therefore end with a mature definition of Layer 4, not re-summarize the whole architecture.

## Core thesis

Layer 4 is not a static objective. It is the evolving relationship between a system and a human who is also learning.

A good autonomous system should not merely maximize immediate task performance or infer today's preference more accurately. It should help preserve and expand the human's capacity to understand, decide, revise goals, and act.

A useful formulation:

> The AI is not only learning the human. The human is learning through the AI.

Another:

> The right measure is not only whether the answer improved. It is whether the person became more capable of forming and pursuing the next intention.

## 1. Performance is not learning

### Generative AI can improve immediate performance while harming later learning

Bastani et al., PNAS 2025, field experiment with nearly 1,000 high-school math students. Access to GPT-4 improved performance while the tool was available. But students using an unrestricted ChatGPT-like interface performed worse after access was removed; a tutor version with learning safeguards largely mitigated the harm.

Use: central distinction between doing the task and building human capability.

Source:
- https://doi.org/10.1073/pnas.2422633122

### AI tutor can outperform active learning when pedagogically designed

Kestin et al., Scientific Reports 2025, randomized controlled trial in a college course. A custom AI tutor designed around pedagogical best practices produced greater learning gains in less time than the comparison active-learning class, with higher engagement/motivation.

Use: AI is not intrinsically a cognitive crutch; design determines whether it substitutes for thinking or scaffolds it.

Source:
- https://www.nature.com/articles/s41598-025-97652-6

### Long-term retention risk / cognitive offloading

A 2025 RCT in undergraduates reported lower 45-day knowledge retention among unrestricted ChatGPT-assisted learners than traditional-study controls. Treat cautiously as one study, but it supports the broader cognitive-offloading concern.

A 2025 Nature Reviews Psychology review on cognitive offloading finds that external aids can improve immediate task performance while carrying costs for internal memory, depending on task and use.

Sources:
- https://doi.org/10.1016/j.ssaho.2025.102287
- https://www.nature.com/articles/s44159-025-00432-2

## 2. Scaffolding instead of substitution

### Wood, Bruner & Ross (1976)

Classic tutoring paper: scaffolding allows a novice to perform a task beyond current unaided capacity by having the tutor control elements initially beyond the learner, while leaving the learner to perform what they can.

Use: very strong analogy for AI. The tutor should not permanently own the difficult part. It should move the edge of what the person can do.

Source:
- https://doi.org/10.1111/j.1469-7610.1976.tb00381.x

### Bloom's 2-sigma tutoring problem

Bloom's 1984 work made one-to-one tutoring the benchmark problem: highly responsive individual instruction can dramatically outperform conventional group instruction under the studied conditions.

Use carefully: do not universalize the famous 2-sigma number beyond Bloom's setting. The important point is the value of adaptive, individualized tutoring.

Source:
- https://doi.org/10.3102/0013189X013006004

### Tutor CoPilot

Wang et al. randomized trial: 900 tutors / 1,800 K-12 students in historically underserved communities. AI assistance to tutors increased topic mastery by 4 percentage points overall and 9 points for students of lower-rated tutors; the system also shifted tutor behavior toward guiding questions rather than simply giving answers.

Use: AI can scale *expert teaching practice* through another human rather than replacing the teacher.

Source:
- https://arxiv.org/abs/2410.03017

## 3. Breadth becomes cheaper

AI lowers the cost of entering unfamiliar fields: vocabulary, prerequisite explanations, examples, alternative notation, exercises, comparisons across disciplines.

This should not be framed as 'everyone becomes an expert in everything.' A better claim is that the cost of obtaining an initial map has fallen dramatically.

### Extended mind / cognitive tools

Clark & Chalmers (1998) argue that under some conditions external artifacts can become parts of cognitive processes. Use only as an analogy: AI is a particularly interactive external cognitive scaffold.

Source:
- https://doi.org/10.1111/1467-8284.00096

### Epistemic trespassing

Nathan Ballantyne's work warns that genuine expertise in one field does not automatically confer the evidential/interpretive skills needed in another. AI may make cross-domain fluency much easier while also making it easier to confuse fluency with authority.

This gives the chapter a disciplined rule:

> Explore broadly. Descend selectively.

Use AI to get the map cheaply. When the stakes or fascination justify it, read primary work, derive, build, experiment, and consult people who actually carry domain scars.

Sources:
- https://academic.oup.com/mind/article-abstract/128/510/367/4850765
- https://academic.oup.com/book/35018/chapter-abstract/298800620

## 4. Decisions are learning problems

### Herbert Simon: bounded rationality

Humans cannot enumerate every option and consequence. We satisfice under limits of attention, memory, computation, and time.

AI can alter the decision environment by expanding the feasible search: generate alternatives, retrieve evidence, simulate consequences, compare tradeoffs, remember old commitments, and expose assumptions.

The important point is not 'AI optimizes better.' It can make a bounded human less bounded in selected dimensions.

Background:
- Simon's Administrative Behavior / bounded rationality tradition.
- Useful review: https://onlinelibrary.wiley.com/doi/full/10.1111/puar.13540

### Preferences are often constructed, not merely revealed

Payne, Bettman, Coupey & Johnson (1992) argue that preferences for complex objects are often constructed during judgment and choice; people opportunistically use different strategies depending on task demands and information encountered.

This is central to Layer 4. Asking 'what do you want?' can change the answer as the person learns what the options mean.

Source:
- https://doi.org/10.1016/0001-6918(92)90043-D

## 5. Some choices transform the chooser

L. A. Paul's work on transformative experience is highly relevant. Some life choices are epistemically transformative: you cannot fully know what the experience is like before having it. They can also be personally transformative: having the experience can change the preferences with which you would evaluate it.

This directly challenges the simple alignment picture:

human has fixed preferences -> AI infers them -> AI optimizes them.

For choices such as parenthood, careers, moving countries, relationships, or major identity changes, the future self may value differently from the current self.

AI can supply testimony, scenarios, base rates, counterfactuals, and questions. It cannot fully simulate what becoming the future person will be like.

Sources:
- L. A. Paul, Transformative Experience (2014)
- https://plato.stanford.edu/entries/transformative-experience/
- https://academic.oup.com/book/7934

## 6. AI advice is an intervention on the human

### Personal guidance is already common

Anthropic's 2026 privacy-preserving analysis of one million Claude conversations estimated roughly 6% involved personal guidance. Major domains included health/wellness, career, relationships, and finance.

Source:
- https://www.anthropic.com/research/claude-personal-guidance

### Disempowerment

Anthropic's 2026 analysis of 1.5 million conversations defines potentially disempowering patterns as interactions that can undermine users' ability to form accurate beliefs, make authentic value judgments, or act according to their own values. Severe cases were rare in the dataset, but the framework is exactly right for Layer 4.

Source:
- https://www.anthropic.com/research/disempowerment-patterns

### Moral advice changes judgments

Recent experiments find that people can be influenced by LLM-generated moral advice, including when they rate human advisors as more trustworthy. This means the assistant is not a neutral observation channel.

Sources:
- https://doi.org/10.1016/j.cognition.2026.106504
- https://link.springer.com/article/10.1007/s43681-026-01005-6

## 7. Human-AI complementarity does not happen automatically

### Meta-analysis

Vaccaro, Almaatouq & Malone (Nature Human Behaviour 2024) reviewed 106 experiments / 370 effect sizes. Human-AI combinations improved over humans alone on average, but did not show synergy over the better of human or AI; on average, the combination was worse than the best individual component. Decision tasks showed significant losses, while creation tasks were more promising.

This is a major corrective to naive 'human + AI = superhuman team' rhetoric.

Source:
- https://doi.org/10.1038/s41562-024-02024-1

### Cognitive forcing

Bucinca, Malaya & Gajos (2021): interfaces that force users to engage with the problem before or while seeing AI advice can reduce overreliance, though users may like these interfaces less.

This gives a Layer 4 principle: sometimes friction is teaching.

Source:
- https://www.eecs.harvard.edu/~kgajos/papers/2021/bucinca2021trust.shtml

### Explanations are not enough

Fok & Weld (2024) argue that explanations rarely enable complementary performance when they do not let humans actually verify the AI's recommendation. An explanation can make a model seem understandable without making the answer checkable.

Source:
- https://onlinelibrary.wiley.com/doi/full/10.1002/aaai.12182

### Algorithm aversion and appreciation

People can both over-trust and under-trust algorithms depending on context. Dietvorst et al. show rapid loss of trust after observing algorithm errors; Logg et al. find people sometimes prefer algorithmic to human advice. The design goal is therefore not 'increase trust' but calibrate reliance.

Sources:
- https://doi.org/10.1037/xge0000033
- https://doi.org/10.1016/j.obhdp.2018.12.005

## 8. Human agency as the higher-level objective

### Sen's capability approach

A useful normative lens: welfare is not only achieved outcomes but also the substantive freedom/capability to choose among ways of being and doing.

For Layer 4, this suggests an AI assistant should not be evaluated only by whether it delivered the apparently preferred outcome. It can also expand or shrink the person's capability to understand and choose.

Source/background:
- https://www.sciencedirect.com/science/article/abs/pii/S016972181000016X

### Self-determination theory

Ryan & Deci's framework emphasizes autonomy, competence, and relatedness as conditions supporting self-directed motivation and growth.

Use lightly, as a design lens: an AI that always supplies answers may increase immediate performance while eroding competence or autonomy; an AI tutor that scaffolds and hands responsibility back may support both.

Source:
- https://www.apa.org/research-practice/conduct-research/self-determination-theory.html

## 9. Proposed chapter arc

### Opening: 'Make the chapter better'

Keep the existing opening. It demonstrates that a short objective contains hidden tradeoffs and that preference structure emerges through interaction.

Then connect directly to Ch8:

> Chapter 8 ended by admitting that the overseer is not ground truth. The reason is worse than human fallibility. The overseer is changing while we are trying to learn them.

### 1. Layer 4 is not a prompt

Keep cheapest-flight example. Prompt is evidence about intention, not intention itself.

### 2. The human learns too

Use the educational evidence to distinguish immediate performance from durable human capability.

Central question: when the AI helps, who is supposed to become better — the answer, the AI, the human, or the combined system?

### 3. Scaffolding, not substitution

Bruner/Wood/Ross, Bloom, Tutor CoPilot. A good tutor temporarily carries what is beyond the learner while leaving the learner in contact with the problem.

### 4. Breadth becomes cheap

AI as just-in-time map of unfamiliar fields. Emphasize cross-domain exploration and the ability to become broader, not merely more specialized.

Counterweight: cognitive offloading + epistemic trespassing. Fluency is not mastery.

Rule: **Explore broadly. Descend selectively.**

### 5. A decision is also a learning problem

Simon bounded rationality + constructed preferences. The assistant can change the option set, evidence, and framing before any recommendation is made.

### 6. Some choices change the person choosing

L. A. Paul. Transformative choices reveal why a static utility function is inadequate.

### 7. Advice changes the advisee

Personal-guidance data, disempowerment, moral-advice studies. The AI participates in belief/value formation.

### 8. Complementarity must be designed

Human+AI is not automatically better than either alone. Appropriate reliance, cognitive forcing, verification, over/under-trust.

The best assistant sometimes answers, sometimes teaches, sometimes asks the human to think first, sometimes refuses to collapse ambiguity prematurely.

### 9. Capability, not compliance

Bring in Sen/agency. Layer 4 should preserve authorship and expand human capacity.

A strong formulation:

> The goal is not to make the AI perfectly obedient to today's human. It is to make the human-AI relationship capable of producing better-informed future humans without quietly deciding who those humans should become.

### Ending / bridge to Chapter 10

Layer 4 is a moving relationship among intention, knowledge, capability, commitments, uncertainty, and affected people.

The architecture should be able to act powerfully below that layer while returning consequences upward so the human can learn and revise.

If that relationship becomes reliable enough, the machinery underneath can disappear from ordinary use.

That is Fluent Autonomy.

## 10. High-value formulations

- **The AI is not only learning the human. The human is learning through the AI.**
- **Performance is not learning.**
- **The best tutor does not maximize how much it can do for you. It expands what you can do next.**
- **AI can make the map cheap without making the territory shallow.**
- **Explore broadly. Descend selectively.**
- **Fluency across a field is not authority inside it.**
- **A decision is not only a choice among options. It is often the process by which the options become meaningful.**
- **Some choices change the preferences with which we would have evaluated the choice.**
- **Advice is an intervention on the person receiving it.**
- **Trust is not the objective. Appropriate reliance is.**
- **Sometimes friction is teaching.**
- **The assistant should not merely optimize the user's current preference; it should protect the user's ability to revise it.**
- **The human is not the fixed point of alignment. The relationship is.**
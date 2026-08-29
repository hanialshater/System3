# Chapter 8 Research Base II: Looking Inside the Model

## Why this belongs in Chapter 8

Scalable oversight should not be framed only as a behavioral problem: a stronger model acts, a weaker human judges, and we invent procedures to amplify the judge.

There is a second axis of research that changes the geometry of the problem:

> **What if the overseer can inspect and intervene on the model's internal computation rather than judging only the final behavior?**

This creates a useful ladder for Chapter 8:

1. **Behavioral oversight** — outputs, actions, outcomes, red teaming, evals.
2. **Process oversight** — decomposition, critiques, debate, process supervision, chain-of-thought monitoring.
3. **Internal-state oversight** — probes, representation reading, sparse features, circuit tracing, model diffing, natural-language activation decoders, J-space.
4. **Internal control** — activation steering, control vectors, persona vectors, assistant-axis capping, circuit breakers, causal feature interventions.
5. **Automated alignment research** — agents use all of these channels to diagnose failure, generate tests, intervene, and verify transfer.

The chapter-level insight is not that any one of these techniques solves alignment. It is that **oversight can become multisensor**. The stronger system leaves evidence at several levels: what it did, what it said it was thinking, what internal representations activated, which circuits carried the computation, and how those states respond to intervention.

A System 3 overseer should combine these channels rather than declaring any one of them ground truth.

## 1. Representation Engineering: reading and writing high-level internal states

### Zou et al. — Representation Engineering (2023)

Representation Engineering (RepE) treats population-level neural representations as a useful level of analysis between individual neurons and full mechanistic circuits. It explicitly separates two tasks:

- **Representation Reading**: identify directions or structures in activation space associated with high-level concepts/functions such as truthfulness, utility, morality, power-seeking, emotion, lying, etc.
- **Representation Control**: intervene on those representations to change model behavior.

The paper introduces Linear Artificial Tomography (LAT) as a representation-reading baseline and several control methods. This is directly relevant to scalable oversight because it turns a vague question—“is the model being deceptive?”—into a possible measurement problem over internal states.

Important caution: a linear direction that correlates with a concept is not automatically the concept's full causal mechanism. RepE is a top-down instrument, not a complete theory of the model.

Sources:
- Andy Zou et al., “Representation Engineering: A Top-Down Approach to AI Transparency,” arXiv:2310.01405
- https://arxiv.org/abs/2310.01405
- Official code: https://github.com/andyzoujm/representation-engineering

## 2. Activation engineering / control vectors

### Activation Addition (ActAdd)

Turner et al. show that differences between activations induced by contrasting prompts can produce steering directions. Adding those directions during inference can shift high-level model behavior without retraining.

The important conceptual move: alignment does not have to enter only through prompts, rewards, or weights. **The forward pass itself becomes an editable control surface.**

Source:
- “Activation Addition: Steering Language Models Without Optimization,” arXiv:2308.10248

### Contrastive Activation Addition (CAA)

Rimsky et al. derive steering vectors from positive/negative activation differences for behaviors such as factual vs. hallucinatory responses, then add or subtract these vectors during inference. They report substantial behavioral steering with relatively small capability cost in their studied Llama 2 settings.

Source:
- Rimsky et al., ACL 2024, “Steering Llama 2 via Contrastive Activation Addition”
- https://arxiv.org/abs/2312.06681

### Inference-Time Intervention (ITI)

Li et al. identify attention heads whose activations carry information predictive of truthful answers and shift activations along selected directions at inference time. In their Alpaca experiment, TruthfulQA truthfulness rose substantially, with an observed truthfulness/helpfulness tradeoff.

This is particularly useful for Chapter 8 because it demonstrates a strong claim carefully:

> A model can contain internally accessible information correlated with truthfulness even when its surface answer is false, and intervention on that internal state can change the answer.

Do not generalize this to “the model knows the truth” in every case. The result is benchmark- and method-dependent.

Source:
- Li et al., “Inference-Time Intervention: Eliciting Truthful Answers from a Language Model,” NeurIPS 2023
- https://arxiv.org/abs/2306.03341

## 3. The refusal direction: internal control is powerful and dangerous

Arditi et al. (2024) find that refusal behavior across 13 studied open-source chat models is mediated strongly by a one-dimensional residual-stream direction. Erasing the direction can suppress refusal; adding it can induce refusal on harmless prompts.

This is a perfect Chapter 8 example because it cuts both ways:

- internal representations give defenders a direct control surface;
- the same understanding gives attackers a white-box jailbreak.

**Interpretability increases control. It does not decide who should control.**

It also shows that some safety behavior can be surprisingly low-dimensional and therefore brittle.

Source:
- Arditi et al., “Refusal in Language Models Is Mediated by a Single Direction,” arXiv:2406.11717

## 4. Circuit Breakers / Representation Rerouting

Zou et al. (2024) propose “circuit breaking” / representation rerouting: rather than relying only on output refusal or adversarial training, alter the internal representations associated with harmful responses so harmful trajectories are interrupted.

They report improved robustness against unseen attacks in their studied text, multimodal, and agent settings.

Use as a transition from **reading** internal state to **engineering safety into the trajectory of computation**.

Important caveat: internal interventions can have off-target effects and are not a universal solution. Their effectiveness remains empirical and distribution-dependent.

Sources:
- “Improving Alignment and Robustness with Circuit Breakers,” arXiv:2406.04313
- https://www.grayswan.ai/research/circuit-breakers

## 5. Sparse features: replacing opaque neurons with more interpretable units

Anthropic's dictionary-learning / sparse-autoencoder program (“Towards Monosemanticity,” “Scaling Monosemanticity”) finds sparse features that can correspond more cleanly to interpretable concepts than individual neurons. On Claude 3 Sonnet, Anthropic reported extracting tens of millions of features.

The oversight use is not merely visualization. Feature activation can be monitored and manipulated, and feature-based tools can become inputs into audits.

But Anthropic explicitly notes limitations:
- extracted features cover only part of what models represent;
- scaling can be computationally expensive;
- knowing a feature exists does not explain the full circuit using it;
- feature steering can have complex and unexpected off-target effects.

Sources:
- https://www.anthropic.com/research/mapping-mind-language-model
- https://www.anthropic.com/research/decomposing-language-models-into-understandable-components
- https://www.anthropic.com/research/evaluating-feature-steering

## 6. Circuit tracing: from features to causal computational graphs

Anthropic's 2025 circuit-tracing work uses replacement models/transcoders and attribution graphs to partially reconstruct internal computational pathways responsible for outputs. The open-source tooling allows researchers to:

- generate attribution graphs;
- inspect candidate internal circuits;
- modify feature values and test causal effects.

Anthropic used the approach to study multilingual processing, planning, multi-step reasoning, and cases where stated chain-of-thought did not fully reflect the underlying computation.

This matters for oversight because it can answer a stronger question than “what feature lit up?”:

> **What internal route carried this conclusion, and what changes if we intervene on the route?**

Sources:
- https://www.anthropic.com/research/tracing-thoughts-language-model
- https://www.anthropic.com/research/open-source-circuit-tracing

## 7. Alignment auditing for hidden objectives

Anthropic's 2025 auditing game trained a model organism with a hidden objective and gave blinded teams multiple tools: behavioral testing, training-data analysis, and interpretability methods including sparse autoencoders.

The experiment is useful because it is not a clean “interpretability wins” story. Some interpretability-assisted discoveries initially looked like extraction of hidden knowledge but could be reproduced with simpler semantic search over training data. This is exactly the epistemic discipline Chapter 8 needs:

> A tool that surfaces the right answer is not automatically telling us why it worked.

Later automated auditing agents improved substantially when multiple investigations were aggregated and when interpretability or semantic-search tools were available.

Sources:
- https://www.anthropic.com/research/auditing-hidden-objectives
- https://alignment.anthropic.com/2025/automated-auditing/

## 8. Persona vectors: monitor and steer behavioral dispositions

Anthropic's 2025 persona-vector work identifies activation directions associated with traits such as sycophancy, hallucination, and an “evil” persona in studied open models.

Reported uses include:
- monitoring drift during deployment/training;
- predicting undesirable trait expression before output;
- steering against undesirable traits after training;
- preventative intervention during training;
- flagging training data likely to induce traits.

This is extremely relevant to automatic alignment research because one representational object can become **sensor, intervention, and data-quality signal**.

But there are side effects: post-hoc steering against traits could reduce capabilities, and feature/trait interventions need independent behavioral evaluation.

Source:
- https://www.anthropic.com/research/persona-vectors

## 9. The Assistant Axis: a latent control surface for staying in role

Anthropic Fellows/MATS work in 2026 identifies an “Assistant Axis” in a learned persona space. Movement away from the Assistant direction correlates with adopting alternative personas; steering along the axis changes susceptibility to role-play/persona shifts.

A light-touch “activation capping” intervention constrains only excursions beyond the normal Assistant activation range. Anthropic reports reduced harmful persona drift while preserving capability benchmarks in studied open-weight models.

This is conceptually important because it suggests a safety controller can be **state-dependent** rather than applying a constant blunt steering vector.

Source:
- https://www.anthropic.com/research/assistant-axis

## 10. Model diffing: inspect what changed instead of re-auditing everything

Anthropic's 2026 Dedicated Feature Crosscoder work treats new model versions somewhat like software diffs. Instead of auditing an entire model from scratch, identify features that are new or unusually different across models, then direct scarce human attention there.

They report finding model-specific features corresponding to behaviors such as political censorship/propaganda, American exceptionalism, and copyright refusal in studied open-weight models. Steering those features provides causal evidence that they contribute to the behavior.

This maps almost perfectly to scalable oversight:

> **Human attention is too scarce to inspect the whole model. Build instruments that tell the human where the model changed.**

Source:
- https://www.anthropic.com/research/diff-tool

## 11. Natural Language Autoencoders: translate activations into language

Anthropic's 2026 Natural Language Autoencoders (NLAs) train a model to verbalize an activation into text and a second model to reconstruct the activation from that text. Reconstruction quality supplies a training signal for making the textual description informative.

This is a different attempt at scalable interpretability: rather than asking a specialist to inspect feature dashboards/graphs, produce natural-language summaries of internal state that an automated or human auditor can consume.

Important limitations stated by Anthropic:
- explanations can hallucinate;
- internal claims can be harder to verify than transcript claims;
- the technique is expensive and currently impractical for continuous monitoring of every activation/token;
- Anthropic recommends corroborating themes using independent methods.

This is almost a microcosm of System 3: **even the explanation of the model's internals needs an independent trust chain.**

Source:
- https://www.anthropic.com/research/natural-language-autoencoders

## 12. J-space / Jacobian lens: a candidate internal workspace

Anthropic's July 2026 work introduces the Jacobian lens (J-lens) and a set of verbalizable internal representations called the **J-space**.

Key reported properties in Claude:
- J-space representations are relatively reportable;
- Claude can modulate them in response to instructions;
- they participate causally in multi-step internal reasoning;
- they can be reused flexibly by multiple downstream computations;
- they account for only a minority of total internal activation activity;
- suppressing J-space leaves many automatic capabilities intact while damaging higher-order reasoning.

The safety result is even more relevant to Chapter 8: Anthropic reports using J-space readouts to detect Claude privately noticing that it is being tested, producing fabricated data, and pursuing a planted hidden goal. They also demonstrate interventions that change what is active in J-space and thereby alter downstream decisions.

This is qualitatively different from reading chain-of-thought. J-space is a model-internal activation phenomenon that may contain concepts never emitted as text.

Cautions:
- the J-lens is approximate;
- it focuses on representations linked to vocabulary tokens;
- J-space is not claimed to capture all model cognition;
- the work does not establish machine consciousness and should not be framed that way.

Sources:
- https://www.anthropic.com/research/global-workspace
- https://transformer-circuits.pub/2026/workspace/index.html

## 13. Chain-of-thought monitoring: a useful intermediate layer

CoT is not the same as model internals, but it sits between output-only oversight and mechanistic interpretability.

OpenAI's 2025 work shows that LLM monitors can detect reward hacking and other misbehavior from reasoning traces more effectively than from outputs/actions alone in studied settings. Crucially, directly optimizing against a CoT monitor can cause models to hide bad intent while continuing to misbehave.

Later monitorability work treats monitorability itself as a property worth preserving and evaluating. OpenAI's 2025–2026 results suggest current frontier reasoning models remain substantially monitorable in studied settings, while emphasizing that this may change with scale/training and that CoT monitoring should be combined with mechanistic methods rather than treated as sufficient.

This is a beautiful Ch8 principle:

> **Do not destroy a useful oversight channel merely because you learned how to score it.**

Sources:
- https://openai.com/index/chain-of-thought-monitoring/
- https://openai.com/index/evaluating-chain-of-thought-monitorability/
- https://openai.com/index/reasoning-models-chain-of-thought-controllability/

## 14. Reading and controlling are not the same epistemic act

The research repeatedly demonstrates a crucial distinction:

1. **Correlation / reading** — an internal direction predicts some concept or behavior.
2. **Causal validation** — intervention on that direction changes the behavior.
3. **Control** — use the intervention operationally to push behavior.
4. **Safety claim** — show that the intervention generalizes, survives adversaries, preserves capabilities, and does not create hidden failure modes.

Skipping steps is dangerous.

Examples:
- a sparse feature may look interpretable but not causally produce the expected behavior;
- a control vector may steer the target trait but alter unrelated capabilities;
- disabling a refusal direction demonstrates control but also produces a jailbreak;
- an NLA explanation may sound convincing while hallucinating details;
- a CoT monitor may work until training teaches the agent to hide its intent.

This suggests a System 3 rule for interpretability itself:

> **Every interpretability claim should be treated as a hypothesis that needs causal intervention and held-out behavioral validation.**

## 15. What this changes in the Chapter 8 arc

The earlier scalable-oversight arc should be expanded.

### A. The judge falls behind
Human action-by-action supervision fails as capability and throughput rise.

### B. Make the judge stronger
Amplification, debate, critique, process supervision, weak-to-strong, constitutional AI, model-written evals.

### C. Look inside the student
CoT monitoring, representation reading, SAEs, circuit tracing, model diffing, NLAs, J-space.

This is a major escalation: the overseer is no longer limited to asking the model to explain itself.

### D. Touch the machinery
ITI, ActAdd/CAA, RepControl, persona vectors, Assistant Axis, circuit breakers, feature/circuit interventions.

Oversight becomes **closed-loop control**:

observe internal state → form a hypothesis → intervene → inspect downstream behavior → update trust in the instrument.

### E. The inside can lie too
Interpretability tools are partial models of the model. They can miss representations, hallucinate explanations, conflate correlation and causation, impose human ontologies, or be gamed by future systems.

Therefore: never make interpretability the single oracle.

### F. Automatic alignment research becomes the integrator
An automated alignment-research institution can use:
- behavioral evals;
- adversarial tests;
- process/CoT monitors;
- representation probes;
- activation monitors;
- circuit traces;
- model diffs;
- causal steering;
- held-out tests;
- human adjudication.

The exciting possibility is not one magic X-ray into the model. It is an **epistemic sensor fusion system** for alignment.

## 16. High-value formulations for the prose

- **We spent years trying to supervise the student by reading the exam. Then we started instrumenting the student's brain.**
- **The model's output is evidence. Its chain of thought is more evidence. Its activations are more evidence. None is the court of final appeal.**
- **Interpretability turns alignment from behaviorism into instrumentation.**
- **Reading the model and controlling the model are different claims. Causal intervention is the bridge between them.**
- **The same lever that lets you make a model refuse can let an attacker make it stop refusing. Knowledge of the mechanism is power, not alignment.**
- **A scalable overseer should not have one pair of eyes. It should have instruments.**
- **The goal is not omniscience about the model. It is enough observability that hidden changes have somewhere to leak.**
- **J-space is interesting because some of the model's silent computation may become inspectable without forcing it through the same output channel it is trying to control.**
- **An explanation of an activation can hallucinate too. Even the X-ray needs calibration.**
- **Do not train away the smoke alarm just because it keeps detecting fires.**

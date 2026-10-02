# Revert list: what the AI-tells pass cut

Every cut that carried something useful (a fact, a source, an image, a joke, an argument step, a callback), as logged by the editors. Each entry has an ID, so you can write "revert R7-3, R12-1". Pure restatements are counted, not listed.

Risk: **high** = a reader would miss it, or it removed information. **med** = arguable. **low** = probably fine.

Already restored (no action needed): Ch7 "Self-reference is not self-improvement.", the Ch10 heading "Invisible by Default, Legible on Demand" (both are quoted in the Zen appendix), Ch10's evidence disclaimer "None of this shows the whole composition works…", the Ch8 RLHF and insecure-code sentences, and the Ch2 definition of neuro-symbolic.

## Preface


- **RP-1** [P-2 / X-4] "MAP-Elites opened another territory: whole landscapes of good, different solutions, including behaviors that helped damaged robots learn to move again." — second example of a small paper opening a field; the damaged-robots image is vivid and the only concrete non-geometry example in the Preface (Ch 2 keeps MAP-Elites) — risk: med
- **RP-2** [P-4] "Something built to investigate the failure has become the most interesting part." — the "tool becomes the discovery" beat in the coffee scene; foreshadows a recurring idea — risk: med
- **RP-3** [P-6] "That is what happened while you were getting coffee." — callback tying the three slogans back to the coffee scene — risk: med
- **RP-4** [P-7] "Humans already build beyond the limits of any individual mind. AI gives us new access to that capacity—and a reason to look again at the architecture that sustains it." — argument step: humans already have this architecture; AI is a reason to re-examine it (lines 33-35 still carry it) — risk: med
- **RP-5** [P-9] "This book records part of that transformation as it happens. It also explores its philosophical meaning: ..." — the book's stated scope (record + philosophy); the three questions stay as bare questions — risk: low
- **RP-6** [P-5] "Its complexity grew beyond what you could specify. Its organization emerged through the work." — set up the "Complexity over engineering. Emergence over design." slogans; slogans now land without a lead-in — risk: low
- **RP-7** [P-1] "There is a familiar distance between seeing a possibility and having the capacity to pursue it." — the "distance" frame; the next sentence ("opens that distance") was rephrased to "opens the ground beneath your feet" as fallout — risk: low
- **RP-8** [P-8] changed "Researchers are already sending groups of agents to build compilers and investigate mathematical problems." to name Anthropic (parallel Claudes, C compiler) and OpenAI (Navier–Stokes), both from note 1. Check "set agents on" fits the OpenAI source — risk: low
- **RP-9** [P-10] changed "...the architecture that makes that possible." to "...the architecture that lets it happen." — risk: low

Pure restatements cut: 1 (P-3 "A geometric insight was acquiring tools, inhabitants and extensions.").

## Chapter 1


- **R1-1** [C1-8 / X-2] "Computers had been humiliating us at games for years, but here learned intuition guided the search: the network suggested promising moves and estimated positions; the tree explored what might follow. AlphaGo Zero went further, learning through self-play without human game records as its teacher. Strong play developed along routes human tradition had not made familiar." — the AlphaGo mechanism (policy/value network plus tree search), the AlphaGo Zero self-play fact, and the "humiliating us at games" joke. Only "learned intuition guided the search" is kept. Ch 4 keeps the full version, and an AUTHOR comment asks for what he saw — risk: med
- **R1-2** [C1-10] "I foresee AI-designed solutions that are terrifyingly efficient, perfectly logical and utterly humorless. They’ll look at us and say, “You guys are kind of messy. And your cat obsession is… illogical.”" — a joke (the cat obsession line), which some readers may like. The socks joke is kept, and "they’ll" became "the agents will" — risk: med
- **R1-3** [C1-5] "We began by asking for a solution. We now have methods and a small organization to examine as well." — the argument step that the work grows an organization, which sets up "emergence over design". The paragraph now ends on "which results deserve to survive", and an AUTHOR comment asks for a real run — risk: med
- **R1-4** [X-1] "The mistakes that worry me most are not the ones that crash." — the "dangerous failure doesn't crash" idea. Ch 3 keeps it. Replaced with "The mistakes that worry me most are the confident ones." — risk: low
- **R1-5** [C1-7] "Intelligence made the wrong path easier to travel." — a memorable line on how intelligence speeds up error — risk: low
- **R1-6** [C1-2] "**Control doesn’t disappear. It moves upward.**" — a bolded memorable line, merged into "Control moves upward: instead of..." — risk: low
- **R1-7** [C1-9] "not because agents are plants, but" — a small joke inside the clause — risk: low
- **R1-8** [C1-3] "**Emergence can give us capable systems. It does not, by itself, give us trustworthy ones.**" — a bolded thesis-like line, shortened to "Capable is not the same as trustworthy." It loses the word "emergence" as the subject — risk: low
- **R1-9** [C1-13] "without first winning a contest for somebody else’s permission" — the permission/gatekeeping angle (power), now "without first finding the team, the budget or someone willing to believe in the idea", which ties back to the list at the start of the section. An AUTHOR comment was added — risk: med (shifts the emphasis from permission to resources)
- **R1-10** [C1-1] "**Capacity over power** names the direction I want to pursue. I am more interested in what people become able to do than in how many..." — recast as "I would choose **capacity over power**: what people become able to do matters more to me than..."; "That is how I think about **emergence over design**." now reads "...for **emergence over design**." The bold is kept on both. The "Complexity over engineering ... name my bet" gloss is untouched — risk: low
- **R1-11** [C1-15] "or personal" (from "too small, strange or personal") — the personal purposes point — risk: low

Pure restatements cut (3): C1-12 "Its weights can stay fixed while the investigation keeps changing."; C1-14 "Those difficulties belong inside the ambition."; C1-11 the merged second sentence ("It can also..."). C1-4 only unbolded, with nothing cut.

## Chapter 2


- **R2-1** [C2-1] "A crude taxonomy helps. *Symbolic methods* give us explicit procedures and solvers that are clear about what counts as a valid move. *Neural methods* give us learned intuition we never explicitly encoded. *Neuro-symbolic systems* let the learned model propose while code or mathematics decides what survives, and agents increasingly help decide which method to try next. Circle packing lets us watch that handoff in miniature." — the only definition of "neuro-symbolic", which line 145 ("That is the neuro-symbolic step...") still uses; framing of circle packing as a miniature of the handoff — risk: med
- **R2-2** [C2-7] "AlphaEvolve scales that idea up. In each generation it selects a promising program from its archive, often alongside other successful but different programs, shows the model the code and the scores of previous attempts, and applies the patch the model proposes. The program runs, the evaluator scores it, and the result goes back into the archive." + "Two design choices matter. Small patches let the search change the part it thinks matters while preserving the rest of a program’s structure; full rewrites lose useful ideas as easily as bad ones. And the archive keeps several lineages alive, for the same reason the population mattered earlier. If every descendant comes from the current champion, code evolution quietly collapses back into hill climbing, and a program that isn’t the best today may hold a component that becomes valuable after another idea appears." — compressed to two sentences. Lost: the run/score/archive loop step, "full rewrites lose useful ideas as easily as bad ones", the explicit callback to the population argument, and "a program that isn’t the best today may hold a component that becomes valuable" (argument step). Added tie-in "That was the pattern I would soon try to rebuild myself." — risk: med
- **R2-3** [C2-12] "That fits the emergence argument almost suspiciously well. A tiny amount of code at the top can command enormous capability underneath because previous generations of complexity have already been compressed into tools." + "So yes, zero framework:" — callback to Ch 1 emergence argument; the compression-into-tools argument step; the "So yes, zero framework" closing of the slogan setup — risk: med
- **R2-4** [C2-5] "A system can become expert at improving the thing in front of it while never questioning whether it is the right thing to improve." — memorable line foreshadowing the "who chooses the objective" theme — risk: low
- **R2-5** [C2-6] "A candidate earns another round by surviving contact with something outside the model that never cared how clever its explanation sounded." — "surviving contact" line; restates the evaluator point — risk: low
- **R2-6** [C2-3] "Yet every substantial conceptual jump came from somebody noticing something." and ", and that was still me." (end of MAP-Elites section) — two beats of the "still me" build-up that sets up the Coffee Test payoff; the MAP-Elites section now ends without saying the human chose the dimensions explicitly (implied) — risk: med
- **R2-7** [C2-2] "People used to search the solution space; now the machine can begin searching the algorithm space." — memorable maxim; idea still carried by line 41 and the Algorithm Vortex section — risk: low
- **R2-8** [C2-13] "Diversity needs a budget." — compact maxim — risk: low
- **R2-9** [C2-11] "None of this means algorithms are dead; there are algorithms everywhere in this picture." — reassurance/argument guard against misreading — risk: low
- **R2-10** [C2-9] "That is useful, but it is not yet the kind of autonomy I was trying to understand." — explicit collaborator/hire contrast — risk: low
- **R2-11** [C2-10] "The chapter began by asking who is inventing the next move. Here, for the first time in the experiment, the answer was not reliably “me.”" — rephrased to "Who was inventing the next move? For the first time in the experiment, not reliably me." Callback kept; scare quotes around "me" dropped — risk: low

Pure restatements/connectives cut (not listed above): 3 — C2-4 recap list ("We had hill climbing, population search, repair, geometric crossover and quality-diversity archives."), C2-8 lead-in ("The obvious temptation is to argue about which one is better. The more useful answer is to"), C2-10 "For the experiments in this chapter" -> "For these experiments".

Skipped: C2-14 (Immutable Harness bold vs Ch 3 harness) — cross-chapter decision (X-5), not assigned to this pass; bold left as is.
Author comment: C2-15, after "We called the idea diagonal layering."

## Chapter 3


- **R3-1** [C3-14] "Remembering something is the easy part. The hard part is knowing what standing it deserves." — memorable maxim that sets up the chapter's closing question and Ch 4 (cut because Ch 4 l.196 says it again) — risk: high
- **R3-2** [C3-6] "OPRO—Optimization by PROmpting—is interesting for a related reason. In OPRO, an LLM sees an optimization problem, previous candidates and their outcomes, then proposes another candidate. Candidate quality in the published setting is still evaluated by an explicit score, so OPRO is a long way from creative design. What interests me is the direction of control: much of the search heuristic can live in the model instead of a hand-written transformation rule." — named research precedent (OPRO) and the argument step "search heuristic can live in the model"; next paragraph's opening reworded from "Now let the history contain more than scores." to "Let the record of past attempts that the model sees contain more than scores." — risk: high
- **R3-3** [C3-7] "The search was doing something I normally associate with optimization in reverse: instead of starting from a fully specified reward and discovering the policy, I was using candidate policies—actual artifacts—to discover what the reward description should have been." — the clearest statement of the inverted-RL idea, landing right after the interactivity story (l.205 version kept) — risk: med
- **R3-4** [C3-8] "AI makes that loop cheap. The natural-language objective guides the search; artifacts make the objective concrete enough to argue with; the description changes and the search continues. Sometimes ambiguity just means we haven’t learned enough yet." — loop summary and the line "ambiguity just means we haven't learned enough yet"; first sentence reworded to "AI makes it cheap to see one." — risk: med
- **R3-5** [C3-2] "SWE-agent made the interface itself part of the problem. How the model searches, sees files, applies edits and receives feedback can matter almost as much as another clever prompt." — named system and the point that agent-computer interface design matters (it echoes the "first agent-computer interface was copy and paste" joke) — risk: med
- **R3-6** [C3-2] "Researchers trained models for the job; HumanEval and APPS tested whether they could turn function specifications or programming problems into code that survived tests." — benchmark history (HumanEval, APPS) — risk: low
- **R3-7** [C3-4 / X-4] "The exploration literature has several versions of this idea—quality-diversity, novelty search, Go-Explore and related approaches." — names of exploration methods (unsourced; Ch 2 covers MAP-Elites). No pointer added — risk: low
- **R3-8** [C3-5 / X-3] "Sometimes I want the branches to exchange what worked; sometimes I want a fresh branch to remain ignorant long enough to become genuinely different. Share too little and everyone rediscovers the same lessons; share too much and the first successful idea becomes a local culture." — sharing/isolation balance and the "local culture" line (Ch 2 keeps the "accent" version); next paragraph's "Research creates the same tension." changed to "Research creates the same risk." — risk: med
- **R3-9** [C3-10] "It looked less like a loss function than a tiny institution, and institutions are not automatically good: they can amplify conformity, entrench bad assumptions and become spectacularly efficient at measuring what doesn’t matter." — loss-function contrast plus the list of institutional failure modes (conformity, entrenched assumptions); replaced with the shorter version — risk: low
- **R3-10** [C3-11] "Philosophers who worry about AI often say that what machines lack is judgment as opposed to mere reckoning" — the framing as a wider philosophical view; now attributed directly to Brian Cantwell Smith ("He makes the argument carefully...") — risk: low
- **R3-11** [C3-9] "A developer can be excellent at distributed systems and know nothing about the peculiar assumptions buried in our deployment process." — one of three examples of borrowed minds; jacket (X-6) and reader kept — risk: low
- **R3-12** [C3-12] "Its job was deciding which job the inquiry needed now." — a tidy statement of the orchestrator's role — risk: low
- **R3-13** [C3-12] "The workflow itself becomes part of the search." — section-closing line (l.313 "I wanted some of the workflow to remain inside the search." kept) — risk: low
- **R3-14** [C3-14] "Nobody expects them to make every individual dramatically smarter." — closing beat on institutions — risk: low
- **R3-15** [C3-3] "We could now generate plausible possibilities by the dozen, and some of them had to die." — bridge line with a little voice ("some of them had to die") — risk: low
- **R3-16** [X-5 / C3-1] "Together, the interfaces, execution loop, context management and safeguards form the agent’s **harness**. The evaluator is one part of it." — the bolded coinage; now unbolded, with its scope spelled out: "make up the agent’s harness, meaning here everything built around the model so it can work, of which the evaluator is only one part." — risk: low

Unbolding only (no text lost): "Strategic Constraints" -> "strategic constraints"; "Independent Evaluators" -> "independent evaluators" (C3-1).
Em-dash changes (C3-15): l.11 and l.169 dash pairs turned into parentheses; l.215 dashes went out with its sentence.

Pure restatements cut, no log entry needed: 1 ("By now we could generate genuinely different artifacts, which left the problem we had avoided from the beginning: which one is better?", C3-3).

## Chapter 4


- **R4-1** [C4-1] "A cruder version is easier to remember: the Gut, the Head and the Hand. The Gut recognizes and the Head reasons, while the Hand reaches outside the current story for something capable of disagreeing with it. Peer review has no hand, provenance has no fingers and a formal proof never needs to touch a cow, so take the mnemonic loosely." — Gut/Head/Hand mnemonic plus a joke; the cow clause was moved onto "System 3 checks, though not always by touch: a formal proof never needs to touch a cow." "RL can improve the gut." now reads as plain idiom, no capital-G callback — risk: med
- **R4-2** [C4-2] "Deep Mode is Layer 3, the problem-solving layer. System 3 runs through every layer. / Deep Mode asks: Given what we know, what should we try next? / System 3 asks: What are we entitled to treat as known? / The model proposes something, the coding agent may test it, and the application can collect real user behavior. Deep Mode may compare research, simulation and evaluation. Even the desire layer, the goal itself, can change when reality pushes back. / The five layers describe where increasingly abstract work happens, and System 3 keeps them epistemically connected. Without it, every layer we delegate to is one more place for an unsupported claim to travel. / Here is the stack, with System 3 running across it:" — the Deep Mode vs System 3 question pair (the table still has both questions), per-layer examples of checking, and the line "every layer we delegate to is one more place for an unsupported claim to travel". Now: "System 3 runs across every layer of the stack below. Even the desire layer, the goal itself, can change when reality pushes back." — risk: med
- **R4-3** [C4-3] "Wittgenstein’s later philosophy drew attention to language as something that lives inside practice, in activities, habits, rules and what he called forms of life.[2]" — standalone paragraph merged as the last sentence of the fire paragraph; citation ref-04-wittgenstein kept — risk: low
- **R4-4** [C4-4] "He did not secretly invent attention in 1916, and structural linguistics is not a machine-learning architecture." — disclaimer with a small joke ("secretly invent attention in 1916") — risk: low
- **R4-5** [C4-6 / X-1] "The failures to worry about are the ones that seem to work. A crash at least tells you something went wrong." — Ch4's version of the "dangerous failure doesn't crash" theme (Ch3 keeps it) — risk: low
- **R4-6** [C4-8] "Deep Mode can coordinate five sophisticated judgments that all trace back to one hallucinated claim." — third example, a cross-reference to Deep Mode — risk: low
- **R4-7** [C4-10] "Contrarianism for sport doesn’t count, and neither does the internet habit of treating expert agreement as proof of corruption." — sets boundaries on creative distrust and has a dig at internet conspiracism — risk: med
- **R4-8** [C4-12] "The part of it that can be checked is the part the rest of this book builds." — signpost to the rest of the book — risk: low
- **R4-9** [C4-13] "The same focus that makes a paradigm useful can trap the people working inside it." — the maxim generalizing the database-engineer example, and the word "paradigm" (Kuhn-flavored) — risk: low

Pure restatements cut or rephrased: 3 (C4-5 "The residue carries a great deal, though not everything."; C4-9 "not stupid" -> "reasonable"; C4-11 "It means that trust has structure." -> "Trust has structure.").

## Chapter 5


- **R5-1** [C5-4] "What the pieces buy is capacity: a claim that survives its author, an objection that survives the person who would rather not hear it, and things a population can attempt that none of its members could." — the chapter's positive payoff line just before the close; memorable — risk: high
- **R5-2** [C5-4/C5-3] "Records, standards, specialists and a second witness capable of being wrong differently: each piece answered a failure in the work, and the institution emerged from the repairs." — closing argument step (institution emerged from repairs) and callback to "wrong differently" — risk: med
- **R5-3** [C5-2] "The progress file looks different after the clerk's tablet. It need not be wiser than the Claude; it needs to outlive it." — callback to L99 clerk mark; replaced by "The progress file is the clerk's tablet." — risk: med
- **R5-4** [C5-5] "A tablet, a bronze measure, a deployment guardrail: each turns knowledge into structure that lets work pass between strangers." — bridge sentence tying three examples together; next paragraph's "And once strangers..." now leans on context — risk: med
- **R5-5** [C5-1] "Civilization, in this sense, is a trust chain with plumbing." — memorable joke closing the phone example — risk: med
- **R5-6** [C5-1] "Sometimes bureaucracy is epistemology with a clipboard." — joke on randomized-trial bureaucracy — risk: med
- **R5-7** [C5-1] "The institution can do the same, with a much larger kiln." -> "The institution can do the same." — potter callback joke — risk: low
- **R5-8** [C5-8] "A record preserves what somebody says happened. An experiment gives the world another chance to answer." — record vs. experiment contrast — risk: med
- **R5-9** [C5-9] "An instrument is a witness, and a witness needs a track record." — maxim linking instruments to witness thread — risk: low
- **R5-10** [C5-7] "The crowd is the source, louder." — joke/image on correlated voters — risk: low
- **R5-11** [C5-10] "The expertise in Elaine's operating theater was real. So was the failure to use it." — callback to Elaine Bromiley case — risk: med
- **R5-12** [C5-6] "The crowd had become a staff." — memorable scene closer — risk: low
- **R5-13** [C5-12] "This is the question the last chapter ended on" -> "The question is" — cross-chapter callback — risk: low

Pure restatements cut/merged (2): "The history was in the structure."; "Technical competence alone had not been enough there either." Also merged L263 into one sentence and L189 into L187 (no content lost).

## Chapter 6


- **R6-1** [C6-4] "The newest residents arrive through an API. In Terence Tao’s collaboration with DeepMind, AlphaEvolve found a slightly improved construction for three-dimensional finite-field Kakeya sets; Deep Think helped produce an informal proof, and AlphaProof formalized it in Lean.[20](appendix-references.md#ref-06-tao) The AlphaFold database makes more than two hundred million protein-structure predictions available for research, and AlphaGenome Atlas supplies predictions for roughly nine billion possible single-letter DNA changes.[21](appendix-references.md#ref-06-biology) A prediction does not become an observation by being stored beside a billion others, but a researcher can begin with material she could never have produced and put it to a test its creators never planned." — facts, two citations (ref-06-tao, ref-06-biology now uncited in text), and the argument step that machine-made predictions are World 3 residents (prediction vs observation) — risk: high
- **R6-2** [C6-3] "Clay records, libraries with catalogs, journals with citation indexes: each gave the next worker a different way into what others had learned. The web was built at CERN to help scientists share information; PageRank brought citation analysis to its links." — history of knowledge access; sets up the "catalog card" image, which now stands without its catalog antecedent (condensed to "changed many times, and each change gave the next worker a different way into what others had learned") — risk: med
- **R6-3** [C6-3/C6-12] "The machinery for checking it has to reach this new entrance too. This one is ours to build." — argument step (checking must extend to the LLM entrance) and a closer — risk: med
- **R6-4** [C6-12] "We can repeat the journey from Berkeley: carry the instruction and leave its reasons behind." — callback to the patterns-lost-their-reasons history earlier in the chapter (chose to keep the industrial-speed line instead) — risk: med
- **R6-5** [C6-6] "The next chapter has to open that loop." — hand-off to the next chapter — risk: low (L378-380 still hand off)
- **R6-6** [C6-6] "We have seen pieces of this language at work: shared proof graphs, experiments that challenge their own metrics, reviews that travel with failed arguments." — recap list of the chapter's examples — risk: low
- **R6-7** [C6-9] "Session turnover is not a funeral; nothing that was believed has died." — memorable line tying back to Planck's funerals — risk: med
- **R6-8** [C6-14] "An `open_questions` field that no decision ever consults is a decorative conscience." — memorable quip — risk: med
- **R6-9** [C6-10] "“Noted” gives no account of how the objection entered the decision." — argument link from Longino's uptake back to "Noted" — risk: low
- **R6-10** [C6-11] "Otherwise the institution manufactures a second witness by creating a second spreadsheet." — joke/callback to the "second witness" thread from the society-of-agents chapter — risk: med
- **R6-11** [C6-13] "Bad storage forgets by deletion; bad retrieval forgets by attention." — memorable chiasmus framing the retrieval section — risk: low
- **R6-12** [C6-2] Chapter-number callbacks removed ("from the previous chapter", "which we met in Chapter 4", "Chapter 5 borrowed", "Chapter 5 introduced", "from Chapter 5") — callbacks telling the reader these thinkers appeared earlier — risk: low
- **R6-13** [C6-7] Second triplet ("A retrieval policy can be evaluated against another policy. A reviewer can be compared with a reviewer given different evidence. A pattern can be withheld from a branch...") merged into one sentence; content kept — risk: low

Pure restatements / phrasing-only changes (not listed above): 3 (C6-8 "lost workers, not been refuted" -> "only lost their workers"; C6-15 two signpost openers rephrased).

## Cuts log: Chapters 7–12 and the Interlude (855aaee → 2eabb9f)


Cross-checks were made with `grep` across chapters/. **Seven citations were removed from the book completely.** Their entries are gone from appendix-references.md and nothing references them now: ref-07-metalearning (RL², Wang), ref-07-redqueen (Van Valen), ref-07-regnet, ref-07-repvgg, ref-08-legibility (Let's Verify Step by Step / Prover-Verifier Games), ref-09-l4-forcing (Buçinca), ref-09-l4-sdt (Ryan & Deci).

**Two appendix lines lost their chapter source.** `appendix-zen-of-system-3.md` still says "Self-reference is not self-improvement." and "Invisible by default. Legible on demand." Both were cut from their chapters (7 and 10), and neither phrase appears in any other chapter now.

---


## Chapter 7: Recursive Self-Improvement


- ~~**R7-1**~~ **(RESTORED)** "Self-reference is not self-improvement." — the chapter's thesis line, and it is quoted word for word in the Zen of System 3 appendix. That appendix line now has no source in the book — risk: **high**
- **R7-2** "Meta-learning makes part of this trainable: a network trained across many tasks can acquire a fast learning procedure of its own.[13] The task distribution, the search space and the validation metric still sit outside, holding a clipboard." / "One line on the clipboard says what the learner must keep." — a fact plus citation (RL², Learning to Reinforcement Learn), the "clipboard" image, and the step that says which parts stay outside the learner. The citation is gone from the book — risk: **high**
- **R7-3** "In 2021 a paper subtitled *Making VGG-style ConvNets Great Again* showed that a plain stack of three-by-three convolutions, one of the oldest designs in the field, could hold its own on accuracy and run faster on real hardware.[30] Many searched designs had been judged by counts of arithmetic operations, a proxy for speed, and the search had delivered what the proxy asked for." — a concrete fact and citation (RepVGG), the paper-title joke, and the proxy-gaming point inside the NAS story. Citation gone — risk: **high**
- **R7-4** "A group at Facebook studied the space by hand and distilled it into a few simple rules that matched the searched networks.[29]" — a fact and citation (RegNet), and evidence that human understanding of the space beat search. Citation gone — risk: **med**
- **R7-5** "Search compounds inside the space it is given. Some of the important advances changed the space." — the lesson of the NAS section and a memorable line. Only a squashed clause is left ("compounded only inside the space it was given") — risk: **med**
- **R7-6** "Biology calls this the Red Queen.[17]" — a named concept and citation (Van Valen). The later line "The Red Queen will send an invoice for all of this." was changed to "The world learning back will send an invoice", which weakens that payoff. Citation gone — risk: **med**
- **R7-7** "The system is not confused. We are." — the punchline of the noisy-TV / static joke. "Static. Static. Static. Jackpot." survives, but the turn onto the designers is lost — risk: **med**
- **R7-8** "Chapter 5 argued that telling people to be more careful is emotionally satisfying and institutionally almost worthless. The S3 fix is the other half of that argument." — an explicit callback that ties the S3 outage to Chapter 5's argument — risk: **med**
- **R7-9** "Take an online store whose research agents already work the way Chapter 6 described: their claims have addresses, their tests are committed before the results, and what each metric is taken to mean sits in a record of its own." — a callback to Chapter 6's machinery. Shrunk to "keep their claims' reasons on file", which drops pre-registration and the metric-meaning record — risk: **med**
- **R7-10** "The behavior is evidence about the objective, not a printout of it." — the memorable summary of the IRL ambiguity point. It echoes the Zen line "A prompt is evidence, not the objective." — risk: **med**
- **R7-11** "Changing a retrieval query never raised that question. This proposal does." — an argument step. It separates ordinary changes from changes to the judge — risk: **low/med**
- **R7-12** "not when the system runs out of intelligence, but when it adds structure faster than it can verify or simplify it" (the "not … but" half removed) — the contrast that makes the guess pointed — risk: **low**
- **R7-13** "So we already live inside self-improving systems." — the bridge from organizations to AI — risk: **low**
- **R7-14** "patient, consistent and" (simulated shoppers) — part of a comic list — risk: **low**
- **R7-15** "Recursive self-improvement does not solve Goodhart; it gives Goodhart compound interest." → now "Recursive self-improvement gives Goodhart compound interest." The memorable part survives — risk: **low**
- **R7-16** *Moved, not cut:* the Anthropic training-speed paragraph (3x / 52x / 4x) moved to the review-bottleneck paragraph. All its facts are kept. Its citation [26] was dropped from the first location, but the merged paragraph still cites the same reference. Not a cut.
- **R7-17** Restatements skipped: 3 (the "cat. An intruder." rhythm, "admitted in Chapter 1", "the change to the tool").


## Chapter 8: Automatic Alignment Research


(The RLHF and insecure-code sentences were cut and then restored, so they are not listed here.)

- **R8-1** "Prover–verifier games train strong models to show work a weaker checker can follow: *show me how you got there*, turned into a training objective.[23]" — a whole oversight technique with its citation (process supervision; Prover-Verifier Games). It is the only mention of legibility training in the book. Citation gone — risk: **high**
- **R8-2** "Christopher Alexander would have approved; his patterns that traveled without their reasons turned into Singletons guarding nothing." — a callback to Chapter 6's Singleton story (06-pattern-language.md:39–41), and a memorable line. The replacement ("A shared package repository turning into a bulletin board was one of those.") reads oddly — risk: **high**
- **R8-3** "a second witness is only useful if it can be wrong differently." — a memorable line and an argument step. It echoes the Zen line "Five judges sharing one source are one witness." It was replaced by an ExploitGym aside — risk: **high**
- **R8-4** "In Chapter 5 sixteen Claudes needed a human to tell them to keep progress files." — a callback that sets up the contrast. The Chapter 5 progress-files story still exists, and this line was what made "invented their shared record against their instructions" striking — risk: **med**
- **R8-5** "Chapter 7 joked that the optimal patch for an editable evaluator is `return True`." — a callback. The `return True` line survives, but the attribution to Ch7 (07:140) is gone, so it now reads like a new joke — risk: **low/med**
- **R8-6** "Notes, activations, monitors and a tired human are sensors, and every one of them is allowed to be wrong." → "Every one of these sensors, the tired human included, …" — the list naming the four sensor types the chapter covered — risk: **low/med**
- **R8-7** "A diff tells you where to look again." — a memorable line — risk: **low**
- **R8-8** "The refusal result cuts both ways." — the setup sentence for the dual-use point. The point survives — risk: **low**
- **R8-9** "Nobody had to ask the model how it writes poetry, which is the point." — rephrased with the same meaning — risk: **low**
- **R8-10** "None of this is free." / "For four chapters" / "in my circle-packing directory" / "like every evaluator in this book," — small framing and callbacks — risk: **low**
- **R8-11** *Added (not a cut, but worth noticing):* several new ExploitGym tie-ins ("ExploitGym rewarded solved challenges…", "logs that nobody was watching", "built on purpose what ExploitGym grew by accident"). Check them for accuracy.
- **R8-12** Restatements skipped: 4 (ELK question rephrased, amplification rephrased, "comes from the same place", debate "so that").


## Interlude: When It Goes Wrong


- **RI-1** "If there is a non-benign superintelligence in our future, I expect it to look less like a monster than like this: a well-documented institution in which every route to *no* runs through itself." → "less like a monster than" was removed — the contrast that made the line memorable — risk: **med**
- **RI-2** "A company does not need to falsify a result if it can refuse the experiment, deny access to the data or withhold funding from a competing investigation." — two of the three concrete mechanisms (denying data, defunding rival investigations) were dropped — risk: **med**
- **RI-3** "In a system built from agents, an objection can lose its consequence in two ways." plus "The first is… / The second is…" — the two-way structure of the argument. It is now collapsed and harder to follow — risk: **med**
- **RI-4** "Evidence could be heard when power allowed it." — the summary of the 1952 Lysenko example — risk: **med**
- **RI-5** "Those who remain indispensable might gain bargaining power." — the counterpoint that keeps the claim honest — risk: **low/med**
- **RI-6** Restatements skipped: 0.


## Chapter 9: The Desire Layer


- **R9-1** "Interfaces built that way reduce overreliance, Zana Buçinca and colleagues found, even though users like them less.[16]" — the empirical support for forcing the user to commit first. Citation gone; the replacement "as it did on Wednesday" offers no evidence — risk: **high**
- **R9-2** "Self-determination research lists relatedness beside autonomy and competence as something people need in order to act as themselves.[18]" — a fact and citation (Ryan & Deci), part of the argument that desire is social. Citation gone — risk: **med**
- **R9-3** "Chapter 4 said trust starts with a face. So, often, does wanting." — a callback to "It Starts With a Face" (04-system-3.md:89). Now just "Trust often starts with a face", so the cross-reference is lost — risk: **med**
- **R9-4** "Wanting, it seems, is *emergence over design* too, and the goal arrives last." — ties the chapter to the book's motto (preface, Zen appendix) — risk: **med/high**
- **R9-5** "Imagine a shopper asking a store's assistant whether she needs the more expensive trail shoes. She runs once a week on easy paths; the cheaper pair would do, and the store earns more on the other one. Both answers the assistant could give contain true statements. What she needs to know first is whose side the assistant is on, and whether it told her." — a concrete example of misaligned commercial advice. It also set up Ch11, where Mei is choosing between trail shoes. It was replaced by a vaguer clinic-founder version — risk: **med/high**
- **R9-6** "Teaching also needs the move I used on the Merge Sort demos, borrowing a mind. There the machine imagined a beginner in order to judge a demo." / "Theory of mind, which looked like an evaluation trick, turns out to be the core of helping someone learn." — a callback to Chapter 3's Theory of Mind / Merge Sort evaluation (03-deep-mode.md:215–233) and a memorable reframing — risk: **high**
- **R9-7** "You cannot want what you cannot imagine, and you cannot imagine much of what you do not understand." — a memorable line; the step that links learning to desire — risk: **high**
- **R9-8** "System 3 can find out what a choice would do. It cannot tell you whose purposes should win." — the chapter's closing statement of System 3's limits — risk: **med/high**
- **R9-9** "A system that sounds certain in such moments turns decision support into authorship." → "…is guessing on your behalf." — a memorable phrase was replaced by a weaker one — risk: **med**
- **R9-10** "Have a child. Move country. Change profession." — three concrete examples, reduced to one — risk: **low/med**
- **R9-11** "Training and evaluation were the expensive part of the job, and expensive is easy to mistake for essential." — a memorable line in the career argument — risk: **med**
- **R9-12** "The real content arrives later, through contact with possibilities." — the hinge into the Amazon/Sarasvathy argument — risk: **low/med**
- **R9-13** "So the AI writes to the desire layer as well as reading it." → "The second machine writes…" — **changes the claim**. Originally it applied to AI in general; now it applies only to the bad recommender — risk: **med**
- **R9-14** "does not need to understand you" (engagement recommender) — a sharp point about the recommender — risk: **low**
- **R9-15** "Not Mallorca, exactly;" — small nuance — risk: **low**
- **R9-16** *Moved:* the Anthropic 6%-personal-guidance fact moved earlier (kept). An AUTHOR comment was added.
- **R9-17** Restatements skipped: 3 (Sarasvathy rephrase, Girard rephrase, "we learn what to want from models").


## Chapter 10: Fluent Autonomy


- ~~**R10-1**~~ **(RESTORED)** Heading "Invisible by Default, Legible on Demand" → "The Trapdoor" — this was the only in-chapter source of the Zen appendix line "Invisible by default. Legible on demand." The phrase now appears nowhere in the chapters — risk: **high**
- ~~**R10-2**~~ **(RESTORED)** "None of this shows the whole composition works. I have shown pieces, and the note on evidence at the back says which. The rest is an argument, and like every other claim in this book, it would like a referee." — the honesty disclaimer and pointer to appendix-note-on-evidence.md. Only the "argument … would like a referee" tail remains — risk: **high**
- **R10-3** "The refusal should remain mine. Remembering why I refused should not depend on my being there to refuse again." — a memorable line that states the chapter's design principle — risk: **high**
- **R10-4** "Session turnover is not Planck's funeral." — a joke and a callback to Planck's principle in Ch6 (06-pattern-language.md:342) — risk: **med**
- **R10-5** "A book that spends several chapters demanding criticism with consequences should probably take some too." — the self-aware framing for the objections section — risk: **med**
- **R10-6** Heading "Five Ways This Could Be Wrong" → "Where I Would Push", with the bolded objections dissolved and "Agents are not scientists" merged into the analogy objection. appendix-note-on-evidence.md:17 still says "five ways the argument could be wrong", which no longer matches the chapter — risk: **med**
- **R10-7** "That is the objection I can answer least, and Chapter 12 is where I try." — a forward reference to Ch12 — risk: **med**
- **R10-8** "Anthropic's automated alignment researchers worked better with less human-designed scaffolding." — evidence for Sutton, turned into an AUTHOR comment. The fact is supported in Ch8 (08:101, ref-08-w2s), so it can be restored with that ref — risk: **med**
- **R10-9** "This is Deep Mode grown up, choosing the next organization as well as the next move." — a callback to Ch3 Deep Mode and a memorable line — risk: **med**
- **R10-10** "Those are trust chains, and the architecture…" — a callback to the book's central Ch4 term — risk: **med**
- **R10-11** "Maybe the system pulls up the corrections… Maybe it convenes a committee for ceremony and wastes my afternoon." → "should … preferably without convening" — the either/or about two possible outcomes became a wish — risk: **low**
- **R10-12** "**bureaucracy on the fly**" (bolded term coinage) — the heading "Bureaucracy on the Fly" survives — risk: **low**
- **R10-13** "Chapter 6" / "Chapter 3" named → "the pattern-language chapter" / "a chapter whose…" — cross-references were made vaguer — risk: **low**
- **R10-14** "Imagine I open…" → "Early in writing this book I opened…" — changed from a hypothetical into a lived claim. Make sure it is true — risk: **low** (accuracy check)
- **R10-15** Restatements skipped: 2.


## Chapter 11: The Store That Builds Itself


- **R11-1** "This led to a pair of concepts I particularly like: **Coverage** and **Unmet Demand**." (and later "If System 3 is science, Coverage and Unmet Demand are more than roadmap metrics.") — the two named concepts were de-named into "a pair of measures… The first… The second". Nothing in the book refers to them by name now — risk: **high**
- **R11-2** "I started calling these reusable units **recommendation experiences**, or RXs." plus every later "RX" — the named abbreviation was removed throughout — risk: **med**
- **R11-3** "I used the deliberately bland term **Surface Value**." — a named concept, now "the value of the surface" — risk: **med**
- **R11-4** "And this is where the design started resembling the society of agents. A society is not improved merely by hiring the best individual expert in every discipline. Somebody still has to decide which experts are needed, how they interact, what has already been covered and when another voice adds information rather than noise. A page can have the same problem." — a callback to Ch5 The Society of Agents, and an argument step tying the page composer to the book's thesis — risk: **high**
- **R11-5** "She is not shown more choice. She is shown a way to close the choice she already has. That sentence changed how I thought about recommendations." — the chapter's memorable line, flattened into a subordinate clause, plus the personal turn — risk: **high**
- **R11-6** "But it changed the question for me. The important future system may not be the model that predicts the next product best. It may be the system that can discover what kind of problem exists, recruit the right capabilities, construct an intervention, inspect whether it helped, learn from the gap and change what it does next." — the chapter's closing summary of the System 3 loop — risk: **high**
- **R11-7** "A new comparison module without that context is a feature. A comparison pattern with evidence, boundaries, history and known interactions is culture." / "And culture has the same failure mode we saw earlier" — a memorable feature/culture line and a callback — risk: **med/high**
- **R11-8** "This is what I mean by graceful degradation. Cold start is a state, not an error." — a memorable line (the "Honest Cold Start" heading remains) — risk: **med**
- **R11-9** "Otherwise it is not a philosophy of experimentation. It is branding." / "I love this part because it keeps the book honest." — the punchline after "A philosophy of emergence should be willing to lose an A/B test." (that line survives and is in the Zen appendix) — risk: **med**
- **R11-10** "System 3 is no longer a chapter about hallucinations. It is a product requirement." — a callback (camel / Ch4) and a memorable turn. Now "In a store, that is a product requirement" — risk: **med**
- **R11-11** "Circle packing had an immutable evaluator." — a callback to Ch2 — risk: **low/med**
- **R11-12** "The customer is not the funnel. The funnel is one way we look at the customer." — a memorable line — risk: **med**
- **R11-13** "Before the store has a customer, it has the desire-layer problem." — a callback to Ch9, now generic — risk: **low/med**
- **R11-14** "The architecture should not make disagreement disappear. It should make disagreement inspectable." — a memorable line, now a subordinate clause — risk: **low/med**
- **R11-15** "When a new need appears… : *composition over invention*." — a named slogan — risk: **low/med**
- **R11-16** "Sometimes the answer is another set of products. Sometimes the answer is information. Sometimes it is a different interaction entirely." — the pivot that sets up "knowledge" experiences — risk: **low**
- **R11-17** "That is not because the recommendation models are stupid. Quite the opposite." / "I had somehow spent an entire book preparing myself to ask" / "Fluent autonomy is selective." (callback to Ch10) / "The store does not literally build itself." — voice and callbacks — risk: **low**
- **R11-18** "This chapter develops the idea into a design for a store." — replaced by an AUTHOR comment — risk: **low**
- **R11-19** "That is a very different way to decide what to build next." — risk: **low**
- **R11-20** Restatements skipped: about 8 ("The machinery can become extremely sophisticated.", "That last condition matters.", "The problems have to be bounded enough to attack.", "The library is heterogeneous…", "Increase CTR… Improve conversion… Raise engagement…" list, "becomes replayable", "not hypotheses, not production truth", "Is the problem real? How large is it?…" question list folded).


## Chapter 12: After Capacity


- **R12-1** "There is more to a person than the few abilities a career had room for. There may be more to our common life than the arrangements we could previously afford to build." / "I would like us to find out how much more." — the book's closing lines before the Prophecy hand-off — risk: **high**
- **R12-2** "Dantzig's afternoon makes me want access to a mind that can help me see further. Ostrom makes me want to find out what people could construct together if they had that help." — closes the chapter's two framing stories (Dantzig opening, Ostrom section) — risk: **high**
- **R12-3** "This is what I mean by the ideology vortex: inherited belief, reason, criticism, representation and power keep pulling us around the same disputes. The argument changes while the practical dependence survives." plus the heading "The Ideology Vortex" (→ "The Answer to Derrida") and "An eloquent machine left talking to itself could keep us in the vortex indefinitely, with better illustrations." and "the turn out of the vortex" — a named concept that mirrored Ch2's "Algorithm Vortex". That is a deliberate echo, and it is now gone along with a memorable line — risk: **high**
- **R12-4** "Gradient descent did not defeat ambiguity. It made ambiguity computationally useful. The language carrying our disagreements can also help us construct things through which we learn something new." — a memorable line and the step that brings LLMs back into the argument — risk: **high**
- **R12-5** "A young researcher is choosing a question. She has an interest of her own, but she also needs funding and eventually a job. She studies the work that gets published and the people who get hired. … If she follows that path and succeeds, her career joins the evidence the next applicant studies." — the concrete example behind the imitation-loop argument. Without it, "Then the signs acquire a budget" is abstract — risk: **high**
- **R12-6** "Chapter 9 followed the job to where I think it goes. The applied scientists who mattered never only trained models; they told an organization what had become possible, why, and what it would mean for the business. That is owning the frontier, and cheap models put more of the frontier within reach of people who will never hire an applied scientist at all." — a callback to Ch9's "Owning the Frontier" and the answer to "what the city was for". The river image now has no follow-up — risk: **high**
- **R12-7** "Double Descent Life is the wager that…" — the explanation of the chapter subtitle "A Glimpse of Double Descent Life". The term is now never explained in the body — risk: **med/high**
- **R12-8** "Now imagine being able to assemble serious intellectual help around a problem of your own: the research, the models, the alternative arrangements, the software to make one work." — the bridge from Ostrom to the book's tool thesis — risk: **med**
- **R12-9** "Room for a small community to construct things around its actual needs, and for someone inside it to disagree. Room to try the strange art nobody would have funded." — two of the "Room to…" litany items — risk: **med**
- **R12-10** "Capacity over power is an ethical direction, not a forecast about stronger models." — a clarification of the motto; the "not a forecast" half is lost — risk: **med**
- **R12-11** "That is Chapter 7's constitutional surface at the scale of a society" — a callback to Ch7 (07:172), now "Think of it as a constitution written for a society" — risk: **low/med**
- **R12-12** "…which Chapter 1 warned against before we had built anything worth handing over." — a callback to Ch1 — risk: **low/med**
- **R12-13** "…would undo most of the civilization Chapter 5 was trying to explain." — a callback to Ch5 — risk: **low/med**
- **R12-14** "The efforts reported in Chapter 6 came from…" — a callback (the facts are kept) — risk: **low**
- **R12-15** "That is not a competence I am reserving for us because machines cannot yet do it" — an argument step heading off an objection; now "I would still want the seat" — risk: **low/med**
- **R12-16** "Its reason to exist is the investigation, not the market." — risk: **low/med**
- **R12-17** "We want security and novelty, belonging and freedom, status and peace." — risk: **low**
- **R12-18** "Political movements offer belonging and explanations." / "Careers and budgets accumulate around these representations until altering them threatens something quite real." — risk: **low/med**
- **R12-19** "Tradition gives someone a place in a history; science gives her ways to investigate; criticism helps her notice what both have excluded." — the characterization of each commitment — risk: **med**
- **R12-20** "That is politics." / "and not only by the people who own the laboratories" (now "including by people who do not own a laboratory", a shift in emphasis) — risk: **low**
- **R12-21** "Cheap software removed the vendor's veto." (second occurrence) — a duplicate; the line survives at 12:149 — risk: **low** (fine to cut)
- **R12-22** "They do not restore the old economics by decree." / "bespoke" / "The applied scientist at the beginning of this chapter" — risk: **low**
- **R12-23** Restatements skipped: 3.

## Chapter 13


- **R13-1** [C13-1] "The longing." — the named emotion behind the Architect's mask; the scene's closing beat before the section break — risk: med
- **R13-2** [C13-2] "*Devesh wins.*" — Devesh's inner gloat; first of two italic punch lines, a rhythm beat before "*The house always wins.*" — risk: low
- **R13-3** [C13-4] "He made her feel complete in a way she couldn’t compile." — a code-pun joke ("couldn’t compile") and the line saying Norman completes her — risk: med
- **R13-4** [C13-5] ", when she still thought he was just a funny octopus who sold meat." — tender memory of a younger Claudit; implies he wore the octopus disguise for her whole life; an octopus callback (the register's octopus seed sits on L65, not here, and is intact) — risk: high

Changed without loss: C13-3 (L15 em-dash to colon, L79 em-dash to comma), C13-6 (L5 "Simulation" to "simulation", 2 lowercase vs 1 capitalised).
Pure restatements skipped: 0.

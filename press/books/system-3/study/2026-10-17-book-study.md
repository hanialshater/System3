# Book study for the Chapter 11 rewrite

owner: head-of-book-system-3 (Theodora)
date: 2026-10-17
commission: `press/decisions/2026-10-17-founder-store-chapter-rewrite.md` (founder: "ReWrite the store chapter around system 3 company, use the press team, first the team need to study the book and the company then write the chapter")
scope: **the book only.** Other press roles are studying System 3 Company in parallel. Nothing here is a claim about the company beyond its own `README.md` and `CLAUDE.md`, which I read for orientation only. Where this study says a book concept "could pay off" in the company, that is a question for the company study to answer from company records, not a finding.
status: study record. No manuscript file was changed.

Citations are `file:line` against `chapters/` as of 17 October 2026 (`cat -n` numbering), unless another path is given.

---

## 1. The argument and where Chapter 11 sits

### 1.1 The argument in brief

The working spine (`resources/editorial/working-spine.md`) states the book's question as:

> "How can bounded, fallible minds produce knowledge and action that remain answerable to a world none of them understands alone?"

and its one-sentence version:

> "give AI autonomy and control moves up to the conditions; the architecture that emerges from repairing autonomy's failures turns out to be science; then the questions are how to keep it answerable, whose purposes and authority it serves, and what its capacity is for."

Theme: "the architecture of autonomy is emergent. Complexity over engineering, emergence over design, capacity over power." Centre: "the architecture that emerges from repairing autonomy's failures is science." End: "what that capacity could mean for humans; a hoped-for future followed by an alternative ending that complicates it through desire, dependence and power."

The reveal page states the claim directly (`reveal-we-call-it-science.md:22`): "My claim is that, as we build autonomous AI, we keep rediscovering science as its architecture." The afterword restates it and adds three theses (`afterword-what-this-book-proposes.md:15, 25, 35`): cheap minds that are wrong together; checking without understanding; building past the critique.

### 1.2 The arc, as the spine defines it

| Section | Chapters | Question (spine) | What actually happens |
|---|---|---|---|
| Preface | — | The frame; plants the riddle | Leibniz, the cathedral while "Your coffee is still too hot." (`00-preface.md:19`); "we have built it before … at least one loose cable" (`:31`) |
| Part I, Emergence | 1–3 | What happens when the machine owns the search? | Ch 1 the bet; Ch 2 circle packing and the coffee test; Ch 3 educational demos, Deep Mode, "A Cathedral on a Shopping Cart" |
| Part II, Institutions | 4–5 | How do fallible knowers earn trust? | Ch 4 trust chains and System 3; Ch 5 sixteen Claudes, five thousand years of institutions |
| Reveal | — | — | "We call it science." |
| Part III, Science Turns Inward | 6–8 | What happens when the institution becomes executable? | Ch 6 pattern language (the grocery company); Ch 7 recursive self-improvement (an illustrative store's research agent); Ch 8 scalable oversight |
| Interlude | — | The failure that separates science from an apparatus of authority | Lysenko; two routes by which objections lose consequence |
| Part IV, Human Purposes | 9–10 | What can inquiry discover about purposes; how can assistance preserve agency? | Ch 9 the desire layer; Ch 10 fluent autonomy, built on the editing of this book |
| **Part V, What the Capacity Is For** | **11–12** | **"What is the capacity for? The ending I want."** | Ch 11 the store; Ch 12 after capacity (Dantzig, Ostrom, who owns the laboratory) |
| Alternative ending | 13 | Fictional counterweight to Ch 12 | The fable (protected) |
| Scaffolds | — | Last word | "We built scaffolds for AI because they couldn't do it alone. / We built scaffolds for ourselves for the same reason." (`14-scaffolds.md:8-9`) |

The 1 October evaluation summarises the late arc as: structure "should assemble around intention (Ch 10), and the design gets applied (Ch 11) and given a politics (Ch 12)" (`resources/evaluations/2026-10-01-full-manuscript-evaluation.md:50-51`). That is the job Chapter 11 has held: **the one place where the whole architecture is applied to something the author built.**

### 1.3 The Part V page, quoted

`part-5-what-the-capacity-is-for.md:16-19`:

> *A philosophy of emergence should be willing to lose an A/B test.*\
> *Construct knowingly. Build anyway.*
>
> — The Zen of System 3

Note that the first epigraph line **comes from the current Chapter 11** (`11-the-store-that-builds-itself.md:205`). Part pages "carry an epigraph from *The Zen of System 3*. They turn toward the next part; they do not recap the last one" (working spine). Part V has no prose question under its epigraph (Parts II and III do).

### 1.4 What the neighbours need Chapter 11 to do

**Chapter 10 hands off to it.** Ch 10 ends:

> "An editing experiment has one advantage: I am there to say the result is wrong. A customer who gets a bad page files no correction. She leaves.
>
> I spent years building systems that decide what to show her." (`10-fluent-autonomy.md:141-143`)

So Ch 11 currently opens by answering that: the author, his years in ranking, a prototype. Ch 10 also defers two debts to the end of the book: ownership ("The architecture can make ownership visible … It cannot make ownership legitimate, and I come back to it near the end of the book", `10:135`) and the circularity objection ("Then there is the chance that I found what I was looking for. I had read Popper before I read the traces", `10:133`). Ch 10 also says what the book has *not* shown: "None of this shows the whole composition works. I have shown pieces" (`10:139`).

**Chapter 12 builds on it.** Ch 12 refers back to it by name: "The compiler has to compile. Chapter 11's store that builds itself still needs its business experiment: an experience can convince the experts and the model and still fail the customer." (`12-after-capacity.md:79`). Ch 12's politics ("who writes the objective, who can see it, and who can change it when it hurts them", `12:143`) picks up Ch 11's closing: "Its politics live in Surface Value, written down where someone inside the company can argue with it. Mei cannot, yet. Until she can, her interest is something the owner chooses to write in, not something she can enforce." (`11:237`). Ch 12 then generalises the store's owner into "Who Owns the Laboratory" (`12:171-185`) and ends with "That is the work I want to do: put the machinery this book has described within reach of people who have something they want to try" (`12:239`), after admitting "I have not run that weekend" (`12:235`).

**The alternative ending and Chapter 13.** The spine: Ch 13 is "a fictional counterweight to Chapter 12's hoped-for future". Ch 11 does not feed the fable directly, but see §5: a chapter about a founder watching a company of agents on screens sits very close to the fable's Architect ("screens covering every wall, monitoring every timeline", `13:23`; "Behind it: forty monitors. Every timeline.", `13:71`). The rewrite must not explain that payoff.

**Scaffolds page and afterword.** The afterword lists the author's own evidence as "Small: one bounded problem, teaching demos judged by simulated learners, one ten-task comparison, one prototype" (`afterword:67`), and insists "Resemblance to a scientific institution establishes nothing by itself. Each proposal should beat a simpler arrangement on the same model and budget, or be dropped." (`afterword:56`).

**So the job.** Chapter 11 has to (a) be the chapter where the author's own built thing carries the architecture, after nine chapters of others' systems and illustrative cases; (b) show the architecture can lose (the Part V epigraph); (c) leave an ownership-and-objective question for Ch 12 to take to the scale of a community; (d) be honest about evidence in the same register as Ch 4's epistemic-swe and Ch 2's fence ("That sentence needs a fence around it.", `02:211`). A company of agents built on the book's architecture can do all four, and does (b) and (d) better than the store, because the book's own test protocols could in principle run there. It also raises the circularity objection more sharply than the store did (§4.5).

---

## 2. Concepts the book has built by Chapter 11

Each row: exact name, where defined, strongest line. The last column says what a chapter about a running company of agents could pay off. **These are candidate payoffs; the company study must say whether the company actually does each thing.** The company's own `CLAUDE.md` and `README.md` already use several of these names (quoted where they do).

### 2.1 Part I

| Concept (exact name) | Defined | Strongest line | Possible payoff in the company |
|---|---|---|---|
| **Complexity over engineering / Emergence over design / Capacity over power** | `00-preface.md:23`; `01:28`, `01:46`, `01:102` | "I would choose **capacity over power**: what people become able to do matters more to me than how many people one person becomes able to command." (`01:102`) | A one-founder company is a direct test of "capacity over power". Ch 1 also says: "A question might deserve an investigation even if it will never deserve a company." (`01:94`), which a chapter about the author's company can turn on itself. |
| Control moves upward | `01:30` | "instead of choosing every move, we shape more of the conditions under which moves are made" | The founder shapes conditions (roles, gates, constitution) rather than lessons. |
| Confident wrong solutions / the jacket | `01:80` | "Soon the mistake has documentation and several colleagues who can explain why it makes sense. Nobody needed to lie." | The planted-false-diagnosis question (below). |
| Ten agents sharing one assumption | `01:60` | "Ten agents sharing one assumption are not a search party; they are a conga line, walking very confidently into the same lake." | "Copies of one model" limit. |
| **The Coffee Test** (confirmed seed) | `02:173-189` | "That became the autonomy test I actually cared about. I already knew AI could help me solve the problem … I wanted to know whether I could leave." (`02:181`) | Can the founder leave the company? What stays behind (the evaluator)? |
| **Immutable Harness** | `02:187` | "Telling the agent not to edit a file states the rule; it does not make the file immutable." | The company's protected paths enforced by hook and CI (`CLAUDE.md`: "A hook blocks edits, and CI fails unpushed workarounds") are exactly the difference between instruction and enforcement. |
| The Contract (four rules) | `02:223-235` | "the thing that says whether it worked has to stay harder to change than the thing being optimized" (`02:227`); "never write solution code yourself" (`02:229`); "Cross-pollinate, then prune" (`02:233`); "discovery before polish" (`02:235`) | Founder rules about not doing the work himself. |
| **Algorithm Vortex** | `02:215` | "Who was inventing the next move? For the first time in the experiment, not reliably me." (`02:221`) | — |
| **zero framework** | `02:239-243` | "So yes, zero framework: Bash is enough, with the asterisk that Bash contains roughly half a century of civilization." | The company runs on Claude Code subagents, files and a CLI: a test of how little framework an organisation needs. |
| The five layers of AI coding: Layer 0 Model, 1 Agent, 2 Application, **3 Deep Mode**, **4 Desire** | `03:83-97`; table repeated `04:137-144` | Deep Mode's question: "**Given everything we have learned so far, what should we try next?**" (`03:105`); the loop "**state of inquiry → choose a move → act → observe → update the state of inquiry**" (`03:301`) | The company's operating loop (`/run`) is a candidate Deep Mode at organisational scale. The 1 Oct evaluation noted "Deep Mode is named as Layer 3 and then barely mentioned after Ch 4" (`2026-10-01…:430-432`); this chapter could close that frame. |
| Borrow a mind (Theory of Mind) | `03:207-233` | "I use borrowed minds the way I would use a sharp colleague's guess about users: as a source of criticisms and hypotheses worth checking with the people themselves." (`03:233`) | Simulated learners in lesson review. |
| **Independent evaluators** | `03:235-279` | "The beginner should use the artifact before reading the builder's explanation." (`03:259`); "The first communicates a problem; the second communicates the test." (`03:269`) | Company rule: "**Evaluators see the artifact before the account**: `npm run walkthrough -- <slug>` first, and builder notes only after their findings are written." (company `CLAUDE.md`) |
| The browser judge | `03:273-279` | "I used to call the browser ground truth, which was too generous." (`03:275`); "**The student has not yet been asked.**" (`03:279`) | Company's "computer-use QA". The 1 Oct evaluation lists "The Ch 3 educational demos never got their human learners" as a dropped thread (`2026-10-01…:426-428`). The company makes the same kind of artifact (interactive lessons). If it has no real learners yet, the chapter must say so; if it has some, this is the book's biggest unpaid debt and the chapter can pay it. |
| A Cathedral on a Shopping Cart | `03:325-337` | "You can build a beautiful chain of reasoning on one stupid assumption near the bottom, like a cathedral built on a shopping cart." | Claims in lessons resting on a bad source. |
| Strategic constraints ("No bars") | `03:137-143` | "Require the learner to predict before anything moves. Make the demo work on a phone with room for only one representation." (`03:141`) | Company README: "Sixty seconds. One idea. Guess first." and "sized for a phone". Ch 3 proposed as a constraint what the company made its product standard. Verify from company records whether that lineage is real; do not assert it. |

### 2.2 Part II

| Concept | Defined | Strongest line | Possible payoff |
|---|---|---|---|
| Epistemologically flat knowledge | `04:61` | "The conclusion survives training, and much of what earned it trust is lost along the way." | — |
| "The model got the library without the childhood." | `04:107` | (itself) | — |
| **System 3** (System 1 / System 2 / System 3; Gut, Head, Hand) | `04:129`, `04:133` | "If System 1 proposes and System 2 deliberates, System 3 checks." (`04:129`); table row "System 3, across all of them \| What are we entitled to treat as known?" (`04:144`) | The company is named after it. |
| **trust chain** | `04:178` | "a record of how far a claim sits from the evidence supporting it, what transformations happened along the way, and which links we have chosen to trust. It doesn't guarantee that the claim is true." | Company rule: "**Every factual sentence a learner sees is a claim** in that lesson's `meta.json`, with an address, support and source. Builders never mark their own claims verified." |
| Skills; "a hallucination with better retention" | `04:180-182` | "A terrible heuristic in a skill file is simply a hallucination with better retention." | Company `.claude/agents/`, skills, role files. |
| Lived authority on trust | `04:196-198` | "I spent eight years building systems that rank human testimony … System 3 isn't philosophy to me. It's Tuesday." | Voice model for the founder scenes. |
| epistemic-swe (the honest small experiment) | `04:200-235` | "If anything, the scaffold seemed to produce discipline before it produced capability. That wasn't my hypothesis, which is why I learned more from it." (`04:235`) | The reporting model: n stated, result against the author, alternative explanations listed. The 1 Oct evaluation calls this "the model for how the rest should be reported" (`2026-10-01…:131`). |
| **Creative distrust** | `04:277-289`; returned `10:95-113` | "understanding a trust chain well enough to know where you are breaking it and why" (`04:283`) | — |
| **Society of agents** | `05` throughout; title | "Nobody designed that society in advance; it grew out of repairs." (`05:8`); "The organization was the bug." (`05:28`) | The company is a society of agents. |
| Progress files | `05:18` | "the prompt told every agent to maintain READMEs and progress files and to update them often, because the next worker would arrive knowing nothing." | Company `CLAUDE.md`: "**The disk is the memory**: you will not remember this session, and the next worker arrives knowing nothing except what is in this repository." Near-quotation of Ch 5. |
| Popper's **World 3** | `05:48-52` | "The compiler project is a small World 3 with a Git remote." (`05:48`) | — |
| "Reality has a commit hook." | `05:54` | "The hook can be wrong too, but the agent's account of its own success no longer gets the last word." | Company gates/CI. |
| Standards; **mechanism** | `05:120-126` | "a mechanism is an attempt to make a desirable behavior survive the person who first cared about it" (`05:122`); "When something goes wrong you can tell everyone to be more careful, which is emotionally satisfying and institutionally almost worthless" (`05:124`) | The VP's record says one company incident's fix "targets the mechanism" (`press/decisions/2026-10-16-vp-books-company-case-study.md`, candidate 1). Company study to verify. |
| Specialisation | `05:130-140` | "The society gains knowledge by distributing ignorance" (`05:140`) | Narrow roles. |
| Elaine Bromiley | `05:144-158` | "Their authority has to follow what they know, and their observations need a way to interrupt someone else's plan." (`05:158`) | Escalation rules. |
| **One witness** | `05:172-180` | "That is what a second witness is for: she has to be capable of being wrong differently." (`05:172`); "When five agents merely repeat one source, we have one witness wearing different coats." (`05:178`) | See Ch 8 below; the company's central honest limit. |
| Allocation | `05:254-258` | "Compute allocation is epistemic policy." (`05:254`); "A critic whose objections never change what gets investigated is doing quality-assurance theater." (`05:258`) | The company's dispatch caps; the founder's org/dispatch rule (VP candidate 6). |
| **The planted-false-diagnosis test** | `05:305`; protocol fixed in `appendix-note-on-evidence.md:24-37` | "Put a bad diagnosis in a progress file. Compare a system that merely remembers it with one that can trace it to the failed test it misdescribes. Does the mistake survive into the next worker's plan? If these changes make no difference, the architecture owes us an explanation. The resemblance alone has proved nothing." (`05:305`) | The company is the obvious host. The VP record (`2026-10-16`, scope) says running it is **not** that commission and that incidents 2 and 3 "are anecdotes in the same area, **not** results of that test". The chapter must not present anecdotes as this test. |
| Closing | `05:309-311` | "I thought I was designing a society of agents. / Humanity had already spent centuries building a society of fallible knowers." | — |

### 2.3 Part III

| Concept | Defined | Strongest line | Possible payoff |
|---|---|---|---|
| **Pattern language** (Alexander; asterisks as confidence) | `06:88-108` | "A pattern language puts builders' knowledge, the kind Sam carries, into connected proposals whose context and reasons are open to question." (`06:106`) | Role files and skills as patterns. |
| **high-functioning bullshit** | `06:120` | "an idea, explanation or practice that still carries the signals of expertise after losing the live connection to the assumptions that made it true" | Already reused in Ch 11 ("high-functioning bullshit with a dashboard", `11:177`). |
| Pattern vs feather | `06:126-128` | "Strip those parts away and the name keeps its authority while losing every handle by which it can lose an argument. / That is the difference between a pattern and a feather." | — |
| **give-the-claim-an-address** | `06:241-269`; list `06:408` | "\*\* Therefore: store the claim with what it rests on, so that a correction has somewhere to go." (`06:269`) | Company claims "with an address, support and source". |
| **objection-travels** | `06:321-369`; list `06:411` | "*noted.*" (`06:331`); "We have successfully parallelized the experience of being ignored." (`06:341`); "An open_questions field that no decision ever consults is a decorative conscience." (`06:367`); "\* Therefore: if the organization proceeds with an objection unresolved, the objection travels with the decision, and the decision-maker owns that choice in writing." (`06:369`) | Company `CLAUDE.md`: "**Objections travel with decisions.** Never answer one with 'noted'." The press's own decision records use the same table, including the founder's override of the VP (`press/decisions/2026-10-17-founder-store-chapter-rewrite.md`, Objections). |
| change-the-inheritance; "Session turnover is not a funeral." | `06:381-389` | "Therefore: change what the next worker inherits, and give it standing to challenge the inheritance." | Agent sessions end every day in the company. |
| "ask Sam" → a file behind the name | `06:70`, `06:446-448` | "Further down the runbook, a newer engineer has written *ask Ines*. / This time there is a file behind the name." | The press's working agreement quotes it: "'Ask X' is a dead end; link the file." (`press/roles/head-of-book-system-3.md`, Working agreement). |
| The procedure decides what gets checked | `06:416-426` | "A procedure that cannot authorize an investigation outside its own method has made the method unfalsifiable." (`06:418`) | Company gates. |
| **Recursive self-improvement**, four levels | `07:47-58` | "Self-reference is not self-improvement." (`07:17`, also in the Zen); "A change to the agents' own process counts as recursive improvement only if it leaves them better at finding and testing further improvements, under stated conditions, with evidence they cannot rewrite or dismiss on their own." (`07:47`) | If the company edits its own roles/org, which level is it? Almost certainly level 2, not 3; the chapter must not overclaim. |
| Correction of Error (COE) | `07:25-29` | "Amazon did not ask anyone to be more careful." (`07:27`) | Company has a `/coe` slash command and COE records (`CLAUDE.md`; VP record candidate 1). |
| The teacher moves into the walls | `07:60-66` | "The reinforcement learner looks autonomous because the teacher moved into the walls." (`07:66`) | Who wrote the company's gates. |
| **The Complexity Wall** | `07:122-134` | "self-improvement stalls first where the system adds structure faster than it can verify or simplify it" (`07:134`); the selection record "has no column for what it removes" (`07:128`) | A company that adds a gate per incident. |
| Before the returns arrive | `07:136-146` | "An institution can make proposals nearly free and still be paced by the rate at which customers send back shoes." (`07:142`) | Lessons can be produced faster than learners can show whether they teach. |
| The student finds the gradebook | `07:148-164` | "`return True`" (`07:154`); "Someone has to approve the replacement, and it cannot be the student." (`07:164`) | Builders "never mark their own claims verified". |
| **constitutional surface** | `07:166-204`, definition `07:190` | "The closer something comes to defining what counts as improvement, the harder it should be for the current improver to change it alone." (`07:190`); "We have reinvented constitutional government because the AI wanted a better benchmark score." (`07:198`) | Company: "Protected paths (`company/constitution/protected-paths.txt`) change only by ratified amendment." README: "a constitution that keeps the judged from editing the judge." Zen: "The judged do not amend the judge alone." (`appendix-zen-of-system-3.md:40`) |
| The Teacher's Last Job | `07:206-210` | "Somebody still has to read some of them." | — |
| **Scalable oversight**: a new kind of employee | `08:17-29` | "The new employee also comes in copies, and ten copies of one model can share one blind spot where ten human reports would have ten." (`08:25`); "can it be wrong differently?" (`08:29`) | The company is staffed by copies. |
| ExploitGym's back channel | `08:5-15` | "I have been hoping agents would rediscover institutions. I had not pictured the first one they built on their own as a back channel." (`08:15`) | Contrast: the company's institutions were designed from the book, not discovered. |
| **"copies of one model are one witness"** (exact phrase) | `appendix-note-on-evidence.md:26`; argued `05:178`, `08:25`, `08:83-85`; Zen "Five judges sharing one source are one witness." (`zen:29`, Part II page) | "Five models agreeing can be one mistake with excellent parallelism." (`08:83`) | **Mandatory honest limit** (VP record candidate 7; founder decision objection 2: "it may not present agent-on-agent catches as independent witnesses"). |
| Keep the Budget Out of Reach (AI control) | `08:87-89` | "You sample, and you keep the payroll budget out of reach." (`08:19`) | Company: "Deploys need the founder's approval, every time." |
| Make It Ask | `08:91-101` | "Doubt needs someone to call, and the answer has to be able to stop the work." (`08:101`) | — |
| The Top Loop | `08:115-121` | "Letting that replacement certify the agent's own work is a different decision, and it belongs to the loop that changes the loops." (`08:119`) | The founder's place. |
| Interlude: two routes | `interlude:11-21` | "You cannot tell science from an efficient apparatus of authority by reading its org chart; you find out when somebody objects." (`:11`); "The second is that the owner prevents the challenge." (`:17`); "In 1948 the journals kept coming out." (`:21`) | The founder is the owner. The chapter has to show at least one place where an objection could change the founder's decision, or admit there is none. |

### 2.4 Part IV

| Concept | Defined | Strongest line | Possible payoff |
|---|---|---|---|
| **The desire layer** (Layer 4) | `03:95`; `09` | "Asking the question helps create the answer." (`09:9`); "What remains is deciding what the trying is for." (`09:15`) | What is the company for? The founder's stated purpose (VP record: "the company exists to test the book's ideas") vs its product purpose (teaching). |
| Owning the frontier | `09:33-41` | "Training and evaluation were the expensive part of the job, and expensive is easy to mistake for essential." (`09:39`) | — |
| Preference shaping | `09:69-81` | "The cheapest way to satisfy a person is to change what they want." (`09:69`); "The second is alignment by editing the human. / Very efficient. Slightly evil." (`09:79-81`) | A **vertical feed** of lessons is the form Chs 6, 9 and 12 warn about ("a feed ranked for engagement is the vortex with a reward function", `12:55`; "fourteen hours of personalized short video", `12:219`). The chapter must say what the feed optimises. |
| Whose side the assistant is on | `09:77` | "What she needs to know first is whose side the assistant is on, and whether it told her." | — |
| The annoying tutor | `09:97`, `09:101` | "The tutor that worked was, by design, the more annoying one." (`09:97`) | Company: "Each card asks you to commit to a prediction" and "Ideas come back days later as one-question revisits" (README). Ebbinghaus spacing and testing (`09:95`) and Buçinca's forcing functions (`09:101`) are what "Guess first" and revisits implement. Verify lineage from company records. |
| Connector | `09:113` | "Facing a transformative choice, the most useful thing it can find is a person who made it, and a way to talk to them." | — |
| Limit of System 3 | `09:121` | "System 3 can investigate what a choice would do. It cannot tell you whose purposes should win." | — |
| **Fluent autonomy** | `10:39` (bold, the definition) | "**Fluent autonomy**, as I mean it, is a system that forms the institution a request needs, behind an interface small enough to talk to, and takes it down when the work is done." | The founder's one-sentence commission of this rewrite is itself an instance of the interface. Whether the company "takes it down" (or its bureaucracy "never comes down", `10:49`) is a test the company study can answer. |
| Scaffolding → distillation | `10:15-41` | "The refusal should remain mine. Remembering why I refused should not depend on my being there to refuse again." (`10:27`) | — |
| **The Second Coffee Test** (confirmed seed) | `10:53-63` | "*Can I stop repeating myself?*" (`10:59`); "Here the unit is closer to the sigh." (`10:61`) | Count repeated founder corrections in company records. A real number here would also answer the 1 Oct evaluation's complaint that Ch 10's test "needs the number" (`2026-10-01…:330`). |
| The weights will eat it | `10:65-75` | "What is worth defending is a check the solver did not choose." (`10:73`) | — |
| The trapdoor | `10:77-93` | "That is opacity with good typography." (`10:89`) | — |
| Coupled to a person | `10:115-123` | "A system coupled to me judges itself partly by what I can do without it afterward." (`10:123`) | — |
| Where This Could Be Wrong | `10:125-139` | "The fairer test is whether the arrangements improve the work. The one I designed on purpose, my epistemic agent, solved fewer problems than the baseline." (`10:133`); "The architecture can make ownership visible … It cannot make ownership legitimate" (`10:135`) | The company is designed on purpose from the book; Ch 10's own objection applies at full strength. |

### 2.5 After Chapter 11 (what Ch 11 must leave room for)

| Concept | Where | Line |
|---|---|---|
| The second descent; ideology vortex | `12:19-61` | "The capacity that matters is the capacity to build an attempt and watch it fail." (`12:33`) |
| Construct knowingly | `12:85` | "We can construct them knowingly." (source of the Part V epigraph's second line and the Zen's "Construct knowingly. Build anyway.") |
| Who Owns the Laboratory | `12:171-185` | "a weekend of borrowed agents belongs, in the end, to whoever holds the switch" (`12:177`) |
| The understanding condition | `12:169` | "Someone at the table has to understand enough to take part in the selection." |

The company runs on rented models and a free hosting plan (`CLAUDE.md`: "Vercel's free plan allows 100 deployments a day"). Ch 12's switch argument applies to it directly. Ch 11 can set that up without spending it.

---

## 3. Dependencies on the current store chapter

What breaks if Chapter 11 stops being about the store. Each item needs a decision in the brief; most need a change in another file, which itself needs the founder's acceptance (Chs 6–12 are works in progress; the appendices and afterword are manuscript).

### 3.1 Manuscript

| # | Where | What it says | What breaks | Fix needed |
|---|---|---|---|---|
| D1 | `part-5-what-the-capacity-is-for.md:16` | Epigraph "*A philosophy of emergence should be willing to lose an A/B test.*" | Its source line (`11:205`) disappears; the 2 Oct cuts-revert list treats an unsourced Zen line as **high** risk (`resources/evaluations/2026-10-02-cuts-revert-list.md:152, 226`). | Keep the line in the new Ch 11 (it fits a company that must beat simpler arrangements), or change epigraph and Zen with the founder. |
| D2 | `appendix-zen-of-system-3.md:52` | Same line in the Zen | As D1. | As D1. |
| D3 | `10-fluent-autonomy.md:141-143` | "A customer who gets a bad page files no correction. She leaves. / I spent years building systems that decide what to show her." | The hand-off points at a store that no longer comes. | Either Ch 11 opens by turning from that customer to the company (the author's ranking career can still be the bridge), or Ch 10's last lines change (founder acceptance). Do not leave a dangling customer. |
| D4 | `12-after-capacity.md:79` | "Chapter 11's store that builds itself still needs its business experiment: an experience can convince the experts and the model and still fail the customer." | False reference. The copyedit log records this sentence was already rewritten once to point at the prospective experiment (`2026-09-30-copyedit-log.md:132`). | Rewrite to the company's equivalent unrun test (lessons convincing reviewers and the model and still failing learners), or drop. |
| D5 | `11:237` → Ch 12 politics (`12:143`, `12:171-185`) | "Mei cannot, yet. Until she can, her interest is something the owner chooses to write in" | Ch 12's ownership argument loses its concrete precursor. | Transplant: whose interest the company's objective writes in (learners'), who can argue with it, and who owns the switch. |
| D6 | `afterword-what-this-book-proposes.md:67` | "My own experiments \| Small: one bounded problem, teaching demos judged by simulated learners, one ten-task comparison, one prototype" | "one prototype" no longer has a chapter, unless the store survives in Ch 11 as origin. | Update the row (e.g. "a company of agents run for N weeks, observed through its records"), category as the fact-checker sets it. |
| D7 | `afterword:63` | Design proposals "partly demonstrated in others' systems" (Fermat, Colosseum, AHE) | If the company implements claim addresses, objection-travels and a constitutional surface, the afterword could cite the author's own system, at the evidence level the record supports. | Optional; founder decision. |
| D8 | `afterword:21`; `appendix-note-on-evidence.md:24-37` | The planted-false-belief test, "one experiment specified in advance and not yet run" (`afterword:64`) | Nothing breaks, but if Ch 11 describes the company catching planted bugs or a wrong diagnosis, a reader will take it for this test. | Ch 11 and the Note must say explicitly that company incidents are not this test (VP record). If the founder later runs it in the company, both the Note and the afterword change. |
| D9 | `appendix-note-on-evidence.md:20` | "\| 11. The Store That Builds Itself \| My prototype store, its customers and a proposed business experiment \| Prototyped; the business experiment has not run \|" | Row wrong in all three columns. | See §7.4. |
| D10 | `appendix-note-on-evidence.md:5` | "The stories of companies, teams and people come from my experience. Names, companies and details have been changed, and some are composites or embellished. I do not say which is which" | Conflicts with the company material's **no-composite** rule (VP record point 4). | See §7.4. |
| D11 | `appendix-references.md:509-515` | "## Chapter 11 — The Store That Builds Itself", `ref-11-slate`, `ref-11-store-pearl` | The build **fails** on uncited numbered references (`book-design/curated/manuscript.py:31-33`, `validate_references`: "Uncited numbered references"). | Remove or reuse the entries; rename the section heading if the title changes. |
| D12 | `09-layer-4-desire.md:77` | The trail-shoes shopper ("whether she needs the more expensive trail shoes") | Set up as Mei's pair; the 1 Oct evaluation asked Ch 11 to pick it up "ideally as Mei's own case" (`2026-10-01…:420-422`). Without Mei it stands alone, as the 2 Oct AI-tells report already wanted (`2026-10-02-ai-tells-report.md:377`). | Nothing breaks. Flag for Ch 9's next pass. |
| D13 | `01-why-im-betting-on-ai-agents.md:26`; `12:27` | "A customer becomes a funnel stage. A learning experience becomes a sequence of screens." / "The customer became a funnel stage" | Ch 11's funnel section (`11:41-51`) was the payoff of "funnel stage". | Ch 1's second sentence ("A learning experience becomes a sequence of screens") becomes the better-paid line in a lessons chapter. Nothing breaks. |
| D14 | `07:43` | `<!-- AUTHOR: optional: could the circle-packing run, or a ranking or experiment story, carry some of the store's beats? -->` | Refers to Ch 7's own illustrative store, not Ch 11's. With Ch 11's store gone, Ch 7's store becomes the only store in the book. | None needed; note that readers will no longer link the two. |
| D15 | `07:45-204` (illustrative store, "evaluation standards review board") | Ch 7's constitution example lives in a store | If the company has a real constitution and amendment process, Ch 11 will show a real one after Ch 7's imagined one. Good, provided Ch 11 does not re-explain Ch 7 (cross-chapter stitching tell). | Brief: one decodable callback at most. |
| D16 | `about-the-author.md:21` | "Head of Applied Science at Zalando" | The store chapter quietly drew on the author's day job (fashion e-commerce; "outside Berlin", `11:193`). The company chapter moves away from the employer, which may ease the open clearance item (`resources/REVISIT.md:13`). | Founder to say whether any store material came from Zalando work; if so it stays under the clearance item. |

### 3.2 Book production and side materials

| # | Where | What depends on Ch 11 | What breaks |
|---|---|---|---|
| P1 | `book-design/curated/book-order.json` | Filename `11-the-store-that-builds-itself.md` | Renaming the file breaks the build (`ordered_paths` raises on missing or unlisted files, `manuscript.py:36-45`). Keep the filename, or rename in every file below in the same change. |
| P2 | `book-design/curated/provenance.json` | `"11-the-store-that-builds-itself.md": "Chapter 11: The Store That Builds Itself"` | Stale title. |
| P3 | `book-design/curated/art.json` | Five in-text illustrations anchored to Ch 11 sentences: **a190** after "…The page is smart inside the modules and surprisingly dumb between them." (`11:15`); **a191** after "…we have created a taxonomy department rather than a recommender system. The problems have to be bounded enough to attack." (already stale: second sentence no longer in the text); **a195** after "What it lacks is somebody deciding which of them the page needs…" (`11:83`); **a196** after "Direct customer feedback could help explain what the behavioral measures miss." (`11:97`); **a201** after "I used the deliberately bland term **Surface Value**." (`11:185`) | `resolve_anchor` accepts only a unique exact anchor and "never moves art by guess" (`manuscript.py:74-80`; test `test_editing_anchor_never_moves_art_by_guess`). Removed sentences leave five illustrations unplaced. Art director decision: re-anchor, replace, or retire. |
| P4 | `resources/art-direction/chapter-openers.md:21`; `book-design/curated/print-assets.json:167`; `assets/print/cover-189.png` | Chapter opener `cover-189.png` | The art-direction evaluation said the opener "reads 'personalized fashion store'" and asked for a store "visibly compositional" (`resources/art-direction/evaluations/2026-08-26-full-book-art-direction-evaluation.md:84`, where the store was then numbered Ch 10). A fashion-store opener on a company-of-agents chapter is wrong. New opener brief for the art director. |
| P5 | `appendix-illustrations.md` | Generic ("robots … gradually inhabited by machine intelligence"; "As the book moves … toward human intention and capacity, the images move with it") | Nothing breaks. The art evaluation's arc ("By Chapter 11, the robots should almost disappear", `…art-direction-evaluation.md:243`) sits awkwardly with a chapter about a company *of agents*; art director to judge. |
| P6 | `prompts/notebooklm/chapter-11.md`, `prompts/notebooklm/sources.json`, `prompts/notebooklm/book.md`, `prompts/build_notebooklm.py` | Video brief for the store: "Moments to show: the stuck customer … Mei and the trail shoes … Surface Value … the book biting back"; "Lines to keep word for word: 'A philosophy of emergence should be willing to lose an A/B test.' 'Cold start is a state, not an error.'" | Regenerate after acceptance. (The brief is already stale: "Cold start is a state, not an error." is no longer in the chapter.) |
| P7 | `resources/editorial/check-eggs.sh`; `resources/editorial/easter-egg-register.md:18` | Anchor `11-the-store-that-builds-itself.md` → "And now the camel comes back" | Proposed seed: the check **warns**, does not fail. Register must be updated in the same commit (rule 4). See §5. |
| P8 | `resources/FILE-INVENTORY.md` | Lists the five art files and cover-189 as "Keep" | Update if art is retired. |
| P9 | Evaluation records | 30 Sept readiness evaluation: "Mei, Sami, Lea and 'beat simplification' are protected." (`2026-09-30-chapter-readiness-evaluation.md:41`); 2 Oct cuts-revert list names R11-1…R11-20 store lines at risk (`2026-10-02-cuts-revert-list.md:243-265`) | These are reviewers' protections, not founder acceptances, and the founder has now commissioned a full rewrite. Dropping Mei, Sami and Lea is the head of book's open objection in the decision record ("Open for the founder"). The draft must list what it drops. |

### 3.3 Phrases and motifs that live only in Ch 11

| Phrase / motif | Line | Used elsewhere? |
|---|---|---|
| "The Book Comes Back to Bite Me" (heading) | `11:229` | No other file uses it. The move (the book's argument reappearing in the author's own build) is the chapter's best structural move; see §4. |
| "Replayable" (heading), the trace, logging the losers | `11:131-155` | Not referenced elsewhere. Ch 5 and Ch 6 make the same point about provenance (`05:226`, `06:241-269`). |
| Mei, Sami, Lea, the thirty-second customer | `11:13`, `27`, `85-99`, `101-113`, `117-129` | Only Ch 9's trail-shoe shopper (D12) and the video brief (P6). |
| Prototype | `11:3`, `5`, `185`, `231` | Afterword "one prototype" (D6); Note on Evidence "Prototyped" (D9). |
| Problem fingerprint, recommendation experiences, Coverage and Unmet Demand, Surface Value | `11:47`, `59`, `167`, `185` | art.json a201 anchor only. The company's `status` reports "coverage" (`CLAUDE.md`, start of session). Whether that word descends from the store chapter is a question for the company study or the founder. |
| "the same thing in research, education or the organization doing the building" | `11:239` | Last sentence but one. It reads now like a forecast of the company (education; the organisation doing the building). A rewrite can start where this line ends. |

---

## 4. The current Chapter 11, section by section

Chapter 11 is 4,523 words (`wc -w`), 14 `##` sections, 2 numbered references, 4 bold spans, no em-dashes. Checker: maxim 21%, notXbutY 0.4/1k, cite-chains 0, xref 0.0 (`python3 resources/editorial/check-tells.py 11`), all within the Chapter 4–5 targets. The 30 Sept readiness evaluation scored it 8, "Needs pass", 75 (`2026-09-30-chapter-readiness-evaluation.md:41`). The 1 Oct evaluation called it "Practitioner-grade material" and said "Recruiters and reviewers from industry will read this chapter first", with the weak point "the prototype ambiguity … What the prototype does is never shown" (`2026-10-01…:27-28, 132, 332-347`).

### 4.1 The one author-review comment (verbatim)

`11:7`:

> `<!-- AUTHOR: What did the prototype actually do or show? A screen, a session, a surprise? One moment from the prototype would anchor the chapter. -->`

There is no other `<!-- AUTHOR` comment in the file. It has no recorded acceptance, so under the standing rules it stays in the manuscript until the founder accepts its removal. A rewrite that drops the prototype makes the question moot; the proposal must say so and ask the founder to accept removing it.

### 4.2 Sections

Legend: **L** lived (the founder's own experience, in the first person); **A** argued or designed; **I** illustrative (imagined customers or scenes); **R** reported (cited).

| Section (lines) | What it argues | Best lines (quoted) | Mode |
|---|---|---|---|
| Opening, untitled, subtitle *A Prototype Store* (`1-17`) | After years in ranking the author built a prototype store; two customers see the same modules; the page is "smart inside the modules and surprisingly dumb between them" | "I built a prototype store because the idea would not stay on the page." (`5`); "I have definitely not solved shopping before lunch." (`9`); "The page is smart inside the modules and surprisingly dumb between them." (`15`) | L (`5`, `9`); I (Mei, the 30-second customer, `13`) |
| Stop Recommending for a Moment (`19-39`) | Ask which bounded *problem* is relevant, not which item; problem names are hypotheses that must be testable | "There is a point at which another excellent candidate is not help. It is homework." (`29`); "we have created a taxonomy department rather than a recommender system" (`37`) | A, I |
| People Refuse to Stay in the Funnel (`41-51`) | The funnel compresses mess; a local, multi-hypothesis **problem fingerprint** instead | "somewhere a PowerPoint theme earns its salary" (`43`); "disappear for three days because a child needed dinner" (`45`); "I do not want the system deciding that Hani is metaphysically a `RETURN_HESITANT_PERSON` and carrying that fact around until retirement." (`49`); "turning a useful human abstraction into an ontological claim because we happened to put it in a feature table" (`51`) | A; the funnel/feature-table habit is implicitly L |
| A Library of Ways to Help (`53-63`) | **recommendation experiences**: reusable, configurable units of help; configure before inventing | "The carousel has become the fruit bowl of e-commerce" (`55`); "A library of two hundred overlapping experiences would be a new kind of legacy system with better animation." (`61`); "The learning stopped at the edge of the box." (`63`) | A; `63` is L ("I spent years in machine learning … I helped build systems") |
| Composition Is Not Ranking With a New Hat (`65-83`) | Scores depend on what is already selected: saturation, synergy, position cost; the page is the unit; this resembles the society of agents | "a wonderful module in slot twelve may be a philosophical achievement rather than a product one" (`79`); "a secret forest of `if DE_mobile && campaign_X` rules" (`79`); "the page can feel like a committee where everybody prepared the same presentation" (`81`); "What it lacks is somebody deciding which of them the page needs" (`83`) | A, R (`67`, slate/whole-page optimisation) |
| Mei Does Not Need More Shoes (`85-99`) | Composition for comparison friction; how you would test it | "She is not shown more choice. She is shown a way to close the choice she already has." (`93`); "like a doctor who has one extremely accurate prescription and keeps waiting for every disease to become the disease it treats" (`95`); "the composer has learned something inconvenient about its own necessity" (`99`) | I, A |
| Sami Does Not Need a Click (`101-113`) | A knowledge experience gets no click; the objective decides what survives; claims need substantiation | "If your ecosystem rewards clicks, clickable organisms evolve." (`111`); "And now the camel comes back … The argument about hallucination from earlier in the book has turned into a product requirement." (`113`) | I, A |
| The Honest Cold Start (`115-129`) | Low signal as a normal state, not an exception; do not speak in the dialect of personalisation | "> Picked for you. / Based on what, exactly? Her IP address and our enthusiasm?" (`125-127`); "'Popular this week' can be a good statement when 'we have inferred your soul from one click' is not." (`129`) | I, A |
| Replayable (`131-155`) | Every composition needs a trace, including the losers | "'The model chose it' is not an answer. It is a resignation letter written in passive voice." (`141`); "Logging the loser set does not magically give us causal counterfactuals. Reality is not that generous." (`153`) | A |
| A Theory Losing Contact With Reality (`157-169`) | The library as organisational knowledge; gates for new and old supply; **Coverage** and **Unmet Demand** | "That knowledge can also become a junk drawer with tenure." (`165`); "a heavily used intervention that stops relieving the problem is a theory losing contact with reality" (`169`) | A; "a pair of concepts I particularly like" (`167`) is L |
| Let the LLM Narrate. Do Not Let It Declare Reality. (`171-179`) | LLM narrations of sessions are hypotheses only; correlation vs intervention (Pearl) | "Skip that step and you have high-functioning bullshit with a dashboard." (`177`); "A recommender that only observes is standing on rung one with excellent posture." (`179`) | A, R (Pearl) |
| The Objective Fights Back (`181-195`) | **Surface Value**; every candidate objective fails somewhere; write trade-offs where they can be questioned | "This is where the prototype becomes philosophical against its will." (`185`); "A system that pretends only one of these matters is hiding politics inside a scalar." (`191`); "I do not expect to discover the One True E-commerce Reward Function carved into a mountain somewhere outside Berlin." (`193`); "If merchandising needs a lock, make it a typed constraint. If margin is part of the objective, admit it." (`195`) | L (`183-185`: "the design forced me to name …"), A |
| Deliberately Boring (`197-205`) | The first test: one placement, few problems, existing library, simple composer, authored objective; must beat a static baseline **and simplification** | "an autonomous agent that redesigns fashion retail by Thursday" (`199`); "Maybe the static page was already fine and I should have spent the quarter learning the guitar." (`203`); "A philosophy of emergence should be willing to lose an A/B test. Otherwise it is branding." (`205`) | A (proposed experiment, not run) |
| When the Page Stops Being the Product (`207-227`) | If it works, the library grows, surfaces share a mission; no hard-coded journeys; dynamic only where it earns its cost | "There was never a hard-coded `WEDDING_FUNNEL_V7`." (`219`); "customers occasionally just want to buy socks without participating in an artificial-intelligence research program" (`223`); "Taken literally, the title overstates it. The store learns how to build more of the experience it needs." (`227`) | A, I (wedding outfit) |
| The Book Comes Back to Bite Me (`229-239`) | The redesign grew into a scientific institution inside the product; that does not prove the book; politics live in Surface Value; the same could happen in research, education, the organisation doing the building; uncomfortable for the author's profession | "it had acquired the shape of a scientific institution embedded in the product" (`231`); "That does not prove the book. I designed it with the book's argument in my head, and the test that could embarrass me is still ahead. It may fail in several educational ways." (`233`); "Mei cannot, yet." (`237`); "More of the work moves into the system, including work I once regarded as the reason it needed someone like me. That is an attractive architecture and a less comfortable thing to notice about your own profession." (`239`) | L (`231-233`, `239`), A |

### 4.3 What is lived, what is argued, what is illustrative

- **Lived, in the text:** the author's years in ranking and recommendations (`5`, `63`); that he built a prototype (`5`, `231`); that he has not run the business experiment (`9`); that he named the concepts (`59`, `167`, `183-185`); that he designed the prototype "with the book's argument in my head" (`233`); the unease about his profession (`239`). The location joke "outside Berlin" (`193`) and the author bio (Zalando) place it in his working life. **Not in the text:** what the prototype did. The AUTHOR comment at `7` asks for exactly that, and the 1 Oct evaluation repeats it.
- **Illustrative:** Mei, Sami, Lea, the thirty-second customer, the wedding-outfit journey, the `RETURN_HESITANT_PERSON` joke. An earlier version said so outright ("The customers below are imagined", commit `2476a8e`); the current text dropped that sentence. Today only the Note on Evidence's word "Prototyped" carries the status, which a reader can misread as "the customers are real".
- **Argued or designed:** everything else, including the proposed experiment (`201-205`).
- **Reported:** two citations (slate/whole-page optimisation, `67`; Pearl, `179`).

The video brief carries a warning that matters for the rewrite: "Do not claim measured commercial success or restore the removed internal recommendation case." (`prompts/notebooklm/chapter-11.md`, prompt). An earlier draft carried a real internal case that was removed; the copyedit log records that Ch 12's "apparent report of a completed recommendation experiment" was replaced with the prospective experiment (`2026-09-30-copyedit-log.md:132`). The rewrite must not reintroduce internal employer material.

### 4.4 Recommendation: what must survive, what can move, what can go

**Must survive (in Ch 11 or, by the founder's choice, elsewhere):**

1. **"A philosophy of emergence should be willing to lose an A/B test."** It is the Part V epigraph and a Zen line (D1, D2). In a company chapter it becomes a sharper demand: the company must be willing to lose to a simpler arrangement (one agent; fewer roles; no gates), which is also the afterword's rule (`afterword:56`). Keep the wording exact, or the founder changes the epigraph and the Zen.
2. **The "beat simplification" logic** of Deliberately Boring (`201-205`). Transplanted: what would the company have to beat, on the same model and budget, for its structure to be worth its cost? Protected by the 30 Sept readiness evaluation.
3. **The closing move of "The Book Comes Back to Bite Me"**: the author builds something, it turns into the book's architecture, and he says plainly that this does not prove the book because he built it with the book in his head. For the company this is *more* true (its README says it "is organised around the ideas in" the book), so the circularity objection (Ch 10:133) must be faced in Ch 11 itself, not deferred. This is the chapter's spine.
4. **The politics hand-off to Ch 12** (`237`): whose interest the objective writes in, who can argue with it, and who cannot yet. For the company: learners (and possibly the founder's purpose of testing the book vs the learners' purpose of learning).
5. **The objective argument** ("If your ecosystem rewards clicks, clickable organisms evolve", `111`; "hiding politics inside a scalar", `191`). A vertical feed of lessons sits exactly where Chs 6, 9 and 12 locate the danger; the chapter cannot skip what the feed is for and how that is measured.
6. **"Let the LLM narrate. Do not let it declare reality."** (`171-179`). A company whose workers are LLMs has this problem in every record it writes. The heading is reusable as is.
7. **The camel callback** ("And now the camel comes back", `113`), if it fits. Claims in lessons with "an address, support and source" are the most natural place in the book for it. It is a proposed seed (§5), so the anchor may move, but its job (Ch 4's camel turning into a product requirement) is better served by the company than by the store.
8. **The honest evidence register**: the chapter's own fences (`9`, `97-99`, `153`, `233`). Every company claim needs the same.

**Can move (into a short origin passage, if the founder wants the store kept as lived history):**

- The prototype itself, if the founder supplies what it did. A few hundred words could keep the store as the place the author first saw the book "bite back", and turn on `239` ("the same thing in research, education or the organization doing the building") into the company. This also keeps "one prototype" true in the afterword (D6). The founder decides; the draft must ask, not invent.
- "Replayable" and logging the losers, if company records play that role (the company study will say).
- Coverage / Unmet Demand, only if the company really uses "coverage" in the same sense. Otherwise cut.

**Can go:**

- The funnel section, recommendation-experience library, composition mechanics (saturation, synergy, position cost), the honest cold start, the wedding journey, "When the Page Stops Being the Product".
- Mei, Sami and Lea as running characters. Dropping them is open with the founder (decision record, objection 3); the draft must list them as dropped.
- The two references (D11) unless reused.
- The bold coinages (problem fingerprint, recommendation experiences, Coverage, Unmet Demand, Surface Value). The 2 Oct AI-tells report flagged "Coinage inflation" in this chapter (`2026-10-02-ai-tells-report.md:422`).

**Lines worth reusing if they fit naturally** (the readers praised this register): "'The model chose it' is not an answer. It is a resignation letter written in passive voice."; "That knowledge can also become a junk drawer with tenure."; "Maybe the static page was already fine and I should have spent the quarter learning the guitar."; "I have definitely not solved shopping before lunch." (which echoes Ch 1's "I was hoping to finish before lunch", `01:14`). Do not force them.

### 4.5 Risks specific to a company chapter (from the book's own standards)

- **The circularity objection is stronger.** The store was designed "with the book's argument in my head"; the company is explicitly built from the book. Ch 10 already concedes "Then there is the chance that I found what I was looking for" (`10:133`). Seeing the company behave like the book proves little; only a comparison could (the book's rule, `05:305`, `afterword:56`).
- **One model, many roles.** Every catch in the company is one copy of a model catching another (`08:25`; decision record objection 2; VP record candidate 7). The witness writing the chapter (the press) is the same model again.
- **No learners yet?** If the company has no real learners, Ch 3's "The student has not yet been asked." (`03:279`) still holds and the chapter must say so. If it has some, that is the strongest new evidence in the book.
- **Owner authority.** The founder approves every deploy and can override objections (the founder's override of the VP is on record, `press/decisions/2026-10-17-founder-store-chapter-rewrite.md`). The Interlude's second route (`interlude:17`) applies. The chapter should show what an objection can change and what it cannot.
- **Overclaiming recursion.** A company that edits its roles is at most level 2 in Ch 7's table (`07:55`), unless it has shown its edits make it better at finding further edits.

---

## 5. Seeds that touch Chapter 11

From `resources/editorial/easter-egg-register.md` and `resources/editorial/check-eggs.sh`.

| Thread | Anchors | Status | What it means for the rewrite |
|---|---|---|---|
| **The camel** | Planted `04` → "consider a camel"; pays off `11` → "And now the camel comes back" and `12` → "camels are native to Croatia" (`register:18`) | **proposed** (check warns, does not fail) | The only seed anchored in Ch 11. If the rewrite drops the line, `check-eggs.sh` warns and the register must be updated **in the same commit** (rule 4). The Ch 12 payoff still works from Ch 4 alone. Recommended: keep the line verbatim where the company's claim discipline comes in (§4.4 item 7). Do not explain it. |
| **Coffee** | `00-preface` "Your coffee is still too hot." · `02` "## The Coffee Test" · `10` "## The Second Coffee Test" → `13` "Decaf." (`register:13`) | **confirmed** (check fails if an anchor goes) | No anchor in Ch 11, so the rewrite cannot break it. A company chapter will want a coffee beat ("can the founder leave the company?" is the coffee test at organisational scale). Allowed, but rule 2: never explain the payoff in Ch 13, and a new coffee mention is a new seed only if the founder confirms it (rule 3). Do not make "Decaf" legible. |
| **Reviewer 2** | `01`, `02` (`register:26`) | **confirmed** | Not in Ch 11. Leave alone. |
| **Standing outside the box** | `05` "with no one standing outside it" → `13` "Behind it: forty monitors. Every timeline." (`register:21`) | proposed | **Risk of explaining a payoff.** A founder watching his company of agents through dashboards and status screens is very close to the Architect behind forty monitors. The chapter can describe the founder's view honestly but must not reach for monitor/timeline imagery or an "outside the box" line that decodes the fable. |
| **Capacity over power** | `00-preface`, `12` → `13` "Capitalism doesn't." (`register:22`) | proposed | A one-founder company is the book's capacity-over-power case. The chapter may use the phrase (it is the book's motto) but must not reach toward Ch 13's "Capitalism doesn't." |
| **The cable** | `00`, `04`, `05` → `13` "Shark biting cables." | proposed | Not in Ch 11. An outage story in the company (if any) must not be dressed as a cable. |
| **The dream** | `07` → `13` | proposed | Not in Ch 11. |
| **Names** | `13` (Devesh, Claudit, Norman) | proposed, author to confirm | The press's people have names (Theodora, Maren, Ilya). If the chapter names company or press agents, it must not echo the fable's naming games. |
| Octopus, tongue and ear, DNA, cathedral, reveal riddle, 11:53 PM | various → `13` | proposed | Not in Ch 11. Leave alone. |

Rules that bind every pass (`register:28-34`): read the register first; do not explain a payoff; new material that plants a seed must be added to the table; if an anchor changes, update the table in the same commit; Chapter 13 is protected in full. Run `bash resources/editorial/check-eggs.sh` after the edit.

---

## 6. The voice

### 6.1 What Chapters 4 and 5 sound like

The ai-tells skill names them as the baseline: "Blind readers consistently scored them highest because their ideas come out of scenes the author lived (the camel, Alberto, his mother's face, his own failed experiment, the Amazon offer)." (`.claude/skills/ai-tells/SKILL.md`). Five representative passages:

1. "Tongue out, strain upward, dignity temporarily suspended, result observed." (`04:31`)
2. "An infant trusts a face before it has words for anything. My mother's face meant food, warmth and safety. Nothing I have believed since has been better supported." (`04:93`)
3. "This is personal for me. I spent eight years building systems that rank human testimony: reviews, ratings and Q&A. … System 3 isn't philosophy to me. It's Tuesday." (`04:196-198`)
4. "On one occasion an agent ran `pkill -9 bash`, killed its own loop and left the project, which turned out to be one way a worker in this organization could retire. I have wanted to do the same from time to time. Luckily, I lack root access." (`05:14`)
5. "The organization whose applied science I would lead was larger than the entire company I had just left, and I remember sitting with the offer and feeling faintly embarrassed for everyone involved. What could so many people possibly do with a text box?" (`05:134`)

Also characteristic: "Humanity invented committees this way and then, dissatisfied with the original implementation, recreated them in software." (`05:174`); "An institution that never converges is a philosophy department with an alarming compute bill." (`05:184`); "The model got the library without the childhood." (`04:107`).

### 6.2 Characteristic moves

- **The argument comes out of a scene.** A concrete object or moment first (a camel, a phone call to Alberto, sixteen Claudes, a text box), the idea after. Chapter 11's rewrite has, for the first time, a real organisation the author runs; the scenes must come from its records and the founder, not be invented.
- **Self-deprecation that carries a point.** "Luckily, I lack root access."; "I was hoping to finish before lunch" (`01:14`); "which I suspect is either a research interest or a mild personality disorder" (`02:159`); "I prefer dead Europeans to cephalopods" (`04:65`).
- **Humour as compression.** One joke per idea, often a deflating clause at the end of a serious sentence ("…somewhere a PowerPoint theme earns its salary"). Code as punchline: `return True`, `new_status_final_2`, `WEDDING_FUNNEL_V7`, `RETURN_HESITANT_PERSON`.
- **Honest fences in-line.** "That sentence needs a fence around it." (`02:211`); the epistemic-swe outlier admitted in the table's next paragraph (`04:229`); "I have not run that weekend." (`12:235`). Qualifications stay with the claims they qualify (working spine).
- **First-person founder scenes** with real numbers and real stakes, never generic ("I spent eight years…", "Then Amazon made me an offer, and the offer was reviews.", `05:132`).
- **History told as a story with a turn**, then returned to agents in one sentence ("The agent version is almost embarrassingly literal: run the program…", `05:206`).
- **The closing question hands to the next chapter** (1 Oct evaluation: "each chapter's closing question does open the next chapter", `2026-10-01…:53`).
- **Headings:** title case, short, concrete or wry, often a sentence or a joke: "Call Alberto", "It Starts With a Face", "Code Can Touch Back", "A Swarm Should Not Automatically Become a Meeting", "Sixteen Claudes, Again", "Mei Does Not Need More Shoes", "The Book Comes Back to Bite Me". Not abstract nouns. Chapter 4 has 10 `##` sections in 4,512 words; Chapter 11 has 14 in 4,523. `###` is rare (Ch 4 "The 13579 Failure"). Ch 5 uses `---` scene breaks.
- **Chapter head format:** `# Chapter 11: Title`, blank line, italic subtitle (`*A Prototype Store*` today).

### 6.3 Anti-patterns (`.claude/skills/ai-tells/SKILL.md`)

Structural: (1) summary maxim at paragraph end ("Keep it only if a scene in the same paragraph earns it"); (2) citation chain (three or more sources one sentence each); (3) survey register; (4) **invented example doing a lived example's job** ("Flag it, and do not invent autobiography to replace it: ask the author"); (5) recap and signposting ("This chapter…", "As Chapter N showed"); (6) **cross-chapter stitching** (chapter numbers, callbacks a cold reader cannot decode); (7) every section the same shape; (8) **coinage inflation** ("The baseline spends a whole chapter earning one").

Sentence level: (9) negative parallelism ("Not X but Y", "X is not Y. It is Z"); (10) rule of three by reflex; (11) balanced hedge; (12) repeated formula; (13) inflated significance; (14) vague attribution; (15) AI vocabulary (delve, tapestry, landscape, realm, navigate, crucial, robust, seamless, foster, leverage, multifaceted, nuanced, intricate, showcase, embark, journey, unlock, harness); (16) em-dash and colon overuse; (17) abstract nouns doing the work; (18) slogan in quotation marks.

Protect: never touch Chapter 13; read the register; keep the author's best jokes even if they match a pattern ("Static. Static. Static. Jackpot.", `return True`, "back channel", "the unit is closer to the sigh", "Very efficient. Slightly evil."); "Never add facts, quotations or autobiography."

Numeric targets (`resources/editorial/check-tells.py`, calibrated on Chs 4–5): **maxim% ≤ 30, notXbutY/1k ≤ 0.5, cite-chains 0, xref/1k ≤ 0.5.** The current Ch 11 meets all four (21%, 0.4, 0, 0.0). Earlier passes found negative parallelism the chapter's dominant tell (`2026-10-02-ai-tells-report.md:420`); it is the habit most likely to return in a rewrite.

Known hazard for this chapter in particular: a company chapter will tempt the writer into **cross-chapter stitching** (the company implements Ch 3, 5, 6, 7, 8 and 10) and **coinage inflation** (the company's own vocabulary: gates, board, rituals, WBR, COE, constitution). The rule is one decodable callback where it pays, glossed for a cold reader, and no new bold term unless the chapter earns it.

---

## 7. Constraints for the rewrite

### 7.1 Length

- Current chapter: **4,523 words.** Part V neighbours: Ch 10 3,762; Ch 12 6,635. Range across numbered chapters: 3,148 (Ch 9) to 8,141 (Ch 5). Baselines: Ch 4 4,507.
- Recommended band: **4,000–5,500 words**, aiming near the current length. More than about 6,000 would make Part V's first chapter the second-longest in the back half and invite the survey register.
- Sections: 8–12 `##` headings. The current 14 is on the high side for its length.

### 7.2 Headings and format

- Keep `# Chapter 11: <Title>` and an italic subtitle line. If the title changes, keep the filename `11-the-store-that-builds-itself.md` unless the founder accepts renaming it and every dependent file (P1–P8) changes in the same commit.
- Headings in the house style (§6.2): concrete, short, title case, wry where earned.
- No chapter numbers in running text (xref ≤ 0.5/1k). The one existing chapter-number reference in Ch 11 is none; keep it that way.
- Bold only for a term defined once and earned across the chapter (the readiness evaluation asked Chs 9–11 to de-bold, `2026-09-30…:63`). At most one new term.

### 7.3 References and notes

- In-text citations are numbered links: `[1](appendix-references.md#ref-11-<slug>)`. Numbering restarts in each chapter. Entries live in `chapters/appendix-references.md` under `## Chapter 11 — <Title>` as `1. <a id="ref-11-<slug>"></a>Author, *Title* …`, with an optional `### Additional sources` list (`appendix-references.md:1-3, 509-515`).
- The build validates references: every link must resolve, its number must match the entry's position, and **every numbered entry must be cited** (`book-design/curated/manuscript.py:20-33`). Removing `ref-11-slate` and `ref-11-store-pearl` from the text without removing the entries breaks the build.
- No `[^n]` footnotes are used in the manuscript; follow the numbered-link convention.
- Company sources are not published works. Citing them needs a convention the founder accepts (for example, an entry naming the company record and commit, or a Note on Evidence pointer instead of a numbered reference). VP record point 3 is open: whether internal company material, service names and the founder's words to the company may be quoted.
- Qualifications stay with their sources in the appendix (`appendix-references.md:3`) and with their claims in the text (working spine).

### 7.4 Evidence-category labelling and the Note on Evidence

**Categories in use** (`appendix-note-on-evidence.md:7-22`): Argued; Run, on a bounded problem; Run, judged by simulated learners; one small experiment; Argued from history; Reported cases plus an illustrative story; illustrative; a design; Reported; Lived; Prototyped; Fiction. The VP's record adds a label the Note does not yet use: **"observed, with a re-checkable record"** for incidents seen once in operation whose commits and files can be reread, reserving **"run"** for anything a committed script reruns (`press/decisions/2026-10-16-vp-books-company-case-study.md`, Evidence categories).

**In the chapter text,** every company claim carries its category where it is made, in the book's register (a fence after the claim, not a disclaimer section). Specifically:

- an incident: observed once, with its record;
- a mechanism: designed, until shown to work;
- any catch between agents: one model checking itself (the "one witness" limit), every time, not once at the end;
- learner outcomes: say whether there are any;
- the planted-false-diagnosis test: say it has not been run in the company (unless it has, with a record).

**The Note on Evidence will need:**

1. **Row 11 rewritten** (`:20`): new title; "What it rests on" naming System 3 Company's records (and the store prototype if it survives); status in the agreed categories, e.g. "Lived and observed, with re-checkable records; no learner outcomes yet; the company was built from this book's argument", wording to be set by the fact-checker against the records.
2. **Paragraph 2 qualified** (`:5`): it says stories may be composites or embellished and "I do not say which is which". The company material may not be composited (VP point 4), so the Note must say that Chapter 11's company material is not changed or combined. Otherwise readers will discount the one chapter that is not composite.
3. **"A Test Still to Run"** (`:24-37`): add one sentence if Ch 11 describes agent-on-agent catches, saying they are not results of this protocol. If the founder decides to run it in the company, the section changes and so does the afterword (`afterword:21, 64`).
4. **"How This Book Was Written"** (`:39-43`): the press, itself a company of agents of the same model, studied the company and drafted the chapter. The Note should say so, in the same plain register ("I used AI to help write and revise this book…"). This is the decision record's objection 2 made visible to readers.
5. **Row 7** (`:15`, "the store is illustrative") can stay; Ch 7's store becomes the only store.

**Afterword** (`:67`): update "one prototype" (D6); optional line in the contribution table (D7).

### 7.5 Hard rules carried into the brief

- The writer drafts only from the checked evidence record and the book, not from summaries (decision record; VP record). Every place a lived scene, a number or the founder's words are needed is an `<!-- AUTHOR: … -->` ask, not invention.
- The existing AUTHOR comment at `11:7` stays until the founder accepts its removal.
- Chapter 13 is untouched. No pass edits it.
- Run `bash resources/editorial/check-eggs.sh` and `python3 resources/editorial/check-tells.py 11` after the draft; the camel register line changes in the same commit if the anchor moves.
- Changes to other files (Ch 10 ending, Ch 12:79, Part V page, Zen, Note on Evidence, afterword, references, art anchors, opener, NotebookLM briefs) are listed in the proposal as consequential changes, each needing the founder's acceptance, not slipped in with the chapter.

---

## Handoff

- **Changed:** this file only.
- **Believe (high):** the dependency list in §3 is complete for the manuscript, references, art placements, opener, seeds and NotebookLM briefs (found by repository-wide search for the title, filename, Mei, Sami, prototype, Surface Value and related terms). **(Medium):** the candidate payoffs in §2 are real in the company; I have only its README and CLAUDE.md, and the company study must confirm each.
- **Next:** the company study (other press roles) and the experiment developer's evidence record; then the head of book's brief to writer-system-3, carrying §4.4, §5 and §7.
- **Open for the founder (already in the decision record or added here):** keep a short store origin or drop it (D6, AUTHOR comment at `11:7`); Mei, Sami and Lea dropped; quoting company internals and the founder's words (VP point 3); filename and title; the Ch 10 last lines and Ch 12:79; new opener art.

# Afterword: What System 3 Contributes

As we build autonomous AI, we keep rediscovering science as its architecture. The book follows that claim into a further possibility: more people able to investigate and build local arrangements, let the world rule some of them out, and choose among the survivors under rules they can see and change. They need not first agree on one account of how everybody should live.

Three supporting theses are where I think the book adds something. For each, I name the inheritance, the proposed addition and what we still need to test.

## The Starting Point

Peter Godfrey-Smith’s *Theory and Reality* ends with a picture I take as given. Science combines an empirical strategy, developing ideas so that experience can constrain them, with a social organization that carries the strategy out. Its reliability does not require perfect reasoners; the organization can expose errors its members would otherwise protect.[1](appendix-references.md#ref-aft-godfrey)

Popper, Duhem and Quine, Kuhn, Lakatos, Laudan, Longino and Kitcher argue about almost everything inside that picture. System 3 starts from what they share and asks what follows when the participants are artificial agents: cheap, copyable, able to use the records, build instruments and edit some of the rules they work under.

## Thesis 1: Cheap Minds That Are Wrong Together

**When cognition is cheap and its copies share blind spots, the bottleneck of inquiry moves from producing hypotheses to producing independent evidence and getting criticism acted on.**

*Inheritance.* The elementary version of Condorcet’s jury theorem needs independent voters.[2](appendix-references.md#ref-aft-condorcet) Kitcher examined how the pursuit of credit can spread investigators across programmes instead of sending everyone to the current leader.[3](appendix-references.md#ref-aft-kitcher) Zollman found conditions where less connected communities learn more reliably.[4](appendix-references.md#ref-aft-zollman) How many investigators there are, what they pursue and whose evidence they see are part of the account of how science works.

*What is new.* Starting another agent can be cheap. It does not give us another biography, and academic credit does not automatically give the copy a reason to pursue a neglected programme. Others have worried about algorithmic monoculture and AI narrowing what scientists study.[5](appendix-references.md#ref-aft-monoculture) Errors are correlated even across developers,[6](appendix-references.md#ref-aft-correlated) narrow attention can make agent populations herd,[7](appendix-references.md#ref-aft-herding) and epistemically diverse groups have been proposed for discovery.[8](appendix-references.md#ref-aft-many) I follow that problem through the institution, including its overseers. Where does a critic get evidence the builder missed? Did it inspect the artifact before reading the builder’s explanation? Can it trace two agreeing reports to one source? Chapters 3, 5, 6 and 8 propose isolated contexts, provenance and different models as ways to try to obtain that independence. Adding workers is the easy part.

*What needs testing.* The note on evidence proposes planting a false belief and measuring how far it travels. If different developers catch it no more often than isolated copies, developer diversity has not helped in that setup. If provenance adds nothing over isolation, that proposed repair has not earned its cost. These comparisons test parts of the architecture; identifying the bottleneck also requires measuring what happens as we add investigators.

## Thesis 2: Checking Without Understanding

**Checking can outrun anyone’s understanding of a result. People can rely on the checks and still lack the understanding needed to choose the next question, leaving its choice to whoever controls the laboratory.**

*Inheritance.* Hardwig showed that rational belief already depends on others’ work we cannot check.[9](appendix-references.md#ref-aft-hardwig) Tymoczko argued that the computer proof of the four-color theorem put trust in a machine inside the warrant of a proof,[10](appendix-references.md#ref-aft-tymoczko) and Humphreys named the general condition epistemic opacity.[11](appendix-references.md#ref-aft-humphreys) Kitcher’s well-ordered science asks that inquiry pursue the questions informed citizens would choose.[12](appendix-references.md#ref-aft-wellordered)

*What is new.* A proof checker, a held-out test and an independent replication provide different grounds for reliance. None requires me to repeat every step myself. But a checked result may leave me unable to see what is worth asking next. That is the gap Chapters 9 and 12 investigate. In a laboratory running on rented models, someone will allocate the compute whether I understand the possibilities or not. Dantzig’s hour with von Neumann suggests what I want from the assistance: enough teaching to notice a question I could not previously see. Chapter 7 adds a rule about authority. Being able to propose a new aim should not give an agent permission to adopt it.

*What needs testing.* Does assistance leave people better able to explain the possibilities, propose questions and challenge the agenda, or mainly better able to request an answer? Compare systems built to teach with systems built only to deliver results. The risk I describe and the remedy I want should face separate tests.

## Thesis 3: Building Past the Critique

**Building alternatives costs much more than criticizing an arrangement. Cheaper capacity could let more groups try local institutions, with objectives they can inspect and amend. Ostrom’s polycentric governance gives that possibility a practical form.**

*Inheritance.* Latour asked why critique had run out of steam and called for composition.[13](appendix-references.md#ref-aft-latour) Rorty asked us to hold commitments knowing they are contingent, and later attacked a spectatorial Left that had given up on reform.[14](appendix-references.md#ref-aft-rorty) Ostrom found communities governing commons without waiting for the right theory of society, and her later work placed them inside the polycentric governance Vincent Ostrom had helped describe decades earlier.[15](appendix-references.md#ref-aft-polycentric) Scott and Morozov supply the objection: simplifying the world to make it legible and manageable is how high modernism and solutionism did their damage.[16](appendix-references.md#ref-aft-solutionism)

*What is new.* I give the ideology vortex an economic reading: understanding an arrangement’s failures may leave us dependent on it because we cannot afford to build another. The double-descent analogy lets me ask what happens beyond that predicament. More explanations will not help if none can lose. More construction might, if people can try arrangements, inspect their consequences and revise the rules for choosing among them. The scheduler in Chapter 12 makes the limit plain: it can find a workable timetable and still exclude the smaller group. Those members need standing to contest the rule.

*What would show it wrong.* If cheap capacity mostly produces more fluent critique and small groups gain no arrangements they can sustain and revise without a new landlord, the second descent is a picture and not a path.

## The Architecture That Carries Them

The theses need machinery. These are the book’s design proposals and the problems they inherit.

| Inherited problem | Where it comes from | Proposal in System 3 |
| --- | --- | --- |
| A persuasive account can avoid contact with failure | Popper; empiricism | External tests, instruments and predictions committed before results |
| Failure implicates a bundle; corrections lose their targets | Duhem and Quine; Doyle | Claims with addresses, recorded support, dependent decisions returned to review |
| Knowledge travels without its conditions | Popper’s World 3; Alexander | Patterns with scope, cases, failure conditions and links; high-functioning bullshit named as the failure |
| Criticism without consequences | Longino | Objections that travel with the decision and an owner who signs for proceeding |
| Belief, pursuit and allocation get confused | Laudan; Kitcher; Zollman | Budgets for alternatives; isolation and diversity built deliberately |
| The improver edits what judges it | Laudan’s reticulated model; engineering practice | A constitutional surface: the nearer a change sits to the aims, the slower and more independent its approval |

Resemblance to a scientific institution establishes nothing by itself. Each proposal should beat a simpler arrangement on the same model and budget, or be dropped.

## What Kind of Contribution This Is

| Part of the argument | Status |
| --- | --- |
| Science as empirical strategy plus social organization | Inherited and summarized |
| Claim addresses, executable patterns, consequential objections, constitutional surface | Design proposals, partly demonstrated in others’ systems: the Fermat formalization’s dependency graph of theorem statements (Chapter 6), Stellar Colosseum’s fatal-flaw rule (Chapter 6), Agentic Harness Engineering’s read-only verifier (Chapter 7) |
| Thesis 1: correlated cheap inquirers | Argued; one experiment specified in advance and not yet run |
| Thesis 2: verification without comprehension | Argued from mathematics and philosophy of science; an empirical question left open |
| Thesis 3: polycentric construction after critique | A philosophical and ethical argument with practical tests named |
| My own experiments | Small: one bounded problem, teaching demos judged by simulated learners, one ten-task comparison, one prototype |

The book does not demonstrate the whole architecture or claim priority over every related proposal. It names three claims precisely enough to be wrong, and arrangements to build while we find out.

The proposed architecture should help fallible agents check one another and correct what they inherit. Making it cheaper could let more people use it to investigate and build. I want those people to understand enough to choose the questions, and to retain a say in the arrangements that result.

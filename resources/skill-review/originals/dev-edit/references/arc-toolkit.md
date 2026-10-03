# Arc toolkit

Diagnostics that have found real problems, each with the case that showed it.

## Contents
- Book level: spine, parts, handoffs, evidence gradient, peaks, compounding, seeds, narrator, recap, balance, title, ceremony, endings
- Chapter level: one spine, engines, section order, section endings, the abstract peak, known history, metaphors, case-first
- Arc options as beat sketches

---

## Book level

**Spine and parts.** Write the spine in one sentence, then a table of parts with the single question each answers. If a part needs two questions, it is two parts or one of them is in the wrong place. System 3 went from "Chapters 1–4 build pieces, 5 reveals" to five parts once the author said 4–5 were the institutions part and 9–10 were about keeping the human in control. The question table made it obvious that Part IV needed a threat to answer, which produced the interlude.

**Handoffs.** Each chapter should end on the question the next one opens; within a chapter, each section can open on the previous section's last word. `arc_map.py --handoffs` prints every seam. Good seams in System 3: Ch 3 ends "How do you know what to trust?" → Part II; Ch 8 "the overseer is not ground truth" → Ch 9 "Find me the cheapest flight", philosophy straight into ordinary life. A seam that needs a thousand words of narration in between was already working.

**Evidence gradient.** Tag every chapter: Run, Argued, Designed, Reported, Imagined. In System 3 the evidence thins exactly as the stakes rise: Ch 2–3 were run, Ch 4 had one small experiment, Ch 5 is argued from history, Ch 6–12 are designed, argued or reported. Making the reveal louder (its own page) without better support raises the cost of that gap. The highest-leverage fix is usually one small experiment the book already designs (Ch 5's planted-bad-diagnosis test), not more prose.

**Whose objection is strongest.** Name the objection a skeptic will raise and check whether the text answers it where it lands. System 3: "you rediscovered bureaucracy and relabelled it". The answer is to say which jobs make it science rather than organization (independent disagreement, instruments with track records, provenance, funding the weaker program, objections with consequences).

**Peaks, troughs and variance.** Score chapters, then look at the shape, not the mean. The Dream had higher peaks than Sapiens but deeper troughs, and its biggest idea arrived in Ch 42 instead of Ch 2. An arc that peaks at the book's lowest-scoring chapter (the "eighth verb" argument across System 3 Ch 5–8 peaked in Ch 8) is a structural problem even if each chapter is fine.

**Compounding.** One lens that pays off in every later chapter (Harari's imagined realities) beats several good ideas that compete. Check whether the big ideas compound or merely accumulate.

**Seeds and payoffs.** Keep a register: thread, where planted, where it pays off, confirmed/proposed. System 3's octopus, cable, coffee, camel and tongue-ear threads make the fable in Ch 13 feel inevitable, and every one of them looks like a digression on its own. The Ch 3 history was cut once even after the reason to keep it was written down. Confirmed seeds block a pass; proposed ones are questions. Never explain a payoff.

**Narrator consistency.** "Chapters 7–10 are told by a different narrator": someone who read everything instead of someone who watched it happen. First-person density per 1,000 words is a quick proxy (in the 3 October 2026 text Ch 5–7 run at about 2, Ch 8 at 11, Ch 11 at 7, and the other core chapters at 14–39). Ch 5 is history by design; Ch 6–7 are the real gap. A personal experiment ages better than a research catalogue.

**Recap and re-teaching.** Later chapters should invoke the thesis, not re-teach it. Look for the same anecdote opening several chapters (the editing-with-an-agent story opened three of five) and the manuscript recapping itself (four full recaps between Ch 7 and 12). `arc_map.py --recaps` finds near-verbatim repeats across files.

**Holding pens and listicles.** The Dream's Part V ran seven chapters on one formula (thinker → insight → surprise connection → "philosophy became engineering") and bounced across three centuries. Material that belonged inside the chronological narrative had been collected in a holding pen. Scattered back into the timeline, each figure reinforces momentum instead of killing it.

**Balance.** Word count per part. System 3 Part III ≈ 16,400 against Part IV ≈ 5,300, while Part IV carries the answer to the book's biggest threat. Cut where the weight isn't earned (Ch 6), not evenly.

**Title.** Check what the title names. "Towards Fluent Autonomy" names Ch 10, the shortest core chapter, inside Part IV; the spine is emergence → science → capacity. Decide the title last.

**Ceremony.** Count page turns between chapters. Reveal page → three paragraphs → part title → epigraph page was four turns before Ch 6; folding the paragraphs onto the part opener removed one. Epigraphs drawn from an appendix spend that appendix.

**Two endings.** If the book ends twice (System 3: Ch 12 the ending capacity wins, Ch 13 the ending power wants), label the alternative so readers don't have to guess, and make sure the label doesn't give away the punchline (the Fisher quote before "Capitalism doesn't."). Let the last word come after both.

## Chapter level

**One spine.** A chapter with two engines (Ch 1: the VP's question and "can I stop hovering?") runs at 7. Braiding them into one question ("if the agent can work while I'm getting coffee, what am I for?") is worth more than any polish.

**Engines that disappear.** A question planted on page one and never mentioned again leaves the reader without a reason to continue. Bring it back once, at the section where it matters.

**Section order builds stakes.** Order sections so stakes rise: what we can do, what it's for, what can go wrong. Then the ending can land with irony ("Then I went for coffee" right after explaining how badly that can go).

**End sections on a turn.** A section that closes on a settled thought lets the reader put the book down. End on the next worry.

**The abstract peak.** If the chapter's most frightening idea is told abstractly, turn it into a four-sentence story the reader watches happen.

**Known history.** Compress history readers already know (AlphaGo, the LLM story) by about half. Keep history that derives something (Ch 3's coding-tool history builds the five layers instead of asserting them; keep that).

**Decorative vs organizing metaphor.** Double Descent in Ch 12 was decorative until it organized the chapter (first descent, the rise, whether a second descent follows). A metaphor that doesn't structure the chapter is a pun.

**Case-first.** Real exhibit, then the operation it demonstrates, then the hard case. Philosophy drawn out of events rather than asserted beside them. A philosopher roll-call (one paragraph-long introduction per thinker) is the most common way Ch 6 lost momentum.

**Cold opens.** Ch 5's petrification scene is the model: start inside the event. Two cold opens in a row on catastrophes is a tic.

**Discovery vs discipline.** Every structural fix trades a little discovery for clarity. Name the trade. Past about 9 on momentum, a chapter moves from essay toward story; for a first chapter that's right.

**Fluff vs structural recap.** Some soft-looking lines carry the structure ("Then the difficulty reaches us." turns the chapter from agents to the human). List them as kept, with the reason.

## Arc options as beat sketches

When order is the question, show the options in one block with a rough energy line and the trade-off, then recommend and let the author choose:

```
A  claim → Amazon → phone → theatre → turn
   ▃       ▅        ▄       ▇         ▅      keeps the handoff chain; fall lands last
C  Amazon → claim → phone → theatre → turn
   ▅        ▃       ▄       ▇         ▅      most alive opening; breaks the chain
```

The author chose C over the recommended A. Recommend, don't decide.

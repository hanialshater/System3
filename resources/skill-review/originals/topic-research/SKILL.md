---
name: topic-research
description: Find material for Hani's writing — exhibits, cases, thinkers, studies and lineage for a chapter or post that already exists, or a research base for a chapter being planned. Searches his own material first (chapters, drafts, archived books like The Dream, the Arabic blog, past chats), then the web; maps every candidate to the operation it would demonstrate; checks collisions with other chapters; credits lineage; budgets words so additions don't swell the chapter; and hands recent claims to fresh-claims. Use whenever the user asks "find examples", "what else could go here", "research for chapter N", "real cases for", "who argued this before", "is there a better exhibit", "discovery pass", or wants a chapter grounded in real events rather than invented ones.
---

# Topic research

Finding is a different job from checking (fresh-claims) and from remembering (story-mining). It asks: what should be here? The best passes in System 3 came from it: Fermat, Riemann and Navier–Stokes as exhibits in Chapter 6; Jacobs, the replication crisis and Ostrom's throughput question carried into Chapter 12 from The Dream; Russell's assistance-game lineage credited in Chapter 9. The worst outcome also came from it: a research base turned straight into a chapter, and Chapter 8 became "an eleven-technique instrument tour" that a blind reader scored 5.

## Two modes

**A. Exhibits for an existing chapter (default).**
**B. A research base for a chapter being planned**, in the repo's format (`resources/chapter-NN-*-research.md`; template in `references/templates.md`). A research base is raw material, never the chapter.

## Mode A workflow

1. **Name the chapter's operations.** List the moves the chapter argues (Ch 6: give the claim an address, separate use from investigation, keep the funding decision visible, find where the result lives). A candidate earns a place only by demonstrating one of them.
2. **Search his own material first** with `scripts/own_material.py "<pattern>" --roots chapters resources <archive> <blog>`. The Jacobs case, Ostrom's "the bottleneck was always human throughput" and the Newton brachistochrone answer were already written. Then past chats (conversation_search). Then the web.
3. **Collect candidates** in a table: candidate | operation it demonstrates | why it beats the current example | source (primary first) | date | already used in (run `--used-only` for the collision check) | words it costs.
4. **Choose one per stop.** Exhibits arrive at the stop they illustrate, never as a gallery at the end. If a thinker or case already lives in another chapter, use a callback ("Duhem again"), or keep the idea and drop the name.
5. **Prefer**, in order: the author's own experiment or lived case; a real case with a scene in it (Fermat's agents losing the thread rhymed with Carlini); a documented historical case; a study. Invented composites only as marked hypotheticals.
6. **Write it as a scene, not a news brief.** Three paragraphs opening "In August 2026, Anthropic reported…" read as a press digest. Carlini was watched, not reported.
7. **Budget the words.** "Anything worth a pass without a great increase in pages" was answered with +230 words and two offsetting cuts. State the net change.
8. **Credit lineage** the chapter builds on (Russell's assistance games under Layer 4; Harari on who sets science's priorities). Cite where a reader would look.
9. **Hand recent claims to fresh-claims** before they go in. Phrase contested or causal claims as what they are: Mumford's real review title ("Mother Jacobs' Home Remedies", 1962) instead of a quotation The Dream couldn't verify; the South Bronx as "the standard example", not a causal claim.
10. **Mark shelf life.** Load-bearing exhibits should survive a year; weeks-old results are illustrative and dated in the text.

## What the research must not do

- Turn a chapter into a survey or catalogue (Ch 8, the Ch 7 learning-methods first half). Many techniques in sequence is a reference section.
- Make the evidence louder where it's already thin without making it better (the reveal problem).
- Introduce a philosopher as new in a later chapter.
- Replace a lived example with a famous one when the lived one is the reason the passage is his.

## Output

A short report: the operations, the chosen candidate per stop with the reason, rejected candidates and why (one line each), collisions found, word budget, claims sent to fresh-claims. If he wants it placed, apply as a flagged pass (de-llm's apply_pass or dev-edit's ops), not as free rewriting.

## Files

- `scripts/own_material.py` — search his corpus first; `--used-only` for collisions.
- `references/templates.md` — research-base template and candidate table.

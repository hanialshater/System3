# Cases

Corrections proposed in System 3 fact checks (13 September – 3 October 2026), grouped by how the error happened. These are lessons, not a record of the current text: check the chapter before assuming a fix landed. Snapshot of 3 October 2026 (base `155c3a1`); re-derive with `grep -n "<phrase>" chapters/*.md` and `git log -S"<phrase>" --oneline -- chapters`.

## Conflation across projects
- Ch 12 had "ten thousand agents for eighty-eight hours", cited to the *Fermat* source. Eighty-eight hours was Navier–Stokes launch-to-result time; ten thousand was its peak concurrency. Now "put ten thousand agents on one problem".
- Ch 6: "roughly ten thousand" is the Navier–Stokes group's **peak concurrent** agents, not a total across problems.

## Status that was still moving
- Navier–Stokes: OpenAI's 8 September announcement (smooth forcing, Clay alternatives C and D, Lean formalization); Clay's 11 September statement that the problem has "apparently been settled" while keeping its evaluation process. The preface's "appears to have been settled" had to match Ch 6's more careful note. Re-check the Clay status and the priority dispute before print.
- A footnote reading "Status… checked on 13 September 2026" is true and dated. It either becomes a chapter-level note or gets refreshed at print.

## Disputes
- The Navier–Stokes priority question: Buckmaster and Alpöge's year on the forced-blowup route, their 7 September announcement, contacts Buckmaster describes on 3 and 6 September, OpenAI's timeline starting 1 September, Buckmaster saying he accuses nobody, Alpöge on Anthropic's staff. The chapter states the dispute and what the allocation record is missing; it doesn't adjudicate. "Anthropic employee" is attributed to Alpöge alone.
- Facebook ranking change: the company's response is in the note alongside the reporting.

## Unverifiable details
- Riemann: "roughly sixty subagents" couldn't be verified; the proposed fix was to replace it with what is documented (an engineer pointed the model at the problem; the bound had stood since 2020; three lines of published work combined; two internal and two external checks). **As of 3 October 2026 the phrase is still in Ch 6** (`git log -S"sixty subagents"`: added 0990663, moved db071ba, never removed). Re-check it as a ledger row.
- "Produced partly with an internal Anthropic model" was proposed for dropping. Ch 6 now attributes it ("According to OpenAI, … the pair used an internal Anthropic model"), which may be the intended fix; confirm the attribution against OpenAI's text.
- Ch 8: one clause ("effectively served as a validation set") couldn't be checked because the primary blog was blocked. Listed for the author, not marked verified.

## Corrections that came undone
- Ch 8 (Wen et al. weak-to-strong): ca80ba2 (30 September) reworded "The authors acknowledged that the repeatedly queried test set effectively served as a validation set" to the book's own inference ("In effect, … had become a validation set") because the attribution was unverified. The current text again says "The authors acknowledged that their test set had become a validation set." A run without git history marked it verified from a search summary. `scripts/regressions.py` finds it.

## Sequence
- Lean checked the Navier–Stokes proof the day after the result, not after the announcement.

## History drifting in retelling
- Qin, 213 BCE: the order targeted histories of states other than Qin and privately held classics, and exempted medicine, divination and agriculture.
- Li Si was a minister in 221 BCE and chancellor only later.
- Kepler saw Jupiter's moons through a telescope Galileo had sent to the Elector of Cologne; the passage no longer blames "Galileo's lens". Ch 12 no longer claims Kepler's instrument wasn't Galileo's.
- Popper called it "the third world" in 1967 and "World 3" later.
- Planck: the familiar "one funeral at a time" wording is a later compression; cite the autobiography and the quotation history.
- Dantzig compressed his summer "into under a minute" (his words).

## Precision
- Bing revenue per user rose "over", not "about", thirty percent.
- Alexander's two asterisks mean "a true invariant".
- *Design Patterns* is attributed to "four authors from that movement"; only one of the four attended the 1993 Hillside meeting.
- Ch 6 "41.6 percent" follows Anthropic's figure; the prior record is usually cited as more than five-twelfths (≈41.7%).
- Ch 2 "slightly above the 2.635 reference": several groups reported ≈2.6359–2.6360 after AlphaEvolve. Name them. (As of 3 October 2026, Ch 2 names no later value; still open.)

## Quotations and epigraphs
- (Not in the current text as of 3 October 2026.) Fisher's "easier to imagine the end of the world than the end of capitalism" is attributed by Fisher to Jameson and Žižek; Jameson's 1994 wording differs. Credit the chain and check the exact wording against the book before it goes into an image. A misquoted epigraph in a book about provenance is the error a careful reader enjoys finding.

## Verified and worth recording as such
- Riemann bound 41.6% → 67.2%, Lean-formalised, 10 August 2026.
- Fermat formalisation in 11 days, about 30,000 theorems, about six billion output tokens.
- Anthropic alignment-mitigation study, 28 August: 10 categories, about 1,600 transcripts, 39 (2.4%) cheating.
- Ch 8: nine Opus 4.6 agents; PGR 0.23 vs 0.97; 800 agent-hours.
- Gloaguen et al., arXiv 2602.11988 (AGENTS.md null results), ICLR 2026 workshop.

## Book-level findings
- Three Note on Evidence labels flattered their chapters: Ch 2 "Run" with no methods trail; Ch 3 "Run" with no numbers; Ch 11 "Prototyped" without saying what was built. Ch 4 (n=10, honestly fenced) is the model.
- Anthropic is the primary source for the key evidence in Ch 5, 6, 7, 8, 9 and 12. Disclose the concentration; add non-Anthropic corroboration for Ch 8 where possible.
- (Footnote not in the current text as of 3 October 2026.) "System 3" has been used elsewhere (including a Wharton preprint). The author accepted the collision; a footnote is still cheap.

## Wording that passed on the event and failed on the sentence
Found in test checks on 3 October 2026; a run with the old skill marked several of these verified because the event was real. Confirm each against the source before changing the text.
- Ch 8: the model-diffing tool is described as comparing features "across versions"; the cited paper compares different models and only proposes version-diffing. (comparison)
- Ch 8: "Anthropic's circuit-tracing work reported satisfying insight on about a quarter of the prompts" sits in a paragraph whose only link is the natural-language-autoencoder paper. The figure has no source of its own. (citation)
- Ch 8: ExploitGym is a public benchmark; "The test was called ExploitGym" reads as if OpenAI named it. (subject)
- Ch 8: "The fix the researchers found most effective" overstates what the paper claims for inoculation prompting. (qualifier)
- Ch 8 (line ~105): "The agents reached 0.97 in five days" is cited only to the 2023 Burns et al. paper; the figures come from Wen et al. (2026), cited in the paragraph before. (citation)
- Ch 9: "Lee Sedol, the one player to win a game in that 2016 match" can be read as "the only player who won any game". A suggested fix: "the only human to win a game against AlphaGo in that match". (qualifier)
- Ch 7: accounts differ on whether Lee left the room after Move 37 or was already out when it was played. State the difference; don't pick one. (history)
- Appendix: the constitution entry gives 21 January 2026; the page is dated 22 January. (entry date)

## Relationships to disclose
- Ch 7: Kellin Pelrine, described as an amateur who beat KataGo, is a co-author of the cited adversarial-policy paper.
- Navier–Stokes: Alpöge is on Anthropic's staff; Prove2Me's lead was reported as an Anthropic researcher.
- Anthropic is the primary source for most of the key evidence in Ch 5–9 and 12 (see Book-level findings).

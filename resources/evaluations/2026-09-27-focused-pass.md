# Focused pass on the supplied v2

This review copy follows `System3-arc-edit-v2.patch`. It supersedes the earlier arc-parts evaluation for the passages changed here. It is not a record of author acceptance.

## What changed

1. The science reveal and its explanation share one page. The revised paragraph specifies the function behind the resemblance: accepted claims can be reopened, rival explanations can receive resources, investigators can bring independently gathered evidence, and failures can change methods and standards. The existing Part III question and narrative follow on the next page.
2. The short interlude remains before the human chapters. “Every part of System 3 can survive this” becomes “Much of System 3's machinery can survive this,” preserving the distinction between an apparatus and its corrective function.
3. The first AI failure concerns authority to dismiss a result, change the standard and certify the change. It no longer treats designing one's own tests or instruments as evidence that their answers were predetermined.
4. The ownership route specifies actions that block a challenge: refusing an experiment, denying data access and withholding funding. Ownership alone is not asserted to cause corruption.
5. The bargaining argument distinguishes people an owner no longer needs from the people who remain indispensable. It no longer asserts that every remaining worker loses bargaining power.
6. Part IV is titled “Human Purposes,” matching the chapters' work on intention and agency.
7. “An Alternative Ending” is visible before Chapter 13. The Fisher page is removed. Chapter 12's existing handoff, the complete fable and the final scaffolds page are unchanged. The fable can complicate the hoped-for future through politics, desire, identity and its emotional ending.
8. Part titles and epigraphs share a page. The v2 checker still distinguishes confirmed seeds from proposed readings.

## Historical precision

The interlude's new reference is Lysenko's own report, especially its concluding announcement of Party approval:
https://www.marxists.org/reference/archive/lysenko/works/1940s/report.htm

The historical check also consulted Svetlana A. Borinskaya, Andrei I. Ermolaev and Eduard I. Kolchinsky, “Lysenkoism Against Genetics,” *Genetics* 212(1), 2019, pp. 1–12:
https://doi.org/10.1534/genetics.118.301413

The revision incorporates politically permitted criticism in 1952 and avoids suggesting that the damage was simply undone in the mid-1960s. The application to AI institutions remains an argument. This was a targeted check of the revised interlude, not a fact-check of the whole book.

## Text boundaries

All numbered chapter files (preface, Chapters 1–13 and scaffolds) are byte-identical to the supplied v2 baseline. The new prose is confined to the reveal's short paragraph and the interlude. The Chapter 10 paragraph from the earlier assistant revision is not included in this v2-based pass.

The full Markdown was reconstructed from the supplied manuscript and source patches. Source-only illustration tags omitted by the original assembly cannot be recovered from that text. Use the incremental patch for an existing repository; the packaged source directory is not a replacement for the entire repository.

## Verification

The manuscript builds without missing-glyph warnings. The reveal, Part III opener, interlude, Part IV opening and Chapter 12→13→scaffolds sequence were visually checked. The callback checker passes. The incremental patch passes whitespace validation and reverse-application validation against the revised source. New historical sources are included in the footnote and references.

## Reveal refinement

The final narrow pass changes only the reveal paragraph and its spacing in the manuscript. “We call it science” begins roughly one-third down the page, with a larger interval before the explanation. The incremental `System3-reveal-pass.patch` isolates this pass; the cumulative v2 patch also includes it. The surrounding argument and ending remain unchanged.

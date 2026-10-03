# System 3 house style (from the 30 September 2026 copyedit plan)

| Item | Rule | Notes |
|---|---|---|
| Spelling | American (color, behavior, catalog, program, traveled, labeled, fiber, gray, anesthetist, theater, plow) | British spellings survive only in titles, proper names and quotations. "Research program" for Lakatos and Kitcher alike. |
| Quotation marks | Curly (“ ” ‘ ’) in prose | Straight only in code, URLs, HTML comments, raw LaTeX. The renderer prints quotes as typed. |
| Punctuation with quotes | American: commas and periods inside closing quotes | |
| Ellipsis | Single glyph (…) | Code keeps `...` |
| Dashes | Unspaced em dash (—), used sparingly | Don't add dashes where a comma works. Epigraph attributions ("> — The Zen of System 3") are the conventional exception. |
| Serial comma | Mostly omitted. Remove from simple word lists; keep where the last item is a clause or long phrase, or where it helps the reader | No global pass: many series are rhythmic clause sequences. |
| Numbers | Words for one to one hundred in narrative prose | Numerals for measurements, scores, percentages from studies, years, table data, technical problem statements ("26 circles"), pattern and move numbers, World 3. |
| Percent | "percent" in prose, "%" in tables | |
| Headings | Title case; capitalize words of four or more letters, including prepositions (With, From, Into, Than) and all verbs (Is) | Short prepositions, articles and conjunctions lowercase unless first or last, or after a colon or dash. |
| Bold | Only a coined term at its first definition, and Chapter 6's pattern *Therefore* lines | Not for emphasis or slogans. Borrowed terms go in italics. |
| Italics | Titles of books, papers treated as works, ships; words as words; non-English terms | |
| Cross-references | "Chapter 6"; "the previous chapter" where adjacent | |
| Compounds | e-commerce, email, dataset, on call (noun) / on-call (adjective), open-ended, best-known | |
| Company and model names | As the source styles them: Claude Code, Claude Opus 4.6, GPT-4, AlphaEvolve, DeepMind, OpenAI | |
| Citations | Chapter-scoped numbered notes matching the appendix entry | Enforced by `manuscript.validate_references`; a deleted cited sentence moves its entry to "Additional sources" and the chapter is renumbered. |

## Lint on 3 October 2026 (`main`)

Spelling still British in three places: "centre" (Ch 7), "catalogue" (Ch 8), "grey" (Ch 9). Nine bold spans remain. Headings: "Additional sources" in the references (title case would be "Additional Sources").

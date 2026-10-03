# Defects seen in past proofs

| Defect | Where | Cause | Fix |
|---|---|---|---|
| Six figure captions printed with no figure above them | Ch 2 (pp. 25, 26, 27, 30 ×2, 41 of the 372-page proof) | Figures commented out as missing; captions left outside the comments | Restore the technical figures or move captions into the comments; ten Ch 2 figures still unrecovered (`resources/art-direction/missing-figures.md`) |
| Running headers as garbage glyphs ("V", "V}}}}V") | Preface and every back-matter page | Non-chapter header path, likely a font-encoding mismatch in the ReportLab build | Fix the header font path; check back matter on every proof |
| The same page of claims printed twice | Ch 4 seven claims, pp. 92–93 | Duplicated block | Remove; `proof_qa.py` flags duplicate page text |
| Chapter opener subtitle ≠ body subtitle | Ch 5 | Cover lettering generated from an older title | Check `provenance.json` titles; regenerate or retitle |
| Wrong note printed | Ch 6 Saussure note showed Ch 4's text | `[^saussure]` defined in two chapters; joined build keeps the first | Chapter-scoped keys; duplicate-key check |
| Endnotes only for some chapters | Ch 5–7 had notes, Ch 8–9 none | Apparatus applied unevenly | One system for the whole book |
| Preface dated before the events it reports | Preface said August, reported 11 September | Date not updated with content | Date check in fresh-claims |
| Internal reference error | "rest of this chapter" for "rest of this book", end of Ch 4 | Edit drift | Read seams in extracted text |
| ✓ ✗ ʊ not printing | Several chapters | Body font lacks the glyphs | Change text or font; `--source` glyph check |
| Picture-book density | 229 of 372 pages carried an image (~1 per 1.6 pages), while all technical diagrams were missing | Every page got art; argument pages got filler | 8–10 per chapter at section breaks; restore diagrams |
| Images omitted for review | 26 of 102 art anchors missing on 3 Oct 2026 `main` | Text passes deleted anchor sentences | Re-anchor via `art.json`; run the art audit after every text pass |
| Build passes, warnings ignored | pandoc warned about duplicate notes | Warnings not failing CI | Treat note and anchor warnings as failures for release builds |

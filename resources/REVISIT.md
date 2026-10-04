# Remaining editorial and production decisions

Repository housekeeping was applied on 27 September 2026. The current
[file inventory](FILE-INVENTORY.md) records what remains and the disposition of
retired files.

| Item | Remaining work |
| --- | --- |
| Chapter 2 technical figures | Recover original figures and data, or commission reviewed replacements. Since 30 September the ten absent figures are `DIAGRAM — missing figure` comments; the build tracks them and the reading edition no longer prints placeholders. See [missing figures](art-direction/missing-figures.md). |
| Chapter 5 visual directions | Seven briefs remain, including an opener request that conflicts with the selected opener and a glass-box concept already represented by a107. Reconcile before producing new art; see [backlog](art-direction/chapter-05-society-of-agents.md). |
| Chapter 5 Paged.js proof | Evaluate against the current chapter before adopting its composition across the book. |
| Front and back matter | A title page, copyright/ISBN page, dedication, acknowledgments and a decision on an index. None is in the manuscript. |
| Clearance | Employer communications/legal review: the author bio names Zalando, and Chapter 5 describes the author's work at Amazon. |
| Disclosure policy | Chapter 6 now uses an imagined online grocer, but Chapter 11 keeps identifying details (“outside Berlin”, “fashion retail”, `DE_mobile`, “Add to Bag”), Chapter 7’s store sells clothes and shoes, and the bio names the employer. Choose one policy and apply it to all of them, together with the clearance row above. |
| Chapter 6 references | Since the 4 October rewrite, Chapter 6 cites as plain `&#91;N&#93;` text, not linked `[N](appendix-references.md#ref-06-…)` citations. The 40 `ref-06-` appendix entries still follow the previous version; Frankfurt, for example, is cited but has no entry. The build’s reference check fails until the citations are linked and the appendix section is rebuilt in citation order. |
| Print production | Choose a printer; then set bleed, cover/spine geometry and output profile and obtain a physical proof. |
| Video production | The current 15 briefs have checked source hashes and section order. Bespoke shot choices and generated videos still need editorial review. |

## Completed

- 30 September: the author delegated the remaining manuscript decisions (see the copyedit log). The drafting markers were accepted, `SLOT 4` was removed, the unverifiable clauses were resolved, and the manuscript is proofread-ready.

- Removed obsolete upload workflows and the retired TeX helper.
- Made the back-cover utility use bundled fonts and visually checked its one-page output.
- Archived legacy opener references and old art directions; published a current asset register.
- Retired two competing video packs and generated one source-anchored pack with a freshness check.
- Repaired the Chapter 1 image and Chapter 4 photo links; recorded unrecovered Chapter 2 figures without fabricated substitutes.
- Retired the reader-map and objections drafts: their roles are fulfilled by the evidence appendix and Chapter 10.
- Shortened the root README and retained its editorial guidance in `editorial/working-spine.md`.
- Preserved current manuscript prose, selected artwork, LFS objects and historical evaluations.

Ignored PDF archives and build diagnostics are local recovery material. They are
not part of the push and have not been erased.

## Chapter 6: optional author material

The Ines thread is an explicitly imagined case. The earlier prompts for real author experiences remain optional; do not turn the fictional incidents into autobiography.

- A design pattern you watched being applied as a rule (formerly Slot 3, “The Pattern Goes to Work”).
- An experiment whose meaning was decided after the result came in (formerly Slot 1, “Commit the Test Before the Result”).
- What you believed before a result changed your mind (formerly Slot 2, “Change the Representation”).
- Optional Alexander close: verify the passage about the language as a gate in *The Timeless Way of Building*, “The Kernel of the Way,” before using it. The current chapter closes on Ines and hands the procedure to Chapter 7.

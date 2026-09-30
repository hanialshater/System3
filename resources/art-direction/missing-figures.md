# Chapter 2 and Chapter 5 figure register

The 27 September audit found ten missing legacy Chapter 2 files. The 30 September
art pass resolves those briefs and the seven Chapter 5 briefs in the curated
6×9 edition. Three briefs were already represented by existing artwork; twelve
native PDF diagrams and two new illustrations fill the remaining gaps.

“Resolved” means implemented and checked in the proof, not separately approved
by the author. Chapter prose and the fourteen cover/opening plates are preserved.
The original brief text remains in each chapter as an `ART RESOLVED` comment with
the exact asset ID. The renderer checks the corresponding placement anchors.

| Former file / brief | Resolution | Evidence or qualification |
| --- | --- | --- |
| image0135 — algorithm vortex | `ch2-vortex` | Nested search levels and an external fixed evaluator; placed at the concept’s explanation |
| image0138 — citrus packing | Existing `a018`, moved to the problem introduction | Preserves the established citrus, caliper and square illustration |
| image0139 — reference packing | `ch2-reference` | Exact published AlphaEvolve B.12 Construction 1 coordinates; 26 positive radii, all boundaries and 325 circle pairs checked without tolerance |
| image0136 — algorithm history | `ch2-search-roles` | Search roles replace an overly linear historical ladder; methods can coexist |
| image0140 — hill climbing | `ch2-hill` | Explicit 26-circle schematic derived by shrinking the reference radii; not recovered run snapshots |
| image0141 — crossover | `ch2-crossover` | Correct four-circle counterexample: reversed indexing sends all averaged centers to the square’s center |
| image0122 — evolutionary run | `ch2-evolution` | Chapter-reported endpoints, about 2.08 and 2.45; no invented generations or trajectory |
| image0123 — MAP-Elites | `ch2-archive` | Explicit schematic occupancy map; no fabricated quality scores |
| image0124 — AlphaEvolve | `ch2-alphaevolve` | Source-checked, simplified proposal / execution / evaluation / archive loop |
| image0125 — code evolution | `ch2-result` | Rounded chapter-reported values with explicit evidence limit, not a reconstructed run |
| Robot queue | Existing `a079` | Original selected illustration retained |
| Harness ladder | `ch5-harness` | Seven failure / response pairs, placed after CI has been introduced |
| Linux boss level | `ch5-linux-gate` | New editorial illustration; crowd is a visual metaphor, not an exact agent-count diagram |
| GCC oracle | `ch5-gcc` | Schematic shrinking failing subset; interaction caveat retained |
| Popper / three worlds | Existing `a083` | Original selected illustration retained |
| Outside designer | `ch5-outside-designer` | New diptych; preserves the separate Part III `a107` illustration |
| Seven jobs and an eighth | `ch5-institution` | Function map; revision arrow targets the institutional frame |

## Sources and reproducibility

- Exact coordinates, validation values and source hash:
  `book-design/curated/circle-packing-reference.json`.
- Source: [Google DeepMind’s mathematical-results notebook, B.12, Construction 1](https://github.com/google-deepmind/alphaevolve_results/blob/master/mathematical_results.ipynb).
- Architecture: [AlphaEvolve technical report](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/AlphaEvolve.pdf).
- Compiler harness: [Nicholas Carlini, Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler).
- The author’s original [agent-autonomy blog](https://www.hani-alshater.com/en/free-writing/agent-autonomy) supplied visual recovery leads. Its raster charts were not substituted for raw run data.
- Native diagrams and live labels: `book-design/curated/technical_figures.py`.
- New raster provenance and generation instructions: `book-design/curated/art-completion.json`.

The published reference sums to **2.6358627564136983**. The chapter’s rounded
2.635 reference and 2.636 best-run report cannot by themselves establish a new
record. Original experiment logs, evaluator versions and tolerances remain an
evidence issue, not an unfilled illustration slot. The new caption says so.

Build with `python book-design/pdf.py build --preview --strict-art` in the pinned
PDF environment. The build verifies manuscript and figure labels, embedded
fonts, page bounds, raster collisions and effective image resolution. Native
vector diagrams remain sharp without raster upscaling.

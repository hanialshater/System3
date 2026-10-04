# Easter-egg register

Seeds planted early that pay off later, mostly in the alternative ending. To an editor who does not know the payoff, every seed looks like a digression, so this register exists to be read **before** any edit pass touches the passages below.

`check-eggs.sh` in this folder checks the anchors after every edit pass. It **fails** only for confirmed seeds. Proposed seeds produce **warnings**: they are questions for the author, not constraints.

Anchors are pointers, not protected wording. Protect what the seed does. If an edit improves the wording and the seed still works, update the anchor in the same commit.

Status: **confirmed** = author has confirmed it is deliberate. **proposed** = found by a reader, author to confirm or delete.

| Thread | Planted (file → anchor) | Pays off (file → anchor) | Status |
|---|---|---|---|
| Coffee | `00-preface` → "Your coffee is still too hot." · `02` → "## The Coffee Test" · `10` → "## The Second Coffee Test" | `13` → "Decaf." | confirmed |
| The octopus | `01` → "octopuses: eight-armed problem-solvers" · `04` → "hyper-intelligent octopus" · `12` → "It requires an octopus" | `13` → "Hadn't the octopus dreamed it was love?" | proposed |
| The cable | `00-preface` → "at least one loose cable" · `04` → "taps an undersea cable" · `05` → "One of the culprits was a loose cable." | `13` → "Shark biting cables." | proposed |
| Tongue and ear | `04` → "*Can your tongue touch your ear?*" · Zen → "The tongue cannot reach the ear." | `13` → "But so would simulated fingers touching a simulated face." | proposed |
| DNA as a copier | `01` → "Do you bet on DNA, a biological fax machine" | `13` → "Your DNA is just a fax machine" | proposed |
| The camel | `04` → "consider a camel" | `11` → "And now the camel comes back" · `12` → "camels are native to Croatia" | proposed |
| The dream | `07` → "The Learner Dreams, and the Dream Can Be Wrong" | `13` → "hadn't he dreamed he was an octopus?" | proposed |
| The cathedral | `00-preface` → "Eventually there is a cathedral" | `03` → "A Cathedral on a Shopping Cart" | proposed |
| Standing outside the box | `05` → "with no one standing outside it" | `13` → "Behind it: forty monitors. Every timeline." | proposed |
| Capacity over power | `00-preface` → "Capacity over power." · `12` → "## Capacity Over Power" | `13` → "Capitalism doesn't." | proposed |
| The reveal riddle | `00-preface` → "we never thought to call it an architecture" | `reveal page` → "We call it science." | proposed |
| 11:53 PM | `12` → "In October 1947" (the Doomsday Clock was first set at seven minutes to midnight in 1947) | `13` → "11:53 PM, three minutes." | proposed — may be coincidence |
| Names | — | `13` → Devesh (roughly "lord of the gods"), Claudit (Claude + audit?), Norman (Don Norman's user?) | proposed — author to confirm |
| Reviewer 2 | `01` → "Reviewer 2" | `02` → "Reviewer 2" | confirmed (named in the evaluation prompt) |

## Rules for edit passes

1. Read this register before editing any file named in it.
2. Do not explain a payoff. The fable in Chapter 13 stays unexplained; the reader either catches the octopus or does not.
3. New material (part pages, interlude, divider pages) may plant seeds but must be added to this table when it does.
4. If an anchor has to change, update the table in the same commit.
5. Chapter 13 (`chapters/13-the-prophecy.md`) is protected in full. No edit pass, line edit or AI-tells fix touches it; only the author changes it. That includes typography: the file is the author's text of 21 September 2026 (commit `48fdb6b`), and `check-eggs.sh` fails if it changes. After an author edit, update `PROTECTED_CH13` in the script.

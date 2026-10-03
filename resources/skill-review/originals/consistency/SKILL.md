---
name: consistency
description: Keep a long manuscript consistent with itself — coinages defined once in their home chapter, thinkers introduced once and called back afterwards, one number for each count the book commits to, recurring ideas and examples living in one home, characters and names spelled one way, chapter titles and subtitles matching across files, README, references, evidence table and cover art, cross-references and antecedents that still point at something after edits. Maintains a book bible (JSON) and checks it after every pass. Use whenever the user asks for a consistency check, "does the book agree with itself", "cross-chapter", "collision", "introduced twice", "decide once, apply everywhere", after any structural or cutting pass, or before a proof.
---

# Consistency

The book disagreeing with itself is the error edits create most and readers notice fastest. Every case below happened in System 3:

- **A thinker introduced twice.** Ch 6 introduced Duhem–Quine, Lakatos and Kitcher as if for the first time after Ch 5 had met all three with cases attached. Fix: make Ch 6's versions callbacks ("Duhem again"), or keep the idea and drop the name.
- **An argument made four times.** The shared-source argument appeared in Ch 3, 5, 6 and 8.
- **A count that drifted.** Seven jobs vs eight verbs blurred in Ch 5 until the diagram fixed the count.
- **Arithmetic.** "Two centuries" that was three.
- **Orphans.** The Leavitt reference after its passage was cut; "the curator" and "the bargain" without antecedents; a dangling "Otherwise" — all left by cuts.
- **Titles.** The Ch 5 opener's subtitle differed from the body's; a chapter renamed while its cover lettering kept the old title; "Layer 4" against the chapter-number reference system.
- **Scope words.** "The rest of this chapter" that meant "the rest of this book"; "the rest of this book" that should have become "the next three chapters" once parts existed.
- **Front and back matter vs chapters.** A Zen maxim ("Ground every claim. Trace every source.") overstating Ch 4's "Not every sentence needs a dossier"; the preface's "appears to have been settled" stronger than Ch 6's note.
- **The same idea or example in several homes.** "The dangerous failure doesn't crash" (Ch 1, 3, 4), AlphaGo (Ch 1, 4), the diversity-sharing balance (Ch 2, 3), exploration methods (Preface, Ch 2, 3), the invented jacket (Ch 1 and its Ch 3 callback). Decide one home, apply everywhere.
- **One term, two scopes.** Ch 2 bolds "Immutable Harness"; Ch 3 bolds "harness" with a wider scope.
- **Characters planned and never used.** Mei and Sami were meant to recur; the store appears in Ch 7 and Ch 11 with no callback.

## The book bible

A JSON file in the repo (`resources/editorial/book-bible.json`; seed: `references/system3-bible.json`) with:
- **terms** — each coinage, its home chapter and variants.
- **people** — each thinker's home chapter and the introducing forms that should appear only there.
- **counts** — constructions the book commits to ("seven jobs", "eight verbs", "five layers").
- **repeats** — ideas and examples with an ID (X-1…), one home, and a decision note.
- **names** — canonical spellings with diacritics (Alpöge, Córdoba, Martínez-Zoroa).
Homes marked `?` are open decisions; list them for the author rather than choosing.

## Workflow

1. **Discover** (`scripts/check_bible.py chapters --discover`): terms bolded in several files, people introduced with a role word in several files, the same noun counted with different numbers. Turn real hits into bible entries.
2. **Check** (`scripts/check_bible.py chapters BIBLE --readme README.md --order book-order.json`): terms bolded outside home, variants, re-introductions, count mismatches, repeats outside home, name variants, title mismatches across the chapter H1, references headings, Note on Evidence and README, references to missing chapters, scope phrases to read.
3. **Read what the script can't:** antecedents near every cut (diff the pass and read each seam), claims in the Zen appendix and part pages against the chapters they quote, the preface against the chapters it previews, opener art lettering against titles (`book-design/curated/provenance.json`), and whether each callback still has something to call back to (dev-edit's `arc_map.py --recaps` finds near-verbatim repeats).
4. **Fix with the smallest change** — usually turning a second introduction into a callback, or deleting the repeat outside its home — flagged as usual. When the fix needs a decision (which home, which scope), list it in a cross-chapter table (`X-n | what | where | proposed home`) and don't apply it until the author decides.
5. **Update the bible in the same commit** whenever a term, home or count changes.

## Boundaries

Numbers against their sources belong to fresh-claims; recaps and re-teaching to dev-edit; spelling and typography to copyedit. This skill only asks whether the book agrees with itself.

## Files

- `scripts/check_bible.py` — discovery and checking.
- `references/system3-bible.json` — seed bible from past edits and the 2 Oct cross-chapter list.

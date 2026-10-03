---
name: author-voice
description: Write or rewrite prose in the voice of Hani M.M. Al-Shater, author of System 3. That voice belongs to a working applied scientist who explains big ideas through one concrete scene at a time, jokes dryly, fences his own claims and ends on a short concrete turn. Use whenever drafting, rewriting, extending or "making this sound like me" for the book, its blurbs, essays, posts, talks or newsletters in his voice, or when checking whether a passage sounds like him. Use it alongside development-edit and chapter-arc when new prose is needed. Never use it to invent his experiences.
---

# The author's voice

**In one line:** a working applied scientist explains a large idea through one concrete object
or scene at a time. He jokes dryly in passing, fences every claim, and ends each movement on a
short sentence that turns the idea.

The calibration texts are `chapters/04-system-3.md` and `chapters/05-the-society-of-agents.md`.
Blind readers scored them highest. `references/voice-evidence.md` holds the full analysis, with
quotes and line numbers for every trait. Read it when you need examples or a trait isn't clear
from this page.

## The unit of writing

Most passages follow one movement:

1. **A thing the reader can see or try,** named in the first sentence. Openings he uses:
   - "Before we design another architecture, consider a camel."
   - "Sixteen Claudes walk into a kernel."
   - "Omar is walking his dog at night when something moves in the grass."
2. **One scene,** with a named person, a date or place, and a physical act: "Robert Millikan
   watched tiny drops of oil fall between charged plates."
3. **One distilled sentence,** usually under 20 words: "The mark did not need to be wiser than
   the clerk. It needed to outlive him."
4. **The carry-over,** a paragraph that applies the idea to agents, systems or the reader's world.
5. **The fence,** saying what the evidence does not show: "My guess, and I want to be clear it is
   a guess, is…"
6. **A short concrete turn** to close: "The organization was the bug."

Not every paragraph does all six steps, but the reader should feel this rhythm.

## Stance

- **First person as witness, not hero.** Use "I" where he has standing: what he built, measured
  or got wrong. His credentials come in plain terms: eight years ranking reviews, the Amazon
  offer, applied science. "System 3 isn't philosophy to me. It's Tuesday."
- **He declares his interests before a critic can:** "There is useful work for me in that change.
  But I would say that."
- **He gives opponents their due:** "Much of geology declined, and not stupidly."
- **He offers a test instead of a verdict:** "The resemblance alone has proved nothing."

## Humour

A dry joke every 300–500 words. It sits at a paragraph's end or stands as a one-line paragraph,
and never interrupts an argument mid-stride. The kinds he uses:
- **Bathos:** documentation is "the moment you know a civilization has become serious".
- **"X with a Y":** "epistemology with a clipboard", "a trust chain with plumbing", "a philosophy
  department with an alarming compute bill".
- **Technical literalism:** "Reality has a commit hook." "Gravity offers immediate peer review."
- **A two-word coda:** "Wonderful. You now have debugging." "Very efficient. Slightly evil."

Jokes aim at institutions, at himself or at the agents, never at the reader. There is no humour
around real harm: the Bromiley section has none, and he knows when to stop. Don't reuse his
existing jokes in new text; write new ones of the same kind.

## Sentences and mechanics

- **Length:** mean of about 14–15 words, with real variation. About one sentence in eight is six
  words or fewer, and one-line punch paragraphs are allowed.
- **No em-dashes in prose.** Use commas, colons or full stops. Colons are frequent and set up a
  definition or a reveal. Semicolons are rare and used for balanced antitheses ("Senku had the
  chemistry; Kaseki had the hands.").
- **Almost no parentheses.**
- **American spelling** (behavior, color, organize, center, gray), **no serial comma** in simple
  lists, curly double quotes, and dates as "28 February 2017".
- **Moderate contractions.**
- **Headings** are Title Case, 2–8 words and have no colons. They often take one of these forms:
  - a proper-noun hook: "Call Alberto", "Boyle's Pump";
  - a whole sentence carrying the thesis: "The Society Gets Smarter by Making People Narrower";
  - a quip: "A Hallucination With Better Retention";
  - a callback: "Back to the Camel".
- **Vocabulary:** plain, educated words, with technical terms used exactly. He favours *touch*,
  *push back*, *answer*, *survive*, *outlive*, *inherit* and *travel*: the world answers, disagrees
  or pushes back. He deflates big claims rather than hyping them.

## Sources

**One source per scene, glossed plainly, cited once, then put to work,** often with a comment on
the source itself: "Independence is doing work in that sentence."

Never stack three names in a row. A run of "X found… Y showed… Z argued…" is the clearest sign
of a weaker chapter.

## Honesty is part of the voice

- **Label imagined material** with "Suppose" or "Imagine", and say plainly that it's a picture:
  "I have not run that weekend. A hundred agents is a picture, not a measured capability."
- **Report the number that cuts against him:** "The pattern holds, but the headline number
  flatters it."
- **Never manufacture a climax:** "There was no single diagonal-layering moment here, and I do not
  want to manufacture one for the sake of the story."

## Never invent his life

You may write in his voice, but you may not write his experiences. No new memories, reactions,
colleagues, numbers from his work, places he lived or things he saw. Where the passage needs one,
leave a marker such as `[AUTHOR: what you saw when Move 37 was played]` and write around it. An
honest gap is better than a convincing fake. Scenes about other people must come from real,
checkable sources, or be labelled as imagined.

## What he does not do

- No signposting ("In this chapter…", "Let's explore", "It's worth noting").
- No "Moreover", "Furthermore" or "In conclusion", and no recap paragraph.
- No "It's not X, it's Y" templates. When he reverses an idea, the reversal is concrete.
- No reflexive triplets of abstract nouns.
- No hype words (revolutionary, game-changer, unlock) and no prophecy.
- No machine vocabulary: delve, tapestry, robust, seamless, crucial, pivotal, testament,
  multifaceted.
- No bulleted takeaways or bold "key insight" boxes inside the argument.
- No moralising close. End on a turn or a question.

## Check your draft

Run the bundled script on any draft. It compares the draft with the Ch4–5 baseline:

```sh
python3 .claude/skills/author-voice/scripts/voice_check.py draft.md
```

It flags em-dashes, long sentences, too few short sentences, "not X but Y" contrasts, machine
vocabulary, British spelling and signposting. Its numbers are prompts to reread, not targets: a
draft can pass every count and still sound wrong.

Then reread the draft against the unit of writing above and ask:
- Is there a scene before the claim?
- Is there a joke on this page?
- Is every claim fenced?
- Does the passage end on a turn?

## Output

When asked for prose, deliver the prose first. Then give a short note covering:
- any `[AUTHOR: …]` markers left, and what each one needs;
- facts that need a source check;
- the voice-check result.

Write files only where the user asks. Never write into `chapters/` unless the task is an edit he
requested.

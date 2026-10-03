---
name: development-edit
description: Run a development (structural) edit on a chapter or the whole System 3 book the way its author works, by evaluating it against his rubric, blind-reading against the strongest chapters, proposing arc and scene changes, then editing in focused passes with a cut log he can revert. Use whenever the author asks to evaluate, score, fix, restructure, tighten or "improve" a chapter, asks how far a chapter is from publishable, asks for a blind read, or wants a pass on narrative momentum, arc or human feel, even if he doesn't say "development edit". Not for line-level AI-tell sweeps alone (use ai-tells) or video prompts (use video-briefs).
---

# Development edit, the author's way

A development edit changes what a chapter does: its arc, its scenes, its argument and its
momentum. Line polish comes later. This author has strong views on how it should go, learned
over a year of drafting and several rounds of edits that went wrong. The steps below encode them.

## The rubric (what "good" means here)

This is a synthesis book of ideas, stories and philosophy. Do not judge it like an
empirical monograph or ask for full evidence everywhere. Score it on the author's rubric:

| Dimension | Question |
|---|---|
| Provocative ideas | Does it say something a smart reader would argue with? |
| Big ideas | Does it change how the reader sees the field? |
| Learn something new | Does the reader leave with a fact, mechanism or story they didn't have? |
| Thinks philosophically | Does it raise a question about knowledge, trust, agency or wanting? |
| Fun to read | Jokes, surprise, delight |
| Narrative momentum | Does each section make you want the next? |
| Prose | Clear, varied, concrete |
| Voice and identity | Could only this author have written it? |
| Reads as human | Free of machine tells (see the `ai-tells` skill) |

The calibration baseline is **Chapters 4 and 5** (blind readers scored them 8–8.5). Their
strength comes from scenes the author lived: the camel, Alberto, his mother's school, his own
failed experiment, the Amazon offer. Judge every other chapter against that, not against an
abstract standard.

## Step 1: Learn the intent before touching anything

Ask, or find in the conversation, what the author wants the chapter to do. He usually has a
clear arc in mind:
- Ch9: from the crisis, to what is left in the seat, to what we want when AI can do things for us.
- Ch8: a technical alignment chapter, not rules of thumb.

His intent beats your diagnosis. If you think the intended arc is weak, say so once, with
reasons, and then serve his choice.

Collect the constraints:
- lines he has required (for example the Ch9 vibe-coder sentence);
- the seed register (`resources/editorial/easter-egg-register.md`);
- protected chapters (Chapter 13 is protected in full);
- the evidence note (`chapters/appendix-note-on-evidence.md`), which says what is lived, reported or imagined.

## Step 2: Evaluate honestly

1. Read the whole chapter.
2. Score it on the rubric, overall and section by section. Name the three biggest problems.
3. **Use a blind reader rather than your own judgment for scores.** Self-grading runs high: in
   this project self-estimates of 8.6 came back as 7.0–7.4 from blind readers. Spawn a subagent
   that has not seen your edits. Give it Chapter 4 as the baseline plus the target chapter, and
   ask for:
   - scores for reads-as-human, engagement, momentum, prose, voice and overall;
   - per-section scores;
   - 6 concrete fixes;
   - what still separates the chapter from the baseline.
4. Separate line problems (fixable by editing) from **ownership problems**, which only the
   author can fix: a missing lived scene, a real number, his own reaction to an event. Line
   editing alone tops out at around 7.5. The gap above that is almost always ownership.

## Step 3: Propose before editing

Before changing text, give the author:
- the proposed arc, as a short list of sections with what each one does;
- which scenes carry it, and which of them need his material;
- the expected score change, stated honestly (for example "7.0 to about 7.5 with line work; 8+ needs your scene");
- what will be cut, and what that costs.

Wait for his go on structural changes.

## Step 4: Edit in focused passes

- **One section or one problem per pass.** After each pass, re-run a blind read on that section.
  Iterate until it approaches the baseline or stops improving.
- **Lead with scenes.** Open on an incident, an object or a person rather than a thesis. Bring a
  source in through the scene, and use one source per point rather than a tour of papers.
- **Never invent autobiography.** Don't add experiences, numbers, quotes or reactions the author
  didn't supply. Where his material is needed, leave an `<!-- AUTHOR: what is needed -->`
  comment. Invented examples are allowed only when clearly labelled as imagined ("write Mallorca
  as imagined").
- **Verify new facts.** New reported material, such as a historical event or a paper, needs a
  real source checked before it goes in, plus a reference entry.
- **Give each story one home.** When an example recurs, tell it fully in one place and use short
  callbacks elsewhere, each adding something. A story mentioned in many places and told in none
  is the failure to avoid.

## Step 5: Protect the voice while cutting

These lessons are hard-won. An automated pass once cut dozens of lines the author then asked
back.
- **Jokes are protected.** "Epistemology with a clipboard" and "a trust chain with plumbing" are
  not maxims to trim.
- **Rewrite callbacks, don't delete them.** Replace "Chapter 5 argued…" with an image the reader
  can recognise ("sixteen Claudes building a compiler…"). Don't remove the link.
- **Cut a short paragraph-ending line only if it repeats the sentence right before it.** A line
  that adds a turn, an image or the next step of the argument stays.
- **Never edit to hit a number.** Checker counts are flags for attention, not targets.
- Keep coined terms that earn their place (Gut/Head/Hand, Surface Value). Cut only the ones that
  don't.
- Never cut a sentence that something else depends on: a Zen appendix line, a later callback,
  the evidence note, a term used later. Grep before cutting.

## Step 6: Approval modes and the cut log

- Respect the author's split. Some chapters he approves line by line, others he lets you fix.
  Ask if it is unclear. **Protected chapters get proposals only.**
- Keep a **cut log** for every pass, recording each removed or materially changed passage that
  carried something:
  `ID | chapter | exact text | what it carried | risk (high/med/low)`
- After the pass, show the cuts grouped by reason, with your recommendation for each, so he can
  revert some. Never present only the gains.
- When restoring, put text back in its original place and smooth the seams. Never re-add something
  his own later edit deliberately removed.

## Step 7: Finish cleanly

1. Rebuild references if citations changed.
2. Regenerate the video briefs: `python3 prompts/build_notebooklm.py`.
3. Run the seed check: `bash resources/editorial/check-eggs.sh`.
4. Commit with a message that names what changed and why.
5. If the author pushed edits meanwhile, merge them, and wherever both of you touched the same
   passage, his wording wins. Verify that every line he added survives the merge.

## Report format

Tables first, then prose. For an evaluation:

| Dimension | Score | Evidence (quote or section) |
|---|---|---|

Then give:
- the three biggest problems;
- the fixes that are line edits;
- the fixes that need the author, phrased as specific questions ("What did the prototype actually show on the first day?").

For an edit pass, report:
- what changed, by section;
- before and after blind-read scores;
- the cut log;
- any AUTHOR comments left.

Related skills: `chapter-arc` (shape of a chapter), `book-arc` (shape of the book),
`author-voice` (how the prose should sound), `ai-tells` (line-level machine patterns).

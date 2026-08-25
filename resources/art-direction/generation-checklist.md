# Chapter Art Generation Checklist

Use this before every new chapter-opener generation or edit.

The purpose is to prevent the recurring failure mode where a good chapter-specific concept drifts into generic AI / fantasy / infographic art.

## 1. Start from the benchmark, not from a generic style prompt

Reference:

`resources/chapter-openers/chapter-11-capacity-over-power.jpg`

Ask first:

- Is the canvas **2:3 portrait**?
- Is the background warm cream paper?
- Is the palette restrained blue / ochre / olive / warm gray?
- Is the title area quiet and spacious?
- Does the scene have one dominant idea?
- Does it look like literary watercolor illustration rather than concept art?

If any answer is no, fix that before adding chapter-specific content.

## 2. First sentence of every generation brief

Use wording equivalent to:

> **One standalone 2:3 portrait book chapter opener on warm cream watercolor paper, matching the established System 3 Chapter 11 illustration language; not a grid, collage, poster sheet, landscape image, infographic, or fantasy concept-art scene.**

This constraint should appear before the chapter concept.

## 3. Lock the exact chapter text

Before generation, copy the title / subtitle from the current manuscript.

Do not let an image model invent:

- alternate titles;
- alternate subtitles;
- quotes;
- slogans;
- chapter summaries;
- labels;
- “helpful” explanatory text.

If a chapter-specific quote is deliberately part of the art direction, specify it exactly.

## 4. State the philosophical image in one sentence

If the concept cannot be compressed into one sentence, it is probably too busy.

Examples:

- Chapter 1: a human releases a few simple agents and their independent motion becomes a much larger emergent form.
- Chapter 3: an inquiry sits at the center while different agents perform different kinds of cognition and the next move remains open.
- Chapter 5: a differentiated robot society works beneath an old scientific tower and a pale future eclipse.
- Chapter 8: a human and AI stand side by side before multiple possible futures, with neither choosing for the other.
- Chapter 11: a human opens doors into expanded human possibility.

## 5. Limit visual nouns

For a normal opener, aim for:

- **1 primary metaphor**;
- **1 primary focal point**;
- **3–7 meaningful secondary actors / objects** maximum;
- **0 explanatory cards** unless the chapter art direction explicitly requires them.

Do not solve weak concept clarity by adding more objects.

## 6. Robot count and behavior

Robots are not decoration.

Each visible robot should justify its existence through a distinct action, position, or relationship.

Prefer 4–7 differentiated agents over 20 identical mascots.

Useful actions include:

- reading;
- observing through an instrument;
- building;
- testing;
- recording;
- challenging / comparing;
- carrying an artifact between places.

## 7. Text-clutter test

Default opener text:

- chapter number;
- title;
- subtitle.

Anything else must earn its place.

Allowed exceptions:

- Chapter 3's short Deep Mode quote;
- Chapter 4's seven-claims evidence experiment.

Do not add:

- “what this chapter builds”;
- bullet lists;
- signs explaining the metaphor;
- fake sticky notes;
- invented mottos;
- captions explaining the obvious.

## 8. Color / tone guardrails

Reject or revise if the image drifts toward:

- dark cinematic fantasy;
- black / gold epic concept art;
- cyberpunk;
- glowing portals;
- saturated orange-and-teal grading;
- glossy 3D robots;
- digital poster aesthetics;
- photoreal fantasy matte painting.

Desired tone:

- warm;
- curious;
- slightly whimsical;
- intellectually serious;
- handmade;
- hopeful without becoming utopian advertising.

## 9. Aspect-ratio test

Final chapter page is **2:3 portrait**.

Do not accept a beautiful concept in the wrong ratio as final art.

Landscape and square generations are exploration only.

## 10. Thumbnail test

Shrink the page mentally to a small thumbnail.

Can you still answer:

- What is the main shape?
- Where does the eye go first?
- What is the one metaphor?

If the answer is “there are many cool details,” simplify.

## 11. Chapter-specificity test

Ask:

> Could this exact image plausibly open three other AI books?

If yes, reject it.

Generic failures we have already seen:

- person staring at mountains = “deep thought” but not Deep Mode;
- generic recommendation vortex = not Algorithm Vortex;
- robots crossing a bridge = “trust” but not System 3;
- fantasy academy = “society” but not Society of Agents;
- robot repairing its own chest = generic self-modification, not the chapter's scaffold-level recursive improvement.

## 12. Delayed-meaning test

Best openers have two readings:

**Before the chapter:** the image is emotionally / visually compelling.

**After the chapter:** a second meaning clicks into place.

Examples:

- Chapter 5: the reader later realizes the distant tower represented science.
- Chapter 2: the reader later notices the boundary stayed fixed while the search inside it changed.
- Chapter 6: the old dusty rule becomes the danger of inherited culture becoming ritual.

Prefer this over explanatory symbolism.

## 13. Edit before regenerating when the concept is right

If an image has the right composition and soul but too much clutter, **edit / simplify the existing image** rather than inventing a new metaphor.

Typical surgical edits:

- remove labels;
- reduce robots;
- remove footer prose;
- enlarge negative space;
- correct title / subtitle;
- soften saturation;
- replace generic prop with chapter-specific prop;
- restore a source photograph without changing it.

Do not throw away a strong visual idea because one rendering pass became busy.

## 14. Photo integrity rule

When a chapter uses a real photograph as evidence, the photograph is not a style reference — it is an epistemic object.

Do not:

- redraw it;
- reconstruct it with an image model;
- beautify faces;
- add or remove people / animals / accessories;
- alter background details;
- replace it with a visually similar synthetic photo.

Use the exact source image and design *around* it.

This matters especially for Chapter 4, where one of the claims concerns whether the photograph is real / unedited.

## 15. Acceptance rubric

Score every candidate 1–10 on:

| Dimension | Question |
|---|---|
| **Concept fidelity** | Does it capture the actual chapter turn, not only the title? |
| **Aesthetic level** | Would this look intentional in a professionally illustrated literary book? |
| **Style match** | Does it belong beside the Chapter 11 benchmark? |
| **Clarity** | Can the dominant metaphor be read without explanation? |
| **Specificity** | Could this image belong only to this chapter / book? |
| **Restraint** | Is every object / word earning its place? |
| **Delayed meaning** | Does the image gain a second reading after the chapter? |

A final opener should normally score **9+ on concept fidelity, style match, and restraint** before it is considered locked.

## 16. Final pre-commit check

Before committing an image to `resources/chapter-openers/`:

- [ ] 2:3 portrait.
- [ ] Exact chapter number / title / subtitle.
- [ ] Correct cream-paper / muted watercolor visual language.
- [ ] No accidental invented text.
- [ ] No generic AI / fantasy drift.
- [ ] No unnecessary explanatory clutter.
- [ ] Main metaphor matches the chapter.
- [ ] Reviewed against Chapter 11 at side-by-side size.
- [ ] Reviewed at thumbnail size.
- [ ] If using a source photo, the photo itself is untouched.

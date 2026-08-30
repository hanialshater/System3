# Art Generation Jobs — Fluent Autonomy (Chapter 10)

Generated from `book-design/manifests/chapter-10.json`. For each job below:

1. Generate the image per prompt.
2. Save it EXACTLY as `book-design/art/ch10/<slot-id>.png` (path is the contract —
   the renderer picks files up by name; nothing else to wire).
3. Commit. The next `python3 book-design/render.py 10` places it on the page.

Do not put readable text inside any image except opener-plate hand lettering.
Jobs marked AUTHOR DATA FIGURE or DIAGRAM are not generation jobs — skip them.


## Job: opener  →  `art/ch10/opener.png`

**Geometry.** Full chapter opener, 2:3 portrait (e.g. 1600x2400px). Title area occupies the upper 20-30% with hand lettering AS SPECIFIED in the brief (this is the one slot type allowed lettering: small blue 'CHAPTER N', large black brush title, blue subtitle). Illustration owns the rest. Generous margins and paper.

**Scene.** REGENERATE OPENER: existing asset carries stale numbering/title (STALE ASSET: art carries old numbering (Chapter 9). Regeneration job in art-prompts; draft uses it for palette continuity.). Produce the opener for CHAPTER 10 — 'Fluent Autonomy' / 'When the Architecture Gets Out of the Way' — keeping the existing asset's core visual idea and palette.

**Style (mandatory, from resources/art-direction/): warm cream paper with
visible grain; restrained watercolor with fine ink contours; muted Prussian/denim
blue, ochre, warm gray, olive, parchment; visible blooms, imperfect ink, soft
edges. Literary illustration — NOT slideware, fantasy concept art, cyberpunk,
sci-fi glow, 3D render, or glossy AI imagery. Robots, when present, are small
hand-built storybook machines (cream/brass/gray-blue, simple dark expressive
eyes), physically engaged in work — never product mascots, never crowds of
identical robots. Humans are ordinary and embodied, often from behind or
three-quarter view. One dominant idea per image; small details that reward
rereading. Absolutely no readable text, labels, signs, UI, or diagram arrows
inside the artwork (illegible incidental scribbles are fine).**


## Job: small-sentence  →  `art/ch10/small-sentence.png`

**Geometry.** Landscape-ish scene around 1400x1000px, composition weighted toward one corner; the two outward edges may run dense, the two inward edges must dissolve into plain cream paper (the page wraps text around this art). No hard rectangular border.

**Scene.** Corner scene: one small handwritten sentence on a slip of paper at the top; beneath the floorboards it rests on, a vast cutaway of quiet machinery — archives, messengers, little laboratories — assembling itself around the sentence's weight. The surface stays calm.

**Style (mandatory, from resources/art-direction/): warm cream paper with
visible grain; restrained watercolor with fine ink contours; muted Prussian/denim
blue, ochre, warm gray, olive, parchment; visible blooms, imperfect ink, soft
edges. Literary illustration — NOT slideware, fantasy concept art, cyberpunk,
sci-fi glow, 3D render, or glossy AI imagery. Robots, when present, are small
hand-built storybook machines (cream/brass/gray-blue, simple dark expressive
eyes), physically engaged in work — never product mascots, never crowds of
identical robots. Humans are ordinary and embodied, often from behind or
three-quarter view. One dominant idea per image; small details that reward
rereading. Absolutely no readable text, labels, signs, UI, or diagram arrows
inside the artwork (illegible incidental scribbles are fine).**


## Job: origami-bureau  →  `art/ch10/origami-bureau.png`

**Geometry.** Portrait-ish vignette around 900x1100px, single subject, all edges dissolving softly into plain cream paper. Reads clearly at 4cm tall.

**Scene.** Margin vignette: a small government office unfolding out of flat paper like origami around a single problem on a desk — one clerk window, one stamp, one archive drawer — clearly designed to fold away again when done.

**Style (mandatory, from resources/art-direction/): warm cream paper with
visible grain; restrained watercolor with fine ink contours; muted Prussian/denim
blue, ochre, warm gray, olive, parchment; visible blooms, imperfect ink, soft
edges. Literary illustration — NOT slideware, fantasy concept art, cyberpunk,
sci-fi glow, 3D render, or glossy AI imagery. Robots, when present, are small
hand-built storybook machines (cream/brass/gray-blue, simple dark expressive
eyes), physically engaged in work — never product mascots, never crowds of
identical robots. Humans are ordinary and embodied, often from behind or
three-quarter view. One dominant idea per image; small details that reward
rereading. Absolutely no readable text, labels, signs, UI, or diagram arrows
inside the artwork (illegible incidental scribbles are fine).**


## Job: friction  →  `art/ch10/friction.png`

**Geometry.** Small isolated spot around 1000x750px, one object or micro-scene centered on plain cream, soft vignetted edges. Reads clearly at 3cm.

**Scene.** Small spot: a hand resting with deliberate pleasure on a large, satisfying brake lever; behind it, a chute of outgoing money frozen mid-air. Relief as comedy.

**Style (mandatory, from resources/art-direction/): warm cream paper with
visible grain; restrained watercolor with fine ink contours; muted Prussian/denim
blue, ochre, warm gray, olive, parchment; visible blooms, imperfect ink, soft
edges. Literary illustration — NOT slideware, fantasy concept art, cyberpunk,
sci-fi glow, 3D render, or glossy AI imagery. Robots, when present, are small
hand-built storybook machines (cream/brass/gray-blue, simple dark expressive
eyes), physically engaged in work — never product mascots, never crowds of
identical robots. Humans are ordinary and embodied, often from behind or
three-quarter view. One dominant idea per image; small details that reward
rereading. Absolutely no readable text, labels, signs, UI, or diagram arrows
inside the artwork (illegible incidental scribbles are fine).**

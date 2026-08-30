#!/usr/bin/env python3
"""Compile art-slot briefs from the manifests into generation-ready prompt
files for an external image model (synced via git).

Usage: python3 book-design/export_prompts.py
Writes book-design/art-prompts/chapter-NN.md + README.md.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAN = ROOT / "book-design" / "manifests"
OUT = ROOT / "book-design" / "art-prompts"

STYLE = """Style (mandatory, from resources/art-direction/): warm cream paper with
visible grain; restrained watercolor with fine ink contours; muted Prussian/denim
blue, ochre, warm gray, olive, parchment; visible blooms, imperfect ink, soft
edges. Literary illustration — NOT slideware, fantasy concept art, cyberpunk,
sci-fi glow, 3D render, or glossy AI imagery. Robots, when present, are small
hand-built storybook machines (cream/brass/gray-blue, simple dark expressive
eyes), physically engaged in work — never product mascots, never crowds of
identical robots. Humans are ordinary and embodied, often from behind or
three-quarter view. One dominant idea per image; small details that reward
rereading. Absolutely no readable text, labels, signs, UI, or diagram arrows
inside the artwork (illegible incidental scribbles are fine)."""

GEOMETRY = {
    "opener-plate": "Full chapter opener, 2:3 portrait (e.g. 1600x2400px). Title area occupies the upper 20-30% with hand lettering AS SPECIFIED in the brief (this is the one slot type allowed lettering: small blue 'CHAPTER N', large black brush title, blue subtitle). Illustration owns the rest. Generous margins and paper.",
    "corner-bleed": "Landscape-ish scene around 1400x1000px, composition weighted toward one corner; the two outward edges may run dense, the two inward edges must dissolve into plain cream paper (the page wraps text around this art). No hard rectangular border.",
    "margin-vignette": "Portrait-ish vignette around 900x1100px, single subject, all edges dissolving softly into plain cream paper. Reads clearly at 4cm tall.",
    "spot": "Small isolated spot around 1000x750px, one object or micro-scene centered on plain cream, soft vignetted edges. Reads clearly at 3cm.",
    "figure-frame": "Rectangular plate around 1600x1200px, full-bleed inside its frame; the page adds the frame and typeset caption.",
}

HEADER = """# Art Generation Jobs — {title} (Chapter {n})

Generated from `book-design/manifests/chapter-{n:02d}.json`. For each job below:

1. Generate the image per prompt.
2. Save it EXACTLY as `book-design/art/ch{n:02d}/<slot-id>.png` (path is the contract —
   the renderer picks files up by name; nothing else to wire).
3. Commit. The next `python3 book-design/render.py {n}` places it on the page.

Do not put readable text inside any image except opener-plate hand lettering.
Jobs marked AUTHOR DATA FIGURE or DIAGRAM are not generation jobs — skip them.
"""


def main():
    OUT.mkdir(exist_ok=True)
    index = []
    for mf in sorted(MAN.glob("chapter-*.json")):
        man = json.loads(mf.read_text())
        n = man["chapter"]
        lines = [HEADER.format(title=man["title"], n=n)]
        jobs = 0
        if not man.get("opener_art") or man.get("opener_note"):
            brief = man.get("opener_brief") or (
                f"REGENERATE OPENER: existing asset carries stale numbering/title "
                f"({man.get('opener_note','')}). Produce the opener for CHAPTER {n} "
                f"— '{man['title']}' / '{man['subtitle']}' — keeping the existing "
                f"asset's core visual idea and palette.")
            lines += [f"\n## Job: opener  →  `art/ch{n:02d}/opener.png`\n",
                      f"**Geometry.** {GEOMETRY['opener-plate']}\n",
                      f"**Scene.** {brief}\n", f"**{STYLE}**\n"]
            jobs += 1
        for slot in man["slots"]:
            if slot["type"] == "pull-quote":
                continue
            b = slot.get("brief", "")
            if b.startswith(("AUTHOR DATA FIGURE", "DIAGRAM")):
                lines += [f"\n## (skip) {slot['id']} — {b.split(':')[0]}\n"]
                continue
            lines += [f"\n## Job: {slot['id']}  →  `art/ch{n:02d}/{slot['id']}.png`\n",
                      f"**Geometry.** {GEOMETRY[slot['type']]}\n",
                      f"**Scene.** {b}\n", f"**{STYLE}**\n"]
            jobs += 1
        (OUT / f"chapter-{n:02d}.md").write_text("\n".join(lines))
        index.append(f"- [Chapter {n} — {man['title']}](chapter-{n:02d}.md): {jobs} jobs")
        print(f"chapter {n:02d}: {jobs} generation jobs")

    (OUT / "README.md").write_text(
        "# Art Prompts — generation queue\n\n"
        "One file per chapter; each job is a self-contained prompt for an external\n"
        "image model. The return contract is the file path in each job's heading:\n"
        "save the image there, commit, and the renderer picks it up by name on the\n"
        "next `python3 book-design/render.py all`. See `../PIPELINE.md`.\n\n"
        "Priority: chapter 8 and 13 openers (no asset exists), then the stale\n"
        "renumbered openers (chapters 9, 10, 11 — chapter 12's is an open editorial\n"
        "decision, ask before regenerating), then interior slots front to back.\n\n"
        + "\n".join(index) + "\n")


if __name__ == "__main__":
    main()

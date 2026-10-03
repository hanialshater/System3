#!/usr/bin/env python3
"""Mechanical QA of a built book PDF. Complements, never replaces, looking at pages.

  proof_qa.py BOOK.pdf [--source CHAPTER_DIR] [--render 12,45,92] [--out qa/]

Checks per page: text that shouldn't print (comment fragments, ASSISTANT/CLAUDE/AUTHOR/SLOT
markers, [Missing figure], VISUAL/DIAGRAM briefs, raw LaTeX, Markdown residue), garbage
running headers (short glyph runs like "V}}}}V"), captions with no image on the page,
duplicated page text, image density (pages with images / total), straight quotes in prose,
and fonts not embedded. With --source, also lists glyphs used in the manuscript that never
appear in the PDF's extracted text (e.g. ✓ ✗ ʊ dropped by a font). --render writes PNGs of
chosen pages for visual review.
"""
import argparse, collections, hashlib, re, subprocess
from pathlib import Path
import pdfplumber

LEAKS = r"(<!--|-->|ASSISTANT (EDIT|DRAFT)|CLAUDE (DRAFT|EDIT)|AUTHOR:|SLOT ?\d|\[Missing figure\]|\bVISUAL\b ?[—-]|\bDIAGRAM\b ?[—-]|\\(vspace|clearpage|textheight|LARGE|begin\{)|\*\*\w|^#{1,4} |\[\^)"
CAPTION = r"^\s*(\*?Figure \d+|Fig\. ?\d+)"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf"); ap.add_argument("--source"); ap.add_argument("--render", default=""); ap.add_argument("--out", default="qa")
    a = ap.parse_args()
    issues = collections.defaultdict(list); seen = {}; img_pages = 0; text_all = []
    with pdfplumber.open(a.pdf) as pdf:
        n = len(pdf.pages)
        for i, p in enumerate(pdf.pages, 1):
            t = p.extract_text() or ""; text_all.append(t)
            lines = [l for l in t.splitlines() if l.strip()]
            if p.images: img_pages += 1
            for l in lines:
                if re.search(LEAKS, l): issues["leak"].append((i, l[:100]))
                if re.search(CAPTION, l) and not p.images: issues["caption without image"].append((i, l[:80]))
            for l in (lines[:1] + lines[-1:]):
                s = l.strip()
                if 1 <= len(s) <= 20 and re.fullmatch(r"[^\w\s]*\w?[^\w\s]{2,}\w?", s):
                    issues["garbage header/footer"].append((i, s))
            body = " ".join(lines[1:-1])
            if len(body) > 300:
                h = hashlib.md5(body.encode()).hexdigest()
                if h in seen: issues["duplicate page text"].append((i, f"same as p{seen[h]}"))
                else: seen[h] = i
            sq = len(re.findall(r"[A-Za-z]'[A-Za-z]|\"[A-Za-z]", body))
            if sq > 3: issues["straight quotes"].append((i, f"{sq} on page"))
    fonts = subprocess.run(["pdffonts", a.pdf], capture_output=True, text=True).stdout.splitlines()[2:]
    for f in fonts:
        cols = f.split()
        if len(cols) > 4 and "no" in cols[-5:-3]:
            issues["font not embedded"].append((0, f.strip()))
    if a.source:
        src = "".join(p.read_text(encoding="utf-8") for p in Path(a.source).glob("*.md"))
        src = re.sub(r"<!--.*?-->|```.*?```", "", src, flags=re.S)
        pdf_chars = set("".join(text_all))
        rare = {c for c in set(src) if ord(c) > 0x024F and c not in pdf_chars and not c.isspace()}
        for c in sorted(rare): issues["glyph in source, missing in PDF"].append((0, f"{c} U+{ord(c):04X} ×{src.count(c)}"))
    print(f"pages {n}; pages with images {img_pages} ({img_pages / n:.0%})")
    for k, v in issues.items():
        print(f"\n== {k} ({len(v)})")
        for pg, s in v[:25]: print(f"  p{pg}: {s}" if pg else f"  {s}")
    if a.render:
        Path(a.out).mkdir(exist_ok=True)
        for pg in [int(x) for x in a.render.split(",") if x]:
            subprocess.run(["pdftoppm", "-f", str(pg), "-l", str(pg), "-r", "70", "-png", a.pdf, f"{a.out}/p{pg}"])
        print(f"\nrendered to {a.out}/ — look at them")

if __name__ == "__main__":
    main()

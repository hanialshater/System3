#!/usr/bin/env python3
"""Audit interior art placement against the manuscript (mirrors the curated renderer).

  art_audit.py ART_JSON CHAPTER_DIR [--order book-order.json] [--context]

Anchors resolve like book-design/curated/manuscript.py: lower-case alphanumeric tokens,
accepted only if exactly one paragraph contains them; the image is placed after that
paragraph. Reports per chapter: images placed, words per image (density), anchors that
no longer resolve or resolve twice (the renderer silently omits them), images at a
section break vs inside a section's run, and open VISUAL/DIAGRAM briefs. --context prints
the end of the paragraph each image follows, to judge whether the picture draws it.
"""
import argparse, json, re
from collections import defaultdict
from pathlib import Path

def norm(t): return " ".join(re.findall(r"[a-z0-9]+", (t or "").lower().replace("’", "'")))

def blocks(raw):
    raw = re.sub(r"<!--.*?-->", "\n", raw, flags=re.S)
    raw = re.sub(r"(?m)^\[\^[^\]]+\]:.*$", "", raw)
    return [b.strip() for b in raw.split("\n\n") if b.strip()]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("art"); ap.add_argument("dir"); ap.add_argument("--order"); ap.add_argument("--context", action="store_true")
    a = ap.parse_args()
    art = json.load(open(a.art)); d = Path(a.dir)
    names = json.load(open(a.order)) if a.order else sorted(p.name for p in d.glob("*.md"))
    by = defaultdict(list)
    for e in art:
        by[e.get("section") or e.get("chapter")].append(e)
    print(f"{'file':40}{'images':>7}{'words/img':>10}{'missing':>8}{'dup':>5}{'at break':>9}{'briefs':>7}")
    problems = []
    for n in names:
        p = d / n
        if not p.exists(): continue
        m = re.match(r"(\d\d)-", n)
        key = n if n in by else (int(m.group(1)) if m else None)
        entries = by.get(key, [])
        raw = p.read_text(encoding="utf-8"); bs = blocks(raw); nb = [norm(b) for b in bs]
        words = len(re.sub(r"<!--.*?-->", " ", raw, flags=re.S).split())
        missing = dup = brk = 0
        for e in entries:
            if not e.get("after"):
                problems.append((n, e["id"], "NO ANCHOR (handled specially or unplaced)", "")); continue
            w = norm(e["after"]); hits = [i for i, b in enumerate(nb) if w in b]
            if not hits: missing += 1; problems.append((n, e["id"], "MISSING", e["after"][:90]))
            elif len(hits) > 1: dup += 1; problems.append((n, e["id"], "AMBIGUOUS", e["after"][:90]))
            else:
                i = hits[0]
                if i + 1 >= len(bs) or bs[i + 1].startswith("#"): brk += 1
                if a.context: print(f"     {e['id']}: …{bs[i][-120:]}")
        briefs = len(re.findall(r"<!--\s*\[?(VISUAL|DIAGRAM)", raw))
        if entries or briefs:
            print(f"{n[:40]:40}{len(entries):>7}{(words // len(entries) if entries else 0):>10}{missing:>8}{dup:>5}{brk:>9}{briefs:>7}")
    if problems:
        print("\nanchors to fix (the renderer omits these images):")
        for p in problems: print("  ", *p)

if __name__ == "__main__":
    main()

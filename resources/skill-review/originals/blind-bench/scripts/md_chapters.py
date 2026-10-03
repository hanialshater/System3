#!/usr/bin/env python3
"""Build chapters.json from a Markdown chapter directory (e.g. System 3's chapters/).

  md_chapters.py CHAPTER_DIR BOOK_ID [--order book-order.json] [--only-numbered] > chapters.json

Strips HTML comments, footnote definitions, citation links, code fences and the H1 title
(titles are not sent to judges). Covers, part pages and appendices are skipped with
--only-numbered.
"""
import argparse, json, re
from pathlib import Path
ap = argparse.ArgumentParser(); ap.add_argument("dir"); ap.add_argument("book")
ap.add_argument("--order"); ap.add_argument("--only-numbered", action="store_true")
a = ap.parse_args(); d = Path(a.dir)
names = json.load(open(a.order)) if a.order else sorted(p.name for p in d.glob("*.md"))
out = []
for n in names:
    m = re.match(r"(\d\d)-", n)
    if a.only_numbered and not m: continue
    if not (d / n).exists(): continue
    t = (d / n).read_text(encoding="utf-8")
    title = (re.search(r"(?m)^# (.+)$", t) or [None, n])[1]
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S); t = re.sub(r"```.*?```", "", t, flags=re.S)
    t = re.sub(r"(?m)^\[\^[^\]]+\]:.*$", "", t); t = re.sub(r"\[\^[^\]]+\]|\[\d+\]\([^)]*\)", "", t)
    t = re.sub(r"(?m)^# .+$", "", t, count=1)
    if len(t.split()) < 200: continue
    out.append({"id": f"{a.book}-{m.group(1) if m else n[:-3]}", "book": a.book, "title": title.strip(), "words": len(t.split()), "text": t.strip()})
print(json.dumps(out, ensure_ascii=False))

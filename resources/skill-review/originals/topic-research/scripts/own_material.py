#!/usr/bin/env python3
"""Search the author's own material before the web, and show where a candidate is already used.

  own_material.py "Ostrom|commons|irrigation" --roots chapters resources ~/dream ~/blog [--context 1]
  own_material.py "Jacobs" --roots chapters --used-only

For each root (Markdown/text files, recursively), prints matches with file:line and a little
context, grouped by file, newest-modified first. --used-only prints just the files and counts:
that's the collision check (is this thinker or case already carried by another chapter?).
Archived and draft material often holds the best candidates (the Jacobs case, the Ostrom
throughput question and Newton's brachistochrone were all already written somewhere).
"""
import argparse, re, os
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("pattern"); ap.add_argument("--roots", nargs="+", default=["."])
ap.add_argument("--context", type=int, default=0); ap.add_argument("--used-only", action="store_true")
a = ap.parse_args()
rx = re.compile(a.pattern, re.I)
files = []
for r in a.roots:
    p = Path(os.path.expanduser(r))
    if p.is_file(): files.append(p)
    elif p.is_dir(): files += [f for f in p.rglob("*") if f.suffix.lower() in (".md", ".txt", ".markdown") and ".git" not in f.parts]
files.sort(key=lambda f: -f.stat().st_mtime)
total = 0
for f in files:
    try: lines = f.read_text(encoding="utf-8", errors="ignore").splitlines()
    except Exception: continue
    hits = [i for i, l in enumerate(lines) if rx.search(l)]
    if not hits: continue
    total += len(hits)
    print(f"\n## {f}  ({len(hits)})")
    if a.used_only: continue
    for i in hits[:12]:
        lo, hi = max(0, i - a.context), min(len(lines), i + a.context + 1)
        for j in range(lo, hi):
            mark = ">" if j == i else " "
            print(f"  {mark}{j + 1}: {lines[j].strip()[:220]}")
print(f"\n{total} matches in {sum(1 for f in files if True)} files searched")

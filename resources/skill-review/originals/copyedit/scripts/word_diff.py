#!/usr/bin/env python3
"""Word-level diff of a mechanical pass: every changed token with context and a count per
change type, so a bad substitution (programme→program turning "programmers" into
"programrs") shows up before commit.

  word_diff.py BEFORE AFTER            # files or directories with matching names
  git diff --word-diff=porcelain is the git-native alternative.
"""
import difflib, re, sys
from collections import Counter
from pathlib import Path

def pairs(a, b):
    a, b = Path(a), Path(b)
    if a.is_dir(): return [(a / f.name, f) for f in sorted(b.glob("*.md")) if (a / f.name).exists()]
    return [(a, b)]

kinds = Counter()
for x, y in pairs(sys.argv[1], sys.argv[2]):
    wa = re.findall(r"\S+", x.read_text(encoding="utf-8")); wb = re.findall(r"\S+", y.read_text(encoding="utf-8"))
    sm = difflib.SequenceMatcher(None, wa, wb, autojunk=False); shown = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal": continue
        old, new = " ".join(wa[i1:i2]), " ".join(wb[j1:j2]); kinds[f"{old[:30]} → {new[:30]}"] += 1
        if shown < 200:
            print(f"{y.name}: [{op}] …{' '.join(wa[max(0, i1 - 4):i1])} {{{old}}} → {{{new}}} {' '.join(wb[j2:j2 + 4])}…"); shown += 1
print("\nchange types (check every rare one by eye):")
for k, v in kinds.most_common(): print(f"  {v:>4}  {k}")

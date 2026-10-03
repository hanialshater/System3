#!/usr/bin/env python3
"""Map a manuscript's structure so arc claims rest on numbers, not impressions.

  arc_map.py CHAPTER_DIR [--order book-order.json]           # table per file + part totals
  arc_map.py CHAPTER_DIR --handoffs                          # last lines of each file vs first lines of the next
  arc_map.py CHAPTER_DIR --motifs camel,octopus,coffee,Alberto   # where each motif appears (counts)
  arc_map.py CHAPTER_DIR --recaps                            # sentences that repeat an earlier chapter (re-teaching)
  arc_map.py CHAPTER_DIR --markers                           # unresolved drafting markers per file

Files named part-*.md open a part; numbered files and others are counted inside the
current part. Without --order, files sort by name. Numbers describe the text; they
do not score it.
"""
import argparse, json, re
from pathlib import Path

MARKERS = r"CLAUDE DRAFT|CLAUDE EDIT|ASSISTANT EDIT|ASSISTANT DRAFT|SLOT ?\d*|TODO|AUTHOR:|EDITORIAL|\[Missing figure\]"

def body(t):
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"```.*?```", "", t, flags=re.S)
    t = re.sub(r"(?m)^\[\^[^\]]+\]:.*$", "", t)
    return t

def paras(t):
    out = []
    for b in body(t).split("\n\n"):
        b = b.strip()
        if b and not b.startswith(("#", "|", "!", "---", "```")):
            out.append(" ".join(b.split()))
    return out

def sents(t):
    flat = " ".join(paras(t))
    flat = re.sub(r"\[\^[^\]]+\]|\[\d+\]\([^)]*\)", "", flat)
    return [s.strip() for s in re.split(r"(?<=[.!?”])\s+(?=[A-Z“*])", flat) if s.strip()]

def stats(t):
    b = body(t); w = max(1, len(b.split()))
    return {
        "words": w,
        "heads": len(re.findall(r"(?m)^#{2,4} ", b)),
        "notes": len(set(re.findall(r"\[\^([^\]]+)\](?!:)", t))) + len(re.findall(r"\]\(appendix-references\.md#", t)),
        "bold/1k": 1000 * len(re.findall(r"\*\*[^*]+\*\*", b)) / w,
        "I/1k": 1000 * len(re.findall(r"\b(?:I|I'm|I’m|I've|I’ve|my|me|myself)\b", b)) / w,
        "markers": len(re.findall(MARKERS, t)),
    }

def load(d, order):
    d = Path(d)
    names = json.load(open(order)) if order else sorted(p.name for p in d.glob("*.md"))
    return [(n, (d / n).read_text(encoding="utf-8")) for n in names if (d / n).exists()]

def shingles(s, k=5):
    w = re.findall(r"[a-z’']+", s.lower())
    return {" ".join(w[i:i + k]) for i in range(len(w) - k + 1)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir"); ap.add_argument("--order")
    ap.add_argument("--handoffs", action="store_true")
    ap.add_argument("--motifs")
    ap.add_argument("--recaps", action="store_true")
    ap.add_argument("--markers", action="store_true")
    ap.add_argument("--threshold", type=float, default=0.45, help="recap shingle overlap")
    a = ap.parse_args()
    files = load(a.dir, a.order)
    main_files = [(n, t) for n, t in files if not n.startswith(("appendix", "about", "back-matter"))]

    print(f"{'file':40}{'words':>7}{'heads':>6}{'notes':>6}{'bold/1k':>8}{'I/1k':>7}{'markers':>8}")
    part, totals = "(front)", {}
    for n, t in files:
        if n.startswith("part-") or n.startswith(("alternative", "back-matter")) or n.startswith("interlude"):
            part = n
        elif n.startswith(("appendix", "about")):
            part = "(back matter)"
        s = stats(t)
        totals.setdefault(part, 0); totals[part] += s["words"]
        print(f"{n[:40]:40}{s['words']:>7}{s['heads']:>6}{s['notes']:>6}{s['bold/1k']:>8.1f}{s['I/1k']:>7.1f}{s['markers']:>8}")
    print("\nwords per part (part page through the file before the next part):")
    for p, w in totals.items():
        print(f"  {p:40}{w:>7}")

    if a.handoffs:
        print("\n== handoffs: last two sentences → next file's first two")
        for (n1, t1), (n2, t2) in zip(main_files, main_files[1:]):
            s1, s2 = sents(t1), sents(t2)
            print(f"\n{n1} → {n2}\n   END:   {' '.join(s1[-2:])[:300]}\n   START: {' '.join(s2[:2])[:300]}")

    if a.motifs:
        terms = [m.strip() for m in a.motifs.split(",") if m.strip()]
        print("\n== motifs (count per file; blank = absent)")
        print(f"{'file':40}" + "".join(f"{m[:9]:>10}" for m in terms))
        for n, t in main_files:
            b = body(t).lower()
            row = [len(re.findall(r"\b" + re.escape(m.lower()), b)) for m in terms]
            if any(row):
                print(f"{n[:40]:40}" + "".join(f"{(str(c) if c else ''):>10}" for c in row))

    if a.recaps:
        print(f"\n== sentences that substantially repeat an earlier file (5-word shingle overlap ≥ {a.threshold})")
        seen = []  # (file, sentence, shingles)
        for n, t in main_files:
            for s in sents(t):
                sh = shingles(s)
                if len(sh) < 4:
                    continue
                for n0, s0, sh0 in seen:
                    if n0 != n and len(sh & sh0) / len(sh) >= a.threshold:
                        print(f"\n  {n}: {s[:200]}\n    ≈ {n0}: {s0[:200]}")
                        break
            seen += [(n, s, shingles(s)) for s in sents(t) if len(shingles(s)) >= 4]

    if a.markers:
        print("\n== unresolved markers")
        for n, t in files:
            for m in re.finditer(r"<!--[^>]{0,40}(?:" + MARKERS + r")[^>]{0,80}", t):
                print(f"  {n}: {' '.join(m.group(0).split())[:150]}")
            for m in re.finditer(r"\*?\[Missing figure\]\*?", t):
                print(f"  {n}: {m.group(0)}")

if __name__ == "__main__":
    main()

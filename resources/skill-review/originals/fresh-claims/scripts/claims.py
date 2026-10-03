#!/usr/bin/env python3
"""Pull checkable claims out of Markdown chapters and flag the risky ones.

  claims.py CHAPTER_DIR [--order book-order.json]            # claim ledger as TSV on stdout
  claims.py CHAPTER_DIR --since 2025 --only fresh             # only claims about recent events
  claims.py CHAPTER_DIR --numbers "agents,hours,days,theorems,percent"   # same unit, different numbers across files
  claims.py CHAPTER_DIR --notes                               # footnote integrity across the whole book

A claim is a sentence with a number, a year, a percentage, a quantity word or a
named organization plus a reporting verb. "fresh" = mentions a year >= --since or a
month name with such a year nearby. The ledger is a worklist for verification, not
a verdict: every row still needs a source checked by a person or a search.
"""
import argparse, json, re, sys
from collections import defaultdict
from pathlib import Path

ORGS = r"(Anthropic|OpenAI|Google|DeepMind|Meta|Facebook|Microsoft|Clay|CERN|Nature|Science|arXiv|Amazon|Bing|NVIDIA|Prove2Me|xAI)"
MONTHS = r"(January|February|March|April|May|June|July|August|September|October|November|December)"
NUM = r"(\d[\d,\.]*\s?(%|percent|per cent)?|\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty|thirty|forty|fifty|sixty|hundred|thousand|million|billion)\b)"
HEDGES = r"\b(reported|reportedly|announced|claimed|according to|says|said|stated|apparently|proposed|preprint|at the time of writing)\b"

def clean(t):
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    return t

def body_and_notes(t):
    t = clean(t)
    notes = dict(re.findall(r"(?m)^\[\^([^\]]+)\]:\s*(.*)$", t))
    body = re.sub(r"(?m)^\[\^[^\]]+\]:.*$", "", t)
    return body, notes

def sentences(body):
    flat = " ".join(l.strip() for l in body.splitlines() if l.strip() and not l.lstrip().startswith(("#", "|", "!")))
    return [s.strip() for s in re.split(r"(?<=[.!?”])\s+(?=[A-Z“*(])", flat) if s.strip()]

def classify(s, since):
    years = [int(y) for y in re.findall(r"\b(1[5-9]\d\d|20\d\d)\b", s)]
    fresh = any(y >= since for y in years)
    has_num = bool(re.search(NUM, s, re.I))
    org = re.search(ORGS, s)
    hedged = bool(re.search(HEDGES, s, re.I))
    refs = re.findall(r"\[\^([^\]]+)\]", s)
    kind = []
    if fresh: kind.append("fresh")
    if has_num: kind.append("number")
    if org: kind.append("org:" + org.group(1))
    if years and not fresh: kind.append("history")
    return kind, hedged, refs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir"); ap.add_argument("--order")
    ap.add_argument("--since", type=int, default=2025)
    ap.add_argument("--only", choices=["fresh", "number", "unsourced"])
    ap.add_argument("--numbers")
    ap.add_argument("--notes", action="store_true")
    a = ap.parse_args()
    d = Path(a.dir)
    names = json.load(open(a.order)) if a.order else sorted(p.name for p in d.glob("*.md"))
    files = [(n, (d / n).read_text(encoding="utf-8")) for n in names if (d / n).exists() and not n.startswith("appendix-references")]

    if a.notes:
        defined = defaultdict(list); used = defaultdict(list)
        for n, t in files:
            body, notes = body_and_notes(t)
            for k in notes: defined[k].append(n)
            for k in set(re.findall(r"\[\^([^\]]+)\](?!:)", body)): used[k].append(n)
        for k, fs in defined.items():
            if len(fs) > 1: print(f"DUPLICATE KEY  [^{k}] defined in {', '.join(fs)} (a joined build prints the first definition everywhere)")
        for k, fs in used.items():
            if k not in defined: print(f"UNDEFINED      [^{k}] used in {', '.join(fs)}")
        for k, fs in defined.items():
            if k not in used: print(f"UNUSED         [^{k}] defined in {', '.join(fs)}")
        refs_path = d / "appendix-references.md"
        if refs_path.exists():
            anchors = set(re.findall(r'<a id="([^"]+)"', refs_path.read_text(encoding="utf-8")))
            cited = defaultdict(list)
            for n, t in files:
                for num, anc in re.findall(r"\[(\d+)\]\(appendix-references\.md#([^)]+)\)", t):
                    cited[anc].append((n, int(num)))
            for anc, uses in cited.items():
                if anc not in anchors:
                    print(f"MISSING ANCHOR #{anc} cited in {', '.join(sorted({u[0] for u in uses}))}")
                if len({u[1] for u in uses}) > 1:
                    print(f"NUMBER CLASH   #{anc} cited with numbers {sorted({u[1] for u in uses})}")
            for anc in sorted(anchors - set(cited)):
                print(f"UNCITED ENTRY  #{anc} (fine if listed as an additional source)")
        for n, t in files + ([("appendix-references.md", refs_path.read_text(encoding="utf-8"))] if refs_path.exists() else []):
            for m in re.finditer(r"(?:checked|accessed|status[^.]{0,40}) on [^.\]]*\d{4}", t):
                print(f"DATED CHECK    {n}: {m.group(0)}  (re-check before print)")
        return

    if a.numbers:
        units = [u.strip() for u in a.numbers.split(",")]
        seen = defaultdict(list)
        for n, t in files:
            body, _ = body_and_notes(t)
            for s in sentences(body):
                for u in units:
                    W = r"(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty|thirty|forty|fifty|sixty|eighty|ninety|hundred|thousand|million|billion)"
                    for m in re.finditer(r"(\d[\d,\.]*(?:\s(?:thousand|million|billion))?|\b" + W + r"(?:[\s-]" + W + r")*)\s+(?:[A-Za-z][\w.\-]*\s+){0,3}" + re.escape(u) + r"\b", s, re.I):
                        seen[u].append((m.group(1).strip().lower(), n, s[:160]))
        for u, rows in seen.items():
            vals = {v for v, _, _ in rows}
            if len(vals) > 1:
                print(f"\n== '{u}': {len(vals)} different numbers")
                for v, n, s in rows: print(f"   {v:>12}  {n}: {s}")
        return

    print("file\tkind\thedged\tnotes\tsentence")
    for n, t in files:
        body, notes = body_and_notes(t)
        for s in sentences(body):
            kind, hedged, refs = classify(s, a.since)
            if not kind: continue
            if a.only == "fresh" and "fresh" not in kind: continue
            if a.only == "number" and "number" not in kind: continue
            if a.only == "unsourced" and (refs or "history" in kind and "number" not in kind): continue
            if a.only == "unsourced" and not ("fresh" in kind or "number" in kind): continue
            print(f"{n}\t{','.join(kind)}\t{'yes' if hedged else ''}\t{','.join(refs)}\t{re.sub(r'\[\^[^\]]+\]','',s)[:220]}")

if __name__ == "__main__":
    main()

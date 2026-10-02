#!/usr/bin/env python3
"""Count prose tells per chapter and compare them with the Chapter 4-5 baseline.

The counts are heuristics for an editor's attention, not verdicts. A flagged line
may be exactly right; the point is to see where a chapter leans on a habit more
than the author's strongest chapters do.

Usage:
    python3 resources/editorial/check-tells.py                 # summary table
    python3 resources/editorial/check-tells.py 07 --lines      # flagged lines for chapters starting with 07
"""
import re
import sys
from pathlib import Path

CHAPTERS = Path(__file__).resolve().parents[2] / "chapters"

CONTRAST = [
    r"\bnot (?:merely|only|just|simply)\b",
    r"\b(?:is|are|was|were) not [^.;:]{1,60}[.;] (?:It|They|This|That) (?:is|are|was|were)\b",
    r"\bisn’t [^.;:]{1,60}[.;] (?:It|This|That)’s\b",
    r"\bnot [^.,;:]{1,40}, but\b",
    r"\bnot [^.,;:]{1,40} but (?:a|an|the|to|in|on|as)\b",
    r"\bless (?:a|an|like) [^.,;:]{1,40} than\b",
    r"\b(?:does|do|did|need) not [^.;:]{1,50}\. (?:It|They|This|That) (?:only|just|simply)\b",
]
CROSSREF = [
    r"\bChapter \d+\b",
    r"\b(?:previous|last|earlier|next) chapter\b",
    r"\bas we (?:saw|have seen)\b",
    r"\bthis chapter\b",
]
CITE = re.compile(r"\]\(appendix-references\.md#")
SENT = re.compile(r"(?<=[.!?”*])\s+(?=[A-Z“*`(])")


def paragraphs(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    for block in text.split("\n\n"):
        b = block.strip()
        if not b or b[0] in "#|>-!*" and not b.startswith("**") or b.startswith("*") and b.endswith("*") and "\n" not in b and len(b.split()) < 15:
            continue
        if b.startswith(("```", "<", "\\")):
            continue
        yield b


def last_sentence(p):
    clean = re.sub(r"\[\d+\]\([^)]*\)", "", p).strip()
    parts = [s for s in SENT.split(clean) if s.strip()]
    return parts, parts[-1] if parts else ""


def analyse(path):
    text = path.read_text()
    words = len(text.split())
    paras = list(paragraphs(text))
    maxims, contrasts, chains, xrefs = [], [], [], []
    for p in paras:
        parts, last = last_sentence(p)
        if len(parts) >= 3 and len(last.split()) <= 12 and not re.search(r"\d", last):
            maxims.append(last)
        if len(CITE.findall(p)) >= 3:
            chains.append(p[:90])
    for i, line in enumerate(text.splitlines(), 1):
        for pat in CONTRAST:
            for m in re.finditer(pat, line):
                contrasts.append((i, line[max(0, m.start() - 30):m.end() + 30]))
        for pat in CROSSREF:
            for m in re.finditer(pat, line):
                if line.startswith("# "):
                    continue
                xrefs.append((i, line[max(0, m.start() - 30):m.end() + 30]))
    long_paras = [p for p in paras if len(p.split()) >= 25]
    return {
        "words": words,
        "maxim_pct": 100 * len(maxims) / max(1, len(long_paras)),
        "contrast_k": 1000 * len(contrasts) / words,
        "chains": len(chains),
        "xref_k": 1000 * len(xrefs) / words,
        "detail": {"maxims": maxims, "contrasts": contrasts, "chains": chains, "xrefs": xrefs},
    }


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    show = "--lines" in sys.argv
    files = sorted(CHAPTERS.glob("[0-1][0-9]-*.md"))
    if args:
        files = [f for f in files if any(f.name.startswith(a) for a in args)]
    print(f"{'chapter':40} {'words':>6} {'maxim%':>7} {'notXbutY/1k':>12} {'cite-chains':>12} {'xref/1k':>8}")
    for f in files:
        r = analyse(f)
        print(f"{f.name[:40]:40} {r['words']:>6} {r['maxim_pct']:>6.0f}% {r['contrast_k']:>12.1f} {r['chains']:>12} {r['xref_k']:>8.1f}")
        if show:
            d = r["detail"]
            for s in d["maxims"]:
                print(f"    maxim:    {s}")
            for i, s in d["contrasts"]:
                print(f"    contrast: L{i}: …{s}…")
            for s in d["chains"]:
                print(f"    chain:    {s}…")
            for i, s in d["xrefs"]:
                print(f"    xref:     L{i}: …{s}…")
    print("\nTargets, calibrated on Chapters 4-5 as this tool measures them: maxim% <= 30, notXbutY/1k <= 0.5, cite-chains 0, xref/1k <= 0.5")


if __name__ == "__main__":
    main()

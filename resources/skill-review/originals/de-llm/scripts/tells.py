#!/usr/bin/env python3
"""Measure LLM-prose tells per 1,000 words and list the flagged lines.

Heuristics for an editor's attention, not verdicts. Always read the baseline
column: a habit is a tell only where a draft leans on it harder than the
author's own cleanest writing does.

Usage:
  tells.py FILE [FILE ...]                 # table, one row per file
  tells.py FILE --list                     # plus every flagged instance
  tells.py FILE --list --only antithesis,hedge
  tells.py DRAFT --baseline CLEAN.md ...   # adds a ratio column vs. baseline
"""
import re, sys, argparse
from pathlib import Path

SENT = re.compile(r"(?<=[.!?”\"*)])\s+(?=[A-Z“\"*`(])")

SIGNPOST = re.compile(r"(?i)(?:^|(?<=[.!?]\s))(?:so,? |this is where|this is what (?:I mean|matters)|that is what I mean|"
    r"there is (?:an obvious problem|a question|one more|another|something)|here(?:'s| is) (?:the|what|where|why)|"
    r"the (?:key|important|real|interesting) (?:point|insight|question|part|thing) is|it is worth|"
    r"this changes how|at its most compressed|in other words|put (?:simply|differently|another way)|"
    r"notice (?:that|what|how)|look (?:back )?at what|the point is|what matters (?:here )?is|"
    r"consider (?:what|how)|this matters (?:because|far beyond)|that is the (?:surprise|problem|point)|"
    r"those questions will|for now, the|the resemblance is|growth is the right word|.{0,20}helps draw)")
HEDGE = re.compile(r"\b(?:does not|do not|did not|cannot|can't|is not|are not|was not|need not|does not mean|"
    r"doesn't|don't|isn't|aren't)\b")
ANTI = [  # X/Y family
    (r"\b(?:is|are|was|were|does|do) not\b[^.!?]{0,80}[.!?]\s+(?:It|They|That|This)\s+(?:is|are|was|does)\b", "not-X. It-is-Y"),
    (r",\s(?:not|never)\s[^.!?,;]{1,50}[.!?]", "X, not Y"),
    (r"\bnot (?:merely|only|just|simply)\b", "not only/merely"),
    (r"\bnot [^.,;:]{1,40},? but\b", "not X but Y"),
    (r"[^.!?\n;]{8,};\s[^.!?\n]{8,}(?:not|n't|nothing|never|only)\b[^.!?\n]*[.!?]", "semicolon antithesis"),
]
BECOME = re.compile(r"(?i)\b(?:become|becomes|became|becoming)\b")
OPENERS = re.compile(r"(?m)(?:^|(?<=[.!?]\s))(Suppose|Consider|Take|Imagine|Here is|Picture)\b")
Q_HEAD = re.compile(r"(?m)^#{2,4}\s+(.*\?\s*$|What .* (?:Actually|Really) .*|.*,\s+Not\s+.*|[^:\n]{2,25}:\s+.*)$")

def clean(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"(?m)^\[\^[^\]]+\]:.*$", "", text)          # footnote defs
    text = re.sub(r"\[\^[^\]]+\]|\[\d+\]\([^)]*\)", "", text)    # footnote refs
    return text

def paragraphs(text):
    for b in text.split("\n\n"):
        b = b.strip()
        if not b or b.startswith(("#", "|", ">", "!", "---", "```", "<", "- ", "* ", "1.", "2.", "3.")):
            continue
        yield b

def sents(p):
    return [s.strip() for s in SENT.split(p) if s.strip()]

def analyse(text):
    raw = text
    text = clean(text)
    paras = list(paragraphs(text))
    words = max(1, sum(len(p.split()) for p in paras))
    hits = {k: [] for k in ["signpost", "anaphora", "antithesis", "parallel-pair", "hedge",
                            "closing-moral", "become", "opener", "one-liner", "q-heading"]}
    long_paras = 0
    for p in paras:
        ss = sents(p)
        flat = " ".join(p.split())
        for m in SIGNPOST.finditer(flat):
            hits["signpost"].append(flat[m.start():m.start() + 110])
        # anaphora: 3+ consecutive sentences sharing first word
        firsts = [s.split()[0].lower().strip("*“\"") for s in ss if s.split()]
        run = 1
        for i in range(1, len(firsts)):
            run = run + 1 if firsts[i] == firsts[i - 1] else 1
            if run == 3:
                hits["anaphora"].append(" / ".join(x[:40] for x in ss[i - 2:i + 1]))
        for pat, label in ANTI:
            for m in re.finditer(pat, flat):
                hits["antithesis"].append(f"[{label}] " + flat[max(0, m.start() - 40):m.end()][:170])
        for a, b in zip(ss, ss[1:]):
            wa, wb = a.split(), b.split()
            if 2 <= len(wa) <= 9 and 2 <= len(wb) <= 9 and abs(len(wa) - len(wb)) <= 3 and wa[0] == wb[0]:
                hits["parallel-pair"].append(f"{a} | {b}")
        for s in ss:
            if HEDGE.search(s):
                hits["hedge"].append(s[:150])
        if len(ss) >= 3:
            long_paras += 1
            last = ss[-1]
            if len(last.split()) <= 14 and not re.search(r"\d|[“\"]", last):
                hits["closing-moral"].append(last)
        if len(ss) == 1 and len(p.split()) <= 14:
            hits["one-liner"].append(p)
        for m in BECOME.finditer(flat):
            hits["become"].append(flat[max(0, m.start() - 50):m.end() + 40])
        for m in OPENERS.finditer(flat):
            hits["opener"].append(m.group(1) + ": " + flat[m.start():m.start() + 90])
    for m in Q_HEAD.finditer(raw):
        hits["q-heading"].append(m.group(0).strip())
    rates = {k: 1000 * len(v) / words for k, v in hits.items()}
    rates["closing-moral"] = 100 * len(hits["closing-moral"]) / max(1, long_paras)  # percent of 3+ sentence paras
    rates["q-heading"] = len(hits["q-heading"])  # raw count
    return words, rates, hits

COLS = ["signpost", "anaphora", "antithesis", "parallel-pair", "hedge", "closing-moral", "become", "opener", "one-liner", "q-heading"]
UNITS = {"closing-moral": "%", "q-heading": "n"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--baseline", help="author's cleanest text, for comparison")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    rows = []
    if a.baseline:
        rows.append(("BASELINE " + Path(a.baseline).name, *analyse(Path(a.baseline).read_text(encoding="utf-8"))))
    for f in a.files:
        rows.append((Path(f).name, *analyse(Path(f).read_text(encoding="utf-8"))))
    hdr = f"{'file':34}{'words':>7}" + "".join(f"{c[:9]+('('+UNITS[c]+')' if c in UNITS else ''):>14}" for c in COLS)
    print("per 1,000 words unless marked; closing-moral = % of 3+ sentence paragraphs; q-heading = count")
    print(hdr)
    for name, w, r, _ in rows:
        print(f"{name[:34]:34}{w:>7}" + "".join(f"{r[c]:>14.2f}" if c not in UNITS else f"{r[c]:>14.0f}" for c in COLS))
    if a.list:
        only = set(filter(None, a.only.split(",")))
        for name, w, r, h in rows:
            if name.startswith("BASELINE"):
                continue
            print(f"\n=== {name}")
            for k in COLS:
                if only and k not in only:
                    continue
                if h[k]:
                    print(f"\n-- {k} ({len(h[k])})")
                    for x in h[k]:
                        print("   ", x)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Measure a passage against the author's voice baseline (Chapters 4 and 5).

Usage:
    python3 voice_check.py draft.md            # report
    python3 voice_check.py draft.md --json     # machine-readable

Counts are flags for attention, not targets. Read every flagged line in context.
"""
import json
import re
import sys
from pathlib import Path

# Measured on chapters/04-system-3.md and 05-the-society-of-agents.md (prose only).
BASELINE = {
    "em_dash_per_1k": 0.0,
    "mean_sentence_words": 14.5,
    "short_sentence_share": 0.13,   # sentences of 6 words or fewer
    "colon_per_1k": 6.5,
    "semicolon_per_1k": 1.0,
}
AI_VOCAB = ["delve", "tapestry", "robust", "seamless", "crucial", "moreover", "furthermore",
            "ultimately", "unlock", "game-changer", "game changer", "let's", 
            "realm", "foster", "multifaceted", "nuanced", "intricate", "showcase", "embark",
            "pivotal", "testament", "underscore", "navigate the"]
BRITISH = ["behaviour", "colour", "favour", "centre", "grey", "organis", "recognis", "optimis",
           "labelled", "theatre", "realis", "analysed", "neighbour", "programme"]
CONTRAST = [r"\bnot (?:merely|only|just|simply)\b",
            r"\b(?:is|are|was|were|isn't|aren't) not [^.;:]{1,60}[.;] (?:It|They|This|That) (?:is|are|was|were)\b",
            r"\bisn[’']t [^.;:]{1,60}[.;] (?:It|This|That)[’']s\b",
            r"\bnot [^.,;:]{1,40}, but\b"]
SIGNPOST = [r"\bin this (?:chapter|section|essay|post)\b", r"\bit(?:'|’)s worth noting\b",
            r"\bin conclusion\b", r"\blet(?:'|’)s (?:explore|dive|take a look)\b", r"\bhere(?:'|’)s the thing\b"]
SENT = re.compile(r"(?<=[.!?”])\s+(?=[A-Z“\"(])")


def prose(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    keep = [l for l in text.splitlines() if l.strip() and not l.lstrip().startswith(("#", "|", ">"))]
    return "\n".join(keep)


def analyse(text):
    p = prose(text)
    words = max(1, len(p.split()))
    k = 1000 / words
    sents = [s for s in SENT.split(re.sub(r"\s+", " ", p)) if s.strip()]
    lens = [len(s.split()) for s in sents] or [0]
    low = p.lower()
    paras = [b for b in re.split(r"\n\s*\n", p) if len(b.split()) >= 25]
    r = {
        "words": words,
        "em_dash_per_1k": round(p.count("—") * k, 2),
        "mean_sentence_words": round(sum(lens) / len(lens), 1),
        "short_sentence_share": round(sum(1 for n in lens if n <= 6) / len(lens), 2),
        "long_sentence_share": round(sum(1 for n in lens if n >= 30) / len(lens), 2),
        "colon_per_1k": round(p.count(":") * k, 2),
        "semicolon_per_1k": round(p.count(";") * k, 2),
        "first_person_per_1k": round(len(re.findall(r"\b(?:I|me|my|I'm|I’ve|I've)\b", p)) * k, 2),
        "contrast_per_1k": round(sum(len(re.findall(c, p)) for c in CONTRAST) * k, 2),
        "ai_vocab": sorted({w for w in AI_VOCAB if re.search(r"\b" + re.escape(w), low)}),
        "british_spelling": sorted({w for w in BRITISH if re.search(r"\b" + w, low)}),
        "signposting": sorted({m.group(0) for s in SIGNPOST for m in re.finditer(s, low)}),
        "serial_commas": len(re.findall(r"\w+, \w+(?: \w+)?, and \w+", p)),
        "long_paragraphs": len(paras),
    }
    flags = []
    if r["em_dash_per_1k"] > 0.5: flags.append("em-dashes: the best chapters use none in prose")
    if r["mean_sentence_words"] > 20: flags.append("sentences run long; the baseline mean is about 14-15 words")
    if r["short_sentence_share"] < 0.06: flags.append("too few short punch sentences (baseline about 13%)")
    if r["contrast_per_1k"] > 0.5: flags.append("'not X but Y' contrasts above baseline")
    if r["ai_vocab"]: flags.append("machine-flavoured vocabulary: " + ", ".join(r["ai_vocab"]))
    if r["british_spelling"]: flags.append("British spelling (the book is American): " + ", ".join(r["british_spelling"]))
    if r["signposting"]: flags.append("signposting: " + ", ".join(r["signposting"]))
    r["flags"] = flags
    return r


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    r = analyse(Path(args[0]).read_text())
    if "--json" in sys.argv:
        print(json.dumps(r, indent=2, ensure_ascii=False)); return 0
    for key in ["words", "em_dash_per_1k", "mean_sentence_words", "short_sentence_share", "long_sentence_share",
                "colon_per_1k", "semicolon_per_1k", "first_person_per_1k", "contrast_per_1k"]:
        base = BASELINE.get(key)
        print(f"{key:24} {r[key]:>8}" + (f"   (baseline {base})" if base is not None else ""))
    print("flags:" if r["flags"] else "flags: none")
    for f in r["flags"]:
        print("  - " + f)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

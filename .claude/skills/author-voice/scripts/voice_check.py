#!/usr/bin/env python3
"""Measure a passage against the author's voice baseline (Chapters 4 and 5).

Usage:
    python3 voice_check.py draft.md            # report
    python3 voice_check.py draft.md --json     # machine-readable
    python3 voice_check.py draft.md --book chapters/   # also flag 8+ word runs copied from the book

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
    "landing_share": 0.37,          # paragraphs (3+ sentences) ending on a short line (Ch4 0.39, Ch5 0.35)
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
    # Blank lines are kept so paragraph boundaries survive; headings, tables and quotes are dropped.
    keep = [("" if l.lstrip().startswith(("#", "|", ">")) else l) for l in text.splitlines()]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(keep)).strip()


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
    multi = [b for b in re.split(r"\n\s*\n", p) if len(SENT.split(b.strip())) >= 3]
    def lands(b):
        last = SENT.split(re.sub(r"\s+", " ", b.strip()))[-1]
        return len(last.split()) <= 12 and not re.search(r"\d", last)
    r["landing_share"] = round(sum(1 for b in multi if lands(b)) / len(multi), 2) if multi else 0.0
    flags = []
    if r["em_dash_per_1k"] > 0.5: flags.append("em-dashes: the best chapters use none in prose")
    if r["mean_sentence_words"] > 20: flags.append("sentences run long; the baseline mean is about 14-15 words")
    if r["short_sentence_share"] < 0.06: flags.append("too few short punch sentences (baseline about 13%)")
    if r["short_sentence_share"] > 0.2: flags.append("choppy: more than one sentence in five is 6 words or fewer (baseline about 13%)")
    if r["mean_sentence_words"] < 12: flags.append("sentences run short on average; the baseline mean is about 14-15 words")
    if r["landing_share"] > 0.5: flags.append("too many paragraphs end on a short general line; end most on their last fact")
    if r["contrast_per_1k"] > 0.5: flags.append("'not X but Y' contrasts above baseline")
    if r["ai_vocab"]: flags.append("machine-flavoured vocabulary: " + ", ".join(r["ai_vocab"]))
    if r["british_spelling"]: flags.append("British spelling (the book is American): " + ", ".join(r["british_spelling"]))
    if r["signposting"]: flags.append("signposting: " + ", ".join(r["signposting"]))
    r["flags"] = flags
    return r


def copied(text, book_dir, n=8):
    """Runs of n+ words that also appear in the manuscript."""
    norm = lambda t: re.findall(r"[a-z0-9’']+", t.lower().replace("’", "'"))
    words = norm(prose(text))
    grams = {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}
    hits = set()
    for f in sorted(Path(book_dir).glob("[0-9][0-9]-*.md")):
        w = norm(prose(f.read_text()))
        for i in range(len(w) - n + 1):
            g = " ".join(w[i:i + n])
            if g in grams:
                hits.add((f.name, g))
    return sorted(hits)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    r = analyse(Path(args[0]).read_text())
    if "--book" in sys.argv:
        book = sys.argv[sys.argv.index("--book") + 1]
        args = [a for a in args if a != book]
        hits = copied(Path(args[0]).read_text(), book)
        r["copied_runs"] = [f"{name}: ...{g}..." for name, g in hits]
        if hits:
            r["flags"].append(f"{len(hits)} run(s) of 8+ words copied from the manuscript; write new sentences or mark a deliberate callback")
    if "--json" in sys.argv:
        print(json.dumps(r, indent=2, ensure_ascii=False)); return 0
    for key in ["words", "em_dash_per_1k", "mean_sentence_words", "short_sentence_share", "long_sentence_share",
                "landing_share", "colon_per_1k", "semicolon_per_1k", "first_person_per_1k", "contrast_per_1k"]:
        base = BASELINE.get(key)
        print(f"{key:24} {r[key]:>8}" + (f"   (baseline {base})" if base is not None else ""))
    print("flags:" if r["flags"] else "flags: none")
    for f in r["flags"]:
        print("  - " + f)
    for c in r.get("copied_runs", [])[:10]:
        print("    copied: " + c)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

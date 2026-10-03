#!/usr/bin/env python3
"""Measure where an Arabic text sits between Levantine and MSA, and where the dialect lives.

  ar_register.py FILE [FILE ...]            # table: markers per 1,000 words, opening vs body share
  ar_register.py FILE --list msa            # every MSA marker in context (for a Levantine target)
  ar_register.py FILE --list lev            # every Levantine marker in context (for an MSA target)
  ar_register.py FILE --glossary glossary.tsv   # flag English terms rendered inconsistently

"Opening share" is the fraction of Levantine markers that sit in the first three words
of a sentence. A high share with a low rate is the "Levantine-light" pattern: dialect at
the start of sentences, MSA in the body. Heuristics for attention, not verdicts.
"""
import re, sys, argparse
from collections import Counter

LEV = """مش مو هاي هاد هادا هادي هيك هون هناك؟ شو ليش وين مين إمتى امتى بس رح راح عم بدي بدنا بدك بدكم بده بدها
إشي اشي شي كتير هسا هسّا هلأ هلق هلّق لسا لسّا حدا منشان عشان علشان زلمة يعني طيب اللي إللي هيه هيّه هوّ
منقدر بنقدر بقدر بتقدر بنعرف بعرف بتعرف بدّي بدّك ماشي خلّيني خليني خلينا يلا يلّا كمان برضو برضه هيدا هيدي""".split()
LEV = [w for w in LEV if not w.endswith("؟")]
MSA = """ليس ليست ليسوا لكنّ لكنه لكنها إنّما إنما بل الذي التي الذين اللواتي سوف لن لم هذا هذه ذلك تلك هؤلاء
لدى حيث إذ كي ماذا لماذا كيفما أيضًا أيضاً قد إنّ إنه إنها أنّ يجب ينبغي سيكون كان""".split()
SENT_SPLIT = re.compile(r"(?<=[.!؟?…])\s+|\n+")
TOK = re.compile(r"[\u0600-\u06FF]+")

def strip_md(t):
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"`[^`]*`", " ", t)
    t = re.sub(r"(?m)^\[\^[^\]]+\]:.*$", " ", t)
    return t

def norm(w):
    w = re.sub(r"[\u064B-\u0652\u0640]", "", w)  # diacritics, tatweel
    return w

def strip_clitics(w):
    for p in ("و", "ف"):
        if w.startswith(p) and len(w) > 3 and w[1:] in LEVSET | MSASET:
            return w[1:]
    return w

LEVSET = {norm(w) for w in LEV}; MSASET = {norm(w) for w in MSA}

def analyse(text):
    text = strip_md(text)
    sents = [s for s in SENT_SPLIT.split(text) if TOK.search(s)]
    words = 0; lev = Counter(); msa = Counter(); lev_open = 0; lev_total = 0; latin = Counter()
    hits = {"lev": [], "msa": []}
    for s in sents:
        toks = TOK.findall(s); words += len(toks)
        for m in re.finditer(r"[A-Za-z][A-Za-z\-]+", s):
            latin[m.group(0)] += 1
        for i, t in enumerate(toks):
            w = strip_clitics(norm(t))
            if w in LEVSET:
                lev[w] += 1; lev_total += 1
                if i < 3: lev_open += 1
                hits["lev"].append((w, s.strip()[:120]))
            elif w in MSASET:
                msa[w] += 1; hits["msa"].append((w, s.strip()[:120]))
    words = max(words, 1)
    return {"words": words, "lev_k": 1000 * sum(lev.values()) / words, "msa_k": 1000 * sum(msa.values()) / words,
            "open": lev_open / max(1, lev_total), "lev": lev, "msa": msa, "latin": latin, "hits": hits}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--list", choices=["lev", "msa"])
    ap.add_argument("--glossary", help="TSV: english<TAB>arabic rendering<TAB>variants to flag (comma-separated)")
    a = ap.parse_args()
    print(f"{'file':38}{'words':>7}{'lev/1k':>8}{'msa/1k':>8}{'lev share':>10}{'opening':>9}  top Levantine | top MSA")
    for f in a.files:
        r = analyse(open(f, encoding="utf-8").read())
        share = r["lev_k"] / max(0.01, r["lev_k"] + r["msa_k"])
        tl = " ".join(w for w, _ in r["lev"].most_common(6)); tm = " ".join(w for w, _ in r["msa"].most_common(6))
        print(f"{f.split('/')[-1][:38]:38}{r['words']:>7}{r['lev_k']:>8.1f}{r['msa_k']:>8.1f}{share:>10.0%}{r['open']:>9.0%}  {tl} | {tm}")
        if a.list:
            for w, s in r["hits"][a.list]:
                print(f"   [{w}] {s}")
        if a.glossary:
            body = strip_md(open(f, encoding="utf-8").read())
            for line in open(a.glossary, encoding="utf-8"):
                if not line.strip() or line.startswith("#"):
                    continue
                parts = line.rstrip("\n").split("\t")
                if len(parts) < 3 or not parts[2].strip():
                    continue
                for v in [x.strip() for x in parts[2].split(",") if x.strip()]:
                    n = body.count(v)
                    if n:
                        print(f"   glossary: '{v}' x{n} — house rendering for {parts[0]} is '{parts[1]}'")
    print("\nlev share = Levantine / (Levantine + MSA) markers. opening = share of Levantine markers in a sentence's first three words.")

if __name__ == "__main__":
    main()

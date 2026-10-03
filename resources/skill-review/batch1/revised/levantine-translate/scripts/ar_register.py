#!/usr/bin/env python3
"""Measure where an Arabic text sits between Levantine and MSA, where the dialect lives,
and which Levantine it leans to.

  ar_register.py FILE [FILE ...]                 # table (see legend printed at the end)
  ar_register.py FILE --list msa                 # every MSA marker in context (for a Levantine target)
  ar_register.py FILE --list lev                 # every Levantine marker in context (for an MSA target)
  ar_register.py FILE --list nonjo               # Syrian/Lebanese forms (for a Jordanian target)
  ar_register.py FILE --list latin               # English words outside code, links and URLs
  ar_register.py FILE --glossary GLOSSARY.tsv --register blog|book   # terminology drift
  ar_register.py --selftest                      # built-in fixtures; run after editing the word lists

"Opening share" is the fraction of Levantine markers that sit in the first three words of a
sentence. A high share with a low rate is the "Levantine-light" pattern: dialect at the start
of sentences, MSA in the body. The variety column is a rough signal from a handful of forms;
it can say "leans Syrian/Lebanese", it cannot certify Jordanian. Heuristics for attention,
not verdicts.
"""
import re, sys, argparse, signal
from collections import Counter

# Pan-Levantine markers. Deliberately left out because they are also ordinary MSA:
# هو/هوّ (pronoun), يعني («وهذا يعني»), طيب (adjective), راح («راح يبحث»), كان, إنه/إنها
# (the normal Levantine complementiser, so not MSA either).
LEV = """مش هاي هاد هادا هادي هيك هون شو ليش وين مين إمتى امتى بس رح بدي بدنا بدك بدكم بده بدها
شي كتير لسا لسّا حدا علشان اللي إللي هيه هيّه بقدر بتقدر بعرف بتعرف بدّي بدّك ماشي
خلّيني خليني خلينا يلا يلّا كمان برضو برضه هات قديش أديش منيح مزبوط ولك تبعي تبعه تبعها""".split()
# Forms more typical of Jordanian (and Palestinian) than of Syrian/Lebanese speech.
JO = "هسا هسّا هسع هسّع إشي اشي عشان زلمة بنقدر بنعرف بنشوف بنحكي هاظ هاظا هظول".split()
# Forms more typical of Syrian/Lebanese speech. A Jordanian target lists them with --list nonjo.
NONJO = "هيدا هيدي هلق هلّق هلأ مو منشان كرمال عم منقدر منعرف منشوف منحكي إنو انو".split()
# Two-word Levantine forms of address.
PHRASES = ["يا خال", "يا حج", "يا حجة", "يا زلمة", "يا عمي", "يا خالي"]
MSA = """ليس ليست ليسوا لكنّ لكنه لكنها إنّما إنما بل الذي التي الذين اللواتي سوف لن لم هذا هذه ذلك تلك هؤلاء
لدى حيث إذ كي ماذا لماذا كيفما أيضًا أيضاً قد إنّ أنّ يجب ينبغي سيكون""".split()

SENT_SPLIT = re.compile(r"(?<=[.!؟?…])\s+|\n+")
TOK = re.compile(r"[؀-ۿ]+")
TANWEEN = re.compile(r"[ً-ٍ]")  # case endings: a word carrying one is MSA, e.g. «حدًّا»


def strip_md(t):
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"`[^`]*`", " ", t)
    t = re.sub(r"(?m)^\[\^[^\]]+\]:.*$", " ", t)
    return t


def strip_links(t):
    t = re.sub(r"\]\([^)]*\)", "]", t)
    return re.sub(r"https?://\S+|www\.\S+", " ", t)


def norm(w):
    return re.sub(r"[ً-ْـ]", "", w)  # diacritics, tatweel


LEVSET = {norm(w) for w in LEV + JO + NONJO}
JOSET = {norm(w) for w in JO}
NJSET = {norm(w) for w in NONJO}
MSASET = {norm(w) for w in MSA}
PHRASESET = {tuple(norm(x) for x in p.split()) for p in PHRASES}


def strip_clitics(w):
    for p in ("و", "ف"):
        if w.startswith(p) and len(w) > 2 and w not in LEVSET | MSASET and w[1:] in LEVSET | MSASET:
            return w[1:]
    return w


def ctx(toks, i, n=6):
    return " ".join(toks[max(0, i - n):i] + ["[" + toks[i] + "]"] + toks[i + 1:i + n + 1])


def analyse(text):
    text = strip_md(text)
    sents = [s for s in SENT_SPLIT.split(text) if TOK.search(s)]
    words = 0; lev = Counter(); msa = Counter(); lev_open = 0; jo = 0; nj = 0
    hits = {"lev": [], "msa": [], "nonjo": [], "jo": [], "latin": []}
    latin = Counter()
    for s in sents:
        for m in re.finditer(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ\-']+", strip_links(s)):
            latin[m.group(0)] += 1; hits["latin"].append((m.group(0), s.strip()[:100]))
        toks = TOK.findall(s); words += len(toks)
        nt = [norm(t) for t in toks]
        for i, t in enumerate(toks):
            w = strip_clitics(nt[i])
            if i + 1 < len(toks) and (strip_clitics(nt[i]), nt[i + 1]) in PHRASESET:
                w = w + " " + nt[i + 1]
            if (w in LEVSET or " " in w) and not TANWEEN.search(t):
                lev[w] += 1
                if i < 3: lev_open += 1
                hits["lev"].append((w, ctx(toks, i)))
                if w in JOSET: jo += 1; hits["jo"].append((w, ctx(toks, i)))
                if w in NJSET: nj += 1; hits["nonjo"].append((w, ctx(toks, i)))
            elif w in MSASET:
                msa[w] += 1; hits["msa"].append((w, ctx(toks, i)))
    n = max(words, 1); lt = sum(lev.values())
    if jo + nj < 3: variety = "too few"
    elif nj >= 2 * jo: variety = "Syr/Leb lean"
    elif jo >= 2 * nj: variety = "Jordan lean"
    else: variety = "mixed"
    return {"words": words, "lev_k": 1000 * lt / n, "msa_k": 1000 * sum(msa.values()) / n,
            "open": lev_open / max(1, lt), "lev": lev, "msa": msa, "hits": hits,
            "jo": jo, "nonjo": nj, "variety": variety, "latin": latin, "latin_n": sum(latin.values())}


def has_arabic(s):
    return bool(TOK.search(s))


def read_glossary(path):
    rows = []
    for ln, line in enumerate(open(path, encoding="utf-8"), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.rstrip("\n").split("\t")
        parts += [""] * (5 - len(parts))
        rows.append((ln, *[p.strip() for p in parts[:5]]))
    return rows


def lint_glossary(path):
    """Problems in the glossary itself: wrong field count, empty renderings, a rendering listed as a variant."""
    out = []; renders = {}
    for ln, line in enumerate(open(path, encoding="utf-8"), 1):
        if not line.strip() or line.startswith("#"):
            continue
        n = len(line.rstrip("\n").split("\t"))
        if n != 5:
            out.append(f"line {ln}: {n} fields, expected 5")
    for ln, en, book, blog, var, _ in read_glossary(path):
        if not book or not blog:
            out.append(f"line {ln}: {en} has an empty book or blog rendering")
        for r in (book, blog):
            renders.setdefault(norm(r), en)
    for ln, en, book, blog, var, _ in read_glossary(path):
        for v in [x.strip() for x in var.split(",") if x.strip()]:
            if norm(v) in renders:
                out.append(f"line {ln}: variant '{v}' is the house rendering of {renders[norm(v)]}")
    return out


def check_glossary(raw, path, register):
    body = norm(strip_md(raw)); plain = strip_links(strip_md(raw)).lower()
    for ln, en, book, blog, var, note in read_glossary(path):
        house = book if register == "book" else blog
        for v in [x.strip() for x in var.split(",") if x.strip()]:
            n = body.count(norm(v))
            if n:
                print(f"   glossary: '{v}' x{n}; house rendering for {en} ({register}) is '{house}'")
        other = blog if register == "book" else book
        if other and other != house and has_arabic(other) and norm(other) in body and norm(house) not in body:
            print(f"   glossary: {en} appears as the {('blog' if register == 'book' else 'book')} rendering '{other}'; {register} uses '{house}'")
        if has_arabic(house) and re.search(r"(?<![A-Za-z])" + re.escape(en.lower()) + r"(?![A-Za-z])", plain):
            print(f"   glossary: English '{en}' left in the text; {register} rendering is '{house}'")


FIXTURES = {
    "jo": "هسا خلّينا نحكي بصراحة. أنا بدي أعرف شو اللي صار، بس مش قادر أفهم ليش هيك. إشي غريب كتير. "
          "عشان هيك بنقدر نقول إنه الزلمة كان صح، ومش لازم نعيد الحكي. وبس. ولك هات المعادلة يا خال. "
          "هسّع بنعرف قديش الشغلة بدها وقت، وهاد كل اللي بدنا ياه. لسا في إشي ناقص بس منيح هيك. "
          "حدا بيعرف وين راحوا؟ ما حدا. خلينا نكمّل بكرا، ومش رح نوقف هون.",
    "msa": "إن المقيِّم هو أداة القياس، وهذا يعني أن النتيجة تعتمد عليه. والسؤال هو: من يقيّم المقيِّم؟ "
           "وقد راح الباحث يبحث عن الجواب في الكتب التي لم يقرأها أحد من قبل. ليس هذا سؤالًا جديدًا، "
           "بل هو سؤال قديم بلغت فيه الدقة حدًّا لم يبلغه سؤال آخر. لذلك يجب أن ننظر إليه من جديد، "
           "لأن الذين سبقونا لم يملكوا الأدوات التي نملكها اليوم، ولن نفهم ما فعلوه إلا إذا عرفنا حدودهم.",
    "leb": "هلّق عم اشتغل على هيدا المشروع، ومنعرف إنو مو سهل. منشان هيك منقدر نقول إنو الشغل كتير. "
           "شو بدك تعمل؟ هيدي القصة كلها، وما في حدا بيعرف ليش. هلأ منشوف شو بيصير، بس مو هلّق. "
           "عم نحكي عن إشي ما منعرف كيف بدو يخلص، وكرمال هيك عم نستنى. خلينا نشوف بكرا، يلا.",
}


def selftest():
    r = {k: analyse(v) for k, v in FIXTURES.items()}
    share = {k: x["lev_k"] / max(0.01, x["lev_k"] + x["msa_k"]) for k, x in r.items()}
    checks = [
        ("MSA fixture under 15% Levantine", share["msa"] < 0.15),
        ("Jordanian fixture over 85% Levantine", share["jo"] > 0.85),
        ("«حدًّا» with tanween not counted as Levantine", "حدا" not in r["msa"]["lev"]),
        ("«إنه» not counted as MSA", "إنه" not in r["jo"]["msa"]),
        ("clitic «وبس» / «ومش» counted", r["jo"]["lev"]["بس"] >= 2 and r["jo"]["lev"]["مش"] >= 2),
        ("«هات» and «يا خال» counted", r["jo"]["lev"]["هات"] >= 1 and r["jo"]["lev"]["يا خال"] >= 1),
        ("Jordanian fixture reads 'Jordan lean'", r["jo"]["variety"] == "Jordan lean"),
        ("Lebanese fixture reads 'Syr/Leb lean'", r["leb"]["variety"] == "Syr/Leb lean"),
    ]
    import os
    g = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "glossary.tsv")
    if os.path.exists(g):
        problems = lint_glossary(g)
        checks.append(("glossary.tsv lint clean" + ("" if not problems else ": " + "; ".join(problems)), not problems))
    ok = True
    for name, passed in checks:
        print(("PASS  " if passed else "FAIL  ") + name); ok &= passed
    for k in r:
        print(f"      {k}: share {share[k]:.0%}, variety {r[k]['variety']} (jo {r[k]['jo']}, non-jo {r[k]['nonjo']})")
    return 0 if ok else 1


def main():
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--list", choices=["lev", "msa", "jo", "nonjo", "latin"])
    ap.add_argument("--glossary", help="TSV: english, book (MSA), blog (Levantine), variants to flag, note")
    ap.add_argument("--register", choices=["blog", "book"], default="blog", help="which glossary column is the house rendering")
    ap.add_argument("--min-words", type=int, default=50, help="skip files with fewer Arabic words (default 50)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    if not a.files:
        ap.error("give at least one file, or --selftest")
    print(f"{'file':30}{'words':>6}{'lev/1k':>8}{'msa/1k':>8}{'share':>7}{'open':>6}{'latin':>6}  {'variety':14} top Levantine | top MSA")
    for f in a.files:
        raw = open(f, encoding="utf-8").read()
        r = analyse(raw)
        if r["words"] < a.min_words:
            print(f"{f.split('/')[-1][:30]:30}  only {r['words']} Arabic words; nothing to measure (is this the English file?)")
            continue
        share = r["lev_k"] / max(0.01, r["lev_k"] + r["msa_k"])
        tl = " ".join(w for w, _ in r["lev"].most_common(6)); tm = " ".join(w for w, _ in r["msa"].most_common(6))
        print(f"{f.split('/')[-1][:30]:30}{r['words']:>6}{r['lev_k']:>8.1f}{r['msa_k']:>8.1f}{share:>7.0%}{r['open']:>6.0%}"
              f"{r['latin_n']:>6}  {r['variety']:14} {tl} | {tm}")
        if a.list:
            for w, s in r["hits"][a.list]:
                print(f"   [{w}] {s}")
        if a.glossary:
            check_glossary(raw, a.glossary, a.register)
    print("\nshare = Levantine / (Levantine + MSA) markers. open = Levantine markers in a sentence's first three words."
          "\nlatin = English words outside code, links and URLs. variety = Jordanian vs Syrian/Lebanese forms (rough;"
          "\n'too few' means under 3 such forms). The author's own variety comes from him, not from this column.")


if __name__ == "__main__":
    main()

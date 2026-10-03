#!/usr/bin/env python3
"""Blind pairwise benchmark of chapters: Swiss pairing, full text, both orders,
multiple judges, Bradley-Terry with bootstrap intervals, resumable JSONL cache.

  bench.py --chapters chapters.json --dry-run --rounds 3          # mock judge, no API
  bench.py --chapters chapters.json --estimate --rounds 6
  bench.py --chapters chapters.json --judge anthropic:claude-sonnet-5-5 --rounds 6
  bench.py --chapters chapters.json --judge anthropic:MODEL --judge openai:MODEL@https://api.openai.com/v1
  bench.py --chapters chapters.json --fit-only                     # refit from cache

chapters.json: [{"id": "S3-05", "book": "S3", "title": "...", "text": "..."}, ...]
Blinding: book and title are never sent. Names in --strip (author names, book titles,
self-references like "this book") are replaced with neutral tokens before judging.
Each judge is also asked whether it recognises either text; recognition is logged.
Env: ANTHROPIC_API_KEY, OPENAI_API_KEY.
"""
import argparse, hashlib, json, os, random, re, sys, urllib.request
from collections import defaultdict

CRITERIA = ["big_ideas", "thought_provoking", "engagement", "fun", "momentum", "prose", "awkwardness", "novelty"]
RUBRIC = """You are judging two chapters of popular nonfiction head-to-head. Read BOTH in full.
For each criterion name the better chapter ("X" or "Y"), or "tie" when there is no real difference.
Judge as a reader of the finished book. Ignore extraction noise (page numbers, headers, hyphenation).

big_ideas: the larger, more portable central idea (statable in one sentence and still significant)
thought_provoking: leaves the reader arguing with it afterwards; disturbance, not size
engagement: holds attention through its difficult middle, not just its opening
fun: actual pleasure (laughs, delight, play); not momentum, not insight
momentum: pulls the reader forward structurally (setups, open questions, handoffs)
prose: better sentences (rhythm, precision, compression, voice)
awkwardness: FEWER trust- or immersion-breaking moments (flat jokes, register lurches, self-promotion,
  visible scaffolding, name-dropping, production artifacts); the less awkward chapter wins
novelty: newer ideas, framings and examples relative to the chapter's own publication date

Do not reward length, fame or familiarity. Decide each criterion independently.
Respond with ONLY JSON: {"big_ideas":"X|Y|tie", ... one key per criterion ...,
"recognised":"none|X|Y|both", "recognised_as":"<book/author you think it is, or empty>", "rationale":"<=80 words"}"""

def blind(text, strip):
    for s in strip:
        text = re.sub(re.escape(s), "[REDACTED]", text, flags=re.I)
    return text

def call(judge, prompt):
    kind, rest = judge.split(":", 1)
    if kind == "mock":
        rnd = random.Random(hashlib.md5(prompt.encode()).hexdigest())
        out = {c: rnd.choice(["X", "Y", "tie"]) for c in CRITERIA}; out.update(recognised="none", recognised_as="", rationale="mock")
        return json.dumps(out)
    if kind == "anthropic":
        req = urllib.request.Request("https://api.anthropic.com/v1/messages", method="POST",
            headers={"content-type": "application/json", "x-api-key": os.environ.get("ANTHROPIC_API_KEY", ""), "anthropic-version": "2023-06-01"},
            data=json.dumps({"model": rest, "max_tokens": 600, "messages": [{"role": "user", "content": prompt}]}).encode())
        r = json.load(urllib.request.urlopen(req, timeout=600))
        return "".join(b.get("text", "") for b in r["content"])
    if kind == "openai":
        model, _, base = rest.partition("@"); base = base or "https://api.openai.com/v1"
        req = urllib.request.Request(base.rstrip("/") + "/chat/completions", method="POST",
            headers={"content-type": "application/json", "authorization": "Bearer " + os.environ.get("OPENAI_API_KEY", "")},
            data=json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}]}).encode())
        r = json.load(urllib.request.urlopen(req, timeout=600))
        return r["choices"][0]["message"]["content"]
    raise ValueError(judge)

def judge_pair(judge, a, b, strip):
    prompt = f"{RUBRIC}\n\n=== CHAPTER X ===\n{blind(a['text'], strip)}\n\n=== CHAPTER Y ===\n{blind(b['text'], strip)}"
    raw = call(judge, prompt)
    j = json.loads(re.sub(r"^```(json)?|```$", "", raw.strip()).strip())
    return j

def fit(items, games, iters=300):
    """Bradley-Terry by MM, regularised with one virtual tie against a reference item."""
    import math
    REF = "__ref__"; allit = list(items) + [REF]
    games = list(games) + [(i, REF, 0.5) for i in items]
    w = defaultdict(float); n = defaultdict(float); p = {i: 1.0 for i in allit}
    for i, j, s in games:
        w[i] += s; w[j] += 1 - s; n[(i, j)] += 1; n[(j, i)] += 1
    opp = {i: [j for j in allit if n[(i, j)]] for i in allit}
    for _ in range(iters):
        newp = {i: w[i] / sum(n[(i, j)] / (p[i] + p[j]) for j in opp[i]) for i in allit}
        g = newp[REF]; p = {k: max(v / g, 1e-9) for k, v in newp.items()}
    lg = {k: math.log(v) for k, v in p.items() if k != REF}
    m = sum(lg.values()) / len(lg)
    return {k: v - m for k, v in lg.items()}

def games_from(cache, criterion=None, judge=None):
    out = []
    for r in cache:
        if judge and r["judge"] != judge: continue
        crits = [criterion] if criterion else CRITERIA
        for c in crits:
            v = r["verdict"].get(c)
            if v == "X": out.append((r["x"], r["y"], 1.0))
            elif v == "Y": out.append((r["x"], r["y"], 0.0))
            elif v == "tie": out.append((r["x"], r["y"], 0.5))
    return out

def bootstrap(items, cache, B=200, seed=0):
    rnd = random.Random(seed); samples = defaultdict(list)
    for _ in range(B):
        res = [rnd.choice(cache) for _ in cache]
        for k, v in fit(items, games_from(res), iters=100).items(): samples[k].append(v)
    return {k: (sorted(v)[int(.025 * len(v))], sorted(v)[int(.975 * len(v)) - 1]) for k, v in samples.items()}

def swiss(items, scores, played, rnd):
    order = sorted(items, key=lambda i: (-scores.get(i, 0), rnd.random())); pairs = []; used = set()
    for i in order:
        if i in used: continue
        for j in order:
            if j != i and j not in used and frozenset((i, j)) not in played:
                pairs.append((i, j)); used |= {i, j}; break
    return pairs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapters", required=True); ap.add_argument("--cache", default="matches.jsonl")
    ap.add_argument("--judge", action="append", default=[]); ap.add_argument("--rounds", type=int, default=6)
    ap.add_argument("--strip", action="append", default=[], help="names/titles to redact (repeatable)")
    ap.add_argument("--one-order", action="store_true", help="skip the swapped order (halves cost, weaker control)")
    ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--estimate", action="store_true")
    ap.add_argument("--fit-only", action="store_true"); ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    chs = {c["id"]: c for c in json.load(open(a.chapters, encoding="utf-8"))}; items = list(chs)
    judges = ["mock:x"] if a.dry_run else a.judge
    if a.estimate:
        avg = sum(len(c["text"].split()) for c in chs.values()) / len(chs) * 1.35 * 2
        calls = len(items) // 2 * a.rounds * (1 if a.one_order else 2)
        print(f"{calls} calls per judge, ~{avg:,.0f} input tokens each, ~{calls * avg / 1e6:.1f}M input tokens per judge. Check current pricing."); return
    cache = [json.loads(l) for l in open(a.cache)] if os.path.exists(a.cache) else []
    done = {(r["judge"], r["x"], r["y"]) for r in cache}
    if not a.fit_only:
        if not judges: sys.exit("give --judge or --dry-run")
        rnd = random.Random(a.seed); played = {frozenset((r["x"], r["y"])) for r in cache}
        with open(a.cache, "a") as out:
            for rd in range(a.rounds):
                scores = fit(items, games_from(cache)) if cache else {}
                for i, j in swiss(items, scores, played, rnd):
                    played.add(frozenset((i, j)))
                    for x, y in ([(i, j)] if a.one_order else [(i, j), (j, i)]):
                        for jd in judges:
                            if (jd, x, y) in done: continue
                            try:
                                v = judge_pair(jd, chs[x], chs[y], a.strip)
                            except Exception as e:
                                print("error", jd, x, y, e, file=sys.stderr); continue
                            rec = dict(judge=jd, round=rd, x=x, y=y, verdict=v); cache.append(rec); done.add((jd, x, y))
                            out.write(json.dumps(rec) + "\n"); out.flush()
                print(f"round {rd + 1}: {len(cache)} judgments cached")
    if not cache: sys.exit("no judgments")
    overall = fit(items, games_from(cache)); ci = bootstrap(items, cache)
    per = {c: fit(items, games_from(cache, c)) for c in CRITERIA}
    rec = defaultdict(lambda: [0, 0])
    for r in cache:
        for side in ("x", "y"):
            rec[chs[r[side]]["book"]][1] += 1
            if r["verdict"].get("recognised") in (side.upper(), "both"): rec[chs[r[side]]["book"]][0] += 1
    print("\nrank\tid\tbook\tBT\t95% CI\t" + "\t".join(CRITERIA))
    for k, (cid, s) in enumerate(sorted(overall.items(), key=lambda kv: -kv[1]), 1):
        lo, hi = ci[cid]
        print(f"{k}\t{cid}\t{chs[cid]['book']}\t{s:+.2f}\t[{lo:+.2f},{hi:+.2f}]\t" + "\t".join(f"{per[c][cid]:+.1f}" for c in CRITERIA))
    books = defaultdict(list)
    for cid, s in overall.items(): books[chs[cid]["book"]].append(s)
    print("\nbook\tmean BT\tchapters\trecognised")
    for b, v in sorted(books.items(), key=lambda kv: -sum(kv[1]) / len(kv[1])):
        r = rec[b]; print(f"{b}\t{sum(v)/len(v):+.2f}\t{len(v)}\t{r[0]}/{r[1]}")
    if len({r['judge'] for r in cache}) > 1:
        print("\nper-judge ranks differ? compare: " + ", ".join(sorted({r['judge'] for r in cache})))

if __name__ == "__main__":
    main()

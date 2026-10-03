#!/usr/bin/env python3
"""Check that a manuscript agrees with itself, against a book bible (JSON).

  check_bible.py CHAPTER_DIR BIBLE.json [--readme README.md] [--order book-order.json]
  check_bible.py CHAPTER_DIR --discover            # propose bible entries from the text

Bible sections (all optional):
  terms:    [{"term": "harness", "home": "03", "variants": ["Harness"], "defined_by": "bold"}]
            flags the term bolded/defined outside its home chapter, and variant spellings
  people:   [{"name": "Duhem", "home": "05", "intro": ["Pierre Duhem", "physicist Pierre Duhem"]}]
            flags an introduction (full name or appositive) outside the home chapter
  counts:   [{"pattern": "(\\\\w+) (jobs|verbs) of science", "value": "eight"}]
            flags a different number in that construction
  repeats:  [{"id": "X-1", "anchor": "doesn't crash", "home": "03"}]
            flags the idea appearing outside its home chapter (decide once, apply everywhere)
  names:    [{"canonical": "Alpöge", "variants": ["Alpoge"]}]
Always checks: chapter titles and subtitles across the chapter H1, README, references
headings and the Note on Evidence; "Chapter N" cross-references to missing chapters;
"this chapter / this book / rest of the book" phrases for review.
"""
import argparse, json, re
from collections import defaultdict, Counter
from pathlib import Path

def strip(t):
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S); t = re.sub(r"```.*?```", " ", t, flags=re.S)
    return re.sub(r"(?m)^\[\^[^\]]+\]:.*$", "", t)

def lines_with(t, rx, flags=0):
    for i, l in enumerate(t.splitlines(), 1):
        if re.search(rx, l, flags): yield i, l.strip()

def load(d, order):
    names = json.load(open(order)) if order else sorted(p.name for p in Path(d).glob("*.md"))
    out = {}
    for n in names:
        p = Path(d) / n
        if p.exists(): out[n] = p.read_text(encoding="utf-8")
    return out

def chap(n):
    m = re.match(r"(\d\d)-", n); return m.group(1) if m else None

def discover(files):
    bold = defaultdict(set); intro = defaultdict(set); counts = Counter()
    for n, t in files.items():
        b = strip(t)
        for m in re.finditer(r"\*\*([^*]{2,40})\*\*", b): bold[m.group(1).strip().lower()].add(n[:2])
        for m in re.finditer(r"\b(?:philosopher|physicist|mathematician|economist|historian|sociologist|psychologist)\s+([A-Z][a-z]+(?: [A-Z][a-z]+)+)", b):
            intro[m.group(1)].add(n[:2])
        for m in re.finditer(r"\b(two|three|four|five|six|seven|eight|nine|ten)\s+(jobs|verbs|layers|failures|patterns|principles|questions|functions|moves|steps)\b", b, re.I):
            counts[(m.group(1).lower(), m.group(2).lower(), n[:2])] += 1
    print("== bolded in more than one file (candidate terms; pick a home)")
    for k, v in sorted(bold.items()):
        if len(v) > 1: print(f"  {k!r}: {sorted(v)}")
    print("\n== introduced with a role word in more than one file (candidate people)")
    for k, v in sorted(intro.items()):
        if len(v) > 1: print(f"  {k}: {sorted(v)}")
    print("\n== counted constructions (check the book uses one number per thing)")
    by = defaultdict(list)
    for (num, noun, f), c in counts.items(): by[noun].append(f"{num}@{f}×{c}")
    for noun, v in sorted(by.items()):
        if len({x.split('@')[0] for x in v}) > 1: print(f"  {noun}: {', '.join(sorted(v))}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir"); ap.add_argument("bible", nargs="?"); ap.add_argument("--readme"); ap.add_argument("--order")
    ap.add_argument("--discover", action="store_true")
    a = ap.parse_args()
    files = load(a.dir, a.order)
    if a.discover: discover(files); return
    bible = json.load(open(a.bible, encoding="utf-8")) if a.bible else {}
    issues = defaultdict(list)

    for e in bible.get("terms", []):
        home = e["home"]
        for n, t in files.items():
            b = strip(t)
            if chap(n) and chap(n) != home and re.search(r"\*\*[^*]*\b" + re.escape(e["term"]) + r"\b[^*]*\*\*", b, re.I):
                issues["term bolded outside home"].append(f"{n}: **{e['term']}** (home {home})")
            for v in e.get("variants", []):
                for i, l in lines_with(b, r"\b" + re.escape(v) + r"\b"):
                    issues["term variant"].append(f"{n}:{i}: '{v}' → '{e['term']}'")
    for e in bible.get("people", []):
        for n, t in files.items():
            if not chap(n) or chap(n) == e["home"]: continue
            for intro in e.get("intro", []):
                for i, l in lines_with(strip(t), re.escape(intro)):
                    issues["re-introduced outside home"].append(f"{n}:{i}: {intro} (home {e['home']}) — make it a callback")
    for e in bible.get("counts", []):
        for n, t in files.items():
            for m in re.finditer(e["pattern"], strip(t), re.I):
                if m.group(1).lower() != e["value"].lower():
                    issues["count mismatch"].append(f"{n}: '{m.group(0)}' (bible: {e['value']})")
    for e in bible.get("repeats", []):
        for n, t in files.items():
            if chap(n) and chap(n) != e["home"] and e["anchor"].lower() in strip(t).lower():
                issues["repeat outside home"].append(f"{n}: [{e['id']}] '{e['anchor']}' (home {e['home']})")
    for e in bible.get("names", []):
        for n, t in files.items():
            for v in e["variants"]:
                for i, l in lines_with(t, r"\b" + re.escape(v) + r"\b"):
                    issues["name variant"].append(f"{n}:{i}: '{v}' → '{e['canonical']}'")

    # titles across places
    titles = {}
    for n, t in files.items():
        m = re.search(r"(?m)^# Chapter (\d+): (.+)$", t)
        if m: titles[int(m.group(1))] = m.group(2).strip()
    def compare(src_name, text, rx):
        for m in re.finditer(rx, text, re.M):
            num, title = int(m.group(1)), m.group(2).strip().rstrip("|").strip()
            canon = titles.get(num)
            norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower().replace("’", "'"))
            if canon and norm(canon) not in norm(title):
                issues["title mismatch"].append(f"{src_name}: Chapter {num} '{title[:60]}' vs file '{canon}'")
    refs = files.get("appendix-references.md", "")
    compare("appendix-references", refs, r"^## Chapter (\d+) — (.+)$")
    ev = files.get("appendix-note-on-evidence.md", "")
    compare("note-on-evidence", ev, r"^\| (\d+)\. ([^|]+)\|")
    if a.readme and Path(a.readme).exists():
        compare("README", Path(a.readme).read_text(encoding="utf-8"), r"Chapter (\d+) — ([^\]\n]+)\]")

    # cross-references
    maxch = max(titles) if titles else 99
    for n, t in files.items():
        b = strip(t)
        for i, l in lines_with(b, r"\bChapter (\d+)\b"):
            for num in re.findall(r"\bChapter (\d+)\b", l):
                if int(num) > maxch: issues["reference to missing chapter"].append(f"{n}:{i}: Chapter {num}")
        for i, l in lines_with(b, r"\b(this chapter|the rest of (this|the) (book|chapter)|the next chapter|the previous chapter|earlier chapter)\b", re.I):
            issues["scope phrases to review"].append(f"{n}:{i}: {l[:140]}")

    for k, v in issues.items():
        print(f"\n== {k} ({len(v)})")
        for x in v[:40]: print("  ", x)
    if not issues: print("no issues")

if __name__ == "__main__":
    main()

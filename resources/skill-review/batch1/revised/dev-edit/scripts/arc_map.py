#!/usr/bin/env python3
"""Map a manuscript's structure so arc claims rest on numbers, not impressions.

  arc_map.py CHAPTER_DIR [--order book-order.json]       # table per file + part totals
  arc_map.py CHAPTER_DIR --handoffs                      # chapter END vs next chapter START (+ apparatus seams)
  arc_map.py CHAPTER_DIR --motifs "camel,loose cable,coffee"   # counts per file; QUOTE the list
  arc_map.py CHAPTER_DIR --recaps                        # sentences sharing 5-word runs with an earlier chapter
  arc_map.py CHAPTER_DIR --numbers                       # decimals/percentages restated in more than one file
  arc_map.py CHAPTER_DIR --markers                       # unresolved drafting markers per file
  arc_map.py CHAPTER_DIR --provenance 21                 # lines the author changed himself in the last 21 days
  arc_map.py CHAPTER_DIR --protected FILE                # exit 1 if a listed line is missing

Files named part-*.md open a part; numbered files and others are counted inside the
current part. Without --order, files sort by name. Numbers describe the text; they
do not score it. Every list this prints is a list of candidates for you to read.
Runs on python 3.8+ (tested 3.11, 3.12). Provenance needs git.
"""
import argparse, json, re, subprocess, time
from pathlib import Path

MARKERS = r"CLAUDE DRAFT|CLAUDE EDIT|ASSISTANT EDIT|ASSISTANT DRAFT|SLOT ?\d*|TODO|AUTHOR:|EDITORIAL|\[Missing figure\]"
BOTS = re.compile(r"^(Claude|github-actions|dependabot)", re.I)
# Mechanical passes that would otherwise "own" lines the author wrote (System 3:
# typography 1bce77f, copyedit 75e80c2, both 30 Sep 2026). Used only if present in the repo.
DEFAULT_IGNORE_REVS = ["1bce77f", "75e80c2"]
# Commit summaries that suggest an assistant's edit committed under the author's name
# (System 3: 8bcaac3 "Apply developmental edit F…"). Marked "?" in --provenance: ask him.
ASSISTED = re.compile(r"\b(apply|applied|claude|assistant|edit [A-Z]\b|pass\b)", re.I)


def body(t):
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"```\{=latex\}.*?```", "", t, flags=re.S)   # layout TeX only
    t = re.sub(r"(?m)^```[\w{}=.-]*\s*$", "", t)            # keep other fenced text (Zen appendix, prompts)
    t = re.sub(r"(?m)^\[\^[^\]]+\]:.*$", "", t)
    return t


def paras(t):
    """Prose paragraphs, without headings, tables, images, rules, the italic subtitle
    under the H1 and italic captions under images."""
    out, prev = [], ""
    for b in body(t).split("\n\n"):
        b = b.strip()
        italic_only = bool(re.fullmatch(r"\*[^*].*\*", b, flags=re.S)) if b else False
        if b and not b.startswith(("#", "|", "!", "---", "<")) \
           and not (italic_only and (prev.startswith(("#", "!")) or not out)):
            out.append(" ".join(b.split()))
        prev = b or prev
    return out


def sents(t):
    flat = " ".join(paras(t))
    flat = re.sub(r"\[\^[^\]]+\]|\[\d+\]\([^)]*\)", "", flat)
    return [s.strip() for s in re.split(r"(?<=[.!?”])\s+(?=[A-Z“*>])", flat) if s.strip()]


FIRST = r"\b(?:I|I[’']m|I[’']ve|I[’']d|I[’']ll|[Mm]y|[Mm]e|[Mm]yself)\b"


def stats(t):
    b = body(t); w = max(1, len(b.split()))
    return {
        "words": w,
        "heads": len(re.findall(r"(?m)^#{2,4} ", b)),
        "notes": len(set(re.findall(r"\[\^([^\]]+)\](?!:)", t))) + len(re.findall(r"\]\(appendix-references\.md#", t)),
        "bold/1k": 1000 * len(re.findall(r"\*\*[^*]+\*\*", b)) / w,
        "I/1k": 1000 * len(re.findall(FIRST, b)) / w,
        "markers": len(re.findall(MARKERS, t)),
    }


def load(d, order):
    d = Path(d)
    disk = sorted(p.name for p in d.glob("*.md"))
    if not order:
        return [(n, (d / n).read_text(encoding="utf-8")) for n in disk]
    names = json.load(open(order, encoding="utf-8"))
    for m in sorted(set(names) - set(disk)):
        print(f"warning: in order but missing on disk: {m}")
    for m in sorted(set(disk) - set(names)):
        print(f"warning: on disk but not in order: {m}")
    return [(n, (d / n).read_text(encoding="utf-8")) for n in names if (d / n).exists()]


def shingles(s, k=5):
    w = re.findall(r"[a-z’']+", s.lower())
    return {" ".join(w[i:i + k]) for i in range(len(w) - k + 1)}


def git(cwd, *args):
    return subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True)


def provenance(path, days, extra_ignore=()):
    """Lines the author (not Claude, not a bot) last changed in the past `days` days.
    A commit under his name can still carry an assistant's edit: read the summary."""
    p = Path(path).resolve()
    root = Path(git(p.parent, "rev-parse", "--show-toplevel").stdout.strip() or p.parent)
    cmd = ["blame", "-w", "-M", "--line-porcelain"]
    if (root / ".git-blame-ignore-revs").exists():
        cmd += ["--ignore-revs-file", str(root / ".git-blame-ignore-revs")]
    for rev in list(DEFAULT_IGNORE_REVS) + list(extra_ignore):
        if git(root, "cat-file", "-e", rev + "^{commit}").returncode == 0:
            cmd += ["--ignore-rev", rev]
    r = git(p.parent, *cmd, "--", p.name)
    if r.returncode != 0:
        return [f"  (git blame failed: {r.stderr.strip()[:120]})"]
    cutoff, n, hits = time.time() - days * 86400, 0, []
    sha = who = summ = ""; t = 0
    for line in r.stdout.splitlines():
        if re.match(r"^[0-9a-f]{40} ", line): sha = line[:7]
        elif line.startswith("author "): who = line[7:]
        elif line.startswith("author-time "): t = int(line[12:])
        elif line.startswith("summary "): summ = line[8:]
        elif line.startswith("\t"):
            n += 1; text = line[1:].strip()
            if text and not text.startswith(("<!--", "```", "![")) and not BOTS.match(who) and t >= cutoff:
                maybe = "?" if ASSISTED.search(summ) else " "
                hits.append(f"  L{n:<4} {sha}{maybe} {time.strftime('%d %b', time.localtime(t))}  "
                            f"{summ[:45]:45}  {text[:80]}")
    return hits


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dir"); ap.add_argument("--order")
    ap.add_argument("--handoffs", action="store_true")
    ap.add_argument("--motifs", help='comma-separated; quote the whole list when a term has a space, '
                    'e.g. "loose cable,camel". Matches word starts ("cable" counts "cables"); '
                    r'add \b for an exact end, e.g. "cat\b". A grid misses payoffs that do not repeat the word.')
    ap.add_argument("--recaps", action="store_true")
    ap.add_argument("--min-shared", type=int, default=3,
                    help="recaps: shared 5-word runs needed to report a pair (default 3)")
    ap.add_argument("--numbers", action="store_true",
                    help="decimals and percentages that appear in more than one file, with context")
    ap.add_argument("--markers", action="store_true")
    ap.add_argument("--provenance", type=int, metavar="DAYS",
                    help="lines the author changed himself in the last DAYS days (needs git)")
    ap.add_argument("--ignore-rev", action="append", default=[],
                    help="provenance: extra mechanical commit to look through (repeatable)")
    ap.add_argument("--only", help="comma-separated file-name prefixes to limit --provenance, e.g. 10-,01-")
    ap.add_argument("--protected", metavar="FILE", help="exit 1 if any listed line is missing from the text")
    a = ap.parse_args()
    files = load(a.dir, a.order)
    main_files = [(n, t) for n, t in files if not n.startswith(("appendix", "about", "back-matter"))]

    print(f"{'file':40}{'words':>7}{'heads':>6}{'notes':>6}{'bold/1k':>8}{'I/1k':>7}{'markers':>8}")
    part, totals = "(front)", {}
    for n, t in files:
        if n.startswith(("part-", "alternative", "back-matter", "interlude")):
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
        def seam(n1, t1, n2, t2):
            s1, s2 = sents(t1), sents(t2)
            print(f"\n{n1} → {n2}\n   END:   {' '.join(s1[-2:])[:300]}\n   START: {' '.join(s2[:2])[:300]}")
        print("\n== handoffs: chapter to chapter (part pages, reveal and interlude skipped)")
        chaps = [(n, t) for n, t in main_files if not n.startswith("part-")]
        for (n1, t1), (n2, t2) in zip(chaps, chaps[1:]):
            seam(n1, t1, n2, t2)
        print("\n== apparatus seams (count the ceremony)")
        for (n1, t1), (n2, t2) in zip(main_files, main_files[1:]):
            if n1.startswith("part-") or n2.startswith("part-"):
                seam(n1, t1, n2, t2)

    if a.motifs:
        terms = [m.strip() for m in a.motifs.split(",") if m.strip()]
        print("\n== motifs (count per file; blank = absent)")
        print(f"{'file':40}" + "".join(f"{m[:11]:>12}" for m in terms))
        pats = [re.compile(r"\b" + r"\s+".join(re.escape(w) for w in m.lower().split()).replace(r"\\b", r"\b"))
                for m in terms]
        for n, t in main_files:
            b = body(t).lower()
            row = [len(p.findall(b)) for p in pats]
            if any(row):
                print(f"{n[:40]:40}" + "".join(f"{(str(c) if c else ''):>12}" for c in row))

    if a.recaps:
        print(f"\n== sentences sharing ≥ {a.min_shared} five-word runs with an earlier chapter "
              "(re-teaching, or a deliberate callback: you decide) [shared runs]")
        prose = [(n, t) for n, t in main_files if not n.startswith("part-")]
        seen = []
        for n, t in prose:
            mine = [(s, shingles(s)) for s in sents(t) if not s.startswith(">")]
            for s, sh in mine:
                if len(sh) < 4:
                    continue
                k, n0, s0 = max(((len(sh & sh0), n0, s0) for n0, s0, sh0 in seen), default=(0, "", ""))
                if k >= a.min_shared:
                    print(f"\n  {n}: {s[:200]}\n    ≈ {n0}: {s0[:200]}  [{k}]")
            seen += [(n, s, sh) for s, sh in mine if len(sh) >= 4]

    if a.numbers:
        print("\n== numbers restated across files (check each restatement against its source chapter)")
        where = {}
        for n, t in main_files:
            for s in sents(t):
                for m in re.findall(r"(?<![\w.])\d+\.\d+(?![\w.]*\d)|\d+(?:\.\d+)?\s?%|\d+ per ?cent", s):
                    where.setdefault(m.replace(" ", ""), []).append((n, s))
        for num, occ in sorted(where.items(), key=lambda kv: kv[0]):
            if len({n for n, _ in occ}) > 1:
                print(f"\n  {num}")
                for n, s in occ:
                    print(f"    {n[:32]:32} {s[:170]}")

    if a.markers:
        print("\n== unresolved markers")
        for n, t in files:
            for m in re.finditer(r"<!--[^>]{0,40}(?:" + MARKERS + r")[^>]{0,80}", t):
                print(f"  {n}: {' '.join(m.group(0).split())[:150]}")
            for m in re.finditer(r"\*?\[Missing figure\]\*?", t):
                print(f"  {n}: {m.group(0)}")

    if a.provenance:
        only = tuple(x.strip() for x in a.only.split(",")) if a.only else None
        print(f"\n== the author's own changes in the last {a.provenance} days "
              "(his decisions: ask before cutting; read the commit summary)")
        for n, _ in files:
            if only and not n.startswith(only):
                continue
            hits = provenance(Path(a.dir) / n, a.provenance, a.ignore_rev)
            if hits:
                print(f"\n{n}\n" + "\n".join(hits))

    if a.protected:
        whole = "\n".join(" ".join(t.split()) for _, t in files)
        lines = [l.strip() for l in Path(a.protected).read_text(encoding="utf-8").splitlines()
                 if l.strip() and not l.lstrip().startswith("#")]
        gone = [l for l in lines if " ".join(l.split()) not in whole]
        print("\n== protected lines missing" if gone else f"\n== protected lines: all {len(lines)} present")
        for l in gone:
            print(f"  MISSING  {l}\n    then: git log -S\"{l[:40]}\" --oneline -- {a.dir}")
        if gone:
            raise SystemExit(1)


if __name__ == "__main__":
    main()

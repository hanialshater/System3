#!/usr/bin/env python3
"""Find corrections that were made in git history and have since come undone.

  regressions.py [CHAPTER_DIR] [--files 08-automatic-alignment-research.md,00-preface.md] [--all] [--since 2026-09-01]

Run from inside the repository. For every commit that touched the chapters and
whose message looks like a correction (fact, verif, correct, attribut, source,
claim, accuracy, reword, drop, remove; --all takes every commit), the script
compares the lines it removed with the lines it added. It reports a commit when
both are true in the current text:
  - wording the commit removed is back (a run of 4+ words unique to the old line), and
  - wording the commit added is gone (the correction itself no longer stands).
That pattern is a correction that a later edit or merge silently reversed, e.g. an
attribution removed as unverified and later restored. Each hit is a lead, not a
verdict: read `git show <hash>` and the current paragraph before calling it a regression.
"""
import argparse, re, subprocess, sys
from pathlib import Path

KEYS = r"fact|verif|correct|attribut|source|claim|accura|reword|drop|remov|unsupported|cite|citation"


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def words(s):
    # Citation links, anchors and list numbers change with every renumbering; they are not wording.
    s = re.sub(r"\[\d+\]\([^)]*\)|<a id=\"[^\"]*\"></a>|^\s*\d+\.\s|<[^>]+>", " ", s)
    return re.findall(r"[\w’'\-]+", s.lower())


def grams(s, n=4):
    w = words(s)
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dir", nargs="?", default="chapters")
    ap.add_argument("--files", help="comma-separated chapter files to limit the search to")
    ap.add_argument("--all", action="store_true", help="look at every commit, not only correction-like ones")
    ap.add_argument("--since", help="only commits after this date (YYYY-MM-DD)")
    a = ap.parse_args()
    d = Path(a.dir)
    paths = [str(d / f.strip()) for f in a.files.split(",")] if a.files else [str(d)]
    log = ["log", "--format=%h%x09%ad%x09%s", "--date=short"] + (["--since", a.since] if a.since else []) + ["--"] + paths
    hits = 0
    for line in git(*log).splitlines():
        h, date, subj = line.split("\t", 2)
        if not a.all and not re.search(KEYS, subj, re.I):
            continue
        diff = git("show", "--format=", "--unified=0", h, "--", *paths)
        cur_file, rem, add = None, {}, {}
        for l in diff.splitlines():
            if l.startswith("+++ "):
                cur_file = l[6:] if l.startswith("+++ b/") else None
            elif l.startswith("-") and not l.startswith("---") and cur_file:
                rem.setdefault(cur_file, []).append(l[1:])
            elif l.startswith("+") and not l.startswith("+++") and cur_file:
                add.setdefault(cur_file, []).append(l[1:])
        for f in rem:
            p = Path(f)
            if not p.exists():
                continue
            now = " ".join(words(p.read_text(encoding="utf-8")))
            added = set().union(*(grams(x) for x in add.get(f, []))) if add.get(f) else set()
            removed = set().union(*(grams(x) for x in rem[f]))
            back = sorted(g for g in removed - added if f" {g} " in f" {now} ")
            gone = [g for g in added - removed if f" {g} " not in f" {now} "]
            if back and added and len(gone) >= max(1, len(added - removed) // 2):
                hits += 1
                print(f"\n== {h} {date} {subj}\n   file: {f}")
                print(f"   removed wording back in current text: {'; '.join(back[:6])}{' …' if len(back) > 6 else ''}")
                print(f"   added wording now gone: {'; '.join(gone[:6])}{' …' if len(gone) > 6 else ''}")
    if not hits:
        print("No reversed corrections found" + ("" if a.all else " among correction-like commits (try --all)") + ".")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        sys.exit(f"git failed: {e.stderr.strip()} (run from inside the repository)")

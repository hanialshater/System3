#!/usr/bin/env python3
"""Guard the lines a pass must not touch, and prove it afterwards.

Three sources of guarded sentences, each checked verbatim:
  protected   references/protected.txt (the author's list; exact strings)
  restored    sentences added by commits whose subject says "Restore…", plus
              quotes in resources/evaluations/*revert-list*.md, that are still
              in the chapter (the author took these back; do not re-cut them)
  seed        easter-egg anchors from resources/editorial/check-eggs.sh

Usage:
  protected.py --repo REPO --audit
      Before a pass: is every protected.txt line still somewhere in chapters/?
      Missing lines are listed with the commit that removed them.
  protected.py --repo REPO --chapter chapters/11-the-store-that-builds-itself.md --list
      Print the guarded sentences for one chapter (read them before choosing cuts).
  protected.py --repo REPO --chapter chapters/11-....md --check COPY.md [--since 2026-10-02]
      After a pass: how many guarded sentences survive verbatim in COPY.md.
      Prints "restored: 47/48 kept" and every changed sentence; exits 1 if any
      changed. Quote these counts in the report instead of asserting "untouched".

Never writes anything. Python 3.11+.
"""
import argparse, re, signal, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
PROTECTED_TXT = HERE.parent / "references" / "protected.txt"
SENT = re.compile(r"(?<=[.!?…])[”’\"*)]*\s+(?=[A-Z“\"*`(‘])")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def sentences(text):
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    out = []
    for block in re.split(r"\n\s*\n", text):
        block = norm(block)
        if not block or block.startswith(("|", "```", "<", "!")):
            continue
        block = re.sub(r"^#+\s*", "", block)
        for s in SENT.split(block):
            s = s.strip()
            if len(s.split()) >= 3:
                out.append(s)
    return out


def git(repo, *args):
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def protected_lines():
    if not PROTECTED_TXT.exists():
        return []
    return [l.strip() for l in PROTECTED_TXT.read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.lstrip().startswith("#")]


def restored_sentences(repo, chapter, base, since=None):
    """Sentences the author put back, still present in the base text."""
    found = []
    args = ["log", "--format=%x00%h %s", "-p", "--no-color", "-U0"]
    if since:
        # a bare date means midnight; git would otherwise use the current time of day
        args.append(f"--since={since} 00:00:00" if re.fullmatch(r"\d{4}-\d\d-\d\d", since) else f"--since={since}")
    log = git(repo, *args, "--", chapter)
    for commit in log.split("\x00")[1:]:
        head, _, diff = commit.partition("\n")
        if not re.search(r"(?i)\brestor", head.split(" ", 1)[-1]):
            continue
        added = "\n".join(l[1:] if l[1:].strip() else "" for l in diff.splitlines()
                          if l.startswith("+") and not l.startswith("+++"))
        found += [(s, head.split()[0]) for s in sentences(added)]
    # quotes in revert lists whose ID matches this chapter
    m = re.match(r"(\d\d)-", Path(chapter).name)
    pre = f"R{int(m.group(1))}-" if m else "RP-" if "preface" in chapter else None
    for rl in sorted((Path(repo) / "resources" / "evaluations").glob("*revert-list*.md")):
        for line in rl.read_text(encoding="utf-8").splitlines():
            idm = re.match(r"- \*\*(R[A-Z0-9]*-\d+)\*\*", line)
            if not idm or not pre or not idm.group(1).startswith(pre):
                continue
            for q in re.findall(r"\"([^\"]{12,})\"", line):
                found += [(s, f"{rl.name}:{idm.group(1)}") for s in sentences(q)]
    nb, seen, out = norm(base), set(), []
    for s, src in found:
        if s not in seen and s in nb:
            seen.add(s); out.append((s, src))
    return out


def seed_anchors(repo, chapter):
    sh = Path(repo) / "resources" / "editorial" / "check-eggs.sh"
    if not sh.exists():
        return []
    name = Path(chapter).name
    return [(a, tier) for tier, f, a in re.findall(r'^check (\w+) (\S+) "(.*)"$', sh.read_text(encoding="utf-8"), re.M)
            if f == name]


def guarded(repo, chapter, since=None):
    """[(kind, sentence, source)] for one chapter, all present in the repo's current text."""
    base = (Path(repo) / chapter).read_text(encoding="utf-8")
    nb = norm(base)
    g = [("protected", p, "protected.txt") for p in protected_lines() if norm(p) in nb]
    g += [("restored", s, src) for s, src in restored_sentences(repo, chapter, base, since)]
    g += [("seed", a, t) for a, t in seed_anchors(repo, chapter) if norm(a) in nb]
    return g


def check(guards, text):
    nt = norm(text)
    return [(k, s, src) for k, s, src in guards if norm(s) not in nt]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", required=True, help="System 3 repo root (read only)")
    ap.add_argument("--chapter", help="chapter path inside the repo, e.g. chapters/11-....md")
    ap.add_argument("--check", metavar="COPY", help="edited copy to verify against the guarded sentences")
    ap.add_argument("--list", action="store_true", help="print the guarded sentences")
    ap.add_argument("--audit", action="store_true", help="check protected.txt against chapters/")
    ap.add_argument("--since", help="only restore commits since this date (e.g. 2026-10-02)")
    a = ap.parse_args()
    repo = Path(a.repo)
    if a.audit:
        allt = norm("\n".join(p.read_text(encoding="utf-8") for p in sorted((repo / "chapters").glob("*.md"))))
        miss = [p for p in protected_lines() if norm(p) not in allt]
        for p in miss:
            who = git(repo, "log", "-1", "--format=%h %an %ad %s", "--date=short", "-S", p, "--", "chapters").strip()
            print(f"MISSING {p!r}\n        last change: {who or 'unknown'}")
        print(f"protected.txt: {len(protected_lines()) - len(miss)}/{len(protected_lines())} present in chapters/")
        sys.exit(1 if miss else 0)
    if not a.chapter:
        ap.error("--chapter is required unless --audit")
    if Path(a.chapter).name.startswith("13-") or Path(a.chapter).name in ("alternative-ending.md", "14-scaffolds.md"):
        print("WARNING: this file is protected in full (typography only). No pass edits it.")
    g = guarded(repo, a.chapter, a.since)
    if a.list or not a.check:
        for k, s, src in g:
            print(f"[{k}] {s}    ({src})")
        print(f"\n{len(g)} guarded sentences in {a.chapter}")
    if a.check:
        miss = check(g, Path(a.check).read_text(encoding="utf-8"))
        for kind in ("protected", "restored", "seed"):
            n = sum(1 for k, *_ in g if k == kind)
            m = [x for x in miss if x[0] == kind]
            print(f"{kind}: {n - len(m)}/{n} kept verbatim")
            for _, s, src in m:
                print(f"   CHANGED ({src}): {s}")
        sys.exit(1 if miss else 0)


if __name__ == "__main__":
    main()

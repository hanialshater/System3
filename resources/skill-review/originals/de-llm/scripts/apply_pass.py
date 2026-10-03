#!/usr/bin/env python3
"""Template for one de-LLM pass. Copy it, fill EDITS, run it.

  python3 apply_pass.py chapters/06-pattern-language.md --name "de-LLM pass" \
      --log pass_log.json --changes CHANGES.md

Each edit is (old, new, why, flag):
  old   exact text; must occur exactly once, or the edit is skipped with FAIL
        (so the same script runs safely on a later version of the file)
  new   replacement; '' deletes
  why   short reason, shown in the change list ("signpost", "restates the
        paragraph before", "seven-sentence anaphoric run folded into one")
  flag  None for pure cuts/folds of the author's own words; a note when ANY
        new or recast wording enters the text. The note becomes an inline
        <!-- ASSISTANT EDIT (<name>): note --> before the edited paragraph.
"""
import argparse, json, re, sys

EDITS = [
    # ("old text", "new text", "why", None),
    # ("Suppose the budget owner", "Say the budget owner", "opener tic", '"Say" replaces "Suppose".'),
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--name", default="de-LLM pass")
    ap.add_argument("--log", default="pass_log.json")
    ap.add_argument("--changes", default="CHANGES.md")
    a = ap.parse_args()
    s = open(a.path, encoding="utf-8").read()
    w0 = len(re.sub(r"<!--.*?-->", "", s, flags=re.S).split())
    log, fails = [], 0
    for old, new, why, flag in EDITS:
        n = s.count(old)
        if n != 1:
            print(f"FAIL ({n} matches): {old[:80]!r}"); fails += 1; continue
        if flag:
            # put the flag at the start of the paragraph that contains the edit
            i = s.index(old); start = s.rfind("\n\n", 0, i); start = 0 if start < 0 else start + 2
            s = s[:start] + f"<!-- ASSISTANT EDIT ({a.name}): {flag} -->\n" + s[start:]
        s = s.replace(old, new, 1)
        log.append({"old": old, "new": new, "why": why, "flag": flag})
    open(a.path, "w", encoding="utf-8").write(s)
    w1 = len(re.sub(r"<!--.*?-->", "", s, flags=re.S).split())
    json.dump(log, open(a.log, "w"), ensure_ascii=False, indent=1)
    out = [f"# {a.name}: {a.path}", "",
           f"{len(log)} changes, {fails} skipped. Words {w0:,} → {w1:,} ({w1 - w0:+,}).",
           "Every cut is struck through with its reason, so any line can be restored.", ""]
    for i, e in enumerate(log, 1):
        o = re.sub(r"\s+", " ", e["old"]).strip(); nw = re.sub(r"\s+", " ", e["new"]).strip()
        out += [f"**{i}. {e['why'][0].upper() + e['why'][1:]}.**" + (" *(new wording, flagged)*" if e["flag"] else ""),
                f"> ~~{o[:700]}~~"] + ([f"> → {nw}"] if nw else []) + [""]
    open(a.changes, "w", encoding="utf-8").write("\n".join(out))
    print(f"{len(log)} applied, {fails} failed; words {w0} -> {w1}; log {a.log}; changes {a.changes}")
    sys.exit(1 if fails and not log else 0)

if __name__ == "__main__":
    main()

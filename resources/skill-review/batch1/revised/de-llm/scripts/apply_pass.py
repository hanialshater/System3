#!/usr/bin/env python3
"""Template for one de-LLM pass. Copy it and protected.py next to your outputs, fill EDITS
and KEEPS, run it on a COPY of the chapter (never on the repo file when the repo is read-only).

  python3 apply_pass.py work/ch11.md --name "de-LLM pass" \
      --log work/ch11.pass.json --changes work/CHANGES.md \
      --repo /home/user/System3 --chapter chapters/11-the-store-that-builds-itself.md

Each edit is (old, new, why, flag):
  old   exact text from the chapter; must occur exactly once, or the edit is skipped
        with FAIL. Type curly quotes and apostrophes (’ “ ”) as the manuscript has them.
  new   replacement; '' deletes
  why   short reason, shown in the change list ("signpost", "restates the
        paragraph before", "seven-sentence anaphoric run folded into one"). Required.
  flag  None for pure cuts/folds of the author's own words; a note when ANY
        new or recast wording enters the text. The note becomes an inline
        <!-- ASSISTANT EDIT (<name>): note Was: '<old>' --> before the edited paragraph.
        The build strips HTML comments; the author deletes the markers on sign-off.

Each keep is (text, why): a candidate the pass looked at and left alone on purpose.
The reason is required, exactly as for a cut; the change list prints every keep.

Edits apply in order. An edit whose old text overlaps an earlier edit's new text is
refused: it would be editing Claude's wording as if it were the author's.

With --repo and --chapter, the result is checked against the guarded sentences
(protected list, lines the author restored, easter-egg anchors; see protected.py).
If any would change, nothing is written unless --allow-guarded, and then the change
list names each one under "Guarded lines changed".

Exit 0 only when every edit applied. Nothing is written if the edit list is malformed.
  python3 apply_pass.py --selftest     # checks this script on a temporary file
"""
import argparse, json, re, sys, tempfile
from pathlib import Path

EDITS = [
    # ("old text", "new text", "why", None),
    # ("Suppose the budget owner", "Say the budget owner", "opener tic", '"Say" replaces "Suppose".'),
]
KEEPS = [
    # ("Nobody is lying. The hypothesis has been fitted to the result.", "parallel carries the joke"),
]


def words(s):
    return len(re.sub(r"<!--.*?-->", "", s, flags=re.S).split())


def validate(edits, keeps):
    bad = [e for e in edits if len(e) != 4 or not e[0] or not str(e[2]).strip()]
    bad += [k for k in keeps if len(k) != 2 or not k[0] or not str(k[1]).strip()]
    if bad:
        sys.exit("bad edit or keep (needs old text and a reason; keeps need a reason too):\n  "
                 + "\n  ".join(repr(b)[:160] for b in bad))


def cap(why):
    why = str(why).strip().rstrip(".")
    return why[:1].upper() + why[1:]


def run(path, name, log_path, changes_path, edits, keeps, repo=None, chapter=None, allow_guarded=False):
    validate(edits, keeps)
    s0 = s = Path(path).read_text(encoding="utf-8")
    m = re.match(r"(\d\d)-", Path(chapter or path).name)
    tag = f"C{int(m.group(1))}" if m else Path(path).stem[:8]
    log, skipped = [], []
    for old, new, why, flag in edits:
        n = s.count(old)
        if n != 1:
            print(f"FAIL ({n} matches): {old[:80]!r}")
            if n == 0 and ("'" in old or '"' in old):
                print("   hint: the manuscript uses curly quotes (’ “ ”); retype the old text")
            skipped.append((old, f"{n} matches")); continue
        if any(e["new"] and (e["new"] in old or old in e["new"]) for e in log):
            print(f"FAIL (overlaps an earlier edit's new text): {old[:80]!r}")
            skipped.append((old, "edits Claude's own wording from an earlier edit")); continue
        i = s.index(old)
        s = s[:i] + new + s[i + len(old):]               # replace first, so the flag's "Was:" is never matched
        if flag:
            start = s.rfind("\n\n", 0, i); start = 0 if start < 0 else start + 2
            was = re.sub(r"\s+", " ", old)[:200].replace("--", "–")
            s = s[:start] + f"<!-- ASSISTANT EDIT ({name}): {flag} Was: {was!r} -->\n" + s[start:]
        log.append({"id": f"{tag}-{len(log) + 1}", "old": old, "new": new, "why": why, "flag": flag})

    guarded_hit = []
    if repo and chapter:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        try:
            import protected
        except ImportError:
            sys.exit("protected.py not found: copy it next to this script (cp <skill>/scripts/protected.py .)")
        g = protected.guarded(repo, chapter)
        before = set(protected.check(g, s0))          # already missing in the copy before the pass
        guarded_hit = [x for x in protected.check(g, s) if x not in before]
        for k, sent, src in guarded_hit:
            print(f"GUARDED ({k}, {src}): {sent[:100]!r}")
        if guarded_hit and not allow_guarded:
            print(f"{len(guarded_hit)} guarded sentence(s) would change. Nothing written. "
                  "Drop those edits, or ask the author and rerun with --allow-guarded.")
            return 1

    w0, w1 = words(s0), words(s)
    out = [f"# {name}: {path}", "",
           f"{len(log)} changes, {len(skipped)} skipped, {len(keeps)} kept on purpose. "
           f"Words {w0:,} → {w1:,} ({w1 - w0:+,}; comments excluded).",
           "Every cut is struck through with its reason, so any line can be restored by its ID.", ""]
    for e in log:
        o = re.sub(r"\s+", " ", e["old"]).strip(); nw = re.sub(r"\s+", " ", e["new"]).strip()
        out += [f"**{e['id']}. {cap(e['why'])}.**" + (" *(new wording, flagged)*" if e["flag"] else ""),
                f"> ~~{o[:700]}~~"] + ([f"> → {nw}"] if nw else []) + [""]
    if keeps:
        out += ["## Kept on purpose", "", "| Line | Why it stays |", "|---|---|"]
        out += ["| " + re.sub(r"\s+", " ", t)[:200].replace("|", "/") + f" | {cap(w)} |" for t, w in keeps] + [""]
    if skipped:
        out += ["## Skipped", ""] + [f"- ({why}) " + re.sub(r"\s+", " ", o)[:120] for o, why in skipped] + [""]
    if guarded_hit:
        out += ["## Guarded lines changed (author approval needed)", ""]
        out += [f"- [{k}, {src}] {sent}" for k, sent, src in guarded_hit] + [""]
    Path(log_path).write_text(json.dumps(log, ensure_ascii=False, indent=1), encoding="utf-8")
    Path(changes_path).write_text("\n".join(out), encoding="utf-8")
    Path(path).write_text(s, encoding="utf-8")          # chapter last: no edit without a record
    print(f"{len(log)} applied, {len(skipped)} failed; words {w0} -> {w1}; log {log_path}; changes {changes_path}")
    return 1 if skipped else 0


def selftest():
    text = ("Para one has the agent’s proposal. So keep the losing branches.\n\n"
            "Twice here. Twice here.\n\nSuppose the budget owner says no.\n")
    with tempfile.TemporaryDirectory() as d:
        f, lg, ch = Path(d, "c.md"), Path(d, "l.json"), Path(d, "C.md")
        f.write_text(text, encoding="utf-8")
        # malformed list: nothing written
        try:
            run(f, "t", lg, ch, [("So keep", "", "", None)], []); assert False, "empty reason accepted"
        except SystemExit:
            pass
        assert f.read_text(encoding="utf-8") == text and not ch.exists(), "wrote despite bad edit"
        edits = [("Suppose the budget", "Say the budget", "opener tic", "Say replaces Suppose."),
                 ("Twice here.", "", "duplicate", None),                 # 2 matches
                 ("agent's proposal", "x", "straight quote", None),      # curly miss
                 ("Say the budget owner", "The owner", "edit own text", None)]  # overlaps earlier new
        rc = run(f, "t", lg, ch, edits, [("Para one", "the author's opener")])
        out, c = f.read_text(encoding="utf-8"), ch.read_text(encoding="utf-8")
        assert rc == 1, "partial failure must exit 1"
        assert "Say the budget owner" in out and "ASSISTANT EDIT (t)" in out and "Was: 'Suppose the budget'" in out
        assert "## Skipped" in c and "2 matches" in c and "Claude's own wording" in c
        assert "## Kept on purpose" in c and "The author's opener" in c and "**C" not in c
        assert "1 changes, 3 skipped" in c
    print("selftest ok")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", help="the chapter COPY to edit in place")
    ap.add_argument("--name", default="de-LLM pass")
    ap.add_argument("--log", help="JSON log path (outside the repo)")
    ap.add_argument("--changes", help="change list Markdown path (outside the repo)")
    ap.add_argument("--repo", help="System 3 repo, for the guarded-sentence check")
    ap.add_argument("--chapter", help="the chapter's path inside --repo, e.g. chapters/11-....md")
    ap.add_argument("--allow-guarded", action="store_true", help="only after the author approved those lines")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    if not (a.path and a.log and a.changes):
        ap.error("path, --log and --changes are required (put the log and change list next to your outputs)")
    sys.exit(run(a.path, a.name, a.log, a.changes, EDITS, KEEPS, a.repo, a.chapter, a.allow_guarded))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Lint Markdown prose against a house style sheet. Skips code, comments, URLs, raw LaTeX,
YAML and link targets. Reports; never edits.

  style_lint.py FILE_OR_DIR [...] [--only quotes,spelling,...]

Checks: quotes (straight quotes in prose), ellipsis (three periods), dash (spaced em dash,
double hyphen), spelling (British -> American list), numbers (numerals 1-100 in narrative
prose, excluding measurements, years, percentages, versions, tables), percent ('%' in prose),
heading (title case: words of 4+ letters capitalized, short function words lower),
compounds (house forms), bold (bold spans per 1,000 words; only coined terms should be bold),
serial (serial commas in short word lists — report only; rhythmic clause series keep theirs),
space (double spaces, trailing spaces).
"""
import argparse, re
from pathlib import Path

BRIT = {"catalogue": "catalog", "programme": "program", "travelled": "traveled", "fibre": "fiber", "colour": "color",
        "behaviour": "behavior", "labelled": "labeled", "grey": "gray", "anaesthetist": "anesthetist", "theatre": "theater",
        "organisation": "organization", "organise": "organize", "recognise": "recognize", "analyse": "analyze",
        "favour": "favor", "centre": "center", "modelling": "modeling", "judgement": "judgment", "plough": "plow",
        "defence": "defense", "licence": "license", "towards": "toward", "artefact": "artifact", "optimise": "optimize"}
COMPOUNDS = {r"\becommerce\b": "e-commerce", r"\be-mail\b": "email", r"\bdata set\b": "dataset", r"\bopen ended\b": "open-ended"}
SMALL = {"a", "an", "the", "and", "but", "or", "nor", "for", "so", "yet", "as", "at", "by", "in", "of", "off", "on", "per", "to", "via", "vs"}

def prose_lines(text):
    text = re.sub(r"<!--.*?-->", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    for i, line in enumerate(text.splitlines(), 1):
        if line.startswith(("    ", "\t", "|", "<", "\\")) or re.match(r"^\s*[\w_]+:\s", line):
            continue
        clean = re.sub(r"`[^`]*`", "", line)
        clean = re.sub(r"\[\d+\]\([^)]*\)", "", clean)
        clean = re.sub(r"\]\([^)]*\)|<https?://[^>]*>|https?://\S+", "]", clean)
        clean = re.sub(r"\[\^[^\]]+\]", "", clean)
        yield i, line, clean

def title_case_issues(h):
    out = []
    for seg in re.split(r"\s*[:—–]\s*", h):
        words = re.findall(r"[A-Za-z0-9’'][\w’'-]*", seg)
        for k, w in enumerate(words):
            if not w[0].isalpha(): continue
            edge = k == 0 or k == len(words) - 1
            if edge and w[0].islower(): out.append(w)
            elif not edge and len(w) >= 4 and w[0].islower(): out.append(w)
            elif not edge and w.lower() in SMALL and w[0].isupper(): out.append(w)
    return out

def lint(path, only):
    text = Path(path).read_text(encoding="utf-8"); hits = []
    words = max(1, len(text.split()))
    def add(kind, i, msg):
        if not only or kind in only: hits.append((kind, i, msg))
    for i, raw, l in prose_lines(text):
        if raw.startswith("#"):
            h = raw.lstrip("#").strip()
            bad = title_case_issues(re.sub(r"^Chapter \d+:\s*", "", h))
            if bad: add("heading", i, f"{h}  ← {', '.join(bad)}")
            continue
        if re.search(r"[A-Za-z]'[A-Za-z]|(^|\s)\"\w|\w[.,!?]?\"(\s|$)|(^|\s)'\w", l): add("quotes", i, l.strip()[:120])
        if "..." in l: add("ellipsis", i, l.strip()[:120])
        if re.search(r"\s—\s|\s--\s|\w--\w", l): add("dash", i, l.strip()[:120])
        for b, a in ({} if Path(path).name.startswith("appendix-references") else BRIT).items():
            if re.search(r"\b" + b + r"\b", l, re.I): add("spelling", i, f"{b} → {a}: {l.strip()[:90]}")
        for rx, a in COMPOUNDS.items():
            if re.search(rx, l, re.I): add("compounds", i, f"→ {a}: {l.strip()[:90]}")
        for m in re.finditer(r"(?<![\d.,$€£#v-])\b([1-9]\d?|100)\b(?![\d.,:%×x/-]|\s?(?:percent|per cent|ms|s\b|seconds|minutes|hours|days|GB|MB|k\b|px|pt|°|BCE|CE|AD|circles|th|st|nd|rd))", l):
            ctx = l[max(0, m.start() - 25):m.end() + 25]
            if not re.search(r"\b(19|20)\d\d\b|Chapter|chapter|Part|§|p\.|pp\.|Ch\.?|Layer|System|version|GPT|Opus|Reviewer|Move|step \d|\d+\.\d|from \d+ to|circle \d", ctx):
                add("numbers", i, f"'{m.group(0)}' in: …{ctx.strip()}…")
        if re.search(r"\d%", l): add("percent", i, l.strip()[:120])
        for m in re.finditer(r"\b(\w+), (\w+),? and (\w+)\b", l):
            if "," in m.group(0)[len(m.group(1)) + 2:]: add("serial", i, m.group(0))
        if re.search(r"\S  +\S", raw) or raw.endswith(" ") and not raw.endswith("  "): add("space", i, repr(raw[-40:]))
    bold = len(re.findall(r"\*\*[^*\n]+\*\*", re.sub(r"<!--.*?-->|```.*?```", "", text, flags=re.S)))
    if (not only or "bold" in only) and bold:
        hits.append(("bold", 0, f"{bold} bold spans ({1000 * bold / words:.1f}/1k words) — keep only coined terms at first definition"))
    return hits

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("paths", nargs="+"); ap.add_argument("--only", default="")
    a = ap.parse_args(); only = set(filter(None, a.only.split(",")))
    files = []
    for p in a.paths:
        pp = Path(p); files += sorted(pp.glob("*.md")) if pp.is_dir() else [pp]
    total = {}
    for f in files:
        hits = lint(f, only)
        if not hits: continue
        print(f"\n### {f.name}")
        for kind, i, msg in hits:
            total[kind] = total.get(kind, 0) + 1
            print(f"  {kind:9} L{i}: {msg}" if i else f"  {kind:9} {msg}")
    print("\nsummary:", ", ".join(f"{k} {v}" for k, v in sorted(total.items())) or "clean")

if __name__ == "__main__":
    main()

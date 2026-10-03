#!/usr/bin/env python3
"""Pull checkable claims out of Markdown chapters and flag the risky ones.

  claims.py CHAPTER_DIR [--order book-order.json]            # claim ledger as TSV on stdout
  claims.py CHAPTER_DIR --only fresh                         # recent events, dated or not
  claims.py CHAPTER_DIR --only risky                         # fresh + org-reported + superlative + present-tense status
  claims.py CHAPTER_DIR --numbers [--near "Navier,Fermat"]  # same unit, different numbers or qualifiers across files
  claims.py CHAPTER_DIR --notes                              # footnote and numbered-citation integrity
  claims.py CHAPTER_DIR --entries --files 07-recursive-self-improvement.md   # the appendix entries those files cite, to check one by one
  Add --files a.md,b.md to any mode to limit it to those chapters.

A claim is a sentence with a number, a year, a date, a superlative, a present-tense
status or an organization reporting something. "fresh" = a year >= --since, a date
whose year is only given earlier in the paragraph or section, or a term from
--recent (model names, live problems). Citations can be [^footnotes] or numbered
links into appendix-references.md; a sentence counts as sourced if its paragraph
carries one, since that is where this book puts them. The source column says which
citation a sentence relies on: its own, "next:" (the first citation after it in the
paragraph, which is how this book cites), or "before:" (only cited earlier: suspect).
"shared-cite(n)" means n claim sentences lean on one citation; check that the source
really covers each of them, not just the last. The ledger is a worklist for
verification, not a verdict: every row still needs a source checked by a person or
a search.
"""
import argparse, json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

ORGS = (r"\b(Anthropic|OpenAI|Google(?: DeepMind)?|DeepMind|Meta|Facebook|Microsoft|Clay(?: Mathematics Institute)?|CERN|"
        r"Nature|Science|arXiv|Amazon|Bing|NVIDIA|Prove2Me|xAI|Hugging Face|Redwood Research|METR|Epoch AI|Apollo Research|"
        r"Mistral|DeepSeek|Alibaba|Baidu|Apple|IBM|Wharton)\b")
MONTHS = r"(January|February|March|April|May|June|July|August|September|October|November|December)"
NUM = (r"(\d[\d,\.]*\s?(%|percent|per cent)?|\b(two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty|"
       r"thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion)\b)")
HEDGES = r"\b(reported|reportedly|announced|claimed|according to|says|said|stated|apparently|proposed|preprint|at the time of writing)\b"
REPORT = (r"\b(reported|reports|announced|announces|published|publishes|released|claimed|claims|found|finds|says|said|stated|"
          r"showed|shows|described|estimated|suspended|launched|gave|put|set)\b|’s (report|account|announcement|paper|post|blog|statement|analysis|study)")
# Versioned model names and live problems; a bare "Claude" or "Claude Code" is not a dated claim.
RECENT = (r"\b((?:Claude )?(?:Opus|Sonnet|Haiku) \d[\d.]*|Claude \d[\d.]*|(?:Claude )?Mythos(?: Preview)?|GPT-?[5-9][\w.]*|"
          r"o[3-9]\b|Gemini \d[\d.]*|Deep Think|Millennium (?:Prize )?Problems?)\b")
# Strong superlatives only; "most", "every" and "never" are everywhere in essay prose.
# Case-sensitive on purpose: "the first [Proper noun]" is a claim, "the first version" is not.
SUPER = (r"\b([Tt]he first (?:to\b|person|system|model|team|doctorate|[A-Z]\w+)|first[- ]ever|"
         r"[Tt]he only (?:case|game|person|system|model|team|group|lab)\b|largest|biggest|fastest|best-known|best known|"
         r"(?:new|previous|prior|world) record|record-\w+|unprecedented|state[- ]of[- ]the[- ]art|all-time|never before)")
STATUS = (r"\b(at the time of writing|as I write|currently|to date|has (?:already )?(?:been )?(?:set|built|solved|settled|"
          r"proved|released|shipped|announced|suspended|found)|have (?:already )?(?:set|built|solved|settled)|remains? (?:open|unsolved|unsettled|pending|under review)|"
          r"pending|is available|are available|no longer)\b")
# Someone's study, paper or system reporting a result, named or not.
RESULT = (r"\b(study|studies|paper|preprint|experiment|analysis|survey|benchmark|evaluation|report|announcement|et al\.|colleagues)\b"
          r".{0,120}\b(found|finds|showed|shows|reported|reports|measured|went from|rose|fell|improved|reached|achieved)\b")
CITE = r"\[(\d+)\]\(appendix-references\.md#([^)]+)\)"
FOOT = r"\[\^([^\]]+)\](?!:)"
W = r"(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion)"


def clean(t):
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    return t


def body_and_notes(t):
    t = clean(t)
    notes = dict(re.findall(r"(?m)^\[\^([^\]]+)\]:\s*(.*)$", t))
    body = re.sub(r"(?m)^\[\^[^\]]+\]:.*$", "", t)
    return body, notes


def paragraphs(body):
    """Yield (heading_index, paragraph_text). Headings, tables and images are skipped."""
    h = 0
    for block in re.split(r"\n\s*\n", body):
        lines = [l.strip() for l in block.splitlines() if l.strip()]
        if not lines:
            continue
        if lines[0].startswith("#"):
            h += 1
            lines = [l for l in lines if not l.startswith("#")]
        lines = [l for l in lines if not l.startswith(("|", "!"))]
        if lines:
            yield h, " ".join(lines)


def sentences(par):
    # A sentence can end with a citation link: "trust.[1](appendix-references.md#x) Next".
    return [s.strip() for s in re.split(r"(?<=[.!?”)])\s+(?=[A-Z“*(])", par) if s.strip()]


def years_in(s):
    return [int(y) for y in re.findall(r"\b(1[5-9]\d\d|20\d\d)\b", s)]


def classify(s, since, ctx_year, recent, src_year=None):
    text = re.sub(CITE, "", re.sub(FOOT, "", s))
    years = years_in(text)
    kind = []
    fresh = any(y >= since for y in years)
    undated_date = re.search(r"\b(\d{1,2} " + MONTHS + r"|" + MONTHS + r" \d{1,2}\b|(?:in|on|by|since|until|during|from|last|this|early|late|mid-|’s|'s) ?" + MONTHS + r")\b", text)
    if not fresh and not years and undated_date and ctx_year and ctx_year >= since:
        kind.append(f"fresh(date,{ctx_year}?)")
    elif fresh:
        kind.append("fresh")
    if not kind and recent.search(text):
        kind.append("fresh(term)")
    # Names with numbers in them (System 3, Opus 4.6, Layer 0, Reviewer 2) and list markers are not quantities.
    numtext = re.sub(r"\b[A-Z][\w-]* \d[\d.]*\b|(?:^|\s)\d{1,2}\.(?=\s|$)", " ", text)
    if re.search(NUM, numtext, re.I): kind.append("number")
    org = re.search(ORGS, text)
    if org:
        kind.append(("org-report:" if re.search(REPORT, text) else "org:") + org.group(1))
    if not org and re.search(RESULT, text, re.I): kind.append("reported-result")
    if re.search(SUPER, text): kind.append("superlative")
    if re.search(STATUS, text, re.I): kind.append("status")
    if years and not fresh: kind.append("history")
    hedged = bool(re.search(HEDGES, text, re.I))
    refs = re.findall(FOOT, s) + [a for _, a in re.findall(CITE, s)]
    return kind, hedged, refs, text


def numbered_cites(t):
    return re.findall(CITE, t)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dir"); ap.add_argument("--order")
    ap.add_argument("--since", type=int, default=2025)
    ap.add_argument("--only", choices=["fresh", "risky", "number", "unsourced"])
    ap.add_argument("--skip", default="13-the-prophecy.md",
                    help="comma-separated files to leave out (default: the protected fiction chapter); pass '' to include everything")
    ap.add_argument("--recent", help="extra comma-separated terms that make a sentence fresh, e.g. 'Navier,ExploitGym'")
    ap.add_argument("--source-dates", action="store_true",
                    help="also mark a claim fresh when its paragraph cites a source dated >= --since")
    ap.add_argument("--numbers", nargs="?", const="agents,hours,days,theorems,tokens,percent",
                    help="comma-separated units (default: agents,hours,days,theorems,tokens,percent)")
    ap.add_argument("--files", help="comma-separated chapter files to limit any mode to")
    ap.add_argument("--entries", action="store_true",
                    help="list the appendix entries cited by the selected files, with what to check in each")
    ap.add_argument("--near", help="with --numbers: only compare numbers in paragraphs naming one of these events, grouped by event, e.g. 'Navier,Fermat,Riemann'")
    ap.add_argument("--notes", action="store_true")
    a = ap.parse_args()
    d = Path(a.dir)
    recent = RECENT + ("|\\b(" + "|".join(re.escape(x.strip()) for x in a.recent.split(",")) + ")\\b" if a.recent else "")
    recent = re.compile(recent)
    names = json.load(open(a.order)) if a.order else sorted(p.name for p in d.glob("*.md"))
    skip = {x.strip() for x in a.skip.split(",") if x.strip()}
    only = {x.strip() for x in a.files.split(",")} if a.files else None
    if only:
        missing = only - {p.name for p in d.glob("*.md")}
        if missing: sys.exit(f"not found in {d}: {', '.join(sorted(missing))}")
        if not a.order: names = sorted(only)
    files = [(n, (d / n).read_text(encoding="utf-8")) for n in names
             if (d / n).exists() and not n.startswith("appendix-references") and n not in skip
             and (only is None or n in only)]
    refs_path = d / "appendix-references.md"

    if a.entries:
        if not refs_path.exists(): sys.exit(f"no appendix-references.md in {d}")
        entry = {anc: (int(num), body) for num, anc, body in
                 re.findall(r'(?m)^(\d+)\.\s*<a id="([^"]+)"></a>(.*)$', refs_path.read_text(encoding="utf-8"))}
        for n, t in files:
            cites = list(dict.fromkeys(anc for _, anc in numbered_cites(t)))
            if not cites: continue
            print(f"\n== {n}: {len(cites)} cited entries")
            for anc in cites:
                if anc not in entry:
                    print(f"  MISSING #{anc}"); continue
                num, body = entry[anc]
                flags = []
                if not years_in(body): flags.append("NO DATE")
                if not re.search(r"https?://|doi\.org|arXiv", body): flags.append("NO LINK (fine for a book; not for a web post)")
                if re.search(r"\*[^*]+\*\s*\d+", body) and not re.search(r"\d+\s*[–-]\s*\d+|pp?\.|article|e\d+", body):
                    flags.append("JOURNAL WITHOUT PAGES")
                if re.search(r"\b\d{1,2} " + MONTHS + r" 20\d\d|" + MONTHS + r" \d{1,2}, 20\d\d", body):
                    flags.append("EXACT DATE: confirm against the page")
                print(f"  [{num}] #{anc}  {'; '.join(flags)}\n      {body.strip()[:300]}")
        print("\nFor each entry check: authors, title wording, venue, volume and pages, the date on the page itself, "
              "and that the URL or DOI resolves to this work (not a newer version or a landing page).")
        return

    if a.notes:
        defined = defaultdict(list); used = defaultdict(list)
        for n, t in files:
            body, notes = body_and_notes(t)
            for k in notes: defined[k].append(n)
            for k in set(re.findall(FOOT, body)): used[k].append(n)
        for k, fs in defined.items():
            if len(fs) > 1: print(f"DUPLICATE KEY  [^{k}] defined in {', '.join(fs)} (a joined build prints the first definition everywhere)")
        for k, fs in used.items():
            if k not in defined: print(f"UNDEFINED      [^{k}] used in {', '.join(fs)}")
        for k, fs in defined.items():
            if k not in used: print(f"UNUSED         [^{k}] defined in {', '.join(fs)}")
        if refs_path.exists():
            ref_text = refs_path.read_text(encoding="utf-8")
            ordinal = {anc: int(num) for num, anc in re.findall(r'(?m)^(\d+)\.\s*<a id="([^"]+)"', ref_text)}
            anchors = set(re.findall(r'<a id="([^"]+)"', ref_text))
            for anc, c in sorted(Counter(re.findall(r'<a id="([^"]+)"', ref_text)).items()):
                if c > 1: print(f"DUPLICATE ANCHOR #{anc} in appendix-references.md")
            # Title quotes: the house style is the majority of “…” vs ‘…’ at the start of a title.
            styles = {anc: ("single" if re.search(r"(?:^|[,.] )‘[^’]{3,}[,.]?’", body) and "“" not in body else "double")
                      for anc, body in re.findall(r'(?m)^\d+\.\s*<a id="([^"]+)"></a>(.*)$', ref_text)}
            house = Counter(styles.values()).most_common(1)[0][0] if styles else None
            for anc, st in styles.items():
                if st != house: print(f"QUOTE STYLE    #{anc} uses {st} quotes for titles; most entries use {house}")
            cited = defaultdict(list)
            for n, t in files:
                seq = []
                for num, anc in numbered_cites(t):
                    cited[anc].append((n, int(num)))
                    if anc in ordinal and ordinal[anc] != int(num):
                        print(f"WRONG NUMBER   {n}: [{num}] links #{anc}, which is entry {ordinal[anc]} in the appendix")
                    if int(num) not in seq: seq.append(int(num))
                if seq and seq != list(range(1, len(seq) + 1)):
                    print(f"OUT OF ORDER   {n}: citation numbers appear as {seq[:12]}{'…' if len(seq) > 12 else ''}")
                own = n.split("-")[0]  # 04-system-3.md -> 04, interlude-....md -> interlude
                for anc in sorted({anc for _, anc in numbered_cites(t) if not anc.startswith(f"ref-{own}-")}):
                    print(f"OTHER CHAPTER  {n}: cites #{anc}, which belongs to another chapter's list")
            for anc, uses in cited.items():
                if anc not in anchors:
                    print(f"MISSING ANCHOR #{anc} cited in {', '.join(sorted({u[0] for u in uses}))}")
                if len({u[1] for u in uses}) > 1:
                    print(f"NUMBER CLASH   #{anc} cited with numbers {sorted({u[1] for u in uses})}")
                if len({u[0] for u in uses}) > 1:
                    print(f"CROSS-CHAPTER  #{anc} cited from {sorted({u[0] for u in uses})} (numbering restarts per chapter)")
            for anc in sorted(set(ordinal) - set(cited)):
                print(f"UNCITED ENTRY  #{anc} is numbered {ordinal[anc]} but never cited")
        for n, t in files + ([("appendix-references.md", refs_path.read_text(encoding="utf-8"))] if refs_path.exists() else []):
            for m in re.finditer(r"(?:checked|accessed|retrieved|status[^.]{0,40}) on [^.\]]*\d{4}|at the time of writing|as I write", t):
                print(f"DATED CHECK    {n}: {m.group(0)}  (re-check before print)")
        return

    if a.numbers:
        units = [u.strip() for u in a.numbers.split(",")]
        events = [e.strip() for e in a.near.split(",")] if a.near else [""]
        seen = defaultdict(list)
        # Number, then at most three words (not numbers, not "in"/"and"), then the unit; model versions like "Opus 4.6" are skipped.
        pat = (r"(?<![\d.])(?<!Opus )(?<!Sonnet )(?<!Haiku )(?<!GPT-)(\d[\d,\.]*(?:\s(?:thousand|million|billion))?|\b" + W + r"(?:[\s-]" + W + r")*)"
               r"\s+((?:(?!in\b|and\b|to\b|\d|" + "|".join(map(re.escape, units)) + r")[A-Za-z][\w.\-]*\s+){0,3})")
        for n, t in files:
            body, _ = body_and_notes(t)
            for _, par in paragraphs(body):
                hits = [e for e in events if e in par]
                if not hits: continue
                for s in sentences(par):
                    s = re.sub(CITE, "", s)
                    for u in units:
                        for m in re.finditer(pat + re.escape(u) + r"\b", s, re.I):
                            for e in hits:
                                seen[(e, u)].append((m.group(1).strip().lower(), m.group(2).strip(), n, s[:160]))
        for (e, u), rows in seen.items():
            vals = {v for v, _, _, _ in rows}
            quals = {q for _, q, _, _ in rows}
            if len(vals) > 1 or (e and len(quals) > 1):
                print(f"\n== {e + ': ' if e else ''}'{u}': {len(vals)} numbers, qualifiers {sorted(quals)}")
                for v, q, n, s in rows: print(f"   {v:>12} {q:<14} {n}: {s}")
        return

    # Year of each numbered reference entry (the latest year it mentions), for --source-dates.
    source_year = {}
    if (d / "appendix-references.md").exists():
        for anc, line in re.findall(r'(?m)^\d+\.\s*<a id="([^"]+)"></a>(.*)$', (d / "appendix-references.md").read_text(encoding="utf-8")):
            source_year[anc] = max(years_in(line), default=0)
    for n, t in files:
        _, notes = body_and_notes(t)
        for k, v in notes.items():
            source_year[k] = max(years_in(v), default=0)

    print("file\tkind\thedged\tsource\tsentence")
    for n, t in files:
        body, notes = body_and_notes(t)
        ctx_year, last_h = None, None
        for h, par in paragraphs(body):
            if h != last_h:
                ctx_year, last_h = None, h  # a new section resets the date context
            par_refs = re.findall(FOOT, par) + [x for _, x in re.findall(CITE, par)]
            src_year = max((source_year.get(r, 0) for r in par_refs), default=0) if a.source_dates else 0
            sents = sentences(par)
            # Where each sentence's nearest following citation is.
            nxt = []
            for i, s in enumerate(sents):
                later = [r for t2 in sents[i:] for r in re.findall(FOOT, t2) + [x for _, x in re.findall(CITE, t2)]]
                nxt.append(later[0] if later else None)
            claim_by_cite = Counter()
            rows = []
            for i, s in enumerate(sents):
                kind, hedged, refs, text = classify(s, a.since, ctx_year, recent)
                # A count or result in a paragraph that follows a recent date in the same section.
                if ctx_year and ctx_year >= a.since and not any(k.startswith("fresh") for k in kind) and \
                        any(k == "number" or k.startswith(("org-report", "reported-result")) for k in kind):
                    kind.insert(0, f"fresh(context,{ctx_year}?)")
                if src_year >= a.since and not any(k.startswith("fresh") for k in kind) and \
                        any(k == "number" or k.startswith(("org", "reported-result", "superlative", "status")) for k in kind):
                    kind.insert(0, f"fresh(source,{src_year})")
                ys = years_in(text)
                if ys: ctx_year = max(ys)
                if not kind: continue
                fresh = any(k.startswith("fresh") for k in kind)
                risky = fresh or any(k.startswith(("org-report", "reported-result", "superlative", "status")) for k in kind)
                src = ",".join(refs) or (f"next:{nxt[i]}" if nxt[i] else ("before:" + ",".join(par_refs) if par_refs else ""))
                claimish = fresh or "number" in kind or any(k.startswith(("org-report", "reported-result")) for k in kind)
                if claimish and nxt[i]: claim_by_cite[nxt[i]] += 1
                rows.append((kind, hedged, refs, text, fresh, risky, src, nxt[i], claimish))
            for kind, hedged, refs, text, fresh, risky, src, cite, claimish in rows:
                if claimish and cite and claim_by_cite[cite] > 1:
                    kind = kind + [f"shared-cite({claim_by_cite[cite]})"]
                if a.only == "fresh" and not fresh: continue
                if a.only == "risky" and not risky: continue
                if a.only == "number" and "number" not in kind: continue
                # Unsourced: a figure or fresh claim with no citation after it in its paragraph.
                if a.only == "unsourced" and (src and not src.startswith("before:") or not claimish): continue
                print(f"{n}\t{','.join(kind)}\t{'yes' if hedged else ''}\t{src}\t{text[:220]}")


if __name__ == "__main__":
    main()

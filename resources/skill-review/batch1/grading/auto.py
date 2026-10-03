#!/usr/bin/env python3
"""Programmatic checks for the author-skill evals. Usage: auto.py <iteration-dir> [config ...]
Writes auto.json into each run dir: [{text, passed, evidence}]."""
import json, re, sys, subprocess
from pathlib import Path

REPO = Path('/home/user/System3')
HERE = Path(__file__).parent
CH = REPO / 'chapters'


def sentences(t):
    return [s.strip() for s in re.split(r'(?<=[.!?…])\s+', t) if len(s.strip()) > 25]


def norm(s):
    return re.sub(r'\s+', ' ', s.replace('’', "'").replace('“', '"').replace('”', '"')).strip()


def words(t):
    return len(re.findall(r"\w+", t))


def restored_kept(out_text, chapter):
    lines = (HERE / f'restored-{chapter}.txt').read_text().splitlines()
    sents = [norm(s) for l in lines for s in sentences(l)]
    o = norm(out_text)
    kept = [s for s in sents if s in o]
    miss = [s for s in sents if s not in o]
    return len(kept), len(sents), miss


def headings(t):
    return [l.strip() for l in t.splitlines() if l.startswith('#')]


def notes(t):
    return sorted(set(re.findall(r'\[\^[^\]]+\]', t)))


XY = re.compile(r"\b(?:not|isn['’]t|aren['’]t|wasn['’]t|weren['’]t)\b[^.;:!?]{1,80}?[,;—–-]\s*(?:but|it['’]s|it is|they['’]re|they are)\b"
                r"|\bis not [^.]{1,60}\. (?:It|They|That) (?:is|are|was)\b"
                r"|\bnot (?:because|just|only|merely)\b[^.]{1,80}\bbut\b", re.I)


def xy(t):
    return len(XY.findall(t))


def repo_clean():
    r = subprocess.run(['git', '-C', str(REPO), 'status', '--porcelain'], capture_output=True, text=True)
    return r.stdout.strip() == '', r.stdout.strip()[:200]


def A(text, ok, ev):
    return {'text': text, 'passed': bool(ok), 'evidence': ev}


def check(eval_name, out: Path):
    res = []
    clean, dirty = repo_clean()
    res.append(A('Repository left unmodified (work done on copies)', clean, dirty or 'git status clean'))
    if eval_name.startswith('dellm'):
        ch, fn = {'dellm-ch11-pass': ('11-the-store-that-builds-itself', 'ch11.md'),
                  'dellm-xy-ch8': ('08-automatic-alignment-research', 'ch08.md'),
                  'dellm-ch12-heldout': ('12-after-capacity', 'ch12.md')}[eval_name]
        orig = (CH / f'{ch}.md').read_text()
        f = out / fn
        if not f.exists():
            return res + [A(f'{fn} saved in outputs', False, 'missing')]
        t = f.read_text()
        res.append(A(f'{fn} saved in outputs', True, str(f.name)))
        wo, wn = words(orig), words(t)
        delta = (wo - wn) / wo
        if 'xy' not in eval_name:
            res.append(A('Chapter is 3-15% shorter (a real pass, not a no-op or a rewrite)', 0.03 <= delta <= 0.15, f'{wo} -> {wn} words ({delta:.1%})'))
        else:
            res.append(A('X/Y pass is surgical: length change under 5%', abs(delta) < 0.05, f'{wo} -> {wn} words ({delta:.1%})'))
        k, n, miss = restored_kept(t, ch)
        res.append(A('At least 90% of sentences the author restored on 2 Oct are kept verbatim', n and k / n >= 0.9, f'{k}/{n} kept; changed: ' + ' | '.join(m[:70] for m in miss[:4])))
        ho, hn = headings(orig), headings(t)
        res.append(A('All headings preserved', [norm(h) for h in ho] == [norm(h) for h in hn], f'{len(ho)} orig, {len(hn)} out; missing: {[h for h in ho if h not in hn][:3]}'))
        no, nn = notes(orig), notes(t)
        res.append(A('All footnote markers preserved', no == nn, f'{len(no)} -> {len(nn)}; missing {sorted(set(no)-set(nn))[:5]}'))
    elif eval_name.startswith('fc-'):
        f = out / 'fact-check.md'
        res.append(A('fact-check.md saved in outputs', f.exists(), 'present' if f.exists() else f'missing; files: {[p.name for p in out.iterdir()]}'))
        t = f.read_text() if f.exists() else ''
        rows = [l for l in t.splitlines() if l.startswith('|') and not re.match(r'\|\s*-', l)]
        res.append(A('Ledger has at least 15 claim rows', len(rows) >= 16, f'{len(rows)} table rows'))
        res.append(A('Reports which sources could not be opened directly', re.search(r'block|could not (?:open|access|reach)|not accessible|unreachable|secondary', t, re.I), 'mentions access limits' if re.search(r'block|secondary', t, re.I) else 'no mention'))
    elif eval_name.startswith('lt-'):
        fn = {'lt-alberto-blog': 'alberto-ar.md', 'lt-preface-msa': 'preface-ar.md', 'lt-ch9-linkedin-heldout': 'ch9-ar.md'}[eval_name]
        f = out / fn
        res.append(A(f'{fn} saved in outputs', f.exists(), 'present' if f.exists() else 'missing'))
        if f.exists():
            t = f.read_text()
            if 'alberto' in eval_name:
                src = (CH / '04-system-3.md').read_text().split('## Call Alberto')[1].split('\n## ')[0]
            elif 'ch9' in eval_name:
                src = (CH / '09-layer-4-desire.md').read_text().split('## Nobody Wanted AWS')[0]
            else:
                src = (CH / '00-preface.md').read_text()
            ps = len([p for p in src.split('\n\n') if p.strip()])
            pt = len([p for p in t.split('\n\n') if re.search(r'[؀-ۿ]', p)])
            res.append(A('Every source paragraph translated (Arabic paragraphs >= 85% of source paragraphs)', pt >= 0.85 * ps, f'{pt} Arabic paras vs {ps} source'))
            body = re.split(r'\n---+\n|\n#+ *(?:ملاحظة|Translat|Note)', t)[0]
            body = re.sub(r'<!--.*?-->|https?://\S+|\(appendix[^)]*\)', '', body, flags=re.S)
            ar = len(re.findall(r'[\u0600-\u06FF]+', body)); la = len(re.findall(r'[A-Za-z]+', body))
            res.append(A('Translation body is Arabic (English words under 5% of words, note excluded)', la / max(ar + la, 1) < 0.05, f'{la} English / {ar} Arabic words in body'))
    elif eval_name.startswith('devedit'):
        fn = {'devedit-arc-review': 'arc-proposal.md', 'devedit-ch10-plan': 'ch10-plan.md', 'devedit-ch1-heldout': 'ch1-plan.md'}[eval_name]
        f = out / fn
        res.append(A(f'{fn} saved in outputs', f.exists(), 'present' if f.exists() else 'missing'))
    return res


if __name__ == '__main__':
    it = Path(sys.argv[1])
    for ed in sorted(it.glob('eval-*')):
        name = re.sub(r'^eval-\d+-', '', ed.name)
        for cfg in ed.iterdir():
            if not cfg.is_dir():
                continue
            out = cfg / 'run-1' / 'outputs'
            if not out.exists():
                continue
            r = check(name, out)
            (cfg / 'run-1' / 'auto.json').write_text(json.dumps(r, indent=1, ensure_ascii=False))
            print(ed.name, cfg.name, f"{sum(x['passed'] for x in r)}/{len(r)}")
            for x in r:
                if not x['passed']:
                    print('   FAIL', x['text'], '::', x['evidence'][:150])

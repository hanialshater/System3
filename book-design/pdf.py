#!/usr/bin/env python3
"""Explicit, incremental PDF builds from the current repository manuscript.

  .venv-pdf/bin/python book-design/pdf.py status
  .venv-pdf/bin/python book-design/pdf.py build --preview
"""
import argparse
from contextlib import contextmanager
import fcntl
import hashlib
from importlib.metadata import PackageNotFoundError, version
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
CURATED = ROOT/'book-design/curated'
OUTPUT = ROOT/'output/pdf'
PDF_NAME = 'System3_Curated_6x9.pdf'
PACKAGES = ('PyMuPDF','reportlab','markdown-it-py','Pillow')
sys.path.insert(0,str(CURATED))


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream,'sha256').hexdigest()


def snapshot(root=ROOT):
    paths = list((root/'chapters').glob('*.md'))
    paths += [root/'book-design/pdf.py',root/'book-design/requirements-pdf.txt']
    paths += [p for p in (root/'book-design/curated').rglob('*') if p.is_file()
              and '__pycache__' not in p.parts and 'tests' not in p.parts
              and p.suffix.lower() in ('.py','.json','.png','.jpg','.ttf','.pfb','.afm')]
    files = {str(p.relative_to(root)):digest(p) for p in sorted(paths)}
    runtime = {name:version(name) for name in PACKAGES}
    runtime['python'] = '.'.join(map(str,sys.version_info[:2]))
    inputs = dict(files=files,runtime=runtime)
    return dict(fingerprint=hashlib.sha256(json.dumps(inputs,sort_keys=True).encode()).hexdigest(),**inputs)


def fresh(state, inputs, pdf):
    return (state.get('fingerprint') == inputs['fingerprint'] and pdf.is_file()
            and state.get('pdf_sha256') == digest(pdf)
            and (pdf.parent/'build-report.json').is_file()
            and state.get('report_sha256') == digest(pdf.parent/'build-report.json'))


def read_state(directory):
    try:
        return json.loads((directory/'build-state.json').read_text())
    except (FileNotFoundError, ValueError):
        return {}


def atomic_json(path, value):
    temp=path.with_suffix('.json.tmp')
    temp.write_text(json.dumps(value,indent=2)+'\n')
    os.replace(temp,path)


@contextmanager
def build_lock():
    directory=ROOT/'tmp/pdfs'
    directory.mkdir(parents=True,exist_ok=True)
    with (directory/'build.lock').open('w') as lock:
        try:
            fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError('Another PDF build is running.')
        yield


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['build','status'],nargs='?',default='build')
    parser.add_argument('--force',action='store_true',help='Rebuild even if the inputs match.')
    parser.add_argument('--preview',action='store_true',help='Render contact sheets and section samples for visual review.')
    parser.add_argument('--strict-art',action='store_true',help='Fail if an existing artwork anchor or illustrated cover needs review.')
    args=parser.parse_args()
    if not (CURATED/'art.json').exists() or not (CURATED/'assets/fonts').exists():
        parser.error('Curated assets are missing. See book-design/PDF.md for the one-time import.')
    try:
        inputs=snapshot()
    except PackageNotFoundError as error:
        parser.error(f'{error}. Install book-design/requirements-pdf.txt into .venv-pdf first.')
    state=read_state(OUTPUT);pdf=OUTPUT/PDF_NAME
    current=fresh(state,inputs,pdf)
    if args.command=='status':
        print('Current: no rebuild needed.' if current else 'Out of date: run the build command when you want a new PDF.')
        if state:
            changed=sorted(k for k in set(inputs['files'])|set(state.get('files',{})) if inputs['files'].get(k)!=state.get('files',{}).get(k))
            if changed:print('Changed inputs:\n'+'\n'.join(changed))
        return
    with build_lock():
        # Recheck under the lock, in case a preceding build finished meanwhile.
        state=read_state(OUTPUT)
        if fresh(state,inputs,pdf) and not args.force:
            if args.strict_art and state.get('art_review_count',0):
                raise RuntimeError('Current proof has artwork needing review; see build-report.json.')
            print(f'Unchanged; keeping {pdf}')
            if args.preview:
                from verify import previews
                previews(pdf,OUTPUT/'previews')
            return
        work=Path(tempfile.mkdtemp(prefix='build-',dir=ROOT/'tmp/pdfs'))
        candidate=work/PDF_NAME
        subprocess.run([sys.executable,str(CURATED/'render.py'),'--work-dir',str(work),'--output',str(candidate)],check=True)
        from verify import verify,previews
        validation=verify(candidate,work)
        if not validation['passed']:
            raise RuntimeError(f'PDF verification failed; previous published proof retained. Inspect {work}/verification.json')
        summary=json.loads((work/'build-summary.json').read_text())
        art_review_count=len(summary['pending_art'])+len(summary['cover_warnings'])
        if args.strict_art and art_review_count:
            raise RuntimeError(f'{art_review_count} artwork issues need review. See {work}/build-summary.json. Previous published proof retained.')
        if snapshot()['fingerprint'] != inputs['fingerprint']:
            raise RuntimeError('Inputs changed during the build. Previous proof retained; rebuild when edits are ready.')
        if args.preview:previews(candidate,work/'previews')
        OUTPUT.mkdir(parents=True,exist_ok=True)
        new_state=dict(**inputs,pdf_sha256=digest(candidate),art_review_count=art_review_count,
                       built_at=datetime.now(timezone.utc).isoformat())
        report=dict(**summary,verification=validation,fingerprint=inputs['fingerprint'],
                    built_at=new_state['built_at'],visual_review='Contact sheets and representative pages require human review before distribution.')
        # State is written last. A crash between replacements is detected by the PDF hash.
        os.replace(candidate,pdf)
        atomic_json(OUTPUT/'build-report.json',report)
        new_state['report_sha256']=digest(OUTPUT/'build-report.json')
        if args.preview:
            import shutil
            preview_dest=OUTPUT/'previews'
            if preview_dest.exists():shutil.rmtree(preview_dest)
            shutil.move(str(work/'previews'),str(preview_dest))
        atomic_json(OUTPUT/'build-state.json',new_state)
        print(f'Built {summary["pages"]} pages: {pdf}')
        print(f'Verified {validation["text_blocks"]} text blocks; {summary["original_art_regions"]} interior illustrations.')
        pending=sum(n['reason']=='pending visual design' for n in summary['production_notes'])
        print(f'Art review: {art_review_count} existing placements/covers; {pending} manuscript design directions. Details: {OUTPUT}/build-report.json')


if __name__=='__main__':
    try:
        main()
    except (RuntimeError,subprocess.CalledProcessError) as error:
        print(str(error),file=sys.stderr)
        sys.exit(1)

"""One-time import of the user's curated assets. Never executes archive scripts.

The 190 MB placement PDF is only needed during import, not during book builds.
Archive paths are read explicitly; extractall is deliberately avoided.
"""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

import fitz
from pdf_clipping import place_art

ROOT = Path(__file__).resolve().parent
PREFIX = 'System3_6x9_Curated/'


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path)
    parser.add_argument('reference_pdf', type=Path)
    args = parser.parse_args()
    target = ROOT / 'assets'
    if target.exists():
        parser.error('Assets already exist; move them aside explicitly before re-importing.')
    (target / 'art').mkdir(parents=True)
    (target / 'fonts').mkdir()
    with zipfile.ZipFile(args.archive) as archive:
        def read(name):
            return archive.read(PREFIX + name)
        def data(name):
            return json.loads(read('design/' + name + '.json'))
        for name in archive.namelist():
            if name.startswith(PREFIX + 'fonts/') and not name.endswith('/'):
                (target / 'fonts' / Path(name).name).write_bytes(archive.read(name))
            if name.startswith(PREFIX + 'art/cover-') and name.endswith('.png'):
                (target / 'art' / Path(name).name).write_bytes(archive.read(name))
        selection = data('curation')['selected_ids']
        rows = [a for a in data('art-map') if a['id'] in selection]
        rows.append(dict(id='photo58', source_page=58, clip=[.19,.31,.866,.651]))
        bindings = {b['art']: b for b in data('text-art-bindings')}
        revisions = data('revisions')
        source = fitz.open(stream=read('source/Placement_Source.pdf'), filetype='pdf')
        chapters = data('curation')['chapter_source_pages']
        for a in rows:
            if a['id'] == 'a153':
                # The old crop included a rule and a sliver of a source footnote.
                a['clip'][3] = .888
            c = a['clip']
            ratio = (c[2] - c[0])*612 / ((c[3] - c[1])*792)
            width = min(432, 350*ratio)
            layer = fitz.open()
            page = layer.new_page(width=width, height=width/ratio)
            page.draw_rect(page.rect, color=None, fill=(252/255,246/255,231/255))
            if a['id'] in revisions:
                page.insert_image(page.rect, stream=read(revisions[a['id']]))
            else:
                place_art(layer, page, source, dict(a, paper=None), page.rect)
            output = target / 'art' / (a['id'] + '.jpg')
            page.get_pixmap(matrix=fitz.Matrix(300/72,300/72), alpha=False).pil_save(output,format='JPEG',quality=95,subsampling=0,optimize=True)
            layer.close()
            a['file'] = str(output.relative_to(ROOT))
            a['chapter'] = next((int(ch) for ch, pages in chapters.items() if a['source_page'] in pages), 4)
            a['after'] = bindings.get(a['id'], {}).get('after')
        source.close()
        (ROOT / 'art.json').write_text(json.dumps(rows, indent=2) + '\n')
        (ROOT / 'layout.json').write_text(json.dumps(data('immersion'), indent=2) + '\n')
        # Chapter 4's special illustrated exercise is already composed in the proof.
        reference = fitz.open(args.reference_pdf)
        cover_page = next(b['page'] for b in data('build-summary')['bookmarks'] if b['title'].startswith('4. '))
        reference[cover_page-1].get_pixmap(matrix=fitz.Matrix(300/72,300/72), alpha=False).save(target/'art/cover-058.png')
        reference.close()
        titles = {}
        for name in archive.namelist():
            if name.startswith(PREFIX+'manuscript/') and name.endswith('.md'):
                titles[Path(name).name] = next((line[2:].strip() for line in archive.read(name).decode().splitlines() if line.startswith('# ')), None)
        provenance = dict(
            archive=args.archive.name, archive_sha256=digest(args.archive),
            reference_pdf=args.reference_pdf.name, reference_sha256=digest(args.reference_pdf),
            imported_art=len(rows), covers=14, source_titles=titles,
            notes='Cropped curated art and embedded fonts only. Manuscript is read from repository chapters/. Cover 058 is rendered from the supplied proof. Other covers are original PNG masters. Original source-page numbers are provenance, never new output page numbers.',
        )
        (ROOT / 'provenance.json').write_text(json.dumps(provenance, indent=2)+'\n')
    print(f'Imported {len(rows)} interior assets, 14 covers and fonts into {target}')


if __name__ == '__main__':
    main()

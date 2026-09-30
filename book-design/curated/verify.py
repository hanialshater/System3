"""Fail the build on lost manuscript text, off-page text or art/text collisions."""
import json
from pathlib import Path
import re
import unicodedata

import fitz
from markdown_it import MarkdownIt
from print_quality import audit as audit_print_quality

MD = MarkdownIt('commonmark').enable('table')


def compact(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text).lower() if c.isalnum())


def plain(text):
    out = []
    for token in MD.parse(text):
        if token.type == 'inline':
            out.extend(c.content for c in token.children if c.type in ('text','code_inline','softbreak','hardbreak'))
    return ' '.join(out)


def citation_fragments(value):
    # Superscript labels are excluded from PDF body spans; check the prose around them.
    return re.split(r'\[\^[^]]+\]|\[\d+\]\(appendix-references\.md#ref-[A-Za-z0-9_-]+\)', value)


def verify(pdf, work):
    expected = json.loads((work/'expected.json').read_text())
    placements = json.loads((work/'placements.json').read_text())
    covers = json.loads((work/'cover-placements.json').read_text())
    cover_pages = {c['page'] for c in covers}
    document = fitz.open(pdf)
    texts, outside, collisions, fonts, blank_pages = [], [], [], set(), []
    for n, page in enumerate(document, 1):
        for block in page.get_text('dict',flags=fitz.TEXTFLAGS_DICT & ~fitz.TEXT_PRESERVE_IMAGES)['blocks']:
            for line in block.get('lines', []):
                for span in line['spans']:
                    rect = fitz.Rect(span['bbox'])
                    if not span['flags'] & 1 and rect.y0 >= 40 and rect.y1 <= 607:
                        texts.append(span['text'])
                    if not page.rect.contains(rect):
                        outside.append(dict(page=n, text=span['text'], bbox=span['bbox']))
        for font in page.get_fonts():
            fonts.add(font[0])
        if not any(40 <= w[1] and w[3] <= 607 for w in page.get_text('words')) and not page.get_images():
            blank_pages.append(n)
        if n in cover_pages:
            continue
        art = [fitz.Rect(a['rect']) for a in placements if a['page'] == n]
        for word in page.get_text('words'):
            box = fitz.Rect(word[:4])
            if box.y0 < 40 or box.y1 > 607:
                continue
            for rect in art:
                # Tiny boundary tolerances accommodate glyph bounding-box rounding.
                inner = fitz.Rect(rect.x0+1,rect.y0+1,rect.x1-1,rect.y1-1)
                if box.intersects(inner):
                    collisions.append(dict(page=n,text=word[4],art_rect=list(rect)))
    actual = compact(' '.join(texts))
    missing = []
    for i, row in enumerate(expected):
        # Repeated table headers across page breaks interrupt the concatenated
        # table text. Verify each complete source cell independently.
        fragments = [part for value in row.get('cells',[row['raw']]) for part in citation_fragments(value)]
        wants = [compact(f if row['kind']=='code' else plain(f)) for f in fragments]
        if any(w and w not in actual for w in wants):
            missing.append(dict(index=i,chapter=row['chapter'],kind=row['kind'],text=row['raw']))
    unembedded = []
    for xref in fonts:
        name, ext, kind, content = document.extract_font(xref)
        # ReportLab creates an unused Helvetica resource; only live spans matter.
        if not content and any(name.replace('-','') == s['font'].replace('-','')
            for p in document for b in p.get_text('dict',flags=fitz.TEXTFLAGS_DICT & ~fitz.TEXT_PRESERVE_IMAGES)['blocks']
            for l in b.get('lines',[]) for s in l['spans']):
            unembedded.append(name)
    print_quality = audit_print_quality(document, placements, covers)
    report = dict(
        pages=len(document), all_pages_6x9=all(p.rect==fitz.Rect(0,0,432,648) for p in document),
        repaired=document.is_repaired, bookmarks=len(document.get_toc()),
        links=sum(len(p.get_links()) for p in document), text_blocks=len(expected),
        unmatched_blocks=missing, off_page_spans=outside, art_text_collisions=collisions,
        unembedded_live_fonts=unembedded, blank_pages=blank_pages,
        print_quality=print_quality,
    )
    document.close()
    report['passed'] = (report['all_pages_6x9'] and not report['repaired']
        and not any([missing,outside,collisions,unembedded,blank_pages]) and report['bookmarks'] >= 19
        and print_quality['passed'])
    (work/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    return report


def previews(pdf, directory):
    """Contact sheets for all pages plus readable samples; never used as book pages."""
    from PIL import Image, ImageDraw
    directory.mkdir(parents=True,exist_ok=True)
    document = fitz.open(pdf)
    for offset in range(0,len(document),24):
        sheet = Image.new('RGB',(864,1452),'#ddd9d1')
        draw = ImageDraw.Draw(sheet)
        for i, page in enumerate(document[offset:offset+24]):
            pix = page.get_pixmap(matrix=fitz.Matrix(.46,.46),alpha=False)
            im = Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
            im.thumbnail((198,216))
            x=(i%4)*216+9;y=(i//4)*242+22
            sheet.paste(im,(x,y));draw.text((x,y-17),str(offset+i+1),fill='black')
        sheet.save(directory/f'contact-{offset//24+1:02}.jpg',quality=90)
    # Every section start, plus the first body page after each illustrated cover.
    pages={1,2}
    for _,_,n in document.get_toc():
        pages.update([n,min(n+1,len(document))])
    for n in sorted(pages):
        document[n-1].get_pixmap(matrix=fitz.Matrix(1.8,1.8),alpha=False).save(directory/f'page-{n:04}.png')
    document.close()

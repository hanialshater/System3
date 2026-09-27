"""Validate a candidate PDF before replacing the last successful proof."""
import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import fitz


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
    def handle_data(self, data):
        self.parts.append(data)


def chars(s):
    # Count letters/digits, with standard typographic ligatures expanded.
    import unicodedata
    return Counter(c for c in unicodedata.normalize('NFKC', s) if c.isalnum())


pdf_path, html_path = map(Path, sys.argv[1:])
html = html_path.read_text()
data = json.loads(re.search(r'window.CHAPTER_DATA=(.*?);</script>', html, re.S)[1])
parser = Text()
for block in data['blocks']:
    if block['kind'] != 'break':
        parser.feed(block['html'])
parser.feed(data['notes'])
expected = chars(''.join(parser.parts))
doc = fitz.open(pdf_path)
body = []
outside = []
for number, page in enumerate(doc, 1):
    if abs(page.rect.width-432) > 1 or abs(page.rect.height-648) > 1:
        raise ValueError(f'Wrong trim size on page {number}: {page.rect}')
    # Cover lettering belongs to the inherited bitmap. All body text is live.
    if number == 1:
        continue
    for block in page.get_text('dict')['blocks']:
        if block['type'] != 0:
            continue
        for line in block['lines']:
            for span in line['spans']:
                x0,y0,x1,y1=span['bbox']
                if y0 > 39 and y1 < 614:
                    body.append(span['text'])
                    if x0 < 37 or x1 > 396 or y0 < 43 or y1 > 608:
                        outside.append(dict(page=number,text=span['text'],bbox=span['bbox']))
actual = chars(''.join(body))
missing = expected - actual
extra = actual - expected
# List numbering is generated in CSS and is not part of manuscript HTML text.
for digit in '0123456789':
    extra.pop(digit, None)
if missing or extra:
    raise ValueError(f'PDF character inventory differs: missing={dict(missing)}, extra={dict(extra)}')
if outside:
    raise ValueError(f'Text outside readable area: {outside[:10]}')
if not doc[1].get_text().strip():
    raise ValueError('Blank chapter opening')
links = sum(len(p.get_links()) for p in doc)
if links < data['noteCount']:
    raise ValueError('Footnote links missing')
print(json.dumps(dict(pages=len(doc),selectableText=True,manuscriptCharacterInventory='exact',
                     trim='6 × 9 in',links=links,textOutsideReadableArea=len(outside))))

"""Prepare a chapter proof without changing a byte of the manuscript."""
import base64
import html
import json
import re
import sys
from pathlib import Path

from markdown_it import MarkdownIt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE.parent / 'curated'))
from manuscript import prepare, resolve_anchor, latex_break, reference_entries, REFERENCE_LINK

md = MarkdownIt('commonmark', {'html': False, 'typographer': False})


def uri(path):
    path = Path(path)
    mime = {'.jpg': 'image/jpeg', '.png': 'image/png', '.otf': 'font/otf'}[path.suffix]
    return f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode()


def main():
    raw = (ROOT / 'chapters/05-the-society-of-agents.md').read_text()
    text, definitions, directions, old_images = prepare(raw)
    # A standalone chapter proof includes its slice of the central reference appendix.
    entries = reference_entries((ROOT / 'chapters/appendix-references.md').read_text())
    citations = REFERENCE_LINK.findall(text)
    for number, anchor in citations:
        if anchor not in entries or entries[anchor][0] != int(number):
            raise ValueError(f'Missing or misnumbered reference: {anchor}')
    definitions.extend((anchor, entries[anchor][1]) for anchor in dict.fromkeys(a for _, a in citations))
    text = REFERENCE_LINK.sub(lambda m: f'[^{m[2]}]', text)
    keys = list(dict.fromkeys(re.findall(r'\[\^([^]]+)\]', text)))
    notes = dict(definitions)
    if set(keys) != set(notes):
        raise ValueError('Footnote references and definitions differ')

    def refs(value):
        return re.sub(r'\[\^([^]]+)\]', lambda m: f'<sup><a href="#note-{keys.index(m[1])+1}" aria-label="Note {keys.index(m[1])+1}">{keys.index(m[1])+1}</a></sup>', value)

    lines = text.splitlines()
    tokens = md.parse(text)
    blocks = []
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t.level != 0 or t.type.endswith('_close'):
            i += 1
            continue
        end = i + 1
        if t.nesting == 1:
            while end < len(tokens):
                if tokens[end].level == 0 and tokens[end].nesting == -1:
                    end += 1
                    break
                end += 1
        source = '\n'.join(lines[t.map[0]:t.map[1]]) if t.map else ''
        if t.type == 'fence' and t.info == '{=latex}':
            if latex_break(t.content):
                blocks.append(dict(raw=source, html='<div class="manuscript-break" aria-hidden="true"></div>', kind='break'))
        else:
            markup = refs(md.renderer.render(tokens[i:end], md.options, {}))
            kind = 'paragraph' if t.type == 'paragraph_open' else t.type
            blocks.append(dict(raw=source, html=markup, kind=kind))
        i = end
    for i, block in enumerate(blocks):
        if block['kind'] != 'break':
            block['html'] = re.sub(r'^<(\w+)', rf'<\1 data-block="b{i}"', block['html'], count=1)
    specs = json.loads((HERE / 'chapter-05.json').read_text())
    curated = json.loads((HERE.parent / 'curated/art.json').read_text())
    art = [a for a in curated if a['chapter'] == 5]
    if {a['id'] for a in art} != set(specs['art']):
        raise ValueError('Every Chapter 5 artwork needs an explicit treatment')
    for a in art:
        a.update(specs['art'][a['id']])
        at = resolve_anchor(blocks, a['after'])
        if at is None:
            raise ValueError(f"Missing or ambiguous art anchor: {a['id']}")
        a['block'] = at
        a['uri'] = uri(HERE / a['cutout']) if a.get('cutout') else uri(HERE.parent / 'curated' / a['file'])
        # Historical source-page parity is deliberately absent from layout data.
        del a['source_page']
    note_html = '<section class="notes"><h2>References</h2><ol>'
    for index, key in enumerate(keys, 1):
        note_html += f'<li id="note-{index}" data-note="{index}">' + md.renderInline(notes[key]) + '</li>'
    note_html += '</ol></section>'
    result = dict(blocks=blocks, art=art, notes=note_html, directions=directions,
                  cover=uri(HERE.parent / 'curated/assets/art/cover-078.png'),
                  noteCount=len(keys), spec=specs)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()

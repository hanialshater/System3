"""Non-destructive PDF placement transparency for artwork on paper.

The original raster streams stay unchanged. PDF soft masks feather only the
placement boundaries; source typography remains outside the saved clip paths.
"""
import fitz


def obj(doc, text, stream=None):
    n = doc.get_new_xref()
    doc.update_object(n, text)
    if stream is not None:
        doc.update_stream(n, stream.encode())
    return n


def resource(doc, page, kind, name, ref):
    typ, val = doc.xref_get_key(page.xref, 'Resources')
    if typ == 'xref':
        target = int(val.split()[0])
    else:
        target = obj(doc, val if typ == 'dict' else '<< >>')
        doc.xref_set_key(page.xref, 'Resources', f'{target} 0 R')
    doc.xref_set_key(target, f'{kind}/{name}', f'{ref} 0 R')


def soften_placement(doc, page, first_stream, rect, fade=(16, 18, 16, 18)):
    """Apply one feathered PDF transparency group to newly placed artwork.

    Fade widths are left, top, right, bottom in points. Zero leaves an edge
    crisp where the illustration reaches the physical page boundary.
    """
    x0, ytop, x1, ybottom = rect
    y0, y1 = page.rect.height-ybottom, page.rect.height-ytop
    w, h = x1-x0, y1-y0
    left, top, right, bottom = fade
    fn = obj(doc, '<< /FunctionType 2 /Domain [0 1] /C0 [0] /C1 [1] /N 1 >>')
    mult = obj(doc, '<< /Type /ExtGState /BM /Multiply >>')
    coords = []
    if left: coords.append((x0, y0, x0+left, y0))
    if right: coords.append((x1, y0, x1-right, y0))
    if bottom: coords.append((x0, y0, x0, y0+bottom))
    if top: coords.append((x0, y1, x0, y1-top))
    shadings = []
    for c in coords:
        shadings.append(obj(doc, f'<< /ShadingType 2 /ColorSpace /DeviceGray '
                            f'/Coords [{" ".join(map(str,c))}] /Function {fn} 0 R /Extend [true true] >>'))
    stream = f'q {x0} {y0} {w} {h} re W n 1 g {x0} {y0} {w} {h} re f /M gs\n'
    stream += '\n'.join(f'/S{i} sh' for i in range(len(shadings))) + '\nQ'
    mask = obj(doc, f'<< /Type /XObject /Subtype /Form /BBox [0 0 {page.rect.width} {page.rect.height}] '
                   '/Group << /S /Transparency /CS /DeviceGray /I true >> '
                   f'/Resources << /ExtGState << /M {mult} 0 R >> /Shading << '
                   + ' '.join(f'/S{i} {n} 0 R' for i,n in enumerate(shadings)) + ' >> >> >>', stream)
    gs = obj(doc, f'<< /Type /ExtGState /BM /Darken /SMask << /S /Luminosity /G {mask} 0 R /BC [0] >> >>')
    name = f'Immersion{gs}'
    resource(doc, page, 'ExtGState', name, gs)
    streams = page.get_contents()[first_stream:]
    if streams:
        doc.update_stream(streams[0], f'q /{name} gs\n'.encode()+doc.xref_stream(streams[0]))
        doc.update_stream(streams[-1], doc.xref_stream(streams[-1])+b'\nQ')


def fitted_rect(rect, aspect):
    """Actual contained image rectangle; avoids feathering the letterbox."""
    r=fitz.Rect(rect)
    if r.width/r.height>aspect:
        w=r.height*aspect
        return fitz.Rect((r.x0+r.x1-w)/2,r.y0,(r.x0+r.x1+w)/2,r.y1)
    h=r.width/aspect
    return fitz.Rect(r.x0,(r.y0+r.y1-h)/2,r.x1,(r.y0+r.y1+h)/2)

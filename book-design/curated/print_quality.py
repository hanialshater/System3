"""Resolution checks at actual placement size; DPI tags alone never count."""
import json
from pathlib import Path

from PIL import Image


CURATED = Path(__file__).resolve().parent
MINIMUM_PPI = 300


def effective_ppi(pixels, rect):
    width, height = rect[2] - rect[0], rect[3] - rect[1]
    if width <= 0 or height <= 0:
        raise ValueError('Image placement must have positive area')
    return min(pixels[0] * 72 / width, pixels[1] * 72 / height)


def cover_path(source_page, root=CURATED):
    manifest = root / 'print-assets.json'
    entries = json.loads(manifest.read_text()).get('covers', {}) if manifest.exists() else {}
    name = f'cover-{source_page:03}.png'
    entry = entries.get(name, {})
    return root / entry.get('file', f'assets/art/{name}')


def audit(document, placements, covers, root=CURATED):
    art = {a['id']: a for a in json.loads((root / 'art.json').read_text())}
    sources = []
    for item in placements:
        path = root / art[item['id']]['file']
        with Image.open(path) as im:
            size = im.size
        sources.append(dict(asset=item['id'], file=str(path.relative_to(root)),
                            page=item['page'], pixels=list(size),
                            effective_ppi=round(effective_ppi(size, item['rect']), 2)))
    for item in covers:
        path = cover_path(item['source_page'], root)
        with Image.open(path) as im:
            size = im.size
        sources.append(dict(asset=path.stem, file=str(path.relative_to(root)),
                            page=item['page'], pixels=list(size),
                            effective_ppi=round(effective_ppi(size, [0, 0, 432, 648]), 2)))
    embedded = []
    for n, page in enumerate(document, 1):
        for im in page.get_image_info():
            embedded.append(dict(page=n, pixels=[im['width'], im['height']],
                                 effective_ppi=round(effective_ppi((im['width'], im['height']), im['bbox']), 2)))
    # Subpixel raster rounding at cropped edges can produce 299.9 PPI.
    low_sources = [x for x in sources if x['effective_ppi'] < MINIMUM_PPI - 1]
    low_embedded = [x for x in embedded if x['effective_ppi'] < MINIMUM_PPI - 1]
    return dict(minimum_ppi=MINIMUM_PPI, source_images=sources,
                embedded_images=embedded, low_resolution_sources=low_sources,
                low_resolution_embedded=low_embedded,
                passed=not low_sources and not low_embedded,
                scope='Pixel resolution at trim size, not proof of captured detail or printer-specific press compliance.')

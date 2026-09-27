"""Manuscript-only transformations; never modify the source files."""
import re
import json


def ordered_paths(directory, manifest):
    names = json.loads(manifest.read_text())
    if len(names) != len(set(names)):
        raise ValueError('Duplicate manuscript in book order')
    paths = [directory / name for name in names]
    missing = [p.name for p in paths if not p.is_file()]
    unknown = set(directory.glob('*.md')) - set(paths)
    if missing or unknown:
        raise ValueError(f'Update book order: missing={missing}, unlisted={sorted(p.name for p in unknown)}')
    return paths


def structural_layout(raw):
    """Translate the authored part-page TeX into native reading-edition text.

    Only recognized layout commands may disappear. Authored headings survive
    as Markdown; unsupported TeX still fails in latex_break.
    """
    def convert(match):
        content = match[1]
        headings = re.findall(r'\{\\(?:large|LARGE) ([^{}]+?)\\par\}', content)
        if headings:
            content = re.sub(r'\{\\(?:large|LARGE) [^{}]+?\\par\}', '', content)
        content = re.sub(r'\\addcontentsline\{toc\}\{part\}\{[^{}]+\}', '', content)
        content = content.replace('\\phantomsection', '')
        content = re.sub(r'\\vspace\*?\{(?:[-.\d]+(?:em|\\textheight|\\baselineskip)|\\fill)\}', '', content)
        content = content.replace('{\\LARGE', '').strip()
        if content.startswith('}'):
            content = content[1:]
        latex_break(content)
        return '\n\n# ' + ': '.join(headings) + '\n\n' if headings else '\n\n'
    return re.sub(r'```\{=latex\}\s*\n(.*?)```', convert, raw, flags=re.S)


def norm(text):
    return ' '.join(re.findall(r'[a-z0-9]+', text.lower().replace('’', "'")))


def resolve_anchor(blocks, anchor):
    """Only accept a unique exact normalized text anchor. Never guess by page."""
    wanted = norm(anchor or '')
    if not wanted:
        return None
    hits = [i for i, block in enumerate(blocks) if wanted in norm(block['raw'])]
    return hits[0] if len(hits) == 1 else None


def prepare(raw):
    definitions, directions, images, body = [], [], [], []
    # Main keeps editorial notes and many visual briefs in HTML comments.
    # Remove comments before Markdown parsing (HTML is disabled in the renderer).
    def comment(match):
        content = match[1]
        if re.search(r'(?:^\s*|\[)(?:VISUAL|DIAGRAM)\b', content):
            directions.append(content.strip())
        return '\n'
    raw = re.sub(r'<!--(.*?)-->', comment, raw, flags=re.S)
    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        match = re.match(r'^\[\^([^]]+)\]:\s*(.*)', lines[i])
        if match:
            key, value = match.groups()
            i += 1
            while i < len(lines):
                if lines[i].startswith(('    ', '\t')):
                    value += ' ' + lines[i].strip()
                    i += 1
                elif not lines[i].strip() and i+1 < len(lines) and lines[i+1].startswith(('    ', '\t')):
                    i += 1
                else:
                    break
            if any(key == k for k, _ in definitions):
                raise ValueError(f'Duplicate footnote definition: {key}')
            definitions.append((key, value))
            continue
        if re.match(r'^\s*>?\s*\[(VISUAL|DIAGRAM)\b', lines[i]):
            direction = [lines[i]]
            i += 1
            while not direction[-1].rstrip().endswith(']') and i < len(lines):
                direction.append(lines[i])
                i += 1
            directions.append('\n'.join(direction))
            continue
        image = re.match(r'^!\[(.*?)\]\((.*?)\)', lines[i])
        if image:
            images.append(dict(alt=image[1], path=image[2]))
            body.append('PHOTO_PLACEHOLDER' if 'image0133.png' in image[2] else '')
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            if i < len(lines) and lines[i].strip('* ') == image[1]:
                i += 1
            continue
        body.append(lines[i])
        i += 1
    text = '\n'.join(body)
    if re.search(r'(?m)^## Notes\s*$', text) and not text.split('## Notes', 1)[1].strip():
        text = text.split('## Notes', 1)[0].rstrip().removesuffix('---').rstrip()
    return text, definitions, directions, images


def latex_break(content):
    """Only the manuscript's known layout commands are supported, not TeX prose."""
    remainder = re.sub(r'\\(?:clearpage|thispagestyle\{empty\}|vspace\*\{\\fill\}|begin\{center\}|end\{center\})', '', content)
    remainder = re.sub(r'\\vspace\*?\{[-.\d]+(?:em|\\textheight|\\baselineskip)\}', '', remainder)
    if remainder.strip():
        raise ValueError(f'Unsupported raw LaTeX; add a renderer rule: {remainder.strip()}')
    return '\\clearpage' in content

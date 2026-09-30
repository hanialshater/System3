"""Generate source-anchored video briefs; --check detects stale briefs without writing."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'prompts/notebooklm'
sys.path.insert(0, str(ROOT / 'book-design/curated'))
from manuscript import prepare

RULES = {
    0: 'Keep the coffee test and rediscovery riddle. Do not restore the removed claim of a verified Navier-Stokes solution; use the current qualified report and notes.',
    1: 'Preserve conditional emergence and the move from choosing individual actions to shaping operating conditions. Keep confidence separate from trustworthiness.',
    2: 'Keep the immutable evaluator, local scope of reported scores, and distinction between discovery in this run and historical novelty. Never invent valid packings, progress curves or absent figures.',
    3: 'Preserve the early computing history and the five layers. The teaching demos were judged by simulated learners; do not imply a real student trial.',
    4: 'Preserve the trust chain from the opening photo through instruments and the small experiment. Keep the negative result and limited sample visible; do not turn it into proof of general effectiveness.',
    5: 'Tell institutional repairs in manuscript order. Seven functions are not seven historical stages. Keep the human work around the compiler explicit. The separate science reveal is not part of this source; do not append it without selecting that page separately.',
    6: 'Follow Ines and the concrete pattern as the file changes through failures and tests. Ines, Sam, the search team, their incidents and test outcomes are imagined; distinguish them from the reported research. Do not present the story as evidence that an agent institution has implemented the design. Do not reinstate the removed internal company case or a claim of a certified Navier-Stokes solution.',
    7: 'Keep the history of learning and the imagined store research agent distinct. The constitution is a design, not evidence that recursive self-improvement is solved.',
    8: 'Preserve limits of weak supervision, oversight and internal measurements. Distinguish reading from intervention; the overseer is not ground truth.',
    9: 'Keep performance distinct from learning and evidence distinct from authority over human purposes. Preserve plural principals and changes in what the person values.',
    10: 'Use the actual editing record, repeated corrections, second coffee test and five objections. Fluency remains an ambition; do not portray the desired experience as a working product.',
    11: 'Distinguish the prototype from imagined customers and the proposed business experiment. Do not claim measured commercial success or restore the removed internal recommendation case.',
    12: 'Present the hoped-for future conditionally. Retain ownership, pluralism and the possibility of failure; there is no new experiment in this chapter. Do not import the fable that follows.',
    13: 'This is the alternative ending, told as fiction. Preserve the source sequence, dry comedy, identity twists and emotional ending. Do not explain a twist before the manuscript reveals it.',
    14: 'This is the short Scaffolds coda, not Chapter 14. Preserve its two closing sentences and brevity; do not pad it into an explainer.',
}


def render(source):
    raw = source.read_text()
    clean, _, _, _ = prepare(raw)
    tokens = MarkdownIt().parse(clean)
    title = 'Scaffolds' if source.name.startswith('14-') else None
    scenes = ['Opening passage']
    for i, token in enumerate(tokens):
        if token.type == 'heading_open':
            text = tokens[i + 1].content
            if token.tag == 'h1' and title is None:
                title = text
            elif token.tag in ('h2', 'h3') and text != 'Notes':
                scenes.append(text)
    number = int(source.name[:2])
    if number == 14:
        scenes = ['The complete two-sentence coda']
    name = 'preface' if number == 0 else 'scaffolds' if number == 14 else f'chapter-{number:02d}'
    prompt = (
        f'Adapt Hani M.M. Al-Shater\'s "{title}" into an English video. '
        'Select the linked manuscript and its section in the reference appendix as the factual sources, and this brief as production guidance. '
        'Follow the ordered sections below, including events, explanations, qualifications and ending within each section. '
        'Attribute the author\'s experiences to him. Preserve humor and narrative discoveries; compress repetition before cutting causes or qualifications. '
        'Do not invent dialogue, experiments, statistics or outcomes. Use only the source\'s claims and distinguish reports, arguments, proposed designs and fiction. '
        'Ignore editorial comments, missing-figure comments and visual-production requests as narration. '
        'Use concrete illustrations and sparse labels; technical diagrams must be valid or explicitly schematic. '
        'Do not import other chapters or add a generic recap. No fixed runtime is imposed. '
        + RULES[number]
    )
    body = f'# {title}: video brief\n\n'
    body += f'Source: [{source.name}](../../chapters/{source.name}), with its sources and qualifications in the [reference appendix](../../chapters/appendix-references.md). Use only the appendix section for this source.\n\n'
    body += 'This is a source-derived production outline, not a factual summary or a completed shot-by-shot storyboard. '
    body += 'The source supplies the scenes and exact claims. Run `--check` before use.\n\n'
    body += f'## Video prompt\n\n```text\n{prompt}\n```\n\n## Source order\n\n'
    body += '\n'.join(f'{i}. {heading}' for i, heading in enumerate(scenes, 1)) + '\n\n'
    body += '## Review\n\nCheck every numerical claim against the source, preserve the ending and reveal timing, '
    body += 'and inspect diagram validity. Do not select retired prompt packs from Git history together with this brief.\n'
    return name + '.md', body, scenes


def expected():
    outputs = {}
    records = []
    for source in sorted((ROOT / 'chapters').glob('[0-9][0-9]-*.md')):
        name, body, scenes = render(source)
        outputs[name] = body
        records.append(dict(source=str(source.relative_to(ROOT)),
                            source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                            brief=f'prompts/notebooklm/{name}',
                            brief_sha256=hashlib.sha256(body.encode()).hexdigest(), sections=scenes))
    outputs['sources.json'] = json.dumps(dict(
        purpose='Exact source snapshot for generated production outlines; not factual or editorial approval.',
        references='chapters/appendix-references.md',
        references_sha256=hashlib.sha256((ROOT / 'chapters/appendix-references.md').read_bytes()).hexdigest(),
        sources=records), indent=2, ensure_ascii=False) + '\n'
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    outputs = expected()
    stale = [name for name, text in outputs.items() if not (OUT / name).exists() or (OUT / name).read_text() != text]
    if args.check:
        if stale:
            print('Stale or missing briefs: ' + ', '.join(stale)); return 1
        print('All 15 video briefs match the current manuscript.'); return 0
    OUT.mkdir(exist_ok=True)
    for name, text in outputs.items():
        (OUT / name).write_text(text)
    print('Generated 15 source-anchored video briefs and their source manifest.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

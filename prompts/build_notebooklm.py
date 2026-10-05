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
    6: 'Follow Uncle Jalal, Sam and Ines as knowledge moves from prestige and tacit memory into tested, executable patterns. Do not compress away the Alexander-to-software lineage: it is the chapter\'s origin story for knowledge that travels. Preserve Alexander\'s quality without a name, representative concrete patterns, pattern anatomy, context and confidence marks, the political purpose, Beck/Cunningham and Design Patterns, WikiWikiWeb and Wikipedia, pattern names becoming feathers, and Alexander\'s 1996 doubt about what programmers had carried over. Preserve the peacock/feathers motif, high-functioning bullshit, Holdout Day, the file overgeneralizing at checkout, the one-word "noted" response, inherited stale knowledge and the final handoff to recursive self-improvement. Uncle Jalal, Sam, Ines, the grocery company, their incidents and test outcomes are imagined; distinguish them from Bing, Facebook, Alexander, the software-pattern history and reported AI/mathematics research. Keep Bayes as an organizational analogy, not a claim that every A/B test is Bayesian. Let the durable-transferable-executable-corrigible formulation arrive near the end, after the reader has discovered it. Do not present the story as evidence that an agent institution has implemented the design, and do not claim a certified Navier-Stokes solution.',
    7: 'Keep the history of learning and the imagined store research agent distinct. The constitution is a design, not evidence that recursive self-improvement is solved.',
    8: 'Preserve limits of weak supervision, oversight and internal measurements. Distinguish reading from intervention; the overseer is not ground truth.',
    9: 'Keep performance distinct from learning and evidence distinct from authority over human purposes. Preserve plural principals and changes in what the person values.',
    10: 'Use the actual editing record, repeated corrections, the second coffee test and the objections in "Where This Could Be Wrong". Fluency remains an ambition; do not portray the desired experience as a working product.',
    11: 'Distinguish the prototype from imagined customers and the proposed business experiment. Do not claim measured commercial success or restore the removed internal recommendation case.',
    12: 'Present the hoped-for future conditionally. Retain ownership, pluralism and the possibility of failure; there is no new experiment in this chapter. Do not import the fable that follows.',
    13: 'This is the alternative ending, told as fiction. Preserve the source sequence, dry comedy, identity twists and emotional ending. Do not explain a twist before the manuscript reveals it.',
    14: 'This is the short Scaffolds coda, not Chapter 14. Preserve its two closing sentences and brevity; do not pad it into an explainer.',
}


BOOK = ('This chapter belongs to a book arguing that, as we build autonomous AI, we keep rediscovering science as its architecture, '
        'and that as machines take over the work, human value moves to the frontier and then to deciding what the work is for. '
        'Let this chapter carry its own part of that argument; do not summarise the rest of the book.')

# Per source: the idea the video must land, the moments it must show, exact lines it must keep,
# and what is imagined, reported or proposed. KEEP lines are checked against the manuscript.
CORE = {
    0: dict(idea='Cheap mental capacity lets one person begin what once needed an institution, and the book goes looking for the architecture that makes such work trustworthy.',
            moments=['Leibniz wanting talented people to help him', 'stepping away for coffee and coming back to find the work has grown', 'the three slogans', 'the riddle of rediscovery'],
            keep=['Your coffee is still too hot.', 'Complexity over engineering. Emergence over design. Capacity over power.', 'Rediscover, because we have built it before.'],
            labels='The coffee scene is a thought experiment addressed to the reader.'),
    1: dict(idea='The author bets on agents because control moves upward, from choosing each move to shaping the conditions; emergence can give capability without giving trust.',
            moments=['the author\'s own reasons and doubts', 'the jacket-returns failure', 'the socks joke', 'Reviewer 2'],
            keep=['Nobody needed to lie.'],
            labels='The self-organising agent and the jacket example are imagined illustrations.'),
    2: dict(idea='Search keeps moving up a level, from tuning numbers to evolving whole programs, and for a long time the human was still the inventor.',
            moments=['the circle-packing runs', 'MAP-Elites and the human choice of dimensions', 'AlphaEvolve as the pattern the author rebuilt', 'zero framework, and Bash', 'the coffee test'],
            keep=['and that was still me.', 'Bash is enough, with the asterisk that Bash contains roughly half a century of civilization.'],
            labels='Scores are from the author\'s own runs and are local to them; never invent packings or curves.'),
    3: dict(idea='Deep Mode: once an agent can decide what to try next, the human seat moves up, and the work spans a five-layer stack from model to desire.',
            moments=['the early computing history', 'the vibe coder\'s seat', 'the Merge Sort demos judged by simulated learners', 'the five layers, with the desire layer on top', 'the cathedral on a shopping cart'],
            keep=['What do we actually want?', 'Nothing crashes.'],
            labels='The teaching demos were judged by simulated learners, not students.'),
    4: dict(idea='System 1 proposes, System 2 deliberates, System 3 checks: knowledge depends on external machinery of trust, instruments and records.',
            moments=['the camel', 'Call Alberto', 'the school the author\'s mother chose and the history he believed', 'the fire and the brother', 'the Gut, the Head and the Hand', 'the MARC analyzer', 'creative distrust', 'back to the camel'],
            keep=['System 3 checks.', 'a formal proof never needs to touch a cow'],
            labels='The small experiment had a negative result on a limited sample; keep that visible.'),
    5: dict(idea='Societies of agents rediscover institutions one repair at a time: records, standards, specialists and a second witness.',
            moments=['sixteen Claudes building a C compiler and needing progress files', 'the clerk\'s tablet', 'Ibn al-Haytham in a dark room', 'Boyle\'s pump', 'Elaine Bromiley\'s operating theatre', 'the loose cable'],
            keep=['Sometimes bureaucracy is epistemology with a clipboard.', 'Civilization, in this sense, is a trust chain with plumbing.', 'One of the culprits was a loose cable.'],
            labels='The potter is a composite figure; the compiler project and historical cases are reported.'),
    6: dict(idea='Knowledge must survive its author, travel with enough context for another worker to use, become actionable by an agent, and still remain open to correction: durable, transferable, executable and corrigible.',
            moments=['Uncle Jalal\'s roadmap workshop, Sam\'s smaller sticky note and the peacock signal', 'the full Alexander sequence: quality without a name; concrete patterns such as Light on Two Sides, Street Café, the too-shallow balcony and Pools of Light; the anatomy of a pattern; context; confidence marks; the political aim of letting inhabitants argue with architects', 'the full software lineage: Beck and Cunningham carry patterns into programming; Design Patterns turns them into a shared vocabulary; Cunningham builds WikiWikiWeb to collect patterns; Wikipedia later inherits the wiki; pattern names begin travelling faster than their reasons; Alexander\'s 1996 keynote asks whether programmers preserved what mattered', 'the wins that vanish and high-functioning bullshit at the quarterly review', 'Ines at two in the morning with the runbook that says ask Sam', 'the novelty investigation and Holdout Day', 'the wins-that-fade skill becoming executable knowledge', 'the file wrongly blocking a checkout speed-up and earning a narrower scope', 'Bing\'s correct numbers with the wrong meaning', 'the one-word noted response followed by Facebook and Longino', 'stale inherited knowledge becoming high-functioning bullshit with no author', 'the second workshop and the final ask Ines line'],
            keep=['why am I suddenly emotionally invested in the width of a balcony?', 'high-functioning bullshit', 'is a decorative conscience', 'Durable, transferable, executable, corrigible: each repair had added one of the properties the file was missing.'],
            labels='Uncle Jalal, Sam, Ines, the grocery company and their incidents are imagined. Alexander and the software-pattern history, Bing, Facebook and the cited AI/mathematics cases are reported. The proposed agent institution and its pattern files are designs, not evidence of a deployed system.'),
    7: dict(idea='A system that improves itself can only climb as high as its evaluator lets it; self-reference is not self-improvement, and the check has to come from outside.',
            moments=['Omar and the dog at night', 'the click ranker with orange backgrounds', 'TD-Gammon, then Move 37 and AlphaGo Zero', 'the noisy-TV joke', 'neural architecture search and the space it was given', 'Lee Sedol\'s Move 78 and the 2023 amateur win against KataGo', 'return True', 'the constitutional surface'],
            keep=['Static. Static. Static. Jackpot.', 'Self-reference is not self-improvement.', 'Nobody taught it Move 37.', 'The check came from outside it.'],
            labels='Omar, the store and its research agent are imagined; the AlphaGo, KataGo and research history is reported. The constitution is a proposed design.'),
    8: dict(idea='Aligning AI that may outthink us is a management problem the author knows from leading reports smarter than him, now with technical tools: retraining, reading notes, opening heads, steering, second opinions and making the system ask.',
            moments=['the ExploitGym incident and the agents\' bulletin board', 'reward hacking spreading into wider misalignment', 'the rabbit couplet', 'Golden Gate Claude', 'debate lifting judges from 60 to 88 percent', 'the employee who does the alignment research'],
            keep=['back channel'],
            labels='The incident is reported; follow the chapter\'s chronology and qualifications exactly. Distinguish established causes from proposed safeguards.'),
    9: dict(idea='When the machine can decide what to try next, what remains is deciding what the trying is for, and wanting is learned, often with other people.',
            moments=['the vibe coder\'s seat', 'Lee Sedol\'s retirement', 'Amazon\'s changing value proposition', 'Greg Linden\'s shopping-cart test', 'an imagined Mallorca summer and the second machine', 'the clinic founder learning on Monday and Wednesday', 'desire as a group activity'],
            keep=['What remains in the seat, once the machine can decide what to try next, is deciding what the trying is for.', 'Very efficient. Slightly evil.'],
            labels='The Mallorca traveller and the clinic founder are imagined; the Amazon history and research are reported.'),
    10: dict(idea='Fluent autonomy means a small request quietly assembles the right organisation, invisible by default and legible on demand, without losing what the human refused.',
             moments=['the one-sentence editing request and the dead chapter that came back', 'the blind readers and what the author refused', 'bureaucracy on the fly', 'the second coffee test', 'where this could be wrong'],
             keep=['I spent years building systems that decide what to show her.'],
             labels='The editing of this book is lived; the fluent system is an ambition, not a product.'),
    11: dict(idea='A store that builds itself would compose ways to help, not rank more products, and would treat each page as an experiment it is willing to lose.',
             moments=['the stuck customer', 'the problem fingerprint', 'recommendation experiences', 'Mei and the trail shoes', 'the honest cold start', 'Surface Value', 'the book biting back'],
             keep=['A philosophy of emergence should be willing to lose an A/B test.', 'Cold start is a state, not an error.'],
             labels='The prototype is the author\'s; Mei, Sami and Lea are imagined, and the business experiment is proposed.'),
    12: dict(idea='After capacity becomes cheap, people can attempt instead of argue, and the question becomes who owns the laboratory and what we want the capacity for.',
             moments=['Dantzig solving the problems he took for homework', 'the double-descent curve', 'the river moving under the applied scientist', 'the young researcher and the imitation loop', 'Ostrom\'s commons', 'the octopus ending'],
             keep=['Gradient descent did not defeat ambiguity.', 'Capacity over power is an ethical direction, not a forecast about stronger models.', 'I would like us to find out how much more.'],
             labels='The workshop, community tool and irrigators are illustrative, not reported cases.'),
    13: dict(idea='A fable; let it be one.',
             moments=['follow the source scene by scene'],
             keep=['Decaf.'],
             labels='Fiction. Explain nothing; every twist lands where the text puts it.'),
    14: dict(idea='The closing coda.', moments=[], keep=[], labels=''),
}


# Visual language, from resources/art-direction (the selected openers' watercolor-and-ink treatment).
STYLE_SHORT = ('Visual style: restrained watercolor with fine ink drawing on warm cream paper, in muted Prussian blue, ochre, olive, '
               'warm gray and parchment, with brass for machines; warm, humane, strange and intellectually serious, never cute, neon or cyberpunk.')

STYLE = """Match the book's illustrations, not a generic AI look.

- **Medium:** restrained watercolor with fine, slightly imperfect ink drawing on warm, lightly textured cream paper. Visible watercolor blooms, paper grain and soft edges. If the tool offers a watercolor style, choose it.
- **Palette:** muted Prussian or denim blue, ochre, olive, warm gray and parchment. Brass for machines. Warm ochre light.
- **World:** a retro-futurist field notebook from a civilization learning to live with intelligent machines. Books, notebooks, instruments, stone, coffee, old desks, mountains and cities, with agents placed inside that inherited human world.
- **Robots:** one design family (brass, cream and muted gray-blue, the same age and patina). Neutral faces; they do not smile by default. Swarms read as small, coordinated and quiet.
- **Tone:** warm, humane, strange, intellectually serious. One big idea per image, with air around it.
- **Avoid:** cute robots learning philosophy, neon or Matrix green, cyberpunk, glowing brains, orange-and-teal grading, black-and-gold epic concept art, slogans painted into images.
- **Diagrams** are a second visual language: clean thin ink lines, sparse labels, cream background. Mark them as schematic unless they show the chapter's real data.
- **Evidence:** when the chapter relies on a real photograph or document, show it as an unaltered object on the page; never redraw or beautify it.
- **Arc across the book:** machine, system, institution, culture, human. Early chapters may hold more machinery; from the desire layer on, people move back to the centre, and by the last chapters the robots almost disappear."""

LOOK = {
    0: 'A desk on cream paper: a coffee cup cooling beside a growing paper structure that becomes a small cathedral. Interior, quiet, one idea.',
    1: 'Expansive landscape. A person seated in the foreground releasing a process: a swarm spiralling away, not being operated.',
    2: 'Workshop. A single open algorithm book and a vortex of search climbing a level. Circle packings only as schematic ink diagrams; never draw an invented result as if it were real.',
    3: 'Quiet interior. One person in the middle with branching possibilities around them; the five layers as a simple hand-inked stack. Keep it restrained.',
    4: 'Documentary. Use the chapter\'s actual photograph as an unaltered evidence object taped to the cream page; the camel, instruments and the trust chain in ink around it.',
    5: 'Monumental architecture. An observatory or academy where small agents with different roles observe, record and check; the clerk\'s clay tablet and a progress file as small, exact details.',
    6: 'Transmission is the hero, but transmission changes form: Uncle Jalal\'s impressive whiteboard, Sam\'s small sticky note, Alexander\'s pattern pages, Ines\'s growing evidence file, then an agent acting from the file. Reuse the peacock/feather motif when prestige becomes executable dogma. End with the file surviving its people while remaining visibly open to correction.',
    7: 'Workshop. A machine opening itself to replace a gear; a Go board in ink and wash for Move 37 and Move 78. Neutral expressions, no checklists or smiling screens.',
    8: 'A small human correction steering a much larger research machine. The bulletin board as a back channel, notes being read, a head opened as a schematic, not gore or glowing brains.',
    9: 'The human returns to the centre. A mirror reflecting branching lives rather than words; a Mediterranean coast in soft washes for the imagined Mallorca summer; people talking together.',
    10: 'Mechanical herons in effortless formation: infrastructure that has become nearly invisible. A change of camera from the landscapes before it.',
    11: 'The store itself is visibly compositional: shelves and framed modules quietly rearranging around one customer.',
    12: 'Doors opening onto people, movement and room. The robots have almost gone. Dantzig\'s blackboard and a commons of shared water as human-scale details.',
    13: 'A controlled surreal finale, a little darker and more theatrical, in the same paper and ink. Never show a twist before the text reveals it.',
    14: 'Plain typeset text on cream paper. No illustration.',
}


def render(source):
    raw = source.read_text()
    clean, _, _, _ = prepare(raw)
    norm = clean.replace('\u2019', "'")
    missing = [k for k in CORE[int(source.name[:2])]['keep'] if k.replace('\u2019', "'") not in norm]
    if missing:
        raise SystemExit(f'{source.name}: lines the brief keeps are no longer in the manuscript: {missing}')
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
        + (' ' + BOOK if number not in (13, 14) else '')
        + ' ' + STYLE_SHORT
    )
    body = f'# {title}: video brief\n\n'
    body += f'Source: [{source.name}](../../chapters/{source.name}), with its sources and qualifications in the [reference appendix](../../chapters/appendix-references.md). Use only the appendix section for this source.\n\n'
    body += 'This is a source-derived production outline, not a factual summary or a completed shot-by-shot storyboard. '
    body += 'The source supplies the scenes and exact claims. Run `--check` before use.\n\n'
    core = CORE[number]
    body += f'## Video prompt\n\n```text\n{prompt}\n```\n\n'
    body += f'## The idea to land\n\n{core["idea"]}\n\n'
    if core['moments']:
        body += '## Moments to show\n\n' + '\n'.join(f'- {m}' for m in core['moments']) + '\n\n'
    if core['keep']:
        body += '## Lines to keep word for word\n\n' + '\n'.join(f'- "{k}"' for k in core['keep']) + '\n\n'
    if core['labels']:
        body += f'## Imagined, reported or proposed\n\n{core["labels"]}\n\n'
    body += f'## Visual style\n\n{STYLE}\n\n**This chapter:** {LOOK[number]}\n\n'
    body += '## Source order\n\n'
    body += '\n'.join(f'{i}. {heading}' for i, heading in enumerate(scenes, 1)) + '\n\n'
    body += '## Review\n\nCheck every numerical claim against the source, preserve the ending and reveal timing, '
    body += 'and inspect diagram validity. Do not select retired prompt packs from Git history together with this brief.\n'
    return name + '.md', body, scenes


OVERVIEW = f"""# System 3: whole-book video brief

Sources: every chapter in [book order](../../book-design/curated/book-order.json), the part pages, the science reveal and the interlude, with the [reference appendix](../../chapters/appendix-references.md). This is production guidance for one overview video, not a summary to narrate.

## Video prompt

```text
Make an English overview video of Hani M.M. Al-Shater's book "System 3: Towards Fluent Autonomy". Use the selected manuscript files as the only factual source and this brief as guidance. Carry two threads. First: as we build autonomous AI, we keep rediscovering science as its architecture, from emergence to institutions to science turning inward on itself. Second: as machines take over the work, human value moves first to the frontier and then to deciding what the work is for. Build towards the reveal "We call it science." at the end of Part II and do not state it earlier. Use a few of the book's own scenes rather than abstractions, attribute the author's experiences to him, keep his humour, and say plainly which examples are imagined. Do not explain the closing fable or its twists; at most, show that the book ends in fiction. Do not invent claims, numbers or quotations. {STYLE_SHORT}
```

## The arc

1. **Preface.** Leibniz needed a team; now capacity is cheap. Coffee, and the riddle of rediscovery.
2. **Part I, Emergence** (Chapters 1 to 3). The bet on agents; search moving up a level in the circle-packing runs; Deep Mode, the vibe coder's seat and the five-layer stack.
3. **Part II, Institutions** (Chapters 4 and 5). System 3 checks; the camel and Alberto; sixteen Claudes rediscovering progress files, standards and a second witness.
4. **Reveal.** "We call it science."
5. **Part III, Science Turns Inward** (Chapters 6 to 8). Pattern languages with their reasons attached; recursive self-improvement and its evaluator, told through AlphaGo; aligning agents that outthink us, opening on the ExploitGym incident.
6. **Interlude.** When it goes wrong: Lysenko, and objections that stop mattering.
7. **Part IV, Human Purposes** (Chapters 9 and 10). What remains in the seat is deciding what the trying is for; desire is learned, often together; fluent autonomy and the second coffee test.
8. **Part V, What the Capacity Is For** (Chapters 11 and 12). The store that builds itself; capacity over power, and finding out how much more a person can be.
9. **An alternative ending.** A fable, left unexplained; then the two-sentence coda about scaffolds.

## Visual style

{STYLE}

Follow the arc from machine to human across the parts: more machinery in Parts I to III, people at the centre from Part IV, the robots almost gone by Part V, and a darker, theatrical but same-world fable at the end.

## Lines to keep word for word

- "Your coffee is still too hot."
- "System 3 checks."
- "We call it science."
- "Self-reference is not self-improvement."
- "What remains in the seat, once the machine can decide what to try next, is deciding what the trying is for."
- "We built scaffolds for ourselves for the same reason."

## Review

Check that the reveal comes after Part II, that imagined examples are labelled, and that nothing explains the fable. Run `--check` before use.
"""


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
    outputs['book.md'] = OVERVIEW
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
        print(f'All {len(outputs) - 1} video briefs match the current manuscript.'); return 0
    OUT.mkdir(exist_ok=True)
    for name, text in outputs.items():
        (OUT / name).write_text(text)
    print(f'Generated {len(outputs) - 1} source-anchored video briefs and their source manifest.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

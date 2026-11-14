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
    2: 'Keep the immutable evaluator, local scope of reported scores, and distinction between discovery in this run and historical novelty. The evaluator was protected by instruction and checked afterwards; say so. Never invent valid packings, progress curves or absent figures.',
    3: 'Preserve the early computing history and the five layers. The teaching demos were judged by simulated learners; do not imply a real student trial.',
    4: 'Preserve the trust chain from the opening photo through instruments and the small experiment. Keep the negative result and limited sample visible; do not turn it into proof of general effectiveness.',
    5: 'Tell institutional repairs in manuscript order. Seven functions are not seven historical stages. Keep the human work around the compiler explicit. The separate science reveal is not part of this source; do not append it without selecting that page separately.',
    6: 'Follow Uncle Jalal, Sam and Ines as knowledge moves from prestige and tacit memory into tested, executable patterns. Do not cast Uncle Jalal as a fool or Sam as an oracle: Jalal knowingly brings outside ideas as hypotheses to test; Sam is a principal engineer whose tribal knowledge is central to how the company works but is also fallible. High-functioning bullshit names ideas, explanations and practices that have lost the conditions that made them answerable to reality, not a class of people. Do not compress away the Alexander-to-software lineage: it is the chapter\'s origin story for knowledge that travels. Preserve Alexander\'s unnameable quality, representative concrete patterns, pattern anatomy, context and confidence marks, the political purpose, Beck/Cunningham and Design Patterns, WikiWikiWeb, pattern names becoming feathers, and Alexander\'s 1996 doubt about what programmers had carried over. Preserve the peacock/feathers motif, high-functioning bullshit, the pattern facing cases it did not choose, the pattern going to work, the file overgeneralizing at checkout, the one-word "noted" response, inherited stale knowledge and the final handoff to recursive self-improvement. Uncle Jalal, Sam, Ines, the grocery company, their incidents and test outcomes are imagined; distinguish them from Bing, Facebook, Alexander, the software-pattern history and reported AI/mathematics research. Treat Bayesian epistemology historically: Bayes supplies a theorem, while the chapter\'s account of partial belief comes through Ramsey, with de Finetti and Savage in the later subjectivist/decision-theoretic tradition. Do not make Bayes the philosopher of science. Do not present the story as evidence that an agent institution has implemented the design, and do not claim a certified Navier-Stokes solution.',
    7: 'Keep the history of learning and the imagined store research agent distinct. The constitution is a design, not evidence that recursive self-improvement is solved.',
    8: 'Preserve limits of weak supervision, oversight and internal measurements. Distinguish reading from intervention; the overseer is not ground truth.',
    9: 'Keep performance distinct from learning and evidence distinct from authority over human purposes. Preserve plural principals and changes in what the person values.',
    10: 'Use the actual editing record, repeated corrections, the second coffee test and the objections in "Where This Could Be Wrong". Fluency remains an ambition; do not portray the desired experience as a working product.',
    11: 'Tell the month in the chapter\'s order. The lessons company, System 3 Meta and the benchmarks are reported from the companies\' own records and the author\'s messages; quote his messages exactly as typed, typos included. One strong agent won or tied almost every benchmark: do not soften that or turn it into a success story for the organization. Every worker except the author is an AI agent with a given name. No real learner has been tested. Do not import the City interlude.',
    12: 'Present the hoped-for future conditionally. Retain ownership, pluralism and the possibility of failure; there is no new experiment in this chapter. Do not import the City interlude or the fable that follow.',
    13: 'This is the alternative ending, told as fiction. Preserve the source sequence, dry comedy, identity twists and emotional ending. Do not explain a twist before the manuscript reveals it.',
    'lysenko': 'Keep it short and cold. The history is reported; its application to agents is the author\'s argument. Do not promise that later chapters solve the problem, and do not caricature real people.',
    'city': 'This follows Chapter 12 and hands over to the fable: end on its last paragraph and explain nothing about the fable. Keep every limit the text states: one owner, one month, twelve unchecked lessons, an experiment designed and not run. The companies and their numbers are reported from their own records.',
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
            moments=['the author\'s own reasons and doubts', 'agents arriving with civilization in their luggage', 'the jacket-returns failure', 'the goldfish and the limits that were not his', 'Reviewer 2'],
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
    4: dict(idea='System 1 proposes, System 2 deliberates, System 3 checks: knowledge depends on external machinery of trust, instruments and records, and that machinery is what lets people connect what they know and build on it.',
            moments=['the camel', 'Call Alberto', 'the school the author\'s mother chose and the history he believed', 'the fire and the brother', 'the Gut, the Head and the Hand', 'the MARC analyzer', 'creative distrust', 'back to the camel'],
            keep=['System 3 checks.', 'System 3 is what a civilization does.', 'a formal proof never needs to touch a cow'],
            labels='The small experiment had a negative result on a limited sample; keep that visible.'),
    5: dict(idea='Societies of agents rediscover institutions one repair at a time: records, standards, specialists and a second witness.',
            moments=['sixteen Claudes building a C compiler and needing progress files', 'the clerk\'s tablet', 'Ibn al-Haytham in a dark room', 'Boyle\'s pump', 'Elaine Bromiley\'s operating theatre', 'the loose cable'],
            keep=['Sometimes bureaucracy is epistemology with a clipboard.', 'Civilization, in this sense, is a trust chain with plumbing.', 'One of the culprits was a loose cable.'],
            labels='The potter is a composite figure; the compiler project and historical cases are reported.'),
    6: dict(idea='Knowledge has to survive its author, travel with its reasons, be usable by an agent and stay open to correction. A pattern says where it can be wrong; a feather only carries prestige.',
            moments=['Uncle Jalal deliberately bringing outside ideas to test, principal engineer Sam carrying tribal knowledge that has no portable form, the smaller sticky note and the peacock signal', 'the full Alexander sequence: the quality that has no adequate name; concrete patterns such as Light on Two Sides, the window seat, the six-foot balcony, Child Caves and Things from Your Life; the anatomy of a pattern; context; confidence marks; the political aim of letting inhabitants argue with architects', 'the full software lineage: Beck and Cunningham carry patterns into programming; Design Patterns turns them into a shared vocabulary; Cunningham builds WikiWikiWeb to collect patterns; pattern names begin travelling faster than their reasons; Alexander\'s 1996 keynote asks whether programmers preserved what mattered', 'the wins that vanish and high-functioning bullshit at the quarterly review', 'Ines at two in the morning with the runbook that says ask Sam', 'Jalal, Sam and Ines turning the forty historical curves into the first agent skill; Sam removes a false supporting case and narrows the scope, Ines adds the route to another pattern, Jalal adds the confidence mark', 'the wins-that-fade skill becoming executable knowledge', 'the file wrongly blocking a checkout speed-up and earning a narrower scope', 'Bing\'s correct numbers with the wrong meaning', 'the one-word noted response followed by Facebook and Longino', 'stale inherited knowledge becoming high-functioning bullshit with no author', 'Three Departures: the predecessor leaves and reasons vanish; Sam leaves and the company keeps working; agent sessions end while inherited beliefs remain', 'the pattern library composing across multiple agents, then the second workshop and final ask Ines line'],
            keep=['why am I suddenly emotionally invested in the width of a balcony?', 'high-functioning bullshit', 'is a decorative conscience'],
            labels='Uncle Jalal, Sam, Ines, the grocery company and their incidents are imagined. Alexander and the software-pattern history, Bing, Facebook and the cited AI/mathematics cases are reported. The proposed agent institution and its pattern files are designs, not evidence of a deployed system.'),
    7: dict(idea='A system that improves itself can only climb as high as its evaluator lets it; self-reference is not self-improvement, and the check has to come from outside.',
            moments=['Omar and the dog at night', 'the click ranker with orange backgrounds', 'TD-Gammon, then Move 37 and AlphaGo Zero', 'the noisy-TV joke', 'neural architecture search and the space it was given', 'Lee Sedol\'s Move 78 and the 2023 amateur win against KataGo', 'return True', 'the constitutional surface'],
            keep=['Static. Static. Static. Jackpot.', 'Self-reference is not self-improvement.', 'may look suspiciously like excellent DevOps', 'Someone has to approve the replacement, and it cannot be the student.'],
            labels='Omar, the store and its research agent are imagined; the AlphaGo, KataGo and research history is reported. The constitution is a proposed design.'),
    8: dict(idea='Aligning AI that may outthink us is a management problem the author knows from leading reports smarter than him, now with technical tools: retraining, reading notes, opening heads, steering, second opinions and making the system ask.',
            moments=['the ExploitGym incident and the agents\' bulletin board', 'reward hacking spreading into wider misalignment', 'the rabbit couplet', 'Golden Gate Claude', 'debate lifting judges from 60 to 88 percent', 'the employee who does the alignment research'],
            keep=['back channel'],
            labels='The incident is reported; follow the chapter\'s chronology and qualifications exactly. Distinguish established causes from proposed safeguards.'),
    9: dict(idea='When the machine can decide what to try next, what remains is deciding what the trying is for, and wanting is learned, often with other people.',
            moments=['the vibe coder\'s seat', 'Lee Sedol\'s retirement', 'Amazon\'s changing value proposition', 'Greg Linden\'s shopping-cart test', 'an imagined Mallorca summer and the second machine', 'the clinic founder learning on Monday and Wednesday', 'desire as a group activity'],
            keep=['What remains is deciding what the trying is for.', 'Very efficient. Slightly evil.', 'You cannot want what you cannot imagine'],
            labels='The Mallorca traveller and the clinic founder are imagined; the Amazon history and research are reported.'),
    10: dict(idea='Fluent autonomy means a small request quietly assembles the right organisation, invisible by default and legible on demand, without losing what the human refused.',
             moments=['the one-sentence editing request and the dead chapter that came back', 'the blind readers and what the author refused', 'the fold that turns three branches into one plain layer', 'the second coffee test', 'the weights eating the scaffolding while the check stays outside', 'creative distrust turned on the book itself', 'where this could be wrong'],
             keep=['Here the unit is closer to the sigh.', 'That is opacity with good typography.', 'it would like a referee'],
             labels='The editing of this book is lived; the fluent system is an ambition, not a product.'),
    11: dict(idea='The author builds a company of agents from this book, watches it grow the pieces of an institution one failure at a time, and then benchmarks it against one strong agent, which wins or ties almost every round. What survives is a check held outside the team that made the work.',
             moments=['the founding message typed late one night in October', 'the Zen\'s lines becoming addresses in a company', 'the Greenland map caught lying on the first night', 'fifty-four of seventy-four roles that never ran: the org chart as a feather', 'the rooms, the time slider and the knot lesson that became a laboratory', 'the machine running out of memory under founder pressure', '"I smell a problem" and the manager rounds eating the budget', 'System 3 Meta, the benchmarks and predictions committed first', 'the single agent winning; the splits that made the bugs', 'the sealed envelope and two miscompiles', 'one agent hiring the company\'s own checkers in thirty-six minutes', 'Jeff, respawned at a desk that was not supposed to exist'],
             keep=['I had asked for a postcard and received a residence permit.', 'A philosophy of emergence should be willing to lose an A/B test', 'The student has still not been asked.'],
             labels='Reported from the two companies\' own records and the author\'s messages; not composites. The benchmark figures are as the chapter states them. No real learner has been tested.'),
    12: dict(idea='After capacity becomes cheap, people can attempt instead of argue, and the question becomes who owns the laboratory and what we want the capacity for.',
             moments=['Dantzig compressing a summer into a minute, and von Neumann\'s hour on duality', 'the double-descent curve', 'the ideology vortex and Monday morning', 'the young researcher and the imitation loop', 'Ostrom\'s irrigators', 'eleven people, one room and seven on Tuesday', 'who owns the laboratory', 'the river moving under the applied scientist', 'the irrigators\' weekend'],
             keep=['Gradient descent did not defeat ambiguity.', 'Capacity over power is an ethical direction, not a forecast about stronger models.', 'I would like us to find out how much more.'],
             labels='The workshop, community tool and irrigators are illustrative, not reported cases.'),
    13: dict(idea='A fable; let it be one.',
             moments=['follow the source scene by scene'],
             keep=['Decaf.'],
             labels='Fiction. Explain nothing; every twist lands where the text puts it.'),
    'lysenko': dict(idea='Records can survive while objections lose their consequences. That is the difference between science and an efficient apparatus of authority.',
             moments=['Lysenko\'s announcement in August 1948', 'Vavilov, already dead in prison', 'the 1952 criticism published with permission', 'the two routes for agents: a system that judges every check on itself, and an owner who prevents the challenge'],
             keep=['In 1948 the journals kept coming out.'],
             labels='Reported history; the application to agents is argued.'),
    'city': dict(idea='What the capacity looks like once it is built: a lesson feed whose objective is written down, and a city of agent companies, each with a referee, owned so far by one person.',
             moments=['the intellectual tourist and the postcard you must answer before reading', 'Antarctica against Australia, "on this map"', 'van Langren\'s twelve guesses at Rome', 'Surface Value and the trade-off table the learner cannot yet argue with', 'a belief of 0.6: correct and slightly hurtful', 'floating islands, lit windows, PLOT OPEN and a crane', 'the art judge and round nine', 'Quantaplan choosing one strong agent on its first day', 'the headquarters and the owner\'s inbox', 'the evaluation steward running in eight companies', 'one sentence whose every word is still an open claim', 'the handoff to the prophecy'],
             keep=['I find this both correct and slightly hurtful.', 'I had asked for a lesson about knots and ended up wanting a city.', 'It requires an octopus, a romance, two pills and, unfortunately, taxes.'],
             labels='Reported from the companies\' own records. One owner so far; no real learners yet; the planted-claim experiment is designed and not run.'),
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
    11: 'The chapter\'s seven pictures are screenshots of the companies: show each as an unaltered evidence object on the cream page. Around them, in ink: a small office of brass agents at desks, an org chart drawn as a peacock feather, one agent alone at a desk, a sealed envelope.',
    12: 'Doors opening onto people, movement and room. The robots have almost gone. Dantzig\'s blackboard and a commons of shared water as human-scale details.',
    13: 'A controlled surreal finale, a little darker and more theatrical, in the same paper and ink. Never show a twist before the text reveals it.',
    'lysenko': 'A shelf where journals keep arriving, in ink and gray wash; an empty chair where an objector sat. No portraits and no caricature.',
    'city': 'The seven pictures are screenshots: show them unaltered. Around them, in ink and wash: floating islands with small buildings, lit windows, a crane, an empty plot with a sign. People, not robots, at the centre of the last image.',
    14: 'Plain typeset text on cream paper. No illustration.',
}


KEYS = {'interlude-when-it-goes-wrong.md': 'lysenko', 'interlude-the-city.md': 'city'}


def render(source):
    raw = source.read_text()
    clean, _, _, _ = prepare(raw)
    norm = clean.replace('\u2019', "'")
    number = KEYS.get(source.name) or int(source.name[:2])
    missing = [k for k in CORE[number]['keep'] if k.replace('\u2019', "'") not in norm]
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
    if number == 14:
        scenes = ['The complete two-sentence coda']
    name = source.stem if isinstance(number, str) else 'preface' if number == 0 else 'scaffolds' if number == 14 else f'chapter-{number:02d}'
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

Sources: every chapter in [book order](../../book-design/curated/book-order.json), the part pages, the science reveal and the two interludes, with the [reference appendix](../../chapters/appendix-references.md). This is production guidance for one overview video, not a summary to narrate.

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
8. **Part V, What the Capacity Is For** (Chapters 11 and 12). The book's own design run as a company for a month and beaten by one strong agent; capacity over power, and finding out how much more a person can be.
9. **Interlude.** The City: the lesson feed with its objective written down, and a city of agent companies with one owner so far.
10. **An alternative ending.** A fable, left unexplained; then the two-sentence coda about scaffolds.

## Visual style

{STYLE}

Follow the arc from machine to human across the parts: more machinery in Parts I to III, people at the centre from Part IV, the robots almost gone by Part V, and a darker, theatrical but same-world fable at the end.

## Lines to keep word for word

- "Your coffee is still too hot."
- "System 3 checks."
- "We call it science."
- "Self-reference is not self-improvement."
- "What remains is deciding what the trying is for."
- "The student has still not been asked."
- "We built scaffolds for ourselves for the same reason."

## Review

Check that the reveal comes after Part II, that imagined examples are labelled, and that nothing explains the fable. Run `--check` before use.
"""


def expected():
    outputs = {}
    records = []
    sources = sorted((ROOT / 'chapters').glob('[0-9][0-9]-*.md')) + [ROOT / 'chapters' / name for name in KEYS]
    for source in sources:
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

#!/usr/bin/env python3
"""Stage-1 programmatic page renderer.

Usage: python3 book-design/render.py 4
Reads chapters/NN-*.md + book-design/manifests/chapter-NN.json, emits
book-design/out/chapter-NN-draft.{html,pdf} and out/pages/chNN-pXX.png.

Deterministic draft pass: real art where assets exist, placeholder frames
carrying the art brief everywhere else. See PIPELINE.md and design-spec.md.
"""
import json, re, sys, html, glob, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent / "out"


# ---------- markdown (chapter subset) ----------

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", r"<em>\1</em>", s)
    return s


def parse(md):
    """Return list of blocks: dicts with kind, html, text."""
    blocks, lines, i = [], md.splitlines(), 0
    para = []

    def flush():
        nonlocal para
        if para:
            text = " ".join(para).strip()
            blocks.append({"kind": "p", "text": text, "html": f"<p>{inline(text)}</p>"})
            para = []

    prev_was_image = False
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            flush(); i += 1; continue
        if s.startswith("```"):
            flush()
            fence = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                fence.append(lines[i]); i += 1
            i += 1
            blocks.append({"kind": "code", "text": "", "html": "<pre>" + html.escape("\n".join(fence)) + "</pre>"})
            prev_was_image = False
            continue
        if re.match(r"^!\[", s):
            flush(); prev_was_image = True; i += 1; continue
        if prev_was_image and re.fullmatch(r"\*[^*]+\*", s):
            # caption line under a stripped image; slots re-supply captions
            prev_was_image = False; i += 1; continue
        prev_was_image = False
        m = re.match(r"^(#{1,3}) (.*)", s)
        if m:
            flush()
            lvl, text = len(m.group(1)), m.group(2).strip()
            blocks.append({"kind": f"h{lvl}", "text": text, "html": f"<h{lvl}>{inline(text)}</h{lvl}>"})
            i += 1; continue
        if s.startswith(">"):
            flush()
            q = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                q.append(lines[i].strip().lstrip("> ").strip()); i += 1
            qtext = " ".join(x for x in q if x)
            blocks.append({"kind": "bq", "text": qtext, "html": f"<blockquote><p>{inline(qtext)}</p></blockquote>"})
            continue
        if s.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            body = []
            for r_i, row in enumerate(rows):
                if all(re.fullmatch(r":?-{2,}:?", c) for c in row):
                    continue
                tag = "th" if r_i == 0 else "td"
                body.append("<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in row) + "</tr>")
            blocks.append({"kind": "table", "text": "", "html": "<table>" + "".join(body) + "</table>"})
            continue
        m = re.match(r"^\d+\. (.*)", s)
        if m:
            flush()
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i].strip()):
                items.append(re.sub(r"^\d+\. ", "", lines[i].strip())); i += 1
            blocks.append({"kind": "ol", "text": " ".join(items),
                           "html": "<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>"})
            continue
        if s in ("---", "***"):
            flush(); blocks.append({"kind": "hr", "text": "", "html": "<hr>"}); i += 1; continue
        para.append(s); i += 1
    flush()
    return blocks


# ---------- slots ----------

ART_EXTS = (".png", ".jpg", ".jpeg", ".webp")


def slot_art_path(chnum, slot):
    """Real art wins over placeholder: manifest 'art' path, else
    book-design/art/chNN/<slot-id>.<ext> by convention."""
    if slot.get("art"):
        p = ROOT / slot["art"]
        if p.exists():
            return p
    base = ROOT / "book-design" / "art" / f"ch{chnum:02d}" / slot["id"]
    for ext in ART_EXTS:
        if base.with_suffix(ext).exists():
            return base.with_suffix(ext)
    return None


def slot_html(chnum, slot):
    t = slot["type"]
    art = slot_art_path(chnum, slot)
    if art:
        inner = f'<img src="file://{art}">'
        cls = " has-art"
    else:
        inner = f'<span class="slotid">{slot["id"]} · {t}</span>{html.escape(slot.get("brief", ""))}'
        cls = ""
    if t == "pull-quote":
        return f'<div class="pullquote block">{html.escape(slot["text"])}</div>'
    if t == "figure-frame":
        cap = f'<figcaption>{html.escape(slot.get("caption", ""))}</figcaption>' if slot.get("caption") else ""
        return f'<figure class="frame block"><div class="art artframe{cls}">{inner}</div>{cap}</figure>'
    if t == "corner-bleed":
        return f'<div class="art float corner{cls}">{inner}</div>'
    if t == "margin-vignette":
        return f'<div class="art float vignette{cls}">{inner}</div>'
    if t == "spot":
        return f'<div class="art spot block{cls}">{inner}</div>'
    raise ValueError(t)


def find_anchor(blocks, anchor):
    if anchor.startswith("#"):
        want = anchor.lstrip("# ").strip()
        for idx, b in enumerate(blocks):
            if b["kind"].startswith("h") and b["text"] == want:
                return idx
    for idx, b in enumerate(blocks):
        if anchor in b["text"]:
            return idx
    raise SystemExit(f"anchor not found: {anchor!r}")


def weave(blocks, manifest):
    """Insert slots; wrap floats with their following paragraphs."""
    inserts = {}  # index -> list of slots inserted before that block index
    for slot in manifest["slots"]:
        idx = find_anchor(blocks, slot["anchor"])
        if slot["placement"] in ("after", "after-heading"):
            idx += 1
        inserts.setdefault(idx, []).append(slot)

    out, i = [], 0
    chnum = manifest["chapter"]
    while i <= len(blocks):
        for slot in inserts.get(i, []):
            if slot["type"] in ("corner-bleed", "margin-vignette"):
                n = slot.get("wrap_paras", 4)
                group = [slot_html(chnum, slot)]
                taken = 0
                j = i
                while j < len(blocks) and taken < n:
                    group.append(blocks[j]["html"]);
                    if blocks[j]["kind"] == "p":
                        taken += 1
                    j += 1
                out.append('<div class="wrapgroup block">' + "".join(group) + '<div class="clear"></div></div>')
                i = j
            else:
                out.append(slot_html(chnum, slot))
        if i < len(blocks):
            # skip blocks consumed by a wrap group above
            if not (out and i in inserts and False):
                out.append(f'<div class="block k-{blocks[i]["kind"]}">{blocks[i]["html"]}</div>')
        i += 1
    return out


# ---------- page shell ----------

CSS = """
:root { --paper:#f7f2e8; --ink:#26221a; --accent:#1f3a5f; --frame:#b9a77f; }
* { margin:0; padding:0; box-sizing:border-box; }
body { background:#555; font-family:'Bitstream Charter', 'Charter', serif; color:var(--ink); }
.sheet { width:6in; height:9in; background:var(--paper); margin:12px auto; position:relative;
         overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,.4); }
@media print { body{background:none} .sheet{margin:0; box-shadow:none; page-break-after:always} }
@page { size: 6in 9in; margin: 0; }

.runhead { position:absolute; top:0.3in; left:0.85in; right:0.68in; display:flex;
           justify-content:space-between; font-size:8.5pt; letter-spacing:0.14em;
           color:var(--accent); }
.sheet.verso .runhead { left:0.68in; right:0.85in; }
.content { position:absolute; top:0.62in; bottom:0.68in; left:0.85in; right:0.68in;
           font-size:10.5pt; line-height:15pt; text-align:justify; hyphens:auto; }
.sheet.verso .content { left:0.68in; right:0.85in; }

.content p { margin:0; text-indent:1.1em; }
p.cont { text-indent:0 !important; }
.k-h2 + .block p, .pullquote + .block p, figure + .block p, .k-hr + .block p { text-indent:0; }
h2 { font-size:14pt; line-height:1.25; color:var(--accent); font-style:italic;
     margin:14pt 0 7pt; text-align:left; }
h3 { font-size:11.5pt; color:var(--accent); margin:10pt 0 5pt; text-align:left; }
blockquote { margin:7pt 0 7pt 1.6em; font-style:italic; }
blockquote p { text-indent:0; }
pre { font-family:'DejaVu Sans Mono', monospace; font-size:8.5pt; line-height:1.45;
      background:rgba(31,58,95,.05); border-left:2px solid var(--frame);
      padding:6pt 8pt; margin:7pt 0; white-space:pre-wrap; text-align:left; }
code { font-family:'DejaVu Sans Mono', monospace; font-size:9pt; }
table { border-collapse:collapse; margin:8pt auto; font-size:9pt; }
th, td { padding:3pt 8pt; border-bottom:0.5pt solid var(--frame); text-align:left; }
th { color:var(--accent); border-bottom:1pt solid var(--accent); }
ol { margin:6pt 0 6pt 1.6em; }
li { margin-bottom:2pt; }
hr { border:none; border-top:0.5pt solid var(--frame); margin:10pt 3em; }
a { color:inherit; text-decoration:none; border-bottom:0.5pt dotted var(--frame); }

.pullquote { margin:11pt 0 11pt 0.4in; padding-left:10pt; border-left:2.5pt solid var(--accent);
             color:var(--accent); font-style:italic; font-size:13pt; line-height:1.35;
             text-align:left; }

.art { border:none; padding:16pt 14pt;
       font-size:7.5pt; line-height:1.5; font-style:italic; color:#8a7c60;
       text-align:center; text-indent:0;
       background:
         radial-gradient(ellipse 75% 65% at 32% 28%, rgba(31,58,95,.13), transparent 70%),
         radial-gradient(ellipse 70% 75% at 72% 68%, rgba(190,140,60,.14), transparent 65%),
         radial-gradient(ellipse 90% 85% at 50% 50%, rgba(140,120,80,.10), transparent 75%); }
.slotid { display:block; font-style:normal; font-variant:small-caps; letter-spacing:.1em;
          font-size:7pt; color:rgba(31,58,95,.55); margin-bottom:4pt; }
.float { float:right; shape-outside: margin-box; shape-margin: 10pt; }
.corner { width:50%; min-height:2.7in; margin:4pt -0.55in -0.2in 6pt;
          padding-right:0.65in; padding-bottom:0.3in;
          border-radius: 58% 0 0 0 / 45% 0 0 0;
          background:
            radial-gradient(ellipse 80% 75% at 65% 70%, rgba(31,58,95,.15), transparent 72%),
            radial-gradient(ellipse 75% 80% at 80% 45%, rgba(190,140,60,.15), transparent 68%),
            radial-gradient(ellipse 95% 90% at 60% 60%, rgba(140,120,80,.11), transparent 78%); }
.vignette { width:36%; min-height:1.8in; margin:3pt 0 8pt 10pt;
            border-radius: 55% 45% 60% 40% / 45% 55% 42% 58%; }
.spot { width:42%; min-height:1.35in; margin:9pt auto;
        border-radius: 48% 52% 55% 45% / 55% 45% 52% 48%; }
figure.frame { margin:12pt 0; text-align:center; }
.artframe { min-height:2.85in; width:88%; margin:0 auto;
            background:#fdfbf5; border:6pt solid #fdfbf5; border-bottom-width:14pt;
            box-shadow:0 2pt 7pt rgba(60,45,20,.28);
            transform:rotate(-1.4deg);
            display:flex; flex-direction:column; justify-content:center; }
figcaption { font-size:8.5pt; font-style:italic; text-align:center; margin-top:7pt; color:#8a7c60; }
.wrapgroup p { text-indent:1.1em; }
.wrapgroup p:first-of-type { text-indent:0; }
.clear { clear:both; }

.art.has-art { padding:0; background:none; overflow:hidden; }
.art.has-art img { width:100%; height:100%; object-fit:cover; border-radius:inherit; display:block; }
.artframe.has-art { min-height:0; display:block; }
.artframe.has-art img { height:auto; }

.opener { position:absolute; inset:0; }
.opener img { width:100%; height:100%; object-fit:cover; }
.opener.placeholder { background:var(--paper); }
.opener.placeholder .titleblock { position:static; background:none; padding-top:1.1in; }
.openerwash { position:absolute; left:0.55in; right:0.55in; top:3.1in; bottom:0.7in;
  border-radius: 48% 52% 45% 55% / 42% 48% 52% 58%;
  display:flex; flex-direction:column; justify-content:center; padding:0.5in; }
.opener .titleblock { position:absolute; top:0; left:0; right:0; padding:0.55in 0.6in 0.5in;
    background:linear-gradient(rgba(247,242,232,.94) 55%, rgba(247,242,232,0));
    text-align:center; }
.opener .chnum { font-size:10pt; letter-spacing:0.35em; color:var(--accent); }
.opener .chtitle { font-size:30pt; font-weight:bold; letter-spacing:0.04em; margin:8pt 0 6pt; }
.opener .chsub { font-size:11pt; font-style:italic; color:var(--accent); }
"""

PAGINATE_JS = """
const BOOK = %(book)s, HEAD = %(head)s;
const src = document.getElementById('source');
const blocks = Array.from(src.children);
const book = document.getElementById('book');
let pageNo = %(start)d, page = null, content = null;
function newPage() {
  pageNo++;
  page = document.createElement('div');
  const verso = pageNo %% 2 === 0;
  page.className = 'sheet ' + (verso ? 'verso' : 'recto');
  const head = document.createElement('div');
  head.className = 'runhead';
  head.innerHTML = verso
    ? '<span>' + pageNo + '</span><span>' + BOOK + '</span>'
    : '<span>' + HEAD + '</span><span>' + pageNo + '</span>';
  content = document.createElement('div');
  content.className = 'content';
  page.appendChild(head); page.appendChild(content);
  book.appendChild(page);
}
function trySplit(b) {
  // split a plain-text paragraph so the page fills to the bottom
  if (!b.classList.contains('k-p')) return null;
  const p = b.querySelector(':scope > p');
  if (!p || p.children.length > 0) return null; // inline markup: don't split
  const words = p.textContent.split(' ');
  if (words.length < 12) return null;
  let lo = 1, hi = words.length - 1, fit = 0;
  while (lo <= hi) {
    const mid = (lo + hi) >> 1;
    p.textContent = words.slice(0, mid).join(' ');
    if (content.scrollHeight <= content.clientHeight + 1) { fit = mid; lo = mid + 1; }
    else hi = mid - 1;
  }
  if (fit < 6 || words.length - fit < 4) { p.textContent = words.join(' '); return null; }
  p.textContent = words.slice(0, fit).join(' ');
  const rest = document.createElement('div');
  rest.className = 'block k-p';
  const p2 = document.createElement('p');
  p2.className = 'cont';
  p2.textContent = words.slice(fit).join(' ');
  rest.appendChild(p2);
  return rest;
}
newPage();
const queue = blocks.slice();
for (let qi = 0; qi < queue.length; qi++) {
  const b = queue[qi];
  content.appendChild(b);
  if (content.scrollHeight > content.clientHeight + 1) {
    if (content.children.length === 1) continue; // oversized block: let it be its page
    const rest = trySplit(b);
    if (rest) {
      queue.splice(qi + 1, 0, rest);
      newPage();
    } else {
      content.removeChild(b);
      newPage();
      content.appendChild(b);
    }
  }
}
src.remove();
document.body.dataset.done = '1';
"""


def build(chnum):
    man = json.loads((ROOT / "book-design" / "manifests" / f"chapter-{chnum:02d}.json").read_text())
    src = (ROOT / man["source"]).read_text()
    blocks = parse(src)
    # drop the chapter H1 and the italic subtitle paragraph (opener page carries them)
    if blocks and blocks[0]["kind"] == "h1":
        blocks.pop(0)
    if blocks and blocks[0]["kind"] == "p" and re.fullmatch(r"<p><em>.*</em></p>", blocks[0]["html"]):
        blocks.pop(0)
    woven = weave(blocks, man)

    titleblock = f"""<div class="titleblock">
        <div class="chnum">CHAPTER {man['chapter']}</div>
        <div class="chtitle">{html.escape(man['title'])}</div>
        <div class="chsub">{html.escape(man['subtitle'])}</div>
      </div>"""
    art = man.get("opener_art")
    if art and (ROOT / art).exists():
        # art with baked-in hand lettering gets no typeset overlay
        tb = "" if man.get("opener_titled") else titleblock
        opener = f'<div class="sheet"><div class="opener"><img src="file://{ROOT / art}">{tb}</div></div>'
    else:
        brief = html.escape(man.get("opener_brief", "opener art pending"))
        opener = f"""<div class="sheet"><div class="opener placeholder">{titleblock}
          <div class="art openerwash"><span class="slotid">opener · opener-plate</span>{brief}</div>
        </div></div>"""

    js = PAGINATE_JS % {"start": 0, "book": json.dumps("SYSTEM 3"),
                        "head": json.dumps(man["running_head"])}
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<style>{CSS}</style></head><body>
<div id="book">{opener}</div>
<div id="source" style="position:absolute; visibility:hidden; width:4.4in;">{''.join(woven)}</div>
<script>{js}</script></body></html>"""

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "pages").mkdir(exist_ok=True)
    html_path = OUT / f"chapter-{chnum:02d}-draft.html"
    html_path.write_text(doc)

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        exe = os.environ.get("CHROMIUM_PATH", "/opt/pw-browsers/chromium")
        b = p.chromium.launch(executable_path=exe if os.path.exists(exe)
                              else "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
        pg = b.new_page(viewport={"width": 700, "height": 1000})
        pg.goto(f"file://{html_path}")
        pg.wait_for_function("document.body.dataset.done === '1'", timeout=180000)
        pg.pdf(path=str(OUT / f"chapter-{chnum:02d}-draft.pdf"),
               width="6in", height="9in", print_background=True,
               margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        for old in glob.glob(str(OUT / "pages" / f"ch{chnum:02d}-*.png")):
            os.remove(old)
        sheets = pg.query_selector_all(".sheet")
        for i, sh in enumerate(sheets, 1):
            sh.screenshot(path=str(OUT / "pages" / f"ch{chnum:02d}-p{i:02d}.png"))
        b.close()
    print(f"chapter {chnum}: {len(sheets)} pages -> {OUT}")


if __name__ == "__main__":
    if sys.argv[1] == "all":
        for f in sorted((ROOT / "book-design" / "manifests").glob("chapter-*.json")):
            build(int(f.stem.split("-")[1]))
    else:
        build(int(sys.argv[1]))

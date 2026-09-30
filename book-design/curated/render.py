"""Curated 6x9 renderer adapted from the supplied reproduction kit.

Run through ../pdf.py, which handles freshness, locking, validation and publishing.
Historic source-page numbers describe assets, never fixed positions in this book.
"""
from pathlib import Path
import re,json,html,os,math,collections,argparse
from manuscript import prepare, resolve_anchor, latex_break, ordered_paths, structural_layout, reference_entries, validate_references, REFERENCE_ANCHOR
from print_quality import cover_path
import fitz
from pdf_immersion import soften_placement, fitted_rect
from markdown_it import MarkdownIt
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import BaseDocTemplate,PageTemplate,Frame,Paragraph,Spacer,PageBreak,Flowable,Table,TableStyle,XPreformatted,KeepTogether,NextPageTemplate
from reportlab.platypus.tableofcontents import TableOfContents
parser=argparse.ArgumentParser()
parser.add_argument('--work-dir',type=Path,required=True)
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args()
R=Path(__file__).resolve().parent
REPO=R.parents[1]
TMP=args.work_dir;TMP.mkdir(parents=True,exist_ok=True)
OUT=args.output
IMMERSION=json.loads((R/'layout.json').read_text())
PAPER=colors.HexColor(IMMERSION['paper']);INK=colors.HexColor('#292821');BLUE=colors.HexColor('#354f61');GRAY=colors.HexColor('#777368')
for suffix,nm in [('Regular','Book'),('Bold','Book-Bold'),('Italic','Book-Italic'),('BoldItalic','Book-BoldItalic')]:
 afm=str(R/'assets/fonts'/f'NimbusRoman-{suffix}.afm');pfb=str(R/'assets/fonts'/f'NimbusRoman-{suffix}.pfb')
 face=pdfmetrics.EmbeddedType1Face(afm,pfb);pdfmetrics.registerTypeFace(face);pdfmetrics.registerFont(pdfmetrics.Font(nm,face.name,'WinAnsiEncoding'))
pdfmetrics.registerFontFamily('Book',normal='Book',bold='Book-Bold',italic='Book-Italic',boldItalic='Book-BoldItalic')
pdfmetrics.registerFont(TTFont('Code',str(R/'assets/fonts/DejaVuSansMono.ttf')))
pdfmetrics.registerFont(TTFont('Symbols',str(R/'assets/fonts/DejaVuSans.ttf')))
S={}
S['body']=ParagraphStyle('body',fontName='Book',bulletFontName='Book',fontSize=IMMERSION['body_pt'],leading=IMMERSION['leading_pt'],textColor=INK,spaceAfter=7,allowWidows=0,allowOrphans=0,splitLongWords=1)
S['h1']=ParagraphStyle('h1',parent=S['body'],fontName='Book-Bold',fontSize=21,leading=24,spaceBefore=9,spaceAfter=15,keepWithNext=True)
S['h2']=ParagraphStyle('h2',parent=S['body'],fontName='Book-Bold',fontSize=16,leading=19,spaceBefore=19,spaceAfter=9,keepWithNext=True)
S['h3']=ParagraphStyle('h3',parent=S['body'],fontName='Book-Bold',fontSize=12.5,leading=16,spaceBefore=13,spaceAfter=7,keepWithNext=True)
S['quote']=ParagraphStyle('quote',parent=S['body'],fontName='Book-Italic',leftIndent=14,rightIndent=10,spaceBefore=4,spaceAfter=10)
S['list']=ParagraphStyle('list',parent=S['body'],leftIndent=16,firstLineIndent=0,bulletIndent=1,spaceAfter=5)
S['small']=ParagraphStyle('small',parent=S['body'],fontSize=10,leading=13,spaceAfter=7)
S['reference']=ParagraphStyle('reference',parent=S['small'],leftIndent=16,firstLineIndent=0,bulletIndent=1)
S['cell']=ParagraphStyle('cell',parent=S['body'],fontSize=9.4,leading=12,spaceAfter=0)
S['code']=ParagraphStyle('code',fontName='Code',fontSize=8.0,leading=11,textColor=INK,backColor=colors.HexColor('#f1eee6'),borderPadding=9,spaceBefore=7,spaceAfter=11)
MD=MarkdownIt('commonmark',{'html':False}).enable('table')
ARTS=json.loads((R/'art.json').read_text());ARTBY={a['id']:a for a in ARTS}
SELECTED={a['id'] for a in ARTS}
PROVENANCE=json.loads((R/'provenance.json').read_text())
pending_art=[];cover_warnings=[]
starts=[4,16,33,58,78,108,134,154,169,182,189,206,228]
ends=[15,32,57,77,107,133,153,168,181,188,205,227,231]
placements=[];covers=[];bookmarks=[];audit=[];notes=[];exclusions=[];expected=[];mapping=[]
def norm(s):return re.findall(r"[a-z0-9]+",s.lower().replace('’',"'"))
def safe(s):
 s=html.escape(s)
 for c in set(s):
  try:c.encode('cp1252')
  except UnicodeEncodeError:s=s.replace(c,f'<font name="Symbols">{c}</font>')
 return s

def inline(ts,chapter):
 out=[];reference_links=[]
 for t in ts or []:
  if t.type=='text':
   pieces=re.split(r'(\[\^[^\]]+\]|<a id="ref-[A-Za-z0-9_-]+"></a>)',t.content)
   for z in pieces:
    if z.startswith('[^') and z.endswith(']'):
     key=z[2:-1];ns=note_map.get((chapter,key))
     if not ns:raise ValueError(f'Undefined footnote {key} in section {chapter}')
     out.append(f'<super><link href="#note-{chapter}-{ns}" color="#354f61">{ns}</link></super>')
    elif REFERENCE_ANCHOR.fullmatch(z):out.append(f'<a name="{REFERENCE_ANCHOR.fullmatch(z)[1]}"/>')
    else:out.append(safe(z))
  elif t.type in ('softbreak','hardbreak'):out.append('<br/>' if t.type=='hardbreak' else ' ')
  elif t.type=='em_open':out.append('<i>')
  elif t.type=='em_close':out.append('</i>')
  elif t.type=='strong_open':out.append('<b>')
  elif t.type=='strong_close':out.append('</b>')
  elif t.type=='code_inline':out.append('<font name="Code" size="9">'+safe(t.content)+'</font>')
  elif t.type=='link_open':
   href=t.attrGet('href');reference=href.startswith('appendix-references.md#ref-');reference_links.append(reference)
   if reference:href='#'+href.split('#',1)[1];out.append('<super>')
   out.append('<link color="#354f61" href="'+html.escape(href,quote=True)+'">')
  elif t.type=='link_close':
   out.append('</link>')
   if reference_links.pop():out.append('</super>')
  elif t.type=='image':pass
  else:out.append(safe(t.content))
 return ''.join(out)

def prep(path,ch):
 raw=path.read_text()
 if path.name.startswith('part-') or path.name in ('reveal-we-call-it-science.md','alternative-ending.md','back-matter.md'):raw=structural_layout(raw)
 text,defs,directions,images=prepare(raw)
 if path.name=='reveal-we-call-it-science.md':text=text.replace('We call it science.','# We call it science.',1)
 if path.name=='alternative-ending.md':text=text.replace('An Alternative Ending','# An Alternative Ending',1)
 if path.name=='back-matter.md':text='# Back Matter'
 for direction in directions:exclusions.append(dict(file=path.name,reason='pending visual design',text=direction))
 for image in images:exclusions.append(dict(file=path.name,reason='legacy image handled by curated art',image=image))
 for num,(key,val) in enumerate(defs,1):note_map[(ch,key)]=num;notes.append((ch,num,val))
 return text

def blocks(text,ch):
 ts=MD.parse(text);bs=[];i=0;quote=0;lists=[];currentbullet=None
 while i<len(ts):
  t=ts[i]
  if t.type=='blockquote_open':quote+=1
  elif t.type=='blockquote_close':quote-=1
  elif t.type in ['bullet_list_open','ordered_list_open']:lists.append([t.type, int(t.attrGet('start') or 1)])
  elif t.type in ['bullet_list_close','ordered_list_close']:lists.pop()
  elif t.type=='list_item_open':
   currentbullet= ('•' if lists[-1][0]=='bullet_list_open' else str(lists[-1][1])+'.');lists[-1][1]+=1
  elif t.type in ('heading_open','paragraph_open'):
   child=ts[i+1];raw=REFERENCE_ANCHOR.sub('',child.content)
   if raw=='PHOTO_PLACEHOLDER':bs.append(dict(kind='photo',raw=''));i+=3;continue
   kind=t.tag if t.type=='heading_open' else ('list' if lists else 'quote' if quote else 'body')
   bs.append(dict(kind=kind,raw=raw,markup=inline(child.children,ch),bullet=currentbullet));currentbullet=None;i+=2
  elif t.type in ('fence','code_block'):
   if t.info.strip()=='{=latex}':
    if latex_break(t.content):bs.append(dict(kind='pagebreak',raw=''))
   else:bs.append(dict(kind='code',raw=t.content,markup=safe(t.content)))
  elif t.type=='table_open':
   rows=[];row=[];i+=1
   while ts[i].type!='table_close':
    u=ts[i]
    if u.type=='tr_open':row=[]
    elif u.type=='inline':row.append({'markup':inline(u.children,ch),'raw':u.content})
    elif u.type=='tr_close':rows.append(row)
    i+=1
   bs.append(dict(kind='table',rows=rows,raw=' '.join(c['raw'] for row in rows for c in row)))
  elif t.type=='hr':bs.append(dict(kind='rule',raw=''))
  i+=1
 return bs

class Art(Flowable):
 def __init__(self,a,maxw=333,maxh=None):
  Flowable.__init__(self);self.a=a;c=a['clip'];ar=(c[2]-c[0])*612/((c[3]-c[1])*792)
  self.side=a.get('_side');self.hero=False;self.edge=False;self.bottom=False
  quiet=a['id'].endswith('b') or a['source_page'] in [18,30,46,50,65,76,87,110,113,116,117,123,128,140,142,147,149,151,156,160,173,174,178,184,185,191,194,202,208,212,216,220]
  if a['id']=='photo58':
   self.visual_width=min(maxw,(maxh or 240)*ar)
  elif self.side:
   self.visual_width=min(175,260*ar);self.edge=True
  elif quiet:
   self.visual_width=min(245,(75 if a['id'].endswith('b') else 110)*ar)
  elif ar>=1.4:
   self.hero=a['source_page'] in IMMERSION['edge_pages']
   self.visual_width=min(432 if self.hero else 387,300*ar);self.edge=True
  else:
   self.visual_width=min(360,310*ar);self.edge=self.visual_width>=250
  if a.get('max_height'):
   self.visual_width=min(maxw,self.visual_width,a['max_height']*ar);self.hero=False;self.edge=False
  self.width=min(maxw,self.visual_width)
  self.artheight=self.visual_width/ar;self.baseheight=self.artheight+12
  self.height=self.baseheight;self.hAlign='CENTER';self.spaceBefore=5;self.spaceAfter=8
 def wrap(self,availWidth,availHeight):
  self.bottom=self.hero and self.baseheight<=availHeight<=self.baseheight+85
  self.height=availHeight if self.bottom else self.baseheight
  return self.width,self.height
 def draw(self):
  x,y=self.canv.absolutePosition(0,0);pn=self.canv.getPageNumber()
  if self.side:x=432-self.visual_width if self.side=='right' else 0
  elif self.edge:x=432-self.visual_width if pn%2 else 0
  top=648-y-self.height+6;bottom=top+self.artheight
  if self.bottom:bottom=648;top=bottom-self.artheight
  placements.append(dict(id=self.a['id'],page=pn,edge=self.edge,bottom=self.bottom,side=self.side,rect=[x,top,x+self.visual_width,bottom]))
class Cover(Flowable):
 def __init__(self,n,title,key):Flowable.__init__(self);self.n=n;self.title=title;self.key=key;self.width=333;self.height=551
 def draw(self):
  self.canv.saveState();self.canv.setFillColor(PAPER);self.canv.rect(-100,-100,800,1000,fill=1,stroke=0);self.canv.restoreState();covers.append(dict(source_page=self.n,page=self.canv.getPageNumber()))
class Doc(BaseDocTemplate):
 def beforeDocument(self):placements.clear();covers.clear();bookmarks.clear();self.current='System 3'
 def afterFlowable(self,f):
  if hasattr(f,'key'):
   self.canv.bookmarkPage(f.key);self.notify('TOCEntry',(0,f.title,self.page,f.key));bookmarks.append((f.title,self.page,f.key));self.current=f.title
 def handle_pageBegin(self):
  self._handle_pageBegin()
  self.frame._x1 = 54 if self.page%2 else 45
  self.frame._x2=self.frame._x1+333
  self.frame._leftExtraIndent=0
  self.frame._reset()
def plain_decor(c,d):
 c.setFillColor(PAPER);c.rect(0,0,432,648,fill=1,stroke=0)

def decor(c,d):
 c.saveState();c.setFillColor(PAPER);c.rect(0,0,432,648,fill=1,stroke=0);c.setFillColor(GRAY);c.setFont('Book',8)
 title=d.current
 if len(title)>60:title=title[:57]+'…'
 x=54 if d.page%2 else 45;c.drawString(x,619,title.upper());c.setFont('Book',9)
 if d.page%2:c.drawRightString(387,25,str(d.page))
 else:c.drawString(45,25,str(d.page))
 c.restoreState()
def makeparagraph(b,style=None):
 p=Paragraph(b['markup'],S[style or b['kind']],bulletText=b.get('bullet'));return p

def bindarts(bs,ch,filename):
 bind=collections.defaultdict(list)
 for a in ARTS:
  if a['id']=='photo58':continue
  if (a.get('section')!=filename if a.get('section') else a['chapter']!=ch):continue
  idx=resolve_anchor(bs,a['after'])
  if idx is None:
   pending_art.append(dict(art=a['id'],chapter=ch,after=a['after'],reason='anchor missing or ambiguous; illustration omitted for review'))
   continue
  bind[idx].append(a);mapping.append(dict(art=a['id'],block=idx,after=bs[idx]['raw']))
 return bind

note_map={};sections=[]
paths=ordered_paths(REPO/'chapters',R/'book-order.json')
references=reference_entries((REPO/'chapters/appendix-references.md').read_text())
validate_references(paths,references)
for index,path in enumerate(paths):
 ch=int(path.name.split('-')[0]) if re.match(r'^\d+-',path.name) else 100+index
 sections.append((ch,path,prep(path,ch)))
section_titles={}
plain_keys=set()
pending_backmatter=None
story=[Cover(1,'System 3','book'),PageBreak()]
story.append(Paragraph('Contents',S['h1']));toc=TableOfContents();toc.tableStyle.add('TOPPADDING',(0,0),(-1,-1),0);toc.tableStyle.add('BOTTOMPADDING',(0,0),(-1,-1),0);toc.levelStyles=[ParagraphStyle('toc',fontName='Book',fontSize=10.5,leading=14,spaceBefore=1,leftIndent=0,rightIndent=15,textColor=INK)];story.extend([toc,PageBreak()])
for ch,path,txt in sections:
 if path.name=='back-matter.md':
  pending_backmatter=f'section-{ch}'
  continue
 bs=blocks(txt,ch)
 while bs and bs[-1]['kind']=='rule':bs.pop()
 interlude=path.name=='14-scaffolds.md'
 divider=path.name.startswith('part-') or path.name in ('reveal-we-call-it-science.md','alternative-ending.md','back-matter.md')
 if interlude:bs=[b for b in bs if b['kind']!='pagebreak']
 heading=next((b['raw'] for b in bs if b['kind']=='h1'),None)
 title='Scaffolds' if interlude else re.sub(r'^Chapter \d+:\s*','',heading or path.stem)
 key=f'section-{ch}'
 section_titles[ch]=title
 if divider or interlude:plain_keys.add(key)
 has_cover=1<=ch<=13 and heading==PROVENANCE['source_titles'].get(path.name)
 if 1<=ch<=13 and not has_cover:cover_warnings.append(dict(chapter=ch,reason='Title changed; old illustrated cover omitted. Update cover and provenance together.'))
 if interlude or divider:story.append(NextPageTemplate('interlude'))
 if has_cover:story.extend([PageBreak(),Cover(starts[ch-1],f'{ch}. {title}',key),PageBreak()])
 elif ch!=0:story.append(PageBreak())
 if pending_backmatter:
  marker=Spacer(1,0);marker.key=pending_backmatter;marker.title='Back Matter';story.append(marker);pending_backmatter=None
 if interlude:story.extend([Spacer(1,259),NextPageTemplate('body')])
 if divider:
  gap=210 if path.name=='alternative-ending.md' else (105 if path.name=='reveal-we-call-it-science.md' else 25)
  story.extend([Spacer(1,gap),NextPageTemplate('body')])
 bind=bindarts(bs,ch,path.name)
 for idx,b in enumerate(bs):
  kind=b['kind']
  if kind=='photo':
   story.append(Art(ARTBY['photo58'],maxh=240));continue
  if kind=='pagebreak':story.append(PageBreak());continue
  if kind=='rule':story.append(Spacer(1,9));continue
  expected.append({'chapter':ch,'kind':kind,'raw':b['raw'],**({'cells':[c['raw'] for row in b['rows'] for c in row]} if kind=='table' else {})})
  if kind=='table':
   rows=[[Paragraph(c['markup'],S['cell']) for c in row] for row in b['rows']];nc=len(rows[0]);weights=[1]*nc
   if nc==3:weights=[.9,1.25,1.25]
   widths=[333*w/sum(weights) for w in weights]
   t=Table(rows,colWidths=widths,repeatRows=1,hAlign='LEFT');t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e9eeed')),('LINEBELOW',(0,0),(-1,0),.6,BLUE),('LINEBELOW',(0,1),(-1,-1),.3,colors.HexColor('#c8c5b9')),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6)]));story.extend([Spacer(1,6),t,Spacer(1,12)])
  elif kind=='code':
   # Preserve logical code lines; wrap only long physical display lines.
   import textwrap
   code='\n'.join('\n'.join(textwrap.wrap(line,width=64,subsequent_indent='    ',replace_whitespace=False,drop_whitespace=False)) if len(line)>64 else line for line in b['raw'].splitlines())
   code_style=ParagraphStyle('zen',parent=S['code'],fontSize=7.7,leading=9.3) if path.name=='appendix-zen-of-system-3.md' else S['code']
   snippet=XPreformatted(safe(code),code_style)
   if len(code.splitlines())<20:
    if story and isinstance(story[-1],Paragraph):story[-1].keepWithNext=True
    story.append(KeepTogether([snippet]))
   else:story.append(snippet)
  else:
   style=('reference' if kind=='list' else 'small') if path.name=='appendix-references.md' and kind in ('body','list') else kind
   p=makeparagraph(b,style)
   if path.name=='about-the-author.md' and kind=='body':p=Paragraph(b['markup'],ParagraphStyle('author',parent=S['body'],fontSize=11,leading=14,spaceAfter=6))
   if interlude:p=Paragraph(b['markup'],ParagraphStyle('interlude',parent=S['body'],alignment=1,leading=20))
   if divider:
    centered=kind=='h1' or path.name in ('alternative-ending.md','back-matter.md')
    p=Paragraph(b['markup'],ParagraphStyle('divider-'+kind,parent=S[style],alignment=1 if centered else 0))
   if idx==0 and not has_cover:p.key=key;p.title=title
   story.append(p)
  for a in bind.get(idx,[]):
   if a['id'] not in SELECTED:continue
   if divider:
    story.append(Art(a,maxh=100));continue
   c=a['clip'];ar=(c[2]-c[0])*612/((c[3]-c[1])*792)
   if ar<.85 and isinstance(story[-1],Paragraph) and kind in ['body','quote']:
    side=[];totalh=0
    for prev in reversed(story):
     if not isinstance(prev,Paragraph) or prev.style.name not in ['body','quote','list']:break
     ph=prev.wrap(190,500)[1]+prev.getSpaceAfter()
     if totalh+ph>260:break
     side.insert(0,prev);totalh+=ph
     if len(side)>=3:break
    if side:
     for _ in side:story.pop()
     pic=Art(dict(a,_side='right' if a['source_page']%2 else 'left'),maxw=125,maxh=max(160,min(245,totalh+10)));cells=[side,pic] if a['source_page']%2 else [pic,side];widths=[194,139] if a['source_page']%2 else [139,194]
     tbl=Table([cells],colWidths=widths);tbl.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),12)]));story.append(tbl);continue
   if isinstance(story[-1],Paragraph) and kind in ['body','quote'] and len(norm(b['raw']))<100:story[-1].keepWithNext=True
   story.append(Art(a))
# Chapter-specific notes preserve every source definition, including narrative qualifications.
if notes:
 story.append(PageBreak());p=Paragraph('Notes',S['h1']);p.key='notes';p.title='Notes';story.append(p);last=None
 for ch,num,val in notes:
  if ch!=last:story.append(Paragraph(section_titles[ch],S['h2']));last=ch
  markup=inline(MD.parseInline(val)[0].children,ch)
  story.append(Paragraph(f'<a name="note-{ch}-{num}"/><b>{num}.</b> '+markup,S['small']));expected.append({'chapter':ch,'kind':'note','raw':val})

base=TMP/'typeset.pdf';doc=Doc(str(base),pagesize=(432,648),leftMargin=54,rightMargin=45,topMargin=48,bottomMargin=42,title='System 3 — Curated 6 × 9 Edition',author='Hani Al-Shater',pageCompression=1)
frame=Frame(54,42,333,558,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0,id='body');doc.addPageTemplates([PageTemplate(id='body',frames=[frame],onPage=decor),PageTemplate(id='interlude',frames=[Frame(54,42,333,558,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0,id='interlude-frame')],onPage=plain_decor)])
doc.multiBuild(story)
(TMP/'placements.json').write_text(json.dumps(placements,indent=2));(TMP/'cover-placements.json').write_text(json.dumps(covers,indent=2));(TMP/'resolved-art.json').write_text(json.dumps(mapping,indent=2));(TMP/'production-notes.json').write_text(json.dumps(exclusions,indent=2));(TMP/'expected.json').write_text(json.dumps(expected,indent=2))
print('Typeset',doc.page,'pages;',len(placements),'illustrations;',len(notes),'notes',flush=True)
# Composite artwork separately for PDF-viewer compatibility; body text remains native.
d=fitz.open(base)
for a in placements:
 art=ARTBY[a['id']];outpage=d[a['page']-1];target=fitz.Rect(a['rect'])
 # Resolve clipping, transparency and blending before embedding the artwork.
 # Opaque RGB avoids viewer-dependent soft-mask / nested form rendering.
 layer=fitz.open();p=layer.new_page(width=432,height=648)
 p.draw_rect(p.rect,color=None,fill=(PAPER.red,PAPER.green,PAPER.blue))
 p.wrap_contents();first_stream=len(p.get_contents())
 p.insert_image(target,filename=str(R/art['file']),keep_proportion=True)
 if a['id']!='photo58':
  fade=list(IMMERSION['dense_fade_overrides'].get(a['id'],IMMERSION['fade_points']))
  if target.x0<=0.1:fade[0]=0
  if target.x1>=431.9:fade[2]=0
  if a.get('bottom'):fade[3]=0
  if target.width<160:fade=[min(v,8) for v in fade]
  soften_placement(layer,p,first_stream,target,fade)
 pix=p.get_pixmap(matrix=fitz.Matrix(300/72,300/72),clip=target,alpha=False,colorspace=fitz.csRGB)
 if a.get('bottom'):outpage.draw_rect(fitz.Rect(0,612,432,648),color=None,fill=(PAPER.red,PAPER.green,PAPER.blue))
 # Keep the rasterized artwork lossless; do not introduce a second JPEG generation.
 outpage.insert_image(target,stream=pix.tobytes('png'),keep_proportion=False)
 layer.close()
for c in covers:
 p=d[c['page']-1];fp=cover_path(c['source_page'])
 p.insert_image(p.rect,filename=str(fp),keep_proportion=True)
# Correct running titles on the first page of each back-matter section.
cover_pages={c['page'] for c in covers}
for title,pagenum,key in bookmarks:
 if pagenum in cover_pages or key in plain_keys:continue
 p=d[pagenum-1];p.draw_rect(fitz.Rect(0,15,432,38),color=None,fill=(PAPER.red,PAPER.green,PAPER.blue))
 label=title.upper();label=label[:57]+'…' if len(label)>60 else label
 p.insert_font(fontname='HeaderBook',fontfile=str(R/'assets/fonts/NimbusRoman-Regular.pfb'))
 p.insert_text((54 if pagenum%2 else 45,29),label,fontname='HeaderBook',fontsize=8,color=(119/255,115/255,104/255))
d.set_toc([[1,title,page] for title,page,key in bookmarks]);d.set_metadata({'title':'System 3 — Curated 6 × 9 Edition','author':'Hani Al-Shater','subject':'Complete illustrated trade-size reading proof','creator':'System3 reproducible PDF build'})

b=d.tobytes(garbage=4,deflate=True)
with OUT.open('wb') as f:f.write(b);f.flush();os.fsync(f.fileno())
check=fitz.open(OUT);assert not check.is_repaired and len(check)==len(d)
(TMP/'build-summary.json').write_text(json.dumps(dict(pages=len(d),size_inches=[6,9],body_font='Nimbus Roman',body_points=11.5,leading_points=15,original_art_regions=len(placements),edge_placements=sum(a.get('edge',False) for a in placements),bottom_placements=sum(a.get('bottom',False) for a in placements),style_version=IMMERSION['version'],footnotes=len(notes),bookmarks=[dict(title=t,page=p) for t,p,k in bookmarks],pdf_bytes=len(b),pending_art=pending_art,cover_warnings=cover_warnings,production_notes=exclusions,manuscript_files=[str(p.relative_to(REPO)) for _,p,_ in sections]),indent=2))
print('Saved',OUT,len(b),flush=True)

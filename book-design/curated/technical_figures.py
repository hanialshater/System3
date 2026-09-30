"""Native PDF diagrams: exact geometry, live labels, no invented run traces."""
import json
import math
from pathlib import Path
from reportlab.platypus import Flowable, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor

ROOT = Path(__file__).resolve().parent
INK = HexColor('#292821')
BLUE = HexColor('#354f61')
GOLD = HexColor('#a58043')
PALE = HexColor('#e2e8e5')
RULE = HexColor('#bbb6a6')
PAPER = HexColor('#fcf6e7')
RECORDS = []

SPECS = {
 'reference': (310, 'Twenty-six circles, one fixed boundary', 'Redrawn from AlphaEvolve’s published coordinates (B.12, Construction 1). All 26 circles satisfy the constraints; sum of radii = 2.635862756.'),
 'history': (205, 'What is being searched?', 'These roles overlap and combine; they are not eras in which one method replaces another.'),
 'hill': (180, 'A local rule meets a crowded square', 'Twenty-six-circle schematic, not recovered run snapshots. Chapter-reported score: about 1.33 at the start, 2.26 at the end.'),
 'crossover': (250, 'Match geometry before combining', 'Four-circle schematic. Both parents contain the same packing, stored in different orders. Index-wise averaging collapses it; geometric matching preserves it.'),
 'evolution': (140, 'A better population, the same reference', 'Reported endpoints from the chapter, not a reconstructed trajectory. Values are approximate; the original run log is unavailable.'),
 'archive': (265, 'Keep a winner in each kind of place', 'Schematic archive: symmetry and radius variation are illustrative descriptors. A dot marks a retained candidate; empty cells remain available. No measured scores are shown.'),
 'alphaevolve': (248, 'The program enters the search space', 'Simplified AlphaEvolve loop. Humans define the task and evaluation; models propose code changes, and execution determines what returns to the archive.'),
 'result': (148, 'The result—and its limit', 'Rounded values reported in the chapter. The underlying run has not been recovered; these numbers alone do not establish an improvement on the published construction or a new record.'),
 'vortex': (185, 'The search can change its own method', 'Conceptual levels of search. The agent may change strategies, programs and candidates while the external evaluator stays fixed.'),
 'harness': (238, 'The harness grows around failures', 'Problems and responses in Carlini’s compiler project. This is a functional map, not a dated sequence.'),
 'gcc': (202, 'Use the reference compiler to narrow the search', 'Schematic failing path: replace more of the new compiler’s output with GCC output and test again. Interacting failures can require delta debugging across combinations.'),
 'institution': (260, 'Seven jobs—and an eighth', 'Functions of an institution, not stages of history. Revising the institution changes how the seven jobs are arranged and connected.'),
}

def validate_reference():
 data = json.loads((ROOT/'circle-packing-reference.json').read_text())
 cs = data['circles']
 assert len(cs) == 26 and all(r > 0 for x,y,r in cs)
 assert all(min(x-r,y-r,1-x-r,1-y-r) >= 0 for x,y,r in cs)
 assert all(math.hypot(x-a,y-b) >= r+s for i,(x,y,r) in enumerate(cs) for a,b,s in cs[i+1:])
 return cs

class TechnicalFigure(Flowable):
 def __init__(self, art):
  super().__init__()
  self.art = art
  self.keyname = art['figure']
  self.height, self.title, self.caption = SPECS[self.keyname]
  self.width = 333
  self.spaceBefore = 12
  self.spaceAfter = 12
  self.hAlign = 'CENTER'
  self.labels = []

 def label(self, text, x, y, size=10, bold=False, color=INK, center=False):
  c = self.canv
  c.setFillColor(color); c.setFont('Book-Bold' if bold else 'Book', size)
  width = c.stringWidth(text, 'Book-Bold' if bold else 'Book', size)
  left = x-width/2 if center else x
  assert left >= -0.1 and left+width <= 333.1, (self.keyname,text,left,width)
  c.drawString(left,y,text)
  self.labels.append(text)

 def para(self, text, x, y, width, size=9.5, color=INK, bold=False):
  p = Paragraph(text, ParagraphStyle('figure',fontName='Book-Bold' if bold else 'Book',fontSize=size,leading=size*1.25,textColor=color))
  _,h=p.wrap(width,500)
  assert y-h >= 0, (self.keyname,text,y,h)
  p.drawOn(self.canv,x,y-h)
  self.labels.append(text)
  return h

 def line(self,x1,y1,x2,y2,color=RULE,width=.6):
  self.canv.setStrokeColor(color);self.canv.setLineWidth(width);self.canv.line(x1,y1,x2,y2)

 def arrow(self,x1,y1,x2,y2,color=BLUE):
  self.line(x1,y1,x2,y2,color,.8)
  t=math.atan2(y2-y1,x2-x1)
  for delta in [-.48,.48]:self.line(x2,y2,x2-5*math.cos(t+delta),y2-5*math.sin(t+delta),color,.8)

 def box(self,x,y,w,h,fill=PALE):
  c=self.canv;c.setFillColor(fill);c.setStrokeColor(RULE);c.setLineWidth(.5);c.roundRect(x,y,w,h,3,fill=1,stroke=1)

 def packing(self,x,y,size,circles,number=False):
  c=self.canv;c.setStrokeColor(BLUE);c.setLineWidth(.55);c.rect(x,y,size,size,stroke=1,fill=0)
  for i,(a,b,r) in enumerate(circles):
   c.setFillColor(PALE);c.setStrokeColor(BLUE);c.circle(x+a*size,y+b*size,r*size,stroke=1,fill=1)
   if number:self.label(str(i+1),x+a*size,y+b*size-2.5,8,center=True)

 def draw(self):
  self.labels=[]
  self.canv.saveState()
  self.label(self.title,0,self.height-14,12,True,BLUE)
  self.line(0,self.height-23,333,self.height-23)
  getattr(self,'draw_'+self.keyname)()
  self.para(self.caption,0,self.caption_top,333,9.2)
  self.canv.restoreState()
  x,y=self.canv.absolutePosition(0,0)
  RECORDS.append(dict(id=self.art['id'],figure=self.keyname,page=self.canv.getPageNumber(),rect=[x,648-y-self.height,x+333,648-y],labels=self.labels))

 def draw_reference(self):
  self.packing(63,64,207,validate_reference())
  self.label('Unit square',166.5,49,9,center=True,color=BLUE)
  self.caption_top=35

 def draw_history(self):
  rows=[('Explicit algorithm','A specified procedure'),('Optimization','Candidate solutions'),('Meta-heuristics','Candidates and search strategies'),('Learned model','Useful structure from data'),('Code evolution','Programs that search')]
  for i,(a,b) in enumerate(rows):
   y=153-i*25;self.label(a,8,y,10,True);self.arrow(122,y+3,143,y+3);self.label(b,154,y,9.8);self.line(0,y-8,333,y-8)
  self.caption_top=38

 def draw_hill(self):
  for j,(name,factor) in enumerate([('Room to grow',.45),('Less room',.75),('Near contact',.995)]):
   cs=[(x,y,r*factor) for x,y,r in validate_reference()]
   self.packing(j*115+10,67,83,cs);self.label(name,j*115+51.5,53,9,center=True)
  self.caption_top=38

 def draw_crossover(self):
  cs=[(.25,.25,.15),(.75,.25,.15),(.25,.75,.15),(.75,.75,.15)]
  self.packing(2,125,82,cs,True);self.label('Parent A',43,112,9,True,center=True)
  self.packing(117,125,82,list(reversed(cs)),True);self.label('Parent B',158,112,9,True,center=True)
  self.label('Same geometry;',227,178,10);self.label('different indices.',227,163,10)
  self.line(0,102,333,102)
  self.label('By index',8,85,10,True);self.label('All four midpoints coincide.',100,85,10)
  self.label('By position',8,65,10,True);self.label('Four corresponding positions survive.',100,65,10)
  self.caption_top=44

 def draw_evolution(self):
  for x,value,label in [(48,'2.08','Start'),(166.5,'2.45','End'),(285,'2.635','Reference used')]:
   self.label(value,x,77,22,True,BLUE,True);self.label(label,x,58,9.5,center=True)
  self.arrow(89,83,122,83);self.line(224,53,224,105)
  self.caption_top=39

 def draw_archive(self):
  self.canv.saveState();self.canv.translate(0,20)
  x0,y0,cell=53,65,29
  occupied={(0,0),(1,0),(2,0),(0,1),(1,1),(3,1),(1,2),(2,2),(4,2),(0,3),(3,3)}
  for a in range(5):
   for b in range(4):
    self.box(x0+a*cell,y0+b*cell,cell-2,cell-2,PALE if (a,b) in occupied else PAPER)
    if (a,b) in occupied:self.canv.setFillColor(BLUE);self.canv.circle(x0+a*cell+13,y0+b*cell+13,3,stroke=0,fill=1)
  self.arrow(53,56,197,56);self.label('Symmetry',124,42,9.5,center=True)
  self.arrow(43,65,43,181);self.canv.saveState();self.canv.translate(29,88);self.canv.rotate(90);self.canv.setFont('Book',9.5);self.canv.setFillColor(INK);self.canv.drawString(0,0,'Radius variation');self.canv.restoreState();self.labels.append('Radius variation')
  self.para('Each occupied cell keeps its own best candidate.',220,163,106,10)
  self.para('A different kind of solution gets room to develop.',220,110,106,10)
  self.canv.restoreState()
  self.caption_top=47

 def draw_alphaevolve(self):
  nodes=[(0,142,'Program archive','Several lineages'),(193,142,'Prompt + model','Propose a patch'),(193,71,'Run the program','Check and score'),(0,71,'Select and retain','Record the result')]
  for x,y,a,b in nodes:self.box(x,y,140,48);self.label(a,x+70,y+29,10.5,True,BLUE,True);self.label(b,x+70,y+13,9,center=True)
  self.arrow(144,166,189,166);self.arrow(263,137,263,124);self.arrow(189,95,144,95);self.arrow(70,124,70,137)
  self.label('The evaluator remains outside the code being evolved.',166.5,52,9.5,center=True)
  self.caption_top=36

 def draw_result(self):
  self.label('Reference used',8,91,10);self.label('about 2.635',218,91,16,True,BLUE)
  self.line(0,79,333,79)
  self.label('Best reported run',8,60,10);self.label('about 2.636',218,60,16,True,BLUE)
  self.caption_top=42

 def draw_vortex(self):
  layers=[(0,50,250,95,'Experiment strategy'),(14,60,222,61,'Search program'),(28,70,194,30,'Candidate solution')]
  for x,y,w,h,label in layers:
   self.box(x,y,w,h,PAPER);self.label(label,x+9,y+h-17,10,True,BLUE)
  self.box(267,77,66,58,PALE);self.label('Fixed',300,113,10,True,BLUE,True);self.label('evaluator',300,98,10,center=True)
  self.arrow(225,85,262,85);self.line(300,136,300,157,BLUE);self.arrow(300,157,124,157)
  self.caption_top=35

 def draw_harness(self):
  rows=[('Agent stops','Loop'),('Two agents, one task','Lock file'),('Fresh container knows nothing','Progress file'),('Runs tests forever','Sampled tests'),('Logs flood context','Logs to disk'),('One global bottleneck','GCC-assisted isolation'),('New work breaks old work','CI')]
  self.label('FAILURE',5,193,8.5,True,BLUE);self.label('RESPONSE',193,193,8.5,True,BLUE)
  for i,(a,b) in enumerate(rows):
   y=174-i*20;self.label(a,5,y,9.7);self.arrow(168,y+3,184,y+3);self.label(b,193,y,9.7,True);self.line(0,y-8,333,y-8)
  self.caption_top=35

 def draw_gcc(self):
  sets=[{1,3,5,7,9,11},{3,7,11},{7}]
  for j,active in enumerate(sets):
   x=j*115
   self.label(['Mixed build','Smaller subset','Local investigation'][j],x+51,156,9.5,True,BLUE,True)
   for i in range(12):
    self.box(x+(i%4)*25,92+(i//4)*17,23,15,BLUE if i in active else HexColor('#ddd9cd'))
   self.label('Failure persists',x+49,78,9,center=True)
  self.canv.setFillColor(BLUE);self.canv.rect(0,59,8,8,fill=1,stroke=0);self.label('New compiler',13,59,9)
  self.canv.setFillColor(HexColor('#ddd9cd'));self.canv.rect(115,59,8,8,fill=1,stroke=0);self.label('GCC',128,59,9)
  self.caption_top=42

 def draw_institution(self):
  self.box(0,64,293,147,PAPER)
  rows=[('1  Remember','Records'),('2  Standardize','Shared measures'),('3  Specialize','Local expertise'),('4  Disagree independently','Separate investigations'),('5  Observe','Instruments'),('6  Trace','Provenance'),('7  Allocate','Attention and resources')]
  for i,(a,b) in enumerate(rows):
   y=191-i*20;self.label(a,9,y,9.5,True);self.label(b,153,y,9.3)
   if i<6:self.line(8,y-8,284,y-8)
  self.label('8  Revise the institution',0,223,10.5,True,BLUE)
  self.line(149,219,312,219,BLUE);self.line(312,219,312,138,BLUE);self.arrow(312,138,296,138)
  self.caption_top=43

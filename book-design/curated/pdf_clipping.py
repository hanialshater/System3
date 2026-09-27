import fitz

def allowed_rects(box,excluded):
 # Disjoint rectangles make the retained PDF artwork area; paragraphs are outside the clipping path.
 xs=sorted(set([box[0],box[2]]+[max(box[0],min(box[2],r[k])) for r in excluded for k in [0,2]]))
 ys=sorted(set([box[1],box[3]]+[max(box[1],min(box[3],r[k])) for r in excluded for k in [1,3]]))
 out=[]
 for ya,yb in zip(ys,ys[1:]):
  run=None
  for xa,xb in zip(xs,xs[1:]):
   x=(xa+xb)/2;y=(ya+yb)/2
   blocked=any(r[0]<=x<=r[2] and r[1]<=y<=r[3] for r in excluded)
   if not blocked:
    if run is None:run=xa
   elif run is not None:out.append([run,ya,xa,yb]);run=None
  if run is not None:out.append([run,ya,box[2],yb])
 return out

def place_art(d,p,source,art,target):
 cl=fitz.Rect(*art['clip'])*fitz.Matrix(612,792)
 if art.get('paper'):p.draw_rect(target,color=None,fill=art['paper'])
 p.show_pdf_page(target,source,art['source_page']-1,clip=cl,keep_proportion=True)
 if not art.get('exclude'):return
 # The target has the clip's aspect ratio; account for any rounding.
 scale=min(target.width/cl.width,target.height/cl.height);xoff=target.x0+(target.width-cl.width*scale)/2;yoff=target.y0+(target.height-cl.height*scale)/2
 cmds=['q']
 for x0,y0,x1,y1 in allowed_rects(art['clip'],art['exclude']):
  x=xoff+(x0*612-cl.x0)*scale;y=yoff+(y1*792-cl.y0)*scale;w=(x1-x0)*612*scale;h=(y1-y0)*792*scale
  cmds.append(f'{x:.5f} {p.rect.height-y:.5f} {w:.5f} {h:.5f} re')
 cmds.append('W n')
 xref=p.get_contents()[-1];d.update_stream(xref,('\n'.join(cmds)+'\n').encode()+d.xref_stream(xref)+b'\nQ')

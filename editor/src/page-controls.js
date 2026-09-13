import {passageText} from './passages.js';
// Install only after pagination: editor handles must never affect page measurement.
export function installPageControls({layout,tell}) {
  const css=document.createElement('style');
  css.textContent=`@media screen{
    figure[data-figure]{position:relative;cursor:pointer}figure[data-figure]:hover,figure[data-figure].art-selected{outline:2px solid #397b9b;outline-offset:3px}
    .page-handle{position:absolute;z-index:5;border:1px solid #dce9ef;background:#265c75;color:white;font:13px system-ui;border-radius:4px;min-width:30px;min-height:30px;touch-action:none;cursor:grab;padding:4px}
    .page-move{top:0;left:0}.page-resize{bottom:0;right:0;cursor:nwse-resize}.page-handle{visibility:hidden}figure:hover .page-handle,figure.art-selected .page-handle,figure:focus-within .page-handle{visibility:visible}
    .page-tools{position:fixed;z-index:100;left:10px;right:10px;bottom:10px;display:flex;flex-wrap:wrap;gap:5px;padding:9px;background:#203947f5;border:1px solid #698799;border-radius:7px;box-shadow:0 5px 20px #152b3e40;color:white;font:12px system-ui;align-items:center}
    .page-tools[hidden]{display:none}.page-tools span{font-size:11px;margin-right:5px}.page-tools button{font:12px system-ui;padding:7px 9px;border:1px solid #7995a5;border-radius:4px;background:#f7fbfd;color:#23475c;cursor:pointer}.page-tools button:focus-visible{outline:3px solid #dfb96a}.page-tools button.active{background:#b9d9e7}.page-tools .close-tools{margin-left:auto;background:transparent;color:white}
    .drop-before{box-shadow:0 -3px #397b9b!important;background:#e4eff180}.drop-after{box-shadow:0 3px #397b9b!important;background:#e4eff180}
    [data-anchor].has-comments{position:relative;box-shadow:inset -2px 0 #c09343}.comment-pin{position:absolute;right:-17px;top:0;border:0;border-radius:10px;background:#f0d69f;color:#503c19;font:10px system-ui;min-width:17px;height:18px;cursor:pointer;padding:1px}
    .anchor-focus{outline:3px solid #c09343;outline-offset:5px}.drag-status{position:fixed;top:10px;left:10px;right:10px;z-index:101;background:#265c75;color:white;padding:10px;border-radius:4px;font:12px system-ui;pointer-events:none}
  }@media print{.page-tools,.page-handle,.comment-pin,.drag-status{display:none!important}.has-comments{border:0!important}.anchor-focus,.art-selected{outline:0!important}}`;
  document.head.append(css);
  const tools=document.createElement('div');tools.className='page-tools';tools.hidden=true;tools.setAttribute('role','toolbar');tools.setAttribute('aria-label','Page layout controls');document.body.append(tools);
  let active=null,drop=null,drag=null,frame=0,suppressClick=false,textTarget=null,paragraphTarget=null;
  const paragraphs=()=>[...document.querySelectorAll('.pagedjs_pages [data-anchor]')];
  const sectionOf=el=>el.closest('[data-section]')?.dataset.section;
  const sendLayout=(f,changes)=>tell({type:'layout',figure:f.dataset.figure,changes});
  const button=(label,action,selected=false)=>{const b=document.createElement('button');b.type='button';b.textContent=label;b.classList.toggle('active',selected);b.onclick=action;tools.append(b);return b;};
  const hide=()=>{tools.hidden=true;active?.classList.remove('art-selected');active=null;};
  function select(f,notify=true) {
    active?.classList.remove('art-selected');active=f;f.classList.add('art-selected');tools.replaceChildren();tools.hidden=false;
    const figure=layout.figures.find(x=>x.id===f.dataset.figure);if(!figure)return;
    const label=document.createElement('span');label.textContent='ARTWORK';tools.append(label);
    for(const [style,title] of [['left','Wrap left'],['wide','Block'],['right','Wrap right']])button(title,()=>sendLayout(f,{style,width:style==='wide'?100:46}),figure.style===style);
    button('Layout',()=>tell({type:'figure-select',figure:figure.id}));
    button('Edit art',()=>tell({type:'art',figure:figure.id}));
    button('Comment',()=>tell({type:'comment',target:{kind:'figure',section:figure.section,figure:figure.id,quote:figure.title}}));
    button('×',hide).classList.add('close-tools');
    if(notify)tell({type:'figure-select',figure:figure.id});
  }
  function clearDrop(){drop?.classList.remove('drop-before','drop-after');drop=null;}
  function nearest(x,y){
    let score=Infinity,best=null;
    for(const p of paragraphs()) {const r=p.getBoundingClientRect();if(r.height<2)continue;const dx=Math.max(r.left-x,0,x-r.right),dy=Math.max(r.top-y,0,y-r.bottom),d=dy+dx*.5;if(d<score){score=d;best=p;}}
    return best;
  }
  function move(e){
    if(!drag||e.pointerId!==drag.pointer)return;drag.x=e.clientX;drag.y=e.clientY;
    if(drag.mode==='move'){
      clearDrop();drop=nearest(e.clientX,e.clientY);if(!drop)return;
      const r=drop.getBoundingClientRect(),area=drop.closest('.pagedjs_page').querySelector('.pagedjs_page_content').getBoundingClientRect();
      drag.placement=e.clientY<r.top+r.height/2?'before':'after';const x=(e.clientX-area.left)/area.width;
      drag.style=x<.32?'left':x>.68?'right':'wide';drop.classList.add(`drop-${drag.placement}`);
      drag.status.textContent=`Drop ${drag.placement} this paragraph · ${drag.style==='wide'?'full-width block':`wrap ${drag.style}`} · Esc to cancel`;
    }else{
      const dx=e.clientX-drag.startX,dy=e.clientY-drag.startY;
      drag.width=Math.min(100,Math.max(20,Math.round((drag.rect.width+dx)/drag.area.width*100)));
      drag.height=Math.min(150,Math.max(20,Math.round(drag.original.height*(drag.rect.height+dy)/drag.rect.height)));
      // A transform gives feedback without repaginating under the pointer.
      drag.figure.style.transformOrigin='top left';drag.figure.style.transform=`scale(${drag.width/drag.original.width},${drag.height/drag.original.height})`;
      drag.status.textContent=`${drag.width}% page width · ${drag.height} mm high · Release to reflow`;
    }
  }
  function scrollDrag(){if(!drag)return;const dy=drag.y<60?-12:drag.y>innerHeight-60?12:0;if(dy){scrollBy(0,dy);move({pointerId:drag.pointer,clientX:drag.x,clientY:drag.y});}frame=requestAnimationFrame(scrollDrag);}
  function finish(cancel=false){
    if(!drag)return;const d=drag;drag=null;cancelAnimationFrame(frame);d.status.remove();d.figure.style.transform='';
    if(!cancel){
      if(d.mode==='resize')sendLayout(d.figure,{width:d.width??d.original.width,height:d.height??d.original.height});
      else if(drop)sendLayout(d.figure,{section:sectionOf(drop),anchor:drop.dataset.anchor,placement:d.placement,style:d.style,width:d.style==='wide'?100:46});
    }
    clearDrop();suppressClick=true;setTimeout(()=>suppressClick=false,100);
  }
  for(const f of document.querySelectorAll('.pagedjs_pages figure[data-figure]')){
    const image=f.querySelector('img');if(!image)continue;image.draggable=false;
    for(const [mode,label,glyph] of [['move','Move illustration to a paragraph','↕'],['resize','Resize illustration','↘']]){
      const h=document.createElement('button');h.type='button';h.className=`page-handle page-${mode}`;h.setAttribute('aria-label',label);h.title=label;h.textContent=glyph;f.append(h);
      h.onpointerdown=e=>{if(e.button!==0)return;e.preventDefault();e.stopPropagation();select(f);h.setPointerCapture(e.pointerId);const original=layout.figures.find(x=>x.id===f.dataset.figure);const status=document.createElement('div');status.className='drag-status';status.textContent=mode==='move'?'Drag to a paragraph. Left or right wraps text around the artwork.':'Drag to resize. Release to reflow text.';document.body.append(status);drag={mode,pointer:e.pointerId,figure:f,startX:e.clientX,startY:e.clientY,x:e.clientX,y:e.clientY,rect:f.getBoundingClientRect(),area:f.closest('.pagedjs_page').querySelector('.pagedjs_page_content').getBoundingClientRect(),original:{height:original.height,width:original.width??(['left','right'].includes(original.style)?46:100)},status};frame=requestAnimationFrame(scrollDrag);};
      h.onkeydown=e=>{if(['Enter',' '].includes(e.key)){e.preventDefault();select(f);tell({type:'figure-select',figure:f.dataset.figure});}};
    }
    f.onclick=e=>{if(suppressClick||e.target.closest('.page-handle,.comment-pin'))return;select(f);};
    f.ondblclick=()=>tell({type:'art',figure:f.dataset.figure});
    f.onkeydown=e=>{if(e.target===f&&['Enter',' '].includes(e.key)){e.preventDefault();select(f);}};
  }
  document.addEventListener('pointermove',move);
  document.addEventListener('pointerup',()=>finish());document.addEventListener('pointercancel',()=>finish(true));
  document.addEventListener('keydown',e=>{if(e.key==='Escape'){finish(true);hide();}});
  document.addEventListener('pointerup',e=>{
    if(suppressClick||e.target.closest('.page-tools,figure,.comment-pin'))return;
    const selection=getSelection();if(!selection?.rangeCount)return;
    const quote=passageText(selection.getRangeAt(0).cloneContents());if(!quote)return;
    const node=selection.getRangeAt(0).startContainer;const p=(node.nodeType===1?node:node.parentElement).closest('[data-anchor]');if(!p)return;
    const section=sectionOf(p);textTarget={kind:'text',section,quote:quote.slice(0,2000),figure:''};paragraphTarget={section,quote:p.dataset.anchor};
    active?.classList.remove('art-selected');active=null;tools.replaceChildren();tools.hidden=false;
    button('Comment on selection',()=>tell({type:'comment',target:textTarget}));
    const hasBreak=(layout.blockBreaks||[]).some(b=>b.section===section&&b.quote===p.dataset.anchor);
    button(hasBreak?'Remove page break':'New page before paragraph',()=>tell({type:'block-break',target:paragraphTarget,enabled:!hasBreak}));
    button('×',hide).classList.add('close-tools');
  });
  // Keep text selection visible while using its floating toolbar.
  tools.onpointerdown=e=>e.preventDefault();
  document.addEventListener('click',e=>{if(e.target.closest('figure,.page-tools,.comment-pin')||getSelection()?.toString().trim())return;const section=sectionOf(e.target);if(section)tell({type:'select',section});});
  for(const t of (layout.comments||[]).filter(t=>!t.resolved)){
    let target;
    if(t.target.kind==='figure')target=[...document.querySelectorAll('[data-figure]')].find(f=>f.dataset.figure===t.target.figure&&f.querySelector('img'));
    else if(t.target.kind==='text')target=paragraphs().find(p=>sectionOf(p)===t.target.section&&p.dataset.anchor.includes(t.target.quote));
    if(!target)continue;target.classList.add('has-comments');
    const pin=document.createElement('button');pin.className='comment-pin';pin.textContent='●';pin.setAttribute('aria-label','Open comment thread');pin.onclick=e=>{e.stopPropagation();tell({type:'thread',thread:t.id,target:t.target});};target.append(pin);
  }
  window.addEventListener('message',e=>{
    if(e.origin!==location.origin||e.source!==parent||!e.data?.studio||e.data.type!=='focus-anchor')return;
    const t=e.data.target;const el=t.kind==='figure'?[...document.querySelectorAll('[data-figure]')].find(f=>f.dataset.figure===t.figure&&f.querySelector('img')):paragraphs().find(p=>sectionOf(p)===t.section&&(t.kind==='section'||p.dataset.anchor.includes(t.quote)));
    if(el){el.scrollIntoView({behavior:'smooth',block:'center'});el.classList.add('anchor-focus');setTimeout(()=>el.classList.remove('anchor-focus'),3000);}else tell({type:'anchor-missing'});
  });
}

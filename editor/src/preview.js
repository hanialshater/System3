import { Previewer } from 'pagedjs';
import MarkdownIt from 'markdown-it';
import footnote from 'markdown-it-footnote';
import DOMPurify from 'dompurify';
import {renderArt} from './art-render.js';
const md = new MarkdownIt({ html: false, typographer: false }).use(footnote);
const $ = s => document.querySelector(s);
let renderId = null;
function tell(data) { parent.postMessage({ ...data, id: renderId, studio: true }, location.origin); }
function safe(text) { return text.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
async function render(data) {
  renderId = data.id;
  const { layout, sections, fullMarkdown, chapter, zoom } = data;
  const t = layout.typography;
  const dimensions = {book:[152.4,228.6],a5:[148,210],letter:[215.9,279.4]}[t.paper];
  const [width,height] = dimensions;
  const css = `
    @font-face{font-family:Nimbus;src:url('${location.origin}/fonts/NimbusRoman-Regular.otf')}
    @font-face{font-family:Nimbus;src:url('${location.origin}/fonts/NimbusRoman-Bold.otf');font-weight:bold}
    @font-face{font-family:Nimbus;src:url('${location.origin}/fonts/NimbusRoman-Italic.otf');font-style:italic}
    @page{size:${width}mm ${height}mm;margin:${t.margin}mm;@top-left{content:'SYSTEM 3';font-family:Georgia;font-size:7pt;color:#65737d}@top-right{content:'CHAPTER ${chapter.number}';font-family:Georgia;font-size:7pt;color:#65737d}@bottom-center{content:counter(page);font-family:Georgia;font-size:8pt;color:#65737d}}
    *{box-sizing:border-box}body{margin:0;background:#e6e8ea;color:#292b2c;font-family:${t.font},serif;font-size:${t.size}pt;line-height:${t.leading}}
    .pagedjs_page{background:#fcf8ee}
    p{margin:0 0 .62em;text-align:${t.align};orphans:3;widows:3;overflow-wrap:break-word}
    h1{font-size:2.15em;line-height:1.06;font-weight:normal;letter-spacing:-.025em;margin:.3em 0 .55em;color:#273e4b}
    h2{font-size:1.65em;font-weight:normal;line-height:1.13;margin:1em 0 .6em;color:#273e4b;break-after:avoid}
    h3,h4{break-after:avoid;line-height:1.2}h2+p,h3+p{break-before:avoid}
    blockquote{margin:.8em 0 .8em 1em;border-left:2px solid #c4a66a;padding-left:.8em;font-style:italic}
    .section-break{break-before:page}.section-marker{display:none}
    figure{margin:1em 0;break-inside:avoid;clear:both}figure img{display:block;width:100%;height:100%;object-fit:contain;mix-blend-mode:multiply}
    figure.wide{width:100%}figure.left,figure.right{width:46%;clear:none;float:left;margin:.4em 1em .5em 0}figure.right{float:right;margin:.4em 0 .5em 1em}
    figure.plate{break-before:page;break-after:page;display:flex;align-items:center;justify-content:center;height:${height-t.margin*2-3}mm!important}
    code{font-size:.8em;overflow-wrap:anywhere}pre{font-size:.82em;white-space:pre-wrap;word-break:break-word;background:#eee9de;padding:.7em}
    table{border-collapse:collapse;width:100%;font-size:.8em}th,td{padding:.3em;border-bottom:1px solid #c7c0b4;text-align:left}
    a{color:inherit;text-decoration:none;overflow-wrap:anywhere}.footnotes{font-size:.78em;break-before:avoid}.footnotes-sep{border:0;border-top:1px solid #b9b2a4;margin-top:1.5em}.footnote-item p{text-align:left}.footnote-backref{display:none}
    ul,ol{padding-left:1.4em}img{max-width:100%}
  `;
  let content = '';
  const warnings=[];
  for (const section of sections) {
    const cleaned = section.markdown.replace(/^>\s*\[(?:VISUAL|DIAGRAM)[\s\S]*?\]\s*$/gm, '');
    const holder = document.createElement('div');
    // Include definitions in each section so footnotes resolve; gather rendered notes at section end.
    const definitions = fullMarkdown.match(/^\[\^[^\]]+\]:[^\n]*(?:\n(?: {2,}|\t)[^\n]*)*/gm) || [];
    holder.innerHTML = DOMPurify.sanitize(md.render(cleaned + '\n\n' + definitions.join('\n')), { FORBID_TAGS:['style','iframe','form'], FORBID_ATTR:['style'] });
    holder.querySelectorAll('img').forEach(img => { img.remove(); });
    // Scope footnote IDs to avoid collisions between independently rendered sections.
    holder.querySelectorAll('[id]').forEach(el=>el.id=`${section.id}-${el.id}`);
    holder.querySelectorAll('a[href^="#"]').forEach(el=>el.setAttribute('href',`#${section.id}-${el.getAttribute('href').slice(1)}`));
    for (const figure of layout.figures.filter(f=>f.section===section.id && f.style!=='hidden')) {
      const anchor = [...holder.querySelectorAll('p')].find(p => p.textContent.includes(figure.anchor));
      if (!anchor || !figure.anchor.trim()) { warnings.push(`“${figure.title}”: anchor passage not found.`); continue; }
      const f = document.createElement('figure'); f.className=figure.style; f.style.height=`${figure.height}mm`; f.dataset.figure=figure.id;
      let src=figure.art;
      try{src=await renderArt(figure.art,figure.edit);}catch(e){warnings.push(`“${figure.title}”: ${e.message}`);}
      f.setAttribute('role','button');f.setAttribute('tabindex','0');f.setAttribute('aria-label',`Edit artwork: ${figure.title}`);
      f.innerHTML=`<img src="${src}" alt="${safe(figure.title)}">`;
      anchor.after(f);
    }
    content+=`<section data-section="${safe(section.id)}" class="${layout.breaks.includes(section.id)?'section-break':''}">${holder.innerHTML}</section>`;
  }
  for (const f of layout.figures) if (!data.allSectionIds.includes(f.section) && f.style!=='hidden') warnings.push(`“${f.title}”: its section was renamed or removed. Reattach it in Artwork.`);
  $('#pages').innerHTML='';
  const style=document.createElement('style');style.textContent=css;document.head.append(style);
  await document.fonts.ready;
  const previewer = new Previewer();
  const blob=URL.createObjectURL(new Blob([css],{type:'text/css'}));
  try {
    const flow=await previewer.preview(content,[blob],$('#pages'));
    // Screen furniture is kept outside Paged.js, which intentionally rewrites print media rules.
    const screen=document.createElement('style');
    screen.textContent=`@media screen{body{background:#e6e8ea}.pagedjs_pages{display:flex;flex-direction:column;align-items:center;gap:24px;padding:24px 16px;zoom:${zoom/100}}.pagedjs_page{flex:none;margin:0;box-shadow:0 3px 12px #17253324}}@media print{body{background:white}.pagedjs_pages{display:block;padding:0;zoom:1}.pagedjs_page{margin:0!important;box-shadow:none;break-after:page}}`;
    document.head.append(screen);
    const artStyle=document.createElement('style');artStyle.textContent='@media screen{figure[data-figure]{position:relative;cursor:pointer}figure[data-figure]:hover,figure[data-figure]:focus-visible{outline:2px solid #417b98;outline-offset:5px}figure[data-figure]:hover::after,figure[data-figure]:focus-visible::after{content:"Edit artwork";position:absolute;right:0;top:0;background:#265c75;color:white;padding:7px 10px;font:12px system-ui;border-radius:3px;pointer-events:none}}';document.head.append(artStyle);
    tell({type:'rendered',pages:flow.total,warnings});
  }
  finally {URL.revokeObjectURL(blob);}
  document.addEventListener('click',e=>{const f=e.target.closest('[data-figure]');if(f){tell({type:'art',figure:f.dataset.figure});return;}const s=e.target.closest('[data-section]');if(s)tell({type:'select',section:s.dataset.section});});
  document.addEventListener('keydown',e=>{const f=e.target.closest('[data-figure]');if(f&&['Enter',' '].includes(e.key)){e.preventDefault();tell({type:'art',figure:f.dataset.figure});}});
}
window.addEventListener('message',e=>{
  if(e.origin!==location.origin || e.source!==parent || !e.data?.studio)return;
  if(e.data.type==='render')render(e.data).catch(error=>tell({type:'error',message:error.message}));
  if(e.data.type==='zoom'){const style=document.createElement('style');style.textContent=`@media screen{.pagedjs_pages{zoom:${Number(e.data.zoom)/100}}}`;document.head.append(style);}
  if(e.data.type==='print')window.print();
});
tell({type:'ready'});

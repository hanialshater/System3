import './style.css';
import './layout.css';
import { splitSections, joinSections, words, defaultLayout, validateLayout, layoutPath } from './model.js';
import { GitHub } from './github.js';
import {renderComments} from './comments.js';
import {renderLayoutPanel} from './layout-panel.js';
const $ = s => document.querySelector(s);
const esc = s => String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const icons={book:'▤',github:'↥'};
const github=new GitHub();
let catalog=[],chapter,sections=[],layout,selected='',tab='text',scope='section',zoom=85,timer,renderId=0,ready=false,history=[],future=[],baseMarkdown='',baseLayout=null,readBranch='main',busy=false;
let currentPageCount=0,activeFigure='',commentTarget=null,pendingFocus=null;
const art=[{url:'/art/knowledge-and-hands.webp',title:'Knowledge needs hands'},{url:'/art/clay-and-memory.webp',title:'Clay and memory'}];
const draftKey=()=>`system3-studio-v1-ch${chapter.number}`;
const section=()=>sections.find(s=>s.id===selected)||sections[0];
const snapshot=()=>JSON.stringify({sections,layout,selected});
function checkpoint(){history.push(snapshot());if(history.length>60)history.shift();future=[];}
function restore(value){const s=JSON.parse(value);sections=s.sections;layout=s.layout;selected=s.selected;refresh();changed();}
function flash(message,error=false){$('#notice').textContent=message;$('#notice').classList.toggle('error',error);$('#notice').hidden=false;}
function clearNotice(){$('#notice').hidden=true;}
function saveLocal(){try{localStorage.setItem(draftKey(),JSON.stringify({markdown:joinSections(sections),sections,layout,baseMarkdown,baseLayout,readBranch,selected,updated:Date.now()}));$('#save-state').textContent='Draft saved on this device';}catch{flash('Local storage is full. Download your draft to keep these changes.',true);}}
function changed(){saveLocal();$('#undo').disabled=!history.length;$('#redo').disabled=!future.length;$('#word-count').textContent=`${words(joinSections(sections)).toLocaleString()} words`;clearTimeout(timer);timer=setTimeout(renderPreview,550);}
function renderPreview(){
  const visible=scope==='chapter'?sections:[section()];
  if(!visible[0])return;
  const id=++renderId;ready=false;$('#render-state').textContent='Laying out pages…';$('#export').disabled=true;
  $('#preview').src=`/preview.html?render=${id}`;
}
function sendRender(){
  $('#preview').contentWindow.postMessage({studio:true,type:'render',id:renderId,layout,sections:scope==='chapter'?sections:[section()],allSectionIds:sections.map(s=>s.id),fullMarkdown:joinSections(sections),chapter:{number:chapter.number,title:chapter.title},zoom},location.origin);
}
window.addEventListener('message',e=>{
 if(e.origin!==location.origin||e.source!==$('#preview')?.contentWindow||!e.data?.studio)return;
 const d=e.data;if(d.type==='ready'){sendRender();return;}if(d.id!==renderId)return;
 if(d.type==='rendered'){ready=true;currentPageCount=d.pages;$('#render-state').textContent=`${d.pages} ${d.pages===1?'page':'pages'} · ${scope==='chapter'?'Full chapter':'Selected section'}`;$('#export').disabled=false;$('#warnings').textContent=d.warnings.join(' ');$('#warnings').hidden=!d.warnings.length;}
 if(d.type==='error'){ready=false;$('#render-state').textContent='Layout needs attention';flash(`Could not render: ${d.message}`,true);}
 if(d.type==='art'){editArtwork(d.figure);return;}
 if(d.type==='figure-select'){const f=layout.figures.find(f=>f.id===d.figure);if(f){selected=f.section;activeFigure=f.id;tab='art';refresh();const card=[...document.querySelectorAll('[data-card]')].find(el=>el.dataset.card===f.id);card?.scrollIntoView({block:'nearest'});}return;}
 if(d.type==='layout'){const f=layout.figures.find(f=>f.id===d.figure);if(!f)return;checkpoint();const c=d.changes||{};Object.assign(f,c);layout=validateLayout(layout,chapter.number);selected=layout.figures.find(x=>x.id===f.id)?.section||selected;activeFigure=f.id;tab='art';refresh();changed();return;}
 if(d.type==='comment'){openComments(d.target);return;}
 if(d.type==='thread'){openComments(d.target);const el=[...document.querySelectorAll('[data-thread]')].find(el=>el.dataset.thread===d.thread);el?.scrollIntoView({block:'center'});return;}
 if(d.type==='block-break'){checkpoint();layout.blockBreaks??=[];layout.blockBreaks=layout.blockBreaks.filter(b=>b.section!==d.target.section||b.quote!==d.target.quote);if(d.enabled)layout.blockBreaks.push(d.target);refresh();changed();return;}
 if(d.type==='anchor-missing')flash('This passage or illustration has changed. The discussion is preserved in Comments.');
 if(d.type==='rendered'&&pendingFocus){const target=pendingFocus;pendingFocus=null;$('#preview').contentWindow.postMessage({studio:true,type:'focus-anchor',target},location.origin);}
 if(d.type==='select'&&scope==='chapter'&&sections.some(s=>s.id===d.section)){selected=d.section;refresh();}
});
async function editArtwork(id){
 const figure=layout.figures.find(f=>f.id===id);if(!figure||document.querySelector('.art-dialog'))return;
 try{const {openArtEditor}=await import('./art-editor.js');await openArtEditor(figure,changes=>{checkpoint();Object.assign(figure,changes);refresh();changed();});}catch(e){flash(e.message,true);}
}
function openComments(target){commentTarget=target;selected=sections.some(s=>s.id===target.section)?target.section:selected;tab='comments';refresh();$('#comment-body')?.focus();}
function focusAnchor(target){
 if(!sections.some(s=>s.id===target.section)){flash('This section was removed. Its discussion is preserved.');return;}
 if(scope==='section'&&selected!==target.section){selected=target.section;pendingFocus=target;refresh();renderPreview();}
 else $('#preview').contentWindow.postMessage({studio:true,type:'focus-anchor',target},location.origin);
}
function changePanel(action){checkpoint();action();refresh();changed();}
function loadChapter(number){
 activeFigure='';commentTarget=null;pendingFocus=null;
 chapter=catalog.find(c=>c.number===Number(number));baseMarkdown=chapter.markdown;baseLayout=chapter.layout?JSON.stringify(chapter.layout,null,2)+'\n':null;readBranch=chapter.branch||'main';
 let draft=null;try{draft=JSON.parse(localStorage.getItem(draftKey()));}catch{}
 const text=draft?.markdown??chapter.markdown;sections=Array.isArray(draft?.sections)&&draft.sections.every(s=>typeof s.id==='string'&&typeof s.title==='string'&&typeof s.markdown==='string')?draft.sections:splitSections(text);layout=validateLayout(draft?.layout??chapter.layout,chapter.number);baseMarkdown=draft?.baseMarkdown??baseMarkdown;baseLayout=draft&&'baseLayout' in draft?draft.baseLayout:baseLayout;readBranch=draft?.readBranch??readBranch;
 selected=draft?.selected||sections.find(s=>s.title==='Civilization Had No Senku')?.id||sections[0].id;
 if(!sections.some(s=>s.id===selected))selected=sections[0].id;
 history=[];future=[];refresh();renderPreview();$('#save-state').textContent=draft?'Local draft restored':'Repository manuscript loaded';
}
function refresh(){
 $('#chapter-select').value=chapter.number;
 $('#chapter-name').textContent=chapter.title;
 $('#word-count').textContent=`${words(joinSections(sections)).toLocaleString()} words`;
 $('#section-list').innerHTML=sections.map((s,i)=>`<button class="section-item ${s.id===selected?'selected':''}" data-select="${esc(s.id)}" draggable="true" data-drag="${esc(s.id)}"><span class="section-number">${String(i+1).padStart(2,'0')}</span><span>${esc(s.title)}<small>${words(s.markdown).toLocaleString()} words${layout.breaks.includes(s.id)?' · New page':''}</small></span><span class="grip" aria-hidden="true">⠿</span></button>`).join('');
 $('#section-title').textContent=section()?.title||'';
 $('#up').disabled=sections.indexOf(section())===0;$('#down').disabled=sections.indexOf(section())===sections.length-1;
 $('#undo').disabled=!history.length;$('#redo').disabled=!future.length;
 document.querySelectorAll('[data-tab]').forEach(b=>{b.classList.toggle('active',b.dataset.tab===tab);b.setAttribute('aria-selected',String(b.dataset.tab===tab));});
 renderPanel();
}
function renderPanel(){
 const pane=$('#edit-panel');
 if(tab==='text'){
  pane.innerHTML=`<div class="panel-heading"><span>SECTION MANUSCRIPT</span><span>Markdown</span></div><textarea id="manuscript" aria-label="Section manuscript" spellcheck="true"></textarea><div class="editor-foot"><label><input type="checkbox" id="new-page" ${layout.breaks.includes(selected)?'checked':''}> Start section on a new page</label><p>Edit here. The pages update as you write.</p></div>`;
  $('#manuscript').value=section()?.markdown||'';
  let editing=false;
  $('#manuscript').addEventListener('input',e=>{
   if(!editing){checkpoint();editing=true;}const s=section();s.markdown=e.target.value;
   // Keep a separating newline so adjacent sections never merge on serialization.
   if(!s.markdown.endsWith('\n\n'))s.markdown=s.markdown.replace(/\n*$/,'')+'\n\n';
   const title=s.markdown.match(/^## (.+)$/m);if(title)s.title=title[1];
   $('#section-title').textContent=s.title;changed();
  });
  $('#manuscript').addEventListener('blur',()=>{editing=false;});
  $('#new-page').onchange=e=>{checkpoint();layout.breaks=e.target.checked?[...new Set([...layout.breaks,selected])]:layout.breaks.filter(x=>x!==selected);changed();};
 }else if(tab==='type'){
  const t=layout.typography;
  pane.innerHTML=`<div class="panel-heading"><span>CHAPTER TYPOGRAPHY</span></div><div class="settings"><label>Typeface<select id="font"><option value="Nimbus">Nimbus Roman</option><option value="Georgia">Georgia</option><option value="Palatino">Palatino</option></select></label><div class="range-label"><label for="font-size">Type size</label><output id="size-output">${t.size} pt</output></div><input id="font-size" type="range" min="9" max="16" step="0.5" value="${t.size}"><div class="range-label"><label for="leading">Line spacing</label><output id="leading-output">${t.leading}</output></div><input id="leading" type="range" min="1.15" max="1.9" step="0.01" value="${t.leading}"><div class="range-label"><label for="margin">Page margins</label><output id="margin-output">${t.margin} mm</output></div><input id="margin" type="range" min="10" max="27" step="1" value="${t.margin}"><label>Page size<select id="paper"><option value="book">Trade · 6 × 9 in</option><option value="a5">A5 · 148 × 210 mm</option><option value="letter">Letter · 8.5 × 11 in</option></select></label><label>Alignment<select id="align"><option value="justify">Justified</option><option value="left">Left aligned</option></select></label><button id="reset-type" class="secondary">Reset typography</button><p class="hint">These settings apply to the whole chapter. Text and illustrations flow into as many pages as they need.</p></div>`;
  for(const [id,key] of [['font','font'],['font-size','size'],['leading','leading'],['margin','margin'],['paper','paper'],['align','align']]){
   const el=$('#'+id);el.value=t[key];el.onchange=e=>{checkpoint();layout.typography[key]=['size','leading','margin'].includes(key)?Number(e.target.value):e.target.value;renderPanel();changed();};
   if(el.type==='range')el.oninput=e=>{const out=$('#'+({size:'size',leading:'leading',margin:'margin'}[key])+'-output');if(out)out.textContent=e.target.value+({size:' pt',margin:' mm'}[key]||'');};
  }
  $('#reset-type').onclick=()=>{checkpoint();layout.typography=defaultLayout(chapter.number).typography;renderPanel();changed();};
 }else if(tab==='comments'){
  const target=commentTarget?.section===selected?commentTarget:{kind:'section',section:selected,quote:'',figure:''};
  renderComments(pane,{layout,sections,selected,target,onChange:changePanel,onTarget:openComments,onFocus:focusAnchor,escape:esc});
 }else{
  renderLayoutPanel(pane,{layout,sections,selected,activeFigure,art,escape:esc,onChange:changePanel,onEdit:editArtwork,onComment:openComments,onFocus:focusAnchor});
 }

}
function moveSection(from,to){if(from===to||to<0||to>=sections.length)return;checkpoint();const [s]=sections.splice(from,1);sections.splice(to,0,s);refresh();changed();}
function download(name,content,type='text/plain'){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([content],{type}));a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000);}
function githubDialog(){
 $('#github-dialog').showModal();$('#read-branch').value=readBranch;$('#token').value='';$('#github-status').textContent=github.token?'Connected for this session.':'Reading is public. Saving requires a token for this repository.';
}
async function withBusy(fn){if(busy)return;busy=true;$('#github-status').textContent='Working…';document.querySelectorAll('#github-dialog button[data-action]').forEach(b=>b.disabled=true);try{await fn();}catch(e){$('#github-status').textContent=e.message;flash(e.message,true);}finally{busy=false;document.querySelectorAll('#github-dialog button[data-action]').forEach(b=>b.disabled=false);}}
async function boot(){
 $('#app').innerHTML=`<header class="topbar"><a class="brand" href="/" aria-label="Book Studio"><span class="brand-mark">S<sup>3</sup></span><span>Book Studio<small>SYSTEM 3</small></span></a><div class="save-area"><span id="save-state">Opening manuscript…</span><button class="icon-button" id="undo" aria-label="Undo" disabled>↶</button><button class="icon-button" id="redo" aria-label="Redo" disabled>↷</button></div><div class="top-actions"><button id="github" class="secondary">GitHub sync <span aria-hidden="true">↗</span></button><button id="export" class="primary" disabled>Export PDF</button></div></header><div id="notice" role="status" hidden></div><main class="workspace"><aside class="outline"><div class="outline-heading"><span>MANUSCRIPT</span><span class="edition">01–06</span></div><label class="sr-only" for="chapter-select">Chapter</label><select id="chapter-select"></select><h1 id="chapter-name"></h1><p id="word-count" class="muted"></p><div class="outline-subheading">SECTIONS <span>Drag to reorder</span></div><nav id="section-list" aria-label="Chapter sections"></nav><div class="outline-footer"><a href="https://github.com/hanialshater/System3" target="_blank" rel="noopener">hanialshater / System3 ↗</a><button id="download" class="text-button">Download draft files</button></div></aside><section class="editor"><div class="section-toolbar"><span id="section-title"></span><button class="icon-button" id="up" aria-label="Move section up">↑</button><button class="icon-button" id="down" aria-label="Move section down">↓</button></div><div class="tabs" role="tablist" aria-label="Editor controls"><button role="tab" data-tab="text" class="active">Manuscript</button><button role="tab" data-tab="type">Typography</button><button role="tab" data-tab="art">Layout & art</button><button role="tab" data-tab="comments">Comments</button></div><div id="edit-panel"></div></section><section class="proof"><div class="proof-toolbar"><div><span class="live-badge">LIVE PROOF</span><span id="render-state" aria-live="polite">Preparing…</span></div><div class="proof-controls"><label class="sr-only" for="scope">Preview scope</label><select id="scope"><option value="section">This section</option><option value="chapter">Full chapter</option></select><label class="sr-only" for="zoom">Preview zoom</label><select id="zoom"><option value="55">55%</option><option value="70">70%</option><option value="85" selected>85%</option><option value="100">100%</option></select></div></div><div id="warnings" role="status" hidden></div><iframe id="preview" title="Paginated book preview"></iframe><div class="proof-footer">Drag artwork · Select text to comment <span>Paged.js</span></div></section></main><dialog id="github-dialog"><form method="dialog"><button class="dialog-close" aria-label="Close GitHub settings">×</button></form><div class="dialog-content"><span class="eyebrow">GITHUB SYNC</span><h2>Keep the book together.</h2><p>Manuscript, layout, artwork settings, and comments save in one commit to <strong>hanialshater/System3</strong>.</p><label>Read from branch<input id="read-branch" value="main" autocomplete="off"></label><label>Save to review branch<input id="write-branch" value="book-editor/drafts" autocomplete="off"></label><label>Fine-grained access token<input id="token" type="password" placeholder="GitHub token · Contents: read and write" autocomplete="off"></label><p class="hint">Limit access to System3. The token stays in memory for this tab and goes directly to GitHub. <a href="https://github.com/settings/personal-access-tokens/new" target="_blank" rel="noopener">Create a token ↗</a></p><p id="github-status" role="status"></p><div class="dialog-actions"><button class="secondary" data-action="pull" id="pull">Pull chapter</button><button class="primary" data-action="save" id="push">Save chapter to GitHub</button></div><button id="disconnect" class="text-button">Disconnect token</button></div></dialog><dialog id="pull-confirm"><div class="dialog-content"><h2>Replace the local draft?</h2><p>Pulling replaces this chapter’s local text, layout, and comments. Download the draft first if you want to keep it.</p><div class="dialog-actions"><button id="cancel-pull" class="secondary">Cancel</button><button id="confirm-pull" class="primary">Pull and replace</button></div></div></dialog>`;
 const response=await fetch('/book/catalog.json');if(!response.ok)throw new Error('Could not load the manuscript.');catalog=await response.json();
 $('#chapter-select').innerHTML=catalog.map(c=>`<option value="${c.number}">Chapter ${c.number}</option>`).join('');
 $('#chapter-select').onchange=e=>{saveLocal();loadChapter(e.target.value);};
 $('#section-list').onclick=e=>{const b=e.target.closest('[data-select]');if(b){selected=b.dataset.select;refresh();if(scope==='section')renderPreview();}};
 let dragging;$('#section-list').ondragstart=e=>{dragging=e.target.closest('[data-drag]')?.dataset.drag;e.dataTransfer.setData('text/plain',dragging||'');};
 $('#section-list').ondragover=e=>e.preventDefault();$('#section-list').ondrop=e=>{e.preventDefault();const target=e.target.closest('[data-select]')?.dataset.select;if(target&&dragging)moveSection(sections.findIndex(s=>s.id===dragging),sections.findIndex(s=>s.id===target));};
 $('#up').onclick=()=>moveSection(sections.indexOf(section()),sections.indexOf(section())-1);$('#down').onclick=()=>moveSection(sections.indexOf(section()),sections.indexOf(section())+1);
 document.querySelectorAll('[data-tab]').forEach(b=>b.onclick=()=>{tab=b.dataset.tab;refresh();});
 $('#scope').onchange=e=>{scope=e.target.value;renderPreview();};$('#zoom').onchange=e=>{zoom=+e.target.value;$('#preview').contentWindow.postMessage({studio:true,type:'zoom',zoom},location.origin);};
 $('#undo').onclick=()=>{if(history.length){future.push(snapshot());restore(history.pop());}};$('#redo').onclick=()=>{if(future.length){history.push(snapshot());restore(future.pop());}};
 $('#download').onclick=()=>{download(chapter.path.split('/').pop(),joinSections(sections));download(`chapter-${String(chapter.number).padStart(2,'0')}.json`,JSON.stringify(layout,null,2)+'\n','application/json');};
 $('#export').onclick=()=>{if(ready)$('#preview').contentWindow.postMessage({studio:true,type:'print'},location.origin);};
 $('#github').onclick=githubDialog;
 $('#disconnect').onclick=()=>{github.token='';$('#token').value='';$('#github-status').textContent='Disconnected. Your draft remains on this device.';};
 const acceptToken=()=>{if($('#token').value.trim())github.token=$('#token').value.trim();$('#token').value='';};
 $('#pull').onclick=()=>{$('#pull-confirm').showModal();};$('#cancel-pull').onclick=()=>$('#pull-confirm').close();
 $('#confirm-pull').onclick=()=>{$('#pull-confirm').close();withBusy(async()=>{acceptToken();const branch=$('#read-branch').value.trim();const remote=await github.load(chapter.path,layoutPath(chapter.number),branch);checkpoint();baseMarkdown=remote.markdown;baseLayout=remote.rawLayout;readBranch=branch;sections=splitSections(remote.markdown);layout=validateLayout(remote.layout,chapter.number);selected=sections.find(s=>s.id===selected)?.id||sections[0].id;refresh();changed();$('#github-status').textContent=`Loaded chapter ${chapter.number} from ${branch}.`;clearNotice();});};
 $('#push').onclick=()=>withBusy(async()=>{
  acceptToken();const markdown=joinSections(sections);const savedLayout=structuredClone(layout);const branch=$('#write-branch').value.trim();
  const result=await github.save({path:chapter.path,layoutPath:layoutPath(chapter.number),markdown,layout:savedLayout,baseMarkdown,baseLayout,readBranch,writeBranch:branch});
  layout.comments=result.layout.comments;baseMarkdown=markdown;baseLayout=JSON.stringify(result.layout,null,2)+'\n';readBranch=branch;saveLocal();refresh();renderPreview();$('#read-branch').value=branch;
  $('#github-status').innerHTML=`Saved to ${esc(branch)}. <a href="${esc(result.url)}" target="_blank" rel="noopener">View commit ↗</a> · <a href="https://github.com/hanialshater/System3/compare/main...${encodeURIComponent(branch)}" target="_blank" rel="noopener">Review changes ↗</a>`;clearNotice();
 });
 if(innerWidth<800){zoom=55;$('#zoom').value='55';}
 matchMedia('(max-width:800px)').addEventListener('change',e=>{if(e.matches){zoom=55;$('#zoom').value='55';$('#preview').contentWindow.postMessage({studio:true,type:'zoom',zoom},location.origin);}});
 loadChapter(5);
}
boot().catch(e=>{document.body.innerHTML=`<main class="boot-error"><h1>Could not open Book Studio</h1><p>${esc(e.message)}</p><button onclick="location.reload()">Try again</button></main>`;});

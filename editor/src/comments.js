import {renderedPassages} from './passages.js';
// Discussion anchors belong to content, never to a transient printed page number.
export function normalizeComments(value) {
  if (!Array.isArray(value)) return [];
  const ids = new Set();
  return value.filter(t => t && typeof t.id === 'string' && t.target && typeof t.target.section === 'string' && !ids.has(t.id) && ids.add(t.id)).map(t => ({
    id: t.id.slice(0,100),
    target: {kind:['text','figure','section'].includes(t.target.kind)?t.target.kind:'section',section:t.target.section,quote:String(t.target.quote||'').slice(0,2000),figure:String(t.target.figure||'').slice(0,100)},
    resolved:!!t.resolved,
    messages:Array.isArray(t.messages)?t.messages.filter(m=>m&&typeof m.id==='string'&&typeof m.body==='string').map(m=>({id:m.id.slice(0,100),author:String(m.author||'Anonymous').slice(0,80),body:m.body.slice(0,5000),createdAt:String(m.createdAt||'').slice(0,40)})):[]
  }));
}

// Merge independent comments/replies when another collaborator saves first.
// Never silently replace an existing message with a different version.
export function mergeComments(base=[],local=[],remote=[]) {
  const result=structuredClone(remote);
  for (const thread of local) {
    const prior=base.find(t=>t.id===thread.id);
    const other=result.find(t=>t.id===thread.id);
    if (!other) { result.push(structuredClone(thread)); continue; }
    for (const key of ['target','resolved']) {
      const old=JSON.stringify(prior?.[key]),ours=JSON.stringify(thread[key]),theirs=JSON.stringify(other[key]);
      if (ours!==old && theirs!==old && ours!==theirs) throw new Error('A discussion changed in two places. Pull the shared branch before saving.');
      if (ours!==old) other[key]=structuredClone(thread[key]);
    }
    for (const message of thread.messages) {
      const existing=other.messages.find(m=>m.id===message.id);
      if (existing && JSON.stringify(existing)!==JSON.stringify(message)) throw new Error('A comment changed in two places. Pull the shared branch before saving.');
      if (!existing) other.messages.push(structuredClone(message));
    }
    other.messages.sort((a,b)=>a.createdAt.localeCompare(b.createdAt)||a.id.localeCompare(b.id));
  }
  return result;
}

export function renderComments(pane,{layout,sections,selected,target,onChange,onTarget,onFocus,escape:esc}) {
  let author='';try{author=localStorage.getItem('system3-comment-author')||'';}catch{}
  const label=t=>t.kind==='figure'?`Artwork: ${layout.figures.find(f=>f.id===t.figure)?.title||t.quote||'Removed illustration'}`:t.kind==='text'?`“${t.quote}”`:sections.find(s=>s.id===t.section)?.title||'Section';
  const fullMarkdown=sections.map(s=>s.markdown).join('');
  const textBySection=new Map();
  const missing=t=>{
    const s=sections.find(s=>s.id===t.section);if(!s)return true;
    if(t.kind==='figure')return !layout.figures.some(f=>f.id===t.figure);
    if(t.kind!=='text')return false;
    if(!textBySection.has(s.id))textBySection.set(s.id,renderedPassages(s.markdown,fullMarkdown).join('\n').replace(/\s+/g,' '));
    return !textBySection.get(s.id).includes(t.quote.replace(/\s+/g,' '));
  };
  const all=layout.comments||[];
  pane.innerHTML=`<div class="panel-heading"><span>CHAPTER DISCUSSION</span><span>${all.filter(t=>!t.resolved).length} open</span></div><div class="settings comments-panel"><p class="hint">Select text on a page, or use an illustration’s Comment button. Threads travel with the content.</p><form id="new-comment"><label>Your name<input id="comment-author" maxlength="80" placeholder="Name shown to collaborators" required value="${esc(author)}"></label><div class="comment-target">${esc(label(target))}</div>${target.kind!=='section'?'<button type="button" id="comment-section" class="text-button">Comment on section instead</button>':''}<label class="sr-only" for="comment-body">New comment</label><textarea id="comment-body" maxlength="5000" placeholder="Leave feedback, ask a question…" required></textarea><button class="primary" type="submit">Add comment</button></form><p class="hint sync-hint">Use GitHub sync to share. Collaborators pull the same review branch to see updates; independent replies merge when saved.</p><label class="resolved-toggle"><input id="show-resolved" type="checkbox"> Show resolved threads</label><div id="threads">${[...all].reverse().map(t=>`<article class="comment-thread ${t.resolved?'resolved':''}" data-thread="${esc(t.id)}" ${t.resolved?'hidden':''}><button class="thread-anchor" data-focus="${esc(t.id)}">${esc(label(t.target))}</button><small class="thread-section">${esc(sections.find(s=>s.id===t.target.section)?.title||'Removed section')}${missing(t.target)?' · Anchor changed':''}</small>${t.messages.map(m=>`<div class="comment-message"><div><strong>${esc(m.author)}</strong><time>${esc(Number.isNaN(Date.parse(m.createdAt))?'':new Date(m.createdAt).toLocaleString([],{month:'short',day:'numeric',hour:'2-digit',minute:'2-digit'}))}</time></div><p>${esc(m.body)}</p></div>`).join('')}<form data-reply="${esc(t.id)}"><label class="sr-only" for="reply-${esc(t.id)}">Reply</label><textarea id="reply-${esc(t.id)}" name="reply" maxlength="5000" placeholder="Reply…" required></textarea><div class="thread-actions"><button class="secondary" type="submit">Reply</button><button class="text-button" type="button" data-resolve="${esc(t.id)}">${t.resolved?'Reopen':'Resolve'}</button></div></form></article>`).join('')||'<p class="empty">Start the conversation.</p>'}</div></div>`;
  const name=()=>{const input=pane.querySelector('#comment-author');if(!input.value.trim()){input.focus();input.reportValidity();return null;}try{localStorage.setItem('system3-comment-author',input.value.trim());}catch{}return input.value.trim();};
  const message=(author,body)=>({id:crypto.randomUUID(),author,body:body.trim(),createdAt:new Date().toISOString()});
  pane.querySelector('#new-comment').onsubmit=e=>{e.preventDefault();const author=name(),body=pane.querySelector('#comment-body').value;if(!author||!body.trim())return;onChange(()=>{layout.comments??=[];layout.comments.push({id:crypto.randomUUID(),target:structuredClone(target),resolved:false,messages:[message(author,body)]});});};
  pane.querySelector('#comment-section')?.addEventListener('click',()=>onTarget({kind:'section',section:selected,quote:'',figure:''}));
  pane.querySelector('#show-resolved').onchange=e=>pane.querySelectorAll('.resolved').forEach(el=>el.hidden=!e.target.checked);
  pane.querySelectorAll('[data-focus]').forEach(el=>el.onclick=()=>onFocus(all.find(t=>t.id===el.dataset.focus).target));
  pane.querySelectorAll('[data-resolve]').forEach(el=>el.onclick=()=>onChange(()=>{const t=all.find(t=>t.id===el.dataset.resolve);t.resolved=!t.resolved;}));
  pane.querySelectorAll('[data-reply]').forEach(form=>form.onsubmit=e=>{e.preventDefault();const author=name(),body=form.elements.reply.value;if(!author||!body.trim())return;onChange(()=>all.find(t=>t.id===form.dataset.reply).messages.push(message(author,body)));});
}

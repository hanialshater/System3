import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile,readdir} from 'node:fs/promises';
import {splitSections,joinSections,validateLayout} from '../src/model.js';
import {GitHub} from '../src/github.js';
import {mergeComments} from '../src/comments.js';
test('all six manuscripts round-trip without loss',async()=>{
 for(const name of (await readdir('../chapters')).filter(x=>/^0[1-6]-/.test(x))){const text=await readFile('../chapters/'+name,'utf8');assert.equal(joinSections(splitSections(text)),text,name);}
});
test('headings inside code fences do not become sections',()=>{
 const text='# Chapter\n\n```python\n## not a heading\n```\n\n## Actual section\nText\n';assert.equal(splitSections(text).length,2);
});
test('section reorder moves complete text and references',()=>{
 const text='# Opening\n\n## One\nA[^a].\n\n## Two\nB.\n\n[^a]: Source.\n';const sections=splitSections(text);const reordered=[sections[0],sections[2],sections[1]];const result=joinSections(reordered);assert.ok(result.indexOf('B.')<result.indexOf('A[^a]'));assert.ok(result.includes('[^a]: Source.'));
});
test('untrusted layout values cannot inject CSS or external image URLs',()=>{
 const l=validateLayout({typography:{font:'evil; color:red',size:900},figures:[{section:'x',anchor:'y',art:'https://evil.invalid/x'}]},5);assert.equal(l.typography.font,'Nimbus');assert.equal(l.typography.size,16);assert.equal(l.figures.length,0);
});
const settings={path:'chapters/test.md',layoutPath:'book-design/editor/test.json',markdown:'new',layout:{version:1},baseMarkdown:'old',baseLayout:null,readBranch:'main',writeBranch:'book-editor/drafts'};
test('changed remote manuscript blocks every mutation',async()=>{
 const g=new GitHub();g.token='test';const calls=[];g.request=async(p,o)=>{calls.push([p,o]);return {object:{sha:'parent'}}};g.load=async()=>({markdown:'remote change',rawLayout:null});await assert.rejects(g.save(settings),/remote manuscript or layout has changed/);assert.equal(calls.filter(([,o])=>o?.method).length,0);
});
test('save commits both files atomically and never forces a branch update',async()=>{
 const g=new GitHub();g.token='test';const calls=[];g.load=async()=>({markdown:'old',rawLayout:null});g.request=async(p,o)=>{calls.push([p,o]);if(p.startsWith('git/ref/'))return {object:{sha:'parent'}};if(p==='git/commits/parent')return {tree:{sha:'tree'}};return {sha:p==='git/trees'?'new-tree':'new-commit'};};await g.save(settings);const tree=JSON.parse(calls.find(([p])=>p==='git/trees')[1].body);assert.deepEqual(tree.tree.map(x=>x.path),[settings.path,settings.layoutPath]);const patch=JSON.parse(calls.at(-1)[1].body);assert.equal(patch.force,false);assert.equal(patch.sha,'new-commit');
});
test('main cannot be saved from the editor',async()=>{
 const g=new GitHub();g.token='test';await assert.rejects(g.save({...settings,writeBranch:'main'}),/review branch/);
});

test('art edits survive layout serialization and keep the source asset',()=>{
 const input={figures:[{id:'a',section:'s',anchor:'text',art:'/art/knowledge-and-hands.webp',height:70,style:'wide',edit:{crop:{x:.2,y:.1,width:.6,height:.8},rotation:25,flipX:true,brightness:.1,contrast:.2,saturation:0,opacity:.8}}]};
 const result=validateLayout(JSON.parse(JSON.stringify(validateLayout(input,5))),5).figures[0];assert.equal(result.art,input.figures[0].art);assert.equal(result.edit.rotation,25);assert.equal(result.edit.saturation,0);assert.deepEqual(result.edit.crop,input.figures[0].edit.crop);assert.equal(result.edit.flipX,true);
});
test('out-of-bounds crops and non-finite art controls are normalized',()=>{
 const input={figures:[{section:'s',anchor:'text',art:'/art/clay-and-memory.webp',edit:{crop:{x:.9,y:-4,width:5,height:0},rotation:Infinity,brightness:'url(bad)',opacity:-1}}]};const e=validateLayout(input,5).figures[0].edit;assert.ok(e.crop.x+e.crop.width<=1);assert.equal(e.crop.y,0);assert.ok(e.crop.height>0);assert.equal(e.rotation,0);assert.equal(e.brightness,0);assert.equal(e.opacity,.1);
});

const thread=(id,body)=>({id,target:{kind:'text',section:'opening-1',quote:'Opening',figure:''},resolved:false,messages:[{id:`${id}-1`,author:'Hani',body,createdAt:'2026-09-13T10:00:00Z'}]});
test('independent threads and simultaneous replies merge without losing either contributor',()=>{
 const base=[thread('a','First')],local=structuredClone(base),remote=structuredClone(base);
 local[0].messages.push({id:'local',author:'A',body:'Local reply',createdAt:'2026-09-13T10:01:00Z'});
 remote[0].messages.push({id:'remote',author:'B',body:'Remote reply',createdAt:'2026-09-13T10:02:00Z'});
 local.push(thread('b','Second'));remote.push(thread('c','Third'));remote[0].resolved=true;
 const merged=mergeComments(base,local,remote);assert.equal(merged.length,3);assert.equal(merged[0].messages.length,3);assert.equal(merged[0].resolved,true);assert.equal(local[0].messages.length,2);
 assert.equal(mergeComments(base,merged,merged)[0].messages.length,3);
});
test('conflicting comment edits stop the save rather than overwrite a message',()=>{
 const base=[thread('a','First')],local=structuredClone(base),remote=structuredClone(base);
 local[0].messages[0].body='Local revision';remote[0].messages[0].body='Other revision';assert.throws(()=>mergeComments(base,local,remote),/changed in two places/);
});
test('layout geometry, paragraph breaks, and discussion anchors survive serialization',()=>{
 const input={figures:[{id:'a',section:'s',anchor:'A paragraph',art:'/art/clay-and-memory.webp',style:'left',height:80,width:38,gap:6,placement:'before'}],comments:[thread('t','Keep this')],blockBreaks:[{section:'s',quote:'A paragraph'}]};
 const result=validateLayout(JSON.parse(JSON.stringify(validateLayout(input,5))),5);assert.equal(result.figures[0].width,38);assert.equal(result.figures[0].placement,'before');assert.deepEqual(result.comments,input.comments);assert.deepEqual(result.blockBreaks,input.blockBreaks);
});
test('GitHub saves merge remote-only comments atomically alongside local layout edits',async()=>{
 const base={version:1,comments:[thread('a','First')]},local=structuredClone(base),remote=structuredClone(base);local.figures=[];remote.comments.push(thread('b','Collaborator comment'));
 const g=new GitHub();g.token='test';let written;
 g.load=async()=>({markdown:'old',rawLayout:JSON.stringify(remote)});
 g.request=async(p,o)=>{if(p.startsWith('git/ref/'))return{object:{sha:'parent'}};if(p==='git/commits/parent')return{tree:{sha:'tree'}};if(p==='git/trees')written=JSON.parse(o.body);return{sha:'next'};};
 const result=await g.save({...settings,layout:local,baseLayout:JSON.stringify(base)});assert.equal(result.layout.comments.length,2);assert.equal(JSON.parse(written.tree[1].content).comments[1].messages[0].body,'Collaborator comment');assert.deepEqual(result.layout.figures,[]);
});

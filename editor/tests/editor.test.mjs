import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile,readdir} from 'node:fs/promises';
import {splitSections,joinSections,validateLayout} from '../src/model.js';
import {GitHub} from '../src/github.js';
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

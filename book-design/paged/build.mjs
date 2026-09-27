import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { execFileSync } from 'node:child_process';
import { chromium } from 'playwright-core';
import { checkMasks } from './check-masks.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '../..');
const output = path.join(root, 'output/pdf/chapter-05-paged');
const scratch = path.join(root, 'tmp/pdfs/paged-ch5');
const stem = 'System3_Chapter05_Paged';
const args = new Set(process.argv.slice(2));
for (const arg of args) if (!['--status','--force','--prepare'].includes(arg)) throw new Error(`Unknown argument ${arg}`);
const python = process.env.SYSTEM3_PYTHON || path.join(root, '.venv-pdf/bin/python');
const browserPath = process.env.SYSTEM3_CHROME || ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/usr/bin/chromium', '/usr/bin/google-chrome'].find(p=>fs.existsSync(p));
if (!browserPath) throw new Error('Set SYSTEM3_CHROME to a Chromium executable');
const sha = value => crypto.createHash('sha256').update(value).digest('hex');
const arts = JSON.parse(fs.readFileSync(path.join(here,'../curated/art.json'))).filter(a=>a.chapter===5);
const inputs = ['chapters/05-the-society-of-agents.md','book-design/curated/art.json','book-design/curated/manuscript.py',
  ...['prepare.py','build.mjs','verify.py','check-masks.mjs','layout.js','proof.css','chapter-05.json','package.json','package-lock.json'].map(p=>`book-design/paged/${p}`),
  ...fs.readdirSync(path.join(here,'fonts')).sort().map(p=>`book-design/paged/fonts/${p}`),
  ...fs.readdirSync(path.join(here,'assets')).sort().map(p=>`book-design/paged/assets/${p}`),
  ...arts.map(a=>`book-design/curated/${a.file}`),'book-design/curated/assets/art/cover-078.png','book-design/curated/assets/fonts/DejaVuSansMono.ttf'];
const fingerprint = Object.fromEntries(inputs.map(p=>[p,sha(fs.readFileSync(path.join(root,p)))]));
fingerprint.runtime = execFileSync(browserPath,['--version'],{encoding:'utf8'}).trim() + ' / Node ' + process.version + ' / ' + execFileSync(python,['-c','import fitz, markdown_it; print(fitz.VersionBind, markdown_it.__version__)'],{encoding:'utf8'}).trim();
const inputHash = sha(JSON.stringify(fingerprint));
const statePath = path.join(output,'build-state.json');
const targets = [`${stem}.pdf`,`${stem}.html`,'validation.json'];
let state;
try { state = JSON.parse(fs.readFileSync(statePath)); } catch {}
const fresh = state?.inputHash === inputHash && targets.every(p=>fs.existsSync(path.join(output,p)) && sha(fs.readFileSync(path.join(output,p)))===state.outputs[p]);
if (args.has('--status')) { console.log(JSON.stringify({status:fresh?'current':'needs-build',output:path.join(output,`${stem}.pdf`)},null,2)); process.exit(0); }
if (fresh && !args.has('--force') && !args.has('--prepare')) { console.log('Chapter 5 proof is current; no rebuild.'); process.exit(0); }
fs.mkdirSync(output,{recursive:true}); fs.mkdirSync(scratch,{recursive:true});
const lock = path.join(output,'.build-lock');
let lockFd;
try { lockFd = fs.openSync(lock,'wx'); } catch { throw new Error(`Another proof build holds ${lock}; if it crashed, remove this lock and retry.`); }
let browser;
try {
  fs.writeFileSync(lockFd, String(process.pid));
  const data = JSON.parse(execFileSync(python,[path.join(here,'prepare.py')],{maxBuffer:64*1024*1024,encoding:'utf8'}));
  let fonts = '';
  for (const [file,weight,style] of [['Regular',400,'normal'],['Bold',700,'normal'],['Italic',400,'italic'],['BoldItalic',700,'italic']]) {
    const font = fs.readFileSync(path.join(here,`fonts/NimbusRoman-${file}.otf`)).toString('base64');
    fonts += `@font-face{font-family:'Nimbus Roman';font-weight:${weight};font-style:${style};src:url(data:font/otf;base64,${font}) format('opentype');font-display:block;}`;
  }
  fonts += `@font-face{font-family:'Proof Mono';src:url(data:font/ttf;base64,${fs.readFileSync(path.join(here,'../curated/assets/fonts/DejaVuSansMono.ttf')).toString('base64')}) format('truetype');font-display:block;}`;
  const css = fs.readFileSync(path.join(here,'proof.css'),'utf8');
  const mediaStart = css.indexOf('@media screen');
  const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>System 3 · Chapter 5 composition proof</title><style>${fonts}\n${css.slice(0,mediaStart)}</style><style data-pagedjs-ignore>${css.slice(mediaStart)}</style>
  <script>window.PagedConfig={auto:false};window.CHAPTER_DATA=${JSON.stringify(data).replaceAll('<','\\u003c')};</script>
  <script>${fs.readFileSync(path.join(here,'node_modules/pagedjs/dist/paged.polyfill.js'),'utf8').replaceAll('</script','<\\/script')}</script></head><body>
  <nav class="toolbar" aria-label="Proof controls"><strong>System 3 / Chapter 5</strong><span id="status">Composing pages…</span><label><input type="checkbox" id="masks">Text masks</label><label><input type="checkbox" id="spreads">Facing pages</label><button id="print">Print</button></nav>
  <aside class="legend"><span style="background:#65bc9a"></span>Available text area<br><span style="background:#ba7345"></span>Protected artwork contour<br>Text follows the contour. Each illustration has a separate silhouette mask and an intentional crop at the page edge.</aside><main id="pages"></main>
  <script>${fs.readFileSync(path.join(here,'layout.js'),'utf8')}</script></body></html>`;
  const candidateHTML = path.join(scratch,`${stem}.html`);
  fs.writeFileSync(candidateHTML,html);
  if (args.has('--prepare')) { console.log(candidateHTML); }
  else {
    console.log('Paginating Chapter 5 with Paged.js…');
    browser = await chromium.launch({executablePath:browserPath,headless:true});
    const page = await browser.newPage({viewport:{width:1400,height:1000},deviceScaleFactor:1});
    const errors = [];
    page.on('pageerror',e=>errors.push(e.message));
    page.on('console',m=>{if(m.type()==='error')errors.push(m.text());});
    await page.goto(pathToFileURL(candidateHTML).href,{waitUntil:'load',timeout:120000});
    await page.waitForFunction(()=>window.proofReady || window.proofError,{},{timeout:120000});
    const error = await page.evaluate(()=>window.proofError);
    if (error || errors.length) throw new Error(error || errors.join('\n'));
    const report = await page.evaluate(() => {
      const clean = s=>s.normalize('NFKC').replace(/\s/g,'');
      const expected = window.CHAPTER_DATA.blocks.filter(b=>b.kind!=='break').map(b=>{
        const el=document.createElement('div'); el.innerHTML=b.html;
        return {id:el.firstElementChild.dataset.block,text:clean(el.textContent)};
      });
      const failures=[];
      for(const b of expected){
        const found=[...document.querySelectorAll(`.pagedjs_page [data-block="${b.id}"]`)];
        if(clean(found.map(e=>e.textContent).join(''))!==b.text)failures.push(b.id);
      }
      const ordered=[...document.querySelectorAll('.pagedjs_page [data-block]')].map(el=>el.dataset.block).filter((id,i,list)=>i===0||id!==list[i-1]);
      if(JSON.stringify(ordered)!==JSON.stringify(expected.map(b=>b.id)))failures.push('reading-order');
      const notes=document.createElement('div');notes.innerHTML=window.CHAPTER_DATA.notes;
      if(clean(notes.textContent)!==clean([...document.querySelectorAll('.pagedjs_page .notes')].map(e=>e.textContent).join('')))failures.push('notes');
      const art=[...document.querySelectorAll('.pagedjs_page [data-art]')].map(el=>{
        const page=el.closest('.pagedjs_page');const n=+page.dataset.pageNumber;
        const side=n%2?'right':'left'; const image=el.querySelector(`.side-${side}`);
        const box=image.getBoundingClientRect(), paper=page.getBoundingClientRect();
        const spec=window.CHAPTER_DATA.art.find(a=>a.id===el.dataset.art);
        const exclusions=el.querySelector('.exclusion');
        return {id:el.dataset.art,page:n,side,mode:spec.mode,
          bleed:spec.bleed||0,
          edgeError:Math.round((side==='left'?box.left-paper.left+(spec.bleed||0):box.right-paper.right-(spec.bleed||0))*100)/100,
          float:exclusions?getComputedStyle(exclusions).float:null,shape:exclusions?getComputedStyle(exclusions).shapeOutside:null};
      });
      const reveal=[...document.querySelectorAll('.pagedjs_page p')].find(el=>el.textContent.startsWith('Each piece answered a failure'));
      const pg=reveal?.closest('.pagedjs_page');
      const first=pg?.querySelector('.pagedjs_page_content p');
      const opener=document.querySelector('.pagedjs_page .cover');
      const originalOpener=opener?.children.length===1 && opener.firstElementChild.tagName==='IMG' && opener.firstElementChild.src===window.CHAPTER_DATA.cover && opener.getBoundingClientRect().width===576 && opener.getBoundingClientRect().height===864;
      const storyPages=[...document.querySelectorAll('.story-page')].map(el=>{
        const spec=window.CHAPTER_DATA.art.find(a=>a.id===el.dataset.art);
        const bottom=Math.max(...[...el.querySelectorAll('p,h2')].map(p=>p.getBoundingClientRect().bottom))-el.getBoundingClientRect().top;
        return {id:el.dataset.art,textBottom:bottom,artTop:spec.artTop,clearance:spec.artTop-bottom};
      });
      return {pages:window.proofPageCount,blocksVerified:expected.length,textFailures:failures,art,
        noteCount:window.CHAPTER_DATA.noteCount,productionDirections:window.CHAPTER_DATA.directions.length,
        reveal:{page:Number(pg?.dataset.pageNumber),startsPage:first===reveal},
        originalOpener,storyPages,fontLoaded:document.fonts.check('16px "Nimbus Roman"')};
    });
    if(report.textFailures.length || report.art.length!==18 || !report.reveal.startsPage || !report.fontLoaded || !report.originalOpener)throw new Error(`DOM validation failed: ${JSON.stringify(report)}`);
    if(report.art.some(a=>Math.abs(a.edgeError)>1 || (a.float && a.float!==a.side)))throw new Error(`Outer-edge placement failed: ${JSON.stringify(report.art)}`);
    if(report.storyPages.some(s=>s.clearance<12))throw new Error(`Immersive scene crosses its text boundary: ${JSON.stringify(report.storyPages)}`);
    report.masks=await page.evaluate(checkMasks);
    if(report.masks.some(m=>m.overlaps.length || !m.wordsInOpenContour || m.minimumAvailableLineWidth<230))throw new Error(`Text-mask validation failed: ${JSON.stringify(report.masks)}`);
    const candidatePDF=path.join(scratch,`${stem}.pdf`);
    await page.pdf({path:candidatePDF,printBackground:true,preferCSSPageSize:true,displayHeaderFooter:false,tagged:true});
    fs.writeFileSync(path.join(scratch,'dom-validation.json'),JSON.stringify(report,null,2));
    await browser.close(); browser=null;
    const pdfReport=JSON.parse(execFileSync(python,[path.join(here,'verify.py'),candidatePDF,candidateHTML],{encoding:'utf8',maxBuffer:4*1024*1024}));
    if(pdfReport.pages!==report.pages)throw new Error('Browser and PDF page counts differ');
    report.pdf=pdfReport;
    report.inputHash=inputHash;
    if(inputs.some(p=>sha(fs.readFileSync(path.join(root,p)))!==fingerprint[p]))throw new Error('Inputs changed during the build; previous proof retained. Rebuild the current manuscript.');
    fs.writeFileSync(path.join(scratch,'validation.json'),JSON.stringify(report,null,2));
    for(const name of targets)fs.copyFileSync(path.join(scratch,name),path.join(output,`${name}.new`));
    for(const name of targets)fs.renameSync(path.join(output,`${name}.new`),path.join(output,name));
    const outputs=Object.fromEntries(targets.map(p=>[p,sha(fs.readFileSync(path.join(output,p)))]));
    fs.writeFileSync(statePath,JSON.stringify({inputHash,inputs:fingerprint,outputs,builtAt:new Date().toISOString()},null,2));
    console.log(JSON.stringify({pdf:path.join(output,`${stem}.pdf`),preview:path.join(output,`${stem}.html`),pages:report.pages,blocks:report.blocksVerified,notes:report.noteCount},null,2));
  }
} finally {
  if(browser)await browser.close();
  fs.closeSync(lockFd);fs.unlinkSync(lock);
}

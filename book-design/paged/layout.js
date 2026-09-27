/* Live text follows exclusions; SVG silhouettes or transparent derivatives reveal the art. */
const D = window.CHAPTER_DATA;
const polygon = points => `polygon(${points.map(([x,y]) => `${x}% ${y}%`).join(',')})`;
const points = p => p.map(v => v.join(',')).join(' ');
function svgArt(a, side) {
  const id = `${a.id}-${side}`;
  if (a.cutout) return `<svg class="scene-art side-${side}" role="img" aria-label="${a.label}" viewBox="0 0 100 100" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg"><image width="100" height="100" preserveAspectRatio="none" href="${a.uri}"/></svg>`;
  return `<svg class="scene-art side-${side}" role="img" aria-label="${a.label}" viewBox="0 0 100 100" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg"><defs><clipPath id="${id}-silhouette"><path d="${a.silhouette}"/></clipPath></defs><image width="100" height="100" preserveAspectRatio="none" href="${a.uri}" clip-path="url(#${id}-silhouette)"/></svg>`;
}

async function prepareProof() {
  for (const a of D.art) {
    const img = new Image(); img.src = a.uri; await img.decode();
    a.height = Math.round(a.width * img.naturalHeight / img.naturalWidth);
  }
  const groups = new Map(), wide = new Map();
  let previousEnd = -1;
  for (const a of D.art) {
    if (a.mode === 'wide' || a.mode === 'immersive') { wide.set(a.block, a); previousEnd = a.block; continue; }
    let start = a.block;
    let words = D.blocks[start].raw.split(/\s+/).length;
    while (start > previousEnd + 1 && a.block - start + 1 < a.paragraphs && D.blocks[start-1].kind === 'paragraph') {
      const more = D.blocks[start-1].raw.split(/\s+/).length;
      if (words + more > (a.mode === 'landscape' ? 340 : 250)) break;
      words += more; start--;
    }
    if (a.includeHeading && start>previousEnd+1 && D.blocks[start-1].kind==='heading_open') start--;
    if (a.sectionStart && start>0 && D.blocks[start-1].kind==='heading_open') D.blocks[start-1].html=D.blocks[start-1].html.replace('<h2','<h2 class="scene-heading"');
    groups.set(start, {...a, end: a.block});
    previousEnd = a.block;
  }
  let content = '';
  for (let i = 0; i < D.blocks.length; i++) {
    const a = groups.get(i);
    if (a) {
      const profile = D.spec.profiles[a.profile];
      const reserve = a.reserve || a.width - 60 - (a.bleed || 0) + 22;
      const sceneHeight=a.sceneHeight || a.height;
      const flow= a.mode==='contour';
      content += `<div class="scene ${flow?'contour':'story-page'} ${a.mode}" data-art="${a.id}" style="--art-width:${a.width}px;--art-height:${a.height}px;--art-top:${a.artTop||0}px;--art-bleed:${a.bleed||0}px;--scene-height:${sceneHeight}px;--reserve-width:${reserve}px;${flow?`--contour-right:${polygon(profile.right)};--contour-left:${polygon(profile.left)};`:''}">`;
      content += svgArt(a, 'left') + svgArt(a, 'right');
      if(flow) {
        content += `<div class="exclusion" aria-hidden="true"></div>`;
        for (const side of ['left','right']) content += `<svg class="mask-guide side-${side}" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><polygon points="${points(profile[side])}"/></svg>`;
      }
      content += D.blocks.slice(i,a.end+1).map(b=>b.html).join('') + '</div>';
      i = a.end;
    } else content += D.blocks[i].html;
    const w = wide.get(i);
    if (w) content += `<figure class="wide-scene ${w.mode}" data-art="${w.id}" style="--art-width:${w.width}px;--art-height:${w.height}px;--art-top:0px;--art-bleed:${w.bleed||0}px;margin-left:0;margin-right:0">${svgArt(w,'left')}${svgArt(w,'right')}</figure>`;
  }
  // The author's original chapter opener is locked: the complete image, untouched.
  const cover = `<div class="cover"><img src="${D.cover}" alt="Original Chapter 5 illustrated opener"/></div>`;
  const source = cover + `<article class="chapter">${content}${D.notes}</article>`;
  const preview = new Paged.Previewer();
  await Promise.all(['16px "Nimbus Roman"','italic 16px "Nimbus Roman"','bold 16px "Nimbus Roman"','bold italic 16px "Nimbus Roman"','12px "Proof Mono"'].map(font=>document.fonts.load(font)));
  await document.fonts.ready;
  const flow = await preview.preview(source, undefined, document.querySelector('#pages'));
  window.proofReady = true;
  window.proofPageCount = flow.total;
  document.querySelector('#status').textContent = `${flow.total} pages · 6 × 9 in`;
  if (/^#page-\d+$/.test(location.hash)) document.querySelector(location.hash)?.scrollIntoView();
}
document.querySelector('#masks').addEventListener('change', e => document.body.classList.toggle('masks',e.target.checked));
document.querySelector('#spreads').addEventListener('change', e => document.body.classList.toggle('spreads',e.target.checked));
document.querySelector('#print').addEventListener('click', () => window.print());
prepareProof().catch(e => { window.proofError = e.stack; document.querySelector('#status').textContent = e.message; console.error(e); });

// Runs in the browser after pagination, using live word boxes rather than image bounds.
export function checkMasks() {
  return [...document.querySelectorAll('.pagedjs_page .contour')].map(scene => {
    const art = window.CHAPTER_DATA.art.find(a => a.id === scene.dataset.art);
    const exclusion = scene.querySelector('.exclusion');
    const box = exclusion.getBoundingClientRect();
    const side = getComputedStyle(exclusion).float;
    const polygon = window.CHAPTER_DATA.spec.profiles[art.profile][side].map(([x,y]) => [box.x+x*box.width/100,box.y+y*box.height/100]);
    function inside(x,y) {
      let result = false;
      for (let i=0,j=polygon.length-1;i<polygon.length;j=i++) {
        const [xi,yi]=polygon[i], [xj,yj]=polygon[j];
        if (((yi>y)!==(yj>y)) && (x<(xj-xi)*(y-yi)/(yj-yi)+xi)) result=!result;
      }
      return result;
    }
    const overlaps = [];
    let wordsInOpenContour = 0;
    for (const p of scene.querySelectorAll('p')) {
      const walker = document.createTreeWalker(p,NodeFilter.SHOW_TEXT);
      let node;
      while ((node=walker.nextNode())) for (const match of node.textContent.matchAll(/\S+/g)) {
        const range=document.createRange();
        range.setStart(node,match.index);range.setEnd(node,match.index+match[0].length);
        for (const word of range.getClientRects()) {
          const y=word.y+word.height/2;
          if (y<box.top || y>box.bottom) continue;
          if ([word.left+1,(word.left+word.right)/2,word.right-1].some(x=>inside(x,y))) overlaps.push(match[0]);
          if (word.right>box.left && word.left<box.right) wordsInOpenContour++;
        }
      }
    }
    return {id:art.id,page:Number(scene.closest('.pagedjs_page').dataset.pageNumber),side,overlaps,wordsInOpenContour,
      minimumAvailableLineWidth:scene.getBoundingClientRect().width-box.width-10};
  });
}

import MarkdownIt from 'markdown-it';
import footnote from 'markdown-it-footnote';
const md=new MarkdownIt({html:false}).use(footnote);
export function passageText(element){
  const copy=element.cloneNode(true);
  copy.querySelectorAll('.footnote-ref,.footnote-backref,.comment-pin').forEach(el=>el.remove());
  return copy.textContent.trim();
}
export function renderedPassages(markdown,fullMarkdown=markdown){
  const holder=document.createElement('div');
  const definitions=fullMarkdown.match(/^\[\^[^\]]+\]:[^\n]*(?:\n(?: {2,}|\t)[^\n]*)*/gm)||[];
  holder.innerHTML=md.render(markdown+'\n\n'+definitions.join('\n'));
  return [...holder.querySelectorAll('p')].filter(p=>!p.closest('.footnotes')).map(passageText).filter(Boolean);
}

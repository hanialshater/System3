export function splitSections(markdown) {
  const lines = markdown.split(/(?<=\n)/);
  const sections = []; let chunk = ''; let title = 'Opening'; let fence = null;
  for (const line of lines) {
    const f = line.match(/^\s*(`{3,}|~{3,})/);
    if (f) { if (!fence) fence = f[1][0]; else if (f[1][0] === fence) fence = null; }
    if (!fence && /^## /.test(line)) {
      if (chunk) sections.push({ title, markdown: chunk });
      title = line.replace(/^## /, '').trim(); chunk = '';
    }
    chunk += line;
  }
  if (chunk) sections.push({ title, markdown: chunk });
  const counts = {};
  return sections.map(s => { const slug = s.title.toLowerCase().replace(/[^a-z0-9]+/g, '-'); counts[slug] = (counts[slug] || 0) + 1; return { ...s, id: `${slug}-${counts[slug]}` }; });
}
export const joinSections = sections => sections.map(s => s.markdown).join('');
export const words = text => (text.replace(/\[[^\]]*\]/g, '').match(/\b[\w’'-]+\b/g) || []).length;
export const layoutPath = number => `book-design/editor/chapter-${String(number).padStart(2, '0')}.json`;
export function defaultLayout(number) {
  return {
    version: 1,
    typography: { font: 'Nimbus', size: 11.5, leading: 1.42, margin: 17, paper: 'book', align: 'justify' },
    breaks: [],
    figures: number === 5 ? [
      { id: 'glassmaker', section: 'civilization-had-no-senku-1', anchor: 'Knowing how to produce it was only the beginning.', art: '/art/knowledge-and-hands.webp', title: 'Knowledge needs hands', style: 'wide', height: 67 },
      { id: 'clay', section: 'civilization-had-no-senku-1', anchor: 'The mark did not need to be wiser than the clerk.', art: '/art/clay-and-memory.webp', title: 'Clay and memory', style: 'right', height: 57 }
    ] : []
  };
}
export function validateLayout(input, number) {
  const base = defaultLayout(number);
  if (!input || typeof input !== 'object') return base;
  const t = input.typography || {};
  const bound = (v, min, max, fallback) => Number.isFinite(+v) ? Math.min(max, Math.max(min, +v)) : fallback;
  return {
    version: 1,
    typography: { font: ['Nimbus', 'Georgia', 'Palatino'].includes(t.font) ? t.font : base.typography.font, size: bound(t.size, 9, 16, 11.5), leading: bound(t.leading, 1.15, 1.9, 1.42), margin: bound(t.margin, 10, 27, 17), paper: ['book', 'a5', 'letter'].includes(t.paper) ? t.paper : 'book', align: t.align === 'left' ? 'left' : 'justify' },
    breaks: Array.isArray(input.breaks) ? input.breaks.filter(x => typeof x === 'string') : [],
    figures: Array.isArray(input.figures) ? input.figures.filter(f => f && typeof f.section === 'string' && typeof f.anchor === 'string' && ['/art/knowledge-and-hands.webp', '/art/clay-and-memory.webp'].includes(f.art)).map(f => ({ id: String(f.id), section: f.section, anchor: f.anchor, art: f.art, title: String(f.title || 'Illustration'), style: ['wide','left','right','plate','hidden'].includes(f.style) ? f.style : 'wide', height: bound(f.height, 30, 110, 65) })) : base.figures
  };
}

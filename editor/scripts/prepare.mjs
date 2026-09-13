import { readdir, readFile, mkdir, writeFile } from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
const root = new URL('../', import.meta.url);
const chapters = new URL('../chapters/', root);
const output = new URL('public/book/', root);
await mkdir(output, { recursive: true });
const catalog = [];
let branch = process.env.VERCEL_GIT_COMMIT_REF || '';
if (!branch) { try { branch = execFileSync('git', ['branch', '--show-current'], { encoding: 'utf8' }).trim(); } catch { branch = 'main'; } }
for (const name of (await readdir(chapters)).filter(n => /^0[1-6]-.*\.md$/.test(n)).sort()) {
  const markdown = await readFile(new URL(name, chapters), 'utf8');
  const number = Number(name.slice(0, 2));
  let layout = null;
  try { layout = JSON.parse(await readFile(new URL(`../book-design/editor/chapter-${name.slice(0, 2)}.json`, root), 'utf8')); } catch (e) { if (e.code !== 'ENOENT') throw e; }
  const entry = { number, branch, path: `chapters/${name}`, title: markdown.split('\n')[0].replace(/^# Chapter \d+: /, ''), markdown, layout };
  catalog.push(entry);
}
await writeFile(new URL('catalog.json', output), JSON.stringify(catalog));
